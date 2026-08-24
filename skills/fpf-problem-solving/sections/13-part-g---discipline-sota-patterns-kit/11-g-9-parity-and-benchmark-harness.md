## G.9 — Parity and Benchmark Harness

> **Status:** Stable

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

### G.9:0.1 — What goes wrong if missed

- benchmark numbers mix different windows, baselines, or comparator editions and still pretend to be comparable
- reuse across distinct source-local meanings, a reference-plane crossing, or a normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

### G.9:0.2 — What this buys

- one exact `ParityPlanRef` that fixes the plan edition, baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport` that cites that exact plan and echoes its active baseline binding, pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs for one explicit subject—either one `EntityOfConcernRef` or target refs under their existing subject patterns—with a `ReferencePlane`, scope, window, applicable rules, CSLC comparability and admissibility references, comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`), and reproducibility pins for editions and policy ids;
* executes parity in a way that **G.5** can consume, with selected-set outcomes and a DRR and SCR evidence trace;
* publishes an edition-pinned **ParityReport** suitable for downstream consumption, shipping, refresh wiring, and RSCR.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window and freshness regime,
* comparator semantics, including any normalization or comparability mapping,
* the active C.21 replay basis when DHC coordinates are compared, including the exact Characteristic, Scale, measurement definition, Method, MethodDescription or model, and time or population basis,
* reuse across distinct F.17 source-local meanings or ReferencePlanes (the obtaining relation, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to make these recoverable as **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new governing spec refs.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement and comparator definitions. When DHC, QD, or OEE modes are used, the required definition pins are introduced only through the corresponding `Extensions` blocks; omit them when unused.
* **Telemetry versus objectives.** `IlluminationSummary`, coverage, and regret are report-only telemetry by default. A dominance change needs an explicit CAL policy id recorded in the audit pins.
* **Crossing visibility.** Every crossing used by parity must be visible and auditable through its `CrossingBundle` and `GateCrossing` checks; failure blocks publication or use of the parity result.
* **Cross-sense and reference-plane reuse.** When expressions have distinct F.17 source-local meanings, recover both cells and establish the required F.9 relation; a ReferencePlane crossing follows its own declared crossing basis. Each actual crossing carries explicit pins, its audit evidence relation, and R-channel penalty placement.
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
  `RSCRTriggerKindId.EvidencePathOrSourceRelationEdit`,
  `RSCRTriggerKindId.PenaltyPolicyEdit`,
  `RSCRTriggerKindId.BaselineBindingEdit`,
  `RSCRTriggerKindId.TelemetryDelta`
  }
  *(Pattern-local deltas; cross-tradition or Bridge-calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over-trigger parity runs that use one already recovered meaning and ReferencePlane.)*

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
  `entityOfConcernRef?`, `targetRefs[]?`, *(exactly one subject branch)*
  `ClaimScope`, `EvaluationWindow`, `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlannedFillingRows[]?`,
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

**(1) `ParityPlan`** *(one exact `U.WorkPlan` episteme; `ParityPlan` is the local application name)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan := ⟨
  ParityPlanId(UTS),                       // continuing plan lineage
  planEdition,                            // one immutable edition
  CGFrameId?,                              // exact cited CG frame when the plan depends on one
  entityOfConcernRef? := EntityOfConcernRef, // one-EntityOfConcern branch only
  targetRefs[]?,                            // exact-target branch only; existing kinds and editions
  groundingHolonRef := GroundingHolonRef,
  referencePlaneRef := ReferencePlane,
  claimScopeRef := ClaimScope,
  EvaluationWindow,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  BaselineSet,                            // exact method-family or generator-family targets (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  EvidenceGraphId, PathId[], PathSliceId?,
  PlannedFillingRows[]?                    // declaration-local A.15.3 content inside this WorkPlan; no independent row refs
