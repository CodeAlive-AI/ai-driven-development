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

Describe an FPF-grounded pattern ecosystem as a family of framework editions and publication and access-facing presentation carriers, plus access routes, over selected structures. For each durable ecosystem-architecture claim, or technical claim on which later work will rely, state the exact subject and relation and cite the defining or constraining ClaimGraph in its subject pattern. The smallest route below needs no ClaimGraph citation when ordinary guidance or an honest stop already answers the question. A principle framework edition renders a selected architecture in pattern-language form for a declared reader and use. That architecture covers recurring problem situations, forces, known failure modes, reusable SoTA solution moves, consequences, cases, relation records, evaluation methods, and refresh conditions. Known failure modes include beginner mistakes and experienced-practitioner failures caused by stale, local-only, or non-SoTA practice.

Start with the smallest route that answers the current question:

1. Name the concrete ecosystem question and who needs the answer.
2. Classify the likely case: a framework-family boundary, an adjacent result or service, a publication carrier, access-facing presentation carrier, or access route, a DPF-suite question, or another relation already handled by a direct pattern.

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
  blockedOverreadRefs?
  dependentUsePatternLocators
```

This record answers the declared ecosystem question for its intended use. Include `blockedOverreadRefs` only when `F.19`'s grounded-contribution test admits them; otherwise omit the field. The record carries a contextual ecosystem answer; the subject claims and patterns it cites remain its content sources and semantic loci.

Classify the family members as follows:

`Conceptual Core` is the legacy authority and publication-family partition. `First Principles Framework edition` is the whole scoped FPF framework edition as a transdisciplinary first-principles framework. `FPF Core pattern set` is the framework-edition view of the general FPF Core used for dependency, relation, and edition reasoning. Use these compatible views and scopes for their respective questions.

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

In this pattern, *product* is Plain management wording for a deliberately identified result or service boundary. It helps a team state intended use, identity or current state, access, later change and retirement rules, and any maintenance that actually obtains. It is not one FPF technical kind and it creates no `U.Product`. Before making a product-boundary claim, name the direct subject—the thing the claim is about—and the relation that carries its identity, edition, current state, provision, publication, availability, or maintenance. The subject may be, for example, a framework-edition episteme, an evidence-package episteme, an admitted System, an admitted service arrangement, a Method, a programme-description episteme, or another result already admitted by its subject pattern. Constitution or publication establishes only the claims made by those acts; maintenance and future Work need their own evidence. If the direct kind or relation is not settled, keep the management boundary as a proposal and return that question instead of inventing a common object kind.


A framework edition is an episteme. Treat its Readme, Preface, table of contents, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route as named publication units in the same managed boundary when they share the edition's declared readers and use, edition boundary, access, and change rule. Being outside the pattern set or in another file does not by itself create another product or a maintenance claim.


Make a separate adjacent product only when people need to change, cite, or use its direct subject independently. Look for an independently useful identity, edition or current state, named users and use, an intensional rule for what belongs, access, a later-review or retirement rule, or cross-framework reuse or reliance. A separately established maintenance relation may also matter, but product identity does not require it. Examples include a registry, MethodDescription collection, evidence package, guide, tool reference, access service, or inquiry programme; other direct subjects may also justify a separate boundary. The label does not settle the kind: a guide or evidence package may be an editioned episteme; a tool reference may identify an episteme, a tool System, or both; and an access service needs its own service and provider-System claims. File location does not decide the boundary.


When the direct subject is independently used or changed, keep it separate and point from the framework to its exact edition or current state. An annex may carry a declared snapshot or projection, but it returns to the authoritative subject and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, keep it as a named support publication unit of the framework edition.


One presentation carrier may expose several managed products without merging their direct subjects. Each constituent keeps its own identity, edition or state, form, access, later-change and retirement rules, and any separately established maintenance relation; the outer navigation names the exact constituents and stays neutral. A result reused by several DPFs may therefore be managed as an ecosystem companion or service product. Shared use does not make it a parent DPF. Open another DPF only when its own field-boundary assessment finds recurring practitioner problems, constructive Methods, an independently useful first cut, evidence practice, and its own edition and change boundary.


When *programme* is used, start with what actually continues. An inquiry programme may be managed as a continuing programme or service product, but neither label says what persists. If a subject pattern admits the programme as a System or another exact arrangement, name it. Otherwise name the current programme-description episteme and any provider System, maintenance relation, accepted commitment, or service state that independently obtains. Bounded inquiry projects remain separate Work occurrences, and their results remain separate epistemes. A maintained inquiry evidence package is its own editioned episteme. The management boundary may coordinate these subjects and relations, but it does not turn them into one indefinitely continuing `U.Work` or one generic Product. If the persisting arrangement is still unclear, return that exact architecture question.

DRRs, build manifests, quality runs, digests, logs, and campaign state remain development or process evidence by default. They become reader products only when a selected public use gives a direct subject its own product identity and publication or availability route.


Use these tests in order: name the intended managed boundary and ordinary use; identify every direct subject, its kind, and the identity or current-state relation used by the decision; group only publication units that share the framework edition, readers, access, and change rule; test a proposed adjacent subject for independent use and change; select the smallest useful boundary; then record exact pointers, snapshot return, and neutral-carrier navigation. Establish maintenance only when a maintained claim is made. If a needed kind or relation remains unresolved, record that question and stop short of the technical product claim.


#### E.4:4.2 - Keep several DPF products usable as one suite

Use this branch when separately constituted DPF product series contribute to one ecosystem and people need to recover which product series belong to the Suite and how to use their current or historical editions. Keep distinct each continuing DPF product series, any separately constituted DPF Suite Reference product series, the continuing DPF Suite collection, and any as-of description of that collection. This introduces no `U.Product`, `U.DPFSuite`, or `U.DPFSuiteReference` kind.


Here *DPF product series* is Plain relation-defined wording for a continuing collection of a DPF's edition epistemes. The series begins when a product-constitution decision names at least one existing edition, intended readers and use, a content-selection and edition-admission rule, a reidentification rule, and later-review and retirement conditions. The decision's effect begins the collection and admits the first edition. A separate publication occurrence may make that edition available. A maintaining System, maintenance commitment, revision duty, another edition, or continued availability requires a separate claim. The decision Work and record are not the product series or the belongs-to occurrence.


Say **“this edition belongs to this product series.”** A later edition joins only when its `EpistemeEditionRelation` to the actual source edition obtains, the product-series rule still holds, and an admission decision takes effect. The edition relation establishes episteme continuity but does not admit the edition to the product series. A parallel branch, fork, translation, or derivative joins only when both its source relation and the admission rule pass. Otherwise it remains a related episteme outside the series or begins another product series. The series need not be one total version order.

An admitted edition continues to belong historically when it becomes superseded, unavailable, non-current, or retired while the same product series continues. Those states do not end the occurrence. If the product series ends or its identity rule identifies another product series, belonging to the old series ends and remains a past fact. Another product series must admit the edition through its own decision and a new occurrence. If review shows that the edition never satisfied the admission rule, correct the false claim; no valid occurrence existed. Do not remove and re-admit the same edition merely because availability or currentness changed. The same edition and continuing product series keep one occurrence rather than starting another.

A **DPF Suite** is a continuing collection of DPF product series. A separately constituted DPF Suite Reference product series can also belong after its own inclusion decision. The Suite rule states which product series may belong; individual editions do not. The Suite begins when a constitution decision identifies the ecosystem purpose and intended use, inclusion and removal rules, a reidentification rule, later-review and retirement conditions, and includes at least one actual DPF product series. Any maintenance relation or future maintenance Work must be established separately. The decision Work and record remain distinct from the Suite and the first inclusion occurrence.


The same Suite continues while its ecosystem purpose, rule for which product series may belong, inclusion and removal rules, and identity conditions remain within the declared evolution rule. Adding or removing a product series normally preserves it. Starting, changing, transferring, or ending a maintenance arrangement does not by itself reidentify the Suite. Changing a DPF or Reference edition, publication, availability fact, Reference answer, or configuration description does not by itself reidentify the Suite. Changing an identity anchor outside the rule identifies another Suite.


After constitution, a temporary one-product-series or empty state can preserve the same Suite only when an explicit decision keeps those anchors in force and names a restoration, review, or retirement condition. Present no current cross-DPF answer in that state. An end or retirement decision closes the continuing collection and ends every current belongs-to occurrence; separate removals are unnecessary. The Suite and the past facts remain identifiable, but later active use requires another constitution decision, another Suite, and new inclusions. Before constitution there is only a possible-future Suite.

Say **“this product series belongs to this DPF Suite.”** The relation begins when the product series satisfies the operative inclusion rule and an inclusion decision takes effect. It remains current while the same product series and Suite continue and no later removal decision has taken effect. While they continue, only an effective inclusion or removal changes that occurrence. If either collection ends, or its identity rule identifies another collection, belonging to the old collection ends; neither case requires a prior removal. A proposal, description, publication, locator, or common use may report the relation but does not make it obtain.

Loss of qualification does not silently change belonging. Show an action-changing warning and decide whether to repair qualification, remove the product series, change the Suite under its identity rule, or retire it. Until that decision, do not present the product series as qualifying, current for the defeated common use, or recommended on that basis. Restoration before removal keeps the same occurrence while the same product series and Suite continue. An effective removal ends it; a later inclusion begins another occurrence.

After an occurrence ends, say that the product **belonged** to the Suite and say when it ended; do not present past belonging as current. A reconstituted product series or Suite, or one reidentified under its rule, is another collection and needs a new inclusion decision and occurrence.

Belonging establishes collection membership between the product series and Suite. Apply `A.1` before asserting parthood or holonhood: the current definitions leave matters 3, 5, and 6—constructive parthood and assembly, a composition-grounded whole characteristic, and possible participation in a larger constructive assembly—unsettled. Treat both as continuing collections; a later complete `A.1` result and direct part predicate can add a constructive part or holon claim. State order, dependency, compatibility, recommendation, publication, availability, currentness, maintenance, and use through their own direct predicates. One product series may belong to several Suites. Use the direct sentence without assurance fields unless the publication elects `B.3.5`; after election, use its `validationMode=axiomatic` and current `C.13 set`-trace obligations without treating the trace as the cause.

A DPF Suite Reference product series belongs to the Suite only after its own inclusion decision and keeps its own reader use, admission, reidentification, later-review, and retirement conditions. Any maintenance relation remains separate. The Reference may join after the first DPF products. While its current availability and source return support the claim, it can supply a trustworthy cross-DPF route. Suite identity and direct use of a known DPF result rest on their own grounds.


For a reproducible as-of answer, use an optional **DPF Suite configuration description**: a `U.Episteme` about the Suite, the product series that belong at that time or in that scope, selected editions or states, and direct source return. Its own editions are description editions. Constitution and inclusion decisions establish Suite identity and belongs-to occurrences.

Use `G.5 JointUseSet` only when every identified result or edition is necessary for one bounded use. It represents that jointly necessary subset; another question may need resources from only some product series in the Suite. Suite constitution and inclusion remain the grounds for identity and membership.

Present the Suite as current or available only while its direct currentness and availability facts support that statement and readers can return to the collection identity, inclusion and removal decisions, and any product-series state claimed as current. Present it as maintained only when a separate maintenance relation and its current evidence support that stronger statement. A neutral carrier, current DPF Suite Reference edition, or optional configuration description may expose or pin those returns while preserving the distinct identities and relations of the Suite, product series, editions, carrier, access, maintenance, and currentness. Apply `E.17`, `E.24.PUB`, `C.2.P`, and `G.11` to their direct claims; use `E.4.PFR` only for a dependency or compatibility relation that separately obtains; and use `E.11.DSG` for the Reference's problem-led route and direct-DPF bypass.

The ordinary method is:

1. Declare the ecosystem scope and intended architecture use. Cite the exact source, pattern host, selected architecture structure, publication relation, or bounded model-use structure only when the record actually relies on it.
2. Name the family member being created, used, or changed.
3. Name only the fields from `FPFEcosystemArchitectureRecord@Context` that this architecture claim actually uses. For PF work, the pattern-language publication carrier exposes a reader-facing expression of the selected problem-and-solution architecture.
4. If the family member is FPF itself as a framework edition, open `E.4.FPF` for form, presentation carriers, access routes, and whole-FPF adequacy routing.
5. Apply `E.5.3`: dependencies point toward more stable framework editions. FPF Core does not depend on domain or local frameworks.
6. State publication and first-entry claims using `E.11` and `E.17`; state framework-carrier structure-account assertions using `E.4.FPF` for FPF itself or `E.4.DPF`/`E.4.DPF.DA` for domain and local frameworks.
7. State pattern-use recommendation claims using `E.11.PUR`.
8. When a framework-architecture question is open, record the selected answer in one `E.9` DRR and use `E.4.PFAD` to profile its framework-specific content. Use `C.32.PAD` only for an exact project architecture decision and `C.32.ADR` only to project such a decision into an ADR-like publication.
9. State relation, dependency, compatibility, deprecation, and edition claims using `E.4.PFR` only when its named maintenance use requires that representation; otherwise use the direct subject assertion.
10. Settle names using `F.18`.
11. State SoTA and source-use claims using `G.2`.
12. State currentness, refresh, and edition-change claims using `G.11`, the exact edition values, and their source/currentness assertions.
13. Before using a carrier or transformed or generated view as evidence, state the exact source-return or preservation assertion under the predicate defined in `C.33`, `C.34`, or `C.35`.
14. Evaluate whole-FPF adequacy through `E.2.DA`, DPF or local-framework package adequacy through `E.4.DPF.DA`, individual pattern quality through `E.21`, improve through `E.23`, and use `E.19` only when the local process asks for admission review.

Use this routing table when a proposed change is ambiguous. Its rows are common routes, not a closed taxonomy:

| Proposed work | Route to | Decision boundary |
| --- | --- | --- |
| The form of FPF itself changes: README, Preface, ToC, monolith, host set, skill pack, MCP-backed access, or whole-FPF publication/access route. | `E.4.FPF`, with `E.2.DA` for whole-FPF adequacy; state relation or edition claims directly and open `E.4.PFR` only for its named maintenance consumer. | FPF uses the whole-FPF route, `E.4.DPF.DA` remains the package route for domain or local frameworks, and the carrier exposes the framework edition as a separate subject. |
| Accepted changes are being assembled into an FPF, DPF, or LPF publication, or continuity with a predecessor publication is claimed. | `E.4.PFIP` for the accepted-source and predecessor-preservation comparisons. | Require both PFIP conclusions when both claims are made. Source parity, build success, carrier continuity, and package adequacy answer narrower questions. |
| A distinction or rule is intended to constrain ordinary FPF use across many domains and downstream frameworks depend on it. | An accepted FPF Core amendment decision under `E.9`, followed by the exact subject patterns whose assertions change. | Core admission requires the transdomain constraint and accepted amendment decision; local and domain guidance stays in its direct framework edition. |
| A reusable principle supports FPF-grounded work but is not a general Core rule for all domains. | Give the foundational principle pattern set or other named framework edition its own identity; state its dependency directly and open `E.4.PFR` only for its named maintenance consumer. | The framework edition and dependency boundary stay visible outside the Core table of contents. |
| A source tradition or professional domain needs FPF-shaped patterns. | Domain principle framework through `E.4.DPF`, `G.2`, and `E.4.PFAD`; state dependencies directly and open `E.4.PFR` only for its named maintenance consumer. | The framework adds recurring domain problems, SoTA solution moves, cases, and use conditions to its source account. |
| One bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—needs guidance. | Local practice framework through `E.4.DPF`; keep local source, publication, quality, and refresh records, and state separately any direct relation used for maintenance, responsibility, authority, assignment, or contact. If a load-bearing owner label has no current direct relation, return `missing-governor` instead of inventing one. | The named local setting bounds the guidance; a general FPF rule requires its own Core-amendment grounds. |
| Material needed for ordinary framework use shares the framework edition, readers, access, and change rule. | Keep it as a named support publication unit of that framework edition and expose it through the edition's carrier route. | Another managed product needs an independent use or change rule. |
| A registry, guide, evidence package, service, programme, or other result has an independently useful identity or state, users and use, content rule, access, or later-review and retirement rule. | Name its direct subject and the relevant relation, keep it as a separate product, and point to its exact edition or current state; any embedded snapshot returns to that source. State maintenance only when it separately obtains. | Keep direct subjects separate under shared use, co-location, or one outer carrier; an unresolved kind remains a proposed product and an open question. |
| One carrier exposes several managed products. | Keep the outer carrier neutral and retain each direct subject's form, identity, access, change rule, and any separately established maintenance relation. Use `E.11.PFP` only for FPF, DPF, or LPF constituents. | The neutral carrier exposes the exact direct subjects; framework-family fields apply only to framework constituents. |
| Several DPF product series and a DPF Suite Reference product series are proposed for one ecosystem. | Use `E.4:4.2` to decide product-series and Suite constitution, which editions belong to which product series, which product series belong to the Suite, identity through change, later review and retirement, optional configuration description, and truthful exposure; state maintenance separately only when it obtains. Use `E.4.PFAD` when the answer must be selected. | Constitution and inclusion or removal decisions establish the subjects and relations; titles, co-lists, carriers, Reference entries, and configuration descriptions report them. |
| Existing material is hard to find, teach, or publish. | Use `E.11` for discovery, the relevant didactic pattern for teaching, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use `G.5` only when the missing value is a selected-set result declaration. | Treat findability, teaching, and publication as their direct repair questions; architecture repair requires an architecture claim. |
| A cross-reference claims use, specialization, dependency, publication, source reuse, preservation, quality, deprecation, or supersession. | State the direct relation function and edition effect; open `E.4.PFR` only for its named maintenance consumer. | The link label remains a locator; the direct predicate states the relation meaning. |
| A framework split, dependency boundary, presentation-carrier or access-route choice, or adoption consequence must be decided. | Record one selected answer in an `E.9` DRR, using `E.4.PFAD` for its framework-specific content. Use `C.32.PAD` only when the decision is an exact project architecture decision and `C.32.ADR` only to project such a decision into an ADR-like publication. | The DRR carries the selected answer; diagrams, folders, manifests, PFAD relations, and project-specific projections may expose only their direct claims. |
| A source, search result, transformed view, or generated carrier supplies candidate material. | `G.2`, `C.33`, `C.34`, or `C.35` before architecture use. | Use the admitted source or preservation claim as authority for the declared contribution. |
| Whole-FPF adequacy, DPF package adequacy, individual pattern quality, repeated improvement, admission gating, or currentness is the live problem. | `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23`, `E.19`, and `G.11` according to the claim. | Use the exact evaluation or refresh route for the live question; package and whole-FPF conclusions remain distinct from aggregated pattern scores. |

This pattern should leave the reader able to state the architecture directly. Name the family member and selected pattern-language architecture, then state its dependency editions, publication or access carriers, preserved structures, and each neighboring claim under its exact predicate with the subject pattern as locator.

### E.4:5 - Archetypal Grounding

Tell: A team creating a hydroponic-cucumber domain principle framework creates a domain framework edition grounded in FPF Core and horticulture SoTA. It declares its dependency on an FPF Core edition and records its source packs. The team drafts domain patterns under `E.8` and publishes an all-in-one publication carrier for growers or agronomists.

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

Show: A Codex-process local practice framework may depend on FPF Core and selected architecture-domain patterns. Its handoff patterns, prelanding patterns, and process runbooks are local framework material. A Core-amendment decision under `E.9` remains the route for changing FPF Core.

Show: A generated relation graph over pattern names can help inspect missing relation assertions. After `C.35` admits the carrier, state each supported relation directly. Open a reusable `E.4.PFR` row only when a named maintenance consumer requires it.

Show: In the cucumber DPF, the Readme, table of contents, pattern collection, and coverage account share one framework edition, reader use, access route, and change rule, so they remain publication units of one product. A greenhouse-calibration source registry has its own edition rule and is reused by another crop DPF, so its current registry edition is a separate episteme. One web carrier may expose both while preserving their exact identities and direct relations.


### E.4:6 - Bias-Annotation

**Scope: limited.** This pattern helps make architecture claims about FPF-grounded framework ecosystems and their publication, access, companion, service, and separately established maintenance boundaries. Product taxonomy, service design, programme ontology, and content management remain with their direct patterns.


The recurrent drift is publication-first architecture: the visible file, all-in-one carrier, card deck, table of contents, or graph is treated as the architecture because it is what a reader sees first. The repair is to name the selected structures and dependency direction first, then use publication patterns to expose them.

Another recurrent drift is Core absorption: useful domain or local material is pulled into the Core because it is well written or broadly reusable. The repair is to ask which domain or local situation the claim addresses and which framework edition should depend on which more stable edition.

| Lens | Declared bias and counter-check |
| --- | --- |
| **Gov** | Favors an explicit intended use, identity and admission rule, currentness rule, and retirement response. Counter-risk: a useful grouping becomes a mandatory governance form or an unsupported promise of future Work. Add a maintainer, maintenance relation, or commitment only when that separate claim changes use or responsibility, and use its direct pattern. |
| **Arch** | Favors separating framework editions, support publication units, adjacent results, services, programmes, DPF lines, and carriers before composing them. Counter-risk: decomposition multiplies products. Choose the smallest product that preserves independent use and change, and let a neutral carrier expose several exact constituents without merging them. |
| **Onto-Epist** | Favors a direct subject kind and identity or current-state relation before technical use of *product*. Counter-risk: an ontology catalogue replaces ordinary architecture work. Keep *product* as Plain management wording, name only distinctions used by the decision, and return an unresolved-kind question rather than minting `U.Product`. |
| **Prag** | Favors observable independence in use, access, change, currentness, availability, and reliance over labels or file layout. Counter-risk: a small guide or service inherits a quality-management, service-management, bibliographic, or content-management regime. Apply the cheapest direct test that can change the decision; inspect maintenance only when it is claimed. |
| **Did** | Favors familiar product wording at first recognition, followed immediately by the exact subject when a technical claim is made. Counter-risk: readers copy examples as a closed taxonomy. Mark an illustrative list as illustrative; for a closed list, state the common kind, membership rule, and closure. Make the direct case recoverable in ordinary project language. |

### E.4:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| CC-E4.1 First route and family case | The work names the ecosystem question, classifies the likely case, gives the direct next pattern or honest stop, and opens a complete ecosystem-architecture record only when durable architecture or later reliance needs it. When a record is needed, it names whether the family member is Core, Tooling Reference, Pedagogical Companion, a foundational principle pattern set, a First Principles Framework edition, FPF Core, a domain principle framework, or a local practice framework. |
| CC-E4.2 Selected structures named | The ecosystem-architecture record names its intended use and every field from `FPFEcosystemArchitectureRecord@Context` that the claim actually uses. Cite a source, pattern host, publication relation, or bounded model-use structure only when the record uses that independently established value. |
| CC-E4.3 E.5.3 respected | Dependency direction points toward more stable framework editions, and Core does not depend on domain or local frameworks. |
| CC-E4.4 Publication and access separated | Each publication form or unit, presentation carrier, access route, access occurrence, and view keeps its direct subject and predicate; apply the direct pattern to each claim. |
| CC-E4.5 Exact predicate and assertion named | Each architecture-adjacent claim names its exact subject and predicate; a pattern identifier is only the locator for the next question's defining or constraining ClaimGraph. |
| CC-E4.6 Source-return present | Any carrier used as architecture evidence states captured structure, lost structure, admissible use, and the source to return to. |
| CC-E4.7 Framework carrier structure-account explicit | A Readme, Preface, ToC, all-in-one carrier, skill-pack carrier, or other form-bearing framework carrier states which framework structures its selected form exposes for whom. An MCP, retrieval, search, or assistant route identifies the first form-bearing carrier or response it reaches and returns to the same account; it is not scored as that carrier. Missing form or adequacy content is repaired as an exact assertion using `E.4.FPF`, `E.4.DPF`, or `E.4.DPF.DA` before adoption or adequacy claims are made. |
| CC-E4.8 Product decision proportional and typed | *Product* remains Plain management wording. Each product decision names its direct subjects and the identity, edition, current-state, provision, publication, availability, or maintenance relations it actually uses. Framework support units stay in one product when their edition, use, access, and change rule agree; an adjacent subject needs an independent use or change reason. Shared use and one carrier are only probes. An unresolved kind is returned as a question, not `U.Product`. |
| CC-E4.9 DPF Suite truth | Constitution identifies the Suite and each DPF product series; a DPF Suite Reference product series enters only through its separate inclusion. Admission, inclusion, and removal decisions establish edition-to-product and product-to-Suite membership. The account keeps decision effects while the same subjects continue, endings or reidentification, past belonging, identity anchors, a temporary empty state, retirement, and any configuration description recoverable. Maintenance uses its own direct claim; snapshots, lists, Reference entries or editions, carriers, and `JointUseSet` report only their stated facts. |


### E.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Core absorption | A domain or local framework is placed into the FPF Core because it is useful. | Create a separate framework edition and state its dependency directly; open `E.4.PFR` only for a named maintenance consumer. |
| File tree or package manifest as architecture | A folder layout, package descriptor, or manifest is read as the ecosystem architecture. | Use the file or manifest as a carrier and recover the direct architecture, relation, dependency, source-return, publication, access, quality, and currentness claims needed for the question. |
| Publication-only architecture | A table of contents or all-in-one carrier is used as the architecture description. | State the selected structures and source return directly; open an ecosystem-architecture record only for durable architecture or later reliance, and use `E.11` and `E.17` for the exact practical-entry and publication assertions. |
| Ontology or talk guide as framework | A framework names domain entities, terms, or conversation moves but does not identify recurring domain problems, known failure modes, SoTA solution moves, and worked repairs. | Keep the ontology, glossary, or communication guide as support material; create or repair the framework around problem situations, solution moves, cases, and quality routes. |
| Relation flattening | Every cross-reference is treated as the same relation. | State the direct predicate and subject pattern; open `E.4.PFR` only for a named maintenance consumer. |
| Outside the pattern set means another product | A Preface, coverage account, or refresh note is given a separate product identity although it shares the framework edition's readers, access, and change rule. | Keep it as a named support publication unit unless an independent use or change rule justifies another product. Maintenance may distinguish the products only when it separately obtains and changes use. |
| Product label used as an object kind | A guide, service, programme, registry, System, or episteme is asserted to be the same kind because each is managed as a product. | Keep *product* as Plain management wording. Name each direct subject and the relation used for identity, current state, provision, or maintenance; return an unresolved-kind question when needed. |
| Shared carrier or shared use means one product | A cross-framework registry or service is absorbed into one DPF, or a combined carrier merges a framework and catalogue. | Decide each product from its direct subjects, use, identity, and change rule; keep exact constituent pointers and let the outer carrier remain neutral. State maintenance only when it separately obtains. |
| Service or publication scheme used as universal architecture | A full service-management system, bibliographic entity model, or content-management process is imposed on every framework unit, programme, guide, or tool. | Reuse only the distinction that answers the current boundary question; keep service, publication, content, and programme claims under their own subject patterns. |
| DPF list presented as a Suite | A title or co-list replaces product-series constitution, the Suite-constitution decision, the direct belongs-to occurrences, identity rules, and later-review and retirement conditions. | Keep a proposal until `E.4:4.2` passes; then identify the Suite collection and the product series that belong to it. State maintenance only when it separately obtains. |
| Suite belonging inflated | Two product series belong to the same Suite, so the text infers order, dependency, compatibility, maintenance, publication, or co-use. | Keep the Suite claim at product-series grain and apply the direct predicate for every stronger claim. |
| Source-carrier authority | A summary, graph, or generated candidate set is treated as authoritative. | Admit the carrier through `C.35` or record preservation through `C.33` and `C.34` before use. |

### E.4:9 - Consequences

This pattern makes FPF ecosystem work slower at the beginning because a framework author must name family membership, dependency direction, selected structures, and the patterns needed for neighbouring claims. The gain is that later work can evolve without hidden Core changes, hidden publication substitutions, or hidden source loss.

It also makes some attractive names and short labels provisional until `F.18` settles them. That cost is intentional: short names are useful only after the value being named, its source-local meaning, and its intended use are explicit.

### E.4:10 - Rationale

An ecosystem-architecture record identifies the selected structures across FPF patterns, frameworks, source packs, exact presentation carriers, access routes, quality records, and decisions. Direct assertions state relation meaning and decision rationale. Source-return and currentness patterns qualify carriers and access routes. Architecture work therefore names the selected structures and applies the relevant direct pattern to each neighboring claim.

The old Core, Tooling Reference, and Pedagogical Companion distinction remains valuable, but it is only one family partition. Domain and local principle frameworks need their own framework editions so they can depend on Core without redefining it.

### E.4:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and E.4 mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should continuing product series and a Suite keep identity while editions or included series change? | The constructional comparison carried by `A.14:14` is the best-known line for this bounded FPF question: distinguish set, sum, tuple, and assembly constructions, make the constructor and identity rule explicit, and keep the operation prior to any derived part claim. | Generic `MemberOf`, fixed extent, list-as-collection, and automatic constructive parthood are the serious defaults. | Those defaults hide product-specific admission, Suite inclusion, history, and identity-through-change. **Adapt:** `E.4:4.2` states edition admission, edition-to-product belonging, product-series inclusion/removal, and Suite identity separately; `CC-E4.9` checks the complete history and decision account. | `A.14:14` supplies the selected constructional synthesis and its source limits. BORO and later constructional work are source roles inside that comparison, not maturity or authority evidence for E.4; E.4 leaves the unresolved `A.1` holon questions open. | Reopen only if the A.14 comparison changes the product-series or Suite identity rule, or an actual case defeats the ordinary separate-relation form at comparable effort. |
| How should a framework family be scoped without mistaking one current edition, file tree, or software feature model for the ecosystem architecture? | Marchezan de Paula et al.'s 2022 systematic review of 58 studies and 41 product-line scoping approaches is the best-known-line candidate for comparing product, domain, and asset scope across technical and organizational aspects. | File-tree architecture, one-off result scoping, and a mandatory feature-model process are the serious alternatives. | The first two hide reuse and change conditions; the last imports software-specific machinery before the framework question is settled. **Adapt:** the family table, ecosystem-architecture record, routing table, and ordinary method name the scoped boundary, intended use, reusable contribution, conditions, alternatives, and reopen triggers; **reject** software assets and the generic scoping process as FPF ontology. | Marchezan de Paula et al., [*Software product line scoping: A systematic literature review*](https://doi.org/10.1016/j.jss.2021.111189) (2022), is a broad scoping synthesis and reports evaluation gaps; it does not prove FPF family adequacy or select a universal process. Current internal FPF patterns supply the direct distinctions. | Reopen if stronger current family-scoping evidence changes the variables needed for a truthful scoped framework boundary or demonstrates a lower-effort comparison with the same organizational and change coverage. |
| What keeps a pattern ecosystem from becoming a recipe-book list with impressive labels but no validated use? | Riehle, Harutyunyan, and Barcomb's 2025 handbook method is the best-known-line candidate for explicit pattern discovery and validation through questions, cases, applications, and evidence limits. | Pattern count, broad naming, and one favorable expert review are the serious defaults. | The defaults make visible inventory substitute for recurring problem, solution, case, relation, and validation value. **Adapt:** `Archetypal Grounding`, `E.21` routing, conformance checks, and anti-patterns require worked cases, explicit relation claims, and honest evidence limits; open an ecosystem record only for durable architecture or later reliance. **Reject:** a full research programme as the cheap entry route. | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (2025), supplies validation pressure but does not validate E.4 or decide its architecture. Iba's pattern-language work is lineage and stays outside this section. | Reopen if current pattern-validation practice changes the evidence needed for the ecosystem claim or exposes a cheaper non-dominated validation route. |

Use official catalogues, vocabulary standards, current release pages, tool documentation, lineage sources, and source-maintenance checks only for their stated source or default contribution. Product kind, service kind, publication identity, relation truth, and SoTA rank each require their direct evidence and pattern.

### E.4:12 - Relations

- **Builds on:** `E.2/P-5 FPF Layering` and `E.5.3` for modular extension, directed dependency, and family-order discipline.
- **Coordinates with:** `E.4.FPF` when the work concerns FPF itself as a first-principles framework edition, its presentation carriers, access routes, and whole-FPF adequacy route.
- **Coordinates with:** `E.2.DA` when the scoped FPF object needs whole-FPF Pillar adequacy evaluation.
- **Coordinates with:** `E.4.PFAD` when the ecosystem-architecture record opens a framework-architecture question; `E.4.PFAD` profiles the framework-specific content, `E.9` supplies the decision-record method and content requirements, and the resulting DRR records the selected answer.
- **Coordinates with:** `E.4.DPF` when the work is to author a domain principle framework or local practice framework.
- **Coordinates with:** `E.4.PFR` when a named maintenance consumer needs a reusable relation, edition, dependency, compatibility, deprecation, or preservation record; otherwise state the direct relation assertion.
- **Coordinates with:** `E.4.DPF.DA` when a domain or local framework package must be evaluated as a package rather than as an average of its pattern bodies.
- **Coordinates with:** `E.11` for discoverability, `E.11.PFP` for the common publication form of FPF, DPF, or LPF constituents, `E.11.DSG` for the separately constituted DPF Suite Reference product series and its reader-facing cross-DPF answers, `E.11.PUR` for pattern-use recommendation, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

- **Coordinates with:** `G.2`, `G.11`, `C.33`, `C.34`, and `C.35` for source, currentness, preservation, and produced-carrier admission claims.

### E.4:End

