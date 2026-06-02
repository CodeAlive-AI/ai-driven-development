## C.30.ASV - Architecture Structural View Adequacy (ASV)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.ASV:1 - Problem frame

Use this pattern when an architecture discussion needs to say which selected structure is being viewed, not merely that there is a diagram, model, table, dashboard, ADR, generated relation graph, or generic "view".

The first useful move is `ArchitectureStructureKindTriage@Project`:

```text
ArchitectureStructureKindTriage@Project:
architectureClaimRef?:
describedHolonRef?:
boundedContextRef?:

live architecture concern:
suspected wrong collapse:
practitioner prompt label:
candidate structure kinds:
smallest useful structure-kind set:
primaryGoverningPatternApplicationRef:
admissibleArchitectureMove:
governingPatternApplicationRefs:
stop condition:
```

Ordinary minimum: name the live architecture object or the described holon and bounded context, the one structure kind or structure-kind set that changes action, one non-admissible overread, and the next admissible architecture move or stop. All other fields are conditional and may be `not live`.

Start with `C.30` when the architecture claim itself is unclear. Use C.30.ASV only when a view over selected architecture-relevant structure changes the next architecture move. Use the triage record when it names the live structure kind and the next admissible architecture move. Open a full `ArchitectureStructuralView@Context` only when the view changes action, selected support reading, correspondence, source return, publication, comparison, evidence, assurance, gate, decision, or exact governing pattern use.


What goes wrong if C.30.ASV is missed: "architecture" silently means "module diagram"; a view becomes a publication face; a viewpoint becomes a structure kind; TEVB is stretched into a full architecture ontology; a Transduction Graph Architecture (TGA) graph, Layered Control Architecture (LCA)/control sketch, code-agent relation graph, or neural-network block diagram becomes the architecture by appearance.

What C.30.ASV buys in practice: the practitioner can name the architecture claim, selected structures, structure kind, viewpoint, selected relation kinds, selected constraints, selected invariants, live operation or dynamics descriptions, hidden or lost structure, correspondence, source or reliance relation, source-return condition, admissible use, and non-admissible use before relying on a view.

Not this pattern when the live question is only the general architecture claim. Use `C.30`. If the live question is structure as such, use A.22. If the view is a TGA graph/path/crossing relation, use `E.18` and `C.30.TGA-FLOW-REL` when architecture-flow description is live. If the view is used as evidence, assurance, causal proof, gate result, work record, release permission, or decision authority, use the exact governing pattern and keep C.30.ASV only to the view portion.

Thin precision-restoration pointer: if the live issue is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural view, an architecture description, a publication face, a carrier, a source relation, or another receiving object, use `C.30.P` first. Do not copy the `C.30.P` trigger table here; C.30.ASV resumes only after the architecture structural-view object or exact non-ASV exit is recoverable.
### C.30.ASV:2 - Problem

An architecture structural view is not a generic view. It is a D/S view over one or more `candidate:U.Structure` references selected by an `ArchitectureOf@Context` claim record. A conforming architecture structural view keeps the D/S relation, described entity, bounded context, structure references, structure kind, viewpoint, hidden or lost structure, correspondence, source or reliance relation, source return, and admissible use recoverable.

Without this pattern:

- a module/interface view is treated as all architecture;
- a TGA graph or control diagram is treated as proof;
- a structure kind is treated as a `U.Viewpoint`;
- a TEVB viewpoint bundle is mutated to carry architecture-specific structure kinds;
- a diagram, table, dashboard, generated relation graph, or ADR is treated as the view itself;
- functional architecture is treated as a peer ontology rather than a structure-kind reading under C.30;
- cross-view consistency is asserted by prose instead of correspondence records;
- omitted structure is relied on in subsequent work without a source-return condition.

### C.30.ASV:3 - Forces

| Force | Tension |
| --- | --- |
| View usefulness vs view overread | Views make architecture discussable, but a useful artifact can be mistaken for the architecture claim, selected structure, publication, proof, or decision. |
| Structure kind vs viewpoint | A structure kind classifies selected structure; a viewpoint names a way of viewing. They often travel together but are not the same kind. |
| TEVB reuse vs TEVB mutation | TEVB gives useful engineering viewpoints over holons; architecture needs more structure kinds without expanding the TEVB core by implication. |
| Small triage vs full view record | Many cases need only the live structure kind and next move; full view records are justified only when they change action. |
| Multi-view correspondence vs single-view shortcut | Architecture work often needs relations among functional, flow, control, module, information, work, evidence, scale, and placement views; one favored diagram cannot carry all claims. |
| Hidden structure vs practical compression | A useful view omits something; omitted structure becomes a problem only when subsequent action relies on it. |

### C.30.ASV:4 - Solution

Govern architecture structural views with `ArchitectureStructuralView@Context` records. A conforming record is a D/S view over selected `candidate:U.Structure` references in one `ArchitectureOf@Context` claim record, under one declared `ArchitectureStructureKindRef` and one `DescriptionContext.ViewpointRef`.

