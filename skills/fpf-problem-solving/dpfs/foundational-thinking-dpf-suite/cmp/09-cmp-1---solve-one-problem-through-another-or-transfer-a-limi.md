## CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.1:1 - Problem frame

Use this pattern when an unfamiliar computational problem might be solved through another problem, or when you need to determine what an assumed solver would make possible. The useful connection must turn admitted inputs into usable queries and recover the answer required by the original question.

Start by naming the problem to be answered and the problem whose solver will be used. Construct a conversion on one revealing input and say how each possible solver answer returns to the first problem. A working conversion, a failed return condition or a correctly directed impossibility consequence is a useful first result.

A **computational reduction from A to B** is an effective way to solve A using a solver for B. The main route constructs a query and an answer-recovery procedure; a later branch covers several queries. The reader needs elementary algorithms, finite representations, function composition and arguments about termination. The graph example explains its representation and assumes a suitable shortest-path solver. The undecidability example uses the stated halting result as a mathematical premise.

Use an available solver directly when its admitted inputs and answers already fit the question. C.29.2 supplies ordinary computational formulation. The present method develops the missing reduction and what follows from it. Approximate, randomized or physically realized computations require the corresponding answer and resource guarantees when they enter this connection.

### CMP.1:2 - Problem

Two problems can have similar names or output shapes while admitting different inputs or requiring different guarantees. A conversion can lose the distinction that determines the answer, create a target input outside the solver's domain, or leave no effective way to recover the original output.

A reduction can also be used backwards. Solving A through B supplies an A-solver when B is solvable; a known impossibility for A then constrains B. Reversing that implication can rule out a useful algorithm without justification.

The task is to construct the connection, establish its answer relation and effective execution, and carry only the consequence that its direction and resource conditions support.

### CMP.1:3 - Forces

| Force | Tension |
| --- | --- |
| Reusing a solver and preserving the question | The solver may answer a translated problem while the original output or a negative case remains unresolved. |
| Mathematical definition and effective construction | A conversion can be well defined while computing it requires the answer being sought. |
| Computability and resource use | An effective reduction can create instances too large for the intended budget. |
| General limit and restricted use | A universal impossibility can coexist with algorithms for a narrower input class or a weaker answer. |

### CMP.1:4 - Solution

**Local mantra:** specify both answers; construct the queries; recover every relevant answer; establish direction and cost; use the consequence; revise the changed condition.

#### CMP.1:4.1 - Specify the two problems and the intended conclusion

Call A the problem to be answered through B. State each problem's admitted inputs and required outputs. An output might be a value, a satisfying witness, a decision including negative cases, or an approximation with a stated guarantee. Choose the forms actually needed.

For a decision problem, write `A(x)` for the proposition to be decided on input x. A solver must return a correct yes or no and terminate on every admitted input. If a proposed procedure only eventually confirms positive cases, retain that different capability in the problem statement.

For a witness problem, let `Ans_A(x,y)` mean that y is an acceptable answer for x. Specify what the procedure should do when no witness exists if that case is admitted. Use C.29.2 when the answer, representation or available elementary operations still need formulation.

Name the intended use of the reduction: build an algorithm from an available solver, transfer a known impossibility, or derive a resource consequence. This selects what effectiveness, return and cost arguments are needed.

#### CMP.1:4.2 - Construct a query from the available input and operations

Build a terminating procedure f that maps each admitted A-input x to an admitted B-input `f(x)`. Work from the information actually present in x and the operations available to the conversion.

A useful way to begin is to identify what a B-instance must represent about x. Construct its components and relations, then retain any additional information needed for answer recovery. When the input contains a program, a conversion can assemble a new program description with that program embedded in it. Constructing the description and executing the embedded program are different operations.

Check the solver's input conditions. A graph procedure accepting only nonnegative edge weights cannot be used unchanged when the conversion creates negative edges. A procedure specified for finite explicit inputs needs a suitable finite representation.

If producing `f(x)` assumes an answer to A(x) that the available operations do not obtain, the proposed conversion has not supplied the reduction. Replace that assumption with an effective construction from the available input, or retain it as the unresolved computational contribution. When obtaining the answer during conversion is effective, include that work in the cost and usefulness comparison.

#### CMP.1:4.3 - Construct answer recovery and establish correctness

