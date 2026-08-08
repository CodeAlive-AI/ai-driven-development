## E.22 - Improvement-Oriented Quality Evaluation Question Framing

Status: Core.

### E.22:1 - Problem frame

Use `E.22` when someone is about to ask for a quality evaluation, quality review, returned-finding absorption, improvement proposal, or follow-up hypothesis over an object version named by value, and the question needs to say what kind of evaluation is wanted before the evaluator starts.

`E.22` frames the question. It does not evaluate the object. `evaluationPatternLocator` identifies the FPF pattern description containing the evaluation predicate or constraint; an optional `semanticEvaluationMethodRef` names the separately identified `U.Method` used for that evaluation. A characteristic-space specification, Q-Bundle description, rubric description, review-profile description, evidence-basis description, and result-form description constrain or describe that evaluation. None of those specifications performs the evaluation or substitutes for the subject assertion or semantic Method. For example, `E.21`, `E.9.DA`, or `E.2.DA` may supply the predicate for evaluating one FPF object, while `A.19.ECS` and `C.25` supply supporting quality-model descriptions. `E.19` instead defines an admission or refresh review-gate and findings profile. Use `E.19` as `evaluationPatternLocator` only when its review result is itself the object under evaluation; otherwise its later gate check remains distinct from the quality evaluation.

Not this pattern when the question is already scoped and one direct evaluation is enough. Run the object-under-improvement evaluation directly. Use `E.23` when repeated improvement across passes is needed.

First useful move: write a `QualityEvaluationQuestionFrame` for one exact object version and a `QualityEvaluationUseDeclaration`. Name the exact selected `CharacteristicSpace`, the by-value predicate and/or admitted comparator required by that evaluation, one `U.ClaimScope`, and the exact intended work or decision that will consume the result. In the declaration, keep the governing evaluation pattern and optional semantic method separate from quality-model, evidence-basis, and result-form descriptions and from the performer assignment; then state the purpose, floor or improvement aim, and protected trade-offs.

Here *move* is Plain wording for writing the frame. It is not a shared Move identity, selected repair, WorkPlan, performed `U.Work`, or actual `U.Transformation`; if dated framing work itself matters, A.15 governs that separate occurrence.

What goes wrong if missed: "review this" can mean too many different things. A floor check may be mistaken for exceptional improvement, a review may suggest work without naming a changed evaluation result, absorption may count closed rows without re-evaluating the changed object, or a follow-up suggestion may be overread as a decision, work plan, gate, evidence, assurance, or release.

What this buys in practice: requester and evaluator start with the same object version, selected characteristic space, criterion or comparator, evaluation scope, consuming use, evaluation purpose, value source, protected trade-offs, evidence basis, and result form. A small floor question can stay small, while a request for proposals or trade-off analysis returns the additional information needed for a later improvement decision.

Primary EntityOfConcern in plain terms: the framed quality-evaluation question for one object version.

A below-floor value, finding, improvement aim, or need for evaluation is not by itself an actual Problem. If the consuming use relies on an actual Problem, cite one current C.22.PFR `ProblematicForRelation` occurrence with its direct participants and temporal identity; the frame, evaluation, result, and evidence may support a claim about it but neither create nor split it.

### E.22:2 - Problem

Quality evaluations fail when the evaluator has to infer the question. The same object can be checked for floor adequacy, improved toward exceptional expression, compared across trade-offs, mined for open questions, or evaluated after finding absorption. Those purposes produce different findings.

The defect is not that reviewers need more ceremony. The defect is that an unframed question hides the object under improvement, the evaluation that supplies values, and the allowed shape of returned work.

### E.22:3 - Forces

| Force | Tension |
|---|---|
| Cheap readiness vs ambitious improvement | A floor evaluation should be short; exceptional improvement needs richer proposals. |
| Explicit purpose vs reviewer discovery | The request names the purpose, while the reviewer can still report important unasked questions. |
| Evaluation vs follow-up action | A useful evaluation may suggest a follow-up, but the suggestion remains a hypothesis until the pattern that defines or constrains the claim, relation, or boundary is applied. |
| Multi-coordinate gain vs Goodhart risk | Raising one visible value can damage usability, affordability, locality, source preservation, or corpus ecology; use `E.13` when the visible value or metric is being treated as the intended value itself. |
| Proposal portfolio vs selected result | Several candidate improvements may be useful without becoming a selected set, pool policy, front insertion, parity, or refresh result. |

### E.22:4 - Solution

`E.22` gives one compact declaration for improvement-oriented quality evaluation questions. It keeps the question from replacing the evaluation and keeps the evaluation result from becoming a decision or work product beyond its authority.

#### E.22:4.1 - Local names and kind settlement

