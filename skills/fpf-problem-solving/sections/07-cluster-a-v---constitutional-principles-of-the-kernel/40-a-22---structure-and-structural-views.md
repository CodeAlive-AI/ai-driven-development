## A.22 - Structure and Structural Views (STRUCT-CAL)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to select `U.Structure` as the `EntityOfConcern`: the organization, relation class, constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes a next engineering or reasoning action.

The first A.22 question is positive: what is organized, over which bounded context and declared substrate, which relation, constraint, invariant, or variation matters, what is preserved, what is lost or hidden, and which admissible use or stop condition follows.

The first useful move is small:

```text
StructureQuestionCard@Project:
  declared structure substrate:
  bounded context:
  selected structure:
  relation, operation, constraint, invariant, or variation class:
  preserved structure:
  lost, hidden, or excluded structure:
  reliance relation, if being claimed:
  admissible use:
  non-admissible overread:
  governingPatternApplicationRefs, if another claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

Stop at this card when it makes the next structure use clear. Open heavier records only when a named description, view, publication, extraction, coarsening, comparison, mathematical-lens, architecture-description, or other neighboring claim is being made.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source publication, source-use record, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source-basis or lens reliance only when it is being claimed, add a `StructureUseReturnCondition` when loss matters, and apply the FPF pattern that governs any non-structure claim being made.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim being made, use the governing FPF pattern and keep A.22 only to the selected-structure portion.

Thin precision-restoration pointer: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another governed claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

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
- structure and another FPF claim kind governed by its governing pattern;
- structure in general and architecture-specific structure selected by `C.30`.

### A.22:3 - Forces

| Force | Tension |
| --- | --- |
| First-principles structure EntityOfConcern vs ontology inflation | FPF needs a reusable selected-structure EntityOfConcern for relations, constraints, invariants, variation classes, preserved organization, and lost organization, but adding one such EntityOfConcern can accidentally invite many false root kinds. |
| Useful compression vs structure-use return | Structure makes work easier by compressing cases, but a `StructureUseReturnCondition` is needed when compression, extraction, coarsening, source-description reuse, base-dependence reuse, grounding reuse, evidence reuse, lens reuse, simulation reuse, or representation reuse hides a distinction needed for action. |
| Description and view usability vs structure confusion | Descriptions and views make structure inspectable, but a useful view can be mistaken for the structure itself. |
| Mathematical-lens application vs mathematical overread | C.29 lenses can expose structure, but lens output does not become the structure and does not license evidence, causal, assurance, or decision claims by itself. |
| Architecture dependency vs architecture takeover | Architecture uses selected structure through `C.30`; A.22 does not import architecture as its parent or make every structure an architecture. |
| Plain engineering speech vs Tech recovery | Words such as structure, graph, architecture, module, function, interface, pattern, block, layer, level, tier, stack, expert, cache, router, and gate can remain in Plain prose, but FPF-governed use needs recoverable Tech fields and FPF pattern applications. Source-label recovery is governed by `C.30.STRAT` before A.22 accepts a selected-structure portion. |

### A.22:4 - Solution

Select `U.Structure` as the A.22 ontic head: a dependent, non-agentive `EntityOfConcern` used when selected organization changes a next engineering or reasoning action.

> `U.Structure` is the organization of typed relations, constraints, invariants, variation classes, and admissible references to operation or dynamics descriptions over a declared substrate, or declared A.6.6 base declaration when base-dependence is being claimed, inside a bounded context and admissible-use frame.

The A.22 ontic head is intentionally narrow. `U.Structure` is the selected organization under concern: typed relations, constraints, invariants, variation classes, operation or dynamics references, preserved organization, and lost organization over a declared substrate in a bounded context. The grounding object may be a `U.Holon`, `U.System`, `U.Episteme`, declared substrate, or another declared substrate, EntityOfConcern type, relation kind, or record kind named by the direct governing pattern; the selected structure remains the structure of or over that object.

The first useful A.22 use is about the selected structure itself: name the bounded context, selected structure, relation, constraint, invariant, variation class, operation or dynamics reference that matters, preserved or lost organization, and the structure-use return condition or governing-pattern application needed for work. Description records, views, publications, diagrams, publication forms, and renderings are aids that make that selected-structure use inspectable, reusable, comparable, or safe to rely on; they do not share the center of the Solution.

`U.Structure` may fill `EntityOfConcern` for a structure description, view, or structure-claim relation. When a structure description or view is being used, `DescriptionContext.EntityOfConcernRef` names the selected structure, structure claim, or relation governed by the governing pattern for that use; publication forms, publication units, and renderings only make the episteme or view available.

A.22 governs `U.Structure` as a dependent, non-agentive ontic head. It works first over selected-structure EntityOfConcern records and structure-claim reliance relations. Structural descriptions, structural views, extracted structural views, structural-aspect descriptions, structural-coarsening descriptions, and structure-use return conditions are subordinate record forms used only when they preserve the selected-structure use, expose loss, enable comparison, or state a reliance boundary. A.22 does not govern architecture descriptions directly; `C.30` and its subpatterns govern architecture as a use of selected structure over a described holon.

#### A.22:4.1 - Selected Structure Object

```text
U.Structure ::= {
  structureId,
  declaredStructureSubstrateRef:
    U.EntityRef | U.HolonRef | U.EpistemeRef | DeclaredSubstrateRef,
  boundedContextRef,
  relationSignatureRefs?,
  operationOrDynamicsDescriptionRefs?,
  constraintRefs?,
  invariantRefs?,
  symmetryRefs?,
  topologyOrGeometryRefs?,
  stateSpaceRefs?,
  causalOrPredictiveDescriptionRefs?,
  informationRegularityRefs?,
  coarseGrainingRefs?,
  generalStructureAspectKindRefs:
    functional | mereological | modular | transformationFlow |
    control | workMethod | roleEnactor | evidenceAssurance |
    semantic | informational | causalPredictive | dynamical |
    algebraic | topological | geometric | scaleCoarseGrained |
    otherDeclared,
  granularityOrScaleRef?,
  equivalenceOrIsomorphismCriterion?,
  variationClassRefs?,
  preservedUnder?,
  brokenBy?,
  admissibleUse,
  nonAdmissibleUse
}
```

The field list is a recovery aid, not a demand to fill every field. The ordinary record names only the fields that carry the next admissible use. When state, dynamics, causality, measurement, bridge, evidence, assurance, gate, work, decision, or mathematical-lens claims are being made, the record names the governing pattern instead of absorbing that claim kind into A.22.

A.22 `generalStructureAspectKindRefs` are general structure-aspect cues. C.30.ASV `ArchitectureStructureKindRef` values are architecture-local structure-kind classifiers for structures selected by `ArchitectureOf@Context`. A matching label does not imply identity. Use a declared mapping when an A.22 aspect is used as an architecture structure kind.

#### A.22:4.1a - Compact auxiliary boundary

Use description, publication, source-use, evidence, work, gate, decision, release, architecture-description, and mathematical-lens patterns when those claims are being made. The A.22 application contains the selected-structure portion and the structure-use return condition that protects that structure use; neighboring claims remain with their governing patterns. A publication, diagram, graph, table, dashboard, file, model card, generated representation, or lens output may make a structural description or view available; it does not become the selected structure or supply neighboring claim authority by appearance.

#### A.22:4.1b - Constraint-governed unfolding structure

Use `A.22.CGUS` when the current A.22 structure is an organization among several governed loci and constraints: admitted starting records, already-current starting structures, relation signatures, constraints, invariants, guarded transitions, preserved and lost structure, admissible next forms, and conditions for stop, return, split, or currentness refresh. This structure specialization is still `U.Structure`; it is not a route, workflow, method, work plan, performed work, decision, evidence relation, gate, architecture description, or publication.

Open `A.22.CGUS` only when the candidate has several loci and cross-locus constraints. A route card, table, graph, README entry, narrative, slide, or happy-path example may describe or demonstrate the unfolding structure, but it is not the structure itself.

#### A.22:4.2 - Structure claim reliance relation selection


A.22 does not mint a local generic reliance record. When a structure claim relies on something beyond the selected structure itself, choose the reliance relation kind, name the relation record by value, and name the governing pattern:

| Current reliance relation kind | What is named | Governing ontology to apply |
| --- | --- | --- |
| Source-description relation | source episteme, source view, publication form or rendering where relevant, described structure or structure claim, source-basis pins or structure-use return condition, admissible and non-admissible use | `A.7`, `A.6.3`, `E.17`, `E.17.0`, and local source-publication rules |
| Base-dependence or basedness | `dependent = structure claim or structural description`, `base`, declared `baseRelation`, scope, declared `Γ_time` when temporal scope is claimed, witness refs when witness use is claimed, admissible and non-admissible use | `A.6.6` SWBD or Context-local SWBD specialization |
| EntityOfConcern or grounding-holon grounding | selected EntityOfConcern, `GroundingHolonSlot` when grounding-holon grounding is being claimed, bounded context, viewpoint, reference plane, observation or witness condition if observation or witness use is being claimed | `C.2.1`, `A.6.4`, `A.6.3.RT`, `A.6.6` only if it is a base-dependence claim |
| Evidence or witness reliance | evidence-use relation, evidence-provenance relation, claim ref, witness publication or observation record, timespan and freshness; if an evidence graph is current, its graph path remains a mathematical or provenance expression rather than an action route | `A.10`, `A.2.4`, `G.6` |
| Mathematical-lens reliance | lens candidate, lens card, or lens-use record; primary `EntityOfConcern`; relation record or claim record named by value when lens reliance is being claimed; preserved structure; lost structure; stop condition; `MathLensUseOutputRef`; C.29 lens-use result; or `LensUseAdmissibilityValue` | `C.29`, `C.26`, `F.9`, named mathematical-lens pattern |
| Simulation, generated representation, model, or extracted trace | source publication or representation publication, extraction method, validation boundary, preserved structure, lost structure, structure-use return condition | source-description and Description-context patterns plus `C.29`, `A.10`, or governing pattern when a claim of that kind is being made |

If no reliance relation kind can be selected, keep the wording as a source-finding note, recognition cue, ordinary help, quote-only wording, or reduced-use cue. Do not create a generic reliance record to make the claim look governed.

`U.Structure` does not carry description, representation, extraction, mathematical-lens, simulation, or generic reliance state as an internal structure field. Those are source-description, source-use, base-dependence, evidence, lens, extraction, simulation, or publication relations about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, SWBD, or lens output.

#### A.22:4.3 - Structural descriptions and views

Structural descriptions and views reuse existing episteme and view machinery. Architecture does not define a second ontology of descriptions, views, viewpoint bundles, multi-view descriptions, publications, publication forms, or source-pin sets. Every record whose name ends in `Description@Context` here is a specialization of existing `U.Episteme` governed by `C.2.1` and `E.10.D2`. Every record whose name ends in `View@Context` here is a specialization of existing `U.View` or `U.EpistemicViewing` governed by `A.6.3` and `E.17.0`. `DescriptionContext` is imported, not locally redefined.

```text
StructuralDescription@Context ::= {
  descriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | NamedClaimGoverningPatternRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse
}

