## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` when the current claim is a performed occurrence: dated work enacted by a holder under `U.RoleAssignment`, with its method, temporal extent, concrete bindings, used resources, affected referent, and containing system recoverable. Keep model use, actual change, entity-identity inception, evaluation, evidence, delivery, acceptance, and downstream effects under their own direct patterns.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the occurrence; surrounding records may identify, constrain, evidence, schedule, publish, or judge it, but they do not become the occurrence by being published.

**First useful result.** Identify one dated work occurrence and state only the facts needed by the current use: `performedBy -> U.RoleAssignment`, `enactsMethod -> U.Method`, temporal extent, `executedWithin`, concrete bindings, used resources, and affected referent. Add a method-description reference, model-use relation, actual-change claim, evaluation result, evidence relation, production claim, delivery, or acceptance relation only when that separately governed object is current.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover the `U.RoleAssignment`, enacted `U.Method`, temporal extent, accountable `U.System` or system in subsystem position, affected referent, concrete bindings, and used resources. Recover method-description, model-use, change, evaluation, evidence, production, delivery, or acceptance claims separately when current.
3. Decide whether the encountered record, trace, item, or display is performed `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or an `A.15.4` appearance-based reliance repair case.
4. For composite, repeated, interrupted, or overlapping occurrences, declare the work-part relation, naming threshold, and aggregation policy before using totals or identity claims. Do not name a work part when a temporal relation, evidence slice, telemetry segment, or missing-source-relation note is the actual object needed.
5. If the required occurrence references cannot be recovered, lower the claim to a missing-source-relation note, work-evidence note, plan note, publication-use note, declarative-representation note, or `A.15.4` repair request; do not backdate work.

**Ordinary use.** For a simple occurrence, one readable assertion naming performer assignment, enacted method, temporal extent, affected referent, and used resources is enough.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose performer assignment, enacted method, temporal extent, affected referent, bindings, and resource use remain inspectable while neighboring change, evaluation, evidence, production, delivery, and acceptance claims retain their own identities and governors.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only a `SlotFillingsPlanItem` (`A.15.3`), only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

### A.15.1:1 - Problem Frame

After we have separated **who is assigned** (via `U.RoleAssignment`), **what capability is being relied on** (via `U.Capability`), and **how in principle** the work is done (via `U.Method` or `U.MethodDescription`), we still need a precise concept for **what happened as performed work** in real time and space.

That concept is **`U.Work`**: the **dated performed occurrence** of enacting a `U.Method` by a specific performer under a `U.RoleAssignment`, with concrete bindings and resource use, **naming the domain referent affected by the occurrence** (asset, product, patient, learner, or dataset) - **not** merely the manipulation of records about that referent. Managers care about Work because cost, time, and responsibility attach to performed occurrences. Architects care because Work connects plans and method descriptions to accountable performance without absorbing the separately governed changes, measurements, verdicts, or downstream effects.

### A.15.1:2 - Problem (what breaks without a clean notion of Work)

1. **Plan and occurrence confusion.** Schedules and diagrams get mistaken for performed work, so audits and KPIs attach to plans or representations instead of dated occurrences.
2. **Method-description and work conflation.** A method description, code artifact, or SOP is reported as if it were performed work; conversely, logs are treated as recipes.
3. **Who and when leakage.** People and calendars are baked into method descriptions; reuse and staffing agility collapse.
4. **Resource dishonesty.** Energy, money, and tool wear are booked to methods or roles, not to performed work occurrences; costing and sustainability measures drift.
5. **Mereology muddle.** Teams hand-wave over work parts, retries, overlaps, or long-running episodes; roll-ups double-count or miss work.

### A.15.1:3 - Forces (what the definition must balance)

| Force                              | Tension we resolve                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail** | One Work notion for surgery, welding, ETL, proofs, lab cycles—while letting each keep its vocabulary. |
| **Granularity vs. aggregation**    | Atomic occurrences vs. composite operations; we need roll-up without double-count.                           |
| **Concurrency vs. order**          | Parallel or overlapped activities need clear part and overlap semantics.                              |
| **Identity vs. retries**           | A failed attempt, a retry, and a resumed episode—what is “the same” work?                             |
| **Time realism vs. simplicity**    | We need intervals and coverage but cannot bury users in temporal logic notation.                      |

### A.15.1:4 - Solution — define `U.Work` as the accountable, dated occurrence

#### A.15.1:4.1 - Definition

**`U.Work`** is a **4D occurrence holon**: a **dated performed enactment** of a `U.Method` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System`**, including a system in subsystem position when the larger-holon part relation is current, with concrete bindings and resource use. When a method-description reference is current, `methodDescriptionRef` names the `U.MethodDescription` used to identify, constrain, or justify the enacted method. A `BoundedModelUseStructure` or one of its direct model-use relations enters only when that model-use organization changes the receiving claim.
When the current claim needs a formal state-change witness, represent the selected change through a **morphism** `Δ` on a declared **state-plane** (`StatePlaneRef`), mapping the selected pre-state to the selected post-state under declared bindings for one or more **affected referents**. The work remains the dated occurrence; the morphism is a mathematical-lens expression for the separately governed change claim and does not establish a universal work-result relation.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core reference descriptors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start and end timestamps and, where relevant, location or asset.
2. **Method-description reference** — `methodDescriptionRef -> U.MethodDescription` when the description episteme is current; edition pinned when reliance depends on edition.
3. **Performer** — `performedBy -> U.RoleAssignment`; the referenced assignment has an admitted holder system, role value, role-taxonomy episteme, and effective reference scheme. Its temporal extent is described separately from those four relation participants.
4. **Parameters** — concrete values bound for this occurrence (from the **MethodDescription** parameter declarations).
5. **Direct participation and change claims** — recover each affected referent, used or consumed resource, parameter binding, supplied constituent, premise or reference use, operation argument or result binding, and actual change through its own direct relation or A.6.1 binding. Do not collect these as one input-output family.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Evaluation and downstream-effect claims** — success class, characteristic value, measurement result, comparison result, acceptance verdict, and downstream subject effect remain different objects under their direct patterns. None is an intrinsic field of `U.Work`.
8. **Links** — predecessor, successor, overlap, containment, temporal-part, episode-part, operational-part, concurrent-part, or another declared work relation to other `U.Work` occurrences when composite work is current.
9. **Semantic locality and model use when current** — recover the effective reference scheme, claim scope, exact `ModelUseRelation`, or `BoundedModelUseStructure` required by the receiving claim. Do not infer any of them from the method description or role assignment.
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre-state reference** and **post-state reference** (or a declared **Δ-predicate** evaluated on evidence) on the declared state-plane (**StatePlaneRef**).
11. **System** — `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2 (required for admitting the performed-work claim).
12. **Evidence and telemetry references (when current)** — if the occurrence feeds G.11 refresh or QD and OEE archives, cite the telemetry, evidence, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern; do not elevate telemetry into dominance without the governing comparison or archive policy.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe, code artifact, or diagram**     | **`U.MethodDescription`**         | Is it an episteme or publication describing a way of doing?     |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer, enactment, bindings, affected referent, and resource-use facts? |
| The **state change observed for this occurrence** | **`U.Work` delta claim**             | Did the referent change from pre to post on the declared state-plane? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A `U.Work` publication projects an already declared work occurrence; it does not create the occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, or publication face count as performed work.

Preparation work is `U.Work` only when preparation has actually occurred and has its own performer assignment, enacted method, temporal extent, affected referent, bindings, and resource-use facts. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, performer assignment, enacted method, concrete bindings, resource-use claims, and affected referent. Project a change, evaluation-result, evidence, production, delivery, or acceptance reference only as a separately governed neighboring claim. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the `U.Work` occurrence as the dated performed occurrence; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize surrogate `U.Work`; a publication may cite only work occurrences that meet the occurrence references in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the `U.Work` occurrence.

Launch values bind only at the occurrence. Planned proposals remain proposals; do not back-fill plan publications with performed-work bindings. Pre-state and post-state references bind to the occurrence: pre at start, post at completion or at declared checkpoints.

### A.15.1:5 - Work mereology (how occurrences form holarchies)

We adopt a **4D extensional** stance for occurrences: a Work is identified primarily by its **spatiotemporal extent** and its occurrence references (`methodDescriptionRef` when current, performer, parameterization). This avoids double-counting and keeps aggregation sound. FPF adapts insights from BORO and constructive ontologies to Work while staying practical.

#### A.15.1:5.1 - Parts and wholes of Work (occurrence facts)

* **Temporal-part (`TemporalPartOf_work`).** A proper **time-slice relation** over one selected `U.Work` occurrence or work phase. The selected part is grounded by parent work identity plus interval and, when needed, a named aspect such as resource use, telemetry, SLA coverage, or interval-local evidence. A temporal part is useful for monitoring, utilization, lead time, and interval-local evidence. It has no independent method-switch identity by that fact.
* **Episode-part (`EpisodeOf_work` or `WorkEpisode`).** A **policy-governed, event-bounded, maximally continuous enactment fragment** of one parent work occurrence. It starts at a work-entry, resumption, mode-switch, or switch-to-method event and ends at interruption, switch-away, completion, or a policy-declared pause. It is not an arbitrary time slice. It remains under the parent work identity only when the exact continuity-policy description selected for that work says that the interrupted or resumed activity is still the same `U.Work`.
`continuityPolicyDescriptionRef` designates the exact `U.MethodDescription` whose claims state the episode boundaries and work-continuity rule used for this occurrence. Interpret those claims under that episteme's effective `U.ReferenceScheme`; name any current `U.ClaimScope`, temporal qualification window, or model-use structure separately. These values govern the identity judgment without becoming a context container or another part of the work.

* **Operational-part (`OperationalPartOf_work`).** A **work-part occurrence** that may enact a factor of a recovered `U.Method`, for example, an incision occurrence within an appendectomy occurrence, possibly **overlapping** with others in time. If a method-description reference is current, it identifies, describes, constrains, or evidences that method factor; the referenced `U.MethodDescription` is not enacted. If no `U.Method` factor is recovered, govern the material as a work part, evidence segment, telemetry segment, mechanism material, system-component behavior, or missing-source-relation note under the direct pattern.
* **Parallel-part (`ConcurrentPartOf_work`).** Two work-part occurrences that **overlap** in their windows, coordinated by the same higher-level occurrence.

**Naming threshold.** Do not mint a durable public U-kind, durable named work object, or separate work occurrence for every interval, telemetry segment, pause, or episode-looking wording. Use a derivative part relation unless the downstream use needs a named work part with its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or the neighboring object that is actually current.

**Didactic rule:** **Method composition is not proof of Work decomposition, and Work decomposition is not proof of method composition.** A temporal work part may enact the same whole method during a slice. An episode may continue one method or mode, span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational part may correspond to a method factor only when that factor is recovered as `U.Method`.

**Quick choice test.**

- Ask **"which interval or aspect of the parent work do I need?"** If that is enough, use `TemporalPartOf_work`.
- Ask **"which continuous attempt under the episode policy do I need?"** If entry, resumption, mode-switch, interruption, switch-away, completion, or policy pause is the boundary, use `EpisodeOf_work`.
- Ask **"which performed sub-occurrence has its own performer assignment, temporal extent, enacted method, affected referent, bindings, resource use, or aggregation role?"** If that is current, use `OperationalPartOf_work` or another declared work-part relation. A neighboring evaluation or effect claim does not establish work parthood by itself.
- Ask **"which way-of-doing part is being composed?"** If the answer needs preconditions, effects, interface, and whole-method relation, recover a `U.Method` submethod under `A.3.1` and `B.1.5`; do not make the work part itself carry the method identity.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **Causal-use relation reference** — if one work occurrence is claimed to explain, trigger, or cause another, keep the work-occurrence link separate from the causal-use claim governed by `C.28` or another causal-use pattern named by value.
* **`retryOf`** — a new Work instance re‑attempting the same MethodDescription with revised parameters.
* **`resumptionOf`** — an episode or later occurrence that **continues** after interruption; policy decides whether it is under the same parent `U.Work` identity or a separate `U.Work` linked to the earlier occurrence.

These relations are **occurrence facts**, not method-design assumptions.

#### A.15.1:5.3 - Operators for roll‑ups (Γ\_time and Γ\_work)

* **Temporal coverage — `Γ_time(S)`**
  For a set `S` of Work parts, returns a **coverage interval set** (union of intervals) or, when required, the **convex hull** `[min t₀, max t₁]`. Use **union** for utilization; use **hull** for lead time.
  *Properties:* idempotent, commutative, monotone under set inclusion.

* **Resource aggregation — `Γ_work(S)`**
  For a set `S` of Work parts, returns the **aggregated resource ledger** (materials, energy, time, money) with de-duplication rules for shared and overlapped parts declared by the exact aggregation-policy description.
  *Properties:* additive on **disjoint** parts; requires **overlap policy** otherwise (e.g., attribute costs to the parent once, not to each child).

**Manager’s tip:** Pick the coverage operator that matches your KPI: **union** for machine utilization; **hull** for calendar elapsed; never mix silently.

#### A.15.1:5.4 - Identity of a Work (extensional criterion, pragmatically framed)

Two work records refer to the same `U.Work` only when they resolve to one occurrence under the declared work-identity tolerances and continuity-policy description. Check at least:

* the same time-space extent within the declared temporal and spatial tolerances;
* the same enacted `U.Method` and, when current, the same `U.MethodDescription` edition;
* the same performer `U.RoleAssignment`;
* the same affected referent and concrete parameter bindings, or explicit equivalence relations for changed bindings; and
* the same continuity-policy description interpreted under its effective `U.ReferenceScheme`.

A changed label, record, publication, or model-use structure does not decide work identity. A changed participant, extent, binding, or policy outcome identifies another occurrence unless the exact continuity rule admits the change.

#### A.15.1:5.5 - Interruptions, retries, resumptions (episode policy)

* **Retry:** **new Work** with its own window and parameters; link via `retryOf`.
* **Episode under the same parent work:** split one `U.Work` into event-bounded episodes only when `continuityPolicyDescriptionRef` admits the interruption, resumption, mode switch, or policy pause inside the same parent occurrence.
* **Separate occurrence after interruption or change:** identify another `U.Work` when that policy treats interruption, retune, rework, retry, changed parameter set, changed method-description edition, changed affected referent, switch-away, or restart as a new occurrence. Link the occurrences through `retryOf`, `resumptionOf`, `precedes`, `overlaps`, `contains`, or another declared relation that actually obtains.
* **Rework:** identify new work after failed earlier work unless the exact continuity-policy description admits it as an episode or operational part of the same parent occurrence. Keep any causal attribution with the governing causal-use pattern.

**Why it matters:** plans, costs, quality statistics, telemetry evidence, and method-reliance claims depend on whether the selected interval is a temporal part, event-bounded episode, operational part, or new occurrence. Name the exact policy episteme, effective reference scheme, and any current scope or temporal qualification before relying on that distinction.

#### A.15.1:5.6 - Compositionality of effects (Δ)

For any work occurrence with parts, the **effect of the whole** is the rules-declared composition of the effects of its parts plus any declared overheads and residuals. Composition aligns with the overlap rules used by `Gamma_work`, such as no double-count of shared fixed costs and consistent attribution of variable deltas.

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer:** `U.RoleAssignment` with holder system `OR_Team_A`, role value `SurgicalTeamRole`, role-taxonomy episteme `HospitalRoles-2025`, and effective reference scheme `Hospital-Operating-Scheme-2025`; the assignment occurrence covers the surgery interval.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02-10:07 -> **resumptionOf** same occurrence (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Gamma_work:** totals consumables and staff time once (no double-count for overlapping work-part occurrences).

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **`methodDescriptionRef`:** `ETL_v12.bpmn`.
* **Performer:** `U.RoleAssignment` with holder system `ETL_Runtime`, role value `TransformerRole`, role-taxonomy episteme `DataOpsRoles-2025`, and effective reference scheme `DataOps-Execution-Scheme-2025`; the assignment occurrence covers the ETL interval.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage input and output once at the parent.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer:** `U.RoleAssignment` with holder system `LabRig_7`, role value `TransformerRole`, role-taxonomy episteme `ThermoLabRoles-v2`, and effective reference scheme `ThermoLab-Experiment-Scheme`; the assignment occurrence covers the laboratory-work interval.
* **Work identity:** the occurrence is identified by the occurrence interval plus occurrence references; the thermodynamic state-plane trace is a dynamics or geometry relation used to describe the change, not a work-control relation or ordered instruction sequence.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer:** `U.RoleAssignment` with holder system `ClaimsTeam_A`, role value `ClaimsHandlerRole`, role-taxonomy episteme `InsuranceOpsRoles-2026`, and effective reference scheme `Claims-Handling-Scheme-2026`; the assignment occurrence covers the claims-work interval.
* **Episode policy:** a customer callback interruption under one hour keeps the same parent work identity and creates two `EpisodeOf_work` fragments: `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38`.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer:** `U.RoleAssignment` with holder system `Engine_Cell7`, role value `EngineOperationRole`, role-taxonomy episteme `EngineCellRoles-2026`, and effective reference scheme `TestBench-Operating-Scheme-2026`; the assignment occurrence covers the engine-run interval.
* **Episodes:** start, stop, mode-change, fuel/ignition policy, or diagnosis policy may bound `EpisodeOf_work` fragments. The definition uses boundary events and policy, not a human-attention metaphor.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer:** `U.RoleAssignment` with holder system `Receiver_Rx42`, role value `DetectorReceiverRole`, role-taxonomy episteme `RadioLabRoles-2026`, and effective reference scheme `RadioLab-Reception-Scheme-2026`; the assignment occurrence covers the reception interval.
* **Episodes:** a continuous reception interval between retune, on/off, interruption, or declared diagnostic mode events is `EpisodeOf_work` only under the receiver's episode policy.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

### A.15.1:6.7 - Bias-Annotation

| Bias | How A.15.1 prevents it |
| --- | --- |
| Plan-as-work bias | `U.WorkPlan`, schedules, method descriptions, and intended parameter bindings stay separate from the dated occurrence. |
| Log-as-work bias | Telemetry, dashboards, provenance rows, and work publications can evidence or describe a work occurrence; they do not become the occurrence. |
| Method-as-occurrence bias | `U.Method` and `U.MethodDescription` identify or constrain the way of doing; `U.Work` records the dated performed enactment. |
| Evidence-as-authority bias | Evidence, assurance, gate, release, and causal-use claims keep their governing patterns and do not follow from a work record by appearance. |
| Record-only transformation bias | Record manipulation qualifies as `U.Work` only when an exact affected-referent or direct operation-participation relation makes the record or dataset the entity transformed or otherwise affected; a context label establishes neither relation. |

### A.15.1:7 - Scope Declaration and Rationale

* **Applicability:** Use the same occurrence test for pragmatic costing, architectural accountability, teaching examples, and source or evidence questions; when the current claim is only about a description, publication, source, or evidence relation, apply the governing pattern for that claim.
* **Scope declaration:** The occurrence head is universal. Temporal semantics use the declared temporal reference; episode identity uses `continuityPolicyDescriptionRef` and its effective `U.ReferenceScheme`; claim scope, qualification windows, model-use structure, evidence, and source currentness remain separate when current.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment`, direct `Work.performedBy = RoleAssignment` wording, and derived `RoleEnactmentFact` when a named fact is needed, so that costing, quality, and audit rest on **work occurrences**, not on plans or recipes.

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is a dated performed occurrence. It is not a `U.Method` (semantic way), not a `U.MethodDescription` (description), not a `U.Role` or `U.RoleAssignment` (assignment), and not a `U.WorkPlan` (plan or schedule).

