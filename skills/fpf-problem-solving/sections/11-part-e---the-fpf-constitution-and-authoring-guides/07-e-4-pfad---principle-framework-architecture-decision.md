## E.4.PFAD - Principle-Framework Architecture Decision

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4.PFAD:1 - Problem frame

Use this pattern when an author is choosing among a new or revised principle framework, a contribution to an existing framework, another maintained product that is not a framework, a thinner publication or access route, and no new maintained product, and that choice will settle a boundary that later work must use. The boundary may concern the public field and first use, framework edition, dependencies, initial pattern placement or relations, the kind and maintenance boundary of a non-framework product, or the publication or access consequence. Another author or reviewer must need the answer and its rationale for later action.

Here *product* has the Plain management meaning declared in `E.4:4.1`; it is not a technical kind. When a maintained non-framework alternative is selected, the answer names the direct subject—the thing being maintained—its kind, and the relations used for identity, current state, provision, and maintenance. If a kind or relation that can change the answer is unresolved, keep it as an explicit decision question and do not invent `U.Product`.

A proposed new or substantially revised DPF also needs an answer about its field boundary. That answer says who can first use the framework and for what, which connected problem families and useful results it covers, what the current FPF and admitted DPFs already provide, and what remains uncovered. It compares serious alternatives, tests one representative case that crosses problem families, states where the evidence runs out, and names the change that will require a refresh. Together these must support one independently usable pattern language. One pattern or a narrow authoring slice is not a DPF merely because it has a broad title or a coherent carrier.

If a cheap search, curated reading route, useful contribution to an existing framework, suitable non-framework product, or stop answers the immediate need without settling such a boundary, use that result and stop. Do not open a framework-architecture DRR merely because `E.4.PFAD` exists.

When the architecture question is live, use `E.4.PFAD` to state the framework-specific content of one ordinary `E.9` DRR. Decision Work selects the answer; the DRR records it. This pattern is a practitioner-facing profile and locator. No PFAD relation or second decision record is created, and acceptance remains separate.

### E.4.PFAD:2 - Problem

Framework authors repeatedly need to decide whether a recurring practitioner problem calls for a new framework, an existing framework contribution, another maintained product such as a programme, service, or evidence package, a thinner access result, or no maintained product. When a framework is selected, later work needs its public field promise, first-edition boundary, FPF Core dependency, problem-family coverage, first patterns and their material relations, representative use, important omissions, and publication or access consequence. Generic decision prose can hide those choices.

A small coherent authoring slice creates a common false positive: its few current patterns and neat structure are mistaken for a field-scale pattern language. Source diagrams create another: one list or hierarchy is copied into the DPF although Methods, Work, subjects, descriptions, capabilities, providers, and cultural change may have different structures. A large framework-specific form creates the opposite problem by making proposal, acceptance, DRR, edition, authoring, quality review, and publication look like one extra decision object.

The useful result is one readable answer whose framework consequences and limits are visible without adding a second decision stage or making cheap exploratory work produce decision paperwork.

### E.4.PFAD:3 - Forces

| Force | Tension |
| --- | --- |
| Discoverability | Authors need a recognizable framework question, but a locator must not become another decision object. |
| Framework scale | A narrow pattern set can be useful, but a broad public framework needs connected problem-family coverage, a first use that does not depend on unpublished authoring context, and a stated reason for later refresh rather than a pattern count. |
| Several structures | A decision needs one coherent practice-architecture answer, but Method, Work, subject, description, capability, provider, and cultural structures need not line up one-for-one. |
| Decision memory | Later work needs rationale and consequences, but the DRR is not the accepted answer, performed authoring, or framework edition. |
| Framework detail | Edition, dependency, pattern placement, relations, omissions, the sources that later authors must be able to revisit, and publication consequences matter, but unrelated quality, naming, and package apparatus must stay conditional. |
| Cheap exit | A suitable non-framework product, small access result, or existing-framework contribution may solve the immediate problem without a framework decision. |
| Relation precision | Initial pattern relations may shape the architecture, but a row or schema does not make those relations obtain. |
| Evolution | The answer needs a reopen condition without turning every refresh concern into a mandatory field. |

### E.4.PFAD:4 - Solution

#### E.4.PFAD:4.1 - Decide whether the architecture question is open

Ask whether choosing a framework, a maintained non-framework product, a thinner route, an existing-framework contribution, or stop will settle at least one boundary used by later authoring or review:

- the public field promise, a first use that does not depend on unpublished authoring context, or the problem-family coverage of a proposed DPF;
- an intended or existing framework edition;
- an FPF Core or other current edition dependency;
- initial pattern placement or a material relation among those patterns that changes the architecture;
- the direct subjects and maintenance boundary for a continuing programme, an admitted service, or a separate editioned result when later work must maintain or use them;
- a publication or access consequence; or
- for a proposed DPF Suite, the ecosystem use, which product series may belong, constitution, inclusion and removal rules, identity through change, maintenance and source-return conditions, exposure choice, and any separate Guide-product decision.

