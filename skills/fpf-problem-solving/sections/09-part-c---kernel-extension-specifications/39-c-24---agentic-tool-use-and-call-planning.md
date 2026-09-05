## C.24 - Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Agentic tool-use and call planning.

**Intent.** Help a practitioner turn an already fixed action or option into a budgeted call plan, then revise that plan or return a bounded checkpoint without confusing planning with selection or execution.

**Instantiates and refines Pillars.** `E.2` `P-3` Scalable Formality, `P-7` Pragmatic Utility, `P-10` Open-Ended Evolution, `P-11` SoTA Alignment, and `C.19.1` Bitter-Lesson Preference when a real scale comparison is current.

**Depends on.** `A.15` and its planning and Work patterns for Methods, descriptions, plans, performed Work, and attribution; `A.15.7` for a situation-responsive next-action decision; `C.11` for a fixed choice among a current `OptionSet`; `C.2.1` when the relied-on decision or checkpoint needs a persistent episteme; `C.18` for candidate generation; `C.19` for live-pool policy; `C.19.1` for a scale-based comparison or waiver; `C.16` for measured comparison inputs; `G.6` for call-trace representation; and `B.3` only when a named assurance use needs one bounded assurance result.

**Coordinates with.** `U.PromiseContent` for service acceptance conditions, `C.28` when a planned call is intended to support a causal use, and `E.17`/`E.24.PUB` when an already obtained result is being published or made available.

### C.24:0 - Use this when

Use `A.15.7` first when ongoing Work still needs the next action to be chosen from current facts within a domain Method. Enter `C.24` only after that action is fixed and tool or service calls must be planned. A call plan is neither the situation-responsive decision nor proof that the chosen action was performed.


Use `C.24` when a decision has already fixed the action or option and the practical question is now:

- which admitted Methods to call, in what order;
- which time, compute, cost, and risk budget to reserve;
- what stops or replans the route; and
- whether the useful output is a `CallPlan` or a `CheckpointReturn`.

Do not use it to generate candidates, keep a live pool, choose among unresolved options, execute calls, or score completed Work.

### C.24:0.1 - What goes wrong if missed

- a route is scheduled by an opaque heuristic, so nobody can see which budget is being burned or what should stop it;
- unresolved choice or pool-policy work is smuggled into a plan;
- a route description is mistaken for a Method, a plan for performed Work, or a successful probe for committed rollout; and
- replanning loses the decision that made the route admissible in the first place.

### C.24:0.2 - What this buys

- one small, tool-neutral plan that cites the accepted decision basis;
- visible budgets, stop conditions, and replan triggers before calls are made;
- one replayable call-trace reference after Work occurs; and
- one bounded checkpoint when more route probing is justified but commitment is not.

**Primary working object.** One `ATC.CallPlan : U.WorkPlan`. Each step selects a `U.Method`. A route description may help locate or constrain that Method, but remains a separate `U.MethodDescription`. Actual calls are dated `U.Work` and remain outside this planning result.

**First useful move.** Say whether the fixed action came from A.15.7 or C.11 and cite exactly one corresponding reference in `decisionBasis`. Then write the ordered Method refs, budget, stop or replan condition, and next planned action. Add route-description refs only where the route cannot be understood without them.

**Not this pattern when.** Use `C.11` while fixed-option choice is unresolved, `C.19` while treatment of a live pool is unresolved, `G.5` when the current task is selector-facing result declaration, `A.15.5` for work-entry readiness, and `A.15.1` when the question is what Work actually occurred or which Method it enacted.

### C.24:0.3 - First-minute questions

1. Which accepted A.15.7 decision or C.11 `ChoiceResult` fixed the action or option now being planned?
2. Does every planned step name an admitted Method, rather than only a vendor route or endpoint label?
3. Which budget is current: a still-upstream probe budget or an enactment/call budget?
4. What event stops or replans the route?
5. Is the useful output a plan, a checkpoint, or a return to a neighbouring pattern?

