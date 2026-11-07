## EAM.12 - Integrate Specialist Results for an Asset Recommendation or Decision

> **Type:** Method
> **Status:** Stable

### EAM.12:1 - Problem frame

Use this pattern when an asset recommendation or decision must combine specialist answers. Finance reports affordability, maintenance recommends an intervention and operation offers an outage, but somebody must determine whether those answers concern the same option and whether the decision lies within their authority.

Begin with the result requested: advice, an asset choice or authorization. Give the recipient a supported answer at that scope. Delivering adequate advice can complete the request for advice before an authorizing decision exists.

### EAM.12:2 - Problem

Specialist results can disagree without using contradictory words. A cost estimate can concern another configuration, a condition forecast another duty and an outage another period. Combining their favorable conclusions does not establish that one asset option is feasible.

Financial advice, a spending allocation, an asset decision and equipment-work permission can also be mistaken for one approval.

### EAM.12:3 - Forces

Integration must preserve specialist limits while giving the decision maker a usable answer. Waiting for every conceivable result can postpone sufficient advice; omitting one decisive condition can make implementation unjustified. Authority may be distributed even when one committee makes the portfolio choice.

### EAM.12:4 - Solution

Name the decision and recipient. Establish whether the practitioner is asked to recommend an option, select it within delegated scope or authorize a specified action. Recover the actual basis and limits of the relevant authority when the requested conclusion relies on it.

For each specialist result used, match the asset, configuration, receiving service, horizon and proposed intervention. Extract the part that changes this decision: a condition account, qualified capacity, intervention scope, cost estimate, funding allocation or outage arrangement. The existence of a supplying framework description is not an obtained case result.

Resolve conflicting assumptions before combining conclusions. If engineering supports one duty and the operating proposal requires another, obtain an applicable result or keep that option conditional. If two estimates include the same expense, count it once. Preserve material uncertainty and missing results in the recommendation.

Distinguish advice from the conditions it uses. A finance practitioner can estimate cost and assess affordability against a funding allocation; the allocation sets the spending limit. A service mandate states the required delivery; engineering evidence supports what an arrangement can actually deliver. Identify the particular authority whose decision would change an allocation or mandate. Their amendment does not establish physical capability.

Present the supported option, reasons, conditions and displaced alternatives to the person who will decide. A concise recommendation can be sufficient. When uncertainty can change the decision, identify the missing result and the attainable inquiry worth undertaking; do not replace that question with a demand for every specialist's approval.

The authorized decision maker selects an asset option within the actual spending, service and other applicable conditions. State what was selected and the conditions of its use. Maintenance and operating authorities separately settle the permissions for protected work and resumption when that work is to occur.

Return the answer that exists. Report advice as advice, an authorized choice as an authorized choice and an unresolved decision as unresolved. Reopen the affected choice when a relied-on result, authority, configuration, duty or condition changes.

### EAM.12:5 - Archetypal Grounding

In the constructed CityWater case, the funding board allocates €8 million capital, €0.60 million initial operating expenditure and €3 million annually. The water-service authority sets the required delivery and has authority over its mandate. The infrastructure committee selects the asset programme within those conditions.

The EAM team recommends refurbishing A and B, modifying C and continuing D under its supported policy. The combination uses €7 million capital, €0.50 million initially for operation, €1.85 million annually and eight available work days. The finance practitioner checks those amounts against the allocations. The operating and engineering results qualify service and technical feasibility for the proposed work.

Sending that recommendation answers the committee's request for advice. If the committee then selects it within its authority, the team can report the authorized asset programme. That fact alone does not permit a maintenance crew to isolate D. Its work and resumption permissions must apply to the actual intervention. If finance's cost model instead concerns a replacement of D, the team reconciles that mismatch before relying on its favorable affordability conclusion.

### EAM.12:6 - Bias-Annotation

A powerful specialist or committee can make its preferred criterion appear universal. Preserve the source and scope of the conditions used, the interests affected and the decision rights of other participants. An estimate from a recognized expert still needs to concern this option.

### EAM.12:7 - Conformance Checklist

Do all relied-on results apply to the same option and use? Is the result advice, selection or authorization, with its actual recipient and scope? Are financial evidence, spending allocation, service obligation and technical support distinct? Can the recipient see the remaining condition that changes implementation?

### EAM.12:8 - Common Anti-Patterns and How to Avoid Them

Collecting favorable signatures without reconciling their assumptions leaves the option unsupported. Compare the relevant content of the results.

Using a budget approval as permission to operate or isolate equipment changes the scope of authority. Obtain the decision for the actual act when it is needed.

### EAM.12:9 - Consequences

The recipient gets one usable answer with its reasons and conditions. Some decisions remain conditional while adequate advice is delivered. The integration work can expose a precise missing result instead of commissioning a broad new study, and actual responsibility for implementation remains visible.

### EAM.12:10 - Architectural Rationale

The pattern integrates results at the asset decision because no single specialty owns all of its premises. It preserves the actual distribution of authority. Separating the requested result from later actions allows adequate advice to complete the request for it.

### EAM.12:11 - SoTA-Echoing

The common professional source account connects asset value decisions to multidisciplinary contributions. This pattern favors content reconciliation over a generic approval checklist.

### EAM.12:12 - Relations

[EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md)–[EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) provide reconciled alternatives, combinations and timing. [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) and [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) supply their maintenance results; [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) supplies the relevant service comparison; [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md) supports configuration applicability. [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) supports useful advice and proportionate evidence demands.

### EAM.12:End
