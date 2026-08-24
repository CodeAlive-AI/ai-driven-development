## E.11.PFP - Framework Publication Form Profile

> **Type:** Specialization of E.11
> **Status:** Candidate
> **Normativity:** Normative unless marked informative.

### E.11.PFP:1 - Problem frame

Use this pattern when one FPF, DPF, or LPF edition needs a public Markdown form that a cold reader can enter and a small deterministic checker can recognize. The framework's pattern set, product boundary, and edition values must already be selected for the publication being assembled or checked.

The first useful result is a form application that names the edition source, the public units that bear its projections, and each missing, reordered, duplicated, unresolved, or mismatched form element. A passing form check does not accept the edition, prove framework adequacy, identify a carrier, or establish a publication occurrence.

Do not use this pattern to decide whether one pattern set is a framework, whether a catalogue or guide is another product, or whether an edition is current or available. Use the E.4 family for the product and framework boundary, E.24.PUB for publication occurrence and carrier relations, and the applicable decision, quality, and currentness patterns for those claims.

### E.11.PFP:2 - Problem

FPF-family publications can expose the same useful material through different headings, edition labels, index layouts, and Readme cards. A familiar reader can compensate. A cold reader or parser cannot reliably tell which edition is present, which index is authoritative, whether several Part tables form one index, or whether a support table is a rival front door.

The opposite repair is also harmful. A rigid carrier template can put authorship, credits, dates, status, dependencies, build details, and maintainer records ahead of the reader's question whether or not those facts change the reader's choice. It can also force a catalogue, inquiry programme, guide, or other adjacent product to pretend that it is a framework edition. The common form must therefore be exact where shared recognition matters, practitioner-first in its opening, and explicitly limited to framework editions.

### E.11.PFP:3 - Forces

| Force | Tension |
| --- | --- |
| Cold-reader entry | Stable labels and order reduce search cost, but edition administration must not displace practical entry or the pattern bodies. |
| Exact edition return | Readers need a stable public designation and locator, while dates, filenames, statuses, and build digests must not become edition identity. |
| One logical index | FPF-family editions need one authoritative pattern index, while visible Part or placement groups remain useful. |
| Product variation | FPF, DPF, and LPF editions share a front form, but their body, reference tail, and choice-relevant public cues differ. |
| Product boundary | Support units may belong to one framework product; independently useful adjacent products need their own identity, form, access, and maintenance. |
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

Between the title and ToC, retain only the shortest public cues already justified by product use. An exact edition designation or locator belongs there only when its possible values change the reader's next use, reliance, return, language, dependency, or access choice. When such a cue is present, project it from one product-owned edition or relation record; do not maintain a second editable copy. Add authorship, credit, date, lifecycle, dependency, language, or access only under the same next-working-move test. A date is a cue, not edition identity, and a visible lifecycle word is not evidence of acceptance, currentness, maintenance, availability, access, or authorization.

Reader front matter extends from the opening title through the Readme and Preface up to the first pattern-body collection H1. It must not contain campaign keys; candidate, review, or result identifiers; local disk or repository paths; source or candidate digests; Git commits or blobs; generated comments; build commands; machine warnings; or "do not edit" instructions. Detailed edition, provenance, rebuildability, and maintenance records remain adjacent maintainer evidence or product-declared reference-tail material unless a separately selected public use justifies a reader-facing projection.

#### E.11.PFP:4.2 - Put public units into the established Table of Contents

Immediately after the single `# Table of Contents` H1, continue the product's established ToC grammar. Represent the exact Readme and Preface before the logical pattern index using the same kind of labelled segment and rows already used for non-pattern units in that product. When an established ToC already represents Preface and pattern groups, add Readme there; do not invent a generic `Publication route`, a second mini-menu, or a new table shape. A non-pattern publication unit receives no fabricated PatternID. Its product-declared entry remains mechanically recognizable and, when the carrier supports links, resolves to the exact unit.

Place the one authoritative logical pattern index after those public-unit entries. It may be one table or several ordered, uniquely labelled Part or placement segments. Every authoritative segment uses:

```text
| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
```

Across all segments, every pattern body has exactly one row, every row resolves to exactly one body, and no PatternID appears twice. A Part label groups rows for navigation; it is not a pattern row, a semantic parent, or another index.

