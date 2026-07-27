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

Use this pattern when an accepted `ProblemCard@Context` is ready enough to guide work, but the next FPF use is unsettled. Ask which accepted distinction should shape the next question, which relation and participants that question asserts, and what result or stop is needed before the next action.

The accepted `ProblemCard@Context` is the primary `EntityOfConcern` of any materialized P2W note. Start from one accepted claim and one decision or use that needs it. Then state the relation being asserted, name its participants, and apply the pattern that governs that relation. A separately current `U.Viewpoint` episteme or `BoundedModelUseStructure` may participate in the carry-through claim, but neither becomes an identity field of the ProblemCard or note. Method selection, planning, dated work, actual change, result interpretation, and return remain separate continuations under their direct patterns. P2W introduces no relation kind or occurrence and is neither dated work nor a `U.Transformation`.

Keep three objects separate. The **accepted ProblemCard** is the `EntityOfConcern` of a materialized P2W note. The note is identified under `C.2.1` by its ClaimGraph, that exact card, and its effective `U.ReferenceScheme`; its ClaimGraph names the receiving use and designates a separate viewpoint or model-use structure only when the claim actually uses one. The **subject EntityOfConcern** of each direct pattern is the system, episteme, method, role, work occurrence, relation, or other project entity addressed by that pattern. The **compact note, diagram, plan, trace, and publication** are epistemes or publication-side values that describe, constrain, or make those direct claims inspectable. Later method enactment or dated work can change or preserve a subject EntityOfConcern; improving a P2W note or completing its fields does not establish that subject change, work occurrence, evidence, acceptance, or result.

**Primary reader and question.** The reader already has an accepted `ProblemCard@Context` and must decide one next claim. Ask in ordinary words: **what relation am I asserting, between which participants, and what result would change the next action?** Then apply the pattern that governs that relation. Source wording or a supporting episteme may help formulate the question but does not supply the downstream result.

**So-what adoption test.** Use P2W only when keeping the accepted distinction changes which relation you assert, what result you write, or whether you continue, split, stop, or return. If the relation and result are already settled and P2W would add only another note, skip P2W and apply the direct pattern.

E.11.PUA governs a smaller use and may begin without `ProblemCard@Context`: apply one selected pattern to one current practical question, obtain the first directly typed result, and state its receiving use. E.18.1 begins only when the wider work-facing continuation depends on preserving accepted problem-side material. PUA may support one pattern inspection inside a P2W flow, but it does not replace the accepted-problem carry-through.


#### E.18.1:1.1 - Use this when

- an accepted `ProblemCard@Context` names a working problem and the team needs a disciplined next FPF use toward method, planning, performed work, or result interpretation;
- an invariant, `U.Signature(profile=FormalSubstrate)`, `PrincipleFrame`, mechanism-position, method-position, `A.15.2 U.WorkPlan` or plan-item, performed-work, result-record, or source-currentness cue is present, but the FPF kind or relation to use next is still unsettled;
- a transformation-flow structure, mathematical path relation in a graph-shaped description, flow diagram, principle scheme, scenario, functional description, or source publication helps the team think, while the next FPF use still lacks an FPF kind or relation named by value;
- a result artifact, telemetry line, acceptance record, quality-evaluation record, done-state update, feedback pin, or integration claim needs to be unpacked before it can guide the next FPF use.

#### E.18.1:1.2 - What goes wrong if missed

The team jumps from a convincing problem-side formulation into downstream language without naming the FPF relation being used. The work then looks responsive to the accepted problem, but the next record is unclear, the result phrase becomes too broad, and measurement or source-currentness changes have no honest return relation.

#### E.18.1:1.3 - What this buys

The practitioner gets one concrete next move: keep the accepted claim in view, state the question and participants, apply the pattern that answers it, and use the result it returns. Split several relation claims before applying their patterns. If the relation or needed facts are missing, keep the cue and stop. If a relied-on result changes, reopen only the continuation that used it. Add the compact note only when another person or later action must replay that path. The accepted problem-side distinction remains useful without becoming hidden permission to start work.

#### E.18.1:1.4 - Not this pattern when

- there is no accepted problem-side record; use `C.22.2` or the problem-side pattern named by value first;
- the FPF kind under repair, relation, and record to write are already settled; use that pattern directly and do not add a P2W layer;
- the requested output is a local project procedure, schedule, or work-management method; use the relevant work, planning, method, gate, or operational-management pattern;
- the requested record or claim is an evidence case, assurance case, gate record, decision record, architecture description, publication-use claim, or wording-use repair; use the recovered relation and its governing pattern directly.

### E.18.1:2 - Problem

An accepted problem-side distinction becomes useful when it is ready to guide downstream work or work-planning use. The accepted problem card may expose an invariant, mathematical lens, functional role, mechanism-position candidate, method candidate family, planning constraint, result cue, or changed measurement assumption. Without P2W, that useful distinction is either overcompressed into "we have a solution" or scattered across several related FPF patterns before the working distinction is preserved.

P2W solves a carry-through problem. First say which accepted claim must affect which decision or use. Then write one ordinary relation-specific question, name its participants, apply the pattern that answers it, and keep that pattern's result or stop. Add a compact note only when another person or later action must replay the path. P2W succeeds when the accepted claim, receiving use, concrete question, direct pattern, and result remain inspectable without turning their use-specific connection into a relation kind or treating a note, diagram, plan, trace, or publication as the subject entity or as proof that work occurred.

### E.18.1:3 - Forces

| Force | P2W-preserved content | Pressure to manage |
|---|---|---|
| Problem-side usefulness | An accepted problem-side distinction may guide method, planning, work, or result interpretation. | The distinction is tempting to treat as a completed downstream claim. |
| Governing-kind precision | The reader states one concrete relation question and uses the pattern that governs it; P2W adds no relation species. | A diagram, source phrase, or filled note can look like the relation already obtains. |
| Practical readability | First use needs one recognizable claim, concrete question, direct pattern, result, and next move or stop. | Too much boundary prose or mandatory record apparatus can hide the working P2W application. |
| Non-linear use | P2W may skip, branch, split, stop, or reopen continuations in the carry-through structure. | A readable diagram or graph-shaped expression can be mistaken for a prescribed project sequence. |
| Result usefulness | Result phrases often point to artifacts, telemetry, acceptance, measurement, refresh, or role enactability. | One broad result word can hide several different records. |
| Governing-pattern economy | Direct governing patterns keep their own rules. | Repeating their non-use doctrine inside P2W creates content fanout. |

### E.18.1:4 - Solution

**Local P2W mantra.** The five actions below form the local P2W `mantra`: a short repeatable formulation that keeps this pattern's Solution in attention. The Plain names add memorability, not a new kind or a project-work order.

| Shown continuation | Direct pattern | Solution use | Expected result | Current condition |
|---|---|---|---|---|
| Carry one accepted distinction. | `E.18.1` | Cite the accepted problem-side record, state the one distinction that matters, and say which decision or use needs it. | The accepted distinction and the decision or use it will inform. | The problem-side record is accepted and that decision or use would change if the distinction changed. |
| Ask and recover. | `E.18.1` | State the unsettled practical question, name its participants and relation, and locate the pattern that answers it. | One concrete question, relation, participants, and direct pattern. | A diagram, source phrase, or familiar label has not yet answered the question. |
| Apply the direct pattern. | The pattern recovered in the preceding row. | Apply its Solution while keeping the accepted distinction visible in the concrete method-selection, planning, dated `U.Work`, actual-change, interpretation, or other claim being made. | The result that answers the question, or that pattern's honest stop. | The relation, participants, and direct pattern are recoverable. |
| Continue, branch, or stop. | `E.18.1` | Keep one returned result, split results that answer different relation questions, or retain the cue and stop. | One continuation per answered question, or one explicit stop. | One question, several independent questions, or no answerable relation remains. |
| Return locally after change. | The pattern governing the changed assumption, coordinated through `E.18.1`. | Return only to the smallest earlier P2W continuation affected by the changed assumption, then apply the direct pattern governing that continuation. | A local return with what still carries and what no longer carries stated. | Measurement, source currentness, problem-side content, or another relied-on assumption changed. |

For conformance or pattern-authoring use, the same conditional continuations can also be admitted by `A.22.CGUS` as a `DemonstrativeUnfoldingSlice@Context`; each table row is then one mantra move restored to `DemonstratedPatternUseRow@Context`. This heavier reading is not required for ordinary P2W use, and the local CGUS need not be registered as a separate corpus object.

The decision aid below helps the practitioner choose the one relation question to answer now. Fill a compact carry-through or replay note only when another person or later action must recover the path. The aid shows the accepted claim, concrete question, relation and participants, direct pattern, returned result or stop, and the smallest continuation to reopen after a relied-on result changes.

Choose the first of these three levels that lets the current reader act and any later reader replay the path truthfully:

1. **Ordinary conversational use.** Repeat the local P2W mantra, state one concrete relation question and its participants, apply the direct pattern, use its result or stop, and finish. Write no P2W note when feedback is fast, the use is local, and nobody later needs to replay the path.
2. **Reliance-bearing use.** Add the compact note in `4.1` when transfer, audit, delayed feedback, expensive reversal, automation, or durable reuse depends on recovering the accepted claim and direct continuation.
3. **Structure-bearing use.** Add the exact `E.18.3` structure in `4.0b` only when branches, joins, guards, preserved structure, omitted-structure notes, path slices, or neighboring governed positions matter to the receiving use.

Move upward only when the transfer, audit, delayed-feedback, costly-reversal, automation, durable-reuse, or explicit-structure need in the corresponding row is present. More fields do not improve the subject result and do not substitute for applying the direct pattern.

