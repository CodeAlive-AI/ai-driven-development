## E.18.3 - Constraint-Governed Transformation-Flow Unfolding Structure

> **Type:** E.18 transformation-flow specialization of `A.22.CGUS`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### E.18.3:0 - Use This When

Use this pattern when the unfolding structure is specifically a `U.Structure` whose substrate is transformation-flow structure over bounded `U.Transformation` values and adjacent governed loci such as method-selection, mechanism realization, work planning, work occurrence, evidence, assurance, gate, architecture use, narrative or publication use, result interpretation, or refresh.

Do not use this pattern merely because a visible record or description is a route, path, graph, process map, chain, loop, or swimlane. First ask whether transformation loci, crossings, guards, valuation, and transformation-flow preserved or lost structure are recoverable.

### E.18.3:1 - Problem Frame

`E.18` already gives FPF a rich language for transformation-flow structure: transfers, paths, crossings, guards, valuations, publication faces, comparability, refresh locality, and structure-positioned slot-filler loci. `A.22.CGUS` gives the broader A.22 specialization of `U.Structure` for constraint-governed unfolding structures. A practitioner needs the narrow bridge between them: when is an unfolding structure a transformation-flow unfolding structure, and what must remain outside it?

### E.18.3:2 - Problem

Transformation-flow artifacts are easy to overread. A path diagram becomes a workflow. A flow card becomes performed work. A P2W chain becomes work authorization. A graph expression becomes the whole structure. A gate, evidence path, architecture decision, or publication face becomes part of the transformation-flow ontology by visual adjacency.

The repair cannot be lexical. The pattern must say which transformations and adjacent loci are current, how they are constrained, what structure is preserved and lost, which direct governing patterns govern stronger claims, and when the current slice stops or returns.

### E.18.3:3 - Forces

| Force | Tension |
| --- | --- |
| Transformation-flow richness vs universal-parent drift | E.18 is rich enough to explain many route-shaped transformation cases, but narrative, abduction, grounding, improvement, and README-entry seeds are not transformation-flow merely by shape. |
| Flow card usefulness vs work-order overread | A path or flow card can guide a next FPF use, but it does not authorize performed work or decide launch readiness. |
| Adjacent loci vs ontology absorption | Method, work, evidence, gate, decision, architecture, publication, and refresh loci can be adjacent to a flow without becoming flow ontology. |
| Demonstrative slices vs actual traces | A path slice may show a traversal for learning or review; actual project history may branch, pause, retry, or skip that traversal. |

### E.18.3:4 - Solution

Select `ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure` as the E.18 transformation-flow specialization of `ConstraintGovernedUnfoldingStructure@Context`.

```text
ConstraintGovernedTransformationFlowUnfoldingStructure@Context:
  kind: U.Structure
  unfoldingStructureRef:
  boundedContextRef:
  transformedEntityOrConcernRef:
  transformationLoci[]:
  adjacentGovernedLoci[]:
  transferOrDependencyRelations[]:
  pathOrPathSliceRefs[]:
  crossingRefs[]:
  guardRefs[]:
  flowValuationRef?:
  methodWorkLinkageRef?:
  evidenceOrAssuranceLinkageRef?:
  architectureUseRef?:
  narrativeOrPublicationUseRef?:
  preservedTransformationStructure:
  lostOrHiddenTransformationStructure:
  nonAdmissibleOverreads:
  returnToGoverningPatternCondition:
  stopOrReopenCondition:
```

The record is admitted only when the substrate is bounded transformation-flow structure. `A.3.4` governs each atomic bounded transformation claim. `E.18` governs the compound structure over transformations, crossings, path slices, guards, valuations, and structure-positioned loci. This pattern governs the narrower `U.Structure` specialization that says how the current transformation-flow structure unfolds toward next uses without becoming those uses.

