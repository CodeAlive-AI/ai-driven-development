## C.28 - CausalUse-CAL: Causal-Use Questions, Identification, and Realizability

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Causal-use calculus.

**Intent.** Help a practitioner decide what a causal-looking claim is supported to say, under which limits, and which narrower statement remains when the support is insufficient.

**Primary EntityOfConcern.** One exact causal-use question. The claim, estimand or contrast, evidence paths, identification result, estimate, sampling-realizability result, performed sampling and resulting data, simulation result, support result, and downstream decision remain separately identified.

**Not a physical ontology.** This pattern does not define causation in the world or replace domain science. It supplies a practical interface for using causal evidence and models without promoting association, simulation, or a graph label into a stronger causal claim.

### C.28:0 - Use This When

Use `C.28` when a result is offered as support for a causal effect, intervention, counterfactual comparison, causal fairness claim, causal policy, causal benchmark, or causal explanation. Common cues include:

- “method A improves the outcome”;
- “users who received X did better, so X works”;
- “this policy would have prevented the failure”;
- “the model shows what would have happened”;
- “this fairness metric proves the intervention is fair”; and
- “this benchmark shows that one causal method is better”.

The cue opens a question, not a verdict. Ask what claim is being supported and what use of the evidence depends on that support.

**Not this pattern when.** If no causal statement or causal evidential reliance is current, stay with the direct pattern: `C.16` for measurement, `C.27` for temporal change, `A.10` for an evidence path, `C.11` for choice, `C.19` for live-pool policy, `C.24` for call planning, `D.5` for bias or fairness audit, or `G.9` for ordinary parity.

**Activation condition.** C.28 is needed when causal support changes the statement relied on by a downstream publication, choice, deployment, audit, assurance, policy evaluation, or benchmark. C.28 decides only the causal-support boundary. The downstream pattern still decides whether to publish, choose, deploy, certify, assure, or abstain.

**Simulation boundary at entry.** A report that only describes simulator output and makes no causal use exits to ordinary model or simulation handling. Simulator output offered as support for an effect, counterfactual, policy, fairness, benchmark, or evidence claim stays in C.28 and must name the model, assumptions, validation, supported causal use, and unsupported use.

#### C.28:0.1 - What Goes Wrong If Missed

- association becomes an intervention-effect claim;
- a changed metric becomes causal fairness;
- a simulated trace becomes realized counterfactual evidence;
- an estimated number is treated as proof that its estimand was identified;
- support for one population or environment is transported to another without an endpoint or assumption; or
- a support verdict is mistaken for permission to publish, deploy, or certify.

#### C.28:0.2 - What This Buys

The cheap result states the question, rung, available support components, the common validity threat that matters now, the causal statement supported, the statement not supported, and the next useful step. Heavy profiles appear only when identification, estimation, counterfactual-sampling realizability, actual sampling evidence, transport, target-trial emulation, causal policy evaluation, representation learning, or fairness work is actually current.

#### C.28:0.3 - First-Minute Questions

1. What exact causal-use question is being asked, and which claim-bearing episteme states it?
2. Is the intended statement observational, interventional, or counterfactual?
3. What is actually available: an evidence path and empirical data regime, an identification or bound result, an estimate, a prospective counterfactual-sampling realizability result, dated sampling Work plus resulting data, or a simulation result?
4. Which common validity problem could overturn the use: intervention definition or consistency, time order, confounding, overlap, interference, selection or missingness, measurement, or transport?
5. What causal statement or evidential reliance is supported now, and what stronger statement is not?
6. Does the downstream pattern have enough basis to make its own decision, or should it abstain, downgrade, or request more evidence?

#### C.28:0.4 - First Output

The first output may be only this triage:

```text
CausalUseTriageRecord:
  causalUseQuestionRef?: CausalUseQuestionRef
  causalUse: yes | no | unclear
  targetCausalityLadderRung?: CausalityLadderRung
  comparatorOrCounterfactualRef?
  availableSupportCues?
  liveThreats?
  supportedUse?
  unsupportedUse?
  nextCausalUseAction
```

`supportedUse` means the causal statement or evidential reliance supported under the named limits. It is not a permission or command. `unsupportedUse` states the nearby stronger causal statement or reliance that the evidence does not support.

```text
nextCausalUseAction =
  stopNoCausalUse |
  reportAssociationOnly |
  keepNonCausalSimulationUse |
  downgradeCausalWording |
  requestIdentificationOrBound |
  requestEstimate |
  requestCounterfactualSamplingRealizabilityCheck |
  requestPerformedSamplingEvidence |
  requestTransportCheck |
  requestEvidenceDesign |
  sendFairnessUseToD5BiasAuditReport |
  sendParityUseToG9 |
  abstainDownstream
```

Triage may be the final result when it blocks the overclaim and names the narrower statement. Do not open a durable object merely because a causal word appears.

**Adjacent simulation examples.** “The simulator produced these traces” with no causal reliance returns `keepNonCausalSimulationUse`. “The simulated traces support what would happen under policy P” remains inside C.28 and needs `simulationResultRef`, model assumptions, validation, supported use, and unsupported use.

### C.28:1 - Problem Frame

FPF already has patterns for measurement, temporal claims, evidence, assurance, choice, exploration, call planning, fairness, parity, and mathematical lenses. Each keeps its own result. Causal support cuts across them, so a small shared interface is needed.

The practical question is “what does this evidence support us to say about this causal question, and what would overturn that conclusion?”

### C.28:2 - Problem

Three kinds of collapse can produce causal overclaim:

1. **Rung collapse:** observation, intervention, and counterfactual comparison are treated as the same question.
2. **Support collapse:** data regime, identification, estimation, direct sampling, and simulation are treated as one alternative-valued “basis”.
3. **Authority collapse:** an evidential conclusion is treated as publication, choice, deployment, fairness, or assurance authority.