**What is always needed, and what is optional.** The stable P2W core is only: one accepted problem-side claim; one receiving decision or use; one concrete relation-specific question; one direct pattern per independent claim; the result or honest stop returned by that pattern; a split when several claims are current; and the smallest local return when a relied-on result changes.

| Material | Modularity status | Boundary |
|---|---|---|
| Accepted claim -> receiving use -> concrete question -> direct pattern -> result or stop -> split/local return | **Stable P2W core** | Sections `4.0`, `4.0a`, and `4.2`-`4.7` state this interface without copying the direct pattern's procedure. |
| Compact positive, stop, or replay episteme | **Conditional reliance extension** | Open only for transfer, audit, delayed feedback, costly reversal, automation, or durable reuse; it records the core result and adds no prerequisite to conversational use. |
| Explicit transformation-flow unfolding structure | **Conditional structure extension owned by `A.22.CGUS` / `E.18.3`** | Open only when branches, joins, guards, paths, preserved structure, or stop/return positions matter; P2W supplies no hybrid or shortened structure schema. |
| Development-loop and DPF didactic branches | **Conditional didactic extension** | Open only when cheap generation or a fast DPF seed raises one of the concrete questions in `4.1a` or `4.1b`. Apply the unchanged core to that question and use the Relations map once for an exceptional object; this extension is not a lifecycle, workflow, authority record, or second owner catalogue. |
| Practice naming and publication | **Conditional publication extension owned by `F.8`, `F.18`, and `F.17`** | Open only when a public document, training material, or tool interface must cite the settled E.18.1 practice. Naming adds no core field or result. |
| Relation obtaining, occurrence identity, reusable signatures, admission, production, evidence, gates, decisions, and other neighbouring doctrine | **Handled by the direct pattern, not a P2W extension** | The direct pattern defines the applicable result, assertion, or blocker. P2W cites that result and never copies the pattern's occurrence, derivation, admission, or assurance method. |

No conditional extension may add a mandatory input to ordinary P2W use, change the kind or identity of a result returned by the direct pattern, or mutate the stable core. When an extension is not needed, omit it rather than filling its fields with generic placeholders.


**Assurance scope by use.** For a materialized positive note, check the accepted ProblemCard edition, carried ClaimGraph slice, decision or use that relies on the result, effective ReferenceScheme, returned result kind and ref, direct pattern, and carry-through rationale. Check a separate `U.Viewpoint` episteme or `BoundedModelUseStructure` only when the note's claim designates one. For a stop description, check that no result was fabricated and that the cue and stop are stated. The note is a `C.2.1` episteme about the accepted ProblemCard, not a P2W relation occurrence or `RelationSignature`. For practitioner guidance or conformance, verify that the mantra reaches one result or honest stop without making the note, structure, reader, or checklist perform work. Pattern authoring or review additionally replays the cases, owner boundaries, checklist, and no-new-kind and non-procedural boundaries. None of these checks adds Work, transformation, evidence, gate, or downstream subject facts.

#### E.18.1:4.0 - P2W result without a new relation species

An ordinary P2W application is a practitioner move: preserve one accepted problem-side claim, name the receiving decision or use, ask one concrete question per independent relation, and keep only the result or stop returned by the pattern that governs that relation. This move introduces no `ProblemToWorkCarryThroughRelation@Context`, reusable predicate definition, `RelationSignature`, or P2W relation occurrence.

When transfer, audit, delayed feedback, costly reversal, automation, or durable reuse requires another person or later action to replay the claim, use the `C.2.1` episteme in `4.1`. Its identity is its ClaimGraph, the accepted `ProblemCard@Context` as EntityOfConcern, and the effective `U.ReferenceScheme`. The ClaimGraph records the accepted card edition and carried claim slice, decision or use relying on the result, concrete question, direct pattern, returned result kind and ref or exact stop, and why the carried content remains relevant. It designates a separately identified `U.Viewpoint` episteme or `BoundedModelUseStructure` only when that object participates in the claim; neither becomes another identity discriminator. These are use-specific claim contents, not SlotSpecs of another relation species; the returned result retains its own kind, relation semantics when applicable, identity, and direct pattern.

The conversational, transfer, audit, delayed-feedback, automation, and durable-reuse cases in this pattern need a truthful, replayable claim; none asks whether repeated P2W relation occurrences are the same individual. The conversational move, optional positive note, and stop description therefore close those uses without a relation-kind candidate. `A.6.RCD`, `E.24`, `E.24.UK`, `A.6.0`, and relation-species naming do not open. If a later use asks whether a P2W relation occurrence persists, recurs, ceases, or participates in another relation, reopen `A.6.RCD` and obtain the direct subject settlement and admission before declaring or instantiating such a kind.

A positive use closes only when the accepted card and carried slice remain current for the receiving use, the direct pattern has returned its result for that use, and the rationale remains a truthful claim in the note or is directly recoverable in conversation. A preceding P2W note may be cited for replay, but it supplies neither occurrence continuity nor a supporting relation; any relation among returned values remains governed by its own direct pattern. If these conditions fail, correct the value-kind pair, apply the actual direct pattern, split the claims, or retain a reduced-use cue and stop.

#### E.18.1:4.0a - P2W Declarative Carry-Through Structure

Use P2W as a declarative interface from one accepted `ProblemCard@Context` claim to results or stops returned by direct patterns. P2W preserves the carried claim and receiving use, states the concrete question, cites the selected relation and direct pattern, and keeps each returned result or honest stop on a separate continuation. It owns none of the selected relations or results and does not reproduce how a neighbouring pattern identifies, derives, admits, or evaluates its subject.

The table below is the complete P2W-local decision aid. It asks only what result or blocker the direct pattern returned for this use; it does not copy that pattern's test, derivation, or admission method.

| P2W-local question | Required interface result | P2W disposition |
|---|---|---|
| What accepted problem-side content matters now? | The accepted card edition, carried ClaimGraph slice, and decision or use that will rely on the answer. | Carry only that content. |
| What practical question remains unsettled? | One ordinary relation-specific question that does not presuppose its answer or a new relation kind. | Name the participants, then locate the direct pattern. |
| Which direct relation and pattern govern the answer? | One direct governing pattern per independently governed claim. | Apply that pattern; split when several claims are current. |
| What did the direct pattern return? | The result it defines, a reduced-use cue, or an exact blocker. | Carry that result, keep the cue, or stop; do not copy that pattern's method into P2W. |
| Which continuations remain current? | One or more separate results from their direct patterns, or no continuation. | Keep one continuation per answered question; display order and chronology add no relation. |
| What changed later? | The changed relied-on relation and the smallest dependent continuation. | Reapply its direct pattern and reopen only that continuation. |

When the conditional structure extension opens, `A.22.CGUS` and `E.18.3` supply the admitted structure, typed positions, SlotSpecs, relation references, and stop or return boundaries. P2W adds only its accepted claim, receiving use, one returned result or honest stop, split, and local return; it adds no structure field. Plain actions such as `carry`, `recover`, `write`, `split`, `stop`, and `return` guide use of the method. They are not P2W relation kinds, commitments, permissions, gates, or substitutes for the direct pattern's rules.


#### E.18.1:4.0b - Conditional structure extension through E.18.3

Open this extension only when the reader must show explicit branches, joins, guards, paths, preserved structures, omitted-structure notes, or distinct stop and return positions. `E.18.3` supplies the complete `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` specialization, while `A.22.CGUS` supplies its generic `ConstraintGovernedUnfoldingStructure@Context`, reference relations, typed positions, admissible next forms, and use-boundary relations. E.18.1 declares no P2W subset schema and no hybrid record that mixes fields from those two patterns.

| P2W need in the structure-bearing use | Representation supplied by the direct pattern | P2W boundary |
|---|---|---|
| Cite the accepted starting `ProblemCard@Context` | The underlying A.22.CGUS `acceptedStartingRecordReferenceRefs[]` cites one `UnfoldingStructureReferencedValueRelation@Context` with `referenceKind=acceptedStartingRecord`, exact ProblemCard kind/ref, and `C.22.2` as direct owner. | The accepted card remains a record; it does not become the transformation-flow structure or one of its positions. |
| Expose transformation-flow topology or positions defined by neighbouring patterns | The E.18.3 `transformationPositionRefs[]`, `governingPatternPositionRelationRefs[]`, path or slice refs, and relation-reference epistemes needed by the stated decision or use. | E.18.3 and the direct neighbouring patterns define those values; P2W neither shortens their schemas nor turns display order into project-work order. |
| Preserve the carried claim and why the decision or use needs it | Conversational P2W content or the compact note in `4.1`; if the structure relies on that episteme, cite it through the reference relation supplied by `A.22.CGUS` or `E.18.3`. | No `carriedProblemCardClaimGraph` or receiving-use field is added to the E.18.3 structure. |
| State a stop or the smallest return | E.18.3 `stopBoundaryRef` and `governingPatternReturnBoundaryRefs[]`, backed by the corresponding A.22.CGUS boundary relations. | Stop and return remain distinct boundaries defined by A.22.CGUS and E.18.3; P2W contributes only the local continuation that stops or reopens. |

If explicit structure is not required, use the stable conversational core. If transfer, audit, delayed feedback, costly reversal, automation, or durable reuse requires replay but not structure, use the compact positive note or stop description in `4.1`. If the next question is work-facing, apply the A.15 family before claiming a plan, readiness, launch, or performed `U.Work`. `G.11` handles source currentness; `E.18` handles transformation-flow refresh; P2W reopens only the smallest affected application.

#### E.18.1:4.1 - Compact carry-through note (conditional reliance extension)

