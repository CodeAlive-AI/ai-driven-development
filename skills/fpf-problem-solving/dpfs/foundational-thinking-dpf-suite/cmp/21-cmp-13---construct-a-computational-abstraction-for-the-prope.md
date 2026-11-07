## CMP.13 - Construct a Computational Abstraction for the Property Being Asked

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.13:1 - Problem frame

**Use this when** computing every relevant state or execution is unaffordable, but the question needs only some of their properties. You want to calculate with ranges, classes, relations or other summaries and determine what their answers establish about the original computation. Use it also when such a calculation reports an impossible path or loses a distinction needed for the answer.

The reader can describe the admitted inputs, elementary transitions and requested observation. Examples include asking which outcomes a rule system permits, whether a procedure can reach a failing state, or which dependencies can affect a returned value. The method constructs another computation over descriptions of possibilities, then relates its result to the question.

The first useful result is an effective abstract operation or small abstract execution with a justified conclusion about the original process. Extending that result across loops or interacting components requires the corresponding closure or composition argument. A finite reachability example can be done by hand; building an analyzer for a programming language requires its semantics and suitable algorithms for its representations.

Use direct computation when it already answers the question affordably. If the required change is a numerical error allowance, CMP.8 supplies that construction. If the problem is whether the original process describes the intended subject, return to that modeling question: a sound calculation about the process retains its subject assumptions.

### CMP.13:2 - Problem

How can a calculation discard detail yet retain a justified answer to the property being asked, and recover the distinctions that an inconclusive answer exposes?

A summary can combine possibilities that never occur together. A sequence of individually possible transitions can then appear to be an executable path. Conversely, retaining every distinction may make the supposedly cheaper calculation as difficult as the original. Loops add another difficulty: successive summaries can keep changing even when each update is easy.

### CMP.13:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Useful loss and needed distinctions | A small summary is useful only if it retains enough to answer the current question. |
| Possible and realizable | An overapproximation can exclude an outcome conclusively while leaving an included outcome unconfirmed. |
| Local operations and whole executions | Each transition must respect the interpretation, and loops require closure over repeated transitions. |
| Precision and completion | More detailed states and slower extrapolation may improve an answer while increasing the obtaining cost. |
| Separate summaries and correlation | Cheap independent properties may lose the relation that determines the result. |

### CMP.13:4 - Solution

**Local mantra:** choose the property; describe the represented possibilities; derive the abstract operations; compute a sufficient closure; interpret the answer; refine the distinction that blocks its use.

#### CMP.13:4.1 - Choose the observation and the direction of inference

Specify the original states, initial possibilities and transitions. Include the program location or phase when the same stored values permit different next steps there. Identify what the answer concerns: a reachable value, a path, termination, an interaction or another property. A set of reached states usually loses the order needed for a path question.

Choose what an abstract value represents. Write `gamma(a)` for the original possibilities represented by abstract value `a`. It can be a set of integer values, environments, graph states or complete traces. The concrete domain in this construction is the process being analyzed; it need not consist of physical objects.

For an overapproximation, every original possibility must remain among the represented ones. If the calculated possibilities exclude a bad outcome, that outcome is excluded from the original process. An included bad outcome may require reconstruction before it supports a counterexample. For an underapproximation, represented possibilities must be realizable: a retained witness can establish existence, while a missing witness leaves other executions unresolved. Choose the direction for the question and maintain it through the operations. The remaining steps develop the overapproximation branch.

#### CMP.13:4.2 - Derive computable operations on the summaries

For an original operation `f` and abstract input `a`, construct `f#(a)` so that it covers every allowed result of applying `f` to an input represented by `a`. If `post(X)` collects the one-step successors of states in `X`, the condition is:

`post(gamma(a)) ⊆ gamma(post#(a))`.

This is the soundness direction: the abstract step may add possibilities, but it must retain every original successor. Handle branch restrictions, failure and the actual arithmetic under the same interpretation. For example, an interval operation justified over unbounded integers needs revision for wraparound arithmetic.

Provide a way to combine incoming possibilities. An abstract join of `a` and `b` covers `gamma(a) ∪ gamma(b)`; it may include additional states. Implement the comparison used to recognize that a new result is already covered. Choose a representation whose operations and comparisons are affordable; an arbitrary logical formula may express the wanted property while making those operations difficult to compute.

