## E.8 - FPF Authoring Conventions & Style Guide

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)

### E.8:0 - Use this when

Use `E.8` when you are writing, revising, or reviewing one FPF pattern and need to know what shape, voice, reader-recognition function, and assurance material the pattern must carry before it can be treated as mature FPF text.

Use it especially when a draft is technically correct but hard to use: the cold reader cannot tell when to apply it, what action to take, what mistake that action prevents, which related pattern defines or constrains a specific outside claim, or which assurance material is informative rather than the first user-facing guidance.

**Not this pattern when.** Use `E.9` when the main work is deciding why FPF should change and how that decision is distributed across patterns. Use `E.19` when the main work is an admission or refresh review. Use the local domain pattern when the question is what FPF says inside that domain rather than how a pattern should be authored.

### E.8:0.1 - What goes wrong if missed

A pattern can satisfy a checklist and still be practically unreadable. It may open with package architecture instead of a recognisable working moment, bury its payoff, hide the pattern that defines or constrains a specific outside claim, or let assurance prose silently replace the reader-facing claim. The result is a formally neat text that authors can defend but practitioners cannot reliably use.

### E.8:0.2 - What this buys

`E.8` gives FPF authors one shared pattern shape and one shared authoring discipline: recognition text first, assurance text second, canonical sections present, terminology kept stable, SoTA used as current practice grounding rather than decoration, and practical consequences visible before a reader has to reconstruct the architecture.

**First useful move.** Put the working situation, first action-guiding move, practical payoff, ordinary boundary, and nearest heavier assurance condition into the recognition text before tightening template details or conformance material.

**Solution and working move.** `Solution` gives the pattern's conditional answer to its `Problem frame`, `Problem`, and `Forces`: what the reader should do or decide, under which conditions, what result to seek, and when to stop or return. A **working move** is ordinary reader-facing wording for one such action or judgement. Reserve `U.Move`, dated `U.Work`, and `U.Transformation` for claims that actually assert those admitted objects. `E.11.PUA` governs use of one selected `Solution` to reach the first useful result. When alternatives are formally qualified under `A.22.CGUS`, call them `continuation candidates`; `E.18.3` applies only when the selected CGUS uses a qualifying transformation-flow substrate.

**Move wording in pattern prose.** In ordinary prose, say **recommend this pattern use**, **coordinate these uses**, or **show their total order** when those are the actual claims. When the durable governed object matters, use its exact published designation under `E.11.PUR`: `PatternUseRecommendation@Context`, `PatternUseCoordination@Context`, or `PatternUseSequence@Context`; the suffix is retrieval wording, and the sequence designation requires an admitted total order for the named use. For any other claim, recover the actual relation under its governing pattern. State what cited content contributes and use `E.10.MOVE` when the current relation remains unclear.

**Cheap stop.** If the draft already gives a cold reader the working situation, first useful move, practical payoff, ordinary boundary, and nearest heavier assurance condition, do not add more authoring apparatus just to look mature. Use conformance material to verify that guidance; do not let it replace the guidance.

**FPF-governed wording extension.** Add heavier assurance, conformance, SoTA, or relation material only when it changes correctness or use: it repairs a false claim, stabilizes the primary `EntityOfConcern`, supplies a missing concrete contribution, grounds a practical payoff, or states an action-changing boundary. Cite the exact pattern that defines or constrains the live value.

When an authoring pass claims quality improvement rather than ordinary drafting, keep these pattern responsibilities distinct: `E.22` frames the improvement-oriented quality-evaluation question, the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings, `C.16.Q` repairs overloaded quality and evaluative-characterization wording, `C.25` carries engineering quality-family endpoints when those endpoints are claimed, and `E.23` governs any repeated quality-improvement method. Closing checklist rows or satisfying a review profile is not by itself quality improvement.

When a pattern claims practical payoff through a visible score or other proxy, name the intended value and the relation by which the proxy bears on it. If the proxy is being treated as the value itself, apply `E.13` before admitting the payoff claim.


**Quality or projection evidence placement.** Development, quality-review, projection, assembly, and landing evidence belongs in its own evaluation, review, projection, or release carrier rather than in the pattern body. Keep it in a pattern only when that work is the pattern's declared `EntityOfConcern` and intended-reader use. A Part E pattern may govern FPF authoring, review, evaluation, entry, or publication, but it does not narrate the development of its own current version. Judge placement by the sentence's use, not by a blacklist of words.

**Pattern positions across coupled flows.** During drafting, `E.21` questions may guide a focused author-side check. A product-level conclusion still requires an independent `E.21` evaluation and the applicable `E.19` admission review. Keep their objects and evidence distinct even when an applicable flow relation connects drafting, review, publication, use, and later refresh. A publication may guide or constrain later Work; assert the actual Work and its evidence only through the patterns that admit those claims.

**Maturity rule.** Section completeness is not pattern maturity. A pattern matures when its `Problem frame`, `Solution`, worked cases, boundaries, source/SoTA use, relations, consequences, and conformance checks all point to the same usable action guidance for the declared reader and use. If the reader still needs the DRR, source notes, campaign handoff, or author memory to know what to do, the pattern is not mature for that use.

**Primary EntityOfConcern in plain terms.** The primary `EntityOfConcern` of `E.8` is the authored FPF pattern: its canonical sections, reader-recognition function, wording discipline, examples, rationale, anti-patterns, SoTA-Echoing, and relations.

**Primary working reader.** The first reader is an FPF author or reviewer shaping pattern prose for later practitioners and managers. The downstream practitioner is the reader the pattern must ultimately serve, so the authoring guide must model the same recognition discipline it requires.

### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern supplies action- or judgement-guiding content for a recurring working situation. In ordinary phrases such as “use this pattern” and “apply this pattern”, the acting participant is the person or other capable system; the pattern is the guidance that participant uses.

Call the pattern content a `U.MethodDescription` only when it describes one independently admitted `U.Method` under A.3.2 and that distinction matters to the current claim. Keep the Method and its description episteme separate. A `Solution` can guide future action or help choose a Method without establishing that any dated Work has happened. The intended reader, an actual performer System, local system-role classification, assignment, capability, responsibility, authority, result, and Transformation remain separate whenever those claims are current.

When a pattern or worked case does assert dated `U.Work`, first recover every actual performer's A.13 core: the admitted `U.System`, local agential kind and criterion, classification, same obtaining assignment, scope, working situation, window, and adequate core evidence; add a characteristic profile only when its own receiving use consumes it. Then independently admit the Work under A.15.1 from its performance history, enacted Method, time, and containing System. Add F.6 afterward only when the pattern also needs precise assignment-bound attribution through that same assignment. A short practitioner sentence may omit identifiers unused by its receiving claim only when every relation the claim consumes remains recoverable.

`Pattern application` is ordinary shorthand for user-side use: a user or another capable system recognizes the situation and uses the pattern's `Solution` to choose the next action or judgement. The pattern body is description-side guidance. Assert a performer, assignment, dated `U.Work`, result, or `U.Transformation` only when independently established and material to the receiving claim; a `Conformance Checklist` checks the authored description and evidenced use but does not replace the `Solution`.

The pattern's main job is constructive action or judgement guidance. In the opening `Problem frame` and `Solution`, state the primary `EntityOfConcern`, first admissible move, first useful result or practical delta, and only the boundaries that change that move. Error prevention, auditability, conformance evidence, citations, and architecture rationale remain secondary. Repeat another source's distinction only when it adds a local action, case, evidence value, or recognition needed on first reading. State what this pattern governs; do not surround it with an unbounded catalogue of other things.

Name an FPF object by its known kind and state the relation the sentence actually uses. For a neighbouring pattern, state its concrete contribution and cite the PatternID; identify an exact episteme, `ClaimGraph`, edition, or relation assertion only when that identity changes the receiving use. Put detailed discovery in its dedicated carriers, including README, ToC, `E.11`, and `I.2`, and keep compact pattern relations late in `Relations`. Do not repeat the same boundary or reference family in small prose variants.

Use `E.8` to keep the pattern's positive subject and action guidance first. Apply `F.19` once to each changed natural span as the common precise-plain-language pass. Its connected reading owns language-general semantic completeness and contribution, coordination and foregrounding repair, kind and loss preservation, and local revalidation after wording changes. These facets form one connected `F.19` reading, not separate `E.8` checks.

For FPF authoring, `E.8` adds the pattern-specific question: can the intended reader still recognize this pattern's `EntityOfConcern`, working situation, first action or judgement, first useful result, and action-changing boundary before optional modeling and assurance? A cold reader must recover that path from the pattern body; `F.19` governs the sentence-level recovery. Do not copy its method, regression table, or result boundary into a local authoring profile.

If the `F.19` reading leaves an FPF value unresolved, take the exact `E.10`, `E.10.ARCH`, `E.10.ROLE`, `A.6.F`, `F.18`, or subject-pattern route and state that source's concrete contribution. Ordinary PatternID citation and “use this pattern” wording remain ordinary; use an identity-bearing MethodDescription or dated Work claim only when the selected route requires it. Keep development and release evidence outside practitioner guidance unless rewritten as the user's action or boundary.
When an action-adjacent pattern classifies wording or another semio-facing object, connect that classification to the reader's current action. State the admissible use now and any independently grounded boundary that changes that use. Route any other genuinely live claim to the FPF pattern that defines or constrains it.

`Semio-Echoing` is admissible only for one grounded wording-use overread that changes the reader's action or boundary. Keep the pattern's own `EntityOfConcern`, positive move, and result primary. Use a thin cue to the exact subject pattern only when its contribution is needed; do not add a generic counterreading catalogue.

### E.8:1 - Problem frame
FPF grows through patterns written and revised by authors from many
disciplines. Without a shared structure, practitioner-facing use order, and
semantic writing discipline, the framework would fracture or become formally
uniform but harder to use, violating Pillars **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**.

### E.8:2 - Problem
*Structural drift*, *stylistic fragmentation*, and revision by visible proxies
rather than working use threaten five qualities:

1. **Comparability** – readers cannot align patterns lacking common
   headings.
2. **Narrative cohesion** – prose swings from dry jargon to informal
   blog style.
3. **Practitioner use across revisions** – cleanup can erase the recognizable
   situation, first action or judgement, first useful result, ordinary boundary,
   or affordable stop while leaving a tidier-looking text.
