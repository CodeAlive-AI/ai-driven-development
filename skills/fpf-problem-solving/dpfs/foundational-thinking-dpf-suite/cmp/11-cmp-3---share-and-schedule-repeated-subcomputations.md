## CMP.3 - Share and Schedule Repeated Subcomputations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.3:1 - Problem frame

**Use this when** a procedure repeatedly obtains the same intermediate answer, or retains so many intermediate values that it cannot finish within the available memory. You need to determine which work can be shared, when to perform it, and what to retain for later use.

The situation occurs in dynamic programming, symbolic evaluation, database computations, program analysis and differentiation of computational graphs. The repeated unit is a subcomputation with stated inputs and a needed result. Similar-looking calls may still require different answers because their data, assumptions or effects differ.

The gain is an evaluation procedure that performs less repeated work or fits the available storage while preserving the requested answer. The reader needs to understand a function call and a directed dependency graph; the graph is explained here as a set of intermediate results with arrows from each prerequisite to its consumer. CMP.2 can supply the original recursive procedure.

Direct recomputation is often best for a cheap, seldom-repeated operation. Apply this method when sharing or storage choices can change the feasibility or cost of the computation. A changing environment requires the meaning of reuse to be established before previous results are used.

### CMP.3:2 - Problem

How can repeated computations be identified and reorganized without merging cases that need different answers, using an evaluation order and storage policy that support the requested result?

“Cache the answer” leaves three questions open: what counts as the same question, which answers must already be available, and whether the retained information suffices for the eventual output.

### CMP.3:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Sharing and distinctions | A coarse reuse key saves work but can conflate different continuations. |
| Demand and predictable order | Computing only requested states avoids unused work; a regular order can simplify access and scheduling. |
| Time and storage | Retaining values avoids computation but can exhaust memory or increase data movement. |
| Value and witness | A small working table can retain the optimum value while losing the path attaining it. |
| Reuse and change | An answer remains usable only while the data and conditions on which it depends still apply. |
| Mathematical equality and execution effects | Repeating a pure calculation and repeating an observation or state change can produce different behavior. |

### CMP.3:4 - Solution

**Name the repeated question → retain its determining information → expose dependencies → choose evaluation order → choose retained values → recover the required output.**

#### CMP.3:4.1 - State what a subcomputation means

Describe the result of one subcomputation as a function of its inputs and fixed environment. Include every condition that can change the returned answer or its use. A pair of sequence indices identifies an edit-distance subproblem only within specified sequences, edit operations and costs.

For optimization, distinguish the best remaining value from accumulated cost already incurred. If two histories lead to the same remaining problem but have different past costs, share the remaining answer and combine it with each history's cost. Merging the complete histories may lose a better total. When history changes the allowed future choices, retain that history information in the state.

This question is also useful before an implementation exists: identify the small family of questions that many possible constructions would ask. A recursion tree can then be designed around those questions instead of optimized after the fact.

#### CMP.3:4.2 - Define reuse by the answer the continuation needs

Choose a representation of subproblem identity, often called a key. Equal keys must imply interchangeable answers for the intended continuation. The key can contain input values, an immutable object's identity, a data revision, parameters and relevant assumptions. A cache local to one fixed computation may keep some of these implicit in its scope.

MATH.2 supplies the reasoning behind an identification: the operation used after identification must give the same required result whichever representative was used. An implementation also needs an effective way to recognize the keys. A hash narrows candidates; resolve collisions before treating different data as identical.

Distinguish completed answers from computations that have merely begun. Reading an unfinished entry as a result can introduce circular reasoning. In parallel evaluation, decide whether repeated demand waits for one producer or safely computes another copy; preserve the meaning of completion in either case.

For an operation with effects, state what reuse preserves. Replacing two reads of a changing sensor by one stored reading changes the observation sequence. Repeating a random draw and reusing one sample changes dependence. Sharing a pure calculation on an already obtained reading or sample can be valid. Select the intended operation before choosing the reuse rule.

#### CMP.3:4.3 - Construct the dependency graph and an evaluation order

For each distinct subproblem, identify which other results are needed to obtain its answer. Make the direction from prerequisite to consumer explicit. Count distinct states and the work needed to combine each state's prerequisites and alternatives; the number of states alone does not establish the total cost.

If dependencies are acyclic, two standard constructions are available:

| Construction | How it obtains results | Useful condition |
| --- | --- | --- |
| Memoized evaluation | On a call, return a completed stored answer if present; otherwise obtain prerequisites, compute the result and store it. | Only part of the possible graph is expected to be reached. |
| Ordered table evaluation | Obtain a topological order, in which prerequisites precede their consumers, and compute states in that order. | The needed state region and dependency order are known and regular access helps. |

These methods can be combined by regions. Independent ready states can also be evaluated concurrently, provided the sharing and combination operations preserve the result.

