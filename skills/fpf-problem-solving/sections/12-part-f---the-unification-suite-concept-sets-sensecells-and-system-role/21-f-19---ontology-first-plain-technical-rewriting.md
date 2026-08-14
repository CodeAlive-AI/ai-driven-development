## F.19 - Ontology-First Plain Technical Rewriting

> **Type:** Plain-technical precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative for FPF-governed technical prose unless explicitly marked informative; informative for external source prose until it is rewritten for FPF use

**Plain-name.** Ontology-first plain rewriting.

**Intent.**
Repair technical prose whose object, claim, relation, action, role- or function-shaped wording, or flow is buried under extra apparatus. The repair is not cosmetic plain-language editing. It first separates content from apparatus by ontology, then writes the remaining content in the shortest plain technical form that preserves FPF kinds, slots, claim boundaries, and admissible use. Repair any remaining word, head, name, or wording-use problem with `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining claim.

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

**What goes wrong if missed.** Authors replace one official-sounding phrase with another. The text becomes smoother or shorter while the hidden kind error remains, or it becomes easy to read by losing the FPF kind, slot, relation position, system-role-kind or assignment distinction, function or functioning claim, claim boundary, or admissible-use boundary.

**What this buys.** Plain technical wording becomes an ontological discipline with less apparatus: fewer words, clearer objects, fewer repeated negative catalogues, and no loss of technical semantics.

**First useful move.** Mark the span under repair. Split it into content candidates and apparatus candidates before rewriting either side.

**Not this pattern when.**

- If the problem is only one overloaded word or head after the content is visible, apply `E.10`.
- If the problem is a durable reusable name, apply `F.18`.
- If the span already names the content-bearing relation, source-use relation, state-family value, architecture label, characteristic, quality term, function wording, evidence claim, gate claim, work claim, decision claim, or other FPF object named by value, use the specific pattern that defines, constrains, or tests that claim and say what it contributes.
- If the source text is only being observed and not admitted into FPF-governed prose, keep the observation source-side.

**Primary EntityOfConcern in plain terms.** One phrase-level, sentence-level, row-level, paragraph-level, or small-section technical-prose repair whose goal is kind-preserving plain expression.

### F.19:1 - Problem frame

Mature technical languages accumulate enough ontology that many bad sentences are not bad because the terms are unknown. They are bad because a simple technical claim is wrapped in process language, role language, status language, quality-proof evidence, pattern-reference boilerplate, or repeated negative distinctions.

The repair question is:

> What content remains when words that add no object, kind, relation, claim, system-role or function distinction, flow, evidence value, or user-facing action are removed?

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
| Plain wording vs ontology | Short prose helps readers, but careless simplification erases kinds, slots, relation positions, use relations, system-role kinds, classification judgments, assignment occurrences, function or functioning claims, ordinary meanings, or claim boundaries. |
| Precision vs apparatus | Technical precision needs kind recovery, but extra role, record, card, table, schema, data-structure wrapping, locus, flow, status, and process words can bury the claim. |
| Local repair vs semantic change | Some extra words are boilerplate; others carry a hidden kind, relation, current ontic slot, relation position, use relation, evidence-use relation, or admissible-use boundary. |
| Flow separation vs readable prose | Development, evaluation, projection, and use flows must stay distinct without making every sentence narrate those flows. |
| Reuse vs repetition | References to related patterns matter, but repeated "if X, apply Y" prose can become reference fanout. |
| Plainness vs synonym churn | Plain prose should reduce apparatus, not create a new set of loose paraphrases for established FPF terms. |

### F.19:4 - Solution

Use `OntologyFirstPlainRewrite` as a five-step repair over one bounded span.

1. **Bound the span.** Name the sentence, row, paragraph, or small section under repair. Name visible apparatus candidates: pattern-application drift, role label, container word, status word, process trace, quality proof, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or other overwrap.
2. **Separate content from apparatus by ontology.** For each phrase part, ask what object, head kind, claim kind or relation kind, current ontic slot, relation position, use relation, publication relation, admissible use, concerned actor or reader, and design, run, or coupled-flow position it carries. When *role* occurs, use `E.10.ROLE` to recover whether the claim concerns a local system-role kind, classification of an admitted System, obtaining system-role assignment, participation in another relation, a declaration or representation position, another direct relation, or ordinary wording. When *function* occurs, use `A.6.F` to recover the actual claim rather than treating *function* as one technical kind: the familiar estimate of roughly seven meanings is only a recall cue, the dispatch is non-exhaustive, and one occurrence can be metonymic or carry more than one reading. If a phrase part changes one of those values, keep it as content. If it only restates process, a role- or function-shaped label, negative catalogue, reference boilerplate, record, card, table, schema, data-structure wrapping, or quality proof without changing content, classify it as apparatus.
3. **Remove or move apparatus.** Delete the apparatus or move it to the document, record, note, or publication relation where it belongs: `DRR`, review record, quality result, architecture note, README, ToC, `E.11`, or `I.2` entry locus, projection record, release or landing evidence document, or source-side note. Do not replace it with a smoother synonym, role label, container word, status word, record, card, table, schema, data-structure wrapper, or publication-form word.
4. **Restore remaining content precision.** Restore every complement needed to determine the claim: what was selected, changed, compared, transformed, published, evaluated, or relied on. Use `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining word, head, relation, claim, slot, use, name, or admissible-use boundary.
5. **Rewrite and check loss.** Write the shortest plain technical sentence that preserves the repaired object, kind, claim, relation, action, current ontic slot, relation position, use relation, any current system-role kind, classification judgment or assignment occurrence, any function or functioning claim, ordinary wording when that is all the source means, flow position, established term, and admissible use. The rewrite fails if it changes one of those values without an accepted semantic decision, or if it becomes harder for the declared reader to use.

