## G.11 - Telemetry-Driven Refresh and Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
> **Status:** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time and maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit publication units and records).** `RefreshQueue`, `RefreshPlan@Context` (WorkPlanning plan item), `RefreshReport@Context` (Work or Audit record), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue, alias docking, and Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge Sentinels; CL, Φ, and plane policy pins), `G.5` (set-returning selection and dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness and decay), `E.18` (GateCrossing and CrossingBundle visibility), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support records whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note.**
`G.11` cites `G.Core` for RSCR trigger-kind meaning, CN and CG admissibility, tri-state guards, penalties, set-return semantics, shipping or harvesting delegation, `RSCRTriggerKindId` values, and default governing definitions.
Refresh plans and reports cite those governed definitions; they do not create local trigger meanings or default definitions inside the refresh record.

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, or parity result may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, or source currentness changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner gets a small refresh kit: name the affected object, currentness object kind, source record, edition or lineage pins, affected scope, governing pattern, planned refresh action, and report. The refresh can stay local while still preserving comparability, selected-set meaning, archive and front meaning, and source-currentness evidence.

#### G.11:0.3 - First output
For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not create a local "reopen and refresh" pair and does not decide whether the artifact improved.

Write one `RefreshCurrentnessLine@Context` or one `RefreshPlan@Context` with the affected scope and direct governing pattern named. If the meaning belongs to selected-set publication, archive or front stewardship, cultural evolution, term bridges, evidence, dashboard, or shipping, cite that governing pattern rather than defining the meaning inside the refresh record.

Framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions are refresh and currentness claims governed here when currentness is the live question. Record the framework-specific trigger and cite `E.4`, `E.4.PFR`, `E.4.PFAD`, `G.2`, `E.11`, or `E.17` as the direct owner of the affected framework, source, decision, or publication meaning instead of creating a private refresh vocabulary in the framework pattern.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **decay** (freshness windows expire; epistemic debt grows),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

Without an explicit orchestration kit, refresh becomes either:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only refresh result that silently accumulates drift.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: it turns typed refresh causes into **scoped plans** and **auditable execution reports**, while delegating all cause semantics and universal invariants to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and admissibility

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Local trigger aliases are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS, Path, or policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance, `PortfolioMode`, or Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Refresh is triggered by run-time telemetry and decay, yet must remain auditable as Work (pins, refs, paths), not as opaque “decisions.”
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration kit

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  RSCRTriggerSetIds := {GCoreTriggerSetId.RefreshOrchestration},

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    RSCRTriggerKindId,
    RSCRTriggerAliasId?,
    scope: PathSliceId[] | PatternScopeId,
    payloadPins{…},

    RefreshPlanId,
    RefreshReportId,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    SlotFillingsPlanItemRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩`

By the `G.Core` **Expansion rule**, the **effective** conformance ids, trigger kinds, and pin obligations for `G.11` are the manifest expansions (profiles, sets, and pin sets) plus the explicit deltas above.

**TriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (pattern-governed; conceptual artefacts)

`G.11` defines a minimal kit of *authoring-plane* artefacts that make refresh explicit and auditable.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (WorkPlanning plan item).**
   A planned refresh is a WorkPlanning object that **does not execute Work** and **does not embed gate decisions**. It declares:

* `RefreshPlanId` (UTS-published id; editioned)
* `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
* `TargetScope := PathSliceId[] | PatternScopeId[]`
* `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
* `PlannedActions := RefreshAction[]` (each action delegates to a governing pattern)
* `RequiredPins := {EditionPins, PolicyPins, UTS pins, Path pins}` for replayability
* `PlanItemRefs := SlotFillingsPlanItemRef[]` (when planning baselines or reruns requires explicit planned slot fillings)

3. **`RefreshReport@Context` (Work or audit artefact).**
   An execution report (Work or Audit artefact) that records:

* `RefreshReportId` (UTS-published id; editioned)
* `ExecutedActions[]` with links to cited artefacts governed by cited patterns (e.g., new parity report id, new pack id)
* `ObservedDeltas` (telemetry deltas, admissibility changes, evidence-relation or source-relation changes) as refs and pins, not as untyped prose
* `RSCRRefs[]` (any RSCR or regression harness artefacts invoked)
* `EmittedNotices[] := DeprecationNoticeId[]` and `EditionBumpLogId[]`
* the canonical trigger kinds actually applied (not only aliases)

4. **`DeprecationNotice@Context` and `EditionBumpLog@Context`.**
   Controlled evolution artefacts that preserve ID-continuity:

* **DeprecationNotice** explains scope, reason class (canonical trigger kind ids), and successor refs.
* **EditionBumpLog** records edition increments and the pins that justify them.

> *Note (normative by delegation).* ID continuity and alias discipline are governed by `G.Core` (do not restate as local rules here).

#### G.11:4.2a - Selected-set, archive, and cultural-variant currentness

Use this line when refresh currentness concerns a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, or path slice.

```text
RefreshCurrentnessLine@Context:
  governedObjectRef:
  currentnessObjectKind:
  sourceRecordRef:
  editionOrLineagePins:
  affectedPathSliceOrScope:
  directGoverningPatternRef:
  plannedRefreshAction:
  refreshReportRef?:
```

`currentnessObjectKind` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, cultural-variant lineage, style or tradition term bridge, or path-slice scope. G.11 records the refresh plan, scope, pins, report, and deprecation or edition-bump publication. It does not define selected-set publication, archive or front semantics, cultural-evolution semantics, or term-bridge semantics. Use `G.5`, `C.18`, `C.19`, `C.36`, `F.17`, `F.18`, and `F.9` for those meanings.

Freshness and currentness are handled by `RefreshPlan@Context`, `RefreshReport@Context`, `DeprecationNotice@Context`, and `EditionBumpLog@Context`; do not add a separate ticket kind for the same concern.

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)



`G.11` turns typed causes into scoped actions without governing the semantics of those actions.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness and decay events (`B.3.4`),
* evidence, bridge, policy, or edition edits (from the respective governing patterns’ publication faces, forms, or units).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence and source relations, with `G.6` `PathId` and `PathSliceId` refs when a graph path slice is the current math-lens expression,
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions and policies).

The closure is a *planning-time claim* (“these slices are affected”), not a Work-time output.

**4.3.3 Planning (P2W boundary).**
Produce `RefreshPlan@Context` that schedules actions of the form:

* `RerunHarvest` (delegates to the selected harvest, source-currentness, or SoTA governing definition named by value, such as `G.1` or `G.2`, when that definition is current)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetPublication` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates to `G.7` and visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
Execute planned actions as Work (or Work-bound audit) and publish `RefreshReport@Context`.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped pack, parity report, evidence relation, source relation, dashboard slice, fairness audit, policy evaluation, or selector output consumes `C.28`, refresh planning includes causal-use sentinel causes when they can change supported use, unsupported use, support verdict, or downstream assurance:

| Causal-use sentinel | Typical affected C.28 result or related claim | Refresh payload pins |
| --- | --- | --- |
| counterfactual-realizability shift | `CounterfactualSamplingRealizabilityProfile`, `realizedCounterfactualSampleSupportBasis`, causal evidence design | profile refs, action-primitive refs, work-plan refs, physical, ethical, and operational constraint refs, target counterfactual distribution refs, admissible-use refs, and unadmissible-use refs |
| counterfactual-data identification and bounding shift | `CausalIdentificationProfile`, `identifiedCounterfactualEstimateSupportBasis`, bounds or partial-identification result | available data regime set refs, realized counterfactual data refs, counterfactual-data identification method refs, counterfactual-data bound refs, assumption refs |
| target-trial reporting shift | `TargetTrialProtocolRecord`, `TargetTrialEmulationMappingRecord`, applied intervention-effect support verdict | protocol refs, observational data source refs, eligibility, treatment, time-zero, and assignment mappings, follow-up and outcome mappings, emulation-gap refs, residual-confounding and sensitivity refs and additional-analysis refs |
| causal-fairness shift | `CausalFairnessUseAuditCard`, causal fairness support verdict, fairness assurance | protected-variable refs, decision-variable refs, and outcome-variable refs, permitted-path refs and prohibited-path refs, fairness estimand refs, causal-use question refs, support basis refs, support record refs and verdict refs |
| causal-representation-validation shift | `CausalVariableRepresentationRecord`, learned causal-variable admissible use | intervention-validity, mechanism-invariance, abstraction-fidelity, counterfactual-query-preservation, representation-shift refs, OOD refs, supported-causal-variable-use refs, and unsupported-causal-variable-use refs |
| off-policy or causal-RL evaluation shift | `OffPolicyCausalEvaluationProfile`, causal action-policy admissible use, policy parity | behavior-policy refs and evaluation-policy refs, sequential horizon refs, adaptive policy class refs, unit-history conditioning refs, overlap refs and support-basis refs, policy transportability refs, estimator and uncertainty refs |
| simulation-validation shift | `simulationOnlyCounterfactualOutputBasis`, bounded model-supported counterfactual use | counterfactual model assumption refs, simulation validation refs, `CausalUseSupportStatement` and `CausalUseUnsupportedStatement` refs, sensitivity and rival-cause refs |

