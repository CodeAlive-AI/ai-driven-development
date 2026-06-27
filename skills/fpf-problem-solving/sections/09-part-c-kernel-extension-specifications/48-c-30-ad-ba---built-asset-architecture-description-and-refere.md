## C.30.AD.BA - Built-Asset Architecture Description and Reference Designation

> **Type:** Architecture-description subpattern under `C.30.AD`
> **Status:** Stable
> **Normativity:** Normative for built-asset architecture-description, asset-information, digital-twin, and reference-designation use.

**Builds on.** `C.30`, `C.30.AD`, `C.30.ASV`, `A.1`, `A.22`, `E.17`, `E.17.0`, `E.17.1`, `E.17.2`, `E.24.PUB`, and `A.7`.

**Coordinates with.** `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.29`, `C.16`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, `C.27`, and `F.18`.

**Use this when.** Use this pattern when a BIM model, IFC exchange, asset register, dashboard, digital-twin view, handover table, maintenance information set, cost or energy view, or ISO/IEC 81346-style reference designation is used as an architecture description for a built asset.

**Not this pattern when.** If the current question is the architecture claim itself, use `C.30`. If the current question is the general architecture-description mechanism, use `C.30.AD`. If the current question is one structural view, use `C.30.ASV`. If the current question is selected structure as such, use `A.22`. If the current claim is evidence, assurance, decision, causal use, work, or gate passage, keep this pattern only for the built-asset description boundary and use the direct governing pattern.

**What goes wrong if missed.** A BIM model, asset register, dashboard, digital-twin view, or reference designation starts acting as the built asset, architecture, evidence, assurance, gate, work, or decision.

**What this buys.** Built-asset descriptions remain usable while the asset, architecture claim, views, designations, publications, source relations, and currentness boundaries stay separate.

### C.30.AD.BA:1 - Problem Frame

Built-asset practice uses many useful descriptions: BIM models, IFC exchanges, asset-information models, COBie-like handover tables, reference-designation systems, dashboards, digital-twin views, maintenance records, energy views, cost views, and sensor feeds. These descriptions help engineers operate across design, construction, operation, maintenance, repair, refurbishment, and end-of-life use.

The danger is semio-bias. The description starts acting like the built asset, the architecture, the evidence, the assurance, the gate record, the work, or the decision because it is detailed, current, standardized, or tool-readable. `C.30.AD.BA` keeps the built asset, its architecture claim, its architecture description, its views, its reference designations, its publications, and its source relations separate.

### C.30.AD.BA:1.0 - Problem

Built-asset descriptions often carry enough structure to look like the built asset, enough designation discipline to look like identity, enough current data to look like evidence, and enough lifecycle coverage to look like authority. The problem is to admit BIM, IFC, asset-information, reference-designation, digital-twin, telemetry, maintenance, and handover material only after the described holon, architecture claim, selected structures, views, sources, publications, and admissible uses are explicit.

### C.30.AD.BA:1.1 - Forces

| Force | Tension |
| --- | --- |
| Tool-readable model vs built asset | BIM, IFC, asset registers, and digital twins can be detailed and current, but they remain descriptions or source relations. |
| Reference designation vs identity proof | Designation codes coordinate aspect-sensitive descriptions; they do not prove parthood, function, identity, evidence sufficiency, or assurance. |
| Lifecycle richness vs selected-structure recovery | Built-asset information crosses design, construction, operation, maintenance, refurbishment, and end-of-life use; each view still needs selected structure, source, and admissible-use boundaries. |
| Design material vs run material | Digital-twin and sensor-linked views can join design-side and run-side descriptions; the physical asset, work occurrence, telemetry, and description stay distinct. |
| Standards usefulness vs ontology import | Standards make exchange and designation practical; FPF adopts the relation discipline without importing a code-list ontology as FPF ontology. |

### C.30.AD.BA:2 - Solution

Use a `BuiltAssetArchitectureDescriptionUseCard@Project` for the first controlled slice:

```text
BuiltAssetArchitectureDescriptionUseCard@Project:
  architectureClaimRef: ArchitectureOf@ContextRef
  describedHolonRef:
  boundedContextRef:
  builtAssetKindCue:
    facility | plant | bridge | campusBuilding |
    infrastructureAsset | productAsset | otherDeclared
  selectedStructureRefs:
  structureKindRefs:
  architectureStructuralViewRefs:
  referenceDesignationRefs?
  assetInformationRefs?
  digitalTwinViewRefs?
  publicationOrExchangeRefs?
  correspondenceRefs?
  sourceReturnCondition?
  DesignRunTagRefs?
  admissibleUse:
  nonAdmissibleUse:
  firstNeighborPatternApplication?
```

`@Project` guard: in this card name, `@Project` marks a project-side use card for first-pass built-asset architecture-description triage. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

Expand to `BuiltAssetArchitectureDescription@Context` only when durable description use is current:

```text
BuiltAssetArchitectureDescription@Context:
  architectureDescriptionRef: ArchitectureDescription@ContextRef
  architectureClaimRef: ArchitectureOf@ContextRef
  describedBuiltAssetRef: U.HolonRef
  boundedContextRef: U.BoundedContextRef
  viewSetRefs:
  referenceDesignationSchemeRefs:
  assetInformationModelRefs:
  digitalTwinDescriptionRefs:
  exchangeOrPublicationRefs:
  sourceEpistemeRefs:
  correspondenceRefs:
  sourceReturnCondition:
  currentnessOrEditionBoundary:
  admissibleUse:
  nonAdmissibleUse:
```

`BuiltAssetArchitectureDescription@Context` is a specialization of `ArchitectureDescription@Context`. It is a Description episteme about `ArchitectureOf@Context`; it is not the built asset and not the architecture itself.

### C.30.AD.BA:3 - View and Relation Discipline

| Built-asset description material | Recover as | Neighboring owner |
| --- | --- | --- |
| BIM model or IFC exchange | Architecture-description publication or exchange over selected structures. | `C.30.AD`, `E.17`, `A.10` when source or evidence is claimed |
| Asset register or handover table | Asset-information description and source relation. | `C.30.AD.BA`, `E.17`, `A.10` |
| Reference designation | Aspect-sensitive designation relation over object identity and selected structure use. | `C.30.AD.BA`, `A.22`, `C.30.ASV` |
| Functional or MEP view | Functional structure or transformation-flow structure view. | `A.6.F`, `C.30.ASV`, `C.30.TFS-REL` |
| Module, equipment, or product structure view | Component, module, interface, or allocation relation. | `A.14`, `C.13`, `A.6.M`, `C.30.ASV` |
| Cost, schedule, operation, maintenance, sustainability, or energy view | Description view, characteristic view, or work-related source relation depending on the claim. | `C.16`, `A.10`, `A.15`, `C.27`, or `B.3` according to the recovered claim |
| Digital-twin view | Description or source relation connected to the physical asset and its current state claims. | `C.30.AD.BA`, `A.10`, `C.27`, `B.3` |

### C.30.AD.BA:4 - Reference Designation Boundary

A reference designation helps identify an object across aspect-sensitive descriptions. It does not prove that the functional object, product object, location object, property object, and activity-side object are one FPF entity in all uses. Recover the designation relation first:

```text
BuiltAssetReferenceDesignationUse@Context:
  designationRef:
  designationSchemeRef:
  designatedEntityRef:
  aspectOrViewRef:
  architectureClaimRef:
  selectedStructureRef?:
  correspondenceRefs?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse:
```

Use the designation to coordinate descriptions. Do not use the designation code as part-whole proof, function proof, evidence sufficiency, assurance, gate passage, or decision authority by appearance.

### C.30.AD.BA:5 - Digital Twin and Design-Run Boundary

A digital twin can describe, monitor, simulate, or forecast a built asset. It does not become the built asset by being connected to sensors or operations data.

Use `DesignRunTagRefs` when a description crosses design-side and run-side material. A design model, built asset, sensor relation, operation record, maintenance work, and physical transformation remain different objects unless a direct governing pattern relates them.

Example boundary: a lathe can transform a workpiece without becoming the workpiece's super-holon. Likewise, a building-management system can change equipment state without becoming part of that equipment merely because the dashboard shows both in one operational view. Use `HolonBoundaryCrossingRelation@Context`, `U.Transformation`, `U.Work`, evidence, source, and architecture-description relations before any MHT or part-whole claim is admitted.

### C.30.AD.BA:6 - Archetypal Grounding (Worked Slice)

A hospital facility has a BIM model, IFC exchange, asset register, fire-safety dashboard, energy view, maintenance records, and reference designations for rooms, systems, and equipment.

`C.30.AD.BA` records the built asset as described holon, the `ArchitectureOf@Context` claim, the selected structures being described, and the view set. The fire-safety view may involve control structure and evidence; the energy view may involve characteristics and current sensor claims; the asset register may carry source-return conditions; the reference designation coordinates object identity across aspect-sensitive views. None of these descriptions is treated as the hospital, the architecture, a safety proof, a gate record, or a work occurrence by appearance.

### C.30.AD.BA:6.1 - Bias-Annotation

| Bias | How C.30.AD.BA prevents it |
| --- | --- |
| Model-as-asset bias | The BIM model, IFC exchange, dashboard, or digital twin remains an architecture-description, source, publication, or view object, not the physical built asset. |
| Designation-as-identity bias | ISO/IEC 81346-style designation is treated as a designation relation with aspect and admissible-use boundaries, not as universal identity proof. |
| Currentness-as-assurance bias | Sensor freshness or model edition bounds use; evidence, assurance, gate, decision, and release claims keep their direct owners. |
| Design-run collapse | `DesignRunTagRefs` keep design-side model material, run-side telemetry, operation records, maintenance work, and physical transformations distinct. |
| Standard-as-ontology bias | Built-asset standards inform source and exchange discipline without importing their classifications as FPF U-kinds. |

