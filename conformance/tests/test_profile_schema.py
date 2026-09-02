"""
test_profile_schema.py ;;; tests for the Profile conformance harness.

Per CR-ES-AG-001 §3.6.

These tests use a temporary directory containing fixture YAML files
plus a synthetic profile-types.yaml and schema. They verify that the
harness detects:
  - valid records pass
  - invalid id regex fails
  - missing provenance fails
  - invalid profile_type fails (not registered)
  - duplicate ids fail

They are NOT pytest-dependent ;;; they use a tiny harness around the
check module's validation logic. To run:
  python3 conformance/tests/test_profile_schema.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Tiny self-contained Profile schema + profile-types fixture for tests.
TEST_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "Test Profile Schema",
    "type": "object",
    "required": [
        "id", "canonical_name", "definition", "status", "version",
        "profile_type", "characteristics", "governance", "provenance",
    ],
    "additionalProperties": False,
    "properties": {
        "id": {"type": "string"},
        "canonical_name": {"type": "string"},
        "definition": {"type": "string"},
        "status": {"type": "string"},
        "version": {"type": "string"},
        "profile_type": {"type": "string"},
        "characteristics": {"type": "array"},
        "governance": {"type": "string"},
        "provenance": {"type": "array"},
        "mappings": {"type": "array"},
    },
}

TEST_TYPES = {
    "profile_types": [
        {
            "id": "agentic-execution",
            "canonical_name": "Agentic Execution",
            "definition": "test",
            "governance": "enterprise-semantics",
            "status": "Established",
        },
    ],
}

VALID_PROFILE = """\
id: ES:PROFILE:test-valid
canonical_name: Test Valid Profile
definition: |
  Test profile that should pass all conformance checks.
status: Candidate
version: 0.1.0
profile_type: agentic-execution
characteristics:
  - id: ES:CHAR:test-char-1
    canonical_name: Test Characteristic 1
    description: First test characteristic.
governance: enterprise-semantics
provenance:
  - source: test
    note: test
mappings: []
"""

INVALID_ID_PROFILE = """\
id: Profile:test-invalid
canonical_name: Test Invalid ID Profile
definition: test
status: Candidate
version: 0.1.0
profile_type: agentic-execution
characteristics:
  - id: ES:CHAR:test-char-1
    canonical_name: Test Characteristic 1
    description: test
governance: enterprise-semantics
provenance:
  - source: test
mappings: []
"""

MISSING_PROVENANCE_PROFILE = """\
id: ES:PROFILE:test-missing-prov
canonical_name: Test Missing Provenance Profile
definition: test
status: Candidate
version: 0.1.0
profile_type: agentic-execution
characteristics:
  - id: ES:CHAR:test-char-1
    canonical_name: Test Characteristic 1
    description: test
governance: enterprise-semantics
provenance: []
mappings: []
"""

INVALID_PROFILE_TYPE = """\
id: ES:PROFILE:test-invalid-type
canonical_name: Test Invalid Type Profile
definition: test
status: Candidate
version: 0.1.0
profile_type: not-registered-type
characteristics:
  - id: ES:CHAR:test-char-1
    canonical_name: Test Characteristic 1
    description: test
governance: enterprise-semantics
provenance:
  - source: test
mappings: []
"""

DUPLICATE_PROFILE_1 = """\
id: ES:PROFILE:test-dup
canonical_name: Duplicate 1
definition: test
status: Candidate
version: 0.1.0
profile_type: agentic-execution
characteristics:
  - id: ES:CHAR:test-char-1
    canonical_name: Test Characteristic 1
    description: test
governance: enterprise-semantics
provenance:
  - source: test
