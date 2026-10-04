## F.1 - Find and Select Sources for a Current Question

<a id="f1---question-relative-source-selection"></a>

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

> **One-sentence summary.** Find inspectable material for the current question, expose search and access limits, and select the smallest sufficient source set when its claims, rivals or counterexamples need a justified basis.

**Historical titles (informative).** *Domain-Family Landscape Survey*; *Question-Relative Source Selection*.
**Aliases (informative).** *Source cut*; *question-relative source selection*; *question-led source finding*.

### F.1:1 - Problem frame

**Use this when.** A current question needs source material, but you do not yet know where to find it, which words its sources use, or whether the available access reaches the needed passage. Use :4.4 to obtain inspectable candidate material with its consequential search and access limits. A catalogue reference, familiar phrase or ranked fragment may be a useful lead while still omitting the condition that changes the answer.

When candidate sources are already inspectable and more than one may change the answer, use :4.2 to justify the smallest sufficient source cut. Ask how each exact source and edition can change the answer or its limits, and retain the distinct contributions that matter. Finding and source selection can be used separately: a sufficient known source can answer directly, and a justified cut can start without a new search.

The source-selection branch returns one `SourceCutNote : U.Episteme`. Before treating the note as that episteme, identify the receiving question as one exact project entity. That question is the note's `EntityOfConcern`; the intended use remains in the ClaimGraph rather than becoming a second subject. Name the effective `U.ReferenceScheme` explicitly: it must resolve the question, the cited source-edition designators, and the answer-changing role claims. The ClaimGraph also names deliberate exclusions, known limits or source gaps, and reopen conditions. If the question or scheme is still missing, keep an ordinary working note and return that missing value instead of claiming a C.2.1 episteme. A one-screen source note may represent the same episteme when it carries the same claims; its compact form neither admits a source nor contains its local meaning.

**What this buys.** You can reach material under unfamiliar wording, explain what the available search could have missed, and return passages whose contribution to the current question can be inspected. Later term recovery, comparison, synthesis or direct source use can then begin from a reason for each source rather than from one influential canon, a bibliography quota, a domain label or an opaque search score.

**Not this pattern when.** If one already identified source closes the question, use its claim directly or use `F.0.1` for one source-local meaning. Use `F.9` for an actual relation between recovered local senses and `F.0.2` for a bounded conceptual comparison or synthesis. Use `G.2` for a broader refreshable SoTA pack. When the receiving work requires an exhaustive, protocol-defined, or appraisal-bearing evidence review, use its domain method; F.1 does not replace that search, appraisal, or reporting discipline. Building or maintaining an access system is a separate engineering question; this pattern uses the finding means already available.

**Primary results.** Finding returns inspectable candidate material, why it matters, and consequential search or access limits; it may instead return the precise missing material. A passage with a short explanation can suffice; no special record is required. Source selection returns one question-relative `SourceCutNote`. Neither result establishes source truth, applicability, completeness, reliance or assurance.

### F.1:2 - Problem

Without question-led finding and a justified source cut where one is needed:

1. **Word drift.** Familiar terms silently change meaning across sources and editions.
2. **Canon lock.** One influential standard is mistaken for the whole answer.
3. **Recency blur.** An old edition remains load-bearing merely because it was used first.
4. **Category bleed.** Designed structures, performed occurrences, system roles, statuses, permissions, and measurements are merged before their source claims are inspected.
5. **Source bloat.** A large reading list hides which sources can actually change the current answer.
6. **Search substitution.** Rank, similarity, or family membership is mistaken for relevance, truth, or completeness.
7. **Vocabulary lock.** The question's first wording misses a source that uses another name or explains the needed relation differently.
8. **Access blur.** A title, excerpt or failed search over one subset is treated as if the full source had been inspected.

### F.1:3 - Forces

| Force | Tension |
| --- | --- |
| Relevance vs finiteness | The cut must expose answer-changing rivals and limits while remaining small enough to inspect together. |
| Local fidelity vs cross-source use | Each source keeps its own claims and meanings while later work may compare them. |
| Recency vs continuity | New editions matter, but only changed relied premises should reopen the result. |
| Efficient search vs human judgment | Search aids may prioritize candidates but cannot decide their role in the answer. |
| Compact memory vs source analysis | A short result should keep the decision recoverable without becoming a second literature review. |
| Wider discovery vs question fidelity | Query variants may omit a word to reach more material, while the original conditions still govern what can answer the question. |
| Available access vs coverage | A cheap route may reach enough material; a consequential blind spot may justify another route or an honest access gap. |

<a id="f14---solution--select-by-answer-changing-role"></a>

### F.1:4 - Solution — find inspectable material and select by answer-changing role

#### F.1:4.1 - Minimal vocabulary

- **Exact source and edition.** The identified publication, canon, corpus, practice source, or other claim-bearing basis being considered.
- **Receiving question and use.** What needs an answer and what that answer will serve. A plain concern can start finding. For source selection, independently identify the exact question that the selection claims concern; it is the `SourceCutNote`'s EntityOfConcern, while the intended use remains claim content.
- **Candidate material.** A passage or other source content that can be inspected for a contribution to the question. A source address without accessible content remains a lead.
- **Query variant.** Words tried to reach material for the same original question; any added interpretation is a hypothesis, not a replacement question.
- **Answer-changing role.** The inspected claim, limit, rival explanation, counterexample, transfer condition, material non-fit, or other stated contribution by which a source can change the answer.
- **Source cut.** The finite set of sources retained for that question and use.
- **`SourceCutNote`.** One C.2.1 episteme identified by its source-selection ClaimGraph, the exact receiving question as EntityOfConcern, and the named effective ReferenceScheme under which that question, source editions, and role claims are read.
- **Domain family.** An informative discovery label, such as workflow, provenance, services, sensing, types, or control. It carries no semantics and cannot admit, merge, or replace a source.
- **Local search policy.** An optional named way to prioritize candidate inspection using search terms, descriptors, citations, embeddings, distances, active learning, or portfolio readings. Its output is attention guidance, not a source-selection verdict.

