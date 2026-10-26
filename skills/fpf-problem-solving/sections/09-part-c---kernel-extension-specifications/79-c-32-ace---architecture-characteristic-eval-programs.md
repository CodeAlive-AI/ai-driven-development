## C.32.ACE - Architecture Characteristic Eval Programs

> **Type:** Architecture eval-support subpattern under C.32
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.32.ACE:1 - Problem frame

Use this pattern when an architecture team already has project architecture-characteristic rows and must evaluate the current architecture, compare candidate architectures, monitor evolution, or prepare a selection input.

Primary working reader: an architect or evaluator preparing readings over declared architecture-characteristic criteria without turning those readings into the criteria or the decision.

Typical entry phrases:

```text
"We have criteria rows; which eval reading shows how candidate A and candidate B compare under the same parity frame?"
"The monitor is useful, but is this a reading, a test failure, or a decision input?"
"Two methods, roles, system variants, or AI workflows need fair comparison against the same architecture characteristics."
```

**First-minute use slice.** A product-family team has ACS rows for substitutability, evidence reuse, and latency, plus safety as a monitored guardrail. Two candidate architectures look plausible. The practitioner writes one ACE program record with the same claim scope, selected context slices, reference scheme and plane, evaluation window, parity frame, and input projections for both candidates. `EvalService-7` first has the A.13 core for candidate evaluation, and A.15.1 independently admits `CandidateEvalWork-42`, which enacts `ArchitectureCandidateEvaluationMethod-7` and occurs within `ProductFamilyEvaluationService-7`. This first-minute record expressly represents precise evaluator attribution under `EvaluatorAssignment-3`, an obtaining occurrence of directly declared species `EvaluatorAssignment`, so it also includes the separate F.6 relation through the same A.13 assignment. A Work-only ACE record would omit those assignment and attribution refs, and failed F.6 attribution alone would leave `CandidateEvalWork-42` intact while its independent A.13/A.15.1 grounds still hold. `CandidateLatencyReading-42` and `CandidateEvidenceScopeFinding-42` are typed results established through their result patterns. Those results can become inputs for `A.19.CPM` comparison or the next C.32 synthesis pass; neither the program record, Work, nor a result defines the criterion or decides the architecture.

This pattern frames architecture evaluation over declared criteria rows, Q-Bundle slots, candidates, bearers or selected structures. Use a parity frame when the receiving inference depends on comparable conditions. The optional record below uses a C.32.ACE-local form and introduces no new U-kind. Its program label establishes neither Method or MethodDescription membership, a WorkPlan, dated Work, nor an evaluation result. When measurement validity, comparison policy, a selection result, G.5 result declaration, publication, or architecture decision is current, use the definition and test for that claim.

Ordinary working move: choose the declared criteria rows, bind the claim scope, relevant context slices, reference scheme and plane, evaluation window, and input projections, and establish parity for the variants when comparison depends on it. When a particular actual evaluation Work occurrence is claimed, recover each exact evaluator through A.13 and let A.15.1 independently admit the `U.Work` occurrence. Add `evaluationWorkAttributionRefs` only when the program or receiving use expressly represents precise assignment-bound attribution; missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold. Any A.6.1 operation application is an additional relation, not a substitute for the Method enacted by the Work. Return the typed results established through their result patterns as feedback for comparison or the next synthesis pass.

The first useful result explains how a bounded architecture evaluation will obtain the result needed by the receiving use. An ordinary account can suffice; use `ArchitectureCharacteristicEvalProgram@Project` when a record helps preserve that framing. When a reusable way of evaluating is current, identify that separate `U.Method` under A.3.1; when a claim-bearing episteme describes that exact Method, test the same episteme for `U.MethodDescription` under A.3.2. A planned evaluation belongs to A.15.2, an actual dated evaluation to A.15.1, and each result to its direct measurement, comparison, evaluation, or assertion pattern. Use the record to frame readings of characteristics through rows, slots, candidates, or structures; it is not any of those neighboring objects.

