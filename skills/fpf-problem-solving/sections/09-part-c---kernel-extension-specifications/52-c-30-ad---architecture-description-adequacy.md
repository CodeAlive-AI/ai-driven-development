## C.30.AD - Architecture Description Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-description adequacy.

**Intent.**
Keep an architecture description useful without letting the description, view, diagram, publication, or tool publication face become the architecture itself.

**Builds on.** `C.30`, `C.30.ASV`, `A.1`, `A.22`, `E.24.PUB`, `A.7`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, `C.2.P`, `E.10`, `E.10.ARCH`, and `E.10.D2`.

**Coordinates with.** `C.30.AD.BA`, `C.30.P`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `A.6.3.NAR`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `A.6.F`, `A.6.M`, `C.29`, `C.16`, `C.16.P`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `A.15.5`, `C.11`, `C.28`, `E.8`, `E.10.MOVE`, `E.11.PUR`, `E.24.CD`, and `F.18`.

### C.30.AD:0 - Use this when

Use this pattern when work must create, inspect, compare, reuse, or rely on an architecture description, a set of such descriptions, a generated view of architecture relations, or a description used as a specification. First name what the description is about: one holon, one `ArchitectureRelation` occurrence that actually obtains, or one selected `U.Structure`.

Use it to answer:

- what architecture-side thing each description is about: a holon, an obtaining architecture-relation occurrence, or a selected structure;
- which architecture claim the description carries or lets the practitioner inspect, without confusing that claim with the thing described;
- which selected structures and structure kinds the description covers;
- whether a description really qualifies as `U.View`: name the viewpoint and show that the E.17.0 conformance relation actually holds;
- how views correspond, which sources enter the use, when a stronger use must return to a source, how fresh the description is, and whether specification use is allowed;
- what the description may guide, what it may not be used for, and what architecture move comes next.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, file, or architecture model is treated as architecture, selected structure, `U.View`, proof, gate, assurance, decision, work authorization, or release authorization merely because it presents those claims.

**What this buys.** A reader can tell what each description is about, how its views correspond, where reused material came from, how fresh it is, what it may be used for, and which other claims need their own patterns.

**First useful description-use output.** In one or two ordinary sentences, say which description is being used, what it describes, which reference scheme gives its terms meaning, why it is being used, which structure matters, what use is allowed, and what architecture move comes next. If you call it a `U.View`, also name the viewpoint and the conformance relation that actually holds. Stop if this answers the question. Keep `ArchitectureDescriptionUseCard@Project` only when the result must be retained, compared, or handed on:

```text
ArchitectureDescriptionUseCard@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef defined by the pattern for the exact relation by which this description use concerns the Work
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
  nextClaimPatternRef?: PatternRef
```

`@Project` is only a retrieval cue. It creates no project, authority, context, viewpoint, parthood, or Work. When an actual project matters, `projectWorkOccurrenceRef` names the composite `U.Work` recovered under `A.15.6`. Include `architectureDescriptionProjectUseRelationRef` only when a named pattern defines how this description use concerns that Work and the relation actually holds. A Work reference alone is not project locality. If locality matters but the relation is not defined, return `missing-governor`; otherwise omit both project-local fields.

The card is optional and does not identify the description. For its declared use, it retains the described thing, reference scheme, purpose, selected structures and their kinds, allowed and disallowed use, and the next architecture move or pattern needed for a separate claim. If it calls the description a `U.View`, it also retains the viewpoint and the conformance relation that actually holds. Use the fuller `ArchitectureDescriptionUseAccount` only when correspondence, source use or return, freshness, specification or regulated use, comparison, publication, representation, or project locality must remain inspectable. Keep any authority claim in its own pattern and relation.

**Not this pattern when.**

- If the current use is a grounded architecture claim, an obtaining `ArchitectureRelation`, or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view and its viewpoint-conformance test, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a representation, publication occurrence, publication face or form, report, dashboard, file, carrier, source-expression relation, or publication-currentness relation, use `C.2.P`, `E.17`, `E.24.PUB`, or the pattern that defines or tests that representation, publication, or source-use claim.
- If the description is being used as a pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and use the pattern that defines or tests the other claim.

### C.30.AD:1 - Problem frame

Architecture practice needs descriptions that remain useful over time: multi-view documents, view models, generated relation graphs, transformation-flow views, control sketches, module or interface diagrams, deployment views, model cards, system cards, and architecture-decision description sets. Teams use them to compare, reuse, refresh, and inspect architecture claims. If a project also claims a system-role assignment, Work attribution, authority, or responsibility, keep that as a separate claim: use A.2.1 for assignment, A.15.1 for Work admission, and F.6 only for assignment-bound Work attribution; use an admitted domain relation for authority or responsibility, or return an A.6.RCD missing governor if a rule needed to state or test that claim is absent. `VP.AllocationResponsibility` is only a clue to the concern.

A description is not the architecture, an architecture relation that actually holds, or the selected structure. The same holon or relation occurrence can have several descriptions, and a description set can contain several separately identified epistemes. A description counts as `U.View` only while the E.17.0 conformance relation actually holds between that same episteme and one viewpoint episteme. Different views can hide, lose, coarsen, or emphasize different structures: for example functional, flow, control, module, interface, placement, information-custody, evidence-reuse, assurance, or scale structure.

