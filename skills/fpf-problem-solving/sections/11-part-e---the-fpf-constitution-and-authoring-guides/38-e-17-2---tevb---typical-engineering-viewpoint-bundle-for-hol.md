## E.17.2 - TEVB - Typical Engineering Viewpoint Bundle for Holons
> **Status:** Stable

**Use this when.** A team needs one small reusable family of engineering viewpoints for descriptions of a holon, so that functional, procedural, allocation-responsibility, and module-interface claims remain distinguishable and comparable.

**First useful result.** One exact `U.ViewpointBundleLibrary` edition and its exact TEVB bundle edition, whose `ViewFamilyId` is `VF.TEVB.ENG`; one exact holon as the candidate episteme's EntityOfConcern; and one singular exact `U.ViewpointRef` from that bundle edition resolving the exact TEVB viewpoint episteme P used for the current E/P conformance judgment. Add construction, cross-view, evaluation, or publication objects only when the next work depends on them.

> **Tech-name:** `TEVB`
> **Plain-name:** typical engineering viewpoint bundle for holons

TEVB is one governed `U.ViewpointBundle` packaged by E.17.1. It is not an architecture framework, a method, a set of publication forms, or a second entity beside its four referenced viewpoint epistemes. It fixes a conceptual viewpoint bundle but prescribes no modelling notation, storage format, or tool API.

**Builds on:** E.17.0 for `U.Viewpoint`, `EpistemeViewpointConformanceRelation`, and `U.View`; E.17.1 for bundle packaging by `U.ViewpointRef`; C.2.1 for episteme identity; C.13 for the constituent collections of viewpoint conventions; A.22 for their selected structures; A.6.6 and E.17.0 for exact constituent-dependency relations; A.6.3 for optional view construction; E.24.PUB for publication.

**Used by:** E.18 transformation-flow descriptions, E.17 multi-view publication, architecture-description patterns, and domain patterns that need a reusable engineering concern family for holons.

### E.17.2:1 - Problem frame

Engineering descriptions repeatedly ask four different questions about one holon:

1. **Functional:** what transformations, capabilities, and effects characterize what the holon can or is intended to do?
2. **Procedural:** what methods, orders, states, concurrency, failures, and recovery rules characterize how relevant behavior unfolds?
3. **Allocation-responsibility:** which exact systems, role assignments, capabilities, and responsibility structures are related to the holon's behavior?
4. **Module-interface:** what constituent holons, interfaces, dependency structures, substitutability conditions, and change rules characterize its construction?

The questions recur across hardware, software, organizations, and mixed systems. Their answers may appear as prose, models, diagrams, cards, or publications, but those forms do not identify the viewpoints or make an episteme a view.

### E.17.2:2 - Problem

How can engineers reuse a compact family of these four concern-bearing viewpoints while keeping all of the following distinct:

- the exact holon described by a candidate episteme;
- the exact viewpoint episteme and its selected convention structure;
- the candidate episteme and any dependent `U.View` membership;
- a viewpoint selected for one describing use;
- the methods, transformations, structures, roles, modules, and interfaces mentioned in the claims;
- any viewing construction, evaluation, cross-view relation, publication occurrence, form, representation, or carrier?

Without that separation, a label such as `functional view` can stand indiscriminately for a concern convention, a diagram, a query output, a report section, or a claim about a system. The next engineering action then relies on the wrong object.

### E.17.2:3 - Forces

| Force | Tension |
|---|---|
| Reuse vs exact edition | Teams need stable families, while conformance depends on exact claim-bearing viewpoint editions. |
| Small core vs subject breadth | Four viewpoints should remain learnable without pretending that safety, mission, data, deployment, and every domain concern are the same four things. |
| Holon-centered view vs concern objects | A view can concern one holon while its claims designate methods, transformations, role assignments, capabilities, and structures through exact relations. |
| Familiar engineering language vs kind precision | `functional view` should remain readable without turning `functional`, `view`, or a diagram label into an intrinsic kind by spelling. |
| Direct authoring vs generated descriptions | Both can yield conforming views; neither route establishes conformance by itself. |
| Cross-view comparison vs invented links | Comparable views need exact direct relations, not a universal correspondence record or matching diagram positions. |
| Viewpoint reuse vs publication reuse | The same viewpoint can govern unpublished epistemes and many publication forms; packaging must not redefine membership. |

