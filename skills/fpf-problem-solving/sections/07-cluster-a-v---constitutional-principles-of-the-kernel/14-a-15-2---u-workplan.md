## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when the current claim is intended work: horizon, planned window, intended role values or role-admission conditions, planned constraints, resource budgets, dependencies, acceptance targets, and baselines for subsequent variance against performed `U.Work`.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, reservation, planning cue, or P2W preparation note is being treated as a method, method description, performed work, evidence, approval, gate result, publication cue, query-plan representation, or database query-optimizer representation. `U.WorkPlan` is an episteme for intended `U.Work`; it can coordinate intended work, but it does not make work happen.

**First output.** One plan record or `PlanItem` naming horizon, cadence, target `U.Method`, method-description reference when current, planned window, intended role values, role-admission conditions, capability-fit conditions, or proposed `U.RoleAssignment`, planned constraints, resource budgets, dependencies, acceptance targets, planned preparation or full-kit tasks when current, planned baseline, and the variance relation expected when `U.Work` occurs.

**First-use checks.**
1. Name the intended work occurrence or work family that needs planning.
2. Recover target method, method-description reference when current, planned window, intended role values, role-admission conditions, capability-fit conditions, planned resources, dependencies, acceptance targets, baseline, and context.
3. Decide whether the encountered planning input is a `U.WorkPlan`, a method description, performed `U.Work`, a `SlotFillingsPlanItem`, `WorkEntryReadiness@Context`, evidence, gate claim, `A.15.4` appearance-based reliance repair case, publication-use cue, or declarative representation. A planning input may be a record, cue, or plan element; that phrase is not a new kind.
4. Declare `PlanItem` decomposition, dependency relation, and planned-baseline policy before using the plan for coordination or variance.
5. When work occurs, connect the `U.Work` record back to the `PlanItem` and record variance rather than rewriting the plan as if it had happened.

**Ordinary use.** For simple coordination, a compact `PlanItem` with intended method, window, intended role value or role-admission condition, resource budget, dependency, acceptance target, and baseline is enough.

**Reliance-bearing use.** Use the fuller WorkPlan record when cross-role coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, release preparation, evidence-reference notes, source-currentness requests, or P2W carry-through depends on the plan.

**Stop condition.** Stop once the intended work is coordinated at the needed granularity or the encountered planning input is assigned to method, method description, performed work, evidence, gate, publication-use, declarative-representation, or `A.15.4` appearance-based reliance repair use without claiming to be a plan.

**What goes wrong if missed.** Teams treat calendars, tickets, reservations, or rollout notes as if work already happened, or treat a plan as method, evidence, gate result, approval, or publication authority.

**What this buys.** One intended-work record that keeps horizon, window, intended role values, role-admission conditions, capability-fit conditions, constraints, budgets, dependencies, acceptance targets, baseline, and subsequent variance against performed `U.Work` inspectable.

**Not this pattern when.** Not this pattern when the current claim is a dated performed work occurrence (`A.15.1`), a `SlotFillingsPlanItem` (`A.15.3`), work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used for work or reliance before the governing pattern slot or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).

### A.15.2:1 - Context (plain‑language motivation)

Operations happen in **time**. Even with perfect roles, abilities, and methods, nothing ships unless teams decide when and by whom concrete work occurrences are intended to happen, under what **constraints** and **budgets**. Teams need a first-class concept for **plans and schedules** that does **not** get confused with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **written recipe** (that is `U.MethodDescription`),
* the **performed work occurrence** (that is `U.Work`), or
* the **state-change model** (that is `U.Dynamics`).

`U.WorkPlan` is that missing intended-work record.

### A.15.2:2 - Problem (what breaks without `WorkPlan`)

1. **“Workflow = schedule” conflation.** Flowcharts or code are used as calendars; resource clashes and SLA misses follow.
2. **Plan and occurrence blur.** Gantt bars or Kanban tickets are reported as if the work already happened; audits and costing degrade.
3. **Specification and time leakage.** People and calendars creep into MethodDescriptions; reuse and staffing agility collapse.
4. **No variance model.** Without planned baselines, deviations in time, cost, and quality cannot be explained or improved.
5. **Structure entanglement.** BoM and org charts get baked into “process” views; plans become brittle and unmaintainable.

