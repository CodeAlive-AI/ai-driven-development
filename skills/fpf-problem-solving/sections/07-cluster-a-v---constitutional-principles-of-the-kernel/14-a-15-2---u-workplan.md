## A.15.2 - U.WorkPlan

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.WorkPlan` when one exact episteme carries substantive claims for coordinating possible future performed work over a horizon through `PlanItem` content: intended method, planned window, performer and role conditions, capability-fit requirements, resource budgets, dependencies, commitments, acceptance targets, and a baseline for later comparison. C.2.1 keeps the episteme identity through one already identified present EntityOfConcern. A designator for merely possible future performance remains claim content; it neither designates a dated Work occurrence admitted under `U.Work` nor becomes another entity merely because it is planned.

**Use this when.** Use this pattern when a schedule, calendar, rota, Kanban ticket, Gantt bar, shift plan, rollout plan, reservation, planning cue, or P2W preparation note may be an episteme about intended work but is being treated as a method, method description, performed work, evidence, approval, gate result, publication cue, query-plan representation, or database query-optimizer representation. A system may use `U.WorkPlan` to coordinate intended work only when the plan's substantive claims, present EntityOfConcern, effective reference scheme, and intended-performance designators are recoverable. The episteme itself neither acts nor makes work happen.

**First useful object.** One exact `U.WorkPlan` episteme with one present EntityOfConcern and at least one `PlanItem` content component. The content names the possible future performance or repeated-work subject being coordinated, horizon, target `U.Method`, an exact method-description use when current, planned window, intended performer and role conditions, A.2.2 capability-fit requirement, constraints, resource budgets, dependencies, commitments, acceptance targets, planned preparation tasks when current, baseline, and the later local fulfilment or variance question that a receiving use needs.

**First-use checks.**
1. Identify one present `U.Entity` that the plan claims concern, as C.2.1 requires. It may be an exact existing system, asset, promise-content edition, or other direct-owner entity for which work is being coordinated; when the claims are expressly reflexive, C.2.1 permits the same plan episteme as its own EntityOfConcern. Name possible future performances, a repeated-work family, or a proposed group separately as plan-content designators. If no one joint present EntityOfConcern can be identified, split the claim content or lower the cue rather than treating a future Work occurrence as already existing.
2. Recover target method, exact method-description use when current, horizon, planned window, intended performer and role conditions, A.2.2 capability-fit requirement, planned resources, dependencies, commitments, acceptance targets, baseline, and effective reference scheme. A desired participant, operation argument, or operation result enters as A.15.3 declaration-local planned-filling content only against one exact declaration member whose direct pattern owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate; A.15.2/A.15.3 own the intended-use claim. If no reusable planned filling is needed, keep the choice as ordinary plan content; if typed reuse is needed but the exact member, corresponding predicate, or direct owner is absent, return the exact missing-governor blocker. An expected effect enters only as a plan claim under its exact direct pattern.
3. Decide whether the encountered source or cue supports a `U.WorkPlan`, a method description, a performed Work occurrence admitted under `U.Work`, A.15.3 planned-filling content, `WorkEntryReadiness@Context`, evidence, a gate claim, an `A.15.4` appearance-based reliance repair case, a publication-use cue, a forecast or dynamics model, or a declarative representation. A record, cue, diagram, or plan element remains a representation or source item until its exact governed claim is recovered.
4. Declare the `PlanItem` organization, governed base claims or constraint semantics, baseline policy, and the exact later local fulfilment or variance question before coordinating or comparing the plan. A readable one-case answer may stop at A.6.RCD disposition 2 as a local compound assertion. Repeated use of the same parameterized rule may justify disposition 3's reusable predicate-definition episteme without a relation kind. Open a relation-kind candidate only when a receiving use genuinely consumes occurrence semantics, and then require the A.6.RCD admission route, a standalone direct governor, obtaining and applicability laws, and a non-optional occurrence-identity rule; otherwise return `missing-governor` for that dependent use.
5. When work occurs, first identify the exact Work occurrence independently as an individual admitted under `U.Work` by A.15.1. A separate plan-use assertion may then compare exact plan content with independently obtaining relations involving that occurrence under a named policy; it does not rewrite the plan, create an actual-use fact, or turn the local assertion into a universal relation kind.

**Ordinary use.** For simple coordination, one `PlanItem` content component inside one exact `U.WorkPlan`, with intended method, planned window, intended performer or role condition, resource budget, dependency, commitment or acceptance target, and baseline, is enough.

**Reliance-bearing use.** Use fuller WorkPlan claim content when cross-role coordination, budget reservation, delivery commitment, gate preparation, audit expectation, cross-context acceptance, release preparation, evidence-reference notes, source-currentness requests, or P2W carry-through depends on the plan.

**Stop condition.** Stop once a system can coordinate the intended work at the needed granularity or the encountered source or cue is assigned to method, method description, performed work, evidence, gate, publication use, representation, forecast or dynamics, or `A.15.4` appearance-based reliance repair without claiming to be a plan. Stop only the dependent typed-relation use when its direct governor is absent; the plan and any truthfully expressible local claim remain usable.

**What goes wrong if missed.** Teams treat calendars, tickets, reservations, or rollout notes as if work already happened; identify a possible future performance as an existing Work occurrence; let the plan episteme act; or treat a plan as method, evidence, gate result, approval, or publication authority.

**What this buys.** One identifiable intended-work episteme whose present subject, horizon, windows, intended performer and role conditions, capability-fit requirements, constraints, budgets, dependencies, commitments, acceptance targets, baseline, and later comparisons with independently identified Work occurrences remain inspectable.

**Not this pattern when.** Not this pattern when the current claim is a dated performed work occurrence (`A.15.1`), A.15.3 declaration-local planned-filling content, work-entry readiness or full-kit condition (`A.15.5`), a reliance appearance being used before the governing pattern or relation is recovered (`A.15.4`), a method (`A.3.1`), a method description (`A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), a non-agentive forecast or dynamics model (`A.3.3`), or a declarative representation overread as a work-control or method claim (`C.2.P.DR`).

