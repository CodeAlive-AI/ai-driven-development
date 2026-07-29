## E.23 - Quality Improvement Loop Method

Status: Core.

### E.23:1 - Problem frame
When the entry phrase is "loop engineering", "agent loop", "harness loop", or "improve this with an agent", treat the phrase as a recognition cue, not as an FPF kind. First recover the object version under improvement and the evaluation that can be rerun. If those cannot be named, this is not yet an `E.23` use; name the live claim and send it to its direct governing pattern. Common exits are work, transformation-flow structure, evolutionary retention and publication, source use, refresh, gate-decision publication, and DPF framework authoring.

Use `E.23` when an object version will be improved through repeated passes under a declared object-under-improvement evaluation. The object can be a pattern, `DRR`, FPF corpus object, engineering quality object, naming candidate, OEE and NQD candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, if an exact evaluation supplies values and stop meanings for that object kind.

Not this pattern when one direct quality evaluation is enough. Use `E.22` to frame one evaluation and then run the named object-under-improvement evaluation. Use `A.19.ECS` first if the needed evaluation characteristic space does not exist.

First useful move: name the object version under improvement, the exact evaluation that will re-evaluate it, the improvement aim, protected trade-offs, cost and risk account, and local stop condition.

What goes wrong if missed: teams close discharge rows instead of improving quality, retry blindly, optimize visible values while damaging protected qualities, stop forever after a local all-`5` result, or let a review recommendation become decision, work, evidence, selected-set publication, parity, or refresh by stealth.

What this buys in practice: each pass has a declared object version, an intended evaluation-result change, a rerunnable evaluation, protected trade-offs, and a stop or switch condition. Effort can then change substantive quality and stop when no non-dominated change is worth its cost, instead of merely producing more review state.

Primary EntityOfConcern in plain terms: the repeated quality-improvement method for one object version under one declared evaluation.

### E.23:2 - Problem

FPF often improves artifacts by repeated review, repair, and re-evaluation. The loop is useful only when the changed object is evaluated again by the same object-under-improvement evaluation or by a declared stronger one. Without that discipline, repeated passes become checklist closure, agentic retry, source citation, or process state.

The loop also avoids the maturity-ladder trap. A floor or all-`5` result can close this loop under current use, comparison set, source state, and cost boundary; it is not proof that the object cannot improve under a new use, source, front, or payoff.

The loop also fails when an ordinal value becomes a work target. `5` is an assigned result after measurement, not an instruction to add apparatus until a `5` can be defended. Below-floor values return repair work. Above-floor improvement becomes current work when the frame selects it, but the target is a substantive content improvement: stronger positive action guidance, worked slice, case and countercase coverage, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or another named content gain. `Stay at 4` or `no proposal` is admissible only after a by-value search finds no non-dominated content improvement worth its cost under protected qualities.

### E.23:3 - Forces

| Force | Tension |
|---|---|
| Improvement ambition vs cost | Exceptional improvement can be valuable while ordinary floor work stays affordable. |
| General adaptive methods vs specialized cycles | Broad loops scale, while specialized cycles can be cheaper when the characteristic space fits. |
| Feedback vs self-confirming retry | Feedback helps only when re-evaluation checks changed quality. |
| Operation hardening vs bureaucracy | Verification, memory, decomposition, and supervision are admitted only when their expected improvement effect justifies cost. |
| Visible improvement vs protected trade-offs | One coordinate can rise while use, source preservation, locality, or ecology worsens. |
| Proposal portfolio vs selector overread | Proposals can guide improvement without becoming selected results or work plans. |

### E.23:4 - Solution

`E.23` is the general method for repeated improvement of an object version under one `QualityEvaluationUseDeclaration@Context` named by value. The governing evaluation pattern or semantic method evaluates; its characteristic-space, Q-Bundle, rubric, review-profile, evidence-basis, and result-form descriptions constrain or interpret that evaluation. The loop changes the object, re-evaluates the changed version through the same declared method and quality model, checks trade-offs and cost, and decides whether to stop, continue, switch method family, open a new frame, or hold until the information basis is sufficient.

#### E.23:4.1 - Local names and kind settlement
Source and practitioner phrases such as "loop engineering", "agent loop", "harness loop", "prompt loop", and "workflow hardening loop" are entry phrases. Lower them into `ObjectUnderImprovementRef`, `QualityEvaluationUseDeclaration@Context`, `ImprovementAim`, `MethodFamilySelection`, `CostAndRiskAccount`, and `QualityImprovementLoopRecord@Context`, or else name the direct governing pattern for the live claim and leave `E.23` closed.

Quick lowering map:

| Entry cue | `E.23` use | Exit when this is the live claim |
|---|---|---|
| "Build a loop" or "loop engineering" | Ask which object version is being improved and which evaluation will be rerun. | If no object-version improvement claim is present, choose the direct governing pattern named by the live claim. |
| Agent retry, monitor, or escalation cycle | Use `E.23` only when the retry changes an object version and re-evaluation can show a changed result on declared coordinates. | Performed execution and work plans use the A.15 family; gate passage uses `A.21`; transformation-flow cycle structure uses `E.18`. |
| Harness engineering | The harness can be the object under improvement when its next version is evaluated against declared quality, cost, and risk conditions. | Running the harness is work; comparing harness variants is `G.9`; retaining variants is `C.18` or `C.19`; selected-set publication is `G.5`. |
| Fast DPF seed hardening | A local DPF seed, pattern seed, relation record, or source pack can enter `E.23` after the object version and evaluation are declared. | Source-use and source-pack return use `G.2`; source decay, edition change, and refresh use `G.11`; PFAD and PFR decisions use `E.4.PFAD` and `E.4.PFR`; first-entry publication uses `E.11` only when publication is current. |

