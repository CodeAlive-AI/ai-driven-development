## EAM.4 - Assess Demand and Service Need for Asset Decisions

> **Type:** Method
> **Status:** Stable

### EAM.4:1 - Problem frame

Use this pattern when an asset choice depends on how much service will be needed, where and when. Average demand can fit current capability while a seasonal peak, protected service group or changing use makes an option inadequate.

Begin with the service question and distinguish current commitments from forecasts. Return the demand scenarios and requirements needed to compare asset options. If an existing demand assessment answers the question at the relevant boundary and period, use it. Construct a new account when its missing basis could change the asset choice.

### EAM.4:2 - Problem

Demand totals hide timing, location and service differences. Forecasts can be treated as commitments, while existing commitments can be dismissed as optional scenarios. Even plausible forecasts may conceal which observation, population or loss allowance produced the number. A large forecast model can also obscure a simple known shortfall.

### EAM.4:3 - Forces

Underestimating demand can leave service inadequate; overestimating it can commit resources to unnecessary capacity. Better forecasts cost time and data work. Uncertainty matters through the options or claims it could change, not merely through the width of a reported interval. A useful component account must preserve the period and boundary in which its quantities can be combined.

### EAM.4:4 - Solution

#### EAM.4:4.1 - Fix the service question and reuse an adequate answer

Identify the service result, recipients and relevant horizon. State the quantity and quality required, its timing and location, and the source and authority of any commitment. [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) can supply the operating service and commitment account.

Separate an authorized requirement from a forecast of use. A known seasonal commitment can be compared directly with the applicable capability. Further forecasting is useful when the choice depends on a missing or uncertain demand premise. Keep a protected-service or peak requirement explicit even when average consumption is lower.

#### EAM.4:4.2 - Construct an applicable observation basis

Choose the boundary at which demand will be compared with asset contribution. For a water district, distinguish water delivered to users from water entering the district: distribution losses make the quantities different. For a transport service, trips requested, passengers carried and vehicle movements likewise need a stated relation.

Recover present use, unmet requests and committed future use. Establish whether the observations cover the relevant users, place, period and operating conditions. Rationing, failure or inaccessible capacity can suppress recorded delivery. Obtain the missing need estimate or retain that uncertainty; relabeling observed delivery does not recover it.

Separate components whose drivers or possible interventions differ. Household use, other use and losses may be useful for a water decision. Reconcile their sum with the total on the same boundary and interval. If they disagree, investigate the mismatch that could affect the choice. A residual between compatible inlet and customer measurements may estimate losses; an unexplained discrepancy between incompatible meters cannot be assigned that meaning.

Keep the observation and its limitations available alongside the component account. More detailed segmentation is useful when it changes an option or the needed forecast.

#### EAM.4:4.3 - Vary drivers and form coherent scenarios

For each material change, explain how it affects a component: more users, different use per user, a new industrial commitment, changed losses or a shared environmental condition. Apply that change to the appropriate base. For example, a 10% increase in household use changes the household component, not automatically the district's losses and industrial use.

Combine component values for conditions that can occur together in the period being compared. Several site maxima can occur at different hours; weather can also make formerly separate peaks coincide. Where timing matters, construct a common-period profile or obtain the applicable specialist account. Preserve location, service class and quality conditions that a total could conceal.

Form an unchanged-policy baseline before crediting a proposed demand-management measure. Describe a measure's affected users, expected effect, delivery conditions and cost as an alternative for EAM.7. Use its reduction only in the scenario where those conditions hold. A proposed service reduction remains subject to the relevant authority.

Test the drivers that can change eligibility or preference. A justified range or a few explicit scenarios can be sufficient. If an option has 100 units of spare contribution, an uncertain additional demand spanning 90–170 leaves its adequacy unresolved; a range wholly above 100 establishes that this option cannot cover that demand range without another contribution. This threshold can identify a useful further inquiry. Give a scenario a probability only when evidence supports that interpretation.

A more elaborate forecast is needed when an important dependency, changing population or response to price, weather or restrictions cannot be supported by the simple account. Ask the specialist for the demand at the required boundary and periods, the relevant driver combinations, uncertainty and limitations. The receiving asset decision still compares the returned result under those conditions.

#### EAM.4:4.4 - Return the demand and the premise that could change it

Compare the constructed demand with the contribution being considered, including losses, coincidence, storage and operating conditions through applicable relationships. Return quantity, recipients, location, period, drivers and uncertainty conditions to [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) and EAM.7. Keep the source of an authorized commitment distinguishable from the evidence for a forecast.

