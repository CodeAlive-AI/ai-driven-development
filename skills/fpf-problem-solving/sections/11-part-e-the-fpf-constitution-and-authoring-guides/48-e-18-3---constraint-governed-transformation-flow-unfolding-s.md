## E.18.3 - Constraint-Governed Transformation-Flow Unfolding Structure

> **Type:** E.18 transformation-flow specialization of `A.22.CGUS`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### E.18.3:0 - Use This When

Use this pattern when a team is planning, reviewing, or explaining a transformation and a route-like flow card is useful, but branches, joins, guards, or connections to separately governed positions determine what can follow. The practical need is to recover those transformation-flow relations without treating displayed order as performed-work order, evidence, decision, or authorization.

The admitted object is a `U.Structure` whose substrate is transformation-flow structure over bounded `U.Transformation` values, typed flow positions, exact flow relations, and explicit connections to positions governed by neighboring patterns.

Do not use this pattern merely because a visible record or description is a route, path, graph, process map, chain, loop, or swimlane. First ask whether typed transformation positions, exact crossings and guards, a flow valuation when current, preserved transformation structures, C.33 adequacy notes, and direct governing-pattern connections are recoverable.

The first useful move is small: name the transformed entity and kind, then name two candidate transformation positions and the exact relation or guard that may change which continuation is admissible. If that relation is not recoverable, keep the visible artifact as a `ProvisionalUnfoldingDemonstrationDescription@Context` and use the broader `A.22.CGUS` admission question.

### E.18.3:1 - Problem Frame

`E.18` already gives FPF a rich language for transformation-flow structure: transfers, dependencies, paths, crossings, guards, valuations, publication faces, comparability, slice-local refresh, and structure-positioned slot fillings. `A.22.CGUS` gives the broader A.22 specialization of `U.Structure` for constraint-governed unfolding structures. A practitioner needs the narrow bridge between them: when is an unfolding structure a transformation-flow unfolding structure, and which neighboring claims remain under their direct patterns?

### E.18.3:2 - Problem

Transformation-flow artifacts are easy to overread. A path diagram becomes a workflow. A flow card becomes performed work. A P2W chain becomes work authorization. A graph expression becomes the whole structure. A gate, evidence path, architecture decision, or publication face becomes part of the transformation-flow ontology by visual adjacency.

The repair cannot be lexical. E.18.3 admission depends on naming the transformed entity and kind, typed flow positions, exact relation values and signatures, independent structural-function and subject-use classifiers, connections to positions governed elsewhere, preserved structures, C.33 adequacy notes, and separate stop and return boundaries.

### E.18.3:3 - Forces

| Force | Tension |
| --- | --- |
| Transformation-flow richness vs universal-parent drift | E.18 is rich enough to explain many route-shaped transformation cases, but narrative, abduction, grounding, improvement, and public practical-use cards or walkthroughs are not transformation-flow merely by shape. |
| Flow card usefulness vs work-order overread | A path or flow card can guide a next FPF use, but it does not authorize performed work or decide launch readiness. |
| Neighboring positions vs ontology absorption | Method, work, evidence, gate, decision, architecture, publication, and currentness positions can connect to a flow position without becoming transformation-flow kinds. |
| Demonstrative slices vs actual traces | A path slice may show a traversal for learning or review; actual project history may branch, pause, retry, or skip that traversal. |

### E.18.3:4 - Solution

Select `ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure` as the E.18 transformation-flow specialization of `ConstraintGovernedUnfoldingStructure@Context`.