**CC-A15.1-2 (Required links).**
A conforming `U.Work` claim names:
(a) `enactsMethod -> U.Method` (the method enacted),
(b) `methodDescriptionRef -> U.MethodDescription` when a source-material episteme is the current method description or an editioned method description is current,
(c) `performedBy -> U.RoleAssignment` (the exact assignment whose interval covers the occurrence), and
(d) `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2.

**CC-A15.1-3 (Time window).**
A conforming `U.Work` claim carries a closed interval `[t_start, t_end]`, or an explicitly marked open end for in-flight work, and, where relevant, location or asset.

**CC-A15.1-4 (Interpretation and policy basis).**
A load-bearing work claim names the exact method-description edition when current, its effective `U.ReferenceScheme`, `continuityPolicyDescriptionRef`, and any claim scope, qualification window, aggregation-policy description, acceptance predicate, or selected model-use structure on which the judgment actually depends. Plain *work-judgment basis* is shorthand for these separately governed values, not a new context object or record.

If two local senses must be related, F.9 receives the exact sense endpoints and the claimed direction and loss. A different reference scheme, role assignment, or model-use structure alone does not establish a Bridge.
**CC-A15.1-4b (State-plane reference).**
The work claim names the `StatePlaneRef` used for its delta judgement.

**CC-A15.1-5 (RoleAssignment interval coverage).**
The `performedBy` `U.RoleAssignment` interval covers the work interval. If it does not, keep the work occurrence and the assignment claim separate: repair or reject the attribution, or establish a retroactive assignment only under the exact A.2.1 rule that admits it.

**CC-A15.1-6 (Parameter binding).**
Parameters declared by the `U.MethodDescription` have concrete values bound at work creation or start and recorded with the work occurrence. Defaults in the method description do not by themselves admit the performed-work claim.

**CC-A15.1-7 (Capability check).**
Capability thresholds stated by the `U.Method` or `U.MethodDescription` are checked against the holder in `performedBy` for the performed-work interval or declared checkpoints. A violation is stated by the separately governed evaluation-result episteme or direct characteristic/evaluation relation; it is not recorded as an intrinsic work outcome.

**CC-A15.1-8 (Acceptance criteria).**
An acceptance claim names the exact criterion or comparator specification, its edition, applicable scope and window, the evaluation or acceptance work that applied it, and the direct result relation. Success class, quality measurement, comparison result, and acceptance verdict remain distinct; no verdict is an intrinsic field of `U.Work`.
**CC-A15.1-9 (Resource honesty).**
Performed consumptions and costs (energy, materials, machine-time, money, tool wear) are booked to `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans; performed values belong in work occurrences.

