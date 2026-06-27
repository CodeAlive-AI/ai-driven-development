## B.1.2 - System Aggregation and Holon Delimitation

> **Type:** Part B holonic construction pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### B.1.2:0 - Use This When

Use this pattern when a physical, operational, organizational, cyber-physical, or socio-technical system is treated as a whole made from parts, and the aggregation claim depends on how the system is delimited from its environment.

Typical moments:

- a machine, plant, robot, vehicle, building asset, service organization, or operating unit is aggregated from components or subholons;
- a system-level characteristic is rolled up from component characteristics;
- an external signal, supply, measurement, control, source, or publication relation is being mistaken for a part;
- a functional element must be allocated to candidate physical or organizational bearers;
- a boundary-interface-compatibility check is needed for a system aggregate.

**First useful move.** Name the candidate system whole, the candidate part relations, and the holon delimitation relation. Then decide which crossing relations remain external, which become internal after aggregation, and which are represented in a view or publication.

**What goes wrong if missed.** System aggregation becomes a drawing exercise. Ports, suppliers, documents, digital twins, dashboards, source records, and measuring instruments become components by placement. Functional parts become physical parts by label. External change or measurement is read as containment.

**What this buys.** B.1.2 makes system aggregation usable for engineering while keeping part-whole, holon delimitation, boundary crossing, functional structure, module allocation, and mathematical expression distinct.

**Not this pattern when.**

- If the object is not an admitted `U.System` or candidate system, use `A.1` first.
- If the question is generic part-whole vocabulary, use `A.14`.
- If the question is constructive grounding, use `C.13`.
- If the question is functional behavior or functional element, use `A.6.F` and architecture structural-view owners.
- If the question is module or bearer allocation, use `A.6.M` and architecture owners.
- If the question is a mathematical aggregation lens, use `C.29`.

### B.1.2:1 - Problem Frame

B.1.2 specializes B.1 for system holons. It keeps the useful engineering concerns from system-specific aggregation: physical plausibility, system delimitation, external crossing relations, component integration, whole-level characteristics, and boundary-interface compatibility.

It does not make `Gamma_sys` the pattern head. It does not create generic boundary or interaction U-kinds. It does not say that a system changing another holon becomes the changed holon's super-holon.

### B.1.2:2 - Problem

Without B.1.2:

1. **Boundary by drawing.** A box in a diagram is accepted as system delimitation.
2. **External relations become parts.** Suppliers, grids, sensors, controllers, teachers, measuring instruments, or digital twins are placed inside the system because they interact with it.
3. **Functional and physical structures collapse.** A resistor symbol, control function, chassis function, or service role is treated as a physical component by label.
4. **Whole-level characteristics lack grounding.** Mass, capacity, reliability, safety, throughput, assurance, or agency-like characteristics are rolled up without saying which part relations and scales are used.
5. **Transformation becomes containment.** A tool, teacher, actuator, script, or controller changes a holon and is then treated as that holon's containing whole.

### B.1.2:3 - Forces

| Force | Tension |
| --- | --- |
| Engineering concreteness vs broad FPF holon scope | System aggregation must be practical for systems without making all holons systems. |
| System delimitation vs external dependency | A system has a boundary in context, but many critical relations cross it. |
| Component structure vs functional structure | Physical or organizational bearers may realize multiple functions, and one function may require multiple bearers. |
| Conservative roll-up vs redundancy | Weakest-link and conservation checks are useful, but redundancy or substitution may require B.2 whole reidentification. |
| Description vs in-life system | Diagrams, BIM models, digital twins, and dashboards describe systems; they are not the system by appearance. |

### B.1.2:4 - Solution

Use B.1.2 to recover a system aggregation relation and its delimitation discipline.

#### B.1.2:4.1 - System Aggregation Relation

```text
SystemAggregationRelation@Context:
  candidateSystemWholeRef: U.System
  boundedContextRef:
  identityOrRecognitionRule:
  componentRelationRefs?
  portionRelationRefs?
  phaseRelationRefs?
  memberRelationRefs?
  holonDelimitationRelationRef:
  externalBoundaryCrossingRelationRefs?
  internalizedBoundaryCrossingRelationRefs?
  functionalElementRefs?
  moduleOrBearerAllocationRefs?
  wholeLevelCharacteristicRefs?
  constructionBasisRef?
  evidenceRelationRefs?
  mathLensOrRepresentationRef?
```

