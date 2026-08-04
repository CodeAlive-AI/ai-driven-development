## G.Core - Part G Core Invariants


**Tag.** Architectural pattern (Part‑G core invariants hub; refactoring/deduplication)
**Stage.** *design‑time* (authoring discipline + ID‑stable citation discipline; no run‑time mechanism)
**Primary hooks.** E.8 (pattern template), E.10 (lexical/ontological rules), E.19 (conformance discipline), A.6.7 (SuiteObligations + suite protocol pins), A.15.3 (planned baseline), A.19 (CN‑Spec), G.0 (CG‑Spec), A.19.CHR (CHR suite boundary), C.23 (SoS‑LOG), F.17 (UTS), F.15 (RSCR).

**Status.** Stable
**Placement.** Part G core section before `G.0` (without renumbering `G.0…G.13`).
**Normativity.** Normative unless explicitly marked informative

**Purpose.** Provide *one governing definition* for Part‑G‑wide invariants (**delegation-first citation and change-control discipline**), plus a typed **RSCR trigger kind catalogue** and a **Default Governing Definition Index**, so Part G can be refactored without semantic drift or public‑ID breakage.

**Phase‑2 constraint.** `G.Core` is the only new Part‑G pattern introduced in Phase‑2; discipline/method/generator specifics remain in `G.x` as `Extensions`, citations to existing governing patterns, or Phase‑3 seeds (appendix) without new Phase‑2 norms.

**Post‑Phase‑2 evolvability policy.** The Phase‑2 restriction above is historical. From Phase‑3 onward, new Part‑G `PatternId`s are permitted when (i) they introduce a genuinely new **kit/pack class** (typically levels `G.2–G.5`), or (ii) they are required to preserve **one governing pattern per wiring extension** and wiring-only separation. Method/discipline/generator specifics SHOULD still default to `GPatternExtension` modules under `G.x:Extensions` (scoped by `PatternScopeId = G.x:Ext.*` and `GoverningPatternId`), rather than adding new Part‑G patterns.

### G.Core:1 - Problem frame

Part G contains patterns for CG‑frame characterization and its downstream artefacts (cards, evidence graphs, bridge surfaces, refresh/shipping orchestration, parity harnesses, dashboards, interop surfaces). In the current spec, several invariants are already present as **suite obligations/protocol norms** and are **reused across Part G**.

*Part‑G‑wide* invariants are governed by `G.Core` so every `G.x` can:

* cite the core invariants rather than restating them, and
* isolate pattern-scoped specifics as `Extensions` without turning each `G.x` into a mixed bag of universal rules, kit surfaces, and method/generator descriptions.

This pattern (`G.Core`) therefore acts as the **deduplication hub** for FPF Part G.

### G.Core:2 - Problem

Without one governing definition for Part‑G‑wide invariants, Part G drifts in at least six recurring ways:

1. **Shadow governing spec refs** emerge: downstream patterns restate CN‑Spec / CG‑Spec constraints, accidentally creating “local specs” that can diverge from the canonical governing spec refs.
2. **Crossing discipline becomes inconsistent**: “crossing events” and “crossing visibility” are described differently across `G.x`, causing ambiguity about what must be pinned (UTS/Path/policy‑ids/editions) and what triggers refresh/regression.
3. **Guard semantics drift**: tri‑state eligibility and “unknown handling” can be reinterpreted in local prose, producing hidden fourth statuses or implicit coercions.
4. **Hidden scalarization appears**: partial orders are silently collapsed into scalars, or totalization is introduced implicitly through “helpful” numeric summaries.
5. **Suite/kit/pack mixing blurs governing-definition assignment**: downstream patterns drift into “governing” what should remain governed by the suite boundary (`A.6.7` and `A.19.CHR`), kit surfaces (each `G.x`), or shipping (`G.10`).
6. **Refactoring breaks public IDs**: CC items and trigger labels become hard to evolve because removing duplicates risks breaking external references.

Part G requires a single place where these invariants and refactoring disciplines live, while keeping Part G patterns modular and method/discipline specifics explicitly separated.

### G.Core:3 - Forces

* **One governing definition vs. usability:** We must centralize universal invariants, but `G.x` must remain readable and pattern-scoped for authors.
* **Delegation-first vs. completeness:** Many norms already have canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, and the relevant Part E patterns. `G.Core` must cite those governing definitions rather than duplicating semantics.
* **Public-id and alias continuity:** Public CC IDs and deprecated trigger labels must remain stable as labels; deduplication must not break citations.
* **Typed change control:** RSCR/refresh must become *id‑based* (catalogued trigger kinds) rather than prose-based “meaning”.
* **Strict distinction:** Keep governing spec refs (CN‑Spec, CG‑Spec), suites, kits/surfaces, policies, planned baselines, audits, and refresh orchestration distinct.
* **Minimal specificity naming:** New IDs must be kind‑suffixed and minimally specific, to reduce semantic lock‑in while remaining precise.
* **Phase‑2 scope discipline:** `G.Core` must not become a container for discipline/method/generator taxonomies; those remain pattern-scoped (`Extensions`), delegated to existing governing patterns, or marked Phase‑3 seeds (appendix) without new Phase‑2 norms.

### G.Core:4 - Solution

`G.Core` establishes Part‑G‑wide invariants as **delegation rules + typed catalogs + authoring discipline**.

#### G.Core:4.1 - Delegation-first citation for Part‑G‑wide invariants

