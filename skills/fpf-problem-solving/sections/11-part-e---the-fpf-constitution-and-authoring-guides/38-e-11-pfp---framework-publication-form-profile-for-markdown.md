## E.11.PFP - Framework Publication Form Profile for Markdown

> **Type:** Specialization of E.11
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.11.PFP:1 - Problem frame

Use this pattern when one FPF, DPF, or LPF edition needs a public Markdown form that a cold reader can enter and a small deterministic checker can recognize. The framework's pattern set, product boundary, and edition values must already be selected for the publication being assembled or checked.

The first useful result is a publication arrangement in which readers can find both the whole-framework explanation and each directly useful pattern. Name the edition source and public units; locate the twelve substantive answers under section 4.7 and each missing, reordered, duplicated, unresolved, or mismatched form element. A passing form check does not accept the edition, prove framework adequacy, identify a carrier, or establish a publication occurrence.

Do not use this pattern to decide whether one pattern set is a framework, whether a catalogue or guide is another product, or whether an edition is current or available. Use the E.4 family for the product and framework boundary, E.24.PUB for publication occurrence and carrier relations, and the applicable decision, quality, and currentness patterns for those claims.

### E.11.PFP:2 - Problem

FPF-family publications can expose the same useful material through different headings, edition labels, index layouts, and Readme cards. A familiar reader can compensate. A cold reader or parser cannot reliably tell which edition is present, which index is authoritative, whether several Part tables form one index, or whether a support table is a rival front door.

Even a navigable collection can leave readers unable to explain what its Methods accomplish together, why they are arranged that way, which assumptions and sources support several patterns, or how a narrower profile changes use. Those answers can be scattered through development notes and disappear when the pattern bodies are published.

A rigid carrier template can put authorship, credits, dates, status, dependencies, build details, and maintainer records ahead of the reader's question whether or not those facts change the reader's choice. It can also force a catalogue, inquiry programme, guide, or other adjacent product to pretend that it is a framework edition. The common form must be exact where shared recognition matters, put the practitioner's question first, and explicitly limit its scope to framework editions.

### E.11.PFP:3 - Forces

| Force | Tension |
| --- | --- |
| Cold-reader entry | Stable labels and order reduce search cost, but edition administration must not displace practical entry or the pattern bodies. |
| Exact edition return | Readers need a stable public designation and locator, while dates, filenames, statuses, and build digests must not become edition identity. |
| One logical index | FPF-family editions need one authoritative pattern index, while visible Part or placement groups remain useful. |
| Product variation | FPF, DPF, and LPF editions share a front form, but their body, reference tail, and choice-relevant public cues differ. |
| Whole and direct use | Readers need the language's shared problem, organization, reasons, and limits, while a direct question may be answered by one pattern. |
| Product boundary | Support units may belong to one framework product; independently useful adjacent products need a truthful boundary and public return. |
| Deterministic checking | Syntax checks should be reproducible, but they must not infer table purpose, product truth, or reader value from prose. |
| Form and carrier separation | Expressions following one reusable form may be borne by several carriers, and one outer carrier may expose several products, without merging their identities. |
| Accessibility and translation | Predictable headings and navigation aid many readers and tools, while one English label set cannot silently stand in for every language or access need. |

### E.11.PFP:4 - Solution

Apply common reader-facing publication-form rules to construct or inspect a particular expression of one FPF, DPF, or LPF edition. This profile states requirements for the selected reusable rules and their realization in the expression. Keep the expression, its reusable form, the independently identified presentation carrier whose actual state yields it, the expressed edition, and the publication occurrence distinct under E.24.PUB.

#### E.11.PFP:4.1 - Preserve the compact product opening

For an all-in-one Markdown publication, preserve the product-declared compact opening and use this H1 route:

1. `# <product-declared publication title>`;
2. `# Table of Contents`;
3. the exact product-declared Readme H1;
4. the exact product-declared Architectural Reference H1;
5. the pattern bodies or pattern collection in the order selected by that edition; and
6. reference and maintenance material under headings declared by the product pattern.

The title and Readme H1 are separate product declarations. A checker receives both exact strings; it does not derive the Readme H1 by concatenating `Readme` to a longer carrier title.

The common profile does not insert a metadata block, edition record, warning, or other lines into a compact predecessor opening merely to make products look alike. A product-specific builder may pin a compact front shape, including the line at which the ToC begins, when that shape protects an established reader entry.

Between the title and ToC, retain only the shortest public cues already justified by product use. An exact edition designation or locator belongs there only when its possible values change the reader's next use, reliance, return, language, dependency, or access choice.

When such a cue is present, project it from one product-owned edition or relation record; do not maintain a second editable copy. Add authorship, credit, date, dependency, language, access, or a product-declared maintenance status, support window, or currentness window only under the same next-working-move test.

A date is a cue, not edition identity, and a visible status or window is not evidence of acceptance, currentness, maintenance, availability, access, or authorization.

When readers copy, adapt, translate or redistribute a framework publication, its copyright-license notice tells them what permission the rights holder grants. Identify the covered material, rights holder and chosen license, and make the license text reachable from a standalone copy. Project a compact notice from the product's chosen licensing terms; retain applicable attribution and mark any third-party or differently licensed material.

The author of an independently created DPF or LPF chooses its license. Where copyright permission is needed, reuse of another framework's protected expression is governed by that material's terms; applicable copyright exceptions remain available. Adopting its methods or publication form does not impose that framework's license on the new work.

Reader front matter extends from the opening title through the Readme and architectural reference up to the first pattern-body collection H1. It must not contain campaign keys; candidate, review, or result identifiers; local disk or repository paths; source or candidate digests; Git commits or blobs; generated comments; build commands; machine warnings; or "do not edit" instructions. Detailed edition, provenance, rebuildability, and maintenance records remain adjacent maintainer evidence or product-declared reference-tail material unless a separately selected public use justifies a reader-facing projection.

#### E.11.PFP:4.2 - Put public units into the established Table of Contents

Immediately after the single `# Table of Contents` H1, continue the product's established ToC grammar. Represent the exact Readme and architectural-reference unit before the logical pattern index using the same kind of labelled segment and rows already used for non-pattern units in that product.

When an established ToC already represents the whole-account unit and pattern groups, add Readme there; do not invent a generic `Publication route`, a second mini-menu, or a new table shape.

A non-pattern publication unit receives no fabricated PatternID. Its product-declared entry remains mechanically recognizable and, when the carrier supports links, resolves to the exact unit. The unit's public title follows E.4's `<name of the explained whole> Architectural Reference` rule; its declared section key is a separate address choice.

Place the one authoritative logical pattern index after those public-unit entries. It may be one table or several ordered, uniquely labelled Part or placement segments. Every authoritative segment uses:

```text
| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
```

Across all segments, every published pattern body has exactly one row, every current `PatternRef` row resolves to exactly one complete body, and no PatternID or reserved locator appears twice.

Explicit `PlannedCatalogEntry` rows reserve future locators under E.8 H-10; they are outside the current-pattern row/body bijection and supply no available pattern or current dependency. A Part label groups rows for navigation; it is not a pattern row, a semantic parent, or another index.

PatternID, title, Part, and `§` position remain separate even when one row displays them together. PatternID supplies the stable public address within the named framework; the title explains the pattern; Part and `§` show where the current edition places it. Within each Part, the ToC rows and pattern bodies follow the same order. That order need not ascend by PatternID, and moving or retitling a pattern does not by itself change its PatternID.

For a portable reference, apply `E.8` H-10 to retain the complete PatternID or SectionRef and enough context to recover the publication set and document. Add a qualifier only where that identification is not already unambiguous.

A publication may declare a short `DocID` beside its full document title. State the publication set in which the declaration is unambiguous. The declaration identifies the whole document, not its embedded Readme, Architectural Reference or pattern collection.

A framework's existing reference code may be declared as that DocID without changing any PatternID; a standalone Architectural Reference may declare its own document qualifier. A document without a DocID remains referable by its full title within the named set.

Keep the document, the framework it publishes, the selected edition, its publication units and its carrier distinct. Several units can share one document; one framework can have several edition documents or carriers. A reference to an exact edition names that edition separately. A current-carrier catalogue derives its document identities from their declarations and full titles; it does not confer framework membership, pattern identity or authority.

Keep document identity recoverable from cross-document link labels and their accompanying context; add a qualifier when the complete address does not already supply it. The hyperlink may still provide a convenient carrier. An extracted passage retains the complete local address and any identifying context it needs.

For a DPF, `E.4.DPF:4.0.3` supplies the reference-code, local-locator and continuity decisions; this profile makes the selected distinctions visible.

Use E.8:4.2.2.2 to distinguish a source citation from an invitation to apply another contribution. Keep that purpose and any use-changing condition clear in ordinary prose. If an extract loses the heading that supplied this meaning, retain it in the extract; preserving the address alone does not preserve the intended reading. No repeated labels are needed when the wording is already clear.

Reserve `Support index — <lookup job>` for a secondary pattern lookup. Its exact header is:

```text
| PatternID | Pattern title | Lookup use |
```

Ordinary relation, source-return, maintenance, and reference tables may cite PatternIDs under truthful headings and other complete headers. Do not infer that they are indexes from their cell values. Reject a second `# Table of Contents`, a `Pattern Index` heading for the same job, an authoritative header outside the authoritative ToC region, or a support heading and header that do not occur together. Public-unit entries are navigation inside the one ToC, not another pattern catalogue.

#### E.11.PFP:4.3 - Keep one practical-entry set and two visible forms

Start the Readme body with `## Practical entries`. The product maintains one declaration for every selectable example and assigns each key exactly one public form: ordinary practical entry or Practical-Use Card. Each declared key occurs once, at H3 for an ordinary entry or at H4 for a card. A compact locator may precede or follow these examples, but it is a finding aid rather than another editable entry set.

The Readme explains what its selected examples help the reader do. Use F.19:4.4 to decide whether a catalogue or coverage-boundary reading also needs an explicit correction. The Readme tells the reader to bring the actual question and to use the product's index, direct patterns, or another finding aid when no example fits.

Tell readers that they can ask an assisting agent for explanations and comments in ordinary language, without the framework's specialist vocabulary. For example: “Explain this and give me your comments in ordinary language, without framework jargon.” Clear wording is the default under `F.19`; the request helps the assistant adapt its wording to the reader.

The selected examples should make two uses visible without implying that every question belongs to either displayed case:

- an ordinary entry shows how one direct pattern or one bounded direct route can answer a comparatively simple difficulty without a mantra; and
- a Practical-Use Card shows a recurring complex difficulty whose useful answer spans several direct pattern contributions and whose long dependency is easier to retain with a mantra.

The `First useful result or blocker` value gives the result of the action the entry supports, or a condition preventing that action. When several actions could be meant, name the relevant action in the value.

Use this ordinary-entry form:

```text
### <ordinary-entry key> — <plain title>

- **Situation:** <recognizable working situation>
- **Question:** <practical question>
- **First useful result or blocker:** <smallest useful result of the named action, or the condition preventing that action>
- **Start with:** <direct PatternID or bounded plausible set>
- **Stop or return:** <ordinary stop, wrong-turn return, or reopen condition>
```

When the product selects at least one card, place all selected cards under one group:

```text
### Practical-Use Cards

<brief introduction to the selected cross-pattern examples and the questions they help answer>

#### <card key> — <plain title>

- **Situation:** <recognizable recurring difficulty>
- **Question:** <practical question>
- **First useful result or blocker:** <smallest useful result of the named action, or the condition preventing that action>
- **Mantra:** <plain repeatable wording that retains the cross-pattern dependency>
- **Start with:** <direct PatternIDs or bounded route>
- **Stop or return:** <ordinary stop, wrong-turn return, or reopen condition>

##### Expansion for <card key>

<optional explanation only>
```

`### Practical-Use Cards` is a group inside the one `Practical entries` set, not another front door or selectable key. Omit the group when the product selects no cards.

The card's canonical structural field is `Mantra`; its value begins directly with the repeatable wording and needs no `Local`/`Long` prefix. A local reminder for one direct pattern or bounded result may remain in that pattern, an ordinary entry, or other teaching material, but it does not by itself select the richer card form. `E.11` owns this content decision.

Every selectable ordinary entry and card shares one product-wide semantic-key namespace. The product declaration assigns each key one form, so a key cannot occur as both H3 and H4. An H5 expansion repeats its enclosing card key only to attach optional explanation; it is not another selectable occurrence.

A card has zero or one expansion. Its compact portion ends after `Stop or return`; the expansion ends at the next H4-or-higher heading or the end of the group. The expansion may explain branch choices, examples, or exact result support, but cannot contain another H4 card or H5 expansion.

The product-language application declares one deterministic reading-burden measure and two maxima: one for the mantra and one for the complete compact card. The measure must suit the publication language; whitespace counting is suitable only where it meaningfully measures reading burden.

The maxima protect scanability and recall. They are not targets, proof of reader value, a fixed card count, or authority to delete a choice-changing distinction. Content that a compact card cannot carry truthfully returns to the direct patterns or, only when first choice needs it, the same-key expansion.

Applying this grammar does not select a card, prove that the examples cover the product, or show that every cited pattern is needed in a particular case. `E.11` defines the direct-entry/card comparison, cross-pattern mnemonic-gain test, and non-exhaustive discoverability purpose. The product-specific E.4 pattern declares its selected example keys, forms, reading-burden measure, and two limits. A validator consumes those values and checks structure; it does not decide content value.