If no such boundary and receiving use are present, close the exploratory use without `E.4.PFAD` or an `E.9` DRR. If they are present, decision Work selects a framework, maintained non-framework product, thinner route, existing-framework contribution, or stop and one `E.9` DRR records that answer. The cheap exit and the architecture decision are alternative entry outcomes, not serial stages.

For every maintained alternative, use *product* only as the first management cue. Then compare the direct subjects at the same grain: the exact framework or package episteme, System, service arrangement, Method, programme description, carrier, or other admitted result, and the relations that later work will rely on. A quality-management, service-management, publication, or content-management scheme may supply a useful probe, but it does not settle the FPF kind. If the unresolved kind can change the selected boundary, keep the boundary proposed and make that kind the next decision question.

#### E.4.PFAD:4.2 - State the compact framework answer

When the architecture question is open, the framework-specific part of the DRR states:

1. the intended practitioner, public field name and promise, recurring problem, and bounded architecture question;
2. the selected outcome: a new or revised framework edition, a contribution to an existing framework, a maintained non-framework product, a thinner publication or access route, or no new maintained product now; for a maintained non-framework product, also the direct subject kind and the identity, current-state, provision, or maintenance relations used by the decision;
3. its field boundary: who can first use it without unpublished authoring context and for what; the connected problem families and useful results; what the current FPF and admitted DPFs already provide and what remains uncovered; serious alternatives, such as splitting or merging the proposed framework, using existing sources directly, contributing to an existing framework, selecting a programme or service boundary, selecting a separate evidence-package episteme, or keeping no maintained product; the limits of evidence; and what change will require a refresh;
4. the selected problem-family pattern sets, first patterns and their material relations, representative cross-problem application, and important omissions;
5. which practice structures change the answer and how their Methods, descriptions, patterns, direct subjects, and managed result boundaries fit together. When those structures do not line up one-for-one, use a completed `C.32.MWA` synthesis; use `E.23.CDI` only when capability development for a named Work family changes the answer;
6. the existing or intended-edition boundary, selected FPF Core dependency, and only the other exact edition dependencies required by this answer;
7. the sources to revisit for each important claim, whether the evidence supports, suggests, or only motivates it, the limits of that evidence, and the publication or access consequence; and
8. material alternatives, accepted costs or losses, practical consequences, the first authoring action or stop, and the reopen condition.

When professional Method coverage can change point 5, the same compact framework answer projects five connected claim groups from points 1, 3, 4, 5, 7, and 8. The projection is content of that one answer and its one ordinary `E.9` DRR, not a second architecture record, fixed schema, or later DPF invention. Fill each group only to the grain that changes first use:

1. **Practice truth and first use:** identify every bounded practice claim or promised practice contribution by its exact subject and scope, mark that claim—not the answer as a whole—as obtaining or possible-future, and state practitioner, recurring or anticipated difficulty, sought result, first use, non-use boundary, qualification window, and receiving decision.
2. **Project and Method positions:** name the direct project subjects, use and environment, materially different solution forms, and Methods under their actual operational, system-change, solution, Method-of-interest, or Method-development relations. Keep incumbent Work, development or trial Work, candidate-practice Work, and intended Work distinct.
3. **Selected structures and correspondences:** include only the Method, Work, subject, transformation-flow, capability/provider, description, contribution, Method-development, and cultural structures whose correspondence, conflict, or non-isomorphism changes the answer.
4. **Pressures and evidence:** keep constraints, conflicts, failures, environment or interest changes, and observed, source-supported, estimated, contradicted, and missing links distinct from causal history and temporal unfolding.
5. **Contribution, subtraction, gaps, and reopen:** state what current FPF and admitted DPFs already supply, each receiving pattern and domain filling still needed, exact external results, honest omissions and gaps, and the observation that reopens the architecture.

One answer may contain several bounded practice claims with different truth status. Every selected practice question names the claim or claims it consumes, so an obtaining incumbent-practice claim can coexist with a possible-future candidate-practice claim without backdating the candidate or erasing current incumbent coverage. Independently obtaining A.13 agency claims and actual development or trial Work keep their own status; neither proves that the candidate practice obtains. Public coverage is another claim and remains limited to the exact obtaining or prospective contribution and later package evaluation.

For an obtaining practice claim, name actual recurring difficulties and representative actual Work. A precise Agent-performer branch first supplies A.13's core: the exact admitted System, local agential system-role kind and criterion, classification, obtaining assignment, and needed scope, working situation, and window. Add the agency-characteristic profile only when a Grade, autonomy or profile claim, a criterion-dependent characteristic, or a named assurance use consumes it. A.15.1 then independently admits the actual Work from its performance history, Method, extent, and containment. Only after admission does F.6 supply any precise assignment-bound attribution through that same obtaining assignment. State evidence limits; a missing F.6 relation leaves admitted Work intact and only the attribution unresolved.

