"""
test_concept_schema.py ;;; tests for the Concept conformance harness.

Per CR-ES-AG-003 §3 (conformance harness extension).

These tests use a temporary directory containing fixture YAML files plus a
synthetic profile-types + concept-schema. They verify that the Concept
harness detects:
  - valid concept passes
  - invalid concept id fails
  - Agentic concept without WSF grounding fails (per FND-ES-AG-001-Grounding-Result)
  - profile_binding to nonexistent profile fails
  - relationship subject to unknown concept fails

Usage:
  python3 conformance/tests/test_concept_schema.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent.parent

CONCEPT_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Test Concept Schema",
    "type": "object",
    "required": [
        "id", "canonical_name", "definition", "status", "version",
        "concept_type", "governance", "provenance",
    ],
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string"},
        "canonical_name": {"type": "string"},
        "definition": {"type": "string"},
        "status": {"type": "string"},
        "version": {"type": "string"},
        "concept_type": {"type": "string"},
        "wsf_grounding": {"type": "array"},
        "profile_bindings": {"type": "array"},
        "relationships": {"type": "array"},
        "governance": {"type": "string"},
        "provenance": {"type": "array"},
    },
}

PROFILE_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Test Profile Schema",
    "type": "object",
    "required": ["id", "status", "version", "profile_type", "characteristics", "governance", "provenance"],
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string"},
        "profile_type": {"type": "string"},
    },
}

PROFILE_TYPES = {"profile_types": [
    {"id": "agentic-execution", "governance": "enterprise-semantics", "status": "Established"},
]}

VALID_CONCEPT = """\
id: ES:CONCEPT:test-valid
canonical_name: Test Valid Concept
definition: Test
status: Candidate
version: 0.1.0
concept_type: value-stream
wsf_grounding:
  - wsf_concept_id: external:wsf:Value
    relationship: specializes
profile_bindings: []
relationships: []
governance: enterprise-semantics
provenance:
  - source: test
"""

AGENTIC_WITHOUT_GROUNDING = """\
id: ES:CONCEPT:test-agentic-no-grounding
canonical_name: Test Agentic Concept Without WSF Grounding
definition: Test
status: Candidate
version: 0.1.0
concept_type: agentic-value-stream
profile_bindings:
  - profile_id: ES:PROFILE:agentic-execution
    profile_type: agentic-execution
    active: true
wsf_grounding: []
relationships: []
governance: enterprise-semantics
provenance:
  - source: test
"""

INVALID_ID_CONCEPT = """\
id: Concept:test-invalid
canonical_name: Test Invalid ID Concept
definition: Test
status: Candidate
version: 0.1.0
concept_type: workflow
wsf_grounding: []
profile_bindings: []
relationships: []
governance: enterprise-semantics
provenance:
  - source: test
"""

PROFILE_BINDING_TO_NONEXISTENT = """\
id: ES:CONCEPT:test-bad-profile-binding
canonical_name: Test Bad Profile Binding
definition: Test
status: Candidate
version: 0.1.0
concept_type: agentic-workflow
wsf_grounding:
  - wsf_concept_id: external:wsf:Activity
    relationship: references
profile_bindings:
  - profile_id: ES:PROFILE:does-not-exist
    profile_type: agentic-execution
    active: true
relationships: []
governance: enterprise-semantics
provenance:
  - source: test
"""

RELATIONSHIP_TO_UNKNOWN = """\
id: ES:CONCEPT:test-unknown-rel
canonical_name: Test Unknown Relationship
definition: Test
status: Candidate
version: 0.1.0
concept_type: value-stream
wsf_grounding: []
profile_bindings: []
relationships:
  - subject: ES:CONCEPT:value-stream
    predicate: profile-of
    object: ES:CONCEPT:does-not-exist
    status: provisional
governance: enterprise-semantics
provenance:
  - source: test
