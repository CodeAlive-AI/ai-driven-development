## G.0 - Frame Standard and Comparability Governance — CG‑Spec

**Tag.** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage.** *design-time* legality gate (establishes comparison legality & evidence minima; constrains run-time gates)
**Primary output.** `CG‑Spec` — a notation-independent legality gate for a `CG‑Frame`, published to UTS (with explicit edition pins for downstream reproducibility and RSCR).
**Primary hooks.** `USM.ScopeSlice(G)`, `entityOfConcern`, `SCP`, `MinimalEvidence`, `CNSpecRef`, `Γ‑fold`, `Φ(CL)` / `Φ_plane` policy pins, `UTS` publication (Name Cards + edition pins).
**Non-duplication note.** Universal Part‑G invariants are governed by `G.Core` and are satisfied here **only via delegation** (`CC‑G0‑CoreRef` → `CC‑GCORE‑*`). Single‑governing definition CN/CG spec-ref discipline is enforced via `CC‑GCORE‑CN‑CG‑1` (no shadow specs; no competing defaults).

### G.0:1 - Problem frame

A team defines or evolves a `CG‑Frame` (e.g., a frame for creativity measurement, decision quality, architecture trade‑offs, or selected-set publication). Downstream mechanisms (G.1–G.5 and beyond) must compare, aggregate, and publish CHR‑typed observations in ways that are:

* lawful with respect to measurement admissibility (scale/unit/polarity constraints),
* auditable with explicit evidence minima and provenance,
* reproducible via pinned editions and explicit policy ids,
* portable only via explicit crossings (bridges and reference-plane moves), never via implicit semantic leakage.

`CG‑Spec` is the single design-time object that fixes *what comparisons and aggregations are lawful in this frame*, under which pinned assumptions and minimal evidence requirements, so that run-time selection and publication can be audited without inventing new “local legality gates”.

Didactic subtitle: **Design-time rules for safe, auditable comparison.**

### G.0:2 - Problem

Without a single, frame-level legality standard:

* comparisons and aggregations drift into *implicit assumptions* (hidden scalarisation; silent totalisation of partial orders),
* numeric gates run on “whatever is available” rather than declared evidence minima and lane/carrier requirements,
* cross-context reuse happens without explicit crossing visibility and stated losses,
* selection outcomes become hard to audit because legality, evidence minima, and penalty routing are not pinned and traceable.

### G.0:3 - Forces

* **Pluralism vs. comparability.** Multiple traditions must co-exist while allowing admissible comparison where justified.
* **Expressiveness vs. safety.** Rich comparator sets and aggregators vs. measurement admissibility constraints.
* **Locality vs. portability.** Context-local semantics first; portability only via explicit bridges and explicit losses.
* **Assurance vs. agility.** Evidence minima must meet the claim threshold while staying light enough to adopt.
* **Design-time vs. run-time.** Keep legality standards and templates design-time; run-time only cites and applies them.

### G.0:4 - Solution — CG‑Spec as the design-time legality gate

`CG‑Spec` is a **notation-independent** UTS-published object that, for a given `CG‑Frame`, defines:

* the **ComparatorSet** (explicit, finite, typed) permitted in this frame,
* the **ScaleComplianceProfile** (SCP) that constrains lawful operations per characteristic,
* **MinimalEvidence** requirements per characteristic (lanes, carriers, freshness windows, crossing allowances, failure behavior),
* the frame’s **penalty and trust folding wiring** (by explicit policy ids and edition pins),
* **AcceptanceStubs** as design-time templates (thresholds remain governed by CAL, not by CG‑Spec),
* optional method-family hooks (e.g., illumination/QD or explore↔exploit guards) *as wiring only*, with semantics governed by the corresponding patterns.

`CG‑Spec` constrains downstream gate checks by being *referenced and pinned*; it is not itself an admissibility mechanism.

#### G.0:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part-G core invariants; governing-pattern citation)

**GCoreLinkageManifest (normative; size-controlled via profiles/sets).**

Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2`).
Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`
  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
