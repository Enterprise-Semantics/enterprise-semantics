<!--
Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-22)
Filing: CR-ES-001 §10 + §11-§13 (governance scaffolding, no destructive replaces)
-->

# Workflow Profile Subdir (Reserved)

**Status:** Reserved at v0.0.1, no profile records landed yet.
**Profile family:** `workflow`, execution choreography
**Authored by:** Emmanuel A. Otchere
**Date:** 2026-09-22
**Provenance:** CR-ES-001 §18 + ADR-ES-001 §16

## Scope

This directory holds Workflow-family profile records per CR-ES-001 §18. Profiles provide semantic organisation rather than independent authorities.

## Status of contents

Empty at v0.0.1. Profile records will be introduced by:

- Concept-specific ADRs (ADR-ES-002 onwards), for domain profiles.
- Profile-pattern ADRs, for cross-domain profiles.

The existing `registry/profiles/agentic-execution.profile.yaml` is the canonical implementation of the `agentic-execution` Profile type. It lives under `registry/profiles/` per the existing repo structure, this `profiles/agentic/` subdir is reserved for future domain-specific profiles.

## Out of scope

- Substantive concept promotion (lands in concept-specific CRs).
- Registry migration (held for housekeeping CR).
- Profile record content (lands in concept-specific CRs).

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 dash rule
- SDO-neutral sourcing (ISO/IEC, ITU-T, ETSI, NIST)
- No vendor-specific material from embargoed sources
