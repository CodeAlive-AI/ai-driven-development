## OPS.10 - Qualify Operating Capacity Under Variability

> **Status:** Stable


### OPS.10:0 - Use This When

Use this Method when demand, a proposed commitment, a queue policy or a resource change requires an answer about what the operation can support. Typical cues are “we have enough hours on average,” “the system is only eighty percent utilized,” “add another person,” or “this buffer should guarantee the deadline.”

The first useful result is a capacity-and-service comparison for the actual demand, resource arrangement and horizon. It states usable resource time, required load, relevant variation, feasible alternatives, supported service consequences and uncertainty. It returns a bounded option or the exact missing input needed to decide.

Start with a simple load/time bound and add only the analysis that the service question requires. Use OPS.9 when the limiting mechanism is itself unresolved. Use OPS.5 for an individual admission decision under an adequate capacity basis. A clinical staffing rule, engineering capability, labor condition or financial authorization is supplied by its own qualified practice.

When the needed calculation is missing, OPS.10.1 - Construct and Compare Operating Capacity Models develops finite, mean or probabilistic service consequences from the operating conditions. OPS.10.2 - Construct and Revise a Feasible Deadline Schedule develops resource sequencing, calendar placement and conditional time reserve for a finite delivery. Reuse an adequate calculation without repeating these constructions.

### OPS.10:1 - Problem frame

Capacity is useful only relative to a service, resource capability, operating conditions and time window. Nominal resource hours, accessible hours, hours usable by the required skill or configuration, completed service visits and accepted operating results are different quantities.

Variability matters even when totals fit. Demand can arrive together, service can take longer, a provider can withdraw access, a qualified person can be absent, or failed work can return. The operation may have enough total hours and still miss a deadline because the needed hours occur at the wrong time or require incompatible resources.

### OPS.10:2 - Problem

Average load divided by nominal capacity can conceal unusable time, setup, recovery, skill restrictions and rework. A favorable mean can also conceal long waits or losses for a protected service class.

The opposite response applies a sophisticated queueing model to every decision. That creates calculation effort and apparent precision without improving a bounded choice that a transparent schedule or stress scenario could already settle.

### OPS.10:3 - Forces

| Force | Practical tension |
| --- | --- |
| utilization and timely service | Keeping a resource busy can consume the slack needed to absorb a burst or recover. |
| simple estimates and changing conditions | A mean estimate is cheap; its validity can disappear when mix, timing or availability changes. |
| pooling and capability | Shared time can help only where the resource can perform the required service under its conditions. |
| capacity and reversibility | Extra capacity can be costly or slow to obtain; scheduling and batch changes can be cheaper but have their own consequences. |
| explicit reserve and apparent waste | Unused capacity can look inefficient while protecting a specified response or recovery scenario. |

### OPS.10:4 - Solution

#### OPS.10:4.1 - State the demand and service question

Name the accepted result, population, demand profile, horizon and service criterion. Distinguish a service-visit queue from the operation's final accepted-result population. State whether the question concerns a hard deadline for known jobs, a mean delay, a probability of completion, a protected response class or a bounded overload scenario.

Recover the initial unfinished work and its remaining service requirements. Preserve the customer's waiting origin when local release times differ. If a target is an existing commitment, keep its parties and authority; a calculated service scenario does not create a promise.

#### OPS.10:4.2 - Recover usable time and required load

For each necessary resource, identify capability, access, calendar, location, configuration and skill conditions. Deduct known unusable intervals only where they actually remove the needed service. Keep uncertainty about outages or absence separate from known deductions.

Translate each demand class into resource-time requirements under the supplied Method. Include normal setup, joint-resource occupancy, expected or scenario-specific rework, recovery and other consequential load. State which effects are already included in a service-time estimate so they are not counted again as lost capacity.

Use compatible units. Two hours of a specialist and two hours of a general resource are not four hours of interchangeable service. A test attempt and an accepted release are not two interchangeable outputs.

The first calculation is a necessary bound: required load cannot exceed usable time for a resource within the required window. Passing that bound is not enough when precedence, arrival timing, simultaneous resources or non-interchangeable classes can prevent a schedule.

#### OPS.10:4.3 - Choose the smallest adequate service analysis

