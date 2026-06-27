## C.30.AD - Architecture Description Adequacy

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Architecture-description adequacy.

**Intent.**
Keep an architecture description useful without letting the description, view, diagram, publication, or tool publication face become the architecture itself.

**Builds on.** `C.30`, `C.30.ASV`, `A.1`, `A.22`, `E.24.PUB`, `A.7`, `A.6.3`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, `C.2.P`, `E.10`, and `E.10.ARCH`.

**Coordinates with.** `C.30.AD.BA`, `C.30.P`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.PAD`, `C.32.ADR`, `C.32.ADA`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `A.6.F`, `A.6.M`, `C.29`, `C.16`, `C.16.P`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `A.15.5`, `C.11`, `C.28`, `E.8`, `E.10.MOVE`, `E.11.PUR`, `E.24.CD`, and `F.18`.

### C.30.AD:0 - Use this when

Use this pattern when an architecture description is the current EntityOfConcern: a durable description, multi-view description set, architecture documentation set, model set, generated architecture relation graph, view set, or specification-use record over one `ArchitectureOf@Context`.

Use `C.30.AD` when the practitioner needs to know:

- which `ArchitectureOf@Context` claim the description is about;
- which selected structures or architecture structure kinds are described;
- which views are used under which viewpoints;
- which correspondences, source returns, freshness boundaries, or specification-use boundaries make the description usable;
- what the description can guide and which uses are non-admissible.

**What goes wrong if missed.** A diagram, documentation set, generated relation graph, model card, ADR publication set, or architecture model starts acting as architecture, proof, gate, assurance, decision, work authorization, or release authorization by presentation alone.

**What this buys.** The practitioner can keep one architecture description inspectable across views, viewpoints, selected structures, correspondences, publications, source returns, and direct governing-pattern applications.

**First useful description-use output.** Write one `ArchitectureDescriptionUseCard@Project`:

```text
ArchitectureDescriptionUseCard@Project:
  architectureClaimRef:
  describedHolonRef:
  boundedContextRef:
  descriptionPurpose:
  selectedStructureRefs:
  structureKindRefs:
  viewpointRefs:
  architectureStructuralViewRefs:
  correspondenceRefs:
  sourceReturnCondition?:
  specificationUseBoundary?:
  admissibleUse:
  nonAdmissibleUse:
  firstGoverningPatternApplication?:
```

`@Project` guard: in this card name, `@Project` marks a project-side use card for first-pass triage or specification-use control. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

The use card is a controlled first-pass slice. It can close ordinary use only when it names one architecture claim, one usable description purpose, the selected structures or structure kinds being described, viewpoint refs being used, admissible use, non-admissible use, and one remaining architecture candidate use or direct governing-pattern application. Expand to the fuller `ArchitectureDescription@Context` record when cross-view correspondence, reuse, source return, freshness, specification use, regulated use, comparison, or project-side authority use is being made.

**Not this pattern when.**

- If the current use is a grounded architecture claim or one first architecture question, use `C.30`.
- If the current use is a selected structure or structural description outside architecture, use `A.22`.
- If the current use is one architecture structural view, use `C.30.ASV`.
- If the current use is built-asset architecture-description, BIM, IFC, asset-information, digital-twin, or reference-designation specialization, use `C.30.AD.BA`.
- If architecture or structure wording is still ambiguous, use `C.30.P`.
- If the current use is only a publication face, publication form, report, dashboard, file, or source-current relation, use `C.2.P`, `E.17`, or the publication or source pattern governing the claim.
- If the description is being used as pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, decision, work authorization, causal-use claim, release authorization, deontic permission, or mathematical-lens use, keep `C.30.AD` only for the description boundary and apply the direct pattern governing that claim to the claim being made.

### C.30.AD:1 - Problem frame

Architecture practice needs durable descriptions: multi-view documents, view models, generated relation graphs, architecture transformation-flow views, LCA control sketches, module or interface diagrams, deployment views, model cards, system cards, and architecture decision description sets. These descriptions are useful because they let teams compare, reuse, refresh, inspect, and use architecture claims across viewpoint families and working concerns; A.15 allocation-responsibility semantics apply only when a project role relation itself is being governed.

The difficulty is that the description is not the architecture. The same architecture can have several descriptions. The same description set can contain several views. Each view is written from one viewpoint or concern-framed practice and can hide, lose, coarsen, or emphasize different structure. A view can describe functional structure, flow or transformation-flow structure, control structure, module or interface structure, placement structure, information custody, evidence-reuse relation, assurance relation, scale or coarsening relation, or another declared architecture-relevant structure.

The first-minute practitioner can ask:

- What `ArchitectureOf@Context` is this description about?
- Which selected structures or structure kinds does this view describe?
- Which viewpoint makes this view useful?
- What correspondence connects this view to the architecture claim and other views?
- When does source return to a source episteme, source view, or direct governing pattern for that claim become necessary?
- What admissible architecture move remains after the description has been used?

### C.30.AD:2 - Problem

How can FPF govern architecture descriptions without:

- treating a description, model, view, diagram, graph, card, table, dashboard, file, publication, publication form, or rendering as the architecture itself;
- treating all architecture documentation as one generic description with no selected-structure recovery;
- losing the link between a viewpoint and the architecture structure kind being described;
- letting one attractive view hide lost structure, stale source, or missing correspondence;
- letting publication quality become evidence sufficiency, assurance, gate passage, decision claim, work completion, or release authorization;
- making ordinary architecture triage too heavy for a first useful architecture move.

### C.30.AD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful description vs architecture overread | A good description guides architecture work, but it is not the architecture, selected structure, decision claim, proof, or release authorization. |
| Multi-view richness vs selected-structure recovery | Several views can be needed, but each view names the architecture claim, viewpoint, selected structure or structure kind, and admissible use before it is relied on. |
| Viewpoint utility vs viewpoint-as-kind collapse | Viewpoints help a role or practice inspect an architecture; they do not choose the structure kind unless `C.30.ASV` or another governing structural-view pattern names the structure-kind relation by value. |
| Reuse vs freshness | A reused architecture description needs source edition, structure edition, or source-return boundaries when its admissible use depends on currentness. |
| Specification-use vs publication form | A description can be used as a specification, but specification use is a use boundary over a Description episteme or its publication form, not the architecture itself. |
| Thin C.30 bridge vs full description mechanism | C.30 keeps the architecture move central; this pattern carries the heavier architecture-description mechanism when durable description use is being made. |

### C.30.AD:4 - Solution

Use `ArchitectureDescription@Context` when the current EntityOfConcern is the description episteme or specification-use record over one `ArchitectureOf@Context`. The described holon is recovered through `ArchitectureOf@Context.describedHolonRef`; the `DescriptionContext.EntityOfConcernRef` for the architecture description points to the architecture claim record.

`C.30.AD` does not mint `U.Architecture`, does not redefine `U.Viewpoint`, and does not replace generic Description, view, publication, or publication-form machinery. It specializes those records for architecture descriptions whose views remain tied to selected architecture-relevant structures.

Built-asset architecture-description, BIM, IFC, asset-information, digital-twin, and ISO/IEC 81346 reference-designation detail is governed by `C.30.AD.BA`. C.30.AD keeps the general architecture-description bridge and does not absorb that built-asset specialization.

#### C.30.AD:4.1 - Architecture-description record

```text
ArchitectureDescription@Context ::= {
  architectureDescriptionId: ArchitectureDescriptionId,
  architectureClaimRef: ArchitectureOf@ContextRef,
  descriptionContext: DescriptionContext(
    EntityOfConcernRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = primaryViewpointRef?
  ),
  describedHolonRef: U.HolonRef,
  selectedStructureRefs: FinSet(U.StructureRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),
  architectureStructuralViewRefs: FinSet(ArchitectureStructuralViewRef),
  correspondenceRefs: FinSet(CorrespondenceRef),
  sourceEpistemeRefs?: FinSet(U.EpistemeRef),
  sourceViewRefs?: FinSet(U.ViewRef),
  sourceReturnCondition?,
  freshnessCueRefs?: FinSet(ArchitectureDescriptionFreshnessCueRef),
  specificationUseBoundary?,
  publicationUseBoundary?,
  admissibleUse,
  nonAdmissibleUse
}
```

`describedHolonRef` is a recoverable field copied from the referenced `ArchitectureOf@Context`; it is not the architecture description's `DescriptionContext.EntityOfConcernRef`.

Minimum conformance for the record:

- `architectureClaimRef` names one `ArchitectureOf@Context`;
- `selectedStructureRefs` or `structureKindRefs` name the architecture-relevant structures being described;
- every architecture structural view names its viewpoint and selected structure or structure kind;
- `correspondenceRefs` or a source-return condition is present when cross-view or source reuse is being made;
- `admissibleUse` and `nonAdmissibleUse` say what the description can and cannot carry.

#### C.30.AD:4.1a - Traceable architecture multi-view description chain

A full architecture description is traceable only when the reader can recover the chain that makes a view useful without turning the view into the architecture. The chain is a trace requirement, not a prescribed method or work plan:

```text
workingConcernRef
  or A15AllocationResponsibilityFamilyRef when A.15 allocation-responsibility semantics apply
