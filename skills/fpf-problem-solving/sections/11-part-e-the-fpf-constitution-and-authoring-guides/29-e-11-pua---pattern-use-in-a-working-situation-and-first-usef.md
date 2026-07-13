## E.11.PUA - Pattern Use in a Working Situation and First Useful Result

> **Type:** Pattern-language use pattern (E)
> **Status:** Stable
> **Normativity:** Normative within FPF pattern use from a current practical question to the first directly governed result.

### E.11.PUA:1 - Problem frame

#### E.11.PUA:1.1 - Use this when

Use this pattern when a person or assisting agent has a current entity or relation of concern, a practical question, and one plausible FPF pattern, and needs to turn that pattern's `Solution` into the smallest result that can be used now.

The ordinary working moment is simple: "This pattern looks relevant. What do I do with it, what result should I expect, and when should I stop or return?" The user should be able to answer that question conversationally before any durable pattern-use record is considered.

**Primary EntityOfConcern.** One use of one selected FPF pattern for a current practical question, ending at one exact first result and its realized or explicitly intended receiving use.

**What this buys.** The user gets a direct path from a pattern to a useful subject result without confusing pattern inspection, method description, planning, performed work, and result evidence. A heavier trace remains available when another person, agent, tool, audit, or delayed decision will rely on the distinctions.

**Not this pattern when.** Use `E.11` while several public practical-use cards are still being compared. Use `E.11.PUR` when applicability, recommendation, or coordination among several candidate uses is the current question. Use `E.18.1` when a wider method, plan, work, interpretation, and return flow depends on preservation of accepted problem-side distinctions. Use the A.15 family for intended or performed work.

### E.11.PUA:2 - Problem

Reading a pattern does not by itself apply it. Without an explicit use method, users often stop at recognition, create a meta-card instead of the subject result, or report a plan, note, generated answer, or support record as if the intended physical, clinical, organizational, learned, or epistemic result already existed.

The opposite failure is also common: every bounded use is burdened with a shortlist, candidate form, five fit records, provenance graph, and closure dossier. The paperwork then becomes the apparent result and obscures the direct `Solution` that should guide the work. FPF adds no generic `U.Result`, `U.WorkProduct`, or `U.PatternApplication`: the direct pattern supplies the exact result kind and the relation by which that result enters its receiving use.

### E.11.PUA:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Immediate usefulness | A reader needs a first result, not a tour of the pattern library. |
| Ontological precision | Pattern text, semantic method, plan, dated work, actual result, evidence, and receiving use have different kinds and remain governed by different direct patterns. |
| Light ordinary use | A reversible question with fast feedback should be handled in conversation or a short note. |
| Durable reliance | Transfer, audit, automation, delayed feedback, expensive feedback, or hard reversal can rely on addressable distinctions. |
| Result honesty | A generated description or plan does not establish a physical change, clinical outcome, learned capability, organizational change, or performed work. |
| Flow locality | Pattern selection, selected-pattern application, and downstream subject work can have different results even when one result later supports another flow. |
| Recoverable return | A wrong pattern, missing basis, stronger neighbor, or changed question is represented by a named return rather than silent improvisation. |

### E.11.PUA:4 - Solution

Apply one selected pattern through a short result-oriented procedure. Keep the subject result in the foreground; add addressable pattern-use records only when a named receiving use relies on them.

#### E.11.PUA:4.0 - Kind-preserving dependency spine

The acting `U.System` works under a `U.RoleAssignment`: it selects, constructs, or refines a semantic `U.Method`, records intended work only when planning is current, performs dated `U.Work`, and thereby changes, preserves, examines, or evaluates the real EntityOfConcern. The epistemic support line may guide and evaluate this work; it does not become the actor, role assignment, method, work, or affected entity.

Use this conceptual dependency structure. It states semantic dependencies and possible results, not a workflow, form, interface, serialization, or instruction to materialize every position:

```text
current EntityOfConcern + bounded context + practical question
  -> optional accepted problem-side material when current
  -> public-template or direct-pattern inspection
  -> selected or rejected direct pattern under a fit reason
  -> selected, constructed, or refined U.Method when the Solution makes that method current
  -> PlanItem or U.WorkPlan when intended work is current
  -> dated U.Work when work occurs
  -> exact direct result under its governing pattern
  -> receiving use, stop, return, or neighboring pattern when current
```

`TaskSignature` remains a pre-method-selection signature. It can constrain method search; it is not the task, plan, or work occurrence. OEE and NQD may retain method or architecture candidates before selection. G.5 publishes a selected set; A.3.1 settles method identity; A.15 governs planning and work.

