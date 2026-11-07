## SYSE.20 - Reconcile Overlapping Engineering Work and Required Order

> **Status:** Stable

### SYSE.20:0 - Use This When

Use this pattern when engineering Work overlaps to shorten feedback, but some results, configurations, or safety
conditions still require a particular order. A local improvement—for example faster simulation, earlier review,
or self-service tooling—may delay or weaken the integrated engineering result.

Begin with that result and the decision that will use it. For an actual arrangement, name the performed Work
and the Methods it enacts. For a proposed arrangement, name the planned operations and Methods in its WorkPlan
or intended-use account. In either case, identify the direct relations that matter. Do not infer those relations
from a lifecycle diagram, team chart, toolchain, or list of disciplines.

The first useful result explains which contributions may proceed together, what each must wait for, and
whether the resulting arrangement can deliver the required engineering result. It carries two distinguishable
epistemic contributions: a Method-and-Work architecture account explaining the dependencies, alternatives and
moved burdens, and a bounded decision record stating the authorized outcome. They can share one short account.
An authorized Agent performs the decision Work; later Agents perform implementation and test Work. The account,
the decision and an actually changed arrangement are different results.

The intended reader can obtain the relevant engineering Methods, interpret configuration and evidence
conditions, and consult the people responsible for specialized operations. This pattern teaches construction
of their feasible arrangement. It does not supply an unknown curing time, simulation qualification or safety
permission. Recover those particular inputs from their responsible source.

If a known applicable dependency already answers the question and no arrangement needs to change, apply it
directly. If only one missing fact prevents a choice, obtaining that fact can be sufficient; there is no need
to build a new lifecycle description.

Use `C.32.MWA` when the main difficulty is synthesizing several practice structures in any domain. Use this
pattern for the engineering specialization: overlapping contributions to an engineered System create a conflict
among constraints such as configuration identity, integration, evidence, platform availability, or specialist
assurance, and the project must decide whether and how to change the arrangement. Use Operations Management when the main result concerns continuing flow, queues, or throughput. Use
Method Engineering when the reusable Method itself is the subject being developed. Use `SYSE.15` first when the
project still lacks a usable account of its engineering Methods.

#### SYSE.20:0.1 - Precision Restoration

| Name in this pattern | What it denotes |
| --- | --- |
| engineering result at risk | A named result whose usability can change with the Work arrangement—for example an integration recommendation, accepted configuration, verified interface claim, released design, or usable service condition. State its kind and the decision or Work that uses it. |
| Method-and-Work architecture account | An episteme describing the selected Method and Work structures, their direct relations, the conflict, alternatives, and moved burdens for one decision. It is a description of the arrangement. |
| Work overlap | A temporal relation between admitted Work occurrences whose extents intersect under a named temporal reference. Overlap alone establishes neither Work parthood nor Method composition. |
| required order | A direct dependency that makes one occurrence or condition precede another for a named use—for example a temporal meet, transformation completion, result-use guard, configuration release, or authority condition. State the governing relation. |
| Method unfolding | An organization of positions, branches, returns, or stops inside one identified reusable Method. Dated Work order supplies evidence about Work; it establishes a Method unfolding only when the Method structure is grounded separately. |
| enabling or provider Work | Separately admitted Work that changes an enabling System or supplies a needed result or service. State its dependency on engineering Work; establish any Work-part relation separately. |
| capability-development Work | Work intended to change an Agent's capability for later Work. Its earlier occurrence establishes temporal order; capability change needs its own evidence. |
| moved burden | A burden that decreases in one scope and increases in another—for example, a material cost, delay, evidence need, dependency, risk exposure, or loss of control. Name the actual burden and receiving scope. |
| reconfiguration alternative | Possible-future content proposing a change to one or more named relations in the engineering arrangement. |
| bounded reconfiguration decision record | An episteme recording the authorized bounded choice outcome for the named result, configuration, use and time window, with its grounds and next question. A selected change can be supplied to later implementation Work; rejection, further inquiry and rerouting retain their own outcomes. |

An Agent performs Work. Systems can participate as, for example, equipment, a platform, the engineered subject,
or part of its environment. Models are epistemes used in Work. State each direct relation, and use the more
specific Agent wording when agency matters to the claim.

### SYSE.20:1 - Problem Frame

Engineering does not normally proceed as one total sequence. Modeling can overlap implementation, evidence review
can begin before a test finishes, and provider Work can restore a service while project Work continues. At the
same time, some dependencies are real: a test uses a released rig configuration; a simulation result refers to a
particular model and solver configuration; a release decision waits for admitted evidence.

Several structures can therefore matter to one decision. Common examples are:

- a Method structure showing composition or an unfolding;
- a Work structure showing parthood, overlap, and required order;
- a subject structure showing the engineered System and enabling Systems;
- a representation-use structure showing which models and evidence refer to which configuration; and
- provider, capability-development, or cultural-change structures when they change the decision.

Select structures that expose a decision-relevant relation or conflict, using these examples as starting points.
Their descriptions can correspond without lining up one-for-one.

### SYSE.20:2 - Problem