StructuralView@Context ::= {
  viewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  structureRefs: FinSet(U.StructureRef),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse
}
```

`descriptionContext.ViewpointRef` is the viewpoint field. Do not duplicate it locally under another name unless the governing pattern supplies a more specific view record.

#### A.22:4.4 - Extracted and transformed structural views

Use extracted or transformed structure records when a corpus, trace, model, lens, simulation, generated representation, coarsening pass, observer boundary, or budget boundary produces a view of structure that may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
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
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
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
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
  aspectKindRef,
  structureRefs: FinSet(U.StructureRef),
  structureClaimRelianceRefs?: FinSet(U.ScopedWitnessedBaseDeclarationRef | EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | NamedClaimGoverningPatternRef),
  admissibleUse,
  nonAdmissibleUse
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  descriptionContext: DescriptionContext(EntityOfConcernRef, BoundedContextRef, ViewpointRef),
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

`C.30` uses A.22 by selecting architecture-relevant structures for one described holon through `ArchitectureOf@Context`. `C.30.ASV` then governs architecture structural views over those selected structures. A structure can be used by architecture, but a structure is not an architecture merely because an architecture description refers to it.

Architecture-related records that belong to C.30 or its subpatterns include `ArchitectureOf@Context`, `ArchitectureDescription@Context`, `ArchitectureStructuralView@Context`, `ArchitectureStructureKindRef`, `ArchitectureStructureKindTriage@Project`, `FunctionalStructureView@Context`, `ArchitectureTransformationFlowStructureRelation@Context`, `ControlStructureView@Context`, and `CrossScopeArchitectureResidualTriage@Context`. A.22 may name them as FPF pattern applications. It does not define their architecture-specific conformance.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The reliance relation is treated as the structure. | Name `declaredStructureSubstrateRef` and, when source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is being claimed, name the reliance relation record by value and name the governing FPF pattern; keep structure as selected organization over the declared substrate and do not turn that reliance relation into structure. |
| The diagram, graph, table, dashboard, or publication form is the structure. | Treat it as publication, description, view, publication form, source-description relation, base-dependence relation, grounding relation, evidence relation, lens relation, simulation relation, extraction relation, or representation relation only when its relation is explicit. |
| A transformation-flow graph expression is the structure in every sense. | Use `E.18` for graph, path, crossing, and flow valuation; use A.22 only for the selected structure claim; use `C.30.TFS-REL` when an architecture-to-transformation-flow relation claim is being made. |
| A mathematical lens output is the structure. | Use `C.29` for lens-use result and admissibility, and cite `MathLensUseOutputRef` only through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| A structure proves evidence, assurance, safety, causality, or gate passage. | Assign those claims to `A.10`, `G.6`, `B.3`, `C.28`, `A.20`, or `A.21`. |
| A structure is a decision or work record. | Use `C.11`, `A.20`, `A.21`, `A.15`, or the project-side decision pattern that governs the claim being made. |
| Architecture is a root kind beside structure. | Use `C.30`: architecture is selected structure for a described holon through `ArchitectureOf@Context`. |
| Function, module, interface, platform, layer, stack, block, expert, cache, router, or gate becomes a root kind by appearing in structure prose. | Use `C.30.STRAT` for source-label recovery, then `A.6.F`, `A.6.M` module-relation repair when a module-interface claim is being made, `A.6.0`, `A.6.5`, `A.6.B`, `A.6.C`, `A.6.8`, `E.18`, `C.30.ASV`, and governing patterns as triggered. |

#### A.22:4.8 - Worked slices

**Architecture kernel slice.** A team says, "the architecture is the graph." A.22 does not accept that sentence as a root-kind claim. The repair is:

```text
declaredStructureSubstrateRef: TransformationFlowStructureRef under E.18, with mathematical graph description under E.18.2 when that expression is the current claim
candidate structure: selected transformation-flow structure
structure-claim reliance relation: selected relation record named by value(
  sourceDescriptionOrPatternApplicationRef = SourceViewRef, E.18 selected structure or crossing record, or E.18.2 mathematical graph description,
  governingPatternRef = E.18, A.6.6, A.10, or C.29 when that reliance claim is being made,
  relationKind = source-description | base-dependence | evidence | lens, selected for this reliance,
  validationBoundary = graph-path currentness boundary, slice currentness boundary, or crossing currentness boundary
)
next FPF pattern application: C.30.TFS-REL when this selected structure is used in an architecture-to-transformation-flow relation
non-admissible use: graph as whole architecture, work, evidence, gate, or decision
```

The useful structure use survives: the practitioner can use the graph as a governed reliance relation for selected flow structure without turning it into architecture ontology.

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
| Tell | A practitioner sees an arrangement that matters but does not yet know whether it is a diagram, a model, a graph, an architecture claim, a source description, base-dependence relation, evidence relation, lens relation, or decision. A.22 asks first: what organization is being selected, over what declared substrate and with what reliance relation, under what context, and with what loss? |
| Show: `U.System` | In a plant, vehicle, software system, or neural-network model, the selected structure may be transformation-flow, control, module-interface structure, placement, information, scale, or declared logical structure. The structure record does not become the system and does not prove that the system is safe, maintainable, or ready. |
| Show: `U.Episteme` | A paper, model, generated relation graph, dashboard, architecture note, or mathematical-lens output can describe selected structure or serve as a source-description or A.6.6 base-dependence relation for a selected-structure claim. The episteme, view, or publication is not the structure itself; it carries a description, view, or reliance relation named by value with validation and structure-use return boundaries. |

### A.22:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: universal within FPF structure claims.

| Bias risk | Mitigation |
| --- | --- |
| Architecture bias | Do not make architecture the parent of all structure. A.22 stays upstream; C.30 carries grounded architecture and selected-structure adequacy. |
| Mathematical-formalism bias | A mathematical lens can expose preserved structure and lost structure, but C.29 remains the governing pattern for lens-use result, admissibility, and stop condition. |
| Diagram bias | A useful diagram or generated relation graph is attractive enough to be mistaken for the structure. description, specification-use, and publication boundaries stay explicit. |
| Review-only bias | Checks leave a repair action: name the structure, name the structure-claim reliance relation record by value, state a structural view, add a `StructureUseReturnCondition`, or apply the governing FPF pattern. |
| Didactic-thinning risk | Semantic repair does not leave inert prose. The recognition text keeps the first useful move and the practical payoff visible before the formal records. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, view, relation, or repair guidance above.

### A.22:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Selected structure EntityOfConcern.** | An FPF-governed structure claim names `U.Structure`, an existing FPF kind, or a relation record named by value; it does not mint an architecture-adjacent root kind. | Replace the broad noun with `U.Structure`, an existing FPF kind, or a relation record named by value. |
| **CC-A22-2 Non-agentive structure.** | Structure wording does not make the structure act, optimize, prove, decide, warrant, sense, plan, or adapt. | Apply the governing pattern for the agency, proof, decision, or work claim and keep A.22 to selected organization. |
| **CC-A22-3 Structure-claim reliance relation boundary.** | When source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is claimed, the governing A.6.6 relation ontology, source-description ontology, evidence ontology, lens ontology, assurance ontology, causal ontology, gate ontology, decision ontology, or publication ontology is named. | Add the governing pattern, relation kind where the relation is being claimed, validation boundary, admissible use, and non-admissible use, or mark the reliance phrase as carrying no admissible reliance. |
| **CC-A22-4 Description and view separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Treat the visible form as description, view, source-description relation, A.6.6 base declaration, publication form, or publication and name the selected structure separately only if selected organization is being claimed. |
| **CC-A22-5 DescriptionContext reuse.** | Description epistemes and specification-use cases reuse `DescriptionContext`, `U.Episteme`, `U.View`, `A.6.3`, and `E.17` machinery; no second architecture-local description and view ontology is introduced. | Replace local description and view fields with the imported DescriptionContext fields or assign the claim to the existing governing pattern. |
| **CC-A22-6 Structure-use return.** | `StructureUseReturnCondition` is present when hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one structure-use return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Non-structure claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims are assigned to their governing patterns. | The check passes when the governing FPF pattern and the claim kind being made are named, while the A.22 record remains limited to selected-structure use. |
| **CC-A22-8 Architecture pattern application.** | Architecture claims use `C.30` and `ArchitectureOf@Context`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Apply C.30 or a C.30 subpattern and keep A.22 only as the selected-structure EntityOfConcern and structure-claim reliance relation. |
| **CC-A22-9 Plain and Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, the relevant Tech fields and FPF pattern applications are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair leaves a remaining admissible practitioner use: name the structure, name the structure-claim reliance relation record by value, state a structural view, add a `StructureUseReturnCondition`, or apply the FPF pattern that governs the claim kind being made. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-A22-11 CGUS admission.** | A constraint-governed unfolding claim names several loci, cross-locus constraints, preserved and lost structure, direct governing-pattern exits, admissible next forms, and stop or return conditions. | Use `A.22.CGUS` only after those fields are recoverable; otherwise lower the visible route-shaped artifact to a description, demonstrative slice, README seed, or ordinary cue. |

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, publication-form, description, or view relation; name the structure separately only when selected organization is being claimed. |
| **Reliance-interpretation-as-structure** | A trace used as source basis, benchmark, lens output, model, or simulation is treated as the structure. | Name the governing A.6.6 relation ontology, source-description ontology, evidence ontology, or lens ontology; state relation kind where the relation is being claimed, validation boundary, and non-admissible use. |
| **Loss-free extraction** | Extracted or coarsened structure is used without lost structure or structure-use return. | Add `preservedStructure`, `lostStructure`, `validationBoundary`, and `structureUseReturnCondition`. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureOf@Context` and C.30; keep A.22 as the upstream selected-structure EntityOfConcern. |
| **Lens ontology import** | A mathematical lens output becomes the imported ontology. | Use C.29 for the lens, cite it through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the surviving action: structure card, structure-claim reliance relation, Description or view, `StructureUseReturnCondition`, or FPF pattern application. |