Keep ontology visible only where it carries the sentence. A term-source or type annotation is needed only when it changes how the reader identifies the object, kind, relation, slot, use, publication boundary, admissible use, or applicable rule. A record, card, table, schema, data structure, dashboard, or named form remains apparatus unless it carries one of those values. If ordinary domain wording already preserves them, keep the ordinary sentence. "The aircraft flies" is better than a typed expansion unless the flight function, system kind, or slot relation is under repair.

Treat `exact`, `direct`, `current`, `governed`, `subject`, `owner`, `defining`, and similar qualifiers as content only when they distinguish live alternatives. Remove them when no such contrast changes the truth, action, stop, or reliance. A PatternID may remain an ordinary citation; expand it into a claim-bearing episteme, `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, `U.Work`, or another formal identity only when the current claim or a named later use depends on that distinction.

Keep ordinary practitioner action and instrumental pattern-use wording ordinary when it does not assert a particular dated Work occurrence. “Use `E.9` to record the decision” and “the framework maintainer compares the editions” need no invented Method, MethodDescription, performer, assignment, or Work identity.

Open the identity-bearing branch only when the sentence deliberately asserts a particular dated `U.Work` occurrence. Then point to its complete A.15.1/F.6 basis. Add a local system-role kind or a separate System-classification judgment only when that neighboring claim matters. Treat a pattern episteme as a `U.MethodDescription` only after `A.3.2` establishes that it has an already admitted Method as its `EntityOfConcern` and explains how that Method is performed. Otherwise cite the applicable pattern content as guidance and use `A.3.1` for the Method itself.

When one sentence joins unlike claims and no genuine common head covers them, split the claims and use `E.10:0.2c.17` for the resulting list. Do not invent an umbrella object merely to preserve one grammatical subject.

Use the full result form when the repair must be inspectable; otherwise a local rewrite plus the kind-preservation check is enough.

#### F.19:4.1 - Result form

| Field | Meaning |
|---|---|
| `TextSpanRef` | Bounded span under repair. |
| `ApparatusCandidateSet` | Visible pattern-application, role, record, card, table, schema, data-structure wrapping, locus, flow, status, process, negative-catalogue, reference, or quality-proof apparatus candidates. |
| `ContentCandidateSet` | Phrase parts that may carry object, kind, claim, relation, current ontic slot, relation position, use relation, a system-role kind, classification judgment or assignment occurrence, function or functioning claim, ordinary wording, flow position, evidence-use value, or user-facing action. |
| `ObjectOfConcern` | Object the span is about. |
| `KindAndClaimMap` | Head kind, claim kind, relation kind, current slot, relation position, use relation, publication relation when it changes admissible use, scope, and—when another pattern contributes—the pattern id plus what its content defines, constrains, or tests. |
| `ConcernAndFlowPosition` | Concerned actor or reader; any exact local system-role kind, separate System-classification judgment, or assignment occurrence; relation or representation position; ordinary reader wording; and design, run, or coupled-flow position—only where each changes meaning. |
| `ApparatusDisposition` | Removed, moved, retained as content, or blocker when separation is not yet possible. |
| `RemainingContentPrecisionRestoration` | `not needed`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, a named pattern plus its concrete contribution, or blocker. |
| `PlainRewrite` | Short rewrite after apparatus removal and remaining-content precision restoration. |
| `KindPreservationCheck` | Pre-rewrite and post-rewrite object kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope; disposition is `preserved`, `split`, `intentionally changed by accepted decision`, or `blocker`. |
| `LossCheck` | What became worse, less local, less current, less recoverable, or less usable if the rewrite is accepted. |

#### F.19:4.2 - Pattern-prose specialization

When the repaired prose is an FPF pattern, apply the same algorithm with one purpose test:

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
| Pattern use, ordinary | "`A.15` handles the work-planning claim." | "Use `A.15` to plan the work." |
| Pattern use, identity-bearing | "The pattern performed the planning." | "Engineer E performed planning Work W. Point to W's complete A.15.1/F.6 basis; use `A.3.2` only if a named episteme describes the enacted Method." |
| Pattern and relation, ordinary | "The governing relation is `C.29`." | "Use `C.29` to test whether the mathematical lens is admissible for this task." |
| Pattern and relation, identity-bearing | "`C.29` says so." | "If a comparison depends on the rule edition, cite the claim-bearing episteme and `ClaimGraph` that contain the admissibility rule." |
| Pattern-text purpose | "Pattern text must not contain corpus projection evidence." | "A pattern must not contain projection evidence about itself." |
| Evaluation scope | "The evaluation has pre-landing host-set use." | "This is a host-only evaluation; corpus-entry values need corpus-projection evidence." |
| Negative catalogue | "This pattern is not proof, not work, not a gate, not a decision." | "This result evaluates pattern quality. Use `A.10` for any separate project-evidence claim." |
| Role-shaped label | "The platform owns scale." | "This scale compares platform and non-platform alternatives." |
| Publication and evidence mix | "The dashboard is the evidence gate." | "The dashboard presents evidence. Use `A.10` for the evidence claim and `A.21` for any gate decision." |
| Comparison, carrier, and publication mix | "E.4.PFIP preserves expression, carrier, and publication." | "The framework maintainer compares the predecessor and candidate publication expressions for the declared use. Use `E.10:0.2c.17` to separate the expression comparison from carrier-bearing and publication-occurrence claims." |

### F.19:6 - Bias-Annotation

`F.19` deliberately biases toward shorter, reader-facing prose. The protected value is kind-preserving clarity, not brevity by itself. A rewrite that removes terms while losing object kind, relation kind, current ontic slot, relation position, use relation, source-use relation, or admissible-use boundary is worse than the original.

`F.19` also protects against two common reviewer biases:

- **negative-catalogue bias:** explaining a class by long lists of what it is not;
- **apparatus-preservation bias:** replacing one process, role, record, card, table, schema, data-structure wrapper, locus, flow, status, or quality-proof phrase with another phrase that still hides the object.

### F.19:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-F19-1` | The repair names the text span and visible apparatus candidates before rewriting. |
| `CC-F19-2` | The repair separates apparatus from content by object, kind, claim or relation kind, current ontic slot, relation position, use relation, publication relation when it changes admissible use, the exact system-role-kind, classification, assignment, other direct relation or ordinary wording recovered from any role-shaped phrase, the actual claim recovered from any function-shaped phrase, and flow position; lexical dislike is not enough. |
| `CC-F19-3` | Apparatus is removed or moved before wording-use precision restoration is applied to the remaining content. |
| `CC-F19-4` | Content-bearing wording remains content and is repaired by `E.10`, `E.10.ARCH`, `F.18`, or the specific pattern that defines, constrains, or tests the remaining claim rather than deleted as style. |
| `CC-F19-5` | A removed apparatus word is not replaced by a synonym, metonymy, role label, container word, or status word that carries the same hidden apparatus. |
| `CC-F19-6` | Established FPF terms are preserved unless a named precision-restoration or naming pattern changes them. |
| `CC-F19-7` | Every accepted rewrite includes a `KindPreservationCheck`; a wording change that changes object kind, relation kind, claim kind, current ontic slot, relation position, use relation, admissible use, or scope without an accepted decision remains a blocker. |
| `CC-F19-8` | Development, evaluation, projection, landing, use-found, repair, and source-management evidence stay in the evidence, projection, release, or publication loci that carry them unless the text is about that flow object. |
| `CC-F19-9` | The accepted rewrite is shorter or clearer without losing technical semantics; a longer rewrite is admissible only when it recovers a hidden kind, relation, system-role or assignment distinction, function or functioning claim, slot, relation position, or claim boundary. |
| `CC-F19-10` | The repair records any value, usability, locality, currentness, or kind-recoverability loss. |
| `CC-F19-11` | Term-source or type annotation is used only when it changes the object, kind, relation, slot, use, publication boundary, admissible use, or rule the reader must apply; stable ordinary prose is not expanded into type labels. |
| `CC-F19-12` | The accepted plain rewrite passes MG-DA cold-reader recovery: a reader without the `DRR`, campaign notes, or author memory can state the content-bearing object, kind or ordinary status, relation or claim position, admissible use, next practical action, and—when another pattern contributes—its id and contribution. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, and unqualified `specialization` are not plain enough when they hide what a practitioner must recognize. |
| `CC-F19-13` | Every added qualifier or formal identity has a named live contrast: it changes truth, action, stop, migration, publication, reuse, or reliance. An ordinary PatternID citation does not by itself require a `ClaimGraph`, `U.MethodDescription`, `U.Method`, actor, assignment, or `U.Work` expansion. |
| `CC-F19-14` | After apparatus removal, the sentence names every complement needed to determine what was selected, changed, compared, transformed, published, evaluated, or relied on. |
| `CC-F19-15` | Ordinary practitioner action and instrumental “use pattern X” wording stays ordinary when it does not assert identity-bearing dated Work. When it does, the text points to the complete A.15.1/F.6 basis. A local system-role kind and a separate System-classification judgment appear only for their own claims, and `U.MethodDescription` appears only after the `A.3.2` test passes. |
| `CC-F19-16` | A heterogeneous list is split when its members need different heads or predicates; the rewrite uses `E.10:0.2c.17` instead of inventing one umbrella head. |

