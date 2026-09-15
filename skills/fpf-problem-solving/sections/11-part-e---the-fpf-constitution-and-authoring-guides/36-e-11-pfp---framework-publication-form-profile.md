## E.11.PFP - Framework Publication Form Profile

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

The opposite repair is also harmful. A rigid carrier template can put authorship, credits, dates, status, dependencies, build details, and maintainer records ahead of the reader's question whether or not those facts change the reader's choice. It can also force a catalogue, inquiry programme, guide, or other adjacent product to pretend that it is a framework edition. The common form must therefore be exact where shared recognition matters, practitioner-first in its opening, and explicitly limited to framework editions.

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
| Form and carrier separation | One form may be borne by several carriers, and one outer carrier may expose several products, without merging their identities. |
| Accessibility and translation | Predictable headings and navigation aid many readers and tools, while one English label set cannot silently stand in for every language or access need. |

### E.11.PFP:4 - Solution

Apply one common reader-facing publication form to one FPF, DPF, or LPF edition. The profile is the reusable rule for that form. It is not the form itself, the presentation carrier that bears the form, the edition expressed by it, or the publication occurrence that makes the edition available.

#### E.11.PFP:4.1 - Preserve the compact product opening

For an all-in-one Markdown publication, preserve the product-declared compact opening and use this H1 route:

1. `# <product-declared publication title>`;
2. `# Table of Contents`;
3. the exact product-declared Readme H1;
4. the exact product-declared Preface H1;
5. the pattern bodies or pattern collection in the order selected by that edition; and
6. reference and maintenance material under headings declared by the product pattern.

The title and Readme H1 are separate product declarations. A checker receives both exact strings; it does not derive the Readme H1 by concatenating `Readme` to a longer carrier title. The common profile does not insert a metadata block, edition record, warning, or other lines into a compact predecessor opening merely to make products look alike. A product-specific builder may pin a compact front shape, including the line at which the ToC begins, when that shape protects an established reader entry.

Between the title and ToC, retain only the shortest public cues already justified by product use. An exact edition designation or locator belongs there only when its possible values change the reader's next use, reliance, return, language, dependency, or access choice. When such a cue is present, project it from one product-owned edition or relation record; do not maintain a second editable copy. Add authorship, credit, date, dependency, language, access, or a product-declared maintenance status, support window, or currentness window only under the same next-working-move test. A date is a cue, not edition identity, and a visible status or window is not evidence of acceptance, currentness, maintenance, availability, access, or authorization.

When readers copy, adapt, translate or redistribute a framework publication, its copyright-license notice tells them what permission the rights holder grants. Identify the covered material, rights holder and chosen license, and make the license text reachable from a standalone copy. Project a compact notice from the product's chosen licensing terms; retain applicable attribution and mark any third-party or differently licensed material. The author of an independently created DPF or LPF chooses its license. Where copyright permission is needed, reuse of another framework's protected expression is governed by that material's terms; applicable copyright exceptions remain available. Adopting its methods or publication form does not impose that framework's license on the new work.

Reader front matter extends from the opening title through the Readme and Preface up to the first pattern-body collection H1. It must not contain campaign keys; candidate, review, or result identifiers; local disk or repository paths; source or candidate digests; Git commits or blobs; generated comments; build commands; machine warnings; or "do not edit" instructions. Detailed edition, provenance, rebuildability, and maintenance records remain adjacent maintainer evidence or product-declared reference-tail material unless a separately selected public use justifies a reader-facing projection.

#### E.11.PFP:4.2 - Put public units into the established Table of Contents

Immediately after the single `# Table of Contents` H1, continue the product's established ToC grammar. Represent the exact Readme and Preface before the logical pattern index using the same kind of labelled segment and rows already used for non-pattern units in that product. When an established ToC already represents Preface and pattern groups, add Readme there; do not invent a generic `Publication route`, a second mini-menu, or a new table shape. A non-pattern publication unit receives no fabricated PatternID. Its product-declared entry remains mechanically recognizable and, when the carrier supports links, resolves to the exact unit.

Place the one authoritative logical pattern index after those public-unit entries. It may be one table or several ordered, uniquely labelled Part or placement segments. Every authoritative segment uses:

```text
| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
```

Across all segments, every pattern body has exactly one row, every row resolves to exactly one body, and no PatternID appears twice. A Part label groups rows for navigation; it is not a pattern row, a semantic parent, or another index.