Stop when the account distinguishes the useful options or identifies a specific unresolved premise. Obtain further forecasting or measurement when its attainable answer can change the choice or warranted claim enough to justify its burden and delay. When an observation changes a relied-on driver, [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns to this account and the affected capability or alternative; unchanged components can remain usable.

### EAM.4:5 - Archetypal Grounding

#### EAM.4:5.1 - Use a supplied requirement

In CityWater, North's dry-window minimum is 700 m³/h and its wet-season minimum is 1,100. Current usable capability is 1,000. An annual average of 800 would not establish adequacy for the wet season: the explicit deficit is 100 m³/h at that required time. Both shortlisted C arrangements add 200 and pass this quantity comparison under their supplied qualifications.

Now suppose a new forecast suggests 1,250 in a later period. That forecast is not automatically a revised mandate. The practitioner reports that the current 1,200-capability option would fall short by 50 under this scenario and identifies which service or investment decision would use it. A sufficiently credible and consequential scenario can warrant another option without inventing a new commitment.

#### EAM.4:5.2 - Build the scenario from its components

In a separate constructed district, Westbank, compatible observations of an unrestricted critical hour give 1,000 m³/h at the inlet: 600 for households, 300 for other users and 100 losses. The case supplies compatible measurement coverage and the loss estimate. Proposed usable capability at the same inlet is 1,200 m³/h; required quality is unchanged.

| Component at the common critical hour | Observed base, m³/h | Scenario assumption | Scenario demand, m³/h |
| --- | ---: | --- | ---: |
| Household use | 600 | 10% more use on the same service basis | 660 |
| Other use | 300 | No material change | 300 |
| Losses | 100 | Qualified future estimate of 140 | 140 |
| Total at the inlet | 1,000 | Sum of compatible components | 1,100 |

The calculation is 600 × 1.10 + 300 + 140 = 1,100. It leaves 100 m³/h of contribution available within the proposed capability. A separately supported new industrial requirement of 150 during that same hour gives 1,250 and exceeds capability by 50. The industrial addition is counted once: it was absent from the 300 base.

If the industrial maximum occurs at another hour, the practitioner obtains the other components for that hour before forming its total. Adding unrelated maxima would not establish the actual peak. If the original 1,000 observation was rationed, the unrestricted baseline first needs an applicable estimate of suppressed use.

A proposed leakage measure may reduce the scenario's losses from 140 to 80. With the industrial addition, the total would then be 660 + 300 + 150 + 80 = 1,190. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) can compare that measure with added supply, using its cost and evidence of achievable reduction. The ten-unit margin exists only while the assumed reduction, coincidence and other contributions remain supported. Treating the proposed 80 as the unchanged-policy loss estimate would hide the intervention that makes the option work.

### EAM.4:6 - Bias-Annotation

Observed delivery favors users who currently receive service. Consider excluded or suppressed demand when it changes the intended outcome. Demand reduction can move burden onto users whose interests are absent from the investment meeting.

### EAM.4:7 - Conformance Checklist

Can the reader recover the observation base and each material driver? Do component sums share a boundary and period, with suppressed use and coincidence addressed where they matter? Are the unchanged-policy baseline and proposed measures distinct? Are commitments, observations and forecasts distinguishable? Does each selected scenario change a decision or claim, and is any probability supported?

### EAM.4:8 - Common Anti-Patterns and How to Avoid Them

Comparing average demand with peak capacity can answer the wrong question. Compare required service at its actual window.

Using forecast demand as an authorized obligation silently changes the decision. Preserve the forecast's evidence and let the relevant authority decide any commitment.

Crediting a proposed reduction in the baseline conceals the option needed to produce it. Keep its effect with its implementation conditions and burden.

### EAM.4:9 - Consequences

Asset alternatives can be sized and timed against a need whose construction is recoverable. Some expansion proposals become unnecessary, while a local or seasonal deficit becomes explicit. Changing one driver can reopen the affected scenario without rebuilding adequate observations. The account remains qualified by its assumptions.

### EAM.4:10 - Architectural Rationale

Capacity is judged relative to a receiving service. [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) supplies the demand construction and its conditions; [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) determines what an asset arrangement can deliver, and [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) compares ways to close the gap. Keeping forecasts, commitments and proposed measures distinct supports both a direct known-requirement comparison and adaptation when the demand basis changes.

### EAM.4:11 - SoTA-Echoing

Choose the least burdensome supported comparison that distinguishes the asset options. [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) supplies measurement and uncertainty distinctions; [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) supplies the service and commitment account. North's known 1,100 m³/h requirement already exposes a 100 m³/h shortfall. A more accurate annual average would not resolve that peak-service question.

The Environment Agency, Natural Resources Wales and Ofwat's *Water resources planning guideline*, updated 16 June 2026, [§§6.1 and 6.4.1–6.4.3](https://www.gov.uk/government/publications/water-resources-planning-guideline/water-resources-planning-guideline#section-6--developing-your-demand-forecast), develops component demand, the observed baseline, critical periods and assumptions before additional measures. EAM adapts that contribution in the component reconciliation and driver construction above. The Westbank case shows why a changed driver or proposed reduction changes the asset comparison. Its values and arithmetic are constructed here.

A full specialist forecast is preferable when the relevant dependencies or uncertainty cannot be supported by that small construction. Request its result for the actual asset boundary and decision horizon. Reopen the method choice when new observations invalidate a driver or range, a changed period reveals a consequential peak, or the decision needs a fuller forecast. The water-planning source's jurisdictional duties and planning horizon remain with that source.

### EAM.4:12 - Relations

[EAM.2](11-eam-2---relate-assets-to-strategy-services-and-required-capa.md) supplies the service contribution and its source. [OPS.1](../ops/29-ops-1---identify-the-operating-system-commitments-and-flow-u.md) supplies operating commitments and populations. [EAM.6](15-eam-6---assess-asset-capacity-resilience-and-interdependence.md) consumes the scenario's quantity, place, period and conditions to compare capability; [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) uses its gap and qualified demand-management possibilities to develop alternatives. [EAM.13](22-eam-13---track-realized-outcomes-and-reconsider-asset-plans.md) returns changed observations or commitments to the affected part of this account.

### EAM.4:End