Reserve `Support index — <lookup job>` for a secondary pattern lookup. Its exact header is:

```text
| PatternID | Pattern title | Lookup use |
```

Ordinary relation, source-return, maintenance, and reference tables may cite PatternIDs under truthful headings and other complete headers. Do not infer that they are indexes from their cell values. Reject a second `# Table of Contents`, a `Pattern Index` heading for the same job, an authoritative header outside the authoritative ToC region, or a support heading and header that do not occur together. Public-unit entries are navigation inside the one ToC, not another pattern catalogue.

#### E.11.PFP:4.3 - Give each practical entry five recognizable fields

Start the Readme body with `## Practical entries`. Each `###` entry uses these fields in order:

1. `Situation`;
2. `Question`;
3. `First useful result or honest blocker`;
4. `Start with`; and
5. `Stop or return`.

`Start with` resolves to one current PatternID or a named small route. `Stop or return` gives the ordinary non-use boundary, the sufficient first-result boundary, or the exact missing input. Keep richer branches, tests, and boundary notes when they help the reader; the five fields are a recognition layer, not a ceiling on useful content.

An independently published Readme starts with its exact product-declared Readme H1. If identifying the edition outside the surrounding carrier changes use or return, follow that H1 with the same shortest public cue and then emit `## Practical entries`; otherwise do not duplicate an edition or maintenance record merely to make the file look complete. The standalone Readme is another carrier of the same edition form, not another edition.

This profile keeps the structural keys in canonical English. A translation may translate surrounding prose and values and may add a human-readable gloss, but it does not silently replace or reorder the keys. A translated structural-key profile needs a separately selected recovery and checking rule. Test the translated and low-tool carrier with actual readers and navigation tools rather than treating English parser success as accessibility evidence.

#### E.11.PFP:4.4 - Keep support units and adjacent products distinct

A Readme, Preface, ToC, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route may be publication units of one framework product when they share its declared readers and use, edition boundary, access, maintainer, and change cadence. A unit does not become another product merely because it is outside the pattern set or stored in another file.

An adjacent result is a separate maintained product when people need to change, cite, use, or maintain it independently. Look for its own useful identity, version or current state, users and use, rule saying what content belongs, access route, maintenance commitment, refresh or retirement rule, or cross-framework reuse or reliance. Examples include a source registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme. This is an open list; those labels do not decide the boundary by themselves.

When the adjacent result is independently maintained, point from the framework to its exact edition or state. An annex may carry a declared snapshot or projection, but it returns to the authoritative product and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, include it as a named support publication unit of the framework product.

One outer presentation carrier may expose several products. The carrier stays neutral: each product keeps its own identity, edition or state, status, form, access, and maintenance boundary. Apply this profile only to FPF, DPF, or LPF constituents. A catalogue, evidence package, guide, service, programme, or other non-framework product uses the form selected for its own kind and receives no invented framework family, dependency field, or pattern index.

DRRs, build manifests, quality runs, digests, logs, and campaign state are process or maintainer evidence by default. They become reader products only after a separately selected public use gives them their own product boundary.

#### E.11.PFP:4.5 - Check syntax and product truth at the right boundary

The common form check handles only recoverable syntax and projection agreement:

- the product-declared title and Readme H1, the compact opening, and absence of prohibited development or machine material from reader front matter;
- the required H1 sequence plus the product-declared body and reference tail;
- product-declared Readme and Preface entries in the established ToC grammar, before the logical pattern index, with no generic rival mini-menu;
- authoritative index segments, aggregate row/body bijection, duplicates, and reserved support-index grammar;
- the Readme heading and five ordered fields; and
- equality and source agreement of every optional public cue that is actually projected.

For Markdown grouping, one canonical bounded invocation runs the focused source-hazard guard and a parser-backed render together. It returns the rendered heading outline and block, list, table, code, and link structure for inspection while the candidate is already loaded. The agent does not discover a second renderer or reread the same file merely to close that form question. A clean mechanical result supports but does not replace the reader-visible judgement.

The product-specific check compares every visible cue with the exact edition or relation record from which it was projected and checks the product-specific body, reference tail, and any pinned compact-front shape. A syntax-valid but unresolved value fails there. A field absent from the public opening is not a form defect unless a selected reader use and product-specific rule require it.

