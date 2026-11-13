## E.17.2 - TEVB - Project-local Typical Engineering Viewpoint Bundle Template for Holons
> **Status:** Stable
> **Type:** Authoring template; no TEVB catalogue value is shipped by this pattern.

**Use this when.** A project wants to author a small local family of engineering viewpoints for descriptions of holons, so that functional, procedural, allocation-responsibility, and module-interface claims remain distinguishable and comparable.

**What goes wrong if missed.** One functional, procedural, responsibility or structural label, or a label for a diagram or report, can come to mean several things at once. People may take it for the viewpoint, the view, the described holon, a publication face, or proof of an engineering relation. The opposite failure is to require all four viewpoints and their full authoring machinery for one local reading.

**What this buys.** TEVB supplies a four-position authoring template. Once a project has constituted its own catalogue L and bound four local references to four viewpoint epistemes, that project can reuse the resulting local family while keeping candidate episteme, described holon, conformance, cross-view relations, and publication separate. One use may select just one bound member.

**First action.** Resolve the already admitted project-local catalogue edition L and the local declaration designated by `f_eng`, then resolve only the `U.ViewpointRef` needed for the present question. If L or the declaration is new, missing, or disputed, use E.17.1:4.2 to constitute or verify `<G_L, K_L, R_L>` for that edition. If a needed P edition is missing, author and admit it under E.17.0 before binding its reference.

Reuse those results while the catalogue edition, effective scheme, declaration, and relied-on premises remain unchanged.

**First useful result.** A materialized local family has one project-local L, ordinary family designator `f_eng`, four local references `r_functional`, `r_procedural`, `r_allocation`, and `r_module`, and four local P targets to which those references resolve under `R_L`. For a later use, the result consists of the admitted L and declaration, one needed reference resolving one P, and a readable E/P conformance judgment.

Before the four bindings exist, the result is only an authoring template, not a reusable family value.

**Ordinary stop.** For materialization, stop when the local catalogue triple, declaration claim block, four reference bindings, and four P targets are recoverable. For later use, stop after resolving the admitted L and declaration, the one needed P, and its E/P judgment. Reopen full catalogue constitution only under the E.17.1:4.2 triggers.

Add another member, structured viewpoint-authoring witness, C.13/A.22 organization, construction history, cross-view relation, evaluation, or publication object only when a named receiving use depends on it.

**Not this pattern when.** Keep a one-off viewpoint local when no recurring four-position family is needed. Author another E.17.1 declaration for safety, assurance, information, mission, deployment, business, publication, or architecture-framework-specific concerns outside the four TEVB positions. TEVB is not a universal architecture framework.

> **Tech-name:** `TEVB` — the template name, not a family designator or catalogue value
> **Plain-name:** project-local typical engineering viewpoint bundle template for holons

**Product-form boundary.** This pattern ships no catalogue edition, effective scheme, family designator, `U.ViewpointRef`, or viewpoint episteme edition. Every `L`, `f_eng`, `r_*`, `P_*`, `C_*`, `Q_*`, and `S_*` symbol below is a variable in the template until one project supplies and verifies its binding.

Equal labels in two projects establish no shared family or cross-project reuse. Such reuse begins only when both uses resolve the same L and member references.

The template does not by itself constitute an architecture framework, a `U.Method`, a set of publication forms, or an additional entity alongside catalogue L and its referenced P editions. It prescribes no modelling notation, storage format, or tool API.

**Builds on:** E.17.0 for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View`; E.17.1 for bundle packaging by `U.ViewpointRef`; C.2.1 for episteme identity; C.13 for the constituent collections of viewpoint conventions; A.22 for their selected structures; A.6.6 and E.17.0 for constituent-dependency relations; A.6.3 for optional view construction; E.24.PUB for publication.

**Used by after a project materializes the bindings:** E.18 transformation-flow descriptions, E.17 multi-view publication, architecture-description patterns, and domain patterns that need that local engineering concern family for holons.

### E.17.2:1 - Problem frame

Engineering descriptions repeatedly ask four different questions about one holon:

1. **Functional:** what transformations, capabilities, and effects characterize what the holon can or is intended to do?
2. **Procedural:** what methods, orders, states, concurrency, failures, and recovery rules characterize how relevant behavior unfolds?
3. **Allocation-responsibility:** which admitted Systems and local system-role kinds relate to the holon’s behavior? Which current C.3.2 judgments, obtaining assignments, capabilities, transformations, and separately governed responsibility relations or selected structures relate to it? Each such C.3.2 judgment says that one System counts under a kind for one `KindSignature` edition and context slice.
4. **Module-interface:** what constituent holons, interfaces, dependency structures, substitutability conditions, and change rules characterize its construction?

The questions recur across hardware, software, organizations, and mixed systems. Their answers may appear as prose, models, diagrams, cards, or publications, but those forms do not identify the viewpoints or make an episteme a view.

### E.17.2:2 - Problem

How can engineers reuse a compact family of these four concern-bearing viewpoints while keeping all of the following distinct:

- the holon described by a candidate episteme;
- the viewpoint episteme and its target kind or, only in the triggered structured branch, its selected convention structure;
- the candidate episteme and any dependent `U.View` membership;
- a viewpoint selected for one describing use;
- the Methods, transformations, selected structures, local system-role kinds, assignments, modules, and interfaces mentioned in the claims;
- any viewing construction, evaluation, cross-view relation, publication occurrence, form, representation, or carrier?

Without that separation, a label such as `functional view` can stand for a concern convention, a diagram, a query output, a report section, or a claim about a system. The next engineering action then relies on the wrong object.

### E.17.2:3 - Forces

| Force | Tension |
|---|---|
| Reuse vs exact edition | Teams need stable families, while conformance depends on exact claim-bearing viewpoint editions. |
| Small core vs subject breadth | The four positions should be learnable. Safety, mission, data, deployment and other domain concerns can require different positions. |
| Holon-centered view vs concern objects | A view can concern one holon while its claims designate Methods, transformations, local system-role kinds, assignments, capabilities, and structures through relations. |
| Familiar engineering language vs kind precision | `functional view` should remain readable without turning `functional`, `view`, or a diagram label into an intrinsic kind by spelling. |
| Direct authoring vs generated descriptions | Both can yield conforming views; neither route establishes conformance by itself. |
| Cross-view comparison vs invented links | Comparable views need direct relations, not a universal correspondence record or matching diagram positions. |
| Viewpoint reuse vs publication reuse | Many unpublished epistemes can conform to the same viewpoint, and each episteme may later have many publication forms; packaging must not redefine membership. |

### E.17.2:4 - Solution

**Local mantra.** To materialize a local instance, constitute L and bind `f_eng`, four references, and four P targets. To use an admitted instance, resolve L, its declaration, and only the needed reference. Then identify the holon-centered candidate E and test its conformance under E.17.0. For any additional engineering or publication claim, keep its objects and relations distinct and use the applicable pattern.

Use the mantra to recall the procedure. The rules below specify the positions, how to materialize a local family, how to use the conformance test and when to stop. Their variables do not denote repository-shipped values.

#### E.17.2:4.1 - Bind one project-local declaration without embedding viewpoint values

One project instantiates the template only by supplying these bindings:

```text
L_local = catalogue episteme identified by <G_L, K_L, R_L>
f_eng   = ordinary family designator interpreted under R_L

