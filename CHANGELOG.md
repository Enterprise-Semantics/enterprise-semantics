# Changelog

All notable changes to this repository are documented in this file. Dates use
the committer's local time.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) semantics.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Dash rule: this changelog uses colons (:) and semicolons (;) only ;;; no en-dash, no em-dash.

## [Unreleased]

### Planned

- CR-ES-AG-002 ;;; register `agentic-execution` profile_type and land the corresponding Profile records (per ADR-ES-AG-001 §6).
- CR-ES-AG-003 ;;; Agentic Value Stream Candidate-status YAML record.
- CR-ES-AG-004 ;;; Agentic Workflow Candidate-status YAML record.
- Identifier registry for concept IDs.
- Concept YAML schema for concept records.

## [0.1.0] ; 2026-09-02 ; CR-ES-AG-001 Profile semantic construct

### Added

- `schema/profile.schema.json` ;;; JSON Schema (Draft 2020-12) for Profile YAML records.
- `registry/profile-types.yaml` ;;; Profile type registry (agentic-execution, autonomous-operation, example-do-not-use).
- `registry/profiles/_base.profile.yaml` ;;; Profile conventions + canonical example (self-documenting).
- `conformance/check.py` ;;; Profile conformance harness (reads YAML records, validates against schema + registry invariants, exits 0/1/2).
- `conformance/tests/test_profile_schema.py` ;;; 5-case test suite (valid, invalid id, missing provenance, unregistered profile_type, duplicate ids).
- `conformance/tests/fixtures/profile-valid.yaml` ;;; test fixture ;;; valid Profile.
- `conformance/tests/fixtures/profile-invalid-id.yaml` ;;; test fixture ;;; invalid Profile id regex.
- `conformance/tests/fixtures/profile-missing-provenance.yaml` ;;; test fixture ;;; empty provenance.
- `docs/profile.md` ;;; Profile semantic construct documentation.

### Conformance

- `python3 conformance/check.py` ;;; `NO_DRIFT (0 Profile record(s) validated)` ;;; exit 0. (No real Profiles yet ;;; agentic-execution registers in CR-ES-AG-002.)
- `python3 conformance/tests/test_profile_schema.py` ;;; `5/5 cases passed`.

### Implemented by

- CR-ES-AG-001 ;;; per ADR-ES-AG-001 §6 CR-ES-AG-001 (the Profile semantic construct).
- Authored by manny-es (the dedicated Enterprise-Semantics sub-agent).

## [0.0.1] ; 2026-09-02 ; Skeleton

### Added

- README.md (purpose, ownership, status, relationship to WSF/OpenDEA).
- CODEOWNERS (sole owner: @emmanuel-a-otchere).
- .gitignore (credential, AI-model, and workspace-noise patterns).
- LICENSE (Apache-2.0).