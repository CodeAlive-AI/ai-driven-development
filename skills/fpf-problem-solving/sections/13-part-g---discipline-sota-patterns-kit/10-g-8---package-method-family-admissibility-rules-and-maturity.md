## G.8 - Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)

> **Status:** Stable

**Use this when.** A selector needs a stable, citable package of C.23 admissibility rules and a maturity ladder for an already grounded G.5 method-family row. Resolve that row, the applicable rule editions and the evidence for the stated admission use, then publish their references as a bundle and maturity card. Later applications record their outcomes in the ledger.

**Boundary.** Use C.23 to define the rule itself. An ordinary G.5 result over grounded rows needs no G.8 bundle unless this packaged rule or ladder is consumed.




**Policy references.** The kit may cite the IDs of policies such as `Φ/Ψ/Φ_plane`, `FailureBehaviorPolicyId`, illumination promotion and E/E‑LOG. Cite the policies by ID only; their definitions stay with their governing sources. Under `F.8:8.1`, each must resolve, and a newly minted ID needs a resolvable `PolicySpecRef` and `MintDecisionRef`. G.8 MUST NOT silently mint policy IDs.

### G.8:1 - Problem frame

Method families compete within a `CG‑Frame`. For lawful dispatch, a selector needs auditable tri-state admissibility decisions and evidence it can cite by ID. Cite any crossings the use depends on, and preserve alternatives in the set returned under a partial order. Rules spread across prose, dashboards and checklists can leave it without the rule edition, threshold source or evidence basis needed for its result.

The **selector-facing, UTS-citable bundle** identifies the applicable C.23 rules and cites the card for the method family’s ordinal or partially ordered maturity ladder. It connects these to Acceptance (`G.4`), evidence paths (`G.6`), selection and the registry (`G.5`), and refresh (`G.11`). Those patterns retain their governing definitions.

### G.8:2 - Problem

1. **Selector needs a stable input artefact.** Maturity narratives and scattered SoS‑LOG excerpts leave `G.5` to reconstruct the rules or guess their defaults.
2. **Thresholds leak into LOG.** Numeric gates embedded in rule text or ladder rungs blur the boundary between LOG decisions (`C.23`) and Acceptance thresholds (`G.4`).
3. **Auditability is brittle.** Decisions (`pass/degrade/abstain`) lack stable, citable links to evidence paths (`G.6`) and crossing pins (Bridge/CL/Φ policy ids as required for the stated use), so later re‑checks and RSCR become ad‑hoc.
4. **Telemetry contaminates decision semantics.** Undeclared use of QD/OEE/illumination signals in dominance, or a changed definition edition, can alter outcomes without making the new basis visible.
5. **Refresh is under‑specified.** Bundle evolution (rules, ladders, pins, policies, editions) must be RSCR‑addressable via typed trigger kinds, not by free‑text “reasons”.

### G.8:3 - Forces

| Force                                        | Tension                                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Pluralism vs. dispatchability**            | Preserve multiple method families and partial orders ↔ provide a consumable artefact for `G.5`.        |
| **Auditability vs. authoring friction**      | Fine‑grained pins and citations ↔ keeping authoring lightweight and notation‑independent.                    |
| **Maturity as poset vs. scalar ranking**     | The declared ladder may be ordinal or partially ordered ↔ a single readiness number can hide its distinctions.                                  |
| **Telemetry richness vs. decision hygiene**  | Rich QD/OEE telemetry ↔ avoid illegitimate promotion into dominance without explicit policy.                 |
| **Design‑time packaging vs. run‑time trace** | Authoring produces stable bundles ↔ run‑time produces branch‑specific path traces and admissibility ledgers. |
| **Interoperability vs. crossing discipline** | Reuse across meanings, kinds or planes ↔ establish the actual correspondence and its receiving-use conditions.                           |

### G.8:4 - Solution — Publish SoS‑LOG bundles and maturity cards as UTS‑citable kit

#### G.8:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part-G core invariants)

**GCoreLinkageManifest (normative).**
*(Canonical shape, Nil‑elision, and Expansion rule are per `G.Core:4.2`.)*

