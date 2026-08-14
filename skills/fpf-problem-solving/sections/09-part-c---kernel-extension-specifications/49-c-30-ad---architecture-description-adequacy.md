## C.30.AD - Architecture Description Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-description adequacy.

**Intent.**
Keep an architecture description useful without letting the description, view, diagram, publication, or tool publication face become the architecture itself.

**Builds on.** `C.30`, `C.30.ASV`, `A.1`, `A.22`, `E.24.PUB`, `A.7`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, `C.2.P`, `E.10`, and `E.10.ARCH`.

**Coordinates with.** `C.30.AD.BA`, `C.30.P`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `A.6.3.NAR`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `A.6.F`, `A.6.M`, `C.29`, `C.16`, `C.16.P`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `A.15.5`, `C.11`, `C.28`, `E.8`, `E.10.MOVE`, `E.11.PUR`, `E.24.CD`, and `F.18`.

### C.30.AD:0 - Use this when

Use this pattern when current work must create, inspect, compare, reuse, or rely on a durable architecture-description episteme, a multi-view description set, a generated architecture-relation view, or a specification-use record. Open it only after the practitioner can name the exact described object: one holon, one obtaining `ArchitectureRelation` occurrence, or one exact selected `U.Structure`.

Use `C.30.AD` when the practitioner needs to know:

- which exact holon, architecture-relation occurrence, or selected structure each description episteme is about;
- which architecture claim is being carried or inspected, without substituting that claim for the description's EntityOfConcern;
- which selected structures or architecture structure kinds are described;
- which descriptions qualify as `U.View` under which exact `U.Viewpoint` epistemes and independently obtaining `EpistemeViewpointConformanceRelation` occurrences;
- which cross-view correspondence claims, source-to-use paths, source-return conditions for stronger use, freshness boundaries, and specification-use boundaries make the description usable;
- what the description can guide and which uses are non-admissible.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, file, or architecture model starts acting as architecture, selected structure, `U.View`, proof, gate, assurance, decision, work authorization, or release authorization by presentation alone.

**What this buys.** The practitioner can keep architecture descriptions inspectable across exact subjects, views, viewpoints, selected structures, cross-view correspondence claims or separately governed relations, source-to-use paths, applicable source-return conditions, representations, publications, and subject pattern applications.

**First useful description-use output.** Write one `ArchitectureDescriptionUseCard@Project`:

```text
ArchitectureDescriptionUseCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact description-use or work-use pattern
  architectureDescriptionRef?: U.EpistemeRef constrained to ArchitectureDescription
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  )
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim)
  claimScope?: U.ClaimScope, byValue
  concernRefs?: FinSet(U.EntityRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)
  descriptionPurpose:
  selectedStructureRefs: FinSet(U.StructureRef)
  structureKindRefs: FinSet(ArchitectureStructureKindRef)
  viewpointRefs?: FinSet(U.EpistemeRef constrained to U.Viewpoint)
  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?:
  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier)
  specificationUseBoundary?:
  admissibleUse:
  nonAdmissibleUse:
  firstGoverningPatternApplication?:
```

`@Project` is a compatibility and retrieval cue for a project-side use card. The suffix supplies no project identity, authority, context, viewpoint, parthood, or work occurrence. When one actual project matters, `projectWorkOccurrenceRef` identifies the composite `U.Work` recovered under `A.15.6`, and `architectureDescriptionProjectUseRelationRef` identifies the exact obtaining relation by which this description use concerns that work. Name that relation's subject pattern; the reference to work alone does not establish project locality.

The card is a controlled first-pass slice, not an identity constructor. It can close ordinary use only when it names one exact EntityOfConcern, the effective `U.ReferenceScheme`, one usable description purpose, the selected structures and their structure-kind classifications, admissible use, non-admissible use, and one remaining architecture candidate use or subject pattern application. If it calls the description a `U.View`, it also names the exact viewpoint episteme and the separately obtaining conformance relation. Expand to the fuller `ArchitectureDescription` record when cross-view correspondence, source use, a stronger-use source-return condition, freshness, specification use, regulated use, comparison, publication, representation, or project-side authority use is current.

**Not this pattern when.**

- If the current use is a grounded architecture claim, an obtaining `ArchitectureRelation`, or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view and its viewpoint-conformance test, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a representation, publication occurrence, publication face, publication form, report, dashboard, file, carrier, source-expression relation, or publication-currentness relation, use `C.2.P`, `E.17`, `E.24.PUB`, or the direct representation, publication, or source-use pattern governing the claim.
- If the description is being used as pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and apply the direct pattern governing that claim to the claim being made.

### C.30.AD:1 - Problem frame

Architecture practice needs durable descriptions: multi-view documents, view models, generated relation graphs, architecture transformation-flow views, LCA control sketches, module or interface diagrams, deployment views, model cards, system cards, and architecture decision description sets. These descriptions let teams compare, reuse, refresh, inspect, and use architecture claims across viewpoint families and working concerns. When the project also claims a system-role assignment, Work attribution, authority, or responsibility, each remains a separate object: use A.2.1 and F.6 for assignment and Work, and an admitted direct domain predicate or exact A.6.RCD missing governor for responsibility. `VP.AllocationResponsibility` is only a viewpoint cue.

