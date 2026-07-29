## E.22 - Improvement-Oriented Quality Evaluation Question Framing

Status: Core.

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or follow-up hypothesis over an object version named by value, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. The governing evaluation pattern description names the method to apply; an optional semantic evaluation method is the method itself. A characteristic-space specification, Q-Bundle description, rubric description, review-profile description, evidence-basis description, and result-form description constrain or describe that evaluation. None of those specifications performs the evaluation or substitutes for its governing method. For example, `E.21`, `E.9.DA`, or `E.2.DA` may govern evaluation of one FPF object, while `A.19.ECS` and `C.25` supply supporting quality-model descriptions. `E.19` instead governs an admission or refresh review gate and findings profile. Use `E.19` as the evaluation method only when its review result is itself the object under evaluation; otherwise its later gate check remains distinct from the quality evaluation.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame@Context` naming the object version and a `QualityEvaluationUseDeclaration@Context`. In that declaration, name the governing evaluation pattern separately from its quality-model, evidence-basis, and result-form descriptions; then state the purpose, floor or improvement aim, and protected trade-offs.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming a changed evaluation result, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

What this buys in practice: requester and evaluator start with the same object version, evaluation purpose, value source, protected trade-offs, evidence basis, and result form. A small floor question can stay small, while a request for proposals or trade-off analysis returns the additional information needed for a later improvement decision.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

### E.22:2 - Problem

Quality evaluations fail when the evaluator has to infer the question. The same object can be checked for floor adequacy, improved toward exceptional expression, compared across trade-offs, mined for open questions, or evaluated after finding absorption. Those purposes produce different findings.

The defect is not that reviewers need more ceremony. The defect is that an unframed question hides the object under improvement, the evaluation that supplies values, and the allowed shape of returned work.

### E.22:3 - Forces

| Force | Tension |
|---|---|
| Cheap readiness vs ambitious improvement | A floor evaluation should be short; exceptional improvement needs richer proposals. |
| Explicit purpose vs reviewer discovery | The request names the purpose, while the reviewer can still report important unasked questions. |
| Evaluation vs follow-up action | A useful evaluation may suggest a follow-up, but the suggestion remains a hypothesis until the pattern that governs the claim, relation, or boundary is applied. |
| Multi-coordinate gain vs Goodhart risk | Raising one visible value can damage usability, affordability, locality, source preservation, or corpus ecology; use `E.13` when the visible value or metric is being treated as the intended value itself. |
| Proposal portfolio vs selected result | Several candidate improvements may be useful without becoming a selected set, pool policy, front insertion, parity, or refresh result. |

### E.22:4 - Solution

`E.22` gives one compact declaration for improvement-oriented quality evaluation questions. It keeps the question from replacing the evaluation and keeps the evaluation result from becoming a decision or work product beyond its authority.

#### E.22:4.1 - Local names and kind settlement

The evaluation method and the descriptions it uses occupy different positions. `QualityEvaluationUseDeclaration@Context` keeps those positions together for one intended evaluation without collapsing their kinds.

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation; its ClaimGraph carries the requested quality-evaluation question about that version. |
| `QualityEvaluationUseDeclaration@Context` | `U.Episteme` whose EntityOfConcern is the same exact object version. It describes how evaluation of that version is to be performed and interpreted, referring separately to the performer assignment, governing pattern description, optional semantic method, quality-model descriptions, expected evidence basis, and result form. |
| `ObjectVersionUnderQualityEvaluation` | Exact `U.Entity` version being evaluated, paired with its exact `U.Kind`. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or distinguishable combination of purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested substantive change beyond the floor when improvement beyond the floor is requested. |
| `ExpectedEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation. It describes the evidence-use positions and missingness rule expected when the named governing evaluation pattern evaluates that version in the stated qualification window. It can be identified before a use declaration cites it and is not the evidence values later found. |
| `TradeoffProtectionSet@Context` | A local `U.Set` value whose members are exact characteristic or coordinate references paired with their kinds. Its identity is extensional within the question context. |
| `EvaluationQualificationWindow` | Edition, source-currentness, comparison-set, time, or declared-use window in which the requested result is intended to be current. |
| `ExpectedQualityEvaluationResultFormDescription` | `U.Episteme` describing the result-row form declared by the governing evaluation pattern. |
| `QualityReviewFindingRow` | Actionable evaluation finding that identifies the observed issue, affected evaluation property, correction direction, and closure test. |
| `CandidateImprovementProposalRow@Context` | E.22 proposal episteme with an exact correction target, expected substantive evaluation effect, trade-offs, kind-restoration disposition, outside-claim return when needed, and closure test. |
| `CandidateImprovementOutsideClaimReference@Context` | Bounded local ClaimGraph node form inside one proposal row. It identifies the outside governed value, relation signature, or boundary description and the exact method description that governs the return. It is not an episteme, relation, or independently referenceable entity. |
| `KindRestorationCheck` | Conditionally present check when a finding or proposal changes wording, naming, or precision-restoration content. |
| `CandidateImprovementProposalPortfolio@Context` | A local `U.Set` value whose members are `CandidateImprovementProposalRow@Context` epistemes for one question frame. Membership, not a document serialization, determines the portfolio. |
| `ImprovementFollowUpHypothesis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version expected to change. It claims that one named next operation or method application is expected to address one finding and produce a stated evaluation effect under a stated test condition. A stop disposition, return, or selected plan is not such a hypothesis. |

```text
QualityEvaluationUseDeclaration@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  evaluationPerformerRoleAssignmentRef?: U.EntityRef, referencing one U.RoleAssignment
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing one U.MethodDescription
  semanticEvaluationMethodRef?: U.MethodRef, referencing the U.Method described by the governing pattern
  evaluationCharacteristicSpaceSpecDescriptionRef?: U.EpistemeRef, referencing one A.19.ECS specification description
  evaluationQBundleDescriptionRef?: U.EpistemeRef, referencing one C.25 Q-Bundle description
  evaluationRubricDescriptionRef?: U.EpistemeRef, referencing one evaluation-rubric description
  evaluationReviewProfileDescriptionRef?: U.EpistemeRef, referencing one evaluation-review-profile description
  expectedEvaluationEvidenceBasisRef: U.EpistemeRef, referencing one ExpectedEvaluationEvidenceBasis@Context
  expectedEvaluationResultFormDescriptionRef: U.EpistemeRef, referencing one ExpectedQualityEvaluationResultFormDescription

ExpectedEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose evaluation needs the expected evidence
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  governingEvaluationPatternDescriptionRef: U.EntityRef, referencing one U.MethodDescription
  expectedEvidencePositionDescriptionRefs[1..*]: U.EpistemeRef, each referencing one evidence-position description
  expectedEvidenceRelationKindRefs[1..*]: U.KindRef, each referencing one expected evidence-relation kind
  missingEvidenceDispositionRuleRef: U.EpistemeRef, referencing one U.MethodDescription that states the missing-evidence disposition rule
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
```

Every field above with a `*Ref` suffix stores the stated A.6.5 `RefKind`; resolving it yields the referent kind named after `referencing`. The use declaration and expected evidence basis carry the same exact object-version value in `entityOfConcernRef`. The expected basis does not point back to the declaration: it can be created from the object version, governing evaluation-pattern description, expected evidence positions and relation kinds, missingness rule, and qualification window; the declaration is then created with a reference to that completed basis. This construction removes the former mutual dependency.

`evaluationPerformerRoleAssignmentRef` identifies who is assigned to perform the evaluation; it is neither the method nor the object being evaluated. `governingEvaluationPatternDescriptionRef` identifies the FPF pattern or other method description that governs the evaluation. `semanticEvaluationMethodRef`, when recoverable, identifies the method described by that pattern. The characteristic-space, Q-Bundle, rubric, and review-profile references identify epistemes that specify the quality model or its use; they do not supply an actor and do not become alternative values of a method slot.

Two carriers may publish the same edition of either episteme. A `QualityEvaluationUseDeclaration@Context` changes edition when its exact object version, bounded context, applicable grounding or viewpoint, claim graph, reference scheme, performer assignment, governing pattern description, semantic method, quality-model descriptions, expected evidence-basis edition, or result-form description changes. An `ExpectedEvaluationEvidenceBasis@Context` changes edition when its object version, bounded context, applicable grounding or viewpoint, governing pattern description, expected evidence positions or relation kinds, missingness rule, qualification window, claim graph, or reference scheme changes. Carrier or support serialization alone changes neither episteme. `TradeoffProtectionSet@Context` and `CandidateImprovementProposalPortfolio@Context` are set values, not records; an episteme may describe or publish either set without becoming the set.

#### E.22:4.2 - Quality evaluation purposes

| Purpose value | Use when | Expected result |
|---|---|---|
| `floorEvaluation` | The question is whether the object reaches a declared floor. | Values below floor, first repair, architecture hold, refresh, new-frame assignment, or admissible stop. |
| `exceptionalImprovementEvaluation` | The floor is reached and the requester wants non-dominated improvement toward exceptional expression. | Per-coordinate proposal or no-candidate disposition. |
| `paretoTradeoffEvaluation` | A candidate change may improve some values while worsening protected qualities. | Trade-off account and non-dominated comparison. |
| `candidateImprovementProposalEvaluation` | The requester needs candidate-change proposals before changing the object or generating variants. | Proposal row or bounded proposal portfolio with an expected effect on the later evaluation result. |
| `openQuestionDiscoveryEvaluation` | The requester wants important unasked questions surfaced. | Question classified as existing-coordinate issue, candidate future coordinate, or outside-evaluation issue. |
| `absorptionEvaluation` | Returned findings or suggestions have been applied or rejected. | Quality-impact account over the changed object. |

Purposes can be combined, but the result keeps them distinguishable. A floor result does not answer exceptional improvement. Absorption count does not establish a changed evaluation result. A proposal is not a selected work item.

#### E.22:4.3 - Question frame
An improvement aim is not a command to make every coordinate exceptional. A `5` is assigned only by the named evaluation after the changed object earns it. The frame may ask for substantive non-dominated proposals that could move named coordinates toward exceptional expression, while admitting `no proposal` or `stay at current value` when every plausible change would add apparatus, proof prose, boundary catalogues, or process evidence while damaging protected qualities. That no-proposal result needs checked review locations and evidence-basis references; it is not a cheap refusal to improve.

```text
QualityEvaluationQuestionFrame@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration@Context about the same object version
  evaluationPurposeSelection: QualityEvaluationPurposeSelectionValue
  declaredQualityFloorDescriptionRef?: U.EpistemeRef, referencing one declared-quality-floor description
  desiredImprovementAimDescriptionRef?: U.EpistemeRef, referencing one desired-improvement-aim description
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  nonUseBoundaryDescriptionRef: U.EpistemeRef, referencing one non-use-boundary description
```
The shortest floor frame names the object version, one `QualityEvaluationUseDeclaration@Context`, purpose `floorEvaluation`, and the declared floor. The declaration may cite defaults supplied by the governing evaluation pattern for its characteristic space, evidence basis, result form, and qualification window. If the question depends on another edition, source state, comparison set, time window, or declared use, state that window explicitly. For one FPF pattern version under E.21, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, scope narrowing, or a blocker-only substitute result.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame@Context`; do not report the current request as passed under an easier scope.