Neither check decides framework scale from pattern count. Report `pattern_count = 1` as a diagnostic. Use E.4, E.4.PFAD, E.4.DPF.DA, E.11, E.21, and the applicable subject patterns to judge whether the result is a usable pattern language for its declared field and first use.

#### E.11.PFP:4.6 - Return the form result without overclaiming

Return the exact framework edition, edition-record source, carriers checked, form units found, public-cue agreement, logical-index result, practical-entry result, product-specific tail checked, and every mismatch or unresolved ref. Say separately whether the edition, carrier, publication occurrence, availability, currentness, or framework adequacy has an applicable result. Do not infer those claims from form conformance.

### E.11.PFP:5 - Archetypal Grounding

**DPF, all-in-one and low-tool.** A horticulture DPF is distributed as one Markdown file and a printed copy. Both open with the public framework name and `Edition: Horticulture DPF 2.1`; the Markdown line links to a public edition page and the print line gives the same public address. The ToC, practical entries, Preface, four pattern bodies, coverage account, and refresh note follow. Authorship, source provenance, and change history remain reachable after the bodies. Readers can identify and return to the edition without crossing build records before their first working question.

**FPF, split carriers.** One website exposes an FPF edition through a front page and a separately downloadable Readme. The front page already identifies the edition, so its embedded Readme begins with practical entries. The standalone Readme repeats only the short edition line because it can circulate alone. Both return to the same public edition record; neither mints another edition or editable status copy.

**LPF with a choice-relevant cue.** An LPF supports two public language editions whose maintenance windows differ. The product-specific rule shows one short language-and-support cue after `Edition` because it changes which edition a practitioner should use. It does not copy the maintainer, build digest, source path, or complete dependency record into the opening.

**Adjacent product.** A separately maintained horticulture source registry has its own current state, users, selection rule, access route, and refresh commitment. The DPF points to that state; copying a snapshot into an annex does not create a second authoritative registry. One combined website may expose both, but the registry retains its catalogue form and receives no invented framework fields.

**Near miss.** A relation table has rows whose first cells are PatternIDs and titles, followed by relation and source-return columns. It remains a relation table. A checker that calls it another pattern index from those cell values is guessing semantics from data shape and fails this profile.

### E.11.PFP:6 - Bias-Annotation

**Scope:** Limited to the public Markdown form of an FPF, DPF, or LPF edition and faithful low-tool projections of that form. It is not a universal publication template and does not prescribe the form of an adjacent guide, catalogue, service, programme, evidence package, or maintainer record.

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Gov | A visible status or form pass is read as acceptance, authority, release, or currentness. | Keep those claims under their own decisions and relations; the form only exposes selected public cues. |
| Arch | A file, website, or combined package is treated as the product or edition, or every nearby result is forced into the framework form. | Name edition, publication form, carrier, occurrence, support unit, and adjacent product separately; apply this profile only to framework constituents. |
| Onto-Epist | A date, filename, digest, or editable front block becomes edition identity or evidence that a relation obtains. | Use one stable public designation and edition-record return; project only exact facts from their own records. |
| Prag | Administrative completeness displaces the reader's first question, or an optional cue appears without changing use. | Put the smallest useful edition cue first, then the ToC and practical entries; require a named reader decision for every extra front cue. |
| Did | Predictable labels become rigid English-only machinery, or terse navigation hides the patterns needed to act. | Keep recognizable headings and five entry fields, retain useful detail, and test translations, low-tool carriers, headings, labels, and navigation with their intended readers. |