### A.22:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| FPF gains a reusable selected-structure EntityOfConcern without minting architecture, module, interface, platform, or graph as root kinds. | A conforming use states context, declared substrate or named reliance relation record, preserved and lost structure, and non-admissible use when the claim has FPF-governed use. |
| Structural views become usable without confusing the view, publication form, publication, source-use relation, grounding relation, and selected structure EntityOfConcern. | Existing loose prose that says "the structure is the diagram" needs repair. |
| C.29 mathematical lenses and E.18 transformation-flow structures can supply governed reliance relations for structure claims without becoming structure ontology. | FPF pattern applications are named when evidence, assurance, causal-use, gate, work, or decision claims are being made. |
| Architecture work can start from selected structure through C.30 instead of forcing architecture to be either a document or a module diagram. | Architecture-specific conformance stays outside A.22, so practitioners can require one extra C.30 application when the architecture claim or durable architecture-description use is being made. |

### A.22:10 - Rationale

FPF needs one general selected-structure EntityOfConcern because many useful project claims depend on organization before they depend on a specific architecture, mathematical, measurement, or publication pattern. The selected-structure entity has to be dependent, non-agentive, and claim-bearing through descriptions or views: it can be described, sourced, compared, coarsened, extracted, or used by architecture, but it does not act or certify.