For a possible-future practice claim, name intended use, incumbent Work or Method and observed problem evidence, candidate Methods and architecture, realization conditions, a planned representative trial, expected acceptance and failure observations, and reopen conditions. Any incumbent-practice or actual trial-Work claim stays independently obtaining when supported, but the candidate-practice Work, candidate-practice Agents, and current candidate-practice coverage remain unasserted until their own conditions obtain.

For every selected question, name its receiving pattern and the exact bounded practice claim or claims whose values change first use. If a required group or claim-to-question binding is absent at that grain, return a bounded PFAD gap before DPF authoring; the DPF author does not invent the missing value. A completed `C.32.MWA` synthesis is used only when several selected structures do not line up one-for-one, and `E.23.CDI` only when capability development changes the answer.

The answer is one identified claim-bearing episteme under C.2.1 and is recorded, with its rationale, in one ordinary E.9 DRR. Decision Work selects that answer. A separately identified authorized acceptance decision accepts, redirects, rejects, or reopens it; carrier identity, DRR identity, or the fact that authoring continued identifies neither the accepting decision nor acceptance. Only the exact accepted answer is handed to E.4.DPF.

Common practice questions include:

| Practice question | Pattern that supplies or tests the answer |
| --- | --- |
| What contribution or effect is required? | `A.6.F`; use `C.30.ASV` only when a selected architecture view changes the answer. |
| Which Methods construct a larger Method, and which genuine interfaces matter? | `B.1.5`; use `A.6.M` only for a real module, port, or implemented-interface claim. |
| What changed, and how are the transformation-flow positions related? | `A.3.4`, `E.18`, and `C.30.TFS-REL`. |
| What Work occurred, which Method did it enact, and who performed it? | `A.13` followed by independent `A.15.1` admission; `F.6` only afterward for precise assignment-bound attribution, with the A.13 profile branch only when consumed. |
| Which System has the needed capability, and what did a provider actually contribute? | `A.2.2` plus the applicable Work, provision, or service pattern. |
| What cultural generation, transmission, reconstruction, recognition, selection, retention, or loss matters? | `C.36`. |

If another question changes the answer, name it and the pattern that handles it instead of forcing it into these rows. Do not infer Method parthood from a required contribution, transformation, performed Work, capability, provider contribution, or cultural change.
For a DPF Suite answer, an architecture decision takes effect to constitute the continuing collection. It selects the ecosystem use, which product series may belong, inclusion and removal rules, identity through change, alternatives, practical consequences, and the reopen condition. The same `E.9` DRR records that answer. A current maintained-Suite claim also identifies the capable maintaining System and its accepted commitment, the working source return for product series and any product-series state presented as current, the refresh response, and one exposure choice: an independent Suite route, a bounded Guide projection with source return, or a neutral combined carrier. Guide constitution, inclusion, maintenance, and refresh remain separate decisions and claims. A proposed result use or future constraint is not an obtaining dependency or compatibility relation; apply `E.4.PFR` only after the edition-level case facts exist.

For an existing-framework contribution, maintained non-framework product, thinner route, or stop, state only the parts needed to explain that outcome and the later-used boundary. A selected maintained product still names its direct subjects and the relations used; a proposed boundary with an unresolved kind says so. Do not fabricate a field assessment or package merely to fill the list.

When the architecture keeps, merges, removes, reuses, or omits a load-bearing contribution, record the `E.8:4.1.3` same-situation disposition and the action or result that changed. A narrower label or example is not a difference. A difference that adds an unsupported or needless burden is not worth preserving merely because it changes action.

When the answer treats a promised problem family as covered by a result maintained outside the framework, name the exact result, its direct kind, supplying product and edition or current state, receiving use, practical discovery route, and every currentness or availability condition that can change that use. State that the result remains external. If those facts are absent, or the result does not answer the promised use, record a gap or omission rather than relabelling the result as framework content, a MethodDescription, or source evidence. When the selected keep, merge, removal, profile, external reliance, or omission materially changes the stable set for a promised problem family, obtain a current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition. A matching current result remains usable when that edition and its exact basis are unchanged; the architecture answer does not ask D12 to prove that a revisit occurred.

Keep the ordinary `E.9` grounds, sources, affected loci, rationale, and consequences in the same DRR. Add naming, quality, admission, currentness, or package details only when they change this answer or a named later use requires them. Use the pattern that defines, constrains, or tests each added claim; do not make it a standing PFAD field.

#### E.4.PFAD:4.3 - State initial pattern relations directly

