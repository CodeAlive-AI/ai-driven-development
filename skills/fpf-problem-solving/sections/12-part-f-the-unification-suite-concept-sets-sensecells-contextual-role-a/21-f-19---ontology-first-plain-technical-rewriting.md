## F.19 - Ontology-First Plain Technical Rewriting

> **Type:** Plain-technical precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for FPF-governed technical prose unless explicitly marked informative; informative for external source prose until it is rewritten for FPF use

**Plain-name.** Ontology-first plain rewriting.

**Intent.**
Repair technical prose whose object, claim, relation, action, role, or flow is buried under extra apparatus. The repair is not cosmetic plain-language editing. It first separates content from apparatus by ontology, then writes the remaining content in the shortest plain technical form that preserves FPF kinds, slots, claim boundaries, and admissible use. Remaining word, head, naming, or wording-use problems then apply `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern for the object.

**Builds on.** `E.8`, `E.10`, `E.10.ARCH`, `F.18`, `A.6.P`, `A.7`, `E.18`, `E.21`, and source-use, evidence, assurance, gate, work, decision, publication, architecture, characteristic, state-family, and relation patterns when those objects carry the repaired span's claim.

**Coordinates with.** `E.19`, `E.22`, `E.23`, `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P`, `E.11`, `I.2`, pattern-quality records, review records, `DRR`s, projection loci, and source-side notes.

### F.19:0 - Use this when

Use `F.19` when a bounded piece of technical prose is trying to say something precise, but the reader must pass through role labels, container words, status words, process traces, quality proof, repeated negative catalogues, reference boilerplate, or pattern-application metaphors before the object and action are visible.

Typical in-scope prose includes:

- FPF pattern prose;
- `DRR` text and architecture notes;
- review findings and quality-loop records;
- project-facing FPF guidance;
- source prose being rewritten for FPF use;
- other technical prose whose accepted ontology, domain model, controlled vocabulary, or role model must survive simplification.

**What goes wrong if missed.** Authors replace one official-sounding phrase with another. The text becomes smoother or shorter while the hidden kind error remains, or it becomes easy to read by losing the FPF kind, slot, role, claim boundary, or admissible-use boundary.

**What this buys.** Plain technical wording becomes an ontological discipline with less apparatus: fewer words, clearer objects, fewer repeated negative catalogues, and no loss of technical semantics.

**First useful move.** Mark the span under repair. Split it into content candidates and apparatus candidates before rewriting either side.

**Not this pattern when.**

- If the problem is only one overloaded word or head after the content is visible, apply `E.10`.
- If the problem is a durable reusable name, apply `F.18`.
- If the span already names the content-bearing relation, source-use relation, state-family value, architecture label, characteristic, quality term, function wording, evidence claim, gate claim, work claim, decision claim, or other FPF object named by value, apply the governing pattern for that object.
- If the source text is only being observed and not admitted into FPF-governed prose, keep the observation source-side.

**Primary EntityOfConcern in plain terms.** One phrase-level, sentence-level, row-level, paragraph-level, or small-section technical-prose repair whose goal is kind-preserving plain expression.

### F.19:1 - Problem frame

Mature technical languages accumulate enough ontology that many bad sentences are not bad because the terms are unknown. They are bad because a simple technical claim is wrapped in process language, role language, status language, quality-proof evidence, pattern-reference boilerplate, or repeated negative distinctions.

The repair question is:

> What content remains when words that add no object, kind, relation, claim, role, flow, evidence value, or user-facing action are removed?

Examples inside FPF:

- "`A.15` handles the claim" when the text needs to say that `A.15` applies to a work-planning claim;
- "pattern text" when the text means "the pattern" or "the pattern of concern";
- "governing relation" when the named object is a pattern, not a relation;
- long "not X, not Y, not Z" paragraphs when the text needs a positive object, action, and one stop condition;
- corpus-projection proof written inside a pattern whose own user-facing action is not corpus projection.

The same defect appears outside pattern prose. A system note may hide an evaluation claim inside process language; a project note may treat a dashboard as evidence authority when it is a publication form; an architecture memo may replace a scale-preference claim over alternatives with a platform label.

These failures confuse coupled transformation flows. A pattern under development, a pattern being applied, a quality evaluation of that pattern, a project work occurrence, a source publication, and a projection record are different objects. They may influence one another; they do not become one another by being mentioned in the same paragraph.

### F.19:2 - Problem

How can FPF make technical prose plain without:

- treating plain language as a synonym-replacement exercise;
- deleting content-bearing technical terms as "jargon";
- replacing established terms with colourful synonyms or role nicknames;
- letting process, review, projection, or quality proof become pattern content;
- repeating the same boundary doctrine in every local pattern;
- hiding current ontic slot, relation-position, use-relation, or claim-kind changes under a shorter phrase;
- turning every phrase repair into a new local mini-ontology?

### F.19:3 - Forces

| Force | Tension |
|---|---|
| Plain wording vs ontology | Short prose helps readers, but careless simplification erases kinds, slots, relation positions, use relations, role values, or claim boundaries. |
| Precision vs apparatus | Technical precision needs kind recovery, but extra role, record, card, table, schema, data-structure wrapping, locus, flow, status, and process words can bury the claim. |
| Local repair vs semantic change | Some extra words are boilerplate; others carry a hidden kind, relation, current ontic slot, relation position, use relation, evidence-use relation, or admissible-use boundary. |
| Flow separation vs readable prose | Development, evaluation, projection, and use flows must stay distinct without making every sentence narrate those flows. |
| Reuse vs repetition | References to related patterns matter, but repeated "if X, apply Y" prose can become reference fanout. |
| Plainness vs synonym churn | Plain prose should reduce apparatus, not create a new set of loose paraphrases for established FPF terms. |

### F.19:4 - Solution

Use `OntologyFirstPlainRewrite` as a five-step repair over one bounded span.

1. **Bound the span.** Name the sentence, row, paragraph, or small section under repair. Name visible apparatus candidates: pattern-application drift, role label, container word, status word, process trace, quality proof, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or other overwrap.
2. **Separate content from apparatus by ontology.** For each phrase part, ask what object, head kind, claim kind or relation kind, current ontic slot, relation position, use relation, publication relation, admissible use, concerned actor or reader role when a role is current, and design, run, or coupled-flow position when flow separation matters. If a phrase part changes one of those values, keep it as content. If it only restates process, role label, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or quality proof without changing content, classify it as apparatus.
3. **Remove or move apparatus.** Delete the apparatus or move it to the document, record, note, or publication relation where it belongs: `DRR`, review record, quality result, architecture note, README, ToC, `E.11`, or `I.2` entry locus, projection record, release or landing evidence document, or source-side note. Do not replace it with a smoother synonym, role label, container word, status word, record, card, table, schema, data-structure wrapper, or publication-form word.
4. **Restore remaining content precision.** Apply `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern when a remaining word, head, relation, claim, current ontic slot, relation position, use relation, source-use relation, durable name, or admissible-use boundary is still hidden.
5. **Rewrite and check loss.** Write the shortest plain technical sentence that preserves the repaired object, kind, claim, relation, action, current ontic slot, relation position, use relation, actual role value when current, flow position when current, established term, and admissible use. The rewrite fails if it changes one of those values without an accepted semantic decision, or if it becomes harder for the declared reader to use.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed when the wording can change the object, kind, relation, current ontic slot, relation position, use relation, publication relation, admissible use, or governing pattern. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves those values, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

