## CMP.6 - Derive an Iterative Computational Update from Local Information

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.6:1 - Problem frame

**Use this when** a desired result is hard to construct directly, but the current candidate reveals a computable improvement: a beneficial local replacement, a derivative, a violated condition or feedback about a proposed change. You need to turn that information into an update rule and determine what repeated updates can establish.

This is an algorithmic design problem. It occurs in discrete local search, iterative equation solving, optimization and learning procedures. The input need not be numerical: swapping two choices or changing one symbol can be the available operation. The difficulty is connecting an accessible local signal to a useful change of the whole candidate.

The gain is an executable update, an appropriate step or acceptance rule, and a stopping or progress account suited to the requested result. The reader needs to follow the candidate's admissible changes and comparisons. Differentiation is a prerequisite only for the derivative-based branch; MATH.10 supplies the corresponding mathematical variation.

Use a direct construction when it already gives the required result affordably. An existing iterative method can also be used directly when its hypotheses fit. This pattern is needed when the update or its justification must be constructed or changed.

### CMP.6:2 - Problem

How can local information generate an admissible sequence of computational changes with a justified improvement or termination claim, without confusing local progress, convergence and the original objective?

A direction that improves an infinitesimal model may fail at a finite step. A locally unchangeable candidate may still be globally poor. An indefinitely improving sequence may never return the finite answer its recipient needs.

### CMP.6:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Cheap information and useful direction | A local signal is accessible but can omit interactions determining the effect of a change. |
| Large progress and model validity | A large step may save iterations or leave the region where its prediction applies. |
| Feasibility and improvement | An improving unconstrained move can violate the original conditions. |
| Local and global conclusions | A local stopping test needs additional structure to establish a global optimum. |
| Iteration count and work per iteration | A stronger update may require more information or computation. |
| Computed and receiving criteria | Decreasing a surrogate or training loss can leave the intended use unchanged or worse. |

### CMP.6:4 - Solution

**Choose the comparison → construct the available changes → derive a useful update → control its extent → establish progress → return the result at its supported scope.**

#### CMP.6:4.1 - State the candidate, criterion and wanted conclusion

Describe the current candidate `x`, its admissible set and the result wanted. A criterion `J(x)` can measure an objective, a residual or a potential used to establish progress. State which it is. A potential that decreases helps analyze the algorithm; its relation to the recipient's requested answer still needs to be established.

Separate possible conclusions: one improved candidate, no improving change in a specified neighborhood, a point meeting a residual tolerance, a global optimum, or a sequence converging under stated conditions. Select the useful conclusion now rather than automatically pursuing the strongest one.

When the iteration serves a model or learner, retain its target through C.29.2 and the relevant modeling or learning method. Optimization error, error in the subject model and performance on later cases are different questions.

#### CMP.6:4.2 - Construct local changes and their obtainable consequences

Specify what may change at one step. Examples include flipping one binary choice, exchanging two assignments, updating a coordinate, adding a vector direction or replacing a violated part of a construction. MATH.10 supplies the comparison under admissible variation; the present task is to obtain a useful change by a finite computation.

Determine what information is available about a proposed change:

- a directly computed difference in `J`;
- a local approximation, such as a derivative or a small model of the objective;
- a response or estimate obtained from samples or feedback.

Choose a procedure that uses this information. A discrete local search can examine neighbor changes and select one with positive gain. A smooth minimization can use a negative gradient. A coordinate method can solve a smaller update problem while holding other coordinates fixed. A residual correction needs a relation showing how that correction changes the residual or another progress measure.

If obtaining the direction calls another hard problem, include its algorithm and cost or accept an approximate direction with an appropriate result condition. Writing an argmin expression identifies the desired update; it does not automatically supply an algorithm for obtaining it.

#### CMP.6:4.3 - Make the finite update admissible and useful

For discrete replacements, compute the whole finite difference when it is affordable. Apply only changes that retain the required constraints, or pair the change with a specified repair whose effect is included in the comparison.

For a direction `d`, construct `x'=x+η*d` with step size `η`. The local information must support that finite change. A known upper model can determine a suitable step; otherwise a trial-and-reduction rule can search for a step whose observed effect supports acceptance. Include every trial evaluation in the cost.

