## CMP.8 - Construct an Approximate Computation with Controlled Error

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.8:1 - Problem frame

**Use this when** computing the requested answer without approximation is unavailable or too expensive, and a cheaper computation can retain enough information for the receiving task. You need to construct that computation, determine what it loses, and control the loss through a parameter or a stopping rule.

This occurs in discrete optimization, compressed computation, function evaluation and numerical solution. Rounding item values to shorten a dynamic program and discretizing a continuous equation are different instances. The shared difficulty is obtaining a useful finite answer with a warranted relation to the original computational question.

The result is an algorithm, its approximation controls, and an answer accompanied by the error, bound or settled distinction it actually supports. The reader needs to follow the original problem and its comparisons; calculus is required only for a construction that uses it.

Use an existing adequate algorithm directly when no new approximation choice is needed. A faster procedure that preserves every requested answer may need only a representation or scheduling change. Choosing an approximate description of the subject itself belongs to modeling; this method starts from the computational question that description supplies. CMP.5 develops relaxation and recovery; the present method develops adjustable loss, finite arithmetic and stopping, including constructions that use no relaxation.

### CMP.8:2 - Problem

How can a finite computation be made affordable by discarding or approximating information while retaining the answer quality needed next?

A small internal change can produce a large output change. A small residual can coexist with a poor answer. Two refinements can agree because both omit the same contribution. Refining everything can spend the budget without reducing the error that matters.

### CMP.8:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Cheap computation and useful distinctions | Coarsening reduces work but can merge alternatives whose difference decides the answer. |
| Mathematical convergence and finite return | Eventual convergence may supply neither an affordable stage nor a recognizable stopping condition. |
| Local error and composed error | A small loss at every operation can accumulate or be amplified downstream. |
| Objective quality and admissibility | An excellent approximate objective value can accompany an infeasible returned object. |
| Precision and conditioning | More accurate arithmetic helps only the errors it controls. |
| Strong guarantees and obtaining cost | A computable conservative bound can be more useful than an inaccessible sharp one. |

### CMP.8:4 - Solution

**State the needed distinction → construct the cheaper computation → bound the lost contribution → include arithmetic and recovery → refine the limiting part → return the qualified answer.**

#### CMP.8:4.1 - Choose what approximation means for this answer

State the original input, admissible answers and receiving use. Select the comparison that use needs: absolute error in a value, relative error away from zero, distance between objects, an optimization ratio, or agreement on a named finite observation. An approximate optimum usually still needs an admissible witness.

For a threshold decision, an enclosure entirely on one side can settle the question even when it is wide. If the enclosure crosses the threshold, return the unresolved decision or refine it. Equality may require another method; do not promise that arbitrary refinement will decide every equality case.

Separate the computational target from any claim about a modeled subject. A result close to the solution of the supplied equations does not by itself establish that those equations answer the physical or organizational question. Preserve the subject interpretation through C.29 and the applicable modeling method.

#### CMP.8:4.2 - Construct a family of cheaper procedures

Choose what to simplify and provide the operations that obtain the simplified answer. Possibilities include rounding values to reduce the number of states, truncating a series with a bounded tail, evaluating on a finite grid, retaining a compressed summary, or stopping an iteration once a sufficient bound is reached.

Let a parameter control the discarded information. It can be a rounding interval, polynomial degree, mesh size, retained rank, iteration count or arithmetic precision. Describe how changing it alters both the algorithm and the information retained. One parameter need not control every source of error.

If the construction changes the feasible set, provide a recovery procedure and its feasibility argument. If it changes only the objective used to select an answer, establish how that selection compares under the original objective. CMP.2 and CMP.3 can construct and schedule the resulting subproblems.

Try the simplest family that can meet the receiving requirement. A parameterized approximation scheme is unnecessary when one cheap direct calculation or an already available bound settles the question.

#### CMP.8:4.3 - Carry error through the operations actually used

Relate the computed intermediate object to the original target. MATH.20 supplies comparison arguments; MATH.21 supplies approximation and convergence. The present task must make their sufficient stage obtainable.

For example, if an intermediate approximation has distance at most e from its target and the next operation G obeys `d(G(u),G(v))≤L*d(u,v)` on the relevant inputs, this contribution to final error is at most L\*e. Add another error term only when it measures a comparable discrepancy and an argument, such as a triangle inequality, permits that addition. A probability of failure and a numerical error are different quantities.

For an optimization construction, compare the original objective of the recovered candidate with the original optimum. Follow every inequality in its proper direction. Rounding values can bound objective loss while leaving constraints unchanged; rounding constraint coefficients needs a separate admissibility argument.

When several approximations are composed, carry their bounds through the actual downstream operations. Allocate finer resolution where it changes the final bound most usefully. An unbounded sensitivity or a lost discontinuous distinction can require another formulation rather than further use of the same family.

#### CMP.8:4.4 - Include finite arithmetic and the sensitivity of the question