### A.15.2:3 - Forces (what the definition balances)

| Force                              | Tension we resolve                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain idioms** | One plan concept that fits hospitals, fabs, data centers, and research labs—while honoring local terms. |
| **Commitment vs. flexibility**     | Plans need enough firmness to coordinate, while remaining easy to update as reality changes.                         |
| **Intended performer vs. performed-work assignee** | Plans may name intended performers; the assignment used for performed work is still checked for the work interval. |
| **Budgets vs. performed resource use**            | Plans state targets and reservations; only `U.Work` records performed resource use.                                   |
| **Decomposition vs. fulfilment**  | Plan tasks decompose conveniently; they do not force a shape on performed Work occurrences.                       |

### A.15.2:4 - Solution - `U.WorkPlan` as the time-bound intention for `U.Work`

#### A.15.2:4.1 - Definition

**`U.WorkPlan`** is an **`U.Episteme`** that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended role values, role-admission conditions, or proposed `U.RoleAssignment`s**, **resource budgets and reservations**, and **acceptance targets** within a `U.BoundedContext`.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - `PlanItem` values (what a `WorkPlan` is made of)

A `U.WorkPlan` **contains `PlanItem` values** (think: scheduled tasks or operations), each of which typically states:

1. **Target Method and specification** — the **Method** to be enacted and the **MethodDescription** intended for enactment.
2. **Planned window** — e.g., earliest start and latest finish, timebox, recurrence (cron-like), blackout periods.
3. **Role-admission conditions** — intended `U.Role` values and role conditions, not people; optional proposed `U.RoleAssignment`s if pre-assignment is admitted in the context.
4. **Capability-fit conditions** — minimal abilities or envelopes expected of the performer, checked for the performed-work interval.
5. **Resource budgets and reservations** — planned energy, materials, machine windows, money, and reservations on assets.
6. **Dependencies** — precedence, overlap constraints, required gate references, and required approval references.
7. **Acceptance targets** — quality windows and SLA targets to be judged when Work completes.
8. **Location and asset constraints** — where the work occurrence is expected to take place.
9. **Links to Service promises** (if any) — external commitments that this plan aims to satisfy.

> **Didactic guardrail:** **No logs or performed occurrence values** belong in a WorkPlan; **no step logic** or solver internals either - that is the Method or MethodDescription.

#### A.15.2:4.3 - Clear distinctions for schedule, process, and workflow wording

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| "The **schedule** for tomorrow's surgeries" | **`U.WorkPlan`**                                     | Calendar of intended work occurrences with who and when constraints. |
| "The **workflow** for appendectomy"         | **`U.MethodDescription`** and `U.Method`             | Recipe and semantic way, not a calendar.          |
| "The **process** already ran at 10:00"      | **`U.Work`**                                         | A dated performed occurrence with resources and outcomes.          |
| "The **thermodynamic trajectory**"        | **`U.Work`** occurrence plus **`U.Dynamics`** model  | A realized trajectory plus its model, not a plan. |
| "The **plan** assigns Dr. Lee"              | **WorkPlan** naming an intended `U.RoleAssignment`   | Assignment is still checked for the work interval.        |
| "The **budget** for Shift-B"                | **WorkPlan** (planned ledger)                        | Actual costs land on **Work**, not on the plan.   |

> **Schedule-word guard.** Schedule-like words do not determine the kind by themselves. Use `U.WorkPlan` only when intended work, horizon or window, role constraints, resource constraints, dependencies, acceptance target, and baseline are current; otherwise recover method, method description, work, evidence, gate, publication-use, or declarative-representation claims separately.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or work occurrences)

Keep three separations crystal‑clear:

* **Method composition** -> admits a composite **`U.Method`** when recovered submethods, whole-forming relations, and whole-level commitments are current.
* **Work composition** -> relates performed **`U.Work`** occurrences as temporal parts, episodes, operational parts, concurrent parts, predecessors, successors, overlaps, containment, or another declared work relation.
* **Plan mereology** (epistemic structure) -> organizes **`PlanItem` values** for coordination (phases, sprints, shifts), with **precedence** and **resource reservations**.

