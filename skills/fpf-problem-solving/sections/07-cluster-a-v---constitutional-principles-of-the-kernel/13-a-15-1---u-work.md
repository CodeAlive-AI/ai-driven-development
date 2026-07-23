## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` as the admitted kind when the current claim concerns one performed Work individual: a world-side dated occurrence enacted by a holder under `U.RoleAssignment`. The occurrence stands in actual `enactsMethod`, temporal, binding, resource-use, affected-referent, and containing-system relations; an assertion, description, log, or record about it is a separate `U.Episteme` and does not store fields in the occurrence. Keep model use, actual change, entity-identity inception, evaluation, evidence, delivery, acceptance, and downstream effects under their own direct patterns.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the admitted kind; one Work individual is the world-side occurrence. A separate assertion or description episteme may designate that occurrence and its obtaining relations, while surrounding records may constrain, evidence, schedule, publish, or judge it; none becomes the occurrence by being published.

**First useful object.** One independently identified world-side dated Work occurrence admitted under `U.Work`. When the receiving use needs an assertion or description, keep that object as a separate `U.Episteme`: let it designate the occurrence and state only the needed independently obtaining `performedBy -> U.RoleAssignment`, actual `enactsMethod -> U.Method`, temporal, `executedWithin`, affected-referent, direct-relation or A.6.1 binding, and resource-use relations. Add a method-description reference, model-use relation, actual-change claim, evaluation result, evidence relation, production claim, delivery, or acceptance relation only when that separately governed object is current.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover the `U.RoleAssignment`, enacted `U.Method`, temporal extent, accountable `U.System` or system in subsystem position, affected referent, concrete bindings, and used resources. Recover method-description, model-use, change, evaluation, evidence, production, delivery, or acceptance claims separately when current.
3. Decide whether the encountered record, trace, item, or display designates a Work individual admitted under `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or an `A.15.4` appearance-based reliance repair case.
4. For composite, repeated, interrupted, or overlapping occurrences, declare each work-part relation and the naming threshold. Before using totals, recover the exact `B.1.4` temporal aggregation or `B.1.6` work-resource aggregation and its policy. Do not name a work part when a temporal relation, evidence slice, telemetry segment, or missing-source-relation note is the actual object needed.
5. If the required occurrence references cannot be recovered, lower the claim to a missing-source-relation note, work-evidence note, plan note, publication-use note, declarative-representation note, or `A.15.4` repair request; do not backdate work.

**Ordinary use.** For a simple occurrence, one readable assertion naming performer assignment, enacted method, temporal extent, affected referent, and used resources is enough.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as one Work individual admitted under `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose performer assignment, enacted method, temporal extent, affected referent, bindings, and resource use remain inspectable while neighboring change, evaluation, evidence, production, delivery, and acceptance claims retain their own identities and governors.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only declaration-local `SlotFillingsPlanItem` content inside an A.15.3-governed WorkPlan, only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

### A.15.1:1 - Problem Frame

After we have separated **who is assigned** (via `U.RoleAssignment`), **what capability is being relied on** (via `U.Capability`), **how in principle** the work is done (the exact `U.Method`), and which claim-bearing episteme describes that method when current (`U.MethodDescription`), we still need a precise concept for **what happened as performed work** in real time and space.

A Work individual stands in actual performer, method, temporal, containing-system, affected-referent, binding, and resource-use relations only when those relations obtain world-side; they are not fields stored in the occurrence. A separate assertion or description may designate that individual and state the relations, but the episteme neither creates the relations nor becomes the Work occurrence.

### A.15.1:2 - Problem (what breaks without a clean notion of Work)

1. **Plan and occurrence confusion.** Schedules and diagrams get mistaken for performed work, so audits and KPIs attach to plans or representations instead of dated occurrences.
2. **Method-description and work conflation.** A method description, code artifact, or SOP is reported as if it were performed work; conversely, logs are treated as recipes.
3. **Who and when leakage.** People and calendars are baked into method descriptions; reuse and staffing agility collapse.
4. **Resource dishonesty.** Energy, money, and tool wear are represented as fields or booked to methods or roles instead of being stated through separately obtaining resource-use relations involving exact Work individuals; costing and sustainability measures drift.
5. **Mereology muddle.** Teams hand-wave over work parts, retries, overlaps, or long-running episodes; roll-ups double-count or miss work.

### A.15.1:3 - Forces (what the definition must balance)

| Force                              | Tension we resolve                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail** | One Work notion for surgery, welding, ETL, proofs, lab cycles—while letting each keep its vocabulary. |
| **Granularity vs. aggregation**    | Selected-grain occurrences vs. composite Work; we need roll-up without presuming partlessness or letting Work parthood create another object's composition. |
| **Concurrency vs. order**          | Parallel or overlapped activities need clear part and overlap semantics.                              |
| **Identity vs. retries**           | A failed attempt, a retry, and a resumed episode—what is “the same” work?                             |
| **Time realism vs. simplicity**    | We need intervals and coverage but cannot bury users in temporal logic notation.                      |

### A.15.1:4 - Solution — admit accountable dated Work occurrences under `U.Work`

#### A.15.1:4.1 - Definition and occurrence identity

`U.Work` is the admitted U-kind for dated 4D occurrence holons. One Work individual is one independently identified world-side dated performed occurrence with its own governed temporal extent. Exact `performedBy` relations connect that Work individual to one or more obtaining `U.RoleAssignment` occurrences; each assignment's holder `U.System` is a performer in that attribution. An exact `enactsMethod` relation connects the Work individual to an exact `U.Method`. Exact containing-system, affected-referent, direct subject-relation or A.6.1 binding, and performed resource-use relations are recovered independently when current. An occurrence designator permits reference but does not identify work by label, ticket, trace, record, or storage convention; an assertion or description about the occurrence is a separate `U.Episteme`.

The actual `enactsMethod` relation obtains between the Work occurrence and the exact `U.Method`; it is not a field of either participant. An exact `U.MethodDescription` may be cited when its claims identify, constrain, or justify that method for the receiving use; the description is not enacted and its fields do not become actual work bindings. A selected model-use structure likewise enters only through the exact receiving relation whose interpretation it changes.

When actual change is current, identify one exact `U.Transformation` independently under A.3.4 and recover the exact work-to-change facts under their direct subject governor or the accepted A.15.PROD/A.6.RCD route. A morphism, delta expression, state-plane trace, pre-state, or post-state may represent or support that neighboring change claim; none is a mandatory field of a Work occurrence or a work-identity discriminator by form.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core occurrence references and neighboring links

When a separate assertion or description episteme describes one Work occurrence, recover the following content at the granularity required by the current use. Each item names an occurrence designator, a world-side relation or temporal fact, or a reference to another episteme; the list is not a slot or field schema for the Work individual:

