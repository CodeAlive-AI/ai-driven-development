## A.15.1 - U.Work

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `U.Work` as the admitted kind when the current claim concerns one performed Work individual: a world-side dated occurrence performed by one or more admitted holder `U.System`s under exact obtaining `U.RoleAssignment`s. The systems perform the work; the assignments are the separately obtaining role-holding relations under which the attribution is valid. The occurrence has an actual temporal extent, enacts an exact method, and is executed within an exact containing system. State a binding, resource-use fact, or direct work-to-referent relation only when it actually obtains and the receiving use needs it; an assertion, description, log, or record about the occurrence is a separate `U.Episteme` and does not store fields in the occurrence. When the reader asks what the work returned, changed, produced, transferred, or caused someone to accept, use the concrete three-question route in §4.6 instead of adding an output or outcome field to Work.

**Use this when.** Use this pattern when a plan, method description, schedule, log, telemetry stream, dashboard, approval-looking cue, publication face, result statement, or evidence-provenance relation is being treated as if it were performed work. `U.Work` is the admitted kind; one Work individual is the world-side occurrence. A separate assertion or description episteme may designate that occurrence and its obtaining relations, while surrounding records may constrain, evidence, schedule, publish, or judge it; none becomes the occurrence by being published.

**First useful object.** One independently identified world-side dated Work occurrence admitted under `U.Work`. When the receiving use needs an assertion or description, keep that object as a separate `U.Episteme`: let it designate the occurrence and state the admitted holder `U.System` that actually performed it, the exact obtaining `U.RoleAssignment` under which that system performed it, and, when explicit attribution identity is consumed, the F.6 attribution relation linking the Work occurrence to that assignment. State actual `enactsMethod -> U.Method`, temporal extent, and `executedWithin -> U.System`. Add a direct work-to-referent relation, binding, or resource-use relation only when it actually obtains and the receiving claim uses it. If the next sentence reports a result, change, production, delivery, or judgment, select its exact object and owner from §4.6; do not make it a Work field.

**First-use checks.**
1. Name the candidate occurrence and the work-facing claim that depends on it.
2. Recover every admitted `U.System` that actually performed the occurrence and the exact obtaining `U.RoleAssignment` under which each system performed it; then recover the enacted `U.Method`, temporal extent, and accountable or containing `U.System`. Add only the concrete bindings, performed resource-use facts, and direct work-to-referent relations that actually obtain and matter to the receiving use. Route any claimed result, change, production, delivery, evidence use, or judgment through the one matching §4.6 row.
3. Decide whether the encountered record, trace, item, or display designates a Work individual admitted under `U.Work`, only a plan (`A.15.2`), only a method (`A.3.1`), only a method description (`A.3.2`), only evidence for work (`A.10`), only a publication-use relation (`E.17`), only a declarative representation (`C.2.P.DR` or the direct representation pattern), or an `A.15.4` appearance-based reliance repair case.
4. For composite, repeated, interrupted, or overlapping occurrences, declare each work-part relation and the naming threshold. Before using totals, recover the exact `B.1.4` temporal aggregation or `B.1.6` work-resource aggregation and its policy. Do not name a work part when a temporal relation, evidence slice, telemetry segment, or missing-source-relation note is the actual object needed.
5. If the required occurrence references cannot be recovered, lower the claim to a missing-source-relation note, work-evidence note, plan note, publication-use note, declarative-representation note, or `A.15.4` repair request; do not backdate work.

**Ordinary use.** For a simple occurrence, one readable assertion naming the actual performer system, the covering assignment under which it performed, enacted method, temporal extent, and containing system is enough. Add a binding, used resource, or work-to-referent fact only when the assertion relies on that obtaining relation.

**Reliance-bearing use.** Add only the exact neighboring claims on which cost, quality, audit, evidence, conformance, gate, release, measurement, model use, or aggregation currently depends; do not turn them into fields of the work occurrence.

**Stop condition.** Stop once the occurrence is either recoverable as one Work individual admitted under `U.Work` at the needed granularity or lowered to a neighboring relation that no longer claims performed work.

**What goes wrong if missed.** Teams count plans, method descriptions, approval-looking cues, dashboards, telemetry, or evidence records as if work already happened, then attach cost, responsibility, quality, or result claims to the wrong EntityOfConcern.

**What this buys.** One dated occurrence identity whose actual performer systems, covering assignments, enacted method, temporal extent, and containing system remain inspectable, together with any actually obtaining work-to-referent, binding, and resource-use relations used by the claim. A practitioner can then report a result or consequence through the concrete §4.6 branch without turning it into Work identity.

**Not this pattern when.** Not this pattern when the current claim is only a method (`A.3.1`), only a method description (`A.3.2`), only a plan or schedule (`A.15.2`), only declaration-local `SlotFillingsPlanItem` content inside an A.15.3-governed WorkPlan, only work-entry readiness or full-kit preparation before work entry (`A.15.5`), only a visible cue that needs `A.15.4` appearance-based reliance repair before reliance, only evidence or assurance (`A.10` or `B.3`), only publication-use behavior (`E.17`), or only a declarative representation overread as a work-control or method claim (`C.2.P.DR` or the direct representation pattern).

### A.15.1:1 - Problem Frame

After we have separated **who is assigned** (via `U.RoleAssignment`), **what capability is being relied on** (via `U.Capability`), **how in principle** the work is done (the exact `U.Method`), and which claim-bearing episteme describes that method when current (`U.MethodDescription`), we still need a precise concept for **what happened as performed work** in real time and space.

Every Work individual has actual performer-system, covering-assignment, enacted-method, temporal, and containing-system facts. It stands in a direct work-to-referent, binding, or resource-use relation only when that relation obtains world-side; none is a field stored in the occurrence. A separate assertion or description may designate that individual and state the relations, but the episteme neither creates the relations nor becomes the Work occurrence.

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

`U.Work` is the admitted U-kind for dated 4D occurrence holons. One Work individual is one independently identified world-side dated performed occurrence with its own governed temporal extent. The actual performer is an admitted `U.System`. For every performer, recover the exact obtaining `U.RoleAssignment` whose `HolderSystemSlot` resolves to that system, whose role interpretation is current, and whose occurrence covers the work or the exact attributed work part. The system acts; the assignment is the world-side relation under which the attribution holds, and it neither acts nor enacts a method.

The canonical F.6 relation `performedUnderAssignment(W, RA)` attributes one exact Work occurrence to one exact assignment occurrence. For an obtaining attribution, its actual-performer projection is `S = RA.HolderSystemSlot`; the relation obtains only when admitted system `S` actually performed `W` under `RA` and `RA` covers the attributed extent. In practitioner prose name both objects: `S performed W under RA`. The legacy spelling `performedBy(W, RA)` is a deprecated compatibility alias only; do not author new claims with it, and never say that `RA` performed `W`.

An exact `enactsMethod` relation connects the Work individual to an exact `U.Method`, and one exact `executedWithin` relation names its containing `U.System`. Direct work-to-referent, binding, and performed resource-use relations are recovered independently only when they obtain and the current claim needs them. An occurrence designator permits reference but does not identify work by label, ticket, trace, record, or storage convention; an assertion or description about the occurrence is a separate `U.Episteme`.

The actual `enactsMethod` relation obtains between the Work occurrence and the exact `U.Method`; it is not a field of either participant. An exact `U.MethodDescription` may be cited when its claims identify, constrain, or justify that method for the receiving use; the description is not enacted and its fields do not become actual work bindings. A selected model-use structure likewise enters only through the exact receiving relation whose interpretation it changes.

When actual change is current, identify one exact `U.Transformation` independently under A.3.4 and recover the exact work-to-change facts under their direct subject governor or the accepted A.15.PROD/A.6.RCD route. A morphism, delta expression, state-plane trace, pre-state, or post-state may represent or support that neighboring change claim; none is a mandatory field of a Work occurrence or a work-identity discriminator by form.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

#### A.15.1:4.2 - Core occurrence references and neighboring links