⟩`

`ParityPlanRef := <ParityPlanId, planEdition>` designates one immutable plan edition. Changing its subject, baseline binding, comparator edition, or another active value that can change the run or its interpretation creates a new `planEdition`. The lineage id may remain only while this is still the same continuing plan; old `ParityPlanRef` values continue to resolve their old editions.

Exactly one subject branch is present. Use `entityOfConcernRef` when the report compares results about one EntityOfConcern. Use `targetRefs[]` when the targets themselves are compared; each ref keeps the kind and edition defined by its existing subject pattern. In particular, a G.5 method-family target is an exact `MethodFamilyRowRef`, and a generator-family target is an exact `GeneratorFamilyRowRef`.

For example, a direct comparison of `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>` puts those two exact row refs in `targetRefs[]`; the plan may explicitly use the same two refs as its `BaselineSet`. A comparison of their results for `Pump-P17` instead puts `Pump-P17` in `entityOfConcernRef`, leaves `targetRefs[]` absent, and uses `BaselineBindingRef` to say how the two method rows supply results about that pump.

`BaselineSet` names the alternatives treated as the comparison baseline; it supplies `targetRefs[]` only when the plan explicitly says that the same exact refs serve both purposes. Otherwise the subject and baseline remain separate, and `BaselineBindingRef` records how that baseline applies to the named subject. These exact values determine what is compared and when the parity claim is usable; do not add `ParityContextId`. If the plan relates expressions with distinct source-local meanings, first recover the exact F.17 cells and establish the required F.9 relation. A shared label, source note, or generic context identifier does not establish comparability.

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by running one exact `ParityPlanRef`. By itself it is not a dated `U.Work` occurrence, audit performance, evidence path, assurance result, or gate decision; those claims require A.15 and A.15.1, A.10 and G.6, B.3, or A.21 respectively.

`ParityReport := ⟨
  ParityReportId(UTS),
  parityPlanRef := ParityPlanRef,
  entityOfConcernRef?, targetRefs[]?,        // exactly one subject branch is present
  groundingHolonRef, referencePlaneRef,
  claimScopeRef, EvaluationWindow,
  BaselineSet, BaselineBindingRef, FreshnessWindows,
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

The report carries the exact `ParityPlanRef` and echoes the `BaselineBindingRef` used in that edition. For example, if `<PumpParityPlan, E4>` used `PumpBaselineBinding-E7` and a later `E5` changes the binding or comparator, an old report still resolves `E4` and `PumpBaselineBinding-E7`. A missing historical plan edition or binding is an unresolved required input; it is never replaced with the current value.

**Naming discipline.**

* Heads reuse existing U‑types and LEX discipline; no new “strategy” primitive is minted here.
* The older labels `ParityPlan@Context` and `ParityReport@Context` are retired. The suffix named neither identity nor comparison basis; current records are `ParityPlan` and `ParityReport`, with all operative conditions carried in explicit fields and exact refs.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (one exact `U.WorkPlan`)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the exact `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) used as the comparison baseline. When SoS-log or source-maturity values change baseline eligibility or interpretation, cite `SoS‑LOGBundleId?` and the source-maturity ids by reference; acceptance-gate thresholds remain in `G.4` Acceptance.
2. **Bind subject, scope, and evaluation window.** Choose exactly one subject branch: one `entityOfConcernRef`, or exact `targetRefs[]` under their existing kinds and editions. For G.5 families, use `MethodFamilyRowRef` or `GeneratorFamilyRowRef`, not a bare lineage id. Then fix `groundingHolonRef`, `referencePlaneRef = ReferencePlane`, one exact `ClaimScope`, and `EvaluationWindow`; record them without silent widening, narrowing, collapse of an EntityOfConcern into the grounding holon, or window drift.
3. **Define baseline-set reference.** Declare what counts as the baseline and how it applies to the selected subject in `BaselineBindingRef` (for example, through an EvidenceGraph path slice or an upstream shipped package or publication-record id). If `BaselineSet` also supplies the exact compared targets, say so and use the same refs by value; otherwise keep baseline and subject refs distinct.
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

   When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned fillings when applicable.** If parity depends on planned slot fillings, this WorkPlan contains the relevant A.15.3 rows in `PlannedFillingRows[]`; each row points to a declaration member defined by its own pattern and has no independent reference or identity. Omit the field when no such row is needed.
10. **Publish crossing pins (when invoked).** When expressions have distinct recovered F.17 meanings, establish the required F.9 relation and publish its Bridge and CL pins; ReferencePlane or Kind crossings cite their own exact crossing basis and pins. Penalties affect `R_eff` only (invariants pinned through `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; run eligibility or acceptance checks under the plan’s `TaskSignature (S2)` and refuse or abstain on non-admissible operations (record trace; no “fourth status”). If a live `A.21` gate consumes this check, cite its `GateDecisionRef`/`DecisionLogRef`; do not create a `G.9`-local CSLC gate.
2. **Invoke selection/dispatch.** Apply **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s `PortfolioMode` and selected-set semantics.

   When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record the comparability mapping when used.** If `UNM_id?`, `NormalizationMethodId[]?`, or `NormalizationMethodInstanceId[]?` was declared, echo it in `ParityReport` or its explicit pins delta. Record the ids and any scoped notes required by the cited specification in the audit pins and SCR; cite the applicable `PathId` values.