1. **Occurrence and extent** — one occurrence designator plus exact start and end, or an explicitly open end for in-flight work; add location only when the work claim depends on it.
2. **Performer** — each actual `performedBy` relation points to an exact `U.RoleAssignment`; every such assignment has its own holder system, role value, role-taxonomy episteme, effective reference scheme, obtaining condition, and extent under A.2.1.
3. **Enacted method** — actual `enactsMethod -> U.Method`. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on the exact description edition; the description is not enacted.
4. **Containing system** — `executedWithin -> U.System`; if ordinary speech says subsystem, name that `U.System` and its exact part relation to the larger holon.
5. **Affected referent** — the exact subject, asset, product, patient, learner, dataset, document, or other referent with respect to which this occurrence is performed. This work-scope fact does not by itself assert change, production, delivery, or acceptance.
6. **Actual participation and bindings** — each participant, parameter, supplied constituent, premise, reference use, operation argument, or operation result only through an obtaining direct subject relation or exact A.6.1 operation-application binding. A MethodDescription field, plan row, type-compatible value, or log token establishes none of them.
7. **Performed resource use** — exact energy, material, machine-time, money, tool-wear, or other resource-use facts at the boundary needed by costing or sustainability use.
8. **Continuity and identity policy** — `workContinuityPolicyRef` to the exact C.2.1 episteme whose claims state the tolerances, interruption boundaries, and reidentification rule used to resolve descriptions or records to this occurrence. It is not necessarily a `U.MethodDescription` and does not become a work part.
9. **Work mereology and temporal relations** — exact parent, part, predecessor, successor, overlap, retry, or resumption relations only when their predicates obtain.
10. **Actual change and production claims** — exact A.3.4 transformations, direct work-to-change facts, and only the current A.15.PROD production-work, entity-identity-inception, or production-completion claim. None follows from work identity or parthood.
11. **Evaluation and downstream claims** — characteristic value, measurement result, comparison result, evaluation-result episteme, acceptance verdict, delivery, transfer, and downstream effect remain different objects under their direct patterns.
12. **Evidence, publication, and model use** — cite only the exact evidence-use, publication-use, currentness, claim-scope, reference-plane, bridge, or selected model-use relation needed by the receiving claim.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| A claim-bearing episteme expressed through a **recipe, code artifact, or diagram** and substantively about one admitted exact method | **`U.MethodDescription`** | Does the same episteme meet A.3.2's exact membership threshold? Otherwise keep the representation, publication, formal substrate, or other direct owner. |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | One Work individual admitted under **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer, enactment, bindings, affected referent, and resource-use facts? |
| The **actual state change associated with this occurrence** | **`U.Transformation` plus exact work-to-change facts** | Is the change independently grounded under A.3.4, and does a separately governed relation connect it to this work? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A publication about one Work occurrence projects an already declared assertion or description episteme; it does not create the world-side occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, publication face, or carrier count as performed work.

Preparation is classifiable as one Work individual under `U.Work` only after it actually occurs and the exact `performedBy`, `enactsMethod`, temporal, affected-referent, binding, and resource-use relations required by A.15.1 obtain independently. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, performer assignment, enacted method, concrete bindings, resource-use claims, and affected referent. Project a change, evaluation-result, evidence, production, delivery, or acceptance reference only as a separately governed neighboring claim. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the Work occurrence as the dated performed individual admitted under `U.Work`; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize a surrogate Work occurrence; a publication may cite only Work individuals that meet the occurrence basis in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the Work occurrence.

A planned, gate-selected, or launch-labelled value becomes actual only when an obtaining direct subject relation or exact A.6.1 operation-application binding makes it participate in the occurrence. Do not back-fill a plan or infer an actual binding from shared wording. Pre-state and post-state references remain with an independently governed transformation or comparison claim; they do not bind to the Work occurrence merely because their times bracket it.

#### A.15.1:4.6 - Route neighboring participant, change, and production claims

| Current claim | Direct route from exact Work | Non-inference |
| --- | --- | --- |
| actual participant in a direct subject relation | cite the independently identified obtaining relation occurrence and its exact participant | work scope, plan content, or type compatibility does not establish participation |
| actual operation argument or result | cite the exact A.6.1 application and operation-application binding | a MethodDescription field or A.15.3 planned filling is not an actual binding |
| actual changed referent | cite the independently identified A.3.4 transformation and exact work-to-change fact | temporal overlap, a delta expression, or common referent does not establish the link |
| production-work participation | use the A.15.PROD whole-work or exact proper-work-part branch | work, work parthood, or an intended method effect does not make the occurrence production work |
| entity-identity inception or production completion | cite the exact A.15.PROD local claim with its specification or criterion edition and boundary | neither claim follows from work completion, result wording, delivery, or acceptance |
| evaluation, result episteme, delivery, acceptance, or downstream effect | cite its exact direct governor and relation to the work or subject when current | none is an intrinsic Work field or identity discriminator |

### A.15.1:5 - Work mereology (how occurrences form holarchies)

Work identity is occurrence-grounded and 4D, but temporal extent alone is not sufficient. Resolve one occurrence under its exact `workContinuityPolicyRef` using performer assignment, actual enacted method, extent, affected referent, containing system, actual bindings, resource-use facts, and the tolerances current to that policy. MethodDescription, plan, log, publication, or trace identity does not replace this rule.

#### A.15.1:5.1 - Parts and wholes of Work (occurrence facts)

* **Temporal-part (`TemporalPartOf_work`).** A proper **time-slice relation** over one selected Work occurrence or work phase. The selected part is grounded by parent work identity plus interval and, when needed, a named aspect such as resource use, telemetry, SLA coverage, or interval-local evidence. A temporal part is useful for monitoring, utilization, lead time, and interval-local evidence. It has no independent method-switch identity by that fact.
* **Episode-part (`EpisodeOf_work`).** A **policy-governed, event-bounded, maximally continuous enactment fragment** of one parent Work occurrence. It starts at a work-entry, resumption, mode-switch, or switch-to-method event and ends at interruption, switch-away, completion, or a policy-declared pause. It is not an arbitrary time slice. It remains under the parent work identity only when exact `workContinuityPolicyRef` says that the interrupted or resumed activity is still the same Work occurrence; `WorkEpisode` is not introduced as a second kind or relation name.
`workContinuityPolicyRef` designates the exact C.2.1 episteme whose claims state the episode boundaries, tolerated variation, and work-continuity rule used for this occurrence. Interpret those claims under that episteme's effective `U.ReferenceScheme`; name any current `U.ClaimScope`, temporal qualification window, or model-use structure separately. The policy episteme governs the identity judgment without becoming a MethodDescription, context container, or work part.

