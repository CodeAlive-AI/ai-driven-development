## KCAE.COMPOSE - Connect Contributions to a Feasible Whole Result

> **Type:** Method pattern
> **Status:** Stable

### KCAE.COMPOSE:1 - Problem frame

**Use this when** the work needs several contributions, one candidate leaves a required result unprovided, or individually suitable methods interact through a common resource or condition. Three relevant procedures can be a useless recommendation if none obtains the input needed by the others. Two good methods can be alternatives rather than steps in a sequence. A compatible pair does not establish a compatible whole.

The gain is an explainable, feasible arrangement of contributions, with outstanding inputs and alternatives visible. Do not use this pattern to turn every source into a workflow. A sufficient explanation or single method can be delivered directly. The receiving discipline still supplies the methods themselves and the criteria for their results.

### KCAE.COMPOSE:2 - Problem

Retrieval ranks items; useful work often requires a set and connections that are absent from the ranking. Similarity, co-citation and adjacent storage do not tell the engineer which result must feed which operation. Selecting the highest individually scored methods can also miss a complementary set whose members are weak alone.

### KCAE.COMPOSE:3 - Forces

Searching every subset is expensive. Pruning by a familiar category can remove the only useful complement. Explicit links save repeated reasoning but age with the sources and receiving situation. More methods can improve coverage while making the whole too costly, too slow or impossible to execute.

### KCAE.COMPOSE:4 - Solution

C.39:4.2–C.39:4.4 supplies the general construction: recover a neighboring contribution, work backward from the needed result, explain the joins, then follow the proposed way forward and refine only consequential gaps. The domain work here is to obtain those contributions from a changing corpus, retain several source-qualified partial arrangements, and revise them when a missing contribution or failed connection changes the search.

#### KCAE.COMPOSE:4.1 - Work backward from the receiving result

State the result to be obtained in terms that permit inspection. “Use three patterns” is an inventory objective; “identify which exports are absent without resending an already accepted export” is a receiving result. Recover each candidate's required inputs, produced results, conditions, performer capabilities and resource demands from sufficient source context. Where the source leaves an essential relation implicit, obtain the interpretation from an appropriate reader and label it as interpretation.

Start with a candidate that can produce the receiving result. For each missing required input, ask whether it is already available, can be obtained from the case, or requires another method. Search for that missing result, preserving its meaning. Continue backward until each necessary starting input has a real provider or an explicit unresolved dependency. A circular promise that A will provide B's input after B supplies A's input is not a completed construction; identify an initial value, iterative procedure or outside provider that actually breaks the cycle.

Explanations, distinctions and criteria can be intermediate results. A diagnostic distinction may be needed before choosing an action. Do not exclude it because it is not itself executable software.

#### KCAE.COMPOSE:4.2 - Establish the connection, not just the adjacency

For each proposed connection, compare the actual output with the required input. Check what it denotes, granularity, units, source edition, time, authority and applicable population. A daily count is not a list of individual export identifiers. A list of transmitted identifiers is not proof that the destination accepted them. A percentage of completed jobs cannot silently become a probability of success for a different job.

When the two sides differ, name and obtain a conversion. This may be a deterministic transformation, another method or an expert judgement. State the information it loses and the receiving criterion it preserves. If the required conversion cannot be supplied, the methods do not yet connect. Renaming an output field cannot repair incompatible meanings.

Keep a small explanation of the relation: which result supplies which need, under which case conditions, on which source basis. This can be an annotated diagram, table or ordinary prose; a graph database is optional. Source-authored cross-references remain source relations. A connection inferred for this case remains a situated judgement. Do not silently promote it into a timeless assertion about every use of either method.

#### KCAE.COMPOSE:4.3 - Compare alternatives before selecting the whole

Distinguish a sequence, concurrent work, mutually exclusive alternatives and supportive explanation. A prerequisite must be obtained before the dependent step. Concurrent work requires the shared conditions to hold together. Alternatives offer different ways to obtain the same needed result; listing them together does not authorize doing both.

