## E.4 - FPF Ecosystem Architecture: Framework Families, Products and DPF Suites

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative.

### E.4:1 - Problem frame

Use this pattern when an FPF user, framework author, or steward needs to create, extend, or use an FPF-grounded pattern ecosystem and must know what belongs to FPF itself, what belongs to the FPF Core, what belongs to a domain or local framework, which records carry relation and edition claims, and which neighboring patterns contain the defining content for publication, access, naming, source, currentness, and quality work.

Primary `EntityOfConcern`: the FPF-grounded pattern ecosystem for one named ecosystem question. The first useful result is a direct route or honest stop: name the question, classify the likely case, and point to the next pattern. Open a complete ecosystem-architecture record only when the answer must settle durable architecture or support later reliance.

This pattern buys a practical distinction: a reader can tell whether the work changes FPF itself as a first-principles framework edition, changes the FPF Core, creates a domain principle framework, creates a local practice framework, publishes or teaches existing content, exposes a skill-pack, index, or response carrier, or an MCP, retrieval, search, or assistant access route, or records a dependency on another framework edition. Use `E.4.FPF` when the work is the form of FPF itself; use `E.11` and `E.17` for first-entry and publication questions; use `E.4.DPF` when the work is to author a domain or local framework.

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

When the available methods are insufficient for the needed result under the relevant conditions, use C.39 to find or develop a missing operation or connection. When a method and its connections need a reusable explanation in a framework, use E.4.CM to develop that explanation, choose its placement and provide a reader entry. An adequate available method can be used directly.

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

Conceptual Core names FPF's general conceptual content within the existing Core, Tooling Reference and Pedagogical Companion family partition. An FPF edition is an identified body of framework content. Its publication units present that content, and readers obtain them through available access routes. The FPF Core pattern set consists of the selected Core subject patterns in that FPF edition. A framework-edition dependency names the relied-on FPF edition and the particular Core claims required for its use.

The Kernel is the subset of Core content that defines admitted universal meta-concepts and the rules for their meanings and relations. Membership follows that defining content, wherever it occurs in the patterns. Other Core content explains reusable methods, states their conditions and grounds, or governs the framework. All eleven E.2 pillars remain constitutional first principles outside the Kernel subset; they govern both Kernel and other Core content.

Readers obtain the relevant content from an FPF publication and use the supplying patterns for the question at hand. A pattern can contain both a definition and an explanation of its application. A Part heading, file boundary or selected rendering therefore does not define the Kernel's membership or constitute a separate Kernel edition. The Architectural Reference explains the framework as a whole; the pattern bodies retain the definitions, conditions and methods on which a use relies.

A domain or local framework identifies the Core content and edition on which it relies. That content may include a Kernel definition, a general method or a constitutional authoring requirement. The dependent framework supplies its own domain or local problems, methods, sources and use conditions. Authors can revise those contributions while preserving the relied-on meanings and obligations; a change to a supplying claim reopens the uses that depend on it. A shared publication carrier supplies access to these frameworks without merging their content or edition boundaries.

