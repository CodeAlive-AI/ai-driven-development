## G.11 - Telemetry-Driven Refresh and Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
> **Status:** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time and maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs, when their use calls for them.** `RefreshQueue`, `RefreshPlan@Context` (a local application name for one exact `U.WorkPlan`, not a new kind), `RefreshReport@Context` (record of refresh Work or its audit), `DeprecationNotice@Context`, and `EditionBumpLog@Context`. Continued reliance on an already applicable result requires none of these solely to prove that refresh was omitted.

**Primary hooks.** `G.Core` (RSCR trigger catalogue, alias docking, and Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge Sentinels; CL, Φ, and plane policy pins), `G.5` (set-returning selection and dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness and decay), `E.18` (GateCrossing and CrossingBundle visibility), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support results whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note.**
`G.11` cites `G.Core` for RSCR trigger-kind meaning, CN and CG admissibility, tri-state guards, penalties, set-return semantics, shipping or harvesting delegation, `RSCRTriggerKindId` values, and default governing definitions.
Refresh plans and reports cite those governed definitions; they do not create local trigger meanings or default definitions inside the refresh record.

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, parity result, or a use that relies on an `A.6.RCD` predicate definition or derived relation kind may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, source currentness, a relied-on base relation definition, the named substrate edition, or derivation applicability changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner first decides what the available support permits for the receiving use. When a changed premise requires upkeep, the refresh kit names the affected object and scope, the source and policy basis, and the justified action. Planning and reporting remain separate, and refresh can stay local while preserving comparability and subject-specific result meanings.

When a later or replacement source may change a claim and the actual receiving uses must first be found and revalidated, use `A.10.1` for the bounded search frame, discovery coverage and gaps, exact-use test, action-changing reach, application of the direct subject guidance, and the independently obtained subject result. `G.11` continues to govern source currentness, decay, refresh planning, and refresh reporting. A practitioner or admitted System may use a separately established currentness result or independently obtained subject result to plan later refresh without changing either result or the governing patterns.

#### G.11:0.3 - First output

For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not decide whether the artifact improved.

First establish whether the current conditions and available basis already support the receiving use. If they do, retain that result without a new currentness line, WorkPlan, waiver or skip-refresh certificate. When a later recipient needs a changed limit or retained reason, keep the minimum useful content with the existing result or publication; a `RefreshCurrentnessLine@Context` can express it when a structured line is useful. Produce a `RefreshPlan@Context` only for selected planned refresh. For an underlying claim about a selected set, archive, culture, bridge, evidence, dashboard or shipping, obtain that subject pattern's result; currentness does not establish its adequacy.

When currentness is the live question, use G.11 to record framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions. In that record, cite `E.4` for the affected framework, `E.4.PFR` for a framework relation, `E.4.PFAD` for the framework architecture decision, `G.2` for source use, and `E.11` for discovery. For publication, cite `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. Do not create private refresh vocabulary for these neighboring meanings.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **currentness conditions** (a relied-on premise changes, a justified review becomes due, or an actual qualification or use window ends),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

The kit addresses two recurring refresh failures:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only refresh result that leaves currentness drift unresolved.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: its users turn typed refresh causes into **scoped plans** and record execution in **auditable execution reports**. Cause semantics and universal invariants remain delegated to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and admissibility

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Local trigger aliases are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS, Path, or policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance, `PortfolioMode`, or Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Actual refresh Work must remain inspectable through the needed pins, references and paths. A currentness decision or an unchanged use must not become a fictitious Work occurrence.
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration kit

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

```text
GCoreLinkageManifest := ⟨
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

    RefreshPlanId?,
    RefreshReportId?,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    WorkPlanRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩
```

By the `G.Core` **Expansion rule**, the **effective** conformance ids, trigger kinds, and pin obligations for `G.11` are the manifest expansions (profiles, sets, and pin sets) plus the explicit deltas above.

**TriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (subject-qualified; conceptual artefacts)

`G.11` defines a kit of authoring-plane artefacts for actual refresh planning and reporting. `RefreshPlanId` is required on a plan and `RefreshReportId` on a report. The linkage manifest applies to the triggers and actions that occur; retaining applicable support creates no trigger, plan or report merely to fill their pins.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (one exact `U.WorkPlan`).**
   A planned refresh is one `U.WorkPlan` episteme under A.15.2. It **does not execute Work** and **does not embed gate decisions**. `RefreshPlan@Context` is only this pattern's application name for the plan; it declares:

   * `RefreshPlanId` (UTS-published id; editioned)
   * `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
   * `TargetScope := PathSliceId[] | PatternScopeId[]`
   * `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
   * `PlannedActions := RefreshAction[]` (each action delegates to a subject pattern)
   * `RequiredPins := {EditionPins, PolicyPins, UTS pins, Path pins}` for replayability
   * `PlannedFillingRows[]?` as ClaimGraph content kept inside the WorkPlan under A.15.3 when a value must be pinned against a declaration member defined by its own pattern. A row is addressed only through the WorkPlan and has no separate reference or identity.
3. **`RefreshReport@Context` (record of refresh Work or its audit).**
   An execution or audit report that records:

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

Use this line when refresh currentness concerns a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, path slice, reused `A.6.RCD` predicate definition, or admitted derived relation kind.

```text
RefreshCurrentnessLine@Context:
  governedObjectRef:
  currentnessObjectKind:
  sourceRecordRef:
  editionOrLineagePins:
  affectedPathSliceOrScope:
  subjectPatternLocator:
  receivingUseAndApplicableConditions:
  currentnessConclusion:
  plannedRefreshAction?:
  refreshReportRef?:
```

`currentnessObjectKind` may name, for example, a selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, a cultural lineage, a term bridge, or a reused predicate definition. Use the line only when its recipient needs this structured currentness result; identify the temporal reference and relevant window within its conditions and pins. `plannedRefreshAction?` is absent when no refresh is selected, and `refreshReportRef?` is absent when no such report exists. The line states applicability for a use, not that the subject claim is true or adequately supported. Use `G.5` for selected-set declaration, `E.17` and `E.24.PUB` for publication, `C.18` for archive and front relations, `C.19` for pool treatment, `C.36` for cultural-evolution claims, `F.17` for exact local `SchemeSenseCell`s, `F.18` for name settlement, `F.9` for obtaining Bridges, and `A.6.RCD` for a derived relation kind.

Use the existing result or publication for a needed currentness conclusion or limitation. Use `RefreshPlan@Context`, `RefreshReport@Context`, `DeprecationNotice@Context` or `EditionBumpLog@Context` when the corresponding plan, performed work, deprecation or edition change actually occurs; do not add an empty ticket or notice for unchanged applicability.

When the governed object is a reusable `A.6.RCD` predicate definition or an admitted derived relation kind, the currentness line pins the exact base definitions, named substrate and edition, authorized derivation operation, and applicability scope. A change to any of them reopens the affected derivation and its dependent uses under `A.6.RCD`; G.11 schedules the bounded refresh but does not redefine the relation or derivation.

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)



Use `G.11` to plan scoped actions from typed causes; action semantics remain with their subject patterns.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness and decay events (`B.3.4`),
* evidence, bridge, policy, edition, relied-on base-definition, named-substrate-edition, or derivation-applicability edits (from the respective subject patterns' publication faces, forms, or units).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence and source relations, with `G.6` `PathId` and `PathSliceId` refs when a graph path slice is the current math-lens expression,
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions and policies).

The closure is a planning-time claim about affected slices, distinct from execution of the planned refresh actions. Interpret a B.3.4 trigger for the receiving claim and use: available information may establish continued applicability, a narrower use, an obtainable refresh need or a necessary suspension. An age-only signal does not determine that disposition. If support remains sufficient, stop with the usable result; retain only the limitation or reason a later recipient needs.

**4.3.3 Planning (P2W boundary).**
When the selected response requires planned refresh, use C.11 and C.19.2 for its marginal contribution, cost, delay and displaced work. Produce `RefreshPlan@Context` for the actions actually selected; possible action forms include:

* `RerunHarvest` (delegates to the selected harvest, source-currentness, or SoTA governing definition named by value, such as `G.1` or `G.2`, when that definition is current)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetResult` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates changes to the obtaining Bridge to `F.9`, calibration-record changes to `G.7`, and crossing visibility to `E.18` and the applicable visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
When selected actions are performed as Work or Work-bound audit, publish the corresponding `RefreshReport@Context`. A scoped applicability judgement can reuse available information without a new experiment; a plan alone establishes neither performance nor a new observation.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped result consumes C.28, refresh planning watches the causes that can change a supported use, unsupported use, support-result verdict, limits, or downstream decision basis:

| Sentinel | Affected result | Refresh pins |
| --- | --- | --- |
| sampling-realizability shift | `CounterfactualSamplingRealizabilityResult` | target distribution, decision Method and any derivation, physical, ethical, operational, and history constraints, required sampling construction or obstruction, unresolved questions, status, supported use, and unsupported use |
| performed sampling or resulting-data shift | dated sampling Work plus A.10 evidence path and empirical data regime | WorkPlan when used; actual performer identified through A.13; dated Work independently admitted through A.15.1; Method and window; resulting sample or data; provenance and currentness. Add F.6 with the same A.13 assignment only if the refresh decision needs to say exactly under which assignment the Work was performed. F.6 identifies neither performer nor assignment; a missing or failed attribution leaves the Work intact. A realizability result cannot substitute. |
| identification or bound shift | `CausalIdentificationResult` | data-regime refs, assumptions, identifying derivation, bound or failure witness, sensitivity |
| estimate shift | `CausalEstimateResult` | identification or design basis, data, estimator Method, diagnostics, uncertainty, sensitivity, and any live estimation-consistency result |
| target-trial practice shift | protocol and mapping results | question/estimand, protocol-to-data mapping, assumptions, estimate/precision, sensitivity and reporting source edition |
| causal-fairness shift | C.28 support result plus D.5 `BiasAuditReport@Context` | fairness estimand, extra counterfactual-identification assumptions, estimate and consistency result when used, support components and result, affected population, audit limits, and decision |
| causal-representation shift | `CausalVariableRepresentationRecord` | intervention validity, invariance, abstraction fidelity, query preservation, shift and use limits |
| off-policy or causal-RL shift | `OffPolicyCausalEvaluationResult` | behaviour/evaluation policies, horizon/history, confounding, overlap, endpoints, estimator and uncertainty |
| simulation-validation shift | `simulationResultRef` in `CausalSupportComponentRefs` | model assumptions, validation, sensitivity, supported model use and unsupported realized/interventional use |
| transport-endpoint shift | `CausalTransportabilityResult` | source/target population, domain, environment and data-generating regime, assumptions, windows, formula and unresolved limits |

These are payload distinctions under existing G.Core trigger kinds, not new trigger kinds. Reopen only the affected result and downstream uses that consumed it.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring live as `GPatternExtension` blocks. Scheduling, ordering, priority, and budget policy for the refresh queue are not separate extension semantics: `G.11` defines the required policy pins on `RefreshQueue` and `RefreshPlan@Context`, while A.15.2 and A.15.3 keep the WorkPlan and its local content separate from dated Work.

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

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (use-qualified currentness and interpreted planning debt)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* The receiving claim/use and the changed premise or applicable review condition, with source references where published.
* `FreshnessWindowDeclRef?`, `DecayPolicyIdRef?` or `EpistemicDebtBudgetRef?` only when the adopted window, deterioration model or planning measure is used. Their source supplies the meaning; no default expiry or debt budget is required.
* `PathSliceId[]` for the dependent claims and uses actually affected, not every use of an old carrier.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** B.3.4 determines what the trigger means for the use. Continue, narrow, refresh, suspend or an authorized exception remain available where warranted; no Refresh/Deprecate/Waive triad or automatic downgrade is introduced here. Currentness is not assurance of the underlying claim. Budget and priority logic apply only when their interpreted policies are used.

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

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the subject patterns)
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
* planned refresh remains the exact `U.WorkPlan` locally called `RefreshPlan@Context`; executed refresh is recorded in `RefreshReport@Context` or Work-bound audit.

If no priority or budget policy is declared, no scheduling heuristic is admissible by appearance; the plan must either use the ordinary queue order or state the missing policy pin as a blocker.