* **Operational-part (`OperationalPartOf_work`).** A **work-part occurrence** that may enact a factor of a recovered `U.Method`, for example, an incision occurrence within an appendectomy occurrence, possibly **overlapping** with others in time. If a method-description reference is current, it identifies, describes, constrains, or evidences that method factor; the referenced `U.MethodDescription` is not enacted. If no `U.Method` factor is recovered, govern the material as a work part, evidence segment, telemetry segment, mechanism material, system-component behavior, or missing-source-relation note under the direct pattern.
* **Concurrent work parts (derived use-side reading; no fourth parthood relation).** First state each exact work-part relation to the same parent and then state the independently governed interval `overlaps` fact. When coordination is current, state its exact direct relation separately. Shared parentage and overlap do not by themselves establish coordination, and `ConcurrentPartOf_work` is not introduced as a primitive work-part relation.

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
* **`retryOf`** — a new Work occurrence re-attempting the same intended objective or enacted Method after the prior occurrence has ended under the exact work-continuity policy; revised bindings remain separately governed actual facts.
* **`resumptionOf`** — an episode or later occurrence that **continues** after interruption; policy decides whether it is under the same parent Work-occurrence identity or a separate Work occurrence linked to the earlier occurrence.

These relations are **occurrence facts**, not method-design assumptions.

#### A.15.1:5.3 - Work-occurrence relations used by Part B roll-ups

`A.15.1` supplies the identity of each independently identified Work occurrence or Work part and makes its exact temporal and performed resource-use relations recoverable. It does not itself return a temporal aggregate or resource ledger.

* **Temporal coverage.** When a receiving use needs utilization, elapsed time, phase coverage, or another roll-up over Work intervals, open `B.1.4`. Its recovered `ContextTemporalAggregation@Context`, coverage and non-overlap conditions, aggregation policy, and optional `Gamma_time` notation govern union, hull, or another admitted temporal aggregate. The work intervals remain A.15.1 facts.
* **Resource aggregation.** When a receiving use needs a total over materials, energy, time, money, tool wear, or another performed resource value, open `B.1.6`. Its recovered `WorkResourceAggregation@Context`, typed resource-accounting basis, evidence refs, overlap or deduplication policy, ledger, aggregation rule, and optional `Gamma_work` notation govern the aggregate. Each contributing performed resource-use relation obtains separately with its exact Work occurrence as a participant; any ledger or assertion about that relation is a separate episteme.

**Manager's tip:** cite the exact `B.1.4` or `B.1.6` aggregation result and policy beside the KPI. A Work-part list, shared parent, or operator spelling supplies neither the aggregate nor its policy.

#### A.15.1:5.4 - Identity and reidentification of Work

Two descriptions, assertions, records, or traces resolve to the same Work occurrence only when they designate one occurrence under the exact `workContinuityPolicyRef` and its declared tolerances. Check at least:

* compatible spatiotemporal extent at the selected resolution;
* the same exact set of performer `U.RoleAssignment` values current at the selected identity grain;
* the same actual enacted `U.Method`, or a policy-admitted method switch within one occurrence;
* the same containing `U.System` and affected referent at the identity grain;
* compatible actual direct-relation and A.6.1 bindings, with every admitted change named by policy; and
* compatible resource-use and work-part facts where the policy makes them identity-bearing.

An occurrence designator, label, ticket, record, MethodDescription edition, WorkPlan, publication, evidence set, or model-use structure may help resolve the occurrence but does not decide identity. A changed description edition alone does not reidentify work when the enacted method and occurrence facts remain the same. A changed performer assignment, enacted method, extent, affected referent, containing system, actual binding, or continuity outcome identifies another occurrence unless the exact policy admits the variation inside one bounded Work.

#### A.15.1:5.5 - Interruptions, retries, resumptions, and description changes

* **Retry:** identify a new Work occurrence admitted under `U.Work`, with its own extent and actual bindings; link it through `retryOf` only when that relation's policy holds.
* **Episode under the same parent work:** retain event-bounded fragments inside one Work occurrence only when `workContinuityPolicyRef` admits the interruption, resumption, mode switch, or policy pause.
* **Separate occurrence after interruption or actual change:** identify another Work occurrence when the policy treats interruption, retune, rework, retry, changed actual binding, changed affected referent, switch-away, restart, or method switch as crossing the work boundary. Link occurrences only through an exact obtaining `retryOf`, `resumptionOf`, `precedes`, `overlaps`, `contains`, or other declared relation.
* **MethodDescription change:** record the selected description edition separately. A changed description edition neither splits nor preserves Work by itself; apply the continuity policy to the actual enacted method and occurrence facts.
* **Rework:** identify new work after failed earlier work unless the exact policy admits it as an episode or operational part of the same parent occurrence. Keep any causal attribution with the governing causal-use pattern.

Plans, costs, quality statistics, telemetry evidence, and method-reliance claims depend on whether the selected interval is a temporal part, event-bounded episode, operational part, or new occurrence. Name the exact policy episteme, effective reference scheme, and any current scope or temporal qualification before relying on that distinction.

#### A.15.1:5.6 - Work mereology does not compose effects or transformations

A parent Work can have exact work parts without having one composite effect or composite transformation. Any temporal aggregate uses `B.1.4`; any performed-resource aggregate uses `B.1.6`; each names its own aggregation concern, policy, and evidence. Identify every actual transformation independently under A.3.4 and every work-to-change fact under its direct governor.

Work parthood, method parthood, temporal inclusion, a common affected referent, a list of changed characteristics, or adjacent plan items establishes neither transformation parthood nor a composite transformation. If a receiving production or effect claim requires transformation composition and no accepted governor supplies it, retain the exact Work and independently identified transformations and return the missing-governor blocker. A.15.PROD may still recover any independent production-work, entity-inception, or completion claim that does not depend on that missing composition.

### A.15.1:6 - Archetypal grounding (parallel domains)

Each case below is presented as readable content of a separate assertion or description episteme. Arrow notation abbreviates independently obtaining world-side relations involving the named Work individual; `methodDescriptionRef` and continuity-policy references cite separate epistemes. The bullet layout declares no slots or fields on the Work individual.

#### A.15.1:6.1 - Surgical case (overlap and episodes)

