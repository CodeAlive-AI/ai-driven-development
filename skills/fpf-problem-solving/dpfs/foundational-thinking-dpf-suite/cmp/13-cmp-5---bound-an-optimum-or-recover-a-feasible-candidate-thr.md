## CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.5:1 - Problem frame

**Use this when** an optimization problem is difficult to solve directly, but weakening some of its restrictions or costs gives a more accessible problem. Its solution may help construct a candidate for the original problem, or bound how much better the current candidate could become.

The situation occurs in combinatorial selection, scheduling, routing, program synthesis and continuous optimization. A relaxed solution can make an inaccessible search informative, but it may violate the original conditions. For example, fractional choices are useful for reasoning about an indivisible selection even though the fractions cannot be implemented as that selection.

The gain is a useful bound, a recovered admissible candidate, or both, together with a reason they apply to the original question. The reader needs feasible sets, an objective and inequalities. MATH.20 supplies further bound reasoning; a solver for the selected relaxed problem may be obtained as a separate contribution.

Use an available direct method when it already produces the needed result at acceptable cost. Approximation alone does not make a problem a relaxation: this method needs the correspondence and inequality that support its bound. A good heuristic can still be used without that bound, with its result stated accordingly.

### CMP.5:2 - Problem

How can solving an easier problem help obtain or assess an answer to the original one, without treating the easier problem's admissibility or optimum as the original result?

The designer must construct both directions of use: how original candidates are represented in the relaxed problem, and how the relaxed output yields a bound or a candidate that the original recipient can use.

### CMP.5:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Easy and informative relaxation | Removing many restrictions may simplify solution but leave a weak bound or hard recovery. |
| Relaxed value and admissible candidate | The easier optimum can be unobtainable under the original conditions. |
| Solver effort and useful improvement | Tightening a bound can cost more than exploring or using the current candidate. |
| Recovery and lost quality | Rounding or repair can restore feasibility while worsening the objective. |
| Mathematical and computed bounds | Approximate optimization and arithmetic can weaken or invalidate a claimed bound direction. |
| One criterion and several interests | A scalar optimization result answers its stated criterion; other objectives retain their own comparison. |

### CMP.5:4 - Solution

**State the original problem → construct the easier comparison → obtain its informative result → recover an admissible answer → bound the loss → choose the next use.**

#### CMP.5:4.1 - State what the original candidate must satisfy

Name the original feasible set `F`, objective `f`, and whether it is minimized or maximized. Include the conditions that make a candidate usable in the receiving activity. An abstract numerical optimum can leave implementation, uncertainty or other subject conditions outside this particular problem; keep that boundary visible through C.29 and MMP.10.

State what would change the present decision: a better candidate, an infeasibility conclusion, a bound on possible improvement, or an answer within a given tolerance. This selects how much work to spend on the relaxation and recovery.

If several criteria matter, use the existing characterization and Pareto methods to preserve their trade-offs. The scalar constructions below apply to the chosen optimization question. They do not replace that broader comparison with a model-specific score.

#### CMP.5:4.2 - Construct the relaxation and derive the bound direction

For minimization, give a relaxed feasible set `R`, objective `g`, and a way of representing each `x` in `F` by `i(x)` in `R`, such that `g(i(x))≤f(x)`. Where minima exist, this yields `min_R g≤min_F f`. For maximization, use the reversed objective inequality so that the relaxed optimum is an upper bound on the original optimum.

Common constructions include:

| Construction | Why the comparison can hold | Main design risk |
| --- | --- | --- |
| Drop a constraint or allow fractions instead of integral choices | Every original feasible point remains available with the same objective. | The relaxed optimum may be far from any original feasible candidate. |
| Make transitions or costs more permissive | Every original path remains represented at no greater cost in a minimizing problem. | The relaxed route may use operations forbidden in the original problem. |
| Replace a coupling constraint by a multiplier term | The signed term gives a bound on the objective for original feasible points, while the relaxed computation may separate into smaller problems. | A wrong sign or an unsupported minimizing step reverses or loses the bound. |