4. **Semantic and relation clarity** – generic heads, false agency, imprecise
   neighboring-pattern contributions, and drifting package or relation words can
   change what the prose asserts or what a reader may do.
5. **Reviewability after guidance** – missing or misplaced grounding, boundary,
   SoTA, conformance, assurance, and publication-reference material can hide a
   defect or replace the positive guidance it is meant to verify.

### E.8:3 - Forces

| Force | Tension |
|-------|---------|
| **Uniformity vs Expressiveness** | Consistent template ↔ freedom for diverse domains. |
| **Rigor vs Readability** | Formal precision ↔ engaging prose. |
| **Brevity vs Completeness** | Concise patterns ↔ mandated safety subsections. |

### E.8:4 - Solution — One template, enriched by style principles

#### E.8:4.1 - Canonical Pattern Template
Within each pattern, the **canonical** section headings **SHALL** appear in the order below.
For each **canonical content section heading (1–12)**, the `<Title>` component (after the heading separator, e.g. ` - `) **MUST** start with the canonical section title (case-insensitive match; canonical capitalisation preferred); an optional clarifier after an em dash is allowed (e.g., `Solution — …`).
The mandatory **Footer marker** (section **13**) is the final sentinel and is governed by **H-9** rather than the standard `<FullId> - <Title>` shape.

**Extensibility.**
Authors **MAY** add additional sections. Prefer expressing them as subsections under the nearest canonical section (e.g., `4.1`, `4.1.1` under *Solution*). If an additional pattern-level section is necessary, it **MUST NOT** delete or reorder the canonical sections and its title **MUST NOT** shadow a canonical title.

**Mandatory vs optional.**
* Canonical sections **1–13** are mandatory in every pattern.
* Canonical sections carry content. Authors must not use omission placeholders as section substitutes; when a section is intrinsically small, write the smallest content-bearing grounding, misuse, boundary, or reduced-case statement that preserves the section's function.
* **First substantive authoring seed.** The first non-empty authored body of a pattern **SHALL** already instantiate the canonical section frame by value: title line, header block, canonical sections **1–13**, and the footer marker.
* **Seed is not maturity.** The canonical frame is a minimum authoring seed, not a mature pattern claim. Before a pattern is used for public, teaching, enterprise, reliance-bearing, landing-input, release-input, or ordinary practitioner guidance, each canonical section must carry enough recognition, action guidance, worked material, source/SoTA use, boundary, consequence, and relation content for the declared use. A material maturity, readiness, admission, or landing claim also needs the independent complete `E.21` result selected for that conclusion; an author-side provisional pass or focused repair check does not supply it. A file with correct headings, thin bullets, scenario labels, or compressed DRR recap remains a pattern seed until that content is present or the package explicitly marks it as `seedOnly`.
* Recognition openings and first-minute working guidance belong **inside** that canonical frame. Any retained pre-template entry material must also stay inside that same canonical frame rather than appearing as one pre-template opening memo. Authors **MUST NOT** seed one pre-template opening memo and postpone canonical sectioning, `Conformance Checklist`, or footer-marker installation to one separate `E.19`, assembly, or review-repair pass.

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell-Show-Show; at least one content-bearing grounding slice, reduced grounding case, or ordinary/non-use boundary)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (grounded misuse, text-invited misreading, or a decision-relevant non-use boundary under `CC-SG.11`)
9. **Consequences**
10. **Rationale**
11. **SoTA-Echoing** (current-best problem answer; by-value comparison at comparable effort; explicit trade-off and adopt/adapt/reject decision whenever external or internal practice changes the Solution)
12. **Relations**
13. **Footer marker**

**Footer marker.** End each pattern with a single visible sentinel heading line by itself: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or shown by editors. The footer marker is intentionally content-free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H-1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H-9**, not by the standard `<FullId> - <Title>` shape.

**H-2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Previously authored text may use Unicode dash variants such as ` – ` or ` — ` as separators; tooling **SHOULD** treat those variants as migration candidates, and authors **SHOULD** migrate touched headings to ` - `.

**H-3 (FullId).** `FullId` is the complete address used by this heading grammar.
For a **pattern heading** it is the PatternID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot-separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H-9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in PatternIDs.

PatternID segments may be numeric or mnemonic. When the surrounding text identifies the framework, the complete PatternID identifies one pattern in that framework; the shape of its segments does not by itself state the pattern's title, meaning, Part, publication position, dependency, Method relation, or use order. A mnemonic segment may help recognition but does not define the pattern.

Whether a PatternID stays with a changed pattern is an authoring decision, not a grammar decision. For a DPF, use `E.4.DPF`; use `E.11.PFP` to show current publication position separately. When the surrounding text does not already identify the framework, name the framework together with the PatternID. Add the edition when the reference must select the body published in one edition.

**H-4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in previously authored patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H-9**).

**H-5 (Where kind and normativity are declared).** Pattern **kind** (for example, Architectural or Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** or **informative**) **MUST** also be declared in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading, for example `(informative)` or `(non‑normative)`, but headings **MUST NOT** use square‑bracket tags.

**H-6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H-7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H-8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published pattern or companion texts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)`, `0..1 (partial)`, or `0..n` over deontic adjectives like “mandatory or optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility or validity constraints as predicates (`Definition:`, `Invariant:`, or `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate with a truth condition (optionally quantified), for example “every selected interval lies within the declared qualification window”, rather than as “X MUST …”.
* If the constraint needs to be checked as part of pattern conformance, authors **SHOULD** reference the predicate identifier from the Conformance Checklist, and call out validator behaviour when relevant, rather than duplicating the predicate with RFC keywords.

**H-9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags):
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

**H-10 (Publication-token classification and addressability).** Before emitting an FPF-governed token as a reference, authors **MUST** classify it under exactly one of these seven E.8-local publication-token classes and use the matching form:

- `PatternRef` uses one PatternID to name a pattern that continues across editions of the framework identified by the surrounding text. In the assembled publication being checked, it resolves to one complete H2 body, one matching `:End`, and a truthful ToC status for that PatternID. A reference intended to select the body published in one edition also names that framework edition. A structural checker may verify and report publication conformance but does not establish the pattern's identity, status, or authority.
- `PlannedCatalogEntry` names an explicit future catalogue commitment. It has no current pattern semantics, governing force, prerequisite force, or addressable body; a useful prose mention **MUST** say `planned` or `future`, and a current semantic dependency **MUST** cite existing content that supplies the needed definition, constraint, test, method, or other rule, or state the current gap.
- `SectionRef` names one exact heading path inside one current pattern. Authors and tooling **MUST** read the complete section identifier before examining any substring.
- `LocalDeclaredId` names an exact declaration within one pattern, such as a conformance clause, component, interface row, or predicate. Its scope is local unless an explicit stable anchor or a separate promotion decision establishes wider use.
- `LocalAlias` names an explicitly declared compatibility alias and resolves to its declared canonical local target.
- `PatternFamilySelector` selects a navigable pattern family using canonical spelling `<base>.*`. It requires a current base pattern and at least one current matching member and **MUST NOT** stand in for one exact governing target.
- `NonReferenceToken` classifies a schematic example or ordinary local prose/code that neither occupies a reference-bearing position nor declares a local public ID. It explicitly denotes no reference; key-like typography or backticks alone do not change that class.

Resolution and checking are declaration-first and context-sensitive. Authors and tooling **MUST NOT** split complete SectionRefs, strip a local-ID prefix, promote a local symbol by visual resemblance, or replace these classes with an ignore list. An unresolved token in a reference-bearing authoring form is an error; ordinary code or local wording is not silently upgraded to a reference.

**H-11 (Assembled Part boundaries and title agreement).** In the assembled publication, every compact ToC Part label **MUST** be a bold separator with a blank line on both sides, not a duplicate structural Part heading. Its title and ASCII ` - ` separator **MUST** agree exactly with the corresponding `# Part <letter> - <title>` body heading. A reserved body Part that has no compact ToC table, including current Part H, does not require an empty compact label or table.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere and requires every heading to carry content-bearing grounding, boundary, consequence, rationale, source-use, relation, or reduced-case material rather than an omission placeholder.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF uses *Problem frame* because generic `Context` and universal `U.BoundedContext` do not identify the actual value a claim needs.

Route each use directly. Recover source-local meaning through `F.0.1`, use `F.1` to select answer-changing sources, state `ClaimScope` through `A.2.6`, and use `A.1.1` for an admitted bounded-model use. Add `F.17` only when a durable address or basis relation is needed, `F.9` only for an obtaining Bridge between two exact local senses, and the applicable plane relation for a `ReferencePlane` claim. Otherwise leave the relation unasserted rather than inferring it from a shared word, source, or context.


#### E.8:4.1.2 - Preserve Pattern Use Value Across Material Revisions

A revision is material when the actual change can alter what a working reader recognizes, does, obtains, or must stop doing, regardless of whether the change is labelled as cleanup, clarification, terminology repair, or ontology alignment. Treat the revision as material when it can change at least one of these values:

- the primary `EntityOfConcern`, governed kind, direct relation, claim kind, or scope;
- the recurring situation or practical question that lets a reader recognize the use;
- a Solution action, action condition, result kind, first useful result, stop, return, risk disclosure, or stronger-neighbor handoff;
- the definition, constraint, test, method, cited-pattern contribution, split, merge, relocation, or source/SoTA stance that changes what the reader may do;
- the asserted commonality, member set, membership rule, order, or governing premise of a list; or
- ordinary first-use affordability.

For this comparison, the **earlier edition** is the exact accepted pattern edition that this candidate is intended to replace for the declared use. A formatting correction, spelling repair, citation repair, exact mechanical rendering, or wording change is `not triggered` only when the smallest comparison of the earlier edition and proposed text shows that all these values are preserved. A clean comparison needs no additional positive ledger, evidence table, or pattern section. Physical line count, file size, section count, inventory rows, and the author's label for the change do not establish materiality.

**Use one bounded material-revision loop over the actual prose.** Before treating a materially revised pattern as authored:

1. Recover the useful earlier-edition use at idea level: the recognizable situation and intended reader, first admissible action or judgement, first useful result, action-changing boundary or stop, and any domain claim, example, or relation needed to perform that move. Classify a changing or disappearing earlier-edition use only as retained, a valid outcome whose defective mechanism is repaired, an explicitly authorized retirement with a corrected action or boundary, or unsupported residue.
2. Draft the candidate's positive practitioner path in domain-recognizable language before guards: governed subject, recurring problem, action the reader can take, first useful result, and next action-changing condition or stop.
3. Compare the earlier edition and proposed text at comparable application effort. Preserve every useful earlier-edition move or deliberately replace it with an at-least-equally-usable action, result, or boundary; admit a candidate-only use only from an exact accepted decision, source/SoTA stance, finding, or working need.
4. Apply `F.19` to each changed natural span. Remove exactness intensifiers, invented counterreadings, role or process wrappers, formal identities, and assurance apparatus that fail its contribution test, while preserving every kind, relation, use, and action-changing detail. Keep ordinary pattern-use wording ordinary; open a deeper FPF route only for a genuinely unresolved value.
5. Check that recognition, first action, and first useful result still precede optional modeling, evidence, conformance, and assurance work. `F.19` is the common semantic pass over the changed span; `E.10` is a cue and an exact route for residual FPF wording, not a second normal-pass algorithm.
6. For every changed public or consumed interface—entry wording, input or result, field or position meaning, action order, stop, return, or reconsideration condition—repair each determinate stale ToC or README cue, example, relation, and true direct consumer in the same authoring increment. Find consumers by the meaning they teach or use; a shared word, identifier, or nearby reference is not enough.

Earlier-edition and candidate-only uses remain different bases, and both may be present in one revision. Compare that exact earlier edition with the candidate edition. An earlier-edition use keeps its earlier-edition basis and one of the four classifications above; a candidate-only use keeps its exact accepted basis. Do not classify a candidate-only use as an earlier-edition use or invent history for it. Treat a selected use as required when its loss changes action or boundary, and as optional when it demonstrates breadth only. Backward compatibility alone is not improvement, and a candidate-only promise is not improvement until the text supports its executable use. Use desk replay by default and escalate to a cold reader, AI-agent, or observed-work check only when ambiguity or consequence justifies it. If later independent review needs a recoverable note, use the smallest existing authoring source; do not create a card, score, universal schema, or one written row per idea.

Test first-use affordability by checking whether the positive Solution supports this short rendering:

```text
recognizable situation -> proposed action or judgement -> first useful result -> next action-changing condition or stop
```

This rendering explains the pattern; it does not claim that actual work is linear. Use an optional local mantra only when it improves recall, and show one ordinary traversal only when several rows materially improve explanation; choose the smallest form that keeps the action, result, and boundary recoverable. Explanatory rows may fade as competence or task demand permits, but an independently action-changing condition or boundary may not. If the traversal itself must be a durable governed object, use the exact published `DemonstrativeUnfoldingSlice@Context` designation only after `A.22.CGUS` admits that structure for the named pattern use. Put a subject-side check immediately before the continuation it changes, and keep authoring, review, quality, and release checks outside the subject Solution.

**Resolve authoring lists with `F.19`.** When a list can change pattern use, apply the same connected `F.19` reading used for prose. `E.8` keeps only the authoring effect: put the practitioner's proposition or action before illustrative material; declare a genuinely normative closed set as closed under its governing rule; signal examples as non-exhaustive when a plausible reader could mistake them for a classification; and do not let a noun series or catalogue replace the `Solution`.

Do not add a second enumeration taxonomy or a per-member result form. `E.10` may cue a suspicious head or series, `F.19` decides its membership semantics and discourse load, and an exact subject pattern settles any unresolved kind, relation, or normative set.

#### E.8:4.1.3 - Decide Whether a Narrower Contribution Changes Practice

Use this when a broader available contribution and a proposed narrower contribution both appear to answer the same recognizable working situation. State the intended reader, use, and scope. Apply both contributions at comparable effort and find the first difference in what the reader notices or decides, does, needs or checks, obtains, or uses as a stop, return, or retry. A narrower title, domain noun, paraphrase, or extra example is not enough by itself. If no action-changing difference remains, omit or merge the narrower text and point to what already answers the situation. If the two contributions address different situations, state that boundary before deciding their relation.

An action-changing difference shows that the contribution is distinct; it does not show that the contribution is worth keeping. Retain or merge it only when the changed action, result, boundary, or saved source reconstruction is warranted and useful for the declared reader, use, and scope under the applicable domain, evidence, currentness, affordability, and architecture checks. Use only the checks that can change this decision. Repair or reject a distinct contribution that is wrong, stale, unsafe, unsupported, incompatible, or needlessly burdensome. Keep an explicit gap when no acceptable contribution answers the situation.

Naming a dependency does not settle the comparison. Say which available result supplies the reusable part, what kind of result it is, which product and edition or current state supplies it, how the reader uses it, and which currentness or availability condition can change that use. State maintenance separately only when it changes the receiving use. Then preserve any remaining domain problem, filling, constraint, relation, evidence limit, return, or discovery need without copying the general rule.

When reuse or a gap closes the reader's question, state which of these is actually true:

1. **Use an available result.** Name the result, what kind of result it is, the product and edition or current state that supplies it, the receiving use, and any currentness or availability condition that can change that use. The supplying product may be an FPF, DPF, LPF, or a separate non-framework product. If maintenance changes the use, state its separately established relation and evidence.
2. **Use a MethodDescription.** Name the public description, the Method it describes, and how the reader uses the description to select or perform that Method. State availability, currentness, or a separately established maintenance fact only when it changes that use. Do not report the expected result as already obtained.
3. **Use a direct source as evidence.** Name the source, the claim or decision it supports, the receiving use, its limits, and a usable locator. Source availability is not result production.
4. **State a named unavailable result.** Name what is missing, the action or decision it blocks, the missing condition, and the observable condition for retry.

For example, "feed the animals" may be true for both a mouse and a tiger yet fail to tell the feeder what food to give. Grain and meat change the action, so keep or link the animal-specific guidance when that difference is warranted for the declared use.

By contrast, a pump-maintenance restatement of an available evidence-use contribution adds nothing if it changes only pump nouns and one example. Omit or merge the restatement, point to the maintained result that already answers the situation, and judge any promised maintenance-framework coverage separately.

A tiger-feeding proposal may instead require manager approval and a laboratory certificate before every ordinary feeding. That proposal changes the feeder's action, but if no safety rule, evidence limit, law, or observed failure warrants the burden for the declared use, reject it or repair it to the smallest warranted check. Distinctness alone does not preserve it.

A result maintained outside the receiving framework may answer the reader's use without becoming part of that framework. In a package-coverage account, count that external result only when the exact result and supplying product, receiving use, practical discovery route, and any material currentness or availability condition are explicit, and say that the result remains external. Otherwise keep the promised family as a gap or omission. When the resulting stable pattern set materially changes a promised problem family, obtain a current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition. Reuse a matching current result when the exact edition, promised families, declared use, relied-on results, and relevant conditions did not change; do not record proof that a revisit happened.

#### E.8:4.2 - Stylistic Principles (S-0 ... S-19)

| # | Principle | Guideline |
|---|-----------|-----------|
| S-0 | Governing-claim flow | Begin with the recognisable working situation and governing claim or action. Add context, grounding, examples, and a closing line only when they help the reader understand or use that claim. |
| S-1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S-2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S-3 | Embedded Mini-Definitions | Gloss a new term in parentheses on first appearance. |
| S-4 | Contextualisation | Brief historical or disciplinary lineage references. |
| S-5 | Grounded Clarification | State the pattern's positive object and move first. Apply the `F.19` plausible-reader guard test; retain a local negative boundary only for a grounded misreading that changes understanding or action. |
| S-6 | Earned closing line | End when the result or boundary is clear. Add a memorable closing line only when it reinforces that result without introducing a new claim or displacing the practical close. |
| S-7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S-8 | Grounded transfer examples | Use examples from other fields when the pattern claims transfer breadth and each example changes recognition, application, or a boundary. No fixed example count establishes breadth. |
| S-9 | Physical Grounding Reference | Tie an abstraction to the actual system doing the work and to the holon or physical process it changes. Mention a local transformer system-role classification or an obtaining assignment only when it changes the claim; ordinary *transformer* may remain readable metonymy for that system. |
| S-10 | Readable blocks | Keep the governing claim with the explanation needed to use it. Split prose or use a list only when that structure makes the reader's work easier; no sentence or item count is a verdict. |
| S-11 | Narrative Flow | Foreground the governing practitioner claim or action and let the section read as a continuous explanation. Apply `F.19` when coordination, catalogues, or modifiers create bullet soup or delay that message. |
| S-12 | Full claims over tags | Use a clause when a list item carries a claim or action. Labels, values, and locally complete steps need no artificial subject-and-verb expansion; item count and sentence count are not verdicts. Use the `F.19` contribution and list tests. |
| S-13 | SoTA-Echo structure | Name the practice question, selected best-known line, serious alternative or default, defect overcome, exact pattern mutation, source roles and limits, and reopen condition. Assign roles from answer-changing content, not authority, prevalence, freshness, or praise: an official source may be the best-known line if its answer wins; lineage-only and identity/currentness-only material stays outside. |
| S-14 | Didactic-content sufficiency | New and substantially revised patterns carry enough didactic content to be teachable without nearby project notes. |
| S-15 | Worked slices over scenario labels | Transform-like families show at least one concrete source and resulting-publication slice; scenario names alone are not enough. |
| S-16 | Ordinary vs FPF-governed wording realism | Keep ordinary use light, and make heavier review records explicit only for disputed, high-risk, or higher-impact cases. |
| S-17 | Self-contained monolith prose | A merged pattern must explain itself inside the monolith; planning shorthand and review-context dependencies are not admissible in pattern prose. |
| S-18 | Intended-reader discipline | Keep every pattern host or monolith section addressed to the intended FPF user; move package-development, architecture-placement rationale, developer, reviewer, and executor correspondence, and quality or projection evidence to separate companion, evaluation, review, projection, or release carriers unless the sentence has been rewritten as the user's admissible move or boundary. |
| S-19 | Precision before relaxation | Apply the connected `F.19` reading and kind/loss comparison before accepting a plain or didactic rewrite. Route only an unresolved FPF head, qualifier, relation, or admissible-use question to `E.10`, `E.10.ARCH`, or its subject pattern. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight. Engagement remains subordinate to semantic discipline: hooks, quotable lines, Plain restatements, and didactic images may improve recognition, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim kind or admissible-use boundary they carry must be recoverable through the governed Tech reading or named neighboring pattern. Ordinary Plain prose without that claim kind or admissible-use boundary stays ordinary prose.