When an initial pattern relation changes the selected architecture, state the relation and its participants as an ordinary assertion. For example: `Pattern A frames the recurring problem; Patterns B and C specialize its reusable move for two stated situations.` Use the pattern that defines or constrains each relation function.

An optional `E.4.PFR` row may later represent these assertions for maintenance. The row neither makes the relations obtain nor becomes mandatory for the architecture answer. A generic relation catalogue is not a prerequisite for the decision.

#### E.4.PFAD:4.4 - Keep the answer, DRR, authoring, and publication distinct

Decision Work selects the answer. The `E.9` DRR records that answer and its rationale. An authorized acceptance decision accepts, redirects, rejects, or reopens it. Later authoring follows an accepted answer. A framework edition is the maintained pattern-language result assembled from accepted sources, not the DRR or the authoring Work. An ADR-like document, site, PDF, or other carrier publishes or projects claims about these things; its form creates none of them.

When the answer uses `C.32.MWA` or `E.23.CDI`, keep each proposed Method distinct from the pattern that describes it, the Work that performs it, the result of that Work, the framework answer, the DRR, and the resulting edition. A proposal or evidence locator may help a reader find supporting material; it is none of those things.

Use `C.32.PAD` only when the question is an exact project architecture decision about a named composite project Work, and use `C.32.ADR` only to project that project decision. For an ordinary framework answer, publish the selected decision episteme or a reader-specific projection through `E.17` and `E.24.PUB`. None of these is a mandatory stage of principle-framework authoring.

### E.4.PFAD:5 - Archetypal Grounding

#### Positive DPF

A systems-management group considers a public DPF for recurring problems in service launch, cross-team coordination, incident response, and feedback-based improvement. A broad FPF route covers several shared distinctions, and an admitted neighboring DPF covers one specialist branch, but neither gives this practitioner group a coherent first use across the four problem families. The field-boundary assessment compares a new DPF with direct FPF-and-source use, a guide, contribution to the neighboring DPF, two independently maintained DPF edition series, and no maintained product. It favors one DPF because a representative service-launch case needs patterns from several problem-family sets together and has an independent refresh boundary.

The source accounts organize Methods, dated Work, service and equipment subjects, descriptions, provider capabilities, and cultural change differently. A completed `C.32.MWA` result makes those correspondences and conflicts readable without turning the source layout into the DPF structure. The `E.9` DRR records the public promise, selected problem-family sets and material relations, representative case, Core and other exact dependencies, omitted procurement and certification questions, the sources to revisit, which claims the evidence supports, suggests, or only motivates, the publication consequence, first authoring action, and reopen condition. `E.23.CDI` is absent because capability development does not change this answer. No PFAD relation, mandatory PFR row, or proposal locator substitutes for the selected answer.

#### Exploratory access result

Existing FPF and source material answer the immediate need through a curated route. No later author or reviewer needs a settled framework boundary. The inquiry closes with that route and no PFAD or DRR.

#### Decision-level access result

A team needs a maintained choice among a DPF, an access route, and stop because later work depends on the rationale. The architecture question is therefore open. One `E.9` DRR selects no new framework edition, states the maintained access consequence and stop, and records when to reconsider the answer.

#### Non-framework programme product

A cross-domain inquiry need recurs, but practitioners do not need another pattern language. The decision compares a DPF, a maintained inquiry-programme boundary, a separate inquiry evidence-package episteme, a curated route, and no maintained product. It selects the programme boundary because named users need continuing access to inquiry Methods, bounded-project intake, and result return. The answer does not invent a Programme or Product kind.

Its first usable version is a current programme-description episteme that names the users and questions, inquiry Methods, project intake, result return, access, change, and retirement rules. Capable provider and maintaining Systems accept the needed commitments; when a service is claimed, the answer also names the admitted service state. Each bounded inquiry project is separate Work, and each returned result is a separate episteme. A subject pattern may instead admit the programme itself as a System or another exact arrangement, in which case the answer names it. A bounded project may end while the managed programme continues and evolves. The inquiry evidence package remains its own editioned episteme.

#### DPF suite and guide

Three independently maintained DPF product series already cover one recurring practitioner use. The architecture question is therefore not whether to merge them into another DPF. When one architecture decision takes effect, it constitutes the continuing Suite collection, states its ecosystem use, defines which product series may belong, selects inclusion and removal rules and identity through change, identifies the capable maintaining System and its accepted Suite-maintenance commitment, and chooses source return and exposure. Its `E.9` DRR records that answer and the initial inclusion decisions. Each DPF edition still belongs to its own product series under that series rule. The answer separately decides whether a Guide product series is constituted and included, identifies its capable maintaining System and commitment, and states its refresh route. It records any proposed cross-DPF result use but makes no dependency or compatibility claim until the edition-level predicates pass. A later author may propose inclusion or removal, but returns that proposal to the Suite decision; one DPF cannot settle it from inside its own edition.

