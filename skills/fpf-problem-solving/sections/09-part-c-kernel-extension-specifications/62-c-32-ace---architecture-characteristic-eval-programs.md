## C.32.ACE - Architecture Characteristic Eval Programs

> **Type:** Architecture eval-support subpattern under C.32
> **Status:** Draft
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

**First-minute use slice.** A product-family team has ACS rows for substitutability, evidence reuse, and latency, plus safety as a monitored guardrail. Two candidate architectures look plausible. Using C.32.ACE, the practitioner defines one eval program with the same parity frame, evaluates both candidates against the declared rows, records latency readings, evidence-scope findings, and protected safety loss, and records the result as input for `A.19.CPM` comparison or the next C.32 synthesis pass. The eval result informs the architecture work; it cannot define the criterion or decide the architecture.

The primary `EntityOfConcern` is one architecture-characteristic eval program over declared criteria rows, Q-Bundle slots, candidates, bearers, or selected structures under a parity frame. Measurement validity, comparison policy, selection results, G.5 publications, and architecture decisions remain with their receiving patterns.

Ordinary working move: choose the declared criteria rows to read, hold one parity frame for the variants being evaluated, run the eval operation, and return readings or front information as feedback for comparison or the next synthesis pass.

The first useful output is an `ArchitectureCharacteristicEvalProgram@Project`. The eval program is the project working record for evaluation over declared criteria. It reads characteristics through rows, slots, candidates, or structures; it is not the characteristic itself, the scale row, the measurement-validity claim, the comparison policy, or the decision:

For a first pass, fill only the evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame, eval purpose, eval operation, result form, receiving use, and refresh or retire condition. Add trigger modes, method references, uncertainty policy, and comparison policy only when the current receiving use needs them.

```text
ArchitectureCharacteristicEvalProgram@Project:
  evaluatedCriteriaSetRef:
  evaluatedCriteriaRowRefs:
  evaluatedQBundleSlotRefs?:
  evaluatedCandidateRefs?:
  evaluatedBearerOrSelectedStructureRefs:
  evalPurpose: characterizeCurrentArchitecture | compareCandidates | monitorEvolution | prepareSelection | triggerNextSynthesis
  evalQuestion:
  parityFrameRef:
  evalScope: singleCriterion | coupledCriteria | qBundleSlice | variantPortfolio | holisticUseSlice
  evalOperation: measurement | simulation | benchmark | scenarioWalkthrough | test | monitor | expertReview | evidenceAudit
  triggerMode: onePass | batchComparison | continual | onChange | manualOnDemand
  resultForm: reading | band | rank | dominanceRelation | tradeoffFront | qualitativeState | evidenceFinding
  runContext: designTime | laboratory | pipeline | production | workReview | decisionPrep
  measurementOrObservationMethodRefs:
  resultRef?:
  uncertaintyAndMissingDataPolicy:
  proxyRisk:
  protectedCounterCharacteristicRefs:
  comparisonPolicyRef?:
  receivingUseRef:
  refreshOrRetireCondition:
```

What goes wrong if C.32.ACE is missed: a project has architecture-characteristic rows but treats a test, monitor, dashboard, or source-side "fitness function" as the criterion or as the decision. The team may then reject useful losing variants as errors, optimize one indicator, or choose a candidate without fair comparison.

What C.32.ACE buys in practice: eval work is framed as typed evaluation over declared architecture criteria. A losing candidate can still add knowledge about the solution space, while an actual error remains a failure against an expectation that causes unplanned rework.

Adoption test: after using C.32.ACE, the record shows which variants were read under the same parity frame, what result form was produced, and which receiving pattern may use that reading as feedback.

Not this pattern when the characteristic rows do not exist yet. Also not this pattern when the current work is measurement validity, composite-quality modeling, explicit comparison, set-returning selection, local choice, publication of a selected set, evidence, assurance, or project architecture decision.

Common exits by claim kind:

- `C.32.HCS` and `C.32.ACS` before characteristic rows exist.
- `C.16` for measurement validity, readings, units, uncertainty, or comparability claims.
- `C.25` for Q-Bundles and composite quality families.
- `E.13` when an eval result or dashboard starts replacing the declared architecture concern.
- `C.32` for candidate synthesis, `C.32.MLAO` for residual input, and `E.23` for repeated improvement feedback.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for publication of a selected set.
- `A.10` and `B.3` when evidence or assurance claims are being made.
- `C.32.PAD` for project decision.

### C.32.ACE:2 - Problem

Architecture synthesis is an optimization and learning activity under competing characteristics. It needs evals: deliberate measurement, simulation, benchmark, scenario, review, or monitoring runs that say how a current architecture or candidate architecture reads against declared criteria.