4. **Publish trace.** Emit `ParityReport` with the exact `ParityPlanRef`, its `BaselineBindingRef`, EvidenceGraph citations, and all active edition and policy-id pins, so the run can be checked and run again.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

**Ordinary case: compare two pump-triage method rows.** The team from the G.5 example wants a reproducible comparison of the two exact selector-row editions, not a claim that one Method is universally better. Both rows use the same scheme, units, and ReferencePlane, so no normalization or crossing branch is needed.

```text
ParityPlanRef = <PumpTriageParity, E1>
targetRefs = [<ThresholdTrendReview-local, R3>,
              <SpectralResidualReview-local, R2>]
entityOfConcernRef = absent
groundingHolonRef = PumpMaintenanceProgram-H1
referencePlaneRef = PumpVibrationTriage-RP1
claimScopeRef = PumpFleet-F7-VibrationTriageClaims-E1
EvaluationWindow = 2026-08-01T00:00Z .. 2026-08-07T23:59Z
BaselineSet = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>]
BaselineBindingRef = PumpTriageBaselineBinding-E1
FreshnessWindows = { sensorSeries: at-most-24h-old-at-run,
                     evidencePath: at-most-72h-old-at-run }
CNSpecRef.edition = PumpCN-E2
CGSpecRef.edition = PumpCG-E4
ComparatorSpecRef.edition = PumpTriageComparator-E3
ParityPinSet = [PumpVibrationMeasureSpec-E2]
EvidenceGraphId = PumpTriageEvidence-E5
PathId[] = [PumpReadings-P7, ComparatorRun-P3]
PathSliceId = PumpParitySlice-S2
expected selector result = unordered Shortlist
```

The plan explicitly says that `BaselineSet` and `targetRefs[]` contain the same two row refs. `EvaluationWindow` bounds the observations and results included in the comparison. `FreshnessWindows` asks a different question at run or reuse time: whether each required input and evidence path is still recent enough to rely on. A report from this run carries `parityPlanRef=<PumpTriageParity, E1>`, `BaselineBindingRef=PumpTriageBaselineBinding-E1`, the same evidence path, and the unordered `Shortlist`; it does not invent a scalar winner. A cold reader can therefore recover the subject, comparison boundary, two window meanings, measurement and comparator editions, and evidence without opening a causal, crossing, assurance, telemetry, or publication branch.

**Conditional specialization case.** Loop-engineering parity may add further pins after the ordinary comparison boundary above is complete. An evaluation program, benchmark script, or dashboard is part of the evaluation or comparison procedure; it is not the Characteristic being improved.

- Two agentic search setups both claim bounded specialization on the same declared task family.
- Their `ParityPlan` also pins the same threshold target, adaptation budget, prior-exposure declaration, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- Their CSLC-admissible `ParityReport` states what was held constant, which signals remained telemetry, and why the outcome stays a selected set or partial order rather than collapsing into a scalar winner. These specialization values extend the complete comparison boundary; they do not replace its subject, scope, windows, baseline binding, comparator editions, or evidence.

#### G.9:4.3b — Conditional causal method rung parity

Use this extension only when a parity report compares causal methods or causal-use claims. Start with a cheap screen and stop at degraded parity or abstention when the methods answer different questions.

