## E.17.2 - TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons
> **Status:** Stable authoring template; no TEVB catalogue value is shipped by this pattern.

**Use this when.** A project wants to author one small local family of engineering viewpoints for descriptions of holons, so that functional, procedural, allocation-responsibility, and module-interface claims remain distinguishable and comparable.

**What goes wrong if missed.** A functional, procedural, responsibility, structural, diagram, or report label starts doing several jobs at once: it is treated as the viewpoint, the view, the described holon, a publication face, or proof of an engineering relation. The opposite failure is to require all four viewpoints and their full authoring machinery for one local reading.

**What this buys.** TEVB supplies a four-position authoring template. Once a project has constituted its own catalogue L and bound four exact local references to four exact viewpoint epistemes, that project can reuse the resulting local family while keeping candidate episteme, described holon, conformance, cross-view relations, and publication separate. One use may select just one bound member.

**First action.** Resolve the already admitted project-local catalogue edition L and the local declaration designated by `f_eng`, then resolve only the `U.ViewpointRef` needed for the present question. If L or the declaration is new, missing, or disputed, use E.17.1:4.2 to constitute or verify `<G_L, K_L, R_L>` for that edition. If a needed P edition is missing, author and admit it under E.17.0 before binding its reference. Reuse those results while the catalogue edition, effective scheme, declaration, and relied-on premises remain unchanged.

**First useful result.** For materialization: one exact project-local L, ordinary family designator `f_eng`, four exact local references `r_functional`, `r_procedural`, `r_allocation`, and `r_module`, and four exact local P targets to which those references resolve under `R_L`. For later use: the admitted L and declaration, one needed reference resolving one exact P, and a readable E/P conformance judgment. Before the four bindings exist, the result is only an authoring template, not a reusable family value.

**Ordinary stop.** For materialization, stop when the exact local catalogue triple, declaration claim block, four reference bindings, and four exact P targets are recoverable. For later use, stop after resolving the admitted L and declaration, the one needed P, and its E/P judgment; reopen full catalogue constitution only under the E.17.1:4.2 triggers. Add another member, structured viewpoint-authoring witness, C.13/A.22 organization, construction history, cross-view relation, evaluation, or publication object only when a named receiving use depends on it.

**Not this pattern when.** Keep a one-off viewpoint local when no recurring four-position family is needed. Author another E.17.1 declaration for safety, assurance, information, mission, deployment, business, publication, or architecture-framework-specific concerns outside the four TEVB positions. TEVB is not a universal architecture framework.

> **Tech-name:** `TEVB` — the template name, not a family designator or catalogue value
> **Plain-name:** project-local typical engineering viewpoint bundle template for holons

**Product-form boundary.** This pattern ships no exact catalogue edition, effective scheme, family designator, `U.ViewpointRef`, or viewpoint episteme edition. Every `L`, `f_eng`, `r_*`, `P_*`, `C_*`, `Q_*`, and `S_*` symbol below is a variable in the template until one project supplies and verifies its exact binding. Equal labels in two projects establish no shared family or cross-project reuse. Such reuse begins only when both uses resolve the same exact L and member references.

The template does not by itself constitute an architecture framework, a `U.Method`, a set of publication forms, or an additional entity alongside exact catalogue L and its referenced P editions. It prescribes no modelling notation, storage format, or tool API.

**Builds on:** E.17.0 for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View`; E.17.1 for bundle packaging by `U.ViewpointRef`; C.2.1 for episteme identity; C.13 for the constituent collections of viewpoint conventions; A.22 for their selected structures; A.6.6 and E.17.0 for exact constituent-dependency relations; A.6.3 for optional view construction; E.24.PUB for publication.

**Used by after a project materializes the bindings:** E.18 transformation-flow descriptions, E.17 multi-view publication, architecture-description patterns, and domain patterns that need that exact local engineering concern family for holons.

### E.17.2:1 - Problem frame

Engineering descriptions repeatedly ask four different questions about one holon:

1. **Functional:** what transformations, capabilities, and effects characterize what the holon can or is intended to do?
2. **Procedural:** what methods, orders, states, concurrency, failures, and recovery rules characterize how relevant behavior unfolds?
3. **Allocation-responsibility:** which admitted Systems, exact local system-role kinds, current C.3.2 judgments that one System counts under a kind for one `KindSignature` edition and context slice, obtaining assignments, capabilities, transformations, and separately governed responsibility relations or selected structures are related to the holon's behavior?
4. **Module-interface:** what constituent holons, interfaces, dependency structures, substitutability conditions, and change rules characterize its construction?

The questions recur across hardware, software, organizations, and mixed systems. Their answers may appear as prose, models, diagrams, cards, or publications, but those forms do not identify the viewpoints or make an episteme a view.

### E.17.2:2 - Problem

How can engineers reuse a compact family of these four concern-bearing viewpoints while keeping all of the following distinct:

- the exact holon described by a candidate episteme;
- the exact viewpoint episteme and its exact target kind or, only in the triggered structured branch, its selected convention structure;
- the candidate episteme and any dependent `U.View` membership;
- a viewpoint selected for one describing use;
- the Methods, transformations, selected structures, local system-role kinds, assignments, modules, and interfaces mentioned in the claims;
- any viewing construction, evaluation, cross-view relation, publication occurrence, form, representation, or carrier?

Without that separation, a label such as `functional view` can stand indiscriminately for a concern convention, a diagram, a query output, a report section, or a claim about a system. The next engineering action then relies on the wrong object.

### E.17.2:3 - Forces

| Force | Tension |
|---|---|
| Reuse vs exact edition | Teams need stable families, while conformance depends on exact claim-bearing viewpoint editions. |
| Small core vs subject breadth | Four viewpoints should remain learnable without pretending that safety, mission, data, deployment, and every domain concern are the same four things. |
| Holon-centered view vs concern objects | A view can concern one holon while its claims designate Methods, transformations, local system-role kinds, assignments, capabilities, and structures through exact relations. |
| Familiar engineering language vs kind precision | `functional view` should remain readable without turning `functional`, `view`, or a diagram label into an intrinsic kind by spelling. |
| Direct authoring vs generated descriptions | Both can yield conforming views; neither route establishes conformance by itself. |
| Cross-view comparison vs invented links | Comparable views need exact direct relations, not a universal correspondence record or matching diagram positions. |
| Viewpoint reuse vs publication reuse | Many unpublished epistemes can conform to the same viewpoint, and each episteme may later have many publication forms; packaging must not redefine membership. |

### E.17.2:4 - Solution

**Local mantra.** To materialize a local instance, constitute L and bind `f_eng`, four exact references, and four exact P targets. To use an admitted instance, resolve L, its declaration, and only the needed reference. Then identify holon-centered candidate E and test E.17.0 conformance. For any additional engineering or publication claim, keep its objects and relations distinct and use the applicable pattern.

The mantra is a recall aid. The following sections specify the template positions, local materialization, conformance use, and stopping rules; none of their variables denotes a repository-shipped value.

#### E.17.2:4.1 - Bind one project-local declaration without embedding viewpoint values

One project instantiates the template only by supplying these exact bindings:

```text
L_local = catalogue episteme identified by <G_L, K_L, R_L>
f_eng   = ordinary family designator interpreted under R_L