* **Top work occurrence:** `Appendectomy_Case_2025-08-10T0905_1142`.
* **Actual method and containing system:** `enactsMethod -> Appendectomy@Hospital-2025`; `executedWithin -> SurgicalService_A`.
* **Affected referent and performed resources:** an exact affected-referent relation connects the occurrence to `Patient_8472`; separately obtaining resource-use relations connect it to actual use of operating theatre `OR_7`, consumables pack `AppendectomyKit_8472`, and assigned staff time during the occurrence. No result, change, delivery, or acceptance follows from those relations.
* **`methodDescriptionRef`:** `Appendectomy_v5`.
* **Performer:** `U.RoleAssignment` with holder system `OR_Team_A`, role value `SurgicalTeamRole`, role-taxonomy episteme `HospitalRoles-2025`, and effective reference scheme `Hospital-Operating-Scheme-2025`; the assignment occurrence covers the surgery interval.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02-10:07 -> **resumptionOf** same occurrence (per hospital policy).
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses union for OR utilization and hull for patient lead time under separately declared policies.
* **B.1.6 resource roll-up:** a recovered `WorkResourceAggregation@Context` totals consumables and staff time once under its typed resource basis and overlap policy; every contributing resource-use relation continues to obtain independently with the exact Work occurrence as a participant.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing system:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `executedWithin -> DataPlatform_Prod`.
* **Affected referent, actual participation, and performed resources:** `WarehouseOrders_2025-08-11` is the affected dataset. The obtaining source-dataset participation of `RawOrders_2025-08-11` and destination-dataset participation of `WarehouseOrders_2025-08-11`, under their exact project data-use relations, are the actual-use facts on which this case relies. Actual cluster machine-time on `ETL_Cluster_3` and storage use on `WarehouseStore_1` are performed resource-use facts. None supplies a generic input/output binding or an automatic dataset-transformation claim.
* **`methodDescriptionRef`:** `ETL_v12.bpmn`.
* **Performer:** `U.RoleAssignment` with holder system `ETL_Runtime`, role value `TransformerRole`, role-taxonomy episteme `DataOpsRoles-2025`, and effective reference scheme `DataOps-Execution-Scheme-2025`; the assignment occurrence covers the ETL interval.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses hull for SLA and union for cluster utilization under separately declared policies.
* **B.1.6 resource roll-up:** a recovered resource aggregation sums compute minutes under its declared overlap policy; source-dataset participation, destination-dataset participation, storage use, returned values, and downstream result claims stay under their exact direct relations rather than one input-output family.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Actual method and containing system:** `enactsMethod -> Carnot_Cycle_Operation@ThermoLab`; `executedWithin -> LabRig_7`.
* **Affected referent and performed resources:** `WorkingFluidCharge_7`; actual electrical-energy use attributed to the run through `HeaterBank_7` and `Chiller_7` during 13:00-13:06. Any thermodynamic energy-exchange or transformation claim remains separately governed.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer:** `U.RoleAssignment` with holder system `LabRig_7`, role value `TransformerRole`, role-taxonomy episteme `ThermoLabRoles-v2`, and effective reference scheme `ThermoLab-Experiment-Scheme`; the assignment occurrence covers the laboratory-work interval.
* **Work identity:** a separate identity assertion under exact `workContinuityPolicyRef` designates the occurrence and cites the independently obtaining performer-assignment, enacted-method, temporal, containing-system, affected-referent, binding, and performed resource-use relations needed by that policy. The thermodynamic state-plane trace separately describes or evidences actual change; it is not a work-identity field, work-control relation, or ordered instruction sequence.
* **Part B roll-ups:** B.1.4 may use the exact run interval in a temporal aggregation; B.1.6 may aggregate the performed energy-use facts under a typed resource basis and selected overlap policy. Any thermodynamic energy-exchange or transformation claim keeps its direct governor; no "steps" are required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing system:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `executedWithin -> ClaimsOperations_A`.
* **Affected referent and performed resources:** `Claim_8142`; actual handler time during 09:00-09:42 and 10:11-10:38, plus actual case-system time on `ClaimsPlatform_A` during those episodes. The callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer:** `U.RoleAssignment` with holder system `ClaimsTeam_A`, role value `ClaimsHandlerRole`, role-taxonomy episteme `InsuranceOpsRoles-2026`, and effective reference scheme `Claims-Handling-Scheme-2026`; the assignment occurrence covers the claims-work interval.
* **Episode policy:** a customer callback interruption under one hour keeps the same parent work identity and creates two `EpisodeOf_work` fragments: `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38`.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **Actual method and containing system:** `enactsMethod -> FourStrokeEngineOperation@TestBench-2026`; `executedWithin -> Engine_Cell7`.
* **Affected referent and performed resources:** `EngineUnderTest_7`; actual fuel use from `FuelBatch_F7` and ignition-electrical-energy use during 13:00-13:30. Any thermodynamic change, result, or evidence claim remains separately governed.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer:** `U.RoleAssignment` with holder system `Engine_Cell7`, role value `EngineOperationRole`, role-taxonomy episteme `EngineCellRoles-2026`, and effective reference scheme `TestBench-Operating-Scheme-2026`; the assignment occurrence covers the engine-run interval.
* **Episodes:** start, stop, mode-change, fuel/ignition policy, or diagnosis policy may bound `EpisodeOf_work` fragments. The definition uses boundary events and policy, not a human-attention metaphor.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **Actual method and containing system:** `enactsMethod -> EnvelopeDetection@RadioLab-2026`; `executedWithin -> Receiver_Rx42`.
* **Affected referent and performed resources:** `RF_TestSignal_42_2115`; actual receiver-channel time on `Rx42_Channel_1` and electrical-energy use during 21:15-21:20. Waveform and telemetry traces remain separately governed representations or evidence.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer:** `U.RoleAssignment` with holder system `Receiver_Rx42`, role value `DetectorReceiverRole`, role-taxonomy episteme `RadioLabRoles-2026`, and effective reference scheme `RadioLab-Reception-Scheme-2026`; the assignment occurrence covers the reception interval.
* **Episodes:** a continuous reception interval between retune, on/off, interruption, or declared diagnostic mode events is `EpisodeOf_work` only under the receiver's episode policy.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15-10:22. Exact `performedBy(Pump37_RecognitionWork_2026-07-20T1015_1022, Pump37_EvaluatorAssignment_2026-07-20)` obtains. That `U.RoleAssignment` has holder system `RecognitionEvaluator_A`, role value `HolonRecognitionEvaluatorRole`, role-taxonomy episteme `FPFRoles-2026`, effective reference scheme `FPF-Recognition-Scheme-2026`, and an assignment extent covering the work. Exact `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)` and `executedWithin(Pump37_RecognitionWork_2026-07-20T1015_1022, FPF_Recognition_Service_A)` obtain, and the governed affected-referent fact concerns `Pump_37`. A separate assertion about the Work occurrence cites exact A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017`, whose `candidateArgument` binding designates `Pump_37` and whose `judgmentResult` binding returns `unknown`. Separately obtaining resource-use relations ground seven minutes of evaluator time and the application compute time on `RecognitionRunner_A`.

The returned `unknown` value remains the A.6.1 result binding. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1. None is the Work occurrence or an intrinsic Work result field.

