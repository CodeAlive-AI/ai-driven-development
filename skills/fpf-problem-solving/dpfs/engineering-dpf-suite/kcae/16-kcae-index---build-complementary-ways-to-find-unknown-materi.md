## KCAE.INDEX - Build Complementary Ways to Find Unknown Material

> **Type:** Method pattern
> **Status:** Stable

### KCAE.INDEX:1 - Problem frame

Use this when repeated questions concern a large corpus and the useful source, phrase or contribution is often unknown. The governed object is the reusable retrieval arrangement: indexed units, selection grounds, query operations, result combination and independent source access. Its useful result is an implemented or implementable route design that can expose material a single representation would miss. The source reader and workload must be available. If direct reading of a bounded dossier already supplies the result at acceptable cost, it is a sufficient rival.

### KCAE.INDEX:2 - Problem

A lexical system can miss another profession's vocabulary. A dense embedding can blur negation or a rare identifier. A summary tree can exclude the only branch containing an exception. Adding a second endpoint over the same summaries preserves the same omission. Merely listing these technologies leaves the engineer without the construction that joins their strengths, pays their maintenance cost and preserves a way beyond their common blind spots.

### KCAE.INDEX:3 - Forces

Prepared views reduce recurring work but cost construction and refresh. Several views increase discovery opportunities and duplicate results. Early filtering saves work and can exclude the unknown answer. Rich context improves interpretation but lowers the number of candidates that fit a fixed budget. The aim is a useful and maintainable arrangement for the workload, not an exhaustive representation of all knowledge.

### KCAE.INDEX:4 - Solution

#### KCAE.INDEX:4.1 - Specify the retrieval operations and their source units

Start with the question families from KCAE.USE and the addressable units from KCAE.SOURCE. Define what each route returns: source edition, unit identifier, matched text or span, route and query used, ranking value with its local meaning, and a way to open the reading unit. Preserve version, permission and authority metadata independently of the score. The first interface is a candidate-finding operation; it does not claim that the material supports the user's action.

Build an exact reader and an inventory enumerator even when semantic retrieval is the primary discovery route. The enumerator lists the permitted units in a selected snapshot without requiring a relevance match. It enables update validation and a direct original scan. A source corpus that cannot be enumerated can still be searched through its provider, but the independent-scan promise is then bounded by what that provider actually exposes.

Choose retrieval units by the distinctions the queries need. Index whole source bodies through bounded units, including examples, appendices and footnotes where they can matter. Index titles, controlled vocabulary and summaries as additional fields or views. Keep their source spans and derivation separate so that a hit from an explanatory prefix cannot be misquoted as original text. KCAE.SOURCE supplies the expansion from a small hit to its enclosing conditions.

#### KCAE.INDEX:4.2 - Construct views with different selection grounds

For an exact/lexical route, define normalization and fields deliberately. Preserve exact identifiers and error codes even if a second field lowercases, stems or expands terms. Decide how the languages in the actual corpus are tokenized. A BM25-style inverted index ranks term matches; a raw-text search remains useful for newly changed or unusual strings that the index does not yet represent. Test punctuation-sensitive identifiers, inflections and negation-bearing phrases on actual source snippets. Full-text relevance and exact equality are different operations.

For a dense route, select an embedding model whose language and domain behaviour can be examined on the workload. Embed source units, not only cards. Use the compatible query encoding and similarity operation; record model, dimensions, preprocessing, normalization and unit-generation versions. Keep independently built spaces separate until compatibility has been established. Comparing a new query embedding with vectors from an incompatible earlier model yields a numerically computable but uninterpretable score.

An approximate nearest-neighbour index trades search work and storage for approximation. On a manageable, representative subset, compare its returned neighbours with an exact search in the same vector space. This tests approximation, not semantic relevance. Separately judge whether the model ranks the needed source distinctions. A high approximation recall cannot repair an embedding that never captured the relevant condition. Token-level late interaction is another candidate when finer matching earns its additional representation and query cost; KCAE.Profiles:1 explains the ColBERT lineage without making it mandatory.

For a structural route, extract relations whose meaning is established: section containment, explicit source references, table ownership, edition succession or symbol definitions from a qualified code parser. Store relation kind, source basis and target identity. A query such as “what defines this symbol?” can use that structure directly. A query such as “what would improve this work?” needs additional interpretation; proximity in a document graph does not establish useful contribution.