For example, suppose a differentiable minimizing objective satisfies

`J(x+s)≤J(x)+grad J(x)·s+(L/2)*||s||²`

on the relevant region, with known `L>0`. Choosing `s=-grad J(x)/L` gives

`J(x+s)≤J(x)-||grad J(x)||²/(2L)`.

This derives a finite descent step from a bound on the local model's error. When that bound is unavailable, an adaptive step rule needs its own termination or acceptance conditions. One unsuccessful trial can justify reducing or changing the step; it does not establish that the direction never helps.

For constrained problems, use an admissible parameterization, projection or other constraint-preserving update. Reestablish the progress account for that update. Simply clipping a coordinate can change the original unconstrained argument.

With noisy feedback, first choose what the next action must establish. A comparison of two fixed candidates can support accepting a particular change; a noisy direction can instead support progress in expectation over a sequence. These require different constructions. Repeating a measurement or taking a larger sample is useful only when the additional information changes the step or its warranted use. A deterministic monotone-descent statement cannot be inferred from a noisy sign alone.

##### CMP.6:4.3.1 - Decide a proposed change from uncertain comparisons

For minimization, fix the current candidate x and one admissible proposal y while collecting evidence about `Delta=J(y)-J(x)`. Construct observations whose mean is that difference. For example, if `J(x)=E[l(x,Z)]` and both candidates can be evaluated on a fresh case Z, use `Y=l(y,Z)-l(x,Z)`. This paired difference retains the same target; its variance can differ from that of two independently estimated means. An observation of only the chosen action's consequence does not supply the unchosen value: obtain a compatible observation or estimation procedure before using this construction. MMP.7 supplies a missing account of the observation law.

Use CMP.9 to obtain an interval `[a_n,b_n]` for Delta with the error guarantee needed by the decision. For a fixed sample count, use its fixed-count construction. For repeated inspection, use its simultaneous intervals or another bound valid at the chosen stopping time. Known bounds on Y, independence and a stable target are conditions of that particular construction, not conclusions obtained from the sample itself.

Choose a useful decrease threshold tau >= 0 before inspecting the comparison. Accept y when `b_n < -tau`; on the interval's coverage event, this establishes `J(y)<J(x)-tau`. If `a_n >= -tau`, this comparison rules out a decrease greater than tau. Otherwise it is unresolved: obtain further information when worthwhile, try another proposal, or retain x with that unresolved comparison. A time limit supplies a finite return without pretending that an inconclusive test rejected the proposal.

Repeated adaptation needs error control across comparisons as well as within each comparison. Number proposed comparisons j=1,2,..., assign failure budgets `delta_j=delta/(j*(j+1))`, and let CMP.9 construct a simultaneous interval using delta_j for each. Choose that comparison's candidates from the earlier history, then collect fresh observations satisfying its stated law conditional on that history. The conditional failure bound is at most delta_j; summing these bounds gives probability at least `1-delta` that all comparisons used in the adaptive sequence are covered. Reusing observations to select the proposal and then treating them as fresh comparison evidence needs a different valid argument.

On this joint event, every accepted move decreases the same J. A finite candidate set cannot revisit a candidate through such moves. This does not guarantee that each noisy comparison resolves in finite time, especially at equality. A tau-local conclusion additionally needs every neighbor's comparison to rule out a decrease greater than tau at the returned candidate, or a bound covering the remaining neighbors. Without that coverage, return an improved candidate and the actual unresolved alternatives. A changed objective, admissible set or feedback law reopens the affected comparisons.

##### CMP.6:4.3.2 - Construct progress from a noisy direction

When checking each move costs too much, a stochastic update can trade that per-move claim for an expected result. Derive the trade-off from the information actually supplied. Consider an unconstrained differentiable J with the upper model above and a lower bound `J_low`. Let H_t denote all information available before drawing feedback at iteration t, including x_t. Suppose an obtainable gradient estimate g_t satisfies

`E[g_t | H_t]=grad J(x_t)` and `E[||g_t-grad J(x_t)||^2 | H_t] <= v`.