The selected design keeps A.22 small enough for first use. A practitioner can write one `StructureQuestionCard@Project` and stop. Heavier DescriptionContext, A.6.6 base-dependence, extraction, lens, evidence, and structure-use return records are used only when the next use would otherwise hide loss, source-basis dependence, or non-structure claim kind.

The reason to keep C.30 separate is architectural clarity. Architecture is selected structure for a described holon under context and concern; architecture descriptions are Description epistemes and specification-use cases or views over that claim, while publications only make those epistemes or views available. A.22 supplies the structure substrate, not the architecture ontology.

### A.22:11 - SoTA-Echoing

| Exact practice or source anchor | FPF adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description practice | Adopt the separation of described entity of interest, concern, viewpoint, view, and correspondence as pressure for DescriptionContext separation, mapped here to `EntityOfConcern` and `DescriptionContext` terms. | A.22 structural descriptions and views reuse `DescriptionContext`, viewpoint, view, and correspondence machinery rather than inventing a local display ontology. | ISO 42010 does not make every structure an architecture and does not add evidence, assurance, gate, or decision authority. |
| OMG SysML v2 view practice | Adapt views-as-queries and model-view discipline as a source for treating views as selected renderings over model content. | A structural view states selected, hidden, or lost structure when the selection changes action. | A view is not the structure and not a proof of the described holon. |
| C.29 mathematical-lens discipline | Adopt preserved structure, lost structure, lens-use admissibility, and stop-condition discipline when a mathematical lens is used for a structure claim. | Cite C.29 output through C.29 lens-use result, preserved structure, lost structure, stop condition, and structure-use return discipline. | Lens output is not structure, evidence, assurance, causal-use relation, or decision. |
| arXiv:2603.00601 code-space architecture relation-graph work and related code-probing practice | Adapt partial-observability, typed-relation, uncertainty, and structure-use return pressure for extracted structural views. | Use extracted structural-view records with validation boundaries and an observation value selected from `observed`, `inferred`, or `unknown` where needed, plus structure-use return conditions. | Do not mint `U.CodeSpace` and do not treat probe output, probe JSON, or benchmark output as structure adequacy, assurance, release evidence, or assurance evidence. |
| Coarsening, compression, and RG-adjacent traditions | Adopt the need to say what structure is preserved and what is lost. | Use `StructuralCoarseningDescription@Context` and `StructureUseReturnCondition` before relying on a coarsened structure for action. | RG, epiplexity, structural information, and equivalence reasoning are governed by C.29, C.16, or another governing pattern named for the claim being made. |
| GonzoML neural-network architecture discussions as practitioner-language intake | Adapt block replacement, dataflow change, memory placement, cache placement, path-selection, pruning, distillation, and architecture-search wording as general architecture-operation recognition material. | When such wording is used, keep block, cache, expert, router, gate, and similar words as `C.30.STRAT` source labels until changed structure kind, source-description relation, source-use relation, base-dependence relation, evidence relation, lens output, preserved structure, lost structure, and FPF pattern applications are recovered. | Neural-network labels, benchmark results, ablations, or pruning masks do not become structure ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

