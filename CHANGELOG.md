# Changelog

All notable changes to this repository are documented in this file. Dates use
the committer's local time.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) semantics.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Dash rule: this changelog uses colons (:) and semicolons (;) only ;;; no en-dash, no em-dash.

## [Unreleased]

### Planned

- CR-ES-AG-005 ;;; Agentic Flow.
- CR-ES-AG-008 ;;; Agentic Capability.
- CR-ES-AG-009 ;;; AI Agent (must precede CR-ES-AG-010 per FND-ES-AG-006).
- CR-ES-AG-010 ;;; Agentic Agent (conditional, gated on FND-ES-AG-006 + FND-ES-AG-009).
- CR-ES-AG-011 ;;; Agentic Service, Agentic Product, Agentic AI.
- CR-ES-AG-012 ;;; Profile conformance gate extension (cross-record checks).
- CR-ES-AG-013 ;;; First semantic release tag.

## [0.6.0] ; 2026-09-02 ; CR-ES-AG-007 Agentic Enterprise concept record

### Added

- `concepts/enterprise.concept.yaml` ;;; base Concept record (Established, v1.0.0). Specializes WSF Entity.
- `concepts/agentic-enterprise.concept.yaml` ;;; profiled Concept record (Candidate, v0.1.0). Profile binding to ES:PROFILE:agentic-execution. Profile characteristics applied across the eight enterprise areas.

### Conformance

- `python3 conformance/check_concepts.py` ;;; NO_DRIFT (8 Concept record(s) validated), exit 0.

### Implemented by

- CR-ES-AG-007 ;;; per ADR-ES-AG-001 §6.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result ;;; FND-ES-AG-005.

## [0.5.0] ; 2026-09-02 ; CR-ES-AG-006 Agentic Operations concept record

### Added

- `concepts/operations.concept.yaml` ;;; base Concept record (Established, v1.0.0). Specializes WSF Activity + references WSF Event.
- `concepts/agentic-operations.concept.yaml` ;;; profiled Concept record (Candidate, v0.1.0). Profile binding to ES:PROFILE:agentic-execution.

### Conformance

- `python3 conformance/check_concepts.py` ;;; NO_DRIFT (6 Concept record(s) validated), exit 0.

### Implemented by

- CR-ES-AG-006 ;;; per ADR-ES-AG-001 §6.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result ;;; FND-ES-AG-004.

## [0.4.0] ; 2026-09-02 ; CR-ES-AG-004 Agentic Workflow concept record

### Added

- `concepts/workflow.concept.yaml` ;;; base Concept record (status=Established, v1.0.0). Specializes WSF Activity + references WSF Event.
- `concepts/agentic-workflow.concept.yaml` ;;; profiled Concept record (status=Candidate, v0.1.0). Profile binding to `ES:PROFILE:agentic-execution`.

### Conformance

- `python3 conformance/check.py` ;;; `NO_DRIFT (1 Profile record(s) validated)`, exit 0.
- `python3 conformance/check_concepts.py` ;;; `NO_DRIFT (4 Concept record(s) validated)`, exit 0.
- `python3 conformance/tests/test_profile_schema.py` ;;; `5/5 cases passed`, exit 0.
- `python3 conformance/tests/test_concept_schema.py` ;;; `5/5 cases passed`, exit 0.

### Implemented by

- CR-ES-AG-004 ;;; per ADR-ES-AG-001 §6 CR-ES-AG-004.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result.

## [0.3.0] ; 2026-09-02 ; CR-ES-AG-003 Agentic Value Stream concept record

### Added

- `concepts/value-stream.concept.yaml` ;;; base Concept record (status=Established, v1.0.0). Specializes WSF Value.
- `concepts/agentic-value-stream.concept.yaml` ;;; profiled Concept record (status=Candidate, v0.1.0). Profile binding to `ES:PROFILE:agentic-execution`.
- `conformance/check_concepts.py` ;;; Concept conformance harness (validates against schema/concept.schema.json + enforces WSF grounding for Agentic concepts).
- `conformance/tests/test_concept_schema.py` ;;; 5-case test suite.

### Conformance

- `python3 conformance/check_concepts.py` ;;; `NO_DRIFT (4 Concept record(s) validated)`, exit 0.
- `python3 conformance/tests/test_concept_schema.py` ;;; `5/5 cases passed`, exit 0.

### Implemented by

- CR-ES-AG-003 ;;; per ADR-ES-AG-001 §6 CR-ES-AG-003.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result.

## [0.2.0] ; 2026-09-02 ; CR-ES-AG-002 agentic-execution profile_type + Profile record

### Added

- `registry/profiles/agentic-execution.profile.yaml` ;;; First governed Profile record (Established status, version 1.0.0, profile_type=agentic-execution). Carries the four governed characteristics from ADR-ES-AG-001 §3.3 (goal-directed execution under bounded autonomy, AI-augmented decision-making, adaptive behavior, human governance not human execution). Provenance cites WSF live baseline, ADR-ES-AG-001, FND-ES-AG-001 canonical, and FND-ES-AG-001-Grounding-Result.
- `schema/profile.schema.json` ;;; added `applies_to` field (optional list of base concept kinds the Profile can apply to).
- `schema/concept.schema.json` ;;; new concept schema with WSF grounding (mandatory for Agentic concepts per FND-ES-AG-001-Grounding-Result), profile_bindings, governed relationships, lifecycle status, mappings.
- `conformance/check.py` ;;; extended with applies_to validation.

### Conformance

- `python3 conformance/check.py` ;;; `NO_DRIFT (1 Profile record(s) validated)`, exit 0.
- `python3 conformance/tests/test_profile_schema.py` ;;; `5/5 cases passed`, exit 0.

### Implemented by

- CR-ES-AG-002 ;;; per ADR-ES-AG-001 §6 CR-ES-AG-002.
- Authored by manny-es (the dedicated Enterprise-Semantics sub-agent).
- Grounded per FND-ES-AG-001-Grounding-Result ;;; WSF live baseline cited explicitly in provenance.

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