For broad corpus questions, consider summaries or entity/community views at several scales. They can expose themes that local nearest-neighbour retrieval scatters. Retain source membership for each summary and permit leaf/original retrieval independently of the hierarchy. If an answer claims “the main objections across this corpus,” its sampling and coverage question differs from finding one useful objection. KCAE.SEARCH:4.6 constructs the coverage-to-answer operation; KCAE.ASSESS checks both its individual claims and the scope of its aggregate. A view supplies material to that operation, not the broad conclusion by itself.

#### KCAE.INDEX:4.3 - Make selection filters explicit

Apply access restrictions before material can reach an unauthorized component. Other filters are claims about the question. If the user asks about current operational policy and an authority rule selects the governing edition, use that rule; if the question asks about history or conflicts, retain the relevant older editions. Do not infer a subject/Suite filter from the first few words and then make every route inherit it.

Compare early filtering with later assessment. Early exclusion is appropriate when the predicate is reliable and required, such as an access boundary. A guessed topic is better used as one retrieval preference with a broad route still available. When a route supports only post-filtering of its first K hits, permission-safe candidate inspection may still suffer poor recall because eligible hits were below K. Over-fetching or a natively filtered index can help; measure the actual operation and report the boundary.

A route can fail because the useful document is absent, its extraction is incomplete, the model missed its meaning, the approximate search lost it, a filter excluded it, or the candidate window was too small. Preserve enough route information to distinguish these causes during evaluation. Otherwise every failure invites another model while the source never entered the index.

#### KCAE.INDEX:4.4 - Combine candidates without inventing a common probability

Run the selected routes against the same intended corpus/edition conditions. Deduplicate by source identity and overlap, while retaining which routes found a candidate. Keep competing editions distinct where the use needs them. Merge adjacent fragments into one reading candidate when their overlap would otherwise consume the budget repeatedly; do not merge conflicting source claims merely because their words are similar.

