## CMP.2 - Derive a Recursive Procedure from a Problem Decomposition

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.2:1 - Problem frame

**Use this when** you can state the answer required from a finite input, but a procedure for obtaining it is missing or unaffordable. Parts of the task resemble the whole, or a transformation produces another instance whose answer could help. You need to choose those subproblems and determine what they must return.

An engineer, researcher or AI agent may recognize a recursive formula yet be unable to turn an unfamiliar problem into one. A common difficulty appears at recombination: each part returns a correct answer to its own question, but those answers omit information needed for the whole. Another appears at progress: a call changes its input without bringing computation closer to a return.

The gain is a recursive procedure with usable base cases, a reason its calls return, a justified way of combining their results and an initial account of its cost. The reader needs to follow finite case distinctions, functions and a simple inductive argument. MATH.4 can supply that argument; C.29.2 supplies the relation between a computational answer and the question it is meant to settle.

Use a suitable existing procedure directly when it already answers the question within the available resources. This method develops recursion for obtaining a finite answer. A server, stream or other intentionally continuing process needs a progress condition appropriate to that behavior.

### CMP.2:2 - Problem

How can one discover a recursive algorithm whose subproblems are obtainable, whose answers suffice to reconstruct the requested result, and whose unfolding has an acceptable cost?

Choosing a familiar equation or writing a self-call does not settle those questions. The designer must connect the meaning of a subproblem to the operation that uses its answer.

### CMP.2:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Small subproblems and sufficient answers | A short returned value can omit the boundary information needed for recombination. |
| Natural structure and useful decomposition | Following input syntax makes some arguments easy; a different split may reduce work or expose the needed result. |
| Generality and effective choice | A mathematical existence argument can leave the next branch or object unavailable to computation. |
| Progress and branching | Every call may become smaller while their number grows too quickly. |
| Simple cost model and actual representation | Counting additions can hide copying, growing integers or expensive access. |
| Reuse and changed questions | A summary adequate for one result may discard information needed by a later result. |

### CMP.2:4 - Solution

**State the answer → propose smaller questions → derive the join → strengthen what must be returned → establish return → compare the work.**

#### CMP.2:4.1 - Fix the question and the available operations

Describe an input `x`, the information available about it, and what a returned answer must allow its recipient to do. Asking for an optimum value, one attaining object, or every attaining object gives different result requirements. State the empty and degenerate cases when they belong to the input family.

List the operations that can actually be performed on this input: inspect a constructor, split an interval, compare keys, compute a remainder, test a condition, or call a supplied procedure. A proposed step such as “choose the correct partition” remains a construction task until the partition can be obtained.

For example, maximum segment sum on a sequence of integers asks for a contiguous nonempty segment with largest sum. Returning its sum answers a value query; locating the segment also requires endpoints. Permitting the empty segment changes the base case and the answer on an all-negative input.

#### CMP.2:4.2 - Choose a decomposition by asking how answers would join

Take a representative input and suppose that selected smaller questions have been answered correctly. Try to construct the answer for this input from those returned values. This local design question avoids having to unfold the entire recursion while inventing it.

Useful proposals include removing one element, splitting into balanced parts, following the constructors of a structured input, or transforming the input while decreasing another measure. The last case includes Euclid's replacement of a pair by a divisor and remainder. Input size need not decrease in every component.

For each proposal, account for every form a valid answer can take. If a sequence is split into left and right parts, an optimal contiguous segment lies wholly on one side or crosses the boundary. The crossing case shows what the two recursive answers must supply.

Keep the proposal that makes the join both justified and obtainable. If the only available join searches the original problem again, change the subproblem question, retain more information, or try another decomposition.

#### CMP.2:4.3 - Strengthen the returned result when the join needs more

Write the join using named values. Each value must come from the input, a smaller answer or an available local operation. A missing value identifies a specific revision of the subproblem, rather than a reason to discard recursion as a whole.

For maximum segment sum, the best segment on each side is insufficient: a crossing segment uses a suffix of the left side and a prefix of the right. Let each nonempty part return four quantities:

- `T`: the sum of the whole part;
- `P`: the largest sum of a nonempty prefix;
- `S`: the largest sum of a nonempty suffix;
- `B`: the largest sum of a nonempty contiguous segment.

For a left summary `L` and right summary `R`, construct:

```text
T = L.T + R.T
P = max(L.P, L.T + R.P)
S = max(R.S, R.T + L.S)
B = max(L.B, R.B, L.S + R.P)
```