`methodWorkLinkageRef?` may point to one `MethodWorkUnfoldingLinkage@Context` when the method-work relation itself must stay inspectable. If only a method, method description, work plan, work-entry readiness, or performed-work claim is current, point directly to the A.3 or A.15 governing record instead of creating a linkage record.

`pathOrPathSliceRefs[]` does not make the structure a chain. A transformation-flow unfolding structure may branch, join, cycle, expose partial orders, or keep several guarded continuations live. A path slice is one selected traversal for explanation, comparison, or local review.

#### E.18.3:4.0a - Field Glosses

The record is a transformation-flow `U.Structure` specialization. Fields that point outside transformation-flow name adjacent governed loci; they do not transfer authority into E.18.3.

| Field | What this slot names | Not this | Direct exit when stronger claim is current |
| --- | --- | --- | --- |
| `unfoldingStructureRef` | the A.22.CGUS structure record or local CGUS block being specialized | not a route card or workflow title | `A.22.CGUS` for the generic structure |
| `transformedEntityOrConcernRef` | entity or concern whose transformation-flow unfolding is organized | not the carrier, diagram, or method description | direct pattern for that EntityOfConcern |
| `transformationLoci[]` | selected positions in the E.18 transformation-flow structure | not a performed sequence | `E.18` and `A.3.4` |
| `adjacentGovernedLoci[]` | method, work, evidence, architecture, publication, or refresh positions adjacent to the flow | not claims governed by E.18.3 itself | direct governing pattern for each adjacent locus |
| `transferOrDependencyRelations[]` | flow relations or dependencies among loci | not proof that a work order is feasible | `E.18`, `A.6.0`, `A.6.5`, or C.29 when a lens is current |
| `pathOrPathSliceRefs[]` | selected traversal or local slice through the flow | not the whole topology and not a project procedure | `DemonstrativeUnfoldingSlice@Context`, E.18, or A.15 family as current |
| `crossingRefs[]` | boundary-crossing positions in the selected flow | not gate passage | `A.20`, `A.21`, or E.18 crossing discipline |
| `guardRefs[]` | conditions that permit or block a continuation | not evidence or assurance by itself | `A.20`, `A.21`, `A.10`, or `B.3` as current |
| `flowValuationRef?` | valuation over the selected flow relation | not an architecture score or decision | E.18 valuation discipline; comparison or decision patterns when current |
| `methodWorkLinkageRef?` | optional A.15-owned relation record for method and work linkage | not work authorization | `A.15` and A.15 child patterns |
| `architectureUseRef?` | optional C.32.P2S or C.30.TFS-REL architecture-use relation | not architecture decision or description | `C.32.P2S`, `C.30`, `C.30.TFS-REL`, `C.32.PAD`, or `C.30.AD` |
| `preservedTransformationStructure` | transformation-flow structure kept by the unfolding use | not the complete structure in a source description, source-use record, or observed system | `C.33` or `C.34` when preservation adequacy is current |
| `lostOrHiddenTransformationStructure` | transformation-flow structure omitted, coarsened, or not recoverable | not a failure by itself | return to E.18, C.33, C.34, or the receiving governing pattern for omitted or coarsened structure |
| `nonAdmissibleOverreads` | blocked stronger readings for this flow use | not a catalogue of unrelated mistakes | direct pattern needed for the blocked claim |
| `returnToGoverningPatternCondition` | condition that sends the next claim to the direct pattern | not a local mini-ontology of reopening | receiving governing pattern named by value |
| `stopOrReopenCondition` | condition to stop at a description or reopen the smallest affected relation | not a `G.11` refresh unless currentness is the claim | `G.11` only for currentness or decay; direct governing pattern otherwise |

#### E.18.3:4.1 - Adjacent Locus Rule

An adjacent governed locus can be present in the unfolding structure, but its stronger claim remains outside this pattern.