local declaration claim block in G_L:
  familyDesignator = f_eng
  targetKindCompatibility = U.Holon target-kind criterion
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

The four `r_*` variables must be bound to local `U.ViewpointRef` values. The four `P_*` variables must be bound to already admitted viewpoint episteme editions. `f_eng` and any reader-facing names are ordinary designators under `R_L`. Designator, reference, viewpoint episteme, any optional selected viewpoint-convention structure, declaration claim block, and catalogue L remain distinct.

The template does not admit P as `U.Viewpoint`, make another episteme a `U.View`, or establish publication. Use E.17.0 for both dependent-kind membership tests, E.17.1 for L and its declaration claim block, and E.24.PUB for publication.

The four positions are fixed for a project declaration that claims conformance to this template. Safety, assurance, information, mission, deployment, business, and publication-oriented viewpoints use another local E.17.1 declaration or a later project catalogue edition with an explicitly revised declaration. A recurring label alone neither binds nor extends `f_eng`.

#### E.17.2:4.2 - Materialize each local viewpoint before binding its reference

Each `P_*` variable must be bound to one C.2.1 episteme that independently gains `U.Viewpoint` membership under E.17.0.

Start with E.17.0's self-contained branch: give P its admitted target kind as EntityOfConcern and put the complete fixed target-kind, concern, admissibility, semantic-form, coverage, consistency, completeness, omission, and describing-use test in its ClaimGraph.

Use the structured C/Q/S branch below only when separately versioned convention components and their organization change a named project reuse, comparison, or maintenance action.

For any one of the four positions:

1. identify the target kind and the complete fixed claims required by E.17.0;
2. in the ordinary self-contained branch, constitute P with that target kind as EntityOfConcern;
3. in the independently triggered structured branch, identify convention epistemes under their least-powerful admitted kinds, construct collection C under C.13, recover every selected obtaining direct relation, state ordinary constraint episteme `Q_org`, let a system perform the A.22 selection work, and identify selected structure S. Constitute P with S as EntityOfConcern;
4. apply the five E.17.0 viewpoint-membership conditions to the resulting P, then bind its project-local reader designator and `U.ViewpointRef`; and
5. record the resolution under `R_L` in the local declaration claim block.

No constituent, `Q_org`, or P becomes a `U.Signature` merely to fit this template. A constituent is a `U.MethodDescription` only when it describes one independently admitted method under A.3.2.

Selection work and its result remain separate from C, S, P, and selected relation occurrences. The table below gives optional recipes with template variables. A project supplies the values.

The four template positions use these concern objects and patterns when one project authors its P editions:

| Template position | Concern subjects and applicable claim-specific patterns |
|---|---|
| functional | `U.Transformation` under A.3.4; the independently identified holder System, with its qualified ability stated in the concern episteme under A.2.2; transformation-flow `U.Structure` under E.18 and A.22 |
| procedural | `U.Method` under A.3.1; transformation-flow `U.Structure` under E.18 and A.22; operational-state `U.Structure` under A.19.SPR and A.22 |
| allocation-responsibility | local system-role kind under A.2; when the view claims that one System counts under that kind, the separate C.3.2 judgment over candidate, kind, `KindSignature` edition, and context slice; an optional `KindExtension` representation only for a named set-consuming use; obtaining assignment occurrence under a directly declared `U.SystemRoleAssignment` species when an assignment claim is current; `SystemRoleKindRelationStructure` under A.2.7 and A.22; the independently identified holder System, with its qualified ability stated in the concern episteme under A.2.2; `U.Transformation` under A.3.4; an independently governed responsibility relation or selected structure when responsibility is current |
| module-interface | dependency `U.Structure` under B.1.1 and A.22; every module, interface, boundary, substitutability, or change-policy relation separately names its predicate, participants, obtaining test, and applicable pattern |