| Receiving question | Appropriate first analysis | What it can establish |
| --- | --- | --- |
| Can these known jobs fit the actual windows? | A finite schedule using arrival, readiness, service, calendar and precedence data, or a necessary time/resource bound. | A feasible assignment; impossibility only when a necessary bound or complete valid search excludes the deadline. |
| What is a useful mean steady-state screen? | A queueing approximation whose population, service, routing, stability and dependence assumptions fit. | A qualified mean estimate, not a tail guarantee. |
| What happens under a specified disruption or burst? | A trace replay or explicit stress schedule, with actual policy and resources. | A conditional scenario result, not its probability of occurrence. |
| Does a changing or coupled operation meet a probabilistic service target? | A stochastic model or simulation of the relevant inputs and policy, retaining parameter and model uncertainty. | A conditional service probability; reliance on actual service additionally needs the corresponding input and model basis. |

For a single continuously available compatible server operating first-come, first-served, a finite calculation can be very small. For each job in arrival order, start is the later of its arrival and the previous finish; finish is start plus service time; wait is start minus arrival. This assumes no other setup, interruption, precedence or resource requirement. Add those conditions to the schedule when they apply.

Do not use a steady-state approximation for a finite overload or changing regime merely because it yields a number. Correlated bursts, feedback, blocking, priorities and skill classes may require a different model. A specialist analysis is a named input with a receiving use, not a substitute for stating the operating question.

#### OPS.10:4.4 - Test variability and the proposed change

Compare the current arrangement with the smallest material alternatives: demand/admission changes, timing, usable access, skill coverage, batch/setup changes, pooling or segregation, reserve, recovery and capacity acquisition.

Keep the result and service criterion fixed. Inspect arrival patterns as well as total demand, service and recovery variation as well as average duration, and common-cause losses as well as independent failures. Test the plausible adverse conditions that can reverse the choice.

A batching change may reduce setup time while delaying the first result or defect feedback. A pooled resource may improve a mean while changing a tail or protected class. A reserve must name the disturbance and capability it covers. A proposed schedule must not claim improvement by moving waiting outside the measured start boundary.

Use C.11.CRC for the finite comparison of consequences, resource cost, transition, reversibility and affected options. Keep a recommendation, provision of the resource, authority to use it and the resulting performance separate.

#### OPS.10:4.5 - State exactly what the result supports

Name each result as a hard bound, a feasible schedule under stated inputs, a stress scenario, an estimated mean, a percentile/probability forecast or an unresolved question. Attach the relevant uncertainty, data window and model limitations. Historical coverage of a target is not automatically its future probability.

For a consistently defined population with stable compatible averages, Little's relation L = λW connects mean in-system count, effective flow rate and mean time. Returns, rework, abandonment and finite-window boundary terms need correct population accounting. The arrival/exit rate of service visits is not necessarily the rate of accepted final results. The relation is useful for consistency; it neither supplies a delay distribution nor makes a protective buffer sufficient.

If the available basis supports only a load bound, return that bound and the exact missing service information. A missing distribution does not prevent a known infeasibility result or a useful conditional stress comparison.

#### OPS.10:4.6 - Return the operating decision and refresh basis

Return demand and result units, horizon, usable capacity and load assumptions, the selected analysis, alternative consequences, chosen option or exact blocker, provision/decision authority, residual demand and reopening conditions.

OPS.5 can use this basis for admission. OPS.8 can use it for release and protection. OPS.7 can use changed feasibility evidence for an existing commitment. Use OPS.13, or an appropriate method from the responsible service practice, to establish a wider credible service offer; the local capacity result alone does not supply it.

Reopen when mix, arrivals, access, capability, absence, failure/rework, resource coupling or the service criterion changes. Retain observations of actual performance so the next decision can test, rather than silently inherit, the previous model.

### OPS.10:5 - Archetypal Grounding

#### OPS.10:5.1 - PumpWorks: fit, reserve and a deferred package

In this constructed extension, four eligible test packages each require two consecutive rig-hours, including their normal setup, under the current estimate. In the next eight-hour horizon, this operation has access during hours 0–6; hours 6–8 are currently reserved for another use. This gives six continuous usable rig-hours. Permission and required configuration for the tests are current; release authority and SafetyQuestion-S19 remain separate.

The initial load is eight rig-hours, so all four packages cannot fit the six usable hours even before uncertain recovery. More ready packages or a larger buffer cannot remove that deficit.

