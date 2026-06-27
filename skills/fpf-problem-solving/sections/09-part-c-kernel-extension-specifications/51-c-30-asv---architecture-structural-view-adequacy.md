## C.30.ASV - Architecture Structural View Adequacy (ASV)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.ASV:1 - Problem frame

Use this pattern when an architecture discussion needs a view over selected architecture-relevant `U.Structure` refs in an `ArchitectureOf@Context` claim.

The first useful move is `ArchitectureStructureKindTriage@Project`: name the architecture claim or pre-claim described holon and bounded context, the smallest useful `ArchitectureStructureKindRef` set, the selected structure or structure-kind under consideration, and the next admissible architecture move.

```text
ArchitectureStructureKindTriage@Project:
  architectureClaimRef?:
  describedHolonRef?:
  boundedContextRef?:
  candidateStructureKindRefs:
  smallestUsefulStructureKindRefs:
  primaryGoverningPatternApplicationRef:
  admissibleArchitectureMove:
  stopCondition:
```

`@Project` guard: in this triage name, `@Project` marks a project-side use card for first-pass architecture-structure triage. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

Start with `C.30` when the architecture claim itself is unclear. Use C.30.ASV only when a structural view over selected architecture-relevant structure changes the next architecture use. Use a full `ArchitectureStructuralView@Context` only when the view changes action, selected reliance relation, correspondence, source return, publication, comparison, or another governing-pattern use.

What goes wrong if C.30.ASV is missed: one favored diagram, module view, TEVB viewpoint, generated relation graph, control sketch, or neural-network block diagram is treated as the architecture view or proof without naming the selected structure kind, hidden or lost structure, correspondence, and next architecture use.

What C.30.ASV buys in practice: the practitioner can bind selected structure kind to view record, viewpoint, construction mode, selected relations, hidden or lost structure, correspondence, source-return condition, and admissible use before relying on that view.

Not this pattern when the question under repair is only the general architecture claim, structure as such, selected transformation-flow relation, mathematical graph description, transformation-flow path relation, or crossing relation. Use `C.30`, `A.22`, `E.18`, `E.18.2`, `C.29`, or `C.30.TFS-REL` as appropriate. If the view is used for another claim being made, use the governing pattern and keep C.30.ASV only to the view portion.

Thin precision-restoration pointer: if the issue under repair is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural view, an architecture description, a publication face, a publication form, a source relation, or another governed claim or relation named by value, use `C.30.P` first. Do not copy the `C.30.P` trigger table here; apply C.30.ASV only after the architecture structural-view claim or non-ASV claim named by value is recoverable.

### C.30.ASV:2 - Problem

An architecture structural view is selected-structure triage for an `ArchitectureOf@Context` claim: which architecture-relevant structure is being viewed, which structure kind is under consideration, what relation, constraint, invariant, operation, dynamics description, hidden or lost structure, correspondence, source or reliance relation, and source-return condition changes the next architecture move. The view is represented as a Description episteme, including an episteme-lane `U.View` when the view claim is being made, only to record that selected-structure move. Publication faces, forms, units, and renderings may publish the view; they are not the view and do not become the selected structure.

Without this pattern:

- a module-interface view is treated as all architecture;
- a selected transformation-flow structure, mathematical graph description, or control diagram is treated as proof;
- a structure kind is treated as a `U.Viewpoint`;
- a TEVB viewpoint bundle is mutated to carry architecture-specific structure kinds;
- a diagram, table, dashboard, generated relation graph, or ADR is treated as the view itself;
- functional architecture is treated as a peer ontology rather than a structure-kind interpretation under C.30;
- cross-view consistency is asserted by prose instead of correspondence records;
- omitted structure is relied on in subsequent work without a source-return condition.

### C.30.ASV:3 - Forces

| Force | Tension |
| --- | --- |
| View usefulness vs view overread | Views make architecture discussable, but a useful publication form or source material can be mistaken for the architecture claim, selected structure, publication, proof, or decision. |
| Structure kind vs viewpoint | A structure kind classifies selected structure; a viewpoint names a way of viewing. They often appear together but are not the same kind. |
| TEVB reuse vs TEVB mutation | TEVB gives useful engineering viewpoints over holons; architecture needs more structure kinds without expanding the TEVB core by implication. |
| Small triage vs full view record | Many cases need only the structure kind under consideration and next architecture use; full view records are justified only when they change action. |
| Multi-view correspondence vs single-view shortcut | Architecture work often needs relations among functional, flow, control, module, information, work, evidence, scale, and placement views; one favored diagram cannot carry all claims. |
| Hidden structure vs practical compression | A useful view omits something; omitted structure becomes a problem only when subsequent action relies on it. |

### C.30.ASV:4 - Solution

Govern architecture structural views by first naming the selected architecture-relevant structure, structure kind, view construction, correspondence, hidden or lost structure, source or reliance relation, source-return condition, admissible use, and next architecture move. Use `ArchitectureStructuralView@Context` as the record form when that view must be durable, reusable, comparable, or reliance-bearing.

A conforming `ArchitectureStructuralView@Context` record is a Description or view over selected `U.Structure` references in one `ArchitectureOf@Context` claim record, under one declared `ArchitectureStructureKindRef` and one `DescriptionContext.ViewpointRef`. The description and view machinery makes the selected-structure move inspectable; it does not replace that move.

C.30.ASV is the selected-structure-kind-to-view relation pattern for architecture work. It explains how different selected structure kinds become views under declared viewpoints and concerns. It is not a complete architecture-description pattern; a durable `ArchitectureDescription@Context` composes one or more structural-view records through C.30 and E.17.0 only when description use is being made.