#### E.22:4.4 - Finding and proposal rows

An actionable finding first identifies where an issue was observed, which exact entity would change, the affected evaluation characteristic or coordinate, the current evaluation result for that characteristic or coordinate when known, the proposed correction, and the closure test. A proposal adds a typed expected evaluation effect, protected trade-offs, and any outside claim together with its return to the direct governing pattern.

```text
CandidateImprovementProposalRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under improvement
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context about the same object version
  reviewLocationDescriptionRef: U.EpistemeRef, referencing one description of the observed location in the reviewed object
  correctionTargetRef: U.EntityRef, referencing the exact entity proposed to change
  correctionTargetKindRef: U.KindRef, referencing the exact kind of the correction target
  affectedEvaluationCharacteristicOrCoordinateRef: U.EntityRef, referencing one governed characteristic or evaluation coordinate
  affectedEvaluationCharacteristicOrCoordinateKindRef: U.KindRef, referencing its exact kind
  currentAffectedEvaluationResultRef?: U.EntityRef, referencing the current result value for that characteristic or coordinate
  currentAffectedEvaluationResultKindRef?: U.KindRef, referencing the exact kind of that result value
  expectedSubstantiveEvaluationEffect: ProposalEvaluationEffectValue
  proposedCorrectionDescriptionRef: U.EpistemeRef, referencing one correction description
  kindRestorationCheckDisposition: ProposalKindRestorationCheckDispositionValue
  kindRestorationCheckRef?: U.EpistemeRef, referencing one KindRestorationCheck result
  expectedTradeoffRefs[]: U.EpistemeRef, each referencing one expected-trade-off description
  outsideClaimReferences[]?: CandidateImprovementOutsideClaimReference@Context by value
  closureTestRef: U.EpistemeRef, referencing one closure-test description

CandidateImprovementOutsideClaimReference@Context in CandidateImprovementProposalRow@Context.claimGraph:
  outsideClaimOrBoundaryDescriptionRef: U.EpistemeRef, referencing one description of the outside claim or boundary
  outsideValueRef?: U.EntityRef, referencing the exact outside governed value
  outsideValueKindRef?: U.KindRef, referencing the exact kind of that outside value
  outsideRelationSignatureRef?: U.EntityRef, referencing the exact U.Signature of the outside relation
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  returnConditionDescriptionRef: U.EpistemeRef, referencing one description of the condition for returning to that governing pattern
```