For comparison, assume one adverse scenario: one of the planned packages needs a single consecutive two-hour repeat, after which it passes. The failed attempt is identified on completion and its repeat can run next under the current test conditions. This is a supplied scenario, not an estimated failure probability. The resource owner can offer hours 6–8 to this operation through a separate access and cost decision that accounts for the displaced use.

| Option | Usable rig-hours | Planned packages | Explicit reserve | Accepted test packages without repeat | Accepted packages in the one-repeat scenario |
| --- | ---: | ---: | ---: | ---: | ---: |
| current access, plan three | 6 | 3 | 0 | 3 | 2, with unfinished load returned |
| extra access, plan three | 8 | 3 | 2 | 3 | 3 |
| extra access, plan four | 8 | 4 | 0 | 4 | 3, with unfinished load returned |

If the operating decision requires three completed packages in both stated scenarios, the second option supports that comparison; the first does not. If the decision instead values four nominal completions and can accept the stated adverse shortfall, the third is a different choice. Cost, permission and affected commitments remain explicit rather than being hidden in “maximum utilization.”

The first useful return can therefore be: obtain the authorized extra access, admit three packages for this plan, reserve two hours for the named repeat scenario, and return the fourth package to OPS.5 and any affected existing commitment to OPS.7. If the extra access is not obtained, use the six-hour result instead.

More than one repeat, a longer repeat, changed configuration or another loss reopens the comparison. A passed test package still does not settle the release decision for R42.

#### OPS.10:5.2 - Equal total load, different waiting

One continuously available server processes four one-hour jobs. There is no setup, failure, other resource or initial backlog.

| Scenario | Arrival times in hours | Start times | Waiting times |
| --- | --- | --- | --- |
| one burst | 0, 0, 0, 0 | 0, 1, 2, 3 | 0, 1, 2, 3 |
| one job per hour | 0, 1, 2, 3 | 0, 1, 2, 3 | 0, 0, 0, 0 |

Both consume four server-hours and finish the last job at hour 4. If the criterion is completion within two hours of arrival, two of four jobs meet it in the burst scenario and all four in the second. The difference follows from the stated arrival scenarios.

This result tells the practitioner why total hours alone cannot settle service. It does not authorize delaying already arrived demand and then starting its clock later.

#### OPS.10:5.3 - Nominal beds and qualified capacity

A hospital's bed count is not the capacity for every care requirement. The receiving question may depend on the supplied clinical class, staffing qualification, equipment, cleaning readiness, access and synchronized availability.

OPS.10 can compare operating arrangements from those qualified inputs and state a resource-time or scenario result. If the clinical eligibility or staffing Method is missing, it returns that exact input. It does not invent a clinical staffing ratio or treat every empty bed as usable service capacity.

### OPS.10:6 - Bias-Annotation

| Bias | Consequence | Countermeasure |
| --- | --- | --- |
| nominal-capacity bias | Calendar presence substitutes for usable capability and access. | Recover the relevant service and resource conditions. |
| average sufficiency | Equal totals are treated as equal service. | Inspect arrival timing, variation and the actual service criterion. |
| double-counted loss | A failure is included in service time and again deducted from capacity. | State each estimate's contents and count the effect once. |
| precise-number confidence | A sophisticated model hides poor premises. | Match model scope to the question and qualify the result kind. |
| reserve-as-waste bias | Recovery capacity is removed to increase utilization. | Compare the named disturbance and service consequence. |

### OPS.10:7 - Conformance Checklist

1. Are demand, service visits, accepted results and the waiting origin distinct where they affect the calculation?
2. Does usable capacity include the actual capability, access, calendar and joint-resource conditions?
3. Does required load include relevant setup, recovery and rework without double counting?
4. Does the chosen analysis fit the finite/steady, deterministic/stochastic and dependence conditions?
5. Are the service criterion, uncertainty and adverse scenarios explicit in the option comparison?
6. Does the result distinguish its supported claim from resource provision, authority and a service promise?
7. Can the receiving admission, queue or commitment decision use the result and identify its reopening condition?

The calculation is recognizable when another practitioner can reproduce its inputs and outputs. Assurance requires the empirical and professional basis appropriate to the claimed bound, model or forecast.

