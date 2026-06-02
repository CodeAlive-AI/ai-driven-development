## E.23 - Quality Improvement Loop Method

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### E.23:1 - Problem frame

Use `E.23` when the working question is: "how do we improve this?" The object under improvement can be a chair, component, subsystem, nuclear-plant safety case, policy, method, architecture description, benchmark result, declared transduction result, FPF pattern, `DRR`, corpus slice, or another exact object. `E.23` is the entry pattern for repeated improvement, but it does not say what "better" means by itself: the loop starts only after the object version and the object-under-improvement evaluation for that object are declared. If the object has no adequate object-under-improvement evaluation yet, construct or repair the object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS` before opening the loop.

The governed object is the repeated quality-improvement method parameterized by `<ObjectVersionUnderImprovement, ObjectUnderImprovementEvaluationRef>`. The loop does not supply quality values or construct coordinate sets. It changes the object under improvement, asks the object-under-improvement evaluation to re-read the changed object version, and decides whether to stop, narrow, continue, switch method, or hold for more exact information.

Use it especially when the work is more than a cheap admissibility read:

- an already admissible object under improvement is being improved toward exceptional expression;
- returned findings must be absorbed row by row and then re-read for actual quality movement;
- one `E.22` read returns a bounded portfolio of candidate improvement proposals, and the loop must choose, apply, re-read, or hand off those proposals without pretending the read already selected a winner;
- a proposed improvement may raise visible coordinates while damaging usability, affordability, repair locality, corpus ecology, neighbour fit, source-content preservation, or another protected quality;
- an agentic or tool-using loop is being considered and its cost, supervision, retry, memory, verification, or stop posture matters;
- a specialized improvement cycle, such as throughput, variation, learning, stabilization, or orientation under uncertainty, is being selected for one declared characteristic space.

**Not this pattern when.** Use `E.22` alone for one framed `floorRead` or other single quality review when no repeated improvement method is needed. Use the object-under-improvement evaluation itself when the question is already scoped and the work is a direct value read. Use `A.19.ECS` when the live problem is constructing or repairing the object-under-improvement evaluation `CharacteristicSpace` for the object under improvement. Use `C.16.Q` when the live problem is overloaded `quality` wording. Use `C.25` when the live problem is a composite engineering quality-family endpoint. Use project-side evidence, assurance, gate, work, release, safety, or compliance patterns when the result is being reused for those exact claims.

**First useful move.** Name the exact object version under improvement and the object-under-improvement evaluation before changing anything. If the evaluation is missing or not adequate for the object kind and use, construct or repair it through `A.19.ECS` first. Then state the improvement aim, floor, protected trade-offs, selected quality-read purpose, and the condition under which the next pass would stop, narrow, continue, switch method, or hold.

**Cheap stop.** If one `E.22` short-form `floorRead` under the object-under-improvement evaluation gives an admissible stop and no repeated improvement aim is live, do not open `E.23`.

**What goes wrong if missed.** A team counts closed checklist rows as quality improvement. An agent retries because it can, not because the object-under-improvement evaluation moved. A `DRR` becomes longer but not more decision-bearing. A pattern gets more machinery while first use becomes harder. A specialized cycle is used because it is familiar, even though the declared characteristic space does not fit it. An OEE/NQD run changes candidates without saying which `Q` movement it seeks relative to the current comparison set or front.

**What this buys.** `E.23` gives any improvement effort a disciplined shape: choose the object, declare the object-under-improvement evaluation that says what improvement means, change the object, re-read it, inspect trade-offs, justify added operation families, and stop or switch when the declared values, trade-offs, and costs no longer make another pass admissible.

**Governed object in plain terms.** The governed object is a repeated method for improving one exact object under improvement under the object-under-improvement evaluation that supplies values for that object under improvement.

**Primary working reader.** The first reader is the person running or supervising a repeated improvement pass. The downstream reader is the reviewer, steward, engineer, author, or maintainer who must judge whether the changed object version actually improved under the declared evaluation.

### E.23:2 - Problem

Improvement work often borrows loop language without saying what is being improved, which evaluation supplies the values, or what would make another pass worth its cost.

The recurring failures are:

1. **Value invention by loop.** The method starts scoring "quality" without naming the object-under-improvement evaluation that supplies quality values.
2. **Discharge-count substitution.** Row closure, checklist closure, or issue-count reduction is treated as quality movement before the changed object version is re-read.
3. **Unbounded retry.** An agent, reviewer, or author keeps iterating because more attempts are possible, not because a live quality movement remains feasible.
4. **Cheap-read overloading.** A simple floor check becomes a heavy improvement apparatus.
5. **Goodharted improvement.** Visible coordinates rise while protected trade-offs get worse.
6. **Method-family mismatch.** A PDCA or PDSA, POOGI, OODA, Ralph-like, variation-reduction, NQD quality-side improvement, or other specialized cycle is applied outside the characteristic space it was built to improve.
7. **Neighbour theft.** The loop silently absorbs `E.22` question framing, `E.21` pattern-quality values, `E.9.DA` `DRR` adequacy values, `C.25` Q-Bundle endpoints, `C.16.Q` term repair, `C.19.1` method-preference discipline, `C.22.1` adaptation signatures, or `C.24` call planning.
8. **NQD quality-side capture.** The loop uses the `Q` side of NQD to improve one candidate, then silently starts governing novelty, diversity, descriptor or distance definitions, archive or front insertion, pool policy, selected-set publication, parity, or refresh.
9. **Administrative-state quality.** Landing, review praise, external-review completion, popularity, adoption, or absence of blockers is used as evidence of improved quality by itself.

### E.23:3 - Forces

| Force | Tension |
|---|---|
| **Improvement ambition vs first-use cost** | Exceptional improvement may be worthwhile, but ordinary floor reads must remain cheap. |
| **General adaptive methods vs specialized cycles** | Broad agentic methods can scale, while object-family cycles can be cheaper and more reliable when the characteristic space fits. |
| **Feedback use vs self-confirming retry** | Feedback can improve the next pass, but agent or author self-assessment cannot replace object-under-improvement evaluation re-read. |
| **Operation hardening vs bureaucracy** | Specification articulation, decomposition, memory, verification, supervision, or search breadth can help, but each added operation must justify its cost and stop condition. |
| **Visible improvement vs protected trade-offs** | A change can improve one coordinate while worsening affordability, usability, locality, neighbour fit, source preservation, or corpus ecology. |
| **Proposal portfolio vs selector overread** | A useful read may return several improvement proposals, but choosing candidates for generation, front or archive retention, selected-set publication, parity, or refresh belongs to the OEE/NQD neighbours. |
| **Reusable method vs neighbour authority** | `E.23` needs one reusable improvement method while keeping value reads, quality bundles, precision restoration, adaptation signatures, and tool-call planning in their governing patterns. |

### E.23:4 - Solution

Run a `QualityImprovementLoopMethod` only after naming the exact `ObjectVersionUnderImprovement` and the `ObjectUnderImprovementEvaluationRef` that supplies values and stop meanings.

`QualityImprovementLoopMethod := <ObjectUnderImprovementRef, ObjectUnderImprovementEvaluationRef, ImprovementAim, DeclaredFloor?, TradeoffProtectionSet, QualityReadQuestionFrameRef, MethodFamilySelection, OperationFamilySelectionSet?, QualityReviewFindingRows?, ChangedObjectVersionRef?, ObjectUnderImprovementEvaluationReRead, CostAndRiskPosture, StopNarrowContinueSwitchHoldDecision>`

`ObjectUnderImprovementRef` is a local field for the exact object kind and exact version under the object-under-improvement evaluation. It does not mint a broad new kernel kind.

Admissible object forms include one pattern version, one `DRR` version, episteme publication, architecture description, method description, policy text, benchmark result, declared transduction result, or another exact object kind named by the object-under-improvement evaluation. The object under improvement is not a file bundle, task list, campaign, chat, review packet, source collection, or vague produced thing unless the object-under-improvement evaluation explicitly reads that object kind.

When the object under improvement is a transduction result, the loop also names the producing transduction or `E.18` graph, path, crossing, or flow-valuation context when that context is live; the exact result kind; the object version under improvement; and the object-under-improvement evaluation. The system carrier or rendering of the result is not the object under improvement unless the object-under-improvement evaluation explicitly reads that system carrier or rendering kind.

When the object-under-improvement evaluation also supplies the `Q` side of an NQD or OEE comparison, `E.23` may govern repeated changes to one candidate, object version under improvement, or declared transduction result so that its `Q` position moves relative to a declared comparison set, external candidate set, current non-dominated front, competing candidate set, `SoTA` line, or selected set. `E.23` does not govern novelty, diversity, descriptor or distance definitions, generation, front or archive insertion, candidate-pool policy, selected-set publication, parity, or refresh semantics.

#### E.23:4.1 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement method for one object under improvement under one object-under-improvement evaluation. | Not a universal work sequence, not project management, not a process script, and not proof of quality by itself. |
| `ObjectUnderImprovementRef` | Exact object kind and exact version under improvement. | Not a source bundle, campaign, chat, task list, review packet, source collection, or generic produced thing unless the object-under-improvement evaluation reads that object kind. |
| `ObjectUnderImprovementEvaluationRef` | Pattern, object-under-improvement evaluation `CharacteristicSpace`, Q-Bundle, rubric, review profile, or local evaluation that supplies values and stop meanings. | Not an opinion, prompt, checklist count, coordinate set, or score sheet invented by `E.23`; construct missing object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS`. |
| `ImprovementAim` | Declared desired movement under the object-under-improvement evaluation: floor repair, exceptional improvement, trade-off inspection, absorption impact, open-question discovery, or another exact object-under-improvement evaluation aim. | Not permission to optimize visible values while damaging protected qualities. |
| `MethodFamilySelection` | Selected method family for the current object under improvement: general adaptive loop, specialized cycle, or mixed operation-family set. | Not a universal ladder, maturity level, or new kernel kind. |
| `OperationFamilySelectionSet` | Optional operation families selected because they can move the object-under-improvement evaluation enough to justify their cost and risk. | Not mandatory apparatus for every loop. |
| `ObjectUnderImprovementEvaluationReRead` | Re-run or cited result from the object-under-improvement evaluation on the changed object version under improvement. | Not executor self-assessment, reviewer praise, discharge count, or absence of blockers. |
| `CostAndRiskPosture` | Declared cost and risk account used to judge whether the next pass or added operation is worth doing. | Not a scalar quality value and not resource ontology. |
| `StopNarrowContinueSwitchHoldDecision` | The local decision after a re-read: stop, narrow the aim, continue, switch method family, or hold for more exact information. | Not a release gate, work authority, safety acceptance, or evidence claim by itself. |
| `QualityImprovementLoopRecord` | Local record of one loop pass or pass sequence: object version under improvement, object-under-improvement evaluation, applied rows, re-read result, trade-offs, cost and risk posture, and stop decision. | Not proof of quality by itself and not a project release, gate, evidence, assurance, safety, compliance, or work-authority record. |
| `QualitySideMovementClaim` | Local claim that the changed object version moved on declared `Q` components under one NQD/OEE comparison. | Not an `N` or `D` claim, not archive or front insertion, not candidate-pool policy, not selected-set publication, not parity, and not refresh. |
| `SourceContributionStratum` | One distinguishable contribution type made by an accepted source or practice line inside a source-bearing improvement: value semantics, operation family, boundary, comparison discipline, failure mode, protected trade-off, or stop discipline. | Not a maturity level, not an architecture layer, not evidence rank, and not permission to cite a source without saying what it contributes. |
| `SourceComposedResultClaim` | The changed object version capability, move, explanation, method result, or other object-under-improvement evaluation-readable result produced by composing accepted source or practice lines. | Not a mathematical function, not a TGA morphism, not a module function, not source volume, and not a novelty claim without object-under-improvement evaluation re-read. |