```text
ImprovementFollowUpHypothesis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version expected to change
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  boundedContextRef: U.BoundedContextRef
  groundingHolonRef?: U.HolonRef
  viewpointRef?: U.ViewpointRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame@Context about the same object version
  qualityReviewFindingDescriptionRef: U.EpistemeRef, referencing one episteme that describes the exact QualityReviewFindingRow
  proposedNextOperationDescriptionRef?: U.EpistemeRef, referencing one operation description
  proposedNextMethodRef?: U.MethodRef, referencing one U.Method
  expectedEvaluationEffectDescriptionRef: U.EpistemeRef, referencing one expected-evaluation-effect description
  testConditionDescriptionRef: U.EpistemeRef, referencing one test-condition description
```

Exactly one of `proposedNextOperationDescriptionRef` and `proposedNextMethodRef` is present. The question frame, proposal row, and follow-up hypothesis preserve the same exact object-version EntityOfConcern unless a proposal explicitly opens a new frame for a different version. `QualityEvaluationQuestionFrame@Context` changes edition when the object version, bounded context, applicable grounding or viewpoint, use declaration, purpose, floor or aim, trade-off set, qualification window, non-use boundary, claim graph, or reference scheme changes. A proposal row changes edition when its bounded context, applicable grounding or viewpoint, frame, correction target, affected evaluation coordinate, proposed correction, expected effect, trade-offs, outside-claim nodes, closure test, claim graph, or reference scheme changes. A follow-up hypothesis changes edition when its bounded context, applicable grounding or viewpoint, frame, finding description, proposed operation or method, expected effect, test condition, claim graph, or reference scheme changes. Carrier and serialization changes alone do not change any of these epistemes.