| Local name | Kind and function |
|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement `U.Method` for one object version under one declared evaluation use. |
| `ObjectUnderImprovementRef` | Exact `U.Entity` version being changed, paired with its exact `U.Kind`. |
| `QualityEvaluationUseDeclaration@Context` | The E.22 `U.Episteme` that keeps evaluator assignment, governing evaluation pattern, optional semantic method, quality-model descriptions, evidence basis, and result form distinct. E.23 reuses it; it does not define a second evaluation ontology. |
| `LoopEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version evaluated in one loop pass. It describes the evidence values actually checked and missing evidence positions found for that pass and is distinct from E.22's expected evidence-basis description. |
| `LoopEvaluationResultFormDescription` | `U.Episteme` describing the result-row form used for the current pass; normally the same form cited by the evaluation-use declaration. |
| `ImprovementAim` | Desired evaluation-result change. It names the intended quality change, not a value established by the repair itself. |
| `MethodFamilySelection` | Selected method family for the current object and evaluation. |
| `OperationFamilySelectionSet` | Optional operation-family set selected because its operations can change the evaluated result enough to justify cost. |
| `ObjectUnderImprovementReEvaluation` | Re-run or cited result of the governing evaluation method on the changed object version. |
| `CostAndRiskAccount` | Cost and risk account used to judge another pass or operation. |
| `ImprovementLoopDecisionValue` | Local closed value set `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. |
| `QualityImprovementLoopRecord@Context` | `U.Episteme` whose EntityOfConcern is the exact starting object version for one improvement-loop application. Its claim graph relates that version to changed versions, applied proposal rows, evaluation-use declaration, actual evidence basis, results, trade-offs, cost and risk, and the loop decision. It describes the loop; it is not the method, performer, work occurrence, or changed object. |
| `QualitySideEvaluationChangeClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it compares before and after evaluation results for named object versions on declared `Q` coordinates under one evaluation-use declaration and qualification window. |
| `SourceComposedResultClaim` | Controlled claim-node form inside a `U.ClaimGraph`; it relates one changed-object result claim to exact accepted source-use decisions and each source contribution. It is neither the changed object nor a source-use decision. |
| `KindRestorationCheck` | Conditionally present precision-repair check governed by the selected restoration pattern. |

```text
LoopEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version evaluated in this loop pass
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about that object version
  checkedEvidenceValueRefs[]: U.EntityRef, each referencing one evidence value actually checked
  checkedEvidenceValueKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence value
  checkedEvidenceRelationRefs[]: U.EntityRef, each referencing one governed evidence relation
  checkedEvidenceRelationKindRefs[]: U.KindRef, each referencing the exact kind of the paired evidence relation
  unfilledEvidencePositionDescriptionRefs[]: U.EpistemeRef, each referencing one description of an unfilled evidence position
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description

QualityImprovementLoopRecord@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact starting object version for this loop application
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that starting object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  changedObjectVersionRefs[1..*]: U.EntityRef, each referencing one changed object version
  changedObjectVersionKindRefs[1..*]: U.KindRef, each referencing the exact kind of the paired changed version
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context
  appliedProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context
  loopEvaluationEvidenceBasisRefs[1..*]: U.EpistemeRef, each referencing one LoopEvaluationEvidenceBasis@Context
  evaluationResultRefs[1..*]: U.EpistemeRef, each referencing one result episteme produced by the declared evaluation use
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  costAndRiskAccountDescriptionRef: U.EpistemeRef, referencing one cost-and-risk-account description
  loopDecisionValue: ImprovementLoopDecisionValue
  loopDecisionReasonDescriptionRef: U.EpistemeRef, referencing one loop-decision-reason description
QualitySideEvaluationChangeClaim in U.ClaimGraph:
  qualityEvaluationUseDeclarationRef
  beforeObjectVersionRef and afterObjectVersionRef
  beforeEvaluationResultRefs[] and afterEvaluationResultRefs[]
  evaluationCoordinateRefs[]
  qualificationWindowDescriptionRef

SourceComposedResultClaim in U.ClaimGraph:
  changedObjectVersionRef and changedObjectVersionKindRef
  resultClaimNodeRef
  acceptedSourceUseDecisionRefs[1..*]
  sourceContributionDescriptionRefs[1..*]
```

Checked evidence-value refs and kinds are positionally paired; checked evidence-relation refs and kinds form a second positional pair. Changed object-version refs and kinds are paired in the same way. The two named claims are node forms inside the claim graph of a result or loop episteme; a table row or serialization may publish them but does not become the claim.

Two carriers may publish the same episteme edition. `LoopEvaluationEvidenceBasis@Context` changes edition when the evaluated object version, bounded context, applicable grounding or viewpoint, declared evaluation use, checked evidence values or relations, unfilled evidence positions, qualification window, claim graph, or reference scheme changes. `QualityImprovementLoopRecord@Context` changes edition when its starting object version, bounded context, applicable grounding or viewpoint, changed-version relation, evaluation-use declaration, applied proposals, evidence-basis editions, evaluation results, trade-offs, cost and risk, decision, claim graph, or reference scheme changes. Carrier and support serialization alone change neither episteme. These names belong to the loop method. They do not create quality values, project evidence, release state, selected-set publication, parity, refresh, or proof of quality.

#### E.23:4.1a - Improvement Unfolding Structure Block

Use this block when a named review or replay use relies on the improvement loop's constraint-governed unfolding structure rather than only its method record. It keeps the proposal epistemes, predicted evaluation-result changes, decision value, information-basis hold, and neighboring relations exact instead of treating them as generic structural locations.

```text
ImprovementUnfoldingStructureBlock:
  unfoldingStructureRef: U.EntityRef, referencing one ImprovementLoopUnfoldingStructure
  objectVersionUnderImprovementRef: U.EntityRef
  objectVersionKindRef: U.KindRef
  evaluationFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context or equivalent exact frame
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context
  currentEvaluationResultRefs[]: U.EpistemeRef under that evaluation pattern
  candidateRepairProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context under E.22
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  expectedEvaluationResultChangeRefs[]: U.EpistemeRef, each referencing one ExpectedEvaluationResultChange@Context
  loopDecisionValue: ImprovementLoopDecisionValue
  unfilledInformationBasisPositionDescriptionRefs[1..*]?: U.EpistemeRef
  informationBasisSufficiencyConditionRef?: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  methodWorkLinkageRef?: U.EntityRef, referencing one MethodWorkUnfoldingLinkage@Context
  evidenceRelationRefs[]?: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with exact evidence relation kind and direct governing pattern
  evaluationRelationRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with exact evaluation relation kind and direct governing pattern
  stopBoundaryRef: U.EntityRef, referencing one ImprovementLoopBoundaryCondition@Context
  governingPatternReturnBoundaryRefs[]: U.EntityRef, each referencing one ImprovementLoopBoundaryCondition@Context
