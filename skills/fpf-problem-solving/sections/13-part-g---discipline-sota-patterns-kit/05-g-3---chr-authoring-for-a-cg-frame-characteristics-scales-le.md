## G.3 - CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates

**Tag.** Architectural pattern (CHR kit; publishes lawful measurement primitives; constrains CAL authoring and selector/dispatch use)
**Stage.** *design‑time* (authoring & publication; enables admissible run-time consumption by `G.4` / `G.5`)
**Primary output.** `CHR Pack@CG‑Frame` — a notation‑independent, UTS‑published CHR bundle that provides: typed Characteristics/Scales/Levels/Coordinates, legality + guard surfaces, aggregation/comparison specs, RSCR hooks/tests, and provenance pins.
**Primary hooks.** `G.1` (CG‑FrameContext), `G.2` (SoTA synthesis inputs), `A.19.CHR` (CHRMechanismSuite boundary + pins), `A.15.3` (SlotFillingsPlanItem baseline), `A.18/C.16` (MM‑CHR legality), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4` (trust, freshness/decay), `A.10` (provenance anchors/carriers), `G.6` (EvidenceGraph/Path citation), optional `C.18 and C.19` (QD/OEE wiring), `G.11` (refresh orchestration).
**Non‑duplication note.** Universal Part‑G invariants (bridge‑only crossings, tri‑state semantics, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, linkage discipline) are governed by `G.Core`. This pattern cites them via `G.3:4.1` and delegates where needed.

### G.3:1 - Problem frame

A team is defining or evolving a `CG‑Frame` (via `G.1`) and has plural, competing SoTA traditions and constructs (via `G.2`). The team needs a *admissibility-ready CHR publication* that makes downstream work possible without hidden semantic drift:

* **CAL authoring (`G.4`)** needs typed, admissible operands and guard/legality surfaces to build admissibility and acceptance rules (thresholds and policy cut‑offs remain governed by CAL).
* **Selector/dispatch (`G.5`)** needs CHR‑typed quantities and explicit provenance pins so selection can remain set-returning and auditable under admissible orders.
* **Cross‑context reuse** must be explicit (bridges + loss accounting + pinned policy ids), and refresh must be tractable by typed RSCR causes rather than prose.

The resulting publication is a **CHR Pack** that is **CG‑Frame‑scoped**, **notation‑independent**, and **UTS‑published**, with explicit edition/policy pins sufficient for reproducibility and RSCR.

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** across contexts (same token, different referent/sense).
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (no explicit bridge and loss notes; unclear `entityOfConcern` changes).
* **Un-auditable aggregation** (no explicit legality surface and guard surface; no proof hooks; unclear Γ‑fold governing-definition assignment).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

### G.3:3 - Forces

| Force                                             | Tension                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Pluralism vs comparability**                    | Preserve tradition‑specific meaning ↔ enable admissible cross‑tradition use.       |
| **Expressiveness vs legality**                    | Model rich measurement semantics ↔ block illegal operations “by construction”. |
| **Portability vs honesty**                        | Encourage reuse ↔ forbid implicit crossings and hidden loss.                   |
| **Ease of authoring vs auditability**             | Keep authoring teachable ↔ require explicit pins, provenance, and tests.       |
| **Downstream flexibility vs upstream discipline** | Let CAL/selector choose policies ↔ keep thresholds/policy cut‑offs out of CHR. |

### G.3:4 - Solution — CHR authoring kit and publication surface

#### G.3:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
},
CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

// Pins strengthened for CHR authoring (delta over PinSets)
CorePinsRequired := {
// NOTE: `CG-FrameContext`, `entityOfConcern`, `CNSpecRef.edition`, `CGSpecRef.edition` are already required
// by `GCorePinSetId.PartG.AuthoringMinimal` (cite, don’t restate here).
UTSRowId[],                      // required: CHR terms are public ids (Name Cards plus public-id continuity records)
PathId[]/PathSliceId[],          // required: worked examples/tests and refresh anchoring cite paths
ReferencePlane,                  // required: definitional claims are plane-scoped
Φ/Ψ/Φ_plane policy-ids?,         // iff crossings/plane moves are exercised in examples or imports
ΓFoldRef.edition?                // iff an explicit Γ-fold artefact is pinned (otherwise use DefaultId)
// NOTE: method-/discipline-specific pins (e.g., DescriptorMapRef/DistanceDefRef/DHCMethodRef/InsertionPolicyRef)
// are declared only inside Extensions (e.g., `G.3:Ext.QD_OEE_Wiring`) to keep core linkage universal.
},

// consumed iff any published `CHR.AggregationSpec` relies on default Γ-fold (no explicit override pinned)
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerKindIds := {
RSCRTriggerKindId.EvidenceSurfaceEdit,
RSCRTriggerKindId.TokenizationOrNameChange,
RSCRTriggerKindId.CrossingBundleEdit,
RSCRTriggerKindId.ReferencePlaneEdit,
RSCRTriggerKindId.EditionPinChange,
RSCRTriggerKindId.PolicyPinChange,
RSCRTriggerKindId.DefaultGoverningDefinitionChange,
RSCRTriggerKindId.FreshnessOrDecayEvent,
RSCRTriggerKindId.LegalitySurfaceEdit,
RSCRTriggerKindId.BaselineBindingEdit
}
⟩`

