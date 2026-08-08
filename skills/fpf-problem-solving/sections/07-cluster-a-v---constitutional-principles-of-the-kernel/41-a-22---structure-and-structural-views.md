## A.22 - Structure and Structural Views (STRUCT-CAL)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to select `U.Structure` as the `EntityOfConcern`: an organization among exact constituents and obtaining relations, selected to expose a relation class, applied constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes the next engineering or reasoning action.

The first A.22 question is not “which diagram or record shows the structure?” It is “which organization is selected for this named use?” Recover that organization in this order:

1. identify every constituent independently through the content that defines its kind and identity;
2. recover the exact relation occurrences among those constituents that actually obtain under their direct predicates;
3. state the exact constraints applied to those constituents and relations, plus the named selection-use frame that says what question or action this organization serves;
4. name the resulting selected organization and the admissible action or stop that follows.

When the use makes a load-bearing claim that a structure was selected, also recover the selecting system, its dated selection work and exact method-enactment relation, and the exact participant relations or A.6.1 bindings used by that work. Those neighboring facts support the selection judgment; they do not enter `U.Structure` identity. If the judgment must persist, identify a separate C.2.1 result episteme whose claim content designates the selected structure.

The first useful move is small:

```text
StructureQuestionCard@Project:
  named selection use:
  independently identified constituents:
  exact obtaining relation occurrences selected:
  constraints applied:
  selected structure:
  preserved structure:
  lost, hidden, or excluded structure:
  admissible action:
  stop or non-admissible overread:
  selecting system, method, and dated work, when selection is claimed:
  selection-result episteme, when a durable result is needed:
  claim scope or effective reference scheme of that claim, if current:
  reliance relation, if a neighboring reliance claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

Here `@Project` is a compatibility and retrieval cue, not a type or relation assertion. It identifies neither a project entity nor a composite project `U.Work`, and it establishes no context, authority, viewpoint, or parthood. When this card is used in relation to one actual project, name that exact composite `U.Work` and the relation by which the current structure-selection work, decision, description, or other identified object concerns it. Otherwise no project-work reference is implied. The same rule applies to `ArchitectureStructureKindTriage@Project` below.

Stop at this card when it makes the next structure use clear. Open heavier records only when a named description, view, publication, extraction, coarsening, comparison, mathematical-lens, architecture-description, or other neighboring claim is being made.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source publication, source-use record, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source-basis or lens reliance only when it is being claimed, add a `StructureUseReturnCondition` when loss matters, and apply the FPF definition or test for any non-structure claim being made.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim, use the pattern that defines or tests that claim and keep A.22 only to the selected-structure portion.

Thin precision-restoration pointer: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another exact claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

### A.22:2 - Problem

FPF needs a selected-structure EntityOfConcern that is useful before any one domain ontology, mathematical formalism, architecture notation, or publication form takes over. Working projects often notice that "the structure" is doing real work:

- dependencies repeat across cases;
- a method or work description hides an invariant relation;
- a model compresses a trace by preserving one relation class and losing others;
- a diagram shows an arrangement but is mistaken for the arrangement itself;
- a mathematical lens exposes preserved structure but is then overread as ontology;
- an architecture discussion needs selected structure over a holon before it can describe architecture.

How can FPF let a practitioner name structure as an EntityOfConcern while preserving the distinction between:

- selected structure and the source-description relation, source-use relation, evidence relation, lens output, simulation, generated representation, or declared substrate from which it was inferred or declared;
- structure and a Description episteme or view of that structure;
- structure and a publication face, diagram, table, graph, or publication form;
- structure and mathematical-lens application;
- structure and another FPF claim kind whose definition or test remains in the cited pattern;
- structure in general and architecture-specific structure selected by `C.30`.

### A.22:3 - Forces

| Force | Tension |
| --- | --- |
| First-principles structure EntityOfConcern vs ontology inflation | FPF needs a reusable selected-structure EntityOfConcern for organizations that expose relations, applied constraints, invariants, variation classes, preserved arrangement, and lost arrangement, but adding one such EntityOfConcern can accidentally invite many false root kinds. |
| Useful compression vs structure-use return | Structure makes work easier by compressing cases, but a `StructureUseReturnCondition` is needed when compression, extraction, coarsening, source-description reuse, base-dependence reuse, grounding reuse, evidence reuse, lens reuse, simulation reuse, or representation reuse hides a distinction needed for action. |
| Description and view usability vs structure confusion | Descriptions and views make structure inspectable, but a useful view can be mistaken for the structure itself. |
| Mathematical-lens application vs mathematical overread | C.29 lenses can expose structure, but lens output does not become the structure and does not license evidence, causal, assurance, or decision claims by itself. |
| Architecture dependency vs architecture takeover | Architecture uses selected structure through `C.30`; A.22 does not import architecture as its parent or make every structure an architecture. |
| Plain engineering speech vs Tech recovery | Words such as structure, graph, architecture, module, function, interface, pattern, block, layer, level, tier, stack, expert, cache, router, and gate can remain in Plain prose, but FPF use needs recoverable Tech fields and pattern applications. Use `C.30.STRAT` to recover source labels before A.22 accepts a selected-structure portion. |

### A.22:4 - Solution

Select `U.Structure` as the A.22 ontic head: a dependent, non-agentive organization selected from independently identified constituents and exact obtaining relation occurrences under applied constraints for one named use frame.

The constituents keep their own identities and kinds. Every selected relation occurrence must already satisfy its defining predicate and retain identity under that predicate's occurrence rule. A.22 neither creates those participants nor makes their relations obtain. A system or practitioner selects their organization; A.22 supplies the identity and boundary rule for that selected organization.

The applied constraints are the exact constraint claims used in the selection judgment, not the identity of the document, table, rule card, or constraint episteme that carries them. The named use frame states the question being answered, the admissible action, and the non-admissible overread. A generic phrase such as “current use” or “appropriate structure” is not a use frame.

A system may perform dated structure-selection work by an exact method and may create a result episteme about the selected structure. The system acts; the pattern, constraints, graph, result, and structure do not. The method, work, A.6.1 binding or direct participation relation, decision, and C.2.1 result episteme are neighboring objects. None constitutes or reidentifies the structure.

A diagram, graph, table, model, description, view, or publication may designate, represent, or describe the selected organization and its already identified constituents. Its form does not establish a constituent's identity, make a relation obtain, or select a structure. Use C.29, C.2.1, E.17.0, and the exact publication or source-use patterns for those neighboring claims.

#### A.22:4.1 - Base `U.Structure` Identity and Selection

For a selected structure `S`, recover four identity discriminators:

```text
StructureIdentity(S) = <
  exact independently identified constituents,
  exact selected obtaining relation occurrences,
  exact constraints as applied,
  one named selection-use frame