### E.17.2:4 - Solution

**Local mantra.** Select TEVB. Resolve one exact viewpoint episteme. Identify the holon-centered candidate episteme. Test E.17.0 conformance. Keep every mentioned engineering object and every publication object under its direct governor.

The mantra is a recall aid. The following sections specify the bundle, the four viewpoint witnesses, the conformance use, and the stopping rules.

#### E.17.2:4.1 - Fix the bundle without embedding viewpoint values

The core TEVB bundle is:

```text
TEVB.EngBundle : U.ViewpointBundle
  viewFamilyId = VF.TEVB.ENG
  EntityOfConcernClassSpec = U.Holon
  viewpointRefs = {
    ref(VP.Functional),
    ref(VP.Procedural),
    ref(VP.AllocationResponsibility),
    ref(VP.ModuleInterface)
  }
```

Each `VP.*` token is the `ViewpointId` designator of one exact viewpoint episteme edition P. Each bundle member is a `U.ViewpointRef`; resolving it under the effective reference scheme yields exact P. The designator, reference, viewpoint episteme, selected viewpoint-convention structure, and bundle membership remain distinct.

Bundle membership does not admit P as `U.Viewpoint`, does not make another episteme a `U.View`, and does not establish any publication. E.17.0 owns both dependent-kind membership rules; E.24.PUB owns publication.

The four-member set is fixed for this TEVB edition. Safety, assurance, information, mission, deployment, business, and publication-oriented viewpoints use another E.17.1 bundle or an explicit later TEVB edition. A recurring label alone does not extend this bundle.

#### E.17.2:4.2 - Recover each viewpoint through an exact convention witness

Every TEVB viewpoint is the same individual as one C.2.1 episteme P. Its exact EntityOfConcern is one selected viewpoint-convention structure S, not the holon later described by a conforming view.

For each of the four viewpoints:

1. identify exact convention epistemes under their least-powerful admitted kinds;
2. construct exact collection C under C.13;
3. recover every selected direct relation occurrence among those epistemes;
4. identify ordinary constraint episteme `Q_org` about C;
5. let a system perform A.22 structure-selection work using C, the exact relation occurrences, the applied constraints from `Q_org`, and the describing-use frame, yielding exact S;
6. identify ordinary episteme P with `EntityOfConcern(P)=S` and apply the five E.17.0 viewpoint-membership conditions;
7. only then use the corresponding `VP.*` designator and `U.ViewpointRef`.

No constituent, `Q_org`, or P becomes a `U.Signature` merely to fit this construction. A constituent is a `U.MethodDescription` only when it describes one independently admitted method under A.3.2. Exact selection work and its result remain separate from C, S, P, and the selected relation occurrences.

The concern epistemes have these exact subjects and governors:

| Viewpoint designator | Exact concern EntityOfConcern and direct governor |
|---|---|
| `VP.Functional` | exact `U.Transformation` under A.3.4; exact `U.Capability` under A.2.2; exact transformation-flow `U.Structure` under E.18 and A.22 |
| `VP.Procedural` | exact `U.Method` under A.3.1; exact transformation-flow `U.Structure` under E.18 and A.22; exact operational-state `U.Structure` under A.19.SPR and A.22 |
| `VP.AllocationResponsibility` | exact `U.RoleAssignment` under A.2.1; exact role-relation `U.Structure` under A.2.7 and A.22; exact `U.Capability` under A.2.2; exact `U.Transformation` under A.3.4 |
| `VP.ModuleInterface` | exact dependency `U.Structure` under B.1.1 and A.22; module, interface, boundary, substitutability, and change-policy claims remain governed by their direct patterns |

