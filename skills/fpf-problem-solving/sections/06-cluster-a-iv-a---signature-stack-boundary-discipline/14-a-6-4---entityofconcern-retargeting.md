## A.6.4 - EntityOfConcern retargeting
> **Status:** Stable
> **Type:** Definitional pattern

**One-line summary.** Use EntityOfConcern retargeting when one episteme concerns one entity and another concerns a different entity, yet a stated invariant remains useful across that change for one named purpose.

**Retargeting in plain terms.** The two epistemes are not merely different descriptions of the same thing. They concern different things, and the receiving use keeps only what a stated invariant supports.

**Use this when.** Use this pattern only after C.2.1 identifies the two epistemes and shows that their exact EntitiesOfConcern differ. A changed model kind, ontology frame, predicate set, coordinate system, or notation is a cue to repeat that identity test, not proof of retargeting.

**What goes wrong if missed.** A changed EntityOfConcern is treated as “the same thing in another form”, so claims, evidence, gate results, work authority, or currentness are carried into a use they do not support. The opposite error is to demand a semantic Bridge or reversible mapping when the case needs neither.

**First useful move.** Name both epistemes and both EntitiesOfConcern. Then say what remains supported, what is lost, the receiving action for which that loss is acceptable, and what supports that judgement.

**What this buys.** The reader can decide one receiving use without pretending that every source claim survives, that the arrow performed Work, or that a mathematical representation decided what the epistemes concern.

**Not this pattern when.** If the EntityOfConcern is preserved, use the pattern for the change that actually occurred: A.6.3.CR for wording, A.6.3.RT for representation scheme or reasoning medium, A.6.3.CSC for controlled coarsening, or E.17.EFP for explanation mode. A normal time-to-frequency description of the same signal is first a C.29 and A.6.3.RT case. Use F.9 for a separately claimed Bridge between two local senses; use A.6.1, A.15, A.10, B.3, A.21, C.27, A.3.3, or E.24.PUB only when an operation application, Work, evidence, assurance, a gate, temporal adequacy, dynamics, control, or publication is actually claimed.

### A.6.4:1 - Problem frame

Several familiar moves can hide a real change of EntityOfConcern, but none proves that change merely by its name or notation:

* **Physical module and realized function.** An episteme about cabinet `Cab-7` and one about routing function `Route-A` concern different exact entities when C.2.1 identifies the cabinet and the function independently. The obtaining realization relation can then help support a bounded retargeting claim.
* **Signal and spectrum.** The ordinary Fourier case often concerns one signal in two representations. That is a C.29 mathematical-lens use followed by A.6.3.RT when the EntityOfConcern is preserved. A.6.4 opens only if the receiving episteme concerns a separately identified spectrum object and the use explains why that object, rather than the original signal under another representation, is current.
* **Observations and fitted model.** A dataset and a learned model can be different exact entities. The fit and held-out test may support a named prediction use, while individual observations and unmodelled distinctions remain visible losses. Model fitting itself is separate Work.

For a case used positively, the local arrow r relates two identified epistemes with different EntitiesOfConcern, q affirmatively states the bounded-use proposition, and the current case facts satisfy it. If a system produced or changed an episteme, identify that application and Work separately.

A domain relation, mathematical transform, or F.9 Bridge may support one case, but none is a universal admission field and none substitutes for the independent EntityOfConcern test.

### A.6.4:2 - Problem

Without this discipline:

1. **Notation decides ontology.** A changed coordinate system, mathematical domain, model kind, or predicate vocabulary is treated as proof that the EntityOfConcern changed.
2. **Retargeting is confused with viewing.** A real move from one independently identified entity to another is called another view, so its loss and receiving-use boundary disappear.
3. **The invariant and loss remain rhetoric.** Phrases such as “energy is preserved” or “the model summarizes the data” do not say which claim survives, which distinctions disappear, or which use remains sound.
4. **A mapping apparatus replaces the actual case.** A generic kind bridge, score, diagram, or reversible optic is demanded even when the endpoint entities, invariant, loss, use, and support already answer the question.
5. **Arrow, claim, and execution collapse.** A mathematical arrow is treated as if it granted a use, performed an operation, or produced an episteme.
6. **Structural reinterpretation duplicates the core rule.** E.18 or a discipline pack invents another retargeting ontology instead of placing the same arrow and separate use claim in its own transformation-flow structure.
7. **Neighboring changes disappear into one label.** Grounding, representation, scope, operating conditions, viewpoint selection, publication, operation application, and performed Work are folded into retargeting instead of being identified only when they occur.