#### E.11.PUA:4.1 - The ordinary seven-step use

1. **Recognize the working situation.** Name the subject or relation in ordinary domain language and ask the current practical question. State an exact kind now only when a nearby kind difference can change the pattern or result.
2. **Inspect one direct pattern.** Read its Problem frame, Problem, Forces, Solution, Consequences, ordinary boundary, and nearest stronger neighbor. Do not select from its title or one trigger word alone.
3. **Say what useful result would answer the question.** Name the result plainly enough to distinguish it from a plan, description, recommendation, work occurrence, or other nearby value. Make kind, relation signature, flow position, and receiving-use relation explicit only when that distinction remains ambiguous or a named later use will rely on replay.
4. **Apply the Solution.** Perform the pattern's action-guiding method under its conditions. A project-tailored method description, WorkPlan, gate result, or work occurrence is created only through its direct governing pattern.
5. **Check what now exists.** The use may have produced a new result, grounded a result that already existed for the current question, or produced only an honest interim result while the subject-result expectation stays open. Do not turn grounding into production.
6. **State the immediate continuation only as needed.** Name the next receiving use, stronger neighbor, or unresolved clarification in conversation. Materialize basis, expectation, result, flow, provenance, or boundary epistemes only when a named later use needs them to remain addressable.
7. **Stop or return.** Stop when the smallest useful produced or grounded result can answer the current question. Return when the concern, basis, expected result, governing pattern, result kind, or receiving-use condition changes.

The practical delta has three honest forms. A result absent before the use may exist afterward. A pre-existing result may remain the same entity while its grounding for the current receiving use becomes adequate. If the subject result still does not exist, the smallest interim result and return condition become explicit while the expectation remains open.

#### E.11.PUA:4.2 - Reliance profiles

```text
PatternUseRelianceProfileValue = ordinaryBounded | relianceBearing
```

In `ordinaryBounded` use, the subject, practical question, inspected pattern, useful result in ordinary language, and stop or return remain recoverable in conversation. State an exact kind or relation signature only when needed to distinguish the result from a nearby value. No candidate basis, fit record, flow-position record, provenance note, or closure record is required.

In `relianceBearing` use, materialize only the distinctions that the named receiving use will rely on. Transfer may need a candidate basis and rationale. Automation may need exact kinds and relation signatures. Delayed review may need the result, flow position, and receiving-use disposition. No profile causes all support records to be materialized.

When one named later use needs a compact replay carrier but not the fuller candidate and closure relations, use this reliance-bearing trace:

```text
CompactPatternUseTrace@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalQuestionDescriptionRef: U.EpistemeRef
  consideredDirectPatternRef: U.EntityRef, referencing one U.MethodDescription
  patternSelectionDisposition: selected | rejected
  compactFitRationaleRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  expectedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  expectedResultDescriptionRef: U.EpistemeRef
  obtainedResultRef?: U.EntityRef
  obtainedResultKindRef?: U.KindRef
  obtainedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  boundaryDisposition: stop | return
  boundaryConditionDescriptionRef: U.EpistemeRef
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
```

The trace is absent from ordinary conversational use. When materialized for a named reliance, the expected-result signature is present exactly when the expected kind admits a relation. A selected pattern may have an obtained result; a rejected pattern leaves obtained-result positions absent. A return names its receiving pattern; a stop does not.

#### E.11.PUA:4.2.1 - Admitted support species and governing patterns

```text
PracticalUseQuestion@Context <: U.Episteme
PatternUseResultExpectation@Context <: U.Episteme
PatternUseBoundaryCondition@Context <: U.Episteme
CandidatePatternUseRationale@Context <: U.Episteme
PatternUseCoordinationRationale@Context <: U.Episteme
PracticalUseCardComparisonRationale@Context <: U.Episteme
PatternUseFitFinding@Context <: U.Episteme
CandidatePatternUse@Context <: U.Episteme
PatternUseApplicabilityFinding@Context <: U.Episteme
```

PUA governs the practical question, optional compact trace, candidate basis, candidate support episteme, candidate rationale, and actual-result closure. `E.11` governs public card comparison rationale. `E.11.PUR` governs fit, applicability, recommendation, coordination rationale, coordination, and ordering. These relations consume A.6.5 SlotSpec discipline; A.6.5 does not govern their identity.

#### E.11.PUA:4.3 - Question, boundary, and expectation

