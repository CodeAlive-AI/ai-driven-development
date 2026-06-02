## E.8 - FPF Authoring Conventions & Style Guide

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless explicitly marked informative)

### E.8:0 - Use this when

Use `E.8` when you are writing, revising, or reviewing one FPF pattern and need to know what shape, voice, reader-recognition role, and assurance material the pattern must carry before it can be treated as mature FPF text.

Use it especially when a draft is technically correct but hard to use: the cold reader cannot tell when to apply it, what action to take, what mistake that action prevents, where neighbouring patterns take over, or which assurance material is informative rather than the first user-facing guidance.

**Not this pattern when.** Use `E.9` when the main work is deciding why FPF should change and how that decision is distributed across patterns. Use `E.19` when the main work is an admission or refresh review. Use the local domain pattern when the question is what FPF says inside that domain rather than how a pattern should be authored.

### E.8:0.1 - What goes wrong if missed

A pattern can satisfy a checklist and still be practically unreadable. It may open with package architecture instead of a recognisable working moment, bury its payoff, hide its neighbouring boundaries, or let assurance prose silently replace the reader-facing claim. The result is a formally neat text that authors can defend but practitioners cannot reliably use.

### E.8:0.2 - What this buys

`E.8` gives FPF authors one shared pattern shape and one shared authoring discipline: recognition text first, assurance text second, canonical sections present, terminology kept stable, SoTA used as live practice grounding rather than decoration, and practical consequences visible before a reader has to reconstruct the architecture.

**First useful move.** Put the working situation, first action-guiding move, practical payoff, ordinary boundary, and nearest heavier assurance condition into the recognition text before tightening template details or conformance material.

**Cheap stop.** If the draft already gives a cold reader the working situation, first useful move, practical payoff, ordinary boundary, and nearest heavier assurance condition, do not add more authoring apparatus just to look mature. Use conformance material to verify that guidance; do not let it replace the guidance.

**FPF-force-bearing authoring extension.** Add heavier assurance, conformance, SoTA grounding, relation material, or neighboring-pattern material only when the light recognition text would leave a live false claim, unstable governed object, hidden neighbouring-pattern boundary, unbacked practical payoff, or misleading admissible use.

When an authoring pass claims quality improvement rather than ordinary drafting, keep these roles distinct: `E.22` frames the improvement-oriented quality-read question, the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings, `C.16.Q` repairs overloaded quality and evaluative-characterization wording, `C.25` carries engineering quality-family endpoints when live, and `E.23` governs any repeated quality-improvement method. Closing checklist rows or satisfying a review profile is not by itself quality improvement.


**Maturity rule.** Section completeness is not pattern maturity. A pattern matures when its `Problem frame`, `Solution`, worked cases, boundaries, and conformance checks all point to the same usable action guidance.


**Governed object in plain terms.** The governed object is the authored FPF pattern body: its canonical sections, reader-recognition role, wording discipline, examples, rationale, anti-patterns, SoTA-Echoing, and relations.

**Primary working reader.** The first reader is an FPF author or reviewer shaping pattern prose for later practitioners and managers. The downstream practitioner is the reader the pattern must ultimately serve, so the authoring guide must model the same recognition discipline it requires.

### E.8:0.3 - Pattern Kind In Plain Terms

An FPF pattern is an action-guiding method description for a recurring working situation. It is applied by an intended FPF user who recognizes the situation, understands the problem and forces, and then uses the `Solution` to decide what to do, what to stabilize, what to avoid, and what practical change should follow.

A pattern is not a procedure, function, API, workflow engine, parameterized call, or checklist bundle. Its `Problem frame`, `Problem`, `Forces`, `Solution`, `Consequences`, worked slices, and anti-patterns carry the guidance. Its `Conformance Checklist` checks whether that guidance has been applied and authored correctly; it must not replace the `Solution` or turn the pattern into a control form.

The primary content-bearing job is constructive method guidance: the pattern must say what the user should do so the recurring error does not arise. Error prevention, auditability, and conformance checks are evidence that the guidance is usable; they are not the pattern's center.

When an action-adjacent pattern classifies wording, a name, a publication face, an explanation class, a comparison unit, or another semio-facing object, that classification is only useful if it returns to action guidance. The pattern must say what use or action is admissible now, what neighboring use or action is not admissible under the current pattern, and which exact neighboring FPF pattern governs the case when the live claim has become work, evidence, gate, decision, assurance, engineering justification, release, or reliance.
### E.8:1 - Problem frame
FPF grows through the addition of patterns written by authors from many
disciplines. Without a shared structure *and* voice, the framework would
fracture, violating Pillars **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**.

### E.8:2 - Problem
*Structural drift* and *stylistic fragmentation* threaten three qualities:

1. **Comparability** – readers cannot align patterns lacking common
   headings.
2. **Narrative cohesion** – prose swings from dry jargon to informal
   blog style.
3. **Reviewability after guidance** – missing sections hide boundary and assurance checks
   (Archetypal Grounding, Bias‑Annotation) that let reviewers verify the action guidance without replacing it.

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
The **Footer marker** (section **13**, if present) is a sentinel and is governed by **H-9** rather than the standard `<FullId> - <Title>` shape.

**Extensibility.**
Authors **MAY** add additional sections. Prefer expressing them as subsections under the nearest canonical section (e.g., `4.1`, `4.1.1` under *Solution*). If an additional pattern-level section is necessary, it **MUST NOT** delete or reorder the canonical sections and its title **MUST NOT** shadow a canonical title.

**Mandatory vs optional.**
* Canonical sections **1–13** are mandatory in every pattern.
* The escape hatch `Not applicable` is permitted **only** where explicitly stated below; when used, it **MUST** include a short justification (1 paragraph).
* **First substantive authoring seed.** The first non-empty authored body of a live pattern **SHALL** already instantiate the canonical section frame by value: title line, header block, canonical sections **1–13**, and the footer marker.
* Recognition-role openings and first-minute working guidance belong **inside** that canonical frame. Any retained pre-template entry material must also stay inside that same canonical frame rather than appearing as one pre-template opening memo. Authors **MUST NOT** seed one pre-template opening memo and postpone canonical sectioning, `Conformance Checklist`, or footer-marker installation to one separate `E.19`, assembly, or review-repair pass.

**Template:**
- **Title line:** Hashes + FullId + ` - ` + Pattern Title; optional `(informative)` note.
- **Header block:** Type, Status; optional Normativity override.
1. **Problem frame**
2. **Problem**
3. **Forces**
4. **Solution**
5. **Archetypal Grounding** (Tell-Show-Show; System and Episteme; `Not applicable` allowed only with justification)
6. **Bias‑Annotation**
7. **Conformance Checklist**
8. **Common Anti‑Patterns and How to Avoid Them** (`Not applicable` allowed only with justification)
9. **Consequences**
10. **Rationale**
11. **SoTA-Echoing** (post-2015 practice alignment; terminology drift and deltas; full comparison or reduced SoTA required whenever external or internal practice changes the Solution)
12. **Relations**
13. **Footer marker**

**Footer marker.** End each pattern with a single visible sentinel heading line by itself: `### <PatternId>:End`. This makes truncation detectable even when HTML comments are stripped or surfaced by editors. The footer marker is intentionally content‑free: **do not** place prose under it.

*Note.* Pattern boundaries are still parseable by scanning for the next pattern heading (`## …`), but an explicit `:End` marker helps retrieval pipelines (and LLM prompts) distinguish “this chunk is the whole pattern” from “this chunk was cut mid‑pattern”.

