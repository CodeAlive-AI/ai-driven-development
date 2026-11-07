## SIE.2 - Recover and Qualify Source Semantics and Authority

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SourceSemanticInventory@Use` that records the load-bearing source assets, local meanings, schemes, editions and effectivity, identifiers, claims, owners and authority scope, provenance, access, currentness, gaps, and exact returns for one semantic-integration use.

### SIE.2:1 - Problem Frame

**Use this when** a bounded integration use exists, yet endpoint meanings are being inferred from labels, column names, class names, diagrams, sample values, or undocumented organizational knowledge. The recognizable failure is a mapping that runs while joining different concepts, editions, grains, or authority scopes.

The primary EntityOfConcern is the set of source-local semantic premises that the receiving use actually consumes. The first move is to select one load-bearing source asset and recover its scheme, edition or effectivity, meaning, owner, authority, provenance, and access conditions. The first result is an inventory that makes both usable premises and exact gaps inspectable.

The payoff is a clean separation between what a source says, what an integrator infers, and what another owner must decide. Do not use SIE.2 to construct an ontology, establish a cross-source correspondence, decide identity, fuse claims, or judge receiving-use adequacy. If model adequacy for a required distinction remains unsettled, request `UseFitSemanticModel@Use` from `SIE.3` or another qualified direct provider. Adequate reuse can finish that question; an actual missing distinction may require extension or construction.

### SIE.2:2 - Problem

Source inventories often list files and endpoints but omit the meanings that make their values usable. A table called `feature`, an API field called `available`, and an identifier called `partNumber` appear self-describing. Their actual senses may depend on an edition, profile, configuration, interval, issuer, lifecycle state, organizational rule, or local extension.

When those dependencies are hidden, later workers can neither justify a correspondence nor trace a failure. A changed source looks like a schema defect even when the meaning changed; an access right is mistaken for authority; and a provenance record is mistaken for truth.

### SIE.2:3 - Forces

| Force | Tension |
| --- | --- |
| Selectivity | Reading every source is infeasible, while skipping one load-bearing definition can invalidate the package. |
| Formal and operative meaning | Standards and schemas provide inspectable definitions, while actual profiles, extensions, and Work can narrow or alter use. |
| Edition and effectivity | A stable name aids reuse, while its meaning or applicability can change across revisions, profiles, configurations, and intervals. |
| Authority | Publishers and stewards define bounded schemes or values, while the receiver may need a decision outside their scope. |
| Access | A source may be meaningful but unavailable, restricted, delayed, or legally unusable for the proposed integration. |
| Adequacy | Existing models reduce construction work, while forcing an inadequate model hides a real semantic gap. |

### SIE.2:4 - Solution

Recover source semantics at the smallest grain that can change the receiving answer. Preserve term, concept, type, relation, schema, model, claim, data item, carrier, identifier, and world-side referent as different questions. Qualify each relied-on premise by source identity, edition/effectivity, authority scope, provenance, access, currentness, and known gaps.

#### SIE.2:4.1 - Pattern-Use Unfolding

1. **Take the source cut from the use contract.** Add another source only when it can change an answer claim, test, loss, or stop condition.
2. **Identify the source asset and carrier.** Record publisher or owning System, title or endpoint, profile/module, version or edition, publication and effectivity, retrieval location, and carrier kind. Keep the asset distinct from the concepts and claims it carries.
3. **Recover the local scheme and scope.** State the domain, population, lifecycle state, configuration, jurisdiction, or Work context in which the source definitions apply.
4. **Recover exact meanings.** For every load-bearing endpoint, record the designation, definition or operative rule, type/relation role, examples and counterexamples, units or codes, and unresolved ambiguity. Use source-local language before normalizing it.
5. **Separate identifiers and identified entities.** Record the scheme, issuer or owner, syntax, resolution behavior where relevant, use restrictions, grain, interval, and what the identifier does not establish.
6. **Separate claims, data, and provenance.** Record which claim a data item represents, its scope and time, how it was derived, who or what supplied it, and which uncertainty or status accompanies it. Provenance does not make the claim true.
7. **Recover authority and access.** Name who may define the scheme, issue identifiers, decide authoritative values, approve local extensions, grant access, and authorize receiving use. Mark unsupported assumptions.
8. **Assess currentness and use adequacy.** Compare the source premise with the contract. State whether it is adequate, adequate only under conditions, unresolved, obsolete for this use, inaccessible, or missing.
9. **Return an inadequate model.** If the required distinction cannot be expressed in the available source or supplied semantic model, request `UseFitSemanticModel@Use`; do not hide the gap in a mapping rule.
10. **Record dependencies and next results.** Identify the exact definitions, editions, authority facts, and gaps consumed by `SIE.4`–`SIE.10`, plus observations that reopen this inventory.

#### SIE.2:4.2 - Record the Result

| Inventory position | Required content |
| --- | --- |
| source identity | owning/publishing System, asset or endpoint, profile/module, carrier, location |
| edition and applicability | version/edition, publication, effectivity/configuration/interval, local extension status |
| local semantic endpoints | designation, definition or operative rule, type/relation role, scope, examples/counterexamples, units/codes |
| identifiers | scheme, issuer/owner, syntax, resolution behavior, restrictions, grain, interval, identified-entity claim |
| claims and data | source claim, represented data item, scope/time, uncertainty/status, derivation and provenance |
| authority and access | meaning, identifier, value, extension, access, and receiving-use authority scopes |
| qualification | adequate, conditional, unresolved, obsolete, inaccessible, missing, or model-gap return with reason |
| dependency and reopen | consuming package rows, known gaps, next result, and source/edition/meaning changes that reopen |

#### SIE.2:4.3 - What Changes in Practice

Mappings are grounded in the recovered source meanings. A later correspondence or transformation can point to exact source-local endpoints and editions, and a failure can return to the owner of the missing meaning, authority, access, or model. An inventory row can be useful even when its disposition is unresolved or inaccessible.

### SIE.2:5 - Archetypal Grounding - AP242 and QIF Source Cut

For the AP242/QIF query in `SIE.1`, the team inventories only source premises that can change the configuration-bound answer.

| Source row | Qualification for the constructed use |
| --- | --- |
| AP242:2025 edition 4 | Product-definition, configuration/change, and effectivity source for the case. Record the official publication identity and current stage 90.92, “to be revised”. The source owner defines its model; Systems Engineering decides which released configuration applies locally. |
| local AP242 exchange/profile | Record the exact application protocol/profile, implementation conventions, export version, local extensions, identifiers, and configuration/effectivity fields actually supplied. The standard title alone does not establish those facts. |
| QIF source | Record the applicable ISO 23952:2020 carrier/profile, plan, characteristic, and result meanings, identifiers, measurement context, status, and local quality authority. A QIF result identifier does not establish AP242 feature identity. |
| local source records | Record export or API occurrence, timestamps, derivation, access, issuer, local configuration or inspection status, and gaps. A reachable file is not automatically current or authorized for review. |

The inventory marks an unresolved local AP242 extension used by one feature class. Because its meaning can change the correspondence, the package stops that row and returns to the extension owner. Other rows can continue. If neither AP242 nor QIF can express a required tolerance-state distinction, the inventory requests a qualified `UseFitSemanticModel@Use`; it does not invent the distinction in the transform.

### SIE.2:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Custody or access is mistaken for semantic or value authority. | Record each authority scope and the evidence for it separately. |
| Architecture | The inventory mirrors the integration platform rather than governed sources. | Identify source assets and meanings independently of the selected realization. |
| Ontology/Epistemology | Term, concept, type, relation, identifier, claim, data, and referent collapse into one “field”. | Use separate inventory positions and preserve unresolved senses. |
| Pragmatics | Exhaustive documentation delays the use without changing it. | Inspect only premises that can change an answer, loss, test, or stop. |
| Didactics | A standards citation is read as proof that the local export conforms or is current. | Record the local profile, occurrence, evidence, extension, and effectivity separately. |

### SIE.2:7 - Conformance Checklist

- [ ] Every included source can change a named contract position.
- [ ] Source asset, carrier, local scheme, semantic endpoint, identifier, claim, data item, and referent remain distinguishable.
- [ ] Edition, profile/module, effectivity/configuration/interval, and local extensions are explicit where load-bearing.
- [ ] Definitions or operative rules include scope and at least one discriminating example or counterexample where ambiguity matters.
- [ ] Identifier scheme, issuer/owner, grain, interval, restrictions, and resolution assumptions are explicit.
- [ ] Claims retain provenance, scope, time, status, and uncertainty without treating provenance as truth.
- [ ] Meaning, identifier, authoritative-value, extension, access, and receiving-use authorities remain separate.
- [ ] Every row has an adequate, conditional, unresolved, obsolete, inaccessible, missing, or model-gap disposition.
- [ ] Consuming rows and reopen conditions are recoverable.

### SIE.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Data dictionary by column name | Add source-local definition, scope, edition, units/codes, examples, and authority. |
| Standards title as implementation evidence | Inspect the actual profile, export, extension, occurrence, and conformance evidence. |
| “Same ID format means same object.” | Record scheme, issuer, grain, interval, and identified-entity claim; use `SIE.5` for cross-source identity. |
| Provenance equals truth | Keep derivation and source authority separate from domain truth and receiving acceptance. |
| Read every source | Start from the contract and add only action-changing premises. |
| Patch a model gap in code | Return the missing semantic-model result before relying on the rule. |

### SIE.2:9 - Consequences

Mappings become reviewable against exact endpoints, and source changes can be traced to the rows that relied on them. Authority, access, and model gaps appear before implementation. The same inventory can support several direct pattern entries while each use retains its own qualification.

The cost is source-local reading and coordination with publishers, stewards, domain specialists, and access owners. Some attractive automation must wait because the source meaning or applicability is unresolved.

### SIE.2:10 - Rationale

Semantic integration cannot preserve a meaning that has not been recovered at the source. Source-local recovery also prevents a shared vocabulary from becoming a hidden replacement for source authority. Qualification by use keeps the inventory finite and prevents documentation breadth from substituting for a workable package.

### SIE.2:11 - SoTA-Echoing

The best-known line combines terminology work, metadata-registry discipline, provenance, and source-local meaning recovery. The serious default is schema inspection plus organizational folklore. Its defect is not informality alone; it leaves no stable relation among the source claim, edition, authority, and mapping premise. SIE.2 adapts the line into a use-qualified manifest with an explicit inadequate-model return.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `F.0.1` and `F.0.2` | adopt | Recover source-local meaning and episteme identity; do not establish a cross-source correspondence or domain truth. |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) | adapt | Keeps objects, concepts, definitions, and designations distinct; it does not decide the receiving integration. |
| [ISO/IEC 11179-3:2023](https://www.iso.org/standard/78915.html) and its [item-mapping amendment](https://www.iso.org/standard/89914.html?browse=tc) | adapt | Contribute registry-item identity, versions, definitions, and mapping metadata; no automatic cross-source identity or fitness follows. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Distinguishes entities, activities, agents, derivation, revision, invalidation, attribution, and primary source; provenance establishes neither truth nor permission. |
| schema-only discovery | reject as sufficient | Structure and samples can locate questions but cannot replace source-local meaning, edition, authority, and applicability. |

Reopen when a source change alters a relied-on meaning, scheme, edition, effectivity, authority, access condition, or provenance chain, or when repeated cases show that an inventory position cannot support the downstream decision.

### SIE.2:12 - Relations

- `SIE.1` supplies the receiving use, source cut, answer claims, preserved distinctions, and stop conditions.
- `SIE.3` qualifies an available model for the named use or develops an actual missing distinction. Request that result when the recovered source model leaves the integration's model question unsettled.
- `SIE.4`, `SIE.5`, and `SIE.6` consume exact endpoint meanings, source claims, identifiers, editions, and authority limits.
- `SIE.7`–`SIE.10` consume the manifest, provenance, currentness, and gap dispositions relevant to implementation and validation.
- Domain sources, MDM, access owners, Systems Engineering, Data Engineering, and applications retain their respective meanings, values, permissions, operational results, and decisions.

### SIE.2:End
