## B.1.1 - Dependency Structure and Relation Grounding

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.1.1:0 - Use This When

Use this pattern when an aggregation, architecture, assurance, or construction claim depends on how candidate parts, members, phases, portions, or external relations depend on each other.

Typical moments:

- a dependency diagram is used to justify a whole-level claim;
- a graph mixes parthood, mapping, order, time, resource, and boundary-crossing relations;
- a project needs to know whether a relation is part-whole, dependence, representation, influence, source use, publication use, or evidence relation;
- a selected dependency structure will be expressed with a graph, table, matrix, or another mathematical or representation lens.

**First useful move.** Name the dependency relation under concern before choosing graph notation. Then decide whether the relation is part-whole, boundary crossing, order, temporal phase, resource relation, mapping, evidence, publication use, source use, or another directly governed relation.

**What goes wrong if missed.** A graph becomes the ontology; an edge named "depends on" carries many relation kinds at once; external influence becomes parthood; order and time are encoded as structure; and mathematical checks look precise while the relation being checked remains unclear.

**What this buys.** B.1.1 lets dependency material bear on B.1 aggregation without letting graph notation decide relation kinds.

**Not this pattern when.**

- If the current relation word is a mereology question, use `A.14`.
- If the current part-whole claim needs constructional grounding, use `C.13`.
- If the current object is architecture selected structure, use `A.22` and `C.30`.
- If the current expression is mathematical-lens choice, use `C.29`.
- If the current question is performed work, use `A.15.1`.

### B.1.1:1 - Problem Frame

B.1.1 separates dependency structure from graph representation.

A dependency structure can be ontology-side when a direct pattern has selected the relation under concern. A dependency graph is a mathematical or representation description of that selected relation structure. The graph may be useful, but it is not the holon, not the part-whole relation, and not the constructional grounding by itself.

### B.1.1:2 - Problem

Without B.1.1:

1. **Edge drift spreads.** `ComponentOf`, `MemberOf`, `PhaseOf`, `SerialStepOf`, `RepresentationOf`, source use, evidence relation, and control relation all become generic graph edges.
2. **Boundary crossing becomes parthood.** A power grid, supplier, teacher, measuring instrument, model, or source record is drawn as a part because it affects the holon.
3. **Design and run objects mix.** Planned structure, design description, actual work occurrence, and telemetry are placed in one dependency expression without a DesignRunTag or owner distinction.
4. **Acyclic graph discipline overclaims.** A graph check says something about the drawing, but the ontology-side relation remains ungrounded.
5. **Mappings become parts.** A digital twin, dashboard, diagram, or architecture description is treated as a constituent of the object it describes.

### B.1.1:3 - Forces

| Force | Tension |
| --- | --- |
| Visual clarity vs relation precision | Graphs make dependencies visible but tempt one-edge-fits-all modeling. |
| Part-whole locality vs external influence | External systems can influence, measure, transform, or supply a holon without becoming its parts. |
| Mathematical checks vs ontology-side grounding | Acyclicity, cutsets, reachability, and flow checks help only after relation kinds are selected. |
| Design view vs run evidence | Design-time dependency descriptions and run-time evidence often share labels but have different governed objects. |

### B.1.1:4 - Solution

Use dependency structure first; use graph representation second.

#### B.1.1:4.1 - Dependency Structure Frame

```text
DependencyStructure@Context:
  structureUnderConcernRef:
  boundedContextRef:
  candidateNodeRefs:
  dependencyRelationRefs:
  partWholeRelationRefs?
  boundaryCrossingRelationRefs?
  orderRelationRefs?
  temporalRelationRefs?
  resourceRelationRefs?
  representationRelationRefs?
  evidenceRelationRefs?
  publicationOrSourceUseRefs?
  designRunTag?
  directOwnerRefs:
```

This frame is not a U-kind. It records which relation claims are current and which direct owners govern them.

#### B.1.1:4.2 - Graph Representation

Use graph language only when a graph is the selected mathematical or representation lens:

```text
DependencyGraphRepresentation@Context:
  representedDependencyStructureRef:
  nodeExpression:
  edgeExpression:
  graphPropertyChecks?
  mathLensRef?
  publicationOrViewRef?
```

The graph may express acyclicity, reachability, cutsets, weak links, flow, or traceability. Those checks apply to the graph expression and bear on the selected relation only when the relation owner admits the mapping.

#### B.1.1:4.3 - Relation Grounding Guide

| If the edge means... | Recover... | Direct owner |
| --- | --- | --- |
| part of the whole | part-whole relation over admitted holons | `A.14`, `C.13`, `B.1` |
| member of a collection | membership or collection-as-whole claim | `A.14`, `C.13`, `C.16` |
| phase of the same carrier | temporal phase relation | `A.14`, temporal owner, `B.1.4` |
| ordered step or branch | method, process-view, or order relation | method owner, `B.1.4`, `C.29` when lens is current |
| performed work part | work occurrence relation with evidence and timing | `A.15.1` |
| external influence, signal, supply, measurement, or control | boundary-crossing relation or direct transformation, evidence, measurement, source-use, or control relation | `A.1`, `A.3.4`, `A.10`, `C.26`, or direct owner |
| representation, dashboard, digital twin, or architecture description | description or representation relation, not parthood | `C.2.1`, `E.17`, `C.30.AD`, `C.30.AD.BA` |