The difficulty is that a description is not the architecture, an obtaining architecture relation, or its selected structure. The same holon and architecture-relation occurrence can have several descriptions. A description set can contain several separately identified epistemes. One such episteme is a `U.View` only while an exact `EpistemeViewpointConformanceRelation` obtains between that same episteme and one exact viewpoint episteme. Each view can hide, lose, coarsen, or emphasize different structure. A view can describe functional structure, flow or transformation-flow structure, control structure, module or interface structure, placement structure, information custody, evidence-reuse relation, assurance relation, scale or coarsening relation, or another declared architecture-relevant structure.

The first-minute practitioner can ask:

- What exact holon, obtaining `ArchitectureRelation` occurrence, or selected structure is this description episteme about?
- What exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme` keep that episteme identifiable?
- Which selected structures or structure kinds does this description carry?
- Which exact viewpoint episteme and conformance relation, if any, make this same episteme a `U.View`?
- What correspondence connects this description to architecture claims and other view epistemes without inventing a subject relation?
- Which source episteme, source view, representation, or publication enters this use through which source-to-use path, and what stronger use would activate a source-return condition?
- What admissible architecture move remains after the description has been used?

### C.30.AD:2 - Problem

How can FPF govern architecture descriptions without:

- treating a description, model, view, diagram, graph, card, table, dashboard, file, publication occurrence, publication form, carrier, or rendering as the architecture, an obtaining relation, or a selected structure;
- treating all architecture documentation as one generic description with no exact EntityOfConcern or selected-structure recovery;
- granting `U.View` membership because an episteme was authored, constructed, queried, selected, bundled, diagrammed, or published;
- losing the link between one exact viewpoint episteme, the five-part conformance predicate, and the architecture structure kind being described;
- letting one attractive view hide lost structure, stale source, or missing correspondence;
- letting publication quality become empirical grounding, evidence sufficiency, assurance, gate passage, decision claim, work completion, or release authorization;
- making ordinary architecture triage too heavy for a first useful architecture move.

### C.30.AD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful description vs architecture overread | A good description guides architecture work, but it is not the architecture, an obtaining `ArchitectureRelation`, selected structure, decision claim, proof, or release authorization. |
| Multi-view richness vs exact episteme identity | Several descriptions can be needed, but each keeps its exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme`; a description set does not blur those identities. |
| Viewpoint utility vs automatic view membership | A viewpoint helps a role or practice inspect an architecture, but only the independently obtaining E.17.0 conformance relation makes the same episteme a `U.View`; a viewpoint label or bundle does not. |
| Viewpoint utility vs viewpoint-as-kind collapse | Viewpoints do not choose the selected structure kind; `C.30.ASV` or another governing structural-view pattern keeps viewpoint conformance and structure-kind recovery separate. |
| Reuse vs freshness | A reused architecture description names its source-to-use path and applicable source or structure edition. A source-return condition is added only when stronger use must return to a named source or the exact defining or constraining ClaimGraph. |
| Specification-use vs representation and publication | A description can be used as a specification, but specification use is a bounded use of an episteme or publication; it is not the diagram, publication occurrence, publication form, carrier, architecture, or project Work. |
| Thin C.30 bridge vs full description mechanism | C.30 keeps the obtaining architecture relation and selected structure central; the rule content located here defines the heavier description mechanism when durable description use is being asserted. |

### C.30.AD:4 - Solution

Use `ArchitectureDescription` when current work must create, inspect, or rely on a C.2.1 `U.Episteme` about exactly one architecture-side EntityOfConcern: one holon, one obtaining `ArchitectureRelation` occurrence, or one exact selected `U.Structure`. The episteme keeps the C.2.1 identity triple `<exact ClaimGraph, one exact EntityOfConcern, effective U.ReferenceScheme>`. An `ArchitectureClaim` can be cited as carried claim content or trace, but the claim record is not automatically the description's EntityOfConcern and does not replace the described subject.

Keep `ClaimScope`, empirical grounding, concern, viewpoint, view membership, selected model-use structure, representation, publication occurrence, publication form, carrier, project Work, and project-use relation outside that identity triple. Add each only when it independently applies. `modelUseStructureRef` is optional and appears only when an actually selected DDD model-use structure changes interpretation or selection.

`C.30.AD` does not mint `U.Architecture`, does not redefine `U.Viewpoint`, and does not replace generic Description, view, representation, publication, or publication-form machinery. It specializes those objects for architecture-description use while keeping every selected architecture-relevant structure directly recoverable.

Built-asset architecture-description, BIM, IFC, asset-information, digital-twin, and ISO/IEC 81346 reference-designation detail is governed by `C.30.AD.BA`. C.30.AD keeps the general architecture-description bridge and does not absorb that built-asset specialization.

#### C.30.AD:4.1 - Architecture-description record