#### Existing framework

A local practice framework already has an accepted architecture answer and a source record. Changing an example or publication carrier creates no new PFAD stage. Reopen only when its selected edition boundary, dependencies, initial pattern architecture, or publication or access consequence changes.

### E.4.PFAD:6 - Bias-Annotation

**Scope: limited.** This profile decides a later-used architecture boundary for an FPF-grounded framework, maintained adjacent result or service, thinner route, existing-framework contribution, or stop. It does not provide a universal product ontology, a service-design Method, a publication taxonomy, or a mandatory decision form for exploration.

The first drift is form-first decision making: a team starts from a schema, row, ADR heading, or status field and assumes that filling it has settled the architecture. Start from the reader's problem, alternatives, later-used boundary, and practical consequence instead.

The second drift is machinery-first entry: proposal, dependency, quality, naming, and publication apparatus appears before the reader knows whether a framework decision is needed. Keep that apparatus conditional on its own receiving use.

The third drift is slice-as-product: the small set currently being authored receives a broad DPF name before its field promise, several problem families, representative first use, omissions, and refresh boundary have been tested. Treat the slice as a seed or existing-framework contribution until the field-boundary assessment supports a DPF.

The fourth drift is architecture-by-layout: source rows, levels, chapters, or diagrams become the product structure. Recover the Methods, Work, subjects, descriptions, capabilities, providers, cultural change, and their actual relations first; use `C.32.MWA` when several structures must be reconciled.

The fifth drift is relation-by-representation: a table row or reference list is treated as the relation it records. State the relation directly; add a representation only when a named maintenance or checking use needs it.

| Lens | Declared bias and counter-check |
| --- | --- |
| **Gov** | Favors one later-used decision with explicit rationale, capable maintainers where needed, and a reopen condition. Counter-risk: every exploration becomes an approval exercise. Keep the cheap exit and require a DRR only when later work needs the settled boundary. |
| **Arch** | Favors comparison among framework, existing-framework contribution, maintained adjacent result or service, thinner route, and stop. Counter-risk: every useful result becomes its own framework or product. Select the smallest independently useful boundary and keep carriers, frameworks, services, programmes, and evidence packages distinct. |
| **Onto-Epist** | Favors direct subject kinds and actual identity, current-state, provision, maintenance, dependency, and publication relations. Counter-risk: the decision becomes an ontology inventory. Use *product* as Plain management wording, name only distinctions that change the answer, and return an unresolved-kind question rather than minting `U.Product`. |
| **Prag** | Favors representative first use, serious alternatives, evidence limits, omissions, and one next action. Counter-risk: product-line, service-management, bibliographic, or content-management apparatus dominates a small decision. Reuse only the external distinctions that discriminate among the live alternatives. |
| **Did** | Favors a recognizable working question and filled unlike cases before assurance detail. Counter-risk: compressed labels hide the object boundary, while formal precision hides the decision. State the ordinary alternative first, then explain the exact subject in one direct sentence. |

