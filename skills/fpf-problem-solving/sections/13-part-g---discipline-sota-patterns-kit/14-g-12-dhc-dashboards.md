## G.12 — DHC Dashboards (Discipline-Health Time Series and Views)

**Tag:** Architectural kit pattern; notation-independent.

**Stage:** optional series authoring → measurement and series-update Work → representation → optional publication and refresh.

**Primary hooks:** C.21 for discipline-health Characteristics and the common replay basis; C.16 for measurement; C.2.1 for result and series epistemes; C.29 for representations; E.24.PUB for publication availability; G.6 for evidence paths when relied on; G.11 for refresh; G.Core, A.19, and G.0 for the exact legality and comparison surfaces actually used.

**Optional hooks:** G.2 for SoTA palettes, G.5 for selector results, C.18 and C.19 for QD or open-ended telemetry, G.8 for maturity views, G.10 for shipping, F.18 when public names are needed, and F.9 only for actual distinct-local-sense comparison.

### G.12:0 — Use This When

Use G.12 when a team needs several recorded C.21 coordinate results arranged across windows, a dashboard view over them, or refresh wiring for that view.

Start from the C.21 results, not from a screen layout. State the discipline, intended use, ClaimScope, coordinate-result refs, and windows. Stop with a local view when no audience publication or refresh use exists.

Do not use G.12 for one ordinary field-health claim, to manufacture measurements from rows, to turn a dashboard into evidence or authority, or to require publication and telemetry for every C.21 use.

### G.12:1 — Intent

Produce a reproducible discipline-health series and view while keeping five objects separate:

1. C.16 measurement results and their C.2.1 coordinate-result epistemes;
2. one optional C.2.1 `DHCSeries` episteme that orders exact result refs by window;
3. rows and slices that represent those results or series;
4. any E.24.PUB publication occurrence, form, carrier, audience, and availability interval; and
5. any measurement, series-assembly, rendering, upload, or refresh Work.

### G.12:2 — Problem Frame

Dashboards drift or become misleading when they:

* treat `ClaimScope` and a selected `TargetSlice` as one field;
* copy a value without its C.21 replay basis;
* average nominal or ordinal values or mix Units;
* hide normalization, distance, comparison, or target-band rules;
* require a Bridge for every source difference or omit F.9 when distinct local senses are actually related;
* turn a row, screenshot, UTS name, form, or carrier into the measurement or series episteme;
* turn selected sets or archives into one scalar winner; or
* rebuild everything because changed definition and evidence pins cannot be localized.

### G.12:3 — Forces

| Force | Tension |
| --- | --- |
| Readable view vs replay | A useful dashboard should be easy to read, while every relied-on coordinate must return to its exact definition and result. |
| Stable history vs changed definitions | A new method or Scale edition may invalidate trend comparability without changing historical results. |
| Optional publication vs local use | A local view may be enough; audience availability adds a separate publication relation. |
| Selective refresh vs process burden | Refresh needs actionable pins, but a one-off view needs no telemetry framework. |
| Set-valued results vs headline pressure | A view can summarize without manufacturing a scalar winner. |

### G.12:4 — Solution

#### G.12:4.0 — G.Core linkage

This pattern consumes G.Core obligations only for the branches actually opened.

**GCoreLinkageManifest (G.12)**

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }.
* `RSCRTriggerSetIds` := {`GCoreTriggerSetId.BridgeCalibrationKit`} only when crossing or refresh wiring is used.
* `RSCRTriggerKindIds` := {`RSCRTriggerKindId.LegalitySurfaceEdit`} only when a persisted series or view depends on that surface. Optional panels add only their own declared trigger kinds.
* `DefaultsConsumed` := `∅`; portfolio defaults become current only through `G.12:Ext.PortfolioTelemetry`.
* `CorePinSetIds` := {`GCorePinSetId.PartG.AuthoringMinimal`, `GCorePinSetId.PartG.CrossingVisibilityPins`} with nil-elision.

The minimal durable series basis is `DHCSeriesRef.edition`, `DisciplineRef`, `IntendedUse`, `ClaimScopeRef`, exact coordinate-result refs, and their windows. Each coordinate resolves the complete `DHCReplayBasis` from C.21. `PathSliceId[]`, crossing pins, public-name rows, shipping pins, publication refs, and telemetry pins are conditional.