PatternID, title, Part, and `§` position remain separate even when one row displays them together. PatternID supplies the stable public address within the named framework; the title explains the pattern; Part and `§` show where the current edition places it. Within each Part, the ToC rows and pattern bodies follow the same order. That order need not ascend by PatternID, and moving or retitling a pattern does not by itself change its PatternID.

When the surrounding text does not already identify the framework, name the framework together with the PatternID. To select the body published in one edition, also name that framework edition. For a DPF, `E.4.DPF` supplies the choice of reference code and local locator, and the continuity decision; this profile only makes the selected distinctions visible in the publication.

Reserve `Support index — <lookup job>` for a secondary pattern lookup. Its exact header is:

```text
| PatternID | Pattern title | Lookup use |
```

Ordinary relation, source-return, maintenance, and reference tables may cite PatternIDs under truthful headings and other complete headers. Do not infer that they are indexes from their cell values. Reject a second `# Table of Contents`, a `Pattern Index` heading for the same job, an authoritative header outside the authoritative ToC region, or a support heading and header that do not occur together. Public-unit entries are navigation inside the one ToC, not another pattern catalogue.

#### E.11.PFP:4.3 - Keep one practical-entry set and two visible forms

Start the Readme body with `## Practical entries`. The product maintains one declaration for every selectable example and assigns each key exactly one public form: ordinary practical entry or Practical-Use Card. Each declared key occurs once, at H3 for an ordinary entry or at H4 for a card. A compact locator may precede or follow these examples, but it is a finding aid rather than another editable entry set.

The Readme says plainly that its entries are selected examples, not a catalogue or coverage boundary. It tells the reader to bring the actual question and to use the product's index, direct patterns, or another finding aid when no example fits. Tell readers that they can ask an assisting agent for explanations and comments in ordinary language, without the framework's specialist vocabulary. For example: “Explain this and give me your comments in ordinary language, without framework jargon.” Clear wording is the default under `F.19`; the request helps the assistant adapt its wording to the reader.

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

<plain statement that these are selected examples of extended cross-pattern use, not a catalogue or prescribed workflow>

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

`### Practical-Use Cards` is a group inside the one `Practical entries` set, not another front door or selectable key. Omit the group when the product selects no cards. The card's canonical structural field is `Mantra`; its value begins directly with the repeatable wording and needs no `Local`/`Long` prefix. A local reminder for one direct pattern or bounded result may remain in that pattern, an ordinary entry, or other teaching material, but it does not by itself select the richer card form. `E.11` owns this content decision.

Every selectable ordinary entry and card shares one product-wide semantic-key namespace. The product declaration assigns each key one form, so a key cannot occur as both H3 and H4. An H5 expansion repeats its enclosing card key only to attach optional explanation; it is not another selectable occurrence. A card has zero or one expansion. Its compact portion ends after `Stop or return`; the expansion ends at the next H4-or-higher heading or the end of the group. The expansion may explain branch choices, examples, or exact result support, but cannot contain another H4 card or H5 expansion.

The product-language application declares one deterministic reading-burden measure and two maxima: one for the mantra and one for the complete compact card. The measure must suit the publication language; whitespace counting is suitable only where it meaningfully measures reading burden. The maxima protect scanability and recall. They are not targets, proof of reader value, a fixed card count, or authority to delete a choice-changing distinction. Content that a compact card cannot carry truthfully returns to the direct patterns or, only when first choice needs it, the same-key expansion.

Applying this grammar does not select a card, prove that the examples cover the product, or show that every cited pattern is needed in a particular case. `E.11` defines the direct-entry/card comparison, cross-pattern mnemonic-gain test, and non-exhaustive discoverability purpose. The product-specific E.4 pattern declares its selected example keys, forms, reading-burden measure, and two limits. A validator consumes those values and checks structure; it does not decide content value.

Use `First useful result or blocker` for this field in new entries. In existing publications, `First useful result or honest blocker` identifies the same field, with the same value and position; including both labels in one entry repeats the field.

This profile keeps structural field keys in canonical English. A translation may translate surrounding prose and values and may add a human-readable gloss, but it does not silently replace or reorder the field keys. A translated structural-key profile needs a separately selected recovery and checking rule. Test translated and low-tool publications with actual readers and navigation tools rather than treating English parser success as accessibility evidence.

#### E.11.PFP:4.4 - Keep support units and adjacent products distinct