mappings: []
"""

DUPLICATE_PROFILE_2 = DUPLICATE_PROFILE_1.replace(
    "canonical_name: Duplicate 1",
    "canonical_name: Duplicate 2",
)


def run_check_in_tmp(tmpdir: Path) -> tuple[int, str]:
    """Set up a synthetic repo and run check.py against it. Returns (exit, stdout)."""
    profiles_dir = tmpdir / "registry" / "profiles"
    types_path = tmpdir / "registry" / "profile-types.yaml"
    schema_path = tmpdir / "schema" / "profile.schema.json"
    conformance_dir = tmpdir / "conformance"
    check_src = REPO_ROOT / "conformance" / "check.py"

    profiles_dir.mkdir(parents=True)
    schema_path.parent.mkdir(parents=True)
    conformance_dir.mkdir(parents=True)

    types_path.write_text("# auto-generated test types\n" + _yaml_dump(TEST_TYPES))
    schema_path.write_text(json.dumps(TEST_SCHEMA, indent=2))

    # Copy check.py into the tmp conformance dir (it computes REPO_ROOT from
    # its own location, so we copy and let it resolve relative to tmpdir).
    shutil.copy(check_src, conformance_dir / "check.py")

    return _run_check(profiles_dir)


def _yaml_dump(obj) -> str:
    import yaml
    return yaml.safe_dump(obj, sort_keys=False)


def _run_check(profiles_dir: Path) -> tuple[int, str]:
    """Run the conformance harness against the given profiles dir."""
    conformance_dir = profiles_dir.parent.parent / "conformance"
    result = subprocess.run(
        [sys.executable, "check.py"],
        cwd=conformance_dir,
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.returncode, result.stdout + result.stderr


def assert_in(needle: str, haystack: str, label: str) -> bool:
    ok = needle in haystack
    print(f"  {'OK' if ok else 'FAIL'}: {label}")
    return ok


def case_valid_only() -> bool:
    print("Case: valid profile passes")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "registry" / "profiles").mkdir(parents=True)
        (tmp / "schema").mkdir(parents=True)
        (tmp / "conformance").mkdir(parents=True)
        import yaml as _y
        (tmp / "registry" / "profile-types.yaml").write_text(
            "# t\n" + _y.safe_dump(TEST_TYPES, sort_keys=False)
        )
        (tmp / "schema" / "profile.schema.json").write_text(json.dumps(TEST_SCHEMA))
        shutil.copy(REPO_ROOT / "conformance" / "check.py", tmp / "conformance" / "check.py")
        (tmp / "registry" / "profiles" / "ok.yaml").write_text(VALID_PROFILE)
        code, out = _run_check(tmp / "registry" / "profiles")
        return (
            assert_in("NO_DRIFT", out, "valid profile produces NO_DRIFT")
            and (code == 0)
        )


def case_invalid_id() -> bool:
    print("Case: invalid id regex fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "registry" / "profiles").mkdir(parents=True)
        (tmp / "schema").mkdir(parents=True)
        (tmp / "conformance").mkdir(parents=True)
        import yaml as _y
        (tmp / "registry" / "profile-types.yaml").write_text(
            "# t\n" + _y.safe_dump(TEST_TYPES, sort_keys=False)
        )
        (tmp / "schema" / "profile.schema.json").write_text(json.dumps(TEST_SCHEMA))
        shutil.copy(REPO_ROOT / "conformance" / "check.py", tmp / "conformance" / "check.py")
        (tmp / "registry" / "profiles" / "bad-id.yaml").write_text(INVALID_ID_PROFILE)
        code, out = _run_check(tmp / "registry" / "profiles")
        return (
            assert_in("does not match regex", out, "invalid id detected")
            and (code == 1)
        )


def case_missing_provenance() -> bool:
    print("Case: missing provenance fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "registry" / "profiles").mkdir(parents=True)
        (tmp / "schema").mkdir(parents=True)
        (tmp / "conformance").mkdir(parents=True)
        import yaml as _y
        (tmp / "registry" / "profile-types.yaml").write_text(
            "# t\n" + _y.safe_dump(TEST_TYPES, sort_keys=False)
        )
        (tmp / "schema" / "profile.schema.json").write_text(json.dumps(TEST_SCHEMA))
        shutil.copy(REPO_ROOT / "conformance" / "check.py", tmp / "conformance" / "check.py")
        (tmp / "registry" / "profiles" / "no-prov.yaml").write_text(MISSING_PROVENANCE_PROFILE)
        code, out = _run_check(tmp / "registry" / "profiles")
        return (
            assert_in("provenance must be non-empty", out, "missing provenance detected")
            and (code == 1)
        )


def case_invalid_profile_type() -> bool:
    print("Case: unregistered profile_type fails")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "registry" / "profiles").mkdir(parents=True)
        (tmp / "schema").mkdir(parents=True)
        (tmp / "conformance").mkdir(parents=True)
        import yaml as _y
        (tmp / "registry" / "profile-types.yaml").write_text(
            "# t\n" + _y.safe_dump(TEST_TYPES, sort_keys=False)
        )
        (tmp / "schema" / "profile.schema.json").write_text(json.dumps(TEST_SCHEMA))
        shutil.copy(REPO_ROOT / "conformance" / "check.py", tmp / "conformance" / "check.py")
        (tmp / "registry" / "profiles" / "bad-type.yaml").write_text(INVALID_PROFILE_TYPE)
        code, out = _run_check(tmp / "registry" / "profiles")
        return (
            assert_in("not registered", out, "unregistered profile_type detected")
            and (code == 1)
        )


def case_duplicate_ids() -> bool:
    print("Case: duplicate ids fail")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "registry" / "profiles").mkdir(parents=True)
        (tmp / "schema").mkdir(parents=True)
        (tmp / "conformance").mkdir(parents=True)
        import yaml as _y
        (tmp / "registry" / "profile-types.yaml").write_text(
            "# t\n" + _y.safe_dump(TEST_TYPES, sort_keys=False)
        )
        (tmp / "schema" / "profile.schema.json").write_text(json.dumps(TEST_SCHEMA))
        shutil.copy(REPO_ROOT / "conformance" / "check.py", tmp / "conformance" / "check.py")
        (tmp / "registry" / "profiles" / "a.yaml").write_text(DUPLICATE_PROFILE_1)
        (tmp / "registry" / "profiles" / "b.yaml").write_text(DUPLICATE_PROFILE_2)
        code, out = _run_check(tmp / "registry" / "profiles")
        return (
            assert_in("duplicate Profile id", out, "duplicate ids detected")
            and (code == 1)
        )


def main() -> int:
    cases = [
        case_valid_only,
        case_invalid_id,
        case_missing_provenance,
        case_invalid_profile_type,
        case_duplicate_ids,
    ]
    results = [c() for c in cases]
    passed = sum(results)
    total = len(results)
    print(f"\n{passed}/{total} cases passed")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())