When a separate assertion or description episteme describes one Work occurrence, recover the following content at the granularity required by the current use. Each item names an occurrence designator, a world-side relation or temporal fact, or a reference to another episteme; the list is not a slot or field schema for the Work individual:

1. **Occurrence and extent** — one occurrence designator plus exact start and end, or an explicitly open end for in-flight work; add location only when the work claim depends on it.
2. **Performer system and assignment** — name each admitted holder `U.System` that actually performed the occurrence and the exact obtaining `U.RoleAssignment` under which it performed. Verify that the assignment's `HolderSystemSlot` resolves to that same system and recover its role value, role-taxonomy episteme, effective reference scheme, obtaining condition, and extent under A.2.1. When explicit F.6 attribution identity is used, `performedUnderAssignment(W, RA)` cites `RA` as the assignment ground; the actual performer remains its holder system.
3. **Enacted method** — actual `enactsMethod -> U.Method`. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on the exact description edition; the description is not enacted.
4. **Containing system** — `executedWithin -> U.System`; if ordinary speech says subsystem, name that `U.System` and its exact part relation to the larger holon.
5. **Work-to-referent relation, when current** — name the exact direct subject relation and its subject, asset, product, patient, learner, dataset, document, or other referent only when that relation actually obtains and the receiving claim uses it. "Work on X", shared timing, a record mention, or a convenient `affected` field establishes no such relation. An obtaining work-to-referent fact does not by itself assert change, production, delivery, or acceptance.
6. **Actual participation and bindings** — each participant, parameter, supplied constituent, premise, reference use, operation argument, or operation result only through an obtaining direct subject relation or exact A.6.1 operation-application binding. A MethodDescription field, plan row, type-compatible value, or log token establishes none of them.
7. **Performed resource use** — exact energy, material, machine-time, money, tool-wear, or other resource-use facts at the boundary needed by costing or sustainability use.
8. **Continuity policy, only when current** — when a named identity, episode, retry, resumption, or aggregation use must resolve an ambiguous segmentation, cite `workContinuityPolicyRef` to the exact C.2.1 episteme whose claims state the branch criterion and tolerances for that use. Interpret it under its effective `U.ReferenceScheme` and direct policy owner when one exists. It is a `U.MethodDescription` only if the same episteme independently satisfies A.3.2's method-description criterion. A simple uninterrupted occurrence needs no continuity-policy reference; the policy supports a judgment about the occurrence and neither constitutes nor rewrites it.
9. **Work mereology and temporal relations** — exact parent, part, predecessor, successor, overlap, retry, or resumption relations only when their predicates obtain.
10. **Actual change and production claims** — exact A.3.4 transformations, direct work-to-change facts, and only the current A.15.PROD production-work, entity-identity-inception, or production-completion claim. None follows from work identity or parthood.
11. **Evaluation and downstream claims** — use the one matching §4.6 row for evaluation work and result, evidence use, delivery or transfer, and acceptance; omit every row that is not current.
12. **Evidence, publication, and model use** — cite only the exact evidence-use, publication-use, currentness, claim-scope, reference-plane, bridge, or selected model-use relation needed by the receiving claim.

#### A.15.1:4.3 - Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| A claim-bearing episteme expressed through a **recipe, code artifact, or diagram** and substantively about one admitted exact method | **`U.MethodDescription`** | Does the same episteme meet A.3.2's exact membership threshold? Otherwise keep the representation, publication, formal substrate, or other direct owner. |
| The **semantic "way of doing"**               | **`U.Method`**             | Same method identity across notations?                         |
| The **assignment** ("who is being what")     | **`U.Role` value plus `U.RoleAssignment` relation** | Can be reassigned without changing the system?                  |
| The **ability** ("can do within bounds")      | **`U.Capability`**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs and resource-use evidence | One Work individual admitted under **`U.Work`** | Did it happen during the stated temporal extent, with the recovered performer system, covering assignment, enactment, and containing system? Are any claimed binding, work-to-referent, or resource-use facts independently obtaining? |
| The **actual state change associated with this occurrence** | **`U.Transformation` plus exact work-to-change facts** | Is the change independently grounded under A.3.4, and does a separately governed relation connect it to this work? |

#### A.15.1:4.4 - Publication-use boundary for `U.Work`

A publication about one Work occurrence projects an already declared assertion or description episteme; it does not create the world-side occurrence, add performed-occurrence facts, or make a plan, source reconstruction, dashboard, publication face, or carrier count as performed work.

Preparation is classifiable as one Work individual under `U.Work` only after it actually occurs and the actual performer `U.System`, its covering `U.RoleAssignment` and F.6 attribution when explicit, the exact `enactsMethod`, temporal extent, and `executedWithin` relation obtain independently. Add a work-to-referent, binding, or resource-use fact only through its own obtaining relation when the receiving preparation claim needs it. The readiness relation that asks whether intended work is ready enough to enter a work boundary is `WorkEntryReadiness@Context` under `A.15.5`; a readiness label, full-kit checklist, or launch-looking cue is not a performed occurrence.

| Publication-use pressure | Work-local rule |
|---|---|
| PlainView, TechCard, InteropCard, or AssuranceLane presents work material | Project only the work-occurrence references needed by that view: temporal extent, actual performer system, covering assignment and F.6 attribution when explicit, enacted method, and containing system, plus any independently obtaining binding, resource-use, or work-to-referent relation on which the view relies. Project a neighboring result, change, production, delivery, evidence, or judgment only through its matching §4.6 row; do not add a consequence field to Work. |
| numeric, comparable, aggregation, or benchmark content appears | Pin the comparator, aggregation policy, CG-Spec, reference plane, and transport edition needed by the claimed comparison; do not hide scalarization in the publication face. |
| publication cites method-description, work-plan, or cross-context material | Keep the Work occurrence as the dated performed individual admitted under `U.Work`; cite `U.MethodDescription` references, work-plan references, cross-context material, Bridge relation, UTS relation, reference-plane, or edition relation only through the direct governing pattern named for that citation. |
| reconstructed records look like a performed occurrence | Do not synthesize a surrogate Work occurrence; a publication may cite only Work individuals that meet the occurrence basis in this pattern. |

#### A.15.1:4.5 - Crossing visibility for work publications

When a work publication crosses a method-description edition, effective reference scheme, claim scope, selected model-use structure, reference plane, unit, or publication edition, publish the exact crossing or change relation used by the publication. Penalties and reliability changes belong to the relevant comparison, bridge, publication, or evidence relation; they do not change the identity of the Work occurrence.

A planned, gate-selected, or launch-labelled value becomes actual only when an obtaining direct subject relation or exact A.6.1 operation-application binding makes it participate in the occurrence. Do not back-fill a plan or infer an actual binding from shared wording. Pre-state and post-state references remain with an independently governed transformation or comparison claim; they do not bind to the Work occurrence merely because their times bracket it.

#### A.15.1:4.6 - Route a result or consequence to its direct owner

Start with the ordinary sentence the reader needs, then select exactly one row for each separate claim. An absent row stays absent; the table is not a result record to fill.

| Reader's sentence | Direct owner and exact object | Stop / non-inference |
| --- | --- | --- |
| **This work happened.** | A.15.1: exact `W : U.Work`, performer system, covering assignment, enacted method, extent, and containing system | a log, plan, output, or verdict does not establish `W` |
| **The application returned X** or **X is a result of W.** | exact A.6.1 application and result binding; add an already governed subject-specific `WorkResultRelation` only when its predicate actually obtains. If the wording hides the relation, use A.6.P.WMR to recover it | a result binding is not production, delivery, acceptance, or a universal work-result relation |
| **This referent changed.** | A.3.4: one exact `U.Transformation` plus the exact subject-governed work-to-change fact | temporal overlap, a delta picture, or common referent does not connect the change to `W` |
| **W produced X**, **X first existed**, or **production completed.** | the one current A.15.PROD branch: production-work participation, entity-identity inception, or production completion, each with its own criterion and boundary | one branch establishes neither of the other two nor delivery or acceptance |
| **Evaluation found V.** | separate evaluation `U.Work`; exact evaluation application and result binding or direct evaluation-result relation; when a durable claim is needed, one C.2.1 evaluation-result episteme | the evaluator's work, returned value, and result episteme are three different objects |
| **These observations support the claim.** | A.10 claim-bound evidence-provenance relation, or A.2.4 for the lighter episteme evidence-use relation | evidence supports the named claim for the bounded use; it does not create the work, result, or verdict |
| **X was delivered or transferred.** | the exact subject-owned delivery or transfer relation; use A.2.3 only when a current promise-content use supplies its delivery predicate | production, a package, or a handoff label does not establish transfer; absent a direct governor, return the exact missing-governor blocker |
| **X was accepted.** | exact criterion edition, acceptance or evaluation work, result binding or result episteme, and the exact subject-owned acceptance relation; use A.2.3 only for its promise-content branch | delivery, a passing evaluation value, or evidence alone does not establish acceptance |