```

`ImprovementLoopUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization governed here for improvement-loop use. It is neither a root U-kind nor performed work, evidence, or quality proof. The structure relates the exact values above; it is not their kind.

E.23 governs the coordinate-qualified prediction episteme:

```text
ExpectedEvaluationResultChange@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose later evaluation result is predicted
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about that object version
  evaluationCoordinateRef: U.EpistemeRef, referencing one governed evaluation-coordinate description
  coordinateScaleRef: U.EpistemeRef, referencing one scale description that admits results for that coordinate
  currentEvaluationResultRef: U.EpistemeRef, referencing one current result episteme under the declared evaluation use
  changeExpressionKind: ExpectedEvaluationChangeExpressionKindValue
  expectedScaleValueRef?: U.EntityRef, referencing one value admitted by coordinateScaleRef
  expectedScaleValueKindRef?: U.KindRef, referencing the exact kind of that scale value
  expectedScaleRangeRef?: U.EpistemeRef, referencing one range description on coordinateScaleRef
  expectedScaleDirection?: EvaluationScaleDirectionValue
  candidateRepairProposalRefs[]: U.EpistemeRef, each referencing one CandidateImprovementProposalRow@Context
  predictionBasisRefs[]: U.EpistemeRef, each referencing one prediction-basis episteme
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
```

`ExpectedEvaluationChangeExpressionKindValue` is `expectedValue | expectedRange | expectedDirection`. Exactly one of value, range, or direction is present according to that kind. An expected value includes its exact kind and is admitted by `coordinateScaleRef`; an expected range belongs to that scale. `EvaluationScaleDirectionValue` is `increaseOnScale | decreaseOnScale | preserveWithinRange | enterDeclaredRange | leaveDeclaredRange`. Free direction prose does not close this episteme. The episteme predicts a later re-evaluation result. Its edition changes when the object version, bounded context, applicable grounding or viewpoint, declared evaluation use, coordinate, scale, current result, expected value, range, or direction, proposal set, prediction basis, protected trade-offs, claim graph, or reference scheme changes. A carrier or rendering change alone does not change the prediction episteme. It is not an operation, move, transition, work occurrence, or proof of improvement.

`ImprovementLoopDecisionValue` is `stop | continue | switchMethodFamily | openNewFrame | holdUntilInformationBasisSufficient`. The hold value has non-empty `unfilledInformationBasisPositionDescriptionRefs[]` and an `informationBasisSufficiencyConditionRef`; other values leave both absent. Each description says which information-basis position is unfilled without pretending to reference an entity that does not exist. The sufficiency condition says what information would make continuation admissible.

`ImprovementLoopBoundaryCondition@Context` carries `boundaryConditionKind = stop | governingPatternReturn | informationBasisSufficiency`, a condition description, the affected object-version ref and exact kind, and a conditional receiving-pattern ref when the boundary is a governing-pattern return. Source currentness stays with G.11, selected-set publication stays with G.5, work stays with A.15, and evidence and assurance stay with their direct governing patterns.

A visible cycle such as "draft -> evaluate -> repair -> re-evaluate" may be useful before execution. While any position, relation, expected result change, protected trade-off, decision value, or boundary needed for the wider improvement CGUS remains unresolved, keep that presentation as a `ProvisionalUnfoldingDemonstrationDescription@Context` about the object version and proposed continuation set. It may guide slot discovery, but it is not yet a structure or a slice. Admit the wider `ImprovementLoopUnfoldingStructure` first. Only then may a separate `DemonstrativeUnfoldingSlice@Context` select one traversal through that admitted structure and name it as EntityOfConcern. Neither episteme is a `QualityImprovementLoopRecord@Context`, performed work, or proof of improvement.

#### E.23:4.2 - Loop method

For one quality-improvement loop:

1. Declare `ObjectUnderImprovementRef`, its exact kind and version, and one `QualityEvaluationUseDeclaration@Context`. Keep the evaluation performer assignment, governing pattern description, optional semantic method, quality-model descriptions, expected evidence basis, and result-form description in their separate slots.
2. Declare `ImprovementAim`, declared floor or desired substantive evaluation-result change, protected trade-offs, cost and risk account, and local stop condition. Do not declare `5`, all-`5`, or `5-defensible` as the work target; name the content property to improve instead.
3. Use `E.22` to frame the first quality evaluation when the purpose is not already explicit.
4. Run the object-under-improvement evaluation in its declared result form. For one FPF pattern version, this is an E.21 result with every coordinate, every `ShortRationale`, the `PrecisionRestorationProfile`, evidence basis, coordinate-specific payloads, and status. A loop record, profile pass, blocker summary, two-column table, or "no blockers" note is not a substitute.
5. Record row-atomic findings or proposal rows when work is returned. A step is closed only after its finding or proposal row is written; do not rely on memory or a later grouped summary.
6. Apply repairs or variants to the object. Repair below-floor findings first. When exceptional improvement is requested, search coordinate-by-coordinate for substantive content improvements: better positive action guidance, a missing worked slice, case and countercase coverage, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or relocation of quality proof or process proof. Guards, boundary catalogues, relation menus, or quality proof added solely to make a higher value defensible are dominated changes, not improvements. A no-change closure is admissible only when the row cites its `LoopEvaluationEvidenceBasis@Context` and explains why no non-dominated content improvement is available under the protected trade-offs. When generation, selection, publication, parity, refresh, decision, planning, work, evidence, or assurance claims leave quality improvement, keep the pattern that governs that claim, relation, or boundary in the loop record or `Relations`. Do not let loop-method prose replace the object's positive content. For precision-restoration defects, use the selected restoration or governing pattern named by the evaluation: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or an object-specific pattern. Before closure, a bounded complete `KindRestorationCheck` states what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope were present before the edit and what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope the changed text now carries when those items are live. No-op closure is admissible only as `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` with its evidence basis; otherwise unchanged text remains a live finding. When another pattern governs the kind under repair, relation, claim, or position, cite that pattern; `E.23` records the repair and reruns the evaluation, it does not duplicate the restoration algorithm.
7. Re-evaluate the changed object version through the object-under-improvement evaluation, preserving that evaluation's coordinate set, evidence basis, result-row shape, short rationales, attention-discharge rows, and coordinate-specific payloads.
8. Record what improved, what stayed floor-only, what was unchanged by value with its evaluation evidence basis, what became worse, and which rows were reclassified outside the evaluation.
9. Decide `stop`, `continue`, `switchMethodFamily`, `openNewFrame`, or `holdUntilInformationBasisSufficient`.
10. Leave a `QualityImprovementLoopRecord@Context` sufficient for the next reader to replay the object versions, `QualityEvaluationUseDeclaration@Context`, actual `LoopEvaluationEvidenceBasis@Context`, evaluation results, applicable source-use and currentness result references, limitations, trade-offs, cost and risk, and the loop decision with its reason.

#### E.23:4.3 - Stop, continue, and reopen

Stop when the current object version meets the declared floor or improvement aim and no feasible non-dominated proposal remains worth its cost under the current use, comparison set, source state, and protected trade-offs. If the remaining proposal mainly makes a value easier to argue while adding apparatus or worsening use, affordability, locality, source preservation, or ecology, reject that proposal; continue searching for a substantive content improvement if the improvement aim is still open, and stop only with a by-value no-proposal disposition.

Continue only when at least one `ExpectedEvaluationResultChange@Context` states a scale-qualified change worth its cost and risk. Switch method when the current method family is not changing the evaluated result, is too costly, or no longer fits the evaluation. Use `holdUntilInformationBasisSufficient` only with non-empty unfilled-position descriptions and the sufficiency condition that would make continuation admissible.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result closes this loop locally. It does not say that future development is impossible. A new use, `Q` component, source anchor, `SoTA` front, comparison set, affordability boundary, or higher-payoff proposal can open a later loop.

#### E.23:4.4 - Method-family selection

| Method family | Use when |
|---|---|
| `PDSAorPDCAFamily` | Learning quality, baseline comparison, measuring instruments, or standardize-then-repeat action matter for the improvement loop. |
| `POOGIFamily` | The evaluation problem is throughput-shaped or constraint-shaped. |
| `OODAFamily` | Orientation quality and feedback under changing conditions affect the evaluation. |
| `RalphLikeGeneralAdaptiveFamily` | A broadly capable agent can improve the object through repeated specification, feedback, memory, and verification under `C.19.1` cost and risk discipline. |
| `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` | The performer or harness stays fixed while the object version is edited and re-evaluated. |
| `NQDQualitySideImprovementFamily` | The evaluation supplies the `Q` side for a declared NQD and OEE comparison and loop changes seek a non-dominated change in evaluated `Q` coordinates. |
| `SoTAReachAndMaintainFamily` | Reaching or maintaining an externally assigned front depends on composing several accepted source or practice anchors. |
| `SpecializedObjectFamilyCycle` | A specialized method family fits a declared characteristic space and is BLP-compatible. |

The selected family is justified by characteristic-space fit, the declared `ExpectedEvaluationResultChange@Context` values, cost and risk, and protected trade-offs. Familiarity, automation, or current popularity is not enough.

#### E.23:4.5 - Operation-family selection

An operation family is selected only when the loop record names:

1. one scale-qualified `ExpectedEvaluationResultChange@Context`;
2. failure mode addressed;
3. cost or risk reason;
4. protected trade-offs;
5. stop or removal condition.

Typical operation families are specification articulation, task decomposition, context refresh with carry-forward evidence, failure-context retry, verification against specification, memory or distillation, external critic or co-regulation, proposal portfolio use, search breadth or variants, bounded object-change budget, held-out evaluation, rejected-change memory, optimizer-memory separation, source-anchor contribution assignment, agent-tool-interface hardening, and task-family adaptation signature. They remain selectable only for the loop that justifies them.

#### E.23:4.6 - Cost and BLP discipline

`C.19.1` governs the preference for broad, scale-amenable methods when safety, admissibility, and practical fitness are comparable. `E.23` uses that preference but still evaluates end-to-end accepted-work cost:

```text
AcceptedWorkCost ~= resource_cost + tool_and_instrument_cost + adaptation_attempt_cost + skilled_attention_cost + rework_and_delay_cost + risk_exposure - avoided_loss_value
```

This is not a hidden quality score. It is a prompt for cost and risk reasoning. `resource_cost` can include compute, materials, energy, consumables, occupied facilities, or another resource consumed by the declared work; the other terms are interpreted for the actual project rather than presumed to be software costs. If avoided loss is large, an expensive loop can be right. If the object is simple, a direct edit or adjustment, small repair, lower-cost performer, specialized cycle, or one-shot evaluation can be better.

Harness improvement is usually the first high-leverage intervention when it reduces blind retry: better frames, row shapes, test cases, source references, local tools, memory, verification, and stop conditions.