### A.6.4:3 - Forces

* **Different subject versus unsupported new claim.** Changing the EntityOfConcern is permitted only when the receiving claims are conservative with respect to the declared invariant.
* **Useful loss versus hidden loss.** Retargeting may discard information, but the loss boundary and the use that tolerates it must be visible.
* **Direct case versus universal apparatus.** A domain relation, mathematical map, semantic Bridge, or diagram is relevant only when the current case actually relies on it. None identifies the A.6.4 arrow or makes its separate use assertion true; a witness supports that assertion rather than identifying the arrow.
* **Composition versus accidental equivalence.** Compatible retargetings may compose. Equality of two evaluation routes, reversibility, idempotency, or semantic correspondence requires its own stated conditions; it does not follow from the word *retargeting*.
* **Modularity.** The retargeting arrow relates two epistemes, q states one bounded-use proposition, and a separate current-case judgement says whether the facts satisfy it, fail it, or leave it undecidable. Grounding, publication, Work, evidence, assurance, gate, flow structure, and cross-local-sense correspondence remain separate.

### A.6.4:4 - Solution — separate the arrow, use claim, current-case judgement, and any application

#### A.6.4:4.1 - Informal definition

> **Definition.** An **EntityOfConcern-retargeting morphism** is a local `EpMorphism r : X -> Y` whose exact endpoint epistemes concern different exact entities. A separate bounded-use assertion q affirms or denies that one declared invariant makes the stated loss acceptable for one named receiving use under named conditions.

`EntityOfConcernRetargetingMorphism` is a local mathematical subtype under C.29, not a durable kind. This pattern defines that subtype and the practical discipline for claims about its use.

Keep four things distinct:

1. **The arrow `r`.** Within the selected formal substrate, its exact domain X, codomain Y, arrow rule or designator, and declared formal equivalence identify it. The two endpoint epistemes and their different EntitiesOfConcern are recoverable. A changed use claim does not create another arrow.
2. **The bounded-use assertion `q`.** This is a C.2.1 episteme about exact arrow r. Its ClaimGraph states the invariant, visible loss, named receiving use, conditions, and affirmative or negative polarity. Its complete claim content, exact EntityOfConcern, and effective ReferenceScheme identify q. A citation inside q can point to case facts; it does not decide whether those facts satisfy the proposition.
3. **The current-case judgement.** Compare the exact current facts with q's conditions and proposition, and report `satisfies`, `fails`, or `cannot decide`. That result is not q's polarity and does not reidentify q or r. Use A.20 only when the case raises an internal-constraint check, A.10 only for a current evidence-use claim, and B.3 only for a current assurance claim or its material-reliance threshold. Otherwise the named rule and direct case facts are enough.
4. **Any application occurrence.** If a system actually computes, authors, or otherwise produces or changes an episteme by using the declared operation, identify that A.6.1 application, its argument and result bindings, the performing system, and any Work separately. The mathematical statement `r : X -> Y` alone names no occurrence.

The smallest useful practitioner account still asks six cheap questions:

| Question | What it recovers |
| --- | --- |
| Which source and receiving epistemes are related? | exact endpoints X and Y of r |
| Which different entities do they concern? | the independently identified EntityOfConcern pair |
| What exactly does q affirm or deny? | invariant, visible loss, named receiving use, conditions, and polarity |
| Which current facts bear on that proposition? | the direct case basis |
| What do those facts show? | `satisfies`, `fails`, or `cannot decide` |
| If the case cannot be decided, what is missing? | the exact missing fact and reopen condition |

These answers may be one short paragraph; they require no new record form or assurance package. Add preserved or withdrawn commitment lists, predicate changes, grounding, scheme, scope, operating conditions, viewpoint selections, evidence, currentness, or a durable result only when they change the proposition, judgement, or receiving action. Add an F.9 Bridge only when the same case separately claims a semantic relation between two exact F.17 local senses.

