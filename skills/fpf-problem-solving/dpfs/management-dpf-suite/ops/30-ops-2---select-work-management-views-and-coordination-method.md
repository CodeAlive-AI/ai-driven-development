## OPS.2 - Select Work-Management Views and Coordination Methods

> **Status:** Stable


### OPS.2:0 - Use This When

Use this pattern when the same continuing Work is being called a project, process, case, workflow, queue, programme, or control loop and that choice changes coordination. Enter when one view hides a decision that another exposes: a process map may not show a permissible next action for an exceptional case, a project plan hides recurring service, a case file hides aggregate load, a queue hides commitments and subject state, or a loop diagram hides the operating account.

The first useful move is a question-to-view decision:

> For decision `D` about subjects `S` at grain `G`, use view `V` and coordination Method `M` under conditions `C`; relate it to views `V2...` through these subject correspondences, commitments, handoffs, coexistence rules, and stop conditions.

This result need not select one permanent mode. It may choose one view, several compatible views, or no new view when the existing coordination already answers the question.

Recognition is cheap: enter when practitioners disagree about “what kind of Work this is” or cannot answer a current question from the existing view. Assurance is heavier: selected structures, direct relations, Work, Methods, planning claims, control claims, rates, authority, safety, and evidence keep their own FPF or specialist tests.

Do not use OPS.2 to classify Work into a universal natural kind, infer performed Work from a plan, select a structure by diagram appearance, or prescribe one lifecycle. If the question concerns only the identity of an already selected structure, mathematical lens, or architecture view, use `A.22`, `C.29`, or `C.30.LCA` directly.

#### OPS.2:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| Work | Actual dated activity under its governing FPF pattern, including the enacted Method. Intended activity belongs to a plan or proposal. A management view describes or coordinates Work; it does not create another Work occurrence. |
| viewpoint question | The exact question a view must answer for a named user and decision, such as dates and allocation, repeatability, changing subject state, aggregate waiting, or feedback and rate separation. |
| Work-management mode | The selected use of one or more descriptions and coordination Methods for the current Work and questions. It is a decision result, not a Work kind or maturity stage. |
| project view | A description emphasizing a time-bounded undertaking, commitments, intended results, decisions, dates, WorkPlan content, allocation, dependencies, and closure conditions. |
| programme view | A description coordinating several projects or change commitments and their dependencies or intended contributions. The label does not create a containing System, benefit, or authority. |
| process view | A description emphasizing a recurring Method, inputs, results, repeated order or constraints, and control points. It does not prove that every occurrence follows the description. |
| case view | A description organized around a changing subject, current facts, commitments, discretionary or constrained next Work, exceptions, and closure conditions. The case is not its file. |
| queueing view | A description of eligible items, membership, order or service relation, waiting, arrival, departure, resource demand, and policy for one receiving question. The queue is not a board column. |
| control-structure view | A current FPF description of one selected control structure and its actual observation, actuation, reference, supervision, feedback, and rate-relevant relations. It is conditional, not an Operations default. |
| coordination Method | A reusable way of coordinating the Work under stated conditions. A view can expose what the Method needs without being that Method. |
| mixed-mode decision | An explicit co-use account stating subject correspondence, scope and grain, commitments, handoff or coexistence conditions, decision rules, conflicts, and stops among unlike views and Methods. |

### OPS.2:1 - Problem Frame

Project, process, and case management are often offered as competing descriptions of reality. Operations practice then chooses a tool or school and lets its default object model decide what exists. Yet one release operation can have a project for platform migration, a recurring process for validation, cases for field incidents, a queue for a scarce test rig, and a control view for observation and intervention at unlike rates.

These views are useful when they supply information needed by the receiving decision. They need not be isomorphic. Select each for the question it can answer and preserve correspondence where decisions cross them.

### OPS.2:2 - Problem

One-mode selection loses information. A process-only account can force evolving cases through a route whose next Work depends on new facts. A case-only account can hide repeatable validation and shared capacity. A project-only account can treat continuing service as a temporary deliverable. A queue-only account can optimize waiting while breaking a commitment. A control-only account can turn observation and actuation into a complete management Method.