For a first pass, make the claim scope and selected context slices, reference scheme and plane, evaluation window and input projections, evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame when required by the receiving inference, eval purpose, intended eval operation, result form, receiving use, and refresh or retire condition recoverable. Add project-use refs only for a claimed project-local program; add Method, MethodDescription, actual evaluation Work, operation-application, and typed-result refs only when those separate objects are current.

```text
ArchitectureCharacteristicEvalProgram@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureEvalProgramProjectUseRelationRef?: U.RelationRef governed by the exact eval-program-use or work-use pattern
  claimScopeRef: U.EntityRef referencing one U.ClaimScope
  selectedContextSliceRefs:
  effectiveReferenceScheme:
  referencePlane?:
  evaluationWindow:
  inputProjectionRefs:
  evaluatedCriteriaSetRef:
  evaluatedCriteriaRowRefs:
  evaluatedQBundleSlotRefs?:
  evaluatedCandidateRefs?:
  evaluatedBearerOrSelectedStructureRefs:
  evalPurpose: characterizeCurrentArchitecture | compareCandidates | monitorEvolution | prepareSelection | triggerNextSynthesis
  evalQuestion:
  parityFrameRef?: when the receiving inference depends on comparable conditions
  evalScope: singleCriterion | coupledCriteria | qBundleSlice | variantPortfolio | holisticUseSlice
  evalOperation: measurement | simulation | benchmark | scenarioWalkthrough | test | monitor | expertReview | evidenceAudit
  triggerMode: onePass | batchComparison | continual | onChange | manualOnDemand
  resultForm: reading | band | rank | dominanceRelation | tradeoffFront | qualitativeState | evidenceFinding
  runContext: designTime | laboratory | pipeline | production | workReview | decisionPrep
  measurementOrObservationMethodRefs:
  methodDescriptionRefs?:
  evaluationWorkRefs?: FinSet(U.EntityRef constrained to U.Work)
  evaluationWorkAttributionRefs?: FinSet(U.RelationRef constrained to obtaining performedUnderAssignment relations)
  evaluationOperationApplicationRefs?: subject-pattern relation or A.6.1 application references
  evaluationResultRefs?: typed result references accepted under the definition and test for each result
  uncertaintyAndMissingDataPolicy:
  proxyRisk: material risk, unresolved risk, or reason no material proxy risk was identified
  protectedCounterCharacteristicRefs?: when a loss needs protection
  comparisonPolicyRef?:
  receivingUseRef:
  refreshOrRetireCondition:
```

Here `@Project` is a compatibility and retrieval cue only. It supplies no project entity, composite-work identity, context, authority, viewpoint, or parthood. A program local to one actual project names both the composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining program-use relation in `architectureEvalProgramProjectUseRelationRef`; either field alone is insufficient. `evalOperation` states the intended operation family in the program record, not an actual run or application. Each `evaluationWorkRef` names one independently identified `U.Work` occurrence whose exact actual performers have A.13 cores and which A.15.1 admits independently. `evaluationWorkAttributionRefs` are optional and appear only when the record or receiving use expressly represents precise assignment-bound attribution; any present ref resolves through F.6 to the same obtaining A.13 assignment, and its absence or failure does not invalidate the Work ref. Any A.6.1 application binding and each typed result remain under the applicable patterns. A program, Method, MethodDescription, Work occurrence, operation application, assignment, attribution, and result never substitute for one another.

What goes wrong if C.32.ACE is missed: a project has architecture-characteristic rows but treats a test, monitor, dashboard, or source-side "fitness function" as the criterion or as the decision. The team may then reject useful losing variants as errors, optimize one indicator, or choose a candidate without fair comparison.

What C.32.ACE buys in practice: eval work is framed as typed evaluation over declared architecture criteria. A losing candidate can still add knowledge about the solution space, while an actual error remains a failure against an expectation that causes unplanned rework.

