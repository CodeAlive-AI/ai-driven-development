## EAM.6 - Assess Asset Capacity, Resilience, and Interdependence

> **Type:** Method
> **Status:** Stable

### EAM.6:1 - Problem frame

Use this pattern when an asset option must meet demand through a particular arrangement, outage or disruption. The total installed rating appears sufficient, but the needed contribution depends on shared assets, access, timing or recovery.

Begin with the service criterion and one applicable capacity bound. Return the supported capacity and consequence account, including the condition that makes a proposed option fail. A simple calculation can be sufficient. Develop the dependencies and recovery intervals when they determine what service remains available.

### EAM.6:2 - Problem

Nominal ratings can be added even when the assets cannot supply the same service together. A fallback can rely on the same failed provider as the asset it is meant to replace. Normal-load adequacy and a successful isolated-outage calculation can then conceal loss of several contributions together.

Recovery also changes the answer over time. Enough stored reserve for one interval may be exhausted before another asset becomes usable. A single final recovery time hides that intermediate service failure.

### EAM.6:3 - Forces

Reserve capability and recovery provisions cost resources while protecting a specified service. Pooling can improve utilization but create common dependencies. More elaborate models can improve a consequential assessment, but unsupported detail cannot establish a probabilistic reliability claim.

### EAM.6:4 - Solution

#### EAM.6:4.1 - Establish the contribution being tested

Recover demand, required service, configuration and horizon. Keep quantities and time units compatible. [EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) can supply scenario demand and its place, period and driver conditions; [EAM.5](14-eam-5---assess-asset-condition-and-performance.md) can supply the applicable condition concern. Use [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) or a specialist result to distinguish nominal capability from usable contribution.

State where the service must be delivered and which population or function it protects. An aggregate spare capacity elsewhere is useful only if the arrangement can deliver it where and when needed. Begin with a supply or load bound that the available inputs support.

#### EAM.6:4.2 - Derive the disturbance from actual dependencies

Identify the asset contributions and the dependencies that can change the answer. Follow shared power, control, providers, access, storage or another asset's functioning to the service they enable. Explain which contributions cease, degrade or remain usable when a selected dependency is lost. Include a common dependency even when it crosses the portfolio's ownership boundary.

Test a fallback against that same loss. A second pump on the failed feeder supplies no replacement flow until its needed power is restored. An alternative is independent of that feeder loss only when its power, control, connection and other necessary support remain usable under the stated scenario. This is a dependency claim for the named disturbance; a separate statistical independence claim needs its own evidence.

Choose adverse conditions because their consequences can change the asset decision: a named outage, common-provider loss or credible demand burst. Use an existing qualified scenario where it matches. Preserve simultaneous calls on shared reserve; one standby contribution cannot be allocated twice to incompatible users.

Compare material alternatives on the same disturbance and service criterion. An alternative may change the dependency itself, so recalculate the remaining contributions rather than carrying over the old consequence account.

#### EAM.6:4.3 - Follow service through recovery

Divide the disturbance into intervals at which demand, usable contribution or restoration changes. Use times to usable service, including the necessary access, work, testing and return conditions. A repair-completion estimate alone may omit the time before the contribution can actually be used.

For each interval, compare required service with supported available contribution. Where an additive bound is applicable, the positive difference is the deficit. Multiply a constant deficit by the interval length to obtain the reserve volume or resource needed during it. Carry the remaining usable reserve forward; test both its deliverable rate and its remaining amount. Account for other users' simultaneous demands on it.

Credit replenishment only when its route, rate, timing and operating conditions are supported. If flows or demand vary materially within an interval, refine the intervals or obtain an appropriate time-dependent result. A total-volume comparison alone cannot establish pressure, quality or other delivery conditions.

The service requirement may include an allowed interruption, minimum contribution or restoration deadline. Apply that actual criterion to each interval. Report where and for how long it fails. Keep evidence for restoration timing separate from a proposed recovery plan: an unqualified time leaves the dependent conclusion conditional.

