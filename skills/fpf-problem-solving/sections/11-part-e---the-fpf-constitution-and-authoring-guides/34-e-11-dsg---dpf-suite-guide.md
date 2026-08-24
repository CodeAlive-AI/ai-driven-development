## E.11.DSG - DPF Suite Guide

> **Type:** Specialization of E.11 (E)
> **Status:** Candidate
> **Normativity:** Normative for a maintained DPF suite guide and its public entries.

### E.11.DSG:1 - Problem frame

#### E.11.DSG:1.1 - Use this when

Use this pattern when a practitioner may need results from several DPFs, cannot yet tell which DPF applies, or needs a truthful stop because the current DPF ecosystem lacks part of the answer. The guide should let a cold reader begin from that working situation, recover the exact suite edition behind the guidance, and reach the needed DPF results or sources without treating co-listing as dependency or compatibility.

**First useful result.** Give one short answer that names the situation and returns each needed item in its real use: an available maintained result, a maintained MethodDescription, direct-source evidence, or a named unavailable result. Say what each contributes and end with an ordinary stop or return. Do not fill a missing result with another title.

**Primary `EntityOfConcern`.** One exact DPF suite guide edition: a non-framework `U.Episteme` that gives readers practical access to one DPF suite. Its continuity with earlier or later guide editions is established only by exact edition relations.

**What this buys.** A reader can act on a small answer and still return to the exact suite edition, member products, source facts, warnings, and stronger relations when those details change the action.

**Not this pattern when.** Use `E.4:4.2` and `E.4.PFAD` to decide suite architecture, membership, maintenance, and exposure. Use one DPF directly when its result is already clear. Use `E.11.PFP` only for an FPF, DPF, or LPF edition; a suite guide is not a framework edition. A publication that compares several suites has its own product boundary. Use the direct patterns for lookup Work, publication, availability, dependency, compatibility, evidence, authority, or currentness claims.

### E.11.DSG:2 - Problem

A list of DPFs does not tell a practitioner which combination answers one working question. A detailed guide can fail in the opposite direction: every entry repeats member states, warnings, sources, evidence, relations, and metadata until the first useful answer disappears.

Both failures invite stronger false claims. Readers may infer that listed DPFs form one framework, depend on each other, are compatible, are current, or are available. They may treat the guide as the Work of finding an answer, as evidence for the answer, or as the source of suite membership. A changed member edition can then make advice stale while the exact suite and guide editions remain unclear.

### E.11.DSG:3 - Forces

| Force | Pressure on the solution |
| --- | --- |
| Fast first use | A reader needs an answer before a catalogue of internal distinctions. |
| Exact return | The answer must still lead to the exact guide, suite, DPF, and source editions that support it. |
| Independent products | Suite, guide, member DPFs, adjacent evidence products, and carriers change under different commitments. |
| Honest combination | Several resources may be necessary, alternatives, or merely plausible; the guide must not overstate the relation. |
| Current action | Date, status, warning, availability, and source return matter only when they change what the reader should do. |
| Low record burden | Ordinary lookup may remain conversation; addressable answers are justified only by later review, reuse, publication, or reliance. |
| Language reach | Translation and language-specific maintenance may change the episteme or the product boundary. |

### E.11.DSG:4 - Solution

Write the practical answer first. State the recognizable situation and question, then say what each returned item actually is and what it contributes: an available maintained result of its own kind and supplying product, a maintained MethodDescription used to select or perform its Method, direct-source evidence for a named claim or decision, or a named unavailable result with its blocker and retry. End with the ordinary stop or return. Add exact identity, relation, evidence, warning, or reliance detail only when it changes the answer's truth, the reader's choice, or a named later use.

#### E.11.DSG:4.1 - Keep the guide line and each edition exact

**DPF suite guide** is Plain relation-defined wording for exact guide editions connected by accepted `EpistemeEditionRelation` occurrences and maintained for one reader use; it names no separate line object or root kind. A **DPF suite guide edition** is one exact `U.Episteme`, identified under `C.2.1` as:

```text
<claim content = J_g, EntityOfConcern = G, effective ReferenceScheme = R_g>
```

`G` is that exact guide edition. `J_g` states its intended readers and use, one exact suite-edition reference, selected problem-led entries, the exact resource and blocker claims those entries make, and only the source, warning, availability, and currentness claims that change those entries. `R_g` resolves the guide and suite editions, cited DPF products and editions, results, adjacent products, direct sources, and relation words used in the entries. A title, date, language tag, file, carrier, or publication occurrence cannot replace this identity.