### G.11:5 - Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). The maintenance team uses `G.11` to produce a refresh plan scoped to the affected inspection slices and publishes a refresh report of the executed actions with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by subject pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL or plane penalties. The maintainers use `G.11` to ingest canonical trigger kinds, compute the minimal closure over affected `PathSliceId`s, schedule targeted parity reruns, then re-ship the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

**Paired currentness case.** A pack's export-date label changes, but its relied-on claims, source editions, qualification conditions and receiving use remain unchanged and adequately supported by available information. Retain the result; no refresh plan, waiver or no-refresh notice is needed. In the paired case, a dependency changes so that the shipped benchmark comparison no longer supports use beyond its stated window. Restrict that comparison and retain the warning with the shipped result so a later receiver cannot infer continued comparability. Plan the targeted check or update when it is justified and obtainable; currentness reporting alone does not repair the comparison.

### G.11:6 - Bias-Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions and policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: create queue, plan and report content only for the corresponding need; retain applicable support without an omission certificate, while preserving warnings a later receiver needs.
* **Onto and Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System and Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose and Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion plus explicit deltas; delegated to `G.Core`).                                                                                                                                       | `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD and OEE wiring).**     | When QD, OEE, or both are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin, edition, and policy wiring of the applicable extension blocks: `G.11:Ext.QDRefreshWiring`, `G.11:Ext.OEERefreshWiring`, or both. **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while keeping method-specific pin lists inside the applicable extension blocks.                  |
| **CC‑G11.3 (Telemetry-metric admissibility).**             | If a refresh publishes Illumination, QD, or OEE outcomes, it **SHALL** publish **Q, D, and QD‑score** and any coverage or regret as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy id SHALL be recorded** in SCR-visible evidence bindings through the cited subject patterns.                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge or plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL`, `CL^k`, `CL^plane`, and the relevant `Φ`, `Ψ`, and `Φ_plane` policy ids with loss notes so penalties are assigned to `R_eff` only (F and G invariant).                                                                                                                                | Keeps penalty assignment auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set or archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (`Pareto` or `Archive`) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross-context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef`, BridgeCard, UTS, and `CL` or `Φ_plane` policy ids. Missing or non-conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Use-qualified currentness).** | A freshness or decay trigger SHALL be interpreted under B.3.4 for the relied-on claim/use and affected dependencies. Continue on sufficient applicable support without mandatory refresh, deprecation, waiver, WorkPlan or omission certificate. A later receiver SHALL receive the minimum action-changing limitation or reason with the existing result/publication. Publish `DeprecationNotice@Context` only for actual deprecation; an exception requires actual authority and scope. | Preserves useful currentness warnings without treating age as lost assurance or manufacturing a completion artefact. |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`, dominance, Γ-fold, or guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` and the applicable subject patterns rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).** | Before changed refresh content is republished downstream, run or cite the required targeted RSCR or regression check for its affected scope. Keep the reference in the existing result/publication or corresponding `RefreshReport@Context`. Reuse a current matching result for unchanged content; no new execution report is required solely to repeat that reference. A missing required check retains the applicable `degrade` or `abstain` outcome under its governing policy. | Keeps actual republication checks while separating their evidence from unnecessary repeated work. |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed publication or output consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification and bounding, target-trial reporting, causal fairness, causal representation validation, off-policy and causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped causal-use results while preserving `G.Core` trigger governance. |
| **CC-G11.11 (Relation-derivation dependency refresh).** | When a reused `A.6.RCD` predicate definition or admitted derived relation kind depends on base definitions, a named substrate edition, an authorized derivation operation, or an applicability scope, the refresh plan **SHALL** pin those dependencies and reopen the affected derivation and dependent uses when one changes. The plan uses existing canonical trigger kinds; it does not mint a relation-specific trigger kind. | Prevents a once-valid derivation from surviving a changed semantic or substrate basis. |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context or plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins and E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Lost currentness warning** | A later recipient relies beyond the supported condition or window because the changed limitation was omitted. | The old result can no longer support that receiving use. | Keep the minimum useful warning or decision with the existing result; use a deprecation notice only for actual deprecation. An unchanged immediate use needs no skip-refresh record (CC‑G11.7). |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning and execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear governing-definition assignment boundaries.** Orchestration coordinates actions under their governing definitions; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids, editions, and policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop coordinates reruns and republishing; trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W planning-to-work boundary** so that the exact `U.WorkPlan` and its declaration-local planned-filling rows remain planning content while dated Work remains independently established.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

**0. QD currentness requires visible survey support.**
   Practice: current QD work is surveyed as approaches, applications, and challenges, with archive, diversity, descriptor, and evaluator-currentness concerns still live.
   Source: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 2026, DOI `10.1016/j.swevo.2025.102240`.
   Alignment: `RefreshCurrentnessLine@Context` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, descriptor or distance edition, and path-slice scope, while `C.18`, `C.19`, and `G.5` keep archive, pool, and selected-set meanings.
   Adoption: **Adopt and bound** (survey support changes refresh currentness fields and boundaries; it is not the governing ontology source).

**0a. Open-ended engineering outputs need source and evaluator currentness.**
   Practice: self-improving-agent, AlphaEvolve-style, and DeepEvolve-style lines use generated variants, external knowledge, evaluators, tests, archives, and empirical validation.
   Source: Darwin Godel Machine `arXiv:2505.22954`, AlphaEvolve `arXiv:2506.13131`, and DeepEvolve-style deep-research augmentation `arXiv:2510.06056`.
   Alignment: G.11 refresh records carry source, evaluator, descriptor, policy, edition, lineage, and report refs; generated method text, evaluator success, and archive update keep their subject patterns.
   Adoption: **Adopt and adapt** (refresh tracks currentness and smallest affected scope; it does not accept generated text as proof, gate passage, or performed work).

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring, retraining, and reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (`arXiv:1706.04599`, 2017); Amershi et al., *Software Engineering for Machine Learning* (ICSE-SEIP 2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition and policy pins for replay.
   Adoption: **Adopt and adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift and decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (`arXiv:1802.07569`, 2019); De Lange et al., *A Continual Learning Survey* (`arXiv:1909.08383`, 2021).
   Alignment: `B.3.4` supplies use-qualified currentness. `G.11` interprets changed conditions and justified review signals before planning an affected-scope refresh; elapsed time alone implies neither truth decay nor deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor and distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy and edition conditions.
   Source: contemporary QD families such as CMA-MAE (`arXiv:2205.10752`) and differentiable QD (`arXiv:2106.03894`).
   Alignment: QD-specific meaning lives with the subject patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set and archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (`arXiv:1901.01753`, 2019); later generator-family claims require a named `G.2` SoTA pack or exact current source.
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt and adapt** (adapted to Part G pin and UTS publication discipline).

5. **Efficient orchestration benefits from bandit and early-stopping scheduling, but scheduling must not redefine trigger, action, parity, shipping, or Part-G-wide default semantics.**
   Practice: modern hyperparameter and experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: ASHA (`arXiv:1810.05934`) and BOHB (`arXiv:1807.01774`) as representative post-2015 scheduling practice.
   Alignment: scheduling is expressed as `RefreshQueue` and `RefreshPlan@Context` policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and the exact `U.WorkPlan` stays separate from dated Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; Default Governing Definition Index), `G.6` (EvidenceGraph, `PathId` and `PathSliceId`), `G.7` (Bridge sentinels; CL, Φ, and plane pins), `G.5` (selector and set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness and decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), `A.6.RCD` for reopening reused predicate definitions and derived relation kinds when their base definitions, named substrate edition, authorized derivation operation, or applicability changes, `C.18` and `C.19` archive, front, and live-pool policy pins, `C.32.P2S` when telemetry, decay, or freshness reopens architecture problem-to-structure carry-through, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support results, verdicts, supported-use values, unsupported-use values, and SoTA-sensitive causal-use sentinel payloads), `F.15` (RSCR harness publications, when present).
**Publishes to:** UTS (refresh plan, refresh report, deprecations, edition bumps), and to the relevant subject patterns’ publication faces, forms, or units through delegated actions.

### G.11:End