### C.24:0.4 - First output

The first useful output is one of these:

```text
CallPlan:
  decisionBasis:
    situationResponsiveDecisionEpistemeRef?  # A.15.7; only when this plan relies on the retained decision
    fixedOptionChoiceResultRef?               # C.11; only a choose-now result
  objective
  plannedCallsInOrder:
    - methodRef
      methodDescriptionRef?          # only when the route description is needed
      dependsOnPlannedStepRefs?      # only when dependency changes the route
      mayRunInParallelWithStepRefs?  # only when safe parallelism matters
  plannedBudgetEnvelope
  stopOrReplan
  nextPlannedAction
```

```text
CheckpointReturn:
  decisionBasis:
    situationResponsiveDecisionEpistemeRef?  # A.15.7
    fixedOptionChoiceResultRef?               # C.11 choose-now result
  objectiveOrTaskFamily
  testedMethodRefs
  testedMethodDescriptionRefs?
  evidenceRefs
  burnedBudget
  residualBudget
  recommendedNextAction
  commitTrigger
```


`nextPlannedAction` and `recommendedNextAction` are local fields, not claims that Work has occurred. Exactly one decision-basis reference is present. Add one of the branch-specific refs in C.24:4.4 only when that constraint still affects the plan. A plan with no current policy branch needs no policy placeholder. If neither output can cite its accepted decision basis and state what happens next, the C.24 work is unfinished.

If the A.15.7 decision changes, is withdrawn, or no longer fixes the action, reopen the plan and return to A.15.7. If the C.11 `ChoiceResult` changes or no longer says `choose now`, return to C.11. A changed live-pool branch returns separately to C.19. Do not revise the call plan as though its decision basis were still settled.

### C.24:1 - Problem frame

Tool-using Systems may plan across web services, local programs, instruments, robots, or human-operated routes. The implementation may be an LLM agent, a search system, a conventional planner, or a fixed program. The planning problem is the same: turn a fixed action or option into an ordered and bounded route without hiding route grounding, budget, or stop logic.

A local system-role kind or assignment is recorded only when that separate fact matters. When planning, revision, or a call is claimed as precise performed Work, recover each exact actual performer through A.13 and let A.15.1 independently admit the dated Work from its performer, Method, interval, and containment facts. Add the exact A.2.1 assignment reference and F.6 only when the plan or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment; F.6 identifies neither assignment nor performer, and missing or failed F.6 leaves the Work intact.

### C.24:2 - Problem

We need a tool-neutral way to produce or revise one call plan under explicit budgets and policy while keeping Method, route description, plan, performed Work, service promise, trace representation, the decision basis that fixed the action, and any assurance result distinct.

### C.24:3 - Forces

| Force | Tension |
| --- | --- |
| General method vs local shortcut | A scalable approach may improve with data or compute, while a narrow route may be safer or cheaper in the present task. |
| Exploration vs delivery | A bounded probe may reduce uncertainty, while service and cost limits require commitment or stop. |
| Assurance vs autonomy | A named high-consequence use may need a bounded assurance result, while ordinary planning should not inherit assurance apparatus. |
| Description vs enactment | A callable route description helps planning, but it is not the Method, plan, call, or evidence of performance. |

### C.24:4 - Solution

#### C.24:4.0 - Local objects and boundaries

- `ATC.CallRouteDescription` is a `U.MethodDescription` whose EntityOfConcern is the selected admitted Method and whose claims explain how that Method is carried out through the route, under A.3.2. When it carries vendor-local route data, it states the vendor or source scheme, exact scheme or API edition, intended use, and selected Method ref before any access details, inputs, outputs, or route limits.
- `ATC.CallPlan` is a `U.WorkPlan` for intended calls. Its steps select Methods and may cite route descriptions.
- `ATC.CheckpointReturn` is a C.2.1 result episteme stating what was tested, what budget was burned, and what route action is recommended next. It is not the tested Work.
- `ATC.CallGraphRef` cites the applicable `G.6` trace representation over actual call Work. The representation records or points to facts; it creates none of them.