Keep the owner-specific claim boundaries explicit:

- **Functional:** functioning status, input/output boundary, and functional-port coverage remain claims in `E_rule.functionalCoverage` unless a separately identified EntityOfConcern and direct governor are current. The three concern epistemes stay separately about exact Transformation, exact Capability, and exact transformation-flow Structure; there is no universal function entity or one multi-subject concern episteme.
- **Procedural:** order, concurrency, failure, and recovery remain coverage claims unless another exact EntityOfConcern is independently identified. Method mention grants no MethodDescription membership, state wording is not a Structure, and procedural content is not performed work.
- **Allocation-responsibility:** holder, transformer, allocation, segregation, and responsibility remain typed constraint claims unless their exact direct occurrence or selected structure is independently recovered. A role value is not a RoleAssignment, allocation wording is not an obtaining relation, and selected structure performs no work.
- **Module-interface:** current `moduleIn(...)` remains a claim record. Whole-holon, candidate-module, boundary, interface, substitutability, and change-policy content stays in the coverage-rule episteme until a direct module-relation pattern admits exact participant kinds, predicate, obtaining, and occurrence identity. The claim record is not that relation and a module topic is not an EntityOfConcern.

Split any phrase spanning several exact subjects into separate concern epistemes, or retain it as one constraint claim over candidate content. Assign each stakeholder constituent exactly one governed referent disposition—exact system, role value, C.13 collection-as-whole, or context-local classification. Do not coerce heterogeneous constituents into Signatures merely to make the rows uniform.



The four witnesses are:

| Exact substrate | Applied constraints, selected structure, and viewpoint episteme | Selected direct dependencies | Method and work boundary |
|---|---|---|---|
| `C_functional = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.functionalTransformation, E_concern.capability, E_concern.transformationFlowStructure, E_rule.functionalCoverage, E_rule.functionalModuleSeparation, E_rule.functionalRetargeting}` | `Q_org.functional` is an ordinary constraint episteme about C. A.22 selects `S_functional`; `P_functional` has `EntityOfConcern=S_functional`, is designated `VP.Functional`, and passes E.17.0 viewpoint membership. | Each concern episteme depends on `E_target.tevbHolon`; `E_rule.functionalCoverage` depends on all three concern epistemes and `E_admitted.tevbEpisteme`; separation depends on functional-transformation concern; retargeting depends on the target. | No method constituent is required. A method convention enters only as exact `U.MethodDescription` after its method passes A.3.1. |
| `C_procedural = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.method, E_concern.transformationFlowStructure, E_concern.operationalStateStructure, E_rule.proceduralCoverage, E_rule.proceduralMethodBoundary, E_rule.proceduralNoWorkInference}` | `Q_org.procedural` is about C. A.22 selects `S_procedural`; `P_procedural` has `EntityOfConcern=S_procedural`, is designated `VP.Procedural`, and passes E.17.0 viewpoint membership. | Each concern episteme depends on the target; coverage depends on all concerns and admitted-episteme kind; method boundary depends on method concern; no-work-inference depends on method and transformation-flow concerns. | Operational methods remain subjects of separate method-description epistemes. Concern selection, view construction, evaluation, and use do not form one method or workflow by mention. |
| `C_allocation = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.roleAssignment, E_concern.roleRelationStructure, E_concern.capability, E_concern.transformation, E_rule.allocationCoverage, E_rule.allocationNoWorkInference, E_rule.allocationRetargeting}` | `Q_org.allocation` is about C. A.22 selects `S_allocation`; `P_allocation` has `EntityOfConcern=S_allocation`, is designated `VP.AllocationResponsibility`, and passes E.17.0 viewpoint membership. | Each concern episteme depends on the target; coverage depends on all four concerns and admitted-episteme kind; no-work-inference depends on role-assignment, role-structure, and transformation concerns; retargeting depends on the target. | Raw role values and raw methods are not collection members. Allocation or analysis method enters only through an exact method-description episteme. The selected structure performs no work. |
| `C_module = {E_target.tevbHolon, E_admitted.tevbEpisteme, E_concern.dependencyStructure, E_rule.moduleCoverage, E_rule.interfaceTyping, E_rule.functionalModuleSeparation, E_rule.substitutabilityChange, E_rule.moduleRetargeting}` | `Q_org.module` is about C. A.22 selects `S_module`; `P_module` has `EntityOfConcern=S_module`, is designated `VP.ModuleInterface`, and passes E.17.0 viewpoint membership. | Dependency-structure concern depends on the target; coverage depends on target, dependency structure, and admitted-episteme kind; typing, functional separation, and substitutability/change depend on dependency structure; retargeting depends on target and dependency structure. | No method, work, or module relation enters by mention. A direct module or interface relation joins only after its own pattern supplies participants, obtaining law, and occurrence identity. |