`G.Core` is a *citation hub*, not a “second spec”. For any Part‑G‑wide invariant that already has a governing definition, `G.Core`:

1) standardises naming via `SuiteObligations.*` (A.6.7:4.2), and
2) records where the invariant is governed, so downstream patterns cite rather than restate.

**Delegation table (normative index; no semantic duplication).**

| Obligation handle | Canonical governing definition(s) | Part‑G note |
| --- | --- | --- |
| `transport_declarative_only` + `cg_spec_cite_required_for_numeric_ops` | A.6.7 + A.19 (CN‑Spec) + G.0 (CG‑Spec) + A.19.CHR | CN/CG are *pins*, not copies (“governing spec refs are pins, not copies”). No embedded/shadow governing spec refs. |
| `bridge_only_crossings` | A.6.7 + E.18 | Any cross-Context or cross-plane/kind move is Bridge‑mediated; no implicit crossings. |
| `crossing_visibility_required` | E.18 (CrossingBundle) + A.6.7 | Crossing visibility is a published **CrossingBundle**. `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL surfaces, BridgeCards, CrossingBundle registries, and UTS rows for crossing artefacts) are treated as crossing-bundle edits. If the required CrossingBundle is missing/non‑conformant, downstream consumers MUST **abstain** from cross-Context or cross-plane reuse (no silent crossings). |
| `two_bridge_rule_for_described_entity_change` | A.6.7 | entityOfConcern retargeting requires an explicit KindBridge (`CL^k`) in addition to any Context/Plane Bridge. |
| `guard_decision_tristate(pass|degrade|abstain)` + `unknown_never_coerces_to_pass` | A.6.7 + C.23 | `GuardDecision := {pass|degrade|abstain}` only; `unknown` maps to `degrade`/`abstain` via explicit SoS‑LOG branch/policy pins. |
| `penalties_route_to_r_eff_only` | A.6.7 | Penalties affect the **R lane (R_eff)** only; **F/G invariants** must not be altered by penalties. |
| `no_silent_scalarisation_of_partial_orders` + `no_silent_totalisation` | A.6.7 | Partial orders stay set‑valued; no silent scalar ranks or “helpful” totalisation. |
| `planned_slot_filling_in_work_planning_only` + `finalize_launch_values_in_work_enactment_only` + `gate_decision_separation` | A.15.3 + A.19.CHR + A.6.7 | Planned baselines are WorkPlanning‑only; launch/finalization values are WorkEnactment‑only; planning does not govern GateDecision/DecisionLog semantics. |
| `DefaultGoverningDefinitionIndex.single_governing_definition_per_DefaultId` | this pattern | Any default names exactly one governing definition; `G.Core.DefaultGoverningDefinitionIndex` is an index, not a second spec. |

This pattern also governs four pieces of Part‑G‑wide infrastructure that are **not** already governed elsewhere:

* the typed **RSCRTriggerKindId catalogue** (single writer),
* the **Default Governing Definition Index** (one governing definition per DefaultId; index only), and
* the **Δ‑discipline** for ID‑stable deduplication (delegation without public‑ID breakage), and
* the **linkage compression catalogues** (`GCoreConformanceProfileId`, `GCoreTriggerSetId`, `GCorePinSetId`) used to keep `G.x` linkage sections small.

#### G.Core:4.2 - Mandatory `G.Core linkage` manifest requirement for every `G.x`

Every pattern `G.x` in Part G SHALL include a short, explicit **Core linkage** section that is notation‑independent and id‑based.

* Relations: `Builds on: G.Core`.
* Solution: include a section named `G.x:<n> - G.Core linkage (normative)` that contains a `GCoreLinkageManifest` listing, at minimum:

  * `CoreConformanceProfileIds := { GCoreConformanceProfileId… }` *(preferred)* and/or `CoreConformanceIds := { CC‑GCORE‑… }`
  * `RSCRTriggerSetIds := { GCoreTriggerSetId… }` *(preferred)* and/or `RSCRTriggerKindIds := { RSCRTriggerKindId… }`
  * `CorePinSetIds := { GCorePinSetId… }` *(preferred)* and/or `CorePinsRequired := { … }` *(pins/refs surfaced by the kit; include policy‑id pins and edition pins when applicable; list only additions/overrides if pin sets are used)*
  * `DefaultsConsumed := { DefaultId… }` *(ids only; governing definition is resolved via `G.Core.DefaultGoverningDefinitionIndex`; cite governing definition, don’t restate)*
  * `TriggerAliasMapRef?` *(present or cited) if the pattern uses local trigger tokens*

**Nil‑elision (normative size rule).** Any field whose value is `∅` MAY be omitted; omission means `∅` and does not relax any obligation.

**Expansion rule (normative).** If profile/set ids are used, the effective `CoreConformanceIds` / `RSCRTriggerKindIds` / `CorePinsRequired` are the unions of their expansions plus any explicitly listed ids (see `G.Core:4.2.2`, `G.Core:4.2.3`, and `G.Core:4.3.4.2`).

##### G.Core:4.2.1 - `GCoreLinkageManifest` (canonical shape)

`GCoreLinkageManifest` is the minimal, pattern‑local wiring manifest for citing `G.Core` without duplicating universal prose.

A `G.x` MAY render the manifest as prose, a table, or structured notation, but the ids SHALL be recoverable by authoring review:

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds?: {GCoreConformanceProfileId…},
  CoreConformanceIds?: {CC‑GCORE‑…},
  RSCRTriggerSetIds?: {GCoreTriggerSetId…},
  RSCRTriggerKindIds?: {RSCRTriggerKindId…},
  CorePinSetIds?: {GCorePinSetId…},
  CorePinsRequired?: {…pin ids…},
  DefaultsConsumed?: {DefaultId…},
  TriggerAliasMapRef?: TriggerAliasMapRef
⟩`