For the last construction, consider minimization with constraint `h(x)≤0`. For `λ≥0`, `f(x)+λ*h(x)≤f(x)` on original feasible points. Minimizing this expression over a larger, simpler set therefore supplies a lower bound if that minimum is obtained or bounded from below. The returned point can violate `h(x)≤0`; its usefulness as a bound does not make it an admissible answer.

Choose a relaxation by both its solving cost and its receiving use. A tighter mathematical description can be computationally worse, or make recovery harder. Existing portfolio and improvement methods can compare several candidate relaxations.

#### CMP.5:4.3 - Obtain a result with the strength its next use requires

Select an obtaining procedure for the relaxed problem. It may return an optimum, a candidate with a bound, a dual bound, or a heuristic estimate. Retain that distinction when using the result.

For minimization, a feasible relaxed point with value `P` gives an upper bound on the relaxed minimum. It does **not** by itself give a lower bound on the original minimum. To support such a lower bound, obtain the relaxed optimum or another justified lower bound `L`, for example from a feasible dual construction. MATH.20 supplies the bound argument; the relevant solver or proof supplies its computed value.

With an original feasible candidate of value `C`, the useful comparison is `L≤original optimum≤C`. A relaxed candidate's value `P` may lie on either side of the original optimum. Keep it separately when it guides recovery.

Check the computational bound direction when rounding, stopping tolerances or incomplete solving can change an exclusion or conclusion. A conservative weaker bound can be preferable to an expensive stronger one. C.11.DUA selects extra computation or assurance according to its possible effect.

#### CMP.5:4.4 - Construct an admissible original candidate

Give an effective recovery operation when a candidate is needed. Rounding, selecting a subset, scheduling fractional allocations, repairing violated conditions or searching near the relaxed answer can serve this role. Test the original conditions after recovery and explain why the operation preserves or restores them.

A generic instruction to “round the result” is insufficient. Rounding upward can violate a capacity limit, while rounding downward can leave coverage incomplete. Derive the direction and any subsequent repair from the constraints.

Track objective change through recovery. If every recovered candidate has cost at most `α` times an attained minimizing relaxation value `R*`, then `C≤α*R*≤α*original optimum` for nonnegative costs and the stated approximation factor. If the relaxed solver returns only a feasible value `P`, the first inequality may still hold with `P`, but the comparison to the original optimum needs a separate bound on `P` or a direct comparison of `C` with a justified lower bound.

Recovery can fail or produce no better candidate. Retain an already admissible better candidate. A useful bound alone can still guide search or show that further improvement is too small to matter.

#### CMP.5:4.5 - Return to the original problem and choose the next move

Return the recovered candidate under its original conditions and the bound that applies to the original objective. For minimization, an additive gap `C-L` bounds how much the candidate can still improve. A ratio uses additional conditions, such as a positive denominator; a zero or negative lower bound does not support a generic ratio claim.

Use the result to adopt the candidate, stop at an adequate gap, guide a branch of CMP.4, tighten the relaxation, revise recovery or choose a different algorithm. The stronger relaxation is worthwhile only if its expected contribution warrants the extra work.

When the question or allowed operations change, recheck the representation `i`, bound direction and recovery. A bound from a more restrictive former problem may cease to constrain the new one. A bound that remains valid may also become too weak to be useful.

### CMP.5:5 - Archetypal Grounding

#### CMP.5:5.1 - Recover indivisible choices from a fractional solution

In weighted vertex cover, a graph represents pairs that must be covered. Selecting a vertex covers its incident edges and incurs nonnegative cost `w(v)`. The original problem minimizes `sum w(v)*z(v)` with `z(v)` equal to 0 or 1 and `z(u)+z(v)≥1` on every edge.