C.28 keeps those distinctions visible while allowing a cheap stop.

### C.28:3 - Forces

| Force | Tension |
| --- | --- |
| Causal safety vs affordability | Ordinary claims need a quick screen; consequential claims need replayable support. |
| Formal precision vs readable practice | Graphs, estimands, assumptions, and proofs matter, but a cold reader still needs a clear first action. |
| Identification vs estimation vs realizability | The target may be identifiable but not yet estimated, bounded but not point-identified, or directly sampleable only under special constraints. |
| Domain breadth vs one pattern | Potential outcomes, SCMs, target trials, causal ML, transport, causal RL, representation learning, and fairness use different specialist methods. |
| Shared support vs local authority | Neighbours need the result, but keep their own decision and publication rules. |

### C.28:4 - Solution

Use the smallest result that answers the current question:

1. triage the claim;
2. stabilize the question in a small card when it must be reused;
3. run the common threat screen;
4. add only the specialist result needed now; and
5. issue a small `CausalUseSupportResult` when another pattern must consume the conclusion.

#### C.28:4.0 - Public contract and support components

C.28 uses references to actual objects. It introduces no universal kind for a causal-use question, estimand, or potential-outcome contrast.

- `CausalUseQuestionRef` identifies the exact question content, normally a C.2.1 episteme.
- `CausalEstimandRef` identifies the mathematical target or the episteme that describes it under its direct pattern.
- `PotentialOutcomeContrastRef` identifies the exact contrast or its description.
- `CausalUseSupportResultRef` identifies one C.2.1 result episteme defined below.

Support is composable. A real result may use several components:

```text
CausalSupportComponentRefs:
  evidencePathRefs?
  empiricalDataRegimeRefs?
  identificationResultRef?
  estimateResultRef?
  counterfactualSamplingRealizabilityResultRef?
  simulationResultRef?
  targetTrialMappingResultRef?
  offPolicyCausalEvaluationResultRef?
  causalVariableRepresentationRecordRef?
  transportabilityResultRef?
```

These fields answer different questions. Do not compress them into one exclusive value. Each optional specialist ref identifies the exact result or record actually used. Keep a component's own assumptions, uncertainty or sensitivity, supported and unsupported uses, and reopen information with that component when its defining contract requires them; do not copy fields merely to complete a standard list. The common `CausalUseSupportResult` still states its own `supportedUse`, `unsupportedUse`, `limits`, optional evidence window, and `reopenCondition`. Naming a specialist subject in prose does not make its result available to a consumer.

| Component | Question it answers | Does not establish |
| --- | --- | --- |
| evidence path and data regime | What observations, assignments, or samples are available, and where did they come from? | identification or a valid estimate |
| identification result | Can the estimand be expressed or bounded from those data and assumptions? | a numerical estimate or direct sampling |
| estimate result | What value and uncertainty were obtained under an identification or design basis? | identification by the number alone |
| counterfactual-sampling realizability result | Can samples from the declared target distribution be obtained under the stated constraints, and how was that decided? | a WorkPlan, performed sampling, resulting data, or identification of every target |
| simulation result | What did the model produce under its assumptions and validation? | realized evidence or an intervention effect |
| target-trial mapping result | How does the declared trial protocol map to one observational data source, and which gaps, residual-confounding risks, and sensitivity checks remain? | identification, low risk of bias, or a valid estimate by reporting completeness alone |
| off-policy evaluation result | What does logged behaviour support about one evaluation policy under the stated history, confounding, overlap, endpoint, estimator, and uncertainty conditions? | authority to deploy or unqualified policy optimality |
| causal-variable representation record | Which learned, selected, or abstracted variables preserve the interventions, invariances, and queries needed for this use? | causal validity for every query, shift, or domain |
| transportability result | Which support transfers between exact endpoints, under which assumptions? | transfer by a shared label or population name |

`CausalEmpiricalDataRegime` is a local classification used only when it helps distinguish evidence:

```text
CausalEmpiricalDataRegime =
  observationalOrNaturalBehaviorData |
  randomizedInterventionData |
  governedInterventionData |
  realizedCounterfactualSamplingData
```

`realizedCounterfactualSamplingData` is used only when an A.10 evidence path cites dated sampling Work and the resulting sample or data. A realizability result or WorkPlan alone establishes no empirical regime. Model output is recorded separately through `simulationResultRef`, not as an empirical regime.

#### C.28:4.1 - Causality-Ladder Rung

```text
CausalityLadderRung =
  observationalAssociationRung |
  interventionalActionRung |
  counterfactualComparisonRung
```

- observational: passive observation, natural behaviour, or association;
- interventional: action setting, experiment, policy change, or action effect;
- counterfactual: counter-to-fact, potential-outcome, or unit-history-conditioned comparison.

Lower-rung data may contribute to a higher-rung result only through a replayable identification, bound, or other specialist result. The rung label itself supplies no support.

#### C.28:4.1a - Causal-Use Claim Kind

```text
CausalUseClaimKind =
  causalEffectClaim |
  counterfactualComparisonClaim |
  causalFairnessClaim |
  causalPolicyClaim |
  causalBenchmarkParityClaim |
  causalEvidenceSupportClaim |
  causalAssuranceSupportClaim
```

Choose the kind by the claim being supported, not by the tool or source. Simulation for a causal claim uses the appropriate claim kind plus `simulationResultRef`; it does not need a simulation-only claim kind.

#### C.28:4.2 - Question cards and support result

Use a local card when the question must survive beyond the current sentence:

```text
LocalCausalUseQuestionCard:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind?
  comparatorOrCounterfactualRef?
  causalEstimandRef?
  supportedUse
  unsupportedUse
  nextCausalUseAction
```

Use a durable card only for a reusable or consequential claim:

```text
DurableCausalUseQuestionCard:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind
  comparatorOrCounterfactualRef?
  causalEstimandRef: CausalEstimandRef
  potentialOutcomeContrastRef?: PotentialOutcomeContrastRef
  interventionOrAssignmentWindowRef?
  followUpWindowRef?
  outcomeMeasureRef?
  causalAssumptionRefs
  rivalCauseRefs?
  causalSupportComponentRefs
  commonThreatScreenRef?
  supportedUse
  unsupportedUse
  stopOrReopenCondition
```

When another pattern needs a stable conclusion, issue this small C.2.1 result episteme:

```text
CausalUseSupportResult:
  causalUseQuestionRef: CausalUseQuestionRef
  causalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  causalEstimandRef?: CausalEstimandRef
  causalSupportComponentRefs: CausalSupportComponentRefs
  commonThreatScreenRef?
  verdict: supported | bounded | unsupported | undecided
  supportedUse
  unsupportedUse
  limits
  evidenceWindowRef?
  reopenCondition
```

Its identity and reference follow C.2.1. The result states causal support only. A downstream pattern may cite it as one basis and then make its own decision. `undecided` supplies no causal conclusion; the downstream pattern decides whether to abstain, seek evidence, or use a non-causal result.

#### C.28:4.3 - Common causal-validity screen

Run only the questions relevant to the current claim. A live threat either points to an existing specialist field/result or lowers the support result; it does not trigger a mandatory dossier.

```text
CommonCausalThreatScreen:
  causalUseQuestionRef
  interventionWellDefinedOrConsistency?: clear | liveThreat | notApplicable
  temporalOrdering?: clear | liveThreat | notApplicable
  exchangeabilityOrConfounding?: clear | liveThreat | notApplicable
  positivityOrOverlap?: clear | liveThreat | notApplicable
  interferenceOrSpillover?: clear | liveThreat | notApplicable
  selectionCensoringOrMissingness?: clear | liveThreat | notApplicable
  measurementErrorOrConstructShift?: clear | liveThreat | notApplicable
  transportToTarget?: clear | liveThreat | notApplicable
  routedThreatRefs?
  resultingSupportBoundary
```

**Ordinary effect case.** A randomized treatment study records `interventionWellDefinedOrConsistency=clear`, `temporalOrdering=clear`, `positivityOrOverlap=clear`, `interferenceOrSpillover=notApplicable`, `selectionCensoringOrMissingness=clear`, and `measurementErrorOrConstructShift=clear` for its declared target and window. The screen points to the trial and estimate results; it does not repeat them.

**Countercase.** An observational cohort has the right rung label and a plausible estimand, but records `exchangeabilityOrConfounding=liveThreat` and `positivityOrOverlap=liveThreat` because severity is unmeasured and one treatment region has no comparator. The claimed effect remains `unsupported` until a suitable design or new evidence closes those threats; a suitable bound can instead support a correspondingly bounded claim. “Observational data” was classified correctly; that label does not establish validity.

#### C.28:4.4 - Identification result

Identification answers whether the estimand can be expressed or bounded from the available data and assumptions. The conclusion must be replayable:

```text
CausalIdentificationResult:
  causalUseQuestionRef: CausalUseQuestionRef
  causalEstimandRef: CausalEstimandRef
  availableDataRegimeRefs
  causalAssumptionRefs
  modelOrDiagramRefs?
  calculusOrDerivationMethodRef?
  status: identified | bounded | nonidentified | unclear
  identifyingExpressionOrDerivationRef?   # required when identified
  boundResultRef?                         # required when bounded
  obstructionOrFailureWitnessRef?         # required when nonidentified
  falsificationOrNegativeControlRef?
  sensitivityAnalysisRef?
  supportedUse
  unsupportedUse
```

An `identified` label without an identifying expression or derivation is incomplete. A `bounded` result cites the bound. A `nonidentified` result exposes the obstruction or failure witness. Identification is neither a numerical estimate nor direct physical sampling.

**Replayable identified case.** For `treatment_effect_in_population_P`, `AdjustmentSet_Z` is justified as blocking the relevant back-door paths. `backdoor_adjustment_derivation_7` states the identifying expression in ordinary terms: compare treated and untreated outcomes within each Z group, then average those differences using the target population's Z distribution. The result cites the data regime, assumptions, expression, and the confounding or overlap change that would reopen it.

**Replayable nonidentified case.** In a treatment cohort, unmeasured severity affects both treatment and outcome, and no valid adjustment set, instrument, proxy, or useful bound is available. `unmeasured_severity_obstruction_3` is the failure witness. The result is `nonidentified`; reporting an adjusted number does not change that status.

#### C.28:4.5 - Counterfactual sampling realizability

Use this result to answer whether a declared target distribution can be sampled under current constraints. It is prospective: it does not say that sampling was planned, performed, or yielded data.

```text
CounterfactualSamplingRealizabilityResult:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCounterfactualDistributionRef
  targetCausalityLadderRung: counterfactualComparisonRung
  modelOrDiagramRefs?
  sameUnitConflictCheck
  ancestorRegimeConflictCheck
  physicalConstraintRefs
  ethicalConstraintRefs
  operationalConstraintRefs
  unitHistoryAvailabilityRef?
  decisionMethodRef
  decisionDerivationRef?
  positiveSamplingConstructionRef?  # required when realizable
  boundResultRef?                   # required when bounded
  obstructionOrFailureWitnessRef?   # required when nonrealizable
  status: realizable | bounded | nonrealizable | unclear
  supportedUse
  unsupportedUse
```

A `realizable` result cites the sampling construction that the decision Method accepts. A `bounded` result cites its bound. A `nonrealizable` result exposes the obstruction or failure witness. `unclear` names what remains unresolved. “Realized counterfactual sampling” never means observing incompatible outcomes for one unit in one realized world.