The first-minute practitioner can ask:

- What holon, obtaining `ArchitectureRelation` occurrence, or selected structure is this description about?
- Which ClaimGraph, EntityOfConcern, and reference scheme identify the description?
- Which structures and structure kinds does it describe?
- If it is called a `U.View`, which viewpoint and which conformance relation make that true?
- What claim or relation connects it to architecture claims and other views without pretending that proximity creates correspondence?
- Which sources, representations, or publications enter this use, by what path, and when must stronger use return to a source?
- After using the description, what architecture move remains admissible?

### C.30.AD:2 - Problem

How can FPF keep architecture descriptions adequate without:

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
| Viewpoint utility vs automatic view membership | A viewpoint helps a practitioner or practice inspect an architecture, but only the independently obtaining E.17.0 conformance relation makes the same episteme a `U.View`; a viewpoint label or bundle does not. |
| Viewpoint utility vs viewpoint-as-kind collapse | Viewpoints do not choose the selected structure kind. Use `C.30.ASV`, or the pattern for the particular structural view, to keep viewpoint conformance and structure-kind recovery separate. |
| Reuse vs freshness | A reused architecture description names its source-to-use path and applicable source or structure edition. A source-return condition is added only when stronger use must return to a named source or the exact defining or constraining ClaimGraph. |
| Specification-use vs representation and publication | A description can be used as a specification, but specification use is a bounded use of an episteme or publication; it is not the diagram, publication occurrence, publication form, carrier, architecture, or project Work. |
| Thin C.30 bridge vs full description mechanism | C.30 defines the obtaining architecture relation and bounded architecture claim; C.30.AD defines the heavier description-use account only when durable description use is current. |

### C.30.AD:4 - Solution

An `ArchitectureDescription` is the local name for a C.2.1 `U.Episteme` that describes one architecture-side EntityOfConcern: a holon, an obtaining `ArchitectureRelation` occurrence, or a selected `U.Structure`. Use the name only when its ClaimGraph makes that subject, the described structures, purpose, and use boundary recoverable. It remains an episteme identified by `<ClaimGraph, EntityOfConcern, ReferenceScheme>`; it is not a record or a new root kind. A cited `ArchitectureClaim` is content or trace, not automatically the thing described.

Keep `ClaimScope`, empirical grounding, concern, viewpoint, view membership, selected model-use structure, representation, publication occurrence, publication form, carrier, project Work, and project-use relation outside that identity triple. Add each only when it independently applies. `modelUseStructureRef` is optional and appears only when an actually selected DDD model-use structure changes interpretation or selection.

`C.30.AD` does not mint `U.Architecture`, redefine `U.Viewpoint`, or replace generic Description, view, representation, publication, or publication-form machinery. It defines their architecture-description use while keeping every selected architecture-relevant structure directly recoverable.

For built-asset architecture descriptions, BIM, IFC, asset information, digital twins, and ISO/IEC 81346 reference designation, use `C.30.AD.BA`. C.30.AD keeps the general architecture-description bridge and does not absorb that specialization.

#### C.30.AD:4.1 - Architecture-description use account

```text
ArchitectureDescriptionUseAccount:
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  claimGraphRef: exactly one C.2.1 ClaimGraph
  entityOfConcernRef: exactly one of (
    describedHolonRef | architectureRelationOccurrenceRef | selectedStructureRef
  )
  effectiveReferenceScheme: U.ReferenceScheme, byValue

  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim)
  selectedStructureRefs: FinSet(U.StructureRef)
  structureKindRefs: FinSet(ArchitectureStructureKindRef)

  claimScope?: U.ClaimScope, byValue
  concernRefs?: FinSet(U.EntityRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)

  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  descriptionSetUseClaimRefs?: FinSet(U.EpistemeRef)
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)

  sourceEpistemeRefs?: FinSet(U.EpistemeRef)
  sourceViewRefs?: FinSet(U.ViewRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  freshnessClaimRefs?: FinSet(U.EpistemeRef)

  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier)
  specificationUseBoundary?
  publicationUseBoundary?
  admissibleUse
  nonAdmissibleUse
```

The account points to an already constituted episteme; it is not the episteme and does not add slots to it. Its `claimGraphRef`, `entityOfConcernRef`, and `effectiveReferenceScheme` fields expose the ClaimGraph, EntityOfConcern, and reference scheme that identify the episteme. When the described thing is a relation occurrence or selected structure, the participant trace can still recover its holon. `architectureClaimRefs` carries relevant claim content or trace; `selectedStructureRefs` names the structures described, and `structureKindRefs` classifies them.

Minimum conformance for a retained `ArchitectureDescriptionUseAccount`:

- the account resolves to one exact architecture-description episteme and exposes its exact ClaimGraph, one exact EntityOfConcern, and effective `U.ReferenceScheme`;
- actual architecture-relation references identify independently obtaining `ArchitectureRelation` occurrences; required, desired, expected, candidate, unresolved, or negative architecture content stays claim content;
- `selectedStructureRefs` names the architecture-relevant structures being described, and `structureKindRefs` classifies those selected structures;
- any cited `ArchitectureStructuralView` is the same description episteme admitted as `U.View` only by a separately obtaining E.17.0 conformance relation to one exact viewpoint episteme;
- cross-view composition uses explicit description-set use claims, correspondence claims, or independently obtaining relations; source use names source-to-use paths; a source-return condition appears only when stronger use requires return to a named source or exact defining or constraining ClaimGraph;
- representation and publication fields identify their own objects and occurrences; they do not establish the description, architecture, selected structure, view membership, empirical grounding, or truth;
- `admissibleUse` and `nonAdmissibleUse` say what the description can and cannot carry.

#### C.30.AD:4.1a - Traceable architecture multi-view description chain

When a full architecture-description use relies on a view, the reader must be able to recover the chain that makes that view useful without turning the view into the architecture or letting a list create view membership. The chain is a trace requirement, not a prescribed method or work plan:

```text
workingConcernRef
-> exact viewpoint episteme
-> independently obtaining EpistemeViewpointConformanceRelation
-> the same ArchitectureDescription episteme admitted as U.View
-> exact entityOfConcernRef
-> selectedStructureRef and, when actual, ArchitectureRelationOccurrenceRef
-> optional ArchitectureClaimRef
-> architecture-description use (optional ArchitectureDescriptionUseCard) or multi-view description-set use claim
-> admissibleArchitectureMove or pattern needed for a separate claim
```

When allocation or responsibility is current, add the exact direct relation separately. A system-role kind or assignment can support the work context but does not establish responsibility; `VP.AllocationResponsibility` only helps recognize the concern. When a source episteme or source view is used, a source-to-use path joins it to the view or description. Representation adds its own representation relation or object. Publication adds a publication occurrence with its form and carrier kept distinct. Cross-view use adds a correspondence claim or a direct correspondence relation only when its exact predicate obtains. A source-return condition is added only when a stronger use must return from a derivative or reused expression to a named source or exact defining or constraining ClaimGraph.

`E.17.0` tests whether the description is a `U.View`; `C.30.ASV` tests whether it carries the right selected structure and structure kind. `C.30.AD` records how the description is composed and used: what it describes, which views and correspondence it uses, where source material enters, when stronger use must return to a source, and what architecture move or separate claim remains.

If a needed link is absent, do not substitute a label, query result, bundle, diagram, file, or publication. Add the missing reference or relation that actually holds, narrow the allowed use, or use the pattern that defines how to recover it.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

An architecture description episteme is not a `U.View` because it is put in a multi-view set, authored under a viewpoint label, constructed by A.6.3, returned by a query, selected, bundled, diagrammed, rendered, or published. First identify the candidate episteme by its C.2.1 identity. Then identify one exact viewpoint episteme and test the fixed five-part E.17.0 predicate. Only a separately obtaining `EpistemeViewpointConformanceRelation(candidateEpisteme, exactViewpoint)` admits that same episteme as `U.View`.

When a receiving use needs one multi-view description set, recover an exact collection of independently identified description epistemes under `C.13`; set membership is ordinary collection membership. A shared file, bundle, heading, graph, publication, or query result neither identifies that collection nor grants `U.View` membership. The collection keeps no second episteme identity for its members.

`C.30.AD` can record use of already recoverable architecture structural views inside one description set without minting a local relation kind:

```text
ArchitectureDescriptionViewUseClaim content:
  architectureDescriptionSetRef:
  usedArchitectureStructuralViewRef:
  usePurpose:
    orientation | comparison | implementationGuidance |
    assuranceInput | sourceUse | strongerUseReturn | declaredOther
  correspondenceClaimOrRelationRefs?: FinSet(U.EpistemeRef | U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  admissibleUse:
  nonAdmissibleUse:
C.2.1 constitution:
  entityOfConcernRef: exactly one architectureDescriptionSetRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionViewUseClaim` is a C.2.1 episteme about one description set. The block separates what the claim says from the objects that identify it; it does not add slots to the episteme. The claim cannot make anything a `U.View` or make a view, set, viewpoint, or structure obtain. Each referenced view must already satisfy E.17.0. Use `C.30.ASV` to check viewpoint conformance and selected structure, `A.22` for structure itself, and `C.30` for an obtaining architecture relation or grounded architecture claim. Use `C.30.AD` only for description identity and use, cross-view correspondence, source use or return, freshness, specification or publication use, and the remaining architecture move.
Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` for the selected transformation-flow structure, path, crossing, or valuation; `E.18.2` for its graph-shaped mathematical description; `C.30.TFS-REL` when either is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Boundary, interface, or Markov-blanket view | `A.1`, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `C.26`, `C.26.3`, and `C.29` according to the recovered claim; `A.6.B` only when the recovered object is L, A, D, or E statement classification inside a boundary package. `C.30.AD` records only exact description identity, description-set use, cross-view correspondence, source-to-use path when a source is used, an applicable stronger-use return condition, freshness, representation, or publication use. |
| Evidence or assurance reuse view | Use `A.10`, `B.3`, or the relevant evidence or assurance pattern for the non-architecture claim. |
| Architecture residual view | Use `C.30.ILC` for a cross-scope or interlevel architecture residual. C.30.AD records only the view episteme, its conformance, description-set use, correspondence to other views, and allowed use; add a source-use relation only when a source is actually used. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | Use `C.32.MLAO` for the residual-reducing multilevel candidate frame, `C.32` for the candidate architecture palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. Record with C.30.AD only the exact description identity, description-set use, cross-view correspondence, source-to-use path when used, applicable source-return condition, freshness, representation, publication use, or specification use. |

#### C.30.AD:4.3 - Cross-view correspondence, source use, and return conditions

Before combining two views, establish whether they describe the same holon, the same architecture-relation occurrence, the same selected structure, related structures, or different subjects. State that correspondence as a claim or cite a direct relation that actually holds; merely placing views in one file, list, model, or publication creates no correspondence. When source material enters the current use, record its source-to-use path. Add a return condition only when stronger use must go back to a named source or defining or constraining ClaimGraph.

**Coarse-graining check.** A coarser description groups, omits, or summarizes distinctions found in another description or source. Before relying on it, name the described subject, the finer and coarser description structures, the mapping or correspondence between them, the distinctions kept and lost, and the intended use. These are facts about the descriptions and their use. They do not show that the subject itself has matching levels, parts, or relations. If the decision needs that subject-side claim, establish it separately through the pattern that defines or tests the subject relation; otherwise say only that the description was coarsened.

```text
ArchitectureDescriptionCorrespondenceClaim content:
  architectureDescriptionSetRef:
  fromViewRef:
  toViewRef:
  correspondenceKind:
    sameDescribedHolon | sameArchitectureRelationOccurrence |
    sameSelectedStructure | refinement | abstraction | coarseGraining | projection |
    sourceDerived | conflict | declaredOther
  preservedStructureRefs?
  lostStructureRefs?
  directCorrespondenceRelationRefs?: FinSet(U.RelationRef)
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?
  admissibleUse:
  nonAdmissibleUse:
C.2.1 constitution:
  entityOfConcernRef: exactly one architectureDescriptionSetRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionCorrespondenceClaim` is a C.2.1 episteme about one description set. The block separates claim content from its C.2.1 identity; it does not add slots or create a world-side relation. Cite a direct correspondence relation only when its predicate is defined, the facts satisfy it, and the relation actually holds. Correspondence helps a reader combine views without changing what each is about; it does not establish proof, grounding, assurance, gate passage, shared subject, or architecture identity.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness claim only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment state, or an external condition. Keep this bounded claim distinct from any publication-currentness relation:

```text
ArchitectureDescriptionFreshnessClaim content:
  sourceEditionRefs:
  structureEditionRefs?
  modelOrToolEditionRefs?
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange |
    controlRateChange | modelEditionChange | evidenceDecay |
    toolApiChange | regulatoryChange |
    incidentFinding | declaredOther | unknown
  admissibleUseUntil?
  sourceReturnCondition?
C.2.1 constitution:
  entityOfConcernRef: exactly one ArchitectureDescriptionRef
  effectiveReferenceScheme: U.ReferenceScheme, byValue
```

`ArchitectureDescriptionFreshnessClaim` is a C.2.1 episteme about one architecture description. The block separates claim content from its C.2.1 identity. Add a source-return condition only when stronger use must go back to a named source or defining or constraining ClaimGraph. Freshness bounds current use; it does not make the description true, grounded, evidence-sufficient, or publication-current.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a bounded use of an exact description episteme or of one of its publications.

```text
ArchitectureDescriptionSpecificationUseAccount@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDescriptionProjectUseRelationRef?: U.RelationRef defined by the pattern for the exact relation by which this specification use concerns the Work
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  sourceEpistemeRef?: U.EpistemeRef
  sourceViewRef?: U.ViewRef
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  representationRef?: U.EntityRef
  publicationOccurrenceRef?: EpistemePublicationRelationRef
  publicationFormRef?: U.EntityRef
  carrierRef?: U.EntityRef constrained to U.PresentationCarrier
  declaredUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther
  claimPatternRefs?: FinSet(PatternRef)
  admissibleUse:
  nonAdmissibleUse:

```

This account records how an existing description or publication is used as a specification. It is not an episteme, relation, MethodDescription, Method, pattern application, or Work occurrence. `claimPatternRefs` cites PatternIDs for separate claims. When project locality matters, name the composite `U.Work` and include the project-use relation only if a pattern defines it and it actually holds. If locality matters but the relation is undefined, return `missing-governor`; otherwise omit both project fields. A project label or this account creates neither Work nor relation.

If specification use is also claimed to be a pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, performed work, work authorization, decision, causal use, or release authorization, use the pattern that defines or tests that other claim. The description remains only the description boundary.

Keep the description episteme, its possible `U.View` membership, diagram or other representation, publication occurrence, publication form, and carrier distinct. Authoring, construction, querying, selection, bundling, rendering, filing, or publication creates none of the subject-side architecture relation, selected structure, description truth, empirical grounding, project Work, or project-use relation by itself.

#### C.30.AD:4.6 - Other claims and applicable patterns

| Question after the architecture-description boundary is clear | FPF application |
| --- | --- |
| Grounded architecture claim, selected structures, first architecture move | `C.30` |
| Recommended FPF pattern use after reading the description | `E.11.PUR` |
| Work-entry readiness or full-kit condition for intended architecture work | `A.15.5` |
| Architecture or structure wording is still overloaded | `C.30.P` |
| Architecture structural view or structure-kind and viewpoint relation | `C.30.ASV` |
| Transformation-flow relation or graph description used by architecture | `C.30.TFS-REL`; `E.18` for the selected structure and `E.18.2` for its mathematical description |
| Control structure view | `C.30.LCA` |
| Cross-scope or interlevel architecture residual, conflict, or frustration in the described holon | `C.30.ILC` |
| Multilevel-learning or frustration mathematical-lens result with recoverable level mapping or scale mapping and preserved structure and lost structure | `C.29` with the admitted C.29-local lens output |
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `C.32.MLAO` for the residual-reducing frame, `C.32` for the candidate palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or pool treatment, `G.5` for selected-set result declaration, `C.11` for final local choice, and measurement patterns named by value when those claims are being made |
| Generic description, view, viewpoint, publication, publication form, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or the pattern that defines or tests the quality claim |
| Evidence, assurance, internal constraint, gate, work planning, performed work, local choice, project architecture decision, causal use, or release | `A.10` for evidence, `B.3` for assurance, `A.20` for an internal-constraint result, `A.21` for a named gate decision, `A.15.2` for work planning, `A.15.1` for performed Work, `C.11` for local choice, `C.32.PAD` for a project architecture decision, `C.28` for causal use, or the direct domain pattern for the particular release, admissibility, approval, or other claim |

#### C.30.AD:4.6a - Candidate, front, and selected-set description boundary

An architecture description may also carry a project architecture decision or selected structures cited by an ADR-like publication. Use `C.32.PAD` for the decision relation, `C.32.ADR` for its publication projection, and `C.32.ADA` for decision adequacy. C.30.AD retains only description identity, E.17.0 view conformance, description-set use, correspondence claims or relations that actually hold, source paths and applicable return conditions, freshness, representation, publication use, and specification use.

An architecture description may contain claims about an archive, front, selected set, candidate palette, local choice, or planned architecture move. That content does not turn the description into any of those things or establish recommendation, readiness, authorization, or permission. Use `C.32.MLAO` and `C.32` for candidates, `C.18` and `C.19` for archives, fronts, and pools, `G.5` for a selected-set result, `C.11` for local choice, `C.30` for the architecture move, `C.30.ASV` for the structural view, `E.11.PUR` for recommended pattern use, and `A.15.5` or the A.15 family for readiness and Work. If the content is published, use `E.17` for the source-backed face and source return, and `E.24.PUB` for the publication occurrence, form, carrier, audience, bounded use, and availability. C.30.AD still records only the architecture description and its publication use.

For an architecture-description claim, record its C.2.1 identity and only the view conformance, set use, viewpoint, correspondence, source path or return condition, freshness, representation, publication use, and specification use that actually apply. If a source only grounds the first architecture move, use `C.30`. If it synthesizes alternatives, use `C.32` or `C.32.MLAO`. If it changes which variants are archived, pooled, compared, selected, published, locally chosen, or decided, use the pattern that defines or constrains that relation.

### C.30.AD:5 - Archetypal Grounding (Worked Cases)

| Case | C.30.AD treatment |
| --- | --- |
| "The architecture is documented in this view set." | Treat the set as a package of separately identified architecture-description epistemes only if each has an exact claim graph, one EntityOfConcern, and effective `U.ReferenceScheme`. A member is a `U.View` only with its exact viewpoint episteme and independently obtaining E.17.0 conformance relation. The set is not the architecture, relation occurrence, or selected structure. |
| A transformation-flow graph expression is included in an architecture document. | Use `E.18.2` for the mathematical graph description, `E.18` for the selected flow structure, path, and crossing semantics, and `C.30.TFS-REL` when the graph is used by architecture. `C.30.AD` records the exact description and its path from the source expression into that use; add a source-return condition only if a stronger use must return to the named source or exact defining or constraining ClaimGraph. The graph expression or rendering creates no actual transformation. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card publishes or represents a description episteme about an exact architecture-side object. Use the direct domain pattern for the safety or release claim, `B.3` for a separate named safety-assurance claim, `A.10` for evidence, and `A.21` only for a named gate decision. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated representation or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TFS-REL` only when an exact architecture structural view or flow relation is being used. Generation and display establish neither relation occurrence nor view membership. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Identify every description episteme separately, including its EntityOfConcern and scheme. Each cited view also names its exact viewpoint and obtaining conformance relation; an `ArchitectureDescriptionViewUseClaim` records set use without minting membership. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records exact description identities, view conformance, description-set use, and correspondence among views. Use `C.30.LCA` for the control view and `A.10`, `G.6`, or `B.3` for evidence or assurance. If a system-role assignment, F.6 Work attribution, authority, allocation, or responsibility is claimed, cite its separate direct relation, or record the exact missing governor if a rule needed to state or test that claim is absent. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records exact description epistemes, architecture claims carried as content, structural views, and source-to-use paths for reused views. A source-return condition is added only when a product-specific use exceeds the declared reuse boundary. `A.6.M` normalizes module-interface claims and routes any proposed direct relation; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting frame are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records set use, correspondence, and each view use boundary. Use `C.30.ILC` for the residual; use `C.29` only when the description contains a recoverable level or scale mapping with preserved and lost structure. |
| An operations model groups individual queues and interactions into three broad bands. | Name the operating subject, the fine and coarse description structures, the grouping map, the distinctions preserved and lost, and the use of the three-band view. This establishes a coarser description, not three subject levels. Use `C.30.STRAT`, `C.29`, `A.22`, or `C.30` only if their separate subject or model claims are needed and supported. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | Record with `C.30.AD` only the exact description or publication use of that comparison. Use `C.32.MLAO` for residual-reducing frames, `C.32` for candidate palettes, `A.19.CPM` or `A.19.SelectorMechanism` for comparison and selector-policy use, `C.18` or `C.19` for archives, fronts, and current-pool treatment, `G.5` for selected-set result declaration, and `C.11` for final local choice. For a measurement claim, use the pattern that defines or tests the measured characteristic and result. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | Treat the second description as its own `U.Episteme` and name its source, representation, publication, review, or evaluation relation directly. Keep the path to the first description and its EntityOfConcern visible without treating either description as architecture, residual, decision, or proof. |

