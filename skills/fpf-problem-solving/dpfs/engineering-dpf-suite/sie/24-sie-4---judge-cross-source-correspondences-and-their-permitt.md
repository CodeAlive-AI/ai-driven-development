## SIE.4 - Judge Cross-Source Correspondences and Their Permitted Uses

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `QualifiedCorrespondenceSet@Use` whose rows identify exact source-local endpoints, relation or incompatibility, orientation, bounded use, permitted loss, justification and evidence, source versions, any known exceptions or counterevidence bearing on the relation, confidence where meaningful, and accepted, rejected, unresolved, or incompatible disposition.

### SIE.4:1 - Problem Frame

**Use this when** two or more governed sources contain concepts, types, relations, fields, codes, model elements, or claims that appear to match and a receiving use needs their relation made explicit. Typical triggers are a shared label, a crosswalk, an automated matcher result, a spreadsheet of “equivalences”, or a model-to-model mapping whose semantic premise has never been judged.

For one cross-source correspondence row and its named use, recover both endpoint senses and ask which direct relation, difference, or incompatibility is supported. The first result is a set that preserves accepted, rejected, unresolved, and incompatible rows rather than forcing every candidate into an equivalence.

The payoff is a defensible semantic premise for identity work, claim composition, executable mappings, and validation. Do not use SIE.4 to construct a missing semantic model, decide cross-source identity, define transformation code, or choose the authoritative value. A local relation inside one governed source remains with its source owner unless the cross-source use makes it an integration premise.

### SIE.4:2 - Problem

Correspondence candidates are cheap. Labels can be normalized, lexical similarity scored, hierarchies compared, and model structures aligned. Yet “similar”, “related”, “narrower”, “same field name”, and “safe to substitute here” answer different questions. A row can state a relation correctly even when using it would lose a distinction the receiver needs.

When candidate generation and qualification collapse, downstream mapping code inherits an unstated ontology and loss policy. Counterexamples are discarded as data-quality defects, source versions disappear, and a reviewer cannot tell whether the relation itself or only its use is unsupported.

### SIE.4:3 - Forces

| Force | Tension |
| --- | --- |
| Automation | Matchers can surface many candidates, while their scores do not establish relation truth or permitted use. |
| Reuse | A general crosswalk is attractive, while relation adequacy can change with receiver, grain, interval, and accepted loss. |
| Precision | Naming the relation the evidence supports avoids claiming more, even when the sources do not fully characterize it. |
| Coverage | Pressure favors filling every row, while unresolved and incompatible rows can be the most decision-useful result. |
| Direction | Transformation needs an orientation, while many conceptual relations are not symmetric or safely reversible. |
| Versioning | Stable mapping identifiers aid reuse, while endpoint meaning can change across source editions and profiles. |

### SIE.4:4 - Solution

Separate candidate discovery, direct relation judgment, and bounded-use qualification. For each row, identify exact source-local endpoints, state the relation or incompatibility and orientation, establish it from the evidence applicable to those endpoints and use a counterexample when it distinguishes disputed relations, then decide whether that relation may support the named use under a stated loss boundary. Keep the direct relation and its use qualification independently inspectable.

#### SIE.4:4.1 - Pattern-Use Unfolding

1. **Take the question from the contract.** State the receiving answer and why this endpoint relation can change it.
2. **Bind exact endpoints.** Reference the `SIE.2` source rows, schemes, definitions, editions, profiles, effectivity, units, codes, and local extensions. Do not map labels without their senses.
3. **Generate candidates without promotion.** Lexical, structural, instance, expert, historical, or matcher evidence may nominate a row. Record the candidate source and score where useful, but do not treat nomination as acceptance.
4. **State the direct relation or difference.** Use the narrowest warranted relation vocabulary. State direction and whether the inverse, symmetry, or transitivity is supported. A pair may be excluded from a join while the relation remains unknown. To assert that an assignment is absent, use evidence that excludes it for this configuration, such as a complete governing plan.
5. **Check what warrants the relation.** Apply the definitions, governing assignment or other evidence to the endpoints and the range claimed. When a relation over a class is proposed, vary a relevant version, unit, grain or scope. One verified counterexample can defeat a general substitution. A complete governing plan can settle the relation for one pair directly. A service can also derive a correspondence by applying a valid inference to supported premises. In SKOS, two successive exactMatch relations entail a further exactMatch. Two successive broadMatch relations leave the direct broadMatch open. The rule and premises determine what the service can warrant. [SKOS Reference, mapping properties](https://www.w3.org/TR/skos-reference/#mapping)
6. **Qualify the receiving use.** State which substitution, comparison, join, navigation, or transformation the row permits, what semantic loss it introduces, and which uses remain forbidden.
7. **Preserve evidence and authority.** Record justification, evidence source, reviewer or domain authority where required, uncertainty or confidence, and the owner of any unresolved domain judgment.
8. **Assign a row disposition.** Use accepted-for-use, accepted-with-loss, rejected, unresolved, or incompatible. A row can state a true broader/narrower relation yet be rejected for this use.
9. **State dependencies and tests.** Name whether `SIE.5`, `SIE.6`, or `SIE.7` consumes the row, plus a test or observation that reopens it.

#### SIE.4:4.2 - Record the Result

| Correspondence position | Required content |
| --- | --- |
| row identity and use | stable row identifier, receiver/use, consuming result |
| source endpoint | source, scheme/model, exact sense, edition/profile/effectivity, identifier |
| target endpoint | source, scheme/model, exact sense, edition/profile/effectivity, identifier |
| direct relation | relation or explicit difference/incompatibility, orientation, inverse/symmetry/transitivity qualification |
| use qualification | permitted operation, accepted loss, forbidden reuse, conditions |
| warrant | candidate origin, justification, evidence, authority, uncertainty/confidence where meaningful |
| challenge | grounds for the relation at the stated scope and discriminating cases where needed |
| disposition and continuation | accepted-for-use, accepted-with-loss, rejected, unresolved, incompatible; downstream reference and reopen condition |

#### SIE.4:4.3 - What Changes in Practice

The team stops treating a mapping spreadsheet as a bag of equalities. A proposed row can be tested against the applicable evidence or inference rule. A warranted relation can then be qualified for the operation the receiver needs. A person or service may perform both steps under the applicable terms. Unresolved and incompatible rows remain visible to the interface and tests.

### SIE.4:5 - Archetypal Grounding - Product Feature and Inspection Characteristic

In the AP242/QIF application, the lexical candidate `feature ↔ characteristic` is too broad. The source inventory distinguishes an AP242 product-definition feature, a QIF inspection characteristic, the plan relation that applies a characteristic to a feature, and a measured result concerning that characteristic.

| Candidate row | Direct relation judgment | Use qualification and disposition |
| --- | --- | --- |
| AP242 feature `F-17` ↔ QIF characteristic `C-17` | not identity and not class equivalence; the QIF plan asserts that `C-17` concerns the identified product feature under configuration/effectivity `R/E` | accepted-for-use as a directed `inspection-characteristic-concerns-feature` relation only after `SIE.5` qualifies the feature endpoint; no reverse substitution |
| AP242 feature type `hole` ↔ QIF characteristic type `diameter` | a diameter characteristic can characterize some holes, but the types are neither equal nor simply broader/narrower | accepted-for-use for navigation from a selected plan row with a qualified feature endpoint to its linked hole feature and diameter characteristic. Return their separate source identifiers and types with the plan relation; forbidden as a global type crosswalk |
| AP242 feature `F-22` ↔ QIF characteristic `C-99` | Only the shared local label supports this candidate. The accessible plan excerpt supplies no assignment at `R/E`. | Exclude the pair from the join and return the link as unresolved. If the complete governing plan for `R/E` contains no such assignment, return an established non-match for that configuration. |
| legacy feature class ↔ current QIF characteristic class | one local extension lacks an authoritative definition | unresolved and stopped for dependent mapping; return to the extension owner |

The set records endpoint editions and counterexamples such as a non-dimensional inspection characteristic and a feature absent at effectivity `E`. It establishes semantic premises; it does not decide that identifiers denote the same entity or specify executable joins.

### SIE.4:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A matcher or integrator silently becomes the domain relation authority. | Record the warrant, decision scope, and required domain authority for each accepted row. |
| Architecture | Available mapping technology limits the relation vocabulary. | State the semantic relation first; choose its carrier later. |
| Ontology/Epistemology | Similarity, correlation, broader/narrower relation, and equivalence collapse. | Use the narrowest supported relation and preserve uncertainty and counterexamples. |
| Pragmatics | Every possible endpoint pair is reviewed. | Restrict rows to relations that can change the contract or a dependent result. |
| Didactics | Direction arrows are read as a mandatory processing order. | Explain orientation as relation or transformation meaning, not lifecycle sequence. |

### SIE.4:7 - Conformance Checklist

- [ ] Every row serves a named receiving use and consuming result.
- [ ] Both endpoints reference exact source-local senses and applicable editions/profiles.
- [ ] Candidate generation is distinguishable from relation judgment.
- [ ] The direct relation, difference, or incompatibility uses the narrowest warranted kind and states orientation.
- [ ] Inverse, symmetry, and transitivity are not inferred without support.
- [ ] The grounds support the relation over its claimed scope. Where examples distinguish plausible relations, their consequences for the proposed use are explicit.
- [ ] Permitted operation, semantic loss, conditions, and forbidden reuse are explicit.
- [ ] Evidence, uncertainty/confidence, and decision authority are inspectable.
- [ ] Rejected, unresolved, and incompatible rows remain available to downstream interfaces and tests.
- [ ] The set claims neither cross-source identity nor executable transformation by implication.

### SIE.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Same label, therefore same meaning | Recover endpoint senses and test counterexamples. |
| Matcher score as truth | Treat the score as candidate evidence; obtain a relation warrant and use decision. |
| Every relation is `sameAs` | Distinguish identity, equivalence, broader/narrower, related, concerns, transforms-to, difference, and incompatibility. |
| One global crosswalk | Qualify rows by use, source editions, loss, and forbidden reuse. |
| Symmetric spreadsheet mapping | State orientation and test whether the inverse is supported. |
| Delete failed rows | Retain rejected, unresolved, and incompatible dispositions for receiver and validation behavior. |

### SIE.4:9 - Consequences

The correspondence set gives mapping and interface work explicit semantic premises and preserves negative results. It makes version and loss dependencies visible and allows a narrow use to proceed while other rows remain unresolved.

The work depends on what remains to be established for the row. A similarity score can nominate a correspondence. An automated check with sufficient grounds can establish the relation and apply a use rule within its mandate. If the use requires approval of a new loss, obtain the decision from whoever holds that authority. Running an approved mapping can deliver its result. Attributing the choice of mapping to its operator requires evidence that the operator made that choice.

### SIE.4:10 - Rationale

A direct relation and permission to use that relation answer different questions. Keeping them separate allows a true relation to be rejected for a loss-sensitive use and a qualified narrow relation to support one operation without being promoted globally.

### SIE.4:11 - SoTA-Echoing

The best-known line combines explicit relation vocabularies, mapping metadata, alignment evaluation, and direct Bridge truth. The serious default is a two-column crosswalk plus confidence score. Its defect is that it hides endpoint senses, relation algebra, bounded-use loss, and counterexamples. SIE.4 adapts current mapping practice into a set that records negative dispositions and qualifies each relation for its receiving use.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `F.9` | adopt | Governs each direct cross-context Bridge and separate bounded-use claim; a package row must not replace Bridge truth. |
| [SKOS Reference](https://www.w3.org/TR/skos-reference/) | adapt | Supplies distinct mapping relation forms and cautions through their semantics; SKOS does not prove a candidate relation or authorize substitution. |
| [SSSOM 1.0](https://mapping-commons.github.io/sssom/1.0/spec-model/) | adapt | Contributes inspectable subjects, predicates, objects, provenance, justification, confidence, and source versions; metadata completeness is not relation truth. |
| [OAEI 2025 results](https://oaei.ontologymatching.org/2025/results/) | adapt | Demonstrate task- and track-dependent alignment evaluation; benchmark performance does not decide a local row. |
| label-only or score-only crosswalk | reject as sufficient | It can nominate candidates but cannot establish endpoint senses, relation, permitted loss, or authority. |

Reopen when an endpoint meaning or edition changes, a counterexample defeats the relation or use qualification, the receiver's loss boundary changes, or a better relation vocabulary materially changes action.

### SIE.4:12 - Relations

- `SIE.2` supplies exact endpoint senses, editions, profiles, authority limits, and model gaps.
- `SIE.3` is a conditional return when available models cannot express a required endpoint distinction.
- `SIE.5` consumes rows that expose a load-bearing cross-source identity question.
- `SIE.6` uses correspondences to decide which source claims are comparable or composable without erasing scope or conflict.
- `SIE.7` consumes only accepted rows under their stated use and loss conditions; it adds executable transformation semantics.
- `SIE.10` tests correspondence truth and use qualification independently from mapping execution.

### SIE.4:End