Each witness remains independently recoverable. Exact constituent editions identify C; every selected dependency occurrence passes the E.17.0 predicate; optional `D_dependencyUse` states obtaining and named-use admissibility as separate claims; and A.22 selects S from exact C, selected occurrences, applied Q constraints, and the use frame. Exact P is then identified by its claim content, S EntityOfConcern, and effective scheme. Changing only the Q edition leaves S unchanged when those selection inputs remain semantically unchanged. No topic list, citation, displayed edge, hidden O, D, or neighboring witness supplies another witness's closure.

The dependency relation in this table is exact `ViewpointConventionDependencyRelation` from E.17.0. It obtains only when interpreting or replaying the fixed claims of the dependent episteme relies on an exact criterion, law, public name, or method claim of the base episteme, and replacing the base edition can change that interpretation or replay. Co-membership, citation, or a visible arrow is insufficient.



When an A.22 selection judgment needs an explicit claim that one obtaining dependency occurrence is admissible for that use, identify the separate decision-use episteme described by E.17.0. Do not insert that decision, its evidence, or its evaluation result into the dependency relation or S identity.

#### E.17.2:4.3 - Keep the four concern conventions distinct

**Functional.** A conforming candidate episteme foregrounds exact transformations, capabilities, effects, functional elements, or transformation-flow relations of its holon. It does not identify a module structure by functional vocabulary and does not mint `U.Function`. Responsibility claims route to exact role and allocation governors.

**Procedural.** A conforming candidate episteme foregrounds exact methods, order, state, concurrency, failure, and recovery related to its holon. A procedural view about a holon is not a `U.MethodDescription`; that dependent kind requires one admitted method as the episteme's exact EntityOfConcern.

**Allocation-responsibility.** A conforming candidate episteme foregrounds exact systems, role values, role assignments, capabilities, transformations, and selected responsibility structures related to its holon. A role label does not prove an assignment, and a responsibility-oriented view does not itself assign a role or perform work.

**Module-interface.** A conforming candidate episteme foregrounds exact constituent holons, dependency structures, boundaries, interfaces, compatibility, substitutability, and change policy. It remains distinct from the functional viewpoint: many modules may support one transformation, one module may support several transformations, and either description may be incomplete without becoming the other.

The following are practitioner recognition and claim-shape cues, not embedded `StakeholderFamilies` or `AllowedEpistemeKinds` fields. A reader label creates no role assignment and enters neither viewpoint nor view identity; every example still needs its exact EntityOfConcern, direct governor, and E.17.0 conformance basis.