### E.11.PFP:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFP.1 Scope truthful | The form expresses one named FPF, DPF, or LPF edition; no carrier or adjacent product is relabelled as that edition. |
| CC-PFP.2 Practitioner-first opening | The compact product-declared opening leads directly to the ToC; the common profile has not inserted a record or completeness block ahead of the reader's question. |
| CC-PFP.3 Edition return works when needed | When exact edition return changes use or reliance, the shortest public designation and locator resolve without repository knowledge; otherwise no unused return field is mandatory. |
| CC-PFP.4 Extra cues earn their place | Every cue before the ToC is projected from its exact record and changes a named reader decision or action; no common optional field is required merely for completeness. |
| CC-PFP.5 Development state excluded | Reader front matter contains no campaign or candidate identifier, local path, digest, Git identity, generated comment, build command, machine warning, or maintainer instruction. |
| CC-PFP.6 Entries and order recognizable | The title, compact cues, ToC, Readme and Preface entries in the product's established ToC grammar, Readme, Preface, pattern collection, and product-declared reference tail occur in the selected order; every declared target resolves where links are used. |
| CC-PFP.7 Logical index singular | One logical index may use several labelled segments, but aggregate row/body membership is bijective and PatternIDs are unique. |
| CC-PFP.8 Other tables remain truthful | Only the closed authoritative and support-index grammars are treated as indexes; relation and reference tables are not reclassified from cell values. |
| CC-PFP.9 Practical entry usable | Every entry gives the five fields in order and retains any richer content needed for the first useful result and stop boundary. |
| CC-PFP.10 Readme projection restrained | A standalone Readme repeats a short edition cue only when circulating without it would change use or return; it does not duplicate the edition or rebuildability record. |
| CC-PFP.11 Product boundary preserved | Framework support units share the declared framework boundary; independently useful adjacent products retain their own identity, form, access, and maintenance. |
| CC-PFP.12 Combined carrier neutral | Every constituent product keeps its own form and identity; E.11.PFP applies only to framework constituents. |
| CC-PFP.13 Claims remain separate | Form conformance is not reported as acceptance, adequacy, carrier identity, publication, availability, access, maintenance, or currentness. |
| CC-PFP.14 Scope examples survive | The rule remains usable for FPF, DPF, and LPF editions and for a low-tool or non-clickable carrier without introducing a second edition identity. |
| CC-PFP.15 Navigation remains usable | The ToC represents Readme and Preface in its established product-native grammar before the singular pattern index; headings and labels describe their purpose, and the integrated rendered-structure summary plus intended-reader inspection exposes grouping defects without a second full read. |

### E.11.PFP:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Complete record before entry | Author, assistance, date, lifecycle, dependency, provenance, or the whole edition record appears before the ToC merely because it exists. | Preserve the product's compact opening; project only cues whose possible values change a named reader move and keep the full record in maintainer evidence or the justified reference tail. |
| Development state as public identity | Candidate keys, local paths, digests, commits, blobs, generated comments, or machine warnings describe the publication to readers. | Keep them in builder or maintainer evidence; publish a stable designation and public return. |
| Date as edition identity | Two editions on one day become indistinguishable. | Use a stable public designation linked to the exact edition record; show a date only when it changes reader use. |
| Fresh navigation grammar | A generic mini-menu is inserted ahead of an established ToC, duplicating units and making one product unlike itself. | Extend the product's existing non-pattern ToC segment and make the checker recognize that exact grammar. |
| Flat-index compulsion | Visible Part grouping is removed merely to satisfy one-table code. | Check one logical index across consistently headed, uniquely labelled segments. |
| Index by cell guess | A relation or source-return table is rejected because it cites PatternIDs and titles. | Recognize only the closed authoritative and support-index grammars. |
| Readme as another edition | The standalone Readme mints its own designation or copies a full editable record. | Repeat only the shortest cue whose absence would change use or return when the Readme circulates independently; never duplicate the edition or rebuildability record. |
| Outside the pattern set means another product | A Preface, coverage account, or refresh note is split into a product with no independent use. | Keep it as a named support unit when it shares the framework boundary. |
| Shared use means one product | A cross-framework registry or service is absorbed into one DPF. | Treat shared use as a prompt to inspect the boundary; preserve an independent product when its own use and maintenance make that useful. |
| Combined carrier merges products | A framework and catalogue receive one identity and one framework index. | Keep the outer carrier neutral and each constituent in its own selected form. |
| Parser pass as accessibility | Canonical English labels parse, so translation, assistive navigation, low-tool return, and cold-reader use are assumed. | Test the actual carrier and reader route; repair headings, labels, links, and projections without weakening source return. |

### E.11.PFP:9 - Consequences

Readers retain each product's compact familiar opening and find Readme and Preface in the ToC grammar already used by that product, before the one authoritative pattern index. Optional public cues remain recoverable from one source when they change use, while development and rebuildability records stay out of reader front matter. Builders gain checks that fail on missing public-unit entries, structural, projection, and development-state drift without guessing table meaning, inventing a rival navigation block, or forcing a second renderer-discovery pass.