#### G.12:4.1 — Objects

| Local name | Exact object | Boundary |
| --- | --- | --- |
| `DHCCoordinateResultRef` | Ref to one persisted C.21/C.16 coordinate-result episteme and its active C.21 replay basis. | It is not a row, series, evidence path, or acceptance decision. |
| `DHCSeries` | One C.2.1 episteme whose EntityOfConcern is the discipline and whose ClaimGraph orders coordinate-result refs by explicit windows under one intended use, ClaimScope, and comparison basis. | It is not a public U-kind, publication occurrence, dashboard, carrier, or Work. |
| `DHCRow` | One representation element showing an exact coordinate-result ref and selected readable fields. | It does not compute, establish, or replace the result. |
| `DashboardSlice` | A C.29 view or grouping over exact row, result, or series refs. | It adds no comparison, normalization, acceptance, or selection semantics. |
| `DHCTelemetryPin` | A G.11-facing refresh payload with a canonical trigger, exact affected scope, and changed definition, window, evidence, or policy pins. | It is not evidence, currentness, an edition relation, or refresh Work. |
| dashboard publication | An E.24.PUB occurrence for one selected series or view edition, audience, bounded use, form, carrier, and availability interval. | A UTS row, rendering, upload, or release label does not make it obtain. |

Conceptual forms:

```text
DHCSeries := <
  DHCSeriesRef.edition,
  DisciplineRef,
  IntendedUse,
  ClaimScopeRef,
  ComparisonBasis,
  CoordinateResultRefs[],
  WindowOrder,
  DHCDefinitionSetRef.edition?,
  TargetSliceRef?,
  CurrentnessRuleRef?
>

DHCRow := <
  RowId,
  DHCCoordinateResultRef,
  Window,
  DisplayedValue,
  DisplayedScaleOrUnit,
  DisplayedStance?,
  DisplayAnnotations?
>

DashboardSlice := <
  DashboardSliceId,
  DHCSeriesRef.edition?,
  IncludedCoordinateResultRefs[],
  IncludedRowIds[],
  ViewSpecRef?,
  Annotations?
>
```

`TargetSliceRef` is present only when the series construction or publication consumes an A.2.6 selection. The ClaimGraph must then state how each selected slice belongs to or is covered by the authoritative `ClaimScope`. A changing time window is not silently encoded as “latest.”

#### G.12:4.2 — Method of obtaining the result

**Stage A — Select what the view is about**

1. **Start from exact results.** Select persisted C.21 coordinate-result refs for one already identified discipline. Do not compute from labels or restate Characteristic semantics in G.12.
2. **Fix use, scope, and windows.** Name IntendedUse and ClaimScope. Add a `TargetSliceRef` only when the computation or publication really consumes it, and state its relation to the scope.
3. **Check replay identity.** For every coordinate, resolve the C.21 `DHCReplayBasis`: Characteristic, Scale, Unit when current, `DHCMethodRef.edition`, exact Method and MethodDescription, model or calibration pins when used, time or population basis, and any distance or definition-set edition.
4. **Choose the comparison branch.** Directly comparable C.16 readings need no Bridge. Actual distinct-local-sense use cites the obtaining F.9 relation, direction, admitted use, and loss. Add reference-plane routing only when a real plane crossing is used; cite its exact basis, and keep any assurance consequence in R only.
5. **Open optional panels only when used.** Portfolio, QD, open-ended, maturity, SoTA, shipping, and advanced-view fields appear only through their extension blocks.

**Stage B — Construct or update content**

1. When new coordinates are required, separately identify the C.16 measurement Method, MethodDescription, model, calibration, dated Work, result, and result episteme. G.12 creates none of them from a row.
2. Assemble or revise the `DHCSeries` ClaimGraph from exact coordinate-result refs and windows. This assembly may be dated Work; the series episteme is its result, not the Work or work record.
3. Apply A.18 and any exact A.19/G.0 comparison, normalization, distance, or aggregation rule actually used. Nominal and ordinal values remain non-arithmetic unless an explicit lawful transformation creates another Scale.
4. Construct `DHCRow` and `DashboardSlice` representations. They may omit fields for readability only when every displayed claim still resolves its exact result and replay basis.