local declaration claim block in G_L:
  familyDesignator = f_eng
  targetKindCompatibility = exact U.Holon target-kind criterion
  viewpointRefs = {
    r_functional,
    r_procedural,
    r_allocation,
    r_module
  }

resolve_R_L(r_functional) = P_functional
resolve_R_L(r_procedural) = P_procedural
resolve_R_L(r_allocation) = P_allocation
resolve_R_L(r_module) = P_module
```

The four `r_*` variables must be bound to exact local `U.ViewpointRef` values; the four `P_*` variables must be bound to exact already admitted viewpoint episteme editions. `f_eng` and any reader-facing names are ordinary designators under `R_L`. Designator, reference, viewpoint episteme, any optional selected viewpoint-convention structure, declaration claim block, and catalogue L remain distinct.

The template does not admit P as `U.Viewpoint`, make another episteme a `U.View`, or establish publication. Use E.17.0 for both dependent-kind membership tests, E.17.1 for L and its declaration claim block, and E.24.PUB for publication.

The four positions are fixed for a project declaration that claims conformance to this template. Safety, assurance, information, mission, deployment, business, and publication-oriented viewpoints use another local E.17.1 declaration or a later exact project catalogue edition with an explicitly revised declaration. A recurring label alone neither binds nor extends `f_eng`.

#### E.17.2:4.2 - Materialize each local viewpoint before binding its reference

Each `P_*` variable must be bound to one exact C.2.1 episteme that independently gains `U.Viewpoint` membership under E.17.0. Start with E.17.0's self-contained branch: give P its exact admitted target kind as EntityOfConcern and put the complete fixed target-kind, concern, admissibility, semantic-form, coverage, consistency, completeness, omission, and describing-use test in its ClaimGraph. Use the structured C/Q/S branch below only when separately versioned convention components and their organization change a named project reuse, comparison, or maintenance action.

For any one of the four positions:

1. identify the exact target kind and the complete self-contained P ClaimGraph;
2. apply the five E.17.0 viewpoint-membership conditions;
3. only in the independently triggered structured branch, identify exact convention epistemes under their least-powerful admitted kinds, construct exact collection C under C.13, recover every selected obtaining direct relation, state ordinary constraint episteme `Q_org`, let a system perform the A.22 selection work, and identify exact selected structure S;
4. bind the resulting exact P to its project-local reader designator and exact `U.ViewpointRef`; and
5. record the resolution under exact `R_L` in the local declaration claim block.

No constituent, `Q_org`, or P becomes a `U.Signature` merely to fit this template. A constituent is a `U.MethodDescription` only when it describes one independently admitted method under A.3.2. Exact selection work and its result remain separate from C, S, P, and selected relation occurrences. The structured-witness table below contains variables and optional recipes, not current repository values.

The four template positions use these exact concern objects and patterns when one project authors its P editions:

| Template position | Exact concern EntityOfConcern and applicable pattern |
|---|---|
| functional | exact `U.Transformation` under A.3.4; exact `U.Capability` under A.2.2; exact transformation-flow `U.Structure` under E.18 and A.22 |
| procedural | exact `U.Method` under A.3.1; exact transformation-flow `U.Structure` under E.18 and A.22; exact operational-state `U.Structure` under A.19.SPR and A.22 |
| allocation-responsibility | exact local system-role kind under A.2; when the view claims that one exact System counts under that kind, the separate C.3.2 judgment over candidate, kind, exact `KindSignature` edition, and context slice; an optional `KindExtension` representation only for a named set-consuming use; exact obtaining assignment occurrence under a directly declared `U.SystemRoleAssignment` species when an assignment claim is current; exact `SystemRoleKindRelationStructure` under A.2.7 and A.22; exact `U.Capability` under A.2.2; exact `U.Transformation` under A.3.4; an independently governed responsibility relation or selected structure when responsibility is current |
| module-interface | exact dependency `U.Structure` under B.1.1 and A.22; every module, interface, boundary, substitutability, or change-policy relation separately names its predicate, participants, obtaining test, and applicable pattern |
Keep these claim boundaries explicit:

- **Functional:** functioning status, input/output boundary, and functional-port coverage remain claims in `E_rule.functionalCoverage` unless the claim identifies a separate EntityOfConcern and states its exact predicate, participants, and obtaining test. The three concern epistemes stay separately about exact Transformation, exact Capability, and exact transformation-flow Structure; there is no universal function entity or one multi-subject concern episteme.
- **Procedural:** every method, order, state, concurrency, failure, and recovery claim designates its exact operational subject and the admitted method, state-transition, or transformation-flow relation that gives the claim meaning. A bounded coverage rule may remain in P, but a candidate E cannot satisfy it through vocabulary alone. Method mention grants no MethodDescription membership, state wording is not a Structure, procedural content is not performed work, and safety evidence is added only for a safety-bearing claim or named reliance.
- **Allocation-responsibility:** holder System, local system-role kind, four-input C.3.2 classification judgment, optional extension representation, assignment, transformer relation, allocation, segregation, capability, and responsibility remain separate typed claims or concern objects. A local system-role kind is not a classification judgment or assignment; classification or assignment establishes neither responsibility nor Work; and a selected structure performs no Work.
- **Module-interface:** A.6.M `ModuleInterfaceClaim` remains claim content. Whole-holon, candidate-module, boundary, independently identified `InterfaceSpecification` episteme and its resolving reference, substitutability, and change-policy content stays in the coverage-rule episteme until an exact module-relation declaration supplies participant kinds, predicate, obtaining rule, and occurrence identity and current facts satisfy it. The claim record is not that relation and a module topic is not an EntityOfConcern.

Split any phrase spanning several exact subjects into separate concern epistemes, or retain it as one constraint claim over candidate content. Give each stakeholder constituent exactly one referent—exact System, local system-role kind, claim-bearing C.3.2 classification-assertion episteme when that judgment is current, exact obtaining system-role assignment, C.13 collection-as-whole, or other independently governed subject. A `KindExtension` remains an optional representation for a named set-consuming use, not the kind or judgment. Cite any responsibility concern through its separately governed direct predicate. Do not coerce heterogeneous constituents into Signatures merely to make the rows uniform.



The following four rows are structured-branch recipes. Every symbol is a template variable until a project binds exact values; an ordinary self-contained P does not materialize this row.

| Exact project substrate after binding | Applied constraints, selected structure, and viewpoint episteme | Selected direct dependencies | Method and work boundary |
|---|---|---|---|
| `C_functional = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.functionalTransformation, E_concern.capability, E_concern.transformationFlowStructure, E_rule.functionalCoverage, E_rule.functionalModuleSeparation, E_rule.functionalRetargeting}` | `Q_org.functional` is an ordinary constraint episteme about C. A.22 selects `S_functional`; exact project `P_functional` has `EntityOfConcern=S_functional`, is assigned local reader designator `d_functional`, and passes E.17.0 viewpoint membership before `r_functional` is bound to it. | Each concern episteme depends on `E_target.tevbHolon`; `E_rule.functionalCoverage` depends on all three concern epistemes and `E_admitted.tevbEpisteme`; separation depends on functional-transformation concern; retargeting depends on the target. | No method constituent is required. A method convention enters only as exact `U.MethodDescription` after its method passes A.3.1. |
| `C_procedural = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.method, E_concern.transformationFlowStructure, E_concern.operationalStateStructure, E_rule.proceduralCoverage, E_rule.proceduralMethodBoundary, E_rule.proceduralNoWorkInference}` | `Q_org.procedural` is about C. A.22 selects `S_procedural`; exact project `P_procedural` has `EntityOfConcern=S_procedural`, is assigned local reader designator `d_procedural`, and passes E.17.0 membership before `r_procedural` is bound. | Each concern episteme depends on the target; coverage depends on all concerns and admitted-episteme kind; method boundary depends on method concern; no-work-inference depends on method and transformation-flow concerns. | Operational methods remain subjects of separate method-description epistemes. Concern selection, view construction, evaluation, and use do not form one method or workflow by mention. |
| `C_allocation = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.systemRoleKind, E_concern.systemRoleKindRelationStructure, E_concern.capability, E_concern.transformation, E_concern.responsibility, E_rule.allocationCoverage, E_rule.allocationNoWorkInference, E_rule.allocationRetargeting}`; add `E_concern.systemRoleClassification` only for an independently current four-input C.3.2 judgment, and add `E_concern.systemRoleAssignment` only for an independently current assignment claim | `Q_org.allocation` is about C. Use A.22 to select `S_allocation`; exact project `P_allocation` has `EntityOfConcern=S_allocation`, is assigned local reader designator `d_allocation`, and passes E.17.0 membership before `r_allocation` is bound. | Each current concern episteme depends on the target; coverage depends on all current concerns and the admitted-episteme kind; no-work-inference depends on whichever kind, classification, assignment, transformation, and responsibility concerns are current; retargeting depends on the target. | A bare *role* label, raw kind or relation reference, and raw Method are not collection members. Only exact current concern epistemes enter C. An allocation or analysis Method enters only through an exact MethodDescription episteme. The selected structure performs no Work. |
| `C_module = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.dependencyStructure, E_rule.moduleCoverage, E_rule.interfaceTyping, E_rule.functionalModuleSeparation, E_rule.substitutabilityChange, E_rule.moduleRetargeting}` | `Q_org.module` is about C. A.22 selects `S_module`; exact project `P_module` has `EntityOfConcern=S_module`, is assigned local reader designator `d_module`, and passes E.17.0 membership before `r_module` is bound. | Dependency-structure concern depends on the target; coverage depends on target, dependency structure, and admitted-episteme kind; typing, functional separation, and substitutability/change depend on dependency structure; retargeting depends on target and dependency structure. | No method, work, or module relation enters by mention. A direct module or interface relation joins only after its own pattern supplies participants, obtaining law, and occurrence identity. |

Each project-bound structured witness remains independently recoverable. Exact constituent editions identify C; every selected dependency occurrence passes the E.17.0 predicate; optional `D_dependencyUse` states obtaining and named-use admissibility as separate claims; and A.22 selects S from exact C, selected occurrences, applied Q constraints, and the use frame. Exact P is then identified by its ClaimGraph, S EntityOfConcern, and effective scheme. Changing only the Q edition leaves S unchanged when those selection inputs remain semantically unchanged. No topic list, citation, displayed edge, hidden O, D, template variable, or neighboring witness supplies another witness's closure.
The dependency relation in this table is exact `ViewpointConventionDependencyRelation` from E.17.0. It obtains only when interpreting or replaying the fixed claims of the dependent episteme relies on an exact criterion, law, public name, or method claim of the base episteme, and replacing the base edition can change that interpretation or replay. Co-membership, citation, or a visible arrow is insufficient.



When an A.22 selection judgment needs an explicit claim that one obtaining dependency occurrence is admissible for that use, identify the separate decision-use episteme described by E.17.0. Do not insert that decision, its evidence, or its evaluation result into the dependency relation or S identity.

#### E.17.2:4.3 - Keep the four concern conventions distinct

**Functional.** A conforming candidate episteme foregrounds exact transformations, capabilities, effects, functional elements, or transformation-flow relations of its holon. It does not identify a module structure by functional vocabulary and does not mint `U.Function`. Any neighboring responsibility claim keeps the admitted System, local system-role kind, current C.3.2 classification judgment, exact assignment, kind-relation structure, capability, transformation, and direct responsibility relation separate; use A.2, C.3.2, A.2.1, A.2.7, or the direct responsibility pattern for the claim actually made.

**Procedural.** A conforming candidate episteme foregrounds exact methods, order, state, concurrency, failure, and recovery related to its holon and designates the exact admitted method, state-transition, or transformation-flow relations on which each claim depends. A procedural view about a holon is not a `U.MethodDescription`; that dependent kind requires one admitted method as its exact EntityOfConcern. Ordinary operational recovery needs no safety package unless the claim is safety-bearing or a named receiving decision relies on one.

**Allocation-responsibility.** A conforming candidate episteme foregrounds exact Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, relations among those kinds, capabilities, transformations, and separately governed responsibility relations or selected structures related to its holon. A label creates no kind, classification, or assignment; a classification judgment needs its candidate, kind, `KindSignature` edition, and context slice but no assignment. The view may state that judgment, but it does not make the criterion true, create an assignment or responsibility relation, or perform Work.

**Module-interface.** A conforming candidate episteme foregrounds exact constituent holons, dependency structures, boundaries, interfaces, compatibility, substitutability, and change policy. It remains distinct from the functional viewpoint: many modules may support one transformation, one module may support several transformations, and either description may be incomplete without becoming the other.

The following are practitioner recognition and claim-shape cues, not embedded `StakeholderFamilies` or `AllowedEpistemeKinds` fields. A reader label creates neither a system-role classification nor an assignment and enters neither viewpoint nor view identity; every example still needs its exact EntityOfConcern, the predicate and participants of each claimed relation, its obtaining test, and its E.17.0 conformance result.

| Template position | Typical readers or concern holders | Distinctive claim-shape and conformance cues |
|---|---|---|
| functional | System-engineering and architecture readers, product or capability owners, and reliability or performance readers inspecting capability envelopes | Look for service-capability and promise content, delivery or access and API descriptions, input/output signatures, and functional-port boundaries as separate claims about the holon. Ground bounded behavior in exact transformations, capabilities, or a selected transformation-flow structure; keep service delivery Work, access relations, publications, and module interfaces separate, and do not mint `U.Function`. |
| procedural | Operations and run-time owners, control and automation engineers, and safety readers | Look for exact operational subjects and admitted method, state-transition, and transformation-flow relations behind order, state, concurrency, failure, and recovery claims. Where step boundaries are current, make preconditions and postconditions explicit and type-checked. Open an exact safety-analysis basis, A.10 evidence path, or B.3 assurance branch only when the current claim is safety-bearing or a named receiving decision relies on it; otherwise stop at the operational relations and ordinary failure/recovery boundary. Keep method, method description, work plan, dated Work, calendars, and selected state or flow structures distinct. |
| allocation-responsibility | Organization and operations designers, safety or compliance readers concerned with segregation of duties, and device or system engineers | Look for the admitted System and exact local system-role kind; when the claim says that System counts under the kind, recover the separate four-input C.3.2 judgment. Look separately for any assignment occurrence, segregation and escalation constraints, capability and transformation claims, and responsibility relation or structure. A kind locator is neither a classification result nor an assignment; none of those claims proves responsibility; allocation wording is not an obtaining relation; and no view or selected structure performs the allocated Work. |
| module-interface | Hardware or software architects, integration and test engineers, and lifecycle or maintenance readers concerned with replaceable units | Look for module decomposition, protocols, schemas, physical connectors, APIs, interface and conformance expectations, version and change policies, dependency and allowed-coupling structures, replaceability and variation points, and explicit functional-to-module correspondence or allocation without identity by default. Ports or connector diagrams do not establish module/interface relations; state and test each direct relation separately, and use A.6.4 for any functional-to-module retargeting. |

#### E.17.2:4.4 - Recognize holon-centered TEVB views by conformance

TEVB keeps two subjects explicit:

| Episteme | Exact EntityOfConcern | Job |
|---|---|---|
| viewpoint episteme P | exact admitted target kind in the self-contained branch; exact selected viewpoint-convention structure S only in a triggered structured branch | states the target-kind criterion, concerns, admitted episteme kinds, semantic-form, coverage, consistency, completeness, omission, and describing-use rules |
| candidate or view episteme E | one exact holon H admitted by P's target criterion | states claims about H; whenever it relates H to another engineering object, it names the exact predicate, participants, and obtaining test |

`EpistemeViewpointConformanceRelation(E,P)` must pass the fixed E.17.0 predicate. Only then is the same episteme E a `U.View`. Direct authoring, query execution, A.6.3 construction, a reader-facing label, declaration membership, or publication does not establish that membership. A reader-facing system-role label also establishes neither the local kind nor a C.3.2 classification judgment or assignment.

For one current describing use, its exact use qualification carries one singular `viewpointRef : U.ViewpointRef` resolving P under the effective reference scheme. Any reader-facing viewpoint name is only P's ordinary designator. The use qualification, designator, reference, and P remain distinct; selection identifies neither E nor H, establishes no conformance, and adds no conformance participant or episteme-identity field.

Recover exact H only as `EntityOfConcern(E)` from E's C.2.1 constitution. Do not import a legacy context tuple, generic bounded-context object, or model-use identity field into E, P, S, conformance, or selection. Another use may select another P while E remains unchanged; several selected viewpoints require an exact C.13 collection of their references rather than one overloaded reference.
If a user needs a view whose exact subject is a Method, local system-role kind, system-role assignment, transformation, responsibility relation, or structure rather than H, identify another candidate episteme with that EntityOfConcern and use a viewpoint whose target-kind criterion admits it. Do not silently retarget a holon-centered TEVB view.

#### E.17.2:4.5 - Import, subset, and extend one materialized local instance

An E.17.0 multi-view use can import TEVB only after it resolves one admitted project catalogue edition L, retrieves the declaration claim block designated by exact local `f_eng`, and resolves the exact imported `r_*` members or subset. Open `<G_L, K_L, R_L>` under E.17.1:4.2 only when L or the declaration is new, missing, or disputed, or a named later use consumes the catalogue constitution as premises. `f_eng` is only an ordinary designator inside L: it identifies neither L nor any viewpoint by itself and is not a member reference. Each imported reference resolves exact P under `R_L`; any reader-facing viewpoint name is only P's designator. A local subset names retained references, preserves `<editionDesignator(L), f_eng>` provenance, and records whether each omission is unused coverage or an intentional exclusion.

If local work changes only reader-facing aliases or adds examples, keep those as naming or annex content. If it changes a viewpoint's target criterion, concerns, admitted episteme kinds, or conformance rules, identify another viewpoint episteme edition and bind another exact reference as needed. If it changes family membership, identify another catalogue episteme or declaration claim block. Do not keep an old designator while changing the exact P it resolves under the same effective scheme.

Several local families may be used together, but each member retains its exact catalogue provenance and resolved viewpoint edition. Similar labels do not merge members. Two projects can claim use of the same reusable family only when they resolve the same exact L, declaration, and member references; independent instances of this template remain different local families even when all four labels match.

A project may bind its local four positions to reader names such as `Functional`, `Procedural`, `Allocation-Responsibility`, and `Module-Interface`. Those names do not perform the binding. A different reference-to-position mapping is another local declaration and must not silently reuse the earlier `f_eng` under `R_L`.

#### E.17.2:4.6 - Keep cross-view relations and publication separate

A materialized local TEVB instance provides four exact project references; the template alone provides none. Neither instance nor template asserts correspondence among resulting views. When a later engineering use depends on a relation between a functional claim and a module claim, or between a procedural claim and a system-role-assignment claim:

1. identify the exact participating entities or epistemes;
2. state the exact realization, allocation, dependency, consistency, trace, or other direct relation claimed;
3. use the concrete pattern that defines and tests that relation, including its obtaining law;
4. use A.6.RCD when no existing direct or derived relation is sufficient;
5. use C.29 only for a representation of the recovered relation.

If a separate receiving claim asserts dated `U.Work`, use A.15.1 to establish its performer, Method, time, and containing System, and F.6 to identify the assignment under which the performer acted. Those Work facts are neither participants in the cross-view relation nor prerequisites for identifying it.

E.17 and E.24.PUB may publish a selected TEVB view edition through three distinct relations: `PublicationFormExpressionRelation(selectedEdition,publicationForm,boundedUseDeclaration)`, `PublicationFormBearingRelation(presentationCarrier,publicationForm)`, and the five-participant `EpistemePublicationRelation(selectedEdition,audienceDeclaration,boundedUseDeclaration,publicationForm,presentationCarrier)`. Each retains its own participant set and maximal continuous obtaining interval; changing a participant or restoring availability after a gap yields another occurrence without reidentifying unchanged E or P.

Rendering, printing, upload, or carrier manipulation is separate system-performed `U.Work`. Use C.29 only when a representation corresponds to independently recovered objects or relations. A publication-side viewpoint, when current, is another exact viewpoint episteme selected by reference—not a TEVB position label reused as a form or file name. View episteme, viewpoint episteme, construction, conformance, form, carrier, publication, rendering, and representation remain distinct; publication and representation make no represented world-side relation obtain.

### E.17.2:5 - Worked cases

The cases below assume one hypothetical project has already constituted exact `L_local`, bound `f_eng`, and resolved `r_functional -> P_functional`, `r_procedural -> P_procedural`, `r_allocation -> P_allocation`, and `r_module -> P_module` under exact `R_L`. They demonstrate a materialized local instance; they do not assert that these values exist in the repository or in another project.

#### E.17.2:5.1 - Four views of a processing plant

Exact plant `Plant_X : U.System` is the EntityOfConcern of four separately identified epistemes.

- E1 states transformations, capabilities, material-flow effects, and functional boundaries. `r_functional` resolves `P_functional`; E1 conforms to that P and is a functional `U.View`.
- E2 states claims about exact admitted method `PlantOperation`, exact A.19.SPR operational-state structure `PlantRunState`, and exact E.18 transformation-flow structure `PlantRunFlow`; its order, failure, and recovery claims designate the exact transition conditions and flow relations in those structures. It conforms to `P_procedural`; it is not a method description because its EntityOfConcern is the plant. No safety-bearing claim or named reliance is present in this case, so no safety-analysis, A.10, or B.3 branch is opened.
- E3 states that `PumpUnit-3` counts as local kind `CoolingCirculatorSystemRole` in the plant slice through a separate C.3.2 judgment over the exact candidate, kind, `KindSignature` edition, and slice; that claim needs no assignment. E3 separately states any obtaining assignments, capabilities, transformations, and governed responsibility structures that are current. It conforms to `P_allocation`; neither E3 nor `P_allocation` makes the classification criterion true, creates an assignment or responsibility relation, or performs Work.
- E4 states constituent equipment holons, dependency structure, pipes, interfaces, substitutability, and change policy. It conforms to `P_module`; the diagram rendering E4 is published in remains separate.

The four conformance occurrences make E1-E4 views. Their shared holon and common local declaration do not establish any cross-view realization or consistency relation. Those claims are tested separately.

#### E.17.2:5.2 - Query output missing a required concern

A query constructs episteme Y from plant model X, and A.6.3 records that construction. Y is labelled `functional view`, but it omits the output-condition coverage required by exact `P_functional`. Construction obtains; conformance does not. Y is not a `U.View` under that P until another episteme edition with repaired claim content passes the predicate.

#### E.17.2:5.2.1 - Ordinary non-safety jam recovery

Candidate procedural episteme `E_jamRecovery` concerns exact conveyor system H. Its ClaimGraph designates exact admitted method `ClearJam`, an exact operational-state structure with `Running`, `Blocked`, and `Resetting` positions, the exact transition conditions between those positions, and the exact E.18 flow relation that resumes only after the blockage sensor is clear. These method, state, and flow facts supply the operational basis for its failure-and-recovery claims. If `EpistemeViewpointConformanceRelation(E_jamRecovery,P_procedural)` obtains, E is a procedural `U.View`.

No claim in this case is safety-bearing, no receiving decision relies on a safety analysis, and no evidence or assurance result is requested. Therefore neither an A.10 evidence path nor a B.3 assurance branch is opened. A later actual clearing remains separately identified `U.Work`; the procedural episteme does not perform it.

#### E.17.2:5.2.2 - Safety-triggered recovery use

Suppose a second claim says that restarting H after the same jam is safe for an exposed operator, and a named restart decision relies on that proposition. The project now identifies the exact safety-analysis episteme and its hazard, guard, and recovery claims; relates the relied-on evidence through A.10; and uses B.3 when the assurance claim or material-reliance threshold is current. The operational method, state transitions, and flow relations remain the same exact operational basis; safety analysis and reliance are added because this claim and decision trigger them, not because every failure or recovery description requires assurance.

#### E.17.2:5.3 - Responsibility diagram and actual assignment

A responsibility-diagram episteme E concerns exact System H. Exact local reference `r_allocation : U.ViewpointRef` resolves exact `P_allocation`; `EpistemeViewpointConformanceRelation(E,P_allocation)` obtains.

**Diagram cue.** One box names `MaintainerSystemRole@Plant`. That spelling can help locate the plant-side definition; by itself it establishes neither an exact local system-role kind, an assigned-kind domain, a C.3.2 judgment, nor an assignment.

**Classification-only claim.** If a current claim says `PumpUnit-3` counts as `CoolingCirculatorSystemRole` for exact `CoolingCirculatorKindSignature-2` and `PlantSlice-7`, recover `J(PumpUnit-3, CoolingCirculatorSystemRole, CoolingCirculatorKindSignature-2, PlantSlice-7) = true` under C.3.2. No assignment is required.

**Assignment claim.** If a separate claim says admitted System S holds an assignment, first recover the exact local kind—here named `MaintainerSystemRole`—through C.3 and declare the exact assigned-kind domain—here named `PlantMaintenanceSystemRoleKindDomain`. The diagram cue identifies neither. Then recover exact `RA : MaintenanceWorkAssignment <: U.SystemRoleAssignment` under A.2.1, with S in `HolderSystemSlot`, `PlantMaintenanceSystemRoleKindDomain` as the declaration-local assigned-kind domain, and `MaintainerSystemRole` as RA's assigned-kind value.

E can assert or describe RA without becoming RA. Any responsibility of S remains a separately governed direct claim.

#### E.17.2:5.4 - One view, two publications

Module-interface view E is published as an interactive model and as a printed inspection sheet. Both publication occurrences select the same episteme edition. Their forms and carriers differ; E, its conformance occurrence, and its `U.View` membership do not.

#### E.17.2:5.5 - DDD Context Mapping method and product

A team enacts DDD Context Mapping. The way of doing is one independently admitted `U.Method` under A.3.1; an episteme that substantively describes that method may separately be a `U.MethodDescription` with the method as its exact EntityOfConcern. Neither is a TEVB viewpoint or view by its label.

First determine whether the product is a claim-bearing episteme or only a diagram, form, or carrier. A claim-bearing product called a Context Map is separately identified under C.2.1 as candidate episteme E with its own exact claim content, EntityOfConcern, and effective scheme. It becomes a `U.View` only if one exact viewpoint P admits E's EntityOfConcern and `EpistemeViewpointConformanceRelation(E,P)` obtains. Method enactment, product naming, diagram form, declaration position, publication, and visual resemblance grant no membership. If the map represents independently recovered domain regions or relations, C.29 defines that correspondence; a mere carrier remains with E.24.PUB, and the drawing makes no represented world-side relation obtain.

### E.17.2:6 - Consequences


| Gain | Cost or boundary |
|---|---|
| One project can make four familiar engineering concern positions reusable across its holons after exact local bindings exist. | Materializing L, four exact P editions, and four reference resolutions is real work; equal labels do not create cross-project reuse. |
| Viewpoint episteme, its exact target kind or conditionally selected convention structure, view episteme, and described holon remain distinct. | Authors recover P's truthful EntityOfConcern—its exact admitted target kind by default, or S only in the triggered structured branch—and exact H as EntityOfConcern(E). |
| Directly authored and generated descriptions use one conformance rule. | Query or rendering provenance cannot substitute for conformance. |
| Cross-view engineering claims keep their direct semantics. | A package or diagram cannot provide realization, allocation, or consistency by appearance. |
| Publication can evolve independently of the engineering viewpoints. | Publication forms and carriers need their own direct relations when they affect work. |

Reopen the TEVB template when its four positions no longer give a small useful engineering concern family for routine holon description. Reopen one materialized local instance when a bound P's exact target criterion or conformance rules change, or when a candidate concern cannot be expressed without changing a local binding. Author another local family instead when the concern is orthogonal rather than a replacement for the four.

### E.17.2:7 - Provisional local design rationale and source status

This edition reports no N/U/C/D coordinate result, Pareto frontier, NQD harvest, or computed dominance comparison. The four TEVB positions are a provisional local authoring cut for routine holon description. They are retained because each changes a different immediate practitioner question and none is safely recoverable from another by label alone:

| Template position | Immediate question | Why the position is locally retained |
|---|---|---|
| functional | What transformations, capabilities, effects, and input/output boundaries characterize what H can or is intended to do? | Module structure does not determine function; procedure does not establish capability or effect; responsibility does not supply transformation semantics. |
| procedural | What methods, order, state, concurrency, failure, and recovery characterize how relevant behaviour unfolds? | Functional possibility does not determine order or recovery; a method mention does not make the holon-centred view a MethodDescription or performed Work. |
| module-interface | Which constituent holons, dependencies, interfaces, compatibility conditions, substitutability rules, and change boundaries characterize construction? | Similar function does not identify the same module organization, and a diagram or port label makes no module/interface relation obtain. |
| allocation-responsibility | Which exact Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, capabilities, transformations, and separately governed responsibility relations or structures are related to the behaviour? | Neither function nor procedure says which System counts under which kind for which signature edition and slice, is assigned, has capability, participates in the transformation, or bears responsibility. The view itself performs no Work and establishes none of those relations or judgments. |

The cut is deliberately small, not claimed complete. Serious omitted branches remain visible rather than being forced into the four:

| Omitted candidate family | Current local disposition |
|---|---|
| information/data | Orthogonal when data meaning, schema, information flow, or information lifecycle is the primary action-changing concern; author another exact local family rather than treating module-interface as data semantics. |
| safety/assurance | Orthogonal when hazard, safety, evidence, confidence, or reliance is current; use the applicable safety pattern, A.10 for evidence, and B.3 for assurance when those claims are current, and author a separate viewpoint family if recurring. Ordinary failure and recovery remain procedural without a universal assurance burden. |
| mission/context | Often ordinary target, use, or scope claims; author another family when mission or environment becomes a recurring independent comparison and selection concern. |
| deployment/operational | May use procedural, module-interface, and allocation positions together; author another family when deployment topology or operational environment changes a distinct recurring action. |
| business/usage/publication | Keep service, promise, stakeholder-use, and publication questions under their direct patterns; author another family only when their recurring concern cannot be represented without changing the TEVB positions. |

**Source status.** ISO 42010 is historical vocabulary lineage only. Function–behaviour–structure language is also lineage and a recognition aid, not evidence for this exact four-position cut. Query or projection production uses C.2.1 to identify the candidate episteme and A.6.3 to state its construction; it is not an external source for viewpoint selection. Responsibility/allocation is retained because it changes the practical question and avoids a recurrent function/actor collapse, not because an unreported engineering-practice harvest selected it. SysML v2 is deliberately not used as positive evidence or lineage for this selection: official status, search prominence, systems-oriented naming, and prospective scope do not supply a demonstrated current solution to this exact reusable-family problem. No unrelated modeling-language comparator is imported merely because it is current elsewhere.

**Reopen.** Re-run source selection and a bounded actual-use comparison when an exact current problem-solving source or exercised project result supplies a better reusable family; when routine project replay repeatedly needs one omitted branch at the same frequency and action impact as the four; when two retained positions cease to change different actions; or when the four-position template produces more selection work than it saves. Until such evidence exists, call the cut provisional local rationale and never a computed frontier.

### E.17.2:8 - Pattern contributions and boundaries

- **E.17.2** provides the four-position project authoring template and its concern distinctions. It supplies no exact L, declaration, reference, P edition, or membership occurrence; a project materializes those objects through the patterns below.
- Use **E.17.0** for `U.Viewpoint` and `U.View` membership, `ViewpointConventionDependencyRelation`, `EpistemeViewpointConformanceRelation`, and ordinary-use stops.
- Use **E.17.1** for catalogue L, local family declarations, and packaging by exact viewpoint references; it admits no bundle U-kind.
- Use **C.2.1** to identify every constituent episteme, Q, P, candidate E, assertion, and description.
- Use **C.13** to construct exact collections and **A.22** to select structures.
- Use **A.6.3** only for optional source-to-receiving viewing construction; that construction does not grant view membership.
- Use **A.3.1/A.3.2** for Methods and MethodDescriptions, **A.3.4** for transformations, **A.2** for local system-role kinds, **C.3.2** for their `KindSignature` declarations, four-input classification judgments, and optional extensions, **A.2.1** for exact `U.SystemRoleAssignment` species and occurrences, **A.2.2** for capabilities, **A.2.7** for relations among system-role kinds, the direct responsibility pattern for responsibility, **E.18** for transformation flows, and **B.1.1** plus applicable module or interface patterns for dependency, module, and interface relations.
- Use **E.24.PUB** for publication objects and relations and **C.29** for representations of independently recovered objects or relations.
- Use **A.6.RCD** to state or derive a needed relation claim, or return its exact blocker, when current predicates are insufficient.

### E.17.2:9 - Conformance checklist

1. The pattern is used as an authoring template until one project supplies exact `<G_L, K_L, R_L>`, ordinary `f_eng`, four exact `r_* : U.ViewpointRef` values, four exact P targets, and their resolution path; labels or variable names fill none of those positions.
2. Exact `G_L` contains one local declaration claim block with the four bound references; it is not an inferred bundle U-kind, separate bundle entity, embedded viewpoint value, view, document, form, carrier, or publication occurrence.
3. Each reader-facing viewpoint name is only the project-local designator of exact P; designator, reference, P, any structured-branch S, and declaration position remain distinct.
4. Each P passes all five E.17.0 viewpoint-membership conditions. It uses the self-contained branch by default; an exact C/Q/S witness is required only when separately versioned convention organization changes a named action.
5. In a triggered structured branch, each witness names exact least-powerful constituent editions, every selected obtaining dependency occurrence, ordinary `Q_org`, exact A.22-selected S, and ordinary P; optional dependency-use decisions and evaluations remain named-use neighbors.
6. Each concern episteme has one independently recoverable EntityOfConcern. Every relation claim names its exact predicate, participants, obtaining test, and applicable pattern; a multi-subject phrase is split or retained as a constraint claim, never promoted to a hidden group kind.
7. Candidate E has one exact holon H as EntityOfConcern and becomes `U.View` only through obtaining `EpistemeViewpointConformanceRelation(E,P)`.
8. A singular describing-use reference selects P without entering E/P identity or conformance; A.6.3 construction, declaration membership, naming, evaluation, rendering, and publication grant no membership.
9. Every procedural failure or recovery claim has an exact operational subject and admitted Method, state-transition, or transformation-flow basis. A safety-analysis episteme, A.10 evidence path, or B.3 assurance branch appears only for a safety-bearing claim or named reliance. Procedural views remain distinct from MethodDescriptions and Work; allocation-responsibility views keep the local system-role kind, any four-input C.3.2 classification judgment, optional extension, assignment, performer System, and responsibility relation distinct; module-interface views remain distinct from direct module relations or functional views.
10. DDD Context Mapping remains a `U.Method`; a product called Context Map is a separately identified episteme and becomes a View only through exact E/P conformance.
11. Every cross-view relation names its exact predicate, participants, obtaining test, and applicable pattern; a diagram edge, correspondence label, citation, shared holon, or common template is insufficient.
12. Form expression, carrier bearing, five-participant publication and recurrence, rendering work, C.29 representation, and any publication-side viewpoint remain distinct and make no represented world-side relation obtain.
13. Cross-project reuse is claimed only for the same resolved L, declaration, and exact member references. Equal TEVB position labels or independently filled templates establish no shared family.
14. Later ordinary reuse resolves the admitted L and declaration, then one needed P, and stops after the readable conformance judgment unless a named receiving work needs more structure. It reopens full catalogue constitution only under the E.17.1:4.2 triggers.

### E.17.2:End

