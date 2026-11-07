# Computational Thinking DPF

**DocID:** `CMP` within **FPF Library**.

> A pattern language for constructing, understanding, analyzing and transforming algorithms, including their interpretation and interaction.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 24 October 2026
- **Status:** Eternal alpha: a repertoire open to correction and extension.
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Cited sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Computational Thinking here means algorithmics within computer science: reasoning about effective ways to obtain and transform representations and to maintain required behavior. Begin with what the work needs to obtain or do, even when no algorithmic problem has yet been recognized. The Readme shows how to enter that inquiry. The Architectural Reference explains computation, its grounds, and how the methods work together; the Table of Contents gives direct entries to their complete constructions. A description can itself be an input to an interpreter, translator, analyzer or learner. A useful computation can return an answer or continue responding to an environment.

The reference code **CMP** names this DPF. Its numbers are stable pattern addresses; § shows position within a Part. Numerical algorithms are one application alongside symbolic, discrete, randomized and learning procedures. A computing device enters when its operations or physical limits matter to the algorithm or its realization.

This publication belongs to the [Foundational Thinking DPF Suite](../_index.md). Its [Reference (Foundational)](../suite-reference/_index.md) explains the mathematical, physical, computational and methodological connections. References such as C.29.2 and B.5.MPC name patterns in [FPF Core](../../../sections/03-first-principles-framework-readme/_index.md). Open a supplier when its contribution is needed; revisit a receiving conclusion when that contribution changes.