Three recurring errors make the engineering arrangement hard to change.

First, a sequence-only account serializes Work that could overlap and postpones integration feedback. Second, an
“everything is concurrent” account loses guards and result dependencies. Third, a diagram turns unlike relations
into levels: a Work part, a model use, provider Work, and earlier training appear as one stack merely because they
occupy different rows.

Local optimization then hides the project result. Faster code generation can increase review and integration
delay. More simulation can strengthen a claim about the wrong configuration. A self-service platform can shorten
setup while moving maintenance and assurance burdens to a provider. The local metric improves, but the receiving
engineering decision gains no usable result.

### SYSE.20:3 - Forces

The recurring tensions are:

- Useful overlap shortens feedback, while stale configuration and provisional evidence can propagate through it.
- Required order protects identity, safety, and authority, while total serialization delays learning.
- Several Methods can be enacted together, while co-use does not by itself compose one larger Method.
- Shared models can improve correspondence, while every model preserves some distinctions and loses others.
- Provider services can reduce local effort, while availability, compatibility, and maintenance remain project
  concerns when the engineering result depends on them.
- A project can choose a new arrangement, while cultural continuation depends on later recognition, enactment,
  selection, and retention.
- More views can reveal a hidden conflict, while views that cannot change the decision add reading and maintenance
  cost.

### SYSE.20:4 - Solution

Describe the current engineering arrangement through the structures that change the decision. State each
direct relation, expose the conflict and moved burdens, generate materially different reconfigurations, and let an
authorized Agent decide whether and how to change the arrangement and return the actual bounded outcome.

#### SYSE.20:4.1 - Pattern-Use Unfolding

The reusable Method has the following eight recurring moves. They organize use of this pattern; they do not claim that
the project's engineering Work occurs as eight consecutive stages.

1. **Decision boundary.** The Agent names the engineering result at risk, its configuration and intended use, the
   decision that needs it, the time window, and the authority for changing the Work arrangement.
2. **Obtaining Work and Methods.** The Agent identifies representative performed Work with its extent, performing
   Agents, assignments when attribution matters, and enacted Methods. A possible-future arrangement instead uses
   a WorkPlan or intended-use description and names the later Work that would test it.
3. **Direct Work relations.** The Agent states every needed Work relation—for example parthood, temporal overlap,
   required order, result use, or service dependency—through its governing pattern. A common interval is evidence
   only for overlap; a Work part supplies no Method-part claim.
4. **Decision-relevant companion structures.** Other structures—for example subject, representation,
   configuration, provider, capability, or cultural structures—are added only when one changes the decision. Each
   description states its subject, use, important correspondences, and losses.
5. **Conflict and moved burden.** The Agent identifies the incompatible results or constraints and the engineering
   consequence. Every claimed local gain names any material burden moved to another Agent, System, decision, or
   time interval.
6. **Alternatives.** The Agent develops a finite current option set whose members change at least one named
   relation. Keep the feasible incumbent.
7. **Choice.** The authorized Agent uses `C.11` or a domain decision Method to compare the fixed option set on one
   stated basis and choice rule. Record the actual outcome: a selected alternative or retained tie-set with its
   grounds; rejection of the current set with its reason; a chosen next probe and the comparison defect it would
   resolve; or rerouting to a named receiving question. Retain accepted losses, preserved constraints, missing
   evidence and the reopen condition as they apply to that outcome.
8. **Realization and return.** When implementation is selected, assigned Agents perform separately identified
   implementation Work. Later representative Work supplies observations about the changed arrangement and the
   engineered result. An authorized Agent uses those observations to preserve, narrow, or reopen the decision.
   A different choice outcome continues through its own named question or Work.

For a claimed constituent connection, use B.1.5.EW to select a moment and recover what larger work is being performed through the action. In a constructed requirement-verification trial, acquiring a sample can be part of checking a response requirement, within an ongoing acceptance exercise. A transient-response requirement may rule out an acquisition setting adequate for a steady reading. If obtaining the needed samples monopolizes the shared instrument and defeats a second commitment, this pattern compares changed windows, support or trial arrangements. Keep instrument skill, measurement design and whole-trial coordination visible; satisfying one does not establish the other two. Use B.1.5.RS if the proposal instead replaces a constituent Method and must preserve several receiving uses.

##### SYSE.20:4.1.1 - Derive the dependencies from the result that must become usable

Start at the receiving use and work backward. For an integration recommendation, ask what must be true of
the assembled evidence before the lead can make it. Follow each needed result to the operation that produces
it, then ask its performer which inputs are needed to start, to continue and to finish that operation.
These can differ. A reviewer can inspect the test procedure before measurements arrive but cannot conclude
that the measured response meets the requirement before obtaining those measurements.

Recover a dependency through its reason. A test waits for rig release because the selected test Method
requires that physical and authorized condition. A simulation waits for a model edition when its qualifying
claim depends on that edition. Two otherwise independent tasks may wait for the same specialist or instrument.
Department names and adjacent boxes in a lifecycle drawing supply none of these reasons. Use performed Work
and its records to recover the actual arrangement; use the performers' intended operations and their qualified
input needs for a prospective arrangement. Compare the two when the plan and actual practice disagree.

