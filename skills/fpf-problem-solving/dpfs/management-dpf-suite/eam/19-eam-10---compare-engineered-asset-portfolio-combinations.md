## EAM.10 - Compare Engineered-Asset Portfolio Combinations

> **Type:** Method
> **Status:** Stable

### EAM.10:1 - Problem frame

Use this pattern when asset choices compete for shared funding, service, people, outages or other resources. Several individually attractive projects cannot all be performed, choosing one changes the feasible alternatives for another, or performing them together changes their consequences.

Begin with the actual combination question and its constraints. Return the preferred feasible combination, a justified non-dominated set or the precise condition that prevents one. An isolated single-asset comparison can remain in EAM.9.

### EAM.10:2 - Problem

Ranking assets by condition or ranking projects by a benefit ratio can miss a better feasible combination. Options can be indivisible, mutually exclusive or dependent. A low-capital alternative at one station can release funding for a valuable option elsewhere, while separate project approval hides that interaction.

Adding standalone costs can also count shared preparation twice or omit a cost caused by the combination. Calling the difference a portfolio saving without identifying its cause leaves the decision dependent on an unsupported discount.

### EAM.10:3 - Forces

Shared allocation must preserve required service and actual technical eligibility while comparing value. A more complete model can reveal a better combination but costs effort and relies on input quality. Deferral can preserve flexibility or create unacceptable risk, depending on its supported policy.

### EAM.10:4 - Solution



#### EAM.10:4.1 - Define complete choices and different kinds of coupling


State the portfolio scope, requested result and horizon. Recover the alternatives and their eligibility from [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md)–EAM.9. Identify which choices are mutually exclusive, mandatory, optional or dependent, and why. Include continued use or no new work when it is a qualified alternative. An omitted asset can still matter through a shared service or resource.

Distinguish three questions about a proposed combination. A prerequisite or exclusion determines which selections can coexist: a new unit may need an enabling connection, while two replacements for the same role may be mutually exclusive. A shared resource limit constrains the work or use at a particular time: two eligible jobs may need the same crew or exceed an outage allowance. A joint consequence changes what happens when the choices are taken together: common mobilization may reduce cost, while simultaneous demand can require additional provision. One arrangement can create all three, but each needs its own evidence.

For each material relation, identify the affected alternatives, its operating or engineering cause, the time and conditions under which it holds, and the resulting constraint or consequence. [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) supplies service and dependency conditions. A promised saving cannot make a combination technically eligible.



#### EAM.10:4.2 - Construct the whole consequence account


Start from compatible policies on the same service boundary, perspective and horizon. If a policy omits later support or its ending, return to EAM.8. Then describe what work and service the combination actually entails. Identify shared preparation, enabling work, recurring operation, temporary service and ending consequences. Obtain amounts and dates for those actual operations.

Reconcile this whole account with the separate accounts. For costs on the same basis, `joint adjustment = whole-combination cost − sum of standalone costs`. A negative amount is a saving; a positive amount is an additional cost. Explain what causes it and when it occurs. Where effects differ by date, construct the dated differences first and obtain their financial value through [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) on the applicable basis. [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) develops this interaction comparison and dated funding constraints; its return must identify the combination, common baseline, perspective, amounts, dates and significant assumptions.

Count each shared consequence once. If two estimates each contain the same mobilization, the combination that uses one mobilization retains one payment. If three jobs share it, reconstruct their common account; summing all three pairwise discounts could remove more mobilizations than were included. If sharing requires extra supervision or temporary service, include that cost too. An allocation of common cost among departments does not by itself create a saving in the whole payment.

Keep unpriced consequences visible. Shared disruption can change a service or environmental result even when the expenditure sum is unchanged. Use [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md)'s actual criteria to compare those consequences; a cash adjustment cannot silently settle them. When the combination changes a demand or recovery premise, return that premise to [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) or [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) before relying on its qualification.



#### EAM.10:4.3 - Test constraints and compare the feasible combinations