When the judgement is `fails`, do not use an affirmative q as support for that case. When it is `cannot decide`, keep the source material, name the exact missing fact and what would reopen the question, and stop. Failure of an affirmative q does not by itself establish a negative q; a negative assertion needs its own claim content and case basis.

#### A.6.4:4.2 - Formal declaration and object boundaries

Repeated formal use may be declared in an A.6.0 `U.Signature(profile=FormalSubstrate)` episteme. That declaration is about the local subtype `EntityOfConcernRetargetingMorphism`; it is not the subtype, one arrow, a use claim, or an application occurrence.

```text
SubjectKind     = local formal subtype EntityOfConcernRetargetingMorphism of EpMorphism
RangedValueKind = admitted ordered-pair range over exact U.Episteme values satisfying the declared endpoint-kind constraints
ResultKind      = omitted; r is the declared subject, not an operation result
Applicability   = selected formal substrate and endpoint and arrow-family conditions
```

`X` and `Y` are exact C.2.1 epistemes. `r : X -> Y` is one local mathematical arrow under C.29. Its identity uses the exact endpoints, arrow rule or designator, and the selected substrate's equivalence criterion; the endpoints alone do not identify it. The declaration states which parts of X and Y's claim content, exact EntityOfConcern, and effective ReferenceScheme remain the same or differ. If r's rule reads a representation or another separately obtaining relation, it names the exact occurrence and compares endpoint facts without changing that occurrence.

A.6.4 reuses the one A.6.2 formal model: category `Ep`, endpoint-only thin category `EoCBase`, `dom`, `cod`, identities, `compose`, and the declared mapping `α`. For retargeting arrow r, `α(r)=u_{α(X),α(Y)}` is the unique formal endpoint arrow between the independently different EntitiesOfConcern. It records only that endpoint difference and deliberately forgets r's arrow rule; it is not an independently declared domain or world-side relation. The local characteristic `entityOfConcernChangeMode(r)=retarget` records the same endpoint difference. No function evaluation or second retargeting calculus is implied.

The bounded-use assertion q, current-case judgement, and any application occurrence remain separate. Grounding, representation, an F.9 Bridge, evidence, publication, Work, gate, currentness, and assurance also remain separate objects or claims under their direct patterns. Add A.6.5 SlotSpecs only inside an exact reusable direct-relation declaration; they are not fields of r, X, Y, or q.

#### A.6.4:4.3 - Laws (ER-0...ER-6)

These laws refine A.6.2 for the local retargeting subtype. They do not assert durable U-kind membership.

**ER-0 - Arrow class and endpoint basis.**

An arrow `r : X -> Y` is in the local retargeting subtype only when X and Y are exact C.2.1 epistemes, `entityOfConcernChangeMode(r)=retarget`, and their exact EntitiesOfConcern differ. A shared label, kind name, diagram, implementation, use claim, or F.9 card identifies neither r nor its endpoints by itself.

**ER-1 - Arrow identity and neighboring facts.**

1. The selected formal substrate supplies r's arrow rule or designator and equivalence criterion; same endpoints alone do not identify an arrow.
2. The declaration states which parts of X and Y's claim content, exact EntityOfConcern, and effective ReferenceScheme remain the same or differ. It names any separately obtaining representation or other relation that r's rule reads and the endpoint facts compared; r does not change that occurrence.
3. Grounding, scope, operating condition, representation, and any viewpoint selected for a describing use remain separate values or relations.
4. A different scheme, scope, context, or plane does not by itself create an F.9 Bridge. Cite F.9 only for an actually claimed direct relation between two exact F.17 local senses.

**ER-2 - Separate use proposition and current-case judgement.**

For each named receiving use, one separate C.2.1 assertion q affirmatively or negatively states whether the source claims conservatively support the declared invariant in the receiving episteme and whether the visible loss is acceptable under the named conditions. The same r may have different q assertions for different uses without changing arrow identity.

A separate current-case judgement applies q to the exact current facts and returns `satisfies`, `fails`, or `cannot decide`. A direct fact, proof, test, or obtaining relation can supply the ordinary case basis. Open A.20 only for an internal-constraint claim, A.10 only for evidence use, and B.3 only for assurance or its material-reliance threshold. None identifies r, changes q's polarity, or turns `cannot decide` into support.