>
```

Base `U.Structure` identity has no ambient context field. A bounded-context label, `U.ContextSlice`, `U.ClaimScope`, project record, description, view, graph, table, or publication is not automatically an additional discriminator. If an exact scope is referenced by an applied constraint, that constraint contributes through the third discriminator. If a model-use structure is independently selected as a constituent of another structure, it contributes through the first discriminator.

The first discriminator is an exact plurality, not a graph node set created by notation. A separately useful C.13 collection may designate the same constituents, but collection membership neither proves parthood nor replaces their direct identities. The second discriminator contains the exact relation occurrences chosen for this organization; a relation name, edge label, tuple position, or adjacency row is insufficient. The third contains the semantic constraints actually applied; changing only the rationale, formatting, or publication of an unchanged constraint claim does not change this discriminator. The fourth names the use question and its admissible action or stop.

Two references resolve to the same `U.Structure` when all four discriminators resolve to the same values. A changed designator, selecting system, method, work occurrence, result episteme, description, graph, representation scheme, view, or publication leaves the structure unchanged when the four discriminators remain unchanged. Replacing a constituent, a selected relation occurrence, an applied constraint, or the named use frame can identify another structure. If a relation occurrence itself may have been reidentified, apply its direct relation pattern before reapplying A.22.

If no current predicate definition, applicability condition, or occurrence rule can identify the required constituent or test the obtaining-relation claim for this use, stop at the exact description or representation and return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact needed to decide the test is unavailable, return `missing-information`. State a negative only when an applicable non-obtaining criterion or complete closure basis and satisfying facts establish it. If the constraints or named use frame are absent, name that exact gap: the material may show an arrangement, but it does not yet support the claimed selected `U.Structure`.

The following two compact records are recovery aids, not new ontic kinds. In `SelectedStructureBasis`, the selected structure, constituents, selected obtaining relations, applied constraints, and use frame state identity; the preserved/lost and action/stop rows state the use-return boundary rather than adding identity fields.

```text
SelectedStructureBasis:
  selectedStructureRef:
  constituentRefs:
  selectedObtainingRelationOccurrenceRefs:
  appliedConstraintClaimRefs:
  namedSelectionUseFrame:
  preservedStructure:
  lostHiddenOrExcludedStructure:
  admissibleAction:
  stopOrNonAdmissibleUse:

StructureSelectionUse:
  selectingSystemRef:
  selectionMethodRef:
  selectionWorkRef:
  directParticipationOrOperationBindingRefs:
  selectedStructureRef:
  selectionResultEpistemeRef?, when the judgment must persist:
  selectionDecisionRef?, when an accountable choice is current:
```

`StructureSelectionUse` records how a system performed the selection and reached the judgment. `SelectedStructureBasis` records the four identity discriminators plus the use-return boundary. Do not copy the system, work, method, result episteme, or decision into the structure basis. A `U.ClaimScope`, effective `U.ReferenceScheme`, or model-use structure that merely qualifies a claim about either record does not enter base identity. A scope referenced by an applied constraint or a model-use structure selected as a constituent enters only through that already declared discriminator.

A.22 structure-aspect names such as functional, mereological, modular, transformation-flow, control, semantic, causal, dynamical, algebraic, topological, geometric, or coarse-grained remain cues for which relations and constraints to recover. They do not identify a structure without the four discriminators. C.30.ASV `ArchitectureStructureKindRef` values remain architecture-local classifiers; a matching label does not imply identity.

#### A.22:4.1a - Compact auxiliary boundary

Use description, publication, source-use, evidence, work, gate, decision, release, architecture-description, and mathematical-lens patterns when those claims are being made. The A.22 application contains the selected-structure portion and the structure-use return condition that protects that structure use; use each neighboring pattern only for the definition or test it contributes. A publication, diagram, graph, table, dashboard, file, model card, generated representation, or lens output may make a structural description or view available; it does not become the selected structure or supply neighboring claim authority by appearance.

#### A.22:4.1b - Constraint-governed unfolding structure

Use `A.22.CGUS` when the current A.22 structure is an organization among several identified loci and constraints: admitted starting records, already-current starting structures, relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, admissible next forms, and conditions for stop, return, split, or currentness refresh. This structure specialization is still `U.Structure`; it is not a route, workflow, method, work plan, performed work, decision, evidence relation, gate, architecture description, or publication.

Open `A.22.CGUS` only when the candidate has several loci and cross-locus constraints. A route card, table, graph, README entry, narrative, slide, or happy-path example may describe or demonstrate the unfolding structure, but it is not the structure itself.

#### A.22:4.1c - Bounded And Cross-Context Model-Use Structure Specializations

`BoundedModelUseStructure` is a `U.Structure` selected over one exact model episteme, exact admitted model-use holons, the obtaining model-applicability, actual model-use, and model-expression-coherence occurrences defined and tested by A.1.1, exact applied constraint claims used by the selection judgment, and one named bounded-model-use frame. Its A.22 identity uses exactly those constituents, selected occurrences, exact constraint claims, and frame. A claim scope, membership outcome, boundary display, or carrier is not an applied constraint by itself; a constraint claim may instead state a proposition about that scope or its A.2.6 membership predicate. No boundary crossing participates in that identity. Continuity across model editions additionally requires the exact C.2.1 episteme-edition relation and declared A.1.1 continuity rule. It is not a holon, description, view, or endpoint manufactured by a later crossing.

`CrossContextRelationStructure` is a conditional specialization of a different already identified `U.Structure`. Membership requires exact obtaining crossing occurrences that satisfy independently defined predicates, selected among several bounded model-use structures, applied constraints, and one named crossing-analysis use, with all four A.22 base discriminators established. Until a compatible crossing predicate and current facts establish those occurrences, a Context Map can describe only a proposed crossing organization and no positive `CrossContextRelationStructure` member is asserted. The selecting system and its work remain separate. Sharing a participant does not merge structures, and overlap does not prove parthood.

**Pending local name settlement.** The following F.18 NameCard is local to A.22 while the positive crossing-occurrence basis is unavailable. It does not create the structures, crossing relations, mapping method, or view.

```text
NameCard:
  NameCardId: NC-CROSS-CONTEXT-RELATION-STRUCTURE
  GovernedValueRef: U.Structure selected over several BoundedModelUseStructure values and their exact crossing relations
  SubjectPatternLocator: A.22
  ReferenceScheme: FPFCoreReferenceScheme
  LocalSenseRef: conditional selected organization of independently defined obtaining crossings among several bounded model-use structures under all four A.22 base discriminators; a Context Map may describe only a proposed organization until that exact positive basis exists
  TechLabel: CrossContextRelationStructure
  PlainLabel: relations among bounded contexts
  CandidateSet: CrossContextRelationStructure; BoundedContextRelationStructure; ContextRelationStructure; ContextMapStructure
  RejectedCandidates: BoundedContextRelationStructure hides plurality; ContextRelationStructure leaves the endpoint kind unresolved; ContextMapStructure confuses the structure with the DDD view and FPF Map
  SelectionRationale: reserve one local retrieval label for the conditional cross-structure rule without retyping its proposed description, view, diagram, or publication as an admitted structure
  PublicRowStatus: pending
  LineageEntries: replaces broad context-map and bounded-context-relation wording
  RefreshCondition: reopen when an independently defined crossing relation obtains and one positive A.22 membership witness is available; only then rerun F.18/F.17 for public reuse