`decisionBasis` contains exactly one of two references. `situationResponsiveDecisionEpistemeRef` refers to an episteme identified under C.2.1 because this plan relies on an A.15.7 decision; the episteme states the selected action, deciding System, intended performer, action-changing fact, relevant Method limit, and stop or feedback condition. `fixedOptionChoiceResultRef` refers to a C.11 `ChoiceResult` whose result is `choose now`. The first is not a `ChoiceResult`, and the second does not become a situation-responsive decision by being consumed here.

There is no catch-all `ATC.PolicyRef`. When a constraint branch is current, cite its actual object: C.19 `PoolPolicyResult` or `EmitterPolicy`, a C.19.1 probe, comparison, local-policy, or waiver result, or a domain constraint whose kind and defining pattern are named. Time, compute, cost, risk, stop, and replan ceilings remain fields of this plan.

#### C.24:4.1 - Owned planning operations

C.24 owns only planning and replanning:

```text
planCalls(
  decisionBasis,
  objective,
  admittedMethodRefs,
  routeDescriptionRefs?,
  budget
) -> CallPlan

revisePlan(
  currentCallPlanRef,
  checkpointOrSignalRefs,
  residualBudget
) -> CallPlan | CheckpointReturn | neighborExit
```

`A.3.1` supplies Method admission. The decision basis fixes the action or option being planned; it does not admit the Methods chosen for plan steps. An A.15.7 basis keeps the selected action, deciding System, intended performer, action-changing fact, relevant domain-Method limit, and stop or feedback condition. A C.11 basis is a `ChoiceResult` whose lawful result is `choose now`; `probe again`, `reject current set`, and `reroute` do not fix an action for C.24. C.18 may supply generated candidate or front material, and C.19 may supply a live-pool treatment that informed the decision; neither record admits a Method. Comparison comes from the selected evaluation Method and, when scale preference is claimed, `C.19.1`. A.15.1 governs the actual call or observation Work; `G.6` provides the trace representation of its independently established facts, results, and provenance relations. C.24 only constrains what the plan or checkpoint must retain for those later uses.


#### C.24:4.2 - Bounded scout or probe cycle

When the accepted decision basis permits enactment planning but the usable route is still unfamiliar, the admitted System may perform a bounded scout pass and return a `CheckpointReturn`.

If another probe could still change which option survives the `OptionSet`, the budget remains a C.11 probe budget and planning returns there. If changed live facts or domain-Method limits could change an A.15.7 action, return there instead. If the action or option remains fixed and only route shape or rollout order is uncertain, the probe uses enactment budget and its checkpoint belongs here.

A successful probe is not a commitment. Commitment needs the named `commitTrigger`, enough residual budget, and any separately required safety or assurance condition.

#### C.24:4.3 - Planning laws

**ATC-1 — Plan the call, not the app.** A plan step selects a Method. A route description, endpoint, service promise, trace row, or response does not become that Method or an actual call.

**ATC-2 — Use the actual C.19.1 branch.** Start with C.19.1's scale-claim probe. Consume its actual first result: `no scale claim yet`, `local analogy or policy`, `bounded scale comparison`, or `full Scale-Audit selected`. Only the latter two open comparison or audit work. A completed comparison may then warrant a bounded preference or `no scale-based preference`. Keep a `BLP-waiver` separate: it is used only when a declared generality preference would otherwise decide the use, and it records rationale, the admitted review System, the direct waiver-review responsibility or missing governor, and expiry or review. If comparable evidence is absent, stop the empirical preference; do not invent a slope vector or treat a waiver as evidence.

**ATC-3 — Make budgets and harm limits visible.** A `CallPlan` states its planned ceilings. A `CheckpointReturn` or Work-side record states actual burn. The admitted System stops or replans when a named ceiling or safety condition is breached.