| Viewpoint | Typical readers or concern holders | Distinctive claim-shape and conformance cues |
|---|---|---|
| `VP.Functional` | System-engineering and architecture readers, product or capability owners, and reliability or performance readers inspecting capability envelopes | Look for service-capability and promise content, delivery or access and API descriptions, input/output signatures, and functional-port boundaries only as separately governed claims about the holon. Ground bounded behavior in exact transformations, capabilities, or a selected transformation-flow structure; keep service delivery Work, access relations, publications, and module interfaces separate, and do not mint `U.Function`. |
| `VP.Procedural` | Operations and run-time owners, control and automation engineers, and safety readers | Look for operational methods and procedures, control logic, workflow or orchestration logic, ordering, state, concurrency, failure, and recovery. Where step boundaries are current, make preconditions and postconditions explicit and type-checked; trace failure and recovery claims to their exact safety-analysis basis. Keep the method, method description, work plan, dated Work, calendars, and selected state or flow structures distinct. |
| `VP.AllocationResponsibility` | Organization and operations designers, safety or compliance readers concerned with segregation of duties, and device or system engineers | Look for exact holder and role-assignment claims, segregation and escalation constraints, responsibility structures, transformer or device loci, and capability allocation to physical, organizational, or software systems. A role value is not an assignment, allocation wording is not an obtaining relation, and no view or selected structure performs the allocated Work. |
| `VP.ModuleInterface` | Hardware or software architects, integration and test engineers, and lifecycle or maintenance readers concerned with replaceable units | Look for module decomposition, protocols, schemas, physical connectors, APIs, interface and conformance expectations, version and change policies, dependency and allowed-coupling structures, replaceability and variation points, and explicit functional-to-module correspondence or allocation without identity by default. Ports or connector diagrams do not establish module/interface relations; each direct relation and any functional-to-module retargeting keeps its own governor. |

#### E.17.2:4.4 - Recognize holon-centered TEVB views by conformance

TEVB keeps two subjects explicit:

| Episteme | Exact EntityOfConcern | Job |
|---|---|---|
| viewpoint episteme P | selected viewpoint-convention structure S | states the target-kind criterion, concerns, admitted episteme kinds, semantic-form, coverage, consistency, completeness, omission, and describing-use rules |
| candidate or view episteme E | one exact holon H admitted by P's target criterion | states claims about H and designates other engineering objects only through exact governed relations |

`EpistemeViewpointConformanceRelation(E,P)` must pass the fixed E.17.0 predicate. Only then is the same episteme E a `U.View`. Direct authoring, query execution, A.6.3 construction, a `VP.*` label, bundle membership, or publication does not establish that membership.

For one current describing use, its exact use qualification carries one singular `viewpointRef : U.ViewpointRef` resolving P under the effective reference scheme. Any `ViewpointId` is only P's designator. The use qualification, designator, reference, and P remain distinct; selection identifies neither E nor H, establishes no conformance, and adds no conformance participant or episteme-identity field.

Recover exact H only as `EntityOfConcern(E)` from E's C.2.1 constitution. Do not import a legacy context tuple, generic bounded-context object, or model-use identity field into E, P, S, conformance, or selection. Another use may select another P while E remains unchanged; several selected viewpoints require an exact governed collection rather than one overloaded reference.
If a user needs a view whose exact subject is a method, role assignment, transformation, or structure rather than H, identify another candidate episteme with that EntityOfConcern and use a viewpoint whose target-kind criterion admits it. Do not silently retarget a holon-centered TEVB view.

#### E.17.2:4.5 - Import, subset, and extend without semantic drift

An E.17.0 multi-view use first selects one exact `U.ViewpointBundleLibrary` edition and its exact TEVB bundle edition, whose `ViewFamilyId` is `VF.TEVB.ENG`, and then names the exact imported `U.ViewpointRef` members or subset from that edition. `VF.TEVB.ENG` is only the family designator: it neither identifies the selected editions by itself nor serves as a member reference. Each imported reference resolves exact viewpoint episteme P, while P's `VP.*` token is only its `ViewpointId` designator. A local subset names the retained references, preserves the exact source-edition provenance, and records whether each omission is merely unused coverage or an intentional local exclusion.

If local work changes only reader-facing aliases or adds examples, keep those as naming or annex content. If it changes a viewpoint's target criterion, concerns, admitted episteme kinds, conformance rules, or bundle membership, identify a new viewpoint or bundle edition. Do not keep the old designator while changing the exact P that it is supposed to designate under the same effective reference scheme.

