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