If the team plans to draw samples, use a separate A.15.2 WorkPlan. If sampling occurs, recover every precise performer's A.13 core and independently admit the dated Work under A.15.1. Add F.6 only when the sampling claim also needs precise assignment-bound attribution. If the samples are used as evidence, cite the resulting data through an A.10 evidence path. Actual sampling support requires both the dated Work and resulting data or evidence ref; neither `realizable` nor a WorkPlan can stand in for them. Identification from those data, when claimed, is another `CausalIdentificationResult`.

#### C.28:4.6 - Applied profiles

**Target trial.**

```text
TargetTrialProtocolRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  targetPopulationRef
  eligibilityCriteriaRef
  treatmentStrategyRefs
  assignmentProcedureRef?
  timeZeroRef
  followUpWindowRef
  outcomeMeasureRef
  potentialOutcomeContrastRef?: PotentialOutcomeContrastRef
  causalEstimandRef: CausalEstimandRef
  analysisPlanRef
```

An observational emulation keeps the protocol and its mapping to available data as separate results:

```text
TargetTrialMappingResult:
  causalUseQuestionRef: CausalUseQuestionRef
  targetTrialProtocolRef
  observationalDataSourceRef
  eligibilityCriteriaMappingRef
  treatmentStrategyMappingRefs
  assignmentAndTimeZeroMappingRef
  followUpWindowMappingRef
  outcomeMeasureMappingRef
  identifyingAssumptionRefs
  protocolToDataGapAccountRef
  residualConfoundingAssessmentRef
  sensitivityMappingRefs
  supportedUse
  unsupportedUse
  reopenCondition
```

Every mapping field identifies the actual mapping. `protocolToDataGapAccountRef` points to one account that lists the observed gaps or explicitly states that none was found within the declared source and window. The residual-confounding and sensitivity fields remain present even when their bounded result is favourable. Reporting completeness is not a risk-of-bias, identification, or estimate verdict.

**Filled target-trial mapping.** `HypertensionEmulationMap-2025` maps `HypertensionTargetTrial-1` to `ClinicRecords-2022-2024`: age and diagnosis fields implement eligibility; prescription records distinguish the two treatment strategies; the prescription date supplies assignment and time zero; encounter records map the twelve-month follow-up; and the recorded systolic-pressure field maps the outcome. `GapRecord-17` states that adherence after prescription is not observed, `ResidualConfoundingAssessment-17` retains unmeasured severity as a live threat, and `SensitivityMap-17` points to the negative-control and quantitative-bias analyses. The result supports construction and review of this emulation. It does not by itself establish identification, low bias, or a transportable effect; new severity or adherence data reopens it.

**Estimation.**

```text
CausalEstimateResult:
  causalEstimandRef: CausalEstimandRef
  identificationResultRef?: CausalIdentificationResultRef
  designBasedIdentificationResultRef?
  dataRef
  estimatorMethodRef
  diagnosticRefs?
  uncertaintyResultRef
  sensitivityAnalysisRef?
  estimationConsistencyResultRef?  # when consistency is a live support condition
  methodSpecificDetailRefs?        # only for the selected estimator family
  supportedUse
  unsupportedUse
```

At least one identification or explicit design-based basis is required before the estimate supports a causal use. Orthogonal scores, nuisance models, and cross-fitting belong in `methodSpecificDetailRefs` only when a DML Method is selected. `estimationConsistencyResultRef` points to the consistency result defined by the selected estimation Method or its direct evaluation pattern; C.28 introduces no universal consistency-result kind.

**Counterfactual fairness.** Before D.5 uses a counterfactual-fairness support result, its C.28 components cite the identification result and the extra assumptions needed to connect the available data to that counterfactual question. When the fairness conclusion depends on an estimate, they also cite the estimate and its `estimationConsistencyResultRef`. Without those conditions, return `bounded` or `unsupported`; more data, even an unlimited amount of the same data, does not repair missing counterfactual identification or an inconsistent estimator. Associative or interventional fairness claims use their own rung and do not inherit this stronger branch by label.

**Non-DML estimate.** A randomized trial cites `random_assignment_identification_4`, `trial_data_8`, `DifferenceInMeansMethod_2`, `standard_error_result_5`, and its attrition sensitivity check. It needs no orthogonal-score, nuisance-model, or cross-fitting fields. The estimate supports only the declared population, outcome, assignment, and follow-up window.

**Transport.**

```text
CausalTransportabilityResult:
  causalUseQuestionRef: CausalUseQuestionRef
  sourcePopulationRef?
  targetPopulationRef?
  sourceDomainRef?
  targetDomainRef?
  sourceEnvironmentRef?
  targetEnvironmentRef?
  sourceDataGeneratingRegimeRef?
  targetDataGeneratingRegimeRef?
  selectionAssumptionRefs?
  domainShiftAssumptionRefs?
  sourceWindowRef?
  targetWindowRef?
  overlapEvidenceRef?
  transportComparatorOrFormulaRef
  semanticBridgeRef?          # only when interpretation differs
  supportedUse
  unsupportedUse
  unresolvedAssumptionRefs?
```

Identify every endpoint dimension that differs in the current claim. Population, domain, environment, data-generating regime, and semantic scheme answer different questions. A shared label proves nothing; a semantic Bridge is added only when its F.9 relation independently obtains.

**Off-policy evaluation.**

```text
OffPolicyCausalEvaluationResult:
  causalUseQuestionRef: CausalUseQuestionRef
  evaluationPolicyRef
  behaviorPolicyRef
  sequentialHorizonRef?
  unitHistoryConditioningRef?
  confoundingAssumptionRefs?
  overlapOrSupportCheckRef
  policyTransportabilityResultRef?
  estimatorRef?
  uncertaintyResultRef?
  supportedUse
  unsupportedUse
  reopenCondition
```

**Causal representation.** Use this record only when variables are learned, selected, or abstracted rather than supplied by the domain:

