## MATH.20 - Bound a Mathematical Unknown by Comparable Constructions

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### MATH.20:1 - Problem frame

Use this pattern when obtaining a mathematical value or object is difficult, but a justified comparison could already answer the receiving question. Construct something known to lie below, above, inside or outside the unknown in the relevant mathematical order.

Examples include bounding a best attainable value by a feasible construction and an inequality, enclosing a set between simpler sets, or converting an equation residual into a bound on solution error. The common method is to build and justify the comparison, then determine what it permits next.

**First useful move:** name the unknown and one comparison that would change the next action. A single feasible construction can settle an existence question or one side of an optimum bound. A proved enclosure can exclude a region. Construct only the bound the current question needs.

The reader needs elementary inequalities, sets and functions. The examples introduce their graph and set constructions; the residual example also uses linear equations and an inverse map. More specialized bounds require the properties of their particular mathematical objects.

If an available value or direct calculation answers the question more easily, use it. FPF's characterization and choice methods select among alternatives; this pattern supplies mathematical bounds those choices may use. A mathematical comparison applied to a physical or organizational subject also requires the correspondence work in C.29 and MMP.

### MATH.20:2 - Problem

A plausible estimate can be close in familiar cases while lying on the wrong side of an unknown elsewhere. A bound on an intermediate quantity can also be mistaken for a bound on the requested result. For example, a small equation residual need not imply a small error in its solution.

Bounds themselves can be uninformative. A wide interval may leave the receiving choice unchanged, and separately sharp coordinate bounds may never be attained together. The work needs both a justified relation and a way to tell whether improving that relation would help.

### MATH.20:3 - Forces

| Force | Tension |
| --- | --- |
| Obtaining and comparing | It can be easier to bound a result than to construct it, but the comparison still needs an argument. |
| Direction | Feasible constructions and relaxed problems bound optima in different directions. |
| Tightness | A simpler bound can be cheaper; a tighter one matters only through the result it enables. |
| Propagation | An operation can preserve, reverse or destroy a comparison. |
| Attainability | A bound may be approached without being attained, or may require incompatible equality conditions. |
| Reuse | A proved comparison remains useful while its domain and premises survive. |

### MATH.20:4 - Solution

**Local mantra:** name the unknown and the needed comparison; construct a simpler comparator; prove its direction and scope; carry the comparison through the required operations; tighten or expose the gap; return the bounded result to use.

#### MATH.20:4.1 - Choose the quantity or object and its order

State what is unknown: a number, a function, a set, an error, an optimal value, or another mathematical object. State the comparison relation. Numerical order, pointwise order between functions and set inclusion support different conclusions.

For a numerical bound `L≤q≤U`, say which q is being bounded and under which assumptions. For an enclosure `L⊆S⊆U`, L consists of established members of S, while U contains every possible member under the stated description. Cardinality alone does not establish either inclusion.

For an optimum, distinguish the optimal value from an object attaining it. A bounded nonempty set of real values has an infimum and supremum, but an attaining object needs a further argument. For example, the interval `(0,1)` has infimum 0 and contains no minimum.

Select the needed direction and strength. To show `q≤t`, an upper bound at most t suffices. To refute that claim, a lower bound greater than t suffices. If the bounds straddle t, they leave this question open.

#### MATH.20:4.2 - Construct a comparator from available structure

Choose a construction whose relation to the unknown can be proved with available information.

| Requested result | Useful construction | Reason for the direction |
| --- | --- | --- |
| Minimum of an objective | A feasible candidate gives an upper bound; minimizing over a larger feasible set gives a lower bound. | The minimum is no larger than any admitted value; added choices can only lower the infimum. |
| Maximum of an objective | A feasible candidate gives a lower bound; maximizing over a larger feasible set gives an upper bound. | The maximum is no smaller than any admitted value; added choices can only raise the supremum. |
| Unknown set | Build a subset of verified members or a superset containing all admitted possibilities. | Membership proofs establish the two inclusions in opposite directions. |
| Error in a result | Relate a computable discrepancy to that error through the governing equation or map. | The derived inequality, such as the inverse-map bound in :5.2, connects the measured quantity to the requested one. |

Other constructions can use symmetry, a conserved quantity, a norm inequality or a comparison theorem. Select the property that supplies the missing direction. A familiar shape or similar-looking value is a candidate for investigation until that relation is established.

A comparator can be a different kind of object from the result. In :5.1 a node potential produces a numerical lower bound on every path length. The derivation makes those resulting values comparable; it does not compare a potential directly with a path.