```

This pending card has no `UnifiedTermRowRef`. Until its refresh condition is met, `CrossContextRelationStructure` is an A.22-local provisional designator only; other Core hosts must cite the descriptive A.22 conditional cross-structure rule rather than consume that label as public vocabulary.

DDD `Context Mapping` names a repeatable `U.Method`. A.15.2 defines the intended mapping plan; A.15.1 identifies each exact dated mapping Work individual admitted under `U.Work`, the performer system and obtaining role assignment, and the exact `enactsMethod` relation. C.2.1 independently identifies the candidate episteme called a `Context Map`. While exact independently defined crossing occurrences or the four A.22 base discriminators are missing, its EntityOfConcern is the proposed or described crossing organization, not an exact `CrossContextRelationStructure`. Only after both conditions are met may a corresponding C.2.1 episteme designate the exact structure. Either episteme is additionally a `U.View` only when the E.17.0 test establishes `EpistemeViewpointConformanceRelation(E, P)`. Use C.29 for any representation relation and E.17/E.24.PUB for rendering or publication; form and carrier remain separate. Thus method, plan, work, proposal, selected structure, candidate episteme, dependent view membership, representation, and publication stay distinct while the external source terms remain retrievable.

#### A.22:4.1d - Transformation-flow structure network profile

Use `E.18.NET` when one engineering use selects two or more independently identified transformation-flow structures, or nested networks of them, together with exact obtaining relations across their boundaries. Apply the four A.22 discriminators directly: the exact TFS or nested-network members are the constituents; the exact cross-member relation occurrences satisfy their defining predicates and identity rules; the exact applied endpoint, boundary-exposure, and acyclic direct-member constraints are selected under E.18.NET; and the named network-use frame states the practical question or action and the forbidden overread. Record the return condition separately; it reopens selection when a member, relation, constraint, or use-frame value changes and is not a fifth identity discriminator. The result is one dependent, non-agentive `U.Structure` specialization. E.18.NET defines the network's detailed identity, reference, recursion, local-state, and conformance rules; A.22 does not copy those fields.

Selecting a constituent in the first discriminator does not create a separately re-identifiable membership occurrence. A member row, graph edge, containment picture, or shared label proves neither membership nor another relation. If a receiving use genuinely needs a world-side membership relation, recover its participants, obtaining predicate, and identity rule; otherwise use the exact constituent discriminator and do not mint a generic membership edge.

#### A.22:4.2 - Structure claim reliance relation selection


A.22 does not mint a local generic reliance record. When a structure claim relies on something beyond the selected structure itself, choose the reliance relation kind, name the relation record by value, and name the definition or test used for that relation:

| Current reliance relation kind | What is named | Definition or test to apply |
| --- | --- | --- |
| Source-description relation | source episteme, source view, publication form or rendering where relevant, described structure or structure claim, source-basis pins or structure-use return condition, admissible and non-admissible use | `A.7`, `A.6.3`, `E.17`, `E.17.0`, and local source-publication rules |
| Base-dependence or basedness | `dependent = structure claim or structural description`, `base`, declared `baseRelation`, scope, declared `Γ_time` when temporal scope is claimed, witness refs when witness use is claimed, admissible and non-admissible use | `A.6.6` SWBD or Context-local SWBD specialization |
| EntityOfConcern or grounding-holon grounding | selected EntityOfConcern, `GroundingHolonSlot` when grounding-holon grounding is being claimed, effective reference scheme, claim scope, optional model-use structure, viewpoint, reference plane, and observation or witness condition when current | `C.2.1`, `A.2.6`, `A.6.4`, `A.6.3.RT`, `A.6.6` only if it is a base-dependence claim |
| Evidence or witness reliance | evidence-use relation, evidence-provenance relation, claim ref, witness publication or observation record, timespan and freshness; if an evidence graph is current, its graph path remains a mathematical or provenance expression rather than an action route | `A.10`, `A.2.4`, `G.6` |
| Mathematical-lens reliance | lens candidate, lens card, or lens-use record; primary `EntityOfConcern`; relation record or claim record named by value when lens reliance is being claimed; preserved structure; lost structure; stop condition; `MathLensUseOutputRef`; C.29 lens-use result; or `LensUseAdmissibilityValue` | `C.29`, `C.26`, `F.9`, named mathematical-lens pattern |
| Simulation, generated representation, model, or extracted trace | source publication or representation publication, extraction method, validation boundary, preserved structure, lost structure, structure-use return condition | source-description and Description-context patterns plus `C.29`, `A.10`, or the pattern that defines or tests the exact claim |

If no reliance relation kind can be selected, keep the wording as a source-finding note, recognition cue, ordinary help, quote-only wording, or reduced-use cue. Do not create a generic reliance record to make the claim look resolved.

`U.Structure` does not carry description, representation, extraction, mathematical-lens, simulation, or generic reliance state as an internal structure field. Those are source-description, source-use, base-dependence, evidence, lens, extraction, simulation, or publication relations about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, SWBD, or lens output.

#### A.22:4.3 - Structural descriptions and views

Structural descriptions and views reuse existing episteme and view machinery. Architecture does not define a second ontology of descriptions, views, viewpoint bundles, multi-view descriptions, publications, publication forms, or source-pin sets. Every record whose name ends in `Description@Context` here is an existing `U.Episteme`: `C.2.1` supplies its identity and `E.10.D2` constrains its describing use. Every record whose name ends in `View@Context` here remains that same episteme and has `U.View` membership only when the E.17.0 conformance test to an exact viewpoint episteme passes. A.6.3 supplies only an optional source-to-receiving construction. `DescriptionContext` is imported, not locally redefined.

```text
StructuralDescription@Context ::= {
  descriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse
}

StructuralView@Context ::= {
  viewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  structureRefs: FinSet(U.StructureRef),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse
}
```

`descriptionContext.ViewpointRef` is the viewpoint field. When reliance is on a named claim, `U.EpistemeRef` resolves the exact C.2.1 claim-bearing episteme; a PatternID normally locates the definition, constraint, or test it uses, and an exact ClaimGraph is added only when that identity changes the use. Do not duplicate the viewpoint field locally under another name unless another cited pattern defines a more specific view record.

#### A.22:4.4 - Extracted and transformed structural views

Use extracted or transformed structure records when a corpus, trace, model, lens, simulation, generated representation, coarsening pass, observer boundary, or budget boundary produces a view of structure that may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  sourceCorpusOrTraceRefs,
  structureRefs: FinSet(U.StructureRef),
  extractionDescriptionRef,
  preservedStructure,
  lostStructure,
  validationBoundary,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructureExtractionDescription@Context ::= {
  extractionDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  sourceInputKind,
  lensOrMethodRef,
  budgetOrObserverBoundary?,
  preservedStructureKinds,
  lostStructureKinds,
  validationBoundary,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}

StructuralAspectDescription@Context ::= {
  aspectDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  aspectKindRef,
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  admissibleUse,
  nonAdmissibleUse
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, EffectiveReferenceScheme, ViewpointRef?, ModelUseStructureRef?),
  sourceStructureRefs: FinSet(U.StructureRef),
  resultStructureRefs: FinSet(U.StructureRef),
  preservedUnder,
  brokenBy,
  lostStructure,
  structureUseReturnCondition,
  admissibleUse,
  nonAdmissibleUse
}
```