**ATC-4 — Keep live-pool exploration declared.** Cite a C.19 `PoolPolicyResult` only while treatment of that still-live pool constrains this plan. Cite its exact `EmitterPolicy` only when the plan actually uses that profile; then record `explore_share`, including `0` when the current profile explicitly plans none. Do not fabricate either ref after the fixed action or option has made pool treatment irrelevant, and do not silently turn illumination or novelty telemetry into a decision criterion.

**ATC-5 — Preserve replay after execution.** Each actual call is recovered as dated Work with its performer, enacted Method, interval, containing-System relation recoverable under A.15.1, plan ref, actual budget delta, inputs and outputs subject to privacy, and any route-description edition used. Cite the applicable G.6 trace representation. The plan and trace do not establish these facts by themselves.

**ATC-6 — Add assurance only for a named use.** When a planning or rollout decision depends on assurance, name the target claim and use, then cite the B.3 result with its basis, disposition, limits, and reopen condition. No policy label or confidence level substitutes for that result.

**ATC-7 — Bind vendor routes to the selected Method.** Vendor-specific tokens belong in an edition-pinned `ATC.CallRouteDescription` that recovers the vendor or source scheme, exact scheme or API edition, intended use, and selected Method ref. Access details, inputs, outputs, and limits may follow. An arbitrary profile, executable adapter, or F.9 Bridge does not satisfy this binding. When executable adaptation is current, identify the Method, MethodDescription, System, and performed Work through their direct patterns. Cite an F.9 Bridge only when its relation independently obtains between two local meanings.

#### C.24:4.4 - Policy and comparison branches

Add only the branch that still constrains this plan:

```text
CallPlan optional branch fields:
  poolPolicyResultRef?             # C.19; only while live-pool treatment still matters
  emitterPolicyRef?                # C.19; only when this exact versioned profile is used
  scaleClaimProbeResultRef?        # C.19.1 first result
  scaleComparisonResultRef?        # only when the probe selected a bounded comparison
  scaleAuditResultRef?             # only when the probe selected a full Scale-Audit
  blpLocalPolicyRef?               # C.19.1 local policy or analogy, not empirical evidence
  blpWaiverRef?                    # separate from the comparison result
  explore_share?                   # only with the applicable C.19 branch
  risk_bound
  cost_ceiling
  time_ceiling
  stop_conditions
  tie_breakers?
  comparison_tolerances?
  assuranceResultRef?              # only for a named assurance use
```

Each comparison tolerance names its characteristic, bearer, scale, evidence basis, and window. Graduation, rollout, or widening uses a concrete condition defined by the cited result or direct domain pattern. Plan-local ceilings and stop conditions need no policy object. If another domain constraint is current, give its field the actual result-kind name and cite its defining pattern; do not put it in a catch-all constraint ref. When a condition relies on assurance, cite the exact B.3 result and its supported scope; no universal assurance level is inherited from C.19.

#### C.24:4.5 - Causal action-use field

Add the causal field only for a named causal use in which the planned calls are intended to observe, intervene, collect counterfactual-rung evidence, simulate for a causal claim, condition a counterfactual policy, or evaluate a policy causally:

```text
CallPlan.causalActionUseSpec?:
  causalUseQuestionRef: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalEvidenceDesignRef?
  causalSupportComponentRefs?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  supportedUse
  unsupportedUse
```

The field states the planned causal use and any support already consumed. It does not estimate an effect, prove identification, certify fairness, or turn simulation output into realized counterfactual evidence. Use `C.28` for those support questions.

#### C.24:4.6 - Public quick card

Record:

- exactly one decision-basis reference—an A.15.7 decision episteme or a C.11 `choose now` `ChoiceResult`—plus the objective and ordered Method refs;
- route-description refs only when needed, with their source scheme, exact edition, intended use, and selected Method binding;
- dependencies or safe parallelism only when they change the route;
- time, compute, cost, and risk budgets plus stop and replan conditions;
- next planned action; and
- an exact C.19 or C.19.1 result, B.3 assurance result, causal-use result, provenance ref, or named domain-constraint result only when that branch is current.

