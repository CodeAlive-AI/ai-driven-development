## C.30.AD.BA - Built-Asset Architecture Description and Reference Designation

> **Type:** Architecture-description subpattern under `C.30.AD`
> **Status:** Stable
> **Normativity:** Normative for built-asset architecture-description, reference-designation, model-exchange, and digital-twin use

**Builds on.** `C.30`, `C.30.AD`, `C.30.ASV`, `A.1`, `A.22`, `C.2.1`, `E.17.0`, `E.17`, `E.24.PUB`, and `A.7`.

**Coordinates with.** `A.6.P`, `A.6.RCD`, `A.6.REL`, `A.6.F`, `A.6.M`, `C.30.TFS-REL`, `C.30.LCA`, `C.29`, `C.16`, `C.27`, `C.27.TA`, `C.28`, `A.3.4`, `A.10`, `G.11`, `A.15`, `A.15.1`, `A.15.5`, `A.21`, `A.2.8.PER`, `A.2.9`, `B.3`, and `F.18`.

**Use this when.** Use this pattern when a BIM or IFC publication, asset-information description, reference designation, cost, schedule, operation, maintenance, sustainability, or energy view, or digital-twin description is being used to say something about the architecture of one exact built asset.

**What goes wrong if missed.** A rich model is treated as the asset or its architecture; a file or multi-view bundle is allowed to select structure or grant `U.View` membership; or a designation and a live data feed are asked to carry identity, occurrence, truth, and currentness claims that their direct relations do not establish.

**What this buys.** An engineer can use current built-asset information systems while keeping the physical asset, actual subject relations, exact selected structures, any obtaining `ArchitectureRelation`, bounded architecture claims, each description episteme, exact viewpoint conformance, each representation and publication object, each designation or reference relation, and each currentness claim inspectably connected but distinct.

**Not this pattern when.** Use `C.30` when the current object is the direct architecture relation or bounded architecture claim, `C.30.AD` when no built-asset specialization is needed, and `C.30.ASV` when one structural view is under repair. Use the direct designation/reference, evidence, currentness, Work, decision, transformation, or causal-use pattern when that relation rather than built-asset architecture-description use is current. When auxiliary-view, telemetry, simulation, maintenance, or digital-twin material is used to claim that an intervention caused an effect, handle that causal use under `C.28`; `C.27` remains the owner of temporal-claim adequacy. When a twin, dashboard, exchange result, or release screen looks like gate passage, recover whether a named gate decision is current. Use `A.21` when that gate must decide a bounded action or when its `GateDecisionResult` is being relied on; the display remains a cue until the required result is established. Return any separate evidence, work-entry readiness, assurance, Work, or other claim to its own governor. Do not collapse release into gate passage: route a release action or other performed Work to the exact `A.15.1` `U.Work` occurrence, work-entry readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a claim that a subject was released to its named subject predicate and participants; if that predicate cannot be recovered, return `A.6.RCD missing-governor`. An authorization-looking label does not choose among these claims.

### C.30.AD.BA:1 - Problem Frame

Built-asset work joins descriptions made for design, fabrication, construction, commissioning, operation, maintenance, adaptation, and decommissioning. A hospital, bridge, plant, railway corridor, or campus can therefore have a geometry model, spatial decomposition, functional and flow descriptions, product and equipment structures, cost and schedule descriptions, operation and maintenance records, sustainability and energy views, asset registers, live telemetry, inspection histories, and several reference-designation schemes.

These are not interchangeable descriptions of one undifferentiated object. They select different structures of the same built asset, or sometimes describe different entities related to that asset. The architect needs to recover which exact EntityOfConcern each description has, which A.22 structure each claimed view describes, how the views correspond, which designation or reference relation makes an entity retrievable, and what currentness boundary permits the description to guide the next architecture move.

### C.30.AD.BA:1.0 - Problem

How can an engineer assemble a usable built-asset architecture description from model exchanges, designation systems, and operational information without making the exchange schema, designation code, dashboard, or digital-twin system stand in for the built asset, an obtaining architecture relation, a selected structure, or a conforming view?

### C.30.AD.BA:1.1 - Forces

| Force | Tension |
| --- | --- |
| Long asset life vs changing descriptions | The built asset can retain identity while descriptions, model editions, sensor systems, representations, publications, and information uses change. |
| Many useful structures vs exact description identity | Spatial, functional, flow, module, interface, placement, control, and information structures can all matter, but every description still has one exact C.2.1 EntityOfConcern and every selected structure keeps its own A.22 identity. |
| Exchange interoperability vs FPF relation meaning | IFC and related exchange formats carry explicit object and relation data, but exchange content is source description until actual subject relations and selected structures are recovered under their subject patterns. |
| Designation stability vs aspect dependence | A reference designation can make an object retrievable across descriptions while still depending on a declared structuring aspect, designation scheme, exact referent, and qualification window. |
| Auxiliary-view usefulness vs direct claim ownership | Cost, schedule, operation, maintenance, sustainability, and energy views can guide architecture work; their characteristic measurement, Work, temporal-claim adequacy, causal use, evidence, assurance, and currentness claims still require `C.16`, `A.15.1`, `C.27`, `C.28`, `A.10`, `B.3`, and `G.11`. |
| Live coupling vs currentness | Telemetry and simulations can update a digital-twin description rapidly; freshness and fidelity still bound each claim made from it and do not create physical change. |