Distinguish the direct input from an indirect influence. If a corrected model supplies simulation inputs and the simulation informs test settings,
retain those intermediate uses before deciding what the model change affects in the test. A Dependency Structure Matrix can help recover and sequence many such relations; use its
construction and sequencing methods named in :11 when coupling makes a short account inadequate. A matrix
whose relation or direction is unclear cannot settle the order.

At each receiving operation, recover only the conditions that change its use: the relevant configuration,
meaning, physical state, precision, authority or availability. A version identifier helps locate a result;
it does not establish its compatibility. Use SYSE.10 for evidence and model-use qualification, SYSE.13 for
configuration correspondence and SYSE.14 for a release or transition decision. Preserve a qualified result
already supplied by those Methods.

Stop refining when the next arrangement decision can be made. If no one can supply an operation's input need
or duration well enough to distinguish the options, that is the next engineering inquiry. Adding more arrows
does not supply the missing knowledge.

##### SYSE.20:4.1.2 - Separate early useful work from the use that needs a final result

For a proposed overlap, identify the work to begin and the information it would use. Split independent
preparation from the part that depends on the unfinished result. Preparing a test script against an agreed
interface may proceed while a model is corrected; making the final performance judgement still needs the
qualified evidence. This split changes the work arrangement only if the Method permits the preparation to
remain useful and the later join includes what was postponed.

When early work uses preliminary values, recover what can change and how the receiving operation responds.
A qualified engineering model, interface envelope or prior evidence may show that some changes leave the
result valid, require a bounded correction, or invalidate it. Name that basis and the affected work. Without
it, the word “provisional” provides no reason to expect reuse. A speculative run can still be useful for
learning, but compare its learning value and possible repetition separately from a qualifying run.

Choose between starting, waiting and obtaining a discriminating result. Starting is useful when its output
can reach the receiving use under the allowed changes, or when the learning warrants its expected discarded
work. Waiting is appropriate when the final input is near and proceeding would commit expensive or irreversible
work on an unsupported premise. A small model comparison, fit trial or supplier answer is appropriate when
it can settle the particular uncertainty soon enough to affect this choice. Keep its time and support in the
same comparison. Unknown change frequency or rework cost remains unknown; do not fabricate an expected-value
calculation.

Agree how an input change reaches its consumers, who interprets its consequence and what must be reconciled
before the final use. For a permitted envelope, a change inside it can retain the supported result; a change
outside it returns to the affected operation and its receivers. The reason for that distinction must remain
available to the receiving engineer. Updating a status label cannot replace the reconciliation.

Physical duration, necessary sequence and authority can constrain this choice independently. A quicker
calculation cannot shorten a qualified thermal dwell, and early review cannot issue a permission whose
required evidence is absent. Negotiate a changed condition with its holder when the condition itself is
questioned; until then, construct alternatives that respect it.

##### SYSE.20:4.1.3 - Construct alternatives by changing the obstructing relation

Use the recovered conflict to generate an arrangement, rather than choosing a fashionable process label.
Trace the result backward to its limiting contribution, change a relation that could remove that limitation,
and follow the changed arrangement forward to the same receiving result. The following moves answer different
causes; use the relevant one or a supported combination.

| What prevents useful progress | Construction to try | What must still be supplied |
| --- | --- | --- |
| An entire activity waits although only its final inference needs the late input | Separate preparation or independent work from the final join; overlap the former | A valid split, the later interpretation and any repeated work |
| Early work is repeatedly invalidated by an upstream change | Agree a qualified interface or change envelope, shorten the interval to usable feedback, or postpone the sensitive portion | A professional basis for the envelope and a response when it is exceeded |
| Several contributions need one scarce resource | Reorder their use, reserve compatible windows, reduce the competing demand, or obtain qualified additional capacity | Setup, access, recovery and the consequences for displaced commitments |
| A provider condition blocks otherwise ready engineering work | Compare waiting, a qualified alternative service and a changed engineering Method | Compatibility, real availability, authority and continuing support for the alternative |
| Two design contributions depend on one another | Begin from an explicit provisional assumption, perform an informative iteration and reconcile both results | The assumption's permitted use, feedback, acceptance or revision condition, and a stopping decision |
| A local acceleration only moves the queue | Change the limiting receiving contribution or retain the incumbent | A gain at the integrated result and the burdens borne elsewhere |

For a feedback cycle, placing one activity first does not remove the reciprocal dependency. A DSM sequencing
method can identify the coupled group; its tearing method makes the starting assumptions explicit. Retain
those assumptions in the engineering reasoning and obtain the feedback that can confirm or revise them.
Choose an iteration whose result can change the coupled decision. Stop, narrow the question or change the
arrangement when another iteration cannot justify its cost or cannot meet the required use.

A proposed support replacement needs more than an available tool. Identify the compatible configuration,
qualified performer, access, service window and continuing responsibility. If the laboratory inherits
validation or maintenance from a provider, those are contributions to obtain, not consequences erased by
the word “local”. Use SYSE.12 when that support arrangement itself requires design.

