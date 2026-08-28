## F.9 - Alignment and Bridge across Contexts
> **Type:** Pattern
> **Status:** Stable

**"Translate across contexts; never collapse them."**

**Type:** Architectural pattern.
**Status:** Stable.
**Normativity:** Normative.
**Builds on:** F.17 for exact scheme-based `SchemeSenseCell` identity and `SenseCellAddressRef`; F.18 for designation selection; C.2.1 for assertion and description-episteme identity; F.0.1 for `senseFamily` and bridge-only crossing discipline; F.7 and F.8 for downstream naming and reuse decisions.

**Coordinates with:** A.6.REL for demand-driven occurrence individuation; C.2.1 for assertion, occurrence-description, and Card identity; E.24.PUB for publication occurrence, form, and carrier; A.10 for evidence-provenance relations and local reliance dispositions; B.3 for actual named assurance claims and their bounded `AssuranceResult` values; E.10.ROLE for claim-bearing source wording with *role*; A.2, C.3, F.4, F.5, and A.2.1 for local system-role kinds and assignments; A.13 and A.15.1 for exact actual performers and independently admitted Work; F.6 only for a precise assignment-bound attribution expressly consumed by the Bridge use; A.6.5 for relation-slot discipline; C.29 for mathematical-lens use; A.6.3.CSC for controlled coarsening; C.26.1 and C.26.2 for quantum-like export boundaries.

**Plain entry cues (informative).** Context-to-context translator; sense bridge.

### F.9:1 - Intent and applicability

**Intent.** Govern one actual semantic `Bridge` relation between two exact F.17 `SchemeSenseCell` values from different semantic contexts. Keep that occurrence separate from every assertion, Bridge description episteme, Bridge Card, registry record, publication occurrence, publication form, presentation carrier, bounded-use claim, evidence or assurance relation, and object created when a proposed use is actually performed.

**Applicability.** Use this pattern when an author needs to compare local senses across contexts, reuse a familiar label, connect design-time and run-time senses, compare two standards' terms, or justify a cross-context row. A shared word or available mapping is only a reason to ask whether a Bridge obtains.

**Primary EntityOfConcern in plain terms.** One actual correspondence or difference between two exact local senses. This pattern concerns the direct `Bridge` occurrence, not a card, context, transport chain, work process, local system-role kind, assignment occurrence, evidence item, or global meaning layer.

**Admissible move in plain terms.** First resolve the two local senses. Then state and test the correspondence or difference between them. If the Bridge obtains, state the proposed use separately: what the reader will do, direction, correspondence rule, and tolerated loss. A current C.2.1 claim answers whether the Bridge suits that bounded use. Check ordinary reliance under A.10; use B.3 only when an actual named assurance claim is current. If the use happened, recover its Work, assertion, publication, relation, operation application, or other object under its subject pattern. Add a Bridge Card only when a reusable package is worth maintaining.

**Primary working reader.** An author, checker, or practitioner deciding first whether a cross-local semantic relation actually obtains and then whether it supports one named use.

**Use this when.** Use F.9 when a receiving claim needs an exact semantic relation between two local senses whose `<ReferenceScheme, LocalSenseClaim>` interpretation bases differ. Different schemes, identical spelling, a mapping implementation, or a request for comparison does not establish that relation.

**What goes wrong if missed.** Teams turn shared labels and convenient mappings into silent equivalence, substitution, structural inference, status transfer, classification under a local system-role kind, or assignment to it. They also mistake evidence about a proposed use, or a polished card, for the relation itself.

**What this buys.** A reader can see which relation is true, which proposed use is being judged, what evidence supports reliance on that judgement, and whether any downstream act actually happened. Those facts can change independently without silently merging local meanings.

**Not this pattern when.** Not F.9 when the case is still inside one semantic context, or when the live question is a local system-role kind, assignment occurrence, performed-work attribution, evidence use, status use, source use, publication, assurance, authorization, a gate, a decision, or a mathematical-lens operation. Use the subject pattern for that object; cite F.9 only when cross-context semantic correspondence is also needed.

**Recognition versus assurance note.** Resolving the endpoint senses and testing the direct Bridge predicate recognizes the semantic relation. A separate C.2.1 claim judges one bounded use. A.10 states whether ordinary evidence reliance passes. When an actual named assurance claim is current, B.3 supplies its bounded result for the same use. None of those steps supplies legal, policy, or deontic authorization.

### F.9:2 - Problem frame

Cross-context work fails in predictable ways:

1. **String-equals fallacy.** Identical spellings such as "process", "role", "accuracy", or "ready" are taken as identical meaning.
2. **Relation-to-use jump.** A true semantic correspondence is treated as sufficient for whatever comparison, substitution, translation, or publication is wanted next.
3. **Design-run jumping.** Design artefacts are substituted for run-time occurrences, or run-time occurrences are treated as design definitions.
4. **Direction amnesia.** A symmetric relation is read as two use licences, or narrower and broader senses are used in the unsafe direction.
5. **Loss blindness.** The proposed use does not name which differences it tolerates.
6. **Evidence and permission collapse.** A score, card, or assurance record is treated as the semantic relation, authorization, or proof that the use occurred.

F.9 answers these failures by separating the direct relation, the bounded-use proposition, reliance on that proposition, optional packaging, authorization, and any actual receiving object.

### F.9:2.1 - Problem

A shared label across contexts can look like identity or permission before any semantic relation is tested. Even after a Bridge obtains, its truth does not answer whether one particular comparison or substitution is suitable. The problem is to preserve useful cross-context work while keeping the relation, the proposed use, its evidence, and the downstream act individually testable.

### F.9:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Locality versus reuse | Senses are context-local, yet people need common labels and comparison points across contexts. |
| Simplicity versus fidelity | Few Bridge kinds are teachable; too few hide material semantic differences. |
| Relation truth versus practical use | A correspondence can obtain while a proposed direction, rule, or tolerance is unsuitable. |
| `senseFamily` continuity versus explanation | Some relations compare senses within one family; others explain a cross-family connection without making them substitutable. |
| Evidence versus authorization | Evidence or assurance may support reliance on a bounded-use claim but does not grant legal, policy, or deontic permission. |
| Bridge discipline versus subject patterns | F.9 defines how to state semantic correspondence; using it must not create local system-role kinds or assignments, work, evidence relations, publications, or status occurrences. |

### F.9:4 - Solution

Start with the two exact local senses, not with a context object, mapping table, or card. Resolve each endpoint as an F.17 `SchemeSenseCell` coordinate:

```text
<ReferenceScheme by value, LocalExpression, LocalSenseClaim>
```

For F.9, **semantic bounded context** is a Plain practice name for the local interpretation basis recovered from one exact cell's `<ReferenceScheme, LocalSenseClaim>` projection. It is not an entity, relation participant, selected model-use structure, project situation, scope, viewpoint, description, designator, or reference. Two expressions under the same projection remain with ordinary designation and scope operations. Different projections make a Bridge question possible but do not make a Bridge obtain.

When the two cells are from different semantic contexts, declare one relation-semantic `BridgePredicateProfile` and test it against their current meanings. Shared spelling, different schemes, a mapping implementation, a card, a registry entry, evidence, an assessment score, or publication establishes none of those facts by itself.