```text
ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  boundedContextRef: U.BoundedContextRef
  transformedEntityRef: U.EntityRef
  transformedEntityKindRef: U.KindRef
  transformationPositionRefs[]: U.EntityRef, each referencing one ConstraintGovernedUnfoldingPosition@Context
  governingPatternPositionRelationRefs[]: U.EntityRef, each referencing one TransformationFlowGoverningPatternPositionRelation@Context
  transferRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=transfer
  dependencyRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=dependency
  pathIds[]: E.18 PathId
  pathSliceIds[]: E.18 PathSliceId
  demonstrativeSliceRefs[]: U.EpistemeRef, each referencing one DemonstrativeUnfoldingSlice@Context
  crossingRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=crossing
  guardRelationReferenceEpistemeRefs[]: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with structuralFunction=guard
  transformationFlowValuationRef?: U.EntityRef, referencing one E.18 TransformationFlowValuation
  methodWorkLinkageRef?: U.EntityRef, referencing one MethodWorkUnfoldingLinkage@Context
  evidenceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=evidence
  assuranceRelationReferenceEpistemeRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=assurance
  architectureUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=architecture
  narrativeUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=narrative
  publicationUseReferenceRefs[]?: U.EpistemeRef, each referencing one TransformationFlowRelationReference@Context with subjectUse=publication
  preservedTransformationStructureRefs[]: U.EntityRef, each referencing one U.Structure
  structureInformationAdequacyNoteRefs[]?: U.EpistemeRef, each referencing one StructuralInformationAdequacyNote@Context
  governingPatternReturnBoundaryRefs[]: U.EntityRef, each referencing one UnfoldingStructureUseBoundaryCondition@Context
  stopBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
```

`unfoldingStructureRef` names the generic `ConstraintGovernedUnfoldingStructure@Context` whose `specializedStructureRef` points to this narrower transformation-flow structure. The reciprocal references state the specialization relation; they do not split the primary EntityOfConcern or create a second transformation-flow structure.

The transformed entity and its kind are both present. A flow position points to one typed `ConstraintGovernedUnfoldingPosition@Context`; an external governed position is related through `TransformationFlowGoverningPatternPositionRelation@Context`, not put into a heterogeneous adjacency list.

Paths and demonstrations remain different. `pathIds[]` and `pathSliceIds[]` identify E.18 flow structure. `demonstrativeSliceRefs[]` identify post-admission A.22.CGUS epistemes whose EntityOfConcern is the already-admitted wider structure. A pre-admission flow card, worked example, or explanation remains a separate `ProvisionalUnfoldingDemonstrationDescription@Context` and does not fill `demonstrativeSliceRefs[]`. An admitted demonstrative slice can be linear while the current flow structure branches, joins, cycles, or keeps alternatives live.

A pattern-selection flow, selected-pattern-application flow, and downstream-subject-work flow keep different EntitiesOfConcern, changes, work occurrences, results, direct governing patterns, constraints, and returns. One flow's result may fill an input, tool, context, or constraint position in another flow without changing kind. E.18 relates those positions without turning the flows into one workflow. When a `DemonstrativeUnfoldingSlice@Context` asserts this cross-flow provenance, its `transformationFlowStructureRef`, `pathSliceId`, and `designRunTag` are all present; otherwise all three are absent. Those fields locate the demonstration in one flow valuation. They do not merge the demonstrated structures, rows, work occurrences, or result claims. A nested pattern-selection slice is present only when selection provenance is current; it returns a candidate, fit finding, or recommendation to the enclosing demonstrated-pattern-use row rather than borrowing that row's application result.


Preserved transformation structure is carried by exact `U.Structure` refs. Captured, expected-but-uncaptured, lost, and hidden structure for a declared use is carried by C.33 `StructuralInformationAdequacyNote@Context`. E.18.3 does not mint parallel free-text loss fields. Stop and governing-pattern return are different boundary relations. Source currentness and decay remain with G.11; E.18 slice-local flow refresh remains with E.18.

`methodWorkLinkageRef?` appears only when a named receiving use relies on an inspectable method-to-work relation. A method, method description, WorkPlan, work-entry readiness relation, or performed Work remains governed by its exact A.3 or A.15 pattern.

#### E.18.3:4.0 - Application sequence

1. Start from one admitted generic CGUS and name this narrower structure through the reciprocal specialization refs.
2. Name the transformed entity and kind, then the typed transformation positions that matter to the current use.
3. Reference the exact transfer, dependency, crossing, or guard relations. Add a subject-use classifier only when the same relation supports a separately governed evidence, assurance, architecture, narrative, or publication use.
4. Connect every neighboring governed position through its exact kind, ref, governing pattern, connection kind, rationale, and supporting relation when that connection kind needs one.
5. Name paths and path slices as transformation-flow structure; name demonstrative slices separately as presentation epistemes. Add the E.18 flow locator triple only when cross-flow demonstration provenance is current.
6. Name preserved transformation structures and use C.33 for omitted or hidden structure needed by the declared use.
7. Add a stop boundary and separate returns to the direct patterns governing stronger claims. If the transformation substrate, exact relation, or typed connection is absent, keep the artifact as a `ProvisionalUnfoldingDemonstrationDescription@Context`, route card, graph description, or broader A.22.CGUS admission question; do not fill `demonstrativeSliceRefs[]`.