### C.30.AD.BA:8 - Conformance Checklist

| ID | Check | Why it matters |
| --- | --- | --- |
| CC-BA-1 | The built asset or facility is named as `describedHolonRef`, and the architecture claim is named as `architectureClaimRef`. | Prevents description-as-asset and description-as-architecture collapse. |
| CC-BA-2 | Selected structures or structure kinds are named for each used view. | Prevents BIM or dashboard labels from replacing structure recovery. |
| CC-BA-3 | Reference designations name their scheme, designated entity, aspect or view, correspondence, and admissible use. | Prevents designation codes from becoming identity or parthood proof. |
| CC-BA-4 | Digital-twin, sensor, operation, and maintenance material carries source, currentness, and `DesignRunTag` boundaries when used across design and run material. | Prevents design-side and run-side objects from being silently merged. |
| CC-BA-5 | Evidence, assurance, gate, decision, work, and causal claims are returned to their governing patterns. | Keeps built-asset description useful without overclaiming authority. |

### C.30.AD.BA:8.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| BIM is the asset | A model or IFC exchange is treated as the building, plant, or facility itself. | Name the physical built asset as `describedHolonRef` and keep the model as description or publication material. |
| Designation code proves parthood | A designation prefix or aspect label is used as proof that one object is a part, function, product, or location of another. | Recover designation scheme, aspect or view, selected structure, correspondence, and admissible use. |
| Digital twin grants authority | Sensor-connected twin material is treated as evidence sufficiency, assurance, gate passage, or work completion. | Keep source/currentness boundaries and apply `A.10`, `B.3`, `A.21`, or work patterns for the authority claim. |
| Lifecycle view merge | Design model, as-built model, operation record, maintenance work, and physical transformation are merged because one dashboard shows them together. | Use `DesignRunTagRefs`, source relations, work refs, and transformation refs before admitting any identity, parthood, or MHT claim. |

### C.30.AD.BA:9 - Consequences

The gain is a practical bridge between FPF architecture-description discipline and current built-asset practice. Engineers can use BIM, IFC, asset-information, reference-designation, and digital-twin material without treating descriptions as the asset or as automatic proof.

The cost is extra relation recovery. The description must say which asset, architecture claim, selected structures, views, designations, sources, and admissible uses are live before it can guide architecture work.

### C.30.AD.BA:10 - Rationale

Built-asset engineering already relies on rich description systems. Their practical value comes from disciplined relation use: which asset is described, which architecture claim is current, which structures or views are being used, which source edition or run-side state is current, and which authority claim is actually being made.

The pattern specializes `C.30.AD` for built assets because BIM, IFC, asset-information, reference-designation, and digital-twin practice make the description/asset boundary especially easy to overread. It keeps standards and tools useful while preserving the FPF distinction between holon, architecture claim, description episteme, publication, source relation, evidence, work, and authority.

### C.30.AD.BA:10.1 - SoTA-Echoing

| Source family | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 architecture-description practice | Separates architecture of an entity from architecture description, views, viewpoints, and correspondence. | Adopt through `C.30.AD` and specialize here for built assets. | Keep built asset, architecture claim, description, view, and publication separate. |
| ISO 19650 information management for built assets | Treats information management across built-asset life as a serious engineering concern. | Adopt as practice discipline, not as FPF ontology. | Asset information needs source, edition, currentness, and admissible-use boundaries. |
| IFC / ISO 16739 and openBIM practice | Provides standardized digital descriptions of built assets, properties, and relations. | Use as exchange and description discipline. | Tool-readable structure is not evidence, assurance, gate passage, or architecture adequacy by itself. |
| ISO/IEC 81346 reference designation | Provides aspect-sensitive reference designation across object descriptions. | Adopt as designation discipline, not as a code-list ontology import. | A designation coordinates views; it does not prove parthood, function, or identity across every use. |
| Digital-twin practice for buildings and manufacturing | Connects BIM, asset metadata, sensors, maintenance, and operations descriptions. | Adopt as source and description discipline with `DesignRunTag` boundaries. | A digital twin may guide action, but the physical asset, description, telemetry, work, and evidence remain distinct. |

### C.30.AD.BA:11 - Relations

- **Specializes:** `C.30.AD` for built-asset architecture-description use.
- **Uses architecture and structure owners:** `C.30`, `C.30.ASV`, `A.1`, and `A.22`.
- **Uses description and publication owners:** `E.17`, `E.17.0`, `E.17.1`, `E.17.2`, `E.24.PUB`, and `A.7`.
- **Coordinates built-asset views with:** `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.29`, `C.16`, `C.27`, and `F.18`.
- **Returns authority claims to:** `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, and `C.28`.

### C.30.AD.BA:End