**Stage C — Publish or refresh only when required**

1. If public designators are needed, use F.18 for names of already constituted series or views. A name row is not publication.
2. If an audience must be able to obtain the selected edition, establish E.24.PUB with exact audience, bounded use, form, carrier, and interval.
3. If changed definitions, windows, evidence paths, crossing bases, or policies must trigger selective maintenance, emit G.11 telemetry pins naming the affected result or series slice. Otherwise stop without refresh wiring.

#### G.12:4.9 — Optional Extensions

> An extension adds only the panel-specific fields, pins, and triggers consumed by that view. It does not redefine C.21, C.16, comparison, evidence, publication, selection, or refresh semantics.

##### `G.12:Ext.SoTAPalette` — SoTA palette alignment

* `PatternScopeId`: `G.12:Ext.SoTAPalette`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.2`
* Optional pins: `SoTA_PackRef.edition?`, exact F.17 cell refs, and obtaining F.9 relation refs when alignment is actually displayed.
* No additional trigger kind by default.

##### `G.12:Ext.PortfolioTelemetry` — selector result panel

* `PatternScopeId`: `G.12:Ext.PortfolioTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `G.5`
* Conditional values: `TaskSignatureRef?`, resolved `DominanceRegime`, resolved `PortfolioMode`, and exact selector result and basis refs.
* Set-returning semantics remain visible. A scalar headline is only a view annotation unless a separate policy lawfully constructs it.

##### `G.12:Ext.QDTelemetry` — illumination or archive panel

* `PatternScopeId`: `G.12:Ext.QDTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* Conditional pins: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceSpecRef.edition?`, `InsertionPolicyRef`, `EmitterPolicyRef?`, `ArchiveSnapshotRef?`, and `PathSliceId[]` when refresh uses them.
* Illumination and coverage stay telemetry unless a separate accepted policy promotes them.

##### `G.12:Ext.OpenEndedTelemetry` — open-ended or transfer panel

* `PatternScopeId`: `G.12:Ext.OpenEndedTelemetry`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `C.19`
* Conditional pins: `TransferRulesRef.edition`, `EnvironmentValidityRegionId?`, `ProbeBudgetPolicyId?`, and `PathSliceId[]`.
* Open-ended signals do not become dominance objectives by display.

##### `G.12:Ext.MaturityLadderPanel` — maturity view

* `PatternScopeId`: `G.12:Ext.MaturityLadderPanel`
* `GPatternExtensionKind`: `DisciplineSpecific`
* `GoverningPatternId`: `G.8`
* Conditional values: `MaturityCardRef`, `MaturityRungId?`, and evidence-path refs when the displayed rung relies on them.
* Adds `RSCRTriggerKindId.MaturityRungChange` only for a refresh-wired view.

##### `G.12:Ext.PackInclusion` — shipping stub