#### E.23:4.7 - Source-composed, OEE, and NQD improvement

Accepted `SoTA` is the working external front only when assigned by the object-under-improvement evaluation, accepted source-use decision, or declared comparison set. `E.23` can govern a loop that reaches, maintains, or improves relative to that front; it does not self-assign `SoTA`.

When an evaluation-result change depends on source use, source currentness, or a dated external front, the loop record cites the exact accepted result from `G.2` or `G.11`, including the edition or date needed for replay. `E.23` carries that reference; it does not make the source-use or currentness decision.

When several source anchors are used, the loop records each exact accepted source-use decision and each source contribution. The changed object's result episteme then carries a `SourceComposedResultClaim` node in its `U.ClaimGraph`, relating the result claim to those decisions and contributions, and the changed object version is re-evaluated.

For NQD and OEE, `E.23` can change one object version or candidate to improve its evaluation result on declared `Q` coordinates. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over novelty, diversity, descriptors, distances, archive or front insertion, pool policy, selected-set publication, parity, and refresh.

### E.23:5 - Worked slices
**Agent harness improvement from a loop-engineering request.** A user asks to "build an agent loop that improves my local DPF seed." The `E.23` entry is not the loop word; it is the recovered object and evaluation use: `ObjectUnderImprovementRef = PersonalDevelopmentDPFSeed@v0.1`; `governingEvaluationPatternDescriptionRef = E.4.DPF.DA or E.21`; the separate quality-model, expected-evidence-basis, and result-form refs are those declared by that pattern; and `ImprovementAim = make the seed usable as a local first-entry framework without public-Core claims`. The loop may change only the declared seed version, or a declared evaluation or harness slice that is itself the object under improvement. Source-use prompts, pattern-seed expansion, adversarial examples, or harness checks enter the loop only when the record states an `ExpectedEvaluationResultChange@Context` and a removal or stop condition for that declared slice. Source-use decisions are `G.2`; source decay, edition change, and refresh orchestration are `G.11`; the harness run itself is `U.Work`; parity between harness variants is `G.9`; retained candidate variants are `C.18` or `C.19`; selected-set publication is `G.5`; PFAD and PFR claims stay with `E.4.PFAD` and `E.4.PFR`. A change outside the declared slice opens that neighboring work; it is not one giant `E.23` evolution loop.

**Affordable floor evaluation.** A pattern needs admission readiness. E.22 frames `floorEvaluation`; E.21 evaluates its complete coordinate set. If the result is admissible and no improvement aim is requested, E.23 stays closed. If an admission, refresh, landing, or release crossing is claimed, E.19 and the release process named by value still check the gate conditions; the E.21 status is necessary quality evidence, not the gate itself.

**Pattern exceptional improvement.** A pattern already passes floor but lacks worked slices and source-currentness. Use `E.22` to frame optional exceptional improvement for named coordinates. The practitioner then applies `E.23`: search for substantive non-dominated content improvements, apply proposal rows, re-evaluate the changed pattern through `E.21`, check what became worse, and stop locally only when no worthwhile content improvement remains under the declared use. The loop may stop at `4`, but only after the missing-exceptional opportunity has been searched and discharged by value; it is not a proof-building run toward all-`5`.

**Physical prototype improvement.** The object version is `PumpAssembly@Prototype-3`, kind `U.System`. Its `QualityEvaluationUseDeclaration@Context` keeps six positions distinct: a vibration-test engineer role assignment performs the evaluation; a pump-vibration evaluation pattern description governs it; a steady-operating-point vibration evaluation method is the semantic method; an engineering Q-Bundle description and characteristic-space specification define RMS vibration, efficiency, and manufacturability coordinates and scales; an expected-evidence-basis episteme names calibrated test-bench measurements at declared operating points; and a result-form episteme describes the coordinate rows. An E.22 proposal describes an impeller-geometry change while its `TradeoffProtectionSet@Context` retains efficiency and manufacturability. The E.23 loop description carries an `ExpectedEvaluationResultChange@Context` with the current result, `changeExpressionKind=expectedDirection`, and `expectedScaleDirection=decreaseOnScale`. Dated machining and assembly of Prototype-4 remain A.15 work. The loop cannot claim improvement until Prototype-4 is evaluated by the declared method on the same characteristic space and evidence basis.

**Three proposals remain three evaluated alternatives.** Under that same evaluator assignment, evaluation method, quality model, and expected evidence basis, E.22 can return three exact `CandidateImprovementProposalRow@Context` values: change impeller geometry, change bearing-support stiffness, and add vibration isolation. The `QualityImprovementLoopRecord@Context` cites all three rows without merging them into one repair summary. Each row has its own `ExpectedEvaluationResultChange@Context` whose `entityOfConcernRef` names the pump-assembly version expected to change, whose prediction uses an admitted scale, and whose protected-trade-off membership remains separate, such as efficiency, mass, manufacturability, or service access. If comparable operating-point measurements are missing, the actual `LoopEvaluationEvidenceBasis@Context` names that unfilled position. None of the predictions selects a proposal: `holdUntilInformationBasisSufficient` states the comparability condition. A later pass may continue only from proposals whose expected change remains worth cost and risk after that position is filled.


**DRR improvement.** A `DRR` needs drafting adequacy for authoring across several selected pattern hosts. Use the coordinates supplied by `E.9.DA`, apply decision repairs through the `E.23` method, and re-evaluate the changed `DRR` through `E.9.DA`. The improved object is still a decision record, not prewritten pattern prose.

**NQD quality-side improvement.** A generated candidate has declared `Q` components and a comparison set. `E.22` returns proposal rows. `E.23` may change the candidate and re-evaluate `Q`; archive or front insertion, selected-set publication, parity, and refresh remain under the pattern that governs each claim and are not quality-loop decisions.

### E.23:6 - Bias annotation