The framing episteme, evaluation method, descriptions used by that method, performer assignment, dated evaluation Work, actual operation application, evidence use, and result occupy different positions. `QualityEvaluationUseDeclaration` keeps the intended evaluation bindings together without collapsing those kinds.

The remaining local support names ending in `@Context` are compatibility and retrieval names only. The suffix supplies no context entity, scope, participant, relation, or identity component; every episteme follows C.2.1 identity, every set is identified by its stated extensional rule, and every neighboring Work, decision, evidence, viewpoint, grounding, or result relation remains under its direct governor.

| Local name | Kind and role |
|---|---|
| `QualityEvaluationQuestionFrame` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation; its ClaimGraph carries the requested quality-evaluation question about that version and its exact use bindings. |
| `QualityEvaluationUseDeclaration` | `U.Episteme` whose EntityOfConcern is the same exact object version. It describes how evaluation of that version is intended to be performed and interpreted, referring separately to performer assignment, governing evaluation pattern, optional semantic method, selected characteristic space, predicate/comparator binding, ClaimScope, quality-model descriptions, expected evidence basis, result form, and qualification window. |
| `ObjectVersionUnderQualityEvaluation` | Exact `U.Entity` version being evaluated, paired with its exact `U.Kind`. |
| `EvaluationCharacteristicSpaceSelection` | One exact `U.CharacteristicSpace` selected for this evaluation use. Its specification description is a separate episteme and does not become the space. |
| `EvaluationCriterionSelection` | The exact by-value `CharacteristicSpacePredicate`, exact admitted `ComparatorSpecRef`, or both, required by the governing evaluation pattern and, when declared, its separately identified semantic evaluation Method. At least one is present. |
| `EvaluationClaimScope` | One exact set-valued `U.ClaimScope` governing the evaluation claim. It is not a context label, selected structure, window, or evidence set. |
| `QualityEvaluationResultConsumingUse` | The exact directly governed intended-work, dated-work, or decision object that is expected to consume the evaluation result, paired with its exact kind and use description. It does not authorize or perform that use. |
| `QualityEvaluationPurposeSelection` | Requested evaluation purpose or distinguishable combination of purposes. |
| `DeclaredQualityFloor` | Minimum acceptable coordinate or status floor when the frame declares a floor claim. |
| `DesiredImprovementAim` | Requested substantive change beyond the floor when improvement beyond the floor is requested. |
| `ExpectedEvaluationEvidenceBasis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version under evaluation. It describes expected evidence-use positions and the missingness rule for the exact method, space, criterion, scope, and qualification window. It can be identified before a use declaration cites it and is not the evidence values later found. |
| `TradeoffProtectionSet@Context` | A local `U.Set` value whose members are exact characteristic or coordinate references paired with their kinds. Its identity is extensional for the exact question-frame edition, not for a context label. |
| `EvaluationQualificationWindow` | Edition, source-currentness, comparison-set, time, or declared-use window in which the requested result is intended to be current. The actual evaluation application later binds its exact point or interval. |
| `ExpectedQualityEvaluationResultFormDescription` | `U.Episteme` describing the result-row form declared by the governing evaluation pattern. It is not an actual result. |
| `QualityReviewFindingRow` | Actionable evaluation finding that identifies the observed issue, affected evaluation property, correction direction, and closure test. |
| `CandidateImprovementProposalRow@Context` | E.22 proposal episteme with an exact correction target, expected substantive evaluation effect, trade-offs, kind-restoration disposition, outside-claim return when needed, and closure test. |
| `CandidateImprovementOutsideClaimReference@Context` | Bounded local ClaimGraph node form inside one proposal row. It identifies the outside governed value, relation signature, or boundary description and the exact FPF pattern identity that governs the return. It is not an episteme, relation, or independently referenceable entity. |
| `KindRestorationCheck` | Conditionally present check when a finding or proposal changes wording, naming, or precision-restoration content. |
| `CandidateImprovementProposalPortfolio@Context` | A local `U.Set` value whose members are `CandidateImprovementProposalRow@Context` epistemes for one question frame. Membership, not a document serialization, determines the portfolio. |
| `ImprovementFollowUpHypothesis@Context` | `U.Episteme` whose EntityOfConcern is the exact object version expected to change. It claims that one named next operation or method application is expected to address one finding and produce a stated evaluation effect under a stated test condition. A stop disposition, return, selected plan, performed Work, or actual Transformation is not such a hypothesis. |

```text
QualityEvaluationUseDeclaration <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  evaluationPerformerRoleAssignmentRef?: U.EntityRef, referencing one U.RoleAssignment
  evaluationPatternLocator: U.EntityRef, locating the exact FPF pattern description that contains the defining or constraining ClaimGraph
  semanticEvaluationMethodRef?: U.MethodRef, referencing the separately identified U.Method used for the evaluation
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing one exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing one exact U.ClaimScope
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  evaluationCharacteristicSpaceSpecDescriptionRef?: U.EpistemeRef, referencing one A.19.ECS specification description
  evaluationQBundleDescriptionRef?: U.EpistemeRef, referencing one C.25 Q-Bundle description
  evaluationRubricDescriptionRef?: U.EpistemeRef, referencing one evaluation-rubric description
  evaluationReviewProfileDescriptionRef?: U.EpistemeRef, referencing one evaluation-review-profile description
  expectedEvaluationEvidenceBasisRef: U.EpistemeRef, referencing one ExpectedEvaluationEvidenceBasis@Context
  expectedEvaluationResultFormDescriptionRef: U.EpistemeRef, referencing one ExpectedQualityEvaluationResultFormDescription

