## E.4 - FPF Ecosystem Family Architecture

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4:1 - Problem frame

Use this pattern when an FPF user, framework author, or steward needs to create, extend, or use an FPF-grounded pattern ecosystem and must know what belongs to FPF itself, what belongs to the FPF Core, what belongs to a domain or local framework, which records carry relation and edition claims, and which neighboring patterns contain the defining content for publication, access, naming, source, currentness, and quality work.

Primary `EntityOfConcern`: the FPF-grounded pattern ecosystem for one named ecosystem question. The first useful result is a direct route or honest stop: name the question, classify the likely case, and point to the next pattern. Open a complete ecosystem-architecture record only when the answer must settle durable architecture or support later reliance.

This pattern buys a practical distinction: a reader can tell whether a claim changes FPF itself as a first-principles framework edition, changes the FPF Core, creates a domain principle framework, creates a local practice framework, publishes or teaches existing content, exposes a skill-pack, index, or response carrier, or an MCP, retrieval, search, or assistant access route, or records a dependency on another framework edition. Use `E.4.FPF` when the work is the form of FPF itself; use `E.11` and `E.17` for first-entry and publication questions; use `E.4.DPF` when the work is to author a domain or local framework.

### E.4:2 - Problem

FPF has grown from a single core pattern set into an ecosystem of core rules, tools, companions, domain frameworks, local practice frameworks, source packs, decisions, quality records, publication and access-facing presentation carriers, and access routes. If those objects are described only by file names, abbreviations, or reader-facing tables of contents, several different kinds collapse:

- a pattern set is treated as a publication or access carrier;
- a local practice framework is treated as an FPF Core amendment;
- a relation record is treated as a method order;
- a dependency on a framework edition is treated as a specialization relation;
- a source or generated carrier is treated as architecture evidence without source-return and preservation claims.

The result is a framework that may look organized but cannot answer ordinary architecture questions: what structure is selected, what depends on what, what can change independently, what is preserved by a projection, and which stronger claim requires another pattern before it is used.

### E.4:3 - Forces

| Force | Tension |
| --- | --- |
| Core stability | The FPF Core must stay stable enough to supply dependable constraints to downstream frameworks, while domain and local frameworks need faster evolution. |
| Reuse and source-local meaning | Domain and local frameworks should reuse FPF Core distinctions, but they must not silently redefine Core meaning or treat a local label as a universal premise. |
| Publication pressure | Readers need all-in-one carriers, tables of contents, cards, examples, and first-entry material, but those carriers do not by themselves settle architecture. |
| Relation richness | Pattern ecosystems need recommendation, specialization, dependency, publication, preservation, evaluation, and source-use relations, but a single "related patterns" list hides the relation function. |
| Source and generation pressure | Source summaries, relation graphs, and generated candidate sets speed work, but their losses and admissible use must be declared before architecture work relies on them. |
| Problem-solving primacy | Frameworks need vocabulary and ontology, but a DPF is valuable only when those distinctions help a practitioner recognize typical problem situations and choose stronger solution moves. |
| Evolution pressure | Framework editions, dependencies, and names change over time, so compatibility, deprecation, supersession, and refresh conditions must be explicit. |

### E.4:4 - Solution

Describe an FPF-grounded pattern ecosystem as a family of framework editions and publication and access-facing presentation carriers, plus access routes, over selected structures. For each durable ecosystem-architecture claim, or technical claim on which later work will rely, state the exact subject and relation and cite the defining or constraining ClaimGraph in its subject pattern. The smallest route below needs no ClaimGraph citation when ordinary guidance or an honest stop already answers the question. A principle framework edition is not merely a bundle of documents, an ontology catalogue, a literature survey, or a guide to talking about a domain. Its pattern language renders a selected architecture of recurring problem situations, forces, known failure modes, reusable SoTA solution moves, consequences, cases, relation records, evaluation methods, and refresh conditions for a declared reader and use. Known failure modes include beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice.

Start with the smallest route that answers the current question:

1. Name the concrete ecosystem question and who needs the answer.
2. Classify the likely case: a framework-family boundary, an adjacent maintained result, a publication carrier, access-facing presentation carrier, or access route, a DPF-suite question, or another relation already handled by a direct pattern.
3. Point to that direct pattern and state the next useful move, or stop with the exact missing distinction.
4. Open the complete ecosystem-architecture record only when the answer must persist as ecosystem architecture or later work must rely on the selected structures and relations.

This route is ordinary guidance, not a new record or package. A direct pattern or honest stop is a complete first result when no durable ecosystem-architecture record is needed.

Create an ecosystem-architecture record only when that durable architecture or later reliance is current. Use these fields:
```text
FPFEcosystemArchitectureRecord@Context:
  ecosystemScopeRef
  intendedArchitectureUse
  claimScopeRef?
  sourceRefs?
  patternHostRefs?
  selectedArchitectureStructureRefs?
  publicationRelationRefs?
  boundedModelUseStructureRef?
  frameworkFamilyMembers
  selectedPatternSetRefs
  selectedProblemSituationStructureRefs
  selectedKnownFailureModeRefs
  selectedSoTASolutionMoveRefs
  selectedSolutionMoveStructureRefs
  selectedRelationRecordRefs
  frameworkCarrierRenderingRefs
  selectedDependencyAndEditionRefs
  selectedPublicationOrAccessCarrierRefs
  selectedSourcePackRefs
  selectedDecisionRefs
  qualityAndImprovementRefs
  currentnessAndRefreshRefs
  blockedOverreadRefs
  dependentUsePatternLocators
```

This record answers the declared ecosystem question for its intended use. It is not a new root kind, a source of semantic locality, or a substitute for the subject claims and patterns it cites.

Classify the family members as follows:

`Conceptual Core` is the legacy authority and publication-family partition. `First Principles Framework edition` is the whole scoped FPF framework edition as a transdisciplinary first-principles framework. `FPF Core pattern set` is the framework-edition view of the general FPF Core used for dependency, relation, and edition reasoning. These are related views and scopes, not competing core objects.

| Family member | Architecture contribution | Authoritative content loci |
| --- | --- | --- |
| Conceptual Core | Core FPF distinctions, rules, and patterns that other FPF-grounded frameworks depend on. | `E.4`, `E.5.3`, and the exact subject patterns containing the defining ClaimGraphs |
| Tooling Reference | Optional tools, schemas, scripts, machine checks, or helper publications that inspect or support FPF use. | Use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, and relevant tool patterns for their declared tool functions; use `G.5` only for a selector-facing selected-tool-set result declaration. |
| Pedagogical Companion | Tutorials, playbooks, worked examples, and learning material that teach FPF without changing Core meaning. | `E.17`, didactic patterns |
| Foundational principle pattern set | Foundational threshold material or principle patterns that may support FPF-grounded use but need settled names and dependency boundaries. | `F.18`, `E.4.PFR` |
| First Principles Framework edition | The scoped FPF framework edition as a transdisciplinary first-principles framework with Core pattern set, publication and access-facing presentation carriers, access routes, relation records, and whole-FPF adequacy route. | `E.4.FPF`, `E.2.DA`, `E.4.PFR`, `E.11`, `E.17`, `G.11` |
| FPF Core pattern set | The current general FPF pattern core as a framework edition. | `E.4`, `E.5.3`, and the current Core subject-pattern descriptions and defining ClaimGraphs |
| Domain principle framework | A domain-bounded framework grounded in FPF and in domain SoTA. | `E.4.DPF`, `G.2`, `E.4.PFAD`, `E.4.PFR` |
| Local practice framework | A framework for one bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—grounded in FPF and often in a domain framework. Add a local system-role kind, a separate System-classification judgment, or an exact assignment occurrence only when the framework claim independently uses it; recover ambiguous *role* wording through `E.10.ROLE`. | `E.4.DPF`, `E.4.PFAD`, `E.4.PFR`, `G.11` |

#### E.4:4.1 - Place support units and adjacent products deliberately

In this pattern, *product* is Plain management wording for a deliberately maintained result or service boundary. It is useful because it makes a team decide intended use, identity or current state, access, maintenance, refresh, and retirement together. It is not one FPF technical kind and it creates no `U.Product`. Before making a product-boundary claim, name the direct subject—the thing the claim is about—and the relation that carries its identity, edition, current state, provision, or maintenance. The subject may be, for example, a framework-edition episteme, an evidence-package episteme, an admitted System, an admitted service arrangement, a Method, a programme-description episteme, or another result already admitted by its subject pattern. If the direct kind or relation is not settled, keep the management boundary as a proposal and return that exact question instead of inventing a common object kind.

A framework edition is an exact episteme. Treat its Readme, Preface, table of contents, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route as named publication units in the same managed boundary when they share the edition's declared readers and use, edition boundary, access, maintainer, and change cadence. Being outside the pattern set or in another file does not by itself create another maintained result.

Make a separate adjacent product only when people need to change, cite, use, or maintain its direct subject independently. Look for an independently useful identity, edition or current state, named users and use, an intensional rule for what belongs, access, a maintenance commitment, a refresh or retirement rule, or cross-framework reuse or reliance. For example, a registry, MethodDescription collection, decision-support publication, inquiry evidence package, practitioner guide, pedagogical companion, catalogue, tool reference, access service, or inquiry programme may justify a separate boundary. The label does not settle the kind: a guide or evidence package may be an editioned episteme; a tool reference may identify an episteme, a tool System, or both; and an access service needs its own service and provider-System claims. The list is open, and file location does not decide the boundary.

When the direct subject is independently maintained, keep it separate and point from the framework to its exact edition or current state. An annex may carry a declared snapshot or projection, but it returns to the authoritative subject and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, keep it as a named support publication unit of the framework edition.

One presentation carrier may expose several managed products without merging their direct subjects. Each constituent keeps its own identity, edition or state, form, access, maintainer, and refresh relation; the outer navigation names exact constituents and stays neutral. A result reused by several DPFs may therefore be managed as an ecosystem companion or service product. Shared use does not make it a parent DPF. Open another DPF only when its own field-boundary assessment finds recurring practitioner problems, constructive Methods, an independently useful first cut, evidence practice, and a maintenance boundary.

When *programme* is used, start with what actually continues. An inquiry programme may be managed as a continuing programme or service product, but neither label says what persists. If a subject pattern admits the programme as a System or another exact arrangement, name it. Otherwise name the current programme-description episteme, capable provider and maintaining Systems with their accepted commitments, and any admitted service state. Bounded inquiry projects remain separate Work occurrences, and their results remain separate epistemes. A maintained inquiry evidence package is its own editioned episteme. The management boundary may coordinate these subjects and relations, but it does not turn them into one indefinitely continuing `U.Work` or one generic Product. If the persisting arrangement is still unclear, return that exact architecture question.

DRRs, build manifests, quality runs, digests, logs, and campaign state remain maintainer or process evidence by default. They become reader products only when a separately selected public use gives a direct subject its own maintained boundary.

Use these tests in order: name the intended managed boundary and ordinary use; identify every direct subject, its kind, and the identity or current-state relation used by the decision; group only publication units that share the framework edition, readers, access, maintainer, and cadence; test a proposed adjacent subject for independent use and maintenance; select the smallest useful boundary; then record exact pointers, snapshot return, and neutral-carrier navigation. If a needed kind or relation remains unresolved, record that question and stop short of the technical product claim.

#### E.4:4.2 - Keep several DPF products usable as one suite

Use this branch when independently maintained DPF products contribute to one ecosystem and people need to recover which product series belong to the Suite and how to use them while each product changes on its own. Keep three subjects distinct: each continuing DPF or Guide product series, the continuing DPF Suite collection, and any as-of description of that collection. This introduces no `U.Product` or `U.DPFSuite` kind.

