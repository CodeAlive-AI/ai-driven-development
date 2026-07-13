## A.22.CGUS - Constraint-Governed Unfolding Structure

> **Type:** A.22 specialization of `U.Structure`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22.CGUS:0 - Use This When

Use this when a team has a P2S flow card, a P2W carry-through note, an abductive prompt path, an improvement cycle, a narrative ordering, a typing-grounding trace, or a README first-entry seed, and the visible form helps but also misleads. It looks like a route, loop, chain, table, graph, or story, while the useful engineering question is not "which sequence should everyone follow?" but "which admitted records, current structures, typed positions, relation instances, constraints, and guards make each continuation admissible or inadmissible?"

When that is the live question, name the object as `ConstraintGovernedUnfoldingStructure@Context`: an A.22-governed `U.Structure` whose SlotSpec-grounded positions, relation signatures, exact referenced values, cross-position constraints, invariants, guarded transitions, preserved structures, C.33 adequacy notes, direct governing-pattern exits, admissible next-form kinds, and use boundaries jointly constrain more than one continuation.

Use CGUS only after the candidate structure has more than one typed position and the relations or constraints among those positions affect admissible continuations. A single recommendation, diagram, slogan, pattern list, or document section is not enough.

### A.22.CGUS:1 - Problem Frame

FPF often needs to explain how several admitted records, current structures, typed positions, and relations jointly constrain several admissible next forms without turning that explanation into a workflow. A problem card, `G.2` source pack, architecture concern, candidate set, evaluation result, cue publication, and current `U.Structure` can participate through exact governed relations in pattern-use recommendations, candidate structures, rival hypotheses, evidence work, repair proposals, reader-facing narratives, or structure-use return conditions. The point is the recoverable constraint structure, including relation signatures, guards, preserved structures, C.33 loss notes, and direct governing-pattern exits, not a one-input-one-output conversion.

These structures can be architecture-facing, reasoning-facing, narrative-facing, improvement-facing, typing-grounding-facing, evidence-facing, currentness-facing, or first-use-facing. They share one structural need: typed positions are connected by relations and constrained together, so admissible continuations are recoverable only while the relevant structures, C.33 adequacy notes, guards, exits, and governing-pattern boundaries remain visible.

### A.22.CGUS:2 - Problem

The problem is that a constraint-governed unfolding structure becomes unrecoverable when one route-shaped or loop-shaped description stands in for it.

First, the structure's typed positions, exact relations, constraints, preserved structures, C.33 adequacy notes, stop boundary, and direct governing patterns disappear behind decorative prose. Words such as "flow", "move", "unfold", "loop", or "route" remain, but no reader can recover what constrains a continuation.

Second, one demonstration of the structure becomes a fake workflow. A teaching sequence, diagram, README entry, prompt example, or happy path is treated as the order of real project work. Method, work plan, performed work, evidence, gate, decision, publication, and architecture claims then become unsupported inferences from displayed order.

### A.22.CGUS:3 - Forces

| Force | Tension |
| --- | --- |
| Useful unfolding vs workflow overread | A structured unfolding helps a practitioner see what can come next, but the project sequence may be nonlinear, partial, interrupted, iterative, or delegated to different governing patterns. |
| Reusable `U.Structure` specialization vs root-kind inflation | FPF needs a reusable A.22 specialization of `U.Structure` for constraint-governed unfolding without minting `U.Route`, `U.Workflow`, `U.Process`, `U.Architecture`, or another root kind by appearance. |
| Description usefulness vs semio-bias | Route cards, graphs, tables, slides, narratives, and README lines can suggest the structure before admission or present it after admission, but provisional descriptions and admitted demonstrative slices are not the structure itself. |
| Local claims vs universal calculus | P2W, P2S, abduction, narrative, improvement, grounding, refresh, and option selection need different direct governing patterns; CGUS only carries the shared constraint-governed unfolding structure. |
| Didactic entry vs shadow navigation | First-entry seed lines help new readers start while remaining publication aids rather than a second specification or navigation authority beside the governing patterns. |

### A.22.CGUS:4 - Solution

Select `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` as a thin A.22 specialization of `U.Structure` for constraint-governed unfolding across typed positions and exact governed relations.

A constraint-governed unfolding structure is a `U.Structure` whose typed positions, relation signatures, referenced relation values, constraints, invariants, guarded transitions, preserved structures, C.33 adequacy notes, and governing-pattern exits jointly constrain admissible next forms. It states how admitted starting records and already-current structures participate through exact relations. It makes no displayed-order claim about real work and fixes no cardinality of starting records, starting structures, or resulting records.

Do not read "unfolding" as a chain by default. The unfolding structure may be branching, merging, cyclic, partially ordered, or graph-shaped, and it may leave several alternative next forms live at once. Before the wider structure passes the admission test, a linear chain, seminar order, prompt path, or happy path remains a `ProvisionalUnfoldingDemonstrationDescription@Context`. After admission, a presentation of one traversal may be a `DemonstrativeUnfoldingSlice@Context` whose EntityOfConcern is that admitted CGUS.

#### A.22.CGUS:4.1 - Constraint-governed unfolding structure

```text
UnfoldingStructureReferenceKindValue = acceptedStartingRecord | relationInstance | constraint | invariant | guardedTransition | currentness
UnfoldingStructureBoundaryKindValue = admissibleUse | nonAdmissibleUse | stop | return

ConstraintGovernedUnfoldingStructure@Context <: U.Structure:
  boundedContextRef: U.BoundedContextRef
  declaredStructureSubstrateRef: U.EntityRef, referencing one U.Structure
  entityOfConcernRef: U.EntityRef
  entityOfConcernKindRef: U.KindRef
  specializedStructureRef?: U.EntityRef, referencing one narrower U.Structure
  acceptedStartingRecordReferenceRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=acceptedStartingRecord
  acceptedStartingStructureRefs[]: U.EntityRef, each referencing one U.Structure
  relationSignatureRefs[]: U.EntityRef, each referencing one U.Signature
  structurePositionRefs[]: U.EntityRef, each referencing one ConstraintGovernedUnfoldingPosition@Context
  relationInstanceReferenceRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=relationInstance
  constraintReferenceRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=constraint
  invariantReferenceRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=invariant
  guardedTransitionReferenceRefs[]: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=guardedTransition
  preservedStructureRefs[]: U.EntityRef, each referencing one U.Structure
  structureInformationAdequacyNoteRefs[]?: U.EpistemeRef, each referencing one StructuralInformationAdequacyNote@Context under C.33
  admissibleNextFormKindRefs[]: U.KindRef
  demonstrativeSliceRecipeRefs[]?: U.EntityRef, each referencing one U.MethodDescription
  admissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  nonAdmissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  stopBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  structureUseReturnBoundaryRefs[]: U.EntityRef, each referencing one UnfoldingStructureUseBoundaryCondition@Context
  currentnessRelationReferenceRefs[]?: U.EntityRef, each referencing one UnfoldingStructureReferencedValueRelation@Context with referenceKind=currentness
```

