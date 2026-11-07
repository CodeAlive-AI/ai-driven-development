## CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.11:1 - Problem frame

**Use this when** repeated attempts to accelerate a computation leave a question about what any algorithm could achieve under the available access. You can construct different admitted inputs that require different answers but remain indistinguishable before enough queries, comparisons, communication or stored information.

The gain is a lower bound tied to an explicit computational model, or a concrete change of access or requested answer that escapes that bound. This can stop fruitless optimization, reveal a needed index or observation, and separate an intrinsic restriction of the chosen model from a poor implementation.

The reader needs to follow the input family, allowed observations and the demanded answer. Counting, elementary probability or a mathematical adversary argument is used according to the branch. The adversary is a proof construction: it keeps several inputs consistent with what an algorithm has learned.

Use a known applicable bound directly when no new argument is needed. Timing one program establishes its performance, not a lower bound for every program. Undecidability through an effective reduction uses CMP.1; physical energy or transport limits use their physical formulation. The present method establishes computational information requirements under specified access.

### CMP.11:2 - Problem

How can one establish a minimum amount of computational work without enumerating every possible algorithm, and use the result without extending it beyond the model that made the proof valid?

An algorithm can make adaptive choices, preprocess data, exploit a promise or use randomization. A proof that ignores an allowed operation can forbid a procedure that actually works. A lower bound valid for a comparison model can disappear when keys have an accessible integer encoding.

### CMP.11:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Universal algorithm claim and bounded model | The proof must cover every admitted procedure without claiming more access restrictions than the task has. |
| Adaptive queries and remaining alternatives | Later queries depend on earlier answers, so the argument must survive that choice. |
| Strong answer and affordable observation | Exact identification can cost more than approximation or a promise-restricted decision. |
| Worst-case and expected cost | A hard input for each deterministic rule need not be one hard input distribution for randomization. |
| Preprocessing and online response | A cheap query can hide information acquired earlier. |
| Useful restriction and impossible-demand rhetoric | A bound should change construction or expectation, not merely declare the task hard. |

### CMP.11:4 - Solution

**Fix access and answer → construct indistinguishable alternatives → bound how fast observations separate them → respect the cost and error quantifiers → state the limit → change the assumption that constrains the work.**

#### CMP.11:4.1 - State the computational model and the claimed quantity

Specify the admitted inputs, promised structure, allowed queries or operations, prior information and required output. Count what the claim concerns: number of input probes, comparisons, transmitted bits, retained states, total time or another defined resource.

Include preprocessing and advice where they depend on the input. If preprocessing builds an index, distinguish its cost from a subsequent query's cost. An operation that reveals an entire vector is different from one that reads one bit, even if both are written as one function call.

State whether the bound concerns worst-case or expected cost, deterministic or randomized computation, and exact or error-tolerant answers. For randomization, say whether the error guarantee holds on every input and which randomness is available. These quantifiers determine the argument.

#### CMP.11:4.2 - Construct alternatives that the available observations have not separated

Describe a transcript: the sequence of queries and replies, or messages and observations, available to the procedure. Consider all inputs still consistent with it. If two of those inputs require incompatible answers, a deterministic procedure seeing that transcript cannot correctly finish on both.

Construct those alternatives rather than simply counting unknown data. For a bit query, place a decisive difference at an unread position. For a comparison algorithm, retain different orders compatible with the observed comparisons. For a communication or streaming algorithm, find different earlier inputs that lead to the same message or stored state but require different outputs after one common continuation.

Adapt the construction to the permitted answer. Distinct inputs do not need separate transcripts when the same answer is acceptable for both. A common approximation interval or permitted error can therefore weaken the lower bound.

#### CMP.11:4.3 - Turn indistinguishability into a resource bound

Use the form that fits the access:

- **Adversary:** answer queries while retaining incompatible possible inputs. Show how many queries are needed before no such pair remains.
- **Counting:** if each observation has at most b possible replies, q observations have at most `b^q` transcripts. If N input classes require mutually different outputs, then `b^q≥N`, giving `q≥log_b N` for a worst-case depth bound.
- **State or message collision:** with fewer than N distinguishable retained states or messages, two of N necessary input classes collide. A shared continuation then forces an error.

Establish that each constructed transcript is consistent with at least one admitted input. An adversary that combines incompatible answers proves nothing about the actual problem. A counting argument needs output-distinct classes, not merely many syntactically different inputs.

When an algorithm already provides an upper bound in the same model, compare the two. Matching orders of growth can establish asymptotic optimality for that model. A gap locates remaining room for a better construction or a stronger argument; it is not itself proof that the current algorithm is improvable.