### F.19:8 - Common anti-patterns and how to avoid them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Lexical paint | One umbrella word is replaced by another while the object kind stays hidden. | Recover the object kind and rewrite in the object's technical name. |
| Hypergeneric repair | The rewrite uses `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` to sound precise while hiding the actual object, relation, rule, or action. | Restore the practitioner-recognizable object and relation; for specialization, say what specializes what and which inherited or changed slots or uses matter. |
| Plain-language drift | Smooth prose drops the kind named by value or admissible-use boundary. | Remove apparatus first, then restore remaining wording precision before shortening. |
| Flow smuggling | Development, projection, landing, or evaluation evidence is written as user-facing guidance. | Move the evidence to the review record, quality result, projection record, release document, or other appropriate evidence document and keep only the resulting user-facing action or boundary. |
| Role-shaped label as ontology | The word *role* is treated as one technical value or replaces the object kind. | Recover the local system-role kind, classification, obtaining assignment, relation participation, declaration or representation position, another direct relation, or ordinary wording that the sentence actually needs; do not infer any branch from the word alone. |
| Function-shaped label as ontology | The word *function* is treated as one technical value or as proof of functioning, capability, assignment, or Work. | Use `A.6.F` to recover the claim by meaning; allow metonymy and more than one reading, and treat the familiar count of meanings only as a recall cue. |
| False common head | One grammatical subject is made to select, compare, carry, publish, and evaluate unlike things. | Split the claims and use `E.10:0.2c.17`; retain only heads that fit every listed member. |
| Slot label as ontology | A slot, field, relation-position, or use-relation label replaces the object kind, or the same object in several slots or relation positions is treated as several kinds. | Preserve object kind, slot, relation position, and use separately; cite the specific pattern only when its definition, constraint, or test is needed. |
| Apparatus-looking data structure | A record, card, table, schema, dashboard, or data-structure word is kept because it sounds precise, but it does not carry the EntityOfConcern, slot relation, publication boundary, admissible use, or next action. | Remove it, or use `E.24.CD`, `E.24.PUB`, or the specific content pattern when the structure really carries a candidate-ontic, publication, or domain relation. |
| Negative catalogue | The sentence defines an object by listing what it is not. | Lead with the positive object and action; keep only local documented confusion and named stop condition. |
| Over-annotation as precision | The rewrite replaces a clear domain sentence with type labels, source-ontology tags, or slot names that do not change the claim. | Keep the domain sentence and annotate only the term or relation under repair. |
| Triggerless formal expansion | A PatternID citation becomes an “exact direct current subject owner”, `ClaimGraph`, Method, actor, assignment, or Work claim even though no alternative identity changes the result. | Keep the ordinary citation and action. Open the formal branch only after naming the contrast or later use that consumes it. |
| Overformalized precision | The rewrite preserves all terms but makes the sentence harder to think with or generalize from. | Keep the content-bearing kind and claim, drop apparatus that changes neither, and use a plain technical sentence plus a reference named by value where needed. |
| Apparatus-preserving paraphrase | A rewrite changes wording but keeps the same status, process, or quality-proof apparatus. | Return to the apparatus-and-content split and repair by value. |

