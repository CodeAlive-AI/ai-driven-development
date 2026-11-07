## ECO.10 - Trace Efficiency Savings through Demand Responses (Rebound Effects)

> **Type:** Method pattern
> **Status:** Stable

### ECO.10:1 - Problem frame

Use this pattern when a method or technology uses less of a resource per useful result and you need to know whether total resource use will also fall. Start by naming the useful result, resource, boundary and comparison without the change. Then follow the responses which can change total use.

The useful result is a conditional total-use comparison or a response threshold that matters to the decision. A fixed-output engineering comparison can stand alone when that is the stated question and output truly remains fixed.

### ECO.10:2 - Problem

Lower unit consumption can make a service cheaper, enable more frequent use, release spending for other activities or make new activities feasible. These responses can offset some or all of the initial saving. The case in which they more than offset it is commonly called Jevons's paradox or backfire.

An increase observed after an efficiency improvement does not establish this mechanism: demand could have grown anyway. Nor does higher output automatically defeat the purpose; growth, accessibility and a resource cap are different purposes.

### ECO.10:3 - Forces

Physical efficiency, prices, demand and total effects have different boundaries and time scales. Forecasting every response can be more expensive than the decision warrants. A useful threshold can guide action even when the future volume is unknown.

### ECO.10:4 - Solution

#### ECO.10:4.1 - State the comparison

Name the service or other useful result in units that preserve the needed performance. Identify the resource whose total matters, the affected activities, the period and the situation without the proposed improvement. A cost reduction, an energy reduction and an emissions reduction are different claims.

Use three totals under the same resource account: use without the improvement, use after the improvement at the counterfactual output without an induced response, and use after the response. The first minus the second is the fixed-output saving; the third minus the second is the response-induced change. Include equipment, infrastructure or transition burdens in the relevant totals when they matter to the claimed scope. A burden that arises even at unchanged output belongs in the second total, not in the demand response. Reuse the relevant PHY, MMP, OPS, MA or FIN result.

#### ECO.10:4.2 - Follow the responses that can change the answer

Ask how the improvement changes attainable action. Can users buy more of the same service, providers expand output, released funds support other activity, or a previously infeasible use become practical? Do prices, capacity, time, access rules or a resource cap limit these responses? Trace the mechanism before choosing a demand estimate.

Keep resource use within the focal activity separate from consequential use elsewhere. Add effects only within the declared total, avoid counting the same effect twice, and retain uncertainty where the effect is not known. Consider a new model, causal study or measurement only when its result can change the choice, supported conclusion or warranted use, and its attainable value warrants the burden.

For a simple unchanged service with resource use per unit e and volume q, total use is e × q. Compare improved total use with the counterfactual total, not just with last year's observed value. If per-unit use falls from e0 to e1, the fixed-boundary break-even volume is q0 × e0/e1 when e1 is positive. This is a threshold under the stated assumptions, not a demand forecast. When additional terms matter, compare the full totals instead of extending this simple threshold unchanged.

#### ECO.10:4.3 - Return the consequence to the actual purpose

First state whether total use after the response is lower than, equal to or higher than use without the improvement. Then, if useful, report the fraction of the fixed-output saving offset by the induced response: divide the response-induced change by the fixed-output saving. This percentage requires a positive, well-defined saving. Otherwise report the separate totals and the induced change. The percentage here uses the declared resource account; an operating-only rebound estimate and an estimate including equipment or transition burdens have different bases. A response which exceeds a positive fixed-output saving is the backfire case.

Compare responses appropriate to the purpose. A growth objective may welcome more valuable output. A resource cap may require allocating the released capacity or controlling aggregate use as well as improving efficiency. Each intervention has its own feasibility, cost and affected interests; the rebound calculation does not select a policy automatically.

Return a choice, a conditional operating limit or the observation that would change it. Stop when the comparison already distinguishes the feasible alternatives.

### ECO.10:5 - Archetypal Grounding

#### ECO.10:5.1 - Half the energy per unit

A constructed process would produce 100 equivalent units at 2 kWh each without an improvement: 200 kWh. The improved process uses 1 kWh per unit. At unchanged output its fixed-output saving is 100 kWh.