Raw lexical, vector and graph scores usually have different meanings. A simple candidate-combination baseline is rank fusion. Reciprocal rank fusion assigns a candidate the sum of 1/(c + rank) across lists in which it appears. It uses order rather than pretending that raw scores share a scale. The positive constant c controls how much top ranks dominate; the original 2009 study used 60, which is historical experimental selection rather than a universal setting. [RRF source](https://cormack.uwaterloo.ca/cormack/cormacksigir09-rrf.pdf).

Fusion still favours material with several appearances. Preserve a tested allocation for route-unique candidates before the later shortlist: for example, take a fused core, then admit the highest-ranked unrepresented candidate from each materially different route, within the same budget. Treat query paraphrases from one model as related search attempts, not independent votes proving relevance. Compare this diversity policy with simple fusion on held-out questions; keep it only where it recovers valuable contributions at acceptable cost.

For a concrete constructed pool, suppose lexical order is A, B, C and dense order is D, A, B. With c = 60, A receives 1/61 + 1/62, B receives 1/62 + 1/63, and D receives 1/61. A and B win the top two positions because each appears in both lists. The route-unique D disappears from a two-item shortlist. Retaining D for inspection may expose a cross-language exception. Its eventual usefulness must be judged from the source; its uniqueness is a reason to inspect, not evidence of truth.

Choose candidate-window size from downstream reading capacity and error costs. A pool of 100 hits is an internal search result, not a request to stuff 100 fragments into the principal agent's context. Assess and expand within the search service or separate reader where supported; deliver the sufficient result through KCAE.DELIVER. Too narrow a pool cannot be repaired by a perfect reranker, because the relevant source never reaches it.

#### KCAE.INDEX:4.5 - Provide an independent original-text route

Implement a route that can inspect source units without passing the same relevance filter. Enumerate permitted units from the snapshot, divide them into bounded reading batches, include their source addresses and necessary local context, and ask question-relative screening questions. Preserve the unprocessed extent and batch outcomes. The examiner may be a person, a generative model or a qualified typed assessor. The route can be used initially for a rare novel question, as a complement to indexes, or after a consequential suspected miss.

A first pass can ask whether a block contains a potentially useful condition, explanation or method; a second expands promising blocks into reading units. A later pass can search for an unresolved relationship across the retained sources. A single winner from each batch is unsafe where several contributions are needed: allow multiple candidates and an explicit no-candidate/unknown outcome. Scores normalized inside different batches are not globally comparable probabilities. Reassess finalists together or use separately qualified pointwise criteria.

A large corpus makes complete inspection expensive. Schedule by source order, strata or a declared sample that is independent of the failed selector; use affordable partial coverage when that can answer the current question. A stratified sample is a diagnostic route, not an exhaustive scan. If the route first chooses batches by the same summary classifier that failed, its independence has been lost. If the examiner reads all blocks but misses a cross-block relation, byte coverage has increased without semantic completeness. KCAE.SEARCH preserves both limits in its return.

#### KCAE.INDEX:4.6 - Join the routes to maintenance and evaluation

Publish each view with its source generation, covered subset and build configuration. Define readiness per operation: an exact reader can be ready before dense indexing; a graph can support containment while semantic edges remain unqualified. KCAE.CHANGE supplies coherent switching, partial readiness and deletion handling. Decide how new or changed units enter current queries while expensive views catch up.

Test complementary retrieval on cases independently authored from the working needs. Include a rare identifier, vocabulary mismatch, late exception, graph-relevant question, broad synthesis and source not represented by any summary. Measure sufficient contributions recovered within the recipient's budget, not just union size. Remove a redundant route if its maintenance and query cost earn no useful difference. Add or replace a route when a repeated consequential gap exposes a different required distinction.

### KCAE.INDEX:5 - Archetypal Grounding

CedarBench has a hypothetical snapshot of 6,000 documents and 32,000 retrieval units. Many support requests use customer vocabulary absent from the English manual. The engineer builds a lexical field preserving product identifiers, a dense field from complete source units, structural parent/reference relations and an exact reader. The query “our analyst removes double reports every morning” yields a throughput article lexically and a receipt-reconciliation note semantically. The pool retains both and opens their conditions.

A new supplier note appears before its embedding is ready. The current-source inventory and direct reader expose it; the route reports that dense coverage lags. An independent block pass can examine the new units. This is a designed integration of persistent additional retrieval and current source reading, not proof that the dense route is superior. In a three-document historical dossier, a cached full reading can replace this machinery with less total effort.

### KCAE.INDEX:6 - Bias-Annotation

Queries derived from titles favour title-based systems. Test vocabulary and relationships supplied by real work. Correlated retrievers can create apparent agreement; preserve provenance and inspect route-unique gains. Majority-language averages can hide important minority-language losses.

### KCAE.INDEX:7 - Conformance Checklist

Does the design explain source units, encoding, filters, candidate combination, source expansion and maintenance? Can the independent route reach material the principal selector excludes? Are scores interpreted locally? Can a known loss be attributed to ingestion, representation, filtering, approximation, pool size or later assessment? Has the chosen arrangement been compared at the actual reading budget?

### KCAE.INDEX:8 - Common Anti-Patterns and How to Avoid Them

Calling several searches over one card store “independent” hides a shared bottleneck; add an original-body route. Multiplying scores turns retrieval ranks into unsupported probabilities; use a declared ranking policy and a separate assessment. A graph of document mentions is not a graph of necessary method relations; interpret the receiving relationship through KCAE.COMPOSE. A failed lexical trial is not required to justify engineering a semantic route for a forecast workload.

### KCAE.INDEX:9 - Consequences

Unknown material becomes reachable through more than one selection ground, and the system can explain which parts remain unsearched. The design increases storage, update and evaluation work. It cannot guarantee future semantic completeness; it provides attainable ways to investigate consequential omissions.

### KCAE.INDEX:10 - Architectural Rationale

Prepared representations and query-time inspection solve different cost problems. Their common source-address contract makes them interchangeable and combinable, while route independence protects against compression becoming an exclusive ontology. The evaluation decides how much of that plurality earns its cost.

### KCAE.INDEX:11 - SoTA-Echoing

The current practice question concerns hybrid, graph, multiscale and agentic retrieval under a changing corpus. KCAE.Profiles:1 compares their constructions, including the historical ColBERT, HyDE, GraphRAG, RAPTOR and LazyGraphRAG lines with current source/view studies. This pattern adopts multiple candidate grounds and exact source return, adapts fusion to preserve useful unique findings, and rejects a technology-independent winner. Code-domain findings remain code-domain evidence. Reopen the selection after a changed query family, model, update regime or measured loss.

### KCAE.INDEX:12 - Relations

KCAE.SOURCE supplies units and reading expansion. KCAE.SEARCH operates the available routes for a developing question. KCAE.ASSESS decides contribution after retrieval. KCAE.CHANGE maintains source/view correspondence, and KCAE.EVAL tests marginal and whole-use value. CMP.10 can supply the underlying data-structure and operation-cost reasoning.

### KCAE.INDEX:End