##### E.8:4.1.1 - Heading & ID discipline (human tooling + retrieval)
FPF is often consumed through full‑text search and retrieval (RAG). A reader or an LLM may see a subsection without its parent headings, so headings must be **self‑identifying**.

**H-1 (Heading shape).** Every pattern heading and every subsection heading inside a pattern **SHALL** follow:
`<hashes> <FullId> - <Title> (optional note of non‑normativity)`

*Exception.* The **Footer marker** is a sentinel heading and is governed by **H-9**, not by the standard `<FullId> - <Title>` shape.

**H-2 (Heading separator).** The canonical separator between `<FullId>` and `<Title>` is ` - ` (ASCII, space-hyphen-space).
Previously authored text may use Unicode dash variants such as ` – ` or ` — ` as separators; tooling **SHOULD** treat those variants as migration candidates, and authors **SHOULD** migrate touched headings to ` - `.

**H-3 (FullId).** `FullId` is the full hierarchical address.
For a **pattern heading** it is the pattern ID (e.g., `A.2`, `E.10.D1`).
For **headings inside a pattern**, append dot‑separated ordinal section numbers after the colon (`:`) (e.g., `A.2:4.4`, `E.10.D2:3`).
*Exception:* the Footer marker uses the reserved sentinel token `:End` as defined in **H-9**.
The colon (`:`) is **reserved** for section paths and **MUST NOT** appear in pattern IDs.

**H-4 (Ordinals).** Ordinals in section paths **SHOULD** track the canonical template numbering (**1 = Problem frame**, …, **13 = Footer marker**) to maximise cross‑pattern comparability. During refactors or in previously authored patterns, ordinals **MAY** be local. In that case, the **canonical section title at the start of `<Title>`** is the semantic key; readers and tools **MUST NOT** infer section semantics from the ordinal alone.
*Note:* the Footer marker itself is exempt from ordinal encoding; it uses the reserved token `:End` (see **H-9**).

**H-5 (Where kind and normativity live).** Pattern **kind** (e.g., Architectural / Definitional) **MUST** be declared in the **Header block**, not encoded into the heading text. Normativity (**normative** / **informative**) **MUST** also live in the Header block when it deviates from the default. If a reminder is needed for readers, authors **MAY** add a short parenthetical note at the end of the heading (e.g., `(informative)` / `(non‑normative)`), but headings **MUST NOT** use square‑bracket tags.

**H-6 (Heading levels).** Heading levels **MUST** preserve a fixed offset between structural layers (Part or Cluster (flat) → Pattern → Pattern sections):
* Part and Cluster headings **MUST** use `#` (level 1) across the file.
* A Pattern heading **MUST** use `##` (level 2).
* Inside a pattern, each nested section **MUST** add exactly one `#` per level (e.g., `## A.2 - …`, `### A.2:2 - …`, `#### A.2:2.1 - …`).

**H-7 (Ellipsis discipline).** Authors **MUST NOT** use **three consecutive full stops/dots** (`...`) as punctuation in headings or narrative prose. Authors **MUST** use the Unicode ellipsis `…` (U+2026) instead. For editorial elisions in quotations, authors **SHOULD** prefer `[…]` to make the omission explicit and distinguish it from retrieval truncation.
*Exception:* literal three‑dot sequences that are part of an external language’s syntax **MAY** appear **only inside code spans or fenced code blocks**.

**H-8 (Normative keywords).** The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119, as clarified by RFC 8174 (only when capitalised). Authors **SHOULD** avoid informal deontic phrasing (“need to”, “is required to”) in normative clauses.

**Deontics vs admissibility.** Use RFC keywords only for **deontic obligations** (requirements on authors, reviewers, implementers/tooling, or published pattern or companion texts) — i.e., things an agent can choose to do or omit. Do **not** use RFC keywords to state **definitions**, **structural invariants**, **typing rules**, or other **admissibility conditions** of the modeled world.

When you need an enforceable constraint that is *mathematical* rather than *deontic*, express it as a non‑deontic predicate using one of: `Definition:`, `Invariant:`, or `Well‑formedness constraint:` (optionally with formal quantifiers). Prefer mathematical terms like `cardinality 1..1 (total)` / `0..1 (partial)` / `0..n` over deontic adjectives like “mandatory or optional” when the intent is cardinality, not duty.

**Admissibility predicate discipline (recommended shape).**
When expressing admissibility/validity constraints as predicates (`Definition:` / `Invariant:` / `Well‑formedness constraint:`):
* Authors **MUST NOT** use RFC keywords inside the predicate block.
* Authors **SHOULD** give each predicate a stable identifier and short name (e.g., `RA‑1 (Locality)`, `RE‑3 (Method gate)`), so that Conformance Checklist items can reference it without re‑authoring the rule.
* Authors **SHOULD** write the constraint as a declarative predicate (optionally quantified), e.g., `role ∈ Roles(context)`, rather than as “X MUST …”.
* If the constraint needs to be checked as part of pattern conformance, authors **SHOULD** reference the predicate identifier from the Conformance Checklist (and/or call out validator behaviour), rather than duplicating the predicate with RFC keywords.

**H-9 (Footer marker sentinel).** Footer marker **SHALL** be a single heading line whose `FullId` is the pattern ID followed by the reserved sentinel token `:End` (no ordinals, no title, no square‑bracket tags):
`### <PatternId>:End`
It is the only allowed heading *inside* a pattern whose section token is non‑numeric. It **MUST** be the final line of the pattern and **MUST NOT** carry any prose. Tooling and readers **MUST** treat it as a boundary sentinel, not as a semantic section.

*Unification note:* historic A‑ and D‑templates differed only by the presence/absence of **Bias‑Annotation** and **Relations**; the unified template keeps the headings everywhere while allowing explicit `Not applicable` statements when justified.
The Alexandrian pattern canon historically calls *Problem frame* “Context”. FPF avoids that label because **Context** is already overloaded in FPF (e.g., `U.BoundedContext` and its Plain‑register label).

#### E.8:4.2 - Stylistic Principles (S-0 ... S-19)

| # | Principle | Guideline |
|---|-----------|-----------|
| S-0 | Narrative Flow Seven-Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven-step mnemonic. |
| S-1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S-2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S-3 | Embedded Mini-Definitions | Gloss a new term in parentheses on first appearance. |
| S-4 | Contextualisation | Brief historical or disciplinary lineage anchors. |
| S-5 | Prophylactic Clarification | Pre-empt common misreadings inside the prose. |
| S-6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S-7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S-8 | Trans-disciplinary Tie-ins | Illustrate using at least two distinct fields. |
| S-9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S-10 | Punchy Blocks | <= 5 sentences per paragraph; lists for clarity. |
| S-11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S-12 | Full sentences over tags | Avoid “keyword soup”. Each list item SHOULD contain a subject and a verb; prefer 2-4 sentence micro-paragraphs to bare tag lists. |
| S-13 | SoTA-Echo structure | In the SoTA-Echoing section, present: **claim -> practice -> source -> alignment -> adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/planes. |
| S-14 | Didactic-content sufficiency | New and substantially revised patterns carry enough didactic content to be teachable without nearby project notes. |
| S-15 | Worked slices over scenario labels | Transform-like families show at least one concrete source and resulting-publication slice; scenario names alone are not enough. |
| S-16 | Ordinary vs FPF-force-bearing realism | Keep ordinary use light, and make heavier review records explicit only for disputed, high-risk, or higher-impact cases. |
| S-17 | Self-contained monolith prose | A merged pattern must explain itself inside the monolith; planning shorthand and review-context dependencies are not admissible in live prose. |
| S-18 | Reader-role discipline | Keep live pattern prose addressed to the intended FPF user; move package-development and architecture-placement rationale to separate companion notes or clearly marked informative placement notes. |
| S-19 | Precision before relaxation | In FPF-force-bearing prose, restore the head kind named by a generic phrase before treating any qualifier as trustworthy claim guidance; then restore the claim force hidden in the qualifier before allowing any later plain, didactic, or coarsened restatement. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight. Engagement remains subordinate to semantic discipline: hooks, quotable lines, Plain restatements, and didactic images may improve recognition, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim force they carry must be recoverable through the governed Tech reading or named neighboring pattern. Ordinary Plain prose without that claim force stays ordinary prose.

