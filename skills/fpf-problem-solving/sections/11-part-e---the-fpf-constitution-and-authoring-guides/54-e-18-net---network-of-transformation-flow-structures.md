## E.18.NET - Network of Transformation-Flow Structures

> **Tech-name:** **TransformationFlowStructureNetwork**
> **Plain-name:** Network of transformation-flow structures
> **Type:** Structural pattern for ontic relations (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### E.18.NET:1 - Problem frame — intent and first useful result

Use this pattern when one engineering question depends on two or more independently identified transformation-flow structures, or on nested networks of them, and at least one exact relation connects positions across their boundaries. Typical situations include a toolchain that builds another tool, a production system related to the product it helps produce, or an operating flow whose observation returns to a separate development flow.

Start with the practical choice, not with a graph:

1. decide whether the case is several valuations of one flow structure, an internal portion of one flow structure, or a network of independent flow structures;
2. identify each candidate member independently;
3. name the exact obtaining relation occurrences that connect positions in different members;
4. select only the members, relations, boundary exposures, and constraints needed for the current question; and
5. return one exact network reference, or stop at the proposed description and name either the exact relation-claim result returned by its governing pattern or the separate missing network discriminator.

The first useful result is therefore small. It is either:

```text
selectedNetworkRef: one exact TransformationFlowStructureNetwork
directMemberRefs[]: at least two refs to independently identified TransformationFlowStructure or E.18.NET-conforming TransformationFlowStructureNetwork values
selectedCrossFlowRelationOccurrenceRefs[]: exact selected obtaining cross-flow relation occurrences
selectedNetworkConstraintRefs[]: exact applied endpoint, boundary-exposure, and acyclic direct-member constraints
networkUseFrame:
  questionOrAction: the concrete question answered or action enabled
  forbiddenOverread: what this selection does not establish
returnCondition: the first member, relation, constraint, or use-frame change that reopens selection
```

or an exact stop such as:

```text
proposedNetworkDescriptionRef: current diagram or record
blockedClaim: "the compiler-building flow produces the compiler-use flow input"
exactRelationClaimResultRefOrOutcome: exact result returned by the pattern that governs this claim
```

When the relation claim has a positive obtaining result but a network endpoint is not bound, keep that positive result and state a separate E.18.NET selection blocker:

```text
obtainingRelationOccurrenceRef: exact positive occurrence returned by its governing pattern
networkSelectionBlocker:
  missingEndpointOrPositionBinding: exact participant, member, position, or binding that is absent
```

An unavailable fact yields the governing pattern's `missing-information` outcome; a sufficient case basis that fails its positive test yields `factually unsupported`. Neither outcome alone asserts a negative. Carry an inapplicable or negative result only when that pattern's applicable rule and case basis establish it. A missing member, applied constraint, or `networkUseFrame` remains its own network-selection blocker and never becomes a relation result. Keep `proposedNetworkDescriptionRef` until all four A.22 discriminators—members, selected obtaining relation occurrences, applied constraints, and use frame—are recoverable; only then assert `selectedNetworkRef`.

Do not use E.18.NET merely because one flow branches, contains a detailed portion, has several valuations, or is drawn as a network. Use E.18 for one selected `TransformationFlowStructure`, its valuations and internal `U.Transfer` relations; use E.18's `SubflowRef` for one parent-relative internal portion. Use E.18.2 when the current object is a graph, wiring diagram, tuple, category-theory expression, or another mathematical description. Use A.22.CGUS and E.18.3 when the current object is an admitted demonstrative traversal rather than the network itself.

### E.18.NET:2 - Problem

Teams routinely connect flows that concern different objects, Work occurrences, architecture boundaries, valuation state, and change cadence. A development flow produces or changes a tool; another flow uses the tool; another evaluates the use; feedback returns to development. A manufacturing system is changed through one flow while products are made through another. A compiler is built by one toolchain and then participates in a later build.

A single picture can hide three different ontic answers:

| Working situation | What is actually selected | What to do |
| --- | --- | --- |
| Several valuations, paths, or slices share one exact TFS identity | one `TransformationFlowStructure` | stay in E.18; do not mint another structure |
| A detailed portion resolves through positions and internal `U.Transfer` occurrences of one exact parent TFS | one parent-relative `SubflowRef` | stay in E.18; return through the parent's boundary positions |
| Independently identified TFS or nested-network values are connected by exact obtaining relations across their boundaries | one `TransformationFlowStructureNetwork` | apply this pattern |

When the third case is treated as one giant TFS, local state appears global, an internal `U.Transfer` is asked to mean production, use, evaluation, feedback, correspondence, and dependency, and a change in one member appears to reidentify everything. When the first or second case is over-split into a network, the model invents members and relations that the engineering situation does not need.

### E.18.NET:3 - Forces

| Force | Tension to hold |
| --- | --- |
| Local autonomy vs one engineering question | Members keep their identity and state while a selected structure makes their exact coordination inspectable. |
| Recursive reuse vs fixed levels | A member may itself be a network, but membership paths must remain finite and acyclic. |
| Plain diagrams vs exact relations | A readable edge helps recognition, but only an obtaining relation of an admitted kind contributes to identity. |
| Boundary exposure vs flattening | A parent can use a nested boundary position without copying the nested member's internal structure. |
| Useful local state vs false global state | Valuation, path slice, and `DesignRunTag` remain local to one leaf TFS position binding. |
| Stable selection vs evolving members | Reidentify only when an A.22 discriminator changes; records, renderings, and selection Work remain separate. |

### E.18.NET:4 - Solution

#### E.18.NET:4.1 - Select a dependent non-agentive structure

`TransformationFlowStructureNetwork@Context` is a dependent, non-agentive specialization of `U.Structure` defined by E.18.NET and selected through the A.22 identity law. It is not a root U-kind, acting system, holon, workflow, graph, record, publication, `FlowValuation`, WorkPlan, or performed Work. The `@Context` suffix qualifies retrieval and use; it adds no identity discriminator.

For `N : TransformationFlowStructureNetwork`, recover exactly:

```text
StructureIdentity(N) = <
  directMemberRefs[],
  selectedCrossFlowRelationOccurrenceRefs[],
  selectedNetworkConstraintRefs[],
  networkUseFrame
>
```

The four field names have the same meanings as in the first-use result: exact direct members, exact selected obtaining cross-flow occurrence refs, exact applied network constraints, and one concrete use frame. `returnCondition` is not a fifth identity discriminator; it records when the current use must return and reselect.

The direct-member set contains at least two exact values. Each member is one independently identified `TransformationFlowStructure` or one independently identified E.18.NET-conforming `TransformationFlowStructureNetwork`. At least one selected relation occurrence binds positions in different direct members or in different leaf TFS members reached through them. The use frame says what the practitioner will decide or do with this selected organization and names the forbidden overread. “Current use”, “appropriate network”, and the title of a diagram are not use frames.

A row in a record does not create a member or make membership obtain. This profile needs no generic `networkMemberOf` relation. If a future receiver needs a separately re-identifiable world-side membership occurrence, reopen that relation question under A.6.RCD; do not infer it from the member list.

#### E.18.NET:4.2 - Reidentification and change locality

Replacing a direct member, selected relation occurrence, applied endpoint or exposure constraint, acyclicity constraint, or named selection-use frame identifies another selected network. Reidentifying a nested member reopens every parent network that selects that exact member.

Changing only a name, reference designator, record edition, graph layout, mathematical description, publication, selecting system, selection Work, evidence item, `FlowValuation`, `PathSliceId`, or local `DesignRunTag` leaves the network unchanged when the four A.22 discriminators still resolve to the same values.

#### E.18.NET:4.3 - Recurse through finite member paths

The selected direct-member nesting is acyclic. No direct or transitive member path from a network resolves back to that network, and every member path used by a reference is finite. This permits build-the-builder and supply-network recursion without inventing level-1, level-2, or level-3 network kinds.

Cycles among selected cross-flow relation occurrences remain possible when their applicable predicates and constraints permit them. Feedback from operation or evaluation to development is therefore compatible with acyclic membership: the cycle is among those relation occurrences, not in network containment.

`E.18` defines the complete `FlowPositionRef` identity. Import that tuple unchanged; E.18.NET defines only the `ExposedFlowPositionRef` extension needed for a boundary position reached through one finite member path:

```text
FlowPositionRef := <
  transformationFlowStructureRef,
  localFlowPositionId
>

ExposedFlowPositionRef := <
  networkStructureRef,
  memberPath[],
  leafFlowPositionRef
>
```

Every hop in `memberPath[]` resolves through the preceding network's direct members. Its final member is the TFS named by `leafFlowPositionRef`. When the path crosses a nested network, the leaf position must be one of the boundary positions that nested network exposes for the current higher-level use. Two different paths to the same leaf TFS position are two different exposures.

The parent network may compose the finite path and use the exposed boundary. It may not copy or silently flatten the nested member's internal structure. `FlowValuation`, `PathSliceId`, actual fillings, and `DesignRunTag` qualify use of a position; they are not part of `FlowPositionRef` or `ExposedFlowPositionRef` identity.

#### E.18.NET:4.4 - Keep valuation and design/run state leaf-local

Each `positionBindingRef` cites an E.18 position/valuation binding or a declaration-local binding whose pattern defines the needed participant meanings, value kind, and reference mode. A network introduces no universal cross-flow value kind.

`DesignRunTag` belongs to one exact position binding inside one exact leaf TFS. A network has no network-level `FlowValuation`, global design/run ladder, or automatic crossing that changes the carried entity's kind. If the same episteme fills local positions in different members—for example one position concerned with design work and another with production, verification, or later operation—record each leaf-local binding and the exact relation that obtains between them. Those ordinary member descriptions create no fixed TFS taxonomy or lifecycle phase.

#### E.18.NET:4.5 - Preserve the direct cross-flow relations

For every relation used by the network, recover:

- the exact obtaining occurrence;
- the exact relation kind;
- the pattern that defines or tests its predicate, applicability, and occurrence-identity rule;
- the complete signature and participant order;
- the endpoint member and position binding for every participant; and
- direction only when the direct relation has direction.

An n-ary relation remains n-ary. Do not decompose it into invented binary arrows. A row, edge label, shared entity, temporal adjacency, operation result, plan row, or graph connection never makes the relation obtain.

`U.Transfer` remains E.18's internal relation kind for one TFS. It is not a universal relation between network members. For any production, use, participation, evaluation, correspondence, feedback, dependency, supply, or other cross-flow relation, the relation kind must already be admitted. Use its applicable relation pattern to recover the participant meanings, predicate, applicability, and occurrence-identity rule; current case facts or constituting history must satisfy the predicate affirmatively. Only then does one world-side occurrence obtain. Use A.6.REL only when a named use must distinguish that occurrence from another. For ordinary network selection, the PatternID and exact relation occurrence are enough; add `relationFunctionClaimRef` to the defining or constraining `ClaimGraph` only when comparison, migration, or reliance depends on that exact rule identity. The network selects only the exact already-obtaining occurrence ref.

If no admitted relation kind and applicable predicate cover the intended participants and use, carry `missing-governor` from the pattern governing the relation claim. If required case facts are unavailable, carry its `missing-information` result; if the available basis is sufficient to apply the positive test but that test fails, carry `factually unsupported`. Neither result by itself establishes a negative. Carry an inapplicable or negative result only when the governing pattern defines that outcome and its current basis establishes it. Only a positive obtaining occurrence may fill `selectedCrossFlowRelationOccurrenceRefs[]`.

After a positive occurrence is established, test the E.18.NET endpoint and position bindings separately. A missing binding blocks network selection but does not change the relation result. Missing members, applied constraints, and use-frame values are likewise separate network-selection blockers. A row, graph edge, or episteme neither admits a relation kind nor creates an occurrence. In none of these branches substitute `creates`, `produces`, `uses`, `input`, `output`, `result`, `handoff`, or `transfer` as a generic edge.

#### E.18.NET:4.6 - Record the network without replacing it

When the selected answer must survive beyond the immediate work, describe it with a separate C.2.1 episteme:

```text
TransformationFlowStructureNetworkRecord@Context <: U.Episteme:
  entityOfConcernRef: one exact TransformationFlowStructureNetwork ref
  entityOfConcernKindRef: TransformationFlowStructureNetwork
  claimScope?: U.ClaimScope
  effectiveReferenceScheme: U.ReferenceScheme
  directMemberRows[]:
    memberRef: TransformationFlowStructureRef | TransformationFlowStructureNetworkRef
  exposedFlowPositionRows[]:
    exposedFlowPositionRef: ExposedFlowPositionRef
    memberPath[]
    leafTransformationFlowStructureRef
    leafFlowPositionRef
  crossFlowRelationRows[]:
    exactRelationOccurrenceRef: U.RelationRef
    exactRelationKindRef: U.KindRef
    subjectPatternLocator: U.EntityRef, locating the pattern that defines or tests this relation
    relationFunctionClaimRef?: U.EntityRef, referencing the exact defining or constraining ClaimGraph when the recorded use depends on that rule identity
    endpointRows[]:
      relationParticipantPositionRef
      memberRef
      flowPositionRef: FlowPositionRef | ExposedFlowPositionRef
      positionBindingRef
  architectureCorrespondenceRowRefs[]?: C.32.CONWAY episteme refs
  selectedNetworkConstraintRefs[]
  networkUseFrame
  preservedNetworkStructure
  lostOrHiddenNetworkStructure
  returnCondition
```

The record describes the network; it is not the network. Its member and relation rows cite objects that already exist and occurrences that already obtain. An architecture-correspondence row is a qualified reading only. It contributes no member or selected cross-flow relation unless an exact separately grounded relation occurrence and endpoint bindings also satisfy the network identity.

E.18.NET defines this composite locator for one nested cross-flow row:

```text
NetworkCrossFlowRelationRowRef := <
  transformationFlowStructureNetworkRecordRef: U.EpistemeRef, referencing one exact current TransformationFlowStructureNetworkRecord@Context edition,
  exactRelationOccurrenceRef: U.RelationRef,
  orderedEndpointBindingIdentity[]: <
    relationParticipantPositionRef,
    memberRef,
    flowPositionRef: FlowPositionRef | ExposedFlowPositionRef,
    positionBindingRef
  >
>
```

Resolve the record ref first, then match `crossFlowRelationRows[]` by the exact occurrence ref and the complete ordered endpoint-binding identity. Exactly one row must match. Zero matches or several matches leave the locator unresolved and stop that consumer; never fall back to the containing record, the occurrence alone, or a prose pointer. `NetworkCrossFlowRelationRowRef` is a reference shape, not a U-kind, episteme, or relation occurrence. Its `U.EpistemeRef` targets the containing record, never the nested row.

#### E.18.NET:4.7 - Keep descriptions, demonstrations, architecture, and Work outside identity

Use E.18.2 for a graph, hypergraph, network expression, wiring diagram, category-theory object, tuple, fold, or other mathematical description of the selected network. State what that description preserves and loses. A rendered graph or publication face remains under E.17 and C.29 as applicable.

Use A.22.CGUS and E.18.3 for an admitted network-aware `DemonstrativeUnfoldingSlice@Context`. Its finite paths must map to already admitted included positions, its cross-flow relations must cite admitted exact relation-reference epistemes, and its tags remain in leaf-local bindings. The slice demonstrates one traversal; it is neither the network nor an actual trajectory, WorkPlan, or Work occurrence.

Use C.30.TFS-REL when architecture uses the selected network. Name one exact containing holon whose `ArchitectureOf@Context` selects the network, or explicitly state the inter-holon use and its participating architecture claims without inventing a bearer. Use C.32.CONWAY only for its one-pair architecture-influence reading; the pair neither acts nor becomes the network.

Only admitted Systems perform Work. Selecting a network, writing its record, or drawing its graph may be Work when A.15.1 independently admits the occurrence after each precise performer has an A.13 core; none is performance by the network, and no Work claim is needed merely to select or discuss the network. When selection Work is material, cite those already established A.13 and A.15.1 results. Cite F.6 only when the current network account also needs precise assignment-bound attribution, and leave its proof with F.6. Keep the Method, performer, dated Work, result episteme, selection or decision relation, and any C.11 choice result separate. A result episteme is not a decision or accountability relation by form; state accountability, duty, responsibility, or authority only through the exact direct relation that obtains.

### E.18.NET:5 - Archetypal Grounding — worked cases

#### E.18.NET:5.1 - Same surface vocabulary, different ontic answers

**Several valuations of one TFS.** A cooling-loop review compares nominal-load and emergency-load valuations of the same exact cooling-loop `TransformationFlowStructure`. Both valuations use the same structure positions and internal `U.Transfer` occurrences. The load value, path slice, and local tags differ; the TFS identity does not. E.18.NET is not used.

**Internal coffee subflow.** A coffee-brewing TFS exposes a preparation portion containing grinding, dosing, and wetting positions plus their parent-internal `U.Transfer` occurrences. Its entry and exit remain positions of the brewing TFS. The practitioner uses E.18's `SubflowRef`; no second TFS or network is created.

**Independent network.** A roastery-production TFS and a café-brewing TFS concern different objects and have separate Work occurrences, valuation boundaries, and architecture change cadence. The applicable supply pattern defines its predicate and applicability, and the current delivery-and-acceptance facts satisfy that predicate for a dispatch position in the first and an accepted-stock position in the second. For ordinary first use, fill the selected network directly:

```text
selectedNetworkRef: RoasteryCafeSupplyNetwork@CoffeeService
directMemberRefs[]:
  - RoasteryProductionTFS@Dispatch
  - CafeBrewingTFS@AcceptedStock
selectedCrossFlowRelationOccurrenceRefs[]:
  - SupplyOccurrence@Lot24Dispatch-to-CafeAcceptance
selectedNetworkConstraintRefs[]:
  - SupplyEndpointConstraint@Dispatch-to-AcceptedStock
  - SelectedExposureConstraint@RoasteryDispatch-and-CafeAcceptedStock
  - AcyclicDirectMemberConstraint@RoasteryCafe
networkUseFrame:
  questionOrAction: decide which accepted stock can enter the coffee-service brewing flow
  forbiddenOverread: shared coffee does not make both members one TFS or make supply a generic edge
returnCondition: either member, the supply occurrence, an endpoint or exposure, acyclicity, or the coffee-service question changes
```

This filled basis is enough for the immediate selection; it is not a `TransformationFlowStructureNetworkRecord@Context`. Create that separate descriptive record only when the result must survive the current work. If the supply claim has no admitted relation kind or applicable predicate, carry the governing pattern's `missing-governor` result. If required facts are unavailable, carry `missing-information`; if a sufficient case basis fails the positive test, carry `factually unsupported`. Neither result asserts a negative. Only an applicable negative rule and satisfying case basis can supply a negative result. When the supply occurrence obtains but an endpoint binding is missing, keep the positive occurrence and name the missing binding as a separate E.18.NET selection blocker. A missing member, applied constraint, or coffee-service use frame is also a separate selection blocker.

#### E.18.NET:5.2 - Project system-of-interest and recursive build-the-builder

For one project question, practitioners ask which independently identified flow structures must be considered together to connect production and later operation of the project system-of-interest, and which builder branches must also be visible. The actual project remains composite `U.Work`; the selected network is a non-agentive `U.Structure`. Project designation and `U.System` identity remain separate from any local system-role kind, classification, assignment, selection Work, or result episteme. None follows from a project or network label.

For the compiler-and-application use, identify five TFS values by the questions they answer:

1. `CompilerEditionPreparationTFS`, whose loci bind compiler-edition preparation and the obtaining source-use occurrences needed by the build;
2. `BootstrapCompilerBuildTFS`, whose loci bind Work on pre-existing build substrates and the separately grounded production and identity-inception claims for one bootstrap compiler;
3. `ApplicationBuildTFS`, whose loci bind application-production Work and the exact use of that admitted compiler;
4. `ReleaseAssuranceTFS`, selected for release-assurance questions; and
5. `DeploymentOperationTFS`, selected for deployment and operation after the application system exists.

These names designate independently identified TFS values, not lifecycle kinds. They assert no transformation of a not-yet-existing compiler or application. Use E.18 for each TFS, A.15.1 for any current Work occurrence, A.3.4 for a change of a continuing referent, A.15.PROD for production or identity inception, and the applicable relation pattern for each exact cross-member occurrence.

Select the nested network values from those already established inputs:

| Selected network | Direct members | Exact selected cross-member occurrence and ordered endpoint binding | Network use frame |
|---|---|---|---|
| `CompilerRealizationNetwork` | `CompilerEditionPreparationTFS`; `BootstrapCompilerBuildTFS` | `CompilerEditionSourceUsedByBootstrapBuild-1`: `CompilerSourceEditionReady` -> `BootstrapCompilerBuildInput` | connect the admitted source edition to the bootstrap-compiler build question |
| `ApplicationCompilerUseNetwork` | `CompilerRealizationNetwork`; `ApplicationBuildTFS` | `BootstrapCompilerUsedByApplicationBuild-1`: exposed `ExecutableCompilerResult` -> `ApplicationCompilerUsePosition` | connect the admitted compiler to the application-build question |
| `ReleaseAssuranceNetwork` | `ApplicationCompilerUseNetwork`; `ReleaseAssuranceTFS` | `ApplicationBuildEvaluatedForRelease-1`: exposed `ApplicationBuildResult` -> `ReleaseEvaluationSubject` | connect the application result to the release-assurance question |
| `DeliveryOperationNetwork` | `ReleaseAssuranceNetwork`; `DeploymentOperationTFS` | `ReleasedApplicationUsedByDeployment-1`: exposed `ReleasedApplicationPosition` -> `DeploymentApplicationInput` | connect the released application to the deployment-and-operation question |

Each named occurrence is independently established under its project predicate before selection. Each network applies its exact endpoint-binding and boundary-exposure constraints plus the acyclic direct-member constraint, and each keeps the use frame in its row. The local names select or add nothing by themselves.

No claim about who selected these networks is required. If the case also needs `CompilerNetworkSelectionWork-5`, cite each precise performer's independently established A.13 core and the Work's independent A.15.1 admission. Add F.6 only if the case also needs exact assignment-bound attribution; its assignment declaration and proof remain outside E.18.NET. Adding or removing the Work or attribution claim changes none of the four network identities above. The result episteme may describe the selected structures and cite a separate selection or decision relation, but it is not a decision or accountability relation by form. Any accountability claim needs its own exact predicate and participants.

A compiler-production case can close on separately grounded identity inception, production completion or readiness, evidence, and decision while naming the application-build position as the downstream use outside that closed case. Project-level reasoning continues into the member where the compiler later participates. The same joint-selection question recurs for a builder system: select the TFS in which that admitted builder performs exact Work together with the independently identified TFS or nested network concerning production and identity inception of the builder, or its later change after it exists. Shared identity creates no edge; use obtaining production, inception, participation, application, use, or other relation occurrences and their endpoint bindings.

The bootstrap compiler result is exposed from the outer network through one finite member path:

```text
ExposedFlowPositionRef:
  networkStructureRef: DeliveryOperationNetwork
  memberPath[]:
    - ReleaseAssuranceNetwork
    - ApplicationCompilerUseNetwork
    - CompilerRealizationNetwork
    - BootstrapCompilerBuildTFS
  leafFlowPositionRef:
    transformationFlowStructureRef: BootstrapCompilerBuildTFS
    localFlowPositionId: ExecutableCompilerResult
```

Each path entry is a direct member of the preceding network, the final entry is the TFS named by `leafFlowPositionRef`, and no network repeats. `FlowValuation`, path slices, and `DesignRunTag` remain leaf-local. “Builds”, “uses”, “evaluates”, and “delivers” are ordinary cues until each link resolves to an admitted relation kind, complete participant signature, obtaining occurrence, and endpoint bindings.

Before these identities and relations are grounded, A.1.STM may show the dependency only as a Plain provisional long-mantra map and must name the missing member, the exact relation-claim result returned by its governing pattern, or the separate missing occurrence, endpoint, or position binding. It is not yet an E.18.NET selection. Once the network is admitted, a separate A.22.CGUS demonstrative slice may traverse admitted positions and relation-reference epistemes; it remains a demonstration, not the project, network, case, or Work order.

#### E.18.NET:5.3 - N-ary relation and feedback cycle

A manufacturing release relation has three participants defined by one admitted domain relation pattern: one product-definition position in a TFS selected to answer the development question, one equipment-readiness position in a TFS selected to follow the changes that establish equipment readiness, and one release-condition position in a TFS selected for assurance. Its network row keeps the three participants and their order. It is not replaced by three unlabeled arrows.

Later, an exact use-observation relation connects a position in a TFS selected for operation or use back to a position in a TFS selected to answer the development question. The relation occurrences form a feedback cycle, while the selected direct-member nesting remains acyclic. The feedback does not make the operation-or-use TFS a member of itself and does not turn observation into development Work.

#### E.18.NET:5.4 - Architecture and two demonstrative boundaries

For one containing holon, a current `ArchitectureOf@Context` claim may select the network among its structures. If the selected members belong to separately named holons and no containing bearer is grounded, record the use as inter-holon and name the participating architecture claims. Do not invent one system merely to fill the architecture field.

A Plain A.1.STM long-mantra map may display proposed members and a missing cross-member link before network admission. It names the intended final result and the absent member, relation kind or predicate, predicate result, occurrence, or endpoint binding; it asserts neither an E.18.NET structure nor a CGUS.

After the network is admitted, a separate teaching mantra may show one finite admitted dependency slice. The slice uses the network locator family, cites admitted positions and exact relation-reference epistemes, and keeps omissions and return visible. It does not prescribe project Work order, make the path the whole network, or turn a leaf-local `DesignRunTag` into a project phase.

### E.18.NET:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for uses of this pattern.

| Bias risk | Mitigation in this pattern |
| --- | --- |
| **Gov:** demanding a fully reusable relation occurrence can hide the cheaper local decision. | The first result permits a proposed description and one exact result from the pattern governing the relation claim, or one separate missing-discriminator blocker; it invents no common status kind or generic relation. |
| **Arch:** a network-shaped case can tempt the reader to invent one containing holon. | C.30.TFS-REL keeps named-containing-holon and explicit inter-holon uses separate. |
| **Onto/Epist:** a graph, record, or demonstrative slice can be mistaken for the selected network. | The four A.22 identity discriminators precede every description, record, rendering, architecture reading, and demonstration. |
| **Prag:** exact member, relation, endpoint, and constraint apparatus can crowd out first use. | The practitioner first produces one small network result or one exact stop; the durable record remains optional. |
| **Did:** the coffee and build-the-builder cases can be over-read as a closed domain ontology or a universal edge vocabulary. | The cases demonstrate boundary choices only; each cross-flow relation still needs an admitted kind, its applicable predicate, and exact participants. |

### E.18.NET:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-E18-NET-01 Three-way discriminator** | The case is explicitly distinguished from several valuations of one exact TFS and from one E.18 `SubflowRef`. | Return to member identity and relation basis; do not decide from diagram shape, team labels, or stage names. |
| **CC-E18-NET-02 A.22 identity** | Exact direct members, selected obtaining cross-flow occurrences, applied constraints, and one concrete selection-use frame are recoverable. | Recover the missing discriminator or stop at a proposed description. |
| **CC-E18-NET-03 Independent members** | Every member keeps its own TFS or independently identified E.18.NET-conforming network identity, transformations, Work, valuations, boundaries, and local state. | Split any merged object; reidentify each member under E.18 or E.18.NET and restore its own Work, valuation, boundary, and state. |
| **CC-E18-NET-04 Finite acyclic membership** | Every member path is finite and no member path returns to the same network. | Repair the selected member set or return the cyclic-membership blocker; do not add level kinds. |
| **CC-E18-NET-05 Exposed position** | Every `ExposedFlowPositionRef` resolves hop by hop to an exposed leaf TFS position. | Recover the missing member hop or boundary exposure; do not flatten the nested network. |
| **CC-E18-NET-06 Leaf-local state** | Every valuation, path slice, and `DesignRunTag` remains attached to one exact leaf-TFS binding. | Remove the network-global state field and restore the local bindings. |
| **CC-E18-NET-07 Direct relations** | Every selected cross-flow relation has an admitted kind, applicable predicate, exact positive obtaining occurrence, complete participant order, and grounded endpoint bindings. The governing pattern's relation result remains distinct from E.18.NET selection blockers. | Carry that pattern's exact `missing-governor`, `missing-information`, `factually unsupported`, or positive result; carry an inapplicable or negative result only when that pattern defines it and the case basis establishes it. After a positive result, name a missing endpoint binding separately; do not rewrite it as a relation failure. |
| **CC-E18-NET-08 N-ary preservation** | Participant count, order, kinds, positions, and direction match the direct relation. | Restore the direct signature and remove invented binary decompositions. |
| **CC-E18-NET-09 Record and row-locator separation** | Member rows and relation rows describe already identified objects and occurrences; the record does not create them, and every `NetworkCrossFlowRelationRowRef` resolves exactly one nested row by record, occurrence, and ordered endpoint-binding identity. | Separate the C.2.1 episteme from the selected `U.Structure`; repair or remove any locator that resolves zero or several rows. |
| **CC-E18-NET-10 Non-agentivity** | The network, record, graph, pattern, architecture reading, and demonstrative slice do not act, build, select, decide, warrant, or perform Work. Network identity needs no actor or selection-Work claim. | Describe the network through direct members, selected obtaining occurrences, endpoint bindings, applied constraints, and its use frame. If actual selection Work is current, cite every precise performer's A.13 core and the independent A.15.1 Work admission; cite F.6 only when exact assignment-bound attribution is also current. Keep result episteme, choice, decision, and accountability relations separate. |
| **CC-E18-NET-11 Representation boundary** | Mathematical descriptions, graphs, views, publications, and demonstrations are identified separately and state preserved/lost structure when relied on. | Apply E.18.2, C.29, E.17, A.22.CGUS, or E.18.3 as appropriate. |
| **CC-E18-NET-12 Useful result or stop** | The practitioner receives one exact network ref and return condition, or a proposed description with one exact reason selection cannot close: the governing pattern's relation-claim result, or a separate absent member, applied constraint, use frame, endpoint, or position binding. | Restore the exact result or blocker at its own layer; do not end with a local status taxonomy or make a network-selection blocker change the relation result. |

### E.18.NET:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| One giant flow | Development, use, evaluation, and refresh are called valuations solely because they are coupled. | Test shared TFS identity; when independent members and a direct relation are needed, select a network. |
| Detail becomes a member | A zoomed diagram, team boundary, or named stage becomes another TFS. | Use E.18 `SubflowRef` while every position and internal transfer still resolves in one parent. |
| Universal cross-flow edge | `creates`, `produces`, `uses`, `input`, `result`, `handoff`, or `transfer` labels stand in for several relations. | Apply the pattern that defines or tests the exact relation and carry its result. Only after a positive occurrence, test endpoint bindings and other network discriminators separately. |
| Record makes the world | Filling `memberRows` or drawing edges is treated as establishing members and relations. | Ground members and relation occurrences first; keep the record descriptive. |
| Recursive flattening | A parent copies all nested positions and state into one global graph. | Keep finite member paths and expose only the boundary positions needed by the parent use. |
| Global design/run ladder | One `DesignRunTag` is assigned to the network. | Restore one tag per exact leaf position binding. |
| Network as actor or workflow | The network builds, evaluates, repairs, schedules, or authorizes. | Name the acting system and its Work, or the exact decision, gate, or assurance claim and result; keep the network non-agentive. |
| Pretty graph as network | A connected diagram is accepted without exact members, relations, constraints, and use frame. | Keep it as an E.18.2 or provisional description until all four A.22 discriminators are recoverable. |

### E.18.NET:9 - Consequences

| Gain | Cost or trade-off |
| --- | --- |
| Independent flows can be coordinated without losing their identity or local change boundary. | Members and cross-flow relations must be grounded before the network can be claimed. |
| Recursive networks scale without numbered levels. | Exposed positions require finite path resolution and explicit boundary selection. |
| Cross-flow relations keep their participant meanings and n-ary signatures. | A missing relation kind or predicate remains visible instead of being hidden by a convenient generic edge. |
| Local valuations and tags remain usable without becoming global state. | A network record carries more explicit member and endpoint references than a simple graph. |
| Graphs and mantras remain useful descriptions. | Their distinct claims use E.18.2 or E.17 for descriptions and publications, A.22.CGUS or E.18.3 for demonstrations, C.30.TFS-REL for architecture use, A.15 for Work, and E.18.NET for the selected network. |

Adoption test: use E.18.NET only when the current question needs independently identified members and at least one exact relation across their boundaries. If one TFS or one parent-relative `SubflowRef` answers the question, the added network, endpoint, and member-path apparatus buys nothing and stays absent.

### E.18.NET:10 - Rationale and naming

The selected head preserves the established `TransformationFlowStructure` name, says that the members are structures rather than valuations, and supports recursion without fixed levels. The shorter cue “transformation-flow network” is retrieval wording only after the governed value is clear.

Mint vs reuse: E.18.NET mints the durable names `TransformationFlowStructureNetwork`, `TransformationFlowStructureNetworkRecord@Context`, `ExposedFlowPositionRef`, and `NetworkCrossFlowRelationRowRef` for the governed value family, separate description episteme, and two reference shapes defined here. It reuses `U.Structure`, `U.Episteme`, `TransformationFlowStructure`, `FlowPositionRef`, relation kinds, and relation occurrences without changing their meanings; labels, records, and references create none of those values.

```text
NameCard:
  NameCardId: NC-TRANSFORMATION-FLOW-STRUCTURE-NETWORK
  GovernedValueRef: TransformationFlowStructureNetwork@Context <: U.Structure
  SubjectPatternLocator: E.18.NET
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: recursive selected organization over independently identified TransformationFlowStructure or TransformationFlowStructureNetwork values and exact cross-flow relation occurrences, with member boundaries and locally exposed positions preserved
  TechLabel: TransformationFlowStructureNetwork
  PlainLabel: network of transformation-flow structures
  CandidateSet: TransformationFlowStructureNetwork; TransformationFlowNetwork; CrossFlowRelationStructure; TransformationFlowDependencyStructure; CoupledTransformationFlowStructure; FlowOfFlows; CreatorGraph; CreationStructure
  RejectedCandidates: TransformationFlowNetwork can mean one network-shaped TFS; CrossFlowRelationStructure hides the transformation-flow use; TransformationFlowDependencyStructure narrows to one projection; CoupledTransformationFlowStructure suggests one merged TFS; FlowOfFlows conflicts with FlowValuation; CreatorGraph confuses the ontic structure with a graph and narrows change to creation; CreationStructure excludes operation, repair, modification, and reuse
  SelectionRationale: preserve the established TransformationFlowStructure head, make structures rather than valuations the members, and permit recursive membership without numbered levels
  LineageEntries: flow-of-flows and creator-graph examples remain retrieval lineage for the stress cases; fixed two-level and one-giant-flow ontic readings are retired
  RefreshCondition: reopen if repeated use cannot distinguish one TFS with several valuations, one subflow, and a recursive network of independently identified TFS values
```

### E.18.NET:11 - SoTA-Echoing

Each line below is inherited only while the cited current pattern version retains both the named body decision and the named source-use row for its declared use. E.18.NET relies on the currentness decision recorded with that source-use row; it does not independently turn the cited literature or tool practice into current authority. When one cited source-use row changes, reopen only the affected line here.

For the working reader, these lines support the boundary already exercised in the worked cases in sections 5.1–5.4: select a network only from independently identified members and exact relations, keep positions and state local to their leaf TFS, treat graphs as descriptions, and let a demonstrative path cite only already admitted positions and relation references.

| Current pattern version and exact source-use locus | E.18.NET disposition | Concrete mutation in E.18.NET | Qualification and smallest reopen |
| --- | --- | --- | --- |
| `A.22:4.1` and the `A.22:11` row “FPF `C.2.1`, `A.6.3`, and `E.17` description and view discipline” | **Adopt** the four selected-structure discriminators and the separation of structure from its description, view, record, selecting system, and selection Work. | Network identity is the exact `directMemberRefs[]`, selected obtaining `selectedCrossFlowRelationOccurrenceRefs[]`, exact `selectedNetworkConstraintRefs[]`, and one `networkUseFrame`; the descriptive record and selection activity remain separate and non-agentive. | Applies while A.22 keeps those four discriminator meanings and that description/view boundary. Reopen this line if A.22 changes a discriminator or allows a description, view, record, or selection activity to identify or authorize the structure. |
| `E.18:5.1` through `E.18:5.3` and the `E.18:12` rows `Applied category theory and compositional open systems`, `Operads, wiring diagrams, and hypergraph categories`, and `Open-graph and string-diagram rewriting` | **Adapt** one-TFS typed positions, valuation locality, exact internal `U.Transfer`, interface exposure, and replay-local rewrite discipline to recursively selected members. | A network keeps leaf-TFS position and valuation identity, resolves each exposed position through a finite member path, and leaves `U.Transfer` inside the TFS that contains it; cross-flow relations remain obtaining world-side occurrences under their applicable predicates. | Applies while E.18 keeps those position, valuation, `U.Transfer`, crossing, and replay-locality decisions. Reopen this line if E.18 changes any of them or its named source-use rows no longer support typed interfaces and localized rewrites. |
| `E.18.2:4.1` through `E.18.2:4.3` and the `E.18.2:9` rows `Model-based systems and architecture-description practice` and `Applied category theory, wiring diagrams, and graph rewriting` | **Adopt** the subject/description/lens separation and **adapt** the permitted expressions to member paths, n-ary relation views, quotients, and folds. | A mathematical description may expose or compare network structure only after naming its network subject, declared use, preserved structure, lost structure, and stop; it neither creates nor reidentifies the network or its relation occurrences. | Applies while E.18.2 keeps the five-way discriminator and the named rows' preserved/lost-structure and C.29 lens-use boundary. Reopen this line if the selected subject branch, preserved/lost account, mapping mode, or C.29 return condition changes. |
| `A.22.CGUS:4.4` and its `A.22.CGUS:11` rows on OCPQ, JuliaHub Dyad 3.2 with Modelica 3.7 as historical lineage, and ModelingToolkit/FMI; plus `E.18.3:4.2a`, `E.18.3:4.4`, and its `E.18.3:11` OCPQ and ModelingToolkit/FMI rows | **Adapt** typed object-and-relation structure, Dyad's current separation of reusable component models from separately selected analyses, and post-admission demonstration discipline to a network locator. | A network-aware demonstration consumes already admitted positions and exact relation-reference epistemes, keeps member-local state, branches, omissions, and return visible, and never turns the displayed path into the network, model, analysis, WorkPlan, or performed Work. | Applies while A.22.CGUS keeps Dyad as its current engineering comparator and Modelica only as historical lineage, and while CGUS and E.18.3 keep post-admission slices and exact locator admission. Reopen this line if those object-relation, model-analysis, admission, or locator decisions change. |

The F.18 NameCard entries `flow-of-flows` and `creator-graph` remain naming and stress-example lineage only; they authorize no current ontology or practice claim. A new need for cyclic member identity, a separately re-identifiable membership occurrence, or cross-flow semantics that cannot preserve the direct relation and its endpoints reopens the E.18.NET architecture decision itself, not the source-currentness status of every row above.

### E.18.NET:12 - Relations

Builds on: `A.22` for selected-structure identity and non-agentivity; `E.18` for one TFS, internal `U.Transfer`, `FlowPositionRef`, valuations, paths, slices, and local state; `A.6.REL`, `A.6.RCD`, and `A.6.P.WMR` for exact relation recovery and `missing-governor`; `C.2.1` for the optional descriptive record; and `F.18` for the stable local name.

Coordinates with: `A.15.6` for actual project Work, project system-of-interest designation, and subject- or claim-centred case closure; `A.1.STM` for a Plain provisional long-mantra display and backward/forward attention use; `E.18.2` and `C.29` for mathematical descriptions; `A.22.CGUS` and `E.18.3` for admitted demonstrative slices; `C.30.TFS-REL` for architecture use; `C.32.CONWAY` for one qualified architecture-influence pair; `A.3.4`, `A.12`, and the A.15 family for actual transformation, causal or acting positions, Work, production, and work-to-change claims; `E.17` for publication; `E.11` for public entry and recognition; and `E.11.PUA` for using one already selected pattern to reach its first useful result.

Does not replace: the direct pattern that defines or constrains any selected production, use, participation, evaluation, feedback, dependency, correspondence, supply, evidence, assurance, gate, decision, causal, or work relation. E.18.NET selects already obtaining occurrences for one network use; it does not mint their kinds or make them obtain.

### E.18.NET:End