The opposite failure is an ungoverned hybrid: every tool and view is kept, but subjects, grains, states, and decisions disagree. Participants spend more effort reconciling records than coordinating Work.

### OPS.2:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar methods | Teams can act quickly with a known project or process Method, while familiarity can hide the wrong question. |
| Several truths | Unlike views can all be useful, while their subjects and state claims may conflict. |
| Runtime discretion | Some Work can be planned, while new facts require case-responsive continuation. |
| Aggregate coordination | Individual cases need attention, while shared queues and resources require a population view. |
| Control language | Feedback and rate distinctions can change coordination, while a loop diagram can overclaim stability, safety, or authority. |
| Affordability | A full multi-model account is expensive, while one view may omit the next decision. |

### OPS.2:4 - Solution

Select views and coordination Methods from the operating questions they must answer. Preserve Work identity across views, select actual structures independently, and combine only those views whose distinct information changes the decision.

#### OPS.2:4.1 - Pattern-Use Unfolding

1. **Recover the operating input.** Start from the OPS.1 operating System, continuing result, commitments, subjects, units, horizon, and decision. Stop if the mode question is only a label preference.
2. **List the viewpoint questions.** Name each user, decision, subject, grain, horizon, and missing information. Separate planning, recurring execution, case continuation, aggregate waiting/capacity, and control questions.
3. **Generate serious view candidates.** Include project or programme, process, case, queueing, and control-structure views only where their questions are current. Include the incumbent as the no-change option, and a simpler view when it is a plausible alternative.
4. **Compare fit to the current Work.** Examine the conditions that distinguish the serious candidates: for example, predictability, recurrence, subject identity, decision latency, runtime discretion, plannability, shared-resource coupling, exception frequency, evidence refresh or authority. Reuse an adequate existing selection when its grounds still hold.
5. **Select the coordination Method separately.** Recover the actual rule or reusable way currently used: what fact permits a start or continuation, who applies it, what it orders, what evidence it needs and when it stops. Use `OPS.17:4.1`–`OPS.17:4.4` when a real alternative or combination must be chosen. Compare the incumbent with that alternative at the same operating decision and include application and maintenance effort. Retain the incumbent when adequate. A notation, board, model or view alone is not this rule.
6. **Qualify a selected structure when needed.** Use `A.22` when the decision needs a claim about a selected transformation-flow, queue/resource-dependency, commitment, event, case-state, control or other structure. Preserve its actual constituents and relations. A mathematical graph or diagram represents that subject under its own correspondence conditions.
7. **Use the control branch conditionally.** When observation, decision, influence or their timing changes coordination, use `C.43` to recover the actual participants, information, choice, realization and return. That ordinary account can suffice. Use `A.22` and `C.30.LCA` when a selected control structure and view are needed; use `B.2.5` only for an obtaining two-sided supervisor relation and `C.27.TA`, `C.27` or `A.3.3` for the exact rate, temporal or dynamics claim. Stop without a control account when no such relation changes the decision.
8. **Compose views explicitly.** State the shared subjects, relevant grain and horizon, state and evidence correspondence, governing commitments, receiving decisions, handoff and update rules. If Methods coexist, settle which rule governs a disputed permission, ordering, resource or stop decision; retain the other rule where its conditions still hold. Use the existing `OPS.17:4.4` composition result where current. An unresolved conflict returns to its authority; a “hybrid” label does not settle it.
9. **Examine a consequential change when its handling is unresolved.** For a new or changed rule or an uncertain correspondence, change an input the rule uses and apply the resulting permitted action or stop. Identify unaffected subwork: a new fact may retire one exception without changing the recurring procedure, case identity or every view. Reuse a current qualifying replay or operating observation when it already answers this question; communicate what the next participant can still rely on.
10. **Return the selection.** State the views and coordination Methods to use, the grounds for a material rejection, and any unresolved correspondence or needed input. A sufficient existing selection can finish the decision. Identify revision conditions when the selection will be maintained or reused.