### A.15.2:1 - Context (plain‑language motivation)

Intended operations are coordinated in **time**. Even with suitable roles, abilities, and methods, no intended performance begins merely because it is forecast or described: a system must decide when and by whom possible future work is intended, under what **constraints** and **budgets**. Teams need a first-class concept for **plans and schedules** that does **not** get confused with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **written recipe** (that is `U.MethodDescription`),
* the **performed work occurrence** (an individual admitted under `U.Work`), or
* the **state-change model** (that is `U.Dynamics`).

`U.WorkPlan` is that missing intended-work episteme.

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
| **Budgets vs. performed resource use** | Plans state targets and reservations; A.15.1 and the exact resource-use or ledger pattern govern performed resource-use facts. |
| **Decomposition vs. fulfilment**  | Plan tasks decompose conveniently; they do not force a shape on performed Work occurrences.                       |

### A.15.2:4 - Solution - `U.WorkPlan` as the time-bound intention for `U.Work`

#### A.15.2:4.1 - Definition, membership, and identity

`U.WorkPlan` is a same-individual dependent kind under `U.Episteme`. C.2.1 first identifies exact episteme P by:

```text
<exact ClaimGraph, one already identified present EntityOfConcern, effective U.ReferenceScheme>
```

A.15.2 recognizes that same P as `U.WorkPlan` when its ClaimGraph substantively declares coordination of possible future performed work over one exact horizon through at least one `PlanItem` and, when several items are current, their plan-content organization. The intended-performance designator may denote one proposed future performance, a named repeated-work family, or one bounded proposed group. It remains claim content: planning it neither asserts the existence of a dated Work occurrence nor makes a merely possible performance into C.2.1's already identified EntityOfConcern.

The present EntityOfConcern is the exact existing entity that the plan claims concern under its direct pattern. It may be an existing system, asset, promise-content edition, or another identified entity for which work is being coordinated. When the plan claims are expressly about their own coordination commitments, C.2.1's reflexive option permits P itself. When the claims concern several entities jointly, C.2.1 still requires one independently identified joint EntityOfConcern; otherwise split the claim content rather than filling the position with a list of unrelated or merely possible referents.

The stable positive membership condition is substantive intended-work content. At least one `PlanItem` must name its intended-performance designator and state the intended method or method family, planned window or entry condition, intended performer or role condition, and the constraints, resources, dependencies, commitments, acceptance targets, or baseline needed by the named receiving use. A calendar picture, ticket title, publication, approval cue, method description, forecast, or list of dates that supplies no such intended-work claims does not gain `U.WorkPlan` membership by format.

The dependent kind supplies no second identity rule. Changing exact ClaimGraph content, the present EntityOfConcern, or the effective `U.ReferenceScheme` identifies another episteme under C.2.1. An explicit `EpistemeEditionRelation` may preserve historical continuity only when its own predicate obtains. Changing only a file path, carrier, layout, publication occurrence, ticket key, or version label leaves identity unchanged when the three C.2.1 discriminators are preserved.

Planned methods, possible-performance designators, performer designations, role conditions, windows, desired fillings, capability-fit requirements, resource budgets, dependencies, commitments, acceptance targets, and expected effects are claim content or separately governed planned claims. They establish no dated work occurrence, obtaining `U.RoleAssignment`, capability-fit result, actual participant, resource use, transformation, result value, result episteme, produced entity, delivery, acceptance verdict, or downstream outcome.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

#### A.15.2:4.2 - `PlanItem` content

A `PlanItem` is a declaration-local content component in one exact `U.WorkPlan`, not a U-kind, future or performed work occurrence, method part, assignment, relation occurrence, or result record. Its designator is interpreted inside that exact plan edition. A receiving episteme may refer to the content component, but the designator or reference does not make its intended claims actual.