* `CorePinSetIds :=`
  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins`
* `CorePinsRequired :=` *(delta over PinSets)*
  * `UTSRowId[]`
  * `ReferenceMap`
  * `ComparatorSetRef.edition`
  * `SCPRef.edition`
  * `ΓFoldRef.edition?`
  * `MinimalEvidenceRef.edition?`
  * `FailureBehaviorPolicyId?`
* `DefaultsConsumed := {DefaultId.GammaFoldForR_eff}` *(governing definition: `CC‑G5.4` per `G.Core.DefaultGoverningDefinitionIndex`)*
* `RSCRTriggerSetIds := {GCoreTriggerSetId.CGSpecGate}`
* `RSCRTriggerKindIds :=` *(delta over TriggerSets)*
  * `RSCRTriggerKindId.EvidenceSurfaceEdit`
  * `RSCRTriggerKindId.TokenizationOrNameChange`
  * `RSCRTriggerKindId.DefaultGoverningDefinitionChange`
* `TriggerAliasMapRef := ∅`

#### G.0:4.2 - CG‑Spec object model (normative)

`CG‑Spec` is authored per `CG‑Frame`. It SHALL:

* be **published to UTS** as a notation-independent object,
* reference CHR characteristics by id (measurement semantics remain governed by CHR packs),
* constrain what comparisons and aggregations are lawful in this frame via explicit comparator specs and SCP bindings,
* declare minimal evidence gates per characteristic, including explicit failure behavior wiring,
* cite `CN‑Spec` for normalization/comparability policies (no duplication and no shadow specs),
* publish edition pins and policy ids so downstream selection, parity, shipping, and refresh can be reproducible and RSCR-aware.

#### G.0:4.3 - CG‑Spec conceptual model (normative)

```
CG‑Spec :=
⟨
  UTS.id, Edition,
  Context, Purpose, Audience,

  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},

  entityOfConcern := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live},          // only refines ReferencePlane=world; introduces no new planes

  ReferenceMap := minimal map{term/id → UTS|CHR|SoTA-pack refs},

  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,          // CN‑Spec is the governance card (one governing definition)

  Characteristics := [CHR.Characteristic.id…],          // pointers only; authored in G.3 CHR pack

  // Edition-addressable segments (pins MUST be exposed)
  ComparatorSet := ⟨ComparatorSetId, ComparatorSetRef.edition, [ComparatorSpec…]⟩,
  SCP := ⟨SCPId, SCPRef.edition, map Characteristic.id → SCPEntry⟩,
  MinimalEvidence := ⟨MinEvId, MinimalEvidenceRef.edition?, map Characteristic.id → MinEvidenceEntry⟩,  // min pin: CGSpecRef.edition

  Γ‑fold := ⟨GammaFoldId, ΓFoldRef.edition,
             defaultRef := DefaultId.GammaFoldForR_eff,
             override? := ⟨overrideRef, proof_refs, boundary_notes⟩
           ⟩,

  // Penalty routing and plane policies are by explicit policy ids.
  // Semantics (tri-state, penalties→R_eff-only, crossing visibility, set-return) are governed by G.Core.
  CL‑Routing := ⟨policy_id, map Bridge.CL → penalty_spec⟩,
  Φ := ⟨phi_policy_id, phi_table_ref?, psi_policy_id?, phi_plane_policy_id?⟩,

  AcceptanceStubs := [AcceptanceStubId…],     // templates only; thresholds remain governed by CAL (G.4)

  // Optional hooks are wiring-only; semantics are governed by governing definitions.
  E/E‑LOG Guard? := ⟨policy_id, pins…⟩,
  Illumination? := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    DescriptorMapRef.edition?, DistanceDefRef.edition?, DHCMethodRef.edition?,
    InsertionPolicyRef?, PromotionPolicyId?
  ⟩,

  RSCR := ⟨
  RSCRTestId[]?,             // SHOULD cover: illegal_op_refusals; unit and scale legality checks; freshness windows; // partial-order scalarisation refusals; threshold semantics; CL→R_eff routing;
                            // and refusal of degrade.order on unit mismatches (MM‑CHR).
    RSCRTriggerKindId[]
  ⟩,

  Naming := UTS Name Cards (twin labels plus bridge notes),
  PublicIdContinuity := ⟨governing definition, DRR link, refresh cadence, decay and aging policy, deprecations⟩,
  Provenance := ⟨carrier types, SoTA-pack refs, DRR/SCR linkage⟩