#### MATH.20:4.3 - Establish the bound over its claimed domain

Prove the inequality or inclusion for every admitted case to which the result will apply. A feasible witness establishes one attainable value. A claim about all candidates needs a relation covering all of them, as the edge inequalities in :5.1 cover every path.

Track the assumptions used. For a relaxed feasible set, establish the original set's inclusion in it and keep the objective unchanged on original candidates. For a norm estimate, specify the norm and the operator property that supports it. For a probabilistic inequality, retain its distributional conditions and probability claim.

Use a known comparison theorem when it settles this question. If it does not, MATH.19 can construct the missing intermediate inequality and MATH.6 can test a suspected overclaim with a separating case.

Where the comparison cannot be established, return the condition that is missing or the counterexample. A trial value may remain useful for exploration without being used as the unproved bound.

#### MATH.20:4.4 - Propagate the comparison through the needed operations

For an order-preserving map F, `L≤q≤U` implies `F(L)≤F(q)≤F(U)`. For an order-reversing map, the endpoints exchange roles. Establish the relevant behavior on the admitted domain.

For example, multiplication by a nonnegative scalar preserves numerical order, while multiplication by a negative one reverses it. Squaring is increasing on nonnegative inputs; an interval crossing zero needs its minimum and maximum square computed on that interval. From `-2≤x≤1`, the bound is `0≤x²≤4`.

For sets, image and preimage under a fixed function preserve inclusion; complement reverses it in a fixed ambient set. Thus an enclosure can be carried into a subsequent transformation without requiring the original set to be enumerated.

Keep shared variables and constraints when combining bounds. If `x∈[0,1]`, separately bounding x and -x gives `-1≤x+(-x)≤1`, but retaining the dependency gives equality to zero. The loose result is valid; its loss comes from forgetting that the terms use the same x.

A bound computed with approximate arithmetic must preserve the claimed direction after that computation. A computational continuation can use error bounds or enclosing arithmetic for this purpose; the mathematical argument states the comparison it must maintain.

#### MATH.20:4.5 - Tighten the comparison or identify what prevents it

Inspect where the proof introduces slack. It may enlarge the feasible set, forget a dependency, replace a quantity by a worst-case value, or use one norm for effects that could be bounded separately.

Improve the part that can change the receiving result. Construct a better feasible candidate, strengthen the inequality, partition the domain, retain a lost relation, or add an available premise. A bound on a requested component can be enough when a bound on the whole object is costly or impossible.

Check attainability and equality conditions. When a feasible value meets a proved bound in the opposite direction, the optimum is established. When equality conditions conflict, the current bound can remain valid while failing to identify an attainable result. A sequence approaching a bound can establish an infimum or supremum without an attaining object.

If the gap reflects missing information, expose it. Two admissible constructions with different answers can show why the current assumptions do not determine a narrower result. That identifies a useful next assumption, observation or mathematical question.

#### MATH.20:4.6 - Use the bounded result and stop at the needed strength

Return the comparator, its relation to the requested result and the premises needed by the next use. A numerical interval, a set inclusion or a short inequality can carry this result.

For a minimization with feasible value U and lower bound L, the candidate is within `U-L` of the optimal value when these quantities are finite. The receiver can use that gap to decide whether further optimization matters. If only exclusion, existence or a threshold result was needed, stop once that result follows.

General choices about cost, value and further work use FPF's existing characterization, Pareto and improvement methods. Componentwise mathematical bounds can inform them, but a candidate attaining one coordinate need not attain another. Preserve which constructions actually realize the compared results.

Reopen the affected bound when its domain, objective, available information or following operation changes. Preserve bounds whose proofs still apply.

### MATH.20:5 - Archetypal Grounding

#### MATH.20:5.1 - Bound a shortest path before completing a search

Consider a finite directed graph with nonnegative edge weights and at least one path from s to t. Its shortest path length D is attained: cycles can be removed without increasing length, leaving one of finitely many simple paths.

Any particular s-to-t path of length U gives `D≤U`. For a lower bound, assign a number p(v) to each node such that, for every edge from u to v,

`p(v)-p(u)≤w(u,v)`.

Along any path, add these inequalities. The intermediate potentials cancel, giving `p(t)-p(s)≤path length`. Therefore `p(t)-p(s)≤D≤U`.

Take nodes s,a,b,t and these edges:

| Edge | Weight |
| --- | ---: |
| s to a | 2 |
| a to t | 5 |
| s to b | 4 |
| b to t | 1 |
| a to b | 1 |