Use `First useful result or blocker` for this field in new entries. In existing publications, `First useful result or honest blocker` identifies the same field, with the same value and position; including both labels in one entry repeats the field.

This profile keeps structural field keys in canonical English. A translation may translate surrounding prose and values and may add a human-readable gloss, but it does not silently replace or reorder the field keys. A translated structural-key profile needs a separately selected recovery and checking rule. Test translated and low-tool publications with actual readers and navigation tools rather than treating English parser success as accessibility evidence.

#### E.11.PFP:4.4 - Keep support units and adjacent products distinct

A Readme, architectural reference, ToC, pattern-body collection, relation or edition note, and refresh route may be publication units of one framework product when they serve its declared use and edition boundary. Place each unit where its readers can find and use it. A separate file is a carrier choice.

Use `E.4:4.1` to decide an adjacent product boundary from the useful result and its intended use. People may need to use, cite, or change a result as an identified whole, whether it appears inside a collection or through a separate carrier. State its identity, edition or current state, users, use, content boundary, and access route to the extent needed for that use. An established maintainer or maintenance commitment is not a prerequisite; record maintenance and refresh conditions when they are established and change reliance or use.

Examples include a source registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme. Their labels do not decide the boundary. Where an independent boundary is useful, point to the exact product edition or state. An annex may carry a declared snapshot or projection with a return to that product. Where ordinary framework use needs the material within the same boundary, include it as a named support publication unit.

One outer presentation carrier may expose several products. Each keeps its own identity, edition or state, form, access, and any separately established status or maintenance relation. Apply this profile to the FPF, DPF, or LPF constituents. A catalogue, evidence package, guide, service, programme, or other non-framework product uses the form selected for its own kind.

DRRs, build manifests, quality runs, digests, logs, and campaign state are process or maintainer evidence by default. A selected public use can justify a separate reader product or a public explanation drawn from that evidence. Publish durable use-changing reasons in the whole account or the relevant pattern; keep the dated decision, review, and release history in their records.


#### E.11.PFP:4.5 - Check syntax and product truth at the right boundary

The deterministic part of the form check handles recoverable syntax and projection agreement:

- absence of raw HTML from the complete Markdown publication under E.8:4.1.1, while retaining literal code, mathematical notation and Markdown autolinks;
- the product-declared title and Readme H1, the compact opening, and absence of prohibited development or machine material from reader front matter;
- the required H1 sequence plus the product-declared body and reference tail;
- product-declared Readme and architectural-reference entries in the established ToC grammar, before the logical pattern index, with no generic rival mini-menu;
- one correctly addressed, content-free architectural-reference end heading at the boundary of that unit;
- authoritative index segments, aggregate current-pattern row/body bijection, distinct future-facing `PlannedCatalogEntry` rows, duplicates, and reserved support-index grammar;
- the Readme's one practical-entry set; the product's declaration of example keys and forms; exactly one H3 ordinary entry or H4 card per declared key; five ordered ordinary-entry fields; a non-empty card-group explanation; six ordered card fields; the shared reading-burden measure and mantra/card limits; and zero or one same-key H5 expansion with the declared boundary; and
- equality and source agreement of every optional public cue that is projected.

Check Markdown grouping with a focused source-hazard scan and a parser-backed render of the same candidate. Inspect the rendered heading outline and the block, list, table, code and link structure together. Reuse matching unchanged results. A clean mechanical result supports but does not replace the reader-visible judgement.

The product-specific check compares every visible cue with the exact edition or relation record from which it was projected and checks the product-specific body, reference tail, and any pinned compact-front shape. A syntax-valid but unresolved value fails there. A field absent from the public opening is not a form defect unless a selected reader use and product-specific rule require it.

A reader also follows the twelve content questions in section 4.7 to their public answers. A link or heading proves only that a target exists; reading establishes whether it answers the question at the claimed scale and preserves direct use. Reuse unchanged answers and current matching results. This content reading belongs to the selected authoring or publication question; the common form adds no separate release procedure.

Neither check decides framework scale from pattern count. Report `pattern_count = 1` as a diagnostic. Use E.4, E.4.PFAD, E.4.DPF.DA, E.11, E.21, and the applicable subject patterns to judge whether the result is a usable pattern language for its declared field and first use.

#### E.11.PFP:4.6 - Return the form result without overclaiming

Return the exact framework edition, edition-record source, carriers checked, form units found, public-cue agreement, logical-index result, practical-entry declaration and form result, product-specific tail checked, the public answers or unresolved content questions under section 4.7, and every mismatch or unresolved ref. Say separately whether the edition, carrier, publication occurrence, availability, currentness, or framework adequacy has an applicable result. Do not infer those claims or the truthfulness of card selection from form conformance.

#### E.11.PFP:4.7 - Explain the Methods at each selected scale
Develop the practical way and its explanation for the receiving use through C.39:4.3–4.6. E.4.CM applies that general work to connected framework Methods. The publication functions below organize its public answers and add framework-specific form and placement; they are not a universal template for developing or describing every Method.

Use all twelve substantive E.8 functions as authoring questions for the whole framework and each substantive profile selected by its architecture. Answer them at the scope the publication promises. A framework may describe one composite Method through many patterns, several related Methods, or a repertoire used in different combinations. Where an exact MethodDescription claim matters, use `A.3.1` to identify the admitted Method and `A.3.2` to test the description episteme's MethodDescription membership. The number of patterns, mantras, files, or description media does not settle that identity.

The whole account connects the answers that individual pattern bodies supply. Write the shared answer once and give exact returns to inherited content. Determine those answers from the language's promised work before committing to an illustrative route.

E.8:4.2.1.3 governs the choice and continuation of examples: a connected account need not follow one project, and a successful route through one case does not establish the account's completeness. Keep explanations of significant alternatives and limits even when they require leaving that case.

At a narrower scope, state what changes in the situation, contribution, combination, evidence, result, or boundary. When an answer is missing, say which question remains open, which promised use it limits, and what remains usable.

Develop a missing instruction in the underlying account through E.8:4.2.1.1 before choosing how to present it. Then follow the promised use through the resulting publication, including any return to a supplying explanation. The reader must still obtain the input meanings, necessary operation, intermediate result and action-changing conditions that make the continuation possible.

A short entry may rely on its reachable developed destination; it must keep any condition needed before taking its first action. A full explanation elsewhere does not close a gap if the reader cannot find or use it under the declared access conditions.

Restore missing content at its source or repair its presentation and return, then revalidate the affected connected reading under F.19. A sound file structure or resolved link alone does not establish that the instruction survived.

