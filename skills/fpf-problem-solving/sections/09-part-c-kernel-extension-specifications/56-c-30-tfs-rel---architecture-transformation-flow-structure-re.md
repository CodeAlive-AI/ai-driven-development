## C.30.TFS-REL - Architecture Transformation-Flow Structure Relation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Tech-name:** `ArchitectureTransformationFlowStructureRelation` (relation record)
> **Plain-name:** architecture transformation-flow structure relation
> **Governed object:** the architecture-side relation from `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional architecture-description use to one selected `TransformationFlowStructure` under `E.18`.

### C.30.TFS-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a selected `TransformationFlowStructure`, its path, path slice, crossing, flow valuation, edition pin, plane pin, context pin, no-hidden-scalarization claim, or mathematical description.

The first useful move is small. `ArchitectureTransformationFlowStructureRelation@Context` is a C.30-side relation record for a relation being used between `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use and the E.18 selected transformation-flow structure being used for architecture work. It names the architecture locus, selected structure or view reference when used in the relation, conditional description reference when durable description use is being made, any functional structure view, view-local functional element record, functional behavior, transformer-side filler, candidate bearer, input condition, output condition, functional port, E.18 selected structure, mathematical description, math-lens use, correspondence, publication or edition used by an extracted or generated graph when current, extraction or probe locus, relation observation class, unexplored region, hidden relation-structure return condition, and admissible architecture use that changes the relation.

```text
ArchitectureTransformationFlowStructureRelation@Context:
architectureClaimRef?:
selectedArchitectureStructureRefs?:
architectureStructuralViewRef?:
architectureDescriptionRef?:
functionalStructureViewRef?:
functionalElementRefs?:
functionalBehaviorRefs?:
transformerSideFillerRefs?:
candidateBearerRefs?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:
transformationFlowStructureViewRef?:
transformationFlowStructureRef?:
transformationFlowUnfoldingStructureRef?:
selectedPathOrSliceRefs?:
crossingBundleRefs?:
flowValuationRefs?:
mathematicalDescriptionRefs?:
mathLensUseRefs?:
correspondenceRefs?:
sourcePublicationOrEditionRef?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
nonAdmissibleUse:
```

