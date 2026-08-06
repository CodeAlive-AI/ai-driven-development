## A.6.9 - Cross-Context Sameness Disambiguation - Repairing cross-context "same", "equivalent", and "align" via explicit Bridges (RPR-XCTX)
> **Type:** Relational precision-restoration pattern
> **Status:** Stable

**Use this pattern when** a document, table row, boundary statement, or publication claim uses *same*, *equivalent*, *aligned*, *mapped*, or *corresponding* in a way that may hide ordinary designation, a non-semantic lane or id claim, or a real relation between exact local senses.

**What goes wrong if missed.** A label match, explanation, ID mapping, or partial correspondence becomes global identity or a licence for an unspecified use. Direction, use rule, tolerated loss, evidence, and the actual downstream act disappear inside one umbrella word.

**What this buys.** The sentence becomes one concrete result: a same-context designation, a claim stated using its concrete predicate or constraint, an obtaining F.9 Bridge plus a separately stated bounded use, or an explicit stop. A card is added only when the claims must travel.

### E.24.UK settlement

A.6.9 admits neither `U.CrossContextSamenessDisambiguation` nor a semantic-context entity as a durable U-kind. It reuses exact F.17 `SchemeSenseCell` values, the direct F.9 `Bridge` relation, ordinary C.2.1 claims, and the existing A.10 or B.3 reliance branch. It introduces no public use-claim kind, universal use relation, shared assessment object, permission kind, or receiving-use occurrence.

> **Type:** Architectural (A) — A.6.P specialisation (RPR)
> **Status:** Stable
> **Normativity:** Normative
> **Placement:** A.6 cluster; follows the A.6.P relation-precision route for cross-context wording.
> **Builds on:** A.6.P for relational prose repair; F.17 for exact scheme-based SenseCells; F.18 for designation; F.9 for the direct Bridge relation, profile, bounded-use boundary, and card boundary; C.2.1 for claim and description identity; F.0.1, F.7, and F.8 for sense-family and downstream naming discipline; A.7 and A.6.6 for lane and identifier dispatch; E.19 for normative precision
> **Coordinates with:** A.10 for evidence-provenance relations and local reliance dispositions; B.3 for assurance; E.17.0 for View membership; E.24.PUB for publication occurrence, form, and carrier; C.3.3 for kind or classification transfer; A.2.6 for scope operations; A.6.3.RT for representation transition; A.22 for structure; A.2.1, F.6, and A.15.1 for role and Work claims

Use this pattern when umbrella sameness wording could hide which exact local senses, designation, lane, identifier, scope operation, representation transition, structure relation, or proposed use is current. The trigger starts a dispatch; it does not oblige the author to assert a Bridge or complete a card.

When the remaining question is semantic, recover the obtaining Bridge first. Then state the proposed use separately in ordinary language: what someone will do, in which direction, by which correspondence rule, and how much semantic loss that use tolerates. Give that C.2.1 claim affirmative or negative polarity. F.9, A.10, and B.3 supply the exact follow-through; A.6.9 teaches the reader how to recover it from ambiguous prose.

### A.6.9:1 - Problem frame

Cross-context prose routinely compresses a multi-part claim into one adjective: *same*, *equivalent*, *align*, *map*, *matches*, or *corresponds*.

First decide whether this is a Bridge situation at all. A positive F.9 case has two exact F.17 `SchemeSenseCell` endpoints whose `<ReferenceScheme, LocalSenseClaim>` projections differ, plus an applicable relation-semantic profile whose predicate is true for those cells. A label, id, system, mapping implementation, selected structure, card, or publication cannot substitute for those objects.

If a Bridge obtains, several questions still remain independent:

* what concrete comparison, substitution, translation, explanation, publication, or other use is proposed;
* the direction of that use;
* the use-specific correspondence rule;
* the semantic-loss tolerance for that use;
* whether the C.2.1 claim about that use is affirmative or negative;
* whether current A.10 evidence or B.3 assurance supports relying on that claim;
* whether separate authorization is required; and
* whether any Work, assertion, publication, relation, operation application, or other receiving object actually occurred.

A.6.9 makes that dispatch visible. It prevents an explanation, mapping witness, score, or polished card from becoming global identity, authorization, or proof of performance.

### A.6.9:2 - Problem

When an umbrella predicate is used as if it were a complete answer, readers silently choose defaults:

* **Symmetry hallucination:** “equivalent” is read as symmetric even when the intended relation is narrower or broader.
* **Relation-to-use jump:** a true correspondence is treated as sufficient for the requested comparison or substitution.
* **Loss erasure:** “same” implies lossless transfer although units, granularity, preconditions, or stance differ.
* **Permission confusion:** “A is suitable for this comparison” is read as permission or authorization to perform it.
* **Implicit inversion:** relation symmetry is treated as two safe use directions, or endpoint order is mistaken for the safe inclusion direction.
* **Occurrence smuggling:** a named “publication use” or “mapping use” is treated as an actual publication or mapping operation.
* **Temporal incoherence:** an unpinned claim silently combines different glossary, schema, code-list, ontology, or model editions.

These are ontology and inference defects, not merely word-choice defects.

### A.6.9:3 - Forces

