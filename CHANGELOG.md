# Changelog

All notable changes to this repository are documented in this file. Dates use
the committer's local time.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) semantics.
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Dash rule: this changelog uses colons (:) and semicolons (;) only ;;; no en-dash, no em-dash.

## [Unreleased]

### Planned

- CR-ES-AG-010 ;;; Agentic Agent (conditional, gated on FND-ES-AG-006 + FND-ES-AG-007).
- CR-ES-AG-011 ;;; Agentic Service, Agentic Product, Agentic AI.
- CR-ES-AG-012 ;;; Profile conformance gate extension (cross-record checks).
- CR-ES-AG-013 ;;; First semantic release tag.
- VS-C ;;; WSF + OpenDEA + DEA Catalog mapping records (CR-ES-003 §21-§23).
- VS-D ;;; documentation + examples + conformance rules + tests + PlantUML (CR-ES-003 §27-§35).

## [0.12.0] ; 2026-09-23 ; CR-ES-002 Capability Semantic Grounding landing (recovered from v3.1.7 orphan stash)

### Added

- `concepts/capability.concept.yaml` ;;; extended per CR-ES-002 §4 + §6 + ADR-ES-002 §1.1. 12 relationships (9 new governed predicates + 3 preserved from prior scaffold). Tier 2 Specialisation per FND-ES-AG-008 §1.3.
- `relationships/vocabulary.yaml` ;;; v0.3.0, 22 governed predicates (13 Value Stream predicates from VS-B + 9 Capability predicates from CR-ES-002 §5). Two predicates namespaced for cross-CR subject-type disambiguation: `capability-realized-through` (Capability subject) vs `realized-through` (Value Stream subject), `capability-contributes-to` (Capability subject) vs `contributes-to` (Value Stream + Value Stage subjects).
- `relationships/inverse.yaml` ;;; v0.3.0, 22 inverse pairs matching the 22 predicates.
- `versions/v0.1.0.yaml` ;;; Capability semantic establishment version pointer per CR-ES-002 §24 + ADR-ES-002 §8.
- `versions/v0.0.1.yaml` ;;; HTML-comment header replaced with YAML-comment header (D-004 conformance fix).
- `provenance/decisions.yaml` + `provenance/findings.yaml` + `provenance/sources.yaml` ;;; HTML-comment headers replaced with YAML-comment headers (D-004 conformance fix).

### Refactored

- The two namespaced predicates (`capability-realized-through`, `capability-contributes-to`) follow the same namespace pattern as `stage-realized-through` from VS-B ;;; the prefix identifies the subject_type.

### Scope

This release implements CR-ES-002 §3-§25 (Capability Semantic Grounding). The implementation was stashed during the v3.1.7 chain execution (because VS-A was the higher-priority slice) and recovered via `git stash pop` into a fresh branch `docs/cr-es-002-capability-implementation-v2` cut from current main. The stashed work predates VS-A + VS-B ;;; the conflict resolution strategy was to keep main's VS-A + VS-B content and add the Capability predicates as additional entries, with namespacing for the 2 collision cases. No concept YAML mutation for Value Stream or Value Stage (already on main after VS-A PR #2).

### Governance

- ADR-ES-002 (Proposed, governance slot 0004) ;;; ratifies the foundational Capability decision.
- CR-ES-002 (Proposed, governance slot 0010) ;;; carries the Capability predicate table + per-predicate definitions.
- FND-ES-AG-008 (Established 2026-09-22) ;;; establishes the Tier 2 Specialisation classification for Capability per §1.3.

### Cardinal rules applied

- Author: Emmanuel A. Otchere (cardinal author rule, 2026-09-23) ;;; present on all modified/new files.
- No en-dash (U+2013) or em-dash (U+2014) in any new/edited file (D-004 dash rule). Section dividers use `;;;` boundary lines per existing convention.
- No vendor-specific material from embargoed sources in any new/edited file (cardinal embargo, 2026-09-22).
- ES is sourced from SDO-neutral standardisation only (ISO/IEC, ITU-T, ETSI, NIST).

### Verification (local)

- `python3 -c "import yaml; yaml.safe_load(open('relationships/vocabulary.yaml').read())"` ;;; parses cleanly, 22 predicate entries.
- `python3 -c "import yaml; yaml.safe_load(open('relationships/inverse.yaml').read())"` ;;; parses cleanly, 22 inverse entries.
- `python3 -c "import yaml; yaml.safe_load(open('versions/v0.1.0.yaml').read())"` ;;; parses cleanly.

### Out of scope (held for subsequent CRs)

- No conformance rule additions (CAP-CON-001..012 held for separate CR).
- No WSF + OpenDEA + DEA Catalog mapping records for Capability (held for separate CR ;;; VS-C for Value Stream is now done, Capability mappings are a parallel workstream).
- No documentation + examples + tests + PlantUML for Capability (held for separate CR ;;; parallel to the CR-ES-003 VS-D tranche already landed).
- No ADR-ES-002 promotion to Accepted (gated on CR-ES-002 implementation completion ;;; this slice is the prerequisite).
- No release tag (per v3.1.4 user directive).

