## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` when the current claim is a performed occurrence: a dated, resource-consuming occurrence enacted by a holder under `U.RoleAssignment`, inside a `U.BoundedContext`, with method, time window, parameter bindings, resources, affected referent, result, and evidence relations kept inspectable.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the occurrence; surrounding records may identify, constrain, evidence, schedule, publish, or judge it, but they do not become the occurrence by being published.

**First output.** One work-occurrence record naming `performedBy -> U.RoleAssignment`, `enactsMethod -> U.Method`, `methodDescriptionRef` when the source episteme is current, `executedWithin`, time window, concrete parameter bindings, affected referent, resource ledger, pre-state and post-state references or a declared delta predicate, outcome, and the governing `U.BoundedContext`.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover the `U.RoleAssignment`, enacted `U.Method`, method-description source, time window, accountable `U.System` or system in subsystem position, affected referent, parameters, resources, outcome, and evidence relation when current.
3. Decide whether the encountered record, trace, or source candidate or display is performed `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or a work-relevant source-restoration case (`A.15.4`).
4. For composite, repeated, interrupted, or overlapping occurrences, declare the work-part relation and aggregation policy before using totals or identity claims.
5. If the required occurrence references cannot be recovered, lower the claim to a source-gap note, work-evidence note, plan note, publication-use note, declarative-representation note, or source-restoration request; do not backdate work.

**Ordinary use.** For a simple occurrence, one compact work card with performer, method, time window, affected referent, resources, and outcome is enough.

**Reliance-bearing use.** Use the full record when cost, quality, audit, evidence, conformance, gate, release, result measurement, cross-context reuse, or aggregation claims depend on the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence record that keeps performer, role assignment, enacted method, method-description source, time window, affected referent, resources, outcome, evidence relation, and repair boundary inspectable.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only a `SlotFillingsPlanItem` (`A.15.3`), only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible source cue that needs source restoration before reliance (`A.15.4`), only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

### A.15.1:1 - Problem Frame

After we have separated **who is assigned** (via `U.RoleAssignment`), **what capability is being relied on** (via `U.Capability`), and **how in principle** the work is done (via `U.Method` or `U.MethodDescription`), we still need a precise concept for **what happened as performed work** in real time and space.

That concept is **`U.Work`**: the **dated run-time occurrence** of enacting a `U.Method` by a specific performer under a `U.RoleAssignment`, with concrete parameter bindings, resource consumption, and outcomes, **naming the domain referent changed by the occurrence** (asset, product, or dataset) - **not** merely the manipulation of records about that referent. Managers care about Work because cost, time, defects, and result evidence are booked on performed occurrences. Architects care because Work ties plans and method descriptions to accountable performed work.

### A.15.1:2 - Problem (what breaks without a clean notion of Work)

1. **Plan and run confusion.** Schedules and diagrams get mistaken for performed work, so audits and KPIs attach to plans or representations instead of dated occurrences.
2. **Method-description and work conflation.** A method description, code artifact, or SOP is reported as if it were performed work; conversely, logs are treated as recipes.
3. **Who and when leakage.** People and calendars are baked into method descriptions; reuse and staffing agility collapse.
4. **Resource dishonesty.** Energy, money, and tool wear are booked to methods or roles, not to performed work occurrences; costing and sustainability measures drift.
5. **Mereology muddle.** Teams hand-wave over sub-runs, retries, overlaps, or long-running episodes; roll-ups double-count or miss work.

### A.15.1:3 - Forces (what the definition must balance)

| Force                              | Tension we resolve                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail** | One Work notion for surgery, welding, ETL, proofs, lab cycles—while letting each keep its vocabulary. |
| **Granularity vs. aggregation**    | Atomic runs vs. composite operations; we need roll‑up without double‑count.                           |
| **Concurrency vs. order**          | Parallel or overlapped activities need clear part and overlap semantics.                              |
| **Identity vs. retries**           | A failed attempt, a retry, and a resumed episode—what is “the same” work?                             |
| **Time realism vs. simplicity**    | We need intervals and coverage but cannot bury users in temporal logic notation.                      |

### A.15.1:4 - Solution — define `U.Work` as the accountable, dated occurrence

#### A.15.1:4.1 - Definition

**`U.Work`** is a **4D occurrence holon**: a **dated run-time enactment** of a `U.Method` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System`**, including a system in subsystem position when the larger-holon part relation is current, inside a `U.BoundedContext`, that binds concrete parameters, consumes and produces resources, and leaves an auditable trace. When a method-description source is current, `methodDescriptionRef` names the `U.MethodDescription` used to identify, constrain, or justify the enacted method.
When the current claim needs a formal state-change witness, represent the occurrence through a **morphism** `Δ` on a declared **state-plane** (`StatePlaneRef`), mapping pre-state plus inputs to post-state plus outputs for one or more **affected referents**. The work itself remains the dated occurrence; the morphism is the selected mathematical-lens expression for its delta claim.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core reference descriptors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start and end timestamps and, where relevant, location or asset.
2. **Method-description source** — `methodDescriptionRef -> U.MethodDescription` when the description source is current; edition pinned when reliance depends on edition.
3. **Performer** — `performedBy → U.RoleAssignment` (whose holder slot, role value, and bounded-context slot admit the performer).
4. **Parameters** — concrete values bound for this run (from the **MethodDescription** parameter declarations).
5. **Inputs and outputs** — materials, information, or product states used or produced by the Work; service delivery is judged through the Outcome row.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Outcome** — success and failure classes, quality measures, acceptance verdicts (**map-then-compare** per **ComparatorSet** under **CG-Spec**; pin editions).
8. **Links** — predecessor, successor, and overlap relations to other Work, plus step or run nesting if part of a bigger operation.
9. **Context** — the bounded context under which this run is judged, normally inherited from the method-description source and `U.RoleAssignment`; see A.15 for cross-checks.
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre-state reference** and **post-state reference** (or a declared **Δ-predicate** evaluated on evidence) on the declared state-plane (**StatePlaneRef**).
11. **System** — `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2 (required for admitting the performed-work claim).
12. **Evidence and telemetry references (when current)** — if the run feeds G.11 refresh or QD and OEE archives, cite the telemetry, evidence, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern; do not elevate telemetry into dominance without the governing comparison or archive policy.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe, code artifact, or diagram**     | **MethodDescription**         | Is it an episteme or publication describing a way of doing?     |
| The **semantic "way of doing"**               | **Method**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** (“can do within bounds”)      | **Capability**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs, resources | **Work**               | Did it happen at (t₀, t₁), consume resources, produce outcomes? |
| The **state change observed for this occurrence** | **Work.Δ**             | Did the referent change from pre→post on the declared state-plane? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A `U.Work` publication projects an already declared work occurrence; it does not create the occurrence, add run-time facts, or make a plan, source reconstruction, dashboard, or publication face count as performed work.

Preparation work is `U.Work` only when preparation has actually occurred and has its own performer, method, time window, affected referent, resources, and outcome. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only occurrence references: time window, performer, enacted method-description source, parameter-binding occurrence, resource-ledger reference, state-change references, outcome, and acceptance-verdict reference when current. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites design-time material or cross-context material | Keep the `U.Work` occurrence run-time; cite the design-time or cross-context material through Bridge relation, UTS relation, `DesignRunTag`, reference-plane, or edition relation as needed. |
| reconstructed records look like a run | Do not synthesize surrogate `U.Work`; a publication may cite only work occurrences that meet the occurrence references in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses design-time state, run-time state, context, reference plane, unit, or edition, publish the crossing relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the `U.Work` occurrence.

Launch values bind only at the occurrence. Plan-time proposals remain proposals; do not back-fill plan publications with run-time bindings. Pre-state and post-state references bind to the occurrence: pre at start, post at completion or at declared checkpoints.

### A.15.1:5 - Work mereology (how runs form holarchies)

We adopt a **4D extensional** stance for occurrences: a Work is identified primarily by its **spatiotemporal extent** and its occurrence references (method-description source when current, performer, parameterization). This avoids double-counting and keeps aggregation sound. FPF adapts insights from BORO and constructive ontologies to Work while staying practical.

#### A.15.1:5.1 - Parts and wholes of Work (design‑neutral, run‑time facts)

* **Temporal‑part (`TemporalPartOf_work`).** A proper **time‑slice** of a Work (e.g., the first 10 minutes of a 2‑hour run). Useful for monitoring and SLAs.
* **Episode‑part (`EpisodeOf_work`).** A **resumption fragment** after an interruption (same run identity if policy deems it one episode; see 5.5).
* **Operational-part (OperationalPartOf_work).** A **sub-run** that enacts a **factor** of the Method or method-description source, for example, an incision run within an appendectomy run, possibly **overlapping** with others in time.
* **Parallel‑part (`ConcurrentPartOf_work`).** Two sub‑runs that **overlap** in their windows, coordinated by the same higher‑level run.

**Didactic rule:** **Method composition ≠ proof of Work decomposition.** Sub‑runs often map to method factors, but retries, batching, pipelining, and failures make the mapping non‑isomorphic.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **Causal-use relation reference** — if one work occurrence is claimed to explain, trigger, or cause another, keep the work-occurrence link separate from the causal-use claim governed by `C.28` or another causal-use pattern named by value.
* **`retryOf`** — a new Work instance re‑attempting the same MethodDescription with revised parameters.
* **`resumptionOf`** — a Work episode that **continues** an interrupted run (policy decides identity; see 5.5).

These relations are **run‑time facts**, not design assumptions.

#### A.15.1:5.3 - Operators for roll‑ups (Γ\_time and Γ\_work)

* **Temporal coverage — `Γ_time(S)`**
  For a set `S` of Work parts, returns a **coverage interval set** (union of intervals) or, when required, the **convex hull** `[min t₀, max t₁]`. Use **union** for utilization; use **hull** for lead time.
  *Properties:* idempotent, commutative, monotone under set inclusion.

* **Resource aggregation — `Γ_work(S)`**
  For a set `S` of Work parts, returns the **aggregated resource ledger** (materials, energy, time, money) with de-duplication rules for shared and overlapped parts (context-declared).
  *Properties:* additive on **disjoint** parts; requires **overlap policy** otherwise (e.g., attribute costs to the parent once, not to each child).

**Manager’s tip:** Pick the coverage operator that matches your KPI: **union** for machine utilization; **hull** for calendar elapsed; never mix silently.

#### A.15.1:5.4 - Identity of a Work (extensional criterion, pragmatically framed)

Two Work records refer to the **same Work** iff, in the relevant context:

* their **time–space extent** is the same (within declared tolerance),
* they link to the **same `MethodDescription`**,
* they have the **same performer** (`U.RoleAssignment`), and
* they bind the **same parameters** (or declared‑equivalent values).

If any of these differ (or the context declares equivalence absent), they are **distinct** Work instances (e.g., a retry).

#### A.15.1:5.5 - Interruptions, retries, resumptions (episode policy)

* **Retry:** **new Work** with its own window and parameters; link via `retryOf`.
* **Resumption:** **same Work identity** split into **episodes** if the context’s **episode policy** declares so (e.g., “power loss under 5 minutes keeps identity”).
* **Rework:** **new Work** initiated after a failure in earlier Work; link the occurrences and put any causal attribution in the governing causal-use pattern.

**Why it matters:** plans, costs, and quality stats depend on whether you treat a disruption as **one episode** or **a new run**. Declare the policy **in the bounded context**.

#### A.15.1:5.6 - Compositionality of effects (Δ)

For any work occurrence with parts, the **effect of the whole** is the rules-declared composition of the effects of its parts plus any declared overheads and residuals. Composition aligns with the overlap rules used by `Gamma_work`, such as no double-count of shared fixed costs and consistent attribution of variable deltas.

### A.15.1:6 - Archetypal grounding (parallel domains)

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top run:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **Method-description source:** `Appendectomy_v5`.
* **Performer:** `U.RoleAssignment` with holder slot `OR_Team_A`, role value `SurgicalTeamRole`, bounded-context slot `Hospital_2025`, and current-window slot covering the surgery interval.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02–10:07 → **resumptionOf** same run (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Γ\_work:** totals consumables and staff time once (no double‑count for overlapping sub‑runs).

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top run:** `ETL_Nightly_2025‑08‑11T01:00–01:47`.
* **Method-description source:** `ETL_v12.bpmn`.
* **Performer:** `U.RoleAssignment` with holder slot `ETL_Runtime`, role value `TransformerRole`, bounded-context slot `DataOps_2025`, and current-window slot covering the ETL run.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage input and output once at the parent.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Method-description source:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer:** `U.RoleAssignment` with holder slot `LabRig_7`, role value `TransformerRole`, bounded-context slot `ThermoLab`, and current-window slot covering the lab run.
* **Work identity:** the occurrence is identified by the run interval plus occurrence references; the thermodynamic state-plane trace is a dynamics or geometry relation used to describe the change, not a work-control relation or ordered instruction sequence.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.

### A.15.1:6.4 - Bias-Annotation

| Bias | How A.15.1 prevents it |
| --- | --- |
| Plan-as-work bias | `U.WorkPlan`, schedules, method descriptions, and intended parameter bindings stay separate from the dated occurrence. |
| Log-as-work bias | Telemetry, dashboards, provenance rows, and work publications can evidence or describe a work occurrence; they do not become the occurrence. |
| Method-as-occurrence bias | `U.Method` and `U.MethodDescription` identify or constrain the way of doing; `U.Work` records the run-time enactment. |
| Evidence-as-authority bias | Evidence, assurance, gate, release, and causal-use claims keep their governing patterns and do not follow from a work record by appearance. |
| Record-only transformation bias | Record manipulation qualifies as `U.Work` only when the context declares the record or dataset as the affected product referent. |

### A.15.1:7 - Scope Declaration and Rationale

* **Applicability:** Use the same occurrence test for pragmatic costing, architectural accountability, teaching examples, and source or evidence questions; when the current claim is only about a description, publication, source, or evidence relation, apply the governing pattern for that claim.
* **Scope declaration:** Universal; temporal semantics and episode policy are **context‑local** via `U.BoundedContext`.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment`, direct `Work.performedBy = RoleAssignment` wording, and derived `RoleEnactmentFact` when a named fact is needed, so that costing, quality, and audit rest on **runs**, not on plans or recipes.

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is a dated run-time occurrence. It is not a `U.Method` (semantic way), not a `U.MethodDescription` (description), not a `U.Role` or `U.RoleAssignment` (assignment), and not a `U.WorkPlan` (plan or schedule).