C.30.ASV does not extend the TEVB core viewpoint set by implication. It defines architecture structure kinds and architecture-specific structure-kind and view-record bindings. TEVB viewpoints are reused when the structure-kind view uses one of the TEVB core viewpoints; other structure-kind views use `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, a governing FPF pattern, or a source or reliance record.

#### C.30.ASV:4.1 - Architecture structural view record
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

```text
ArchitectureStructuralView@Context ::= {
  viewId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    EntityOfConcernRef = selectedStructureEntityOfConcernRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedStructureEntityOfConcernRef: U.StructureRef | FinSet(U.StructureRef) (= structureRefs),
  viewpointRef: U.ViewpointRef (= descriptionContext.ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
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
  structureKnowledgeState?:
    declared | observed | inferred | generated | simulated |
    extracted | hypothesized | unknownRegionPresent,
  correspondenceModelRefs?,
  sourceOrRelianceRelationRefs?,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

`DescriptionContext.EntityOfConcernRef` names the selected structure or selected structure set represented by `structureRefs`. `architectureClaimRef` names the enclosing `ArchitectureOf@Context` claim, and the described holon and bounded context are recovered through that claim record.

**EntityOfConcern discipline.** C.30.ASV treats selected structure as the EntityOfConcern for this view use when the view concerns dependent, non-agentive organization rather than one publication form or source material. This does not add a parallel EntityOfConcern head: `DescriptionContext.EntityOfConcernRef`, `selectedStructureEntityOfConcernRef`, and `structureRefs` must converge on the same selected structure or structure set, while `architectureClaimRef` remains the enclosing architecture-claim context.
`viewpointRef` is a recovery label for `descriptionContext.ViewpointRef`, not a second independent viewpoint slot. If the implementation stores only `DescriptionContext`, the viewpoint remains recoverable there.

`structureKnowledgeState?` states how the selected structure is known when partial knowledge matters: declared, observed, inferred, generated, simulated, extracted, hypothesized, or with an unknown region present. Unknown or inferred structure may guide inspection or source return; it cannot by itself supply assurance, gate, release, causal proof, or architecture decision.

#### C.30.ASV:4.2 - Architecture structure-kind classifier

`ArchitectureStructureKindRef` is a C.30-local `DiscriminatorToken` enumeration over architecture-relevant `U.Structure` references selected by `ArchitectureOf@Context`. It is not `U.Kind`, `U.Viewpoint`, `U.ViewpointBundle`, `StructuralAspectDescription`, `StructuralView@Context`, or a root `U.*` kind. `ArchitectureStructuralView@Context` uses `structureKindRef` to say which selected structure kind is being viewed.

```text
ArchitectureStructureKindRef ::= one of {
  FunctionalStructure,
  TransformationFlowStructure,
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
  AllocationResponsibilityStructure,
  EvidenceAssuranceStructure,
  ScaleEvolutionStructure,
  OtherDeclaredStructureKind
}
```

The first group is the seed classifier set for ordinary architecture structural-view use. `SecurityTrustBoundaryStructure`, `WorkMethodStructure`, `AllocationResponsibilityStructure`, `EvidenceAssuranceStructure`, and `ScaleEvolutionStructure` are classifier values over selected `U.Structure` references, not new root kinds. ASV may use them to name the selected architecture-relevant structure, but their full semantics stay in the named security, work and method, allocation-responsibility, evidence and assurance, scale, characterization, or mathematical-lens patterns.
Do not enumerate structure kinds by default. Choose the smallest useful structure-kind set that changes the next architecture move. If no structure kind changes action, keep the phrase as ordinary recognition wording or a source note. This does not weaken kind discipline; it prevents `ArchitectureStructureKindRef` from becoming an audit checklist.

Inside C.30.ASV, `OtherDeclaredStructureKind` is always an architecture-structure-kind classifier value over `U.Structure`; it does not mint a general FPF root kind.

`OtherDeclaredStructureKind` is admissible only when the local text names:

- `declaredStructureKindName`;
- `declaredStructureKindDefinition`;
- allowed relation families;
- locally triggered overreads;
- governing-pattern applications;
- `boundedContextRef`.

Each structure kind needs a short definition, allowed relation families, locally triggered overreads, typical governing-pattern applications, and example architecture structural view records. This is not a new root-kind set; it is a controlled classifier set over `U.Structure`.

#### C.30.ASV:4.3 - Small triage output

Use `ArchitectureStructureKindTriage@Project` before a full view record when the practitioner only needs to identify the structure kind under consideration and next architecture move.

```text
ArchitectureStructureKindTriage@Project ::= {
  architectureClaimRef?: ArchitectureOf@ContextRef,
  describedHolonRef?: U.HolonRef,
  boundedContextRef?: U.BoundedContextRef,
  architectureConcernCue?,
  sourceMaterialRef?,
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  smallestUsefulStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  selectedStructureRefs?,
  hiddenOrLostStructureCueRefs?,
  primaryGoverningPatternApplicationRef?,
  admissibleArchitectureMove:
    inspect | split | relate | downgrade | assignGoverningPattern | stop |
    otherDeclared,
  governingPatternApplicationRefs?,
  nonAdmissibleOverread?,
  stopCondition
}
```

`architectureConcernCue?` and `sourceMaterialRef?` are recognition and source-reference positions; they do not create `ArchitectureStructureKindRef` values. `primaryGoverningPatternApplicationRef?` names the one direct governing pattern that carries the next non-ASV claim kind when such a claim is current. `nonAdmissibleOverread?` names only the overread that would change this triage. Candidate generation, evidence, assurance, gate, publication, decision, or work claims are named through `governingPatternApplicationRefs?` and stay with their governing patterns rather than becoming ASV fields.

When `architectureClaimRef` is absent, `describedHolonRef` and `boundedContextRef` are required for triage. This pre-claim form does not create a new kind and does not publish an `ArchitectureOf@Context` claim by itself; it only lets the practitioner identify the structure kind under consideration before forming a full architecture claim. A full `ArchitectureStructuralView@Context` still requires `architectureClaimRef`; do not promote triage to a full view record until that architecture claim is available.
Practitioner prompt labels are first-entry cues, not `ArchitectureStructureKindRef` values. FPF-governed records use the Tech values below:

```text
Functional -> FunctionalStructure
Flow -> TransformationFlowStructure
Control -> ControlStructure
Module -> ModuleInterfaceStructure
Method and work -> WorkMethodStructure
Role -> AllocationResponsibilityStructure
Evidence -> EvidenceAssuranceStructure
Scale -> ScaleEvolutionStructure
Security -> SecurityTrustBoundaryStructure

```

#### C.30.ASV:4.3a - Evolutionary-engineering candidate structural view

Use this view when a retained variant, front member, selected set, or architecture-candidate palette needs structural-view triage. The ASV claim is not "this archive is architecture"; it is "this candidate makes a selected structure or structure kind current for an `ArchitectureOf@Context` claim."

```text
ArchitectureCandidateStructuralView@Context:
  CandidateSetOrArchiveRef:
  CandidateRef:
  ArchitectureOfRef:
  SelectedStructureOrStructureKindRef:
  StructuralViewRef:
  AffectedCharacteristicRef:
  CorrespondenceOrLossRef?:
  NextGoverningPatternRef:
```

If the candidate cannot name a selected structure or structure kind, keep it in `C.18`, `C.19`, or `G.5`. If the view only publishes, compares, or explains the candidate, use `C.30.AD`, the comparison pattern, or the publication-use pattern named by value. ASV admits the candidate only for selected-structure triage.

#### C.30.ASV:4.4 - Architecture viewpoint bundle and binding rows



Architecture structural views use `VF.ARCH.STRUCTURE` without turning structure kinds into viewpoints. The bundle is separate from `VF.TEVB.ENG`: it may import TEVB, but it does not expand the TEVB core engineering viewpoint set.

Declaration source: `VF.ARCH.STRUCTURE` is an `E.17.1` and `F.18` declared viewpoint bundle for architecture structural-view records. Its `VP.Architecture*` ids are viewpoint ids only. They do not add TEVB viewpoints, name structure kinds, define publication faces, or carry decision, evidence, gate, or assurance authority.

#### C.30.ASV:4.4a - Structural-view publication-use boundary

This subsection is the C.30.ASV structural-view publication-use boundary. C.30.ASV governs architecture structural-view adequacy: selected architecture-relevant structure, structure kind, view construction, correspondence, hidden structure and lost structure, source return, and next architecture move. When a view, diagram, graph, card, benchmark, probe output, model publication, or architecture note is used for evidence sufficiency, safety assurance, gate passage, release permission, work record, or decision authority, apply the pattern governing that claim; keep only the structural-view record and the next architecture move in C.30.ASV.

```text
VF.TEVB.ENG core stays:
  { VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface }
```

TEVB is the small engineering viewpoint bundle over holons. The architecture problem is broader than TEVB, but the broader coverage is not solved by placing record sets inside a `U.ViewpointBundle`. The `U.ViewpointBundle` carries viewpoints; a separate architecture-local description binds structure kinds, view record sets, construction modes, correspondence requirements, and governing-pattern applications.

```text
VF.ARCH.STRUCTURE : U.ViewpointBundle {
  viewFamilyId = VF.ARCH.STRUCTURE,
  imports = { VF.TEVB.ENG },
  EntityOfConcernClassSpec = {
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

`viewRecordSetRef` names the allowed Description-episteme or specification-use record set for one structure-kind binding. It is not a package grouping, not a `U.ViewpointBundle`, not a `ViewFamilyId`, and not a new TEVB viewpoint.

#### C.30.ASV:4.5 - Initial architecture structure kinds and view records

The initial set is a seed for first architecture moves, not an atlas. Use the table to choose one structure kind under consideration and the governing-pattern application that carries any non-ASV claim kind.

| Seed structure kind | Structural view | Minimum record fields beyond common ASV fields | First boundary |
| --- | --- | --- | --- |
| `FunctionalStructure` | `FunctionalStructureView@Context` | `functionalBehaviorRefs`, `functionalElementRefs?`, `transformerSideFillerRefs?`, `candidateBearerRefs?`, input-condition refs, output-condition refs, functional-port refs, capability refs, dependency refs, allocation refs, correspondence refs | Use `A.6.F`, `A.3.4`, capability, work, module-allocation, or requirement patterns when those claims are being made. |
| `TransformationFlowStructure` | `TransformationFlowStructureView@Context` | `transformationFlowStructureRef`, `pathSliceRefs`, `crossingRefs`, `valuationRefs`, `mathematicalDescriptionRefs?` | Use `E.18` and `C.30.TFS-REL` for selected transformation-flow structure, transformation-flow path, or crossing input; use `E.18.2` and `C.29` for mathematical graph descriptions; use `C.28` for causal claims. |
| `RuntimeInteractionStructure` | `RuntimeInteractionStructureView@Context` | runtime elements, connectors and protocols, event topology and message topology, failure boundaries and latency boundaries | Use temporal, failure, evidence, or assurance patterns when runtime claims exceed structure. |
| `ModuleInterfaceStructure` | `ModuleInterfaceStructureView@Context` | module relation refs, interface specs, admissibility conditions, substitutability policy or change policy | Use `A.6.M` module-relation repair and conformance evidence when those claims are being made. |
| PlacementDeploymentStructure | PlacementDeploymentStructureView@Context | allocation-to-site refs or environment refs, network locality or physical locality, jurisdiction constraints or safety constraints | Use temporal, evidence, law-domain, regulatory, or safety patterns when claims of those non-placement kinds are being made. |
| `InformationDataStructure` | `InformationDataStructureView@Context` | state bearer and residence refs, schema refs, semantic refs, persistence locus, provenance relation, custody relation, source-return conditions, privacy constraints | Use evidence, privacy, or source-return patterns when those claims are being made. |
| `SecurityTrustBoundaryStructure` | `SecurityTrustBoundaryStructureView@Context` | protected asset or effect refs, trust boundary refs, untrusted input refs, privilege or authority refs, data-flow and control-flow refs, attack exposure refs, abuse or misuse path refs, secure-default or hardening boundary, supply-chain or update-channel refs, detection-response boundary refs when the corresponding claim is being made | Gives a first security-architecture move before evidence, assurance, gate, risk-score, or compliance proof. |
| `ControlStructure` | `ControlStructureView@Context` | control role refs, declared control-rate refs, observer, estimator, controller, planner, and supervisor relations, feedback refs | Use `C.30.LCA`, dynamics, temporal, causal, evidence, and assurance patterns when those claims are being made. |
| `ConstraintRequirementStructure` | `ConstraintRequirementStructureView@Context` | requirement refs, constraint refs, and invariant refs, affected structure refs, admissibility conditions | Requirements shape structures; requirement, gate, evidence, causal, or decision claims apply their governing patterns. |
| `MaterialSpatialStructure` | `MaterialSpatialStructureView@Context` | geometry, adjacency, containment, energy flow or material flow, safety separation | Physical separation is not safety proof; safety, evidence, dynamics, or causal claims apply their governing patterns. |
| `DeclaredLogicalStructure` | `LogicalStructureView@Context` | local logical relation class, relation constraints, correspondence to functional structures, module structures, runtime structures, and data structures | Covers `logical architecture` without making `logical` a universal ontology token. |

Externally governed classifier values remain admissible when they are the architecture-relevant structure under consideration, but C.30.ASV does not define their full record families:

| Externally governed classifier value | ASV use | Full semantics and governing patterns |
| --- | --- | --- |
| `WorkMethodStructure` | Method arrangement or work arrangement changes the architecture move. | Use `MethodDescription`, `WorkPlan`, `WorkEnactment`, exception-handling relation, launch relation or gate relation, and `A.15` governing patterns; do not turn a work-method diagram into work authority. |
| `AllocationResponsibilityStructure` | Responsibility or enactor allocation changes the architecture move. | Use role, enactor, organization, work, and stakeholder patterns when those claim kinds are being made; do not treat an org chart as architecture truth. |
| `EvidenceAssuranceStructure` | Evidence reuse or assurance arrangement changes affected structure or source return. | Use `A.10`, `G.6`, or `B.3` for evidence sufficiency or assurance verdict; ASV only names the structure and loss boundary. |
| `ScaleEvolutionStructure` | Scale window, replacement or change policy, trajectory reference, or coarse-graining changes the architecture move. | Use `C.29`, `C.16`, temporal, source-return, or decision patterns for scale, characterization, or selection claims. |
| `OtherDeclaredStructureKind` | A local structure kind is declared because none of the seed or externally governed values fits. | Name definition, relation families, false interpretations, governing patterns, and context; do not mint a root kind by label alone. |

Minimum useful seed examples:

| Structure kind | Minimal example | False interpretation | First governing pattern |
| --- | --- | --- | --- |
| `FunctionalStructure` | Capability, effect, or transformation allocation. | Purpose truth or requirement satisfaction. | `A.6.F`, capability, work, or requirement pattern when that claim kind is being made. |
| `TransformationFlowStructure` | Transformation-flow path, crossing, valuation, or selected transformation slice. | Whole architecture or causal proof. | `E.18`, `C.30.TFS-REL`, `E.18.2`, C.29, or C.28 when selected structure, graph description, transformation-flow path, crossing, mathematical-lens, or causal-use claim kind is being made. |
| `ControlStructure` | Controller, observer, plant, feedback, or rate relation. | Stability, safety, or assurance proof. | `C.30.LCA`, temporal, dynamics, causal, evidence, or assurance pattern when that claim kind is being made. |
| `ModuleInterfaceStructure` | Module relation, interface spec, or substitutability boundary. | Module tree as all architecture. | `A.6.M` module-relation repair, conformance evidence, or decision pattern when that claim kind is being made. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody. | Database label. | Evidence, privacy, or source-return pattern when that claim or reliance use is being made. |
| `SecurityTrustBoundaryStructure` | Trust boundary, untrusted input, privilege path, or attack exposure. | Security proof, risk score, or compliance label. | Evidence, assurance, gate, `C.24` agentic tool-use relation or call-planning relation, C.16, C.25, or C.30.LCA when that security, evidence, assurance, gate, tool-use, measurement, quality, or control claim kind is being made. |
| `MaterialSpatialStructure` | Separation, adjacency, containment, or energy path or material path. | Safety proof or geometry as architecture truth. | Safety, evidence, dynamics, or causal pattern when that claim kind is being made. |
| `DeclaredLogicalStructure` | Local logical relation class with correspondence to other structures. | Universal logical architecture ontology. | Correspondence, function, module, runtime, data, or governing pattern when that relation is being claimed or a claim of that kind is being made. |
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
    C.16 | C.25 | C.24 agentic tool-use relation or call-planning relation when tool authority is being claimed | C.30.LCA when a control relation is being claimed
  admissibleUse:
  otherClaimBoundary:
    compliance, risk-score, assurance, checklist-security, and zero-trust claims apply the evidence, assurance, risk, gate, or security pattern governing the claim being made
}
```

`SecurityTrustBoundaryStructure` carries adversarial-boundary interpretation: which protected assets or effects are under consideration, who or what is trusted, where untrusted input crosses, what authority or privilege is exposed, which adversarial paths and attack exposures matter, which data-flow or control-flow security boundaries matter, and where secure defaults, hardening, update or supply-chain channels, detection, or response boundaries change the next architecture move.

Apply evidence, assurance, gate, or compliance patterns only when the architecture move relies on evidence sufficiency, assurance verdict, gate passage, regulatory acceptance, or release authority. If the selected move is structural, first recover the structure: trust boundary, loss-control relation, control relation, evidence reuse structure, or affected structure or affected view.

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
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 or A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

#### C.30.ASV:4.6 - Functional structure view boundary

`FunctionalStructureView@Context` under C.30.ASV does not mint `U.Function`. It may publish `FunctionalElement@Context` as a view-local functional-structure record when the view selects a bounded context, a functional behavior, and a bearer or candidate-bearer locus. The functional element is not identical with the behavior: the behavior is grounded as `U.Transformation` for one bounded required change or required effect, or as `TransformationFlowStructure` for compound behavior, while the functional element is the view-local record that binds that behavior to bearer, capability, ports, and allocation claims when those claims are current.

Identity for `FunctionalElement@Context` is:

- selected `FunctionalStructureView@Context`;
- bounded context;
- functional behavior reference: `U.Transformation` or `TransformationFlowStructure`;
- bearer or candidate-bearer locus: normally `U.System` or candidate system bearing `TransformerRole@Context`, or an explicit not-yet-allocated gap.

If no bearer or candidate allocation is current, do not claim a full functional element. Record a required transformation gap, required effect gap, capability gap, functional behavior slot, or candidate allocation question. This preserves the practical architecture move without pretending that a module, component, diagram row, or function word has already supplied the bearer.

```text
FunctionalStructureView@Context ::= {
  architectureStructuralViewRef: ArchitectureStructuralView@ContextRef,
  functionalElementRefs?: FunctionalElement@Context refs,
  sourceFunctionWordingRefs?,
  functionalBehaviorRefs?: U.Transformation refs; TransformationFlowStructure refs,
  transformerSideFillerRefs?: U.System bearing TransformerRole@Context,
  candidateBearerRefs?: candidate system refs; explicit gap refs,
  capabilityRefs?,
  inputConditionRefs?,
  outputConditionRefs?,
  functionalPortRefs?,
  functionalDependencyRefs?,
  allocationRefs?,
  correspondenceRefs?,
  nonFunctionClaimNotes?,
  flowRelationRefs?,
  moduleInterfaceRelationRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

A selected transformation-flow structure, mathematical graph description, transformation-flow path slice, crossing, or flow valuation is not a functional element by default. When a transformation-flow relation is being used, connect the functional view to `TransformationFlowStructure` through `C.30.TFS-REL`. When a mathematical graph description is being used, connect it through `E.18.2`; when math-lens use is being claimed, connect it through `C.29`. When module allocation is being claimed, connect the functional view to `A.6.M` module-relation repair rather than treating function and module as one kind. Functional ports and module interfaces can both use `U.Signature` discipline, but functional ports govern behavior input and output slots while module interfaces govern substitution, compatibility, boundary, and change-policy claims.

Composability and quality compositionality are separate claims. If the view says parts can be assembled, keep that as a structure claim or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim.

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationOrRecordKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredRelationOrRecordKind: QBundleSlot | structuralCharacteristicQBundleInputSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidenceRelationForQBundleSlot(A.10-governed evidence relation only when evidence provenance is the claim being made)
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures and view relations and model relations. They do not make safety, latency, reliability, or another quality propagate automatically.

#### C.30.ASV:4.7 - Correspondence and source return

Use correspondence records when the view relates functional, flow, control, module-interface, information, runtime, placement, work, evidence, scale, or logical structures. Do not assert cross-view consistency by prose alone.

Correspondence examples:

| Source wording | Recover |
| --- | --- |
| "This function is implemented by that module." | `FunctionToModuleAllocationRef` or the allocation or relation record named by value. |
| "This flow crosses that runtime boundary." | `FlowToRuntimeInteractionCorrespondence`. |
| "This evidence covers the replacement." | `EvidenceReuseToAffectedStructure`; assign sufficiency or verdict to `A.10`, `G.6`, or `B.3`. |
| "This requirement constrains that structure." | `RequirementToStructureConstraint` or a constraint record named by value. |
| "This scale window changes the structure kind." | `ScaleWindowToStructureKindCorrespondence`; assign scale-lens claims to `C.29` when those claims are being made. |

Use `SourceReturnCondition` when compression, extraction, coarsening, evidence reuse, ML evaluation, bounded exception, many-to-many allocation, publication, or decision claim hides a distinction needed for action, assurance, causal use, law-domain review, regulatory review, comparison, or reopening.

If `viewConstruction` is `query`, `extraction`, `coarsening`, `correspondenceSlice`, or `sourceReturnSlice`, and omitted structure changes action, assurance, causal use, law-domain or regulatory review, or subsequent decision reopening, `SourceReturnCondition` is needed.

When the view is used to name affected structures for a next architecture use but no decision record is being used, use C.30 `AffectedArchitectureStructureNote`: affected structure kinds, affected structure refs when known, affected ASV refs, accepted or suspected view loss, source-return condition, and the next admissible use. The note is not an architecture decision, ADR, gate passage, evidence sufficiency, or release authority.

Use the thinnest source or reliance relation that preserves the next architecture move. Use fuller source, evidence, assurance, or claim-kind relation only when the source or reliance relation being used cannot be inspected, used, compared, refreshed, or bounded without it. A `ControlStructureViewNote` may precede full `C.30.LCA` use or proof-governing pattern applications when one control relation and its boundary are enough for the architecture move being made.

Treat source return as a user action, not only a metadata field:

```text
SourceReturnAction:
  returnTo:
    sourceStructure | sourceEpisteme | sourceView | sourceTrace |
    sourceCorpus | sourceModel | sourceEvidence | sourcePublication
  because:
    hiddenRelation | lostConstraint | coarsenedScale |
    ambiguousExtraction | staleEdition | crossViewMismatch |
    lawDomainOrRegulatoryUse | assuranceOrDecisionUse
  nextSourceReturnAction:
    inspect | split | downgradeUse | addCorrespondence |
    openNeighborPattern | stop
```

Do not make source return mandatory for ordinary local recognition when no hidden distinction is being used for action. Do not omit source return when a hidden distinction carries a selected reliance relation, assurance, law-domain, comparison, causal, gate, or decision commitment. The condition is needed only when the repaired text still relies on the hidden source-side distinction.

Model cards, system cards, and evaluation harness reports may publish or substantiate an architecture structural view only when the structural-view claim is recoverable. The view must name the relevant structure kind, such as `RuntimeInteractionStructure`, `InformationDataStructure`, `SecurityTrustBoundaryStructure`, `EvidenceAssuranceStructure`, `ModuleInterfaceStructure`, or another declared structure kind; it must also state intended-use scope, evaluation scope and known loss when evaluation is used, deployment-context mismatch when that mismatch is being claimed, and the evidence or assurance governing pattern when the publication is used beyond transparency. A card or harness is not architecture adequacy, safety proof, or release claim or gate claim by publication alone.

#### C.30.ASV:4.8 - Worked slices

**Runtime degradation.** A team says, "The architecture is fine, but incidents happen when failover starts." The first architecture move is to recover runtime interaction, control relation, failover relation, placement, and evidence-assurance structures before turning a dashboard or deployment diagram into proof:

```text
Runtime degradation slice:
  selected structure kinds:
    RuntimeInteractionStructure
    ControlStructure
    InformationDataStructure
    PlacementDeploymentStructure
    EvidenceAssuranceStructure
  first architecture move:
    recover runtime interaction topology, control relation or failover relation,
    state custody, placement relation, locality relation, evidence relation, and observability relation
  nonAdmissibleUse:
    deployment diagram as runtime proof,
    observability dashboard as evidence sufficiency,
    green indicator value as gate authority or release authority
```

Use `C.24` only when tool-use, call planning, call graph, work execution, or budgeted agentic tool-use is the claim being made. Do not absorb those claims into architecture structure.

**CPS or plant architecture.** A plant drawing, P&ID-like publication form, LCA sketch, or safety-case view is not the plant architecture by itself. First recovery can require:

```text
CPS and plant architecture first recovery:
  MaterialSpatialStructure:
    physical separation, adjacency, energy path or material path
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

**Chiplet or device architecture.** A packaging diagram or interconnect sketch may involve several structure kinds:

```text
Chiplet and device architecture first recovery:
  MaterialSpatialStructure:
    packaging, adjacency, thermal path, energy path
  TransformationFlowStructure:
    interconnect topology, data flow path, energy flow path, or signal flow path
  ModuleInterfaceStructure:
    interface specification, protocol, conformance boundary
  PlacementDeploymentStructure:
    physical locality, substrate, host environment
first architecture move:
  separate interconnect topology, packaging path, thermal path, or energy path,
  interface specification, and evidence boundary and conformance boundary
correspondenceOrLossLine:
  record the preserved relation among interconnect, physical package,
  interface, and placement, plus any benchmark or packaging-view loss
stop condition:
  no packaging diagram or benchmark becomes performance, safety,
  evidence, or gate proof by appearance
```

**Organization or operating-model architecture.** An org chart or work-method diagram can be architecture-relevant only after the work, role, information, and evidence records are separated:

```text
Organization and operating-model architecture first recovery:
  AllocationResponsibilityStructure:
    responsibility allocation and enactment boundary
  WorkMethodStructure:
    repeatable work method and exception-handling relation
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

**Evidence reuse across product variants.** A certification or test package reused across module variants may be architecture-relevant as an evidence-and-assurance structure view, but it is not an assurance verdict:

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
    A.10, G.6, or B.3 for evidence sufficiency or assurance verdict
  nonAdmissibleUse:
    evidence-structure view as assurance verdict
```

**Organization service architecture.** A service organization sketch that shows teams, handoffs, escalation points, and dashboards is not the organization architecture by itself. First recovery can require:

```text
Organization service architecture first recovery:
  describedHolonRef: service organization or service-delivery system
  candidateStructureKindRefs:
    WorkMethodStructure:
      method arrangement, work-plan boundaries, exception handling, and performed-work records
    AllocationResponsibilityStructure:
      role assignments, responsibility split, enactor availability, and escalation relation
    InformationDataStructure:
      ticket state, customer record custody, dashboard source, and source-return condition
    EvidenceAssuranceStructure:
      audit trail, service-level evidence relation, assurance claim, and gate or release record only when those claims are being made
  C30ASVBoundary:
    ASV names selected structure and view boundary; staffing decision, work authority, evidence sufficiency, assurance, and service-quality claims go to their governing patterns
```

**AI agent diagram.** A "planner-memory-tools" diagram is not the agent's architecture by itself. It may start first recovery as a structure-kind set, without minting an AI-domain ontology:

```text
AI-agent architecture first recovery:
  RuntimeInteractionStructure:
    model-tool-memory-planner-evaluator-human topology
  InformationDataStructure:
    memory scopes, data custody, provenance, retention,
    context-window relation and source-return relation
  SecurityTrustBoundaryStructure:
    untrusted content channels, prompt-injection or instruction boundary,
    tool authority, secret-bearing contexts, memory custody crossing and data custody crossing,
    output handling, supply-chain or update channel
  ModuleInterfaceStructure:
    tool specs, API specs, and interface specs and substitutability limits
  EvidenceAssuranceStructure:
    eval harness, human approval, evidence decay, incident feedback
admissibleArchitectureMove:
  split runtime interaction, information, security boundary, module-interface, and evidence-assurance claims before relying on the diagram
correspondenceOrLossLine:
  record the preserved relation among runtime topology, information custody,
  security boundary, module-interface, and evidence-assurance structures,
  plus any diagram or evaluation-harness loss
governingPatternApplicationRefs:
  C.30.TFS-REL when an E.18 flow relation is being used,
  A.6.M module-relation repair for tool, API, or interface relation claims,
  A.10, G.6, or B.3 when evidence or assurance reliance is being claimed,
  C.24 agentic tool-use relation or call-planning relation, E.16, A.20, or A.21 when tool-call, autonomy, constraint, or gate authority is being claimed
stop condition:
  ASV contains only the structural-view record; evidence sufficiency, assurance, gate, autonomy, and tool-call authority claims are assigned to the governing patterns for those claims
```

Structural AI-agent security is architecture structure when these structure kinds change the next architecture move. When the claim being made is latent representation, decoding, or effect adequacy rather than architecture structure, keep the phrase as a reduced-use source cue until the representation, decode, or effect-adequacy pattern governing that claim carries that claim.

**Generated code-agent relation graph.** A probe JSON or code-agent architecture relation graph can be an architecture structural view publication only after observed, inferred, or unknown observation value, evidence pointers or source pointers, unexplored regions, typed relation semantics, and source-return conditions are present. Belief-state proof and downstream-change safety assurance apply the patterns governing those claims.

**Neural-network block replacement.** Replacing attention, FFN, convolution, SSM, recurrent, memory block or cache block, MoE expert-selection, pruning, distillation, or another block is an architecture move only when the changed structure kind, flow relation, module-interface claim kind, preserved and lost structure, affected characteristic, source relation, and decision or evidence governing pattern are named.

### C.30.ASV:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner looks at an architecture "view" and asks whether it is functional, flow, control, module-interface, information or data, placement, scale, work, evidence, or declared logical structure. C.30.ASV turns that question into structure-kind triage or a full structural view record. |
| Show: `U.System` | A plant, vehicle, software system, product platform, AI-agent system, or neural-network model can require several structural views over the same architecture claim. One module view does not exhaust the system architecture, and one flow graph does not prove work, evidence, safety, or release. |
| Show: `U.Episteme` | A diagram, model, generated relation graph, ADR, dashboard, SysML view, or C4 diagram is an episteme, view, or publication face. It can publish an architecture structural view only when the architecture claim, structure refs, structure kind, viewpoint, hidden structure and lost structure, correspondence, source or reliance relation, and admissible use are recoverable. |

### C.30.ASV:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture structural-view claims over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-view bias | Make module-interface one structure kind, not the default meaning of architecture. |
| Viewpoint-kind conflation | Keep structure kind, viewpoint, view record, and viewpoint bundle separate. |
| TEVB mutation bias | Import TEVB where useful; do not expand `VF.TEVB.ENG` by implication. |
| Check-only bias | Every failed conformance check gives a repair action or governing-pattern application. |
| Didactic-thinning risk | The pattern starts with triage and action, not taxonomy alone. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### C.30.ASV:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-ASV-1 Structure target.** | Every architecture structural view names `structureRefs` or a recoverable selected-structure reference. | Name the selected structure reference, or downgrade the source material to an architecture question, diagram, note, or publication that does not claim to be a structural view. |
| **CC-ASV-2 Structure kind.** | Every architecture structural view names `structureKindRef`. | Use `ArchitectureStructureKindTriage@Project`; if no structure kind changes action, keep the text as ordinary prose or a source note. |
| **CC-ASV-3 Same selected architecture claim.** | The view preserves `architectureClaimRef`, `DescriptionContext`, and the claim record's `describedHolonRef` and `boundedContextRef` unless explicit retargeting or a bridge is declared. | Restore the same claim record and bounded context, or add an explicit retargeting or bridge note before using the view. |
| **CC-ASV-4 Viewpoint discipline.** | The view is under `VF.ARCH.STRUCTURE` or another declared architecture-specific bundle, rather than an ad-hoc tag. | Assign the view to `VF.ARCH.STRUCTURE`, a declared local viewpoint bundle, or a governing pattern; otherwise keep the label as Plain recognition wording. |
| **CC-ASV-5 Lost structure.** | The view names hidden or lost structure, especially for query, extraction, coarsening, or publication uses. | Add a one-line hidden-structure note or lost-structure note, or narrow the admissible use so omitted structure is not relied on. |
| **CC-ASV-6 Correspondence.** | Cross-view relations are carried by `correspondenceModelRefs` or correspondence records, not by prose alone. | Add a correspondence note or stop at a single-view statement without cross-view consistency claim. |
| **CC-ASV-7 No publication collapse.** | A diagram, model, table, dashboard, generated relation graph, or ADR is kept as publication form, record, or source relation, not the architecture structural view itself. | Keep the source material as publication form or source relation and name the source episteme or view; do not require a full architecture view unless it changes the next architecture use. |
| **CC-ASV-8 No single-view architecture.** | If a decision uses an architecture view as decision claim, it names the affected structures and views, not only one favored diagram. | Add affected structure and view refs, or narrow the statement to the single view's admissible use. |
| **CC-ASV-9 No proof overread.** | The view does not act as evidence, safety proof, causal proof, gate decision, or work record without a named governing pattern. | Assign the claim being made to `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, or mark the proof, evidence, gate, or assurance use unsupported; do not add more C.30.ASV fields as a substitute. |
| **CC-ASV-10 Relation or correspondence record named by value.** | Every cross-reference names the kind named by value, relation, or record: selected structure, structure kind, viewpoint, correspondence record, allocation record, bridge record, evidence relation, publication relation when a publication claim is being made, interface specification, or governing record named by value. | Replace the ambiguous reference with the kind, relation, or record that actually carries the claim, or split the sentence into separate records. |
| **CC-ASV-11 Source return.** | When compression, extraction, coarsening, evidence reuse, publication, or many-to-many allocation hides distinctions, `SourceReturnCondition` is present. | Add one source-return trigger, or narrow the view's admissible use so omitted distinctions are not used for action, assurance, causal use, law-domain review, regulatory review, or reopening. |
| **CC-ASV-12 Architecture-name recovery.** | Every `<X>Architecture` phrase recovers `<X>StructureKind` or a declared local relation. | Rewrite the phrase through `ArchitectureStructureKindTriage@Project`; if no relation is being claimed, keep the name as Plain prose and do not let it carry ontology. |
| **CC-ASV-13 Useful action.** | The repair leaves a surviving admissible architecture move: inspect, split, relate, downgrade, assign to a governing pattern, generate candidates, stop, state a structural view, add correspondence, add source return, or apply the governing pattern. | Restore one move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30.ASV:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Module diagram as architecture view** | One module-interface diagram is treated as the whole architecture. | Use structure-kind triage; keep module-interface as one structure kind and add other views only when they change action. |
| **Viewpoint as structure kind** | `VP.Functional`, `VP.ModuleInterface`, or another viewpoint is used as if it were the selected structure kind. | Recover `ArchitectureStructureKindRef` and bind it to a viewpoint through `ArchitectureStructureKindViewRecordBinding` when needed. |
| **Structure kind as viewpoint** | `FunctionalStructure` or `ControlStructure` is added to TEVB as a new viewpoint. | Keep TEVB core unchanged; use `VF.ARCH.STRUCTURE` and binding rows. |
| **Publication-face collapse** | A diagram, model, table, dashboard, generated relation graph, ADR, or C4 view is treated as the ASV record. | Recover source episteme or source view and publication relation; use an ASV record only if the view changes action. |
| **Single-view decision** | A decision uses one architecture view as if it covered all affected structures. | Name affected structures and view refs, or narrow the decision to the single view's admissible use. |
| **Lost-structure silence** | Extracted, generated, coarsened, or compressed views hide distinctions but still justify action. | Add hidden structure and lost structure and source-return condition, or narrow admissible use. |
| **Proof overread** | The structural view is used as evidence sufficiency, safety proof, causal proof, gate decision, or work record. | Assign the claim being made to the governing pattern and keep ASV only to view adequacy. |
| **Risk color as security architecture** | A red, yellow, or green risk cell, risk matrix, maturity score, or compliance color stands in for `SecurityTrustBoundaryStructure` or resource-allocation priority. | Recover protected asset or effect, trust boundary, untrusted input, privilege or authority relation, data flow or control flow, abuse or misuse path, and the evidence named by value, assurance, measurement, causal, gate, selection, or allocation claim kind if that claim is being made; do not treat ordinal risk color as security architecture adequacy, resource-allocation priority, or gate passage. |
| **Taxonomy without action** | The text classifies a view but does not say what changes in practice. | Add `admissibleArchitectureMove` or stop at Plain recognition wording. |

### C.30.ASV:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture views become Description epistemes and specification-use cases over selected structures, not diagrams by appearance. | A conforming use states architecture claim, structure refs, structure kind, viewpoint, and use when the view has FPF-governed use. |
| TEVB remains stable while architecture gets broader structure-kind coverage. | Structure-kind bindings add one explicit record when architecture-specific coverage matters. |
| Functional, flow, control, module-interface, placement, information, runtime, work, evidence, scale, material, and logical structures can be separated. | Some familiar names require triage before they can carry FPF claim kinds. |
| Failed checks produce repair actions rather than only classification objections. | The checklist is longer than a pure taxonomy, but it is more useful for action. |

### C.30.ASV:10 - Rationale

C.30.ASV exists because architecture descriptions are multi-view by nature, but FPF cannot let "view" absorb every architecture claim. A structure kind and a viewpoint are different. A structure kind says what kind of selected structure is being described; a viewpoint says how an episteme or view is oriented toward a concern. They may be bound, but they are not interchangeable.

The pattern keeps first use light by providing `ArchitectureStructureKindTriage@Project`. If triage identifies the structure kind under consideration and the next admissible architecture move, no full view record is needed. The full record is used when a view changes action, correspondence, publication, source return, source or reliance use, or non-view claim kind.

The TEVB decision is conservative. TEVB remains the small engineering viewpoint bundle over holons. Architecture may import it, but architecture-specific structure kinds and view-record bindings are defined beside TEVB rather than mutating TEVB.

### C.30.ASV:11 - SoTA-Echoing

| Practice or source line | C.30.ASV adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description discipline | Adopt explicit concern, viewpoint, view, correspondence, and source-side `EntityOfConcernRef` discipline, mapped here to `DescriptionContext.EntityOfConcernRef`. | ASV records require architecture claim, `DescriptionContext`, viewpoint, structure kind, correspondence when used, and admissible use. | ISO terminology does not override FPF EntityOfConcern and Description-episteme boundary and specification-use and refinement discipline and does not make a view the architecture itself. |
| OMG SysML v2 view-as-query and MBSE traceability practice | Adapt model-view discipline and traceability to FPF Description or views. | Generated, queried, or model-derived views state `viewConstruction`, selected structure, hidden and lost structure, and source-return condition when action relies on the selection. | Tool models and queries do not become source episteme, source or reliance relation, evidence sufficiency, gate passage, or assurance. |
| UAF, ArchiMate, C4, and multi-view architecture practice | Adapt viewpoint-library and lightweight diagram communication pressure. C4 contributes communication and zoom pressure only. | C4-like, UAF-like, and ArchiMate-like diagrams can publish ASV records only when Description-episteme or specification-use content, DescriptionContext EntityOfConcern, structure refs, structure kind, viewpoint, and publication relation are explicit. | Do not import their layer, viewpoint, enterprise taxonomies, structure-kind adequacy, evidence sufficiency, or architecture decision claim without a recoverable C.30 or C.30.ASV source view. |
| Systems security engineering, secure-by-design, SSDF, and CSF-style practice | Adopt security as architecture-side structure when trust boundaries, authority, untrusted input, secure defaults, hardening, update channels, and detection boundaries and response boundaries change action. | Use `SecurityTrustBoundaryStructure` before evidence, assurance, gate, risk score, or compliance proof. | A security framework, checklist, risk color, or control catalog is not security architecture adequacy, evidence sufficiency, assurance, or gate passage by itself. |
| Theory of Code Space, arXiv:2603.00601 and related code-agent architecture relation-graph probing | Adopt partial-observability, typed relation discovery, invariant discovery, uncertainty reporting, and externalized architecture relation graphs as ASV practice source. | Treat an externalized code-agent relation graph as a diagnostic architecture-description or ASV publication only with observed, inferred, or unknown observation value, evidence pointers, unexplored regions, typed relation semantics, and source-return conditions. | Do not mint `U.CodeSpace`; do not treat probe JSON, cognitive-model publication, dependency-F1 result, or diagnostic relation graph as architecture adequacy, internal belief proof, agent authority, safe-code-change authority, assurance, or release authority. |
| GonzoML neural-network architecture discussions | Adopt practitioner operation language for architecture views: block substitution, relation retargeting, dataflow changes, memory placement or cache placement, path-selection or gating, MoE expert-selection, pruning, distillation, NAS, ablation, and compute, memory, or latency tradeoffs. | Use those phrases as recognition cues for changed structure kind, flow relation, module-interface claim kind, security or trust boundary, data-custody relation, preserved and lost structure, affected characteristic, source relation, and decision or evidence governing pattern. | Neural-network labels, benchmarks, ablations, pruning masks, block, layer, router, cache, or state labels, or search outputs do not become FPF ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### C.30.ASV:12 - Relations

Builds on: `C.30.P`, `C.30`, `A.1`, `A.22`, `E.24.PUB`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `A.7`, `E.10.D2`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `E.18`, `C.29`, `C.16`, `C.25`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.32.P2S`, `C.32`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `C.33`, `C.34`, and `C.35` when problem-to-structure carry-through, candidate-set, architecture-decision, ADR-projection, decision-adequacy, capture, preservation, or generated-carrier claim kinds are being made. Use `A.6.M` when the module-interface claim kind is being made.

Other claims stay with their governing patterns: `C.30` for grounded architecture and selected-structure adequacy, `A.1` for the described holon recovered through `ArchitectureOf@Context`, `A.22` for selected-structure EntityOfConcern, `E.24.PUB` for ontic-description and publication-form boundary, `C.33` for captured and lost selected structure in a view, `C.34` for preservation or correspondence between a view and another structure-bearing object, `C.35` for generated or discovered carriers before candidate admission, `E.18` for selected transformation-flow structure, transformation-flow path, and crossing discipline, `E.18.2` and `C.29` for mathematical graph descriptions and mathematical-lens use, `C.16` for characterization, `C.25` for Q-Bundles, `C.28` for causal use, `A.10` and `G.6` for evidence, `B.3` for assurance, `A.20` and `A.21` for gate or release records, `A.15` for work, `C.11` for decisions, `C.32.P2S` for problem-to-structure carry-through when the view is one captured or lost-structure stage, and `E.17` for publication. `C.30.ASV` governs architecture structural-view adequacy for the selected structure being viewed.

### C.30.ASV:End