### A.15.1:6.8 - Bias-Annotation

| Bias | How A.15.1 prevents it |
| --- | --- |
| Plan-as-work bias | `U.WorkPlan`, schedules, method descriptions, and intended parameter bindings stay separate from the dated occurrence. |
| Log-as-work bias | Telemetry, dashboards, provenance rows, and work publications can evidence or describe a work occurrence; they do not become the occurrence. |
| Method-as-occurrence bias | `U.Method` and `U.MethodDescription` identify or describe the way of doing; an independently grounded assertion that one Work individual is admitted under `U.Work` designates the dated performed occurrence. |
| Evidence-as-authority bias | Evidence, assurance, gate, release, and causal-use claims keep their governing patterns and do not follow from a work record by appearance. |
| Record-handling-as-transformation bias | Copying, formatting, evaluating, or publishing records can be grounded as Work occurrences admitted under `U.Work` without an automatic change claim. Any claimed record or dataset transformation still needs independent A.3.4 identity and exact work-to-change facts. |

### A.15.1:7 - Scope Declaration and Rationale

* **Applicability:** Use the same occurrence test for pragmatic costing, architectural accountability, teaching examples, and source or evidence questions; when the current claim is only about a description, publication, source, or evidence relation, apply the governing pattern for that claim.
* **Scope declaration:** The occurrence head is universal. Temporal semantics use the declared temporal reference; episode identity uses `workContinuityPolicyRef` and its effective `U.ReferenceScheme`; claim scope, qualification windows, model-use structure, evidence, and source currentness remain separate when current.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with exact `U.RoleAssignment` and actual `enactsMethod` relations, so that costing, quality, and audit rest on independently identified work occurrences rather than plans, recipes, or a generic role-enactment fact.

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is the admitted kind for dated performed Work occurrences. Each Work individual is world-side; it is not a `U.Method` (semantic way), `U.MethodDescription` (description), `U.Role` or `U.RoleAssignment` (assignment), `U.WorkPlan` (plan or schedule), or assertion, record, log, or publication about work.

**CC-A15.1-2 (Required occurrence basis).**
A conforming assertion or description about a Work individual designates one world-side occurrence admitted under `U.Work` and makes every exact `performedBy -> U.RoleAssignment`, actual `enactsMethod -> U.Method`, temporal extent, `executedWithin -> U.System`, affected referent, every current direct-relation or A.6.1 binding, and performed resource-use fact recoverable. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on that exact description edition. The episteme designates these independently obtaining relations; it does not turn them into occurrence fields.
**CC-A15.1-3 (Time window).**
A conforming assertion or description about one Work occurrence designates a world-side individual with a closed temporal extent `[t_start, t_end]`, or an explicitly open end while the occurrence is in flight. The episteme states or designates that extent and, where relevant, location or asset; neither an interval field nor the presence of the record creates the occurrence.

**CC-A15.1-4 (Interpretation and policy basis).**
A load-bearing work claim names `workContinuityPolicyRef`, its effective `U.ReferenceScheme`, and any exact method-description edition, claim scope, qualification window, aggregation-policy episteme, or selected model-use structure on which the judgment actually depends. Acceptance criteria, evaluation work, result epistemes, and evidence uses remain neighboring claims rather than work-identity fields.

If two local senses must be related, F.9 receives the exact sense endpoints and the claimed direction and loss. A different reference scheme, role assignment, description edition, or model-use structure alone does not establish a Bridge.
**CC-A15.1-4b (No mandatory state-plane or delta).**
A Work claim needs no `StatePlaneRef`, pre-state, post-state, or delta merely to establish occurrence identity. When actual change is current, A.3.4 identifies the transformation and its state or boundary facts; a separate work-to-change claim connects it to Work.
**CC-A15.1-5 (RoleAssignment interval coverage).**
Every `U.RoleAssignment` cited by an obtaining `performedBy` relation covers the work interval or the exact performed part attributed to it. If one does not, keep the work occurrence and that assignment claim separate: repair or reject the attribution, or establish a retroactive assignment only under the exact A.2.1 rule that admits it.

**CC-A15.1-6 (Actual participant and operation binding).**
Every actual parameter, participant, premise, constituent, operation argument, or operation result used by the work is established through an obtaining direct subject relation or exact A.6.1 application binding. A MethodDescription declaration, default, A.15.3 planned filling, gate selection, compatible ValueKind, or stored token establishes no actual binding.
**CC-A15.1-7 (Capability check).**
Any capability threshold relied on for a Work occurrence is recovered under A.2.2 or the exact direct capability-fit or evaluation owner. A `U.Method` or `U.MethodDescription` may cite or describe that threshold but does not create the capability fact. Check the threshold against each relevant holder in `performedBy` for the performed-work interval or declared checkpoints; state a violation through its separately governed evaluation-result episteme or direct characteristic/evaluation relation, never as an intrinsic work outcome.

