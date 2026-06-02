## G.9 — Parity / Benchmark Harness

> **Status:** Stable

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

### G.9:0.1 — What goes wrong if missed

- benchmark numbers mix different windows, baselines, or comparator editions and still pretend to be comparable
- cross-context reuse or normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

### G.9:0.2 — What this buys

- one `ParityPlan@Context` that fixes baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport@Context` that echoes the active pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs with explicit scope (`describedEntity`, `ReferencePlane`, window), explicit governance, CSLC comparability and admissibility references, and comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`) and explicit reproducibility pins (editions + policy‑ids);
* executes parity in a way that is consumable by **G.5** (selected-set outcomes, DRR/SCR evidence trace);
* publishes **ParityReport@Context** suitable for downstream consumption, shipping, and refresh/RSCR wiring.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window / freshness regime,
* comparator semantics (including any normalization / comparability mapping),
* method‑family “measurement” edition pins (incl. DHC method/spec),
* cross‑Context reuse (Bridge refs, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to make these recoverable as **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new governing spec refs.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement/comparator definitions. When DHC/QD/OEE modes are used, the required definition pins are introduced only via the corresponding `Extensions` blocks (nil‑elision when unused).
* **Telemetry vs objectives.** IlluminationSummary and coverage/regret are telemetry: **report‑only by default**; dominance changes require explicit CAL policy ids (recorded in audit pins).
* **GateCrossing visibility.** Any crossings/gates used by parity must be visible and auditable via CrossingBundle + GateCrossing checks; failures block parity publication/consumption.
* **Cross‑Context reuse.** Any reuse across contexts or reference planes must carry explicit crossing pins, audit support, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

### G.9:4 — Solution
#### G.9:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant** and therefore binds to **G.Core** by declaration (not by restating invariants here).

**GCoreLinkageManifest (G.9)** *(normative; expands per `G.Core:4.2`)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  }

* `RSCRTriggerSetIds` := {
  `GCoreTriggerSetId.CGSpecGate`
  }
* `RSCRTriggerKindIds` := {
  `RSCRTriggerKindId.EvidenceSurfaceEdit`,
  `RSCRTriggerKindId.PenaltyPolicyEdit`,
  `RSCRTriggerKindId.BaselineBindingEdit`,
  `RSCRTriggerKindId.TelemetryDelta`
  }
  *(Pattern‑local deltas; cross‑tradition / bridge‑calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over‑trigger baseline (within‑context) parity runs.)*

* `DefaultsConsumed` := {
  `DefaultId.DominanceRegime`,
  `DefaultId.PortfolioMode`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Defaults are cited through `G.Core.DefaultGoverningDefinitionIndex` (not restated here); the expected default governing definitions are `CC‑G5.28`, `CC‑G5.23`, and `CC‑G5.4` respectively.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `ComparatorSpecRef.edition`,
  `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlanItemRefs[]?`,
  `EvidenceGraphId`,
  `Budgeting?`,
  `EpsilonDominance?`,
  `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`,
  `SCPRef.edition?`, `MinimalEvidenceRef.edition?`
  }
*(Nil‑elision applies; mode‑specific definition pins are introduced only by the corresponding `GPatternExtension` blocks.)*

* `TriggerAliasMapRef` := `∅`

#### G.9:4.1 — Objects and publication records

All objects below are **notation‑independent**; serialisations (if any) are handled in shipping and interop publication forms, not here.

**(1) `ParityPlan@Context`** *(WorkPlanning record)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan@Context := ⟨
  ParityPlanId(UTS),
  CGFrameId?,                              // or CG-FrameContext id/scope anchor cited by the referenced frame records
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  ParityContextId,
  BaselineSet,                            // method-family / generator-family baseline scope (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  PlanItemRefs[]?                          // references to A.15.3 SlotFillingsPlanItem (planned baseline), when parity depends on planned slot fillings
⟩`

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport@Context`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by running a `ParityPlan@Context`. By itself it is not a dated `U.Work` occurrence, audit performance, evidence path, assurance result, or gate decision; those claims require `A.15`/`A.15.1`, `A.10`/`G.6`, `B.3`, or `A.21` respectively.

