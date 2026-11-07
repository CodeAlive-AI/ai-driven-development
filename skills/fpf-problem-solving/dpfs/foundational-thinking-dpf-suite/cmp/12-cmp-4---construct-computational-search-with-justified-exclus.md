## CMP.4 - Construct Computational Search with Justified Exclusions

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.4:1 - Problem frame

**Use this when** an answer must be constructed by choosing among alternatives, direct enumeration is too costly, and information about a partial choice can eliminate some of its completions. You need a search procedure that saves work while retaining the answers its recipient needs.

Examples include finding an assignment satisfying constraints, selecting a best combination, constructing a counterexample and exploring possible program states. The general difficulty is deciding which alternatives may be omitted. A promising search order can find an answer quickly while providing no reason to exclude the alternatives visited later.

The gain is a search with explicit coverage, useful exclusion rules and a result that remains interpretable if computation is interrupted. The reader needs finite sets, logical conditions and inequalities; MATH.20 supplies a more developed bound argument. C.29.2 supplies the wanted computational answer.

Use direct construction or enumeration when it already solves the problem at acceptable cost. Heuristic search is also useful when a good candidate is enough. Apply the exclusion method to the conclusions that must be retained, without requiring proof of global optimality for every candidate search.

### CMP.4:2 - Problem

How can a procedure omit whole sets of candidates and still return a valid witness, a justified optimum or a warranted statement that no required answer exists?

The exclusion must concern every relevant completion represented by the omitted branch. Failure of one attempted completion or poor predicted performance alone does not establish that result.

### CMP.4:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Coverage and early progress | Broad exploration retains alternatives; informed order may obtain a useful witness sooner. |
| Cheap and strong exclusions | A weak inexpensive bound can save more total work than a costly tight bound. |
| One answer and all answers | A rule preserving one optimum can discard other attaining objects. |
| Current candidate and remaining possibility | A feasible result establishes what can be done; a branch bound constrains what remains possible. |
| Reuse and assumptions | A learned conflict can remain useful across branches but fail after constraints change. |
| Return time and strength of conclusion | An interrupted search can still supply a candidate and a bound, while exhaustion supports a stronger conclusion. |

### CMP.4:4 - Solution

**Represent the alternatives → cover them by extensions → derive exclusions → choose exploration order → retain the remaining possibility → return the supported answer.**

#### CMP.4:4.1 - Define a partial choice and its completions

State what constitutes a complete candidate, when it is admissible, and which result is wanted: one witness, a best value and witness, every optimum, a count, or a counterexample. For optimization, state the criterion and its direction.

Choose a representation `s` of partial choices. Explain which complete candidates it represents and what information is still undecided. Include past choices when they change future feasibility or cost. If several histories have the same remaining question, CMP.3 can share that question while preserving the history-dependent contribution.

Construct extensions that cover the relevant completions. Binary inclusion/exclusion, a variable's remaining values and legal next transitions are common forms. Overlap is permitted for finding one witness but can duplicate results; counting and enumeration need a way to handle it. A symmetry reduction needs an account of which answers it identifies and whether the recipient accepts that identification.

#### CMP.4:4.2 - Derive an exclusion that applies to the entire branch

Select a reason for omitting `s` according to the result required:

| Reason | Required argument | What it allows |
| --- | --- | --- |
| Infeasibility | No completion of `s` can satisfy the original conditions. | Discard `s` when looking for admissible answers. |
| Bound | Every completion has a value no better than a bound compared with an already admissible answer. | Discard `s` for the corresponding optimization conclusion. |
| Dominance | Another retained choice supplies an admissible answer at least as good for every continuation that matters. | Omit dominated work while retaining the stated result. |
| Equivalent completions | A retained representative accounts for the answers required from `s`. | Share or omit duplicate work with the appropriate treatment of identity and multiplicity. |

Construct these arguments from the constraints and the partial state. Propagating a choice can shrink the permitted values of other variables; an empty remaining domain then excludes that branch. A bound may come from relaxing the remaining problem through CMP.5. Dominance must include future possibilities, not merely compare the current partial scores.

For a maximization problem, let `L` be the value of the best admissible candidate already obtained, often called the incumbent. Let `U(s)` be at least as large as the value of every admissible completion of `s`. If one optimum is required, `U(s)≤L` permits exclusion. If every attaining candidate is required, equality can still contain needed answers; use `U(s)<L` for this bound-based exclusion and preserve the attaining alternatives.

For minimization, reverse the bound directions: a lower bound on every completion is compared with the cost of a known feasible candidate. A candidate score and a bound on all completions have different roles even when their numerical values coincide.

#### CMP.4:4.3 - Reuse consequences within their conditions

When a conflict occurs, identify which partial assignments and original conditions imply it. A smaller conflicting subset can exclude the same combination elsewhere, saving repeated discovery. Apply the learned consequence only where those conditions hold.