Here *DPF product series* is Plain relation-defined wording for a continuing collection of a DPF's edition epistemes. The series begins only when a product-constitution decision names at least one existing edition, intended readers and use, content-selection and edition-admission rule, access, refresh and retirement conditions, reidentification rule, and a capable maintaining System whose maintenance commitment has been accepted. The decision's effect begins the collection and admits the first edition; its Work and record are not the product series or the belongs-to occurrence.

Say **“this edition belongs to this product series.”** A later edition joins only when its `EpistemeEditionRelation` to the actual source edition obtains, the product-series rule still holds, and an admission decision takes effect. The edition relation establishes episteme continuity but does not admit the edition to the product series. A parallel branch, fork, translation, or derivative joins only when both its source relation and the admission rule pass. Otherwise it remains a related episteme outside the series or begins another product series. The series need not be one total version order.

An admitted edition continues to belong historically when it becomes superseded, unavailable, non-current, or retired while the same product series continues. Those states do not end the occurrence. If the product series ends or its identity rule identifies another product series, belonging to the old series ends and remains a past fact. Another product series must admit the edition through its own decision and a new occurrence. If review shows that the edition never satisfied the admission rule, correct the false claim; no valid occurrence existed. Do not remove and re-admit the same edition merely because availability or currentness changed. The same edition and continuing product series keep one occurrence rather than starting another.

A **DPF Suite** is a continuing collection of DPF product series. The DPF Suite Guide product series can also belong after its own constitution and inclusion. The Suite rule states which product series may belong; individual editions do not. The Suite begins when a constitution decision identifies the ecosystem purpose and intended use, inclusion and removal rules, reidentification rule, maintenance conditions, and a capable maintaining System whose Suite-maintenance commitment has been accepted, and includes at least one actual DPF product series. The decision Work and record remain distinct from the Suite and the first inclusion occurrence.

The same Suite continues while its ecosystem purpose, rule for which product series may belong, inclusion and removal rules, and maintenance and identity conditions remain within the declared evolution rule. Adding or removing a product series normally preserves it, as can an explicit maintenance transfer that preserves those conditions. Changing an edition, publication, availability fact, Guide, or configuration description does not by itself reidentify the Suite. Changing an identity anchor outside the rule identifies another Suite.

After constitution, a temporary one-product-series or empty state can preserve the same Suite only when an explicit decision keeps those anchors in force and names a restoration, review, or retirement condition. Present no current cross-DPF answer in that state. An end or retirement decision closes the continuing collection and ends every current belongs-to occurrence; separate removals are unnecessary. The Suite and the past facts remain identifiable, but later active use requires another constitution decision, another Suite, and new inclusions. Before constitution there is only a possible-future Suite.

Say **“this product series belongs to this DPF Suite.”** The relation begins when the product series satisfies the operative inclusion rule and an inclusion decision takes effect. It remains current while the same product series and Suite continue and no later removal decision has taken effect. While they continue, only an effective inclusion or removal changes that occurrence. If either collection ends, or its identity rule identifies another collection, belonging to the old collection ends; neither case requires a prior removal. A proposal, description, publication, locator, or common use may report the relation but does not make it obtain.

Loss of qualification does not silently change belonging. Show an action-changing warning and decide whether to repair qualification, remove the product series, change the Suite under its identity rule, or retire it. Until that decision, do not present the product series as qualifying, current for the defeated common use, or recommended on that basis. Restoration before removal keeps the same occurrence while the same product series and Suite continue. An effective removal ends it; a later inclusion begins another occurrence.

After an occurrence ends, say that the product **belonged** to the Suite and say when it ended; do not present past belonging as current. A reconstituted product series or Suite, or one reidentified under its rule, is another collection and needs a new inclusion decision and occurrence.

Belonging alone establishes neither parthood nor holonhood, and it does not make either impossible. The current product-series and Suite definitions leave A.1 matters 3, 5, and 6 unsettled: no constructive part relation and assembly, composition-grounded whole characteristic, or possible participation in a larger constructive assembly is currently established. Treat both as continuing collections without a present holon or parthood claim. If a later complete A.1 result and direct part predicate pass, state that additional claim separately. Belonging also settles no relation about order, dependency, compatibility, recommendation, publication, availability, currentness, maintenance, or use in an answer. One product series may belong to several Suites. Use the direct sentence without assurance fields unless the publication elects `B.3.5`; after election, use its `validationMode=axiomatic` and current `C.13 set`-trace obligations without treating the trace as the cause.

The DPF Suite Guide product series belongs to the Suite after its own inclusion decision and keeps its own reader use and maintenance conditions. It may join after the first DPF products; it did not belong beforehand. Its absence, unavailability, staleness, or non-use does not erase the Suite or block direct use of a known DPF result; it only prevents a claim that the Guide currently supplies a trustworthy cross-DPF route.

For a reproducible as-of answer, use an optional **DPF Suite configuration description**: a `U.Episteme` about the Suite, the product series that belong at that time or in that scope, selected editions or states, and direct source return. Its own editions are description editions, never Suite editions. It describes neither the belongs-to occurrences into existence nor the Suite's identity.

Use `G.5 JointUseSet` only when every identified result or edition is necessary for one bounded use. A question may need resources from only some product series in the Suite. The set therefore neither defines Suite identity nor implies that every product is used together.

Present the Suite as currently maintained only while a capable System holds its Suite-maintenance commitment and readers can return to the collection identity, inclusion and removal decisions, and any product-series state claimed as current. A neutral carrier or Guide may expose those returns, and an optional configuration description may pin them, but none merges the Suite, Guide, product series, edition, carrier, access, maintenance, or currentness. Apply `E.17`, `E.24.PUB`, `C.2.P`, and `G.11` to their direct claims; use `E.4.PFR` only for a dependency or compatibility relation that separately obtains; and use `E.11.DSG` for the Guide's problem-led route and direct-DPF bypass.
The ordinary method is:

1. Declare the ecosystem scope and intended architecture use. Cite the exact source, pattern host, selected architecture structure, publication relation, or bounded model-use structure only when the record actually relies on it.
2. Name the family member being created, used, or changed.
3. List the selected structures that matter for the architecture claim: recurring problem-situation structures, known failure modes, reusable SoTA solution-move structures, pattern set, pattern-use relations, pattern-framework relations, decision records, dependency and edition records, publication and access-facing presentation carriers, access routes, source packs, quality records, and currentness records. For PF work, the pattern-language publication carrier exposes a reader-facing expression of that problem-and-solution architecture, not a neutral list of topics.
4. If the family member is FPF itself as a framework edition, open `E.4.FPF` for form, presentation carriers, access routes, and whole-FPF adequacy routing.
5. Apply `E.5.3`: dependencies point toward more stable framework editions. FPF Core does not depend on domain or local frameworks.
6. State publication and first-entry claims using `E.11` and `E.17`; state framework-carrier structure-account assertions using `E.4.FPF` for FPF itself or `E.4.DPF`/`E.4.DPF.DA` for domain and local frameworks.
7. State pattern-use recommendation claims using `E.11.PUR`.
8. When a framework-architecture question is open, record the selected answer in one `E.9` DRR and use `E.4.PFAD` to profile its framework-specific content. Use `C.32.PAD` only for an exact project architecture decision and `C.32.ADR` only to project such a decision into an ADR-like publication.
9. State relation, dependency, compatibility, deprecation, and edition claims using `E.4.PFR` only when its named maintenance use requires that representation; otherwise use the direct subject assertion.
10. Settle names using `F.18`.
11. State SoTA and source-use claims using `G.2`.
12. State currentness, refresh, and edition-change claims using `G.11`, the exact edition values, and their source/currentness assertions.
13. Before using an all-in-one carrier, table of contents, relation graph, summary, skill pack, MCP-backed service, or generated carrier as evidence, state the exact source-return or preservation assertion under the predicate defined in `C.33`, `C.34`, or `C.35`.
14. Evaluate whole-FPF adequacy through `E.2.DA`, DPF or local-framework package adequacy through `E.4.DPF.DA`, individual pattern quality through `E.21`, improve through `E.23`, and use `E.19` only when the local process asks for admission review.

Use this routing table when a proposed change is ambiguous:

| Proposed work | Route to | Blocked overread |
| --- | --- | --- |
| The form of FPF itself changes: README, Preface, ToC, monolith, host set, skill pack, MCP-backed access, or whole-FPF publication/access route. | `E.4.FPF`, with `E.2.DA` for whole-FPF adequacy and `E.4.PFR` for relation or edition records. | Do not treat FPF as a DPF, do not use `E.4.DPF.DA` for whole-FPF adequacy, and do not treat a carrier as the framework edition. |
| Accepted changes are being assembled into an FPF, DPF, or LPF publication, or continuity with a predecessor publication is claimed. | `E.4.PFIP` for the accepted-source and predecessor-preservation comparisons. | Require both PFIP conclusions when both claims are made. Source parity, build success, carrier continuity, and package adequacy answer narrower questions. |
| A distinction or rule is intended to constrain ordinary FPF use across many domains and downstream frameworks depend on it. | An accepted FPF Core amendment decision under `E.9`, followed by the exact subject patterns whose assertions change. | Do not promote a local checklist or domain technique to Core merely because it is useful. |
| A reusable principle supports FPF-grounded work but is not a general Core rule for all domains. | Foundational principle pattern set or other named framework edition, with `E.4.PFR` dependency records. | Do not hide a new framework edition inside the Core table of contents. |
| A source tradition or professional domain needs FPF-shaped patterns. | Domain principle framework through `E.4.DPF`, `G.2`, `E.4.PFAD`, and `E.4.PFR`. | Do not treat a literature summary as the framework. |
| One bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—needs guidance. | Local practice framework through `E.4.DPF`; keep local source, publication, quality, and refresh records, and state separately any direct relation used for maintenance, responsibility, authority, assignment, or contact. If a load-bearing owner label has no current direct relation, return `missing-governor` instead of inventing one. | Do not make local policy a general FPF rule. |
| Material needed for ordinary framework use shares the framework edition, readers, access, maintainer, and change cadence. | Keep it as a named support publication unit of that exact framework edition and expose it through the edition's carrier route. | Do not create another managed product merely because the unit is outside the pattern set or stored separately. |
| A registry, guide, evidence package, service, programme, or other result has an independently useful identity or state, users and use, content boundary, access, or maintenance and refresh boundary. | Name its direct subject and the relevant relation, keep a separate managed boundary, and point to the exact edition or state; any embedded snapshot returns to that authority. | Shared use, co-location, or one outer carrier does not merge direct subjects. If the kind is unresolved, keep the boundary proposed and return the question. |
| One carrier exposes several managed products. | Keep the outer carrier neutral and retain each direct subject's own form, identity, access, and maintenance relation. Use `E.11.PFP` only for FPF, DPF, or LPF constituents. | Do not give a non-framework subject a framework family, dependency field, or pattern index. |
| Several DPF product series and a Guide product are proposed for one ecosystem. | Use `E.4:4.2` to decide product-series and Suite constitution, which editions belong to which product series, which product series belong to the Suite, identity through change, maintenance, optional configuration description, and truthful exposure; use `E.4.PFAD` when the answer must be selected. | A title, co-list, shared carrier, Guide entry, or configuration description creates none of those subjects or relations. |
| Existing material is hard to find, teach, or publish. | Use `E.11` for discovery, the relevant didactic pattern for teaching, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use `G.5` only when the missing value is a selected-set result declaration. | Do not call publication repair architecture repair. |
| A cross-reference claims use, specialization, dependency, publication, source reuse, preservation, quality, deprecation, or supersession. | `E.4.PFR` for the relation function and edition effect. | Do not let a link label decide the relation meaning. |
| A framework split, dependency boundary, presentation-carrier or access-route choice, or adoption consequence must be decided. | Record one selected answer in an `E.9` DRR, using `E.4.PFAD` for its framework-specific content. Use `C.32.PAD` only when the decision is an exact project architecture decision and `C.32.ADR` only for its ADR-like projection. | Do not replace the answer with a diagram, folder, manifest, PFAD relation, or project-specific decision pattern used as the default framework route. |
| A source, search result, transformed view, or generated carrier supplies candidate material. | `G.2`, `C.33`, `C.34`, or `C.35` before architecture use. | Do not treat a carrier as authoritative because it has plausible names. |
| Whole-FPF adequacy, DPF package adequacy, individual pattern quality, repeated improvement, admission gating, or currentness is the live problem. | `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23`, `E.19`, and `G.11` according to the claim. | Do not average pattern scores into package adequacy or whole-FPF adequacy, and do not run all quality gates when only one evaluation or refresh question is live. |