This is enough for an ordinary plan. Do not fill the heavier branches merely to make the record look complete.

#### C.24:4.7 - Closure and worked cases

Close as a `CallPlan` when route order and budgeted enactment are the current question. Close as a `CheckpointReturn` after a bounded route probe, when one further route probe remains justified. Return to A.15.7 or C.11 when the corresponding decision basis reopens; return to the applicable neighboring pattern when pool treatment, selector declaration, readiness, execution, or publication becomes the current question.

**A.15.7 decision into a known route.**

During ongoing repository-repair Work, changed source facts make `produce_patch_and_verify` the next action under the current repair Method. Using the steering Method in A.15.7, the responsible maintainer makes that decision. The retained decision names the repair agent as intended performer, the changed-source fact, and test failure as the stop and feedback condition. Because the call plan relies on the decision later, the team retains it in one episteme identified under C.2.1. The episteme describes the situation-responsive decision; it is not a C.11 `ChoiceResult`.

```text
CallPlan:
  decisionBasis:
    situationResponsiveDecisionEpistemeRef = patch_action_decision_17
  objective = produce_patch_and_verify
  plannedCallsInOrder =
    - methodRef = InspectRepositoryMethod_4
      methodDescriptionRef = inspect_repo_route_v3
    - methodRef = EditCandidateMethod_2
      methodDescriptionRef = edit_candidate_route_v2
    - methodRef = TargetedTestMethod_7
      methodDescriptionRef = targeted_tests_route_v5
  plannedBudgetEnvelope = {time<=45_minutes, compute<=x2, cost<=y2, risk<=r2}
  stopOrReplan = targeted_tests_fail_twice
  nextPlannedAction = enact_now
```

The plan claims no call occurred. If the first call is performed, recover its dated Work, performer, assignment where current, Method, interval, plan ref, and trace representation through the direct patterns.


**Unfamiliar route.**

```text
CheckpointReturn:
  decisionBasis:
    fixedOptionChoiceResultRef = ci_route_choice_09
  objectiveOrTaskFamily = unfamiliar_ci_failure
  testedMethodRefs = [LogTraceMethod_2, MinimalReproductionMethod_5]
  evidenceRefs = [trace_result_1, reproduction_result_1]
  burnedBudget = 1_probe_cycle
  residualBudget = 2_probe_cycles
  recommendedNextAction = run_minimal_reproduction_once_more
  commitTrigger = reproduction_is_stable_and_required_evidence_is_current
```

**Two vendor routes with one token.** Vendor A and Vendor B both publish a route called `search`. `vendor_a_search_v2` states scheme `VendorA API`, edition `2026-07`, intended use `repository text search`, and selected Method `RepositoryTextSearchMethod_3`. `vendor_b_search_v5` states scheme `VendorB agent tools`, edition `2026-08`, intended use `web source retrieval`, and selected Method `WebSourceRetrievalMethod_8`. The shared token identifies neither binding; the description fields do. An executable adapter, if used, remains distinct from the Method it implements, and its execution remains separate Work.

**Scale comparison, when current.** The cheap C.19.1 probe for `BatchSearchMethod_3` and `IndexedSearchMethod_6` returns `bounded scale comparison` for the same repository-search task and `10k–100k files` window. The comparison then uses elapsed time and missed-match rate from `repo_search_benchmark_12`, including uncertainty and cost limits, and warrants a preference for `IndexedSearchMethod_6` only inside that window. If one Method is evidenced only on small text files and the other only on large mixed repositories, the comparison returns `no scale-based preference`. A project may separately cite a local policy or `BLP-waiver`; neither changes the empirical result.

**Near misses.** A route label with no recovered Method remains probe material. A plan with no Work is still intent. A trace row does not prove performer, assignment, Method, or service acceptance. A successful probe without a commit trigger is not rollout.