ExpectedEvaluationEvidenceBasis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version whose evaluation needs the expected evidence
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  evaluationPatternLocator: U.EntityRef, locating the same exact FPF evaluation pattern description
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same exact U.ClaimScope
  expectedEvidencePositionDescriptionRefs[1..*]: U.EpistemeRef, each referencing one evidence-position description
  expectedEvidenceRelationKindRefs[1..*]: U.KindRef, each referencing one expected evidence-relation kind
  missingEvidenceDispositionRuleRef: U.EpistemeRef, referencing one exact episteme that states the missing-evidence disposition rule under its subject pattern
  qualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
```

Every field above with a `*Ref` suffix stores the stated A.6.5 `RefKind`; resolving it yields the referent kind named after `referencing`. The use declaration and expected evidence basis carry the same exact object version, governing evaluation pattern, selected characteristic space, criterion binding, ClaimScope, and qualification window. The expected basis does not point back to the declaration: it can be constituted from those exact values, expected evidence positions and relation kinds, and missingness rule; the declaration is then constituted with a reference to that completed basis. This preserves the former acyclic construction.

At least one of `selectedEvaluationPredicate` and `selectedComparatorSpecRef` is present; both may be present. A label such as *review*, *quality*, or *current context* supplies neither. A.19 owns the predicate by value. A.19.CPM or the exact direct consumer owns comparator admission and any actual comparison application. Neither the predicate nor comparator owns evaluation scope, evidence, time, Work, or result.

`evaluationPerformerRoleAssignmentRef` identifies who is assigned to perform the evaluation; it is neither the semantic Method nor the object being evaluated. `evaluationPatternLocator` locates the exact FPF pattern description containing the defining or constraining ClaimGraph; it is neither the semantic Method, performer, dated Work, nor result. If that description is asserted to be a `U.MethodDescription`, its membership requires an independent A.3.2 result. `semanticEvaluationMethodRef`, when recoverable, identifies the separately admitted Method used for the evaluation. Any episteme claimed to describe that Method remains a separate object and requires an independent A.3.2 membership result. The characteristic-space, Q-Bundle, rubric, review-profile, evidence-basis, and result-form references identify separate epistemes that specify the quality model or its use; they do not supply an actor and do not become alternative values of the pattern or method slots.

None of these declaration fields is dated evaluation Work or an evaluation result. When evaluation is performed, A.15.1 identifies one dated `U.Work` and its direct method-enactment relation. The direct evaluation pattern contains the defining content for the exact evaluation and typed result; when it exposes a reusable operation, A.6.1 separately identifies the actual application and result binding. A durable result episteme, when needed, remains under C.2.1. Actual evidence use, provenance, currentness, viewpoint selection, empirical grounding, and any work-to-result or decision-use relation remain separate under their direct governors. A frame, declaration, description, role assignment, dashboard, or carrier establishes none of those occurrences.

Two carriers may publish the same edition of either episteme. A `QualityEvaluationUseDeclaration` changes edition when its exact object version, claim graph, reference scheme, performer assignment, governing evaluation pattern, semantic method, selected characteristic space, predicate/comparator binding, ClaimScope, qualification window, quality-model descriptions, expected evidence-basis edition, or result-form description changes. An `ExpectedEvaluationEvidenceBasis@Context` changes edition when its object version, claim graph, reference scheme, governing evaluation pattern, selected space, predicate/comparator binding, ClaimScope, expected evidence positions or relation kinds, missingness rule, or qualification window changes. Carrier, context label, viewpoint, grounding record, or support serialization alone changes neither episteme. `TradeoffProtectionSet@Context` and `CandidateImprovementProposalPortfolio@Context` are set values, not records; an episteme may describe or publish either set without becoming the set.

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
QualityEvaluationQuestionFrame <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under evaluation
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationUseDeclarationRef: U.EpistemeRef, referencing one QualityEvaluationUseDeclaration about the same object version
  selectedEvaluationCharacteristicSpaceRef: U.EntityRef, referencing the same exact U.CharacteristicSpace
  selectedEvaluationPredicate?: CharacteristicSpacePredicate by value
  selectedComparatorSpecRef?: ComparatorSpecRef
  evaluationClaimScopeRef: U.EntityRef, referencing the same exact U.ClaimScope
  resultConsumingUseRef: U.EntityRef, referencing one exact directly governed intended-work, dated-work, or decision object
  resultConsumingUseKindRef: U.KindRef, referencing its exact kind
  resultConsumingUseDescriptionRef: U.EpistemeRef, describing how that work or decision will use the evaluation result
  evaluationPurposeSelection: QualityEvaluationPurposeSelectionValue
  declaredQualityFloorDescriptionRef?: U.EpistemeRef, referencing one declared-quality-floor description
  desiredImprovementAimDescriptionRef?: U.EpistemeRef, referencing one desired-improvement-aim description
  tradeoffProtectionSet: TradeoffProtectionSet@Context by value
  evaluationQualificationWindowDescriptionRef: U.EpistemeRef, referencing one EvaluationQualificationWindow description
  nonUseBoundaryDescriptionRef: U.EpistemeRef, referencing one non-use-boundary description
```