**CC-A15.1-8 (Acceptance criteria).**
An acceptance claim names the exact criterion or comparator specification, its edition, applicable scope and window, the evaluation or acceptance work that applied it, and the direct result relation. Success class, quality measurement, comparison result, and acceptance verdict remain distinct; no verdict is an intrinsic field of the Work occurrence or a condition of `U.Work` membership.
**CC-A15.1-9 (Resource honesty).**
Performed resource-use facts (energy, materials, machine-time, money, tool wear) are attributed through exact obtaining relations to particular Work individuals admitted under `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans. Any aggregate ledger, unit conversion, allocation, or overlap and deduplication result belongs to `B.1.6` and cites the contributing Work occurrences and resource-use facts.

**CC-A15.1-10 (Mereology declared).**
When exact work-part relations obtain among Work individuals, declare each relation: temporal-part, episode-part, operational-part, or another relation with its own predicate. Ambiguous mixtures lower aggregation and identity claims. A `TemporalPartOf_work` claim names parent work identity plus interval or aspect; an `EpisodeOf_work` claim names the event-bounded continuity policy; an `OperationalPartOf_work` claim names the occurrence-side part and any recovered method factor separately. Concurrency adds a separate interval `overlaps` fact and, when current, a separately governed coordination claim; it is not a fourth work-part relation.

**CC-A15.1-11 (Temporal coverage selection).**
For a temporal roll-up, `B.1.4` names the exact Work refs, aggregation concern, time window, coverage and non-overlap conditions, and policy selecting union, convex hull, or another admitted result. A.15.1 supplies the occurrence intervals but does not own the aggregate.

**CC-A15.1-12 (Resource aggregation).**
For a resource roll-up, `B.1.6` names the exact Work refs, typed resource basis, units, evidence, delimitation and time window, overlap or deduplication policy, ledger, and aggregation rule. A.15.1 supplies performed resource-use facts but does not own the aggregate ledger.

**CC-A15.1-13 (Identity and retries).**
A retry is a new Work occurrence admitted under `U.Work` and linked via `retryOf` only when that relation obtains. An interruption remains inside the same occurrence only when exact `workContinuityPolicyRef` admits an episode; otherwise the later enactment is another occurrence. Changed actual method, affected referent, participant binding, performer assignment, containing system, or temporal extent is tested by that policy. A changed MethodDescription edition alone is a neighboring description-selection change.
**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-locality evaluation).**
A work occurrence keeps one identity when several receiving uses evaluate it. Each use names its own effective reference scheme, claim scope, criterion, qualification window, evaluation work, and result episteme. Use F.9 only when an exact Bridge between local senses is actually needed; a shared work name or record carries no acceptance across uses.
**CC-A15.1-16 (Method-description changes do not decide Work identity).**
If a selected MethodDescription edition changes during the occurrence, state the description-selection or override claim separately. Split the Work occurrence only when `workContinuityPolicyRef` says that the corresponding actual enacted-method, binding, performer, affected-referent, or extent change crosses the occurrence boundary.
**CC-A15.1-17 (Distributed performers).**
If multiple `U.RoleAssignment` values jointly perform the same top-level work occurrence, name every obtaining `performedBy` relation and verify each assignment's coverage. If the use instead needs a parent work with child occurrences, give every child its exact performer assignment and work-part relation. A lead, accountability, or coordination claim remains separate and cannot substitute one designated assignment for the actual performer set.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry support a claim about work only through an exact evidence-use relation that identifies the work occurrence, method-description edition when current, performer assignment, temporal extent, affected referent, and the policy or qualification values on which the receiving claim relies.

**CC-A15.1-19 (Affected referent and work scope).**
Each assertion or description about a Work occurrence designates the exact Work individual and states the direct work-to-referent relation needed by the receiving use. That relation must obtain independently; naming the referent in the episteme establishes neither actual change, production, delivery, acceptance, nor a universal `affected` relation.
**CC-A15.1-20 (Actual change stays neighboring).**
When the receiving claim needs actual change, identify an exact `U.Transformation` under A.3.4 and the exact work-to-change facts. Work can occur without a current transformation claim, and a no-op, evaluation, inspection, communication, or record-handling occurrence is not forced into a delta schema.
**CC-A15.1-21 (Record handling remains Work without automatic transformation).**
Copying, formatting, evaluating, or publishing records can be performed by Work individuals admitted under `U.Work` when performer assignment, actual enacted method, extent, containing system, affected referent, exact bindings, and resource-use facts are grounded. Identify any actual record or dataset transformation separately under A.3.4; a label, output record, or post-state picture does not establish it.
**CC-A15.1-22 (Executed-within declaration).**
Each Work occurrence stands in one exact `executedWithin -> U.System` relation, which an assertion or description about the occurrence may state. When the accountable system is a subsystem in ordinary speech, name the system and its exact part relation to the larger holon. When that system differs from the affected referent, keep both identities and any current direct work-to-subject or work-to-change relation explicit.

**CC-A15.1-23 (No transformation composition from Work mereology).**
Exact Work parts support only their declared work-part facts and provide inputs to separately recovered `B.1.4` or `B.1.6` aggregation claims. They establish neither component transformations, transformation parthood, a composite transformation, nor a parent effect. Recover each actual transformation independently and return the exact missing-governor blocker when a current claim requires unavailable transformation composition.
**CC-A15.1-24 (No new claims on publication views).**
MVPK views about Work project the declared assertion or description of the Work occurrence; they do not add properties or claims. Numeric or comparable content names unit, scale, reference-plane, and `EditionId` pins; work-publication views do not use "signature" for these publication pins.

**CC-A15.1-25 (No Gamma leakage).**
Publication views cite exact `B.1.4` temporal-aggregation or `B.1.6` work-resource-aggregation results and policies when showing aggregates. They do not encode aggregation semantics in prose or imply defaults. Optional Gamma notation lives with its recovered Part B aggregation claim; the view carries only pinned references needed by the publication use.

**CC-A15.1-26 (No input-output re-listing).**
Publication views do not restate method-description input and output lists; they publish presence pins and source references only under the publication-use pattern governing that view.

**CC-A15.1-27 (Comparator ordering and return sets).**
Across-occurrence comparison presented on a publication view about Work uses a declared `ComparatorSet` (map-then-compare), returns sets when order is partial, and lowers hidden scalarization or ordinal-mean claims.

**CC-A15.1-28 (Comparator and transport pins).**
Numeric or comparable acceptance or KPI claims on a publication view about Work pin `ComparatorSet.edition`, comparator-spec edition, and, where conversions occur, `TransportRegistry.edition` with the selected transport policy ids. Bridge ids carry cross-context or cross-plane reuse; penalties affect the reliability relation only.

**CC-A15.1-29 (Telemetry-reference pins, when applicable).**
If a work occurrence feeds G.11 or QD and OEE portfolios, the evidence relation cites the telemetry, archive, and policy references declared by the governing comparison, archive, evidence, or refresh pattern. Illumination remains report-only telemetry unless a governing comparison, archive, or selection pattern promotes that use.

**CC-A15.1-30 (Part naming parsimony).**
Do not create a durable named work part for every interval, telemetry segment, pause, event-log row, engine stroke label, detector component, or encountered wording. Name a work part only when downstream use needs its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or another direct neighboring object.

**CC-A15.1-31 (Method and work granularity are coupled but not isomorphic).**
A work part may enact a recovered submethod, but the correspondence is not automatic. A temporal work part usually enacts the same whole method during a slice. An episode records continuity under one method or mode and may span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational work part corresponds to a method factor only when that factor is recovered as `U.Method` under `A.3.1` and `B.1.5`; otherwise govern the material as a work part, method-description node, evidence segment, mechanism material, or system-component behavior under the direct pattern.

### A.15.1:9 - Work-to-aggregation interface

`A.15.1` makes the occurrence-side inputs recoverable without storing them in the occurrence: a separate assertion or description episteme designates exact Work individuals or work parts and states their temporal extents and the separately obtaining resource-use relations selected for aggregation. Aggregation remains a neighboring claim with its own EntityOfConcern and direct owner.

#### A.15.1:9.1 - Temporal aggregation return

For utilization, lead time, cycle time, phase coverage, or another temporal roll-up, use `B.1.4`. Name the exact work refs, carrier or aggregation concern, time window, coverage and non-overlap conditions, aggregation policy, and admissible use there. Union, convex hull, and optional `Gamma_time` notation are properties of that recovered temporal aggregation, not fields or identity invariants of a Work occurrence.

When the exact `B.1.4` result selects the Work-interval profile, retain these use-specific choices:

* **Union of intervals** for utilization or availability: preserve every covered instant and do not count overlap twice.
* **Convex hull** `[min t_start, max t_end]` for lead time or cycle time: preserve elapsed span from first start to last end, including gaps.
* **Declared algebraic behavior:** for either exact set-based policy, duplicate input is idempotent, input order is irrelevant, and adding intervals cannot shrink the union or hull. If another policy lacks those properties, name it rather than borrowing the union/hull result.

Never switch union and hull silently between KPIs. The formulas above profile a recovered B.1.4 aggregation over Work intervals; they do not make A.15.1 the temporal-aggregation owner.

#### A.15.1:9.2 - Resource aggregation return

For a total or ledger over performed resource-use facts, use `B.1.6`. Name the exact work refs, typed resource-accounting basis, units, measurement or evidence refs, holon delimitation, time window, overlap or deduplication policy, aggregation rule, and admissible use there. Additivity, allocation, traceability, the aggregate ledger, and optional `Gamma_work` notation belong to that recovered resource-aggregation claim, not to Work-occurrence identity.

When an exact `B.1.6` aggregation must allocate shared or overlapping resource use, retain these non-default policy examples:

* **Parent attribution:** book a declared shared fixed value once at the parent and independently measured variable values at children.
* **Pro rata by wall time:** divide a declared shared value by relative durations only when that driver is admissible for the resource basis.
* **Driver based:** allocate by an exact measured or governed driver such as CPU share, weight, or priority.

Whichever policy is selected, add only disjoint or explicitly deduplicated values and keep every aggregate figure traceable to its contributing Work refs and evidence. A policy label alone establishes neither allocation nor ledger value.

A Work publication or KPI may cite either result under its publication-use governor. It may not recreate an unselected operator, infer an aggregate from parthood, or turn an aggregation record into a Work occurrence.

### A.15.1:10 - Work-claim interpretation checks

When another decision relies on a work occurrence, perform three quick checks:

1. **Method-description interpretation.** Does `methodDescriptionRef`, when current, resolve to the exact `U.MethodDescription` edition under the effective `U.ReferenceScheme` used by the receiving claim? If not, repair the reference or relate the exact local senses through F.9 when a real cross-locality claim is current.
2. **Role-assignment coverage.** Does every obtaining `performedBy` relation resolve to an exact `U.RoleAssignment` whose interval covers the occurrence or exact performed part attributed to it? If not, keep the work and defective attribution claim separate until A.2.1 admits or repairs that assignment.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the current criterion edition to the exact independently obtaining relations involving the Work occurrence, changed subject, measurement results, or delivered entity required by that criterion? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separately governed.

These checks recover exact governing objects. They neither create one judgment-context object nor make acceptance part of work identity.

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed occurrence."** Dumping telemetry without occurrence references (`methodDescriptionRef` and edition when current, performer assignment, time window, affected referent, and exact evidence-use relation) -> **Not Work**. Recover the work occurrence and relate the log as evidence.
* **Record-handling-as-transformation.** ETL, copying, formatting, evaluation, or publication work is treated as proof that a record or dataset changed -> Keep the grounded Work occurrence, but assert actual change only after A.3.4 identifies the transformation and an exact work-to-change fact obtains.
* **Silent cross-locality acceptance.** "Ops accepted it, so audit accepts it." -> Name each receiving criterion, evaluation work, result episteme, and acceptance relation; add F.9 only when exact local senses must be bridged.
* **Description-change-as-occurrence-change.** A MethodDescription edition swap is treated as automatically splitting or preserving Work -> State the description-selection change separately, then apply `workContinuityPolicyRef` to actual method, binding, performer, referent, and extent changes.
* **Budget on the method.** Charging costs to Method or Role -> Attribute performed resource use only through exact relations involving Work individuals; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Slice-as-episode.** A monitoring interval, telemetry window, crank-angle segment, or one-second reception trace is called an episode only because it has timestamps -> Use `TemporalPartOf_work`, an evidence relation, or a telemetry relation unless a declared episode policy supplies event-bounded continuity.
* **Episode-as-new-work by habit.** A pause, retune, or interruption is always recorded as a new occurrence -> Apply exact `workContinuityPolicyRef`. Keep the same parent Work with `EpisodeOf_work` only when that policy preserves identity; otherwise identify a separate Work occurrence admitted under `U.Work`.
* **Method-factor-as-work-part by label.** A step, stroke, receiver component, graph node, or method-description section is treated as a work part or submethod by name -> Recover the current object: `U.Method` factor, `U.MethodDescription` constituent, `TemporalPartOf_work`, `OperationalPartOf_work`, evidence segment, mechanism material, system-component behavior, or missing-source-relation note.
* **Granularity inflation.** Every interval or trace row receives a durable work-part name -> Name the work part only when a current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on it.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> recover the exact `B.1.4` temporal aggregation and cite its policy per KPI.
* **Double-count in overlaps.** Summing child and parent resource facts as one ledger -> recover the `B.1.6` aggregation claim and apply its exact overlap or deduplication policy.

### A.15.1:12 - Existing work-log repair applications

1. **Recover occurrence assertions.** For existing logs, identify the independently grounded Work occurrence and write an assertion or description that cites its designator, actual `enactsMethod`, optional `methodDescriptionRef`, exact `performedBy`, extent, affected referent, bindings, containing system, and resource-use facts. Do not create Work by creating a record.
2. **Recover the work-judgment basis.** Name exact `workContinuityPolicyRef`, its effective reference scheme, and any current MethodDescription edition, scope, qualification window, aggregation policy, criterion, or evidence-use relation without making those epistemes part of the Work.
3. **Record the continuity policy.** Cite exact `workContinuityPolicyRef` and decide when an interruption stays within one occurrence, creates an episode, or forces a new occurrence.
4. **Separate slice, episode, and operational part.** Use interval/aspect for `TemporalPartOf_work`, event-bounded continuity for `EpisodeOf_work`, and recovered occurrence-side part plus any separately recovered method factor for `OperationalPartOf_work`.
5. **Name only useful work parts.** If no current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on the candidate part, keep it as a relation, evidence slice, or telemetry slice.
6. **Return temporal roll-up to B.1.4.** Cite the exact temporal aggregation and its union, hull, coverage, and non-overlap policy in the KPI rather than recreating it on Work.
7. **Return resource roll-up to B.1.6.** Recover the typed resource ledger, evidence basis, allocation, and overlap or deduplication policy there; each contributing performed resource-use relation remains independently obtaining with an exact Work occurrence as a participant.
8. **Pull plans out.** Keep calendars and planned fillings in exact `U.WorkPlan` content; establish performed values only through direct relations in which the Work occurrence participates and through exact A.6.1 bindings.
9. **Bind actual values directly.** Recover each participant or parameter through its obtaining subject relation or exact A.6.1 application binding; retain MethodDescription defaults and WorkPlan choices as non-actual neighbors.

### A.15.1:13 - Consequences

| Benefits                                                                                                                 | Trade-offs and mitigations                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Cost, time, and quality claims cite concrete Work individuals through exact governing relations; root-cause analysis and accountability improve. | **More explicit occurrence claims.** Identify Work occurrences and their assertion or description epistemes; do not treat record creation as occurrence creation. |
| **Sound roll-up inputs.** Exact Work refs, intervals, parts, and performed resource-use facts make temporal and resource aggregation replayable. | **Direct-owner discipline.** Recover temporal aggregation in `B.1.4` and work-resource aggregation in `B.1.6`; cite their policies and results rather than copying Gamma semantics into Work. |
| **Cross-locality clarity.** Exact method-description, scheme, scope, criterion, evaluation, and acceptance relations prevent silent meaning drift. | **Bridge upkeep.** Maintain F.9 Bridges only for exact local-sense crossings that a receiving use actually needs. |
| **4D extensional coherence.** Parts, overlaps, and retries stop double-counting and identity confusion.                  | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |

### A.15.1:13.0 - Rationale

`U.Work` is retained as the admitted kind for dated Work occurrences because method, method description, work plan, affected entity, actual change, evaluation-result episteme, delivered entity, and downstream effect are different FPF objects. One Work individual is the world-side occurrence; an assertion or description about it is a separate episteme. The same wording in a source episteme, publication occurrence, method description, or work plan can point to several of these objects, but performed-work claims need occurrence grounding, temporal bounds, role assignment, enacted method, and affected referent rather than a convenient method or plan label. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local three-way distinction: `U.Work` as the admitted kind, one Work individual as a world-side dated occurrence, and an assertion or description about that occurrence as a separate `U.Episteme`. The occurrence stands in exact performer, method, temporal, affected-referent, binding, containing-system, and resource-use relations, while neighboring change, evaluation, evidence, production, delivery, and acceptance claims remain separate. Historical occurrence modeling is used as lineage only when a current practice still needs that distinction.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they designate independently grounded Work individuals and make involved objects, performer or role assignment, enacted method, temporal extent, affected referent, and exact interpretation or policy references needed by the receiving claim recoverable. | Treating telemetry or event rows alone as Work occurrences or as membership evidence for `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry can support, replay, measure, or diagnose a claim about work, but the occurrence still needs performer assignment, enacted method, temporal extent, affected referent, bindings, and resource-use facts. | Counting trace, metric, or log existence as the performed work, a result, or dominance evidence without the governing evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Assertions or descriptions about Work cite exact evidence-provenance relations and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | A.15.1 supplies exact Work intervals, parts, and performed resource-use facts; `B.1.4` governs temporal aggregation and `B.1.6` governs work-resource aggregation, each with its exact policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |

### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`; C.2.1 for episteme edition and effective `U.ReferenceScheme`; A.2.6 for claim scope; and C.27.TA for temporal qualification. A.1.1 enters only when a separately identified `BoundedModelUseStructure` changes the receiving work claim.
* **Coordinates with:** A.15 for Role-Method-Work alignment; A.6.1 and the exact direct relation patterns for actual bindings and participants; A.3.4 for independently identified actual transformations; A.15.PROD for local production-work, entity-identity-inception, and production-completion claims; B.1.4 for temporal aggregation and optional `Gamma_time`; B.1.6 for work-resource aggregation, ledger discipline, and optional `Gamma_work`; `E.10` and `E.10.ARCH` for work-wording recovery; `A.10`, `B.3`, `E.17`, and `A.15.4` for evidence, assurance, publication-use, or appearance-based reliance repair; `A.15.5` for readiness before performed work; and `C.32.P2S` for carry-through. A permission, gate, result, production, delivery, or acceptance claim remains independent of Work identity.
* **Informs:** reporting and KPI patterns; assurance and evidence patterns that use Work as the reference occurrence; and scheduling patterns that compare exact `U.WorkPlan` claims with independently identified Work occurrences admitted under `U.Work`.

### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Separation aid:** Who? **RoleAssignment**. Can? **Capability**. How? **Method**. Which account of the method? **MethodDescription**. Did it happen? **Work**.
* **Interpretation checks:** exact method-description edition and scheme; covering `U.RoleAssignment`; separately governed criterion, evaluation work, result episteme, and acceptance relation.
* **Roll-ups:** A.15.1 supplies exact Work refs, intervals, parts, and performed resource-use facts; cite `B.1.4` for temporal aggregates and `B.1.6` for resource ledgers, each with its declared policy.
* **Episodes vs retries:** same occurrence split vs new occurrence; write the policy.
* **Resource honesty:** performed resource use is related to exact Work individuals through separately obtaining resource-use relations; participants, operation values, changes, results, delivery, acceptance, and outcomes retain their direct relations and owners.

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, identify one Work individual admitted under `U.Work`, then recover the separately obtaining performer-assignment, enacted-method, binding, resource-use, temporal, affected-referent, and containing-system relations required by the receiving use. Carry actual change, production, evaluation-result, evidence, delivery, acceptance, transfer, or receiving-use claims as separately governed continuation objects.