**Three-question result check.** (1) **Did the work occur?** Name `W` and its performer, assignment, method, time, and containing system. (2) **What separate result or consequence is claimed?** Name the exact returned value, entity, change, production claim, or transfer and use its row above. (3) **Who judged or accepted what, by which criterion and evidence?** Name the evaluation work, result, evidence relation, and acceptance relation separately. If the reader needs only the first or first two answers, stop there.

### A.15.1:5 - Work mereology (how occurrences form holarchies)

Work identity is occurrence-grounded and 4D. Start from the actual performance history: work-entry and end events, occupied spatiotemporal extent, performer systems and assignments, enacted method, containing system, any direct work-to-referent relations, actual bindings, resource use, and exact work-part or temporal relations. A distinct actual work-entry after an established completion or termination identifies a later occurrence; a proper work part and its parent are distinct individuals; independently grounded concurrent performances are distinct. A record, trace, policy episteme, or later judgment creates none of them. A continuity policy is needed only when a named use must decide how to group that already existing history across an interruption, resumption, mode or method switch, performer replacement, referent or binding change, or composite boundary.

#### A.15.1:5.1 - Parts and wholes of Work (occurrence facts)

* **Temporal-part (`TemporalPartOf_work`).** A proper **time-slice relation** over one selected Work occurrence or work phase. The selected part is grounded by parent work identity plus interval and, when needed, a named aspect such as resource use, telemetry, SLA coverage, or interval-local evidence. A temporal part is useful for monitoring, utilization, lead time, and interval-local evidence. It has no independent method-switch identity by that fact.
* **Episode-part (`EpisodeOf_work`).** A named, event-bounded fragment selected inside one parent Work occurrence for a current use. Entry, resumption, mode switch, switch-to-method, interruption, switch-away, completion, or a declared pause may supply the candidate boundary. The direct episode predicate also cites an exact `workContinuityPolicyRef` only when the use needs that policy to decide whether the fragment remains under the parent; timestamps or an episode-looking label alone establish no episode relation.

`workContinuityPolicyRef` designates the exact C.2.1 episteme whose claims state the named use, boundary events, tolerated variation, and branch criterion. Interpret those claims under that episteme's effective `U.ReferenceScheme`; name any current `U.ClaimScope`, temporal qualification window, or model-use structure separately. The policy episteme classifies the already existing history for that use. A later or competing policy edition can revise the identity or segmentation assertion, but it neither becomes a `U.MethodDescription` by policy form nor changes the occurrence, its parts, or their actual facts.

* **Operational-part (`OperationalPartOf_work`).** A **work-part occurrence** that may enact a factor of a recovered `U.Method`, for example, an incision occurrence within an appendectomy occurrence, possibly **overlapping** with others in time. If a method-description reference is current, it identifies, describes, constrains, or evidences that method factor; the referenced `U.MethodDescription` is not enacted. If no `U.Method` factor is recovered, govern the material as a work part, evidence segment, telemetry segment, mechanism material, system-component behavior, or missing-source-relation note under the direct pattern.
* **Concurrent work parts (derived use-side reading; no fourth parthood relation).** First state each exact work-part relation to the same parent and then state the independently governed interval `overlaps` fact. When coordination is current, state its exact direct relation separately. Shared parentage and overlap do not by themselves establish coordination, and `ConcurrentPartOf_work` is not introduced as a primitive work-part relation.

**Naming threshold.** Do not mint a durable public U-kind, durable named work object, or separate work occurrence for every interval, telemetry segment, pause, or episode-looking wording. Use a derivative part relation unless the downstream use needs a named work part with its own resources, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use. Otherwise lower to a temporal relation, evidence slice, telemetry segment, method-description constituent, missing-source-relation note, or the neighboring object that is actually current.

**Didactic rule:** **Method composition is not proof of Work decomposition, and Work decomposition is not proof of method composition.** A temporal work part may enact the same whole method during a slice. An episode may continue one method or mode, span several operational parts, repeat the same method fragment, or be split by evidence policy without changing method identity. An operational part may correspond to a method factor only when that factor is recovered as `U.Method`.

**Quick choice test.**

- Ask **"which interval or aspect of the parent work do I need?"** If that is enough, use `TemporalPartOf_work`.
- Ask **"does this named use need an event-bounded fragment of the parent?"** If yes, recover the candidate boundary events. Cite `workContinuityPolicyRef` only when interruption, resumption, switch, replacement, or pause leaves the grouping ambiguous for that use; then use `EpisodeOf_work` only when its direct predicate is satisfied.
- Ask **"which performed sub-occurrence has its own actual performer system, covering assignment, temporal extent, enacted method, affected referent, bindings, resource use, or aggregation role?"** If that is current, use `OperationalPartOf_work` or another declared work-part relation. A neighboring evaluation or effect claim does not establish work parthood by itself.
- Ask **"which way-of-doing part is being composed?"** If the answer needs preconditions, effects, interface, and whole-method relation, recover a `U.Method` submethod under `A.3.1` and `B.1.5`; do not make the work part itself carry the method identity.

#### A.15.1:5.2 - Key relations among Work

* **`precedes` or `happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains` or `within`** — one Work's window contains another's.
* **Causal-use relation reference** — if one work occurrence is claimed to explain, trigger, or cause another, keep the work-occurrence link separate from the causal-use claim governed by `C.28` or another causal-use pattern named by value.
* **`retryOf`** — a later Work occurrence that starts after the earlier occurrence ended and re-attempts the same named objective or enacted Method under the exact predicate of the retry relation. Similar wording or revised bindings alone do not establish the link.
* **`resumptionOf`** — an event-bounded episode or later Work occurrence that continues after interruption. Cite a continuity policy only when the named use must decide whether the later performance remains under the same parent or is a distinct occurrence linked to the earlier one.

These relations are **occurrence facts**, not method-design assumptions.

#### A.15.1:5.3 - Work-occurrence relations used by Part B roll-ups

`A.15.1` supplies the identity of each independently identified Work occurrence or Work part and makes its exact temporal and performed resource-use relations recoverable. It does not itself return a temporal aggregate or resource ledger.

* **Temporal coverage.** When a receiving use needs utilization, elapsed time, phase coverage, or another roll-up over Work intervals, open `B.1.4`. Its recovered `ContextTemporalAggregation@Context`, coverage and non-overlap conditions, aggregation policy, and optional `Gamma_time` notation govern union, hull, or another admitted temporal aggregate. The work intervals remain A.15.1 facts.
* **Resource aggregation.** When a receiving use needs a total over materials, energy, time, money, tool wear, or another performed resource value, open `B.1.6`. Its recovered `WorkResourceAggregation@Context`, typed resource-accounting basis, evidence refs, overlap or deduplication policy, ledger, aggregation rule, and optional `Gamma_work` notation govern the aggregate. Each contributing performed resource-use relation obtains separately with its exact Work occurrence as a participant; any ledger or assertion about that relation is a separate episteme.

**Manager's tip:** cite the exact `B.1.4` or `B.1.6` aggregation result and policy beside the KPI. A Work-part list, shared parent, or operator spelling supplies neither the aggregate nor its policy.