The words `loop`, `method family`, and `operation family` are local method words. They do not create a sequence that every project must run. They name repeated use of an object-under-improvement evaluation-controlled improvement method.

#### E.23:4.2 - Relationship to E.22, A.19.ECS, and object-under-improvement evaluations

`E.23` is one loop method, not a separate cycle for each object kind. Different applications are object-under-improvement-specific loop instances: they differ by `ObjectUnderImprovementRef`, object-under-improvement evaluation, active coordinates, protected trade-offs, stop meanings, and neighbour exits. A product-design instance, safety-case instance, pattern-version instance, `DRR` instance, NQD candidate instance, architecture-description instance, or corpus-adequacy instance uses the same method only after the declared object kind and object-under-improvement evaluation are named. `E.23` does not turn those differences into holon levels, maturity ladders, or a decision-composition algebra.

The parameter pair is simple: name the object version under improvement, then name the evaluation that supplies the values for that object. Examples:

- a physical product, engineering design, policy text, method description, safety-case argument, or other domain object under improvement uses a declared object-under-improvement evaluation `CharacteristicSpace`, Q-Bundle, rubric, review profile, or assurance-adjacent evaluation pattern that supplies those values;
- an FPF pattern version uses `E.21`;
- a `DRR` version uses `E.9.DA`;
- an FPF-corpus or whole-FPF Pillar-adequacy object under improvement uses `E.2.DA`;
- a durable naming object under improvement uses `F.18`;
- an engineering quality-family object under improvement may use `C.25` as the Q-Bundle endpoint;
- an NQD/OEE object under improvement uses the declared `Q` side or the governing OEE/NQD neighbour.

If no adequate object-under-improvement evaluation exists for the object under improvement, `A.19.ECS` is opened before `E.23`. `A.19.ECS` constructs or repairs the object-under-improvement evaluation `CharacteristicSpace`: object kind, declared use, contrast cases, coordinate set, scales, value meanings, evidence and missingness rules, protected trade-offs, status meanings, and stop or reopen condition. `E.23` starts only after that evaluation is recoverable enough to re-read a changed object version.

For NQD/OEE use, the object-under-improvement evaluation can be the declared `Q` side of `C.18` or a governing OEE/NQD neighbour. `E.23` then asks whether object changes produce expected `Q` movement relative to the current comparison set, external candidate set, current non-dominated front, competing candidate set, accepted `SoTA` line, or selected set named by that object-under-improvement evaluation. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` still govern candidate characteristics, novelty and diversity treatment, descriptor and distance definitions, archive and front semantics, pool policy, selected-set publication, parity, and refresh.

`E.23` does not define the coordinates, floors, values, dominance rules, or measuring instruments. If no object-under-improvement evaluation is declared, the loop cannot start as a quality-improvement loop. First repair the question through `E.22`, repair overloaded quality wording through `C.16.Q`, construct or repair the object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS`, or select an existing exact object-under-improvement evaluation.