Open this extension only when transfer, audit, delayed feedback, expensive reversal, automation, or durable reuse requires someone to replay the stable P2W core. It records a result already returned by a direct pattern or an honest stop; it is not a prerequisite for conversational use and does not widen the core.
```text
ProblemToWorkCarryThroughNote@Context <: U.Episteme:
  claimGraph: U.ClaimGraph by value
  entityOfConcernRef: U.EpistemeRef, referencing one accepted ProblemCard@Context
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
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
  claimGraph: U.ClaimGraph by value
  entityOfConcernRef: U.EpistemeRef, referencing one accepted ProblemCard@Context
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
  editionId
  reducedUseCueDescriptionRef: U.EpistemeRef
  nextPracticalQuestionDescriptionRef: U.EpistemeRef
  stopConditionDescriptionRef: U.EpistemeRef
  returnConditionDescriptionRef?: U.EpistemeRef
```
Use `ProblemToWorkCarryThroughNote@Context` only after the selected direct pattern has returned a positive result for the stated question. Under `C.2.1`, the note is identified by `<claimGraph, entityOfConcernRef, effectiveReferenceSchemeRef>`: its claim content, the accepted ProblemCard as EntityOfConcern, and the effective ReferenceScheme. The ClaimGraph states the decision or use relying on the result, carry-through claim, and rationale. When a separately identified `U.Viewpoint` episteme or `BoundedModelUseStructure` participates in the claim, the ClaimGraph designates it; otherwise no surrogate field is filled. The note, its claim, and its optional predecessor reference are neither a reusable predicate definition nor a P2W relation kind or occurrence. Use `ProblemToWorkStopDescription@Context` when the direct pattern instead returns a blocker or only a reduced-use cue; record that returned reason and stop without fabricating a positive relation. `U.EpistemeRef` is the admissible reference kind for citing either episteme.

A positive note is well formed only when the named result kind is one that the direct pattern actually returns for the stated question, the carried ClaimGraph content remains relevant to the receiving use, and every continuation stays separate. When the result is a relation occurrence, assertion, or description, the note cites that exact object; the direct pattern retains its obtaining or claim basis, occurrence-identity rule, and any receiver-conditioned reusable declaration or typed SlotSpecs. P2W adds no relation-specific field or sufficiency rule. A predecessor note supports replay only and does not establish identity or continuity of another occurrence.

For first-minute use, state the question, apply the direct pattern, and continue with its result or stop. Materialize a `ProblemToWorkCarryThroughNote@Context` only when transfer, audit, delayed feedback, automation, or durable reuse requires replay; materialize a `ProblemToWorkStopDescription@Context` when that replay must preserve a bounded stop. The positive note names the accepted problem card, decision or use relying on the result, next practical question, and direct continuation. The stop description names the accepted problem card, cue, next question, and stop condition. Neither episteme becomes a relation or substitutes for the result produced by the direct pattern.

Each continuation names one direct pattern and one question or use that its result answers. If several continuations are current, write one row for each; do not combine value kind and relation signature, method and mechanism, evidence and assurance, plan and `U.Work`, or refresh and residual triage in one field.

| Compact note field | Filled cooling-fixture example |
|---|---|
| Accepted problem card reference | `ProblemCard@Context PC-FAB-042`, accepted for a cooling-fixture deformation problem. |
| Carried problem-card claim | The deformation is not one more tuning defect; the downstream comparison use relies on preserving the conserved heat-flow structure identified by the problem card. |
| Receiving use | Decide which mathematical-lens result is needed before formal-substrate declaration and method comparison. |
| Next practical question | Which structure is preserved, which is lost, and where does the heat-flow lens stop? |
| Direct governing pattern | `C.29` Mathematical Lens Use. |
| Result written and use it answers | Apply the `C.29` Solution and write its local lens-use result: target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
| Local non-overread | This continuation selects no method, WorkPlan, work occurrence, evidence verdict, or gate result. |
| Stop condition | Stop before method comparison until the comparator, measurement relation, and candidate-set relation are named by value. |
| Return condition | A changed measurement, reference plane, or source-currentness relation returns first to its direct governing pattern and then reopens only the dependent P2W continuation. |

The note closes positively when the direct pattern has returned its positive result and the carried problem-card claim remains visible in that result or its stated basis. It closes by bounded stop when the direct pattern returns a blocker or reduced-use cue and no positive continuation can be stated.

#### E.18.1:4.1a - Conditional development-loop relation-selection extension

Open this didactic extension only when cheap generation, open-ended search, or evolutionary-engineering work has produced many variants before the project has a stable problem, comparison basis, selected set, work entry, or currentness relation. Apply the unchanged P2W core to the one question that changes the next action. The four rows below are discriminators, not an owner catalogue; use the single map in Relations only after the question is stated.

If the current question is still **problem formulation or opportunity**, return first to `C.22.2` to accept or revise the `ProblemCard@Context` and its carried claim. That is an upstream return, not another downstream P2W result.

| Source cue | Ask this concrete question | Continue or stop |
|---|---|---|
| "We generated many variants." | Which variants are actually retained, and under which descriptor or front? | Carry the returned archive/front value. If no retained-set relation is current, keep only the candidate-set cue. |
| "This is the best set." | Is the current claim comparison, selector application, local choice, or publication of a selected set? | Split those claims. Apply only the branch being asserted; a score or front supplies none of the others. |
| "The candidate is ready." | Is the team planning work, checking entry readiness, reporting a dated `U.Work` occurrence, claiming a gate or permission result, or asserting acceptance for one named use? | Name one question and use the Relations map once. For acceptance, name the predicate and its participants; stop if `ready` or `accepted` is the only basis. |
| "We trust the generator." | Does the sentence name an autonomy declaration or boundary—what the generator may do or spend, and when it must stop—or is it about evidence, assurance-sensitive confidence, permitted action, or merely a project label? | For a declared autonomy limit, apply `E.16` and carry its exact declaration or boundary result; that result supplies no evidence, assurance, or permission. Otherwise apply `A.10`, `B.3`, or `A.2.8.PER` only to the one claim actually made. If the phrase is only a label, retain it and make no action claim. |

Cheap variant generation shifts effort toward problem production, characterization, archive stewardship, fair comparison, explicit choice, autonomy boundaries, evidence, assurance, performed work, effect measurement, currentness, and repair. P2W preserves the accepted problem-side claim while one of those relations becomes current; an archive, front, selected set, confidence phrase, or choice rule supplies neither an `A.2.8.PER` permission result nor performed work. Source wording such as `trust budget`, `problem factory`, `solution factory`, or `factory of factories` remains a project label until the evidence, assurance, autonomy, work-organization, or other direct relation is named.

#### E.18.1:4.1b - Conditional development-for-developed first-minute extension

Open this didactic extension only for a fast DPF seed, and keep the source-use and hardening continuations distinct. An accepted problem-side record may cite a `G.2` source-use relation, source `U.EpistemePublication`, source-pack cue or return, and provisional framework purpose. `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, and `G.11` govern their own proposal, review, authoring, evaluation, improvement, and currentness values. P2W preserves the carried claim only until one of those exact relations is selected.

**Cooling-module example.** `ProblemCard@Context PC-DEV-041` states that cheap generation produces many cooling-module layouts while fair problem framing and comparison remain weak. The carried claim is that the current candidate set retains maintainable low-energy variants until energy use, service access, manufacturability, thermal margin, and test cost are represented in the current characteristic and comparison relations. A `C.18` archive and front are current now. `A.19` governs the characteristic space and its comparability boundary; `A.19.CPM` comparison becomes current only when that characteristic space and comparator are current. `G.5` selected-set publication remains stopped until that comparison and front are current. An `E.16` generator boundary may separately bound search and test spending. Prototype observations enter through `A.10`; assurance-sensitive confidence use enters through `B.3`. A `C.30` architecture-candidate relation appears only for retained layouts that change selected structure. `A.15.2` has not yet produced a `U.WorkPlan`, and `A.15.1` has not yet admitted a dated `U.Work` occurrence. Thermal and serviceability measurements can feed but cannot create three separate results: `A.15.5` may return `WorkEntryReadiness@Context` for one named intended-work concern; `A.21` may publish `GateDecision` only for one current `OperationalGate(profile)` and its declared checks; `A.2.8.PER` may return one named non-prohibition, granted-permission, permission-exercise, non-violation, or permission-conflict result with its required participants and basis. An actual release action is an `A.15.1` `U.Work` occurrence; a further claim that a subject was released needs its named subject predicate and participants. No such release predicate is current in this example, so an `approved`, `authorized`, or `released` cue stops as `missing-governor` for that attempted use rather than inheriting the measurement, readiness, or gate result. `G.11` reopens currentness-dependent continuations when descriptors, tests, competitor information, or cited publication editions change.

The current next relation in this example is the `C.18` front record. Architecture comparison, selected-set publication, planning, and work are possible later continuations, not alternative fillers of one field.

#### E.18.1:4.1c - Conditional naming and publication extension

Ordinary P2W use skips this extension. Open it only when a pattern author, publisher, trainer, or tool builder must decide whether a P2W expression may be cited outside its local use. Naming and publication apply only to results already established under their direct patterns; they neither admit a relation kind nor create an episteme instance. The F.8, F.18, and F.17 results refer to the stable practice and add no core field, continuation, or closure condition.

**F.8 decisions.**

| Candidate expression | What is being named and for which use | F.8 result and naming route | Blocked use and reopen condition |
|---|---|---|---|
| `ProblemToWorkCarryThrough` | E.18.1 as one `U.MethodDescription`: the public practice that carries an accepted ProblemCard claim to one result or honest stop returned by a direct pattern | `nameDirectPatternValue`; E.18.1 owns the practice, F.18 owns the NameCard, and F.17 publishes the public row under `FPFCoreReferenceScheme` | Not a relation kind, occurrence, workflow, work, or result; reopen when the practice boundary or public reader use changes |
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
  LocalSense: the E.18.1 practice that carries one accepted ProblemCard claim to one result or honest stop returned by a direct pattern for a stated receiving use
  NameCardRef: NameCard.E18.1.ProblemToWorkCarryThrough.FPFPublic
  LocalSenseBasisRelationRefs: [LocalSenseBasisRelation.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21]
```