### E.11.PFP:10 - Rationale

The shared rule fixes only the recognition points whose reuse pays across FPF, DPF, and LPF: a compact product-declared opening, Readme and Preface represented in the established ToC grammar, one logical pattern index, practical-entry fields, truthful product boundaries, and recognizable major units. It leaves titles, optional public cues, the exact product-native ToC segment, front line shape, and reference tails with the product-specific rule because their value depends on the reader's choice. Limiting the profile this way preserves deterministic checking without turning one candidate's navigation experiment or maintenance record into a universal reader experience.

### E.11.PFP:11 - SoTA-Echoing

| Current source or practice | Qualification and by-value decision | Contribution adopted here | Shortcut rejected and receiving loci |
| --- | --- | --- | --- |
| [ISO/IEC/IEEE 26514:2022, *Design and development of information for users*](https://www.iso.org/standard/77451.html) | Current published international standard checked 2026-08-22. **Adapt:** retain its user-needs, audience/task, presentation, packaging, version/change-control, and maintenance concerns without importing a universal document template. | Start from reader need; keep public information identifiable, presentable in different media, and maintainable across editions. | A complete maintainer record is not automatically the best front. Applied in 4.1, 4.3, 4.5, Grounding, and CC-PFP.2-5/10/14. |
| [Diátaxis](https://diataxis.fr/start-here/) and its [how-to guidance](https://diataxis.fr/how-to-guides/) | Current maintained documentation architecture checked 2026-08-22. **Adapt:** organize entry around what the reader is trying to do and keep action-guiding routes concrete; do not force its four document modes into FPF product kinds. | Practical entries lead from situation and question to a first useful result, direct route, and stop or return; optional detail earns its place by use. | A metadata-first home page and one rigid document taxonomy are both rejected. Applied in 4.1, 4.3, Grounding, CC-PFP.2/4/9, and Consequences. |
| [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/), especially multiple ways, headings and labels, and consistent navigation | Current W3C Recommendation checked 2026-08-22. **Adopt:** descriptive headings, consistent navigation, and more than one usable finding route where the carrier permits it. **Adapt:** the Markdown profile remains one source form, not a claim of full WCAG conformance. | Stable major headings, one authoritative ToC, practical entries, truthful labels, and explicit testing of translated and low-tool projections. | Parser success or canonical English alone is not accessibility. Applied in 4.2-4.5, Bias-Did, CC-PFP.7-10/14-15, and the accessibility anti-pattern. |
| Current FPF `E.11`, `E.17`, and `E.24.PUB` | Current local pattern-language architecture. **Adopt:** working-question entry, bounded publication projection with source return, and separation of edition, form, carrier, occurrence, access, and use. | The shared form preserves practical entry and exact edition return while product-specific patterns keep body, reference, publication, and access decisions. | A front door does not replace pattern bodies, and a form pass does not establish product, publication, or currentness claims. Applied throughout 1, 4.3-4.6, Grounding, and Relations. |

Reopen this source use when a newer applicable standard or repeated FPF-family use shows that the profile no longer supports cold entry, edition return, segmented navigation, translation, accessibility, or product separation without avoidable reader or maintainer burden.

### E.11.PFP:12 - Relations

- **Specializes:** `E.11` for the common reader-facing form of one FPF, DPF, or LPF edition; `E.11` retains practical-use discoverability and first-result routing.
- **Coordinates with:** `E.4`, `E.4.FPF`, and `E.4.DPF` for framework/product boundary, product-specific publication units, optional reader cues, body order, and carrier assembly.
- **Coordinates with:** `E.24.PUB` for publication occurrence, selected edition, form expression, carrier bearing, audience, bounded use, availability, and access; and `E.17` for bounded publication projections and source return.
- **Coordinates with:** `E.4.PFR` for exact dependency and edition relations, `G.11` for currentness and refresh, `E.4.DPF.DA` and `E.2.DA` for applicable package or whole-FPF adequacy, and `E.21` for pattern quality.
- **Does not replace:** product-specific builders or validators, the edition record, `FPFEditionRebuildabilityRecord`, `FrameworkPackageManifest`, an architecture decision, or a public product boundary.

### E.11.PFP:End