**CC-A15.1-10 (Mereology declared).**
When a work occurrence has parts, the selected part relation is declared: temporal-part, episode-part, operational-part, or concurrent-part. Ambiguous mixtures lower aggregation and identity claims. A `TemporalPartOf_work` claim names parent work identity plus interval or aspect; an `EpisodeOf_work` claim names the event-bounded continuity policy; an `OperationalPartOf_work` claim names the occurrence-side part and any recovered method factor separately.

**CC-A15.1-11 (Temporal coverage selection).**
For a roll-up, the exact aggregation-policy description declares whether temporal coverage uses union for utilization or convex hull for lead time. Silent mixing lowers the KPI or comparison claim.

**CC-A15.1-12 (Resource aggregation).**
Aggregation of resource ledgers across work parts names an overlap policy, such as attributing shared machine-time to the parent only, before totals are used.

**CC-A15.1-13 (Identity and retries).**
A retry is a new `U.Work` occurrence linked via `retryOf`. An interruption remains inside the same occurrence only when the exact `continuityPolicyDescriptionRef` admits an `EpisodeOf_work`; otherwise the later enactment is another occurrence. Changed method-description edition, affected referent, parameter binding, or temporal extent is tested by that policy rather than by a context label.

**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-locality evaluation).**
A work occurrence keeps one identity when several receiving uses evaluate it. Each use names its own effective reference scheme, claim scope, criterion, qualification window, evaluation work, and result episteme. Use F.9 only when an exact Bridge between local senses is actually needed; a shared work name or record carries no acceptance across uses.
**CC-A15.1-16 (Method-description reference changes during work).**
If the method-description edition changes mid-occurrence, split the work into episodes bound to the respective editions, or record an exact override occurrence and its direct relation to the work and selected description edition. Silent substitution lowers the work claim.