**Method- and generator-specific pins.** Specify method- or generator-specific pins, editions and policies only in the `GPatternExtension` modules of `G.8:5`. The bundle and ledger schemas may list these as optional fields activated by the relevant extension. The core manifest lists only base-kit pins and Part-G-wide links.

```text
GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

RSCRTriggerSetIds := { GCoreTriggerSetId.EvidenceGraphKit },

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
},

CorePinsRequired := {
  // Public ids governed by this pattern (strengthen conditional pins where G.8 publishes UTS publication units)
  UTSRowId[],                    // bundle/ledger/card rows + any referenced UTS rows
  SoS‑LOGBundleRef,
  SoSLogRuleId[],
  MethodFamilyRowRef,             // exact G.5 <MethodFamilyId, rowEdition>
  RegistrationContext,

  // Closed value sets (ids only; UTS-registered)
  DegradeModeEnum,
  MaturityRungs,

  // Maturity ladder pins
  MaturityCardRef,               // required; recommended: published as separate UTS artefact
  MaturityRungId?,               // iff a specific rung is asserted at packaging/run-time

  // Evidence / provenance pins
  A10EvidenceGraphRef?[],        // packaging-time A.10 carriers (when PathId/PathSliceId not yet available)
  EvidenceGraphId?,              // iff resolvable to G.6 EvidenceGraph
  PathId[]/PathSliceId[]?,       // run-time ledgers typically have them

  // Authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[],  // edition-pinned method-description refs
},

DefaultsConsumed := {
DefaultId.PortfolioMode,
DefaultId.DominanceRegime,
DefaultId.GammaFoldForR_eff
},
⟩
```

*(RSCR payload pins typically include: `SoS‑LOGBundleRef`, `SoSLogRuleId[]`, `MaturityRungId?`, and `EvidenceGraphId/PathId/PathSliceId?`.
Crossing payload pins follow the actual sense, kind or plane correspondence and receiving use under G.Core:4.2.3; F.9 sense reuse uses `G.8:Ext.BridgeReuseWiring`. CL and loss-policy pins are required only by the actual calibration or separate named assurance use.
Method-/generator‑specific payload pins are listed only inside the relevant `GPatternExtension` blocks in `G.8:5`.)*

Include `DefaultId.GammaFoldForR_eff` in `DefaultsConsumed` **only if** the bundle or ledger exports aggregated `R_eff` summaries. Otherwise apply nil-elision.

#### G.8:4.2 - Kit: objects and naming discipline (LEX heads; twin‑register safe)

**Objects / surfaces (pattern-governed).**

* **`SoS‑LOG.Rule`**
  An executable tri‑state decision schema `{pass | degrade(mode) | abstain}` for `(TaskSignature, MethodFamily)`, cited by a rule id. *(“pass” may be described as “admit” in prose, but the normative tri‑state vocabulary is `G.Core`’s `{pass|degrade|abstain}`.)*
  `C.23` defines the rule. `G.8` packages its ID and the pins that bind it.

* **`SoS‑LOGBundle@Context`**
  A selector‑facing, notation‑independent packaging object published to UTS.

* **`AdmissibilityLedger@Context`**
  A run‑time ledger view that records admissibility outcomes, cited evidence paths, branch tokens, and the pins required for audit/refresh.

* **`MethodFamily.MaturityCardDescription@Context`**
  A maturity ladder description published as a citable artefact: **ordinal/poset**, closed rungs, `ReferencePlane` declared; no thresholds inside.

**Naming discipline (E.10 + “Spaces ≠ Maps”).**

* Technical heads are normative; Plain twins are didactic only and MUST NOT cross kinds.
* Do **not** alias `CharacteristicSpace` and `DescriptorMap`.

  * `DescriptorMapRef` is a **map‑reference** (typically used with QD archives).
  * `CharacteristicSpaceRef` is a **space‑reference** (grid/cell semantics, if used).
* A `CharacteristicSpaceRef` identifies the exact space. When the use depends on its defining episteme, carry `characteristicSpaceDescriptionRef: U.EpistemeRef` separately and resolve the pair under A.19:5.1.1.1. Other required edition pins follow their direct reference patterns; informal names supply no pin.