#### B.1.1:4.4 - Graph Checks Are Conditional

Acyclicity, topological order, cutset, reachability, and flow checks are useful only after the graph is selected as a lens over a selected relation structure.

Do not infer:

- parthood from graph adjacency;
- independence from graph separation without relation-owner admission;
- performed work from a planned step graph;
- whole reidentification from a graph property without B.2;
- architecture from a graph without selected-structure and architecture owners.

### B.1.1:5 - Archetypal Grounding (Worked Cases)

#### B.1.1:5.1 - Plant Supplier

Source graph: `PowerGrid -> Plant`.

If the edge means electricity supply, recover a boundary-crossing or supply relation. The power grid is not a plant part. Use part-whole relations only for admitted plant internals.

#### B.1.1:5.2 - Digital Twin

Source graph: `DigitalTwin -> Turbine`.

If the edge means representation, recover the architecture-description, publication, source-use, evidence, or digital-twin relation. The digital twin is not a turbine component by graph adjacency.

#### B.1.1:5.3 - Work Plan And Work Occurrence

Source graph: `Prep -> Weld -> Paint`.

If the graph describes a method or process view, use the method and order owners. If the graph describes performed work, use A.15.1 with occurrence identity, timing, evidence, and work-part relation. Do not let the same graph do both jobs.

### B.1.1:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Graph as ontology | A graph node or edge is treated as the in-life object or relation. | Recover the dependency structure and direct relation owners before graph expression. |
| One-edge-fits-all | `depends on` carries parthood, order, representation, source use, evidence, and influence at once. | Split relation kinds and assign direct owners. |
| External influence as parthood | Supply, measurement, teaching, source use, or control is drawn as a component relation. | Use boundary-crossing, evidence, source-use, publication-use, transformation, or direct relation owner. |
| Design-description and run-occurrence collapse | A planned dependency graph is treated as evidence of performed work. | Separate design description, work occurrence, and evidence relations. |

### B.1.1:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B1.1-1` | A dependency claim names the relation kind before graph notation is relied on. |
| `CC-B1.1-2` | Graph, matrix, table, or diagram wording is treated as mathematical or representation expression unless a direct owner selects it as the structure under concern. |
| `CC-B1.1-3` | Part-whole edges use A.14 and C.13 discipline. |
| `CC-B1.1-4` | Boundary-crossing, transformation, evidence, source-use, publication-use, and representation relations are not recast as parthood. |
| `CC-B1.1-5` | Design description, run occurrence, and evidence are not mixed without direct owners and DesignRunTag or equivalent scope discipline. |
| `CC-B1.1-6` | Graph checks are interpreted only through the selected relation owner and C.29 when the mathematical lens is relied on for the current claim. |

### B.1.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| DependencyGraph as ontology | The graph is treated as the thing being built. | Name the dependency structure and relation owners first. |
| External supplier as part | A supplier or infrastructure system is drawn inside the product. | Use a boundary-crossing relation, supply relation, commitment relation, A.6.C contract-language unpacking, evidence relation, publication-use relation, source-use relation, or another direct owner; use parthood only for admitted parts. |
| Mapping as parthood | A model, dashboard, or digital twin is a node inside the asset. | Use representation, publication, architecture-description, or evidence owners. |
| Order as component | A subsequent step is represented as a component of an earlier step. | Use order, method, or work occurrence owners. |
| Acyclicity as adequacy | The graph has no cycles, so the model is accepted. | Check whether the selected relation is grounded and whether graph checks answer the current concern. |

### B.1.1:8 - Consequences

Positive consequences:

- Dependency views become useful without becoming hidden ontology.
- External influences can be discussed without corrupting parthood.
- Graph checks keep their value and their limits.
- B.1 aggregation receives cleaner part-whole inputs.

Costs:

- A diagram alone is no longer enough; relation kinds and owners must be named.
- Some compact dependency graphs need multiple relation layers or views.
- Graph-based checks may need C.29 when the mathematical lens is relied on.

### B.1.1:9 - Rationale

Dependency language is useful exactly because it is broad. That breadth is also the danger. FPF keeps the breadth for recognition, then restores precision by separating relation kinds, selected structures, mathematical expressions, and publication forms.

B.1.1 therefore does not abolish dependency graphs. It makes them honest: a graph represents a selected relation structure; relation grounding comes from the direct owners.

### B.1.1:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Systems engineering dependency modeling | Dependency views are useful only when edge meaning is declared and traceable to the current engineering concern. |
| Graph theory and mathematical-lens practice | A graph property applies to the graph expression; it bears on the object only through an admitted mapping to the selected relation. |
| Applied ontology relation discipline | Part-whole, membership, representation, evidence, source-use, and influence relations have different admissibility conditions. |
| FPF design-description and run-occurrence distinction | A design dependency expression and a performed-work occurrence need separate owners and evidence. |

### B.1.1:11 - Relations

- **Builds on:** `B.1`, `A.1`, `A.14`, `C.13`, and `A.6.5`.
- **Coordinates with:** `A.15.1` for work occurrence, `B.1.4` for contextual and temporal aggregation, `C.29` for graph as mathematical lens, `A.22` and `C.30` for selected structure and architecture, `C.30.AD` and `C.30.AD.BA` for architecture description and digital-twin cases.
- **Can contribute evidence to:** `B.2` when dependency evidence bears on whole reidentification after existing-whole explanations fail.

### B.1.1:End