Keep these claim boundaries explicit:

- **Functional:** functioning status, input/output boundary, and functional-port coverage remain claims in `E_rule.functionalCoverage` unless the claim identifies a separate EntityOfConcern and states its predicate, participants, and obtaining test. A concern episteme about a Transformation, a holder's ability or a transformation-flow Structure has respectively that Transformation, holder System or Structure as EntityOfConcern. State the ability in its claim content. Select an ability-assertion episteme itself as subject only for a question about that assertion. When several of these concerns are needed, keep their subject accounts distinct. There is no universal function entity or one multi-subject concern episteme.
- **Procedural:** every method, order, state, concurrency, failure, and recovery claim designates its operational subject and the admitted method, state-transition, or transformation-flow relation that gives the claim meaning. A bounded coverage rule may remain in P, but a candidate E cannot satisfy it through vocabulary alone. Method mention grants no MethodDescription membership, state wording is not a Structure, procedural content is not performed work, and safety evidence is added only for a safety-bearing claim or named reliance.
- **Allocation-responsibility:** holder System, local system-role kind, four-input C.3.2 classification judgment, optional extension representation, assignment, transformer relation, allocation, segregation, capability, and responsibility remain separate typed claims or concern objects. A local system-role kind is not a classification judgment or assignment. Classification or assignment establishes neither responsibility nor Work.
- **Module-interface:** A.6.M `ModuleInterfaceClaim` remains claim content. Whole-holon, candidate-module, boundary, independently identified `InterfaceSpecification` episteme and its resolving reference, substitutability, and change-policy content stays in the coverage-rule episteme until a module-relation declaration supplies participant kinds, predicate, obtaining rule, and occurrence identity and current facts satisfy it. The claim record is not that relation and a module topic is not an EntityOfConcern.

Split any phrase spanning several subjects into separate concern epistemes, or retain it as one constraint claim over candidate content.

Give each stakeholder constituent exactly one referent—System, local system-role kind, claim-bearing C.3.2 classification-assertion episteme when that judgment is current, obtaining system-role assignment, C.13 collection-as-whole, or other independently governed subject.

A `KindExtension` remains an optional representation for a named set-consuming use, not the kind or judgment. Cite any responsibility concern through its separately governed direct predicate. Do not coerce heterogeneous constituents into Signatures merely to make the rows uniform.



The following four rows are structured-branch recipes. Every symbol is a template variable until a project binds values. A project using the ordinary self-contained P branch does not instantiate the structured recipe for that position.

| Project substrate after binding | Applied constraints, selected structure, and viewpoint episteme | Selected direct dependencies | Method and work boundary |
|---|---|---|---|
| `C_functional = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.functionalTransformation, E_concern.capability, E_concern.transformationFlowStructure, E_rule.functionalCoverage, E_rule.functionalModuleSeparation, E_rule.functionalRetargeting}` | `Q_org.functional` is an ordinary constraint episteme about C. A.22 selects `S_functional`; project `P_functional` has `EntityOfConcern=S_functional`, is assigned local reader designator `d_functional`, and passes E.17.0 viewpoint membership before `r_functional` is bound to it. | Each concern episteme depends on `E_target.tevbHolon`; `E_rule.functionalCoverage` depends on all three concern epistemes and `E_admitted.tevbEpisteme`; separation depends on functional-transformation concern; retargeting depends on the target. | No method constituent is required. A method convention enters only as `U.MethodDescription` after its method passes A.3.1. |
| `C_procedural = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.method, E_concern.transformationFlowStructure, E_concern.operationalStateStructure, E_rule.proceduralCoverage, E_rule.proceduralMethodBoundary, E_rule.proceduralNoWorkInference}` | `Q_org.procedural` is about C. A.22 selects `S_procedural`; project `P_procedural` has `EntityOfConcern=S_procedural`, is assigned local reader designator `d_procedural`, and passes E.17.0 membership before `r_procedural` is bound. | Each concern episteme depends on the target; coverage depends on all concerns and admitted-episteme kind; method boundary depends on method concern; no-work-inference depends on method and transformation-flow concerns. | Operational methods remain subjects of separate method-description epistemes. Concern selection, view construction, evaluation, and use do not form one method or workflow by mention. |
| `C_allocation = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.systemRoleKind, E_concern.systemRoleKindRelationStructure, E_concern.capability, E_concern.transformation, E_concern.responsibility, E_rule.allocationCoverage, E_rule.allocationNoWorkInference, E_rule.allocationRetargeting}`; add `E_concern.systemRoleClassification` only for an independently current four-input C.3.2 judgment, and add `E_concern.systemRoleAssignment` only for an independently current assignment claim | `Q_org.allocation` is about C. Use A.22 to select `S_allocation`; project `P_allocation` has `EntityOfConcern=S_allocation`, is assigned local reader designator `d_allocation`, and passes E.17.0 membership before `r_allocation` is bound. | Each current concern episteme depends on the target; coverage depends on all current concerns and the admitted-episteme kind; no-work-inference depends on whichever kind, classification, assignment, transformation, and responsibility concerns are current; retargeting depends on the target. | A bare *role* label, raw kind or relation reference, and raw Method are not collection members. Only current concern epistemes enter C. An allocation or analysis Method enters only through a MethodDescription episteme. |
| `C_module = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.dependencyStructure, E_rule.moduleCoverage, E_rule.interfaceTyping, E_rule.functionalModuleSeparation, E_rule.substitutabilityChange, E_rule.moduleRetargeting}` | `Q_org.module` is about C. A.22 selects `S_module`; project `P_module` has `EntityOfConcern=S_module`, is assigned local reader designator `d_module`, and passes E.17.0 membership before `r_module` is bound. | Dependency-structure concern depends on the target; coverage depends on target, dependency structure, and admitted-episteme kind; typing, functional separation, and substitutability/change depend on dependency structure; retargeting depends on target and dependency structure. | No method, work, or module relation enters by mention. A direct module or interface relation joins only after its own pattern supplies participants, obtaining law, and occurrence identity. |