For a single-query witness reduction, give a recovery procedure `r(x,z)`. For every admitted x and every answer z the B-solver is permitted to return, establish:

`Ans_B(f(x),z) implies Ans_A(x,r(x,z))`.

The recovery must terminate under those conditions. Include negative outcomes, failure reports or approximation bounds when the A-contract needs them. A single fortunate B-answer is insufficient if the solver may validly return another answer that the recovery cannot use.

For a yes/no-preserving decision reduction, establish both directions:

`A(x) iff B(f(x))`.

Then the B-answer is the A-answer. If recovery reverses or otherwise changes the returned answer, state that rule and prove the resulting correspondence. For example, one positive implication alone leaves the no branch undecided.

When several queries are needed, construct the calling algorithm. State how a returned answer determines the next query and retained state, why every query is admitted, and why correct target answers lead to termination with the required A-answer. An adaptive reduction is a procedure using the solver, rather than one fixed input map.

Compose reductions by composing their actual conversions and recovery procedures. Intermediate answers must satisfy the next procedure's conditions. MATH.17 and MATH.18 support the mathematical composition and interpretation questions; the present work additionally establishes effective execution under the selected computational model.

#### CMP.1:4.4 - Follow the direction of the consequence

For an established reduction from A to B:

- A suitable B-solver, together with the reduction, gives a suitable A-solver.
- If no such A-solver can exist under the stated model and guarantee, no B-solver with the assumed capability can exist.

Write the constructed A-procedure before using the second conclusion. It shows what the assumed B-solver would enable and where the contradiction arises.

Keep the scope of a limit. An impossibility for a total decision procedure on an unrestricted input class leaves other questions open: positive-case recognition, bounded execution, a restricted class, or a different computational model. Choose an alternative only when it supplies a useful answer for the work. The finite-state return in :5.2 shows such a change.

For a complexity consequence, use a reduction with the required resource bound. An unboundedly expensive input conversion supplies no efficient A-algorithm merely because B has one.

#### CMP.1:4.5 - Derive the cost that can change the choice

When cost matters, include input conversion, query size, solver calls and answer recovery under a named computational model. If conversion costs `T_f(n)`, its output has size at most `m(n)`, B costs `T_B(m(n))`, and recovery costs `T_r(n,m(n))` including the returned answer size relevant to it, the one-query construction has the corresponding total bound:

`T_A(n) <= T_f(n)+T_B(m(n))+T_r(n,m(n))`.

If the answer size is not bounded through these arguments, include it explicitly. For several queries, sum the costs of their construction, calls and recovery, including any adaptive work between calls. Analyze peak simultaneous storage separately from total work.

The representation matters. A quantity written with n bits can have a value exponential in n; enumerating that many states changes the cost claim. Exact rational operations also have costs depending on operand length when bit complexity is the model.

Use the result to choose or reject the reduction for the current resources. Another solver, a smaller representation or a different computational construction can preserve the answer while changing cost. C.29.2 supplies the surrounding resource and accuracy formulation.

#### CMP.1:4.6 - Return a usable construction or a bounded limit

For solver reuse, return the input construction, solver conditions, recovery and relevant cost. A user should be able to follow an input through to its original answer.

For a limit, return the reduction argument, its computational assumptions and the excluded guarantee. Use that result to revise the actual question or allocation of work. A failed implementation attempt supplies neither this limit nor a reason to stop searching for a valid reduction.

When the input class, answer guarantee, representation or available solver changes, revisit the affected connection. Retain the earlier consequence for the conditions under which it was established.

### CMP.1:5 - Archetypal Grounding

#### CMP.1:5.1 - Solve difference constraints through a graph problem

The input is a finite set of variables and inequalities of the form:

`x_v <= x_u+w(u,v)`,

with rational weights. The required answer is an assignment satisfying all inequalities or a correct infeasibility report.

Construct a directed graph with one vertex per variable and an edge u to v of weight `w(u,v)` for each inequality. Add a new source s with a zero-weight edge to every variable vertex. Use a solver that permits negative edge weights and returns either shortest-path distances from s or a reachable negative cycle.

A negative cycle proves infeasibility: sum its inequalities. Every variable cancels, leaving `0 <= sum of cycle weights`, which is false for a negative total.

If there is no negative cycle, all vertices are reachable from s and their shortest distances are finite. For every edge, the shortest-path condition gives:

`d(v) <= d(u)+w(u,v)`.

Thus `x_v=d(v)` recovers a satisfying assignment. This proves the required return for either solver outcome.

For example, take `x_b<=x_a+3`, `x_c<=x_b-2` and `x_a<=x_c+1`. Distances `(d(a),d(b),d(c))=(-1,0,-2)` satisfy all three. If the final bound changes to `x_a<=x_c-2`, the directed cycle has weight `3-2-2=-1` and proves infeasibility.

For n variables and m inequalities, construction adds n+1 vertices and m+n edges. Reading or assembling those lists and copying back an assignment takes O(n+m) operations under the explicit-graph model. Add the selected solver's cost on that graph and the rational-arithmetic costs appropriate to the representation.

The graph is a computational construction for the given inequalities. If those inequalities describe schedules, flows or another subject, their physical or organizational adequacy is a further modeling question. The reduction has established the answer for the supplied mathematical constraints.

#### CMP.1:5.2 - An event decider would decide halting

A team asks for a procedure that always decides whether an arbitrary deterministic program with unbounded working memory will eventually emit a designated event. The input is a finite program description, its finite initial data and the event to be recognized. The guarantee includes terminating with “no” for a program that never emits it.

Use the halting problem as A: given a program P and input x, decide whether P(x) terminates. Under the ordinary Turing-computable model, no total algorithm decides this for all programs and inputs.

Construct a program Q with x and P's description included. Q simulates P on x, suppresses the simulated program's output, and emits the designated event if and when the simulation halts. The description of Q is obtained by placing the supplied data inside this fixed wrapper; constructing it does not run P(x).

If P(x) halts, Q emits. If P(x) does not halt, Q never reaches its emitting step. A supposed total event-decider applied to Q would therefore decide A in both cases. This contradicts the halting result, so the requested universal event-decider is unavailable under these assumptions.

The direction matters: halting was reduced to event decision. The argument constructed a halting decider from the assumed event decider.

Now change the admitted system to a fully represented deterministic finite-state machine with effective transitions and a decidable emitted-event label on each transition. Starting from its initial state, follow transitions while remembering visited states. Return yes upon the event; return no if the machine halts without it or repeats a state before emitting it. At most the number of reachable states can be visited before such repetition or termination. Determinism and complete state make the future repeat as well.

This supplies a usable decision procedure for the changed class. If an environment can add unrepresented inputs or the “state” omits a changing counter, restore those inputs or state before applying this finite-state result. C.29.2 and A.3.3.TR supply that formulation work. The original universal impossibility and this restricted procedure remain compatible.

#### CMP.1:5.3 - A small description can create an expensive search

An input describes b Boolean state variables. A conversion that explicitly constructs every possible state may produce `2^b` vertices. Even a solver linear in the resulting graph size then gives an exponential dependence on b.

The construction may still be effective and useful for small b. For a larger budget-constrained use, keep the original answer condition and seek a representation or method that avoids explicit expansion, or derive a suitable restriction of reachable states. Calling the target solver efficient does not settle the cost of the whole reduction.

#### CMP.1:5.4 - Recover a witness through adaptive decision queries

The required answer is the lexicographically least satisfying assignment of a Boolean circuit C on n ordered input bits, or `UNSAT`. An available solver decides whether a supplied circuit has any satisfying assignment and terminates on either answer.

First query C. A negative answer gives `UNSAT`. After a positive answer, retain a prefix with a satisfying extension. Try its next bit as 0 and query the circuit with that prefix fixed. Keep 0 if the answer is yes; otherwise keep 1. The retained prefix still has a satisfying extension. After n bit choices it is a complete satisfying assignment; preferring 0 at each position makes it the least one.

For `C(a,b,c)=(a or b) and (not a or c)`, the answers are:

`C: yes -> prefix 0: yes -> prefix 00: no -> prefix 010: yes`.

The recovered answer is `010`. For circuit size N, copying each restricted circuit takes O(N) work. There are at most n+1 calls, giving total work bounded by `(n+1)T_B(O(N))+O(nN+n)` and sequential-call space `O(N+n+S_B(O(N)))`.

If the solver only recognizes satisfiable inputs and may diverge otherwise, the query at prefix `00` can fail to return. This construction then lacks its required guarantee. Obtain a total decider or use finite enumeration, whose worst-case work is `O(2^n N)`.