```text
CausalRungParityScreen:
  comparedMethodsRef
  targetCausalityLadderRungSet
  causalSupportComponentTypeSet
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  sameTransportEndpoints: yes | no | unclear
  cheapParityStop:
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportComponentsDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    differentEndpointsAbstain |
    returnToC28
```

`causalSupportComponentTypeSet` records which methods rely on evidence paths/data regimes, identification, estimates, direct counterfactual sampling, simulation, or transport. Difference is not an automatic ban, but it must be exposed and bridged; one label cannot make unlike components equivalent.

Open the full record only when comparison remains meaningful:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  causalEstimandRef: CausalEstimandRef
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalSupportComponentRefs: CausalSupportComponentRefs
  declaredCausalSupportLossRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  sourceDomainRef?
  targetDomainRef?
  sourceEnvironmentRef?
  targetEnvironmentRef?
  sourceDataGeneratingRegimeRef?
  targetDataGeneratingRegimeRef?
  transportabilityResultRef?
  estimateResultRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

The record names every changed transport endpoint that matters; population and semantic scheme do not substitute for domain, environment, or data-generating regime. Different rungs, estimands, windows, endpoints, or support components require a bridge/loss, degraded parity, or abstention. G.9 makes the parity conclusion; C.28 supplies the cited causal-support result and does not authorize the benchmark conclusion.

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
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Explains **why** a parity run degraded/abstained by citing SoS‑LOG ids and evidence paths; does not redefine guard semantics.

**GPatternExtension block: `G.9:Ext.DHCParityPins`**
**GPatternExtension: DHCParityPins**
* **PatternScopeId:** `G.9:Ext.DHCParityPins`
* **GPatternExtensionId:** `DHCParityPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **Required replay values and pins (minimum; conditional on DHC parity):**
  * `DisciplineRef`
  * `IntendedUse`
  * `ClaimScopeRef`
  * `ComparisonBasis`
  * `CharacteristicRef.edition`
  * `ScaleRef.edition`
  * `UnitRef.edition?`
  * `DHCMethodRef.edition`
  * `MethodRef`
  * `MethodDescriptionRef.edition?`
  * `MeasurementModelRef.edition?`
  * `CalibrationBasisRef?`
  * `TimeOrPopulationBasis`
  * `DHCDefinitionSetRef.edition?`
  * `TargetSliceRef?`
  * `DistanceDefRef.edition?`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit}`