Testing for errors is a neighboring use. A test asks whether an expectation is violated. An eval asks how variants compare, how a candidate changes the trade-off front, which constraint is hit, or whether the next synthesis pass should open. A candidate that loses the eval is not automatically an error; it may be a deliberate probe that improves the architecture team's knowledge of the solution space.

Evolutionary-architecture sources often say "fitness function". In FPF that is source-side wording. The recoverable FPF object is an eval program over declared architecture-characteristic rows, Q-Bundle slots, candidate structures, and a parity frame. Some eval programs can be automated tests or monitors, but automation does not change the kind.

### C.32.ACE:3 - Forces

| Force | Tension |
|---|---|
| Variant learning | Candidate architectures may be valuable even when they lose the selection being made. |
| Fair comparison | Eval results are useful only when context, budgets, windows, units, and missing-data treatment are explicit. |
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
4. Establish the parity frame: context, resource budget, time window, units, admissible observation or evidence inputs, and policy for missing or unknown readings.
5. Choose eval scope: one criterion, coupled criteria, one Q-Bundle slice, a candidate portfolio, or a holistic use slice.
6. Choose eval operations. Use measurement, simulation, benchmark, scenario walkthrough, monitor, review, or evidence audit according to the claim. Use `test` only when the eval operation is actually checking an expectation or hard constraint.
7. Declare the result form: reading, band, rank, dominance relation, trade-off front, qualitative state, or evidence finding.
8. Name proxy risk and protected counter-characteristics before the eval result can drive work. Optimize only the cycle's chosen indicators; keep the remaining protected characteristics visible as guardrails or risk signals.
9. State the receiving use: `C.32` synthesis input, `C.32.MLAO` residual input, `E.23` improvement feedback, `A.19.CPM` comparison input, `A.19.SelectorMechanism` selection input, `C.11` choice input, input for publishing a selected set under `G.5`, or architecture-decision input for `C.32.PAD`.
10. Refresh or retire the eval program when the evaluated row, C.32 candidate palette, bearer, selected structure, environment, parity frame, or source-currentness relation changes.

**Stop condition.** Stop C.32.ACE when the eval program names evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame, eval purpose, eval operation, result form, receiving use, proxy risk, protected counter-characteristics, and refresh or retire condition.

**Lowering condition.** Keep the result as an eval result only while the evaluated rows, evaluated candidates or structures, parity frame, eval operation, result form, and receiving use still match the work being done. Lower the result to report-only when missing data, proxy risk, or parity-frame mismatch prevents synthesis, comparison, selection, publication of a selected set, choice, evidence, assurance, or decision use. Retire the eval program when its evaluated row, bearer, selected structure, environment, source-currentness relation, or receiving use no longer belongs to the current architecture work. Return to `C.32.ACS` when the criteria row is missing or wrong, to `C.16` when measurement validity is current, to `C.25` when the evaluated item is composite, and to the named receiving pattern when a stronger downstream claim is current.

### C.32.ACE:5 - Worked slices

**Latency candidate.** A service candidate promises latency under 100 ms and an eval reads 240 ms. If the 100 ms band is a hard constraint, the candidate is inadmissible for this cycle. If the project is still exploring a trade-off front, the candidate is a losing variant with useful evidence about resource placement, interface burden, or control separation. Treat it as an error only when the project used that expectation to plan work and unplanned rework follows.

**BIM digital twin.** A built-asset team compares architecture candidates that combine placement, schedule, use-phase, maintenance, and cost structures. ACE does not treat the number of dimensions as the evaluation. The practitioner defines a parity frame and evals the ACS rows declared for the project, such as access, source-return cost, observability, and maintenance reach, then records results with the parity-frame and result-form fields needed by `A.19.CPM`.

**Method-family architecture.** A review-method family has ACS rows for evidence reuse, change reach, and role substitutability, plus a C.25 teachability bundle. ACE defines a batch eval over three method variants. One variant loses on teachability but reveals a reusable evidence relation; C.32 may use it as a stepping stone.

**AI-agent workflow.** A model-supported workflow has candidates with different function graphs and tool boundaries. ACE evaluates latency, evidence refresh, policy controllability, and rollback under the same task set and evidence window. A benchmark score is not the architecture decision; it supplies one eval reading inside the parity frame.

**Role-team escalation.** A hospital escalation team has ACS rows for decision latency, accountability clarity, evidence custody, and role continuity. ACE evaluates two role-boundary variants under the same incident scenarios and handoff evidence window. The result can feed comparison or the next synthesis pass; staffing choice remains with the receiving decision pattern.

### C.32.ACE:6 - Kind and Receiving-Claim Boundary