### E.4.PFAD:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-PFAD.1 Opening discriminator | A later-use field promise, edition, dependency, pattern-placement or material relation, non-framework direct-subject or maintenance boundary, or publication or access boundary makes the architecture question live. |
| CC-PFAD.2 Cheap exit | A suitable maintained non-framework result or service, route, existing-framework contribution, or stop that settles no such boundary closes without PFAD or a DRR. |
| CC-PFAD.3 One decision record | Decision Work selects a new or revised framework, contribution to an existing framework, maintained non-framework product, thinner publication or access route, or no new maintained product now; one ordinary `E.9` DRR records it. |
| CC-PFAD.3a Field boundary | A selected new or substantially revised DPF has a reviewed field-boundary assessment. It names the practitioner and a first use that needs no unpublished authoring context, connected problem families and results, what the FPF and admitted DPFs already provide, what remains uncovered, serious alternatives, representative cross-problem use, evidence limits, the decision that uses the assessment, and the later observation that reopens it. |
| CC-PFAD.3b Coverage, contributions, and omissions | The answer names selected problem-family pattern sets, first patterns and material relations, one representative cross-problem application, important omissions, and the sources to revisit for important claims; no count or authoring slice proves adequacy. For each load-bearing contribution that it keeps, merges, removes, reuses, profiles, supplies externally, or omits, it applies `E.8:4.1.3` and names the resulting action. An external return names the exact result and kind, supplying product and edition or current state, receiving use, discovery route, and material currentness or availability conditions, and says that the result remains external; an insufficient return remains a gap or omission. After a material promised-family change, the answer obtains the current `E.4.DPF.DA` `D12DomainProblemFamilyCoverageAdequacy` result for the resulting exact DPF or LPF edition and reuses it only while the exact edition and basis remain unchanged, without asking for evidence that someone revisited it. |
| CC-PFAD.3c Professional-practice projection and several structures | When professional Method coverage changes the answer, the same compact answer projects five connected groups by value: claim-scoped practice truth and first use; project and Method positions; selected structures and correspondences; pressures and evidence; and contribution, subtraction, gaps, and reopen. One answer may carry several bounded practice claims with different obtaining or possible-future status, and every selected question names the claim or claims it consumes. The answer, one ordinary E.9 DRR that records it, and the separately identified accepting decision remain distinct. A missing required group or claim-to-question binding returns a bounded PFAD gap before DPF authoring. `C.32.MWA` is used only when several selected structures do not line up one-for-one and `E.23.CDI` only when capability development changes the answer. The route never infers Method parthood from a contribution, transformation, performed Work, capability, provider contribution, or cultural change. A fixed view list, source layout, second record, or Method hierarchy does not pass this check. |
| CC-PFAD.3d Maintained-object boundary | *Product* remains Plain management wording. A selected maintained alternative names every direct subject and the identity, current-state, provision, or maintenance relation used by the answer. A programme case also separates provider and maintaining Systems, any admitted service state, bounded Work, and evidence-package epistemes. An unresolved kind remains an explicit question, not `U.Product`. |
| CC-PFAD.4 Compact payload | The DRR carries only the applicable content groups in `E.4.PFAD:4.2` and ordinary E.9 grounds and rationale; a maintained non-framework product, thinner route, or stop answer does not fabricate irrelevant fields. |
| CC-PFAD.5 Direct relation assertions | Relations among initial patterns are stated directly under their actual relation functions; no PFR row is required. |
| CC-PFAD.6 Object boundaries | Answer, acceptance, DRR, authoring Work, Method results, edition, and publication remain distinct; proposal locators identify none of them. For a programme answer, the exact persisting subjects, provider and maintaining Systems, any admitted service state, each bounded inquiry Work occurrence, and each evidence-package edition remain distinct. |
| CC-PFAD.7 Conditional apparatus | Naming, quality, admission, currentness, and package details appear only when they change the answer or serve a named use. |
| CC-PFAD.8 Reopen condition | The DRR states what change in field boundary, framework architecture, evidence, or receiving use requires reconsideration. |
| CC-PFAD.9 DPF Suite decision | A selected Suite answer states the ecosystem use, which product series may belong, Suite constitution, inclusion and removal rules, identity when product series change, maintenance commitment, source return and refresh conditions, exposure choice, alternatives, consequences, and reopen condition. It separately states edition-to-product belonging and whether the Guide product series has been constituted and included. Belonging establishes no holonhood, constructive parthood, dependency, or compatibility; a stronger claim needs its own complete predicate. |

### E.4.PFAD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| PFAD as a second decision | Authors reconcile an E.9 answer with another PFAD result. | Keep one answer selected by decision Work and recorded in one E.9 DRR; use PFAD only as the framework-specific profile. |
| Paperwork on the cheap exit | A curated route, suitable non-framework result or service, existing-framework contribution, or stop triggers a DRR without settling a later-used boundary. | Close the exploratory use directly. |
| Programme erased by a result-kind test | A continuing inquiry programme is called no product because it is not an episteme or publication package. | Keep the Plain programme-product boundary when it is useful, but name what actually continues: an admitted programme System or arrangement, or the current programme description, provider and maintaining Systems, commitments, and any admitted service state. Keep bounded Work and evidence-package epistemes separate. |
| Product word used as the alternative's kind | A programme, service, guide, registry, System, or episteme is selected as a generic Product without identifying the maintained subject. | Apply `E.4:4.1`; name the direct kind and relation, or keep the boundary proposed and return the unresolved question. |
| External management scheme decides the FPF boundary | A QMS product category, full service-management system, bibliographic model, or content-management process is copied into every alternative. | Reuse only the distinction that changes this decision and keep each claim under its direct subject pattern. |
| Authoring slice as framework | A few coherent current patterns receive a broad public field name. | Keep them as a seed or contribution until a field-boundary assessment, representative cross-problem use, omissions, and refresh boundary support a DPF. |
| Source layout as product architecture | Rows, chapters, levels, or diagrams are copied into pattern sets or DPF structure. | Recover the actual structures and relations; use `C.32.MWA` when they do not line up one-for-one. |
| Proposal locator as Method or edition | A proposal or evidence locator is treated as a Method, MethodDescription, accepted decision, or available FPF result. | Name the evidence, Method, description, decision, and edition separately. |
| Mandatory relation row | A PFR row is required before relations among initial patterns can be understood. | State each relation directly and add a row only for a named maintenance use. |
| ADR as decision | A publication projection is treated as the answer or acceptance. | Name the answer and acceptance separately; use ADR only as a projection. |
| Conditional detail made universal | Every decision must supply naming, quality, admission, currentness, and package records. | Include only details that change this answer or serve a named use. |
| Hidden Core change | A domain or local framework decision silently changes FPF Core meaning. | State dependency direction and keep Core changes in their own accepted decision. |