`ProposalEvaluationEffectValue` is the closed local value set `repairFloor | raiseTowardExceptional | preventProtectedQualityLoss | classifyOutsideEvaluation | preserveCurrentValue`. It identifies the coarse substantive evaluation effect expected from this proposal. It does not duplicate the coordinate-qualified prediction later carried by E.23 `ExpectedEvaluationResultChange@Context`.

`ProposalKindRestorationCheckDispositionValue` is `triggered | notTriggered | ordinaryProse | alreadySatisfied | blocker`. The `triggered` and `blocker` states include `kindRestorationCheckRef`; the other values leave it absent. Current affected-evaluation result ref and kind are both present or both absent; the exact kind recovers whether the named evaluation returned a scale value, status, or another admitted result for that characteristic or coordinate. Outside value ref and kind are paired, and `outsideRelationSignatureRef` is present when the outside value is a relation. `CandidateImprovementOutsideClaimReference@Context` is a bounded local ClaimGraph node form, not a U-kind, episteme, relation, or relation-reference episteme. It is constructed inside one proposal row without a back-reference to that row; its node identity is determined by the containing proposal edition and ClaimGraph position.

`reviewLocationDescriptionRef` describes where the issue was observed in the reviewed object. `correctionTargetRef` identifies the exact entity that would change. They are not interchangeable positions. The row is a faithful typed proposal form of `QualityReviewFindingRow` and one possible member of a `CandidateImprovementProposalPortfolio@Context` set. It remains a proposal episteme, not a selected repair, plan, work occurrence, or proof of improvement.

For wording, naming, and precision-restoration proposals, `proposedCorrectionDescriptionRef` does more than say "replace X with Y". It states the recovered object kind, relation, slot or use position when current, admissible use, and scope before and after the change. If no kind-preserving repair is recoverable, the row remains blocking.

#### E.22:4.5 - Absorption impact values

| Absorption impact | Meaning |
|---|---|
| `coordinateImproved` | A named coordinate or status has stronger content evidence after the change. |
| `floorOnlyClosure` | A below-floor defect was repaired enough for the floor but not exceptional expression. |
| `unchangedBecauseAlreadySatisfied` | The suggestion was already satisfied by value, with the exact review locations and the evaluation property they already satisfy named by value. |
| `tradeoffIntroduced` | A repair raised one property and damaged another. |
| `qualityLossDetected` | The applied or proposed change lowers a value or protected quality. |
| `outsideObjectUnderImprovementEvaluation` | The suggestion belongs under another exact evaluation or pattern. |
| `notAdmissibleForDeclaredUse` | The suggestion is rejected for the declared purpose and boundary. |

The absorption result states the changed evaluation result under the object-under-improvement evaluation, not a count of accepted rows.

#### E.22:4.6 - OEE and NQD proposal portfolios

When the object is a candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, `E.22` can frame the quality question and return proposal rows. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over candidate characteristics, archive and front semantics, pool policy, selected-set publication, parity, and refresh.

### E.22:5 - Worked slices

**Floor evaluation.** A reviewer is asked whether one pattern is ready for ordinary use. The frame names `E.21`, purpose `floorEvaluation`, the declared floor, and the expected `E.21` result form. The result is a complete `E.21` coordinate table with `ShortRationale` and `EvaluationEvidenceBasis`, not a narrative "looks fine."

**Exceptional improvement.** A pattern already passes the floor. The frame asks for substantive non-dominated improvements for named coordinates while protecting usability and related-pattern fit. The result returns proposal rows for content improvements such as missing worked cases, source-currentness carry-through, mature-comparator discharge, deletion of displaced apparatus, or relation cleanup, plus checked no-candidate dispositions for coordinates where no non-dominated content move remains. It does not ask the evaluator to make every coordinate `5`.

**Absorption.** External review returns many suggestions. The frame asks for `absorptionEvaluation`. The result says which changes improved coordinates, which were already satisfied, which introduced trade-offs, and which belong outside the evaluation.

