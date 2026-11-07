# Engineering Asset Management Principles Framework

**DocID:** `EAM` within **FPF Library**.

> A domain pattern language for making and revising value-oriented decisions about engineered assets over their lives, for one asset, an interacting asset System or a portfolio.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Release:** 27 September 2026
- **Status:** Eternal alpha: the current Methods can be used for their stated asset questions and conditions; the framework continues to develop as practice, sources and evidence change.
- **License:** Original framework content © 2026 Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Start with the [Readme](_index.md#engineering-asset-management-principles-framework-readme) for a working difficulty or the [Table of Contents](_index.md#table-of-contents) for a familiar question or PatternID. Open the pattern that can supply the needed answer and stop when that answer is sufficient. Use the [Citation](_index.md#citation) to identify this release.


# Table of Contents

Search for the asset decision or result you need. Dependencies identify useful result relations, not a mandatory sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Engineering Asset Management Principles Framework Readme](_index.md#engineering-asset-management-principles-framework-readme) | Follow connected asset decisions and their changed-condition returns. |
| [Citation](_index.md#citation) | Cite the framework or a particular pattern contribution. |
| [Engineering Asset Management Principles Framework Architectural Reference](_index.md#engineering-asset-management-principles-framework-architectural-reference) | Understand the asset-value problem, the related Methods and their limits. |
| [EAM.Reference:1](01-eam-reference-1---the-working-problem-and-practical-gain.md) | The working problem and practical gain |
| [EAM.Reference:2](02-eam-reference-2---forces-and-working-distinctions.md) | Forces and working distinctions |
| [EAM.Reference:3](03-eam-reference-3---architectural-rationale.md) | Architectural Rationale |
| [EAM.Reference:4](04-eam-reference-4---recognition-assurance-and-ordinary-stops.md) | Recognition, assurance and ordinary stops |
| [EAM.Reference:5](05-eam-reference-5---predictable-mistakes-consequences-and-bias.md) | Predictable mistakes, consequences and bias |
| [EAM.Reference:6](06-eam-reference-6---current-sources-and-what-they-support.md) | Current sources and what they support |
| [EAM.Reference:7](07-eam-reference-7---qualified-returns-from-related-practice.md) | Qualified returns from related practice |
| [EAM.Sources:1](29-eam-sources-1---professional-and-technical-sources.md) | Professional and technical sources |
| [EAM.Application - Cross-Pattern Applications](_index.md#cross-pattern-applications) | Follow one asset and its different choice in a constrained programme. |
| [Engineering Asset Management Principles Framework Sources and Edition Notes](_index.md#engineering-asset-management-principles-framework-sources-and-edition-notes) | Recover the source contributions and qualified specialist returns. |
| [EAM.Boundary - Framework Boundary and Refresh](08-eam-reference-8---framework-boundary-and-revision.md) | Find the scope, ordinary stops and reasons to reopen a result. |

**Part A - Outcomes and the Asset Information Basis**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [EAM.1 - Frame the Engineered Assets and Required Outcomes](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) | Stable | *Keywords:* single asset, asset System, portfolio, service, horizon. *Query:* "Which options should we compare for this asset or portfolio, for what service and period?" Agree the asset options, required service, comparison period and decision maker. | [EAM.2](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md), [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md); [FPF A.1.SCR](../../../sections/05-part-a---kernel-architecture-cluster/05-a-1-scr---finding-the-acting-or-changed-system.md) |
| 2 | [EAM.2 - Relate Assets to Strategy, Services, and Required Capability](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md) | Stable | *Keywords:* strategy, service, stakeholder, required capability. *Query:* "What required contribution must the assets support?" Relate proposed asset work to an actual service outcome and its authority. | [EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md), [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md), [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md); [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) |
| 3 | [EAM.3 - Establish the Asset Information and Configuration Basis](12-eam-3---establish-the-asset-information-and-configuration-ba.md) | Stable | *Keywords:* unit identity, configuration, effectivity, source applicability. *Query:* "Which information applies to this asset and comparison?" Resolve the answer-changing mismatch with a sufficient information basis. | [SYSE.13](../../engineering-dpf-suite/syse/38-syse-13---establish-configuration-identity-variants-and-effe.md); [EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md), [EAM.5](14-eam-5---assess-asset-condition-and-performance.md); [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) |

**Part B - Demand, Condition, Capacity, and Interdependence**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 4 | [EAM.4 - Assess Demand and Service Need for Asset Decisions](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) | Stable | *Keywords:* demand, components, drivers, coincident peak, scenario, forecast, service requirement. *Query:* "What service will be needed under the conditions that matter?" Construct compatible demand scenarios and distinguish their evidence from the mandated service. | [EAM.2](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md), [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md); [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) |
| 5 | [EAM.5 - Assess Asset Condition and Performance](14-eam-5---assess-asset-condition-and-performance.md) | Stable | *Keywords:* condition, performance, diagnosis, exposure, forecast. *Query:* "What do observed condition and delivered performance support?" Return a qualified account for the asset decision. | [MNT.4](../../engineering-dpf-suite/mnt/15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md), [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md); [OPS.18](../ops/52-ops-18---control-operating-quality-and-reliability.md); [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) |
| 6 | [EAM.6 - Assess Asset Capacity, Resilience, and Interdependence](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) | Stable | *Keywords:* capacity, bottleneck, resilience, shared dependency, usable reserve, recovery intervals. *Query:* "Can the assets support service during normal use and disturbance?" Derive lost contributions and follow available service and reserve through recovery. | [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md), [EAM.5](14-eam-5---assess-asset-condition-and-performance.md); [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md), [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md) |

**Part C - Alternatives, Conflicts, Combinations, and Timing**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 7 | [EAM.7 - Generate Ways to Supply an Asset-Dependent Service](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) | Stable | *Keywords:* acquire, modify, lease, service option, functional alternative. *Query:* "Which acquisition or change can provide the needed contribution?" Generate comparable qualified alternatives with their whole burden. | [EAM.2](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md), [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md), [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md); [SYSE.5](../../engineering-dpf-suite/syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) |
| 8 | [EAM.8 - Generate Maintenance, Renewal, and Retirement Alternatives](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) | Stable | *Keywords:* continue, maintain, renew, replace, retire, later intervention, horizon, residual value. *Query:* "Which continued-use or change option is worth considering?" Construct supported policies with dated consequences and a compatible ending premise. | [EAM.5](14-eam-5---assess-asset-condition-and-performance.md), [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md); [MNT.6](../../engineering-dpf-suite/mnt/17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md), [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md); [FIN.6](../fin/19-fin-6---value-capital-projects.md), [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md); [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) |
| 9 | [EAM.9 - Compare Asset Alternatives and Reconcile Decisions When They Conflict](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) | Stable | *Keywords:* asset alternatives, lifetime consequences, conflicting choices, funding, service mandate, simultaneous work. *Query:* "Which asset alternative is supported, and what unresolved conflict remains?" Compare eligible asset alternatives and identify any conflicting service, funding or work condition and the decision needed to resolve it. | [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md), [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md), [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md), [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md); [FPF C.32.MWA](../../../sections/09-part-c---kernel-extension-specifications/82-c-32-mwa---synthesize-an-architecture-account-of-methods-and.md) |
| 10 | [EAM.10 - Compare Engineered-Asset Portfolio Combinations](19-eam-10---compare-engineered-asset-portfolio-combinations.md) | Stable | *Keywords:* capital allocation, indivisible options, portfolio, combination, shared work, joint consequences. *Query:* "Which eligible asset combination should receive the allocation?" Construct whole consequences and compare programmes under the dated binding conditions. | [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md), [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md), [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md), [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md); [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md); [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) |
| 11 | [EAM.11 - Time Asset Interventions and Manage Dependencies](20-eam-11---time-asset-interventions-and-manage-dependencies.md) | Stable | *Keywords:* whole outage, dependencies, calendar, preparation, contingency. *Query:* "Can the selected programme be completed while preserving service?" Construct a supported calendar or expose the limiting prerequisite. | [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md), [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md), [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md); [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md), [MNT.15](../../engineering-dpf-suite/mnt/26-mnt-15---reconcile-simultaneous-maintenance-operation-and-su.md); [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) |

**Part D - Decisions, Outcomes, and Continuing Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 12 | [EAM.12 - Integrate Specialist Results for an Asset Recommendation or Decision](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) | Stable | *Keywords:* recommendation, specialist result, decision, authorization. *Query:* "What supported answer is requested and who makes the asset decision?" Integrate applicable results and distinguish advice from actual authorization. | [EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md), [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md), [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md), [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md); [FPF A.6.F](../../../sections/06-cluster-a-iv-a---signature-stack-boundary-discipline/22-a-6-f---function-and-functional-precision-restoration.md), [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md) |
| 13 | [EAM.13 - Track Realized Outcomes and Reconsider Asset Plans](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) | Stable | *Keywords:* realized outcome, variance, attribution, revision, changed premise. *Query:* "What has actually changed, and should the asset plan be retained or revised?" Compare obtained outcomes with the decision premises at the same scope. | [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md), [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md); [FPF A.10](../../../sections/07-cluster-a-v---constitutional-principles-of-the-kernel/07-a-10---evidence-graph-referring-claim-bound-evidence-and-pro.md), [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) |
| 14 | [EAM.14 - Decide Whether and How to Change the Asset-Management System](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) | Stable | *Keywords:* roles, information flow, responsibility, management system, arrangement. *Query:* "What in the organization of asset work prevents timely, supported decisions?" Compare feasible changes to responsibilities, information flow or support with keeping the current arrangement. | [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md), [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md), [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md); [OPS.11](../ops/43-ops-11---coordinate-interacting-operating-structures.md); [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md); [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) |
| 15 | [EAM.15 - Decide Whether and How to Change Engineering Asset-Management Methods](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) | Stable | *Keywords:* Method, reusable operations, comparison, variant, trial, refresh. *Query:* "Should this way of making asset decisions be retained or changed?" Compare ways of answering the same asset question, including the effort of applying and maintaining them. | [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md), [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md); [FPF A.3.1.MV](../../../sections/05-part-a---kernel-architecture-cluster/27-a-3-1-mv---construct-and-maintain-a-method-variant.md); [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) |
| 16 | [EAM.16 - Deliberately Continue and Change Engineering Asset-Management Culture](25-eam-16---deliberately-continue-and-change-engineering-asset.md) | Stable | *Keywords:* culture, transmission, use, recognition, selection, retention, branch. *Query:* "Which asset-management practices do people use, and should they continue or change?" Establish what the evidence supports and compare continuation, change, a qualified branch or stopping. | [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md), [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md); [FPF C.36.MC](../../../sections/09-part-c---kernel-extension-specifications/130-c-36-mc---qualify-and-develop-a-method-culture.md); [FPF C.36](../../../sections/09-part-c---kernel-extension-specifications/91-c-36---cultural-evolution-and-cultural-evolution-engineering.md) |

# Engineering Asset Management Principles Framework Readme

## Practical entries

The connections below follow an asset question through the methods whose results it needs. Start where the uncertainty lies: a supported option comparison can go straight to the decision, while a shared funding or outage constraint changes the question to a whole programme. Use the Table of Contents for a known PatternID or a question not illustrated here. When working with a colleague or assistant, describe the asset, the difficulty and the answer you need in ordinary work language.

The CityWater amounts and conditions are constructed teaching inputs. The two full [Cross-Pattern Applications](_index.md#cross-pattern-applications) retain the engineering qualifications, service requirements and calculations behind the shorter uses below.

### EAM-ASSET - Compare continued use and change for one asset

- **Situation:** CityWater can keep pump D functioning under a supported policy, but replacement may give better value.
- **Question:** Which policy should the infrastructure committee choose for the required service and horizon?
- **First useful result or blocker:** A supported recommendation, or the service, engineering or economic uncertainty preventing it.
- **Start with:** [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) for the policies; [EAM.1](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) if the comparison is unclear.
- **Stop or return:** Sufficient advice can finish the inquiry. A shared resource constraint sends the policies to the programme comparison.

The committee's value question differs from the maintenance question of which intervention supports continued functioning. If only a repair estimate is available, [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) first constructs the service policy: supported intervals, recurring duties, later work and ending. Its separate four-year example shows how an omitted year-three overhaul can reverse the comparison. A complete qualified policy can go directly to comparison.

[EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) uses the applicable condition and maintenance results to describe two complete policies: continued use with its initial intervention and recurring support, and replacement with integration and terminal value. [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) consumes those qualified alternatives and compares their consequences on the same basis.

In [APP-EAM-01](26-eam-application-1---app-eam-01---one-asset-and-a-supported-v.md), at the example's 3% real rate, five-year present cost is about €5.080 million for continuation and €3.568 million for replacement. With the required service equal and resources available for either, the €1.512 million difference supports recommending replacement. The break-even annual cost of continued use is about €0.670 million: an applicable range of €0.95–1.05 million leaves the recommendation unchanged, whereas a credible €0.60 million could reverse it. Further costing is useful when its attainable answer can change the decision enough to warrant the inquiry.

[EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) uses the comparison and its conditions to give the committee sufficient advice. The committee can then select a policy within its authority; maintenance and operating practitioners settle permissions for the work and return to service. If the request concerned only the maintenance response, the applicable MNT result could already finish it. If D competes with other assets for funding or an outage window, take its two policies into the combination below.

### EAM-COMBINATION - Choose asset work under shared constraints

- **Situation:** CityWater's individually preferred asset options exceed the shared capital allocation.
- **Question:** Which complete programme supplies the required service within the funding and work windows?
- **First useful result or blocker:** A programme recommendation with a supported calendar, or the conflict preventing it.
- **Start with:** [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) when alternatives and conditions are known; establish a missing service or option result where needed.
- **Stop or return:** Finish with sufficient programme advice. A changed funding, service or work condition reopens the affected comparison.

The demand and capability comparison in [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) and [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) identifies North's wet-season shortfall: 1,100 m³/h required against 1,000 available. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) supplies two qualified ways to add 200 m³/h at C, modification or leased service. Together with the supported A, B and D policies, these become the alternatives for [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) to reconcile and [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) to combine.

Under the €8 million capital limit and the other supplied limits, [APP-EAM-02](27-eam-application-2---app-eam-02---the-same-asset-in-a-constra.md) finds the least-cost eligible programme: refurbish A and B, modify C, continue D. It uses €7 million capital, €0.50 million initial operating expenditure and €1.85 million annually; its present cost is €14.592 million. Replacing D as well would require €10 million capital. Leasing C instead makes D replacement affordable, but raises total present cost to €15.350 million. The individual D result therefore remains true under its own resource assumption, while the programme comparison favors continuation.

[EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) consumes the selected interventions and their whole outage durations. A on days 1–2, B on 3–4, C on 5–7 and D on day 8 fits the twelve-day window and the single team, restoring each asset before the next outage. It avoids the A/C and B/D overlaps that would breach the dry-window service minimum. Use [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) to send a programme recommendation with a supported calendar to the committee.

If a demand driver or shared dependency changes, [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) and [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) reconstruct the affected service conditions before the same options are compared again. If work can share a real preparation or mobilization, [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) reconciles the whole consequences with the separate policies and [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) qualifies that arrangement. Its separate P+Q case changes a 4.0 estimate to 3.8 by paying for one mobilization; incompatible access windows remove that saving. These constructions are used when their premise is missing or changes.

A changed limit returns to the affected choice. If the funding board raises capital to €10 million, retaining the other premises, replacing D joins the preferred programme. If only seven days remain, the eight-day arrangement fails: the declared alternatives instead permit A refurbishment, B replacement, C leased service and D continuation. If D's engineering qualification fails, remove continuation before comparing programmes; cost savings cannot restore it. Each changed case is worked through in the full application.

### EAM-CHANGE - Reconsider a decision after a changed condition

- **Situation:** Observed service, condition or expenditure differs from a relied-on plan premise.
- **Question:** Does the difference change the plan, its explanation or the next decision?
- **First useful result or blocker:** A retained or revised plan, or the applicable observation needed to decide.
- **Start with:** [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) for the outcome comparison; use [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) first if asset or configuration correspondence is unsettled.
- **Stop or return:** Retain a sufficient plan; reopen the choice changed by the observation. Further inquiry needs an attainable answer worth its burden.

Suppose annual expenditure for the selected CityWater policy is €1.95 million against €1.85 million planned. [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) compares the same scope and interval. Applicable bills explain a €0.12 million tariff effect and a €0.02 million reduction elsewhere: 1.85 + 0.12 − 0.02 = 1.95.

That result updates the price premise for [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) or [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) where it can change the next choice. It does not establish an equipment defect. If the comparison instead joins different units or configurations, [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) first resolves that mismatch. If C's work is complete but usable service falls below the wet-season requirement, return the service deficiency to [EAM.5](14-eam-5---assess-asset-condition-and-performance.md) and [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) and the applicable operating or engineering response. The cause can remain under investigation while a supported response is taken.

### EAM-PRACTICE - Improve how asset decisions are made

- **Situation:** Appraisals repeatedly fail or consume avoidable effort despite usable individual asset plans.
- **Question:** What should change in the way the decisions are produced?
- **First useful result or blocker:** Supported advice about the arrangement, method or continued practice, or a result needed to decide.
- **Start with:** [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) for the working arrangement, [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) for the selection method, or [EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) for use and continuation among practitioners.
- **Stop or return:** Answer the identified recurring difficulty; change another part of the practice when its contribution matters to that answer.

In [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md)'s appraisal office, mismatched station identifiers cause six hours of rework a week. A maintained correspondence and responsibility for returning mismatches would take twelve hours to establish and half an hour a week to maintain. Over ten comparable weeks, that is seventeen hours against sixty hours of continued rework, if the repair removes the mismatch. The comparison supports proposing the bounded repair; examine later appraisals to see whether it helps. Use [EAM.3](12-eam-3---establish-the-asset-information-and-configuration-ba.md) to establish the applicable unit correspondence. If assigned work exceeds available time under adequate existing responsibilities, [EAM.14](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) uses OPS to compare operating adjustments. If organizational responsibilities or decision rights must change, or agreed responsibilities must become workable, it uses [OCE.9](../oce/31-oce-9---realize-a-bounded-organization-capability-increment.md) to exercise an appraisal from request to usable result and an unmatched-unit return.

If the information is adequate but the selection rule fails, [EAM.15](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) addresses the method instead. Funding D, C and A in condition-priority order exhausts CityWater's capital before B, whereas combination comparison supplies the required programme. That calculation supports changing the comparison for this case. A proposed reusable method can be tried on other relevant cases when the consequences for adoption justify the effort.

[EAM.16](25-eam-16---deliberately-continue-and-change-engineering-asset.md) takes that proposed instruction into a question about its transmission, use or continuation among practitioners. Distribution and teaching establish different facts from later appraisals using the method. Its existing branch example retains programme comparison for central planners with shared constraints and single-asset comparison for depot cases whose independence is established. A shared constraint returns a depot case to the programme comparison.

## How to read and apply the framework

Begin with a pattern's Problem frame and Solution. Its worked case shows a minimally useful result and a consequential branch. Read its assurance questions, alternatives and source comparison to judge a more consequential use.

This edition proposes source-grounded Methods and constructed applications. It does not report field effectiveness of the integrated repertoire. An equipment-specific assessment, financial input, operating condition or actual authorization must come from the practice or authority responsible for it.

## Citation

Cite: Anatoly Levenchuk, *Engineering Asset Management Principles Framework*, version shown above. For a particular contribution, add its PatternID and title. The framework was developed with AI-assisted authoring and review. Original text is reusable under the license above; cited third-party works are not relicensed.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Engineering Asset Management Principles Framework Architectural Reference

- [EAM.Reference:1 - The working problem and practical gain](01-eam-reference-1---the-working-problem-and-practical-gain.md) (12 lines)
- [EAM.Reference:2 - Forces and working distinctions](02-eam-reference-2---forces-and-working-distinctions.md) (10 lines)
- [EAM.Reference:3 - Architectural Rationale](03-eam-reference-3---architectural-rationale.md) (18 lines)
- [EAM.Reference:4 - Recognition, assurance and ordinary stops](04-eam-reference-4---recognition-assurance-and-ordinary-stops.md) (10 lines)
- [EAM.Reference:5 - Predictable mistakes, consequences and bias](05-eam-reference-5---predictable-mistakes-consequences-and-bias.md) (10 lines)
- [EAM.Reference:6 - Current sources and what they support](06-eam-reference-6---current-sources-and-what-they-support.md) (8 lines)
- [EAM.Reference:7 - Qualified returns from related practice](07-eam-reference-7---qualified-returns-from-related-practice.md) (18 lines)
- [EAM.Reference:8 - Framework boundary and revision](08-eam-reference-8---framework-boundary-and-revision.md) (14 lines)
- [EAM.Reference:End](09-eam-reference-end.md) (3 lines)

### Part A - Outcomes and the Asset Information Basis

- [EAM.1 - Frame the Engineered Assets and Required Outcomes](10-eam-1---frame-the-engineered-assets-and-required-outcomes.md) (79 lines)
- [EAM.2 - Relate Assets to Strategy, Services, and Required Capability](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md) (75 lines)
- [EAM.3 - Establish the Asset Information and Configuration Basis](12-eam-3---establish-the-asset-information-and-configuration-ba.md) (99 lines)

### Part B - Demand, Condition, Capacity, and Interdependence

- [EAM.4 - Assess Demand and Service Need for Asset Decisions](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) (118 lines)
- [EAM.5 - Assess Asset Condition and Performance](14-eam-5---assess-asset-condition-and-performance.md) (75 lines)
- [EAM.6 - Assess Asset Capacity, Resilience, and Interdependence](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) (127 lines)

### Part C - Alternatives, Conflicts, Combinations, and Timing

- [EAM.7 - Generate Ways to Supply an Asset-Dependent Service](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) (75 lines)
- [EAM.8 - Generate Maintenance, Renewal, and Retirement Alternatives](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) (149 lines)
- [EAM.9 - Compare Asset Alternatives and Reconcile Decisions When They Conflict](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) (85 lines)
- [EAM.10 - Compare Engineered-Asset Portfolio Combinations](19-eam-10---compare-engineered-asset-portfolio-combinations.md) (144 lines)
- [EAM.11 - Time Asset Interventions and Manage Dependencies](20-eam-11---time-asset-interventions-and-manage-dependencies.md) (75 lines)

### Part D - Decisions, Outcomes, and Continuing Practice

- [EAM.12 - Integrate Specialist Results for an Asset Recommendation or Decision](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) (77 lines)
- [EAM.13 - Track Realized Outcomes and Reconsider Asset Plans](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) (75 lines)
- [EAM.14 - Decide Whether and How to Change the Asset-Management System](23-eam-14---decide-whether-and-how-to-change-the-asset-manageme.md) (87 lines)
- [EAM.15 - Decide Whether and How to Change Engineering Asset-Management Methods](24-eam-15---decide-whether-and-how-to-change-engineering-asset.md) (75 lines)
- [EAM.16 - Deliberately Continue and Change Engineering Asset-Management Culture](25-eam-16---deliberately-continue-and-change-engineering-asset.md) (83 lines)

### Cross-Pattern Applications

- [EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison](26-eam-application-1---app-eam-01---one-asset-and-a-supported-v.md) (57 lines)
- [EAM.Application:2 - APP-EAM-02 - The same asset in a constrained programme](27-eam-application-2---app-eam-02---the-same-asset-in-a-constra.md) (69 lines)
- [EAM.Application:End](28-eam-application-end.md) (3 lines)

### Engineering Asset Management Principles Framework Sources and Edition Notes

- [EAM.Sources:1 - Professional and technical sources](29-eam-sources-1---professional-and-technical-sources.md) (18 lines)
- [EAM.Sources:End](30-eam-sources-end.md) (1 lines)
