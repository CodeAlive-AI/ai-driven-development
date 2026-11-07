## MNT.6 - Diagnose Condition and Choose a Maintenance Response

> **Type:** Method
> **Status:** Stable

### MNT.6:1 - Problem frame

Use this pattern when current condition raises a maintenance choice: repair, replace, adjust, inspect, defer, restrict use or stop. The first suspected cause has attracted a repair proposal, but the practitioner needs to know whether it is the supported and feasible response.

Return the diagnosis needed for that choice and a recommendation or selected maintenance response with its limits. A recommendation is a finished result when it adequately answers the request. Selecting an intervention does not establish its permission, perform it or demonstrate restored functioning.

### MNT.6:2 - Problem

Diagnosis can become either premature certainty or an endless search. A plausible cause triggers the first familiar repair; alternatively, advice is withheld until every possible root cause is eliminated. Both lose the practical question: which remaining uncertainty changes what should be done now?

A technically effective repair can also be worse than another response when access, support, service loss or intervention-induced faults are considered.

### MNT.6:3 - Forces

Waiting may allow deterioration or loss of service; acting early may waste useful life and create new faults. More diagnosis can narrow the choice but delay a necessary response. A reversible restriction can preserve useful operation while reducing demand, but only within its supported and permitted envelope. Compare these consequences without treating urgency as evidence of either cause or authority.

### MNT.6:4 - Solution

Begin with the requested decision and time horizon. Recover the relevant required function, current condition and failure account. Use already adequate evidence before asking for more. Separate the diagnosis supported now from the stronger causal account that may remain unresolved.

Form the alternatives that can answer this case. Include retaining the present arrangement, deferring with stated conditions, restricting operation, targeted inspection and stopping when they are plausible responses. Repair and replacement can have different support, downtime and recurrence consequences. A candidate without the means or authority for its actual performance can remain a recommendation, but it is not a feasible immediate act.

Compare the alternatives at the same required use. Explain what failure or condition each addresses, the consequence of delay, the expected intervention effect and its material uncertainty. Include disturbance, introduced defects, access, support, service loss and later restoration. Do not conceal an unacceptable condition by averaging it into a favourable cost score.

Test whether the remaining diagnosis uncertainty changes the choice. If all plausible mechanisms justify the same bounded response, give that response with its supported explanation. If one mechanism favours replacement and another would make it ineffective, seek the smallest worthwhile discrimination. State the result needed from a specialist rather than commissioning an unrestricted investigation.

Use [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) where support and operation can change feasibility. A part awaiting applicability evidence can block installation while leaving replacement at a suitable future outage as the best recommendation. If no feasible alternative preserves the required use, return the precise unmet condition to the appropriate operating or engineering decision.

State the chosen answer in ordinary terms: what to do or recommend, for which unit and configuration, under which conditions, why it is preferable and what would reopen it. Retain only uncertainty and conditions that change the recipient's use. If the request is for advice and the answer is adequate, stop.

For performance of a selected intervention, carry the selected scope to [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) and MNT.9. When an operative requirement is disputed, appraise its merits separately: the protected party, relevant harm, baseline and marginal protection, whole burden and displaced harm matter. Preserve present force while the authorized holder considers an amendment. A maintenance recommendation does not amend that requirement.

### MNT.6:5 - Archetypal Grounding

