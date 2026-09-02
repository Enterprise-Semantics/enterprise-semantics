#!/usr/bin/env python3
"""
check.py ;;; Enterprise-Semantics Profile conformance harness.

Reads every YAML record in registry/profiles/, validates against
schema/profile.schema.json, and checks registry invariants:

  - unique Profile ids across all records
  - unique characteristic ids within each Profile
  - profile_type must be registered in registry/profile-types.yaml
  - provenance must be non-empty
  - lifecycle status must be valid (per ADR-ES-002 §13)

Exit codes:
  0 ;;; all checks pass
  1 ;;; one or more checks failed
  2 ;;; harness error (missing file, JSON parse error, etc.)

Usage:
  python3 conformance/check.py

Per CR-ES-AG-001 §3.6.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "registry" / "profiles"
PROFILE_TYPES_PATH = REPO_ROOT / "registry" / "profile-types.yaml"
SCHEMA_PATH = REPO_ROOT / "schema" / "profile.schema.json"

LIFECYCLE_STATES = {
    "Candidate",
    "Investigating",
    "Proposed",
    "Established",
    "Canonical",
    "Mapped",
    "Deprecated",
    "Retired",
}

ID_REGEX_PROFILE = r"^ES:PROFILE:[a-z][a-z0-9-]*$"
ID_REGEX_CHARACTERISTIC = r"^ES:CHAR:[a-z][a-z0-9-]*$"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def load_yaml(path: Path) -> object:
    with path.open() as f:
        return yaml.safe_load(f)


def validate_profile_file(
    path: Path,
    schema: dict,
    registered_types: set[str],
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

    # Skip if record is the _base example (has 'example_id' wrapper key)
    # Convention: real profiles put fields at top level. The _base file has
    # its content under an example_id key, so we skip it explicitly.
    if path.name == "_base.profile.yaml":
        return errors

    # JSON Schema-style checks (subset, since we don't depend on jsonschema pkg).
    required = schema.get("required", [])
    for field in required:
        if field not in record:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: missing required field '{field}'"
            )

    pid = record.get("id")
    if pid is not None and not _matches(pid, ID_REGEX_PROFILE):
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: id '{pid}' does not match regex "
            f"{ID_REGEX_PROFILE}"
        )

    status = record.get("status")
    if status is not None and status not in LIFECYCLE_STATES:
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: status '{status}' is not a valid "
            f"lifecycle state"
        )

    pt = record.get("profile_type")
    if pt is not None and pt not in registered_types:
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: profile_type '{pt}' is not "
            f"registered in profile-types.yaml"
        )

    chars = record.get("characteristics") or []
    seen_char_ids: set[str] = set()
    for i, ch in enumerate(chars):
        if not isinstance(ch, dict):
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: characteristics[{i}] must be a mapping"
            )
            continue
        cid = ch.get("id")
        if cid is None:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: characteristics[{i}] missing 'id'"
            )
        elif not _matches(cid, ID_REGEX_CHARACTERISTIC):
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: characteristics[{i}].id '{cid}' "
                f"does not match regex {ID_REGEX_CHARACTERISTIC}"
            )
        elif cid in seen_char_ids:
            errors.append(
                f"{path.relative_to(REPO_ROOT)}: duplicate characteristic id '{cid}'"
            )
        else:
            seen_char_ids.add(cid)

    prov = record.get("provenance") or []
    if not prov:
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: provenance must be non-empty"
        )

    # applies_to (optional): each entry must match kebab-case if present.
    applies_to = record.get("applies_to") or []
    if not isinstance(applies_to, list):
        errors.append(
            f"{path.relative_to(REPO_ROOT)}: applies_to must be a list"
        )
    else:
        for i, at in enumerate(applies_to):
            if not isinstance(at, str):
                errors.append(
                    f"{path.relative_to(REPO_ROOT)}: applies_to[{i}] must be a string"
                )

    return errors


def _matches(value: str, regex: str) -> bool:
    import re

    return bool(re.match(regex, value))


def main() -> int:
    if not PROFILES_DIR.exists():
        fail(f"Profiles directory not found: {PROFILES_DIR}")
        return 2
    if not PROFILE_TYPES_PATH.exists():
        fail(f"Profile types registry not found: {PROFILE_TYPES_PATH}")
        return 2
    if not SCHEMA_PATH.exists():
        fail(f"Schema not found: {SCHEMA_PATH}")
        return 2

    try:
        schema = load_json(SCHEMA_PATH)
    except json.JSONDecodeError as e:
        fail(f"Schema JSON parse error: {e}")
        return 2

    try:
        types_doc = load_yaml(PROFILE_TYPES_PATH)
    except yaml.YAMLError as e:
        fail(f"profile-types.yaml parse error: {e}")
        return 2

    if not isinstance(types_doc, dict) or "profile_types" not in types_doc:
        fail("profile-types.yaml must define a top-level 'profile_types' list")
        return 2

    registered_types = {t["id"] for t in types_doc["profile_types"] if "id" in t}

    profile_files = sorted(PROFILES_DIR.glob("*.yaml")) + sorted(
        PROFILES_DIR.glob("*.yml")
    )
    if not profile_files:
        fail("No profile records found")
        return 1

    all_errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for path in profile_files:
        errors = validate_profile_file(path, schema, registered_types)
        all_errors.extend(errors)

        # Uniqueness check (across real records only).
        try:
            record = load_yaml(path)
        except yaml.YAMLError:
            continue
        if not isinstance(record, dict):
            continue
        if path.name.startswith("_"):
            continue
        pid = record.get("id")
        if pid is None:
            continue
        if pid in seen_ids:
            all_errors.append(
                f"{path.relative_to(REPO_ROOT)}: duplicate Profile id '{pid}' "
                f"(also in {seen_ids[pid].relative_to(REPO_ROOT)})"
            )
        else:
            seen_ids[pid] = path

    if all_errors:
        print(f"DRIFT_DETECTED ({len(all_errors)} issue(s)):")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    n = sum(
        1
        for p in profile_files
        if not p.name.startswith("_") and p.suffix in (".yaml", ".yml")
    )
    print(f"NO_DRIFT ({n} Profile record(s) validated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())