The following is an open recognition palette, not a closed record schema or an unnamed kind defined by enumeration. Include only the claim families needed by the receiving use, and keep every current neighboring relation under its direct governor:

1. **Target method and description use** — the `U.Method` intended for enactment and, when current, an exact `U.MethodDescription` edition used by one named planned instruction, reliance, constraint, or justification claim. The description neither identifies the method, constrains or justifies it by itself, nor becomes the enacted object.
2. **Planned window or entry condition** — earliest start, latest finish, timebox, recurrence, blackout period, or another exact intended temporal condition.
3. **Intended performer and role conditions** — intended holder designation, `U.Role` value, role-admission conditions, and, when already obtaining, an exact `U.RoleAssignment` intended to cover later work. A proposed holder-role tuple is not an obtaining assignment.
4. **Capability requirement** — an exact A.2.2 threshold or `CapabilityFitCondition` needed for work admission, plus any current capability reference. The plan neither creates `U.Capability` nor evaluates fit for the later work interval.
5. **Resource budgets and reservations** — intended energy, materials, machine windows, money, and exact reservation claims. A planned budget is neither a performed resource-use fact nor a B.1.6 aggregate ledger result.
6. **Dependencies and commitments** — exact precedence, overlap, exclusivity, gate, approval, source-currentness, promise, or other planned claims under their direct predicates and conditions. A reference states neither gate passage, approval, promise fulfilment, nor world-side ordering by itself.
7. **Acceptance targets** — an exact criterion, quality window, or SLA target to be evaluated later under its direct owner; the target is not an evaluation or acceptance verdict.
8. **Location, affected-subject, and asset constraints** — where a proposed performance is intended to occur and which existing referent it is intended to concern, without asserting actual participation or change.
9. **Desired planned bindings** — only A.15.3 declaration-local `SlotFillingsPlanItem` content against a current governed RelationSignature participant declaration, A.6.1 operation argument or result declaration, or another exact declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate. A.15.2/A.15.3 own the intended-use claim. Without that exact member and direct owner, keep the choice as ordinary plan content when no reusable planned filling is needed; otherwise return the exact missing-governor blocker.
10. **Expected effect, result, or delivery target** — an exact planned claim under the direct pattern for the intended changed subject, characteristic, evaluation value, entity, publication, delivery, or other effect. The broad words `output`, `result`, `outcome`, `deliverable`, or `handoff` do not name one plan field or one universal kind.

A method description may describe generic participant meanings and intended effects, but it supplies no planned filling by itself. A desired filling remains planned; an expected result or effect remains expected. Neither establishes a dated Work occurrence admitted under `U.Work`, actual participant, operation application, actual change, returned value, result episteme, produced entity, acceptance verdict, delivery occurrence, or downstream outcome.

> **Didactic guardrail:** No log, telemetry value, performed-work fact, actual participant, or actual result belongs in WorkPlan identity-bearing claims merely because the plan later receives a comparison. Step logic and solver internals remain with the exact Method, MethodDescription, Mechanism, or representation pattern.

#### A.15.2:4.3 - Clear distinctions for schedule, process, and workflow wording

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| "The **schedule** for tomorrow's surgeries" | **`U.WorkPlan`** | Episteme declaring intended cases, windows, performer and role constraints, resources, dependencies, and targets without asserting occurrence. |
| "The **workflow** for appendectomy"         | **`U.MethodDescription`** and `U.Method`             | Recipe and semantic way, not a calendar.          |
| "The **process** already ran at 10:00" | A Work occurrence admitted under `U.Work` only when A.15.1 grounds that dated individual | Exact performer-assignment, enacted-method, temporal, containing-system, participant, affected-referent, and resource-use relations must obtain independently as required by the receiving claim; change, result, acceptance, and outcome stay separately governed. |
| "The **thermodynamic trajectory**" | **`U.Dynamics`** representation or model; add exact changed-subject and `U.Transformation` claims only when their direct predicates obtain | A trajectory expression is neither plan nor performed work by form. |
| "The **plan** assigns Dr. Lee" | **`U.WorkPlan`** carrying an intended holder and role claim; optionally cite an already obtaining `U.RoleAssignment` | The plan does not create or validate an assignment for the performed-work interval. |
| "The **budget** for Shift-B" | **`U.WorkPlan`** planned resource-budget claim | Actual performed resource use is established through independently obtaining relations involving exact Work occurrences under A.15.1 and the direct resource-use owners; any aggregate ledger or allocation result stays with B.1.6. |

> **Schedule-word guard.** Schedule-like words do not determine the kind by themselves. Use `U.WorkPlan` only when intended work, horizon or window, role constraints, resource constraints, dependencies, acceptance target, and baseline are current; otherwise recover method, method description, work, evidence, gate, publication-use, or declarative-representation claims separately.

#### A.15.2:4.4 - Plan mereology (composition of plans ≠ composition of methods or work occurrences)

Keep three separations crystal-clear:

* **Method composition** admits a composite `U.Method` only when A.3.1/B.1.5 or another exact method owner supplies recovered submethods, whole-forming relations, and whole-level commitments.
* **Work organization** starts with exact A.15.1 work-part relations. Temporal overlap is an independently governed interval fact under B.1.4, and coordination is a separate direct claim when it obtains. Shared parentage or overlap creates neither a `ConcurrentPartOf_work` primitive nor coordination.
* **Plan-content organization** arranges declaration-local `PlanItem` components inside the exact ClaimGraph for coordination. It is epistemic organization, not world-side work or method mereology.

Common plan-content claim families include:

* **precedence or dependency constraints** naming exact source and target item designators, start or finish conditions, and any prerequisite or gate condition;
* **overlap or exclusivity constraints** naming the exact scheduling policy and the windows it permits or excludes;
* **refinement claims** stating which intended-performance designator is preserved and exactly which window, constraint, target, or budget is tightened; and
* **alternative claims** stating the alternatives and the independently governed condition used to choose among them.

These prose families and any local spellings do not admit reusable relation kinds. Each current claim stays inside the exact WorkPlan ClaimGraph and names its predicate, participants, governed base claims or fully stated constraint semantics, derivation when compound, condition, scope, and qualification. A graph edge, row order, or repeated spelling creates no world-side ordering, assignment, resource use, work parthood, or typed relation. If another use repeats the same parameterized semantics, A.6.RCD may first yield a reusable predicate-definition episteme without occurrence ontology. Only a receiving need for distinct relation occurrences opens a derived- or primitive-kind candidate, the E.24/E.24.UK admission route, a standalone direct pattern, and A.6.REL occurrence discipline after admission. Absent the needed substrate, definition owner, or occurrence settlement, return the exact blocker rather than minting `Precedes_pl`, `MutuallyExclusive_pl`, `Refines_pl`, or another pseudo-kind here.

**Didactic rule:** A `PlanItem` does not force an identical work shape. A later one-case comparison with an independently identified Work occurrence remains a separate local plan-use assertion unless an admitted direct relation has actually been supplied.

#### A.15.2:4.5 - How `WorkPlan` meets `Work`

First identify exact `W : U.Work` under A.15.1. For an ordinary one-case question, use A.6.RCD disposition 2: create or cite a separate C.2.1 assertion episteme whose EntityOfConcern is exact WorkPlan edition P and whose ClaimGraph says whether W's independently governed performer assignments, enacted method, temporal extent, affected referent, application or subject-relation bindings, and performed resource-use facts satisfy exact content component I under named policy edition F. A negative answer is assertable only when F supplies an applicable explicit negative or closure criterion and the exact case facts satisfy it. F states the governed base predicates, mapping or derivation, applicability, polarity, and boundary needed by this use. This is a local compound assertion about P; it neither adds actual facts to P nor admits a `WorkPlanFulfilmentRelation` kind.

The assertion makes exact W, exact P edition, declaration-local I designator, exact F, polarity, and the supporting independently obtaining relations involving W recoverable. Failure of an applicable explicit criterion can support a governed negative claim; absent or unavailable occurrence relations return `missing-information`, while absent predicate or policy authority returns `missing-governor`. Neither stop is the negative claim. A shared label, schedule window, ticket key, record link, or policy name alone establishes nothing. Several exact Work occurrences may satisfy different parts of I, and one consolidated Work occurrence may satisfy several items, only when the local assertion states the exact split or consolidation mapping under F. Exact unplanned Work remains a valid Work occurrence admitted under `U.Work`; a separate plan-use assertion may classify it as unplanned for one named variance or improvement use.

If a receiving practice repeatedly needs the same parameterized fulfilment rule but consumes no relation-occurrence identity, use A.6.RCD disposition 3 to publish one predicate-definition episteme with one truthful exact EntityOfConcern, participant meanings, derivation, applicability, polarity, dependencies, and currentness; it is not a `RelationSignature` or relation kind. Only when a named receiver also needs distinguishable fulfilment occurrences may A.6.RCD return a relation-kind candidate for E.24/E.24.UK admission, a standalone direct subject settlement, and later A.6.REL discipline. Until those requirements are met, return the exact blocker only for the stronger use; do not infer partlessness, deny the local assertion or reusable predicate semantics, or add a universal `fulfils` edge.

A variance question is handled in the same economy. Use a separate local comparison assertion, or the exact measurement, evaluation, acceptance, resource, temporal, or other direct relation already governing the compared values. Name one planned value in exact P and I, one independently governed actual value, the comparison method, scale, qualification window, and exact result. Do not make variance an intrinsic field of a Work occurrence, enter it into P's identity-bearing claim content, or rewrite the plan. Common comparison questions include:

* **schedule variance:** actual Work extent against the planned window, using the exact temporal comparison and any B.1.4 aggregate needed by the receiving KPI;
* **resource or cost variance:** exact A.15.1 performed resource-use facts or a B.1.6 aggregate result against the planned budget;
* **method variance:** actual `enactsMethod` against the intended method, including an exact substitution claim when current;
* **description-selection variance:** the exact method-description edition cited by a named assertion about a Work occurrence or by a separately governed instruction-use claim, compared with the planned description reference, without treating that episteme as enacted;
* **acceptance-target variance:** a separately governed measurement, evaluation, or acceptance verdict against the planned target; and
* **assignment variance:** every exact performed-work `U.RoleAssignment` against the intended holder and role claims.

> **Manager's view:** A plan that cannot support one exact later local fulfilment or variance question is only a calendar picture for that use, not yet a reliance-bearing WorkPlan.

### A.15.2:5 - What a good `WorkPlan` states (review checklist)

Use this as a human-facing recognition palette, not a rigid schema or a definition by enumeration:

1. **Present EntityOfConcern, horizon, and cadence** (for example, the current service system and “W36 surgeries” or “daily ETL”), with possible future performances kept as plan-content designators.
2. **`PlanItem` content components** with intended-performance designator, target Method, any exact method-description use, planned windows, and dependencies.
3. **Intended holder and role conditions**, any already obtaining assignment reference, and exact A.2.2 capability threshold or fit condition; a proposed tuple or threshold is not an assignment or fit result.
4. **Safety envelopes**, constraints, and other admissibility conditions for planned work.
5. **Resource budgets** and exact **reservation claims** on assets.
6. **Acceptance targets** with their direct criteria and intended qualification windows.
7. **Cross-context interpretation boundary:** pin each effective reference scheme; use F.9 only for an exact pair of `SenseCell` values and its admitted use, and use the direct owner for value conversion, target comparison, verdict reuse, or another stronger claim.
8. **Baseline and exact episteme edition relation** plus change notes, so variance is attributable without treating a version label as identity.
9. **Policy pointers** to A.15.1 work continuity, B.1.4 temporal aggregation, B.1.6 resource aggregation, and any exact local comparison policy needed by the receiving KPI.
10. **Exception question** stating how ad hoc or emergency Work will be handled by a local plan-use assertion; use one reusable predicate-definition episteme only for repeated semantics, and require an admitted direct relation kind before claiming fulfilment or exception occurrences.

### A.15.2:6 - Archetypal grounding (parallel domains)

#### A.15.2:6.1 - Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025-08-12`, whose present EntityOfConcern is the exact operating service system for that day; the proposed cases remain plan-content designators until surgery Work occurs.
* **`PlanItem` content:** `Case_1_Appendectomy`, `Case_2_Hernia`, with windows and intended surgeon and anesthetist holder and `U.Role` conditions; cite an exact `U.RoleAssignment` only when it already obtains.
* **Budgets:** OR time blocks, consumables envelopes, and exact reservation claims.
* **Later local assertion:** Each exact surgery Work occurrence is identified independently as an individual admitted under `U.Work`. A separate assertion about the plan edition then names the fulfilment policy and maps the independently obtaining `performedBy`, `enactsMethod`, temporal, affected-referent, binding, and performed resource-use relations involving each occurrence to the intended case content before any duration, substitution, resource, or acceptance comparison is made.

#### A.15.2:6.2 - Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36`, whose present EntityOfConcern is the exact fab system or governed asset group under concern.
* **`PlanItem` content:** `Tool_42 chamber clean`, `Tool_13 calibration`; the ClaimGraph carries an exact exclusivity constraint with production windows under the named scheduling policy, not a reusable `MutuallyExclusive_pl` relation kind.
* **Reservations:** nitrogen, DI water, metrology window.
* **Later local assertion:** The exact chamber-cleaning Work occurrence is identified independently as an individual admitted under `U.Work`. A separate assertion about this plan edition states how independently obtaining relations involving that Work individual satisfy the item under the named policy; its temporal extent and resource-use relations are then compared under A.15.1 and B.1.6 with the planned window and budget to state early completion and cost underrun.

#### A.15.2:6.3 - Data-center rollout (multi-context plan)

* **WorkPlan:** `DC_Rollout_Phase-2`, whose present EntityOfConcern is the exact rollout-owning system or current service system named by the plan.
* **Interpretation boundary:** Operations and Security Audit use separately pinned reference schemes and direct acceptance criteria. Reuse of a term such as “ready” or “passed” may cite F.9 only through an exact Bridge between two `SenseCell` values with stated losses and admitted use; F.9 does not translate target values or transfer a verdict.
* **`PlanItem` content:** `Deploy Service A`, `Pen-test A`; exact dependency and window claims name their predicates and conditions inside the plan ClaimGraph.
* **Later local assertions:** Exact deployment and audit Work occurrences are identified independently as individuals admitted under `U.Work`. Separate operations and audit evaluations apply their own targets and produce separately governed verdicts; plan-use assertions state exact local fulfilment and per-context comparison without adding those actual facts to the plan content or creating one cross-context fulfilment relation.