Write the constraints at the whole-combination scope. Separate initial capital, initial operating expenditure and recurring operating envelopes where they are different decisions. Include later commitments when they bind: the year-three overhaul in an [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) policy needs its funding, crew and service window at that time. A low initial outlay does not establish that later provision. Do not count a resource twice or assume unused funding must be spent.

Enumerate a small finite set of indivisible choices. For the CityWater shortlist, choose exactly one of two options for each of four stations and compare all sixteen. For a different question, the feasible no-work, single and combined choices depend on what service is mandatory. Remove combinations excluded by a supported prerequisite, technical condition or resource limit, retaining the reason. Obtain a feasible service-preserving calendar through [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) where timing can defeat an otherwise eligible selection.

For a larger problem, select an optimization or scenario method whose objective, choices, constraints and interactions represent the actual question. Specify what is selectable, which selections imply or exclude others, dated resource use and the joint effects. Model contingent actions with the information available when each action is chosen; the combination cannot assume different early choices for future outcomes that are not yet known. A mathematical optimum applies to the represented set and basis.

Compare eligible combinations using the actual value criteria. When required service and other material consequences are equal, minimize total present cost. Otherwise preserve justified trade-offs or a non-dominated set. A cheaper programme that requires more scarce resources does not automatically dominate a dearer one.



#### EAM.10:4.4 - Explain the choice and the condition that could change it


Show the preferred combination and the consequential alternatives it displaces. Test a changed funding limit, engineering qualification, demand driver, shared-work condition or resource date when it could alter the answer. Use coherent conditions across the combination; a common disruption cannot be favorable for one component and absent for another without grounds.

Return the recommendation, the whole consequence account, feasibility conditions and the decision-changing uncertainty to [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) and EAM.12. [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) later returns observations to the premise they affect. If a missing shared-work fact can change the choice, obtain it only when its attainable answer warrants the inquiry's full burden. A project that remains locally useful can be deferred for a qualified portfolio reason without being relabelled technically poor.

### EAM.10:5 - Archetypal Grounding



#### EAM.10:5.1 - A shared operation changes the comparison


Consider a separate constructed service requirement. Two interventions P and Q together and a different complete solution Z are both qualified to supply it over the same horizon. P or Q alone is insufficient. Their subsequent operating, ending and other material consequences are equal; all different costs are payable now in €million, and funding is sufficient for either whole solution. Thus their initial cost difference decides this bounded comparison.

P costs 2.0, including 0.2 mobilization, and Q also costs 2.0 including 0.2. Z costs 3.9. The operating practitioner establishes that P and Q can be performed sequentially during one qualified visit, using one 0.2 mobilization. Required service remains supported during the work; the shared visit incurs no additional consequence outside the supplied account.

| Whole choice | Separate estimate | Joint adjustment | Comparable cost |
| --- | ---: | ---: | ---: |
| P and Q with one mobilization | 4.0 | −0.2 | 3.8 |
| Complete solution Z | 3.9 | 0 | 3.9 |

The whole P+Q account is `1.8 + 1.8 + 0.2 = 3.8`. Adding the separate estimates would prefer Z at 3.9; the supported joint account prefers P+Q by 0.1. That result concerns one actual payment saved through a feasible work arrangement.

Suppose incompatible access windows require two visits and two mobilizations. P+Q returns to 4.0 and Z becomes cheaper at 3.9. If instead the proposed shared visit fails the service condition, remove that arrangement as ineligible and compare any qualified two-visit arrangement with Z. Reducing its price cannot repair the lost service. [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) establishes which visit arrangement is feasible; [EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md) uses its consequences.

The example does not infer a common saving for CityWater's separate station jobs. A proposed CityWater sharing arrangement would need its own work, service and financial account before altering the following result.



#### EAM.10:5.2 - The sixteen supplied CityWater combinations


The common CityWater application supplies four two-option choices. Initial capital must not exceed €8 million, initial operating expenditure €0.60 million, annual operation €3 million and the available team/outage time twelve days. All amounts and eligibility results are constructed.