### F.19:9 - Consequences

`F.19` makes technical prose easier to read because it removes apparatus before shortening the sentence. It also makes reviews stricter: a pleasant paraphrase does not count unless the pre-rewrite and post-rewrite kind, relation, current ontic slot, relation position, use relation, admissible use, and scope are preserved or deliberately changed by accepted decision.

The cost is that some edits need a short repair note before they look simple. That cost is intentional. Without the note, agents tend to do lexical replacement, narrow a graph into a sequence, widen a work occurrence into a method, turn a publication into evidence, or hide a pattern application under a route-like metaphor.

### F.19:10 - Rationale

Plain technical style in FPF is not a separate aesthetic layer. It is the visible result of ontology-first repair with less apparatus. The order matters:

1. remove or move boilerplate;
2. restore remaining wording, names, relations, slots, and uses through the specific pattern contribution needed by the claim;
3. write the shortest sentence that keeps the recovered meaning.

Putting `F.19` beside wording-use restoration keeps `E.10` from becoming a phrase-style super-pattern. `E.10` catches words and heads whose kind or use is hidden; `E.10.ROLE` resolves a role-shaped trigger without defaulting to one ontology, and `A.6.F` does the same for function-shaped wording without turning its recall count into a closed taxonomy. `F.19` catches the earlier phrase-level problem: the content may not even be visible until process, role-shaped, function-shaped, status, reference, quality, or negative-catalogue apparatus is removed.