**S-0 (Narrative Flow Seven-Step Heuristic) — explanation**
Narrative flow is recommended to follow these steps: **Hook -> Frame -> Weave -> Anchor -> Bridge -> Flow -> Close**.

Brief explanations:
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Open attention with a vivid but bounded image or paradox that maps back to the governed object and claim. |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Anchor** | Tie to a concrete System/Episteme or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S-1 (Density w/o Jargon), S-2 (Internal Cohesion), S-4 (Contextualisation), and S-6 (Quotable Closers).
#### E.8:4.2.1 - Recognition text and assurance text
Every canonical pattern SHALL stabilise one governed object early enough that a cold reader can tell what kind of thing the pattern is actually governing. If ordinary forms vary (`note`, `sheet`, `guided UI`, `rendering`, `review aid`), the text must make explicit which of those are merely presentation forms of one governed object and which would instead name a different act, process, work-result record, or governing companion. Recognition and assurance texts may refine that object differently, but they must not silently swap the central object kind.

If a pattern uses a broad umbrella or head together with a narrower operative branch, the text must also make the stack explicit early enough for first reading: what the broad head names, what the current narrowed branch is, what governed object is actually in play, what move is being carried by that object, and what wider work or process remains outside the pattern. A qualifier alone does not restore that stack.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `recognition shell / assurance shell` wording is retired.
These names refer to two reading-order roles carried by existing sections or projections inside one pattern; they do **not** mint new `authoritySourceRef` targets, governing-pattern relations, publication-form/face kinds, `SurfaceKind`s, or a second face family.
A third didactic-content role remains optional and is justified only when the family is especially easy to misuse, easy to over-read, or hard to teach without extra scaffolding.

The **recognition text** is the first-reading text.
It is the part of the pattern that lets a cold working reader recognise the situation quickly enough to decide whether to keep reading.
It should start from a subject-domain or practice moment before internal taxonomy whenever the pattern is meant to help real work rather than only internal canon maintenance.
In practice it usually lives in an early `Use this when` line or equivalent opening, plus the upper parts of `Problem frame`, `Problem`, `Solution`, `Consequences`, and nearby worked slices.
Its job is to make visible:
- what ordinary working situation this pattern is for;
- what goes wrong if the pattern is missed;
- what the pattern buys the reader in practice;
- when this is not the right pattern;
- what governed object is actually being kept stable;
- and, when technical terms must appear early, a pairwise plain gloss for each early FPF-force-bearing term.

The **assurance text** is the second-reading text.
It carries the heavier FPF-force-bearing material that makes the pattern reviewable and auditable:
- declaration blocks and typed fields when those are part of the pattern's declared conformance or boundary claim;
- representation ontology, described-entity discipline, or governed-object discipline;
- any minimal modeling or mathematical lens that keeps the governed object stable;
- guidance/check, invariants, admissibility, and exit or neighbouring-pattern conditions;
- `SoTA-Echoing` when it is carrying live explanatory force;
- and the review hooks that let a broader or more consequential interpretation or use be checked explicitly.

The assurance text may sharpen, justify, and discipline the recognition text.
It must **not** silently replace, strengthen, or universalize the claim that the recognition text made visible.
If the recognition text says “this pattern helps with a bounded working situation”, the assurance text must not quietly turn that into an unbacked carrier claim, unbacked guarantee, or broader universality claim.

If a pattern claims **universal** or **transdisciplinary** status, that claim must already be visible in the recognition text.
It is not enough for universality to appear only later in a guidance/check sheet, declaration block, or `SoTA-Echoing` rationale.
A broad claim should therefore be demonstrated in the recognition text through at least **three heterogeneous reader or domain situations**.
When a compact matrix helps, `F.16` is the preferred template for showing that breadth.
If `SoTA-Echoing` carries live FPF force, the practical implication of those rows should be recoverable from the recognition text and case bank rather than remaining a late-only justification layer.

A **third didactic-content role** means enough didactic and operational content that the pattern survives without nearby project documents. Typical indicators include:
- at least one concrete source and resulting-publication slice in Archetypal Grounding when the pattern governs transforms or publication change;
- at least one boundary-heavy example or anti-example when nearby patterns or other governing companion roles are easy to confuse;
- reviewer guidance that tells what to inspect first and which neighboring FPF pattern governs the failure mode and which exact project-side FPF kind and reference carries the claim or effect;
- local mini-definitions or glossary material for recurring terms that would otherwise be recovered only from project context.

Pattern density is therefore not “more metadata” and not “longer tag lists”. It is the presence of enough recognition, assurance, and, when needed, extra didactic material that a reader can understand the pattern, apply it lightly in ordinary cases, and recognise when a heavier review path is required.
#### E.8:4.2.2 - Package-form and governing-pattern relation role-word discipline

FPF pattern prose is not free-form descriptive English. When authors name a *package-form* or a *governing-pattern relation*, they must use role words with stable semantic intent.

Use the following distinctions explicitly:

This is a cross-cutting review discipline, not a replacement for local pattern lexica. For example, `A.6.7` / `A.19.CHR` already carry the suite/kit/pack distinction, and `E.17.1` already carries the viewpoint bundle/family/library distinction.
- **governing pattern** = the pattern that carries the primary guidance/check force of the family;
- **specialization** = a named refinement under an existing governing pattern;
- **overlay** = a cross-cutting governance role or reading-order projection over existing governing patterns;
- **profile** = a declarative review/use role derived from a governing pattern rather than a replacement pattern;
- **family** = a recurring class of cases governed by one pattern or governing companion;
- **bundle** = a packaged set of defaults, allowances, or coordinated members;
- **cluster** = a navigation or reading-order grouping; not by itself a governing-pattern claim;
- **suite** = a coordinated set of members with explicit suite semantics under the governing FPF pattern or named authority reference;
- **pack** = an editorial or review grouping, not automatically a semantic-authority claim;
- **kit** = a reusable coordinated publication or boundary-description package with kit-level semantics under the governing FPF pattern or named authority reference;
- **record** = a case, report, or review record;
- **umbrella** = a provisional or review-stage head spanning possible subfamilies before a final governing FPF pattern, accepted `DRR`, or pattern-body decision.

These words are not interchangeable. In particular, authors must not let `cluster`, `bundle`, `suite`, `family`, `profile`, `overlay`, or `umbrella` do the work of an unnamed governing-pattern relation. When that relation matters, it must be stated directly: `specialization under ...`, `profile governed by ...`, `overlay over ...`, `bundle under ...`, or another equally explicit formulation.

A pattern may reuse a pattern-native role word when that role is already defined by the governing pattern. Outside that case, authors must not improvise near-synonyms or shift between role words for stylistic variety.

##### E.8:4.2.2.1 - Precision-restoration placement discipline

When a pattern or companion text is drafted from `E.10` or `E.10.ARCH`, distinguish two authoring objects:

* **`ontologicalNeighborhood`** is the set of nearby governed-object kinds, relation kinds, and exact FPF patterns that can carry the recovered meaning after the wording is repaired.
* **`pattern nest`** is the publication and specialization placement of a pattern under its governing pattern family.

These are not synonyms. A precision-restoration pattern is placed in the pattern nest whose governed object it repairs, while its `ontologicalNeighborhood` may name several exact exits. For example, quality-term repair lives in the `C.16` characterization nest, even though its exits can include relation construction, action invitation, evidence, assurance, source transfer, engineering quality bundles, pattern-quality evaluation, or mathematical-lens adequacy.

Receiving patterns should use a thin pointer when the first-stage wording repair belongs elsewhere. The pointer names the exact restoration pattern and the condition that triggers it; it does not copy the trigger registry, the full `E.10.ARCH` recovery algorithm, or a second local architecture for the same repair. The receiving pattern then keeps its own subject matter: the characteristic, structure, view, episteme, relation, evidence, assurance, gate, work, decision, or adequacy question it already governs.

If a draft proposes a new precision-restoration pattern, the authoring claim must show the repeated wording failure, the recovered governed-object kind, the intended pattern nest, the exact neighboring exits, and the admissible action left after repair. A new pattern is not justified merely because a word appears often, because a local checklist wants a bucket, or because a campaign needs a tidy grouping.
#### E.8:4.2.3 - Reader-role discipline for live pattern prose

A live pattern is written for its intended FPF user: the person who will use the pattern to organise thought, inspect a case, publish a note, or review a result under that pattern.
Its FPF-force-bearing sections therefore explain what the pattern lets that user do, what it forbids, what it costs, and how it relates to neighbouring patterns in user terms. When neighbouring patterns or other governing companion roles are named, the prose should answer one user question such as `which neighboring FPF pattern applies`, `which exact project-side FPF kind and reference is live`, `which nearby pattern is easy to confuse`, or `what must stay coordinated here`; it should not read as one explanatory aside about why the package architecture was split that way.
`E.8` reader and reviewer wording is FPF pattern-authoring wording. Project-side publication readers, explanation readers, comparative review units, and participants in named project-side review relations are governed by the publication or project-side patterns that name those live objects, such as `E.17`, `E.17.ID.CR`, `E.17.EFP`, `A.10`, `A.15.4`, `A.20`, or `A.21`.

Authors must keep FPF-development or package-architecture material separate from that user-facing body.
In particular, `Problem`, `Solution`, `Consequences`, `Rationale`, worked slices, and ordinary-vs-FPF-force-bearing guidance must not do the work of:
- arguing that the material is worth isolating;
- justifying overlay/profile/governing-pattern or authority-reference choice as a package decision;
- discussing authority-reference freeze, naming freeze, merge posture, blast radius, or safest landing form;
- or narrating future package promotion or defer decisions.

If architecture-placement commentary is still helpful, the default place is a separate companion note or ADR-like architecture note.
A live pattern may include a short optional informative subsection such as `Architectural placement note (informative)` only when that placement materially helps users avoid misuse; even then, it must stay clearly separated from the user-facing solution and rationale rather than replacing them.

#### E.8:4.2.4 - Human-facing fit beyond role correctness
Human-facing fit is also subject-domain fit. A recognition text that starts from internal taxonomy, pattern-placement convenience, or package-architecture wording before the problem-domain moment is still under-authored even if its later guidance/check text is correct. When a broader umbrella name and a narrower operative branch are both live, the recognition text should also tell the reader which stack is actually active rather than leaving that reconstruction to a later declaration block or companion note.

A pattern can already be role-clean, boundary-clean, and reader-role-clean, yet still fail the first minute of use for a cold working reader.
That failure usually appears when the text is admissible but does not yet make the working situation, practical payoff, governed object, non-use boundary, or first action-guiding move visible enough.

**P-2 epistemic precision check.** When `E.10` selects epistemic precision restoration for pattern prose, the first admissible action-guiding move must survive as a remaining admissible reader move or be replaced by an exact neighboring FPF pattern application that now carries the live claim. This is a direct `E.2` `P-2` and `E.12` requirement, not an optional style preference. Intentional didactic metaphors and vivid Plain recognition lines are admissible when they are ordinary recognition aids or when their claim force maps back to Tech under `E.10:6.2`. A precision-corrected rewrite that leaves the recognition text inert is still under-authored.


For canonical patterns, the first-reading text should behave as a **recognition text** and the heavier review/check scope should remain in an **assurance text**.

When a pattern claims practice guidance or is meant to be used by engineers, managers, researchers, or other working readers, authors should make the following visible before the heavier harness takes over:
- a recognisable `Use this when` or equivalent first-minute recognition cue;
- a concrete working situation in `Problem frame`, not only taxonomic or pattern-placement language;
- a short statement of what goes wrong if the pattern is missed or misread;
- a short statement of what this pattern buys the reader in practice;
- the first admissible action-guiding move the user should take in that situation;
- a short `Not this pattern when` boundary for ordinary nearby non-use cases;
- one minimally viable worked case or use slice that shows what changes in practice;
- when a typed declaration block, formal lens, or other compact modeling material is FPF-force-bearing, a short user-facing statement of what kind of object the pattern is governing and what minimal lens keeps that object reviewable;
- pairwise plain glosses for any FPF-force-bearing technical terms that must appear before the heavier declaration role arrives;
- when `SoTA-Echoing` is carrying live explanatory force, a short working-reader implication for each row or cluster of rows and a visible link back to the case bank or worked slices that those rows discipline;
- a visible split between the recognition text and the heavier assurance text or companion material;
- and, if the draft implicitly serves several working-reader situations, an explicit primary working reader, primary concern, or primary viewpoint.

**Problem-frame recognition signature (informative).** A canonical pattern should
expose the working situation through its `Problem frame`, not through one
separate navigation block. When an `E.11` pattern-entry discoverability problem
is live, the same `Problem frame` may also carry candidate-pattern and
tempting-wrong-pattern cues; otherwise it should stay with action guidance
rather than becoming a local catalogue row.

The local recognition signature should make recoverable:

- the concrete working situation;
- the governed object or stabilized concern;
- what goes wrong if the pattern is missed or misread;
- the first admissible action-guiding move and what that move buys;
- the ordinary not-this-pattern boundary;
- the first admissible action-guiding result; when an `E.11` discoverability
  problem is live, the first admissible entry stop or entry-stabilizing result.

`Use this pattern when`, `This pattern applies when`, or equivalent `Problem
frame` prose may be used as the first sentence or compact cue of this
signature.
It is not one separate required section.
Cross-pattern comparison belongs in `J.4`; expanded case walk-through belongs in
`I.2`.

If the prose points to neighbouring patterns or other governing companion roles, it should present them as neighboring FPF patterns, exact project-side FPF kinds and references, or `E.11` entry-recognition reclassifications rather than as hidden co-authorities of the current pattern.

If the pattern claims broad, universal, or transdisciplinary usefulness, that breadth should already be visible in the recognition text.
At minimum the recognition text should show at least three heterogeneous reader or domain situations rather than one narrow case family with a later broad claim attached.
When a compact matrix helps, `F.16` is the preferred template for making that breadth legible.

This is not a request to flatten the pattern into plain language only.
It is a rule about ordering, layering, and text consistency: the recognition text must help a working reader recognise the pattern early, while the assurance text continues to carry the full claim force.
If the pattern uses technical lexicon, ontological distinctions, or a mathematical lens, those structures must remain recoverable, but the first-reading text should not require the reader to decode that full stack before recognising the working situation.
The assurance text may tighten or discipline the recognition text; it must not silently shift what the recognition text claimed.