An algorithm implemented with finite representations performs approximations beyond those in its ideal construction. Identify consequential rounding, overflow, underflow, cancellation and approximate comparisons. Use integer or rational operations, higher precision, a stable reformulation or directed bounds where they improve the required answer affordably.

**Conditioning** describes how the mathematical answer responds to changes in the problem data. **Forward error** compares the returned value with the requested answer. **Backward error** asks how much the data would need to change to make the returned value an answer to the changed problem. Fix the permitted data changes and the measure of their size; those choices determine the claim.

A small backward error supports a small forward error only with suitable sensitivity control. A stable calculation cannot recover a distinction already absent from uncertain input data. Conversely, a well-conditioned question can be computed poorly by an unstable expression; :5.2 demonstrates a local repair.

Use a cheap bound or estimate of sensitivity when a stronger computation would not change the decision. When even the error bound is computed approximately, preserve the direction needed for its use.

#### CMP.8:4.5 - Derive refinement and stopping from the receiving requirement

Choose a stage from an a priori bound or use an observable enclosure with a justification that refinement reduces it. Include the work and storage needed to reach that stage. A bound polynomial in a numeric magnitude can still be exponential in that magnitude's encoded length.

Identify what currently limits the answer: approximation loss, arithmetic, insufficiently known input, or an unresolved subject assumption. Refine the responsible part. Comparing two resolutions can reveal failure or help estimate a rate, but their agreement alone is not a bound on the unresolved remainder.

Stop when the supported result is sufficient or when further refinement is not worth its expected effect. C.11.DUA helps compare additional computation with acting under the remaining uncertainty. Return a conditional or partial answer when that is what the available construction supports.

#### CMP.8:4.6 - Use the result and revise the affected construction

Return the value or witness together with the approximation meaning needed by its recipient. Distinguish a proved error bound, an empirically estimated error and an unbounded heuristic approximation.

A changed tolerance can require a different stage. A changed requested property can invalidate the error measure. A changed arithmetic format can invalidate an implementation argument while preserving the mathematical scheme. Reopen that part, retaining the constructions and comparisons that still hold.

### CMP.8:5 - Archetypal Grounding

#### CMP.8:5.1 - Round profits to construct a shorter discrete computation

Choose a subset of items within capacity W to maximize total profit. After removing items individually too heavy, suppose there are n items with positive integer weights and nonnegative integer profits `p_i`. If no positive profit remains, the empty subset is optimal. Otherwise let `P=max p_i`; at least that one item is feasible, so `P≤OPT`.

For `0<ε<1`, set `K=ε*P/n` and scaled profits `q_i=floor(p_i/K)`. Keep weights and capacity unchanged. Construct a dynamic program `D(j,q)` returning the minimum weight of a subset of the first j items with total scaled profit q:

```text
D(0,0) = 0; D(0,q) = infinity for q > 0
D(j,q) = min(D(j-1,q), w_j + D(j-1,q-q_j))
```

An out-of-range index is infeasible. Retain enough choices to recover a subset, and select the largest q with `D(n,q)≤W`. Including zero, there are at most `n*floor(n/ε)+1` scaled-profit positions. The straightforward table therefore takes `O(n³/ε)` arithmetic operations; weight arithmetic and witness storage have their own costs. Compute the rounding reliably when ε is supplied as a finite rational value.

Let A be the returned subset and O an original optimum. Because A maximizes the scaled profit among the same feasible subsets,

`p(A) ≥ K*q(A) ≥ K*q(O) > p(O)-n*K ≥ (1-ε)*OPT`.

The strict middle inequality follows from losing less than K on each of at most n selected items. Thus the returned object remains feasible and its loss is controlled, without knowing OPT in advance.

For A=(weight 5, profit 12), B=(3,7), C=(2,6), capacity 5 and `ε=1/2`, K=2 and scaled profits are 6,3,3. A and {B,C} tie under the scaled objective; a rule retaining A returns profit 12 although the optimum is 13. The approximation claim permits this. With `ε=1/4`, K=1 and the scaled objective distinguishes profit 13 from 12, returning {B,C}.

If the requested result changes to every optimal subset, the former error guarantee is insufficient. K=1 restores the original integer objective and lets this table obtain the optimal value, but can restore the large table the approximation was designed to avoid. Enumerating every optimum also requires reconstruction of every feasible subset attaining that value, including alternatives discarded by the minimum-weight entry. For example, with capacity 2 and two items of weights 1 and 2, each with profit 5, either singleton is optimal, although the minimum-weight entry retains only the first. The number of optimal subsets, and hence enumeration output, can be exponential. CMP.4 offers search with bounds; the cost and output requirement decide the choice.

#### CMP.8:5.2 - Repair an unstable evaluation without changing its target

Compute `f(x)=sqrt(1+x)-1` for a small positive x. Under binary64 round-to-nearest arithmetic, take `x=10^-16`. The addition can round `1+x` to 1, so the direct expression returns zero. The positive mathematical answer is about `5*10^-17`.

Rationalizing gives the same real-valued function:

`f(x)=x/(sqrt(1+x)+1)`.