Source selection, source identity, source-local meaning, source truth, source adequacy, cross-source relation, synthesis, reliance, and assurance are separate questions.

#### F.1:4.2 - Source-selection method

**Step 1 — State the receiving question and use.**
Say what answer is needed, what later use it serves, and which source difference could change that answer.

**Step 2 — Name candidate sources by exact edition.**
Use identified sources whose relevant claims can be inspected. A discipline or domain-family label may help discovery but is not a source.

**Step 3 — Inspect the answer-changing role of each candidate.**
Ask what claim or limit from that edition can change the answer. If that role depends on a disputed expression, pause selection only long enough to use F.0.1's ordinary branch: name the exact source, edition, and passage, and say in plain language what the expression means there. Then return to source selection. Do not run this branch for every candidate. Look deliberately for intended-use contributions, rival explanations, action-changing counterexamples, transfer limits, and material non-fit. One source may serve several roles.

**Step 4 — Take the smallest sufficient cut.**
Retain sources that cover distinct answer-changing roles. Exclude a candidate when no inspected claim from it changes the stated question or use. Do not optimize for a fixed count, diversity score, canonical status, or exhaustive appearance.

**Step 5 — Record exclusions, gaps, limits, and reopen conditions.**
Name deliberate exclusions and why they do not change this answer. State a load-bearing source gap rather than treating an unavailable source as irrelevant. Say which question, use, edition, rival, counterexample, or transfer-boundary change would reopen the cut.

**Step 6 — Return one `SourceCutNote`.**
Identify it under C.2.1 by three values: the ClaimGraph produced by Steps 1–5, the exact receiving question from Step 1 as EntityOfConcern, and the named effective ReferenceScheme that resolves the question, cited editions, and role claims. Keep the intended use in the ClaimGraph. Use a one-screen representation when it helps the receiver hold the result in view. Detailed source analysis stays with the receiving comparison, synthesis, or evidence method.
**Step 7 — Recover only the meanings the work needs.**
After the cut is stable, create an F.17 local-sense cell only for a retained expression that later reuse, a claim, a named receiver, or an actual relation needs. Do not postpone a meaning needed by Step 3 to this stage, and do not manufacture a cell for every retained source.

##### F.1:4.2.1 - When the cut will support a SoTA claim

A source cut used to claim SoTA has a stricter role test because source relevance and source currentness do not establish the best-known answer. `E.8:11` owns the FPF definition of SoTA and the meanings of its comparison roles; F.1 neither redefines SoTA nor selects the winning line. For each retained source, record one of those roles in plain wording: **best-known-line candidate**, **serious current rival**, **failure or counterexample evidence**, **official or popular comparator**, **lineage only**, or **identity/currentness only**.

The first three roles can supply answer-changing evidence. An official or popular comparator may stay only when its named defect is necessary to the comparison. Roles are assigned by contribution, not institution: an official standard or widely used practice may instead be a best-known-line candidate when its substantive answer wins against the serious alternatives. Officiality, prevalence, maintenance, citation, freshness, or academic praise contributes nothing to that rank. An official catalogue, publisher page, or registry entry may verify the source's identity, edition, publication date, or maintenance state; it establishes neither truth, adequacy, nor SoTA rank.

For a SoTA claim, disable the generic one-source cheap exit unless the one source is itself a current critical synthesis that compares the serious alternatives for the named question and the author can state why no known action-changing rival or counterexample remains hidden. Otherwise retain the necessary rival and failure evidence or return an unresolved source gap. Do not manufacture confidence from a one-source cut.

An original FPF or DPF answer is compared under E.8:11 on the same basis as a source-derived answer. Select the sources needed to expose serious alternatives, their limits and relevant failure evidence; do not require a prior external publication containing the authored answer. The original answer still needs that comparison, so its authorship does not restore the generic one-source exit.

The `SourceCutNote` records the `E.8:11` roles and the missing comparison, but it does not itself select the best-known line. Use `F.0.2` when an actual cross-source synthesis claim is required. Use `G.2` only when a broader refreshable evidence pack is justified; a bounded comparison does not require that apparatus by default.


#### F.1:4.3 - The `SourceCutNote`

The note's exact EntityOfConcern is the independently identified receiving question from Step 1. It is not the note, its file or one-screen form, the retained-source list, or a question-and-use bundle. The intended use remains part of what the note claims. Name the effective ReferenceScheme explicitly and make sure it resolves the question, every exact source-edition reference, and every answer-changing role statement. If either the question or scheme is unresolved, return that gap and keep the text as an ordinary working note.

Its ClaimGraph states:

- the receiving question and intended use;
- every retained source and exact edition;
- the answer-changing role of each retained source;
- for a SoTA-supporting cut, each retained source's plain role and any unresolved rival, counterexample, or synthesis gap;
- deliberate exclusions and their reasons;
- known limits and load-bearing source gaps;
- the distinction between designed and performed material when it affects the answer; and
- the conditions that reopen the cut.

A one-screen source note is a compact representation of the same episteme when it carries the same claims. If its ClaimGraph differs, it is another C.2.1 episteme rather than a second F.1 result kind. A short form does not establish source truth, adequacy, or local meaning.

<a id="f144---optional-search-assistance"></a>

#### F.1:4.4 - Find candidate material when sources or terminology are uncertain

Use this branch when the current question lacks material that can be inspected: its source, wording, location or available finding route is uncertain. Begin with the means you have. A paper catalogue, available files, a source's references, a colleague or a search service can supply a route. An already identified sufficient source can be used directly.

##### F.1:4.4.1 - Keep the question and bound the available material

Keep the original question, what an answer would change, and any unresolved condition. A plain concern can start finding; it need not yet have the independent identity required for a SourceCutNote. Separate that concern from the words tried in a search. If you add an interpretation, mark it as a hypothesis to test against the material.

Source reading can change what you understand the question to be. Keep the original receiving concern and explain what the new material changes: a different needed result, a mistaken premise or an additional condition. Use B.5.PI:4.4 when that inquiry needs reconstruction, then return with the revised question. A query variant tries another way to find material for a question; a revised question can require different material.