### A.22:12 - Relations

Builds on: `C.2.1`, `A.6.P`, `A.7`, `A.6.2`, `A.6.3`, `A.14`, `C.16`, `C.29`, `E.10.D2`, `E.10`, `C.2.P`, `E.17.0`, `E.17.1`, `E.24`, `E.24.PUB`, and `F.18`.

Coordinates with: `A.22.CGUS`, `C.30.P`, `C.30.STRAT`, `C.30`, `C.30.ASV`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `A.6.F`, `E.18`, `E.18.3`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, `C.11`, `C.16`, `C.25`, `G.5`, `C.33`, `C.34`, and `C.35` when architecture-specific structure-capture, preservation, or discovery adequacy claim kinds are being made.

Queue `7b` relation note: `C.33`, `C.34`, and `C.35` govern architecture-specific capture, preservation, and discovery adequacy over selected structures. A.22 keeps the general selected-structure portion; it does not decide architecture use, candidate admission, measurement, evidence, assurance, or decision authority for those adequacy claims.

Does not replace: `C.30.P` or `C.30.STRAT` wording-use precision restoration, `C.30` for grounded architecture adequacy and conditional architecture-description use, `C.29` for mathematical-lens use, `C.16` for measurement and characterization, `C.28` for causal-use relation, `B.3` for assurance, `A.10` and `G.6` for evidence, `A.20` and `A.21` for gates and release, `A.15` for work, `C.11` for decisions, or `E.17` for publication.

### A.22:End