The frame's exact object version, characteristic space, predicate/comparator binding, ClaimScope, and qualification window equal those of its use declaration and expected evidence basis. These bindings make the question replayable; they do not reidentify the space, predicate, comparator, scope, method, or consuming object. A changed binding creates a changed frame edition and requires a newly evaluated result.

`resultConsumingUseRef` is not a generic *use* placeholder. Before occurrence it may resolve to one A.15.2 `U.WorkPlan` that names the particular intended Work, or to the exact decision question or decision-governing object under its direct pattern. It may resolve to `U.Work` only when that dated Work already obtains under A.15.1. The frame neither creates the consuming Work or decision nor authorizes it.

The shortest floor frame names the object version, one `QualityEvaluationUseDeclaration`, the exact selected characteristic space, applicable predicate and/or comparator, ClaimScope, result-consuming work or decision, purpose `floorEvaluation`, and the declared floor. The declaration may cite defaults supplied by the governing evaluation pattern for its quality-model descriptions, evidence basis, result form, and qualification window, but defaults do not replace the exact selected space, criterion, scope, or consumer. If the question depends on another edition, source state, comparison set, time window, or declared use, state that window explicitly. For one FPF pattern version under E.21, compactness never permits omitted coordinates, missing `ShortRationale`, absent `PrecisionRestorationProfile`, scope narrowing, or a blocker-only substitute result.

The frame does not authorize post-hoc scope replacement. If the requested floor is landing-input, corpus-facing, `Stable`, release, external-review, or another stated use, the evaluator measures that use. If a different use becomes interesting, open a new `QualityEvaluationQuestionFrame`; do not report the current request as passed under an easier scope.

The frame and declaration perform no evaluation. A dated evaluation Work occurrence, its method enactment, any actual operation application, actual evidence use, typed result binding or direct result relation, and optional result episteme remain separate. An expected result-form description is not the result, and the consuming work or decision does not become current merely because the frame names it.

#### E.22:4.4 - Finding and proposal rows

An actionable finding first identifies where an issue was observed, which exact entity would change, the affected evaluation characteristic or coordinate, the current evaluation result for that characteristic or coordinate when known, the proposed correction, and the closure test. A proposal adds a typed expected evaluation effect, protected trade-offs, and any outside claim together with the subject-pattern locator needed to check that claim independently.

```text
CandidateImprovementProposalRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version under improvement
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's exact U.ClaimScope
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
  subjectPatternLocator: U.EntityRef, locating the exact FPF subject-pattern description; the evaluation claim separately cites the defining ClaimGraph
  reconsiderationConditionDescriptionRef: U.EpistemeRef, referencing one description of the condition that activates renewed use of that subject pattern
```

```text
ImprovementFollowUpHypothesis@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact object version expected to change
  entityOfConcernKindRef: U.KindRef, referencing the exact kind of that object version
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  qualityEvaluationQuestionFrameRef: U.EpistemeRef, referencing one QualityEvaluationQuestionFrame about the same object version
  evaluationClaimScopeRef: U.EntityRef, referencing that frame's exact U.ClaimScope
  qualityReviewFindingDescriptionRef: U.EpistemeRef, referencing one episteme that describes the exact QualityReviewFindingRow
  proposedNextOperationDescriptionRef?: U.EpistemeRef, referencing one operation description
  proposedNextMethodRef?: U.MethodRef, referencing one U.Method
  expectedEvaluationEffectDescriptionRef: U.EpistemeRef, referencing one expected-evaluation-effect description
  testConditionDescriptionRef: U.EpistemeRef, referencing one test-condition description
```

