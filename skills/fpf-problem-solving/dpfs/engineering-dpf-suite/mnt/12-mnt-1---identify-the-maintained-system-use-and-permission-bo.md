## MNT.1 - Identify the Maintained System, Use, and Permission Boundary

> **Type:** Method
> **Status:** Stable

### MNT.1:1 - Problem frame

Use this pattern when a maintenance request names equipment but leaves unclear what must keep working, in which configuration, for whom or under whose control. A planner asked to “fix PS17” needs a sufficiently bounded question before choosing a task or promising an outage.

Identify the maintained System, its required use and the decisions that control access and return to operation. The first useful result is a question that the maintenance practitioner and the receiving operator understand alike. If those values are already clear and adequate, use them directly. Selecting a replacement bearing belongs in [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md); changing the plant's service concept belongs with the responsible engineering and operating decisions.

### MNT.1:2 - Problem

A stock number identifies a replaceable part, an equipment tag identifies a unit and an operating commitment identifies a required contribution. They answer different questions. Repairing the tagged unit can still leave the required service unavailable when a shared controller, cooling supply or bypass is outside the assumed boundary.

Unclear control makes the same mistake consequential: the person requesting a recommendation may be unable to stop the equipment, authorize intrusive work or accept restricted operation. Knowing that distinction early prevents a recommendation from becoming an unsupported commitment to act.

### MNT.1:3 - Forces

A narrow boundary keeps the question answerable, but omitting a shared dependency can make the answer unusable. A broad inventory may reveal more equipment while delaying the urgent decision. Required functioning also varies with load, season and time horizon; a configuration adequate for reduced summer demand may be inadequate for peak demand. The useful boundary includes what changes this maintenance answer, not everything connected to the machine.

### MNT.1:4 - Solution

Begin with the requested result: condition interpretation, policy choice, intervention recommendation, actual repair, functioning evidence or return to use. Ask what decision will consume it and by when. This often resolves apparent disagreement: the engineer can finish advice today although the repair remains unready.

Locate the actual unit and maintenance-relevant configuration. Reconcile its tag with installed constituents and applicable descriptions only where a difference could change the answer. For a bearing decision, the actual bearing arrangement and shaft assembly matter; an unrelated cabinet-label discrepancy may not. Preserve an unknown configuration as unknown until it is resolved for a use that needs it.

State required functioning as an observable contribution under an operating envelope. For example, “circulate heating water for the east district at the agreed seasonal flow and pressure” is more useful than “pump healthy.” Include the horizon, permissible loss of service and any qualified fallback. Obtain those operating values from the responsible operation; maintenance does not invent a capacity allowance.

Then trace the few interactions that can change the decision. A shared electrical supply can prevent simultaneous isolation; a standby pump can preserve service only if it is actually available under the same conditions. Identify affected people and other Systems when their exposure, access or service loss changes the alternatives.

Recover control at the point where it matters. Establish who can request and receive advice, permit access, stop operation, authorize the proposed intervention and resume use. One person may hold several of these roles, but possession of one authority does not establish the others. For an advice-only request, resolve only authority questions that constrain the recommendation or its interpretation.

Return the bounded question in the existing work discussion or record. A useful concise form is: “For this unit and configuration, under this required use and horizon, decide this maintenance question; this operating limit and this unresolved fact can change the answer.” A separate inventory or new form is unnecessary when the current record already supplies those values.

For a consequential reliance claim, inspect the identity evidence, operating-source applicability and actual permission basis. Recognition of the right equipment is a lighter claim than assurance that a proposed act is permitted. A disagreement about the merits of a requirement belongs in a separate appraisal under [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md); it does not silently alter present authority.

### MNT.1:5 - Archetypal Grounding

In the constructed PS17 case, the request on 18 September 2026 concerns PumpTrain-PS17-B in configuration C41. Its bearing vibration is rising. DistrictHeatingOperation-East can tolerate the agreed reduced-capacity state for four hours; the operating capacity result supplies the applicable demand and standby assumptions.