### C.30.AD:5.1 - Bias-Annotation

| Bias | How C.30.AD prevents it |
| --- | --- |
| Description-as-architecture bias | `ArchitectureDescription` is a C.2.1 episteme about one exact holon, architecture-relation occurrence, or selected structure; it does not become that object or create it. |
| View-as-structure bias | The same description episteme is a `U.View` only through an E.17.0 conformance relation that actually holds. Use `C.30.ASV` to test selected-structure adequacy; C.30.AD records set use and correspondence without inventing membership. |
| Publication-as-authority bias | Representation, publication occurrence, publication form, carrier, dashboard polish, model-card form, or report label does not establish description truth, empirical grounding, evidence, assurance, gate, decision, work authorization, or release authorization. |
| Freshness-as-evidence bias | A freshness claim bounds admissible use; it does not make the description evidence-sufficient or publication-current. |
| Semio-bias in architecture work | Use `C.30` for obtaining architecture relations, selected structures, and architecture claims. Open C.30.AD only when work must create, inspect, or rely on a description episteme with its own ClaimGraph, EntityOfConcern, and reference scheme. |

### C.30.AD:6 - Conformance checklist

| Check | Condition to establish | Repair if failed |
| --- | --- | --- |
| **CC-C30AD-1 Episteme identity.** | Every architecture description has one exact claim graph, one exact EntityOfConcern—holon, obtaining `ArchitectureRelation` occurrence, or selected structure—and an effective `U.ReferenceScheme`. | Add the missing C.2.1 identity component or use `C.30`/`A.22` until the subject-side object is recoverable. |
| **CC-C30AD-2 Subject and holon recovery.** | The one EntityOfConcern is supplied directly. If it is an architecture-relation occurrence or selected structure, its participant trace recovers the exact holon without copying that holon into description identity; architecture-claim refs remain optional content or trace. | Restore the exact EntityOfConcern and participant trace; remove derived identity from an optional architecture-claim field. |
| **CC-C30AD-2a Traceable multi-view chain.** | For a description use that relies on a view, the reader can recover the concern, viewpoint, conformance relation, same episteme as `U.View`, EntityOfConcern, selected structure, optional actual architecture relation, description use (or set use when current), and next architecture move or pattern needed for a separate claim. Add allocation, responsibility, source use, representation, publication, correspondence, project use, or stronger-use return only when it is current. Responsibility names its own predicate and participants or the missing governor; assignment and viewpoint establish neither responsibility nor authority. | Add the missing object or relation, narrow the allowed use, or use the pattern that defines how to recover it. |
| **CC-C30AD-3 Viewpoint and structure kind.** | Every asserted architecture structural view identifies the candidate episteme, exact viewpoint episteme, independently obtaining five-part E.17.0 conformance relation, selected structure, and structure kind. | Use `E.17.0` and `C.30.ASV` before relying on the view; a label, query, bundle, diagram, or publication is insufficient. |
| **CC-C30AD-4 Correspondence and source use.** | Cross-view use names a correspondence claim or independently obtaining relation; source-derived or reused use names its source-to-use path; a source-return condition is present only when stronger use opens return to the named source or exact defining or constraining ClaimGraph. | Add the missing claim or direct relation, or narrow the admissible use. |
| **CC-C30AD-5 Representation and publication boundary.** | A diagram, rendering, publication occurrence or form, dashboard, card, file, or carrier is not treated as architecture, selected structure, `U.View`, truth, decision, evidence, assurance, gate passage, Work, authorization, or release. | Use `C.2.P`, `E.17`, `E.24.PUB`, or the pattern for the actual representation, publication, source-use, or other non-description claim. |
| **CC-C30AD-6 Specification-use boundary.** | Specification use names the description episteme or publication. Project locality additionally names one composite `U.Work` and a project-use relation that actually holds; separate non-description claims cite their applicable patterns. | Add the description, Work, and use relation as needed, or keep the use non-project-specific. |
| **CC-C30AD-7 Remaining architecture candidate use.** | Under the declared use boundary, the description still identifies the next architecture move, view repair, source repair, return condition, or pattern needed for a separate claim. | Add that remaining use or reduce the account to source, representation, or publication use. |
| **CC-C30AD-8 Coarse-graining boundary.** | A coarsening claim names the described subject, finer and coarser description structures, their mapping or correspondence, distinctions preserved and lost, and allowed use. It asserts no matching subject levels, parts, or relations without a separate subject-side basis. | Add the missing description facts, narrow the use, or establish the needed subject relation through its own pattern. |