##### G.Core:4.2.2 - `GCoreConformanceProfileId` catalogue (compression primitive)

A `GCoreConformanceProfileId` is a stable identifier for a named set of `CC‑GCORE‑*` items. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

| GCoreConformanceProfileId | Expands to `CC‑GCORE‑*` (set) | Notes |
| --- | --- | --- |
| `GCoreConformanceProfileId.PartG.AuthoringBase` | `{CC‑GCORE‑CN‑CG‑1, CC‑GCORE‑CROSS‑1, CC‑GCORE‑PEN‑1, CC‑GCORE‑SET‑1, CC‑GCORE‑P2W‑1, CC‑GCORE‑DEF‑1, CC‑GCORE‑TRIG‑1, CC‑GCORE‑TRIG‑2, CC‑GCORE‑TRIG‑3, CC‑GCORE‑TRIG‑4, CC‑GCORE‑ID‑1, CC‑GCORE‑ID‑2, CC‑GCORE‑LINK‑1, CC‑GCORE‑LINK‑2}` | Default baseline for most Part‑G kits. |
| `GCoreConformanceProfileId.PartG.TriStateGuard` | `{CC‑GCORE‑GUARD‑1}` | Add when the kit defines/consumes eligibility/guard outcomes. |
| `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` | `{CC‑GCORE‑UTS‑1}` | Add when the kit mints/evolves public ids (UTS rows). |
| `GCoreConformanceProfileId.PartG.ShippingBoundary` | `{CC‑GCORE‑SKP‑1}` | Add when shipping boundaries are in scope for the kit. |

##### G.Core:4.2.3 - `GCorePinSetId` catalogue (compression primitive)

A `GCorePinSetId` is a stable identifier for a named set of commonly recurring **pin obligations** used in Part‑G kits. It exists solely to reduce repetition in `G.x` linkage sections (no new semantics).

**Conditional pins (normative).** In pin‑set expansions below, a pin marked with `?` is **conditional**: it **MUST** be present iff the pattern actually uses the corresponding surface/artefact class; otherwise it MAY be omitted (nil‑elision permitted) and is treated as `∅`. A `G.x` MAY strengthen a conditional pin to unconditional by listing it explicitly in `CorePinsRequired`.

| GCorePinSetId | Expands to `CorePinsRequired` (set) | Notes |
| --- | --- | --- |
| `GCorePinSetId.PartG.AuthoringMinimal` | `{CG-FrameContext, entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩, CNSpecRef.edition, CGSpecRef.edition}` | Baseline scope+spec pins for most Part‑G authoring kits (design‑time, citable, refreshable). |
| `GCorePinSetId.PartG.CrossingVisibilityPins` | `{BridgeId/BridgeCardId, BridgeMatrixId?, CL/CL^k/CL^plane, Φ/Ψ/Φ_plane policy-ids, CrossingBundleId?, UTSRowId[]?, PathId[]/PathSliceId[]?}` | Use when the kit asserts or consumes crossings (Bridge‑only + visible). Conditional pins cover “only if that bundle is used” cases (UTS publication, path‑citable evidence, explicit CrossingBundle reference). |

#### G.Core:4.3 - RSCR Trigger Catalogue and docking discipline

`G.Core` is the **single writer** for Part‑G‑wide trigger kinds.

##### G.Core:4.3.1 - Definitions

* **RSCRTriggerKindId**
  Canonical, stable identifier for a *trigger kind* (a class of “why RSCR/refresh must fire”). Cross-pattern reason code.

* **RSCRTriggerAliasId**
  Pattern-scoped human label/token kept for ergonomics and alias continuity (e.g., `G.11:T4`, `G.6:H3:lane-tag correction`).

* **TriggerAliasMap**
  Mapping table: `RSCRTriggerAliasId → {RSCRTriggerKindId…}` (1..n).

* **RSCRTrigger**
  Minimal conceptual form (notation-independent):

  ```
  RSCRTrigger := ⟨
    triggerKindId: RSCRTriggerKindId,
    scope: PathSliceId[] | PathId[] | PatternScopeId,
    payloadPins: { …id pins… }
  ⟩
  ```

  Where `payloadPins` contains any edition pins, policy-ids, Bridge ids, evidence pins, regression-set ids, etc., required to make the trigger actionable.

##### G.Core:4.3.2 - Governing-definition model

* TriggerGoverningDefinition := `G.Core`.
* Any new trigger kind SHALL be added to `G.Core` first.
* Other patterns MAY define aliases only (or cite shared alias maps), and MUST map aliases to canonical kinds.

##### G.Core:4.3.3 - Authoring rules

* **No implicit triggers:**
  Any RSCR/SCR/refresh artefact that *records reasons* MUST record canonical `RSCRTriggerKindId`. Aliases may be recorded as labels, but must not be the only reason code.

* **No implicit overloading:**
  A local token string (e.g., `T4`) SHALL NOT silently change meaning across patterns; namespace is part of the alias (`G.11:T4` ≠ `A.20:T4`).