⟩
```

**Local typing notes (non-exhaustive; normative intent but no shadow specs).**

* `ComparatorSpec` MUST be typed against SCP/CHR constraints. Examples of lawful comparators are frame-local choices and are authored here (e.g., dominance where lawful; lexicographic over typed traits; medoid/median for ordinal where lawful; explicit weighted sums only where legality is proven and units are aligned).
* `MinimalEvidenceEntry` MUST declare: lane requirements, evidence carriers, freshness window (if any), and explicit failure behavior wiring. The semantics of `{pass|degrade|abstain}` and `degrade(mode=…)` are delegated to `G.Core`.

#### G.0:4.4 - Interfaces (normative)

| Interface          | Consumes                             | Produces / constrains                                                      |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope signals    | `CG‑Spec.Scope`, `entityOfConcern`, `ReferenceMap`                         |
| **G.0‑2 SCP**      | CHR pack refs (G.3), legality proofs | `CG‑Spec.SCP` + bindings to lawful operators/aggregators                   |
| **G.0‑3 Evidence** | SoTA inputs (G.2), carriers (A.10)   | `CG‑Spec.MinimalEvidence`, `Γ‑fold` segment pins, `CL‑Routing`, `Φ` ids    |
| **G.0‑4 Publish**  | All above                            | Versioned `CG‑Spec@UTS` plus Name Cards, public-id continuity records, and RSCR tests and trigger kinds  |
| **G.0‑5 Expose_CrossingHooks** | `CG‑Spec` + crossing/plane/policy pins | GateCrossing inputs for `GateChecks` (`E.18/A.21`): plane checks, lane purity, lexical SD pins |
| **→ G.1**          | `CG‑Spec`                            | Generator guardrails (Comparator/SCP/MinEv pins); degrade/abstain wiring   |
| **→ G.2**          | `CG‑Spec`                            | Harvesting inclusion/exclusion and crossing policy constraints             |
| **→ G.3**          | `CG‑Spec`                            | Required CHR characteristics/scales/operators to exist                     |
| **→ G.4**          | `CG‑Spec`                            | Acceptance templates; evidence minima; Γ‑fold override proof hooks         |
| **→ G.5**          | `CG‑Spec`                            | Eligibility gates and explainability pins (Path/UTS/policy ids)            |
| **→ G.6**          | `CG‑Spec`                            | EvidenceGraph/SCR pinning surface (policy ids + Path/PathSlice discipline) |

#### G.0:4.5 - CG‑Spec authoring chassis (informative)

1. **Charter the frame.** Declare `Context`, `Scope`, `entityOfConcern`, boundary examples/non-examples, and `ReferenceMap`.
2. **Draft ComparatorSet and SCP.** Enumerate permitted comparator forms and bind each to CHR characteristics and legality constraints (scale/unit/polarity discipline). Attach guard bindings as explicit references/pins.
3. **Bind Characteristics.** Ensure every compared quantity is a CHR characteristic id (reuse/mint via UTS discipline).
4. **Declare MinimalEvidence.** For each characteristic: required lanes/carriers, freshness window, crossing allowances (if any), and explicit failure behavior wiring (tri-state semantics delegated to `G.Core`).
5. **Pin trust folding and penalties.** Cite the one governing definition for `DefaultId.GammaFoldForR_eff` unless explicitly overridden with proof refs; publish `Φ`/CL policy ids explicitly.
6. **Publish and register regression tests.** Publish `CG‑Spec@UTS` with edition-pinned segments; register RSCR tests for the frame’s legality surfaces and evidence minima.
7. **Public-id continuity and refresh readiness.** Declare refresh cadence and deprecations with lexical continuity notes; ensure RSCR trigger kinds are emitted as canonical ids.

#### G.0:4.6 - Extensions (pattern-scoped; non-core)

All blocks below are `GPatternExtension` modules (PatternScopeId; not new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SpecRefSurfaces**

* **PatternScopeId:** `G.0:Ext.SpecRefSurfaces`
* **GPatternExtensionId:** `SpecRefSurfaces`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19`
* **Uses:** `{A.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CNSpecRef.edition` (and any CN-side policy ids referenced by `CG‑Spec` fields)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring-only):** `CG‑Spec` SHALL cite CN‑Spec; it SHALL NOT restate normalization/comparability semantics.