If the improvement induces output of 150 units, total use is 150 kWh and the actual saving is 50 kWh. Half the fixed-output saving is offset: rebound is 50%. At 220 units total use is 220 kWh; actual saving is −20 kWh, so rebound is 120%, the backfire case. The break-even output is 200 units.

These are conditional arithmetic cases. If output without the improvement would already have risen to 180 units, the relevant counterfactual is 360 kWh, not 200. Observing 220 improved units against an earlier year's 100 does not by itself demonstrate backfire.

Now suppose the declared account also includes 150 kWh for the new equipment and transition in the same period, absent from the no-improvement alternative and incurred regardless of output. The three totals at an induced volume of 150 are 200, 250 and 300 kWh. Fixed-output saving is −50 kWh; the response adds a further 50 kWh. Total use rises by 100 kWh, but this account has no positive saving whose offset can be expressed as a rebound percentage. The operating efficiency gain remains real; the broader total separates its additional burden from the demand response.

#### ECO.10:5.2 - An AI task becomes cheaper

A firm reduces the cost per accepted analysis and considers using the saving for more analyses. Token count is not the useful-result unit if acceptance, human revision or result quality also changes. The firm compares cost and resource use per accepted result, possible volume and the receiving work's value.

A fixed budget can increase the number of useful analyses without lowering expenditure. Electricity or hardware use may move differently from expenditure.

### ECO.10:6 - Bias-Annotation

A dramatic paradox can replace a causal account. Engineering optimism can assume fixed demand without saying so; pessimism can assume unlimited expansion. Preserve both the technical gain and the conditions of its economic response.

### ECO.10:7 - Conformance Checklist

Are the useful result, resource, boundary, period and counterfactual recoverable? Does each response have a plausible mechanism? Are the arithmetic and any rebound percentage consistent with that comparison? Does the conclusion distinguish resource conservation from valuable expansion and avoid treating a scenario as an observed causal estimate?

### ECO.10:8 - Common Anti-Patterns and How to Avoid Them

- **A unit saving is reported as a total saving.** Carry it through the relevant volume and other induced uses.
- **Every subsequent increase is called rebound.** Compare with what would have happened without the change.
- **Backfire is assumed for every efficiency gain.** Find the attainable response and its constraints.
- **A carbon, energy or cost figure changes meaning mid-calculation.** Keep each total and its conversion grounds separate.

### ECO.10:9 - Consequences

Efficiency proposals can be compared without hiding their demand consequences or discarding their useful gains. A threshold may be enough to choose a bounded trial or operating rule. Broader effects can remain conditional rather than being replaced by an unsupported universal rebound rate.

### ECO.10:10 - Architectural Rationale

The physical relation between input and result is one contribution to a larger economic account. Demand and feasible uses can change because of the improvement itself. Separating that response from unrelated growth connects engineering, economics and the receiving purpose without reducing them to one number.

### ECO.10:11 - SoTA-Echoing

[Brockway and colleagues (2021)](https://eprints.whiterose.ac.uk/id/eprint/171952/) compares evidence and modeling approaches for economy-wide energy rebound; its estimates are not transferable constants. The [FAccT 2025 analysis of AI rebound](https://facctconference.org/static/docs/facct2025-206archivalpdfs/facct2025-final37-acmpaginated.pdf) makes contemporary AI mechanisms and attribution limits explicit.

This pattern adopts mechanism and boundary analysis, then uses only the detail needed by the receiving choice. Fixed-output engineering calculation remains the right rival for a fixed-output question. A broad macroeconomic model is useful when its additional responses can change the decision and its assumptions fit; it is not a prerequisite for the simple threshold. Reopen when performance, demand, access, prices or the resource boundary changes.

### ECO.10:12 - Relations

ECO.2 supplies price responses; ECO.3 identifies new feasible exchanges; ECO.7/.9 address shared-resource or rule changes when those are selected. PHY and MMP supply physical and computational models, OPS supplies flow and capacity, MA and FIN supply cost and financial comparisons. General FPF choice and portfolio methods compare the retained alternatives; this pattern adds the demand-response contribution.

### ECO.10:End
