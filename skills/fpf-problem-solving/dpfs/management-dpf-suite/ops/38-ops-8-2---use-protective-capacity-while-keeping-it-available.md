## OPS.8.2 - Use Protective Capacity While Keeping It Available

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative

### OPS.8.2:1 - Problem frame

**Use this when** a person, machine or computing resource has idle intervals reserved for another service, and useful auxiliary work could occupy those intervals. An operator could prepare the next job or practise a skill. A machine could run an experimental batch. A computing resource could run a background analysis. Each choice is useful only if its interruption or completion leaves the required service available on the terms being protected.

Construct a usable arrangement: eligible auxiliary work, conditions for starting it, what triggers its end or interruption, and how the resource becomes ready for the protected work. The first result can be a short timing comparison that accepts one candidate and rejects another.

Start from the protection already selected through OPS.8: what work needs which capability, amount of resource, response time and access. If an existing arrangement meets those conditions and the proposed auxiliary work changes none of them, apply it. Choosing a learning goal or an improvement experiment belongs to the corresponding development method; this pattern establishes whether its execution fits the operation.

### OPS.8.2:2 - Problem

“No work is running” and “this capacity can be promised elsewhere” describe different conditions. An auxiliary job can consume the time needed to resume the protected service, retain a required resource after suspension, or create another commitment that prevents recall.

Keeping all such intervals empty can also forgo useful preparation and development. The practitioner needs to distinguish work that preserves the selected protection from work that spends it, and to compare the useful contribution with the costs of interruption and recovery.

### OPS.8.2:3 - Forces

| Force | Practical tension |
| --- | --- |
| Useful preparation and availability | Auxiliary work can improve later service while obstructing a call that arrives now. |
| Short fragments and retained progress | Smaller units can be easier to stop, but repeated saving, switching and reconstruction can consume their value. |
| Nominal priority and actual release | A priority rule can demand a return while the required person, machine state or memory remains unavailable. |
| Development and present capability | Learning may expand future options; the protected work still needs capability available today. |
| One return and sustained service | A quick first response can conceal exhaustion, displaced recovery or insufficient capacity for subsequent calls. |

### OPS.8.2:4 - Solution

**Working sequence:** recover the protected service → choose an auxiliary unit → construct its interruption or completion and the return to service → compare the preserved service and useful gain → operate the arrangement and revise changed conditions.

#### OPS.8.2:4.1 - Recover what must remain available

Name the protected work, the event that can call the resource, and the condition that counts as ready. Readiness includes the capability, access, configuration and inputs needed for the next protected action. Moving a person back to a workstation may precede readiness if the person still needs a handover or must reconstruct the situation.

Distinguish two common requirements:

- Be ready by a known time, with no earlier call included in the selected protection.
- Be ready within a stated delay after a call that can arrive while auxiliary work is running.

A job that fits the first requirement may fail the second. Also retain the amount and duration of protected service needed after the return; a prompt start alone may not satisfy the commitment.

Separate capacity needed for this protection from capacity left over after it. An idle interval does not establish either amount. If several services rely on the same reserve, retain their relevant joint demand through OPS.10.1. OPS.12 supplies the human capability, fatigue, rest and relief conditions that the allocation must preserve.

#### OPS.8.2:4.2 - Choose a unit that can yield the required resources

Identify a useful auxiliary contribution and its actual execution conditions. Preparation, learning, research, an improvement trial and an ordinary lower-priority job can all qualify. Compare the unit that can be stopped or completed, not the whole project name.

For that unit, establish how progress and resources can be released:

| Auxiliary arrangement | What must be established |
| --- | --- |
| Finish before a known protected start | The unit, cleanup and restoration fit the available calendars before that start. |
| Pause and resume later | A permissible stopping point can be reached; the needed resources are released; sufficient state remains for resumption. |
| Abandon and later restart | Abandonment is permissible, resources can be recovered in time, and lost work and any remaining effects are included in the choice. |
| Transfer the auxiliary work | A capable recipient is available, the handover fits, and the transfer does not consume another resource needed by the protected service. |

For human work, a short note of the current state, next step and unresolved difficulty can reduce later reconstruction when that information would otherwise be lost. Use the existing work materials when adequate. Include the time to leave that note and the effort of repeated transitions.

For equipment, recover the work needed to leave a usable state: for example completing an indivisible cycle, removing material, cleaning or restoring a fixture. For computing, distinguish pausing execution from releasing the memory, accelerator, license or other allocation the protected job needs. A saved computation can help auxiliary resumption without itself preparing the protected job.