#### A.15.1:5.4 - Identity and reidentification of Work

Two descriptions, assertions, records, or traces resolve to the same Work occurrence only when they designate the same actual world-side performance history, not merely the same name or policy edition. First compare the direct facts at the selected grain:

* the same actual work-entry or start and compatible occupied spatiotemporal extent;
* the same performance history, with each performer system, covering assignment, enacted method, and containing system, plus every actually obtaining work-to-referent, binding, and resource-use fact used by the identity claim, placed at the interval where it obtains;
* compatible work-part and temporal relations; and
* no fact that already identifies distinct individuals: a proper part versus its parent, independently grounded concurrent performances, or a later work-entry after the first occurrence's established completion or termination.

A corrected or later description of the same actual start, open end, or completed end can refine the assertion without changing the occurrence. A change of performer, assignment, method, referent, binding, resource use, or containing system during an otherwise unended performance history is an actual change to state explicitly; that change alone neither splits nor preserves the Work occurrence.

When a named receiving use must decide whether an interruption, resumption, method or mode switch, performer replacement, retune, rework, referent or binding change, or composite boundary stays inside one parent, cite the exact continuity-policy episteme, its effective reference scheme, applicable scope and window, and the branch criterion it applies to those facts. The selected policy can support one identity or segmentation assertion for that use. A later or competing policy edition may revise that assertion or supply another interpretation; it does not retroactively change what occurred.

#### A.15.1:5.5 - Interruptions, retries, resumptions, and description changes

* **Established end and later entry:** identify a later Work occurrence when the first occurrence has actually completed or terminated and another work-entry occurs. A larger composite Work may contain both only through explicit work-part relations.
* **Retry:** identify the later Work occurrence independently and add `retryOf` only when that relation's own predicate connects it to the ended attempt.
* **Ambiguous interruption or resumption:** preserve the actual boundary events and facts. If a named use must decide same-parent versus separate-occurrence grouping, apply its exact `workContinuityPolicyRef`; without that criterion, return an unresolved segmentation rather than making the policy implicit.
* **Performer, assignment, method, referent, binding, retune, or mode change:** state the actual change where it occurs. Split or retain the parent only when the direct facts already decide the boundary or a policy current to the named identity, episode, retry, resumption, or aggregation use supplies the criterion.
* **MethodDescription change:** record the selected description edition separately. A changed description edition neither splits nor preserves Work by itself; only an accompanying actual occurrence change enters the boundary judgment.
* **Rework:** identify the later performance independently. Relate it as another occurrence, episode, or operational part only after the applicable direct predicate and any genuinely needed boundary policy are satisfied. Keep causal attribution with the governing causal-use pattern.

Plans, costs, quality statistics, telemetry evidence, and method-reliance claims may depend on whether the selected history is a temporal part, event-bounded episode, operational part, or later occurrence. Name a continuity-policy episteme, effective reference scheme, scope, and qualification window only when that distinction is actually current. Otherwise retain the direct occurrence facts and stop; do not add policy apparatus to a simple uninterrupted case.

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
* **Performer system and assignment:** admitted system `OR_Team_A` performs this occurrence under exact `OR_Team_A_SurgicalTeamAssignment_2025-08-10 : U.RoleAssignment`, whose role value is `SurgicalTeamRole`, role-taxonomy episteme is `HospitalRoles-2025`, effective reference scheme is `Hospital-Operating-Scheme-2025`, and obtaining extent covers the surgery interval. The team system acts; the assignment does not.
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** a brief power dip occurs from 10:02 to 10:07. The named surgery-continuity use applies `HospitalWorkContinuityPolicy_2025`, a C.2.1 policy episteme interpreted under `Hospital-Operating-Scheme-2025`; its stated pause-and-resumption criterion keeps both event-bounded fragments under the same parent Work. The power dip alone would not decide that grouping.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses union for OR utilization and hull for patient lead time under separately declared policies.
* **B.1.6 resource roll-up:** a recovered `WorkResourceAggregation@Context` totals consumables and staff time once under its typed resource basis and overlap policy; every contributing resource-use relation continues to obtain independently with the exact Work occurrence as a participant.

#### A.15.1:6.2 - ETL pipeline (parallelism and retries)

* **Top work occurrence:** `ETL_Nightly_2025-08-11T01:00-01:47`.
* **Actual method and containing system:** `enactsMethod -> Nightly_ETL_Load@DataOps-2025`; `executedWithin -> DataPlatform_Prod`.
* **Affected referent, actual participation, and performed resources:** `WarehouseOrders_2025-08-11` is the affected dataset under the exact project data relation used by this case. The obtaining source-dataset participation of `RawOrders_2025-08-11` and destination-dataset participation of `WarehouseOrders_2025-08-11`, under their exact project data-use relations, are the actual-use facts on which this case relies. Actual cluster machine-time on `ETL_Cluster_3` and storage use on `WarehouseStore_1` are performed resource-use facts. None supplies a generic input/output binding or an automatic dataset-transformation claim.
* **Actual change, separately established:** A.3.4 identifies `WarehouseOrders_LoadTransformation_2025-08-11` as the bounded change of the exact dated warehouse partition across 01:00–01:47 under the declared source-snapshot and partition-write conditions. Before that boundary the partition lacks exact row set `AcceptedOrdersRowSet_2025-08-11`; after it, the project data-state relation to that row set obtains. A separate subject-governed work-to-change claim connects the transformation to `ETL_Nightly_2025-08-11T01:00-01:47`; temporal overlap, the destination designation, or the post-state alone would not. The transformation and connecting claim are not fields of the Work occurrence.
* **Performer system and assignment:** admitted system `ETL_Runtime` performs this occurrence under exact `ETL_Runtime_TransformerAssignment_2025-08-11 : U.RoleAssignment`, whose role value is `TransformerRole`, role-taxonomy episteme is `DataOpsRoles-2025`, effective reference scheme is `DataOps-Execution-Scheme-2025`, and obtaining extent covers the ETL interval. The runtime system acts; the assignment does not.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `WarehouseWrite` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **B.1.4 temporal roll-up:** a recovered temporal aggregation uses hull for SLA and union for cluster utilization under separately declared policies.
* **B.1.6 resource roll-up:** a recovered resource aggregation sums compute minutes under its declared overlap policy; source-dataset participation, destination-dataset participation, storage use, returned values, and downstream result claims stay under their exact direct relations rather than one input-output family.

#### A.15.1:6.3 - Thermodynamic cycle (work through a state-plane trace)

* **Run:** `Carnot_Cycle_Run_2025-08-09T1300_1306`.
* **Actual method and containing system:** `enactsMethod -> Carnot_Cycle_Operation@ThermoLab`; `executedWithin -> LabRig_7`.
* **Affected referent and performed resources:** `WorkingFluidCharge_7`; actual electrical-energy use attributed to the run through `HeaterBank_7` and `Chiller_7` during 13:00-13:06. Any thermodynamic energy-exchange or transformation claim remains separately governed.
* **`methodDescriptionRef`:** `Carnot_Cycle_Spec` with Dynamics model.
* **Performer system and assignment:** admitted system `LabRig_7` performs this occurrence under exact `LabRig_7_TransformerAssignment_2025-08-09 : U.RoleAssignment`, whose role value is `TransformerRole`, role-taxonomy episteme is `ThermoLabRoles-v2`, effective reference scheme is `ThermoLab-Experiment-Scheme`, and obtaining extent covers the laboratory-work interval. The rig system acts; the assignment does not.
* **Work identity:** this uninterrupted six-minute run is identified from its actual entry, extent, performer system, covering assignment and F.6 attribution when explicit, enacted method, and containing system, together with the actually obtaining work-to-referent, binding, and performed resource-use relations used in this case. No continuity-policy reference is needed because no interruption or competing segmentation is current. The thermodynamic state-plane trace separately describes or evidences actual change; it is not a work-identity field, work-control relation, or ordered instruction sequence.
* **Part B roll-ups:** B.1.4 may use the exact run interval in a temporal aggregation; B.1.6 may aggregate the performed energy-use facts under a typed resource basis and selected overlap policy. Any thermodynamic energy-exchange or transformation claim keeps its direct governor; no "steps" are required.