#### G.8:4.3 - `SoS‑LOGBundle@Context` schema (conceptual; notation‑independent)

A conforming bundle is published to UTS. Its field meanings are fixed, and its internal representation may vary:

```
SoS-LOGBundle@Context :=
⟨
  UTS.id := SoS‑LOGBundleRef,
  Edition,

  // Scope + spec pins (from GCorePinSetId.PartG.AuthoringMinimal)
  CG-FrameContext,
  entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
  CNSpecRef.edition,
  CGSpecRef.edition,

  MethodFamilyRowRef,             // exact G.5 <MethodFamilyId, rowEdition>
  RegistrationContext,

  SoSLogRuleId[] ,               // ids only; semantics governed by C.23
  ClosedEnums: {DegradeModeEnum, MaturityRungs},  // ids only; UTS-registered closed value sets
  A10EvidenceGraphRef?[] ,        // packaging-time evidence carriers (A.10 anchors) when paths are not yet stable
  MaturityCardRef ,               // UTS ref to maturity card (required; may be embedded but MUST be citable)
  MaturityRungId? ,               // if a specific rung is asserted at packaging time

  // Optional: Acceptance wiring (thresholds remain governed by G.4)
  AcceptanceClauseId[]? ,

  // Optional: Evidence wiring (for later audit & rung transition justification)
  EvidenceGraphId? ,
  PathId[]/PathSliceId[]? ,

  // Optional: correspondence wiring, under the actual channel/use conditions of G.Core:4.2.3
  BridgeId/BridgeCardId? ,
  CL/CL^k/CL^plane? ,
  Φ/Ψ/Φ_plane policy-ids? ,

  // Optional: selector semantics pins (explicit value or resolved via DefaultGoverningDefinitionIndex)
  PortfolioMode? ,
  DominanceRegime? ,

  // Optional: QD / OEE pins (only when those surfaces are declared)
  CharacteristicSpaceRef? ,
  characteristicSpaceDescriptionRef? , // U.EpistemeRef; exact definition under A.19:5.1.1.1
  DescriptorMapRef.edition? ,
  DistanceDefRef.edition? ,
  EmitterPolicyRef? ,
  InsertionPolicyRef? ,
  // Optional: Open-ended pins (only when those surfaces are declared)
  GeneratorFamilyRowRef? ,       // exact G.5 <GeneratorFamilyId, rowEdition>
  EnvironmentValidityRegionId? ,
  CouplerPolicyId? ,
  TransferRulesRef.edition? ,

  // Optional: branch/failure wiring (policy-bound)
  FailureBehaviorPolicyId? ,
  SoSLogBranchId[]? ,

  // Optional: authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[] ,

  Notes
⟩
```

**Bundle requirements**

* `SoS‑LOGBundle@Context` **does not introduce** new legality or normalization rules; it cites the pinned references above.
* Thresholds and numeric gates are cited by id from `G.4` Acceptance (no embedding inside the bundle).
* Cite the actual correspondence and receiving-use grounds under G.Core:4.2.3, with F.9 wiring through `G.8:Ext.BridgeReuseWiring` when applicable. Evidence paths are citable when available.

**Binding obligations B1–B5**