This pattern should leave the reader with one architecture sentence: "This framework edition belongs to this family member, expresses this selected architecture of recurring problems and solution moves in pattern-language form, depends on these stable editions, publishes or gives access through these carriers, preserves these selected structures, and states each neighboring claim under its exact predicate or constraint with the subject pattern available as a locator."

### E.4:5 - Archetypal Grounding

Tell: A team creating a hydroponic-cucumber domain principle framework should not place every useful crop-growing rule into `FPF-Spec.md`. It creates a domain framework edition grounded in FPF Core and horticulture SoTA, declares its dependency on an FPF Core edition, records its source packs, drafts domain patterns under `E.8`, and publishes an all-in-one publication carrier for growers or agronomists.

Mini-example:

| Record field | Filled slice |
| --- | --- |
| `ecosystemScopeRef` | `HydroponicCucumberPrincipleFramework@GreenhouseCropDomain` |
| `intendedArchitectureUse` | choose the framework-family, dependency, and publication architecture for the hydroponic-cucumber framework edition |
| `sourceRefs?` | source entries cited by `GreenhouseControlSourcePack@2026Q2` and `CropProductionSourcePack@2026Q2` |
| `patternHostRefs?` | `DPF.GROW.NutrientSolutionMonitoring` and `DPF.GROW.ClimateControlInterpretation` |
| `selectedArchitectureStructureRefs?` | recurring crop-growing problem situations, solution moves, dependency direction, and source-return structure used by this record |
| `publicationRelationRefs?` | the publication relations from `HydroponicCucumberPF@2026Q3` to `GrowerCarrier@2026Q3` and `GrowerReadme@2026Q3` |
| `frameworkFamilyMembers` | domain principle framework; local grower practice framework as a later dependent edition |
| `selectedPatternSetRefs` | crop-growth problem framing, nutrient-solution monitoring, climate-control interpretation, harvest-quality feedback patterns |
| `selectedRelationRecordRefs` | source or decision reuse from horticulture source pack; specialization from general FPF authoring patterns; publication relation to all-in-one carrier |
| `selectedDependencyAndEditionRefs` | depends on `FPFCorePatternSet@Edition`; no reverse dependency from FPF Core |
| `selectedPublicationOrAccessCarrierRefs` | domain all-in-one publication carrier plus readme as first-entry carrier |
| `selectedSourcePackRefs` | greenhouse-control and crop-production `G.2` source packs |
| `qualityAndImprovementRefs` | `E.21` pattern-quality evaluation and `E.23` improvement loop for drafted domain patterns |
| `currentnessAndRefreshRefs` | `G.11` refresh condition when source pack, Core edition, or crop-production practice changes |
| `blockedOverreadRefs` | do not read the publication carrier as the architecture itself; do not read domain patterns as FPF Core changes |

Show: A Codex-process local practice framework may depend on FPF Core and selected architecture-domain patterns. Its handoff patterns, prelanding patterns, and process runbooks can be local framework material. They do not define the FPF Core merely because they use FPF vocabulary and are useful to this workspace.

Show: A generated relation graph over pattern names can help inspect missing relation records. It becomes architecture input only after `C.35` admits the carrier and `E.4.PFR` records the relation functions. The graph's shape alone is not the ecosystem architecture.

Show: In the cucumber DPF, the Readme, table of contents, pattern collection, and coverage account share one framework edition, reader use, access route, maintainer, and cadence, so they remain publication units in one managed boundary. A greenhouse-calibration source registry is revised separately and reused by another crop DPF, so its current registry edition is a separate episteme. One web carrier may expose both, but its links neither merge their identities nor create a generic Product relation.

### E.4:6 - Bias-Annotation

**Scope: limited.** This pattern helps make architecture claims about FPF-grounded framework ecosystems and their maintained publication, access, companion, and service boundaries. It does not supply a universal product taxonomy, a service-design Method, a programme ontology, or a complete content-management system.

The recurrent drift is publication-first architecture: the visible file, all-in-one carrier, card deck, table of contents, or graph is treated as the architecture because it is what a reader sees first. The repair is to name the selected structures and dependency direction first, then use publication patterns to expose them.

Another recurrent drift is Core absorption: useful domain or local material is pulled into the Core because it is well written or broadly reusable. The repair is to ask which domain or local situation the claim addresses and which framework edition should depend on which more stable edition.