Keep the feasible incumbent in the comparison. Do not generate many variants that differ only in names or
diagram layout. C.18 helps when a genuinely different alternative is still missing; C.11 compares the
resulting option set.

##### SYSE.20:4.1.4 - Follow every option through the whole resource and evidence arrangement

Place the proposed operations on the same time reference, using durations and availability supplied by the
case. For an operation with fixed duration, its earliest permitted start is no earlier than the latest of
its required input arrivals, resource availability and applicable permission. Its finish adds that duration.
Include setup, transfer, interpretation, reconciliation, recovery and final decision work where they consume
time. If operations share a resource, choose and test their order; an unconstrained dependency graph alone
does not give a feasible schedule.

This elementary calculation assumes the stated duration and availability conditions. A multi-resource
operation needs a joint available window, not just separate dates at which each resource was once free.
Non-preemptible work needs a window long enough to finish. For substantial resource contention or repeated
flow, use an appropriate project-scheduling or Operations Management Method. Keep the engineering
dependencies and eligibility conditions as its inputs, and bring the resulting feasible arrangement back
to the receiving engineering decision.

Calculate the first usable whole result, including the final join. A faster simulation is immaterial to
the deadline if a rig or decision still finishes later. Conversely, two individually feasible tasks can
make the whole impossible when they require the same engineer simultaneously. Include necessary provider
work and other commitments even when they belong to different Work wholes.

For uncertain durations or availability, use supported intervals or explicit scenarios and state the
conclusion they permit. If the deadline must hold through a qualified worst case, a calculation at the
average is insufficient. Do not claim a worst-case guarantee from an unqualified estimate. A smaller
conditional plan or a precise missing availability commitment can be the useful result.

Compare the whole arrangements on the declared basis: for example, meet the evidence and safety conditions
by the deadline, then minimize additional continuing support. Include immediate implementation and rework
as well as recurring costs when they change the decision. The fastest local operation need not win. If
options remain tied or none is feasible, return that outcome and its reason rather than inventing a score.

##### SYSE.20:4.1.5 - Put the chosen arrangement into use and observe its receiving result

The decision states the selected change, any required permission and its conditions, the responsible performers
and what would reopen the choice. Implementation makes the necessary resources and instructions available: reserve the
windows, establish the service configuration, communicate the agreed inputs and change returns, and revise
the applicable WorkPlan or MethodDescription.

Observe a representative performance far enough to see the result used. Did the intended inputs arrive
under their stated configurations? Could the operations share their resources as planned? What preparation
survived an update, what was repeated, and when was the integration recommendation actually usable?
Compare those observations with the proposed reasons for overlap. Separate a shorter preparation time from
a shorter whole result, and a technically usable result from an authorized release.

Use current evidence if it already answers the chosen question; a new trial is not mandatory merely because
the account was rewritten. Where the arrangement is new, distinguish a constructed schedule, a pilot and
evidence of recurring performance. If support or performers differ in the intended use, successful work
under richer assistance does not settle that transfer.

##### SYSE.20:4.1.6 - Return from the changed condition to the affected construction

Begin with the changed fact: a provider's latest completion, resource window, configuration, interpretation
rule, requirement or authority condition. Find the operation that relied on it, recompute or reinterpret
that contribution, and follow its direct receiving uses and shared demands. Retain an independent operation
and its evidence when their conditions still hold.

Reconsider the whole choice when the change defeats its acceptance rule. Valid individual results can remain
too late or jointly incompatible for the required use. Conversely, a changed local estimate need not reopen
an unaffected release claim. Distinguish redoing permitted Work, changing its plan, varying or replacing a
Method, and correcting an inaccurate description.

If an alternative still meets the same conditions, obtain the decision within the holder's authority and
implement the difference. If none does, return the missing contribution or ask the holder to change
the receiving condition. Silence, a later date typed into a plan, and an unconfirmed supplier request are
not changed commitments. A project-local observation can enter SYSE.21 without establishing a wider cultural
change.

#### SYSE.20:4.2 - Record the Result

Keep the following decision-relevant content obtainable in the Method-and-Work architecture account.
The table helps another engineer recover the reasoning; it does not require seven separate records or
duplication of adequate current models. Explain an omitted position only when the receiving engineer could otherwise mistake it for an unanswered question that affects the choice.

| Result position | Required content |
| --- | --- |
| use boundary | Engineering result at risk, receiving decision or Work, configuration, intended use, time window, deciding Agent, and authority scope. |
| current Method and Work structures | Representative performed Work or a prospective plan, performing Agents, enacted or proposed Methods, Work wholes where claimed, and every direct relation used by the decision. |
| companion structures | Only structures that change the decision, with each structure's subject, use, important correspondences, and losses. Section 1 gives an open example set. |
| conflict | Incompatible results or constraints and the consequence for the engineered result. |
| moved burdens | Each material burden, the scope that loses it, and the scope that receives it. |
| alternatives and choice | Fixed option set, proposed changed relations, comparison basis, choice rule and actual bounded outcome: selected option or retained tie-set with grounds; rejected set with reason; chosen probe with its comparison defect; or named receiving question. Retain applicable losses and preserved constraints. |
| continuation | Next question or permitted Work, receiving Agents and their decisions, each supplied result, missing evidence and the reopen condition. Include implementation and later representative Work when that continuation applies. |