* **Granularity discipline:**
  If a local cause is narrower than an existing canonical kind, map it to that kind and keep the nuance as a local scope note. If the difference matters for planning/selection, add a new canonical kind.

* **Multi-cause discipline:**
  When an event spans multiple canonical kinds, record multiple triggers (preferred) or map the alias to a set `{…}` and require emitting the full set.

##### G.Core:4.3.4 - Seed canonical catalogue (Phase‑2 minimum)

The Phase‑2 stabilized canonical catalogue (based on the Phase‑2 inventory; sufficient to dock deprecated `G.6:H3` and `G.11:T0…T7` trigger labels and to populate `RSCRTriggerKindIds` in `G.0…G.13`):

* `RSCRTriggerKindId.LegalitySurfaceEdit`
* `RSCRTriggerKindId.PenaltyPolicyEdit`
* `RSCRTriggerKindId.CrossingBundleEdit`
* `RSCRTriggerKindId.ReferencePlaneEdit`
* `RSCRTriggerKindId.EditionPinChange`
* `RSCRTriggerKindId.TokenizationOrNameChange`
* `RSCRTriggerKindId.PolicyPinChange`
* `RSCRTriggerKindId.TelemetryDelta`
* `RSCRTriggerKindId.FreshnessOrDecayEvent`
* `RSCRTriggerKindId.EvidenceSurfaceEdit`
* `RSCRTriggerKindId.MaturityRungChange`
* `RSCRTriggerKindId.BaselineBindingEdit`
* `RSCRTriggerKindId.DefaultGoverningDefinitionChange`

##### G.Core:4.3.4.1 - Canonical kind definitions (normative, minimal)

Each `RSCRTriggerKindId` SHALL have a short, stable definition in `G.Core` (single-writer) to prevent semantic drift.

| RSCRTriggerKindId | Minimal meaning (cause class) | Typical payload pins (non-exhaustive) |
| --- | --- | --- |
| `RSCRTriggerKindId.LegalitySurfaceEdit` | A legality surface changed (CG‑Spec: ComparatorSet/SCP/Γ_fold/MinimalEvidence, or equivalent legality inputs). | `CGSpecRef.edition`, `ComparatorSetRef.edition`, `SCPRef.edition`, `ΓFoldRef.edition` |
| `RSCRTriggerKindId.PenaltyPolicyEdit` | A penalty / Φ / Ψ / FailureBehavior / SoS‑LOG branch policy changed. | penalty policy ids, `Φ`/`Ψ` policy ids, SoS‑LOG branch id pins |
| `RSCRTriggerKindId.CrossingBundleEdit` | A crossing bundle changed (Bridge/CL routing, crossing-bundle registry cards, crossing policy pins), including `edition_key` changes of crossing‑relevant artefacts (BridgeCards, CrossingBundle registries, UTS rows for crossing artefacts). | `BridgeId/BridgeCardId`, `BridgeMatrixId?`, `CL*` ids, crossing policy ids, `UTSRowId[]`, `PathId/PathSliceId?` |
| `RSCRTriggerKindId.ReferencePlaneEdit` | ReferencePlane or plane-routing surface changed. | `ReferencePlaneId`, plane-policy ids |
| `RSCRTriggerKindId.EditionPinChange` | Any pinned edition relevant to downstream artifacts changed (including **`CNSpecRef.edition`**, `CGSpecRef.edition`, comparator/method/descriptor/distance/etc.). Crossing‑artefact edition_key changes are additionally classified as `CrossingBundleEdit` per multi‑cause discipline. | changed `*.edition` pins, affected `PathSliceId`s |
| `RSCRTriggerKindId.TokenizationOrNameChange` | A published tokenization / naming / alias surface changed in a way that can affect docking, citations, or dispatch (e.g., UTS Name Cards, twin labels, alias maps). | affected `UTSRowId[]`, `NameCardId[]`, alias ids / maps |
| `RSCRTriggerKindId.PolicyPinChange` | A policy-id pin used by characterization changed (selection, insertion, emission, routing, refresh policy, etc.). | policy ids (and other non-edition configuration pins when they are explicitly pinned) |
| `RSCRTriggerKindId.TelemetryDelta` | Telemetry inputs that influence refresh/selection changed (not merely display-only). | telemetry ids/refs, `Audit`-published pins |
| `RSCRTriggerKindId.FreshnessOrDecayEvent` | Time/freshness/decay conditions affecting validity changed (window shift, decay thresholds, freshness policy edits). | freshness window refs/ids, decay/freshness policy ids |
| `RSCRTriggerKindId.EvidenceSurfaceEdit` | Evidence graph / evidence surface changed in ways that affect admissibility/acceptance/comparison. | evidence pins, `EvidenceGraph` refs, affected `PathId`s |
| `RSCRTriggerKindId.MaturityRungChange` | Maturity rung/ladder state changed for relevant artifacts or paths. | maturity rung ids, affected scopes |
| `RSCRTriggerKindId.BaselineBindingEdit` | Planned baseline bindings changed (planned slot fillings / binding refs), requiring a re-run along the P2W path. | `SlotFillingsPlanItem` refs, planned pins, variance pins |
| `RSCRTriggerKindId.DefaultGoverningDefinitionChange` | The governing definition of a `DefaultId` (as recorded in `G.Core.DefaultGoverningDefinitionIndex`) changed, or a default row was added/deprecated. | affected `DefaultId.*`, old governing definition ref, new governing definition ref |

