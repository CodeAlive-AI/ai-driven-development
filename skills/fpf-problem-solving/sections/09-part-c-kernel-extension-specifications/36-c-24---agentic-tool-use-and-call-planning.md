## C.24 - Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Agentic tool-use and call planning.

**Intent.** Govern admissible tool-call planning and replanning under explicit budget, assurance, and policy while keeping upstream choice, pool policy, planning, and execution distinct.

**Instantiates and refines Pillars.** `E.2` `P-3` Scalable Formality, `P-7` Pragmatic Utility, `P-10` Open-Ended Evolution, `P-11` SoTA Alignment, and the Bitter-Lesson Preference: prefer scalable, general methods that benefit from more data or compute over fragile hand-tuned heuristics when assurance and cost stay comparable.

**Depends on.** A-kernel (`A.1–A.15`) for holonic basics and Role-Method-Work separation; `B.3` Trust & Assurance (`F–G–R` with CL penalties); `E.3/E.5` (precedence and Guard-Rails); `C.5` `Resrc-CAL`; `C.18` `NQD-CAL` (candidate generation and declared set results); `C.19` `E/E-LOG` (explore-exploit policies); optional `Compose-CAL` and `KD-CAL` where available.

**Coordinates with.** `U.WorkPlan` and `U.PromiseContent` bindings (acceptance gates), Working-Model publication discipline per `B.3`, and evidence or provenance (`G.6`).

### C.24:0 - Use this when

- one concrete choice result already exists and the next task is now how to plan, gate, sequence, and replan tool calls admissibly
- the next admissible output should be one enactment-facing `CallPlan` or one `CheckpointReturn`, not one more local choice result or pool-policy result
- budget, assurance, and stop conditions must be visible before calls are burned

### C.24:0.1 - What goes wrong if missed

- calls get scheduled by ad-hoc heuristics, so the plan cannot say which budget is being burned or what event should stop or replan execution
- planning quietly collapses into execution, or execution quietly inherits unresolved upstream choice and pool-policy questions
- a successful probe is mistaken for committed rollout even though the commit trigger was never made explicit

### C.24:0.2 - What this buys

- one tool-agnostic planning record for admissible calls, budgets, stop conditions, and replan triggers
- one explicit enactment record with objective, budget, stop conditions, and next planned action
- one replayable call graph and assurance record instead of one opaque chain of tool invocations

### C.24:0.3 - First-minute questions

- Has one choice result already been fixed, with the accepted decision material named, so that planning may begin now?
- Which budget is being burned now: enactment budget, tool-call budget, or still one upstream probe budget?
- What event stops or replans the route?
- Is the next admissible output one `CallPlan`, one `CheckpointReturn`, or a neighbouring-pattern exit?

### C.24:0.4 - First output

The first useful output is either one enactment-facing `CallPlan` with the current objective, cited route descriptions, the planned budget envelope, the stop or replan condition, and the next planned action stated explicitly in one place, or one bounded `CheckpointReturn` with the current objective or task family, the burned and residual actual budget, the commit trigger, and the recommended next action stated explicitly in one place.

In C.24, move-like wording is plan-local shorthand only when it means `nextPlannedAction` inside a `CallPlan` or `recommendedNextAction` inside a `CheckpointReturn`. It does not name a general project move, pattern-use recommendation, work-entry readiness relation, performed work, or a whole `U.WorkPlan`. If the current source wording asks which FPF pattern use is recommended, use `E.11.PUR`; if it asks whether intended work is ready to start, use `A.15.5`; if it uses move-like wording outside C.24 call planning, restore the project concern with `E.10.MOVE`.

If that first output still cannot be written honestly, the current planning result is not finished `C.24` planning yet.

### C.24:1 - Problem frame

Modern systems in agential roles increasingly rely on tool-call planning: selecting admissible tool-service routes, arranging intended call work, and replanning under uncertainty. Without a calculus:

* calls are scheduled by **ad-hoc heuristics**,
* **budgets** (compute, cost, wall-time) are implicit,
* **assurance** and **policy provenance** are lost, and
* systems in agential roles either over-constrain themselves with brittle scripts or wander without guard-rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM-based, search-based, code-based, robotic) plan calls **admissibly**, **auditably**, and **scalably**. (Role-Method-Work alignment; didactic primacy.)

Immediate failure indicators for this pattern:

* the current planning result cannot say whether one choice result already exists,
* the current text cannot distinguish route description, call plan, and executed call work,
* the budget being burned is still only probing-before-choice budget rather than enactment or tool-call budget, or
* the next admissible output is still undefined as one enactment-facing plan, one `CheckpointReturn`, or one neighbouring-pattern exit.

If the question under repair is still which fixed option should survive now, apply `C.11`. If it is still pool policy over several still-live candidate lines, apply `C.19`. If it is already public selected-set publication, apply `G.5`.

### C.24:2 - Problem
We need a **tool-agnostic** way to (i) identify **admissible route descriptions**, (ii) compose one **call work plan** that cites them, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain-specific heuristics into the core and **without** collapsing `U.MethodDescription`, `U.WorkPlan`, and `U.Work` into one object.

### C.24:3 - Forces

| Force                                    | Tension                                                                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **General methods vs. bespoke local heuristics**       | Scalable, model-centric search ↔ short-term wins of bespoke scripts (guarded by **Bitter-Lesson Preference**).        |
| **Assurance vs. Autonomy**               | F-G-R gates & CL penalties ↔ system latitude to sequence calls and learn online.                                       |
| **Exploration vs. Delivery**             | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E-LOG policy).                                |
| **Route vs. plan vs. execution**         | `U.MethodDescription` ↔ `U.WorkPlan` ↔ `U.Work` ↔ service promises (`U.PromiseContent`).                              |

### C.24:4 - Solution — Signature & Realization

**Local value names.**
*`ATC.CallRouteDescription`* is a `U.MethodDescription` with `accessSpec` for one tool service or callable route;
*`ATC.CallPlan`* is a `U.WorkPlan` specialised for intended tool-call work; it cites one or more `ATC.CallRouteDescription` editions plus planned order, budget ceilings, stop or replan triggers, and `nextPlannedAction`;
*`ATC.CallGraph`* is an evidence or provenance graph over a `U.Work` ledger;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E-LOG) and local call gates **including BLP tolerances (alpha, delta)**.

**Roles.**
A **System in AgentialRole** prepares or revises one **CallPlan** that cites one or more **CallRouteDescription** editions. Upon enactment, a **Performer** executes **Work** (calls), and **Observers** record **Observations** with acceptance checks. Route descriptions stay design-time; the call plan stays schedule-of-intent; actual call work stays run-time. (A.15 strict distinction.)

**Operators (Gamma_agential; CAL, conceptual):**

1. `Gamma_agential.eligible(tool, TaskSignature, K_ctx) -> {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow-list or deny-list, and context K (including safety constraints).

2. `Gamma_agential.enumerate(TaskSignature, K_ctx) -> CandidateSet<ATC.CallRouteDescription>`
   Returns admissible callable route descriptions. It **MAY** delegate to **NQD-CAL** for heterogeneous route families and **MUST** apply the current **E/E-LOG lens** (objectives & telemetry) to tag candidates.

3. `Gamma_agential.plan(Objective, CandidateSet, Budget, ATC.Policy) -> ATC.CallPlan`
   Produces one **call plan** that cites the selected route descriptions, declares one planned budget envelope (compute, cost, time, risk), one intended call order, and one stop or replan policy. Internal route logic remains in the cited method descriptions; the plan is a `U.WorkPlan` that cites method descriptions, not a method description and not yet work.

4. `Gamma_agential.execute(ATC.CallPlan) -> {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint-fit) and logs provenance suitable for B.3 assurance reporting (design-time and run-time separated).