#### E.18.3:4.0a - Exact relation references

`E.18.3` governs `TransformationFlowRelationReference@Context`, a reference-bearing episteme whose EntityOfConcern is one exact transformation-flow relation instance. The episteme records two independent classifications without becoming the referenced relation:

```text
TransformationFlowRelationReference@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the exact relation instance
  entityOfConcernKindRef: U.KindRef, referencing that relation kind
  boundedContextRef: U.BoundedContextRef
  claimGraph: U.ClaimGraph by value
  referenceSchemeRef: U.ReferenceSchemeRef
  editionId
  FlowStructureSlot = <FlowStructureSlot, ConstraintGovernedTransformationFlowUnfoldingStructure@Context, U.EntityRef>
  StructuralFunctionSlot? = <StructuralFunctionSlot, TransformationFlowStructuralFunctionValue, by-value>
  SubjectUseSlot? = <SubjectUseSlot, TransformationFlowSubjectUseValue, by-value>
  RelationSignatureSlot = <RelationSignatureSlot, U.Signature, U.EntityRef>
  DirectGoverningPatternSlot = <DirectGoverningPatternSlot, U.MethodDescription, U.EntityRef>
```

`TransformationFlowStructuralFunctionValue` is `transfer | dependency | crossing | guard`. It states what the referenced relation does inside the flow structure. `TransformationFlowSubjectUseValue` is `evidence | assurance | architecture | narrative | publication`. It states which separately governed subject use the same relation supports. At least one classifier is present; both may be present when both claims are true. Neither classifier changes the exact relation signature, value kind, value ref, or direct governing pattern.

For example, one crossing relation can also support evidence use. It remains one exact relation with `structuralFunction=crossing` and `subjectUse=evidence`; the two classifiers do not create two relations or let E.18.3 own the evidence claim.

#### E.18.3:4.1 - Connections to positions governed elsewhere

```text
TransformationFlowGoverningPatternPositionRelation@Context <: U.Relation:
  FlowStructureSlot = <FlowStructureSlot, ConstraintGovernedTransformationFlowUnfoldingStructure@Context, U.EntityRef>
  FlowPositionSlot = <FlowPositionSlot, ConstraintGovernedUnfoldingPosition@Context, U.EntityRef>
  NeighborGoverningPatternSlot = <NeighborGoverningPatternSlot, U.MethodDescription, U.EntityRef>
  NeighborPositionKindSlot = <NeighborPositionKindSlot, U.Kind, U.KindRef>
  NeighborPositionRefSlot = <NeighborPositionRefSlot, U.Entity, U.EntityRef>
  PositionConnectionKindSlot = <PositionConnectionKindSlot, TransformationFlowPositionConnectionKindValue, by-value>
  SupportingRelationReferenceSlot? = <SupportingRelationReferenceSlot, TransformationFlowRelationReference@Context, U.EpistemeRef>
  ConnectionRationaleSlot = <ConnectionRationaleSlot, U.Episteme, U.EpistemeRef>
  RelationRefKind = U.EntityRef
  Direction = FlowPositionSlot -> NeighborPositionRefSlot
  Dependence = bounded-context local to FlowStructureSlot and NeighborGoverningPatternSlot editions
  Identity = <FlowStructureSlot, FlowPositionSlot, NeighborGoverningPatternSlot, NeighborPositionRefSlot, PositionConnectionKindSlot>
```

`TransformationFlowPositionConnectionKindValue` is `basisDependency | producedResult | governingConstraint | returnTarget | comparisonPeer`. `basisDependency`, `producedResult`, `governingConstraint`, and `returnTarget` carry an exact supporting relation reference. `basisDependency` states a dependency on a basis position governed elsewhere; it creates no obligation. `comparisonPeer` permits the supporting reference to remain absent because this E.18.3 relation itself states the exact pairwise comparison connection and rationale. The neighbor ref is always paired with its exact kind.

This connection relation keeps the neighboring pattern visible without importing its result kind into transformation-flow ontology. Recommendation, method, work, evidence, assurance, gate, architecture, narrative, publication, and currentness claims remain under their direct governing patterns.