-> viewpointRef
-> selectedStructureRef or structureKindRef
-> ArchitectureOf@ContextRef
-> ArchitectureStructuralView@ContextRef governed by C.30.ASV
-> ArchitectureDescription@ContextRef governed by C.30.AD
-> sourceEpistemeRef or sourceViewRef when source use is being made
-> PublicationUnitRef, publication face, or publication form only when published
-> correspondenceRef or sourceReturnCondition when cross-view or source reuse is being made
-> admissibleArchitectureMove or governing-pattern application
```

`E.17.0` carries the generic multi-view Description machinery. `C.30.ASV` carries the selected-structure-kind-to-view relation and view adequacy. `C.30.AD` carries the architecture-specific composition and use boundary: which architecture claim the description is about, which structural views it uses, what correspondence or source return keeps the use honest, and which architecture move or governing pattern remains admissible.

If any link in the chain is absent, do not fill it with a documentation label. Either add the missing reference, reduce the admissible use, or apply the governing pattern that can recover the missing relation.

#### C.30.AD:4.2 - View membership, viewpoint, and structure-kind binding

Architecture descriptions can contain several `ArchitectureStructuralView@Context` records. Each such view remains governed by `C.30.ASV`; C.30.AD does not mint a second structural-view record and does not decide whether the view has the right structure kind, viewpoint, hidden or lost structure note, correspondence, or source return.

C.30.AD records only membership or use of an already recoverable architecture structural view inside one architecture description:

```text
ArchitectureDescriptionViewMembership@Context ::= {
  architectureDescriptionRef: ArchitectureDescriptionRef,
  architectureStructuralViewRef: ArchitectureStructuralViewRef,
  architectureClaimRef: ArchitectureOf@ContextRef,
  membershipPurpose:
    orientation | comparison | implementationGuidance |
    assuranceInput | sourceReturn | declaredOther,
  correspondenceRefs?: FinSet(CorrespondenceRef),
  sourceReturnCondition?,
  admissibleUse:
  nonAdmissibleUse:
}
```

Use `C.30.ASV` when the current question is whether the view has the right structure kind, viewpoint, hidden or lost structure note, correspondence, or source return. Use `A.22` when the current question is structure as such. Use `C.30` when the current question is the grounded architecture claim. Use `C.30.AD` only for the description's membership, composition, correspondence, source-return, freshness, specification-use, publication-use, or remaining architecture candidate-use boundary.

Common architecture-description views:

| View use | Required FPF application |
| --- | --- |
| Function or functionality view | `A.6.F` for function or functionality wording and `C.30.ASV` for the structural view. |
| Transformation-flow view | `E.18` plus `C.30.TFS-REL` when the selected transformation-flow structure, path, crossing, valuation, or graph-shaped mathematical description is used by architecture. |
| Control or LCA view | `C.30.LCA` when a control structure view is being used. |
| Module or interface view | `A.6.M`, signature or interface patterns, and `C.30.ASV` when module-interface structure is being used. |
| Mathematical-lens view | `C.29` for lens-use result and preserved and lost structure; `C.30.AD` only for the architecture-description use of the lens result. |
| Boundary, interface, or Markov-blanket view | `A.1`, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `C.26`, `C.26.3`, and `C.29` according to the recovered claim; `A.6.B` only when the recovered object is L, A, D, or E statement classification inside a boundary package; `C.30.AD` records only the architecture-description membership, use boundary, correspondence, source return, freshness, or publication use. |
| Evidence or assurance reuse view | `A.10`, `B.3`, or assurance or evidence pattern governing the claim for the non-architecture claim. |
| Architecture residual view | `C.30.ILC` when the view is about a cross-scope or interlevel architecture residual. If the view uses conflict wording or frustration wording, C.30.AD records only membership, correspondence, and source return; C.30.ILC governs the residual. |
| Multilevel-learning or frustration mathematical-lens view | `C.29` when the view contains a recoverable level mapping or scale mapping and preserved structure and lost structure; `C.30.AD` records only the architecture-description use of that lens result. |
| Residual-reducing candidate or optimization view | `C.32.MLAO` for the residual-reducing multilevel candidate frame; `C.32` for the candidate architecture palette; `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use; `C.18` and `C.19` for archive, front, or current-pool treatment; `G.5` only for selected-set publication; `C.11` only for final local choice. C.30.AD records only description membership, correspondence, source return, freshness, publication use, or specification use. |