**S-0 (Governing-claim flow) — explanation**

Open with the recognisable working situation and the claim or action that governs the passage. Add history, related patterns, examples, imagery, or a recall line only when it helps the intended reader understand or use that claim. A prerequisite may come first when the reader needs it to interpret the claim or act safely. Apply `F.19` when atmosphere, coordination, or rhetorical scaffolding delays the governing message.

#### E.8:4.2.1 - Recognition text and assurance text
Every canonical pattern SHALL stabilise one primary `EntityOfConcern`, relation record, or claim record early enough that a cold reader can tell what kind of thing the pattern is actually governing. If ordinary forms vary (`note`, `sheet`, `guided UI`, `rendering`, `review aid`), the text must make explicit which of those are merely presentation forms of one primary selected EntityOfConcern, relation, or claim and which would instead name a different act, process, work-result record, or governing companion. Recognition and assurance texts may refine that selected item differently, but they must not silently swap the central kind.

If a pattern uses a broad umbrella or head together with a narrower operative branch, the text must also make the stack explicit early enough for first reading: what the broad head names, what the current narrowed branch is, what primary `EntityOfConcern`, relation record, or claim record is actually in play, what exact action assertion and predicate are current, and what wider work or process remains outside the pattern. A qualifier alone does not restore that stack.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `recognition shell` and `assurance shell` wording is retired.
These names refer to two reading-order functions carried by existing sections or projections inside one pattern; they do **not** mint new `authoritySourceRef` targets, generic neighboring-pattern relations, publication-form or face kinds, `publication-face kind`s, or a second face family.
A third didactic-content function remains optional and is justified only when the family is especially easy to misuse, easy to over-read, or hard to teach without extra scaffolding.

The **recognition text** is the first-reading text.
It is the part of the pattern that lets a cold working reader recognise the situation quickly enough to decide whether to keep reading.
It should start from a subject-domain or practice moment before internal taxonomy whenever the pattern is meant to help real work rather than only internal canon maintenance.
In practice it usually appears in an early `Use this when` line or equivalent opening, plus the upper parts of `Problem frame`, `Problem`, `Solution`, `Consequences`, and nearby worked slices.
Its job is to make visible:
- what ordinary working situation this pattern is for;
- what goes wrong if the pattern is missed;
- what the pattern buys the reader in practice;
- when this is not the right pattern;
- what primary `EntityOfConcern`, relation record, or claim record is actually being kept stable;
- and, when technical terms must appear early, a pairwise plain gloss for each early FPF-governed technical term.

The **assurance text** is the second-reading text.
It carries the heavier FPF-governed material that makes the pattern reviewable and auditable:
- declaration blocks and typed fields when those are part of the pattern's declared conformance or boundary claim;
- representation ontology, EntityOfConcern discipline, or primary-EntityOfConcern discipline;
- any minimal modeling or mathematical lens that keeps the primary `EntityOfConcern`, relation record, or claim record stable;
- guidance or check material, invariants, admissibility, and stop or neighbouring-pattern conditions;
- `SoTA-Echoing` when it carries explanatory work;
- and the review hooks that let a broader or more consequential interpretation or use be checked explicitly.

The assurance text may sharpen, justify, and discipline the recognition text.
It must **not** silently replace, strengthen, or universalize the claim that the recognition text made visible.
If the recognition text says “this pattern helps with a bounded working situation”, the assurance text must not quietly turn that into an unbacked carrier claim, unbacked guarantee, or broader universality claim.

If a pattern claims **universal** or **transdisciplinary** status, that claim must already be visible in the recognition text.
It is not enough for universality to appear only later in a guidance or check sheet, declaration block, or `SoTA-Echoing` rationale.
A broad claim should therefore be demonstrated in the recognition text through **heterogeneous reader or domain situations adequate to the claimed breadth**. The separate three-domain minimum in `A.8` applies to universal-core U-kind admission.
When a compact matrix helps, `F.16` is the preferred template for showing that breadth.
If `SoTA-Echoing` carries an FPF-governed claim, the practical implication of those rows should be recoverable from the recognition text and case bank rather than remaining a late-only justification layer.

A **third didactic-content function** means enough didactic and operational content that the pattern survives without nearby project documents. Typical indicators include:
- at least one concrete source and resulting-publication slice in Archetypal Grounding when the pattern defines or constrains transforms or publication change;
- at least one boundary-heavy example or anti-example when nearby or companion patterns are easy to confuse;
- reviewer guidance that tells what to inspect first and which neighboring FPF pattern defines or constrains the failure mode and which project-side FPF kind and reference named by value carries the claim or effect;
- local mini-definitions or glossary material for recurring terms that would otherwise be recovered only from project context.

Pattern density is therefore not “more metadata” and not “longer tag lists”. It is the presence of enough recognition, assurance, and, when needed, extra didactic material that a reader can understand the pattern, apply it lightly in ordinary cases, and recognise when a heavier review profile is required.

#### E.8:4.2.2 - Package-form and neighboring-pattern reference discipline

FPF package-form words and neighbouring-pattern references carry stable meanings. State the actual relation used by the sentence, and use the exact subject pattern when that relation is not recoverable from ordinary wording.

For an ordinary neighbouring-pattern reference, state the concrete contribution and cite the PatternID. An identifier or locator only helps the reader find that content. Identify an exact claim-bearing episteme, `ClaimGraph`, edition, or relation assertion only when a named later use depends on that identity.

A local `...PatternLocator` field may remain where an existing schema already uses it as a non-semantic convenience, but ordinary prose and entry cues do not require one. It never substitutes for the cited content's concrete contribution or, when the stronger identity branch is active, for the exact claim-bearing content. Changing only a locator without changing what it resolves is a representation change; changing the defining content or exact assertion may reopen the semantic object whose receiving use depends on it.

Keep the following package and relation words distinct:

- **pattern reference** = an ordinary citation to content whose concrete contribution is stated in the current sentence;
- **specialization** = an exact relation in which the child carries the required parent content plus an explicit child delta and use boundary;
- **overlay** = a cross-cutting reading or review projection over stated source content; it adds no authority or obtaining relation by name;
- **profile** = a declarative bounded-use or review projection from stated source content, not a replacement pattern or actor;
- **family** = a recurring class of cases under an explicit membership rule, not a hidden common owner;
- **bundle** = a packaged set of defaults, allowances, or coordinated members whose actual relations remain explicit;
- **cluster** = a navigation or reading-order grouping, with no semantic relation by grouping alone;
- **suite** = a coordinated set whose suite-level membership and coordination semantics are explicitly stated;
- **pack** = an editorial, source, review, or delivery grouping, not semantic authority;
- **kit** = a reusable coordinated publication or boundary-description package with exact kit-level membership and use;
- **record** = a case, report, assertion, representation, or review record under its own identity;
- **umbrella** = a provisional review head spanning possible subfamilies before an exact membership rule and the relevant claims and relations are settled.

These words are not interchangeable and do not stand in for a missing relation. Say `specialization of ... with delta ...`, `profile projecting ... for use ...`, `overlay reading ...`, `bundle containing ... under membership rule ...`, or another exact formulation. A source-defined position name may be reused when the cited content defines that position and the current assertion uses it in that sense; otherwise recover the meaning through `E.10.ROLE` and do not improvise near-synonyms for stylistic variety. The preceding receiving-use discriminator decides whether exact claim-bearing content must also be identified.

##### E.8:4.2.2.1 - Precision-restoration placement discipline

When a pattern or companion text is drafted from `E.10` or `E.10.ARCH`, distinguish two authoring objects:

* **`semanticArea`** is the Part-F semantic unit for a wording-use restoration row: one Concept-Set row, one UTS row, or an explicitly bounded row-set. It is declared with `semanticAreaBaseConcept` and `semanticAreaSenseFamily`.
* **`ontologicalNeighborhood`** is the applicability neighborhood around that named `semanticArea`: nearby primary `EntityOfConcern` kinds, relation kinds, claim records, content that defines or constrains the current use, non-use boundaries, and remaining reader use that can carry the recovered meaning after the wording is repaired.
* **`pattern nest`** is the publication and specialization placement of a pattern under a declared family or membership relation.

These are not synonyms. A precision-restoration pattern is placed in the pattern nest whose primary `EntityOfConcern`, relation record, or claim record it repairs. Its `semanticArea` states the Part-F semantic unit it repairs, while its `ontologicalNeighborhood` may name several direct relations and pattern content that defines or constrains the asserted uses. For example, quality-term repair lives in the `C.16` characterization nest, even though its neighbouring relations can include relation construction, action invitation, evidence, assurance, source-use assignment, engineering quality bundles, pattern-quality evaluation, or mathematical-lens use.

Affected patterns should use a thin pointer when the first-stage wording repair belongs elsewhere. The pointer names the selected restoration pattern and the condition that triggers it; it does not copy the trigger registry, the full `E.10.ARCH` recovery algorithm, or a second local architecture for the same repair. The affected pattern then keeps its own subject matter: the characteristic, structure, view, episteme, relation, evidence, assurance, gate, work, decision, or adequacy question it already governs.

