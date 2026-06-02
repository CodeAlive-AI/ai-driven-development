## C.30.TGA-FLOW-REL - Architecture/TGA Flow-Structure Relation

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.30.TGA-FLOW-REL:1 - Problem frame

Use this pattern when an architecture discussion depends on a Transduction Graph Architecture (TGA) graph, path, path slice, crossing, flow valuation, edition pin, plane/context pin, or no-hidden-scalarization claim.

The first useful move is small. `ArchitectureFlowStructureRelation@TGA` is a C.30-side relation record that links an architecture description or architecture structural view to E.18 graph, path, crossing, or flow-valuation relation; it is not the graph, not the architecture, not an architecture decision, and not a complete architecture view by itself.

```text
ArchitectureFlowStructureRelation@TGA:
architectureDescriptionRef:
architectureStructuralViewRef:
functionalStructureViewRef:
flowTransductionStructureViewRef:
transductionGraphRef:
activePathOrSliceRefs:
crossingBundleRefs:
flowValuationRefs:
correspondenceRefs:
sourceReturnCondition?:
admissibleUse:
nonAdmissibleUse:
governingPatternApplicationRefs:
```

Ordinary minimum: name either `architectureStructuralViewRef` or `architectureDescriptionRef`, one E.18 graph or path-slice reference, the architecture-flow `FlowTransductionStructure`, one blocked overread, and stop or exact governing pattern application. Use crossing, flow-valuation, correspondence, and source-return fields only when they change the next architecture move. All other fields are conditional and may be `not live`.

Use this relation only when a functional-architecture or flow-structure claim uses E.18 graph/path/crossing/valuation relation. Stop when the architecture flow relation and non-admissible uses are clear. Do not open work, evidence, assurance, gate, causal, mathematical-lens, P2W, or architecture-decision claim unless that claim kind is live.


What goes wrong if this pattern is missed: a TGA graph becomes functional architecture, whole architecture ontology, work sequence, evidence path, gate result, causal flow proof, assurance claim, or project decision by appearance.

What this buys in practice: the practitioner can use E.18 for flow/transduction structure while C.30 remains the governing architecture-description locus and C.30.ASV remains the architecture-structural-view locus.

Not this pattern when the live question is a graph, path, crossing, or flow valuation without architecture-description claim kind. Use E.18 directly. If the live question is architecture description without E.TGA graph/path/crossing claim kind, use C.30. If it is a functional view without flow/TGA claim kind, use C.30.ASV and A.6.F. If it is work, evidence, assurance, gate, causal use, mathematical-lens adequacy, P2W, or decision claim, use the exact governing pattern and keep C.30.TGA-FLOW-REL only to the architecture-flow relation.

### C.30.TGA-FLOW-REL:2 - Problem

TGA already governs transduction graphs, paths, crossings, and flow valuations. Architecture descriptions often need those objects when they discuss flow/transduction structure, functional dependencies, data movement, control paths, evidence flows, neural-network dataflow, or code-agent relation graphs.

The risk is overread. A TGA graph can be useful enough that practitioners start treating it as the architecture, the functional architecture, the work sequence, or the proof that evidence, gate, safety, causality, or assurance conditions are satisfied. C.30.TGA-FLOW-REL prevents that collapse by relating architecture structural views to E.18-governed graph/path/crossing objects without redefining E.TGA.

### C.30.TGA-FLOW-REL:3 - Forces

| Force | Tension |
| --- | --- |
| Flow relation vs architecture takeover | E.TGA graph/path/crossing relation can be essential, but it does not become all architecture ontology. |
| Functional view vs flow view | A functional structure view may need a flow relation, but a graph/path/crossing object is not a functional element by itself. |
| Graph precision vs work overread | E.18 gives precise graph/path/flow valuation objects; work occurrence and work results remain outside TGA unless their own pattern is live. |
| No-hidden-scalarization vs architecture scoring | E.18 set-return and no-hidden-scalarization discipline can inform architecture reasoning, but it does not become a general architecture score. |
| Small relation vs unneeded non-architecture apparatus | A project often needs one relation record, not a full C.29 lens card, evidence path, assurance case, or decision record. |
| E.18 stability vs C.30 integration | A TGA-based architecture description needs a relation to E.18 without rewriting E.TGA as generic architecture-description theory. |

### C.30.TGA-FLOW-REL:4 - Solution

C.30.TGA-FLOW-REL is the C.30 entry relation to E.18 when an architecture description or architecture structural view uses E.TGA graph/path/crossing/flow-valuation objects as flow/transduction structure relation.