#### E.18.3:4.2 - Provisional flow demonstration and admitted slice

Before a `ConstraintGovernedTransformationFlowUnfoldingStructure@Context` passes admission, a path fragment, flow card, worked example, replay, or first-use explanation remains a `ProvisionalUnfoldingDemonstrationDescription@Context`. Its subject is the transformed entity, current flow question, or proposed continuation set. Candidate positions and relation descriptions may guide discovery, but they are not admitted transformation positions or relation instances.

After the generic CGUS and this transformation-flow specialization are admitted, a separate `DemonstrativeUnfoldingSlice@Context` may teach or demonstrate one admissible traversal. It names the admitted CGUS as EntityOfConcern and states included typed positions, C.33 notes for relevant omitted structure, loop-compression rule, presentation-ordering rule, alternatives, and return boundary when those affect use. It may cite the provisional description as derivation basis; it does not retype that description or the transformed entity.

Do not infer that demonstrated order is project work order. If work order is current, open the work-plan or method-description pattern. Do not infer that a demonstrated path is the whole transformation-flow topology. If the admitted flow has branches, joins, cycles, alternatives, or partial orders, name what the slice omits or compresses before relying on it for comparison, architecture, evidence, or work planning.

A pre-admission flow card can still help slot discovery. Each visible candidate position states the subject-domain object or question it concerns and the exact admission coordinate still unresolved. Once the transformed entity, typed positions, exact crossing or guard relations, valuation, preserved structures, C.33 notes, governing-pattern connections, and boundaries are recoverable, admit the structure first and create the slice second. This preserves the practical aid without circularly using a supposed slice as evidence for its own whole.

#### E.18.3:4.3 - Boundary

This `U.Structure` specialization is not a second transformation ontology, workflow, method, work plan, performed work, mathematical graph, publication, evidence relation, gate decision, architecture decision, or architecture description. It is a transformation-flow structure over typed transformation positions and exact relation references, together with explicit connections and returns to the patterns governing stronger claims.

#### E.18.3:4.4 - Replay and change localization

Replay one use from the reciprocal CGUS specialization refs, transformed entity and kind, typed transformation positions, exact relation signatures and values, structural-function and subject-use classifiers, governed-position connections, path and slice ids, optional valuation, preserved structures, C.33 adequacy notes, and stop and return boundaries. For each continuation, recover the exact relation or guard that admits it and the pattern governing any stronger claim.

Localize changes by the relation they affect. A changed relation value reopens its classifiers, dependent guards, and continuations. A changed neighbor value or kind reopens that governed-position connection and its supporting relation. A changed path or valuation reopens only the dependent path slices and demonstrations. Changed omitted structure reopens the C.33 note. Source edition, freshness, telemetry, and decay remain G.11 changes; E.18 owns only slice-local flow refresh. Reconstruct the wider specialization only when the transformed entity, transformation-position set, relation topology, preserved structure, or declared use boundary changes.

### E.18.3:5 - Worked Slices

**Minimal first use.** In the candidate-set repair situation, name `CandidateSetComparisonBasis@Review-2026-07` and its kind, then describe candidate `ReferenceEditionChangePosition`, `ComparisonRecalculationPosition`, and the proposed dependency `ComparisonDependsOnAdmittedEdition`. Keep the result as a `ProvisionalUnfoldingDemonstrationDescription@Context` with return descriptions pointing to G.11 and A.19. This already prevents a stale-edition comparison from looking current without asserting typed positions or a relation instance prematurely. Admit the full E.18.3 structure only when the exact dependency and every required admission coordinate are recoverable.

**P2W carry-through.** Accepted problem-side records may name distinctions, constraints, and unresolved relation positions that jointly guide later method selection, planning, work, interpretation, and return. `E.18.3` can relate those positions to candidate governing-pattern positions through exact connection kinds and supporting relations. It does not authorize launch or performed work, and it does not replace E.18.1 carry-through.

**Transformation-flow mini-example.** A team has a flow card "admitted reference-publication edition changes -> recalculate comparison -> update candidate set -> decide whether to repair." E.18.3 admits only the transformation-flow slice:

```text
transformedEntityRef: CandidateSetComparisonBasis@Review-2026-07
transformedEntityKindRef: U.Episteme
transformationPositionRefs[]: ReferenceEditionChangePosition; ComparisonRecalculationPosition; CandidateSetUpdatePosition; DecisionRepairPosition
governingPatternPositionRelationRefs[]: G2SourceUseBasisConnection; G11CurrentnessBasisConnection; A19ComparisonResultConnection; C18RetainedSetResultConnection; C32PADRepairReturnConnection
dependencyRelationReferenceEpistemeRefs[]: ComparisonDependsOnAdmittedEdition; CandidateSetUpdateDependsOnComparison
pathIds[]: CandidateSetRepairFlow
pathSliceIds[]: EditionChangeToDecisionRepairSlice
demonstrativeSliceRefs[]: DemonstrativeUnfoldingSlice@CandidateSetRepairTeaching
guardRelationReferenceEpistemeRefs[]: EditionAdmissionGuard; ComparisonBasisChangeGuard
preservedTransformationStructureRefs[]: EditionToComparisonDependencyStructure; ComparisonToCandidateSetDependencyStructure
structureInformationAdequacyNoteRefs[]: CandidateSetRepairTeachingOmissionNote under C.33, naming omitted comparison branches and return
governingPatternReturnBoundaryRefs[]: return to G.11 for currentness; A.19 for comparison; C.18 for retained-set stewardship; C.32.PAD for decision repair
stopBoundaryRef: stop stronger use when any named position or supporting relation is no longer recoverable
```

Before those typed positions, exact relation references, C.33 omission note, and returns are recoverable, the flow card remains a provisional demonstration description. The block above is admitted only after they are recoverable; its `demonstrativeSliceRefs[]` then names a separate post-admission slice.

**Local edition-relation repair.** `G.11` admits `ReferencePublicationEdition@v2`, while `ComparisonDependsOnAdmittedEdition` still references v1. Keep the transformed entity, flow positions, path ids, preserved structures, and all return boundaries. Replace the stale relation value ref, then re-evaluate `EditionAdmissionGuard`. Reopen the A.19 comparison position only if the admitted comparison basis changed; reopen the C.18 retained-set position only if the comparison result changed; reach C.32.PAD only if that retained-set change affects the current decision. The edition change therefore propagates through exact dependent relations instead of reopening the whole flow by proximity.

**Connected-box proxy failure.** A team reports that every flow-card box is connected and adds low-value edges until path coverage reaches its target. The relation count rises, but guards no longer distinguish admissible alternatives, stale dependencies remain unrepaired, and wrong governing-pattern returns increase. Edge count and path coverage describe the expression only; they do not establish current, useful transformation-flow structure. Remove edges without a declared structural function or subject use, evaluate whether practitioners select the correct guarded continuation and smallest repair, and use `E.13` when display coverage substitutes for those outcomes.

**Architecture P2S projection.** A P2S flow card includes architecture-relevant problem pressure, selected or unknown structures, synthesis positions, and actual-structure feedback relations. If one slice is transformation-flow structure, `E.18.3` names that slice and its exact connections. Architecture use remains with `C.32.P2S` and `C.30.TFS-REL`; an architecture decision remains with `C.32.PAD`.

**Physical workpiece transformation.** A heat-treatment structure concerns `GearBlank@Lot-14`, admitted as a project `U.Holon`, and relates load, soak, quench, and hardness-evaluation positions. `QuenchAdmittedAfterSoakRange` is an exact guard relation; furnace loading and quenching remain planned or performed work under A.15, and the hardness result remains under its evaluation and evidence patterns. A flow card can expose guarded alternatives before execution without claiming that the work occurred.

**Clinical transformation planning.** A treatment-adjustment structure concerns `Patient@Case-17`, admitted as a `U.System`, and relates assessment, intervention-candidate, contraindication-guard, observed-state, and return positions. The structure can show that one observed state changes which intervention remains admissible. It does not authorize treatment, establish evidence sufficiency, replace clinical judgement, or claim that an intervention occurred; those claims remain with their clinical DPF, work, evidence, and gate patterns.