The first question is “Should we recommend a bearing replacement at the next suitable outage?” It is not yet “May we dismantle the bearing now?” The planner identifies the installed bearing arrangement and retains the specialist applicability return needed for a replacement. The operating controller retains the stop and resume decisions.

This boundary permits a supported recommendation while the replacement-part return is outstanding. If the standby train later becomes unavailable, the four-hour allowance is no longer usable on its earlier basis. The recommendation's service assumptions and scheduling branch reopen; an unrelated equipment inventory does not.

For a small noncritical fan with an unambiguous tag, known function and a currently applicable work procedure, the existing identification can be enough. Rebuilding the whole plant's asset hierarchy adds no value to that task.

### MNT.1:6 - Bias-Annotation

Equipment registers favour named, owned assets. Shared utilities, contractor access, operators and people affected by loss of service can be less visible. Follow the actual consequence and control relation when it changes the question, even if the relevant party has no row in the maintenance database.

### MNT.1:7 - Conformance Checklist

For the requested use, can the recipient identify the actual maintained unit and the configuration distinctions that affect the answer? Is required functioning tied to the relevant operating envelope and horizon? Are material service dependencies and loss allowances supported? Are access, intervention and resumed-use authorities distinguished where they change the next act?

An adequate existing answer closes this identification task. These questions do not require a complete inventory, a new permission record for advice or examination of unaffected constituents.

### MNT.1:8 - Common Anti-Patterns and How to Avoid Them

“Fix asset 204” leaves the required service unstated. Recover what the unit must contribute before treating a component-level success as the answer. Conversely, expanding a bearing question into an enterprise-wide asset study postpones the useful result; include only answer-changing dependencies.

A requester's urgency can also be mistaken for operating authority. Return the recommendation to that requester while obtaining any actual intervention decision from its proper holder.

### MNT.1:9 - Consequences

The maintenance practitioner can direct evidence and effort toward the same use that the operator needs. The cost is a small amount of boundary reconciliation, sometimes revealing that the question cannot yet be answered as phrased. A bounded recommendation remains useful even when an operating or permission limit blocks the proposed work.

### MNT.1:10 - Architectural Rationale

Function, configuration and control are identified together because each can invalidate the same apparently sensible repair. Making them one entry Method is less costly than diagnosing the wrong unit and correcting the plan later. It does not make this entry compulsory: direct condition, policy or fleet questions can start from already adequate identification.

Maintenance retains the function-in-use question. Broader investment, disposal and service redesign remain decisions of their own practices.

### MNT.1:11 - SoTA-Echoing

The practice question is which boundary makes maintenance advice useful. This pattern adapts the function-and-maintenance-regime relationship in IAM's 2024 *Anatomy of Asset Management*, §7.7.5, and uses [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) for configuration identity. Against a register-only starting point, it adds the required-use and control reasoning in the Solution and PS17 case. It accepts a small identification cost to avoid a wrong-subject or wrong-service answer. IAM's broader discipline does not become this pattern's scope. Reopen the boundary when a changed use, installed configuration or shared dependency changes the maintenance decision. See [IAM's account](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf).

### MNT.1:12 - Relations

[MNT.2](13-mnt-2---select-and-reopen-the-maintenance-policy.md) uses the bounded functioning question to select a policy; [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) and [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) use it to interpret failure and condition. [MNT.8](19-mnt-8---isolate-make-safe-and-authorize-the-maintenance-inte.md) and [MNT.11](22-mnt-11---hand-back-and-authorize-resumed-use-after-maintenan.md) develop the action-specific permission and return-to-use results. [FPF A.1.SCR](../../../sections/05-part-a---kernel-architecture-cluster/05-a-1-scr---finding-the-acting-or-changed-system.md) supports System recognition, [FPF A.2.8.PER](../../../sections/05-part-a---kernel-architecture-cluster/17-a-2-8-per---granted-permission-exercise-and-non-prohibition.md) supports permission and [SYSE.13](../syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) supplies configuration identity and effectivity. [OPS.10](../../management-dpf-suite/ops/40-ops-10---qualify-operating-capacity-under-variability.md) supplies an operating capacity result when the maintenance question consumes it.

### MNT.1:End
