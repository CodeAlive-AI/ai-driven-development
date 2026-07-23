## E.18.1 - P2W Problem-to-Work Carry-Through

> **Tech-name:** `ProblemToWorkCarryThrough`
> **Plain-name:** problem-to-work carry-through
> **Type:** Architectural pattern (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part E -> E.18 child pattern
> **Builds on:** `E.18` Transformation Flow Structure, `C.22.2` ProblemCard@Context, `A.6.0` `U.Signature`, `A.6.1` `U.Mechanism`, `A.3.4` actual bounded change, the A.15 work family, `A.15.PROD` local production-claim recovery, `A.6.RCD` exact missing-governor disposition, `A.6.REL` relation-occurrence and receiving-use discipline, `A.6.P` relational precision restoration, `A.6.P.WMR` wording-to-relation recovery, `C.29`, `C.16`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `F.8`, `F.18`, `F.17`, `F.9`, `G.5`, `G.9`, `G.11`, `A.20`, and `A.21`.
> **Purpose:** preserve selected distinctions from an accepted problem-side record as method selection, planning, performed work, result interpretation, and return become current.

### E.18.1:1 - Problem frame

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is not yet settled. The practitioner has an unsettled carry-through question: which problem-side distinction can be carried into the next FPF relation or record named by value?

The primary `EntityOfConcern` is the accepted `ProblemCard@Context` whose carried claim must remain usable under one named receiving-use viewpoint while the practitioner selects and applies one direct governor. P2W may carry that claim through method selection, planning when current, dated work when it occurs, an actual transformation when independently grounded, exact subject claims about what changed, result interpretation, and local return when an earlier assumption changes. No P2W relation kind or occurrence is introduced; P2W itself is neither the dated work nor a `U.Transformation`.

Keep three objects separate. The **accepted ProblemCard** is the `EntityOfConcern` of a materialized P2W note under the named receiving-use viewpoint. The **subject EntityOfConcern** of each direct pattern is the system, episteme, method, role, work occurrence, relation, or other project entity addressed by that pattern. The **compact note, diagram, plan, trace, and publication** are epistemes or publication-side values that describe, constrain, or make those direct claims inspectable. Later method enactment or dated work can change or preserve a subject EntityOfConcern; improving a P2W note or completing its fields does not establish that subject change, work occurrence, evidence, acceptance, or result.

**Primary working reader, concern, and viewpoint.** The primary reader is the practitioner who already has an accepted `ProblemCard@Context` and is choosing one next FPF-governed relation without treating source wording or a supporting episteme as downstream authority. The concern is use of that accepted claim in the current continuation, not a new relation occurrence or the whole downstream project. The viewpoint is the named receiving use: which direct relation and governing pattern can carry this accepted distinction into one governed value?

**So-what adoption test.** Adopt P2W only when preserving the accepted distinction changes the direct relation selected, the governed value written, or the decision to continue, split, stop, or return. If the direct relation and value are already settled and P2W would add only another note, do not use it; apply the direct pattern.

E.11.PUA governs a smaller use and may begin without `ProblemCard@Context`: apply one selected pattern to one current practical question, obtain the first directly typed result, and state its receiving use. E.18.1 begins only when the wider work-facing continuation depends on preserving accepted problem-side material. PUA may support one pattern inspection inside a P2W flow, but it does not replace the accepted-problem carry-through.


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

P2W solves a carry-through problem. A practitioner starts from an accepted problem-side claim, states the receiving use, recovers and applies the direct pattern for the next relation, and checks that the resulting governed value still carries that claim. Conversational use may close there. A compact note is added only when a named reliance needs replay. The pattern succeeds when the current use or reliance-conditioned note keeps the accepted problem-side claim, named receiving use, direct governor, and owner-returned value inspectable without treating their use-specific connection as a relation kind or occurrence, and without treating the note, diagram, plan, trace, or publication as the subject entity or as proof that downstream work occurred.

### E.18.1:3 - Forces

| Force | P2W-preserved content | Pressure to manage |
|---|---|---|
| Problem-side usefulness | An accepted problem-side distinction may guide method, planning, work, or result interpretation. | The distinction is tempting to treat as a completed downstream claim. |
| Governing-kind precision | The next relation and value become usable only through their direct governor; P2W adds no relation species. | Diagrams, graph-shaped expressions, source wording, and a filled note can look like an obtaining relation occurrence. |
| Practical readability | First use needs one recognizable claim, direct pattern, governed value, and continuation. | Too much boundary prose or mandatory record apparatus can hide the working P2W application. |
| Non-linear use | P2W may skip, branch, split, stop, or reopen continuations in the carry-through structure. | A readable diagram or graph-shaped expression can be mistaken for a prescribed project sequence. |
| Result usefulness | Result phrases often point to artifacts, telemetry, acceptance, measurement, refresh, or role enactability. | One broad result word can hide several different records. |
| Governing-pattern economy | Direct governing patterns keep their own rules. | Repeating their non-use doctrine inside P2W creates content fanout. |

### E.18.1:4 - Solution

**Local P2W mantra.** The five actions below form the local P2W `mantra`: a short repeatable formulation that keeps this pattern's Solution in attention. The Plain names add memorability, not a new kind or a project-work order.

| Shown continuation | Direct pattern | Solution use | Expected result | Current condition |
|---|---|---|---|---|
| Carry one accepted distinction. | `E.18.1` | Cite the accepted problem-side record and name the one distinction on which the downstream use relies. | A carried distinction with a named receiving use. | The problem-side record is accepted and a downstream use relies on the distinction. |
| Ask and recover. | `E.18.1` | State the next unsettled practical question; recover the exact FPF relation that can answer it and the pattern governing that relation. | One question, direct relation, and direct governing pattern named by value. | The next relation is unsettled; a diagram, source phrase, or familiar label is insufficient. |
| Apply the direct pattern. | The pattern recovered in the preceding row. | Apply its Solution while retaining the problem-side distinction in the method selection, plan, work relation, interpretation, or other directly governed value. | A directly governed value in which the carried distinction remains recoverable. | The relation and its governing pattern are recoverable. |
| Continue, branch, or stop. | `E.18.1` | Record one continuing relation, branch across independently governed relations, or retain a reduced-use cue and stop. | A bounded continuation set or an explicit stop condition. | One, several, or no relation-governed continuations are current. |
| Return locally after change. | The pattern governing the changed assumption, coordinated through `E.18.1`. | Return only to the smallest earlier P2W continuation affected by the changed assumption, then apply the direct pattern governing that continuation. | A local return with what still carries and what no longer carries stated. | Measurement, source currentness, problem-side content, or another relied-on assumption changed. |

For conformance or pattern-authoring use, the same conditional continuations can also be admitted by `A.22.CGUS` as a `DemonstrativeUnfoldingSlice@Context`; each table row is then one mantra move restored to `DemonstratedPatternUseRow@Context`. This heavier reading is not required for ordinary P2W use, and the local CGUS need not be registered as a separate corpus object.

The declarative carry-through structure below helps select the relation-governed P2W application. Fill a compact carry-through note or replay note only when the receiving use relies on a durable record. The structure shows which claim can be preserved, which exact relation and direct pattern are recovered, which governed value the practitioner obtains from that pattern, which cue is stopped, and which earlier continuation reopens after a relied-on relation changes.

Use the cheapest apparatus that keeps the current reliance honest:

1. **Ordinary conversational use.** Repeat the local P2W mantra, apply the direct pattern, obtain its governed value, and stop. Write no P2W note when feedback is fast, the use is local, and no later user relies on replay.
2. **Reliance-bearing use.** Add the compact note in `4.1` when transfer, audit, delayed feedback, expensive reversal, automation, or durable reuse depends on recovering the accepted claim and direct continuation.
3. **Structure-bearing use.** Add the exact `E.18.3` structure in `4.0b` only when branches, joins, guards, preserved structure, omitted-structure notes, path slices, or neighboring governed positions matter to the receiving use.

Moving upward in this ladder is justified only by a named reliance need. More fields do not make the subject result better and do not substitute for applying the direct pattern.

**PCP-MOD core-versus-extension cut.** The stable P2W core is only: one accepted problem-side claim, one named receiving use and unsettled question, one direct governor per independently governed claim, the exact governed value or honest stop returned by that owner, a split when several claims are current, and the smallest local return when a relied-on value changes.

| Material | Modularity status | Boundary |
|---|---|---|
| Accepted claim -> receiving use -> direct governor -> governed value or stop -> split/local return | **Stable P2W core** | Sections `4.0`, `4.0a`, and `4.2`-`4.7` state this interface without reproducing an owner's algorithm. |
| Compact positive, stop, or replay episteme | **Conditional reliance extension** | Open only for transfer, audit, delayed feedback, costly reversal, automation, or durable reuse; it records the core result and adds no prerequisite to conversational use. |
| Explicit transformation-flow unfolding structure | **Conditional structure extension owned by `A.22.CGUS` / `E.18.3`** | Open only when branches, joins, guards, paths, preserved structure, or stop/return positions matter; P2W supplies no hybrid or shortened structure schema. |
| Development-loop selection catalogue and DPF seed | **Conditional didactic extension** | Open only for the named development use; each row applies the unchanged core to one question and cannot turn the catalogue into a lifecycle, workflow, or authority record. |
| Practice naming and publication | **Conditional publication extension owned by `F.8` / `F.18` / `F.17`** | Open only for a named public, training, or tool-interface receiver after the governed practice is settled; naming adds no core field or result. |
| Relation obtaining, occurrence identity, reusable signatures, admission, production, evidence, gates, decisions, and other neighbouring doctrine | **Owner-side, not a P2W extension** | The direct owner returns the value, assertion, or blocker. P2W cites that returned object and never copies the owner's occurrence, derivation, admission, or assurance method. |

No conditional extension may add a mandatory input to ordinary P2W use, change the kind or identity of an owner-returned value, or mutate the stable core. When an extension is not current, omit it rather than filling its fields with generic placeholders.


**Assurance scope by use.** For a materialized positive compact note, check the accepted ProblemCard edition and carried ClaimGraph slice, named receiving-use viewpoint, governed value kind and ref, direct governing pattern, and carry-through rationale; for a stop description, check that no governed value has been fabricated and that the reduced-use cue and stop are exact. The note is a `C.2.1` episteme about the accepted ProblemCard, not a P2W relation occurrence or `RelationSignature`. For practitioner guidance or a conformance use, verify that the local mantra reaches one directly governed value or one honest stop without making the note, structure, reader, or checklist perform work. For pattern authoring or review, also replay the worked and discriminating cases, neighboring-authority boundaries, checklist, and no-new-kind and non-procedural boundaries. None of these assurance uses adds a work occurrence, transformation, evidence result, gate decision, or downstream subject claim.

#### E.18.1:4.0 - P2W result without a new relation species

An ordinary P2W application is a practitioner move: preserve one accepted problem-side claim, name the receiving use and unsettled question, apply one direct governing pattern per independent claim, and accept only the governed value or stop that owner returns. This move introduces no `ProblemToWorkCarryThroughRelation@Context`, reusable predicate definition, `RelationSignature`, or P2W relation occurrence.

When named reliance requires a durable claim, use the `C.2.1` episteme in `4.1`. Its exact `EntityOfConcern` is the accepted `ProblemCard@Context` under the named receiving-use viewpoint. Its ClaimGraph records the accepted card edition and carried claim slice, the unsettled question, the direct governor, the owner-returned value kind and ref or exact stop, and why the carried content remains relevant. Those are use-specific claim contents, not SlotSpecs of another relation species; the governed value retains its own kind, relation semantics when applicable, identity, and direct pattern.

Current P2W receivers consume the truth and replayability of that use-specific claim, not a stable identity for repeated P2W relation occurrences. The conversational move, optional positive note, and stop description therefore close the current use more economically than a relation-kind candidate. `A.6.RCD` stops before kind admission; `E.24`, `E.24.UK`, `A.6.0`, and a relation-species `F.18` naming decision do not open. If a later named receiver genuinely consumes P2W occurrence identity, recurrence, cessation, or participation in another relation, reopen `A.6.RCD` and obtain the required direct subject settlement and admission before declaring or instantiating such a kind.

A positive use closes only when the accepted card and carried slice are current for the named viewpoint, the direct pattern has returned the exact governed value for that use, and the rationale remains a truthful claim in the note or is directly recoverable in conversational use. A preceding P2W note may be cited for replay, but it supplies neither occurrence continuity nor a supporting relation; any relation among owner-returned values remains governed by its own direct pattern. If these conditions fail, correct the value-kind pair, apply the actual owner, split the claims, or retain a reduced-use cue and stop.

#### E.18.1:4.0a - P2W Declarative Carry-Through Structure

Use P2W as a declarative interface from one accepted `ProblemCard@Context` claim to values or stops returned by their direct governing patterns. P2W owns the carried claim, named receiving use, unsettled question, selected direct governor, resulting governed value or honest stop, and separation of independently governed continuations. It does not reproduce how a neighbouring pattern identifies, derives, admits, or evaluates that pattern's subject.

The table below is the complete P2W-local recognition architecture. When an owner-side condition is indispensable, P2W asks only whether the direct pattern has returned its exact governed value or blocker for the current use. The direct pattern retains its occurrence basis, recovery branches, criteria, derivation method, and admission law.

| P2W-local question | Required interface result | P2W disposition |
|---|---|---|
| What accepted problem-side content matters now? | Exact accepted card edition, carried ClaimGraph slice, and named receiving use. | Carry only that content. |
| What practical question remains unsettled? | One question stated without presupposing its answer or relation kind. | Continue to governor recovery. |
| Which direct relation and pattern govern the answer? | One direct governing pattern per independently governed claim. | Apply that pattern; split when several claims are current. |
| What did the direct pattern return? | Its exact governed value, a reduced-use cue, or an exact blocker. | Carry the value, lower the cue, or stop; do not recreate the owner's method. |
| Which continuations remain current? | One or more separately governed values, or no continuation. | Keep separate continuations; display order and chronology add no relation. |
| What changed later? | The changed relied-on relation and the smallest dependent continuation. | Reapply its direct pattern and reopen only that continuation. |

When the conditional structure extension opens, `A.22.CGUS` and `E.18.3` own the admitted structure, typed positions, SlotSpecs, relation references, and stop/return boundaries. P2W contributes only its accepted claim, receiving use, one owner-returned value or honest stop, split, and local return; it adds no structure field. Plain actions such as `carry`, `recover`, `write`, `split`, `stop`, and `return` are method-use guidance, not P2W relation kinds, commitments, permissions, gates, or substitute owner rules.


#### E.18.1:4.0b - Conditional structure extension through E.18.3

Open this extension only when the named receiving use depends on explicit branches, joins, guards, paths, preserved structures, omitted-structure notes, or distinct stop and return positions. `E.18.3` owns the complete `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` specialization, while `A.22.CGUS` owns its generic `ConstraintGovernedUnfoldingStructure@Context`, reference relations, typed positions, admissible next forms, and use-boundary relations. E.18.1 declares no P2W subset schema and no hybrid record that mixes fields from those two owners.

| P2W need in the structure-bearing use | Owner-side representation | P2W boundary |
|---|---|---|
| Cite the accepted starting `ProblemCard@Context` | The underlying A.22.CGUS `acceptedStartingRecordReferenceRefs[]` cites one `UnfoldingStructureReferencedValueRelation@Context` with `referenceKind=acceptedStartingRecord`, exact ProblemCard kind/ref, and `C.22.2` as direct owner. | The accepted card remains a record; it does not become the transformation-flow structure or one of its positions. |
| Expose transformation-flow topology or governed neighbouring positions | The exact E.18.3 `transformationPositionRefs[]`, `governingPatternPositionRelationRefs[]`, path/slice refs, and relation-reference epistemes selected by that receiving use. | E.18.3 and the direct neighbouring patterns own those values; P2W neither shortens their schemas nor turns display order into work order. |
| Preserve the carried claim and receiving-use rationale | Conversational P2W content or the conditional compact note in `4.1`; if the structure relies on that episteme, cite it through an exact owner-governed reference. | No `carriedProblemCardClaimGraph` or receiving-use field is added to the E.18.3 structure. |
| State a stop or smallest governing-pattern return | E.18.3 `stopBoundaryRef` and `governingPatternReturnBoundaryRefs[]`, backed by the corresponding A.22.CGUS boundary relations. | Stop and return remain distinct owner-governed boundaries; P2W contributes only the local continuation that stops or reopens. |

If explicit structure is not required, use the stable conversational core. If named reliance requires a durable episteme but not structure, use the compact positive note or stop description in `4.1`. If a next continuation is work-facing, apply the A.15 family before claiming plan, readiness, launch, or performed work. `G.11` governs source currentness; `E.18` governs slice-local transformation-flow refresh; P2W returns only to the smallest affected application.

#### E.18.1:4.1 - Compact carry-through note (conditional reliance extension)

Open this extension only when transfer, audit, delayed feedback, expensive reversal, automation, or durable reuse depends on replaying the stable P2W core. It records an already obtained owner result or honest stop; it is not a prerequisite for conversational use and does not widen the core.
```text
ProblemToWorkCarryThroughNote@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EpistemeRef, referencing one accepted ProblemCard@Context
  viewpointRef: U.ViewpointRef, naming the receiving-use viewpoint
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  carriedProblemCardClaimGraph: U.ClaimGraph by value
  nextPracticalQuestionDescriptionRef: U.EpistemeRef
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  governedValueKindRef: U.KindRef
  governedValueRef: U.EntityRef
  carryThroughRationaleDescriptionRef: U.EpistemeRef
  localNonOverreadDescriptionRef?: U.EpistemeRef
  precedingCarryThroughNoteRef?: U.EpistemeRef, referencing one ProblemToWorkCarryThroughNote@Context
  continuationDescriptionRefs[1..*]: U.EpistemeRef
  returnConditionDescriptionRef?: U.EpistemeRef

ProblemToWorkStopDescription@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EpistemeRef, referencing one ProblemCard@Context
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
Use `ProblemToWorkCarryThroughNote@Context` only after the direct pattern has returned an exact governed value. Its `EntityOfConcern` is the accepted ProblemCard under the named receiving-use viewpoint; its ClaimGraph states the use-specific carry-through claim and rationale. The note, its claim, and its optional predecessor reference are neither a reusable predicate definition nor a P2W relation kind or occurrence. Use `ProblemToWorkStopDescription@Context` when no governed value exists; it states the reduced-use cue and stop without fabricating a positive relation. `U.EpistemeRef` is the admissible reference kind for citing either episteme.

A positive note is well formed only when its governed value conforms to the named kind, its direct governing pattern owns that exact value, the carried ClaimGraph content remains relevant to the receiving use, and every listed continuation stays separately governed. When that value is a relation occurrence, assertion, or description, the note cites the exact owner-returned object; the direct owner retains its obtaining or claim basis, applicable occurrence-identity rule, and any receiver-conditioned reusable declaration or typed SlotSpecs. P2W adds no relation-specific field or sufficiency rule. A predecessor note supports replay only and does not establish identity or continuity of another occurrence.

For first-minute use, apply the direct pattern and continue or stop conversationally. Under named replay, transfer, audit, or delayed-feedback reliance, materialize a `ProblemToWorkCarryThroughNote@Context` for a positive continuation or a `ProblemToWorkStopDescription@Context` for a bounded stop. The positive note names the accepted problem card, receiving use, next practical question, and direct continuation. The stop description names the accepted problem card, reduced-use cue, next question, and stop condition. Neither episteme becomes a relation or substitutes for the governed value produced by the direct pattern.

Each continuation names one exact direct pattern and one exact governed use. If several continuations are current, write one continuation row for each; do not combine value kind and relation signature, method and mechanism, evidence and assurance, plan and work, or refresh and residual triage in one field.

| Compact note field | Filled cooling-fixture example |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-FAB-042`, accepted for a cooling-fixture deformation problem. |
| Carried problem-card claim | The deformation is not one more tuning defect; the downstream comparison use relies on preserving the conserved heat-flow structure identified by the problem card. |
| Receiving use | Decide which mathematical-lens result is needed before formal-substrate declaration and method comparison. |
| Next practical question | Which structure is preserved, which is lost, and where does the heat-flow lens stop? |
| Direct governing pattern | `C.29` Mathematical Lens Use. |
| Governed use and value written | Apply the `C.29` Solution and write its local lens-use result: target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
| Local non-overread | This continuation selects no method, WorkPlan, work occurrence, evidence verdict, or gate result. |
| Stop condition | Stop before method comparison until the comparator, measurement relation, and candidate-set relation are named by value. |
| Return condition | A changed measurement, reference plane, or source-currentness relation returns first to its direct governing pattern and then reopens only the dependent P2W continuation. |

The note closes positively when the direct pattern has produced or amended its governed value and the carried problem-card claim remains recoverable in that value or its stated basis. It closes by bounded stop when no direct continuation can be recovered.

#### E.18.1:4.1a - Conditional development-loop relation-selection extension

Open this didactic extension only when cheap generation, open-ended search, or evolutionary-engineering work has produced many variants before the project has a stable problem, characteristic set, comparison basis, selected set, work entry, or currentness relation. Apply the unchanged P2W core to one current development question through the catalogue below; do not add a parallel development-loop record schema or make the catalogue a universal continuation set.

| Current development question | Exact value or relation to name | Direct governing pattern |
|---|---|---|
| Problem formulation or opportunity | Accepted or revised `ProblemCard@Context` and the carried claim. | `C.22.2` |
| Characteristic-space construction | Exact `U.CharacteristicSpace`, characteristic slots, scales, value sets, and comparability boundary. | `A.19`; measurement values and their evidence remain with `C.16`. |
| Archive/front descriptor construction | Exact descriptor set and edition used by an archive or front. | `C.18`, citing its `A.19` characteristic-space basis. |
| Acceptance construction | Exact acceptance relation and criterion use. | `C.25`. |
| Parity construction | Exact parity plan or report with comparator, normalization, bridge, and evidence pins. | `G.9`; its comparison input remains governed by `A.19.CPM`. |
| Variant retention or lineage | Exact archive, front, retained-population, descriptor, or lineage record. | `C.18`; use `C.19` when live-pool treatment is current. |
| Fair comparison | Exact comparison mechanism and result. | `A.19.CPM` |
| Selected-set publication | Exact selector-facing publication and published set identity. | `G.5` |
| Selection mechanics or selected-set result | Exact selector mechanism, selection application, or selected-set result before publication. | `A.19.SelectorMechanism` |
| Local decision among explicit options | Exact `C.11` choice result; any accountable obligation, recommendation-as-duty, or prohibition remains a separate `A.2.8 U.Commitment`. | `C.11` for the choice; `A.2.8` only when the deontic relation is independently current. |
| Generator autonomy boundary | Exact autonomy declaration or boundary. | `E.16` |
| Evidence use | Exact evidence-use relation and evidence references. | `A.10`. |
| Provenance use | Exact provenance or lineage relation and its cited records. | `G.6`. |
| Assurance-sensitive confidence use | Exact assurance claim and its evidence inputs. | `B.3` |
| Architecture candidate | Exact candidate architecture relation. | `C.30`. |
| Structural view | Exact structural-view relation. | `C.30.ASV`. |
| Architecture description | Exact architecture-description relation. | `C.30.AD`. |
| Interlevel residual | Exact interlevel-residual relation and level transition. | `C.30.ILC`. |
| Planned work | Exact `U.WorkPlan`, plan item, or work-entry relation. | The applicable A.15-family pattern. |
| Performed work | Exact dated Work occurrence admitted under `U.Work`. | `A.15.1` |
| Effect measurement | Exact bearer, characteristic, scale, measurement procedure, value, and evaluation use. | `C.16` and the direct evaluation pattern. |
| Source currentness or decay | Exact currentness, edition, freshness, or decay relation. | `G.11` |


Cheap variant generation shifts effort toward problem production, characterization, archive stewardship, fair comparison, explicit choice, autonomy boundaries, evidence, assurance, performed work, effect measurement, currentness, and repair. P2W preserves the accepted problem-side claim while one of those relations becomes current; an archive, front, selected set, confidence phrase, or choice rule does not authorize work. Source wording such as `trust budget`, `problem factory`, `solution factory`, or `factory of factories` remains a project label until the evidence, assurance, autonomy, work-organization, or other direct relation is named.

#### E.18.1:4.1b - Conditional development-for-developed first-minute extension

Open this didactic extension only for a fast DPF seed, and keep the source-use and hardening continuations distinct. An accepted problem-side record may cite a `G.2` source-use relation, source `U.EpistemePublication`, source-pack cue or return, and provisional framework purpose. `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, and `G.11` govern their own proposal, review, authoring, evaluation, improvement, and currentness values. P2W preserves the carried claim only until one of those exact relations is selected.

**Cooling-module example.** `ProblemCard@Context PC-DEV-041` states that cheap generation produces many cooling-module layouts while fair problem framing and comparison remain weak. The carried claim is that the current candidate set retains maintainable low-energy variants until energy use, service access, manufacturability, thermal margin, and test cost are represented in the current characteristic and comparison relations. A `C.18` archive and front are current now. `A.19.CPM` comparison becomes current when its characteristic space and comparator are accepted. `G.5` selected-set publication remains stopped until that comparison and front are current. An `E.16` generator boundary may separately bound search and test spending. Prototype observations enter through `A.10`; assurance-sensitive confidence use enters through `B.3`. A `C.30` architecture-candidate relation appears only for retained layouts that change selected structure. A WorkPlan and dated Work remain absent until their A.15 relations are actually made. Any work-entry, gate, or authorization claim that relies on thermal or serviceability facts remains stopped until the exact measurement use is named. `G.11` reopens currentness-dependent continuations when descriptors, tests, competitor information, or cited publication editions change.

The current next relation in this example is the `C.18` front record. Architecture comparison, selected-set publication, planning, and work are possible later continuations, not alternative fillers of one field.

#### E.18.1:4.1c - Conditional naming and publication extension

Ordinary P2W application skips this extension. Open it only when a pattern author, publisher, training use, or tool interface must decide whether a P2W expression may be cited beyond its current local use. Naming and publication apply only to already governed values; they neither admit a relation kind nor create an episteme instance. The F.8/F.18/F.17 result references the stable core and adds no core field, continuation, or closure condition.

**F.8 decisions.**

| Candidate expression | Recovered governed object and current use | F.8 result and naming route | Blocked use and reopen condition |
|---|---|---|---|
| `ProblemToWorkCarryThrough` | E.18.1 as one `U.MethodDescription`: the public practice that carries an accepted ProblemCard claim to one owner-returned value or honest stop | `nameDirectPatternValue`; E.18.1 owns the practice, F.18 owns the NameCard, and F.17 publishes the public row under `FPFCoreReferenceScheme` | Not a relation kind, occurrence, workflow, work, or result; reopen when the practice boundary or public reader use changes |
| `ProblemToWorkCarryThroughNote@Context` | E.18.1-local `U.Kind` label for reliance-conditioned `U.Episteme` instances governed by `4.1` and identified under `C.2.1` | `reuseLocalSenseLabel`; the declared use is pattern-local and names no external receiver, so no NameCard or F.17 row is current | Not a relation kind, occurrence, evidence result, or work record; reopen before any external citation, cross-context reuse, training label, or tool-interface use |
| `ProblemToWorkStopDescription@Context` | E.18.1-local `U.Kind` label for `U.Episteme` instances that state a reduced-use cue and exact stop | `reuseLocalSenseLabel`; keep it inside E.18.1 without a NameCard or term row | Not a blocker kind, failure state, empty relation, or rejection record; reopen before any external or durable reuse |
| `ProblemToWorkReplayNote@Context` | E.18.1-local `U.Kind` label for `U.Episteme` instances that state retained content and the smallest reopen after change | `reuseLocalSenseLabel`; keep it inside E.18.1 without a NameCard or term row | Not a refresh process, change log, relation occurrence, or authority record; reopen before any external or durable reuse |

The remaining field labels in `4.0a`, `4.1`, and `4.8` are one-off schema-position phrases under their containing forms. Their F.8 result is `localPhraseOnly`; they receive no NameCards or term rows. A later receiver that needs any local form or field label outside E.18.1 must reopen this decision before reuse.

**F.18 NameCard for the public practice name.**

```text
NameCard:
  NameCardId: NameCard.E18.1.ProblemToWorkCarryThrough.FPFPublic
  GovernedValueRef: E.18.1
  GoverningPatternRef: E.18.1
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: SenseCell.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21
  TechLabel: ProblemToWorkCarryThrough
  PlainLabel: problem-to-work carry-through
  CandidateSet: [Problem-to-Work Carry-Through, Problem-to-Governed-Value Carry-Through, Accepted-Claim Continuation, Work-Facing Claim Preservation, Problem-to-Work Path, Principles-to-Work Carry-Through]
  RejectedCandidates: governed-value hides the work-facing receiving use; continuation suggests order; preservation suggests unchanged content; path suggests workflow; principles excludes non-principle ProblemCard claims
  SelectionRationale: the selected pair keeps the established P2W mnemonic while the no-relation head fits a practitioner discipline that may continue, split, stop, or return
  BridgeRefs: none
  UnifiedTermRowRef: UTS.E18.1.ProblemToWorkCarryThrough.FPFPublic
  LineageEntries: Principles-to-Work Carry-Through -> Problem-to-Work Carry-Through when the accepted source widened from principle cues to any accepted ProblemCard claim
  RefreshCondition: reopen when the governed practice, reference scheme, public reader use, or repeated workflow/relation overread changes
```

**F.17 public term row and local-sense basis.**

```text
UnifiedTermRow:
  UTSRowId: UTS.E18.1.ProblemToWorkCarryThrough.FPFPublic
  UnificationThreadId: E18.1.P2W.Terminology.2026-07-21
  Block: P2W practice
  GovernedValueRef: E.18.1
  GovernedValueKindRef: U.MethodDescription
  DirectGoverningPatternRef: E.18.1
  UnifiedTechName: ProblemToWorkCarryThrough
  UnifiedPlainName: problem-to-work carry-through
  NameCardRef: NameCard.E18.1.ProblemToWorkCarryThrough.FPFPublic
  SenseCellRefs: [SenseCell.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21]
  BridgeRefs: none
  RowRationale: publish the no-relation practice name for stable reader reference
  AdmissibleUse: identify and cite the E.18.1 practitioner discipline
  BlockedUse: infer a relation kind, occurrence, workflow, work, transformation, evidence, or result
  RowEdition: 2026-07-21
  CurrentnessCondition: review when E.18.1, its NameCard, reference scheme, or public reader use changes

SenseCell.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21:
  Context: FPF English public publication, edition 2026-07-21
  LocalExpression: problem-to-work carry-through
  LocalSense: the E.18.1 practice that carries one accepted ProblemCard claim to one owner-returned value or honest stop for a named receiving use
  NameCardRef: NameCard.E18.1.ProblemToWorkCarryThrough.FPFPublic
  LocalSenseBasisRelationRefs: [LocalSenseBasisRelation.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21]
```

`LocalSenseBasisRelation.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21` relates that SenseCell to basis episteme `E.18.1` as a `U.MethodDescription`, narrowed to units `1-4`, in the same public context. Its description supports the stated practice sense and admits naming-only citation; it admits no relation, workflow, work, result, evidence, authority, or external reuse of the three local note-form labels. No Bridge is current.

#### E.18.1:4.2 - Positive carry-through table

| Recognition situation | P2W application | Governed value or stop carried forward |
|---|---|---|
| Accepted problem-side output | State the accepted problem-card claim, receiving use, and unsettled question. | The selected direct continuation; a compact note only under named reliance. |
| Mathematical-lens cue | Recover the exact preserved structure, lost structure, payoff, declared use, and stop under `C.29`. | The `C.29` lens-use result or stop; mathematical wording supplies no declaration or project-world authority. |
| `FormalSubstrate` or `PrincipleFrame` declaration cue | Recover the already governed subject and ranged value, then apply `A.6.0` to the exact selected profile. | One profile-specific `U.Signature` declaration or stop; the two profiles are not stages in a declaration sequence. |
| Ontology, predicate-definition, relation-kind, or U-kind cue | Return first to the direct subject pattern; use `A.6.RCD` only for the residual relation-bearing claim and `E.24` or `E.24.UK` for the exact admission question. | The owner-returned admitted value, local result, or blocker; a generic declaration-stack application is not a result. |
| UTS, bridge, measurement, normalization, comparison, or parity cue | Select the exact current object: UTS publication -> `F.17`; bridge -> `F.9`; measurement -> `C.16`; normalization -> `A.19.UNM`; comparison -> `A.19.CPM`; parity plan/report -> `G.9`. | One value or stop from the named owner; no member of the cue family substitutes for another. |
| Mechanism or method cue | Apply `A.6.1` to an exact mechanism declaration, `E.20` to mechanism-method stabilization, or `A.3.1` to the exact method question. | One mechanism, stabilization, or method result or stop; the cue supplies none of the neighboring values. |
| Archive/front or live-pool cue | Apply `C.18` to archive/front stewardship or `C.19` to policy over a still-live pool. | One archive/front record or one live-pool policy result; neither is selection or selected-set publication. |
| Comparison, parity, selector, or selected-set cue | Apply `A.19.CPM` to general comparison, `G.9` only to parity/benchmark use, `A.19.SelectorMechanism` to selection mechanics, and `G.5` to selector-facing selected-set publication. | One comparison, parity, selection, or publication result from its exact owner; no hidden scalar winner or positional owner inference. |
| Transformation or temporal cue | Apply the direct transformation or temporal pattern for the exact claim. | Only the owner-returned actual-change, temporal, dynamics, or adequacy value, or its blocker; P2W does not reconstruct the occurrence basis. |
| Planning, performed-work, or work-to-change cue | Apply the direct planning, work, or subject-governed relation pattern. | Separate owner-returned plan, dated-work, and work-to-change values or stops. |
| Evidence, assurance, provenance, conformance, gate, release, readiness, or authorization cue | Split the claims first. Evidence -> `A.10`; assurance -> `B.3`; provenance -> `G.6`. For conformance, recover the exact subject and rule: `A.20` owns only E.18 step constraint validity, `A.21` owns only an obtaining gate-decision relation and its publication, `E.19` owns only FPF pattern-quality review, and another subject or regulatory conformance claim stays with its exact owner. Work-entry readiness -> `A.15.5`. A release act or authorization stays with its direct owner; an A.21 gate decision may govern a release-crossing decision but is not itself release, authorization, readiness, or performed work. | One result or stop from each exact owner. A conformance label, green gate display, release cue, or readiness word supplies none of the neighboring claims. |
| Publication face or form, publication occurrence or bounded availability, explanation-faithfulness, or publication-work cue | Multi-view publication face/form -> `E.17`; exact publication occurrence and bounded availability use -> `E.24.PUB`; explanation-faithfulness use -> `E.17.EFP`; publication work -> its exact A.15.1 work and direct subject relations. | One owner-returned face/form, publication occurrence or availability result, explanation-faithfulness result, work result, or stop; form, occurrence, work, access, and reliance remain distinct. |
| Result or production cue | Apply `A.6.P.WMR` to unresolved result wording and `A.15.PROD` only for the production question actually current. | Carry each exact direct subject claim, exact `A.6.1` application binding, or exact local `A.15.PROD`/`A.6.RCD` claim on its own continuation. If WMR returns an exact non-assertability result, preserve its independent `factually unsupported`, `missing-information`, or `missing-governor` reason; only the last is an ontology blocker that names the affected use and future owner. No generic result or omnibus production value is introduced. |
| Changed measurement, source-currentness, problem-side, or other relied-on relation | Return first to the pattern governing the changed relation. | The amended value or blocker and the smallest dependent P2W continuation. |

These continuations form a typed non-linear carry-through, not a required sequence. P2W consumes direct-owner results; it does not reproduce their algorithms or make display order, chronology, shared wording, or a common referent supply a missing relation.


#### E.18.1:4.3 - Direct-relation distinctions

P2W starts from an accepted problem-side record and carries only the distinction needed by the named receiving use. It selects the direct relation to apply next; the neighbouring pattern remains responsible for deciding whether its governed value obtains and for returning that value or an exact stop.

When one wording span makes several claims current, P2W splits them before continuation. A mathematical lens and a formal declaration, a mechanism and a method, a plan and dated work, an actual change and a work-to-change claim, or a result and a production question therefore travel on separate owner-governed continuations. P2W records which owner result is being carried, not the neighbour's internal basis.

Four bounded interface conditions prevent common authority leaks without copying owner doctrine:

- an actual-transformation continuation is available only when `A.3.4` has returned an exact current transformation value;
- a work-to-change continuation is available only when its direct subject governor has returned the exact claim or blocker;
- unresolved result wording first returns to `A.6.P.WMR`, after which P2W carries each truthful exit separately or stops;
- a production continuation opens only for the exact question selected under `A.15.PROD`, whose returned local claim or blocker remains distinct from work, change, result, acceptance, and release.

The same interface rule applies to declarations, measurement, evidence, gates, decisions, publication, architecture, function, module interfaces, integration, and refresh: recover the exact relation, apply its direct pattern, and carry only that governed result or stop. For a conformance, gate, release, or publication cue, first distinguish the exact subject and relation: step validity, pattern-quality review, gate-decision publication, release or authorization, work-entry readiness, publication face/form, publication occurrence/availability, explanation-faithfulness, and publication work have different owners. A source label, diagram, note, plan, trace, or familiar noun may help recognize a candidate relation but never supplies the owner result.


#### E.18.1:4.4 - Boundary and relation discipline

P2W is not a catalogue of boundary doctrines from other governing patterns. It has one local boundary rule: carry only the accepted problem-side distinction, recover the next direct relation and governor, and continue only with the value or honest stop that governor returns. If several relations are current, split them; if none is recoverable, retain a reduced-use cue and stop.

Bounded owner-side interface conditions may appear in `4.0a`, `4.2`, `4.3`, `4.6`, a discriminating case, or a conformance row only when they decide whether P2W may accept an owner-returned value, must split it, or must stop. They do not restate the neighbour's occurrence basis, recovery branches, production criteria, derivation method, or admission law. Section `4.6` is the canonical P2W relation-selection aid; Relations is the canonical owner map.

A local P2W application closes positively when the direct governing pattern has produced or amended its governed value and the carried distinction remains recoverable in that value or its stated basis. It closes by bounded stop when no continuing relation can be recovered and the reduced-use cue plus stop condition are stated. A following method selection, planning act, work occurrence, evaluation, or other owner application is not unfinished P2W work.

A wider P2W carry-through slice remains current only while a named downstream receiving use relies on the accepted problem-side distinction. It closes when no remaining receiving use relies on that distinction and no return condition is current. A later changed assumption opens a new local return to the smallest affected application rather than retroactively keeping every earlier application open.


#### E.18.1:4.5 - Return and refresh rule

P2W can reopen earlier applications without becoming a work procedure. Reopen only the smallest application whose assumption changed:

| Changed assumption | Smallest reopened application |
|---|---|
| measurement value, unit, scale, reference plane, or transport relation | measurement, normalization, bridge, or comparison application |
| changed source-use record, admitted reference-publication edition, source-pack reference, source-currentness relation, or publication-use relation | work-relevant appearance-based reliance repair, publication-use, `G.11` refresh, or the direct governing-pattern application named by the changed relation |
| result artifact, telemetry, acceptance, done-state, or role-enactability record | result-related split plus the evidence named by value, measurement, quality, role, or refresh relation |
| archive, front, or retained exploration value | `C.18` archive/front stewardship application |
| still-live pool treatment | `C.19` live-pool policy application |
| comparator or general comparison result | `A.19.CPM` comparison application; use `G.9` only when the changed object is a parity plan or report |
| selector mechanics or selected-set result | `A.19.SelectorMechanism` selection application |
| selector-facing selected-set publication | `G.5` publication application |
| problem-side statement or accepted carried distinction | problem-side correction in the problem-card application |

The earlier dated Work occurrence admitted under `U.Work` remains the same world-side occurrence. P2W may cite it during return, but the changed assumption determines which application is reopened.

#### E.18.1:4.6 - Relation selection aid

Use this aid conversationally, or after the compact carry-through note, when several cues compete for the next FPF application. Pattern names for the relation families are listed once in `E.18.1:12`; their detailed rules remain in those patterns.

| Current P2W condition | Relation-selection move | P2W result |
|---|---|---|
| One exact relation is recoverable. | Apply its direct governing pattern. | Carry the returned governed value or exact stop. |
| Several independently governed relations are current. | Split them and apply each direct pattern separately. | Keep one continuation per returned value or blocker. |
| A cue names only a possible relation family. | Preserve the cue without choosing an answer by vocabulary. | Stop until the exact relation and governor are recoverable. |
| A direct owner returns a reduced-use result or blocker. | Keep that result intact. | Lower or stop; do not replace it with a P2W-local surrogate. |
| A relied-on relation changes. | Reapply its direct pattern. | Reopen only the smallest dependent continuation. |


#### E.18.1:4.7 - Lowering and reopen block

Use this block when conversational P2W use or a compact carry-through note cannot preserve and continue the stronger-looking cue from a wording span in an admitted source or from a source-pack cue. P2W succeeds when it leaves one relation-governed application. If the application is not recoverable by value, lower the cue, stop, or reopen the smallest affected application.

| Claim family | Observable lowering or stop condition | Reopened or continuing relation |
|---|---|---|
| Accepted problem-side record or entry cue | No accepted `ProblemCard@Context`, or the accepted problem-side statement changes the carried distinction. | Stop before P2W begins, or return to the problem-side record named by value that changed. |
| First-principles or mathematical-lens claim | Preserved structure, lost structure, payoff, declared use, or stop cannot be named. | Lower to a reduced-use cue; continue only after `C.29` returns the exact lens-use value or stop. |
| `FormalSubstrate` or `PrincipleFrame` declaration claim | The already governed subject, ranged value, selected profile, or applicable declaration law cannot be named. | Preserve the cue and stop until the exact `A.6.0` profile-specific declaration is current. |
| Ontology, predicate-definition, relation-kind, U-kind, UTS, bridge, measurement, normalization, comparison, or parity claim | The exact governed object or its direct owner in the canonical Relations map cannot be named. | Preserve the cue and stop; continue only through the one mapped owner for the object actually current. |
| Mechanism, method, selected-set, transformation, temporal, dynamics, planning, performed-work, or result claim | The wording span from the admitted source blurs relation positions that change different P2W applications. | Split to the recovered relation and continue only through that relation. |
| Another governed relation is only signaled by a label, diagram, port, module-interface phrase, publication, view, approval word, readiness word, or wording phrase | The wording span from the admitted source classifies a possible relation but does not name the relation being made. | Preserve the cue and stop local continuation until the governed relation is recoverable by value. |

#### E.18.1:4.8 - Conditional reliance replay after a changed owner value

Open this extension only when a named reliance needs a durable account of what still carries after `G.11` source-currentness repair, appearance-based reliance repair, changed measurement, changed problem-side record, FPF pattern change, or a use-found defect. Ordinary local return uses the stable core in `4.5` without materializing this note.

```text
ProblemToWorkReplayNote@Context <: U.Episteme:
  entityOfConcernRef: U.EpistemeRef, referencing the accepted ProblemCard carried by the original ProblemToWorkCarryThroughNote@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  originalCarryThroughNoteRef: U.EpistemeRef, referencing one ProblemToWorkCarryThroughNote@Context
  changedValueRef: U.EntityRef
  changedValueKindRef: U.KindRef
  changedValueDirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  stillCarriedClaimGraph: U.ClaimGraph by value
  noLongerCarriedClaimGraph?: U.ClaimGraph by value
  smallestReopenedContinuationDescriptionRef: U.EpistemeRef
  refreshCurrentnessLineRef?: U.EpistemeRef, referencing one RefreshCurrentnessLine@Context
  nextDirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
```

`changedValueRef` names the exact owner-returned changed value, occurrence, assertion, or description episteme; `changedValueKindRef` names that selected object's kind, and `changedValueDirectGoverningPatternRef` names its direct owner. When the changed object is a relation, reapply that direct pattern and `A.6.REL` before filling the replay note. The referenced owner result retains the admitted relation kind, actual participants, obtaining occurrence or assertion basis, applicable occurrence-identity rule, and any reusable `RelationSignature` or typed SlotSpecs required by its own named receiver. E.18.1 does not copy those fields or decide which relation representation is sufficient.

Thus a readable direct-relation assertion, an explicitly individuated occurrence, and a typed assertion or description can all enter P2W replay, but only as the exact object returned by their owner. Relation use or individuation does not become signature-dependent merely because P2W cites it; a typed receiving episteme carries its own signature reference when its owner requires one.

A source edition, measurement value, unit, reference plane, method set, comparator, module-interface relation, publication-use relation, problem-side record, or FPF pattern publication likewise retains its own exact kind and direct pattern. The two by-value ClaimGraph slices state which problem-card content still constrains downstream use and which content no longer does; `noLongerCarriedClaimGraph` is absent when no previously carried claim was invalidated. `smallestReopenedContinuationDescriptionRef` localizes repair; `refreshCurrentnessLineRef` appears only when a `G.11` `RefreshCurrentnessLine@Context` is current. The next direct pattern determines whether to continue, stop, split, lower to a reduced-use cue, or return to the problem-side pattern.

### E.18.1:5 - Archetypal Grounding

#### E.18.1:5.0 - Seal-failure carry-through

A maintenance team has an accepted `ProblemCard@Context` for recurrent seal failure. It records the operating conditions, the distinction between thermal deformation and material degradation, and the observations that would challenge that distinction. The team uses E.18.1 because diagnostic-method selection, repair planning, dated repair work, interpretation of the post-repair measurements, and return after a changed diagnosis all depend on preserving these accepted problem-side distinctions.

E.11.PUA may help the team inspect and apply one diagnostic-pattern candidate inside this flow. Its result might be one fit finding or one diagnostic method-selection input. That smaller result does not replace the accepted problem material, the repair plan, the repair work, or the later interpretation and return relations.


`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, an accepted problem-side record may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same record may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W application asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision claim. |
| Show with P2W | The team carries one accepted claim, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records references to dated Work occurrences while keeping those records as separate epistemes, and unpacks result relations; it writes a compact note only when replay matters. | The team separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. The practitioner preserves that claim, applies `C.29` for the mathematical-lens question, and carries the returned lens-use value or stop. A separately current formal declaration opens its own owner-governed continuation; method selection waits for its own direct relations.

2. **Planning from selected enough method.** A method family is selected enough for planning. The practitioner applies `A.15.2`; any compact P2W note cites the owner-returned planning value and the problem-side claim it preserves. The WorkPlan retains its own content and authority.

3. **Performed work after planning.** A dated work occurrence has appeared, so the practitioner applies `A.15.1` and carries that returned value. Any actual-change claim opens `A.3.4`; any work-to-change claim opens its exact direct subject governor. P2W carries only the values or blockers those owners return and keeps production, gate, release, provenance, launch-value, and later result questions on separate continuations.

4. **Result interpretation without generic result.** A source says the work result proves that the approach worked. The practitioner applies `A.6.P.WMR`; P2W carries each returned exact direct subject claim, exact `A.6.1` application binding, or exact local `A.15.PROD`/`A.6.RCD` claim on its own continuation. If WMR returns an exact non-assertability result, P2W preserves `factually unsupported`, `missing-information`, or `missing-governor` as independently reasoned; only the last is an ontology blocker that names the affected use and future owner. P2W neither repeats the recovery method nor turns the wording into a generic result or production value.

5. **Functional explanatory order.** A source diagram places formal declaration, principle framing, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. The diagram helps recognize candidate continuations, but P2W carries only values returned by their direct patterns; the display order supplies no sequence or authority.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. The practitioner opens separate `A.6.M` module-interface and `E.18` transformation-flow applications. Planning, work, evidence, gate, function, and architecture cues remain stopped until their exact relations are current. Conversational P2W use or the compact note carries only the owner result that changes the present application.

7. **Result measurement returns to planning.** A source says one performed work occurrence produced telemetry and an artifact. `A.6.P.WMR` first returns an exact direct subject claim, exact `A.6.1` application binding, exact local `A.15.PROD`/`A.6.RCD` claim, or exact non-assertability result. P2W carries those results separately; the last independently records `factually unsupported`, `missing-information`, or `missing-governor`, and only `missing-governor` is an ontology blocker that names the affected use and future owner. When later `C.16` measurement changes the relied-on reference plane, the practitioner reapplies `C.16` and `G.11`, then reopens only the dependent `A.15.2` planning, method-comparison, or `C.22.2` problem-side continuation. The earlier dated work occurrence is not rewritten.

8. **Pump 14 pressure adjustment.** Accepted `ProblemCard@Context PC-P14-PRESSURE` says Pump 14 discharge pressure is below its operating band. The selected set-point-adjustment `U.Method`, `WP-P14-2026-07-15` when planning is current, dated work `W-P14-ADJUST-1010-1020`, actual change `T-P14-PRESSURE-RISE`, and the work-to-change claim remain separate values from `A.3.1`, `A.15.2`, `A.15.1`, `A.3.4`, and the exact direct subject governor. P2W carries only the values or blockers those owners return; later measurement and decision uses remain separate. `A.15.PROD` returns no production continuation for this case, and no transformation-composition question is current.


#### E.18.1:5.2 - Additional worked situations

| Situation | P2W application | What changes |
|---|---|---|
| First-minute use | A practitioner has only an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." State the accepted card reference, carried problem-card claim, receiving use, and next practical question conversationally, or in a compact note only under named reliance. Then name one direct governing pattern and governed use, or state the stop condition. | The first continuation applies `C.29` to preserved structure, lost structure, payoff, declared use, and stop condition. A later formal-substrate declaration under `A.6.0` is a separate continuation; neither continuation selects a method or writes evidence. |
| Diagram and approval note in the same source publication or source-use record | The same source publication contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the claim carried from the accepted problem card. | Diagram cue, evidence-looking cue, and gate-looking cue are separated by relation recovery; conversational use or the compact note keeps only the carried claim and current direct relation. |
| Principle story without accepted problem-side record | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the source remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts a problem-side record. |
| Acceptance label hides wrong measurement | A dashboard shows a green acceptance label, but the measurement used the wrong reference plane. | Acceptance color does not guide the next FPF use; P2W returns to measurement, normalization, source-currentness repair, planning, and method comparison. |
| Changed unit after source-currentness repair | Later source-currentness repair changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated Work occurrence admitted under `U.Work` is cited, not rewritten. |
| Clinical differential carried into care planning | An accepted problem card distinguishes an adverse treatment effect from progression of the underlying condition. Diagnostic-method choice, care planning, performed clinical work, and outcome interpretation all depend on retaining that distinction. | The practitioner applies the clinical DPF and direct work, evidence, and measurement patterns. The problem-side claim does not authorize treatment, and a changed observation reopens the diagnostic continuation before any dependent plan or work-entry relation. |
| Learning difficulty carried into teaching and assessment | An accepted problem card distinguishes missing recall from a wrong conceptual model. Teaching-method selection, session planning, performed teaching work, and later assessment depend on that distinction. | The selected educational method and A.15 work relations keep their own values. A lesson plan or completed session does not prove changed learner capability; an assessment that challenges the distinction reopens the smallest method or problem continuation. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | The practitioner applies `C.29` for mathematical-lens use and, separately when current, `A.6.0` for `U.Signature(profile=FormalSubstrate)`; P2W preserves the accepted claim across those continuations without settling empirical truth or work authorization. |
| FPF relation rule changes after a P2W use | Reapply the direct relation owner and `A.6.REL`, then fill the replay note with the exact owner-returned changed occurrence, assertion, or description ref, its exact kind and direct owner, the still-carried and no-longer-carried claims, smallest reopened continuation, and next direct pattern. The referenced owner result, not P2W fields, retains participants, obtaining or claim basis, identity rule, and any receiver-conditioned signature. | The earlier use is replayed rather than trusted by age; only the affected direct relation and dependent P2W continuation change. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, `E.18` transformation-flow relation, a dated Work occurrence admitted under `U.Work`, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W application being made is written; the remaining readings stop as named cues until their governed relations are being made. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side record. | The mathematical phrase lowers to a reduced-use cue; P2W does not justify method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source-use relation becomes stale | A result-looking source-use relation or publication cue is later replaced by a fresher source-use relation with a different artifact reference and measurement reference. | The practitioner applies `A.15.4` appearance-based reliance repair before continuing P2W; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled transformation-flow slices

These pilots are grounding checks, not source terminology to import. They exercise the same common shape: one current `TransformationFlowStructure` can relate several transformation-flow valuations or slices, one slice may develop or select a usable product, another slice may apply it, and an evaluation or refresh slice may return to the smallest affected development or application slice. The transformation-flow structure does not merge the slice-local objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each slice. Use each pilot to check whether the P2W use being made can name the joined transformation-flow slices, the carried object's slice-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service STF | An accepted service-quality problem carries heat or mass-balance structure through `U.Signature(profile=FormalSubstrate)`, declaration-stack, mechanism-position, normalization, method-selection, `A.15.2 U.WorkPlan` or plan-item records, a dated Work occurrence admitted under `U.Work`, telemetry, measurement, and refresh relations. | Positive whole-chain readability, freshness, set-return selection, actual launch values only through independently obtaining direct relations or exact A.6.1 bindings involving the world-side Work occurrence, and relation-local refresh. |
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
| Carried problem-card claim | The observed deformation is not one more tuning defect; the later method-comparison use relies on preserving the conserved heat-flow structure. |
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
- **Architectural bias (Arch):** diagrams, selected structures, and module-interface language help classify the next P2W application; they do not displace the accepted claim, receiving-use viewpoint, direct governor, or owner-returned value.
- **Ontological and epistemic bias:** a source publication, diagram, compact note, or formal declaration remains separate from the subject EntityOfConcern and from the relation or result claimed through its direct pattern.
- **Pragmatic bias (Prag):** the carry-through structure is useful for action without becoming a prescribed project procedure.
- **Didactic bias (Did):** the local P2W mantra and positive carry-through structure come before the heavier relation aids, so precision does not bury the working P2W application.

### E.18.1:7 - Conformance Checklist

- `CC-E18.1-1` The P2W use starts from an accepted `ProblemCard@Context` or stops before P2W begins.
- `CC-E18.1-1a` The accepted ProblemCard under the named receiving-use viewpoint, each direct pattern's subject EntityOfConcern, and every supporting compact note, diagram, plan, trace, or publication remain distinct. Note completeness does not prove a P2W relation occurrence, subject change, performed work, evidence, acceptance, or result.
- `CC-E18.1-1b` Every positive `ProblemToWorkCarryThroughNote@Context` identifies one accepted ProblemCard as its EntityOfConcern, names one receiving-use viewpoint, carries the exact ProblemCard ClaimGraph slice, and cites the direct governing pattern, governed value kind and ref, and carry-through rationale. It introduces no reusable P2W predicate, `RelationSignature`, relation kind, or occurrence. When the governed value is a relation occurrence, assertion, or description, the note cites the exact owner-returned object; the owner result retains the admitted kind, obtaining or claim basis, applicable identity rule, and any reusable declaration required by its own named receiver.
- `CC-E18.1-1c` When the conditional publication extension is current, the public practice name has an exact F.8 `nameDirectPatternValue` decision, F.18 NameCard, and F.17 row for the already governed E.18.1 method description. The three note-form designators remain E.18.1-local under `reuseLocalSenseLabel`, and schema-position field labels remain `localPhraseOnly`; neither group receives publication apparatus before an external receiver makes durable reuse current. No naming or publication object admits a kind, relation, occurrence, work, evidence, or authority claim or adds a stable-core input.
- `CC-E18.1-2` A materialized positive `ProblemToWorkCarryThroughNote@Context` contains the current use-specific claim and has one or more separate continuation descriptions. A materialized `ProblemToWorkStopDescription@Context` instead states the reduced-use cue and stop without fabricating a relation. Local non-overread and return conditions appear when relied on; absent fields are not filled by generic unions.
- `CC-E18.1-3` The stable core remains recoverable without a note or explicit structure: accepted problem-side claim, named receiving use and question, exact direct governor, owner-returned value or honest stop, split, and smallest local return. When explicit structure is current, its generic fields and relations come unchanged from `A.22.CGUS` and its transformation-flow specialization comes unchanged from `E.18.3`; E.18.1 adds no hybrid schema.
- `CC-E18.1-4` One wording span from an admitted source may split into several FPF applications; the record does not compress them into one generic token.
- `CC-E18.1-5` Result wording is unpacked into concrete result-related relations; a generic `WorkResult` kind is not admitted.
- `CC-E18.1-6` `PrincipleFrame` references keep postulates and CHR observability distinct from units, planes, comparators, thresholds, ontology editions, CHR editions, plans, work, evidence, and gates.
- `CC-E18.1-7` Measurement, `G.11` source-currentness relation, reference-plane, method-set, comparator, or problem-side changes return to the smallest affected application.
- `CC-E18.1-8` The stable P2W core contains only accepted claim, receiving use/question, direct governor, owner-returned value or honest stop, split, and local return. Reliance notes, explicit E.18.3 structure, development catalogues, and naming/publication are conditional extensions. Well-formedness constraint: no conditional extension adds a mandatory input, changes an owner-returned value, or mutates the core. Relation obtaining and identity, occurrence declarations, admission, production, evidence, gate, decision, and other neighbouring algorithms remain with their direct owners.
- `CC-E18.1-9` Local boundary wording remains only where it names a near-miss that changes the next P2W application.
- `CC-E18.1-10` The pattern leaves one useful relation-governed continuation: apply the direct pattern and obtain its governed value, write a reliance-conditioned compact note, split independently governed claims, stop with a reduced-use cue, or return to the smallest continuation affected by a changed relation.
- `CC-E18.1-11` For a structure-bearing conformance or pattern-authoring use, archetypal grounding can replay at least one coupled transformation-flow-slice pilot from `E.18.1:5.3`; the pilot uses one owner-governed `TransformationFlowStructure` while keeping objects, slice-local relation positions, `DesignRunTag` boundaries, and evidence distinct. The self-evolving-spec pilot keeps development-slice evidence or use-found evidence outside the used pattern, specification, or process description. Ordinary P2W use does not open this extension.
- `CC-E18.1-12` Every carried claim family can be lowered, stopped, split, or reopened through `E.18.1:4.7`; a cue from a wording span in an admitted source or from a source-pack cue that cannot name the recovered FPF kind or relation remains a reduced-use cue.
- `CC-E18.1-13` Every materialized replay names the changed owner-returned value, occurrence, assertion, or description, its exact kind and direct governing pattern, still-carried and no-longer-carried ClaimGraph refs, smallest reopened continuation, any current `G.11` currentness line, and next direct pattern. When the changed object is relation-bearing, its referenced owner result—not a P2W copy—retains the admitted kind, participants, obtaining or claim basis, applicable occurrence-identity rule, and any receiver-conditioned `RelationSignature` or typed SlotSpecs.
- `CC-E18.1-14` When a generated DPF seed or cheap framework seed enters P2W, the record names the `G.2` source-use record, source `U.EpistemePublication` reference, source-pack cue, or source-pack return when that source use is current, the problem-side cue when that is current, the next governing relation (`G.2`, `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, `G.11`, or another direct governing pattern), and the stop condition that prevents the seed from becoming public authority by generation alone.
- `CC-E18.1-15` An actual-transformation continuation carries only an exact current value or blocker returned by `A.3.4`; E.18.1 does not reconstruct the occurrence basis or infer actuality or composition from a method, plan, model, description, flow position, adjacency, shared work, or common referent.
- `CC-E18.1-16` A work-to-change or production continuation carries only the separate value or blocker returned by its direct subject governor or `A.15.PROD`; E.18.1 does not reproduce either owner's branches or criteria. The Pump 14 replay reaches adjustment work, actual pressure change, measurement, and decision without opening production or transformation-composition.



### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats neighbouring algorithms or long lists of what P2W is not. | Keep the owner-return interface in `4.4`, relation selection in `4.6`, and the canonical owner map in Relations; local cases name only the owner-returned value, split, or stop needed by P2W. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as relation-governed carry-through over FPF applications; use the `stop`, `split`, and `return` moves as method-use guidance, never as P2W relation kinds or a project-work order. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, work, evidence, or result. | State the carried distinction and next FPF-use question conversationally; materialize a compact note only under named reliance, then apply the direct pattern. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Apply `C.29` to preserved structure, lost structure, payoff, declared use, and stop condition; continue only through the recovered relation, and add a P2W note only under named reliance. |
| **Generic result token.** "Result" becomes one local kind or P2W repeats the complete recovery method. | Apply `A.6.P.WMR`, then carry each exact direct subject claim, exact `A.6.1` application binding, or exact local `A.15.PROD`/`A.6.RCD` claim separately. Preserve an exact non-assertability result as independently `factually unsupported`, `missing-information`, or `missing-governor`; stop and name a future owner only for `missing-governor`. Introduce no generic result family. |
| **Choice-as-commitment.** A `C.11` choice result is treated as an accountable obligation, recommendation-as-duty, or prohibition. | Keep the option set, comparison basis, choice rule, and choice result under `C.11`; open a separate `A.2.8 U.Commitment` only when its accountable subject, modality, referents, scope, and window are independently recoverable. |
| **Plan, path, or proximity as actual change.** A desired state, model, method, plan, flow arrow, adjacent work, or common affected referent is treated as an actual or composite transformation. | Apply `A.3.4` and any direct work-to-change or `A.15.PROD` owner separately; carry only their returned values or blockers and open no composition or production continuation by proximity. |
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

`E.18.1` is a child of `E.18` because a P2W use can rely on transformation-flow structure as its setting when the carried claim spans several transformation-flow slices, typed positions, or returns. It does not define graph semantics or prescribe performed-work order. It helps a practitioner preserve an accepted problem-side claim while selecting and applying the next direct pattern; that pattern, not P2W, produces or amends the governed value.

The PCP-MOD cut keeps one smallest stable practice: preserve the accepted claim for a named receiving use, recover and apply the direct governor, accept its value or honest stop, split independently governed claims, and return only to the smallest affected continuation. Reliance notes, E.18.3 structure, development catalogues, and naming/publication open only for their named uses and do not mutate that core. Relation occurrence, declaration, admission, production, evidence, gate, decision, and other neighbouring doctrine remain owner-side. This cut preserves the predecessor's problem, declaration, method, plan, work, result, evidence, currentness, and return value as separate continuations without reviving its mega-record or burying the first action under apparatus.

### E.18.1:11 - SoTA-Echoing

The sources below are current comparators for specific P2W moves, not authorities imported by reputation. Each row states what changed in the Solution and which overread remains blocked.

The synthesis that combines these moves into one P2W carry-through discipline is an FPF-scoped architectural hypothesis, not established SoTA. The sources support the problem-first, relation-separated, replayable moves named in their rows; they do not establish that P2W is a universal workflow or that one carry-through claim is sufficient for every downstream claim. The hypothesis is limited to an accepted problem-card claim, one named receiving use, and one value governed by its direct pattern; outside that boundary, use the direct pattern, split independently governed claims, or stop.

| Exact source and currentness role | Move adopted in P2W | Overread rejected and practical effect |
|---|---|---|
| Roger Jiao, [*Towards rigorous problem formulation for engineering design research: from motivations to measurable claims via metric-measure-method*](https://doi.org/10.1080/09544828.2026.2633289), *Journal of Engineering Design* 37, 2026. Current engineering-design research comparator for problem-first coherence and method-first failure. | Keep the accepted problem-side claim, characteristic meaning, measurement relation, method, and validation use connected. Select the method only after the practical question and relevant characteristic or measurement relation are recoverable. This source changed the local P2W mantra, compact note, development-loop table, and method-selection stop. | Its Metric-Measure-Method vocabulary is not imported as FPF ontology: FPF recovers characteristic, scale, measurement, and `U.Method` under their direct patterns. Tool availability, fashionable AI, or a ready dataset cannot choose the problem or method. |
| Jenny Zhang et al., [*Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents*](https://arxiv.org/abs/2505.22954), 2025; Nico Pelleriti et al., [*What Do Evolutionary Coding Agents Evolve?*](https://arxiv.org/abs/2605.20086), 2026. A recent open-ended agent-evolution system paper paired with the current diagnostic limitation study. | Preserve generated variants and stepping stones in exact C.18 or C.19 structures; preserve the evaluator, edit history, comparison basis, and replay relation before interpreting a higher score. This source pair changed the development-loop relation table, cooling-module case, replay note, and proxy guard. | Archive membership or best benchmark score does not establish new algorithmic structure, method superiority, performed work outside the run, or subject improvement. Pelleriti et al. show why replay and intervention on search traces are needed to distinguish structural novelty, retuning, recombination, and evaluator overfit. |
| Yoichi Ishibashi, Taro Yano, and Masafumi Oyamada, [*Effective Harness Engineering for Algorithm Discovery with Coding Agents*](https://arxiv.org/abs/2605.15221), 2026. Current harness-design study under fixed budget with explicit evaluation-hack and parallel-execution concerns. | Keep generation method, harness, evaluator, budget, safety boundary, comparison, selected result, and later work as separate governed relations. This source changed the exact direct-relation selection table and the rule that evaluation or gate-looking material remains stopped until its governor is current. | A score produced by an exploitable evaluator or unsafe execution harness cannot carry method selection, evidence, gate passage, or work-entry use. More generated candidates do not substitute for an admissible comparison basis. |
| Haoxiang Qin et al., [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges*](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100, 2026. Current peer-reviewed QD survey comparator. | Keep descriptor space, diversity relation, archive or front, comparator, and selected-set publication distinct. This source changed the development-loop table, AutoML and QD pilot, and selected-set stop condition. | A front or archive is a structured retained set, not a scalar winner, method choice, decision, WorkPlan, or work authorization. Descriptor or distance change reopens only dependent comparison and selection continuations. |
| Sarah Malik and Antonios Kontsos, [*A Digital Thread Approach for Real-Time Defect Correction in Polymer Additive Manufacturing*](https://doi.org/10.32548/2026.me-04580), 2026; Sastry Veluri and Kannan Gopala Krishnan, [*Agentic Digital Thread for Managing the Non-Conformities in Manufacturing of Aerospace Products*](https://doi.org/10.4271/2026-26-0763), 2026. Current manufacturing feedback and proposed agentic digital-thread cases. | Connect sensed defects, process state, design or process correction, quality use, and return through exact relations; preserve the dated work occurrence and reopen only the dependent design, method, planning, or decision continuation. These sources changed the return table, measurement cases, and traceability boundary. | Data continuity, report generation, confidence prediction, or a named digital thread does not itself establish evidence sufficiency, approval, decision, authorization, or completed correction. The aerospace architecture is one proposed domain implementation, not universal P2W ontology. |
| Modelica Association, [*Modelica Language Specification 3.7*](https://specification.modelica.org/), 2026; JuliaHub, [Dyad 3.2 changelog](https://help.juliahub.com/dyad/stable/manual/changelog.html) and [current syntax and analysis documentation](https://help.juliahub.com/dyad/stable/), 2026. Current relation-first multi-domain modeling comparators. | Keep reusable model components and relations, analysis definitions, model compilation, solver or simulation work, and analysis results as separately governed values. This source pair changed the diagram and model-use boundary and supports the exact E.18.3 relation projection. | Acausal model structure or an agent-authored model does not become one execution order, performed simulation, empirical evidence, accepted method, or physical result. A model representation can expose a continuation without supplying its downstream authority. |

As of 2026-07-21, the Jiao article, QD survey, manufacturing digital-thread papers, Modelica 3.7, and Dyad 3.2 documentation are publication or practice anchors. Dyad 3.2 is a minor continuation of the 3.1 foundation with no source-level migration, so the selected component, relation, and analysis distinction remains current. The DGM paper is a recent system result; the 2026 EvoTrace and harness papers are current preprints and carry corresponding uncertainty. Reopen these adoptions when stronger studies change problem-first method selection, distinguish generated structural novelty differently, revise evaluator-hack controls, alter QD archive semantics, or show that digital-thread continuity warrants a stronger use than the exact direct relation currently supports.

### E.18.1:12 - Relations
- `A.22.CGUS` supplies the general constraint-governed unfolding structure when P2W exposes typed structure positions, constraints, admissible next forms, and stop or return conditions.
- `E.18.3` supplies the complete `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` specialization when explicit transformation-flow structure is current; its underlying generic structure, accepted-starting-record references, positions, next-form kinds, and boundary relations remain under `A.22.CGUS`. P2W references those owner records and adds no subset or hybrid structure schema.
- `G.2` governs source-use records, source-pack return, evidence anchors for admitted source publications, and source-currentness payloads before DPF hardening can rely on a seed drawn from those admitted sources.
- `E.4.DPF`, `E.4.PFAD`, and `E.4.PFR` govern DPF authoring, framework architecture decisions, and framework relation records when a generated or cheap seed is carried toward hardening.
- `E.23` governs repeated quality improvement only after the object version and evaluation are recoverable; P2W may carry a seed to that point but does not become the improvement method.
- `G.11` governs currentness, admitted-source decay, source-use relation change, edition change, and refresh when a changed source publication, source-use relation, or telemetry reopens the smallest affected P2W application.

- `E.18` governs selected `TransformationFlowStructure`, transfer annotations, flow valuation, `ConstraintValidity`, `GateFit`, gate profile, design tags, and run tags.
- `C.22.2` governs the accepted problem-side record and problem-side claims related to the carried distinction.
- `A.6.P` governs recovery and readable statement of each direct relation. `A.6.REL` wholly governs direct obtaining, occurrence individuation, and the receiver-conditioned use of any reusable `RelationSignature`; P2W cites the exact owner-returned occurrence, assertion, or description and does not copy that doctrine into note fields. `A.6.RCD`, `E.24`, and `E.24.UK` govern any later P2W relation-kind candidate and admission, while `A.6.0` declares a `RelationSignature` only after that settlement. `F.8` selects the public practice-name decision and the local-only note-form and field-label results; `F.18` governs the practice NameCard and `F.17` publishes only its public term row. This edition introduces no P2W relation species, signature, occurrence, or relation NameCard.
**Canonical object-to-owner map.** Read each arrow independently; the row order is not a declaration or work sequence.

| Current governed object or question | Direct owner and P2W boundary |
|---|---|
| Mathematical-lens use; `FormalSubstrate` or `PrincipleFrame` declaration; ontology or admission | Mathematical-lens use -> `C.29`. Each profile-specific signature -> `A.6.0`. Ontology, predicate-definition, relation-kind, or U-kind question -> direct subject pattern, then `A.6.RCD` only for a residual relation-bearing claim and `E.24`/`E.24.UK` for the exact admission; `A.6.0` opens only after settlement. |
| UTS publication; bridge; measurement; normalization; comparison; parity | UTS publication -> `F.17`; bridge -> `F.9`; measurement -> `C.16`; normalization -> `A.19.UNM`; general comparison -> `A.19.CPM`; parity/benchmark plan or report -> `G.9`. |
| Mechanism; mechanism-method stabilization; method | Mechanism declaration -> `A.6.1`; mechanism-method stabilization -> `E.20`; method -> `A.3.1`. |
| Transformation; temporal aspect; temporal-claim adequacy; dynamics | Actual bounded transformation -> `A.3.4`; temporal aspect -> `C.27.TA`; temporal-claim adequacy -> `C.27`; dynamics episteme -> `A.3.3`. |
| Archive/front or retained exploration value; live-pool policy; selector mechanics; parity comparison; selected-set publication | Archive/front stewardship and retained exploration value -> `C.18`; still-live pool treatment -> `C.19`; selection mechanics -> `A.19.SelectorMechanism`; parity comparison -> `G.9`; selector-facing selected-set publication -> `G.5`. `C.19` does not publish the selected set. |
| Role-method-work alignment; performed work; planning; planned filling; appearance-based work reliance; work-entry readiness | Alignment -> `A.15`; dated work -> `A.15.1`; planning -> `A.15.2`; planned filling/baseline -> `A.15.3`; appearance-based reliance repair -> `A.15.4`; work-entry readiness -> `A.15.5`. Production-work, entity-inception, and completion questions -> `A.15.PROD`; unresolved result/input/handoff wording -> `A.6.P.WMR`; an exact still-missing direct governor -> `A.6.RCD`. |
| Evidence; assurance; provenance | Evidence -> `A.10`; assurance -> `B.3`; provenance -> `G.6`. Each claim keeps its own subject, predicate, and use. |
| Step constraint validity; exact subject or regulatory conformance; FPF pattern-quality review | E.18 step constraint validity -> `A.20`. Another conformance claim -> the direct subject or regulatory owner recovered for that rule and subject. FPF pattern-quality review -> `E.19`. Neither `A.20` nor `E.19` is a universal conformance owner. |
| Gate-decision publication; release act or authorization; work-entry readiness; local choice; accountable commitment | An obtaining gate-decision relation and its publication -> `A.21`. A release-crossing gate decision remains a gate decision, not a release act, authorization, readiness, or performed work; those claims return to their exact direct owner, with work-entry readiness -> `A.15.5`. Local choice result -> `C.11`; an independently current obligation, recommendation-as-duty, prohibition, or other deontic commitment -> `A.2.8`. |
| Architecture; architecture description; structural view; problem-to-structure architecturing; reusable structure | Architecture -> `C.30`; architecture description -> `C.30.AD`; structural view -> `C.30.ASV`; problem-to-structure architecturing -> `C.32.P2S`; reusable structure -> `C.31`. |
| Module interface; function; wording use | Module-interface relation -> `A.6.M`; hidden function-like claim -> `A.6.F`; wording-use repair -> `E.10`. |
| Multi-view publication face or form; publication occurrence and bounded availability use; explanation-faithfulness use; publication work | Multi-view publication face/form -> `E.17`; exact publication occurrence and bounded availability use -> `E.24.PUB`; explanation-faithfulness use -> `E.17.EFP`; rendering, uploading, indexing, or other publication work -> exact `A.15.1` work plus its direct subject relations. Form, carrier, occurrence, work, access, and reliance are different objects or relations. |

### E.18.1:End