The declared substrate is the structure being unfolded, not a topic label or container. `specializedStructureRef` is present only when one narrower `U.Structure` record is current, such as an E.18.3 transformation-flow specialization. That narrower record may point back through its `unfoldingStructureRef`; the reciprocal references state one generic-to-narrower specialization relation and do not create two unrelated unfolding structures. Accepted starting records and accepted starting structures remain different: a record may describe, publish, or evaluate a structure without becoming that structure. Every referenced entity retains its exact kind and direct governing pattern.

#### A.22.CGUS:4.1.1 - Dependent position, reference, and boundary relations

```text
ConstraintGovernedUnfoldingPosition@Context <: U.Relation:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  positionSlotSpecRef: U.EntityRef, referencing one A.6.5 SlotSpec
  positionFillingRef?: U.EntityRef
  positionFillingKindRef?: U.KindRef
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  RelationRefKind: U.EntityRef
  Dependence: bounded-context local to unfoldingStructureRef
  Identity: <unfoldingStructureRef, positionSlotSpecRef, positionFillingRef if present>

UnfoldingStructureReferencedValueRelation@Context <: U.Relation:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  referenceKind: UnfoldingStructureReferenceKindValue
  referencedValueKindRef: U.KindRef
  referencedValueRef: U.EntityRef
  directGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  relationSignatureRef?: U.EntityRef, referencing one U.Signature
  RelationRefKind: U.EntityRef
  Direction: unfoldingStructureRef -> referencedValueRef
  Dependence: bounded-context local to unfoldingStructureRef and referencedValueRef editions
  Identity: <unfoldingStructureRef, referenceKind, referencedValueKindRef, referencedValueRef>

UnfoldingStructureUseBoundaryCondition@Context <: U.Relation:
  unfoldingStructureRef: U.EntityRef, referencing one ConstraintGovernedUnfoldingStructure@Context
  boundaryConditionKind: UnfoldingStructureBoundaryKindValue
  conditionDescriptionRef: U.EpistemeRef
  affectedStructureRef: U.EntityRef, referencing one U.Structure
  boundaryGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  conditionalReceivingPatternRef?: U.EntityRef, referencing one U.MethodDescription
  RelationRefKind: U.EntityRef
  Dependence: bounded-context local to unfoldingStructureRef and affectedStructureRef editions
  Identity: <unfoldingStructureRef, boundaryConditionKind, conditionDescriptionRef, affectedStructureRef, conditionalReceivingPatternRef if present>
```

The two `...KindValue` declarations are local closed enumerations, not U-kinds. Position filling ref and kind are both present or both absent. A relation signature is present when the referenced value is a relation. Every boundary names its governing pattern; only `return` names a conditional receiver.

`StructuralInformationAdequacyNote@Context` under C.33 carries captured, expected-but-uncaptured, lost, and hidden structure for a declared use. CGUS does not mint parallel loss or hiddenness fields. A use boundary is not permission, gate passage, evidence, assurance, or currentness refresh by itself.

#### A.22.CGUS:4.2 - Admission test

A readable chain is not sufficient for admission. Use CGUS only when the current structure recovers all of the following:

| Coordinate | Recovery for CGUS admission | Reduced use when absent |
| --- | --- | --- |
| Structure identity | One exact `U.Structure` substrate, bounded context, EntityOfConcern, and kind. | Keep a note, card, description, or method description. |
| Typed positions | More than one SlotSpec-grounded position and any current filling ref-kind pairs. | Keep a list or seed description. |
| Connecting relations | Relation signatures and exact referenced relation instances. | Keep an index until connections are recoverable. |
| Cross-position constraints | Constraints, invariants, guards, branches, joins, cycles, partial orders, or many-to-many dependencies that matter to the use. | Keep a linear presentation as a provisional demonstration description until the wider structure is admitted. |
| Preserved and omitted structure | Preserved structures and any C.33 adequacy notes needed by the declared use. | Lower the adequacy claim and retain the return. |
| Admissible next forms | Exact next-form kinds, not one forced next record. | Do not claim a usable unfolding structure. |
| Direct governing-pattern exits | Each stronger claim points to its direct pattern. | The structure is overreading itself as method, work, evidence, gate, architecture, publication, or refresh authority. |
| Use boundaries | Admissible, non-admissible, stop, and return conditions are explicit. | Keep the artifact as a provisional explanation. |

Branches or joins that are current remain visible. A cycle shown as "return to the start" is not thereby a chain. One slice may be linear because attention needs one path; the wider structure remains graph-shaped when its relations are graph-shaped.

#### A.22.CGUS:4.3 - Provisional demonstrations, admitted-structure descriptions, and demonstrative slices

A presentation may help discover positions and relations before any CGUS exists. Keep that pre-admission object as a C.2.1-conformant episteme about the actual subject-domain object, question, or proposed continuation set:

```text
DemonstrationUseModeValue = workedSlice | firstUseExample | actualCaseReplay | variantComparison | otherDeclared
DemonstrationPresentationFormValue = orderedList | chainDiagram | flowCard | table | narrativePath | slideSequence | promptBlock | graphSlice | otherDeclared

ProvisionalUnfoldingDemonstrationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the actual subject-domain object, question, or proposed continuation set
  entityOfConcernKindRef: U.KindRef
  boundedContextRef: U.BoundedContextRef
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  groundingHolonRef?: U.HolonRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  demonstrationUseMode: DemonstrationUseModeValue
  presentationForm: DemonstrationPresentationFormValue
  provisionalContinuationDescriptionRefs[1..*]: U.EpistemeRef
  candidatePositionDescriptionRefs[2..*]: U.EpistemeRef
  candidateRelationDescriptionRefs[]?: U.EpistemeRef
  unresolvedCGUSAdmissionCoordinateDescriptionRefs[1..*]: U.EpistemeRef
  admissionTransitionConditionDescriptionRef: U.EpistemeRef
```

This local declaration form is an episteme, not a structure slice and not a new root kind. Its C.2.1 identity comes from its exact EntityOfConcern, DescriptionContext, optional grounding holon, ClaimGraph, reference scheme, and edition. `entityOfConcernRef` names the subject that the explanation is currently about; it may not point to a not-yet-admitted CGUS. Candidate positions and relations are claims to investigate, not admitted `ConstraintGovernedUnfoldingPosition@Context` or relation instances. At least one unresolved admission coordinate remains present while the description is provisional.

Once every coordinate in `4.2` is recoverable and the wider `ConstraintGovernedUnfoldingStructure@Context` is admitted, describe that structure without selecting a traversal through it by creating this C.2.1-conformant episteme:

```text
ConstraintGovernedUnfoldingStructureDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one admitted ConstraintGovernedUnfoldingStructure@Context
  entityOfConcernKindRef: U.KindRef, referencing ConstraintGovernedUnfoldingStructure@Context
  boundedContextRef: U.BoundedContextRef
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  groundingHolonRef?: U.HolonRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  preservedStructureRefs[]: U.StructureRef
  structureInformationAdequacyNoteRefs[]?: U.EpistemeRef, each referencing one StructuralInformationAdequacyNote@Context under C.33
  declaredUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  descriptionUseReturnBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
```

Its EntityOfConcern is the admitted CGUS. Its ClaimGraph may describe branches, joins, cycles, partial orders, positions, relations, constraints, and admissible next forms without choosing one route through them. Carrier, diagram form, table layout, or publication location does not determine its identity. A new edition is required when the described CGUS edition, DescriptionContext, applicable grounding, ClaimGraph, reference scheme, preserved-structure account, adequacy account, declared use, or return boundary changes.

When one presentation selects a traversal or ordering through that admitted structure, create a different post-admission episteme:

```text
DemonstrativeUnfoldingSlice@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one admitted ConstraintGovernedUnfoldingStructure@Context
  boundedContextRef: U.BoundedContextRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  derivedFromProvisionalDemonstrationRef?: U.EpistemeRef, referencing one ProvisionalUnfoldingDemonstrationDescription@Context
  demonstrationUseMode: DemonstrationUseModeValue
  transformationFlowStructureRef?: U.EntityRef, referencing one E.18 TransformationFlowStructure
  pathSliceId?: E.18 PathSliceId
  designRunTag?: E.18 DesignRunTag
  demonstratedPatternUseRowRefs[]: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
  includedStructurePositionRefs[]: U.EntityRef, each referencing one ConstraintGovernedUnfoldingPosition@Context
  omittedStructureInformationAdequacyNoteRefs[]?: U.EpistemeRef, each referencing one StructuralInformationAdequacyNote@Context under C.33
  loopCompressionRuleRef?: U.EntityRef, referencing one U.MethodDescription
  alternativeSliceRefs[]?: U.EpistemeRef, each referencing one DemonstrativeUnfoldingSlice@Context
  presentationOrderingRuleRef: U.EntityRef, referencing one U.MethodDescription
  presentationForm: DemonstrationPresentationFormValue
  admissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  nonAdmissibleUseRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
  sliceReturnBoundaryRef: U.EntityRef, referencing one UnfoldingStructureUseBoundaryCondition@Context
```

The transition does not retype the provisional episteme or any subject-domain result. The admitted slice cites the provisional description only as its derivation basis, names the already-admitted CGUS as EntityOfConcern, and replaces candidate position and relation descriptions with exact admitted structure positions and relation references. Its edition changes when that CGUS edition, included positions, omitted-structure account, traversal or ordering rule, alternatives, use boundary, ClaimGraph, or reference scheme changes; carrier or rendering change alone does not. If admission later fails, the provisional explanation may remain useful under its declared use while the slice claim is withdrawn.

The local mode and presentation-form values are enumerations, not CharacteristicSpaces or U-kinds. Presentation form says how the episteme is rendered; it is not a carrier kind. Add an E.17 publication relation only when publication is current.

The E.18 triple is all present or all absent. When present, it locates this post-admission demonstration in one flow valuation and relates pattern-selection, selected-pattern-application, and downstream-subject-work slices without merging their structures, rows, work occurrences, or results.

#### A.22.CGUS:4.3.1 - Demonstrated pattern-use rows

When a local pattern mantra is admitted as a `DemonstrativeUnfoldingSlice@Context`, `mantra move` is bounded Plain wording for one `DemonstratedPatternUseRow@Context` inside that slice. The row consumes A.6.5 SlotSpec discipline, but A.6.5 does not govern the row's identity. The row is not a root U-kind, an operation, or a work occurrence. It shows one result-bearing conditional continuation. A short repeatable formula that only recalls one pattern's Solution may still be a useful local mantra without containing such rows and without becoming a CGUS.

```text
DemonstrationBasisModeValue = publicTemplate | projectCandidate

DemonstratedPatternUseRow@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing the containing DemonstrativeUnfoldingSlice@Context
  boundedContextRef: U.BoundedContextRef
  claimGraph: U.ClaimGraph by value
  referenceScheme: U.ReferenceScheme by value
  editionId
  sourcePracticeContinuationDescriptionRef?: U.EpistemeRef, referencing one PatternUsePracticeContinuationDescription@Context
  demonstrationBasisMode: DemonstrationBasisModeValue
  demonstratedResultFlowPosition: PatternUseResultFlowPositionValue
  nestedPatternSelectionSliceRef?: U.EpistemeRef, referencing one DemonstrativeUnfoldingSlice@Context
  actionOrProposedUseDescriptionRef: U.EpistemeRef
  directPatternIdentifier: PatternIdentifierValue
  directPatternName: PatternNameValue
  publicCandidateUseTemplateRef?: U.EpistemeRef, referencing one PublicCandidatePatternUseTemplate@FPFReadme
  projectCandidatePatternUseRef?: U.EpistemeRef, referencing one CandidatePatternUse@Context
  publicPracticalUseQuestionRef?: U.EpistemeRef, referencing one PublicPracticalUseQuestion@FPFReadme
  projectPracticalUseQuestionRef?: U.EpistemeRef, referencing one PracticalUseQuestion@Context
  solutionMethodDescriptionRef: U.EntityRef, referencing one U.MethodDescription
  publicResultTemplateRef?: U.EpistemeRef, referencing one PublicPatternUseResultTemplate@FPFReadme
  projectResultExpectationRef?: U.EpistemeRef, referencing one PatternUseResultExpectation@Context
  publicContinuationConditionRef?: U.EpistemeRef, referencing one PublicPatternUseBoundaryConditionTemplate@FPFReadme
  projectContinuationConditionRef?: U.EpistemeRef, referencing one PatternUseBoundaryCondition@Context
  alternativeDemonstratedRowRefs[]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
  returnDemonstratedRowRefs[]?: U.EpistemeRef, each referencing one DemonstratedPatternUseRow@Context
  applicabilityFindingRef?: U.EpistemeRef, referencing one PatternUseApplicabilityFinding@Context
  recommendationRef?: U.EpistemeRef, referencing one PatternUseRecommendation@Context
  workPlanRef?: U.EntityRef, referencing one U.WorkPlan
  performedWorkRef?: U.EntityRef, referencing one U.Work
```

In `publicTemplate` mode, exactly the public candidate, question, result, and continuation positions are filled; the project positions are absent. In `projectCandidate` mode, exactly the project candidate, question, expectation, and continuation positions are filled; the public positions are absent. Applicability, recommendation, WorkPlan, and Work refs appear only when those values already exist.

The result-flow position is always present. An unresolved direct-pattern choice opens a separate nested pattern-selection slice. That slice returns a candidate, finding, or recommendation used by the enclosing row; it does not become the enclosing result-producing structure.