#### C.30.AD:4.3 - Correspondence and source return

Architecture descriptions become risky when a reader cannot tell whether two views describe the same architecture claim, the same selected structure, related structures, or different entities of concern. Use correspondence records or source-return conditions when the description is reused across viewpoints, source editions, tool outputs, generated views, or regulated use.

```text
ArchitectureDescriptionCorrespondence@Context ::= {
  architectureDescriptionRef:
  architectureClaimRef:
  fromViewRef:
  toViewRef:
  correspondenceKind:
    sameArchitectureClaim | sameSelectedStructure |
    refinement | abstraction | projection |
    sourceDerived | conflict | declaredOther,
  preservedStructureRefs?:
  lostStructureRefs?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse:
}
```

Correspondence is not proof, assurance, or gate passage. It is a relation that lets a reader use more than one architecture view without silently changing the EntityOfConcern.

#### C.30.AD:4.4 - Freshness and currentness boundary

Use a freshness cue only when the architecture description's admissible use depends on source edition, structure edition, model version, deployment context, or external condition.

```text
ArchitectureDescriptionFreshnessCue:
  sourceEditionRefs:
  structureEditionRefs?:
  modelOrToolEditionRefs?:
  knownRefreshTrigger:
    sourceChange | deploymentChange | interfaceChange |
    controlRateChange | modelEditionChange | evidenceDecay |
    toolApiChange | regulatoryChange |
    incidentFinding | declaredOther | unknown,
  admissibleUseUntil?:
  sourceReturnCondition:
```

Freshness does not make the description evidence-sufficient. It only bounds the use of the description.

#### C.30.AD:4.5 - Specification-use and publication boundary

An architecture description can be used as a specification only when that use is declared. Specification use is not a new architecture kind; it is a use boundary over a Description episteme or its publication.

```text
ArchitectureDescriptionSpecificationUse@Project ::= {
  architectureDescriptionRef:
  sourceEpistemeRef | sourceViewRef,
  publicationUnitRef?:
  governedUse:
    coordination | implementationGuidance | procurement |
    verificationPlanning | assuranceInput | releaseInput |
    declaredOther,
  selectedNeighborPatternRef?:
  admissibleUse:
  nonAdmissibleUse:
}
```

If the specification use becomes pattern-use recommendation, work-entry readiness, evidence, assurance, gate passage, performed work, work authorization, decision claim, causal-use claim, or release authorization, apply the direct pattern governing that claim to the claim being made. The architecture description remains the description boundary, not the governing claim.

Publication forms, diagrams, model faces, files, cards, dashboards, and generated relation graphs remain publications, views, faces, source-current records, or renderings unless the source episteme and use boundary are explicit.

