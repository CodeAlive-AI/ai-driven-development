## MNT.10 - Verify Restored Functioning after Maintenance

> **Type:** Method
> **Status:** Stable

### MNT.10:1 - Problem frame

Use this pattern when a performed maintenance task is being used to claim that the System can again support its required use. A bearing replacement is complete, but the receiving operator needs evidence about functioning under the relevant configuration and load.

Establish the functioning claim that the available evidence supports, or return its unsupported portion. “Restored” means adequate for the stated use and envelope; it need not mean as-new equipment or absence of every defect. [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) handles the distinct permission and transfer of control for resumed use.

### MNT.10:2 - Problem

A completed procedure can leave the original problem unresolved or introduce another fault. An unloaded spin can appear successful while a loaded duty fails. Conversely, repeating every earlier test wastes time when the intervention did not affect those claims and their earlier evidence remains applicable.

The check must be able to reveal the defect that would invalidate the receiving functioning claim.

### MNT.10:3 - Forces

Representative testing improves evidence but can consume the outage and create its own controlled exposure. A short test can support an immediate operating claim while leaving long-horizon reliability unresolved. Stronger assurance may require a specialist or independent return; its value and requirements depend on the actual consequence, not the number of signatures collected.

### MNT.10:4 - Solution

State the required functioning claim, actual configuration, operating envelope and relevant horizon. Recover the operating and engineering acceptance basis. Select the performance, protection or interaction properties whose failure would change the return-to-use decision.

Relate the intervention to those claims. Identify the functioning it was intended to restore and credible faults it could have introduced. Use current adequate evidence for unaffected claims where its subject, conditions and scope still fit. A component or configuration change that invalidates that evidence reopens the affected check.

Choose checks that can discriminate the relevant success and failure states. Use the applicable equipment procedure, measurement basis and competent providers. Where real operating conditions cannot be represented, state what the test does and does not establish. A measurement needs suitable range, uncertainty and operating context for its acceptance comparison.

Plan the check's controlled state transitions with [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) and its time with MNT.7. Verification that requires energization or other exposure does not inherit unrestricted permission from the earlier protected repair. The applicable procedure governs how the test state is established and ended.

Compare observed outcomes with the stated basis. Retain the actual subject, load, duration and material limitations. A passing result supports the named claim only at that scope. A failed result returns to the affected diagnosis, intervention or engineering question; unrelated passing tests do not cancel it.

Return qualified functioning evidence. A restricted-use claim may be supportable when unrestricted use is not, provided the relevant acceptance and authority conditions allow that distinction. Certification or an independent check is obtained where the concrete use requires it. Do not impose one on every functioning question, or omit an operative one merely because a task looks routine.

Stop when the receiving functioning question is adequately answered. A recurrence or life-extension claim may remain unresolved without defeating the narrower current-use result. Select further evidence only when its obtainable contribution or operative requirement justifies it.

### MNT.10:5 - Archetypal Grounding

For the extended constructed PS17 case, the tested installed configuration is C42, with the bearing replacement recorded in MNT.9. The following values are invented to demonstrate a comparison; they are not pump acceptance limits.

The case's agreed immediate-duty basis requires at least 20 litres per second at a differential pressure of at least 150 kilopascals during a 30-minute representative run. Its supplied acceptance rule is simple comparison of the reported values with those limits, using an already qualified measurement basis for this range and duty. The premise includes a prior assessment of calibration and measurement uncertainty, with the resulting decision risk accepted for this limited claim; it does not assume zero uncertainty or make simple comparison suitable for every use. Instrument drift or changed measurement conditions that invalidate that assessment reopen the comparison.

Under those supplied conditions, the constructed observation is 20.8 litres per second at 154 kilopascals throughout that run, with the applicable equipment-specific condition checks also satisfied: 20.8 exceeds 20 and 154 exceeds 150 under the stated rule. The 45-minute test allowance in [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) includes this run and its controlled transitions.

Those observations support the stated immediate duty in the tested envelope. They do not establish performance at an untested winter peak, an as-new lifetime or elimination of the long-horizon recurrence mechanism. The operator receives that scope explicitly.

If the loaded test instead reaches only 18 litres per second, the performed bearing replacement can still be correctly recorded while the required functioning claim fails. The team returns to diagnosis or the relevant engineering question. A test record with a completed checkbox cannot convert that result into restored service.

### MNT.10:6 - Bias-Annotation

The effort already spent on repair creates pressure to interpret a marginal test as success. A familiar easy-to-measure property can also displace the required operating contribution. State the acceptance basis before reading the outcome where that prevents retrospective adjustment.

### MNT.10:7 - Conformance Checklist

Does the evidence concern the actual resulting configuration and required use? Can the selected checks expose the intervention's relevant failure or introduced fault? Are measurement and test conditions suitable for the claim? Are unchanged evidence and unresolved portions used at their true scope? Are required specialist or independent returns present where applicable?

A supported current-use answer closes this question. It does not claim long-term reliability or authorize resumed use by itself.

### MNT.10:8 - Common Anti-Patterns and How to Avoid Them

“Part replaced” is used as evidence of service. Test the functioning the recipient actually needs. “It ran unloaded” becomes permission for full-duty operation. Qualify the operating envelope or obtain the evidence that changes that use.

Every historical test is repeated after a small change. Reopen the claims actually affected, while preserving any concrete requirement for the current verification.

### MNT.10:9 - Consequences

The operator receives an applicable functioning result and can distinguish it from completed maintenance work. Some repairs return for further action; some systems support only a narrower use. Verification effort is concentrated on claims and consequences rather than repeated by checklist inertia.

### MNT.10:10 - Architectural Rationale

The Method is separate from both intervention and release because their outcomes can differ. A task can be performed correctly without restoring the required contribution, and functioning can be established while control or permission remains unresolved.

Claim-specific checking permits adequate prior evidence to remain useful. It also makes a genuine configuration or load change visible as a reason to reopen the affected conclusion.

### MNT.10:11 - SoTA-Echoing

The practice question is what evidence warrants a restored-functioning claim after maintenance. This pattern adapts [FPF B.3](../../../sections/08-part-b---trans-disciplinary-reasoning-cluster/17-b-3---is-this-claim-supported-for-this-use-trust-and-assuran.md)'s use-specific assurance and [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md)'s measurement discipline to intervention-induced failure and operating-envelope checks. Against task-sign-off or indiscriminate retesting, the Method selects checks for the functioning claims and reuses adequate evidence for unaffected claims. The PS17 comparison under load illustrates this reasoning. The trade-off is retaining an explicitly limited immediate-use result instead of claiming lifetime restoration. Equipment procedures supply the concrete acceptance criteria; this synthesis does not establish universal test values. Reopen when configuration, required duty, consequence or the earlier evidence's applicability changes.

### MNT.10:12 - Relations

[MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) supplies the required functioning and [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md) the performed intervention and resulting state. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) governs test protection; [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) includes its time. [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) consumes the supported functioning claim for hand-back. [MNT.12](23-mnt-12---maintain-maintenance-information-and-configuration.md) retains the useful evidence and [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) addresses later recurrence learning. [FPF B.3](../../../sections/08-part-b---trans-disciplinary-reasoning-cluster/17-b-3---is-this-claim-supported-for-this-use-trust-and-assuran.md), [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) and [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) support assurance, evidence and measurement.

### MNT.10:End