**CC-A15.1-17 (Distributed performers).**
If multiple `U.RoleAssignment` values jointly perform the same top-level work occurrence, either designate a lead `U.RoleAssignment` with concurrent parts, or model the top-level occurrence as a parent work with child work occurrences per `U.RoleAssignment`.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry support a claim about work only through an exact evidence-use relation that identifies the work occurrence, method-description edition when current, performer assignment, temporal extent, affected referent, and the policy or qualification values on which the receiving claim relies.

**CC-A15.1-19 (Affected referent).**
Each `U.Work` claim names at least one affected referent, such as asset, product, batch, dataset, or document, through `affected -> {...}`.

**CC-A15.1-20 (State-change witness).**
Each `U.Work` claim carries either explicit pre-state and post-state references on the declared state-plane or a delta predicate evaluable on evidence. A no-op occurrence is flagged as such.

**CC-A15.1-21 (Affected-referent declaration vs. record handling).**
A work occurrence whose only effect is copying or reformatting records qualifies as `U.Work` only when an exact affected-referent or operation-participation relation identifies those records as the product referent. A label or surrounding record does not establish that relation.

**CC-A15.1-22 (Executed-within declaration).**
Each `U.Work` claim names `executedWithin -> U.System`; when the accountable system is a subsystem in ordinary speech, name the system and its part relation to the larger holon. When that system differs from the asset of change, keep `affected` explicit.