**Transfer examples.** The same result shape works for research assistance, program repair, and lab automation. The Methods and safety conditions differ; the plan/checkpoint boundary does not.

### C.24:6 - Bias-Annotation

Keep notation and vendors out of the conceptual contract. Do not average unlike scales. Do not let a route description, plan, trace, response, or confidence label stand in for a Method, performed Work, evidence result, or assurance result.

### C.24:7 - Conformance Checklist

1. Every result cites exactly one accepted decision basis: the A.15.7 decision episteme or the C.11 `ChoiceResult` that made planning current.
2. Every planned step names an A.3.1-admitted Method that realizes or supports the fixed action. The decision basis fixes the action or option; selecting it does not establish Method identity. Route-description refs remain separate and optional.
3. The plan records time, compute, cost, and risk ceilings plus stop or replan conditions.
4. C.18 candidates or front material and C.19 live-pool treatment may inform the decision basis but do not admit Methods; C.24 owns only planning and replanning results.
5. A scale branch first cites one actual C.19.1 probe result, then any selected comparison or Scale-Audit result; a `BLP-waiver` remains separate from evidence.
6. Every vendor-bound `ATC.CallRouteDescription` identifies source scheme, exact edition, intended use, and selected Method; an arbitrary profile, adapter, or Bridge cannot substitute.
7. Each current policy or constraint ref resolves to its actual C.19, C.19.1, B.3, or domain-defined object; a plan with no such branch remains valid.
8. A `CheckpointReturn` states tested Methods, evidence, burned and residual budget, next action, and commit trigger.
9. Actual call claims retain dated Work, performer, Method, interval, plan, budget delta, and G.6 trace refs; the admitted System performs and records the Work.
10. A causal action-use branch uses the current C.28 question, support-component, and support-result contract and grants no downstream authority.
11. The ordinary quick path remains readable without ontology or assurance apparatus.

### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Planning the whole tool lifecycle.** Keep candidate generation, selection, execution, scoring, and publication outside C.24.
- **Route description as Method.** Recover the Method or keep the route in probe state.
- **Plan as execution.** Put actual burn and call facts in Work-side results and the trace.
- **BLP slogan as comparison.** Use C.19.1's probe and any selected comparison; keep a waiver separate or return no scale claim or no scale-based preference.
- **Catch-all policy or profile ref.** Cite the actual PoolPolicyResult, EmitterPolicy, C.19.1 result, B.3 result, or domain-defined constraint, or omit the branch.
- **Confidence threshold as assurance.** Use a direct condition and cite B.3 only for a named assurance use.
- **Executable adaptation by implication.** Store the binding in a route description; identify any executable adaptation independently.
- **Successful probe as commitment.** Require a checkpoint with a commit trigger.

### C.24:9 - Consequences

Tool use becomes inspectable before execution: the result shows which accepted decision fixed the action or option, which Methods are planned, what budget is reserved, and what changes the route. Identical vendor tokens remain distinguishable by source scheme, edition, intended use, and selected Method. The cost is explicit Method grounding and branch-specific constraint refs. Heavy assurance, causal, or scale-comparison records appear only when their use justifies them.

### C.24:10 - Rationale and current practice

**Qualification window.** This comparison uses the source set as of 2026-08-21. Reopen it when a later result changes the relative value of explicit planning, route grounding, active information gathering, checkpoint use and replanning, multidimensional evaluation, or long-horizon budget and dependency handling for the declared use.