**Illustrative migration example (informative).**

Old pre-template top:

```text
Start here when the dominant live question is API, protocol, SLA, published boundary, or compliance wording.
First output: Claim Register.
Neighboring pattern exits / entry-recognition reclassifications: A.6.B, A.6.C.
```

Repaired Problem-frame recognition signature:

```text
Use this pattern when boundary-facing language - API, protocol, SLO/SLA, compliance clause, or other published boundary description - mixes guidance/check clauses, admissibility gates, duties, and evidence into one sentence or published boundary description.

If missed, the text becomes boundary-claim soup: runtime behavior, governance, and evidence are treated as one undifferentiated promise.

Do not use this pattern merely because the text mentions an API or boundary description. If the live question is still one unstable cue, preserve it through the admissible cue-preservation line first.

First admissible action-guiding result: one `A.6.B`-governed atomic claim set or one Claim Register whose live claim/use questions are explicit enough for the governing FPF pattern or named project-side FPF kind and reference to inspect.
```

#### E.8:4.2.5 - Design-time and run-time referents stay separated in live pattern prose

Live pattern prose must keep its referent index explicit. In ordinary body sections, the default truth-makers are run-time or governed-domain objects, states, moves, boundaries, consequences, and user-facing practical effects. Standard-plane wording is still admissible when the sentence is explicitly about the standard as a normative publication, for example in marked migration navigation examples, marked informative notes, or conformance/checklist clauses.

Design-time and control-plane referents are different objects. The current draft, current body, current pass, author, reviewer, handoff, packet, governing companion, landing choice, or other writing-process/control objects must not be smuggled in as the hidden truth-condition of live pattern prose. A quick test is: what makes this sentence true? If the sentence is true because the current text is arranged a certain way, because the author or reviewer must do something next, or because the current control state says so, then it is design-time residue, not live pattern content.

Move that material to the authored-slice carrier, handoff, `DRR`, or companion architecture note. If a sentence is kept in the live pattern, rewrite it so that its truth depends on the governed run-time/domain object or on the standard's declared normative claim set rather than on the current writing pass.