This relation is not a U-kind and not the system itself. It states which relations must be named before a system aggregation claim is relied on.

#### B.1.2:4.2 - Delimitation And Boundary-Crossing

Use `HolonDelimitationRelation@Context` for the current system delimitation: identity rule, included parts, excluded environment, selected structure, and context boundary conditions.

Use `HolonBoundaryCrossingRelation@Context` or a direct owner for relations that cross that delimitation: material flow, energy flow, signal, control, measurement, source use, publication use, evidence relation, transformation, probe relation, supply relation, commitment relation, A.6.C contract-language unpacking, or coupling.

Do not recast crossing relations as parthood merely because the relation is important.

#### B.1.2:4.3 - Boundary-Interface Compatibility Check

When a system aggregate exposes or hides crossing relations, record the compatibility choice:

```text
BoundaryInterfaceCompatibilityCheck@Context:
  systemAggregationRelationRef:
  crossingRelationRef:
  compatibilityDecision: expose | namespace | internalize | exclude | useDirectOwner
  ownerPatternRef:
  evidenceRelationRef?
```

This check is a system-aggregation aid, not a new ontology. It prevents silent loss of external obligations and unmanaged endpoint explosion.

#### B.1.2:4.4 - Whole-Level Characteristics

Roll up system-level characteristics only after the relation and scale are selected.

Useful families include:

- additive quantities such as mass, cost, energy stock, or material amount;
- limiting quantities such as pressure rating, weakest connector, safety class, or availability bottleneck;
- logical or capability claims such as emergency-stop availability or vulnerability exposure;
- architecture characteristics that depend on selected structure.

Use `C.16`, `A.19`, and `C.29` when characteristic space, scale, threshold, or mathematical lens is relied on for the current claim. Use B.2 when redundancy, closure, or coordination creates or reveals a whole that must be reidentified.

#### B.1.2:4.5 - Functional Elements And Bearers

A functional element in a functional view is not automatically a system part.

Recover separately:

- functional behavior or functional element under `A.6.F`;
- physical, organizational, software, or operational bearer under `A.6.M`, A.14, C.13, and architecture owners;
- allocation or correspondence between function and bearer;
- system aggregation only when bearer parthood is independently admitted.

One bearer may realize several functions. One function may require several bearers. This is allocation and correspondence before it is part-whole.

### B.1.2:5 - Archetypal Grounding (Worked Cases)

#### B.1.2:5.1 - Pump Skid

A pump skid is a candidate `U.System` whole. Pumps, frame, valves, controller, and connectors may be components after A.14 and C.13 admit the part-whole relation.

The power grid, maintenance crew, telemetry dashboard, and supplier are not skid components merely because the skid depends on them. They are external systems, epistemes, publications, or source-use objects connected through direct relations.

#### B.1.2:5.2 - Resistor In A Circuit

A resistor symbol in a circuit diagram is a functional or design-description element. The physical bearer may be a packaged resistor, a length of wire, a transistor region, or a module allocation. B.1.2 admits system aggregation only for the chosen physical or operational bearer relation, not for the symbol by label.

#### B.1.2:5.3 - Digital Twin Of A Building Asset

A BIM model, asset register, dashboard, or digital twin may describe the built asset and its systems. It is not the asset's part by being linked in a model. Use architecture-description, publication, evidence, source-use, and designation owners for the description side; use B.1.2 only for admitted system parts of the built asset.

#### B.1.2:5.4 - Lathe And Workpiece

The lathe can change the workpiece through a bounded transformation and work occurrence. That relation does not make the workpiece a lathe component, nor the lathe the workpiece's super-holon. Use A.3.4, A.15.1, A.12, and boundary-crossing owners before any part-whole claim.

### B.1.2:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Box as ontology | A diagram boundary becomes system delimitation by appearance. | Name identity rule, holon delimitation relation, and part relations. |
| Interface as part | Supply, signal, measurement, control, publication, or evidence relation becomes a component. | Keep boundary-crossing and direct-owner relations separate from parthood. |
| Function as bearer | A functional block or symbol is treated as a physical or organizational component. | Recover function, bearer, allocation, and system part-whole claims separately. |
| Description as system | BIM model, dashboard, digital twin, register, or source record is treated as the system. | Use description, publication, evidence, source-use, and designation owners for the description side. |
| Transformation as containment | A tool or teacher changes a holon and is read as that holon's super-holon. | Use A.3.4, A.15.1, A.12, and boundary-crossing owners before part-whole admission. |