The bounded decision record states the authorized Agent's choice and reason. The architecture account can supply
a design constraint to `SYSE.12` and a project-local Method variant to `SYSE.21`; each receiver makes its own decision.

#### SYSE.20:4.3 - What Changes in Practice

Engineers decide which Work may overlap, which dependency requires order, which Methods are enacted and
where a local improvement moves burden. They can choose an arrangement whose implementation and assessment
are feasible under the stated conditions. The account preserves the reasons for those dependencies so they
remain visible when a diagram or process label changes.

### SYSE.20:5 - Worked Case: Power-Converter Integration

This constructed case separates an observed diagnostic account from a plan for the next run. Its durations,
resource commitments and engineering qualifications are stipulated inputs, not measured performance claims
about power-converter projects generally.

#### SYSE.20:5.1 - Recover the failure before making the plan

A team prepares an integration recommendation for a power converter; a separate decision will authorize
release. Its diagnostic run contains the following Work:

| Work occurrence | Interval on the run clock | Directly relevant relation |
| --- | --- | --- |
| physical-model correction | minutes 0–25 | overlaps simulation during minutes 10–25 |
| numerical simulation | minutes 10–35 | uses named model editions and depends on a compatible solver service |
| rig reconfiguration | minutes 30–50 | must finish and receive rig-release authority before closed-loop test |
| closed-loop test | minutes 50–75 | uses the released rig and named converter configuration |
| evidence review | minutes 70–90 | begins before test completion; its final inference needs the test evidence |

The provider performs solver-service recovery during minutes 32–43. That Work remains separately identified;
its overlap does not make it a constituent of the project Work. Earlier laboratory training is neither
simultaneous with nor part of this run. Evidence of capability under the relevant conditions is needed;
the training date establishes only temporal order.

Each occurrence has a performing Agent and enacted Method, with assignment and authority recovered where
the claim uses them. The five intervals establish temporal relations, not that five Methods compose one
Method. The rig-release condition and solver-service dependency require their own grounds.

The engineers connect three descriptions: the Work relations; the converter, control board, power stage,
rig, load bank and platform under their subject and service relations; and the model editions, solver
configuration, simulated results, measured traces and criteria under their representation-use relations.
These are the structures needed here. The conflict is that simulation starts on a changing model and finishes
during service degradation. Its output cannot yet support the intended configuration claim. A recommendation
written at minute 90 is therefore not evidence of a usable whole result.

#### SYSE.20:5.2 - Obtain the inputs that determine possible overlap

For the next run, the lead needs a qualified recommendation for converter configuration C7 by minute 105.
The relevant specialists supply these conditions:

| Contribution or condition | Qualified case input and its consequence |
| --- | --- |
| Model and simulation | Model correction takes 25 minutes. A qualifying simulation takes 25 minutes on the final model with a compatible solver. No qualified change envelope permits an earlier simulation to stand for it. |
| Shared provider | Recovery finishes no later than minute 43; compatible capacity is reserved continuously after recovery for this run. A health and configuration check is included in admitting the simulation result. |
| Rig and test | Rig setup and its release take 20 minutes and depend on already fixed C7 rig instructions, not the unfinished model correction. The test takes 25 minutes after both rig release and the qualifying simulation have become usable. |
| Interpretation | After simulation, a two-minute configuration and evidence check interprets its result for this C7 test. Include this work in every alternative. |
| Review | The applicable review Method permits 15 minutes of procedure and available-evidence preparation followed by a five-minute final inference after the test evidence arrives. A review done wholly after the test takes the same 20 minutes. |
| People and equipment | A modeler, a simulation operator, a test operator and an authorized reviewer are distinct qualified people. One laboratory engineer performs rig setup, the two-minute check and any local-service setup; that engineer cannot do two at once. All have confirmed availability during minutes 0–135, and rig and test equipment remain available through that interval. |
| Local solver alternative | A compatible local service is already qualified for this use. Setting it up takes the laboratory engineer 15 minutes. Using it transfers configuration, security and validation responsibility to the laboratory and adds two hours of maintenance each week; that capacity and authority are available if chosen. These are current case facts, not consequences of installing software. |

The lead's rule is to meet C7 evidence eligibility, rig and authority conditions, and the minute-105 deadline;
among eligible options, prefer lower additional continuing service burden. Setup and interpretation durations
are included in the schedules. Other immediate costs are accepted within the lead's stated budget and do
not distinguish the options in this case.

The current unqualified overlap is excluded: its early result lacks the required support. A feasible current
arrangement would remain an option, but retaining a failed premise is not the incumbent.

#### SYSE.20:5.3 - Construct and compare three complete arrangements

First preserve all dependencies in a serialized option A. Then examine each wait: rig setup need not wait
for the model or simulation, and the first 15 minutes of review need not wait for test completion. Moving
only that independent work earlier constructs B. Finally replace the unavailable shared-service interval
with the qualified local alternative to construct C, including the laboratory engineer's competing setup.