##### G.Core:4.3.4.2 - Canonical trigger sets (compression primitive)

`GCoreTriggerSetId` identifies a named set of `RSCRTriggerKindId` values. A `G.x` MAY cite trigger sets in `RSCRTriggerSetIds` instead of repeating long `RSCRTriggerKindIds` lists.

| GCoreTriggerSetId | RSCRTriggerKindIds (set) | Notes |
| --- | --- | --- |
| `GCoreTriggerSetId.CGSpecGate` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers CG‑Spec legality‑gate kits (e.g., `G.0`). |
| `GCoreTriggerSetId.SoTAHarvestSynthesis` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}` | Covers SoTA harvesting/synthesis packs (e.g., `G.2`). |
| `GCoreTriggerSetId.EvidenceGraphKit` | `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers EvidenceGraph/SCR kits (e.g., `G.6`). |
| `GCoreTriggerSetId.BridgeCalibrationKit` | `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.BaselineBindingEdit}` | Covers bridge calibration/CL kits (e.g., `G.7`). |
| `GCoreTriggerSetId.RefreshOrchestration` | `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.BaselineBindingEdit}` | Covers refresh orchestration (e.g., `G.11`). |

##### G.Core:4.3.5 - Initial alias maps

These alias maps are normative docking artefacts and preserve deprecated alias labels while moving semantics to canonical ids.

**TriggerAliasMap.G11**
Based on the existing trigger catalogue in `G.11` (`T0…T7`).

* `G.11:T0 → { RSCRTriggerKindId.PolicyPinChange }`
* `G.11:T1 → { RSCRTriggerKindId.TelemetryDelta }`
* `G.11:T2 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T3 → { RSCRTriggerKindId.EditionPinChange }`
* `G.11:T4 → { RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.11:T5 → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.11:T6 → { RSCRTriggerKindId.MaturityRungChange }`
* `G.11:T7 → { RSCRTriggerKindId.PolicyPinChange }`

**TriggerAliasMap.G0 (reserved; empty in Phase‑2).**
Map any stable deprecated registry-hook labels emitted/recorded by `G.0` to the canonical kinds above (typically `LegalitySurfaceEdit`, `PenaltyPolicyEdit`, `CrossingBundleEdit`, `ReferencePlaneEdit`, `TokenizationOrNameChange`), preserving the original label text as `RSCRTriggerAliasId`. If none exist, `G.0` SHOULD emit canonical `RSCRTriggerKindId` values directly.

**TriggerAliasMap.G6**
EvidenceGraph `H3` example causes → canonical kinds:

* `G.6:H3:freshness/decay change → { RSCRTriggerKindId.FreshnessOrDecayEvent }`
* `G.6:H3:Bridge CL/CL^k or loss update → { RSCRTriggerKindId.CrossingBundleEdit }`
* `G.6:H3:Φ/Ψ policy change → { RSCRTriggerKindId.PenaltyPolicyEdit }`
* `G.6:H3:lane tag correction → { RSCRTriggerKindId.EvidenceSurfaceEdit }`
* `G.6:H3:ReferencePlane correction → { RSCRTriggerKindId.ReferencePlaneEdit }`
* `G.6:H3:QD/OEE artefact updates (U.DescriptorMapRef.edition/DistanceDef, EmitterPolicyRef, InsertionPolicyRef, archive K-capacity) → { RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange }`

#### G.Core:4.4 - Default Governing Definition Index

`G.Core` provides an index of Part‑G defaults with **one governing definition** per `DefaultId`. The index is not a “second spec”; it is a cross-reference table that points to the *governing definition reference* (a CC item, policy‑id, or TaskSignature rule) and states applicability conditions.

##### G.Core:4.4.1 - Definitions

* **DefaultId**
  Stable identifier of a default (a default constant or default rule).

* **DefaultGoverningDefinitionRef**
  A reference to the governing definition of the default (e.g., a CC item id like `CC‑G5.23`, or a policy id, or a TaskSignature rule definition).

##### G.Core:4.4.2 - Rules

* Exactly one governing definition per `DefaultId`.
* Any other mention in `G.x` MUST be a citation/delegation to the governing definition, not a competing statement.
* A default may be conditional (default-rule) with explicit applicability conditions.
* The Default Governing Definition Index SHALL NOT be used to “smuggle” mandatory invariants as defaults. Invariants remain invariants (typically cited through `CC‑GCORE‑…` and their canonical governing definitions).

##### G.Core:4.4.3 - Seed Default Governing-definition assignment entries (Phase‑2 minimum)

| DefaultId                       | DefaultGoverningDefinitionRef                                           | Notes |
| ------------------------------ | --------------------------------------------------------- | ----- |
| `DefaultId.PortfolioMode`       | `CC‑G5.23`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.DominanceRegime`     | `CC‑G5.28`                                                | Existing governing definition; other mentions delegate to it. |
| `DefaultId.GammaFoldForR_eff`   | `CC‑G5.4`                                                 | Default Γ‑fold for `R_eff` is weakest‑link; overrides require explicit CAL support. |

This table may grow over time; the rule is that the **governing definition must already be named** (or be intentionally set to `G.Core` when the default is truly Part‑G‑wide and not governed elsewhere). Any change in a row (add/remove/change governing definition) SHALL be treated as a refresh‑sensitive edit and recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange` (payload: affected `DefaultId.*`, old governing definition ref, new governing definition ref).