#### A.15.1:6.4 - Claim handling (episodes versus monitoring slices)

* **Top work occurrence:** `ClaimHandling_Case_8142_2026-06-03`.
* **Actual method and containing system:** `enactsMethod -> ClaimHandling@InsuranceOps-2026`; `executedWithin -> ClaimsOperations_A`.
* **Affected referent and performed resources:** `Claim_8142`; actual handler time during 09:00-09:42 and 10:11-10:38, plus actual case-system time on `ClaimsPlatform_A` during those episodes. The callback and monitoring records remain neighboring evidence or telemetry, not occurrence constituents.
* **`methodDescriptionRef`:** `Claims_Method_v7`.
* **Performer system and assignment:** admitted system `ClaimsTeam_A` performs this occurrence under exact `ClaimsTeam_A_HandlerAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `ClaimsHandlerRole`, role-taxonomy episteme is `InsuranceOpsRoles-2026`, effective reference scheme is `Claims-Handling-Scheme-2026`, and obtaining extent covers the claims-work interval. The team system acts; the assignment does not.
* **Episode policy:** the named claims-handling continuity use applies `ClaimsWorkContinuityPolicy_v7`, a C.2.1 policy episteme interpreted under `Claims-Handling-Scheme-2026`. Its stated under-one-hour callback criterion classifies `InitialReview_09:00-09:42` and `ResumedResolution_10:11-10:38` as two `EpisodeOf_work` fragments under the same parent. A later edition may revise that segmentation assertion without changing either interval's actual history.
* **Temporal monitoring slice:** `MonitoringSlice_09:15-09:20` is `TemporalPartOf_work` for queue-latency evidence. It is not a new work occurrence and not an episode unless downstream reliance needs a named part with its own evidence, KPI, acceptance, repair, or aggregation role.
* **Method relation:** both episodes enact the same claim-handling method. The five-minute slice does not prove a submethod.

#### A.15.1:6.5 - Internal-combustion engine (cycle parts without human-only boundary language)

* **Top work occurrence:** `EngineRun_Cell7_2026-06-03T1300_1330`.
* **Actual method and containing system:** `enactsMethod -> FourStrokeEngineOperation@TestBench-2026`; `executedWithin -> Engine_Cell7`.
* **Affected referent and performed resources:** `EngineUnderTest_7`; actual fuel use from `FuelBatch_F7` and ignition-electrical-energy use during 13:00-13:30. Any thermodynamic change, result, or evidence claim remains separately governed.
* **`methodDescriptionRef`:** `FourStrokeOperationSpec_v4`.
* **Performer system and assignment:** admitted system `Engine_Cell7` performs this occurrence under exact `Engine_Cell7_OperationAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `EngineOperationRole`, role-taxonomy episteme is `EngineCellRoles-2026`, effective reference scheme is `TestBench-Operating-Scheme-2026`, and obtaining extent covers the engine-run interval. The engine-cell system acts; the assignment does not.
* **Episodes:** when diagnosis or utilization needs event-bounded fragments, `EngineRunEpisodePolicy_2026`, a C.2.1 policy episteme under `TestBench-Operating-Scheme-2026`, states which start, stop, mode-change, fuel, ignition, or diagnostic events bound an `EpisodeOf_work`. Without that named use and branch criterion, the events remain direct history and do not mint episode objects.
* **Temporal parts:** crank-angle intervals or one-second telemetry windows are `TemporalPartOf_work` unless an exact receiving use requires a named work part for resource, evidence, KPI, acceptance, repair, or aggregation.
* **Method factors:** intake, compression, combustion-expansion, and exhaust are method factors only if recovered as `U.Method` submethods with method-level preconditions, effects, interfaces, and whole-method relation. Actual strokes are work parts or temporal parts of engine work, not submethods by label.

#### A.15.1:6.6 - Detector radio receiver (component behavior, method factor, work part)

* **Top work occurrence:** `ReceiverReception_Rx42_2026-06-03T2115_2120`.
* **Actual method and containing system:** `enactsMethod -> EnvelopeDetection@RadioLab-2026`; `executedWithin -> Receiver_Rx42`.
* **Affected referent and performed resources:** `RF_TestSignal_42_2115`; actual receiver-channel time on `Rx42_Channel_1` and electrical-energy use during 21:15-21:20. Waveform and telemetry traces remain separately governed representations or evidence.
* **`methodDescriptionRef`:** `EnvelopeDetectionMethod_v2`.
* **Performer system and assignment:** admitted system `Receiver_Rx42` performs this occurrence under exact `Receiver_Rx42_DetectorAssignment_2026-06-03 : U.RoleAssignment`, whose role value is `DetectorReceiverRole`, role-taxonomy episteme is `RadioLabRoles-2026`, effective reference scheme is `RadioLab-Reception-Scheme-2026`, and obtaining extent covers the reception interval. The receiver system acts; the assignment does not.
* **Episodes:** when signal-quality or diagnostic use needs event-bounded fragments, `ReceiverReceptionEpisodePolicy_2026`, a C.2.1 policy episteme under `RadioLab-Reception-Scheme-2026`, states whether retune, on/off, interruption, or diagnostic-mode events bound an `EpisodeOf_work`. A trace timestamp or retune label without that current branch criterion remains history, not an episode relation.
* **Temporal parts:** a one-second reception slice is `TemporalPartOf_work` for signal-quality evidence or telemetry aggregation. It is not a new occurrence merely because it appears in a trace.
* **Method and mechanism split:** tuning, rectification, smoothing, and acoustic output may be recovered as method factors, system-component behaviors, mechanism material, evidence traces, or operational work parts depending on the current claim. A detector component or waveform segment does not become a submethod or a work part by label.

#### A.15.1:6.7 - Classification work without result collapse

`Pump37_RecognitionWork_2026-07-20T1015_1022` is one Work individual admitted under `U.Work`, with temporal extent 10:15-10:22. Admitted system `RecognitionEvaluator_A` is the actual performer and performs this work under exact `Pump37_EvaluatorAssignment_2026-07-20 : U.RoleAssignment`. For explicit F.6 attribution, `performedUnderAssignment(Pump37_RecognitionWork_2026-07-20T1015_1022, Pump37_EvaluatorAssignment_2026-07-20)` obtains; its assignment endpoint is the ground under which `RecognitionEvaluator_A` performs and is not the actor. The assignment's role value is `HolonRecognitionEvaluatorRole`, role-taxonomy episteme is `FPFRoles-2026`, effective reference scheme is `FPF-Recognition-Scheme-2026`, and obtaining extent covers the work. Exact `enactsMethod(Pump37_RecognitionWork_2026-07-20T1015_1022, HolonRecognitionEvaluation@FPF)` and `executedWithin(Pump37_RecognitionWork_2026-07-20T1015_1022, FPF_Recognition_Service_A)` obtain, and the governed affected-referent fact concerns `Pump_37`. A separate assertion about the Work occurrence cites exact A.6.1 application `Pump37_RecognitionApplication_2026-07-20T1017`, whose `candidateArgument` binding designates `Pump_37` and whose `judgmentResult` binding returns `unknown`. Separately obtaining resource-use relations ground seven minutes of evaluator time and the application compute time on `RecognitionRunner_A`.

The returned `unknown` value remains the A.6.1 result binding. No `U.Transformation` of `Pump_37` or of a classification record is asserted: this evaluation Work remains admitted from its performer system, covering assignment, enacted method, extent, containing system, application binding, and resource-use facts without a pre-state, post-state, or delta. Candidate-side criterion satisfaction remains under A.1; evidence and assurance remain neighboring relations; and any materialized classification assertion or evaluation-result episteme remains under C.2.1. None is the Work occurrence or an intrinsic Work result field.

#### A.15.1:6.7.1 - Filled result route: build, verify, transfer, accept

`ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work` is performed by `BuildRunner_A : U.System` under `BuildRunnerAssignment_2026-07-21 : U.RoleAssignment`, enacts `ReproducibleBuild@BuildOps-v12`, runs from 09:00 to 09:12, and is executed within `BuildService_A`. Those facts establish the Work occurrence. The rows below add only the result and consequence claims that are current in this case.

| Current case claim | Exact object or relation | Kept separate from |
| --- | --- | --- |
| build application returned the binary | A.6.1 application `BuildApplication_12`, with result binding `builtBinary -> ReleaseBinary_12` | entity inception, production completion, delivery, acceptance |
| subject practice also needs a direct result relation | case-local occurrence `BuildRunReturnedBinary_12` under already declared predicate `BuildRunReturnedBinary@BuildOps-v12`, relating the build Work to `ReleaseBinary_12`; if that declaration were absent, this row would be omitted and the A.6.1 binding retained | a universal `WorkResultRelation` |
| the artifact-store partition changed | `ArtifactStorePopulationTransformation_12 : U.Transformation` under A.3.4, plus the exact BuildOps work-to-change claim relating it to the build Work | the Work occurrence and the returned binary |
| this was production, the binary first existed, and production completed | three separate A.15.PROD local claims: whole-production-work participation for the build Work; inception of `ReleaseBinary_12` at 09:11 under `ReleaseBinaryIdentitySpec_v12`; completion at 09:12 under `BuildCompletionCriterion_v12` | one omnibus production/result record |
| verification returned `pass` | separate `ReleaseBinary12_VerificationWork_2026-07-21T0913_0918 : U.Work`, A.6.1 application `VerifyApplication_12`, result binding `verdict -> pass`, and C.2.1 episteme `BinaryVerificationResult_12` when the durable verdict claim is needed | acceptance and the build Work's result binding |
| checksums and test logs support that verdict claim | A.10 evidence-provenance relation `BinaryVerificationEvidenceUse_12`, bounded to the verification claim and staging decision | truth by carrier presence or acceptance |
| the binary moved to staging | subject-owned transfer occurrence `ArtifactTransferToStaging_12` under `ArtifactTransferredToStaging@BuildOps-v12`, with exact binary and staging-system participants | production, verification, acceptance |
| staging accepted the binary | acceptance work `StagingAcceptanceWork_12` applies `StagingAcceptanceCriterion_v12`; exact subject-owned acceptance relation `StagingAcceptance_12` relates its verdict to `ReleaseBinary_12` | transfer, evidence, or a bare `pass` value |

The readable report is therefore: the build Work occurred; a different entity was returned and produced; an exact store transformation occurred; separate verification Work returned a verdict supported by evidence; a transfer moved the entity; and a later acceptance relation admitted it. Removing any non-current row does not alter the identity of the build Work.

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
* **Scope declaration:** The occurrence head is universal. Temporal semantics use the declared temporal reference. A simple uninterrupted occurrence needs no continuity-policy episteme; identity, episode, retry, resumption, or aggregation claims cite `workContinuityPolicyRef` and its effective `U.ReferenceScheme` only when the named use must resolve an ambiguous boundary. Claim scope, qualification windows, model-use structure, evidence, and source currentness remain separate when current.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** with admitted performer `U.System`s acting under exact obtaining `U.RoleAssignment`s and with actual `enactsMethod` relations, so that costing, quality, and audit rest on independently identified work occurrences rather than plans, recipes, assignments made to act, or a generic role-enactment fact.

### A.15.1:8 - Conformance Checklist (admission checks)

**CC-A15.1-1 (Strict distinction).**
`U.Work` is the admitted kind for dated performed Work occurrences. Each Work individual is world-side; it is not a `U.Method` (semantic way), `U.MethodDescription` (description), `U.Role` or `U.RoleAssignment` (assignment), `U.WorkPlan` (plan or schedule), or assertion, record, log, or publication about work.

**CC-A15.1-2 (Required occurrence basis).**
A conforming assertion or description about a Work individual designates one world-side occurrence admitted under `U.Work` and makes each actual performer `U.System`, the exact obtaining `U.RoleAssignment` under which that system performed, any explicit F.6 `performedUnderAssignment(W, RA)` attribution, actual `enactsMethod -> U.Method`, temporal extent, and `executedWithin -> U.System` recoverable. It also makes every actually obtaining direct work-to-referent relation, direct subject relation or A.6.1 binding, and performed resource-use fact used by the receiving claim recoverable; it does not invent any of them when absent. Cite `methodDescriptionRef -> U.MethodDescription` only when the receiving claim depends on that exact description edition. The episteme designates these independently obtaining objects and relations; it does not turn them into occurrence fields or make the assignment act.
**CC-A15.1-3 (Time window).**
A conforming assertion or description about one Work occurrence designates a world-side individual with a closed temporal extent `[t_start, t_end]`, or an explicitly open end while the occurrence is in flight. The episteme states or designates that extent and, where relevant, location or asset; neither an interval field nor the presence of the record creates the occurrence.

**CC-A15.1-4 (Interpretation and policy basis).**
A load-bearing work claim names direct occurrence facts first. It cites `workContinuityPolicyRef`, its effective `U.ReferenceScheme`, and applicable scope or qualification window only when a named identity, episode, retry, resumption, or aggregation use must resolve an ambiguous segmentation. Any exact method-description edition, aggregation-policy episteme, selected model-use structure, acceptance criterion, evaluation work, result episteme, and evidence use remains a neighboring claim rather than a work-identity field.

If two local senses must be related, F.9 receives the exact sense endpoints and the claimed direction and loss. A different reference scheme, role assignment, description edition, or model-use structure alone does not establish a Bridge.
**CC-A15.1-4b (No mandatory state-plane or delta).**
A Work claim needs no `StatePlaneRef`, pre-state, post-state, or delta merely to establish occurrence identity. When actual change is current, A.3.4 identifies the transformation and its state or boundary facts; a separate work-to-change claim connects it to Work.
**CC-A15.1-5 (RoleAssignment interval coverage).**
Every `U.RoleAssignment` cited by an obtaining F.6 `performedUnderAssignment(W, RA)` attribution has as its holder the exact admitted `U.System` stated to perform the work and covers the work interval or exact performed part attributed to that system. If the holder differs or the assignment does not cover the extent, keep the Work occurrence, performer claim, and assignment claim separate: repair or reject the attribution, or establish a retroactive assignment only under the exact A.2.1 rule that admits it.

**CC-A15.1-6 (Actual participant and operation binding).**
Every actual parameter, participant, premise, constituent, operation argument, or operation result used by the work is established through an obtaining direct subject relation or exact A.6.1 application binding. A MethodDescription declaration, default, A.15.3 planned filling, gate selection, compatible ValueKind, or stored token establishes no actual binding.
**CC-A15.1-7 (Capability check).**
Any capability threshold relied on for a Work occurrence is recovered under A.2.2 or the exact direct capability-fit or evaluation owner. A `U.Method` or `U.MethodDescription` may cite or describe that threshold but does not create the capability fact. Check the threshold against each admitted performer system named through the holder of its covering assignment for the performed-work interval or declared checkpoints; state a violation through its separately governed evaluation-result episteme or direct characteristic/evaluation relation, never as an intrinsic work outcome.

**CC-A15.1-8 (Acceptance criteria).**
An acceptance claim names the exact criterion or comparator specification, its edition, applicable scope and window, the evaluation or acceptance work that applied it, and the direct result relation. Success class, quality measurement, comparison result, and acceptance verdict remain distinct; no verdict is an intrinsic field of the Work occurrence or a condition of `U.Work` membership.
**CC-A15.1-9 (Resource honesty).**
Performed resource-use facts (energy, materials, machine-time, money, tool wear) are attributed through exact obtaining relations to particular Work individuals admitted under `U.Work`, not to `U.Method`, `U.MethodDescription`, `U.Role`, or `U.Capability`. Estimates belong in method descriptions or plans. Any aggregate ledger, unit conversion, allocation, or overlap and deduplication result belongs to `B.1.6` and cites the contributing Work occurrences and resource-use facts.