Exactly one of `proposedNextOperationDescriptionRef` and `proposedNextMethodRef` is present. The question frame, proposal row, and follow-up hypothesis preserve the same exact object-version EntityOfConcern and ClaimScope unless a proposal explicitly opens a new frame for a different version or scope. `QualityEvaluationQuestionFrame` changes edition when the object version, use declaration, selected space, predicate/comparator binding, ClaimScope, consuming work or decision, purpose, floor or aim, trade-off set, qualification window, non-use boundary, claim graph, or reference scheme changes. A proposal row changes edition when its frame, ClaimScope, correction target, affected evaluation coordinate, current result reference, proposed correction, expected effect, trade-offs, outside-claim nodes, closure test, claim graph, or reference scheme changes. A follow-up hypothesis changes edition when its frame, ClaimScope, finding description, proposed operation or method, expected effect, test condition, claim graph, or reference scheme changes. A context label, carrier, viewpoint, grounding record, or serialization change alone changes none of these epistemes.

`ProposalEvaluationEffectValue` is the closed local value set `repairFloor | raiseTowardExceptional | preventProtectedQualityLoss | classifyOutsideEvaluation | preserveCurrentValue`. It identifies the coarse substantive evaluation effect expected from this proposal. It does not duplicate the coordinate-qualified prediction later carried by E.23 `ExpectedEvaluationResultChange@Context` and does not assert an actual changed result.

`ProposalKindRestorationCheckDispositionValue` is `triggered | notTriggered | ordinaryProse | alreadySatisfied | blocker`. The `triggered` and `blocker` states include `kindRestorationCheckRef`; the other values leave it absent. Current affected-evaluation result ref and kind are both present or both absent; when present, the exact result resolves through the direct evaluation pattern's typed result relation or A.6.1 application binding, and any durable result episteme remains separately governed. The proposal row neither produces nor reidentifies that result. The exact kind recovers whether the named evaluation returned a scale value, status, or another admitted result for that characteristic or coordinate. Outside value ref and kind are paired, and `outsideRelationSignatureRef` is present when the outside value is a relation. `CandidateImprovementOutsideClaimReference@Context` is a bounded local ClaimGraph node form, not a U-kind, episteme, relation, or relation-reference episteme. It is constructed inside one proposal row without a back-reference to that row; its node identity is determined by the containing proposal edition and ClaimGraph position.

`reviewLocationDescriptionRef` describes where the issue was observed in the reviewed object. `correctionTargetRef` identifies the exact entity that would change. They are not interchangeable positions. The row is a faithful typed proposal form of `QualityReviewFindingRow` and one possible member of a `CandidateImprovementProposalPortfolio@Context` set. It remains a proposal episteme, not a selected repair, plan, work occurrence, actual Transformation, result binding, or proof of improvement.

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

When the object is a candidate, archive or front member, selected set, parity report, refresh report, or declared transformation result, use `E.22` to frame the quality question and return proposal rows. Use `C.17` for candidate characteristics, `C.18` for archive and front relations, `C.19` for pool policy, `G.5` for selected-set result declaration, `G.9` for parity, and `G.11` for currentness and refresh. When audience availability is current, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

### E.22:5 - Worked slices

**Floor evaluation.** A reviewer is asked whether one pattern is ready for ordinary use. The frame names the exact pattern version, E.21 characteristic space and floor predicate, the evaluation ClaimScope, the decision that will consume the result, `E.21` as the governing evaluation pattern, purpose `floorEvaluation`, the declared floor, and the expected `E.21` result form. Any semantic evaluation Method is named separately when it is recoverable. The result becomes current only through the direct E.21 evaluation under one dated evaluation Work and its exact typed result relation or binding: a complete `E.21` coordinate table with `ShortRationale` and `EvaluationEvidenceBasis`, not a narrative "looks fine" and not the frame itself.

**Exceptional improvement.** A pattern already passes the floor. The frame asks for substantive non-dominated improvements for named coordinates while protecting usability and related-pattern fit. The result returns proposal rows for content improvements such as missing worked cases, source-currentness carry-through, mature-comparator discharge, deletion of displaced apparatus, or relation cleanup, plus checked no-candidate dispositions for coordinates where no non-dominated content move remains. It does not ask the evaluator to make every coordinate `5`.

**Absorption.** External review returns many suggestions. The frame asks for `absorptionEvaluation`. The result says which changes improved coordinates, which were already satisfied, which introduced trade-offs, and which belong outside the evaluation.

**Proposal portfolio.** A candidate improvement campaign needs alternatives before editing. The frame asks for `candidateImprovementProposalEvaluation`. The result returns bounded proposal rows; selection or generation stays with the pattern that defines or constrains that claim and is not decided by the evaluation frame.