#### E.23:4.3 - Work order for using this pattern

For one quality-improvement loop:

1. Declare the object version under improvement and object-under-improvement evaluation; if no adequate object-under-improvement evaluation exists, use `A.19.ECS` before opening this loop.
2. Declare the improvement aim, floor, protected trade-offs, and first stop condition.
3. Frame the first quality review through `E.22`.
4. Run the object-under-improvement evaluation and produce row-atomic findings when work is returned.
5. Apply repairs or variants to the object under improvement, or hand proposal generation and selection to an exact neighbour, without silently damaging protected trade-offs.
6. Record executor discharge as changed-object evidence, not as the quality value.
7. Re-read the changed object version through the object-under-improvement evaluation rather than accepting executor self-assessment. When `Q`-side NQD comparison is live, read the changed object version against the declared comparison set or front named in the loop record.
8. Record what got worse, including reader cost, authoring cost, maintainer cost, neighbour-pattern cost, source-loss risk, corpus-ecology cost, supervision cost, or rework cost when those can change admissible use.
9. Decide `stop`, `narrow`, `continue`, `switchMethodFamily`, or `holdForExactInformation`.
10. Leave one `QualityImprovementLoopRecord` that lets a later reader recover the object version under improvement, object-under-improvement evaluation, applied rows, re-read result, changed trade-offs, cost and risk posture, and stop decision without reconstructing chat memory.

If the next pass has no live findings, feasible non-dominated improvement, required trade-off inspection, or unresolved open question under the declared object-under-improvement evaluation, stop or narrow. Do not continue merely because more attempts are possible.

An all-`5` or all-exceptional claim requires an explicit object-under-improvement evaluation coordinate-value table over the changed object version. It cannot be inferred from a floor-pass capsule, clean discharge table, external-review absorption pass, landing, popularity, adoption, or absence of blockers.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result is a local stop condition, not a permanent maturity end. It closes this loop only under the named object version under improvement, object-under-improvement evaluation, declared `Q` components, externally declared comparison set or current front, protected trade-offs, and cost boundary. Development can reopen when a new use, comparison set, front, archive, `Q` component, source, `SoTA` line, affordability boundary, or higher-payoff proposal changes the object-under-improvement evaluation. Do not encode the stop as a maturity level or as proof that further improvement is impossible.

When the object-under-improvement evaluation uses an ordinal scale, the declared floor is the local viable-for-use threshold under the named use claim; it is not always the same ordinal value. The object-under-improvement evaluation supplies the floor rules for that evaluation. A highest value means exceptional expression for the declared use and can serve as current-front reach or front improvement for this loop only when the object-under-improvement evaluation names the comparison basis: accepted `SoTA`, competing candidates, prior front members, current practice, or another explicit declared use frontier. It is not an upper bound on future development and not self-assigned praise.

For source-bearing improvement work, accepted `SoTA` is treated as the working external front: it shows what currently works for the governed problem at the time of the read. `SoTA` is assigned from outside the loop by the object-under-improvement evaluation, accepted source posture, or declared comparison set. `E.23` can govern a loop that reaches that front, holds the object under improvement near that front as sources change, or tests a front-improving proposal, but it does not assign `SoTA` to itself or to the object under improvement.

Source-bearing improvement is compositional. PDSA or PDCA, POOGI, OODA, Ralph-like loops, SkillOpt-like fixed-performer optimization, MCDA, Goodhart, and NQD/OEE lines are not a citation shelf. Each line contributes one operation family, boundary, value semantic, stop discipline, or comparison discipline. A conforming loop keeps those contribution strata distinguishable enough that an object-under-improvement evaluation read can recover which contribution caused which useful movement and which neighbouring pattern still governs each boundary.

The entry vocabulary may say all `5`s, exceptional, `SoTA`, Pareto front, NQD `Q` movement, proposal portfolio, or shortlist. `E.23` accepts that vocabulary only after `E.22` or the object-under-improvement evaluation has named the governing pattern. In this pattern the shared operational question is simple: which object version under improvement is being changed, which externally declared comparison or value space reads the change, what movement is expected, what trade-off must not worsen, and what local stop or neighbour exit follows?

#### E.23:4.4 - Method-family selection

The generalization is not another named loop. It is a typed improvement method over one declared object under improvement, one exact version, and one declared object-under-improvement evaluation. Improvement is multi-characteristic optimization by changing the object under improvement and accepting only non-dominated gains or explicitly justified trade-offs under the object-under-improvement evaluation.

| Method family | Characteristic-space fit | Boundary |
|---|---|---|
| `PDSAorPDCAFamily` | Learning quality, measurement-backed comparison, stable baseline, standardize-or-repeat action. | Use when the object-under-improvement evaluation has declared measuring instruments or comparable read coordinates; do not reduce improvement to completing four labels. |
| `POOGIFamily` | Throughput, constraint selection for work, system throughput relation, inertia after a constraint shifts. | Use when the quality problem is actually throughput-shaped or constraint-shaped; do not force TOC constraint language onto every object under improvement. |
| `OODAFamily` | Orientation, feedback, decision under uncertainty, changing external situation. | Use when orientation quality and feedback materially change the object read; do not count speed or action cadence as quality. |
| `RalphLikeGeneralAdaptiveFamily` | Broadly capable agent repeatedly works from specification, failure feedback, memory, and verification. | Use only under `C.19.1` cost and risk discipline, supervision boundary where needed, object-under-improvement evaluation re-read, and stop or switch conditions. |
| `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` | Performer, harness, or execution environment stays fixed while a mutable object version under improvement is improved through bounded edits and object-under-improvement evaluation re-read. | Use when the loop changes the object under improvement rather than the performer. If the live work changes candidate generation, archive or front semantics, live pool policy, selected-set publication, parity, or refresh, hand off to `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`. |
| `NQDQualitySideImprovementFamily` | The object-under-improvement evaluation supplies the `Q` side for a declared NQD/OEE comparison, and loop changes seek non-dominated `Q` movement for one candidate, object version under improvement, or declared transduction result. | Use only with declared `Q` components, external comparison basis, comparison set or current front, protected trade-offs, and neighbour exits. A front-improving proposal must name the externally assigned front and the declared result or capability it is expected to improve. `E.23` does not govern novelty, diversity, descriptors, distances, archive or front insertion, pool policy, selected-set publication, parity, or refresh. |
| `SoTAReachAndMaintainFamily` | Several accepted source or practice lines must be composed so the object under improvement reaches or maintains an externally assigned `SoTA` front rather than citing those lines separately. | Use only when each source line has an assigned contribution, contribution strata are distinguishable, the `SourceComposedResultClaim` is named, the object-under-improvement evaluation can read the claimed movement, and protected trade-offs are checked. |
| `SpecializedObjectFamilyCycle` | A narrower method family optimized for one declared characteristic space such as throughput and constraint, variation and defect, learning and stabilization, or orientation quality. | Use when the object-under-improvement evaluation declares that space and the specialization is BLP-compatible; durable adaptation claims are assigned to `C.22.1`. |