**Formal flow-expression boundary.** A team expresses the candidate-set repair slice as a directed graph or DCR model to ask whether `DecisionRepairPosition` is reachable after `EditionAdmissionGuard`. The expression preserves selected dependency and guard topology plus the queried path. It loses subject-use authority, direct governing-pattern connections, C.33 omission notes, and currentness semantics unless those are separately mapped. Use `E.18.2` for the mathematical description and `C.29` for its admissibility and loss. A positive reachability result does not establish currentness, retained-set validity, decision repair, work order, or the identity of the whole E.18.3 structure.

**Reference-currentness repair.** A path slice can depend on an admitted publication edition, a `G.2` source-use relation, a source pack, or a telemetry window. E.18 governs slice-local flow refresh. `G.11` governs source currentness, decay, edition shift, deprecation, reship, and no-change claims. Connect those positions through exact E.18.3 relations without creating a combined currentness-refresh value.

### E.18.3:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Path-as-workflow | Restore the transformed entity and kind, typed flow positions, exact relation references, guards, crossings, preserved structures, C.33 adequacy notes, and direct work-pattern connection. |
| Graph-as-structure-in-every-sense | Keep graph expressions and path cards as provisional descriptions before admission or separate admitted slices afterward; neither presentation is the governed transformation-flow structure. |
| E.18 as universal CGUS parent | Admit E.18.3 only when bounded transformation-flow substrate is current. |
| Gate or evidence absorption | Keep gate and evidence claims with their direct governing patterns even when the same exact relation has a crossing or guard structural function. |

### E.18.3:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-E18.3-1 Transformation substrate.** | Bounded transformations, transformed entity and kind, and typed transformation positions are named. | Use `A.22.CGUS` or another direct pattern instead of E.18.3. |
| **CC-E18.3-2 Flow structure.** | Exact transfer, dependency, crossing, and guard relation refs; path and path-slice refs; demonstrations; and optional valuation are recoverable without union fields. | Lower to a route card, graph description, or ordinary explanation. |
| **CC-E18.3-3 Governing-position connections.** | Every neighboring position has exact kind, ref, governing pattern, connection kind, and rationale. Every connection except `comparisonPeer` has an exact supporting relation; for `comparisonPeer`, this connection relation itself states the exact pair and rationale. | Add the typed connection or remove the neighboring-position claim. |
| **CC-E18.3-4 Preserved and omitted structure.** | Preserved transformation structures are exact refs; relevant loss and hiddenness are C.33 adequacy notes for the declared use. | Add the exact structures and C.33 notes before relying on the slice. |
| **CC-E18.3-5 Stop and return.** | Stop boundary and returns to exact governing patterns are separate; E.18 slice-local refresh and G.11 currentness remain distinct. | Add exact boundaries or keep the slice as a one-use example. |
| **CC-E18.3-6 Non-chain topology.** | Branches, joins, cycles, partial orders, and guarded alternatives are preserved or explicitly lost when the flow is graph-shaped. | Keep a linear path provisional before admission; after admission, a separate demonstrative slice may present it but never replaces the whole flow structure. |

### E.18.3:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **P2W as launch permission** | A carry-through note is used to begin work. | Add method, work-plan, work-entry, or gate record under the direct pattern before work is authorized. |
| **Flow card as architecture decision** | A P2S flow card is treated as the decision or ADR. | Keep flow structure in E.18.3 or C.32.P2S; use `C.32.PAD` and `C.32.ADR` for decision and ADR projection. |
| **Evidence path as evidence** | A path through evidence-looking boxes is treated as sufficient evidence. | Open `A.10`, `B.3`, or `G.6`; name the evidence relation and admissible use. |
| **Loop as improvement** | A retry loop in the flow is called quality improvement. | Use `E.23` only when object version, evaluation frame, repair, and re-evaluation are current. |

### E.18.3:9 - Consequences

This narrower `U.Structure` specialization lets E.18 keep its strength without swallowing every route-shaped pattern. P2W, P2S, agent-loop, gate, evidence, architecture, and currentness-related cases can share exact transformation-flow relations while each subject claim remains governed by its direct pattern.

The cost is an explicit boundary. A flow-shaped structure is admitted as a governed transformation-flow unfolding structure only when it names typed transformation positions, exact relation refs, guards, crossings, preserved structures, C.33 adequacy notes, and direct governing-position connections. Before that admission, the visible episteme remains a provisional demonstration description; only afterward may a separate demonstrative slice present the admitted structure.

### E.18.3:10 - Rationale