* **B1 — Evidence wiring.** At packaging time the bundle SHOULD provide resolvable evidence refs (typically `A10EvidenceGraphRef?[]` and/or `EvidenceGraphId?`). At run time, admissibility outcomes SHOULD cite `PathId/PathSliceId` when available (`G.6`), so rung transitions and `degrade/abstain` traces are audit‑stable.
* **B2 — CL/plane routing pins.** When reuse depends on a sense, kind or plane correspondence, the bundle/ledger MUST cite its obtaining relation and receiving-use grounds under G.Core:4.2.3. An F.9 use keeps its separate bounded-use claim and reliance basis through `G.8:Ext.BridgeReuseWiring`; kind and plane uses retain their direct governing conditions. The bundle/ledger MUST pin the Bridge/CL/Φ/Ψ/Φ_plane references required by that use (reference-only; policy ids resolvable per `F.8:8.1`). CL and loss-policy pins are mandatory only when required by the calibration or separate named assurance account. Any numerical assurance penalty MUST satisfy `CC‑GCORE‑PEN‑1`, including its model applicability and declared-result conditions.
* **B3 — Retention policy and QD fields.** Record `PortfolioMode` and dominance inputs under CC-G8-5 and their G.5 definitions. When the bundle or ledger binds a QD or QD-using generator branch, pin the descriptor, distance, insertion and emitter definitions required for that use under CC-G8-6. `PortfolioMode=Archive` alone preserves evidence and requires no QD definitions. Any illumination telemetry remains report-only unless a `G.4` governing-pattern policy authorises its dominance contribution and that policy id is recorded in the run-time trace.
* **B4 — Open-ended fields.** If the bundle binds an open-ended generator family, pin `GeneratorFamilyRowRef`, `TransferRulesRef.edition` and any validity-region/coupler policy ids used. For unknown transfer validity, apply C.23 R0/R2/R3/R7: use a declared `degrade` branch only after its prerequisites pass and its narrower use is permitted; otherwise return `abstain`. Retain the unknown condition and branch basis.
* **B5 — Telemetry hooks.** On any material telemetry event (illumination increase, archive insertion, probe accounting update, open‑ended coverage/regret proxy update), the emitted telemetry pins SHOULD include the controlling policy ids plus the relevant edition pins (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `TransferRulesRef.edition`) and, when available, `PathSliceId` to keep RSCR planning auditable.

#### G.8:4.4 - `AdmissibilityLedger@Context` (run‑time view; selector‑facing)

A conforming ledger is a UTS-published view (or a view-projection of a Work/Audit artefact) of the branch reached in the run. Its row positions are:

`⟨ MethodFamilyRowRef, TaskSignatureRef, SoSLogRuleId, RuleEdition, EvidenceProfileRef?, ClaimScope?, QualificationWindow?, IntendedAdmissionUse, EligibilityVerdict?, CGSpecVerdict?, AcceptanceVerdictRefs?, PolicyEditionRefs[], GuardDecision ∈ {pass|degrade|abstain}, DegradeMode?/SoSLogBranchId[]?, MaturityRungId?, AcceptanceClauseId[]?, EvidencePathRefs?, CrossingPins?, PortfolioMode?, DominanceRegime?, Edition ⟩`

The bundle, maturity card and ledger bind one exact G.5 `MethodFamilyRowRef = <MethodFamilyId, rowEdition>`; an open-ended generator use also binds `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>`. Their publication `Edition` does not replace a registry-row edition. Resolve an earlier result against the row edition it cites.

Retain every premise established or validly reused for the branch, with its applicable evidence profile, claim scope, qualification window, intended use and policy editions. Follow C.23:4.2.1 when a required reference is unavailable or evaluation stops early: name the missing basis or the judgement not reached, and leave its dependent result unestablished. Identify an applicable earlier result as reused.

These report qualifications add no guard status or maturity rung. `pass` requires the complete admission basis, and `degrade` requires the permitted branch and its prerequisites.

Use `EvidencePathRefs` to cite the relevant `PathId[]` or `PathSliceId[]` when the outcome’s evidence is addressable through a G.6 path or slice. `CrossingPins` retain the correspondence and receiving-use grounds required by G.Core:4.2.3. For `G.8:Ext.BridgeReuseWiring`, these include the F.9 bounded-use claim, reliance basis and applicable Bridge/CL/Φ pins.

#### G.8:4.5 - Maturity ladder as a citable poset (published card)

`MethodFamily.MaturityCardDescription@Context` names the exact `MethodFamilyRowRef`, evidence profile, claim scope and selected slices, qualification window, and intended admission use required by C.23. It is published with:

* closed rungs (UTS‑registered identifiers),
* `Scale kind = ordinal` and a declared `ReferencePlane`,
* (optional) explicit poset edges / precedence constraints,
* rung transition justifications that cite evidence paths (typically `G.6` paths).