The result identifies the candidates, bearers or structures, the conditions of evaluation, the intended result form and its receiving use. A comparative inference retains its parity conditions. An actual result is established separately under the rule for its result kind.

Not this pattern when the characteristic rows do not exist yet. Also not this pattern when the current work is measurement validity, composite-quality modeling, explicit comparison, set-returning selection, local choice, selected-set result declaration, actual publication, evidence, assurance, or project architecture decision.

Common exits by claim kind:

- `C.32.HCS` and `C.32.ACS` before characteristic rows exist.
- `C.16` for measurement validity, readings, units, uncertainty, or comparability claims.
- `C.25` for Q-Bundles and composite quality families.
- `E.13` when an eval result or dashboard starts replacing the declared architecture concern.
- `C.32` for candidate synthesis, `C.32.MLAO` for residual input, and `E.23` for repeated improvement feedback.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for selected-set result declaration. For publication, use E.24.PUB for the occurrence and audience availability, and E.17 when a source-backed face and source return are needed.
- `A.10` and `B.3` when evidence or assurance claims are being made.
- `C.32.PAD` for project decision.

### C.32.ACE:2 - Problem

Architecture synthesis is an optimization and learning activity under competing characteristics. It needs evals: deliberate measurement, simulation, benchmark, scenario, review, or monitoring runs that say how a current architecture or candidate architecture reads against declared criteria.

Testing for errors is a neighboring use. A test asks whether an expectation is violated. An eval asks how variants compare, how a candidate changes the trade-off front, which constraint is hit, or whether the next synthesis pass should open. A candidate that loses the eval is not automatically an error; it may be a deliberate probe that improves the architecture team's knowledge of the solution space.

Evolutionary-architecture sources often say "fitness function". Recover the operation, rule or expression meant by that source term before identifying its FPF use. When an architecture evaluation needs framing over declared criteria or structures, use this pattern; an individual test, monitor or expression keeps its own meaning within that framing. Automation does not change the kind of the program record.

### C.32.ACE:3 - Forces

| Force | Tension |
|---|---|
| Variant learning | Candidate architectures may be valuable even when they lose the selection being made. |
| Fair comparison | Comparison needs the context, budgets, windows, scale-appropriate units and missing-data treatment on which its inference depends; other results retain their own use conditions. |
| Trade-off pressure | Improving one architecture characteristic can worsen another. |
| Automation value | Frequent automated evals reveal drift early, but their results can be overread. |
| Error prevention | Some eval operations are tests, yet error checking must not replace variant comparison. |
| Evolution | A useful eval can expire when the source-currentness relation, environment, declared holon-level ref, or scale window changes. |

### C.32.ACE:4 - Solution

Create an architecture-characteristic eval program only after the evaluated criteria rows exist in `C.32.ACS` or a declared C.25 Q-Bundle slot.

Work in this order:

1. Reference the evaluated ACS criteria set, evaluated rows, and any Q-Bundle slots.
2. State the eval purpose: current characterization, candidate comparison, portfolio-frontier work, post-change impact measurement, monitoring, or trigger for the next synthesis pass.
3. Name the candidates, bearers, and selected structures being evaluated.
4. Establish one exact `U.ClaimScope`, the relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, evaluation window, input projections, resource budget, units (when required by the scale), admissible observation or evidence inputs, and missing-or-unknown policy. When the intended inference relies on parity, establish the required comparable conditions and use `parityFrameRef` if a record is useful. The frame does not replace the underlying bindings.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. Use measurement, simulation, benchmark, scenario walkthrough, monitor, review, or evidence audit according to the claim. Use `test` only when the intended operation checks an expectation or hard constraint. When a particular actual evaluation Work occurrence is claimed, recover each evaluator's A.13 core and let A.15.1 independently admit the occurrence from its history, Method actually followed, extent and containing-System relation. Add `evaluationWorkAttributionRefs` only when the record or receiving use expressly represents precise assignment-bound attribution. Add an operation-application relation only when that claim is needed and its predicate obtains. Establish the typed result separately; the program record itself does not run.
7. Declare the result form. Examples include a reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding; use the definition and test for the actual result kind.
8. Examine material proxy risk before the eval result drives work, and protect the characteristics or constraints it could compromise. If no material risk is found, retain that basis. Optimize only the chosen indicators; keep binding constraints and other necessary safeguards visible.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for a selected-set result declared under `G.5`, or architecture-decision input for `C.32.PAD`. For publication input, distinguish `E.17` source-backed face and source return from the `E.24.PUB` publication occurrence and audience availability.
10. When a criterion, candidate, bearer, structure, environment, parity condition or source premise changes, identify which evaluation dependence is affected. Revise or retire the program if its operation or conditions no longer support the receiving use; retain it when its grounds still apply.