Each project-bound structured witness remains independently recoverable. Constituent editions identify C. Every selected dependency occurrence passes the E.17.0 predicate. Optional `D_dependencyUse` states obtaining and named-use admissibility as separate claims. A.22 selects S from C, selected occurrences, applied Q constraints, and the use frame. P is then identified by its ClaimGraph, S EntityOfConcern, and effective scheme.

Changing only the Q edition leaves S unchanged when those selection inputs remain semantically unchanged. No topic list, citation, displayed edge, hidden O, D, template variable, or neighboring witness establishes that another structured witness meets these requirements.

The dependency relation in this table is `ViewpointConventionDependencyRelation` from E.17.0. It obtains only when interpreting or replaying the fixed claims of the dependent episteme relies on a criterion, law, public name, or method claim of the base episteme, and replacing the base edition can change that interpretation or replay. Co-membership, citation, or a visible arrow is insufficient.



When an A.22 selection judgment needs an explicit claim that one obtaining dependency occurrence is admissible for that use, identify the separate decision-use episteme described by E.17.0. Do not insert that decision, its evidence, or its evaluation result into the dependency relation or S identity.

#### E.17.2:4.3 - Keep the four concern conventions distinct

**Functional.** A conforming candidate episteme foregrounds transformations, capabilities, effects, functional elements, or transformation-flow relations of its holon. It does not identify a module structure by functional vocabulary and does not mint `U.Function`. Any neighboring responsibility claim keeps the admitted System, local system-role kind, current C.3.2 classification judgment, assignment, kind-relation structure, capability, transformation, and direct responsibility relation separate. Use A.2, C.3.2, A.2.1, A.2.7, or the direct responsibility pattern for the claim made.

**Procedural.** A conforming candidate episteme foregrounds methods, order, state, concurrency, failure, and recovery related to its holon and designates the admitted method, state-transition, or transformation-flow relations on which each claim depends. A procedural view about a holon is not a `U.MethodDescription`. That dependent kind requires one admitted method as its EntityOfConcern. Ordinary operational recovery needs no safety package unless the claim is safety-bearing or a named receiving decision relies on one.

**Allocation-responsibility.** A conforming candidate episteme foregrounds Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, relations among those kinds, capabilities, transformations, and separately governed responsibility relations or selected structures related to its holon.

A label creates no kind, classification, or assignment. A classification judgment needs its candidate, kind, `KindSignature` edition, and context slice but no assignment. The view may state that judgment, but it does not make the criterion true or create an assignment or responsibility relation.

**Module-interface.** A conforming candidate episteme foregrounds constituent holons, dependency structures, boundaries, interfaces, compatibility, substitutability, and change policy. It remains distinct from the functional viewpoint. Many modules may support one transformation, one module may support several transformations, and either description may be incomplete without becoming the other.

The following are practitioner recognition and claim-shape cues, not embedded `StakeholderFamilies` or `AllowedEpistemeKinds` fields. A reader label creates neither a system-role classification nor an assignment and enters neither viewpoint nor view identity. Every example needs its EntityOfConcern, the predicate and participants of each claimed relation, its obtaining test, and its E.17.0 conformance result.

| Template position | Typical readers or concern holders | Distinctive claim-shape and conformance cues |
|---|---|---|
| functional | System-engineering and architecture readers, product or capability owners, and reliability or performance readers inspecting capability envelopes | Look for service-capability and promise content, delivery or access and API descriptions, input/output signatures, and functional-port boundaries as separate claims about the holon. Ground bounded behavior in transformations, capabilities, or a selected transformation-flow structure. Keep service delivery Work, access relations, publications, and module interfaces separate, and do not mint `U.Function`. |
| procedural | Operations and run-time owners, control and automation engineers, and safety readers | Look for operational subjects and admitted method, state-transition, and transformation-flow relations behind order, state, concurrency, failure, and recovery claims. Where step boundaries are current, make preconditions and postconditions explicit and type-checked. Open a safety-analysis basis or A.10 evidence path only when the current claim is safety-bearing or a named receiving decision relies on it. Otherwise stop at the operational relations and ordinary failure/recovery boundary. Within that triggered branch, use B.3 only when a named assurance claim for that use is current. Keep method, method description, work plan, dated Work, calendars, and selected state or flow structures distinct. |
| allocation-responsibility | Organization and operations designers, safety or compliance readers concerned with segregation of duties, and device or system engineers | Look for the admitted System and local system-role kind. When the claim says that System counts under the kind, recover the separate four-input C.3.2 judgment. Look separately for any assignment occurrence, segregation and escalation constraints, capability and transformation claims, and responsibility relation or structure. A kind locator is neither a classification result nor an assignment. None of those claims proves responsibility, and allocation wording is not an obtaining relation. |
| module-interface | Hardware or software architects, integration and test engineers, and lifecycle or maintenance readers concerned with replaceable units | Look for module decomposition, protocols, schemas, physical connectors, APIs, interface and conformance expectations, version and change policies, dependency and allowed-coupling structures, replaceability and variation points, and explicit functional-to-module correspondence or allocation without identity by default. Ports or connector diagrams do not establish module/interface relations; state and test each direct relation separately, and use A.6.4 for any functional-to-module retargeting. |

