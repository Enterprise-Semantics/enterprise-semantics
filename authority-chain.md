# Enterprise-Semantics Authority Chain

## Status: Established 2026-09-28 (user-authoritative model)

This document captures the cross-program authority chain as of the user-authoritative model landed 2026-09-28.

## Cross-Program Authority

```
WSF (World-Semantic-Foundation)
    Tier 3 Baseline (Tier 3 foundational concepts)
    |
    +--- wsf:CULTURE      [ADR-WSF-33, Baseline]
    +--- wsf:SYSTEM       [ADR-WSF-34, Baseline]
    +--- wsf:ECOSYSTEM    [ADR-WSF-28, Baseline]
    +--- wsf:NETWORK      [ADR-WSF-37, Baseline ; semantic-kind declaration]
    +--- wsf:CLOSED_LOOP  [ADR-WSF-38, Baseline ; semantic-kind declaration]
    +--- wsf:SERVICE      [ADR-WSF-35, Baseline]
    +--- wsf:PRODUCT      [ADR-WSF-36, Baseline]
    |
    ->
Enterprise-Semantics
    Semantic specializations + canonical concepts (per user model)
    |
    +--- ES-023 / ES-024  Agentic / Autonomous Culture      [Final]
    +--- ES-025 / ES-028  Agentic / Autonomous System       [Final]
    +--- ES-029           Agentic Ecosystem                  [Final]
    +--- ES-030           Autonomous Ecosystem               [Final]    (was ES-033, re-id 2026-09-28)
    +--- ES-031           Agentic Network                    [Proposed] (semantic_kind: specialization_of_canonical)
    +--- ES-032           Autonomous Network                 [Proposed] (semantic_kind: specialization_of_canonical)
    +--- ES-031-SVC       WSF Service integration            [Accepted] (compound ID per Part C 16C)
    +--- ES-032-PRD       WSF Product integration            [Accepted] (compound ID per Part C 16C)
    +--- ES-033           Loop Engineering                   [Proposed] (semantic_kind: engineering_practice)
    +--- ES-034           Closed Loop                        [Proposed] (semantic_kind: behavioral_pattern)
    +--- ES-035           Autonomous Closed Loop             [Proposed] (semantic_kind: behavioral_pattern_specialization)
    |
    +--- ES-036..041      6 Disposition Recons
    |       AI Closed Loop (canonical-reject, profile)
    |       AI Agent (technology-qualified Agent profile)
    |       Agentic AI (technology characteristic, canonical-reject)
    |       AIOps (operational discipline profile)
    |       MLOps (engineering discipline profile)
    |       AI-Native Operations (substrate characteristic profile)
```

## Semantic Kind Taxonomy

Per user-authoritative model, ES-side concepts declare their semantic_kind:

- canonical_specialization: specialization of a canonical foundation (Agentic Network, Autonomous Network, ES-014..017 Service/Product specializations)
- engineering_practice: Loop Engineering (designs/improves Closed Loop)
- behavioral_pattern: Closed Loop (cross-context, instantiable in Process/Workflow/Service/System/Operations/Network/Ecosystem/Enterprise)
- behavioral_pattern_specialization: Autonomous Closed Loop (specialization of Closed Loop)
- foundational_reference: WSF-side base concept reference stub (e.g. service.concept.yaml as reference to ES-031-SVC)

## Voided Tranches (superseded 2026-09-28)

The following tranches were voided in favor of the user-authoritative model:

- ES-034 (was Network integration ; superseded by ES-031 + ES-032 specialization pair)
- ES-035 (was Closed Loop integration ; superseded by ES-034 behavioral_pattern + ES-035 specialization)

See governance docs/superseded/ for the voided files (status header: Voided, superseding decision noted).

## Compound ID Convention

Tranches whose logical ID collides with a user-authoritative ES-NNN assignment use compound IDs:

- ES-031-SVC : Service integration (was ES-031 ; logical ES-031 now belongs to Agentic Network)
- ES-032-PRD : Product integration (was ES-032 ; logical ES-032 now belongs to Autonomous Network)

Compound IDs preserve history without conflicting with the user-authoritative tranche map.

## Author

Emmanuel A. Otchere (cardinal author rule, 2026-09-24)

## WSF Network + Closed Loop Tier-3 Demotion (2026-09-28)

Per user-authoritative model (2026-09-28):

- WSF wsf-vocabulary.ttl removed wsf:Network (parent wsf:System) and wsf:ClosedLoop (parent wsf:Process) from Tier 3 Baseline
- WSF ADR-WSF-37 + ADR-WSF-38 (and companion CRs) demoted to Deprecated in wsf-governance PR #20 / #21
- WSF minimal kernel + wsf:Entity + wsf:System + wsf:Process remain as generic foundations
- WSF wsf-spec PR #3 closed the vocab demotion

### Resulting cross-program authority