Establish what can actually be inspected: which publications, collections or archive portions, which editions, and what access they provide. Full bodies, titles, excerpts and an index have different reach. Record a consequential missing collection or unavailable original. This boundary makes a later no-hit result interpretable and prevents an available subset from silently standing for the whole repertoire.

##### F.1:4.4.2 - Choose an attainable first route

Choose a route that could reach the needed material at acceptable effort. Use a known address or a cheap direct text lookup when it can answer the question. When terminology is uncertain, use a likely contents area, an analogous case or an inspected passage to obtain words the source itself uses.

| Available starting point | First route and likely blind spot |
| --- | --- |
| A cited source or passage address | Obtain that edition and open the passage. A reference alone may expose no body, and a later edition may have changed the relied condition. |
| Words likely to occur in accessible text | Search the bodies for the object, action, result or distinguishing condition. A single phrase may miss another language, earlier name or differently worded explanation. |
| Unfamiliar terminology but a recognizable concern | Browse a relevant contents area or example, then use the source's wording for further lookup. A published classification can place the contribution in another area. |
| A relevant inspected source | Follow a reference or neighbouring passage that could supply the missing contribution, rival or limit. Its references can favour its own lineage. |
| A search, assistant or summarized view | Use returned candidates to choose what to inspect. Its declared fields or representation can omit body conditions; a score cannot establish their absence. |

These are alternative starting points. Choose an additional route only when a consequential gap remains and that route could recover material the first route could not reach. For example, a body search can bypass a title-only index; an older term can bypass a current-name catalogue; a referenced original can expose a condition missing from an excerpt. Repeating the same limited representation with another tool does not repair that limit.

Keep a material search aid's policy recoverable in ordinary wording: searched corpus and editions, route, relevant filter or model, and how its output is interpreted. Retain a score's scale or threshold when it changes what is inspected. No special record is required for an ordinary lookup.

##### F.1:4.4.3 - Try question-preserving variants and repair a blind spot

Form variants from the concern: the object being worked on, needed action or result, failure, and condition that changes the answer. Start with the parts likely to occur in the available text. Trying every detail as one phrase can miss a passage that explains the needed relation in different words.

Keep the original question alongside each consequential variant. Terms suggested by a colleague, an assistant or a promising source remain search hypotheses until their local use is inspected. If a variant drops a constraint to broaden discovery, restore that constraint while reading candidates. Broadening the query permits finding more material; it does not broaden what would answer the question.

After an unhelpful result, ask what that route could have missed. Change the particular term, scope or access path responsible for the suspected omission. When no available route can inspect a load-bearing original, return that access gap rather than inventing its content. Add another route for a reason, not to satisfy a fixed number of searches.

##### F.1:4.4.4 - Inspect the source around the candidate

Open the candidate with its enclosing heading and the definitions, conditions, examples or dependencies needed to understand the passage. Say how its content could contribute to the current question. A useful candidate can supply a direct answer, an operation, a rival, a counterexample or a limit. Mere word similarity supplies none of those roles.

Compare the material obtained with the contributions the next use needs. New wording, another search route or a different document can still repeat the same contribution. When several aspects matter, identify the one still unsupported and why its absence could change the receiving answer; seek material for that gap. Several documents elaborating one aspect do not supply another. Keep an unresolved aspect visible when its source cannot be inspected. A brief statement of the remaining need suffices.

Check what was actually obtained. Distinguish an inspected body passage from a title or reference to an inaccessible original. An excerpt can be returned as inspected material with its missing context stated; it cannot supply an uninspected original's omitted conditions. Recover the source and edition as far as access permits, and retain an unresolved edition identity when it affects use. If a source-role judgement turns on a disputed term, use the ordinary F.0.1 source-local reading and return here or to :4.2.

For a candidate FPF Method, retrieve the relevant complete pattern and the conditions needed for its use through the available publication. Material finding supplies that text; E.11.PUR judges a proposed use and E.11.PUA guides application of a selected pattern. A promising fragment can be enough to continue finding while remaining insufficient to perform the Method.

##### F.1:4.4.5 - Return useful material, its limits and the next move

Return the inspected candidates with source/edition and passage locations, the reason each matters, and any missing condition or access limit. A passage with a short explanation can be enough. Keep inaccessible leads and uninspected candidates visibly separate from material already inspected. State the searched scope and consequential route limits when they affect what the receiver may conclude.

Choose the continuation from the receiving need:

- Use a sufficient identified source directly for the subject question. Finding creates no source-cut obligation.
- Use :4.2 when several inspected sources could change the answer and a justified source cut is needed. Source selection then returns its own SourceCutNote.
- Use the relevant subject method for truth, applicability, synthesis, reliance or assurance. When the inspected contributions still leave an obtaining way unexplained, C.39 develops that connection or returns its precise gap. For proposed FPF uses, continue with E.11.PUR only when such a judgement is current.
- Return the exact missing material or access condition when the next use cannot yet be supplied.

Stop finding when the next use has the material it needs, or no affordable available route could presently change that result. Judge another search by the missing contribution it could supply, not by the availability of more terms or documents. A limited search with no useful hit returns “no useful material found by these routes in this accessible scope”, with the remaining gap. It establishes no claim of universal absence or completeness.

Reopen the affected finding when the question, needed result, source edition or access changes. Reuse a passage whose contribution and conditions still hold. A renamed file or new edition number alone does not require repeating the whole search; a changed relied passage or newly accessible original can. If a search representation changes, check whether it now reaches or hides material needed by the question before changing the received result.

#### F.1:4.5 - Invariants


For finding, keep the original concern distinct from search variants, identify what was actually inspected, and return consequential access limits. A no-hit result is relative to the searched scope and routes. The following invariants govern the source cut when source selection is current:

1. Every retained source has an inspected answer-changing role for the stated question and use.
2. The cut is finite, inspectable, and revisable; no universal count establishes sufficiency.
3. Exact sources and editions remain recoverable.
4. Source-local meanings remain local; F.1 does not merge or relate them.
5. The result contains no F.9 relation, synthesis conclusion, truth verdict, reliance decision, or assurance claim.
6. Domain families and search readings guide discovery only.
7. Designed descriptions and performed occurrences stay distinct when that source difference matters.
8. A changed relied premise reopens the affected cut claims; an unrelated edition-number change does not.
9. One already identified sufficient source is the ordinary cheap exit; for a SoTA claim, the stricter critical-synthesis condition in `F.1:4.2.1` applies.
10. A protocol-defined evidence review continues to follow its domain method.

#### F.1:4.6 - Self-checks


For finding:

- **Question-preservation test.** Could a changed or omitted query term change what would answer the original question? Restore that condition when inspecting candidates.
- **Reach test.** What material could the available route actually inspect, and which consequential blind spot remains? Use a complementary route only if it could repair that gap.
- **Candidate-return test.** Can the receiver obtain the inspected passage, see why it matters and distinguish missing context or an unavailable original?
- **Stop test.** Does the next use already have sufficient material, or is its exact missing basis returned? Do not turn a scoped no-hit result into a claim of absence.

For source selection:

- **Answer-change test.** What can each retained source change in the answer or action? If nothing, exclude it or state the missing role.
- **Rival-and-limit test.** Is a known rival explanation, counterexample, or transfer limit still hidden? Add the source that makes it inspectable or return the source gap.
- **One-source test.** Does one already identified source close the ordinary question? If yes, stop without additional F.1 steps. If the cut will support a SoTA claim, take this exit only when that source is a current critical synthesis of the serious alternatives and no known action-changing rival or counterexample remains hidden.
- **SoTA-role test.** Has each retained source been classified under one of the comparison roles defined in `E.8:11`? If not, classify it there before using the cut for a SoTA claim; do not recreate the role meanings in F.1.
- **Rank test.** Did official status, popularity, maintenance state, date, or a catalogue check raise a source's SoTA role? Remove that inference; keep the check only as source identity/currentness evidence.
- **Gap test.** If the best-known line cannot be established, does the note return the missing rival, counterexample, or synthesis need as a source gap rather than naming the newest available source?
- **Locality test.** Have two sources been treated as saying the same thing merely because they use the same word? If so, use the ordinary F.0.1 branch on the exact passages before deciding their roles, then return to selection.
- **Search-policy test.** Did a score decide membership before source claims were inspected? Undo that decision.
- **Memory test.** Can the receiver hold the cut and each source's role in view? Remove non-changing material or split genuinely different questions.
- **Reopen test.** Can the note say what future change would require selection again?

### F.1:5 - Archetypal Grounding

#### F.1:5.1 - Three heterogeneous source cuts

##### F.1:5.1.1 - Role assignment, performed work, sensing, and execution

Candidate sources include BPMN 2.0 (designed workflow structures), PROV-O (performed activities and provenance), ITIL 4 (service vocabulary), ODRL 2.2 (permissions, prohibitions, and duties), SOSA/SSN (observations and results), and IEC 61131-3 (control-program execution). Retain only those whose exact claims change the receiving question.

The cut keeps false friends visible: a BPMN participant is not an RBAC role; a PROV activity is not a BPMN process; an SOSA observation is an act, not a status; an ITIL incident is not automatically a plant fault. F.1 exposes these source roles but does not settle their relations.

##### F.1:5.1.2 - Methods, types, and measurement

SPEM 2.0 or ISO 24744 may change the reading of Method and MethodDescription; OWL 2 and formal concept analysis may change kind reasoning; SOSA/SSN and ISO 80000-1 may change measurement and quantity claims. The cut preserves the source-fixed differences rather than making *method*, *concept*, or *measurement* globally uniform.

##### F.1:5.1.3 - Control, actuation, and services

Control-theory sources, IEC 61131-3, ISA-95, ITIL 4, and SOSA/SSN can contribute different claims about controller design, program execution, integration, service commitments, and observations. A current question may need only a subset. *Actuation* is not a service promise, and *incident* is not a plant fault merely because the words occur near operational work.

#### F.1:5.2 - Minimal worked source cut

The project brief already identifies this receiving question: **Can one contribution use “process” for both a workflow description and a performed occurrence?** The exact question, not the note or source list, is the `SourceCutNote`'s EntityOfConcern. The project names its effective ReferenceScheme **Workflow and occurrence source cut, August 2026**; that scheme fixes the three editions below and the ordinary-English role statements. The intended use stays in the ClaimGraph.

```text
Receiving use: decide which subjects the later pattern must keep distinct.

Retain:
- OMG BPMN 2.0.2 (January 2014), §10.1: its workflow-structure claim changes the design-description side.
- W3C PROV-O Recommendation (30 April 2013), §3.1: its Activity claim supplies the performed-occurrence contrast.
- W3C SOSA/SSN Recommendation (19 October 2017), §4.3.2.2: Observation supplies an action-changing counterexample—an act that follows a Procedure and yields a Result, not a workflow graph.

Exclude for now:
- thermodynamic-process literature: no inspected claim changes this stated use.

Known limit: service commitments are outside this cut.
Reopen if: the use adds physical transformation or service commitments, a relied edition changes the relevant claim, or a known counterexample no longer fits.
Search policy: none needed for this bounded question.
```

The resulting `SourceCutNote` is identified by that ClaimGraph, the stated receiving question, and the named reading scheme. Because this cut turns on the difference between a designed workflow and a performed occurrence, the project recovers any disputed *process* reading through ordinary F.0.1 while inspecting source roles, before stabilizing the cut. It adds an F.17 cell afterward only if later reuse, a claim, a named receiver, or an actual relation needs one.

#### F.1:5.3 - Portable first-hour case — function-to-module allocation

“First hour” means a compact entry slice, not a deadline or completeness claim.

**Receiving question.** Which current FPF sources must a Systems Engineering author use to prepare a first function-to-module allocation teaching slice without collapsing functions into modules? The project identifies this sentence as one exact question before treating the note as a C.2.1 episteme; that question is its EntityOfConcern.