#### F.9:4.1 - Direct Bridge relation

`Bridge` is a direct species of `U.Relation`. Its reusable `RelationSignature` has exactly two participant meanings:

| SlotKind | ValueKind | refMode | Participant meaning |
| --- | --- | --- | --- |
| `SourceSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact source local sense, resolving its by-value reference scheme, local expression, and local-sense claim. |
| `ReceivingSenseCellSlot` | F.17 `SchemeSenseCell` coordinate | `SenseCellAddressRef` | The exact receiving local sense used by the claimed semantic relation. |

Only the two endpoint meanings are RelationSignature participants. `CL`, Loss Notes, `U.ClaimScope`, an admitted-use qualifier, evidence, counterexamples, policy, time or as-of values, `BoundedModelUseStructure`, description, Card, publication, registry identifier, form, and carrier are qualifiers or neighboring objects. No proposed-use field, use direction, use-specific rule, permitted-loss tolerance, assertion, or reliance result is a third participant.

The reusable Bridge declaration is one independently constituted C.2.1 episteme whose exact EntityOfConcern is the direct `Bridge` relation kind. The same declaration episteme is used relation-facing as the compatible `RelationSignature`; its two SlotSpecs declare participant meanings but create neither endpoint nor occurrence. The relation kind, declaration episteme, RelationSignature use, SlotSpecs, actual cells, obtaining occurrence, assertion, occurrence-description episteme, Card, and publication remain distinct.

An F.9-local `BridgePredicateProfile` is a by-value predicate declaration, not a U-kind, participant, card, claim, or evaluation result. Direction is stated in the Bridge kind and endpoint orientation when the predicate is asymmetric. Its identity-bearing content is only:

1. the `BridgeKind` and its kind-defined symmetry or endpoint orientation;
2. the exact source and receiving endpoint-sense readings, including their `senseFamily` readings where material;
3. the relation-kind-specific congruence, difference, or loss condition, distinct from observed Loss Notes and a proposed use's permitted-loss tolerance;
4. the applicability and as-of basis for testing that condition;
5. the Boolean truth condition; and
6. every stop dependency whose absence prevents a truthful result.

The profile contains no proposed-use field, use direction, use-specific correspondence rule, permitted-loss tolerance, bounded-use proposition, assertion polarity, evidence-reliance classification, assurance claim, authorization, or receiving object.

`Bridge(SourceSenseCell, ReceivingSenseCell; BridgePredicateProfile)` obtains exactly when:

- both endpoint references resolve to exact F.17 `SchemeSenseCell` values;
- their semantic-context projections differ;
- the profile applies to those endpoint readings at its stated as-of basis;
- the current endpoint meanings satisfy its kind-specific correspondence or difference condition and Boolean truth condition; and
- every required dependency is present.

If an endpoint is unresolved, the projections are the same, a dependency is missing, or the predicate is false or unresolved, assert no positive occurrence and state the exact exit: ordinary designation, `unresolved SenseCell endpoint`, `same semantic context`, `missing Bridge dependency`, `Bridge predicate false`, or `Bridge predicate unresolved`.

**Admitted-use qualifier.** The Bridge declaration admits this relation only as the semantic-correspondence or semantic-difference premise for a comparison, explanation, translation, naming, or other bounded-use claim. Its nearest non-use is equally explicit: the Bridge alone licenses no substitution and creates no scope result, model-use crossing, local system-role kind, assignment occurrence, Work, evidence authority, status transfer, U-kind admission, publication, or other subject relation. This readable use boundary is a declaration or description qualifier; it is neither a participant nor profile identity and grants no specific use.

**Non-optional occurrence identity and recurrence rule.** `BridgeOccurrenceIdentityRule` identifies the occurrence by the exact endpoint cells together with the exact profile. For an asymmetric kind, the ordered source-to-receiving tuple is identity-bearing and an inverse relation requires another profile and directed occurrence. For a symmetric kind, swapping only the readable presentation of the same canonical endpoint pair does not create another occurrence. A changed endpoint or changed relation-semantic profile identifies another candidate.

A Bridge is non-recurrent for one fixed canonical endpoint tuple and exact profile: at most one occurrence has that identity. Repeated tests, assertions, descriptions, Cards, registry rows, or publications neither split nor repeat it. A later applicability or as-of basis changes the profile and therefore opens another occurrence candidate. If a claimed lapse and resumption cannot be represented by an endpoint or profile change, stop at `missing Bridge recurrence basis` rather than inventing two occurrences with one identity. Changed proposed use, direction, rule, tolerance, evidence path, reliance disposition, assurance claim, Card, registry entry, publication, form, or carrier never reidentifies or recurs the fixed Bridge.

#### F.9:4.2 - Judge a bounded use separately

Once exact Bridge `b` obtains, state the proposed use in ordinary language before introducing FPF terms. Name:

- `u`: what the reader proposes to compare, substitute, translate, publish, or otherwise do;
- `d`: the exact source-to-receiving direction for that use;
- `r`: the use-specific correspondence rule;
- `t`: the semantic-loss tolerance for that use; and
- whether the claim is affirmative or negative.

The resulting C.2.1 claim asks whether `b` is suitable for `<u,d,r,t>`. Its exact EntityOfConcern is `b`; its ClaimGraph designates `u`, `d`, `r`, `t`, and polarity; its effective ReferenceScheme makes those designations interpretable. That C.2.1 triple identifies the claim episteme. Changing `u`, `d`, `r`, or `t` changes the claim, not the Bridge.

An affirmative claim is one premise for the proposed use. It is not a permission, authorization, evidence-provenance relation, reliance classification, assurance claim, decision, or occurrence of that use. A negative claim says that the Bridge is not suitable for the named use; it does not make the Bridge cease to obtain.

For ordinary evidence reliance, recover the exact A.10 evidence-provenance relation and local `RelianceDisposition` for the same bounded use. Only `pass` supports reliance on the affirmative claim for that use; `degrade` supports only its named narrower use, while `abstain`, `reopen`, `evidence-needed`, `assurance-needed`, or `blocked-current-use` supplies no passing classification.

Use B.3 only when an actual named assurance claim about the proposed use is current. Require its result for the same bounded assurance use; a non-positive disposition stops or narrows that use. A direct domain rule may require the claim, but the Bridge, display, consequence, or A.10 disposition does not create it.

Neither an A.10 passing disposition nor a B.3 `AssuranceResult` with `disposition=supported-for-use` is legal, policy, or deontic authorization. If authorization is needed, recover it under its direct pattern. If a later claim says the use happened, recover the actual Work, assertion episteme, publication occurrence, direct relation, operation application, or other object under its own pattern; the `u` designation in the ClaimGraph names the proposed use and is not that occurrence.

### F.9:5 - Minimal vocabulary

* **Semantic context** - Plain shorthand for the interpretation basis `<ReferenceScheme, LocalSenseClaim>` recovered from an exact F.17 cell; it is not a separate entity or participant.
* **SchemeSenseCell** - the exact F.17 local composite value `<ReferenceScheme by value, LocalExpression, LocalSenseClaim>`.
* **SenseCellAddressRef** - an address that resolves one exact `SchemeSenseCell`; the address is not the cell.
* **Bridge** - an obtaining direct semantic relation between two exact `SchemeSenseCell` values from different semantic contexts under one exact profile.
* **BridgePredicateProfile** - the F.9-local by-value declaration of the direct relation's kind, symmetry or orientation, endpoint readings, correspondence or difference condition, applicability and as-of basis, Boolean truth condition, and stop dependencies.
* **Bounded-use claim** - an ordinary C.2.1 claim that says whether one exact obtaining Bridge is suitable for one named use, direction, use-specific rule, and loss tolerance. This phrase is descriptive, not a new public kind name.
* **Relation orientation** - how the Bridge kind orders or symmetrically relates its endpoint slots; it is not a use licence.
* **Use direction** - the ordered `<UseSourceSenseCell, UseReceivingSenseCell>` designated inside one bounded-use claim.
* **Observed semantic loss** - a difference or counterexample found in evidence. It can bear on a bounded-use claim but is not the use's permitted-loss tolerance.
* **Permitted-loss tolerance** - the maximum named loss accepted by one proposed use; it is content of that use's C.2.1 claim.
* **Bridge occurrence description** - an independently constituted C.2.1 episteme whose exact EntityOfConcern is one already individuated Bridge occurrence. It describes; it neither makes the predicate true nor supplies occurrence identity.
* **Bridge Card** - optional claim-bearing packaging. A filled Card may itself be a Bridge description episteme when its C.2.1 triple concerns an actual occurrence; a candidate Card instead modally describes the admitted relation kind and proposed endpoints. The reusable Card layout, registry row, publication form, and carrier remain separate.
* **CL (Congruence Level)** - optional F.9-local shorthand for the strength of evidence about a stated correspondence. It is neither a participant nor a use threshold and never grants a use.
* **senseFamily** - the local meaning family used by Part F. A `senseFamily` label is not a durable U-kind.

### F.9:6 - Bridge kinds

A Bridge kind classifies the direct semantic relation tested by a profile. It says what correspondence or difference obtains; it does not settle any proposed use.

#### F.9:6.1 - Same-family relation kinds

1. **Equivalence** - the endpoint senses have the same extension and relevant intension under the stated relation condition. The relation is symmetric and should be rare. A later use still names its direction, rule, and tolerance.
2. **Narrower-than** - the source sense is properly included in the receiving sense. The relation is asymmetric.
3. **Broader-than** - the source sense properly includes the receiving sense. The relation is asymmetric.
4. **Partial-overlap** - the senses have a non-empty intersection, while each has cases excluded by the other. The relation is symmetric.
5. **Disjoint** - the senses have no common admissible case under the stated readings. The relation is symmetric.

For inclusion, a narrower-to-broader proposed use is usually easier to justify than the reverse, but neither direction follows from the relation alone. A broader-to-narrower proposal normally needs refined endpoint cells and a separately tested Bridge plus a separately warranted bounded-use claim.

#### F.9:6.2 - Cross-family relation kinds

These kinds state semantic correspondence across different `senseFamily` readings. They explain a connection; they do not create substitution, evidence authority, policy force, or a receiving occurrence.

6. **Design-spec-to-run-occurrence** - a design sense corresponds to a run-time occurrence sense while remaining different in temporal and realization status.
7. **Measurement-evidence-for** - a measurement sense corresponds to the measured aspect of another sense. The kind is semantic; actual evidential support remains with A.10 or B.3.
8. **Policy-constraint-on** - a policy or deontic sense corresponds to a constrained behavioral sense. Actual obligation, permission, or authority remains with the policy or deontic governor.
9. **Viewpoint-correspondence** - a sense used in one view corresponds to a sense used in another view over an EntityOfConcern. View, description, publication, and source-use claims keep their subject patterns.

### F.9:7 - Evidence about relation and use

Evidence must answer the question it actually bears on:

| Evidence question | What the evidence may support | What it cannot establish |
| --- | --- | --- |
| Do the endpoint meanings satisfy the fixed profile? | the claim that the Bridge obtains, is false, or remains unresolved | suitability for an unnamed use |
| Does the Bridge suit `<u,d,r,t>`? | affirmative or negative polarity of the exact C.2.1 bounded-use claim | authorization or performance of the use |
| May the reader rely on that claim now? | an A.10 local `RelianceDisposition`; when an actual named assurance claim is current, its B.3 `AssuranceResult` for the same bounded use | the Bridge occurrence, legal permission, or a receiving occurrence |

`CL` may summarize evidence strength for a stated correspondence: `0` contradicted, `1` weakly comparable, `2` bounded support with explicit counterexamples, and `3` matched stated invariants with no current material counterexample. It is optional and never serves as a use threshold. A `CL=3` label does not make a type-structure use suitable; the separate claim must still name the rule and tolerance, and reliance must still pass under A.10 or B.3.

Observed losses, unit differences, counterexamples, and invariant checks belong in the evidence path or card. The proposed use's permitted-loss tolerance belongs in its ClaimGraph. A loss observation can change without reidentifying either the fixed Bridge or the bounded-use claim; it may instead reopen the claim's polarity or the current reliance disposition.

### F.9:8 - Bridge occurrence, description, Card, and publication

Recover and, when needed, individuate the direct relation before describing it. A Bridge may obtain without any assertion, description, Card, registry row, or publication.

A Bridge occurrence description is constituted independently under C.2.1 from exact claim content, the already individuated occurrence as EntityOfConcern, and an effective `U.ReferenceScheme`. A proposal may instead be a modal C.2.1 episteme whose EntityOfConcern is the admitted direct Bridge relation kind and whose ClaimGraph designates proposed endpoints and profile; it supplies no positive occurrence reference and makes no relation obtain.

Use a Bridge Card only when durable reuse, delayed handoff, evidence review, audit, publication, or costly reversal makes reusable packaging worthwhile. A particular filled Card can be the description episteme when its C.2.1 triple supports that exact use. Its reusable layout remains separate and functions as a publication form only while the exact E.24.PUB `PublicationFormExpressionRelation` obtains for the selected edition and bounded use. When availability matters, publish one selected description/Card edition through E.24.PUB: its `EpistemePublicationRelation` occurrence, publication form, and `U.PresentationCarrier` remain distinct from the selected episteme and from the Bridge.

```text
BridgeCard:
  ClaimMode: actual | candidate | negative
  BridgeOccurrenceRef?: exact ref, actual mode only
  EntityOfConcern: exact obtaining Bridge, or admitted F.9 Bridge relation kind for candidate or negative mode
  ProposedSourceSenseCellRef?: SenseCellAddressRef
  ProposedReceivingSenseCellRef?: SenseCellAddressRef
  ProposedBridgePredicateProfile?: by-value profile
  BoundedUseClaims?: each with u, d, r, t, polarity, and effective ReferenceScheme
  A10EvidenceUse?: exact evidence-provenance relation plus local RelianceDisposition
  B3Use?: exact AssuranceResult for the same bounded assurance use
  ObservedLossAndCounterexamples?:
  EvidenceWarrantAndCurrentness?:
  NearestNonUse?:
  CardReferenceScheme:
```

For `ClaimMode: actual`, the description/Card episteme's exact EntityOfConcern is the already individuated Bridge occurrence. It may package the Bridge assertion, one or more bounded-use propositions, their evidence and polarity, the exact A.10 relation and local disposition, or the exact B.3 `AssuranceResult` when an actual named assurance claim is current, plus currentness and nearest non-use. Its C.2.1 identity is not the occurrence identity.

For `ClaimMode: candidate` or `negative`, no positive occurrence reference exists. The modal description/Card episteme's EntityOfConcern is the admitted F.9 direct `Bridge` relation kind; its ClaimGraph designates the proposed endpoints and profile. `candidate` says the proposed Bridge may obtain; `negative` says its predicate does not obtain. Any bounded-use proposition in the same graph keeps its own polarity. Completing, approving, registering, or publishing the description/Card creates no Bridge.

The exact `<ClaimGraph, EntityOfConcern, effective ReferenceScheme>` triple identifies each description/Card episteme. A changed description or Card edition, evidence path, reliance disposition, B.3 `AssuranceResult`, registry record, E.24.PUB publication occurrence, publication form, carrier, or layout does not reidentify a fixed Bridge. Publish only the selected description/Card edition needed by the named audience and bounded use; publication changes availability, not relation truth.

### F.9:9 - Boundary to coarsening and quantum-like export

Open F.9 when a receiving use needs an actual semantic relation between exact local senses. A lossy or approximate export is not thereby a Bridge, and an actual Bridge is not thereby a quantum-like state transition.

Use this order:

1. resolve the exact F.17 cells, state the relation-semantic profile, and test whether the Bridge obtains;
2. state the proposed use separately as `<u,d,r,t>` and give the C.2.1 claim its polarity;
3. recover the exact A.10 evidence-provenance relation and local disposition or, when an actual named assurance claim is current, its B.3 `AssuranceResult` for the same use;
4. if the use happened, identify the actual governed object and apply its subject pattern;
5. add a Bridge Card only if durable packaging pays;
6. open A.6.3.CSC, C.26.1, or C.26.2 only when coarsening, probe effects, or failure of any faithful-enough report is the live question.

When a state, metric, option, causal reading, or viability claim crosses the semantic boundary, its subject pattern states what survives and what is lost. The Bridge supplies only the semantic-correspondence premise; the bounded-use claim supplies only the named suitability proposition.

### F.9:10 - Invariants

1. **Exact endpoints first.** A Bridge has exactly two F.17 `SchemeSenseCell` participants.
2. **No context object.** Semantic context is recovered from endpoint content and is not a relation participant.
3. **Different context is not enough.** Different projections trigger the question but do not establish the relation.
4. **Profile contains relation semantics only.** Receiving use, direction, use rule, loss tolerance, polarity, reliance, authorization, and receiving objects are absent from profile identity.
5. **Obtaining before occurrence reference.** A positive Bridge reference appears only after the fixed predicate is true and its dependencies are present.
6. **Use claim is separate.** Every proposed use names `u`, `d`, `r`, `t`, and polarity in a C.2.1 claim about the exact Bridge.
7. **Reliance is separate.** A.10 says whether ordinary evidence supports relying on the bounded-use claim. When an actual named assurance claim is current, B.3 supplies its bounded `AssuranceResult`. Neither answer comes from F.9 or the Card.
8. **Proposed use is not an occurrence.** The `u` designation in the ClaimGraph names the proposed use; any actual Work, assertion, publication, relation, or operation application keeps its own identity; apply the relevant pattern to each claim about it.
9. **Card separation.** Card identity, completion, approval, registration, and publication neither make the relation obtain nor make the use happen.
10. **Loss separation.** Observed semantic loss is evidence; permitted loss is tolerance inside the bounded-use claim.
11. **No authorization by implication.** Semantic suitability, evidence reliance, and assurance are not legal, policy, or deontic permission.
12. **No silent inverse or composition.** An inverse asymmetric relation and any direct A-to-C relation are tested independently.
13. **Two-SlotSpec declaration.** The reusable RelationSignature declares only source and receiving SenseCell participant meanings; `CL`, Loss Notes, scope/admitted use, evidence, counterexamples, policy, time, model-use structure, description, publication, and registry values remain qualifiers or neighbors.
14. **Recurrence and identity.** The non-optional identity rule uses the canonical exact endpoints and exact profile; one fixed tuple/profile is non-recurrent, and a changed applicability/as-of basis changes the profile before another candidate is admitted.
15. **Description and publication separation.** A Bridge description/Card is independently constituted under C.2.1, and E.24.PUB independently governs any selected edition's publication occurrence, form, and carrier. None establishes relation truth or identity.

### F.9:11 - Micro-examples

The labels below are readable aliases. An actual case resolves exact F.17 cells and tests one profile before stating a proposed use.

1. **Participant versus Agent.** A `Partial-overlap` Bridge may obtain between the exact BPMN and PROV senses. A separate claim may affirm use of the label "actor" in one orientation table under a rule that preserves the stated participation distinction. That claim creates no local system-role kind or assignment occurrence.
2. **Process design versus Activity occurrence.** A `Design-spec-to-run-occurrence` Bridge may explain the semantic connection. A separate claim can bound an explanatory use; it does not identify a run occurrence from a design artefact.
3. **Observation versus SLO fulfilment.** A `Measurement-evidence-for` Bridge can relate the exact senses. A separate claim asks whether the observation sense is suitable for interpreting one named SLO comparison. A.10 handles ordinary evidence reliance; when an actual named assurance claim is current, B.3 supplies its bounded result for that use.
4. **Subtype across OWL and a curated taxonomy.** An `Equivalence` Bridge obtains only under a profile whose relation condition includes the required class-level invariants. A separate claim asks whether one exact type-structure row may use that Bridge under its stated rule and zero material-loss tolerance.
5. **Accuracy in metrology versus data quality.** A `Partial-overlap` Bridge can make the shared word intelligible. A bounded-use claim may affirm that the label is suitable in one explanatory table while rejecting transfer of measurement methods or values.

### F.9:12 - Worked examples

#### F.9:12.1 - Service target and monitoring observation

A service team resolves two exact cells: the ITIL sense of an availability target and the SOSA sense of an availability observation. Profile `P-SLO-OBS-v2` states a `Measurement-evidence-for` semantic relation: the observation sense concerns a measured availability quantity relevant to the target sense, while observation and target remain different kinds of claim. The profile names the endpoint readings, direction of the semantic relation, applicability to the cited editions, Boolean condition, and required quantity-definition dependency. Current meanings satisfy it, so Bridge `b-slo-obs` obtains.

The team next proposes use `u-slo-check`: compare one observation result with the target. Direction `d-slo` is observation-to-target; rule `r-slo` requires the same quantity kind, aligned windows, and the stated unit conversion; tolerance `t-slo` permits the named rounding loss but no quantity-kind change. A C.2.1 claim with EntityOfConcern `b-slo-obs` states affirmative polarity for `<u-slo-check,d-slo,r-slo,t-slo>`.

Because this is an ordinary bounded evidence use and no assurance claim is made, the team recovers the exact A.10 evidence-provenance relation for the observation record and states `RelianceDisposition=pass` only for `u-slo-check`. That supports reliance within its boundary. It does not make the SLO fulfilled, authorize acceptance, or prove that comparison Work occurred.

#### F.9:12.2 - Behavioral participant and access role

An exact `Partial-overlap` Bridge obtains between a BPMN participant sense and a named RBAC role sense when the profile's overlap and difference conditions are satisfied. A separate bounded-use claim proposes the label "actor" for one glossary row, in the stated direction, under a rule that preserves assignment moment, enforcement locus, multiplicity, and accountability differences, with zero tolerance for reading the label as a local system-role kind or assignment occurrence. Current evidence can support that label use under A.10.

When a later claim uses the RBAC source word *role*, apply `E.10.ROLE` and first say whether it concerns access, permission, authority, a work-facing classification, an assignment, or performed Work. For access, permission, or authority, use the direct pattern for that relation. Use A.2.8.PER for granted permission while keeping actual access separate. If access wording still hides the subject or relation, use A.6.P:4.11a; if the participants and predicate are clear but no direct pattern defines the relation, return A.6.RCD `missing-governor[direct access relation]`.

A work-facing classification separately requires an admitted System, one exact local system-role kind with its `KindSignature`, and the C.3.2 classification judgment under A.2 and C.3. Use F.4 only when the receiving use separately needs a `SystemRoleKindDescription` episteme, and F.5 only when it needs a durable designation. An assignment claim then separately identifies an occurrence of a directly declared species under `U.SystemRoleAssignment` through A.2.1.

If performed Work is also claimed, recover every exact actual performer through A.13 and use A.15.1 to identify the dated Work, exact Method, time, and containing System independently. Add an assignment occurrence and F.6 only when the Bridge account or receiving use expressly represents precise assignment-bound attribution and can supply the direct case fact linking the exact Work-assignment pair. Missing or failed F.6 leaves the Work intact. The Bridge, bounded-use claim, and reliance result establish none of these facts.

#### F.9:12.3 - Subtype notions in one structural row

The endpoint senses are `OWL2:SubClassOf` under a cited OWL profile and curated-taxonomy `is-a` under one named taxonomy edition. The Bridge profile states `Equivalence` and makes its direct relation predicate true only when both endpoint meanings use compatible class-level reasoning and satisfy the stated acyclicity and anti-symmetry conditions. When those facts and dependencies are current, the exact Bridge obtains.

A second premise is still required. The C.2.1 claim names the proposed type-structure row, its source-to-receiving direction, the rule that preserves the three invariants, and zero material-loss tolerance. Only an affirmative current claim with passing A.10 reliance, or, when an actual named assurance claim is current, a B.3 `AssuranceResult` for the same use with `disposition=supported-for-use`, supports relying on the row. A contradicted relation invariant makes the Bridge predicate false; a use-specific tolerance failure can instead make the bounded-use claim negative while the Bridge remains unchanged.

#### F.9:12.4 - Setpoint versus service target

`CTRL:setpoint` and `ITIL:target` share a familiar word but usually have only `Partial-overlap` or are `Disjoint` under the exact readings. A proposed substitution in a control calculation receives a negative bounded-use claim because its rule and tolerance cannot preserve the physical-reference meaning. A didactic comparison may receive a different affirmative claim. Neither claim changes which Bridge obtains.

### F.9:13 - Common Anti-Patterns and How to Avoid Them

| ID | Anti-pattern | Symptom | Repair |
| --- | --- | --- | --- |
| AP-1 | String-equals becomes sense-equals | Same spelling is used as proof of identity. | Resolve the exact cells and test the least-committing relation profile. |
| AP-2 | Profile as use licence | Direction, use rule, or tolerated loss is placed inside profile identity. | Keep only relation semantics in the profile; state `<u,d,r,t>` in a separate C.2.1 claim. |
| AP-3 | Bridge-alone substitution | “A corresponds to B, therefore use A as B.” | Require both the obtaining Bridge and an affirmative bounded-use claim, then check A.10 or B.3 reliance. |
| AP-4 | Symmetry grants two directions | An `Equivalence` Bridge is treated as two approved substitutions. | State and test each proposed use direction separately. |
| AP-5 | Inclusion grants the reverse use | A broader sense is silently substituted for a narrower one. | Refine the endpoint senses and test the reverse relation and bounded use independently. |
| AP-6 | Assessment score grants use | `CL=3` is cited instead of the exact rule, tolerance, and reliance path. | Treat the score as optional evidence shorthand; write and warrant the bounded-use claim. |
| AP-7 | Loss note becomes tolerance | An observed difference is treated as automatically acceptable. | Put observed loss in evidence and the accepted maximum in the claim's `t`. |
| AP-8 | Card creates relation or permission | An approved or published card is cited as obtaining or authorization. | Test the Bridge independently and recover authorization under its direct governor. |
| AP-9 | Named proposed use becomes an actual occurrence | The claim says “publication use” or “comparison use”, so a publication or comparison is presumed. | Recover a publication occurrence under E.24.PUB; recover any comparison or other receiving object under A.15.1, C.2.1, A.6.1, or its direct domain-relation pattern. |
| AP-10 | Evidence failure erases the Bridge | A stale evidence path is said to make the semantic relation disappear. | Reopen reliance or the use claim; change the obtaining claim only when endpoint facts or the profile predicate changed. |
| AP-11 | Bridge as durable U-kind | A local correspondence is used to globalize meaning. | Keep kinds context-local unless the exact admission patterns independently admit a U-kind. |
| AP-12 | Silent relation composition | A-to-B and B-to-C are used as an A-to-C occurrence. | Test and individuate the direct A-to-C Bridge separately. |
| AP-13 | Description identity becomes occurrence identity | A description/Card C.2.1 triple or registry id is used to identify the world-side Bridge. | Apply `BridgeOccurrenceIdentityRule` to exact endpoints and profile; identify the description separately. |
| AP-14 | Same-locality Bridge | Two designations under one exact projection are forced into F.9. | Use ordinary designation and A.2.6 scope operations; no F.9 occurrence is current. |
| AP-15 | Bridge creates another subject fact | Semantic correspondence is said to create a local system-role kind or assignment, perform Work, authorize evidence, transfer status, admit a U-kind, publish an episteme, or relate model-use structures. | Use the pattern that defines that subject relation or state the missing-governor stop. |

### F.9:14 - Reasoning primitives

These are conceptual judgements, not work-enactment, card-completion, registry, publication, permission, or authorization rules.

#### F.9:14.1 - Direct Bridge occurrence

```text
P = <kind, symmetry-or-orientation, endpoint-readings,
     relation-condition, applicability-and-as-of,
     Boolean-truth-condition, stop-dependencies>