### C.30.AD.BA:2 - Solution

Start with one intended architecture use, not with the available tool outputs. Name the exact built asset and recover the actual subject-relation occurrences and exact selected A.22 structures that matter. Cite an obtaining `ArchitectureRelation` only when its C.30 predicate holds; otherwise keep required, desired, expected, candidate, negative, or unresolved content in a bounded `ArchitectureClaim`.

Constitute each architecture description under C.2.1 about exactly one EntityOfConcern: the built asset, one obtaining `ArchitectureRelation` occurrence, or one exact selected structure. Keep its exact ClaimGraph and effective `U.ReferenceScheme` recoverable. The same episteme is a `U.View` only while a separately identified E.17.0 conformance relation to one exact viewpoint episteme obtains. Then recover reference designation, model exchange, source use, representation, publication, and currentness through their own objects and relations.

For a first controlled use, record only the references needed to make the next architecture move:

```text
BuiltAssetArchitectureDescriptionUse@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  builtAssetDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact description-use or work-use pattern
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  descriptionClaimGraphRef: U.ClaimGraphRef
  descriptionEntityOfConcernRef:
    exactly one builtAssetRef |
      ArchitectureRelation occurrence ref |
      selected U.Structure ref
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  builtAssetRef: U.HolonRef
  architectureRelationOccurrenceRefs?: FinSet(U.RelationRef)
  architectureClaimRefs?: FinSet(U.EpistemeRef)
  selectedStructureRefs: FinSet(U.StructureRef)
  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  claimScope?: U.ClaimScope, byValue
  architectureConcernRefs?: FinSet(U.EpistemeRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)
  referenceDesignationRelationRefs?: FinSet(U.RelationRef)
  assetInformationDescriptionRefs?: FinSet(U.EpistemeRef)
  digitalTwinDescriptionRefs?: FinSet(U.EpistemeRef)
  designRunSeparationUse?: BuiltAssetDesignRunSeparationUse, byValue
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?:
  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef)
  descriptionFreshnessClaimRefs?: FinSet(U.EpistemeRef)
  publicationCurrentnessRelationRefs?: FinSet(U.RelationRef)
  admissibleUse:
  nextGoverningPatternApplicationRef:
  nonAdmissibleUse:
```