### CMP.1:6 - Bias-Annotation

The solver's familiar name can draw attention away from its admitted inputs and returned guarantees. Follow the actual conversion and recovery, including the negative branch the original problem requires.

An impossibility argument can also be overextended. Keep its input class, computational model and answer guarantee visible, then examine a changed useful question at those same points. A resource estimate is conditional on the representation used.

### CMP.1:7 - Conformance Checklist

For the reduction being used:

- Both problems have stated admitted inputs and required answers.
- The conversion is effective from the supplied input and produces admitted queries.
- Every solver outcome relied on by the construction has an effective recovery with the required guarantee.
- The correctness argument covers the needed directions and termination conditions.
- The consequence follows the direction of the constructed solver reuse.
- A resource claim includes conversion, calls, recovery and relevant representation sizes.
- The result supplies an algorithm, a useful restricted alternative or a limit with a specific effect on the next move.

### CMP.1:8 - Common Anti-Patterns and How to Avoid Them

**Assuming an unavailable answer to construct the query.** A wrapper program can be constructed without running the program it contains, as in :5.2. Identify that effective construction. If choosing the wrapper requires an answer that the available operations cannot obtain, the conversion remains unresolved.

**Using only the successful branch.** Finding an emitted event confirms a positive case. The universal decision request also requires a terminating negative answer, which simulation alone leaves unresolved.

**Reversing the reduction.** Write the A-procedure using the B-solver before transferring an impossibility or an algorithm. Its actual calls determine the direction.

**Hiding conversion cost behind the solver's bound.** Explicit expansion of b bits into `2^b` states dominates the use in :5.3. Include the created instance and its storage in the resource argument.

### CMP.1:9 - Consequences

An unfamiliar problem can acquire a usable algorithm through a constructed connection to another. The same form of reasoning can establish a limit by showing what an assumed solver would imply.

The reduction retains responsibility for inputs, answers and resource effects at the connection. A new solver or representation can improve it; a changed answer guarantee or input class can invalidate only part of its earlier use.

### CMP.1:10 - Architectural Rationale

Effective conversion and answer recovery make reduction a computational method. Mathematical correspondence supplies the relevant implication, while computability and cost determine whether the connection can be used under the stated conditions.

Solver reuse and impossibility belong together because the latter follows by assuming and then constructing the former. Their guarantees and direction remain explicit. The shortest-path and program-wrapper cases demonstrate different uses of that shared method.

C.29.2 already supplies the computational question, representation and ordinary progress account. This pattern develops a missing reduction, its answer relation and the consequence of an available or assumed solver. More specialized algorithm constructions can supply the conversion or the target solver.

### CMP.1:11 - SoTA-Echoing

Erickson's [Undecidability notes](https://jeffe.cs.illinois.edu/teaching/algorithms/models/07-undecidable.pdf), §§7.4-7.5 and 7.9-7.10, supplies a foundational account of effective program construction and the direction of reduction arguments. The adopted contribution is the explicit construction that turns an assumed solver into another solver. The event-wrapper example here uses the halting result under its stated computational model.

Erickson's [Shortest Paths](https://jeffe.cs.illinois.edu/teaching/algorithms/book/08-sssp.pdf) supplies the directed-graph and negative-cycle machinery used in the solver-reuse case. The recovered inequalities and their infeasibility argument explain what that machinery answers in the source problem.

A direct algorithm is preferable when conversion adds effort without improving the needed result. When a reduction is useful, the choice among ordinary computability, bounded-resource, approximate or randomized reductions follows the answer guarantee being transferred. A preserved decision alone leaves an approximation ratio, probability or practical runtime to its corresponding argument.

### CMP.1:12 - Relations

- **C.29.2** specifies computational answers, representation, progress, accuracy and resources.
- **C.29** establishes a subject correspondence when the computational problem describes something beyond the mathematical construction.
- **MATH.17 and MATH.18** develop operations on operations, interpretations and their preserved consequences.
- **MATH.4 and MATH.12** supply induction and constructive argument methods when the reduction needs them.
- **A.3.3.TR** recovers state and continuation distinctions, including those needed by finite-state restrictions.
- **C.39 and C.40** help develop a missing computational way or explore alternatives when a construction remains unresolved.

### CMP.1:End