**Physical-system proposal.** A vibration evaluation of `PumpAssembly@Prototype-3` selects the exact vibration `CharacteristicSpace`, RMS-vibration predicate and any admitted comparator, one evaluation ClaimScope over the declared operating-point slices, and the design decision that will consume the result. During dated test-bench evaluation Work, the directly governed evaluation relation or actual method operation returns a result finding excessive RMS vibration at one operating point through its exact binding; the frame, subject pattern reference, separately identified semantic Method when named, role assignment, expected evidence basis, and result-form description remain separate. The proposal's `reviewLocationDescriptionRef` points to that evaluation row. Its `correctionTargetRef` points to `ImpellerBladeGeometryDescription@v3`, the exact design episteme that would change; the measurement row is not the correction target. The affected coordinate is the declared RMS-vibration coordinate. The coarse proposal effect is `raiseTowardExceptional`, `kindRestorationCheckDisposition=notTriggered`, and the trade-off set includes efficiency and manufacturability. If the proposal is selected for a repeated loop, E.23 adds a scale-qualified `ExpectedEvaluationResultChange@Context`. Manufacturing a new impeller remains dated work under A.15 rather than an E.22 result.

### E.22:6 - Bias annotation

This pattern biases FPF toward asking the quality question by value. The bias is useful because unframed review requests often produce plausible but wrong answers.

The bias is bounded. `E.22` does not supply quality values, run repeated improvement, publish selected sets, decide work, or certify project claims.

### E.22:7 - Conformance checklist

| Check | Passing condition |
|---|---|
| `CC-E22-1` | Name the exact object version, selected `CharacteristicSpace`, exact predicate and/or admitted comparator, one `U.ClaimScope`, and the exact work or decision that will consume the result. |
| `CC-E22-2` | State purpose, declared floor or improvement aim, protected trade-offs, qualification window, and expected result form. |
| `CC-E22-3` | Keep the object-under-improvement evaluation as the source of values and the coordinate set to be evaluated. A description, dashboard, or frame cannot substitute for the selected space, predicate/comparator, actual evaluation, or result. |
| `CC-E22-4` | Represent actionable returned work as typed finding or `CandidateImprovementProposalRow@Context` values with expected substantive evaluation effect, closure test, and the conditionally present `KindRestorationCheck`. An outside claim cites its subject pattern; E.22 frames the improvement question and does not restate that ontology. |
| `CC-E22-5` | For absorption, report quality impact on the changed object, not only applied and not-applied dispositions. |
| `CC-E22-6` | State a compact declarative non-use boundary when the result might be overread as decision, work, evidence, assurance, gate, release, certification, publication, parity, refresh, or selected-set authority. Keep the result on the evaluation question and name only the specific outside claim plus the pattern that defines or constrains it when one is needed; precision-restoration or phrase-apparatus issues belong to the named evaluation profile and `F.19`, not to a local boundary catalogue. |
| `CC-E22-7` | State what became worse when a proposed or applied improvement raises visible values. |
| `CC-E22-8` | Use `E.23` for repeated improvement after one framed evaluation returns findings or proposals. |
| `CC-E22-8a` | Do not frame `5`, all-`5`, or `5-defensible` as the work target. Frame below-floor repair separately from optional exceptional-improvement proposals. The optional proposal target is substantive content change, not score proof; allow checked `no proposal` or `stay at current value` only when further change would be dominated by apparatus growth, proof theatre, or protected-quality loss. |
| `CC-E22-9` | Name the expected evidence basis and result-row shape from the object-under-improvement evaluation; `E.22` cannot authorize omitted coordinates, missing rationales, missing selected attention-discharge profiles, missing `PrecisionRestorationProfile` when `E.21` is used, unchecked evidence positions, inactive or triggered-coordinate shortcuts, scope narrowing, or a weaker result form. |
| `CC-E22-10` | Keep the question frame, use declaration, evaluation pattern locator, optional semantic Method, any independently admitted method description actually cited, quality-model/evidence/result-form descriptions, performer assignment, dated evaluation Work, method enactment, any actual operation application, actual evidence use, typed result binding or direct result relation, optional result episteme, and result-consuming work or decision distinct. The locator is not the semantic Method, evaluator, dated Work, or result; any `U.MethodDescription` membership requires an independent A.3.2 result, and no generic work-result or evaluation-result relation is inferred. |
| `CC-E22-11` | A low value, finding, failed floor, or improvement aim does not establish an actual Problem. Any actual Problem relied on by the consuming use resolves to one current C.22.PFR occurrence with its direct participants and temporal identity. |