The first condition concerns the current candidate and its history; an estimate unbiased only before adaptive selection is insufficient. Derive the conditions from the feedback mechanism or use a justified supplier. For example, uniform independent sampling of component gradients from a fixed finite average has the required mean. For an expected loss, interchanging differentiation and expectation needs its own conditions. An empirical variance is not automatically a valid bound v.

Choose a fixed step `0<eta<=1/L` and compute `x_(t+1)=x_t-eta*g_t`. Substituting this step into the upper model and taking conditional expectations gives

`E[J(x_(t+1)) | H_t] <= J(x_t) - eta*||grad J(x_t)||^2 + (L*eta^2/2)*E[||g_t||^2 | H_t]`

`<= J(x_t) - (eta/2)*||grad J(x_t)||^2 + (L*eta^2/2)*v`.

Here `E[||g_t||^2 | H_t] <= ||grad J(x_t)||^2+v`; the zero conditional mean of the error removes its cross term. Thus noise adds a cost to the deterministic decrease, rather than merely changing its wording. A realized update can increase J, and the displayed bound need not certify expected decrease close to a stationary point.

For T such updates, sum the inequalities and use the lower bound. With a known `D >= J(x_0)-J_low`, the result is

`(1/T)*sum_(t=0)^(T-1) E[||grad J(x_t)||^2] <= 2*D/(eta*T) + L*eta*v`.

This is a finite stationarity result, not a global-optimum or distance-error guarantee. For a positive epsilon, to request an expected squared gradient norm at most epsilon^2, choose `eta<=1/L` and, when v>0, `eta<=epsilon^2/(2*L*v)`; choose an integer `T>=max(1,4*D/(eta*epsilon^2))`. Return x_R for an index R chosen uniformly from 0,...,T-1 independently of the update randomness. Its expected squared gradient norm equals the average bounded above. CMP.9's reservoir construction can retain one such iterate without storing the whole trajectory. Selecting the last iterate or the smallest noisy observation does not inherit this particular bound.

If b conditionally independent estimates at the same current candidate each have the stated conditional mean and error second moment at most sigma^2, their average has `v<=sigma^2/b`. Compare a smaller step and more iterations with a larger batch and its extra work; count all Tb gradient observations, not only updates. A batch chosen adaptively using its own observed errors needs an argument preserving the assumed mean and second-moment bound. Known L, D and v give the displayed budget; if they are unavailable, this formula does not invent them. Use a qualified estimate for an exploratory run, a supported bound, or the comparison route above according to the receiving claim.

A constraint-preserving parameterization can make this construction applicable to its unconstrained parameters, with J and L expressed there. Arbitrary clipping or projection does not preserve the displayed derivation; use the corresponding constrained progress result. If feedback has a conditional bias, retain its extra inner-product term in the first inequality or repair the estimator. More samples of the same biased signal do not restore the omitted zero-mean condition.

#### CMP.6:4.4 - Establish what repeated updates imply

Select a progress argument appropriate to the state space and update:

| Available structure | What can be established | What remains to be supplied |
| --- | --- | --- |
| A finite candidate set and strict improvement at every accepted change | No candidate repeats; the procedure reaches a state with no accepted improving change. | A feasible way to find or rule out such changes, and a useful bound on the amount of work. |
| A decreasing nonnegative integer potential | At most its initial value many decreases of at least one. | The potential's encoded magnitude can be large, and one iteration may be expensive. |
| A contraction or another quantitative convergence relation | A finite error bound after a chosen number of updates. | A way to compute the required update and connect that error to the requested result. |
| A descent estimate with a bounded-below objective | Bounds on accumulated improvement and, under appropriate assumptions, stationarity measures. | Convergence to one point or global optimality requires its own additional conditions. |
| A conditional mean and second-moment bound for a noisy direction, with the smooth upper model | The finite expected stationarity bound in :4.3.2. | A warranted feedback law, admissible updates, step and sampling cost, and the stated output selection. |

Use MATH.20 for the bound and MATH.21 for the convergence construction when needed. If each step improves but there is no useful stopping guarantee, return that limited procedure or change the method. Equal-value moves need their own cycle handling; strict-improvement reasoning does not cover them.