### E.4.PFAD:9 - Consequences

Authors get a recognizable framework question, one cheap stop rule, one readable decision account, and one next action. Later authors can recover the public field promise, problem-family coverage, representative use, edition boundary, dependencies, initial pattern architecture, omissions, sources to revisit, publication or access consequence, rationale, and reopen condition without reconciling two decision objects.

A new or substantially revised DPF carries more architecture work than a suitable non-framework product, thin route, or existing-framework contribution, and the PFAD profile adds one locator to maintain. That cost prevents a broad title, small authoring slice, source layout, or proposal locator from silently becoming a public pattern language. Conditional naming, package, quality, and machine-readable detail stays out until a named use needs it.

### E.4.PFAD:10 - Rationale

Framework authors need a recurring set of framework-specific questions, so removing every PFAD locator would make the entry harder to discover. They do not need a separate PFAD relation or record: `E.9` already carries one bounded answer, alternatives, rationale, consequences, action, and reopen condition.

The field-boundary assessment prevents a coherent slice from acquiring a field-scale identity without the practitioner coverage and independent use that justify it. The several-structure branch prevents one source layout from standing in for the practice architecture. Direct assertions preserve selected initial pattern relations without making their representation authoritative.

PFAD is therefore a profile by practical question and content, not a new ontological kind or a second stage.

### E.4.PFAD:11 - SoTA-Echoing

| Claim | Source and status | FPF use |
| --- | --- | --- |
| A family architecture needs a boundary for common and variable material, separate from a one-off result. | `ISO/IEC 26550:2015, Software and systems engineering - Reference model for product line engineering and management`, current confirmed edition, `https://www.iso.org/standard/69529.html`; and `ISO/IEC 26552:2019, Tools and methods for product line architecture design`, confirmed current in 2025, `https://www.iso.org/standard/43111.html`. The latter separates domain and application architecture design for a family rather than one system. | **Adapt** the family-versus-single-result question, common-use boundary, variation, and lifecycle comparison when splitting or merging a DPF is live. **Reject** software-product ontology, feature machinery, and the 61-page method-and-tool burden as a DPF threshold; practitioner problem families, first use, evidence, and maintenance still decide. |
| Product-line scoping practice compares product, domain, and asset boundaries together with technical and organizational constraints rather than treating one current slice as the field. | Marchezan de Paula et al., `Software product line scoping: A systematic literature review`, Journal of Systems and Software 186, 2022, `https://doi.org/10.1016/j.jss.2021.111189`. The review analyzes 58 studies and 41 approaches and derives a generic scoping process while reporting differing contexts and limits. | **Adapt** the same-grain comparison of field promise, reusable contributions, alternatives, organizational conditions, and evidence limits. **Reject** software assets, feature scope, or the generic SPL process as the ontology or mandatory method of a DPF; practitioner problems and use still decide. |
| An architecture description can cover products, product lines, families, and business domains while remaining distinct from the architecture and from architecting methods. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise - Architecture description`, current edition, `https://www.iso.org/standard/74393.html`. | **Use only as a boundary comparator:** keep the field or product architecture, the description that expresses it, and the Work and Methods that create or use it separate. **Reject** ISO 42010 as the starting ontology, an authoring Method, or evidence that a DPF field boundary is adequate. |
| Pattern discovery and validation need representative cases and explicit evidence limits beyond a broad name or pattern count. | Riehle, Harutyunyan, and Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, final publication 2025, `https://doi.org/10.1007/978-3-662-70810-1_6`; and Chuprina et al., `Towards an Approach to Pattern-based Domain-Specific Requirements Engineering`, 2024 academia-industry proof of concept, `https://arxiv.org/abs/2404.17338`. | **Adapt** representative cases, explicit evidence limits, and the question of what domain specificity changes. **Reject** a count as validation; do not require a full research programme at the cheap exit. Treat the 2024 line as promising proof-of-concept evidence, not authority for one universal field grammar. Reopen this choice if stronger current pattern-validation or domain-pattern evidence changes those decisions. |
| Distinct contribution, warranted retention, external-result use, and current package coverage are separate questions. | Current `E.8:4.1.3`, `E.4.DPF`, and `E.4.DPF.DA`; current FPF ground. | In `E.4.PFAD:4.2`, apply the same-situation action test, keep an external result honest about its product and receiving use, and obtain the `D12DomainProblemFamilyCoverageAdequacy` result only after a material promised-family change; reuse it only while the exact edition and basis remain unchanged. **Adapt** action-changing contribution evidence, external-result disclosure, and bounded package recheck. **Reject** label or count specificity, action change as sufficient proof of worth, and proof that a revisit occurred. Reopen this choice if the contribution test, external-result boundary, material package trigger, or exact-basis reuse condition changes. |
| Product and service management distinctions can expose different provider, interaction, currentness, and maintenance questions without creating one Product kind. | `ISO 9000:2026`, current quality-management vocabulary, `https://www.iso.org/standard/9000`; and `ISO/IEC 20000-1:2018`, confirmed current in 2023 with Amendment 1:2024, `https://www.iso.org/standard/70636.html`; compared by value in `E.4:11`. | **Adapt** the product-versus-service probe only when it changes a selected alternative, and separate provider and maintaining Systems from the service. **Reject** QMS vocabulary and a full service-management system as FPF ontology or default PFAD payload. |
| Publication and content architecture distinguish edition, expression, carrier, aggregation, content boundary, and lifecycle management. | `IFLA Library Reference Model`, July 2024 maintained edition, `https://repository.ifla.org/handle/20.500.14598/40.2`; and `ISO/IEC/IEEE 26531:2023`, current content-management standard, `https://www.iso.org/standard/81703.html`; compared by value in `E.4:11`. | **Adapt** edition-versus-carrier, snapshot return, content selection, and reuse when the alternative is a guide, package, registry, or combined carrier. **Reject** bibliographic entities and a component-content process as the ontology of programmes, services, Systems, or Methods. |
| One bounded decision account carries alternatives, rationale, consequences, action, and reopen condition. | Current `E.9`; current FPF ground. | Use one ordinary E.9 DRR rather than a PFAD-specific result kind. |
| A public DPF needs a practitioner-use and problem-family coverage answer rather than a pattern count or authoring-slice test. | Current `E.4`, `E.4.DPF`, and `E.4.DPF.DA`; current FPF ground. | Require the DPF field-boundary assessment, including what existing frameworks already provide and what remains uncovered, and expose important omissions without treating carrier prose as proof. |
| Several structures of one practice may be useful and need not line up one-for-one. | Current `A.22`, `C.30.AD`, and proposed `C.32.MWA`; current FPF architecture line. | Use a readable synthesis when those differences change the framework answer; do not copy a source hierarchy into the product. |
| A relation needs actual participants, an obtaining condition, identity when later use needs the occurrence, and a receiving use. | Current `A.6.RCD`, `A.6.REL`, and `E.10:0.0a`; current FPF ground. | Refuse a PFAD relation; state material initial pattern relations directly. |
| Direct framework statements precede optional rows or manifests. | Accepted R3 decision and current `E.4.PFR`; current FPF ground. | Keep PFR representation optional under a named maintenance use. |
| Framework editions, publications, forms, and carriers remain distinct. | Current `E.24.PUB`; current FPF ground. | Treat ADR-like text, sites, and PDFs as projections or publications, not as the decision or framework. |
| Compact ADR sections help preserve decision memory but do not supply FPF ontology. | Nygard, `Documenting Architecture Decisions`, 2011; historical lineage source, `https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions`; MADR, maintained template practice, `https://adr.github.io/madr/`. | Reuse concise question, alternatives, rationale, consequences, and supersession cues only when an ADR-like projection is useful. |