The guide line continues only when a later edition actually uses an earlier edition as its source and preserves the intended readers, practical use, content-selection rule, and maintenance boundary. A new suite edition normally calls for a guide refresh, but does not create a new guide product. A fork, translation, retargeting, or independent reconstruction is not an edition successor merely because it keeps the title.

The guide product has its own capable maintaining System, accepted maintenance commitment, access, refresh route, and retirement boundary. Suite maintenance does not supply guide maintenance, and guide maintenance does not supply suite or member-DPF maintenance. Authorship, publication, a locator, or the word *maintained* establishes none of those commitments.

#### E.11.DSG:4.2 - Make the public minimum immediately useful

Show these guide-level facts where a reader can see them before choosing an entry:

- title and exact guide-edition locator;
- fixed edition date, intended readers, and practical use;
- actionable status or an honest non-current, superseded, or retired warning, together with its as-of basis;
- exact suite-edition locator and a working return to its authoritative source; and
- a table of contents that locates guide sections and member DPFs without implying order or stronger relations.

The edition date says when this edition was constituted. It is not a changing currentness claim or the date of every publication occurrence. Show the author when attribution, trust, contact, reliance, or source return changes what the reader should do. A byline does not identify the guide maintainer, suite maintainer, publisher, or authority.

Every problem-led entry keeps this small visible core:

```text
recognizable situation and practical question
first useful answer or honest blocker
available maintained result, maintained MethodDescription, direct-source evidence, or named unavailable result needed now, and what each contributes
ordinary stop or return
```

Add a member's state, field promise, detailed locator, applicability, evidence, availability, dependency, compatibility, warning, author, or claim-local reopen condition only when it changes the choice, truth, stop, return, or named reliance. Put a genuinely shared boundary once at guide or section level. Do not repeat empty fields, and do not copy `E.11.PFP`'s framework pattern-index grammar into this non-framework guide.

Frame each entry around a real working question and the decision or action the reader needs next. Let the route branch, overlap, or offer several honest stops when the situation does; do not force a false linear procedure. Keep the action-changing guidance in the entry and link to detailed reference material instead of repeating it. At guide level, state whose information need is served, how the guidance is presented and made available, and how it will be maintained; do not turn that information-development discipline into software-only scope or a mandatory documentation process.

#### E.11.DSG:4.3 - Keep lookup Work and the answer separate

A person, team, or assisting System may use one guide edition while doing lookup Work. The guide does not perform that Work. Ordinary use implies no Method, assignment, operation application, evidence, or authority. Identify those objects only when the current claim actually needs their direct rules.

An ordinary answer may remain readable conversation. Persist one only when review, reuse, publication, or later reliance needs an addressable result. First identify the exact practical-question episteme `Q`. Then identify the answer episteme `A` under `C.2.1` as `<claim content = J_a, EntityOfConcern = Q, effective ReferenceScheme = R_a>`. `J_a` states the answer, exact guide edition used, every returned resource or blocker, and what each does in this answer. `R_a` resolves those values and the use-specific relation words. This is an ordinary episteme, not a new lookup-result kind.

Say directly what each returned item does. For an available maintained result, name the result's actual kind, supplying product and edition or current state, and the receiving use. For a MethodDescription, name the described Method and how the reader uses the description; do not present its expected result as already obtained. For direct-source evidence, name the supported claim or decision and the source limits. For an unavailable result, name the blocker and retry condition. Recommendation, alternative, dependency, compatibility, and co-listing remain separate claims and create none of these stronger relations.

#### E.11.DSG:4.4 - Say “smallest” only when it can be tested

Call an answer the **smallest sufficient combination** only when the guide entry gives a recoverable candidate boundary, required result, and sufficiency rule, and removing any returned item makes that result insufficient. The boundary is the resources actually inspected through the entry and its direct source returns, not every publication that might exist.

When that test cannot be completed, return a bounded plausible combination and name the uncertainty or missing item. Do not disguise a convenient shortlist as a `JointUseSet`. Use `G.5` only when every exact returned resource is required for one named use and the current inclusion basis supports the all-member claim.

#### E.11.DSG:4.5 - Return to the suite and source when products change

The guide points to one exact suite edition; it does not decide or copy suite membership. Use the exposure chosen under `E.4:4.2`:

- for an independently exposed suite edition, provide its working publication or access route;
- for a guide projection, name the authoritative suite edition, captured membership and use, omissions or coarsening, as-of boundary, and working source return; or
- for a combined carrier, identify every exact constituent and its form or route while keeping identities, editions, maintenance commitments, access, and currentness separate.

A copied member table or locator without a working source return is orientation only. When a member DPF publishes a new edition, keep product membership only if the product identity, accepted inclusion basis, and exact basis pins remain valid. Then refresh only the guide advice, availability, compatibility, or warnings that actually changed. If the new edition defeats that basis or leaves it unresolved, warn readers and return to `E.4:4.2` and the applicable `E.4.PFAD` decision to decide whether to constitute a new suite edition, remove or restore a member or the suite, or retire it; the guide does not decide that architecture question. Temporary unavailability alone does not change membership, but it may require an action-changing warning or currentness update. If the suite loses its maintainer or edition-recovery route, or would fall below two qualifying member products, present no current-suite answer. Warn, return to the last exact edition, and route the architecture question to restoration or retirement.

#### E.11.DSG:4.6 - Distinguish expression, derivative, edition, and product

Another layout, carrier, rendering, or faithful expression of the same exact claims under the same scheme presents the same guide episteme. A translation or other derivative that changes claims or effective scheme is a distinct episteme with an exact source-to-use path under `C.2.P`; when meanings cross schemes, test the `F.9` Bridge and bounded use separately. It is not an edition successor from title or provenance alone.

A language-specific derivative stays within the same guide product only while readers and use, access, maintenance, warnings, refresh, and retirement share one boundary. If a language community needs an independently useful state or an independent boundary for any of those concerns, select another guide product. A multi-suite comparison publication also has another product boundary.

### E.11.DSG:5 - Archetypal Grounding

#### E.11.DSG:5.1 - Organization change and continuing operation

A manager asks how to reorganize a service without losing control of daily operation. A useful guide answer can be three sentences: name the organization-change result for the organizational change; name the operations result for continuing operation; stop when those two contributions answer the question, or return the missing result. Co-use establishes no dependency between the DPFs.

If the decision is safety-critical or legally constrained, add the exact source date, jurisdiction or applicability, authority boundary, warning, and reopen condition because those values change the answer and action. The simple and expanded answers use the same distinctions; they carry different justified detail.

#### E.11.DSG:5.2 - A non-engineering multilingual suite

A narrative-practice guide may combine results from independently maintained narrative, language-practice, and pedagogical DPFs for one lesson-planning question. Include all three only if removing any one makes that result insufficient under the stated rule. Otherwise present alternatives or a bounded plausible combination.

A Spanish translation of an English guide is a derivative episteme when its effective scheme changes. It remains in the same guide product only while its reader, access, maintenance, warning, refresh, and retirement boundary remains shared. Independent Spanish maintenance selects another guide product, not another edition merely because the title and member list remain recognizable.

#### E.11.DSG:5.3 - Lifecycle returns

| Situation | Reader-facing result |
| --- | --- |
| Only one relevant DPF product exists. | Use that DPF or call it a suite seed; present no suite edition. |
| A member DPF publishes a new edition. | If product identity, the accepted inclusion basis, and exact basis pins remain valid, keep membership and refresh only affected guide claims. If that basis is defeated or unresolved, warn and return to `E.4:4.2` and the applicable `E.4.PFAD` decision to decide whether to constitute a new suite edition, remove or restore a member or the suite, or retire it; the guide does not decide it. |
| A member is temporarily unavailable. | Keep membership and show the action-changing warning or return. |
| Removal would leave one or no members. | Present no singleton or empty edition; mark current suite use unavailable and return to restoration or retirement. |
| There is no identified capable System with an accepted maintenance commitment for the suite or guide. | Keep historical editions exact, but present no current maintained product. |
| A guide projection cannot return to the authoritative suite edition. | Label it orientation only; do not claim exact access, membership truth, availability, or currentness. |
| One carrier exposes several products. | Identify each constituent; infer no merged identity, edition, maintenance, or stronger relation. |
| An answer needs a result the ecosystem does not supply. | Name the product gap and return to a direct source, an existing-DPF change, a new-DPF question, or an explicit stop. |

### E.11.DSG:6 - Bias-Annotation

- **Catalogue bias.** A longer member list looks more complete. Judge the entry by whether it returns the right contributions or blocker for the current question.
- **Combination bias.** Co-use looks like dependency or compatibility. State those relations only after their exact edition-level predicates pass.
- **Freshness-display bias.** A current-looking page or recent date looks maintained. Require the direct maintenance, source-return, status, and currentness facts.
- **Precision-display bias.** Repeated fields and formal identities look safer. Keep the ordinary answer first and add only detail that changes truth or action.