Retain effects outside the suspended activity. Stopping an AI computation does not undo a request it already sent to a person or another service. Establish what has occurred before deciding how to resume or repeat that activity.

#### OPS.8.2:4.3 - Construct the return to protected work

Starting from a possible call, follow the actual operations until the protected resource is ready. Include detection, remaining work before a permissible interruption, preservation or disposal of auxiliary work, resource release, movement or handover, and restoration of the protected configuration or context.

For a simple serial return with immediately available supporting resources, the elapsed time is:

**return delay = detection delay + remaining time to interruption + release time + transfer time + protected-work restoration time.**

Use each duration once. For example, a stop procedure that already saves and releases the auxiliary state does not need a second saving allowance.

Where operations can overlap or must wait for a person, tool or calendar window, construct their precedence and resource placement through OPS.10.2. Adding durations alone then does not determine the return time. The resulting schedule must end at protected-work readiness, rather than at the pause command or departure from the auxiliary task.

Compare the resulting readiness with the protected requirement. For an anytime-call claim, cover the states in which the auxiliary work may be interrupted, including its longest indivisible segment and consequential calls during setup. For a known-time requirement, place completion and restoration before that time. Keep the information available when each decision must be made; an arrangement cannot choose the right auxiliary start using a later call's timing.

Use a bound, a finite set of scenarios or a joint probability model according to the service question. A typical transition time does not establish a maximum or a percentile. OPS.10.1 supplies the corresponding uncertain-capacity comparison. If a material duration remains unknown, retain what the comparison does establish and decide whether learning it can change the choice.

Finally, check that the returned resources can perform the protected work for its required duration. If the arrangement fails, change the auxiliary unit, preparation, recall timing or supporting allocation, or leave this capacity available. Spending some protection is a different operating choice that requires reconsidering the affected commitment through OPS.7 or OPS.13.

#### OPS.8.2:4.4 - Compare useful gain with the whole interruption cost

Compare feasible auxiliary candidates with leaving the interval unused. Retain the result each candidate could supply and the work needed to obtain it, including preparation, interruptions, lost partial progress, later auxiliary resumption and any new obligations.

An already-paid salary does not make those consequences vanish. Use OPS.14 for a financial comparison when it can change the decision. Use OPS.12 when repeated transitions can impair continuing human service. Observe a trial through OPS.16 or A.3.1.WT when an unresolved operating effect justifies one; do not demand a new experiment when the available comparison already settles the choice.

If development is the intended gain, C.40.OI and C.40.DC construct the opportunity and transition. HCD.2 adds the practice, feedback and support needed for a human capability gain. An interruptible activity can fit the reserve and still teach little. C.39.MF and A.3.1.WT support a method-improvement question and its trial. These contributions establish the value being sought; the return construction establishes compatibility with the operation.

Choose the simplest adequate arrangement. The choice may favor a short useful unit, preparation outside the protected resource, another resource, a later window or continued availability.

#### OPS.8.2:4.5 - Operate the start, recall and resumption conditions

Before starting, establish that the protected service is covered under the selected conditions, the auxiliary unit can use the interval, and the recall or finish signal will reach the performer or controller in time. The existing queue and work instructions can carry the arrangement.

On recall, execute the selected interruption and restoration, then start the protected action when its inputs are ready. If the supporting resource or restoration condition has changed, use the corresponding alternative or revise the affected commitment; repeating the old timing estimate cannot restore availability.

When protected work permits auxiliary resumption, recover its actual state and any changes that occurred during the interruption. Continue from a still-valid checkpoint, revise the plan, restart or discard the unit according to the chosen arrangement. Preserve already incurred work and effects in that decision.

Reopen the arrangement when call timing, service demand, resource access, capability, auxiliary stopping behavior, restoration or repeated interruption costs change. Stop elaborating once the operation has a usable choice under the conditions it needs to protect.

### OPS.8.2:5 - Archetypal Grounding

#### OPS.8.2:5.1 - Practice during an operator's reserve interval

An already-qualified operator has a 45-minute interval during which a call can require a return to protected service within five minutes. Once back, the operator and required equipment can sustain that service. A proposed practice exercise uses an independent training setup and can be stopped at short points.

The constructed timing assumptions are maximum durations under this arrangement:

| Return operation | Minutes |
| --- | ---: |
| Detect the call | 1 |
| Reach a stopping point and leave the needed resumption note | 1 |
| Move to the protected workstation | 1 |
| Recover its current situation and prepare the next action | 2 |
| Total, with these operations serial and no additional waiting | 5 |