### A.15.2:7 - Scope Declaration and Rationale

* **Applicability:** Use the same intended-work test for coordination, budgeting, architecture planning, teaching examples, and source or evidence questions. When the current claim is performed work, a non-agentive forecast, dynamics, evidence, assurance, publication use, appearance-based reliance repair, or declarative representation, apply the direct pattern for that claim.
* **Scope declaration:** Domain-general where a system is actually coordinating possible future performed work. A tide table, weather forecast, simulation schedule, or predicted natural trajectory is not a WorkPlan unless its claim content also coordinates a system's intended Work. Interpretation is local through the effective `U.ReferenceScheme` and any exact selected model-use structure; `U.BoundedContext` and F.9 are used only when their own exact conditions are current.
* **Rationale:** Planning and scheduling become a first-class episteme that systems can use to coordinate intended methods, performer and role conditions, and possible future work without turning the episteme into an actor or the proposal into an occurrence.

### A.15.2:7a - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.2-1 | Exact C.2.1 ClaimGraph, one already identified present EntityOfConcern, and effective `U.ReferenceScheme` identify the episteme; A.15.2 adds one stable intended-work membership condition and no second identity. | A possible future performance or PlanItem designator is not used as an existing EntityOfConcern merely because it appears in the plan. Carrier, layout, publication, ticket key, and version label can change without reidentification when the three discriminators remain fixed. |
| CC-A15.2-2 | A conforming `U.WorkPlan` makes substantive claims for coordinating possible future performed work over an exact horizon through at least one `PlanItem`. | The plan states an intended-performance designator, method, window or entry condition, performer or role condition, and the constraints, resources, dependencies, commitments, targets, or baseline needed by its receiving use without asserting that a Work occurrence exists. |
| CC-A15.2-3 | Every `PlanItem` remains declaration-local plan content and names the possible future performance and claims it coordinates. | A `PlanItem` designator is not treated as a U-kind, future entity, method part, Work occurrence, assignment, relation occurrence, or result record. |
| CC-A15.2-4 | Intended holder and role claims and A.2.2 capability requirements remain planned. An exact `U.RoleAssignment` is cited only when it already obtains, and the plan supplies no capability-fit result. | Publication of a holder-role tuple or threshold creates neither assignment, capability, nor fit for the later work interval. |
| CC-A15.2-5 | A desired participant, argument, or result filling targets only A.15.3 content for an exact declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate; A.15.2/A.15.3 own the intended-use claim. | A meaning-only declaration, method-description wording, broad field label, compatible ValueKind, or missing actual-use predicate establishes no planned or actual participation; use ordinary plan content or return the exact missing-governor blocker. |
| CC-A15.2-6 | An expected change, result, entity, delivery, acceptance, or outcome is a plan claim under its exact direct pattern and remains expected. | No `output`, `result`, `outcome`, `deliverable`, or `handoff` field is treated as a universal kind or as proof that the object exists or the effect occurred. |
| CC-A15.2-7 | `PlanItem` organization names exact local predicates and conditions but does not admit relation kinds or force the same shape on performed Work. | Graph order and spellings such as `Precedes_pl` or `MutuallyExclusive_pl` establish no reusable relation or world-side fact. |
| CC-A15.2-8 | A one-case fulfilment answer is A.6.RCD disposition 2: a separate positive or governed-negative local compound assertion about the exact plan edition, supported by independently identified A.15.1 Work occurrences, independently obtaining relations involving them, and a substrate-admitted policy derivation. | Shared labels or links cannot close the claim. Negative polarity needs an applicable explicit criterion and case facts; unavailable relations return `missing-information`, absent authority returns `missing-governor`. Repeated semantics may use a predicate-definition episteme; only an occurrence-facing receiver can open relation-kind admission. |
| CC-A15.2-9 | A variance question compares exact planned and actual values through a local comparison assertion or their direct measurement, temporal, resource, evaluation, or acceptance owner. | Comparison method, scale, qualification window, and result are explicit; no universal variance relation or intrinsic Work field is inferred. |
| CC-A15.2-10 | Cross-context planning pins each effective reference scheme and separates sense alignment from value or verdict mapping. | F.9 is cited only for exact `SenseCell` Bridges and admitted use; target conversion, commitment, acceptance, and verdict reuse stay with direct governors. |
| CC-A15.2-11 | Evidence, assurance, gate, launch-value, and result-measurement claims stay in the patterns that govern those relations. | Evidence-reference notes or requests do not become evidence, assurance, gate passage, or result measurement. |
| CC-A15.2-12 | Planned preparation tasks may appear in the WorkPlan, but `WorkEntryReadiness@Context` remains governed by A.15.5. | The plan says what should be prepared; it does not decide readiness for work entry by itself. |

### A.15.2:7b - Common Anti-Patterns and How to Avoid Them