```
WSF (Tier 1 kernel + Tier 3 foundational entities)
  wsf:Entity       : generic foundation
  wsf:System       : generic (Network removed 2026-09-28)
  wsf:Process      : generic (ClosedLoop removed 2026-09-28)
  wsf:Culture      : Tier 3 Baseline (cross-program anchor for ES-026)
  wsf:Ecosystem    : Tier 3 Baseline (cross-program anchor for ES-029/030)
  wsf:Service      : Tier 3 Baseline (cross-program anchor for ES-031-SVC)
  wsf:Product      : Tier 3 Baseline (cross-program anchor for ES-032-PRD)
      |
      v
Enterprise-Semantics (canonical specializations)
  ES-031 + ES-032   : Network pair (Agentic + Autonomous)
  ES-034 + ES-035   : Closed Loop stack (behavioral_pattern + behavioral_pattern_specialization)
  ES-033            : Loop Engineering (engineering_practice)
```



## ES-ADR-049 ; Per-Concept Repo Self-Containment (Structural Change, 2026-09-30)

Per ES-ADR-049 + CR-ES-049 (Accepted 2026-09-30). Amendment to ES-ADR-030 §2.1.

Each concept repository (`concept-<slug>`) now holds a self-contained exhaustive layout:

- `concept.yaml` ; Authoritative concept record
- `kit/` ; Conformance test kit (manifest + 10 tests)
- `docs/` ; concept.md + conformance.md + target-architectures.md + capability-maturity-model.yaml + assessment.md + measurement.md
- `mappings/` ; wsf.yaml + opendea.yaml + dea-catalogs.yaml (as applicable)
- `examples/` ; concept-specific instances
- `visuals/` ; concept-specific diagrams

Synchronization direction: central repositories remain canonical; per-concept repo is a CI-derived snapshot regenerated by `.github/workflows/sync-concept-repos.yml` (uses `GITHUB_TOKEN` only).

Affected repositories: 48 (all `Enterprise-Semantics/concept-<slug>`).

Cross-program impact:

- WSF: unaffected (no WSF change required)
- ES governance: ES-ADR-030 amended, not replaced
- ES implementation: all 48 per-concept repos updated; central repos unchanged in canonical role

### Author

Emmanuel A. Otchere (cardinal user-authoritative model, 2026-09-28)

## WSF ID Reconciliation ; Cross-Program Pointer ; 2026-09-28

WSF governance documents a formal reconciliation between canonical sequential IDs (ADR-WSF-NNN) and subject-namespace aliases (WSF-ADR-<SUBJECT>-<LOCAL>).

- See: World-Semantic-Foundation/wsf-governance/blob/main/ID-RECONCILIATION.md
- See: World-Semantic-Foundation/wsf-governance/blob/main/id-aliases.yaml

Subject-namespace aliases used in this document and other ES artefacts:

| Alias | Canonical | Status | Notes |
|-------|-----------|--------|-------|
| WSF-ADR-CULTURE-001 | ADR-WSF-33 | Baseline | ES-026 integration |
| WSF-ADR-SYSTEM-001 | ADR-WSF-34 | Baseline | ES-027 integration |
| WSF-ADR-SERVICE-001 | ADR-WSF-35 | Baseline | ES-031-SVC integration (compound) |
| WSF-ADR-PRODUCT-001 | ADR-WSF-36 | Baseline | ES-032-PRD integration (compound) |
| WSF-ADR-NETWORK-001 | ADR-WSF-37 | Deprecated 2026-09-28 | ES-031 + ES-032 (ES-side canonical) |
| WSF-ADR-CLOSED-LOOP-001 | ADR-WSF-38 | Deprecated 2026-09-28 | ES-034 + ES-035 (ES-side canonical) |



## ES-ADR-049 ; Per-Concept Repo Self-Containment (Structural Change, 2026-09-30)

Per ES-ADR-049 + CR-ES-049 (Accepted 2026-09-30). Amendment to ES-ADR-030 §2.1.

Each concept repository (`concept-<slug>`) now holds a self-contained exhaustive layout:

- `concept.yaml` ; Authoritative concept record
- `kit/` ; Conformance test kit (manifest + 10 tests)
- `docs/` ; concept.md + conformance.md + target-architectures.md + capability-maturity-model.yaml + assessment.md + measurement.md
- `mappings/` ; wsf.yaml + opendea.yaml + dea-catalogs.yaml (as applicable)
- `examples/` ; concept-specific instances
- `visuals/` ; concept-specific diagrams

Synchronization direction: central repositories remain canonical; per-concept repo is a CI-derived snapshot regenerated by `.github/workflows/sync-concept-repos.yml` (uses `GITHUB_TOKEN` only).

Affected repositories: 48 (all `Enterprise-Semantics/concept-<slug>`).

Cross-program impact:

- WSF: unaffected (no WSF change required)
- ES governance: ES-ADR-030 amended, not replaced
- ES implementation: all 48 per-concept repos updated; central repos unchanged in canonical role

### Author

Emmanuel A. Otchere (cardinal user-authoritative model, 2026-09-28)