**Proposal portfolio.** A candidate improvement campaign needs alternatives before editing. The frame asks for `candidateImprovementProposalEvaluation`. The result returns bounded proposal rows; selection or generation stays with the pattern that governs that claim and is not decided by the evaluation frame.

**Physical-system proposal.** A vibration evaluation of `PumpAssembly@Prototype-3` finds excessive RMS vibration at one operating point. The proposal's `reviewLocationDescriptionRef` points to that evaluation row. Its `correctionTargetRef` points to `ImpellerBladeGeometryDescription@v3`, the exact design episteme that would change; the measurement row is not the correction target. The affected coordinate is the declared RMS-vibration coordinate. The coarse proposal effect is `raiseTowardExceptional`, `kindRestorationCheckDisposition=notTriggered`, and the trade-off set includes efficiency and manufacturability. If the proposal is selected for a repeated loop, E.23 adds a scale-qualified `ExpectedEvaluationResultChange@Context`. Manufacturing a new impeller remains dated work under A.15 rather than an E.22 result.


### E.22:6 - Bias annotation

This pattern biases FPF toward asking the quality question by value. The bias is useful because unframed review requests often produce plausible but wrong answers.

The bias is bounded. `E.22` does not supply quality values, run repeated improvement, publish selected sets, decide work, or certify project claims.

### E.22:7 - Conformance checklist