The schedules use the shared provider's latest qualified ready time. They show completion bounds under the
stated durations and availability; earlier actual recovery may allow an earlier start.

| Operation or result | A — serialized | B — independent preparation overlaps | C — qualified local solver |
| --- | --- | --- | --- |
| Model correction | 0–25 | 0–25 | 0–25 |
| Local-service setup | none | none | 0–15 |
| Qualifying simulation | 43–68 | 43–68 | 25–50 |
| Configuration and evidence check | 68–70 | 68–70 | 50–52 |
| Rig setup and release | 70–90 | 0–20 | 15–35 |
| Closed-loop test | 90–115 | 70–95 | 52–77 |
| Review preparation | 115–130 | 80–95 | 62–77 |
| Final review and recommendation | 130–135 | 95–100 | 77–82 |
| First usable recommendation | minute 135 | minute 100 | minute 82 |
| Additional continuing service maintenance | none | none | two laboratory hours per week |

A is eligible as an evidence arrangement but its schedule does not meet the deadline. In B, the test starts
by max(20, 68+2) = 70. Review preparation finishes with the test, so the recommendation is ready by 95+5 = 100.
Every required result is joined; early review is preparation, not early release.

For C, placing local setup at 0–15 and rig setup at 15–35 avoids simultaneous demands on the laboratory
engineer and lets simulation begin when the final model is available at 25. The test starts at
max(35, 50+2) = 52 and the recommendation is ready at 77+5 = 82. Reversing those two setup tasks would delay
local-service availability to 35, simulation to 35–60, the test to 62–87 and the recommendation to 92.
Thus even this small example needs a resource order as well as an information order.

Both B and C meet the deadline. The stated rule selects B because C adds continuing laboratory maintenance.
C is faster; the decision does not claim that B dominates it on every criterion. If an earlier recommendation
had additional value or maintenance capacity were unavailable, the comparison would change. Compared with
A, B makes the same qualified result available 35 minutes earlier. Compared with the invalid original run,
there is no supported “ten-minute delay”: its minute-90 output never met the same eligibility conditions.

The lead authorizes implementation of B. The project makes the resource reservations and input/update
arrangements real, updates the plan and review instructions, and follows the next representative run to its
usable recommendation. The provider availability and
compatibility requirement can constrain SYSE.12; the resulting project observation can enter SYSE.21.

#### SYSE.20:5.4 - Change one provider condition and retain the valid work

Before execution, the provider revises its latest ready time from 43 to 60. All other stipulated conditions
remain available. At that latest time, B gives simulation 60–85, interpretation 85–87, test 87–112,
preparation 97–112 and final review 112–117. Its operations remain technically usable, but this bound no
longer guarantees the minute-105 deadline. Earlier observed availability or a tighter qualified bound can
change that conclusion; otherwise choose an arrangement that supplies the required guarantee.

C still finishes at 82 under its unchanged availability and qualification premises. The lead can choose it
within the stated authority and accept its maintenance burden. The model, rig Method and review split do
not require reinvention. If the local service or its continuing support cannot actually be obtained, this
branch is unavailable; the result is the missing provider/capacity commitment or a deadline change for its
holder to decide. A request for faster recovery is not a reply promising it.

This is a prospective change. If some Work has already been performed, start from its actual state and
remaining resources; the table is not permission to restart its clock or discard still-valid results.

#### SYSE.20:5.5 - A coupled design question needs an iteration, not just earlier starts

Consider a pipe route whose clearance depends on a bracket position, while the bracket design depends on
that route. No ordering of the two final designs resolves the cycle. For a stipulated prototype, the
engineers can use a qualified adjustable fixture and a pipe mock-up to test one provisional interface.
They select the initial route and bracket setting within the fixture's permitted range, check the joint
fit, and return the measured interference or clearance to both designs. The fit criterion and fixture
qualification come from the assembly specialists.

A successful joint fit permits the specified final-design step; an interference returns to the affected
geometry. If the needed movement exceeds the fixture's permitted range, its qualification no longer
supports that trial: obtain another means or revise the proposal. The fixture work may be reversible while
drilling final holes is not. Keep drilling behind the required fit and authorization condition.

### SYSE.20:6 - Bias Annotation

Watch for these four recurring interpretation biases:

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| lifecycle or maturity bias | A familiar stage diagram or maturity ladder becomes the Work architecture. | Recover the obtaining Work, Methods, and direct relations before retaining any structure. |
| software-transfer bias | Software evidence sets cadence, assurance, and release conditions for physical engineering. | Transfer only the supported contribution and retain the physical configuration, specialist, safety, and test conditions of the receiving case. |
| official-source bias | Publication or institutional prominence is treated as enacted prevalence or effectiveness. | State the supported source claim and use bounded observations or qualified expert estimates for actual practice. |
| human-only or AI-replacement bias | A job title is assumed to perform all Work, or one AI-produced result is treated as autonomous whole-project engineering. | Identify the performing Agents, their bounded Work and capability, the participating Systems, evidence use, and decision authority. |