C.32.ACE governs architecture-characteristic eval-program construction and the kind boundary between criterion, eval operation, eval result, comparison input, selection input, and decision input. It does not govern starter characteristic selection, ACS scale-row construction, measurement validity, Q-Bundle normal form, candidate synthesis, comparison-policy design, final selection, local choice, publishing a selected set under `G.5`, or architecture decisions. Use `C.32.HCS`, `C.32.ACS`, `C.16`, `C.25`, `C.32`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, or `C.32.PAD` when those claims are being made.

### C.32.ACE:7 - Conformance requirements

| Requirement | Required result |
|---|---|
| `CC-ACE-1` | Every eval references declared ACS rows or C.25 Q-Bundle slots. |
| `CC-ACE-2` | Every eval names evaluated candidates, bearers, or selected structures. |
| `CC-ACE-3` | Purpose, parity frame, scope, eval operation, trigger mode, result form, and run context are explicit. |
| `CC-ACE-4` | Measurement claims exit to `C.16`; composite quality claims exit to `C.25`. |
| `CC-ACE-5` | Proxy risk, missing-data policy, and protected counter-characteristics are named before a receiving synthesis, comparison, or selection pattern uses the eval result. |
| `CC-ACE-6` | Source-side "fitness function" wording is not used as the FPF object name in the record. |
| `CC-ACE-7` | A check or test is admitted only as one eval operation when an expectation or hard constraint is being inspected. |
| `CC-ACE-8` | The eval result does not select, decide, certify, or carry an architecture-adequacy claim by itself. |

### C.32.ACE:8 - Common failures and repairs

| Failure | Symptom | Repair |
|---|---|---|
| `SourceFitnessTermAsFPFObject` | "Fitness function" is written as the object under work. | Rewrite as `ArchitectureCharacteristicEvalProgram@Project` and name evaluated rows, candidates, parity frame, eval operations, and receiving use. |
| `EvalAsCriterion` | A benchmark, monitor, or test is named as the architecture characteristic. | Return to ACS; name the criterion, bearer, scale, proxy risk, and protected counter-characteristics before writing the eval. |
| `TestModeAsEvalWhole` | The team only asks whether one candidate passes while the work question is variant comparison. | Keep the test for the hard constraint, then add eval result forms that compare candidates or expose the trade-off front. |
| `UnfairComparison` | Candidates are compared under different budgets, evidence windows, environments, or missing-data rules. | Rebuild the parity frame or record the result as unusable for selection. |
| `ResultAsDecision` | A rank, score, pass, or dashboard reading selects the architecture. | Treat the result as source material for an A.10 evidence relation when an evidence claim is current, or as comparison input when comparison is current; explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, local choice to `C.11`, publication of a selected set to `G.5`, and project architecture decision to `C.32.PAD`. |
| `SingleIndicatorGoodhart` | Work improves one optimized indicator while an unmeasured architecture concern worsens. | Limit optimized indicators, add protected counter-characteristics, and open `E.13` when proxy-to-value drift appears. |
| `LosingVariantAsError` | A candidate that lost a planned eval is recorded as a mistake. | Record it as a variant result unless an expectation caused unplanned rework; keep useful learning in the variant archive. |

### C.32.ACE:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Evals are typed evaluations over declared criteria. | Variant comparison can proceed without collapsing criteria, readings, and decisions. | The team must write the parity frame before using the result in a receiving pattern. |
| Expectation-failure tests remain one eval operation when their expectation is declared. | Error prevention remains available without replacing optimization. | Some pass-fail dashboards can no longer drive decisions by themselves. |
| Losing variants remain useful. | Architecture exploration keeps stepping stones and source-space learning. | The variant archive needs deliberate upkeep. |
| Proxy and counter-characteristic risks are explicit. | Goodhart pressure is visible before eval results drive work. | More rows may remain monitored as guardrails rather than optimized. |

### C.32.ACE:10 - Rationale

An architecture-characteristic eval program is the missing middle object between criteria rows and architecture selection. It answers "how did these candidates or structures read under this parity frame?" It does not answer "what is the criterion?", "is the measurement valid outside this use?", or "which architecture must be chosen?"

The pattern is architecture-specific because it evaluates selected structures and architecture characteristics. It stays holonic because the same eval form can apply to systems, methods, roles, organizations, cultures, built assets, AI-agent workflows, and evidence-bearing practices after bearers and scale rows are rebound.

### C.32.ACE:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ACE. Keep a source citation only when the draft uses it to set or revise an eval-program field, result-use boundary, or refresh condition.