Several bundles may be used together, but each member retains its bundle provenance and exact resolved viewpoint edition. Similar labels do not merge members.

A consumer that claims TEVB alignment for engineering families named `Functional`, `Procedural`, `Allocation-Responsibility (Device-Structure)`, and `Module-Interface` binds them respectively to `VP.Functional`, `VP.Procedural`, `VP.AllocationResponsibility`, and `VP.ModuleInterface`. A different mapping is another governed bundle or edition and must not silently reuse `VF.TEVB.ENG`.

#### E.17.2:4.6 - Keep cross-view relations and publication separate

TEVB provides four reusable viewpoint references; it does not assert correspondence among any resulting views. When work depends on a relation between a functional claim and a module claim, or between a procedural claim and a role-assignment claim:

1. identify the exact participating entities or epistemes;
2. state the exact realization, allocation, dependency, consistency, trace, or other direct relation claimed;
3. use its direct governing pattern and obtaining law;
4. use A.6.RCD when no existing direct or derived relation is sufficient;
5. use C.29 only for a representation of the recovered relation.

E.17 and E.24.PUB may publish a selected TEVB view edition through three separately governed relations: `PublicationFormExpressionRelation(selectedEdition,publicationForm,boundedUseDeclaration)`, `PublicationFormBearingRelation(presentationCarrier,publicationForm)`, and the five-participant `EpistemePublicationRelation(selectedEdition,audienceDeclaration,boundedUseDeclaration,publicationForm,presentationCarrier)`. Each retains its own participant set and maximal continuous obtaining interval; changing a participant or restoring availability after a gap yields another occurrence without reidentifying unchanged E or P.

Rendering, printing, upload, or carrier manipulation is separate system-performed `U.Work`. C.29 is used only when a representation corresponds to independently recovered objects or relations. A publication-side viewpoint, when current, is another exact viewpoint episteme selected by reference—not a TEVB `VP.*` token reused as a form or file name. View episteme, viewpoint episteme, construction, conformance, form, carrier, publication, rendering, and representation remain distinct; none of publication or representation makes a world-side subject relation obtain.

### E.17.2:5 - Worked cases

#### E.17.2:5.1 - Four views of a processing plant

Exact plant `Plant_X : U.System` is the EntityOfConcern of four separately identified epistemes.

- E1 states transformations, capabilities, material-flow effects, and functional boundaries. `ref(VP.Functional)` resolves P1; E1 conforms to P1 and is a functional `U.View`.
- E2 states exact operating methods, states, order, failure, and recovery claims related to the plant. It conforms to P2 designated `VP.Procedural`; it is not a method description because its EntityOfConcern is the plant.
- E3 states exact role assignments, operator systems, automation systems, capabilities, and responsibility structures. It conforms to P3 designated `VP.AllocationResponsibility`; neither E3 nor P3 performs work or assigns a role.
- E4 states constituent equipment holons, dependency structure, pipes, interfaces, substitutability, and change policy. It conforms to P4 designated `VP.ModuleInterface`; the diagram rendering E4 is published in remains separate.

The four conformance occurrences make E1-E4 views. Their shared holon and common bundle do not establish any cross-view realization or consistency relation. Those claims are tested separately.

#### E.17.2:5.2 - Query output missing a required concern

A query constructs episteme Y from plant model X, and A.6.3 records that construction. Y is labelled `functional view`, but it omits the output-condition coverage required by exact P1. Construction obtains; conformance does not. Y is not a `U.View` under P1 until another episteme edition with repaired claim content passes the predicate.

#### E.17.2:5.3 - Responsibility diagram and actual assignment

A responsibility diagram episteme E concerns exact system H. Exact `r_allocation = ref(VP.AllocationResponsibility) : U.ViewpointRef` resolves exact viewpoint episteme P designated by the `VP.AllocationResponsibility` token; `EpistemeViewpointConformanceRelation(E,P)` obtains. One box names `MaintainerRole@Plant`. This mention does not establish that system S holds the role. Exact `U.RoleAssignment` occurrence RA must be recovered under A.2.1; E can then assert or describe RA without becoming RA.