It imports E.18; it does not redefine E.TGA. It supplies only the architecture-description relation:

```text
ArchitectureFlowStructureRelation@TGA ::= {
  architectureDescriptionRef,
  architectureStructuralViewRef?,
  functionalStructureViewRef?,
  flowTransductionStructureViewRef?,
  transductionGraphRef,
  activePathOrSliceRefs,
  crossingBundleRefs?,
  flowValuationRefs?,
  correspondenceRefs,
  sourceReturnCondition?,
  admissibleUse,
  nonAdmissibleUse
}
```

#### C.30.TGA-FLOW-REL:4.1 - Use trigger

Open this pattern only when a live architecture claim depends on one or more E.18 objects:

- `TransductionGraphRef`;
- `PathId` or `PathSliceId`;
- `CrossingBundleRef`;
- `U.Transfer` flow valuation;
- edition, plane, or context pin;
- no-hidden-scalarization or set-return discipline;
- correspondence between functional structure and flow/transduction structure;
- generated or extracted relation graph used as architecture-flow reliance.

If the sentence only says that work occurred, use A.15 or the governing work pattern. If the sentence only says that a graph exists, use E.18. If the sentence uses the graph as mathematical-lens reliance, use C.29.

#### C.30.TGA-FLOW-REL:4.2 - Relation to functional structure

`FunctionalStructureView@Context` under C.30.ASV may cite `ArchitectureFlowStructureRelation@TGA` when flow is live. That relation does not make the TGA graph a functional element. It says that a functional structure view corresponds to or is declared relative to one E.18 graph/path/crossing relation.

```text
FunctionFlowRelationNote:
functionalStructureViewRef:
flowTransductionStructureViewRef:
architectureFlowStructureRelationRef:
functionOrEffect:
pathOrSliceRef:
crossingBundleRef:
preservedStructure:
lostOrHiddenStructure:
admissibleUse:
nonAdmissibleUse:
```

Use this note when the practitioner needs to see whether the function-flow relation changes inspection, split, relation-making, downgrade, exact governing pattern application, candidate generation, or stop.

#### C.30.TGA-FLOW-REL:4.3 - Exact claim-kind applications

| Live claim kind | Governing pattern to apply |
| --- | --- |
| Work occurrence or work result | `A.15` and the governing work-result or P2W relation |
| Gate decision | `A.21` |
| Evidence claim | `A.10` or `G.6` |
| Assurance claim | `B.3` |
| Causal flow or intervention claim | `C.28` |
| Mathematical-lens adequacy | `C.29` |
| Architecture description or view adequacy | `C.30` or `C.30.ASV` |
| Function-like wording | `A.6.F` |
| Interface/signature/module compatibility | `InterfaceSignatureBoundaryNote` or the exact module/interface repair pattern when live |
| Architecture decision | the exact project-side architecture decision pattern when live |

#### C.30.TGA-FLOW-REL:4.4 - E.18:5.12 boundary statement

For the E.TGA-governed flow/transduction structure kind of an architecture description, an architecture-flow description may consist of an E.TGA transduction graph over the described holon plus MVPK faces and correspondences.

Generic architecture description is governed by C.30. E.TGA supplies the flow/transduction substrate and does not define all architecture structure kinds.

This is the E.18:5.12 boundary statement. It is not a TGA rewrite and not a second E.TGA source of truth.

#### C.30.TGA-FLOW-REL:4.5 - Worked slices

**Functional architecture with live flow.** A team says, "The functional architecture is this TGA graph." The repair is:

```text
functionalStructureViewRef: required effects and dependencies
flowTransductionStructureViewRef: flow/path/crossing structure
transductionGraphRef: E.18 graph
activePathOrSliceRefs: current path slices used for the architecture claim
correspondenceRefs: functional effect to flow path relation
nonAdmissibleUse:
  graph as functional architecture itself,
  graph as work occurrence,
  graph as evidence sufficiency,
  graph as gate result,
  graph as project decision
```

**Neural-network dataflow change.** Replacing attention, SSM, convolution, memory/cache, MoE expert-selection, or another block changes architecture only when the changed structure kind and flow/transduction relation are named. A benchmark, ablation, or pruning result may bear on an exact non-architecture claim, but it does not make the flow relation an architecture decision or evidence sufficiency by itself.