#### EAM.6:4.4 - Compare remedies and return the conditions

Compare additional capability, demand changes, sequencing, reserve, another fallback or changed recovery. Preserve burden and lost service moved to other users. An option that meets this scenario becomes a qualified candidate for the asset comparison, with its costs and remaining conditions.

Obtain a hydraulic, electrical, structural or stochastic result when that relationship determines the answer. Specify the arrangement, disturbance, required service and intervals it must address. A supported specialist result can replace an inadequate simple bound without restarting unrelated parts of the assessment.

Return the service envelope, failed scenario or precise missing result to [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md)–[EAM.10](19-eam-10---compare-engineered-asset-portfolio-combinations.md), and the relevant outage and recovery conditions to EAM.11. Stop when the receiving question is answered. Reopen on changed demand, dependencies, recovery support or operating conditions. Passing the selected scenarios supports only their stated scope.

### EAM.6:5 - Archetypal Grounding

#### EAM.6:5.1 - A sufficient outage and buffer bound

CityWater's North area has 1,000 m³/h usable capability before C is modified and needs 700 during the dry work window. Removing A's 200 leaves 800; removing C's 300 leaves 700. Each isolated outage passes the quantity bound. Removing both leaves 500, a 200 m³/h shortfall. Their individual feasibility therefore does not justify simultaneous work.

In an additional constructed variant, an independently qualified usable buffer contains 400 m³ and can cover that deficit at the required delivery conditions. The arithmetic gives 400 ÷ 200 = two hours. It cannot support a three-hour combined outage without another qualified contribution. This calculation assumes the stated usable volume and delivery rate; it does not derive them from tank size or establish water quality.

After the selected 200 m³/h addition, normal North capability is 1,200 against the wet minimum of 1,100. That comparison does not establish performance under every loss of station, power or control. Any such stronger claim needs its own applicable scenario or model.

#### EAM.6:5.2 - Shared failure and different recovery intervals

A separate constructed water system must continuously deliver 400 m³/h. Two units each supply a qualified 250 m³/h but share one feeder. An independent third source supplies 100 m³/h. Usable stored reserve is 300 m³, with delivery qualified for the deficits considered here.

A feeder loss removes both 250 contributions. One returns after one hour and the other after two. During the first hour, only 100 m³/h remains, so preserving service requires (400 − 100) × 1 = 300 m³. The reserve is exhausted at one hour. During the next hour, 250 + 100 = 350 m³/h leaves another 50 m³/h deficit. The arrangement fails the continuous-service requirement despite normal capability of 600 m³/h.

Now consider a qualified additional 250 m³/h supply that can operate independently of this feeder loss and is usable after half an hour. Its support and connection are supplied as case premises.

| Interval after loss | Available contribution, m³/h | Required reserve rate, m³/h | Required reserve volume, m³ |
| --- | ---: | ---: | ---: |
| 0–0.5 h | 100 | 300 | 150 |
| 0.5–1 h | 350 | 50 | 25 |
| 1–2 h | 600 | 0 | 0 |

Before the first feeder-dependent unit returns, required reserve is 150 + 25 = 175 m³. The initial 300 therefore covers the stated intervals, leaving 125 m³; no replenishment is assumed. From one hour, the available contributions meet the 400 requirement. The added supply is a feasible response to this constructed scenario, to be compared with other supported remedies and their burden.

If the added supply actually depends on the failed feeder, remove its contribution and the first conclusion returns: service fails after one hour. If it is independent but becomes usable only after 1.5 hours, the first hour exhausts storage and the next half-hour has a 50 m³/h deficit. Independence alone therefore does not establish timely service. Earlier availability, a further usable 25 m³ of reserve, a different restoration arrangement or another supported alternative could change that latter result.

Use actual dependency and restoration evidence before relying on such a calculation. The case establishes neither the probability of feeder loss nor the hydraulic feasibility of an unexamined network. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) and EAM.8 compare the supported remedy; [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) must retain its half-hour availability and restoration conditions in the time arrangement.