**ER-3 - Composition and separately claimed final use.**

Two retargeting arrows with an exact matching middle episteme compose in the parent Ep category; A.6.2 category closure supplies the composite and requires it to satisfy the parent laws. The composite remains in the A.6.4 retargeting subtype only when its final endpoint EntitiesOfConcern differ and its other subtype laws hold. A round trip whose final endpoints concern the same exact entity is a preserve-mode EFEM arrow in the parent class, not an A.6.4 retargeting arrow.

A claim that an admitted composite is suitable for a final use is another q: it states the final source and receiving entities, preserved invariant, accumulated loss, receiving use, conditions, and polarity. A separate judgement applies that proposition to the final current case.

No universal SquareLaw follows. A consumer that claims two evaluation routes equivalent, or relies on a correspondence between epistemes, identifies the routes or correspondence, comparison rule, tolerated difference, and witness under the direct governor of that claim.

**ER-4 - Determinism and repeat boundary.**

Determinism, reversibility, and idempotence may be properties of the declared arrow only when the selected formal substrate states the exact domain, equality or equivalence, and evidence used to test them. A repeat property of an operation or application is a different claim: it follows from the rule and inputs of that operation or application. The mathematical statement `r : X -> Y` says nothing about execution or repetition. Ambient time, randomness, solver state, and external services belong to an explicitly declared operation or mechanism.

**ER-5 - Applicability and optional semantic-Bridge branch.**

The formal declaration states admissible endpoint families and material mathematical conditions. Each q separately states the invariant, loss boundary, receiving use, case conditions, and affirmative or negative polarity; the current-case judgement states whether the facts satisfy it. F.9 is triggered only for a separately claimed relation between two exact local senses. Optional `CL` summarizes evidence about that Bridge; it is neither a retargeting threshold nor a participant in r or q.

Legacy `KindBridge` plus mandatory `CL`, and generic SquareLaw-retargeting interfaces, are not reactivated here. A consumer that still needs one identifies a current direct governor or stops at `missing-governor`.

**ER-6 - Separate application, Work, and resulting episteme.**

An arrow that preserves the EntityOfConcern belongs to the A.6.3 preserving branch rather than this subtype. When a system measures, computes, fits, translates, authors, or otherwise changes an episteme, identify the A.6.1 application and bindings when current, the performing system and Work, and the resulting C.2.1 episteme separately. The arrow can relate those epistemes without performing that activity or creating a universal production relation.

#### A.6.4:4.4 - Boundary with representation, explanation, transformation-flow structure, and neighboring claims

A.6.4 is triggered only by an independently established change of exact EntityOfConcern. A changed kind, ontology frame, predicate set, mathematical domain, or notation is a recognition cue that reopens the C.2.1 identity test; none decides the branch by itself.

Boundary rules:
- if the EntityOfConcern is preserved and the main change is representation scheme or reasoning medium, use `A.6.3.RT`;
- if the EntityOfConcern is preserved and the main change is explanation mode, explanatory stance, or explanation-facing publication, use `E.17.EFP`;
- if the same case also asserts a semantic relation between two exact local senses from different semantic contexts, test `F.9` separately and cite a Bridge only when its predicate obtains; use `F.9.1` only for an optional stance note about that already constituted use claim. A domain correspondence, mathematical rule, or direct case fact that supports q does not by itself open F.9;
- if a legacy consumer asks for `KindBridge`, `CL`, or a universal SquareLaw-retargeting witness without a current direct governor, stop at `missing-governor` rather than making that apparatus constitutive in A.6.4;
- if the receiving item is useful only under narrower declared use with visible loss and source-bearing reopen, use `A.6.3.CSC`;
- if decoded or latent output is interpretable but not tied to source claim, access relation, recoverability evidence, admissible-use value, and remaining reader action, keep it report-only, exploratory, source-bearing reopen, or in the named neighboring pattern;
- if a `StructuralReinterpretation`, `PathSliceId`, `CrossingRef`, or `DecisionLogRef` is present, use `E.18`, `A.20`, or `A.21` for graph, path, constraint, and gate relations. Those references do not prove semantic continuity or retargeting admissibility by themselves;
- if changed problem formulation changes abductive prompt, candidate generation, rival-set formation, selected prime hypothesis, plausibility filtering, or abductive reopen, use `B.5.2`;
- if the receiving item is used as work, evidence, assurance, gate passage, temporal claim, dynamics law, or control relation, use `A.15`, `A.10`, `B.3`, `A.21`, `C.27`, `A.3.3`, or another pattern that defines or tests the current claim.