### E.11.DSG:7 - Conformance Checklist

| ID | Passing condition |
| --- | --- |
| `CC-DSG.1` Situation first | A cold reader sees the working situation, practical question, useful answer or blocker, exact contributions, and stop or return before internal apparatus. |
| `CC-DSG.2` Exact guide and suite return | The guide edition is exact, and its public face points to one exact suite edition through a working source return. A locator or copied table is not treated as access. |
| `CC-DSG.3` Separate product boundaries | Guide, suite, member DPFs, adjacent products, lookup Work, answer, publication form, and carrier remain separate. Suite and guide maintenance commitments are independently recoverable. |
| `CC-DSG.4` Progressive detail | Date and actionable status are visible; author, evidence, relation, member-state, warning, and reopen detail appears only when it changes reader action, truth, or named reliance. |
| `CC-DSG.5` Answer discipline | Each returned item is classified and stated separately as an available maintained result of its actual kind and supplying product, a maintained MethodDescription reference, direct-source evidence, or a named unavailable result. Its readable contribution or blocker is explicit; recommendation, alternative, dependency, compatibility, and co-listing create none of those relations. |
| `CC-DSG.6` Smallest claim tested | “Smallest” has a candidate boundary, required result, sufficiency rule, and item-necessity test; otherwise the answer is called bounded and plausible. |
| `CC-DSG.7` Lifecycle honesty | A member-edition change keeps product membership only after product identity, the accepted inclusion basis, and exact basis pins remain valid; a defeated or unresolved basis returns to `E.4:4.2` and `E.4.PFAD`. Temporary unavailability, fewer-than-two transition, missing maintainer, missing source return, warning, and retirement follow their own branches. |
| `CC-DSG.8` Derivative boundary | Expression, translation or other derivative, an established edition-continuity relation, language-specific product, and carrier are distinguished by their actual identity, source, scheme, reader-use, and maintenance facts. |
| `CC-DSG.9` Plain-language whole passage | The complete changed passage can be read by an engineer or manager without reconstructing ontology notation; exact triples and relation terms appear only where they change identification or a stronger claim. |
| `CC-DSG.10` Current task-guide fit | Each entry starts from a real working question, supports necessary branches or honest stops, links out distracting reference detail, and reflects the intended readers' information need, presentation, availability, and maintenance. The guide records what was adopted, adapted, and rejected from current task-guide practice and when to recheck it. |

### E.11.DSG:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails | Repair |
| --- | --- | --- |
| DPF list as guide answer | Titles do not say whether an entry returns an actual maintained result, a MethodDescription, source evidence, or a missing result, nor what it contributes. | State the question, classify each return, name its direct contribution or blocker, and stop or return. |
| Guide as framework | A cross-DPF reader product receives a framework identity or pattern-index grammar. | Keep the guide a separate non-framework episteme product and apply `E.11.PFP` only to actual FPF, DPF, or LPF editions. |
| Guide performs lookup | Publication content is mistaken for dated Work or an operation application. | Name lookup Work, Method, performer, assignment, and bindings only when the direct claim needs them. |
| Membership from navigation | ToC order, a copied table, or co-listing is read as suite membership or a stronger relation. | Return to the exact suite edition; apply the direct predicate to every stronger claim. |
| Mandatory answer record | Every conversation produces a lookup-result object. | Keep ordinary answers in prose; persist only for named review, reuse, publication, or reliance. |
| “Smallest” by confidence | A convenient shortlist is presented as minimal. | Supply the candidate boundary and necessity test or say “bounded plausible combination.” |
| Translation as edition | Shared title or provenance hides changed claims or scheme. | Identify the derivative episteme and source-to-use path; test edition continuity independently. |
| Byline as maintenance or authority | Author attribution is made to carry responsibility, currentness, or authority. | Show attribution when useful and establish maintenance, publication, authority, and currentness separately. |

### E.11.DSG:9 - Consequences

**Benefits.** Readers can start with a short cross-DPF answer, distinguish an actual maintained result from a MethodDescription, source evidence, or a missing result, recover the exact products behind the answer, and see an honest product gap. Maintainers can refresh advice without silently changing membership, edition continuity, dependency, or compatibility.

