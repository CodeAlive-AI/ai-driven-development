## MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work

> **Type:** Method
> **Status:** Stable

### MNT.15:1 - Problem frame

Use this pattern when individually plausible maintenance, operating and support plans cannot be performed together. Two jobs fit their own windows but need the same qualified specialist; an operating fallback depends on equipment that another job intends to isolate.

Recover the actual shared demands and choose a feasible coordination change, or state the unmet combined commitment. A simple resource or dependency bound can be enough. Use [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) or [FPF C.32.MWA.PP](../../../sections/09-part-c---kernel-extension-specifications/83-c-32-mwa-pp---construct-and-compare-method-performance-and-p.md) only when the question requires a broader practice-architecture comparison across different structures.

### MNT.15:2 - Problem

Separate plans can each be valid while their combination is impossible. A Method's steps, actual Work overlaps, System dependencies, provider allocation and authority are different relations. Their descriptions may be drawn as aligned boxes even when the practice does not align that way.

Solving one local conflict can move the burden to operation, an unqualified provider, an exhausted specialist or an unavailable fallback.

### MNT.15:3 - Forces

Shared resources improve utilization while making simultaneous commitments fragile. Combining outages can reduce disruption but increase interference and recovery consequences. Extra capacity can resolve a timing conflict only if it is actually capable, available and permitted. The arrangement must preserve the relevant service and protection conditions as a whole.

### MNT.15:4 - Solution

Name the combined commitment and the conflict that changes it. Use the actual or proposed work and operating horizon. A prospective schedule is not evidence that the work occurred.

Choose only the structures needed to explain the conflict. For a shared specialist, work duration and provider availability may suffice. For simultaneous isolation and fallback, the maintained Systems, operating dependencies and protection authority also matter. A description's nesting does not establish work order or resource independence.

Recover shared demands using compatible quantities and conditions. Distinguish elapsed time from person-hours, nominal capacity from available qualified capacity and sequential dependence from possible overlap. Include common-mode dependencies that could invalidate a fallback or protection assumption.

Compare the whole combination. A condition applying to all selected work cannot be established by approving each job separately. Locate the overload, interference or unsupported transition and determine which alternatives change it: defer a supported job, select another window, obtain another qualified provider, change permitted operating rate or revise the intervention arrangement.

Evaluate what each apparent repair moves elsewhere. A second provider may need access, familiarization and its own support. Deferral changes the failure consequence. A longer shift changes fatigue and protection conditions. A shared outage can remove the recovery option that made each individual plan acceptable.

If the conflict requires a different organization of the practice, use [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) or [FPF C.32.MWA.PP](../../../sections/09-part-c---kernel-extension-specifications/83-c-32-mwa-pp---construct-and-compare-method-performance-and-p.md) to compare the relevant Method, Work, System, provider and description structures. Preserve their actual relations rather than making one universal layer stack. If the simple bound already answers the question, stop there.

Return the selected arrangement or the combined commitment that cannot be met. Identify the people with authority over the changed work and operation. Reopen when a shared resource, interruption, protection condition or service requirement changes.

### MNT.15:5 - Archetypal Grounding

APP-MNT-03 uses a constructed packaging-plant arrangement. Two jobs each require four hours of the same qualified specialist inside one six-hour access window. Their eight-hour combined specialist demand exceeds the six available hours. Each job fits separately; the combination does not.

Preparatory work can overlap continuing production where its access and resources permit. That does not create a second specialist. Reordering two four-hour demands also cannot make their total fit the same six-hour single-person window.

The team compares deferring the lower-consequence job, obtaining another suitable window, using a genuinely qualified additional provider or changing the supported operating arrangement. [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) supplies the consequence of deferral; [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) establishes any added provider's readiness. The selected alternative changes a real constraint rather than the appearance of the schedule.

If an unplanned extension would leave the specialist unable to perform the later protected task adequately, the allocation or timing changes.

For a broader conflict, suppose both jobs rely on the same standby equipment while each plan treats it as independent fallback. The decision now needs the System and operating-dependency structures as well as time. That is a reason to expand the comparison, not to derive an architecture from the schedule's page layout.

The common standby can also affect an action inside a job while the job is under way. Suppose taking a diagnostic reading requires temporarily taking the standby out of service, while that reading is part of locating a fault during service restoration. The broader operating commitment requires the standby to remain available. The diagnostic action is therefore constrained through the restoration and service arrangement. Recover the connection with FPF B.1.5.EW, then compare an applicable alternative diagnostic Method, another supported window or a changed service arrangement. Instrument handling and diagnostic interpretation must both be available; the example supplies no equipment-specific procedure or permission.

### MNT.15:6 - Bias-Annotation

Local planners see their own job's benefits and can assume a shared resource is available because it appears in their plan. Cross-team costs are often assigned to “coordination” without anyone receiving the actual unresolved demand. Name the consuming work and affected operation.

### MNT.15:7 - Conformance Checklist

Does the comparison include every shared demand that can defeat the combined commitment? Are quantities, resource availability and dependencies compatible? Does the selected change alter a real constraint? Are moved burden, failure consequences and protection conditions retained? Do the relevant decision holders control the changed arrangement?

A supported simple bound can complete the question. A comprehensive architecture model is needed only when its additional relations change the answer.

### MNT.15:8 - Common Anti-Patterns and How to Avoid Them

Both jobs are approved, so the programme is assumed feasible. Check the whole shared demand. A second team is added on paper while both depend on the same specialist or tool. Recover the actual independence.

A schedule conflict becomes a universal reorganization project. Use the smallest constraint or structure set that resolves the present coordination question.

### MNT.15:9 - Consequences

The combined arrangement can be judged on actual capacity, service and protection rather than local plan validity. Some commitments are deferred or renegotiated. Broader architectural work remains available when a narrow repair would merely move the conflict.

### MNT.15:10 - Architectural Rationale

[MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) coordinates an intervention with continuing operation; this Method addresses simultaneous commitments whose common conditions cannot be established pairwise. It reuses general cross-structure synthesis only when that larger question is real.

The example's arithmetic is deliberately simple. A more elaborate optimizer is justified by an unresolved decision, not by the existence of several jobs.

### MNT.15:11 - SoTA-Echoing

The question is why individually feasible maintenance plans fail together. This pattern adapts [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md)'s conflict-and-moved-burden comparison to maintenance resources, fallback and protected work. Against copying a work-breakdown diagram as the practice architecture, the Method adds actual-relation recovery and the whole-demand test. It accepts a bounded cross-team comparison to expose a shared constraint while retaining the simple-arithmetic stop. Preparation-aware scheduling research supplies an optional overlap alternative, not proof of independent resources or live effectiveness. Reopen when a new shared dependency or changed operating commitment alters the combination.

### MNT.15:12 - Relations

[MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) supplies ready resources, [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) the consequences of alternative interventions and deferral, and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) the individual operating arrangement. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) preserves protection across shared work. [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) and [FPF C.32.MWA.PP](../../../sections/09-part-c---kernel-extension-specifications/83-c-32-mwa-pp---construct-and-compare-method-performance-and-p.md) support a needed cross-structure architecture comparison. OPS contributes the qualified service and work-management results that the selected coordination consumes.

### MNT.15:End