#### E.17.2:5.4 - One view, two publications

Module-interface view E is published as an interactive model and as a printed inspection sheet. Both publication occurrences select the same episteme edition. Their forms and carriers differ; E, its conformance occurrence, and its `U.View` membership do not.

#### E.17.2:5.5 - DDD Context Mapping method and product

A team enacts DDD Context Mapping. The way of doing is one independently admitted `U.Method` under A.3.1; an episteme that substantively describes that method may separately be a `U.MethodDescription` with the method as its exact EntityOfConcern. Neither is a TEVB viewpoint or view by its label.

First determine whether the product is a claim-bearing episteme or only a diagram, form, or carrier. A claim-bearing product called a Context Map is separately identified under C.2.1 as candidate episteme E with its own exact claim content, EntityOfConcern, and effective scheme. It becomes a `U.View` only if one exact viewpoint P admits E's subject and `EpistemeViewpointConformanceRelation(E,P)` obtains. Method enactment, product naming, diagram form, bundle position, publication, and visual resemblance grant no membership. If the map represents independently recovered domain regions or relations, C.29 governs that correspondence; a mere carrier remains with E.24.PUB, and the drawing creates no world-side relation.

### E.17.2:6 - Consequences


| Gain | Cost or boundary |
|---|---|
| Four familiar engineering concern families become reusable across holons and domains. | A new viewpoint edition needs an inspectable convention witness rather than a label alone. |
| Viewpoint episteme, selected structure, view episteme, and described holon remain distinct. | Authors must recover two different EntityOfConcern values: S for P and H for E. |
| Directly authored and generated descriptions use one conformance rule. | Query or rendering provenance cannot substitute for conformance. |
| Cross-view engineering claims keep their direct semantics. | A package or diagram cannot provide realization, allocation, or consistency by appearance. |
| Publication can evolve independently of the engineering viewpoints. | Publication forms and carriers need their own direct relations when they affect work. |

Reopen TEVB when the four-member bundle no longer gives a non-dominated engineering concern family for holons, when a viewpoint's exact target criterion or conformance rules change, or when a candidate concern cannot be expressed without changing the viewpoint witness. Add another bundle instead when the concern is orthogonal rather than a replacement for the four.

### E.17.2:7 - Rationale and SoTA-Echoing

The core-four choice is inspectable rather than conventional. Treat the SoTA-harvested candidate families—functional, behavioural, procedural, structural/module, allocation/responsibility, information/data, assurance/safety, mission/context, deployment/operational, and business/usage—as alternatives in the N/U/C/D quality space of Novelty, Use-Value, Constraint-Fit, and Diversity_P. Pareto/NQD comparison for engineering holons retains the `F-B-S+R` cut implemented by `VP.Functional`, `VP.Procedural`, `VP.ModuleInterface`, and `VP.AllocationResponsibility` as the minimal non-dominated core: it spans function, behaviour or procedure, structure, and explicit responsibility/allocation while remaining small enough for routine reuse.

Information/data, assurance/safety, mission/context, deployment/operational, and business/usage concerns are not rejected or silently absorbed. They remain orthogonal bundle candidates, quality bundles, or governance-oriented bundles unless a later exact TEVB edition reopens the comparison. A recurring label, an E.18 overlay, or one local omission does not extend `VF.TEVB.ENG`.