**Common relations among `PlanItem` values:**

* **`Precedes_pl` or `DependsOn_pl`** — start and finish constraints and gates.
* **`MayOverlap_pl` or `MutuallyExclusive_pl`** — allowed overlaps versus exclusive windows.
* **`Refines_pl`** — a child `PlanItem` tightens windows and budgets of a parent.
* **`Alternative_pl`** — planned alternatives (e.g., backup rig, backup team).

**Didactic rule:** A `PlanItem` **does not force** an identical Work shape; its relation to performed Work is via **fulfilment** and **variance** (see §6).

#### A.15.2:4.5 - How `WorkPlan` Meets `Work` (Fulfilment and Variance)

When reality happens, each `U.Work` may:

* **Fulfil** a `PlanItem` — link `plannedAs → PlanItem`.
* **Partially fulfil** — multiple Work instances share one `PlanItem` (for example, a split occurrence), or one Work fulfils several `PlanItem` values (for example, consolidated batch).
* **Deviate** - occur with method or method-description substitution, different window, different performer, or policy exception.
* **Be unplanned** — Work with no `PlanItem` (emergency or ad hoc); record it as unplanned when that relation matters for variance, audit, or improvement.

**Variance dimensions** the plan expects to report on:

* **Schedule variance (Δt):** early or late versus planned window.
* **Cost variance (Δc):** actual resource spend vs budget.
* **Scope variance:** different Method or MethodDescription than planned (with justification).
* **Quality variance:** acceptance verdict vs target.
* **Assignment variance:** intended versus actual `U.RoleAssignment`.

> **Manager’s view:** A plan that cannot report variance is a calendar picture, not a management tool.

### A.15.2:5 - What a good `WorkPlan` states (review checklist)

Use this as a human-facing checklist (not a rigid schema):

1. **Horizon & cadence** (e.g., “W36 surgeries, daily ETL”).
2. **`PlanItem` values** with: target Method and MethodDescription, planned windows, dependencies.
3. **Role-admission conditions** (`U.Role` values and conditions), **capability-fit conditions**, and **intended assignments** (optional, context-admitted).
4. **Safety envelopes**, constraints, and other admissibility conditions for planned work.
5. **Resource budgets** and **reservations** on assets.
6. **Acceptance targets** (SLA and quality windows).
7. **Bridges** if plan spans **multiple contexts** (operations, audit, or regulatory).
8. **Baseline and version** plus **change notes** (so variance is attributable).
9. **Policy pointers** (episode policy, overlap policy for Work roll‑ups if needed for KPIs).
10. **Exception relation** (how ad hoc or emergency work is related back to planning, if that relation is needed).

### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025‑08‑12`.
* **`PlanItem` values:** `Case_1_Appendectomy`, `Case_2_Hernia`, with windows, context assignments, and surgeon `U.Role` values; anesthetist intended `U.RoleAssignment` provided.
* **Budgets:** OR time blocks, consumables envelopes.
* **Fulfilment:** Each surgery Work links to its `PlanItem`; variances computed (duration overrun, substitutions).

#### A.15.2:6.2 - Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36`.
* **`PlanItem` values:** `Tool_42 chamber clean`, `Tool_13 calibration`; **MutuallyExclusive\_pl** with production windows.
* **Reservations:** nitrogen, DI water, metrology window.
* **Fulfilment:** Actual clean Work happens earlier; variance logged as **early** with cost underrun.

#### A.15.2:6.3 - Data‑center rollout (multi‑context plan)

* **WorkPlan:** `DC_Rollout_Phase‑2`.
* **Bridges:** Ops context ↔ Security Audit context (different acceptance targets).
* **`PlanItem` values:** `Deploy Service A`, `Pen-test A`; dependencies across contexts.
* **Fulfilment:** Deployment Work passes ops targets; audit Work passes after the deployment work, with variance reported per context.

### A.15.2:7 - Scope Declaration and Rationale