#### CMP.11:4.4 - Handle randomization and average cost with their own argument

Fixing random choices gives a deterministic procedure, but its hard input may depend on those choices. That alone does not establish a bounded-error randomized lower bound on a fixed input.

One route chooses a distribution on inputs before the random choices. If every deterministic procedure within the allowed budget has error greater than δ under that distribution, averaging gives the same obstruction for any mixture of them. A randomized algorithm with error at most δ on every input would contradict it. Use the matching cost convention; a worst-case budget argument does not automatically establish a claim about expected budgets.

Another route couples runs on two inputs using the same random choices and bounds how often they see different observations. Section :5.1 applies this directly. A statistical or information inequality can supply a broader version when observation distributions overlap instead of agreeing exactly.

Keep quantum queries or stronger observation primitives outside a classical-query conclusion unless the proof actually covers them. Their admissibility is a model choice, not an implementation detail that can be ignored.

#### CMP.11:4.5 - Return the limit with a useful continuation

State the bound, input family, access, error and cost conditions together. Indicate whether it rules out the requested budget, establishes optimality within an order, or leaves a gap.

Identify a consequential escape: restrict the input by a defensible promise, allow a weaker answer or error probability, acquire an additional observation, preprocess and retain information, use a stronger primitive, or change the representation. Determine which premise of the lower-bound argument that change removes, then construct the new procedure.

Use C.11.DUA to decide whether proving a tighter bound or obtaining additional information would change the next move. A sufficient lower bound can already justify changing the task.

### CMP.11:5 - Archetypal Grounding

#### CMP.11:5.1 - Determine whether any bit is one

An unknown n-bit input is accessed one bit at a time. Return whether it contains a one. For a deterministic always-correct algorithm, answer zero to every query. Before all n distinct positions have been read, both the all-zero input and an input with a one at an unread position remain possible. Their correct answers differ. Therefore some input requires n queries. A complete scan attains that bound.

Allow a randomized algorithm that uses at most q queries on every run and errs with probability at most `δ<1/2` on every input. Couple its runs on the all-zero input and on the input with just position j set to one, using the same random choices. Unless the zero-input run queries j, both runs have the same transcript and output. Let `p_j` be the probability it queries j on the zero input. Consequently,

`P(output 1 on singleton j) ≤ P(output 1 on zeros)+p_j ≤ δ+p_j`.

Correctness on the singleton requires the left side to be at least `1-δ`, so `p_j≥1-2δ`. Summing over j gives

`q ≥ sum_j p_j ≥ n*(1-2δ)`.

For `δ=1/3`, this gives `q≥n/3`. It is a lower bound under the stated maximum-query convention, not a claim that every randomized algorithm uses exactly that many queries.

Now change the promise: either all bits are zero or at least half are one. Query k independently chosen uniform positions, returning one if any query finds it. On a nonzero promised input, the probability of missing every one is at most `2^-k`; zero inputs always receive the correct answer. For `0<δ<1/2`, choosing `k=ceil(log2(1/δ))` therefore achieves the error requirement independently of n, subject to generating and accessing those positions. For n>2, the singleton inputs used in the earlier bound are excluded. This explains why the new algorithm escapes that growth in cost.

#### CMP.11:5.2 - Bound comparison sorting and identify its escape

Sort n distinct opaque keys, with their order available only through pairwise comparisons. A comparison has two possible outcomes. The `n!` possible input orders require different output permutations, so a correct decision tree needs at least `n!` leaves. A binary tree of height q has at most `2^q` leaves. Thus the worst case needs at least `ceil(log2(n!))` comparisons, which grows as `Ω(n log n)`.

This bound is about comparison sorting. If each key is an integer in `0..K-1` and direct array indexing is an allowed elementary operation, count occurrences in K counters and emit keys in index order. That construction uses `O(n+K)` counter/access operations and corresponding output work. It escapes the comparison bound by observing the encoding through indexing. Large K, long integers or a requirement to preserve distinct record identity can change its storage and reconstruction costs.

A practical consequence is to compare representations and access before spending effort trying to make an ordinary comparison procedure sort arbitrary distinct keys in fewer than order `n log n` comparisons. If comparisons themselves are expensive, a matching comparison count still leaves their internal cost to reduce.

#### CMP.11:5.3 - Expose information hidden in a message

One agent has an n-bit string x and sends one fixed-length binary message to another agent holding y. The receiver must decide whether x=y with no error. If two different strings x and x' produce the same message, take the common receiver input y=x. The receiver sees identical information in both cases but must answer differently. All `2^n` strings therefore need distinct messages, requiring at least n bits. Sending x achieves it.