| Check | Passing condition |
|---|---|
| `CC-E22-1` | Name the object version and object-under-improvement named by value evaluation. |
| `CC-E22-2` | State purpose, declared floor or improvement aim, protected trade-offs, and expected result form. |
| `CC-E22-3` | Keep the object-under-improvement evaluation as the source of values and the coordinate set to be evaluated. |
| `CC-E22-4` | Represent actionable returned work as typed finding or `CandidateImprovementProposalRow@Context` values with expected substantive evaluation effect, closure test, and the conditionally present `KindRestorationCheck`. An outside claim cites its direct governing pattern; E.22 frames the improvement question and does not restate that ontology. |
| `CC-E22-5` | For absorption, report quality impact on the changed object, not only applied and not-applied dispositions. |
| `CC-E22-6` | State a compact declarative non-use boundary when the result might be overread as decision, work, evidence, assurance, gate, release, certification, publication, parity, refresh, or selected-set authority. Keep the result on the evaluation question and name only the specific outside claim plus the pattern that governs it when one is needed; precision-restoration or phrase-apparatus issues belong to the named evaluation profile and `F.19`, not to a local boundary catalogue. |
| `CC-E22-7` | State what became worse when a proposed or applied improvement raises visible values. |
| `CC-E22-8` | Send repeated improvement to `E.23` after one framed evaluation returns findings or proposals. |
| `CC-E22-8a` | Do not frame `5`, all-`5`, or `5-defensible` as the work target. Frame below-floor repair separately from optional exceptional-improvement proposals. The optional proposal target is substantive content change, not score proof; allow checked `no proposal` or `stay at current value` only when further change would be dominated by apparatus growth, proof theatre, or protected-quality loss. |
| `CC-E22-9` | Name the expected evidence basis and result-row shape from the object-under-improvement evaluation; `E.22` cannot authorize omitted coordinates, missing rationales, missing selected attention-discharge profiles, missing `PrecisionRestorationProfile` when `E.21` is used, unchecked evidence positions, inactive or triggered-coordinate shortcuts, scope narrowing, or a weaker result form. |

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame@Context`. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation and return its declared coordinates, evidence basis, rationales, and payload fields. |
| **Scope laundering.** The frame asks one use, but the result answers an easier, local-only, diagnostic, or evaluator-selected use. | Re-run the named evaluation under the requested use; if another use is needed, open a new frame rather than saving the current result. |
| **Applied-count absorption.** Closure count replaces re-evaluation of the changed object. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen, or a `5` target makes the evaluator add apparatus instead of improving content. | Frame the expected evaluation effect as a substantive content change, add trade-off protection, reject dominated changes, apply E.13 when a visible value replaces the intended value, and admit `no proposal` only when checked positions show that no worthwhile content improvement remains. |
| **Recommendation as decision.** A follow-up hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |
| **Lexical repair request.** A finding says only "replace this word" or "avoid that wording." | Rewrite the row as a precision-restoration finding with kind, relation, admissible use, and scope before and after repair; if no kind-preserving repair is recoverable, leave it blocking. |

### E.22:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Review requests become typed. | Evaluators answer the intended quality question. | A complete request names the object and evaluation. |
| Exceptional improvement becomes explicit. | Reviews can propose non-dominated improvements rather than stopping at floor defects. | Each proposal names its protected trade-offs. |
| Absorption becomes quality-aware. | Follow-up says what improved or worsened. | Row discharge alone is not enough. |

### E.22:10 - Rationale

There is no neutral generic request when a quality result is wanted. The useful artifact is the framed question: object version, evaluation, purpose, expected evidence basis, expected result form, and boundary. This keeps review helpful without turning it into process control or project authority.

### E.22:11 - SoTA-Echoing

| Claim | Exact source and status | Inherited contribution and limit | Local adoption and disciplined case |
|---|---|---|---|
| A rubric-level evaluation needs its own reliability check rather than trust in one aggregate judge verdict. | Tianjun Pan et al., *RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following*, arXiv:2603.25133 (2026), and Hongli Zhou et al., *Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization*, arXiv:2603.08091 (2026), are current preprints for automated LLM judging. | Pan et al. show that fine-grained rubric judging can remain inaccurate and variable; Zhou et al. test a taxonomy of twelve bias types across generative and discriminative judges. These works concern LLM judges and instruction-following benchmarks; they do not validate an FPF evaluation or generalize their numeric results to physical, medical, or organizational evaluation. | `QualityEvaluationUseDeclaration@Context` separates governing method, quality-model descriptions, evidence basis, result form, and qualification window. The **Floor evaluation** and **Exceptional improvement** slices require the named evaluation's full result form rather than an unqualified judge verdict. |
| Actionable formative feedback distinguishes the desired condition, current performance, and a move that can close the gap. | D. Royce Sadler, *Formative assessment and the design of instructional systems*, *Instructional Science* 18, 119-144 (1989), DOI 10.1007/BF00117714; John Hattie and Helen Timperley, *The Power of Feedback*, *Review of Educational Research* 77(1), 81-112 (2007), DOI 10.3102/003465430298487. Both are retained historical education lineages. | Sadler supplies the comparison between a quality standard and current work plus action by the learner; Hattie and Timperley synthesize goal, current progress, and next-step feedback questions. Their classroom evidence does not establish FPF kinds, project authority, or the quality of a proposed repair. | The frame keeps floor or aim, current object version, expected result form, and proposal or checked no-proposal result distinct. The **Absorption** slice reports changed quality rather than merely counting accepted feedback. |
| Measurement questions should be derived from an explicit purpose rather than selected first and rationalized later. | Victor Basili, Gianluigi Caldiera, and H. Dieter Rombach, *The Goal Question Metric Approach*, in *Encyclopedia of Software Engineering* (1994), retained historical lineage; Victor Basili et al., *Linking Software Development and Business Strategy Through Measurement*, *Computer* 43(4), 57-65 (2010), DOI 10.1109/MC.2010.108, a later software-organization extension. | GQM contributes the purpose-to-question-to-measure direction; GQM+Strategies makes the link to higher-level goals and rationale explicit. Both are software-measurement methods and do not supply E.22's holonic ontology, evaluation values, or cross-domain quality model. | `QualityEvaluationPurposeSelection` is fixed before the evidence-basis and result-form descriptions. In the **Physical-system proposal**, the vibration purpose is declared before choosing the Q-Bundle, coordinate, measurement evidence, or proposal form. |
| Multi-coordinate improvement needs set-valued alternatives and explicit trade-offs rather than one scalar winner. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | Lin et al. reformulate QD as a large multi-objective problem and use set-based scalarization; Qin et al. survey high-performing collections over descriptor spaces. These algorithmic results do not assign FPF archive, front, publication, or selection authority. | `paretoTradeoffEvaluation`, `TradeoffProtectionSet@Context`, and `CandidateImprovementProposalPortfolio@Context` preserve alternatives and protected coordinates. The **Proposal portfolio** and **Physical-system proposal** slices stop before selection; archive, front, pool, and selected-set claims remain with their direct patterns. |
| Optimizing a measure can damage the intended value through several different mechanisms. | Charles Goodhart, *Problems of Monetary Management: The U.K. Experience* (1975), retained historical monetary-control lineage; Donald T. Campbell, *Assessing the Impact of Planned Social Change*, Occasional Paper 8 (1976), retained social-indicator lineage; David Manheim and Scott Garrabrant, *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585 (2018), later taxonomy; Jongwoon Choi, Gary Hecht, and William Tayler, *Lost in Translation: The Effects of Incentive Compensation on Strategy Surrogation*, *The Accounting Review* 87(4), 1135-1164 (2012), peer-reviewed experimental evidence. | Goodhart concerns control that changes an observed regularity; Campbell concerns corruption pressure on social indicators; Manheim and Garrabrant distinguish several overoptimization mechanisms; Choi et al. show managers treating a measure as the strategic construct. None says that every metric is invalid or supplies the intended value automatically. | The **Goodharted improvement** repair separates floor repair from substantive improvement, protects other qualities, rejects discharge count and all-`5` posture as value, and returns proxy-to-value repair to `E.13`. |
| Automated-judge mitigation is model-dependent and can itself require a declared guarantee or evidence profile. | Sadman Kabir Soumik, *Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines*, arXiv:2604.23178 (2026), current preprint; Benjamin Feuer, Lucas Rosenblatt, and Oussama Elachqar, *Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation*, arXiv:2603.05485 (2026), current preprint. | Soumik compares nine mitigations and reports model-dependent effects across four bias types; Feuer et al. define average bias-boundedness for specified judge settings. These results are benchmark- and model-bound and do not make any LLM judge generally unbiased. | `ExpectedEvaluationEvidenceBasis@Context` and the qualification window state what reliability support is actually claimed. The **Exceptional improvement** slice rejects style or proof apparatus that pleases an evaluator without improving the governed content. |
| OEE and NQD can use proposal-shaped quality pressure without collapsing proposal, candidate retention, and selection. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | The shared comparison question is how to preserve several high-performing alternatives across declared coordinates or descriptors. The sources do not say that an evaluation proposal is already a generated candidate, archive insertion, front update, or selected result. | `CandidateImprovementProposalRow@Context` names the expected later evaluation effect before generation or selection. E.22:4.6 and the **Proposal portfolio** slice keep C.17-C.19 and G.5 authority outside E.22. |

### E.22:12 - Relations

| Pattern | Relation |
|---|---|
| `E.21` | Supplies pattern-quality values and the complete pattern-quality coordinate set. |
| `E.9.DA` | Supplies DRR decision-adequacy values and the complete decision-adequacy coordinate set. |
| `E.2.DA` | Supplies FPF Pillar-adequacy values. |
| `E.19` | Supplies admission or refresh review profiles when that is the evaluation. |
| `E.23` | Governs repeated improvement after framed evaluations return findings or proposal rows. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when framed values, visible measures, proposal counts, or all-`5` posture are being used as the intended improvement value. |

| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by frames or findings. |
| `C.16`, `A.17`, `A.18`, `A.19`, `C.25` | Govern characteristics, scales, measurements, characteristic spaces, and quality bundles. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE and NQD candidate, archive and front, pool, selected-set, parity, and refresh claims. |
| `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3` | Receive decision, call-planning, work, gate, release, evidence, and assurance claims when a quality result is reused beyond evaluation. |

### E.22:End

