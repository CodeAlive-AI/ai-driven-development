## MA.5 - Construct and Update an Operating Forecast

**Type:** Architectural

**Status:** Stable

### MA.5:0 - Use this when

Use this pattern when a coming workload, resource need or monetary consequence must be anticipated and a target or historical average cannot answer the question. Begin with the action the forecast could change and the lead time needed to act.

The pattern governs a conditional operating forecast. It returns the relevant demand, resource and monetary outlook, the assumptions that can change it and the conditions for updating it.

Use an adequate current forecast directly. Additional detail is useful only when it can change the receiving action or its assurance.

### MA.5:1 - Problem frame

An operation needs to anticipate demand, material use, capacity and payment timing. Some inputs can be estimated from current orders; others depend on uncertain demand or intended actions. A future resource threshold can matter even when the central workload estimate fits current capacity.

A forecast expresses what is expected under stated conditions. A target expresses an ambition; an authorized resource amount expresses a decision. Their relationship is useful, but one cannot be substituted for another.

### MA.5:2 - Problem

A forecast built by extending last period's totals can conceal a changed mix, resource threshold or collection delay. A forecast negotiated as a target can conceal expected difficulty.

An elaborate model can still be unhelpful if its horizon is too short to act or its assumptions cannot be revised. Forecast the quantities and conditions that could change the receiving action, with enough detail to show the uncertainty that matters.

### MA.5:3 - Forces

The user needs a timely answer even when the future is uncertain. A single number is convenient, while a range or scenario can better preserve the condition that matters.

Actions taken in response to a forecast can change the outcome. Later evaluation must therefore retain the original conditions and the response rather than treating every numerical miss as the same forecasting failure.

### MA.5:4 - Solution

#### MA.5:4.1 - Choose the receiving use and horizon

State who will use the forecast, what decision or preparation it could change and when that action must occur. Choose a horizon long enough for the relevant response.

Recover the adequate existing account and forecast. Determine whether the missing answer concerns demand, resource conversion, money, timing or uncertainty. Avoid requesting details that the receiving use would not act on.

#### MA.5:4.2 - Construct compatible demand inputs

Fix the output being forecast, the population, period and information cutoff. A forecast of orders accepted next month differs from one of units delivered next month: carry the order backlog and promised delivery dates into the latter. Distinguish units, customers and transactions before combining them. MA.8 supplies the time and population account when several customer cohorts or product phases contribute.

Separate what is already included from what remains to be estimated. For a delivery forecast, begin with due work expected to survive cancellation or rescheduling, then estimate further work that can enter and be delivered in that period. Keep those components disjoint. If a supplied forecast already covers all deliveries, adding current orders to it would count part of the population twice.

Construct the missing component from evidence suited to it. Comparable history can supply a simple benchmark, such as the average further orders received after the same cutoff when demand conditions are stable. Compare like populations and horizons; a seasonal series needs a relevant seasonal comparison, and a changed offer or sales channel can defeat an old average. Judgment can incorporate information absent from that history, but name the changed condition and how it affects the quantity. A specialist forecast can be used directly when its population, cutoff, horizon and assumptions fit.

Begin with the simplest supported forecast that can change the decision usefully. Compare added complexity against that benchmark on observations not used to fit or choose the model when predictive accuracy is the claimed gain. Obtain a forecasting method or specialist contribution where estimation requires it. A few teaching observations, an attractive fit or three labeled scenarios do not establish predictive calibration.

Keep observed facts, commitments, estimates and proposed actions distinguishable. State whether a precise statistical claim reports a mean, quantile or another defined quantity. A central planning scenario is not automatically an expected value. Where the evidence supports only a conditional scenario, preserve that qualification instead of presenting the scenario as an evidenced expectation.

#### MA.5:4.3 - Carry the outlook through work and monetary accounts

Use the relevant output and mix to obtain attempts, setups, processing and resource demand through MA.1. Compare demand with the usable capacity and actual supply options in MA.2. A fixed payment remains fixed under its terms; a further block is introduced only in the branch where it is obtained. Different products can require different resource quantities even when their total unit count is unchanged.

Use MA.4's opening balances and event movements to obtain the monetary outlook. Forecast production or purchases, delivery and recognition, and settlement at their relevant dates; then derive inventory, receivables and payables at period end. Collection of an opening receivable creates a receipt without another sale. Production held for later delivery can require payment before the corresponding revenue. Carry each closing balance into the next period as its opening balance. Preserve any necessary MA.3 assignment for the receiving report without turning that assignment into a new payment.