#### E.17.2:4.4 - Recognize holon-centered TEVB views by conformance

TEVB keeps two subjects explicit:

| Episteme | EntityOfConcern | Job |
|---|---|---|
| viewpoint episteme P | admitted target kind in the self-contained branch, or selected viewpoint-convention structure S only in a triggered structured branch | states the target-kind criterion, concerns, admitted episteme kinds, semantic-form, coverage, consistency, completeness, omission, and describing-use rules |
| candidate or view episteme E | one holon H admitted by P's target criterion | states claims about H. Whenever it relates H to another engineering object, it names the predicate, participants, and obtaining test |

`EpistemeViewpointConformanceRelation(E,P)` must obtain under the fixed E.17.0 predicate. Only then is the same episteme E a `U.View`. Direct authoring, query execution, A.6.3 construction, a reader-facing label, declaration membership, or publication does not establish that membership. A reader-facing system-role label also establishes neither the local kind nor a C.3.2 classification judgment or assignment.

For one current describing use, its use qualification carries a single `viewpointRef : U.ViewpointRef` resolving P under the effective reference scheme. Any reader-facing viewpoint name is only P's ordinary designator. The use qualification, designator, reference, and P remain distinct. Selection identifies neither E nor H, establishes no conformance, and adds no conformance participant or episteme-identity field.

Recover H only as `EntityOfConcern(E)` from E's C.2.1 constitution. Do not import a legacy context tuple, generic bounded-context object, or model-use identity field into E, P, S, conformance, or selection. Another use may select another P while E remains unchanged. Several selected viewpoints require a C.13 collection of their references rather than one overloaded reference.

If a user needs a view whose subject is a Method, local system-role kind, system-role assignment, transformation, responsibility relation, or structure rather than H, identify another candidate episteme with that EntityOfConcern and use a viewpoint whose target-kind criterion admits it. Do not silently retarget a holon-centered TEVB view.

#### E.17.2:4.5 - Import, subset, and extend one materialized local instance

An E.17.0 multi-view use can import TEVB only after it resolves one admitted project catalogue edition L, retrieves the declaration claim block designated by local `f_eng`, and resolves the imported `r_*` members or subset.

Open `<G_L, K_L, R_L>` under E.17.1:4.2 only when L or the declaration is new, missing, or disputed, or a named later use consumes the catalogue constitution as premises.

`f_eng` is only an ordinary designator inside L: it identifies neither L nor any viewpoint by itself and is not a member reference. Each imported reference resolves to P under `R_L`; any reader-facing viewpoint name is only P's designator.

A local subset names retained references, preserves `<editionDesignator(L), f_eng>` provenance, and records whether each omission is unused coverage or an intentional exclusion.

If local work changes only reader-facing aliases or adds examples, keep those as naming or annex content.

If it changes a viewpoint's target criterion, concerns, admitted episteme kinds, or conformance rules, identify another viewpoint episteme edition and bind another reference as needed.

If it changes declared family membership, identify another catalogue episteme carrying the revised declaration claim block. Do not keep an old designator while changing the P it resolves under the same effective scheme.

Several local families may be used together, but each member retains its catalogue provenance and resolved viewpoint edition. Similar labels do not merge members. Two projects can claim use of the same reusable family only when they resolve the same L, declaration, and member references. Independent instances of this template remain different local families even when all four labels match.

A project may bind its local four positions to reader names such as `Functional`, `Procedural`, `Allocation-Responsibility`, and `Module-Interface`. Those names do not perform the binding. A different reference-to-position mapping is another local declaration and must not silently reuse the earlier `f_eng` under `R_L`.

#### E.17.2:4.6 - Keep cross-view relations and publication separate

A materialized local TEVB instance provides four project references. The template alone provides none. Neither instance nor template asserts correspondence among resulting views. When a later engineering use depends on a relation between a functional claim and a module claim, or between a procedural claim and a system-role-assignment claim:

1. identify the participating entities or epistemes;
2. state the realization, allocation, dependency, consistency, trace, or other direct relation claimed;
3. use the pattern that defines and tests that relation, including its obtaining law;
4. use A.6.RCD when no existing direct or derived relation is sufficient;
5. recover any representation's correspondence to that relation; use A.6.3.RT/A.6.3.RT.OE for expression construction or representation-scheme transition, adding C.29 when a mathematical inference or transfer question requires it.

If a separate receiving claim asserts dated `U.Work`, recover each actual performer through A.13 and use A.15.1 to establish the Work, Method, time, and containing System independently. Add F.6 only when that receiving claim also consumes precise assignment-bound attribution through the same obtaining A.13 assignment. Missing or failed F.6 alone leaves independently admitted Work intact. Those Work and optional attribution facts are neither participants in the cross-view relation nor prerequisites for identifying it.

E.17 and E.24.PUB may publish a selected TEVB view edition through `PublicationExpressionRelation(selectedEdition,publicationExpression,boundedUseDeclaration)`, `PublicationExpressionBearingRelation(presentationCarrier,publicationExpression)`, and the five-participant `EpistemePublicationRelation(selectedEdition,audienceDeclaration,boundedUseDeclaration,publicationExpression,presentationCarrier)`. Identify the expression and carrier independently under their own domains.