**Code-agent relation graph.** A code-agent relation graph with `IMPORTS`, `CALLS_API`, `REGISTRY_WIRES`, or `DATA_FLOWS_TO` edges can be used for an architecture-flow relation only with source edition, observed/inferred/unknown status, typed relation semantics, unexplored regions, and source-return condition when subsequent action relies on hidden distinctions.

### C.30.TGA-FLOW-REL:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees a graph or path and wants to use it in an architecture description. C.30.TGA-FLOW-REL asks whether the graph is E.18-governed flow/transduction relation for an architecture structural view, and names its non-admissible uses. |
| Show: `U.System` | A software system, plant, AI agent, neural network, vehicle, or supply chain may have flow/transduction structure. The graph can inform architecture reasoning about that structure without proving work, safety, evidence, gate, or decision claims. |
| Show: `U.Episteme` | A TGA graph, generated relation graph, code-agent probe, neural-network diagram, dashboard, or architecture note is an episteme/view/publication. It can publish or substantiate the flow relation only when its E.18 object, context pins, correspondence, source-return condition, and admissible use are recoverable. |

### C.30.TGA-FLOW-REL:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto/Epist**, **Prag**, **Did**, **Gov**. Scope: architecture-flow relations using E.18 objects.

| Bias risk | Mitigation |
| --- | --- |
| Graph-as-architecture bias | The pattern states that generic architecture description stays with C.30 and structural views with C.30.ASV. |
| Function-flow collapse | Functional structure and flow/transduction structure are related, not identical. |
| Work/evidence/gate overread | The relation table assigns work, evidence, assurance, gate, causal, and decision claim kinds to their governing patterns. |
| Mathematical overread | C.29 carries mathematical-lens adequacy when a graph or valuation is used as a lens. |
| Check-only bias | Conformance checks include repair moves and stop conditions. |

This checklist verifies the preceding guidance after the practitioner has chosen the live move; it is not a required project control form and not a substitute for the card, note, relation, or repair move above.

### C.30.TGA-FLOW-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-TGA-FLOW-1 E.18 object.** | The relation names the E.18 graph, path, slice, crossing, or flow valuation object it uses. | Add the exact E.18 reference or use C.30/C.30.ASV without TGA relation. |
| **CC-TGA-FLOW-2 Architecture locus.** | The relation names the architecture description or architecture structural view it relates to. | Add `architectureDescriptionRef` or `architectureStructuralViewRef`, or keep the graph claim inside E.18 only. |
| **CC-TGA-FLOW-3 Functional/flow separation.** | Functional structure and flow/transduction structure remain separate unless a correspondence is declared. | Add `FunctionFlowRelationNote` or remove the functional-architecture claim from the graph sentence. |
| **CC-TGA-FLOW-4 No TGA architecture takeover.** | The TGA graph is not treated as generic architecture ontology or all architecture structure kinds. | Assign generic architecture-description claims to C.30 and keep this pattern to flow/transduction structure. |
| **CC-TGA-FLOW-5 No work overread.** | A graph/path/slice is not treated as work occurrence or work result. | Assign the work claim to A.15 or the governing work-result pattern. |
| **CC-TGA-FLOW-6 No evidence/assurance/gate overread.** | The relation is not used as evidence sufficiency, assurance claim, gate decision, or release permission without exact evidence, assurance, gate, or release pattern application. | Assign the live claim to A.10/G.6, B.3, A.20/A.21, or release loci as live. |
| **CC-TGA-FLOW-7 Causal and mathematical boundaries.** | Causal/intervention and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the relation's admissible use. |
| **CC-TGA-FLOW-8 Pin and scalarization boundary.** | Edition/context/plane pins and no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin/set-return references or remove the comparison/selection claim. |
| **CC-TGA-FLOW-9 Source return.** | Extracted, generated, coarsened, or partial graphs state source-return conditions when hidden distinctions affect action. | Add source-return condition or narrow the admissible use. |
| **CC-TGA-FLOW-10 Useful action.** | The repair leaves a surviving move: name graph/path/crossing relation, add correspondence, return to source, assign the live claim to an exact governing pattern, or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

### C.30.TGA-FLOW-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Graph-as-architecture** | The E.18 graph is called the architecture. | Use C.30 for architecture description and this relation only for flow/transduction structure. |
| **Graph-as-functional-architecture** | A TGA graph is treated as the functional architecture itself. | Split functional structure from flow/transduction structure and add correspondence. |
| **Flow-as-work-log** | Path or slice wording is treated as work occurrence. | Assign occurrence or result claims to A.15/P2W and keep TGA as graph/path relation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted receiving pattern when live. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover source, observed/inferred/unknown status, hidden structure, and exact evidence/assurance pattern applications. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow graph is treated as permission for tool action or proof that authority is safe. | Keep the graph as a flow relation. A path from untrusted content to tool action opens `SecurityTrustBoundaryStructure` and C.24/E.16/A.20/A.21 governing pattern applications when those claim kinds are live. |