Even when the computed square root is 1, this expression returns approximately `5*10^-17`, preserving the small contribution through the numerator. Near positive zero, the relative condition number is `(sqrt(1+x)+1)/(2*sqrt(1+x))`, which tends to 1. The failure of the direct expression therefore comes from its evaluation, not a large relative sensitivity to x.

This repair assumes the receiving requirement concerns f(x). If it instead asks for an accurate derivative obtained by subtracting nearby rounded function values, that is a new computation. The value repair alone supplies no error bound for that differentiation.

### CMP.8:6 - Bias-Annotation

Numerical language can conceal discrete approximation. The subset construction keeps feasible objects while coarsening selection values; the function construction changes arithmetic while preserving the real function.

### CMP.8:7 - Conformance Checklist

- The receiving answer and approximation comparison are stated, including feasibility or a required witness.
- A finite procedure obtains each selected stage; its loss is related to the original computational target.
- Composed error follows the operations and comparisons actually used.
- Consequential arithmetic error is distinguished from sensitivity to input and from subject-model discrepancy.
- The stopping or refinement rule has an appropriate warrant and affordable execution.
- The returned qualification distinguishes a bound, an estimate and an unbounded heuristic.

### CMP.8:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Treat a good objective value as an admissible answer | Rounded constraints can admit an invalid object. | Preserve constraints or construct and justify recovery. |
| Stop because adjacent refinements agree | Both can omit the same contribution. | Bound the unresolved tail or use a justified enclosure. |
| Increase precision for every failure | Input uncertainty or subject-model error can dominate. | Identify the limiting contribution first. |
| Use a relative error at a zero target | The ratio is undefined or unstable. | Select an absolute or otherwise meaningful comparison. |
| Transfer an approximation guarantee to a changed output | Near-optimal value need not identify all optima or preserve derivatives. | Reconstruct the comparison for the new requested result. |

### CMP.8:9 - Consequences

Approximation becomes a controllable part of algorithm design. The reader can trade computation against a stated loss, distinguish a local implementation repair from a changed problem, and return a useful answer before exhausting every possible refinement.

Some requested distinctions remain too costly or are unsupported by the input. The construction exposes that limit and the specific stronger operation or premise needed to cross it.

### CMP.8:10 - Architectural Rationale

An adjustable approximation joins a mathematical comparison to an effective algorithm. Convergence alone supplies no running procedure; a fast procedure alone supplies no relation to the desired answer. Keeping obtaining, loss, representation and use together makes each approximation step inspectable and replaceable.

Feasibility, accuracy and the receiver's decision are separate obligations because one can survive while another fails. The same distinction permits composition with relaxation, iterative updates, probabilistic estimation and subject modeling without imposing one error measure on all of them.

### CMP.8:11 - SoTA-Echoing

How should an approximation become an affordable algorithm with a selected error? **Adopt** the scaling-and-bound construction illustrated in [MIT's advanced algorithms notes on approximation schemes](https://courses.csail.mit.edu/6.854/21/Notes/n20-approx.html): connect rounding loss to the original objective and to the size of the resulting dynamic program. Sections :4.2–4.5 and :5.1 make those connections explicit. A direct unrounded computation is preferable when its state range is already affordable; the scaled construction deliberately accepts a weaker answer in return for a range controlled by ε.

The simple table is not the strongest known knapsack complexity result. [Chen, Lian, Mao and Zhang, version 3](https://arxiv.org/html/2308.07821v3), combine proximity and approximate profit-function composition to obtain a substantially stronger bound. **Adapt** the comparison lesson: retain the transparent table for a small construction or a suitable workload, but reconsider its representation and composition when its `n³/ε` cost becomes limiting. The stronger asymptotic result does not establish an implementation advantage for every small input. A competing scheme meeting the same output requirement at lower total application effort reopens that choice.

For the numerical branch, **adopt** Higham's separation of [conditioning](https://nhigham.com/2020/03/19/what-is-a-condition-number/) and [backward error](https://nhigham.com/2020/03/25/what-is-backward-error/) in :4.4. Compared with increasing arithmetic precision without locating the error, a local stable reformulation can retain the answer with less work; :5.2 derives one such case. Backward error is useful only for the permitted perturbations and with the sensitivity needed by the output. A changed input uncertainty, output operation or arithmetic implementation reopens this numerical choice. These arguments do not rank the adequacy of the subject model.

### CMP.8:12 - Relations

- **MATH.20 and MATH.21:** supply bounds, convergence and sufficient finite observations; this method supplies the executable approximation and its cost.
- **CMP.3:** constructs shared computation and storage for finite stages; **CMP.5** supplies relaxation and recovery; **CMP.6** supplies iterative updates.
- **C.29.2:** fixes the computational answer, representation and resource conditions.
- **C.29 and MMP.9:** preserve the separate subject correspondence and model-reduction question when this algorithm computes a model's consequence.
- **C.11.DUA:** compares the value of further refinement with its cost and remaining uncertainty.

### CMP.8:End