```text
PracticalUseQuestion@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  questionDescriptionRef: U.EpistemeRef

PatternUseBoundaryCondition@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context or PracticalUseQuestion@Context whose use is bounded
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  boundaryConditionKind: candidateAdmission | minimumUsableResult | stop | return | wrongTurnRecovery | strongerNeighbor | costEscalation | reversibilityEscalation | handoff
  conditionDescriptionRef: U.EpistemeRef
  governingPatternRef: U.EntityRef, referencing one U.MethodDescription
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
  conditionalReceivingPatternPositionKindRef?: U.KindRef
  conditionalReceivingPatternPositionRef?: U.EntityRef

PatternUseResultExpectation@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the CandidatePatternUse@Context whose result is expected
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  expectedResultKindRef: U.KindRef
  expectedResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  expectedResultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  expectedResultDescriptionRef: U.EpistemeRef
  minimumUsableResultBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  intendedReceivingPatternRef: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingUseDescriptionRef: U.EpistemeRef
  handoffBoundaryRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The expectation never proves that the result exists. `return`, `wrongTurnRecovery`, `strongerNeighbor`, and `handoff` boundaries name the receiving pattern. The remaining boundary kinds leave that position absent. Receiving-position kind and ref are both present or both absent. `candidateAdmission` means that Problem frame, Forces, Solution conditions, expected result, and ordinary boundary are recoverable enough for further inspection; it is neither an applicability finding nor a selection.

#### E.11.PUA:4.4 - Candidate basis under named reliance

Construct a durable candidate only after inspecting the direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary. A public README template can supply a reusable starting point, but current project values come from the bounded context.

```text
CandidatePatternUseBasisRelation@Context <: U.Relation:
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one U.MethodDescription
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one ProblemCard@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  additionalBasisRelationRefs[]?: U.EntityRef, each referencing one CandidatePatternUseAdditionalBasisRelation@Context
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  RelationRefKind: U.EntityRef
  Direction: <entityOfConcernRef, practicalUseQuestionRef, directPatternRef> -> candidatePatternUseRef
  Dependence: bounded-context local to the direct pattern, question, expectation, and candidate editions
  Identity: <boundedContextRef, entityOfConcernRef, practicalUseQuestionRef, directPatternRef, directSolutionSectionRef, resultExpectationRef, candidatePatternUseRef>

CandidatePatternUseAdditionalBasisRelation@Context <: U.Relation:
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  basisValueRef: U.EntityRef
  basisValueKindRef: U.KindRef
  basisRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  basisGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  basisUseDescriptionRef: U.EpistemeRef
  RelationRefKind: U.EntityRef
  Direction: basisValueRef -> candidatePatternUseRef for basisUseDescriptionRef
  Dependence: bounded-context local to the candidate and basis value editions
  Identity: <candidatePatternUseRef, basisValueRef, basisValueKindRef, basisRelationSignatureRef if present, basisUseDescriptionRef>

CandidatePatternUse@Context <: U.Episteme:
  boundedContextRef: U.BoundedContextRef
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  problemCardRef?: U.EpistemeRef, referencing one ProblemCard@Context
  publicTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  directPatternRef: U.EntityRef, referencing one U.MethodDescription
  directSolutionSectionRef: U.EntityRef, referencing the E.17 PublicationUnit containing the direct pattern's Solution
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  candidateAdmissionBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  returnBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Each additional basis relation names its exact value, kind, relation signature when current, direct governing pattern, and use in this candidate. The public template is absent when the candidate was formed by direct pattern inspection without a README template. `directSolutionSectionRef` is the Solution section of `directPatternRef`; no redundant solution-method-description ref is retained. A project-tailored method description, when produced, is a separate `U.MethodDescription` under A.3.2 with its own derivation or reuse relation to the direct pattern. Applicability, recommendation, and coordination remain governed by `E.11.PUR`.

#### E.11.PUA:4.4.1 - Rationale subjects stay distinct