If a draft proposes a new precision-restoration pattern, the authoring claim must show the repeated wording failure, `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, the recovered primary `EntityOfConcern` kind or relation/claim record, the intended pattern nest, the neighboring governing relations, and the admissible action left after repair. A new pattern is not justified merely because a word appears often, because a local checklist wants a bucket, or because a campaign needs a tidy grouping.

#### E.8:4.2.3 - Intended-reader discipline for pattern prose

A pattern is written for its intended FPF user: the person who will use the pattern to organise thought, inspect a case, publish a note, or review a result under that pattern.
Its FPF-governed sections explain the user's action, result, cost, and any grounded boundary that changes use. When neighbouring or companion patterns are named, answer the concrete reader question their contribution settles rather than narrating why the package architecture was divided that way.
`E.8` reader and reviewer wording is FPF pattern-authoring wording. Project-side publication readers, explanation readers, comparative review units, and participants in named project-side review relations are governed by the publication or project-side patterns that name those publication units, explanation-use relations, comparative review units, evidence paths, work records, or gate records, such as `E.17`, `E.17.ID.CR`, `E.17.EFP`, `A.10`, `A.15.4`, `A.20`, or `A.21`.

Authors must keep FPF-development or package-architecture material separate from that user-facing body.
In particular, `Problem`, `Solution`, `Consequences`, `Rationale`, worked slices, and ordinary-vs-FPF-governed wording guidance must not do the work of:
- arguing that the material is worth isolating;
- justifying overlay, profile, family, membership, or authority-reference choice as a package decision;
- discussing authority-reference freeze, naming freeze, merge state, blast radius, or safest landing form;
- or narrating future package promotion or defer decisions.

If architecture-placement commentary is still helpful, the default place is a separate companion note or ADR-like architecture note.
A pattern may include a short optional informative subsection such as `Architectural placement note (informative)` only when that placement materially helps users avoid misuse; even then, it must stay clearly separated from the user-facing solution and rationale rather than replacing them.

#### E.8:4.2.4 - Human-facing fit beyond intended-reader correctness
Human-facing fit is also subject-domain fit. A recognition text that starts from internal taxonomy, pattern-placement convenience, or package-architecture wording before the problem-domain moment is still under-authored even if its later guidance or check text is correct. When a broader umbrella name and a narrower operative branch are both used, the recognition text should also tell the reader which stack is actually active rather than leaving that reconstruction to a later declaration block or companion note.

A pattern can already address the intended reader and keep its boundaries clean, yet still fail the first minute of use for a cold working reader.
That failure usually appears when the text is admissible but does not yet make the working situation, practical payoff, primary `EntityOfConcern`, non-use boundary, or first action-guiding move visible enough.

**P-2 epistemic precision check.** When the E.10 criteria call for epistemic precision restoration in pattern prose, the first admissible action-guiding move must survive as remaining admissible reader use or be replaced by a neighboring FPF rule whose content now defines or constrains that claim application. This is a direct `E.2` `P-2` and `E.12` requirement, not an optional style preference. Intentional didactic metaphors and vivid Plain recognition lines are admissible when they are ordinary recognition aids or when their claim kind or admissible-use boundary maps back to Tech under `E.10:6.2`. A precision-corrected rewrite that leaves the recognition text inert is still under-authored.

For canonical patterns, the first-reading text should behave as a **recognition text** and the heavier review/check scope should remain in an **assurance text**.

When a pattern claims practice guidance or is meant to be used by engineers, managers, researchers, or other working readers, authors should make the following visible before the heavier harness takes over:
- a recognisable `Use this when` or equivalent first-minute recognition cue;
- a concrete working situation in `Problem frame`, not only taxonomic or pattern-placement language;
- a short statement of what goes wrong if the pattern is missed or misread;
- a short statement of what this pattern buys the reader in practice;
- the first admissible action-guiding move the user should take in that situation;
- a short `Not this pattern when` boundary for ordinary nearby non-use cases;
- one minimally viable worked case or use slice that shows what changes in practice;
- when a typed declaration block, formal lens, or other compact modeling material is FPF-governed, a short user-facing statement of what kind of object the pattern is governing and what minimal lens keeps that object reviewable;
- pairwise plain glosses for any FPF-governed technical terms that must appear before the heavier declaration content arrives;
- when `SoTA-Echoing` carries explanatory work, a short working-reader implication for each row or cluster of rows and a visible link back to the case bank or worked slices that those rows discipline;
- a visible split between the recognition text and the heavier assurance text or companion material;
- and, if the draft implicitly serves several working-reader situations, an explicit primary working reader, primary concern, or primary viewpoint.

**Problem-frame recognition signature (informative).** A canonical pattern should
expose the working situation through its `Problem frame`, not through one
separate navigation block. When an `E.11` pattern-entry discoverability problem
is present, the same `Problem frame` may also carry candidate-pattern and
tempting-wrong-pattern cues; otherwise it should stay with action guidance
rather than becoming a local catalogue row.

The local recognition signature should make recoverable:

- the concrete working situation;
- the primary `EntityOfConcern`, relation named by value, claim record, or stabilized concern;
- what goes wrong if the pattern is missed or misread;
- the first admissible action-guiding move and what that move buys;
- the ordinary not-this-pattern boundary;
- the first admissible action-guiding result; when an `E.11` discoverability
  problem is present, the first admissible entry stop or entry-stabilizing result.

`Use this pattern when`, `This pattern applies when`, or equivalent `Problem
frame` prose may be used as the first sentence or compact cue of this
signature.
It is not one separate required section.

**Entry-cue authoring rule.** Begin with one ordinary question about the user's object and claim, before any PatternID, card, template label, or internal taxonomy. In the same compact cue, state what cited content contributes, cite the pattern id, and name the smallest result usable now plus its stop or return condition. Add a tempting overread only when the `F.19` plausible-reader test finds independent local ground and an action-changing effect. Name an exact episteme, `ClaimGraph`, or edition only when a later use depends on that identity. The cue guides reading; it does not by itself constitute a result or relation.

Resolve the current head and relation under the exact subject pattern before coarsening. In an ordinary cue, state that pattern's concrete contribution and cite its id; identify exact claim-bearing content only when its identity changes the receiving use. Preserve every live status distinction defined by the subject pattern. A cue or representation supports only the object, status, or relation admitted by its governing pattern.

Compact candidate-pattern comparison belongs in `E.11`-distributed entry material; expanded entry-disambiguation cases belong in `I.2`.

If the prose points to neighbouring patterns or companion content, state whether that content defines a kind, constrains a relation, supplies a test or method, provides a project-side FPF kind and reference named by value, or supplies an `E.11` entry-recognition reclassification; do not present a citation as a hidden co-authority of the current pattern.

If the pattern claims broad, universal, or transdisciplinary usefulness, that breadth should already be visible in the recognition text.
The recognition text should show heterogeneous reader or domain situations adequate to the claimed breadth, rather than one narrow case family with a later broad claim attached.
When a compact matrix helps, `F.16` is the preferred template for making that breadth legible.

This is not a request to flatten the pattern into plain language only.
It is a rule about ordering, assurance depth, and text consistency: the recognition text must help a working reader recognise the pattern early, while the assurance text continues to carry the full claim kind or admissible-use boundary.
If the pattern uses technical lexicon, ontological distinctions, or a mathematical lens, those structures must remain recoverable, but the first-reading text should not require the reader to decode that full stack before recognising the working situation.
The assurance text may tighten or discipline the recognition text; it must not silently shift what the recognition text claimed.

**Illustrative migration example (informative).**

Old pre-template top:

```text
Start here when the dominant question is API, protocol, SLA, published boundary, or compliance wording.
First output: Claim Register.
Neighboring pattern relations and entry-recognition reclassifications: A.6.B, A.6.C.
```

Repaired Problem-frame recognition signature:

```text
Use this pattern when boundary-facing language - API, protocol, SLO/SLA, compliance clause, or other published boundary description - mixes guidance or check clauses, admissibility gates, duties, and evidence into one sentence or published boundary description.

If missed, the text becomes boundary-claim soup: runtime behavior, governance, and evidence are treated as one undifferentiated promise.

Do not use this pattern merely because the text mentions an API or boundary description. If the question is still one unstable cue, preserve it through the admissible cue-preservation line first.