The path s-a-t gives U=7. Choose `p(s)=0, p(a)=2, p(b)=3, p(t)=4`. The edge differences are respectively 2,2,3,1,1, each no larger than its edge weight. Thus `4≤D≤7`.

The equality cases suggest s-a-b-t. It has length 4, meeting the lower bound, so D=4. The proof of optimality uses a feasible path and the comparison applying to every path; it does not need a list of every possible path.

**Changed condition.** Add an edge s-to-t of weight 1. The old potential violates its new edge inequality, since `4>1`; its lower bound is invalid for the enlarged graph. The old path still supplies upper bound 4, and the new edge improves that to 1. The potentials `p(s)=p(a)=p(b)=0, p(t)=1` satisfy every new edge inequality, proving D=1. Only the comparison affected by the new edge had to be replaced.

#### MATH.20:5.2 - Convert a residual to the error actually requested

Suppose `Ax=b` has an invertible linear map A, and an available approximation is xhat. Define its residual by `r=A xhat-b`. Then

`xhat-x=A⁻¹r`.

If the chosen vector norm and induced operator norm give `||A⁻¹||≤K`, it follows that

`||xhat-x||≤K||r||`.

The bound K is the missing comparison between residual and solution error. It can come from a proved estimate of the inverse action; forming the entire inverse is unnecessary when a cheaper bound is available.

For a concrete case, A is diagonal with entries 1 and 0.001, b=(1,1), and xhat=(1,999). Use the maximum absolute coordinate as the vector norm. The inverse scales the coordinates by 1 and 1000, so its operator norm is 1000. The residual is (0,-0.001); the bound on solution error is 1. The actual solution (1,1000) attains that error.

A requested error of at most 0.01 therefore requires a residual bound of at most 0.00001 under this comparison. The apparent smallness of 0.001 was insufficient for that request.

**Changed condition.** Let the second diagonal entry become zero and b=(1,0). The equation fixes the first coordinate and leaves the second arbitrary. Residual zero cannot bound distance to a specified second-coordinate value: solutions with arbitrarily different second coordinates have the same residual. A request about the first coordinate alone is still answerable. Return that determined component or supply an additional condition selecting the second.

The method has derived an error relation and exposed its failure condition. A numerical method can now decide how accurately to obtain the residual and the approximation; the bound itself has not selected a solver.

#### MATH.20:5.3 - Enclose a set and improve the consequence

Let S be the disk `{(x,y): x²+y²≤1}`. The work needs the largest value of `g(x,y)=x+y`, but first seeks cheaper comparable sets.

The diamond `L={(x,y): |x|+|y|≤1}` lies inside S, because `x²+y²≤(|x|+|y|)²≤1`. The square `U=[-1,1]×[-1,1]` contains S, because each coordinate square is at most one. Thus `L⊆S⊆U`.

Over L, `x+y≤|x|+|y|≤1`, attained at (1,0). Over U, `x+y≤2`. Therefore the maximum over S lies between 1 and 2. Its existence follows, for example, from continuity of g on the compact disk.

The point (1,1) attaining the outer bound is outside S. To tighten that bound, retain the relation between the coordinates:

`(x+y)²≤2(x²+y²)≤2`,

where the first inequality follows from `(x-y)²≥0`. Hence `x+y≤sqrt(2)`. The point `(1/sqrt(2),1/sqrt(2))` belongs to S and attains this value, completing the comparison.

The inner set supplied feasible values; the outer set supplied a restriction on all feasible values. A better inequality and its equality case closed the gap. The same inclusion method can enclose a feasible region, a family of functions or another set, with the corresponding proof of membership and bound on the requested operation.

### MATH.20:6 - Bias-Annotation

A single numerical answer can hide which object or property was bounded. The examples make that choice visible: path length, error in a vector, and an enclosed set with an objective on it.

Simple bounds can look weak beside a precise calculation, yet already settle the receiving question. A small displayed residual can produce the opposite bias. Judge the comparison by its proved relation to the needed result, keeping its cost in view.

### MATH.20:7 - Conformance Checklist

For the comparison being used:

- The unknown, comparison relation and requested consequence are identifiable.
- A feasible witness, enclosing object or inequality supplies the claimed direction.
- The proof covers the domain and assumptions of the intended use.
- Operations preserve or reverse the comparison under stated conditions.
- Shared variables and dependencies are retained when their loss matters.
- The bound on a value is distinguished from an object attaining it.
- The remaining gap identifies either sufficient precision or a useful refinement.
- A changed premise reopens the comparison it invalidates, while unaffected results remain available.