This is a project-side use record, not a description identity constructor or a new root kind. `@Project` is a compatibility and retrieval cue and establishes no project entity, Work occurrence, authority, context, viewpoint, parthood, or use relation. When the use is genuinely local to one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work`, and `builtAssetDescriptionProjectUseRelationRef` identifies the separately governed obtaining relation by which this description use concerns that Work. Otherwise both remain absent.

`architectureDescriptionRef` resolves to one exact C.2.1 episteme whose identity is the cited ClaimGraph, one exact `descriptionEntityOfConcernRef`, and effective reference scheme. If that EntityOfConcern is the built asset, it is exactly `builtAssetRef`. If it is an architecture-relation occurrence or selected structure, its exact participants or selection trace recover `builtAssetRef` without deriving identity from an optional architecture claim. `architectureClaimRefs` carry bounded claim content or trace only.

Every value in `architectureStructuralViewRefs` identifies an exact description episteme admitted as `U.View` only through an independently obtaining `EpistemeViewpointConformanceRelation` to one exact viewpoint. It can be the same episteme as `architectureDescriptionRef` only when that description's one EntityOfConcern is the selected structure required by C.30.ASV; otherwise it is a separately identified description episteme connected through an explicit description-set use or correspondence claim or independently obtaining relation. A multi-view use can cite several such description/view epistemes; the use record, collection, file, bundle, list order, or publication creates neither their identities nor their conformance.

`claimScope`, architecture concern, empirical grounding, and `modelUseStructureRef` remain neighboring qualifiers or relations. A DDD-style bounded-model-use structure appears only when that independently selected structure changes interpretation or selection for this use. It replaces none of the asset, relation, structure, description, scheme, scope, grounding, viewpoint, Work, or project-use objects and is absent from base identity.

Use `sourceToUsePathRefs` when a model publication, exchange, measurement description, or other named expression enters the present architecture use. Use a source-return condition only when stronger use of a derivative or reused description must return to that named source or governing pattern. Keep a diagram or model as representation, and keep publication occurrence, form, and carrier separate. Use `G.11` when description freshness, publication currentness, edition, telemetry freshness, model decay, or synchronization currentness is the claim; none establishes architecture adequacy or empirical grounding by itself.

When ISO 19650 discipline is invoked, cite the exact published part and edition rather than an unversioned series label. At the `2026-07-31` source check, ISO lists `ISO 19650-1:2018`, Edition 1, and `ISO 19650-3:2020`, Edition 1, as published editions last confirmed in 2024 and now to be revised, with draft successors under development. The current transfer is therefore exact and bounded: Part 1 contributes whole-life information-management discipline for exchanging, recording, versioning, and organizing information; Part 3 contributes the operational-phase management process and information exchanges. Record the exact standard source and edition in the source-to-use path, the used model or information edition, the reference date and validity window through the currentness loci, the refresh or source-return condition, and `admissibleUse` and `nonAdmissibleUse`. A draft or later edition does not silently replace the cited source. ISO 19650 practice contributes information-management discipline, not FPF ontology, subject-relation truth, architecture adequacy, evidence sufficiency, assurance, Work occurrence, or authority.

#### C.30.AD.BA:2.1 - Recover the selected structures before combining views

For every included view, state the exact candidate description episteme, its selected-structure EntityOfConcern, the architecture concern for which it is used, the exact viewpoint episteme, and the obtaining E.17.0 conformance occurrence. A geometry or coordination model can expose several structures, but the file boundary does not select one structure or grant view membership.

| Encountered description | First recover | Architecture-description use |
| --- | --- | --- |
| Spatial model | Spatial containment, placement, access, or separation structure under its direct relation pattern. | Cite the exact description episteme, selected structure, viewpoint, and conformance occurrence for the exact built asset. |
| Functional or flow model | Required or desired effect claims, functional structure, selected transformation-flow structure, ports, and interfaces under `A.6.F`, `E.18`, or `C.30.TFS-REL`; an actual transformation only under A.3.4. | Keep required content, selected flow organization, actual change, and the description/view use distinct; record correspondence or positive co-reference only when its direct predicate obtains. |
| Product or equipment model | Module claim or admitted module relation, component, interface, allocation, or placement relations under `A.6.M` and their subject patterns. | Keep the physical asset parts distinct from the description elements, representations, and publications that refer to them. |
| Control or operational model | Exact selected control structure under `C.30.LCA`, together with direct control, measurement, Work, and currentness relations. | Cite the control description/view without treating live values, a dashboard, or the LCA diagram as architecture adequacy or proof. |
| Cost, schedule, operation, maintenance, sustainability, or energy view | The exact description episteme and selected structure; then any measurement-result episteme for a claimed Characteristic under `C.16`, operation or maintenance Work under `A.15.1`, positive temporal aspect under `C.27.TA` or action-guiding temporal claim under `C.27`, causal use of an intervention, maintenance action, simulation, telemetry change, or claimed effect under `C.28`, and evidence, reliance, or assurance under `A.10` or `B.3`. | Keep the description or view, measured Characteristic, Work, temporal aspect or claim, causal-use question and verdict, currentness boundary, evidence, and assurance distinct; cite its source-to-use path and `G.11` validity or reopen condition. |

This last row is a distinct recognition-and-routing branch, not a new auxiliary-view kind and not a claim that every such description is an architecture structural view. Admit one as `U.View` only through the same exact selected-structure EntityOfConcern, viewpoint, and independently obtaining E.17.0 conformance required of every other view; return each embedded claim to the owner named in the row.

A single IFC publication may carry source descriptions for several rows. Conversely, one selected structure may be the EntityOfConcern of several descriptions and may be represented or published several times. `C.30.AD.BA` therefore keys each use to exact description identity, selected structure, view conformance, built-asset trace, and declared use rather than to a file, platform, package, or view count.

#### C.30.AD.BA:2.2 - Recover a reference designation as a relation

A reference designation is useful because it makes information about an entity retrievable under an explicit structuring and designation scheme. First recover the exact designation or reference relation through its direct representation/reference/naming owner. `C.30.AD.BA` records only its built-asset architecture-description use; a code, field, repeated string, list row, or the record below neither admits a relation kind nor makes an occurrence obtain. If no current subject pattern supplies the needed relation, keep the designation use as bounded C.2.1 claim content; apply `A.6.RCD` only when a named repeated receiving use genuinely needs a reusable predicate definition or admitted direct relation.

```text
BuiltAssetReferenceDesignationUse:
  designationValue: local designation value, byValue
  referenceDesignationScheme: U.ReferenceScheme, byValue
  designatedEntityRef: U.EntityRef
  selectedAspectStructureRef: U.StructureRef
  designationOrReferenceRelationRef?: U.RelationRef
  qualificationWindow:
  correspondingEntityRef?: U.EntityRef
  correspondenceClaimOrRelationRef?: U.EpistemeRef | U.RelationRef
  admissibleUse:
  nonAdmissibleUse:
```

`selectedAspectStructureRef` names the exact structure in which the designation is interpreted, such as a functional, product, location, or declared local structure. It is not a free aspect label. `designatedEntityRef` names the entity designated in that structure. Include `designationOrReferenceRelationRef` only when the designation or reference relation kind is admitted and the occurrence independently obtains. If a design object and a realized component both need to be retrieved, name the two entities and a bounded correspondence claim or independently obtaining correspondence relation rather than letting one code silently collapse them.

The designation use permits retrieval and cross-description coordination. Part-whole, function, location, identity across aspects, and evidence claims still come from their direct relations or claim owners. Repeated appearance of the same designation expression is insufficient to merge referents when the scheme, selected structure, local sense, or qualification window differs.

#### C.30.AD.BA:2.3 - Keep exchange checking distinct from architecture evaluation

An IFC exchange or another machine-readable model is a representation and publication of one or more epistemes. Its schema relations can preserve valuable source structure. Before using it as architecture-description content:

1. identify every source episteme used, its representation, and the publication occurrence, form, and carrier;
2. recover the exact actual subject-relation occurrences and A.22 selected structures represented by the relation data being used;
3. record the source-to-use path into the exact architecture description or view episteme;
4. state the admissible architecture use and any lost, inferred, unknown, stale, or unavailable relation content.

An exchange checker can use a computer-interpretable specification to evaluate whether declared information is present and shaped as specified. That evaluation concerns the exchange description or publication. It does not make schema relation data obtain in the built asset, constitute a selected structure, grant `U.View` membership, establish description truth, or show that the selected architecture is adequate for the asset's functions, constraints, or architectural characteristics. Apply the architecture, characteristic-evaluation, evidence, and assurance patterns for those claims.

#### C.30.AD.BA:2.4 - Keep a digital-twin description coupled without merging its objects

The phrase *digital twin* can cover a model episteme, software system, sensor systems, telemetry epistemes, simulation methods, operational Work, interfaces, representations, and publications. Recover each current object by its direct kind and relation. `C.30.AD.BA` uses only the exact descriptions and views that contribute to the built asset's architecture-description use.

When one declared architecture-description use crosses design-side and run-side material, fill the optional by-value record named by `designRunSeparationUse`:

```text
BuiltAssetDesignRunSeparationUse:
  designSideDescriptionRefs: FinSet(U.EpistemeRef)
  runSideDescriptionRefs: FinSet(U.EpistemeRef)
  designSideWorkOccurrenceRefs?: FinSet(U.EntityRef constrained to U.Work)
  runSideWorkOccurrenceRefs?: FinSet(U.EntityRef constrained to U.Work)
  telemetryEpistemeRefs?: FinSet(U.EpistemeRef)
  sourceToUsePathRefs: FinSet(U.RelationRef)
  descriptionFreshnessClaimRefs?: FinSet(U.EpistemeRef)
  publicationCurrentnessRelationRefs?: FinSet(U.RelationRef)
  designToRealizationCorrespondenceClaimOrRelationRefs?:
    FinSet(U.EpistemeRef | U.RelationRef)
  directCouplingRelationRefs?: FinSet(U.RelationRef)
  actualTransformationRefs?: FinSet(U.EntityRef constrained to U.Transformation)
  classificationBasis:
  admissibleCrossLifecycleUse:
  blockedMerge:
```

This is a by-value classifier for one built-asset description use, not a new FPF kind, a generic tag, or a relation constructor. `designSideDescriptionRefs` cite exact epistemes used for intended, required, proposed, or design-state material; `runSideDescriptionRefs` cite exact as-built, observed, operating, inspection, or maintenance-state epistemes. The classification is local to the declared use, not intrinsic to an episteme. If one publication carries both, identify the exact description or ClaimGraph loci before classifying them.

Every referenced object and relation keeps its subject pattern. C.2.1 governs description identity; `A.15.1` governs each exact `U.Work`; `G.11` governs freshness, currentness, and decay; the exact source-use owner governs each source path; the direct correspondence or coupling owner governs an affirmative relation; and `A.10` or `B.3` governs reliance or assurance. `C.28` governs a causal use of telemetry, simulation, maintenance, or a claimed physical or energy change; `C.27` continues to govern the temporal adequacy of the change statement. A.3.4 governs an actual physical transformation only when the exact changed referent, boundary, conditions, before/during/after facts, and continuity or reidentification basis are complete. A required or desired effect, live value, simulation result, control-view row, or local design/run classification is not that actual transformation. The local classification states only which already identified references belong on each side of this one cross-lifecycle use. Its nested source and currentness refs must resolve to the same exact refs cited by the enclosing use record, not duplicate or replace them. When an exact side, source path, Work occurrence, currentness boundary, or required direct relation cannot be recovered, state that gap in `blockedMerge` and narrow or block the cross-lifecycle use.

| Local anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Design/run collapse | A design description, realized asset description, telemetry episteme, operation or maintenance Work, and physical change are treated as one because a platform links or displays them together. | Fill `BuiltAssetDesignRunSeparationUse` with the exact side-specific descriptions, Work, sources, and currentness refs; cite correspondence, coupling, or transformation only under its subject pattern, or block the merged use. |
| Lifecycle view merge | Original design, as-built model, operation record, maintenance Work, and an alleged transformation are merged because one dashboard presents them as one lifecycle view. | Keep each existing object and relation reference explicit; actual change enters only through A.3.4, and identity, parthood, evidence, assurance, or architecture adequacy is never inferred from co-display. |

The twin's coupling to the asset establishes neither parthood nor identity between the digital and physical objects. Connection, synchronization, rendering, bundling, and publication also establish neither architecture relation, selected structure, description truth, empirical grounding, view membership, evidence sufficiency, assurance, gate passage, Work, nor project-use relation.

A green twin, dashboard, exchange result, or release screen is therefore a cue, not gate passage. Use `A.21` when a named gate must decide a bounded action or when its decision result is being relied on. Establish or recover the `GateDecisionResult` episteme, its applicable profile application and exact check-application results. Publication and the optional `DecisionLog` follow A.21:4.10 when publication, audit, or reuse is needed; an ordinary one-time decision can stop at its result and rationale. If no named gate decision is current, keep the display as a cue and handle any evidence, work-entry readiness, assurance, Work, or neighboring claim under `A.10`, `A.15.5`, `B.3`, `A.15.1`, or its exact direct governor. Even a `GateDecisionResult` with `decisionValue=pass` establishes neither release, readiness, permission, authorization, nor performed Work.

Recover the release-looking claim before routing it. An actual release action is one exact `A.15.1` `U.Work` occurrence. Use `A.15.5` for work-entry readiness, `A.2.8.PER` for a non-prohibition, granted permission, permission exercise, non-violation, or permission conflict, and `A.2.9` for an instituting or revoking grant act. A further claim that a subject was released needs its named subject predicate and participants. Keep the display as a cue while either is unresolved; return `A.6.RCD missing-governor` only when the predicate cannot be recovered, and state any missing participant information separately. No current model, source, gate result, dashboard, or the word *authorized* supplies one of these relations by appearance.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the built-asset description-use locus and conclusion that depend on it. A changed asset or selected structure reopens the dependent description identity, built-asset trace, or structural-view use; changed view conformance reopens that one view admission; a changed designation scheme, referent, or qualification window reopens only its `BuiltAssetReferenceDesignationUse`; a changed source, model, publication, or telemetry edition or freshness/fidelity boundary reopens its exact source-to-use or currentness locus; changed design/run classification, cited Work, source/currentness ref, correspondence, coupling, or transformation reopens only the affected `BuiltAssetDesignRunSeparationUse` and dependent admissible cross-lifecycle use; and a changed project-use relation or direct governor reopens only that exact relation reference and dependent admissible-use conclusion. Update the affected description, designation, design/run, or currentness locus; when the required input cannot be recovered, narrow or block only that use while unrelated views, descriptions, designations, and uses stay closed.

### C.30.AD.BA:3 - Worked Cases

#### C.30.AD.BA:3.1 - Hospital ventilation and fire compartmentation

A hospital renovation uses an IFC publication, a fire-compartment view, a ventilation flow view, an equipment register, an energy-use view, and live air-handling telemetry. The immediate architecture concern is whether the changed ventilation arrangement preserves smoke-control functions across compartment boundaries. A second intended use is a bounded comparison of air-handling energy consumption; it does not share the smoke-control verdict.

The engineer names the hospital facility as `builtAssetRef`, recovers the actual subject relations and exact fire-compartment, ventilation-flow, equipment-module, and control structures, and cites an obtaining `ArchitectureRelation` only if its C.30 predicate holds. Required or proposed content remains in a bounded architecture claim. Each used architecture description has its exact ClaimGraph, one EntityOfConcern, and effective reference scheme; each claimed structural view additionally has an exact viewpoint and independently obtaining E.17.0 conformance relation.

The IFC publication supplies a source-to-use path for the spatial and equipment descriptions while its representation, publication occurrence, form, and carrier stay separate. The telemetry episteme has a currentness boundary and can support separately governed operating-state claims; it is not itself the control structure, an architecture relation, an actual physical transformation, or architecture evaluation.

For the energy use, one current `C.16` measurement-result episteme attributes `112 kWh ± 4 kWh` electrical-energy consumption to air-handling unit `AHU-3` over a declared 24-hour commissioning window. It names the exact measurand, Characteristic, Scale and unit, method and model, calibration basis, dated measurement Work, time stance, and uncertainty. Its source-to-use path cites the meter telemetry and source edition; its `G.11` currentness condition limits use to the named sensor, calibration, model editions, and validity window and reopens that use when one changes. If the engineer claims that the control revision will reduce the daily consumption rate, the action-guiding temporal claim enters `C.27` with the intervention, window, resistance or cost, evidence or assumption relation, supported use, unsupported use, and reopen condition. If that same statement is used to say that the control revision causes the reduction, and causal support makes publication, choice, deployment, assurance, audit, benchmark, or support treatment admissible, `C.28` additionally governs the causal-use class, support basis, supported use, unsupported use, and verdict. `C.27` temporal adequacy does not establish a causal intervention effect, and `C.28` does not replace the `C.16` measurement result, `C.27` temporal claim, or `G.11` currentness boundary. `A.10` and `B.3` still govern material reliance and assurance. Neither the energy view nor the recent reading proves sustainability, smoke-control adequacy, or architecture adequacy.

An air-handling unit has a product-aspect designation and a location-aspect designation. Each designation use names its scheme, selected structure, designated entity, qualification window, and exact direct relation when one obtains. A bounded correspondence claim or obtaining correspondence relation lets the maintenance team retrieve both descriptions without making the product structure identical to the location structure.

The next architecture move is then concrete: evaluate the proposed flow and control structures against the smoke-control concern and carry the bounded energy-use comparison through its own characteristic and temporal owners. It is not “approve the BIM model.”

#### C.30.AD.BA:3.2 - Bridge inspection twin

A bridge operator combines an as-maintained geometry model, structural-member view, inspection history, strain telemetry, and a simulation view. The bridge remains the built asset across model editions. The structural-member and sensor-placement structures are selected explicitly; each description keeps exact C.2.1 identity and each claimed view exact E.17.0 conformance. Inspection and telemetry claims retain their evidence, grounding, source-use, and currentness relations. A revised simulation model retains the same C.2.1 episteme identity when its claim content, EntityOfConcern, and effective reference scheme are unchanged. Otherwise identify another episteme; assert an `EpistemeEditionRelation` only when its historical-continuation predicate obtains. Assess any declared lineage or continuity claims separately for the intended reuse.

When the operator compares an original design description with the as-maintained geometry, inspection history, and live telemetry, `designRunSeparationUse` cites the exact design-side description and design Work, the exact run-side descriptions and inspection or maintenance Work, their source-to-use and currentness refs, and any separately governed design-to-realization correspondence. `actualTransformationRefs` remains absent unless an exact repair or other physical change satisfies A.3.4. The architecture description can therefore support a decision to inspect or redesign a connection while retaining the route back to the geometry publication, measurement descriptions, and selected structures. It cannot treat a successful data-exchange check, recent sensor sample, simulation result, polished dashboard, or local design/run classification as proof that the bridge architecture is adequate or that design and realized objects are identical.

### C.30.AD.BA:4 - Conformance Checklist

| ID | Check | Repair when absent |
| --- | --- | --- |
| `BA-1` | The exact built asset is recoverable, and every used architecture description has one exact ClaimGraph, one EntityOfConcern—built asset, obtaining `ArchitectureRelation`, or selected structure—and effective `U.ReferenceScheme`. | Recover the asset under `A.1`, subject relations and architecture relation under `C.30`, selected structure under `A.22`, and description identity under C.2.1; do not derive the subject from an optional architecture-claim field. |
| `BA-2` | Every asserted architecture structural view is the same exact description episteme whose selected-structure EntityOfConcern, structure kind, exact viewpoint, and independently obtaining E.17.0 conformance relation are named. | Apply `A.22`, `E.17.0`, and `C.30.ASV`; do not use the file, bundle, dashboard, representation, publication, or current use as the structure or view constructor. |
| `BA-3` | Every relied-on designation names its scheme, designated entity, selected aspect structure, qualification window, and exact designation/reference relation when one is claimed; design/realization correspondence remains a separate claim or relation. | Recover the direct designation/reference owner and occurrence, or keep a bounded designation-use claim; never use repeated spelling as entity identity or parthood proof. |
| `BA-4` | Exchange checking and architecture evaluation have different evaluated objects and governors; source episteme, representation, publication occurrence, form, carrier, actual subject relations, selected structures, and descriptions remain distinct. | Keep description conformance with the exchange use; return relation truth, architecture adequacy, evidence, and assurance to their direct patterns. |
| `BA-5` | Reused or live descriptions name source-to-use, source-return when stronger use needs it, description freshness, and publication-currentness objects appropriate to the exact claim. | Apply `G.11`; do not turn freshness, synchronization, recent publication, or live data into grounding, truth, evidence sufficiency, or architecture adequacy. |
| `BA-6` | Digital and physical objects retain direct kinds, identities, coupling relations, Work, and transformations; actual change is cited only with the full A.3.4 basis. Project-local use additionally names both exact composite Work and the obtaining project-use relation. | Recover model, systems, epistemes, the exact composite `U.Work`, interfaces, coupling, actual changed referent and facts, and `builtAssetDescriptionProjectUseRelationRef` as the separately governed obtaining relation by which this description use concerns that Work before making identity, parthood, transformation, or project-locality claims. |
| `BA-7` | Every used cost, schedule, operation, maintenance, sustainability, or energy view names exact description identity and, when asserted as a structural view, selected structure, viewpoint, and conformance; its characteristic, Work, temporal, causal-use, evidence, assurance, and currentness claims keep exact subject patterns. | Use `C.16` for the measurement result, `A.15.1` for Work, `C.27.TA` or `C.27` for the exact temporal use, `C.28` only when the view, telemetry, simulation, maintenance action, or claimed change is used causally, `A.10` or `B.3` for reliance or assurance, and `G.11` for currentness; do not let the auxiliary view itself establish a causal effect, sustainability, acceptance, evidence, assurance, or architecture adequacy. |
| `BA-8` | Every ISO 19650-based use names the exact part and edition, exact source-to-use path, used information or model edition, source-status reference date, validity window, refresh or source-return condition, and admissible and non-admissible use. | Pin the exact published edition used; reopen this source-use locus when ISO status, the cited edition, information edition, or intended use changes. Do not silently substitute a draft or successor edition or import standard terminology as FPF ontology or authority. |
| `BA-9` | Every declared use that crosses design-side and run-side material fills one `BuiltAssetDesignRunSeparationUse` with exact side-specific descriptions, Work when current, source and currentness refs, classification basis, admissible cross-lifecycle use, and blocked merge; correspondence, coupling, and transformation refs appear only when their direct predicates obtain. | Fill the local record from already governed refs, or narrow or block the cross-lifecycle use. Do not restore a generic tag, infer identity or parthood from co-display, or treat telemetry, Work, correspondence, coupling, or a proposed effect as actual A.3.4 change. |
| `BA-10` | A green twin, dashboard, exchange result, or release screen remains a cue until the required `A.21` `GateDecisionResult` is established for a named gate decision; gate decision, release action, work-entry readiness, permission or grant act, performed Work, and a subject-release predicate remain distinct claims. | When a named gate decision is current, establish or recover its `GateDecisionResult`, applicable profile application and exact check-application results; use publication and the optional `DecisionLog` under A.21:4.10 only when those uses are current. Route a release action or other performed Work to its exact `A.15.1` occurrence, readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a subject-release claim to its named predicate and participants or `A.6.RCD missing-governor`; none is entailed by freshness, evidence, assurance, the display, or a `GateDecisionResult` with `decisionValue=pass`. |

### C.30.AD.BA:5 - Consequences

Assembling multi-view built-asset descriptions takes additional work because the engineer must recover the objects and relations represented in the tool's outputs. That cost is local and reviewable: each description gains exact C.2.1 identity; each asserted view gains an exact selected structure, viewpoint, and conformance relation; each designation use gains an exact referent, scheme, aspect structure, qualification window, and direct-relation disposition; and each live description gains an explicit currentness boundary.

The gain is stronger reuse. A changed model edition, replacement sensor system, revised designation scheme, new representation, or new publication can be incorporated without changing the built asset's identity, inventing an architecture occurrence, or silently reidentifying a description. Architecture evaluation can use the description while remaining distinct from exchange checking, information currentness, evidence sufficiency, assurance, Work, and project locality.

### C.30.AD.BA:6 - Rationale

Built-asset practice is unusually exposed to semio-bias because one information environment often spans geometry, equipment, Work, sensor state, and maintenance history. The repair is a constructive chain from the physical asset and independently obtaining subject relations to exact selected A.22 structures, any actual `ArchitectureRelation`, bounded architecture claims, exact C.2.1 description epistemes, independently conforming views, and the source, representation, publication, designation, grounding, currentness, Work, and project-use relations that make those descriptions usable.

Reference designation demonstrates why this chain matters. Its engineering value is retrieval across heterogeneous descriptions. That value depends on the scheme, selected aspect structure, referent, qualification window, and exact direct-relation disposition being explicit. Treating the code as universal identity would remove precisely the aspect discipline that makes the designation useful.

### C.30.AD.BA:7 - SoTA-Echoing

| Source line | Contribution used here | Mutation of the pattern | Practitioner implication |
| --- | --- | --- | --- |
| [ISO 19650-1:2018, Part 1: Concepts and principles](https://www.iso.org/standard/68078.html) and [ISO 19650-3:2020, Part 3: Operational phase of the assets](https://www.iso.org/standard/75109.html), official status checked `2026-07-31` | ISO 19650-1 contributes information-management concepts and principles for exchanging, recording, versioning, and organizing information across the whole built-asset life; ISO 19650-3 specifies information-management process and exchanges in the operational phase. Both cited editions are published, were last confirmed in 2024, and are marked by ISO as to be revised with draft successors under development. | Adopt the exact whole-life and operational information-management discipline through source-to-use, edition, currentness, refresh, and admissible-use boundaries; do not import ISO terms as FPF U-kinds, relation truth, architecture adequacy, or authority. | Cite the exact part and edition, used information or model edition, reference date, validity window, source-return or refresh condition, and admissible and non-admissible use; a draft or later edition never updates an existing use silently. |
| [buildingSMART IFC 4.3.2 official documentation](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/) | Current IFC exposes explicit object identities, relationship entities, decomposition, systems, processes, products, and aspect-specific schemas. | IFC content enters through exact source epistemes, representations, publication objects, and source-to-use paths; relation data must be checked against actual subject relations before selecting FPF structures. | Preserve useful machine-readable relation content without making an exchange schema, file, representation, or publication the built asset, relation truth, or FPF ontology. |
| [buildingSMART IDS 1.0](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/) | An IDS 1.0 specification states expected IFC information in a computer-interpretable form for an exchange checker to test. | `C.30.AD.BA:2.3` separates exchange-description checking from architecture evaluation and world-side relation truth. | Passing an IDS check shows that declared information was delivered; it does not show that the architecture is adequate or that described relations obtain. |
| [IEC 81346-1:2022](https://webstore.iec.ch/en/publication/64021) | Current reference-designation practice connects unambiguous retrieval to system structuring, aspects, objects, corresponding components, and relations between objects. | The pattern uses an explicit scheme-expression-entity-structure use record, an exact direct designation/reference relation when one obtains, and a separate correspondence claim or relation when design object and realized component both matter. | A stable code remains useful across descriptions without becoming universal identity, parthood proof, or an occurrence constructor. |
| [Digital Twin Consortium AECO working-group priorities](https://www.digitaltwinconsortium.org/working-groups/aeco/) | The AECO working group's stated priorities cover model fidelity, interoperability, interactions between physical and digital components, lifecycle use, and synchronization. | `C.30.AD.BA:2.4` assigns model, system, telemetry, simulation, Work, transformation, representation, publication, and currentness to their direct governors; when one use crosses design and run, `BuiltAssetDesignRunSeparationUse` classifies only exact existing refs on the two sides. | Select the fidelity and freshness needed for the architecture use, fill the local design/run record only when the boundary is current, and never treat connection, co-display, or the local classification as architecture adequacy, identity, parthood, or actual change. |
| FPF `A.1`, `A.22`, `C.30`, `C.30.AD`, `E.17.0`, and `C.30.ASV` | Holon identity, selected structure, direct architecture relation, bounded claim, description episteme, viewpoint, and structural-view conformance already have separate subject patterns. | This pattern specializes their use for built assets rather than importing a built-environment upper ontology or a second description/view identity. | The same method works for a building, plant, bridge, transport asset, or another engineered built holon. |

### C.30.AD.BA:8 - Relations

- **Specializes:** `C.30.AD` for built-asset architecture-description use.
- **Uses architecture and structure patterns:** `C.30`, `C.30.ASV`, `A.22`, `A.6.F`, `A.6.M`, `C.30.TFS-REL`, and `C.30.LCA`.
- **Uses description, view, representation, and publication patterns:** `C.2.1`, `A.7`, `E.17.0`, `E.17`, `E.24.PUB`, and `C.29`.
- **Uses relation, naming, and currentness patterns:** the exact designation/reference predicate and assertion; `A.6.P` for precision repair; `A.6.RCD` only for a demonstrated missing reusable predicate; `A.6.REL` only after the relation kind is admitted, current facts satisfy its obtaining predicate, and occurrence identity matters; `F.18`; and `G.11`.
- **Uses lifecycle information-management source discipline from:** exact published `ISO 19650-1:2018` and `ISO 19650-3:2020` editions through source-to-use, edition, currentness, source-return, and admissible-use boundaries, without ontology or authority import.
- **Records design/run separation in:** one local `BuiltAssetDesignRunSeparationUse` over exact C.2.1 descriptions, `A.15.1` Work, source-use paths, `G.11` currentness, directly governed correspondence or coupling, and A.3.4 transformation refs; the local classification admits no kind or relation.
- **Use for auxiliary-view claims:** `C.16` for characteristic measurement, `A.15.1` for operation or maintenance Work, `C.27.TA` for positive temporal aspects, `C.27` for action-guiding temporal-claim adequacy, `C.28` when an intervention, maintenance action, simulation, telemetry change, or claimed effect is used causally, `A.10` for evidence or material reliance, `B.3` for assurance, and `G.11` for currentness and reopen conditions.
- **Use for gate- and release-looking claims:** `A.21` when a named gate must decide a bounded action or its `GateDecisionResult` is being relied on; the display remains a cue until the required result is established. Route a release action or other performed Work to `A.15.1`, work-entry readiness to `A.15.5`, a permission result or exercise to `A.2.8.PER`, an instituting or revoking grant act to `A.2.9`, and a subject-release claim to its named predicate and participants or `A.6.RCD missing-governor`; none of these claims entails another.
- **Use for other claims:** `A.3.4` and the direct transformation, evaluation, evidence, assurance, Work, decision, acceptance, or project-use pattern named by the claim.

### C.30.AD.BA:End