**Costs.** The guide and suite need separate maintenance commitments and exact source-return paths. High-consequence answers may require more detail than ordinary lookups. Those costs appear only where the reader's action or later reliance needs them.

### E.11.DSG:10 - Rationale

A suite answers which independently maintained DPF products belong together for one use. A guide answers how a reader starts from a situation and uses exact resources. Keeping those products separate permits one guide to be repaired, translated, warned, or retired without rewriting suite membership, and permits a suite edition to change without pretending the old guide stayed current.

Progressive detail is not imprecision. The ordinary sentence carries the useful distinction first; exact episteme identity, edition continuity, source use, and stronger relation predicates remain available when they change the claim.

### E.11.DSG:11 - SoTA-Echoing

| Current line | Contribution used here | Boundary |
| --- | --- | --- |
| Current FPF `E.11` and `E.11.PUA` | Situation-first entry, first useful result, progressive explicitness, and ordinary stop or return. | A guide entry remains weaker than the direct pattern and does not become project Work or a universal workflow. |
| `ISO/IEC/IEEE 26514:2022, Design and development of information for users`, current published edition, `https://www.iso.org/standard/77451.html` | Establish users' information needs, choose presentation, prepare and make information available, and maintain its design through the life cycle. | **Adapt** those guide-level questions. **Reject** software-only scope, the full information-development process, and any inference that a filled template proves a useful guide entry. |
| Diátaxis, `How-to guides`, living practitioner documentation checked 2026-08-22, `https://diataxis.fr/how-to-guides/` | Start from a real-world goal; allow forks, overlap, and multiple entry or exit points; keep action central and link distracting reference detail. | **Adapt** problem-led routing and economy of detail. **Reject** a universal four-part documentation taxonomy for FPF, a forced linear route, and the claim that a guide performs the reader's Work. |
| Current FPF `E.8:4.1.3`, with `A.3.2`, `A.10`, `A.15.1`, `A.15.PROD`, and `C.2.1` at their direct uses | Distinguish an available maintained result, a maintained MethodDescription, direct-source evidence, and a named unavailable result; keep result production, description use, source use, and result availability separate. | **Adapt** the four readable guide returns in `E.11.DSG:1.1`, the Solution opening, `E.11.DSG:4.2–4.3`, `CC-DSG.5`, and the list-as-answer repair. **Reject** a universal resource kind, source availability as result production, and any inference from co-listing to suite membership or a stronger relation. Reopen this choice if those direct FPF boundaries change enough to alter what a guide can truthfully return. |
| Current FPF `E.4`, `C.2.1`, and `G.5` | Separate product boundary, exact episteme and edition identity, and all-members-for-one-use set discipline. | The guide defines none of those objects or predicates and cannot establish them by presentation. |
| Current FPF `C.2.P`, `F.9`, `E.17`, `E.24.PUB`, and `G.11` | Source-linked derivatives, semantic Bridges when needed, source-backed publication, availability, and currentness. | Shared title, visible carrier, locator, or recent date proves none of those claims. |
| Reviewed cross-domain guide situations | Organization/operation, legal, configuration, commercial, language, and contested-problem cases expose different justified depths. | They test the transferable form; they do not select concrete suite members, project answers, or domain authority. |

Reopen only the affected section when a direct FPF pattern changes the identity, relation, publication, source-return, progressive-entry, or currentness result used here; when a newer ISO/IEC/IEEE 26514 edition changes the relevant guidance; when the maintained Diátaxis guidance materially changes; or when cold-reader evidence shows that the short answer no longer supports truthful action. These external lines remain comparison aids, not the guide's ontology or a substitute for project evidence.

### E.11.DSG:12 - Relations

- **Specializes:** `E.11` for one maintained cross-DPF guide product; it does not specialize `E.11.PFP`.
- **Uses:** `E.4:4.2` and `E.4.PFAD` for suite architecture and decisions; `C.2.1` for guide, suite, and persisted-answer epistemes and exact edition continuity; and `G.5` only for an actual `JointUseSet` result.
- **Coordinates with:** `E.4.PFR` for exact edition dependency and compatibility; `C.2.P` and `F.9` for derivatives and cross-scheme use; `E.17`, `E.24.PUB`, and `G.11` for source return, publication, availability, and currentness; `E.11.PUA` and `E.11.PUR` for actual selected-pattern use and pattern-use coordination.
- **Constrains:** public DPF suite guide entries, guide-level metadata and warnings, source-return projections, persisted lookup answers, and lifecycle returns.

### E.11.DSG:End