* **Applicability:** Use the same intended-work test for coordination, budgeting, architecture planning, teaching examples, and source or evidence questions; when the current claim is performed work, evidence, assurance, publication-use, appearance-based reliance repair, or declarative representation, apply the governing pattern for that claim.
* **Scope declaration:** Universal; meanings of windows, budgets, constraints, and authorization references are **context-local** via `U.BoundedContext`.
* **Rationale:** Elevates **planning and scheduling** to a first-class episteme that coordinates Methods, `U.RoleAssignment`s, and Work without conflation.

### A.15.2:7a - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.2-1 | A conforming `U.WorkPlan` names intended `U.Work`, not performed work. | The record can state planned windows and baselines without claiming performed values. |
| CC-A15.2-2 | Each reliance-bearing `PlanItem` names target `U.Method`, method-description reference when current, planned window, intended role value or role-admission condition, planned resource budget, dependencies, and acceptance target. | A performer can prepare the intended work without treating the plan as performed work. |
| CC-A15.2-3 | Proposed `U.RoleAssignment`s remain intended assignments until checked for the performed-work interval by A.15 and A.15.1. | The plan does not accept the role assignment for that interval by publication alone. |
| CC-A15.2-4 | Performed cost, resource use, launch values, substitutions, telemetry, and outcomes belong to performed `U.Work`. | The plan points to the work record for performed values and variance. |
| CC-A15.2-5 | `PlanItem` decomposition does not force the same shape on performed work. | Fulfilment and variance relations explain split, consolidated, emergency, or substituted work. |
| CC-A15.2-6 | Cross-context planning names bridges before reusing planned windows, budgets, or acceptance targets across contexts. | Audit, regulatory, operations, and delivery contexts can judge the plan without hidden equivalence. |
| CC-A15.2-7 | Evidence, assurance, gate, launch-value, and result-measurement claims stay in the patterns that govern those relations. | The WorkPlan may state evidence-reference notes or requests, but it does not become evidence, assurance, gate passage, or result measurement. |
| CC-A15.2-8 | Planned preparation or full-kit tasks may appear in the WorkPlan, but `WorkEntryReadiness@Context` is governed by `A.15.5`. | The plan may say what should be prepared; it does not decide readiness for work entry by itself. |

### A.15.2:7b - Common Anti-Patterns and How to Avoid Them

- **Plan-as-actual.** Do not treat a Gantt bar, Kanban ticket, shift rota, or calendar booking as performed work; create or cite the `U.Work` occurrence when work happens.
- **Workflow-as-schedule.** Do not treat a method description or flowchart as a plan; make a `U.WorkPlan` only when intended windows, constraints, role-admission conditions or intended role values, and baselines are current.
- **Assignment-by-plan.** Do not treat an intended performer in the plan as a `U.RoleAssignment` satisfying the governing role, holder, and bounded-context constraints for the work interval; validate assignment when the work occurrence is prepared or recorded.
- **Budget-as-cost.** Do not book planned budgets as performed resource use; performed values belong to `U.Work`.
- **Plan-shape overreach.** Do not force performed work to match plan decomposition; use fulfilment and variance relations.
- **Evidence-note-as-claim.** Do not treat evidence-reference notes, gate-preparation notes, or source-currentness requests as evidence, gate passage, assurance, or release authorization.