```text
CandidatePatternUseRationale@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  rationaleDescriptionRef: U.EpistemeRef
  rationaleBasisEpistemeRefs[]: U.EpistemeRef
  rationaleUseBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

Candidate rationale has one candidate subject. `E.11.PUR` owns the coordination-rationale schema over a declared candidate set. `E.11` owns the public-card comparison-rationale schema over one public guidance episteme before a project candidate is constructed. No rationale episteme is a universal bag.

#### E.11.PUA:4.5 - Actual result and receiving-use disposition

Materialize this relation only when a named receiving use relies on addressable closure:

```text
PatternUseActualResultReceivingUseDispositionRelation@Context <: U.Relation:
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  actualResultRef: U.EntityRef
  actualResultKindRef: U.KindRef
  actualResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  resultGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  resultFlowPosition: patternSelectionFlowResult | selectedPatternApplicationFlowResult | downstreamSubjectWorkFlowResult
  resultProducingPathSliceId?: PathSliceId
  resultProducingDesignRunTag?: DesignRunTag
  resultProducingWorkRefs[]?: U.EntityRef, each referencing one U.Work
  receivingUseRealizationState: realized | intendedNotYetRealized
  realizedReceivingUseRelationRef?: U.EntityRef
  realizedReceivingUseRelationKindRef?: U.KindRef
  receivingUseRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  receivingUseGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  intendedReceivingUseDescriptionRef?: U.EpistemeRef
  receivingUseRealizationConditionRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  closureBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  RelationRefKind: U.EntityRef
  Direction: candidatePatternUseRef through resultExpectationRef -> actualResultRef -> realizedReceivingUseRelationRef or intendedReceivingUseDescriptionRef
  Dependence: bounded-context local to candidate, expectation, actual result, and receiving-use editions
  Identity: <candidatePatternUseRef, resultExpectationRef, actualResultRef, resultFlowPosition, receivingUseRealizationState, realizedReceivingUseRelationRef if present, intendedReceivingUseDescriptionRef if present>
```

Candidate, expectation, actual result kind, conditional relation signature, and flow position agree. Path slice and `DesignRunTag` are both present when cross-flow provenance is asserted and both absent otherwise. A result from one flow may become an input, tool, context, or constraint in another flow without changing kind; E.18 carries its new relation position, transfer or crossing relation, and the current `DesignRunTag` boundary.

In the `realized` state, the exact receiving-use relation, kind, and signature are present, while intended-use description and realization condition are absent. In `intendedNotYetRealized`, the intended-use description and realization condition are present, while realized relation positions are absent.

When the actual result is `U.Work`, it names the A.15.1-grounded occurrence and `resultProducingWorkRefs[]` is absent. Planning, setup, authorization, triggering, or enabling work does not become the producer of that occurrence. When dated work produces or changes a result of another kind, each cited work occurrence belongs to the same flow and actually produced or changed that result.

#### E.11.PUA:4.6 - Pre-existing and not-yet-produced results

When the result existed before the current use, preserve that fact:

```text
PreExistingResultGroundingFinding@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the pre-existing result entity
  entityOfConcernKindRef: U.KindRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  candidatePatternUseRef: U.EpistemeRef, referencing one CandidatePatternUse@Context
  resultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  actualResultReceivingUseDispositionRelationRef: U.EntityRef, referencing one PatternUseActualResultReceivingUseDispositionRelation@Context
  currentGroundingBasisRefs[1..*]: U.EpistemeRef
  groundingAdequacyDescriptionRef: U.EpistemeRef
  groundingUseBoundaryRef: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
```

The finding is produced by the current grounding exercise. The grounded entity is not. Earlier producing-work provenance remains absent unless its exact relation and evidence are current.

When the expected subject result does not yet exist, close the current use on the exact interim result, its kind, governing pattern, and flow position. Keep the subject-result expectation open. A plan for machining does not become a machined component; a treatment recommendation does not become a changed clinical state; an assessment plan does not become learned capability.

#### E.11.PUA:4.7 - Reliance-bearing final-practice test

Use this test when the declared teaching, rehearsal, or evaluation use is to establish that a participant can select a pattern, preserve the kind of its result, and leave another participant a replayable continuation. This is deliberately `relianceBearing`: the evaluator relies on the selected basis, expectation, grounding state, and continuation. Its row count is a test condition, not a general rule for pattern use. The test does not require or assert a wider CGUS.

```text
PatternUsePracticeContinuationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  actionOrProposedUseDescriptionRef: U.EpistemeRef
  expectedResultDescriptionRef: U.EpistemeRef
  expectedResultKindRef: U.KindRef
  directPatternIdentifier: PatternIdentifierValue
  directPatternName: PatternNameValue
  currentConditionDescriptionRef: U.EpistemeRef
  continuationDisposition: continue | branch | return | stop