This exercise fits the stated response requirement. The calculation does not establish its learning value; its practice and feedback still need to serve the selected development question.

A live lesson with a 25-minute segment that cannot be left can exceed the entire five-minute allowance before transfer or restoration begins. Its fit within the 45-minute interval does not make it suitable for this anytime-call protection.

Now change the workstation's restoration to five minutes. The former exercise gives 1 + 1 + 1 + 5 = 8 minutes and no longer preserves the response. Preparing a usable handover in advance might reduce restoration, but that is a changed arrangement whose time and burden must be included. Otherwise choose another activity or preserve readiness.

#### OPS.8.2:5.2 - A free machine but an unavailable setter

A machine must be ready for its protected job at 09:30. There is no earlier-call requirement in this case. An auxiliary trial needs five minutes of setup by a setter, twenty minutes of unattended machine time and five minutes of restoration by that setter. The setter is available from 09:00 to 09:20 and then from 09:40. The protected job's operator is available at 09:30.

The duration sum is thirty minutes. But setup at 09:00–09:05 and running at 09:05–09:25 leave restoration waiting until 09:40–09:45. The trial does not fit the protected start.

If a separately useful ten-minute trial is available, setup at 09:00–09:05, running at 09:05–09:15 and restoration at 09:15–09:20 fit both calendars. The machine is ready before 09:30. Alternatively, prepare a different unit or obtain another qualified setter; merely labeling the trial low priority changes none of these times.

This arrangement protects the named start. It has not established immediate recall during the trial's indivisible machine cycle.

#### OPS.8.2:5.3 - Suspending a background AI job leaves its accelerator occupied

A protected computation needs an accelerator and its memory. A background job uses that allocation while the protected queue is empty. The scheduler can suspend the job's execution, but under this configuration suspension retains the accelerator allocation. Starting the protected job requires that allocation to be released.

A “suspend on arrival” rule therefore fails to provide the needed resource even if the suspension command is immediate. For example, Slurm's generic-resource documentation states that resources allocated to a suspended job remain unavailable to other jobs. Use a release mechanism supported by the actual application and scheduler, such as checkpointing followed by termination and later restart.

For a constructed alternative, allow one minute to receive the call, checkpoint and terminate; one minute to release and clean up the allocation; and one minute to load the protected computation. With those serial bounds and resources available, the three-minute return fits a three-minute start requirement. The protected computation's subsequent capacity needs are also assumed to fit.

An extra cleanup wait breaks that bound. Keeping the allocation free may then be the usable choice. Separately retain the cost of restarting the auxiliary computation and any external actions that its earlier execution already caused.

### OPS.8.2:6 - Bias-Annotation

A utilization display makes idle time conspicuous while the protection it supplies may be invisible. Conversely, a label such as “reserve” can discourage useful work even when its full return fits the service requirement.

A successful short return can hide later costs. Repeated interruption may waste auxiliary progress, exhaust a person or occupy supporting resources. Judge the arrangement at the receiving service and the intended auxiliary result, rather than by occupied minutes alone.

The numerical cases are constructed timing comparisons that establish conditional consequences.

### OPS.8.2:7 - Conformance Checklist

- The protected work has a recognizable readiness condition, response or start requirement, and sufficient continuing service.
- The auxiliary unit has a usable completion, interruption, transfer or abandonment mechanism.
- The return includes consequential resource release, supporting calendars and restoration.
- The claimed protection covers the relevant call times and auxiliary states under the selected bound, scenario or probability model.
- Auxiliary benefit is compared with transition, restart and continuing-service costs.
- New commitments and external effects survive the accounting of suspension and resumption.
- A changed return condition can change the start or recall decision.

### OPS.8.2:8 - Common Anti-Patterns and How to Avoid Them

| Mistake | What fails | Repair |
| --- | --- | --- |
| Filling every idle interval | Protection disappears when the call arrives. | Recover the protected service and fit the whole return before promising the interval. |
| Treating priority as interruptibility | An indivisible operation or retained allocation prevents recall. | Identify the actual stopping and resource-release mechanism. |
| Ending the calculation at “paused” | Travel, cleanup or restoration delays readiness. | Calculate through the first ready protected action. |
| Fitting duration without fitting calendars | A needed setter or handover participant is unavailable. | Place return operations with their required resources. |
| Treating an easy-to-stop lesson as capability gained | An operating fit substitutes for practice and transfer. | Retain HCD's learning and capability question separately. |
| Counting only the first successful return | Repeated transitions damage auxiliary progress or sustained service. | Compare the whole relevant operating interval and its actual burden. |

