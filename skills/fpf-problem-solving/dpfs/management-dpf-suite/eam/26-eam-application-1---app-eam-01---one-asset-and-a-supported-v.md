## EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison



### EAM.Application:1.1 - Shared CityWater premises

CityWater 2027 is a fictional utility with twelve pumping stations in two service areas. A and C are in North; B and D are in East; the other eight stations supply the remaining capability and are unchanged by the compared options. A, B and D have abnormal vibration. Existing, case-supplied diagnostic accounts distinguish their conditions and support the particular interventions below; the vibration label alone supplies neither diagnosis nor a life estimate.

The case supplies an existing water-delivery mandate issued by CityWater's water-service authority. It requires water of the stated quality and minimum delivered North/East rates of 700/700 m³/h during the dry work window and 1,100/900 during the wet season. The case assigns revision of this mandate to the water-service authority; the infrastructure committee chooses the asset programme within it.

Separately, the supplied operating account gives normal usable North/East capability of 1,000/1,000 m³/h. The wet-season North requirement exceeds present usable capability by 100 m³/h. Both shortlisted C options add 200 m³/h, either by modification or by a qualified leased service. The 200 is the contribution of these options, not an unstated minimum increment. During a dry-window outage, A removes 200 from North and C removes 300; B and D each remove 200 from East. One A or C outage fits the dry requirement, but their simultaneous outage gives only 500 and does not. Simultaneous B and D outages leave 600 in East and also fail. These are finite supplied service bounds, not a hydraulic model or a probability of reliability.

The case additionally supplies applicable engineering and service-risk qualifications for each shortlisted policy, including the supported fallback and response to abnormal conditions. Their boundaries cover the stated duty and horizon. No claim about every contingency or a new real equipment limit is derived from the simple supply totals. If a qualification is absent or invalidated, [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) removes that option from the eligible comparison and returns the missing specialist question. Lower financial cost does not repair the missing qualification.

The comparison horizon is the five years beginning with the initial 2027 decisions. All values are constructed millions of constant-price euros, from the utility's stated perspective. The real discount rate is 3% solely for this example. Initial capital and initial operating cash occur at time zero; recurring costs occur at each year end; residual value occurs at the end of year 5. The supplied terminal values represent remaining service value, net of the stated exit costs, on the same basis for every option. A different sale/withdrawal decision needs its own terminal-value basis. Different technical lives do not disappear at the five-year boundary.

The annual amounts include the specified energy, routine maintenance, inspection, contingent response and continuing service costs under each policy; do not add them again as a separate generic risk allowance. A material unpriced consequence remains outside the sum and must retain its own criterion. Historical expenditure is sunk for this future choice. Accounting depreciation is not an additional cash outflow. Financing and tax effects are held equal in this constructed comparison; a real difference would require explicit treatment by its supplying practice.

Define `a = Σ(t=1..5) 1/(1.03)^t = 4.579707187` and `d = 1/(1.03)^5 = 0.862608784`. For each option, `present cost = initial capital + initial operating cash + annual cost × a − terminal value × d`.

| Asset/option | Initial capital | Initial operating cash | Annual cost | Terminal value | Whole team/outage days | Present cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A: refurbish (`F`) | 2.0 | 0 | 0.30 | 0.40 | 2 | 3.028869 |
| A: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| B: refurbish (`F`) | 2.0 | 0 | 0.35 | 0.40 | 2 | 3.257854 |
| B: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| C: modify (`M`) | 3.0 | 0 | 0.20 | 0.80 | 3 | 3.225854 |
| C: leased service (`L`) | 0 | 0 | 1.20 | 0 | 1 | 5.495649 |
| D: continued-use policy (`K`) | 0 | 0.50 | 1.00 | 0 | 1 | 5.079707 |
| D: replace (`R`) | 3.0 | 0 | 0.35 | 1.20 | 3 | 3.567767 |

Each duration includes the required isolation, intervention, testing and return for that option, using one already qualified and available team. Prerequisite design, procurement and non-outage preparation are supplied as complete before the window. Days denote the same staffed whole-work windows in both the calendar and the estimates; they are not individual person-days. These are teaching inputs, not equipment procedures or industry duration norms. For a real case, use the [MNT.7](../../engineering-dpf-suite/mnt/18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) result rather than assuming those inclusions.

The D continued-use policy is a supported five-year service policy with the specified initial maintenance intervention, recurring maintenance, response and backup provisions. It is not an unsupported extrapolation of a one-year condition forecast. The case's qualification is conditional on unchanged duty and the identified failure mechanism; a new structural finding invalidates it. No new diagnosis, repair effectiveness or permission is inferred from the economic calculation.



### EAM.Application:1.2 - The request about D and its answer

The infrastructure committee asks the EAM practitioner whether D should continue under the supported maintenance policy or be replaced now, assuming both choices have funding and a suitable window. MNT can adequately recommend the 0.50 intervention for maintained functioning. EAM asks the additional value question at the same service and horizon.

Continued use costs `0.50 + 1.00 × a = 5.079707`. Replacement costs `3.00 + 0.35 × a − 1.20 × d = 3.567767`. Replacement saves 1.511940 in present cost within the admitted comparison. The completed result can therefore be a recommendation to replace, qualified by the supplied service, engineering, funding and timing conditions. It is not a work order or a hand-back result.

The comparison also gives a useful stop for inquiry. Holding the other inputs fixed, continued use and replacement are equal when the continued-use annual cost is 0.669861. An existing justified range of 0.95–1.05 does not reverse the recommendation, so a new cost investigation solely to decide between these options is unnecessary. A credible annual cost of 0.60 would reverse that economic choice; a credible result about that possibility could be useful if obtainable in time at a justified total burden. This is sensitivity, not a probability distribution. The EAM practitioner uses the specialist's engineering assessment of D's stated duty and the water-delivery mandate in the shared premises above to establish which policies remain eligible. The sensitivity calculation answers only the cost question.

If the operator asks only about present condition or the intervention needed to maintain the already selected use, the maintenance practitioner can answer by supplying the applicable condition account or intervention recommendation. The operator receives that bounded maintenance answer. When the question is instead which asset option offers better value over this horizon, the EAM practitioner supplies the additional comparison even though there is only one asset.



### EAM.Application:1.3 - When the complete policy is still missing

The D comparison above starts from complete, supported policies. When a new request instead supplies only an initial repair price, [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) constructs the policy before [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) compares it. In its separate asset E case, initial work supports three years but the service is required for four; the further overhaul, its window and temporary service belong to the alternative. Omitting that work reverses the apparent cost preference while leaving year four unsupported.

[FIN.6](../fin/19-fin-6---value-capital-projects.md) supplies the dated financial account for the stated technical policy, and [FIN.7](../fin/20-fin-7---value-assets-and-the-corporation.md) supplies its ending valuation. Moving only the end of the explicit table to year two requires a value that represents the same later cash and ending premise; [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) shows that the whole present cost and preference remain unchanged. Ending the service at year two instead changes the required policy and uses actual exit consequences. A different supplied valuation must be reconciled to its changed assumptions before it can change the recommendation. If an observation later changes technical support or the ending premise, [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns the affected policy to [EAM.8](17-eam-8---generate-maintenance-renewal-and-retirement-alternat.md) and the comparison. D's supplied five-year premises and the programme calculation below remain their own case.
