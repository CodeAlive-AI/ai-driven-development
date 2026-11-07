## CAD.4 - Co-design and Realize the Whole Control Architecture

> **Type:** Method pattern
> **Status:** Stable

### CAD.4:1 - Problem frame

**Use this when** several control architectures appear feasible, or a change of model, hardware, rate or operating demand can invalidate an existing arrangement. Tuning each controller independently does not decide which complete arrangement should be built.

Start with the same required behavior and resource boundary for every candidate. The first useful result is a feasible whole configuration, its comparison with serious alternatives, and the conditions under which its implementation and later use remain justified.

For a fixed, qualified architecture requiring only a local parameter adjustment, use the relevant controller-design method directly and reopen the whole only if that adjustment changes a relied-on interface, resource or constraint.

### CAD.4:2 - Problem

A detailed planning model may improve prediction but miss its deadline. A faster tracker can use more computation or amplify measurement noise. A longer planning interval can save resources while increasing command mismatch. A design assembled from individually preferred choices may have no feasible joint setting.

The problem is to choose and realize a configuration whose control, model and resource assumptions can hold together.

### CAD.4:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Fidelity, horizon and execution time | More planning information can arrive too late to be useful. |
| Strong correction and implementation limits | A gain that shrinks error can increase input, noise sensitivity or computation. |
| Feasibility and performance | Staying within limits does not establish progress, optimality or adequate tracking. |
| Design model and running system | A proven nominal schedule may differ from actual latency, sharing and failure behavior. |

### CAD.4:4 - Solution

#### CAD.4:4.1 - Form complete candidates

Use C.39 to connect the required result to its supplying operations and C.32/SYSE.6 to retain whole alternatives. A candidate specifies the decomposition, model and its operating domain, exchanged command, timing and reset semantics, controller law, feasible command domain, planning continuation and implementation resources.

Keep architecture choices separate from tunable parameters without pretending that the separation is absolute. The number of layers, model order, kind of command, sampling periods, planning horizon and processor arrangement can change the problem being solved. Gains, weights and numeric tolerances tune a selected construction. Changing either group can reopen the other.

CAD.1–CAD.3 supply the positive construction, not merely a screening list. Existing qualified results can replace repeated design work. If the interface law changes, the old error bound is not a reusable result for that new law.

#### CAD.4:4.2 - Evaluate feasibility before ranking attractive scores

For each candidate, establish the connected error behavior, physical constraints and continuation under its own admitted conditions. Include initialization, transitions, planned modes and fallback behavior. A candidate with a missing load-bearing condition is unresolved, not numerically inferior.

Then evaluate the behavior the task actually values: tracking envelope, settling, progress, resource consumption, disturbance rejection or cost. Use the same demand and perturbation class across candidates. An average objective cannot compensate for violating a hard constraint.

Boundedness and convergence are distinct. For example, if the nominal law makes $z_k\to z_*$ and $v_k\to v_*$, the linear error equation has forcing $g_k=Hz_k+Gv_k+w_k$. With a contractive F, $g_k\to0$ implies $e_k\to0$: the contribution of any fixed finite past decays, and the remaining tail is bounded by its shrinking forcing divided by $1-q$. If $Hz_*+Gv_*\neq0$, even zero disturbance can leave a steady bias. A bounded command domain alone establishes neither nominal progress nor zero error.

When the performance claim requires optimality, robust stability or task completion beyond these arguments, supply the corresponding result for the actual connected model. Do not infer it from the presence of MPC, a Lyapunov function for one component, or an optimizer's successful return.

#### CAD.4:4.3 - Include execution in the design equations

Use MMP.22 to turn the mathematical operation into a workable computation. Identify the data needed when the operation starts, the work that can be prepared ahead, the result required at its deadline, and what must happen if it is unavailable.

A necessary timing comparison is

$$
C_{\mathrm{fast}}\leq T_{\mathrm{fast}},\qquad
C_{\mathrm{plan}}\leq T_{\mathrm{plan}},
$$

where C bounds execution under the selected implementation. These isolated inequalities are not sufficient on a shared processor: blocking, interference, communication and scheduling must fit the deadlines together. An operation count or mean runtime is not a worst-case execution bound.

If planning finishes one period after its observation, model that delay and the command that controls the intervening period. Preparing a future segment can make the delay harmless for a predetermined reference but not automatically for a newly observed obstacle. Increasing the processor speed changes the feasible architecture set.

Use the implementation to test unit conversions, numerical tolerances, update order, saturation and reset behavior. A numerical optimizer's constraint tolerance belongs in the margin analysis if it can consume physical clearance. Verify that the lower law actually executed is the law used in CAD.2.