### C.30.AD:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description-as-architecture | A document, diagram, model, graph, view set, or card is said to be the architecture or to create an obtaining architecture relation. | Recover the exact holon, `ArchitectureRelation` occurrence, or selected structure; keep the episteme, representation, publication, and source-to-use relation distinct. |
| Viewpoint-as-structure-kind or view constructor | A stakeholder, role, concern, viewpoint label, authoring template, query, or bundle is used as if it named the selected structure or granted `U.View` membership. | Use `E.17.0` for exact viewpoint conformance and `C.30.ASV` for selected structure and kind. |
| Multi-view fog | Many views are listed, but their separate C.2.1 identities, conformance relations, selected structures, or correspondence cannot be recovered. | Add the description and viewpoint references, conformance relations, selected structures, and correspondence claims or relations that actually hold. |
| Coarse model as subject hierarchy | A grouped or lower-resolution description is treated as proof that the subject has the same levels, parts, or relations. | State the description-side grouping, mapping, preserved and lost distinctions, and allowed use; establish any subject-side relation separately. |
| Specification-as-authority | A specification-looking description is used as Work, gate passage, decision, assurance, evidence, work authorization, or release authorization. | Declare the specification use and use the pattern that defines or tests the other claim. |
| Freshness laundering | A recently generated diagram is treated as adequate because it is current. | Record the bounded freshness claim, source edition, and refresh trigger; do not treat currentness as adequacy, evidence, grounding, or assurance. |
| Architecture-documentation takeover | Practitioner guidance is dominated by diagrams, publications, and wording guards instead of architecture relations, structures, descriptions, and views. | Keep `C.30` about architecture and C.30.AD about descriptions and their use; use the relevant patterns for representation and publication. |

### C.30.AD:8 - Consequences

Positive consequences:

- Architecture descriptions become reusable without pretending to be the architecture, an obtaining relation, or selected structure.
- Multi-view work can keep each episteme identity, exact viewpoint conformance, selected structures, cross-view correspondence, source-to-use paths, applicable source-return conditions, freshness, representation, publication, and specification use inspectable.
- Keep description, view membership, representation, publication, empirical grounding, evidence, assurance, gate, decision, Work, project use, release, and mathematical-lens claims distinct, and use the pattern that defines or tests each non-description claim.
- C.30 can stay focused on architecture while C.30.AD carries the heavier description machinery.

Costs:

- A useful architecture document needs explicit links to exact description epistemes, EntitiesOfConcern, effective schemes, selected structures, and admissible use.
- A claimed view additionally needs the exact viewpoint episteme and independently obtaining E.17.0 conformance relation.
- Reused or regulated descriptions may need correspondence refs, source-to-use paths, source and structure editions, applicable source-return conditions, and freshness claims before they can be relied on.
- Familiar diagrams, files, and publication forms lose implicit authority; establish grounding, evidence, assurance, gate, decision, and release claims through their relevant patterns.

### C.30.AD:9 - Rationale

Architecture work needs descriptions, but a good description is not necessarily a good architecture. A description can guide work only when the reader can identify it, tell what it describes, recover the selected structures and any view conformance, see how it corresponds to other descriptions and sources, and know what use is allowed.

The pattern therefore specializes generic Description and publication machinery for architecture use. It does not mint a new architecture kind, direct subject relation, local view-membership relation, or second meaning of `U.View`; it does not replace `C.30`; and it does not let diagrams or documentation formats establish non-description claims by presentation alone.

### C.30.AD:10 - SoTA-Echoing

**Deliberate exclusion.** SysML v2 is not used here as SoTA or useful lineage. Search prominence, a systems-oriented name, and long-standing promotion do not show that it improves the practitioner questions above, and this pattern has no project evidence that it does. For C.30.AD it is a historical dead end. Reopen this boundary only if concrete project results change a rule, worked case, or practitioner action in this pattern.