**CC-A15.1-10 (Mereology declared).**
When exact work-part relations obtain among Work individuals, declare each relation: temporal-part, episode-part, operational-part, or another relation with its own predicate. Ambiguous mixtures lower aggregation and identity claims. A `TemporalPartOf_work` claim names parent work identity plus interval or aspect; an `EpisodeOf_work` claim names the parent, candidate boundary events, and named use, adding `workContinuityPolicyRef` only when those facts leave the grouping ambiguous for that use; an `OperationalPartOf_work` claim names the occurrence-side part and any recovered method factor separately. Concurrency adds a separate interval `overlaps` fact and, when current, a separately governed coordination claim; it is not a fourth work-part relation.

**CC-A15.1-11 (Temporal coverage selection).**
For a temporal roll-up, `B.1.4` names the exact Work refs, aggregation concern, time window, coverage and non-overlap conditions, and policy selecting union, convex hull, or another admitted result. A.15.1 supplies the occurrence intervals but does not own the aggregate.

**CC-A15.1-12 (Resource aggregation).**
For a resource roll-up, `B.1.6` names the exact Work refs, typed resource basis, units, evidence, delimitation and time window, overlap or deduplication policy, ledger, and aggregation rule. A.15.1 supplies performed resource-use facts but does not own the aggregate ledger.

**CC-A15.1-13 (Identity and retries).**
A distinct actual work-entry after an established completion or termination identifies a later Work occurrence; a proper work part and its parent and independently grounded concurrent performances are also distinct individuals. Add `retryOf`, `resumptionOf`, or `EpisodeOf_work` only when its own predicate holds. An interruption, performer or assignment replacement, method or mode switch, retune, rework, affected-referent change, or binding change is stated as direct history and neither splits nor preserves the parent by itself. Cite `workContinuityPolicyRef` only when a named use needs a branch criterion for that ambiguity. A changed MethodDescription or policy edition alone revises at most the dependent description or segmentation judgment.
**CC-A15.1-14 (Concurrency and ordering).**
Overlaps and precedences among work occurrences use interval relations (`overlaps`, `precedes`, `contains`, or `within`). Implicit "step order" claims are not admitted as performed-work evidence.

**CC-A15.1-15 (Cross-locality evaluation).**
A work occurrence keeps one identity when several receiving uses evaluate it. Each use names its own effective reference scheme, claim scope, criterion, qualification window, evaluation work, and result episteme. Use F.9 only when an exact Bridge between local senses is actually needed; a shared work name or record carries no acceptance across uses.
**CC-A15.1-16 (Method-description changes do not decide Work identity).**
If a selected MethodDescription edition changes during the occurrence, state the description-selection or override claim separately. The edition change alone neither splits nor preserves Work. When an accompanying actual performer-system, covering-assignment, enacted-method, binding, affected-referent, mode, or extent change creates a boundary question for a named use, apply that use's exact continuity-policy criterion; a later policy edition revises the judgment, not the occurrence.
**CC-A15.1-17 (Distributed performers).**
If multiple admitted `U.System`s jointly perform the same top-level work occurrence, name every system, its exact obtaining covering `U.RoleAssignment`, and every explicit F.6 attribution; verify that each assignment's holder is that system and that its obtaining extent covers the attributed work. If the use instead needs a parent work with child occurrences, give every child its actual performer system, covering assignment, and work-part relation. A lead, accountability, or coordination claim remains separate and cannot substitute one designated assignment for the actual performer set.

**CC-A15.1-18 (Logs are evidence, not work by themselves).**
Logs and telemetry support a claim about work only through an exact evidence-use relation that identifies the Work occurrence, actual performer system and covering assignment, enacted method, temporal extent, and containing system, plus any method-description edition, work-to-referent relation, binding, resource-use fact, policy, or qualification value on which the receiving claim relies.

**CC-A15.1-19 (Affected referent and work scope).**
Each assertion or description about a Work occurrence designates the exact Work individual and states a direct work-to-referent relation only when the receiving use needs one. That relation must obtain independently; naming the referent in the episteme establishes neither actual change, production, delivery, acceptance, nor a universal `affected` relation. When the receiving use needs no such relation, omit it without lowering the Work occurrence.
**CC-A15.1-20 (Actual change stays neighboring).**
When the receiving claim needs actual change, identify an exact `U.Transformation` under A.3.4 and the exact work-to-change facts. Work can occur without a current transformation claim, and a no-op, evaluation, inspection, communication, or record-handling occurrence is not forced into a delta schema.
**CC-A15.1-21 (Record handling remains Work without automatic transformation).**
Copying, formatting, evaluating, or publishing records can be performed by Work individuals admitted under `U.Work` when the actual performer system, covering assignment, actual enacted method, extent, and containing system are grounded. State an affected referent, binding, or resource-use fact only through its independently obtaining relation when the receiving claim uses it. Identify any actual record or dataset transformation separately under A.3.4; a label, output record, or post-state picture does not establish it.
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
2. **Performer and assignment coverage.** Is the exact admitted `U.System` named as performer the holder of every `U.RoleAssignment` cited by an obtaining F.6 `performedUnderAssignment(W, RA)` attribution, and does each assignment's obtaining extent cover the occurrence or exact performed part attributed to that system? If not, keep the Work occurrence, performer claim, and defective assignment or attribution claim separate until A.2.1 and F.6 admit or repair them.
3. **Evaluation boundary.** Has separately performed evaluation or acceptance work applied the current criterion edition to the exact independently obtaining relations involving the Work occurrence, changed subject, measurement results, or delivered entity required by that criterion? If not, no acceptance verdict follows. If yes, keep the evaluation work, result episteme, verdict content, evidence, and acceptance relation separately governed.

These checks recover exact governing objects. They neither create one judgment-context object nor make acceptance part of work identity.

### A.15.1:11 - Common Anti-Patterns and How to Avoid Them

* **"The log is the performed occurrence."** Dumping telemetry without occurrence references (actual performer system, covering assignment, enacted method, time window, and containing system, plus any method-description edition, work-to-referent relation, binding, resource-use fact, or evidence-use relation on which the claim relies) -> **Not Work**. Recover the Work occurrence and relate the log as evidence.
* **Record-handling-as-transformation.** ETL, copying, formatting, evaluation, or publication work is treated as proof that a record or dataset changed -> Keep the grounded Work occurrence, but assert actual change only after A.3.4 identifies the transformation and an exact work-to-change fact obtains.
* **Silent cross-locality acceptance.** "Ops accepted it, so audit accepts it." -> Name each receiving criterion, evaluation work, result episteme, and acceptance relation; add F.9 only when exact local senses must be bridged.
* **Description-change-as-occurrence-change.** A MethodDescription edition swap is treated as automatically splitting or preserving Work -> State the description-selection change separately. Only when an accompanying actual history change creates an identity question for a named use should its exact continuity-policy criterion be applied; the policy revises the judgment, not the occurrence.
* **Budget on the method.** Charging costs to Method or Role -> Attribute performed resource use only through exact relations involving Work individuals; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Slice-as-episode.** A monitoring interval, telemetry window, crank-angle segment, or one-second reception trace is called an episode only because it has timestamps -> Use `TemporalPartOf_work`, an evidence relation, or a telemetry relation unless actual boundary events and the direct episode predicate establish an event-bounded fragment for a named use; add a continuity policy only if those facts leave its grouping ambiguous.
* **Episode-as-new-work by habit.** A pause, retune, or interruption is always recorded as either a new occurrence or the same one -> Preserve the boundary events first. Apply exact `workContinuityPolicyRef` only when a named use must decide the grouping; otherwise return unresolved segmentation rather than forcing either answer.
* **Method-factor-as-work-part by label.** A step, stroke, receiver component, graph node, or method-description section is treated as a work part or submethod by name -> Recover the current object: `U.Method` factor, `U.MethodDescription` constituent, `TemporalPartOf_work`, `OperationalPartOf_work`, evidence segment, mechanism material, system-component behavior, or missing-source-relation note.
* **Granularity inflation.** Every interval or trace row receives a durable work-part name -> Name the work part only when a current resource, evidence, KPI, acceptance, repair, aggregation, cross-context reliance, or source-relation return use hangs on it.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> recover the exact `B.1.4` temporal aggregation and cite its policy per KPI.
* **Double-count in overlaps.** Summing child and parent resource facts as one ledger -> recover the `B.1.6` aggregation claim and apply its exact overlap or deduplication policy.