```text
CausalVariableRepresentationRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  sourceRepresentationRef
  selectionOrAbstractionMethodRef
  representationAssumptionRefs
  interventionValidityResultRef
  invarianceResultRefs?
  abstractionFidelityResultRef?
  counterfactualQueryPreservationResultRef?
  uncertaintyResultRef?
  shiftLimitRefs?
  supportedUse
  unsupportedUse
  reopenCondition
```

The record states which interventions and queries the learned or abstracted variables preserve, not that they are causal variables for every query or domain.

**Filled representation case.** `WardStateRepresentation-4` derives three state variables from monitor traces through `WardStateAbstractionMethod-2`. Its intervention-validity result covers dosage interventions, its invariance result covers the two hospitals in the training and hold-out comparison, and its query-preservation result passes the declared one-step counterfactual query but fails the long-horizon query. The record therefore supports the one-step policy comparison only; a new hospital, sensor scheme, intervention family, or long-horizon claim reopens it.

#### C.28:4.7 - Graph and calculus names

Use specialist names only when the result depends on them:

```text
CausalGraphRepresentationKind =
  causalDirectedAcyclicGraphRepresentation |
  acyclicDirectedMixedGraphRepresentation |
  singleWorldInterventionGraphRepresentation |
  structuralCausalModelTwinNetworkRepresentation |
  ancestralMultiWorldNetworkRepresentation |
  counterfactualGraphicalModelRepresentation

GraphSeparationCriterionKind =
  dSeparationCriterion |
  mSeparationCriterion |
  singleWorldInterventionGraphSeparationCriterion |
  ancestralMultiWorldNetworkSeparationCriterion |
  counterfactualGraphSeparationCriterion

CausalInferenceCalculusKind =
  doCalculus |
  ctfCalculus |
  potentialOutcomeCalculus |
  gFormulaCalculus
```

These values classify the formal support form. Concrete refs point to the model, diagram, derivation, assumptions, or proof. A graph-class label is not a proof and does not replace the plain statement of what was identified or bounded.

#### C.28:4.8 - Causal evidence design and Work

Use `CausalUseEvidenceDesignRecord` when additional evidence could change the support boundary:

```text
CausalUseEvidenceDesignRecord:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung
  causalEstimandRef?
  interventionOrProtocolRef?
  plannedDataRegimeRefs?
  identificationQuestionRef?
  estimationQuestionRef?
  samplingRealizabilityQuestionRef?
  transportQuestionRef?
  targetTrialMappingResultRef?
  offPolicyCausalEvaluationResultRef?
  causalVariableRepresentationRecordRef?
  causalEvidenceMethodDescriptionRefs?
  causalEvidenceWorkPlanRef?
  realizedCausalEvidenceWorkRefs?
  workAttributionResultRefs?
  evidencePathRefs?
  modelAssumptionRefs?
  simulationValidationRef?
  decisionThresholdAffected?: yes | no | unclear
  evidenceValueOrProbeWorthinessRef?
  costOrRiskRef?
  supportedUseIfSuccessful
  unsupportedUseWithoutFurtherEvidence
```

The three optional specialist refs are included only when an existing target-trial mapping, off-policy evaluation, or causal-variable representation result shows what additional evidence could change the support boundary. Before execution, cite a MethodDescription or WorkPlan only when used. After execution, cite every precise performer's A.13 core and the independent A.15.1 Work admission; cite F.6 only when precise assignment-bound attribution is also current. If performed counterfactual sampling is used as evidence, also cite the resulting sample or data through `evidencePathRefs`; Work without output data and data without its Work and provenance path each remain incomplete for that claim. Do not copy performer-kind, assignment, or occurrence mechanics into this record unless one of those facts changes causal validity, safety, authorization, or supported use.

Additional evidence is worth planning only when it can change a material causal statement or downstream decision enough to justify cost, risk, and delay, or when safety or release rules independently require it.

#### C.28:4.9 - Support is not authority

`CausalUseSupportResult.verdict` has four values:

- `supported`: the named causal statement or evidential reliance is supported under the stated limits;
- `bounded`: only the narrower statement or reliance is supported;
- `unsupported`: the claimed causal statement or reliance is not supported;
- `undecided`: the available work does not establish a causal conclusion.

The result never authorizes publication, choice, deployment, certification, fairness approval, or assurance. The downstream pattern cites it as one basis, considers its own other conditions, and makes its own decision. Practical guidance such as “report association only” states the remaining evidence boundary; it is not a permission issued by C.28.

#### C.28:4.10 - Causal action policy class

Use this classification only when policy use changes the causal question:

```text
CausalActionPolicyClass =
  naturalBehaviorPolicy |
  interventionalPolicy |
  counterfactualPolicy |
  mixedPolicy
```

`unknown` is an unresolved classification, not a fifth member. Omit the field when the distinction changes no support, comparison, or downstream decision.

#### C.28:4.10a - Naming and ontology settlement

The public `...Ref` names above are local reference contracts, not newly admitted universal kinds. Recover the actual object before choosing a reference:

| Wording cue | Recover |
| --- | --- |
| “causal question” | the exact question content and its C.2.1 episteme |
| “estimand” | the mathematical target or the episteme that describes it |
| “causal evidence” | evidence paths, empirical data regimes, and the separate identification, estimate, sampling-realizability, performed-sampling, resulting-data, simulation, and transport results actually used |
| “policy optimality” | policy class, off-policy result, support result, limits, and the downstream choice decision |
| “fairness evidence” | causal question and support result here; `BiasAuditReport@Context` and audit decision in D.5 |
| “what would have happened” | a sampling-realizability result, performed sampling with resulting data, an identified or bounded estimate, simulation, or an unsupported claim—named separately |

Do not create a universal object merely to preserve a familiar token. Do not replace plain practitioner sentences with a list of ontology fields when the shorter sentence carries the same distinction and stop condition.

#### C.28:4.11 - Neighbor selection