**Receiving use.** Prepare a slice that helps a practitioner generate and compare candidate bearers, modules, allocations, interfaces, and trade-offs instead of copying functions into a component list or selecting familiar bearers first. This use stays in the note's ClaimGraph.

**Effective ReferenceScheme.** `FPFCoreReferenceScheme`, applied to the FPF August 2026 edition and the exact section locators below.

**Retained sources and answer-changing roles.** All five are exact passages in that edition.

1. **A.6.F §§4.2 and 4.5.** Separates the possible subjects hidden by function-like wording and requires function, bearer, flow, module allocation, and interface claims to remain distinct. This blocks the one-function-one-component shortcut.
2. **A.6.M §§4 and 4.3.** Treats module use as claim content over exact holons, allows many-to-many or still-unallocated functional claims, and requires an actual interface specification when compatibility or substitution is claimed. This changes what an allocation row must show.
3. **C.30.TFS-REL §4.2.** Relates functional structure to selected transformation-flow structure without identifying them. This exposes candidate flow topology, crossings, and correspondence limits that can change bearer placement.
4. **C.31 §4.5.** Makes function-module alignment, interface burden, and flow-boundary alignment separate characteristics rather than one modularity score. This changes the trade-offs the comparison must expose.
5. **C.32 §§4–5.** Starts candidate synthesis from functional demand and candidate bearers, keeps materially different configurations visible, and records expected gain, known loss, constraints, and source-return conditions. This prevents the source cut from pretending to choose the architecture.

**Deliberate limits.** The cut claims neither an exhaustive survey of allocation algorithms nor one module taxonomy or cross-sector optimum. It does not decide the final DPF pattern identity.

**First result.** One `SourceCutNote` whose ClaimGraph contains the five roles, use, limits, and reopen conditions; whose EntityOfConcern is the stated question; and whose effective scheme is `FPFCoreReferenceScheme` for FPF August 2026. The later comparison must expose unsupported capabilities, unallocated functions, unresolved interfaces, alternatives, trade-offs, and accepted losses.

**Reopen when.** A relied FPF passage changes, the question expands to external allocation algorithms or another domain, or the intended DPF use changes the required answer or boundary.

#### F.1:5.4 - Readable reasoning moves

- **Retain:** “This exact source stays because this inspected claim changes the answer in this way.”
- **Exclude:** “No inspected claim from this source changes the stated use; record the exclusion and what would reopen it.”
- **Return a gap:** “This unavailable or uninspectable source may be load-bearing; the cut remains limited here.”
- **Keep meanings local:** “Selection puts both sources in view; it does not say their terms are identical or related.”
- **Use search assistance:** “The ranking tells us what to inspect next; the source claim decides whether it enters the cut.”
- **Reopen:** “This question, use, relied claim, rival, counterexample, or transfer boundary changed, so select again.”

<a id="f155---didactic-distillation"></a>

#### F.1:5.5 - Didactic distillation of source selection

> State and independently identify the question; keep the later use in the claims. Keep a source because an inspected claim can change the answer, expose a rival or counterexample, or mark a transfer limit. Return one finite `SourceCutNote` whose ClaimGraph carries those roles, exclusions, limits, and reopen conditions, whose EntityOfConcern is the exact question, and whose named effective scheme resolves the question and exact editions. Search scores may guide inspection; they do not admit or exclude a source. Stop when additional candidates do not change the answer.

#### F.1:5.6 - Manual archive: a rule under an unfamiliar name

A workshop reader asks, “May a shared bench be used while an acceptance run is cooling?” The available fictional archive has three paper binders labelled *Setup*, *Drawings* and *Bookings*. Its card catalogue lists current equipment names. The reader has no searchable index or retrieval service.

The reader preserves the whole question, including the cooling interval, and bounds the search to those binders. The catalogue has no “cooling” entry. That is a limitation of this route. Browsing *Setup* produces a reference to an older equipment name and a drawing whose legend says “reserved interval”. The reader tries that term in the drawing register and obtains drawing D-14, edition 2, note 6. The note reserves the bench through the cooling interval; its exception allows sharing only before the run begins.

The result is that inspected note, its drawing and edition address, why the interval and exception matter, and the scope of the archive searched. It supplies a rule for the subject practitioner to use with the actual run conditions. It does not establish the present bench state or permission by itself. The reader need not produce a SourceCutNote merely to return this sufficient source.

Change the question to “Which inspection condition changed between editions?” The reader obtains the available D-14 edition 1 note and compares it with edition 2 around the exception. Both passages become candidates. If the later comparison needs a justified two-edition basis, :4.2 selects their roles and returns a SourceCutNote. Change the question instead to “What word do these drawings use for the cooling interval?” The inspected wording can answer directly; further source selection adds nothing to that use.

The first failed route mattered because its catalogue vocabulary excluded the older name. The complementary route recovered source wording. This construction works with paper and ordinary reading; it requires no index engineering or automated ranking.

#### F.1:5.7 - An uncertain method-library vocabulary

A project reader asks, “Two proposed pattern uses each fit our concern, but both need the same exclusive instrument. What helps us say which use should precede the other?” They can search the available full FPF publication but know no PatternID for that concern.

The first lookup, “suitable methods”, yields only general fit cues. The reader preserves the shared-instrument condition and tries variants such as “coordination”, “shared constraint” and “precedence”. A contents row points to E.11.PUR. The reader opens the complete pattern, including :4.3–:4.4 and :5.5, rather than treating the row as an applicable Method.

The returned material explains why exclusion alone establishes conflict without selecting A-before-B. An applicable schedule or priority rule can supply a direction; when it is unknown, the direction remains unresolved. The reader returns that passage and the missing-rule question. The later judgement uses E.11.PUR; a work schedule or performed work claim belongs to A.15. Finding the passage creates neither kind of judgement.