When a reusable publication form is selected, establish `PublicationFormConformanceRelation(publicationExpression,publicationForm)`. The same expression witnesses the corresponding form-mediated expression and bearing relations.

Each exact relation retains its own participant set and maximal continuous obtaining interval; changing a participant or restoring its predicate after a gap yields another occurrence without reidentifying unchanged E or P. Broader availability through permitted expressions or carriers can continue when an exact publication changes.

Rendering, printing, upload, or carrier manipulation is separate system-performed `U.Work`. A representation retains its correspondence to independently recovered objects or relations. C.29 adds the conditions for a mathematical inference or transfer.

A publication-side viewpoint, when current, is another viewpoint episteme selected by reference—not a TEVB position label reused as a form or file name. View episteme, viewpoint episteme, construction, conformance, form, carrier, publication, rendering, and representation remain distinct. Publication and representation make no represented world-side relation obtain.

### E.17.2:5 - Worked cases

The cases below assume one hypothetical project has already constituted `L_local`, bound `f_eng`, and resolved `r_functional -> P_functional`, `r_procedural -> P_procedural`, `r_allocation -> P_allocation`, and `r_module -> P_module` under `R_L`. They demonstrate a materialized local instance. They do not assert that these values exist in the repository or in another project.

#### E.17.2:5.1 - Four views of a processing plant

The plant `Plant_X : U.System` is the EntityOfConcern of four separately identified epistemes.

- E1 states transformations, capabilities, material-flow effects, and functional boundaries. `r_functional` resolves `P_functional`; E1 conforms to that P and is a functional `U.View`.
- E2 states claims about admitted method `PlantOperation`, A.19.SPR operational-state structure `PlantRunState`, and E.18 transformation-flow structure `PlantRunFlow`. Its order, failure, and recovery claims designate the transition conditions and flow relations in those structures. It conforms to `P_procedural`. It is not a method description because its EntityOfConcern is the plant. No safety-bearing claim or named reliance is present in this case, so no safety-analysis, A.10, or B.3 branch is opened.
- E3 states that `PumpUnit-3` counts as local kind `CoolingCirculatorSystemRole` in the plant slice through a separate C.3.2 judgment over the candidate, kind, `KindSignature` edition, and slice. That claim needs no assignment. E3 separately states any obtaining assignments, capabilities, transformations, and governed responsibility structures that are current. It conforms to `P_allocation`. Neither E3 nor `P_allocation` makes the classification criterion true or creates an assignment or responsibility relation.
- E4 states constituent equipment holons, dependency structure, pipes, interfaces, substitutability, and change policy. It conforms to `P_module`. E4 remains separate from the diagram rendering in which it is published.

The four conformance occurrences make E1-E4 views. Their shared holon and common local declaration do not establish any cross-view realization or consistency relation. Those claims are tested separately.

#### E.17.2:5.2 - Query output missing a required concern

A query constructs episteme Y from plant model X, and A.6.3 records that construction. Y is labelled `functional view`, but it omits the output-condition coverage required by `P_functional`. Y does not conform to that P and is not a `U.View` under it. A new edition with repaired claim content becomes a `U.View` under that P if it passes the predicate.

#### E.17.2:5.2.1 - Ordinary non-safety jam recovery

Candidate procedural episteme `E_jamRecovery` concerns conveyor system H. Its ClaimGraph designates admitted method `ClearJam`, an operational-state structure with `Running`, `Blocked`, and `Resetting` positions, the transition conditions between those positions, and the E.18 flow relation that resumes only after the blockage sensor is clear.

These method, state, and flow facts supply the operational basis for its failure-and-recovery claims. If `EpistemeViewpointConformanceRelation(E_jamRecovery,P_procedural)` obtains, `E_jamRecovery` is a procedural `U.View`.

No claim in this case is safety-bearing, no receiving decision relies on a safety analysis, and no evidence or assurance result is requested. Therefore neither an A.10 evidence path nor a B.3 assurance branch is opened. A later actual clearing remains separately identified `U.Work`.

#### E.17.2:5.2.2 - Safety-triggered recovery use

Suppose a second claim says that restarting H after the same jam is safe for an exposed operator, and a named restart decision relies on that proposition. The project now identifies the safety-analysis episteme and its hazard, guard, and recovery claims; relates the relied-on evidence through A.10; and uses B.3 only when a named assurance claim for the restart use is current.

If the applicable safety rule or restart decision requires assurance, state that claim, its target, and its named use before applying B.3.

The operational method, state transitions, and flow relations remain the same operational basis. Safety analysis and reliance are added because this claim and decision trigger them, not because every failure or recovery description requires assurance.

#### E.17.2:5.3 - Responsibility diagram and actual assignment

A responsibility-diagram episteme E concerns System H. Local reference `r_allocation : U.ViewpointRef` resolves `P_allocation`; `EpistemeViewpointConformanceRelation(E,P_allocation)` obtains.

**Diagram cue.** One box names `MaintainerSystemRole@Plant`. That spelling can help locate the plant-side definition. By itself it establishes neither a local system-role kind, an assigned-kind domain, a C.3.2 judgment, nor an assignment.

**Classification-only claim.** If a current claim says `PumpUnit-3` counts as `CoolingCirculatorSystemRole` for `CoolingCirculatorKindSignature-2` and `PlantSlice-7`, recover `J(PumpUnit-3, CoolingCirculatorSystemRole, CoolingCirculatorKindSignature-2, PlantSlice-7) = true` under C.3.2. No assignment is required.