First admissible action-guiding result: one `A.6.B`-governed atomic claim set or one Claim Register whose claim/use questions are explicit enough for the pattern content that defines or constrains the claim, or for a named project-side FPF kind and reference, to inspect.
```

#### E.8:4.2.5 - Design-time and run-time referents stay separated in pattern prose

Pattern prose must keep its referent index explicit. In ordinary body sections, the default truth-makers are run-time or governed-domain objects, states, moves, boundaries, consequences, and user-facing practical effects. Normative-standard wording is still admissible when the sentence is explicitly about the standard as a normative publication, for example in marked migration navigation examples, marked informative notes, or conformance/checklist clauses.

Design-time and development-state referents are different objects. The current draft, current body, current pass, author, reviewer, handoff, packet, governing companion, landing choice, or other writing-process objects must not be smuggled in as the hidden truth-condition of pattern prose. A quick test is: what makes this sentence true? If the sentence is true because the current text is arranged a certain way, because the author or reviewer must do something next, or because the current development state says so, then it is design-time residue, not pattern content.

Move that material to the authored-slice carrier, handoff, `DRR`, or companion architecture note. If a sentence is kept in the pattern, rewrite it so that its truth depends on the governed run-time/domain object or on the standard's declared normative claim set rather than on the current writing pass.

If a pattern or example claims **autonomy**, name the admitted `U.System` whose freedom of action is being evaluated and use the current `E.16` pattern that defines or tests the claim. Add another relation only when it is current under its own governing pattern. Admit dated Work under the A.13-first and independent A.15.1 rule in `E.8:0.3`, adding `F.6` only for current assignment-bound attribution. Add autonomy apparatus or a vignette only when it helps the reader use that claim. Apply `F.19` after recovery; if the corpus supplies no direct governor, return `A.6.RCD missing-governor`.

### E.8:5 - Archetypal Grounding (System and Episteme)

| Template element | `U.System` illustration | `U.Episteme` illustration |
|------------------|------------------------|---------------------------|
| Section order | Pump‑assembly pattern follows sections **1–13** and ends with its required `:End` sentinel. | Meta‑analysis pattern follows the same sections and sentinel rule. |
| S-1 Density w/o Jargon | “The pump casing seals at this face.” | “This episteme raises **F (Formality)** by making falsifiers testable.” |
| Governing-claim flow | Opens with the pump's working situation and required claim, then adds only context needed to act. | Opens with the research question and evidence claim, then adds only context needed to interpret it. |

*Note:* Prefer examples that reuse FPF characteristics vocabulary (e.g., **F (Formality)** rather than “F‑score”) unless you explicitly mean an external metric and name it as such.

### E.8:6 - Bias-Annotation
Lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for the authoring conventions in this pattern.
This guidance biases toward **Did** (readability, narrative flow) and **Arch** (template regularity) by design; the mitigation is content-bearing reduced sections and justification through the smallest grounding, misuse, boundary, or reduced-case statement, not omission placeholders.

### E.8:7 - Conformance Checklist

**CC style (canonical).**
Conformance Checklist items are authoring checks: they test whether the pattern guidance has been applied and written correctly in a pattern or companion text that claims conformance. They do not replace `Solution`, do not make the pattern a control form, and do not state deontic obligations about the modeled world. A CC clause of the form “X SHALL ...” is to be read as “In a conforming pattern or companion text, X SHALL ...”.

**Preferred wording for new or edited CC items:** start with an explicit conformance subject (e.g., “Authors ...”, “Reviewers ...”, “A conforming implementation ...”, “A validator ...”). If a CC item is enforcing an admissibility predicate, it **SHOULD** cite the predicate’s identifier (from a `Definition:` / `Invariant:` / `Well-formedness constraint:` block) rather than restating the predicate as “X MUST ...”. For boundary/interface/protocol/declaration patterns, prefer A.6.B-scoped claim IDs (L/A/D/E) or cite an existing Claim Register (A.6.B:7) instead of restating mixed prose.

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC-SG.0 (Heading discipline).** | Pattern and subsection headings **SHALL** follow **H-1 ... H-9** (FullId prefix, reserved punctuation, heading levels, ellipsis discipline). The Footer marker **SHALL** follow **H-9**. | Makes chunks self-contained; reduces ambiguity between author elision and retrieval truncation. |
| **CC-SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Title block -> ... -> Footer marker). | Guarantees structural comparability. |
| **CC-SG.1a (Initial pattern draft shape).** | The first non-empty authored version of a pattern **SHALL** already use the canonical section frame (Title block -> Footer marker). Authors **MUST NOT** start from one pre-template opening memo and promise to backfill canonical sections later. | Prevents large late-stage structural rewrites and keeps drafting aligned with `E.8` from the first substantive pass. |
| **CC-SG.2 (Grounding required).** | Every pattern **MUST** include an *Archetypal Grounding* section with at least one content-bearing Tell, Show, reduced grounding case, or ordinary/non-use boundary. A placeholder saying that grounding is absent is nonconforming. | Keeps patterns teachable and reduces "definition-only" ambiguity. |
| **CC-SG.3** | The *Bias-Annotation* section **SHALL** cite the five Principle-Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross-disciplinary neutrality explicit (ties to Guard-Rail 4). |
| **CC-SG.4** | Deontic normative sentences **MUST** use only RFC-style keywords (see **H-8**); RFC keywords **MUST NOT** appear inside `Definition:`/`Invariant:`/`Well-formedness constraint:` blocks. When enforceable, admissibility/validity predicates **SHOULD** be referenced by id from the Conformance Checklist (rather than duplicated as “X MUST ...”). Informal deontic verbs are prohibited in normative clauses. | Prevents ambiguity between obligation language and model validity; improves auditability. |
| **CC-SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S-0 ... S-19**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC-SG.6 (SoTA-Echo required).** | Every pattern **SHALL** include a **SoTA-Echoing** section. It names the practice question and either gives the smallest adequate best-known comparison or states an honest source gap. Architectural patterns **SHALL** use the full comparison contract below. A definitional pattern may use a reduced comparison, but it still names the ambiguity or terminology question, the best-known current line, the serious default it improves or rejects, and the pattern locus changed. Internal coherence, official status, or a current edition is not a substitute. | Keeps source use tied to the pattern's working problem and prevents an empty mandatory section from becoming a prestige shelf. |
| **CC-SG.7 (Current-best, by-value SoTA).** | Every positive SoTA use **SHALL** state the `practiceQuestion`, `bestKnownLine`, `seriousAlternativeOrDefault`, `defectOvercome`, `patternMutation`, `sourceRolesAndLimits`, and `reopenCondition` in ordinary readable prose. Compare the serious answers at comparable application effort, explain why the selected line is no worse on the relevant values and better on at least one or state the chosen trade-off, and mark each material move adopt, adapt, or reject with its receiving locus. | Makes the best-known-line judgement and its practical consequence independently replayable. |
| **CC-SG.7a (Typed source roles; no currentness laundering).** | Authors **MUST** distinguish best-known-line candidates, serious current rivals, failure or counterexample evidence, official or popular comparators, lineage-only sources, and identity/currentness-only sources. Official, popular, maintained, canonical, highly cited, recent, or academically praised status supplies no positive evidence of SoTA rank. These are roles in one comparison, not permanent source classes: an official or widely used source may be the best-known-line candidate only when its substantive answer wins independently of that status. Keep lineage-only and identity/currentness-only roles outside the pattern body; keep an official or popular default as comparator only when its named defect is necessary and changes a governed locus. If no adequate best-known comparison is available, state the gap instead of substituting a catalogue page, standard, or fresh paper. | Prevents source identity, prestige, prevalence, and freshness evidence from masquerading as the current best answer without excluding a source whose content actually wins. |
| **CC-SG.8 (Actual cross-local or plane relation).** | When SoTA-Echoing uses an obtaining semantic Bridge, it **MUST** identify the two exact F.17 local senses, the F.9 relation, and a separate bounded-use claim; `CL` remains optional evidence shorthand. A ReferencePlane use cites its applicable plane relation. Any penalty cites a named current policy and its applicability; none follows from context, plane, Bridge, or `CL` alone. | Safe, auditable reuse without fictitious relations or automatic penalties. |
| **CC-SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA-Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC-SG.10 (No keyword soup).** | `SoTA-Echoing` entries **MUST** state complete claims. Labels, bullets, and table cells may structure those claims but **MUST NOT** replace the practice question, selected answer, comparison, and pattern consequence with a noun catalogue. | Keeps source structure readable without forcing artificial sentence form on labels or values. |
| **CC-SG.11 (Anti-patterns).** | Every pattern **SHALL** include a **Common Anti-Patterns and How to Avoid Them** section grounded in observed misuse, a text-invited misreading by a plausible intended reader, or an ordinary non-use boundary that changes application. An already established boundary may be referenced. Apply `F.19` to the proposed contrast; neither an invented error nor a placeholder saying no anti-pattern applies supplies a useful case. | Makes relevant misuse and application boundaries recoverable without inventing an opponent or repeating a warning solely to fill the section. |
| **CC-SG.12 (Boundary claim-set discipline).** | If a pattern’s subject is a boundary, interface, API, protocol, connector, SLA, or other published boundary description, it **MUST** either (a) provide an **A.6.B**-governed atomic claim set (`L-*`/`A-*`/`D-*`/`E-*`, with stable IDs), or (b) explicitly cite an existing **A.6.B Claim Register** / scoped claim set that it reuses. | Pulls A.6.B into the authoring contour, prevents boundary-kind soup, and makes review more explicit and repeatable. |
| **CC-SG.13 (Didactic sufficiency).** | New patterns and substantial revisions **MUST** remain understandable without project-planning notes. When a pattern introduces a new named family, profile, or specialization, or adds a non-trivial note derived from another pattern, its Solution and Grounding **SHALL** carry enough didactic content: the relation to the pattern that defines or constrains the specific claim, ordinary-vs-FPF-governed wording guidance, at least one concrete source and resulting-publication slice where applicable, and visible related-pattern or project-side FPF kind and reference named by value cues. | Prevents skeleton-only patterns and project-context leakage. |
| **CC-SG.14 (Controlled prose, not free shorthand).** | FPF-governed prose **SHALL NOT** rely on bare relation words or planning shorthand whose actual relation or cited-pattern contribution is left implicit (e.g., bare “species”, “branch”, “flow”, or API-like “input/output” language). When that relation matters, authors **MUST** name it explicitly—for example, `specialization of ... with delta ...`, `profile projecting ... for use ...`, or `overlay over ...`. When a neighboring pattern supplies a definition, constraint, test, method, or lookup needed by the sentence, state that concrete contribution and cite its id. | Keeps pattern prose precise and self-identifying without inventing a universal locator relation. |
| **CC-SG.15 (Package-form and relation-word discipline).** | When a pattern names a package form or a relation within a family (`primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, `umbrella`), the chosen word **MUST** match the intended ontology and **MUST NOT** be swapped for stylistic variety or left to implication. Any cited neighboring pattern **MUST** be accompanied by its concrete contribution. | Prevents semantic blur while keeping family, membership, projection, and related-pattern relations auditable. |
| **CC-SG.16 (Intended-reader discipline).** | Every pattern section **MUST** remain user-facing. Development and package-architecture rationale or current state belongs in its companion carrier. A Part E pattern may govern authoring, review, evaluation, entry, or publication, but even there the body states the user's move rather than narrating development of that same pattern version. | Keeps pattern prose aligned with its intended reader. |
| **CC-SG.16a (Referent-index discipline in pattern prose).** | Pattern sections **MUST** keep run-time/domain referents, normative-standard referents, and design-time/development-state referents distinct. In ordinary pattern prose, sentence truth **MUST** depend on the governed run-time/domain object or on the pattern's declared normative claim set, not on the current draft state, author action, reviewer action, or development-state status. If a sentence is true only because of the current writing/review pass or text arrangement, it is design-time residue and belongs in carriers or companion notes, not in the pattern. | Prevents Conway/process leakage, DesignRunTag drift, and late cleanup before review or landing. |
| **CC-SG.16b (Quality or projection carrier separation).** | Pattern text **MUST NOT** report development, review, evaluation, projection, assembly, or landing evidence as practitioner guidance. Keep those facts in their own carriers unless that work is the pattern's declared `EntityOfConcern`, or rewrite the supported result as the user's action or boundary. | Prevents package evidence from masquerading as pattern content. |
| **CC-SG.17 (Recognition text and assurance text).** | A canonical pattern **MUST** expose recognition text before its heavier assurance text, and the latter **MUST NOT** silently change the recognized claim. The recognition text states the working situation, first move, payoff, grounded non-use boundary, and primary `EntityOfConcern` in plain user-facing terms; the assurance text supplies the typed detail and checks needed for the same claim. A claimed universal or transdisciplinary reach **MUST** be demonstrated through heterogeneous situations adequate to that claim. | Keeps the first reading usable while preserving assurance depth. |
| **CC-SG.17a (Problem-frame recognition signature and E.11 boundary).** | Authors **SHOULD** put the working situation, primary governed object or claim, first move, payoff, and ordinary non-use boundary in `Problem frame` rather than in a separate navigation block. Add entry-disambiguation cues only for an actual `E.11` discoverability problem; keep expanded cases in `I.2`. Local `Start here`, `First output`, or neighbouring-pattern blocks **SHOULD NOT** replace `Problem frame` and `Solution`. | Keeps recognition in the canonical pattern frame without turning it into a navigation catalogue. |
| **CC-SG.17b (Epistemic precision repair preserves action guidance).** | A `C.2.P` repair **MUST** preserve the first admissible action-guiding move or name the exact neighbouring pattern that now carries it. Plain or didactic wording maps back to the governed Tech reading when it carries an FPF-governed claim or use boundary; otherwise engaging ordinary prose remains admissible. A type-correct rewrite that leaves the reader's move unrecoverable is still under-authored. | Prevents precision repair from making guidance inert. |
| **CC-SG.18 (Precision before relaxation).** | Every changed FPF-governed natural span **MUST** pass the current `F.19` connected reading before a Plain, didactic, or coarsened rendering is accepted. If a head, qualifier, relation, or admissible-use boundary remains unresolved, the author **MUST** take the exact `E.10`, `E.10.ARCH`, or subject-pattern route and keep the recovered reading available. `E.8` adds no rival sentence algorithm. | Keeps simplified prose precise without duplicating the shared language method. |
| **CC-SG.18a (Semio-Echoing auxiliary placement).** | `Semio-Echoing` or comparable material **MUST** remain auxiliary to the pattern's positive `EntityOfConcern`, first move, result, and boundary. Add it only for a grounded wording-use overread that changes the reader's action, route any unresolved claim to its exact subject pattern, and omit a generic counterreading catalogue or row-atomic conformance form. | Prevents a guard inventory from replacing constructive method guidance. |
| **CC-SG.18b (Positive subject content and precision-restoration profile control).** | A conforming pattern's first substantive `Problem frame` and `Solution` content **MUST** state its positive `EntityOfConcern`, first useful move, practical delta, and action-changing boundary. Apply `F.19` as the common precise-language pass and cite a neighboring pattern only for its concrete contribution. Ordinary PatternID use remains ordinary; architecture, review, quality, projection, and package rationale stay outside practitioner prose. | Keeps precision restoration auxiliary to the pattern's own work. |
| **CC-SG.18c (Kind-preserving wording repair).** | After words or syntax change, authors **MUST** apply `F.19`'s local reread to the changed sentence and meaning-dependent neighbours. The pattern's `EntityOfConcern`, practitioner action, first result, and boundary must remain recoverable, and every live kind, relation, use, scope, and action-changing detail must pass the shared kind/loss comparison or an accepted change decision. No per-facet form or authoring ledger is required. | Prevents wording cleanup from becoming ontology or use drift. |
| **CC-SG.19 (Use-value carry-through in material revisions).** | For a materially changed edition, authors **MUST** apply `E.8:4.1.2` once to the actual predecessor and candidate: preserve or deliberately replace useful action, result, boundary, and effort; give candidate-only use an accepted basis; keep positive guidance before optional assurance; and repair every determinate discovery cue and true direct consumer of a changed interface. Each changed natural span, including a list, **MUST** pass the connected `F.19` reading. A clean comparison requires no card, score, or row per idea or list member. | Makes source preservation and plain-language repair executable without a per-idea ledger or second enumeration algorithm. |
| **CC-SG.19a (Distinctness is not worth).** | Under `E.8:4.1.3`, an action-changing difference **MUST NOT** by itself justify retain or merge. The changed action, result, boundary, or saved reconstruction **MUST** also be warranted and useful for the declared reader, use, and scope under the applicable domain, evidence, currentness, affordability, and architecture checks. A distinct but wrong, stale, unsafe, unsupported, incompatible, or needlessly burdensome contribution is repaired, rejected, or left as an explicit gap. | Prevents a specificity test from preserving harmful novelty while keeping ordinary comparison proportionate. |
| **CC-SG.20 (Publication-token use discipline).** | Authors and publication tooling **MUST** apply H-10's seven-class inventory. A `PatternRef` **MUST** use a PatternID whose surrounding text identifies the framework and **MUST** resolve in the publication being checked to one complete addressable body; a reference selecting the body published in one edition **MUST** also name that edition. Authors **MUST** keep `PlannedCatalogEntry` mentions explicitly future-facing, preserve complete `SectionRef` and declared local or alias scope, use `<base>.*` for family selectors, and keep `NonReferenceToken` explicitly non-referential. A checker **MAY** verify and report these facts but **MUST NOT** decide pattern identity, status, or authority. | Lets people and deterministic tooling resolve the same token without treating identifier shape or current position as pattern meaning, inventing missing semantics, or hiding failed references. |
| **CC-SG.20a (Part publication boundary).** | An assembled FPF publication **MUST** satisfy H-11 for every compact ToC Part label and corresponding body Part heading, including blank table/label separation and exact ASCII-separator/title agreement; it **MUST NOT** add an empty compact table merely for a reserved body Part. | Keeps Part boundaries portable across readers and Markdown/RAG parsers without duplicating the structural Part view. |