### SYSE.20:7 - Conformance Checklist

The following conditions are required for a conforming use of this pattern.

- [ ] The account names a recognizable conflict between useful Work overlap and a required order or dependency.
- [ ] The first result contains both a current Method-and-Work architecture account and a bounded reconfiguration
      decision record.
- [ ] Performed Work has its temporal extent, performing Agent and enacted Method; a prospective arrangement
      states its planned operations and qualifications. Assignments are stated where attribution matters.
- [ ] Method composition, Method unfolding, Work parthood, Work overlap, and required order use separate claims.
- [ ] Provider or enabling Work, capability-development Work, and cultural change keep their own relations.
- [ ] Every selected structure changes the current decision and states important correspondences and losses.
- [ ] Every local gain names any material moved burden and its receiving scope.
- [ ] The fixed options differ by a named relation and are compared on one stated basis and rule.
- [ ] Each claimed overlap explains what can begin, which input conditions permit it, and what must be
      reconciled before the receiving use; unsupported preliminary information remains a stated limit.
- [ ] The whole arrangement includes shared resources, support, interpretation and applicable rework;
      local completion times alone do not establish a feasible whole result.
- [ ] The choice, implementation Work, later observations, and cultural continuation are distinguished.
- [ ] The receiving Agent gets the actual choice outcome, missing evidence, next question or Work, and reopen
      condition.

### SYSE.20:8 - Common Failures and Repairs

When one of these recurring failures appears, use the corresponding repair:

| Recurring failure | Repair |
| --- | --- |
| A first–then procedure is presented as levels | Keep the direct temporal or transformation relation; recover Method organization separately. |
| Overlapping Work is treated as proof of Method composition | Identify each Method and require an obtaining Method-part relation before claiming a composite Method. |
| A Work part is placed inside the engineered System | Keep the Work structure and subject structure separate; relate their descriptions through named uses. |
| A connected model is treated as the integrated engineering reality | Name the model epistemes, their subjects, correspondences, losses, and receiving uses. |
| A platform service is assumed usable whenever dependent Work runs | State the provider Work, service condition, compatibility evidence, access, and moved maintenance burden. |
| One local activity becomes faster while the engineering result still waits | Measure the receiving result and identify the limiting contribution and moved burden. |
| A selected option lacks a comparison rule or authority | Recover the fixed option set, basis, rule, deciding Agent and authority before calling it a decision. Name a next probe only when further inquiry is the selected continuation. |
| A preliminary result is accepted because it is labelled provisional | Recover its allowed use, change sensitivity and reconciliation; wait or obtain the missing qualification when these cannot be supplied. |
| Separately feasible tasks require the same resource simultaneously | Construct a joint resource order or obtain qualified capacity, then recompute the first usable whole result. |
| A feedback arrow is removed from a drawing and the dependency is forgotten | State the starting assumption, perform the informative iteration and reconcile the coupled results. |
| A decision is reported as changed practice | Identify later implementation Work and representative observations separately. |
| One project choice is reported as cultural success | Supply it as one project observation to `SYSE.21`. A qualified current account can finish there; claims about recognition, enactment, selection or retention need their own applicable evidence, without automatically commissioning new Work. |

### SYSE.20:9 - Consequences

The project can retain productive overlap without losing real guards, configuration identity, evidence status, or
authority. The selected structures, their direct relations, and their correspondences support one bounded
engineering choice. Platform and capability dependencies become visible before a local gain is
accepted.

The cost is recovery of the Work occurrences, Methods, configurations, result uses, and authority needed by the
choice. Judge diagrams by the relations they make usable for this choice. Some local improvements will lose
priority when their moved burdens become visible.

### SYSE.20:10 - Rationale

Method organization, dated Work order, and simultaneous Work answer different questions. A Method unfolding says
how a reusable way of doing is organized. A temporal relation says when admitted Work occurs. Work parthood says
which occurrence contributes constitutively to another Work whole. Treating them as interchangeable destroys
either useful overlap or necessary order.

Engineering adds a recurring domain difficulty to the general `C.32.MWA` problem: several contributions must
produce a result about one configured engineered System while using models, evidence, specialist decisions, and
enabling Systems with their own identities. Connecting the recovered structures to that result makes their consequences for the bounded
reconfiguration choice explicit.

### SYSE.20:11 - SoTA and Source Use

Competent engineering practice already includes dependency recovery, iterative design and resource-aware
scheduling. Use an adequate existing arrangement directly. This pattern's narrower contribution is to
construct and qualify overlap for one configured engineering result, including preliminary-input use,
evidence joins, provider conditions and shared resource demands. Its worked timings are a conditional
construction, not a comparative field study.

