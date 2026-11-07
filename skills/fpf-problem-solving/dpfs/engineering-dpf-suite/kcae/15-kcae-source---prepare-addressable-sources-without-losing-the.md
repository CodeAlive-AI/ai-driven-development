## KCAE.SOURCE - Prepare Addressable Sources without Losing Their Context

> **Type:** Method pattern
> **Status:** Stable

### KCAE.SOURCE:1 - Problem frame

Use this when documents must become searchable or machine-readable, when a hit cannot be opened reliably, or when extracted text can lose a decisive relation. The governed object is the relation between an exact source edition, its extracted/segmented representations and obtainable reading context. The result is a source inventory and reader that can return that context with known fidelity limits. A clean, fully addressable source already sufficient for the use needs no new extraction pipeline.

### KCAE.SOURCE:2 - Problem

Document bytes, extracted text and meaningful source units are different. A table flattened into lines can attach a permission to the wrong model; OCR can drop “not”; a translation can omit an exception; a heading-based address can drift. A flawless embedding of the resulting text preserves those errors.

### KCAE.SOURCE:3 - Forces

Small retrieval units discriminate topics but sever context. Large reading units preserve relations but cost attention. Normalization improves matching but can erase exact identifiers or provenance. Stable identity must survive harmless movement while still revealing a meaningful edition change.

### KCAE.SOURCE:4 - Solution

#### KCAE.SOURCE:4.1 - Preserve the source and describe its provenance

Obtain an immutable source edition or make a permitted snapshot before extracting it. Preserve publisher/collection, document identity, edition, effective interval when relevant, access class and original format. Use a content digest to detect byte changes; retain semantic identity separately so that identical text in different documents is not accidentally merged. A corpus snapshot fixes a set of source editions, not merely the name of a branch that can move.

For a mutable collection, first capture a coherent set through a source-system snapshot or an approved freeze/copy procedure. A manifest computed while files are changing can describe an impossible combination. If the source system cannot provide a coherent snapshot, state the consistency limit and narrow the usable operation; do not label a best-effort crawl as an atomic edition. KCAE.CHANGE develops live and historical reading contracts.

#### KCAE.SOURCE:4.2 - Extract the relationships needed for reading

Choose the extractor by the actual carrier. Markdown and HTML can expose headings, lists and links. Born-digital PDFs can still scramble columns or reading order. Scanned documents need OCR and inspection of decisive glyphs, tables and notes. Audio/video transcripts need time offsets and returns to the original segment when tone, a demonstration or a visual relation matters. Machine-readable data needs schema, units, null meaning and provenance. Store the original alongside the extraction while permission permits it.

Define a small extraction qualification set from the source's likely failures: an exception containing negation, a multi-column page, a repeated heading, a table with merged cells, a footnote and a cross-document reference. Compare rendered source and extraction for the use-changing relationships, not only character count. Random sampling can detect wider drift, but a sample does not certify every uninspected decisive passage. Mark unqualified regions and allow direct visual or specialist reading where needed.

For a table, retain its title, row identity, column identity, units, span relations and notes. An indexed cell can be small, but its read operation expands to these relations. For example, the extracted CedarBench cell “No” is unusable. The qualified reading says “Destination protocol v1 / automatic resend / No; reconcile receipts manually; note a: receiver lacks duplicate suppression.” The source image or native table remains reachable. If OCR cannot distinguish v1 from v2, return an uncertain extraction and inspect the original before applying the condition.

Distinguish faithful extraction from an authored interpretation. A generated explanatory prefix can make an index easier to search; it remains a derived claim, with the original text separately available. Translation has the same discipline: keep source language and edition, preserve important negations, numerical units and scope, and compare the consequential reading with a competent translator or the source owner when reliance requires it. An old translation can be a search aid or historical artifact without being the current operational authority.

#### KCAE.SOURCE:4.3 - Separate finding units from reading units

Segment by intelligible source structure before imposing a token ceiling. Preserve parent headings, paragraph/list membership, table and figure ownership, explicit references and adjacent conditions. Split an oversized section into bounded retrieval units while leaving its reading unit intact. Overlap can reduce boundary losses, but blind overlap duplicates text and still does not recover a distant definition.

Give each unit a document/edition identity, a local locator, an exact source span where available and an expansion relation. Keep retrieval text, structural metadata and generated context in distinguishable fields. Record which parents or definitions a generated context used. That makes a later parent change capable of invalidating an apparently unchanged child representation.