**Stop condition.** Stop C.32.ACE when the account makes the evaluated rows or slots, subject, purpose, operation, result form, receiving use and necessary conditions recoverable, including parity for a dependent comparison and material proxy risks or protected losses. Retain an adequate existing evaluation program; a changed premise identifies what to revisit.

**Lowering condition.** Use each result only for claims supported by its evaluated subject, criteria, operation and conditions. Missing data, uncontrolled proxy risk or failed parity blocks the inference that depends on it; retain independently usable readings and qualified reports. Publishing such a report does not itself claim the unavailable comparison or decision. Reuse a program for new candidates when its conditions still apply, or revise the affected operation when they do not. Use ACS for a missing or wrong criterion, C.16 for measurement validity and C.25 for a composite quality; comparison, evidence, assurance and decisions retain their own rules.

### C.32.ACE:5 - Worked slices

**Latency candidate.** A service candidate promises latency under 100 ms and an eval reads 240 ms. If the 100 ms band is a hard constraint, the candidate is inadmissible for this cycle. If the project is still exploring a trade-off front, the candidate misses the latency target while supplying useful evidence about resource placement, interface burden, or control separation. Treat it as an error only when the project used that expectation to plan work and unplanned rework follows.

**BIM digital twin.** A built-asset team compares architecture candidates that combine placement, schedule, use-phase, maintenance, and cost structures. ACE does not treat the number of dimensions as the evaluation. The practitioner defines a parity frame and evals the ACS rows declared for the project, such as access, source-return cost, observability, and maintenance reach, then records results with the parity-frame and result-form fields needed by `A.19.CPM`.

**Method-family architecture.** A review-Method family has ACS rows for evidence reuse and change reach. If source wording also says “role substitutability,” use `E.10.ROLE` and `C.32.ACS` to bind the exact recovered subject and predicate—such as substitutability among local system-role kinds under A.2.7, not among holders or assignments—before ACE evaluates it. A separate C.25 bundle covers teachability. ACE defines a batch evaluation over three Method variants. One variant loses on teachability but reveals a reusable evidence relation; C.32 may use it as a stepping stone.

**AI-agent workflow.** A model-supported workflow has candidates with different function graphs and tool boundaries. ACE evaluates latency, evidence refresh, policy controllability, and rollback under the same task set and evidence window. A benchmark score is not the architecture decision; it supplies one eval reading inside the parity frame.

**Hospital escalation.** A hospital escalation team has ACS rows for decision latency, accountability clarity, and evidence custody. Any source “role continuity” or “role-boundary” criterion first goes through `E.10.ROLE` and `C.32.ACS`, which binds the exact subject and predicate—such as continuity of assignment occurrences and their holder Systems, or a boundary among exact participant relations. ACE evaluates two recovered architecture variants under the same incident scenarios and handoff evidence window. The result can feed comparison or the next synthesis pass; staffing choice remains with the receiving decision pattern.