The alternatives in each maximum come from the possible locations of the corresponding segment. To return an actual segment, carry the endpoints attaining each selected prefix, suffix and best segment. Choose a consistent rule for ties when only one witness is wanted.

This is the algorithmic use of strengthening an inductive result in MATH.4. The additional design decision is what summary enables an affordable join for the chosen problem decomposition. Further questions may require a different summary.

#### CMP.2:4.4 - Supply base cases and a decreasing measure

Give a direct result for each case on which recursion stops. Then show that every recursive call reaches such a case after finitely many steps. A nonnegative integer that strictly decreases is often enough. A finite input constructor or a well-founded ordering can supply the same argument when one numerical size is awkward.

For the segment procedure, a singleton `v` returns `(v,v,v,v)`. Split every longer interval into two nonempty shorter intervals. Its length decreases along every call path. This also explains why an empty interval needs its own convention or must be excluded before calling the procedure.

For nonnegative integers with `b>0`, Euclid's call `(a,b) → (b,a mod b)` decreases the second component because `0≤a mod b<b`. The first component may increase relative to its old value; it is the selected measure that must decrease. At `b=0`, return `a`, with the intended convention for `(0,0)` fixed separately.

When a termination checker fails, inspect which decrease is absent from its account. A supplied difference, lexicographic measure or invariant may express the progress already present in the procedure. If progress is genuinely missing, repair the procedure or weaken its claimed result. A small successful run alone does not establish return on every allowed input.

#### CMP.2:4.5 - Establish the result and expose its computational cost

Use the base and smaller-call assumptions to establish the returned property. Recombination must work for every smaller answer allowed by its specification, including the selected tie behavior. When deriving a program from an existing proof, MATH.12 recovers the operations hidden in that proof.

Count the subcalls and local work. A recurrence for mathematical values and a recurrence for computational cost answer different questions. For balanced segment splitting with interval views, constant-cost arithmetic and the four-value join, the work satisfies `W(n)=W(floor(n/2))+W(ceil(n/2))+O(1)`, giving `O(n)` operations. Sequential depth-first evaluation retains `O(log n)` summaries on its call stack. Copying each subarray instead adds work at each level; growing integer values also change the cost per addition.

If equal subproblems recur, CMP.3 can identify and share them. If the decomposition generates alternatives that can be ruled out, CMP.4 can construct those exclusions. If representation dominates the cost, compare the access and update operations before replacing the mathematical construction.

#### CMP.2:4.6 - Use the result and revisit the assumption that changed

Run a small case through the complete procedure, including the use of its returned answer. Change one condition that stresses the construction: empty input, a boundary case, a different output request or a resource limit. Follow the affected base, join and progress arguments.

The result may be a working procedure, an unaffordable but informative construction, or a located missing operation. Use that difference to choose the next algorithmic move. Formal proof or additional testing is chosen for the uncertainty that matters to the receiving use.

### CMP.2:5 - Archetypal Grounding

#### CMP.2:5.1 - A join that initially loses the answer

For `[-2,3,-1,4,-5]`, split into `[-2,3,-1]` and `[4,-5]`. Their best sums are 3 and 4. Keeping only those values would miss the crossing segment `[3,-1,4]`, whose sum is 6.

The strengthened summaries are `L=(0,1,2,3)` and `R=(-1,4,-1,4)`, ordered as `(T,P,S,B)`. The join yields `(-1,4,1,6)`. With attaining endpoints retained, it returns the segment from the second through fourth element. The user can now obtain the segment rather than merely knowing its value.

**Changed condition:** suppose the wanted segment may contain at most two elements. The former crossing winner has length three. The four maxima have discarded the sums of shorter candidate suffixes and prefixes. Add prefix and suffix results indexed by permitted length, combine only lengths whose sum is at most two, and keep the same restriction on internal best segments. In this case the answer becomes 4, attained by `[4]`. For a general limit `k`, a straightforward join over length pairs costs `O(k²)`; the resource consequence can justify a different algorithm. Reusing the old four-value join would silently answer the earlier question.

#### CMP.2:5.2 - A subproblem obtained by a transformation

To compute `gcd(48,18)`, replace the pair by `(18,12)`, then `(12,6)`, then `(6,0)`, and return 6. The equality `gcd(a,b)=gcd(b,a mod b)` follows because a common divisor of either pair divides both entries of the other pair. The remainder operation and decreasing second component turn that equality into a returning procedure.