Specialized cycles and general adaptive loops are alternatives under the same object-under-improvement evaluation discipline. A specialized cycle is not automatically better because it is familiar. A general adaptive loop is not automatically better because it is scalable or automated.

#### E.23:4.5 - Operation-family activation rule

An operation family is selected for a concrete loop only when the loop record names all of the following:

1. the object-under-improvement evaluation coordinate, quality value, or stop meaning expected to improve;
2. the failure mode the operation addresses;
3. the cost or risk reason for adding the operation;
4. the protected trade-offs it must not damage;
5. the stop or removal condition if the operation does not move the object-under-improvement evaluation.

If those fields are absent, the operation family stays unselected for that loop. It may remain a rationale or example, but it must not become required apparatus.

| Operation family | Use when | Boundary |
|---|---|---|
| `SpecificationArticulation` | The object under improvement is not clear enough for repeated attempts. | `E.22` frames the improvement-oriented quality read; `E.9` and the governing object-side pattern name the decision or specification content when live. |
| `TaskDecomposition` | A large object under improvement would otherwise produce blind retries. | Use only when the object-under-improvement evaluation can preserve protected trade-offs across the split. |
| `ContextRefreshWithCarryForwardEvidence` | A fresh context is useful but previous pass evidence must not be lost. | Carried-forward evidence is material for the next pass, not a quality value by itself. |
| `FailureContextRetry` | A failed attempt contains useful error, tool, reviewer, or object-version-under-improvement feedback. | Retrying is inadmissible when the failure shows wrong object under improvement, wrong evaluation, or missing authority. |
| `VerificationAgainstSpecification` | Passing local checks could diverge from the intended result. | `E.22` and the object-under-improvement evaluation decide whether the result meets the declared aim. |
| `MemoryOrDistillation` | Previous failures or local lessons would otherwise be rediscovered repeatedly. | Durable specialization claims go to `C.22.1`; selected-set publication or parity claims go to `G.5` or `G.9` when live. |
| `ExternalCriticOrMetacognitiveCoRegulation` | Fixation, underexploration, or high-cost mistakes are live risks. | Opens only when added supervision cost is justified by `C.19.1` cost and risk comparison and the object-under-improvement evaluation can use the feedback. |
| `ImprovementProposalPortfolioUse` | One `E.22` read returns several candidate improvement proposals, and the loop must decide how to apply, split, reject, or hand off them. | `E.23` can govern object-version-under-improvement changes and re-reads; NQD generation, front or archive handling, selected-set publication, parity, and refresh stay with `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. |
| `SearchBreadthVariantsOrTreeSearch` | Several candidate changes may matter and one linear retry path is too narrow. | Option generation and pool policy stay outside `E.23`; `C.11`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` govern choice, generation, exploration policy, selected-set publication, parity, and refresh when live. |
| `BoundedObjectChangeBudget` | Too many object edits can hide which change moved the object-under-improvement evaluation. | State the permitted edit scope, protected trade-offs, and re-read boundary before applying changes. |
| `HeldOutObjectUnderImprovementEvaluationRead` | The loop could overfit to the same visible read. | Use a held-out or more demanding object-under-improvement evaluation read only when the object-under-improvement evaluation defines that demanding relation; do not invent a second score. |
| `RejectedChangeMemory` | Rejected proposals would otherwise be retried. | Record rejection reason as loop memory; do not treat it as archive, selected-set publication, or source evidence. |
| `OptimizerMemorySeparation` | Local optimizer notes or prompt memories could leak into the changed object version or quality value. | Keep optimizer memory, loop record, changed object version, and object-under-improvement evaluation result distinct. |
| `SourceLineContributionAssignment` | Several accepted `SoTA` or practice lines are being composed into one improvement. | State the contribution of each line as operation family, boundary, comparison discipline, failure mode, protected trade-off, or value semantics; keep contribution strata distinct enough that source names cannot stand in for the source-composed result claim. |
| `AgentToolInterfaceHardening` | Tool-using agent action, observation, and verification need reliability. | `C.24` governs call planning, budgets, stop or replan conditions, and checkpoint returns. |
| `TaskFamilyAdaptationSignature` | A loop claims acquisition of reusable specialization for a task family. | `C.22.1` records threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor-entry fields. |

#### E.23:4.6 - BLP and accepted-work cost

`C.19.1` governs the preference for general, scale-amenable methods when safety and legality are comparable. `E.23` does not replace that preference.

A Ralph-like loop is accepted here only as a current external example of a general adaptive agentic method shape: one broadly capable agent repeatedly works from a specification, receives feedback from the changed object version under improvement, declared transduction result, or tool feedback channel, and starts subsequent attempts with refreshed context or carried state. `E.23` does not import the Ralph name, the infinite-loop idiom, or coding-tool scope as method law.

The local cost and risk prompt is:

```text
AcceptedWorkCost ~= token_or_compute_cost + tool_cost + adaptation_attempt_cost + human_supervision_cost + rework_cost - avoided_loss_value
```

This expression is not a hidden scalar quality score. If avoided loss is large, an expensive loop can be right. If the object under improvement is simple, a cheaper model, human edit, small direct repair, specialized cycle, or one-shot review can be better. If the loop keeps burning attempts without object-under-improvement evaluation movement, BLP does not protect it.

Harness improvement is usually the preferred first improvement move when it can reduce blind trial-and-error: better prompts, better object-under-improvement evaluation frames, better row shapes, better test cases, better exact source references, better local tooling, better memory or distillation, better verification, and better stop conditions. This follows `C.19.1` when the improved harness makes the general method more scale-amenable rather than adding a narrow patch that must be re-tuned for every object under improvement.

#### E.23:4.7 - Re-read, trade-offs, and stopping

Row-atomic absorption changes the object under improvement. It is not coordinate improvement until the object-under-improvement evaluation re-reads the changed object version.

The re-read names:

1. object version under improvement before and after the change;
2. object-under-improvement evaluation;
3. active coordinates, statuses, or declared values affected;
4. findings applied, already satisfied, rejected, or assigned outside the object-under-improvement evaluation;
5. expected and observed quality movement;
6. protected trade-offs that worsened or stayed intact;
7. remaining blockers, feasible non-dominated improvements, or bounded non-use;
8. stop, narrow, continue, switch, or hold decision.

Use `continue` only when another pass has a recoverable expected object-under-improvement evaluation movement. Use `switchMethodFamily` when the current method family is not moving the object under improvement, has become too costly, or no longer fits the characteristic space. Use `holdForExactInformation` when the object under improvement, evaluation, authority, evidence, or source condition is too under-specified for the next pass to be meaningful.

A loop record is sufficient when it lets the next reader tell what changed, what the object-under-improvement evaluation read after the change, what became worse, what remains bounded non-use, and why the chosen stop, narrow, continue, switch, or hold decision follows. A record that lists applied findings without the object-under-improvement evaluation re-read is executor discharge evidence, not quality-improvement closure.

#### E.23:4.8 - Non-use boundaries