**CC-A15.1-2 (Required links).**
A conforming `U.Work` claim names:
(a) `enactsMethod -> U.Method` (the method enacted),
(b) `methodDescriptionRef -> U.MethodDescription` when the source episteme or editioned method description is current,
(c) `performedBy -> U.RoleAssignment` (the assigned performer in context), and
(d) `executedWithin -> U.System`; if ordinary speech says subsystem, name the `U.System` in subsystem position plus the part relation to the larger holon under A.1, A.14, or B.1.2.

**CC-A15.1-3 (Time window).**
A conforming `U.Work` claim carries a closed interval `[t_start, t_end]`, or an explicitly marked open end for in-flight work, and, where relevant, location or asset.

**CC-A15.1-4 (Context reference and judgement).**
A `U.Work` claim is judged inside a declared `U.BoundedContext` (the judgement context).

- By default, the judgement context is the context of the referenced method-description source.
- If `performedBy` references a `U.RoleAssignment` in a different context, cross-context acceptance needs an explicit bridge relation or policy. Otherwise the work claim is not admitted in that context.

**CC-A15.1-4b (State-plane reference).**
The work claim names the `StatePlaneRef` used for its delta judgement.

**CC-A15.1-5 (RoleAssignment interval coverage).**
The `performedBy` `U.RoleAssignment` timespan covers the work interval. If it does not, lower the claim to a non-admitted role-assignment relation for that context or re-judge it in a context that admits retroactive assignments.