*(Nil‑elision + expansion rule are per `G.Core:4.2`. This pattern does not redefine the semantics of core conformance ids, trigger kinds, or defaults; it only declares applicability and required pins.)*

#### G.3:4.2 - Output surface: `CHR Pack@CG‑Frame` (normative)

`CHR Pack@CG‑Frame` is the CHR kit payload that downstream patterns cite and pin (it is not a “shadow spec” for CN/CG).

**Minimum exported objects (kit surface):**

* `CHR.Characteristic[]`
* `CHR.Scale[]`
* `CHR.Level[]` *(when the scale type requires explicit level sets / order structure)*
* `CHR.Coordinate[]` *(encodings + legality annotations; never an implicit “upgrade” of measurement structure)*
* `CHR.Guards` *(guard macro surface; semantics governed by cited definitions; see `G.Core` and `A.18`)*
* `CHR.LegalityMatrix` *(admissible operations per scale type / unit / polarity regimes)*
* `CHR.AggregationSpecs` *(typed aggregators/comparators + proof hooks + edition pins where applicable)*
* `UTS` publication bundle: Name Cards (twin labels), public-id continuity notes, and (when applicable) bridge and loss notes
* RSCR artefacts: `RSCRTestId[]` + worked examples + provenance pins (ReferencePlane, Path/PathSlice, policy ids)

**Mandatory provenance pins (conceptual, notation‑independent):**

* `ReferencePlane`
* `PathId/PathSliceId` citations for worked examples/tests
* R‑anchors (conceptual; KD‑CAL lanes when used) realised via `PathId/PathSliceId` and, where applicable, `A.10` anchor/carrier refs
* policy pins used by crossings or plane moves (when exercised)
* edition pins for any referenced method or metric definitions that affect interpretation

#### G.3:4.3 - CHR authoring chassis (S1–S8)

**S1 — Charter the measurement scope (scope anchor).**
Declare the CHR `U.BoundedContext` and scope for the CG‑Frame, including: `entityOfConcern` boundaries, `ReferencePlane`, freshness/decay expectations, and the list of contested terms likely to require bridging. Output a design‑time `MeasurementCharter` and `KindMap@Context`.
If freshness/decay expectations are anything beyond an explicit “non‑decaying” declaration, wire them via
`G.3:Ext.DecayWiring` (governing pattern: `B.3.4`) rather than encoding decay semantics in CHR prose.
If assurance‑subtype lane tags are used (e.g., TA/VA/LA), declare the lane regime here so downstream evidence discipline can remain lane‑pure (taxonomy/semantics governed by `B.3`; evidence‑path representation & audit governed by `G.6`; this pattern only records wiring).
**Lane docking (wiring‑only; normative).**
If `EvidenceLanes` are used, the charter MUST:
* enumerate the lane tags used (e.g., TA/VA/LA) and cite their governing pattern taxonomy (governed by `B.3`), plus the upstream provenance for their use when available (e.g., `SoTAPaletteDescriptionId` via `G.3:Ext.SoTAPackInputs`);
* expose any lane‑dependent tolerances / proof requirements via explicit pins (policy‑id and/or edition‑pinned refs), not prose;
* treat lane tags as provenance metadata (not Contexts): they MUST NOT be “bridged away” or silently mixed;
* if any cross‑lane comparison/aggregation is claimed, it MUST be explicit and pinned to the governing acceptance/evidence policy (typically `G.4`) and auditable via evidence paths (`G.6`); otherwise downstream consumers treat it as illegal.
*Crossing semantics and penalty routing are cited via `G.Core` (do not restate).*

