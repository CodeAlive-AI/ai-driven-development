## MNT.8 - Isolate, Make Safe, and Authorize the Maintenance Intervention

> **Type:** Method
> **Status:** Stable

### MNT.8:1 - Problem frame

Use this pattern when a selected maintenance intervention will expose people, equipment or the environment to a hazard that requires controlled access, isolation or other protection. A work order is ready, but the actual protection and permission for the proposed act have not been established.

Use the applicable equipment procedure and competent authorized people to establish, verify and maintain those conditions. Return a supported permission to begin the bounded work or the unmet condition. This framework gives maintenance reasoning, not a substitute isolation procedure. A diagnosis-only or recommendation-only answer is not forced through an intervention-permission task.

### MNT.8:2 - Problem

Stopping normal operation does not by itself establish control of every relevant exposure. Stored energy, reaccumulation, shared supplies, remote commands or simultaneous work can leave an intervention unsafe. A permit can state a required condition while the actual machine remains in another state.

Permission and protection also change with the scope of work, crew, shift or test configuration. A correct initial condition can cease to apply.

### MNT.8:3 - Forces

Protection must address the actual hazard and intervention without becoming an unrelated paper exercise. An urgent service need may increase pressure to proceed, while an overbroad restriction may displace harm or prevent useful work. The merits of a requirement and its present operative force are separate questions; neither urgency nor paperwork answers both.

### MNT.8:4 - Solution

Recover the proposed work scope, actual configuration, relevant hazards and applicable procedure. Qualified people determine the equipment- and jurisdiction-specific controls. If the procedure's applicability or the authority to act is unresolved, return that limit before the affected work begins.

Trace the exposure paths needed for the intervention. Depending on the equipment, these can include electrical, mechanical, hydraulic, pneumatic, thermal, chemical or other sources, including stored or reaccumulating energy. This list is illustrative: the applicable procedure and actual hazard analysis establish the set for the job. A control-system stop command is not assumed to be an energy-isolating measure.

Establish the selected isolation and protective conditions through the applicable procedure. Verify the condition that protects the people who will perform the work, using the required competent personnel and suitable means. A signed statement is evidence only to the extent that it supports the actual condition and applicable authority.

Coordinate people whose work can alter that condition. Where contractors, groups, shift changes or simultaneous jobs are involved, maintain the required protection and control through those transitions. A person leaving the work area does not by itself resolve the transfer of protection or permission.

Define the bounded permission for the actual intervention: permitted scope, configuration, protection conditions and the material change that requires a hold or revised decision. During work, respond to a loss of protection or an unexpected condition using the applicable safe hold, restoration or reassessment procedure. Testing that needs an energized or otherwise changed state has its own controlled transition; initial isolation does not authorize any later test state.

If a requirement's merits are disputed, use a separate appraisal. Identify the protected bearer, relevant harm and causal basis, baseline and incremental protection, whole burden and displaced harms. Compare harmful relaxation with harmful retention or tightening, and name who may amend the requirement. Until an authorized change applies, preserve current force. This separation permits substantive criticism without turning a framework discussion into permission to bypass a control.

Return permission only for the supported work and conditions, or state the missing protection, applicability or authority. Keep evidence proportionate to the actual reliance and applicable requirements.

### MNT.8:5 - Archetypal Grounding

In the constructed PS17 case, the specialist part return has arrived and the planned outage is feasible. The authorized personnel still establish the applicable isolation and access conditions for the actual configuration before the bearing intervention.

Suppose they discover that a shared path can reintroduce energy and the assumed isolation does not control it. The protected work does not begin. They return the actual discrepancy for the required competent decision and revise the outage arrangement if necessary. The earlier replacement recommendation remains a completed answer.

In the extended branch, the applicable procedure establishes and verifies protection. The permission covers the selected bearing work, not unrestricted work on neighbouring equipment. A later test that requires a changed operating state uses its applicable controlled transition. Successful testing and final hand-back remain separate results.

OSHA 29 CFR 1910.147 provides a US jurisdiction-bounded illustration of energy-control, verification and restoration requirements, with its own scope and exclusions. Its presence here does not establish that this standard governs PS17 or supply a complete procedure for another installation.

### MNT.8:6 - Bias-Annotation

A familiar machine can make practitioners underestimate changed stored energy, configuration or shared work. A permit's visible completion can also displace attention from the condition it is meant to establish. Recover the actual protection at the point where it matters.

### MNT.8:7 - Conformance Checklist

Is the procedure applicable to the actual intervention and configuration? Have competent authorized people established and verified the required protection? Do shared work and planned state transitions preserve it? Is the permission bounded to the supported scope, with a usable response to material change?

These questions apply to the selected intervention. They neither require a permission package for advice nor authorize omission of operative protection because a recommendation is already complete.

### MNT.8:8 - Common Anti-Patterns and How to Avoid Them

“The machine is stopped” is used as an isolation claim. Establish the applicable exposure controls and their verification. “The permit is signed” is used as proof of the actual state. Check the correspondence between the permission and protection in place.

A disputed requirement is silently relaxed to meet the window. Keep its merits appraisal separate and obtain any amendment from the holder of the relevant authority.

### MNT.8:9 - Consequences

The intervention proceeds only within a supported protection and permission boundary. Some jobs stop or change scope before exposure occurs. The Method adds no claim of universal safety; its result is conditional on the actual procedure, competent performance and continued applicability.

### MNT.8:10 - Architectural Rationale

Selection, protection and performance are distinct because each can be adequate while another remains unresolved. Keeping action-specific protection here preserves the ability to finish useful advice without weakening any condition governing actual work.

A generic framework cannot enumerate every equipment hazard or jurisdictional exception. It therefore governs how the applicable protection is recovered and used, while the qualified procedure supplies the concrete acts.

### MNT.8:11 - SoTA-Echoing

For the question “What supports beginning this protected intervention?”, this pattern adapts the actual-control and verification logic illustrated by [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147). Against a stop-command or permit-only default, the Method adds verified protection, bounded permission and controlled changes of state. The source is an operative US example within its scope, not a universal maintenance law; the local application needs its actual current requirements. [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md) and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) distinguish permission from requirement merits. Reopen when work, configuration, exposure, personnel transition or the applicable rule changes.

### MNT.8:12 - Relations

[MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md) identifies the relevant unit, use and control. [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) establish support and timing; [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) selects the proposed work. [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md) performs within the resulting conditions, while [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) use controlled testing and restoration for their different results. [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md) governs permission, [FPF A.2.2](../../../sections/05-part-a---kernel-architecture-cluster/10-a-2-2---system-capability-conditions-measures-and-fit.md) capability and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) a requirement-merits appraisal.

### MNT.8:End