#### CMP.6:4.5 - Choose a stopping test that supports the receiving answer

Derive the test from the wanted conclusion. Exhausting a discrete neighborhood establishes local optimality for that neighborhood. A residual threshold answers a residual question; a condition or error bound is needed to convert it into distance from a solution. Small successive changes can result from a tiny step even while the candidate remains poor.

For a constrained optimum, the full gradient need not vanish. Use the absence of a feasible improving variation, a suitable projected update or the relevant constrained condition. Report that condition at the scope it establishes.

For noisy comparisons, distinguish a resolved interval test from an exhausted sampling budget. For stochastic directions, the fixed budget in :4.3.2 supports its expected result for the selected output, not an observed certificate for a particular last iterate. An additional assessment can supply a different result when its cost is justified; keep the assessment conditions separate from the update samples used to select that result.

When time runs out, return the best admissible candidate or current approximation together with any supported bound. A tolerance or resource limit belongs to the use that needs the result.

#### CMP.6:4.6 - Revisit the source of a failed improvement

When the step fails, locate whether the direction, extent, feasibility repair, feedback or assumed relation to the objective changed. Revise that part. If local moves repeatedly stop at unsatisfactory candidates, enlarge or change the neighborhood, restart from another candidate, use CMP.4 to explore alternatives or obtain a bound through CMP.5.

Compare alternatives by the quality and cost relevant to the receiving use, using the existing characterization and improvement methods. Faster iteration is valuable only in relation to the result it obtains.

### CMP.6:5 - Archetypal Grounding

#### CMP.6:5.1 - Construct a discrete local-improvement algorithm

Partition the vertices of an undirected graph into two groups to maximize the total nonnegative weight of edges crossing between groups. Start with any partition. At a vertex v, let `I(v)` be the weight of its edges to vertices in the same group and `C(v)` the weight to vertices in the other group. Flipping v changes the cut value by `I(v)-C(v)`.

Compute these differences and flip a vertex whenever its difference is positive. Each flip is an admissible partition change and strictly increases the criterion. Because there are finitely many partitions, the algorithm eventually reaches one with `I(v)≤C(v)` at every vertex.

At this stopping state, `C(v)` is at least half the incident weight at v. Summing over vertices counts every cut edge twice, so the cut value is at least half the total graph weight. The total graph weight bounds any cut, giving a factor-two bound relative to the maximum cut. This is a property derived from the chosen neighborhood and nonnegative weights, rather than an assertion that every local optimum is globally optimal.

For a four-cycle with unit weights, start with all vertices in one group. Flipping vertex 1 produces a cut of value 2. Flipping the opposite vertex 3 produces value 4, which is optimal because all four edges cross. Only incident edges need updating after each flip. Finite termination alone does not make the general algorithm polynomial in the encoded input size; the number and cost of flips require a further account.

**Changed condition:** allow negative edge weights. Take four vertices with weights -3 on edges 1-2 and 3-4, and weight 1 on the four edges between those pairs. With all vertices in one group, each single flip changes the cut by -1, so the algorithm stops at value 0. Moving the pair {1,2} together to the other group produces value 4. Finite termination survives, but the former factor-two guarantee fails. A two-vertex neighborhood opens an improving move; its cost and eventual quality need their own comparison.

#### CMP.6:5.2 - Derive a step and change its constrained stopping condition

Minimize `J(x)=(x-3)²` over real x. Its derivative is `2(x-3)`. The update `x'=x-2η(x-3)` multiplies the error `x-3` by `1-2η`. Thus `0<η<1` contracts its magnitude; with `η=1`, the error oscillates without decreasing.

Choose `η=1/4`. From `x=0`, the iterates are `1.5, 2.25, 2.625, ...`; the objective values are `9/4, 9/16, 9/64, ...`. After k steps from the initial point, the distance to 3 is `3/2^k`. A requested distance at most epsilon therefore has a directly computable iteration bound. This example establishes the update through its algebra rather than through a generic instruction to repeat until the values seem stable.