**CC-A15.1-23 (Compositionality of delta).**
For composite work, the parent effect is the declared composition of child effects under the same overlap policy as `Gamma_work`.

**CC-A15.1-24 (No new claims on publication views).**
MVPK views for `U.Work` project the declared work-occurrence claim; they do not add properties or claims. Numeric or comparable content names unit, scale, reference-plane, and `EditionId` pins; work-publication views do not use "signature" for these publication pins.

**CC-A15.1-25 (No Gamma leakage).**
Publication views reference Gamma operators and policies by id when showing aggregates. They do not encode aggregation semantics in prose or imply defaults. Gamma lives in Part B; views carry pinned references only.

**CC-A15.1-26 (No input-output re-listing).**
Publication views do not restate method-description input and output lists; they publish presence pins and source references only under the publication-use pattern governing that view.

**CC-A15.1-27 (Comparator ordering and return sets).**
Across-occurrence comparison presented on a `U.Work` publication view uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a `U.Work` publication view pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. Bridge ids carry cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

**CC-A15.1-30 (Part naming parsimony).**
Do not create a durable named work part for every interval, telemetry segment, pause, event-log row, engine stroke label, detector component, or encountered wording. Name a work part only when downstream use needs its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or another direct neighboring object.

**CC-A15.1-31 (Method and work granularity are coupled but not isomorphic).**
A work part may enact a recovered submethod, but the correspondence is not automatic. A temporal work part usually enacts the same whole method during a slice. An episode records continuity under one method or mode and may span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational work part corresponds to a method factor only when that factor is recovered as `U.Method` under `A.3.1` and `B.1.5`; otherwise govern the material as a work part, method-description node, evidence segment, mechanism material, or system-component behavior under the direct pattern.