**GPatternExtension: BridgeAndCLWiring**

* **PatternScopeId:** `G.0:Ext.BridgeAndCLWiring`
* **GPatternExtensionId:** `BridgeAndCLWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `F.9`
* **Uses:** `{F.9, G.7}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeCardId/BridgeId` (when crossings are permitted)
  * `CL` / `CL^k` and `Φ`/`Φ_plane` policy ids (when penalties are in play)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring-only):** Crossing semantics and penalty routing are delegated to `G.Core`; this module only lists the required pins used by `CG‑Spec` entries.

**GPatternExtension: SoTAPaletteInputs**

* **PatternScopeId:** `G.0:Ext.SoTAPaletteInputs`
* **GPatternExtensionId:** `SoTAPaletteInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoTA-Pack@CG‑Frame` refs used to justify comparator admissibility, evidence minima, and crossing allowances (e.g., claim sheets, operator inventory, bridge matrix ids)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** Any SoTA palette/tradition semantics are governed by `G.2`. `G.0` only requires that `CG‑Spec` entries cite the needed SoTA artefacts for auditability.

**GPatternExtension: QDAndExplorationHooks**

* **PatternScopeId:** `G.0:Ext.QDAndExplorationHooks`
* **GPatternExtensionId:** `QDAndExplorationHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, C.23}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `InsertionPolicyRef?`
  * `FailureBehaviorPolicyId` / SoS‑LOG branch policy id when `degrade(mode=…)` is used
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** `CG‑Spec` may declare optional QD/exploration hooks; semantics remain governed by the referenced method patterns.

### G.0:5 - Archetypal Grounding — Tell–Show–Show; System / Episteme

#### G.0:5.1 - Archetype 1: System comparability under mixed evidence and unit constraints

**Tell.** Two labs compare energy efficiency results of a physical system where measurements use different rigs and units, and some evidence is missing.

**Show (failure without CG‑Spec).** The team averages an ordinal safety rating, mixes units (“kWh” vs “MJ”), and silently treats missing lanes as zeros. Cross-lab reuse happens without explicit bridge and loss notes, so selection becomes a black box.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* pins the lawful comparator(s) (e.g., unit-aligned ratio comparisons only; ordinal comparisons are order-only),
* declares `MinimalEvidence` lanes/carriers and freshness windows per characteristic,
* declares explicit failure behavior wiring (tri-state semantics delegated to `G.Core`),
* exposes crossing pins (bridge ids + CL/policy ids) when reuse across rigs is attempted,
* publishes the pinned editions so parity/refresh can detect drift.

#### G.0:5.2 - Archetype 2: Epistemic comparability for selected-set publication across traditions

**Tell.** A team selects an R&D set using multiple evaluation traditions: safety assurance, cost models, and readiness heuristics.

**Show (failure without CG‑Spec).** The team collapses partial orders into a single score, hides the threshold policy in code, and cannot explain why cross-tradition penalties changed between runs.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* defines a comparator bundle (e.g., Pareto dominance + explicit lexicographic tiebreaks where lawful),
* pins `CNSpecRef.edition` and the editioned segments (`ComparatorSetRef.edition`, `SCPRef.edition`, `MinimalEvidenceRef.edition`),
* makes `AcceptanceStubs` explicit as templates while locating thresholds in CAL (G.4),
* ensures RSCR triggers are emitted when comparator or policy pins change.

### G.0:6 - Bias-Annotation

`CG‑Spec` can encode (and therefore amplify) biases if authored carelessly:

* **Tradition favoritism.** Comparator choices may privilege a tradition’s evidence style; mitigation: require explicit evidence minima and explicit crossing costs, and keep cross-tradition aggregation gated by explicit justifications.
* **Metric gaming and Goodhart effects.** Overemphasis on a single scalar can lead to gaming; mitigation: preserve set-return semantics and require explicit, auditable scalarisations when they are lawful and intended.
* **Hidden thresholds and opaque safety policy.** Embedding acceptance thresholds in prose or code hides value judgments; mitigation: keep thresholds in CAL acceptance clauses and pin policy ids.
* **Scope creep.** Comparisons leak across entityOfConcern or reference planes; mitigation: require explicit `entityOfConcern` and `ReferencePlane` pins and treat plane moves as explicit crossing events.

### G.0:7 - Conformance Checklist (normative)

| ConformanceId | Statement |
| --- | --- |
| **CC‑G0‑CoreRef** | `G.0` is conformant only if the applicable core obligations listed in `G.0:4.1` are satisfied (delegation to `CC‑GCORE‑*`; no shadow specs, no competing defaults, typed RSCR triggers, explicit pins). |
| CC‑G0‑01 | `CG‑Spec` is published as a notation-independent UTS object with explicit `Edition`, `Context`, `Scope`, `entityOfConcern`, and a minimum `ReferenceMap`. |
| CC‑G0‑02 | `CNSpecRef.edition` is present and is treated as an external governance-card reference (no local redefinition of CN semantics). *(Delegation target: `CC‑GCORE‑CN‑CG‑1`.)* |
| CC‑G0‑03 | `ComparatorSet` is explicit and finite; each comparator is typed and bound to `SCP` and referenced CHR characteristics; **anything not enumerated MUST be treated as illegal/abstain by default** (no implicit comparator defaults). |
| CC‑G0‑04 | `SCP` declares, per characteristic, the lawful operation regime needed for each referenced comparator (scale/unit/polarity constraints and any required proofs/refs). |
| CC‑G0‑05 | `MinimalEvidence` is declared per characteristic and includes explicit lane/carrier requirements, freshness window references (if any), and explicit failure behavior wiring (tri-state semantics delegated). If freshness windows are used, a stable window id (e.g., `PathSliceId`) MUST be pinned for audit. |
| CC‑G0‑06 | `Γ‑fold` is present as an edition-pinned segment and either (i) cites `DefaultId.GammaFoldForR_eff` (one governing definition) or (ii) provides an explicit override with proof refs. |
| CC‑G0‑07 | If crossing penalties are used, `CL‑Routing` and `Φ` policy ids are explicit and auditable (policy ids are exposed as pins/refs) **and are required pins for downstream SCR publication on penalised claims** (see `G.6`). |
| CC‑G0‑08 | `AcceptanceStubs` in `CG‑Spec` are templates only; any context-local thresholds/acceptance policies are governed by CAL acceptance artefacts (G.4) and are cited, not duplicated. |
| CC‑G0‑09 | RSCR tests and triggers for edits to legality surfaces and evidence minima are present and use canonical `RSCRTriggerKindId`s. The RSCR test set SHOULD cover at least: illegal_op_refusals; unit and scale legality checks; freshness windows; partial-order scalarisation refusals; threshold semantics; CL→`R_eff` routing; refusal of `degrade.order` on unit mismatches (MM‑CHR). |
| CC‑G0‑10 | `PublicIdContinuity` is declared: governing definition, DRR link, refresh cadence, decay and aging policy, and deprecations. Deprecations preserve lexical continuity (Δ-discipline; delegated to `CC‑GCORE‑ID‑*`). |
| CC‑G0‑11 | *(Conditional)* If `Illumination` / QD hooks are present, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and any `InsertionPolicyRef` / promotion policy ids are pinned (or explicitly marked absent) and are recorded in provenance/audit pins. |
| CC‑G0‑12 | *(Conditional)* If freshness windows influence gating/selection, they are published and enforced, and the relevant window ids (`PathSliceId` or equivalent) are recorded in SCR/audit pins. |
| CC‑G0‑13 | **Pre-flight numeric gates.** Any numeric comparison/aggregation declared in `ComparatorSet` has associated `GateChecks` for unit legality, scale legality, pinned SOP/editions, and declared comparability assumptions; failing any check yields `refuse` or `abstain` (tri-state semantics delegated). |
| CC‑G0‑14 | **GateCrossing hook exposure.** Exports provide `Expose_CrossingHooks` inputs so `GateChecks` (`E.18/A.21`) can validate plane consistency, crossing intent, lane purity, and lexical SD; failures MUST block publication. |
| **CC‑G0‑Φ** | `Φ(CL)` (and `Φ_plane`, if used) is monotone, bounded, and table-backed; policy ids are published; construction preserves `R_eff ≥ 0`. |
| **CC‑G0‑Unknowns** | *Delegated.* Unknown handling MUST follow the tri-state guard semantics `{pass|degrade|abstain}` with no silent coercions. (See `CC‑GCORE‑GUARD‑1`.) |
| **CC‑G0‑CSLC** | Scale/unit/polarity legality MUST be proven before any aggregation; illegal arithmetic on ordinal/nominal values is nonconformant. (Governed by the relevant legality patterns; `G.0` only binds and cites.) |