5. `Gamma_agential.replan(Signals, ATC.CallPlan, BudgetPrime) -> ATC.CallPlanPrime`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves editioned policy, cited route descriptions, and context.

6. `Gamma_agential.score(Route or PlanAlternative) -> <ValueProxies, Cost, Risk, FGR_floor>`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E-LOG lens** and leaves final dominance to declared policies.

#### C.24:4.1 - Bounded scout/probe cycle for unfamiliar task families

When the choice result is already fixed enough that enactment planning is admissible under `C.24`, but the route across heterogeneous or unfamiliar callable approaches is still uncertain, the system may spend a bounded scout/probe budget before committed rollout and return one checkpoint package that compares the tested routes.

If additional probing could still change which option survives the current `OptionSet`, the budget is still `C.11`-side epistemic budget and the question reroutes upstream. If choice result is already fixed and the uncertainty is only about route or rollout shape, the budget is now enactment budget and the checkpoint belongs in `C.24`.

That `CheckpointReturn` should state the declared utility objective and current `TaskFamily`, the route descriptions or candidate approaches tested, the evidence on each route, the burned and residual actual budget, the recommended next action, and the commit trigger named by value that would justify leaving probe state.

A successful probe does not by itself justify a larger burn or a committed rollout. `C.24` carries the `CheckpointReturn` record and call-plan semantics for this probe loop; `A.15` carries the DesignRunTag split and `E.16` carries the budget partition plus guard and ledger enforcement. Low-human-overlap approaches remain sound only while they stay tied to the declared utility objective, budget boundaries, and evidence locus explicitly.

**Bridge to neighboring patterns.** `ProbeBudget` belongs to `C.11` while it means epistemic budget for further probing before choice. `C.24` carries budgets once they are enactment, tool-call, or rollout budgets. If the question is still which option survives now, apply `C.11`; if it is now pool policy over several still-live candidate lines, apply `C.19`; if it is selector-facing publication of the selected result, apply `G.5`.

**Explicit enactment result.** A conformant `C.24` pass should therefore leave either one enactment-facing `CallPlan` that states the current objective, the cited route descriptions or planned call order, the planned budget envelope, the stop or replan condition, and the next planned action, or one `CheckpointReturn` that states the current objective or task family, the burned and residual actual budget, the evidence locus, the commit trigger, and the recommended next action.

**Unfinished-state rule.** A `C.24` result remains unfinished when it cannot say whether execution should continue now, pause at one checkpoint, or reroute, when it confuses route description with plan or plan with executed work, or when it does not state which budget is planned versus already burned and what event would stop or replan the current route.

**Normative Laws (ATC-Laws).**