A title-only service that cannot search or return those body conditions would require another accessible route or return its limit. If the reader already has a current adequate coordination judgement, finding can stop there. The example's useful search terms are variants for this concern, not fixed names every corpus must use.

#### F.1:5.8 - A changed edition with a known source

An engineer already has the needed fictional WS-4 procedure, edition 2, clause 7. An edition-3 notice names a changed inspection exception. The question remains whether the same inspection condition applies. The engineer opens edition 3 at that clause and reads the exception with its surrounding applicability conditions.

If the relied condition is unchanged, the passage remains usable for its earlier contribution, with the updated edition address. If the exception changed, the engineer returns the changed passage and the earlier passage when the comparison needs it, then reopens the affected subject judgement or source-cut claim. No unchanged chapter needs a new search merely because the cover changed.

Now change the question to whether a particular attachment can be accepted. The retrieved clause does not settle an unknown material or operating condition. The subject engineer receives the passage and that missing premise. A found rule and a justified source cut supply different contributions from engineering applicability.

#### F.1:5.9 - The original cannot be inspected

A review cites a 2025 original, but the reader can obtain only the review's excerpt and the original's catalogue record. The catalogue establishes a lead. The excerpt is inspectable at its own review address; the original's body and omitted conditions remain inaccessible.

Return those distinctions and identify the needed original or authorized access. Continue a use that the excerpt can actually support; keep a dependent judgement open when its missing context can change the answer. Another search over the same catalogue cannot turn the original into inspected material. A later copy of the original reopens that gap; it does not require discarding other unchanged findings.


#### F.1:5.10 - A changed question with two needed contributions

A workshop reader asks, “Which training material will reduce mistakes at handover?” The available fictional archive contains a course catalogue, an incident note, the current equipment register R-4, a handover procedure H-2 and several equipment-identification guides. The immediate concern is a receiver being sent to the wrong pump or being unable to tell whether its preparation is complete.

The catalogue points to a note about equipment labels. Reading it reveals that an old label is used for two different pumps. This gives the reader a more useful local inquiry: what must the handover distinguish so its receiver can identify the equipment and its preparation state? B.5.PI:4.4 permits this revision while retaining the original concern. Searching for another synonym of “course” would keep the earlier hypothesis in control.

The equipment register explains how current identifiers distinguish the pumps. Further guides found through different terms give more identification examples, but leave the preparation-state question unanswered. A reference in the register gives a route to H-2. The next search opens its completion condition in section 5, with the definition of the reported state and interval. The new contribution is that condition, not merely a new document.

The reader now returns R-4:2 for the equipment-identification basis and H-2:5 for the condition on reporting completed preparation. These supply the current requirement question. Stop searching and use them to examine the proposed handover. Choosing a course still requires judging the actual learning need; identifying the requirements did not make that judgement. If the available operations do not explain how to produce the required handover, use C.39 to develop the missing connection, with those passages as inputs.

If the procedure is inaccessible, return the inspected identification passage and the missing preparation-condition source. More identification guides do not close that gap. If both passages were already known and sufficient, open them directly. No additional route or SourceCutNote is needed for that use.

### F.1:6 - Bias-Annotation

- **Gov:** Authority, popularity, international status, or sponsorship does not decide membership; the receiving question and inspected claims do.
- **Arch:** The method keeps source roles explicit and the active cut small without claiming exhaustive coverage.
- **Onto/Epist:** A source, edition, inspected passage, inaccessible lead, source claim, local meaning, source-cut episteme and representation remain different.
- **Prag:** Direct use of one identified sufficient source is the cheap exit. Add a search route only when it can repair a consequential gap at acceptable effort.
- **Did:** A one-screen representation protects working memory; detailed analysis stays with the receiving work.
- **Scope:** Practitioners use F.1 to find material and justify source selection. Truth, adequacy, semantic relations, synthesis, reliance and assurance remain receiving questions.

### F.1:7 - Conformance Checklist

#### F.1:7.1 - Static checks


Checks that refer to a cut or `SourceCutNote` apply when source selection is current; ordinary finding needs no note identity.

- **SCR-F1-S01 (Question and use).** The receiving question is independently identified as the note's exact EntityOfConcern; the intended use and the source difference that can change the answer remain in its ClaimGraph.
- **SCR-F1-S02 (Exact sources).** Every retained source and edition is recoverable.
- **SCR-F1-S03 (Answer-changing roles).** Every retained source has an inspected role; exclusions and source gaps are explicit.
- **SCR-F1-S04 (Finite and inspectable).** The cut can be held in view without dropping a known answer-changing source merely to satisfy a count.
- **SCR-F1-S05 (C.2.1 identity of the source-selection result).** The `SourceCutNote`'s ClaimGraph, exact receiving-question EntityOfConcern, and effective ReferenceScheme are all recoverable. The scheme resolves the question, exact source editions, and role claims. A file, source list, one-screen form, or question-and-use bundle supplies none of these values by form and does not become another source-selection result kind.
- **SCR-F1-S06 (Locality).** No cross-source equivalence, merge, or relation is asserted by selection.
- **SCR-F1-S07 (Temporal honesty).** Designed and performed source claims remain distinct when the difference affects the answer.
- **SCR-F1-S08 (Family neutrality).** No meaning, relation, or membership decision relies on a domain-family label.
- **SCR-F1-S09 (Named search policy).** Any material search aid has a recoverable policy, corpus, method or model edition, and interpretation.
- **SCR-F1-S10 (No algorithmic gate).** A search reading changes the cut only after inspection of source claims.
- **SCR-F1-S11 (Reopen conditions).** The result says which question, use, edition, rival, counterexample, or transfer-boundary change reopens it.
- **SCR-F1-S12 (Domain-method boundary).** A required systematic or appraisal-bearing review remains with its domain method.
- **SCR-F1-S13 (SoTA source roles).** A cut used for a SoTA claim assigns every retained source one of the comparison roles defined in `E.8:11`, records it in plain wording, and says which retained contributions can change the answer. F.1 does not restate or supersede the E.8 definition.
- **SCR-F1-S14 (No authority or currentness laundering).** Official status, popularity, maintained status, citation count, publication date, freshness, or academic praise does not promote a source into the best-known line. An official or widespread source may still earn that role from its substantive comparison. Catalogue and publisher pages support identity/currentness only unless their substantive claims independently enter the comparison.
- **SCR-F1-S15 (SoTA one-source guard and gap).** A one-source SoTA cut is used only when that source critically synthesizes the serious alternatives and no known action-changing rival or counterexample remains hidden. Otherwise the cut retains the necessary comparison or returns a source gap.