### C.32.ACE:6 - Kind and Receiving-Claim Boundary

Use C.32.ACE to frame the architecture evaluation, using its local record when useful, and to keep criterion, reusable evaluation Method, MethodDescription episteme, intended operation family, planned evaluation, actual dated evaluation Work, actual operation application, typed result, comparison input, selection input, and decision input distinct. The local record admits no new U-kind. Use A.3.1, A.3.2, A.15.2, A.15.1, and A.6.1 for their respective objects and relations; use the pattern that defines and tests each actual result. C.32.ACE does not define starter characteristic selection, ACS scale-row construction, measurement validity, Q-Bundle normal form, candidate synthesis, comparison policy, final selection, local choice, G.5 selected-set result declaration, publication, or an architecture decision. When those claims are current, use `C.32.HCS`, `C.32.ACS`, `C.16`, `C.25`, `C.32`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, or `C.32.PAD` as applicable. For publication, use E.24.PUB for the occurrence, form, carrier, audience, bounded use and availability, and E.17 when a source-backed face and source return are needed.

### C.32.ACE:7 - Conformance requirements

| Requirement | Required result |
|---|---|
| `CC-ACE-1` | Every eval references declared ACS rows or C.25 Q-Bundle slots. |
| `CC-ACE-2` | Every eval names evaluated candidates, bearers, or selected structures. |
| `CC-ACE-3` | Purpose, scope, eval operation, trigger mode, result form and run conditions are recoverable; parity is established when the receiving inference depends on it. |
| `CC-ACE-4` | Measurement claims require `C.16`; composite quality claims require `C.25`. |
| `CC-ACE-5` | Before receiving work relies on an eval result, its missing-data treatment and material proxy risks are understood, with relevant constraints and counter-characteristics protected. |
| `CC-ACE-6` | Source-side "fitness function" wording retains its source meaning; any FPF object or claim is identified by the operation, expression or relation actually meant. |
| `CC-ACE-7` | A check or test is admitted only as one eval operation when an expectation or hard constraint is being inspected. |
| `CC-ACE-8` | The eval result does not select, decide, certify, or carry an architecture-adequacy claim by itself. |
| `CC-ACE-9` | A project-local program names both `projectWorkOccurrenceRef` and `architectureEvalProgramProjectUseRelationRef`; the suffix or either reference alone asserts no locality. |
| `CC-ACE-10` | The record separately identifies any reusable Method, MethodDescription, planned evaluation, dated evaluation Work, actual operation application, and typed result that the use needs; `evalOperation` or `resultForm` supplies none of those occurrences or identities. |
| `CC-ACE-11` | Every actual evaluation use binds one exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, evaluation window, and input projections; `evalScope`, `runContext`, and `parityFrameRef` do not replace them. |

### C.32.ACE:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `SourceFitnessTermAsFPFObject` | The source label "fitness function" hides which operation, rule or expression is meant. | Recover that source meaning. Frame the needed architecture evaluation through ACE while retaining the actual function, test or monitor as its own contribution; an ordinary source-local label may remain. |
| `EvalAsCriterion` | A benchmark, monitor, or test is named as the architecture characteristic. | Return to ACS; name the criterion, bearer, scale, proxy risk, and protected counter-characteristics before writing the eval. |
| `TestModeAsEvalWhole` | The team only asks whether one candidate passes while the work question is variant comparison. | Keep the test for the hard constraint, then add eval result forms that compare candidates or expose the trade-off front. |
| `UnfairComparison` | Candidates are compared under different budgets, evidence windows, environments, or missing-data rules. | Establish the comparison's required parity or withhold the unsupported comparative inference. Retain readings that remain usable under their own conditions. |
| `ResultAsDecision` | A rank, score, pass, or dashboard reading selects the architecture. | Treat the result as source material for an A.10 evidence-provenance account when an evidence claim is current, or as comparison input when comparison is current. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. For publication, use E.24.PUB for the occurrence and audience availability, and E.17 when a source-backed face and source return are needed. |
| `SingleIndicatorGoodhart` | Work improves one optimized indicator while an unmeasured architecture concern worsens. | Limit optimized indicators, add protected counter-characteristics, and open `E.13` when proxy-to-value drift appears. |
| `LosingVariantAsError` | A candidate that lost a planned eval is recorded as a mistake. | Record it as a variant result unless an expectation caused unplanned rework; keep useful learning in the variant archive. |
| `ProgramAsRunOrResult` | The ACE record is said to execute, measure, evaluate, or produce the result, or one generic `resultRef` hides the result kind. | Recover each exact evaluator through A.13 and let A.15.1 independently admit the evaluation `U.Work`. Add an attribution ref only when the record expressly represents precise assignment-bound attribution; missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold. Add an operation application only when it independently obtains, and identify the typed result under the applicable pattern; keep the ACE record as the evaluation framing record. |