### A.15.1:9 - Temporal & Aggregation Semantics (normative operators & invariants)

#### A.15.1:9.1 - Temporal coverage `Γ_time`

* **Input:** a finite set `S` of Work instances or Work parts.
* **Output:** either (a) the **union** of their intervals, or (b) the **convex hull** `[min t_start, max t_end]`, as declared by the exact aggregation-policy description and KPI definition.
* **Invariants:**

  * **Idempotent:** `Γ_time(S ∪ S) = Γ_time(S)`
  * **Commutative:** order of elements irrelevant
  * **Monotone:** if `S ⊆ T` then coverage(S) ⊆ coverage(T) (for union) or hull(S) ⊆ hull(T) (for hull)
* **Usage guidance:**

  * Use **union** for **utilization and availability** (how much clock time the asset was busy).
  * Use **hull** for **lead time and cycle time** (elapsed from first touch to last release).
  * **Manager’s tip:** Write the choice near the KPI; many disputes are just a hidden union‑vs‑hull mismatch.

#### A.15.1:9.2 - Resource aggregation `Γ_work`

* **Input:** a finite set `S` of Work instances or parts with resource ledgers.
* **Output:** an **aggregated ledger** (materials, energy, machine‑time, money, tool wear) with explicit **overlap policy**.
* **Invariants:**

  * **Additivity on disjoint parts:** if intervals and resources are disjoint by policy, totals add.
  * **No double‑count:** overlapping costs follow the declared policy (e.g., count once at parent).
  * **Traceability:** each aggregated figure is reconcilable to contributing Work IDs.