| Adjacent locus | Present in E.18.3 as | Direct governing pattern for stronger claim |
| --- | --- | --- |
| Method selection or method relation | locus, dependency, or linkage ref | `A.3.1`, `A.3.2`, `B.1.5`, local method patterns |
| Work planning or work occurrence | locus, readiness dependency, or work linkage ref | A.15 family, especially `A.15.2`, `A.15.5`, `A.15.1` |
| Evidence, assurance, or gate | evidence or gate linkage ref, crossing, guard, or readiness condition | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` |
| Architecture use | architecture-use ref over the current transformation-flow structure when it is used inside an architecture claim | `C.30`, `C.30.TFS-REL`, `C.32.P2S`, `C.32.PAD` |
| Narrative or publication use | demonstrative slice, view, publication, or rendering ref | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Currentness or slice-local refresh | path-slice currentness or refresh trigger | `G.11` for currentness; `E.18` for slice-local flow refresh |

#### E.18.3:4.2 - Demonstrative Slice Rule

A path slice, flow card, worked example, replay, or first-use explanation is a `DemonstrativeUnfoldingSlice@Context` when it teaches or demonstrates an admissible traversal. It must state included loci, omitted branches, loop compression, traversal rule, and return condition when those affect use.

Do not infer that the demonstrated order is the project work order. If work order is current, open the work plan or method-description pattern.

Do not infer that the demonstrated path is the whole transformation-flow topology. If the underlying flow has branches, joins, cycles, alternatives, or partial orders, name what the slice omits or compresses before relying on it for comparison, architecture, evidence, or work planning.

A path slice or flow card can still be useful before work starts. Use it as a slot-filling scaffold: each visible step should either fill a transformation locus, crossing, guard, valuation, preserved/lost transformation-structure field, adjacent-governing-pattern exit, stop condition, or return condition, or else be rejected as a teaching-only position. This keeps attention on the objects being planned while the team is still discovering constraints. The slice is not ready to guide method, work, evidence, gate, architecture, or publication claims until the receiving direct governing pattern has admitted that claim.

#### E.18.3:4.3 - Boundary

This `U.Structure` specialization is not a second transformation ontology, workflow, method, work plan, performed work, mathematical graph, publication, evidence relation, gate decision, architecture decision, or architecture description. It is a transformation-flow structure over transformation loci plus the exit map to the direct patterns that govern those stronger claims.

### E.18.3:5 - Worked Slices

**P2W carry-through.** Accepted problem-side records may name distinctions, constraints, and unresolved loci that jointly guide the next FPF use. `E.18.3` can organize the transformation-flow structure among those records, candidate governing-pattern loci, and possible next uses such as pattern-use recommendations, method-selection frames, work-planning seeds, evaluation-refresh frames, or return-to-governing-pattern requests. It does not authorize launch or performed work.

**Transformation-flow mini-example.** A team has a flow card "admitted reference-publication edition changes -> recalculate comparison -> update candidate set -> decide whether to repair." E.18.3 admits only the transformation-flow slice:

```text
transformedEntityOrConcernRef: candidate-set comparison basis
transformationLoci[]: admitted reference-publication edition change; comparison recalculation; retained candidate-set update; repair-decision locus
adjacentGovernedLoci[]: G.2 source-use record or source pack; G.11 source-currentness relation; A.19 comparison relation; C.18 retained-set record; C.32.PAD decision-repair relation
transferOrDependencyRelations[]: comparison basis depends on the admitted reference-publication edition; retained candidate-set update depends on accepted comparison
pathOrPathSliceRefs[]: one teaching slice from edition change to repair decision
guardRefs[]: stop if the changed reference-publication edition is not admitted through the G.2 source-use record or source pack; return if comparison basis changes
preservedTransformationStructure: dependency from admitted reference-publication edition to comparison basis and retained-set update
lostOrHiddenTransformationStructure: alternative comparison branches not shown in the teaching slice
returnToGoverningPatternCondition: G.11 for currentness, A.19 for comparison, C.18 for retained set, C.32.PAD for decision repair
```

The flow card remains a demonstrative slice until those loci and exits are named.

**Architecture P2S projection.** A P2S flow card includes architecture-relevant problem pressure, selected or unknown structures, synthesis loci, and feedback. If a slice inside it is transformation-flow, `E.18.3` names that transformation-flow structure. The architecture use remains with `C.32.P2S` and `C.30.TFS-REL`; the decision remains with `C.32.PAD`.

**Reference-currentness repair.** A path slice relies on an admitted reference-publication edition, a `G.2` source-use record, a source pack, or a telemetry window. If the flow slice itself must be refreshed, E.18 keeps the slice-local refresh boundary. If the claim is source-currentness relation, decay, edition shift, deprecation, reship, or no-change, `G.11` governs it.

### E.18.3:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Path-as-workflow | Require transformed concern, transformation loci, guards, crossings, preserved and lost transformation structure, and direct work-pattern exit. |
| Graph-as-structure-in-every-sense | Treat graph expressions and path cards as descriptions or demonstrative slices unless the governed transformation-flow structure itself is named. |
| E.18 as universal CGUS parent | Admit E.18.3 only when bounded transformation-flow substrate is current. |
| Gate or evidence absorption | Keep gate and evidence claims with their direct governing patterns even when they appear as crossings, guards, or adjacent loci. |

### E.18.3:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-E18.3-1 Transformation substrate.** | Bounded transformations, transformation loci, and transformed concern are named. | Use `A.22.CGUS` or another direct pattern instead of E.18.3. |
| **CC-E18.3-2 Flow structure.** | Transfer or dependency relations, path or path-slice refs, crossings, guards, and optional valuation are recoverable. | Lower to a route card, graph description, or ordinary explanation. |
| **CC-E18.3-3 Adjacent locus boundary.** | Method, work, evidence, gate, architecture, publication, and refresh claims point to direct governing patterns. | Add direct exits or narrow the claim to the transformation-flow structure. |
| **CC-E18.3-4 Preserved and lost structure.** | Preserved and lost or hidden transformation structure are named. | Add them before using the structure for action, comparison, architecture, or publication. |
| **CC-E18.3-5 Stop or return.** | Stop, return, governing-pattern-specific repair, and currentness-refresh conditions are recoverable. | Add the condition or keep the slice as a one-use example. |
| **CC-E18.3-6 Non-chain topology.** | Branches, joins, cycles, partial orders, and guarded alternatives are preserved or explicitly lost when the flow is graph-shaped. | Treat any linear path as a demonstrative slice, not the whole flow structure. |

### E.18.3:8 - Common Anti-Patterns And Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **P2W as launch permission** | A carry-through note is used to begin work. | Add method, work-plan, work-entry, or gate record under the direct pattern before work is authorized. |
| **Flow card as architecture decision** | A P2S flow card is treated as the decision or ADR. | Keep flow structure in E.18.3 or C.32.P2S; use `C.32.PAD` and `C.32.ADR` for decision and ADR projection. |
| **Evidence path as evidence** | A path through evidence-looking boxes is treated as sufficient evidence. | Open `A.10`, `B.3`, or `G.6`; name the evidence relation and admissible use. |
| **Loop as improvement** | A retry loop in the flow is called quality improvement. | Use `E.23` only when object version, evaluation frame, repair, and re-evaluation are current. |

### E.18.3:9 - Consequences

This narrower `U.Structure` specialization lets E.18 keep its strength without swallowing every route-shaped pattern. P2W, P2S, agent-loop, gate, evidence, architecture, and refresh cases can share transformation-flow structure while each stronger claim remains governed by its direct pattern.

The cost is that a flow-shaped artifact must carry its boundary. If the artifact cannot name transformation loci, guards, crossings, preserved and lost structure, and direct exits, it remains a description or demonstrative slice rather than a governed transformation-flow unfolding structure.

### E.18.3:10 - Rationale

The selected design follows the same principle as E.18: transformation-flow structure is structure, not the whole work process. Constraint-governed unfolding adds a next-use concern. It asks how a transformation-flow structure can unfold toward a next FPF use while protecting the differences among structure, description, method, plan, work, evidence, gate, decision, architecture, publication, and refresh.

### E.18.3:11 - SoTA-Echoing

| Exact source or practice anchor | FPF adoption | Boundary |
| --- | --- | --- |
| OMG, *Case Management Model and Notation (CMMN) Version 1.1*, December 2016 | Adopt weakly structured case-work pressure for transformation-flow slices whose loci are constrained without one fixed work order. | E.18.3 does not import CMMN notation or make a case-management method. |
| Chiariello, Fionda, Ielo, and Ricca, "Direct Encoding of Declare Constraints in ASP", arXiv:2412.10152, 2024; Burattin, Maggi, and Sperduti, "Conformance Checking Based on Multi-Perspective Declarative Process Models", arXiv:1503.04957, 2015 | Adopt declarative constraints and multi-perspective loci as pressure for guards, crossings, and admissible path slices. | E.18.3 does not import Declare, MP-Declare, ASP, or conformance-checking ontology. |
| Hildebrandt and Mukkamala, "Declarative Event-Based Workflow as Distributed Dynamic Condition Response Graphs", EPTCS 69, 2011; Bagheri Hariri et al., "Verification of Semantically-Enhanced Artifact Systems", arXiv:1308.6292, 2013 | Use DCR and artifact-centric/GSM lineage as pressure for relation, condition, response, milestone, and artifact-state loci. | No DCR, GSM, database, or verification-method semantics are adopted as FPF ontology. |
| Modelica Association, *Modelica Language Specification* 3.6 (2023) and 3.7 (2026); JuliaHub, Dyad product page and Dyad documentation v3.0.0 | Adapt the relation-first pattern for model-related transformation-flow slices: component-model construction, connection checking, mode handling, and simulation setup can be organized before one calculation direction, compiler output, solver run, or simulation trace is selected. | E.18.3 governs only the transformation-flow slice that prepares, checks, or uses a model-related structure. It does not govern the physical model, solver semantics, compiler semantics, or AI-agent edit. |
| Ma, Gowda, Anantharaman, Laughman, Shah, and Rackauckas, "ModelingToolkit: A Composable Graph Transformation System For Equation-Based Modeling", arXiv:2103.05244; Rackauckas et al., "Composing Modeling and Simulation with Machine Learning in Julia", arXiv:2105.05946; Functional Mock-up Interface standard | Use these model-toolchain sources to separate symbolic model structure, graph transformations, calibration analyses, surrogate components, exchange packages, and result publications as adjacent loci or governed values in a transformation-flow slice. | E.18.3 does not prove mathematical adequacy, domain validity, evidence readiness, source-currentness relation, or publication truth. Those claims leave to `C.29`, domain DPF patterns, evidence patterns, `G.11`, or publication patterns. |
| Evolutionary architecture and work-control practice | Use local path slices, feedback, and refresh as bounded structure positions rather than one master process. | Architecture, work, evidence, and refresh claims stay with their direct patterns. |

### E.18.3:12 - Relations

Specializes: the `A.22.CGUS` use of `ConstraintGovernedUnfoldingStructure@Context` when the structure substrate is bounded transformation-flow structure with transformation loci, crossings, guards, valuations, preserved or lost transformation structure, and adjacent-governing-pattern exits.

Builds on: `E.18`, `A.3.4`, `A.22`, and `E.17` for transformation-flow structure and publication discipline.

Coordinates with: `E.18.1`, `C.32.P2S`, `C.30.TFS-REL`, `E.23`, `A.15`, `A.10`, `B.3`, `A.20`, `A.21`, `A.6.3.NAR`, and `G.11`.

Does not replace: direct method, work, evidence, gate, architecture, decision, publication, mathematical-lens, or refresh patterns.

### E.18.3:End