If an online solver returns only a partial iterate, separate the time spent solving from the test that permits applying its output. A qualified acceptance rule may allow a feasible inexact result and otherwise keep an admissible prior command or plan. Include the cost of that test and the conditions for progress; a timeout says nothing about admissibility, and feasibility alone does not establish progress. The command-governor alternative in :11 is one developed construction, not a fallback rule for every optimizer.

#### CAD.4:4.4 - Search jointly, with bounded conclusions

A practical first search can enumerate a small number of architecture choices and, within each, solve or tune the continuous parameters. Recompute the error and command domain for every material change. Reject a setting whose necessary constraints fail; retain unresolved settings separately from feasible ones.

Compare feasible candidates through task-relevant trade-offs and costs. Do not collapse incompatible obligations into an invented scalar score. A Pareto comparison can expose choices where one candidate is faster but more resource intensive. If the search covered only a grid, selected controller class or local optimizer, state that reach; it does not prove global architectural optimality.

Investigate the active limitation. If actuator reserve fails, altering the reference interface may help more than enlarging the processor. If timing fails, a reduced model or shorter horizon may help more than increasing gain. If a reduced model loses an important mode, a larger controller budget may be unavoidable. This is the constructive feedback from the whole evaluation to CAD.1–CAD.3.

#### CAD.4:4.5 - Qualify the realization and its revision conditions

Separate mathematical consequence, model qualification and implementation observation. Simulation can reveal an omitted mode or a bad reset. Tests on the target execution arrangement can expose deadline misses. Physical experiments can challenge the model, disturbance envelope and actuator assumptions. None automatically establishes every other claim.

Before relying on the design, identify the operating conditions that support it and the observations that can invalidate them. Examples are a larger reference jump, changed disturbance envelope, delayed sensor, actuator derating, altered model order or shared computing load. Reopen the specific equation, inclusion or comparison using the changed premise.

Choose detection and fallback behavior for the actual failure mode. A reference hold is justified in the running model because it lies within the admitted command class; in another plant it may be unsafe or mission-defeating. For an unexplained timing overrun or model residual beyond the admitted W, stop claiming the old bound and use only a separately qualified response.

The resulting control architecture returns to SYSE.6 with its feasible domain, performance, resource needs and unresolved constraints. That system decision can change sensors, actuators, plant structure or requirements rather than forcing every problem into controller tuning.

### CAD.4:5 - Archetypal Grounding

#### CAD.4:5.1 - Compare rates at the same requested progression

For the discrete actuator example, assume a dedicated planner resource needs two fast ticks per result. The fast controller has a separate resource. Commands are prepared for their applicability interval; initialization supplies the first segment. This is a declared toy resource model, not measured processor performance.

At progression 0.025 per fast tick, a held reference changes by $\delta=N/40$. At progression 0.05 it changes by $\delta=N/20$. The sufficient error and input bounds are derived from CAD.2, with $a=1/2$.

| Command and demand | N | Error bound E | Input bound | Two-tick planning time fits? |
| --- | ---: | ---: | ---: | --- |
| Held, 0.025 per tick | 1 | 0.05 | 0.025 | No |
| Held, 0.025 per tick | 2 | 0.066667 | 0.033333 | Yes |
| Held, 0.025 per tick | 4 | 0.106667 | 0.053333 | Yes |
| Held, 0.05 per tick | 1 | 0.1 | 0.05 | No |
| Held, 0.05 per tick | 2 | 0.133333 | 0.066667 | Yes |
| Held, 0.05 per tick | 4 | 0.213333 | 0.106667 | Yes |
| Joined segment, increment at most 0.05 per tick | 4 | 0.1 | 0.05 | Yes |

At the original demand, two held-command arrangements pass this sufficient input test; their compute use and tracking behavior can be compared. At doubled demand, neither of the considered held arrangements that fits the planning time passes it. The N=4 case also has the direct violating first jump shown in CAD.3. For N=2, two successive positive changes of 0.1 from rest produce an input of 1/16 = 0.0625 at the second change, also above the limit.

The segment arrangement admits the higher demand under the stated sampled model and margins. It adds a clocked reference generator and continuity checks. It does not demonstrate that this arrangement dominates all possible controllers or that more than two layers would help.

#### CAD.4:5.2 - Carry the mathematical result into execution

The planner proposes a next endpoint and applicability time. The reference generator checks that the segment starts at the current reference, remains in $[-0.9,0.9]$, and advances by at most 0.05 per fast tick. The fast law uses that generated reference, not the endpoint held for four ticks. An unavailable segment leaves the reference unchanged; the initialization error must already satisfy the bound.