| Force | Pull | Push |
| --- | --- | --- |
| Brevity | One word such as “same” is fast. | It hides the object, action, direction, rule, tolerance, and stop. |
| Practical interoperability | Teams want shared labels and reusable mappings. | Shared labels and running code are not semantic identity or proof of a safe use. |
| Relation versus use | One semantic relation can remain fixed. | Different uses of it can have opposite polarity or different evidence. |
| Direction | A relation may be symmetric or oriented. | Every proposed use still has its own source-to-receiving direction. |
| Evidence evolves | Counterexamples and warrants change. | Evidence change should reopen reliance without silently reidentifying the Bridge. |
| Version drift | Canons and models change by edition. | The relation profile needs an applicability and as-of basis. |
| Practical safety | Cross-context reuse can save work. | Suitability, reliance, authorization, and actual performance must not collapse. |

### A.6.9:4 - Solution

Treat an umbrella sameness sentence as a **dispatch trigger**, not as an automatic Bridge and not as a demand for a card. Recover the concrete subject and action first. Then choose the smallest truthful branch:

1. **Ordinary designation inside one semantic bounded context.** If both expressions resolve to the same exact `<ReferenceScheme, LocalSenseClaim>` projection, use the ordinary designation owner and stop. When only the admitted extent of that claim changes, apply A.2.6 `widen`, `narrow`, or `refit`. No F.9 Bridge is current.
2. **Lane or reference-plane repair.** If the sentence confuses Object, Description, Carrier, or `CHR:ReferencePlane`, restore the exact kinds under A.7 or the governing plane rule.
3. **Identification or indexing.** If the sentence means same id, key, code, or index target, use A.6.6. Identifier equality does not establish meaning correspondence.
4. **Scope operation.** A.2.6 owns `widen`, `narrow`, `refit`, and `translate` over exact scope values; when the sentence concerns claim extent, recover the exact `U.ClaimScope`. `translate` may consume an independently obtaining F.9 Bridge and a separate affirmative claim for that exact direction, rule, and tolerance; it is neither representation Work nor a structure crossing.
5. **Other locality hidden by context wording.** Route interpretation to the effective `U.ReferenceScheme`; claim extent to `U.ClaimScope`; empirical grounding to one exact `EpistemeEmpiricalGroundingRelation`; time to the qualification window required by the temporal predicate; project wording to an exact composite `U.Work` under A.15.6; viewpoint use to the E.17.0 viewpoint relation and one `U.ViewpointRef` resolving exact P; and any world-side subject claim to the pattern that defines its relation predicate and obtaining condition. None is supplied by a bare context word.
6. **Representation transition.** A representation change is not a Bridge. For ordinary A.6.3.RT use, name the same concern, content to survive, target representation, source comparison, use boundary, and return. When cross-scheme dependency or reliance makes exact claim identity material, independently constitute source episteme `X` and receiving episteme `Y`, require `EntityOfConcern(X)=EntityOfConcern(Y)` exactly, and state exact `v : X -> Y` with scheme relation, preservation, loss, and prohibited strengthening. Assert `RepresentationSchemeTransitionRelation@Context` only when every later-specific six-participant obtaining condition and actual dated representation-transformation Work are present; performed Work alone neither proves `v` nor makes that relation obtain. A Bridge supplies neither `v` nor the Work and makes no transition occurrence obtain.
7. **Structure comparison or crossing.** Recover each exact `BoundedModelUseStructure` independently, then apply the conditional A.22 cross-structure rule in §4.8 only if exact governed subject crossings and a named receiving use remain. A SenseCell Bridge, label, diagram, shared participant, or reference supplies neither structure selection nor crossing; without an exact direct crossing governor, return the A.6.RCD missing-governor stop.
8. **Cross-local semantic relation.** Resolve two exact F.17 `SchemeSenseCell` values from different semantic bounded contexts, declare the F.9 relation-semantic profile, and cite a Bridge only when its predicate obtains. Scheme difference, same spelling, a mapping witness, or two endpoint references alone establishes no Bridge.
9. **Proposed use of an obtaining Bridge.** In a second sentence, name action `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and claim polarity under C.2.1. Recover A.10 or B.3 reliance for that same use.
10. **Explanation or unresolved proposal.** Say plainly what remains unestablished. A candidate or negative card carries no positive occurrence reference.
11. **Claim that the use happened.** Name the actual receiving object and use the rule that defines the claim about that object; the use role inside the C.2.1 claim is not that object.

For A.6.9, **semantic bounded context** is a Plain practice name for the local interpretation basis recovered from one exact cell's `<ReferenceScheme, LocalSenseClaim>` projection. It is not an entity, reference, identity field, project situation, claim scope, grounding holon, qualification window, composite project Work, viewpoint, selected `BoundedModelUseStructure`, description, designator, or publication. Representation transition, A.2.6 scope translation, F.9 local-sense Bridge, and direct structure crossing therefore remain four independently governed moves.

#### A.6.9:4.0 - Trigger and endpoint recovery

Open the dispatch when **same**, **identical**, **equivalent**, **align**, **map**, **match**, **correspond**, *treat as*, *reuse*, *share*, *unify*, *canonical source*, *synced*, *normalized*, *one-to-one*, *same ID*, or *mirrors* could hide the current object or action. Apply equivalent triggers in any language.

Resolve the actual endpoints before choosing the semantic branch. Each candidate endpoint reference must be a `SenseCellAddressRef` resolving one exact F.17 `SchemeSenseCell`. Keep that cell, any C.2.1 description episteme about it, its F.18 designator, and the address reference as four distinct objects: a reference resolves the cell, a designator names it, and a description claims something about it; none substitutes for the cell or for one another. A string, system, table, class name, file, context label, card, id, description, designator, or unresolved reference cannot fill the Bridge endpoint. If a token is metonymic — *the system*, *the model*, *the service*, *that table* — enumerate the plausible governed objects and recover the intended local expression and claim. If either endpoint remains unresolved, keep the sentence explanatory and return `unresolved SenseCell endpoint`.

Pin the endpoint reference-scheme and local-sense-claim editions, or an exact as-of basis, when the correspondence can change with a canon or model edition. `Γ_time` may be used as a compact card label for that basis. It is not a participant. It contributes to profile identity only when it states the profile's exact applicability or as-of basis.

Before testing a Bridge, check ontological strata. Kind or classification transfer remains with C.3.3; value normalization with the measurement owner; role assignment with A.2.1; performed-Work attribution with F.6; publication occurrence, form, and carrier with E.24.PUB; representation transition with A.6.3.RT. F.9 can supply a semantic premise needed by one of those claims but cannot make that neighboring object obtain.

#### A.6.9:4.1 - Stable lens: relation, use claim, reliance, and receiving object

Keep these objects distinct:

1. **Bridge occurrence.** The direct relation has exactly two F.17 cell participants and obtains under one exact F.9 profile.
2. **BridgePredicateProfile.** It contains only Bridge kind, kind-defined symmetry or orientation, endpoint-sense readings, relation-specific correspondence or difference condition, applicability and as-of basis, Boolean truth condition, and stop dependencies.
3. **Bounded-use claim.** An ordinary C.2.1 claim says whether the exact obtaining Bridge is suitable for `<u,d,r,t>`. Its EntityOfConcern is the Bridge; its ClaimGraph designates the use, direction, rule, tolerance, and polarity; its effective scheme interprets them.
4. **Optional Bridge Card.** It packages claims and evidence when durable reuse pays. It neither creates the relation nor grants the use.
5. **Separately governed receiving object.** If the use happened, its Work, assertion, publication, direct relation, operation application, or other object keeps its own participants, obtaining or performance condition, and identity.

```text
Bridge(SourceSenseCell, ReceivingSenseCell; BridgePredicateProfile)
```

Use that notation only after the F.9 predicate passes. For a proposal, write `candidate Bridge(...)` or use a candidate card with no positive occurrence reference.

Changing `u`, `d`, `r`, or `t` changes the bounded-use claim, not the Bridge. Changing evidence, an A.10 relation or local `RelianceDisposition`, or a B.3 claim, record, or disposition reopens reliance without reidentifying either fixed object. A changed endpoint or relation-semantic profile identifies another Bridge candidate.

#### A.6.9:4.2 - Explicit claim skeleton

| Item | When required | Meaning and stop |
| --- | ---: | --- |
| `SourceSenseCellRef`, `ReceivingSenseCellRef` | every Bridge candidate | Exact F.17 addresses; unresolved endpoints stop the semantic branch. |
| semantic-context projections | every Bridge candidate | Derived `<ReferenceScheme, LocalSenseClaim>` pairs; they must differ for F.9. |
| `BridgePredicateProfile` | every Bridge candidate | Exact by-value relation semantics only; a label or id is insufficient. |
| `BridgeKind` and relation orientation | profile and readable explanation | What semantic correspondence or difference is claimed; not a use licence. |
| applicability / `Γ_time`, truth condition, dependencies | profile | When and how the direct predicate is tested; missing dependencies stop without inventing an occurrence. |
| action `u` | every proposed use | What the reader proposes to compare, substitute, translate, publish, or otherwise do. |
| direction `d` | every proposed use | Exact use-source to use-receiving order; relation symmetry supplies no direction by implication. |
| rule `r` | every proposed use | The correspondence rule the action will follow. |
| tolerance `t` | every proposed use | Which semantic loss is acceptable for this action; observed loss remains evidence. |
| polarity and effective ReferenceScheme | every bounded-use claim | Whether the claim is affirmative or negative and how its designations are interpreted. |
| A.10 or B.3 branch | when someone will rely on the claim | The exact evidence-provenance relation plus local disposition, or the B.3 claim or explicit disposition selected by its trigger. |
| authorization claim | only when permission is required | Separate policy or deontic governor; semantic suitability and assurance are insufficient. |
| receiving-object ref | only when the use is said to have happened | Exact Work, assertion, publication, relation, application, or other object under its owner. |
| `ClaimMode` and card EntityOfConcern | only when a card pays | Actual card concerns the obtaining Bridge; candidate or negative card concerns the admitted F.9 Bridge relation kind and carries proposed endpoints and profile in its ClaimGraph. |

Only the two endpoint cells fill the direct relation's participant slots. Use content is ClaimGraph content, not another relation participant or profile component.

#### A.6.9:4.3 - Judgement and change

Choose the least-committing truthful Bridge kind: `Equivalence`, `Narrower-than`, `Broader-than`, `Partial-overlap`, `Disjoint`, or one declared cross-family relation kind. The kind settles relation semantics only.

Then judge the proposed use:

* `Partial-overlap` can support an affirmative label-use claim when its exact rule preserves the named differences; the Bridge does not grant that use automatically.
* `Disjoint` can support a contrastive explanation; a proposed substitution receives negative polarity.
* `Equivalence` is symmetric, but `A -> B` and `B -> A` are different use claims.
* `Narrower-than` and `Broader-than` orient the semantic relation. Narrower-to-broader is usually easier to warrant, but every use direction still needs its own rule, tolerance, polarity, and reliance.
* A broader-to-narrower proposal normally requires refined cells and a separately tested Bridge. Another profile over the same broad endpoints cannot make an unsafe use safe by declaration.
* Type-structure reuse requires a separate claim naming the structural rule and loss tolerance. Matched invariants can support that claim; no `CL` number grants it.

`CL` may remain optional evidence shorthand: `0` contradicted, `1` weakly comparable, `2` bounded support with counterexamples, `3` matched stated invariants with no current material counterexample. It is neither profile identity nor a suitability threshold.

Narrate changes by the object that changed:

1. `retargetEndpoint` for another source or receiving cell;
2. `replaceBridgeProfile` for changed relation-semantic content;
3. `reviseBoundedUseClaim` for changed `u`, `d`, `r`, `t`, effective scheme, or polarity;
4. `retestObtaining` for changed endpoint facts or dependencies under the fixed profile;
5. `reopenReliance` for changed evidence, currentness, A.10 relation or disposition, or B.3 claim, record, or disposition;
6. `reviseBridgeCard` for changed package content;
7. `publishBridgeCardEdition` for a publication occurrence; and
8. `recoverReceivingObject` when the use is claimed to have happened.

An inverse asymmetric relation and any direct A-to-C relation require their own profiles and tests. Two chained Bridges do not entail a third.

#### A.6.9:4.4 - Lexical guardrails

In normative or decision-carrying prose, replace the umbrella word with a sentence that exposes the action and stop:

| Intended meaning | Plain action | Exact follow-through |
| --- | --- | --- |
| ordinary same-context designation | “Both expressions designate this local sense.” | Cite the common projection and naming owner; no Bridge. |
| interpretation | “Use A to explain B; do not substitute it.” | Test the cross-family Bridge; state a separate affirmative explanation-use claim and its nearest non-use. |
| naming convenience | “Use the label ‘actor’ in this comparison; keep account and customer eligibility distinct.” | Obtaining Bridge plus a C.2.1 claim naming direction, label rule, and zero tolerance for eligibility transfer. |
| directional substitution | “For calculation X, read A as B by rule R within tolerance T; do not reverse it.” | Obtaining Bridge, affirmative claim for `<X,A->B,R,T>`, and current A.10 or B.3 reliance. |
| type-structure reuse | “Reuse this subtype row only while invariants I remain true and loss stays within T.” | Obtaining Bridge plus a separately warranted structural-use claim. |
| contrast | “These senses differ in this stated way; do not substitute them.” | Obtaining `Disjoint` or `Partial-overlap` Bridge plus negative substitution-use polarity. |
| unresolved proposal | “The mapping is available, but the semantic relation is not established.” | Candidate card or plain stop naming the missing endpoint, predicate fact, or dependency. |

Plain teaching prose may retain *same*, *align*, or *map* only when the local sentence also tells the reader what to do, what not to infer, and what result would reopen the claim.

#### A.6.9:4.5 - Disambiguation guide

| Trigger | First question | Default route | Stop |
| --- | --- | --- | --- |
| “A is the same as B” | Same local sense or relation between distinct senses? | designation first; otherwise least-committing F.9 kind | no exact cells or predicate -> explanatory only |
| “Align A and B” | Shared label, comparison, substitution, or structure use? | name the proposed action before selecting a Bridge | mapping score alone establishes neither relation nor use |
| “Map A to B” | Semantic reading or operational transformation? | keep code or ETL as witness; test semantics separately | code direction is not use suitability |
| “Same ID/key/one-to-one” | Identifier relation or meaning relation? | A.6.6 first | collision-free ids do not establish sense identity |
| “B is a view/projection of A” | View membership, representation, or sense reuse? | E.17.0, C.29, or representation owner first | dropped constraints block stronger use claims |
| “Equivalent” | What relation, action, direction, rule, and tolerance? | test overlap or inclusion before equivalence | symmetry alone grants no use |

#### A.6.9:4.6 - Mapping witnesses are not Bridges

A lookup table, aligner model, transformation function, API, or ETL step is an implementation or evidence object. It may support the claim that a Bridge obtains or that one bounded use is suitable. It does not determine either claim by itself. Code may run `A -> B` while the semantic Bridge is symmetric, oriented the other way, or absent; and even an obtaining Bridge may be unsuitable for that operation's rule or tolerance.

Keep the witness in the A.10 evidence path or optional card. Test the F.9 predicate first, state the C.2.1 bounded-use claim second, and recover reliance third.

#### A.6.9:4.7 - Coordination boundaries

- **Naming and endpoint objects:** F.18 selects designators; F.17 governs exact scheme-based cells and rows. A `SchemeSenseCell`, C.2.1 description episteme, designator, and resolving reference remain distinct; none creates a Bridge.
- **Reference scheme and scope:** C.2.1 owns the effective `U.ReferenceScheme`; A.2.6 owns `U.ClaimScope`, `widen`, `narrow`, `refit`, and `translate`. A.2.6 translation may consume an exact Bridge plus its affirmative bounded-use claim but is not representation Work or structure crossing.
- **Grounding:** C.2.1 alone supplies an `EpistemeEmpiricalGroundingRelation`. Its grounding holon is the participant against which covered empirical claims are grounded; it is not assumed identical to the episteme's EntityOfConcern.
- **Time:** the qualification window is part of the exact temporal or subject predicate and assertion. F.9 profile applicability or `Γ_time` does not become a generic context or time participant for another claim.
- **Project wording:** A.15.6 recovers an actual project as one exact composite `U.Work` after A.15.1 admission and exact work parthood. Project label, plan, situation word, or Bridge supplies no project identity.
- **Viewpoint:** E.17.0 governs the direct `EpistemeViewpointConformanceRelation`; one `U.ViewpointRef` resolves exact viewpoint episteme P. The viewpoint, its reference, candidate/View episteme, and evaluator remain distinct.
- **Evidence and assurance:** A.10 owns evidence provenance and local reliance; B.3 owns assurance claims, records, and explicit dispositions.
- **Representations and publications:** E.17.0 owns conformance-dependent View membership, E.24.PUB owns publication occurrence/form/carrier, and C.29 owns mathematical-representation objects. A.6.3.RT starts an ordinary same-concern representation move with content to survive, source comparison, loss, use, and return; its triggered exact construction independently identifies `X`, `Y`, and `v`; actual representation-transformation Work is required only for the later-specific six-participant occurrence.
- **Kinds and classifications:** C.3.3 owns classification transfer; F.9 supplies only local-sense correspondence needed by that use.
- **Structures:** A.1.1/A.22 independently select each exact `BoundedModelUseStructure`; §4.8 applies the descriptive A.22 conditional cross-structure rule only after exact governed crossings and all four structure discriminators are recoverable. A SenseCell Bridge cannot substitute for that architecture.
- **Direct subject relations, Work, and roles:** every world-side relation has its own exact predicate, participant bindings, and assertion. A.2.1, F.6, A.15.1, and A.15.6 define assignment and exact performed or composite Work predicates; semantic relation, context wording, and use claim have no enactment effect.
- **Authorization:** the exact policy or deontic governor owns permission. Neither semantic suitability nor assurance grants it.

#### A.6.9:4.8 - Structure comparison and conditional cross-structure selection

Use this branch only when the receiving question depends on the organization of actual subject crossings among several bounded model-use structures. First recover every participating `BoundedModelUseStructure` independently under A.1.1/A.22: one exact model episteme, its admitted model-use holons, the exact obtaining applicability, actual-use, and enduring coherence occurrences, the exact applied constraint claims, and one named bounded-model-use frame. A shared system, model, episteme, scope, or other participant does not merge two selected structures and proves neither overlap nor parthood.

Next enumerate every actually obtaining subject-crossing occurrence selected for the proposed organization. For each one, name its exact participants, relation kind and predicate, direction when asymmetric, applicability, obtaining result, occurrence identity, and recurrence rule, and test them against the pattern that defines those relation rules. An F.9 Bridge relates exact local senses only; a Bridge, context label, edge label, Card, registry row, reference, view, diagram, or common participant establishes no subject crossing. If no current pattern defines a required crossing, stop through A.6.RCD at the exact missing-governor question; do not replace it with a vague edge family.

Only then apply A.22's conditional cross-structure rule for one named receiving or crossing-analysis use. Declare the substrate as the exact independently selected `BoundedModelUseStructure` values; the selected relation organization as the exact obtaining crossing occurrences; the exact applied constraints and invariants; and the use frame as the question, admissible action, and forbidden overread. Those are the four A.22 discriminators. The A.22-local provisional label `CrossContextRelationStructure` is only a retrieval aid for that rule until its own F.18 settlement; A.6.9 does not promote it to public vocabulary. The resulting `U.Structure` is a dependent organization, not a container, holon, collection of contexts, source of its crossings, View, Context Map, diagram, Card, or publication.

When a load-bearing claim says that this organization was selected, separately name the selecting system, exact Method, dated selection `U.Work`, and direct participation relations or A.6.1 bindings. Name the exact selection judgment and its result: when persistence is needed, a C.2.1 result episteme whose exact EntityOfConcern is the selected structure; when an accountable choice is claimed, the exact decision and its direct decision governor. A generic result reference, the selection work by itself, or a visible mapping artifact selects nothing. These neighboring objects may designate or warrant the selection claim but do not enter the structure's four discriminators or make a crossing obtain.

### A.6.9:5 - Archetypal Grounding

#### A.6.9:5.1 - System archetype: IAM User and CRM Customer

The ambiguous sentence is: “An IAM User is the same as a CRM Customer.”

Resolve exact endpoints:

- `SenseCell(IAMRoleReferenceScheme-v3, User-human-or-service-account-role)`;
- `SenseCell(CRMRoleReferenceScheme-v5, Customer-commercial-party-role)`.

Current meanings share some human participants, while service accounts and prospects provide counterexamples. Profile `P-IAM-CRM-OVERLAP-v2` states only the symmetric `Partial-overlap` relation, exact endpoint readings, overlap and difference conditions, edition basis, truth condition, and required membership evidence. Those facts make Bridge `b-iam-crm` obtain.

Now state the use separately. Dashboard team proposes `u-actor-label`: render IAM users as “actors” in a CRM-oriented comparison. Direction `d-iam-crm` is IAM-to-CRM dashboard reading. Rule `r-actor` keeps account eligibility and customer eligibility visible as separate columns. Tolerance `t-actor` allows the shared label but no eligibility, assignment, workflow, or Work inference. A C.2.1 claim about `b-iam-crm` is affirmative for `<u-actor-label,d-iam-crm,r-actor,t-actor>`.

The exact A.10 evidence-provenance relation and `RelianceDisposition=pass` support that claim only for the named dashboard comparison. They do not authorize data processing, assign a role, or prove that a dashboard publication occurred. Reverse label reuse is another bounded-use claim even though the Bridge relation is symmetric.

An optional actual card may package the Bridge claim, this bounded-use claim, observed counterexamples, the A.10 path and disposition, currentness, and nearest non-use. Its EntityOfConcern is `b-iam-crm`; the card neither creates the relation nor performs the dashboard work.

If a later workflow isolates `HumanVerifiedUser` and `VerifiedCustomer`, refine both cells and test another Bridge. A stronger use claim over the broad cells cannot repair a false or unsuitable predicate.

#### A.6.9:5.2 - Episteme archetype: Person in two knowledge-graph schemes

The sentence is: “Person in KG-A is equivalent to Person in KG-B.” The exact cells are `Person-including-fictional` under KG-A v4 and `Person-real-with-external-id` under KG-B v7. Sherlock Holmes and the external-id rule show `Partial-overlap`, not equivalence. The exact overlap Bridge obtains under the least-committing profile.

Two proposed uses then receive separate claims. A glossary comparison that labels both rows “Person” while displaying the fiction and external-id differences can receive affirmative polarity with a warranted A.10 path. A type-structure merge receives negative polarity because its correspondence rule cannot preserve membership and its tolerance permits no such loss. Both claims concern the same Bridge; neither changes its identity. Refining KG-A into `RealPerson` and `FictionalPerson` changes an endpoint and opens a new Bridge test.

#### A.6.9:5.3 - Published NAICS language and a `Conformist` cue

Start with separate objects. C.2.1 identifies exact model episteme edition `NAICS-2022-ClassificationEpisteme` by its exact ClaimGraph, EntityOfConcern, and effective ReferenceScheme; A.1 independently identifies exact `IndustryClassificationApplication-7 : U.System`. If availability matters, E.24.PUB separately tests `EpistemePublicationRelation(NAICS-2022-ClassificationEpisteme, ClassificationAudienceDeclaration-2, ClassificationUseDeclaration-5, NAICS-2022-TableForm, NAICS-2022-PDFCarrier)` together with its exact form-expression and form-bearing occurrences. The episteme, publication occurrence, form, carrier, declarations, and application system keep different identities. Publication makes an edition available; it neither puts NAICS inside the application nor proves access, adoption, applicability, actual use, or Work.

Recover the use branch before selecting structure. Require `HolderSystem(ClassificationAssignment-3)=IndustryClassificationApplication-7`, exact F.6 `performedUnderAssignment(ClassificationWork-4, ClassificationAssignment-3)`, and the application's actual use of the selected NAICS content during that Work concerning exact `ClassifiedOrganization-42`; only then may `ModelUseRelation(ClassificationAssignment-3, NAICS-2022-ClassificationEpisteme, ClassificationWork-4, ClassifiedOrganization-42)` obtain. A positive `NAICSClassificationModelUseStructure` additionally requires exact `ModelApplicabilityRelation(NAICS-2022-ClassificationEpisteme, ClassifiedOrganization-42, ClassificationClaimScope)`, fixed-content coherence with the exact classification-expression episteme under a declared predicate and ReferenceScheme, exact applied constraint claims naming the edition and classification distinctions to preserve, and `NAICSClassificationFrame`: ask which NAICS edition and distinctions govern this classification; use the complete organization for that claim; infer neither use from publication nor system parthood from the word *context*. Without the complete A.1.1/A.22 basis, stop at publication availability or the exact direct relation that does obtain.

Treat DDD *Conformist* only as a Plain cue to a proposed directed subject dependency. Preserve the exact proposed source, target, direction, adoption condition, dependency predicate, update authority, required preserved meaning, permitted loss, claim scope, and standard-edition basis. A positive occurrence would additionally require exact participant meanings and fillers, its direct relation kind and predicate, obtaining and applicability conditions, occurrence identity and recurrence, all supplied by one compatible direct subject governor. The current package has no such governor, so return `missing CROSS-LOCALITY-BRIDGE governor`; the label, published-language status, a table edge, or a selected structure cannot fill that gap.

An F.9 Bridge may separately obtain between exact NAICS-side and application-side `SchemeSenseCell` values and may support one bounded interpretation claim. It is not the proposed adoption, dependency, or update-authority relation, preserves no application meaning by itself, and supplies no subject-crossing occurrence. A later NAICS edition is another C.2.1 episteme edition: re-evaluate applicability, actual use, coherence, preservation, loss, and any future governed crossing before reselecting the structure. Republishing unchanged claims in another form or carrier does not perform that update.

### A.6.9:6 - Bias-Annotation

This pattern is biased toward:

* **Explicit action over fluent ambiguity.** It slows only sentences that would otherwise hide what someone will do.
* **Relation-use separation.** One Bridge can support several independently tested uses without becoming a licence.
* **Locality of meaning.** Exact scheme and local-sense claims provide the interpretation basis without a reified context bearer.
* **Evidence humility.** Scores, counterexamples, and invariants inform claims and reliance but do not manufacture relation truth or permission.

The dispatch stays cheap: same-context designation and direct-relation cases stop before F.9. The heavier path is reserved for a cross-local relation that a named use will actually consume.

### A.6.9:7 - Conformance Checklist

A repaired sentence or boundary statement conforms iff:

1. **Concrete action.** The reader can say what object, comparison, substitution, translation, publication, or other action is at issue.
2. **Dispatch before Bridge.** Effective reference scheme, claim scope, grounding, qualification window, exact composite project Work, viewpoint, representation transition, selected structure, direct subject relation, lane, id, role, and Work claims go to their exact owners first.
3. **Exact endpoints.** Every Bridge candidate uses two F.17 cell addresses resolving exact values.
4. **No context proxy.** Semantic bounded context is the Plain local interpretation basis recovered from the endpoint projection; it is not a project situation, model-use structure, scope, grounding, time, viewpoint, identity, or direct relation participant.
5. **Direct Bridge truth.** A positive occurrence appears only after the exact profile applies, its predicate is true, and dependencies are present.
6. **Profile boundary.** Profile identity contains relation semantics only, with no use, tolerance, polarity, reliance, authorization, or receiving object.
7. **Separate use claim.** Every proposed use names `u`, `d`, `r`, `t`, polarity, and effective scheme in a C.2.1 claim about the exact Bridge.
8. **Evidence honesty.** Observed loss and mapping witnesses stay in evidence; permitted loss stays in the bounded-use claim; `CL` grants nothing.
9. **Reliance branch.** Current reliance follows A.10 or B.3 for the same use and does not become authorization.
10. **Receiving-object boundary.** Any claim that the use happened names the actual object and states the concrete claim using the rule that defines its predicate.
11. **Card boundary.** Actual, candidate, and negative cards use the correct EntityOfConcern and never create a Bridge or receiving occurrence.
12. **Change honesty.** Endpoint, profile, use claim, reliance, card, publication, and receiving-object changes remain distinct.
13. **No inverse or composition.** An asymmetric inverse, opposite use direction, or direct A-to-C Bridge gets its own exact judgement.
14. **Practical result.** The final sentence tells the reader what to do, what not to infer, and what condition would stop or reopen the result.
15. **Same-locality route.** Same projection uses ordinary designation and, when claim extent changes, A.2.6 `widen`, `narrow`, or `refit`; it does not mint a Bridge.
16. **RT boundary.** An ordinary A.6.3.RT note states the same concern, preserved content, representation delta, loss, use, and return. A triggered exact construction adds exact `X`, `Y`, and `v`; actual representation-transformation Work enters only when the later-specific six-participant occurrence is asserted. None is scope translation or a Bridge.
17. **Structure boundary.** Each participating `BoundedModelUseStructure` is independently selected; every selected subject crossing satisfies the predicate and obtaining condition defined for that relation, with its participants and occurrence identity explicit; and the conditional A.22 cross-structure selection names exact substrate, relation organization, applied constraints and invariants, receiving-use frame, selection work or judgment, exact result, and the rule that defines it. Missing relation law returns the A.6.RCD missing-governor stop; shared participants, labels, references, Views, diagrams, Cards, and generic result refs establish none of these facts.
18. **Grounding and endpoint distinctions.** Grounding holon and EntityOfConcern are not assumed identical; every SenseCell, description episteme, designator, and reference remains distinct.
19. **Published-model crossing stop.** The NAICS replay independently identifies the exact episteme edition and application system, keeps E.24.PUB occurrence/form/carrier separate, recovers applicability and actual model use before structure selection, and treats *Conformist* as a proposal only. A positive adoption, dependency, or update-authority crossing requires a current pattern that defines its predicate, obtaining condition, and identity rule; an F.9 Bridge, label, publication, or ignored edition change cannot supply it.

### A.6.9:8 - Common Anti-Patterns and How to Avoid Them

| ID | Anti-pattern | Failure | Repair |
| --- | --- | --- | --- |
| `AP-XCTX-1` | Bridge by adjective | *Same* or *aligned* hides relation and action. | Name the action; dispatch it; test F.9 only if semantic correspondence remains. |
| `AP-XCTX-2` | Scheme difference becomes relation | Two schemes differ, so a Bridge is presumed. | Treat difference as a trigger only; establish the direct predicate. |
| `AP-XCTX-3` | Profile as use licence | Direction, rule, or tolerated loss is embedded in profile identity. | Move it to the separate C.2.1 bounded-use claim. |
| `AP-XCTX-4` | Bridge-alone substitution | An obtaining Bridge is cited as sufficient for a use. | Require the affirmative bounded-use claim and current A.10 or B.3 reliance. |
| `AP-XCTX-5` | Mapping witness becomes semantics | A lookup, score, or ETL path proves the relation or use. | Keep it as evidence and test both propositions explicitly. |
| `AP-XCTX-6` | String or id becomes endpoint | A word, file, id, or system fills a SenseCell slot. | Resolve the exact F.17 cell; handle ids under A.6.6. |
| `AP-XCTX-7` | Symmetry grants two use directions | One symmetric occurrence is read as two licences. | State each direction in its own use claim. |
| `AP-XCTX-8` | Loss note becomes tolerance | An observed difference is assumed acceptable. | Keep it in evidence and name accepted loss as `t`. |
| `AP-XCTX-9` | Confidence laundering | Higher `CL` or reviewer approval grants a use. | Treat `CL` as evidence shorthand and recover claim polarity plus reliance. |
| `AP-XCTX-10` | Suitability becomes permission | An affirmative semantic claim is read as authorization. | Open the exact policy or deontic governor, or state no authorization. |
| `AP-XCTX-11` | Named use becomes occurrence | “Publication use” is treated as a publication. | Recover the exact publication occurrence under E.24.PUB or another receiving object under its actual owner. |
| `AP-XCTX-12` | Chain upgrade | A-to-B and B-to-C become direct A-to-C equivalence. | Test a direct A-to-C Bridge and composite use independently. |
| `AP-XCTX-13` | Timeless or facetless claim | Edition or compared facet stays hidden. | State applicability and refine endpoint readings. |
| `AP-XCTX-14` | Kernel promotion | A strong Bridge is used to admit one global U-kind. | Apply E.24.UK and A.11 independently. |

### A.6.9:9 - Consequences

* **Pros**

  * Turns ambiguous sameness into a visible relation question and a visible action question.
  * Lets one Bridge remain stable while use direction, tolerance, evidence, and polarity change.
  * Prevents scores, cards, assurance, and publications from becoming hidden permission or occurrence.
  * Gives authors exact local stops instead of a vague “not equivalent”.

* **Cons**

  * A positive use normally needs two sentences instead of one adjective.
  * Reviewers must inspect the correspondence rule, tolerated loss, and evidence for the named action.
  * Many attractive “same” claims become only an explanatory comparison or a negative use claim.

**Adoption test (PRAG).** Take one sentence containing *same*, *equivalent*, *align*, or *map*. A practitioner passes when they can name the concrete action, route non-semantic branches, identify the two exact cells, say whether the Bridge obtains, state the separate bounded-use claim and reliance branch, and name any authorization or receiving occurrence still missing. Otherwise keep the sentence explanatory and return the exact missing fact.

### A.6.9:10 - Rationale

Cross-context sameness wording is not one predicate. A.6.9 first restores the actual question and states designation, lane, id, scope, representation, structure, role, and Work claims in ordinary language using their concrete rules. Add exact C.2.1 assertion and `ClaimGraph` identity only when a later use must carry or compare one of those claims independently. Only a remaining cross-local semantic question uses the F.9 Bridge predicate.

For that branch, exact cells and a relation-only profile make correspondence falsifiable. A separate C.2.1 claim makes the proposed use equally explicit without reidentifying the Bridge. A.10 or B.3 can reopen reliance without changing either object. Authorization and the actual receiving object remain visible rather than hiding inside *suitable*, *aligned*, or *mapped*.

The repair sequence is therefore: **name the action; route the object; test the relation; state the use; check reliance; recover permission or performance only when claimed.**

### A.6.9:11 - SoTA-Echoing

(informative; post-2015 alignment)

| SoTA practice | Primary source | What A.6.9 echoes | What A.6.9 adds | Stance |
| --- | --- | --- | --- | --- |
| Correspondences between viewpoints | ISO/IEC/IEEE 42010:2022 | Correspondence is not identity and retains intent and constraints. | Separates the direct semantic relation from each proposed use and actual publication or view object. | **Adopt + specialise** |
| Declarative validation shapes | W3C SHACL (2017) | Make implicit conditions testable. | Uses a profile for relation truth, a claim for bounded-use suitability, and a card only for packaging. | **Adapt** |
| Scored entity alignment with error analysis | BootEA (Sun et al., 2018) and later KG-alignment literature | Alignment evidence is graded and fallible. | Keeps scores and counterexamples as evidence rather than relation identity or a use licence. | **Adapt** |
| Textual entity matching | BERT-INT (Tang et al., 2020); Ditto (Li et al., 2021) | Matchers yield conditional, error-prone correspondences. | Requires exact endpoint readings, a falsifiable Bridge predicate, and a separate action-specific claim. | **Adopt conceptually** |
| Heterogeneous schema matching | SMAT (Zhang et al., 2021) and later neural or LLM matching work | “Match” covers several relation types. | Distinguishes relation kind, relation orientation, proposed-use direction, rule, and tolerance. | **Adapt** |
| Human-in-the-loop matching | Mudgal et al. (SIGMOD 2018) and follow-on work | Scores require abstention and curated error cases. | Uses the exact A.10 evidence or B.3 assurance predicates and preserves explicit negative or blocked outcomes. | **Adapt** |

### A.6.9:12 - Relations

* **Specialises:** A.6.P by restoring the concrete object and action hidden by cross-context sameness wording.
* **Uses:** F.17 exact `SchemeSenseCell` identity; F.9 Bridge participants, relation-only profile, obtaining, occurrence identity, bounded-use boundary, and card boundary; C.2.1 claim identity and polarity; A.10 or B.3 for reliance.
* **Coordinates with:** F.18 and F.5 for designators; A.6.6 for identifiers; C.2.1 for effective reference scheme, episteme edition, and empirical grounding; A.2.6 for scope operations; A.15.6/A.15.1 for exact composite project Work; the patterns that define the temporal and direct predicates for their qualification windows; E.17.0 for viewpoint conformance and View membership; E.24.PUB for publication occurrence, form, and carrier; C.29 for mathematical representation; A.6.3.RT for the ordinary same-concern representation note, triggered exact construction, and later-specific occurrence only when actual Work is current; C.3.3 for classification transfer; A.1.1/A.22 and the pattern that defines each selected structure crossing; direct policy or deontic patterns for authorization.
* **Constrains:** every dependent use to cite an obtaining Bridge, state a separate C.2.1 claim for its exact direction, rule, tolerance, and polarity, recover current reliance, and state any claim about the actual receiving object using the rule that defines its predicate.

### A.6.9:End