The external comparisons in this section are decision aids, not authorities over the FPF boundary. Recheck their current editions and the field's stronger post-2026 scoping practice when a source changes, when a new alternative could change the answer, or when project evidence shows that the selected boundary no longer supports first use.

### E.4.PFAD:12 - Relations

- **Uses:** `E.9` for the one bounded answer selected by decision Work and recorded in the DRR.
- **Uses:** `E.4`, `E.4.DPF`, and `E.4.DPF.DA` for framework scale, authoring, field coverage, and package assurance; uses `E.4:4.2` when one decision selects a maintained DPF suite and `E.11.DSG` when that suite has a separately maintained guide.
- **Uses:** `C.32.MWA` when several practice structures need one readable synthesis; uses `E.23.CDI` only when capability development for a named Work family changes the answer.
- **Uses:** `A.6.RCD`, `A.6.REL`, and the exact relation patterns for material relation assertions among initial patterns.
- **Coordinates with:** `A.22`, `C.30.STRAT`, `B.1.5`, `A.15.1`, `C.30.AD`, and `C.36` for selected structures and exact architecture distinctions.
- **Coordinates with:** `E.4.PFR` for optional relation and edition maintenance representations.
- **Coordinates with:** `C.32.PAD` for an exact project architecture decision, `C.32.ADR` for its ADR-like projection, and `E.17` with `E.24.PUB` for publication of an ordinary framework answer.
- **Coordinates with:** `F.18`, `G.2`, `G.11`, `E.21`, `E.23`, and `E.19` only when naming, source synthesis, refresh, improvement, or admission is current for the selected answer.

### E.4.PFAD:End