A resource shortage can require a changed schedule, scope or supply arrangement. Obtain that operating decision and update the affected delivery and payment consequences; do not retain impossible deliveries merely because their revenue was forecast first. Keep unrelated assumptions unchanged.

#### MA.5:4.4 - Retain the uncertainty that changes action

Use a range, scenarios or a supported probabilistic model according to the question and available evidence. Preserve dependencies between uncertain inputs when independently combining favorable values would create an implausible case.

Inspect the conditions that can change feasibility, a payment block or the useful response. A forecast need not specify every contingency to reveal a decisive capacity threshold. If a material input cannot be estimated adequately, state the conditional conclusion or exact unresolved question.

Represent uncertainty in forecast revenue and receipts at the detail needed for their use. Uncertainty does not by itself prohibit forecasting them; it limits the conclusions a particular forecast can support.

#### MA.5:4.5 - Return the forecast and usable response conditions

Supply the quantities, timing and assumptions in a form the recipient can use. Identify the condition that would require a decision, such as workload beyond usable capacity or a payment before available funding.

The forecast does not authorize that response. Use the responsible operating or financial decision method. When payment feasibility is the question, connect the selected flows to the whole timed cash account, including other relevant receipts and obligations.

#### MA.5:4.6 - Update from changed conditions and learn from outcomes

Revise the affected assumptions when new evidence or an actual decision changes them. Preserve the earlier forecast at the level needed to explain the change or learn from it; do not overwrite its premises and then claim it predicted the result.

When comparing with actual outcomes, distinguish changed external conditions, estimation error, bias and actions taken in response. Action taken in response to a forecast can prevent the adverse outcome it describes and explain a numerical difference. This does not by itself prove the forecasting model was accurate. Examine the claim and comparison actually needed.

Choose refresh timing from the pace of relevant change and the receiving action. A rolling window can help; refreshing unchanged detail on a calendar alone can consume effort without improving the result.

A target gap can initiate design work through MA.10. Preserve the outlook under the existing arrangement while constructing the proposed alternative's outlook from its changed offer, work and provision. The target is not a demand observation. If a design change affects both price and service behavior, revise both dependencies rather than changing only a cost assumption. MA.9 supplies a missing arrangement for people to use and challenge the resulting expectations before commitments are made.

### MA.5:5 - Archetypal Grounding

#### MA.5:5.1 - Obtain the missing demand input

At the information cutoff, a service has sixty booked units due next month. Under the supplied teaching premises they will remain due and be delivered. Three comparable earlier months received another 35, 40 and 45 units after the same cutoff, all delivered in the respective forecast month. These counts exclude each month's already booked work.

Assume unchanged demand conditions and no relevant trend or seasonality for this example. The average residual of (35 + 40 + 45) / 3 = **40** is a simple benchmark, so sixty booked plus forty further units gives **100**. Adding the sixty to a forecast of total deliveries would have been a different, overlapping calculation. These three observations illustrate the construction; they do not establish a calibrated distribution.

The account also considers two separate conditions. A channel interruption would remove twenty of the forty residual units, while a proposed campaign could bring twenty additional units beyond the benchmark. Neither changes the sixty booked units under the supplied premises. The interruption branch gives **80**; the campaign branch gives **120**. The campaign effect is additional to the normal residual population. These are alternative planning scenarios, not probabilities or effects to add simultaneously. In practice, obtain the channel and campaign evidence that makes their effects plausible. If the stable-demand premise fails and no replacement estimate is supported, retain conditional scenarios or obtain a better forecast.

A reader who already has adequate 80/100/120 scenarios can enter the following conversion directly.

#### MA.5:5.2 - Convert and revise the supplied scenarios

A service forecasts next period's workload using three planning scenarios: 80, 100 or 120 accepted units. These are supplied scenarios without probability weights. The adequate resource model requires ten setup hours plus 0.25 qualified staff-hours per unit. A supplied arrangement provides 38 usable hours for 120 currency units; a feasible extra five-hour block costs 80.

| Workload scenario | Required staff-hours | Relevant supply condition |
| --- | ---: | --- |
| 80 units | 10 + 80 × 0.25 = **30** | Fits the supplied 38 hours. |
| 100 units | 10 + 100 × 0.25 = **35** | Fits the supplied 38 hours. |
| 120 units | 10 + 120 × 0.25 = **40** | Needs an adequate additional arrangement; the supplied five-hour block is one option. |

Materials require 3 per unit, and the service price is 10 per accepted unit. In the 100-unit scenario, materials are 300 and sales are 1,000. The supplied collection assumption places the 1,000 receipt on day 30, while the 300 material and 120 resource payments occur on day 1. A funding use needs the whole cash account. If the 1,000 is instead collected next month, current-period revenue can remain 1,000 under the same recognition rule while the closing receivable rises by 1,000 and this period has no corresponding receipt. MA.4 carries that receivable into the next period; it is not a second sale then.