### E.8:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur in drafts and in downstream application. They are predictable ways the Forces in this pattern get violated.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo-culting** | Headings exist, but the section is fragments, decorative bullets, or a table with no governing claim. | Satisfies Uniformity but loses Readability and Didactic Primacy. | State the governing claim and its practical consequence in ordinary prose; introduce a list or table only when that structure improves the reader's work, and apply `F.19` to its contribution and load. |
| **Un-grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell-Show-Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back-propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name-dropping** | SoTA-Echoing lists sources or adopt/adapt/reject labels but never names the practice question, serious alternative, defect overcome, or changed pattern locus. | The reader cannot recover why the selected line is best for this question or what changed in practice. | Supply the complete compact comparison from CC-SG.7, or state an honest source gap. |
| **Currentness laundering** | An official registry entry, publication date, maintained status, latest release, citation count, or widespread default is verified and then reported as evidence that the source is SoTA. | The check establishes source identity, availability, or currentness, not the best-known answer or its advantage over a serious alternative. | Classify the source as official/popular comparator or identity/currentness only. It contributes to SoTA only through an explicit comparison whose defect and pattern mutation are independently shown. |
| **Tool-bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard-Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into subject-specific project profiles. |
| **Hidden trade-offs** | A material cost or limitation is omitted from Consequences. | Hides information needed to judge adoption or applicability. | State the decision-relevant cost or limitation and a mitigation when available. Consequences may state only gains when no such cost or limitation is known. |
| **Skeleton-only pattern** | The template is present, but the pattern gives only one compressed definition block and scenario labels. | Passes form while failing didactic sufficiency. | Add didactic content: local decomposition, concrete slices, reviewer cues, and neighboring-pattern or project-side FPF kind and reference named by value guidance. |
| **PatternID read as definition or order** | A numeric or mnemonic segment is treated as the pattern's meaning, title, current position, dependency, Method relation, or semantic parent. | The address becomes a hidden claim and ordinary reordering threatens reference continuity. | Use the PatternID only as an address together with surrounding text that identifies the framework. Show title and current position separately, state relations directly, and use the applicable product-authoring rule to decide continuity across editions. |
| **Project-context leakage** | A reader needs architecture memos or planning notes to understand the pattern. | The monolith stops being self-sufficient. | Move the essential problem framing, worked slices, and rationale into the pattern itself; keep project reviews informative only. |
| **Repeated content, reference, and architecture boilerplate leakage** | The body repeats a guard, definition, reference, or placement rationale without adding a local action, case, evidence value, or recognition need. | Repetition hides the positive `Solution` and turns the pattern into an architecture note. | Cite the existing source or use the proper discovery or architecture carrier; keep one local boundary only when it changes use. |
| **Quality-carrier leakage** | The pattern body reports development, review, projection, assembly, or landing evidence as if it were practitioner guidance. | The reader sees why the text was processed rather than what to do. | Keep the evidence in its own carrier and retain only the user action or boundary that it supports. |
| **Apparatus overwrap** | Process, status, role, carrier, or quality language displaces the pattern's object and move, or a polished caveat introduces an unsupported relation. | The prose can be true and still force the reader to solve the wrong problem. | Apply the connected `F.19` reading, return the positive practitioner path, and route only a genuinely unresolved FPF value to its exact pattern. |
| **Unresolved wording kept as local style doctrine** | `E.8` locally restates generic-head, qualifier, comparison, or implicit-relation rules instead of resolving the actual sentence. | The authoring pattern grows a rival precision-restoration algorithm and encourages checklist prose. | Apply the connected `F.19` reading; use `E.10` only as a cue or route, and take an unresolved FPF kind, relation, comparison, or admissible-use question to its exact governing pattern. |
| **Package-form and neighboring-relation drift** | Package-form words are varied for style or used without their declared relation. | The reader cannot recover membership, projection, navigation, or another actual relation. | Use the matching term from `E.8:4.2.2`, state the relation, and name any cited content's concrete contribution. |
| **Intended-reader leakage** | Pattern sections start telling the reader why the pattern was isolated, what landing form is safest, or why freeze or merge is premature. | The pattern stops teaching the user and starts narrating FPF-development decisions. | Move package-development reasoning to companion notes; keep pattern sections about admissible use, costs, boundaries, the neighboring content that defines or constrains those claims, and project-side FPF kinds and references for the intended user. |
| **Editorial/development self-instruction leak** | The pattern starts saying things like `this draft should ...`, `later authoring will ...`, or `that is the opening this draft must hold`. | The text stops addressing the working reader and starts narrating the current editorial or drafting process. | Move the sentence to the authored-slice carrier or handoff, or rewrite it as one user-facing claim about the primary `EntityOfConcern`, boundary, or practical consequence. |
| **Intended-reader-clean but pragmatically foggy** | The pattern addresses the right reader, but the first reading still hides the working situation, payoff, governed object, or first move. | Correct audience alone does not make the guidance usable. | Put the recognition cue and one minimal worked case earlier, gloss necessary technical terms, and tie explanatory `SoTA-Echoing` back to the case it changes. |
| **Hybrid audience blob** | One main narrative tries to serve engineers, managers, auditors, architects, and researchers at once with no primary working reader or concern. | The text becomes globally polite but locally blurry; no reader knows which concern governs the first passage. | Make the primary working reader, concern, and viewpoint explicit and assign other audiences to secondary companion uses, other faces, or an explicit out-of-scope note. |