`LocalSenseBasisRelation.E18.1.ProblemToWorkCarryThrough.FPFPublic.2026-07-21` relates that SenseCell to basis episteme `E.18.1` as a `U.MethodDescription`, narrowed to units `1-4`, in the same public context. Its description supports the stated practice sense and admits naming-only citation; it admits no relation, workflow, work, result, evidence, authority, or external reuse of the three local note-form labels. No Bridge is current.

#### E.18.1:4.2 - Positive carry-through: one executable first use

Use the first three rows for an ordinary case. Open the fourth only when the source sentence contains the additional claim. Other relation families use the same branch rule in `4.6`; consult the single owner map in Relations only for the relation actually being asserted.

| What the reader has | Do now | Result or stop |
|---|---|---|
| Accepted `ProblemCard@Context PC-FAB-042`: the cooling-fixture deformation is not one more tuning defect because method comparison must preserve a heat-flow invariant. | Carry that distinction into the question: "Which structure does the proposed mathematical lens preserve, which does it lose, and where does its use stop?" | One recognizable receiving question; no method, declaration, plan, or work claim yet. |
| That question names one mathematical-lens relation. | In the Relations map, select `C.29` once and apply its Solution to the cooling-fixture subject and comparison use. | `CoolingFixtureHeatFlowLensUse-042`: preserved structure, lost deformation factors, payoff for method comparison, declared use, and stop. |
| The `C.29` result still carries the accepted heat-flow distinction. | Continue with that value; stop before method comparison until its comparator, candidate set, and measurement basis are current. | A useful positive P2W continuation. No compact note is needed unless another user must replay it. |
| The same source also shows a `FormalSubstrate` signature. | Split the signature claim from the lens-use claim. Apply `A.6.0` only if its governed subject, ranged value, and selected profile can be named. | A separate declaration result, or a stopped declaration cue. The signature neither replaces the `C.29` result nor selects a method. |

This example exercises the ordinary route: one carried distinction, one concrete question, one map lookup, one result from the direct pattern, and one visible stop. A case with several claims splits before any direct pattern is applied; a case with only a cue stops under `4.6`.

#### E.18.1:4.3 - Direct-relation distinctions that change the branch

P2W carries a returned value or stop; it does not restate the neighboring pattern's internal test. Keep a local distinction here only when it changes which branch the reader takes:

- **Lens or declaration?** Ask whether the current use judges a mathematical representation or declares a governed signature. Split the claims when both are present; the first-use case in `4.2` shows the difference.
- **Mechanism or method?** Ask whether the claim states a law-governed operation application or a reusable way of doing. A shared noun supplies neither; split the questions and use the owner map once for each current claim.
- **Change or timing?** Ask whether the claim is one actual bounded change, one temporal aspect such as an interval or cadence, or a judgment that a temporal claim is adequate for use. A timestamp or before/after picture supplies none of those answers; split the questions before continuing.
- **Work, change, or their connection?** Identify the dated `U.Work` occurrence and actual `U.Transformation` separately. Continue with a work-to-change claim only when a named subject predicate with those participants obtains or an `A.6.RCD` disposition-2 local compound claim states the base facts; otherwise return `missing-governor` for the pair. The BuildOps and current Pump 14 slices in `5.1` show positive results; Pump 14 also shows the explicitly earlier stop in a case record that lacks its project declaration.
- **Approved, ready, released, or permitted?** State the intended result before looking it up: gate decision, permission result, work-entry readiness, release `U.Work` occurrence, or a subject release relation. Carry the one result that its pattern returns. If a stronger subject predicate cannot be named, preserve the cue and return `missing-governor`; `authorization` is not a result type.
- **Result or production?** Let `A.6.P.WMR` separate the concrete result claims. Open `A.15.PROD` only for a selected production-work, entity-inception, or production-completion question; its local claim remains separate from work, change, delivery, acceptance, and release.

For every other exceptional object, state the relation-specific question and consult the canonical map in Relations. A label, diagram, note, plan, trace, or familiar noun can trigger that question but cannot answer it.

#### E.18.1:4.4 - Boundary and relation discipline

P2W does not repeat the boundary rules of neighbouring patterns. Its local rule is simple: carry only the accepted problem-side distinction, state the next relation and participants, apply its direct pattern, and continue only with that pattern's result or honest stop. Split several relation claims; if no relation can be stated, retain the cue and stop.

An owner-specific detail appears outside Relations only when one local discriminator in `4.3` or one worked case needs it to choose, split, or stop. Section `4.6` is the plain branch rule; Relations is the only object-to-owner map. Neither place restates a neighbour's occurrence basis, recovery algorithm, production criterion, derivation method, or admission law.

A local P2W application closes positively when the direct pattern has produced or amended its result and the carried distinction remains visible in that result or its stated basis. It closes by bounded stop when no continuing relation can be recovered and the reduced-use cue plus stop condition are stated. A following method selection, planning act, work occurrence, evaluation, or other direct-pattern use is not unfinished P2W work.

A wider P2W carry-through slice remains current only while a named downstream receiving use relies on the accepted problem-side distinction. It closes when no remaining receiving use relies on that distinction and no return condition is current. A later changed assumption opens a new local return to the smallest affected application rather than retroactively keeping every earlier application open.


#### E.18.1:4.5 - Return and refresh rule

Reopen the relation that supplied the changed value, then only the continuation that relied on it. Do not replay the whole carry-through.

| What changed | First return | Smallest P2W reopen |
|---|---|---|
| A measurement, unit, reference plane, normalization, comparator, selected set, criterion, or other result used by the continuation | Reapply the pattern that returned that result. | Reopen only the continuation whose answer used it. |
| A source publication, source-use relation, freshness/currentness line, or appearance on which the use relied | Apply the currentness or reliance repair for that exact source relation, then reapply the affected owner. | Only continuations that relied on the stale or misleading source value. |
| A result artifact, telemetry line, acceptance label, done-state, or similar record | First state the relation that the record is claimed to report; the record's appearance alone is not a changed world fact. | Reopen a dependent continuation only if the result established under that direct pattern changed. |
| The accepted ProblemCard claim itself | Amend or replace the problem-side result under its direct problem pattern. | Every and only continuation that relied on the changed distinction. |

A dated occurrence already admitted as `U.Work` remains the same world-side occurrence. Return may change a later interpretation or plan; it does not rewrite that occurrence retrospectively.

#### E.18.1:4.6 - Plain relation-selection branch

First say the unsettled question as one ordinary sentence: **"Did this work change that pressure here?"**, **"Does this grant let this technician do this work now?"**, or the equally concrete sentence for the current case. Then name the participants and relation that sentence asserts and take one row. Do not scan every pattern first.

| What you can truthfully state | Do next | Close this P2W move with |
|---|---|---|
| One relation-specific question and its participants. | Use the Relations map once, apply that direct pattern, and keep the accepted problem distinction visible. | The result or exact stop defined by that pattern. |
| Two or more relation-specific questions. | Write one question per claim and apply each direct pattern separately. | One result or blocker per question; no omnibus result. |
| Only a cue such as `result`, `approved`, `ready`, a diagram arrow, or a familiar noun. | State the stronger claim the cue seems to suggest. If its relation and participants still cannot be named, preserve the cue and stop. | The cue plus the unanswered relation-specific question; no guessed answer. |
| The governing pattern returns a lower-use result or blocker. | Keep that result intact. | The returned stop or bounded continuation, not a P2W substitute. |
| A relied-on value later changes. | Use `4.5`: reapply its owner and reopen only the dependent continuation. | What still carries, what no longer carries, and the one next question. |

The ordinary case closes after the first row. The canonical owner map is for locating that one pattern or checking an exceptional branch; it is not a checklist to traverse.

#### E.18.1:4.7 - Lowering and reopen block

Lower only the claim that cannot be made. Keep any independently grounded value and preserve the practical question that would reopen the branch.

| Nearest failure | P2W action | Result |
|---|---|---|
| No accepted problem-side record exists. | Stop before P2W; return to the problem-side pattern. | The source phrase remains a cue, not a carried distinction. |
| A cue suggests one relation, but its subject, other participants, or deciding rule cannot be named. | Preserve the cue and the exact attempted question; use the Relations map only to locate a possible owner. | Stop without a positive relation. |
| One sentence blurs several relations—for example lens plus declaration, plan plus Work, or Work plus change. | Split the sentence into separately answerable questions and apply `4.6` to each. | Independent values or blockers; no sequence is inferred. |
| A direct pattern returns `missing-governor`, `missing-information`, a reduced-use result, or another exact blocker. | Carry that result unchanged and stop only the dependent claim. | An honest blocker with its affected participants or use; independently grounded values remain. |
| A relied-on value changed after a prior positive use. | Apply `4.5`. | Reopen only the smallest dependent continuation. |

#### E.18.1:4.8 - Conditional reliance replay after a value from a direct pattern changes

Open this extension only when transfer, audit, delayed feedback, costly reversal, automation, or durable reuse requires a durable account of what still follows after `G.11` source-currentness repair, appearance-based reliance repair, changed measurement, changed problem-side record, FPF pattern change, or a use-found defect. An ordinary local return uses the stable core in `4.5` and creates no replay note.