These sentinels do not mint new `RSCRTriggerKindId` values. They are domain-facing payload distinctions carried under the canonical trigger kinds governed by `G.Core`, usually evidence-publication edit, edition-pin change, policy-pin change, telemetry delta, freshness or decay event, or tokenization or name change.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring live as `GPatternExtension` blocks. Scheduling, ordering, priority, and budget policy for the refresh queue are not separate extension semantics: `G.11` governs the required policy pins on `RefreshQueue` and `RefreshPlan@Context`, while `A.15` keeps WorkPlanning separate from executed Work.

##### G.11:Ext.TriggerAliases

**PatternScopeId:** `G.11:Ext.TriggerAliases`
**GPatternExtensionId:** `TriggerAliases`
**GPatternExtensionKind:** `InteropSpecific` (alias docking)
**GoverningPatternId:** `G.Core`
**Uses:** `{G.Core}` (cites `G.Core.TriggerAliasMap.G11`)
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `RSCRTriggerKindId[]` (canonical ids recorded on triggers)
* `RSCRTriggerAliasId?` (e.g., `G.11:T0…T7` as labels only)
* `scope: PathSliceId[] | PatternScopeId`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (freshness and decay semantics)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `FreshnessWindowDeclRef` (or equivalent window pin, as defined by the governing definition)
* `DecayPolicyIdRef` or `EpistemicDebtBudgetRef` (policy-bound)
* `PathSliceId[]` (affected evidence carriers)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** Any budget or priority logic remains policy-bound; `G.11` only wires decay events to refresh planning.

##### G.11:Ext.QDRefreshWiring