#### A.22:4.5 - Structure-use return

`StructureUseReturnCondition` is present when compression, extraction, coarsening, evidence reuse, mathematical-lens use, simulation, ML evaluation, bounded exception, many-to-many allocation, or decision reliance hides a distinction needed for action, assurance, causal use, legal review, regulatory review, comparison, or subsequent decision reopening.

Do not make structure-use return mandatory for ordinary local recognition when no hidden distinction is being used for action. The condition is needed only when the repaired text still relies on a hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinction.

#### A.22:4.6 - Relation to architecture
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over structures selected by `ArchitectureOf@Context` and typed by `ArchitectureStructureKindRef`.

A.22 is intentionally upstream of C.30. Architecture uses structure; structure does not import architecture as a parent.

`C.30` uses A.22 by selecting architecture-relevant structures for one described holon through `ArchitectureOf@Context`. `C.30.ASV` then defines and tests architecture structural views over those selected structures. A structure can be used by architecture, but a structure is not an architecture merely because an architecture description refers to it.

Architecture-related records that belong to C.30 or its subpatterns include `ArchitectureOf@Context`, `ArchitectureDescription@Context`, `ArchitectureStructuralView@Context`, `ArchitectureStructureKindRef`, `ArchitectureStructureKindTriage@Project`, `FunctionalStructureView@Context`, `ArchitectureTransformationFlowStructureRelation@Context`, `ControlStructureView@Context`, and `CrossScopeArchitectureResidualTriage@Context`. A.22 may name them as FPF pattern applications. It does not define their architecture-specific conformance.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The reliance relation is treated as the structure. | Recover the exact constituents, selected obtaining relation occurrences, applied constraints, and named use frame. When a neighboring source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance claim is current, name that exact relation and the content that defines or tests it separately. |
| The diagram, graph, table, dashboard, or publication form is the structure. | Treat it as publication, description, view, publication form, source-description relation, base-dependence relation, grounding relation, evidence relation, lens relation, simulation relation, extraction relation, or representation relation only when its relation is explicit. |
| A transformation-flow graph expression is the structure in every sense. | Use `E.18` for one selected TFS and its internal paths, crossings, and valuations; use `E.18.NET` for a selected network of independently identified TFS members and exact cross-member relations; use `E.18.2` and `C.29` for the graph expression. A.22 supplies only the selected-structure identity, and `C.30.TFS-REL` defines and tests the architecture-to-transformation-flow relation claim. |
| A mathematical lens output is the structure. | Use `C.29` for lens-use result and admissibility, and cite `MathLensUseOutputRef` only through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| A structure proves evidence, assurance, safety, causality, or gate passage. | Assign those claims to `A.10`, `G.6`, `B.3`, `C.28`, `A.20`, or `A.21`. |
| A structure is a decision or work record. | Use `C.11`, `A.20`, `A.21`, `A.15`, or the project-side decision pattern whose test answers the claim being made. |
| Architecture is a root kind beside structure. | Use `C.30`: architecture is selected structure for a described holon through `ArchitectureOf@Context`. |
| Function, module, interface, platform, layer, stack, block, expert, cache, router, or gate becomes a root kind by appearing in structure prose. | Use `C.30.STRAT` for source-label recovery, then `A.6.F`, `A.6.M` module-relation repair when a module-interface claim is being made, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.P:4.11a`, `E.18`, `C.30.ASV`, and any other definition or test required by the recovered claim. |

#### A.22:4.8 - Worked slices

**Maintenance-isolation structure selection.** A planner needs to choose which relations matter when isolating a pump skid for maintenance.

```text
named selection use: choose isolation points before Pump_37 maintenance
constituents: independently identified Pump_37, Motor_12, Valve_In_4, Valve_Out_4, and Bus_7
selected obtaining relations: exact installed-with, connected-to, supplied-by, and upstream-of occurrences that currently satisfy their defining predicates
applied constraints: isolate every live energy and material path to Pump_37; retain only relations relevant to this isolation use
selecting system: MaintenancePlanner_A
method and work: IsolationStructureSelectionMethod enacted in SelectionWork_2026-07-25
selected structure: Pump37_MaintenanceIsolationStructure
admissible action: prepare the isolation sequence from the selected paths
stop: reopen selection when a constituent, selected occurrence, or isolation constraint changes
```

`Pump37_MaintenanceIsolationStructure` is identified by the exact constituents, exact selected obtaining occurrences, applied isolation constraints, and maintenance-isolation use frame. `SelectionWork_2026-07-25`, the enacted method, and any C.2.1 episteme that records the judgment remain separate. A graph can represent the same organization under C.29; an edge in that graph neither makes its relation obtain nor replaces the exact relation occurrence. A near miss is a visually identical graph assembled from labels when one connection has not been established: it is a representation candidate, not the selected structure claimed above.

**Architecture kernel slice.** A team says, "the architecture is the graph." A.22 does not accept that sentence as a root-kind claim. The repair is:

```text
declaredStructureSubstrateRef: TransformationFlowStructureRef under E.18, with mathematical graph description under E.18.2 when that expression is the current claim
candidate structure: selected transformation-flow structure
structure-claim reliance relation: selected relation record named by value(
  sourceDescriptionOrPatternApplicationRef = SourceViewRef, E.18 selected structure or crossing record, or E.18.2 mathematical graph description,
  relationContribution = E.18 selected-structure or crossing definition | A.6.6 base-dependence test | A.10 evidence, source-provenance, or reliance test | C.29 mathematical-lens result, chosen for the claim being made,
  relationKind = source-description | base-dependence | evidence | lens, selected for this reliance,
  validationBoundary = graph-path currentness boundary, slice currentness boundary, or crossing currentness boundary
)
next FPF pattern application: C.30.TFS-REL when this selected structure is used in an architecture-to-transformation-flow relation
non-admissible use: graph as whole architecture, work, evidence, gate, or decision
```

The useful structure use survives: the practitioner can use the graph through the selected source-description, base-dependence, evidence, or lens relation without turning it into architecture ontology.

**Extracted code structure slice.** A code-agent relation graph or probe JSON reports imports, calls, registry wiring, and data-flow links. A.22 treats it as an extracted structural view only when the source codebase or publication, extraction method, preserved structure, lost structure, validation boundary, and structure-use return condition are named. The relation graph or probe output is not the codebase architecture itself and is not proof of internal agent belief, assurance, or release readiness.

```text
ExtractedStructuralView@Context:
  sourceCorpusOrTraceRefs: repo snapshot, probe outputs, traces
  preservedStructure: selected typed relation families
  lostStructure: unexplored regions, dynamic calls, hidden generated code, ambiguous relation kinds
  validationBoundary: probe coverage and source codebase or publication edition
  structureUseReturnCondition: when an architecture decision, assurance use, or repair depends on a relation not observed by the extraction