A.6.4 defines arrow r, bounded-use assertion q, and the separate current-case judgement that E.18 may place at a `StructuralReinterpretation` locus. That placement identifies none of them and does not make the judgement `satisfies`.

### A.6.4:5 - Archetypal Grounding (Tell-Show-Show)

**Tell.** Retargeting means “different EntityOfConcern, one supported invariant, visible loss, one named use”.

**Show 1 — Physical module to function.** X concerns cabinet `Cab-7`; Y concerns routing function `Route-A`. C.2.1 identifies the cabinet and function independently. Affirmative q states that the routing-behaviour invariant makes the visible loss acceptable for fault-isolation planning. The obtaining `Realises(Cab-7, Route-A)` relation and behaviour test are current case facts; here the judgement is `satisfies`. Y drops cabinet layout and manufacturer details. E.18 placement identifies neither r nor q and supplies no judgement.

**Show 2 — Fourier near-miss and positive branch.** In the ordinary case, X and Y both concern sampled signal run `Signal-17`; X uses a time-domain representation and Y a frequency-domain representation. Route first through C.29 and then A.6.3.RT. Parseval's relation may support energy preservation, but it does not turn the spectrum notation into another EntityOfConcern.

A positive A.6.4 branch opens only if C.2.1 separately identifies, for example, exact signal run `Signal-17` and exact spectral-distribution object `Spectrum-17` as the two EntitiesOfConcern. The receiving use must actually concern `Spectrum-17`—for example, comparing its peak distribution with another spectrum—rather than merely read another representation of `Signal-17`. Then r relates the two epistemes; affirmative q states the spectral-comparison proposition and may cite the Fourier relation and Parseval test. The current-case judgement is `satisfies` only when the named facts support that use while lost time localization remains visible.

**Show 3 — Dataset to model.** X concerns dataset D; Y concerns fitted model M, independently identified under the applicable model pattern. The fit result and held-out test support q's predictive-invariant claim. Individual observations and unmodelled distinctions are visible losses. The claim supports the named prediction use, not a claim that M is D or that every dataset claim transfers to M. The fitting application and Work remain separate from r and q.

### A.6.4:6 - Bias-Annotation

A.6.4 deliberately biases the reader away from "same thing in another form" when the EntityOfConcern changes. The safe default is to recover the source and receiving pair, invariant, visible loss, bounded use, and witness. Publication rendering, graph notation, a familiar mapping, an F.9 Bridge, or a reversible optic may matter in a selected branch, but none proves retargeting admissibility or carries work authority by itself.

### A.6.4:7 - Conformance Checklist (normative)

**CC-A.6.4-1 - Exact endpoints and changed EntityOfConcern.** C.2.1 identifies X and Y and their exact EntitiesOfConcern; the two entities differ. A changed kind, frame, predicate set, domain, or notation alone does not pass this check.

**CC-A.6.4-2 - Arrow identity.** The selected formal substrate supplies r's exact endpoints, arrow rule or designator, and equivalence criterion. Same endpoints, a diagram, or a use claim alone does not identify r.

**CC-A.6.4-3 - Separate use proposition and case judgement.** One C.2.1 assertion q names r, one receiving use, the invariant, visible loss, conditions, and affirmative or negative polarity. A separate current-case judgement reports `satisfies`, `fails`, or `cannot decide` from exact current facts. The same r may have another q and judgement for another use.

**CC-A.6.4-4 - Conservative receiving claim.** A `satisfies` judgement requires enough current case basis for q's invariant and stated use, and the receiving episteme adds no unsupported commitment about that invariant. Contrary facts yield `fails`; a missing deciding fact yields `cannot decide` plus that fact and the reopen condition. Neither result changes q's polarity.

