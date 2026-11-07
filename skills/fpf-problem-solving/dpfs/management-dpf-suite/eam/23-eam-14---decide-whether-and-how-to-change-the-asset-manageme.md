## EAM.14 - Decide Whether and How to Change the Asset-Management System

> **Type:** Method
> **Status:** Stable

### EAM.14:1 - Problem frame

Use this pattern when the arrangement performing asset management repeatedly prevents useful decisions: information is joined incorrectly, responsibility is unclear, a needed capability is absent or a decision cannot reach the person authorized to make it.

Begin with the actual recurring failure and the people, tools and relations involved. Return a supported decision to retain or change that arrangement. A small correction can suffice; a new enterprise system is one alternative, not the default result.

### EAM.14:2 - Problem

An organization can possess policies, software and a complete asset register while its practitioners still cannot make a timely supported choice. A management-system document describes requirements or an arrangement; it does not establish that people can perform the work, obtain the information or exercise the required authority.

### EAM.14:3 - Forces

A shared arrangement can reduce duplication while creating a bottleneck or common failure. Standardization helps reuse but can obscure local service and asset differences. Changing tools or responsibilities consumes migration, learning and continuing support work whose burden can exceed the improvement.

### EAM.14:4 - Solution

Name the asset-management result that is failing and a representative occurrence or source account. Identify the receiving practitioner and decision, the observed difficulty and its consequence. Keep an untested diagnosis of the cause separate from the observation.

Recover the actual arrangement needed for that result: participating people and Systems, responsibilities, information, tools, capabilities and decision interfaces. Choose only the relations that explain the failure. The asset System being managed and the organization performing asset management are different subjects.

Compare plausible alternatives for the arrangement. These might include retaining the current arrangement, repairing one information correspondence, changing a responsibility, providing a capability, altering a decision interface or replacing a tool. Explain what each alternative would mean for the needed result and what it moves elsewhere.

Include the whole burden: design, access, migration, training, disruption, operation and maintenance of the changed arrangement. Preserve applicable authority and obligations. Obtain any decision needed to implement the proposed change or trial from the person authorized to make it.

Recommend retention or a change whose expected result meets the stated need and whose supported gain warrants its whole burden. Compare adequate alternatives under the relevant priorities, retaining unresolved trade-offs for the person who can decide them. If the cause is uncertain and can alter the choice, obtain the worthwhile discriminating evidence. A conditional recommendation or authorized bounded attempt can be the useful result. If an obvious correctable mismatch already explains the difficulty, give the bounded repair decision without demanding a whole-system study.

Choose the realizing practice by what must change. An information correspondence can be corrected through EAM.3. Use [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) to compare already assigned work with available resources and adjust case allocation, release or coordination within existing responsibilities and authority. This includes giving another case to an already qualified and authorized performer. OPS.11.1 helps identify the activities, shared resources and completion conditions when that operating model is unclear.

Use [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) for a change to organizational responsibilities or decision rights, or to establish agreed responsibilities that participants cannot yet exercise. Supply the selected arrangement or authorized bounded attempt, receiving result, participating people, representative work, service conditions and recovery needs. The change practitioner exercises one complete request-to-result path and its exception return, obtains missing access, support or authority from their responsible providers, and observes the relevant later use.

Bring back the capability that the evidence supports, with its participants, work conditions, retained support and limits, or the missing condition and next repair. Use that result to judge whether the changed arrangement can supply the asset decision on time. When correcting the mismatch under [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) answers the recipient's information question, the practitioner can provide that answer and finish the inquiry. Selection, implementation and observed effect remain different facts; preserve the fallback needed by current decisions.

Return the retained or changed arrangement and the condition that would reopen it. Use [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) for a reusable Method change and [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) for a cultural-process question.

### EAM.14:5 - Archetypal Grounding

In a constructed appraisal office, four cases a week each lose 1.5 practitioner-hours because cost and condition records use inconsistent station identifiers. The observed burden is six hours a week. A proposed maintained correspondence and one responsibility for returning mismatches requires twelve hours to establish, including training, then half an hour a week to maintain.

Over ten comparable weeks, continued rework would consume sixty hours if the observed rate persists. The bounded repair would consume 12 + 10 × 0.5 = seventeen hours if it removes that mismatch. A proposed new application requires eighty hours to establish and two hours a week to support: one hundred hours on the same horizon. These are explicit teaching assumptions, and consequential error risk must be compared separately from time.