**S2 — Mint or reuse terms (UTS‑first).**
For each candidate characteristic, scale, level, or coordinate term: attempt reuse; otherwise mint via UTS Name Cards with twin labels and public-id continuity notes. When a term is imported across contexts, the import must be explicit and auditable (bridge and loss notes live with the crossing artefacts; CHR only cites them).

**S3 — Define `CharacteristicCard` (the CHR unit of meaning).**
A CharacteristicCard is the minimum unit CHR publishes for downstream legality. It SHOULD include (field names are indicative; semantics governed by cited definitions):

`CharacteristicCard := ⟨
  UTSRowId,
  Context,
  ReferencePlane,
  ObjectKind,
  Intent,
  Definition (typed),
  ObservableOf := ⟨instrument/protocol (A.10 anchors/carriers), uncertainty model, validity window⟩,
  EvidenceLanes? (KD‑CAL lanes; wiring only; semantics governed by `G.4` / `G.6`),
  ScaleRef,
  Polarity ∈ {↑, ↓, ⊥},
  Domain/Range,
  UnitSet,
  Bounds / zero semantics (as applicable),
  Freshness / half‑life (or explicit `NonDecayingDecl`; freshness/decay semantics governed by `B.3.4`),
  Missingness semantics (typed; include a classification/mapping when non‑trivial; downstream tri‑state handling is per G.Core),
  Stability/Reliability notes,
  RoleDecls? := RoleDecl[] (wiring‑only; each role declaration names its governing pattern + required pins; see `G.3:4.5`),
  QD.Role? ∈ {Q, D, QD-score} (interop alias for `RoleDecl` with `GoverningPatternId = C.18`; see `G.3:Ext.QD_OEE_Wiring`),
  Micro‑examples (R‑anchors: Path/PathSlice cited; lane tags where applicable)
⟩`

Where `RoleDecl := ⟨ roleLabel, GoverningPatternId, EditionPins?, PolicyPins? ⟩` (wiring-only; the value of `GoverningPatternId` names the FPF pattern that governs the role declaration semantics).

Rules (CHR‑governed intent, semantics governed by cited definitions where indicated):

* Scale/unit/polarity legality obligations cite MM‑CHR governing definitions (`A.18` and `C.16`) and must be *checkable* by downstream patterns.
* Missingness must be typed so downstream can apply tri‑state outcomes without silent coercion (tri‑state semantics are governed by `G.Core`).
* If `EvidenceLanes` are recorded, they are only lane tags for downstream evidence discipline (taxonomy governed by `B.3`; audit surface: `G.6`; any cross‑lane policy is governed by `G.4`); this pattern does not introduce lane semantics or invent bridge‑like constructs.
* If `RoleDecls` are used, each declaration MUST cite the FPF pattern that governs the declaration, for example `C.18` or `C.19`, and surface the edition and policy pins required by that governing pattern; CHR does not define role semantics locally.
* **Role docking (normative, wiring-only):** if any `RoleDecl` is present with `GoverningPatternId = X`,
  then `G.3` MUST include (or explicitly cite) a corresponding `GPatternExtension` block whose governing definition is `X`
  (or whose `Uses` includes `X`) and that surfaces the required pins for that role family. Otherwise the role
  declaration is non-conformant (it is an undocked semantic fragment).
* **Freshness docking (normative, wiring-only):** if a characteristic’s freshness/half-life is defined via a named
  decay model/policy (rather than a pure local statement), the relevant policy/ref MUST be pinned and cited through `B.3.4`
  via `G.3:Ext.DecayWiring`.
* If a characteristic is intended to be *promoted into* `CG‑Spec`, the linkage is explicit and edition‑pinned (wiring lives in an Extension; semantics governed by `G.0`).