A quality-improvement-loop result is not project evidence, assurance, gate passage, release approval, safety acceptance, compliance evidence, or work authority unless the exact neighbouring FPF pattern is opened for that claim.

Repeated agentic attempts are not BLP-compatible merely because they are automated. They need declared object under improvement, object-under-improvement evaluation, protected trade-offs, bounded cost and risk posture, and stop or switch conditions.

External review, landing, monolith placement, praise, popularity, adoption, or absence of blockers does not raise quality values by itself. Such signals may point to content evidence only after the object-under-improvement evaluation says how they matter.

`E.23` must not force full-loop apparatus on cheap local edits. A clean floor read may close through `E.22` plus the object-under-improvement evaluation without opening this method.

### E.23:5 - Archetypal grounding

**Show, cheap floor read.** A requester asks whether one pattern version is admissible for a declared use. `E.22` frames a short `floorRead`; `E.21` reads active pattern-quality coordinates. If `E.21` returns an admissible stop and no improvement aim is live, `E.23` stays closed.

**Show, exceptional pattern improvement.** A steward asks to improve one pattern beyond floor for a declared reader and use window. `E.23` opens the repeated method. `E.22` frames each quality review. `E.21` supplies coordinates and stop meanings. Operation families are selected only when their expected movement, failure mode, cost and risk reason, protected trade-offs, and stop condition are explicit.

**Show, DRR adequacy improvement.** A campaign needs a `DRR` raised to drafting adequacy for pattern drafting and receiving-locus distribution. `E.23` opens the repeated method. `E.22` frames each review. `E.9.DA` supplies coordinates and stop meanings. The result is a better decision record, not a prewritten pattern.

**Show, proposal portfolio for a pattern.** An external review of one pattern returns twenty candidate improvements across first-use usability, source-content preservation, relation precision, and examples. `E.22` frames this as a bounded proposal portfolio rather than as one bug. `E.23` applies or rejects proposals row by row, re-reads the changed pattern through `E.21`, and stops when the declared coordinates have reached all-`5` or no further non-dominated change remains under the current use. If the pattern claims exceptional expression from `SoTA`, the record names which working external front it reaches or improves, and which source lines compose into the source-composed result claim. A later use, more current source line, more directly relevant source line, or changed comparison set can open a new loop.

**Show, proposal portfolio for a DRR.** A reviewer returns many decision-adequacy improvements for one `DRR`. `E.23` uses `E.9.DA` as the object-under-improvement evaluation, preserves decision rationale, applies non-dominated proposal rows, and re-reads the changed `DRR`. The loop does not stop after the first fixed issue when the requested aim is exceptional decision adequacy.

**Show, engineering quality-family object under improvement.** The object under improvement is a system-facing engineering result with availability, resilience, maintainability, or safety-related quality claims. `E.23` can run the method only after the receiving endpoint is declared. `C.25` may supply the Q-Bundle endpoint, but `E.23` does not invent quality values.

**Show, missing object-under-improvement evaluation.** A team asks to improve an onboarding method, but no one has declared the object kind, use, contrast cases, coordinate set, scale meanings, protected trade-offs, or stop condition. `E.23` stays closed. `A.19.ECS` first constructs the object-under-improvement evaluation `CharacteristicSpace`; then `E.22` can frame the first read and `E.23` can run repeated improvement.

**Show, NQD quality-side improvement.** A generated candidate or declared transduction result has a declared `Q` side and comparison set. `E.22` returns a bounded portfolio of candidate improvement proposals. `E.23` may apply one or more proposal rows to one object version under improvement and re-read `Q` movement relative to the externally declared current non-dominated front, accepted `SoTA` line, or competing candidate set. Candidate generation, archive or front insertion, selected-set publication, parity, and refresh stay with `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`.

**Show, fixed-performer object-version-under-improvement optimization.** A fixed model, reviewer harness, or tool-using performer repeatedly edits a mutable object version under improvement. The method can use bounded object changes, held-out object-under-improvement evaluation reads, rejected-change memory, and optimizer-memory separation. The quality claim still comes only from the object-under-improvement evaluation re-read of the changed object version.

**Show, SoTA reach and maintenance.** A pattern draft has ten accepted source or practice lines. A conforming `E.23` loop does not paste ten citations into rationale and call the result `SoTA`. It assigns each line a contribution, keeps contribution strata distinguishable, composes those contributions into one named `SourceComposedResultClaim`, checks whether the object-under-improvement evaluation reads movement toward the externally assigned current front, and records what protected qualities did not get worse. Later source change can reopen the loop to maintain that front.

**Show, overloaded quality wording.** The object under improvement text uses `quality` in a load-bearing way without a recoverable endpoint. `C.16.Q` opens before the loop proceeds. The term is repaired to one exact endpoint or transitional evaluative-ascription form, then `E.23` may use the repaired object-under-improvement evaluation.

**Near miss, agent retries until praise.** A tool-using agent keeps trying until the reviewer says the text is better. This is not an `E.23` closure. The loop must name the object under improvement, object-under-improvement evaluation, expected movement, protected trade-offs, cost and risk posture, and re-read result.

**Near miss, POOGI everywhere.** A team treats every quality problem as a constraint problem. `E.23` permits POOGI-shaped work only when the object-under-improvement evaluation is actually throughput-shaped or constraint-shaped and inertia after constraint shift is a live concern.

### E.23:6 - Bias annotation

`E.23` intentionally biases repeated improvement toward explicit object under improvement, explicit object-under-improvement evaluation, and explicit stop decisions.

The bias is useful because repeated passes often generate convincing activity without object-under-improvement evaluation movement. The bias is dangerous if every small repair is forced through full-loop ceremony. Keep `E.22` short-form reads cheap, and open `E.23` only when repeated improvement or absorption impact is live.

### E.23:7 - Conformance checklist

