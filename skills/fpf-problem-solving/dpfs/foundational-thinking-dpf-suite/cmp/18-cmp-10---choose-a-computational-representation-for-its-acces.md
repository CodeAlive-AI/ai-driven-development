## CMP.10 - Choose a Computational Representation for Its Access and Update Operations

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### CMP.10:1 - Problem frame

**Use this when** a computation spends too much effort finding, updating, combining or storing information, and changing its representation could improve those operations. The mathematical objects may already be understood; the missing choice is how to obtain the needed answers from their stored form.

A sequence can be stored directly or through partial aggregates. A graph can be represented by a matrix or by lists of neighbors. The same relation can have very different computational consequences under those choices. Conversely, a compact representation can lose the multiplicity, ordering or state distinction needed after an update.

The result is a representation with effective read and update operations, a meaning-preservation argument, and a cost comparison for the intended workload. The reader needs the object's relevant operations and elementary algorithm analysis.

Keep the existing representation when it already serves the work affordably. Choosing what the subject model should describe is a separate task. Here the target distinctions are sufficiently known to ask how different representations support their computation; a discovered missing distinction returns to that formulation.

### CMP.10:2 - Problem

How can a representation be constructed around the operations that matter, so that cheaper access or update retains the information and behavior required by the computation?

An encoding can be reversible yet expensive to query. A small stored summary can answer one question while making a later question impossible. An update can be cheap locally but invalidate a shared aggregate, index or cached interpretation.

### CMP.10:3 - Forces

| Force | What must be reconciled |
| --- | --- |
| Read cost and update cost | Precomputed answers accelerate queries but need maintenance when inputs change. |
| Compactness and accessible distinctions | Fewer stored bits can require expensive decoding or discard required identity. |
| Local operations and global invariants | A changed element can affect several summaries or indexes. |
| Initial conversion and repeated use | A better per-operation bound may never repay construction cost. |
| Abstract operation count and realization | Bit growth, memory transfer and output size can dominate a word-operation estimate. |
| Generality and workload fit | A versatile structure can cost more than a simpler one for the actual operation mix. |

### CMP.10:4 - Solution

**Name the operations → choose retained distinctions → construct representation and invariants → derive reads and updates → compare total work → use and revise the choice.**

#### CMP.10:4.1 - Start from the operations and their conditions

List the operations needed by the computation, including their inputs and returned results. Distinguish membership, enumeration, selection by order, aggregation, insertion, deletion and value replacement when their requirements differ. Include whether answers need original identities or only values.

Describe the anticipated operation sequence or range of workloads. A fixed dataset with many queries differs from a changing stream. If the mix is unknown, compare alternatives over the plausible range instead of inventing one universal average.

State which resources constrain the work: storage, worst-case response, total running time, memory transfers or communication. Include the required output size; listing k distinct items takes work to produce those k items under an ordinary explicit-output model.

#### CMP.10:4.2 - Choose what the representation must distinguish

Define how a stored state represents the abstract object or the observations required of it. State the invariants that make reads meaningful. A sorted array needs an order invariant; an aggregate tree needs each stored aggregate to agree with the segment it represents.

If two source states share one representation, check every required read and continuation. Their equality must preserve the requested answers after the allowed updates. MATH.2 supplies identification under operations. If the representation is deliberately lossy, CMP.8 supplies the approximate answer relation.

Keep consequential identity, multiplicity and ordering. A set removes duplicates; a sequence retains positions. A zero numeric value need not mean an absent relation. An object reference and a copied value respond differently to later mutation.

#### CMP.10:4.3 - Construct operations from the representation's structure

Choose a structure whose retained information makes the frequent operation cheaper. A sorted array supports binary search by repeatedly excluding one ordered half. A hierarchy of aggregates answers a range query by combining a small set of segments. Lists of actual neighbors avoid scanning absent graph edges.

Derive each read and update from the invariant. For an update, identify every stored part whose meaning depends on the changed input, and restore it. Include shared summaries and the operations used to recover an original witness. CMP.3 supplies reuse and dependency reasoning when values are cached across computations.

When summaries are combined, state the algebra the procedure needs. An associative operation permits regrouping; it need not permit reordering. An identity element can represent an empty segment. Inverses are required only for a method that subtracts or otherwise undoes an aggregate, not for every range-query construction.

For dynamic storage, include growth and rebuilding. Doubling an array's capacity gives occasional linear copying and bounded total copying over a sequence of appends. The resulting amortized append cost does not claim constant worst-case latency for every individual append. A latency requirement can select incremental rebuilding or another representation.