```text
ProblemToWorkReplayNote@Context <: U.Episteme:
  entityOfConcernRef: U.EpistemeRef, referencing the accepted ProblemCard carried by the original ProblemToWorkCarryThroughNote@Context
  claimGraph: U.ClaimGraph by value
  effectiveReferenceSchemeRef: U.ReferenceSchemeRef
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

`changedValueRef` points to the exact value, occurrence, assertion, or description that changed; `changedValueKindRef` and `changedValueDirectGoverningPatternRef` identify its kind and direct pattern. Reapply that pattern before filling the replay note. If the changed object is a relation, recheck it under that direct pattern and `A.6.REL`. The direct result keeps its participants, obtaining or claim basis, occurrence-identity rule, and any reusable `RelationSignature` or typed SlotSpecs. The replay note records only what still follows, what no longer follows, and which P2W continuation reopens.

P2W may cite a readable relation assertion, an explicitly individuated occurrence, or a typed assertion or description, but it cites the exact object returned by the direct pattern. Citation by P2W does not make relation use signature-dependent; a receiving episteme carries a signature reference only when its own direct pattern requires one.

The changed object may instead be a source edition, measurement, unit, reference plane, method set, comparator, module-interface relation, publication-use relation, problem record, or FPF pattern publication. Whatever changed keeps its own kind and direct pattern. The replay note states which problem-card claims still constrain the downstream use, which no longer do, and the smallest continuation to reopen. Add a `G.11` currentness line only when one exists. The next direct pattern then decides whether to continue, stop, split, retain a reduced-use cue, or return to the problem-side pattern.

### E.18.1:5 - Archetypal Grounding

#### E.18.1:5.0 - Seal-failure carry-through

A maintenance team has an accepted `ProblemCard@Context` for recurrent seal failure. It records the operating conditions, the distinction between thermal deformation and material degradation, and the observations that would challenge that distinction. The team uses E.18.1 because diagnostic-method selection, repair planning, dated repair work, interpretation of the post-repair measurements, and return after a changed diagnosis all depend on preserving these accepted problem-side distinctions.

E.11.PUA may help the team inspect and apply one diagnostic-pattern candidate inside this flow. Its result might be one fit finding or one diagnostic method-selection input. That smaller result does not replace the accepted problem material, the repair plan, the repair work, or the later interpretation and return relations.


`E.18.1` is grounded in a simple System and Episteme contrast. In System-facing work, an accepted problem-side record may lead toward method choice, planning, performed work, result records, and result measurement. In Episteme-facing work, the same record may lead toward a `U.Signature(profile=FormalSubstrate)` declaration, mathematical-lens use, description, publication, evidence, or gate-related claims. The P2W application asks one question in both cases: which FPF kind or relation can carry the next claim being made?

| Archetype | System-side grounding | Episteme-side grounding |
|---|---|---|
| Tell | A manufacturing team accepts a problem card showing that a fabrication issue is caused by a missing functional constraint. | A research team accepts a problem card showing that two descriptions may be almost the same only under a declared `U.Signature(profile=FormalSubstrate)`. |
| Show without P2W | The team treats the principle scheme as method selection, work plan, performed work, and acceptance evidence at once. | The team treats mathematical equivalence as real-world identity, measurement validation, evidence, and decision claim. |
| Show with P2W | The team carries one accepted claim, separates method comparison from `A.15.2 U.WorkPlan` and plan-item records, records references to dated `U.Work` occurrences while keeping those records as separate epistemes, and unpacks result relations; it writes a compact note only when replay matters. | The team separates mathematical-lens use, `U.Signature(profile=FormalSubstrate)`, bridge, measurement, evidence, and provenance relations, and keeps equivalence bounded by the declared formal relation. |

#### E.18.1:5.1 - Worked slices

1. **Thin first-principles start.** An accepted `ProblemCard@Context` says the problem is not one more local tuning task because a conserved structure is being ignored. The practitioner preserves that claim, applies `C.29` for the mathematical-lens question, and carries the returned lens-use value or stop. A separate formal-declaration question opens under `A.6.0` and returns its own declaration result or stop; method selection waits for its own relation and participants.

2. **Planning from selected enough method.** A method family is selected enough for planning. The practitioner applies `A.15.2`; any compact P2W note cites the planning result returned there and the problem-side claim it preserves. The WorkPlan retains its own content and authority.

3. **Performed work after planning; filled positive connection.** **Readable result:** the named build `U.Work` occurrence populated the named artifact-store partition; that occurrence and the store change are connected by the declared BuildOps predicate, not by timing or the word *build*. `A.15.1` grounds `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work`. `A.3.4` separately grounds `ArtifactStorePopulationTransformation_12 : U.Transformation` as the 09:00-09:12 change of `ArtifactStorePartition_12` from no stored `ReleaseBinary_12` to stored `ReleaseBinary_12` under `BuildOpsStoreScheme-v12`. Predicate-definition episteme `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` holds only when that `U.Work` occurrence performs the governed `storeWrite` application that changes the same partition. `BuildApplication_12` supplies that performed application and its `builtBinary -> ReleaseBinary_12` binding, so C.2.1 assertion `BuildWorkPopulatedStore-12` carries the positive local work-to-change claim under `A.6.RCD` disposition 2. P2W keeps the work occurrence, transformation, and assertion separate. If the predicate or one required base fact is absent, this connection stops instead of becoming a universal work-to-change kind.

4. **Result interpretation without generic result.** The sentence *the work result proves the approach worked* does not yet name a result. Ask what can actually be asserted. `A.6.P.WMR` may return a direct subject claim, an `A.6.1` application binding, a local `A.15.PROD` or `A.6.RCD` claim, or a bounded non-assertability result. P2W carries only the returned item. `factually unsupported` and `missing-information` stop an unsupported or underinformed claim; `missing-governor` identifies the absent predicate for the stated participants and use. None becomes a generic result or production value.

5. **Functional explanatory order.** A source diagram places formal declaration, principle framing, mechanism, normalization, method selection, planning, performed work, and result measurement in one readable order. The diagram helps recognize candidate continuations, but P2W carries only values returned by their direct patterns; the display order supplies no sequence or authority.

6. **Interface split before P2W use.** A source says a port-throughput limit makes a solution feasible after integration. The practitioner opens separate `A.6.M` module-interface and `E.18` transformation-flow questions. Planning, work, evidence, gate, function, and architecture cues remain stopped until their relations are asserted. Conversational P2W use or the compact note carries only the direct-pattern result that changes the present decision.

7. **Result measurement returns to planning.** A source says one `U.Work` occurrence produced telemetry and an artifact. First use `A.6.P.WMR` to separate the artifact binding, telemetry claim, and any production or unsupported claim; P2W carries those results on separate continuations. If later `C.16` measurement changes the reference plane used by planning, reapply `C.16` and `G.11`, then reopen only the planning, method-comparison, or problem-side continuation that used that plane. The earlier dated `U.Work` occurrence is not rewritten.

8. **Pump 14 pressure adjustment; governed continuation after an earlier stop.** **Readable result:** the current case record supports `W-P14-ADJUST-1010-1020 caused T-P14-PRESSURE-RISE` under `AdjustmentWorkCausesPressureRise`; P2W carries that returned result rather than inferring it from timing. Exact basis: `PumpTeam-14 : U.System` performs `W-P14-ADJUST-1010-1020 : U.Work` under assignment `RA-P14-ADJUST`, enacts `SetPointAdjustment@PlantOps-v3`, and works in `PumpStation-14` from 10:10 to 10:20 under `A.15.1`. Independently, `A.3.4` returns `T-P14-PRESSURE-RISE : U.Transformation` as the bounded change of continuing `HydraulicLoop_P14`, whose discharge-pressure characteristic changes from `belowBand` to `inBand` over the same interval. Relation-declaration episteme `P14-REL-2026`, owned by `Pump14OperationsRelations`, declares `AdjustmentWorkCausesPressureRise` for those exact participants, and a separate case fact satisfies its actual-causation predicate. In the explicitly earlier case record, `P14-REL-2026` is absent; at that epistemic stage, keep the Work and transformation separate, return `missing-governor: work-to-change claim for <W-P14-ADJUST-1010-1020, T-P14-PRESSURE-RISE>`, and route the missing declaration to `Pump14OperationsRelations`. The separate claim that `PC-P14-PRESSURE` guided `WP-P14-2026-07-15` remains `missing-governor` under A.6.P.WMR; neither the problem claim nor shared timing causes the Work. Later measurement and decision uses remain separate; no production or transformation-composition question opens.


#### E.18.1:5.2 - Additional worked situations

| Situation | P2W application | What changes |
|---|---|---|
| First-minute use | A practitioner has an accepted `ProblemCard@Context` and the sentence "the cooling fixture violates the heat-flow invariant." State the accepted card, carried claim, decision or use needing the answer, and next practical question in conversation. Add a compact note only when another person or later action must replay the path. Then name one direct pattern and the result it must return, or state the stop. | Apply `C.29` to the preserved structure, lost structure, payoff, declared use, and stop condition. A later formal-substrate declaration under `A.6.0` is separate; neither continuation selects a method or writes evidence. |
| Diagram and approval note in the same source publication or source-use record | The same source publication contains a diagram, a test photo, and a manager note saying "approved." Keep P2W focused on the claim carried from the accepted problem card. | Diagram cue, evidence-looking cue, and gate-looking cue are separated by relation recovery; conversational use or the compact note keeps only the carried claim and current direct relation. |
| Principle story without accepted problem-side record | A source has an inspiring principle story but no accepted `ProblemCard@Context`. | P2W stops before it begins; the source remains a reduced-use cue until `C.22.2` or the problem-side pattern named by value accepts a problem-side record. |
| Acceptance claim with and without a governor | For `Fixture-42`, the project-local `ThermalTestAcceptanceRelations` owner governs `acceptedForThermalTest(Fixture-42, CriterionSet-T7, Campaign-T7)`. `CriterionSet-T7` requires leak rate at most `0.5 mL/min` and mounting offset at most `0.2 mm`; current measurements are `0.3 mL/min` and `0.1 mm`, so that predicate is true and P2W carries the exact positive claim. In the earlier dashboard record, only a green `accepted` label exists, the offset was measured from the wrong reference plane, and no acceptance predicate or governor is current. | Apply the direct governor in the positive case. In the earlier case, repair the measurement and return `A.6.RCD missing-governor` for the attempted acceptance claim; the label establishes no acceptance, and `C.25` is not a universal acceptance owner. |
| Changed unit after source-currentness repair | Later source-currentness repair changes only the unit and reference plane used by the planning constraint. | P2W reopens the smallest affected applications; the earlier dated `U.Work` occurrence is cited, not rewritten. |
| Clinical differential carried into care planning | An accepted problem card distinguishes an adverse treatment effect from progression of the underlying condition. Diagnostic-method choice, care planning, performed clinical work, and outcome interpretation all depend on retaining that distinction. | The practitioner applies the clinical DPF and direct work, evidence, and measurement patterns. The problem-side claim does not grant permission to treat; a changed observation reopens the diagnostic continuation before any dependent plan, permission, or work-entry relation. |
| Learning difficulty carried into teaching and assessment | An accepted problem card distinguishes missing recall from a wrong conceptual model. Teaching-method selection, session planning, performed teaching work, and later assessment depend on that distinction. | The selected educational method and A.15 work relations keep their own values. A lesson plan or completed session does not prove changed learner capability; an assessment that challenges the distinction reopens the smallest method or problem continuation. |
| Near-sameness under a formal declaration | A mathematical near-sameness claim preserves heat-flow structure but loses deformation factors outside the model. | The practitioner applies `C.29` for mathematical-lens use. Apply `A.6.0` separately only when the signature's subject, ranged value, and `FormalSubstrate` profile can be named; otherwise keep the signature wording as a stopped cue. P2W preserves the accepted claim across those continuations without settling empirical truth or granting permission to start work. |
| FPF relation rule changes after a P2W use | Reapply that relation's direct pattern and `A.6.REL`. If its result changed and a later continuation relied on it, record the changed result, what still follows, what no longer follows, and the smallest continuation to reopen. | The earlier use is replayed rather than trusted by age; only the changed relation and dependent continuation reopen. |
| Relation selection would over-select from one phrase | A source says "the new port contract proves integration readiness." P2W splits module-interface relation, `E.18` transformation-flow relation, a dated `U.Work` occurrence, evidence cue, gate cue, and architecture-description cue. | Only the relation that changes the P2W application being made is written; the remaining readings stop as named cues until their relations and participants are stated. |
| Formal claim loses payoff | A `U.Signature(profile=FormalSubstrate)` declaration preserves a neat invariant, but no practical payoff or downstream stop condition can be stated for the accepted problem-side record. | The mathematical phrase lowers to a reduced-use cue; P2W does not justify method selection, evidence, gate, or `A.15.2` planning from mathematical prestige alone. |
| Result source-use relation becomes stale | A result-looking source-use relation or publication cue is later replaced by a fresher source-use relation with a different artifact reference and measurement reference. | The practitioner applies `A.15.4` appearance-based reliance repair before continuing P2W; stale result wording cannot continue as evidence, acceptance, or quality evaluation. |

#### E.18.1:5.3 - Pilot examples for coupled transformation-flow slices

These pilots are grounding checks, not source terminology to import. They exercise the same common shape: one current `TransformationFlowStructure` can relate several transformation-flow valuations or slices, one slice may develop or select a usable product, another slice may apply it, and an evaluation or refresh slice may return to the smallest affected development or application slice. The transformation-flow structure does not merge the slice-local objects, `DesignRunTag` boundaries, evidence, gates, work occurrences, or the relation position that the carried object fills inside each slice. Use each pilot to check whether the P2W use being made can name the joined transformation-flow slices, the carried object's slice-local relation position, the `DesignRunTag` boundary, and the smallest reopened slice.

| Pilot | P2W use being made | What it tests |
|---|---|---|
| Coffee service STF | Accepted `ProblemCard@Context PC-COFFEE-SERVICE-17` keeps the service-temperature and throughput problem visible while each next claim opens separately: `C.29` returns `CoffeeHeatMassBalanceLensUse-17`; `A.6.0` returns `CoffeeFormalSubstrateSignature-v3` only for its declared subject and ranged value; `A.6.1` returns the `CoffeeBrewHeatTransferMechanism-v2` declaration and any exact application bindings; `A.19.UNM` returns `CoffeeTemperatureNormalization-v4`; `A.3.1` returns `CoffeeBrewMethod-v5`; `A.15.2` returns `CoffeeShiftPlan-17`; `A.15.1` returns dated `CoffeeBrewWork-17-0815`; `C.16` returns the temperature and throughput measurement results; and `G.11` reopens only the continuation that relies on a changed source, normalization, method, or measurement. | The reader can take any current continuation or stop without treating display order as a declaration stack or project sequence. A signature supplies no mechanism or method; a plan supplies no Work; telemetry supplies no measurement result until `C.16` applies it; refresh changes only the relation that relied on the changed value. |
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
| Result written and use it answers | A C.29 local lens-use result naming target phenomenon, candidate mathematical object, preserved structure, lost structure, payoff, declared use, and stop condition. |
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
| Local stop | No readiness result, granted permission, performed-work claim, evidence verdict, or gate decision follows from the port phrase by itself. |

### E.18.1:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Ontological and epistemic**, **Prag**, **Did**. Scope: **accepted problem-side record plus carried distinction moving toward FPF applications**.

- **Governance bias (Gov):** permission, gate, release, assurance, and decision cues remain local cues until the relation and participants are stated: an `A.2.8.PER` permission result, `A.21 GateDecision`, `A.15.1` release `U.Work` occurrence plus any required named subject release predicate, `B.3` assurance result, or direct decision result. The word `authorization` supplies none of them.
- **Architectural bias (Arch):** diagrams, selected structures, and module-interface language help formulate the next relation question; they do not replace the accepted claim, receiving use, separately governed viewpoint or model-use participant, direct pattern, or returned result.
- **Ontological and epistemic bias:** a source publication, diagram, compact note, or formal declaration remains separate from the subject EntityOfConcern and from the relation or result claimed through its direct pattern.
- **Pragmatic bias (Prag):** the carry-through structure is useful for action without becoming a prescribed project procedure.
- **Didactic bias (Did):** the local P2W mantra and positive carry-through structure come before the heavier relation aids, so precision does not bury the working P2W application.

### E.18.1:7 - Conformance Checklist

- `CC-E18.1-1` The P2W use starts from an accepted `ProblemCard@Context` or stops before P2W begins.
- `CC-E18.1-1a` The accepted ProblemCard as the note's EntityOfConcern, the note's ClaimGraph and effective ReferenceScheme, any separately governed `U.Viewpoint` or `BoundedModelUseStructure` designated by that ClaimGraph, each direct pattern's subject EntityOfConcern, and every supporting compact note, diagram, plan, trace, or publication remain distinct. Note completeness does not prove a P2W relation occurrence, subject change, performed work, evidence, acceptance, or result.
- `CC-E18.1-1b` Every positive `ProblemToWorkCarryThroughNote@Context` identifies one accepted ProblemCard as EntityOfConcern, carries one ClaimGraph for the receiving use, names its effective ReferenceScheme, and designates a separate `U.Viewpoint` episteme or `BoundedModelUseStructure` only when the claim uses one. It cites the carried ProblemCard slice, direct governing pattern, returned value kind and ref, and rationale. It introduces no reusable P2W predicate, `RelationSignature`, relation kind, or occurrence. If the returned value is a relation occurrence, assertion, or description, the note cites that exact object while its direct pattern retains the obtaining or claim basis, occurrence-identity rule, and any reusable declaration required by the receiver.
- `CC-E18.1-1c` When the conditional publication extension is current, the public practice name has an exact F.8 `nameDirectPatternValue` decision, F.18 NameCard, and F.17 row for the already governed E.18.1 method description. The three note-form designators remain E.18.1-local under `reuseLocalSenseLabel`, and schema-position field labels remain `localPhraseOnly`; neither group receives publication apparatus before an external receiver makes durable reuse current. No naming or publication object admits a kind, relation, occurrence, work, evidence, or authority claim or adds a stable-core input.
- `CC-E18.1-2` A materialized positive `ProblemToWorkCarryThroughNote@Context` contains the current use-specific claim and has one or more separate continuation descriptions. A materialized `ProblemToWorkStopDescription@Context` instead states the reduced-use cue and stop without fabricating a relation. Local non-overread and return conditions appear when relied on; absent fields are not filled by generic unions.
- `CC-E18.1-3` The stable core works without a note or explicit structure: accepted claim, receiving use, concrete question, direct pattern, returned result or honest stop, split, and smallest local return. When explicit structure is needed, its generic fields and relations come unchanged from `A.22.CGUS` and its transformation-flow specialization comes unchanged from `E.18.3`; E.18.1 adds no hybrid schema.
- `CC-E18.1-4` One wording span from an admitted source may split into several FPF applications; the record does not compress them into one generic token.
- `CC-E18.1-5` Result wording is unpacked into concrete result-related relations; a generic `WorkResult` kind is not admitted.
- `CC-E18.1-6` `PrincipleFrame` references keep postulates and CHR observability distinct from units, planes, comparators, thresholds, ontology editions, CHR editions, plans, work, evidence, and gates.
- `CC-E18.1-7` Measurement, `G.11` source-currentness relation, reference-plane, method-set, comparator, or problem-side changes return to the smallest affected application.
- `CC-E18.1-8` The stable P2W core contains only accepted claim, receiving use and concrete question, direct pattern, returned result or honest stop, split, and local return. Reliance notes, explicit E.18.3 structure, development examples, and naming or publication are optional extensions. No extension may add a core input or change a returned result. Relation obtaining and identity, occurrence declarations, admission, production, evidence, gates, decisions, and other neighbouring algorithms remain with their direct patterns.
- `CC-E18.1-9` Local boundary wording remains only where it names a near-miss that changes the next P2W application.
- `CC-E18.1-10` The pattern leaves one usable next move: apply the direct pattern and use its result, write a compact note when another person or later action needs replay, split independent claims, keep a cue and stop, or reopen only the continuation affected by a changed relation.
- `CC-E18.1-11` For a structure-bearing conformance or pattern-authoring use, archetypal grounding can replay at least one coupled transformation-flow-slice pilot from `E.18.1:5.3`; the pilot uses one `TransformationFlowStructure` selected under `E.18` while keeping objects, slice-local relation positions, `DesignRunTag` boundaries, and evidence distinct. The self-evolving-spec pilot keeps development-slice evidence or use-found evidence outside the used pattern, specification, or process description. Ordinary P2W use does not open this extension.
- `CC-E18.1-12` Every carried claim family can be lowered, stopped, split, or reopened through `E.18.1:4.7`; a cue from a wording span in an admitted source or from a source-pack cue that cannot name the recovered FPF kind or relation remains a reduced-use cue.
- `CC-E18.1-13` Every materialized replay identifies the changed value, occurrence, assertion, or description; its kind and direct pattern; what still carries and what no longer carries; the smallest reopened continuation; any current `G.11` currentness line; and the next direct pattern. If the changed object is relation-bearing, the cited direct result—not a P2W copy—retains its kind, participants, obtaining or claim basis, occurrence-identity rule, and any receiver-conditioned `RelationSignature` or typed SlotSpecs.
- `CC-E18.1-14` When a generated DPF seed or cheap framework seed enters P2W, the record names the `G.2` source-use record, source `U.EpistemePublication` reference, source-pack cue, or source-pack return when that source use is current, the problem-side cue when that is current, the next governing relation (`G.2`, `E.4.PFAD`, `E.4.PFR`, `E.8`, `E.21`, `E.23`, `G.11`, or another direct governing pattern), and the stop condition that prevents the seed from becoming public authority by generation alone.
- `CC-E18.1-15` An actual-transformation continuation carries only an exact current value or blocker returned by `A.3.4`; E.18.1 does not reconstruct the occurrence basis or infer actuality or composition from a method, plan, model, description, flow position, adjacency, shared work, or common referent.
- `CC-E18.1-16` A work-to-change continuation carries a named subject predicate with its actual `U.Work` and `U.Transformation` participants, a positive `A.6.RCD` disposition-2 local compound claim over governed base facts, or `missing-governor` for that pair. The BuildOps and current Pump 14 replays supply positive branches; Pump 14 also preserves the explicitly earlier `missing-governor` stage in a case record that lacks `P14-REL-2026`. A production continuation separately carries only the local result or blocker returned by `A.15.PROD`. E.18.1 reproduces none of those patterns' internal criteria.



### E.18.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Boundary fanout.** The pattern repeats neighboring algorithms or builds a second owner catalogue. | Keep `4.6` as the plain one/several/no-claim branch, Relations as the only object-to-owner map, and owner details elsewhere only when a local discriminator or worked case changes the reader's action. |
| **Carry-through-as-procedure.** A carry-through structure, diagram, or graph-shaped expression is read as a prescribed project sequence. | Treat it as a way to keep one accepted claim visible across separately answered relation questions. `Stop`, `split`, and `return` guide use of E.18.1; they are not P2W relation kinds or a project-work order. |
| **ProblemCard-as-solution.** The accepted problem card is treated as method, plan, Work, evidence, or result. | State the carried distinction and next question in conversation; add a compact note only when another person or later action needs replay, then apply the direct pattern. |
| **Math-as-authority.** A `U.Signature(profile=FormalSubstrate)` declaration, mathematical lens, or near-sameness does all downstream work. | Apply `C.29` to the preserved structure, lost structure, payoff, declared use, and stop condition. Continue only through the resulting relation; add a P2W note only when another person or later action needs replay. |
| **Generic result token.** The word *result* is treated as one kind, or P2W repeats the whole recovery method. | Ask what can actually be asserted. Apply `A.6.P.WMR`, then carry only the direct subject claim, `A.6.1` application binding, local `A.15.PROD` or `A.6.RCD` claim, or bounded non-assertability result it returns. Keep `factually unsupported`, `missing-information`, and `missing-governor` distinct; only `missing-governor` says that the required predicate for the stated participants and use has no current governor. |
| **Choice-as-commitment.** A `C.11` choice result is treated as an accountable obligation, recommendation-as-duty, or prohibition. | Keep the option set, comparison basis, choice rule, and choice result under `C.11`; open a separate `A.2.8 U.Commitment` only when its accountable subject, modality, referents, scope, and window are independently recoverable. |
| **Plan, path, or proximity as actual change.** A desired state, model, method, plan, flow arrow, adjacent work occurrence, or common affected referent is treated as an actual or composite transformation. | Apply `A.3.4` to the change and the direct work-to-change or `A.15.PROD` pattern to its separate claim. Carry only the results or blockers they return; shared timing or proximity opens no composition or production claim. |
| **Interface shortcut.** Interface, port, protocol, connection, resource, or integration wording selects function, method, work, evidence, gate, or architecture by itself. | Recover the module-interface, signature-slot, function, architecture, work, evidence, or gate relation before continuing. |

### E.18.1:9 - Consequences

| Consequence | Benefit | Cost or mitigation |
|---|---|---|
| A compact carry-through note can be materialized when another person or later action needs replay. | A practitioner can recover how the accepted problem-side claim led to the direct pattern and its result. | Ordinary conversation adds no record; transfer, audit, delayed feedback, costly reversal, automation, or durable reuse pays for the note. |
| Positive carry-through structure comes before boundary. | First use is readable before the heavier relation aid. | Boundary checks are still available in one canonical section. |
| Result language becomes unpackable. | Artifacts, telemetry, acceptance, measurement, refresh, and role enactability can be handled by their own records. | More than one application may be needed for one wording span from an admitted source. |
| P2W stays non-procedural. | The pattern can be used in many project situations without prescribing one local procedure. | A work procedure comes from method material or `A.15.2` planning material outside P2W. |
| Related patterns keep their authority. | P2W avoids duplicating evidence, gate, decision, architecture, publication, mechanism, and work-family doctrine. | Users consult the pattern named by the recovered relation when that relation is being made. |

### E.18.1:10 - Rationale

`E.18.1` is a child of `E.18` because a P2W use may need transformation-flow structure when the accepted claim spans several slices, typed positions, or returns. It does not define graph semantics or prescribe performed-work order. It helps a practitioner keep the accepted claim visible while selecting and applying the next direct pattern; that pattern, not P2W, produces or amends the result.

**Stable core and optional apparatus.** Preserve the accepted claim for one receiving decision or use, ask a concrete relation question, apply the direct pattern, keep its result or honest stop, split independent claims, and return only to the smallest affected continuation. Reliance notes, E.18.3 structure, development examples, and naming or publication open only for their stated uses and do not change that core. Relation occurrence, declaration, admission, production, evidence, gates, decisions, and other neighbouring rules remain in their direct patterns. This separation preserves the predecessor's problem, declaration, method, plan, work, result, evidence, currentness, and return functions without reviving its mega-record or putting apparatus before the first action.

### E.18.1:11 - SoTA-Echoing

The sources below are current comparators for specific P2W moves, not authorities imported by reputation. Each row states what changed in the Solution and which overread remains blocked.

The synthesis that combines these moves into one P2W carry-through discipline is an FPF-scoped architectural hypothesis, not established SoTA. The sources support the problem-first, relation-separated, replayable moves named in their rows; they do not establish that P2W is a universal workflow or that one carry-through claim is sufficient for every downstream claim. The hypothesis is limited to one accepted problem-card claim, one stated decision or use that needs it, and one result or stop from the direct pattern. Outside that boundary, apply the direct pattern, split independent claims, or stop.

| Exact source and currentness role | Move adopted in P2W | Overread rejected and practical effect |
|---|---|---|
| Roger Jiao, [*Towards rigorous problem formulation for engineering design research: from motivations to measurable claims via metric-measure-method*](https://doi.org/10.1080/09544828.2026.2633289), *Journal of Engineering Design* 37, 2026. Current engineering-design research comparator for problem-first coherence and method-first failure. | Keep the accepted problem-side claim, characteristic meaning, measurement relation, method, and validation use connected. Select the method only after the practical question and relevant characteristic or measurement relation are recoverable. This source changed the local P2W mantra, compact note, development-loop table, and method-selection stop. | Its Metric-Measure-Method vocabulary is not imported as FPF ontology: FPF recovers characteristic, scale, measurement, and `U.Method` under their direct patterns. Tool availability, fashionable AI, or a ready dataset cannot choose the problem or method. |
| Jenny Zhang et al., [*Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents*](https://arxiv.org/abs/2505.22954), 2025; Nico Pelleriti et al., [*What Do Evolutionary Coding Agents Evolve?*](https://arxiv.org/abs/2605.20086), 2026. A recent open-ended agent-evolution system paper paired with the current diagnostic limitation study. | Preserve generated variants and stepping stones in exact C.18 or C.19 structures; preserve the evaluator, edit history, comparison basis, and replay relation before interpreting a higher score. This source pair changed the development-loop relation table, cooling-module case, replay note, and proxy guard. | Archive membership or best benchmark score does not establish new algorithmic structure, method superiority, performed work outside the run, or subject improvement. Pelleriti et al. show why replay and intervention on search traces are needed to distinguish structural novelty, retuning, recombination, and evaluator overfit. |
| Yoichi Ishibashi, Taro Yano, and Masafumi Oyamada, [*Effective Harness Engineering for Algorithm Discovery with Coding Agents*](https://arxiv.org/abs/2605.15221), 2026. Current harness-design study under fixed budget with explicit evaluation-hack and parallel-execution concerns. | Keep generation method, harness, evaluator, budget, safety boundary, comparison, selected result, and later work as separate questions under their direct patterns. This source changed the relation-selection table and the rule that an evaluation or gate cue stops until its concrete relation and participants can be stated. | A score produced by an exploitable evaluator or unsafe execution harness cannot carry method selection, evidence, gate passage, or work-entry use. More generated candidates do not substitute for an admissible comparison basis. |
| Haoxiang Qin et al., [*A survey on Quality-Diversity optimization: Approaches, applications, and challenges*](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100, 2026. Current peer-reviewed QD survey comparator. | Keep descriptor space, diversity relation, archive or front, comparator, and selected-set publication distinct. This source changed the development-loop table, AutoML and QD pilot, and selected-set stop condition. | A front or archive is a structured retained set, not a scalar winner, method choice, decision, WorkPlan, or permission to start work. Descriptor or distance change reopens only dependent comparison and selection continuations. |
| Sarah Malik and Antonios Kontsos, [*A Digital Thread Approach for Real-Time Defect Correction in Polymer Additive Manufacturing*](https://doi.org/10.32548/2026.me-04580), 2026; Sastry Veluri and Kannan Gopala Krishnan, [*Agentic Digital Thread for Managing the Non-Conformities in Manufacturing of Aerospace Products*](https://doi.org/10.4271/2026-26-0763), 2026. Current manufacturing feedback and proposed agentic digital-thread cases. | Connect sensed defects, process state, design or process correction, quality use, and return through exact relations; preserve the dated work occurrence and reopen only the dependent design, method, planning, or decision continuation. These sources changed the return table, measurement cases, and traceability boundary. | Data continuity, report generation, confidence prediction, or a named digital thread does not itself establish evidence sufficiency, approval, decision, permission to act, or completed correction. The aerospace architecture is one proposed domain implementation, not universal P2W ontology. |
| Modelica Association, [*Modelica Language Specification 3.7*](https://specification.modelica.org/), 2026; JuliaHub, [Dyad 3.2 changelog](https://help.juliahub.com/dyad/stable/manual/changelog.html) and [current syntax and analysis documentation](https://help.juliahub.com/dyad/stable/), 2026. Current relation-first multi-domain modeling comparators. | Keep reusable model components and relations, analysis definitions, model compilation, solver or simulation work, and analysis results separate under their direct patterns. This source pair changed the diagram and model-use boundary and supports the E.18.3 relation projection. | Acausal model structure or an agent-authored model does not become one execution order, performed simulation, empirical evidence, accepted method, or physical result. A model representation can expose a continuation without supplying its downstream authority. |

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
- `A.6.P` governs recovery and readable statement of each direct relation. `A.6.REL` governs direct obtaining, occurrence individuation, and receiver-conditioned use of any reusable `RelationSignature`; P2W cites the occurrence, assertion, or description returned there and copies none of that doctrine into note fields. `A.6.RCD`, `E.24`, and `E.24.UK` govern any later P2W relation-kind candidate and admission, while `A.6.0` declares a `RelationSignature` only after that settlement. `F.8` selects the public practice-name decision and local-only note-form and field-label results; `F.18` governs the practice NameCard and `F.17` publishes only its public term row. This edition introduces no P2W relation species, signature, occurrence, or relation NameCard.
**Canonical object-to-owner map.** Read each arrow independently; the row order is not a declaration or work sequence.

| Current object or question | Direct pattern and P2W boundary |
|---|---|
| Mathematical-lens use; `FormalSubstrate` or `PrincipleFrame` declaration; ontology or admission | Mathematical-lens use -> `C.29`. Each profile-specific signature -> `A.6.0`. Ontology, predicate-definition, relation-kind, or U-kind question -> direct subject pattern, then `A.6.RCD` only for a residual relation-bearing claim and `E.24`/`E.24.UK` for the exact admission; `A.6.0` opens only after settlement. |
| UTS publication; bridge; characteristic-space construction; measurement; subject-specific evaluation; normalization; comparison; parity | UTS publication -> `F.17`; bridge -> `F.9`; exact `U.CharacteristicSpace`, characteristic slots, scales, value sets, and comparability boundary -> `A.19`. Measurement -> `C.16`, which returns one exact `U.Measure` reading: a claim or recorded reading that cites one `U.DHCMethodRef`, identifies its bearer, states a coordinate or level valid on that template's scale, carries its time stance, and includes the `U.EvidenceStub` required by the template. The referenced `U.DHCMethod` binds the characteristic and scale, plus unit and polarity where applicable; it is a measurement template, not measurement-procedure Work, and the stub points to grounds without becoming the evidence or those grounds. A subject-specific evaluation claim or use separately names its predicate, participants, criterion, and direct subject pattern. Measurement and evidence alone establish no evaluation verdict, downstream permission, readiness, gate, or decision. Normalization -> `A.19.UNM`; general comparison -> `A.19.CPM`; parity/benchmark plan or report -> `G.9`. |
| Mechanism; mechanism-method stabilization; method | Mechanism declaration -> `A.6.1`; mechanism-method stabilization -> `E.20`; method -> `A.3.1`. |
| Transformation; temporal aspect; temporal-claim adequacy; dynamics | Actual bounded transformation -> `A.3.4`; temporal aspect -> `C.27.TA`; temporal-claim adequacy -> `C.27`; dynamics episteme -> `A.3.3`. |
| Archive/front or retained exploration value; live-pool policy; selector mechanics; parity comparison; selected-set publication | Archive/front stewardship and retained exploration value -> `C.18`; still-live pool treatment -> `C.19`; selection mechanics -> `A.19.SelectorMechanism`; parity comparison -> `G.9`; selector-facing selected-set publication -> `G.5`. `C.19` does not publish the selected set. |
| Role-method-work alignment; performed work; planning; planned filling; appearance-based work reliance; work-entry readiness; work-to-change | Alignment -> `A.15`; dated work -> `A.15.1`; planning -> `A.15.2`; planned filling/baseline -> `A.15.3`; appearance-based reliance repair -> `A.15.4`; work-entry readiness -> `A.15.5`. A work-to-change claim -> its named subject predicate with `U.Work` and `U.Transformation` participants, or one local compound claim under `A.6.RCD` disposition 2; absent either basis -> exact `missing-governor`. Production-work, entity-inception, and completion questions -> `A.15.PROD`; unresolved result/input/handoff wording -> `A.6.P.WMR`. |
| Generator-autonomy declaration or boundary; evidence; assurance; provenance | Generator-autonomy declaration or bounded-autonomy question -> `E.16`; evidence -> `A.10`; assurance -> `B.3`; provenance -> `G.6`. An autonomy declaration states the limits and stop conditions it governs; it supplies none of evidence, assurance, permission, or performed Work. Each claim keeps its own subject, predicate, and use. |
| Acceptance record, label, or claimed acceptance | First name the exact acceptance predicate, its participants, and the receiving use, then apply that predicate's direct governor and carry only the result it returns. If no such predicate or governor is current, return exact `A.6.RCD missing-governor` for those participants and that use. A record or label alone does not establish acceptance; `C.25` is not a universal acceptance owner. |
| Step constraint validity; exact subject or regulatory conformance; FPF pattern-quality review | E.18 step constraint validity -> `A.20`. Another conformance claim -> the direct subject or regulatory owner recovered for that rule and subject. FPF pattern-quality review -> `E.19`. Neither `A.20` nor `E.19` is a universal conformance owner. |
| Gate decision; permission; release; work-entry readiness; local choice; accountable commitment | Gate-decision relation and publication -> `A.21`. Non-prohibition, granted permission, permission exercise, non-violation, or permission conflict -> `A.2.8.PER`; instituting or revoking grant act -> `A.2.9`; obligation or prohibition -> `A.2.8`. Release action -> exact `A.15.1` `U.Work` occurrence; a claim that a subject was released -> its named subject predicate and participants or `A.6.RCD missing-governor`. Work-entry readiness -> `A.15.5`. Local choice -> `C.11`. Gate, permission, readiness, release work occurrence, release relation, choice, and commitment do not entail one another. |
| Architecture; architecture description; structural view; problem-to-structure architecturing; reusable structure; cross-scope or interlevel residual | Architecture -> `C.30`; architecture description -> `C.30.AD`; structural view -> `C.30.ASV`; problem-to-structure architecturing -> `C.32.P2S`; reusable structure -> `C.31`; cross-scope or interlevel residual -> `C.30.ILC`. |
| Module interface; function; wording use | Module-interface relation -> `A.6.M`; hidden function-like claim -> `A.6.F`; wording-use repair -> `E.10`. |
| Multi-view publication face or form; publication occurrence and bounded availability use; explanation-faithfulness use; publication work | Multi-view publication face/form -> `E.17`; exact publication occurrence and bounded availability use -> `E.24.PUB`; explanation-faithfulness use -> `E.17.EFP`; rendering, uploading, indexing, or other publication work -> exact `A.15.1` work plus its direct subject relations. Form, carrier, occurrence, work, access, and reliance are different objects or relations. |

### E.18.1:End

