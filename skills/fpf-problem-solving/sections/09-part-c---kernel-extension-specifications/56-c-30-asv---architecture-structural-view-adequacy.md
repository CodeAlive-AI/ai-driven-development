## C.30.ASV - Architecture Structural View Adequacy (ASV)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.ASV:1 - Problem frame

Use this pattern when you have a structural description of one selected architecture-relevant `U.Structure` and need to decide whether that same description is also a `U.View` under one exact viewpoint.

The first useful move is small. In ordinary prose, name the described holon or actual `ArchitectureRelation` when known, the selected structure, the smallest useful structure-kind set, any qualifier that changes interpretation, and the next architecture move. If one or two sentences make those values clear, stop.

For example: “The failover diagram describes runtime-interaction and control structures, but it hides the actual failover relation. Recover that relation before relying on the diagram as a view.” This is already a usable triage result. Use `ArchitectureStructureKindTriage@Project` only when the result must be retained, compared, or handed on.

```text
ArchitectureStructureKindTriage@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureStructuralViewProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  describedHolonRef?: U.HolonRef
  candidateViewEpistemeRef?: U.EpistemeRef
  exactViewpointRef?: U.ViewpointRef
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef
  claimScope?: U.ClaimScope, byValue
  effectiveReferenceScheme?: U.ReferenceScheme, byValue
  modelUseStructureRef?: U.StructureRef
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  smallestUsefulStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  selectedStructureRefs?: FinSet(U.StructureRef)
  claimPatternRefs?: FinSet(PatternRef), if another claim is being made
  admissibleArchitectureMove:
  stopCondition:
```

`@Project` is a compatibility and retrieval cue for a project-side use record. It supplies no project identity, authority, context, viewpoint, parthood, or Work occurrence. When one actual project matters to this triage, `projectWorkOccurrenceRef` identifies the composite `U.Work` recovered under `A.15.6`. Include `architectureStructuralViewProjectUseRelationRef` only when a named pattern defines the relation by which this use concerns that Work and an occurrence of the relation obtains. A Work reference alone does not establish project locality. If locality matters but that relation is not yet defined, use A.6.RCD before filling the field; otherwise omit both project-local fields. `claimPatternRefs` points only to patterns that define or test separate claims; it does not identify a pattern-application occurrence.

Start with `C.30` when the actual architecture relation, exact selected structure, or architecture claim is unclear. Use C.30.ASV only when a structural description over selected architecture-relevant structure changes the next architecture use. Use the full `ArchitectureStructuralView` record only when one exact description episteme passes E.17.0 conformance to an exact viewpoint and the view changes action, selected reliance relation, correspondence, source return, publication, comparison, or another non-ASV claim or use.

What goes wrong if C.30.ASV is missed: one favored diagram, module view, TEVB viewpoint, generated relation graph, control sketch, or neural-network block diagram is treated as the architecture, selected structure, `U.View`, or proof without naming the exact description episteme, selected structure kind, viewpoint-conformance occurrence, hidden or lost structure, correspondence, and next architecture use.

What C.30.ASV buys in practice: the practitioner can distinguish description identity, selected structure and structure kind, exact viewpoint conformance, representation, and publication before relying on a view. Construction history, hidden or lost structure, correspondence, source return, and admissible use remain separately inspectable.

Do not use C.30.ASV when the question is only about a general architecture claim, subject-side `ArchitectureRelation`, structure as such, selected transformation-flow relation, mathematical graph description, transformation-flow path relation, or crossing relation. Use `C.30`, `A.22`, `E.18`, `E.18.2`, `C.29`, or `C.30.TFS-REL` as appropriate. If the view is used for another claim, use the applicable pattern for that claim and keep C.30.ASV only for the view portion.

Thin precision-restoration pointer: if the issue under repair is still whether *view*, *architecture view*, *architecture structural view*, *diagram*, *model*, *graph*, *layer*, or *functional architecture* names a structural description, a `U.View`, an architecture description, a representation, a publication occurrence, a publication form, a source relation, or another claim or relation named by value, use `C.30.P` first. Apply C.30.ASV only after the architecture structural-view claim or non-ASV claim named by value is recoverable.

### C.30.ASV:2 - Problem

Architecture structural-view work is selected-structure triage: which architecture-relevant structure is described, which structure kind is under consideration, which exact viewpoint's fixed rules the description satisfies, and what relation, constraint, invariant, operation, dynamics description, hidden or lost structure, correspondence, source-to-use path or work-reliance relation, and source-return condition changes the next architecture move. The candidate is first one C.2.1 description episteme. That same episteme is a `U.View` only while an exact `EpistemeViewpointConformanceRelation` to an independently identified `U.Viewpoint` episteme obtains. Diagram, representation, publication occurrence, form, carrier, and rendering remain separate.

Without this pattern:

- a module-interface view is treated as all architecture;
- a selected transformation-flow structure, mathematical graph description, or control diagram is treated as proof;
- a structure kind is treated as a `U.Viewpoint`;
- a viewpoint label, query, authoring route, family-declaration membership, diagram, or publication is treated as enough for `U.View`;
- E.17.2's TEVB template or a project-local TEVB declaration is treated as a global bundle and mutated to carry architecture-specific structure kinds;
- a diagram, table, dashboard, generated relation graph, or ADR is treated as the view episteme itself;
- functional architecture is treated as a peer ontology rather than a structure-kind interpretation under C.30;
- cross-view consistency is asserted by prose instead of correspondence claims or independently obtaining relations;
- omitted structure is relied on in subsequent work without a source-return condition.

### C.30.ASV:3 - Forces

| Force | Tension |
| --- | --- |
| View usefulness vs view overread | Views make architecture discussable, but a useful description episteme, diagram, or publication form can be mistaken for architecture, selected structure, view membership, proof, or decision. |
| Structure kind vs viewpoint | A structure kind classifies selected structure; one exact viewpoint episteme states the rules under which the same candidate episteme is a view. They often appear together but are not the same object. |
| TEVB template reuse vs architecture-specific structure | E.17.2 distinguishes four useful authoring positions but supplies no current family or viewpoint references. Only a materialized project-local declaration supplies exact reusable `U.ViewpointRef` values; architecture-specific structure kinds are defined beside them and alter neither the resolved P editions nor declaration membership. |
| Small triage vs full view record | Many cases need only the structure kind under consideration and next architecture use; the full description-plus-conformance record is justified only when it changes action. |
| Multi-view correspondence vs single-view shortcut | Architecture work often needs relations among functional, flow, control, module, information, work, evidence, scale, and placement views; one favored diagram cannot carry all claims. |
| Hidden structure vs practical compression | A useful view omits something; omitted structure becomes a problem only when subsequent action relies on it. |

### C.30.ASV:4 - Solution

For an architecture structural view, first identify one candidate description episteme, its exact selected `U.Structure` EntityOfConcern, effective `U.ReferenceScheme`, structure kind, exact viewpoint episteme, and the direct conformance occurrence. Then add construction history, correspondence, hidden or lost structure, source-to-use path or work-reliance relation when current, source-return condition when needed, admissible use, and next architecture move. Use `ArchitectureStructuralView` only for the same episteme whose E.17.0 conformance actually obtains.

A conforming `ArchitectureStructuralView` is not a second individual beside its description. The candidate retains one C.2.1 identity `<exact ClaimGraph, one exact selected-structure EntityOfConcern, effective U.ReferenceScheme>`. The exact viewpoint and `EpistemeViewpointConformanceRelation` qualify that same episteme as `U.View`; they do not enter its C.2.1 identity.