| E.8 function | Question the whole or profile account answers |
| --- | --- |
| Problem frame | Who is doing what kind of work, under which conditions, and when would this language help? |
| Problem | Which inquiry, intended transformation, opportunity, or recurring difficulty needs an answer? What remains unresolved with the available approach? |
| Forces | Which competing requirements, resource limits, evidence conditions, or values shape the choice of Methods? |
| Solution | Which Methods and pattern contributions answer the problem? How do their results connect, which choices change the route, and where can the reader enter directly? |
| Archetypal Grounding | Which actual or minimally viable worked cases make the needed connections and a consequential branch or limit inspectable? What does each contribute to the declared scope? |
| Bias-Annotation | Which assumptions, perspectives, exclusions, or access conditions affect whose work the language serves and where its claims travel? |
| Conformance Checklist | Which substantive questions establish correct use at this scope? Which answers can be inherited, and which changed conditions need their own judgement? |
| Common Anti-Patterns and How to Avoid Them | Which documented failures, text-invited misreadings, or consequential neighbouring cases need a practical correction? Apply the grounded-guard rule in E.8 and F.19. |
| Consequences | What practical gains, costs, residual limits, and subsequent moves follow from using this arrangement? |
| Architectural Rationale | Why does this organization of Methods serve the declared use? Which serious alternatives and trade-offs explain its boundaries, profiles, composition, and reuse, and when should a different choice be made? |
| SoTA-Echoing | Which current answers and source contributions shaped the Methods and their shared architecture? What was adopted, adapted, or rejected against a serious alternative, and what would reopen that choice? |
| Relations | Which specialization, bounded-use projection, composition, reuse, dependence, or publication-grouping relations actually hold, and where does each named contribution become useful? |

When a condition governs a whole combination of Methods, give it one public statement at the scope where that combination is used. State the quantities, assumptions, or other conditions needed to apply it, and return to that statement from affected profiles and patterns. Pairwise relations remain useful, but a condition on the whole set may require a different decision. A change to that condition reopens the combinations that rely on it; unchanged local contributions remain available.

Also explain the relevant Method-composition structure and how its constituents are enacted in ongoing Work. A selected action can constitute part of a larger work that is being performed at that same moment. Give a representative example in which a condition of the whole changes the constituent action; show where a missing intermediate capability or incompatible resource demand prevents the combination. B.1.5.EW recovers that connection and B.1.5.RS examines a constituent replacement.

A DPF can describe only some of the needed constituent–whole connections: state the preparation, support and coordinating performance needed beyond its own descriptions. Reuse clear existing explanations and stop decomposition when further detail cannot change the use. Keep dependencies on earlier results where later work relies on them.

Publish the connected account as `<framework name> Architectural Reference`, the framework-level application of E.4's architectural-reference function. An all-in-one publication embeds the unit in its front matter; a multi-file framework gives it a discoverable place in that framework's assembly. Readme explains how to enter it. E.11.DSG governs the account and its useful question-led entries; this profile governs the framework's form.

Use `Reference` as this unit's address key, identifying its explanatory function. The qualified title, unit key, file and edition identity remain distinct; a preface with a different introductory function does not replace the architectural account.

At a wider language-assembly level, the corresponding Suite or FPF Library Architectural Reference explains the connections added there and returns to the framework's account. A separate source host, downloadable copy or site page is not another assembly level. Preserve enough rationale, source synthesis, alternatives, and worked detail for the intended reader to understand and adapt the language without its development intake or DRR. An exact inherited answer can satisfy a question; merely naming a pattern or listing source titles cannot supply missing explanation.

These are twelve content functions, not twelve compulsory new H1 sections. Each full pattern body retains its address and E.8 form. The outer Solution explains how to use the contributions together and returns to the bodies in the existing collection. It does not nest them under a new parent heading or require reading the whole account before a direct pattern use. If the public account uses the canonical function labels, prefer `Architectural Rationale`; `Rationale` remains the accepted alias defined by E.8.

There is no fixed number of generality scales. For example, a reader can move from FPF's general treatment of Methods to its Method-development family, a pattern-language construction specialization, a narrower literature-based extension profile, and a pattern that recovers one candidate Method from source and Work evidence. Further useful scales can be introduced.

Explain the relation at each move: a profile is a bounded-use projection; specialization carries inherited content plus a delta; composition connects Method contributions; reuse makes one contribution available in several settings; a chapter or Part groups publication text. A substantive narrowing must pass `E.8:4.1.3`'s same-situation usefulness comparison.

A pattern can participate in several profiles, and a profile can draw on several contributions. Describe this structure through the relations that hold.

For a mathematical view, select the elements and relation being modeled and use the applicable mathematics. Use `C.29` only when a separate question about choosing, transferring, or relying on that mathematical representation remains.

A partial order needs its order properties; a lattice additionally needs the required bounds for every relevant pair. Multiple parentage or overlapping membership alone establishes neither. Keep that mathematical representation distinct from the Methods and their subject-side relations.

##### E.11.PFP:4.7.1 - Make an architectural-reference section recognizable on its own

A reader entering through search, a quotation, a link or a retrieved excerpt may see a heading without its parents. Every heading that introduces architectural-reference content therefore carries the framework's public reference code, the publication-unit key `Reference`, and its complete ordinal section path:

```text
## <FrameworkCode>.Reference:<n> - <Title>
### <FrameworkCode>.Reference:<n>.<m> - <Title>
```

For example, `## STR.Reference:1 - Problem frame - Direction and commitment under changing conditions` identifies the first section of a Strategy architectural-reference unit whose key is `Reference`. `#### FPF.Reference:16.8.2 - Production and situated use are different contributions` identifies a nested section in the FPF Core architectural-reference unit.

Use the framework's declared public code; name the framework as well when quoting outside a context that identifies it. The enclosing H1 gives the qualified Architectural Reference title and has a product-declared ToC entry. Changing a former section key requires updating its maintained current returns; changing the title alone does not preserve a former URL fragment.

Close the complete architectural-reference unit with one content-free H2 heading, `## <FrameworkCode>.Reference:End`, after its last paragraph, list or other content and before the next publication unit. For example, the Strategy architectural-reference unit ends with `## STR.Reference:End`.

This visible boundary shows where the unit ends when it is copied or retrieved separately. It closes the whole unit, not each numbered subsection; it adds neither a content section nor a pattern-index entry. A heading shown inside a fenced example does not close the unit.

Number sibling sections in reading order, starting at 1, and carry the complete parent path into nested headings. Each nesting level adds one heading level and one ordinal. These ordinals locate sections in this publication unit; their titles state the content functions. An account can combine several E.8 functions in one section or explain one function across several sections. Keep that useful arrangement instead of adding twelve empty sections to match numbers. The rule introduces no limit on useful conceptual scales; physical Markdown heading depth remains a carrier constraint.