#### OPS.2:4.2 - Carry the Result

Use the current coordination account when adequate. The following content is needed only for the questions and combinations selected above; retain it in a record when the receiving use or governing requirement needs one.

| Result position | Content for the receiving use |
| --- | --- |
| use boundary | Users, decisions, subjects, grains, horizons, and useful stop. |
| viewpoint questions | The planning, recurrence, case-state, aggregate waiting/capacity, control, or other exact questions that remain current. |
| candidate views | Incumbent (no change), serious alternatives, selection reasons, rejected uses, and missing evidence. |
| coordination Methods | Named Methods, applicability, burden, evidence, authority, and stops; no identity with the view or tool. |
| selected structures | Exact actual structures and direct relations relied on, plus representation and mathematical-lens boundaries. |
| mixed-mode correspondences | Subjects, grains, commitments, state correspondence, handoffs/coexistence, update and decision rules, conflicts, and stops. |
| control branch | Actual information, choice, influence and return needed by the operating question; a selected control view and qualified relation, rate or dynamics claims when that stronger use is needed, or the precise missing result. |
| continuation | Any still-needed subject or state-account input; revision conditions for a maintained or reused selection. |

#### OPS.2:4.3 - What Changes in Practice

The team stops asking whether Work “is” a project, process, or case. It asks which descriptions and coordination Methods answer each decision, then relates them through exact subjects and commitments. A view can be added, narrowed, or retired without retyping the Work or rebuilding every other view.

### OPS.2:5 - Archetypal Grounding — PumpWorks Mixed Operating Views

#### OPS.2:5.1 - Identify the useful views

`PumpWorks-ControlServiceOps` coordinates several unlike questions:

| Current question | Useful view | Boundary |
| --- | --- | --- |
| How should `FieldIncident-I73` continue after new field evidence? | Case view over the field installation, incident state, commitments, evidence, authority, and permissible next Work. | The ticket is a record; safety and product decisions retain their owners. |
| How is release evidence repeatedly produced and checked? | Process view of the recurring validation Method and its input/result relations. | A process description does not establish that an occurrence happened or conformed. |
| How is a time-bounded provider-platform migration coordinated? | Project and, when several projects are coordinated, programme views of commitments, WorkPlan content, decisions, allocations, and closure. | The plan is not performed Work, adoption, or benefit. |
| How is scarce rig access coordinated across eligible requests? | Queueing view over exact request membership, order/service relation, waiting, resource access, and policy. | Establish request membership, service order, and resource access for this queueing view; a board column alone does not establish them. |
| Which observations and interventions matter at unlike rates? | Conditional control-structure views for the product-side plant/controller/observer/supervisor relations and the operating-supervision relation. | FPF owns the generic structures and rate claims; the diagram is neither the account nor the Operations Method. |

The views preserve correspondences to `ReleaseCandidate-R42`, `FieldIncident-I73`, `SafetyQuestion-S19`, `ProviderChange-P8`, the test rig, commitments, evidence results, and decisions. The incident case can request a validation-process occurrence; that occurrence can consume rig capacity; its evidence can inform the weekly release decision; a platform-migration project can change provider access. None of these relations makes the views one structure.

The product-control structure has `FieldPumpInstallation-P4` as plant, `FieldTelemetryObserver-O4`, `DeployedController-C17`, and `FieldModeSupervisor-S1` only where their direct relations obtain. The operating-supervision structure has `ReleaseSupervisorTeam-S2` receive operating-state reports and return release, hold, rollback, or permitted-mode constraints to the operating System. The timing claims remain separate: sub-second product control, minute-to-hour field observation, daily incident triage, weekly release, and slower provider change. OPS.2 selects their use; it establishes no feedback closure, stability, safety, or authority.

#### OPS.2:5.2 - Choose and combine actual coordination rules

In a constructed 09:00–11:00 window, PumpWorks permits at most two active engineering work packages under its existing staffing and recovery policy. T8 is already running. Incident diagnosis I73-D and the older provider-preparation package P8-P are both ready and permitted; both would need engineer E18. I73 has a field-contact window closing at 11:00, while P8-P can wait until the afternoon without violating a promise. The recurring T8 validation procedure is adequate and remains unchanged.