| Lens | Declared bias and counter-check |
| --- | --- |
| **Gov** | Favors an explicit intended use, capable maintainer, accepted maintenance commitment, currentness rule, and retirement response. Counter-risk: a useful grouping becomes a mandatory governance form. Keep only claims that change identity, access, maintenance, refresh, or retirement, and use the relevant decision pattern for authority. |
| **Arch** | Favors separating framework editions, support publication units, adjacent results, services, programmes, DPF lines, and carriers before composing them. Counter-risk: decomposition multiplies managed boundaries. Choose the smallest boundary that preserves independent use and maintenance, and let a neutral carrier expose several exact constituents without merging them. |
| **Onto-Epist** | Favors a direct subject kind and identity or current-state relation before technical use of *product*. Counter-risk: an ontology catalogue replaces ordinary architecture work. Keep *product* as Plain management wording, name only distinctions used by the decision, and return an unresolved-kind question rather than minting `U.Product`. |
| **Prag** | Favors observable independence in use, access, maintenance, refresh, and reliance over labels or file layout. Counter-risk: a small guide or service inherits a quality-management, service-management, bibliographic, or content-management regime. Apply the cheapest direct boundary test that can change the decision. |
| **Did** | Favors familiar product wording at first recognition, followed immediately by the exact subject when a technical claim is made. Counter-risk: readers copy the examples as a closed taxonomy. Treat every list as illustrative and make the direct case recoverable in ordinary project language. |

### E.4:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-E4.1 First route and family case | The work names the ecosystem question, classifies the likely case, gives the direct next pattern or honest stop, and opens a complete ecosystem-architecture record only when durable architecture or later reliance needs it. When a record is needed, it names whether the family member is Core, Tooling Reference, Pedagogical Companion, a foundational principle pattern set, a First Principles Framework edition, FPF Core, a domain principle framework, or a local practice framework. |
| CC-E4.2 Selected structures named | The ecosystem-architecture record names its intended use and the problem-situation, known-failure, SoTA solution-move, pattern-set, relation, decision, publication, access, source, quality, dependency, and currentness structures that matter for the claim. Cite a source, pattern host, publication relation, or bounded model-use structure only when the record uses that independently established value. |
| CC-E4.3 E.5.3 respected | Dependency direction points toward more stable framework editions, and Core does not depend on domain or local frameworks. |
| CC-E4.4 Publication and access separated | All-in-one and access-facing carriers, publication units and forms, tables of contents, cards, Readmes, skill packs, MCP or retrieval routes, assistant integrations, actual access, and views remain non-interchangeable; apply the direct pattern to each claim about them. |
| CC-E4.5 Exact predicate and assertion named | Pattern-use, relation, dependency, decision, naming, source, currentness, quality, and preservation claims each name their exact predicate and subject assertion; a pattern identifier is only the locator for the next question's defining or constraining ClaimGraph. |
| CC-E4.6 Source-return present | Any carrier used as architecture evidence states captured structure, lost structure, admissible use, and the source to return to. |
| CC-E4.7 Framework carrier structure-account explicit | A Readme, Preface, ToC, all-in-one carrier, skill-pack carrier, or other form-bearing framework carrier states which framework structures its selected form exposes for whom. An MCP, retrieval, search, or assistant route identifies the first form-bearing carrier or response it reaches and returns to the same account; it is not scored as that carrier. Missing form or adequacy content is repaired as an exact assertion using `E.4.FPF`, `E.4.DPF`, or `E.4.DPF.DA` before adoption or adequacy claims are made. |
| CC-E4.8 Product boundary proportional and typed | *Product* remains Plain management wording. Every boundary names its direct subjects and the identity, edition, current-state, provision, or maintenance relations used by the decision. Framework support units share one boundary only when their edition, use, access, maintainer, and cadence agree; an adjacent subject has an independent use and maintenance reason. Shared use and one carrier are only probes. An unresolved kind is returned as a question, not `U.Product`. |
| CC-E4.9 DPF Suite truth | The Suite is one constituted collection of DPF product series and, after inclusion, the Guide product series. Product and Suite constitution, edition-to-product belonging, Suite inclusion and removal, decision effects while the same product and Suite continue, what happens when either ends or is reidentified, past belonging, identity anchors, maintenance, a temporary empty state, retirement, and any configuration description remain recoverable. No snapshot, list, Guide, carrier, or `JointUseSet` substitutes for them. |

### E.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Core absorption | A domain or local framework is placed into the FPF Core because it is useful. | Create a separate framework edition with dependency records under `E.4.PFR`. |
| File tree or package manifest as architecture | A folder layout, package descriptor, or manifest is read as the ecosystem architecture. | Use the file or manifest only as a carrier; recover the ecosystem-architecture record, relation records, dependency records, source packs, quality records, exact presentation carriers, access routes, and refresh routes. |
| Publication-only architecture | A table of contents or all-in-one carrier is used as the architecture description. | Add an ecosystem-architecture record and source-return note, then constitute the exact practical-entry and publication assertions under the predicates defined in `E.11` and `E.17`. |
| Ontology or talk guide as framework | A framework names domain entities, terms, or conversation moves but does not identify recurring domain problems, known failure modes, SoTA solution moves, and worked repairs. | Keep the ontology, glossary, or communication guide as support material; create or repair the framework around problem situations, solution moves, cases, and quality routes. |
| Relation flattening | Every cross-reference is treated as the same relation. | Use `E.4.PFR` to state relation function and subject pattern. |
| Outside the pattern set means another product | A Preface, coverage account, or refresh note is given a separate product identity although it shares the framework edition's users, access, maintainer, and cadence. | Keep it as a named support publication unit unless an independent use and maintenance boundary is useful. |
| Product label used as an object kind | A guide, service, programme, registry, System, or episteme is asserted to be the same kind because each is managed as a product. | Keep *product* as Plain management wording. Name each direct subject and the relation used for identity, current state, provision, or maintenance; return an unresolved-kind question when needed. |
| Shared carrier or shared use means one product | A cross-framework registry or service is absorbed into one DPF, or a combined carrier merges a framework and catalogue. | Decide each managed boundary from direct subjects, use, and maintenance; keep exact constituent pointers and let the outer carrier remain neutral. |
| Service or publication scheme used as universal architecture | A full service-management system, bibliographic entity model, or content-management process is imposed on every framework unit, programme, guide, or tool. | Reuse only the distinction that answers the current boundary question; keep service, publication, content, and programme claims under their own subject patterns. |
| DPF list presented as a Suite | A title or co-list replaces product-series constitution, the Suite-constitution decision, the direct belongs-to occurrences, identity rules, and maintenance conditions. | Keep a proposal until `E.4:4.2` passes; then identify the Suite collection and the product series that belong to it. |
| Suite belonging inflated | Two product series belong to the same Suite, so the text infers order, dependency, compatibility, maintenance, publication, or co-use. | Keep the Suite claim at product-series grain and apply the direct predicate for every stronger claim. |
| Source-carrier authority | A summary, graph, or generated candidate set is treated as authoritative. | Admit the carrier through `C.35` or record preservation through `C.33` and `C.34` before use. |