### C.32.ACE:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Evals are typed evaluations over declared criteria. | Variant comparison can proceed without collapsing criteria, readings, and decisions. | The receiving inference must have its required conditions; comparative use needs the applicable parity basis. |
| Expectation-failure tests remain one eval operation when their expectation is declared. | Error prevention remains available without replacing optimization. | Some pass-fail dashboards can no longer drive decisions by themselves. |
| Losing variants remain useful. | Architecture exploration keeps stepping stones and source-space learning. | The variant archive needs deliberate upkeep. |
| Proxy and counter-characteristic risks are explicit. | Goodhart pressure is visible before eval results drive work. | More rows may remain monitored as guardrails rather than optimized. |

### C.32.ACE:10 - Rationale

An architecture-characteristic eval program connects declared criteria to the evaluation result needed by receiving work. It explains what will be observed or derived, under which conditions, and how that answer can be used. A comparison adds the parity conditions on which its inference depends; every actual answer comes from its independently established result kind. It does not answer "what is the criterion?", "is the measurement valid outside this use?", or "which architecture must be chosen?"

The pattern is architecture-specific because it evaluates selected structures and architecture characteristics. The same eval form can be used in system, organization-as-system, built-asset, episteme, work-occurrence, discipline, AI-agent-setup, and C.36-recovered cultural-evolution cases once the admitted holon being described has been identified in each case. It can also evaluate Method-side, Work-side, evidence-side, local-kind, classification, or assignment structures after the described holon, the defining or constraining ClaimGraph located through the subject pattern, the bearer and predicate, and the scale rows are rebound. Unresolved “role” wording goes through `E.10.ROLE`; the pattern does not admit Methods, roles, practices, or cultures as holon kinds by label.

### C.32.ACE:11 - SoTA-Echoing

These rows document how source practice contributes to eval-program fields, result-use boundaries, and refresh conditions in C.32.ACE.

