<!--
Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-22)
Filing: CR-ES-001 §3-§7 (scaffold scaffolding only, no concept mutation, no schema mutation)
-->

# Relationships

This directory holds the governed relationship vocabulary for Enterprise-Semantics.

Per ADR-ES-001 §13 and CR-ES-001 §8:

* Relationships are first-class semantic content.
* Every relationship has a canonical predicate, subject semantics, object
  semantics, direction, inverse where applicable, cardinality where
  applicable, provenance, and lifecycle state.
* Only predicates established through an approved ADR/CR or explicitly
  authorised seed activity become governed relationships.

## Files

| File | Purpose |
|------|---------|
| `vocabulary.yaml` | Authoritative registry of governed predicates |
| `inverse.yaml` | Inverse-predicate map (predicates that have an inverse) |
| `README.md` | This file |

## Governance

Adding a predicate to `vocabulary.yaml` requires:

1. An approved ADR that establishes the semantic decision.
2. A CR that implements the YAML change.
3. Conformance validation per CR-ES-001 §22.
4. Lifecycle state assertion (typically `CANDIDATE` on first introduction,
   `ESTABLISHED` after first concept references it, `CANONICAL` after
   multi-domain adoption).

## Out of scope (per CR-ES-001 §26)

This directory does not introduce:

* Substantive enterprise concepts (Capability, Value Stream, etc.).
* Agentic or Autonomous relationships.
* Vendor-specific relationships. The ES relationship vocabulary is sourced from SDO-neutral standardisation only (e.g. ISO/IEC, ITU-T, ETSI, NIST).

Substantive relationship vocabulary lands through subsequent ADR/CR pairs.