### A.15.2:7c - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Plans become inspectable without being confused with performed work. | More explicit records; mitigate by using compact `PlanItem` values for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep baseline and version visible on the plan. |
| Cross-role and cross-context coordination becomes safer. | Requires bridge checks when contexts differ; name only the bridge needed for the planned use. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.15.5`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, appearance-based reliance repair, work-entry readiness, evidence, assurance, gate, or constraint relation becomes current. |

### A.15.2:7d - SoTA Alignment

| Source tradition | Local invariant adopted | Shortcut rejected |
| --- | --- | --- |
| ISO 21502:2020 project-management guidance and PMBOK Guide Eighth Edition (2025) | A plan is an intended-work coordination episteme: horizon, selected delivery approach or method family, baseline, dependencies, resource expectations, and acceptance targets are declared before performed work and compared with performed values after work occurs. | Treating a schedule, ticket, or baseline as evidence that the work already occurred. |
| ISO 55000:2024 asset-management practice | Asset reservations, maintenance windows, lifecycle objectives, risk, and value expectations belong in planning until actual work changes asset state or resource use. | Treating planned asset availability or reserved capacity as actual asset intervention or actual resource consumption. |
| ISO 9001:2015 with Amendment 1:2024 quality-management practice | Planned quality objectives, acceptance targets, change notes, and performance evaluation stay replayable so variance can drive improvement. | Editing the plan after the fact so that quality, cost, or schedule variance disappears. |
| Case-management and adaptive-work notation practice such as OMG CMMN 1.1 | Weakly structured or ad hoc work can still be related to a plan through case, exception, fulfilment, and variance relations. | Forcing every emergency, adaptive, or consolidated work occurrence into the original plan shape. |

### A.15.2:7e - Relations

* **Builds on:** `A.15` Role-Method-Work Alignment, `A.15.1` `U.Work`, `A.2.1` `U.RoleAssignment`, `U.Method`, and `U.MethodDescription`.
* **Coordinates with:** `A.15.3` for `SlotFillingsPlanItem` values, `A.15.4` for work-relevant appearance-based reliance repair, `A.15.5` for work-entry readiness and full-kit preparation, `A.10` for evidence-provenance relations, `B.3` for assurance, `A.20` and `A.21` for gates and constraint decisions, `C.32.P2S` for architecturing-flow refs to intended work that realizes selected structures, and `E.17` for publication-use questions.
* **Used by:** P2W carry-through when principle-to-work reasoning reaches WorkPlanning, and P2S carry-through when architecture-selected structures require intended work records. Both uses keep plan, work-entry readiness, performed work, evidence, gate, and result-measurement relations separate.

### A.15.2:8 - P2W WorkPlanning Use Relation

When `E.18.1` reaches WorkPlanning, `U.WorkPlan` states intended work occurrences, planned windows, intended role values, role-admission conditions, capability-fit conditions, planned constraints, resource budgets, acceptance targets, evidence-reference notes, source-currentness requests, and `PlanItem` values.

When the P2W use also needs a readiness question, the WorkPlan may supply target PlanItems, planned preparation tasks, reservations, and planned baselines. `A.15.5` carries the `WorkEntryReadiness@Context` relation that judges full-kit condition, commitment disposition, resource readiness, WIP or flow policy, and launch-gate refs when those are current.

If the same P2W source material also makes a performed-work, launch-value, evidence, gate, result, measurement, publication-use, appearance-based reliance repair, or refresh claim, write that meaning as a separate current relation before using the plan.

### A.15.2:9 - Launch-Value Boundary For P2W

For P2W use, `U.WorkPlan` may state planned values, planned fillers, constraints, reservations, intended performers, and evidence-reference notes. Launch values are finalized only at performed-work entry under the current gate relation and performed-work pattern and are recorded with the performed `U.Work` and related gate and provenance records when current.

### A.15.2:10 - Lowering, Repair, and Refresh Conditions

Lower a candidate `U.WorkPlan` claim when horizon, planned window, target method, method-description reference when current, intended role value or role-admission condition, planned constraint, resource budget, dependency, acceptance target, or baseline cannot be named at the granularity required by the next planning use. The acceptable lowered result is a planning cue, method-description note, missing-source-relation note, `A.15.4` repair request, publication-use cue, declarative-representation note, readiness-gap note for `A.15.5`, or evidence-reference note, not a conforming WorkPlan.

Repair the WorkPlan when a subsequent source changes the intended method, planned window, intended role value or role-admission condition, planned resource budget, dependency, acceptance target, baseline, version, bridge, or exception policy. Repair the plan; do not rewrite performed `U.Work` unless the work record itself changed, and do not make the repaired plan into evidence that the work occurred.

Refresh before relying on a WorkPlan for cross-context coordination, budget reservation, release preparation, gate preparation, work-entry readiness, evidence-reference use, performed-work entry, result measurement, or P2W carry-through. If the claim being made after refresh is work-entry readiness, performed work, evidence, assurance, gate passage, publication use, declarative representation, or appearance-based reliance repair, use the governing pattern for that relation and keep only the returned WorkPlan relation here.

### A.15.2:End