FinalPracticePatternUseTestResult@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the selected CandidatePatternUse@Context
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  practicalUseQuestionRef: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  selectedCandidatePatternUseBasisRelationRef: U.EntityRef, referencing one CandidatePatternUseBasisRelation@Context
  selectedFirstResultExpectationRef: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  selectedFirstResultGroundingState: SelectedFirstResultGroundingStateValue
  selectedFirstResultFlowPosition: PatternUseResultFlowPositionValue
  producedDuringExerciseActualResultRelationRef?: U.EntityRef, referencing one PatternUseActualResultReceivingUseDispositionRelation@Context
  preExistingResultGroundingFindingRef?: U.EpistemeRef, referencing one PreExistingResultGroundingFinding@Context
  notYetProducedInterimResultRef?: U.EntityRef
  notYetProducedInterimResultKindRef?: U.KindRef
  notYetProducedInterimResultRelationSignatureRef?: U.EntityRef, referencing one U.Signature
  notYetProducedInterimResultGoverningPatternRef?: U.EntityRef, referencing one U.MethodDescription
  notYetProducedInterimResultFlowPosition?: PatternUseResultFlowPositionValue
  practiceContinuationDescriptionRefs[3..5]: U.EpistemeRef, each referencing one PatternUsePracticeContinuationDescription@Context
  branchOrReturnContinuationDescriptionRef: U.EpistemeRef, referencing one member of practiceContinuationDescriptionRefs
  continuableWorkStateDescriptionRef: U.EpistemeRef
  explicitUnknownDescriptionRef: U.EpistemeRef
  minimalClarificationPatternRef: U.EntityRef, referencing one U.MethodDescription
  expectedClarificationResultKindRef: U.KindRef
  admittedDemonstrativeSliceRef?: U.EpistemeRef, referencing one DemonstrativeUnfoldingSlice@Context
  demonstratedPatternUseRowRefs[3..5]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