### C.30.TGA-FLOW-REL:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| E.18 graph/path/crossing discipline becomes usable in architecture descriptions. | A conforming use names the C.30 architecture record or C.30.ASV structural-view reference that uses the TGA relation. |
| Functional structure and flow/transduction structure stay separable. | Concise "the graph is the architecture" prose is repaired before it carries FPF claim force. |
| Work, evidence, assurance, gate, causal, mathematical, and decision claim kinds are assigned to their governing patterns. | More exact governing pattern applications are named when practitioners try to overuse the graph. |
| The E.18:5.12 boundary statement stays narrow. | Generic architecture-description theory remains outside E.18. |

### C.30.TGA-FLOW-REL:10 - Rationale

E.TGA is already the governing FPF pattern for transduction graphs, paths, crossings, flow valuations, and related pins. Architecture needs to use that work without letting it become generic architecture ontology. The smallest stable relation is therefore a C.30-side record that points to E.18 objects and states admissible and non-admissible architecture use.

This pattern also protects functional architecture. A functional structure view may correspond to flow/transduction structure, but function and flow are different structure kinds. The relation is useful precisely because it preserves that difference while allowing correspondence.

### C.30.TGA-FLOW-REL:11 - SoTA-Echoing

| Practice or source line | C.30.TGA-FLOW-REL adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| E.18 E.TGA graph/path/crossing and flow-valuation discipline | Adopt E.18 as the governing source for graph/path/crossing/valuation objects. | The pattern names E.18 references rather than redefining graph or flow semantics. | E.18 does not become generic architecture-description ontology. |
| ISO/IEC/IEEE 42010:2022 and multi-view architecture practice | Adapt view/correspondence discipline to architecture-flow reliance. | Flow/transduction views relate to architecture descriptions through C.30/C.30.ASV and correspondence refs. | Architecture views do not become proof, evidence, gates, or decisions. |
| MBSE/SysML v2 view and relation practice | Adapt model-derived flow/path views as D/S source relations. | A model-derived flow view states source, selection, hidden/lost structure, and admissible use. | Tool models do not override FPF E.18 or C.30 carriers. |
| Neural-network dataflow and GonzoML architecture-operation corpus | Adopt practitioner flow-structure recognition for block replacement, path-selection, memory/cache placement, MoE expert-selection, pruning, distillation, ablation, and compute/memory/latency tradeoffs. | Such cases open C.30.TGA-FLOW-REL only when flow/transduction structure changes the architecture move. | Benchmarks, ablations, pruning masks, or architecture-search outputs do not become evidence sufficiency, assurance, gate passage, or architecture decision by themselves. |
| Theory of Code Space / arXiv:2603.00601 and code-agent relation graph probing | Adapt observed/inferred/unknown relation graphs and partial-observability warnings. | Generated code relation graphs can be used for flow relation only with typed relation semantics, source pins, unexplored regions, and source return. | Do not mint `U.CodeSpace`; do not treat probe output as internal belief proof, architecture adequacy, assurance, or release evidence or release claim. |

### C.30.TGA-FLOW-REL:12 - Relations

Builds on: `C.30`, `C.30.ASV`, `A.22`, `A.6.F`, `E.18`, `E.17`, `E.17.0`, `A.7`, `E.10`, `C.2.P`, and `F.18`.

Coordinates with: `A.15`, `A.20`, `A.21`, `A.10`, `G.6`, `B.3`, `C.28`, `C.29`, `C.16`, admitted measurement/selection/candidate-set receiving patterns when live, `InterfaceSignatureBoundaryNote`, and the exact module/interface repair pattern when module or interface claim kind is live.

Does not replace: E.18 graph/path/crossing/flow valuation discipline, C.30 architecture-description adequacy, C.30.ASV architecture structural-view adequacy, A.6.F function-use repair, A.15 work, A.10/G.6 evidence, B.3 assurance, A.20/A.21 gate/release records, C.28 causal-use support, C.29 mathematical-lens adequacy, C.16 characterization or admitted characteristic/measurement receiving patterns, or C.11 decisions.

### C.30.TGA-FLOW-REL:End