For PS17 in configuration C41, the constructed decision is how to meet the required normal duty after the next planned outage, not how to guarantee an indefinite bearing life. [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies the abnormal, increasing condition account; vibration magnitude alone does not choose replacement. The case additionally supplies an existing machine-specific inspection and diagnostic account identifying a localized defect in the installed bearing's rolling contact. Its relevant mounting and lubrication findings support replacement under the unchanged design basis rather than correction of an ongoing mounting or lubrication defect. These are explicit diagnostic premises for this teaching case, not conclusions obtainable from the three vibration values alone.

The operating assessment supplies a distinct premise: a permitted lower-duty assignment for this unit still meets the full present district-heating demand until the planned outage two days away. This is not XRI-09's reduced-capacity outage, whose separate bound remains four hours. Normal demand then returns, and that lower-duty assignment cannot meet it. This two-day boundary is a service and supported-use boundary, not a predicted time to bearing failure. Continued use remains within the supplied condition and protection limits; losing one of those limits reopens the operating response immediately.

| Live response | Effect and consequence under the supplied case conditions | Place in the answer |
| --- | --- | --- |
| Continue unrestricted use without intervention | Leaves the diagnosed defect in place, while the available condition assessment does not support unrestricted normal-duty use over the receiving period. | Does not provide a supported answer to the required use. |
| Use the permitted temporary restriction | Reduces the present demand on the affected unit and meets current service needs within its supported conditions; it neither removes the defect nor supplies the later normal duty. | A usable bridge to the outage, not a substitute for restoration. |
| Replace the applicable bearing at the planned outage | Removes the identified local defective component. Preparation, testing and hand-back provisionally fit [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md)'s 225-minute demand within the 240-minute bound. Replacement introduces intervention risk and still needs applicable parts, protected work and functioning verification. | The supported restoration recommendation, conditional on those operative requirements. |
| Stop immediately | Avoids further running of the affected unit but causes service loss that the permitted bridge avoids under the present facts. | Not the preferred present response; return to the operating/protection decision if the bridge loses its supported conditions. |

The recommendation follows from the combination: the restriction meets only the short receiving need, whereas replacement addresses the identified defect and has a bounded usable opportunity before normal demand returns. Neither the vibration rise nor the availability of an outage would establish that comparison alone. The spare applicability/certification return remains outstanding. The finished advice is therefore “use the supported temporary arrangement and recommend replacement at the suitable outage, subject to applicable part and operative work conditions,” not “begin replacement now.” If the part or full window does not become usable, the team must reopen the service arrangement; it cannot silently extend the temporary restriction.

Why this bearing deteriorated earlier than comparable units remains unresolved. The supplied diagnostic basis supports removing the present local defect, but does not establish that replacement prevents every recurrence. That stronger causal uncertainty does not defeat this bounded recommendation; it limits the claim to the present restoration question. Actual resulting functioning and resumed-use authority still require their separate [MNT.10](21-mnt-10---verify-restored-functioning-after-maintenance.md) and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) returns.

Suppose an existing inspection instead shows that a shared mounting defect would make another bearing replacement ineffective. That evidence changes the alternatives and reopens the choice. The team returns the mounting or engineering question instead of repeating the same repair.

In the shared-specialist case, a less urgent job can be deferred only if its failure consequence and operating conditions support that choice. The arithmetic showing that both jobs cannot fit identifies the conflict; it does not decide which consequence to accept.

### MNT.6:6 - Bias-Annotation

The available spare, a recent training course or a vendor's diagnostic label can make one intervention disproportionately salient. Explicitly compare a plausible no-change or less intrusive alternative when it can satisfy the same use. Include the burden borne by operation and maintenance staff, not just the repair budget.

### MNT.6:7 - Conformance Checklist

Does the diagnosis support the actual decision rather than a stronger unnecessary claim? Have the plausible alternatives been compared at the same use and horizon? Are response feasibility, service effects and material uncertainty visible? Is the result clearly advice, a selected act or an unresolved decision?

An adequate recommendation closes the advice request. Any selected further inquiry has an attainable action-changing contribution; actual performance retains its particular conditions.

### MNT.6:8 - Common Anti-Patterns and How to Avoid Them

“Fault detected, replace component” skips the question of whether the replacement addresses the failure. Compare its expected effect with the supported mechanism. “Root cause not proven, no advice possible” withholds a smaller answer even when all remaining causes support it.

A conditional recommendation is then treated as permission. Carry the condition into the receiving work decision rather than dropping it when the work order is opened.

### MNT.6:9 - Consequences

The recipient obtains a timely, qualified choice and knows what is still needed for a different or stronger use. Some investigations stop; some interventions are deferred or redirected. Residual uncertainty remains explicit without becoming a blanket reason to delay every maintenance result.

### MNT.6:10 - Architectural Rationale

Diagnosis and present intervention choice belong together because the required diagnostic resolution depends on the alternatives. Policy remains separate because a reusable task rule can be sound while this case requires an exception. Permission and functioning evidence remain separate because they answer different questions about the selected act.

### MNT.6:11 - SoTA-Echoing

The practice question is how condition knowledge becomes an actionable maintenance answer. This pattern adapts the prediction-to-action gap identified in the 2025 prescriptive-maintenance synthesis into explicit diagnosis, alternative comparison and feasibility returns. Against automatic repair from a prediction, the Solution adds the action-changing uncertainty test and a sufficient-recommendation stop. The source's abstract-level contribution does not establish a deployed autonomous algorithm or a particular repair rule. [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) supplies the general conditional-inquiry reasoning. Reopen when a new mechanism, feasible alternative or consequence changes the answer. See [the author-deposited source](https://orbilu.uni.lu/handle/10993/65591).

### MNT.6:12 - Relations

[MNT.1](12-mnt-1---identify-the-maintained-system-use-and-permission-bo.md), [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) and [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supply the bounded question, failure account and condition. [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) qualify feasible performance. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) governs actual intervention permission; [MNT.9](20-mnt-9---perform-and-record-the-maintenance-intervention.md)–[MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) supply performance, functioning and hand-back results when selected. [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) supports comparison and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) supports advice and evidence-demand appraisal.

### MNT.6:End