**Changed constraint:** require `0≤x≤1`. Projection of the same proposed first step onto this interval gives `x=1`. Further projected steps remain at 1. The derivative there is -4, so a full-gradient-zero stopping test would never recognize the constrained optimum. Every feasible point in the interval has `J(x)≥4=J(1)`, establishing the result. The changed feasible set requires a changed stopping argument, even though a related update can still be used.

#### CMP.6:5.3 - Change from exact information to noisy feedback

Keep `J(x)=(x-3)^2`, but replace the exact derivative by `g(x)=2*(x-3)+zeta`, where each fresh zeta independently equals -2 or 2 with equal probability. Its conditional mean is the derivative and its error variance is 4. With `eta=1/4`, the error `e=x-3` becomes `e'=e/2-zeta/4`, so

`E[e'^2 | e] = e^2/4+1/4`.

At e=0, either outcome increases J from zero to 1/4. A claim that every accepted stochastic step improves J would therefore be false. Repetition obeys `E[e_T^2]=4^(-T)*e_0^2+(1/3)*(1-4^(-T))`: the noise contribution remains near 1/3. More iterations with the same step cannot give an arbitrarily small mean squared error.

Average b fresh gradient estimates at the current x before each update. The noise term becomes `1/(4*b)`, giving

`E[e_T^2]=4^(-T)*e_0^2+(1/(3*b))*(1-4^(-T))`.

For x_0=0, the receiving requirement `E[e_T^2]<=0.1` is met by b=4 and T=5: the bound is `9/1024+(1/12)*(1023/1024)`, about 0.092041. This uses 20 gradient observations. Unlike the general stationarity result, this quadratic recurrence directly supports the last iterate's squared-error claim; its special structure supplies that stronger result. A larger batch, a smaller step or another justified construction can compete on total work.

**Change the feedback condition.** Suppose the signal becomes `g(x)=2*(x-3)+1+zeta`. Its mean is the derivative plus 1. The same update now centers on x=2.5, not x=3. Even unlimited averaging removes only zeta's variation, leaving squared error 1/4 at that center. If the offset 1 is known from a valid calibration, subtract it before updating and recover the earlier argument. If it is unknown, obtain its relation to the target or return the unresolved bias; choosing a smaller sampling error does not repair the target.

The comparison route supports a different receiving choice. Suppose a current candidate and one proposal can be compared through fresh bounded loss differences in [-1,1]. A valid simultaneous interval [-0.18,-0.04] permits the proposal for tau=0.02; [-0.05,0.03] leaves that comparison unresolved; [-0.01,0.08] rules out a decrease greater than 0.02. If further proposals are selected from these results, apply the per-comparison budgets in :4.3.1. A fixed-count interval repeatedly inspected until it favors a proposal does not supply the same claim.

### CMP.6:6 - Bias-Annotation

A familiar update formula can displace the question of which local information is actually available. A gradient-based method, for example, needs a computable gradient or a justified estimate; a symbolic derivative on paper can still leave costly evaluation.

Visible improvement can also be mistaken for sufficient progress. Retain the relation between the improved criterion and the requested result, including the distinction between a finite-state termination argument and an affordable run.

### CMP.6:7 - Conformance Checklist

- The candidate, admissible changes, comparison criterion and requested conclusion are stated.
- The local information and the operation obtaining an update are available under the stated inputs.
- The finite step or replacement has the required feasibility and improvement account.
- Repetition has the claimed termination, convergence or limited progress conditions.
- The stopping test supports the wanted answer rather than merely detecting small changes.
- The cost comparison includes direction construction, trials, state updates and consequential arithmetic or information costs.
- A changed condition is followed through the update and its result claim before reuse.

### CMP.6:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Turn an improving direction into an arbitrary finite step | The quadratic example can oscillate or diverge. Derive step extent or supply an adaptive rule with stated conditions. |
| Stop solely because successive values barely change | A tiny step can hide a large unresolved error. Connect the stopping quantity to the result by a bound. |
| Demand zero full gradient at a constrained optimum | The interval example is optimal with a nonzero derivative. Use feasible variations or the appropriate projected condition. |
| Infer global optimality from a local stop | The neighborhood may miss a better distant candidate. Derive a global comparison or retain the local conclusion. |
| Treat finite termination as a useful runtime bound | The finite state space or potential may be enormous. Account for encoded magnitude and work per step. |