`STR.Reference` names a publication unit. Its section addresses are `SectionRef` uses under E.8, not declarations of additional patterns: the pattern index continues to contain the individually declared pattern bodies. Apply the same self-identifying construction to a profile account or other support unit when it needs its own section addresses, using its product-declared unit key. A profile explained inside the architectural reference retains that unit's section path; this text position does not decide the profile's semantic relations.

The prefix lets a reader distinguish a whole-language Problem frame from the Problem frame of one pattern before choosing what to read or cite. Visible names and numbers also survive copying and printing, where a hidden anchor cannot help.

The visible address and title are separated by an ASCII hyphen with one space on each side. Build each clickable fragment from the complete rendered heading according to the target Markdown carrier's rules, including punctuation removal and duplicate handling. When a heading changes, update its direct links in the publication, source templates and public consumers together. Check that the link resolves to the intended heading, then read that target for the answer the link promises. Keep the visible address usable for search and non-clickable copies. E.8:4.1.1 excludes raw HTML from this form, including compatibility anchors.

##### E.11.PFP:4.7.2 - Make the language's long reasoning visible

Use a long mantra when readers need to keep a substantial connected account in attention across several questions, explanations or pattern contributions. Recover that account before compressing it. Identify what the reader is trying to understand or obtain, the questions that must be related, and why their answers belong together.

A result dependency is one possible connection; shared assumptions, jointly necessary conditions, alternative constructions, conflicting demands and returns can be equally important.

Recover missing reasons through B.5.RA and develop missing constructive joins through E.4.CM. The presence of one operational step per source topic does not preserve the explanation.

Explain how to assemble and revise the answers. Which partial answers can be used now, what remains unknown, and how do local answers constrain the whole? Which changes reopen which other answers? How can a reader choose the next inquiry or construction without mistaking the teaching order for a work sequence? Use the actual subject knowledge to answer these questions. A drawing of connected boxes or a sequence of PatternIDs cannot provide an absent inference, construction or applicability condition.

Keep the full explanation at the scale that owns its subject. E.4.CM:4.5 distinguishes completing an existing pattern, developing a separately useful recurring Method as a pattern, and explaining the material relations of several Methods in an Architectural Reference. The title or mnemonic form settles none of those choices.

A framework can have several long mantras for different questions; a repertoire need not acquire one artificial total sequence.

Where an existing explanation is sufficient, preserve it and repair its name or access instead of writing a shorter substitute. Where a source explanation enables readers to understand or adapt the contribution, retaining its thesis alone is insufficient.

Give the contribution a recognizable name, a stable existing kind of address, and both a compact reminder and a reachable developed account. Use F.18 when selecting a durable public name.

A mantra that recalls a separately applicable reasoning Method returns to that Method's ordinary pattern address and pattern-index entry. A reminder of the language's architecture can return to its Reference section. Establish that difference through E.4.CM:4.5 before choosing the address; completeness of a Reference explanation alone does not make it an adequate sole Method owner. No new markup or universal mantra record is required.

The compact expression may use questions, relations or actions. Choose it from the explanation rather than restricting the explanation to what fits one memorable sentence. Preserve the subject and scope across the two forms.

Make the account visible at each assembly level where it helps explain the whole. A Framework Reference explains the framework's connected reasoning and returns to its full pattern bodies. A Suite or Library Reference explains the connections introduced at that wider level and returns to the constituent accounts, without copying all their explanations.

In a README, show the most consequential reasoning connection in ordinary language, name the long mantra when one is useful, and give a direct return to its full account. This overview can be published without selecting a Practical-Use Card. E.11's comparison of entry forms decides whether a card helps a particular first-entry use; it does not decide whether the underlying subject reasoning is worth publishing.

Treat a compact order as a teaching unfolding of the connected reasoning. Explain material branches and returns, and use A.22.CGUS for the actual continuation and structure questions. A phrase order does not determine Work order or qualify a CGUS by itself. Different long mantras can constrain one another through a shared subject or premise: for example, a system construction changes the means of obtaining it, while a capacity limit can make that construction or its promised use worth reconsidering. State that specific connection; neither co-location in a book nor a universal instruction to read every mantra establishes it.

Check what the reader can reconstruct from the publication. Can the reader explain the needed grounds, recognize locally plausible but jointly incompatible answers, and determine which answers a consequential change reopens? Use materially different circumstances when they expose a hidden restriction.

These are questions about recoverable explanation and application; fluent recitation, one completed example and a mnemonic advantage do not answer them. Conversely, a source-grounded explanation can be useful without a measured recall advantage. Claims of improved learning, memory or field performance require their own evidence.

### E.11.PFP:5 - Archetypal Grounding

**DPF with non-ascending pattern addresses.** A Systems Engineering DPF edition orders `SYSE.1`, `SYSE.16`, `SYSE.17`, and `SYSE.2` because that sequence helps readers. Its ToC rows and H2 bodies follow the same order. The `§` column reports each current position; it is not part of the PatternID. A later move changes the rows and bodies together without renumbering a continuing pattern. A citation outside the carrier says `Systems Engineering DPF, SYSE.16`; one intended to recover the earlier body also names the edition.

**DPF, all-in-one and low-tool.** A horticulture DPF is distributed as one Markdown file and a printed copy. Both open with the public framework name and `Edition: Horticulture DPF 2.1`; the Markdown line links to a public edition page and the print line gives the same public address. The ToC, practical entries, Horticulture Principle Framework Architectural Reference, four pattern bodies, coverage account, and refresh note follow. Authorship, source provenance, and change history remain reachable after the bodies. Readers can identify and return to the edition without crossing build records before their first working question.

**FPF, split carriers.** One website exposes an FPF edition through a front page and a separately downloadable Readme. The front page already identifies the edition, so its embedded Readme begins with practical entries. The standalone Readme repeats only the short edition line because it can circulate alone. Both return to the same public edition record; neither mints another edition or editable status copy.

**LPF with a choice-relevant cue.** An LPF supports two public language editions whose maintenance windows differ. The product-specific rule shows one short language-and-support cue after `Edition` because it changes which edition a practitioner should use. It does not copy the maintainer, build digest, source path, or complete dependency record into the opening.

**Adjacent product.** A separately maintained horticulture source registry has its own current state, users, selection rule, access route, and refresh commitment. The DPF points to that state; copying a snapshot into an annex does not create a second authoritative registry. One combined website may expose both, but the registry retains its catalogue form and receives no invented framework fields.