Bridge(A, B; P) obtains
iff
  A and B resolve to exact F.17 SchemeSenseCell values,
  semanticContext(A) != semanticContext(B),
  applicable(P, A, B, asOfBasis),
  bridgePredicate(P, A, B) = true,
  and requiredDependencies(P) are present.
```

No proposed use, direction, use-specific rule, loss tolerance, claim polarity, reliance result, or card is a component of `P`.

#### F.9:14.2 - Bounded-use proposition

```text
Bridge(A,B;P) obtains as b
and C is a C.2.1 claim with
  EntityOfConcern = b,
  ClaimGraph designating <u,d,r,t,polarity>,
  and an effective ReferenceScheme interpreting those designations
=> C says whether b is suitable for exactly <u,d,r,t>.
```

Changing `u`, `d`, `r`, or `t` changes `C`; it does not change `b`. Affirmative polarity is not evidence reliance, assurance, authorization, or occurrence.

#### F.9:14.3 - Ordinary A.10 reliance

```text
C is current and affirmative for <u,d,r,t>
and EP is the exact A.10 evidence-provenance graph relation for C and u
and RelianceDisposition(EP,u,d,r,t) = pass
=> the reader may rely on C only for that bounded evidence use.
```

A non-passing or narrower disposition supplies no support for the attempted use. The disposition is a local A.10 classification statement, not a new result kind.

#### F.9:14.4 - B.3 assurance branch

```text
C is current and affirmative for <u,d,r,t>
and an actual named assurance claim about this use is current
and its B.3 AssuranceResult carries the same bounded assurance use
and disposition = supported-for-use
=> assurance supports only that bounded use.
```

A `narrowed` disposition supports only its stated narrower use. `abstain`, `evidence-needed`, `reopen`, or `blocked` stops the attempted use. If no assurance claim is current, do not open B.3. A consequence, display, or local threshold creates no assurance claim.

#### F.9:14.5 - Receiving occurrence stays separate

```text
Bridge b obtains
and C is affirmative for proposed use u
and current reliance supports C for u
=> no Work, assertion, publication, relation, or operation application follows.
```

An actual receiving object exists only when its subject pattern supplies its participants or arguments, obtaining or performance facts, and identity.

#### F.9:14.6 - Direction guard

Relation symmetry or orientation does not select `d`. Each proposed direction receives its own bounded-use claim. For an inclusion relation, a broader-to-narrower proposal normally requires refined endpoint senses and a separately tested Bridge; it cannot borrow safety from the inverse reading.

#### F.9:14.7 - Chained-use guard

```text
Bridge(A,B;P1) obtains
and Bridge(B,C;P2) obtains
=> no Bridge(A,C;P3) follows.
```

A composite proposed use must cite each obtaining Bridge, state one exact composite rule and accumulated tolerance in its own claim, and recover current reliance for that claim. If a direct A-to-C correspondence is needed, test it independently.

#### F.9:14.8 - Candidate-card guard

```text
candidate or negative Bridge Card exists
=> no positive Bridge occurrence follows.
```

The card concerns the admitted direct Bridge relation kind and places proposed endpoints, profile, ClaimMode, and polarity in its ClaimGraph. It creates neither relation nor receiving occurrence.

### F.9:15 - Relations

**Builds on:** F.17, F.18, C.2.1, F.0.1, F.7, and F.8.

**Coordinates with:**

* **A.10.** Use it for the exact evidence-provenance graph relation and local `RelianceDisposition` for ordinary bounded evidence use.
* **B.3.** Use B.3 only after an actual named assurance claim is current; it states the bounded `AssuranceResult` or non-positive disposition and does not create the claim, authorization, or use.
* **E.10.ROLE, A.2, C.3, F.4, F.5, A.13, A.15.1, A.2.1, and F.6.** Use E.10.ROLE first when source wording leaves *role* ambiguous. Use A.2 and C.3 for the local system-role kind and any separate System-classification judgment. Use F.4 only when a description of that kind is current, and F.5 only when its durable naming is current. Recover each exact actual performer through A.13 and admit dated Work independently through A.15.1. Use A.2.1 and F.6 only when the receiving Bridge use expressly consumes precise assignment-bound attribution. A Bridge establishes none of these facts.
* **F.8.** A mint-or-reuse decision may consume an obtaining Bridge plus a separately warranted bounded-use claim; it does not strengthen either.
* **A.2.6.** Scope translation may use an obtaining Bridge only together with an affirmative claim naming the exact direction, scope-correspondence rule, and loss tolerance. Use A.2.6 for the translated scope and membership.
* **A.6.1.** Use it to identify any actual operation application. The `u` designation in a Bridge claim names a proposed use and is not an application binding.
* **A.6.5.** Relation-position labels and SlotSpec claims remain governed by slot discipline.
* **C.29.** Mathematical-lens use may cite a Bridge and bounded-use claim; C.29 still governs its mathematical object, preserved and lost structure, and actual lens use.
* **C.34.** Structural correspondence or morphism adequacy may cite an obtaining Bridge and a bounded-use claim but states its own preserved and lost architecture structure.
* **A.6.REL.** Applies the F.9 recurrence and occurrence-identity rule only when a receiver must distinguish or reference the occurrence.
* **C.2.1.** Independently constitutes assertions, modal proposals, occurrence-description epistemes, and filled Cards; none supplies the Bridge predicate or occurrence identity.
* **E.24.PUB.** Use it for any `EpistemePublicationRelation` occurrence, publication form, and presentation carrier for a selected description/Card edition. Publishing creates neither Bridge nor receiving use.
* **A.6.3.CSC, C.26.1, and C.26.2.** Govern coarsening, probe effects, and no-faithful-enough-report cases when those questions are live.

### F.9:16 - Revision law

1. **Endpoint change.** A changed by-value scheme, local expression, or local-sense claim identifies another F.17 cell and requires another Bridge test.
2. **Profile change.** A changed kind, symmetry or orientation, endpoint reading, relation-specific correspondence or difference condition, applicability or as-of basis, Boolean truth condition, or stop dependency identifies another profile and occurrence candidate.
3. **Use-content change.** A changed proposed use `u`, direction, use-specific rule, or permitted-loss tolerance identifies another C.2.1 claim while the fixed Bridge remains unchanged.
4. **Polarity change.** Affirmative versus negative is changed claim content; it is not a changed reliance disposition.
5. **Evidence or reliance change.** A changed evidence item, path, currentness window, A.10 relation, local `RelianceDisposition`, or B.3 `AssuranceResult` reopens reliance without reidentifying the fixed Bridge or fixed C.2.1 claim.
6. **Obtaining change.** New endpoint facts may establish, refute, or leave unresolved the predicate for a fixed occurrence candidate without silently changing its identity.
7. **Description, Card, registry, or publication change.** Apply C.2.1 to description/Card identity and E.24.PUB to publication occurrence, form, and carrier; none creates, removes, reidentifies, or recurs the Bridge.
8. **Receiving occurrence change.** Reidentify or revise the Work, assertion, publication, relation, application, or other receiving object under its subject pattern.

### F.9:17 - Acceptance tests

#### F.9:17.1 - Static conformance

* **SCR-F9-S01 (Well-typed direct relation).** Each actual Bridge has exactly two resolved F.17 `SchemeSenseCell` endpoints and one exact relation-semantic profile.
* **SCR-F9-S02 (Different semantic contexts).** The endpoint `<ReferenceScheme, LocalSenseClaim>` projections differ; same-context aliases stay with designation resolution.
* **SCR-F9-S03 (Profile boundary).** The profile contains only kind, symmetry or orientation, endpoint readings, relation condition, applicability and as-of basis, Boolean truth condition, and stop dependencies.
* **SCR-F9-S04 (Obtaining).** Current endpoint facts satisfy the exact profile and all required dependencies are present. Scheme difference, spelling, implementation, evidence score, card, registry, or publication alone fails this test.
* **SCR-F9-S05 (Separate bounded use).** Every use claim identifies exact Bridge `b`, names `u`, `d`, `r`, `t`, polarity, and an effective ReferenceScheme under C.2.1.
* **SCR-F9-S06 (Reliance branch).** The same bounded use has the exact A.10 relation plus a passing local disposition or, when an actual named assurance claim is current, its exact B.3 `AssuranceResult`; only `supported-for-use` supports the attempted assurance use, while `narrowed` supports only its stated narrower use.
* **SCR-F9-S07 (No authorization overread).** Semantic fit, A.10 reliance, and B.3 assurance are not described as legal, policy, or deontic permission.
* **SCR-F9-S08 (Receiving-object boundary).** A named proposed use is never treated as performed Work, assertion, publication, relation, or operation application.
* **SCR-F9-S09 (Card truthfulness).** An actual card concerns an already individuated occurrence; a candidate or negative card concerns the admitted relation kind and has no positive occurrence ref.
* **SCR-F9-S10 (Plain action).** A practitioner can tell what relation to test, what use is proposed, what would stop reliance, and which downstream claim still needs an applicable pattern.
* **SCR-F9-S11 (Non-optional identity and recurrence).** The declaration states `BridgeOccurrenceIdentityRule`, asymmetric ordering or symmetric canonicalization, and the non-recurrence of one fixed endpoint/profile tuple; a later basis changes the profile before another candidate is admitted.
* **SCR-F9-S12 (Description and publication boundary).** Every actual description/Card concerns an already individuated occurrence under C.2.1; every modal proposal has no positive occurrence ref; E.24.PUB publication, form, carrier, and registry identity establish neither.
* **SCR-F9-S13 (No adjacent fact by Bridge).** No Bridge creates a local system-role kind or assignment, Work, evidence authority, status transfer, U-kind admission, publication, model-use crossing, or another subject relation.

#### F.9:17.2 - Regression checks

* **RSCR-F9-E01 (Same Bridge, changed use).** Reversing direction, changing the use rule, or changing tolerance reidentifies the C.2.1 claim, not the Bridge.
* **RSCR-F9-E02 (Same claim, changed evidence).** Stale or stronger evidence changes the A.10 relation or disposition, or the B.3 branch, without reidentifying the fixed claim.
* **RSCR-F9-E03 (Required but missing assurance claim).** If a direct domain rule requires an assurance claim and none is current, return `RelianceDisposition=assurance-needed` or block the use. Do not manufacture a positive claim or a generic safety-case record.
* **RSCR-F9-E04 (Profile change).** A changed relation condition or endpoint reading identifies another profile and occurrence candidate.
* **RSCR-F9-E05 (Packaging change).** A changed card, registry entry, publication, form, or carrier leaves the Bridge and fixed bounded-use claim unchanged unless their own discriminators changed.
* **RSCR-F9-E06 (Positive proposal versus occurrence).** An affirmative claim with passing reliance proves no comparison Work, assertion, publication, direct relation, or operation application.
* **RSCR-F9-E07 (Polarity versus reliance).** Negative claim polarity and a non-passing reliance disposition remain different facts.
* **RSCR-F9-E08 (Reliance versus authorization).** A.10 `pass` or B.3 `supported-for-use` does not imply permission.
* **RSCR-F9-E09 (No inverse or composition).** Neither an asymmetric inverse nor a direct A-to-C Bridge follows without its own profile and obtaining test.

### F.9:18 - Didactic distillation

Use this five-part script:

1. Find the two exact local senses.
2. Say what semantic relation holds and test whether that Bridge obtains.
3. State the proposed use separately: action, direction, rule, tolerated loss, and polarity.
4. Check whether current evidence or assurance supports relying on that claim; recover authorization separately if needed.
5. If the use happened, identify the actual object and apply the relevant pattern to the claim about it. Make a card only when reuse is worth the maintenance.

The short memory aid is: **relation first, use second, reliance third, receiving occurrence last; packaging is optional.**

### F.9:19 - Archetypal Grounding

#### F.9:19.1 - Tell

A Bridge is an actual semantic relation, not a synonym claim or enactment edge. Its profile says what correspondence holds. A separate claim says whether that relation suits one proposed use. Evidence, authorization, packaging, and actual performance remain separate.

#### F.9:19.2 - Show: service lane

The observation sense can bear a semantic relation to the target sense without being the target status. The team then states and warrants one comparison use; status and acceptance remain separate claims.

#### F.9:19.3 - Show: access-control lane

A process team and an access-control team both use `operator`. An obtaining overlap Bridge plus an affirmative, warranted label-use claim can support one glossary row. It establishes no access, permission, authority, local system-role kind, assignment, performer, or Work. Recover whichever fact is actually claimed under its direct pattern; preserve the source term *access-control role* only when referring to the external scheme.

#### F.9:19.4 - Show: episteme lane

An actual card can package the relation claim, bounded-use claim, evidence path, and reliance disposition. It remains an episteme about the Bridge and creates neither the relation nor the receiving act.

### F.9:20 - Bias-Annotation

Lenses tested: governance, architecture, ontology and episteme, pragmatics, didactics. Scope: universal for cross-context correspondence and reuse.

* **Governance bias.** The pattern adds a separate use claim and reliance check. Mitigation: keep them in ordinary sentences when durable packaging has no payoff.
* **Architecture bias.** Typed relation profiles can look heavier than synonym prose. Mitigation: the five-part script begins with the practical action and introduces exact terms only where they stop a real overread.
* **Ontology and episteme bias.** F.9 resists global meaning claims and keeps claims separate from their subject. Mitigation: explicit Bridges still permit practical cross-context comparison.
* **Pragmatic bias.** Conservative separation can feel slower than reusing a mapping table. Mitigation: a fixed Bridge can support many independently stated uses without being reidentified.
* **Didactic bias.** The four-object split can become bureaucratic if written only in internal nouns. Mitigation: every use starts by saying what a person will do, what rule they will follow, and what result would make them stop.

### F.9:21 - Conformance Checklist

An F.9 use conforms iff:

1. both endpoints resolve to exact F.17 `SchemeSenseCell` values;
2. their semantic-context projections differ;
3. the Bridge has exactly two participants and one relation-semantic profile;
4. the profile contains no receiving-use or reliance content;
5. the profile applies, its Boolean predicate is true, and its dependencies are present before a positive occurrence is cited;
6. every proposed use is a separate C.2.1 claim naming `u`, `d`, `r`, `t`, polarity, and effective scheme;
7. observed loss stays in evidence while permitted loss stays in the bounded-use claim;
8. current ordinary reliance uses the exact A.10 branch for the same bounded use; when an actual named assurance claim is current, use its exact B.3 `AssuranceResult`;
9. no reliance or assurance statement is read as authorization;
10. any actual receiving object is recovered under its subject pattern;
11. description episteme, Card, registry record, E.24.PUB publication occurrence, form, and carrier remain distinct from Bridge occurrence and receiving-use occurrence;
12. inverse and composed relations are tested independently;
13. the reusable RelationSignature declares only two endpoint SlotSpecs, while every `CL`, Loss Note, scope/admitted-use, evidence, counterexample, policy, time, model-use, description, publication, or registry value remains a qualifier or neighbor;
14. the non-optional occurrence identity and non-recurrence rule is stated and applied before a Bridge occurrence is referenced; and
15. same-context designation remains outside F.9; claim-bearing source wording with *role* first uses E.10.ROLE, and each recovered system-role kind, assignment, access, permission, authority, Work, evidence-authority, status, U-kind, publication, structure-crossing, or other subject claim returns to its direct pattern.

### F.9:22 - Consequences

**Benefits.** F.9 permits comparison, translation, and bounded reuse without collapsing local senses. One stable Bridge can support several differently directed or differently tolerant use claims, and evidence can change without silently changing relation identity.

**Costs.** A reader must state two premises instead of one: the semantic relation and the bounded-use proposition. Ordinary evidence reliance may require A.10 work. An actual named assurance claim additionally requires a B.3 result. This cost is paid only when a real cross-context use is proposed; a Card remains optional.

**Failure mode avoided.** A Bridge, score, or card can no longer act as a quiet substitute for a local system-role kind or assignment, status transfer, evidence authority, authorization, publication, or performed-work attribution.

### F.9:23 - Rationale

Cross-context comparison is unavoidable, but the truth of a semantic relation and the suitability of one action are different claims. Putting direction, a use rule, and tolerated loss into `BridgePredicateProfile` would reidentify the relation whenever the proposed use changed. Putting them in a separate C.2.1 claim lets one Bridge remain fixed while several uses are affirmed, rejected, narrowed, or reopened independently.

The same separation keeps evidence honest. A.10 or B.3 can reopen reliance without erasing the relation. A card can travel without becoming the relation. A proposed use can be warranted without being authorized or performed. These boundaries preserve practical reuse and make each failure local and repairable.

### F.9:24 - SoTA-Echoing

| Claim need | SoTA practice | Primary source | Alignment with F.9 | Adoption status |
| --- | --- | --- | --- | --- |
| Shared labels across contexts are not enough. | Terminology and ontology practice distinguishes objects, concepts, definitions, designations, and typed relations. | ISO 704:2022; ISO 1087:2019; ISO/IEC 21838-2:2021 (BFO). | F.9 resolves exact local senses and tests a direct relation instead of using string equality. | Adopt typed term, concept, and relation discipline. |
| Viewpoint boundaries remain explicit during reuse. | Architecture-description practice distinguishes entity of interest, description, viewpoint, view, model kind, concern, and correspondence. | ISO/IEC/IEEE 42010:2022. | F.9 keeps relation, use claim, card, view, and publication separate. | Adopt boundary-explicit correspondence. |
| Metadata and validation do not create use authority. | Web-data practice separates metadata, provenance, constraints, validation, and exchange from the governed data and act. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024). | Evidence and packaging can support a bounded-use claim but do not make a Bridge obtain or grant permission. | Adapt provenance and validation discipline. |
| Interoperability is not semantic identity. | Terminology and controlled-vocabulary practice separates concepts from designations and distinguishes mapping relations instead of treating every mapping as identity. | ISO 704:2022; ISO 1087:2019; W3C SKOS Reference (stable mapping-relation baseline, not current-best SoTA). | F.9 tests exact relation semantics and then judges each proposed use separately. | Adapt only the term, concept, and typed-mapping distinctions; the use-specific judgement is FPF-native. Reject shared spelling, a generic mapping, or interchange success as proof of identity or suitability. |

### F.9:25 - Bridge Card publication discipline

#### F.9:25.1 - Minimal truthful card

A reusable description/Card states its mode and exact C.2.1 identity. An actual one names its already individuated Bridge; a candidate or negative one names the admitted direct Bridge relation kind and modally designates proposed endpoints, profile, and polarity in its ClaimGraph. When it packages a proposed use, it states `u`, `d`, `r`, `t`, polarity, observed loss, evidence, currentness, nearest non-use, and the exact A.10 disposition or, when an actual named assurance claim is current, its B.3 `AssuranceResult`. Missing relation facts are never repaired by filling more fields. If availability matters, E.24.PUB publishes the selected episteme edition for one declared audience and bounded use through its independently governed publication occurrence, form, and carrier.

#### F.9:25.2 - One occurrence, several claims and descriptions

Several bounded-use claims, cards, reviews, or publications may concern the same actual Bridge. Their C.2.1 identities differ when their ClaimGraph, EntityOfConcern, or effective scheme differs; the Bridge identity does not. Prefer one primary current card only when it reduces navigation cost.

#### F.9:25.3 - Revision without silent ontology change

If evidence, observed loss, reliance, assurance, wording, or publication changes while endpoints and profile remain fixed, revise the corresponding claim, evidence relation, disposition, card, or publication. Test another Bridge only when an endpoint or relation-semantic profile component changes.

### F.9:26 - Bundle and endpoint interaction

Viewpoint bundles, quality bundles, dashboards, reports, and endpoint bundles may cite Bridges and bounded-use claims, but they do not absorb their semantics. Each bundle keeps its own ontology and direct use rule.

When a quality-family claim crosses contexts, observed loss may bear on its bounded-use claim and on B.3 assurance, but neither fact retypes the quality family. An F.9.1 stance note may help readers interpret the claim; it remains a separate episteme and cannot widen the relation, proposed use, reliance, authorization, or occurrence.

### F.9:27 - C.29 mathematical-lens use relation

When a mathematical-lens use relies on cross-local meaning, first recover an actual F.9 Bridge. Then state the exact bounded-use claim for the lens direction, correspondence rule, and tolerated loss, and recover current reliance. Use C.29 for the mathematical object, `LensMappingMode`, preserved and lost structure, lens-use judgement, and actual lens use. A Bridge can make a lens interpretable without making any lens use occur.

### F.9:28 - Review matrix

A reader can test bridge integrity with eight questions:

1. Do both endpoint refs resolve exact F.17 `SchemeSenseCell` values from different semantic contexts?
2. Does the profile say only which semantic relation holds, with its endpoint readings, condition, applicability, truth rule, and stop dependencies?
3. Is the Bridge claimed only after that fixed predicate is true?
4. Does each proposed use separately name the action, direction, correspondence rule, tolerated loss, and polarity?
5. Does the same use have the correct current A.10 evidence-provenance relation and local disposition or, when an actual named assurance claim is current, its B.3 `AssuranceResult`?
6. Are semantic suitability, reliance, assurance, and authorization kept distinct?
7. If someone says the use happened, is the actual Work, assertion, publication, relation, operation application, or other object recovered under its own pattern?
8. Does any card remain optional packaging rather than the source of relation truth, permission, or occurrence?

Repair *same*, *equivalent*, *align*, and *map* prose in that order: recover the exact senses; test the Bridge; state the bounded-use claim; check reliance; recover authorization or the actual receiving object only when those questions are live. Do not start from a polished card or a score.

### F.9:End