### E.4:9 - Consequences

This pattern makes FPF ecosystem work slower at the beginning because a framework author must name family membership, dependency direction, selected structures, and the patterns needed for neighbouring claims. The gain is that later work can evolve without hidden Core changes, hidden publication substitutions, or hidden source loss.

It also makes some attractive names and short labels provisional until `F.18` settles them. That cost is intentional: short names are useful only after the value being named, its source-local meaning, and its intended use are explicit.

### E.4:10 - Rationale

The ecosystem needs architecture because FPF patterns, frameworks, source packs, exact presentation carriers, access routes, quality records, and decisions are not one kind of object. A file tree cannot preserve the differences among those objects. A relation graph cannot preserve decision rationale or dependency compatibility. An all-in-one publication carrier, callable access route, or returned access-facing carrier cannot preserve all source-return and currentness obligations by itself. Architecture work must therefore name the selected structures and apply the relevant pattern to claims outside this pattern's scope.

The old Core, Tooling Reference, and Pedagogical Companion distinction remains valuable, but it is only one family partition. Domain and local principle frameworks need their own framework editions so they can depend on Core without redefining it.

### E.4:11 - SoTA-Echoing

#### E.4:11.1 - Continuing product-series and Suite collections

`A.14:14` gives the general constructional comparison. This branch applies only its product-ecosystem consequences.

| Question | E.4 answer |
| --- | --- |
| Current source pressure | The BORO constructional turn and C-FORS distinguish set, sum, tuple, and assembly constructions; Core Constructional Ontology requires explicit constructors and identity choices; Fine's composition work keeps the operation prior to a derived part claim; Fine's social-group account shows how structured subjects may keep identity while participants change. BORO is the implemented-lineage comparator; the 2024–2025 constructional applications remain research comparators rather than demonstrated applied maturity. |
| Adopt or adapt | Keep each product series and Suite as a continuing subject under its declared identity rule while editions or included product series change. State edition admission, edition-to-product belonging, product-series inclusion or removal, and Suite identity as separate conditions. A.14 supplies the general belongs-to and parthood boundary. |
| Reject | Do not use one generic `MemberOf`, a qualified generic collection predicate, a fixed-extent identity, or automatic constructive parthood. Those shortcuts hide the different product and Suite conditions or make change of constituents decide identity by itself. |
| Present result and reach | `E.4:4.2` uses the two ordinary belongs-to sentences and their separate constitution and decision rules. The present definitions leave `A.1` matters 3, 5, and 6 unsettled, so product series and Suite remain collections with holonhood undecided, not prohibited. A later direct part claim remains possible after a complete `A.1` result. `CC-E4.9` checks that this identity, change, decision, and history account remains recoverable. |
| Comparable-effort trade-off | The ordinary sentences plus the existing `E.10` and `A.14` route are no worse for correctness or temporal history and are cheaper for a cold reader and maintainer than a qualified generic relation or immediate technical names. They do not provide one immediate cross-domain query key; name a narrower reusable relation through `F.18` only when repeated query, comparison, or declaration use justifies the extra vocabulary. |

E.4 uses the currentness and reopen rule stated in `A.14:14`. A change to that A.14 source decision reopens only the affected product-series or Suite rule in `E.4:4.2` and `CC-E4.9`. An ordinary new edition, admission, inclusion or removal, qualification warning, availability change, or updated trace follows `E.4:4.2` and reopens the affected ecosystem claim; it does not by itself reopen this architecture.

The broader ecosystem source account follows.