C.30.ASV does not extend the TEVB core viewpoint set by implication. It defines architecture structure kinds and architecture-specific structure-kind/view-record bindings. TEVB viewpoints are reused when the structure-kind view uses one of the TEVB core viewpoints; other structure-kind views use `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, an exact governing FPF pattern, or a source/reliance record.

#### C.30.ASV:4.1 - Architecture structural view record
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

```text
ArchitectureStructuralView@Context ::= {
  viewId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    DescribedEntityRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  viewpointRef: U.ViewpointRef (= descriptionContext.ViewpointRef),
  structureRefs: FinSet(candidate:U.StructureRef),
  structureKindRef: ArchitectureStructureKindRef,
  recordGoverningPatternRef,
  selectedRelationKinds,
  selectedConstraintRefs?,
  selectedInvariantRefs?,
  selectedOperationOrDynamicsDescriptionRefs?,
  viewConstruction:
    directDescription | projection | query | extraction |
    coarsening | correspondenceSlice | sourceReturnSlice,
  structuralAspectDescriptionRef?,
  hiddenOrLostStructure,
  structureKnowledgePosture?:
    declared | observed | inferred | generated | simulated |
    extracted | hypothesized | unknownRegionPresent,
  correspondenceModelRefs?,
  sourceOrRelianceRelationRefs?,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`DescriptionContext.DescribedEntityRef` is the `ArchitectureOf@Context` claim record. The described holon is recovered through `architectureClaimRef.describedHolonRef`. The bounded context is recovered through the claim record and `DescriptionContext`.

`viewpointRef` is a recovery label for `descriptionContext.ViewpointRef`, not a second independent viewpoint slot. If the implementation stores only `DescriptionContext`, the viewpoint remains recoverable there.

`structureKnowledgePosture?` states how the selected structure is known when partial knowledge matters: declared, observed, inferred, generated, simulated, extracted, hypothesized, or with an unknown region present. Unknown or inferred structure may guide inspection or source return; it cannot by itself supply assurance, gate, release, causal proof, or architecture decision.

#### C.30.ASV:4.2 - Architecture structure-kind classifier

`ArchitectureStructureKindRef` is a C.30-local `DiscriminatorToken` enumeration over architecture-relevant `candidate:U.Structure` references selected by `ArchitectureOf@Context`. It is not `U.Kind`, `U.Viewpoint`, `U.ViewpointBundle`, `StructuralAspectDescription`, `StructuralView@Context`, or a root `U.*` kind. `ArchitectureStructuralView@Context` uses `structureKindRef` to say which selected structure kind is being viewed.

```text
ArchitectureStructureKindRef ::= one of {
  FunctionalStructure,
  FlowTransductionStructure,
  ControlStructure,
  ModuleInterfaceStructure,
  RuntimeInteractionStructure,
  PlacementDeploymentStructure,
  InformationDataStructure,
  SecurityTrustBoundaryStructure,
  ConstraintRequirementStructure,
  MaterialSpatialStructure,
  DeclaredLogicalStructure,

  WorkMethodStructure,
  RoleEnactorStructure,
  EvidenceAssuranceStructure,
  ScaleEvolutionStructure,
  OtherDeclaredStructureKind
}
```

The first group is the seed classifier set for ordinary architecture structural-view use. `WorkMethodStructure`, `RoleEnactorStructure`, `EvidenceAssuranceStructure`, and `ScaleEvolutionStructure` are neighbor-governed classifier values: ASV may use them to name the selected architecture-relevant structure, but their full semantics stay in the named work/method, role/enactor, evidence/assurance, scale, characterization, or mathematical-lens patterns.
Do not enumerate structure kinds by default. Choose the smallest useful structure-kind set that changes the next architecture move. If no structure kind changes action, keep the phrase as ordinary recognition wording or a source note. This does not weaken kind discipline; it prevents `ArchitectureStructureKindRef` from becoming an audit checklist.

Inside C.30.ASV, `OtherDeclaredStructureKind` is always an architecture-structure-kind classifier value over `candidate:U.Structure`; it does not mint a general FPF root kind.

`OtherDeclaredStructureKind` is admissible only when the local text names:

- `declaredStructureKindName`;
- `declaredStructureKindDefinition`;
- allowed relation families;
- common false readings;
- exact governing pattern applications;
- `boundedContextRef`.

Each structure kind needs a short definition, allowed relation families, common false readings, typical exact governing pattern applications, and example architecture structural view records. This is not a new root-kind set; it is a controlled classifier set over `candidate:U.Structure`.


#### C.30.ASV:4.3 - Small triage output

Use `ArchitectureStructureKindTriage@Project` before a full view record when the practitioner only needs to identify the live structure kind and next architecture move.

```text
ArchitectureStructureKindTriage@Project ::= {
  architectureClaimRef?: ArchitectureOf@ContextRef,
  describedHolonRef?: U.HolonRef,
  boundedContextRef?: U.BoundedContextRef,
  liveArchitectureConcernCue,
  suspectedWrongCollapse,
  plainPromptLabel,
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  smallestUsefulStructureKindRefs,
  structureKnowledgePosture?,
  primaryGoverningPatternApplicationRef,
  temptingWrongPatternRefs?,
  admissibleArchitectureMove:
    inspect | split | relate | downgrade | assignNeighbor | stop |
    otherDeclared,
  candidateGenerationPatternApplication?: yes | no,
  governingPatternApplicationRefs,
  stopCondition
}
```

`primaryGoverningPatternApplicationRef` names the pattern that carries the next live claim kind. `candidateGenerationPatternApplication?` marks that the next admissible move is to leave ASV for candidate generation; it is not ASV work. `temptingWrongPatternRefs?` names tempting wrong first patterns when that repair is needed. None of these fields governs the triage record itself; C.30.ASV governs the triage record family.
When `architectureClaimRef` is absent, `describedHolonRef` and `boundedContextRef` are required for triage. This pre-claim form does not create a new kind and does not publish an `ArchitectureOf@Context` claim by itself; it only lets the practitioner identify the live structure kind before opening a full architecture claim. A full `ArchitectureStructuralView@Context` still requires `architectureClaimRef`; do not promote triage to a full view record until that architecture claim is available.


Practitioner prompt labels are first-entry cues, not `ArchitectureStructureKindRef` values. FPF-force-bearing records use the Tech values below:


```text
Functional -> FunctionalStructure
Flow -> FlowTransductionStructure
Control -> ControlStructure
Module -> ModuleInterfaceStructure
Method/work -> WorkMethodStructure
Role -> RoleEnactorStructure
Evidence -> EvidenceAssuranceStructure
Scale -> ScaleEvolutionStructure
Security -> SecurityTrustBoundaryStructure

```

#### C.30.ASV:4.4 - Architecture viewpoint bundle and binding rows

Architecture structural views use `VF.ARCH.STRUCTURE` without turning structure kinds into viewpoints. The bundle is separate from `VF.TEVB.ENG`: it may import TEVB, but it does not expand the TEVB core engineering viewpoint set.

Declaration basis: `VF.ARCH.STRUCTURE` is an `E.17.1`/`F.18` declared viewpoint bundle for architecture structural-view records. Its `VP.Architecture*` ids are viewpoint ids only. They do not add TEVB viewpoints, name structure kinds, define publication faces, or carry decision, evidence, gate, or assurance authority.

```text
VF.TEVB.ENG core stays:
  { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
```

TEVB is the small engineering viewpoint bundle over holons. The architecture problem is broader than TEVB, but the broader coverage is not solved by placing record sets inside a `U.ViewpointBundle`. The `U.ViewpointBundle` carries viewpoints; a separate architecture-local description binds structure kinds, view record sets, construction modes, correspondence obligations, and exact governing pattern applications.

```text
VF.ARCH.STRUCTURE : U.ViewpointBundle {
  viewFamilyId = VF.ARCH.STRUCTURE,
  imports = { VF.TEVB.ENG },
  EoIClassSpec = {
    a : ArchitectureOf@Context |
    a.describedHolonRef and a.boundedContextRef are recoverable
  },
  viewpoints = {
    VP.ArchitectureStructure,
    VP.ArchitectureCorrespondence,
    VP.ArchitectureSourceReturn,
    VP.ArchitectureDecisionAffectedStructure
  }
}

ArchitectureStructureKindViewRecordBinding ::= {
  structureKindRef: ArchitectureStructureKindRef,
  allowableViewpointRefs: FinSet(U.ViewpointRef),
  viewRecordSetRef,
  allowedViewConstructionModes,
  requiredCorrespondenceRefs?,
  sourceReturnRequirement?,
  governingPatternApplicationRefs
}
```

`viewRecordSetRef` names the allowed D/S record set for one structure-kind binding. It is not a package grouping, not a `U.ViewpointBundle`, not a `ViewFamilyId`, and not a new TEVB viewpoint.

#### C.30.ASV:4.5 - Initial architecture structure kinds and view records

The initial set is a seed for first architecture moves, not an atlas. Use the table to choose one live structure kind and the exact governing pattern application that carries any stronger claim.

| Seed structure kind | Structural view | Minimum record fields beyond common ASV fields | First boundary |
| --- | --- | --- | --- |
| `FunctionalStructure` | `FunctionalStructureView@Context` | function/effect refs, capability refs, dependency refs, allocation refs | Use `A.6.F`, capability, work, or requirement patterns when those claims are live. |
| `FlowTransductionStructure` | `FlowTransductionStructureView@Context` | `transductionGraphRef`, `pathSliceRefs`, `crossingRefs`, `valuationRefs` | Use `E.18` and `C.30.TGA-FLOW-REL` for graph/path/crossing structure input; use `C.28` for causal claims. |
| `RuntimeInteractionStructure` | `RuntimeInteractionStructureView@Context` | runtime elements, connectors/protocols, event/message topology, failure/latency boundaries | Use temporal, failure, evidence, or assurance patterns when runtime claims exceed structure. |
| `ModuleInterfaceStructure` | `ModuleInterfaceStructureView@Context` | module relation refs, interface specs, admissibility conditions, substitutability/change policy | Use the exact module/interface repair pattern and conformance evidence when those claims are live. |
| `PlacementDeploymentStructure` | `PlacementDeploymentStructureView@Context` | allocation-to-site/environment refs, network/physical locality, jurisdiction/safety constraints | Use temporal, evidence, legal/regulatory, or safety patterns for those stronger claims. |
| `InformationDataStructure` | `InformationDataStructureView@Context` | state bearer and residence refs, schema refs, semantic refs, persistence locus, provenance relation, custody relation, source-return conditions, privacy constraints | Use evidence, privacy, or source-return patterns when those claims are live. |
| `SecurityTrustBoundaryStructure` | `SecurityTrustBoundaryStructureView@Context` | protected asset or effect refs, trust boundary refs, untrusted input refs, privilege or authority refs, data-flow and control-flow refs, attack exposure refs, abuse or misuse path refs, secure-default or hardening boundary, supply-chain or update-channel refs, detection-response boundary refs when live | Gives a first security-architecture move before evidence, assurance, gate, risk-score, or compliance proof. |
| `ControlStructure` | `ControlStructureView@Context` | control role refs, declared control-rate refs, observer/estimator/controller/planner/supervisor relations, feedback refs | Use `C.30.LCA`, dynamics, temporal, causal, evidence, and assurance patterns when those claims are live. |
| `ConstraintRequirementStructure` | `ConstraintRequirementStructureView@Context` | requirement/constraint/invariant refs, affected structure refs, admissibility conditions | Requirements shape structures; requirement, gate, evidence, causal, or decision claims apply their exact governing patterns. |
| `MaterialSpatialStructure` | `MaterialSpatialStructureView@Context` | geometry, adjacency, containment, energy/material flow, safety separation | Physical separation is not safety proof; safety, evidence, dynamics, or causal claims apply their exact governing patterns. |
| `DeclaredLogicalStructure` | `LogicalStructureView@Context` | local logical relation class, relation constraints, correspondence to functional/module/runtime/data structures | Covers `logical architecture` without making `logical` a universal ontology token. |

Externally governed classifier values remain admissible when they are the live architecture-relevant structure, but C.30.ASV does not define their full record families:

| Externally governed classifier value | ASV use | Full semantics and governing patterns |
| --- | --- | --- |
| `WorkMethodStructure` | Method/work arrangement changes the architecture move. | Use `MethodDescription`, `WorkPlan`, `WorkEnactment`, exception path, launch/gate relation, and `A.15` governing patterns; do not turn a work-method diagram into work authority. |
| `RoleEnactorStructure` | Responsibility or enactor allocation changes the architecture move. | Use role, enactor, organization, work, and stakeholder patterns for the stronger claim; do not treat an org chart as architecture truth. |
| `EvidenceAssuranceStructure` | Evidence reuse or assurance arrangement changes affected structure or source return. | Use `A.10`, `G.6`, or `B.3` for evidence sufficiency or assurance verdict; ASV only names the structure and loss boundary. |
| `ScaleEvolutionStructure` | Scale window, replacement path, or coarse-graining changes the architecture move. | Use `C.29`, `C.16`, temporal, source-return, or decision patterns for scale, characterization, or selection claims. |
| `OtherDeclaredStructureKind` | A local structure kind is declared because none of the seed or externally governed values fits. | Name definition, relation families, false readings, governing patterns, and context; do not mint a root kind by label alone. |

Minimum useful seed examples:

| Structure kind | Minimal example | False reading | First governing pattern |
| --- | --- | --- | --- |
| `FunctionalStructure` | Capability, effect, or transformation allocation. | Purpose truth or requirement satisfaction. | `A.6.F`, capability, work, or requirement pattern as live. |
| `FlowTransductionStructure` | Path, crossing, valuation, or transduction slice. | Whole architecture or causal proof. | `E.18`, `C.30.TGA-FLOW-REL`, C.29, or C.28 as live. |
| `ControlStructure` | Controller, observer, plant, feedback, or rate relation. | Stability, safety, or assurance proof. | `C.30.LCA`, temporal, dynamics, causal, evidence, or assurance claim as live. |
| `ModuleInterfaceStructure` | Module relation, interface spec, or substitutability boundary. | Module tree as all architecture. | Exact module/interface repair pattern, conformance evidence, or decision pattern as live. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody. | Database label. | Evidence, privacy, or source return as live. |
| `SecurityTrustBoundaryStructure` | Trust boundary, untrusted input, privilege path, or attack exposure. | Security proof, risk score, or compliance label. | Evidence, assurance, gate, C.24, C.16, C.25, or C.30.LCA as live. |
| `MaterialSpatialStructure` | Separation, adjacency, containment, or energy/material path. | Safety proof or geometry as architecture truth. | Safety, evidence, dynamics, or causal claim as live. |
| `DeclaredLogicalStructure` | Local logical relation class with correspondence to other structures. | Universal logical architecture ontology. | Correspondence, function, module, runtime, data, or exact declared-neighbor pattern as live. |
Minimal `SecurityTrustBoundaryStructureView@Context` fields:

```text
SecurityTrustBoundaryStructureView@Context ::= {
  architectureStructuralViewRef:
  protectedAssetOrEffectRefs:
  trustBoundaryRefs:
  untrustedInputRefs:
  privilegeOrAuthorityRefs:
  dataFlowOrControlFlowRefs:
  attackExposureRefs:
  abuseOrMisusePathRefs:
  secureDefaultOrHardeningBoundary:
  updateOrSupplyChainChannelRefs:
  detectionResponseBoundaryRefs?:
  governingPatternApplicationRefs:
    A.10 | G.6 | B.3 | C.28 | A.20 | A.21 |
    C.16 | C.25 | C.24 when tool authority or agentic tool-use is live | C.30.LCA when control relation is live
  admissibleUse:
  nonAdmissibleUse:
    not compliance proof, not risk score, not assurance verdict, not security by checklist, not secure because a diagram says "zero trust"
}
```

`SecurityTrustBoundaryStructure` carries adversarial-boundary reading: which protected assets or effects are live, who or what is trusted, where untrusted input crosses, what authority or privilege is exposed, which adversarial paths and attack exposures matter, which data-flow or control-flow security boundaries matter, and where secure defaults, hardening, update or supply-chain channels, detection, or response boundaries change the next architecture move.

Do not open evidence, assurance, gate, or compliance pattern use only because the topic is safety, security, or regulation. Open it when the architecture move relies on evidence sufficiency, assurance verdict, gate passage, regulatory acceptance, or release authority. If the live move is structural, first recover the structure: trust boundary, loss-control relation, control relation, evidence reuse structure, or affected structure/view.

Use a `SafetyLossControlStructureNote` when a safety-architecture concern first needs the architecture-side loss-control structure rather than a safety-case verdict:

```text
SafetyLossControlStructureNote:
  lossOrHarm:
  hazardOrUnsafeState:
  unsafeControlActionOrMissingControl:
  controlledProcessOrPlantRef:
  controlConstraintRef:
  feedbackOrObservabilityBoundary:
  timingOrRateBoundary:
  operationalDesignScopeOrMisuseScope:
  foreseeableMisuseRefs?:
  architectureStructureKindRefs:
    ControlStructure | ConstraintRequirementStructure |
    SecurityTrustBoundaryStructure | InformationDataStructure |
    EvidenceAssuranceStructure
  governingPatternApplicationRefs:
    A.3.3 dynamics, C.27 temporal or rate,
    C.28 causal-use, A.10/G.6 evidence,
    B.3 assurance, A.20/A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

#### C.30.ASV:4.6 - Functional structure view boundary



`FunctionalStructureView@Context` under C.30.ASV does not mint `U.Function`. A functional element is a description-side architecture element under `VP.Functional` unless separately grounded as `U.Capability`, `U.Method`, `U.Work`, `U.Role`, or another existing FPF kind.

```text
FunctionalStructureView@Context ::= {
  architectureStructuralViewRef: ArchitectureStructuralView@ContextRef,
  functionOrEffectRefs?,
  capabilityRefs?,
  functionalDependencyRefs?,
  allocationRefs?,
  nonFunctionCarrierNotes?,
  flowRelationRefs?,
  moduleInterfaceRelationRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

A transduction graph, path slice, crossing, or flow valuation is not a functional element. When flow is live, connect the functional view to `FlowTransductionStructure` through `C.30.TGA-FLOW-REL`. When module allocation is live, connect the functional view to the exact module/interface repair pattern rather than treating function and module as one object.

Composability and quality compositionality are separate claims. If the view says parts can be assembled, keep that as a structure/use claim. If it says a whole-system quality follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim.

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredCarrierKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredCarrierKind: QBundleSlot | structuralCharacteristicSupportsQBundleSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidenceSupportForQBundleSlot
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures and view/model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

#### C.30.ASV:4.7 - Correspondence and source return

Use correspondence records when the view relates functional, flow, control, module/interface, information, runtime, placement, work, evidence, scale, or logical structures. Do not assert cross-view consistency by prose alone.

Correspondence examples:

| Source wording | Recover |
| --- | --- |
| "This function is implemented by that module." | `FunctionToModuleAllocationRef` or the exact governing carrier. |
| "This flow crosses that runtime boundary." | `FlowToRuntimeInteractionCorrespondence`. |
| "This evidence covers the replacement." | `EvidenceReuseToAffectedStructure`; assign sufficiency or verdict to `A.10`, `G.6`, or `B.3`. |
| "This requirement constrains that structure." | `RequirementToStructureConstraint` or exact constraint carrier. |
| "This scale window changes the structure kind." | `ScaleWindowToStructureKindCorrespondence`; assign scale-lens claims to `C.29` when live. |

Use `SourceReturnCondition` when compression, extraction, coarsening, evidence reuse, ML evaluation, bounded exception, many-to-many allocation, publication, or decision claim hides a distinction needed for action, assurance, causal use, legal review, regulatory review, comparison, or reopening.

If `viewConstruction` is `query`, `extraction`, `coarsening`, `correspondenceSlice`, or `sourceReturnSlice`, and omitted structure changes action, assurance, causal use, legal or regulatory review, or subsequent decision reopening, `SourceReturnCondition` is live.

When the view is used to name affected structures for a next move but no decision record is live, use C.30 `AffectedArchitectureStructureNote`: affected structure kinds, affected structure refs when known, affected ASV refs, accepted or suspected view loss, source-return condition, and the next admissible move. The note is not an architecture decision, ADR, gate passage, evidence sufficiency, or release authority.

Use the thinnest source or reliance relation that preserves the next architecture move. Open fuller source, evidence, assurance, or claim-kind relation only when the current source or reliance relation cannot be inspected, used, compared, refreshed, or bounded without it. A `ControlStructureViewNote` may precede full `C.30.LCA` use or proof-governing pattern applications when one control relation and its boundary are enough for the current move.

Treat source return as a user action, not only a metadata field:

```text
SourceReturnAction:
  returnTo:
    sourceStructure | sourceEpisteme | sourceView | sourceTrace |
    sourceCorpus | sourceModel | sourceEvidence | sourcePublication
  because:
    hiddenRelation | lostConstraint | coarsenedScale |
    ambiguousExtraction | staleEdition | crossViewMismatch |
    legalOrRegulatoryUse | assuranceOrDecisionUse
  nextMove:
    inspect | split | downgradeUse | addCorrespondence |
    openNeighborPattern | stop
```


Do not make source return mandatory for ordinary local recognition when no hidden distinction is being used for action. Do not omit source return when a hidden distinction carries a selected support reading, assurance, legal, comparison, causal, gate, or decision claim force. The condition is live only when the repaired text still relies on the hidden source-side distinction.

Model cards, system cards, and evaluation harness reports may publish or substantiate an architecture structural view only when the structural-view claim is recoverable. The view must name the relevant structure kind, such as `RuntimeInteractionStructure`, `InformationDataStructure`, `SecurityTrustBoundaryStructure`, `EvidenceAssuranceStructure`, `ModuleInterfaceStructure`, or another declared structure kind; it must also state intended-use scope, evaluation scope and known loss when evaluation is used, deployment-context mismatch when live, and the evidence or assurance governing pattern when the publication is used beyond transparency. A card or harness is not architecture adequacy, safety proof, or release/gate claim by publication alone.

#### C.30.ASV:4.8 - Worked slices

**Runtime degradation.** A team says, "The architecture is fine, but incidents happen when failover starts." The first architecture move is to recover runtime interaction, control/failover, placement, and evidence-assurance structures before turning a dashboard or deployment diagram into proof:

```text
Runtime degradation slice:
  active structure kinds:
    RuntimeInteractionStructure
    ControlStructure
    InformationDataStructure
    PlacementDeploymentStructure
    EvidenceAssuranceStructure
  first architecture move:
    recover runtime interaction topology, control/failover relation,
    state custody, placement/locality, evidence path, and observability relation
  nonAdmissibleUse:
    deployment diagram as runtime proof,
    observability dashboard as evidence sufficiency,
    green status as gate/release authority
```

Use `C.24` only when tool-use, call planning, call graph, work execution, or budgeted agentic tool-use is the live claim. Do not absorb those claims into architecture structure.

**CPS or plant architecture.** A plant drawing, P&ID-like artifact, LCA sketch, or safety-case view is not the plant architecture by itself. First recovery may need:

```text
CPS/plant architecture first recovery:
  MaterialSpatialStructure:
    physical separation, adjacency, energy/material path
  ControlStructure:
    controller, plant, observer, supervisor, control rate
  InformationDataStructure:
    sensor data semantics, provenance, custody, source return
  PlacementDeploymentStructure:
    locality, environment, jurisdiction, safety separation
  EvidenceAssuranceStructure:
    evidence reuse boundary and affected structures
first architecture move:
  relate physical separation, sensor data semantics, control rate,
  placement boundary, and evidence reuse
correspondenceOrLossLine:
  record which separation, data, control-rate, placement, or evidence-reuse
  relation is preserved by the slice and which structure is hidden or lossy
stop condition:
  no P&ID, LCA diagram, or safety case is treated as the architecture
```

**Chiplet or device architecture.** A packaging diagram or interconnect sketch may open several structure kinds:

```text
Chiplet/device architecture first recovery:
  MaterialSpatialStructure:
    packaging, adjacency, thermal path, energy path
  FlowTransductionStructure:
    interconnect topology, data/energy/signal flow path
  ModuleInterfaceStructure:
    interface specification, protocol, conformance boundary
  PlacementDeploymentStructure:
    physical locality, substrate, host environment
first architecture move:
  separate interconnect topology, packaging/thermal/energy path,
  interface specification, and evidence/conformance boundary
correspondenceOrLossLine:
  record the preserved relation among interconnect, physical package,
  interface, and placement, plus any benchmark or packaging-view loss
stop condition:
  no packaging diagram or benchmark becomes performance, safety,
  evidence, or gate proof by appearance
```

**Organization or operating-model architecture.** An org chart or work-method diagram can be architecture-relevant only after the work, role, information, and evidence carriers are separated:

```text
Organization/operating-model architecture first recovery:
  RoleEnactorStructure:
    responsibility allocation and enactment boundary
  WorkMethodStructure:
    repeatable work method and exception path
  InformationDataStructure:
    information custody, state residence, provenance
  EvidenceAssuranceStructure:
    evidence reuse, approval, audit trail, source return
first architecture move:
  relate responsibility allocation, work repeatability,
  information custody, and evidence reuse
correspondenceOrLossLine:
  record the preserved relation among role, work, information, and evidence
  structures, plus any org-chart or work-method-diagram loss
stop condition:
  no org chart or work-method diagram is treated as the architecture, decision,
  evidence sufficiency, or assurance verdict
```

**Evidence reuse across product variants.** A certification or test package reused across module variants may be architecture-relevant as an evidence/assurance structure view, but it is not an assurance verdict:

```text
Evidence reuse across product variants:
  structureKindRef: EvidenceAssuranceStructure
  structuralFeature:
    evidence package shared across module variants
  affectedQBundleSlot:
    assurance maintainability or release readiness
  architectureMove:
    name affected structures, variant boundary, hidden view losses,
    and source-return condition
  governingPatternApplicationRefs:
    A.10/G.6/B.3 for evidence sufficiency or assurance verdict
  nonAdmissibleUse:
    evidence-structure view as assurance verdict
```

**AI agent diagram.** A "planner-memory-tools" diagram is not the agent's architecture by itself. It may open first recovery as a structure-kind set, without minting an AI-domain ontology:

```text
AI-agent architecture first recovery:
  RuntimeInteractionStructure:
    model-tool-memory-planner-evaluator-human topology
  InformationDataStructure:
    memory scopes, data custody, provenance, retention,
    context-window/source-return
  SecurityTrustBoundaryStructure:
    untrusted content channels, prompt-injection or instruction boundary,
    tool authority, secret-bearing contexts, memory/data custody crossing,
    output handling, supply-chain or update path
  ModuleInterfaceStructure:
    tool/API/interface specs and substitutability limits
  EvidenceAssuranceStructure:
    eval harness, human approval, evidence decay, incident feedback
admissibleArchitectureMove:
  split runtime interaction, information, security boundary, module-interface, and evidence-assurance claims before relying on the diagram
correspondenceOrLossLine:
  record the preserved relation among runtime topology, information custody,
  security boundary, module-interface, and evidence-assurance structures,
  plus any diagram or evaluation-harness loss
governingPatternApplicationRefs:
  C.30.TGA-FLOW-REL when E.18 flow relation is live,
  exact module/interface repair pattern for tool, API, or interface relation claims,
  A.10/G.6/B.3 when evidence or assurance reliance is live,
  C.24/E.16/A.20/A.21 when tool-call, autonomy, constraint, or gate authority is live
stop condition:
  no evidence sufficiency, assurance, gate, autonomy, or tool-call authority remains inside ASV
```

Structural AI-agent security is architecture structure when these structure kinds change the next architecture move. When the live claim is latent representation, decoding, or effect adequacy rather than architecture structure, keep the phrase as a reduced-use source cue until the exact governing representation, decode, or effect-adequacy pattern carries that claim.

**Generated code-agent relation graph.** A probe JSON or code-agent architecture relation graph can be an architecture structural view publication only after observed/inferred/unknown status, evidence/source pointers, unexplored regions, typed relation semantics, and source-return conditions are present. It is not proof of the agent's internal belief and not assurance that a downstream code change is safe.

**Neural-network block replacement.** Replacing attention, FFN, convolution, SSM, recurrent, memory/cache, MoE expert-selection, pruning, distillation, or another block is an architecture move only when the changed structure kind, flow relation, module/interface claim kind, preserved and lost structure, affected characteristic, source relation, and decision or evidence governing pattern are named.

### C.30.ASV:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner looks at an architecture "view" and asks whether it is functional, flow, control, module/interface, information/data, placement, scale, work/evidence, or declared logical structure. C.30.ASV turns that question into structure-kind triage or a full structural view record. |
| Show: `U.System` | A plant, vehicle, software system, product platform, AI-agent system, or neural-network model may need several structural views over the same architecture claim. One module view does not exhaust the system architecture, and one flow graph does not prove work, evidence, safety, or release. |
| Show: `U.Episteme` | A diagram, model, generated relation graph, ADR, dashboard, SysML view, or C4 diagram is an episteme, view, or publication face. It can publish an architecture structural view only when the architecture claim, structure refs, structure kind, viewpoint, hidden/lost structure, correspondence, source or reliance relation, and admissible use are recoverable. |

### C.30.ASV:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**, **Gov**. Scope: architecture structural-view claims over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-view bias | Make module/interface one structure kind, not the default meaning of architecture. |
| Viewpoint-kind conflation | Keep structure kind, viewpoint, view record, and viewpoint bundle separate. |
| TEVB mutation bias | Import TEVB where useful; do not expand `VF.TEVB.ENG` by implication. |
| Check-only bias | Every failed conformance check gives a repair move or exact governing pattern application. |
| Didactic-thinning risk | The pattern starts with triage and action, not taxonomy alone. |

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, view, relation, or repair move above.

### C.30.ASV:7 - Conformance Checklist


| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-ASV-1 Structure target.** | Every architecture structural view names `structureRefs` or a recoverable selected-structure reference. | Name the selected structure reference, or downgrade the artifact to an architecture question, diagram, note, or publication that does not claim to be a structural view. |
| **CC-ASV-2 Structure kind.** | Every architecture structural view names `structureKindRef`. | Run `ArchitectureStructureKindTriage@Project`; if no structure kind changes action, keep the text as ordinary prose or a source note. |
| **CC-ASV-3 Same described entity.** | The view preserves `architectureClaimRef`, `DescriptionContext`, and the claim record's `describedHolonRef` and `boundedContextRef` unless explicit retargeting or a bridge is declared. | Restore the same claim record and bounded context, or add an explicit retargeting or bridge note before using the view. |
| **CC-ASV-4 Viewpoint discipline.** | The view is under `VF.ARCH.STRUCTURE` or another declared architecture-specific bundle, rather than an ad-hoc tag. | Assign the view to `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, or a exact governing pattern; otherwise keep the label as Plain recognition wording. |
| **CC-ASV-5 Lost structure.** | The view names hidden or lost structure, especially for query, extraction, coarsening, or publication uses. | Add a one-line hidden/lost-structure note, or narrow the admissible use so omitted structure is not relied on. |
| **CC-ASV-6 Correspondence.** | Cross-view relations are carried by `correspondenceModelRefs` or correspondence records, not by prose alone. | Add a correspondence note or stop at a single-view statement without cross-view consistency claim. |
| **CC-ASV-7 No publication collapse.** | A diagram, model, table, dashboard, generated relation graph, or ADR is kept as publication, record, or carrier, not the architecture structural view itself. | Keep the artifact as publication or carrier and name the source episteme or view; do not require a full architecture view unless it changes the next move. |
| **CC-ASV-8 No single-view architecture.** | If a decision uses an architecture view as decision claim, it names the affected structures and views, not only one favored diagram. | Add affected structure and view refs, or narrow the statement to the single view's admissible use. |
| **CC-ASV-9 No proof overread.** | The view does not act as evidence, safety proof, causal proof, gate decision, or work record without a named exact governing pattern. | Assign the live claim to `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, or mark the proof, evidence, gate, or assurance use unsupported; do not add more C.30.ASV fields as a substitute. |
| **CC-ASV-10 Exact relation carrier.** | Every cross-reference uses exact carriers: structure, structure kind, viewpoint, correspondence, allocation, bridge, evidence relation, publication, interface specification, or exact governing record. | Replace the ambiguous reference with the carrier that actually bears the claim, or split the sentence into separate carriers. |
| **CC-ASV-11 Source return.** | When compression, extraction, coarsening, evidence reuse, publication, or many-to-many allocation hides distinctions, `SourceReturnCondition` is present. | Add one source-return trigger, or narrow the view's admissible use so omitted distinctions are not used for action, assurance, causal use, legal review, regulatory review, or reopening. |
| **CC-ASV-12 Architecture-name recovery.** | Every `<X>Architecture` phrase recovers `<X>StructureKind` or a declared local relation. | Rewrite the phrase through `ArchitectureStructureKindTriage@Project`; if no relation is live, keep the name as Plain prose and do not let it carry ontology. |
| **CC-ASV-13 Useful action.** | The repair leaves a surviving admissible architecture move: inspect, split, relate, downgrade, assign to an exact governing pattern, generate candidates, stop, open a structural view, add correspondence, add source return, or apply the exact governing pattern. | Restore one move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30.ASV:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Module diagram as architecture view** | One module/interface diagram is treated as the whole architecture. | Run structure-kind triage; keep module/interface as one structure kind and add other views only when they change action. |
| **Viewpoint as structure kind** | `VP.Functional`, `VP.ModuleInterface`, or another viewpoint is used as if it were the selected structure kind. | Recover `ArchitectureStructureKindRef` and bind it to a viewpoint through `ArchitectureStructureKindViewRecordBinding` when needed. |
| **Structure kind as viewpoint** | `FunctionalStructure` or `ControlStructure` is added to TEVB as a new viewpoint. | Keep TEVB core unchanged; use `VF.ARCH.STRUCTURE` and binding rows. |
| **Publication-face collapse** | A diagram, model, table, dashboard, generated relation graph, ADR, or C4 view is treated as the ASV record. | Recover source episteme/view and publication relation; open an ASV record only if the view changes action. |
| **Single-view decision** | A decision uses one architecture view as if it covered all affected structures. | Name affected structures and view refs, or narrow the decision to the single view's admissible use. |
| **Lost-structure silence** | Extracted, generated, coarsened, or compressed views hide distinctions but still justify action. | Add hidden/lost structure and source-return condition, or narrow admissible use. |
| **Proof overread** | The structural view is used as evidence sufficiency, safety proof, causal proof, gate decision, or work record. | Assign the live claim to the governing exact governing pattern and keep ASV only to view adequacy. |
| **Risk color as security architecture** | A red, yellow, or green risk cell, risk matrix, maturity score, or compliance color stands in for `SecurityTrustBoundaryStructure` or resource-allocation priority. | Recover protected asset or effect, trust boundary, untrusted input, privilege or authority relation, data/control flow, abuse or misuse path, and the exact evidence, assurance, measurement, causal, gate, selection, or allocation claim kind if it is live; do not treat ordinal risk color as security architecture adequacy, resource-allocation priority, or gate passage. |
| **Taxonomy without action** | The text classifies a view but does not say what changes in practice. | Add `admissibleArchitectureMove` or stop at Plain recognition wording. |

### C.30.ASV:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture views become D/S records over selected structures, not diagrams by appearance. | A conforming use states architecture claim, structure refs, structure kind, viewpoint, and use when the view carries FPF force. |
| TEVB remains stable while architecture gets broader structure-kind coverage. | Structure-kind bindings add one explicit record when architecture-specific coverage matters. |
| Functional, flow, control, module/interface, placement, information, runtime, work, evidence, scale, material, and logical structures can be separated. | Some familiar names require triage before they can carry FPF claim kinds. |
| Failed checks produce repair moves rather than only classification objections. | The checklist is longer than a pure taxonomy, but it is more useful for action. |

### C.30.ASV:10 - Rationale

C.30.ASV exists because architecture descriptions are multi-view by nature, but FPF cannot let "view" absorb every architecture claim. A structure kind and a viewpoint are different. A structure kind says what kind of selected structure is being described; a viewpoint says how an episteme or view is oriented toward a concern. They may be bound, but they are not interchangeable.

The pattern keeps first use light by providing `ArchitectureStructureKindTriage@Project`. If triage identifies the live structure kind and the next admissible architecture move, no full view record is needed. The full record opens when a view changes action, correspondence, publication, source return, source or reliance use, or non-view claim kind.

The TEVB decision is conservative. TEVB remains the small engineering viewpoint bundle over holons. Architecture may import it, but architecture-specific structure kinds and view-record bindings live beside TEVB rather than mutating TEVB.

### C.30.ASV:11 - SoTA-Echoing

| Practice or source line | C.30.ASV adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description discipline | Adopt explicit concern, viewpoint, view, correspondence, and entity-of-interest discipline. | ASV records require architecture claim, `DescriptionContext`, viewpoint, structure kind, correspondence where live, and admissible use. | ISO terminology does not override FPF I/D/S and does not make a view the architecture itself. |
| OMG SysML v2 view-as-query and MBSE traceability practice | Adapt model-view discipline and traceability to FPF D/S views. | Generated, queried, or model-derived views state `viewConstruction`, selected structure, hidden and lost structure, and source-return condition when action relies on the selection. | Tool models and queries do not become source episteme, source or reliance relation, evidence sufficiency, gate passage, or assurance. |
| UAF, ArchiMate, C4, and multi-view architecture practice | Adapt viewpoint-library and lightweight diagram communication pressure. C4 contributes communication and zoom pressure only. | C4/UAF/ArchiMate-like diagrams can publish ASV records only when D/S content, described entity, structure refs, structure kind, viewpoint, and publication relation are explicit. | Do not import their layer, viewpoint, enterprise taxonomies, structure-kind adequacy, evidence sufficiency, or architecture decision claim without a recoverable C.30/C.30.ASV source view. |
| Systems security engineering, secure-by-design, SSDF, and CSF-style practice | Adopt security as architecture-side structure when trust boundaries, authority, untrusted input, secure defaults, hardening, update channels, and detection/response boundaries change action. | Use `SecurityTrustBoundaryStructure` before evidence, assurance, gate, risk score, or compliance proof. | A security framework, checklist, risk color, or control catalog is not security architecture adequacy, evidence sufficiency, assurance, or gate passage by itself. |
| Theory of Code Space / arXiv:2603.00601 and related code-agent architecture relation-graph probing | Adopt partial-observability, typed relation discovery, invariant discovery, uncertainty reporting, and externalized architecture relation graphs as ASV practice basis. | Treat an externalized code-agent relation graph as a diagnostic architecture-description or ASV publication only with observed/inferred/unknown status, evidence pointers, unexplored regions, typed relation semantics, and source-return conditions. | Do not mint `U.CodeSpace`; do not treat probe JSON, cognitive-model publication, dependency-F1 result, or diagnostic relation graph as architecture adequacy, internal belief proof, agent authority, safe-code-change authority, assurance, or release authority. |
| GonzoML neural-network architecture discussions | Adopt practitioner operation language for architecture views: block substitution, relation retargeting, dataflow changes, memory/cache placement, path-selection/gating, MoE expert-selection, pruning, distillation, NAS, ablation, and compute/memory/latency tradeoffs. | Use those phrases as recognition cues for changed structure kind, flow relation, module/interface claim kind, security/trust boundary, data-custody relation, preserved/lost structure, affected characteristic, source relation, and decision/evidence governing pattern. | Neural-network labels, benchmarks, ablations, pruning masks, block/layer/router/cache/state labels, or search outputs do not become FPF ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### C.30.ASV:12 - Relations

Builds on: `C.30.P`, `C.30`, `A.22`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `A.7`, `E.10.D2`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `A.6.F`, `C.30.TGA-FLOW-REL`, `C.30.LCA`, `C.30.ILC`, `E.18`, `C.29`, `C.16`, `C.25`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, the exact module/interface repair pattern when the module/interface claim kind is live, and named receiving patterns for architecture decision and candidate-set claims.

Does not replace: C.30 architecture-description adequacy, A.22 structure carrier, E.TGA graph/path/crossing discipline, C.29 mathematical-lens adequacy, C.16 characterization, C.25 Q-Bundles, C.28 causal-use support, A.10/G.6 evidence, B.3 assurance, A.20/A.21 gate/release records, A.15 work, C.11 decisions, or E.17 publication.

### C.30.ASV:End