If the next use also needs coefficients `u,v` with `u*a+v*b=gcd(a,b)`, the returned number alone is insufficient. Suppose the smaller call supplies `d=u'*b+v'*r`, with `r=a-q*b`. Substitution gives `d=v'*a+(u'-q*v')*b`; return the updated coefficients too. For the original pair, `6=(-1)*48+3*18`. The same recursive decomposition supports a stronger output through a changed join.

### CMP.2:6 - Bias-Annotation

Familiar syntax can make one decomposition appear inevitable. Compare its join and cost with another plausible decomposition when those differences can change the choice. Conversely, an elegant asymptotic bound can hide operations that the actual representation makes expensive.

A successful example demonstrates the construction and can expose a missing case. The general result depends on the base, joining and progress arguments, with any additional assurance selected for the actual use.

### CMP.2:7 - Conformance Checklist

- The input and wanted result distinguish a value from any witness or continuation information that is needed.
- Each subproblem is constructible from available data, and its returned specification supplies the join.
- The base cases cover the stopping situations; every recursive path has the stated progress toward one of them.
- The join preserves the answer property, including boundaries and the chosen treatment of ties.
- The cost account includes branching, recombination and representation costs material to the decision.
- A changed requirement is followed through the returned information and affected clauses before the procedure is reused.

### CMP.2:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the method | Consequence and repair |
| --- | --- |
| Return only the final scalar from each part | The segment example loses crossing answers. Derive the join and retain the boundary summaries it consumes. |
| Treat a changed input as a smaller input | Calls can continue indefinitely. State a well-founded decrease and check every recursive branch against it. |
| Treat termination as affordability | An exponential call tree can terminate correctly. Count calls and local work; share repeated subproblems when useful. |
| Keep the old summary after changing the question | A length constraint or witness request can be lost. Reconstruct what the new join needs and revise the affected result. |

### CMP.2:9 - Consequences

The method makes recursive algorithm design available as a sequence of inspectable choices. It exposes a useful link between mathematical construction and algorithmics: strengthening what a subproblem returns can make a previously unavailable or costly computation possible.

The resulting algorithm need not be the fastest one. Its explicit subproblem and join create opportunities for sharing, new representations, parallel execution or replacement by another algorithm. Those improvements retain their own correctness and resource questions.

### CMP.2:10 - Architectural Rationale

Subproblem meaning, recombination, progress and cost belong together because changing one can force a change in the others. Starting from a recursive syntax would obscure the discovery of the required question and summary. Starting from an induction proof alone can leave the effective decomposition and cost unresolved.

MATH.4 supplies witness construction by induction; MATH.12 supplies extraction from a proof. This pattern constructs and compares recursive obtaining procedures, including decompositions that do not follow the input's constructors. CMP.3 changes how repeated calls are evaluated without silently changing what they ask. C.29.2 retains the common computational formulation and its connection to the receiving question.

### CMP.2:11 - SoTA-Echoing

[Erickson, *Algorithms*, chapter 1](https://jeffe.web.engr.illinois.edu/teaching/algorithms/book/01-recursion.pdf) develops recursion through reductions to simpler instances and separate correctness and running-time arguments. This remains a useful foundational construction line. Adopt the local design question about a correct smaller answer; adapt it by making the information required at the join explicit and testing a changed output request. A remembered recurrence alone supplies less help when the decomposition itself is missing.

For the construction in :4.2–4.5, an available recurrence or input-structural split is the simpler alternative when it already returns enough information for the join and meets the cost requirement. Strengthening a subanswer is worth its extra work when that simpler return loses the requested result, as the four-value segment construction and coefficient-returning divisor procedure demonstrate. Reconsider this choice when a different output, representation or competing decomposition changes either sufficiency or total cost.

The current [Lean reference on recursive definitions](https://lean-lang.org/doc/reference/latest/Definitions/Recursive-Definitions/) distinguishes structural recursion, well-founded measures and forms of partial or continuing behavior. Adopt the distinction between a missing syntactic decrease and an absent termination argument. Formal encoding can check a consequential or difficult construction; its additional work is unnecessary for simply exploring a decomposition.

### CMP.2:12 - Relations

- **C.29.2 - Computational Formulation:** supplies the requested computational result, elementary operations and connection to use.
- **CMP.1:** supplies reuse through an effective reduction; recursion constructs the repeated same-family reduction and its return.
- **MATH.4 and MATH.12:** supply inductive construction and the obtaining operations recoverable from proof.
- **CMP.3:** shares repeated calls and chooses their evaluation and storage; **CMP.4** handles exclusions among alternative extensions.
- **MATH.20:** supplies bounds used when comparing cost or consequences. The general resource and portfolio methods choose among the constructed alternatives.

### CMP.2:End