**PatternScopeId:** `G.11:Ext.QDRefreshWiring`
**GPatternExtensionId:** `QDRefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` (QD semantics; descriptor, distance, and insertion)
**Uses:** `{C.18, C.19, G.5, G.8}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `DescriptorMapRef.edition`, `DistanceDefRef.edition`
* `CharacteristicSpaceRef.edition?` (required when a domain-family coordinate is declared by the QD governing definition)
* `InsertionPolicyRef`, `EmitterPolicyRef` (policy-bound)
* `PathSliceId` (archive or illumination scope) and `policy-id` for emitted telemetry triggers

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.

##### G.11:Ext.OEERefreshWiring

**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration and exploration-exploitation logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the governing patterns)
* `GeneratorFamilyId` and `TransferRulesRef` wiring pins (as published by the governing definitions)
* telemetry scope pins (`PathSliceId`, `policy-id`)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:4.4a - Scheduling and priority policy pins

Scheduling strategies (bandit-style allocation, queueing, cadence policies, early stopping, or manual priority rules) may influence the order and budget of refresh work, but they do not define trigger meaning, action semantics, parity semantics, shipping semantics, or Part-G-wide defaults.

`G.11` therefore treats scheduling as policy-bound refresh planning:

* `RefreshPriorityPolicyIdRef` names the policy used to order or prioritize queue items.
* `BudgetDeclRef` names the time, compute, cost, risk, or cadence boundary for the planned refresh.
* `RSCRTriggerKindId[]` still comes from `G.Core`; scheduling policy does not mint trigger kinds.
* planned refresh remains `RefreshPlan@Context` under WorkPlanning; executed refresh remains `RefreshReport@Context` or Work-bound audit.

If no priority or budget policy is declared, no scheduling heuristic is admissible by appearance; the plan must either use the ordinary queue order or state the missing policy pin as a blocker.

### G.11:5 - Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices and publishes a refresh report with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by governing pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL or plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

### G.11:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions and policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: the kit is intentionally thin: refresh queue entries, `RefreshPlan@Context`, and `RefreshReport@Context` stay explicit, while action semantics remain delegated to governing definitions.
* **Onto and Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System and Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose and Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion plus explicit deltas; delegated to `G.Core`).                                                                                                                                       | `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD and OEE wiring).**     | When QD, OEE, or both are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin, edition, and policy wiring of the applicable extension blocks: `G.11:Ext.QDRefreshWiring`, `G.11:Ext.OEERefreshWiring`, or both. **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while keeping method-specific pin lists inside the applicable extension blocks.                  |
| **CC‑G11.3 (Telemetry-metric admissibility).**             | If a refresh publishes Illumination, QD, or OEE outcomes, it **SHALL** publish **Q, D, and QD‑score** and any coverage or regret as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy id SHALL be recorded** in SCR-visible evidence bindings through the cited governing patterns.                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge or plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL`, `CL^k`, `CL^plane`, and the relevant `Φ`, `Ψ`, and `Φ_plane` policy ids with loss notes so penalties are assigned to `R_eff` only (F and G invariant).                                                                                                                                | Keeps penalty assignment auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set or archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (`Pareto` or `Archive`) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross-context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef`, BridgeCard, UTS, and `CL` or `Φ_plane` policy ids. Missing or non-conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness or decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh**, **Deprecate**, or **Waive**) with **budget notes** (policy-bound), and **SHALL** publish the decision through `DeprecationNotice@Context` and related pins plus SCR-visible evidence bindings through `G.6` or cited governing patterns.                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`, dominance, Γ-fold, or guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` and the applicable governing patterns rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re-shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR or regression check for the affected scope and record `RSCRRefs[]` or equivalent refs in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade` or `abstain` outcomes (policy-bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice-scoped.                                         |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed publication or output consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification and bounding, target-trial reporting, causal fairness, causal representation validation, off-policy and causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped causal-use results while preserving `G.Core` trigger governance. |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context or plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins and E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Debt-by-prose**                  | “We decided not to refresh” exists only in narrative              | Not comparable; cannot be tested                         | Emit a DeprecationNotice (incl. a Waive outcome, if used) with pins (CC‑G11.7)    |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning and execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear governing-definition assignment boundaries.** Orchestration coordinates governing definitions; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids, editions, and policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop is powerful enough to coordinate reruns and republishing, but **too thin to become a second spec**. That is why trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W planning-to-work boundary** so that WorkPlanning plan items remain planning references and executed work remains auditably executed work.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

0. **Queue-7 QD currentness requires visible survey support.**
   Practice: current QD work is surveyed as approaches, applications, and challenges, with archive, diversity, descriptor, and evaluator-currentness concerns still live.
   Source: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 2026, DOI `10.1016/j.swevo.2025.102240`.
   Alignment: `RefreshCurrentnessLine@Context` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, descriptor or distance edition, and path-slice scope, while `C.18`, `C.19`, and `G.5` keep archive, pool, and selected-set meanings.
   Adoption: **Adopt and bound** (survey support changes refresh currentness fields and boundaries; it is not the governing ontology source).

0a. **Open-ended engineering outputs need source and evaluator currentness.**
   Practice: self-improving-agent, AlphaEvolve-style, and DeepEvolve-style lines use generated variants, external knowledge, evaluators, tests, archives, and empirical validation.
   Source: Darwin Godel Machine `arXiv:2505.22954`, AlphaEvolve `arXiv:2506.13131`, and DeepEvolve-style deep-research augmentation `arXiv:2510.06056`.
   Alignment: G.11 refresh records carry source, evaluator, descriptor, policy, edition, lineage, and report refs; generated method text, evaluator success, and archive update keep their governing patterns.
   Adoption: **Adopt and adapt** (refresh tracks currentness and smallest affected scope; it does not accept generated text as proof, gate passage, or performed work).

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring, retraining, and reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (`arXiv:1706.04599`, 2017); Amershi et al., *Software Engineering for Machine Learning* (ICSE-SEIP 2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition and policy pins for replay.
   Adoption: **Adopt and adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift and decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (`arXiv:1802.07569`, 2019); De Lange et al., *A Continual Learning Survey* (`arXiv:1909.08383`, 2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor and distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy and edition conditions.
   Source: contemporary QD families such as CMA-MAE (`arXiv:2205.10752`) and differentiable QD (`arXiv:2106.03894`).
   Alignment: QD-specific meaning lives with the governing patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set and archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (`arXiv:1901.01753`, 2019); later generator-family claims require a named `G.2` SoTA pack or exact current source.
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt and adapt** (adapted to Part G pin and UTS publication discipline).

5. **Efficient orchestration benefits from bandit and early-stopping scheduling, but it must not become semantics.**
   Practice: modern hyperparameter and experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: ASHA (`arXiv:1810.05934`) and BOHB (`arXiv:1807.01774`) as representative post-2015 scheduling practice.
   Alignment: scheduling is expressed as `RefreshQueue` and `RefreshPlan@Context` policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and WorkPlanning stays separate from executed Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; Default Governing Definition Index), `G.6` (EvidenceGraph, `PathId` and `PathSliceId`), `G.7` (Bridge sentinels; CL, Φ, and plane pins), `G.5` (selector and set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness and decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.32.P2S` when telemetry, decay, or freshness reopens architecture problem-to-structure carry-through, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support records, support verdicts, supported-use values, unsupported-use values, and SoTA-sensitive causal-use sentinel payloads), `F.15` (RSCR harness publications, when present).
**Publishes to:** UTS (refresh plan, refresh report, deprecations, edition bumps), and to the relevant governing patterns’ publication faces, forms, or units through delegated actions.

### G.11:End