- **SCR-F1-S16 (Finding return).** The original concern, inspected candidate material, source/edition locations, contribution and consequential search/access limits remain recoverable; leads remain distinct from inspected content.
- **SCR-F1-S17 (Scoped stop).** A sufficient known source can end ordinary finding; a no-hit result states its searched scope and routes and leaves a consequential access gap open.

#### F.1:7.2 - Regression checks

- **RSCR-F1-E01 (Edition change).** Recheck only answer-changing claims that used the changed edition.
- **RSCR-F1-E02 (Use change).** Recheck which sources, rivals, counterexamples, and limits matter when the question or use changes.
- **RSCR-F1-E03 (New false friend).** Add a concise warning when recurrent wording confusion changes the receiving answer.
- **RSCR-F1-E04 (Bounded cut).** Remove non-changing sources or split genuinely different questions when the active cut can no longer be inspected together.
- **RSCR-F1-E05 (Search drift).** A changed taxonomy, corpus, model, descriptor, scale, distance, threshold, or rank cannot silently change membership.
- **RSCR-F1-E06 (Finding reach).** Recheck affected material and limits when the question, access or search representation changes; retain findings whose contribution and conditions still hold.

### F.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One-book domain | One influential source is treated as the whole answer despite a known rival or transfer limit. | State the question and add each source whose inspected claims change it. For a SoTA claim, the one source must itself critically compare the serious alternatives. |
| Currentness laundering | A registry entry, official status, maintained label, citation count, or recent date promotes a source into the best-known line. | Record identity and currentness separately. Select rank only from the answer-changing comparison, or return the unresolved source gap. |
| Source-role collapse | A lineage anchor, popular default, failure case, and best-known-line candidate are all reported as equivalent support. | Classify each retained source by its answer-changing role; official/popular-comparator, lineage-only, and identity/currentness-only roles do not supply SoTA rank. |
| Reading-list cut | Many sources are retained without distinct roles. | Keep only answer-changing roles and record deliberate exclusions. |
| Edition blur | A source is named without the edition that fixes the relied claim. | Identify the edition and reopen only affected claims when it changes. |
| Domain-family inference | A shelf label is treated as evidence of meaning, relation, or relevance. | Use the label only to find sources; inspect their claims. |
| Relation by stealth | Selection prose says two sources are “basically the same.” | Keep them distinct and open an F.9 question if an actual relation is needed. |
| Designed-versus-performed collapse | A design description is treated as a performed occurrence. | State the source role and the time distinction it contributes. |
| Search score as gate | Rank, distance, threshold, or model answer admits or excludes a source. | Use the reading to prioritize inspection; decide from the source's contribution. |
| Variant becomes the question | A broader query drops a condition, and the returned passage answers that broader question instead. | Preserve the original concern and restore its conditions during candidate inspection. |
| Locator becomes source | A title or excerpt is treated as inspection of the unavailable original. | Return what was actually inspected, its address and missing context; retain the original as an inaccessible lead. |
| No hit becomes absence | One phrase or limited index finds nothing, so the whole repertoire is declared empty. | State the route's reach, repair a consequential blind spot if feasible, or return the scoped gap. |
| Exhaustive pretense | A small cut is reported as complete literature coverage or saturation. | State its question-relative limits and use the domain review method when needed. |
| Compact-note inflation | The one-screen representation grows into a second source analysis. | Keep the ClaimGraph concise and place detailed analysis with the receiving work. |
| Context container revival | Sources or meanings are treated as members of a universal Context object. | Identify the exact sources. When a source-role decision depends on a disputed expression, recover its plain local meaning through F.0.1 before selection; create an F.17 cell only for a later durable need. |

### F.1:9 - Consequences


An unfamiliar name or incomplete search view need no longer end finding silently. The practitioner can construct a route from the available source, words or references, repair a consequential blind spot and return material with an honest limit. That result may support a direct answer without requiring source selection.

The source cut becomes small enough to inspect, while a decisive rival, counterexample, or transfer limit cannot be discarded merely to satisfy a count. Later work can recover why each source was present, which edition was used, what the cut deliberately omitted, and what change reopens it.

The cost is explicit judgment. The author must say what each source can change and disclose a load-bearing gap instead of treating absence as evidence against a claim. Unknown rivals can still be missed, so citation chasing, expert leads, search aids, or a domain review method may remain necessary. Their outputs are candidates until source claims are inspected.

The cut is not evidence that its sources are true, sufficient, representative, mutually compatible, or safe to rely on. Those conclusions belong to the receiving synthesis, domain evidence method, F.9 relation, A.10 reliance account, or B.3 assurance claim.

#### F.1:9.1 - Changes that reopen or revise a cut

1. A source edition changes a relied claim, limit, or distinction.
2. The receiving question or intended use changes.
3. A new rival explanation, action-changing counterexample, or transfer limit appears.
4. A formerly retained source no longer changes the answer.
5. A language edition changes distinctions used by the result; treat editions separately unless the source supplies a mapping that preserves them.
6. Search-policy drift reveals a candidate but never changes membership without source inspection.
7. A later F.9 relation is proposed; keep source selection unchanged unless that proposal changes the source roles themselves.

### F.1:10 - Rationale


Finding is useful when the question and the source's wording do not yet meet. An exact address or lexical lookup is sufficient when it reaches the needed content. Variants and complementary routes earn their extra cost by exposing material that the first route could miss. Restoring the original conditions during inspection prevents broader discovery from changing the question. Returning source context and actual access prevents a compact finding aid from supplying claims it never showed.