```

Each practice continuation description states an action or proposed use, the expected result and its kind, the full PatternID and pattern name, and the condition under which that continuation is current. Its `entityOfConcernRef` resolves to the same selected `CandidatePatternUse@Context` as the test result. The test passes only when at least one of the three to five descriptions has `continuationDisposition=branch` or `return`, the final continuable work position is explicit, and one consequential unknown names the minimum clarification pattern and expected clarification-result kind. The selected basis relation resolves to that same candidate; the candidate names the same question and expectation as the test result, and the expectation and test result name the same flow position.

The practice descriptions remain ordinary PUA epistemes when no wider CGUS is admitted. If a wider CGUS is later admitted, `admittedDemonstrativeSliceRef` and `demonstratedPatternUseRowRefs[3..5]` are both present or both absent. The rows correspond in order to the existing practice descriptions, and each row's `sourcePracticeContinuationDescriptionRef` points to its corresponding description. They do not replace or retype the descriptions, candidate, subject result, or continuable work position.

`SelectedFirstResultGroundingStateValue` is `producedDuringExercise | preExistingWithGrounding | notYetProduced`. Exactly one state branch is filled:

- For `producedDuringExercise`, fill `producedDuringExerciseActualResultRelationRef` and leave the other state positions absent. The actual-result relation names the selected candidate and expectation. Its result kind, conditional relation signature, and flow position agree with the expectation. The subject result itself was produced during the exercise.
- For `preExistingWithGrounding`, fill `preExistingResultGroundingFindingRef` and leave the other state positions absent. The finding's `entityOfConcernRef` names the already-existing result; the finding agrees with the selected candidate, expectation, and actual-result relation and cites the current grounding basis. The exercise produces the grounding finding; it does not produce the entity that already existed.
- For `notYetProduced`, fill all five interim-result positions and leave both actual-result positions absent. They name the exact result produced by the current test or planning flow, including its kind, governing pattern, flow position, and relation signature when the kind admits one. The interim result may support later work but does not satisfy the selected subject-result expectation.

The continuable-work description says what project work can proceed from this state-specific result. The test fails when it merely retells a card, expands into a whole-project plan, treats a public template as a recommendation, claims performed work without an A.15.1-grounded `U.Work`, infers a physical, clinical, organizational, or learned change from its description, or asserts a CGUS only because the practice contains several rows.

#### E.11.PUA:4.8 - Replay and currentness

For immediate `ordinaryBounded` use, recover from the conversation the working subject and question, the direct pattern inspected, the useful result produced or grounded, and the stop or return. Do not reconstruct a candidate dossier merely to replay a cheap local use.

When a named later use relies on fuller replay, recover the exact concern, bounded context, practical question, selected direct pattern and edition-pinned Solution, expected result kind and conditional relation signature when applicable, flow position, grounded actual or honest interim result, receiving-use disposition, and stop or return boundary from the support relations materialized for that reliance.

Recheck the smallest affected claim or relation when the concern, candidate basis, direct Solution, expected result, result grounding, flow position, receiving-use condition, or boundary changes. Reopen pattern selection only when that change alters candidate fit; a new measurement of the same result does not by itself select another pattern. `G.11` governs edition, telemetry, currentness-window, and decay orchestration; PUA supplies the use-specific values and change conditions that orchestration inspects.

### E.11.PUA:5 - Archetypal Grounding

#### E.11.PUA:5.1 - Episteme result: a usable problem card

A team has a vague recurring pump-failure concern and asks whether it can be articulated well enough to guide later method selection. In ordinary conversation the team says: "Use C.22.2 to make the pump-failure concern into a usable problem card." It inspects C.22.2, applies the Solution, obtains the card, and stops once the current question is answered.

The card's `ProblemCard@Context` kind and application-flow position remain recoverable from C.22.2 when a later distinction needs them; the team need not state or record those fields during this cheap use. A durable closure or receiving-use relation is created only when the later P2W use or another named receiving use relies on replay.

#### E.11.PUA:5.1a - Evaluation specification without a ProblemCard

An architecture team already has a bounded comparison question but no accepted `ProblemCard@Context` is needed for this use. It applies `A.19.ECS` and produces an `EvaluationCharacteristicSpaceSpec` with declared coordinates, scales, comparators, and evidence rules. The optional `problemCardRef` remains absent. The exact episteme is the `selectedPatternApplicationFlowResult`; when the later comparison actually uses it, the receiving-use relation records that realized use without opening P2W.

#### E.11.PUA:5.1b - A selection result can support later planning

Pattern-selection work under E.11.PUR produces a `PatternUseRecommendation@Context`. That recommendation is a `patternSelectionFlowResult`. A later PUA use applies the recommended planning pattern and produces a `U.WorkPlan` as a separate `selectedPatternApplicationFlowResult`. E.18 may relate the recommendation to the later use through an explicit crossing, but neither the recommendation nor the plan becomes the machined component expected from downstream subject work.

#### E.11.PUA:5.1c - AI-assisted ordinary use returns the subject result

An engineer asks an AI assistant to apply an already selected `A.19.ECS` pattern to a pump-comparison question. The needed result is an `EvaluationCharacteristicSpaceSpec` with admitted coordinates, scales, comparators, and evidence rules. No later use asks for a durable pattern-selection trace.

The assistant returns that specification as the `selectedPatternApplicationFlowResult` and keeps the concern, pattern fit, and stop condition recoverable in the conversation. It does not add candidate, fit, applicability, rationale, or closure records merely because an AI assisted the use. If the available basis cannot support the specification, it names the unresolved coordinate, scale, comparator, or evidence-rule position, returns the use to `A.19.ECS`, and leaves the completed-specification expectation open. Materialize that return as `PatternUseBoundaryCondition@Context` only when a named reliance needs an addressable boundary; do not emit a complete meta-record stack.

#### E.11.PUA:5.2 - Physical result: work is still future

A machining team inspects a planning pattern for a dimensionally accepted component. Applying the selected pattern produces a `U.WorkPlan`. The metal blank remains unchanged.

The plan is an honest `selectedPatternApplicationFlowResult`. The component remains an expected `downstreamSubjectWorkFlowResult` until dated machining work occurs. The team may continue with the A.15 work patterns; it cannot fill the component result position with the plan, simulation, inspection checklist, or generated prose.

After the dated machining `U.Work` occurs, the actual-result relation names the dimensionally accepted physical component or changed physical state in `downstreamSubjectWorkFlowResult` position and cites only work occurrences that produced or changed it. An inspection record may support evidence or description use; it does not replace the physical result.

#### E.11.PUA:5.3 - Clinical result: a state and its note stay separate

A clinician uses a direct pattern to structure a treatment decision. The application produces a treatment-plan episteme and an intended receiving use. The patient's changed clinical state does not yet exist merely because the plan is accepted.

After treatment work occurs, the clinical state and the case-note episteme can both be current, but they keep different kinds and governing relations. The note may support grounding and later reliance; it does not become the patient's state.

If the clinically relevant state existed before the current pattern use, record `preExistingWithGrounding` and produce a `PreExistingResultGroundingFinding@Context` from the current examination or accepted evidence. The examination grounds use of the state for the present question; it does not produce that state or supply an unknown earlier treatment history.

#### E.11.PUA:5.3a - Learned capability and assessment remain separate

Teaching work is performed under its direct educational and A.15 patterns. A later assessment may support a claim that the learner has demonstrated a bounded capability or skill. The capability result and the assessment episteme keep different kinds and governing relations: a completed lesson, assessment plan, or filled assessment record cannot occupy the learned-capability result position by itself.

#### E.11.PUA:5.4 - Pre-existing result: inspection does not reproduce it

A maintenance engineer inspects an installed pump that predates the current pattern use. Current measurements adequately ground the pump for a compatibility question, but the historical production relation is outside the evidence basis.

Use `PreExistingResultGroundingFinding@Context` for the present grounding. Keep producing-work provenance absent. The current inspection neither manufactures the pump nor proves how it was manufactured.

#### E.11.PUA:5.5 - Repair a plan-as-component closure locally

A machining rehearsal selected the correct planning pattern and produced a valid `U.WorkPlan`, but its closure named the plan as `downstreamSubjectWorkFlowResult` and treated the component expectation as satisfied. The concern, candidate basis, direct pattern, and WorkPlan remain sound.

Repair the expectation and actual-result closure: name `U.WorkPlan` as the `selectedPatternApplicationFlowResult`, remove the claimed component actual result and any realized receiving-use relation that depended on it, and keep the component as an open downstream expectation. The next current use enters the A.15 work family. No new candidate selection or reconstruction of the WorkPlan is needed.

#### E.11.PUA:5.6 - Complete trace, absent result

An automated report raises pattern-use trace completeness to 100 percent by filling every candidate, rationale, expectation, and boundary position. Operators begin treating the green report as completion, while actual-result grounding and the intended receiving use remain absent more often.

The trace measure improved while subject progress worsened. Keep completeness as a trace-quality measure, apply `E.13` to the substitution, and evaluate PUA success from the exact grounded result or honest interim result, its flow position, and its receiving-use disposition. Empty actual-result positions are not repaired by adding more support records.

### E.11.PUA:6 - Bias-Annotation

- **Recognition-only bias.** A matching title or trigger word is treated as application. Repair by inspecting the direct pattern's full problem and solution conditions and naming the expected result.
- **Record-as-result bias.** A candidate form, trace, note, dashboard, or assessment record replaces the subject result. Repair by restoring the exact result kind and its direct governing pattern.
- **Plan-as-work bias.** Intended work or a generated plan is reported as performed work. Return to A.15 and ground the dated occurrence before asserting `U.Work`.
- **Flow-collapse bias.** A selection result, application result, and downstream-work result are merged because each is called "result". Restore the flow-local result position and any current E.18 crossing.
- **Maximum-trace bias.** Every use emits every schema. Return to the named reliance and materialize only distinctions that it will use.

### E.11.PUA:7 - Conformance Checklist

| ID | Check | Passing condition |
| --- | --- | --- |
| `PUA-1` | Current concern | The working subject or relation and practical question are recognizable in domain language before the PatternID; an exact kind is explicit only when a nearby kind difference changes the use. |
| `PUA-2` | Direct inspection | Problem frame, Problem, Forces, Solution, Consequences, ordinary boundary, and stronger neighbor were inspected. |
| `PUA-3` | Useful result | Ordinary use distinguishes the useful result from nearby values; exact kind, conditional relation signature, flow position, and intended receiving use are explicit only when ambiguity or named reliance makes them necessary. |
| `PUA-4` | Reliance profile | Ordinary use remains conversational; every materialized support record names the receiving reliance that needs it. |
| `PUA-5` | Honest closure | The use says whether it produced a new result, grounded a pre-existing result, or produced only an interim result. A materialized closure carries exact kind, governor, and flow position only under the conditions stated above. |
| `PUA-6` | Work integrity | `U.Work` names an A.15.1-grounded occurrence and has no producing-work position. Other results cite only same-flow work that produced or changed them. |
| `PUA-7` | Receiving use | The immediate continuation is understandable in ordinary use; realized and intended-not-yet-realized record positions are filled only when a named reliance materializes that relation. |
| `PUA-8` | Return | Changed concern, basis, result, pattern, or use opens a named return instead of silent reinterpretation. |

### E.11.PUA:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| Select from the pattern name | Similar symptoms can have different problem frames and forces. | Inspect the direct pattern and state the result that would answer the current question. |
| Fill the candidate record first | The record freezes a choice before the Solution and boundary are understood. | Inspect first; materialize the candidate only for a named reliance. |
| Report generated text as the result | Text can describe a physical, clinical, organizational, or learned result without producing it. | Name the exact interim episteme and leave the subject expectation open. |
| Treat a support record as proof | A well-formed record proves only that fields were written. | Ground inspection, work, result, evidence, and receiving-use relations through their direct patterns. |
| Copy a result between flows | The same entity may occupy a new relation position, but its kind and provenance do not change by narration. | Use E.18 transfer or crossing relations and keep each flow-local result position. |

### E.11.PUA:9 - Consequences

**Benefits.** A cold reader can apply one pattern and reach a useful result without learning a meta-workflow. Ordinary use remains light, while high-reliance use can preserve basis, expectation, result, and receiving-use distinctions. Physical, clinical, learned, organizational, work, and epistemic results receive the same kind discipline without being forced into one product family.

**Costs.** A success claim is complete only after the result kind and stop condition are named. Reliance-bearing use adds addressable epistemes and relations. Cross-flow uses are represented through explicit E.18 positions instead of one narrative chain.

### E.11.PUA:10 - Rationale

FPF patterns are action-guiding method descriptions, but readers meet them in concrete situations. The missing middle is neither discovery nor recommendation: it is the disciplined application of one selected `Solution` to obtain the first result that the situation can use.

Separating ordinary semantic checking from conditional record materialization protects both usability and rigor. A conversation can be sufficient for a bounded reversible question. A transfer, audit, automated use, or expensive decision can demand addressable support. The same ontology serves both profiles; only the reliance changes the recording granularity.

The first result boundary prevents proxy completion. A plan, note, simulation, or assessment may be valuable and may be the exact result of the current pattern application. It cannot stand for a later physical, clinical, organizational, or learned change. Stop where the current pattern actually produced value, then continue under the pattern that governs the next work.

### E.11.PUA:11 - SoTA-Echoing

| Source or practice line | Problem-solving move taken here | Adoption and boundary |
| --- | --- | --- |
| Pattern-language practice: situation recognition, conditional solution, consequences, and neighboring-pattern composition | Begin with direct inspection of the full pattern rather than title matching, then apply one conditional Solution to a bounded result. | Adopt the conditional-use logic. Reject recipe following and pattern-ID matching as sufficient application. |
| Jin, Bai, and Oulasvirta, *Modeling Trial-and-Error Navigation With a Sequential Decision Model of Information Scent*, arXiv:2603.11759 (2026) | Make bounded inspection, wrong-turn recognition, and explicit return part of the ordinary use rather than assuming one perfect first selection. | Adapt the navigation result to pattern use. The preprint does not decide FPF ontology, shortlist size, or whether records are needed. |
| Current FPF `A.10`, `B.3`, `E.18`, `C.2.1`, and `G.11` evidence, assurance, flow, support-episteme, and currentness practices | Keep basis, result kind, receiving use, and flow provenance addressable when another participant or system will rely on them later. | Adapt conditionally through `relianceBearing`; reject universal trace production for cheap reversible use and keep evidence, assurance, and currentness claims with their governing patterns. |
| Current FPF `E.11`, `E.11.PUR`, and A.15 | Separate public discovery, one selected-pattern use, recommendation or coordination, intended work, and performed work. | Adopt as the governing ontology for those boundaries. PUA adds only the user-side use method and its dependent relations. |

The practical implication is direct: inspect enough to detect a wrong turn, record only what a named later use needs, and never infer a subject result from the existence of its trace.

Conditional pattern use is the lineage anchor, not a claim that traditional pattern-language practice already supplies PUA's result and flow ontology. Recipe following, PatternID matching, and universal trace production are the common comparators; PUA rejects them because they respectively hide conditions, substitute names for inspection, or spend apparatus without a receiving reliance.

The 2026 navigation study is a current preprint anchor rather than settled consensus. Reopen its wrong-turn and return adaptation when peer review, replication, or use evidence changes the observed value of inspection, memory, or backtracking. Reopen the `ordinaryBounded` and `relianceBearing` split when real receiving uses repeatedly lose needed distinctions or pay trace cost without later use. `G.11` orchestrates that evidence and currentness; PUA changes the profile boundary or exact support relations.

### E.11.PUA:12 - Relations

- **Builds on:** `E.11` for public practical-use guidance, `E.8` for action-guiding pattern form, `E.18` for coupled-flow positions, `A.15` for planning and work, `C.2.1` for support epistemes, and `A.6.5` for slot discipline.
- **Coordinates with:** `E.11.PUR` for applicability, recommendation, and coordination; `E.18.1` for accepted problem-to-work carry-through; `E.22` and `E.23` for evaluation and repeated improvement; `G.11` for currentness orchestration; and each direct pattern that governs the selected result.
- **Returns to:** `E.11` when no direct pattern is yet selected, `E.11.PUR` when recommendation or ordering among several candidate uses is current, and the exact subject pattern when the result or work claim leaves PUA's boundary.

### E.11.PUA:End