**S4 — Define `ScaleCard` and `LevelCard` (lawful measurement).**
Publish the scale type and admissible transforms, plus levels/orders when applicable. CHR does not invent new legality semantics; it cites MM‑CHR governing definitions and makes the legality surface concrete for the frame’s characteristics.

Typical distinctions that must be representable:

* **Nominal / categorical:** equality + counting; transforms are permutations.
* **Ordinal:** order‑preserving transforms; no arithmetic that presupposes intervals.
* **Interval:** affine transforms; differences meaningful; means may be lawful if justified.
* **Ratio:** positive scalar transforms; ratios meaningful; products/sums subject to unit discipline.
* **Count / rates:** explicit exposure/timebase requirements; rate conversions must be explicit.
* **Cyclic:** wrap‑around discipline + principal interval declaration.

**S5 — Define `CoordinatePolicy` (encodings without hidden cardinalization).**
When a numeric coordinate/embedding is used for convenience or tooling, CHR MUST publish:

* what invariants are preserved (order only / ratios / topology / wrap‑around),
* what remains illegal,
* what proof hooks are required if a structure with higher scale-type commitment is claimed.

A coordinate never silently upgrades a scale type; if an upgrade is claimed, the proof requirement is explicit and carried by MM-CHR governing definitions.

**S6 — Publish legality + guard surfaces (Guard Macros + LegalityMatrix).**
CHR publishes a `CHR.LegalityMatrix` and a `CHR.Guards` surface that downstream operators can reference.

Guard macro names are allowed as authoring ergonomics, but their semantics MUST cite governing definitions (no “shadow semantics” in this pattern). Examples of macro intents (governing definitions in parentheses):

* `CSLC_PROOF_REQUIRED(x)` (MM‑CHR legality governing definitions: `A.18/C.16`)
* `UNKNOWN_TRI_STATE(x)` (tri‑state semantics governed by `G.Core`)
* `UNIT_CHECK(x)` (MM‑CHR legality governing definitions)
* `RETURN_SET_FOR_PARTIAL_ORDERS()` (set‑return semantics governed by `G.Core`)
* `METRIC_EDITION_REF(...)` (edition‑pin discipline governed by `G.Core`; metric semantics governed by `C.18`/`C.21` as applicable)

**S7 — Publish `AggregationSpecs` (typed, admissible, reproducible).**
CHR may publish typed aggregation/comparison specs that are *safe by construction* and usable as building blocks by `G.4` and `G.5`. For any published spec:

* The legality regime is explicit (scale/unit/polarity constraints + required proof hooks).
* If a contributor folding policy (Γ‑fold) is used and not explicitly overridden, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`; do not restate the default here.
* If method‑role declarations imply metric‑driven comparisons (e.g., QD roles), the relevant edition/policy pins are surfaced (wiring lives in an Extension; semantics governed by the referenced patterns).

**S8 — Publish, test, and evolve (UTS + RSCR readiness).**
Publish the CHR pack and associated Name Cards to UTS. Attach:

* RSCR tests that check legality and guard coverage and reject illegal ops,
* worked examples with Path/PathSlice provenance,
* refresh/decay notes and deprecations with lexical continuity.

This step prepares the RSCR loop but does not govern orchestration (governing definition: `G.11`).

#### G.3:4.4 - Interfaces (normative)

| Interface                           | Consumes                                          | Produces                                                         |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| **G.3‑1 Charter_CHR**               | `CG‑FrameContext` (`G.1`), SoTA inputs (`G.2`)    | `MeasurementCharter`, `KindMap@Context`                          |
| **G.3‑2 MintOrReuse_Terms**         | candidate terms + UTS registry                    | Name Cards + UTS ids for `Characteristic/Scale/Level/Coordinate` |
| **G.3‑3 Define_Characteristic**     | `MeasurementCharter`, candidate semantics         | `CHR.Characteristic[]` (CharacteristicCards)                     |
| **G.3‑4 Define_ScaleLevel**         | CharacteristicCard + MM‑CHR rules                 | `CHR.Scale[]`, `CHR.Level[]`                                     |
| **G.3‑5 Define_CoordinatePolicy**   | Scale/Level + use‑case constraints                | `CHR.Coordinate[]` + legality annotations                        |
| **G.3‑6 Publish_GuardsAndLegality** | Scale/Level/Coordinate set                        | `CHR.Guards`, `CHR.LegalityMatrix`                               |
| **G.3‑7 Publish_AggregationSpecs**  | CHR set + legality hooks + (optional) metric refs | `CHR.AggregationSpecs` (+ proofs/refs + pins)                    |
| **G.3‑8 Publish_CHRPack**           | all CHR artefacts + tests/examples                | `CHR Pack@CG‑Frame` + UTS rows + RSCR tests                      |

#### G.3:4.5 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId-scoped; **not** new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SuiteBoundaryLinkage**

* **PatternScopeId:** `G.3:Ext.SuiteBoundaryLinkage`
* **GPatternExtensionId:** `SuiteBoundaryLinkage`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19.CHR`
* **Uses:** `{A.19.CHR, A.15.3}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CHRMechanismSuiteDescriptionRef.edition?` *(when the suite description is cited as a reproducibility baseline)*
  * `CHRMechanismSuiteSlotFillingsPlanItem` refs *(when planned baseline binds CHR artefacts into WorkPlanning)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds CHR authoring outputs to the P2W seam (`SlotFillingsPlanItem`); suite semantics and membership are governed by `A.19.CHR`.