#### G.Core:4.5 - ID continuity protocol (Δ‑discipline)

When moving universal norms out of `G.x` into `G.Core`:

* existing public CC ids in `G.x` that may be referenced externally SHALL NOT be deleted or renamed;
* such CC items SHALL become **delegation** items that point to the relevant `CC‑GCORE‑…` item(s);
* each `G.x` SHALL add exactly one bridge CC item `CC‑Gx‑CoreRef` (first in its CC list) that makes linked `CC‑GCORE‑…` items mandatory for `G.x` conformance.

Deprecated trigger labels (e.g., `G.11:T*`, `G.6:H3:*`) are preserved as aliases and MUST map to canonical trigger kinds.

Non-CC public identifiers (e.g., `UTSRowId`, `RSCRTriggerAliasId`, deprecation notices, edition bumps) MUST obey the same Δ-discipline: preserve old ids; represent drift via alias/deprecation/edition evolution (see `F.17 (UTS)`); and emit canonical trigger kinds (`RSCRTriggerKindId.TokenizationOrNameChange`, `RSCRTriggerKindId.EditionPinChange`) when downstream impact is possible.

#### G.Core:4.6 - Explicit non-goals

`G.Core` does not:

* introduce CG‑frame kit entities (e.g., BridgeMatrix/ReferencePlane/Φ registries); those remain in their governing `G.x`;
* introduce method-family taxonomies, discipline packs, or generator orchestration mechanisms; those remain as `Extensions` in their governing definitions (e.g., synthesis/shipping/refresh patterns);
* define refresh algorithms; it defines trigger kinds and docking only.

---

### G.Core:5 - Archetypal grounding

**Tell.**
In Phase‑2 refactoring, `G.Core` is the hub that allows each `G.x` to become structurally predictable: (a) a short, normative “Core linkage” slice, and (b) pattern‑scoped `Extensions`. Universal obligations cite canonical governing definitions such as `A.6.7`, `A.15.3`, `A.19`, `G.0`, and `A.19.CHR`, while RSCR trigger kinds and `DefaultGoverningDefinitionRef` references become typed and cite named definitions.

**Show 1: Refresh triggers without semantic drift.**
`G.11` already uses trigger tokens `T0…T7`. `G.Core` keeps them as aliases and maps them to canonical trigger kinds (e.g., `TelemetryDelta`, `EditionPinChange`, `CrossingBundleEdit`). This makes RSCR reason codes consistent across patterns and avoids re-explaining trigger semantics in every pattern.

**Show 2: Resolving competing defaults.**
If multiple patterns imply a default for `PortfolioMode`, the Default Governing Definition Index points to one governing definition (currently `CC‑G5.23`). Other patterns (e.g., bundles/log patterns) must cite that governing definition or delegate to it, rather than restating the default with slightly different wording. This preserves intent while preventing drift and ambiguity.

### G.Core:6 - Bias-annotation (informative)

* **Centralization bias:** One governing hub can become too thick. Mitigation: delegation-first citation; keep only true Part‑G invariants and typed indices here.
* **Over-typing bias:** A trigger catalogue can become overly granular. Mitigation: granularity discipline + scope notes; only add new kinds when planning/selection needs it.
* **Refactor rigidity bias:** Preserving IDs can feel cumbersome. Mitigation: delegation items preserve IDs while enabling deduplication.
* **Default absolutism bias:** Defaults may require conditional rules. Mitigation: Default Governing Definition Index allows conditional default rules with explicit applicability conditions.
* **Single-writer bias:** prefers single‑writer *authoring* for catalogs and explicit governing-definition tables.
  *Mitigation:* delegation-first citation; keep catalogs minimal; avoid “second specs”.
* **Architectural bias:** centralizes invariants to prevent accidental coupling across `G.x`.
  *Mitigation:* keep core thin; force `Extensions` to remain pattern‑scoped.
* **Ontological/epistemic bias:** enforces strict distinction between governing spec refs, kits, mechanisms, and orchestration.
  *Mitigation:* allow didactic scope notes while keeping normative surface id‑based.
* **Pragmatic bias:** adds authoring overhead (linkage sections, alias maps).
  *Mitigation:* one small mandatory bridge CC item per pattern (`CC‑Gx‑CoreRef`) and short linkage slices only.
* **Didactic bias:** risks “glossy hub prose” that hides missing CC coverage.
  *Mitigation:* enforce CC/Solution coherence (E.19) and keep invariants checkable via `CC‑GCORE‑…`.

### G.Core:7 - Conformance checklist (normative) — **CC‑GCORE**

Conformance items are authoring obligations and are enforced transitively by `CC‑Gx‑CoreRef` in every `G.x`.