The selected design follows the same principle as E.18: transformation-flow structure is structure, not the whole work process. Constraint-governed unfolding adds a next-use concern. It asks how a transformation-flow structure can unfold toward a next FPF use while protecting the differences among structure, description, method, plan, work, evidence, gate, decision, architecture, publication, E.18 slice-local refresh, and G.11 currentness.

### E.18.3:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| OMG, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Use as lineage for weakly structured case-work slices whose positions and relations are constrained without one fixed work order. | CMMN is not treated as current best-known process practice. E.18.3 does not import its notation or make a case-management method. |
| Esser and Fahland, "OCPQ: Object-Centric Process Querying & Constraints", arXiv:2506.11541, 2025 | Adopt the current object-centric pressure that typed objects and their relations jointly determine constraint queries. This reinforces multi-object flow positions, joins, many-to-many dependencies, and exact relation-preserving returns. | OCPQ governs event-data queries and constraint checking. E.18.3 does not import event-log, query-language, or process-mining ontology, and an OCPQ result does not become transformation-flow structure. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Use as declarative-process lineage for exact guards, crossings, and admissible path slices under several typed perspectives. | E.18.3 does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011; Bagheri Hariri et al., "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013 | Use as DCR and artifact-centric lineage for distinct relation, condition, response, milestone, and artifact-state positions. | No DCR, GSM, database, or verification-method semantics are adopted as FPF ontology. |
| Modelica Association, *Modelica Language Specification* 3.7 (2026); JuliaHub, Dyad documentation 3.1.0 (2026-06-10), including acausal component and analysis documentation | Adopt the current relation-first pattern for model-related transformation-flow slices: component-model construction, connection checking, mode handling, and simulation setup can be organized before one calculation direction, analysis, compiler output, solver run, or simulation trace is selected. | E.18.3 governs only the transformation-flow slice that prepares, checks, or uses a model-related structure. It does not govern the physical model, solver semantics, compiler semantics, analysis result, or AI-agent edit. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use these model-toolchain sources to keep symbolic model structure, graph transformations, calibration analyses, surrogate components, exchange packages, and result publications as exact separately governed values connected through transformation-flow relations. | E.18.3 does not prove mathematical adequacy, domain validity, evidence readiness, source currentness, or publication truth. Those claims leave to `C.29`, domain DPF patterns, evidence patterns, `G.11`, or publication patterns. |
| Current FPF `E.18`, `E.23`, `C.18`, `C.19`, and `G.11` practice | Use local path slices, feedback relations, candidate-population stewardship, and currentness returns as separately governed structure positions rather than one master process. | Architecture, work, evidence, improvement, archive, front, pool, E.18 slice-local refresh, and G.11 currentness claims remain governed by their direct patterns. |

As of 2026-07-11, OCPQ is the current research comparator for typed multi-object constraint structure, while Modelica 3.7 and Dyad 3.1.0 are current engineering comparators for relation-first models separated from analyses and execution. The older CMMN, Declare, DCR, and artifact-centric rows supply lineage. These source decisions changed `4.0` by requiring exact typed relations before continuation, `4.1` by keeping separately governed positions explicit, `4.2` by preserving graph-shaped alternatives behind a linear demonstration, and the physical case by separating structure from work and analysis. Reopen the adoptions when object-centric constraint methods change object-relation treatment, model languages change model-analysis separation, or use evidence shows that these distinctions no longer prevent workflow, query-result, or execution-artifact overread.

### E.18.3:12 - Relations

Specializes: the `A.22.CGUS` use of `ConstraintGovernedUnfoldingStructure@Context` when the substrate is bounded transformation-flow structure with typed transformation positions, exact relation refs, crossings, guards, valuations, preserved structures, C.33 adequacy notes, and governing-position connections.

Builds on: `E.18`, `A.3.4`, `A.22`, and `E.17` for transformation-flow structure and publication discipline.

Coordinates with: `E.18.1`, `C.32.P2S`, `C.30.TFS-REL`, `E.23`, `C.18`, `C.19`, `G.5`, `A.15`, `A.10`, `B.3`, `A.20`, `A.21`, `A.6.3.NAR`, and `G.11`.

Does not replace: direct method, work, evidence, gate, architecture, decision, publication, mathematical-lens, E.18 slice-local refresh, or G.11 currentness patterns.

### E.18.3:End