"""

VALID_PROFILE = """\
id: ES:PROFILE:agentic-execution
canonical_name: Agentic Execution Profile
definition: Test
status: Established
version: 1.0.0
profile_type: agentic-execution
characteristics:
  - id: ES:CHAR:char-1
    canonical_name: Characteristic 1
    description: Test
governance: enterprise-semantics
provenance:
  - source: test
"""


def _yaml_dump(obj):
    import yaml
    return yaml.safe_dump(obj, sort_keys=False)


def setup_tmp(tmp: Path):
    """Set up a synthetic repo with one valid Profile + zero concepts initially."""
    profiles_dir = tmp / "registry" / "profiles"
    types_path = tmp / "registry" / "profile-types.yaml"
    schema_concept = tmp / "schema" / "concept.schema.json"
    schema_profile = tmp / "schema" / "profile.schema.json"
    conformance = tmp / "conformance"
    concepts_dir = tmp / "concepts"

    profiles_dir.mkdir(parents=True)
    schema_concept.parent.mkdir(parents=True)
    conformance.mkdir(parents=True)
    concepts_dir.mkdir(parents=True)

    (types_path).write_text("# t\n" + _yaml_dump(PROFILE_TYPES))
    (schema_concept).write_text(json.dumps(CONCEPT_SCHEMA))
    (schema_profile).write_text(json.dumps(PROFILE_SCHEMA))
    (profiles_dir / "agentic-execution.profile.yaml").write_text(VALID_PROFILE)
    shutil.copy(REPO_ROOT / "conformance" / "check.py", conformance / "check.py")
    shutil.copy(REPO_ROOT / "conformance" / "check_concepts.py", conformance / "check_concepts.py")


def run_check(tmp: Path, fixture_name: str, fixture_content: str):
    (tmp / "concepts" / f"{fixture_name}.yaml").write_text(fixture_content)
    result = subprocess.run(
        [sys.executable, "check_concepts.py"],
        cwd=tmp / "conformance",
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.returncode, result.stdout + result.stderr


def assert_in(needle: str, haystack: str, label: str) -> bool:
    ok = needle in haystack
    print(f"  {'OK' if ok else 'FAIL'}: {label}")
    return ok


def case_valid():
    print("Case: valid concept passes")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        setup_tmp(tmp)
        code, out = run_check(tmp, "ok", VALID_CONCEPT)
        return assert_in("NO_DRIFT", out, "valid concept produces NO_DRIFT") and code == 0


def case_agentic_without_grounding():
    print("Case: agentic concept without WSF grounding fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        setup_tmp(tmp)
        code, out = run_check(tmp, "agentic-bad", AGENTIC_WITHOUT_GROUNDING)
        return (
            assert_in("must declare WSF grounding", out, "missing WSF grounding detected")
            and code == 1
        )


def case_invalid_id():
    print("Case: invalid concept id fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        setup_tmp(tmp)
        code, out = run_check(tmp, "bad-id", INVALID_ID_CONCEPT)
        return (
            assert_in("does not match regex", out, "invalid id detected")
            and code == 1
        )


def case_profile_binding_to_nonexistent():
    print("Case: profile_binding to nonexistent profile fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        setup_tmp(tmp)
        code, out = run_check(tmp, "bad-binding", PROFILE_BINDING_TO_NONEXISTENT)
        return (
            assert_in("does not reference an existing Profile", out, "bad binding detected")
            and code == 1
        )


def case_relationship_to_unknown():
    print("Case: relationship to unknown concept fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        setup_tmp(tmp)
        code, out = run_check(tmp, "bad-rel", RELATIONSHIP_TO_UNKNOWN)
        return (
            assert_in("must be either a Concept id", out, "unknown relationship target detected")
            and code == 1
        )


def main():
    cases = [
        case_valid,
        case_agentic_without_grounding,
        case_invalid_id,
        case_profile_binding_to_nonexistent,
        case_relationship_to_unknown,
    ]
    results = [c() for c in cases]
    passed = sum(results)
    total = len(results)
    print(f"\n{passed}/{total} cases passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())