| Source to inspect | Why this source is load-bearing here | Transfer into ACE | Concrete ACE mutation | Blocked overread |
|---|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | Separates variant, prototype, candidate, stake, solution, error, eval as variant comparison, and testing as error checking; also requires fair comparison and indicator selection. | Make eval a typed architecture evaluation over declared candidates and criteria. | `test` is admitted only as one `evalOperation` when expectation failure or hard-constraint checking is current; parity frame and result form are mandatory. | A test, check, or pass-fail result is not the whole eval program, not the criterion, and not the decision. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for incremental architecture governance and feedback under source-side fitness-function terminology. | Restore the source term to FPF eval programs over ACS rows, Q-Bundle slots, candidate structures, and parity frames. | ACE record names evaluated rows, purpose, scope, eval operation, trigger mode, result form, run context, receiving use, and refresh or retire condition. | Fitness-function wording is not imported as the FPF object name or as a new architecture characteristic kind. |
| `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`) | Current practitioner source for metric categories and governance practice after quality goals are named. | Carry metric-cadence distinctions as eval-program fields, not as criteria rows. | ACE distinguishes scope, trigger mode, result form, run context, method refs, and refresh or retire condition. | A metric, dashboard, rank, or score is not a project criterion, selected architecture, or architecture decision. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner source for objective definitions, trade-off analysis, and least-worst choices under competing characteristics. | Require declared criteria rows and protected counter-characteristics before synthesis, comparison, or selection uses eval results. | ACE rows carry proxy risk, protected counter-characteristics, and receiving use before result-driven action. | A better reading or rank does not authorize comparison, selection, choice, G.5 publication of a selected set, or decision by itself. |
| Goodhart and proxy-risk line, plus current FPF `E.13` | Optimized proxies can detach from the declared architecture concern. | Keep proxy repair in E.13 while ACE records the risk before result use. | ACE requires proxy risk and protected counter-characteristics; proxy drift exits to `E.13`. | An eval result cannot replace the declared architecture concern. |
| Current FPF `C.16`, `C.25`, `E.23`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, and `C.11` | Existing receiving patterns for measurement, Q-Bundles, repeated improvement, comparison, selection, publication of selected sets, and local choice. | Keep ACE as eval-program and eval-result boundary. | The relation table names C.16 for measurement validity, C.25 for composite quality, E.23 for improvement feedback, A.19.CPM for comparison, A.19.SelectorMechanism for set-returning selection, G.5 for publication of selected sets, and C.11 for local choice. | ACE does not validate measurement, define Q-Bundles, compare, select, publish a selected set under G.5, choose, or decide. |

**Source-currentness boundary.** Use each source row only for the ACE eval-program field, result-use boundary, or refresh condition named in that row. Recheck the row when a named book edition, source presentation, FPF receiving pattern, metric practice, or evolutionary-architecture practice changes the transferred move. If the project wants criteria-row admission, measurement validity, Q-Bundle structure, explicit comparison, selection, publication of a selected set, local choice, evidence, assurance, or decision use, leave ACE and open the receiving pattern.

### C.32.ACE:12 - Relations

- **Builds on:** `C.32.HCS`, `C.32.ACS`, `C.16`, `C.16.P`, `C.25`, `E.13`, `E.22`, `E.23`, and `A.19.CPM`.
- **Receiving uses:** `C.32.P2S` actual-structure feedback and next-synthesis repair, `C.32` candidate synthesis, `C.32.MLAO` residual optimization, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair, `A.19.CPM` comparison, `A.19.SelectorMechanism` selection, `C.11` local choice, publication of a selected set under `G.5`, and architecture-decision work for `C.32.PAD`.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, uncertainty, or cross-case comparability claim is made.
- **Structural-information boundary:** `C.33`, `C.34`, and `C.35` can supply captured structure, lost structure, preservation adequacy, generated-carrier context, or discovered-carrier context for an eval only after `C.32.ACS`, `C.16`, or `C.25` has declared what is being evaluated. ACE remains eval-program and eval-result owner; `C.33`, `C.34`, and `C.35` do not define eval programs.
- **Q-Bundle boundary:** Use `C.25` when the evaluated item is a composite quality family.
- **Test boundary:** Use `test` only as an eval operation for a declared expectation or hard constraint. Error recognition and architecture-synthesis repair use `C.32.FAIL`; non-architecture defects use the local defect-governing pattern.
- **Decision boundary:** ACE can produce readings, ranks, dominance relations, trade-off-front descriptions, and source material for an A.10 evidence relation when an evidence claim is current. Explicit comparison, set-returning selection, local choice, publication of a selected set, and project architecture decision belong to `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, and `C.32.PAD`.

### C.32.ACE:13 - Footer marker

C.32.ACE closes when the eval program names evaluated criteria, evaluated candidates or structures, parity frame, eval purpose, scope, eval operation, trigger mode, result form, method refs, proxy risks, protected counter-characteristics, receiving use, and refresh or retire condition.

### C.32.ACE:End