**GPatternExtension: SoTAPackInputs**

* **PatternScopeId:** `G.3:Ext.SoTAPackInputs`
* **GPatternExtensionId:** `SoTAPackInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `ClaimSheetId[]` / operator & object inventory refs (as cited inputs)
  * `SoTAPaletteDescriptionId?` (when palette/traces are cited; used to dock contested‑term inventory and (if present) lane tags/tolerances)
  * `BridgeMatrixId?` (when terms/constructs are imported across traditions)
  * `UTSRowId[]` drafts/aliases from synthesis
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit}`
* **Notes (wiring‑only):** SoTA pluralism inputs are governed by `G.2`; this module only specifies which synthesis artefacts are cited while authoring CHR.

**GPatternExtension: CGSpecPromotionWiring**

* **PatternScopeId:** `G.3:Ext.CGSpecPromotionWiring`
* **GPatternExtensionId:** `CGSpecPromotionWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.0`
* **Uses:** `{G.0}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CGSpecRef.edition` *(when a characteristic is promoted/linked into `CG‑Spec`)*
  * `CHR.Characteristic.id` pointers included in `CG‑Spec.Characteristics := [...]` *(no shadow ids; CG‑Spec stores pointers, see `G.0`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** Promotion semantics and legality gate governing-definition assignment stays with `G.0`; CHR only pins and cites.

**GPatternExtension: MMCHRLegalityWiring**

* **PatternScopeId:** `G.3:Ext.MMCHRLegalityWiring`
* **GPatternExtensionId:** `MMCHRLegalityWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `A.18`
* **Uses:** `{A.17, A.18, C.16}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * CSLC legality proof anchors/carriers (ids/refs as defined by MM‑CHR governing definitions; cite `A.18/C.16`)
  * Unit coherence references (where units exist)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring‑only):** This module wires CHR artefacts to MM‑CHR legality proof obligations; legality semantics are governed by the referenced patterns.

**GPatternExtension: DecayWiring**

* **PatternScopeId:** `G.3:Ext.DecayWiring`
* **GPatternExtensionId:** `DecayWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `B.3.4` *(freshness/decay semantics)*
* **Uses:** `{B.3.4, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `FreshnessWindowDeclRef` *(or equivalent window pin, as defined by the governing definition)*
  * `DecayPolicyIdRef?` *(policy-bound; if decay model is referenced by id)*
  * `PathSliceId[]` *(affected evidence carriers / examples that witness drift)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit}`
* **Notes (wiring‑only):** CHR does not define decay semantics; it only pins the defined by the governing pattern window/policy and ensures refresh can be triggered on decay events.

**GPatternExtension: QD_OEE_Wiring**

* **PatternScopeId:** `G.3:Ext.QD_OEE_Wiring`
* **GPatternExtensionId:** `QD_OEE_Wiring`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition` *(if any Characteristic declares descriptor roles)*
  * `DistanceDefRef.edition` *(if any Characteristic declares distance roles)*
  * `DHCMethodRef.edition` *(if any Characteristic is used as Q / QD-score)*
  * `InsertionPolicyRef?` *(when archive insertion semantics are declared for reproducibility)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** QD/OEE semantics are governed by `C.18 and C.19`. CHR only surfaces method‑role declarations
  (via `RoleDecls` or the interop alias `QD.Role`) and the edition/policy pins required for reproducible archive/front interpretation.