**CC-A.6.4-5 - Triggered additions only.** For a Description or specification-use episteme, name every material change to claim content, effective scheme, grounding, scope, operating condition, or selected viewpoint under A.7 and E.10.D2. Add those values, evidence, currentness, a route-equivalence test, or a reopen condition only when they change q or the reader's action.

**CC-A.6.4-6 - Separate semantic correspondence.** Test an F.9 Bridge only when the case also claims a relation between two exact local senses. The Bridge, its bounded-use claim, optional `CL`, evidence, and reliance remain separate from r and q.

**CC-A.6.4-7 - Separate application and Work.** Measurement, computation, actuation, model fitting, authoring, and other effects use their exact operation application and Work patterns. The arrow statement `r : X -> Y` neither identifies that occurrence nor proves a production relation.

**CC-A.6.4-8 - Fourier boundary.** A same-signal time/frequency change routes to C.29 and A.6.3.RT. A.6.4 is used only after the receiving spectrum or other mathematical object is independently identified as a different EntityOfConcern.

**CC-A.6.4-9 - StructuralReinterpretation boundary.** E.18 governs structure position, path, crossing, and gate relations. A.20 tests q's exact proposition only when an internal constraint is current, and A.21 governs any gate decision. None identifies r or supplies a `satisfies` judgement merely by reference or placement.

**CC-A.6.4-10 - Honest stop and light ordinary use.** A missing deciding fact yields `cannot decide` and names the fact and reopen condition; contrary facts yield `fails`. Otherwise one short paragraph answering the six practical questions is enough. No separate evidence, assurance, publication, currentness, or reusable declaration is required unless its own use condition is current.

### A.6.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Correct action |
|---|---|---|
| Retargeting as viewing | A changed EntityOfConcern is treated as the same object under another viewpoint. | Use A.6.3 only when `EntityOfConcernRef` is preserved; use A.6.4 when it changes. |
| Retargeting as publication rendering | A diagram, export, or face is treated as the arrow or as support for its use. | Keep publication forms in E.17 and E.24.PUB; state r and the separate use claim q only when each is current. |
| Universal Bridge as admission | A `KindBridge`, F.9 Bridge, `CL`, mapping, or optic is required or used to inherit every downstream claim. | Use the A.6.4 minimum basis; add F.9 only for a separate local-sense relation and state every neighboring claim under its own rule. |
| Mathematical notation decides retargeting | A Fourier, graph, path, or category representation is treated as proof that the EntityOfConcern changed. | Use C.29 for the mathematical lens and repeat the C.2.1 identity test. Use A.6.3.RT when the entity is preserved; use A.6.4 only for independently different entities. |

### A.6.4:9 - Consequences

* **Viewing and retargeting separate cleanly.** A viewing arrow preserves the EntityOfConcern. A retargeting arrow relates epistemes with independently different EntitiesOfConcern; q states one bounded-use proposition, and the separate current-case judgement says whether the facts satisfy it.
* **StructuralReinterpretation receives one core rule.** E.18 can place r and q without duplicating their identities or treating graph position as support for q.
* **Loss becomes usable information.** A lossy mapping can be admitted for a bounded purpose without pretending to be reversible or semantically identical.
* **Optional apparatus stays optional.** F.9 enters only for cross-local-sense correspondence; route-equivalence, evidence, assurance, gate, publication, and Work branches enter only when their own claims are current.
* **Description boundaries remain visible.** Claim content, scheme, grounding, scope, operating condition, and viewpoint changes do not disappear into one retargeting bundle.

### A.6.4:10 - Rationale

A.6.4 exists because some mathematical arrows relate epistemes that concern different entities. The arrow itself neither performs Work nor grants a use. A separate q states the invariant, visible loss, receiving use, conditions, and affirmative or negative proposition; the current-case judgement tests that proposition against exact facts. This lets the reader decide the use without demanding a universal Bridge, reversible mapping, or assurance package.

### A.6.4:11 - SoTA-Echoing

**Practice question.** What current transformation practice helps a reader keep a transformation definition, its execution, and a correctness claim separate—and what, if anything, can that practice say about whether the source and receiving epistemes concern different entities?