#### A.22.CGUS:4.3.2 - Pre-execution slot-filling scaffold

A provisional demonstration can hold attention on visible candidate positions before execution and before CGUS admission. Each visible position initially points to a subject-domain object, question, or proposed continuation and states which A.22.CGUS admission coordinate remains unresolved. It does not yet point to an admitted `ConstraintGovernedUnfoldingPosition@Context`.

Fill the scaffold in small passes. First name the visible candidate positions. Then recover the exact objects, kinds, relation signatures, constraints, invariants, guards, preserved structures, C.33 notes, next-form kinds, and stop or return conditions that would satisfy `4.2`. Keep every unresolved coordinate explicit in the provisional description. Only after the wider structure is admitted may a separate demonstrative slice replace candidate descriptions with exact structure-position and relation refs.

**Minimal first use.** Write three visible candidate positions such as `candidate`, `evaluate`, and `repair`; describe the proposed relation that would make repair conditional on an evaluation result; and show both `accept candidate` and `repair candidate` as possible continuations. Keep this as a `ProvisionalUnfoldingDemonstrationDescription@Context` while the exact position kinds, relation instance, guard, preserved structure, or use boundary remains unresolved. It already helps a team hold the branch in attention without asserting the wider CGUS.

After CGUS admission, create a separate `DemonstrativeUnfoldingSlice@Context`, cite the provisional description as derivation basis, and map only the recovered candidate material to exact admitted positions and relations. The scaffold helps design the wider graph; neither provisional nor admitted presentation asserts project work order or authorizes work.

#### A.22.CGUS:4.3.3 - Bounded names and bridge

`Mantra` is broader Plain didactic wording for a short repeatable formulation that keeps a local pattern's Solution in attention. The word alone does not recover one universal FPF kind. `A.6.P`, for example, can publish a local RPR mantra that recalls its repair order without claiming a wider unfolding structure.

Other patterns may keep an established local name such as `mnemonic`, `watchword`, or `heuristic` when that name better tells their readers what the aid does. A.19's common-space comparison mnemonic, A.15.1's CAC mnemonic, and E.8's seven-step heuristic need not be renamed `mantra`. Conversely, an acronym, title mnemonic, or retrieval label is not a local mantra merely because it is memorable. These are Plain didactic choices interpreted from the local Solution and reader use, not rival FPF kinds.

This pattern governs only the narrower case in which a local mantra presents admissible conditional continuations through a named wider constraint-governed unfolding structure. In that case, `mantra` may name the admitted `DemonstrativeUnfoldingSlice@Context`, and `mantra move` may name one `DemonstratedPatternUseRow@Context` inside it. Neither label grants method, plan, order, authority, work, or teaching-medium identity.

##### Ordinary bounded use

In public FPF explanation, call the admitted slice a `demonstrative walkthrough`. In the bounded seminar context recorded below, `mantra` is the shorter repeatable name for that same demonstrative episteme. One `mantra move` is a `DemonstratedPatternUseRow@Context`: it names the direct pattern, its Solution, the expected result, and the condition for continuing. Outside this admitted CGUS-demonstrative use, interpret a local mantra from the pattern's own Solution and context rather than forcing it into `DemonstrativeUnfoldingSlice@Context`.

##### Naming assurance

The following F.18 cards and directional Bridge preserve the lexical and contextual decisions behind those Plain labels. The separate `LocalSenseBasisRelation@Context` values identify which public pattern episteme or seminar publication episteme supports each local sense. NameCards support naming review; the basis relations support the bounded sense lines. Neither adds a step to CGUS application.

```text
NameCardId: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GoverningPatternRef: A.22.CGUS
BoundedContextRef: FPF English public publication, edition 2026-07-11
LocalSenseRef: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
TechLabel: DemonstrativeUnfoldingSlice@Context
PlainLabel: demonstrative walkthrough
CandidateSet: [demonstrative walkthrough, mantra, mnemonic walkthrough, solution-story refrain, repeated explanatory walkthrough, pattern-use refrain]
RejectedCandidates:
  mantra -> broader local didactic wording that does not by itself identify this CGUS-demonstrative value
  mnemonic walkthrough -> foregrounds a memory technique rather than the represented structure
  solution-story refrain -> overstates narrative form and refrain structure
  repeated explanatory walkthrough -> is too long to serve as the public label
  pattern-use refrain -> narrows the value although a CGUS slice may demonstrate wider structure
SelectionRationale: the phrase identifies a presented explanatory episteme for a cold reader while the Tech value restores represented structure
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
UnifiedTermRowRef: UTS.DemonstrativeUnfoldingSlice.FPFPublic
LineageEntries: demonstrative slice -> cold-reader public Plain label
RefreshCondition: readers treat the phrase as actual traversal, fixed work order, or teaching medium rather than the governed episteme
```

```text
NameCardId: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GoverningPatternRef: A.22.CGUS
BoundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
LocalSenseRef: a short repeatable explanatory walkthrough that helps a participant hold the whole solution structure in mind without prescribing performed-work order
TechLabel: DemonstrativeUnfoldingSlice@Context
PlainLabel: mantra
CandidateSet: [mantra, demonstrative walkthrough, mnemonic walkthrough, solution-story refrain, repeated explanatory walkthrough, pattern-use refrain]
RejectedCandidates:
  demonstrative walkthrough -> accurate but too long for repeated seminar speech and does not foreground attention
  mnemonic walkthrough -> foregrounds a memory technique rather than repeatable explanatory content
  solution-story refrain -> overstates narrative form
  repeated explanatory walkthrough -> is too long for the repeated teaching alias
  pattern-use refrain -> narrows demonstrations to pattern use and loses wider CGUS cases
SelectionRationale: repeated-formula and watchword senses support remembered repetition; the Sanskrit analysis instrument of thought supplies the attentional rationale; bounded context excludes ritual, slogan, method, plan, and work senses
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
UnifiedTermRowRef: UTS.DemonstrativeUnfoldingSlice.SeminarTeaching
LineageEntries: seminar teaching concept -> English lexical comparison -> bounded teaching alias over the same governed value
RefreshCondition: readers infer ritual authority, slogan, rote formula, method, WorkPlan, Work, teaching medium, or cannot recover the demonstrated structure
```