C.30.ASV is the selected-structure structural-view adequacy pattern for architecture work. It explains how descriptions of different selected structure kinds may satisfy declared viewpoints and concerns. It is not a complete architecture-description pattern; `C.30.AD` composes separately identified descriptions, view-use claims, and correspondence only when that broader description use is being made.

C.30.ASV does not extend any TEVB family by implication. It defines architecture structure kinds and architecture-specific bindings to exact viewpoint epistemes. A project reuses a TEVB or architecture viewpoint only through an exact `U.ViewpointRef` resolved from a materialized local declaration in one exact E.17.1 catalogue; E.17.2 and C.30.ASV otherwise provide templates, not current family values. Source-to-use, work-reliance, project-use, representation, and publication relations remain separate from viewpoint conformance.

#### C.30.ASV:4.1 - Architecture structural view record

`StructuralAspectDescription` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` or `U.View` by itself. `ArchitectureStructuralView` names the same architecture-description episteme only after exact E.17.0 conformance obtains.

```text
ArchitectureStructuralView ::= ArchitectureDescription & U.View & {
  viewEpistemeRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: selectedStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,

  selectedStructureRef: U.StructureRef,
  relatedStructureRefs?: FinSet(U.StructureRef),
  structureKindRef: ArchitectureStructureKindRef,

  viewpointRef: U.ViewpointRef,
  viewpointConformanceRelationRef: EpistemeViewpointConformanceRelationRef,
  concernRefs?: FinSet(U.EntityRef),

  describedHolonRef?: U.HolonRef,
  architectureRelationOccurrenceRefs?: FinSet(ArchitectureRelationRef),
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  claimScope?: U.ClaimScope, byValue,
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(EpistemeEmpiricalGroundingRelationRef),

  recordPatternLocator,
  selectedRelationKindRefs?,
  selectedConstraintRefs?,
  selectedInvariantRefs?,
  selectedOperationDescriptionRefs?,
  selectedDynamicsDescriptionRefs?,
  viewConstruction:
    directDescription | projection | query | extraction |
    coarsening | correspondenceSlice | sourceReturnSlice,
  structuralAspectDescriptionRef?: U.EpistemeRef,
  hiddenOrLostStructure,
  structureKnowledgeState?:
    declared | observed | inferred | generated | simulated |
    extracted | hypothesized | unknownRegionPresent,
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  workRelianceRelationRefs?: FinSet(U.RelationRef),
  sourceReturnCondition?,

  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse
}
```

`recordPatternLocator` identifies the pattern whose record form is being used. It is a locator, not a substitute for any rule needed by a current claim.

The selected `U.Structure` is the one EntityOfConcern. Before that field can be filled, A.22 identifies the structure from exact constituents, selected independently obtaining relation occurrences, applied constraint claims, and one exact receiving-use frame. A description, query, diagram, family declaration, file, representation, or publication creates none of those discriminators. `relatedStructureRefs` may name structures needed to interpret correspondence, allocation, or crossing, but they do not create a union-valued EntityOfConcern. When another selected structure becomes primary, identify another description episteme under C.2.1. Assert edition continuity only when its historical-continuation predicate obtains, and apply A.6.4 separately when retargeting is claimed; do not overwrite identity through a view field.

The direct conformance occurrence has exactly two participants: `viewEpistemeRef` as candidate E and `viewpointRef` as exact P. Its fixed E.17.0 predicate requires: (1) independently identified E and admitted P; (2) exact `EntityOfConcern(E)` recovered; (3) P's fixed EntityOfConcern-kind criterion succeeds for that exact object; (4) E has an independently admitted episteme kind accepted by P without circular `U.View` use; and (5) E's fixed claim content under its effective scheme satisfies P's concern-coverage, semantic-form, completeness, and admitted-omission rules. The occurrence is participant-determined by `<E,P>`.

An architecture claim can carry positive, negative, unresolved, required, desired, expected, or candidate content. `architectureRelationOccurrenceRefs` is affirmative only for independently obtaining direct `ArchitectureRelation` occurrences. `describedHolonRef` and participant traces keep the subject recoverable; neither an optional claim nor a diagram derives the subject-side occurrence.

`ClaimScope`, concern, model-use structure, and empirical grounding remain optional neighboring qualifiers or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection for this use. None enters base episteme or selected-structure identity.

`viewConstruction` records provenance only. Direct authoring, A.6.3 construction, projection, query, extraction, selection, bundle inclusion, diagramming, rendering, publication, evaluation, or current use neither satisfies the conformance predicate nor creates selected structure. Representation, publication occurrence, form, and carrier likewise retain their own identities.

`structureKnowledgeState?` states how the selected structure is known when partial knowledge matters: declared, observed, inferred, generated, simulated, extracted, hypothesized, or with an unknown region present. Unknown or inferred structure may guide inspection or source return; it cannot by itself supply architecture truth, assurance, gate, release, causal proof, or architecture decision.

#### C.30.ASV:4.2 - Architecture structure-kind classifier

`ArchitectureStructureKindRef` is a C.30-local `DiscriminatorToken` enumeration over exact architecture-relevant `U.Structure` references selected under A.22 and used by C.30. It is not `U.Kind`, `U.Viewpoint`, `U.ViewpointBundle`, `StructuralAspectDescription`, `ArchitectureStructuralView`, or a root `U.*` kind. An `ArchitectureStructuralView` uses `structureKindRef` to state which kind of selected structure its claim graph describes; that token neither identifies the structure nor grants `U.View` membership.

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
- applicable patterns for non-ASV claims;
- a selected-structure admission test, plus the effective `U.ReferenceScheme` when the local classifier name depends on one.

Each structure kind needs a short definition, allowed relation families, locally triggered overreads, applicable patterns for its non-ASV claims, and example architecture structural-view records. This is not a new root-kind set; it is a controlled classifier set over exact `U.Structure` values.

#### C.30.ASV:4.3 - Small triage output

When triage must be retained, compared, or handed on, use `ArchitectureStructureKindTriage@Project` before a full view record when the practitioner only needs to identify the structure kind under consideration and next architecture move.

```text
ArchitectureStructureKindTriage@Project ::= {
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work,
  architectureStructuralViewProjectUseRelationRef?: U.RelationRef, only when a named pattern defines this project-use relation and the occurrence obtains,
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim,
  architectureRelationOccurrenceRef?: ArchitectureRelationRef,
  describedHolonRef?: U.HolonRef,
  candidateViewEpistemeRef?: U.EpistemeRef,
  exactViewpointRef?: U.ViewpointRef,
  viewpointConformanceRelationRef?: EpistemeViewpointConformanceRelationRef,
  claimScope?: U.ClaimScope, byValue,
  effectiveReferenceScheme?: U.ReferenceScheme, byValue,
  modelUseStructureRef?: U.StructureRef,
  architectureConcernCue?,
  sourcePhrase?,
  inspectedDescriptionOrViewRef?: U.EpistemeRef,
  candidateStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  smallestUsefulStructureKindRefs: FinSet(ArchitectureStructureKindRef),
  selectedStructureRefs?: FinSet(U.StructureRef),
  hiddenOrLostStructureCueRefs?,

  admissibleArchitectureMove:
    inspect | split | relate | downgrade | nameApplicablePattern | stop |
    otherDeclared,
  claimPatternRefs?: FinSet(PatternRef),
  nonAdmissibleOverread?,
  stopCondition
}
```

`architectureConcernCue?` and `sourcePhrase?` are recognition wording. `claimPatternRefs?` names only patterns that define or test separate claims; it does not assert that a pattern-application occurrence exists. `inspectedDescriptionOrViewRef?` and `candidateViewEpistemeRef?` name actual epistemes only when identified under C.2.1. None creates an `ArchitectureStructureKindRef`, selected structure, architecture relation, or `U.View`. Fill `exactViewpointRef` when the exact independently admitted viewpoint is identified; fill `viewpointConformanceRelationRef` only when the same candidate episteme actually conforms to that viewpoint.

When `architectureClaimRef` is absent, `describedHolonRef`, `architectureRelationOccurrenceRef`, or at least one exact candidate selected structure must keep the subject recoverable for the intended triage. `claimScope`, `effectiveReferenceScheme`, and `modelUseStructureRef` are present only when they change this use. The card publishes no architecture claim and creates no subject relation. A full `ArchitectureStructuralView` requires the candidate episteme's exact C.2.1 identity plus obtaining E.17.0 conformance; it does not require an architecture-claim record when the exact selected-structure EntityOfConcern and subject trace are otherwise recoverable.

Practitioner prompt labels are first-entry cues, not `ArchitectureStructureKindRef` values. When the triage is retained as a record, use the technical values below:

```text
Functional -> FunctionalStructure
Flow -> TransformationFlowStructure
Control -> ControlStructure
Module -> ModuleInterfaceStructure
Method and work -> WorkMethodStructure
Allocation and responsibility -> AllocationResponsibilityStructure
Evidence -> EvidenceAssuranceStructure
Scale -> ScaleEvolutionStructure
Security -> SecurityTrustBoundaryStructure
```

#### C.30.ASV:4.3a - Evolutionary-engineering candidate structural view

Use this branch when a retained variant, front member, selected set, or architecture-candidate palette needs structural-description triage. The claim is not "this archive is architecture" and not "this record is already a `U.View`." It is "this candidate makes an exact selected structure or structure kind current for an architecture claim or possible architecture move."

```text
ArchitectureCandidateStructuralDescription:
  CandidateSetOrArchiveRef:
  CandidateRef:
  DescribedHolonOrArchitectureRelationRef:
  SelectedStructureOrStructureKindRef:
  CandidateDescriptionEpistemeRef:
  ExactViewpointRef?:
  ViewpointConformanceRelationRef?:
  AffectedCharacteristicRef:
  CorrespondenceOrLossRef?:
  NextQuestionPatternLocator:
```

If the candidate cannot name an exact selected structure or structure kind, keep it in `C.18`, `C.19`, or `G.5`. If the description is used only to publish, compare, or explain the candidate, use `C.30.AD`, the comparison pattern, or the publication-use pattern named by value. It is an `ArchitectureStructuralView` only when the same candidate description episteme independently conforms to the exact viewpoint under E.17.0.

#### C.30.ASV:4.4 - Project-local architecture viewpoint-family template and binding rows

C.30.ASV ships no exact architecture viewpoint catalogue, family value, reference, or viewpoint episteme edition. `VF.ARCH.STRUCTURE`, `VF.TEVB.ENG`, and `VP.Architecture*` are therefore not current global values. A project may use similarly spelled ordinary designators only after it constitutes exact catalogue episteme L and binds exact local references.

Architecture structural views can reuse a materialized local family without turning structure kinds into viewpoints. The project first:

1. constitutes exact L through obtaining `EpistemeConstitutionRelation(G_L, K_L, R_L)`;
2. places one local declaration claim block inside exact `G_L`, retrieved by ordinary `familyDesignator = f_arch` under `R_L`;
3. states the exact target-kind compatibility condition and a finite non-empty set of exact `U.ViewpointRef` members;
4. resolves every retained reference under `R_L` to one exact P already admitted under E.17.0; and
5. preserves exact catalogue and member provenance for any imported project-local TEVB reference rather than importing a family label.

Until those bindings exist, use this only as an authoring template:

```text
ArchitectureViewpointFamilyTemplate ::= {
  catalogueConstitution: <G_L, K_L, R_L>,
  catalogueEpistemeRef: L,
  catalogueLocator: <editionDesignator(L), f_arch>,
  targetKindCompatibilityCondition: exact criterion that candidate E has recoverable C.2.1 identity and EntityOfConcern(E) is one selected U.Structure, stated by value or by ClaimGraph reference,
  viewpointRefs: {
    r_architecture_structure,
    r_architecture_correspondence,
    r_architecture_source_return,
    r_architecture_decision_affected_structure
  },
  resolutions: {
    resolve_R_L(r_architecture_structure) = P_architecture_structure,
    resolve_R_L(r_architecture_correspondence) = P_architecture_correspondence,
    resolve_R_L(r_architecture_source_return) = P_architecture_source_return,
    resolve_R_L(r_architecture_decision_affected_structure) = P_architecture_decision_affected_structure
  },
  optionalReaderDesignators: {
    d_architecture_structure,
    d_architecture_correspondence,
    d_architecture_source_return,
    d_architecture_decision_affected_structure
  },
  importedReferenceProvenance?: {
    <editionDesignator(L_source), sourceFamilyDesignator, exactSourceViewpointRef>
  }
}

