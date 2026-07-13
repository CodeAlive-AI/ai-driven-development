## E.18.1 - P2W Problem-to-Work Carry-Through

> **Tech-name:** `ProblemToWorkCarryThrough`
> **Plain-name:** problem-to-work carry-through relation
> **Type:** Architectural pattern (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part E -> E.18 child pattern
> **Builds on:** `E.18` Transformation Flow Structure, `C.22.2` ProblemCard@Context, `A.6.0` `U.Signature`, `A.6.1` `U.Mechanism`, the A.15 work family, `C.29`, `C.16`, `F.9`, `A.20`, `A.21`, and Part G comparison, selection, and refresh patterns.
> **Purpose:** preserve selected distinctions from an accepted problem-side record as method selection, planning, performed work, result interpretation, and return become current.

### E.18.1:1 - Problem frame

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is not yet settled. The practitioner has an unsettled carry-through question: which problem-side distinction can be carried into the next FPF relation or record named by value?

The primary EntityOfConcern is the P2W carry-through relation: the relation between accepted problem-side material and the wider work transformation that continues to use its selected distinctions. P2W carries those distinctions through method selection, planning when current, dated work, result interpretation, and return when an earlier assumption changes.

Keep three objects separate. The **P2W relation** is the EntityOfConcern of this pattern. The **subject EntityOfConcern** is the system, episteme, method, role, work occurrence, relation, or other project entity addressed by the accepted problem and by each direct pattern. The **ProblemCard, compact note, diagram, plan, trace, and publication** are epistemes or publication-side values that describe, constrain, or make those relations inspectable. Later method enactment or dated work can change or preserve the subject EntityOfConcern; improving a P2W note or completing its fields does not establish that subject change, work occurrence, evidence, acceptance, or result.

E.11.PUA governs a smaller use and may begin without `ProblemCard@Context`: apply one selected pattern to one current practical question, obtain the first directly typed result, and state its receiving use. E.18.1 begins only when the wider work transformation depends on preserving accepted problem-side material. PUA may support one pattern inspection inside a P2W flow, but it does not replace the accepted-problem carry-through.


#### E.18.1:1.1 - Use this when

- an accepted `ProblemCard@Context` names a working problem and the team needs a disciplined next FPF use toward method, planning, performed work, or result interpretation;
- an invariant, `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, mechanism-position, method-position, `A.15.2 U.WorkPlan` or plan-item, performed-work, result-record, or source-currentness cue is present, but the FPF kind or relation to use next is still unsettled;
- a transformation-flow structure, mathematical path relation in a graph-shaped description, flow diagram, principle scheme, scenario, functional description, or source publication helps the team think, while the next FPF use still lacks an FPF kind or relation named by value;
- a result artifact, telemetry line, acceptance record, quality-evaluation record, done-state update, feedback pin, or integration claim needs to be unpacked before it can guide the next FPF use.

#### E.18.1:1.2 - What goes wrong if missed

The team jumps from a convincing problem-side formulation into downstream language without naming the FPF relation being used. The work then looks responsive to the accepted problem, but the next record is unclear, the result phrase becomes too broad, and measurement or source-currentness changes have no honest return relation.

#### E.18.1:1.3 - What this buys

The practitioner gets one next FPF use whose governing relation is named: preserve the accepted claim, recover and apply the direct pattern, obtain its governed value, stop with a reduced-use cue, branch across independently governed relations, or return to the earlier continuation whose relied-on relation changed. Under named reliance, a compact carry-through note keeps that path replayable. The payoff is practical: accepted problem-side distinctions remain action-guiding without becoming hidden work authorization.

#### E.18.1:1.4 - Not this pattern when

- there is no accepted problem-side record; use `C.22.2` or the problem-side pattern named by value first;
- the FPF kind under repair, relation, and record to write are already settled; use that pattern directly and do not add a P2W layer;
- the requested output is a local project procedure, schedule, or work-management method; use the relevant work, planning, method, gate, or operational-management pattern;
- the requested record or claim is an evidence case, assurance case, gate record, decision record, architecture description, publication-use claim, or wording-use repair; use the recovered relation and its governing pattern directly.

### E.18.1:2 - Problem

An accepted problem-side distinction becomes useful when it is ready to guide downstream work or work-planning use. The accepted problem card may expose an invariant, mathematical lens, functional role, mechanism-position candidate, method candidate family, planning constraint, result cue, or changed measurement assumption. Without P2W, that useful distinction is either overcompressed into "we have a solution" or scattered across several related FPF patterns before the working distinction is preserved.

P2W solves a carry-through problem. A practitioner starts from an accepted problem-side claim, states the receiving use, recovers and applies the direct pattern for the next relation, and checks that the resulting governed value still carries that claim. Conversational use may close there. A compact note is added only when a named reliance needs replay. The pattern succeeds when the relation from accepted problem-side claim to the directly governed value remains inspectable without treating the note, diagram, plan, trace, or publication as the subject entity or as proof that downstream work occurred.

### E.18.1:3 - Forces

| Force | P2W-preserved content | Pressure to manage |
|---|---|---|
| Problem-side usefulness | An accepted problem-side distinction may guide method, planning, work, or result interpretation. | The distinction is tempting to treat as a completed downstream claim. |
| Governing-kind precision | A continuing carry-through relation is admitted only after the next FPF kind or relation is recoverable. | Diagrams, graph-shaped expressions, and source wording can look sufficient without a record to write. |
| Practical readability | First use needs one recognizable claim, direct pattern, governed value, and continuation. | Too much boundary prose or mandatory record apparatus can hide the working P2W application. |
| Non-linear use | P2W may skip, branch, split, stop, or reopen continuations in the carry-through structure. | A readable diagram or graph-shaped expression can be mistaken for a prescribed project sequence. |
| Result usefulness | Result phrases often point to artifacts, telemetry, acceptance, measurement, refresh, or role enactability. | One broad result word can hide several different records. |
| Governing-pattern economy | Direct governing patterns keep their own rules. | Repeating their non-use doctrine inside P2W creates content fanout. |

### E.18.1:4 - Solution

**Local P2W mantra and demonstrative walkthrough.** The five actions below form the local P2W `mantra`: a short repeatable formulation that keeps this pattern's Solution in attention. This particular mantra also presents conditional continuations through the local P2W carry-through structure, so A.22.CGUS can admit it as a `DemonstrativeUnfoldingSlice@Context`; each table row is then one `mantra move` restored to `DemonstratedPatternUseRow@Context`. The local CGUS need not be registered as a separate corpus object. The Plain names add memorability, not a new kind or a project-work order.

| Shown continuation | Direct pattern | Solution use | Expected result | Current condition |
|---|---|---|---|---|
| Carry one accepted distinction. | `E.18.1` | Cite the accepted problem-side record and name the one distinction that must remain usable downstream. | A carried distinction with a named receiving use. | The problem-side record is accepted and a downstream use relies on the distinction. |
| Ask and recover. | `E.18.1` | State the next unsettled practical question; recover the exact FPF relation that can answer it and the pattern governing that relation. | One question, direct relation, and direct governing pattern named by value. | The next relation is unsettled; a diagram, source phrase, or familiar label is insufficient. |
| Apply the direct pattern. | The pattern recovered in the preceding row. | Apply its Solution while retaining the problem-side distinction in the method selection, plan, work relation, interpretation, or other directly governed value. | A directly governed value in which the carried distinction remains recoverable. | The relation and its governing pattern are recoverable. |
| Continue, branch, or stop. | `E.18.1` | Record one continuing relation, branch across independently governed relations, or retain a reduced-use cue and stop. | A bounded continuation set or an explicit stop condition. | One, several, or no relation-governed continuations are current. |
| Return locally after change. | The pattern governing the changed assumption, coordinated through `E.18.1`. | Return only to the smallest earlier P2W continuation affected by the changed assumption, then apply the direct pattern governing that continuation. | A local return with what still carries and what no longer carries stated. | Measurement, source currentness, problem-side content, or another relied-on assumption changed. |

The declarative carry-through structure below helps select the relation-governed P2W application. Fill a compact carry-through note or replay note only when the receiving use relies on a durable record. The structure shows which claim can be preserved, which exact relation and direct pattern are recovered, which governed value the practitioner obtains from that pattern, which cue is stopped, and which earlier continuation reopens after a relied-on relation changes.

Use the cheapest apparatus that keeps the current reliance honest:

1. **Ordinary conversational use.** Repeat the local P2W mantra, apply the direct pattern, obtain its governed value, and stop. Write no P2W note when feedback is fast, the use is local, and no later user relies on replay.
2. **Reliance-bearing use.** Add the compact note in `4.1` when transfer, audit, delayed feedback, expensive reversal, automation, or durable reuse depends on recovering the accepted claim and direct continuation.
3. **Structure-bearing use.** Add the exact `E.18.3` structure in `4.0b` only when branches, joins, guards, preserved structure, omitted-structure notes, path slices, or neighboring governed positions matter to the receiving use.

Moving upward in this ladder must answer a named reliance need. More fields do not make the subject result better and do not substitute for applying the direct pattern.

#### E.18.1:4.0 - `ProblemToWorkCarryThroughRelation@Context`

The positive P2W relation connects one accepted problem-card claim to one value already governed by the direct pattern for a named receiving use. `ProblemToWorkCarryThroughRelation@Context` is a context-dependent local species of `U.Relation`, not a root U-kind, work occurrence, result family, compact note, or substitute for the direct pattern.

```text
ProblemToWorkCarryThroughRelation@Context <: U.Relation:
  BoundedContextSlot = <P2WBoundedContextSlot, U.BoundedContext, U.BoundedContextRef>
  AcceptedProblemCardSlot = <AcceptedProblemCardSlot, U.Episteme, U.EpistemeRef constrained to ProblemCard@Context>
  CarriedClaimGraphSlot = <CarriedClaimGraphSlot, U.ClaimGraph, ByValue>
  ReceivingUseDescriptionSlot = <ReceivingUseDescriptionSlot, U.Episteme, U.EpistemeRef>
  DirectGoverningPatternSlot = <DirectGoverningPatternSlot, U.MethodDescription, U.EntityRef constrained to U.MethodDescription>
  GovernedValueKindSlot = <GovernedValueKindSlot, U.Kind, U.KindRef>
  GovernedValueSlot = <GovernedValueSlot, U.Entity, U.EntityRef>
  GovernedRelationSignatureSlot? = <GovernedRelationSignatureSlot, U.Signature, U.EntityRef constrained to U.Signature>
  CarryThroughRationaleSlot = <CarryThroughRationaleSlot, U.Episteme, U.EpistemeRef>
  PrecedingCarryThroughRelationSlot? = <PrecedingCarryThroughRelationSlot, ProblemToWorkCarryThroughRelation@Context, U.EntityRef constrained to this relation species>
  direction = AcceptedProblemCardSlot with CarriedClaimGraphSlot -> GovernedValueSlot for ReceivingUseDescriptionSlot
```

These SlotSpecs plus the stated direction are the exact `RelationSignature` for this local relation species. Its primary directed relata are the accepted problem card with the carried ClaimGraph slice and the governed value for the named receiving use. The relation depends on the accepted problem-card edition, the carried ClaimGraph slice, the bounded context, the receiving use, the governed value, and the pattern that governs that value. Those six positions determine relation identity. Rewording the rationale or republishing a compact note does not create a new relation. A changed accepted claim slice, receiving use, governed value edition, direct governing pattern, or context does. A relation instance is referenced through `U.EntityRef` constrained to `ProblemToWorkCarryThroughRelation@Context`.

`GovernedValueSlot` conforms to `GovernedValueKindSlot`. `GovernedRelationSignatureSlot` is present when the governed value is a relation instance. `DirectGoverningPatternSlot` names the pattern that governs that value or relation, and `CarryThroughRationaleSlot` states how the carried ClaimGraph content remains relevant to the receiving use. When a preceding relation is present, both relations cite the same accepted problem card and compatible carried ClaimGraph content, and the preceding governed value participates in the exact supporting relation for the current receiving use.

A bounded stop does not fabricate an empty relation instance: it remains conversational or is described by `ProblemToWorkStopDescription@Context` until a governed value exists. A later changed value does not rewrite the earlier relation; the replay note in `4.8` states what remains carried and a new or repaired direct relation is created only under its governing pattern.

The positive P2W relation fails admission when the governed ref does not conform to its stated kind, the named direct pattern does not govern that value or relation, a relation instance lacks its signature, the carry-through rationale cannot show how the accepted ClaimGraph content matters to the receiving use, or the alleged connection comes only from displayed proximity or chronology. Remove the failed relation instance. Then correct the value-kind pair, apply the actual direct pattern, split independently governed claims, or retain a reduced-use cue and stop until a positive relation can be written.

#### E.18.1:4.0a - P2W Declarative Carry-Through Structure

Use P2W as a declarative carry-through structure of relation-governed applications from an accepted `ProblemCard@Context` to directly governed FPF values. The structure is not a prescribed FPF-use procedure. A graph-shaped description, `U.MethodDescription`, `U.WorkPlan`, `TransformationFlowStructure`, flow valuation, or `E.18.2` mathematical description may describe or expose part of that structure only when its own direct pattern admits the use. None of those epistemes or structures becomes the subject EntityOfConcern merely by appearing in the P2W explanation. P2W shows which accepted claim remains relevant, which direct relation and pattern are recovered, which governed value results, which cue stops, and which continuation reopens after a relied-on relation changes.

The table below gives nine recurring recognition questions. Its row labels are Plain orientation, not position kinds, relation kinds, or a closed P2W ontology. In an explicit unfolding structure, every actual position is a `ConstraintGovernedUnfoldingPosition@Context` with a `SlotSpec`; every continuation to a neighboring claim is a `TransformationFlowGoverningPatternPositionRelation@Context` carrying the exact neighboring value kind, value reference, direct governing pattern, connection kind, rationale, and supporting relation when current. A concrete P2W use may answer one question, branch into several independently governed continuations, stop with a reduced-use cue, or return to the smallest earlier application whose assumption changed.

| Recognition question | Question answered | Result before continuation |
|---|---|---|
| Accepted problem-side basis | Which accepted `ProblemCard@Context` and which claim from that card must remain usable downstream? | Exact card reference, carried problem-card claim, and receiving use. |
| Next practical use | What question is still unsettled? | One practical question that does not presuppose its relation kind. |
| Preserved structure and payoff | What structure, invariant, loss, or payoff changes the next use? | Preserved structure, lost structure, payoff, and stop condition under `C.29` when mathematical-lens use is current. |
| Declaration or interpretation relation | Which exact signature, principle-frame, ontology, characteristic, measurement, normalization, or bridge relation is current? | One relation and its direct governing pattern named by value; split the case when several relations are current. |
| Mechanism and method relations | Is the current claim about mechanism meaning, method identity, method comparison, selection, or retained-set treatment? | One exact relation and governed value under its direct pattern. |
| Transformation and temporal relations | Is the current claim a bounded transformation, temporal aspect, dynamics claim, or temporal-claim adequacy use? | One exact direct relation under `A.3.4`, `C.27.TA`, `A.3.3`, or `C.27`. |
| Work preparation | Is a WorkPlan, plan item, planned slot filling, feasibility relation, or work-entry relation current? | One exact A.15-family governed value. |
| Performed work and result relations | Has dated `U.Work` occurred, and which separately governed result, measurement, evidence, acceptance, or source-use relations are current? | Exact work occurrence and separate direct relations; no generic result kind. |
| Return after changed assumption | Which measurement, source-currentness, problem-side, comparison, method, or other relied-on relation changed? | One local return to the smallest affected application and the direct pattern governing the changed relation. |
For Plain explanation, use the action words `carry`, `recover`, `write`, `split`, `stop`, and `return`. They are not P2W relation kinds and introduce no signatures. `Carry` preserves claim content from the accepted problem side. `Recover` names the exact FPF value kind or relation. `Write` creates or amends the value governed by the direct pattern. `Split` gives independently governed claims separate continuations. `Stop` retains a reduced-use cue when no continuation is recoverable. `Return` reopens the smallest earlier application whose relied-on relation changed.

#### E.18.1:4.0b - P2W use of an E.18.3 unfolding structure

When a named receiving use relies on explicit transformation-flow structure, fill the current `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` under `E.18.3`; do not create a parallel P2W block or copy a shortened substitute schema. The following is the P2W-relevant subset of that existing structure, not a separate record kind:

```text
P2W use of ConstraintGovernedTransformationFlowUnfoldingStructure@Context:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  acceptedProblemCardReferenceRef: U.EntityRef, referencing one UnfoldingStructureReferencedValueRelation@Context
    referenceKind: acceptedStartingRecord
    referencedValueKindRef: ProblemCard@Context
    directGoverningPatternRef: C.22.2
  carriedProblemCardClaimGraph: U.ClaimGraph by value
  structurePositionRefs[]: U.EntityRef, each referencing one ConstraintGovernedUnfoldingPosition@Context
  governingPatternPositionRelationRefs[]: U.EntityRef, each referencing one TransformationFlowGoverningPatternPositionRelation@Context
  admissibleNextFormKindRefs[]: U.KindRef
  methodWorkLinkageRef?: U.EntityRef, referencing one MethodWorkUnfoldingLinkage@Context
  evidenceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=evidence
  assuranceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=assurance
  admissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  nonAdmissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  governingPatternReturnBoundaryRefs[]: U.EntityRef, each referencing one UnfoldingStructureUseBoundaryCondition@Context
  stopBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
```

`carriedProblemCardClaimGraph` carries the whole `U.ClaimGraph` of the accepted problem card or a declared by-value projection that contains the carried claim content; it does not mint a distinction kind or an unavailable `ClaimGraphRef`. Every structure position keeps its exact SlotSpec. Every neighboring method, work, evidence, assurance, gate, architecture, publication, currentness, or result claim is connected through an exact governing-pattern-position relation or exact E.18.3 relation-reference episteme and remains governed by its direct pattern.

`admissibleNextFormKindRefs[]` carries exact next-form kinds only. Recommendation, method, WorkPlan, work occurrence, evidence, assurance, gate, architecture, publication, and return claims remain separate exact relations with separate direct governing patterns. Gate and other neighboring claims use `governingPatternPositionRelationRefs[]`; evidence and assurance use their separate subject-use relation references. Stop, non-admissible use, and return remain separate boundary conditions.

Use this fuller structure only when the receiving use depends on recoverable branches, joins, guards, preserved structure, omitted-structure notes, or neighboring governed positions. Otherwise use the compact positive note or stop description in `4.1` when named reliance requires a durable episteme. If a next continuation is work-facing, apply the A.15 family before claiming plan, readiness, launch, or performed work. `G.11` governs source currentness; `E.18` governs slice-local transformation-flow refresh; P2W returns only to the smallest affected application.

#### E.18.1:4.1 - Compact carry-through note
```text
ProblemToWorkCarryThroughNote@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef, referencing one ProblemToWorkCarryThroughRelation@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  acceptedProblemCardRef: U.EpistemeRef, referencing one ProblemCard@Context
  receivingUseDescriptionRef: U.EpistemeRef
  nextPracticalQuestionDescriptionRef: U.EpistemeRef
  continuationDescriptionRefs[1..*]: U.EpistemeRef
  returnConditionDescriptionRef?: U.EpistemeRef

ProblemToWorkStopDescription@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef, referencing one ProblemCard@Context
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  reducedUseCueDescriptionRef: U.EpistemeRef
  nextPracticalQuestionDescriptionRef: U.EpistemeRef
  stopConditionDescriptionRef: U.EpistemeRef
  returnConditionDescriptionRef?: U.EpistemeRef
```

Use `ProblemToWorkCarryThroughNote@Context` only after a positive relation exists; its EntityOfConcern is that relation. Use `ProblemToWorkStopDescription@Context` when no governed value and therefore no P2W relation exists; its EntityOfConcern is the accepted problem card, and its ClaimGraph states the reduced-use cue and stop. `U.EpistemeRef` is the admissible reference kind for citing either episteme.

For first-minute use, apply the direct pattern and continue or stop conversationally. Under named replay, transfer, audit, or delayed-feedback reliance, materialize a `ProblemToWorkCarryThroughNote@Context` for a positive continuation or a `ProblemToWorkStopDescription@Context` for a bounded stop. The positive note names the accepted problem card, receiving use, next practical question, and direct continuation. The stop description names the accepted problem card, reduced-use cue, next question, and stop condition. Neither episteme becomes a relation or substitutes for the governed value produced by the direct pattern.

Each continuation names one exact direct pattern and one exact governed use. If several continuations are current, write one continuation row for each; do not combine value kind and relation signature, method and mechanism, evidence and assurance, plan and work, or refresh and residual triage in one field.

| Compact note field | Filled cooling-fixture example |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-FAB-042`, accepted for a cooling-fixture deformation problem. |
| Carried problem-card claim | The deformation is not one more tuning defect; downstream comparison must preserve the conserved heat-flow structure identified by the problem card. |
| Receiving use | Decide which mathematical-lens result is needed before formal-substrate declaration and method comparison. |
| Next practical question | Which structure is preserved, which is lost, and where must the heat-flow lens stop? |
| Direct governing pattern | `C.29` Mathematical Lens Use. |
| Governed use and value written | Apply the `C.29` Solution and write its local lens-use result: target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
| Local non-overread | This continuation selects no method, WorkPlan, work occurrence, evidence verdict, or gate result. |
| Stop condition | Stop before method comparison until the comparator, measurement relation, and candidate-set relation are named by value. |
| Return condition | A changed measurement, reference plane, or source-currentness relation returns first to its direct governing pattern and then reopens only the dependent P2W continuation. |

The note closes positively when the direct pattern has produced or amended its governed value and the carried problem-card claim remains recoverable in that value or its stated basis. It closes by bounded stop when no direct continuation can be recovered.

#### E.18.1:4.1a - Development-loop relation selection

Cheap generation, open-ended search, or evolutionary-engineering work can produce many variants before the project has a stable problem, characteristic set, comparison basis, selected set, work entry, or currentness relation. Use the compact note above and select one next direct relation from the table below; do not add a parallel development-loop record schema.

| Current development question | Exact value or relation to name | Direct governing pattern |
|---|---|---|
| Problem formulation or opportunity | Accepted or revised `ProblemCard@Context` and the carried claim. | `C.22.2` |
| Characteristic, descriptor, indicator, acceptance, or parity construction | Exact characteristic-space, descriptor-set, indicator-use, acceptance, or parity relation. | `C.16`, `A.19`, `C.25`, or `G.9` according to the claim. |
| Variant retention or lineage | Exact archive, front, retained-population, descriptor, or lineage record. | `C.18`; use `C.19` when live-pool treatment is current. |
| Fair comparison | Exact comparison mechanism and result. | `A.19.CPM` |
| Selected set | Exact selected-set publication or set-returning relation. | `G.5` |
| Selector construction | Exact selector mechanism or choice rule. | `A.19.SelectorMechanism` |
| Local decision among explicit options | Exact decision or commitment relation. | `C.11` |
| Generator autonomy boundary | Exact autonomy declaration or boundary. | `E.16` |
| Evidence use | Exact evidence-use relation and evidence references. | `A.10` or `G.6` according to the claim. |
| Assurance-sensitive confidence use | Exact assurance claim and its evidence inputs. | `B.3` |
| Architecture candidate | Exact candidate architecture, structural-view, architecture-description, or interlevel-residual relation. | `C.30`, `C.30.ASV`, `C.30.AD`, or `C.30.ILC` according to the object. |
| Planned work | Exact `U.WorkPlan`, plan item, or work-entry relation. | The applicable A.15-family pattern. |
| Performed work | Exact dated `U.Work` occurrence. | `A.15.1` |
| Effect measurement | Exact bearer, characteristic, scale, measurement procedure, value, and evaluation use. | `C.16` and the direct evaluation pattern. |
| Source currentness or decay | Exact currentness, edition, freshness, or decay relation. | `G.11` |
| Interlevel residual triage | Exact residual relation and level transition. | The level-and-residual pattern governing that relation. |

Cheap variant generation shifts effort toward problem production, characterization, archive stewardship, fair comparison, explicit choice, autonomy boundaries, evidence, assurance, performed work, effect measurement, currentness, and repair. P2W preserves the accepted problem-side claim while one of those relations becomes current; an archive, front, selected set, confidence phrase, or choice rule does not authorize work. Source wording such as `trust budget`, `problem factory`, `solution factory`, or `factory of factories` remains a project label until the evidence, assurance, autonomy, work-organization, or other direct relation is named.

#### E.18.1:4.1b - Development-for-developed first-minute slice

For a fast DPF seed, keep the source-use and hardening continuations distinct. An accepted problem-side record may cite a `G.2` source-use relation, source `U.EpistemePublication`, source-pack cue or return, and provisional framework purpose. `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, and `G.11` govern their own proposal, review, authoring, evaluation, improvement, and currentness values. P2W preserves the carried claim only until one of those exact relations is selected.

**Cooling-module example.** `ProblemCard@Context PC-DEV-041` states that cheap generation produces many cooling-module layouts while fair problem framing and comparison remain weak. The carried claim is that maintainable low-energy variants must remain available until energy use, service access, manufacturability, thermal margin, and test cost are represented in the current characteristic and comparison relations. A `C.18` archive and front are current now. `A.19.CPM` comparison becomes current when its characteristic space and comparator are accepted. `G.5` selected-set publication remains stopped until that comparison and front are current. An `E.16` generator boundary may separately bound search and test spending. Prototype observations enter through `A.10`; assurance-sensitive confidence use enters through `B.3`. A `C.30` architecture-candidate relation appears only for retained layouts that change selected structure. A WorkPlan and dated Work remain absent until their A.15 relations are actually made. Thermal and serviceability measurement use must be named before any work-entry, gate, or authorization claim relies on it. `G.11` reopens currentness-dependent continuations when descriptors, tests, competitor information, or cited publication editions change.

The current next relation in this example is the `C.18` front record. Architecture comparison, selected-set publication, planning, and work are possible later continuations, not alternative fillers of one field.

#### E.18.1:4.2 - Positive carry-through table

| Recognition situation | P2W application | Governed value or continuation |
|---|---|---|
| Accepted problem-side output | State the accepted problem-card claim, receiving use, and question that remains unsettled. | The direct continuation is named; a compact note is written only under reliance. |
| First-principles or mathematical cue | Name preserved structure, lost structure, payoff, and stop condition. | Mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration. |
| Ontology, UTS, CHR, or `PrincipleFrame` cue | Order ontology, UTS, characteristic, measurement, and principle-frame declarations before downstream use. | Declaration-stack application. |
| Mechanism-position or method-position cue | Separate mechanism-position meaning from method-position meaning, method comparison, and retained-set handling. | Mechanism-position, method-position, method-comparison, selector, or retained-set application. |
| Bounded transformation or temporal-aspect cue | Separate bounded transformation, temporal aspect, and temporal-claim adequacy. | `A.3.4` for bounded transformation, `C.27.TA` for temporal aspect, or `C.27` when authored temporal-claim adequacy or currentness-use is being made. |
| Planning cue | Write or amend a planning record, plan item, evidence-reference pin, freshness request, or planned constraint. | `A.15.2 U.WorkPlan` or plan-item application. |
| Dated performed `U.Work` | Record the work occurrence and relation to plan, gate, launch values, provenance, and later result records. | Performed-work application plus any separate entry or provenance relation. |
| Result phrase | Split the phrase into artifact, resource, launch-value, telemetry, acceptance, measurement, source-use relation, quality, done-state, feedback, parity, refresh, or role-enactability relation. | One or more result-related applications. |
| Changed measurement or `G.11` source-currentness relation | Return to the smallest earlier application whose assumption changed. | Measurement, normalization, source-currentness repair, refresh, planning, method-comparison, or problem-side correction. |

#### E.18.1:4.3 - Direct-relation distinctions

Problem-side input: P2W starts only from an accepted problem-side record. The record carries the distinction that matters for the next FPF use, not the whole problem-side pattern.

First-principles and declarations: mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, ontology, UTS, CHR, measurement, normalization, bridge, and `PrincipleFrame` references are handled as declaration-stack applications. The P2W record names which declaration or direct governing relation is being written or cited, what structure is preserved, what is lost, and which downstream relation is still unsettled.

When mathematical wording points both to a formal declaration and to a mathematical lens, P2W does not decide by vocabulary. Use the slot discipline in `A.6.0:10a.1`: `A.6.0` governs `U.Signature(profile=FormalSubstrate)` declaration, `C.29` governs mathematical-lens use, `A.6.1` governs mechanism consumption or realization, and `E.18.1` governs only the carry-through cue and next-relation selection.

Mechanism and method: do not decide by noun. Recover the claim position. A mechanism-position claim names operation algebra, law set, applicability predicates, effect realization, or mechanism-description need. A method-position claim names a context-defined semantic way of doing work, candidate set, comparison, selector, retained set, or selected-record need. A shared source label, project-side name, or recognizable change concern may correspond to linked method and mechanism-position values. Conversational P2W use or the compact note preserves only the relation currently being carried through and leaves the other candidate governed value as a stopped cue unless the practitioner applies its direct pattern.

Transformation and temporal aspects: a problem-side distinction may point to a bounded transformation, a temporal aspect, and a temporal-claim adequacy question at once. Do not fold these into method, mechanism, plan, or work. `A.3.4` governs bounded transformation under conditions, including transformed object, pre-state, post-state, condition set, and admissible effect claim. `C.27.TA` governs temporal aspects such as interval, deadline, cadence, rhythm, synchronization, currentness window, recovery timing, or stabilization timing when the aspect itself is being named. `C.27` governs adequacy, supported use, unsupported use, or source-currentness use of authored temporal claims.

Planning and performed work: planning records are `A.15.2 U.WorkPlan` values or plan-item records, including evidence-reference pins, feasibility notes, freshness requests, and planned constraints. Performed work is a dated `U.Work` occurrence. P2W states which side of that boundary the continuation uses and which separately governed result relations have appeared.

Result carry-through: a result phrase is treated as a bundle of possible records. The P2W application is to unpack it before it guides any next FPF use.

Structure, publication, function, module-interface, and integration cues: a transformation-flow structure, mathematical graph description, diagram, or publication can help classify the P2W application. Function wording continues only as an `A.6.F` function or functional-relation claim; interface, port, protocol, connection, resource limit, or integration wording continues only as a module-interface, signature-slot, reusable-structure, or architecture relation named by value through `A.6.M`, `A.6.5`, `C.31`, or the `C.30` family. Otherwise the wording remains only a classification cue for conversational use or the compact note.

#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the distinction accepted on the problem side, recover the next FPF kind or relation, and stop when continuation would make a different governing relation current until that relation is named.

A local P2W application closes in either of two ways. It closes positively when the direct governing pattern has produced or amended the relation-governed value and the carried distinction remains recoverable in that value or its stated basis. It closes by bounded stop when no continuing relation can be recovered and the reduced-use cue plus stop condition are recorded. The next method selection, planning act, work occurrence, or evaluation is governed directly by its own pattern; it is not unfinished P2W work merely because it follows the carry-through.

A wider P2W carry-through slice remains current only while a named downstream receiving use relies on the accepted problem-side distinction. It closes when no remaining receiving use relies on that distinction and no return condition is current. A later changed assumption opens a new local return to the smallest affected application rather than retroactively keeping every earlier application open.

| Cue or changed assumption | Local P2W decision | Continuation |
|---|---|---|
| Accepted problem-side record or entry cue | Carry only the accepted distinction and the next FPF-use question. | Continue when the next FPF kind or relation is named; otherwise stop before P2W begins. |
| First-principles or mathematical wording | State preserved structure, lost structure, payoff, and stop condition. | Continue only as mathematical-lens use or as a `U.Signature(profile=FormalSubstrate)` declaration when that relation is being made. |
| Declaration-stack wording | Keep the declaration being made separate from measurement, normalization, comparison, ontology, or bridge relations. | Continue through the declaration relation that changes this P2W application. |
| Work-facing, temporal, or result wording | Recover the concrete mechanism-position, method-position, bounded-transformation, temporal, planning, performed-work, or result-related relation. | Continue through the matching application; split one wording span from an admitted source only when several relations are being made. |
| Another governed relation appears inside the wording span from an admitted source | Preserve the cue as wording from the admitted source or as a source-pack cue, but do not import its governing rule into P2W. | Continue only through the relation that changes this P2W application; leave the other cue stopped until its governing relation is being made. |

#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier applications without becoming a work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| changed source-use record, admitted reference-publication edition, source-pack reference, source-currentness relation, or publication-use relation | work-relevant appearance-based reliance repair, publication-use, `G.11` refresh, or the direct governing-pattern application named by the changed relation |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the evidence named by value, measurement, quality, role, or refresh relation |
| method set, comparator, selector, retained set, or selected record | method-comparison, selector, retained-set, or selected-record application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated `U.Work` occurrence remains a dated occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid after the compact carry-through note, or conversationally when no note is materialized, if several cues compete for the continuing FPF application. It names the relation family recovered by P2W before another pattern governs the claim; pattern names for those families are listed once in `E.18.1:12`.

| What the wording span from an admitted source makes current | Relation to recover before continuation | Local P2W application |
|---|---|---|
| accepted problem-side distinction | accepted `ProblemCard@Context` or equivalent accepted problem-side record plus one unsettled next relation | State what is carried and what question remains. |
| preserved or lost structure, invariant, near-sameness, formal payoff, or formal stop condition | mathematical-lens use or `U.Signature(profile=FormalSubstrate)` declaration | Name preserved structure, lost structure, payoff, and stop condition. |
| postulate, observability, unit, plane, comparator, threshold, ontology edition, CHR edition, normalization, bridge, or measurement | the declaration or measurement-family relation being made | Write or cite only that relation. |
| mechanism position, method position, method candidate set, comparator, selector, retained set, or selected record | the mechanism, method, comparison, selector, retained-set, or selected-record relation being made | Keep these relation positions distinct and continue only through the recovered one. |
| bounded transformation, temporal aspect, dynamics episteme, or temporal supported-use claim | `A.3.4`, `C.27.TA`, `A.3.3`, or `C.27` relation according to the claim being made | Split one phrase when it carries several of these relations. |
| planning record, plan item, performed work, launch value, result artifact, telemetry, acceptance, measurement, refresh, or role enactability | `A.15.2 U.WorkPlan`, plan-item, dated `U.Work`, or the result-related relation being made | Write or cite the record being made; do not let generic result wording guide the next FPF use. |
| structure, transformation-flow cue, diagram, scenario, view, graph expression, publication, module-interface, function, evidence-looking, gate-looking, or decision-looking wording | the relation named by value in the wording span from the admitted source, or no continuation if none is recoverable | Use the wording span only as classification until the relation is recovered. |

#### E.18.1:4.7 - Lowering and reopen block

Use this block when conversational P2W use or a compact carry-through note cannot preserve and continue the stronger-looking cue from a wording span in an admitted source or from a source-pack cue. P2W succeeds when it leaves one relation-governed application. If the application is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Observable lowering or stop condition | Reopened or continuing relation |
|---|---|---|
| Accepted problem-side record or entry cue | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles, mathematical, formal, or declaration-stack claim | Preserved structure, lost structure, payoff, stop condition, declaration relation, measurement relation, normalization relation, bridge relation, or comparison relation cannot be named. | Lower to a reduced-use cue from the wording span in the admitted source or from a source-pack cue; continue only after the recovered declaration, mathematical-lens, measurement, normalization, bridge, or comparison relation is being made. |
| Mechanism, method, selected-set, transformation, temporal, dynamics, planning, performed-work, or result claim | The wording span from the admitted source blurs relation positions that change different P2W applications. | Split to the recovered relation and continue only through that relation. |
| Another governed relation is only signaled by a label, diagram, port, module-interface phrase, publication, view, approval word, readiness word, or wording phrase | The wording span from the admitted source classifies a possible relation but does not name the relation being made. | Preserve the cue and stop local continuation until the governed relation is recoverable by value. |

#### E.18.1:4.8 - Replay after a changed relied-on relation

Use this compact replay note after `G.11` source-currentness repair, appearance-based reliance repair, changed measurement, changed problem-side record, FPF pattern change, or a use-found defect. It names the exact changed value or relation instead of classifying unlike changes as one input or assumption kind.

```text
ProblemToWorkReplayNote@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the original ProblemToWorkCarryThroughRelation@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  originalCarryThroughNoteRef: U.EpistemeRef, referencing one ProblemToWorkCarryThroughNote@Context
  changedValueRef: U.EntityRef
  changedValueKindRef: U.KindRef
  changedRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  changedValueDirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  stillCarriedClaimGraph: U.ClaimGraph by value
  noLongerCarriedClaimGraph?: U.ClaimGraph by value
  smallestReopenedContinuationDescriptionRef: U.EpistemeRef
  refreshCurrentnessLineRef?: U.EpistemeRef, referencing one RefreshCurrentnessLine@Context
  nextDirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
```

`changedRelationSignatureRef` is present when the changed value is a relation. A source edition, measurement value, unit, reference plane, method set, comparator, module-interface relation, publication-use relation, problem-side record, or FPF pattern publication retains its own exact kind and direct pattern. The two by-value ClaimGraph slices state which problem-card content still constrains downstream use and which content no longer does; `noLongerCarriedClaimGraph` is absent when no previously carried claim was invalidated. `smallestReopenedContinuationDescriptionRef` localizes repair; `refreshCurrentnessLineRef` appears only when a `G.11` `RefreshCurrentnessLine@Context` is current. The next direct pattern determines whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.

### E.18.1:5 - Archetypal Grounding

#### E.18.1:5.0 - Seal-failure carry-through

A maintenance team has an accepted `ProblemCard@Context` for recurrent seal failure. It records the operating conditions, the distinction between thermal deformation and material degradation, and the observations that would challenge that distinction. The team uses E.18.1 because diagnostic-method selection, repair planning, dated repair work, interpretation of the post-repair measurements, and return after a changed diagnosis all depend on preserving these accepted problem-side distinctions.

E.11.PUA may help the team inspect and apply one diagnostic-pattern candidate inside this flow. Its result might be one fit finding or one diagnostic method-selection input. That smaller result does not replace the accepted problem material, the repair plan, the repair work, or the later interpretation and return relations.


`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, an accepted problem-side record may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same record may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W application asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision claim. |
| Show with P2W | The team carries one accepted claim, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records dated `U.Work`, and unpacks result relations; it writes a compact note only when replay matters. | The team separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. The practitioner preserves that claim, applies `C.29` for mathematical-lens use, opens a separate `A.6.0` declaration continuation only if needed, and stops before method selection until comparator, measurement, and candidate-set relations are named.

2. **Planning from selected enough method.** A method family is selected enough for planning. The practitioner applies `A.15.2`; any compact P2W note cites the exact planning relation and states which problem-side claim it preserves. The WorkPlan carries its own planned constraints, fillers, evidence-reference pins, and freshness requests.

3. **Performed work after planning.** A dated work occurrence has appeared. `A.15.1` governs that occurrence. Any compact P2W note cites it and keeps gate, release, provenance, and launch-value relations separate from the occurrence.

4. **Result interpretation without generic result.** A source says the work result proves that the approach worked. P2W unpacks artifact, telemetry, measurement, evidence, acceptance, quality-evaluation, refresh, and role-enactability candidates before any one of them guides the next FPF use.

5. **Functional explanatory order.** A source diagram places `U.Signature(profile=FormalSubstrate)`, principle frame, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. The practitioner may use the diagram to recognize candidate continuations, while each direct pattern governs its value and the work family keeps physical time and performed-work chronology.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. P2W first recovers the module-interface relation under `A.6.M` and the transformation-flow relation under `E.18`; it opens separate continuations for `A.6.F` function, `A.15.2` planning, `A.15.1` dated work, `A.10` or `G.6` evidence, `A.20` or `A.21` gate, and `C.30` architecture claims only when each relation is current. Conversational use or the compact note carries only the relation that changes the present P2W application and leaves the other readings as stopped cues.

7. **Result measurement returns to planning.** A performed `U.Work` occurrence produced telemetry and an artifact. Later measurement shows that the planned module-interface constraint was interpreted against the wrong reference plane. P2W separates the measurement relation, reference-plane repair, `G.11` source-currentness repair, any `E.18` slice-local transformation-flow refresh, planning revision, and method-comparison relation before returning to the smallest dependent continuation. If the original `ProblemCard@Context` no longer states the right problem, the problem-side correction returns to the problem-side pattern.

#### E.18.1:5.2 - Additional worked situations

| Situation | P2W application | What changes |
|---|---|---|
| First-minute use | A practitioner has only an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." Write the accepted card reference, carried problem-card claim, receiving use, and next practical question. Then name one direct governing pattern and governed use, or state the stop condition. | The first continuation applies `C.29` to preserved structure, lost structure, payoff, declared use, and stop condition. A later formal-substrate declaration under `A.6.0` is a separate continuation; neither continuation selects a method or writes evidence. |
| Diagram and approval note in the same source publication or source-use record | The same source publication contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the claim carried from the accepted problem card. | Diagram cue, evidence-looking cue, and gate-looking cue are separated by relation recovery; conversational use or the compact note keeps only the carried claim and current direct relation. |
| Principle story without accepted problem-side record | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the source remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts a problem-side record. |
| Acceptance label hides wrong measurement | A dashboard shows a green acceptance label, but the measurement used the wrong reference plane. | Acceptance color does not guide the next FPF use; P2W returns to measurement, normalization, source-currentness repair, planning, and method comparison. |
| Changed unit after source-currentness repair | Later source-currentness repair changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Clinical differential carried into care planning | An accepted problem card distinguishes an adverse treatment effect from progression of the underlying condition. Diagnostic-method choice, care planning, performed clinical work, and outcome interpretation all depend on retaining that distinction. | The practitioner applies the clinical DPF and direct work, evidence, and measurement patterns. The problem-side claim does not authorize treatment, and a changed observation reopens the diagnostic continuation before any dependent plan or work-entry relation. |
| Learning difficulty carried into teaching and assessment | An accepted problem card distinguishes missing recall from a wrong conceptual model. Teaching-method selection, session planning, performed teaching work, and later assessment depend on that distinction. | The selected educational method and A.15 work relations keep their own values. A lesson plan or completed session does not prove changed learner capability; an assessment that challenges the distinction reopens the smallest method or problem continuation. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | The practitioner applies `C.29` for mathematical-lens use and, separately when current, `A.6.0` for `U.Signature(profile=FormalSubstrate)`; P2W preserves the accepted claim across those continuations without settling empirical truth or work authorization. |
| FPF relation rule changes after a P2W use | A governing FPF pattern changes the boundary for architecture-description, evidence, or `A.15.4` appearance-based reliance repair use. Fill the replay note with the changed value, exact kind, relation signature when applicable, direct governing pattern, still-carried claim, no-longer-carried claim, smallest reopened continuation, and next direct pattern. | The earlier use is replayed rather than trusted by age; only the affected direct relation and dependent P2W continuation change. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, `E.18` transformation-flow relation, dated `U.Work` occurrence, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W application being made is written; the remaining readings stop as named cues until their governed relations are being made. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side record. | The mathematical phrase lowers to a reduced-use cue; P2W does not justify method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source-use relation becomes stale | A result-looking source-use relation or publication cue is later replaced by a fresher source-use relation with a different artifact reference and measurement reference. | The practitioner applies `A.15.4` appearance-based reliance repair before continuing P2W; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled transformation-flow slices

These pilots are grounding checks, not source terminology to import. They exercise the same common shape: one current `TransformationFlowStructure` can relate several transformation-flow valuations or slices, one slice may develop or select a usable product, another slice may apply it, and an evaluation or refresh slice may return to the smallest affected development or application slice. The transformation-flow structure does not merge the slice-local objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each slice. Use each pilot to check whether the P2W use being made can name the joined transformation-flow slices, the carried object's slice-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service STF | An accepted service-quality problem carries heat or mass-balance structure through `U.Signature(profile=FormalSubstrate)`, declaration-stack, mechanism-position, normalization, method-selection, `A.15.2 U.WorkPlan` or plan-item records, dated `U.Work`, telemetry, measurement, and refresh relations. | Positive whole-chain readability, freshness, set-return selection, launch values only in performed work, and relation-local refresh. |
| Compiler design and run | Toolchain construction, compiler use, and product execution are separate applications; design and run changes pass through the gate and work relations being used. | `DesignRunTag`, launch gate, reproducible build currentness, `G.11` source-currentness relation, and no collapse of build, run, and product work. |
| TAMP and MPC robotics | Method selection and `A.15.2` planning records may be revised under a declared progress or budget condition before performed work. | Branching and cycle use without imposing one fixed work procedure, and no launch decision or performed-work claim before dated work occurs. |
| AutoML and QD | Method selection returns a Pareto, QD, front, or archive set under comparator and descriptor editions, not a hidden scalar winner. | Set-return discipline, comparator currentness, no hidden scalarization, and retained-set refresh. |
| Freshness or physical-transport case | Work planning and performed work depend on freshness windows, transport relations, units, reference planes, and source-currentness. | No implicit `latest`, no unbridged unit or plane comparison, and smallest affected refresh. |
| Integration under module-interface constraints | After assembly, a result phrase may mean role-enactability under module-interface constraints, evidence, gate, architecture, function, or work relation. | Result carry-through is not artifact-only or telemetry-only; module-interface and integration wording is accepted only after recovering the relation being claimed. |
| Tool-product-use chain | A design-tagged transformation-flow slice makes a tool; a later run or use slice uses the tool to make a chair; another slice uses the chair as context for writing a text. | One selected `TransformationFlowStructure` can relate all slices, but the same carried object may fill a run-result position in one slice and a design-side input, tool, context, or constraint position in another. The relation-position shift is explicit, tied to the `E.18` transformation-flow relation and any `DesignRunTag` being used, and does not change the object's kind by wording. |
| FPF pattern development and self-evolving specification | A development transformation-flow slice creates or repairs a pattern, specification, or process description through drafting, quality evaluation, publication projection, and admitted publication; a later use slice applies that product to its own `EntityOfConcern`; a defect found in use returns to the smallest development slice for repair. | Development, application, and evaluation slices are joined by transfer and return relations inside one selected `TransformationFlowStructure` while keeping objects and `DesignRunTag` boundaries separate; evaluation records or use-found evidence change the product through edits to the smallest development slice, not by entering the used publication's practitioner-facing prose. |

#### E.18.1:5.4 - Filled P2W carry-through notes

Use these as replayable filled examples, not as a second schema beside the compact note in `4.1`.

**Cooling-loop mathematical-lens continuation.**

| Compact note field | Filled value |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-COOL-017`, accepted for a cooling-loop stabilization problem. |
| Carried problem-card claim | The observed deformation is not one more tuning defect; later method comparison must preserve the conserved heat-flow structure. |
| Receiving use | Determine the mathematical-lens result needed before any formal-substrate declaration or method comparison. |
| Next practical question | Which structure is preserved, which is lost, and where does the heat-flow lens stop? |
| Direct governing pattern | `C.29` Mathematical Lens Use. |
| Governed use and value written | A C.29 local lens-use result naming target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
| Local stop | Method comparison waits until comparator, measurement, and candidate-set relations are named. A later `A.6.0` signature declaration is a separate continuation. |

**Port-throughput continuation split.**

| Compact note field | Filled value |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-PORT-008`, accepted for an integration-throughput problem. |
| Carried problem-card claim | The port-throughput constraint affects integration, but the source phrase does not decide which module-interface, transformation-flow, planning, work, evidence, gate, or architecture relation is current. |
| Receiving use | Make the current module-interface and transformation-flow relations inspectable without inferring readiness. |
| Next practical question | Which exact relation is being written now? |
| Continuation 1 | Apply `A.6.M` and write the exact module-interface relation for the port contract. |
| Continuation 2 | Apply `E.18` and write the exact transformation-flow relation that uses that interface. |
| Stopped cues | Apply `A.15.2` only if a planning constraint is actually being written. Evidence, gate, and architecture cues remain stopped until their direct relations are current. |
| Local stop | No readiness proof, work authorization, performed-work claim, evidence verdict, or gate result follows from the port phrase by itself. |

### E.18.1:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and epistemic**, **Prag**, **Did**. Scope: **accepted problem-side record plus carried distinction moving toward FPF applications**.

- **Governance bias (Gov):** authorization, gate, release, assurance, and decision cues are preserved only as local cues until the relevant FPF relation is recovered.
- **Architectural bias (Arch):** diagrams, selected structures, and module-interface language help classify the next P2W application; they do not displace the P2W carry-through relation.
- **Ontological and epistemic bias:** a source publication, diagram, compact note, or formal declaration remains separate from the subject EntityOfConcern and from the relation or result claimed through its direct pattern.
- **Pragmatic bias (Prag):** the carry-through structure is useful for action without becoming a prescribed project procedure.
- **Didactic bias (Did):** the local P2W mantra and positive carry-through structure come before the heavier relation aids, so precision does not bury the working P2W application.

### E.18.1:7 - Conformance Checklist

- `CC-E18.1-1` The P2W use starts from an accepted `ProblemCard@Context` or stops before P2W begins.
- `CC-E18.1-1a` The P2W relation, subject EntityOfConcern of each direct pattern, and supporting ProblemCard, compact note, diagram, plan, trace, or publication remain distinct. Note completeness does not prove subject change, performed work, evidence, acceptance, or result.
- `CC-E18.1-1b` Every positive `ProblemToWorkCarryThroughRelation@Context` fills the accepted ProblemCard, carried ClaimGraph, receiving-use description, direct governing pattern, governed value kind and ref, and carry-through rationale positions; relation signature is present when the governed value is a relation, and any preceding P2W relation preserves compatible problem-side claim content.
- `CC-E18.1-2` A materialized positive `ProblemToWorkCarryThroughNote@Context` references an existing P2W relation and has one or more separate continuation descriptions. A materialized `ProblemToWorkStopDescription@Context` instead references the accepted problem card and states the reduced-use cue and stop condition without fabricating a relation. Local non-overread and return conditions appear when relied on; absent fields are not filled by generic unions.
- `CC-E18.1-3` The positive carry-through structure is recoverable through the accepted problem-side record and carried claim, next practical question, exact E.18.3 positions when explicit structure is relied on, direct governing-pattern-position relations, exact next-form kinds, compact continuations, and distinct stop and return boundaries.
- `CC-E18.1-4` One wording span from an admitted source may split into several FPF applications; the record does not compress them into one generic token.
- `CC-E18.1-5` Result wording is unpacked into concrete result-related relations; a generic `WorkResult` kind is not admitted.
- `CC-E18.1-6` `PrincipleFrame` references keep postulates and CHR observability distinct from units, planes, comparators, thresholds, ontology editions, CHR editions, plans, work, evidence, and gates.
- `CC-E18.1-7` Measurement, `G.11` source-currentness relation, reference-plane, method-set, comparator, or problem-side changes return to the smallest affected application.
- `CC-E18.1-8` Non-P2W governing rules appear only as a recovered relation in `E.18.1:4.6` and as a pattern list in Relations, not as repeated local doctrine.
- `CC-E18.1-9` Local boundary wording remains only where it names a near-miss that changes the next P2W application.
- `CC-E18.1-10` The pattern leaves one useful relation-governed continuation: apply the direct pattern and obtain its governed value, write a reliance-conditioned compact note, split independently governed claims, stop with a reduced-use cue, or return to the smallest continuation affected by a changed relation.
- `CC-E18.1-11` Archetypal grounding can replay at least one coupled transformation-flow-slice pilot from `E.18.1:5.3`; the pilot joins development, application, evaluation, and repair slices in one selected `TransformationFlowStructure` while keeping their objects, slice-local relation positions, `DesignRunTag` boundaries, and evidence distinct. The self-evolving-spec pilot keeps development-slice evidence or use-found evidence outside the used pattern, specification, or process description.
- `CC-E18.1-12` Every carried claim family can be lowered, stopped, split, or reopened through `E.18.1:4.7`; a cue from a wording span in an admitted source or from a source-pack cue that cannot name the recovered FPF kind or relation remains a reduced-use cue.
- `CC-E18.1-13` Every replay names the changed value, exact value kind, relation signature when the changed value is a relation, direct governing pattern, still-carried and no-longer-carried ClaimGraph refs, smallest reopened continuation, any current `G.11` currentness line, and next direct pattern.
- `CC-E18.1-14` When a generated DPF seed or cheap framework seed enters P2W, the record names the `G.2` source-use record, source `U.EpistemePublication` reference, source-pack cue, or source-pack return when that source use is current, the problem-side cue when that is current, the next governing relation (`G.2`, `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, `G.11`, or another direct governing pattern), and the stop condition that prevents the seed from becoming public authority by generation alone.



### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats long lists of what P2W is not. | Keep relation discipline in `E.18.1:4.4`; make local sections state the next P2W application. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as relation-governed carry-through over FPF applications; use `stop`, `split`, and `return` relations. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | Write the carried distinction and next FPF-use question before selecting an application. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Record preserved structure, lost structure, payoff, and stop condition; continue through the recovered relation. |
| **Generic result token.** "Result" becomes one local kind. | Split the phrase into artifact, telemetry, acceptance, quality, measurement, refresh, source-use relation, evidence, or role-enactability relation. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

### E.18.1:9 - Consequences

| Consequence | Benefit | Cost or mitigation |
|---|---|---|
| A compact carry-through note can be materialized under named reliance. | A practitioner can replay how the accepted problem-side claim reached the continuing direct pattern and governed value. | Ordinary conversational use adds no record; transfer, audit, delayed-feedback, or other reliance-bearing use pays for the compact note. |
| Positive carry-through structure comes before boundary. | First use is readable before the heavier relation aid. | Boundary checks are still available in one canonical section. |
| Result language becomes unpackable. | Artifacts, telemetry, acceptance, measurement, refresh, and role enactability can be handled by their own records. | More than one application may be needed for one wording span from an admitted source. |
| P2W stays non-procedural. | The pattern can be used in many project situations without prescribing one local procedure. | A work procedure comes from method material or `A.15.2` planning material outside P2W. |
| Related patterns keep their authority. | P2W avoids duplicating evidence, gate, decision, architecture, publication, mechanism, and work-family doctrine. | Users consult the pattern named by the recovered relation when that relation is being made. |

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because a P2W relation can use transformation-flow structure as its setting when the carried claim spans several transformation-flow slices, typed positions, or returns. It does not define graph semantics or prescribe performed-work order. It helps a practitioner preserve an accepted problem-side claim while selecting and applying the next direct pattern; that pattern, not P2W, produces or amends the governed value.

The design puts the positive carry-through table first because repeated negative distinction sets can make a pattern whose primary EntityOfConcern is P2W behave like reference policing. P2W needs precision, but precision is useful here only when it leaves a surviving action: preserve the accepted claim, recover the exact direct relation and governing pattern, apply that pattern, obtain its governed value, materialize a compact note only under reliance, stop, split, or return locally.

### E.18.1:11 - SoTA-Echoing

The sources below are current comparators for specific P2W moves, not authorities imported by reputation. Each row states what changed in the Solution and which overread remains blocked.

| Exact source and currentness role | Move adopted in P2W | Overread rejected and practical effect |
|---|---|---|
| Roger Jiao, [*Towards rigorous problem formulation for engineering design research: from motivations to measurable claims via metric-measure-method*](https://doi.org/10.1080/09544828.2026.2633289), *Journal of Engineering Design* 37, 2026. Current engineering-design research comparator for problem-first coherence and method-first failure. | Keep the accepted problem-side claim, characteristic meaning, measurement relation, method, and validation use connected. Select the method only after the practical question and relevant characteristic or measurement relation are recoverable. This source changed the local P2W mantra, compact note, development-loop table, and method-selection stop. | Its Metric-Measure-Method vocabulary is not imported as FPF ontology: FPF recovers characteristic, scale, measurement, and `U.Method` under their direct patterns. Tool availability, fashionable AI, or a ready dataset cannot choose the problem or method. |
| Jenny Zhang et al., [*Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents*](https://arxiv.org/abs/2505.22954), 2025; Nico Pelleriti et al., [*What Do Evolutionary Coding Agents Evolve?*](https://arxiv.org/abs/2605.20086), 2026. A recent open-ended agent-evolution system paper paired with the current diagnostic limitation study. | Preserve generated variants and stepping stones in exact C.18 or C.19 structures; preserve the evaluator, edit history, comparison basis, and replay relation before interpreting a higher score. This source pair changed the development-loop relation table, cooling-module case, replay note, and proxy guard. | Archive membership or best benchmark score does not establish new algorithmic structure, method superiority, performed work outside the run, or subject improvement. Pelleriti et al. show why replay and intervention on search traces are needed to distinguish structural novelty, retuning, recombination, and evaluator overfit. |
| Yoichi Ishibashi, Taro Yano, and Masafumi Oyamada, [*Effective Harness Engineering for Algorithm Discovery with Coding Agents*](https://arxiv.org/abs/2605.15221), 2026. Current harness-design study under fixed budget with explicit evaluation-hack and parallel-execution concerns. | Keep generation method, harness, evaluator, budget, safety boundary, comparison, selected result, and later work as separate governed relations. This source changed the exact direct-relation selection table and the rule that evaluation or gate-looking material remains stopped until its governor is current. | A score produced by an exploitable evaluator or unsafe execution harness cannot carry method selection, evidence, gate passage, or work-entry use. More generated candidates do not substitute for an admissible comparison basis. |
| Haoxiang Qin et al., [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges*](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100, 2026. Current peer-reviewed QD survey comparator. | Keep descriptor space, diversity relation, archive or front, comparator, and selected-set publication distinct. This source changed the development-loop table, AutoML and QD pilot, and selected-set stop condition. | A front or archive is a structured retained set, not a scalar winner, method choice, decision, WorkPlan, or work authorization. Descriptor or distance change reopens only dependent comparison and selection continuations. |
| Sarah Malik and Antonios Kontsos, [*A Digital Thread Approach for Real-Time Defect Correction in Polymer Additive Manufacturing*](https://doi.org/10.32548/2026.me-04580), 2026; Sastry Veluri and Kannan Gopala Krishnan, [*Agentic Digital Thread for Managing the Non-Conformities in Manufacturing of Aerospace Products*](https://doi.org/10.4271/2026-26-0763), 2026. Current manufacturing feedback and proposed agentic digital-thread cases. | Connect sensed defects, process state, design or process correction, quality use, and return through exact relations; preserve the dated work occurrence and reopen only the dependent design, method, planning, or decision continuation. These sources changed the return table, measurement cases, and traceability boundary. | Data continuity, report generation, confidence prediction, or a named digital thread does not itself establish evidence sufficiency, approval, decision, authorization, or completed correction. The aerospace architecture is one proposed domain implementation, not universal P2W ontology. |
| Modelica Association, [*Modelica Language Specification 3.7*](https://specification.modelica.org/), 2026; JuliaHub, [Dyad syntax, analysis, and 3.1 release documentation](https://help.juliahub.com/dyad/stable/), 2026. Current relation-first multi-domain modeling comparators. | Keep reusable model components and relations, analysis definitions, model compilation, solver or simulation work, and analysis results as separately governed values. This source pair changed the diagram and model-use boundary and supports the exact E.18.3 relation projection. | Acausal model structure or an agent-authored model does not become one execution order, performed simulation, empirical evidence, accepted method, or physical result. A model representation can expose a continuation without supplying its downstream authority. |

As of 2026-07-11, the Jiao article, QD survey, manufacturing digital-thread papers, Modelica 3.7, and current Dyad documentation are publication or practice anchors. The DGM paper is a recent system result; the 2026 EvoTrace and harness papers are current preprints and carry corresponding uncertainty. Reopen these adoptions when stronger studies change problem-first method selection, distinguish generated structural novelty differently, revise evaluator-hack controls, alter QD archive semantics, or show that digital-thread continuity warrants a stronger use than the exact direct relation currently supports.

### E.18.1:12 - Relations
- `A.22.CGUS` supplies the general constraint-governed unfolding structure when P2W exposes typed structure positions, constraints, admissible next forms, and stop or return conditions.
- `E.18.3` supplies `ConstraintGovernedTransformationFlowUnfoldingStructure@Context`, its exact transformation-flow relation references, governing-pattern-position relations, and distinct stop and return boundaries when the P2W receiving use relies on explicit unfolding structure. P2W adds no parallel block or workflow authority.
- `G.2` governs source-use records, source-pack return, evidence anchors for admitted source publications, and source-currentness payloads before DPF hardening can rely on a seed drawn from those admitted sources.
- `E.4.DPF`, `E.4.PFAD`, and `E.4.PFR` govern DPF authoring, framework architecture decisions, and framework relation records when a generated or cheap seed is carried toward hardening.
- `E.23` governs repeated quality improvement only after the object version and evaluation are recoverable; P2W may carry a seed to that point but does not become the improvement method.
- `G.11` governs currentness, admitted-source decay, source-use relation change, edition change, and refresh when a changed source publication, source-use relation, or telemetry reopens the smallest affected P2W application.

- `E.18` governs selected `TransformationFlowStructure`, transfer annotations, flow valuation, `ConstraintValidity`, `GateFit`, gate profile, design tags, and run tags.
- `C.22.2` governs the accepted problem-side record and problem-side claims related to the carried distinction.
- `C.29`, `A.6.0`, `E.14`, `F.17`, `F.9`, `C.16`, `A.19.UNM`, and Part G govern mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, principle-frame, ontology, UTS, bridge, measurement, normalization, and comparison relations.
- `A.6.1` and `E.20` govern mechanism and mechanism-method stabilization relations. `A.3.4`, `C.27.TA`, `C.27`, and `A.3.3` govern bounded transformation, temporal aspect, temporal-claim adequacy, and dynamics-episteme relations.
- `G.5`, `G.9`, `A.19.SelectorMechanism`, `C.18`, and `C.19` govern candidate-set, comparison, selector, retained-set, and selected-record relations.
- `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, and `A.15.5` govern role-method-work alignment, performed work, planning, planned baselines, work-relevant appearance-based reliance repair, and work-entry readiness.
- `A.10`, `B.3`, `G.6`, `E.19`, `A.20`, `A.21`, and `C.11` govern evidence, assurance, provenance, conformance, gate, release, and decision claims.
- `C.30`, `C.30.AD`, `C.30.ASV`, `C.32.P2S`, `C.31`, `A.6.M`, `A.6.F`, `E.10`, `E.17`, and `E.17.EFP` govern architecture, architecture-description, structural-view, problem-to-structure architecturing, reusable-structure, module-interface, function, wording-use, publication, and publication-use claims.

### E.18.1:End