### G.3:5 - Archetypal Grounding

**AG‑1 — ML fairness auditing (post‑2015 selective and set‑valued practice).**
*System:* a CG‑Frame for evaluating deployed classifiers across cohorts with explicit abstention/defer behavior.
*CHR authoring:* publish `DemographicParityGap` and `EqualizedOddsGap` as Characteristics with:

* explicit ReferencePlane (deployment population + sampling regime),
* `ObservableOf` (audit protocol + uncertainty model + window),
* interval scale (bounded; zero semantics explicit),
* missingness semantics (cohort sparsity and label noise are typed),
* legality surfaces and guard surfaces that forbid illicit cohort mixing and require explicit proof hooks for aggregation across cohorts.

*Downstream:* CAL acceptance binds thresholds and failure behavior; selector remains set‑returning under partial orders and may treat “defer/abstain” as a first‑class outcome (tri‑state semantics pinned through `G.Core`).

**AG‑2 — Clinical diagnostics (post‑2015 evidence‑aware evaluation).**
*System:* a CG‑Frame for comparing diagnostic pipelines under evolving datasets and protocols.
*CHR authoring:* publish `Sensitivity` and `Specificity` as ratio‑scale, dimensionless Characteristics on `[0,1]`, with:

* explicit `ObservableOf` (trial protocol, inclusion criteria, uncertainty model),
* freshness/decay expectations (protocol drift is modelled as decay),
* legality surfaces that forbid averaging incompatible ordinal labels (e.g., severity grades) and require explicit unit/exposure constraints for any derived rate.

*Downstream:* CAL acceptance governs thresholds and guard‑bands; evidence wiring is cited via Path/PathSlice to make refresh triggers actionable.

**AG‑3 — Quality‑Diversity / Illumination (post‑2015 MAP‑Elites/CMA‑ME lineage).**
*System:* a CG‑Frame where selection returns archives/fronts rather than a single winner.
*CHR authoring:* declare which Characteristics play Q/D/QD‑score roles and pin the metric definitions (descriptor map, distance definition, method editions) so archives are reproducible across runs and refresh can be triggered on edition changes. CHR does not scalarize partial orders; set‑return semantics are pinned through `G.Core`.

### G.3:6 - Bias‑Annotation

CHR authoring is where many biases become “baked in” as measurement choices. Typical risks:

* **Proxy bias:** a convenient observable substitutes for the intended construct. Mitigation: require `ObservableOf` + ReferencePlane + micro‑examples; force explicit “what is being measured” rather than relying on labels.
* **Population and protocol shift:** a characteristic’s meaning changes when the sampling regime or protocol changes. Mitigation: explicit validity windows and freshness/decay expectations; edition pins for protocol definitions; RSCR triggers on freshness/decay events and evidence surface edits.
* **Ordinal misuse bias:** ordinal ratings treated as interval/ratio by convenience. Mitigation: publish scale type + admissible transforms; legality matrix + guard macros; reject coordinate upgrades without proof hooks.
* **Cross‑tradition/cross‑context bias:** imported terms erase local meaning. Mitigation: require explicit imports and loss notes; downstream penalties route to `R_eff` only (pinned through `G.Core`), making loss visible rather than silently altering F/G semantics.
* **Metric gaming bias (QD and evaluation):** changing descriptors/distances changes what “diverse” means. Mitigation: edition‑pin metric definitions and make role declarations explicit (wiring via `C.18 and C.19`).