| Source | Retained contribution and actual use here | Limit or difference |
| --- | --- | --- |
| Current FPF A.3.1, A.15.1, A.22, B.1.5, C.27.TA, C.30.STRAT, C.32.MWA, C.32.MLAO and C.36 | Method and Work identity, temporal and constituent relations, selected structures, architecture synthesis, moved burdens and cultural continuation. | C.32.MWA supplies the general account; this pattern develops the engineering construction and its bounded decision. |
| Dependency and Structure Modeling community: [building a DSM](https://dsmweb.org/building-and-creating-a-dsm/), [sequencing](https://dsmweb.org/sequencing-a-dsm/) and [tearing](https://dsmweb.org/tearing-a-dsm/) | Recover direct input dependencies with their explanations, identify coupled groups, and expose provisional assumptions used to begin an iteration. These supply the dependency and cycle treatment in :4.1.1 and :4.1.3. | These established Methods expose real dependencies and starting assumptions. Their application still needs the case's engineering, resource and authority qualifications. |
| [DORA Continuous Integration](https://dora.dev/capabilities/continuous-integration/), “How to implement CI”, “Objections” and “Common pitfalls” | Frequent integration, repeatable builds, feedback and repair belong together; the useful result includes review, integration and testing. This informs the distinction between early local completion and usable whole results. | A software contribution with implementation prerequisites; no universal cadence or physical-test substitution is transferred. |
| [DORA Platform Engineering](https://dora.dev/capabilities/platform-engineering/), updated 12 January 2026, implementation and impact sections | User-journey construction, an initially limited platform, extensibility and task feedback make qualified service support a substantive alternative. They inform :4.1.3 and its return to SYSE.12. | Practitioner guidance already concerns end-to-end use. The pattern adds case-specific engineering compatibility and support comparison. |
| [DORA Streamlining Change Approval](https://dora.dev/capabilities/streamlining-change-approval/), updated 30 October 2025 | Peer review, early feedback and differentiated treatment of consequential changes inform the early-preparation/final-decision split. | The guide retains authorization and separation-of-duties purposes. It supplies no permission to bypass physical, specialist or external release conditions. |
| [DORA 2025, State of AI-assisted Software Development](https://dora.dev/research/2025/dora-report/), v.2025.2, pp.68–72 | The report relates platform quality to whole developer experience and reports performance benefits alongside delivery-instability trade-offs. It supports comparing the receiving result and residual burden in SYSE.20:4.1.4–SYSE.20:4.1.5. | Reported software estimates and interpretation do not establish the converter timings or hardware safety. Use the capability guides above for their implementation guidance. |
| Flow Engineering, [The Iterative Systems Engineering Handbook, Volume I](https://www.flowengineering.com/handbook/iterative-systems-engineering/volume-1), chapters 2 and 4 | Cross-functional negotiation, provisional design assumptions, feedback and whole-project trade-offs inform construction of coupled alternatives. The account itself retains iteration boundaries and external constraints. | Provider-authored practice proposals and cases; claims of universal iterative superiority or organizational prevalence are not adopted. :4 explains the permitted assumption and return in the receiving engineering case. |
| Current AI-engineering evidence qualified in SYSE.15 | Compatible observations can inform a bounded alternative involving AI-capable Systems and its actual support. | An output or local speed gain supplies no whole-project capability, configuration correspondence or decision authority. |

Compared with direct DSM use, this pattern keeps its relation recovery and cycle construction, then joins
them to the engineering result's eligibility and available means. Use the fuller DSM treatment for a coupled
network that needs it. Compared with competent DORA or iterative-engineering practice, the gain is an
obtainable engineering account of what may start, what must be joined, and what a changed condition reopens.
Where a project's existing Method already supplies that account, repeating the pattern adds no new result.

Reopen the affected claim when a later source or representative Work changes the relied-on Method, relation,
qualification or burden. Source publication status alone does not establish a changed engineering answer.

### SYSE.20:12 - Relations

The following direct relations are used by this pattern body.

- `SYSE.15` supplies compatible engineering-Method repertoire claims. Availability alone supplies no fit or
  enactment claim.
- `A.3.1` governs Method identity, multiple-parent classification, participation in several whole Methods,
  refinement, and replacement. `B.1.5` governs any claimed Method composition.
- `A.15.1`, `F.6`, and `C.27.TA` govern performed Work, attribution when needed, and direct temporal claims.
- `A.22`, `C.30`, `C.30.STRAT`, `C.32.MWA`, and `C.32.MLAO` govern selected structures, architecture claims,
  level or stack claims, several-structure synthesis, and moved burdens.
- `C.11` governs the bounded choice after alternatives are available; `C.18` governs alternative generation and
  `C.24` later implementation sequencing when those questions are current.
- `C.2.1`, `C.29`, and the applicable model-use, evidence, configuration, and assurance patterns govern the
  epistemes and correspondences used by the decision. SYSE.10 supplies evidence qualification, SYSE.13
  configuration correspondence, and SYSE.14 the separate release or transition decision.
- `SYSE.20` supplies one bounded platform-design constraint to `SYSE.12`. It supplies one project-local Method
  variant observation to `SYSE.21`, where cultural continuation is evaluated.
- Operations Management retains continuing-flow specialization; Organization Change Engineering retains
  organization capability and assignment changes; application DPFs add the physical, computational, clinical,
  legal, safety, or other specialist distinctions that change their engineering action.

### SYSE.20:End
