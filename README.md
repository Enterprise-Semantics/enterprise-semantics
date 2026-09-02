# enterprise-semantics

> Canonical enterprise-semantics assets: the authoritative structured semantic source for enterprise-level concepts, relationships, identifiers, and provenance.

This repository is the **semantic authority** within the
[Enterprise-Semantics](https://github.com/Enterprise-Semantics) organization. It holds the structured
semantic source from which documentation, mappings, examples, and conformance tests are derived.

The semantic source is intentionally technology-neutral: YAML or JSON records that capture concept, definition, status, relationships, identifiers, and provenance. Markdown, PlantUML, JSON Schema, and API artifacts are generated from this source.

## Status

**Skeleton (v0.0.1).** The semantic seed and the identifier registry land in Phase 4 per the [program plan](https://github.com/Enterprise-Semantics/enterprise-semantics-governance/blob/main/docs/plan/PLAN.md).

## Relationship to other repositories

| Repository | Relationship |
|------------|--------------|
| [`enterprise-semantics-spec`](https://github.com/Enterprise-Semantics/enterprise-semantics-spec) | Downstream: conformance requirements that this source must satisfy. |
| [`enterprise-semantics-governance`](https://github.com/Enterprise-Semantics/enterprise-semantics-governance) | Side: ADRs/CRs/Findings that authorize changes to this source. |
| [`enterprise-semantics-docs`](https://github.com/Enterprise-Semantics/enterprise-semantics-docs) | Downstream: human-readable views generated from this source. |
| [`enterprise-semantics-examples`](https://github.com/Enterprise-Semantics/enterprise-semantics-examples) | Parallel: worked examples; provenance evidence for the seed. |
| [`enterprise-semantics-mappings`](https://github.com/Enterprise-Semantics/enterprise-semantics-mappings) | Downstream: bi-directional mappings from this source to WSF, OpenDEA, DEA Catalogs. |
| [`enterprise-semantics-visuals`](https://github.com/Enterprise-Semantics/enterprise-semantics-visuals) | Parallel: reproducible diagrams that may illustrate source concepts. |
| [`enterprise-semantics-test-probe`](https://github.com/Enterprise-Semantics/enterprise-semantics-test-probe) | Upstream: conformance harness that validates this source. |

## Architectural position

```text
                     WSF
                      : foundation grounding
                      v
             ENTERPRISE SEMANTICS  ;;; this repository lives here
                      : enterprise semantic grounding
                      v
                   OpenDEA
                      :
                  instances
                      v
                DEA Catalogs
```

## Authority boundary

This repository is authoritative for the semantic definitions and relationships that it formally establishes within its declared enterprise scope. A concept appearing in the seed is **not** automatically canonical. Promotion to Canonical requires the appropriate lifecycle progression: Candidate ;; Investigating ;; Proposed ;; Established ;; Canonical.

## Source-of-truth principle

Human-readable Markdown is a presentation of the semantic model, not its machine source of truth. The structured semantic source (YAML or JSON) is authoritative. Generated artifacts must be regenerated from the source; do not hand-edit them.

## Stable semantic identity

Every concept carries a stable identifier independent of filename, repository, display name, Markdown heading, version, or downstream metamodel class. The exact identifier scheme is established by ADR-ES-001; the critical requirement is that semantic identity survives repository restructuring, documentation changes, and downstream representation changes.

## Style and language

- Spec tone (no "We should..." narration in body prose).
- En-dash (–) and em-dash (–) **do not appear** in newly authored content. Use colons (:) or semicolons (;) consistently.
- Commit messages follow `<type>: <imperative description>`.

## Contributing

See [CONTRIBUTING.md](https://github.com/Enterprise-Semantics/.github/blob/main/CONTRIBUTING.md) for the governance workflow and templates.

## License

Apache License 2.0. See [LICENSE](https://github.com/Enterprise-Semantics/enterprise-semantics/blob/main/LICENSE).