Choose unit size using the retrieval question and the operation that consumes the hit. A broad research theme may benefit from section summaries; a protocol exception may need paragraph or cell retrieval. Keep an independent raw/full-body path so that summary selection is not the only way to reach the source. Test a question whose deciding text lies beyond the initial unit; the opening operation should recover it without requiring the user to guess its exact location.

#### KCAE.SOURCE:4.4 - Implement and test the source return

A practical exact reader accepts a source edition and a locator, then returns the requested material, its structural envelope, continuation information and the edition actually served. A pagination cursor should bind the edition and requested unit. Expose an end marker or explicit remaining extent so that truncated output cannot masquerade as complete reading. Do not rely on a line number without its edition.

When a heading moves, a semantic document/section identity can help resolve the new location, but exact historical reading still selects the old edition. When a section splits or merges, preserve explicit predecessor/successor relations and inspect them before treating them as equivalent. A fuzzy match may suggest a new location; it cannot silently establish identity or preserve an earlier judgement.

Verify build, persist, reload, find and read on a fixture that includes additions, deletions and shifted headings. Check that the returned text corresponds to the selected source, that a deleted locator yields an explicit result and that a child unit expands through the correct note. Preserve the qualification result with the extraction/version where the installation needs it. KCAE.EVAL distinguishes this mechanical correctness from useful question answering.

### KCAE.SOURCE:5 - Archetypal Grounding

CedarBench's table has two rows: protocol v1 requires receipt reconciliation; v2 permits idempotent resend after absence is confirmed. A flat extractor returns “v1 v2 No Yes” and loses the note. The engineer retains a row/column representation and source-page locator, verifies both rows against the page, and indexes each row with its heading and note. A query can now find the v1 limitation; opening it returns the complete condition. When a later PDF changes only its pagination, source content can remain semantically equal while exact page coordinates change; the new reader generation updates the locators.

### KCAE.SOURCE:6 - Bias-Annotation

Clean text collections make extraction seem trivial. Include the actual poor scans, minority language and awkward tables that the workload contains. Generated context can project the author's interpretation onto ambiguous text; mark it as derived and preserve the source ambiguity.

### KCAE.SOURCE:7 - Conformance Checklist

Can every decisive hit return to its source edition and reading context? Are source and generated text distinguishable? Were characteristic extraction failures inspected against the original? Does the reader expose truncation, inaccessible regions and uncertain mappings? Does persistence/reload preserve the same return?

### KCAE.SOURCE:8 - Common Anti-Patterns and How to Avoid Them

Indexing only summaries makes their omissions universal; retain searchable original units. Hash-only identity merges unrelated copies; include source provenance. Returning a table cell without row, column and note creates a false claim; expand the reading unit. Treating OCR as semantic proof ignores its loss boundary; qualify the relied-on extraction.

### KCAE.SOURCE:9 - Consequences

The arrangement gains trustworthy source return and reusable extraction. It costs storage and qualification work, and some formats continue to require visual or expert reading. Explicit uncertainty prevents a damaged extraction from appearing to be a confident source claim.

### KCAE.SOURCE:10 - Architectural Rationale

The source remains the basis for later questions, while retrieval units optimize discovery. Their separate identities let the system change chunking or embedding without changing what an exact read means. Preserved context dependencies make selective refresh possible.

### KCAE.SOURCE:11 - SoTA-Echoing

The practice question is how to retrieve small passages without making them contextless. Anthropic's 2024 Contextual Retrieval is a useful historical mechanism: attach context to chunks before indexing. This pattern adapts that idea by retaining generated context separately and exposing its source dependencies; it does not adopt the reported corpus-wide gains as a forecast. Indexing complete sections can avoid chunk expansion within a section; compare its finding performance and per-hit reading cost with smaller units. Reopen the unit design when an actual miss depends on omitted context or when expansion overwhelms the reader. NOT.5 supplies a fuller translation/loss method where notation changes; ordinary file parsing alone is not an A.6.3.RT semantic translation claim.

### KCAE.SOURCE:12 - Relations

KCAE.USE supplies the source roles and allowed use. KCAE.INDEX consumes retrieval units; KCAE.DELIVER consumes reading units; KCAE.CHANGE maintains their identities and dependencies. A.6.3.RT and NOT.5 govern their respective representation-loss questions without replacing this domain extraction and source-reader construction.

### KCAE.SOURCE:End