A constructive starting point is to apply the original operation conceptually to the represented inputs, identify the property of all resulting outputs, and derive a formula for that property. The derived formula performs the abstract calculation without enumerating those inputs. Independent ranges, relations between variables and partitions by selected conditions provide different choices. Use the stronger choice where the receiving question needs the distinction it retains.

#### CMP.13:4.3 - Compute a result closed under the admitted transitions

For a finite graph of program points, associate an abstract state with each point. Initialize it from the admitted inputs. Recompute a successor when a predecessor summary changes and join its new contribution with the old one. CMP.3 supplies dependency scheduling and reuse. With finitely many points, monotone updates and an abstract order with no infinite increasing chain, a fair worklist reaches a stable result; the number and cost of updates still determine feasibility.

An infinite or very long increasing chain may need extrapolation. A **widening** combines successive approximations into a covering value and is chosen so the widening iteration stabilizes. For intervals, a bound that keeps moving outward can be replaced by an infinite bound. Apply such extrapolation where cyclic dependencies need it. Call context, retained relations and placement of widening can change precision, so a larger summary language alone does not guarantee a better computed answer.

Check the resulting closure. If `I` is the initial set and `a` the proposed result, the sufficient conditions are:

`I ⊆ gamma(a)` and `post(gamma(a)) ⊆ gamma(a)`.

Every reachable state is then represented: induction on execution length uses the first condition for the start and the second for each step. An implemented abstract transformer can establish the second condition by showing its result is covered by `a`. Such an `a` is often called a post-fixpoint. A prematurely interrupted growing approximation need not contain every reachable state.

If the closure is too broad, use restrictions from guards, a more discriminating representation, or a narrowing operation with its own soundness conditions. A proposed smaller set is useful only while retaining the initial possibilities and closure. Directly checking these two conditions is often enough for a small construction. An all-executions termination or response-time claim needs a corresponding argument; a closed set of reached states alone supplies neither.

#### CMP.13:4.4 - Recover the conclusion and examine a reported witness

Apply the requested observation to the closed result. If its represented states all satisfy the property, use that conclusion with its original input and transition assumptions. If the result overlaps an unwanted outcome, determine whether the overlap changes the next action. It may already be sufficient to retain the unresolved alternative.

When an actual path matters, reconstruct consecutive original states, starting from an admitted initial state. For abstract path `a0, a1, ..., ak`, propagate:

`X0 = I ∩ gamma(a0)`;

`X(i+1) = post(Xi) ∩ gamma(a(i+1))`.

If some `Xi` is empty, the abstract path is spurious: its steps cannot be joined into one original execution. If the last set is nonempty and these sets were computed without adding possibilities, retained predecessors can recover a concrete path. If this reconstruction is itself approximate, qualify its result with that approximation's direction; a nonempty overapproximation still leaves feasibility unresolved.

Loops and infinite-path properties require their own path and recurrence conditions. A finite prefix reaching a bad state settles finite reachability; repeating an abstract cycle does not by itself produce an infinite original execution.

#### CMP.13:4.5 - Refine the lost distinction and continue from the affected computation

Locate where the reported execution or answer became impossible. Restore the distinction responsible: separate a merged state, retain a relation, distinguish a calling context, or make an abstract operation more precise. A false path through one merged class can suggest splitting its reachable dead ends from the states that supply its outgoing edge.

Recompute affected dependencies and reuse results whose inputs and interpretation remain valid. Confirm that the revised construction removes the particular spurious result and still covers all original behavior. Removing one false path may leave others.

Choose further refinement by what it can change in the receiving work. A coarse result that already answers the question is sufficient. A real counterexample changes the original construction or its allowed use; improving the analyzer cannot make that execution disappear. When refinement remains too costly or inconclusive, return the unresolved property and the condition under which another calculation or direct execution would help. C.11.DUA governs the worth of that additional work.

### CMP.13:5 - Archetypal Grounding

#### CMP.13:5.1 - A graph summary invents a path

The original graph has vertices `a,b,c,d`, edges `a->b` and `c->d`, and initial vertex `a`. The question is whether `d` is reachable. Merge `b` and `c` into abstract vertex `q`, while keeping `a` and `d` separate. An abstract edge exists when any original edge connects the corresponding classes.

