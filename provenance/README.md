<!--
Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-22)
Filing: CR-ES-001 §3-§7 (scaffold scaffolding only ;;; no concept mutation, no schema mutation)
-->

# Provenance

This directory holds the governed provenance registries for Enterprise-Semantics.

Per ADR-ES-001 §14 and CR-ES-001 §9:

* Every canonical semantic concept shall maintain provenance sufficient to
  establish origin, research basis, governing decision, implementation
  history, external grounding where applicable, and downstream mappings.
* Provenance distinguishes SOURCE, RESEARCH, FINDING, DECISION,
  IMPLEMENTATION, and MAPPING.
* A semantic concept must be traceable to the decision and implementation
  that established it.

## Files

| File | Provenance kind | Purpose |
|------|-----------------|---------|
| `sources.yaml` | SOURCE | External sources contributing to ES concepts |
| `findings.yaml` | FINDING | Links to ES Findings that established evidentiary basis |
| `decisions.yaml` | DECISION | Links to ES ADRs that established the governed decision |

## Lifecycle

Provenance records follow the ES concept lifecycle (`PROPOSED`, `CANDID`,
`ESTABLISHED`, `CANONICAL`). Repository presence does not imply maturity
(per ADR-ES-001 §6).

## Out of scope (per CR-ES-001 §26)

This directory does not introduce:

* Substantive enterprise concept provenance.
* Agentic or Autonomous provenance.
* Vendor-specific provenance. The ES provenance model is sourced from SDO-neutral standardisation only (e.g. ISO/IEC, ITU-T, ETSI, NIST).