Dispatchers, auditors and refresh planners can cite the published ladder description. The card describes the ladder under C.23.

#### G.8:4.6 - Interfaces (minimal I/O standard; conceptual)

| Interface                               | Consumes                                                                                   | Produces                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **G.8‑1 `Publish_LOGBundle`**           | `MethodFamilyRowRef`, `SoSLogRuleId[]` with rule editions (C.23), pins to Acceptance/Evidence/Crossings (as applicable) | `SoS‑LOGBundle@Context` (UTS row)                                                     |
| **G.8‑2 `Publish_AdmissibilityLedger`** | Bundle + run‑time branch outcomes + evidence path refs (when available)                    | `AdmissibilityLedger@Context` (UTS row or UTS‑citable view)                           |
| **G.8‑3 `Publish_MaturityCard`**        | Ladder description + (optional) evidence path refs for rung transitions                    | `MaturityCardDescription@Context` (UTS row; editioned)                                |
| **G.8‑4 `Expose_TelemetryHooks`**       | QD/OEE/archive/open‑ended telemetry signals (when declared)                                | telemetry pins for refresh (`…Ref.edition`, policy‑ids, `PathSliceId` when available) |

### G.8:5 - Extensions (pattern‑scoped; non‑core)

Publish method- or generator-specific requirements in `GPatternExtension` blocks with stable **PatternScopeId**s. The core kit is shared across methods and generators.

#### G.8:5.1 - `G.8:Ext.SoSLOGWiring`

**PatternScopeId:** `G.8:Ext.SoSLOGWiring`
**GPatternExtensionId:** `SoSLOGWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.23`
**Uses:** `{C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoSLogRuleId[]`
* `SoSLogBranchId[]?`
* `FailureBehaviorPolicyId?` *(when degrade behaviour is policy‑bound)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.8:4.1`)*
**Notes (wiring‑only):**
* Rule meaning, branch taxonomy, and “probe/sandbox” semantics are governed by `C.23`; this module only binds ids and pins.

#### G.8:5.2 - `G.8:Ext.AcceptanceWiring`

**PatternScopeId:** `G.8:Ext.AcceptanceWiring`
**GPatternExtensionId:** `AcceptanceWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.4`
**Uses:** `{G.4}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `AcceptanceClauseId[]`
* `EvidenceProfileId[]?` *(if the ledger/bundle cites evidence profile ids rather than only paths)*
* `PromotionPolicyId?` *(only if telemetry may be promoted into dominance by explicit CAL policy)*

**RSCRTriggerKindIds (optional delta):** `{RSCRTriggerKindId.PolicyPinChange}` *(only if acceptance policies are pinned as ids in the bundle/ledger)*
**Notes (wiring‑only):**
* Thresholds remain governed by `G.4` Acceptance; this module carries only clause ids and policy pins.

#### G.8:5.3 - `G.8:Ext.BridgeReuseWiring`

**PatternScopeId:** `G.8:Ext.BridgeReuseWiring`
**GPatternExtensionId:** `BridgeReuseWiring`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.7`
**Uses:** `{G.7, F.9, A.10, B.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum; conditional on the stated use):**

* `BridgeId/BridgeCardId` *(the obtaining Bridge used; a `BridgeCardId` is needed only when that Card is relied on)*
* `CL/CL^k/CL^plane` *(when cited; the applicable values are mandatory when required by the `G.7` calibration or named `B.3` assurance account)*
* `Φ/Ψ/Φ_plane policy-ids` *(only the policy ids and editions required by the actual `G.7` calibration or named `B.3` assurance account; reference‑only and resolvable per `F.8:8.1`)*
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(both required when calibration evidence is cited, together with the row locator and active policy pins required by `G.7` `CC‑G7‑SCRLinkage‑1`)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration records by id)*
**Notes (wiring‑only):**
* Present when `SoS-LOGBundle@Context` uses an F.9 sense correspondence. A combined kind or plane use retains its separate relation and receiving conditions under G.Core:4.2.3.
* The wiring MUST keep the obtaining Bridge reference, the separate bounded-use claim (use, direction, rule, and tolerated loss), and the `A.10` reliance basis citable. A separate named assurance use also cites its exact target claim, receiving use, and `B.3` assurance basis/result. Required CL values, policy editions, and evidence remain mandatory for that account; any numerical assurance penalty satisfies the model applicability and declared-result conditions of `CC‑GCORE‑PEN‑1`. Ordinary supported reuse does not require a CL shorthand, calibration record, loss-policy id, or assurance claim merely to fill the package.