### B.1.2:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-B1.2-1` | The candidate whole is an admitted `U.System` or candidate system under A.1. |
| `CC-B1.2-2` | System aggregation names bounded context, identity or recognition rule, part relation, and holon delimitation relation. |
| `CC-B1.2-3` | External supply, signal, control, measurement, source, publication, evidence, transformation, or coupling relations are kept as boundary-crossing or direct-owner relations unless parthood is separately admitted. |
| `CC-B1.2-4` | Functional elements and physical or organizational bearers are separated before allocation or parthood claims. |
| `CC-B1.2-5` | Whole-level characteristic roll-up names the characteristic, scale, relation owner, and mathematical lens when current. |
| `CC-B1.2-6` | A system changing another holon is not treated as that holon's super-holon by transformation, manufacturing, teaching, measurement, repair, or control relation alone. |
| `CC-B1.2-7` | Description artifacts, models, dashboards, digital twins, and registers are kept distinct from the system holon they describe. |

### B.1.2:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Box as boundary | A diagram rectangle determines system membership. | Name holon delimitation, identity rule, and part relations. |
| Supplier as component | External supplier or grid is treated as part of the system. | Use boundary-crossing relation, supply relation, commitment relation, A.6.C contract-language unpacking, evidence relation, or source-use relation. |
| Function block as module | A functional block is treated as a physical component. | Recover functional element, candidate bearer, and allocation relation separately. |
| Digital twin as part | Model or dashboard appears inside the system aggregate. | Use architecture-description, publication, evidence, or source-use owners. |
| Redundancy as arithmetic | Redundancy is averaged into a better system score. | Check characteristic scale and existing-whole explanation; use B.2 when the whole must be reidentified. |

### B.1.2:8 - Consequences

Positive consequences:

- System aggregation remains practical for engineering systems and organizations.
- Boundary and interface concerns become explicit relation work without false U-kinds.
- Functional architecture, module allocation, and physical parthood stop collapsing into one diagram.
- Digital-twin and publication artifacts stay on the description side unless another direct pattern admits a stronger relation.

Costs:

- Engineering diagrams need relation-owner annotations when used for decisions.
- Some familiar component lists must be split into physical parts, functional elements, external systems, sources, and descriptions.
- Whole-level characteristic claims need scale and relation discipline.

### B.1.2:9 - Rationale

System aggregation is the place where holonic thinking is most tempting and most useful. It is also where false parthood is easy: anything connected, measured, represented, or controlled can be drawn inside a system box.

B.1.2 preserves the engineering payoff while requiring holon delimitation, boundary-crossing relation discipline, and direct owners for function, module, characteristic, evidence, and publication claims.

### B.1.2:10 - SoTA-Echoing

| Source family | Current lesson for B.1.2 | FPF decision |
| --- | --- | --- |
| Systems engineering and digital engineering practice | System breakdowns, interfaces, allocations, views, and digital twins must be coordinated but not identified with one another. | B.1.2 separates system aggregation, functional view, bearer allocation, description, and publication claims. |
| Reliability and safety engineering | System-level claims need conservative relation and scale discipline. | Whole-level characteristic roll-up returns to C.16, A.19, and C.29 when those claims are relied on for the current use. |
| Applied ontology and constructional mereology | External dependence and part-whole construction are different relations. | Boundary-crossing relations do not become parthood without A.14 and C.13 admission. |
| Holonic and cyber-physical systems practice | Coordination and closure can create useful whole-level objects. | B.2 owns whole reidentification when existing system aggregation is insufficient. |

### B.1.2:11 - Relations

- **Builds on:** `B.1`, `A.1`, `A.14`, `C.13`, and `A.6.5`.
- **Coordinates with:** `A.6.F` for functional elements, `A.6.M` for module and bearer allocation, `A.22` and `C.30` for selected structure and architecture, `C.16` and `A.19` for characteristics, `C.29` for mathematical lenses, `A.3.4` and `A.12` for transformation and acting-side externalization, and `C.30.AD` or `C.30.AD.BA` for architecture-description cases.
- **Can contribute evidence to:** `B.2` when system aggregation no longer explains the whole-level claim and whole reidentification is needed.

### B.1.2:End