### F.19:11 - SoTA-Echoing

| Claim disciplined by source | Practice or source | Source-use relation | FPF import |
|---|---|---|---|
| Plain prose serves a reader and task, not a generic style preference. | ISO 24495-1:2023, *Plain language - Part 1: Governing principles and guidelines*. | Current standard reference for plain-language principles and task/readership fit. | `F.19` requires declared reader and use and checks loss after rewriting. It adapts plain-language principles to FPF kind preservation. |
| Plain language removes unnecessary complexity while keeping necessary terms. | Federal Plain Language Guidelines and Digital.gov plain-language guidance. | Current government plain-language practice reference for audience-first, direct, organized prose. | `F.19` removes apparatus but preserves established FPF terms unless `E.10` or `F.18` changes them. |
| Legal and technical documents can be clearer without losing controlled terms. | SEC, *A Plain English Handbook: How to Create Clear SEC Disclosure Documents*. | Lineage and practice reference for reducing legalese while retaining disclosure meaning. | `F.19` treats "plain" as meaning-preserving repair, not informal paraphrase or synonym churn. |
| FPF precision restoration must preserve ontology before style. | Current FPF patterns `E.8`, `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, `A.6.P`, `E.21`. | Current FPF source-use relation. | `F.19` becomes the phrase-level sibling to word, head, and use restoration and feeds `E.21` through `PrecisionRestorationProfile`. |

### F.19:12 - Relations

| Related pattern | Relation |
|---|---|
| `E.8` | In FPF pattern authoring under `E.8`, use `F.19` to keep pattern bodies addressed to their intended users. |
| `E.10` | After apparatus removal, use `E.10` for remaining wording whose kind, relation, or admissible use is hidden; use `E.10:0.2c.17` when a heterogeneous list needs different heads or predicates. |
| `E.10.ARCH` | Use its shared wording-use recovery architecture for the remaining content. |
| `E.10.ROLE` | Use its distinctions to recover what role-shaped wording means in the current claim without treating *role* as one technical kind. |
| `A.6.F` | Use its distinctions for function-shaped wording, including metonymy and multiple readings; the familiar count is only a recall cue. |
| `F.18` | Use it for durable reusable names after kind and use are known. |
| `A.6.P` | Use it when the remaining content hides relation kind, endpoint, basedness, anchoring, current ontic slot, relation position, or use relation. |
| `A.19.SPR`, `C.2.P`, `C.16.P`, `C.30.P` | For remaining state-family, source or publication, characteristic or scale, and architecture or structure wording, use the corresponding pattern. |
| `E.21` | An `E.21` evaluation may use `F.19` findings through `PrecisionRestorationProfile` and lower affected quality coordinates without creating one coordinate per apparatus symptom. |
| `E.19`, `E.22`, `E.23` | During review, framing, or improvement-loop work, use `F.19` while keeping quality-loop records out of pattern prose. |
| `E.11` and `I.2` | Use their first-entry cues and expanded entry-disambiguation cases for phrase-level apparatus repair. |

### F.19:End

