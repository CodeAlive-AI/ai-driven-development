## MNT.9 - Perform and Record the Maintenance Intervention

> **Type:** Method
> **Status:** Stable

### MNT.9:1 - Problem frame

Use this method to establish what happened during a maintenance intervention or to perform and record the intervention itself. A later decision can depend on which action took place, on the resulting installed state, or on both. An interruption, substituted part or changed setting can make those questions come apart.

For a historical question, recover which act, item and time matter, and use the evidence sufficient for that claim. For a commissioned intervention, perform it under the applicable procedure and conditions and record the material actions, any change or interruption, and the resulting configuration. [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) establishes restored functioning and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) establishes the hand-back result. A recommendation can answer a request for advice before work begins.

### MNT.9:2 - Problem

A work order describes intended work. Closing its tasks can conceal what was skipped, repeated, changed or performed under different conditions. A subsequent tester may then check the wrong configuration, and a future maintainer may infer that a suspected cause was confirmed.

Unexpected conditions make this worse when the team improvises beyond the permitted scope without revisiting protection, competence or the maintenance choice.

### MNT.9:3 - Forces

The practitioner needs enough freedom to respond to the machine as found while preserving the limits that make the response acceptable. Detailed recording can support later diagnosis but distract from protected work if poorly timed. A work interruption can require relief or re-establishment of a condition; simply extending the shift may impair performance.

### MNT.9:4 - Solution

Recover the selected task and the operative work conditions before performing it. The applicable equipment procedure supplies the technique, tool use, tolerances and controls. Use this Method to organize the intervention and the account that later users need.

When the order is to establish whether a past replacement occurred, inspect the records or other evidence that can decide it for the item and date in question. A replacement carried out today can meet a new work order. Its completion alone cannot establish when an earlier intervention occurred.

Maintain correspondence between work and actual state. Identify the unit, relevant configuration, selected parts and settings. Where the procedure requires a check before an irreversible or consequential step, perform that check at the point where it establishes the needed condition. A later signature cannot recreate an unobserved state that is no longer recoverable.

When the actual condition differs from the expected one, determine what changes. A harmless access detail may remain within the permitted task. Unexpected damage, a different part interface, a lost protection condition or a larger repair can change competence, permission, time and verification. Use the applicable hold or restoration procedure and return the changed maintenance decision rather than silently extending the scope.

If work stops, prepare for its continuation. Preserve a condition that the next practitioner can safely recognize, transfer the relevant unfinished work and protection through the applicable arrangement, and re-establish any condition that no longer has usable support. If fatigue or working conditions impair the task, change allocation, relief or timing. A deadline cannot restore the practitioner’s ability to do the task.

Preserve the facts that later users need. These commonly include material actions, installed or removed part identities, relevant settings and measurements, deviations from the selected work and unresolved conditions. Use the existing maintenance record when it serves that purpose. Applicable regulatory or organizational retention requirements remain in force.

When several performers contribute, reconstruct which actions belonged to this intervention. Match the installed item, the times, the authorized scope and any handoff the next action depended on. An earlier report can supply evidence of the installation a specialist observed. Identify the earlier act and the use of its record today. If the order includes a new independent examination, identify the examination performed and its result. A single entry can answer a question about one act when its meaning and coverage establish that act.

Keep statements at their supported level. “Bearing installed using the applicable procedure” concerns the intervention. “The required flow is restored” needs functioning evidence. “This recurring failure has been eliminated” needs a different horizon and causal basis. Link those later results when they exist without assigning them to a task-completion entry.

Give the tester, operator or maintenance-history user the evidence they need about the work performed and the resulting configuration. If the work is incomplete, state the condition in which it stopped and the condition needed for continuation. Distinguish known unfinished work from work whose performance the surviving records leave unknown. An observation or a complete record of required acts may decide the issue. A blank field in a partial log can leave either history possible.

### MNT.9:5 - Archetypal Grounding

In the extended constructed PS17 branch, the part return, protected access and permission are in place. The team performs the selected bearing intervention under the applicable equipment procedure.

The removed bearing is identified as R551 and the installed compatible bearing as R607. These are constructed serial-unit identifiers. The resulting installed configuration is identified as C42; it retains the same approved design basis although the installed bearing has changed. The maintenance record describes that change; it is not the physical configuration itself.

If unexpected housing damage is found, the original bearing task may no longer answer the condition. The team preserves the supported state and obtains the relevant revised diagnosis and work decision. It does not mark the original plan complete merely because the replacement bearing was available.

In the completed branch, the intervention record identifies the resulting configuration and supplies the material observations to MNT.10. It does not yet claim restored district-heating service or removal of the unresolved long-horizon recurrence mechanism.

### MNT.9:6 - Bias-Annotation

Completion targets reward closed tasks and can discourage reporting deviations or unfinished work. A detailed plan can also make the practitioner expect the machine to match it. Keep actual observations visible where they change the work or later interpretation.

### MNT.9:7 - Conformance Checklist

What act, item, time or installed state does the recipient need to establish, and what evidence covers it? For work to be performed, check its procedure and operative conditions and how material deviations, interruptions and changes of scope were handled. For a claim about the completed job, identify what establishes each consequential handoff. An omitted act, an undocumented act and a remaining obligation can call for different next actions.

The result concerns performed intervention. Functioning and resumed-use claims require their own support only when those are the selected subsequent results.

### MNT.9:8 - Common Anti-Patterns and How to Avoid Them

A task is closed because the planned hours were consumed. Record what actually happened and the remaining state. A substituted part is described only as “equivalent” when applicability is material. Preserve the basis that makes it usable in this configuration.

An exhausted specialist is instructed to finish more carefully. Revise relief or timing in response to the capability limit.

### MNT.9:9 - Consequences

The tester and operator receive an account that corresponds to the intervention, including its limits. Some work returns for a revised decision rather than being completed under an obsolete plan. Recording costs remain focused on useful later claims and operative retention requirements.

### MNT.9:10 - Architectural Rationale

Performance and its account are joined because later maintenance decisions rely on that correspondence. Separating intervention evidence from functioning and release keeps task completion, evidence of functioning and authorization to resume use distinct.

### MNT.9:11 - SoTA-Echoing

The practice question is how to preserve reliable continuation when work differs from its plan. This pattern adapts the work-management concern in GFMAM's maintenance framework and the fatigue-reporting problem in CASA's 2026 maintenance risk account. Against task-closure-only management, it adds the interruption, actual-state and relief decisions in the Solution. It accepts focused reporting and occasional replanning to avoid concealing incomplete or unsupported work. CASA’s aviation account explains how fatigue can impair maintenance work. It supplies no duty-time threshold for every setting. Reopen when a new work variant or observed interruption defeats the continuation arrangement. See [GFMAM](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf) and [CASA's fatigue account](https://www.casa.gov.au/operations-safety-and-travel/safety-management-systems/sector-safety-risk-profiles/maintenance-activities-sector-safety-risk-profile/fatigue).

### MNT.9:12 - Relations

[MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the selected intervention, [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) its support and [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) its operative protection and permission. [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) and [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) handle changed timing or shared work. [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) consumes performed-work and configuration evidence; [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) preserves its useful history. [FPF A.13](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/12-a-13---the-agential-role-agency-spectrum.md) and [FPF A.15.1](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/15-a-15-1---u-work-dated-performed-work-occurrence.md) govern precise performer and performed-Work claims when those stronger claims are made.

### MNT.9:End