* **Notes (wiring-only):** Carry exactly the active fields of the C.21 replay basis. `TargetSliceRef` appears only when the parity computation consumes that A.2.6 selection and states its relation to `ClaimScopeRef`. Compatible same-semantics readings use the admitted C.16 comparison basis directly; actual distinct-local-sense use also cites the obtaining F.9 relation, direction, admitted use, and loss. C.21 defines the DHC semantics.

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
| **G.9‑1 `Plan_Parity`**            | exactly one subject branch—one `EntityOfConcernRef` or exact `targetRefs[]` under their existing kinds and editions—plus `GroundingHolonRef`, `ReferencePlane`, `ClaimScope`, `EvaluationWindow`, `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, mode-specific measurement or normalization editions when used, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `EvidenceGraphId`, `PathId[]`, `PathSliceId?`, `PlannedFillingRows[]?` | one immutable `ParityPlan` WorkPlan edition and its exact `ParityPlanRef` |
| **G.9‑2 `Run_Parity`**             | exact `ParityPlanRef`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                | selected-set, archive, or other set refs; DRR and SCR pins with `PathId[]` and, when needed, `PathSliceId` |
| **G.9‑3 `Publish_ParityReport`**   | exact `ParityPlanRef`, parity-run trace refs, and active pins                                                                                   | `ParityReport` carrying the same exact plan ref and baseline binding (UTS publication record; emits canonical RSCR ids) |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, Default Governing Definition Index links, and P2W split).

1. **CC‑G9.1 — Exact comparison boundary, equal windows (and budgets), and pinned spec editions (local).**
   A `ParityPlanRef = <ParityPlanId, planEdition>` **SHALL** resolve one immutable plan edition. That ParityPlan **SHALL** choose exactly one subject branch: one `EntityOfConcernRef`, or `targetRefs[]` under their existing kinds and editions. It **SHALL** also name `GroundingHolonRef`, `ReferencePlane`, `ClaimScope`, `EvaluationWindow`, baseline set and binding, and evidence refs, and **SHALL** declare a single `FreshnessWindows` shared across baselines. `BaselineSet` supplies the target refs only when the plan explicitly identifies the same refs in both places; otherwise `BaselineBindingRef` relates the separate baseline to the named subject. If `Budgeting` is used and pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the editions required by the referenced specification, comparator, and any measurement or normalization method in use (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings, its exact `ParityPlan` WorkPlan **SHALL** carry the relevant declaration-local A.15.3 rows in `PlannedFillingRows[]` (nil-elision when not applicable). Each row resolves only inside that WorkPlan and has no independent reference, kind, or edition.

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific definition records beyond the pinned governing spec refs (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — CSLC-admissible orders and arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 `PortfolioMode` / selected-set semantics). Additionally: any numeric comparison or aggregation invoked by parity **SHALL** be CSLC-admissible and cite the corresponding CG‑Spec entry; non-admissible operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (citation only; arithmetic admissibility comes from `CG‑Spec`/`MM‑CHR`).

4. **CC‑G9.4 — Normalization discipline (local citation only).**
   If Characteristics differ by unit, scale, or space, the ParityPlan **SHALL** cite the CSLC-admissible comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible and auditable without unrecorded information.
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/PortfolioMode interpretation & telemetry separation (local).**
   `ParityPlan` and `ParityReport` **SHALL** either pin the applicable dominance regime and portfolio mode through explicit references and policy ids, or cite their corresponding defaults in `G.Core.DefaultGoverningDefinitionIndex`. Any non-default promotion behaviour must be bound to a policy and recorded through its policy-id pin.
   `IlluminationSummary`, coverage, and regret **SHALL** be treated as telemetry (report-only by default); any promotion into dominance is an explicitly pinned CAL policy and **MUST** be recorded in the audit pins and SCR.

   5a. **CC‑G9.5a — Adaptation parity disclosure (local; conditional).**
   When the parity claim concerns bounded specialization, the ParityPlan and ParityReport **SHALL** pin the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and any transfer, retention, downstream exploitation efficiency, downside field, or corridor-entry baseline/evidence note that materially affects comparison.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing visibility (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge and reference-plane crossing visibility plus R-channel penalty placement discipline.

8. **CC‑G9.8 — Report replay and evidence trace completeness (local).**
   A ParityReport **SHALL** carry the exact `ParityPlanRef` and `BaselineBindingRef` used for the run and include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering inclusions, refusals, abstentions, and degradations. If the historical plan edition or binding cannot be resolved, return that unresolved input instead of substituting a current edition.

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

14. **CC-G9-CLP-1 - Causal method rung parity.** If a parity report compares causal methods, it SHALL first run `CausalRungParityScreen`; when full parity remains plausible, it SHALL declare target causality-ladder rung, causal-use claim kind, `estimandRef`, interventional-action basis, causal support-component refs, exact transport endpoints and transportability result when needed, estimate result when needed, bridge and loss where rungs differ, and `causalUseSupportResultRef` when relevant C.28 support is consumed, and degraded parity or abstain result where parity cannot be established.

### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross-sense or reference-plane reuse without its obtaining relation and visible pins.** Remedy: recover the exact F.17 cells and cite the obtaining F.9 relation when local meanings differ; cite the exact reference-plane crossing basis and visibility records when planes differ (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve CSLC-admissible outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by the governing policy pattern.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: name the exact `CharacteristicRef`, `ScaleRef`, `UnitRef` when applicable, `DHCMethodRef`, `MethodRef`, and `U.Measure` or result episteme; add `DistanceDefRef` only when used. “Metric” may appear only in Plain with a pointer to those canonical objects.
* **AP‑7 Hidden DHC replay drift.** Remedy: carry every active field of the C.21 replay basis and refuse parity reuse when a required field is unresolved or differs across the compared readings. Register refresh tests only for a named receiver that consumes those changes.

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a selected-set outcome plus the evidence trace. Family labels such as preference-learning comparators, causal decision pipelines, offline-RL evaluation pipelines, and robust BO-style selectors remain illustrative until a `G.2` SoTA pack or named current source pins the exact family being compared; the parity report still must preserve the selected set or partial order rather than collapse everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage; CMA-MAE `arXiv:2205.10752`; DQD `arXiv:2106.03894`; QDax `arXiv:2308.03665`; QDHF or QDAIF refs only when a feedback-guided QD claim is live).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET `arXiv:1901.01753` as lineage; AlphaEvolve `arXiv:2506.13131` when the live generator-family claim is coding-agent discovery; other current generator-family claims require a named `G.2` SoTA pack or exact current source).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes selected-set outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

**Show-D — Causal method rung parity.**
A team compares an observational predictor, an intervention optimizer, and a counterfactual policy strategy under one "best causal method" headline. `G.9` first runs `CausalRungParityScreen`: if rungs, support components, estimands, endpoints, or outcome windows differ, the screen returns degraded parity or abstain before a full record is fabricated. When full parity remains plausible, `G.9` requires `CausalMethodRungParityRecord`: each method declares `targetCausalUseClaimKind`, target `CausalityLadderRung`, `causalEstimandRef`, interventional-action basis, the support components actually consumed, relevant C.28 support result, follow-up window, outcome measure, changed transport endpoints, and estimate-result basis. If those fields differ, the parity report names `declaredCausalityLadderBridgeOrLossRef`, transportability or estimation refs where available, and degraded parity or abstain result. The admissible output may be a selected set by comparable rung, not one scalar winner.

### G.9:9 — Cited Records (what this pattern publishes)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan` and its exact `ParityPlanRef` (one `U.WorkPlan` episteme and immutable edition reference; any planned-filling rows remain declaration-local content)
* `ParityReport` (UTS publication record carrying the exact plan and baseline-binding refs; work-result or audit-facing publication record only when the neighboring source relation is live)
* DRR and SCR refs by id and, when applicable, `PortfolioPackRef?` and selector-output refs by id, for downstream consumption.
* Telemetry pins and events by id, for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