Use the full result form when the repair must be inspectable; otherwise a local rewrite plus the kind-preservation check is enough.

#### F.19:4.1 - Result form

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, negative-catalogue, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that may carry object, kind, claim, relation, current ontic slot, relation position, use relation, actual role value when current, flow position, evidence-use value, or user-facing action. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, scope, and governing pattern when another pattern governs a specific outside claim. |
| `ConcernAndFlowPosition` | Concerned actor or reader role only when a role is current; design, run, or coupled-flow position when it changes meaning. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `F.18`, governing pattern, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became worse, less local, less current, less recoverable, or less usable if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same algorithm with one role test:

> Does this sentence address the pattern's intended user, or does it record development, review, projection, landing, quality, or source-management evidence about the pattern version?

If it records evidence about the pattern version, keep that evidence outside the pattern unless the pattern's own primary `EntityOfConcern` is that evaluation or projection object. The evidence can cause edits to the pattern; it is not automatically pattern content.

Pattern prose keeps:

- the pattern's own primary `EntityOfConcern`;
- the first useful move;
- the practical delta and cost of missing it;
- local boundary prose only for a documented local confusion and named stop condition;
- short declarative references to related patterns after the pattern's own content is visible.

Pattern prose moves out:

- package-placement rationale;
- correspondence about producing the draft rather than using the pattern;
- quality-status proof;
- README, ToC, `E.11`, `I.2`, retrieval, card, monolith-parity, or landing evidence;
- repeated boundary doctrine already carried by another pattern.