#### G.8:5.4 - `G.8:Ext.QDArchiveTelemetry`

**PatternScopeId:** `G.8:Ext.QDArchiveTelemetry`
**GPatternExtensionId:** `QDArchiveTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `EmitterPolicyRef`
* `InsertionPolicyRef`
* `CharacteristicSpaceRef` with separate `characteristicSpaceDescriptionRef: U.EpistemeRef` *(required iff cell boundaries / de‑dup / parity depend on the space definition; resolve the pair under A.19:5.1.1.1)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* Archive/illumination signals are telemetry; promotion into dominance is only via explicit `G.4` policy pins.

#### G.8:5.5 - `G.8:Ext.ExploreExploitTelemetry`

**PatternScopeId:** `G.8:Ext.ExploreExploitTelemetry`
**GPatternExtensionId:** `ExploreExploitTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19`
**Uses:** `{C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExploreExploitBudgetPolicyId?`
* `ProbeAccountingId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* When “probe/sandbox” is used, the controlling policy ids are pinned and recorded in the ledger/bundle trace.

#### G.8:5.6 - `G.8:Ext.OpenEndedWiring`

**PatternScopeId:** `G.8:Ext.OpenEndedWiring`
**GPatternExtensionId:** `OpenEndedWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5` *(generator family registry surface; algorithm semantics remain external to Part‑G core)*
**Uses:** `{G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyRowRef`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by a governing-pattern policy.

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (for example, conservative offline RL and transformer-based policy models). The bundle cites `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`) and cites `AcceptanceClauseId[]` for any floors (governed by `G.4`). The run‑time `AdmissibilityLedger` cites `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` uses the ledger to return a **selected set** under the declared partial order. A scalar winner would discard alternatives that order leaves unresolved.

**Show-B — QD archive dispatch with edition-pinned descriptors.**
A method family uses a QD archive, for example one driven by CMA-ES or a differentiable QD method. The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show-C — Open-ended environment–method co-evolution.**
A generator family operates in an open-ended setting (e.g., POET-style or PAIRED-style regimes). The bundle carries `TransferRulesRef.edition` and validity-region pins. If transfer validity is unknown, a declared narrower-use branch may return `degrade` after C.23’s prerequisites pass; without that permitted branch, the result is `abstain`.

If the evidence profile is missing at R0, report that missing prerequisite. Record the later Acceptance judgement as not reached; assigning it `false` would invent a result. Retain an applicable maturity result when it was validly reused. Coverage/regret telemetry remains report-only unless its governing policy promotes it into dominance.

### G.8:7 - Bias‑Annotation

A maturity label can hide different evidence or admission conditions. Keep the exact rule, row edition and receiving use beside the label; the bundle itself supplies no maturity verdict.

### G.8:8 - Conformance Checklist (CC‑G8)

* **CC‑G8‑CoreRef (G.Core conformance bridge).**
  A conforming `G.8` SHALL satisfy the **effective** set of `CC‑GCORE‑*` obligations implied by `G.8:4.1` (expanded per `G.Core:4.2`), including required pins, trigger sets, and Default Governing Definition Index citation.

* **CC‑G8‑1 (No thresholds in LOG).**
  Any numeric gate, maturity floor, or threshold SHALL be authored as a `G.4` Acceptance artefact and cited by id; the LOG bundle/ladder SHALL NOT embed thresholds.