For a small set, enumerate the feasible combinations. For a large set, retain a bounded frontier: start with several promising receiving methods; expand each at its unresolved inputs; reject combinations with demonstrated contradictions; and retain distinct ways to complete the result. A beam width or a search budget is a declared approximation. It offers tractable search, not proof that the retained set is optimal. Inspect some excluded paths when a cheap screening rule could hide complements. If exact optimality matters, formulate the actual finite optimization problem and obtain an algorithm and assumptions that justify that claim, rather than relabelling heuristic ranking.

A partial arrangement needs enough retained meaning to continue: the receiving result, selected contributions, already obtained results, still missing results, proposed joins, known failed conditions, source editions and remaining search or execution allowance. Keep “result obtained” distinct from “a method could produce it.” In software these can be fields; in a small inquiry an annotated sketch is sufficient. Two arrangements that mention the same methods can differ because one has obtained a required case fact and the other has not.

Choose an unresolved contribution whose possible answers can change completion. Search by the result it must provide, its receiving meaning and necessary conditions, rather than by all the outgoing links of a favored candidate. Add a new candidate to each partial arrangement it can actually extend; qualify its source and joins before treating the extension as feasible. An unknown condition calls for a case fact or a conditional branch. A demonstrated failed join calls for a supplied transformation, a replacement contribution or another arrangement. Merely lowering that arrangement's score does not construct the repair.

Retain materially different alternatives within the budget: for example, a fast route requiring a receipt capability and a slower route that works without it. Prune a branch on a demonstrated failed necessary condition, or on a justified dominance comparison under the same result and conditions. Do not call unlike results dominated because one has a lower retrieval score. If a budget forces removal of an unresolved branch, retain that search limit in the return; do not describe the remaining candidate as the only possible solution.

Assess each whole for result sufficiency, dependencies, total burden and risks. Do not sum normalized within-group selection probabilities as the value of a set. Do not discard a method merely because its independent value is small: receipt reconciliation and safe resend can jointly solve a problem that neither solves alone. Compare that set with a direct manual reconciliation alternative under the same receiving result.

For example, a mapping from local job IDs to destination IDs may have almost no standalone value to the user. Retain it when it supplies the exact connection between a useful local record and an acceptance check. Its correctness, source basis and cost still need qualification. Neither the mapping's low direct task score nor its small size is a reason to discard the only valid join.

#### KCAE.COMPOSE:4.4 - Check joint constraints and scheduling

Collect the resources shared across the whole: a person, permission, device, context window, budget, time interval, data store or physical capacity. Add simultaneous demands where addition has the right meaning; do not add incomparable quantities. Check global conditions as well as pairs.

In CedarBench, three exports each reserve 2 GB and the cache has 5 GB. Every pair needs 4 GB and fits. The whole needs 6 GB and does not. A schedule with two concurrent exports followed by the third removes that particular conflict, provided the first pair releases its reservation. It can still violate a deadline. If each export takes ten minutes and the window is fifteen, this schedule needs twenty minutes and is infeasible. The recommendation must then reduce concurrency demand, change capacity or change the accepted completion condition; simply ordering the steps has not solved the original problem.

Check interference that is not a scalar sum: two methods may mutate the same source, require incompatible configurations or use one judgement as if it were independent evidence for the other. Include transition and cleanup work. “Each method is applicable” and “this whole is feasible now” are different conclusions.

Consider a ten-minute serial work window. The receiving operation B takes four minutes and requires result R. Candidate A obtains R in nine minutes. A followed by B takes thirteen minutes and fails the window. Preserve B and its unsupplied need; search for another way to obtain an equivalent R in at most six minutes, including the joins and preparation. Candidate C supplies the same R under the case's source conditions in five minutes, so C followed by B takes nine and fits. This search constructs an alternative that rejecting A+B alone cannot produce. It does not establish that C is the best possible supplier.

If a new source edition makes C take seven minutes, reopen the partial arrangement whose feasibility used that estimate. C+B now takes eleven minutes. Retain B's still-valid contribution, seek another supplier or a permitted change of schedule, and return the unsatisfied window if neither is available. Do not reuse the earlier nine-minute judgement merely because the method names stayed the same. The durations in this example are constructed assumptions, not measurements of a deployed system.

#### KCAE.COMPOSE:4.5 - Run the construction forward and return the alternatives