The incumbent rule starts the oldest ready package when a slot and performer are free. Its virtue is predictable order with little coordination. The incident rule allows a ready package to precede that order when a named response window would otherwise be lost, provided the incident lead authorizes the exception, the resource owner confirms it, displaced work remains feasible and the active limit is respected. These are supplied local rules, not universal properties of either a case view or Kanban.

Using `OPS.17:4.2`–`OPS.17:4.4`, the coordinator compares the two rules at this decision. Starting the noninterruptible two-hour P8-P would remove E18 from the incident's remaining evidence-and-response interval. The exception instead starts I73-D, defers P8-P to an authorized afternoon review and leaves T8 running. Its extra cost is one bounded confirmation and a follow-up on the deferred package; it avoids no demonstrated cost outside this window. The composition says exactly: readiness and permission govern eligibility, the incident exception governs order among eligible packages, the two-package limit still governs starts, and validation controls its own safe completion. No extra active slot is created.

At 09:50 the field contact becomes unavailable. The exception no longer justifies reserving E18 for live verification. The incident remains a case with a partial diagnostic result, but the live continuation returns for access and permission. T8's completed evidence and the independently permitted T9 validation remain usable; the coordinator reconsiders ready demand without reopening every view. `OPS.5:5.1`, `OPS.6:5.1` and `OPS.7:5.1` develop the admission, observation and commitment decisions for this same constructed matter. They can also be used independently.

The lesson is not to install all five views. It is to keep the existing process where its rule fits and add the case, queue or commitment relation only for a decision it changes.

Reopen the mode decision when a new subject cannot be related across views, a plan repeatedly fails after new facts, queue policy changes a commitment, a control relation becomes decisive, or maintaining one view costs more than the decision value it supplies.

### OPS.2:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| one-true-kind bias | Work is declared inherently project, process, or case. | Recover the question, subject, and selected view; preserve Work identity. |
| tool ontology bias | The tracker schema decides which objects and states exist. | Identify subjects and relations first; treat the schema as representation. |
| hybrid-label bias | “Hybrid” hides missing correspondences and decision rules. | State subject/grain mappings, commitments, coexistence, conflicts, and stops. |
| process-normality bias | Exceptions are forced back into the designed route. | Use a case view when new facts change permissible next Work. |
| project-temporariness bias | Continuing operation is treated as a project deliverable. | Keep the time-bounded change view separate from ongoing service Work. |
| loop-as-method bias | A feedback diagram becomes the whole Operations Method. | Use the conditional FPF control branch and retain the operating decision separately. |

### OPS.2:7 - Conformance Checklist

- [ ] The decision begins with an OPS.1 operating focus and exact viewpoint questions.
- [ ] Work identity is preserved across every selected view.
- [ ] Project, programme, process, case, queueing, and control are selected for questions rather than declared natural Work kinds.
- [ ] Coordination Methods, views, actual structures, diagrams, and tools remain distinct.
- [ ] Selection uses the conditions that distinguish the serious candidates and reuses an adequate current answer.
- [ ] Every mixed-mode use states subject and grain correspondence, commitments, coexistence or handoff, update and decision rules, conflicts, and stops.
- [ ] The control branch names actual participants and direct relations only where they obtain and returns rate/dynamics claims to their FPF owners.
- [ ] A changed case or cross-view probe can expose a failed selection or correspondence.
- [ ] Material rejection grounds, unresolved gaps and any required continuation are explicit; maintained or reused selections retain their revision conditions.

### OPS.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everything is a process.” | Identify changing subjects and ask whether discretionary or constrained case continuation is needed. |
| “Every initiative is a project.” | Separate time-bounded change commitments from recurring and continuing operation. |
| “Case management means no process.” | Retain reusable Methods and recurring subwork while letting subject state govern permissible next Work. |
| “Put all work in one queue.” | Name eligibility, service/resource relation, commitment effects, and the subjects that must remain separate. |
| “Use one integrated model.” | Preserve non-isomorphic views and relate only the claims the decision consumes. |
| “The loop proves control.” | Recover actual relations and use direct rate, dynamics, evidence, safety, and assurance patterns. |