* **CC‑G8‑2 (Tri‑state discipline; delegated).**
  Guard outcomes SHALL obey the tri‑state domain and unknown handling defined in `G.Core` (delegation to `CC‑GCORE‑GUARD‑1`).
  Any sandbox/probe‑only behaviour SHALL be represented as an explicit `C.23` branch and MUST pin (and record) the controlling policy id (typically an E/E‑LOG policy id via `C.19`), rather than inventing a fourth status or silently coercing unknowns.

* **CC‑G8‑3 (Path citation when evidence is path‑addressable).**
  For each recorded `pass/degrade/abstain` outcome whose evidence is path-addressable under `G.6`, the run-time `AdmissibilityLedger` MUST cite that `PathId/PathSliceId`. At packaging time, the bundle/ledger SHALL at minimum provide resolvable evidence refs (e.g., `EvidenceGraphId?` + anchor refs).

* **CC‑G8‑4 (Crossing visibility and penalty routing; delegated).**
  Any cross-Context or cross-plane reuse asserted by the bundle/ledger SHALL satisfy the core crossing visibility and penalty routing invariants (delegation to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`).

* **CC‑G8‑5 (PortfolioMode/dominance hygiene; delegated).**
  The bundle/ledger SHALL treat `PortfolioMode` and dominance fields as pinned inputs and SHALL cite the governing definition for each omitted default through `G.Core.DefaultGoverningDefinitionIndex` (delegation to `CC‑GCORE‑DEF‑1` and `CC‑GCORE‑SET‑1`; governing definitions include `CC‑G5.23` for `DefaultId.PortfolioMode` and `CC‑G5.28` for `DefaultId.DominanceRegime`). It MUST NOT restate default values locally.
  If the bundle/ledger records telemetry that could influence dispatch (e.g., illumination/QD/OEE/open‑ended proxies), such telemetry SHALL remain report‑only unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.

* **CC‑G8‑6 (QD/OEE edition discipline).**
  When QD/OEE surfaces are declared, the bundle/ledger MUST pin the relevant editions and policies (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies, and `TransferRulesRef.edition` when applicable).
  The exact `CharacteristicSpaceRef` and separate `characteristicSpaceDescriptionRef: U.EpistemeRef` are **required iff** cell boundaries / de‑dup rules / parity depend on the space definition. Resolve the pair under A.19:5.1.1.1; neither substitutes for `DescriptorMapRef.edition`.

* **CC‑G8‑7 (Maturity is ordinal/poset).**
  Maturity ladders SHALL be authored as ordinal/poset descriptions with **closed** rung ids (`MaturityRungs`, UTS‑registered) and a declared `ReferencePlane`, and SHALL be published as a citable UTS artefact (editioned; twin‑register safe).
  Rung transitions, when asserted, MUST be justifiable by citable evidence paths (when available).

* **CC‑G8‑8 (Spaces ≠ Maps).**
  `CharacteristicSpace` and `DescriptorMap` SHALL remain distinct kinds; naming and twin‑register discipline must be respected.

* **CC‑G8‑9 (Notational independence).**
  The bundle, ledger, and maturity card SHALL remain notation‑independent (per `E.5.2`); any serialization choice is non‑normative and belongs outside Part‑G core.

* **CC‑G8‑10 (MOO cross‑reference).**
  When a LOG bundle is used to drive or justify a produced selected-set outcome, the record of the producing Work, or the audit artefact, SHOULD cite the controlling mechanism ids (e.g., parity/shipping/refresh artefact ids) and relevant policy pins.

* **CC‑G8‑11 (SoTA‑of‑description trace).**
  If authoring methods (e.g., discovery, clustering, summarisation) materially shaped rule text or rung definitions, the bundle/card SHOULD cite their method description refs (edition‑pinned) to support cross‑stance traceability.

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by a governing-pattern policy pin.

* **Anti‑pattern:** Publishing a bundle that implies a correspondence or receiving-use conclusion without its required grounds, or omits CL/Φ pins required by the actual calibration or named assurance use.
  **Avoid:** retain the actual channel and receiving-use grounds under G.Core:4.2.3, using `G.8:Ext.BridgeReuseWiring` for F.9 reuse. Missing required grounds block the dependent use.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

### G.8:10 - Consequences

* **Positive:** `G.5` receives a stable, citable, selector‑facing artefact without importing rule semantics or threshold logic.
* **Positive:** Pins, crossing references, evidence paths and trigger kinds tell an auditor what grounded the decision and help identify the uses whose checks may need to be reopened.
* **Positive:** The ladder retains its ordinal or partial-order meaning, so a maturity label cannot substitute for the evidence and conditions of admission.
* **Negative:** Requires stricter authoring discipline (UTS publication, pin completeness, explicit wiring).
* **Negative:** Without maintained G.6 paths, a later reader may need more work to recover the cited evidence. Evaluate the resolvable A.10 anchors and their support for the stated use; absence of a graph alone does not lower evidence-support class. If a required basis cannot be recovered, abstain from the dependent use.

### G.8:11 - Rationale

`C.23` defines the rules, `G.4` defines Acceptance and its thresholds, `G.6` supplies path-addressable provenance, and `G.5` defines selection and registry use. A project can cite all four in one auditable package for dispatch without maintaining competing definitions.

### G.8:12 - SoTA-Echoing

These examples illustrate how applications connect decision rules, acceptance thresholds, provenance and set-valued outputs under their respective governing rules:

* **Set-valued selection** retains alternatives when multi-objective or uncertainty conditions do not justify one scalar winner.
* **Quality-Diversity and archive-based evaluation** retain the descriptor, distance and archive-policy editions their evaluation uses, so a telemetry change can be interpreted against that basis. An archive kept solely to preserve evidence needs no QD pins.
* **Open-endedness / curriculum generation** use explicit transfer rules and applicable degrade branches, with telemetry available to refresh orchestration.
* **Reproducible publication** keeps identifiers, editions, policies and traces recoverable for a later application or audit.



### G.8:13 - Relations

**Builds on:** `G.Core`, `C.23`, `G.4`, `G.6`, `G.5`, `C.22`
**Uses:** `A.10` (anchors), `F.8` (policy-id resolvability), `F.9` (cross-semantic relation and bounded-use claims), `F.17`/`E.17` (crossing publication surfaces), `G.7` (when calibration is used), `B.3` (when a separate named assurance use is made), `G.11` (refresh planning/trigger consumption), `G.10` (shipping boundary; if bundled artefacts are shipped), `E.10` (LEX twin registers), `E.5.2` (notation independence), `E.18` (crossing visibility when a selected transformation-flow structure is in use), `A.21` (gate decisions under an applicable profile); optional `C.18` (QD) / `C.19` (E/E‑LOG) when those surfaces are declared.
**Publishes to:** `UTS` (bundle/ledger/card), `G.5` (selector/registry consumption), `G.11` (refresh via typed triggers and pinned telemetry)
**Constrains:** any SoS‑LOG packaging that claims FPF conformance for selector‑facing dispatch across method families.

### G.8:14 - Author’s quick checklist (informative)

* [ ] List the IDs of the applicable C.23 rules in `SoSLogRuleId[]`.
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Every actual sense, kind or plane correspondence retains its relation and receiving-use grounds under G.Core:4.2.3. For F.9 reuse, `G.8:Ext.BridgeReuseWiring` keeps the Bridge, separate bounded-use claim and reliance basis citable. `CL/CL^k/CL^plane` and `Φ/Ψ/Φ_plane` ids and editions are pinned when the calibration or named assurance account requires them; policy ids resolve under `F.8:8.1`.
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] When the bundle binds a QD use, its required descriptor, distance, insertion and emitter definitions are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); the exact space and its separate description-episteme reference are pinned iff cell boundaries/de-dup/parity depend on the space definition; **Spaces ≠ Maps**. `PortfolioMode=Archive` alone does not activate these QD fields.
* [ ] If open-ended surfaces are declared, pin `GeneratorFamilyRowRef`, `TransferRulesRef.edition` and any validity/coupler policies. Handle unknown transfer under the declared C.23 branch: permitted `degrade` after its prerequisites pass, otherwise `abstain`; report unavailable basis and unperformed judgements under C.23:4.2.1.
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

### G.8:End