```

### A.22:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees an arrangement that matters but does not yet know whether it is a diagram, a model, a graph, an architecture claim, a source description, base-dependence relation, evidence relation, lens relation, or decision. A.22 asks first: which exact constituents and obtaining relations are selected, under which applied constraints and named use frame, and what loss changes the next action? |
| Show: `U.System` | In a plant, vehicle, software system, or neural-network model, the selected structure may be transformation-flow, control, module-interface structure, placement, information, scale, or declared logical structure. The structure record does not become the system and does not prove that the system is safe, maintainable, or ready. |
| Show: `U.Episteme` | A paper, model, generated relation graph, dashboard, architecture note, or mathematical-lens output can describe selected structure or serve as a source-description or A.6.6 base-dependence relation for a selected-structure claim. The episteme, view, or publication is not the structure itself; it carries a description, view, or reliance relation named by value with validation and structure-use return boundaries. |

### A.22:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: universal within FPF structure claims.

| Bias risk | Mitigation |
| --- | --- |
| Architecture bias | Do not make architecture the parent of all structure. A.22 stays upstream; C.30 carries grounded architecture and selected-structure adequacy. |
| Mathematical-formalism bias | A mathematical lens can expose preserved structure and lost structure, but C.29 still defines the lens-use result, admissibility, and stop condition. |
| Diagram bias | A useful diagram or generated relation graph is attractive enough to be mistaken for the structure. description, specification-use, and publication boundaries stay explicit. |
| Review-only bias | Checks leave a repair action: name the structure, name the structure-claim reliance relation record by value, state a structural view, add a `StructureUseReturnCondition`, or apply the FPF definition or test needed by the claim. |
| Didactic-thinning risk | Semantic repair does not leave inert prose. The recognition text keeps the first useful move and the practical payoff visible before the formal records. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### A.22:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Base identity.** | The selected `U.Structure` is recoverable from exact independently identified constituents, exact selected obtaining relation occurrences, exact constraints as applied, and one named selection-use frame. | Recover the missing discriminator. If a constituent lacks its defining identity content or a relation lacks its predicate or occurrence rule, stop at that blocker rather than naming a structure from a graph or record. |
| **CC-A22-1a Independent grounding.** | Every constituent and selected relation occurrence keeps its direct identity; a collection, constraint episteme, graph, table, description, view, or publication neither creates them nor makes a relation obtain. | Apply the constituent and direct relation patterns first; treat the visible artifact as a C.29 representation or C.2.1 episteme only when that is what is present. |
| **CC-A22-1b Selection work and result separation.** | When a load-bearing selection claim is current, an exact system performs dated work with an exact method-enactment relation and exact participation relations or A.6.1 bindings. Any durable result is a separate C.2.1 episteme, and any accountable choice uses its decision predicate and test. | Name the acting system, method, work, bindings, and result or decision separately; remove them from structure identity. |
| **CC-A22-1c Reidentification.** | A changed designator, method, work, result episteme, graph, description, or publication leaves the structure unchanged when all four identity discriminators remain unchanged; a changed discriminator reopens identity. | Compare the four discriminators and apply each selected relation occurrence's direct identity rule before reapplying A.22. |
| **CC-A22-1d Transformation-flow network profile.** | An E.18.NET value applies all four A.22 discriminators to exact TFS or nested-network constituents, exact cross-member relation occurrences satisfying their predicates, the E.18.NET constraints as applied, and one named network-use frame. A constituent row supplies no generic membership occurrence, and A.22 carries no duplicate network fields. | Recover any missing member, relation predicate, or identity rule, then apply E.18.NET. If a separate membership relation is actually needed, state its participants and apply its predicate rather than inferring it from the constituent list or graph. |
| **CC-A22-2 Non-agentive structure.** | Structure wording does not make the structure, pattern, constraint, graph, or result act, select, optimize, prove, decide, warrant, sense, plan, or adapt. | Name the exact acting system and its work, or apply the pattern whose proof, decision, or work test answers the claim; keep A.22 to selected organization. |
| **CC-A22-3 Structure-claim reliance relation boundary.** | When source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is claimed, name the concrete relation and the A.6.6, source-description, evidence, lens, assurance, causal, gate, decision, or publication definition or test used for it. | Add the exact relation kind, definition or test, validation boundary, admissible use, and non-admissible use, or mark the reliance phrase as carrying no admissible reliance. |
| **CC-A22-4 Description and view separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Treat the visible form as description, view, source-description relation, A.6.6 base declaration, publication form, or publication and name the selected structure separately only if selected organization is being claimed. |
| **CC-A22-5 DescriptionContext reuse.** | Description epistemes and specification-use cases reuse `DescriptionContext` and `U.Episteme`; E.17.0 supplies the sole `U.View` conformance test, while A.6.3 supplies optional viewing construction. No second architecture-local description or view ontology is introduced. | Replace local description or view fields with the imported use qualification, conformance relation, or construction relation defined by the cited neighboring pattern. |
| **CC-A22-6 Structure-use return.** | `StructureUseReturnCondition` is present when hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one structure-use return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Non-structure claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims use the patterns that define or test those claims. | The check passes when that concrete contribution and the claim kind are named, while the A.22 record remains limited to selected-structure use. |
| **CC-A22-8 Architecture pattern application.** | Architecture claims use `C.30` and `ArchitectureOf@Context`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Apply C.30 or a C.30 subpattern and keep A.22 only as the selected-structure EntityOfConcern and structure-claim reliance relation. |
| **CC-A22-9 Plain and Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, the relevant Tech fields and FPF pattern applications are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair leaves a remaining admissible practitioner use: name the structure, name the structure-claim reliance relation record by value, state a structural view, add a `StructureUseReturnCondition`, or apply the definition or test needed by the claim. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-A22-11 CGUS admission.** | A constraint-governed unfolding claim names several loci, cross-locus constraints, preserved and lost structure, admissible next forms, and stop or reconsideration conditions; any stronger neighboring claim names the concrete definition, constraint, test, method, evidence rule, or assurance rule it uses. | Use `A.22.CGUS` only after those values are recoverable; otherwise lower the visible route-shaped artifact to a description, demonstrative slice, README seed, or ordinary cue. |

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, publication-form, description, or view relation; name the structure separately only when selected organization is being claimed. |
| **Reliance-interpretation-as-structure** | A trace used as source basis, benchmark, lens output, model, or simulation is treated as the structure. | Name the exact A.6.6, source-description, evidence, or lens relation and its definition or test; state relation kind, validation boundary, and non-admissible use. |
| **Loss-free extraction** | Extracted or coarsened structure is used without lost structure or structure-use return. | Add `preservedStructure`, `lostStructure`, `validationBoundary`, and `structureUseReturnCondition`. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureOf@Context` and C.30; keep A.22 as the upstream selected-structure EntityOfConcern. |
| **Lens ontology import** | A mathematical lens output becomes the imported ontology. | Use C.29 for the lens, cite it through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the surviving action: structure card, structure-claim reliance relation, Description or view, `StructureUseReturnCondition`, or FPF pattern application. |