FFMK—refurbish A and B, modify C, continue D—uses €7 million capital, €0.50 million initially for operation, €1.85 million annually and eight days. Its present cost is €14.592284 million, the lowest among the declared eligible combinations. EAM.Application:2 shows all sixteen combinations.

Adding D replacement while retaining the other choices gives FFMR: €10 million capital and lower present cost of €13.080344 million. It is infeasible at the €8 million allocation. Switching C to leased service permits D replacement within capital, but FFLR costs €15.350138 million overall.

If the funding board raises capital to €10 million, FFMR becomes preferred. If D continuation instead loses its engineering qualification, FFLR becomes preferred at the original limits.

### EAM.10:6 - Bias-Annotation

A portfolio objective can conceal which users bear losses and which costs are left outside the model. Document material omissions and the authority for trade-offs. Model size and numerical precision do not establish that the options or consequences are complete.

### EAM.10:7 - Conformance Checklist

Are all required choices, prerequisites and exclusions represented? Does the selected combination meet the dated whole-set constraints and admit a feasible schedule? Can its joint effects be traced to actual work or use and counted once? Can the recipient reproduce the preference and identify a condition that would reverse it?

### EAM.10:8 - Common Anti-Patterns and How to Avoid Them

Funding the highest-ranked items until money runs out can miss a feasible combination of different options. Evaluate the relevant combinations.

Accepting each project separately does not establish the shared condition. Construct the actual whole demands and consequences, then test their dependencies at portfolio scope.

A generic synergy percentage hides which work or cash changes. Reconcile the whole account with the separate accounts and retain the conditions that make the difference possible.

### EAM.10:9 - Consequences

The portfolio can deliver more useful service or value within actual constraints. Some individually preferred projects are displaced. The result's quality still depends on the eligible option set, consequence model and supported feasibility; it does not authorize work.

### EAM.10:10 - Architectural Rationale

The combination is the subject because shared constraints and joint consequences can change which option should be selected at each asset. This differs from both single-asset value comparison and maintenance scheduling. Enumeration is selected for small cases because the assumptions and omitted alternatives remain inspectable.

### EAM.10:11 - SoTA-Echoing

NIST HB135e2025, chapters 4, 7 and 8, supplies common-period costing, comparison of alternatives and programmes, and sensitivity reasoning. Those operations support the explicit consequence comparison; its federal rates and programme rules are outside this use.

[FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) develops whole incremental cash under interactions, dated constraints and service continuations. Its B+C example shows that a negative joint cash effect can reverse the allocation even when the combined initial funding remains feasible. Use that financial construction together with the actual engineering and operating conditions; financial interaction and physical feasibility answer different questions.

Enumeration fits a small indivisible shortlist because every permissible combination and exclusion can be inspected. Independent ranking is defensible only when the relevant choices and consequences are independent and the allocation rule fits the constraints. The value-per-capital ranking in [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) requires divisible, linearly scalable investments and one initial capital limit; indivisibility, minimum scale, interactions or later funding needs can defeat it. These conditions do not hold merely because each asset has a score.

An optimizer can help when enumerating a larger set becomes burdensome, provided the actual selection rules, interactions, dates and criteria can be represented. If a consequential relation remains unqualified, retain that uncertainty or obtain the missing result.

### EAM.10:12 - Relations

[EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md)–[EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) supply supported policies and comparison criteria. [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) supplies applicable demand; [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) supplies service and dependency conditions. [FIN.9](../fin/22-fin-9---compare-capital-investments-and-allocations.md) supplies compatible joint financial consequences and dated funding comparison. [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) establishes timing; [EAM.12](21-eam-12---integrate-specialist-results-for-an-asset-recommend.md) receives the recommendation for decision; [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns changed premises. [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) supports multi-criterion comparison, and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) supports proportionate additional inquiry.

### EAM.10:End