```text
ArchitectureDescription ::= U.Episteme & {
  architectureDescriptionRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  ),
  effectiveReferenceScheme: U.ReferenceScheme, byValue,

  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  selectedStructureRefs: FinSet(U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  claimScope?: U.ClaimScope, byValue,
  concernRefs?: FinSet(U.EntityRef),
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef),

  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView),
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef),
  descriptionSetUseClaimRefs?: FinSet(U.EpistemeRef),
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),

  sourceEpistemeRefs?: FinSet(U.EpistemeRef),
  sourceViewRefs?: FinSet(U.ViewRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  sourceReturnCondition?,
  freshnessClaimRefs?: FinSet(U.EpistemeRef),

  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  specificationUseBoundary?,
  publicationUseBoundary?,
  admissibleUse,
  nonAdmissibleUse
}
```

The record identifies one episteme, not a document container. Its one `entityOfConcernRef` is supplied directly and is never derived merely from an architecture-claim field. When the EntityOfConcern is an architecture-relation occurrence or selected structure, participant traces can still recover its holon without changing episteme identity. `architectureClaimRefs` carries relevant claim content or trace only. `selectedStructureRefs` names the architecture-relevant structures described by the claim graph, while `structureKindRefs` classifies those structures.

Minimum conformance for the record:

- the exact claim graph, one exact EntityOfConcern, and effective `U.ReferenceScheme` are all present;
- actual architecture-relation references identify independently obtaining `ArchitectureRelation` occurrences; required, desired, expected, candidate, unresolved, or negative architecture content stays claim content;
- `selectedStructureRefs` names the architecture-relevant structures being described, and `structureKindRefs` classifies those selected structures;
- any cited `ArchitectureStructuralView` is the same description episteme admitted as `U.View` only by a separately obtaining E.17.0 conformance relation to one exact viewpoint episteme;
- cross-view composition uses explicit description-set use claims, correspondence claims, or independently obtaining relations; source use names source-to-use paths; a source-return condition appears only when stronger use requires return to a named source or exact defining or constraining ClaimGraph;
- representation and publication fields identify their own objects and occurrences; they do not establish the description, architecture, selected structure, view membership, empirical grounding, or truth;
- `admissibleUse` and `nonAdmissibleUse` say what the description can and cannot carry.

#### C.30.AD:4.1a - Traceable architecture multi-view description chain

A full architecture description is traceable only when the reader can recover the chain that makes a view useful without turning the view into the architecture or letting a list create view membership. The chain is a trace requirement, not a prescribed method or work plan:

```text
workingConcernRef
-> exact viewpoint episteme
-> independently obtaining EpistemeViewpointConformanceRelation
-> the same ArchitectureDescription episteme admitted as U.View
-> exact entityOfConcernRef
-> selectedStructureRef and, when actual, ArchitectureRelationOccurrenceRef
-> optional ArchitectureClaimRef
-> ArchitectureDescriptionUseCard or multi-view description-set use claim
-> admissibleArchitectureMove or subject-pattern application
```

When allocation or responsibility is current, add the exact direct relation separately. A system-role kind or assignment can support the work context but does not establish responsibility; `VP.AllocationResponsibility` only helps recognize the concern. When a source episteme or source view is used, a source-to-use path joins it to the view or description. Representation adds its own representation relation or object. Publication adds a publication occurrence with its form and carrier kept distinct. Cross-view use adds a correspondence claim or a direct correspondence relation only when its exact predicate obtains. A source-return condition is added only when a stronger use must return from a derivative or reused expression to a named source or exact defining or constraining ClaimGraph.

`E.17.0` carries the generic viewpoint-conformance test and the rule that the same episteme is a `U.View` iff the direct relation obtains. `C.30.ASV` carries selected-structure and architecture-view adequacy. `C.30.AD` carries the architecture-specific composition and use boundary: which exact objects each description is about, which structural views it uses, which correspondence claims or relations connect them, which source-to-use paths support source use, which stronger uses activate a source-return condition, and which architecture move or subject-pattern application remains admissible.

If any link in the chain is absent, do not fill it with a documentation label, query result, bundle membership, diagram, file, or publication. Either add the missing exact reference or independently obtaining relation, reduce the admissible use, or apply the subject pattern that can recover it.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

An architecture description episteme is not a `U.View` because it is put in a multi-view set, authored under a viewpoint label, constructed by A.6.3, returned by a query, selected, bundled, diagrammed, rendered, or published. First identify the candidate episteme by its C.2.1 identity. Then identify one exact viewpoint episteme and test the fixed five-part E.17.0 predicate. Only a separately obtaining `EpistemeViewpointConformanceRelation(candidateEpisteme, exactViewpoint)` admits that same episteme as `U.View`.

When a receiving use needs one multi-view description set, recover an exact collection of independently identified description epistemes under `C.13`; set membership is ordinary collection membership. A shared file, bundle, heading, graph, publication, or query result neither identifies that collection nor grants `U.View` membership. The collection keeps no second episteme identity for its members.

`C.30.AD` can record use of already recoverable architecture structural views inside one description set without minting a local relation kind:

```text
ArchitectureDescriptionViewUseClaim ::= U.Episteme & {
  claimGraph: {
    architectureDescriptionSetRef,
    usedArchitectureStructuralViewRef,
    usePurpose:
      orientation | comparison | implementationGuidance |
      assuranceInput | sourceUse | strongerUseReturn | declaredOther,
    correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef),
    sourceToUsePathRefs?: FinSet(U.RelationRef),
    sourceReturnCondition?,
    admissibleUse,
    nonAdmissibleUse
  },
  entityOfConcernRef: exactly one architectureDescriptionSetRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

The use claim does not grant `U.View` membership and does not make its view, set, viewpoint, or selected structure obtain. Each `usedArchitectureStructuralViewRef` must already identify the same description episteme whose exact E.17.0 conformance relation obtains. Use `C.30.ASV` when the current question is whether the episteme has the right selected structure, structure kind, exact viewpoint, conformance relation, hidden or lost structure note, source-to-use path, or source-return condition activated by stronger use. Use `A.22` when the current question is structure as such. Use `C.30` when the current question is an obtaining architecture relation or grounded architecture claim. Use `C.30.AD` only for description identity, description-set use, cross-view correspondence, source use, an applicable source-return condition, freshness, specification use, publication use, or the remaining architecture candidate-use boundary.
Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` plus `C.30.TFS-REL` when the selected transformation-flow structure, path, crossing, valuation, or graph-shaped mathematical description is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Boundary, interface, or Markov-blanket view | `A.1`, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `C.26`, `C.26.3`, and `C.29` according to the recovered claim; `A.6.B` only when the recovered object is L, A, D, or E statement classification inside a boundary package. `C.30.AD` records only exact description identity, description-set use, cross-view correspondence, source-to-use path when a source is used, an applicable stronger-use return condition, freshness, representation, or publication use. |
| Evidence or assurance reuse view | `A.10`, `B.3`, or assurance or evidence pattern governing the claim for the non-architecture claim. |
| Architecture residual view | `C.30.ILC` governs a cross-scope or interlevel architecture residual. C.30.AD records only the residual view's exact episteme identity, conformance, description-set use, correspondence to other views, and declared use boundary; source-use relations are added only when such a source is actually used. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | Use `C.32.MLAO` for the residual-reducing multilevel candidate frame, `C.32` for the candidate architecture palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. Record with C.30.AD only the exact description identity, description-set use, cross-view correspondence, source-to-use path when used, applicable source-return condition, freshness, representation, publication use, or specification use. |

#### C.30.AD:4.3 - Cross-view correspondence, source use, and return conditions

Architecture descriptions become risky when a reader cannot tell whether two view epistemes concern the same holon, the same architecture-relation occurrence, the same selected structure, related structures, or different EntitiesOfConcern. A description set therefore carries explicit correspondence claims or references an independently admitted direct correspondence relation. Merely placing two views in one file, model, list, or publication creates neither correspondence nor shared identity. Use source-to-use paths when source epistemes, views, generated outputs, representations, or publications enter current use. Add a source-return condition only when stronger use requires return from a derivative or reused description to a named source or exact defining or constraining ClaimGraph.