Keep its scope simple enough to use. A consequence of the fixed problem can be retained throughout that search. A consequence relying on a temporary assumption applies only under that assumption, unless the assumption is retained in the learned condition. After a constraint or domain change, revisit consequences depending on it.

An observation that a branch was unpromising can guide ordering. Turning it into an exclusion requires the corresponding all-completions argument or an explicitly weaker heuristic conclusion. This is particularly relevant when a learned model proposes branches or estimates their value.

#### CMP.4:4.4 - Choose the exploration order for the next useful result

Maintain the unprocessed partial states. Depth-first exploration retains relatively little state; an order based on bounds can tighten the remaining optimum range; a feasibility heuristic can obtain an incumbent early. Choose according to the result and resources needed now.

At each selected state, propagate applicable conditions, apply a useful exclusion, return or improve a complete admissible candidate, or generate covering extensions. A finite search space and complete processing support eventual exhaustion. In an infinite space, eventual discovery additionally depends on how branches are scheduled; repeatedly expanding one branch can leave an existing witness unvisited.

Compare the cost of an exclusion with the work it is likely to avoid. It can be rational to skip a difficult bound and explore the branch.

#### CMP.4:4.5 - Preserve the meaning of bounds during computation

A mathematical bound must retain its direction in the arithmetic that computes it. For a maximizing search, an upper bound rounded downward without justification may exclude a better answer. Conservative rounding, interval bounds or a justified rational calculation can preserve the exclusion. A score predicted by a model is an estimate unless a suitable bound property has been established.

Use stronger arithmetic or independent checking where an erroneous exclusion could alter a consequential result. Ordinary exploratory search can instead keep a borderline branch or report a qualified result. C.11.DUA selects that extra work by its possible effect on the receiving decision.

Keep a bound for the unprocessed work, including a state whose expansion is interrupted. For maximization with an incumbent `L`, the whole optimum is at most `max(L, max U(s))` over the states still pending. The incumbent supplies a lower bound. If a pending state lacks an upper bound, a finite global upper bound is not yet supplied by this account.

#### CMP.4:4.6 - Return the strongest result actually obtained

On finding a witness, return it with the meaning of its admissibility. For optimization, include its objective value and any remaining bound that the recipient needs. On complete exhaustion, sound exclusions and covering extensions justify optimality if a feasible answer was found, or absence of a feasible answer if none was found.

On interruption, return the available candidate and unresolved possibility. “No witness found within this run” is useful information but does not establish that no witness exists. If only a satisfactory candidate was requested, its obtaining can complete the work without exhausting the search.

Use an initial and changed-condition case to check which conclusion the recipient can actually use. Changing an output from one optimum to all optima, or changing a domain, directly tests the exclusion's scope.

### CMP.4:5 - Archetypal Grounding

#### CMP.4:5.1 - Select a best subset and interpret an interrupted search

Choose a subset of three items within capacity 5. Their `(weight,value)` pairs are `A=(4,7)`, `B=(3,5)` and `C=(2,3)`. Values and weights are positive integers. A partial state fixes which items are included or excluded; the next undecided item supplies the two covering extensions.

An initial candidate `{A}` is admissible with value 7. To bound the root, allow fractions of items. Filling by value per weight takes A and one third of B, giving `7+5/3=26/3`. To establish that this is an upper bound, let a, b and c be the selected fractions. For `0≤a,b,c≤1` and `4a+3b+2c≤5`,

`7a+5b+3c=(5/3)*(4a+3b+2c)+a/3-c/3≤25/3+1/3=26/3`.

The displayed fill attains the bound. Every integral subset is included in this relaxed set, so it too has value at most `26/3`. Since integral subset values are integers, 8 is also a valid upper bound.

If the run is interrupted here, it has established `7≤optimum≤8`, together with candidate `{A}`. It has not established optimality of A.

In the include-A branch, neither B nor C can also fit, so its best completion is A with value 7. In the exclude-A branch, B and C fit together and give 8. This meets the global upper bound, establishing that `{B,C}` is optimal. The algorithm obtained both a usable subset and a stopping reason.

**Changed output:** add an item `D=(5,8)` and ask for all optimal subsets. Once `{B,C}` has value 8, pruning a branch with upper bound 8 could lose the distinct answer `{D}`. Retain equality branches, or use a separate enumeration phase constrained to the established optimum value. The former “one optimum” exclusion answers a different request.

#### CMP.4:5.2 - Use a conflict, then revise its assumptions

Three tasks A, B and C must occupy slots 0 or 1. Every pair conflicts, so conflicting tasks must use different slots. After choosing `A=0`, propagation forces `B=1` and leaves C with no allowed slot. The branch is infeasible. Choosing `A=1` gives the symmetric conflict. Exhausting these two A choices proves that no assignment exists under these constraints.