### F.19:5 - Archetypal Grounding

| Grounding slice | Before | F.19 repair |
|---|---|---|
| Pattern application | "`A.15` handles the work-planning claim." | "Apply `A.15` to the work-planning claim." |
| Pattern vs relation | "The governing relation is `C.29`." | "Mathematical-lens claims are governed by `C.29`." |
| Pattern text role | "Pattern text must not contain corpus projection evidence." | "A pattern must not contain projection evidence about itself." |
| Evaluation scope | "The evaluation has pre-landing host-set use." | "This is a host-only evaluation; corpus-entry values need corpus-projection evidence." |
| Negative catalogue | "This pattern is not proof, not work, not a gate, not a decision." | "This pattern evaluates pattern quality; project evidence claims are governed by project-side evidence patterns." |
| Role label | "The platform owns scale." | "The span makes a scale-preference claim over platform and non-platform alternatives." |
| Publication and evidence mix | "The dashboard is the evidence gate." | "The dashboard is a publication form; evidence and gate claims need their own governing patterns." |

### F.19:6 - Bias-Annotation

`F.19` deliberately biases toward shorter, reader-facing prose. The protected value is kind-preserving clarity, not brevity by itself. A rewrite that removes terms while losing object kind, relation kind, current ontic slot, relation position, use relation, source-use relation, or admissible-use boundary is worse than the original.

`F.19` also protects against two common reviewer biases:

- **negative-catalogue bias:** explaining a class by long lists of what it is not;
- **apparatus-preservation bias:** replacing one process, role, record, card, table, schema, data-structure wrapper, locus, flow, status, or quality-proof phrase with another phrase that still hides the object.

### F.19:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-F19-1` | The repair names the text span and visible apparatus candidates before rewriting. |
| `CC-F19-2` | The repair separates apparatus from content by object, kind, claim or relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, concerned actor or reader role when a role is current, and flow position when flow separation matters; lexical dislike is not enough. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content and is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the governing pattern rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite includes a `KindPreservationCheck`; a wording change that changes object kind, relation kind, claim kind, current ontic slot, relation position, use relation, admissible use, or scope without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in their owning evidence, projection, release, or publication loci unless the text's own object of concern is that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics; a longer rewrite is admissible only when it recovers a hidden kind, relation, role, slot, or claim boundary. |
| `CC-F19-10` | The repair records any value, usability, locality, currentness, or kind-recoverability loss. |
| `CC-F19-11` | Term-source or type annotation is used only for wording whose source ontology can change the object, kind, relation, current ontic slot, relation position, use relation, publication relation, admissible use, or governing pattern; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, and next governing pattern. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide the object a practitioner must recognize. |