**CC-A15.1-6 (Parameter binding).**
Parameters declared by the `U.MethodDescription` have concrete values bound at work creation or start and recorded with the work occurrence. Defaults in the method description do not by themselves admit the performed-work claim.

**CC-A15.1-7 (Capability check).**
Capability thresholds stated by the `U.Method` or `U.MethodDescription` are checked against the holder in `performedBy` for the performed-work interval or declared checkpoints. Violations are recorded on the work outcome.

**CC-A15.1-8 (Acceptance criteria).**
Success and failure classes and quality grades are determined by the acceptance criteria declared or referenced by the `U.MethodDescription` or comparator specification in the judgement context. The verdict is recorded on the work occurrence.

**CC-A15.1-9 (Resource honesty).**
Performed consumptions and costs (energy, materials, machine-time, money, tool wear) are booked to `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans; performed values belong in work occurrences.

**CC-A15.1-10 (Mereology declared).**
When a work occurrence has parts, the selected part relation is declared: temporal-part, episode-part, operational-part, or concurrent-part. Ambiguous mixtures lower aggregation and identity claims.

**CC-A15.1-11 (Temporal coverage selection).**
For a roll-up, the judgement context declares which temporal coverage operator applies: union for utilization or convex hull for lead time. Silent mixing lowers the KPI or comparison claim.

**CC-A15.1-12 (Resource aggregation).**
Aggregation of resource ledgers across work parts names an overlap policy, such as attributing shared machine-time to the parent only, before totals are used.

**CC-A15.1-13 (Identity and retries).**
A retry is a new `U.Work` occurrence linked via `retryOf`. Interruptions treated as the same run are represented as episodes (`resumptionOf`) under a context-declared episode policy.

**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-context evidence).**
If a work occurrence is accepted in multiple contexts, either re-judge it in each context or provide bridge relations that map acceptance criteria, units, and role-assignment relations. Name identity alone does not carry cross-context acceptance.

**CC-A15.1-16 (Method-description source changes during work).**
If the method-description version changes mid-run, split the work into episodes bound to respective method-description source editions, or record an explicit method-description override event in the judgement context. Silent substitution lowers the work claim.

**CC-A15.1-17 (Distributed performers).**
If multiple `U.RoleAssignment` values jointly perform the same top-level work occurrence, either designate a lead `U.RoleAssignment` with concurrent parts, or model the top-level occurrence as a parent work with child work occurrences per `U.RoleAssignment`.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry evidence a work occurrence only after they are bound to method-description source when current, performer, time window, affected referent, and judgement context.

**CC-A15.1-19 (Affected referent).**
Each `U.Work` claim names at least one affected referent, such as asset, product, batch, dataset, or document, through `affected -> {...}`.

**CC-A15.1-20 (State-change witness).**
Each `U.Work` claim carries either explicit pre-state and post-state references on the declared state-plane or a delta predicate evaluable on evidence. A no-op run is flagged as such.

**CC-A15.1-21 (Affected-referent declaration vs. record handling).**
A run whose only effect is copying or reformatting records qualifies as `U.Work` only when the judgement context declares those records to be the product referent, such as data-product manufacture.

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
Across-run comparison presented on a `U.Work` publication view uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a `U.Work` publication view pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. Bridge ids carry cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

### A.15.1:9 - Temporal & Aggregation Semantics (normative operators & invariants)

#### A.15.1:9.1 - Temporal coverage `Γ_time`

* **Input:** a finite set `S` of Work instances or Work parts.
* **Output:** either (a) the **union** of their intervals, or (b) the **convex hull** `[min t_start, max t_end]`—**as declared by context** and KPI.
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

### A.15.1:10 - Cross-Context Checks (MethodDescription, RoleAssignment, and Work)

When a Work is recorded, perform these **three quick checks**:

1. **Method-description context check.** Does `methodDescriptionRef` refer to a MethodDescription **defined in** the judgement context, or bridged to it, when that source is current?

   * If **no**, the Work is **out‑of‑context**; either change context or add a Bridge.

1. **RoleAssignment interval and context check.** Does `performedBy` cover the work interval in the same context, or is it bridged?

   * If **no**, the Work is **unassigned** for that context; remedy via a covering `U.RoleAssignment` or a policy exception.

1. **Standard-Outcome Check.** Do the Work inputs, outputs, and metrics satisfy the **acceptance criteria** from the method-description source or declared standard **as interpreted in that context**?

   * If **no**, the Work **fails** or is “conditionally accepted” per context policy.

> **Manager’s mnemonic:** Context, assignment, Standard → **CAC**. Fail any → the Work is not acceptable *here* (perhaps acceptable elsewhere).

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed run."** Dumping telemetry without occurrence references (method-description source when current, performer, time window, affected referent, context) -> **Not Work**. Create a work-occurrence record and link the log as evidence.
* **Record-only transforms.** ETL or replication of records with no declared affected referent (product or dataset as product) -> **Not Work** in this context; either declare the dataset as the product referent or treat the material under `U.WorkPlan` or the relevant operations pattern.
* **Silent cross‑context acceptance.** “Ops accepted it, so audit accepts it.” → Add a **Bridge** or re‑judge in audit context.
* **Method-description edition drift in mid-run.** Swapping SOP v5->v6 without recording -> split into episodes or record method-description override.
* **Budget on the method.** Charging costs to Method or Role -> Book **only** to Work; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.

### A.15.1:12 - Existing work-log repair applications

1. **Backfill links.** For existing logs, create work-occurrence records and attach `enactsMethod`, `methodDescriptionRef` when current, and `performedBy`.
2. **Name the context.** Pick the judgement context explicitly; add Bridges if multiple contexts accept.
3. **Record the episode policy.** Decide when an interruption keeps identity or forces a new run.
4. **Choose Γ\_time per KPI.** Put "union" or "hull" in the KPI definition so disputes expose the coverage policy instead of hiding it.
5. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
6. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record performed values.
7. **Parameter blocks.** Make parameters explicit and bind them at start; root-cause analyses become easier.

### A.15.1:13 - Consequences

| Benefits                                                                                                                 | Trade-offs and mitigations                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Costs, time, and quality attach to concrete runs; root‑cause analysis and accountability improve. | **More records.** You create Work instances; mitigate with templates and automation.       |
| **Sound roll-ups.** Γ\_time and Γ\_work turn roll-ups from hand-waving into declared policy; KPIs become comparable.     | **Policy discipline.** Choose union or hull and an overlap policy before using the roll-up; write that policy once. |
| **Cross‑context clarity.** CAC checks prevent silent model drift; bridges make acceptance explicit.                      | **Bridge upkeep.** Keep mappings short and focused; review at releases.                    |
| **4D extensional coherence.** Parts, overlaps, and retries stop double-counting and identity confusion.                  | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |

### A.15.1:13.0 - Rationale

`U.Work` is kept as a dated occurrence because method, method description, work plan, and result are different FPF objects. The same source phrase can point to several of them, but performed-work claims need occurrence evidence, time bounds, role assignment, and affected EntityOfConcern rather than a convenient method or plan label. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local `U.Work` distinction: dated occurrence, role-assigned performer, enacted method, method-description source when current, time window, affected referent, resources, outcome, and evidence-provenance relation. Historical occurrence modeling is used as lineage only when a current standard or current practice still needs the same distinction.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` is an occurrence with temporal extent and occurrence references; parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, or log entry as proof of a performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they are bound to involved objects, performer or role-assignment relation, method, time window, context, and affected referent. | Treating telemetry or event rows alone as `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.57.0 and current traces, metrics, and logs practice. | Telemetry is an evidence relation or archive input. It can replay, measure, or diagnose a work occurrence, but the occurrence still needs performer, method, context, time window, affected referent, resources, and outcome. | Counting trace, metric, or log existence as the performed work or as dominance evidence without the governing comparison or archive policy. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Work records state evidence-provenance relation references and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | Roll-ups require declared `Gamma_time`, `Gamma_work`, and overlap policy; partial order and overlap are not hidden in step labels. | Mixing union, hull, parent cost, child cost, and ordinal comparison without a declared policy. |

### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`.
* **Coordinates with:** A.15 Role-Method-Work Alignment (the "four-slot grammar"); B.1 Gamma (aggregation) for resource and time operators; `E.10` and `E.10.ARCH` for source cues such as process, workflow, activity, schedule, algorithm, solver, and procedure; `A.10`, `B.3`, `E.17`, and `A.15.4` when evidence, assurance, publication-use, or source-restoration claims are being made; `A.15.5` when readiness or full-kit preparation is current before performed work; `C.32.P2S` when performed work realizes or inspects selected structures in an architecturing flow.
* **Informs:** reporting and KPI patterns; assurance and evidence patterns (Work as the reference occurrence for audits); scheduling patterns (`U.WorkPlan` -> `U.Work` deltas).

### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Four-slot grammar:** Who? **RoleAssignment**. Can? **Capability**. How? **Method or MethodDescription**. Did? **Work**.
* **CAC checks:** **Context** (judgement), **assignment** (covering `U.RoleAssignment`), **Standard** (acceptance criteria).
* **Roll‑ups:** `Γ_time = union` (utilization) or `hull` (lead time); `Γ_work` with a declared overlap policy.
* **Episodes vs retries:** same run split vs new run; write the policy.
* **Resource honesty:** performed values booked **only** to Work; estimates belong in method descriptions or plans.

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, `U.Work` states the dated occurrence: performer, method-description source, parameters, resources, time window, pre-state, post-state, outputs, outcome, and audit trace.

A `U.Work` occurrence may cite a `U.WorkPlan`, `SlotFillingsPlanItem`, or prior `WorkEntryReadiness@Context` as planned baseline or pre-entry context. The performed-work record states launch values, performed values, substitutions, variance, telemetry, and result-related records; comparator, transport, `PrincipleFrame`, evidence, assurance, gate, and readiness claims are separate current relations when the carry-through record names them.

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.Work` claim when performer, enacted method, method-description source when current, time window, `executedWithin`, affected referent, parameter bindings, resources, outcome, or state-change witness cannot be named at the granularity required by the next performed-work use. The acceptable lowered record is a plan note, readiness-gap note, evidence note, source-gap note, source-restoration request, or method-description reference, not a backdated work occurrence.

Repair the work record when a subsequent source changes the work interval, performer, role assignment, enacted method, method-description edition, parameter binding, resource ledger, outcome, affected referent, state-plane reference, pre-state reference, post-state reference, overlap policy, or aggregation policy. Repair only the changed relation: do not rewrite the method when only evidence changed, do not rewrite evidence when only work time changed, and do not convert a plan or source-restoration request into work.

Refresh before cross-context acceptance, aggregation, comparison, result measurement, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer performed work, use the governing pattern for that relation and keep only the returned `U.Work` reference here.

### A.15.1:End