* `PatternScopeId`: `G.12:Ext.PackInclusion`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.10`
* Conditional values: exact pack ref, selected `DHCSeriesRef.edition` or `DashboardSliceRef`, and the replay or shipping pins the included claims actually require.
* G.10 governs shipping; this extension only identifies what is included.

##### `G.12:Ext.ViewFamilySeed` — advanced view seed

This non-normative seed reserves no semantics. An embedding, prediction, change-point, or drift panel needs its own selected governor, inputs, limitations, and policy before it can affect a claim or decision.

### G.12:5 — Interfaces

| Interface | Consumes | Produces |
| --- | --- | --- |
| `Create_DHCSeries` | exact coordinate-result refs, discipline, intended use, ClaimScope, windows, comparison basis, optional definition-set and target-slice refs | one C.2.1 `DHCSeries` episteme edition |
| `Update_DHCSeries` | prior series edition, added or replaced exact result refs, affected windows, edition rule | successor series episteme edition plus exact edition relation when asserted |
| `Render_DHCView` | exact result or series refs, view specification, annotations | `DHCRow[]` and/or `DashboardSlice` representations |
| `Publish_DHCView` | selected episteme or view edition plus E.24.PUB audience, bounded use, form, carrier, and interval | obtaining publication relation when its predicate holds |
| `Emit_DHCTelemetry` | exact changed definition, window, evidence, crossing, or policy pin and affected slice | G.11-facing telemetry payload |
| optional panel interfaces | the corresponding extension's exact values | only that panel's representation and conditional refresh pins |

### G.12:6 — Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-G12-1` | Every displayed coordinate resolves one exact C.21/C.16 result episteme and the active C.21 replay basis. |
| `CC-G12-2` | ClaimScope is authoritative; TargetSlice is optional, consumed explicitly, and related to that scope. |
| `CC-G12-3` | Direct same-semantics comparison uses C.16 conditions without a Bridge; actual distinct-local-sense use cites exact F.9 direction, admitted use, and loss. |
| `CC-G12-4` | Characteristic, Scale, Unit, Method, MethodDescription, model, calibration, Work, result, result episteme, series episteme, row, slice, publication, form, and carrier are not collapsed. |
| `CC-G12-5` | Numeric, ordinal, target-band, normalization, distance, comparison, and aggregation operations cite their exact lawful definitions. |
| `CC-G12-6` | A series ClaimGraph identifies exact result refs, windows, intended use, ClaimScope, and comparison basis; content change uses the applicable edition rule. |
| `CC-G12-7` | Rows and slices are view-only representations. They introduce no new objective, scalar winner, evidence, acceptance, or authority. |
| `CC-G12-8` | Public names and E.24.PUB publication are conditional and separate; local dashboards need neither. |
| `CC-G12-9` | Refresh telemetry appears only for a named maintenance receiver and identifies the exact affected slice and changed pins. |
| `CC-G12-10` | Optional panel fields appear only with their extension and preserve the source pattern's set, archive, maturity, transfer, shipping, or palette semantics. |
| `CC-G12-11` | The effective G.Core obligations are expanded by value; nil-elided or unused branches are not made mandatory. |

### G.12:7 — Bias-Annotation

G.12 counters screen-first, “latest”-by-default, scalar-winner, and publication-as-truth bias. A clean view can hide incompatible definitions, while a dense technical record can make a simple trend unreadable. Start from exact result claims, show the smallest useful view, and keep deeper replay and refresh detail addressable rather than visually dominant.

### G.12:8 — Consequences

**Benefits.** Dashboard claims can be read quickly and replayed from exact result and definition refs. Historical results remain distinct from changed definitions, and refresh can be local when needed.

**Costs.** A relied-on trend needs exact result, scope, window, and replay identities. Publication and refresh add their own conditional work.

**Risks avoided.** Screenshot-as-result, context-container resurrection, scope/slice collapse, hidden method drift, illicit ordinal arithmetic, scalarization by view, and carrier-as-publication are blocked.

### G.12:9 — Relations

**Builds on:** C.21, C.16, C.2.1, A.2.6, C.29, E.24.PUB, and G.Core only for the active Part-G branches.

**Coordinates with:** G.6 and G.11 for relied-on evidence and refresh; A.19 and G.0 for comparison or aggregation; F.9 for actual distinct-local-sense use; F.18 for optional public names; G.5, C.18, C.19, G.8, G.10, and G.2 through the declared extensions.

### G.12:10 — Author's Quick Checklist

1. Name the discipline, intended use, ClaimScope, exact coordinate-result refs, and windows.
2. Resolve the C.21 replay basis for every coordinate.
3. Add TargetSlice only when consumed and state its relation to ClaimScope.
4. Use the direct comparison branch unless distinct local senses actually require F.9.
5. Keep series episteme, measurement Work/result, row, slice, publication occurrence, form, and carrier separate.
6. Add public naming, publication, evidence paths, assurance, optional panels, and refresh only for named receivers.

### G.12:11 — Worked Micro-examples

**Decision-making dashboard.** A local view shows exact `ReproducibilityRate`, `FormalRecognitionStatus`, `PracticeAdoptionRate`, `AlignmentDensity`, `TraditionShareEntropy`, and `TraditionShareConcentration` result refs. Entropy and HHI occupy separate rows with their directions visible. A portfolio panel preserves the G.5 selected set. No audience publication is claimed.

**Evolutionary architecture dashboard.** A `DHCSeries` episteme orders exact reproducibility and DisruptionBalance results over declared windows. An optional open-ended panel shows transfer events as telemetry. A later E.24.PUB occurrence makes one selected dashboard form available to a named audience; that occurrence neither changes the series content nor turns the rendering Work into the health result.

### G.12:End

