# Profile Semantic Construct

Per [ADR-ES-AG-001 §3](https://github.com/Enterprise-Semantics/enterprise-semantics-governance/blob/main/docs/adr/0003-agentic-semantic-decision.md), `Agentic` is a **Profile modifier**, not a new semantic kind. This document describes the Profile semantic construct that all Agentic (and future) Profiles share.

## What is a Profile?

A `Profile` is a governed configuration overlay on a base concept. It does **not** introduce a new semantic kind ;;; the base concept retains its identity. The Profile adds a governed set of characteristics that apply when the Profile is active.

```text
Profile
  subject: a base concept (e.g. Value Stream, Workflow, Operations, Enterprise)
  profile_type: a named profile family (e.g. agentic-execution, autonomous-operation)
  characteristics: a governed set of properties
  governance: which authority governs the Profile
  status: lifecycle status
```

## Why Profile?

Per ADR-ES-AG-001 §3.2, all four Agentic characteristics (bounded autonomy, AI-augmented decision-making, adaptive behavior, human governance) are **characteristics of execution**, not of the base concept's semantics. A Profile applies them without duplicating the base concept's definition.

A Profile:

- preserves the base concept's identity
- applies a governed configuration overlay
- supports governed relationships (especially the `profile-of` relationship)
- carries its own lifecycle
- can co-exist with other Profiles on the same base concept (a Value Stream can carry both Agentic and Autonomous Profiles at different lifecycle stages)

## Profile family

This repository governs a family of Profiles:

- `agentic-execution` ;;; the Agentic profile (per ADR-ES-AG-001).
- `autonomous-operation` ;;; reserved for future Autonomous semantic work.
- `example-do-not-use` ;;; documentation only.

See [`registry/profile-types.yaml`](../registry/profile-types.yaml) for the canonical registry.

## How to author a Profile record

1. Copy [`registry/profiles/_base.profile.yaml`](../registry/profiles/_base.profile.yaml) as a template.
2. Replace:
   - `id` (format `ES:PROFILE:<kebab-case-name>`)
   - `canonical_name`
   - `definition`
   - `status` (Candidate ;; Investigating ;; Proposed ;; Established ;; Canonical)
   - `version` (semver)
   - `profile_type` (must be registered in `registry/profile-types.yaml`)
   - `characteristics` (list of governed characteristics)
   - `provenance` (non-empty list of evidence sources)
   - `mappings` (list of bi-directional mappings, can be empty)
3. Save as `<profile-id>.yaml` in `registry/profiles/`.
4. Run `python3 conformance/check.py` to validate.
5. Open a PR ;;; review + accept before merge.

## Profile YAML schema

Each Profile record conforms to [`schema/profile.schema.json`](../schema/profile.schema.json). The schema enforces:

- required fields: id, canonical_name, definition, status, version, profile_type, characteristics, governance, provenance
- id format: `^ES:PROFILE:[a-z][a-z0-9-]*$`
- characteristic id format: `^ES:CHAR:[a-z][a-z0-9-]*$`
- lifecycle status from the ADR-ES-002 §13 enum
- semver version format
- profile_type from the registry
- non-empty provenance

## How to validate

From the repo root:

```bash
python3 conformance/check.py
```

Expected output on success:

```text
NO_DRIFT (N Profile record(s) validated)
```

Exit code 0 on success, 1 on any drift, 2 on harness error.

## How to run the schema tests

From the repo root:

```bash
python3 conformance/tests/test_profile_schema.py
```

Expected output on success:

```text
Case: valid profile passes
  OK: valid profile produces NO_DRIFT
Case: invalid id regex fails
  OK: invalid id detected
...
5/5 cases passed
```

## How Profile records relate to concept records

A Profile is independent of the concept records that reference it. The relationship `Agentic X profile-of X` is a governed semantic assertion between two records:

```text
Agentic X (a Profile record in registry/profiles/)
   profile-of
X (a Concept record in concepts/)
```

Concept records land in CR-ES-AG-003+ (Agentic Value Stream, Agentic Workflow, etc.).

## Profile lifecycle

Per ADR-ES-002 §13:

```text
Candidate ;; Investigating ;; Proposed ;; Established ;; Canonical ;; Mapped ;; Deprecated ;; Retired
```

Promotion rules:

- `Candidate --> Investigating` ;; landing a per-concept Finding (FND-ES-AG-NN) that supports the Profile application.
- `Investigating --> Proposed` ;; consolidated Agentic semantic review accepts the Profile application for that concept.
- `Proposed --> Established` ;; ADR-ES-AG-001 (or successor) is Accepted for the profile_type.
- `Established --> Canonical` ;; a Candidate-status concept YAML record is released.

## Related

- [ADR-ES-AG-001](https://github.com/Enterprise-Semantics/enterprise-semantics-governance/blob/main/docs/adr/0003-agentic-semantic-decision.md) ;;; Agentic Semantic Decision (Accepted 2026-09-02).
- [CR-ES-AG-001](https://github.com/Enterprise-Semantics/enterprise-semantics-governance/blob/main/docs/cr/0001-profile-semantic-construct.md) ;;; this CR.
- [ADR-ES-002](https://github.com/Enterprise-Semantics/enterprise-semantics-governance/blob/main/docs/adr/0002-enterprise-semantic-model.md) ;;; Enterprise Semantic Model.