#### C.30.AD:4.6 - Direct governing-pattern applications

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
| Residual-reducing candidate architecture moves, candidate palette, candidate front, shortlist, selected set, or optimization over candidates | `C.32.MLAO` for the residual-reducing frame, `C.32` for the candidate palette, `A.19.CPM` or `A.19.SelectorMechanism` for comparison or selector-policy use, `C.18` and `C.19` for archive, front, or pool treatment, `G.5` for selected-set publication, `C.11` for final local choice, and measurement patterns named by value when those claims are being made |
| Generic description, view, viewpoint, publication, publication form, MVPK face | `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, `E.17`, or `C.2.P` |
| Function or functionality wording | `A.6.F` |
| Module, interface, port, signature, or reusable structure relation | `A.6.M`, a signature or interface pattern named by value, `C.31`, or `C.31.RSA` |
| Mathematical lens or preserved and lost mathematical structure | `C.29` |
| Characteristic, scale, coordinate, score, or quality claim | `C.16.P`, `C.16`, `A.19`, `C.25`, or quality pattern governing the claim |
| Evidence, assurance, gate, work planning, performed work, local choice, project architecture decision, causal-use, release | `A.10`, `B.3`, `A.20`, `A.21`, `A.15.2`, `A.15.1`, `C.11`, `C.32.PAD`, `C.28`, release or admissibility pattern, or governing pattern |

#### C.30.AD:4.6a - Candidate, front, and selected-set description boundary
Architecture-description material can also describe a project architecture decision or the source structure used by an ADR-like projection. Use `C.32.PAD` when the claim is the project architecture decision relation. Use `C.32.ADR` when the claim is publication projection of an architecture-decision description. Use `C.32.ADA` when the claim is adequacy of that decision for a declared use. C.30.AD keeps only architecture-description membership, correspondence, source return, freshness, publication use, and specification use.

An architecture description may describe an archive, front, selected set, candidate palette, local choice, or planned architecture move. That does not make the description the archive-governing pattern, selector, choice rule, pattern-use recommendation, work-entry readiness relation, work authorization, or deontic permission. Use `C.32.MLAO` for residual-reducing multilevel candidate frames, `C.32` for candidate architecture palettes, `C.18` for archive and front relations, `C.19` for current-pool treatment, `G.5` only for selected-set publication, `C.11` for local choice, `C.30` for the architecture move, `C.30.ASV` for selected-structure view triage, `E.11.PUR` for recommended pattern use, `A.15.5` for work-entry readiness, and the A.15 family for planning or performed work.

For an architecture-description claim, record only description membership, view membership, viewpoint, correspondence, source return, freshness, publication use, and specification use. If the source claim only grounds a first architecture move, return to `C.30`. If it synthesizes alternatives, use `C.32` or `C.32.MLAO` according to the residual frame. If it changes which variants are archived, kept in a pool, compared, selected, published, locally chosen, or decided, return to the pattern that owns that relation.

### C.30.AD:5 - Archetypal Grounding (Worked Cases)



| Case | C.30.AD treatment |
| --- | --- |
| "The architecture is documented in this view set." | The view set is an architecture description or publication set only if it names one `ArchitectureOf@Context`, selected structures, viewpoints, view refs, and admissible use. It is not the architecture itself. |
| A transformation-flow graph expression is included in an architecture document. | Use `E.18` for graph, path, and crossing semantics and `C.30.TFS-REL` when the graph is used by architecture. `C.30.AD` records only the architecture-description use and source-return boundary. |
| A model card claims deployment safety. | Use `C.30.AD` only if the card describes an architecture claim or structure view. Safety assurance uses `B.3`; evidence uses `A.10`; release uses `A.21`. |
| A generated code-agent relation graph shows modules and calls. | Treat the graph as a generated view or source publication. Recover observed, inferred, and unknown relations; use `C.30.ASV` or `C.30.TFS-REL` only when an architecture structural view or flow relation is being used. |
| A multi-view description set has functional, deployment, control, and evidence-reuse views. | Each view has an `ArchitectureDescriptionViewMembership@Context` line and a referenced `C.30.ASV` view record. Evidence-reuse claims do not stay inside C.30.AD. |
| A plant safety architecture description combines control, deployment, evidence, and operator-view material. | `C.30.AD` records the architecture-description chain and correspondence among views. `C.30.LCA` governs the control view; `A.10`, `G.6`, or `B.3` governs evidence or assurance; `A.15` is used only if allocation-responsibility semantics apply. |
| A product-line platform document reuses module-interface, variability, and deployment views across products. | `C.30.AD` records which architecture claim and structural views the document uses, plus source-return conditions for product variation. `A.6.M` normalizes module-interface relations; `C.31.RSA` accounts reusable structure or bespoke residue only after structure refs and accounting frame are declared. |
| A multi-view architecture description says local optimization at one declared holon level creates frustration in another. | `C.30.AD` records the description membership, correspondence, and source-return boundary. `C.30.ILC` governs the residual; `C.29` is used only if the description contains a recoverable level mapping or scale mapping with preserved structure and lost structure. |
| An architecture document compares residual-reducing candidate decompositions or optimization moves. | `C.30.AD` records only the description or publication use of that comparison. Residual-reducing frames use `C.32.MLAO`; candidate palettes use `C.32`; comparison and selector-policy use `A.19.CPM` or `A.19.SelectorMechanism`; archives and fronts use `C.18` or `C.19`; selected-set publication uses `G.5`; final local choice uses `C.11`; measurement claims use their governing patterns. |
| A review note, dashboard, or generated report describes gaps in an architecture description rather than the architecture itself. | The architecture description can be the EntityOfConcern for that second-description use; the second description is handled as a Description, view, source relation, publication face, review record, or evaluation record over that EoC. `C.30.AD` keeps the chain to the underlying `ArchitectureOf@Context` visible without treating the second description as the architecture, the residual, the decision, or the proof. |

### C.30.AD:5.1 - Bias-Annotation

| Bias | How C.30.AD prevents it |
| --- | --- |
| Description-as-architecture bias | `ArchitectureDescription@Context` points to one `ArchitectureOf@Context`; the description does not become the architecture, selected structure, or described holon. |
| View-as-structure bias | Every architecture structural view remains bound to `C.30.ASV` or another structure-governing pattern; C.30.AD records membership, correspondence, source return, and use boundary. |
| Publication-as-authority bias | Publication form, dashboard polish, model-card form, or report label does not establish evidence, assurance, gate, decision, work-authorization, or release-authorization claims. |
| Freshness-as-evidence bias | A freshness cue bounds admissible use; it does not make the description evidence-sufficient. |
| Semio-bias in architecture work | C.30 remains centered on architecture as EntityOfConcern; C.30.AD opens only when the architecture description itself is the current EntityOfConcern. |

### C.30.AD:6 - Conformance checklist

| Check | Requirement | Repair if failed |
| --- | --- | --- |
| **CC-C30AD-1 EntityOfConcern.** | The architecture description's `DescriptionContext.EntityOfConcernRef` points to one `ArchitectureOf@Context` claim record. | Add `architectureClaimRef` or use `C.30` until the architecture claim is recoverable. |
| **CC-C30AD-2 Described holon recovery.** | The described holon is recovered through `ArchitectureOf@Context.describedHolonRef`, not by replacing the description EntityOfConcern with the holon. | Restore the strict description boundary and copy only the recoverable holon ref. |
| **CC-C30AD-2a Traceable multi-view chain.** | The description use recovers the chain from working concern or A.15 allocation-responsibility family being used through viewpoint, selected structure or structure kind, architecture claim, ASV view, architecture description, source or publication use when source or publication use is being made, correspondence when used or source return when needed, and remaining admissible architecture move. | Add the missing reference, reduce the admissible use, or apply the governing pattern that can recover the missing relation. |
| **CC-C30AD-3 Viewpoint and structure kind.** | Every architecture structural view names viewpoint and selected structure or structure kind. | Use `C.30.ASV` before relying on the view. |
| **CC-C30AD-4 Correspondence and source return.** | Cross-view, generated-view, source-derived, reused, regulated, or comparison use names correspondence or source-return condition. | Add correspondence and source-return fields or reduce the admissible use. |
| **CC-C30AD-5 Publication boundary.** | Publication face, publication form, diagram, dashboard, card, file, or rendering is not treated as architecture, decision claim, evidence, assurance, gate passage, performed work, work authorization, or release authorization. | Assign publication or source use to `C.2.P` or `E.17` and the non-architecture claim to the direct pattern governing that claim. |
| **CC-C30AD-6 Specification-use boundary.** | Specification use is declared as use over a Description episteme or publication, with direct governing-pattern applications when it carries a non-description claim. | Add `ArchitectureDescriptionSpecificationUse@Project` or demote to ordinary description. |
| **CC-C30AD-7 Remaining architecture candidate use.** | The bounded description still tells the practitioner what architecture move, view normalization, source return, or governing-pattern application remains. | Add the remaining architecture candidate use or reduce the text to source or publication use. |

### C.30.AD:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description-as-architecture | A document, diagram, model, graph, view set, or card is said to be the architecture. | Recover `ArchitectureOf@Context` and keep the source material as description, view, publication form, or source relation. |
| Viewpoint-as-structure-kind | A stakeholder, role, concern, or viewpoint label is used as if it named the selected structure. | Use `C.30.ASV` to recover structure kind and viewpoint separately. |
| Multi-view fog | Many views are listed, but no one can tell which selected structures they describe or how they correspond. | Add architecture claim ref, selected structure refs, viewpoint refs, correspondence refs, and source-return conditions. |
| Specification-as-authority | A specification-looking architecture description is used as performed work, gate passage, decision claim, assurance, evidence, work authorization, or release authorization. | Declare specification use and apply the direct pattern governing that claim to the claim being made. |
| Freshness laundering | A recently generated diagram is treated as adequate because it is current. | Record source edition and refresh trigger; do not treat currentness as adequacy, evidence, or assurance. |
| Architecture-documentation takeover | The pattern spends most of its practitioner guidance on diagrams, publications, and wording guards instead of architecture claim, selected structures, and views. | Keep C.30 centered on architecture and use C.30.AD only when the description itself is the EntityOfConcern. |

### C.30.AD:8 - Consequences

Positive consequences:

- Architecture descriptions become reusable without pretending to be the architecture itself.
- Multi-view work can keep viewpoints, views, selected structures, correspondences, source return, freshness, and specification use inspectable.
- Description, publication, evidence, assurance, gate, decision, work, release, and mathematical-lens claims stay with separate governing patterns.
- C.30 can stay focused on architecture while C.30.AD carries the heavier description machinery.

Costs:

- A useful architecture document needs explicit links to `ArchitectureOf@Context`, selected structures, viewpoints, and admissible use.
- Reused or regulated descriptions may need correspondence, source-return, and freshness fields before they can be relied on.
- Familiar document forms lose implicit authority; evidence, assurance, gate, decision, and release claims must be established by their own patterns.

### C.30.AD:9 - Rationale

Architecture work needs descriptions, but architecture-description adequacy is not architecture adequacy. A description can guide architecture work only when its relation to the described architecture claim, selected structures, viewpoints, views, source material, publication form, and admissible use is recoverable.

The pattern therefore specializes generic Description and publication machinery for architecture use. It does not mint a new architecture kind, does not replace `C.30`, and does not let diagrams or documentation formats establish non-description claims by presentation alone.

### C.30.AD:10 - SoTA-Echoing

| Practice or source line | Source-use relation and currentness | C.30.AD adoption | Action consequence | Boundary |
| --- | --- | --- | --- | --- |
| ISO/IEC/IEEE 42010:2022 architecture-description practice separates architecture description, concern, viewpoint, view, model kind, correspondence, and conformance. | Current international standard and reference source for architecture-description and viewpoint separation. | Adopt the separation of architecture claim, description, viewpoint, view, correspondence, and conformance-to-use; translate it into FPF `EntityOfConcern`, DescriptionContext, view, publication, and direct governing-pattern applications. | Disciplines `C.30.AD:4.1`, `C.30.AD:4.1a`, `C.30.AD:4.2`, `CC-C30AD-1`, `CC-C30AD-3`, and `CC-C30AD-4`: every architecture description names the architecture claim, selected structures, viewpoints and views, correspondence when used or source return when needed, and admissible use. | ISO terminology does not override FPF ontology and does not turn a view or publication into architecture, proof, decision claim, or release authorization. |
| Views-and-Beyond and related architecture documentation practice treats views as stakeholder-relevant projections over architecture. | Mature reference and lineage source for view-based architecture documentation; not used as a mandatory current catalog. | Adopt view usefulness while requiring structure-kind recovery through `C.30.ASV` and description membership through `ArchitectureDescriptionViewMembership@Context`. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.2`, and the multi-view worked case: a view remains useful for a working concern without becoming the selected structure by label. | No mandatory view catalog is imported, and view adequacy remains in `C.30.ASV`. |
| `E.17.0` and MVPK publication machinery in current FPF. | Current internal FPF governing machinery for multi-view Description epistemes, views, viewpoints, publication faces, and publication-form separation. | Reuse generic multi-view and publication machinery instead of minting architecture-local copies. | Disciplines `C.30.AD:4.1a`, `C.30.AD:4.5`, `CC-C30AD-5`, and `CC-C30AD-6`: architecture description composition remains separate from publication form, face, and source-current relation. | C.30.AD specializes architecture-description use; it does not replace E.17.0, E.17.1, E.17.2, E.17, or C.2.P. |
| C4, arc42, ADR, model-card, and system-card practice makes architecture communication practical. | Current practitioner-source family for familiar architecture publication and documentation forms. | Admit these as possible source publications, view publications, decision-description publications, transparency publications, or specification-use records. | Disciplines `C.30.AD:4.5`, worked cases, and anti-patterns: practitioners can use familiar publication forms while keeping source, publication, description, architecture claim, evidence, gate, decision, work-authorization, release-authorization, and other non-description claims separate. | Template, card, graph, or diagram quality is not architecture adequacy by itself. |
| Tool-generated architecture relation graphs and code-agent architecture probing expose useful but partial structure. | Current emerging practice and source-intake concern for generated relation views. | Treat generated graphs as source-derived views with observed, inferred, and unknown relation boundaries. | Disciplines `C.30.AD:4.3`, `C.30.AD:5`, and `CC-C30AD-4`: a generated view can guide structure recovery, source return, and next architecture moves. | Generated relation coverage does not become proof, gate passage, safety assurance, or complete architecture. |