| Claim | Exact source ref and status | Pattern locus changed | Adoption status |
| --- | --- | --- | --- |
| Product and service are management-relevant output distinctions, but their labels do not settle every direct subject in a framework ecosystem. | `ISO 9000:2026, Quality management - Fundamentals and vocabulary`, current fifth edition, `https://www.iso.org/standard/9000`. It distinguishes an organizational product output from a service whose delivery necessarily includes provider-customer activity. | Section 4.1 declares *product* to be Plain management wording and requires the direct subject and relation before a technical claim; `CC-E4.8` repeats that test. | **Adapt** the inexpensive product-versus-service question when it changes provision or maintenance. **Reject** the QMS vocabulary as a universal FPF ontology and do not require a quality-management system merely to place one support unit. |
| A maintained service, its provider, and the system used to manage its life cycle are different concerns. | `ISO/IEC 20000-1:2018, Information technology - Service management - Part 1: Service management system requirements`, confirmed current in 2023 with Amendment 1:2024, `https://www.iso.org/standard/70636.html`. It separates the organization and service-management system from the services planned, delivered, and improved. | The programme paragraph names provider and maintaining Systems, accepted commitments, any admitted service state, bounded Work, and result epistemes separately. | **Adapt** provider, service-life-cycle, and continual-maintenance distinctions for an actual access or inquiry service. **Reject** an IT-service scope and full service-management system for a bounded publication or guide; that effort is justified only by the selected service claim. |
| Publication identity, expression, issued manifestation, physical or digital item, and aggregation should not be collapsed into one carrier. | `IFLA Library Reference Model`, July 2024 maintained edition, `https://repository.ifla.org/handle/20.500.14598/40.2`. Its Work-Expression-Manifestation-Item relations and aggregate treatment make publication-level identity and embodiment explicit. | Sections 4.1 and 4.2 keep edition, publication unit, snapshot, projection, carrier, and neutral combined exposure separate. | **Adapt** the identity-versus-embodiment and aggregate-versus-component discipline for framework publications. **Reject** bibliographic entities as the ontology of services, programmes, Systems, or Methods; applying the full cataloguing model would add effort without answering those boundaries. |
| Reusable user and service information benefits from an explicit content boundary, life-cycle management, and tool-independent assembly. | `ISO/IEC/IEEE 26531:2023, Systems and software engineering - Content management for product life cycle, user and service management information for users`, current second edition, `https://www.iso.org/standard/81703.html`. | Section 4.1 groups support publication units by shared use, edition, access, maintainer, and cadence, while independent content gets its own exact edition or state and snapshot return. | **Adapt** the content-selection, reuse, maintenance, and multi-output discipline when the information scale warrants it. **Reject** a component-content system or complete software-documentation process as the default; a separately stored unit is not automatically a separate product. |
| Architecture descriptions separate architecture expression from the architecture and require concern, view, viewpoint, correspondence, and rationale discipline. | `ISO/IEC/IEEE 42010:2022, Software, systems and enterprise - Architecture description`, official current standard ref, `https://www.iso.org/standard/74393.html`. | `Solution` distinguishes the ecosystem-architecture record from publication carriers; `Common Anti-Patterns` repairs publication-only architecture; `Relations` cites the exact neighboring assertions and subject-pattern locators in `C.30`, `C.33`, `C.34`, `E.11`, and `E.17`. | Adopt the separation and correspondence discipline; adapt it to selected structures of a holonic FPF pattern ecosystem. |
| Reuse across related family members needs reusable core assets, variation, adoption, tooling, and evolution discipline. | Nazar, `Software Product Line Engineering: Adoption, Tooling and AI Era Challenges`, arXiv:2605.21353, 2026 current survey and reopen trigger for stronger post-2026 SPLE synthesis, `https://arxiv.org/abs/2605.21353`. | Family table separates FPF Core, domain frameworks, and local frameworks; `E.5.3` dependency direction is made a conformance check. | Adapt reusable-core and variation discipline; reject feature-model or software-product ontology as universal FPF architecture. |
| Pattern ecosystems need validation, worked cases, and relation clarity rather than recipe-book pattern lists. | Riehle, Harutyunyan, Barcomb, `Pattern Discovery and Validation Using Scientific Research Methods`, arXiv:2107.06065, 2021 current validation-practice source; Iba, `Pattern Languages as Media for the Creative Society`, arXiv:1308.1178, lineage for pattern-language social use. | `Archetypal Grounding` now includes a filled ecosystem-architecture record; `Conformance Checklist` and anti-pattern rows require source-return, exact relation definitions, and explicit repair conditions. | Adopt validation and example pressure; adapt it through `E.21`, `E.23`, worked slices, and near-miss repairs. |
| Relation-rich architecture should be stated as constraints rather than read as performed-work order. | `Dyad 3.3`, current release dated 2026-08-06, `https://help.juliahub.com/dyad/stable/manual/changelog.html`, with current syntax and analysis documentation at `https://help.juliahub.com/dyad/stable/manual/syntax.html` and `https://help.juliahub.com/dyad/stable/manual/analyses.html`. Dyad components carry variables, parameters, connectors, subcomponents, and relations, while analyses are separate workflows that produce solutions or artifacts. `Modelica Language Specification 3.7`, 2026, `https://specification.modelica.org/maint/3.7/MLS.html`, is retained only as historical declarative/acausal lineage and is intentionally not used as the current SoTA comparator. | Boundary wording in `Solution`, `Rationale`, and `E.4.PFR` keeps relation assertions declarative and separates them from dated Work and its results. | **Adapt** Dyad's separation between relation-rich component description and analysis that produces results. **Reject** its physical-model, equation, solver, simulation, component-language, and analysis ontology for FPF; reject Modelica as the current SoTA basis. |

### E.4:12 - Relations

- **Builds on:** `E.2/P-5 FPF Layering` and `E.5.3` for modular extension, directed dependency, and family-order discipline.
- **Coordinates with:** `E.4.FPF` when the work concerns FPF itself as a first-principles framework edition, its presentation carriers, access routes, and whole-FPF adequacy route.
- **Coordinates with:** `E.2.DA` when the scoped FPF object needs whole-FPF Pillar adequacy evaluation.
- **Coordinates with:** `E.4.PFAD` when the ecosystem-architecture record opens a framework-architecture question; `E.4.PFAD` profiles the framework-specific content, `E.9` supplies the decision-record method and content requirements, and the resulting DRR records the selected answer.
- **Coordinates with:** `E.4.DPF` when the work is to author a domain principle framework or local practice framework.
- **Coordinates with:** `E.4.PFR` when a relation, edition, dependency, compatibility, deprecation, or preservation claim must be recorded.
- **Coordinates with:** `E.4.DPF.DA` when a domain or local framework package must be evaluated as a package rather than as an average of its pattern bodies.
- **Coordinates with:** `E.11` for discoverability, `E.11.PFP` for the common publication form of FPF, DPF, or LPF constituents, `E.11.DSG` for the separately maintained Guide product series and its reader-facing cross-DPF answers, `E.11.PUR` for pattern-use recommendation, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.
- **Coordinates with:** `G.2`, `G.11`, `C.33`, `C.34`, and `C.35` for source, currentness, preservation, and produced-carrier admission claims.

### E.4:End