- **Future-work-as-entity.** Do not use a possible future performance or PlanItem designator as C.2.1's already identified EntityOfConcern or as a dated Work occurrence; keep it in plan claim content until an exact direct entity or occurrence exists.
- **Plan-as-actual.** Do not treat a Gantt bar, Kanban ticket, shift rota, or calendar booking as performed work; create or cite an exact Work occurrence admitted under `U.Work` only when A.15.1's occurrence basis is present.
- **Workflow-as-schedule.** Do not treat a method description or flowchart as a plan; make a `U.WorkPlan` only when present subject, intended-performance designator, horizon, window, constraints, performer or role conditions, and baseline are current.
- **Assignment-or-capability-by-plan.** Do not treat an intended holder, role, threshold, or capability reference as an obtaining `U.RoleAssignment`, capability instance, or fit result for later Work; apply A.2.1/A.2.2 at the exact interval and use.
- **Budget-as-cost.** Do not book planned budgets as performed resource use; establish performed facts on exact A.15.1 Work and any aggregate ledger or allocation under B.1.6.
- **Plan-shape overreach.** Do not force performed Work to match plan decomposition, infer non-fulfilment from a missing link or unavailable facts, or mint a fulfilment relation from a local comparison. Stop at a positive or governed-negative local compound assertion when it suffices; use a predicate-definition episteme for repeated semantics without occurrence identity; open relation-kind admission only for a named occurrence-facing need.
- **Context-bridge overreach.** Do not bridge contexts as wholes or use F.9 to convert planned values, commitments, criteria, or verdicts. F.9 relates exact `SenseCell` values and only grants its stated admitted use.
- **Evidence-note-as-claim.** Do not treat evidence-reference notes, gate-preparation notes, or source-currentness requests as evidence, gate passage, assurance, or release authorization.
- **Description-as-planned-filling.** Do not turn a method-description phrase such as input or output into a planned slot. Use A.15.3 only against one exact governed declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate, while A.15.2/A.15.3 own the intended-use claim; otherwise keep ordinary plan content or return the exact missing-governor blocker.
- **Expected-as-actual.** Do not treat a desired filling, expected effect, output, result, outcome, deliverable, or handoff as an actual participant, change, returned value, produced entity, delivery, acceptance, or downstream effect.

### A.15.2:7c - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Plans become inspectable without being confused with performed work. | More explicit claims; mitigate by using compact `PlanItem` content for ordinary coordination. |
| Variance becomes meaningful because planned baseline and performed work stay separate. | Requires discipline around baselines; keep the exact plan edition and baseline visible without treating a version label as identity. |
| Cross-role and cross-context coordination becomes safer. | Requires exact reference-scheme and direct-owner checks; use F.9 only for the `SenseCell` correspondence actually needed. |
| P2W carry-through can prepare work without pretending work already happened. | Use `A.15.1`, `A.15.3`, `A.15.4`, `A.15.5`, `A.10`, `B.3`, `A.20`, or `A.21` only when the performed-work, planned-baseline, appearance-based reliance repair, work-entry readiness, evidence, assurance, gate, or constraint relation becomes current. |

### A.15.2:7d - SoTA Alignment

| Source tradition | Local invariant adopted | Shortcut rejected |
| --- | --- | --- |
| ISO 21502:2020 project-management guidance and PMBOK Guide Eighth Edition (2025) | A plan is an intended-work coordination episteme: horizon, selected delivery approach or method family, baseline, dependencies, resource expectations, and acceptance targets are declared before performed work and compared with performed values after work occurs. | Treating a schedule, ticket, or baseline as evidence that the work already occurred. |
| ISO 55000:2024 asset-management practice | Asset reservations, maintenance windows, lifecycle objectives, risk, and value expectations belong in planning until performed work, actual asset change, and resource use are each established under their direct governors. | Treating planned asset availability or reserved capacity as actual asset intervention or actual resource consumption. |
| ISO 9001:2015 with Amendment 1:2024 quality-management practice | Planned quality objectives, acceptance targets, change notes, and performance evaluation stay replayable so variance can drive improvement. | Editing the plan after the fact so that quality, cost, or schedule variance disappears. |
| Case-management and adaptive-work notation practice such as OMG CMMN 1.1 | Weakly structured or ad hoc Work can still be compared with exact plan content through a local assertion, or through a direct relation when one is actually governed. | Forcing every emergency, adaptive, or consolidated Work occurrence into the original plan shape, or minting a universal fulfilment relation from one comparison. |

### A.15.2:7e - Relations