| Practice line | Adopted move | Rejected overread | Practical effect |
|---|---|---|---|
| Architecture-description viewpoint practice, including ISO 42010 as established vocabulary lineage | Keep concern-bearing viewpoint, view, described entity, correspondence, and publication distinct. | The standard vocabulary does not provide FPF identity, obtaining, construction, or conformance laws. | Engineers can use familiar view language without importing a lifecycle or documentation method. |
| Function-Behaviour-Structure design traditions | Preserve functional, procedural or behavioral, and module-interface concerns as different readings of one holon. | FBS labels do not identify exact transformations, methods, structures, or relations by themselves. | Functional and structural descriptions can be compared without collapse. |
| MBSE and views-as-queries practice | Allow queries and projections as construction routes for candidate view epistemes. | Generated output is not a view until E.17.0 conformance obtains. | Tool-generated and directly authored epistemes share one test. |
| Responsibility and allocation views in engineering practice | Keep allocation and responsibility concerns visible beside function, behavior, and structure. | A responsibility view is not a role assignment, organizational actor, or proof of performed work. | Teams can inspect who or what is claimed to bear work while retaining exact A.2/A.15 governors. |
| FPF constructive relation architecture | Build each viewpoint from exact convention epistemes, direct relation occurrences, applied constraints, selected structure, and exact P. | A topic list, graph, method label, or signature forest is not the viewpoint. | Viewpoint editions remain replayable while ordinary reuse needs only one resolved reference. |

### E.17.2:8 - Ownership and boundaries

- **E.17.2** owns the four TEVB viewpoint witnesses, their bundle membership, and their engineering concern content.
- **E.17.0** owns `U.Viewpoint` and `U.View` membership, both direct relations used by the witness and conformance architecture, and ordinary-use stopping rules.
- **E.17.1** owns library and bundle packaging by references.
- **C.2.1** owns identity of every constituent episteme, Q, P, candidate E, assertion, and description.
- **C.13 and A.22** own exact collection construction and structure selection.
- **A.6.3** owns optional source-to-receiving viewing construction, never view membership.
- **A.3.1/A.3.2, A.3.4, A.2.1/A.2.2/A.2.7, E.18, B.1.1, and module/interface patterns** retain the exact subjects and direct relations mentioned by each viewpoint.
- **E.24.PUB and C.29** own publication and representation objects.
- **A.6.RCD** owns construction or admission of a needed relation when current direct governors are insufficient.

### E.17.2:9 - Conformance checklist

1. The exact TEVB edition contains exactly four `U.ViewpointRef` members, not embedded viewpoint values, views, documents, forms, carriers, or publication occurrences.
2. Each `VP.*` token is only P's `ViewpointId` designator; the reference resolves exact P, while designator, reference, P, S, and bundle position remain distinct.
3. Each P has one exact selected convention structure S as EntityOfConcern and passes all five E.17.0 viewpoint-membership conditions.
4. Each witness names the exact least-powerful constituent editions, every selected obtaining dependency occurrence, ordinary Q_org, exact A.22-selected S, and ordinary P; optional D and evaluation remain named-use neighbors.
5. Each concern episteme has one independently recoverable EntityOfConcern and direct governor; a multi-subject phrase is split or retained as a constraint claim, never promoted to a hidden group kind.
6. Candidate E has one exact holon H as EntityOfConcern and becomes `U.View` only through obtaining `EpistemeViewpointConformanceRelation(E,P)`.
7. A singular describing-use reference selects P without entering E/P identity or conformance; A.6.3 construction, bundle membership, naming, evaluation, rendering, and publication grant no membership.
8. Procedural views are not MethodDescriptions by topic; allocation-responsibility views are not RoleAssignments or actors; module-interface views are not direct module relations or functional views by shared labels.
9. DDD Context Mapping remains a `U.Method`; a product called Context Map is a separately identified episteme and becomes a View only through exact E/P conformance.
10. Every cross-view relation has an exact governor, obtaining test, and participant meanings; a diagram edge, correspondence label, citation, or shared holon is insufficient.
11. Form expression, carrier bearing, five-participant publication and recurrence, rendering work, C.29 representation, and any publication-side viewpoint remain distinct and make no world-side subject relation obtain.
12. Ordinary reuse stops after resolving P and making the readable conformance judgment unless a named receiving work needs more structure.

### E.17.2:End