| Practice or source line | Source-use relation and currentness | C.30.AD adoption | Action consequence | Boundary |
| --- | --- | --- | --- | --- |
| FPF `C.2.1`, `A.22`, `E.17.0`, `C.30`, and `C.30.ASV` separate episteme identity, selected structures, direct architecture relations, architecture claims, and structural-view adequacy. | Current internal definitions for the objects used by this pattern. | Reuse these objects instead of importing a second architecture-description ontology. | Disciplines `C.30.AD:4.1`, `C.30.AD:4.1a`, `C.30.AD:4.2`, `CC-C30AD-1`, `CC-C30AD-3`, and `CC-C30AD-4`: every description has one exact EntityOfConcern and scheme; every asserted view has exact viewpoint conformance; correspondence and source use are explicit. | A description or view remains an episteme and does not become architecture, proof, decision, or release authority. |
| Views-and-Beyond and related architecture documentation practice treats views as stakeholder-relevant projections over architecture. | Mature reference and lineage source for view-based architecture documentation; not used as a mandatory current catalog. | Adopt view usefulness while requiring exact E.17.0 viewpoint conformance and structure-kind recovery through `C.30.ASV`; description-set use remains claim content or a separate relation that actually holds. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.2`, and the multi-view worked case: a view remains useful for a working concern without becoming the selected structure or a `U.View` by label. | No mandatory view catalog or local membership relation is imported, and view adequacy remains in `E.17.0` and `C.30.ASV`. |
| `E.17.0` and MVPK publication machinery in current FPF. | Current internal FPF definitions and publication practices for views, viewpoints, publication occurrences, forms, carriers, and publication separation. | Reuse generic view and publication machinery instead of minting architecture-local copies. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.5`, `CC-C30AD-5`, and `CC-C30AD-6`: architecture-description identity and composition remain separate from representation, publication occurrence, form, carrier, and publication-currentness. | C.30.AD specializes architecture-description use; it does not replace E.17.0, E.17.1, E.17.2, E.17, E.24.PUB, or C.2.P. |
| C4, arc42, ADR, model-card, and system-card practice makes architecture communication practical. | Current practitioner-source family for familiar architecture publication and documentation forms. | Admit these as possible source publications, view publications, decision-description publications, transparency publications, or specification-use records. | Disciplines `C.30.AD:4.5`, worked cases, and anti-patterns: practitioners can use familiar forms while keeping source, representation, publication, description, architecture, evidence, gate, decision, work authorization, release authorization, and other non-description claims separate. | Template, card, graph, or diagram quality is not architecture adequacy by itself. |
| Tool-generated architecture relation graphs and code-agent architecture probing expose useful but partial structure. | Emerging practitioner practice for recovering architecture-relevant relations from code, models, and generated analyses; currentness depends on the analyzed edition and tool run. | Treat generated graphs as representations or source-derived descriptions with observed, inferred, and unknown relation boundaries. | Disciplines `C.30.AD:4.3`, `C.30.AD:5`, and `CC-C30AD-4`: a generated output can guide structure recovery and next architecture moves only through a named source-to-use path; stronger use activates the declared source-return condition. | Generated relation coverage does not become an obtaining subject relation, `U.View`, proof, gate passage, safety assurance, or complete architecture. |

### C.30.AD:11 - Relations

- Use `C.2.1` to identify every architecture-description episteme.
- Use `C.30` for obtaining architecture relations, selected structures, and bounded architecture claims.
- Use `C.30.P` when architecture or structure wording remains overloaded; use `C.30.AD` directly when the architecture-description use is already clear.
- Use `C.30.ASV` to test architecture structural-view adequacy; only E.17.0 conformance admits the same episteme as `U.View`.
- Use `C.33` to account for captured and lost structure when a description, generated relation graph, ADR-like record, or view set carries only part of the needed architecture content.
- Use `C.34` to test preservation or correspondence when comparing a description with another view, source model, generated output, candidate, or realized structure.
- Use `C.29` for a mathematical-lens or coarse-graining result, `C.30.STRAT` for level-word admission, and `A.22` or `C.30` for the separately supported subject structure or architecture relation. Description-side grouping establishes none of those subject claims by itself.
- Use `A.6.3.NAR` for a reader-facing narrative made from a description, view set, or decision route. C.30.AD tests description adequacy; A.6.3.NAR handles structure-to-sequence, source carry-through, lost structure, reader use, and return conditions.
- Use `C.30.TFS-REL`, `C.30.LCA`, and `C.30.ILC` for their named architecture-relation subcases.
- Use `C.32.P2S` for a connected architecturing flow when the description carries only part of the selected structure, decision handoff, method expectation, source continuity, return condition, or feedback from actual structure.
- Use `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, and `E.24.PUB` for generic EntityOfConcern, view, viewpoint, representation, publication occurrence, form, carrier, and MVPK machinery.
- `C.2.P` normalizes source-expression, source-to-use, publication-form, and publication-currentness relation-set overreads.
- Use `E.11.PUR` for recommended FPF pattern use after reading a description; C.30.AD records only the description-use boundary.
- Use `A.15.5` for work-entry readiness and full-kit condition; use the A.15 family for Work and the direct governor for any needed project-use relation. C.30.AD records only descriptions and their view conformance, set use, correspondence, source paths and returns, freshness, representation, publication use, and specification use.
- `E.10.MOVE` restores move-like wording when source prose about an architecture description does not mean a C.30 architecture move or a C.30.AD remaining architecture candidate use.

### C.30.AD:End