* **ATC-1 (Model-the-Call, not the App).** A tool call is one **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule intended calls and cite route descriptions but are neither the route descriptions themselves nor the calls. (A.15.)
* **ATC-2 (Bitter-Lesson Preference).** When two admissible choices are within **delta (assurance)** and **alpha (budget)**, **prefer the more general, scale-benefiting method** whose **slope vector Pareto-dominates** under the declared E/E-LOG objectives; any override **MUST** record a **BLP-waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC-3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall-time, and risk; execution **MUST** abort or replan on breach. Actual burned or residual budget belongs in `CheckpointReturn`, `CallGraph`, or other work-side reporting, not inside the `CallPlan` field set.
* **ATC-4 (Explore-Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E-LOG profiles**. **Informative defaults**: `0` for safety-critical or deterministic tasks; `approx 0.2-0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination telemetry into dominance **requires explicit policy**.
* **ATC-5 (Provenance & Replay).** Every call **MUST** emit a **CallGraph** with: Service id, cited MethodDescription edition, inputs and outputs (redacted per privacy), `CallPlan` ref, **EmitterPolicyRef**, and budget deltas. (NQD/E/E provenance fields apply when used.)
* **ATC-6 (Assurance-First Decisions).** Selection **MUST** respect B.3: WLNK minima on F/R (weakest-link floors), CL penalties on integration, and **no** chimera scores across design-time and run-time scopes. Publish **<F,G,R>** for the typed claim `this plan is admissible under K,S`.
* **ATC-7 (Notation/Vendor Independence).** Core pattern text **MUST NOT** encode vendor-specific tokens; bindings occur in Context via Bridges/Profiles. (Lexical guard-rails.)

#### C.24:4.1a - Planning under budget must consume the same declared doctrine
#### C.24:4.1b - Causal action-use spec for call plans

When a tool-call plan selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation work, the `CallPlan` carries an optional causal action-use spec and cites `C.28` for the causal-use authority.

Optional `CallPlan.causalActionUseSpec?`:

```text
CallPlan.causalActionUseSpec? {
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  naturalBehaviorPolicyRef?: NaturalBehaviorPolicyRef
  evaluationPolicyRef?: EvaluationPolicyRef
  causalEvidenceSupportBasis?: CausalEvidenceSupportBasis
  causalInterventionSpecRef?
  counterfactualConditioningRef?
  counterfactualSamplingRealizabilityProfileRef?
  causalUseEvidenceDesignRef?
  offPolicyCausalEvaluationProfileRef?
  causalUseSupportRecordRef?: CausalUseSupportRecordRef
  causalUseSupportVerdict?: CausalUseSupportVerdict
  supportedUse: CausalUseSupportStatement
  unsupportedUse: CausalUseUnsupportedStatement
}
```

The causal action-use tail may be omitted only when the call plan does not reach `CausalUseActivation`: it is not using the call sequence as causal support, not choosing between observation/intervention/counterfactual-policy regimes, and not publishing the result as causal evidence. If the plan says the call will prove, estimate, improve, prevent, or counterfactually establish an outcome, the support tail is present or the wording is downgraded.

What changes in practice: a call plan that probes, intervenes, samples, simulates, or evaluates a policy for a causal purpose must state `CausalUseClaimKind` and the causal regime of the planned action before execution evidence is treated as support for a causal-use claim.

What this does not establish: `C.24` does not estimate effects, prove identification, certify fairness, or turn simulation output into realized counterfactual-rung evidence; it governs admissible call planning and redirects causal-use support to `C.28`.

- Planning should reuse the declared source set, decision lens, probe budget, and stopping condition rather than creating one planning-only choice semantics.
- Budgeted sequencing may mix exploitation and exploration, but the declared source set and the declared reason for the next probe must stay recoverable.
- Use planning language such as `probe next`, `hold as archive`, `apply G.5 for shortlist publication`, or `stop for now` only when the relevant lens-side reason is stated directly.
- `explore_share`, `backstop_confidence`, probe budgets, and replan triggers are planning harmonization terms for that same declared choice doctrine.
- They may regulate sequence and stopping; they do not redefine `Front`, `Archive`, `Shortlist`, or `SelectionSlot`.
- If the next planned output is one public `Shortlist` or `RankedShortlist`, `C.24` should name that as a neighbouring-pattern exit to `G.5`, not emit the selector artifact itself.

#### C.24:4.2 - Policy profile and BLP precedence

**ATC-Policy fields (conceptual).**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_alpha, BLP_delta_delta }` - realised by referencing an `E/E-LOG` `EmitterPolicy` and adding Bitter-Lesson-Preference clauses. Defaults inherit from `C.19`; any deviation is editioned.

**BLP precedence.** In conflicts with tactics that hard-code narrow scripts, the Bitter-Lesson Preference applies subject to `E.3/E.5` precedence. Where scripts encode safety-critical gating or regulatory compliance, scripts prevail unless the governing context publishes the override rationale, expiry, measured hazard avoided, and planned re-evaluation window.

#### C.24:4.3 - Didactic quick card

**Agentic Call Plan (public field set).**
`Objective - Context(K) - RouteRefsInOrder[edition-pinned] - BudgetEnvelope{time_budget, compute_budget, cost_budget, risk_limit} - PolicyRef - Explore-share - StopConditions - ReplanConditions - BLP tolerances - BLP waiver (if any) - Assurance<F,G,R|K,S> - Provenance ids`

#### C.24:4.4 - Explicit enactment outputs and closure rule

A finished `C.24` pass should publish one enactment result rather than one vague statement that the system now has a plan.

Two output shapes are admissible here:

- one enactment-facing `CallPlan`; or
- one bounded `CheckpointReturn` when probing is still the admissible next action inside enactment planning.

A `CallPlan` should state at least these fields:

- current objective;
- cited route descriptions or planned call order;
- active policy or planning state;
- planned budget envelope or reserved budget;
- stop or replan condition;
- `nextPlannedAction` if the current plan is accepted now.

A `CheckpointReturn` should state at least these fields:

- current task family or objective;
- candidate routes tested so far;
- evidence on those routes;
- burned and residual actual budget;
- recommended next action;
- explicit commit trigger.

A compact result may therefore look like:

```text
CallPlan(
  objective = answer_question_Q,
  policyRef = ee_policy_v1,
  routeRefsInOrder = [search_route_v3, retrieve_route_v1, synthesize_route_v2, code_check_route_v1],
  plannedBudgetEnvelope = {time<=60_minutes, compute<=x1, cost<=y1, risk<=r1},
  stopOrReplan = low_R_or_cost_ceiling,
  nextPlannedAction = enact_now
)
```

or:

```text
CheckpointReturn(
  taskFamily = unfamiliar_lab_protocol,
  testedRoutes = [route_A, route_B],
  burnedBudget = 2_runs,
  residualBudget = 1_run,
  recommendedNextAction = probe_route_B_once_more,
  commitTrigger = route_B_clears_assurance_floor_L1
)
```

Close as one enactment-facing `CallPlan` when the choice result is already fixed enough that execution order, gating, and replanning are now the call-planning question. Close as one `CheckpointReturn` when bounded scout/probe work is still admissible inside enactment planning. Return to the neighbouring pattern when the result has actually fallen back into local choice, pool policy, or selector-facing publication.

If the result still does not state what should execute now, what budget is planned or already burned, and what event stops or replans the route, it is still unfinished `C.24` work.

#### C.24:4.4a - Worked closure slice

Two short contrasts keep the closure law practical.

**Known route, execution should begin now.**
When the objective and route are already fixed enough, `C.24` should close as one enactment-facing call plan:

```text
CallPlan(
  objective = produce_patch_and_verify,
  routeRefsInOrder = [inspect_repo_route, edit_candidate_route, run_targeted_tests_route],
  plannedBudgetEnvelope = {time<=45_minutes, compute<=x2, cost<=y2, risk<=r2},
  stopOrReplan = targeted_tests_fail_twice,
  nextPlannedAction = enact_now
)
```

**Unfamiliar route, one bounded scout pass still admissible.**
When the route is still uncertain inside enactment planning, `C.24` should close as one `CheckpointReturn`:

```text
CheckpointReturn(
  taskFamily = unfamiliar_ci_failure,
  testedRoutes = [log_trace_route, minimal_repro_route],
  burnedBudget = 1_probe_cycle,
  residualBudget = 2_probe_cycles,
  recommendedNextAction = run_minimal_repro_once_more,
  commitTrigger = repro_is_stable_and_assurance_floor_L1_holds
)
```

The practical distinction is simple: if route order and budgeted execution are already the call-planning question, emit one `CallPlan`; if bounded scout work is still the call-planning question inside planning, emit one `CheckpointReturn`.

1. **Research-assistance system in agential role.**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table or plot generator.
   **Plan:** cite route descriptions for `search`, `retrieve`, `synthesize`, and `code_check`; declare `explore_share approx 0.4`; replan on sentinel `low_R`.
   The admissible structure here is one declared budget envelope, one explicit route order, and one visible replan trigger.

2. **Program-repair system in agential role.**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** keep repo-introspection, patch-application, and targeted-test route descriptions distinct; use scout quota across patch families before committed rollout.

3. **Lab-automation system in agential role.**
   Task: adjust a wet-lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** a bounded probe or pilot can inform the route, but committed rollout waits for the declared commit trigger and assurance floor.

### C.24:6 - Bias-Annotation

Lexical firewall and notation independence apply; no vendor tokens; mixed-scale characteristics are never averaged; route descriptions remain distinct from `U.WorkPlan`, and both remain distinct from executed `U.Work`; a successful probe remains distinct from committed rollout until the commit trigger is satisfied.

### C.24:7 - Conformance Checklist

1. **CC-ATC-1 - Declared separation.** `ATC.CallRouteDescription` is a `MethodDescription`; `ATC.CallPlan` is a `U.WorkPlan` that cites route descriptions; execution is `Work`; acceptance is via `U.PromiseContent`. No method-side route logic or actual burn is smuggled into the `U.WorkPlan` field set.
2. **CC-ATC-2 - Budgets on record.** Time budget, compute budget, cost ceiling, and risk limit exist ex ante; stop conditions are listed.
3. **CC-ATC-3 - E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC-ATC-4 - Assurance tuple.** Publish the typed claim `Plan admissible under K,S` with `<F,G,R>` and CL penalties traceable in the `CallGraph` SCR. Design-time and run-time never merged.
5. **CC-ATC-5 - BLP waiver discipline.** Any heuristic override against a general method includes expiry and re-evaluation date.
6. **CC-ATC-6 - Provenance minimum.** Record `{PromiseContentRef, CallPlanRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC-ATC-7 - Notation independence.** No vendor tokens in conceptual text; bindings via Bridges or Profiles only.
8. **CC-ATC-8 - BLP tolerances declared.** `alpha/delta` tolerances are present in `ATC.Policy` or referenced via the active `E/E-LOG` profile.
9. **CC-ATC-9 - `CheckpointReturn` for bounded specialization.** When one route still uses scout/probe discipline on a new task family, it SHALL publish one `CheckpointReturn` with candidate routes, evidence, burned/residual actual budget, next action, and commit trigger; a successful probe alone never counts as committed rollout.
10. **CC-ATC-10 - Recoverable enactment closure.** When `C.24` returns one enactment-facing call plan or one `CheckpointReturn`, the `CallPlan` SHALL state current objective, route refs in order, planned budget envelope, stop or replan condition, and `nextPlannedAction`, while `CheckpointReturn` SHALL state burned/residual actual budget plus next action and commit trigger.
11. **CC-ATC-11 - Neighboring-pattern boundary.** If the question under repair is still fixed-option choice, pool policy over several live lines, or selector-facing publication, `C.24` SHALL apply `C.11`, `C.19`, or `G.5` rather than restating those patterns.
12. **CC-ATC-12 - Role discipline.** User-facing prose and emitted artifacts SHALL speak about systems in agential roles or equivalent typed performers, not one generic `agent` head, when that generic head would blur the holder kind.
13. **CC-ATC-13 - Causal action-use spec.** If one `CallPlan` selects observation, intervention, counterfactual-rung evidence collection, counterfactual policy conditioning, or off-policy causal evaluation for a causal purpose, it SHALL carry `CallPlan.causalActionUseSpec?` with `targetCausalityLadderRung`, `causalUseClaimKind: CausalUseClaimKind`, supported use, unsupported use, and a `C.28` causal-use support reference rather than letting call-planning vocabulary certify the causal claim.

### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Treating route description as plan.** Avoid by keeping callable logic in `ATC.CallRouteDescription` and keeping `ATC.CallPlan` as one `U.WorkPlan` that cites it.
- **Treating planning as execution.** Avoid by publishing actual burn only through `CheckpointReturn`, `Work`, and `CallGraph`, not inside the `CallPlan` field set.
- **Burning enactment budget while the question under repair is still upstream choice or pool policy.** Avoid by rerouting unresolved fixed-option choice to `C.11` and unresolved live-pool governance to `C.19` before building one call plan.
- **Counting a successful probe as committed rollout.** Avoid by publishing one `CheckpointReturn` with a visible commit trigger instead of smuggling rollout through a positive scout result.
- **Hiding stop conditions or replan triggers.** Avoid by making them part of the public `CallPlan` field set rather than one private implementer intuition.

### C.24:9 - Consequences

- tool use under systems in agential roles becomes inspectable as one admissible plan, not one opaque sequence of calls
- downstream work receives one explicit enactment record with objective, route refs, budget envelope, stop conditions, and `nextPlannedAction`
- the cost is stricter discipline around route-description versus plan versus work separation, explicit budgets, and visible policy state before execution begins

### C.24:10 - Rationale

`C.24` exists because tool-use systems fail in a distinctive way: they can look adaptive while actually hiding route choice, budget burn, stop conditions, and replan logic inside one opaque execution chain. A separate planning calculus is therefore necessary so that tool use remains auditable, replayable, and governable before the first irreversible call is made.

Source-use relation and source-currentness for this rationale: these rows are current-practice pressure and BLP-neighbour alignment, not a standalone `SoTA-Echoing` table. A current tool-use or agentic-loop source becomes load-bearing only when it changes one `CallPlan`, `CheckpointReturn`, budget, stop or replan condition, BLP waiver, or relation row.

- Contemporary tool-use systems in agential roles work best when planning, feedback, and replanning stay explicit rather than collapsing into one brittle script. The practical implication is to publish one `U.WorkPlan` that cites route descriptions and carries stop or replan triggers before execution.
- Post-2015 search, optimization, and agentic systems also show that bounded probing is useful but dangerous when it silently becomes commitment. The safeguard here is the explicit `CheckpointReturn` plus visible commit trigger and one explicit split between planned budget envelope and burned actual budget.
- Scaling-first practice favors general, learnable methods over fragile hand-tuned tactics when assurance and cost remain comparable. The practical implication is not blind optimism but disciplined BLP: when a narrow heuristic wins, record the waiver, expiry, and re-evaluation window.
### C.24:12 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a tool-use plan claiming that tool use changes debugging, learning, search, repair, rollout, narrowing, uncertainty reduction, stabilization, or stop/replan rate.
- This pattern keeps: call planning, tool-use sequence, budget, stop/replan, and work trace.
- Non-admissible use: tool-call count, more context, or faster narrowing is effort evidence or input evidence at most; it is not task-success, reasoning-quality, evidence-quality, repair-success, cost, or validity-window evidence by itself.

- Exit: a speed-up claim names task outcome, evaluation harness, repair-success evidence locus when claimed, cost or budget condition, validity window, stop or replan condition, and non-admissible use as a benchmark claim; C.24 remains the tool-use pattern.

Builds on: `A.15` Role-Method-Work alignment (planning vs execution vs service), `B.3` Trust and Assurance (`F-G-R` with `CL`), `C.5 Resrc-CAL`, `C.18 NQD-CAL` (candidate generation and declared set results), and `C.19 E/E-LOG` (policies). Coordinates with `C.28` when a call plan is used to observe, intervene, collect counterfactual-rung evidence, condition a counterfactual policy, or evaluate a policy for causal-use support. Coordinates with `E.23` when a repeated quality-improvement loop is enacted through tool-using agents: `C.24` carries call plans, checkpoint returns, tool-call budgets, stop or replan conditions, and the separation among `CallRouteDescription`, call plan, and executed work; it does not restate the `E.23` loop method, BLP comparison and cost discipline, or other object-under-improvement evaluations governed by their direct patterns. Coordinates with `E.10.MOVE`, `E.11.PUR`, and `A.15.5` when source wording about a move is not plan-local `nextPlannedAction` or `recommendedNextAction`. Constrains: any `U.PromiseContent` used as a tool MUST expose acceptance conditions and observation hooks sufficient for `B.3` reporting. Enables: human-facing Working-Model publication forms with policy and assurance disclosures while keeping design-time and run-time separated.

### C.24:End