### E.8:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Predictable skeleton** – readers instantly know where to find the problem frame, forces, and criteria. | Limits author freedom in macro layout; mitigated by flexibility inside the Solution subsection. |
| **Cohesive voice** – S‑principles give FPF a recognisable style, aiding memorability. | Reviewers must read for style, not only semantics; checklists reduce review effort. |
| **Embedded pedagogy** – Tell-Show-Show and governing-claim flow make the spec self-teaching. | Patterns may become slightly longer; retain only material that improves comprehension or use. |

### E.8:10 - Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the required footer marker makes truncation detectable.

The ASCII ` - ` separator in H-2 keeps heading entry inexpensive: authors can type it directly on ordinary keyboards, and readers can reuse the same characters in search and plain-text tools. Typographic dash variants require an extra input or conversion step while adding no information to the boundary between an identifier and its title. Where a prose dash is useful, `--` is a keyboard-accessible option; the identifier/title separator remains ` - `.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

### E.8:11 - SoTA-Echoing *(normative; typed comparison to contemporary best-known practice)*

**Canonical definition and contract.** This is the FPF definition of `SoTA`: the best-known currently defensible answer to one named practice question. `F.1` may prepare the question-relative source cut and `E.21` may evaluate the resulting pattern, but neither redefines SoTA. A `SoTA-Echoing` section earns its place by changing the pattern's Solution, boundary, case, check, relation, evidence requirement, stop, or reopen condition. It is not a bibliography, source-currentness register, or lineage shelf.

**Source roles in plain wording.** Classify each retained source by what it can do for the question:

- a **best-known-line candidate** supplies or critically synthesizes the strongest current answer being considered;
- a **serious current rival** supplies another answer that could change the selection;
- **failure or counterexample evidence** shows where an answer breaks or does not transfer;
- an **official or popular comparator** exposes a default worth comparing but gains no rank from authority or adoption;
- **lineage only** explains history without supporting the current selection; and
- **identity/currentness only** identifies a source, edition, date, or maintenance state without supporting its truth, adequacy, or rank.

Only the best-known line, serious rivals, failure evidence, and a necessary explicit comparator belong in `SoTA-Echoing`. These are comparison roles, not publisher or institution classes. An official standard, widely used practice, or university-endorsed line can be the best-known-line candidate when its substantive answer wins the comparison, but authority, freshness, prevalence, or praise contributes nothing to that win. Lineage-only and identity/currentness-only material stays in source records, notes, or evidence carriers outside the pattern body. An official or popular default stays as comparator only when its precise defect is needed to explain the selected answer and changes a governed pattern locus.

**Positive comparison contract.** Every positive SoTA use states, in readable prose or one compact table:

1. `practiceQuestion` — the exact working question;
2. `bestKnownLine` — the selected answer, not merely its newest source;
3. `seriousAlternativeOrDefault` — the rival or default that could have changed the answer;
4. `defectOvercome` — the action-changing defect, limit, or trade-off that selection repairs;
5. `patternMutation` — the exact Solution, boundary, case, check, relation, evidence, stop, or reopen locus changed;
6. `sourceRolesAndLimits` — the exact source edition or stable locator, why it has this comparison role, and what it does not establish; source identity supports replay, not rank; and
7. `reopenCondition` — the smallest new evidence, rival, failure, or use change that would require comparison again.

Mark material moves `adopt`, `adapt`, or `reject`. Explain which defect of the incumbent, popular, or official answer is repaired and why the selected line is no worse at comparable application effort on the values that matter and better on at least one, or state the trade-off deliberately accepted. More sources, a later date, a wider deployment, institutional praise, or a longer review cannot replace that comparison.

**Honest gap and lightest sufficient evidence.** If an adequate best-known comparison cannot be established, say which rival, counterexample, or source role is missing and return that source gap. Do not fill the section with a current standard or recent paper. Use `F.1` for the smallest question-relative cut and its SoTA-specific role branch. Use `F.0.2` only when the conclusion actually needs cross-source synthesis. Use a broader `G.2` pack only when repeated refresh or a wider claim justifies that cost.

**Evidence and relation discipline.** Reuse an existing `G.2` pack's exact ClaimSheet, corpus-ledger, Bridge rows, and source roles instead of forking a second narrative. Inherit non-conflicting comparison content from an accepted `DRR` and its source materials while keeping the `DRR` as the decision and placement record. For an obtaining semantic Bridge, identify the two exact `F.17` local senses, the `F.9` relation, and a separate bounded-use claim; otherwise leave that relation unasserted. Keep numeric comparison under its applicable ComparatorSet or CG-Spec without hidden scalarization.

**Writing guidance.** Lead each row with the practice question and practical choice. Name the selected line and serious alternative, state the defect and pattern change, then give source roles, limits, and reopen condition. Complete sentences are preferred to tag lists. External terminology or tooling stays out unless the comparison itself needs it.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self-echo)

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a pattern text remain teachable while retaining a stable reusable shape? | Iba's practitioner pattern-writing line is the best-known candidate here: start from a recurring problem, forces, a usable solution, illustration, and consequences, then make the sequence readable as a whole. | A form-only template that rewards headings and compressed bullets is the serious default. | The default can be structurally complete yet unusable. **Adapt:** `E.8:4.1`, Archetypal Grounding, recognition text, and `CC-SG.2/13/17` require a first action, worked material, and readable continuity rather than heading presence alone. | Takashi Iba, *How to Write Patterns: A Practical Guide for Creating a Pattern Language on Human Actions* (PLoP 2021), supplies practitioner writing guidance, not FPF ontology or evidence that one skeleton fits every pattern. E.8's extra checks and typed boundaries are FPF-local adaptations. | Reopen if a stronger current pattern-writing comparison shows a lower-effort form that preserves the same recognition, action, grounding, and consequence value. |
| What evidence should distinguish pattern validation from a favorable review or folklore count? | Riehle, Harutyunyan, and Barcomb's 2025 handbook method is the best-known candidate for the bounded pattern-discovery and validation question because it makes claims, research methods, cases, and evidence limits explicit. | Ad hoc expert approval and the rule of three are the serious defaults. | The defaults hide what was tested and overstate a small positive history. **Adapt:** E.8 separates a canonical seed from maturity, requires worked grounding and explicit evidence use, and routes quality claims to independent `E.21` results; **reject** a universal research programme for every small pattern. | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (2025), supplies a rigorous validation branch but does not validate E.8. It is neither an admission decision nor a universal minimum case count. | Reopen if stronger current validation practice changes the evidence needed for a maturity claim or demonstrates a cheaper method with equivalent limits and replayability. |
| When does a narrower or domain-specific contribution deserve a separate pattern or framework boundary? | The best-known line for this decision combines action-changing pattern evidence with the 2022 systematic comparison of product-line scoping approaches: compare same-situation use, reusable contribution, family promise, organizational conditions, evidence, and maintenance rather than relying on a label. | Label-only specificity and a full software-product-line process are the serious alternatives. | A label can mint empty specialization, while the full process adds software-specific machinery before value is known. **Adapt:** `E.8:4.1.3` tests the same situation at comparable effort and routes a material family change to `E.4.DPF.DA`; **reject** feature ontology and action change as sufficient proof of worth. | Marchezan de Paula et al., [*Software product line scoping: A systematic literature review*](https://doi.org/10.1016/j.jss.2021.111189) (2022), is the scoping synthesis; Riehle et al. (2025) supplies actual-use pressure; Chuprina et al., [*Towards an Approach to Pattern-based Domain-Specific Requirements Engineering*](https://arxiv.org/abs/2404.17338) (2024), is bounded proof-of-concept evidence, not a universal grammar. | Reopen if current scoping or pattern-validation evidence changes the action test, the family-boundary variables, or the evidence needed for warranted retention. |

### E.8:12 - Relations
* **Coordinates with:** `E.9.DA` when an authored pattern body is drafted from a concrete `DRR` and the blocker is whether the `DRR` selected, distributed, carried source use, carried accepted decisions, or supplied a first drafting action sufficiently for that authoring use. `E.8` still governs the pattern body; `E.9.DA` is not a mandatory authoring section, review card, or substitute for writing the Solution.

* **Builds on:** E.6, E.7
* **Constrained by:** Guard‑Rails E.5.1–E.5.4 (lexical firewall, notation independence, etc.)
* **Coordinates with:** `E.21` when one authored FPF pattern version is evaluated as a scoped pattern-quality claim. `E.8` governs authoring shape, recognition text, action guidance, worked cases, SoTA grounding, and conformance material; `E.21` governs the pattern-quality evaluation, required coordinate values, `PatternQualityStatus`, and stop condition. Do not import `E.21` as a mandatory authoring section or full review card.
* **Coordinates with:** `E.23` when an authored FPF pattern body is being improved through repeated passes. `E.8` still governs the authored pattern body; `E.23` governs the repeated quality-improvement method; the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings.
* **Coordinates with:** `E.13` when an authored pattern claims practical payoff or uses a visible quality value, metric, checklist result, review result, or release posture as if it were the intended value. `E.8` keeps the payoff in user-facing prose; `E.13` repairs proxy-to-value substitution.
* **Coordinates with:** `E.4.DPF` for choosing a DPF reference code, PatternID plan, continuity across editions, and reader return after split, merge, replacement, or retirement; and `E.11.PFP` for current Part, position, public order, and citation display. `E.8` owns only the common identifier grammar and reference wording; identifier form and checker success decide none of those authoring or publication questions.
* **Coordinates with:** `E.11.PUR`, which supplies the recommended-pattern-use decision for a current concern, and `E.10.MOVE`, which disambiguates whether move-like wording names pattern-use recommendation, direct work, plan, gate, transformation, publication, source, architecture, call-planning, or language-state material. These references state concrete contributions; an exact assertion, claim-bearing episteme, or `ClaimGraph` is added only when the named receiving use depends on that identity.


* **Constrains:** All patterns; the DRR template references the same section order.

### E.8:End