| Current issue | Use | C.28 contribution |
| --- | --- | --- |
| measurement or metric | `C.16` | causal support only when the measure is used causally |
| temporal trend or rate | `C.27` | causal support only when time order is used as cause evidence |
| evidence path and provenance | `A.10` | support-result and component refs |
| assurance | `B.3` | one possible basis for a separate bounded assurance result |
| local choice | `C.11` | question, support result, and policy class when needed |
| live-pool policy | `C.19` | causal data or policy support when needed |
| call plan | `C.24` | causal action-use field when planned calls serve a causal claim |
| bias or fairness audit | `D.5` | causal question, rung, estimand, support result, and the additional counterfactual-identification and estimation-consistency conditions when that branch is current |
| method dispatch | `G.5` | causal method-use classification and support refs |
| benchmark parity | `G.9` | rung, estimand, support-component, transport, and support-result parity |

#### C.28:4.12 - Non-Goals

C.28 does not define physical causation, choose one causal school for every domain, certify a graph by naming it, replace domain intervention or outcome definitions, replace measurement/evidence/fairness/choice/assurance/parity patterns, or authorize a downstream action. It also does not require a durable card or specialist profile when triage already blocks the overclaim.

#### C.28:4.13 - Cheap downgrade library

| Case | Plain bounded result |
| --- | --- |
| association only | “The evidence supports an association report; it does not support an intervention-effect claim.” |
| temporal change only | “The change in time is recorded; a causal-effect claim remains unsupported.” |
| non-causal simulation | “The simulator produced these traces; no causal use is claimed.” |
| simulation used causally | “The validated model supports this bounded model-based comparison; it does not supply realized or interventional evidence.” |
| metric-only fairness | “The metric disparity is reported; causal fairness is not established.” |
| logged policy | “The evaluation supports only the named behaviour/evaluation-policy regime and overlap limits; unqualified optimality is unsupported.” |
| cross-rung benchmark | “The methods answer different causal questions; publish the bridge and its loss, report degraded parity, or abstain instead of naming one causal winner.” |

#### C.28:4.14 - Payoff check

Keep a causal-use record only when it changes the supported causal statement, blocks a concrete overclaim, changes evidence work, or supplies a real basis to a downstream decision. Remove fields that do none of those things. Prefer triage when it preserves the same boundary.

#### C.28:4.15 - Publication-unit boundary

When only wording inside one publication unit is unclear, use the publication and wording patterns. Open C.28 only when the wording is relied on causally. A publication decision remains with the publication pattern even after C.28 returns a support result.

#### C.28:4.16 - Causal-laundering cases

| Case | Result |
| --- | --- |
| “Users who received X improved, so X works.” | Observational rung; association supported; intervention effect unsupported unless identification/design results close the gap. |
| “We changed X once, so the policy works everywhere.” | Interventional result limited to its population/environment/window; transport requires exact endpoints and assumptions. |
| “The simulator shows what would have happened.” | With no causal reliance, exit to model reporting. With causal reliance, cite the simulation result, assumptions, validation, supported model use, and unsupported realized/interventional use. |
| “The trial was randomized, therefore the estimate is valid.” | Run the common threats: interference, attrition, measurement, adherence, and analysis can still lower the result. |
| “The observational estimand is identified.” | Cite the identifying expression/derivation for `identified`; a bound supports `bounded` wording, and a nonidentification witness supports `nonidentified` wording. The label alone is incomplete. |
| “The fairness metric improved, therefore the intervention is fair.” | Report metric change. A counterfactual-fairness claim additionally needs its causal estimand, counterfactual-identifiability assumptions, estimate-consistency basis when used, and bounded C.28 support before D.5 audits it. |
| “Logged replay says this policy is optimal.” | Cite behaviour/evaluation policies, overlap, confounding, transport, uncertainty, and bounded support; unqualified optimality is unsupported. |
| “Method A beats Method B causally.” | Use G.9; different rungs, estimands, support components, endpoints, or windows require a bridge with stated loss, degraded parity, or abstention. |

### C.28:5 - Archetypal Grounding

**System.** A product team observes better outcomes among recipients of X. Triage returns association support. If the team needs an effect claim, it opens identification or evidence-design work; the deployment decision still needs its own downstream basis.

**Fairness.** A report claims counterfactual fairness after a policy change. C.28 identifies the rung and estimand, exposes the additional counterfactual-identifiability assumptions, and cites an estimate with its consistency result when the audit relies on that estimate. Missing identification or consistency lowers the support result even with more of the same data. D.5 carries the `BiasAuditReport@Context` and makes the audit conclusion.

**Policy.** Logged behaviour data are used to evaluate a new policy. The result names both policies, horizon, confounding and overlap checks, transport endpoints when changed, estimate and uncertainty, supported regime, and unsupported unqualified optimality. C.11 or another policy pattern makes the choice.

**Causal RL.** An online learner combines logged behaviour, interventions, and a counterfactual-data source. The sampling-realizability result explains whether that source can be produced; dated Work and the resulting data path show whether it was produced; a separate identification or estimate result says what follows from it. Replay reward does not become an optimal-action claim.

**Evidence Work.** A lab's `CounterfactualSamplingRealizabilityResult` cites its decision Method and positive construction. That result supports planning but claims no sample. The later WorkPlan remains prospective. After sampling, the lab cites independently admitted dated Work and the resulting data in an A.10 evidence path before using `realizedCounterfactualSamplingData`; it adds precise assignment-bound attribution only when the receiving support claim uses it. Identification from those data remains a separate result.

**Simulation.** A simulator supports rehearsal and sensitivity analysis under named assumptions and validation. The support result blocks realized-sample and intervention-effect wording. A pure simulator-output report exits C.28 earlier.

**Transport.** The population is unchanged but the care environment and measurement mechanism differ. The transport result names source and target environments and data-generating regimes, then states the assumptions and formula. A population ref alone would miss the shift.