### C.30.AD:11 - Relations

- `C.30` governs grounded architecture and selected-structure adequacy.
- `C.30.P` normalizes overloaded architecture or structure wording before this pattern is used.
- `C.30.ASV` governs architecture structural views and structure-kind and viewpoint separation.
- `C.33` governs capture and loss of selected structure when an architecture description, generated relation graph, ADR-like record, or view set carries only part of the architecture content for a declared use.
- `C.34` governs preservation or correspondence adequacy when the architecture description is being compared with another view, source model, generated output, candidate, or realized structure.
- `C.30.TFS-REL`, `C.30.LCA`, and `C.30.ILC` govern architecture structure-relation subcases named by value.
- `C.32.P2S` governs the connected architecturing flow when the description carries only part of selected structure, decision handoff, method expectation, source-return, or actual-structure feedback.
- `A.7`, `E.17.0`, `E.17.1`, `E.17.2`, and `E.17` govern generic EntityOfConcern, Description, view, viewpoint, publication, and MVPK machinery.
- `C.2.P` normalizes source-current and publication-form relation-set overreads.
- `E.11.PUR` governs recommended FPF pattern use after an architecture description has been read; C.30.AD only records the description-use boundary.
- `A.15.5` governs work-entry readiness and full-kit condition for intended architecture work; C.30.AD only records description, view, correspondence, source-return, freshness, publication-use, and specification-use relations.
- `E.10.MOVE` restores move-like wording when source prose about an architecture description does not mean a C.30 architecture move or a C.30.AD remaining architecture candidate use.

### C.30.AD:End

