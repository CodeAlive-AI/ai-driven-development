## MNT.7 - Coordinate Maintenance Intervention and Continuing Operation

> **Type:** Method
> **Status:** Stable

### MNT.7:1 - Problem frame

Use this pattern when maintenance and operation need one feasible arrangement for access, service continuity and return to use. A repair estimate fits the outage, but shutdown, testing and restoration have not been counted.

Relate the selected intervention's whole demands to the operation's actual service result. Return an actionable timing and operating arrangement, or the unmet condition that prevents it. A recommendation can finish before this coordination is complete. Several jobs that compete across shared resources additionally need [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md)'s whole-combination reasoning.

### MNT.7:2 - Problem

A task duration is not an outage duration. Preparation may occur during operation, while isolation, intrusive work, controlled tests and restoration can consume the service-loss window. Concurrent work can share an access opportunity but also interfere or remove a fallback.

Ignoring the ending conditions is especially costly: a mechanically completed repair can leave the operator without the evidence, configuration or control needed to resume use.

### MNT.7:3 - Forces

A longer window permits more contingency but increases loss of service. Preparation before shutdown can shorten the outage while consuming scarce support. Fallback operation may preserve a contribution at reduced capacity, but only within a qualified demand and duration. The arrangement must account for uncertainty without counting the same allowance twice.

### MNT.7:4 - Solution

Recover the operating commitment for the actual horizon: required service, permissible reduction, applicable fallback and authority over changes. Use a qualified capacity result such as [OPS.10](../../management-dpf-suite/ops/40-ops-10---qualify-operating-capacity-under-variability.md) where relevant. Do not substitute a pump's nameplate rating for the operation's service claim.

Lay out the intervention's dependency and time demands. Separate preparation that can occur without the outage from work that requires shutdown, protected access or a changed operating state. Include the necessary testing and return to control. Some activities can overlap; establish that they do not compete for the same person, equipment, access or protection condition.

Use an elapsed-time model appropriate to the real dependencies. Sum sequential activities; use the critical path only when the supported overlaps are real. Identify whether task estimates already include contingency before adding another allowance. Labour-hours, access-hours and elapsed service-loss time are different quantities.

Compare the resulting demand with the whole available service envelope. If it does not fit, change a real variable: another window, another supported intervention, qualified fallback, additional capable provider, permitted rate adjustment or a justified deferral. A smaller written estimate does not change the work. A rate change is useful only when its service and deterioration consequences are supported.

Agree what happens when a condition changes during the window. The relevant response can be a safe hold, restoration to a supported condition, a separately permitted extension or a revised operating decision. Identify the latest decision point before loss of a viable return becomes consequential. Do not treat an allowance as permission to omit a required check when time runs short.

Return the coordinated arrangement to the people who control operation and maintenance. Preserve the service assumptions, actual resource commitments, protection transitions and stopping conditions that they need to act. The result is qualified by those conditions, not a guarantee that no interruption will occur.

### MNT.7:5 - Archetypal Grounding

The following is the whole-outage calculation for the constructed PS17 application. It is a reasoning example, not an equipment procedure or a time standard. The qualified operating result allows four hours, or 240 minutes, of the stated reduced-capacity operation.

| Selected activity | Elapsed minutes inside the outage | Basis in this constructed plan |
| --- | ---: | --- |
| Controlled shutdown and establishment of isolation | 30 | The applicable protected-access work is included. |
| Selected bearing intervention | 95 | Parts, tools and provider are ready before shutdown. |
| Controlled testing and functioning verification | 45 | Includes the necessary test-state transitions. |
| Final restoration and return of control | 25 | Includes the receiving operator's hand-back work. |
| Explicit contingency | 30 | This is additional to the task estimates, which exclude it. |
| **Whole planned demand** | **225** | Sequential demands; no unsupported overlap is assumed. |

Ninety minutes of preparatory work occurs before the outage and is excluded from its demand. The plan leaves 15 minutes beyond the explicit contingency within the 240-minute operating bound. That arithmetic establishes fit only for the constructed estimates and supported conditions.

If an additional 20-minute demand arises beyond all included allowances, the demand becomes 245 minutes and no longer fits. The team revisits the operating or intervention arrangement. It does not consume testing or hand-back time to preserve the appearance of a four-hour plan.

If the spare applicability return is absent before the planned start, the team does not begin this replacement branch. If the actual isolation cannot be established, the affected protected work does not start. Those limits preserve the earlier completed recommendation and return a different coordination question.

### MNT.7:6 - Bias-Annotation

Repair estimates often reflect the technician's direct work and omit operator preparation, controlled testing or waiting for a release. Name whose time and service loss are counted. A successful previous outage can also hide favourable conditions that are absent now.

### MNT.7:7 - Conformance Checklist

Does the arrangement consume a valid operating-capacity and service result? Are preparation, protected work, testing, restoration and material contingency accounted for without double counting? Are overlaps compatible with actual resources and protection? Is there a supported response when the plan no longer fits?

A coordination result is complete when the responsible people can act on its bounded arrangement or know the unmet condition.

### MNT.7:8 - Common Anti-Patterns and How to Avoid Them

“The repair takes three hours, so it fits” excludes the rest of the outage. Compare complete elapsed demand with the service envelope. Preparation is assumed to overlap operation even though it needs the same isolated machine. Check the dependency before removing it from the outage.

Time pressure can turn contingency into permission to skip restoration evidence. Return to the operating decision when the supported plan expires.

### MNT.7:9 - Consequences

The maintenance and operating commitments refer to one feasible arrangement. Some preparation moves earlier; some work moves to another window. The additional planning effort is justified where it prevents unsupported service promises and identifies the first condition that changes the plan.

### MNT.7:10 - Architectural Rationale

This Method coordinates one intervention with continuing operation. The complete elapsed-time condition belongs here because pairwise task approvals cannot establish whole-window fit. [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) extends that reasoning when several jobs and support arrangements impose simultaneous demands.

Rate adjustment and more advanced scheduling remain options, not compulsory tools. A simple bound can already settle the present question.

### MNT.7:11 - SoTA-Echoing

The practice question is whether maintenance can fit the real operating commitment. This pattern adapts preparation-before-intervention and flexible timing as candidate choices from the bounded scheduling work of Gan and colleagues and Kasuya and Jin. Against repair-duration-only planning, the Method uses the complete elapsed-demand comparison and conditional operating return above. Their models do not supply these constructed times, field effectiveness or permission to change duty. The complete elapsed-time comparison is sufficient when it settles the receiving question. Use optimization or another scheduling model when its attainable improvement in the arrangement or decision warrants the effort. Reopen when demand, preparation dependency or operating capacity changes. See [preparation-aware scheduling](https://journals.sagepub.com/doi/abs/10.1177/09544054251350538) and [flexible-timing research](https://www.sciencedirect.com/science/article/abs/pii/S095183202600342X).

### MNT.7:12 - Relations

[MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) supplies readiness and [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) the selected intervention. [OPS.10](../../management-dpf-suite/ops/40-ops-10---qualify-operating-capacity-under-variability.md) supplies qualified capacity where used. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md)–[MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) govern the actual protection, work, functioning and hand-back returns whose time this Method includes. [MNT.15](26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) handles simultaneous shared demands. A changed service concept returns to operation or engineering rather than being inferred from this maintenance plan.

### MNT.7:End