A Readme, Preface, ToC, pattern-body collection, whole-framework account, relation or edition note, and refresh route may be publication units of one framework product when they serve its declared use and edition boundary. Place each unit where its readers can find and use it. A separate file is a carrier choice.

Use `E.4:4.1` to decide an adjacent product boundary from the useful result and its intended use. People may need to use, cite, or change a result as an identified whole, whether it appears inside a collection or through a separate carrier. State its identity, edition or current state, users, use, content boundary, and access route to the extent needed for that use. An established maintainer or maintenance commitment is not a prerequisite; record maintenance and refresh conditions when they are established and change reliance or use.

Examples include a source registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme. Their labels do not decide the boundary. Where an independent boundary is useful, point to the exact product edition or state. An annex may carry a declared snapshot or projection with a return to that product. Where ordinary framework use needs the material within the same boundary, include it as a named support publication unit.

One outer presentation carrier may expose several products. Each keeps its own identity, edition or state, form, access, and any separately established status or maintenance relation. Apply this profile to the FPF, DPF, or LPF constituents. A catalogue, evidence package, guide, service, programme, or other non-framework product uses the form selected for its own kind.

DRRs, build manifests, quality runs, digests, logs, and campaign state are process or maintainer evidence by default. A selected public use can justify a separate reader product or a public explanation drawn from that evidence. Publish durable use-changing reasons in the whole account or the relevant pattern; keep the dated decision, review, and release history in their records.


#### E.11.PFP:4.5 - Check syntax and product truth at the right boundary

The deterministic part of the form check handles recoverable syntax and projection agreement:

- the product-declared title and Readme H1, the compact opening, and absence of prohibited development or machine material from reader front matter;
- the required H1 sequence plus the product-declared body and reference tail;
- product-declared Readme and Preface entries in the established ToC grammar, before the logical pattern index, with no generic rival mini-menu;
- authoritative index segments, aggregate row/body bijection, duplicates, and reserved support-index grammar;
- the Readme's one practical-entry set; its explicit examples-not-coverage statement; the product's declaration of example keys and forms; exactly one H3 ordinary entry or H4 card per declared key; five ordered ordinary-entry fields; a non-empty card-group explanation; six ordered card fields; the shared reading-burden measure and mantra/card limits; and zero or one same-key H5 expansion with the declared boundary; and
- equality and source agreement of every optional public cue that is actually projected.

For Markdown grouping, one canonical bounded invocation runs the focused source-hazard guard and a parser-backed render together. It returns the rendered heading outline and block, list, table, code, and link structure for inspection while the candidate is already loaded. The agent does not discover a second renderer or reread the same file merely to close that form question. A clean mechanical result supports but does not replace the reader-visible judgement.

The product-specific check compares every visible cue with the exact edition or relation record from which it was projected and checks the product-specific body, reference tail, and any pinned compact-front shape. A syntax-valid but unresolved value fails there. A field absent from the public opening is not a form defect unless a selected reader use and product-specific rule require it.

A reader also follows the twelve content questions in section 4.7 to their public answers. A link or heading proves only that a target exists; reading establishes whether it answers the question at the claimed scale and preserves direct use. Reuse unchanged answers and current matching results. This content reading belongs to the selected authoring or publication question; the common form adds no separate release procedure.

Neither check decides framework scale from pattern count. Report `pattern_count = 1` as a diagnostic. Use E.4, E.4.PFAD, E.4.DPF.DA, E.11, E.21, and the applicable subject patterns to judge whether the result is a usable pattern language for its declared field and first use.

#### E.11.PFP:4.6 - Return the form result without overclaiming

Return the exact framework edition, edition-record source, carriers checked, form units found, public-cue agreement, logical-index result, practical-entry declaration and form result, product-specific tail checked, the public answers or unresolved content questions under section 4.7, and every mismatch or unresolved ref. Say separately whether the edition, carrier, publication occurrence, availability, currentness, or framework adequacy has an applicable result. Do not infer those claims or the truthfulness of card selection from form conformance.

#### E.11.PFP:4.7 - Explain the Methods at each selected scale

Use all twelve substantive E.8 functions as authoring questions for the whole framework and each substantive profile selected by its architecture. Answer them at the scope the publication promises. A framework may describe one composite Method through many patterns, several related Methods, or a repertoire used in different combinations. Where an exact MethodDescription claim matters, use `A.3.2` for the described Method and its description. The number of patterns, mantras, files, or description media does not settle that identity.