**Assignment claim.** If a separate claim says admitted System S holds an assignment, first recover the local kind (here `MaintainerSystemRole`) through C.3 and declare the assigned-kind domain (here `PlantMaintenanceSystemRoleKindDomain`). The diagram cue identifies neither. Then recover `RA : MaintenanceWorkAssignment <: U.SystemRoleAssignment` under A.2.1, with S in `HolderSystemSlot`, `PlantMaintenanceSystemRoleKindDomain` as the declaration-local assigned-kind domain, and `MaintainerSystemRole` as RA's assigned-kind value.

E can assert or describe RA without becoming RA. Any responsibility of S remains a separately governed direct claim.

#### E.17.2:5.4 - One view, two publications

Module-interface view E is published as an interactive model and as a printed inspection sheet. Both publication occurrences select the same episteme edition. Their forms and carriers differ. Both publications involve the same E, its conformance occurrence, and its `U.View` membership.

#### E.17.2:5.5 - DDD Context Mapping method and product

A team enacts DDD Context Mapping. The way of doing is one independently admitted `U.Method` under A.3.1. An episteme that substantively describes that method may separately be a `U.MethodDescription` with the method as its EntityOfConcern. Neither is a TEVB viewpoint or view by its label.

First determine whether the product is a claim-bearing episteme or only a diagram, form, or carrier. A claim-bearing product called a Context Map is separately identified under C.2.1 as candidate episteme E with its own claim content, EntityOfConcern, and effective scheme.

It becomes a `U.View` only if one viewpoint P admits E's EntityOfConcern and `EpistemeViewpointConformanceRelation(E,P)` obtains. Method enactment, product naming, diagram form, declaration position, publication, and visual resemblance grant no membership.

If the map represents independently recovered domain regions or relations, recover how its elements correspond to those subjects. Use A.6.3.RT/A.6.3.RT.OE for constructing the expression or changing its representation scheme. Add C.29 when a mathematical inference or transfer depends on that correspondence. A carrier remains with E.24.PUB, and the drawing makes no represented world-side relation obtain.

### E.17.2:6 - Consequences


| Gain | Cost or boundary |
|---|---|
| One project can make four familiar engineering concern positions reusable across its holons after local bindings exist. | Materializing L, four P editions, and four reference resolutions takes work. Equal labels do not create cross-project reuse. |
| Viewpoint episteme, its target kind or conditionally selected convention structure, view episteme, and described holon remain distinct. | Authors recover P's truthful EntityOfConcern—its admitted target kind by default, or S only in the triggered structured branch—and H as EntityOfConcern(E). |
| Directly authored and generated descriptions use one conformance rule. | Query or rendering provenance cannot substitute for conformance. |
| Cross-view engineering claims keep their direct semantics. | A package or diagram cannot provide realization, allocation, or consistency by appearance. |
| Publication can evolve independently of the engineering viewpoints. | Publication forms and carriers need their own direct relations when they affect work. |

Reopen the TEVB template when its four positions no longer give a small useful engineering concern family for routine holon description.

Reopen one materialized local instance when a bound P's target criterion or conformance rules change, or when a candidate concern cannot be expressed without changing a local binding. Author another local family instead when the concern is orthogonal rather than a replacement for the four.

### E.17.2:7 - Provisional local design rationale and source status

The four TEVB positions are a provisional local choice for authoring routine holon descriptions. They are retained because each changes a different immediate practitioner question and none can reliably be inferred from another by label alone:

| Template position | Immediate question | Why the position is locally retained |
|---|---|---|
| functional | What transformations, capabilities, effects, and input/output boundaries characterize what H can or is intended to do? | Module structure does not determine function; procedure does not establish capability or effect; responsibility does not supply transformation semantics. |
| procedural | What methods, order, state, concurrency, failure, and recovery characterize how relevant behaviour unfolds? | Functional possibility does not determine order or recovery; a method mention does not make the holon-centred view a MethodDescription or performed Work. |
| module-interface | Which constituent holons, dependencies, interfaces, compatibility conditions, substitutability rules, and change boundaries characterize construction? | Similar function does not identify the same module organization, and a diagram or port label makes no module/interface relation obtain. |
| allocation-responsibility | Which Systems, local system-role kinds, current C.3.2 classification judgments, obtaining assignments, capabilities, transformations, and separately governed responsibility relations or structures are related to the behaviour? | Neither function nor procedure says which System counts under which kind for which signature edition and slice, is assigned, has capability, participates in the transformation, or bears responsibility. The view establishes none of those relations or judgments. |

The template uses four positions to keep this family small and makes no claim to completeness. The table identifies important concerns outside the four:

| Omitted candidate family | Current local disposition |
|---|---|
| information/data | Orthogonal when data meaning, schema, information flow, or information lifecycle is the primary action-changing concern; author another local family rather than treating module-interface as data semantics. |
| safety/assurance | Orthogonal when hazard, safety, evidence, confidence, or reliance is current; use the applicable safety pattern, A.10 for evidence, and B.3 only when a named assurance claim for that use is current, and author a separate viewpoint family if recurring. Ordinary failure and recovery remain procedural without a universal assurance burden. |
| mission/context | Often ordinary target, use, or scope claims; author another family when mission or environment becomes a recurring independent comparison and selection concern. |
| deployment/operational | May use procedural, module-interface, and allocation positions together; author another family when deployment topology or operational environment changes a distinct recurring action. |
| business/usage/publication | Keep service, promise, stakeholder-use, and publication questions under their direct patterns; author another family only when their recurring concern cannot be represented without changing the TEVB positions. |