A directed cycle prevents this simple ordering. Determine whether it is an erroneous recursive dependency, a finite-horizon problem missing its horizon coordinate, or a genuine fixed-point problem. For a genuine cycle, provide the iteration, ordering or other solving method and its result conditions. Adding memoization alone does not solve mutually dependent equations.

#### CMP.3:4.4 - Retain what remains live, and recompute selectively

A value is live while a later operation will need it and cannot obtain it more cheaply by another means. Find its last planned consumer. After that use, the storage can be reused unless the requested final output needs the value for reconstruction.

Compare full retention, a moving set of recent values, and selected stored checkpoints from which intervening work is recomputed. Include key storage, lookup, copying, arithmetic size and transfer costs when they can change the choice. The mathematical dependency graph can be unchanged while these execution costs differ substantially.

Recomputation must reproduce the needed value from retained inputs and conditions. If it repeats an external effect or uses changed data, its meaning needs separate treatment. A stored checkpoint is useful only if it contains enough information to restart that part of the computation.

#### CMP.3:4.5 - Recover the value, witness or continuation actually requested

For each return, ask what the recipient must obtain. A dynamic program may return only an optimum value, one attaining sequence of choices, a count, or all attaining sequences. Store a selected predecessor when one witness is required, retain all relevant alternatives when their multiplicity matters, or provide an additional reconstruction procedure.

A small table is not automatically a complete answer. Sometimes an extra pass or a recursive split reconstructs a witness using less storage than retaining all predecessors. Include that work in the cost comparison.

When inputs or requirements change, identify the affected dependencies. Invalidate or recompute their consumers, or show that the changed information cannot alter those results. Choose the simplest reuse boundary that pays for itself; rebuilding a small calculation can be cheaper than maintaining fine-grained dependencies.

#### CMP.3:4.6 - Compare the resulting procedure with the original

Evaluate one complete use under both procedures and follow a changed condition that can break the proposed identification or storage policy. Check returned content as well as operation counts. The method's result is the changed computation and its resource consequence.

Use C.11.DUA when deciding whether another measurement, argument or experiment would change the choice. A theoretical bound can guide an initial implementation; actual resource observations can select among alternatives whose constant factors or memory behavior matter.

### CMP.3:5 - Archetypal Grounding

#### CMP.3:5.1 - Obtain a sequence-editing answer without expanding repeated calls

Let `D(i,j)` be the smallest number of unit-cost insertions, deletions and substitutions transforming the first `i` characters of fixed sequence `A` into the first `j` characters of fixed sequence `B`. Matching characters cost zero. Then:

```text
D(0,j) = j
D(i,0) = i
D(i,j) = min(D(i-1,j)+1,
             D(i,j-1)+1,
             D(i-1,j-1) + (0 if A[i]=B[j] else 1))
```

Here character positions start at 1. Each alternative identifies the last edit or match. Removing it leaves the corresponding smaller problem; adding it to a best smaller answer supplies a candidate for the whole prefix. Thus the minimum covers the possible last steps.

Naively unfolding this recurrence repeatedly requests the same prefix pairs. Within one fixed pair of sequences and one cost rule, use `(i,j)` as the key. Dependencies have smaller `i+j`, so increasing rows and then columns gives a valid order.

For `A=CAB` and `B=AB`, the complete table is:

| Prefix of A | Empty | A | AB |
| --- | --- | --- | --- |
| Empty | 0 | 1 | 2 |
| C | 1 | 1 | 2 |
| CA | 2 | 1 | 2 |
| CAB | 3 | 2 | 1 |

The result is 1; deleting the initial C attains it. There are `(m+1)(n+1)` states for lengths `m,n`, with constant work per interior state under constant-cost character comparison and small-integer arithmetic. Full retention uses `O(mn)` cells. If only the distance is required, the preceding and current row suffice, giving `O(n)` working cells.

**Changed output:** the recipient now needs an edit script. The final distance and two surviving rows do not supply the deleted path. One repair stores a minimizing predecessor for each cell and traces back from `(m,n)`. Another computes forward and backward costs to a middle row, chooses a column minimizing their sum, and recursively reconstructs the two halves. Every edit path crosses that row, which justifies the split. This second construction exchanges recomputation for storage; CMP.2 supplies the recursive decomposition. Neither choice alters the meaning of an allowed edit.

**Changed reuse scope:** for `A=CB`, `B=AB`, the value at `(2,2)` is 1; for `A=CA`, `B=AB`, it is 2. A global cache keyed only by `(i,j)` would conflate them. Restrict the cache to a fixed input pair or include the input identity and relevant conditions.

#### CMP.3:5.2 - Share an expression while preserving its interpretation

For `f(x,y)=(x+y)*(x+y)+(x+y)`, build one node `t=x+y` with three uses, then obtain `t*t+t`. With `x=2,y=3`, the result is 30. This replaces three additions of `x+y` by one and shares its stored value until the final addition.

If `y` changes to 4, `t` and its consumers must change; the result becomes 42. If each occurrence instead meant “read the next measurement and add x,” the shared expression would change the computation's meaning. The subproblem must be a fixed pure addition of supplied values for this identification to hold.