This pattern biases FPF toward adaptive improvement with explicit re-evaluation. The bias is useful because many real objects improve only through feedback and revision.

The bias is bounded. One direct evaluation can close without a loop. Repetition is justified only by a scale-qualified `ExpectedEvaluationResultChange@Context` and acceptable cost and risk.

### E.23:7 - Conformance checklist

| Check | Passing condition |
|---|---|
| `CC-E23-1` | Name object version and object-under-improvement named by value evaluation before claiming a changed evaluation result. |
| `CC-E23-2` | Use `E.22` or an equivalent frame when the evaluation purpose is not already explicit. |
| `CC-E23-3` | Represent returned work as row-atomic E.22 findings or proposal rows with closure tests; pair proposals selected for the next pass with scale-qualified `ExpectedEvaluationResultChange@Context` values. A grouped memory summary does not discharge skipped rows. |
| `CC-E23-4` | Re-evaluate the changed object version before claiming coordinate, status, or `Q` change, or a changed front relation. |
| `CC-E23-5` | Record what became worse and protected trade-offs. |
| `CC-E23-6` | Continue only when a scale-qualified expected evaluation-result change and the cost and risk account support another pass. |
| `CC-E23-7` | Treat all-`5`, exceptional, or front-reaching results as local loop stops, not permanent maturity endings. |
| `CC-E23-7a` | Do not treat `5`, all-`5`, or `5-defensible` as a repair target. Repair below-floor results first. Exceptional-improvement work proceeds through non-dominated proposal rows that name the expected substantive content change, protected trade-offs, and cost and risk. A no-proposal or stay-at-current-value disposition is admitted only when it cites the `LoopEvaluationEvidenceBasis@Context` and explains why every plausible content improvement is dominated, unavailable, or outside the declared scope. Reject changes that add guards, relation catalogues, evidence theatre, or quality proof while reducing use, affordability, locality, or ecology. |
| `CC-E23-8` | When a neighboring claim appears during a loop, name the live claim and its direct governing pattern before continuing. `E.23` may cite that pattern in the loop record, but it does not absorb the neighbor's authority unless the neighbor's object version is itself the declared object under improvement. |
| `CC-E23-8a` | When the evaluation names a precision-restoration defect, apply the selected restoration or governing pattern named by that evaluation. For `E.21`, use its `PrecisionRestorationProfile` to decide whether the repair concerns word, head, or use precision (`E.10`, `E.10.ARCH`, `F.18`), phrase-level plain rewriting (`F.19`), or a governing-pattern repair. The repair row is not closed until it includes a `KindRestorationCheck`: kind, relation, current ontic slot, relation position, use relation or claim kind, admissible use, and scope before and after repair; or a `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` disposition with its evidence-basis references. |
| `CC-E23-9` | Apply `E.10` to load-bearing loop names, status values, examples, stop conditions, and result wording introduced or repaired by the loop. |
| `CC-E23-10` | Preserve the named evaluation's evidence basis, result-row shape, short-rationale rule, attention-discharge rows, and coordinate-specific payloads in every re-evaluation. |
| `CC-E23-11` | If a practitioner entry phrase such as "loop engineering", "agent loop", or "harness loop" appears, lower it to object version plus object-under-improvement evaluation before opening `E.23`, or name the direct neighboring governing pattern and stop the `E.23` overread. |
| `CC-E23-12` | In agent or harness cases, state which slice the loop may change: the target object version, the evaluation, or the harness object. Any other slice becomes neighboring work under its own governing pattern, not implicit `E.23` scope. |

### E.23:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Checklist closed, quality improved.** Discharge count replaces re-evaluation. | Re-evaluate the changed object. |
| **Loop result without evaluation form.** The loop says the object improved but records only prose, applied rows, or values without the named evaluation's evidence basis. | Re-run the object-under-improvement evaluation in its declared result-row shape. |
| **Agentic retry as method law.** Repetition continues without a scale-qualified predicted evaluation-result change. | Add `ExpectedEvaluationResultChange@Context`, cost and risk, trade-offs, and a stop or switch condition. |
| **Operation-family creep.** Verification, memory, supervision, or search is added everywhere. | Keep only operations that can change the evaluation result enough to justify cost. |
| **Goodharted pass.** Visible values rise while protected qualities worsen, or a non-`5` value is treated as a defect to be fixed by more apparatus. | Use trade-off inspection; apply `E.13` when the visible value is replacing the intended value; reject, delete, split, relocate, or hold dominated changes; continue searching for substantive content improvement when the improvement aim is still open; record `stay at current value` only when the `LoopEvaluationEvidenceBasis@Context` shows that no non-dominated content improvement remains. |
| **Lexical substitution closure.** A trigger word disappears, but the replacement narrows, widens, or changes the object kind; for example a graph-shaped method or workflow cue becomes a work sequence without a selected ontology decision. | Reopen the row, recover the pre-repair and post-repair kind through `E.10`, `F.19`, `F.18`, or the governing pattern, and leave the repair blocking if the kind cannot be preserved or explicitly changed by accepted decision. |
| **Maturity-ceiling stop.** All-`5` is treated as end of development. | Close this loop locally and record reopen conditions. |
| **SoTA citation as self-assignment.** Sources are cited as proof of frontier quality. | State source contributions and re-evaluate the composed result. |
| **Loop engineering as ontology.** A fashionable source phrase is treated as a new Core kind or as proof that all repeated activity is one improvement loop. | Use the phrase only as an entry cue; recover object version and evaluation, or send the live claim to its direct governing pattern. Common exits are work, gates, evolutionary retention and publication, source use, refresh, transformation-flow, and DPF governing patterns. |