**Whole Method Engineering account.** An engineer extending a pattern language from a handbook needs both source recovery and a decision about what the new language will let practitioners do. The Method Engineering Principle Framework Architectural Reference explains the overall working question and returns to the source-recovery and comparison patterns. Architectural Rationale compares retaining a profile inside the language with giving it its own usable identity; the shared sources and trade-offs remain public. If the handbook cannot be inspected, the account names the source-dependent claim that remains unresolved and leaves unaffected direct uses available. A catalogue of source titles would not supply that missing basis.

**Condition of a whole combination.** Three proposed activities each need seven observer-hours that cannot be shared between activities. The available total is eighteen observer-hours. Any pair needs fourteen and fits; all three need twenty-one and exceed the total by three. The whole account states the resource condition once. The reader can select a feasible subset or obtain at least three additional observer-hours before committing to all three. Separate successful pairwise checks leave this whole-combination decision open.

**Inquiry and direct use.** Four pump inspections show three repeated orders and one reversal after a vibration cue. The public entry returns directly to `A.3.1.MR`, which recovers candidate Methods from Work evidence. Its worked case compares a fixed order with an exception against a cue-responsive order. In a fifth inspection, observe whether the technician changes order when the vibration cue is present. That observation can distinguish the accounts; until then, both remain candidates. The reader has a next investigative action while the larger inquiry remains open.

**Shared profile.** A Russian-language profile supports both a guide and a slidement. It inherits `F.19` for recovering a sentence's claim, participants, and useful action, and adds Russian agreement checks. For example, change «Группа проверяют результат» to «Группа проверяет результат» (“The group checks the result”): the named collective remains the performer, while the verb agrees with the singular grammatical subject. Read the repaired sentence under F.19; reuse that matching result when the unchanged sentence appears in both formats. The guide and slidement retain their own format and use conditions. The profile's public account explains this shared contribution and language-specific delta once, with returns from both uses.

**Near miss.** A relation table has rows whose first cells are PatternIDs and titles, followed by relation and source-return columns. It remains a relation table. A checker that calls it another pattern index from those cell values is guessing semantics from data shape and fails this profile.

### E.11.PFP:6 - Bias-Annotation

**Scope:** Limited to the public Markdown form of an FPF, DPF, or LPF edition and faithful low-tool projections of that form. It is not a universal publication template and does not prescribe the form of an adjacent guide, catalogue, service, programme, evidence package, or maintainer record.

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Gov | A visible status or form pass is read as acceptance, authority, release, or currentness. | Keep those claims under their own decisions and relations; the form only exposes selected public cues. |
| Arch | A file, website, or combined package is treated as the product or edition, or every nearby result is forced into the framework form. | Name edition, particular expression, reusable publication form, carrier, occurrence, support unit, and adjacent product separately; apply this profile only to framework constituents. |
| Epist (Epistemological and Ontological) | A date, filename, digest, or editable front block becomes edition identity or evidence that a relation obtains. | Use one stable public designation and edition-record return; project only exact facts from their own records. |
| Prag | Administrative completeness displaces the reader's first question, or an optional cue appears without changing use. | Put the smallest useful edition cue first, then the ToC and practical entries; require a named reader decision for every extra front cue. |
| Did | Predictable labels become rigid English-only machinery, terse navigation hides the patterns needed to act, examples read as a coverage catalogue, or compactness deletes a choice-changing distinction. | Keep recognizable headings, the five-field ordinary form and six-field card form, the entry guidance and unmatched-question return in §4.3, one product-language burden measure with mantra/card maxima, useful detail, and direct-pattern return; test translations, low-tool carriers, navigation, and mnemonic recall with intended readers. |

### E.11.PFP:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFP.1 Scope truthful | The particular expression follows the selected publication-form rules and expresses one named FPF, DPF, or LPF edition; no carrier or adjacent product is relabelled as that edition. |
| CC-PFP.2 Practitioner-first opening | The compact product-declared opening leads directly to the ToC; the common profile has not inserted a record or completeness block ahead of the reader's question. |
| CC-PFP.3 Edition return works when needed | When exact edition return changes use or reliance, the shortest public designation and locator resolve without repository knowledge; otherwise no unused return field is mandatory. |
| CC-PFP.4 Extra cues earn their place | Every cue before the ToC is projected from its exact record and changes a named reader decision or action; no common optional field is required merely for completeness. |
| CC-PFP.5 Development state excluded | Reader front matter contains no campaign or candidate identifier, local path, digest, Git identity, generated comment, build command, machine warning, or maintainer instruction. |
| CC-PFP.6 Entries and order recognizable | The title, compact cues, ToC, Readme and architectural-reference entries in the product's established ToC grammar, Readme, architectural reference, pattern collection, and product-declared reference tail occur in the selected order; every declared target resolves where links are used. |
| CC-PFP.7 Logical index and order truthful | One logical index may use several labelled segments, but every current `PatternRef` row resolves to one complete body and every body has one row. Explicit future-facing `PlannedCatalogEntry` rows are outside that bijection; all PatternIDs and reserved locators are unique within the named framework. PatternID is separate from title, Part, and `§` position; ToC and body order agree within each Part even when PatternIDs are non-ascending. When the surrounding text does not identify the framework, a citation names the framework together with the PatternID; a citation selecting the body published in one edition also names that edition. |
| CC-PFP.8 Other tables remain truthful | Only the closed authoritative and support-index grammars are treated as indexes; relation and reference tables are not reclassified from cell values. |
| CC-PFP.9 One entry set and declaration | One `Practical entries` set contains every selectable ordinary entry and selected card. One declaration for the product assigns every key exactly one form; each key has exactly one selectable H3 ordinary-entry or H4 card occurrence, and no rival key list or entry set exists. |
| CC-PFP.9a Ordinary entry usable | Every ordinary entry gives the five fields in order and retains any richer content needed for the first useful result and stop boundary. No mantra is forced onto a locator or ordinary entry. |
| CC-PFP.9b Selected card usable | Every selected card gives the six fields in order, begins its `Mantra` value directly with repeatable plain wording, preserves a real path through several direct pattern contributions, returns to those patterns, and has zero or one same-key H5 expansion outside the compact card. Applying the form is not evidence that the card should have been selected. |
| CC-PFP.9c Product-language guard shared | The product declares one measurable language-appropriate reading-burden rule plus mantra and compact-card maxima, and authoring and validation consume the same values. Canonical English field keys do not make whitespace limits universal. The limits check compactness; they neither select cards nor prove example coverage. |
| CC-PFP.10 Readme projection restrained | A standalone Readme repeats a short edition cue only when circulating without it would change use or return; it does not duplicate the edition or rebuildability record. |
| CC-PFP.11 Product boundary preserved | Framework support units share the declared framework boundary; independently useful adjacent products retain the boundary selected through E.4:4.1, their own identity and form, and the access or separately established maintenance conditions that change use. |
| CC-PFP.12 Combined carrier neutral | Every constituent product keeps its own form and identity; E.11.PFP applies only to framework constituents. |
| CC-PFP.13 Claims remain separate | Form conformance is not reported as acceptance, adequacy, carrier identity, publication, availability, access, maintenance, or currentness. |
| CC-PFP.14 Scope examples survive | The rule remains usable for FPF, DPF, and LPF editions and for a low-tool or non-clickable carrier without introducing a second edition identity. |
| CC-PFP.15 Navigation remains usable | The ToC represents Readme and the architectural-reference unit in its established product-native grammar before the singular pattern index; headings and labels describe their purpose, and the integrated rendered-structure summary plus intended-reader inspection exposes grouping defects without a second full read. |
| CC-PFP.16 Whole account usable | Every substantive E.8 question has a public answer, an exact inherited answer, or an explicit use-changing gap at each selected scope. The framework's Architectural Reference connects Methods and their results, retains their Architectural Rationale and shared source synthesis, and leaves direct pattern entry available. Its embedded or separate carrier does not change that function. Headings or locators alone do not establish this content. |
| CC-PFP.17 Scales and relations truthful | Further useful scales remain possible; the actual specialization, profile, composition, reuse, and publication-grouping relations are distinguished. A claimed mathematical order or lattice satisfies its mathematical conditions. C.29 is used when a separate representation-choice, transfer, or reliance question requires it. |
| CC-PFP.18 Whole-account sections addressable | Every architectural-reference subsection exposes its framework code, declared unit key and complete ordinal path; nested paths and heading levels agree. The whole unit ends with one correctly addressed, content-free H2 `:End` heading before the next unit. Addressed profile or support units identify their declared unit. Links resolve to the intended rendered headings, while the target content supplies the promised answer. Publication-unit addresses do not create pattern-index entries, and a changed title does not itself preserve a former fragment. |

