## G.10 - SoTA Pack Shipping

**Tag:** Architectural pattern (conceptual; notation‑independent; pack‑boundary governing definition)
**Stage:** release‑time composition and publication; edition‑aware; **GateCrossing‑gated** via `E.18` CrossingBundle (and the relevant GateCrossing harness patterns).
**Builds on:** `G.Core` (Part‑G core invariants and delegation); upstream pack/kit governing definitions as cited publications or records (not redefined here).
**Governs (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing selection/parity roster, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not govern:** governing spec refs (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their governing definitions and are **cited**).

### G.10:1 - Problem frame — Shipping without smuggling semantics

Part G produces many **kit-governed** and **suite-governed** publications or records (harvest packs, CHR/CAL packs, evidence graphs, bridge calibration records, log bundles, parity reports). Without an explicit **pack-boundary governing definition**, “shipping” tends to become:

* an ad‑hoc folder/export ritual (tool‑locked, not citable), or
* a silent re‑specification layer (shipping accidentally redefines legality, defaults, or selection semantics), or
* a brittle hand‑off that cannot support RSCR/refresh (no actionable pins/editions/policies attached).

`G.10` fixes the pack boundary: it defines the **single, normative shipping surface** for Part‑G outputs — **`SoTA‑Pack(Core)`** — and a minimal choreography for making shipped artefacts **selector‑ready** and **audit‑citable**, while delegating all Part‑G‑wide invariants to `G.Core` (citation/delegation, not restatement).

### G.10:2 - Problem — Why naive shipping breaks reuse, legality, and refresh

Naive shipping fails (conceptually) when any of the following occurs:

1. **Format-as-governing-spec.** A concrete export format is treated as “the pack,” turning a tool choice into a governing pack definition.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Pack smuggles semantics.** Shipping reintroduces “convenience” rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the governing spec ref.
4. **Invisible crossings.** Cross-context or cross-plane reuse is present, but the pack does not expose the crossing bundles and penalty policy pins needed for audit and refresh planning.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which mechanisms/policies/editions produced them*.
6. **Refresh orphaning.** Telemetry and decay signals exist, but the shipped artefact provides no stable scope keys (`PathId` / `PathSliceId`) and no payload pins for RSCR triggers.

### G.10:3 - Forces

| Force                                              | Tension                                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Notation independence**                          | Make packs portable across tools ↔ still make them concrete enough to be used.                   |
| **Completeness vs minimality**                     | Ship enough to be selector‑ready ↔ avoid duplicating governing definition semantics.                            |
| **Continuity vs evolvability**                     | Preserve public IDs across edition bumps ↔ allow legitimate upgrades and deprecations.           |
| **Cross‑context reuse vs honesty**                 | Enable reuse across Traditions/contexts ↔ keep crossings explicit and auditable.                 |
| **Telemetry usefulness vs semantic contamination** | Export useful signals ↔ avoid turning telemetry into dominance/acceptance without pinned policy. |
| **Fast shipping vs refreshability**                | Ship quickly ↔ ensure RSCR triggers can be planned and scoped (P2W‑path aware).                  |

### G.10:4 - Solution — `SoTA‑Pack(Core)` as the shipping object and publication kit

`G.10` defines a **pack-governed** shipping surface: a notation‑independent object that **cites** all upstream artefacts by stable ids/refs and exposes the minimum pins required to (a) consume the result via selection, (b) audit it via path citations and crossing bundles, and (c) refresh it via typed RSCR triggers.

#### G.10:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (G.10)** *(normative; expands per `G.Core:4.2`; `Nil‑elision` applies)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := { `GCoreTriggerSetId.RefreshOrchestration` }
  *(payload pins: `PackId(UTS)`, `publicationScopeId`, `CNSpecRef.edition`, `CGSpecRef.edition`, `PlanItemRefs := SlotFillingsPlanItemRef[]`, `AuditPins`, `UTSRowId[]`, `PathId/PathSliceId`, crossing policy pins, `TelemetryPinIds`, relevant upstream artefact ids)*

* `DefaultsConsumed` := {
  `DefaultId.PortfolioMode`,
  `DefaultId.DominanceRegime`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Governing definitions are resolved through `G.Core.DefaultGoverningDefinitionIndex` and are not restated here.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; id‑valued unless noted)* := {
  `PackId(UTS)`,
  `publicationScopeId`,
  `contextSliceId?`,

  `PlanItemRefs := SlotFillingsPlanItemRef[]?` *(WorkPlanning planned baseline refs)*,
  `AuditPins` *(pack‑level pin bundle: edition pins (only on `…Ref.edition`), policy‑ids, UTS/Path pins; ids only)*,

  `UTSRowId[]`,
  `PathId[]?`, `PathSliceId[]?`,
  `CrossingBundleIds := CrossingBundleId[]?`,
  `TelemetryPinIds := TelemetryPinId[]?`,
  `PortfolioRosterId?`,

  `MOOManifestId?` *(method‑of‑obtaining‑output disclosure; conceptual object id)*
  }
  *(Optional pins from `CrossingVisibilityPins` MAY be strengthened to unconditional by listing them above; `G.10` typically strengthens `UTSRowId[]` and path/crossing bundles when the pack is publicly shipped.)*

* `TriggerAliasMapRef` := `∅` *(no local trigger tokens in Phase‑2)*

> **Mode‑specific definition pins.** Any additional pins required for QD/OEE/interop shipping are introduced only by `GPatternExtension` blocks in `G.10:4.6` (never smuggled into the core linkage).

#### G.10:4.2 - `SoTA‑Pack(Core)` object model (normative; notation‑independent)

`SoTA‑Pack(Core)` is a **shipment object** (a *pack*, not a kit and not a suite) that **cites** upstream artefacts and exposes pack‑level pins required for downstream use.

```
SoTA‑Pack(Core) :=
⟨
  PackId(UTS),
  publicationScopeId,
  contextSliceId?,
  CG-FrameContext,
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,

  // Governing spec refs (refs + edition pins; semantics governed by their patterns)
  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,
  CGSpecRef := ⟨G.0 ref,  CGSpecRef.edition⟩,

  // Selector-facing selection/parity roster token (conceptual; no formats mandated)
  PortfolioRosterId?,        // produced by `G.10‑1` as part of composition; may cite ε and the applicable pinned regime/mode refs

  // Cited payload packs/kits (ids only; semantics governed by the cited governing patterns)
  SoTAHarvestPackId?          // e.g., G.2 output id
  CHRPackId?                  // G.3 output id
  CALPackId?                  // G.4 output id
  EvidenceGraphId?            // G.6 output id
  BridgeMatrixId?             // G.2/G.7 cited id
  BridgeCalibrationTableId?   // G.7 output id
  SoSLOGBundleId?             // G.8 output id
  ParityReportId?             // G.9 output id
  DashboardSliceId?           // G.12 output id (optional)
  InteropSurfaceId?           // G.13 output id (optional)

  // Path citation surface (ids only; semantics governed by A.10/G.6)
  PathIds := PathId[]?,
  PathSliceIds := PathSliceId[]?,

  // Planned baseline + audit pins (P2W-aware; ids only)
  PlanItemRefs := SlotFillingsPlanItemRef[]?,
  AuditPins := { id pins… },                 // editions only on `…Ref.edition`; includes policies, UTS/Path pins, crossing pins

  // Crossing visibility surface (per GateCrossing; ids only)
  CrossingBundleIds := CrossingBundleId[]?,

  // Telemetry hooks for refresh planning (ids only; PathSlice-keyed; policy-id pinned)
  TelemetryPinIds := TelemetryPinId[]?,

  // Method-of-obtaining-output (MOO) disclosure (conceptual; ids only)
  MOOManifestId?,

  Notes?
⟩
```

#### G.10:4.2.1 - Portfolio roster (normative; pack-governed; governing-definition delegating)

`PortfolioRosterId` identifies the **selector‑facing** pack roster token. The corresponding `PortfolioRoster@Context` is one citation-and-binding roster record inside the shipped publication surface, not a `Surface` or `SurfaceKind` value:
it MUST NOT redefine selection / selected-set semantics (governed by `G.5`) or parity semantics (governed by `G.9`).
Mode‑specific definition pins (QD/OEE/interop) are introduced only via `G.10:Ext.*` blocks.

```
PortfolioRoster@Context :=
⟨
  PortfolioRosterId,
  PackId(UTS),
  CG-FrameContext,
  describedEntity,

  // Selector operation and default-resolution support
  portfolioMode?,
  dominanceRegime?,
  ε?,

  // Published selector outcome and set-result declaration (metadata fields, not local semantics)
  selectorOutcomeKind?,
  setResultFamily?,
  handoffKind?,
  subjectKind?,
  sourceSetFamily?,
  derivedViewKind?,
  sourceSetComposition?,
  basePaletteRef?,
  lensId?,
  shortlistId?,
  promotionPolicyRef?,
  retentionIntent?,

  // Selector-facing roster + provenance hooks (ids only)
  MethodFamilyIds := MethodFamilyId[]?,
  GeneratorFamilyIds := GeneratorFamilyId[]?,
  ParityReportId?,
  SCRId[]?, DRRId[]?,

  // Pin reuse: prefer referencing the enclosing pack’s AuditPins bundle
  AuditPins?,
  Notes?
⟩
```

*Presence rule:* `PortfolioRosterId` MAY be omitted only when the shipped pack is *inputs‑only*
(e.g., shipping CHR/CAL/evidence without any selector‑consumable selected-set/shortlist output).

The `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `sourceSetFamily`, `sourceSetComposition`, `derivedViewKind`, `basePaletteRef`, `lensId`, and `shortlistId` fields in this roster are payload metadata fields or refs inside the shipped publication surface. They do not define new Part-E `SurfaceKind` values and they do not let `G.10` re-govern `G.5`, `C.18`, `C.19`, or `G.2` semantics.

**Interpretation constraints (normative by delegation).** Any universal invariants governing (i) CN/CG spec-ref governing-definition assignment, (ii) crossing visibility and penalty routing, (iii) tri‑state guards, (iv) set‑return semantics, (v) P2W split, (vi) defaults, and (vii) RSCR trigger typing are **not restated here** and are enforced via `G.Core` conformance (see `CC‑G10‑CoreRef`).

#### G.10:4.3 - Shipping choreography (normative; governing-definition delegating)

`G.10` prescribes a minimal, governing-definition delegating sequence for composing a shipped pack:

1. **S‑1 — Gather & pin.** Collect upstream artefact ids and verify the **required pins** implied by the linkage manifest (edition pins, policy pins, UTS/Path pins).
2. **S‑2 — Compose `SoTA‑Pack(Core)` + MOO disclosure.** Assemble the pack object and attach a **`MOOManifest`** that lists the referenced mechanisms/policies/editions that produced the shipped outcomes (ids only; semantics stay with governing definitions).
3. **S‑3 — Publish selection/parity roster (selector‑facing).** Produce a selector‑readable `PortfolioRosterId` with the parity/definition pins required for reproducibility; do not mandate formats.
4. **S‑4 — Anchor and publish path citations.** Ensure A.10 anchors exist and publish/record `PathId/PathSliceId` citations required for downstream explainability (e.g., `C.23/H4`) and maturity rung changes.
5. **S‑5 — Expose CrossingBundle.** For each GateCrossing relevant to the shipped artefacts, expose the required `CrossingBundle` references (fail fast on missing or non‑conformant bundles when required).
6. **S‑6 — Emit telemetry pins for refresh planning.** Whenever illumination increases or archive/OEE pin state changes, emit PathSlice‑keyed telemetry with policy‑id and the active `…Ref.edition` pins (and QD `EmitterPolicyRef`/`InsertionPolicyRef` when applicable).
7. **S‑7 — Publish to UTS (twin labels).** Mint/refresh UTS Name Cards needed to cite the pack and shipped heads (Tech/Plain twins when required); cross‑Context identity travels only via Bridges with CL and loss notes.
8. **S‑8 — Optional: ingest interop surface.** If `G.13` interop is in use, ingest/cite `InteropSurface@Context` as annotation-only notes, pinning external index editions; do not redefine interop semantics.

#### G.10:4.4 - Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | G.* outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas     | `SoTA‑Pack(Core)` (UTS row + surfaces) + `AuditPins` (+ `MOOManifestId?`) (+ `PortfolioRosterId?`) |
| **G.10‑2** | `Publish_UTS`              | `PackId(UTS)`, `UTSRowId[]`, deprecation/edition‑bump notes       | UTS rows/Name Cards for the pack and shipped heads (incl. twins when required) |
| **G.10‑3** | `Expose_CrossingHooks`     | GateCrossings, lanes/planes/contexts                              | **CrossingBundle** (**E.18:CrossingBundle**) per GateCrossing; **fail** on missing/non‑conformant bundles |
| **G.10‑4** | `Pack_MOO`                 | referenced mechanism/policy/edition ids                           | `MOOManifestId` (ids only; governing-definition delegating) |
| **G.10‑5** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition` (+ QD/OEE pins when applicable) |
| **G.10‑6** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for `C.23/H4` & rung changes |
| **G.10‑7** | `Ingest_InteropSurface?`   | (optional) `G.13 InteropSurface@Context`                          | Annotated pack notes citing external‑index editions     |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

> **Note.** Any concrete serialisation/export is *not* part of this interface set. Serialisation belongs to interop/annex governing-definition assignment and must not become the governing definition.

#### G.10:4.5 - Consequence of governing-definition assignment (normative boundary statement)

`G.10` is the **one governing definition** of “shipping” in Part G *(by delegation to `CC‑GCORE‑SKP‑1`)*.
Other `G.x` patterns may produce artefacts that are shipped, but they must not embed shipping obligations; they cite `G.10` shipping surfaces instead.

#### G.10:4.6 - Extensions (pattern‑scoped; non‑core)

All method‑/generator‑/interop‑specific shipping extension declarations live here as `GPatternExtension` blocks.

##### GPatternExtension — `G.10:Ext.QDArchiveShippingPins`

**PatternScopeId:** `G.10:Ext.QDArchiveShippingPins`
**GPatternExtensionId:** `QDArchiveShippingPins`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, G.5, G.8, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `DHCMethodRef.edition?`
* `DHCMethodSpecRef.edition?`
* `EmitterPolicyRef` *(policy‑id / ref)*
* `InsertionPolicyRef` *(policy‑id / ref)*
* `CharacteristicSpaceRef` *(id/ref; iff archive partitioning is declared)*
* `CharacteristicSpaceRef.edition?` *(iff partitioning depends on an editioned space definition)*
* `PathSliceId[]` *(to bind telemetry/refresh scope when archive behaviour is present)*

**RSCRTriggerSetIds:** `∅` *(covered by `G.10` core linkage via `GCoreTriggerSetId.RefreshOrchestration`)*
**Notes (shipping-pin discipline):**
* This block never redefines archive semantics; it only states which pins must be present in the shipped pack when QD archive fields are present.

##### GPatternExtension — `G.10:Ext.OEEShippingPins`

**PatternScopeId:** `G.10:Ext.OEEShippingPins`
**GPatternExtensionId:** `OEEShippingPins`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition`
* `EnvironmentValidityRegion?` *(id/ref; iff an explicit region is declared as part of generator-family support)*
* `PathSliceId[]` *(scope key for refreshable generator telemetry when present)*

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* “Open‑endedness” semantics remain defined by the governing pattern; the pack only carries the pins required to make the shipped claim replayable/auditable.

##### GPatternExtension — `G.10:Ext.InteropCitation`

**PatternScopeId:** `G.10:Ext.InteropCitation`
**GPatternExtensionId:** `InteropCitation`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `InteropSurfaceId`
* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `PlaneMapRef.edition?`
* `MappingPolicyRef`

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* This block only records that an interop surface contributed to the shipped pack’s provenance; it does not redefine any crosswalk semantics.

#### G.10:4.7 - Published surfaces must ship kind, source, derivation, lens, and shortlist token

- Published surfaces should carry the selector outcome kind and, when applicable, the set-result kind or handoff kind, plus the subject kind, source set kind, and relevant declared surface pins.
- These are publication payload metadata fields inside `SoTA-Pack(Core)`, not new Part-E `SurfaceKind` values.
- Good publication fields include `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `subjectKind`, `sourceSetFamily`, `sourceSetComposition`, `dominanceRegime`, `lensId`, `shortlistId`, and any declared archive or promotion-policy ids that the reader needs to interpret the visible set.
- Those payload fields should use controlled tokens, cited ids, or already-declared head labels rather than shipping-local prose values.
- When the visible surface or the shortlisted source is one derived tradition view, also publish the derivation explicitly.
- Useful additional fields there include `derivedViewKind`, `basePaletteRef`, and the declared `qId` or reachability rule id that disciplined that derivation.
- `portfolioMode` may remain as one support field about selector operation, but it should not stand in for the public set label.
- A published surface should mirror semantics that are already declared in the governing palette, front, archive, or shortlist language.
- It should not redefine that semantics locally.
- When one shipped surface still needs a plain-language label, use the declared set-result kind and source set rather than falling back to `portfolioMode`.

#### G.10:4.7.1 - Worked publication slice

- If the visible surface is one tradition front under the declared `Q`, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Front`, `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, and keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable instead of pretending that the palette itself already was that front.
- If one shortlist is emitted from that derived tradition front, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Shortlist`, `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, `basePaletteRef=SoTAPaletteDescriptionId`, and the named `lensId` together.
- If that same shortlisted surface is emitted as one stable public object, also publish `shortlistId=<...>` and keep it recoverable that the token names that shortlist rather than replacing it.
- If one retained tradition archive view is shown, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Archive`, `sourceSetFamily=Archive`, `derivedViewKind=TraditionArchive`, and keep the same `basePaletteRef` recoverable.
- If the shortlist is later ordered, publish `setResultFamily=RankedShortlist` and keep the declared source set visible.
- Do not publish `setResultFamily=ChoiceSet` unless the shipped object is explicitly one mathematical analysis artifact rather than the public selected set.
- Do not publish `sourceSetFamily=TraditionPalette` alone when the visible object is already one derived tradition view; readers need to know which view is on the surface and which base palette it depends on.
- Do not publish `TraditionFront` or `TraditionArchive` as if they were the default meaning of `Tradition`.
- Do not ask `portfolioMode` to tell the reader whether they are seeing one palette, one front, one archive, or one shortlist.

### G.10:5 - Consequences

**Benefits**

* A shipped result becomes **selector‑ready** and **audit‑citable** without turning file formats into governing specifications.
* Shipping is no longer a semantic “backdoor”: pack‑level semantics remain governing-definition delegated.
* RSCR/refresh becomes operationally viable because pack‑level scope keys and payload pins are present.

**Costs / trade‑offs**

* Shipping becomes more explicit (more pins and explicit surfaces), which raises authoring overhead.
* If upstream governing definitions fail to provide citable ids/pins, `G.10` cannot paper over the gap; shipping will block or ship a visibly incomplete pack (depending on policy‑bound failure behaviour, governed by cited definitions).

### G.10:6 - Bias‑Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Format bias (Arch/Prag).** A popular export format is tempting to treat as “the pack”.
  *Mitigation:* keep Core surfaces conceptual (E.5.2); move serialisation recipes to Annex/Interop; keep conformance on semantics.
* **Centralisation bias (Gov).** A single pattern governing shipping semantics can become a bottleneck.
  *Mitigation:* keep shipping as one explicit governing-pattern responsibility, but push mode/method specifics into explicit `G.10:Ext.*` extension blocks and cite governing patterns.
* **Telemetry→dominance bias (Onto/Prag).** Shipping pipelines often “promote” telemetry proxies (illumination/coverage) into ranking.
  *Mitigation:* preserve the telemetry/order separation and require explicit CAL policy‑id for any promotion; record the policy‑id in audit pins/telemetry.
* **Interop authority bias (Onto/Epist).** External indexes can silently override local legality/typing.
  *Mitigation:* `G.10‑6` ingests interop only as cited notes (editions + mapping policy refs), never as a replacement governing spec ref.

### G.10:7 - Archetypal grounding (informative; post‑2015 method families)

**World‑plane (benchmark shipping).**
A CG‑Frame ships a selected set that includes a QD archive (e.g., MAP‑Elites‑class / CMA‑ME‑class families) and a generator family (e.g., POET‑class environment generation). The shipped `SoTA‑Pack(Core)` cites the CHR/CAL packs and records the QD/OEE extension-required pins through the extension blocks so that downstream parity and refresh can be scoped to the affected `PathSliceId`s rather than forcing a global rebuild.

**Episteme‑plane (synthesis shipping).**
A CG‑Frame ships a pluralistic set of admissible methods gathered from post‑2015 literature streams (living review + synthesis pack). The shipped pack carries explicit CN/CG spec refs, evidence path citations, and method‑of‑obtaining‑output disclosure; downstream selection uses set‑valued outcomes and can schedule refresh when the synthesis pack or key pins change.

### G.10:8 - Conformance checklist (CC‑G10)

This pattern inherits order/illumination, evidence, and bridge/penalty legality from the cited governing patterns (not restated here). Shipping‑specific requirements:

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD/OEE fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, (optional) `DHCMethodRef.edition` / `DHCMethodSpecRef.edition` when used, and (OEE) `TransferRulesRef.edition`; include `CharacteristicSpaceRef` (+ `CharacteristicSpaceRef.edition` when it affects partitioning reproducibility); for QD archive semantics also pin `EmitterPolicyRef` and `InsertionPolicyRef`. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active editions of the pinned `…Ref` fields (incl. OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels optional only). |
| **CC‑G10.4 (UTS publication & twins).** | All shipped heads appear on UTS with Tech/Plain twins **per delegated UTS discipline**; cross‑Context identity (when present) is routed via Bridges with CL and loss notes **per delegated crossing discipline**. | Verify UTS rows exist and that any cross‑Context identity is routed via Bridge artefacts with visible CL/loss notes. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For every declared selector set-result or archive published, the pack SHALL list the applicable generation/parity mechanism ids (e.g., QD `EmitterPolicyRef`/`InsertionPolicyRef`, parity harness ids, method refs where the method definition is generative) and the active policy‑id(s) in SCR‑visible bindings and telemetry pins (ids only; governing-definition delegating). | Verify `MOOManifestId` is present when outcomes are intended for downstream use and does not redefine semantics. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack cites all included upstream artefacts by id/ref and exposes the required pins (`AuditPins`, UTS/Path pins, CrossingBundleIds when required). | Verify all present payload artefacts have ids and the pins needed to cite/replay them. |
| **CC‑G10.7 (CrossingBundle exposure).** | For each GateCrossing relevant to shipped artefacts, the pack exposes the relevant `CrossingBundleIds` (or records that no such crossings exist) **per delegated crossing visibility discipline**, and shipping fails fast on missing/non‑conformant crossing bundles when required. | Verify crossing bundle presence/absence is honest and aligned with the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := SlotFillingsPlanItemRef[]` are present (WorkPlanning plan items, cited; no execution logs). | Verify plan items are cited by id and the pack does not treat decision records or execution logs as authoritative plan items. |
| **CC‑G10.9 (Extension‑scoped pin declaration).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | Verify conditional extension pins are not silently omitted when the mode is used. |
| **CC‑G10.10 (Derived tradition-view shipping).** | If the visible shipped surface or shortlisted source is one derived tradition view such as `TraditionFront` or `TraditionArchive`, the pack **MUST** publish the declared `sourceSetFamily`, keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable, and carry the derivation basis (`derivedViewKind`, declared `Q`, or reachability/coverage rule id) with enough explicitness that the visible surface cannot be mistaken for the default palette semantics. | Verify derived tradition views are shipped as derived views, not as silent redefinitions of the base palette. |

### G.10:8.1 - Anti‑patterns and remedies

* **AP‑1 Format‑as‑governing‑specification.** Remedy: keep Core surfaces conceptual (E.5.2); move serialisation to Annex/Interop; enforce `CC‑G10.1`.
* **AP‑2 Hidden edition drift.** Remedy: require `…Ref.edition` pins in AuditPins and treat edition changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑3 “QD archive present” but missing definition pins.** Remedy: enforce `CC‑G10.2` and the `G.10:Ext.QDArchiveShippingPins` pin declarations.
* **AP‑4 Telemetry silently becomes dominance.** Remedy: keep telemetry report‑only unless an explicit CAL policy promotes it; require policy‑id recorded (ties to `CC‑G10.3` and MOO discipline).
* **AP‑5 No PathSlice key → refresh becomes global.** Remedy: enforce PathSlice‑keyed telemetry and path citations (`G.10‑4`, `G.10‑5`).
* **AP‑6 Cross‑Context reuse without visible crossing pins.** Remedy: require `CrossingBundleIds` + Bridge/CL policy pins; fail fast on missing/non‑conformant bundles (`CC‑G10.7`).
* **AP‑7 Interop ingestion rewrites semantics.** Remedy: ingest interop as cited notes only; semantics remain in `G.13` (`G.10‑6`, `G.10:Ext.InteropCitation`).
* **AP‑8 Derived-view collapse.** Remedy: ship `sourceSetFamily`, `derivedViewKind`, `basePaletteRef`, and the declared `Q` or reachability basis with enough explicitness that one derived tradition view cannot masquerade as the default palette meaning.

### G.10:8.2 - SoTA‑Echoing (post‑2015, for orientation)

* **Research‑object packaging & provenance.** Post‑2015 practice increasingly treats “release artefacts” as *packages with explicit provenance, versions, and minimal replay pins* (e.g., modern research‑object and RO‑Crate‑class approaches). `G.10` mirrors the “package‑as‑citation‑surface” idea while keeping semantics governing-definition delegated.
* **Reproducibility regimes in ML/AI.** Contemporary reproducibility checklists, artifact evaluation/badging, and benchmark reporting norms motivate: explicit version pins, explicit method disclosure, and separating telemetry summaries from decision criteria unless policy‑promoted.
* **Scholarly KG interoperability.** ORKG/OpenAlex‑class ecosystems highlight the need to treat external mappings as *interop notes with editions*, not as replacement governing spec refs — matching the `G.10‑6` and `G.10:Ext.InteropCitation` stance.

### G.10:9 - Relations

**Builds on:** `G.Core`; consumes/cites artefacts governed by cited patterns from `G.2` (harvest pack), `G.3` (CHR pack), `G.4` (CAL pack), `G.6` (EvidenceGraph), `G.7` (bridge calibration), `G.8` (SoS‑LOG bundle), `G.9` (parity report), optional `G.12` (dashboard slice), optional `G.13` (interop surface).
**Publishes to / used by:** UTS (pack identity), selector‑facing consumers (via `G.5`), audit and assurance publications (SCR/RSCR), refresh orchestration (`G.11`).
**Constrains:** tooling exports are downstream; serialisation and repository integration are explicitly non‑normative here.

### G.10:End

---