Use concrete case values or a minimally realistic example. Starting with the declared inputs, produce each intermediate result and verify that the next operation can consume it. This exposes missing identity mappings, transformations, conditions and capability assumptions that a backward diagram can conceal. A hypothetical execution explains the construction; an observed application supplies stronger use evidence and should be labelled separately.

Return the selected arrangement with its result, source grounds, joining operations and unresolved conditions. Include a meaningful alternative when the choice depends on cost or uncertainty the recipient must decide. If the only feasible continuation is obtaining a case fact or involving a qualified person, say so. Store reusable relations with the conditions and dependencies that made them valid. KCAE.CHANGE and KCAE.MEMORY can then reopen them when those conditions change.

### KCAE.COMPOSE:5 - Archetypal Grounding

CedarBench's receipt method produces destination-accepted export IDs. A set-difference operation compares them with the intended export IDs and produces the missing IDs. The resend procedure consumes those missing IDs only when the destination supports the stated deduplication protocol and a stable batch identity is available. The operations connect through IDs with a common meaning and batch boundary, not through their shared word “export.”

If the destination supplies only a count, the set difference is not available. Search for a way to obtain identity-bearing receipts, or select a manual reconciliation method whose input really is available. If protocol v1 lacks the required deduplication behaviour, acquiring the IDs does not make unattended resend safe. That changed condition selects another whole rather than a lower score for the same sequence.

### KCAE.COMPOSE:6 - Bias-Annotation

A favourite method can become the anchor around which every other result is forced. Compare a different receiving method and a smaller whole. A known taxonomy can hide an explanatory contribution or an unfamiliar intermediate result; use missing-result queries as well as named categories. A diagram can disguise conjecture as a certified interface; retain the source and case basis of each consequential link.

### KCAE.COMPOSE:7 - Conformance Checklist

Can the receiving result be recognized? Does every required starting input have a provider? Do outputs and inputs match in meaning, units, time and authority? Are conversions supplied? Are alternatives distinguished from jointly performed operations? Does the complete resource schedule fit? Can a forward case traverse every link without inventing an essential step?

### KCAE.COMPOSE:8 - Common Anti-Patterns and How to Avoid Them

A top-five list supplies no composition; expose the missing results and connections. A pairwise compatibility matrix can miss a whole-set overload; calculate the total under the schedule. A topic graph is not a method architecture; qualify the relation required by the current result. An unbounded search for the best possible set delays useful work; use a stated approximation and preserve its limit.

### KCAE.COMPOSE:9 - Consequences

The recipient can explain why the selected contributions work together and where the arrangement could fail. This requires more context than ranking alone. The work is justified when missing joins, complementarities or shared constraints can change the outcome; a single sufficient contribution remains a legitimate smaller solution.

### KCAE.COMPOSE:10 - Architectural Rationale

Source material, situated relations and execution are separate because each can change independently. A reusable relation saves work only within its conditions. Backward construction exposes required providers; forward execution exposes mismatches; whole-set checking exposes constraints no individual assessment can see.

### KCAE.COMPOSE:11 - SoTA-Echoing

A.3.1.DR, A.3.1.QM, C.32.MWA.PP and A.3.1.FT supply recovery, qualification, architecture comparison and transfer methods for method repertoires. This pattern consumes their results in an access arrangement and develops the retrieval-to-connection interface, bounded combination search and source-dependent reuse. Computational search is a serious implementation choice when a finite candidate space and constraints can be stated; a conversational proposer is another, with an explicit inspection burden. Neither receives an optimality claim from plausible output. Reopen the choice when the candidate population or cost of missed combinations changes.

### KCAE.COMPOSE:12 - Relations

KCAE.ASSESS supplies qualified contributions. KCAE.SEARCH obtains missing contributions and alternatives. KCAE.DELIVER carries the selected whole to its recipient. KCAE.MEMORY retains conditional links; KCAE.CHANGE reopens dependent links. C.39 supplies the general construction and repair of connected contributions. E.11.PUR governs coordination when the contributions are FPF patterns; CMP.4 supports computational search where its exclusions can be justified.

### KCAE.COMPOSE:End