| Family member | Architecture contribution | Authoritative content loci |
| --- | --- | --- |
| Conceptual Core | Core FPF distinctions, rules, and patterns that other FPF-grounded frameworks depend on. | `E.4`, `E.5.3`, and the exact subject patterns containing the defining ClaimGraphs |
| Tooling Reference | Optional tools, schemas, scripts, machine checks, or helper publications that inspect or support FPF use. | Use `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability, and relevant tool patterns for their declared tool functions; use `G.5` only for a selector-facing selected-tool-set result declaration. |
| Pedagogical Companion | Tutorials, playbooks, worked examples, and learning material that teach FPF without changing Core meaning. | `E.17`, didactic patterns |
| Foundational principle pattern set | Foundational threshold material or principle patterns that may support FPF-grounded use but need settled names and dependency boundaries. | `F.18`, `E.4.PFR` |
| First Principles Framework edition | The scoped FPF framework edition as a transdisciplinary first-principles framework with Core pattern set, publication and access-facing presentation carriers, access routes, relation records, and whole-FPF adequacy route. | `E.4.FPF`, `E.2.DA`, `E.4.PFR`, `E.11`, `E.17`, `G.11` |
| FPF Core pattern set | The selected Core subject patterns in a named FPF edition. Framework dependencies identify that FPF edition and the relied-on Core claims. | `E.4.FPF:4`, `E.4.PFR:3.4`, `E.5.3`, and the cited Core subject-pattern claims |
| Domain principle framework | A framework grounded in FPF and domain SoTA; a DPF Suite describes a composite discipline through constituent DPFs and justified whole-level patterns. | `C.20`, `E.4.DPF`, `G.2`, `E.4.PFAD`, `E.4.PFR` |
| Local practice framework | A framework for one bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—grounded in FPF and often in a domain framework. Add a local system-role kind, a separate System-classification judgment, or an exact assignment occurrence only when the framework claim independently uses it; recover ambiguous *role* wording through `E.10.ROLE`. | `E.4.DPF`, `E.4.PFAD`, `E.4.PFR`, `G.11` |

#### E.4:4.1 - Place support units and adjacent products deliberately

In this pattern, *product* is Plain management wording for a deliberately identified result or service boundary. It helps a team state intended use, identity or current state, access, later change and retirement rules, and any maintenance that actually obtains. It is not one FPF technical kind and it creates no `U.Product`. Before making a product-boundary claim, name the direct subject—the thing the claim is about—and the relation that carries its identity, edition, current state, provision, publication, availability, or maintenance. The subject may be, for example, a framework-edition episteme, an evidence-package episteme, an admitted System, an admitted service arrangement, a Method, a programme-description episteme, or another result already admitted by its subject pattern. Constitution or publication establishes only the claims made by those acts; maintenance and future Work need their own evidence. If the direct kind or relation is not settled, keep the management boundary as a proposal and return that question instead of inventing a common object kind.


A framework edition is an episteme. Treat its Readme, architectural reference, table of contents, pattern-body collection, framework-scale structure or coverage account, relation or edition note, and refresh route as named publication units in the same managed boundary when they share the edition's declared readers and use, edition boundary, access, and change rule. Being outside the pattern set or in another file does not by itself create another product or a maintenance claim.


Make a separate adjacent product only when people need to change, cite, or use its direct subject independently. Look for an independently useful identity, edition or current state, named users and use, an intensional rule for what belongs, access, a later-review or retirement rule, or cross-framework reuse or reliance. A separately established maintenance relation may also matter, but product identity does not require it. Examples include a registry, MethodDescription collection, evidence package, guide, tool reference, access service, or inquiry programme; other direct subjects may also justify a separate boundary. The label does not settle the kind: a guide or evidence package may be an editioned episteme; a tool reference may identify an episteme, a tool System, or both; and an access service needs its own service and provider-System claims. File location does not decide the boundary.


When the direct subject is independently used or changed, keep it separate and point from the framework to its exact edition or current state. An annex may carry a declared snapshot or projection, but it returns to the authoritative subject and does not fork it. When no independent boundary is useful and ordinary framework use needs the material, keep it as a named support publication unit of the framework edition.

An **architectural reference** is the public account of how a named method language is assembled and why that arrangement helps its intended users. It explains the whole's purpose, constituents, relations, shared conditions, alternatives and limits, with the rationale and source synthesis needed to understand and adapt it. Give the unit the full public name `<name of the explained whole> Architectural Reference`, for example *FPF Library Architectural Reference*, *Engineering Suite Architectural Reference* or *Method Engineering Principle Framework Architectural Reference*. A shorter mention is sufficient once the explained whole is unambiguous. The qualified name identifies the account's subject; it does not select a filename, section key or independent product boundary.

Provide this account at each actual level of language assembly: patterns in a framework, constituent frameworks in a Suite, and Core, Suites and standalone frameworks in FPF Library. Each account explains the connections added at its own level and returns to the full constituent accounts and patterns. That descriptive assembly does not make every Method part of one composite Method or every described discipline part of one discipline. A Suite's disciplinary composition still needs C.20; a library-wide connection can instead be use, specialization, shared terminology or another stated relation.

The account belongs to the explained language. In a one-file framework it can be embedded; in a multi-file assembly it has a discoverable unit at that assembly level, which can be carried separately. Keep its relation to the whole explicit in either form. Source hosts, directories, generated pages and site slices do not create further language levels merely by dividing files. Do not duplicate an account for each carrier, and do not require it before a known pattern can be used directly.


One presentation carrier may expose several managed products without merging their direct subjects. Each constituent keeps its own identity, edition or state, form, access, later-change and retirement rules, and any separately established maintenance relation; the outer navigation names the exact constituents and stays neutral. A result reused by several DPFs may therefore be managed as an ecosystem companion or service product. Shared use does not make it a parent DPF. Open another DPF only when its own field-boundary assessment finds recurring practitioner problems, constructive Methods, an independently useful first cut, evidence practice, and its own edition and change boundary.


When *programme* is used, start with what actually continues. An inquiry programme may be managed as a continuing programme or service product, but neither label says what persists. If a subject pattern admits the programme as a System or another exact arrangement, name it. Otherwise name the current programme-description episteme and any provider System, maintenance relation, accepted commitment, or service state that independently obtains. Bounded inquiry projects require independent A.15.1 admission as separate Work occurrences, and their results remain separate epistemes. A maintained inquiry evidence package is its own editioned episteme. The management boundary may coordinate these subjects and relations, but it does not turn them into one indefinitely continuing `U.Work` or one generic Product. If the persisting arrangement is still unclear, return that exact architecture question.

DRRs, build manifests, quality runs, digests, logs, and campaign state remain development or process evidence by default. Publish the architectural reasons that affect use in the language's architectural reference or the relevant pattern, so readers need not reconstruct them from those records. The dated development, review and release history stays in its records. A selected public use can give a record its own product identity and publication route; ordinary understanding of the language does not require that separate publication.


Use these tests in order: name the intended managed boundary and ordinary use; identify every direct subject, its kind, and the identity or current-state relation used by the decision; group only publication units that share the framework edition, readers, access, and change rule; test a proposed adjacent subject for independent use and change; select the smallest useful boundary; then record exact pointers, snapshot return, and neutral-carrier navigation. Establish maintenance only when a maintained claim is made. If a needed kind or relation remains unresolved, record that question and stop short of the technical product claim.


#### E.4:4.2 - Describe a composite discipline with a DPF Suite

Use this branch when a proposed field contains several subdisciplines and the reader needs both their own Methods and the Methods that connect their contributions. First establish the discipline and its composition through C.20. Then describe that whole in a DPF Suite. A convenient selection of publications, several suppliers to one project, or a common audience can justify a reading route without establishing a composite discipline.

A **DPF Suite is a domain principle framework for a composite discipline**, assembled from the frameworks of its constituent subdisciplines and any justified whole-level patterns. It is a larger DPF, not another ontological kind of field and not a collection constituted merely by a publisher's inclusion decision. The described discipline is a `U.Discipline`; a particular Suite edition is a `U.Episteme` about that discipline. The constituent DPF editions describe its subdisciplines. A directory, website or combined file presents those descriptions. None of these is identical to the discipline.

##### E.4:4.2.1 - Recover the field before arranging its descriptions

State the field's recurring questions, objects of inquiry or intervention, characteristic results, knowledge and reusable practices. Use F.18 for a name that makes that field recognizable. A university subject, profession, conference or community is useful evidence of an established field; it does not by itself establish either the field's exact boundary or a constructive part relation.

For each proposed subdiscipline, recover the C.20 construction:

- the knowledge-bearing and reusable-practice contributions it makes to the larger field;
- the actual relations by which those contributions constrain, enable, test or revise other required contributions;
- the whole-forming arrangement, including admitted alternatives and how a part can be replaced without losing the field;
- the field's identity through changes to theories, Methods, instruments and institutions;
- a whole characteristic that the composition produces or sustains, with its grounds; and
- how this whole can participate in a larger disciplinary assembly.

Explain the coupling in practice. For example, an account of ground behaviour constrains a foundation design; the design identifies what site evidence is needed; observations and failure investigations can revise the account and design Methods. A bibliography listing geotechnics and structural engineering supplies neither this coupling nor a framework that teaches it. Nor does every construction project need to use every branch of those fields.

Use this field construction to reconsider the current Suite architecture. An intake may justify a new Suite, a split or merger of existing Suites, or a change to their boundaries; inclusion in an existing Suite is one possible outcome.

A Suite may describe a bounded, explicitly incomplete portion of a recognized composite discipline. State which constituent subdisciplines and whole-level problems it currently covers, which are outside that coverage, and what the reader can obtain. Partial coverage must not be presented as a complete account of the field. A planned constituent with no usable description is a gap, not an available DPF.

A first Suite edition may contain only one available constituent DPF when the composite field, its other constituents and their whole-forming relations are already established. The common account must offer a present use: for example, explaining where the available contribution applies, which connections it relies on and which needed results the edition cannot yet supply. Compare this benefit with keeping the DPF standalone until a common assembly is useful. One DPF plus an unspecified intention to add more frameworks does not establish a Suite.

##### E.4:4.2.2 - Distinguish composition, specialization and use

Do not infer one relation from another:

| Relation | What must be established | Publication consequence |
| --- | --- | --- |
| A subdiscipline is part of a composite discipline. | C.20's direct part relation and whole construction, including knowledge-practice coupling and continuity. | Its DPF is a constituent description in the Suite; the Suite explains the connection to the whole. |
| One Method or field is a specialization of another. | The inherited construction or constraints and the added subject-specific conditions. Specialization alone does not establish disciplinary parthood. | Retain the general supplier and develop the specialized contribution where its assumptions belong. |
| Work in one field uses a result from another. | The required result, supplying Method, receiving use and relevant conditions. | Give a direct use or dependency link. Do not include the supplier's entire DPF merely because that result is useful. |
| Several publications answer one question together. | Their actual contributions and the conditions for combining them; G.5 only for a jointly necessary selected set. | Supply a cross-framework entry or composition. This need not create a Suite. |
| A publication supports navigation or access. | Its information need, answer, source return and availability. | Keep it as a support publication or independently useful reference; it is not a subdiscipline. |

An engineering decision may need finance, research, mathematical modelling and ethical judgement. Their use does not make their entire disciplines parts of Engineering. Conversely, a subject-specific engineering branch does not become an external supplier merely because its Methods are used in only some projects. Test its participation in the continuing field assembly, not the participant list of one Work occurrence.

Do not force the discipline structure into a tree for filing convenience. If genuine multiple parthood is proposed, establish each direct relation and explain the shared contribution, whole-forming couplings and consequences of change in each assembly. First test whether the apparent overlap is actually a general Core Method, an independent supplier, specialization or two different subject-specific contributions. If it is, publish that distinction instead of duplicating whole DPFs. If genuine shared constituency remains, identify one current constituent description and explicitly assemble it into the affected Suite editions; a casual hyperlink or an unqualified second copy cannot carry that claim.

##### E.4:4.2.3 - Build the larger pattern language

Develop the Suite as a framework under E.4.DPF and E.8. Its entrance explains the composite field, the contribution of each constituent and the important relations between them. A long mantra can help a practitioner retain a connected Method, but neither that phrase nor a Reference substitutes for the Methods it recalls.

Give a whole-level Method its own pattern when it removes a recurring difficulty that the constituent Methods do not independently solve. State its problem frame, problem, forces, construction, limits and cases. The construction may consume results from several DPFs and return questions to them. If a contribution is transdisciplinary, develop it in Core instead of hiding it in a Suite introduction. If the missing work is specific to one subdiscipline, develop it there. If it reveals another field, reopen the field architecture rather than stretching a pattern or an appendix around it.

Expose enough of the language for a reader to select constituent Methods, understand their contributions, combine them where justified and retain their separate assurance obligations. Preserve alternative configurations; a Suite is not a mandatory sequence through every DPF. Use E.11.PFP for the Suite's framework entrance and constituent frameworks. Use E.11.DSG to develop the Suite's architectural reference, including useful problem-led entries. It covers the whole's architecture and can return both constituent and external contributions, labelled by their actual relation. An additional explanation of already described Methods belongs in the relevant pattern or architectural reference. A useful new operation or composition needs its own complete E.8 pattern; a mantra or reference entry cannot hide its missing construction. A teaching course or Guide with a separate learning purpose is a pedagogical companion, while explanations and cases needed to use or adapt the language remain with that language.

##### E.4:4.2.4 - Make the publication reflect the architecture

Give each current full Method description and constituent DPF an unambiguous authoritative home. Assemble the Suite's publication from its selected constituent editions and its own framework-level explanation; make that composition and the editions used recoverable. A Suite directory can be a convenient physical assembly of the complete constituent publications. A standalone DPF needs no artificial Suite. The FPF Library Architectural Reference explains their library-wide connections and boundaries; the library index locates the publications. Neither the index nor that account establishes another discipline above them.

Keep four kinds of change distinct:

1. A change in the discipline's knowledge, practice or composition is judged through C.20's identity and part relations.
2. A change to the framework description produces or revises a framework edition under C.2.1 and C.2.P.
3. A change to files, layout or access can preserve that edition while changing its presentation or availability.
4. A change in publication or maintenance responsibility changes those relations, not the described field by itself.

An editorial decision can select what a Suite edition describes. It cannot make a non-constituent field become a subdiscipline, and it cannot preserve an unsupported part claim until someone formally removes it. Correct the description when its claim is false; qualify incompleteness or uncertainty when the evidence is insufficient. Conversely, an unavailable file or retired framework publication does not erase a discipline.

For a release or reproducible use, identify the Suite edition and the constituent editions it assembles. An optional configuration description can pin those selections; it remains an episteme about the assembly, not the assembly's disciplinary subject. A separately maintained Reference can evolve independently while preserving its source returns. Apply E.4.PFIP when reconstructing publications: preserve useful Methods and their conditions, correct erroneous architecture, and update maintained links to the current full explanations.

##### E.4:4.2.5 - Keep edition series separate from disciplinary structure

When a use needs continuity across releases, a **framework product series** is a continuing collection of edition epistemes. A constitution decision starts it by identifying at least one existing edition, its intended readers and use, content-selection and edition-admission rules, a reidentification rule, and later-review and retirement conditions. When that decision takes effect, the series begins and the first edition is admitted. The decision Work and its record remain separate from the series and the edition's belonging to it. Publication, maintenance and future availability require their own claims.

A later edition joins only when its actual source-edition relation and the series rule hold and a further admission decision takes effect. A fork or translation is not admitted by provenance alone. The series need not have one total version order. Supersession, unavailability, non-currentness or edition retirement does not end the edition's belonging while the same series continues, and a return to availability does not create a new occurrence. If the series ends or is reidentified as another series, current belonging to the old series ends; the past fact remains. Another series needs its own admission decision. If a claimed earlier admission never satisfied the rule, correct the false claim instead of preserving it as historical truth.
The same publishing arrangement can be used for a constituent DPF, a Suite framework or an independently managed Reference. It describes their publication continuity, not `DisciplinePartOfRelation`. A series may end while the described discipline continues, and a revised Suite edition may correct its account of that discipline. Establish publication, availability and maintenance separately through E.17, E.24.PUB, C.2.P and G.11 when those claims matter. Do not make a routine reader reconstruct admission decisions merely to use a current Method.
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
| The form of FPF itself changes: README, Architectural Reference, ToC, monolith, host set, skill pack, MCP-backed access, or whole-FPF publication/access route. | `E.4.FPF`, with `E.2.DA` for whole-FPF adequacy; state relation or edition claims directly and open `E.4.PFR` only for its named maintenance consumer. | FPF uses the whole-FPF route, `E.4.DPF.DA` remains the package route for domain or local frameworks, and the carrier exposes the framework edition as a separate subject. |
| Accepted changes are being assembled into an FPF, DPF, or LPF publication, or continuity with a predecessor publication is claimed. | `E.4.PFIP` for the accepted-source and predecessor-preservation comparisons. | Require both PFIP conclusions when both claims are made. Source parity, build success, carrier continuity, and package adequacy answer narrower questions. |
| A distinction or rule is intended to constrain ordinary FPF use across many domains and downstream frameworks depend on it. | An accepted FPF Core amendment decision under `E.9`, followed by the exact subject patterns whose assertions change. | Core admission requires the transdomain constraint and accepted amendment decision; local and domain guidance stays in its direct framework edition. |
| A reusable principle supports FPF-grounded work but is not a general Core rule for all domains. | Give the foundational principle pattern set or other named framework edition its own identity; state its dependency directly and open `E.4.PFR` only for its named maintenance consumer. | The framework edition and dependency boundary stay visible outside the Core table of contents. |
| A source tradition or professional domain needs FPF-shaped patterns. | Domain principle framework through `E.4.DPF`, `G.2`, and `E.4.PFAD`; state dependencies directly and open `E.4.PFR` only for its named maintenance consumer. | The framework adds recurring domain problems, SoTA solution moves, cases, and use conditions to its source account. |
| One bounded local practice setting—for example a project, organization, workflow, tool, practitioner position, or audience—needs guidance. | Local practice framework through `E.4.DPF`; keep local source, publication, quality, and refresh records, and state separately any direct relation used for maintenance, responsibility, authority, assignment, or contact. If a load-bearing owner label has no current direct relation, return `missing-governor` instead of inventing one. | The named local setting bounds the guidance; a general FPF rule requires its own Core-amendment grounds. |
| Material needed for ordinary framework use shares the framework edition, readers, access, and change rule. | Keep it as a named support publication unit of that framework edition and expose it through the edition's carrier route. | Another managed product needs an independent use or change rule. |
| A registry, guide, evidence package, service, programme, or other result has an independently useful identity or state, users and use, content rule, access, or later-review and retirement rule. | Name its direct subject and the relevant relation, keep it as a separate product, and point to its exact edition or current state; any embedded snapshot returns to that source. State maintenance only when it separately obtains. | Keep direct subjects separate under shared use, co-location, or one outer carrier; an unresolved kind remains a proposed product and an open question. |
| One carrier exposes several managed products. | Keep the outer carrier neutral and retain each direct subject's form, identity, access, change rule, and any separately established maintenance relation. Use `E.11.PFP` only for FPF, DPF, or LPF constituents. | The neutral carrier exposes the exact direct subjects; framework-family fields apply only to framework constituents. |
| Several fields appear to form one larger discipline. | Use `C.20` and `E.4:4.2` to distinguish genuine constituent subdisciplines from specialization, external use and publication grouping. Use `E.4.PFAD` to decide the framework architecture and `E.4.DPF` to develop the composite pattern language. | A Suite describes the established disciplinary composition. Its edition assembles constituent DPF descriptions; a Reference supports use, and neither a folder nor an inclusion decision establishes disciplinary parthood. |
| Existing material is hard to find, teach, or publish. | Use `E.11` for discovery, the relevant didactic pattern for teaching, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. Use `G.5` only when the missing value is a selected-set result declaration. | Treat findability, teaching, and publication as their direct repair questions; architecture repair requires an architecture claim. |
| A cross-reference claims use, specialization, dependency, publication, source reuse, preservation, quality, deprecation, or supersession. | State the direct relation function and edition effect; open `E.4.PFR` only for its named maintenance consumer. | The link label remains a locator; the direct predicate states the relation meaning. |
| A framework split, dependency boundary, presentation-carrier or access-route choice, or adoption consequence must be decided. | Record one selected answer in an `E.9` DRR, using `E.4.PFAD` for its framework-specific content. Use `C.32.PAD` only when the decision is an exact project architecture decision and `C.32.ADR` only to project such a decision into an ADR-like publication. | The DRR carries the selected answer; diagrams, folders, manifests, PFAD relations, and project-specific projections may expose only their direct claims. |
| A source, search result, transformed view, or generated carrier supplies candidate material. | `G.2`, `C.33`, `C.34`, or `C.35` before architecture use. | Use the admitted source or preservation claim as authority for the declared contribution. |
| Whole-FPF adequacy, DPF package adequacy, individual pattern quality, repeated improvement, admission gating, or currentness is the live problem. | `E.2.DA`, `E.4.DPF.DA`, `E.21`, `E.23`, `E.19`, and `G.11` according to the claim. | Use the exact evaluation or refresh route for the live question; package and whole-FPF conclusions remain distinct from aggregated pattern scores. |

This pattern should leave the reader able to state the architecture directly. Name the family member and selected pattern-language architecture, then state its dependency editions, publication or access carriers, preserved structures, and each neighboring claim under its exact predicate with the subject pattern as locator.

### E.4:5 - Archetypal Grounding

A team developing a hydroponic-cucumber domain framework uses FPF's distinction between a method, its description and performed work, together with E.8's framework-authoring requirements. Horticultural sources supply the crop-specific methods and conditions. The team identifies the relied-on Core content and edition, develops its domain patterns and publishes the framework for growers or agronomists. A changed crop-specific threshold reopens the affected domain explanation and its uses; it does not by itself change the meanings of Method or Work.

The edition labels in this example are illustrative. `FPF@C1` names one stipulated FPF edition containing the Core claims cited here. `HydroponicCucumberPF@2026Q3` uses A.3.1:4.3 from that edition to distinguish the nutrient-monitoring method, its description and performed monitoring work. Its revision guidance also applies E.8:4.1.2, item 6, from the same FPF edition: authors repair examples and direct consumers made stale by a changed pattern interface in the same authoring increment. Removing or materially changing either relied-on claim reopens the corresponding domain explanation or revision guidance.

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
| `selectedRelationRecordRefs` | reuse of named horticultural source claims; dependence on selected FPF Core content for the described concepts and framework authorship; publication relation to the all-in-one carrier |
| `selectedDependencyAndEditionRefs` | `HydroponicCucumberPF@2026Q3` depends on `FPF@C1`: the Method/MethodDescription/Work distinction in A.3.1:4.3 for the monitoring explanation, and the direct-consumer repair requirement in E.8:4.1.2, item 6, for pattern revision, as stated above. No reverse dependency from the FPF edition. |
| `selectedPublicationOrAccessCarrierRefs` | domain all-in-one publication carrier plus readme as first-entry carrier |
| `selectedSourcePackRefs` | greenhouse-control and crop-production `G.2` source packs |
| `qualityAndImprovementRefs` | `E.21` pattern-quality evaluation and `E.23` improvement loop for drafted domain patterns |
| `currentnessAndRefreshRefs` | `G.11` refresh when cited source packs, the relied-on `FPF@C1` claims or edition, or crop-production practice change |

Show: A Codex-process local practice framework may depend on FPF Core and selected architecture-domain patterns. Its handoff patterns, prelanding patterns, and process runbooks are local framework material. A Core-amendment decision under `E.9` remains the route for changing FPF Core.

Show: A generated relation graph over pattern names can help inspect missing relation assertions. After `C.35` admits the exact generated result for its intended architecture use, state each supported relation directly. Open a reusable `E.4.PFR` row only when a named maintenance consumer requires it.

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
| CC-E4.7 Framework carrier structure-account explicit | A Readme, Architectural Reference, ToC, all-in-one carrier, skill-pack carrier, or other form-bearing framework carrier states which framework structures its selected form exposes for whom. An MCP, retrieval, search, or assistant route identifies the first form-bearing carrier or response it reaches and returns to the same account; it is not scored as that carrier. Missing form or adequacy content is repaired as an exact assertion using `E.4.FPF`, `E.4.DPF`, or `E.4.DPF.DA` before adoption or adequacy claims are made. |
| CC-E4.8 Product decision proportional and typed | *Product* remains Plain management wording. Each product decision names its direct subjects and the identity, edition, current-state, provision, publication, availability, or maintenance relations it actually uses. Framework support units stay in one product when their edition, use, access, and change rule agree; an adjacent subject needs an independent use or change reason. Shared use and one carrier are only probes. An unresolved kind is returned as a question, not `U.Product`. |
| CC-E4.9 DPF Suite truth | A Suite describes a composite discipline whose constituents, knowledge-practice couplings, identity, composition-grounded characteristic and larger-assembly compatibility are recoverable under C.20. The framework exposes constituent DPFs and justified whole-level Methods, distinguishes external suppliers and support publications, and names its actual coverage. Discipline, framework edition, edition series, publication and maintenance remain distinct. The physical publication reflects the selected composition without ambiguous duplicate Method owners. |
| CC-E4.10 Architectural reference at the explained level | Each declared language assembly has a public architectural reference named for that whole, embedded or separately carried. It explains the connections and use-changing rationale of its level, returns to constituent explanations, and preserves direct pattern use. File divisions do not create assembly levels; an account does not by itself create a discipline, composite Method, independently managed product or product series. |


### E.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Placement decided from usefulness alone | Useful domain Methods are absorbed into Core, or general Methods are left in an arbitrary DPF because their applications have familiar domain names. | Test the premises and construction: domain-specific contributions belong in the relevant DPF; genuinely transdisciplinary distinctions and Methods can belong in Core. Broad usefulness alone settles neither choice. |
| File tree or package manifest as architecture | A folder layout, package descriptor, or manifest is read as the ecosystem architecture. | Use the file or manifest as a carrier and recover the direct architecture, relation, dependency, source-return, publication, access, quality, and currentness claims needed for the question. |
| Publication-only architecture | A table of contents or all-in-one carrier is used as the architecture description. | State the selected structures and source return directly; open an ecosystem-architecture record only for durable architecture or later reliance, and use `E.11` and `E.17` for the exact practical-entry and publication assertions. |
| Ontology or talk guide as framework | A framework names domain entities, terms, or conversation moves but does not identify recurring domain problems, known failure modes, SoTA solution moves, and worked repairs. | Keep the ontology, glossary, or communication guide as support material; create or repair the framework around problem situations, solution moves, cases, and quality routes. |
| Relation flattening | Every cross-reference is treated as the same relation. | State the direct predicate and subject pattern; open `E.4.PFR` only for a named maintenance consumer. |
| Outside the pattern set means another product | A Preface, coverage account, or refresh note is given a separate product identity although it shares the framework edition's readers, access, and change rule. | Keep it as a named support publication unit unless an independent use or change rule justifies another product. Maintenance may distinguish the products only when it separately obtains and changes use. |
| Product label used as an object kind | A guide, service, programme, registry, System, or episteme is asserted to be the same kind because each is managed as a product. | Keep *product* as Plain management wording. Name each direct subject and the relation used for identity, current state, provision, or maintenance; return an unresolved-kind question when needed. |
| Shared carrier or shared use means one product | A cross-framework registry or service is absorbed into one DPF, or a combined carrier merges a framework and catalogue. | Decide each product from its direct subjects, use, identity, and change rule; keep exact constituent pointers and let the outer carrier remain neutral. State maintenance only when it separately obtains. |
| Service or publication scheme used as universal architecture | A full service-management system, bibliographic entity model, or content-management process is imposed on every framework unit, programme, guide, or tool. | Reuse only the distinction that answers the current boundary question; keep service, publication, content, and programme claims under their own subject patterns. |
| DPF list presented as a Suite | A co-list or publisher's inclusion decision replaces a composite discipline and its pattern language. | Establish the C.20 whole and describe it under E.4:4.2; otherwise retain a useful library index, reading route or other publication without the Suite claim. |
| Use inflated into Suite membership | A needed result, similar audience or general Method makes an entire supplier DPF appear to be a constituent discipline. | Test the direct part relation, specialization and use separately. Put transdisciplinary Methods in Core and keep independently useful supplier DPFs outside the Suite unless their actual disciplinary parthood is established. |
| Source-carrier authority | A summary, graph, or generated candidate set is treated as authoritative. | Admit the exact generated or discovered result for its intended architecture use through `C.35` or record preservation through `C.33` and `C.34` before use. |

### E.4:9 - Consequences

This pattern makes FPF ecosystem work slower at the beginning because a framework author must name family membership, dependency direction, selected structures, and the patterns needed for neighbouring claims. The gain is that later work can evolve without hidden Core changes, hidden publication substitutions, or hidden source loss.

It also makes some attractive names and short labels provisional until `F.18` settles them. That cost is intentional: short names are useful only after the value being named, its source-local meaning, and its intended use are explicit.

### E.4:10 - Rationale

An ecosystem-architecture record identifies the selected structures across FPF patterns, frameworks, source packs, exact presentation carriers, access routes, quality records, and decisions. Direct assertions state relation meaning and decision rationale. Source-return and currentness patterns qualify carriers and access routes. Architecture work therefore names the selected structures and applies the relevant direct pattern to each neighboring claim.

The old Core, Tooling Reference, and Pedagogical Companion distinction remains valuable, but it is only one family partition. Domain and local principle frameworks need their own framework editions so they can depend on Core without redefining it.

### E.4:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and E.4 mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a Suite represent a composite field rather than a publication collection? | C.20 supplies the current FPF construction of a discipline from knowledge, reusable practice, direct part relations, whole-forming couplings, continuity and a composition-grounded characteristic. A.14 remains useful for distinguishing publication collections from constructive assemblies. | Folder membership, common audience, co-use and a publisher's inclusion decision are the serious defaults; the opposite error forces every field into a disjoint tree. | The defaults either omit the field or infer its parts from editorial acts. **Adapt:** E.4:4.2 makes a Suite a DPF of a composite discipline, distinguishes parthood, specialization and use, and then assembles its descriptions. Publication-series continuity stays a separate claim. | C.20 is the supplying internal synthesis; its evidence limits remain applicable. This architecture rule does not establish any particular Suite merely by naming it or by passing a file-layout check. | Reopen when a proposed whole fails C.20, a real shared constituency defeats the selected assembly, or a subject-specific contribution is obscured by the present distribution. |
| How should a framework family be scoped without mistaking one current edition, file tree, or software feature model for the ecosystem architecture? | Marchezan de Paula et al.'s 2022 systematic review of 58 studies and 41 product-line scoping approaches is the best-known-line candidate for comparing product, domain, and asset scope across technical and organizational aspects. | File-tree architecture, one-off result scoping, and a mandatory feature-model process are the serious alternatives. | The first two hide reuse and change conditions; the last imports software-specific machinery before the framework question is settled. **Adapt:** the family table, ecosystem-architecture record, routing table, and ordinary method name the scoped boundary, intended use, reusable contribution, conditions, alternatives, and reopen triggers; **reject** software assets and the generic scoping process as FPF ontology. | Marchezan de Paula et al., [*Software product line scoping: A systematic literature review*](https://doi.org/10.1016/j.jss.2021.111189) (2022), is a broad scoping synthesis and reports evaluation gaps; it does not prove FPF family adequacy or select a universal process. Current internal FPF patterns supply the direct distinctions. | Reopen if stronger current family-scoping evidence changes the variables needed for a truthful scoped framework boundary or demonstrates a lower-effort comparison with the same organizational and change coverage. |
| What keeps a pattern ecosystem from becoming a recipe-book list with impressive labels but no validated use? | Riehle, Harutyunyan, and Barcomb's 2025 handbook method is the best-known-line candidate for explicit pattern discovery and validation through questions, cases, applications, and evidence limits. | Pattern count, broad naming, and one favorable expert review are the serious defaults. | The defaults make visible inventory substitute for recurring problem, solution, case, relation, and validation value. **Adapt:** `Archetypal Grounding`, `E.21` routing, conformance checks, and anti-patterns require worked cases, explicit relation claims, and honest evidence limits; open an ecosystem record only for durable architecture or later reliance. **Reject:** a full research programme as the cheap entry route. | Riehle, Harutyunyan, and Barcomb, [*Pattern Discovery and Validation Using Scientific Research Methods*](https://doi.org/10.1007/978-3-662-70810-1_6) (2025), supplies validation pressure but does not validate E.4 or decide its architecture. Iba's pattern-language work is lineage and stays outside this section. | Reopen if current pattern-validation practice changes the evidence needed for the ecosystem claim or exposes a cheaper non-dominated validation route. |

Use official catalogues, vocabulary standards, current release pages, tool documentation, lineage sources, and source-maintenance checks only for their stated source or default contribution. Product kind, service kind, publication identity, relation truth, and SoTA rank each require their direct evidence and pattern.

### E.4:12 - Relations

- **Builds on:** `E.2/P-5 FPF Layering` and `E.5.3` for modular extension, directed dependency, and family-order discipline.
- **Coordinates with:** `E.4.FPF` when the work concerns FPF itself as a first-principles framework edition, its presentation carriers, access routes, and whole-FPF adequacy route.
- **Coordinates with:** `E.2.DA` when the scoped FPF object needs whole-FPF Pillar adequacy evaluation.
- **Coordinates with:** `E.4.PFAD` when the ecosystem-architecture record opens a framework-architecture question; `E.4.PFAD` profiles the framework-specific content, `E.9` supplies the decision-record method and content requirements, and the resulting DRR records the selected answer.
- **Uses:** `C.20` to establish a discipline and its composition before choosing a Suite architecture.
- **Coordinates with:** `E.4.DPF` when the work is to author a domain principle framework, including a DPF Suite, or a local practice framework.
- **Coordinates with:** `E.4.PFR` when a named maintenance consumer needs a reusable relation, edition, dependency, compatibility, deprecation, or preservation record; otherwise state the direct relation assertion.
- **Coordinates with:** `E.4.DPF.DA` when a domain or local framework package must be evaluated as a package rather than as an average of its pattern bodies.
- **Coordinates with:** `E.11` for discoverability, `E.11.PFP` for the common publication form of FPF, DPF, or LPF constituents, `E.11.DSG` for architectural references and their problem-led entries at framework, Suite and Library levels, `E.11.PUR` for pattern-use recommendation, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability.

- **Coordinates with:** `G.2`, `G.11`, `C.33`, `C.34`, and `C.35` for source, currentness, preservation, and admission of generated or discovered results for architecture use.

### E.4:End