`ParityReport@Context := ⟨
  ParityReportId(UTS),
  ParityPlanId,
  BaselineSet, FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // selected-set / archive outcomes (as refs to selector outputs)
  EpsilonDominance?,                        // echoed when used
  AbstainReasons[]?,                        // ids/labels (policy-bound) for abstain/degrade; refusal paths included
  TelemetrySummary? := ⟨IlluminationSummary?, coverage?, regret?⟩,  // report-only by default; promotion requires CAL policy-id pins
  GuardOutcomeTraceRef?,                    // pass/degrade/abstain trace + cited reasons (policy-bound)
  EvidenceTrace := ⟨EvidenceGraphId, PathId[], PathSliceId?⟩,
  CrossingPins?,                            // Bridge/CL/Φ/Ψ/Φ_plane pins, when crossings are invoked
  EditionPinsDelta?,                        // explicit list of edition pins actually active during the run
  PolicyPinsDelta?,                         // explicit list of policy-ids actually active during the run
  RSCRRefs[]                                // parity RSCR test ids / trigger emissions
⟩`

**Naming discipline.**

* Heads reuse existing U‑types and LEX discipline; no new “strategy” primitive is minted here.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (design‑time / WorkPlanning)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) to compare; where parity context matters, cite `SoS‑LOGBundleId?` and source-maturity ids by reference (acceptance-gate thresholds remain in `G.4` Acceptance).
2. **Bind scope.** Fix `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` and record it in the plan (no silent widening/narrowing).
3. **Define baseline-set reference.** Declare what counts as “baseline set” and how it is cited (e.g., `BaselineBindingRef`, the evidence-backed baseline-set reference, pointing to an EvidenceGraph path slice or an upstream shipped package or publication-record id).
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned baselines (when applicable).** If parity depends on planned slot fillings, the plan cites the relevant `SlotFillingsPlanItem` refs (A.15.3) via `PlanItemRefs[]` rather than embedding a competing baseline object (nil‑elision when unused).
10. **Publish crossing pins (when invoked).** Cross-Context or cross-plane/Kind reuse requires explicit Bridge/CL/Φ pins; penalties affect `R_eff` only (invariants pinned through `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; run eligibility or acceptance checks under the plan’s `TaskSignature (S2)` and refuse or abstain on non-admissible operations (record trace; no “fourth status”). If a live `A.21` gate consumes this check, cite its `GateDecisionRef`/`DecisionLogRef`; do not create a `G.9`-local CSLC gate.
2. **Invoke selection/dispatch.** Apply **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s `PortfolioMode` and selected-set semantics.

When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record comparability mapping (when used).** If `UNM_id?` / `NormalizationMethodId[]?` / `NormalizationMethodInstanceId[]?` were declared, **echo them** in `ParityReport@Context` (or in its explicit pins deltas) and record their ids (and any scoped notes required by the cited governing spec ref) in audit pins/SCR; cite the applicable `PathId`s.
4. **Publish trace.** Emit `ParityReport@Context` with EvidenceGraph citations and all active pins (editions/policy‑ids), so the run can be re‑checked and re‑run.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

- Two agentic search setups both claim bounded specialization on the same declared task family.
- The `ParityPlan` pins the same freshness window, threshold target, adaptation budget, prior-exposure declaration, comparator editions, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- A CSLC-admissible `ParityReport@Context` therefore states what was held constant, which signals remained telemetry, and why the outcome stays a governed selected set or partial order rather than collapsing into a scalar winner. The reader can recover the practical comparison from the parity slice itself before reading any optional wiring blocks.

#### G.9:4.3b — Conditional causal method rung parity

Use this conditional extension only when a parity report compares causal methods or causal-use claims. The parity report starts with a cheap screen and may stop at degraded parity or abstain when methods plainly answer different causal uses.

```text
CausalRungParityScreen:
  comparedMethodsRef: ComparedMethodSetRef
  targetCausalityLadderRungSet: {CausalityLadderRung...}
  causalEvidenceSupportBasisSet: {CausalEvidenceSupportBasis...}
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  cheapParityStop: CausalRungParityScreenOutcome
```

```text
CausalRungParityScreenOutcome =
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportBasisDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    returnToC28
```

Open the full `CausalMethodRungParityRecord` only when `CausalRungParityScreenOutcome = comparableEnoughForFullRecord`. Other outcomes are admissible cheap stops: degraded parity, abstain, or apply `C.28`, without fabricating a full parity record.

`targetCausalityLadderRungSet` is the first parity check. Here `CausalityLadderRung` is a cited causal-use taxonomy value, not a maturity level, upgrade ladder, or superiority scale. If the set has more than one causality-ladder rung and no declared bridge and loss makes the comparison meaningful, the screen returns `crossRungDegrade` rather than treating the methods as peers.

`causalEvidenceSupportBasisSet` is the second parity check. If methods depend on different causal support bases and no declared support-loss or bridge makes the comparison meaningful, the screen returns `crossSupportBasisDegrade`.

`sameEstimand = no` returns `differentEstimandAbstain` unless the report names a shared estimand, a bridge and loss relation, or a reason the comparison is intentionally non-parity. A scalar parity result is not admissible across different estimands by default.

`sameOutcomeWindow = no` returns `differentOutcomeWindowAbstain` unless the report pins a common follow-up window or declares the window loss. A method that wins at one horizon is not parity-superior at another horizon by default.

Parity reports comparing causal methods then carry a `CausalMethodRungParityRecord`:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  estimandRef: U.CausalEstimand
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  declaredCausalEvidenceSupportLossRef?
  causalUseSupportRecordRef?
  causalUseSupportVerdict?: CausalUseSupportVerdict
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  causalTransportabilityProfileRef?
  estimationValidityClassRef?
  causalParameterEstimationProfileRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

Parity reports comparing causal methods fill this record so the "same" claims are checkable by fields rather than prose:

- comparedMethodsRef;
- targetCausalityLadderRung;
- targetCausalUseClaimKind: CausalUseClaimKind;
- estimandRef;
- interventionBudgetOrActionSetRef;
- causalEvidenceSupportBasis;
- causalUseSupportRecordRef and causalUseSupportVerdict when a `C.28` support record or verdict is being consumed;
- causalFollowUpWindowRef;
- outcomeMeasureRef;
- declaredCausalityLadderBridgeOrLossRef where causality-ladder rungs differ;
- causalTransportabilityProfileRef where source population, target population, domain, context, or evidence regime differs;
- causalParameterEstimationProfileRef where estimation validity, uncertainty, nuisance handling, or sensitivity differs;
- degraded or abstain posture where parity cannot be established.

Causality-ladder parity is a degrade/abstain condition, not a universal comparison ban. Cross-rung method comparisons must name `declaredCausalityLadderBridgeOrLossRef` and cannot become superiority claims by default.

What changes in practice: one benchmark cannot compare a predictive model, an interventional action/effect question optimizer, and a counterfactual comparison question strategy as one undifferentiated "method improvement" set.

What this does not authorize: `G.9` does not decide causal identification, causal fairness, or counterfactual sampling realizability; it keeps parity/benchmark harness authority and sends causal-use support to `C.28`.

#### G.9:4.9 — Extensions (pattern‑scoped; non‑core)

Most working readers can stop after `G.9:4.3a`. The blocks below are binding-only wiring records used only when the corresponding parity mode is actually active.

The following blocks store **wiring only** (pins/refs/policy‑ids, relevant triggers, and `Uses`), while semantics remains defined in the referenced patterns.

**GPatternExtension block: `G.9:Ext.CrossTraditionParity`**
**GPatternExtension: CrossTraditionParity**
* **PatternScopeId:** `G.9:Ext.CrossTraditionParity`
* **GPatternExtensionId:** `CrossTraditionParity`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.7`
* **Uses:** `{G.7, F.9, E.18, A.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `BridgeId/BridgeCardId[]`
  * `BridgeMatrixId?`
  * `CalibrationLedgerId?` / `BCT.id?`
  * `RegressionSetId?` / `SentinelId[]?` *(when sentinel wiring is used)*
  * `CL/CL^k/CL^plane`
  * `Φ(CL) policy-id`, `Φ_plane policy-id`, `Ψ(CL^k) policy-id?`
  * `CrossingBundleId?`
* **RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(preferred; expands in `G.Core`)*
* **RSCRTriggerKindIds (delta, if any):** `∅`
* **Notes (wiring-only):** This block does not define CL/Φ/Ψ semantics; it only requires the pins needed to cite calibration records and crossing visibility bundles.

**GPatternExtension block: `G.9:Ext.SoSLogGuardNarration`**
**GPatternExtension: SoSLogGuardNarration**
* **PatternScopeId:** `G.9:Ext.SoSLogGuardNarration`
* **GPatternExtensionId:** `SoSLogGuardNarration`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.23`
* **Uses:** `{C.23, G.6, G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` / `BranchId[]` *(ids as cited labels; semantics come from `C.23`)*
  * `FailureBehaviorPolicyId/SoSLogBranchId`
  * `EvidenceTrace.PathId[]` / `PathSliceId?`
  * `AcceptanceClauseId[]` *(when referenced)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Explains **why** a parity run degraded/abstained by citing SoS‑LOG ids and evidence paths; does not redefine guard semantics.

**GPatternExtension block: `G.9:Ext.DHCParityPins`**
**GPatternExtension: DHCParityPins**
* **PatternScopeId:** `G.9:Ext.DHCParityPins`
* **GPatternExtensionId:** `DHCParityPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DHCMethodRef.edition`
  * `DHCMethodSpecRef.edition?` *(when the cited DHC method spec distinguishes method vs method-spec editions)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* **Notes (wiring-only):** Declares the pins required to make DHC‑based parity reproducible and RSCR‑refreshable; semantics of DHC lives in `C.21`.

**GPatternExtension block: `G.9:Ext.QDArchiveParity`**
**GPatternExtension: QDArchiveParity**
* **PatternScopeId:** `G.9:Ext.QDArchiveParity`
* **GPatternExtensionId:** `QDArchiveParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `CharacteristicSpaceRef.edition?` *(when discretisation/topology is referenced)*
  * `EmitterPolicyRef`
  * `InsertionPolicyRef`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Post‑2015 QD families are referenced here only as wiring + edition/policy pin obligations (semantics come from `C.18`/`C.19`/`G.5`).

**GPatternExtension block: `G.9:Ext.OEEParity`**
**GPatternExtension: OEEParity**
* **PatternScopeId:** `G.9:Ext.OEEParity`
* **GPatternExtensionId:** `OEEParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.19`
* **Uses:** `{C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `TransferRulesRef.edition`
  * `EnvironmentValidityRegionId`
  * `ExplorationBudgetPolicyId?`
  * `EvidenceTrace.PathSliceId?` *(for transfer‑keyed events)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Open‑ended parity is expressed as policy/edition pins + telemetry wiring, not as new core norms.

### G.9:5 — Interfaces (minimal I/O; conceptual)

| Interface                          | Consumes                                                                                                                                         | Produces                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **G.9‑1 `Plan_Parity`**            | `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `PlanItemRefs[]?` | `ParityPlan@Context` (UTS entry; edition‑pinned)                                                |
| **G.9‑2 `Run_Parity`**             | `ParityPlan@Context`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                  | Selector outputs (selected sets / archives / sets as refs), DRR+SCR pins with `PathId[]`/`PathSliceId?` |
| **G.9‑3 `Publish_ParityReport`**   | parity-run trace refs + active pins                                                                                                            | `ParityReport@Context` (UTS publication record; emits canonical RSCR ids)                       |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, Default Governing Definition Index links, and P2W split).

1. **CC‑G9.1 — Equal windows (and budgets) & pinned spec editions (local).**
   A ParityPlan **SHALL** declare a single `FreshnessWindows` shared across baselines. If `Budgeting` is used/pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the edition pins required by the referenced governing spec and comparator refs (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings (WorkPlanning baseline), the plan **SHALL** cite the relevant `SlotFillingsPlanItem` refs via `PlanItemRefs[]` (nil‑elision when not applicable).

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific definition records beyond the pinned governing spec refs (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — CSLC-admissible orders and arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 `PortfolioMode` / selected-set semantics). Additionally: any numeric comparison or aggregation invoked by parity **SHALL** be CSLC-admissible and cite the corresponding CG‑Spec entry; non-admissible operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (citation only; arithmetic admissibility comes from `CG‑Spec`/`MM‑CHR`).

4. **CC‑G9.4 — Normalization discipline (local citation only).**
   If Characteristics differ by unit, scale, or space, the ParityPlan **SHALL** cite the CSLC-admissible comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible/auditable without out‑of‑band context.
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/PortfolioMode interpretation & telemetry separation (local).**
   ParityPlan/ParityReport **SHALL** either (i) explicitly pin the applicable regime/mode via refs/policy‑ids, or (ii) cite the corresponding defaults for `DefaultId.DominanceRegime` and `DefaultId.PortfolioMode` via `G.Core.DefaultGoverningDefinitionIndex`. Any non‑default “promotion” behaviour must be policy‑bound and recorded via policy‑id pins.
   IlluminationSummary/coverage/regret **SHALL** be treated as telemetry (report‑only by default); any promotion into dominance is an explicitly pinned CAL policy and MUST be recorded in audit pins/SCR.

5a. **CC‑G9.5a — Adaptation parity disclosure (local; conditional).**
   When the parity claim concerns bounded specialization, the ParityPlan and ParityReport **SHALL** pin the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and any transfer, retention, downstream exploitation efficiency, downside field, or corridor-entry baseline/evidence note that materially affects comparison.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing visibility (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge and reference-plane crossing visibility plus R-channel penalty placement discipline.

8. **CC‑G9.8 — Evidence trace completeness (local).**
   A ParityReport **SHALL** include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering both inclusions and refusals/abstains/degrades.

9. **CC‑G9.9 — Telemetry hooks are emitted with pins (local).**
   When parity emits telemetry for refresh, emitted telemetry **SHALL** carry the active edition pins and policy‑ids needed to re‑run parity (including the active subset of `ParityPinSet` relevant to the emitted event).
   In particular, telemetry items SHOULD cite `PathSliceId` when available, and **SHALL** include the policy id governing the telemetry interpretation.
   Mode‑specific definition pins **SHALL** be included as declared by the active `Extensions` blocks (e.g., `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`, including `EnvironmentValidityRegionId` when OEE parity is in scope).

10. **CC‑G9.10 — RSCR parity tests are published (local).**
   Parity publication **SHALL** include RSCR parity tests (via `F.15` harness refs) that cover negative/refusal paths relevant to this plan (missing pins, edition drift, missing bridge calibration refs, etc.).

11. **CC‑G9.11 — GateCrossing visibility (delegation point).**
    Delegated to `CC‑GCORE‑CROSS‑1` and the applicable GateCrossing/CrossingBundle harness checks (`E.18`, `A.21`, `F.9`, and relevant Part G bridge or crossing wiring). This remains a stable delegation point.

12. **CC‑G9.12 — Tech‑register lexical discipline (local).**
    Tech prose and heads **SHALL** follow E.10: do not introduce drift‑prone primitives (e.g., “metric” as a Tech primitive); reference the source pattern's canonical terms and pinned refs.

13. **CC‑G9.13 — MOO disclosure for parity (local).**
    `Run_Parity` / `Publish_ParityReport` **SHALL** record the ParityHarness identity (UTS ids) and the active pins required to interpret the outcome (editions + policy‑ids), so parity remains auditable without relying on “decision logs”.

14. **CC-G9-CLP-1 - Causal method rung parity.** If a parity report compares causal methods, it SHALL first run `CausalRungParityScreen`; when full parity remains plausible, it SHALL declare target causality-ladder rung, causal-use claim kind, `estimandRef`, interventional-action basis, causal evidence support basis, transportability basis for the source population and target population when needed, estimation-validity basis when needed, bridge and loss relation where rungs differ, `causalUseSupportRecordRef` and `causalUseSupportVerdict` when relevant `C.28` support is consumed, and degraded or abstain posture where parity cannot be established.


### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross‑Context reuse without visible crossing pins.** Remedy: cite Bridge/reference-plane records and crossing visibility records (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve CSLC-admissible outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by the governing policy pattern.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: use `DHCMethodRef`/`U.Measure`/`DistanceDefRef` with editions; “metric” may appear only in Plain with an explicit pointer to canonical terms.
* **AP‑7 Hidden spec drift (spec edition pins missing).** Remedy: pin `DHCMethodSpecRef.edition` and register RSCR tests that fail on spec edition changes; refuse parity reuse on unpinned spec editions.

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a selected-set outcome plus the evidence trace. Family labels such as preference-learning comparators, causal decision pipelines, offline-RL evaluation pipelines, and robust BO-style selectors remain illustrative until a `G.2` SoTA pack or named current source pins the exact family being compared; the parity report still must preserve the selected set or partial order rather than collapse everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage → CMA‑ME / DQD / QDax JMLR 2024, with QDHF or QDAIF refs only when a feedback-guided QD claim is live).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET as lineage; current generator-family claims require a named `G.2` SoTA pack or exact current source).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes selected-set outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

**Show-D — Causal method rung parity.**
A team compares an observational predictor, an intervention optimizer, and a counterfactual policy strategy under one "best causal method" headline. `G.9` first runs `CausalRungParityScreen`: if rungs, support bases, estimands, or outcome windows differ, the screen returns degraded parity or abstain before a full record is fabricated. When full parity remains plausible, `G.9` requires `CausalMethodRungParityRecord`: each method declares `targetCausalUseClaimKind`, target `CausalityLadderRung`, `estimandRef`, interventional-action basis, `CausalEvidenceSupportBasis`, relevant `C.28` support record and verdict when consumed, follow-up window, outcome measure, source population and target population basis, and estimation-validity basis. If those fields differ, the parity report names `declaredCausalityLadderBridgeOrLossRef`, transportability or estimation refs where available, and degraded or abstain posture. The admissible output may be a selected set by comparable rung, not one scalar winner.

### G.9:9 — Cited Records (what this pattern publishes)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan@Context` (WorkPlanning plan item)
* `ParityReport@Context` (UTS publication record; work-result or audit-facing publication record only when the neighboring source relation is live)
* DRR+SCR refs (by id) and (when applicable) `PortfolioPackRef?`/selector output refs (by id), for downstream consumption.
* Telemetry pins/events (by id), for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

### G.9:10 — Relations

**C.27 temporal-claim relation.**

- C.27 may flag: dynamic parity when a benchmark actually compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome.
- This pattern keeps: baseline, freshness, comparator edition, effort/budget parity, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: faster improvement is not benchmark superiority, and `dyn2BenchmarkParityBlock?` is a benchmark input declaration, not a benchmark harness.
- Exit: when live, recover `dynOrderCompared`, baseline window, adaptation/intervention window, effort or budget parity reference, rate/rate-change measure, `G9ParityPlanRef`, and optional `G9ParityReportRef`; G.5 is relevant only if selector publication consumes such a benchmark result.

**C.29 mathematical-lens adequacy relation.**

- C.29 may flag: parity or benchmark input whose comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, parity measure, model-family label, or model-selection basis carries a load-bearing mathematical lens that is missing, under-specified, or overread.
- This pattern keeps: baseline set, freshness, comparator edition, normalization ids, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: a `C.29` output does not publish a benchmark report, create benchmark superiority, supply selector output, or supply parity-measure admissibility by itself.
- Exit: for an under-lensed or overread parity input, cite the applicable `C.29` output for the stated use: `NoMLANeeded`, `MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, or `NeighborGoverningLocusNote`. Use the cheap output that changes the next admissible parity move; full-card work is only required when the live parity or benchmark claim needs it.


**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.17`, `E.18`, `A.21`, `F.17`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping publication form; parity records are cited records).
**Uses:** **G.0**, **A.19**, **F.9**, and `C.28` when parity compares causal methods or causal-use claims.
**Uses (optional, via Extensions):** **G.7**, **C.18 and C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

### G.9:11 — Working reading checks

- If two baselines are being compared under different freshness windows, comparator editions, or silent normalization rules, this pattern has not yet been satisfied.
- If parity cannot tell the reader what was held constant, what remained telemetry, and what crossings or penalties were active, the report is not yet usable.
- If a scalar winner is being claimed where only a selected set or partial order is CSLC-admissible, parity is overclaiming and should publish the CSLC-admissible outcome shape instead.

### G.9:End