The abstract graph has `a->q` and `q->d`. Searching it returns the path `a,q,d`. Each edge has an original witness, yet the first edge arrives at `b` and the second leaves `c`.

Reconstruction gives `X0={a}`, `X1={b}` and `X2=empty`, since `b` has no successor. Split `q` into `{b}` and `{c}`. The recomputed reachable set is `{a,b}`, so `d` is unreachable. The useful result is both the answer and the reason the original summary could not establish it.

**Changed condition:** add edge `b->c`. The abstract path `a,q,q,d` now reconstructs to `a,b,c,d`; this is a real path. The shorter path `a,q,d` still has no consecutive realization, but its failure no longer excludes reachability. The transition change requires the affected search and reconstruction to be updated.

#### CMP.13:5.2 - Obtain a loop property without enumerating its iterations

Consider unbounded integers, positive integer `N`, and:

```text
x = 0
while x < N:
    x = x + 1
```

At the loop head, a set `X` of possible values is transformed by `F(X)={0} ∪ {x+1: x∈X and x<N}`. An interval hull supplies an abstract transformer. Starting at `[0,0]` produces `[0,1]`, `[0,2]` and so on until `[0,N]`; this takes a number of expansions proportional to `N` even though `N` can be written with logarithmically many bits.

Widen the increasing upper endpoint of `[0,0]` and `[0,1]` to obtain `[0,+infinity]`. It contains the initial value and is closed under the guarded update. It already establishes that `x` is never negative.

Suppose the receiving question instead asks for the value on exit. Apply the guard to `[0,+infinity]`: the integer inputs admitted by `x<N` are `[0,N-1]`; adding one and joining the initial value gives `[0,N]`. This smaller interval is itself closed under `F`, and contains 0. The exit condition `x>=N` then leaves `[N,N]`. Therefore every terminating execution exits with `x=N`.

For a termination conclusion, add a different argument: while the guard holds, the nonnegative integer `N-x` decreases by one, and the arithmetic is unbounded. This proves termination from 0 for the stated positive `N`. It explains why the exit value is obtained, rather than merely describing it if obtained.

**Changed condition:** replace the update by `x=x+2`, retaining `N=5`. The guarded interval calculation now gives `[0,6]`; exit intersection gives `[5,6]`. If that bound is sufficient, stop. If the final value is needed, retain the invariant that `x` is even as well. The exit result becomes `{6}`. The old answer 5 was tied to the former update.

#### CMP.13:5.3 - Independent ranges lose the determining relation

Let input `b` be either 0 or 1. Execute `x=b; y=b`, then test whether `x!=y`. Independent intervals give `x∈[0,1]` and `y∈[0,1]`. Their product contains `(0,1)`, so it cannot exclude the unequal branch.

Recover the construction: both assignments use the same `b`. Retain `x=y`, or keep the two input cases separate. Each choice excludes the unequal branch. The shared equality is the needed distinction; refining both independent endpoint ranges cannot recover it.

If the second assignment becomes `y=1-b`, both inputs take the unequal branch. A retained relation must be derived again from the changed operation. The earlier equality is an invalid assumption in the new computation.

### CMP.13:6 - Bias-Annotation

An alarming abstract result can draw attention away from whether its states form an executable case. Trace reconstruction tests that inference. A preference for simpler summaries can hide correlations; a preference for stronger analyses can spend resources recovering distinctions that the current answer does not need. Compare the actual result and cost under the requested observation.

### CMP.13:7 - Conformance Checklist

- The initial possibilities, transitions and requested observation identify the computation being analyzed.
- Each abstract value has an interpretation, and the inference direction supports the claimed conclusion.
- Abstract operations and joins cover their original counterparts; the obtaining algorithm has a justified completion or bounded-result condition.
- A whole-reachability conclusion uses initial containment and transition closure.
- A claimed concrete counterexample has a consecutive realization; a failed reconstruction identifies the lost distinction or remaining uncertainty.
- Refinement preserves the original possibilities and changes a result relevant to the receiving work.