| Source or practice | Contribution used here | Limit and disposition | A.6.4 locus changed |
| --- | --- | --- | --- |
| [Zhao et al., *KBX: Verified Model Synchronization via Formal Bidirectional Transformation* (2024)](https://arxiv.org/abs/2404.18771) | KBX separates formal bidirectional-transformation definitions, generation of a synchronizer, and consistency verification. | **Adapt.** This supports the declaration, application, and use-claim split. KBX synchronizes models; it does not decide FPF EntityOfConcern identity or make one bounded use sound. | Sections 4.1-4.3 and checks 2-4 and 7. |
| [He and Zan, *BIT: A template-based approach to incremental and bidirectional model-to-text transformation* (2024)](https://doi.org/10.1016/j.jss.2024.112148) | BIT distinguishes a usable surface language, a formally defined core, executable printer/parser behavior, round-trip properties, and empirical cases. | **Adapt.** This supports keeping readable first use, formal declaration, execution, and well-behavedness evidence distinct. BIT's model/text synchronization does not decide whether two FPF epistemes concern different entities. | Practitioner entry, sections 4.1-4.3, and check 10. |
| Current FPF C.2.1, C.29, and A.6.3.RT | C.2.1 identifies each episteme and EntityOfConcern; C.29 bounds the mathematical lens; A.6.3.RT handles representation change with preserved EntityOfConcern. | **Adopt.** These are the direct identity and routing rules. | `Use this when`, section 4.4, Show 2, and check 8. |
| Fibrations, cospans, Fourier transforms, and data/model mappings | These provide mathematical lineage and stress cases for endpoints, composition, invariants, and loss. | **Retain as lineage; reject as ontology shortcut.** None proves that the EntityOfConcern changed or that a receiving use is sound. | Problem frame, ER-0 to ER-5, and Show 2. |

The A.6.4 split among r, q, and any application occurrence is a bounded FPF synthesis from these distinctions, not an externally established retargeting ontology. Reopen it if a current direct practice supplies a better identity rule, or if a concrete case cannot keep arrow identity stable while suitability changes across uses.

### A.6.4:12 - Mini-checklist (for use)

When you think you need retargeting, ask:

1. **Does the EntityOfConcern change?** If no, use A.6.3 or another preserving pattern.
2. **Which two epistemes and EntitiesOfConcern are involved?** Name them before naming a mapping technology.
3. **What invariant remains supported?** State the exact claim and its case assumptions.
4. **What is lost, and which receiving use tolerates that loss?** A broad "same meaning" answer is insufficient.
5. **What witnesses the invariant and loss judgement?** If the witness is missing or contradicted, stop or reopen.
6. **Is a relation between two local senses also claimed?** Only then test F.9 separately; no Bridge follows merely from retargeting.
7. **Was computation or other Work performed?** Identify the operation application and Work separately from r and q.

### A.6.4:13 - Relations

* **Placement.** After A.6.3 epistemic viewing and before A.6.5 relation-declaration SlotSpec discipline.
* **Builds on.** A.6.0 for a reusable FormalSubstrate declaration; A.6.2 for the local arrow discipline; A.6.3 for the preserved-EntityOfConcern neighboring branch; C.2.1 for episteme, EntityOfConcern, and use-assertion identity; C.29 for mathematical-lens use; A.6.3.RT for preserved-EntityOfConcern representation transitions; A.6.5 for SlotSpecs inside a reusable direct-relation declaration; A.7 and E.10.D2 for Description and specification-use boundaries; C.2 and C.3 or the relevant domain pattern for the invariant; and F.9 only for a separately claimed relation between exact local senses.
* **Consumed by.** E.18 may place r and q at a `StructuralReinterpretation` locus; A.20 may test the exact proposition carried by q; E.17 may publish an episteme that describes the case; KD-CAL and LOG-CAL may reason over a stated invariant. None redefines r or q.
* **Neighbor boundaries.** A.6.1 and A.15 govern an actual application and Work; A.10 and B.3 govern evidence and reliance when claimed; E.24.PUB governs publication. Legacy `KindBridge` plus mandatory `CL`, and generic SquareLaw-retargeting interfaces, are not constitutive here.

### A.6.4:End