A Work occurrence may be designated by an episteme that also cites a `U.WorkPlan`, exact A.15.3 planned-filling claim, or prior readiness claim as a baseline. State every actual participant, parameter, premise, operation argument or result, resource use, and affected referent only through its obtaining direct relation or exact A.6.1 application binding. Keep plan, comparison, transfer, evidence, assurance, gate, readiness, transformation, production, evaluation, result episteme, delivery, acceptance, and downstream effect under their direct governors.

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate assertion that an individual is Work admitted under `U.Work` when occurrence designator, performer-assignment, actual enacted-method, temporal, `executedWithin`, affected-referent, current direct-relation or A.6.1 binding, resource-use relation, or continuity-policy basis needed by the receiving use cannot be recovered. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated Work occurrence or gratuitous work part.

Repair the work assertion or description when a subsequent source changes the resolved temporal extent, performer assignment, actual enacted method, selected method-description reference, direct binding, resource-use claim, affected referent, containing system, work-continuity policy, or work-part relation. Repair a neighboring `B.1.4` or `B.1.6` result when its overlap or aggregation policy changes; that policy change alone does not rewrite Work. Reidentification follows the occurrence facts and exact continuity policy; a changed description, record, evidence set, publication, or aggregation result alone does not rewrite Work. Repair a neighboring change, evaluation, evidence, production, delivery, or acceptance claim under its own pattern.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a Work-occurrence reference only when the receiving claim actually depends on that occurrence.

### A.15.1:End