If public independent random masks and an error probability are admitted, the task changes. For each mask r, send the parity of the positions where both x and r are one; the receiver compares with its parity from y. Equal strings always match. For unequal strings, choose one differing position: toggling its independent mask bit pairs masks with opposite comparison outcomes, so the parities match with probability 1/2. After k independent masks, falsely accepting equality has probability `2^-k` and the message has k bits. The shared random masks and local parity-computation cost are explicit resources, not information transmitted by the message.

### CMP.11:6 - Bias-Annotation

The word “impossible” can obscure the condition that makes a lower bound true. Each example states an access model and then changes a premise to construct a different result. These are algorithmic limits; interpreting a computed object as a subject property and realizing operations physically remain separate questions.

### CMP.11:7 - Conformance Checklist

- Inputs, promises, observations, preprocessing and required outputs are specified.
- The cost and error claim has explicit worst-case, expected or probabilistic quantifiers.
- Indistinguishable alternatives are admitted inputs requiring incompatible answers.
- The adversary, counting or collision argument covers adaptive behavior allowed by the model.
- Randomized claims use an argument valid for randomization and the stated cost convention.
- The conclusion names both its restriction and a useful continuation or unresolved gap.

### CMP.11:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Generalize from a slow implementation | Another algorithm may avoid its work. | Prove a requirement for every admitted transcript or procedure. |
| Count distinct inputs without considering acceptable answers | Several inputs may legitimately share one output. | Count output-distinct classes. |
| Supply an inconsistent adversary | No actual input could produce its replies. | Retain a nonempty compatible input family. |
| Fix randomness, then choose a different hard input for each seed | This can miss a successful randomized algorithm. | Use one prior input distribution or a valid coupled argument. |
| Ignore input-dependent preprocessing or stronger access | The algorithm already acquired the supposedly missing information. | Charge or expose that resource and restate the model. |

### CMP.11:9 - Consequences

A failed search for a faster algorithm can become a specific limit or a more promising problem. The bound identifies which observations, distinctions or access restrictions determine the remaining cost and helps decide whether to optimize, reformulate or change the requested answer.

The conclusion is conditional. It can remain correct while a new representation, promise or randomization changes what is achievable in the practical task.

### CMP.11:10 - Architectural Rationale

Lower bounds complement construction by studying what a successful construction must distinguish. Transcript-based reasoning handles entire classes of algorithms because identical observed information forces identical deterministic behavior, or bounds the separation of randomized behavior.

The access model belongs in the claim because it determines the observations available. This connects computational complexity to representation and mathematical argument while avoiding an unsupported claim about every possible physical or organizational realization.

### CMP.11:11 - SoTA-Echoing

How can a performance limit cover procedures not yet invented? **Adopt** the decision-tree construction in [Morin's comparison-sorting analysis](https://opendatastructures.org/newhtml/ods/latex/sorting.html), in :4.2–4.3 and :5.2. It overcomes the limit of timing or analyzing only the current algorithm by counting distinctions every comparison procedure must make. Direct performance analysis remains the cheaper sufficient method when the question concerns only that implementation. A new access primitive, key promise or output requirement reopens the universal comparison claim.

For randomized access, **adopt** the explicit separation of deterministic, zero-error, bounded-error and expected-cost models in [Blais's *Randomized Complexity*, query-complexity treatment](https://cs.uwaterloo.ca/~eblais/cs860/w25/queryseparations), for :4.1 and :4.4. The coupled proof in :5.1 supplies its own bound rather than transferring a deterministic adversary unchanged. A direct coupling is lighter than a general minimax argument when it settles the limit; an input-distribution or stronger information method is useful when the simple pair does not. Changed promises, error or cost quantifiers reopen that selection.

The same course's [communication-complexity treatment](https://cs.uwaterloo.ca/~eblais/cs860/w25/communication), following Rao and Yehudayoff's 2020 account, supplies the transcript and public-randomness distinction adapted in :5.3. A full string is the simple zero-error choice; random parity accepts bounded error to reduce communication while retaining local computation and shared randomness. A changed requirement for zero error, private randomness or adaptive adversarial inputs changes the comparison.

### CMP.11:12 - Relations

- **MATH.19 and MATH.20:** supply argument construction and bounds.
- **CMP.1:** transfers algorithms or impossibility through effective reductions; this method derives a limit directly from available information.
- **CMP.9:** constructs random operations and their probability qualifications.
- **CMP.10:** changes representation, access and preprocessing while retaining the required answers.
- **C.29.2:** states the computational problem and cost model; **C.29.3 and PHY.3** address physical realization and physical limits separately.
- **C.11.DUA and C.40:** support choosing further argument, another resource or a changed problem when the bound changes the development direction.

### CMP.11:End