### OPS.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Total demand is below total hours, so the deadline is safe. | Timing, precedence or incompatible capability can prevent a schedule. | Recover the actual resource windows and a feasible witness. |
| Use mean utilization as a service guarantee. | The wait distribution and relevant tail remain unknown. | State the intended service criterion and select a suitable analysis. |
| Treat a scenario as a probability. | No occurrence model or calibrated data supplies that probability. | Label the conditional result and return the missing probabilistic basis. |
| Treat every person or machine-hour as interchangeable. | Capability, configuration and access differ. | Compare usable service capacity by the relevant class. |
| Count repeats as additional delivered results. | Attempts and accepted outputs have different identities. | Keep load and result populations separate. |
| Buy capacity before establishing the limiting mechanism. | The added resource may not change completion. | Use OPS.9 where the treatment basis is unresolved. |

### OPS.10:9 - Consequences

The operation can distinguish known infeasibility, conditional feasibility and supported service uncertainty. Admission and protection decisions can use reserve deliberately rather than treating all unused time as waste.

The cost is maintaining resource and workload premises that can change. A modest schedule can be enough for a small finite decision; a consequential probabilistic promise may need substantial specialist modeling and evidence.

### OPS.10:10 - Rationale

Usable capacity, workload and service are related but different. A load bound answers whether enough required resource time exists. A schedule answers whether that time can be used as needed. A service forecast adds a claim about uncertain outcomes. Keeping these questions separate prevents a cheap answer to one from being mistaken for an answer to all three.

### OPS.10:11 - SoTA-Echoing

| Practice question and selected line | Serious alternative, trade-off and pattern change | Source roles, limits and reopen condition |
| --- | --- | --- |
| Can average population and flow data establish timely service? **Adopt** compatible population accounting; **reject** using a mean identity as a tail guarantee. | Mean utilization cannot distinguish the two arrival scenarios in 5.2. A mean-flow identity can recover different mean times from compatible population data, but does not establish their two-hour completion fractions. Sections 4.1, 4.3 and 4.5 retain the service criterion and result kind. | [Little (2011)](https://doi.org/10.1287/opre.1110.0940) supplies the mature mean-relation basis, not a deadline model. The finite example provides the decision-changing contrast at comparable calculation effort. Reopen when the population, boundary, returns or required service claim changes. |
| What model should handle dependent arrivals and feedback? **Adapt** model selection to the actual temporal and network dependence. | A simple independent-input mean approximation is easier but can omit consequential burst structure. Sections 4.3–4.5 call for a suitable specialist model only when that omission can reverse the decision. | [Whitt and You (2022)](https://doi.org/10.1002/nav.22010) is a bounded model candidate: a single-class open single-server network with Markovian routing, nonrenewal arrivals and feedback, estimating mean steady-state performance through dispersion functions. It does not supply every service tail or transient solution. Reopen for nonmatching routing, classes, regime or service criterion. |
| Should the response be more capacity, pooling, or a different batch policy? **Adapt** finite comparison of setup, waiting, reliability and service effects. | Capacity additions can be lumpy; smaller batches and pooling can have different protected consequences. Sections 4.2–4.4 and 5.1 retain those costs and scenarios rather than selecting a universal utilization or pooling rule. | Reinertsen (2009), batch-size trade-offs, supplies a mechanism candidate. [Andradóttir et al. (2017)](https://doi.org/10.1016/j.ejor.2016.05.009) and [Cao et al. (2021)](https://doi.org/10.1287/opre.2019.1976) supply conditional pooling counterexamples. Their studied conditions are not transferable staffing or rig prescriptions. Reopen when capability, failures, batching or the service criterion changes. |

### OPS.10:12 - Relations

OPS.3 and OPS.4 supply the matching subjects, resource relations and qualified current observations. OPS.8 supplies the release/queue/buffer policy whose consequences are analyzed. OPS.9 supplies a supported limiting mechanism when choosing a capacity treatment depends on it. OPS.11 handles consequential cross-structure constraints.

OPS.5 consumes an adequate capacity basis for admission; OPS.6 continues permitted Work without treating the plan as performance; OPS.7 uses changed feasibility for an existing bounded commitment. OPS.13 and OPS.14 use the capacity basis with their own service and financial inputs to address the wider commitment and operating-consequence decisions.

Current FPF C.16, C.27.TA/C.27, C.11.CRC and C.11 govern measurement, temporal interpretation, finite comparison and choice. Field specialists supply the capability, labor, engineering, clinical, safety and financial premises for their respective uses.

### OPS.10:End