### OPS.2:9 - Consequences

The pattern lets an operation combine familiar management practices without letting any one practice define the ontology. It makes view debt visible: missing correspondences, duplicated state, stale mappings, and coordination cost become explicit decision inputs.

The cost is maintaining subject and state correspondence where several views are genuinely useful. Some integrations are rejected because the views answer no different question or cannot preserve identity and commitments reliably.

### OPS.2:10 - Rationale

Different views earn their place by changing a decision. Project, process, case, queueing, and control descriptions foreground unlike structures, times, and questions. Treating them as views preserves their strengths and avoids a false taxonomy of Work. Explicit mixed-mode rules then make coexistence testable without requiring one universal model.

### OPS.2:11 - SoTA-Echoing

The question is how to coordinate evolving case work with recurring procedures and shared resources. A strong alternative already integrates them. [CMMN 1.1, §4.1 and §5.4.9](https://www.omg.org/spec/CMMN/1.1/PDF) supports runtime case planning, procedural subwork and authorized planning roles. An adaptive project arrangement can likewise revise its plan when facts change. Neither should be represented as an inflexible taxonomy.

At PumpWorks, such an arrangement can retain T8's procedure while a case manager selects incident diagnosis. If its case file, resource policy and decision rights also settle the shared E18 allocation and preserve the field-contact window, use it unchanged. OPS adds no gain by displaying the same decision in more tools. The remaining question arises when the case manager's chosen action, the queue's oldest-ready rule and the resource owner's active limit produce incompatible starts. Sections 4.1.5 and 4.1.8 connect to OPS.17 to recover and compose the actual rules; section 5.2 makes the incident exception govern order without overriding eligibility or increasing the limit. The changed contact condition retires that exception while recurring validation survives.

This synthesis costs rule recovery, agreement on the one disputed decision, mapping of the shared subject and evidence, and maintenance of that correspondence. It can be more expensive than using a capable integrated case model, especially when one owner already maintains all relevant policies. Its conditional gain is avoiding an unsupported cross-view action when those policies were separately governed. Stop adding views when their answers cannot change a decision; retire a duplicate view rather than paying its synchronization cost.

OPS adopts CMMN's coexistence of planned and discretionary work, and the DCR tradition's explicit conditions and responses, without claiming that either source automatically gives domain evidence or external authority. The [Kanban Guide](https://kanbanguides.org/the-kanban-guide/2025.5/) supplies the bounded flow-policy contribution. FPF `C.43` supplies the ordinary control account; `A.22`, `C.29`, `C.30.LCA` and the applicable temporal patterns govern selected structures, mathematical representations and stronger control claims. Reopen when the integrated incumbent already settles the same conflicts more simply, or a new case defeats a relied-on composition rule.

### OPS.2:12 - Relations

- `OPS.1` supplies the operating System, continuing result, commitments, subjects, units, horizon, and control concern.
- `C.43` supplies the ordinary control account. `A.22` governs selected structures; `C.29` governs mathematical-lens use; `C.30.LCA`, `B.2.5`, `C.27.TA`, `C.27` and `A.3.3` govern the corresponding view, supervisor, rate, temporal and dynamics claims when needed.
- `OPS.3` receives selected subjects, grains, view correspondences, direct-relation questions, and representation gaps. `OPS.4` receives the selected participant views and their state-correspondence obligations.
- `OPS.5` later consumes the selected coordination form for admission. `OPS.6` later consumes case-state and continuation needs. `OPS.8`–`OPS.11` later consume queue, constraint, capacity, and interacting-structure questions without making those structures values of one mode taxonomy.
- Project Management, case management, BPM, Kanban, SRE, and other practices offer candidate coordination Methods. Select a particular Method using its applicability conditions and evidence.

### OPS.2:End