| ID | Requirement | Why |
|---|---|---|
| `CC-E23-1` | A quality-improvement loop SHALL name the exact `ObjectUnderImprovementRef` and object version under improvement. | Prevents campaigns, chats, source bundles, or task lists from replacing the object under improvement. |
| `CC-E23-2` | A quality-improvement loop SHALL name the exact `ObjectUnderImprovementEvaluationRef` before values, floors, or stop meanings are used; if none exists, the object-under-improvement evaluation `CharacteristicSpace` SHALL be constructed or repaired through `A.19.ECS` before the loop opens. | Prevents `E.23` from inventing quality values. |
| `CC-E23-3` | The first quality review in the loop SHALL be framed through `E.22` or an explicitly equivalent object-under-improvement evaluation question frame. | Keeps one-read question framing distinct from the repeated method. |
| `CC-E23-4` | Returned actionable findings SHALL be row-atomic, with expected object-under-improvement evaluation movement and closure test recoverable. | Prevents "handled overall" improvement claims. |
| `CC-E23-5` | Executor discharge SHALL NOT be treated as coordinate improvement until the changed object version is re-read by the object-under-improvement evaluation. | Blocks checklist-count and discharge-count substitution. |
| `CC-E23-6` | Every continue decision SHALL state the expected object-under-improvement evaluation movement for the next pass. | Prevents unbounded retry. |
| `CC-E23-7` | Every operation family selected for a loop SHALL name expected object-under-improvement evaluation movement, failure mode, cost and risk reason, protected trade-offs, and stop or removal condition. | Blocks automatic bureaucracy and optional-operation drift. |
| `CC-E23-8` | A method-family selection SHALL state the characteristic-space fit and BLP cost boundary for the object under improvement. | Prevents importing PDCA or PDSA, POOGI, OODA, Ralph-like, or specialized cycles as universal sequences. |
| `CC-E23-9` | A loop SHALL record protected trade-offs and what got worse whenever visible coordinates improve. | Prevents Goodhart-style improvement. |
| `CC-E23-10` | A loop SHALL keep `A.19.ECS`, `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, `C.16.Q`, `C.19.1`, `C.22.1`, and `C.24` in their governed roles when those roles are live. | Prevents neighbour theft. |
| `CC-E23-11` | A loop result SHALL NOT be reused as evidence, assurance, gate, release, safety, compliance, or work authority without opening the exact neighbouring FPF pattern for that claim. | Keeps project-side claims out of the improvement method. |
| `CC-E23-12` | A clean `floorRead` SHALL be allowed to stop through `E.22` plus the object-under-improvement evaluation without opening this method. | Keeps ordinary quality reads affordable. |
| `CC-E23-13` | An all-exceptional or all-`5` result SHALL carry an explicit object-under-improvement evaluation coordinate-value table over the changed object version. | Prevents floor pass, landing, or praise from becoming exceptional-value evidence. |
| `CC-E23-14` | Load-bearing source, authority, basis, support, record, and view wording SHALL recover exact kind or relation under `E.10`. | Keeps loop prose from reintroducing umbrella language. |
| `CC-E23-15` | A closed loop pass SHALL leave a `QualityImprovementLoopRecord` with object version under improvement, object-under-improvement evaluation, applied rows, object-under-improvement evaluation re-read, trade-offs, cost and risk posture, and stop decision recoverable by value. | Prevents quality closure from being reconstructed from chat memory, praise, or checklist closure. |
| `CC-E23-16` | If `E.22` returns a proposal portfolio, the loop SHALL keep proposal rows, selected object changes, rejected proposals, object-under-improvement evaluation re-read, and neighbour exits distinct. | Prevents a review portfolio from becoming a hidden selector result. |
| `CC-E23-17` | If the object-under-improvement evaluation is the `Q` side of NQD/OEE, the loop SHALL name the `Q` components, external comparison basis, comparison set or current front, expected `Q` movement, protected trade-offs, and neighbour exits for generation, archive or front handling, selected-set publication, parity, and refresh. | Lets improvement move candidates in NQD without stealing OEE/NQD semantics or self-assigning exceptional status. |
| `CC-E23-18` | An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result SHALL be treated as a local stop condition for this object-under-improvement evaluation and comparison set, not as proof that further development is impossible. | Prevents maturity-ceiling stagnation while still allowing this loop to close. |
| `CC-E23-19` | A source-bearing loop that claims `SoTA` reach, `SoTA` maintenance, or front improvement SHALL name the external source of that front and SHALL state the source or practice lines composed, object-under-improvement evaluation coordinates affected, and protected characteristics preserved. | Prevents "we cited SoTA" from becoming a self-assigned `SoTA` claim. |
| `CC-E23-20` | When a loop composes several accepted source or practice lines, it SHALL assign each line a contribution, keep contribution strata distinguishable, and state the `SourceComposedResultClaim` before claiming movement toward or maintenance of the external front. | Keeps SoTA reach and maintenance architectural rather than decorative. |

### E.23:8 - Common anti-patterns and repairs

| Anti-pattern | Failure | Repair |
|---|---|---|
| **Loop invents quality.** | The method says the object under improvement improved without an object-under-improvement evaluation. | Name an existing object-under-improvement evaluation, construct or repair one through `A.19.ECS`, or stop before claiming quality movement. |
| **Checklist closed, quality improved.** | Row count replaces coordinate movement. | Re-read the changed object version through the object-under-improvement evaluation. |
| **Agentic retry as method law.** | A broad agent repeats attempts without stop or switch conditions. | Add object under improvement, evaluation, expected movement, cost and risk posture, protected trade-offs, and stop or switch conditions. |
| **Full loop for a small floor check.** | A cheap readiness question becomes expensive ceremony. | Use `E.22` short-form `floorRead` and stop if the object-under-improvement evaluation gives admissible stop. |
| **Specialized-cycle cargo cult.** | PDCA or PDSA, POOGI, OODA, or another named cycle is used because it is familiar. | State the characteristic-space fit; otherwise select another method family or use a direct repair. |
| **Ralph name as authority.** | The loop is treated as good because it resembles a current tool technique. | Use the selected operation-family semantics only when object-under-improvement evaluation payoff and `C.19.1` cost and risk comparison justify them. |
| **Operation-family creep.** | Verification, memory, supervision, tree search, or decomposition is added for every object under improvement. | Apply the operation-family activation rule and remove the operation when it does not move the object-under-improvement evaluation. |
| **Goodharted exceptional pass.** | Visible coordinates rise while first use, affordability, source preservation, or neighbour fit worsens. | Add trade-off inspection and reject, narrow, or split changes that are dominated under the object-under-improvement evaluation. |
| **Neighbour theft.** | `E.23` starts defining characteristic-space construction, pattern quality, DRR adequacy, Pillar adequacy, naming quality, Q-Bundles, quality-term repair, adaptation signatures, or call planning. | Return those claims to `A.19.ECS`, `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, `C.16.Q`, `C.22.1`, or `C.24` as appropriate. |
| **Proposal portfolio becomes winner.** | The loop treats a list of improvement proposals as if it already selected what must be generated or published. | Keep proposals as proposal rows; use the exact decision, NQD, selected-set, parity, or refresh pattern for claims that exceed proposal status. |
| **Quality-side takeover.** | The loop uses `Q` movement to redefine novelty, diversity, archive, front, pool, selected-set, parity, or refresh semantics. | Keep `E.23` to object-version-under-improvement changes and object-under-improvement evaluation re-read; return OEE/NQD semantics to `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. |
| **Maturity-ceiling stop.** | An all-`5`, current-front-reaching, or current-front-improving result is treated as the end of development rather than the end of this loop under current conditions. | Close the current loop, record the object-under-improvement evaluation and comparison set, and allow a later loop when use, `Q`, front, source, `SoTA`, cost, or payoff changes. |
| **SoTA citation as self-assignment.** | The loop treats citation of current practice as proof that the object under improvement itself is `SoTA`. | Treat accepted `SoTA` as the working external front; claim only reach, maintenance, or front-improving proposal after object-under-improvement evaluation re-read. |
| **Source shelf instead of synthesis.** | Many sources are listed, but none has a recoverable contribution to the changed object version. | Assign source-line contributions, keep contribution strata distinguishable, name the `SourceComposedResultClaim`, and re-read the object under improvement through the object-under-improvement evaluation; otherwise mark the sources rationale-only or remove the front-movement claim. |

### E.23:9 - Consequences

| Consequence | Benefit | Cost or guard |
|---|---|---|
| Repeated improvement has one FPF method locus. | Process references and local campaign habits no longer carry hidden doctrine. | The loop must not duplicate object-under-improvement evaluation values. |
| One-read quality framing stays cheap. | A floor read can close without full-loop apparatus. | Requesters must say when exceptional improvement or repeated absorption is live. |
| Agentic and classical loop traditions become selectable method families. | Useful practice is available without importing one universal sequence. | Each family needs characteristic-space fit and cost and risk justification. |
| Row-atomic discharge is separated from quality movement. | Executors can show what changed while reviewers keep value authority. | A re-read is required before coordinate movement is claimed. |
| Goodhart checks become part of improvement. | Protected trade-offs stay visible when values rise. | Some attractive edits will be rejected or narrowed. |
| Proposal portfolios can feed improvement without becoming decisions. | Reviews can return many non-dominated improvement rows, including pattern and `DRR` rows, without pretending one row is the only next move. | Selection, generation, selected-set publication, parity, and refresh need exact neighbour exits when those claims become live. |
| `Q`-side NQD movement is expressible. | A loop can improve a candidate, object version under improvement, or declared transduction result relative to an externally declared comparison set, `SoTA` line, or current front. | `E.23` must not redefine `N`, `D`, archive, front, pool, selected-set, parity, or refresh semantics. |
| Exceptional stop stays local. | All-`5` or current-front-reaching closure can stop the current loop without denying future development. | New use, `Q`, front, source, `SoTA`, cost, or payoff can reopen improvement. |
| Neighbouring pattern authority is preserved. | Quality bundles, term repair, adaptation signatures, call planning, and project claims stay governed by their exact neighbouring patterns. | The user must name exact neighbour exits when those claims become live. |

### E.23:10 - Rationale

Quality improvement is not the same problem as quality review. A review can answer one framed question about one object version under improvement. Improvement changes the object under improvement and then asks whether the changed object version is better under the declared object-under-improvement evaluation.

The separation keeps the first pass affordable. `A.19.ECS` constructs or repairs a missing object-under-improvement evaluation `CharacteristicSpace`; `E.22` frames the read; `E.21`, `E.9.DA`, `E.2.DA`, `F.18`, `C.25`, or another evaluation supplies values; `E.23` governs repetition, absorption, re-read, cost and risk posture, method-family selection, and stopping.

Classical cycles and agentic loops become useful when treated as candidate method families rather than as universal law. POOGI optimizes throughput and constraint selection; PDCA and PDSA optimize learning and stabilization against declared measures; OODA optimizes orientation quality under changing conditions; Ralph-like loops approximate a broad adaptive agent repeatedly working from specification, feedback, verification, and memory. `E.23` asks whether the method family fits the object-under-improvement evaluation and whether the next pass is still worth its cost.

The method also protects against over-optimization. Improvement is multi-characteristic optimization by changes that produce non-dominated gains or explicitly accepted trade-offs, not one scalar quality score.

The `NQD` connection gives a precise reading of "space of characteristics" when open-ended improvement is live: those characteristics can be the declared `Q` components of the comparison. `E.23` can then govern repeated object changes that move one candidate or declared transduction result against an externally declared comparison set, accepted `SoTA` line, or current front. That does not make `E.23` the generator, archive, selector, parity, or refresh pattern.

This also distinguishes `SoTA` from loop-internal improvement. `SoTA` names the working external front at the time of the read. A loop can try to reach that front, maintain it as sources change, or test a front-improving proposal by combining several accepted source or practice lines into one `SourceComposedResultClaim` that the single lines did not already provide. The claim is only admissible when the object-under-improvement evaluation can read that result claim and the protected characteristics together.

`E.23` applies that rule to loops that use it. A loop's source composition can be multi-stratum: classical improvement cycles contribute explicit learning and stop discipline; BLP contributes cost and general-method preference; agentic-loop practice contributes optional operation families; SkillOpt-like work contributes fixed-performer object-version-under-improvement optimization; MCDA and Goodhart lines contribute protected trade-off and proxy checks; OEE/NQD contributes `Q`-side comparison, fronts, and proposal portfolios. The combined result is an improvement-loop method instance that remains cheap for floor reads, useful for externally assigned `SoTA` reach or maintenance, and bounded by neighbours.

The stop rule is deliberately local. Reaching all `5` values or the current non-dominated front means the current loop has no better admissible move under the named object-under-improvement evaluation, `Q` components, externally declared comparison basis, protected trade-offs, and cost boundary. It does not say development is complete forever. It says the next improvement question needs a changed use, changed comparison, changed source, changed `SoTA`, changed cost boundary, or another exact reason to reopen.

### E.23:11 - SoTA-Echoing

`E.23:11` uses `SoTA` in the `E.8` sense: current best-known problem-solving practice for the governed problem. A row that carries a fast-moving current-practice claim is admissible only when it has current-source posture or is explicitly narrowed to lineage, example-only, or rationale-only use.

| Claim | Practice or source line | Local adoption | Non-use boundary |
|---|---|---|---|
| Improvement must preserve desired condition, current condition, next action, and learning from the result. | Lineage-only improvement-cycle material: PDSA and PDCA keep explicit theory, measurement-backed comparison, study and learning, and standardize-or-repeat action. They are not used here as current SoTA for all improvement. | `E.23` requires object version under improvement, object-under-improvement evaluation, improvement aim, re-read, and a decision to stop, narrow, continue, switch method, or hold for more exact information. | Does not import a universal four-label sequence or lean-only scope. |
| Constraint-focused improvement is useful only for throughput-shaped problems. | Lineage-only TOC material: POOGI and Five Focusing Steps keep constraint selection, throughput relation, and inertia after the constraint shifts. | `POOGIFamily` is selectable when the object-under-improvement evaluation is throughput-shaped or constraint-shaped. | Does not make every quality object under improvement a TOC constraint. |
| Orientation and feedback matter under changing conditions. | Lineage-only decision-cycle material: OODA keeps orientation and feedback under a changing external situation. | `OODAFamily` is selectable when orientation quality and feedback change the object read. | Does not count speed, cadence, or action volume as quality. |
| Ralph-like repeated agent work is a current external technique signal, not mature FPF method law. | Thoughtworks Technology Radar Vol. 34, `Ralph loop`, published 2026-04-15, ring `Assess`; Ralph CLI docs at `ralph-cli.dev` as refreshable implementation material; Wiggum.dev `The Loop` docs as rationale material. | Fresh-context repeated agent work from a specification or plan, token-cost warning, task/progress state, failure-context retry, verification, session memory, and possible cross-model review are selectable only when the object-under-improvement evaluation payoff and `C.19.1` cost/risk comparison justify them. | Does not import infinite loop, coding-only scope, convergence by repetition, product command order, or the Ralph/Wiggum name as FPF method authority. |
| Older agentic-loop papers are lineage for operation-family candidates. | Reflexion, Self-Refine, ReAct, LATS, and SWE-agent are retained as lineage-only lines for feedback memory, iterative refinement, reasoning/action coupling, search breadth, and agent-computer interface hardening. | These operation families may be selected only when the object-under-improvement evaluation can read the payoff and `C.19.1` makes the cost/risk acceptable. | Does not import benchmark claims, self-assessment as validation, mandatory tree search, hidden option-pool governance, or coding-benchmark authority. |
| Engineering-design co-regulation is a narrow current research line. | `Supervising Ralph Wiggum` / CRDAL, `arXiv:2603.24768v2` (2026-05-07), is used as current research signal for engineering-design co-regulation. | Metacognitive co-regulation is selectable when fixation, underexploration, or high-cost design mistakes are live risks. | Does not create a universal extra supervisor, proof that self-regulation always improves results, or generic FPF quality values. |
| Financial-alpha self-evolving search is domain-specific current research. | FactorMiner, `arXiv:2602.14670v1` (2026-02-16), is used as current research signal for self-evolving financial-alpha search. | Retrieve/generate/evaluate/distill, modular skill architecture, experience memory, and reduced redundant search are operation-family cues only when a comparable object-under-improvement evaluation exists. | Does not import financial-alpha objectives, factor-library quality values, or automatic transfer to all quality objects under improvement. |
| Fixed-performer object-version-under-improvement optimization is a narrow current research line. | SkillOpt, `arXiv:2605.23904v2` (2026-05-25), keeps a base language agent fixed while iteratively editing an external skill document through add, delete, and replace operations, feedback from failed evaluations, validation or held-out checks, and separated optimizer memory. | `FixedPerformerObjectVersionUnderImprovementOptimizationFamily`, `BoundedObjectChangeBudget`, `HeldOutObjectUnderImprovementEvaluationRead`, `RejectedChangeMemory`, and `OptimizerMemorySeparation` are selectable operation families when a loop improves one mutable object version under improvement and one object-under-improvement evaluation. | Does not make external skill documents the only object-under-improvement form, does not import benchmark claims, and does not treat optimizer memory as object-under-improvement content or quality evidence. |
| Multi-coordinate improvement needs explicit trade-offs and non-dominated gains. | Current proxy-risk anchors: `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current reward-misspecification Goodhart work such as NeurIPS 2024 catastrophic-Goodhart lines; retained lineage: MCDA, Pareto-front reasoning, and quality-attribute trade-off traditions. | `E.23` requires protected trade-offs, what-got-worse read, object-under-improvement evaluation re-read, and explicit all-exceptional coordinate evidence. | Does not require formal optimization, utility functions, or numeric MCDA for ordinary improvement work. |
| OEE/NQD makes improvement relative to declared `Q`, comparison sets, and fronts. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026); retained lineage: QD and open-ended search archive/front practice. | `NQDQualitySideImprovementFamily` lets `E.23` improve one candidate, object version under improvement, or declared transduction result on declared `Q` components relative to an externally declared comparison set, accepted `SoTA` line, or current front, while `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` govern their respective semantics. | Does not let `E.23` define `N`, `D`, descriptor or distance rules, archive insertion, candidate-pool policy, selected-set publication, parity, or refresh. |
| Source-bearing improvement can reach or maintain an externally assigned `SoTA` front. | Internal source-composition rule: currentness comes from the exact external or FPF-neighbour source lines being composed, not from this row by itself. | `E.23` lets a loop claim front reach, front maintenance, or front-improving proposal only when the record names the external front, source or practice lines composed, contribution strata, `SourceComposedResultClaim`, object-under-improvement evaluation coordinates affected, and protected characteristics preserved. | Does not make every SoTA-backed pattern `SoTA` and does not license novelty claims without object-under-improvement evaluation re-read. |
| A high-quality improvement loop should synthesize source lines into a simpler usable method. | Rationale-only synthesis row: improvement-cycle, agentic-loop, MCDA, Goodhart, fixed-performer optimization, and OEE/NQD lines each solve only part of the FPF problem; exact currentness remains on the contributing rows above. | `E.23` can use them as assigned contribution strata in one loop: `E.22` framing, proposal portfolios, object-version-under-improvement changes, re-read, protected trade-offs, local stop, and neighbour exit. | Does not require every project to run every operation family and does not turn the SoTA table into mandatory apparatus. |
### E.23:12 - Relations