### OPS.8.2:9 - Consequences

Useful preparation and development can occupy otherwise idle intervals without spending the selected protection. This requires an arrangement whose return fits.

The construction can also justify leaving an interval empty. It exposes which change would make another use feasible: a smaller auxiliary unit, earlier preparation, a different resource, faster restoration or a revised service commitment.

### OPS.8.2:10 - Architectural Rationale

Protective capacity is useful through the work it can perform when needed. Its availability depends on capability, timing, location, access and state. The same idle machine or person can therefore be available for one protected service and unavailable for another.

The auxiliary unit, its interruption and the restoration form one operating construction. Keeping them together prevents an attractive auxiliary result from hiding the work needed to resume service. Preserving the auxiliary state and restoring the protected state remain separate contributions.

The method uses ordinary scheduling and capacity comparisons for the return. Its particular contribution is selecting and operating auxiliary work around that return, including the effects that remain after interruption. The comparison retains both the encompassing service and the smaller actions through which availability is restored.

### OPS.8.2:11 - SoTA-Echoing

The selected approach compares a complete return with the protected service, then evaluates the auxiliary contribution and its burden. Simpler alternatives remain useful: keep the resource ready, or use only capacity established as excess to protection. Temporarily occupying protective capacity needs the additional construction in sections 4.2–4.5.

Steve Tendon, *The Book of TameFlow* (2022), printed pp. 226–229, distinguishes productive, protective and excess capacity and uses excess capacity for preparation and development. Adopt that distinction. Applying it to temporary use of the reserve adds an explicit interruption and restoration construction; the source's use of excess capacity does not itself establish that permission. Its fixed-expense argument also leaves transition burden, consumables, lost alternatives and changed service consequences to the receiving comparison.

Hopp and Spearman, *Factory Physics*, third edition, §4.4.3 and §§7.4.2–7.4.3, supplies two useful constructions: move eligible preparation outside machine downtime, and use already-capable workers where work needs them. The simple worker-transfer equivalence assumes no handoff delay. Adapt preparation and transfer to the actual return calendars in 4.2–4.3; training and zero-time handover cannot silently replace present operating capability.

[Van Zoonen and Scharp, *Managing Daily Work Intrusions* (2025)](https://doi.org/10.1037/str0000362), describes a ready-to-resume planning intervention. Adopt the small state-and-continuation aid when it reduces reconstruction. Their field study reports reduced attention residue alongside increased general exhaustion, so include the intervention's burden and do not infer a universal response-time benefit. Sections 4.2 and 4.4 keep those two effects in the choice.

The Slurm documentation makes computational resource release concrete: [suspension](https://slurm.schedmd.com/preempt.html) can retain memory and licenses, and [generic resources](https://slurm.schedmd.com/gres.html) remain allocated to suspended jobs. [Requeueing](https://slurm.schedmd.com/sbatch.html) restarts the batch script, so application recovery must be supplied separately. [Backfill scheduling](https://slurm.schedmd.com/sched_config.html) protects expected starts using runtime limits; that is a different timing requirement from an unknown call. [Prolog and epilog behavior](https://slurm.schedmd.com/prolog_epilog.html) adds real preparation, cleanup and failure conditions. Adapt these mechanisms to the selected configuration rather than inferring released capacity from a generic pause command.

Reopen the arrangement when a different auxiliary unit or return mechanism improves useful service at acceptable cost, or when call timing, allocations, interruption behavior or restoration changes.

### OPS.8.2:12 - Relations

OPS.8 selects the protection and its operating purpose. OPS.5 applies a start rule; OPS.7 and OPS.13 handle an incompatible priority or commitment. OPS.8.1 treats earlier work that can return after a release; this method treats the auxiliary work occupying resources needed for protection.

OPS.10.1 supplies capacity and uncertainty comparisons; OPS.10.2 places interruption and restoration with precedence and calendars. OPS.11.1 recovers the operating arrangement, and OPS.15.1 keeps occupancy and waiting intervals distinct.

OPS.12 supplies human capability and workload conditions, OPS.14 the financial comparison, and OPS.16 the operating trial. C.40.OI and C.40.DC, HCD.2 and C.39.MF and A.3.1.WT supply development choices, practice and method trials when those are the auxiliary contribution.

C.11 supports the choice between useful gain, retained protection and unresolved risk. MMP.10 and CMP supply the constraint and obtaining methods used by the scheduling contribution when the simple comparison no longer suffices.

### OPS.8.2:End