* **Typical policies:**

  * **Parent‑attribution:** shared fixed costs at parent; variable costs at children.
  * **Pro‑rata by wall‑time:** split overlaps by relative durations.
  * **Driver‑based:** allocate by a declared driver (e.g., CPU share, weight, priority).

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on a work occurrence, perform three quick checks:

1. **Method-description interpretation.** Does `methodDescriptionRef`, when current, resolve to the exact `U.MethodDescription` edition under the effective `U.ReferenceScheme` used by the receiving claim? If not, repair the reference or relate the exact local senses through F.9 when a real cross-locality claim is current.
2. **Role-assignment coverage.** Does `performedBy` resolve to one `U.RoleAssignment` whose interval covers the occurrence? If not, keep the work and attribution claim separate until A.2.1 admits the assignment.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the current criterion edition to the exact work facts, changed subject, measurement results, or delivered entity required by that criterion? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separately governed.

These checks recover exact governing objects. They neither create one judgment-context object nor make acceptance part of work identity.

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed occurrence."** Dumping telemetry without occurrence references (`methodDescriptionRef` and edition when current, performer assignment, time window, affected referent, and exact evidence-use relation) -> **Not Work**. Recover the work occurrence and relate the log as evidence.
* **Record-only transforms.** ETL or replication with no exact affected-referent or operation-participation relation does not establish what the work changed. Recover that direct relation or keep the material as a plan, method-description, trace, or representation claim.
* **Silent cross-locality acceptance.** "Ops accepted it, so audit accepts it." -> Name each receiving criterion, evaluation work, result episteme, and acceptance relation; add F.9 only when exact local senses must be bridged.
* **Method-description edition drift in mid-occurrence.** Swapping SOP v5->v6 without recording -> split into episodes or record method-description override.
* **Budget on the method.** Charging costs to Method or Role -> Book **only** to Work; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Slice-as-episode.** A monitoring interval, telemetry window, crank-angle segment, or one-second reception trace is called an episode only because it has timestamps -> Use `TemporalPartOf_work`, an evidence relation, or a telemetry relation unless a declared episode policy supplies event-bounded continuity.
* **Episode-as-new-work by habit.** A pause, retune, or interruption is always recorded as a new occurrence -> Apply the exact `continuityPolicyDescriptionRef`. Keep the same parent work with `EpisodeOf_work` only when that policy preserves identity; otherwise identify a separate `U.Work`.
* **Method-factor-as-work-part by label.** A step, stroke, receiver component, graph node, or method-description section is treated as a work part or submethod by name -> Recover the current object: `U.Method` factor, `U.MethodDescription` constituent, `TemporalPartOf_work`, `OperationalPartOf_work`, evidence segment, mechanism material, system-component behavior, or missing-source-relation note.
* **Granularity inflation.** Every interval or trace row receives a durable work-part name -> Name the work part only when a current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on it.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.

### A.15.1:12 - Existing work-log repair applications

1. **Backfill links.** For existing logs, create work-occurrence records and attach `enactsMethod`, `methodDescriptionRef` when current, and `performedBy`.
2. **Recover the work-judgment basis.** Name the exact method-description edition, effective reference scheme, continuity-policy description, and any current scope, qualification window, aggregation policy, criterion, or evidence-use relation.
3. **Record the episode policy.** Decide when an interruption keeps identity or forces a new occurrence.
4. **Separate slice, episode, and operational part.** Use interval/aspect for `TemporalPartOf_work`, event-bounded continuity for `EpisodeOf_work`, and recovered occurrence-side part plus any separately recovered method factor for `OperationalPartOf_work`.
5. **Name only useful work parts.** If no current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on the candidate part, keep it as a relation, evidence slice, or telemetry slice.
6. **Choose Γ\_time per KPI.** Put "union" or "hull" in the KPI definition so disputes expose the coverage policy instead of hiding it.
7. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
8. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record performed values.
9. **Parameter blocks.** Make parameters explicit and bind them at start; root-cause analyses become easier.

### A.15.1:13 - Consequences

| Benefits                                                                                                                 | Trade-offs and mitigations                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Costs, time, and quality attach to concrete work occurrences; root-cause analysis and accountability improve. | **More records.** You create Work instances; mitigate with templates and automation.       |
| **Sound roll-ups.** Γ\_time and Γ\_work turn roll-ups from hand-waving into declared policy; KPIs become comparable.     | **Policy discipline.** Choose union or hull and an overlap policy before using the roll-up; write that policy once. |
| **Cross-locality clarity.** Exact method-description, scheme, scope, criterion, evaluation, and acceptance relations prevent silent meaning drift. | **Bridge upkeep.** Maintain F.9 Bridges only for exact local-sense crossings that a receiving use actually needs. |
| **4D extensional coherence.** Parts, overlaps, and retries stop double-counting and identity confusion.                  | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |

### A.15.1:13.0 - Rationale

`U.Work` is kept as a dated occurrence because method, method description, work plan, affected entity, actual change, evaluation-result episteme, delivered entity, and downstream effect are different FPF objects. The same wording in a source episteme, publication occurrence, method description, or work plan can point to several of them, but performed-work claims need occurrence grounding, temporal bounds, role assignment, enacted method, and affected referent rather than a convenient method or plan label. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local `U.Work` distinction: dated occurrence, role-assigned performer, enacted method, temporal extent, affected referent, concrete bindings, and resource use, with neighboring change, evaluation, evidence, production, delivery, and acceptance claims kept separate. Historical occurrence modeling is used as lineage only when a current practice still needs that distinction.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` is an occurrence with temporal extent and occurrence references; parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, or log entry as proof of a performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they are bound to involved objects, performer or role assignment, enacted method, temporal extent, affected referent, and exact interpretation or policy references needed by the receiving claim. | Treating telemetry or event rows alone as `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry can support, replay, measure, or diagnose a claim about work, but the occurrence still needs performer assignment, enacted method, temporal extent, affected referent, bindings, and resource-use facts. | Counting trace, metric, or log existence as the performed work, a result, or dominance evidence without the governing evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Work records state evidence-provenance relation references and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | Roll-ups require declared `Gamma_time`, `Gamma_work`, and overlap policy; partial order and overlap are not hidden in step labels. | Mixing union, hull, parent cost, child cost, and ordinal comparison without a declared policy. |

### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`; C.2.1 for episteme edition and effective `U.ReferenceScheme`; A.2.6 for claim scope; and C.27.TA for temporal qualification. A.1.1 enters only when a separately identified `BoundedModelUseStructure` changes the receiving work claim.
* **Coordinates with:** A.15 Role-Method-Work Alignment (the "four-slot grammar"); B.1 Gamma (aggregation) for resource and time operators; `E.10` and `E.10.ARCH` for wording cues such as process, workflow, activity, schedule, algorithm, solver, and procedure; `A.10`, `B.3`, `E.17`, and `A.15.4` when evidence, assurance, publication-use, or appearance-based reliance repair claims are being made; `A.15.5` when readiness or full-kit preparation is current before performed work; `C.32.P2S` when performed work realizes or inspects selected structures in an architecturing flow; and `A.2.8.PER` only when this dated work exercises a strong grant through a separately asserted `PermissionExerciseRelation@Context`. Work identity, performance, and result remain independent of the grant and exercise claim.
* **Informs:** reporting and KPI patterns; assurance and evidence patterns (Work as the reference occurrence for audits); scheduling patterns (`U.WorkPlan` -> `U.Work` deltas).

### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Four-slot grammar:** Who? **RoleAssignment**. Can? **Capability**. How? **Method or MethodDescription**. Did? **Work**.
* **Interpretation checks:** exact method-description edition and scheme; covering `U.RoleAssignment`; separately governed criterion, evaluation work, result episteme, and acceptance relation.
* **Roll‑ups:** `Γ_time = union` (utilization) or `hull` (lead time); `Γ_work` with a declared overlap policy.
* **Episodes vs retries:** same occurrence split vs new occurrence; write the policy.
* **Resource honesty:** performed values booked **only** to Work; estimates belong in method descriptions or plans.

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, identify the dated `U.Work`: performer assignment, enacted method, concrete bindings, used resources, temporal extent, affected referent, and containing system. Carry actual change, production, evaluation-result, evidence, delivery, acceptance, transfer, or receiving-use claims as separately governed continuation objects.

A `U.Work` occurrence may be designated by an episteme that also cites a `U.WorkPlan`, exact planned-filling claim, or prior `WorkEntryReadiness@Context` as a baseline. That episteme may state launch values, performed values, substitutions, variance, and telemetry, but each plan, comparison, transfer, evidence, assurance, gate, readiness, production, evaluation, delivery, or acceptance claim retains its direct governor.

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.Work` claim when performer assignment, enacted method, temporal extent, `executedWithin`, affected referent, concrete bindings, or resource-use facts cannot be named at the granularity required by the next performed-work use. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated work occurrence or a gratuitous work part.

Repair the work assertion or description when a subsequent source changes the temporal extent, performer assignment, enacted method, method-description reference, concrete binding, resource-use claim, affected referent, containing system, overlap policy, or aggregation policy. Repair a neighboring change, evaluation, evidence, production, delivery, or acceptance claim under its own pattern; do not rewrite the work occurrence when only that episteme or relation changes, and do not convert a plan or `A.15.4` repair request into work.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a `U.Work` reference only when the receiving claim actually depends on the occurrence.

### A.15.1:End