**Benchmark.** G.9 compares an observational predictor, intervention optimizer, and counterfactual policy only after it checks rung, estimand, support components, window, and endpoints. The admissible result may be a selected set or abstention rather than a scalar winner.

### C.28:6 - Bias-Annotation

Watch for causal prestige, simulation laundering, metric proxy substitution, graph sufficiency, feasibility-as-performance, data-without-Work, support-label substitution, and benchmark scalarization. Recover the question, support components, live threats, supported statement, unsupported statement, and reopen condition in the shortest form that remains replayable.

### C.28:7 - Conformance Checklist

1. One exact causal-use question remains identifiable from entry to result; question, claim, estimand, evidence, and records are not treated as one object.
2. C.28 introduces no universal causal-use-question, estimand, or potential-outcome-contrast kind; it uses local refs to actual objects instead.
3. Data regime, identification, estimate, sampling realizability, performed sampling evidence, simulation, and transport remain distinct and may be combined.
4. A support result states evidence support only; every publication, choice, deployment, fairness, or assurance decision remains with its direct pattern.
5. An identified result cites an expression or derivation; a bounded result cites a bound; a nonidentified result cites an obstruction or witness.
6. A causal estimate cites an identification or explicit design-based result. Method-family details appear only when that Method is selected.
7. The common threat screen routes every live ordinary threat or lowers the result; it is not a mandatory dossier.
8. Non-causal simulator reporting and simulation-supported causal use take different routes at first entry.
9. A sampling-realizability result cites its decision Method, any derivation used, and the construction, bound, or obstruction required by its status; it claims no Work or data.
10. Performed counterfactual-sampling support cites independently admitted dated Work and resulting data or evidence; it cites exact assignment-bound attribution only when the receiving support claim uses it. A WorkPlan or `realizable` label cannot satisfy this branch.
11. Evidence design cites each precise performer's A.13 core and the independent A.15.1 Work result; it cites F.6 only when exact assignment-bound attribution is current, rather than copying assignment mechanics.
12. Transport identifies every changed population/domain/environment/data-generating-regime endpoint separately from semantic schemes.
13. A counterfactual-fairness escalation exposes its additional identification assumptions and, when an estimate is used, estimation consistency before D.5 consumes it.
14. `CausalActionPolicyClass` has the same four members in definition, examples, and consumers; unresolved classification is not a member.
15. Every specialist field changes support, a downstream decision basis, evidence work, or a reopen condition.
16. A target-trial mapping result identifies the observational source and every protocol-to-data mapping, gap, residual-confounding assessment, and sensitivity mapping needed for its bounded use.
17. Every retained specialist result that can independently change support can enter `CausalSupportComponentRefs`; when it shapes further evidence, the evidence-design record can cite the same result without copying it.
18. The whole pattern remains understandable to a practitioner without requiring the formal graph vocabulary on the ordinary path.

### C.28:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Fill-all-cards default | Start with triage and add only the live profile. |
| Rung label as validity proof | Run the common threat screen and cite the actual results. |
| One support-basis enum | Keep data, identification, estimate, sampling, simulation, and transport separate. |
| Estimate creates identification | Require an identification or design-based result first. |
| Graph-only causality | Cite the model or diagram, assumptions, and replayable derivation or bound. |
| Feasibility as performed evidence | Keep the sampling-realizability result separate from a WorkPlan, dated Work, and resulting data. |
| Work or plan as data | Require the A.10 path to the resulting sample or data before claiming the empirical regime. |
| Simulation as realized evidence | Use `simulationResultRef` and state unsupported realized/interventional use. |
| Shared context label proves transport | Name exact causal endpoints, assumptions, and formula. |
| Support verdict authorizes action | Return the support result to the downstream decision pattern. |
| Specialist branch named but not consumable | Put its exact result ref in the common component contract and keep its assumptions, limits, uncertainty, and reopen condition with that result. |
| Ontology dossier as precision | Keep specialist refs behind the ordinary question, threat, and support statement. |

### C.28:9 - Consequences

The pattern makes unsupported causal claims easier to lower while keeping ordinary triage cheap. Consequential claims become replayable across question, support components, threats, limits, and source window. The cost is additional specialist work only where a stronger causal statement or downstream decision genuinely depends on it.

### C.28:10 - Rationale

Temporal change, a higher metric, a convincing graph, or a plausible simulator can all be useful without supporting a causal effect. Conversely, observational data can support a causal estimate when an explicit identification result closes the inferential gap. C.28 therefore separates the question from the components that support it and separates that evidential conclusion from downstream authority.

The integrated contract is deliberately plural: SCM and graphical methods, potential outcomes, target-trial practice, design-based identification, causal ML, transport, causal representation learning, causal RL, and causal fairness may supply different specialist results. None is installed as the universal method.

### C.28:11 - SoTA and lineage

**Qualification window.** This comparison was reviewed through 2026-08-21. Reopen it when a current contribution is materially superseded, TARGET guidance changes, a specialist branch changes the minimum replay fields, or direct consumers need a different support-result contract.