### A.15.1:12 - Existing work-log repair applications

1. **Recover occurrence assertions.** For existing logs, identify the independently grounded Work occurrence and write an assertion or description that cites its designator, each actual performer system, the covering assignment and any explicit F.6 attribution, actual `enactsMethod`, extent, and containing system. Add optional `methodDescriptionRef` and only those independently obtaining work-to-referent, binding, and resource-use relations on which the receiving claim relies. Do not create Work by creating a record.
2. **Recover the work-judgment basis.** Name the direct occurrence facts first. Add exact `workContinuityPolicyRef`, effective reference scheme, scope, or qualification window only when the current identity, episode, retry, resumption, or aggregation judgment needs a branch criterion. Keep any MethodDescription edition, aggregation policy, criterion, and evidence-use relation outside the Work.
3. **Record a continuity policy only for an actual ambiguity.** Cite exact `workContinuityPolicyRef` and its named use when an interruption, resumption, replacement, switch, or composite boundary could support more than one segmentation. If direct facts already close a simple uninterrupted case, omit the policy.
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

`U.Work` is retained as the admitted kind for dated Work occurrences because performer system, role assignment, method, method description, work plan, affected entity, actual change, evaluation-result episteme, delivered entity, and downstream effect are different FPF objects. One Work individual is the world-side occurrence; each actual performer is an admitted `U.System` acting under an exact obtaining `U.RoleAssignment`, and an assertion or description about the work is a separate episteme. The same wording in a source episteme, publication occurrence, method description, or work plan can point to several of these objects, but performed-work claims need occurrence grounding, temporal bounds, actual performer system, covering assignment, enacted method, and containing system rather than a convenient method, assignment, plan, affected-object, or delta label. Add direct work-to-referent, binding, resource-use, or change facts only when their own relations obtain. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local separations: `U.Work` is the admitted kind; one Work individual is a world-side dated occurrence; each actual performer is an admitted `U.System`; the exact obtaining `U.RoleAssignment` states the role under which that system performs; and an assertion or description about the occurrence is a separate `U.Episteme`. The occurrence has exact method, temporal, and containing-system relations; work-to-referent, binding, and resource-use relations are added only when they independently obtain. Neighboring change, evaluation, evidence, production, delivery, and acceptance claims remain separate. Historical occurrence modeling is used as lineage only when a current practice still needs those distinctions.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they designate independently grounded Work individuals and make actual performer systems, covering role assignments, enacted method, temporal extent, and containing system recoverable, together with any involved-object, binding, resource-use, interpretation, or policy relation on which the receiving claim relies. | Treating telemetry or event rows alone as Work occurrences or as membership evidence for `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry can support, replay, measure, or diagnose a claim about work, but the occurrence still needs its actual performer system, covering assignment, enacted method, temporal extent, and containing system. It needs an affected-referent, binding, or resource-use fact only when the receiving claim relies on that independently obtaining relation. | Counting trace, metric, or log existence as the performed work, a result, or dominance evidence without the governing evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Assertions or descriptions about Work cite exact evidence-provenance relations and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | A.15.1 supplies exact Work intervals, parts, and performed resource-use facts; `B.1.4` governs temporal aggregation and `B.1.6` governs work-resource aggregation, each with its exact policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |

### A.15.1:14 - Relations

* **Builds on:** A.1 Holonic Foundation; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`; C.2.1 for episteme edition and effective `U.ReferenceScheme`; A.2.6 for claim scope; and C.27.TA for temporal qualification. A.1.1 enters only when a separately identified `BoundedModelUseStructure` changes the receiving work claim.
* **Coordinates with:** A.15 for Role-Method-Work alignment; A.6.1 and the exact direct relation patterns for actual bindings and participants; A.3.4 for independently identified actual transformations; A.15.PROD for local production-work, entity-identity-inception, and production-completion claims; B.1.4 for temporal aggregation and optional `Gamma_time`; B.1.6 for work-resource aggregation, ledger discipline, and optional `Gamma_work`; `E.10` and `E.10.ARCH` for work-wording recovery; `A.10`, `B.3`, `E.17`, and `A.15.4` for evidence, assurance, publication-use, or appearance-based reliance repair; `A.15.5` for readiness before performed work; and `C.32.P2S` for carry-through. A permission, gate, result, production, delivery, or acceptance claim remains independent of Work identity.
* **Informs:** reporting and KPI patterns; assurance and evidence patterns that use Work as the reference occurrence; and scheduling patterns that compare exact `U.WorkPlan` claims with independently identified Work occurrences admitted under `U.Work`.

### A.15.1:15 - Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Separation aid:** Who performs? **System**. Under which held role? **RoleAssignment**. Can? **Capability**. How? **Method**. Which account of the method? **MethodDescription**. Did it happen? **Work**.
* **Three-question result check:** Did the work occur? What separate result or consequence is claimed? Who judged or accepted what, by which criterion and evidence? Use §4.6 and stop after the last question the receiving use actually asks.
* **Roll-ups:** A.15.1 supplies exact Work refs, intervals, parts, and performed resource-use facts; cite `B.1.4` for temporal aggregates and `B.1.6` for resource ledgers, each with its declared policy.
* **Episodes vs retries:** record end, interruption, resumption, and later work-entry facts first; add a continuity policy only when a named use still has more than one defensible grouping.
* **Resource honesty:** relate performed resource use to exact Work individuals through separately obtaining resource-use relations; route any result or consequence through the one matching §4.6 row.

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, identify one Work individual admitted under `U.Work`, then recover each actual performer `U.System`, the exact obtaining `U.RoleAssignment` under which it performed and any explicit F.6 attribution, plus the separately obtaining enacted-method, temporal, and containing-system relations. Add binding, resource-use, or work-to-referent relations only when the receiving use needs them. When P2W continues into a result or consequence claim, select the exact §4.6 row and carry that object under its own governor.

A Work occurrence may be designated by an episteme that also cites a `U.WorkPlan`, exact A.15.3 planned-filling claim, or prior readiness claim as a baseline. State every actual participant, parameter, premise, operation argument or result, resource use, and work-to-referent fact only through its obtaining direct relation or exact A.6.1 application binding. Do not copy a result or consequence into Work; follow the concrete §4.6 route.

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate assertion that an individual is Work admitted under `U.Work` when the occurrence designator, actual performer system, covering assignment and any explicit F.6 attribution, actual enacted method, temporal extent, or `executedWithin` relation cannot be recovered. If the receiving claim additionally relies on a work-to-referent, direct-relation or A.6.1 binding, or resource-use fact, lower that dependent claim when its independently obtaining relation cannot be recovered; do not lower the Work occurrence merely because an unneeded affected referent or delta is absent. Require a continuity-policy basis only when an identity, episode, retry, resumption, or aggregation claim actually depends on ambiguous segmentation. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, unresolved-segmentation note, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated Work occurrence or gratuitous work part.

Repair the work assertion or description when a subsequent source changes the resolved temporal extent, actual performer system, covering assignment or F.6 attribution, actual enacted method, selected method-description reference, direct binding, resource-use claim, work-to-referent relation, containing system, or work-part relation. Reidentify only when the direct A.15.1 boundary rules or an exact policy current to a named ambiguous use require it. A changed continuity-policy edition repairs the dependent identity, episode, retry, resumption, or aggregation judgment; it does not rewrite the Work occurrence or its actual history. Repair a result or consequence through the one matching §4.6 owner rather than editing Work.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a Work-occurrence reference only when the receiving claim actually depends on that occurrence.

### A.15.1:End