#### CMP.10:4.4 - Count the complete computation under an explicit cost model

Compare construction and conversion, the intended reads and updates, reconstruction or output, and peak storage. A useful first comparison is `construction cost + sum of operation costs` for the workload. Keep several resource dimensions separate when no accepted trade-off combines them.

State what one elementary operation costs. Arithmetic on a bounded machine word can be treated as constant in an appropriate model; multiplying or comparing integers whose encoded lengths grow needs the corresponding bit cost. A symbolic expression that shares subexpressions can be small while its fully expanded output is large.

If transfers between memory levels dominate, analyze blocks moved as well as abstract pointer or arithmetic operations. A representation with contiguous access can outperform one with fewer but scattered accesses. Realization measurements can distinguish close candidates; they need not precede a decision already settled by an adequate cost argument.

Include invalidation and synchronization when shared updates are part of the workload. An operation that is correct in sequential use does not acquire a concurrent guarantee merely because its representation is shared.

#### CMP.10:4.5 - Compare alternatives at the receiving use

Construct the simplest credible alternative, not only a slower version of the favored structure. Compare raw storage with a precomputed index, full retention with reconstruction, or a compact representation with an expanded one according to the actual operations.

Require preservation of the needed answers before treating reduced cost as improvement. For a deliberate approximation, retain its qualified result and the loss it buys. Use the existing characterization, Pareto and improvement methods when choices trade storage, latency, update work and precision.

Select conversion only when its cost and risk are justified by the expected subsequent use. A mixed strategy can keep a simple base representation and add one index for the consequential query. Its update obligations remain part of the choice.

#### CMP.10:4.6 - Return a usable representation and reopen it locally

Return the structure, its meaningful state, read and update procedures, and the resource consequence that motivated the change. A small worked operation should expose the invariant and a consequential change should test its maintenance.

Reconsider the choice when the query mix, update pattern, output identity, data magnitude or physical access cost changes. Preserve the abstract object and valid algorithms where they remain applicable. A newly required distinction that the old representation discarded may require returning to the source data, not merely rebuilding an index from the insufficient summary.

### CMP.10:5 - Archetypal Grounding

#### CMP.10:5.1 - Design stored aggregates for mixed queries and updates

Maintain a sequence of n integers with two operations: replace one element and return the sum of the first k elements. A raw array gives a constant number of word accesses for replacement and k additions for a prefix query. Precomputing every prefix sum makes queries constant-time, but a replacement can change all following prefix sums.

For frequent interleaved queries and updates, build a balanced binary tree over consecutive segments. A leaf stores one element; each internal node stores the sum of its children's segments. Padding to a power of two with zero-valued leaves gives fewer than 4n nodes for n>0 and logarithmic height. Build the sums from the leaves upward in linear many additions.

To replace an element, change its leaf and recompute every ancestor from its two children. To query a prefix, use a fully included segment's stored sum; ignore an excluded segment; at a partially included segment descend into its children. Only the boundary path is partially included, so at most a constant number of nodes per level are visited. Both operations take `O(log n)` additions/accesses, with integer bit costs counted separately.

For `[3,1,4,2]`, the two half sums are 4 and 6 and the root is 10. The prefix of length three combines the left half's 4 and the third leaf's 4, returning 8. Replace the second value by 5: its leaf becomes 5, the left sum 8 and the root 14. The same query now returns 12.

If updates disappear and many queries remain, the simpler prefix array may be preferable. If the aggregation changes to concatenation, retain left-to-right order. For leaves A,B,C,D, the prefix of length three must be ABC; regrouping into AB and C is valid, but combining them in reverse order returns CAB. The tree construction needs associativity, not commutativity. Its unit-cost sum analysis does not automatically apply to copying growing strings.

#### CMP.10:5.2 - Choose graph access by the question, retaining edge meaning

For a directed graph with n vertices and m edges, a Boolean adjacency matrix supports a membership test by one entry lookup. Enumerating a vertex's outgoing neighbors scans n entries. Adjacency lists store actual neighbors; enumeration examines its outgoing degree many entries, while a plain-list membership test can require the same scan. A hash index adds another storage/update trade-off.

A traversal that marks each vertex once and enumerates its outgoing edges therefore takes `O(n+m)` accesses with lists, and up to `O(n²)` with a matrix, excluding construction and output. Repeated pair-membership questions on a dense graph can favor the matrix. The graph's mathematical identity alone does not choose the computational representation.

