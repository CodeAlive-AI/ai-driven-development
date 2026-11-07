## MNT.9 - Perform and Record the Maintenance Intervention

> **Type:** Method
> **Status:** Stable

### MNT.9:1 - Problem frame

Use this pattern when a selected maintenance intervention is being performed and later decisions depend on what actually happened. The planned bearing has been replaced, but an interruption, substituted part or changed setting can leave the work record inconsistent with the machine.

Perform the task within its applicable procedure and operative conditions, preserving the material actions and actual resulting configuration. The first result is evidence of the performed intervention, including its incomplete or changed portions. [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) establishes restored functioning and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) establishes the hand-back result. This pattern does not require physical work to finish a recommendation request.

### MNT.9:2 - Problem

A work order describes intended work. Closing its tasks can conceal what was skipped, repeated, changed or performed under different conditions. A subsequent tester may then check the wrong configuration, and a future maintainer may infer that a suspected cause was confirmed.

Unexpected conditions make this worse when the team improvises beyond the permitted scope without revisiting protection, competence or the maintenance choice.

### MNT.9:3 - Forces

The practitioner needs enough freedom to respond to the actual machine while preserving the limits that make the response acceptable. Detailed recording can support later diagnosis but distract from protected work if poorly timed. A work interruption can require relief or re-establishment of a condition; simply extending the shift may impair performance.

### MNT.9:4 - Solution

Recover the selected task and the operative work conditions before performing it. The applicable equipment procedure supplies the concrete technique, tool use, tolerances and controls. This Method organizes maintenance performance and its usable account; it does not replace that procedure.

Maintain correspondence between work and actual state. Identify the unit, relevant configuration, selected parts and settings. Where the procedure requires a check before an irreversible or consequential step, perform that check at the point where it establishes the needed condition. A later signature cannot recreate an unobserved state that is no longer recoverable.

When the actual condition differs from the expected one, determine what changes. A harmless access detail may remain within the permitted task. Unexpected damage, a different part interface, a lost protection condition or a larger repair can change competence, permission, time and verification. Use the applicable hold or restoration procedure and return the changed maintenance decision rather than silently extending the scope.

Handle interruption explicitly. Preserve a condition that the next practitioner can safely recognize, transfer the relevant unfinished work and protection through the applicable arrangement, and re-establish any condition that no longer has usable support. If fatigue or working conditions impair the task, change allocation, relief or timing. The completion pressure does not supply capability.

Preserve the facts that later users actually need. These commonly include material actions, installed or removed part identities, relevant settings and measurements, deviations from the selected work and unresolved conditions. Use the existing maintenance record when it serves that purpose. Applicable regulatory or organizational retention requirements remain in force.

Keep statements at their supported level. “Bearing installed using the applicable procedure” concerns the intervention. “The required flow is restored” needs functioning evidence. “This recurring failure has been eliminated” needs a different horizon and causal basis. Link those later results when they exist without assigning them to a task-completion entry.

Return the performed work and resulting configuration to the tester, operator or maintenance-history user who needs them. If the work is incomplete, state its actual stopping state and the condition needed for continuation. A truthful partial result is more useful than a closed order that implies unperformed work.

### MNT.9:5 - Archetypal Grounding

In the extended constructed PS17 branch, the part return, protected access and permission are in place. The team performs the selected bearing intervention under the applicable equipment procedure.

The removed bearing is identified as R551 and the installed compatible bearing as R607. These are constructed serial-unit identifiers. The resulting installed configuration is identified as C42; it retains the same approved design basis while the actual bearing individual has changed. The maintenance record describes that change; it is not the physical configuration itself.

If unexpected housing damage is found, the original bearing task may no longer answer the condition. The team preserves the supported state and obtains the relevant revised diagnosis and work decision. It does not mark the original plan complete merely because the replacement bearing was available.

In the completed branch, the intervention record supplies the actual configuration and material observations to MNT.10. It does not yet claim restored district-heating service or removal of the unresolved long-horizon recurrence mechanism.

### MNT.9:6 - Bias-Annotation

Completion targets reward closed tasks and can discourage reporting deviations or unfinished work. A detailed plan can also make the practitioner expect the machine to match it. Keep actual observations visible where they change the work or later interpretation.

### MNT.9:7 - Conformance Checklist

Was the selected work performed within its applicable procedure and operative conditions? Were material deviations, interruptions and changed scope handled by the relevant decision? Can the next user recover the actual installed state and supported work claims? Are incomplete portions and unresolved consequences stated?

The result concerns performed intervention. Functioning and resumed-use claims require their own support only when those are the selected subsequent results.

### MNT.9:8 - Common Anti-Patterns and How to Avoid Them

A task is closed because the planned hours were consumed. Record what actually happened and the remaining state. A substituted part is described only as “equivalent” when applicability is material. Preserve the basis that makes it usable in this configuration.

An exhausted specialist is instructed to finish more carefully. Revise relief or timing in response to the actual capability limit.

### MNT.9:9 - Consequences

The tester and operator receive an account that corresponds to the intervention, including its limits. Some work returns for a revised decision rather than being completed under an obsolete plan. Recording costs remain focused on useful later claims and operative retention requirements.

### MNT.9:10 - Architectural Rationale

Performance and its account are joined because later maintenance decisions rely on that correspondence. Separating intervention evidence from functioning and release prevents one completion claim from silently taking on several incompatible meanings.

### MNT.9:11 - SoTA-Echoing

The practice question is how to preserve reliable continuation when work differs from its plan. This pattern adapts the work-management concern in GFMAM's maintenance framework and the fatigue-reporting problem in CASA's 2026 maintenance risk account. Against task-closure-only management, it adds the interruption, actual-state and relief decisions in the Solution. It accepts focused reporting and occasional replanning to avoid concealing incomplete or unsupported work. CASA's aviation account supplies a relevant failure mechanism, not a universal duty-time threshold. Reopen when a new work variant or observed interruption defeats the continuation arrangement. See [GFMAM](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf) and [CASA's fatigue account](https://www.casa.gov.au/operations-safety-and-travel/safety-management-systems/sector-safety-risk-profiles/maintenance-activities-sector-safety-risk-profile/fatigue).

### MNT.9:12 - Relations

[MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the selected intervention, [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) its support and [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) its operative protection and permission. [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) and [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) handle changed timing or shared work. [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) consumes performed-work and configuration evidence; [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) preserves its useful history. [FPF A.13](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/12-a-13---the-agential-role-agency-spectrum.md) and [FPF A.15.1](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/15-a-15-1---u-work-dated-performed-work-occurrence.md) govern precise performer and performed-Work claims when those stronger claims are made.

### MNT.9:End
