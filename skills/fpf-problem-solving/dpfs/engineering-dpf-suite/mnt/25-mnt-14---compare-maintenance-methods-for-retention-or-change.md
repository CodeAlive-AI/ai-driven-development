## MNT.14 - Compare Maintenance Methods for Retention or Change

> **Type:** Method
> **Status:** Stable

### MNT.14:1 - Problem frame

Use this pattern when an established way of doing maintenance may no longer be the best answer for the current failure, equipment or operating setting. A new predictive tool is proposed, or a once-useful inspection produces little actionable information.

Compare the pertinent Methods and return a justified retain, revise, replace, branch or stop decision. Here a Method is the reusable way of obtaining a maintenance result; a software product or manual can support or describe it. A new trial is selected only when it can provide worthwhile attainable information.

### MNT.14:2 - Problem

A Method can appear superior because it was evaluated on easier equipment, a different consequence or a narrower burden. Changing the tool can be advertised as changing the Method even when the practitioner does the same work. Conversely, a small change in interpretation or response can materially change the Method while leaving the software unchanged.

A useful comparison needs the same receiving maintenance question, supported alternatives and a truthful account of what changes in practice.

### MNT.14:3 - Forces

New Methods can improve detection or response while adding training, integration, false alarms and dependence on a supplier. Keeping a familiar Method reduces transition cost but can retain an ineffective task. A controlled trial can reduce uncertainty, but a small fleet or restricted access may make its promised answer unattainable.

### MNT.14:4 - Solution

State the maintenance result and conditions for the comparison. Recover the failure mechanism, consequence, condition information, support, access and operating needs that can change the answer. Compare the current Method with plausible alternatives at that same use.

Describe the action-changing difference. Is the candidate a different task, a changed trigger, another diagnostic interpretation, a revised response rule or only a different description or software implementation? Keep those objects distinct when continuity, training or evaluation depends on them. A useful Method change should alter what the practitioner notices, decides, does, needs or obtains.

When a useful predictive alternative still has to be constructed, use [MNT.2:4.1.1](13-mnt-2---select-and-reopen-the-maintenance-policy.md#mnt2411---build-and-improve-a-predictive-maintenance-option) to connect the estimate, intervention rule and obtainable support. Bring back an executable option and its consequence comparison. This can include changing preparation or access, or improving the forecasting rule through the interventions it selects. Use already adequate alternatives directly.

Compare practical worth over a relevant horizon. Include preparation, acquisition, configuration, competence, interpretation, false responses, missed conditions, maintenance of the tool, supplier dependence and exit where they matter. Use [FPF C.11.MV](../../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md) for the practical-worth comparison and [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md) when variant identity or maintenance of the repertoire needs that more general Method.

Test the candidate against a consequential unlike case. A Method useful for a visible degradation trend may not expose a hidden protection failure. An online predictor may improve timing while remaining unusable where the support lead time is longer than its warning. These differences can justify branching the repertoire instead of replacing one Method everywhere.

Choose a feasible change when current observations, an applicable model or a reasoned expert estimate make its expected improvement worth the transition and continuing burden. Name the first executable move and obtain the support it needs. A sufficient comparison can justify beginning the change before its eventual benefit has been observed; retain the distinction between that expected benefit and the outcome subsequently obtained.

Use existing evidence first. If it already establishes that the candidate cannot support the needed response, reject it for that use without a trial. If it supports retaining the current Method, return that decision. When an uncertainty could change the choice, assess what a feasible trial or analysis could actually discriminate and the whole burden of obtaining that result. Do not turn a possible study design into an obligatory next task.

Select the supported continuation. State the changed or retained Method and its applicability, the description or tool that will carry it, any real transition support and the condition for reopening the choice. A selected change remains a proposal until performed. Claims about improved maintenance outcomes require evidence at the relevant use, not just successful installation of a tool.

Refresh selectively when a failure, operating condition, support arrangement or answer-changing source result changes. An annual reminder can prompt attention, but currentness is established by the comparison that matters, not a date stamp.

### MNT.14:5 - Archetypal Grounding

A constructed fleet comparison considers replacing periodic condition interpretation with an online predictive service. The new service produces a more frequent remaining-life estimate, but the recurring maintenance decision is whether an actionable warning arrives in time for applicable support and access.

For the current use, existing provider information shows no improvement in the feasible response: the same specialist and part constraint dominates, while the new arrangement adds interpretation and integration work. The engineer retains the current Method and addresses the support deficiency. No new live trial is needed to answer that question.

A different unit family has a supported rapidly changing condition and a genuinely available response. The candidate may be useful there. A bounded comparison can therefore select a separate Method variant instead of a fleet-wide replacement, provided the obtainable evidence warrants the change.

In PS17, long-horizon recurrence remains unresolved after the local repair. The current account can be retained while a future Method comparison is reserved for evidence that changes the policy or response. “Complete a new trial” is not a universal stop condition.

### MNT.14:6 - Bias-Annotation

Technology labels and benchmark accuracy favour visible novelty. Familiarity favours the incumbent. Compare both for the same maintenance result, including burdens and effects outside the team purchasing the tool.

### MNT.14:7 - Conformance Checklist

Are the compared Methods and their practical differences identifiable? Do they answer the same maintenance question under comparable conditions? Are their differing implementation, transition and continuing burdens compared where material? Does the decision preserve unlike uses through an appropriate retain, branch or replacement result?

Any trial has an attainable decision-changing purpose. A supported comparison can close without new experimentation or adoption.

### MNT.14:8 - Common Anti-Patterns and How to Avoid Them

A higher model score is treated as a better maintenance Method. Follow the prediction through interpretation, support and actual response. A software upgrade is called a Method change without an action-changing difference. State what the practitioner does differently.

A comparison ends only after a trial because the template requires one. Use current evidence when it already settles the choice; select a trial only for the remaining worthwhile uncertainty.

### MNT.14:9 - Consequences

The maintenance repertoire changes where practical evidence warrants it and remains stable where it already works. Some new approaches are retained as bounded variants rather than universal replacements. Transition and continuing support costs become part of the choice.

### MNT.14:10 - Architectural Rationale

Method refresh concerns the reusable way of obtaining results and its continued usefulness. Adjusting a policy parameter within that way's declared range, or executing one repair, need not change the Method. A changed trigger, response rule or applicability can require the comparison above even when it is expressed by changing one parameter.

### MNT.14:11 - SoTA-Echoing

The practice question is when a new maintenance approach is worth adopting. This pattern adapts [FPF C.11.MV](../../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md), [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md) and the consequence-oriented line in the [2025 NIST review](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial). Against a predictive-to-autonomous maturity ladder, the Method uses a same-use, whole-burden comparison with retain and branch outcomes. Better prediction remains a possible contribution, not a sufficient adoption argument. The source evidence does not establish universal comparative effectiveness. Reopen with an attainable new capability, changed failure or operating need, or evidence that reverses the practical comparison.

### MNT.14:12 - Relations

[MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md) supplies policy questions; [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) supplies failure knowledge and MNT.4 supplies condition knowledge; [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and MNT.7 supply response feasibility; [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) supplies programme consequences. [FPF C.11.MV](../../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md) supplies practical-worth comparison and [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md) Method-variant maintenance. [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) governs a demanded trial's contribution and burden, while [FPF G.11](../../../sections/13-part-g---discipline-sota-patterns-kit/13-g-11---decide-whether-and-how-to-refresh-sota-packs-and-rela.md) supports selective refresh.

### MNT.14:End