### F.19:8 - Common anti-patterns and how to avoid them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Lexical paint | One umbrella word is replaced by another while the object kind stays hidden. | Recover the object kind and rewrite in the object's technical name. |
| Hypergeneric repair | The rewrite uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` to sound precise while hiding the actual object, relation, specialization target, or governing pattern. | Restore the practitioner-recognizable object and the governing relation; for specialization, say what specializes what and which inherited or changed slots or uses matter. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to the review record, quality result, projection record, release document, or other governing evidence document and keep only the resulting user-facing action or boundary. |
| Role label as ontology | A role label replaces the object kind. | Name the object kind; state the role relation only when it changes the claim. |
| Slot label as ontology | A slot, field, relation-position, or use-relation label replaces the object kind, or the same object in several slots or relation positions is treated as several kinds. | Preserve object kind, current ontic slot, relation position, and use relation separately and apply the governing pattern for the content-bearing relation, signature, lens, role, method, or work claim. |
| Apparatus-looking data structure | A record, card, table, schema, dashboard, or data-structure word is kept because it sounds precise, but it does not carry the EntityOfConcern, slot relation, publication relation, admissible use, or governing pattern. | Treat it as apparatus and remove it, or use `E.24.CD`, `E.24.PUB`, or the direct governing pattern if it really carries a candidate ontic, publication boundary, or subject-pattern relation. |
| Negative catalogue | The sentence defines an object by listing what it is not. | Lead with the positive object and action; keep only local documented confusion and named stop condition. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the claim-governing term or relation that is under repair. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop non-governing apparatus, and use a plain technical sentence plus reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus-and-content split and repair by value. |

### F.19:9 - Consequences

`F.19` makes technical prose easier to read because it removes apparatus before shortening the sentence. It also makes reviews stricter: a pleasant paraphrase does not count unless the pre-rewrite and post-rewrite kind, relation, current ontic slot, relation position, use relation, admissible use, and scope are preserved or deliberately changed by accepted decision.

The cost is that some edits need a short repair note before they look simple. That cost is intentional. Without the note, agents tend to do lexical replacement, narrow a graph into a sequence, widen a work occurrence into a method, turn a publication into evidence, or hide a pattern application under a route-like metaphor.

### F.19:10 - Rationale

Plain technical style in FPF is not a separate aesthetic layer. It is the visible result of ontology-first repair with less apparatus. The order matters:

1. remove or move boilerplate;
2. restore the remaining content through wording-use, naming, relation, slot, source-use, or object-governing patterns named by value;
3. write the shortest sentence that keeps the recovered meaning.

Putting `F.19` beside wording-use restoration keeps `E.10` from becoming a phrase-style super-pattern. `E.10` catches words and heads whose kind or use is hidden. `F.19` catches the earlier phrase-level problem: the content may not even be visible until process, role, status, reference, quality, or negative-catalogue apparatus is removed.

### F.19:11 - SoTA-Echoing

| Claim disciplined by source | Practice or source | Source-use relation | FPF import |
|---|---|---|---|
| Plain prose serves a reader and task, not a generic style preference. | ISO 24495-1:2023, *Plain language - Part 1: Governing principles and guidelines*. | Current standard reference for plain-language principles and task/readership fit. | `F.19` requires declared reader and use and checks loss after rewriting. It adapts plain-language principles to FPF kind preservation. |
| Plain language removes unnecessary complexity while keeping necessary terms. | Federal Plain Language Guidelines and Digital.gov plain-language guidance. | Current government plain-language practice reference for audience-first, direct, organized prose. | `F.19` removes apparatus but preserves established FPF terms unless `E.10` or `F.18` changes them. |
| Legal and technical documents can be clearer without losing controlled terms. | SEC, *A Plain English Handbook: How to Create Clear SEC Disclosure Documents*. | Lineage and practice reference for reducing legalese while retaining disclosure meaning. | `F.19` treats "plain" as meaning-preserving repair, not informal paraphrase or synonym churn. |
| FPF precision restoration must preserve ontology before style. | Current FPF patterns `E.8`, `E.10`, `E.10.ARCH`, `F.18`, `A.6.P`, `E.21`. | Current FPF governing-source relation. | `F.19` becomes the phrase-level sibling to word, head, and use restoration and feeds `E.21` through `PrecisionRestorationProfile`. |

### F.19:12 - Relations

| Related pattern | Relation |
|---|---|
| `E.8` | Applies `F.19` to FPF pattern prose and keeps pattern bodies addressed to their intended users. |
| `E.10` | Restores remaining wording whose kind, relation, or admissible use is hidden after apparatus removal. |
| `E.10.ARCH` | Provides shared wording-use recovery architecture for remaining content. |
| `F.18` | Settles durable reusable names after kind and use are known. |
| `A.6.P` | Restores relation construction when the remaining content hides relation kind, endpoint, basedness, anchoring, current ontic slot, relation position, or use relation. |
| `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P` | Govern state-family, source or publication, characteristic or scale, and architecture or structure wording when those objects remain as content after apparatus removal. |
| `E.21` | Consumes `F.19` findings through `PrecisionRestorationProfile`; it lowers affected quality coordinates without creating one coordinate per apparatus symptom. |
| `E.19`, `E.22`, `E.23` | Use `F.19` in review, framing, and improvement-loop work while keeping quality-loop records out of pattern prose. |
| `E.11` and `I.2` | Provide first-entry cues and expanded entry-disambiguation cases for phrase-level apparatus repair. |

### F.19:End