```text
NameCardId: NameCard.DemonstratedPatternUseRow.SeminarTeaching
GovernedValueRef: DemonstratedPatternUseRow@Context
GoverningPatternRef: A.22.CGUS
BoundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
LocalSenseRef: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
TechLabel: DemonstratedPatternUseRow@Context
PlainLabel: mantra move
CandidateSet: [mantra move, mantra row, demonstrated pattern-use row, walkthrough continuation, mnemonic step, solution-story move]
RejectedCandidates:
  mantra row -> foregrounds a table container rather than the conditional continuation
  demonstrated pattern-use row -> is exact but too technical for repeated seminar speech
  walkthrough continuation -> loses the bounded relation to the seminar mantra alias
  mnemonic step -> suggests a fixed serial step and memory technique
  solution-story move -> overstates narrative form and can be read as movement
SelectionRationale: the phrase keeps the bounded mnemonic relation and names one continuation; row fields restore direct pattern, Solution, result, and condition
BridgeRefs: none; expression and governed row are local to one seminar context
UnifiedTermRowRef: UTS.DemonstratedPatternUseRow.SeminarTeaching
LineageEntries: bounded mantra alias plus local move wording -> typed demonstrated-pattern-use row
RefreshCondition: readers infer universal Move, physical movement, operation, fixed serial step, PlanItem, Work, or a row detached from its slice
```

```text
SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  Context: FPF English public publication, edition 2026-07-11
  LocalExpression: demonstrative walkthrough
  LocalSense: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11

SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  Context: English-language FPF seminar teaching, edition 2026-07-11
  LocalExpression: mantra
  LocalSense: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  localSenseCellRef: SenseCell(FPF-English-Public-2026-07-11, DemonstrativeUnfoldingSlice-public)
  basisEpistemeRef: A.22.CGUS
  basisEpistemeKindRef: U.MethodDescription
  basisPublicationUnitRef: A.22.CGUS:4.3.3-Ordinary-bounded-use
  boundedContextRef: FPF English public publication, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: FPF English public publication, edition 2026-07-11
  viewpointRef: FPFPublicReaderViewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11, FPF English public publication 2026-07-11, FPFPublicReaderViewpoint>
  claimGraph:
    supportedSenseClaim: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
    admittedUseClaim: support the public local-sense line for this SenseCell
    nonAdmittedUseClaim: no evidence, authority, work-order, or naming decision follows from this relation
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPF-Seminar-Teaching-2026-07-11, DemonstrativeUnfoldingSlice-mantra)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11
  basisEpistemeKindRef: U.EpistemePublication
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
  viewpointRef: FPF Seminar Participant Viewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11, English-language FPF seminar teaching 2026-07-11, FPF Seminar Participant Viewpoint>
  claimGraph:
    supportedSenseClaim: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
    admittedUseClaim: support the bounded teaching sense from the seminar expression
    nonAdmittedUseClaim: the slide carrier does not become the sense, naming settlement, method, plan, or work
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11
BridgeCardId: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
BridgeKind: Narrower-than
Direction: seminar CellB to public CellA only
CL: 2
LossNotes: the public sense omits repeated speech, remembered replay, and seminar attentional function
CounterExampleOrInvariantEvidence: a public walkthrough may be read once without mnemonic repetition
AdmittedUse: Naming-only from seminar mantra to public demonstrative walkthrough and the same governed value
NonAdmittedUse: no reverse substitution and no inference of method, plan, order, authority, work, or teaching-medium identity
RevisionTrigger: context edition, observed loss, local label, or governed value changes
```

The local relation species and its SlotKind, ValueKind, RefKind, direction, dependence, and identity are declared in `F.17:5.1`. `SeminarExpression.FPFPracticalUse.2026-07-11` is the seminar content as a `U.EpistemePublication`; the `.pptx` and extracted Markdown are separate carriers or renderings.

The bridge is directional; shared reference to one governed value does not erase the sense difference. It governs only the two senses of this CGUS-demonstrative value and does not govern every local pattern mantra. The seminar publication expression supplies the teaching problem and the local-sense basis; its carriers do not. Dictionaries supply English lexical and etymological evidence, while F.18 plus reader-use tests decide the bounded names. A changed NameCard therefore reopens naming without silently changing the public or teaching sense. A changed SenseCell address, basis-episteme edition, bounded context, or cited publication unit reopens the corresponding `LocalSenseBasisRelation@Context`; a changed supported-sense claim or use boundary opens a new `LocalSenseBasisRelationDescription@Context` edition. F.18 remains the naming procedure.

#### A.22.CGUS:4.4 - Direct Governing Pattern Exits

CGUS carries the unfolding structure. It does not absorb stronger claims.