To cite this edition: Anatoly Levenchuk, *Computational Thinking DPF*, [FPF Library repository](https://github.com/ailev/FPF). Include the version date shown above.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Computational Thinking - Readme](_index.md#computational-thinking---readme) | Follow worked connections between algorithmic methods. |
| Architectural Reference | [Computational Thinking DPF Architectural Reference](_index.md#computational-thinking-dpf-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| CMP.Reference:1 | [Problem frame and the algorithmic difficulty](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md) |  |
| CMP.Reference:1.1 | [A description specifies a family of possible processes](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference11---a-description-specifies-a-family-of-possible-processes) |  |
| CMP.Reference:1.2 | [Mathematical, physical and algorithmic grounds cooperate](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference12---mathematical-physical-and-algorithmic-grounds-cooperate) |  |
| CMP.Reference:1.3 | [Build a whole, introduce a level, and generalize deliberately](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference13---build-a-whole-introduce-a-level-and-generalize-deliberately) |  |
| CMP.Reference:1.4 | [Descriptions can be computed with, and ways can be obtained](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference14---descriptions-can-be-computed-with-and-ways-can-be-obtained) |  |
| CMP.Reference:1.5 | [A computation can be part of a larger computational practice](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference15---a-computation-can-be-part-of-a-larger-computational-practice) |  |
| CMP.Reference:1.6 | [Use the grounds to choose and revise a method](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md#cmpreference16---use-the-grounds-to-choose-and-revise-a-method) |  |
| CMP.Reference:2 | [Forces that shape the construction](02-cmp-reference-2---forces-that-shape-the-construction.md) |  |
| CMP.Reference:3 | [The methods and their connections](03-cmp-reference-3---the-methods-and-their-connections.md) |  |
| CMP.Reference:3.1 | [Construct an algorithm](03-cmp-reference-3---the-methods-and-their-connections.md#cmpreference31---construct-an-algorithm) |  |
| CMP.Reference:3.2 | [Control error and computational cost](03-cmp-reference-3---the-methods-and-their-connections.md#cmpreference32---control-error-and-computational-cost) |  |
| CMP.Reference:3.3 | [Interpret, transform and compose computations](03-cmp-reference-3---the-methods-and-their-connections.md#cmpreference33---interpret-transform-and-compose-computations) |  |
| CMP.Reference:3.4 | [Constituent actions in ongoing work](03-cmp-reference-3---the-methods-and-their-connections.md#cmpreference34---constituent-actions-in-ongoing-work) |  |
| CMP.Reference:4 | [Worked connection - One best selection becomes every best selection](04-cmp-reference-4---worked-connection---one-best-selection-bec.md) |  |
| CMP.Reference:5 | [Use checks, assumptions and recurring failures](05-cmp-reference-5---use-checks-assumptions-and-recurring-failu.md) |  |
| CMP.Reference:6 | [Consequences and Architectural Rationale](06-cmp-reference-6---consequences-and-architectural-rationale.md) |  |
| CMP.Reference:7 | [Shared sources, alternatives and relations](07-cmp-reference-7---shared-sources-alternatives-and-relations.md) |  |

## Part A - Construct an algorithm

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)](09-cmp-1---solve-one-problem-through-another-or-transfer-a-limi.md) | Stable | reduction; solver reuse; input conversion; answer recovery; computability; complexity. Can this problem be solved through another one, and in which direction does a limit transfer? | C.29.2 for the required answer and computational model; MATH.17/.18 for composition and interpretation. |
| 2 | [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](10-cmp-2---derive-a-recursive-procedure-from-a-problem-decompos.md) | Stable | recursion; decomposition; induction; sufficient return; termination. What must smaller problems return so that their answers construct the required whole? | MATH.4/.12 for inductive or extracted constructions; C.29.2 for the computational formulation. |
| 3 | [CMP.3 - Share and Schedule Repeated Subcomputations](11-cmp-3---share-and-schedule-repeated-subcomputations.md) | Stable | memoization; dynamic programming; sharing; dependency order; effects; storage; recomputation. Which repeated subcomputations can share an answer, in what order, and what should be retained or recomputed within the memory limit? | CMP.2 for the recurrence; CMP.10 for representation and operation costs. |
| 4 | [CMP.4 - Construct Computational Search with Justified Exclusions](12-cmp-4---construct-computational-search-with-justified-exclus.md) | Stable | search; branch and bound; pruning; witness; completeness; interruption. Which alternatives can be excluded while preserving the requested answer? | MATH.20 for bounds; CMP.5 for relaxation; MMP.10 for a subject constraint formulation when needed. |
| 5 | [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](13-cmp-5---bound-an-optimum-or-recover-a-feasible-candidate-thr.md) | Stable | relaxation; feasible recovery; upper and lower bounds; approximation. How can an easier problem improve or bound an answer to the original problem? | MATH.20 for comparison; CMP.4 for bounded search; CMP.8 for controlled approximation. |
| 6 | [CMP.6 - Derive an Iterative Computational Update from Local Information](14-cmp-6---derive-an-iterative-computational-update-from-local.md) | Stable | local search; iterative update; neighborhood; step choice; noisy feedback; stopping. What does an admissible local change improve, and what follows on stopping? | MATH.10/.20/.21 for variation, bounds or convergence; CMP.7 for learning that needs an update. |
| 7 | [CMP.7 - Construct a Learner from Examples and Feedback](15-cmp-7---construct-a-learner-from-examples-and-feedback.md) | Stable | learning algorithm; rule class; inductive restriction; feedback; training fit; generalization. Which rule should examples select, and what supports its further use? | CMP.4/.6 for selection or updating; MMP.7 for a modeled data source; C.11.DUA for consequential additional inquiry. |

## Part B - Control error and computational cost

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.8 - Construct an Approximate Computation with Controlled Error](16-cmp-8---construct-an-approximate-computation-with-controlled.md) | Stable | approximation; scaling; discretization; finite stopping; rounding; conditioning. How can a permitted error reduce computation while retaining the answer quality needed next? | MATH.20/.21 for bounds and convergence; CMP.3/.10 for shared computation and representation. |
| 2 | [CMP.9 - Construct a Randomized Estimator or Sampling Procedure](17-cmp-9---construct-a-randomized-estimator-or-sampling-procedu.md) | Stable | randomized algorithm; sampling; estimator; proposal; dependence; stopping time. Which random procedure supplies the required law or finite-run estimate? | A supplied probability target, with MMP.7 where modeled; CMP.10 for access and storage. |
| 3 | [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](18-cmp-10---choose-a-computational-representation-for-its-acces.md) | Stable | data structures; representation; queries; updates; conversion; arithmetic; memory. Which representation makes the required operations affordable? | CMP.2/.3 for compositional summaries and shared work; MATH for preserved structure. |
| 4 | [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](19-cmp-11---derive-a-computational-lower-bound-from-indistingui.md) | Stable | lower bound; adversary; indistinguishable inputs; decision tree; communication; error. What must every algorithm in this model observe or communicate? | MATH.19/.20 for argument and bound; CMP.1 for reduction; C.29.2 for the cost model. |

## Part C - Interpret, transform and compose computations

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](20-cmp-12---construct-an-interpreter-or-a-meaning-preserving-tr.md) | Stable | interpreter; compiler; semantics; binding; environment; control; observable behavior. How does an expression execute, and what must its translation preserve? | MATH.5/.17/.18 for expression composition and interpretation; C.29.3 when realizing the primitives. |
| 2 | [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](21-cmp-13---construct-a-computational-abstraction-for-the-prope.md) | Stable | abstract interpretation; reachable states; sound approximation; fixed point; refinement. Which cheaper computation supports this property, and can its counterexample occur? | MATH.2/.18 for identification and interpretation; CMP.3/.4 for scheduling and exploration. |
| 3 | [CMP.14 - Compose Interacting Computations through Their Required Observations](22-cmp-14---compose-interacting-computations-through-their-requ.md) | Stable | concurrent algorithm; shared state; protocol; atomicity; interference; progress. Which interactions preserve the required whole behavior? | CMP.3/.10/.12 for dependencies, representation and semantics; C.29.3 for implementation assumptions. |
| 4 | [CMP.15 - Compose Independent Extensions of Data Variants and Operations](23-cmp-15---compose-independent-extensions-of-data-variants-and.md) | Stable | expression problem; independent extension; data variants; operations; open recursion; joining implementation; dispatch; separate compilation. How can separately added forms and operations work together without changing old modules? | CMP.12 for interpretation; CMP.14 when interactions change observations; NOT.2 and NOT.3 for new expression structure and meaning. |
| 5 | [CMP.16 - Construct Computational Units and Operations for a Required Whole](24-cmp-16---construct-computational-units-and-operations-for-a.md) | Stable | computational abstraction; units and operations; constructors; invariant; closure; refinement; composition. How can the units and allowed operations be changed together so that the required whole can be obtained and justified? | C.29.2 for the computational question; MATH.17/.18 for composition and interpretation; CMP.2/.10/.12/.14 for recursive construction, storage, execution meaning and interaction. |

# Computational Thinking - Readme

## Practical entries

Bring a need to obtain something, distinguish alternatives, maintain a response or change the way work is done. The computational question is how available operations could produce the required observations across the intended cases. The operations, representation and organization may themselves need to be invented. A mathematical description of the desired answer, a working device and one successful execution each leave different questions open.

Think of a computational description as a way of specifying a family of possible processes. Inputs, retained state, primitive operations and interactions determine which processes can occur; an interpretation says what their observations mean. The description can then be implemented, analyzed, transformed or supplied as data to another computation. This view includes numerical and symbolic work, search and learning, and ongoing interaction. It lets you change the way a result is obtained instead of only executing an existing recipe faster.

If the computational question is not yet clear, use FPF C.29.2 to connect the receiving need to represented information, required observations, available operations and resources. Then follow the difficulty that the formulation exposes. An adequate known algorithm can finish the inquiry. A missing way to assemble useful operations may need [CMP.16](24-cmp-16---construct-computational-units-and-operations-for-a.md); a missing argument or an unavailable physical operation may need a different supplier. CMP.Reference:1 explains these grounds and their consequences before the method-family map in :3.

The examples below show how one method's result makes another method usable, including where to branch or return when a condition changes. Use the Table of Contents and the patterns' own `Use this when` and `Problem frame` for other questions. Open only the contributions the question needs; a sufficient existing answer does not require a new analysis.

For inexpensive direct help, [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](18-cmp-10---choose-a-computational-representation-for-its-acces.md) can settle how to make one membership query in an existing unsorted list: a scan may suffice, with no new index to build. Many later queries or a different update workload can change that choice.

You can ask an assisting agent: “Explain this and give me your comments in the language of my work, without framework jargon.” Ask it to follow an input through the proposed operations, retain the assumptions needed by the next method, and explain what the result permits.

### CP-DESCRIPTION-TO-BEHAVIOR - A notification rule becomes an ongoing service

- **Situation:** You want messages from a named sender to trigger an immediate notification, while other messages wait for a later digest. A rule can be stated, but that statement does not yet define the behavior of the service.
- **Question:** What information and operations make the rule executable, and which changes require another computational organization?
- **First useful result or blocker:** An executable rule connected to its message and notification operations, with explicit conditions on identity, repetition and timeliness, or the unavailable information or operation that prevents that behavior.
- **Start with:** C.29.2 for the computational question. Use [CMP.16](24-cmp-16---construct-computational-units-and-operations-for-a.md) if the units and operations still need construction; use [CMP.12](20-cmp-12---construct-an-interpreter-or-a-meaning-preserving-tr.md) when a rule description needs interpretation. A known adequate implementation can be used directly.
- **Stop or return:** Stop when the required behavior is available with adequate grounds. A different source of messages, required observation or failure condition reopens its dependent construction, rather than automatically requiring every method below.

Start with an admitted event containing a sender identifier, message identifier and content. Suppose sender identity is supplied reliably, events arrive once in order, and a notification operation is available. An interpreter can read a description such as `If(SenderIs(Vasya), Notify, AddToDigest)`: test the supplied identifier and perform the selected action. CMP.12 derives the meaning of those constructors and their composition. Defining the description as data also permits a later tool to translate or analyze rules. It does not make arbitrary natural-language instructions unambiguous.

The word *immediate* introduces a further obligation. Decide whether the receiver needs an eventual response, a bound after receipt, or a bound after the message was sent. The last bound also depends on message transport. An interpreter that selects the correct action does not establish any of these timing guarantees by itself. C.29.3 connects computational operations to an actual executor and readout; the receiving work supplies the useful deadline and the consequences of missing it.

Now the transport may repeat a message. Re-executing `Notify` can duplicate an external effect, even if rule evaluation is a pure function. A message identifier and retained delivery state can support a changed operation, but recording before or after sending leaves different crash cases. CMP.14 develops the interaction and failure conditions; the Readme's retry case below shows why a repeated logical request needs a different argument from a cached function result. CMP.10 helps select storage only after the required identity and retention conditions are known. Deleting delivery state after an arbitrary interval cannot preserve a promise covering later repetitions.

If messages must instead be classified by urgency inferred from content, the known sender test no longer supplies the decision rule. CMP.7 constructs the learner, its candidate rule family, feedback and conditions of further use; CMP.4 or CMP.6 can supply its search or update. Better training fit does not establish the future error rate, and classifier quality does not establish delivery behavior. A change to inference can therefore preserve the notification protocol while reopening the evidence for classification.

This one use can involve an interpreted description, learned behavior and an interacting realization without making all three compulsory. Their connection follows from what the service must do and what its environment supplies. The full methods explain the respective constructions; this entry shows why changing a condition selects a different one.

### CP-INDEPENDENT-EXTENSIONS - A new data form and a new operation must work together

- **Situation:** One contributor adds a data variant while another adds an operation; their separate extensions leave the joint case undefined.
- **Question:** Who supplies the missing behavior, how is it selected, and which old uses remain unchanged?
- **First useful result or blocker:** A composition covering the required pairs, with an explicit joining implementation, or a named unsupported or conflicting pair.
- **Start with:** [CMP.15 - Compose Independent Extensions of Data Variants and Operations](23-cmp-15---compose-independent-extensions-of-data-variants-and.md). Use CMP.12 when the interpretation itself still needs construction; use CMP.14 when shared state or changes during execution affect the result.
- **Stop or return:** Keep a sufficient closed design when independent extension adds no useful freedom. A new required pair, changed meaning or changed dispatch rule reopens the affected composition.

For example, one extension supplies lexical `Let` and its evaluation, while another supplies free-variable analysis for the old arithmetic forms. Combining the modules leaves `FreeVariables(Let)` to be written. The bound name is removed from the body's free names, but not from the value expression's free names. CMP.15:5 derives this joining rule and shows both an executable assembly and a typed alternative. Successful registration alone cannot establish that meaning.

### CP-TRANSLATION-SCOPE - A translation works on test inputs; which executions does it preserve?

- **Situation:** Expressions have been translated to a machine with different arithmetic, and a few successful tests do not settle the permitted input range.
- **Question:** Under which input conditions does the translated program preserve the required result?
- **First useful result or blocker:** A source-to-target correspondence with an established input condition, or a concrete mismatch or unresolved condition preventing that claim.
- **Start with:** [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](20-cmp-12---construct-an-interpreter-or-a-meaning-preserving-tr.md). If the correspondence depends on a property of possible executions, use [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](21-cmp-13---construct-a-computational-abstraction-for-the-prope.md) to obtain that premise.
- **Stop or return:** Use a sufficient correspondence on its established scope. Changed inputs or machine operations reopen the affected premise. An abstract warning alone is not a demonstrated failing execution.

For example, the source computes `(x + 1) * (x - 2)` with unbounded integers. The target uses unsigned 8-bit arithmetic, wrapping modulo 256. CMP.12 specifies evaluation and translation: evaluate each operand in order, pop the right operand before the left, and append the expression's result without changing an existing stack prefix. At `x = 5`, both executions produce 18. That test does not establish correspondence for other inputs.

Suppose the allowed integers satisfy `2 <= x <= 16`. CMP.13 can compute ranges at the expression's intermediate steps: `x + 1` lies in `[3,17]`, `x - 2` in `[0,14]`, and their product in `[0,238]`. These ranges cover every source execution under the stated input condition. No arithmetic intermediate overflows the target range. This discharges the arithmetic premise of CMP.12's correspondence argument; it does not replace the argument about operand order and preservation of the stack.

Now allow `x = 17`. The source returns 270 and the target 14. The changed range calculation warns that wrapping is possible; this concrete execution establishes an actual mismatch. Return to CMP.12 to choose wider arithmetic, retain a justified input restriction, or explicitly change the intended arithmetic. Do not “repair” the analyzer by removing a real input. For a different abstract warning, CMP.13 checks the proposed execution against the original computation. If reconstruction establishes that a lost distinction produced an impossible path, refine that distinction; failure to resolve a path is not proof that it is impossible.

The same connection can supply a premise about control, binding, errors or effects, but it needs an abstraction for that property and the actual execution rules. A range argument establishes none of those other properties by itself. The direct patterns give those constructions beyond this arithmetic example.

### CP-ANSWER-UNDER-LIMITS - Obtain the answer the work needs within available resources

- **Situation:** A finite selection problem is expensive; changing from one best selection to every best selection can invalidate a shortcut.
- **Question:** How can construction, sharing, bounds and retained information preserve the answer now required?
- **First useful result or blocker:** An answer-producing procedure with justified exclusions and sufficient reconstruction information, or the specific resource limit it cannot meet.
- **Start with:** [CMP.2](10-cmp-2---derive-a-recursive-procedure-from-a-problem-decompos.md), then [CMP.3](11-cmp-3---share-and-schedule-repeated-subcomputations.md) when subproblems repeat. A useful bound from [CMP.5](13-cmp-5---bound-an-optimum-or-recover-a-feasible-candidate-thr.md) can justify exclusions in [CMP.4](12-cmp-4---construct-computational-search-with-justified-exclus.md).
- **Stop or return:** Stop at the answer sufficient for the work. Changed data, completeness or permitted error reopen the choices that depended on them; a faster value computation need not retain every witness.

First specify whether the result is a value, one selection attaining it, all such selections, or an allowed approximation. [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](10-cmp-2---derive-a-recursive-procedure-from-a-problem-decompos.md) constructs subproblems with enough returned information to assemble that answer. [CMP.3 - Share and Schedule Repeated Subcomputations](11-cmp-3---share-and-schedule-repeated-subcomputations.md) uses their identity and dependencies to decide what can be computed once, when it is needed, and what must remain available for reconstruction.

CMP.Reference:4 supplies a small connected case. Each distinct item may be selected at most once; costs and values add, and capacity is 5.

| Item | Cost | Value |
| --- | ---: | ---: |
| A | 4 | 7 |
| B | 3 | 5 |
| C | 2 | 3 |

Let `R(i,b)` be the best value using the first `i` items within capacity `b`. CMP.2 separates exclusion of the next item from its feasible inclusion. CMP.3 shares each resulting `(i,b)` subproblem. The final values for capacities 0 through 5 are `0, 0, 3, 5, 7, 8`; B+C attains 8. Keeping only two rows can save value-storage, but recovering a selection still needs choices or justified recomputation. CMP.10 chooses a representation for those actual accesses and retained distinctions. The table uses order `nW` updates for `n` items and integer capacity `W`; that is not a polynomial bound in the number of bits encoding `W`.

If exploring alternatives remains expensive, [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](13-cmp-5---bound-an-optimum-or-recover-a-feasible-candidate-thr.md) permits fractional items to obtain an upper bound. A plus one third of B gives the fractional optimum `26/3`. Since original values are integers, they cannot exceed 8. B+C reaches 8, so the optimum is already settled. [CMP.4 - Construct Computational Search with Justified Exclusions](12-cmp-4---construct-computational-search-with-justified-exclus.md) consumes such a bound to exclude alternatives; it does not treat an arbitrary relaxed candidate as an upper bound.

Now add D with cost 4 and value 8, and request **every** optimal selection. Both D and B+C must survive. The old bound concerned a different item set: D plus one quarter of A gives the new fractional optimum `39/4`, so its integer upper bound is 9 and does not alone settle optimality. The updated recurrence gives optimum 8. At its final state both the exclude-D and include-D branches attain 8; following both recovers the two selections.

The output change also changes pruning: for one optimum, an upper bound `U <= L`, where `L` is an attained value, excludes a branch that cannot improve it. For all optima, equality can hide another required selection, so this exclusion needs `U < L`. Storing only the cheapest selection for each value would keep D and discard B+C; following ties later cannot restore information already lost. Return to the recurrence and retain the required choices and item identities. Listing all answers can itself require much more work than computing their common value.

If a near-optimal answer would actually suffice, [CMP.8 - Construct an Approximate Computation with Controlled Error](16-cmp-8---construct-an-approximate-computation-with-controlled.md) changes the permitted error and construction; it does not answer the request for all exact optima. If the disputed question is what *any* algorithm must spend, [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](19-cmp-11---derive-a-computational-lower-bound-from-indistingui.md) requires a stated access and cost model. One slow implementation establishes no such limit. Other selection problems need their own sufficient subproblems and valid bounds; the item table is an example of the joins, not their scope.

### CP-RETRY-AND-RECOVER - Share calculations without merging requests or repeating their effects

- **Situation:** Requests repeat expensive calculations, replies can be lost, and a restart can erase some remembered results.
- **Question:** Which work may be shared while each logical request still has its required effect and reply?
- **First useful result or blocker:** Distinct reuse and request identities, a retention rule and a composed procedure, or the missing atomic operation or delivery condition.
- **Start with:** [CMP.14](22-cmp-14---compose-interacting-computations-through-their-requ.md) for required observations; [CMP.3](11-cmp-3---share-and-schedule-repeated-subcomputations.md) for reusable calculations; [CMP.10](18-cmp-10---choose-a-computational-representation-for-its-acces.md) for retained records. Return their results to CMP.14's interaction argument.
- **Stop or return:** Keep a sufficient existing procedure. Changed effects, record retention or failure conditions reopen the affected claim. At-most-once effects alone promise neither a reply nor a deadline.

Suppose a request runs a deterministic calculation `f(x)` and adds its result to a shared counter and returns the counter value immediately after that addition. For the input in this example, `f(x) = 5`, and the counter starts at 0. [CMP.14 - Compose Interacting Computations through Their Required Observations](22-cmp-14---compose-interacting-computations-through-their-requ.md) first distinguishes the intended observations: two independently intended requests must add twice; a retransmission of one request must not add again. A lost reply does not show whether the first addition occurred.

CMP.3 supplies a different distinction. A pure calculation of `f(x)` may be shared when its inputs and governing version make its returned result interchangeable. That reuse does not identify two independently intended additions. Give a logical request its own identifier `k`, reused only by its attempts, and keep its payload consistent. Two requests with the same `x` may reuse the calculated 5 while still adding 10 in total. If the calculation is cheap, there is no need to cache it.

These two identities determine what CMP.10 must represent: a cache for calculation results, when worthwhile, and a separate map from completed request identifiers to their payloads and returned results. Discarding a pure calculation's cache entry only causes recomputation under the same conditions. Discarding a request's completion record while an old attempt can still arrive can repeat an effect. The records' retention rules cannot be borrowed from one another merely because both look like tables.

CMP.14 uses those records in the actual interaction. After obtaining the amount, the receiver must atomically either find `k` completed and recover its original reply, or add the amount and record that reply as `k`'s completed result. Sending the reply may follow. For one request the counter becomes 5; loss of its reply followed by a retry returns the stored 5 without another addition. A genuinely new request adds another 5 and receives 10. A later retry of the first request still receives its original 5. An efficient lookup table by itself supplies no atomicity for this composite operation.

Now let a restart preserve the counter but lose completed-request records. Retrying the first request can raise 5 to 10: calculation reuse may remain correct while the composed effect is wrong. Return to CMP.14's failure model and CMP.10's retention choice. Effect and completion result must survive together if that guarantee is required. Persisting an identifier in one place and performing an external service's effect elsewhere does not close the crash interval between them; the missing operation or external guarantee remains a blocker.

Finally, keep the response question separate. Avoiding repeated effects does not require eventual message delivery. Eventual response does: it needs adequate retry, delivery, processing and retained-state conditions for both request and reply. Those conditions still provide no fixed deadline. Reopen only the affected assumption when it changes. The same separation applies to shared calculations, updates and message protocols beyond this counter example; the direct methods determine their actual identity, atomicity, storage and progress requirements.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Computational Thinking DPF Architectural Reference

- [CMP.Reference:1 - Problem frame and the algorithmic difficulty](01-cmp-reference-1---problem-frame-and-the-algorithmic-difficul.md) (64 lines)
- [CMP.Reference:2 - Forces that shape the construction](02-cmp-reference-2---forces-that-shape-the-construction.md) (13 lines)
- [CMP.Reference:3 - The methods and their connections](03-cmp-reference-3---the-methods-and-their-connections.md) (38 lines)
- [CMP.Reference:4 - Worked connection - One best selection becomes every best selection](04-cmp-reference-4---worked-connection---one-best-selection-bec.md) (28 lines)
- [CMP.Reference:5 - Use checks, assumptions and recurring failures](05-cmp-reference-5---use-checks-assumptions-and-recurring-failu.md) (25 lines)
- [CMP.Reference:6 - Consequences and Architectural Rationale](06-cmp-reference-6---consequences-and-architectural-rationale.md) (18 lines)
- [CMP.Reference:7 - Shared sources, alternatives and relations](07-cmp-reference-7---shared-sources-alternatives-and-relations.md) (20 lines)
- [CMP.Reference:End](08-cmp-reference-end.md) (2 lines)

### Part A - Construct an algorithm

- [CMP.1 - Solve One Problem through Another or Transfer a Limit (Computational Reduction)](09-cmp-1---solve-one-problem-through-another-or-transfer-a-limi.md) (231 lines)
- [CMP.2 - Derive a Recursive Procedure from a Problem Decomposition](10-cmp-2---derive-a-recursive-procedure-from-a-problem-decompos.md) (173 lines)
- [CMP.3 - Share and Schedule Repeated Subcomputations](11-cmp-3---share-and-schedule-repeated-subcomputations.md) (190 lines)
- [CMP.4 - Construct Computational Search with Justified Exclusions](12-cmp-4---construct-computational-search-with-justified-exclus.md) (175 lines)
- [CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem](13-cmp-5---bound-an-optimum-or-recover-a-feasible-candidate-thr.md) (171 lines)
- [CMP.6 - Derive an Iterative Computational Update from Local Information](14-cmp-6---derive-an-iterative-computational-update-from-local.md) (248 lines)
- [CMP.7 - Construct a Learner from Examples and Feedback](15-cmp-7---construct-a-learner-from-examples-and-feedback.md) (176 lines)

### Part B - Control error and computational cost

- [CMP.8 - Construct an Approximate Computation with Controlled Error](16-cmp-8---construct-an-approximate-computation-with-controlled.md) (179 lines)
- [CMP.9 - Construct a Randomized Estimator or Sampling Procedure](17-cmp-9---construct-a-randomized-estimator-or-sampling-procedu.md) (187 lines)
- [CMP.10 - Choose a Computational Representation for Its Access and Update Operations](18-cmp-10---choose-a-computational-representation-for-its-acces.md) (161 lines)
- [CMP.11 - Derive a Computational Lower Bound from Indistinguishable Inputs](19-cmp-11---derive-a-computational-lower-bound-from-indistingui.md) (169 lines)

### Part C - Interpret, transform and compose computations

- [CMP.12 - Construct an Interpreter or a Meaning-Preserving Translation](20-cmp-12---construct-an-interpreter-or-a-meaning-preserving-tr.md) (212 lines)
- [CMP.13 - Construct a Computational Abstraction for the Property Being Asked](21-cmp-13---construct-a-computational-abstraction-for-the-prope.md) (188 lines)
- [CMP.14 - Compose Interacting Computations through Their Required Observations](22-cmp-14---compose-interacting-computations-through-their-requ.md) (227 lines)
- [CMP.15 - Compose Independent Extensions of Data Variants and Operations](23-cmp-15---compose-independent-extensions-of-data-variants-and.md) (455 lines)
- [CMP.16 - Construct Computational Units and Operations for a Required Whole](24-cmp-16---construct-computational-units-and-operations-for-a.md) (245 lines)
