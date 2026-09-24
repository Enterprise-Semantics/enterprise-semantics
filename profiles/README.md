<!--
Authored by: Emmanuel A. Otchere (cardinal author rule, 2026-09-22)
Filing: CR-ES-001 §10 + §11-§13 (governance scaffolding, no destructive replaces)
-->

# Semantic Profiles

This directory holds semantic Profile records per CR-ES-001 §18 and ADR-ES-001 §16.

## Profile vs Profile record

A **Profile** in Enterprise-Semantics is a governed configuration overlay applied to a base concept. The base concept retains its semantic identity, the Profile adds characteristics.

A **Profile record** is a YAML file in one of the subdirectories below that declares:

- The Profile's identity (`ES:PROFILE:<kebab-case-name>`).
- The Profile type (e.g. `agentic-execution`, `autonomous-operation`).
- The base concepts(s to which the Profile applies.
- The Profile characteristics (governed attributes applied by the Profile).

Profile types are registered in `../registry/profile-types.yaml`. Profile records bind to a registered profile type.

## Subdirectories

| Subdir | Family | Status at v0.0.1 |
|--------|--------|------------------|
| `enterprise/` | Enterprise | Reserved |
| `capability/` | Capability | Reserved |
| `value/` | Value | Reserved |
| `agentic/` | Agentic | Reserved (canonical Profile lives at `registry/profiles/agentic-execution.profile.yaml`) |
| `autonomous/` | Autonomous | Reserved (Profile type registered as Reserved in `registry/profile-types.yaml`) |
| `operations/` | Operations | Reserved |
| `workflow/` | Workflow | Reserved |
| `value-realization/` | Value Realization | Reserved |

## Out of scope

This directory does not hold:

- Profile types (those live at `../registry/profile-types.yaml`).
- Concept records (those live at `../concepts/`).
- Implementation of Profiles (the canonical Profile patterns live at `../registry/profiles/`).

## Cardinal rules

- Author: Emmanuel A. Otchere
- D-004 dash rule
- SDO-neutral sourcing (ISO/IEC, ITU-T, ETSI, NIST)
- No vendor-specific material from embargoed sources