The original workload fits the 38 hours through **112 units**, since (38 − 10) / 0.25 = 112. If twenty of the 100 units instead require 0.50 hour while eighty still require 0.25, demand becomes 10 + 20 × 0.50 + 80 × 0.25 = **40 hours**. Unchanged total volume therefore crosses the same supply threshold. The operating account must establish a feasible response. An expected workload of 100 alone would not establish an expected block payment: the block depends on how often the threshold is crossed, for which these unweighted scenarios supply no probability.

If new evidence changes the central scenario to 96 units, its resource demand becomes **34 hours**, materials **288** and sales **960**. The existing supply payment remains 120. Updating every amount by four percent would wrongly reduce that unchanged payment.

If the team instead obtains extra capacity in response to the high scenario, the revised forecast includes that decision under its actual terms. Later outcomes are compared with the conditions of each forecast.

### MA.5:6 - Bias-Annotation

People may conceal an adverse outlook when reporting it threatens a target or future resources. Separate the meanings through MA.6 and inspect the incentives through MA.9 when needed.

A modeler can also mistake abundant historical data for stable future behavior. Changed product mix or supply terms can invalidate a precise extrapolation.

### MA.5:7 - Conformance Checklist

Examine whether the forecast has a receiving action and useful horizon; constructs or obtains compatible, nonoverlapping demand inputs; connects them to resource and balance movements; distinguishes facts, estimates and proposed actions; retains uncertainty that can change the result; and has a warranted update rule.

A constructed scenario demonstrates a conditional consequence. Forecast calibration, actual performance and the success of a response require their corresponding evidence.

### MA.5:8 - Common Anti-Patterns and How to Avoid Them

**Adding orders to a total-demand forecast.** Establish which population the forecast already includes before adding a residual.

**Scaling every cost with volume.** Preserve actual supply thresholds and unchanged payments.

**Treating an adverse forecast as a failed promise.** Recover its conditions and the decision it was intended to inform.

**Improving the forecast by rewriting its history.** Retain the earlier premises needed for a valid comparison.

### MA.5:9 - Consequences

The user can prepare for a consequential range and revise the account when evidence changes. The forecast can expose a capacity or funding question early enough for action.

More uncertainty may remain visible than in a negotiated single number. The work also needs maintained assumptions; their detail should be justified by the receiving use.

### MA.5:10 - Architectural Rationale

The forecast is organized around the action it could change because accuracy at an irrelevant horizon has little practical value. Resource and monetary dependencies preserve consequences that total extrapolation can hide.

A stable simple forecast can be adequate for a stable use. Scenarios are useful when different plausible conditions require different responses. A more detailed predictive model is justified by the additional decision-relevant distinction and evidence it can supply.

### MA.5:11 - SoTA-Echoing

The selected line uses Bogsnes's *Implementing Beyond Budgeting*, second edition (2016), printed pp.159–166: forecasts describe expected consequences, should be timely and actionable, and can use scenarios where a point number conceals uncertainty. The current [Beyond Budgeting principles][BB] retain a lean forecasting process distinct from targets and resource allocation.

This changes §§4.1–4.6 by tying horizon and detail to use and preserving responses when learning from outcomes. The pattern qualifies the source's strong external-versus-internal accuracy distinction: intervention changes what comparison is warranted; it does not prohibit evaluating a clearly specified conditional forecast.

Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, third edition, develops the complementary construction: [chapter 6](https://otexts.com/fpp3/judgmental.html) relates judgment to available data and information, [§6.5](https://otexts.com/fpp3/scenarios.html) builds scenarios from drivers and their interactions, and [§5.8](https://otexts.com/fpp3/accuracy.html) separates fitting from accuracy on held-out observations. §§4.2–4.4 apply these distinctions to the accounting population and its resource consequences. The purpose separation in Beyond Budgeting does not itself supply a demand predictor.

The simple residual benchmark makes the input obtainable, while three resource scenarios reveal a supply threshold. Reopen the affected construction when the response horizon, demand basis, dependencies or relevant uncertainty changes; do not require a fitted predictive model for every useful stipulated scenario.

### MA.5:12 - Relations

MA.1–MA.4 supply resource and account construction. MA.6 separates forecast, target and resource decisions; MA.7 explains differences; MA.8 supplies cohort or product assumptions. OPS and the relevant financial practice use the forecast for their decisions.

### MA.5:End