Source selection for conceptual work is neither statistical sampling nor a race to the largest bibliography. The receiving question determines which source differences matter. A source belongs in the active cut when an inspected claim can change the answer, expose a rival or counterexample, or mark where transfer fails.

This keeps the useful part of purposive and iterative sampling—selection for a stated analytic purpose—without importing another field's population, richness scale, saturation claim, or count convention. It also keeps the useful part of systematic-search and AI-assisted screening—recoverable searches and efficient candidate discovery—without treating search coverage, rank, or reporting conformance as source adequacy.

### F.1:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and F.1 mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a small source cut remain question-led while exposing decisive heterogeneous rivals and limits? | Critical interpretive synthesis is the best-known-line candidate for this bounded comparison because it begins from a compass question, uses purposive iterative selection, critiques assumptions, and can synthesize heterogeneous evidence. Perlman, Ben-Sheleg, and Ellen's 2026 scoping review makes the method's recurring phases, variation, and gaps inspectable. | Protocol-first systematic-review reporting and one-canon selection are the serious defaults. PRISMA and PRISMA-S are retained only as an official/popular comparator when a protocol-defined review is actually required. | Fixed eligibility and reporting can preserve search history without deciding which conceptual claim changes the answer; one-canon selection hides rivals and transfer failure. **Adapt:** F.1 uses a stated question, inspected roles, iterative reopen, explicit gaps, and a separate `F.0.2` synthesis boundary. **Reject:** a saturation claim, health-domain appraisal rules, and an exhaustive protocol for every bounded question. | Perlman, Ben-Sheleg, and Ellen, [*Making sense of conducting a critical interpretive synthesis: A scoping review*](https://doi.org/10.1017/rsm.2025.10041) (2026), is the current critical synthesis; PRISMA/PRISMA-S are the explicit protocol comparator; purposive-sampling studies support the variation problem but set no FPF quota. | Reopen if a stronger current source-selection synthesis offers a cheaper method that exposes the same action-changing rivals, counterexamples, limits, and gaps. |
| How may search automation reduce effort without deciding the source cut? | Transparent active-learning screening is the best-known-line candidate for prioritizing inspection in a large candidate set when its corpus, model, and stopping interpretation remain recoverable. | Ranking, similarity, citation count, or an LLM answer used directly as the membership gate is the serious default. | The default converts an attention proxy into relevance, truth, or completeness. **Adapt:** `F.1:4.4`, invariants, self-checks, and regression checks let search readings order inspection but require the underlying claim before membership changes. | van de Schoot et al., [*An open source machine learning framework for efficient and transparent systematic reviews*](https://doi.org/10.1038/s42256-020-00287-7) (2021), supplies an efficient transparent-screening branch, not evidence that a retained source is relevant or sufficient. Search-tool documentation and latest-model status are identity/currentness only. | Reopen if a current method demonstrates lower inspection effort while preserving claim-level membership decisions and explicit omission risk. |
| How should finding adapt to a revised question and stop with enough material for its next use? | Adopt exploratory, source-led search and adapt it with an explicit comparison of the material still needed by the receiving use. In :5.10 this directs the next search to the missing preparation condition and then permits a sufficient stop. | Developed berrypicking already changes the information need, follows references and changes techniques. A sufficient direct lookup remains preferable to further exploration. | Changing terms or documents can leave a necessary contribution unrepresented. **Adopt:** evolving inquiry and varied routes. **Construct:** the connection from their results to :4.4.1's revised question, :4.4.4's remaining contribution and :4.4.5's bounded return to selection or subject work. The deliberate cost is this local comparison; no extra search is required when the material is sufficient. | Bates, [*The Design of Browsing and Berrypicking Techniques*](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html) (1989), §§II–IV, is the developed historical comparator. [BRIGHT-PRO](https://aclanthology.org/2026.acl-long.1705.pdf) (2026), §6.3, supplies contemporary failure evidence: repeated evidence, neglect of a required aspect and continued search after sufficient retrieval in its evaluated agent setting. Neither source establishes an FPF retrieval advantage or a universal stopping rule. | Reopen when the contribution comparison misses a needed aspect, imposes effort without changing the return, or a stronger method supplies the same bounded result more affordably. |

Choose the cheapest attainable route that supplies the needed material and its consequential limits. Source selection still leaves synthesis and assurance to their own methods.

### F.1:12 - Relations

- `E.8:11` owns the canonical SoTA definition, comparison-role meanings, and positive comparison contract. F.1 prepares only the question-relative source cut and records those roles for the receiving comparison.

**Builds on.**

- `C.2.1` identifies the `SourceCutNote` from its ClaimGraph, the exact receiving question as EntityOfConcern, and its effective ReferenceScheme, and distinguishes that episteme from its representation.
- `F.0.1` supplies a plain local reading during selection when a candidate's answer-changing role depends on a disputed expression.
- `F.17` supplies a durable local-sense cell after selection only when later reuse, a claim, a named receiver, or an actual relation needs one.
- `B.5.PI:4.4` helps reconstruct a question revealed by source reading while returning to the original receiving concern.
- `A.11` supplies the parsimony test; finiteness does not replace relevance with a fixed count.
- `E.15` supplies affected-premise reopening across source editions.

**Related later uses.**

- `F.0.2` can compare or synthesize the exact sources, roles, limits, and reopen conditions returned here.
- `C.39` develops a missing obtaining way from inspected contributions; finding those contributions does not supply their connection.
- `F.9` defines any actual relation between distinct recovered local senses; F.1 asserts none.
- `G.2` supplies the broader refreshable SoTA-pack method when that heavier result is required.
- Use `A.10` for reliance and `B.3` for assurance; source selection establishes neither.
- `E.11` supplies public finding cues; `E.11.PUR` judges proposed pattern uses and `E.11.PUA` guides one selected use. Finding supplies the source material needed for those judgements without making them.
- An author of a subject pattern or DPF may use the source cut directly when an inspectable source basis is needed but no cross-source synthesis is current.

### F.1:End