The whole account connects the answers that individual pattern bodies supply. Write the shared answer once and give exact returns to inherited content. At a narrower scope, state what changes in the situation, contribution, combination, evidence, result, or boundary. When an answer is missing, say which question remains open, which promised use it limits, and what remains usable.

| E.8 function | Question the whole or profile account answers |
| --- | --- |
| Problem frame | Who is doing what kind of work, under which conditions, and when would this language help? |
| Problem | Which inquiry, intended transformation, opportunity, or recurring difficulty needs an answer? What remains unresolved with the available approach? |
| Forces | Which competing requirements, resource limits, evidence conditions, or values shape the choice of Methods? |
| Solution | Which Methods and pattern contributions answer the problem? How do their results connect, which choices change the route, and where can the reader enter directly? |
| Archetypal Grounding | What actual or minimally viable worked case shows the language or profile producing a useful result, including a consequential branch or limit? |
| Bias-Annotation | Which assumptions, perspectives, exclusions, or access conditions affect whose work the language serves and where its claims travel? |
| Conformance Checklist | Which substantive questions establish correct use at this scope? Which answers can be inherited, and which changed conditions need their own judgement? |
| Common Anti-Patterns and How to Avoid Them | Which documented failures, text-invited misreadings, or consequential neighbouring cases need a practical correction? Apply the grounded-guard rule in E.8 and F.19. |
| Consequences | What practical gains, costs, residual limits, and subsequent moves follow from using this arrangement? |
| Architectural Rationale | Why does this organization of Methods serve the declared use? Which serious alternatives and trade-offs explain its boundaries, profiles, composition, and reuse, and when should a different choice be made? |
| SoTA-Echoing | Which current answers and source contributions shaped the Methods and their shared architecture? What was adopted, adapted, or rejected against a serious alternative, and what would reopen that choice? |
| Relations | Which specialization, bounded-use projection, composition, reuse, dependence, or publication-grouping relations actually hold, and where does each named contribution become useful? |

When a condition governs a whole combination of Methods, give it one public statement at the scope where that combination is used. State the quantities, assumptions, or other conditions needed to apply it, and return to that statement from affected profiles and patterns. Pairwise relations remain useful, but a condition on the whole set may require a different decision. A change to that condition reopens the combinations that rely on it; unchanged local contributions remain available.

Place the connected account in the product's existing Preface and declared reference or support units. Readme explains how to enter and use it. A large language may use a public Reference for explanations shared across many bodies; a small language may carry them in its Preface. Preserve enough rationale, source synthesis, alternatives, and worked detail for the intended reader to understand and adapt the language without its development intake or DRR. An exact inherited answer can satisfy a question; merely naming a pattern or listing source titles cannot supply missing explanation.

These are twelve content functions, not twelve compulsory new H1 sections. Each full pattern body retains its address and E.8 form. The outer Solution explains how to use the contributions together and returns to the bodies in the existing collection. It does not nest them under a new parent heading or require reading the whole account before a direct pattern use. If the public account uses the canonical function labels, prefer `Architectural Rationale`; `Rationale` remains the accepted alias defined by E.8.

There is no fixed number of generality scales. For example, a reader can move from FPF's general treatment of Methods to a Method Engineering DPF, a pattern-language construction profile, a narrower literature-based extension profile, and a pattern that recovers one candidate Method from source and Work evidence. Further useful scales can be introduced. Explain the relation at each move: a profile is a bounded-use projection; specialization carries inherited content plus a delta; composition connects Method contributions; reuse makes one contribution available in several settings; a chapter or Part groups publication text. A substantive narrowing must pass `E.8:4.1.3`'s same-situation usefulness comparison.

A pattern can participate in several profiles, and a profile can draw on several contributions. Describe this structure through the relations that hold. If a mathematical view is useful, apply `C.29`: select the elements and relation being modeled. A partial order needs its order properties; a lattice additionally needs the required bounds for every relevant pair. Multiple parentage or overlapping membership alone establishes neither. Keep that mathematical representation distinct from the Methods and their subject-side relations.

##### E.11.PFP:4.7.1 - Make a Preface section recognizable on its own

A reader entering through search, a quotation, a link or a retrieved excerpt may see a heading without its parents. Every heading inside the Preface therefore carries the framework's public reference code, the publication-unit key `Preface`, and its complete ordinal section path:

```text