Now attach numeric weights. If zero is used both for an absent edge and for an existing zero-weight edge, those two states become indistinguishable. For edges `0→1` with weight 0, `1→2` with weight 2 and `0→2` with weight 5, treating zero as absence deletes a path of cost 2 and leaves the apparent direct cost 5. Repair the representation with a separate presence indication or an absent value outside the admitted weights. Changing the shortest-path algorithm cannot recover an edge already discarded by its input representation.

### CMP.10:6 - Bias-Annotation

The examples derive the structure from mixed prefix operations or graph access. They assume a sequential computation and state their elementary costs; shared or unusual physical realizations require their corresponding conditions.

### CMP.10:7 - Conformance Checklist

- Required reads, updates, output identity and workload conditions are stated.
- Stored states have an interpretation and the invariants needed by those operations.
- Reads and updates are effective and preserve the required distinctions.
- Cost includes construction, maintenance, recovery, output and consequential representation growth.
- The chosen representation is compared with a credible simpler alternative on the intended workload.
- A changed operation or lost distinction leads to a specific reconstruction or source-return step.

### CMP.10:8 - Common Anti-Patterns and How to Avoid Them

| Tempting move | Failure | Useful repair |
| --- | --- | --- |
| Choose the smallest encoding | Decoding or updates dominate the computation. | Compare the required operations including conversion. |
| Treat all integers as constant-cost values | Operand lengths grow beyond the cost model. | Count bit operations or bound the admitted magnitudes. |
| Update only the changed leaf | Dependent aggregates or indexes retain obsolete answers. | Restore every affected invariant. |
| Reorder associative aggregates | Associativity alone does not permit exchanging operands. | Preserve order or establish commutativity for this operation. |
| Use one value for absence and a meaningful zero | The reader cannot reconstruct the discarded distinction. | Represent presence separately. |

### CMP.10:9 - Consequences

Algorithmic cost becomes changeable through a deliberate representation choice. A reader can replace an expensive access pattern, expose hidden maintenance or decoding work, and retain the original computational meaning through the change.

The best choice can vary with workload and realization. A new operation can reveal that a previously adequate summary is insufficient, opening a return to the richer source or a revised answer requirement.

### CMP.10:10 - Architectural Rationale

A computational representation is useful through what its operations obtain. Reversible encoding, mathematical equivalence and fast access are distinct properties; none implies all the others. Invariants connect them by explaining how stored states support the required observations and updates.

The method therefore places operation design and resource comparison together. It uses mathematical preservation and general portfolio comparison while retaining algorithmic responsibilities for effective conversion, access, maintenance and output.

### CMP.10:11 - SoTA-Echoing

Which representation serves a required mix of operations? **Adopt** the interface-to-implementation comparison in Morin's [*Open Data Structures*, chapters 2](https://opendatastructures.org/newhtml/ods/latex/arrays.html) and [12](https://opendatastructures.org/newhtml/ods/latex/graphs.html), for :4.1–4.5 and :5.2. It compares concrete operations rather than ranking structures by familiarity or compactness. Direct arrays or matrices remain serious alternatives to more elaborate indexing when their workload is favorable. Additional summaries deliberately trade maintenance and storage for cheaper queries; :5.1 derives a balanced aggregate construction with those obligations. A changed query/update mix or required identity reopens the comparison.

When memory transfers dominate, **adapt** the external-memory and cache-oblivious analysis developed in [Demaine's survey](https://people.csail.mit.edu/edemaine/papers/BRICS2002/paper.pdf), in :4.4. Its competing cost model exposes a limit of equal-cost memory accesses. A blocked or recursive layout can reduce transfers while adding construction complexity; choose it only when that saving matters for the receiving work. The historical survey supplies the analysis distinction, not a current hardware performance ranking. A changed memory hierarchy, data layout or measured bottleneck can reverse the practical selection without invalidating the abstract operation argument.

### CMP.10:12 - Relations

- **C.29.2:** supplies computational formulation and the elementary resource model.
- **MATH.2, MATH.17 and MATH.18:** supply identification under operations, operations as objects and preservation through interpretation.
- **CMP.2 and CMP.3:** construct recursive operations and shared intermediate results.
- **CMP.8:** supplies a controlled approximation when the representation intentionally loses information.
- **C.29.3:** establishes relevant physical realization conditions.
- **C.11.DUA and the general characterization, Pareto and improvement methods:** compare the useful effect of conversion, measurement and further optimization.

### CMP.10:End