### E.22:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **"Review this" prompt.** The evaluator infers purpose. | Add a `QualityEvaluationQuestionFrame` with exact object version, space, criterion, ClaimScope, consumer, purpose, and boundary. |
| **Context-labelled frame.** Project, domain, dashboard, cadence, or context label supplies identity or evaluation scope. | Identify the frame by its C.2.1 claim content and exact EntityOfConcern; bind the exact `U.ClaimScope` and other use values separately. |
| **Floor pass sold as excellence.** Readiness is mistaken for exceptional improvement. | State `exceptionalImprovementEvaluation` if wanted. |
| **Frame replaces result.** The question frame names a purpose but returns prose, a two-column value table, or proposal rows without the named evaluation's result form. | Re-run the named evaluation as dated Work with its direct method enactment or A.6.1 operation application and return its declared coordinates, evidence basis, rationales, payload fields, and typed result binding or direct result relation. |
| **Description performs evaluation.** A method description, characteristic-space specification, expected evidence basis, role assignment, or result-form description is treated as evaluation Work or its result. | Keep each description and assignment separate; identify one dated A.15.1 Work occurrence, the direct evaluation application, actual evidence use, and result under their exact governors. |
| **Scope laundering.** The frame asks one use, but the result answers an easier, local-only, diagnostic, or evaluator-selected use. | Re-run the named evaluation under the requested `U.ClaimScope`; if another use is needed, open a new frame rather than saving the current result. |
| **Applied-count absorption.** Closure count replaces re-evaluation of the changed object. | Re-evaluate the changed object and classify impact. |
| **Goodharted improvement.** Visible values rise while protected qualities worsen, or a `5` target makes the evaluator add apparatus instead of improving content. | Frame the expected evaluation effect as a substantive content change, add trade-off protection, reject dominated changes, apply E.13 when a visible value replaces the intended value, and admit `no proposal` only when checked positions show that no worthwhile content improvement remains. |
| **Recommendation as decision.** A follow-up hypothesis is treated as chosen work. | Open the exact decision, work, publication, parity, refresh, evidence, or assurance pattern if that claim is needed. |
| **Finding as actual Problem.** A low coordinate, finding, or floor miss is treated as a Problem occurrence. | Keep the evaluation result epistemic; cite C.22.PFR only when its actual-condition and criterion-applicability participants make one ProblematicFor occurrence obtain. |
| **Lexical repair request.** A finding says only "replace this word" or "avoid that wording." | Rewrite the row as a precision-restoration finding with kind, relation, admissible use, and scope before and after repair; if no kind-preserving repair is recoverable, leave it blocking. |

### E.22:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Review requests become typed. | Evaluators answer the intended quality question. | A complete request names the object and evaluation. |
| Exceptional improvement becomes explicit. | Reviews can propose non-dominated improvements rather than stopping at floor defects. | Each proposal names its protected trade-offs. |
| Absorption becomes quality-aware. | Follow-up says what improved or worsened. | Row discharge alone is not enough. |

### E.22:10 - Rationale

There is no neutral generic request when a quality result is wanted. The useful artifact is the framed question: exact object version, selected characteristic space, predicate and/or comparator, one evaluation ClaimScope, consuming work or decision, governing evaluation pattern, any separately identified semantic Method, purpose, expected evidence basis, expected result form, and boundary. The frame makes those bindings inspectable without becoming the pattern, Method, performer assignment, descriptions, dated evaluation Work, evidence use, result, decision, or project authority.

### E.22:11 - SoTA-Echoing