| Source to inspect | Why this source is load-bearing here | Transfer into ACE | Blocked overread |
|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | Separates variant, prototype, candidate, stake, solution, error, eval as variant comparison, and testing as error checking; also requires fair comparison and indicator selection. | Make eval a typed architecture evaluation over declared candidates and criteria. | A pass-fail result alone does not identify the evaluation question, criterion or receiving decision. One test can be sufficient when it answers the whole stated evaluation question. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Practitioner source for incremental architecture governance and feedback under source-side fitness-function terminology. | Recover the source meaning, then frame the architecture evaluation over the relevant ACS rows, Q-Bundle slots or structures, with parity when the inference requires it. | The source term alone establishes neither an FPF object kind nor an architecture characteristic. |
| `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Practitioner source for metric categories and governance practice after quality goals are named. | Carry metric-cadence distinctions as eval-program fields, not as criteria rows. | A metric, dashboard, rank, or score is not a project criterion, selected architecture, or architecture decision. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner source for objective definitions, trade-off analysis, and least-worst choices under competing characteristics. | Require declared criteria and the protection needed for material counter-losses before synthesis, comparison or selection relies on eval results. | A better reading or rank does not authorize comparison, selection, choice, G.5 selected-set result declaration, actual publication, or decision by itself. |
| Goodhart and proxy-risk line, plus current FPF `E.13` | Optimized proxies can detach from the declared architecture concern. | Keep proxy repair in E.13 while ACE records the risk before result use. | An eval result cannot replace the declared architecture concern. |
| Current FPF `C.16`, `C.25`, `E.23`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, `E.17`, `E.24.PUB`, and `C.11` | Existing patterns for the next questions for measurement, Q-Bundles, repeated improvement, comparison, selection, selected-set result declaration, publication, and local choice. | Keep ACE as the eval-program framing and typed-result dispatch boundary. | ACE does not validate measurement, define every eval result, define Q-Bundles, compare, select, declare a selected-set result under G.5, publish it to an audience, choose, or decide. |

**Source-currentness boundary.** Use each source row only for the ACE eval-program field, result-use boundary, or refresh condition named in that row. Recheck the row when a named book edition, source presentation, FPF pattern for the next question, metric practice, or evolutionary-architecture practice changes the transferred move. If the project wants criteria-row admission, measurement validity, Q-Bundle structure, explicit comparison, selection, selected-set result declaration, actual publication, local choice, evidence, assurance, or decision use, leave ACE and open the pattern for the next question.

### C.32.ACE:12 - Relations

- **Builds on:** `C.32.HCS`, `C.32.ACS`, `C.16`, `C.16.P`, `C.25`, `A.2.6`, `A.19`, `E.13`, `E.22`, `E.23`, and `A.19.CPM`; coordinates with A.3.1, A.3.2, A.15.2, A.15.1, and A.6.1 only for separately current Method, MethodDescription, planned Work, dated Work, or operation-application claims.
- **Receiving uses:** `C.32.P2S` actual-structure feedback and next-synthesis repair, `C.32` candidate synthesis, `C.32.MLAO` residual optimization, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair, `A.19.CPM` comparison, `A.19.SelectorMechanism` selection, `C.11` local choice, selected-set result declaration under `G.5`, source-backed publication-face and source-return work under `E.17`, publication-occurrence and audience-availability work under `E.24.PUB`, and architecture-decision work for `C.32.PAD`.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, uncertainty, or cross-case comparability claim is made.
- **Structural-information boundary:** For an eval, these contributions are available only after `C.32.ACS`, `C.16`, or `C.25` has declared what is being evaluated: `C.33` and `C.34` for captured structure, lost structure, and preservation adequacy, and `C.35` for recovering the kind of a generated or discovered result and assessing its adequacy for that architecture use. Use C.32.ACE for the eval-program frame, and accept each actual typed result under its own measurement, comparison, evaluation, or assertion definition and test. `C.33`, `C.34`, and `C.35` do not define eval programs.
- **Q-Bundle boundary:** Use `C.25` when the evaluated item is a composite quality family.
- **Test boundary:** Use `test` only as an eval operation for a declared expectation or hard constraint. Error recognition and architecture-synthesis repair use `C.32.FAIL`; non-architecture defects use the local defect-subject pattern.
- **Decision boundary:** An evaluation framed by an ACE record may reference separately admitted readings, ranks, dominance relations, trade-off-front descriptions, and other typed results. Establish the result under its measurement, comparison, evaluation or assertion rule. Add precise evaluation Work or operation-application identity when that claim or the receiving rule requires it. Such a result may serve as source material for an A.10 evidence-provenance account when an evidence claim is current. Use `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, `G.5` for selected-set result declaration, and `C.32.PAD` for a project architecture decision. When audience availability is current, use E.24.PUB for the occurrence, form, carrier, audience, bounded use and availability, and E.17 when a source-backed face and source return are needed.

### C.32.ACE:End