ArchitectureStructureKindViewRecordBinding ::= {
  catalogueEpistemeRef: L,
  catalogueLocator: <editionDesignator(L), f_arch>,
  structureKindRef: ArchitectureStructureKindRef,
  allowableViewpointRefs: FinSet(U.ViewpointRef),
  candidateViewRecordSetRef,
  allowedViewConstructionModes,
  requiredConformanceRuleRefs,
  requiredCorrespondenceClaimOrRelationRefs?,
  sourceReturnRequirement?,
  claimPatternRefs: FinSet(PatternRef)
}
```

Every `r_*`, `P_*`, `d_*`, L, and `f_arch` above is a variable until one project supplies the exact binding. A `d_*` value is only P's ordinary designator; it is neither a reference nor P. Another project with matching spellings has not reused this family unless it resolves the same exact L, declaration, and members.

Project-local TEVB reuse follows the same rule. A project may retain one or more exact references from a materialized local TEVB declaration when their exact P rules fit. It preserves each `<editionDesignator(L_source), sourceFamilyDesignator, sourceViewpointRef>` tuple and any omission decision. It does not expand a global TEVB core, infer a cross-family import relation from labels, or claim that E.17.2's four-position template is a materialized family.

`candidateViewRecordSetRef` names an exact C.13 collection of permitted description or specification-use record forms for one structure-kind binding. The binding and family declaration may help retrieve candidate E and resolve exact P, but neither makes the fixed E.17.0 predicate true, identifies an `EpistemeViewpointConformanceRelation` occurrence, grants `U.View` membership, or creates the selected structure. The collection is not a publication face or package grouping, and it neither supplies a `ViewFamilyId` nor adds a viewpoint; publication forms, carriers, catalogue locators, and family designators remain separate.

#### C.30.ASV:4.4a - Structural-view publication-use boundary

This is the C.30.ASV structural-view publication-use boundary. C.30.ASV covers the description episteme's identity, selected architecture-relevant structure, structure kind, E.17.0 viewpoint conformance, construction history, correspondence, hidden and lost structure, source return, and the next architecture move. When a view, diagram, graph, card, benchmark, probe output, model publication, or architecture note is used for evidence sufficiency, safety assurance, gate passage, release permission, work record, or decision authority, use the applicable pattern for that claim; keep only the structural-view record and next architecture move in C.30.ASV.

#### C.30.ASV:4.5 - Initial architecture structure kinds and view records

The initial set is a seed for first architecture moves, not an atlas. Use the table to choose one structure kind under consideration and the applicable pattern for any non-ASV claim.

| Seed structure kind | Structural view | Minimum record fields beyond common ASV fields | First boundary |
| --- | --- | --- | --- |
| `FunctionalStructure` | `FunctionalStructureView` | `functionalBehaviorClaimRefs`, `requiredOrDesiredEffectClaimRefs?`, `actualTransformationRefs?`, `selectedTransformationFlowStructureRefs?`, `functionalElementClaimRefs?`, `transformerSideFillerRefs?`, `candidateBearerRefs?`, input-condition refs, output-condition refs, functional-port refs, capability refs, dependency refs, allocation refs, correspondence refs | Required or desired content stays a claim; use `A.3.4` only for independently actual transformations, and use capability, work, module-allocation, or requirement patterns when those claims are being made. |
| `TransformationFlowStructure` | `TransformationFlowStructureView` | `transformationFlowStructureRef`, `pathSliceRefs`, `crossingRefs`, `valuationRefs`, `mathematicalDescriptionRefs?` | Use `E.18` and `C.30.TFS-REL` for selected transformation-flow structure, transformation-flow path, or crossing input; use `E.18.2` and `C.29` for mathematical graph descriptions; use `C.28` for causal claims. |
| `RuntimeInteractionStructure` | `RuntimeInteractionStructureView` | runtime elements, connectors and protocols, event topology and message topology, failure boundaries and latency boundaries | Use temporal, failure, evidence, or assurance patterns when runtime claims exceed structure. |
| `ModuleInterfaceStructure` | `ModuleInterfaceStructureView` | module claim or admitted relation refs, interface specs, admissibility conditions, substitutability policy or change policy | Use `A.6.M` to repair the module claim and identify the admitted interface or relation separately when those claims are being made. |
| PlacementDeploymentStructure | PlacementDeploymentStructureView | allocation-to-site refs or environment refs, network locality or physical locality, jurisdiction constraints or safety constraints | Use temporal, evidence, law-domain, regulatory, or safety patterns when claims of those non-placement kinds are being made. |
| `InformationDataStructure` | `InformationDataStructureView` | state bearer and residence refs, schema refs, semantic refs, persistence locus, provenance relation, custody relation, source-return conditions, privacy constraints | Use evidence, privacy, or source-return patterns when those claims are being made. |
| `SecurityTrustBoundaryStructure` | `SecurityTrustBoundaryStructureView` | protected asset or effect refs, trust boundary refs, untrusted input refs, privilege or authority refs, data-flow and control-flow refs, attack exposure refs, abuse or misuse path refs, secure-default or hardening boundary, supply-chain or update-channel refs, detection-response boundary refs when the corresponding claim is being made | Gives a first security-architecture move before evidence, assurance, gate, risk-score, or compliance proof. |
| `ControlStructure` | `ControlStructureView` | control-participant refs, declared control-rate refs, observer, estimator, controller, planner, and supervisor relations, feedback refs | Use `C.30.LCA`, dynamics, temporal, causal, evidence, and assurance patterns when those claims are being made. |
| `ConstraintRequirementStructure` | `ConstraintRequirementStructureView` | requirement refs, constraint refs, and invariant refs, affected structure refs, admissibility conditions | Requirements shape structures; use the applicable requirement, gate, evidence, causal, or decision pattern for those claims. |
| `MaterialSpatialStructure` | `MaterialSpatialStructureView` | geometry, adjacency, containment, energy flow or material flow, safety separation | Physical separation is not safety proof; use the applicable safety, evidence, dynamics, or causal pattern for those claims. |
| `DeclaredLogicalStructure` | `LogicalStructureView` | local logical relation class, relation constraints, correspondence to functional structures, module structures, runtime structures, and data structures | Covers `logical architecture` without making `logical` a universal ontology token. |

Classifier values defined outside C.30.ASV remain admissible when they are the architecture-relevant structure under consideration, but C.30.ASV does not define their full record families:

| Classifier value defined outside C.30.ASV | ASV use | Full semantics and applicable patterns |
| --- | --- | --- |
| `WorkMethodStructure` | Method arrangement or work arrangement changes the architecture move. | `A.15` keeps `MethodDescription`, one exact `U.WorkPlan`, and dated `U.Work` occurrences separate; use the applicable pattern for any exception-handling, launch, or gate claim. Do not turn a work-method diagram into work authority. |
| `AllocationResponsibilityStructure` | Exact responsibility relations or enactor-allocation relations change the architecture move. | Preserve each admitted direct responsibility predicate and occurrence through the view. Keep the System, local system-role kind, separate System-classification judgment, assignment, enactor relation, organization relation, actual Work basis, concern or affected-party relation, authority, ownership, stewardship, and responsibility distinct. Recover `owner`, `steward`, and `stakeholder` from the claim they make and use the corresponding direct ownership, governance, stewardship, concern, affected-party, participation, responsibility, authority, or ordinary-label route. Use `E.10.ROLE` only when the source wording actually uses unresolved claim-bearing *role*. Return the exact `missing-governor` for a required relation rather than treating an org chart, title, assignment, or Work as that relation. |
| `EvidenceAssuranceStructure` | Evidence reuse or assurance arrangement changes affected structure or source return. | Use `A.10` for bounded source-to-use reliance, `G.6` for citable provenance paths, and `B.3` only for a named assurance claim; the applicable result pattern establishes evidence sufficiency. ASV only names the structure and loss boundary. |
| `ScaleEvolutionStructure` | Scale window, replacement or change policy, trajectory reference, or coarse-graining changes the architecture move. | Use `C.29`, `C.16`, temporal, source-return, or decision patterns for scale, characterization, or selection claims. |
| `OtherDeclaredStructureKind` | A local structure kind is declared because none of the seed or externally defined values fits. | Name its definition, selected-structure admission test, relation families, applicable patterns, and effective reference scheme when local meaning depends on one; do not mint a root kind by label alone. |

Minimum useful seed examples:

| Structure kind | Minimal example | False interpretation | Pattern for the first non-ASV claim |
| --- | --- | --- | --- |
| `FunctionalStructure` | Capability, required or desired effect claim, or separately actual transformation allocation. | Purpose truth, requirement satisfaction, or a required effect treated as actual change. | `A.6.F`, `A.3.4` only for actual transformation, capability, work, or requirement pattern when that claim kind is being made. |
| `TransformationFlowStructure` | Transformation-flow path, crossing, valuation, or selected transformation slice. | Whole architecture or causal proof. | `E.18`, `C.30.TFS-REL`, `E.18.2`, C.29, or C.28 when selected structure, graph description, transformation-flow path, crossing, mathematical-lens, or causal-use claim kind is being made. |
| `ControlStructure` | Controller, observer, plant, feedback, or rate relation. | Stability, safety, or assurance proof. | `C.30.LCA`, temporal, dynamics, causal, evidence, or assurance pattern when that claim kind is being made. |
| `ModuleInterfaceStructure` | Module relation, interface spec, or substitutability boundary. | Module tree as all architecture. | `A.6.M` module-relation repair, conformance evidence, or decision pattern when that claim kind is being made. |
| `InformationDataStructure` | State bearer, residence, provenance, and custody. | Database label. | Evidence, privacy, or source-return pattern when that claim or reliance use is being made. |
| `SecurityTrustBoundaryStructure` | Trust boundary, untrusted input, privilege path, or attack exposure. | Security proof, risk score, or compliance label. | Evidence, assurance, gate, `C.24` call planning after the action or option is fixed, C.16, C.25, or C.30.LCA when that security, evidence, assurance, gate, call-planning, measurement, quality, or control claim or use is current. |
| `MaterialSpatialStructure` | Separation, adjacency, containment, or energy path or material path. | Safety proof or geometry as architecture truth. | Safety, evidence, dynamics, or causal pattern when that claim kind is being made. |
| `DeclaredLogicalStructure` | Local logical relation class with correspondence to other structures. | Universal logical architecture ontology. | Use the applicable correspondence, function, module, runtime, or data pattern for the relation or claim. |

Minimal `SecurityTrustBoundaryStructureView` fields:

```text
SecurityTrustBoundaryStructureView ::= {
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
  claimPatternRefs:
    A.10 | G.6 | B.3 | C.28 | A.20 | A.21 |
    C.16 | C.25 | C.24 call planning after the action or option is fixed | C.30.LCA when a control relation is being claimed
  admissibleUse:
  otherClaimBoundary:
    compliance, risk-score, assurance, checklist-security, and zero-trust claims use the applicable evidence, assurance, risk, gate, or security pattern
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
  claimPatternRefs:
    A.3.3 dynamics, C.27 temporal or rate,
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 internal-constraint validity, A.21 gate decisions
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive first architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

#### C.30.ASV:4.6 - Functional structure view boundary

A `FunctionalStructureView` under C.30.ASV does not mint `U.Function`, `U.Transformation`, or a bearer relation. It is the same `ArchitectureStructuralView` episteme whose EntityOfConcern is one selected functional `U.Structure` and whose exact viewpoint conformance obtains. It may carry `FunctionalElementClaim` epistemes when the claim graph relates that selected functional structure to required or desired behavior or effect content and to a bearer or candidate-bearer locus. The claim is not identical with any actual behavior occurrence, bearer, capability, port, allocation, or relation.

Keep three branches explicit:

- **required or desired behavior or effect:** a C.2.1 claim; use the applicable requirement, architecture, capability, method, or functional-view pattern for that claim;
- **actual transformation:** an independently identified `U.Transformation` only after A.3.4 recovers the changed referent, extent or boundary, boundary conditions, actual before, during, and after facts, and continuity or reidentification basis;
- **compound flow organization:** an exact selected `TransformationFlowStructure` under E.18, whose constituents and selected obtaining relations are independently identified; the structure is not itself an actual transformation.

`FunctionalElementClaim` has ordinary C.2.1 identity `<exact ClaimGraph, one exact EntityOfConcern, effective U.ReferenceScheme>`. For this use its EntityOfConcern is the selected functional structure. Its claim content may name:

- one or more required or desired behavior or effect claim refs;
- actual transformation refs only when the complete A.3.4 basis independently obtains;
- selected transformation-flow structure refs for compound flow organization;
- a bearer or candidate-bearer locus, normally a `U.System` or candidate system for a separately established transformer system-role-kind claim;
- capability, input and output condition, functional-port, dependency, allocation, and correspondence refs only when the applicable pattern defines or tests that relation or claim.

If no bearer or candidate allocation is current, do not claim a filled functional element. Record a required-behavior gap, required-effect gap, capability gap, functional-behavior slot, or candidate allocation question. This preserves the practical architecture move without pretending that a module, component, diagram row, function word, requirement, or selected flow structure has already supplied the bearer or actual change.

```text
FunctionalStructureViewUse ::= {
  architectureStructuralViewRef: U.EpistemeRef constrained to ArchitectureStructuralView,
  functionalElementClaimRefs?: FinSet(U.EpistemeRef),
  sourceFunctionWordingRefs?,
  functionalBehaviorClaimRefs?: FinSet(U.EpistemeRef),
  requiredOrDesiredEffectClaimRefs?: FinSet(U.EpistemeRef),
  actualTransformationRefs?: FinSet(U.TransformationRef),
  selectedTransformationFlowStructureRefs?: FinSet(U.StructureRef constrained to TransformationFlowStructure),
  transformerSideFillerRefs?: FinSet(U.SystemRef),
  candidateBearerRefs?: candidate system refs; explicit gap refs,
  capabilityRefs?,
  inputConditionRefs?,
  outputConditionRefs?,
  functionalPortRefs?,
  functionalDependencyRefs?,
  allocationRefs?,
  correspondenceClaimOrRelationRefs?,
  nonFunctionClaimNotes?,
  flowRelationRefs?,
  moduleInterfaceClaimOrRelationRefs?,
  admissibleUse,
  nonAdmissibleUse
}
```

**Required cooling effect followed by actual cooling.** Requirement episteme `RequiredCoolingEffect-1` says that Rack 7 should be brought below 30 °C during declared operation. Before the rack or cooling loop has changed, that is required effect claim content: there is no actual `U.Transformation`, even if a functional-view row, flow diagram, or selected `TransformationFlowStructure` cites it. Later, `Rack7CoolingTransformation-42` may be identified under A.3.4 when the exact changed referent and boundary are fixed, operating and ambient boundary conditions are stated, actual before facts show 38 °C, actual during facts recover heat removal, actual after facts show 27 °C, and continuity or reidentification keeps the same referent recoverable. A separate satisfaction or realization predicate is still needed before claiming that the later transformation satisfies `RequiredCoolingEffect-1`; temporal succession or matching labels alone is insufficient.

A selected transformation-flow structure, mathematical graph description, transformation-flow path slice, crossing, or flow valuation is not a functional element or actual transformation by default. When a transformation-flow relation is being used, connect the functional view to the exact `TransformationFlowStructure` through `C.30.TFS-REL`. When a mathematical graph description is being used, connect it through `E.18.2`; when math-lens use is being claimed, connect it through `C.29`. When module allocation is being claimed, use `A.6.M` to repair the module claim and identify the admitted allocation or interface relation separately rather than treating function and module as one kind. Functional ports and module interfaces can both use `U.Signature` discipline, but functional ports specify behavior input and output slots while module interfaces specify substitution, compatibility, boundary, and change-policy claims.

Composability and quality compositionality are separate claims. If the view says parts can be assembled, keep that as a structure claim or use claim. If it says a quality of the whole follows from parts, assign the quality-composition claim to `C.25` and C.16-backed measurement or quality claim.

```text
Composability:
  "A and B can be assembled under interface X."
  recoveredRelationOrRecordKind: ModuleAllocationRelation | InterfaceSpecification
Quality compositionality:
  "The assembled whole preserves safety, latency, or reliability."
  recoveredRelationOrRecordKind: QBundleSlot | structuralCharacteristicQBundleInputSlot | structuralCharacteristicCausalHypothesisForQBundleSlot | structuralCharacteristicEvidenceRelationForQBundleSlot(A.10 describes bounded source-to-use reliance; cited direct relations require their own defining patterns)
Non-admissible:
  successful assembly is not quality propagation
```

Compositional formalisms may express explicit composition structures, view relations, and model relations. They do not make required behavior actual, create transformations, or make safety, latency, reliability, or another quality propagate automatically.

#### C.30.ASV:4.7 - Correspondence and source return

Use correspondence records when the view relates functional, flow, control, module-interface, information, runtime, placement, work, evidence, scale, or logical structures. Do not assert cross-view consistency by prose alone.

Correspondence examples:

| Source wording | Recover |
| --- | --- |
| "This function is implemented by that module." | `FunctionToModuleAllocationRef` or the allocation or relation record named by value. |
| "This flow crosses that runtime boundary." | `FlowToRuntimeInteractionCorrespondence`. |
| "This evidence covers the replacement." | `EvidenceReuseToAffectedStructure`; use `A.10` for bounded source-to-use reliance, `G.6` for citable provenance paths, and `B.3` only for a named assurance claim. Establish sufficiency under the applicable result pattern. |
| "This requirement constrains that structure." | `RequirementToStructureConstraint` or a constraint record named by value. |
| "This scale window changes the structure kind." | `ScaleWindowToStructureKindCorrespondence`; assign scale-lens claims to `C.29` when those claims are being made. |

Use `SourceReturnCondition` when compression, extraction, coarsening, evidence reuse, ML evaluation, bounded exception, many-to-many allocation, publication, or decision claim hides a distinction needed for action, assurance, causal use, law-domain review, regulatory review, comparison, or reopening.

If `viewConstruction` is `query`, `extraction`, `coarsening`, `correspondenceSlice`, or `sourceReturnSlice`, and omitted structure changes action, assurance, causal use, law-domain or regulatory review, or subsequent decision reopening, `SourceReturnCondition` is needed.

When the view is used to name affected structures for a next architecture use but no decision record is being used, use C.30 `AffectedArchitectureStructureNote`: affected structure kinds, affected structure refs when known, affected ASV refs, accepted or suspected view loss, source-return condition, and the next admissible use. The note is not an architecture decision, ADR, gate passage, evidence sufficiency, or release authority.

Use the thinnest source or reliance relation that preserves the next architecture move. Use fuller source, evidence, assurance, or claim-kind relation only when the source or reliance relation being used cannot be inspected, used, compared, refreshed, or bounded without it. A `ControlStructureViewNote` may precede full `C.30.LCA` use or use of the applicable proof or assurance pattern when one control relation and its boundary are enough for the architecture move being made.

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

Model cards, system cards, and evaluation harness reports may publish or substantiate an architecture structural view only when the structural-view claim is recoverable. The view must name the relevant structure kind, such as `RuntimeInteractionStructure`, `InformationDataStructure`, `SecurityTrustBoundaryStructure`, `EvidenceAssuranceStructure`, `ModuleInterfaceStructure`, or another declared structure kind; it must also state intended-use scope, evaluation scope and known loss when evaluation is used, deployment-context mismatch when that mismatch is being claimed, and the applicable evidence or assurance pattern when the publication is used beyond transparency. A card or harness is not architecture adequacy, safety proof, or release claim or gate claim by publication alone.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the `ArchitectureStructuralView` locus and use conclusions that depend on it. A changed selected structure or structure kind reopens its exact structure fields and, when another structure becomes the EntityOfConcern, requires a separately identified description episteme; a changed description identity reopens only that episteme's view admission; a changed viewpoint or conformance occurrence reopens only the E.17.0 predicate; changed construction or knowledge state, correspondence, source edition or lost structure reopens the matching provenance, correspondence, source-to-use, hidden or lost structure, or source-return locus; and a changed admissible-use boundary or applicable rule reopens only its dependent use or claim. Update that locus, narrow use, return to the named source, or stop. If conformance to the current exact viewpoint is not established, use a structural description or `ArchitectureStructureKindTriage@Project` for the next move. Changed use alone leaves fixed `<E,P>` conformance unchanged; unrelated structures, views, and claims stay closed.

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

Use `C.24` when a fixed action or option needs budgeted tool-call planning or replanning. Use `A.15.1` for actual Work and identify any call-graph structure under its applicable pattern. Keep those claims and uses separate from the architecture structural-view claim.

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

**Organization or operating-model architecture.** An org chart or Work-Method diagram can be architecture-relevant only after Systems, local system-role kinds, separate System-classification judgments, assignments, enactor relations, complete actual-Work bases, direct responsibility relations, concern or affected-party relations, information, and evidence are separated:

```text
Organization and operating-model architecture first recovery:
  AllocationResponsibilityStructure:
    direct responsibility relation occurrences and enactor-allocation boundary;
    if the responsibility predicate is unavailable, exact missing-governor
  WorkMethodStructure:
    repeatable work method and exception-handling relation
  InformationDataStructure:
    information custody, state residence, provenance
  EvidenceAssuranceStructure:
    evidence reuse, approval, audit trail, source return
first architecture move:
  relate the exact responsibility and enactor-allocation relations, work repeatability,
  information custody, and evidence reuse
correspondenceOrLossLine:
  preserve the direct responsibility relation and its actual participants;
  record separately any local system-role kind and any System-classification judgment,
  assignment, enactor relation, complete actual-Work basis, concern or affected-party relation,
  information, and evidence structures,
  plus any org-chart or work-method-diagram loss
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
  claimPatternRefs:
    A.10 for bounded source-to-use reliance, G.6 for citable provenance paths, B.3 only for a named assurance claim; the applicable result pattern for evidence sufficiency
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
      admitted direct responsibility relations and their participant split, enactor-allocation relations,
      escalation relations, and separately any local system-role kind,
      System-classification judgment, and obtaining assignment;
      use missing-governor when the source says responsibility but no direct predicate is admitted
    InformationDataStructure:
      ticket state, customer record custody, dashboard source, and source-return condition
    EvidenceAssuranceStructure:
      audit trail, service-level evidence relation, assurance claim, and gate or release record only when those claims are being made
  C30ASVBoundary:
    ASV names selected structure and view boundary; staffing decision, work authority, evidence sufficiency, assurance, and service-quality claims use their applicable patterns
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
claimPatternRefs:
  C.30.TFS-REL when an E.18 flow relation is being used,
  A.6.M module-relation repair for tool, API, or interface relation claims,
  A.10 for bounded source-to-use reliance, G.6 for citable provenance paths, or B.3 only for a named assurance claim,
  C.24 for call planning after the action or option is fixed, E.16 for autonomy budgets and enforcement, A.20 for internal-constraint checks in transformation flow, or A.21 for gate decisions; use the defining pattern for any separate tool-call authority claim
stop condition:
  ASV contains only the structural-view record; evidence sufficiency, assurance, gate, autonomy, and tool-call authority claims use their applicable patterns
```

Structural AI-agent security is architecture structure when these structure kinds change the next architecture move. When the claim is instead about latent representation, decoding, or effect adequacy, keep the phrase as a reduced-use source cue and use the applicable representation, decoding, or effect-adequacy pattern.

**Generated code-agent relation graph.** A probe JSON or code-agent architecture relation graph can be an architecture structural view publication only after observed, inferred, or unknown observation value, evidence pointers or source pointers, unexplored regions, and typed relation semantics are present. Add source-return conditions when the intended use relies on hidden distinctions. Use the applicable proof and assurance patterns for the separate belief-state and downstream-change-safety claims.

**Neural-network block replacement.** Replacing attention, FFN, convolution, SSM, recurrent, memory block or cache block, MoE expert-selection, pruning, distillation, or another block is an architecture move only when the changed structure kind, flow relation, module-interface claim kind, preserved and lost structure, affected characteristic, source relation, and applicable decision or evidence pattern are named.

### C.30.ASV:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner looks at an architecture "view" and asks whether it is functional, flow, control, module-interface, information or data, placement, scale, work, evidence, or declared logical structure. C.30.ASV turns that question into structure-kind triage or a full description-plus-conformance record. |
| Show: `U.System` | A plant, vehicle, software system, product platform, AI-agent system, or neural-network model can require several structural descriptions over the same exact subject-side architecture. One module view does not exhaust the system architecture, and one flow graph does not prove work, evidence, safety, or release. |
| Show: `U.Episteme` | A diagram, model, generated relation graph, ADR, dashboard, SysML view, or C4 diagram may express or publish a description episteme. That same episteme is an architecture structural view only when exact C.2.1 identity, selected structure, structure kind, exact viewpoint, obtaining E.17.0 conformance relation, hidden and lost structure, correspondence, source or reliance relation, and admissible use are recoverable. |

### C.30.ASV:6 - Bias-Annotation

Bias lenses: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture structural-view claims over holons.

| Bias risk | Mitigation |
| --- | --- |
| Module-view bias | Make module-interface one structure kind, not the default meaning of architecture. |
| Viewpoint-kind conflation | Keep selected structure kind, exact viewpoint episteme P, catalogue L, local family declaration, exact `U.ViewpointRef`, candidate description E, and conformance relation separate. |
| TEVB mutation bias | Reuse only exact references from a materialized project-local TEVB declaration when their resolved P rules fit; do not treat E.17.2's template or a `VF.TEVB.ENG` spelling as a current family value. |
| Check-only bias | Every failed conformance check gives a repair action or use of an applicable pattern. |
| Didactic-thinning risk | The pattern starts with triage and action, not taxonomy alone. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, description, direct conformance relation, or repair guidance above.

### C.30.ASV:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-ASV-1 Structure target.** | Every architecture structural view has one exact selected `U.Structure` as its C.2.1 EntityOfConcern. | Name and constitute the selected structure under A.22, or keep the inspected episteme or publication as an architecture question input that does not yet claim to be a structural view. |
| **CC-ASV-2 Structure kind.** | Every architecture structural view names `structureKindRef`. | Use `ArchitectureStructureKindTriage@Project`; if no structure kind changes action, keep the text as ordinary prose or a source note. |
| **CC-ASV-3 Exact episteme and subject trace.** | The view preserves one exact claim graph, one selected-structure EntityOfConcern, effective `U.ReferenceScheme`, and the subject trace to the exact holon and any obtaining `ArchitectureRelation`; optional architecture claim, ClaimScope, empirical grounding, and model-use structure remain separate. | Restore the exact episteme identity and subject trace, or identify a new description before relying on it; do not derive identity from an architecture-claim field or context bundle. |
| **CC-ASV-4 Viewpoint conformance.** | The candidate episteme and exact viewpoint episteme satisfy the fixed five-part E.17.0 predicate, and `viewpointConformanceRelationRef` names the participant-determined obtaining occurrence. A bundle or viewpoint label is only discovery support. | Apply E.17.0. If the predicate does not obtain, keep a structural description or triage result and do not call it `U.View`. |
| **CC-ASV-5 Lost structure.** | The view names hidden or lost structure, especially for query, extraction, coarsening, or publication uses. | Add a one-line hidden-structure note or lost-structure note, or narrow the admissible use so omitted structure is not relied on. |
| **CC-ASV-6 Correspondence.** | Cross-view claims are carried by exact correspondence claims or independently established obtaining relations, not by prose, shared packaging, or graph adjacency alone. | Add a correspondence claim or direct relation, or stop at a single-view statement without a cross-view consistency claim. |
| **CC-ASV-7 No representation or publication collapse.** | A diagram, model, table, dashboard, generated relation graph, ADR, publication occurrence, form, or carrier is kept separate from the view episteme and selected structure. | Name the exact description episteme, any C.29 representation, and the E.24.PUB occurrence, form, and carrier separately; claim `U.View` only when E.17.0 conformance obtains. |
| **CC-ASV-8 No single-view architecture.** | If a decision uses an architecture view, it names the affected structures and views, not only one favored diagram. | Add affected structure and view refs, or narrow the decision to the single view's admissible use. |
| **CC-ASV-9 No proof overread.** | The view does not stand in for empirical grounding, evidence, safety proof, causal proof, gate decision, or work record; each such claim needs the basis required by its applicable pattern. | Use `EpistemeEmpiricalGroundingRelation` for grounding, `A.10` for bounded source-to-use reliance, `G.6` for citable provenance paths, `B.3` only for named assurance, `A.20` for internal-constraint validity, `A.21` for gate decisions, `C.28` for causal support, and the applicable safety or Work pattern for its result; mark an unsupported claim as such. Do not add more ASV fields as a substitute. |
| **CC-ASV-10 Relation or correspondence record named by value.** | Every cross-reference names the exact kind, claim, relation, or record: selected structure, structure kind, viewpoint, conformance occurrence, correspondence claim or relation, allocation record, bridge record, evidence relation, publication relation when publication is current, interface specification, or applicable record kind named by value. | Replace the ambiguous reference with the object that actually carries the claim, or split the sentence into separate objects. |
| **CC-ASV-11 Source return.** | When compression, extraction, coarsening, evidence reuse, publication, or many-to-many allocation hides distinctions on which the intended use relies, `SourceReturnCondition` is present. | Add one source-return trigger, or narrow the view's admissible use so omitted distinctions are not used for action, assurance, causal use, law-domain review, regulatory review, or reopening. |
| **CC-ASV-12 Architecture-name recovery.** | Every `<X>Architecture` phrase recovers exact selected structure, `<X>StructureKind`, or a declared local relation or claim. | Rewrite the phrase through `ArchitectureStructureKindTriage@Project`; if no relation is being claimed, keep the name as Plain prose and do not let it carry ontology. |
| **CC-ASV-13 Useful action.** | The repair leaves a surviving admissible architecture move: inspect, split, relate, downgrade, generate candidates, state a structural description or view, add correspondence, add source return, use the applicable pattern, or stop. | Restore one move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30.ASV:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Module diagram as architecture view** | One module-interface diagram is treated as the whole architecture or as a `U.View` by appearance. | Use structure-kind triage; keep module-interface as one structure kind and apply exact E.17.0 conformance only when view membership matters. |
| **Viewpoint as structure kind** | `VP.Functional`, `VP.ModuleInterface`, or another viewpoint is used as if it were the selected structure kind. | Recover `ArchitectureStructureKindRef`; keep its binding to an exact viewpoint episteme separate. |
| **Structure kind as viewpoint** | `FunctionalStructure` or `ControlStructure` is treated as if it were already an admitted viewpoint P. | Keep structure-kind classification separate; when viewpoint reuse is needed, resolve one exact `U.ViewpointRef` from a materialized local catalogue declaration to exact P and test E.17.0 conformance. |
| **Publication-face collapse** | A diagram, model, table, dashboard, generated relation graph, ADR, or C4 view is treated as the view episteme. | Recover description episteme, representation, and E.24.PUB occurrence, form, and carrier separately; use `ArchitectureStructuralView` only if exact conformance obtains and the view changes action. |
| **Single-view decision** | A decision uses one architecture view as if it covered all affected structures. | Name affected structures and view refs, or narrow the decision to the single view's admissible use. |
| **Lost-structure silence** | Extracted, generated, coarsened, or compressed views hide distinctions but still justify action. | Add hidden structure and lost structure and source-return condition, or narrow admissible use. |
| **Proof overread** | The structural view is used as evidence sufficiency, safety proof, causal proof, gate decision, or work record. | Use the applicable evidence, assurance, causal, gate, or work pattern and keep ASV only to view adequacy. |
| **Risk color as security architecture** | A red, yellow, or green risk cell, risk matrix, maturity score, or compliance color stands in for `SecurityTrustBoundaryStructure` or resource-allocation priority. | Recover protected asset or effect, trust boundary, untrusted input, privilege or authority relation, data flow or control flow, abuse or misuse path, and the evidence named by value, assurance, measurement, causal, gate, selection, or allocation claim kind if that claim is being made; do not treat ordinal risk color as security architecture adequacy, resource-allocation priority, or gate passage. |
| **Taxonomy without action** | The text classifies a view but does not say what changes in practice. | Add `admissibleArchitectureMove` or stop at Plain recognition wording. |

### C.30.ASV:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| Architecture views become exact description epistemes over selected structures, not diagrams by appearance. | A conforming use states C.2.1 identity, selected structure, structure kind, exact viewpoint, obtaining conformance relation, and admissible use. |
| Project-local TEVB reference reuse does not enlarge either template. | Architecture-specific structure-kind bindings add one explicit record when their coverage matters; every reused viewpoint reference retains its exact materialized catalogue and member provenance and grants no view membership. |
| Functional, flow, control, module-interface, placement, information, runtime, work, evidence, scale, material, and logical structures can be separated. | Some familiar names require triage before they can carry FPF claim kinds. |
| Failed checks produce repair actions rather than only classification objections. | The checklist is longer than a pure taxonomy, but it is more useful for action. |

### C.30.ASV:10 - Rationale

C.30.ASV exists because architecture descriptions are commonly multi-view, but FPF cannot let "view" absorb every architecture claim. A structure kind and a viewpoint are different. A structure kind says what kind of selected structure is described; a viewpoint is one exact episteme whose fixed rules the candidate description must satisfy. The direct conformance occurrence, not a label or bundle, makes the same episteme a `U.View`.

The pattern keeps first use light by providing `ArchitectureStructureKindTriage@Project`. If triage identifies the structure kind under consideration and the next admissible architecture move, no full view record is needed. The full record is used when exact conformance obtains and a view changes action, correspondence, publication, source return, source or reliance use, or non-view claim kind.

The TEVB decision is conservative. E.17.2 supplies a four-position project-local authoring template, not a current family or importable bundle. Architecture may reuse only exact `U.ViewpointRef` values resolved from a materialized local declaration, with catalogue and member provenance preserved. Architecture-specific structure kinds and candidate-record bindings are defined beside those exact local references rather than mutating their resolved viewpoint epistemes or treating declaration membership as conformance.

### C.30.ASV:11 - SoTA-Echoing

SysML v2 is intentionally excluded from C.30.ASV's SoTA basis. This pattern treats it as a historical dead end rather than a source or lineage and derives no rule from it.

| Practice or source line | C.30.ASV adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| FPF `C.2.1`, `A.22`, `E.17.0`, `C.30`, and `C.30.AD` | Use exact episteme identity, selected-structure discipline, direct viewpoint conformance, architecture relation, and architecture-description boundaries together. | ASV records require one primary selected structure as EntityOfConcern, effective scheme, structure kind, exact viewpoint, obtaining conformance relation, correspondence when used, and admissible use. | A view remains the same episteme about selected structure; no context field, authoring route, or suffix creates it. |
| [Dyad v3 physical-system modeling and analysis](https://help.juliahub.com/dyad/stable/) | Adopt its current integration of physical models, control analysis, SciML surrogates, calibration, and deployment from one source, with both textual and schematic editing. | A generated or edited description still states `viewConstruction`, selected structure, hidden and lost structure, and a source-return condition when action relies on the description. | Executability, simulation, generation, or tool presentation does not create the source episteme, viewpoint-conformance relation, selected structure, evidence sufficiency, gate passage, or assurance. |
| UAF, ArchiMate, C4, and multi-view architecture practice | Adapt viewpoint-library and lightweight diagram communication pressure. C4 contributes communication and zoom pressure only. | C4-like, UAF-like, and ArchiMate-like diagrams can represent or publish ASV epistemes only when exact description identity, EntityOfConcern, structure refs, structure kind, viewpoint conformance, and publication relations are explicit. | Do not import their layer, viewpoint, enterprise taxonomies, structure-kind adequacy, evidence sufficiency, or architecture decision claim without recoverable FPF objects and relations. |
| Systems security engineering, secure-by-design, SSDF, and CSF-style practice | Adopt security as architecture-side structure when trust boundaries, authority, untrusted input, secure defaults, hardening, update channels, and detection and response boundaries change action. | Use `SecurityTrustBoundaryStructure` before evidence, assurance, gate, risk score, or compliance proof. | A security framework, checklist, risk color, or control catalog is not security architecture adequacy, evidence sufficiency, assurance, or gate passage by itself. |
| Theory of Code Space, arXiv:2603.00601 and related code-agent architecture relation-graph probing | Adopt partial-observability, typed relation discovery, invariant discovery, uncertainty reporting, and externalized architecture relation graphs as ASV practice source. | Treat an externalized code-agent relation graph as a diagnostic description, representation, or ASV publication only with observed, inferred, or unknown observation value, evidence pointers, unexplored regions, and typed relation semantics. Add source-return conditions when the intended use relies on hidden distinctions. | Do not mint `U.CodeSpace`; do not treat probe JSON, cognitive-model publication, dependency-F1 result, or diagnostic relation graph as architecture adequacy, internal belief proof, agent authority, safe-code-change authority, assurance, or release authority. |
| GonzoML neural-network architecture discussions | Adopt practitioner operation language for architecture views: block substitution, relation retargeting, dataflow changes, memory placement or cache placement, path-selection or gating, MoE expert-selection, pruning, distillation, NAS, ablation, and compute, memory, or latency tradeoffs. | Use those phrases as recognition cues for changed structure kind, flow relation, module-interface claim kind, security or trust boundary, data-custody relation, preserved and lost structure, affected characteristic, source relation, and the applicable decision or evidence pattern. | Neural-network labels, benchmarks, ablations, pruning masks, block, layer, router, cache, or state labels, or search outputs do not become FPF ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### C.30.ASV:12 - Relations

Builds on: `C.30.P`, `C.30`, `A.1`, `A.22`, `C.2.1`, `E.24.PUB`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `A.7`, `E.10.D2`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `E.18`, `C.29`, `C.16`, `C.25`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.32.P2S`, `C.32`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `C.33`, `C.34`, and `C.35` when problem-to-structure carry-through, candidate-set, architecture-decision, ADR-projection, decision-adequacy, capture, preservation, or generated-carrier claim kinds are being made. Use `A.6.M` when a module-interface claim is being made, and separately identify the admitted module or allocation relation required by that claim.

Use these patterns for the other claims: `C.30` for direct architecture relations, bounded architecture claims, and selected-structure adequacy; `A.1` for the exact described holon; `A.22` for selected-structure identity; `C.2.1` for description episteme identity; `E.17.0` for exact viewpoint conformance; `E.24.PUB` for publication occurrence, form, and carrier; `C.29` for representation and mathematical-lens use; `C.33` for captured and lost selected structure in a view; `C.34` for preservation or correspondence between a view and another structure-bearing object; `C.35` for generated or discovered carriers before candidate admission; `E.18` for selected transformation-flow structure, transformation-flow path, and crossing discipline; `E.18.2` for mathematical graph descriptions; `C.16` for characterization; `C.25` for Q-Bundles; `C.28` for causal use; `A.10` for bounded source-to-use reliance; `G.6` for citable provenance paths; `B.3` for named assurance; `A.20` for internal-constraint validity; `A.21` for gate decisions and the applicable domain pattern for release; `A.15` for Work alignment and `A.15.6` for project-Work recovery, with project-use relations supplied by their own defining patterns; `C.11` for decisions; and `C.32.P2S` for problem-to-structure carry-through when the view is one captured or lost-structure stage. `C.30.ASV` covers structural-view adequacy for the selected structure being viewed.

### C.30.ASV:End