If a third slot 2 becomes available, the earlier impossibility no longer applies. The construction `A=0, B=1, C=2` is feasible. An implementation reusing conflicts learned under the two-slot domain must retain or reconsider that domain assumption. Searching faster with an obsolete conflict would prevent the useful new answer.

### CMP.4:6 - Bias-Annotation

An early good answer can make unvisited alternatives seem irrelevant. That is a valid stopping choice when the recipient needs only a satisfactory candidate; it does not itself justify an optimum claim. Conversely, insisting on exhaustion can waste resources after further improvement no longer matters.

Examine a bound’s direction and scope. The relevant distinction is what the bound establishes about possible completions, including the arithmetic and assumptions used to obtain it.

### CMP.4:7 - Conformance Checklist

- Partial states have a stated meaning and their extensions cover the answers that must be retained.
- Each exclusion applies to every relevant completion represented by the omitted state.
- The use of equality, symmetry, dominance and duplicates matches the request for one answer, all answers or a count.
- The incumbent is admissible; each bound has the correct direction and computational support for its use.
- Learned consequences retain assumptions that limit their reuse.
- Interrupted work remains represented in the pending possibility, and the returned conclusion matches what was completed.
- Additional pruning or assurance work is chosen for its useful effect.

### CMP.4:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Exclude a branch because one completion failed | Another completion may work. Derive a conflict applying to the entire represented set or continue branching. |
| Use a predicted score as a bound | A better answer may be discarded. Keep the prediction as an ordering heuristic unless its bound property is established. |
| Prune ties while enumerating all optima | Distinct attaining answers disappear, as in the added-D case. Retain equality branches or use a separate complete enumeration. |
| Report interruption as impossibility | Unvisited alternatives remain. Return the candidate, remaining bounds and the limit on the conclusion. |
| Reuse a conflict after its domain changes | A newly feasible answer can be excluded. Reconsider the consequence with its original conditions. |

### CMP.4:9 - Consequences

The search can avoid large parts of a combinatorial space and still support a precise result. It can also supply a useful answer before completion, with the remaining possibility described at the strength actually established.

The method does not guarantee affordable search. Exclusions may be weak, expensive or scarce; the remaining space may still grow exponentially. A changed formulation, relaxation, shared subproblem or weaker requested conclusion can then be the next useful move.

### CMP.4:10 - Architectural Rationale

Coverage and exclusion are complementary: a complete branching scheme loses its guarantee if an unsupported pruning rule is added, while sound pruning cannot recover alternatives that the branching never represented. Exploration order is kept separate because it can improve time to a witness without changing which branches are valid to omit.

MATH.20 supplies the mathematical bound. CMP.5 constructs a relaxed problem that can provide one; CMP.3 can share repeated remaining questions. This pattern combines such contributions into the algorithmic construction and interpretation of search. C.40 concerns broader exploration and further problem development; its interests and stepping stones need not be reducible to a fixed search objective.

### CMP.4:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 2](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/02-backtracking.pdf) develops recursive exploration of choices. Adopt the separation between a partial choice, its extensions and the recursively obtained answer. The present synthesis adds the result-sensitive treatment of branch bounds, interrupted search and changed assumptions.

The primary report [*The SCIP Optimization Suite 10.0*](https://optimization-online.org/wp-content/uploads/2025/11/scipopt-100.pdf) describes current mathematical-programming search and a numerically rigorous mode combining rational and directed-rounding computation. Adopt its substantive lesson that a bound's mathematical direction must survive its computation. The additional cost and supported problem classes limit when that mode is appropriate. This pattern neither requires a solver certificate for ordinary search nor treats a floating-point estimate as an unconditional exclusion.

For :4.2–4.6, compare justified exclusions with simpler exhaustive exploration and heuristic ordering alone. A bound is useful when the branches it safely avoids repay the work of obtaining and maintaining it, or when its conclusion settles the task before exhaustion. If finding a satisfactory candidate is enough, cheap ordering can win without proving a stronger bound. Retain ordinary conservative arithmetic when it supports the required comparison; rational or directed-rounding machinery is useful only when its added cost buys a consequential warranted exclusion. Reopen this selection when the requested output, admitted assumptions, cost of bounds or evidence for their soundness changes. In particular, asking for every optimum changes the usefulness of equality bounds.

### CMP.4:12 - Relations

- **C.29.2:** states the wanted computational answer and its resource conditions.
- **CMP.2:** supplies recursive decomposition; **CMP.3** identifies repeated remaining subproblems and schedules their evaluation.
- **CMP.5 and MATH.20:** construct useful relaxed bounds and justify the corresponding inequalities.
- **MMP.10:** supplies the admissible problem when search serves a modeled subject question.
- **C.11.DUA:** guides the value of further exploration, stronger bounds or additional checking.
- **C.40:** supports the wider development of alternatives and problems, including situations in which the search space or objective itself is being changed.

### CMP.4:End