If a pattern or example claims **autonomy** for any Role/Method/Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id (PolicyIdRef)`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role/Method/Work). Avoid “validity”, “process”, “actor”, “system”, “mechanism” unless mapped to kernel types.

### E.8:5 - Archetypal Grounding (System / Episteme)

| Template element | `U.System` illustration | `U.Episteme` illustration |
|------------------|------------------------|---------------------------|
| Section order | Pump‑assembly pattern follows sections **1–12** (and, optionally, **13**). | Meta‑analysis pattern follows the same sections. |
| S‑1 Density w/o Jargon | “The pump boundary is the sealing plane.” | “This episteme raises **F (Formality)** by making falsifiers testable.” |
| Hook‑Weave‑Anchor | Opens with field anecdote → weaves in Γ‑core → anchors to motor torque. | Opens with historical paradox → weaves in **A.10** anchors → anchors to peer‑review data. |

*Note:* Prefer examples that reuse FPF characteristics vocabulary (e.g., **F (Formality)** rather than “F‑score”) unless you explicitly mean an external metric and name it as such.

### E.8:6 - Bias‑Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for the authoring conventions in this pattern.
This guidance biases toward **Did** (readability, narrative flow) and **Arch** (template regularity) by design; the mitigation is explicit optionality (`Not applicable`) and the requirement to justify omissions in‑text.

### E.8:7 - Conformance Checklist

**CC style (canonical).**
Conformance Checklist items are authoring checks: they test whether the pattern guidance has been applied and written correctly in a pattern or companion text that claims conformance. They do not replace `Solution`, do not make the pattern a control form, and do not state deontic obligations about the modeled world. A CC clause of the form “X SHALL ...” is to be read as “In a conforming pattern or companion text, X SHALL ...”.

**Preferred wording for new or edited CC items:** start with an explicit conformance subject (e.g., “Authors ...”, “Reviewers ...”, “A conforming implementation ...”, “A validator ...”). If a CC item is enforcing an admissibility predicate, it **SHOULD** cite the predicate’s identifier (from a `Definition:` / `Invariant:` / `Well-formedness constraint:` block) rather than restating the predicate as “X MUST ...”. For boundary/interface/protocol/declaration patterns, prefer A.6.B-governed claim IDs (L/A/D/E) or cite an existing Claim Register (A.6.B:7) instead of restating mixed prose.

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC-SG.0 (Heading discipline).** | Pattern and subsection headings **SHALL** follow **H-1 ... H-9** (FullId prefix, reserved punctuation, heading levels, ellipsis discipline). The Footer marker **SHALL** follow **H-9**. | Makes chunks self-contained; reduces ambiguity between author elision and retrieval truncation. |
| **CC-SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Title block -> ... -> Footer marker). | Guarantees structural comparability. |
| **CC-SG.1a (Initial live draft shape).** | The first non-empty authored version of a live pattern **SHALL** already use the canonical section frame (Title block -> Footer marker). Authors **MUST NOT** start from one pre-template opening memo and promise to backfill canonical sections later. | Prevents large late-stage structural rewrites and keeps drafting aligned with `E.8` from the first substantive pass. |
| **CC-SG.2 (Grounding required).** | Every pattern **MUST** include an *Archetypal Grounding* section. If **System** or **Episteme** grounding is inapplicable, authors **MUST** state `Not applicable` and give a one-paragraph justification. | Keeps patterns teachable and reduces “definition-only” ambiguity. |
| **CC-SG.3** | The *Bias-Annotation* section **SHALL** cite the five Principle-Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross-disciplinary neutrality explicit (ties to Guard-Rail 4). |
| **CC-SG.4** | Deontic normative sentences **MUST** use only RFC-style keywords (see **H-8**); RFC keywords **MUST NOT** appear inside `Definition:`/`Invariant:`/`Well-formedness constraint:` blocks. When enforceable, admissibility/validity predicates **SHOULD** be referenced by id from the Conformance Checklist (rather than duplicated as “X MUST ...”). Informal deontic verbs are prohibited in normative clauses. | Prevents ambiguity between obligation language and model validity; improves auditability. |
| **CC-SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S-0 ... S-19**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC-SG.6 (SoTA-Echo required).** | Every pattern **SHALL** include a **SoTA-Echoing** section and clearly state divergence of its Solution from SoTA with explanation of why. Architectural patterns **SHALL** satisfy the full authoring requirements below. Definitional patterns **SHALL** carry reduced SoTA when a full comparison is not meaningful: name which current practice is adopted, adapted, or rejected for terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. Internal coherence alone is not enough. | Ensures explicit lineage, guards against vocabulary drift, and prevents definitional patterns from using internal coherence as zero SoTA. |
| **CC-SG.7 (Post-2015, multi-Tradition).** | For Architectural patterns, SoTA-Echoing **SHALL** cite >= 3 post-2015 sources across >= 2 Traditions; each item **MUST** carry adoption status (adopt/adapt/reject) with reason. | Guards against monoculture; makes intent explicit. |
| **CC-SG.8 (Bridge & CL on reuse).** | Any cross-Context or plane reuse mentioned in SoTA-Echoing **MUST** cite **Bridge id + CL** and (if planes differ) **Φ(CL)**/**Φ_plane** policy-ids; penalties **-> R_eff** only. | Safe, auditable reuse. |
| **CC-SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA-Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC-SG.10 (No keyword soup).** | SoTA-Echoing items **MUST** be written as sentences (not bare noun phrases); bullet lists are acceptable only with complete clauses. | Improves didactic quality and comparability. |
| **CC-SG.11 (Anti-patterns).** | Every pattern **SHALL** include a **Common Anti-Patterns and How to Avoid Them** section. It **MAY** be `Not applicable` only with a one-paragraph justification. | Makes misuse paths explicit and reduces review churn. |
| **CC-SG.12 (Boundary claim-set discipline).** | If a pattern’s subject is a boundary, interface, API, protocol, connector, SLA, or other published boundary description, it **MUST** either (a) provide an **A.6.B**-governed atomic claim set (`L-*`/`A-*`/`D-*`/`E-*`, with stable IDs), or (b) explicitly cite an existing **A.6.B Claim Register** / governed claim set that it reuses. | Pulls A.6.B into the authoring contour, prevents boundary-kind soup, and makes review more explicit and repeatable. |
| **CC-SG.13 (Didactic sufficiency).** | New patterns and substantial revisions **MUST** remain understandable without project-planning notes. When a pattern introduces a new named family, profile, or specialization, or adds a non-trivial governing-pattern-derived note, its Solution and Grounding **SHALL** carry enough didactic content: explicit governing-pattern relation, ordinary-vs-FPF-force-bearing guidance, at least one concrete source and resulting-publication slice where applicable, and visible neighboring-pattern or exact project-side FPF kind and reference cues. | Prevents skeleton-only patterns and project-context leakage. |
| **CC-SG.14 (Controlled prose, not free shorthand).** | FPF-force-bearing prose **SHALL NOT** rely on bare relation words or planning shorthand whose governing-pattern relation is left implicit (e.g., bare “species”, “branch”, “flow”, or API-like “input/output” language). When a governing-pattern relation matters, authors **MUST** name it explicitly (`specialization under ...`, `profile governed by ...`, `overlay over ...`, etc.). | Keeps pattern prose precise and self-identifying. |
| **CC-SG.15 (Package-form and governing-pattern relation role-word discipline).** | When a pattern names a package-form or the governing-pattern relation of a family (`primary carrier`, `specialization`, `profile`, `overlay`, `family`, `bundle`, `cluster`, `suite`, `pack`, `kit`, `record`, `umbrella`), the chosen role word **MUST** match the intended ontology and **MUST NOT** be swapped for stylistic variety or left to implication. | Prevents semantic blur in pattern prose and keeps governing-pattern relations auditable. |
| **CC-SG.16 (Reader-role discipline).** | Authors **MUST** keep live pattern sections user-facing. FPF-development or package-architecture reasoning about isolation, overlay or carrier choice, freeze, merge posture, or planned evolution **MUST NOT** occupy `Problem`, `Solution`, `Consequences`, `Rationale`, or worked slices; if such placement reasoning is still needed, it **MUST** live in a separate companion note or a clearly marked informative placement note. | Keeps pattern prose aligned with its intended reader and prevents package-governance leakage into live use guidance. |
| **CC-SG.16a (Referent-index discipline in live prose).** | Live pattern sections **MUST** keep run-time/domain referents, standard-plane referents, and design-time/control-plane referents distinct. In ordinary live prose, sentence truth **MUST** depend on the governed run-time/domain object or on the pattern's declared normative claim set, not on the current draft state, author action, reviewer action, or control-plane posture. If a sentence is true only because of the current writing/review pass or text arrangement, it is design-time residue and belongs in carriers or companion notes, not in the live pattern body. | Prevents Conway/process leakage and reduces late cleanup before review or landing. |
| **CC-SG.17 (Recognition text and assurance text).** | Admission or substantial revision runs **MUST** check that a canonical pattern exposes a recognition text early enough for the intended working reader and an assurance text that carries declaration, guidance/check, modeling, and review/check scope without silently shifting the recognition-text claim. The recognition text **MUST** expose a recognisable working situation, what goes wrong if the pattern is missed, what the pattern buys, and a clear ordinary `not this pattern when` boundary. Any FPF-force-bearing typed declaration or modeling lens **MUST** be exposed by a short user-facing statement of the governed object, early FPF-force-bearing technical terms **MUST** receive nearby pairwise plain glosses, and any `SoTA-Echoing` used as live explanatory grounding **MUST** state a short practitioner or manager implication plus visible linkage to the worked cases or boundary slices it disciplines. If the pattern claims universal or transdisciplinary reach, the recognition text **MUST** demonstrate that claim through at least three heterogeneous reader or domain situations, preferably using an `F.16`-style example matrix or an equally explicit alternative. | Prevents text-clean but reader-opaque patterns and keeps broad claims visible where cold readers actually enter the text. |
| **CC-SG.17a (Problem-frame recognition signature and E.11 boundary).** | Authors **SHOULD** express a pattern's concrete working situation through the pattern's `Problem frame`, not through a separate navigation block. The `Problem frame` should make recoverable the governed object or stabilized concern, what goes wrong if the pattern is missed or misread, the ordinary not-this-pattern boundary, the first admissible action-guiding move, and the result that move buys. Only when an `E.11` pattern-entry discoverability problem is live should the same recognition text add candidate-pattern, tempting-wrong-pattern, entry-recognition reclassification, or first admissible entry-stop cues. Cross-pattern comparison belongs in `J.4`; expanded case walk-through belongs in `I.2`; lexical-query material belongs under the lexical/naming patterns and companion patterns that already govern it. Pattern-local `Start here when`, `First output`, neighboring-pattern lists, and `Common wrong escalations and boundary transfers` blocks **SHOULD NOT** replace the action-guiding `Problem frame` and `Solution`. | Keeps working-use recognition inside the canonical pattern frame while preventing navigation/workflow language from becoming local pattern structure. |
| **CC-SG.17b (Epistemic precision repair preserves action guidance).** | When authors edit pattern prose under `C.2.P`, the repaired recognition text **MUST** preserve or restore the first admissible action-guiding move as a remaining admissible reader move, or explicitly name the neighboring FPF pattern that now carries the live claim. When both Tech and Plain registers are live, any Plain or didactic wording **MUST** map back to the recovered Tech reading under `E.10:6.2` when it carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim force. More engaging recognition wording remains admissible as ordinary Plain prose only when it does not carry such claim force, or as a recognition aid whose claim force is recoverable through the recovered Tech reading or named exact FPF pattern application. Type-correct but inert wording is not mature pattern prose. | Prevents epistemic precision cleanup from leaving pattern guidance inert while also preventing expressive prose from reintroducing overread. |

| **CC-SG.18 (Precision before relaxation).** | In FPF-force-bearing prose, authors **MUST NOT** leave a generic head noun or FPF-force-bearing qualifier uninterpreted when that phrase carries semantic, boundary, or authority claim force. A narrowing qualifier by itself does **not** restore the head kind. Authors **MUST** restore head kind first, then qualifier claim force, then any comparison criterion or escalation condition before downstream claim or effect. If a later Plain, didactic, or coarsened rendering is kept, the more precise upstream reading **MUST** remain recoverable. | Prevents ambiguity from being hidden inside ordinary-looking phrases and keeps softened prose subordinate to an explicit authoritative reading. |

### E.8:8 - Common Anti-Patterns and How to Avoid Them

These failure modes recur in drafts and in downstream application. They are predictable ways the Forces in this pattern get violated.

| Anti-pattern | Symptom | Why it fails (force violated) | How to avoid / repair |
|-------------|---------|------------------------------|-----------------------|
| **Template cargo-culting** | Headings exist, but each section is a thin bullet list with no narrative. | Satisfies Uniformity but loses Readability and Didactic Primacy. | Use S-0 narrative flow per section; write 2-4 sentence micro-paragraphs before any list/table. |
| **Un-grounded abstractions** | Problem/Solution stay abstract; no concrete System/Episteme Tell-Show-Show. | Breaks teachability and makes misuse likely. | Fill Archetypal Grounding first; then back-propagate concrete nouns into Problem/Forces/Solution. |
| **SoTA name-dropping** | SoTA-Echoing is a list of nouns/buzzwords with no adopt/adapt/reject rationale. | Violates CC-SG.7 and CC-SG.10; readers cannot audit alignment. | For each source, state what is adopted/adapted/rejected and why (complete clauses, 2-4 sentences). |
| **Tool-bound normativity** | A vendor tool, file format, or schema is described as required to apply the pattern. Data governance implied. | Violates Guard-Rails (lexical firewall; notation independence, data governance absence); reduces portability and conceptual clarity. | Keep normative content conceptual; move tooling and data governance into Context-local Profiles. |
| **Hidden trade-offs** | Solution sounds universally good; Consequences lists only benefits. | Removes decision-use value; applicability cannot be judged. | In Consequences, include at least one trade-off and a mitigation; if none exists, explain why. |
| **Skeleton-only pattern** | The template is present, but the pattern gives only one compressed definition block and scenario labels. | Passes form while failing didactic sufficiency. | Add didactic content: local decomposition, concrete slices, reviewer cues, and neighboring-pattern or exact project-side FPF kind and reference guidance. |
| **Project-context leakage** | A reader needs architecture memos or planning notes to understand the pattern. | The monolith stops being self-sufficient. | Move the essential problem framing, worked slices, and rationale into the pattern itself; keep project reviews informative only. |
| **Generic-head underspecification** | An FPF-force-bearing phrase uses a generic head such as `note`, `view`, `guidance`, `output`, or `artifact`, but the text never restores what kind of thing that phrase names. | The reader cannot tell what ontology the sentence is actually governing. | Restore the head kind first in pattern-local or project-local terms before any broader claim or effect or comparison is made. |
| **Qualifier-smuggled claim force** | A modifier such as `comparative`, `safe`, `interactive`, `reliable`, or `faithful` is doing the semantic work while the text leaves its claim force implicit. | The sentence sounds precise without actually stating its comparison criterion, relation claim force, or downstream claim or effect boundary. | Unpack the qualifier into explicit claim force, criteria, named neighboring FPF pattern, or project-side FPF kind and reference rather than relying on the modifier alone. |
| **Mixed comparison criterion** | One sentence compares or ranks publication-form, carrier, process, authority-reference, or project-record values under one declared criterion. | The sentence becomes ontologically incoherent when the compared objects do not share the criterion, even if each local noun sounds plausible. | First restore head kind, then qualifier claim force, then rewrite the comparison through a homogeneous claim-force criterion, threshold, or named receiving-pattern relation condition. |
| **Implicit relation shorthand** | Words like “species”, “branch”, or process metaphors do the semantic work without naming the actual governing-pattern relation. | Readers infer the wrong ontology or workflow. | State the governing-pattern relation explicitly and remove shorthand that only makes sense inside project discussions. |
| **Package-form and governing-pattern relation drift** | Words like `bundle`, `cluster`, `profile`, `overlay`, `family`, `suite`, or `kit` are swapped as if they were stylistic variants. | Readers cannot tell whether the text is naming an `authoritySourceRef` target, a navigation grouping, a review role, or a packaged set of defaults. | Pick one role word by ontology, keep the governing-pattern relation explicit, and do not vary the noun unless the ontology really changes. |
| **Reader-role leakage** | Live sections start telling the reader why the pattern was isolated, what landing form is safest, or why freeze/merge is premature. | The pattern stops teaching the user and starts narrating FPF-development decisions. | Move package-development reasoning to companion notes; keep live sections about admissible use, costs, boundaries, and exact neighboring FPF patterns or project-side FPF kinds and references for the intended user. |
| **Editorial/process-plane self-instruction leak** | The live pattern starts saying things like `this draft should ...`, `later authoring will ...`, or `that is the opening this draft must hold`. | The text stops addressing the working reader and starts narrating the current editorial or drafting process. | Move the sentence to the authored-slice carrier or handoff, or rewrite it as one user-facing claim about the governed object, boundary, or practical consequence. |
| **Role-clean but pragmatically foggy** | The pattern addresses the right reader in principle, but a cold practitioner still cannot recognise the working situation, practical payoff, governed object, first useful move, or project-level implication of the `SoTA-Echoing` early enough. | The text passes role hygiene but still fails `E.12`/`E.13`/`E.14` as working guidance. | Bring a manager-first or practitioner-first recognition cue higher, add one minimally viable worked case, state what changes in practice, expose the governed object and any minimal modeling lens in plain user-facing prose, add plain glosses for early FPF-force-bearing terms, and keep `SoTA-Echoing` tied to visible practitioner or manager implications plus nearby case linkage rather than lineage alone. |
| **Hybrid audience blob** | One main narrative tries to serve engineers, managers, auditors, architects, and researchers at once with no primary working reader or concern role. | The text becomes globally polite but locally blurry; no reader knows which concern governs the first role. | Make the primary working reader, concern, and viewpoint explicit and assign other audiences to secondary companion roles, other faces, or an explicit out-of-scope note. |

### E.8:9 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Predictable skeleton** – readers instantly know where to find context, forces, and criteria. | Limits author freedom in macro layout; mitigated by flexibility inside the Solution subsection. |
| **Cohesive voice** – S‑principles give FPF a recognisable style, aiding memorability. | Reviewers must read for style, not only semantics; checklists reduce review effort. |
| **Embedded pedagogy** – Tell‑Show‑Show and Hook → Close heuristics turn the spec into a self‑teaching text. | Slightly longer patterns; justified by better comprehension and fewer clarifying DRRs. |

### E.8:10 - Rationale
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

A unified template also improves retrieval: a chunk containing `A.2:<n> - Bias‑Annotation` remains self‑identifying even when parent headings are missing, and the recommended footer marker makes truncation detectable.

International and industry standards often speak in terms of *conformance criteria*. FPF uses the label **Conformance Checklist** to make adoption easier for engineers and managers.

### E.8:11 - SoTA-Echoing  *(normative; lineage and deltas to contemporary State-of-the-Art)*

**Purpose.** Make each pattern's relationship to contemporary best-known problem-solving practice explicit and comparable without importing tooling or data governance. This section is prose-first and notation-independent. It does not mint an independent second rule source, but it is an FPF-force-bearing alignment section: the Solution, Conformance Checklist, Relations, worked cases, and other FPF-force-bearing sections must reflect the stance stated here or explicitly justify divergence.

**SoTA definition.** In FPF, `SoTA` names the best-known currently defensible problem-solving practice for the governed problem in the relevant domain or practice tradition. It is not official status, a recent edition, broad popularity, citation volume, institutional adoption, reputation, or familiar terminology. A standard, book, paper, benchmark, or practice report carries SoTA only when it states or justifies the current best-known answer for the governed problem; otherwise it is lineage, current-standard reference, rationale-only material, or rejected-popular-practice material.

**Two-part SoTA test.** A row must pass both tests. First, the source family must be SoTA-bearing: it must represent the current best-known answer for the governed problem or a clearly named current branch of that answer. Second, the pattern must incorporate that answer by value: the adopted, adapted, or rejected stance must change `Solution`, boundary, anti-pattern, rationale, checklist, relation, worked case, evidence requirement, stop/reopen condition, or another FPF-force-bearing pattern locus. A current best-known source that changes no FPF locus is uncaptured SoTA; a citation that changes wording without being current best-known practice is not SoTA.

**Incorporation test.** A SoTA row is accepted as live pattern grounding only when it changes what the pattern lets a working user do, what the pattern forbids them to over-read, which neighbouring FPF pattern must apply, which evidence or validation requirement remains live, or how the Solution and neighbouring FPF-force-bearing sections are written. A citation that only decorates the pattern or proves that the author has read a tradition does not carry E.8.

**Minimum contents (authoring requirements).**
1) **Evidence binding (no duplicate SoTA).** If a **SoTA Synthesis Pack** exists (G.2), this section **SHALL cite** its **ClaimSheet IDs, CorpusLedger entries, and BridgeMatrix rows** as the governing evidence source for claims and report `adopt`, `adapt`, or `reject` **consistent with those IDs**. Avoid forking an untracked SoTA narrative.
1a) **Accepted decision and source material set, not DRR-only narrowing.** When a pattern is drafted under an accepted `DRR` and other accepted decision or source materials also exist by value, the `DRR` remains the decision and placement anchor, but `SoTA-Echoing`, neighboring-pattern relations, and any minimal modeling or mathematical lens **MAY** and **SHOULD** inherit non-conflicting material from that accepted material set.
2) **Sources (current problem-solving anchors, not prestige anchors).** For **Architectural patterns**, cite at least 3 primary SoTA anchors that carry current best-known answers for the governed problem, with at least **two independent Traditions** when more than one serious tradition is live. For **Definitional patterns**, cite at least 1 current source or practice anchor for the reduced issue being governed: terminology work, ambiguity or sense recovery, separation between constraint and ontology, controlled-vocabulary caution, or a comparable definitional problem. If the best source is older but still current, mark why it still answers the governed problem rather than treating source age, standard status, or popularity as SoTA by itself.
3) **Best-known, not merely popular.** Authors **SHALL** distinguish best-known currently defensible practice from merely widespread or fashionable defaults. If the pattern adopts, adapts, or rejects a popular but less defensible practice, that divergence **MUST** be stated explicitly.
3a) **Currentness and lineage status.** Older standards, early papers, and historically important examples may be cited as lineage only when later practice has materially changed the answer. They may carry a live SoTA row only when the pattern states why the anchor is still current for the governed problem or pairs it with a current source that supplies the live practice.
3b) **Problem-domain and practice answerability.** The selected SoTA source family **MUST** answer the governed working problem and the relevant domain or practice tradition. It **MUST NOT** be selected only because it makes package placement, naming neatness, or pattern clustering easier to justify.
4) **Practice alignment.** For each cited item, state **what is adopted, adapted, or rejected** and **why** in 2 to 4 sentences.
5) **Scale admissibility.** If numeric operations are implied, bind to ComparatorSet or CG-Spec and declare partial-order stance with no hidden scalarization.
6) **Cross-Context reuse.** Any reuse across `U.BoundedContext` must expose Bridge id plus CL and, if planes differ, Phi policy ids; penalties affect only `R_eff`.
7) **Lexical hygiene.** Avoid “mapping” unless you mean an explicit Bridge, translation relation, or other named relation with loss notes.

**Writing guidance (readability).**
*Write short paragraphs, not tag lists.* For each Tradition, provide one sentence naming the practice, one sentence comparing it to the pattern's Solution, and one sentence giving adoption status with reason. Where helpful, add one **System** and one **Episteme** micro-example (Tell-Show-Show).

**Format: human-first.** A small table is allowed, but each row **MUST** be accompanied by 1 to 2 sentences as above. Vendor tokens, tool tokens, file formats, or data schemas are out of scope unless the governed problem itself makes them carry FPF force.

#### E.8:11.1 - SoTA alignment for this pattern (E.8 self-echo)

| Claim (E.8 need) | SoTA practice (post-2015) | Source posture | Primary source (post-2015) | Alignment with E.8 | Adoption status |
|---|---|---|---|---|---|
| Pattern texts must be teachable, not just correct. | Use a stable skeleton with context, problem, forces, solution, actions, and consequences, plus illustration and checks, to keep patterns readable and actionable. | **Current practice and writing-guidance support.** This row supports E.8's canonical pattern skeleton and didactic ordering; it is not treated as external authority over FPF ontology. | Iba (2021), “How to Write Patterns: A Practical Guide for Creating a Pattern Language on Human Actions” (PLoP 2021 PLoPourri). | Canonical Template mirrors the skeleton and adds Archetypal Grounding plus Conformance Checklist as first-class sections. | **Adopt and adapt.** Adopt the skeleton; adapt by making bias and conformance explicit sections. |
| Pattern quality needs explicit validation beyond folklore. | Critique of ad hoc validation, including the rule of three, and push toward more rigorous discovery and validation methods. | **Current-best support for pattern discovery and validation rigor in this row's narrow use.** The source changes E.8 by requiring validation to be explicit rather than folklore-based. | Riehle, Harutyunyan, Barcomb (2020), “Pattern Discovery and Validation Using Scientific Research Methods”. | E.8 encodes validation as Conformance Checklist plus SoTA-Echoing with adoption status and evidence binding. | **Adopt.** Adopt auditability goals; keep the mechanism lightweight through checks and evidence binding. |
| Governance should constrain structure, not mandate tools. | Specify conformance and structure; do not prescribe processes, notations, tools, or recording media. | **Current-standard/reference support.** The architecture-description standard supplies a useful conformance-vs-tooling distinction, but E.8 does not import architecture-description ontology as pattern-authoring ontology. | ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise - Architecture description*. | E.8 is template-centric and conformance-centric, with guardrails against tool and notation lock-in in core narrative. | **Adopt.** Directly adopt the conformance-not-tooling discipline for authoring shape. |
| Pattern languages are networks; visuals often mislead. | Systematic surveys report low consensus on what to visualise and ambiguous or inexpressive visuals; relations need clear definition in text. | **Current practice and rationale support.** The source supports the text-first relation discipline; it is not current-best support for all pattern-language visualization. | Quirino, Barcellos, Falbo (2018), “Visual Notations for Software Pattern Languages: A Mapping Study”. | E.8 requires a Relations section and keeps diagrams optional, placing primacy on textual structure and explicit links. | **Adapt.** Use the finding as rationale for text-first, relation-explicit authoring. |

### E.8:12 - Relations
* **Coordinates with:** `E.9.DA` when an authored pattern body is drafted from a concrete `DRR` and the live blocker is whether the `DRR` selected, distributed, carried source use, carried accepted decisions, or supplied a first drafting move sufficiently for that authoring use. `E.8` still governs the pattern body; `E.9.DA` is not a mandatory authoring section, review card, or substitute for writing the Solution.

* **Builds on:** E.6, E.7
* **Constrained by:** Guard‑Rails E.5.1–E.5.4 (lexical firewall, notation independence, etc.)
* **Coordinates with:** `E.21` when one authored FPF pattern version is read as a scoped pattern-quality claim. `E.8` governs authoring shape, recognition text, action guidance, worked cases, SoTA grounding, and conformance material; `E.21` governs the quality read, active characteristics, `PatternQualityStatus`, and stop condition. Do not import `E.21` as a mandatory authoring section or full review card.
* **Coordinates with:** `E.23` when an authored FPF pattern body is being improved through repeated passes. `E.8` still governs the authored pattern body; `E.23` governs the repeated quality-improvement method; the object-under-improvement evaluation such as `E.21` or `E.9.DA` supplies value meanings and stop meanings.

* **Constrains:** All patterns; the DRR template references the same section order.
### E.8:End

