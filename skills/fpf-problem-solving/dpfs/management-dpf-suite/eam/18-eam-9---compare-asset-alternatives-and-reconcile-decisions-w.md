## EAM.9 - Compare Asset Alternatives and Reconcile Decisions When They Conflict

> **Type:** Method
> **Status:** Stable

### EAM.9:1 - Problem frame

Use this pattern when a proposed asset choice must satisfy different technical, service, financial or operating conditions, or when individually reasonable decisions cannot hold together. It also provides the comparison for one asset whose feasible alternatives have different lifetime consequences.

Begin with the conflict or difference that can change the choice. Return a reconciled comparison, a supported recommendation or the precise unresolved conflict. A transparent cost comparison can be sufficient when service and other eligibility conditions are equal.

### EAM.9:2 - Problem

A local saving can move downtime, cost or risk to another participant. A favorable financial score can conceal an unavailable service or unsupported asset policy. Conversely, building a universal weighted score can add assumptions that nobody is authorized or able to justify.

### EAM.9:3 - Forces

Decision makers need a usable comparison that preserves differences in interests and measurement scales. Binding conditions restrict the feasible set, while preferences compare its members. More evidence or negotiation can resolve a conflict, but it must be attainable and worth its full burden.

### EAM.9:4 - Solution

Name the alternatives, receiving service and horizon. Recover the conditions that determine eligibility and their sources. A funding allocation sets a spending limit; a service mandate sets required delivery; engineering evidence supports the proposed functioning. State their different consequences for the choice.

Identify the actual couplings behind a conflict. The same assets can participate in an operating network, a crew schedule, a maintenance programme and a funding decision. Relate their common subjects and dependencies without treating those structures as identical. Use [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md), [MNT.15](../../engineering-dpf-suite/mnt/26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) or [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) when their specific coordination question is needed.

Exclude unsupported alternatives from the eligible comparison or retain them explicitly as conditional proposals. An invalid qualification for D continuation cannot be offset by a low cost. If no option remains, report the unmet service or resource condition and the decision or specialist result that could change it.

Compare eligible alternatives on compatible consequences. For equal required service and admitted nonfinancial conditions, present cost can be a useful criterion. With initial capital K, initial operating cash O, annual costs Ct, terminal value S, rate r and horizon n, use K + O + Σ Ct/(1+r)^t − S/(1+r)^n. Use a consistent price/rate basis and account for costs and residual value once.

When important consequences differ, preserve those differences. An alternative is dominated only when another is at least as good on every relevant criterion and better on at least one under the same conditions. Retain a non-dominated set when no justified priority resolves the trade-off; identify who can make that choice. Do not invent weights to force a ranking.

Test assumptions that can reverse eligibility or preference. A range, scenario or break-even can be enough. Select additional inquiry by the answer it could change and the work, delay and disruption it requires.

Return the recommendation with its reasons, conditions and remaining conflict. Use [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) for a genuine combination decision and [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) for the requested asset decision or authorization. Stop when sufficient advice has been delivered.

### EAM.9:5 - Archetypal Grounding

For D alone, the constructed five-year present costs are €5.079707 million for the supported continued-use policy and €3.567767 million for replacement. With equal required service, applicable technical support and resources for either, the practitioner recommends replacement on cost: the difference is €1.511940 million.

Keeping replacement inputs fixed, continued use becomes equally costly at about €0.669861 million annual cost. A justified range of 0.95–1.05 does not reverse the answer; a credible 0.60 estimate would. The calculation identifies a potentially useful inquiry boundary without giving that lower estimate a probability or treating it as fact.

At the portfolio scope, the same D replacement needs capital that C modification and other work also need. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) compares the whole combinations. The independent D comparison is not wrong; its resource assumption differs from the shared decision.

In a separate constructed choice, three policies are technically supported and affordable. The service mandate permits up to six hours of planned interruption for the same users in the same work window. All three meet that condition; their only material preference differences on the supplied five-year basis are:

| Policy | Present cost, € million | Planned service interruption, hours |
| --- | ---: | ---: |
| P | 3.0 | 4 |
| Q | 3.4 | 1 |
| R | 3.6 | 5 |

R is dominated: P costs less and interrupts service for less time, and Q also improves both consequences. P and Q remain: P is cheaper, while Q avoids three more hours of interruption for an additional €0.4 million in present cost. The infrastructure committee is authorized to choose within the mandate, but no priority between these two consequences has been supplied. The practitioner returns P and Q with that specific trade-off for the committee's decision. Inventing monetary weights for the interruption would conceal the unresolved preference. If a changed mandate permits only two hours, P becomes ineligible and Q is the sole eligible policy on these premises.

### EAM.9:6 - Bias-Annotation

A single monetary criterion can hide losses to groups outside the accounting perspective. Preserve nonfinancial requirements and material unpriced consequences. A familiar model can also hide false precision about future costs or terminal values.

### EAM.9:7 - Conformance Checklist

Are eligibility conditions separated from preferences? Do the quantities share a justified comparison basis? Are transferred burdens and real conflicts visible? Does the recommendation state the assumptions that can reverse it and the recipient's remaining decision?

### EAM.9:8 - Common Anti-Patterns and How to Avoid Them

A weighted score that compensates for failed required service admits an ineligible option. Apply the service condition before comparing preferences.

Treating different views as one aligned hierarchy hides shared dependencies. Recover the actual assets, work, resources and decisions that connect them.

### EAM.9:9 - Consequences

The decision maker receives an explainable preference or a bounded unresolved trade-off. Some options are excluded and some inquiries stop. The comparison can remain conditional.

### EAM.9:10 - Architectural Rationale

Eligibility, preference and actual authority answer different questions. Keeping them separate permits simple economic comparison where justified and richer multi-criterion judgement where needed. The asset-specific consequence account is what connects general comparison guidance to this domain.

### EAM.9:11 - SoTA-Echoing

The common NIST source supports compatible lifecycle-cost comparisons, while the professional landscape recognizes wider value and risk. This pattern uses minimum present cost only under its stated equality and eligibility conditions. Payback, condition rank or an unexplained weighted sum cannot replace that decision basis.

### EAM.9:12 - Relations

[EAM.5](14-eam-5---assess-asset-condition-and-performance.md)–[EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) supply assessments and alternatives. [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) compares combinations, [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) timing and [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) the decision. [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) and [MNT.15](../../engineering-dpf-suite/mnt/26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md) supply their bounded coordination results; [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md), [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) and [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) support comparison, useful inquiry and synthesis across relevant structures.

### EAM.9:End