### G.3:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G3‑CoreRef** | `G.3` is conformant only if the applicable `G.Core` obligations declared in `G.3:4.1` are satisfied (effective expansion of profiles/sets + deltas; explicit pins; typed RSCR triggers; defaults with one governing definition).                       |
| CC‑G3‑01          | `CHR Pack@CG‑Frame` is published as a notation‑independent kit payload with the minimum exported objects listed in `G.3:4.2`.                                                                                                         |
| CC‑G3‑02          | Every `CHR.Characteristic` has an explicit declared `Context`, an explicit `ReferencePlane`, and a filled `ObservableOf` field (instrument/protocol + uncertainty model + validity window).                                               |
| CC‑G3‑03          | Every `CHR.Characteristic` declares its `ScaleRef`, `Polarity`, and `UnitSet` (or an explicit “unitless” declaration), plus bounds/zero semantics where applicable.                                                                   |
| CC‑G3‑04          | Missingness is typed in the CHR artefacts such that downstream tri‑state handling is possible without silent coercion. *(Tri‑state semantics are governed by `G.Core`; the typing obligation is CHR‑local.)*                              |
| CC‑G3‑05          | `CHR.Scale` / `CHR.Level` artefacts encode the scale type and admissible transforms, and make illicit arithmetic checkable by downstream consumers.                                                                                   |
| CC‑G3‑06          | Any published `CHR.Coordinate` includes a `CoordinatePolicy` that states preserved invariants and explicit non‑entitlements; coordinates do not silently upgrade measurement structure.                                               |
| CC‑G3‑07          | `CHR.LegalityMatrix` and `CHR.Guards` exist and are referenced by downstream operator authoring; semantics are governed by cited definitions (MM‑CHR and `G.Core`), not duplicated locally.                                                        |
| CC‑G3‑08          | `CHR.AggregationSpecs` are typed and legality‑constrained; where Γ‑fold is required and no explicit override is pinned, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`. |
| CC‑G3‑09          | If any characteristic is intended for promotion into `CG‑Spec`, the linkage is explicit and edition‑pinned (no shadow ids). *(Governing definition: `G.0`; wiring via `G.3:Ext.CGSpecPromotionWiring`.)*                                             |
| CC‑G3‑10          | UTS Name Cards exist for public ids minted or evolved by the CHR pack (twin labels plus public-id continuity notes). *(Delegation target: `CC‑GCORE‑UTS‑1` via `CC‑G3‑CoreRef`.)*                                                                      |
| CC‑G3‑11          | Worked examples and RSCR tests exist and cite `PathId/PathSliceId`; they cover illegal‑op refusal, unit and scale constraints, polarity invariants, and coordinate non‑entitlements.                                                      |
| CC‑G3‑12          | Thresholds/guard‑bands are not embedded in CHR artefacts; they remain governed by CAL acceptance clauses (`G.4`).                                                                                                                        |
| CC‑G3‑13          | When method‑role declarations are present (via `RoleDecls` and/or `QD.Role` alias), each declaration is **docked** to its governing pattern via a corresponding `G.3:Ext.*` module, and the edition and policy pins required by the governing pattern are surfaced to make downstream interpretation reproducible. *(QD/OEE governing patterns: `C.18` and `C.19`; wiring via `G.3:Ext.QD_OEE_Wiring`.)* |
| CC‑G3‑14          | **Evidence wired.** Each `CHR.Characteristic` links to R‑anchors via `PathId/PathSliceId` (and, where applicable, `A.10` anchor/carrier refs), so downstream evidence discipline (`G.6`) can audit legality and guard claims.            |
| CC‑G3‑15          | An `Archetypal Grounding` section exists with at least two domain‑distinct examples that demonstrate lawful CHR typing/legality and the CHR↔CAL separation (notably: no thresholds in CHR).                                          |
| CC‑G3‑16          | If `EvidenceLanes` are used, lane tags are declared with a citation to their governing pattern taxonomy (`B.3`), and any lane‑dependent tolerances/proof requirements are explicitly pinned (policy‑id / edition refs). Cross‑lane comparison/aggregation is **illegal by default** unless an explicit governing-pattern policy makes it lawful (typically `G.4`), and it must be auditable via evidence paths (`G.6`). |
| CC‑G3‑17          | If the CHR outputs are bound into the planned baseline / suite seam, the binding uses `CHRMechanismSuiteSlotFillingsPlanItem` as defined in `A.19.CHR` + `A.15.3` (no local baseline variants; wiring via `G.3:Ext.SuiteBoundaryLinkage`). |
| CC‑G3‑18          | **Freshness is explicit.** Each `CHR.Characteristic` declares a validity window and either (i) an explicit `NonDecayingDecl` or (ii) a freshness/half‑life statement that is pinned to the governing pattern (`B.3.4`) when policy‑bound (`G.3:Ext.DecayWiring`). Changes in decay windows/policies participate in RSCR via canonical trigger kinds declared in `G.3:4.1`. |

### G.3:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden cardinalization.** Don’t treat ordinal encodings as interval/ratio; do publish coordinate policies that explicitly preserve order‑only invariants and forbid arithmetic upgrades.
* **Unit laundering.** Don’t add or average quantities with incompatible units; do force explicit unit discipline and legality checks via MM‑CHR governing definitions.
* **Polarity drift.** Don’t rely on “higher is better” implicitly; do publish polarity explicitly and make downstream use auditable.
* **Threshold leakage into CHR.** Don’t embed policy cut‑offs in CHR; do keep thresholds in CAL acceptance artefacts.
* **Unpinned semantics.** Don’t cite “the metric” or “the distance” without edition pins; do require edition‑pinned references when semantics affect interpretation.
* **Unscoped reuse.** Don’t reuse CHR terms across contexts without explicit import and loss notes; do keep crossings explicit and auditable (pinned through `G.Core`).

### G.3:9 - Consequences

* **Legality becomes checkable.** Downstream patterns can reject illegal operations and rely on explicit legality surfaces rather than implicit conventions.
* **Comparability without semantic flattening.** Plural traditions remain representable because CHR preserves local meaning while making lawful relations explicit.
* **Reproducible downstream behavior.** Edition/policy pins make “why did this change?” answerable and RSCR actionable.
* **Authoring overhead.** The pattern shifts effort to up‑front authoring: explicit cards, pins, and tests are non‑optional when CHR becomes a public kit surface.

### G.3:10 - Rationale

CHR is the point where “numbers start moving” *only if* measurement semantics are stable enough to support lawful downstream reasoning. By making scale/unit/polarity explicit, publishing legality and guard surfaces, and requiring provenance pins, CHR authoring prevents downstream mechanisms from silently inventing their own legality assumptions.

Separating core invariants into `G.Core` prevents drift and ensures Part‑G‑wide properties (tri‑state, penalty routing, set‑return semantics, RSCR typing, Default Governing Definition Index) cite `G.Core` as their governing definition, while CHR remains responsible for CHR‑specific kit surfaces.

### G.3:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice by:

* treating abstention/defer and set‑valued outcomes as first‑class design objects (consistent with modern selective prediction and set‑valued reporting practice),
* keeping multiobjective and archive‑based reasoning set‑returning rather than silently scalarizing (consistent with QD/illumination and open‑ended evaluation practice after 2015),
* making evaluation semantics reproducible through explicit edition/policy pinning (aligned with the modern emphasis on reproducibility and “specifying the evaluation surface” rather than only reporting metrics),
* modularizing method‑family specifics (QD/OEE, explore‑exploit) via explicit wiring and governing-definition assignment rather than embedding method semantics into universal measurement admissibility.

### G.3:12 - Relations

**Builds on:** `G.Core`, `G.1`, `G.2`, `G.6` (EvidenceGraph / Path citation), `A.19.CHR`, `A.15.3`, `A.17–A.18/C.16` (MM‑CHR), `F.1–F.9` (Contexts/UTS/Bridges), `B.3` / `B.3.4`, `A.10`, `E.10`, `E.5.1–E.5.3`.
**Uses (via Extensions):** `G.0` (promotion/linkage to `CG‑Spec`), optional `C.18 and C.19` (QD/OEE wiring).
**Publishes to:** `G.4` (admissible operators plus legality and guard macros and freshness pins), `G.5` (role declarations plus pins for reproducibility), `UTS` (Name Cards and public-id continuity notes), RSCR tests and hooks.
**Constrains:** any CAL/LOG/selector usage that consumes CHR (must treat CHR artefacts as typed/legal surfaces, not as prose hints).

### G.3:End