### E.11.PFP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Complete record before entry | A maintainer detail—such as authorship, assistance, date, dependency, provenance, a product-declared maintenance status, support window, or currentness window—or the whole edition record appears before the ToC merely because it exists. | Preserve the product's compact opening; project only cues whose possible values change a named reader move and keep the full record in maintainer evidence or the justified reference tail. |
| Development state as public identity | Candidate keys, local paths, digests, commits, blobs, generated comments, or machine warnings describe the publication to readers. | Keep them in builder or maintainer evidence; publish a stable designation and public return. |
| Date as edition identity | Two editions on one day become indistinguishable. | Use a stable public designation linked to the exact edition record; show a date only when it changes reader use. |
| Fresh navigation grammar | A generic mini-menu is inserted ahead of an established ToC, duplicating units and making one product unlike itself. | Extend the product's existing non-pattern ToC segment and make the checker recognize that exact grammar. |
| Flat-index compulsion | Visible Part grouping is removed merely to satisfy one-table code. | Check one logical index across consistently headed, uniquely labelled segments. |
| Index by cell guess | A relation or source-return table is rejected because it cites PatternIDs and titles. | Recognize only the closed authoritative and support-index grammars. |
| Position used as PatternID | Patterns are renumbered when the ToC changes, or identifier order is read as dependency, Method order, or semantic hierarchy. | Keep PatternID stable while the pattern continues, show current `§` position separately, keep ToC and body order aligned, and state every substantive relation in its own field or claim. |
| Readme as another edition | The standalone Readme mints its own designation or copies a full editable record. | Repeat only the shortest cue whose absence would change use or return when the Readme circulates independently; never duplicate the edition or rebuildability record. |
| Outside the pattern set means another product | An architectural reference, coverage account, or refresh note is split into a product with no independent use. | Keep it as a named support unit when it shares the framework boundary. |
| Shared use means one product | A cross-framework registry or service is absorbed into one DPF. | Treat shared use as a prompt to inspect the boundary; preserve an independent product when its own use, citation, or change makes that useful. |
| Combined carrier merges products | A framework and catalogue receive one identity and one framework index. | Keep the outer carrier neutral and each constituent in its own selected form. |
| Parser pass as accessibility | Canonical English labels parse, so translation, assistive navigation, low-tool return, and cold-reader use are assumed. | Test the actual carrier and reader route; repair headings, labels, links, projections, and mnemonic wording without weakening source return. |
| Rival entry sets or key registries | Ordinary entries and cards are maintained as separate front doors or the same key appears once in each list. | Keep one `Practical entries` set and one declaration for the product that assigns every selectable key one form and one occurrence. |
| Card classification by syntax | An H4, six fields, a short body, or a historical label is treated as proof that the reader needs a card. | Use `E.11` to compare the same truthful content without a mantra; the form checker only verifies the selected form. |
| One product's labels, example inventory, and limits made universal | Another product must publish the same topics or another language must use one product's labels and whitespace limits even when they do not support its readers. | Preserve the shared field order and direct-versus-cross-pattern distinction, but let each product select its non-exhaustive examples and declare one suitable measure with mantra/card maxima. |
| Whole account as a second catalogue | A list of pattern names replaces the explanation of how their contributions work together. | State the shared problem, connected results, choices, and reasons; return to the full bodies for each contribution. |
| Recursive form as fixed taxonomy | Every intermediate group receives a parent pattern, or every profile must have one exclusive parent. | Select substantive scopes by useful changes in practice and state the relations that hold; keep publication grouping separate. |

### E.11.PFP:9 - Consequences

Readers retain each product's compact familiar opening and find Readme and the architectural-reference unit in the ToC grammar already used by that product, before the one authoritative pattern index.

Inside the Readme they see one selected practical-entry set: ordinary examples show cheap direct use, while only cross-pattern cards selected by E.11's mnemonic-gain test add a visible mantra and an optional bounded expansion.

Optional public cues remain recoverable from one source when they change use, while development and rebuildability records stay out of reader front matter.

Builders gain checks that fail on missing public-unit entries, duplicate or cross-form keys, card grammar, structural, projection, and development-state drift without guessing table meaning, deciding card value or coverage, or inventing a rival navigation block.

The whole account also makes shared choices and source synthesis accessible beyond individual bodies. Authors can refine one profile without copying the entire language, and readers can see which answers remain inherited. Keeping those returns current costs work; concentrating the shared explanation reduces the number of independently editable copies.

### E.11.PFP:10 - Architectural Rationale

The shared rule fixes only the recognition points whose reuse pays across FPF, DPF, and LPF: a compact product-declared opening, Readme and the architectural-reference unit represented in the established ToC grammar, one logical pattern index, one selected practical-entry set with five-field ordinary examples and six-field selected cards, truthful product boundaries, and recognizable major units.