| ConformanceId        | Statement |
| -------------------- | --------- |
| **CC‑GCORE‑DEL‑1**   | A conforming `G.Core` SHALL be delegation-first: if a norm is already governed by `A.6.7`, `A.15.3`, `A.19`, `G.0`, `A.19.CHR`, or a relevant Part E pattern, `G.Core` cites that governing definition rather than duplicating semantics. |
| **CC‑GCORE‑CN‑CG‑1** | Any pattern in Part G that builds on `G.Core` SHALL cite `CN‑Spec` and `CG‑Spec` as the only spec-legality surfaces and SHALL NOT introduce shadow specs (incl. complying with `SuiteObligations.transport_declarative_only` and `SuiteObligations.cg_spec_cite_required_for_numeric_ops`). |
| **CC‑GCORE‑OBL‑1**   | A conforming `G.Core` SHALL treat the obligation vocabulary in `A.6.7:4.2` as the canonical naming surface for Part‑G‑wide obligations and SHALL NOT introduce competing obligation names for the same norms. |
| **CC‑GCORE‑CROSS‑1** | A Part‑G pattern that introduces or consumes crossings SHALL enforce `SuiteObligations.bridge_only_crossings` and `SuiteObligations.crossing_visibility_required` (CrossingBundle per E.18); SHALL prohibit implicit crossings; SHALL treat `edition_key` changes on **crossing‑relevant artefacts** (Bridge/CL/CrossingBundle registries and UTS rows for crossing artefacts) as `RSCRTriggerKindId.CrossingBundleEdit` (and, when an edition pin is involved, also `RSCRTriggerKindId.EditionPinChange` per multi‑cause discipline); and SHALL cite `SuiteObligations.two_bridge_rule_for_described_entity_change` through its canonical governing definition. |
| **CC‑GCORE‑GUARD‑1** | A Part‑G pattern SHALL treat `GuardDecision := {pass|degrade|abstain}` as the only admissibility/eligibility decision domain (`SuiteObligations.guard_decision_tristate(pass|degrade|abstain)`); `unknown` SHALL NOT silently coerce to `pass` (`SuiteObligations.unknown_never_coerces_to_pass`); “sandbox/probe‑only” SHALL be expressed via SoS‑LOG branch pins (policy/FailureBehavior) (see `C.23`), not as an extra decision value. |
| **CC‑GCORE‑PEN‑1**   | A Part‑G pattern SHALL route penalties/assurance loss to the **R lane (`R_eff`) only** (`SuiteObligations.penalties_route_to_r_eff_only`) and SHALL preserve **F/G invariants** under penalties (penalties do not alter legality/invariant lanes). |
| **CC‑GCORE‑SET‑1**   | A Part‑G pattern SHALL preserve set-return semantics for partial orders and SHALL prohibit silent scalarization/totalization (`SuiteObligations.no_silent_scalarisation_of_partial_orders`, `SuiteObligations.no_silent_totalisation`); any scalar summary SHALL be report-only unless declared as a admissible comparator surface. |
| **CC‑GCORE‑SKP‑1**   | A Part‑G pattern SHALL preserve the suite/kit/pack distinction (A.19.CHR) and SHALL keep shipping concerns governed by their canonical governing patterns (e.g., G.10) rather than embedding shipping semantics into unrelated kits or core invariants. |
| **CC‑GCORE‑P2W‑1**   | A Part‑G pattern that uses planned baselines SHALL anchor them via `SlotFillingsPlanItem` in WorkPlanning (`SuiteObligations.planned_slot_filling_in_work_planning_only`) and SHALL finalize launch values only in WorkEnactment (`SuiteObligations.finalize_launch_values_in_work_enactment_only`); gate decisions remain separated per `SuiteObligations.gate_decision_separation`. |
| **CC‑GCORE‑LINK‑1**  | Every conforming `G.x` SHALL satisfy `G.Core:4.2` by providing a `G.x:<n> - G.Core linkage (normative)` section containing a `GCoreLinkageManifest` (incl. either `CoreConformanceProfileIds` or `CoreConformanceIds`, either `RSCRTriggerSetIds` or `RSCRTriggerKindIds`, and either `CorePinSetIds` or `CorePinsRequired` (or both)). Nil‑elision is permitted for `∅` fields. |
| **CC‑GCORE‑LINK‑2**  | Every conforming `G.x` SHALL include `CC‑Gx‑CoreRef` as the first checklist item; it SHALL make mandatory the effective `CoreConformanceIds` (including expansions of any `CoreConformanceProfileIds`) declared in the linkage manifest. |
| **CC‑GCORE‑UTS‑1**   | If a Part‑G pattern mints, deprecates, or evolves any public identifier, it SHALL publish/update the corresponding UTS entries and cite them via `UTSRowId` pins, delegating UTS semantics (twin labels, alias/deprecation discipline, edition pins) to its canonical governing definition `F.17 (UTS)`. |
| **CC‑GCORE‑ID‑1**    | When deduplicating, existing public CC ids in `G.x` SHALL NOT be deleted/renamed; they SHALL become delegation items to relevant `CC‑GCORE‑…` items. |
| **CC‑GCORE‑ID‑2**    | Public id continuity applies beyond CC item ids: `UTSRowId` rows, `RSCRTriggerAliasId` tokens (e.g., `T0…T7`), deprecation notices, and edition bumps SHALL preserve prior ids and express drift via alias/deprecation/edition evolution (never by reusing/redefining an old id). When downstream behaviour can change, the change SHALL emit a canonical `RSCRTriggerKindId` (e.g., `TokenizationOrNameChange`, `EditionPinChange`). |
| **CC‑GCORE‑TRIG‑1**  | A conforming `G.Core` SHALL define the canonical `RSCRTriggerKindId` catalogue and SHALL be its single writer. |
| **CC‑GCORE‑TRIG‑2**  | Any `G.x` that uses local trigger tokens SHALL provide (or cite) a `TriggerAliasMap` mapping each alias to canonical `RSCRTriggerKindId`. |
| **CC‑GCORE‑TRIG‑3**  | Any artefact that records RSCR/SCR/refresh reasons SHALL record canonical `RSCRTriggerKindId` (aliases may be recorded as labels only). |
| **CC‑GCORE‑TRIG‑4**  | A conforming `G.Core` SHALL keep `TriggerAliasMap.*` consistent with the governing patterns’ deprecated trigger alias catalogues (e.g., `G.11:T*`). Any change to an alias mapping SHALL be treated as refresh‑sensitive; at minimum it SHALL be recorded/emitted as `RSCRTriggerKindId.TokenizationOrNameChange` (and, if the mapped trigger kinds change, the corresponding canonical kinds apply as well). |
| **CC‑GCORE‑DEF‑1**  | A conforming `G.Core` SHALL maintain a Default Governing Definition Index for Part‑G defaults, ensuring each `DefaultId.*` names exactly one governing definition (a CC item or a policy id). All other patterns SHALL cite the governing definition and SHALL NOT state competing defaults. Any governing-definition change MUST be recorded as `RSCRTriggerKindId.DefaultGoverningDefinitionChange`. |