### CMP.6:9 - Consequences

The designer obtains a rule that makes a next computational change from available information and can explain what repeated use achieves. The method connects discrete improvement, continuous optimization and feedback-driven updates through their progress arguments without identifying their different guarantees.

It can also reveal that the available local information is insufficient. A new neighborhood, stronger model, additional observation or different algorithm may be required. The explicit failure locus makes that revision smaller than replacing the entire computational formulation.

### CMP.6:10 - Architectural Rationale

Update construction, finite-step control and stopping belong together because each changes what the algorithm can return. MATH.10 derives conditions from variations and MATH.21 constructs objects through convergence. CMP.6 supplies the effective rule, its repeated execution and the finite answer required from it.

CMP.5 can furnish a bound or an easier update subproblem; CMP.4 explores alternative candidates. CMP.7 can use the update to construct a learner, while keeping optimization progress distinct from performance on further cases. These are complementary algorithmic methods.

### CMP.6:11 - SoTA-Echoing

[Williamson and Shmoys, *The Design of Approximation Algorithms*](https://designofapproxalgs.com/book.pdf), chapter 2 and later local-search constructions, derives global comparisons from specified local neighborhoods. Adopt that style of argument rather than equating local improvement with global success. The cut example makes the neighborhood and nonnegative-weight assumption explicit; a more powerful neighborhood can require more work per update.

[Bottou, Curtis and Nocedal, *Optimization Methods for Large-Scale Machine Learning*](https://leon.bottou.org/publications/pdf/tr-optml-2016.pdf) develops obtaining procedures, step control and the distinction among optimization and statistical errors. Adopt the error-bound-to-update construction and the accounting for inexact information. Its smooth and stochastic analyses have stated assumptions; they do not govern every discrete or learned update.

For the smooth branch, compare a preset step with the upper-model or trial-controlled construction in :4.3 using the same available objective and derivative operations. A known useful L makes the derived step inexpensive; without that information, trial control spends extra evaluations to avoid an unsupported finite step. The quadratic case exhibits a concrete failure of a preset value. Retain a fixed step when its bound already supports the required result; choose trial control when its information gain warrants those evaluations.

For noisy feedback, :4.3.1 composes CMP.9's intervals with a finite-change decision and an error budget across adaptive proposals. It is the appropriate alternative when the receiving work needs a warranted decision about each accepted change. Its sampling can be expensive or leave equality unresolved. In :4.3.2, **adapt** the conditional expected-decrease argument and finite stationarity bound of [Bottou, Curtis and Nocedal, sections 4.1 and 4.3](https://arxiv.org/pdf/1606.04838) to obtain an executable noisy-direction procedure and its budget. This established mathematical line trades per-step improvement for an expected finite-output result. Exact information remains the simpler choice when it is affordable. Larger batches, better estimators or variance-reduction methods deserve comparison when they improve the same requested result per total work. A changed conditional mean, variance bound, feasible region or output selection reopens the affected argument.

For a finite discrete neighborhood, direct gain calculation may be simpler than fitting a continuous model. The cut example derives both update and guarantee from those discrete gains. Revisit the chosen direction, acceptance or stopping rule when feedback, admissible moves or a required progress bound changes, or when another construction obtains the same required result at lower total cost.

### CMP.6:12 - Relations

- **C.29.2:** states the obtaining task, operations and resource conditions.
- **MATH.10:** constructs admissible variations; **MATH.20** supplies bounds; **MATH.21** supplies convergence and finite-approximation reasoning.
- **CMP.4 and CMP.5:** can provide alternative exploration, a relaxed update problem or a useful comparison bound.
- **CMP.7:** uses updates in a learning algorithm while retaining a separate account of further-case performance.
- **CMP.9:** constructs estimates and intervals for noisy comparisons, and a uniform retained iterate when the expected-output argument needs one; **MMP.7** supplies a missing observation law.
- **C.11.DUA and the general improvement methods:** select the value of additional computation, information or a more costly update.

### CMP.6:End