It leaves titles, optional public cues, the exact product-native ToC segment, example selection, the reading-burden measure and two limits, front line shape, and reference tails with the product-specific rule because their value depends on the reader's choice and publication language. These product-specific choices preserve direct entry while keeping deterministic checks narrow.

The twelve E.8 functions supply the content questions because a whole language, a substantive profile, and an individual pattern all need to explain working situations, Methods, evidence, use, and consequences. Reusing the functions makes omissions visible without inventing a new account for every product. Exact inherited answers and explicit deltas keep the explanation proportional to what changes.

The alternative of ad hoc architecture prose can preserve valuable reasons but offers no stable way to find a missing kind of answer. Literal recursive pattern formatting would add parent bodies and rigid heading depth that the subject's relations do not require. The selected form therefore reuses the substantive questions inside the established publication units and keeps the full patterns directly accessible.

### E.11.PFP:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Problem and selected response | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should one public FPF, DPF, or LPF edition give a cold reader an actionable front without confusing navigation, product identity, or maintainer evidence? | The best-known line for this bounded use combines `E.11` situation-first entry with the edition, body, publication, and carrier boundaries in `E.4.FPF`, `E.4.DPF`, and `E.24.PUB`: use a compact product-declared opening, one authoritative ToC, one non-exhaustive practical-entry set, exact returns to full pattern bodies, and only those public cues whose possible values change the reader's next move. | A metadata-first opening and wholesale adoption of a four-mode documentation architecture are alternatives. Diátaxis supplies a goal-oriented alternative that distinguishes tutorials, how-to guides, reference, and explanation; WCAG 2.2 supplies the serious narrower comparator for headings, labels, consistent navigation, and more than one finding route. | Putting maintainer metadata first can delay entry and duplicate maintainer records; a rigid document-mode taxonomy can split or replace the FPF pattern body; accessibility criteria alone cannot decide edition identity, body membership, or product truth. **Adapt:** sections 4.1–4.5, Grounding, and `CC-PFP.2–10/14–15` keep the reader move, authoritative index, truthful labels, stable headings, and source return together. **Reject:** a universal document taxonomy, a mandatory metadata front, and any claim that form or parser conformance establishes accessibility, identity, adequacy, or publication. | Current FPF patterns supply the selected product-specific line. Diátaxis [*Start here*](https://diataxis.fr/start-here/) and [*How-to guides*](https://diataxis.fr/how-to-guides/) supply the goal-oriented comparison and the distinction between documentation needs. [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is a narrow accessibility comparator because its navigation and labelling criteria change the checks; it does not define an FPF-family product or establish this profile's adequacy. | Reopen if translated, assistive, low-tool, or cold-reader use shows that another front reaches the first relevant body and return at lower effort while preserving edition identity, truthful labels, navigation consistency, and the maintainer/public boundary. |
| When should the practical-entry set promote an ordinary entry to a selected card, and how much card apparatus is justified? | The best-known current FPF line is selection by demonstrated mnemonic gain: keep one non-exhaustive entry set, use the lighter five-field ordinary entry by default, add the six-field card only when the longer reminder improves recognition or return, and let each product declare one reading-burden measure and its own maxima. | Card-per-pattern fanout and the opposite no-card rule are the serious defaults. The first turns a navigation aid into a rival catalogue and fixed quota; the second withholds a useful longer reminder even when cross-pattern choice repeatedly fails. | Both defaults ignore the actual reader decision. **Adapt:** section 4.3 and `CC-PFP.9a–c` preserve one entry set, the unmatched-question return and conditional coverage correction in §4.3, stable field order, one same-key expansion, product-language limits, and zero-card permission. **Reject:** universal card counts, copied FPF numeric limits, syntax as proof of mnemonic gain, and a second card front door. | `E.11` supplies the selected mnemonic-gain rule; the current FPF examples, LPF compact locator, and direct-answer DPF Suite Reference are comparison and counterexample evidence. They show that a useful direct entry need not become a card and that a framework may legitimately declare zero cards. No external source, current edition, or local example validates a universal quota or reading measure. | Reopen the smallest affected entry form or check if actual product-language or cold-reader comparison of the same content with and without the card changes its classification, exposes a missing visible field, or shows that the declared burden guard prevents reliable choice and return. |
| How can a language explain its Methods as a whole while preserving direct pattern use and useful profiles? | Combine whole-language explanation with individually usable patterns; distinguish the Method from its representation and retain the shared reasons for combining or narrowing contributions. | Ad hoc prefaces can omit one kind of answer; literal repetition of a full pattern at every group can duplicate content and imply false parentage. | **Adapt:** section 4.7 reuses E.8's twelve substantive questions with exact inherited answers and profile deltas. The publication keeps its direct entries and body grammar. The rationale for organization becomes public; dated development history remains separate. | Fowler's [*Writing patterns*](https://www.martinfowler.com/articles/writingPatterns.html) (2006) is a historical practice account of narrative plus individual patterns. Iba and Kanai's [pattern-language methodology](https://hillside.net/plop/2021/plopourri/PLoP21_PLOPOURRI_Iba_Methodology2.pdf) (2021) contributes bottom-up and whole approaches with several descriptive levels. Gericke, Eckert, and Stacey's [method-description study](https://oro.open.ac.uk/86670/1/86670.pdf) (2022) supports explaining a method's idea, procedure, use, and tools together. These sources motivate the distinctions; they do not establish a universal twelve-section layout or a limit on scale. | Reopen the affected correspondence if actual whole-language or profile use loses an actionable answer, forces duplicate explanation, or makes a direct pattern harder to use. |

### E.11.PFP:12 - Relations

- **Specializes:** `E.11` for the common reader-facing form of one FPF, DPF, or LPF edition; `E.11` retains practical-use discoverability and first-result routing.
- **Uses:** `E.8` for the twelve substantive content functions, preferred Architectural Rationale title, intended-reader boundary, and usefulness of narrowing; `A.3.2` for an exact MethodDescription claim and `C.29` when choosing, transferring, or relying on a mathematical view raises a separate representation question.
- **Coordinates with:** `E.4`, `E.4.FPF`, and `E.4.DPF` for framework/product boundary, product-specific publication units, optional reader cues, body order, and carrier assembly.
- **Coordinates with:** `E.24.PUB` for publication occurrence, selected edition, form expression, carrier bearing, audience, bounded use, availability, and access; and `E.17` for bounded publication projections and source return.
- **Coordinates with:** `E.4.PFR` for exact dependency and edition relations, `G.11` for currentness and refresh, `E.4.DPF.DA` and `E.2.DA` for applicable package or whole-FPF adequacy, and `E.21` for pattern quality.
- **Does not replace:** product-specific builders or validators, the edition record, `FPFEditionRebuildabilityRecord`, `FrameworkPackageManifest`, an architecture decision, or a public product boundary.

### E.11.PFP:End