| Claim | Exact source and status | Inherited contribution and limit | Local adoption and disciplined case |
|---|---|---|---|
| A rubric-level evaluation needs its own reliability check rather than trust in one aggregate judge verdict. | Tianjun Pan et al., *RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following*, arXiv:2603.25133 (2026), and Hongli Zhou et al., *Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization*, arXiv:2603.08091 (2026), are current preprints for automated LLM judging. | Pan et al. show that fine-grained rubric judging can remain inaccurate and variable; Zhou et al. test a taxonomy of twelve bias types across generative and discriminative judges. These works concern LLM judges and instruction-following benchmarks; they do not validate an FPF evaluation or generalize their numeric results to physical, medical, or organizational evaluation. | `QualityEvaluationUseDeclaration` separates the governing evaluation pattern, semantic Method when declared, selected space and criterion, ClaimScope, quality-model descriptions, evidence basis, result form, and qualification window. The **Floor evaluation** and **Exceptional improvement** slices require the named evaluation's full result form rather than an unqualified judge verdict. |
| Actionable formative feedback distinguishes the desired condition, current performance, and a move that can close the gap. | D. Royce Sadler, *Formative assessment and the design of instructional systems*, *Instructional Science* 18, 119-144 (1989), DOI 10.1007/BF00117714; John Hattie and Helen Timperley, *The Power of Feedback*, *Review of Educational Research* 77(1), 81-112 (2007), DOI 10.3102/003465430298487. Both are retained historical education lineages. | Sadler supplies the comparison between a quality standard and current work plus action by the learner; Hattie and Timperley synthesize goal, current progress, and next-step feedback questions. Their classroom evidence does not establish FPF kinds, project authority, or the quality of a proposed repair. | The frame keeps floor or aim, current object version, expected result form, and proposal or checked no-proposal result distinct. The **Absorption** slice reports changed quality rather than merely counting accepted feedback. |
| Measurement questions should be derived from an explicit purpose rather than selected first and rationalized later. | Victor Basili, Gianluigi Caldiera, and H. Dieter Rombach, *The Goal Question Metric Approach*, in *Encyclopedia of Software Engineering* (1994), retained historical lineage; Victor Basili et al., *Linking Software Development and Business Strategy Through Measurement*, *Computer* 43(4), 57-65 (2010), DOI 10.1109/MC.2010.108, a later software-organization extension. | GQM contributes the purpose-to-question-to-measure direction; GQM+Strategies makes the link to higher-level goals and rationale explicit. Both are software-measurement methods and do not supply E.22's holonic ontology, evaluation values, or cross-domain quality model. | `QualityEvaluationPurposeSelection` is fixed before the evidence-basis and result-form descriptions. In the **Physical-system proposal**, the vibration purpose is declared before choosing the Q-Bundle, coordinate, measurement evidence, or proposal form. |
| Multi-coordinate improvement needs set-valued alternatives and explicit trade-offs rather than one scalar winner. | Xi Lin et al., *Quality-Diversity Optimization as Multi-Objective Optimization*, arXiv:2602.00478 (2026), current preprint; Haoxiang Qin et al., *A survey on Quality-Diversity optimization: Approaches, applications, and challenges*, *Swarm and Evolutionary Computation* 100:102240 (2026), DOI 10.1016/j.swevo.2025.102240, current survey. | Lin et al. reformulate QD as a large multi-objective problem and use set-based scalarization; Qin et al. survey high-performing collections over descriptor spaces. These algorithmic results do not assign FPF archive, front, publication, or selection authority. | `paretoTradeoffEvaluation`, `TradeoffProtectionSet@Context`, and `CandidateImprovementProposalPortfolio@Context` preserve alternatives and protected coordinates. The **Proposal portfolio** and **Physical-system proposal** slices stop before selection; archive, front, pool, and selected-set claims remain with their direct patterns. |
| Optimizing a measure can damage the intended value through several different mechanisms. | Charles Goodhart, *Problems of Monetary Management: The U.K. Experience* (1975), retained historical monetary-control lineage; Donald T. Campbell, *Assessing the Impact of Planned Social Change*, Occasional Paper 8 (1976), retained social-indicator lineage; David Manheim and Scott Garrabrant, *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585 (2018), later taxonomy; Jongwoon Choi, Gary Hecht, and William Tayler, *Lost in Translation: The Effects of Incentive Compensation on Strategy Surrogation*, *The Accounting Review* 87(4), 1135-1164 (2012), peer-reviewed experimental evidence. | Goodhart concerns control that changes an observed regularity; Campbell concerns corruption pressure on social indicators; Manheim and Garrabrant distinguish several overoptimization mechanisms; Choi et al. show managers treating a measure as the strategic construct. None says that every metric is invalid or supplies the intended value automatically. | The **Goodharted improvement** repair separates floor repair from substantive improvement, protects other qualities, rejects discharge count and all-`5` posture as value, and requires `E.13`. |
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
| `A.19`, `A.19.ECS`, `A.19.CPM`, `A.2.6` | Govern the selected `CharacteristicSpace`, its construction description, predicate/comparator semantics and actual comparison application, and exact `U.ClaimScope`; E.22 binds their values for one question but does not redefine them. |
| `A.15.1`, `A.6.1`, `C.2.1` | Govern dated evaluation Work and method enactment, any actual operation application and result binding, and any durable result episteme. The direct evaluation pattern contains the defining content for its typed result relation; E.22 mints no generic evaluation-result or work-result relation. |
| `A.2.4`, `A.10`, `G.11` | Govern actual evidence use, provenance, and currentness separately from the expected evidence-basis description. |
| `C.22.PFR` | Governs an actual Problem occurrence when the consuming use relies on one; evaluation need, finding, or floor failure alone establishes none. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18` | Repair load-bearing wording and names introduced by frames or findings. |
| `C.16`, `A.17`, `A.18`, `C.25` | Govern characteristics, scales, measurements, and quality bundles. |
| `C.17`, `C.18`, `C.19`, `G.5`, `G.9` | Govern OEE and NQD candidate, archive and front, pool, selected-set, and parity claims; G.11 currentness remains in the preceding row. |
| `C.11`, `C.24`, `A.15`, `A.20`, `A.21`, `A.10`, `B.3` | Receive decision, call-planning, work, gate, release, evidence, and assurance claims when a quality result is reused beyond evaluation. |

### E.22:End