* **Builds on:** C.2.1 for episteme identity and local assertion identity; `A.15` for Role-Method-Work alignment; `A.15.1` for independently identified performed Work occurrences admitted under `U.Work`; A.2.1 for `U.RoleAssignment`; A.2.2 for capability instances, thresholds, and fit conditions; A.3.1 for `U.Method`; and A.3.2 for `U.MethodDescription`.
* **Coordinates with:** A.15.3 for planned filling against exact governed declarations; A.6.1 for operation argument and result declarations; A.6.5 for RelationSignature participant declarations; A.6.RCD for the existing-direct/local-compound/reusable-predicate/relation-kind economy; E.24/E.24.UK for any later kind admission; A.6.REL only after an admitted direct or derived relation needs occurrence discipline; A.15.4 for work-relevant appearance-based reliance repair; A.15.5 for work-entry readiness; B.1.4 for temporal aggregation; B.1.6 for performed-resource aggregation; A.10 for evidence-provenance relations; B.3 for assurance; A.20 and A.21 for gates and constraint decisions; C.32.P2S for architecturing-flow references to intended work; E.17 for publication-use questions; and F.9 only for exact cross-context `SenseCell` correspondence and admitted use.
* **Used by:** P2W carry-through when principle-to-work reasoning reaches WorkPlanning, and P2S carry-through when architecture-selected structures require intended-work epistemes. Both uses keep present plan subject, possible future performance, readiness, performed Work, actual use, evidence, gate, comparison, result, and downstream effect separately governed.

### A.15.2:8 - P2W WorkPlanning use

When `E.18.1` reaches WorkPlanning, one exact `U.WorkPlan` retains its present EntityOfConcern and states possible future performed work over an exact horizon through `PlanItem` content: intended-performance designators, planned windows, intended methods, performer and role conditions, A.2.2 capability requirements, constraints, resource budgets, dependencies, commitments, acceptance targets, evidence-reference notes, source-currentness requests, and exact planned-filling or expected-effect claims only under their direct governors.

When the P2W use also needs a readiness question, the WorkPlan may supply target PlanItems, planned preparation tasks, reservations, and planned baselines. `A.15.5` carries the `WorkEntryReadiness@Context` relation that judges full-kit condition, commitment disposition, resource readiness, WIP or flow policy, and launch-gate refs when those are current.

If the same P2W source material also claims performed work, an actual launch value or participant, evidence, gate passage, result, measurement, publication use, appearance-based reliance repair, or refresh, recover each as a separate governed object or relation. The WorkPlan claim establishes none of them.

### A.15.2:9 - Launch-value and actual-use boundary for P2W

For P2W use, `U.WorkPlan` may state intended holder and role claims, planned values, exact A.15.3 fillings, constraints, reservations, commitments, and evidence-reference notes. A gate or readiness decision may authorize entry or select values for a proposed occurrence, but neither decision nor the plan makes those values actual.

At performed-work entry, identify one exact Work occurrence as an individual admitted under `U.Work` by A.15.1. Establish each actual participant, parameter, premise, operation argument or result, resource use, affected referent, and other value only through its obtaining direct subject relation or exact A.6.1 operation-application binding. Keep the gate decision, plan claim, Work occurrence, actual-use relation, provenance, change, result episteme, production, delivery, acceptance, and downstream effect separately governed.

### A.15.2:10 - Lowering, repair, and refresh conditions

Lower a candidate `U.WorkPlan` claim when its one present EntityOfConcern, effective `U.ReferenceScheme`, horizon, at least one substantive `PlanItem`, or intended-performance designator cannot be recovered at the granularity required by the receiving planning use. Split the claim content when several existing subjects have no one jointly identified EntityOfConcern. The acceptable lowered object is a planning cue, schedule or forecast representation, method-description note, missing-source-relation note, `A.15.4` repair request, publication-use cue, readiness-gap note for A.15.5, or evidence-reference note, not a conforming WorkPlan.

When intended method, window, performer or role condition, capability requirement, resource budget, dependency, commitment, acceptance target, baseline, plan-content claim, local comparison policy, or exception policy changes, repair the exact ClaimGraph. If claim content, present EntityOfConcern, or effective reference scheme changes, let C.2.1 identify the resulting episteme and use an exact `EpistemeEditionRelation` only when its predicate obtains. A changed file, carrier, layout, publication, ticket key, or version label alone does not reidentify the plan.

Do not rewrite an independently identified Work occurrence when only the plan changes, and do not make a revised plan evidence that Work occurred. Repair an actual participant, resource use, change, result, production, delivery, acceptance, evidence, or downstream effect under its own direct pattern. When a one-case local fulfilment or variance assertion is no longer enough, use A.6.RCD disposition 3 if repeated predicate semantics are sufficient. Only when a named receiver needs distinguishable relation occurrences does kind admission open; if no truthful occurrence settlement or direct owner is available, preserve the plan, local assertions, and reusable definition and return the exact `missing-governor` blocker for that stronger use.

Refresh the selected plan edition before relying on it for cross-context coordination, budget reservation, release or gate preparation, work-entry readiness, evidence-reference use, performed-work entry, result measurement, or P2W carry-through. Recheck F.9 only when an exact `SenseCell` Bridge is current; recheck value, criterion, commitment, or verdict mappings under their direct owners. If the refreshed use claims readiness, performed work, actual participation, evidence, assurance, gate passage, result, publication use, representation, or appearance-based reliance repair, use the direct governing pattern and retain only the intended-work claims here.

### A.15.2:End