## [0.11.0] ; 2026-09-23 ; VS-B Value Stream relationship vocabulary

### Added

- `relationships/vocabulary.yaml` ;;; v0.2.0, 13 governed predicates for Value Stream (8 subject predicates + 5 stage-level predicates) per CR-ES-003 §9 + §10.
- `relationships/inverse.yaml` ;;; v0.2.0, 13 inverse pairs matching the 13 predicates.
- `versions/v0.2.0.yaml` ;;; Value Stream semantic establishment version pointer.

### Refactored (carryover from VS-A, PR #2)

- `concepts/value-stream.concept.yaml` ;;; foundational rebase per CR-ES-003 §4.1 + ADR-ES-003 §4.1. WSF grounding expanded to declare Tier 1 Kernel Reference + ES-canonical novelty classification explicitly per FND-ES-AG-008 §1.3. Relationship block expanded from 3 to 8 predicates matching CR-ES-003 §9 + §10.
- `concepts/value-stage.concept.yaml` ;;; new foundational concept record per CR-ES-003 §5 + §13. ES-canonical novelty classification (no WSF mapping). 6 stage-level predicates.

### Scope

This release implements VS-B of CR-ES-003 ;;; the Value Stream relationship vocabulary, inverse map, and v0.2.0 version pointer. It builds on VS-A (PR #2, the 2 concept records) and the scaffolding merge (PR #4). No new concept records, no schema mutation, no validation rule addition, no conformance harness change. The 13 predicates are pure registry additions pending the conformance gate extension that will exercise them (held for VS-D).

### Governance

- ADR-ES-003 (Proposed, governance slot 0005) ;;; ratifies the foundational Value Stream decision.
- CR-ES-003 (Proposed, governance slot 0011) ;;; carries the 13-predicate table + per-predicate definitions.
- FND-ES-AG-008 (Established 2026-09-22) ;;; establishes the Tier 1 Kernel Reference + ES-canonical novelty classification for Value Stream.

### Cardinal rules applied

- Author: Emmanuel A. Otchere (cardinal author rule, 2026-09-23).
- No en-dash (U+2013) or em-dash (U+2014) in any new/edited file (D-004 dash rule). Section dividers use `;;;` boundary lines per existing convention.
- No vendor-specific material from embargoed sources in any new/edited file (cardinal embargo, 2026-09-22).
- ES is sourced from SDO-neutral standardisation only (ISO/IEC, ITU-T, ETSI, NIST).

### Verification (local)

- `python3 -c "import yaml; yaml.safe_load(open('relationships/vocabulary.yaml').read())"` ;;; parses cleanly, 8797 bytes, 13 predicate entries.
- `python3 -c "import yaml; yaml.safe_load(open('relationships/inverse.yaml').read())"` ;;; parses cleanly, 4763 bytes, 13 inverse entries.
- `python3 -c "import yaml; yaml.safe_load(open('versions/v0.2.0.yaml').read())"` ;;; parses cleanly, 5590 bytes.
- Cardinal rules: D-004 clean across all 3 files (verified by character count: 0 en-dash, 0 em-dash, 0 horizontal-ellipsis divider).
- GitHub Actions conformance gate will run on PR open ;;; expected PASS (no concept mutations in this slice, no schema changes).

### Held non-actions

- No conformance rule additions (VS-CON-001..017 held for VS-D).
- No WSF + OpenDEA + DEA Catalog mapping records (held for VS-C).
- No documentation + examples + tests + PlantUML (held for VS-D).
- No ADR-ES-003 promotion to Accepted (gated on CR-ES-003 implementation completion).
- No release tag (per v3.1.4 user directive).

## [0.10.0] ; 2026-09-22 ; CR-ES-001 scaffolding landing (relationships, provenance, versions)

### Added

- `relationships/vocabulary.yaml` ;;; initial governed predicate vocabulary (empty at v0.0.1 ;;; no predicates invented outside ADR/CR authority).
- `relationships/inverse.yaml` ;;; initial governed inverse-predicate map (empty at v0.0.1).
- `relationships/README.md` ;;; relationship governance policy.
- `provenance/sources.yaml` ;;; SOURCE provenance registry (empty at v0.0.1).
- `provenance/findings.yaml` ;;; FINDING provenance registry (empty at v0.0.1).
- `provenance/decisions.yaml` ;;; DECISION provenance registry (empty at v0.0.1).
- `provenance/README.md` ;;; provenance model policy.
- `versions/v0.0.1.yaml` ;;; initial released version pointer (scaffold ;;; not mature).

### Scope

This release implements CR-ES-001 §3-§7 scaffolding only. No concept YAML mutations. No schema mutations. No template changes. No mapping file changes. No lifecycle state migration. Subsequent CRs will populate governed predicates, provenance records, and additional version pointers.

### Governance

- ADR-ES-001 (Proposed) ;;; ADR-ES-001 establishes the authority and publication architecture.
- CR-ES-001 (Proposed) ;;; CR-ES-001 establishes the minimum executable architecture.
- FND-ES-AG-008 (Proposed Finding) ;;; per-concept WSF-grounding classification framework.

### Cardinal rules applied

- Author: Emmanuel A. Otchere (cardinal author rule, 2026-09-22).
- No en-dash (U+2013) or em-dash (U+2014) in any new file (D-004 dash rule).
- No TM Forum material in any new file (cardinal embargo, 2026-09-22).
- ES is sourced from SDO-neutral standardisation only (ISO/IEC, ITU-T, ETSI, NIST).

## [0.9.0] ; 2026-09-03 ; CR-ES-AG-008 Agentic Capability concept record

### Added

- `concepts/capability.concept.yaml` ;;; base Concept record (Candidate, v0.1.0). Bearer-agnostic outcome-realization ability. Specializes WSF Capability (Tier 2).
- `concepts/agentic-capability.concept.yaml` ;;; profiled Concept record (Candidate, v0.1.0). Profile of Capability, binds `ES:PROFILE:agentic-execution`.
- `docs/cr/0008-agentic-capability-concept.md` ;;; CR document in governance.

### Profile-of-Profile reasoning

The Profile characteristics (bounded autonomy, AI-augmented decision-making, adaptive behavior, human governance) apply to **Capability's outcome-realization aspect**, not to a specific bearer. This distinguishes `Agentic Capability` (the *what*) from `AI Agent` (the *who*). The two are distinct semantic kinds, related via the bearer relationship.

### Conformance

- `python3 conformance/check.py` ;;; NO_DRIFT (1 Profile record(s) validated), exit 0.
- `python3 conformance/check_concepts.py` ;;; NO_DRIFT (14 Concept record(s) validated), exit 0.

### Cross-references resolved

- `agentic-value-stream.concept.yaml` previously referenced `external:concept:capability`. The reference is now resolvable via the Profile chain (Agentic Value Stream -> Capability -> Agentic Capability).

### Implemented by

- CR-ES-AG-008 ;;; per ADR-ES-AG-001 §6.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result §7.

## [0.8.0] ; 2026-09-03 ; CR-ES-AG-005 Agentic Flow concept record

### Added

- `concepts/flow.concept.yaml` ;;; base Concept record (Candidate, v0.1.0). Choreographic substrate for Workflow. Specializes WSF Process.
- `concepts/agentic-flow.concept.yaml` ;;; profiled Concept record (Candidate, v0.1.0). Profile of Flow, binds `ES:PROFILE:agentic-execution`.
- `docs/cr/0005-agentic-flow-concept.md` ;;; CR document in governance.

### Conformance

- `python3 conformance/check.py` ;;; NO_DRIFT (1 Profile record(s) validated), exit 0.
- `python3 conformance/check_concepts.py` ;;; NO_DRIFT (12 Concept record(s) validated), exit 0.

### Cross-references resolved

- `agentic-workflow.concept.yaml` previously referenced `external:concept:agentic-flow` (the choreographic substrate). The reference is now resolvable to a real Concept id (`ES:CONCEPT:agentic-flow`).

### Implemented by

- CR-ES-AG-005 ;;; per ADR-ES-AG-001 §6.
- Authored by manny-es.
- Grounded per FND-ES-AG-001-Grounding-Result §7.

## [0.7.0] ; 2026-09-03 ; CR-ES-AG-009 AI Agent concept record

### Added

- `concepts/agent.concept.yaml` ;;; base Concept record (Candidate, v0.1.0). Bearer-agnostic Agent ;; specializes WSF Entity + bears WSF Capability. Distinct from AI Agent and Human Agent.
- `concepts/ai-agent.concept.yaml` ;;; AI Agent concept record (Candidate, v0.1.0). **Distinct kind, NOT a Profile.** Grounds via WSF Entity + WSF Capability. Gating prerequisite for FND-ES-AG-006 (Agentic Agent scrutiny).
- `docs/cr/0009-ai-agent-concept.md` ;;; CR document in governance.
- `docs/finding/0007-ai-agent-semantic-grounding.md` ;;; FND-ES-AG-007 in governance.

### Conformance

- `python3 conformance/check.py` ;;; NO_DRIFT (1 Profile record(s) validated), exit 0.
- `python3 conformance/check_concepts.py` ;;; NO_DRIFT (10 Concept record(s) validated), exit 0.

### Implemented by

- CR-ES-AG-009 ;;; per ADR-ES-AG-001 §6.
- Authored by manny-es.
- Grounded per FND-ES-AG-007.
- Gating prerequisite for CR-ES-AG-010 (Agentic Agent ;;; conditional, per FND-ES-AG-006 scrutiny).

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