### EAM.6:6 - Bias-Annotation

Average service can hide a severe local loss. Inspect the protected population or location used by the decision. Dependency data can also overrepresent documented technical links while omitting access, providers or decisions that affect real recovery.

### EAM.6:7 - Conformance Checklist

Are demand and usable capability compared under the same conditions? Can the reader trace the selected dependency loss to the contributions that cease? Does the reserve remain available under that loss and concurrent use? Are its amount and rate sufficient in every relevant interval? What supports restoration timing, and what stronger claim would require another model?

### EAM.6:8 - Common Anti-Patterns and How to Avoid Them

Adding nameplate ratings can overstate joint capacity. Recover the actual combined service contribution.

Calling unused capacity “resilience” leaves the protected disturbance unknown. State the loss or demand scenario and test what remains deliverable.

Using final restored capacity to cover an earlier deficit hides interrupted service. Follow the contributions and remaining reserve through the intervening intervals.

### EAM.6:9 - Consequences

The practitioner can reject an infeasible combination or identify a proportionate recovery change before committing resources. The account shows which dependency or restoration premise changes the result, so the affected alternative or timing can be reconsidered. It remains conditional on the modeled service, dependencies and evidence.

### EAM.6:10 - Architectural Rationale

The same arrangement supplies normal service and responses to disturbance. Recovering its dependencies constructs the scenario; interval comparisons establish its service consequences. [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) and specialist models supply applicable capacity reasoning, while EAM relates that result to asset choices and recovery conditions. A necessary bound and a sufficient supported scenario have different reach.

### EAM.6:11 - SoTA-Echoing

For a named outage, first use the qualified capacity/service reasoning in [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) and an applicable supply or duration bound. The constructed 400 m³ buffer and 200 m³/h deficit establish a two-hour limit, sufficient to reject the three-hour proposal.

[IAM Anatomy v4, §7.5.6, pp. 66–67](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf#page=66), relates disturbance to the extent and duration of service loss and recovery objectives. [GFMAM Landscape v3, §3.9](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=45), distinguishes asset and organizational resilience. The dependency and recovery construction above adapts those concerns to an asset choice: the shared feeder removes two contributions, and the time at which independent supply becomes usable changes the answer.

For consequential water-network relationships, extended-period hydraulic analysis is a stronger alternative. The US EPA's [EPANET capabilities and hydraulic modeling description](https://www.epa.gov/water-research/epanet) covers pressure, flow, tank levels and controls. Obtain such a result when deliverability or changing network behavior remains unqualified. Reuse an applicable existing result where available.

A supported simple bound is enough for the failed-duration question; dependency and interval reasoning is needed for the shared-loss question. Neither substitutes for an unresolved hydraulic relationship or failure-probability estimate. Reopen the choice of method when controls, demand, reserve delivery or restoration conditions change the answer beyond the current model's reach.

### EAM.6:12 - Relations

[EAM.4](13-eam-4---assess-demand-and-service-need-for-asset-decisions.md) supplies demand and [EAM.5](14-eam-5---assess-asset-condition-and-performance.md) the condition concern. [EAM.7](16-eam-7---generate-ways-to-supply-an-asset-dependent-service.md) and EAM.8 use a required contribution or recovery alternative; [EAM.9](18-eam-9---compare-asset-alternatives-and-reconcile-decisions-w.md) and EAM.10 use the resulting service and dependency constraints. [EAM.11](20-eam-11---time-asset-interventions-and-manage-dependencies.md) consumes the interval-specific outage and recovery conditions. [OPS.10](../ops/40-ops-10---qualify-operating-capacity-under-variability.md) supplies qualified capacity reasoning, and [FPF C.16](../../../sections/09-part-c---kernel-extension-specifications/27-c-16---measurement-metrics-characterization.md) supports compatible quantities and uncertainty.

### EAM.6:End