Allow `0≤z(v)≤1` instead. Every integral cover remains feasible, so the fractional minimum is a lower bound. Obtain a fractional solution `x` and select every vertex with `x(v)≥1/2`. Each edge has an endpoint at least one half, so the selected vertices cover every edge. This derives feasibility of the rounding rule.

For each selected vertex, `w(v)≤2*w(v)*x(v)`. Summing over selected vertices, and using nonnegative weights for the remaining terms, gives `C≤2*sum w(v)*x(v)`. If `x` attains the fractional minimum, the recovered cover costs at most twice the original optimum. A merely feasible fractional point gives the displayed cost comparison but does not alone establish that approximation factor.

Consider a triangle with unit vertex costs. Setting every fractional value to one half gives value 1.5. Adding the three edge inequalities gives `2*sum x(v)≥3`, proving that 1.5 is the fractional minimum. Threshold rounding selects all three vertices with cost 3. Removing one vertex leaves a valid cover with cost 2, improving the initial candidate. Original costs are integers, so the lower bound 1.5 also implies an original cost of at least 2. The recovered cover is therefore optimal for this instance.

**Changed constraint:** add “select at most one vertex.” The fractional vector with all values one half violates this new constraint, and the recovered two-vertex cover is also inadmissible. If the cardinality constraint is deliberately dropped in the relaxation, 1.5 can remain a lower bound for feasible original solutions, but it provides no feasible cover. On a triangle one selected vertex always leaves the opposite edge uncovered, so the new original problem is infeasible. The previous recovery rule cannot be reused as a solution.

#### CMP.5:5.2 - Use a relaxed answer as a search bound

A robot moves on the finite grid with coordinates `0≤x≤2`, `0≤y≤1`. It can move one horizontal or vertical step at unit cost. The task is to go from `(0,0)` to `(2,0)`; cell `(1,0)` is blocked.

Ignore blocked cells in the relaxed problem. The distance is `abs(dx)+abs(dy)`, here 2. Every permitted original route is also a relaxed route with the same cost, so 2 is a lower bound. The straight relaxed route is unusable. An admissible detour through `(0,1),(1,1),(2,1)` costs 4, giving an initial comparison `2≤optimum≤4`.

CMP.4 can use the relaxed remaining distance at each partial route, together with the distance already traveled. Alternatively, the blocked direct row implies that a valid route must include an upward and a downward move in addition to two horizontal moves, proving a lower bound of 4. That stronger argument closes this small case. The relaxed result was useful without being mistaken for an executable original route.

**Changed operations:** allow diagonal moves at unit cost. The earlier Manhattan distance can overestimate: reaching `(1,1)` from `(0,0)` can cost 1 rather than 2. Relax the new movement problem instead. With unrestricted unit-cost horizontal, vertical and diagonal moves, `max(abs(dx),abs(dy))` is the distance and supplies the corresponding lower bound. The algorithmic thinking consists in rebuilding the comparison after the operations change.

### CMP.5:6 - Bias-Annotation

An elegant relaxed formulation can redirect effort toward solving the surrogate problem ever better while original feasibility remains unresolved. Keep the recipient's candidate or decision in view when choosing solver effort and recovery.

The word “bound” can also conceal a direction error. A convenient relaxed candidate is informative, but its objective value carries only the inequalities actually established. Calling a result approximate does not remove the need to state which conclusion the approximation supports.

### CMP.5:7 - Conformance Checklist

- The original feasible candidates, objective and useful next decision are stated.
- Every original candidate has the required representation in the relaxed problem, with the inequality in the needed direction.
- The relaxed solver's returned candidate, optimum, bound or estimate is used at its actual strength.
- Recovery is effective and its feasibility is established under the original conditions when an original candidate is promised.
- Loss through relaxation, incomplete solution and recovery is kept distinguishable where it affects the conclusion.
- Any additive or multiplicative comparison has its required sign and denominator conditions.
- A changed constraint or operation is followed through the relaxation and recovery before their result is reused.