### MATH.20:8 - Common Anti-Patterns and How to Avoid Them

**One attainable value used as a universal bound in the wrong direction.** A path of length 7 bounds the shortest length from above. The potential inequalities supply the lower bound.

**The comparator's optimizer used as an original solution.** The square's maximizing point in :5.3 is outside the disk. Check membership in the original feasible set before using it as a candidate.

**An operation applied without its order conditions.** Squaring an interval crossing zero requires inspecting zero and both endpoints; simply squaring endpoints in their original order gives the wrong enclosure.

**A discrepancy used as the requested error.** In :5.2 the inverse action amplifies the residual, and singularity removes the full-solution bound. Derive the relation or restrict the requested output.

**Separate extrema treated as jointly attainable.** Retain the common variables and equality conditions. Their incompatibility can explain why a valid bound remains loose.

### MATH.20:9 - Consequences

A justified bound can terminate a search, establish an impossibility, support a controlled approximation or identify missing information. It can also make a difficult problem workable before its complete solution is available.

The constructions reveal further methods: improve a feasible witness, solve a relaxation, exploit a dependency or change the requested output. The comparison provides a reason to choose among these next mathematical operations.

### MATH.20:10 - Architectural Rationale

The unknown is reached through another construction whose mathematical relation to it is tractable. Feasible witnesses, potential inequalities, inverse-map estimates and set inclusions give different ways to establish that relation. Their common structure is an order with a proved direction and operations that preserve the intended consequence.

Constructing bounds and choosing between alternatives have different results. The first supplies an inequality or enclosure; the second uses it with the purposes and costs of the work. This lets the same mathematical method serve proofs, computations and modeling without adding a separate preference system.

The gap is itself useful mathematical information. Matching attainable bounds can establish an optimum; a failed equality condition or two separating cases can show what prevents a narrower answer.

### MATH.20:11 - SoTA-Echoing

The working question is how to obtain a useful justified comparison without first solving the whole problem. The selected line combines feasible construction, relaxation or a comparison identity with explicit order propagation and an examination of the remaining gap.

Vandenberghe's [Duality, EE236A lecture 6, especially 6-4](https://www.seas.ucla.edu/~vandenbe/ee236a/lectures/duality.pdf) derives the relation between feasible primal and dual values. Its contribution to :4.2/:5.1 is that a feasible construction and a general inequality can bound the same optimum from opposite sides. A complete optimal solution is unnecessary for each bound. Direct solution is cheaper for an easy instance; bounding becomes useful when a partial construction already settles the receiving question. Equality and attainment require the particular argument, not an unrestricted assumption of strong duality.

Higham's [What Is Backward Error?](https://nhigham.com/2020/03/25/what-is-backward-error/) and [What Is a Condition Number?](https://nhigham.com/2020/03/19/what-is-a-condition-number/) explain why a discrepancy must be combined with the relevant sensitivity and why norm, perturbation class and requested output matter. The adopted consequence is :4.3/:5.2: derive a bound for the requested error and inspect the inverse action. A bare residual is a cheaper observable but can answer a different question. A proved componentwise or structure-specific estimate can be more informative than a coarse whole-vector estimate; no one condition number is imposed on every problem.

The current [Mathematics in Lean treatment of monotonicity](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html) and [set inclusion](https://leanprover-community.github.io/mathematics_in_lean/C04_Sets_and_Functions.html) makes the quantified preservation steps explicit. It supports :4.3-.4 and the set branch of :5.3. These mechanisms are usable in ordinary proofs or formal checking; choosing Lean is optional.

The synthesis retains the cheapest comparison that supports the requested result and exposes the part of its proof that could be tightened. Reopen it when the domain, objective, available premises or required operation changes, or when a different bound would resolve a still-open use with less work.

### MATH.20:12 - Relations

- **MATH.19** constructs the intermediate inequality or inclusion; **MATH.6** separates a claimed bound from a counterexample.
- **MATH.11** develops invariants that can constrain the unknown; **MATH.17** helps analyze operations used to propagate comparisons.
- **MATH.21** uses bounds to construct limits and obtain sufficient finite approximations.
- **C.29 and MMP** connect the mathematical comparison to the modeled subject.
- Computational methods can use these results in search exclusions, relaxation, approximation and resource analysis.
- FPF's characterization, Pareto and improvement methods use the resulting comparisons to choose the next work.

### MATH.20:End