| Status and live problem | Contribution used | Adopted, adapted, or rejected FPF move |
| --- | --- | --- |
| Lineage: seeing, doing, imagining, and identification | Pearl hierarchy and identification tradition, [On Pearl's Hierarchy and the Foundations of Causal Inference](https://causalai.net/r60.pdf) | Retain the three-rung distinction and no unsupported climb. This is history and foundation, not proof that one graphical school covers every domain. |
| Current counterfactual theory | Correa and Bareinboim, 2025, [Counterfactual Graphical Models](https://proceedings.mlr.press/v267/correa25a.html) | Name graph form and calculus when the derivation depends on them. Do not make the formalism part of ordinary triage or treat a graph label as a result. |
| Current reporting practice | TARGET Statement, BMJ 2025, [Reporting of observational studies explicitly emulating a target trial](https://www.bmj.com/content/390/bmj-2025-087179) | Retain causal question and estimand, assumptions, protocol-to-data mapping, estimate and precision, and sensitivity reporting. Reject the overread that complete reporting is identification or low risk of bias. |
| Current bounded transport research | NeurIPS 2025, [Causal Effect Estimation under Covariate Shift](https://proceedings.neurips.cc/paper_files/paper/2025/hash/795679e4056817ee71d37680939e980f-Abstract-Conference.html) | Keep identification and estimation under a named shift explicit. This does not replace the broader endpoint and assumption requirements for other transport problems. |
| Current sampling-realizability decision | Raghavan and Bareinboim, ICLR 2025, [Counterfactual Realizability](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e59c4efcaed615db8911fecb84c1d51b-Abstract-Conference.html) | **Adopt:** make realizability a replayable prospective result with its decision Method and construction, bound, or obstruction. Keep realizability separate from a WorkPlan, dated Work, or data. |
| Current Layer-3 identification and bounds | Raghavan and Bareinboim, 2026, [Causal Identification from Counterfactual Data: Completeness and Bounding Results](https://arxiv.org/abs/2602.23541) | **Adopt as composition, not collapse:** realized counterfactual data may feed a separate identification or bound result. Producing those data still needs dated Work and an evidence path to the result; realizability alone supplies neither data nor identification. |
| Lineage and current domain practice: potential outcomes | Rubin 1974 and later target-trial practice | Retain estimand, contrast, assignment/time zero, follow-up, outcome, and analysis plan. Use `PotentialOutcomeContrastRef`, not an unadmitted U-kind. |
| Conditional estimator family | Chernozhukov et al. 2018, [Double/debiased machine learning](https://academic.oup.com/ectj/article/21/1/C1/5056401) | Use orthogonal scores and cross-fitting only for a selected DML Method. Reject their use as universal estimation fields. |
| Current counterfactual-fairness limit | Ma et al., CLeaR 2026, [Consistent End-to-End Estimation for Counterfactual Fairness](https://proceedings.mlr.press/v323/ma26a.html) | **Adopt:** a supported counterfactual-fairness use exposes additional counterfactual-identifiability assumptions and estimation consistency. Infinite data does not repair either omission; D.5 receives a bounded or unsupported result when they are absent. |
| Lineage: causal representation | Schölkopf et al., [Toward Causal Representation Learning](https://is.mpg.de/en/publications/scholkopfetal21) | Retain intervention validity, invariance, abstraction fidelity, query preservation, and shift checks when learned causal variables are used. This broad source is lineage, not a claim that one representation is current-best for every domain. |
| Lineage: sequential causal policy | Maiti and Bareinboim, [Sequential Causal Games](https://causalai.net/r145.pdf), plus causal bandit and data-fusion work | Retain natural, interventional, counterfactual, and mixed policy distinctions and keep history, overlap, and transport visible. Do not infer policy optimality from replay reward. |
| 2026 domain-specific representation and policy alternatives | Mandyam et al., [CANDOR](https://proceedings.mlr.press/v333/mandyam26a.html), and Balashankar et al., [Domain Faithfulness through Counterfactually Robust Learning](https://proceedings.mlr.press/v323/balashankar26a.html) | **Reject as shared-interface additions:** imperfect counterfactual annotations, healthcare policy evaluation, subgroup rules, and representation/training choices materially affect their domain Methods, diagnostics, and supported use, but add no missing universal C.28 field. Keep them in method-specific detail and reopen only if a cross-domain result exposes a new minimum support distinction. |
| Lineage: fairness and accuracy | Plecko and Bareinboim, [Fairness-Accuracy Trade-Offs: A Causal Perspective](https://causalai.net/r107.pdf) | Retain the causal estimand and trade-off question, but do not use this lineage alone as current counterfactual-fairness support. The 2026 identification and consistency conditions above now bound D.5 consumption. |

**Why this combination is retained.** The 2025 realizability result answers whether samples can be produced; the 2026 completeness and bounding result answers what can be identified from realized Layer-3 data; the 2026 fairness result states extra conditions for one consequential downstream use. Keeping those results separate preserves their different questions while allowing explicit composition. The domain-specific 2026 lines improve selected Methods but do not dominate the small shared interface. This is the current non-dominated contract for a practitioner who needs a cheap causal stop plus replayable specialist results.

**Synthesis boundary.** No source above establishes the whole C.28 architecture. The orthogonal support components, common threat screen, small support-result interface, support/authority split, and cross-pattern consumer contract are a bounded FPF synthesis. Validate them through filled cases and consumer replay; reopen when they hide a real causal distinction, impose unused apparatus, or fail a practitioner.

### C.28:12 - Relations

- `C.16` keeps measurements and scales; `C.27` keeps temporal-claim adequacy.
- `A.10` keeps evidence paths and provenance and may cite C.28 support components and result.
- `A.2.4` classifies how an episteme is used; it cannot promote simulation output or association into stronger causal evidence.
- `A.15` keeps Method, plan, Work, and attribution for interventions, target trials, and sampling.
- `B.3` may cite a C.28 result as one basis for a separate bounded assurance result.
- `C.11`, `C.19`, and `C.24` keep choice, pool treatment, and call planning and consume only the needed causal refs.
- `D.5` keeps bias/fairness audit and uses `BiasAuditReport@Context` when a causal fairness question is consequential or reusable.
- `G.5` keeps method dispatch; `G.9` keeps parity and benchmark conclusions; `G.11` keeps refresh planning.
- `C.26` is used only for a residual quantum-like modelling issue after ordinary causal explanations are tried.

#### C.28:12.1 - C.29 mathematical-lens relation

`C.29` may describe a mapping as abstraction-like, quotient-like, coarse-graining-like, simulation-like, or macro-model-like. It does not decide causal support. When intervention, policy, counterfactual, causal explanation, or causal decision use is current, apply C.28; otherwise record no causal-use claim or the exact blocker.

### C.28:End