### E.23:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Repeated improvement is governed by one explicit improvement method. | FPF no longer relies on hidden authoring habits. | A complete loop record names its object and evaluation. |
| Row discharge is separated from evaluated quality change. | Improvement claims become replayable. | The claim remains inadmissible until the changed object is re-evaluated. |
| General and specialized loops are comparable. | BLP can be applied without craft folklore. | Comparison is admitted with explicit cost, risk, and characteristic-space fit. |
| Exceptional stop remains local. | All-`5` or front-reaching closure no longer freezes future development. | The closure record includes its reopen conditions. |

### E.23:10 - Rationale

The shared method is simple: change an object version, re-evaluate it by the exact evaluation that gives values, check trade-offs and cost, then stop, continue, switch method, open a new frame, or hold. Classical improvement cycles, agentic loops, fixed-performer optimization, MCDA, Goodhart, and OEE and NQD lines contribute useful operations and boundaries, but they do not replace this method.

### E.23:11 - SoTA-Echoing

| Claim | Exact source and status | Inherited contribution and limit | Local adoption and disciplined case |
|---|---|---|---|
| Repeated improvement needs an aim, explicit measures, tested changes, and learning from each pass; merely naming a cycle is insufficient. | Gerald Langley et al., *The Improvement Guide: A Practical Approach to Enhancing Organizational Performance*, 2nd ed. (Jossey-Bass, 2009), ISBN 9780470430880, retained historical Model-for-Improvement practice; Michael Taylor et al., *Systematic review of the application of the plan-do-study-act method to improve quality in healthcare*, *BMJ Quality & Safety* 23, 290-298 (2014), DOI 10.1136/bmjqs-2013-001862; Julie Reed and Alan Card, *The problem with Plan-Do-Study-Act cycles*, *BMJ Quality & Safety* 25, 147-152 (2016), DOI 10.1136/bmjqs-2015-005076. | Langley et al. contribute aim-measure-change questions and iterative tests. Taylor et al. and Reed/Card show that key iterative, prediction, data-use, and documentation features are often weakly implemented. The evidence is largely healthcare process improvement and does not establish one universal lifecycle. | E.23 requires a declared evaluation use, proposal or prediction, re-evaluation on the same quality model, evidence basis, trade-offs, and a stop or hold decision. The **Affordable floor evaluation** slice stays one-pass when no repeated improvement claim is live. |
| Formative feedback supports improvement only when the current condition, desired condition, and actionable next move remain connected. | D. Royce Sadler, *Formative assessment and the design of instructional systems*, *Instructional Science* 18, 119-144 (1989), DOI 10.1007/BF00117714; John Hattie and Helen Timperley, *The Power of Feedback*, *Review of Educational Research* 77(1), 81-112 (2007), DOI 10.3102/003465430298487. Both are retained historical education lineages. | The works support gap comparison and next-step feedback, not an FPF loop ontology, a selected work plan, or proof that a proposed change improved the object. | E.22 proposal rows and E.23 `ExpectedEvaluationResultChange@Context` keep current result, candidate change, predicted effect, and later measured result distinct. The **Pattern exceptional improvement** slice requires re-evaluation after applying proposals. |
| Reflection, self-feedback, action-observation coupling, and tree search are different adaptive mechanisms, not synonyms for one loop kind. | Noah Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*, arXiv:2303.11366; Aman Madaan et al., *Self-Refine: Iterative Refinement with Self-Feedback*, arXiv:2303.17651; Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, arXiv:2210.03629; Andy Zhou et al., *Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models*, arXiv:2310.04406; John Yang et al., *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*, arXiv:2405.15793. These are retained 2022-2024 stepping stones. | Reflexion uses linguistic feedback memory, Self-Refine iterates self-feedback and output revision, ReAct interleaves reasoning and environment action, LATS adds tree search and environment feedback, and SWE-agent engineers a software-environment interface. Their benchmark gains do not imply that every retry changes an object version or satisfies E.23 comparability. | `RalphLikeGeneralAdaptiveFamily` is selected only when a declared object version is changed and re-evaluated. The **Agent harness improvement** slice sends performed execution, tool use, and work to their direct patterns rather than calling them one E.23 loop. |
| Current harness practice shows both useful operation families and failure from excessive structure. | Boyuan Wang et al., *Harnesses for Inference-Time Alignment over Execution Trajectories*, arXiv:2605.21516 (2026); Wenze Wang, Mehdi Hosseinzadeh, and Feras Dayoub, *A Physical Agentic Loop for Language-Guided Grasping with Execution-State Monitoring*, arXiv:2604.07395 (2026); Roxana Geambasu et al., *Engineering Robustness into Personal Agents with the AI Workflow Store*, arXiv:2605.10907 (2026). These are current preprints for distinct agent settings. | The first separates decomposition from guided execution and reports over-decomposition, over-pruning, and effective partial harnesses; the second contributes bounded physical monitoring, retry, escalation, and finite termination around one grasp primitive; the third proposes hardened reusable workflows to trade flexibility for robustness. None establishes a general-purpose FPF loop kind or says more harness is always better. | Operation families enter E.23 only with expected evaluation-result change, cost, failure mode, and stop or removal condition. The **Agent harness improvement** boundary keeps physical recovery, hardened workflow reuse, and object-version improvement as distinct claims. |
| A fixed performer can improve through bounded edits to an external method-description object while performer and optimizer remain distinct. | Yifan Yang et al., *SkillOpt: Executive Strategy for Self-Evolving Agent Skills*, arXiv:2605.23904 (2026), current preprint. | SkillOpt keeps the target model fixed while a separate optimizer makes bounded edits to one external skill document, accepts only held-out improvement, and keeps rejected-edit memory. Its evidence concerns text skills, selected benchmarks, models, and harnesses; it does not establish the same gains for arbitrary methods, physical systems, or roles. | `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` keeps performer, mutable object, optimizer memory, validation evidence, and acceptance rule separate. The **Agent harness improvement** slice may use this family only when the skill or document version is the declared object under improvement. |
| Trade-off evaluation asks which coordinates improve and which worsen; domain-specific review methods are examples, not the universal ontology. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, DOI 10.1016/j.swevo.2025.102240 (2026), current survey; Rick Kazman, Mark Klein, and Paul Clements, *ATAM: Method for Architecture Evaluation*, CMU/SEI-2000-TR-004 (2000), retained historical software-architecture practice; David Manheim and Scott Garrabrant, *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585 (2018), later proxy-overoptimization taxonomy. | QD/MOO supports set-valued multi-coordinate comparison; ATAM shows scenario-based exposure of architectural quality-attribute trade-offs but is software-architecture-specific and not current general evolutionary architecture; Goodhart variants warn that optimization pressure can invalidate a proxy. | Every pass records protected trade-offs and what became worse. The **Physical prototype improvement** and **Three proposals** slices preserve RMS vibration, efficiency, manufacturability, mass, and service access without turning any one coordinate into a universal score. |
| Proxy optimization and strategy surrogation are different reasons not to target all-`5` or evaluator-preferred apparatus. | Charles Goodhart, *Problems of Monetary Management: The U.K. Experience* (1975), retained historical monetary-control formulation; Donald T. Campbell, *Assessing the Impact of Planned Social Change*, Occasional Paper 8 (1976), retained social-indicator warning; David Manheim and Scott Garrabrant, *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585 (2018), later taxonomy; Jongwoon Choi, Gary Hecht, and William Tayler, *Lost in Translation: The Effects of Incentive Compensation on Strategy Surrogation*, *The Accounting Review* 87(4), 1135-1164 (2012), peer-reviewed experimental evidence. | The common comparison question is whether stronger optimization of the visible measure still improves the intended value. The sources do not forbid measurement; they require attention to mechanism, behavior change, and proxy substitution. | E.23 forbids score-proof targeting, rejects apparatus-only changes as dominated, protects other qualities, and opens `E.13` when the visible target replaces intended value. The **Goodharted pass** repair is the direct boundary. |
| OEE and NQD improvement is relative to declared `Q`, comparison sets, and behavioral or descriptor spaces. | Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Qin et al., *A survey on Quality-Diversity optimization*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | The works support collections of high-performing alternatives and explicit descriptor spaces. They do not give E.23 authority over candidate generation, archive insertion, front maintenance, pool policy, or selected-set publication. | `NQDQualitySideImprovementFamily` changes and re-evaluates one declared object version on `Q`; the **NQD quality-side improvement** slice returns retention and publication claims to C.17-C.19 and G.5. |
| A synthesis claim should expose how each admitted source contributes and which synthesis method and limitations apply. | Joanne McKenzie and Sue Brennan, *Cochrane Handbook for Systematic Reviews of Interventions*, version 6.5 (2024), Chapter 12, is current evidence-synthesis guidance; FPF `G.2` and `G.11` are the current internal governors for source-use decisions and source currentness. | Chapter 12 requires the chosen synthesis method and limitations to be reported instead of using an unexplained narrative-synthesis label. Its healthcare evidence hierarchy and statistical methods are not imported into arbitrary FPF projects. FPF contributes source-use and edition-currentness relations across domains. | `SourceComposedResultClaim` is a claim-node form that relates the changed result to exact accepted source-use decisions and contribution descriptions. E.23 re-evaluates that result; it does not infer front reach from citation count or from the mere presence of several sources. |