| Stronger claim being made | Direct governing pattern or family |
| --- | --- |
| Atomic bounded change | `A.3.4` |
| Method or method description | `A.3.1`, `A.3.2`, and method-composition patterns |
| Work plan, work entry, or performed work | `A.15.2`, `A.15.5`, `A.15.1`, and neighboring work patterns |
| Evidence, assurance, or gate | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` as current |
| Architecture use, architecture decision, or architecture description | `C.30`, `C.30.ASV`, `C.32.P2S`, `C.32.PAD`, `C.32.ADR`, `C.30.AD` |
| Variant archive, non-dominated front, live pool, or selected-set publication | `C.18`, `C.19`, `G.5` |
| Narrative rendering or publication use | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Improvement of an object version | `E.23`, with evaluation patterns for the declared object |
| Source currentness, decay, edition shift, or refresh orchestration | `G.11` |
| Mathematical lens or formal modeling | `C.29`, `A.6.0`, `A.6.1` |

Use the word `refresh` only when a currentness, telemetry, edition, decay, or slice-local refresh claim is actually current. Otherwise use plain return, stop, split, or repair wording and name the direct governing pattern.

#### A.22.CGUS:4.4a - Direct Governing-Pattern Dependent Records

Some CGUS uses need dependent records that keep adjacent method, work, evidence, architecture, description, or publication claims inspectable. A.22.CGUS does not define those record schemas. Reliance on a stronger claim is admitted only when the corresponding CGUS field names its direct governing pattern.

For method and work linkage, use `MethodWorkUnfoldingLinkage@Context`, governed by A.15, only when a named receiving use relies on that relation remaining inspectable across method, method description, role assignment, capability-fit condition, work plan, readiness, performed work, evidence, assurance, or gate positions. If only one method, work-plan, readiness, performed-work, evidence, assurance, or gate claim is current, use that direct governing record instead.

For architecture use, use the C.32.P2S-owned `ArchitectureUnfoldingStructureUse@Project` only when a named unfolding structure is being used as architecture-relevant structure in problem-to-structure architecturing. If the current claim is only grounded architecture, structural view, architecture description, decision, ADR-like projection, measurement, eval, or performed realization work, use the direct pattern for that claim.

This keeps A.22.CGUS thin: it governs the constraint-governed unfolding structure and its safe next-use boundary, while A.15, C.30, C.32, evidence, gate, publication, and domain patterns govern the adjacent records that carry stronger claims.

#### A.22.CGUS:4.5 - Promoted Core Family Cue Examples

The FPF core may promote a few short family cues when a cue helps readers recover a familiar governing pattern and a common blocked overread. This is an example device, not a maintained list of all CGUS families.

For example, `UF.P2S` can be useful when an architecture-facing question moves from problem pressure to candidate, selected, expected, or actual structures. The cue points the reader toward `C.32.P2S` and warns that a P2S card is not itself the architecture decision, architecture description, ADR, or realization work.

For example, `UF.IMP` can be useful when an object version, evaluation frame, candidate repairs, and re-evaluation are current. The cue points toward `E.23` and warns that a retry loop or prompt loop is not quality improvement by shape.

For example, `UF.REFRESH` can be useful when a `G.11` source-currentness relation, telemetry, evidence decay, or edition shift is current. The cue points toward `G.11` and warns that a stale reference set is not current authority.

If no promoted cue helps, omit the cue. Do not invent a core `UF.*` cue merely to make a CGUS use look governed. DPFs and project-local frameworks may carry their own local cue examples when useful, but the governing claim still comes from the local governing-pattern map and the relevant pattern bodies.

#### A.22.CGUS:4.6 - Replay and change localization

Replay one CGUS use from its bounded context, unfolded structure, subject EntityOfConcern and kind, current position fillings, exact referenced relation instances, constraints, invariants, guards, preserved structures, C.33 adequacy notes, admissible next-form kinds, and use boundaries. For each selected continuation, recover the relations and guards that admit it and the direct pattern governing any stronger claim. A demonstrative slice is replayable only as one declared presentation of that wider structure.

Localize a change before reopening wider work. A changed relation instance reopens that reference and its dependent guards or continuations. Changed omitted structure reopens the affected C.33 adequacy note and any slice relying on it. A changed presentation changes the demonstrative slice without changing the CGUS unless it reveals missing or false structure. A freshness, edition, telemetry, or decay change is handled by its exact `G.11` relation. A changed method, work, evidence, architecture, publication, or formal claim returns to the direct governing pattern for that claim. Rebuild the wider CGUS only when its structure identity, position set, relation structure, constraints, or declared use boundary has changed.

### A.22.CGUS:5 - Worked Slices

**Architecture P2S slice.** A team starts with architecture-relevant problem pressure. The unfolding structure may relate problem pressure, unknown structures, candidate structures, architecture characteristics, one `ProjectArchitectureDecision@Context` governed by `C.32.PAD`, realization-work linkage, actual-structure feedback, and return conditions. The P2S flow card can describe those relations, but the decision relation remains governed by `C.32.PAD`, architecture descriptions by `C.30.AD`, and planned or performed work by the A.15 family.

**Abductive search slice.** An inquiry starts from an abductive prompt and a cue set selected for the search. The unfolding structure may relate rival hypotheses, plausibility constraints, hypothesis-generation positions, evidence-return relations, and downstream tests. The structure is not evidence; evidence appears only when an evidence pattern governs the claim.

**Improvement-loop slice.** A pattern version has an evaluation frame and current evaluation result. The unfolding structure may relate E.22 `CandidateImprovementProposalRow@Context` values, protected tradeoffs, scale-qualified E.23 `ExpectedEvaluationResultChange@Context` predictions, one `ImprovementLoopDecisionValue`, and re-evaluation. The loop is not improvement by shape; `E.23` governs repeated improvement only after the object version, evaluation frame, proposal rows, expected result changes, loop decision, and stop or return boundaries are recoverable.

**First-entry seed slice.** A README entry says "develop or review architecture." That line may seed an entry unfolding among problem-side records, candidate first governed records, likely governing-pattern returns, and next readable outputs. The README line is a seed description, not the project's unfolding structure and not a universal FPF route.

**Field-filled scaffold slice.** A team has a visible card sequence "problem pressure -> candidate options -> eval -> repair." At first this is a `ProvisionalUnfoldingDemonstrationDescription@Context` about the cooling-design question and proposed continuations. After every admission coordinate below is recoverable, the team may admit the wider CGUS and create a separate demonstrative slice over it:

```text
acceptedStartingRecordReferenceRefs[]: ProblemCard@Cooling-v2 through one acceptedStartingRecord reference; EvaluationResult@thermal-margin-v1 through one acceptedStartingRecord reference
acceptedStartingStructureRefs[]: CurrentModulePlacementStructure@Cooling-v2
declaredStructureSubstrateRef: ArchitectureCandidateSynthesisAndImprovementStructure@Cooling-v2
structurePositionRefs[]: PressurePosition; CandidateSetPosition; EvaluationResultPosition; RepairProposalPosition; ReturnPosition, each with one SlotSpec and direct governing pattern
relationSignatureRefs[]: CandidateEvaluatedByResult; ProposalChangesCandidate; ResultConstrainsDecision; ReturnTargetsGoverningPattern
constraintReferenceRefs[]: ThermalMarginConstraint; ServiceAccessConstraint; AcceptedLossBoundary, each through an exact constraint reference relation
invariantReferenceRefs[]: MaintainableCoolingPathInvariant through one invariant reference relation
guardedTransitionReferenceRefs[]: RepairAdmissionGuard through one guarded-transition reference relation; the guard admits repair only after the evaluation-result relation is current
preservedStructureRefs[]: CandidateAlternativeStructure; RepairLocalityStructure
structureInformationAdequacyNoteRefs[]: TeachingSliceAdequacyNote@Cooling-v2 under C.33, recording omitted rejected-candidate detail and its declared-use effect
admissibleNextFormKindRefs[]: U.Structure for a C.32 candidate-palette update; U.Episteme for an E.22 candidate-improvement proposal row; U.Relation for an ArchitectureDecisionRelation@Project under C.32.PAD
admissibleUseRef: use for planning and demonstrating relations among current positions
nonAdmissibleUseRef: do not infer performed-work order, authorization, or architecture decision from the slice
structureUseReturnBoundaryRefs[]: return to C.32 when a new candidate structure appears; return to E.23 when the changed object version is evaluated
stopBoundaryRef: stop stronger candidate-set or evaluation use when the candidate-set or evaluation relations are no longer recoverable
```

The same visible chain helps planning because each position asks for a slot. It does not make the project follow that order and does not authorize work.

**Local relation repair slice.** Later `EvaluationResult@thermal-margin-v2` becomes the current result for the same cooling candidate. Keep the candidate set, structure positions, service-access constraint, maintainable-cooling-path invariant, and return boundaries. Replace only the referenced `CandidateEvaluatedByResult` relation instance, then re-evaluate `RepairAdmissionGuard` under its direct governing pattern. If the new result does not satisfy the guard, remove `repair candidate` from the admissible next forms and update the demonstrative slice that showed that branch; the unrelated `accept candidate` continuation remains live. A changed result therefore repairs one relation and its dependent guard before it changes a wider graph.

**Schema-completion proxy failure.** A team counts filled CGUS fields and adds weakly used references until the completion count rises. Update effort then grows, practitioners stop repairing changed relation instances, and wrong next-form choices increase. The count describes field population only; it does not establish recoverability, currentness, or practical value. Remove references without a receiving use, evaluate whether practitioners recover the correct live alternatives and smallest repair, and use `E.13` when field completion is substituting for those outcomes.

**Reference-currentness slice.** A SoTA pack relies on telemetry and admitted publication editions that can decay. CGUS may relate the current reference set, edition-shift relations, decay triggers, possible deprecation or reship records, and a return boundary. The structure is not the currentness claim; `G.11` governs freshness, telemetry, decay, deprecation, reship, and no-change claims.

**Physical-modeling slice.** A team models a physical system or another governed EntityOfConcern whose behavior depends on component relations, conservation-like constraints, operating modes, calibration data, and analysis goals. CGUS may relate the model structure, admitted measured data, mode-change relations, compiler boundary, solver boundary, surrogate-substitution relation, and returns to calibration or model-discovery work. In a digital-twin case, the physical entity, digital model, measured-data history, simulation outputs, services, and bidirectional correspondence relations keep their exact kinds and direct governing patterns. A simulation run, generated code, exchange package, AI-assisted model edit, calibration result, and digital-twin publication are separately governed results. Acausal modeling is useful here because it shows that relations and constraints can be stated before a calculation direction is chosen; `C.29`, `G.11`, `E.23`, evidence patterns, and domain DPF patterns govern stronger mathematical, currentness, evaluation, evidence, or domain-validity claims.

**Formal-expression boundary slice.** A team expresses part of the cooling CGUS as a DCR graph or constraint-solver model to check whether the `repair candidate` branch is reachable under `RepairAdmissionGuard`. The expression preserves selected positions, dependency relations, and the guard. It loses direct governing-pattern exits, C.33 adequacy notes, and any relation not encoded in the chosen formalism. Record that preservation and loss under `C.29`, use the output only for the declared reachability question, and return to CGUS before selecting the next form. Satisfiability or reachability does not establish that the expression is the CGUS, prescribe performed-work order, prove architecture adequacy, or authorize work.

**Method-to-work linkage slice.** A method description is admitted because it may realize a governed structure change or change set. CGUS may organize the method relation, work-plan seed, readiness condition, expected structure effect, evidence or gate linkage, and stop condition. It does not authorize work. The method, plan, work-entry readiness, performed work, evidence, assurance, and gate claims remain with A.3, A.15, A.10, B.3, A.20, and A.21.

### A.22.CGUS:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Workflow bias | Name admissible next forms and actual non-workflow boundary. Use work and method patterns only when work or method claims are current. |
| Semio-bias | Treat cards, graphs, tables, route prose, slides, README entries, and narratives as provisional descriptions before admission or admitted demonstrative slices afterward; neither is the governed unfolding structure itself. |
| E.18 parent bias | Use `E.18.3` only for transformation-flow unfolding. Narrative, abduction, grounding, improvement, refresh, and public practical-use guidance keep their direct governing patterns. |
| Shadow-spec bias | Promoted core family cues and README practical-use cards are retrieval or public-guidance aids. They do not outrank pattern bodies, define a second navigation system, or stand in for DPF maps or local governing maps. |
| Lexical trigger bias | Words such as route, path, loop, process, workflow, diffusion, unfolding, graph, or sequence do not admit CGUS by themselves. Run the admission test. |

### A.22.CGUS:7 - Conformance Checklist

| ID | Passing condition | Failed-check repair |
| --- | --- | --- |
| **CC-CGUS-1 Structure kind.** | The object is `ConstraintGovernedUnfoldingStructure@Context <: U.Structure` or a named narrower `U.Structure` specialization. | Lower to note, seed, description, route card, method description, or governing-pattern record. |
| **CC-CGUS-2 Typed positions and cross-position constraints.** | More than one SlotSpec-grounded position is named, and exact relations or constraints among those positions affect admissible continuations. | Add typed positions and their exact relation references, or stop using CGUS. |
| **CC-CGUS-3 Description separation.** | A pre-admission presentation remains a `ProvisionalUnfoldingDemonstrationDescription@Context`; after admission, a whole-structure account is a `ConstraintGovernedUnfoldingStructureDescription@Context`, while one selected traversal is a `DemonstrativeUnfoldingSlice@Context` whose EntityOfConcern is the admitted CGUS. | Keep the presentation provisional until CGUS admission. After admission, choose the description species by whether the episteme describes the admitted topology or selects one traversal through it. |
| **CC-CGUS-4 Direct governing patterns.** | Method, work, evidence, gate, decision, architecture, publication, refresh, and mathematical claims point to direct governing patterns. | Add governing-pattern exits or narrow the claim. |
| **CC-CGUS-5 Non-workflow boundary.** | The structure does not prescribe performed-work order by itself. | Move work-order claims to a work plan or method description if justified. |
| **CC-CGUS-6 Admissible next form.** | At least one admissible next-form kind is named for the admitted structure. | Keep the artifact as a provisional description until a next use and next-form kind are recoverable. |
| **CC-CGUS-7 Stop, return, and currentness reference.** | Stop and return boundaries are recoverable; any currentness claim is an exact referenced relation governed by `G.11`. | Add the boundary or referenced currentness relation, or lower the structure to a one-use explanation. |
| **CC-CGUS-8 Graph-shaped structure coverage.** | If the admitted starting record set, starting structure set, or visible expression is graph-shaped, case-like, or workflow-shaped, branching, joining, cyclic, partial-order, and alternative-live-next-form structure is preserved or explicitly lost. | Do not collapse the object to a chain. Keep the chain provisional before admission, or make it an admitted slice afterward and name the omitted graph structure. |

### A.22.CGUS:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Pretty route as ontology** | A graph, table, route card, or slide deck is treated as the structure, or its declared use is treated as sufficient CGUS admission. | Keep the artifact as a provisional description while any admission coordinate is unresolved. After admission, describe the whole admitted structure with `ConstraintGovernedUnfoldingStructureDescription@Context`, or create a separate `DemonstrativeUnfoldingSlice@Context` only for one selected traversal. |
| **Universal P2W parent** | P2W is used as the parent for architecture, narrative, abduction, grounding, and refresh. | Use P2W as a rich transformation-flow family; use CGUS for the shared constraint-governed unfolding structure and direct governing patterns for each family. |
| **Loop word as improvement** | A retry loop or prompt loop is called improvement. | Open `E.22` and `E.23`; improvement-loop admission depends on an object version, evaluation frame, exact candidate proposal rows, scale-qualified expected evaluation-result changes, one loop-decision value, and re-evaluation. |
| **README route authority** | A public practical-use card is treated as a fixed FPF procedure. | Return to its `E.11` card expansion and express each continuation through its condition, direct pattern, exact first result, and stop or return boundary. If the explanation claims one wider conditional structure, keep it as `ProvisionalUnfoldingDemonstrationDescription@Context` until A.22.CGUS admission; only then may a separate `DemonstrativeUnfoldingSlice@Context` show one traversal. |
| **Diffusion ontology import** | The diffusion analogy becomes mathematical diffusion, fixed point, CSP, sheaf, or category semantics. | Keep the analogy explanatory only; open `C.29` by a new decision if a mathematical lens is claimed. |
| **Solver or agent as ontology** | An execution artifact, such as a solver run, compiler output, or AI-assisted model edit, is treated as the governed unfolding structure. | Separate the reusable model structure from the execution or publication artifact. Use CGUS for the relation and constraint structure; use the direct mathematical, currentness, evaluation, evidence, publication, or domain pattern for the stronger claim. |

### A.22.CGUS:9 - Consequences

CGUS gives FPF a way to preserve route-shaped usefulness without turning route-shaped artifacts into workflows. A practitioner can see admitted starting records, current starting structures, constraints, possible next forms, alternatives, and return conditions while still knowing which direct pattern governs method, work, evidence, gate, decision, architecture, publication, refresh, or mathematical use.

The cost is extra kind discipline. CGUS admission depends on named typed positions, exact relation references, cross-position constraints, preserved structures, C.33 adequacy notes where the presentation omits relevant structure, non-admissible overreads, and direct pattern exits. If that is too heavy, the right result is a compact provisional demonstration description; an admitted demonstrative slice becomes available only after the wider CGUS exists.

### A.22.CGUS:10 - Rationale

The selected design is a thin A.22 specialization of `U.Structure` because the recurring object is real but not a new root ontology. Constraint-based process modeling, case-management practice, artifact-centric modeling, acausal modeling, architecture-description practice, and FPF's own pattern use all separate a constraint-bearing structure from a performed trace, work order, view, publication, solver run, or example path. FPF adopts that separation as a constraint-governed unfolding structure and refuses to import one universal process calculus.

Physical modeling makes the same distinction concrete. In acausal modeling, component relations, quantities conserved across connections, and mode conditions can be declared before the model is compiled and solved in one chosen direction. The FPF import is only the general architecture of the move: structure and constraints first; derived calculation, demonstration, calibration, publication, or work use later under direct governing patterns.

CGUS is deliberately close to A.22. It is a `U.Structure` over a declared substrate in a bounded context. Descriptions, views, graph renderings, route cards, README entries, and examples help humans use it; they do not become it.

### A.22.CGUS:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| Object Management Group, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Use as lineage for the weakly structured case-work pressure: possible work items and constraints may be visible without selecting one performed-work order. | CMMN is not treated as current best-known process practice. Do not import its notation or treat CGUS as a case-management method. |
| Esser and Fahland, "OCPQ: Object-Centric Process Querying & Constraints", arXiv:2506.11541, 2025 | Adopt the current object-centric pressure that several typed objects and their relations can jointly determine a constraint query. This reinforces graph-shaped starts, joins, many-to-many dependencies, and relation-preserving continuation without reducing the case to one trace. | OCPQ governs event-data querying and constraint checking. CGUS does not import event-log, query-language, or process-mining ontology, and a query result does not become the unfolding structure. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Use as declarative-process lineage for constraints and multiple typed perspectives that admit traces without first selecting one imperative sequence. | FPF does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011 | Use as DCR lineage for keeping conditions, responses, inclusions, exclusions, role assignments, and distribution relations distinct. | Do not import DCR graph semantics as FPF workflow ontology. |
| Bagheri Hariri, Calvanese, Montali, Santoso, and Solomakhin, "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013, with artifact-centric and GSM lineage | Use as artifact-centric lineage for object state, stages, milestones, guards, and state transitions as pressure for typed positions and guarded relation changes. | CGUS does not become an artifact lifecycle method, database schema, or verification method. |
| Modelica Association, *Modelica Language Specification* 3.7 (2026); JuliaHub, Dyad documentation 3.1.0 (2026-06-10), including acausal component and analysis documentation | Adopt the current relation-first modeling practice: reusable components expose relations, connection constraints, units, conservation relations, and modes before one causal direction, analysis, compiler output, solver run, or simulation trace is selected. | FPF does not import DAE, Modelica, Dyad, solver, compiler, or AI-agent ontology. An analysis, solver run, compiler output, or AI-assisted edit is a use over a model structure, not the CGUS itself. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use the model-toolchain separation to preserve the distinct kinds and relations of reusable symbolic model structures, structural transformations, analysis records, calibration records, model-discovery records, surrogate-substitution relations, model-exchange packages, and result publications. | FPF does not import FMI, digital-twin, ML-surrogate, calibration, or co-simulation ontology. Mathematical model claims use `C.29`; currentness, evaluation, evidence, publication, and domain-validity claims exit to their direct governing patterns. |
| FPF pattern-language practice | Use provisional demonstrations before structure admission and demonstrative slices afterward, while keeping pattern bodies as governing authority. | A first-entry route, example, or public card is neither admission evidence by itself nor the specification. |

As of 2026-07-11, OCPQ supplies the current research comparator for typed multi-object constraint queries, while Modelica 3.7 and Dyad 3.1.0 supply the current engineering comparator for relation-first acausal models separated from analyses and execution artifacts. The older CMMN, Declare, DCR, and artifact-centric rows provide lineage and known distinctions, not present-day authority by age or official status. These sources changed `4.2` by requiring graph-shaped and many-to-many recovery, `4.3` by separating a demonstration from the wider structure, and the physical-modeling slice by separating reusable relations from analysis and execution. Reopen these adoptions when a newer object-centric constraint method changes the treatment of objects or relations, when the modeling languages change component-relation or analysis separation, or when use evidence shows that the imported distinction no longer prevents chain or execution-artifact overread.

### A.22.CGUS:12 - Relations

Specializes: the `A.22` use of `U.Structure` when the selected structure is `ConstraintGovernedUnfoldingStructure@Context` and its typed positions, exact referenced relations, cross-position constraints, preserved structures, C.33 adequacy notes, admissible next-form kinds, and direct governing-pattern exits are current.

Specialized by: `E.18.3` for transformation-flow unfolding structures, and by local blocks in `E.18.1`, `C.32.P2S`, `B.5.2`, `A.6.3.NAR`, `E.23`, `C.13`, `B.3.5`, and `C.3` when their admission tests pass.

Coordinates with: `E.11` for public practical-use card expansions, ordinary walkthroughs, and admitted CGUS-demonstrative walkthroughs, `E.10.MOVE` and `C.2.P.DR` for lexical and declarative-representation repair, `C.18`, `C.19`, and `G.5` for archive, front, live-pool, and selected-set claims, `G.11` for currentness and refresh claims, and `E.17` for publication of provisional descriptions or admitted demonstrative slices.

Does not replace: `A.3.1`, `A.3.2`, `A.15`, `A.10`, `B.3`, `A.20`, `A.21`, `C.30`, `C.32.PAD`, `C.32.ADR`, `C.29`, `G.11`, or any direct governing pattern for stronger claims.

### A.22.CGUS:End