The practitioner can recommend the bounded repair, then inspect whether matching actually improves. The projected forty-three-hour difference is not a claim of realized savings. If records reveal that the mismatch was only a symptom of an unresolved configuration, [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md)'s information question remains necessary.

In a larger constructed variant, a new arrangement changes the roles' ongoing responsibilities: the cost analyst is to request a joint appraisal, the condition engineer is to resolve the unit correspondence with the source, and the committee secretary is to return an incomplete contribution to the responsible participant. All three use the maintained unit correspondence when preparing and receiving the appraisal. These contribution and return responsibilities must become workable. Once the authorized arrangement or trial decision is supplied, [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) can exercise an appraisal from its request through comparison to a usable committee packet, including an unknown-unit case. If the condition engineer lacks effective access, the useful first result is that missing access and the responsible provider's required action. After it is supplied, representative later appraisals can establish what the new arrangement actually supports. The result states the observed conditions and remaining limits; purchasing the shared tool does not establish that capability.

A different office may already have adequate responsibilities but have twelve assigned half-hour condition checks competing for four available engineer-hours. Under those durations, the available time accommodates eight checks. The practitioner uses [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) to compare which checks to release now and when to do the remaining four, carrying the effects on the asset decisions. OPS.11.1 relates the checking step to the analyst's and secretary's work before anyone promises completed appraisals. When these choices lie within existing responsibilities and authority, this is operating coordination; a changed allocation does not itself require redesigning the contribution relationships.

### EAM.14:6 - Bias-Annotation

Software providers and organizational sponsors can make their solution define the problem. Include work shifted to frontline practitioners and service users. A structurally neat responsibility chart is not evidence of usable capability or information access.

### EAM.14:7 - Conformance Checklist

Is the failed asset-management result recognizable? Does the selected change act on the actual arrangement and have a plausible mechanism of improvement? Are implementation authority, whole burden and the intended outcome comparison explicit?

### EAM.14:8 - Common Anti-Patterns and How to Avoid Them

Purchasing an application and declaring the management system realized skips the work and relationships needed to use it. Establish the actual capability and interfaces.

Changing the organization to fix one record mismatch can impose needless burden. Compare the bounded correction with the larger alternatives.

### EAM.14:9 - Consequences

Practitioners can obtain a more usable arrangement or retain an adequate one. The change can have migration and continuing costs, and its effects need observation at the intended result.

### EAM.14:10 - Architectural Rationale

The pattern's subject is the arrangement that performs asset management. Keeping it separate from the managed assets, reusable Methods and cultural processes makes the proposed intervention and its evidence testable. The realizing practice follows the needed change: OPS supports operating coordination within existing responsibilities, while [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) supports changing organizational responsibilities or decision rights and making agreed responsibilities workable. [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) uses the resulting capability and its limits to reconsider the asset-management arrangement.

### EAM.14:11 - SoTA-Echoing

For a recurring failure to produce a usable asset decision, identify the failed contribution, compare a bounded correction with retention and larger arrangement changes, and include their continuing burden. For operational adjustment within existing responsibilities, use the coordination in [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) and the OPS.11.1 operating model. When the difficulty requires organizational realization, adapt the complete contribution and exception test in [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) (§§4.1–4.6) to the asset-appraisal work.

An organization-wide maturity assessment is a serious alternative when the weakness is not yet localized. GFMAM's Landscape, third edition (2024), pp.9–10, describes that broader assessment. It can reveal weaknesses outside the observed appraisal flow. For the known identifier mismatch, however, broader coverage does not resolve the mismatch or demonstrate that the repaired flow works. The chosen trade-off is a narrower conclusion with a directly testable correction: the Solution and worked case address this failed contribution without claiming that the entire management system is adequate.

[OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) supplies the realization operations and their result limits; the constructed office comparison supports the bounded burden calculation, not observed improvement. The GFMAM assessment is retained for the wider question. Reopen this choice if failures extend beyond the selected flow, the correction leaves the problem unexplained, or a wider assessment reveals a common cause that changes the proposed arrangement.

### EAM.14:12 - Relations

[EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) can reveal the recurring problem and [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) the information mismatch. [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) addresses reusable ways of doing the work; [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) addresses transmission and continued practice. [FPF A.22](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/49-a-22---structure-and-structural-views.md) supports selected structures and [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) the needed synthesis across unlike practice structures. [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) and OPS.11.1 support workload and flow adjustments within existing responsibilities. [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) supplies a qualified realization or missing-condition result when organizational responsibilities or decision rights must change, or agreed responsibilities must become workable.

### EAM.14:End