**Source status.** ISO 42010 is historical vocabulary lineage only. Function–behaviour–structure language is also lineage and a recognition aid, not evidence for this four-position cut. Query or projection production uses C.2.1 to identify the candidate episteme and A.6.3 to state its construction. That construction supplies no external basis for choosing the viewpoints.

Responsibility/allocation is retained because it changes the practical question and avoids a recurrent function/actor collapse.

**Reopen.** Re-run source selection and a bounded actual-use comparison when a current problem-solving source or exercised project result supplies a better reusable family, when routine project replay repeatedly needs one omitted branch at the same frequency and action impact as the four, when two retained positions cease to change different actions, or when the four-position template produces more selection work than it saves. Until such evidence exists, call the cut provisional local rationale and never a computed frontier.

### E.17.2:8 - Pattern contributions and boundaries

- **E.17.2** provides the four-position project authoring template and its concern distinctions. It supplies no L, declaration, reference, P edition, or membership occurrence. A project materializes those objects through the patterns below.
- Use **E.17.0** for `U.Viewpoint` and `U.View` membership, `ViewpointConventionDependencyRelation`, `EpistemeViewpointConformanceRelation`, and ordinary-use stops.
- Use **E.17.1** for catalogue L, local family declarations, and packaging by viewpoint references. E.17.1 admits no bundle U-kind.
- Use **C.2.1** to identify every constituent episteme, Q, P, candidate E, assertion, and description.
- Use **C.13** to construct collections and **A.22** to select structures.
- Use **A.6.3** only for optional source-to-receiving viewing construction; that construction does not grant view membership.
- Use **A.3.1/A.3.2** for Methods and MethodDescriptions, **A.3.4** for transformations, **A.2** for local system-role kinds, **C.3.2** for their `KindSignature` declarations, four-input classification judgments, and optional extensions, **A.2.1** for `U.SystemRoleAssignment` species and occurrences, **A.2.2** for capabilities, **A.2.7** for relations among system-role kinds, the direct responsibility pattern for responsibility, **E.18** for transformation flows, and **B.1.1** plus applicable module or interface patterns for dependency, module, and interface relations.
- Use **E.24.PUB** for publication objects and relations, **A.6.3.RT/A.6.3.RT.OE** for expression construction and representation-scheme transition, and **C.29** for a mathematical lens over independently recovered objects or relations.
- Use **A.6.RCD** to state or derive a needed relation claim, or return its blocker, when current predicates are insufficient.

### E.17.2:9 - Conformance checklist

1. The pattern is used as an authoring template until one project supplies `<G_L, K_L, R_L>`, ordinary `f_eng`, four `r_* : U.ViewpointRef` values, four P targets, and their resolution path. Labels or variable names fill none of those positions.
2. `G_L` contains one local declaration claim block with the four bound references; it is not an inferred bundle U-kind, separate bundle entity, embedded viewpoint value, view, document, form, carrier, or publication occurrence.
3. Each reader-facing viewpoint name is only the project-local designator of P; designator, reference, P, any structured-branch S, and declaration position remain distinct.
4. Each P passes all five E.17.0 viewpoint-membership conditions. It uses the self-contained branch by default; a C/Q/S witness is required only when separately versioned convention organization changes a named action.
5. In a triggered structured branch, each witness names least-powerful constituent editions, every selected obtaining dependency occurrence, ordinary `Q_org`, A.22-selected S, and ordinary P; optional dependency-use decisions and evaluations remain named-use neighbors.
6. Each concern episteme has one independently recoverable EntityOfConcern. Every relation claim names its predicate, participants, obtaining test, and applicable pattern; a multi-subject phrase is split or retained as a constraint claim, never promoted to a hidden group kind.
7. Candidate E has one holon H as EntityOfConcern and becomes `U.View` only through obtaining `EpistemeViewpointConformanceRelation(E,P)`.
8. A singular describing-use reference selects P without entering E/P identity or conformance; A.6.3 construction, declaration membership, naming, evaluation, rendering, and publication grant no membership.
9. Every procedural failure or recovery claim has an operational subject and admitted Method, state-transition, or transformation-flow basis. A safety-analysis episteme or A.10 evidence path appears only for a safety-bearing claim or named reliance. Within that branch, use B.3 only when a named assurance claim for that use is current. Procedural views remain distinct from MethodDescriptions and Work. Allocation-responsibility views keep the local system-role kind, any four-input C.3.2 classification judgment, optional extension, assignment, performer System, and responsibility relation distinct. Module-interface views remain distinct from direct module relations or functional views.
10. DDD Context Mapping remains a `U.Method`; a product called Context Map is a separately identified episteme and becomes a View only through E/P conformance.
11. Every cross-view relation names its predicate, participants, obtaining test, and applicable pattern; a diagram edge, correspondence label, citation, shared holon, or common template is insufficient.
12. Form expression, carrier bearing, five-participant publication and recurrence, rendering work, mathematical representation under C.29, and any publication-side viewpoint remain distinct and make no represented world-side relation obtain.
13. Cross-project reuse is claimed only for the same resolved L, declaration, and member references. Equal TEVB position labels or independently filled templates establish no shared family.
14. Later ordinary reuse resolves the admitted L and declaration, then one needed P, and stops after the readable conformance judgment unless a named receiving work needs more structure. It reopens full catalogue constitution only under the E.17.1:4.2 triggers.

### E.17.2:End