### E.23:12 - Relations

| Pattern | Relation |
|---|---|
| `A.19.ECS` | Constructs or repairs an object-under-improvement evaluation when none exists. |
| `E.22` | Frames each quality evaluation and can return finding or proposal rows. |
| `E.21` | Supplies pattern-quality values for pattern-improvement loops. |
| `E.9.DA` | Supplies `DRR` decision-adequacy values for `DRR` loops. |
| `E.2.DA` | Supplies FPF Pillar-adequacy values for corpus-level loops. |
| `A.22.CGUS` | Supplies the unfolding structure when one review or replay use inspects object version, evaluation frame, E.22 proposal refs, protected trade-offs, expected evaluation-result changes, and the loop-decision value together. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when loop targets, quality values, metrics, or review results become substitutes for the intended value. |
| `G.2` | Governs source-use and source-pack return before DPF seeds based on source-use records, admitted source publications, agent-practice claims, or source-composed improvement claims can be used as evidence. |
| `F.18` | Supplies durable-name evaluation for naming loops. |
| `C.25`, `C.16.Q` | Govern engineering quality bundles and quality-word precision repair. |
| `C.19.1` | Governs BLP and cost and risk comparison for method-family choice. |
| `C.22.1`, `C.24` | Govern durable task-family adaptation and tool-call planning when the loop makes those claims. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE and NQD candidate characteristics, archive, front, pool, selected set, parity, and refresh. |
| `E.18` | Governs cyclic transformation-flow structures, paths, gates, and slice-local refresh; a cyclic transformation-flow structure is not a quality-improvement method unless an object version is changed and re-evaluated under `E.23`. |
| `E.18.1` | Carries accepted problem-side records or generated seed records toward the next FPF relation, including DPF seed-to-hardening routes before a quality-improvement loop is ready. |
| `E.4.DPF` | Governs DPF authoring routes and publication carriers when a fast local framework seed is the object being carried toward use or admission. |
| `E.4.PFAD`, `E.4.PFR` | Govern framework architecture decisions and framework relation records; `E.23` may improve a declared artifact version but does not decide those framework slots. |
| `A.21` | Governs gate-decision publication; monitoring, retry, escalation, or a green harness state does not publish gate passage unless an `OperationalGate(profile)` gate-decision relation is present. |
| `C.32.P2S` | Uses improvement-loop results only when they reopen architecture problem-to-structure carry-through; E.23 still governs the loop record and re-evaluation. |
| `C.11`, `A.10`, `B.3`, `A.15`, `A.20`, `A.21` | Govern decision, evidence, assurance, work, gate, and release claims when a loop result is reused beyond quality improvement. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by loop records. |

### E.23:End