```text
ArchitectureDescriptionCorrespondenceClaim ::= U.Episteme & {
  claimGraph: {
    architectureDescriptionSetRef,
    fromViewRef,
    toViewRef,
    correspondenceKind:
      sameDescribedHolon | sameArchitectureRelationOccurrence |
      sameSelectedStructure | refinement | abstraction | projection |
      sourceDerived | conflict | declaredOther,
    preservedStructureRefs?,
    lostStructureRefs?,
    directCorrespondenceRelationRefs?: FinSet(U.RelationRef),
    sourceToUsePathRefs?: FinSet(U.RelationRef),
    sourceReturnCondition?,
    admissibleUse,
    nonAdmissibleUse
  },
  entityOfConcernRef: exactly one architectureDescriptionSetRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

This local record is claim content and does not itself instantiate a world-side correspondence relation. A `directCorrespondenceRelationRef` is affirmative only when the exact correspondence predicate is defined, current facts satisfy it, and the occurrence independently obtains. Correspondence is not proof, empirical grounding, assurance, gate passage, shared EntityOfConcern, or architecture identity; it lets a reader use more than one view without silently changing what each episteme is about.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness claim only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment state, or an external condition. Keep this bounded claim distinct from any publication-currentness relation:

```text
ArchitectureDescriptionFreshnessClaim ::= U.Episteme & {
  claimGraph: {
    sourceEditionRefs,
    structureEditionRefs?,
    modelOrToolEditionRefs?,
    knownRefreshTrigger:
      sourceChange | deploymentChange | interfaceChange |
      controlRateChange | modelEditionChange | evidenceDecay |
      toolApiChange | regulatoryChange |
      incidentFinding | declaredOther | unknown,
    admissibleUseUntil?,
    sourceReturnCondition?
  },
  entityOfConcernRef: exactly one ArchitectureDescriptionRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue
}
```

A freshness claim carries a source-return condition only when a stronger use must return to a named source or exact defining or constraining ClaimGraph. It does not make the description empirically grounded, evidence-sufficient, true, or publication-current; it only bounds current use of the exact description episteme under the stated scheme.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a bounded use of an exact description episteme or of one of its publications.

```text
ArchitectureDescriptionSpecificationUse@Project ::= {
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work,
  architectureDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact specification-use or work-use pattern,
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription,
  sourceEpistemeRef?: U.EpistemeRef,
  sourceViewRef?: U.ViewRef,
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  representationRef?: U.EntityRef,
  publicationOccurrenceRef?: EpistemePublicationRelationRef,
  publicationFormRef?: U.EntityRef,
  carrierRef?: U.EntityRef constrained to U.PresentationCarrier,
  governedUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther,
  subjectPatternLocator?: U.EntityRef, referencing one subject-pattern U.MethodDescription,
  admissibleUse:
  nonAdmissibleUse:
}
```

The two project fields preserve the ordinary boundary: `projectWorkOccurrenceRef` identifies an actual composite `U.Work`; `architectureDescriptionProjectUseRelationRef` identifies a separately obtaining project-use relation under its subject pattern. Neither a project label nor this use record creates that Work or relation.

If specification use becomes pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, performed work, work authorization, decision claim, causal-use claim, or release authorization, apply the direct pattern governing that claim to the claim being made. The architecture description remains the description boundary, not the governing claim.

Keep the description episteme, its possible `U.View` membership, diagram or other representation, publication occurrence, publication form, and carrier distinct. Authoring, construction, querying, selection, bundling, rendering, filing, or publication creates none of the subject-side architecture relation, selected structure, description truth, empirical grounding, project Work, or project-use relation by itself.

#### C.30.AD:4.6 - Subject pattern applications

| Question after the architecture-description boundary is clear | FPF application |
| --- | --- |
| Grounded architecture claim, selected structures, first architecture move | `C.30` |
| Recommended FPF pattern use after reading the description | `E.11.PUR` |
| Work-entry readiness or full-kit condition for intended architecture work | `A.15.5` |
| Architecture or structure wording is still overloaded | `C.30.P` |
| Architecture structural view or structure-kind and viewpoint relation | `C.30.ASV` |
| Transformation-flow relation or graph description used by architecture | `C.30.TFS-REL` and `E.18` |
| Control structure view | `C.30.LCA` |
| Cross-scope or interlevel architecture residual, conflict, or frustration in the described holon | `C.30.ILC` |
| Multilevel-learning or frustration mathematical-lens result with recoverable level mapping or scale mapping and preserved structure and lost structure | `C.29` with the admitted C.29-local lens output |
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `C.32.MLAO` for the residual-reducing frame, `C.32` for the candidate palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or pool treatment, `G.5` for selected-set result declaration, `C.11` for final local choice, and measurement patterns named by value when those claims are being made |
| Generic description, view, viewpoint, publication, publication form, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or quality pattern governing the claim |
| Evidence, assurance, gate, work planning, performed work, local choice, project architecture decision, causal-use, release | `A.10`, `B.3`, `A.20`, `A.21`, `A.15.2`, `A.15.1`, `C.11`, `C.32.PAD`, `C.28`, release or admissibility pattern, or subject pattern |

#### C.30.AD:4.6a - Candidate, front, and selected-set description boundary

An architecture description can also carry claims about a project architecture decision or selected structures cited by an ADR-like publication. Use `C.32.PAD` for the project architecture decision relation, `C.32.ADR` for publication projection of an architecture-decision description, and `C.32.ADA` for adequacy of that decision for a declared use. C.30.AD keeps only the exact description identity, possible E.17.0 view conformance, description-set use claims, cross-view correspondence claims or governed relations, source-to-use paths when sources are used, applicable source-return conditions, freshness, representation, publication use, and specification use.

An architecture description may carry claim content about an archive, front, selected set, candidate palette, local choice, or planned architecture move. That does not make the description an archive or front relation, selector, choice rule, pattern-use recommendation, work-entry readiness relation, work authorization, or deontic permission. Use `C.32.MLAO` for residual-reducing multilevel candidate frames, `C.32` for candidate architecture palettes, `C.18` for archive and front relations, `C.19` for current-pool treatment, `G.5` only for selected-set result declaration, `C.11` for local choice, `C.30` for the architecture move, `C.30.ASV` for selected-structure view triage, `E.11.PUR` for recommended pattern use, `A.15.5` for work-entry readiness, and the A.15 family for planning or performed Work. If the content is published, use `E.17` for a source-backed publication face and return to source and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. The C.30.AD record still identifies the architecture description and its declared publication use.

For an architecture-description claim, record exact episteme identity plus only the view conformance, description-set use, viewpoint, cross-view correspondence, source-to-use path, applicable stronger-use return condition, freshness, representation, publication use, and specification use that actually apply. If the current source claim only grounds a first architecture move, require `C.30`. If it synthesizes alternatives, use `C.32` or `C.32.MLAO` according to the residual frame. If it changes which variants are archived, kept in a pool, compared, selected, published, locally chosen, or decided, require the pattern that defines or constrains that relation.

### C.30.AD:5 - Archetypal Grounding (Worked Cases)

| Case | C.30.AD treatment |
| --- | --- |
| "The architecture is documented in this view set." | Treat the set as a package of separately identified architecture-description epistemes only if each has an exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme`. A member is a `U.View` only with its exact viewpoint episteme and independently obtaining E.17.0 conformance relation. The set is not the architecture, relation occurrence, or selected structure. |
| A transformation-flow graph expression is included in an architecture document. | Use `E.18` for graph, path, and crossing semantics and `C.30.TFS-REL` when the graph is used by architecture. `C.30.AD` records the exact description and its path from the source expression into that use; add a source-return condition only if a stronger use must return to the named source or exact defining or constraining ClaimGraph. The graph expression or rendering creates no actual transformation. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card publishes or represents a description episteme about an exact architecture-side object. Safety assurance uses `B.3`; evidence uses `A.10`; release uses `A.21`. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated representation or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TFS-REL` only when an exact architecture structural view or flow relation is being used. Generation and display establish neither relation occurrence nor view membership. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Identify every description episteme separately, including its EntityOfConcern and scheme. Each cited view also names its exact viewpoint and obtaining conformance relation; an `ArchitectureDescriptionViewUseClaim` records set use without minting membership. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records exact description identities, view conformance, description-set use, and correspondence among views. Use `C.30.LCA` for the control view and `A.10`, `G.6`, or `B.3` for evidence or assurance. If a system-role assignment, F.6 Work attribution, authority, allocation, or responsibility is claimed, cite its separate direct relation; otherwise record the exact missing governor. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records exact description epistemes, architecture claims carried as content, structural views, and source-to-use paths for reused views. A source-return condition is added only when a product-specific use exceeds the declared reuse boundary. `A.6.M` normalizes module-interface claims and routes any proposed direct relation; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting frame are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records description-set use, correspondence, and each view's declared use boundary. `C.30.ILC` governs the residual; `C.29` is used only if the description contains a recoverable level mapping or scale mapping with preserved structure and lost structure. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | Record with `C.30.AD` only the exact description or publication use of that comparison. Use `C.32.MLAO` for residual-reducing frames, `C.32` for candidate palettes, `A.19.CPM` or `A.19.SelectorMechanism` for comparison and selector-policy use, `C.18` or `C.19` for archives, fronts, and current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. For a measurement claim, use the pattern that defines or tests the measured characteristic and result. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | The exact architecture-description episteme can be the one EntityOfConcern for that second-description use. Govern the second description as its own `U.Episteme` and name any source-to-use, representation, publication, review, or evaluation relation directly. Keep the chain to the first description's exact EntityOfConcern visible without treating either description as architecture, residual, decision, or proof. |

### C.30.AD:5.1 - Bias-Annotation

| Bias | How C.30.AD prevents it |
| --- | --- |
| Description-as-architecture bias | `ArchitectureDescription` is a C.2.1 episteme about one exact holon, architecture-relation occurrence, or selected structure; it does not become that object or create it. |
| View-as-structure bias | The same description episteme is a `U.View` only through an independently obtaining E.17.0 conformance relation to one exact viewpoint. `C.30.ASV` governs selected-structure adequacy; C.30.AD records description-set use and correspondence without minting membership. |
| Publication-as-authority bias | Representation, publication occurrence, publication form, carrier, dashboard polish, model-card form, or report label does not establish description truth, empirical grounding, evidence, assurance, gate, decision, work authorization, or release authorization. |
| Freshness-as-evidence bias | A freshness claim bounds admissible use; it does not make the description evidence-sufficient or publication-current. |
| Semio-bias in architecture work | `C.30` governs obtaining architecture relations, exact selected structures, and architecture claims. `C.30.AD` opens when work must create, inspect, or rely on an exact description episteme with its own ClaimGraph, one EntityOfConcern, and effective `U.ReferenceScheme`. |

### C.30.AD:6 - Conformance checklist

| Check | Condition to establish | Repair if failed |
| --- | --- | --- |
| **CC-C30AD-1 Episteme identity.** | Every architecture description has one exact claim graph, one exact EntityOfConcern—holon, obtaining `ArchitectureRelation` occurrence, or selected structure—and an effective `U.ReferenceScheme`. | Add the missing C.2.1 identity component or use `C.30`/`A.22` until the subject-side object is recoverable. |
| **CC-C30AD-2 Subject and holon recovery.** | The one EntityOfConcern is supplied directly. If it is an architecture-relation occurrence or selected structure, its participant trace recovers the exact holon without copying that holon into description identity; architecture-claim refs remain optional content or trace. | Restore the exact EntityOfConcern and participant trace; remove derived identity from an optional architecture-claim field. |
| **CC-C30AD-2a Traceable multi-view chain.** | The description use recovers working concern, exact viewpoint episteme, obtaining conformance relation, same episteme as `U.View`, one EntityOfConcern, selected structure, optional actual architecture relation, description-set use, and remaining admissible architecture move. When allocation, responsibility, source use, representation, publication, cross-view correspondence, project use, or a source-return condition activated by stronger use is current, its direct object or relation is added separately. A responsibility claim names its direct domain predicate and actual participants or the exact missing governor; assignment and viewpoint supply neither responsibility nor authority. | Add the missing exact object or direct relation, reduce admissible use, or apply the subject pattern that can recover it. |
| **CC-C30AD-3 Viewpoint and structure kind.** | Every asserted architecture structural view identifies the candidate episteme, exact viewpoint episteme, independently obtaining five-part E.17.0 conformance relation, selected structure, and structure kind. | Use `E.17.0` and `C.30.ASV` before relying on the view; a label, query, bundle, diagram, or publication is insufficient. |
| **CC-C30AD-4 Correspondence and source use.** | Cross-view use names a correspondence claim or independently obtaining relation; source-derived or reused use names its source-to-use path; a source-return condition is present only when stronger use opens return to the named source or exact defining or constraining ClaimGraph. | Add the missing claim or direct relation, or narrow the admissible use. |
| **CC-C30AD-5 Representation and publication boundary.** | Diagram, rendering, publication occurrence, publication form, dashboard, card, file, or carrier is not treated as architecture, selected structure, `U.View`, description truth, decision claim, evidence, assurance, gate passage, performed work, work authorization, or release authorization. | Assign representation, publication, or source use to `C.2.P`, `E.17`, `E.24.PUB`, or its subject pattern and assign every non-description claim to its subject pattern. |
| **CC-C30AD-6 Specification-use boundary.** | Specification use identifies the exact description episteme or publication. Actual project locality additionally names one composite `U.Work` and a separately obtaining project-use relation; subject pattern applications remain explicit for non-description claims. | Add the exact description, Work, and direct use relation as applicable, or demote to ordinary description use. |
| **CC-C30AD-7 Remaining architecture candidate use.** | The description under its declared use boundary still identifies the next architecture move, view normalization, source-to-use repair, applicable source-return condition, or subject-pattern application. | Add the remaining architecture candidate use or reduce the record to source, representation, or publication use. |

### C.30.AD:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description-as-architecture | A document, diagram, model, graph, view set, or card is said to be the architecture or to create an obtaining architecture relation. | Recover the exact holon, `ArchitectureRelation` occurrence, or selected structure; keep the episteme, representation, publication, and source-to-use relation distinct. |
| Viewpoint-as-structure-kind or view constructor | A stakeholder, role, concern, viewpoint label, authoring template, query, or bundle is used as if it named the selected structure or granted `U.View` membership. | Use `E.17.0` for exact viewpoint conformance and `C.30.ASV` for selected structure and kind. |
| Multi-view fog | Many views are listed, but no one can tell their separate C.2.1 identities, conformance relations, selected structures, or correspondence. | Add exact description and viewpoint refs, conformance refs, selected-structure refs, and correspondence claims or governed relations. |
| Specification-as-authority | A specification-looking architecture description is used as performed work, gate passage, decision claim, assurance, evidence, work authorization, or release authorization. | Declare specification use and apply the direct pattern governing that claim to the claim being made. |
| Freshness laundering | A recently generated diagram is treated as adequate because it is current. | Record the bounded freshness claim, source edition, and refresh trigger; do not treat currentness as adequacy, evidence, grounding, or assurance. |
| Architecture-documentation takeover | The pattern spends most of its practitioner guidance on diagrams, publications, and wording guards instead of the architecture relation, selected structures, descriptions, and views. | Keep `C.30` centered on architecture and `C.30.AD` on exact description epistemes and their use; route representation and publication to their subject patterns. |

### C.30.AD:8 - Consequences

Positive consequences:

- Architecture descriptions become reusable without pretending to be the architecture, an obtaining relation, or selected structure.
- Multi-view work can keep each episteme identity, exact viewpoint conformance, selected structures, cross-view correspondence, source-to-use paths, applicable source-return conditions, freshness, representation, publication, and specification use inspectable.
- Description, view membership, representation, publication, empirical grounding, evidence, assurance, gate, decision, Work, project use, release, and mathematical-lens claims stay distinct and return to their subject patterns.
- C.30 can stay focused on architecture while C.30.AD carries the heavier description machinery.

Costs:

- A useful architecture document needs explicit links to exact description epistemes, EntitiesOfConcern, effective schemes, selected structures, and admissible use.
- A claimed view additionally needs the exact viewpoint episteme and independently obtaining E.17.0 conformance relation.
- Reused or regulated descriptions may need correspondence refs, source-to-use paths, source and structure editions, applicable source-return conditions, and freshness claims before they can be relied on.
- Familiar diagrams, files, and publication forms lose implicit authority; grounding, evidence, assurance, gate, decision, and release claims must be established by their own patterns.

### C.30.AD:9 - Rationale

Architecture work needs descriptions, but architecture-description adequacy is not architecture adequacy. A description can guide architecture work only when its own C.2.1 identity and its relation to exact subject-side objects, selected structures, architecture claims, exact viewpoint conformance, other descriptions, source epistemes or views actually used, source-to-use paths, representation, publication, and admissible use are recoverable.

The pattern therefore specializes generic Description and publication machinery for architecture use. It does not mint a new architecture kind, direct subject relation, local view-membership relation, or second meaning of `U.View`; it does not replace `C.30`; and it does not let diagrams or documentation formats establish non-description claims by presentation alone.

### C.30.AD:10 - SoTA-Echoing

| Practice or source line | Source-use relation and currentness | C.30.AD adoption | Action consequence | Boundary |
| --- | --- | --- | --- | --- |
| FPF `C.2.1`, `A.22`, `E.17.0`, `C.30`, and `C.30.ASV` separate episteme identity, selected structures, direct architecture relations, architecture claims, and structural-view adequacy. | Current internal governing line for the exact objects used by this pattern. | Reuse these objects instead of importing a second architecture-description ontology. | Disciplines `C.30.AD:4.1`, `C.30.AD:4.1a`, `C.30.AD:4.2`, `CC-C30AD-1`, `CC-C30AD-3`, and `CC-C30AD-4`: every description has one exact EntityOfConcern and scheme; every asserted view has exact viewpoint conformance; correspondence and source use are explicit. | A description or view remains an episteme and does not become architecture, proof, decision, or release authority. |
| Views-and-Beyond and related architecture documentation practice treats views as stakeholder-relevant projections over architecture. | Mature reference and lineage source for view-based architecture documentation; not used as a mandatory current catalog. | Adopt view usefulness while requiring exact E.17.0 viewpoint conformance and structure-kind recovery through `C.30.ASV`; description-set use remains claim content or a separately governed relation. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.2`, and the multi-view worked case: a view remains useful for a working concern without becoming the selected structure or a `U.View` by label. | No mandatory view catalog or local membership relation is imported, and view adequacy remains in `E.17.0` and `C.30.ASV`. |
| `E.17.0` and MVPK publication machinery in current FPF. | Current internal FPF governing machinery for views, viewpoints, publication occurrences, forms, carriers, and publication separation. | Reuse generic view and publication machinery instead of minting architecture-local copies. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.5`, `CC-C30AD-5`, and `CC-C30AD-6`: architecture-description identity and composition remain separate from representation, publication occurrence, form, carrier, and publication-currentness. | C.30.AD specializes architecture-description use; it does not replace E.17.0, E.17.1, E.17.2, E.17, E.24.PUB, or C.2.P. |
| C4, arc42, ADR, model-card, and system-card practice makes architecture communication practical. | Current practitioner-source family for familiar architecture publication and documentation forms. | Admit these as possible source publications, view publications, decision-description publications, transparency publications, or specification-use records. | Disciplines `C.30.AD:4.5`, worked cases, and anti-patterns: practitioners can use familiar forms while keeping source, representation, publication, description, architecture, evidence, gate, decision, work authorization, release authorization, and other non-description claims separate. | Template, card, graph, or diagram quality is not architecture adequacy by itself. |
| Tool-generated architecture relation graphs and code-agent architecture probing expose useful but partial structure. | Emerging practitioner practice for recovering architecture-relevant relations from code, models, and generated analyses; currentness depends on the analyzed edition and tool run. | Treat generated graphs as representations or source-derived descriptions with observed, inferred, and unknown relation boundaries. | Disciplines `C.30.AD:4.3`, `C.30.AD:5`, and `CC-C30AD-4`: a generated output can guide structure recovery and next architecture moves only through a named source-to-use path; stronger use activates the declared source-return condition. | Generated relation coverage does not become an obtaining subject relation, `U.View`, proof, gate passage, safety assurance, or complete architecture. |

### C.30.AD:11 - Relations

- `C.2.1` governs the exact identity of every architecture-description episteme.
- `C.30` governs obtaining architecture relations, selected-structure adequacy, and bounded architecture claims.
- `C.30.P` normalizes overloaded architecture or structure wording before this pattern is used.
- `C.30.ASV` governs architecture structural-view adequacy, while `E.17.0` alone admits the same episteme as `U.View` through exact viewpoint conformance.
- `C.33` governs capture and loss of selected structure when an architecture description, generated relation graph, ADR-like record, or view set carries only part of the architecture content for a declared use.
- `C.34` governs preservation or correspondence adequacy when the architecture description is being compared with another view, source model, generated output, candidate, or realized structure.
- `A.6.3.NAR` governs a reader-facing narrative rendering made from an architecture description, description set, view set, or architecture-decision route. `C.30.AD` governs architecture-description adequacy; `A.6.3.NAR` governs only the structure-to-sequence relation, selected-source carry-through, lost structure, reader-use boundary, and applicable source-return condition.
- `C.30.TFS-REL`, `C.30.LCA`, and `C.30.ILC` govern architecture structure-relation subcases named by value.
- `C.32.P2S` governs the connected architecturing flow when the description carries only part of selected structure, decision handoff, method expectation, source-to-use continuity, an applicable source-return condition, or actual-structure feedback.
- `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, and `E.24.PUB` govern generic EntityOfConcern, view, viewpoint, representation, publication occurrence, form, carrier, and MVPK machinery.
- `C.2.P` normalizes source-expression, source-to-use, publication-form, and publication-currentness relation-set overreads.
- `E.11.PUR` governs recommended FPF pattern use after an architecture description has been read; C.30.AD only records the description-use boundary.
- `A.15.5` governs work-entry readiness and full-kit condition for intended architecture work; the A.15 family governs Work and project-use relations. C.30.AD records only exact descriptions and their view conformance, description-set use, correspondence, source-to-use paths, applicable source-return conditions, freshness, representation, publication use, and specification use.
- `E.10.MOVE` restores move-like wording when source prose about an architecture description does not mean a C.30 architecture move or a C.30.AD remaining architecture candidate use.

### C.30.AD:End