### A.22:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| FPF gains a reusable selected-structure EntityOfConcern without minting architecture, module, interface, platform, or graph as root kinds. | A conforming use recovers the exact constituents, selected obtaining relation occurrences, applied constraints, named use frame, preserved and lost structure, and non-admissible use. |
| Structural views become usable without confusing the view, publication form, publication, source-use relation, grounding relation, and selected structure EntityOfConcern. | Existing loose prose that says "the structure is the diagram" needs repair. |
| C.29 mathematical lenses and E.18 transformation-flow structures can supply exact reliance relations for structure claims without becoming structure ontology. | FPF pattern applications are named when evidence, assurance, causal-use, gate, work, or decision claims are being made. |
| Architecture work can start from selected structure through C.30 instead of forcing architecture to be either a document or a module diagram. | Architecture-specific conformance stays outside A.22, so practitioners can require one extra C.30 application when the architecture claim or durable architecture-description use is being made. |

### A.22:10 - Rationale

FPF needs one general selected-structure ontic because many useful claims depend on organization before they depend on a specific architecture, mathematical, measurement, or publication pattern. The selected structure is dependent and non-agentive. Claims about it are carried by separate epistemes and views: it can be described, sourced, compared, coarsened, extracted, or used by architecture, but it does not act, select, carry claim content, or certify.

The selected design keeps A.22 small enough for first use. A practitioner can write one `StructureQuestionCard@Project` and stop. Heavier DescriptionContext, A.6.6 base-dependence, extraction, lens, evidence, and structure-use return records are used only when the next use would otherwise hide loss, source-basis dependence, or non-structure claim kind.