### G.9:10 — Relations

**C.27 temporal-claim relation.**

- C.27 may flag: dynamic parity when a benchmark actually compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome.
- This pattern keeps: baseline, freshness, comparator edition, effort/budget parity, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: faster improvement is not benchmark superiority, and `dyn2BenchmarkParityBlock?` is a benchmark input declaration, not a benchmark harness.
- Exit: when live, recover `dynOrderCompared`, baseline window, adaptation or intervention window, effort or budget parity reference, rate or rate-change measure, `G9ParityPlanRef`, and optional `G9ParityReportRef`; G.5 is relevant only if a selector-facing result declaration consumes such a benchmark result.

**C.29 mathematical-lens use relation.**

- C.29 may flag: parity or benchmark input whose comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, parity measure, model-family label, or model-selection basis depends on a mathematical lens that changes the parity claim and is missing, under-specified, or overread.
- This pattern keeps: baseline set, freshness, comparator edition, normalization ids, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: a `C.29` output does not publish a benchmark report, create benchmark superiority, supply selector output, or supply parity-measure admissibility by itself.
- C.29 application: for an under-lensed or overread parity input, cite the applicable `C.29` output for the stated use: `NoMathLensUseNeeded`, `MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, `MathLensUse.FullCard`, or `NeighborGoverningPatternNote`. Use the cheap output that changes the next admissible parity use; full-card work is only required when the live parity or benchmark claim needs it.

**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.17`, `E.18`, `A.21`, `F.17`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping publication form; parity records are cited records).
**Uses:** **G.0**, **A.19**, `A.2.6` for exact `U.ClaimScope`, **F.9**, and `C.28` when parity compares causal methods or causal-use claims.
**Uses (optional, via Extensions):** **G.7**, **C.18 and C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

### G.9:11 — Working reading checks

- If two baselines are being compared under different freshness windows, comparator editions, or silent normalization rules, this pattern has not yet been satisfied.
- If parity cannot tell the reader what was held constant, what remained telemetry, and what crossings or penalties were active, the report is not yet usable.
- If a scalar winner is being claimed where only a selected set or partial order is CSLC-admissible, parity is overclaiming and should publish the CSLC-admissible outcome shape instead.

### G.9:End