### G.Core:8 - Common anti-patterns and how to avoid them

* **Anti-pattern:** Restating CN‑Spec/CG‑Spec rules inside a `G.x` “for convenience”.
  **Avoid:** cite `A.19` and `G.0` through `CC‑GCORE‑CN‑CG‑1`.

* **Anti-pattern:** Adding a fourth guard status (“unknown”, “maybe”, “probe-only”) as a separate decision value.
  **Avoid:** keep guard domain tri‑state; express “probe-only” as policy/branching and record via pins/audit.

* **Anti-pattern:** Treating mandatory invariants as “defaults” to centralize them.
  **Avoid:** keep invariants as invariants (CC‑GCORE‑* cited through canonical governing definitions); restrict the Default Governing Definition Index to true defaults (constants or conditional default-rules).

* **Anti-pattern:** Turning partial orders into scalar ranks silently.
  **Avoid:** keep set‑valued semantics unless a total order is explicitly declared by a comparator/policy.

* **Anti-pattern:** Competing defaults scattered across multiple patterns.
  **Avoid:** Default Governing Definition Index; delegate duplicate statements to the one governing definition.

* **Anti-pattern:** Local trigger tokens without canonical mapping.
  **Avoid:** provide/cite a `TriggerAliasMap` with namespace‑qualified aliases.

* **Anti-pattern:** Breaking public CC ids during dedup.
  **Avoid:** convert to delegation items; preserve IDs.

### G.Core:9 - Consequences

* **Positive:** Part‑G‑wide invariants cite `G.Core` as their governing definition; refactors become safer and easier to audit.
* **Positive:** RSCR becomes reason-code driven (typed triggers), improving traceability and preventing semantic drift.
* **Positive:** Default conflicts become detectable and resolvable because each `DefaultId` names one governing definition.
* **Negative:** Adds an extra authoring step (linkage sections and CoreRef CC item) to each `G.x`.
* **Negative:** Requires careful governance of the trigger catalogue to avoid excessive fragmentation.

### G.Core:10 - Rationale

Universalization of Part G requires a stable "gravity center" for invariants, otherwise each pattern becomes a competing governing source. Delegation-first citation prevents duplication and makes governing-definition assignment explicit, while typed trigger kinds and the Default Governing Definition Index turn historically prose-driven drift into checkable, id-based structure.

### G.Core:11 - SoTA alignment (informative)

Although FPF is conceptual (not a data governance framework), `G.Core` aligns Part‑G authoring with modern best practice patterns seen across post‑2015 work:

* **Selective prediction / abstention** informs tri‑state guard discipline: abstaining or degrading is a first-class outcome, not an error coerced into a scalar.
* **Set-valued / conformal methods** motivate set-return semantics: when comparability is partial or uncertainty is structural, returning sets/regions is often the SoTA-friendly representation.
* **Multiobjective optimization and quality-diversity** reinforce declared set-result and `Archive` semantics instead of forced “best single scalar”.
* **Monotone constrained modelling** (where used) supports “legality-first” scoring/aggregation: constraints and admissibility precede optimization, mirroring CG‑Spec gate discipline.
* **Schema evolution and contract testing** motivate id-stable conformance points and typed trigger catalogues: stable identifiers + regression hooks are the practical mechanism for safe refactoring.

### G.Core:12 - Relations

* **Builds on:**

  * `E.8` pattern template and section discipline
  * `E.10` lexical/ontological rules (strict distinction; twin naming; kind‑suffix discipline)
* `E.18` CrossingBundle (crossing visibility bundle)
  * `E.19` conformance discipline
  * `A.6.7` SuiteObligations + suite protocol pins (delegation support)
  * `A.15.3` SlotFillingsPlanItem (planned baseline anchor)
  * `A.19` CN‑Spec governance card
  * `G.0` CG‑Spec legality gate
  * `A.19.CHR` CHR suite boundary and "governance cards and legality gates are cited as pins, not copied locally" discipline
  * `C.23` SoS‑LOG (tri‑state branches; sandbox/probe‑only)
  * `F.17` UTS (identifier registry; alias/deprecation discipline)
  * `F.15` RSCR (regression/conformance loop)

* **Used by:**

  * `G.0…G.13` patterns (each adds `Builds on: G.Core`, linkage section, CoreRef CC item)

* **Constrains:**

  * Part‑G authoring: no shadow specs, no silent scalarization, tri‑state guards, penalties routing, typed RSCR causes, defaults with one governing definition, and ID‑continuity refactors.

### G.Core:End