The reason to keep C.30 separate is architectural clarity. Architecture is selected structure for an exact described holon and architecture concern; architecture descriptions are Description epistemes and specification-use cases or views over that claim, while publications only make those epistemes or views available. A.22 supplies the structure substrate, not the architecture ontology.

### A.22:11 - SoTA-Echoing

| Exact practice or source anchor | FPF adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| FPF `C.2.1`, `A.6.3`, and `E.17` description and view discipline | Current FPF separates exact EntityOfConcern, effective reference scheme, viewpoint, grounding holon, view, publication, rendering, and carrier. | A.22 structural descriptions and views reuse those direct relations rather than inventing a local display ontology or mandatory context field. | A description or view does not become the selected structure and supplies no evidence, assurance, gate, or decision authority by form. |
| Evans, [Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/), 2026 | Current DDD practice distinguishes actual bounded model-use loci from the view used to inspect relations among them. | A.22 admits the `BoundedModelUseStructure` membership condition and the conditional `CrossContextRelationStructure` membership condition; the latter has no positive member until independently defined crossing occurrences and all four base discriminators exist. The reusable mapping way of doing remains `U.Method`, actual mapping is dated Work, and the product remains a C.2.1 episteme concerning a proposed organization until an exact structure can be designated; it becomes `U.View` only under exact E.17.0 conformance. | The DDD terms do not turn a system part, method, proposal, structure, view, and diagram into one object. |
| OMG SysML v2 | Deliberately excluded from both the SoTA basis and the adopted lineage for this decision: its long-promoted model-and-diagram program has not provided the current working basis needed for A.22. | No move adopted; use evidence from current structure and modeling practices that solve the problem in operating tools and projects. | Search prominence and the word *system* are not SoTA evidence. SysML v2 is recorded here as a historical dead end, not a comparator. |
| C.29 mathematical-lens discipline | Adopt preserved structure, lost structure, lens-use admissibility, and stop-condition discipline when a mathematical lens is used for a structure claim. | Cite C.29 output through C.29 lens-use result, preserved structure, lost structure, stop condition, and structure-use return discipline. | Lens output is not structure, evidence, assurance, causal-use relation, or decision. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-probing practice | Adapt partial-observability, typed-relation, uncertainty, and structure-use return pressure for extracted structural views. | Use extracted structural-view records with validation boundaries and an observation value selected from `observed`, `inferred`, or `unknown` where needed, plus structure-use return conditions. | Do not mint `U.CodeSpace` and do not treat probe output, probe JSON, or benchmark output as structure adequacy, assurance, release evidence, or assurance evidence. |
| Coarsening, compression, and RG-adjacent traditions | Adopt the need to say what structure is preserved and what is lost. | Use `StructuralCoarseningDescription@Context` and `StructureUseReturnCondition` before relying on a coarsened structure for action. | For RG, epiplexity, structural information, or equivalence reasoning, use C.29, C.16, or the cited pattern that defines or tests the exact claim. |
| GonzoML neural-network architecture discussions as practitioner-language intake | Adapt block replacement, dataflow change, memory placement, cache placement, path-selection, pruning, distillation, and architecture-search wording as general architecture-operation recognition material. | When such wording is used, keep block, cache, expert, router, gate, and similar words as `C.30.STRAT` source labels until changed structure kind, source-description relation, source-use relation, base-dependence relation, evidence relation, lens output, preserved structure, lost structure, and FPF pattern applications are recovered. | Neural-network labels, benchmark results, ablations, or pruning masks do not become structure ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### A.22:12 - Relations

Builds on: `A.1`, `C.13`, `C.2.1`, `A.6.REL`, `A.6.0`, `A.6.5`, `A.3.1`, `A.6.1`, `A.15.1`, `A.6.P`, `A.7`, `A.6.2`, `A.6.3`, `A.14`, `C.16`, `C.29`, `E.10.D2`, `E.10`, `C.2.P`, `E.17.0`, `E.17.1`, `E.24`, `E.24.PUB`, and `F.18`.

Coordinates with: `A.1.1`, `A.2.6`, `A.22.CGUS`, `C.30.P`, `C.30.STRAT`, `C.30`, `C.30.ASV`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `A.6.F`, `E.18`, `E.18.NET`, `E.18.3`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, `C.11`, `C.16`, `C.25`, `G.5`, `C.33`, `C.34`, and `C.35` when architecture-specific structure-capture, preservation, or discovery adequacy claim kinds are being made.

Queue `7b` relation note: `C.33`, `C.34`, and `C.35` define or test architecture-specific capture, preservation, and discovery adequacy over selected structures. A.22 keeps the general selected-structure portion; it does not decide architecture use, candidate admission, measurement, evidence, assurance, or decision authority for those adequacy claims.

Does not replace: `C.30.P` or `C.30.STRAT` wording-use precision restoration, `C.30` for grounded architecture adequacy and conditional architecture-description use, `C.29` for mathematical-lens use, `C.16` for measurement and characterization, `C.28` for causal-use relation, `B.3` for assurance, `A.10` and `G.6` for evidence, `A.20` and `A.21` for gates and release, `A.15` for work, `C.11` for decisions, or `E.17` for publication.

### A.22:End