### CMP.5:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Use a feasible relaxed objective as a minimizing lower bound | It can exceed the original optimum. Obtain an optimum, a dual lower bound or another justified bound. |
| Return the relaxed point as the original answer | Fractions or forbidden transitions can make it unusable. Construct and check recovery under the original conditions. |
| Round without examining the constraint | Coverage or capacity can fail. Derive the rounding direction and repair from the constraint's actual form. |
| Reuse the old relaxation after adding allowed operations | A former lower bound can become an overestimate, as with diagonal moves. Rebuild the problem comparison. |
| Tighten a bound after the decision is settled | Additional optimization consumes resources without changing the next action. Stop or redirect effort according to the receiving use. |

### CMP.5:9 - Consequences

A difficult problem can yield useful information and better candidates before it can be solved directly. Bounds can support early stopping, guide search and distinguish an unattained relaxed ideal from an original feasible result.

Weak relaxation or costly recovery can limit the gain. The method exposes these limitations as choices that can be changed: which conditions are relaxed, what result the easier solver supplies, and how the original candidate is reconstructed.

### CMP.5:10 - Architectural Rationale

The method joins two constructions that are often separated: making an easier problem informative and making its result usable in the original problem. Keeping recovery beside the bound prevents an easier optimum from replacing the task that motivated it.

MMP.10 supplies the formulated feasible problem when it arises from modeling; MATH.20 supplies mathematical inequalities. CMP.5 contributes the algorithmic construction of a relaxed obtaining problem and its recovery operation. CMP.4 can consume the bound without requiring a recovered candidate from every branch. Approximate subject models and general surrogate selection retain their own correspondence and portfolio methods.

### CMP.5:11 - SoTA-Echoing

[Williamson and Shmoys, *The Design of Approximation Algorithms*](https://designofapproxalgs.com/book.pdf), especially the introductory rounding constructions and later linear-programming methods, develops the link between relaxation, recovery and approximation bounds. Adopt the obligation to construct both feasibility and objective comparison. The triangle is a small worked instance of the familiar cover construction; its simple instance-specific optimality does not generalize to every graph.

The primary [SCIP 10.0 report](https://optimization-online.org/wp-content/uploads/2025/11/scipopt-100.pdf) adds a current computational consideration: relaxed bounds used in optimization can require rational or directed-rounding support to retain their direction. Adopt that consideration where the conclusion depends on it. A cheap conservative bound or direct candidate can be preferable to the additional solving and certification work.

The connection with relaxed path costs shows another use of the same construction. Here recovery is a separate route search, while the relaxed result supplies an optimistic cost.

For :4.2–4.5, compare relaxation and recovery with a direct algorithm, a cheaper feasible-candidate heuristic, and an already available valid bound. Prefer the lighter construction when it supplies the required candidate or comparison. Solving a relaxation more accurately is worthwhile when a tighter bound changes the search or when its recovered candidate improves the original result enough to repay the effort. Recovery can instead lose feasibility or too much objective value, as the changed cover case shows. Reconsider the selection when a new feasible-set relation, recovery guarantee, competing construction or resource limit changes that trade-off; an LP optimum is not a universal prerequisite.

### CMP.5:12 - Relations

- **MATH.20:** supplies the bound and inequality reasoning; **MMP.10** supplies the feasible problem in a modeled receiving use.
- **CMP.1:** transfers answers through effective problem reductions. The present relaxation can instead preserve a one-sided bound and require separate candidate recovery.
- **CMP.4:** uses relaxed bounds to exclude or prioritize search branches and to describe remaining improvement.
- **C.29 and C.29.2:** preserve the relation between the original subject question and the computational result being returned.
- **C.11.DUA and the general characterization, Pareto and improvement methods:** guide comparison of solver effort, candidate quality and further work.

### CMP.5:End