### CMP.13:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Treat every abstract path as executable | Different steps can use incompatible representatives of one class. | Reconstruct the consecutive original states. |
| Return a growing partial result as all reachable states | Unprocessed transitions can add states. | Establish closure or report the limited exploration performed. |
| Strengthen independent ranges to recover a correlation | The relation is absent from the representation. | Retain a relational property or separate cases. |
| Widen at every combination | Extrapolation discards useful information where a finite join would suffice. | Locate the cyclic dependencies and choose a terminating update strategy there. |
| Keep an invariant after changing the transition | The invariant may exclude new executions. | Recalculate the affected operation and closure. |

### CMP.13:9 - Consequences

The reader obtains a computation over properties, together with the direction in which its answers apply. A false abstract counterexample becomes a constructive guide to a better representation. An already adequate coarse result can end the work.

The result depends on the original semantics and on the abstract operations, evaluation strategy and observation. A sound representation can still yield an answer too imprecise or expensive for use. Some properties remain undecidable or require a different form of reasoning.

### CMP.13:10 - Architectural Rationale

The construction combines two methods of thinking: choose a mathematical account of possible states, then build an effective algorithm on that account. MATH.2's quotient preserves specified operations independently of representative. Here a summary may deliberately combine different successors, so its justification is inclusion of possibilities rather than equality of returned classes. MATH.18 supplies the direction-sensitive comparison between accounts.

The examples expose three distinct causes of lost information: incompatible representatives in a path, extrapolation across iteration, and discarded correlation. Their repairs act on the abstraction and its algorithm. The physical or organizational interpretation of the original state system remains a separate subject correspondence.

### CMP.13:11 - SoTA-Echoing

How can a cheaper computation answer a selected question about executions? **Adopt** the calculational approach organized in Cousot's [*Principles of Abstract Interpretation*](https://mitpress.mit.edu/9780262044905/principles-of-abstract-interpretation/): choose the property semantics and derive effective abstract operations. Its scope includes dataflow, dependency and typing as well as numerical properties. Direct finite exploration remains a serious cheaper alternative when its state space is manageable; a changed property or obtaining cost reopens the choice.

When independent summaries lose a needed relation, **adapt** the combination of algebraic and logical abstractions in [Cousot, Cousot and Mauborgne](https://www.di.ens.fr/~cousot/publications.www/CousotCousotMauborgne-JACM-59-6-32p-2012.pdf), especially their sound-transformer and reduced-product constructions. Combine complementary restrictions when that recovers the answer more cheaply than one uniformly rich domain. Solver-backed relations accept solver and representation costs; simple precomputed operations accept reduced expressiveness. The paper's implementation comparisons are historical, not a ranking of current tools. Reconsider the chosen abstraction and refinement when a lost correlation or unsupported machine semantics prevents the required conclusion.

For a reported abstract counterexample, **adopt** the reconstruct-and-refine step from [Clarke and colleagues](https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/Counterexample-guided%20abstraction%20refinement.pdf), sections 4.3–4.4. Its finite-path construction motivates :4.4–4.5 and :5.1: split the distinction that prevents consecutive realization. Uniformly increasing precision is the rival; it can resolve more future questions but pays for distinctions this path may not need. Infinite-path properties require the additional loop conditions rather than reuse of the finite-path test alone.

How should cyclic abstract computations be scheduled? **Adapt** the question raised by [Yang and colleagues' 2025 interprocedural ordering method](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ECOOP.2025.34): distinguish actual recursive dependencies from spurious cycles introduced by merged call contexts, then choose where widening and narrowing operate. A simple global worklist remains suitable when it produces an adequate result at lower construction cost. The reported advantages concern the paper's recursive-program analyses. Lost call correlation or iteration cost can trigger reconsideration.

### CMP.13:12 - Relations

- **MATH.2 and MATH.18:** supply operation-preserving identification and interpretations between mathematical accounts; the overapproximation here has its stated one-way consequence.
- **CMP.3 and CMP.4:** supply dependency reuse and search; closure over cycles and reconstruction of abstract witnesses are developed here.
- **CMP.8:** supplies controlled numerical approximation; inclusion of possible executions answers a different question from numerical closeness.
- **CMP.12:** supplies effective interpretation of the original expressions and operations whose semantics this abstraction uses.
- **C.29.1 and C.29.2:** supply the surrounding interpretation and computational formulation; applying the result to its intended subject returns to C.29.
- **C.11.DUA:** selects further analysis by the receiving action or conclusion it could change.

### CMP.13:End