### G.0:8 - Common Anti-Patterns and How to Avoid Them

* **Anti-pattern: shadow legality gates in downstream code.** Avoid by requiring downstream to cite `CG‑Spec` segments by id+edition.
* **Anti-pattern: “one number to rule them all”.** Avoid by preserving set-return outputs when only partial orders are lawful; any scalarisation must be explicit, typed, and justified.
* **Anti-pattern: thresholds inside CG‑Spec or CHR.** Avoid by keeping thresholds and acceptance logic in CAL and citing from `CG‑Spec` only via stubs/templates.
* **Anti-pattern: implicit crossings.** Avoid by requiring explicit bridge ids, CL/policy ids, and reference-plane pins.

### G.0:9 - Consequences

* **Lawful comparability.** The frame declares exactly what can be compared/aggregated and under what constraints.
* **Auditable selection.** Downstream selectors can justify outcomes via pinned legality surfaces and explicit evidence minima.
* **Explicit portability costs.** Cross-context reuse becomes deliberate and costed via visible crossings and penalties.
* **Lower drift under evolution.** Edition pinning + typed RSCR triggers makes comparability drift detectable and refreshable.

### G.0:10 - Rationale

`CG‑Spec` centralises frame-level comparability constraints so that:

* CHR authorship (G.3) remains about *measurement meaning* rather than implicit thresholds,
* CAL (G.4) governs context-local acceptance/threshold policies and proof ledgers,
* selectors and dispatchers (G.5) remain policy-governed and auditable rather than encoding hidden legality assumptions,
* refresh (G.11) can treat legality edits and pin changes as explicit causes with canonical trigger ids.

### G.0:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in evaluation and governance by:

* treating “abstain / defer” as a first-class outcome rather than forcing a single brittle scalar (cf. selective prediction / abstention and set-valued reporting practices),
* preserving multiobjective / partial-order outputs as sets (Pareto / archive thinking) rather than silently collapsing to a scalar,
* emphasising reproducibility via explicit versioning/pinning of evaluation surfaces (editions) and explicit policy identifiers,
* making evidence minima explicit and auditable (a conceptual analogue of modern reproducibility/robustness checklists and evaluation protocols),
* keeping method-family specifics modular (e.g., QD/archives, open-ended exploration budgets) via explicit wiring to governing patterns rather than embedding method semantics into the universal legality gate.

### G.0:12 - Relations

**Builds on:** `G.Core`, `A.19 (CN‑Spec)`, `A.10 (evidence carriers)`, `A.17–A.19 / C.16 (MM‑CHR legality)`, `A.18 (CSLC)`, `B.3 (trust / Γ‑fold family)`, `F.* (contexts, bridges, CL, UTS)`, `E.10 (lexical rules)`, `E.5.* (notation independence discipline)`.
**Used by:** `G.1` (generator guards), `G.2` (harvesting constraints), `G.3` (required CHR), `G.4` (acceptance templates / proof hooks), `G.5` (eligibility gates), `G.6` (evidence/pin surfaces), and downstream parity/shipping/refresh where `CG‑Spec` is pinned.
**Publishes to:** `UTS` (Name Cards + editioned `CG‑Spec` segments).

### G.0:End

