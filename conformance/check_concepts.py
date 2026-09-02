#!/usr/bin/env python3
"""
check_concepts.py ;;; Enterprise-Semantics Concept conformance harness.

Reads every YAML record in concepts/, validates against
schema/concept.schema.json, and checks registry invariants:

  - unique Concept ids across all records
  - WSF grounding must be present for Agentic concepts (per FND-ES-AG-001
    Grounding Result ;;; ES must specialize WSF, not duplicate).
  - profile_bindings must reference existing Profile records.
  - relationship subjects/objects must be either registered Concept ids or
    external references (prefixed with 'external:').
  - lifecycle status must be valid (per ADR-ES-002 §13).

Exit codes:
  0 ;;; all checks pass
  1 ;;; one or more checks failed
  2 ;;; harness error

Usage:
  python3 conformance/check_concepts.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CONCEPTS_DIR = REPO_ROOT / "concepts"
PROFILES_DIR = REPO_ROOT / "registry" / "profiles"
SCHEMA_PATH = REPO_ROOT / "schema" / "concept.schema.json"

LIFECYCLE_STATES = {
    "Candidate", "Investigating", "Proposed", "Established",
    "Canonical", "Mapped", "Deprecated", "Retired",
}

ID_REGEX_CONCEPT = r"^ES:CONCEPT:[a-z][a-z0-9-]*$"
ID_REGEX_PROFILE = r"^ES:PROFILE:[a-z][a-z0-9-]*$"


def _matches(value: str, regex: str) -> bool:
    import re
    return bool(re.match(regex, value))


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def load_yaml(path: Path) -> object:
    with path.open() as f:
        return yaml.safe_load(f)


def collect_profile_ids() -> set[str]:
    """Read all Profile records and return their ids."""
    ids: set[str] = set()
    if not PROFILES_DIR.exists():
        return ids
    for path in sorted(PROFILES_DIR.glob("*.yaml")) + sorted(PROFILES_DIR.glob("*.yml")):
        if path.name.startswith("_"):
            continue
        try:
            rec = load_yaml(path)
        except yaml.YAMLError:
            continue
        if isinstance(rec, dict) and "id" in rec and isinstance(rec["id"], str):
            ids.add(rec["id"])
    return ids


def collect_concept_ids() -> set[str]:
    """Read all Concept records (excluding this run's validation) and return their ids."""
    ids: set[str] = set()
    if not CONCEPTS_DIR.exists():
        return ids
    for path in sorted(CONCEPTS_DIR.glob("*.yaml")) + sorted(CONCEPTS_DIR.glob("*.yml")):
        try:
            rec = load_yaml(path)
        except yaml.YAMLError:
            continue
        if isinstance(rec, dict) and "id" in rec and isinstance(rec["id"], str):
            ids.add(rec["id"])
    return ids


def validate_concept_file(
    path: Path,
    schema: dict,
    profile_ids: set[str],
    concept_ids: set[str],
) -> list[str]:
    errors: list[str] = []

    # Skip convention/documentation files (start with _)
    if path.name.startswith("_"):
        return errors

    try:
        record = load_yaml(path)
    except yaml.YAMLError as e:
        return [f"{path.relative_to(REPO_ROOT)}: YAML parse error: {e}"]

    if not isinstance(record, dict):
        return [f"{path.relative_to(REPO_ROOT)}: top-level must be a mapping"]

    rel = str(path.relative_to(REPO_ROOT))

    required = schema.get("required", [])
    for field in required:
        if field not in record:
            errors.append(f"{rel}: missing required field '{field}'")

    cid = record.get("id")
    if cid is not None and not _matches(cid, ID_REGEX_CONCEPT):
        errors.append(f"{rel}: id '{cid}' does not match regex {ID_REGEX_CONCEPT}")

    status = record.get("status")
    if status is not None and status not in LIFECYCLE_STATES:
        errors.append(f"{rel}: status '{status}' is not a valid lifecycle state")

    # FND-ES-AG-001-Grounding-Result ;;; WSF grounding is mandatory for Agentic
    # concepts. We enforce this only for Concepts with profile_bindings to a
    # Profile of profile_type=agentic-execution.
    pbs = record.get("profile_bindings") or []
    is_agentic = any(
        isinstance(pb, dict) and pb.get("profile_type") == "agentic-execution"
        for pb in pbs
    )
    if is_agentic:
        grounding = record.get("wsf_grounding") or []
        if not grounding:
            errors.append(
                f"{rel}: Agentic concepts must declare WSF grounding "
                f"(per FND-ES-AG-001-Grounding-Result)"
            )

    # profile_bindings ;;; each profile_id must reference an existing Profile
    for i, pb in enumerate(pbs):
        if not isinstance(pb, dict):
            errors.append(f"{rel}: profile_bindings[{i}] must be a mapping")
            continue
        pid = pb.get("profile_id")
        if pid is not None and pid not in profile_ids:
            errors.append(
                f"{rel}: profile_bindings[{i}].profile_id '{pid}' does not "
                f"reference an existing Profile record"
            )

    # relationships ;;; subject/object must be Concept ids or external references
    rels = record.get("relationships") or []
    for i, rel_obj in enumerate(rels):
        if not isinstance(rel_obj, dict):
            errors.append(f"{rel}: relationships[{i}] must be a mapping")
            continue
        for side in ("subject", "object"):
            v = rel_obj.get(side)
            if v is None:
                continue
            if isinstance(v, str) and v.startswith("external:"):
                continue
            if isinstance(v, str) and v in concept_ids:
                continue
            errors.append(
                f"{rel}: relationships[{i}].{side} '{v}' must be either a "
                f"Concept id or prefixed with 'external:'"
            )

    prov = record.get("provenance") or []
    if not prov:
        errors.append(f"{rel}: provenance must be non-empty")

    return errors


def main() -> int:
    if not CONCEPTS_DIR.exists():
        # No concepts yet ;;; report but don't fail.
        print("NO_DRIFT (0 Concept record(s) validated)")
        return 0
    if not SCHEMA_PATH.exists():
        print(f"FAIL: Concept schema not found: {SCHEMA_PATH}")
        return 2

    try:
        schema = load_json(SCHEMA_PATH)
    except json.JSONDecodeError as e:
        print(f"FAIL: Concept schema JSON parse error: {e}")
        return 2

    profile_ids = collect_profile_ids()
    concept_ids = collect_concept_ids()

    concept_files = sorted(CONCEPTS_DIR.glob("*.yaml")) + sorted(CONCEPTS_DIR.glob("*.yml"))
    all_errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for path in concept_files:
        errors = validate_concept_file(path, schema, profile_ids, concept_ids)
        all_errors.extend(errors)

        try:
            record = load_yaml(path)
        except yaml.YAMLError:
            continue
        if not isinstance(record, dict):
            continue
        if path.name.startswith("_"):
            continue
        cid = record.get("id")
        if cid is None:
            continue
        if cid in seen_ids:
            all_errors.append(
                f"{path.relative_to(REPO_ROOT)}: duplicate Concept id '{cid}' "
                f"(also in { seen_ids[cid].relative_to(REPO_ROOT) })"
            )
        else:
            seen_ids[cid] = path

    if all_errors:
        print(f"DRIFT_DETECTED ({len(all_errors)} issue(s)):")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    n = sum(
        1 for p in concept_files
        if not p.name.startswith("_") and p.suffix in (".yaml", ".yml")
    )
    print(f"NO_DRIFT ({n} Concept record(s) validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())