A hardware test that reveals a one-tick delay in actuation changes $x_{k+1}=x_k+u_k$ into a model with an input delay. The table is no longer sufficient evidence. Return to CAD.2 to derive the delayed dynamics and to CAD.3 for the resulting margins. Retain the comparison of command meanings and the source-independent arithmetic; do not retain the unqualified physical feasibility conclusion.

### CAD.4:6 - Bias-Annotation

A convenient cost model can favor the hardware already at hand. A small parameter search can make its winner look universal. State the tested choices and preserve alternatives whose decisive conditions remain unknown. The running case demonstrates an interface repair, not an empirical prevalence claim.

### CAD.4:7 - Conformance Checklist

- Complete candidates are compared under the same task and constraints.
- Connected feasibility and continuation are established before performance ranking.
- A convergence or optimality claim has its own applicable grounds.
- Execution, communication and scheduling assumptions fit the implemented arrangement.
- Search limits and unresolved candidates are visible.
- Changed-condition and fallback behavior return to the premise that actually changed.

### CAD.4:8 - Common Anti-Patterns and How to Avoid Them

Optimizing each layer and connecting the winners can destroy feasibility; compare complete settings. Choosing rates from “fast” and “slow” labels hides dynamics and execution costs; derive their effects. A predicted runtime is not a deadline guarantee. A fallback that was never part of the model does not inherit its bound.

### CAD.4:9 - Consequences

The choice can change model order, command representation, rates, controller parameters and hardware together. This broadens the search but can avoid tuning an infeasible arrangement. A declared bounded search yields a defensible local decision, not a universal optimum.

### CAD.4:10 - Architectural Rationale

Control behavior and execution are coupled: computation changes latency, latency changes error, and error changes admissible commands. The whole design must therefore be the unit of comparison. Keeping each intermediate result explicit lets an implementation change reopen only the dependent reasoning.

### CAD.4:11 - SoTA-Echoing

**What should change when a complete control arrangement misses its demand or resource limit?** The selected line compares coupled architecture and tuning choices, while retaining a qualified fixed loop with local command modification as a serious alternative. It adopts the joint-choice formulation in [Verhoek, Stamouli, Pappas and Matni, 2026 preprint, §§3–7](https://arxiv.org/html/2610.20900v1): model dimensions, sampling ratios, horizons and controller parameters affect the same feasibility problem. That construction fixes a two-layer LTI setting and specified delay and controller classes; efficient general optimization remains open. Sections :4.1–4.4 adapt the comparison to a bounded candidate search and require implementation timing rather than treating a computation-cost proxy as a deadline bound. The gain is avoiding incompatible local optima; the cost is a larger search and repeated qualification of coupled choices.

When the lower loop already has the required local performance, first compare changing its command admission or solver. [Garone and Kolmanovsky, §§3–4 and Algorithm 1](https://arxiv.org/html/2111.10234) develop command-governor logic permitting inexact optimization and a non-invariant inner admissible set, with stated feasibility and progress conditions. Adopt the separation between accepting a computed command and merely obtaining a solver output in :4.3; neither an arbitrary partial iterate nor an unqualified hold inherits that result. This can be preferable to buying faster computation or redesigning the tracker, but command progress and admissible-set computation remain costs to compare.

Switching among existing controllers is also a genuine architectural alternative. [Wang, Di Cairano and Sanfelice, 2024, §§III–V](https://www.merl.com/publications/docs/TR2024-091.pdf) combine mode-specific admissible sets with explicit switching and Lyapunov conditions. Adapt that comparison when a fast transient and a less oscillatory final approach favor different controllers; carry the guards and transitions into :4.2 and CAD.3:4.1. Separate stable modes alone do not supply the switched guarantee. Reopen the choice when task demand, computing interference or the cost of maintaining those mode conditions changes.

### CAD.4:12 - Relations

CAD.1, CAD.2 and CAD.3 supply candidate decomposition, connected dynamics and admissible commands. Their results are dependencies of the whole comparison, not mandatory fresh work for every application. C.39 supplies general Method construction; MMP.22 supplies the mathematical-to-practical transformation. SYSE.6 receives the control result within the system architecture decision. C.30.LCA tests the resulting view's coverage, not the control theorem.

CAD.5 supplies observation, internal-state and estimator alternatives with their error and execution conditions. Shared computation can change their observation age, so a different implementation can reopen that information result and the dependent CAD.3 margins.

### CAD.4:End