In differentiation of a longer expression graph, intermediate values may be needed again in reverse order. Keeping all of them can exceed memory. Retain selected restart values and recompute intervening pure operations when needed, comparing the extra work with reduced storage. This applies the same method to a different receiving algorithm.

### CMP.3:6 - Bias-Annotation

Visible repetition can encourage indiscriminate caching. The profitable unit may instead be a larger common subproblem, or no shared unit at all when lookup costs dominate. A small count of stored cells can also hide large objects, metadata and movement between memory levels.

Results obtained from fixed data invite overgeneralization to changing environments. State where a key's omitted parameters are held fixed, and revisit that boundary when the result is reused elsewhere.

### CMP.3:7 - Conformance Checklist

- The repeated question and its determining data are recoverable from the key and its stated scope.
- Equal keys justify the required reuse, including relevant effects, randomness and changed inputs.
- Dependencies determine an evaluation order, or a separate method resolves the genuine cycles.
- Completed results are distinguished from work still being evaluated.
- Storage and recomputation choices preserve the final value, witness or continuation that is required.
- The resource comparison counts relevant transitions, arithmetic, access and storage as well as states.
- The changed-condition use follows the dependency or output requirement that actually changed.

### CMP.3:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Key a subproblem by its position across changing inputs | The edit-distance example reuses an answer to another question. Bind the key to the input and conditions or narrow the cache's lifetime. |
| Treat an in-progress entry as an answer | A cyclic dependency can return unsupported content. Keep completion explicit and supply the appropriate cycle-solving method. |
| Discard predecessors while promising a witness | The optimum value remains but the attaining object cannot be returned. Retain choices or construct a reconstruction pass. |
| Share effects as if they were pure calculations | Observations, updates or random dependence can change. Identify the fixed data calculation that is actually interchangeable. |

### CMP.3:9 - Consequences

Many repeated call trees become a much smaller graph of distinct questions. Evaluation order and retention become design choices, making time, memory and output reconstruction comparable.

The transformation creates responsibilities for identity and change. Its benefit depends on repetition, graph size and access costs; a dependency graph can itself be enormous. A correct shared computation can still be unaffordable, which may call for a changed representation, approximation or problem formulation.

### CMP.3:10 - Architectural Rationale

Identity, dependencies, evaluation and lifetime form one method because changing the result being shared can alter all four. Separating “add a cache” from the required continuation would hide the main correctness question. Including selective recomputation prevents storage minimization and computation minimization from being treated as the same objective.

The mathematical identification is supplied by MATH.2, the subproblem construction by CMP.2, and common computational formulation by C.29.2. This pattern supplies the algorithmic reorganization. It can serve numerical, symbolic and learning procedures.

### CMP.3:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 3](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/03-dynprog.pdf) develops memoization, deliberate evaluation order, space saving and reconstruction of sequence-editing answers. Adopt the progression from a meaningful recurrence to distinct subproblems and their evaluation. Extend the identity question explicitly to changing inputs and effectful operations. The CAB example is a small independent derivation of that general design approach.

[Hirschberg's linear-space reconstruction](https://ics.uci.edu/~dhirschb/pubs/p341-hirschberg.pdf) is a historical but still useful counterexample to the assumption that reconstructing a sequence requires retaining a complete table. Its middle-split method also applies to edit paths. Adopt reconstruction as a choice between storage and additional calculation; do not claim its cost is optimal for every input representation or modern machine.

Current [JAX checkpointing documentation](https://docs.jax.dev/en/latest/gradient-checkpointing.html) shows the same storage/recomputation choice in automatic differentiation. Adopt its substantive distinction between saved intermediates and recomputed pure operations. Compiler behavior and hardware costs affect the best schedule; a particular library interface is an example of realization rather than a prerequisite of this method.

The working choice in :4.3–4.5 is between retaining all needed intermediate answers, recomputing them when requested, and retaining selected answers from which others can be reconstructed. Full retention is simpler when memory is ample and reconstruction would dominate. Recalculation avoids maintaining entries whose results are cheap or rarely reused. Selective retention pays extra scheduling or reconstruction work when it preserves the required answer under a tighter memory limit; the edit-script construction supplies one such choice. Reconsider it when effects change which calls can be shared, the recipient needs a different witness, readout costs change, or a competing reconstruction method improves the same resource trade-off.

### CMP.3:12 - Relations

- **CMP.2:** constructs the subproblems and their combination; this method changes how repeated questions are evaluated.
- **MATH.2:** supplies identification under operations; **A.3.3** helps restore state information when equal retained states allow different continuations.
- **C.29.2:** supplies computational result and resource conditions. **C.29.3** applies when realization changes the relevant execution assumptions.
- **MMP.8:** supplies information restrictions for adaptive choices; a computation used to obtain such a policy must preserve the observations and history on which its choices depend.
- **C.11.DUA:** selects additional checking or measurement for a decision that could change, including the value of further optimization.

### CMP.3:End