| Pattern | Relation |
|---|---|
| `A.19.ECS` | Constructs or repairs an object-under-improvement evaluation `CharacteristicSpace` when no adequate object-under-improvement evaluation exists for the object being improved. `E.23` starts only after that evaluation is declared. |
| `E.22` | Frames each quality review inside the loop and can return one candidate improvement proposal or a bounded proposal portfolio. `E.23` governs repetition, absorption, object-version-under-improvement change, re-read, method-family selection, and decisions to stop, narrow, continue, switch method, or hold for more exact information. |
| `E.21` | Receives FPF pattern-quality reads. `E.23` can improve one pattern version under `E.21`, but `E.21` supplies coordinates, values, statuses, and stop meanings. |
| `E.9.DA` | Receives `DRR` decision-adequacy reads. `E.23` can improve one `DRR` under a declared authoring use, but the result remains a decision record, not a prewritten pattern. |
| `E.2.DA` | Receives whole-FPF or FPF-corpus Pillar-adequacy reads. `E.23` can improve that FPF object under improvement under `E.2.DA`, but `E.2.DA` supplies Pillar coordinates, values, and stop meanings. |
| `F.18` | Receives durable-name and term-improvement reads through its local lexical quality vector. `E.23` can improve naming candidates under `F.18`, but `F.18` supplies naming coordinates, candidate-front discipline, and name-card meanings. |
| `C.25` | May supply the Q-Bundle endpoint for engineering quality-family objects under improvement. `E.23` does not create one universal quality score. |
| `C.16.Q` | Repairs load-bearing ambiguous `quality` wording before a loop can rely on it. `C.16.Q` is not the loop method. |
| `C.19.1` | Governs BLP method preference and waiver discipline for general adaptive versus specialized method families. |
| `C.22.1` | Carries durable task-family adaptation-signature claims produced through an `E.23` loop when threshold, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, or corridor-entry claims are live. |
| `C.24` | Governs call plans, checkpoint returns, tool-call budgets, stop or replan conditions, and separation between call plan and executed work when an `E.23` loop is enacted through tool-using agents. |
| `E.18` | Supplies transduction graph, path, crossing, flow-valuation, and declared transduction-result context when the object under improvement is produced by a transduction. |
| `C.17` | Governs candidate novelty, use-value, surprise, constraint fit, diversity, originality, and resource-efficiency characterization when those are live for OEE/NQD improvement. |
| `C.18` | Governs NQD generation, descriptor and distance pins, archive and front semantics, and illumination telemetry. `E.23` may improve `Q` movement for one object under improvement but does not govern `C.18` semantics. |
| `C.19` | Governs live candidate-pool policy. `E.23` does not decide whether to widen, keep frontier, narrow, sunset, or reroute the pool. |
| `G.5` | Governs selected-set publication, including `Shortlist`, `RankedShortlist`, narrowed handoff, abstain, and escalation results. |
| `G.9` | Governs parity and benchmark comparison over selected sets, archives, fronts, or method families when those claims are live. |
| `G.11` | Governs refresh of shipped set results, archive telemetry, parity reports, or OEE/NQD pins. |
| `C.11` | Governs local decision value when proposal rows become an explicit choice among alternatives rather than a loop-internal object-version change. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Govern evidence, assurance, local CV status, gates, and work when a loop result is reused for project-side claims. `E.23` blocks that overread unless the exact neighbouring pattern is opened. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by a loop record. `E.23` does not accept source, authority, basis, support, record, view, object under improvement, or quality as umbrella substitutes for exact kinds and relations. |

### E.23:End