| Contribution | Adopted, adapted, or rejected move | Boundary and trade-off |
| --- | --- | --- |
| ToolPlanner, EMNLP 2024, [ToolPlanner: A Tool Augmented LLM for Multi Granularity Instructions with Path Planning and Feedback](https://aclanthology.org/2024.emnlp-main.1018/) | **Adopt:** keep path planning, feedback, and replanning explicit instead of hiding them inside one call loop. | The gain is replayable route revision; the cost is a plan object. The LLM benchmark does not define universal FPF objects. |
| PlanningArena, ACL 2025, [PlanningArena: A Modular Benchmark for Multidimensional Evaluation of Planning and Tool Learning](https://aclanthology.org/2025.acl-long.1499/) | **Adapt:** check tool selection, reasoning, user-input interpretation, and execution-relevant constraints separately instead of treating one aggregate score as plan quality. | Its scenarios do not set universal weights or safety limits. C.24 keeps only the dimensions that change this plan or checkpoint. |
| IBM Research, ECAI 2025, [From Grounding to Planning: Benchmarking Bottlenecks in Web Agents](https://research.ibm.com/publications/from-grounding-to-planning-benchmarking-bottlenecks-in-web-agents) | **Retain with a rejected overread:** keep route grounding distinct from plan quality, but reject the claim that planning is always the dominant bottleneck. | This preserves a cheap diagnostic split without hard-coding a web-agent bottleneck order. |
| Aghzal et al., 2026 preprint, [Why Do LLM-based Web Agents Fail? A Hierarchical Planning Perspective](https://arxiv.org/abs/2603.14248) | **Adopt:** separate high-level planning, low-level execution, and replanning; a sound plan does not excuse failed grounding or adaptive control. | The result makes the IBM split conditional. It does not make every web-agent layer mandatory in a known fixed route. |
| DeepPlanning, ACL 2026, [DeepPlanning: Benchmarking Long-Horizon Agentic Planning with Verifiable Constraints](https://aclanthology.org/2026.acl-long.335/) | **Adapt:** retain global budgets, dependencies, or safe parallelism when material, and use the bounded scout and checkpoint cycle for information needed before commitment. | Long-horizon benchmarks expose degradation and efficiency trade-offs, but their task schemas do not belong in every ordinary call plan. |
| `C.19.1` current scale-comparison sources and method | **Adopt conditionally:** use Bitter-Lesson pressure only with the actual probe and a named bearer, scale window, evidence, cost, safety, and uncertainty. | Generality is not a winner by label; local policy and waiver stay separate from empirical comparison. |

This set is non-dominated for C.24's declared use because it keeps the smallest common planning contract while exposing the failure dimensions that later work shows can move independently. Remove a field when it changes no route, stop, reliance, or replay; reopen when a new contribution changes that trade-off rather than merely adding another benchmark.

### C.24:12 - Relations

- `A.3.1` supplies admitted Method identity; neither decision branch admits a Method merely by selecting an action.
- The steering Method in `A.15.7` is used to reach the situation-responsive decision cited through `situationResponsiveDecisionEpistemeRef`; when this plan relies on the decision, its episteme has the identity conditions defined in C.2.1.
- A C.11 `ChoiceResult` whose result is `choose now` is cited through `fixedOptionChoiceResultRef`.
- `C.18` supplies generated candidate or front material, and `C.19` supplies `PoolPolicyResult` or `EmitterPolicy` only when live-pool treatment still constrains the plan. Neither admits a Method.
- `C.19.1` supplies the scale-claim probe, any selected comparison or Scale-Audit result, and any separate local policy or `BLP-waiver`; C.24 invents none of them.
- `A.15`, `A.15.1`, `A.15.2`, `A.2.1`, and `F.6` keep Method, description, plan, Work, performer, and attribution distinct.
- `G.6` supplies the trace representation cited by `ATC.CallGraphRef`.
- `B.3` supplies one bounded assurance result only when a named assurance use is current.
- `C.28` supplies causal-use support when the plan is used for causal evidence, intervention, policy, fairness, or counterfactual work.
- `C.27` evaluates temporal claims about speed, narrowing, recovery, or stop/replan rate. More calls or faster narrowing is not success by itself.
- `E.23` may use C.24 plans and checkpoints inside improvement Work; C.24 does not restate the improvement loop.
- `E.10.MOVE`, `E.11.PUR`, and `A.15.5` recover project moves, pattern-use recommendations, and work-entry readiness when those questions are not plan-local.

### C.24:End