Ordinary minimum: name at least one architecture-side reference (`architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made), at least one E.18-side reference (`transformationFlowStructureRef`, `transformationFlowUnfoldingStructureRef`, `selectedPathOrSliceRefs`, `crossingBundleRefs`, or `flowValuationRefs`), one blocked overread, and stop or governing-pattern application. Use functional-structure, functional-element, functional-behavior, transformer-side filler, candidate-bearer, input-condition, output-condition, functional-port, transformation-flow-structure, transformation-flow unfolding structure, mathematical-description, math-lens-use, crossing, flow-valuation, correspondence, publication-or-edition, extraction-or-probe, observation-class, unexplored-region, and hidden-relation return fields only when they change the next architecture move. All other fields are conditional and may be `not used`.

Use this relation only when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, functional-architecture view, transformation-flow-structure claim, or conditional architecture-description use depends on an E.18 selected structure, path, crossing, or valuation relation. Stop when the architecture-to-transformation-flow relation and non-admissible uses are clear. If another claim is being made, that claim is governed by its governing pattern and this relation remains only the architecture-to-transformation-flow relation.

What goes wrong if this pattern is missed: a transformation-flow diagram, graph-shaped mathematical description, path slice, or flow valuation becomes functional architecture, whole architecture ontology, performed-work occurrence, work-result record, evidence, gate passage, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for selected transformation-flow structure while C.30 remains the grounded architecture and selected-structure adequacy locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the question under repair is a selected transformation-flow structure, mathematical description, path, crossing, or flow valuation without a relation being used for grounded architecture adequacy, conditional architecture-description use, or an architecture structural view. Use E.18 directly for the selected structure. Use E.18.2 when the mathematical-description claim is current and C.29 when the math-lens-use claim is current. If the question under repair is an architecture claim or durable architecture description without a transformation-flow-structure relation, use C.30. If it is a functional view without transformation-flow relation, use C.30.ASV and A.6.F. If another claim being made is present, use the governing pattern and keep C.30.TFS-REL only to the architecture-to-transformation-flow relation.

### C.30.TFS-REL:2 - Problem

Grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions often need E.18 objects when they discuss transformation-flow structure, functional dependencies, data movement, control paths, evidence-flow descriptions, neural-network dataflow, or code-agent relation graphs.

C.30.TFS-REL prevents collapse by requiring the selected architecture-side reference, such as `ArchitectureOf@Context`, structure ref, structural view, or conditional description use, before any E.18-governed selected transformation-flow structure, path, slice, crossing, or valuation gets architecture use.

### C.30.TFS-REL:3 - Forces

| Force | Tension |
| --- | --- |
| Transformation-flow relation vs architecture takeover | E.18 selected transformation-flow structure, path, or crossing relation can be essential, but it does not become all architecture ontology. |
| Functional view vs transformation-flow view | A functional structure view may need a transformation-flow relation, but a path, crossing, valuation, or mathematical description is not a functional element by itself. |
| Structure precision vs work overread | E.18 gives selected structure, path, and flow-valuation objects; work occurrence and work results remain outside this relation unless their own pattern governs the claim being made. |
| No-hidden-scalarization vs architecture scoring | E.18 set-return and no-hidden-scalarization discipline can inform architecture reasoning, but it does not become a general architecture score. |
| Small relation vs unneeded non-architecture apparatus | A project often needs one relation record, not a full C.29 lens card, evidence relation, assurance case, or decision record. |
| E.18 stability vs C.30 integration | An architecture claim, selected transformation-flow structure, architecture structural view, or conditional architecture-description use needs a relation to E.18 without rewriting E.18 as generic architecture adequacy theory. |

### C.30.TFS-REL:4 - Solution

C.30.TFS-REL is the C.30 entry relation to E.18 when a grounded architecture claim, selected architecture-relevant structure, architecture structural view, or conditional architecture description uses selected `TransformationFlowStructure`, path, crossing, or flow-valuation objects as an architecture-relevant transformation-flow relation.

It supplies only the architecture-to-transformation-flow relation:

```text
ArchitectureTransformationFlowStructureRelation@Context ::= {
  architectureClaimRef?,
  selectedArchitectureStructureRefs?,
  architectureStructuralViewRef?,
  architectureDescriptionRef?,
  functionalStructureViewRef?,
  functionalElementRefs?,
  functionalBehaviorRefs?,
  transformerSideFillerRefs?,
  candidateBearerRefs?,
  inputConditionRefs?,
  outputConditionRefs?,
  functionalPortRefs?,
  transformationFlowStructureViewRef?,
  transformationFlowStructureRef?,
  transformationFlowUnfoldingStructureRef?,
  selectedPathOrSliceRefs?,
  crossingBundleRefs?,
  flowValuationRefs?,
  mathematicalDescriptionRefs?,
  mathLensUseRefs?,
  correspondenceRefs?,
  sourcePublicationOrEditionRef?,
  extractionOrProbeLocusRef?,
  relationObservationClassRef?,
  unexploredRegionRefs?,
  hiddenRelationStructureReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

At least one architecture-side field and at least one E.18-side field must be named by value. Optional fields stay `not used` unless they change inspection, correspondence, hidden relation-structure return, governing-pattern application, or stop.

#### C.30.TFS-REL:4.1 - Use trigger

Use this pattern only when a `ArchitectureOf@Context` claim being made, selected architecture-relevant structure, architecture structural view, functional-structure view, transformation-flow-structure claim, or conditional `ArchitectureDescription@Context` use depends on one or more E.18 objects:

- `TransformationFlowStructureRef`;
- `PathId` or `PathSliceId`;
- `CrossingBundleRef`;
- flow valuation over the `U.Transfer` relation;
- edition, plane, or context pin;
- no-hidden-scalarization or set-return discipline;
- correspondence between functional structure and transformation-flow structure;
- generated or extracted relation graph used as candidate input for the architecture-to-transformation-flow relation.

If the sentence only says that work occurred, use A.15 or the governing work pattern. If the sentence only says that a selected transformation-flow structure exists, use E.18. If the sentence uses a graph-shaped expression as mathematical description, use E.18.2. If it relies on a mathematical lens, use C.29.

Use `transformationFlowUnfoldingStructureRef?` only when the architecture relation depends on an `E.18.3` transformation-flow unfolding structure: the selected E.18 structure is being unfolded toward next architecture, decision, work, feedback, narrative, or refresh uses under constraints and direct exits. Generic architecture use of a constraint-governed unfolding structure belongs in `C.32.P2S` or the direct C.30 architecture governing pattern; this pattern keeps only the architecture-to-transformation-flow relation.

#### C.30.TFS-REL:4.2 - Relation to functional structure

`FunctionalStructureView@Context` under C.30.ASV may cite `ArchitectureTransformationFlowStructureRelation@Context` when a transformation-flow relation is being used. That relation does not make the selected E.18 structure a functional element and does not make a functional element identical with the system, module, method, or flow. It says that a functional structure view, functional behavior, or selected functional element corresponds to, is declared relative to, or positively co-refers with one E.18 selected structure, path, crossing, or valuation relation under a named context.

`FunctionalElement@Context` is a view-local functional-structure record governed by C.30.ASV, not a new root kind. It is current only when C.30.ASV has a selected functional structure view, bounded context, functional behavior, and bearer or candidate-bearer locus. Its functional behavior may be a bounded `U.Transformation` or a compound `TransformationFlowStructure`; its transformer-side filler is recovered through A.3.4 when a transformer claim is current; its module relation is allocation or correspondence through A.6.M. A graph-shaped expression, path, valuation, or flow packet is therefore not the functional element by default.

```text
FunctionTransformationFlowRelationNote:
functionalStructureViewRef:
functionalElementRef?:
functionalBehaviorRef?: U.Transformation | TransformationFlowStructure
transformerSideFillerRef?:
candidateBearerRef?:
inputConditionRefs?:
outputConditionRefs?:
functionalPortRefs?:
transformationFlowStructureViewRef:
architectureTransformationFlowStructureRelationRef:
pathOrSliceRef:
crossingBundleRef:
correspondenceOrCoReferenceClaim:
preservedStructure:
lostOrHiddenStructure:
sourcePublicationOrEditionRef?:
extractionOrProbeLocusRef?:
relationObservationClassRef?:
unexploredRegionRefs?:
hiddenRelationStructureReturnCondition?:
admissibleUse:
nonAdmissibleUse:
```

Use this note when the practitioner needs to see whether the function-to-transformation-flow relation changes inspection, split, relation-making, downgrade, claim-governance assignment named by value, candidate generation, or stop. Use C.30.ASV for the functional structure view, A.6.F for function-like wording recovery, A.3.4 for bounded transformation and transformer slots, A.6.M for module-allocation claims and module-correspondence claims, and E.18 for selected transformation-flow structure.

When several transformation-flow variants are kept or compared as candidate architecture inputs, keep each selected transformation-flow structure, path, crossing, valuation, graph-shaped expression, or mathematical description under `E.18`, `E.18.2`, and this relation. Apply `C.32` only to the architecture candidate palette that uses those selected structures. The graph, path, and flow description does not become architecture adequacy, evidence, assurance, gate passage, selected-set publication, or decision by serving as a candidate input.

#### C.30.TFS-REL:4.3 - Claim-kind applications named by value

| Claim kind being made | Governing pattern to apply |
| --- | --- |
| Work occurrence or work result | `A.15` and the governing work-result or P2W relation |
| Gate decision | `A.21` |
| Evidence claim | `A.10` or `G.6` |
| Assurance claim | `B.3` |
| Causal flow or intervention claim | `C.28` |
| Mathematical-lens use | `C.29` |
| Architecture description or view adequacy | `C.30` or `C.30.ASV` |
| Function-like wording | `A.6.F` |
| Interface, signature, or module compatibility | `A.6.M` module-and-interface repair plus `A.6.5` slot discipline, with `A.6.0` only when a signature declaration is being made |
| Architecture decision | the project-side architecture decision pattern when the corresponding claim is being made |

This table is the single boundary for generic non-flow claims. Elsewhere in this pattern, keep only blocked local overreads that the transformation-flow relation itself makes tempting: structure-as-architecture, graph-description-as-architecture, flow-as-work-log, crossing-as-gate, valuation-as-score, generated relation-graph proof, and prompt-data-tool flow as authority proof.

#### C.30.TFS-REL:4.4 - E.18 selected-structure boundary statement

For an E.18-governed selected `TransformationFlowStructure` used by `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context`, an architecture-to-transformation-flow relation may cite the selected E.18 structure over the described holon plus MVPK faces and correspondences.

Grounded architecture adequacy and conditional architecture-description use are governed by C.30. E.18 supplies selected transformation-flow structure objects and relations; it does not define all architecture structure kinds.

This is the named E.18 selected-structure boundary statement for this relation. It is not a second E.18 source of truth and does not depend on a section number staying stable.

#### C.30.TFS-REL:4.5 - Worked slices

**Functional architecture with a transformation-flow relation being claimed.** A team says, "The functional architecture is this flow diagram." The repair is:

```text
functionalStructureViewRef: required effects and dependencies
functionalElementRefs?: not used; no selected `FunctionalElement@Context` is being claimed
functionalBehaviorRefs?: required effect `authorize payment`
transformerSideFillerRefs?: not used
candidateBearerRefs?: not used
inputConditionRefs?: not used
outputConditionRefs?: not used
functionalPortRefs?: not used
transformationFlowStructureViewRef: selected E.18 transformation-flow structure, path structure, crossing structure, or flow-valuation structure
transformationFlowStructureRef: TransformationFlowStructure@PaymentAuthorization
selectedPathOrSliceRefs: path slices used for the architecture claim
correspondenceRefs: functional effect to flow path relation
nonAdmissibleUse:
  flow diagram as functional architecture itself,
  selected transformation-flow structure as work occurrence,
  mathematical graph description as evidence sufficiency,
  crossing as gate result,
  flow relation as project decision
```

Filled relation record:

```text
ArchitectureTransformationFlowStructureRelation@Context:
architectureClaimRef: ArchitectureOf@CheckoutServiceContext
selectedArchitectureStructureRefs: selected request-handling and payment-authorization flow structure
architectureStructuralViewRef: ArchitectureStructuralView@CheckoutRuntimeFlow
architectureDescriptionRef: not used; the durable architecture description is not being evaluated here
functionalStructureViewRef: FunctionalStructureView@CheckoutRequiredEffects
functionalElementRefs: not used
functionalBehaviorRefs: required effect `authorize payment`
transformerSideFillerRefs: not used
candidateBearerRefs: not used
inputConditionRefs: not used
outputConditionRefs: not used
functionalPortRefs: not used
transformationFlowStructureViewRef: TransformationFlowStructureView@PaymentAuthorizationPath
transformationFlowStructureRef: TransformationFlowStructure@Checkout-v3
selectedPathOrSliceRefs: PathSlice@request-to-payment-authorization
crossingBundleRefs: not used
flowValuationRefs: not used
mathematicalDescriptionRefs: not used
correspondenceRefs: required effect `authorize payment` corresponds to the E.18 path slice; this is correspondence, not identity
sourcePublicationOrEditionRef: model or generated graph edition when the flow relation was extracted from one
extractionOrProbeLocusRef: path-slice extraction or code-agent probe locus when current
relationObservationClassRef: observed, inferred, or unknown relation class when current
unexploredRegionRefs: not used
hiddenRelationStructureReturnCondition: reopen if mathematical-description edition, path slice, relation observation class, or required-effect declaration changes
admissibleUse: inspect whether the functional structure view depends on the E.18 path slice being used and whether an architecture split or correspondence note is needed
nonAdmissibleUse: flow diagram as functional architecture itself; selected transformation-flow structure as work occurrence; mathematical graph description as evidence sufficiency; crossing as gate result; flow relation as project decision
```

Near miss: if the selected transformation-flow structure has no C.30-side architecture reference named by value, the case stays in `E.18`. If the same sentence is a mathematical description, use `E.18.2`; if it is a math-lens-use claim, use `C.29`. If it is a work log, evidence claim, gate decision, or benchmark result, that non-flow claim is governed by its governing pattern and this relation keeps only the architecture-to-transformation-flow relation.

**Pump-station flow relation.** A plant team says, "the safety architecture is the bypass flow." C.30.TFS-REL applies only if the plant `ArchitectureOf@Context`, selected control or material-flow structure, and E.18 selected bypass-flow structure are named. The bypass path may be architecture-relevant, but it is not safety proof, performed maintenance work, gate passage, or release permission. The relation record names the plant architecture locus, selected E.18 path or crossing, hidden relation-structure return condition, and the one architecture move changed by the bypass relation.

**Supply-chain transformation-flow relation.** A logistics architecture view may use an E.18 selected flow structure for supplier handoff, transport crossing, freshness window, and valuation. The architecture claim remains about selected supply-chain structure; work occurrences, contractual commitments, evidence, and gate decisions stay with their governing patterns.

**Neural-network dataflow change.** Source labels such as attention block, SSM block, convolution block, memory mechanism, cache mechanism, and MoE expert-selection go through `C.30.STRAT` unless the changed value is already recovered. C.30.TFS-REL applies only when the changed structure kind and transformation-flow relation are named. A benchmark, ablation, or pruning result may bear on a non-architecture claim named by value, but it does not make the flow relation an architecture decision or evidence sufficiency by itself.

**Code-agent relation graph.** A code-agent relation graph with `IMPORTS`, `CALLS_API`, `REGISTRY_WIRES`, or `DATA_FLOWS_TO` edges can be used for an architecture-to-transformation-flow relation only with the source publication or codebase edition, extraction or probe locus, relation observation class selected from {observed, inferred, unknown}, typed relation semantics, unexplored regions, and hidden relation-structure return condition when subsequent action relies on hidden distinctions.

#### C.30.TFS-REL:4.6 - Lowering and currentness conditions

Lower, narrow, or reopen the relation at the smallest changed locus when:

- E.18 selected structure, path, crossing, or flow-valuation semantics change;
- edition, plane, context pin, set-return, or no-hidden-scalarization discipline changes;
- source publication or graph edition, path slice, relation observation class, edition or context pin, unexplored region, or hidden relation-structure return condition changes;
- the C.30 architecture locus, selected architecture-relevant structure, architecture structural view, conditional architecture description, or C.30.ASV relation changes;
- functional-to-transformation-flow correspondence changes;
- a non-flow claim is being made and is governed by `C.30.TFS-REL:4.3` rather than by this relation;
- C.29, C.16, C.28, A.10, G.6, B.3, A.20, A.21, A.15, C.30, C.30.ASV, A.6.F, C.30.STRAT, or E.18 changes the governing boundary used by the relation.

Admissible repair results are: update the affected reference, add or change correspondence, add or change the hidden relation-structure return condition, narrow admissible use, keep the selected-structure claim inside E.18, keep the mathematical-description claim inside E.18.2, keep the math-lens-use claim inside C.29, apply the governing pattern to a non-flow claim, lower to quote-only or reduced-use cue, or block the architecture-to-transformation-flow use.

### C.30.TFS-REL:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees a flow diagram, path, or graph-shaped expression and wants to use it for a grounded architecture claim, selected architecture-relevant structure, architecture structural view, or conditional architecture description. C.30.TFS-REL asks whether a selected E.18 transformation-flow relation is current for the selected architecture locus, and names its non-admissible uses. |
| Show: `U.System` | A software system, plant, AI agent, neural network, vehicle, or supply chain may have transformation-flow structure. A diagram or mathematical description can inform architecture reasoning about that structure without carrying the non-flow claims named in `C.30.TFS-REL:4.3`. |
| Show: `U.Episteme` | A mathematical graph description, generated relation graph, code-agent probe, neural-network diagram, dashboard, or architecture note is an episteme, view, or publication. It can publish or substantiate the transformation-flow relation only when its E.18 object, context pins, correspondence, hidden relation-structure return condition, and admissible use are recoverable. |

### C.30.TFS-REL:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto**, **Epist**, **Prag**, **Did**, **Gov**. Scope: architecture-to-transformation-flow relations using E.18 objects.

| Bias risk | Mitigation |
| --- | --- |
| Structure-or-description-as-architecture bias | The pattern states that grounded architecture adequacy and conditional architecture-description use stay with C.30, mathematical descriptions stay with E.18.2, math-lens uses stay with C.29, and structural views stay with C.30.ASV. |
| Function-flow collapse | Functional structure and transformation-flow structure are related, not identical by default. Identity requires a positive selected-structure co-reference check. |
| Non-flow claim overread | The relation table assigns non-flow claim kinds to their governing patterns. |
| Mathematical overread | Mathematical-lens use of a graph or valuation is governed by C.29. |
| Check-only bias | Conformance checks include repair actions and stop conditions. |

This checklist verifies the preceding guidance after the practitioner has chosen the selected repair action; it is not a required project control form and not a substitute for the card, note, relation, or repair guidance above.

### C.30.TFS-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30TFR-1 E.18 object.** | The relation names the E.18 selected transformation-flow structure, path, slice, crossing, or flow valuation object it uses. | Add the E.18 object reference named by value or use C.30 or C.30.ASV without this relation. |
| **CC-C30TFR-2 Architecture locus.** | The relation names `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use it relates to. | Add `architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made; otherwise keep the selected-structure claim inside E.18, the mathematical-description claim inside E.18.2, or the math-lens-use claim inside C.29. |
| **CC-C30TFR-3 Functional and flow separation.** | Functional structure and transformation-flow structure remain separate unless correspondence or positive selected-structure co-reference is declared. | Add `FunctionTransformationFlowRelationNote`, add the co-reference check, or remove the functional-architecture claim from the flow sentence. |
| **CC-C30TFR-4 No architecture takeover.** | The selected transformation-flow structure or its mathematical description is not treated as generic architecture ontology or all architecture structure kinds. | Assign grounded architecture claims, selected architecture-relevant structures, or conditional architecture-description use to C.30 and keep this pattern to the architecture-to-transformation-flow relation. |
| **CC-C30TFR-5 No work overread.** | A selected structure, path, or slice is not treated as work occurrence or work result. | Assign the work claim to A.15 or the governing work-result pattern. |
| **CC-C30TFR-6 No evidence, assurance, or gate overread.** | The relation is not used as evidence sufficiency, assurance claim, gate decision, or release permission without evidence named by value, assurance, gate, or release pattern application. | Assign the claim being made to A.10, G.6, B.3, A.20, A.21, or the release locus named by value when a release claim is being made. |
| **CC-C30TFR-7 Causal and mathematical boundaries.** | Causal or intervention claims and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the relation's admissible use. |
| **CC-C30TFR-8 Pin and scalarization boundary.** | Edition, context, and plane pins plus no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin and set-return references or remove the comparison or selection claim. |
| **CC-C30TFR-9 Hidden relation return.** | Extracted, generated, coarsened, or partial relation graphs or flow diagrams state the source publication or edition, extraction or probe locus, relation observation class, unexplored regions, and hidden relation-structure return condition when hidden distinctions affect action. | Add the missing relation-structure fields or narrow the admissible use. |
| **CC-C30TFR-10 Useful action.** | The repair leaves a remaining use: name selected structure, path, or crossing relation; add correspondence; return to source; assign the claim being made to a governing pattern; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-C30TFR-11 Lowering and currentness.** | The relation states the smallest changed locus when E.18 semantics or pins, relation observation class, architecture locus, correspondence, hidden relation-structure return, or related governing boundary changes. | Update the affected reference, narrow admissible use, keep the selected-structure claim inside E.18, keep the mathematical-description claim inside E.18.2, keep math-lens use inside C.29, apply the governing pattern to the non-flow claim, lower the relation, or block architecture-to-transformation-flow use. |

### C.30.TFS-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-architecture** | The E.18 selected transformation-flow structure is called the whole architecture. | Use C.30 for the grounded architecture claim, selected architecture-relevant structure, or conditional architecture description, and keep this relation only for the transformation-flow relation. |
| **Graph-description-as-functional-architecture** | A graph-shaped mathematical description or diagram is treated as the functional architecture itself. | Split functional structure, selected transformation-flow structure, mathematical description, and publication face; add correspondence when needed. |
| **Flow-as-work-log** | Path or slice wording is treated as work occurrence. | Assign occurrence or result claims to A.15 or P2W and keep E.18 to selected structure, path, slice, or valuation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern when those claims are being made. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover the source publication or codebase edition, extraction or probe locus, relation observation class selected from {observed, inferred, unknown}, hidden structure, and evidence or assurance pattern governing the claim applications. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow diagram is treated as permission for tool action or proof that authority is safe. | Keep the diagram as a transformation-flow relation or E.18.2 mathematical description. A path from untrusted content to tool action is governed by `SecurityTrustBoundaryStructure`, C.24, E.16, A.20, or A.21 when those claim kinds are being made. |

### C.30.TFS-REL:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| E.18 selected structure, path, crossing, and flow-valuation discipline becomes usable for grounded architecture claims, selected architecture-relevant structures, architecture structural views, and conditional architecture descriptions. | A conforming use names the C.30 architecture record, selected structure ref, C.30.ASV structural-view reference, or conditional architecture-description ref that uses the transformation-flow relation. |
| Functional structure and transformation-flow structure stay separable unless positive co-reference is declared. | Concise "the diagram is the architecture" prose is repaired before it is used for an FPF claim kind or admissible-use boundary. |
| Non-flow claim kinds are assigned to their governing patterns. | More governing patterns are named when practitioners try to overuse the diagram, mathematical expression, or selected structure. |
| The E.18 selected-structure boundary statement stays narrow. | Generic architecture adequacy remains outside E.18. |

### C.30.TFS-REL:10 - Rationale

E.18 is the governing FPF pattern for selected transformation-flow structures, paths, crossings, flow valuations, and related pins. Architecture needs to use that work without letting it become generic architecture ontology. The smallest stable relation is therefore a C.30-side record that points to E.18 objects and states admissible and non-admissible architecture use.

This pattern also protects functional architecture. A functional structure view may correspond to a transformation-flow structure, and in some cases both may refer to the same selected `U.StructureRef`; that identity is not automatic. The relation is useful precisely because it preserves the difference while allowing correspondence or positive co-reference.

### C.30.TFS-REL:11 - SoTA-Echoing

| Practice or reference line | C.30.TFS-REL adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| E.18 transformation-flow structure, path, crossing, and flow-valuation discipline | Adopt E.18 as the governing source for selected structure, path, crossing, and valuation objects. | The pattern names E.18 references rather than redefining flow semantics. | E.18 does not become generic architecture ontology or architecture-description ontology. |
| ISO/IEC/IEEE 42010:2022 and multi-view architecture practice | Adapt view and correspondence discipline to architecture-to-transformation-flow reliance. | Transformation-flow views relate to grounded architecture claims, selected architecture-relevant structures, architecture structural views, or conditional architecture descriptions through C.30, C.30.ASV, and correspondence refs. | Architecture views do not become proof, evidence, gates, or decisions. |
| MBSE and SysML v2 view and relation practice | Adapt model-derived flow views and path views as description-episteme relations derived from a model publication or model edition. | A model-derived flow view states model edition, selected structure, hidden or lost structure, and admissible use. | Tool models do not override FPF E.18 or C.30 relations. |
| Neural-network dataflow and GonzoML architecture-operation corpus | Adopt practitioner flow-structure recognition for block replacement, path-selection, memory and cache placement, MoE expert-selection, pruning, distillation, ablation, and compute, memory, and latency tradeoffs. | Keep block, cache, expert, router, gate, and similar words as `C.30.STRAT` source labels until the transformation-flow structure is recovered; C.30.TFS-REL applies only when that recovered structure changes the architecture move. | Benchmarks, ablations, pruning masks, or architecture-search outputs do not become evidence sufficiency, assurance, gate passage, or architecture decision by themselves. |
| Theory of Code Space and arXiv:2603.00601 code-agent relation graph probing | Adapt relation graphs with relation observation class selected from {observed, inferred, unknown} and partial-observability warnings. | Generated code relation graphs can be used for a transformation-flow relation only with typed relation semantics, source publication or codebase edition pins, extraction or probe locus, unexplored regions, and hidden relation-structure return condition. | Do not mint `U.CodeSpace`; do not treat probe output as internal belief proof, architecture adequacy, assurance, or release evidence or release claim. |

**Currentness boundary.** The inputs to the currentness judgment are E.18 object semantics and pins, C.30 and C.30.ASV architecture-side relation rules, the relation observation class, and the non-flow governing patterns named in `C.30.TFS-REL:4.3`. When one changes, the relation changes only at the affected reference, correspondence, hidden relation-structure return condition, admissible-use boundary, or governing-pattern assignment.

### C.30.TFS-REL:12 - Relations

Builds on: `C.30`, `C.30.ASV`, `A.22`, `A.6.F`, `E.18`, `E.17`, `E.17.0`, `A.7`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `C.30.STRAT`, `C.32.P2S` when architecture-to-transformation-flow grounding is one stage of problem-to-structure architecturing, `C.32` when selected transformation-flow variants become candidate architecture inputs, `C.33` when transformation-flow relation descriptions capture or lose selected architecture structure, `C.34` when transformation-flow relation claims must be preserved across a mapping, model, generated output, or realization, `C.35` when a generated or discovered transformation-flow carrier may seed synthesis, `A.15`, `A.20`, `A.21`, `A.10`, `G.6`, `B.3`, `C.28`, `C.29`, `C.16`, admitted measurement, selection, or candidate-set governing patterns when those claims are being made, `A.6.M` module-and-interface repair, `A.6.5` slot discipline, and `A.6.0` when a signature declaration is being made.

Related claims stay with their governing patterns: `C.30.STRAT` for stratification wording and source-label repair, `E.18` for selected transformation-flow structure, path, crossing, and flow-valuation discipline, `E.18.2` and `C.29` for mathematical descriptions and lens-use claims, `C.30` for grounded architecture and selected-structure adequacy, `C.30.ASV` for architecture structural-view adequacy, `C.32.P2S` for connected problem-to-structure carry-through, `A.6.F` for function-use repair, and the non-flow governing patterns named in `C.30.TFS-REL:4.3`. `C.30.TFS-REL` governs only the architecture-to-transformation-flow-structure relation being claimed.

### C.30.TFS-REL:End

