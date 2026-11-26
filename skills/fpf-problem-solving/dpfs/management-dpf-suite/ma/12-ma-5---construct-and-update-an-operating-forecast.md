## MA.5 - Construct and Update an Operating Forecast

**Type:** Architectural

**Status:** Stable

### MA.5:0 - Use this when

Use this pattern when a coming workload, resource need or monetary consequence must be anticipated and a target or historical average cannot answer the question. Start with the quantity, dates and use the recipient has specified. Where the horizon is yours to choose, allow time for the action the forecast is intended to inform.

The pattern governs a conditional operating forecast. It returns the relevant demand, resource and monetary outlook, the assumptions that can change it and the conditions for updating it.

Use an adequate current forecast directly. Seek greater detail when the requested outlook or a decision that relies on it needs that detail.

### MA.5:1 - Problem frame

An operation needs to anticipate demand, material use, capacity and payment timing. Some inputs can be estimated from current orders; others depend on uncertain demand or intended actions. A future resource threshold can matter even when the central workload estimate fits current capacity.

A forecast expresses what is expected under stated conditions. A target expresses an ambition; an authorized resource amount expresses a decision. Their relationship is useful, but one cannot be substituted for another.

### MA.5:2 - Problem

A forecast built by extending last period's totals can conceal a changed mix, resource threshold or collection delay. A forecast negotiated as a target can conceal expected difficulty.

An elaborate model can still be unhelpful if its horizon is too short to act or its assumptions cannot be revised. Forecast the requested quantities under the relevant conditions, including uncertainty that could change their interpretation.

### MA.5:3 - Forces

The user needs a timely answer even when the future is uncertain. A single number is convenient, while a range or scenario can better preserve the condition that matters.

Actions taken in response to a forecast can change the outcome. Later evaluation must therefore retain the original conditions and the response rather than treating every numerical miss as the same forecasting failure.

### MA.5:4 - Solution

#### MA.5:4.1 - Choose the receiving use and horizon

Keep the forecast quantity, information cutoff, horizon and delivery date set by the recipient. For example, an update of the month-end outlook using orders known by Friday keeps that cutoff and month end. Where a choice is delegated, select dates that give the intended recipient time to prepare or act. Supplying the forecast on its agreed basis can complete the commission.

Recover the adequate existing account and forecast. Determine whether the missing answer concerns demand, resource conversion, money, timing or uncertainty. Request the detail needed to support that answer or its intended use.

#### MA.5:4.2 - Construct compatible demand inputs

Fix the output being forecast, the population, period and information cutoff. Orders requested for next month can exceed the quantity delivered and accepted in that month. For delivered units, include the due backlog, work that can be completed in time and the applicable acceptance conditions. Distinguish units, customers and transactions before combining them. MA.8 supplies the time and population account when several customer cohorts or product phases contribute.

Separate work already included from work still to be estimated. For requested deliveries, begin with booked work due in the period that is expected to remain due. Add further requests for that period from the remaining population. If the supplied forecast already covers all requests, adding the booked quantity counts it twice. To forecast completed deliveries, follow both contributions through the feasible service arrangement for the same period.

Construct the missing component from evidence suited to it. Comparable history can supply a simple benchmark, such as the average further orders received after the same cutoff when demand conditions are stable. Compare like populations and horizons; a seasonal series needs a relevant seasonal comparison, and a changed offer or sales channel can defeat an old average. Judgment can incorporate information absent from that history, but name the changed condition and how it affects the quantity. A specialist forecast can be used directly when its population, cutoff, horizon and assumptions fit.

Begin with the simplest supported forecast that answers the receiving question. Compare added complexity against that benchmark on observations not used to fit or choose the model when predictive accuracy is the claimed gain. Obtain a forecasting method or specialist contribution where estimation requires it. A few teaching observations, an attractive fit or three labeled scenarios do not establish predictive calibration.

Keep observed facts, commitments, estimates and proposed actions distinguishable. State whether a precise statistical claim reports a mean, quantile or another defined quantity. A central planning scenario is not automatically an expected value. Where the evidence supports only a conditional scenario, preserve that qualification instead of presenting the scenario as an evidenced expectation.

#### MA.5:4.3 - Carry the outlook through work and monetary accounts

For a question about resource demand or a payment that depends on it, use the relevant output and mix to obtain attempts, setups, processing and resource demand through MA.1. Compare demand with the usable capacity and actual supply options in MA.2. A fixed payment remains fixed under its terms; a further block is introduced only in the branch where it is obtained. Different products can require different resource quantities even when their total unit count is unchanged.

For a monetary outlook that depends on balances and settlement, use MA.4's opening balances and event movements. A forecast confined to workload or its capacity threshold can be returned from the quantities already established. Forecast production or purchases, delivery and recognition, and settlement at their relevant dates; then derive inventory, receivables and payables at period end. Collection of an opening receivable creates a receipt without another sale. Production held for later delivery can require payment before the corresponding revenue. Carry each closing balance into the next period as its opening balance. Preserve any necessary MA.3 assignment for the receiving report without turning that assignment into a new payment.

When a shortage changes the forecast, distinguish the pressure on capacity, an action management could take and the action it can be expected to take. An approved response can settle the latter. With a decision still open, report the forecast at issue, or the outcomes conditional on the available responses. Implementing a supply change requires the corresponding authority.

#### MA.5:4.4 - Retain the uncertainty that changes action

Use a range, scenarios or a supported probabilistic model according to the question and available evidence. Preserve dependencies between uncertain inputs when independently combining favorable values would create an implausible case.

Inspect the conditions that can change feasibility, a payment block or the useful response. A forecast need not specify every contingency to reveal a decisive capacity threshold. If a material input cannot be estimated adequately, state the conditional conclusion or identify the question the missing input leaves open.

Represent uncertainty in forecast revenue and receipts at the detail needed for their use. State which conclusions the available evidence supports.

#### MA.5:4.5 - Return the forecast and usable response conditions

Supply the quantities, timing and assumptions in a form the recipient can use. If a decision is at issue, identify the relevant condition, such as workload beyond usable capacity or a payment before available funding.

The forecast does not authorize that response. When a response is commissioned, use the responsible operating or financial decision method. When payment feasibility is the question, connect the selected flows to the payer’s resources at the relevant dates, including other obligations and only transfers that can reach it in time.

#### MA.5:4.6 - Update from changed conditions and learn from outcomes

Revise the affected assumptions when new evidence or an actual decision changes them. Preserve the earlier forecast at the level needed to explain the change or learn from it; do not overwrite its premises and then claim it predicted the result.

When comparing with actual outcomes, distinguish changed external conditions, estimation error, bias and actions taken in response. Action taken in response to a forecast can prevent the adverse outcome it describes and explain a numerical difference. This does not by itself prove the forecasting model was accurate. Choose a comparison that can test the forecast claim under its stated conditions.

Meet the agreed reporting dates. When the timing of later updates is open, use the pace of change and the lead time for the receiving action. A rolling window can help; refreshing unchanged detail on a calendar alone can consume effort without improving the result.

A target gap can initiate design work through MA.10. Preserve the outlook under the existing arrangement while constructing the proposed alternative's outlook from its changed offer, work and provision. The target is not a demand observation. If a design change affects both price and service behavior, revise both dependencies rather than changing only a cost assumption. MA.9 supplies a missing arrangement for participants to use and challenge the resulting expectations before commitments are made.

### MA.5:5 - Archetypal Grounding

#### MA.5:5.1 - Obtain the missing demand input

At the information cutoff, sixty booked units are due next month and are expected to remain due. In three comparable earlier months, customers requested another 35, 40 and 45 units for delivery in the respective month after the same cutoff. These requests came in addition to each month’s booked work. The historical units were delivered. Here the first question concerns the volume customers will request for next month.

Assume unchanged demand conditions and no relevant trend or seasonality for this example. The average residual of (35 + 40 + 45) / 3 = **40** is a simple benchmark, so sixty booked plus forty further units gives **100 units requested for delivery**. A forecast already covering all such requests includes the sixty. These three observations illustrate the construction; they do not establish a calibrated distribution.

The account also considers two separate conditions. A channel interruption would remove twenty of the forty residual units, while a proposed campaign could bring twenty additional units beyond the benchmark. Neither changes the sixty booked units under the supplied premises. The interruption branch gives **80 units requested** and the campaign branch **120**. The campaign effect is additional to the normal residual population. These are alternative planning scenarios, not probabilities or effects to add simultaneously. In practice, obtain the channel and campaign evidence that makes their effects plausible. If the stable-demand premise fails and no replacement estimate is supported, retain conditional scenarios or obtain a better forecast.

A reader with adequate scenarios of requested deliveries can use them directly to calculate the resources needed to fulfil them. The next comparison shows how much can be delivered and accepted under each supply arrangement.

#### MA.5:5.2 - Convert and revise the supplied scenarios

For demands of 80, 100 and 120 units, the service calculates how much time it would take to fulfil every request. The scenarios carry no probability weights. One setup takes ten hours and each unit requires 0.25 qualified staff-hours. The base arrangement provides 38 usable hours for 120 currency units. A further five-hour block can be obtained for 80. In the following comparison the resources booked for the period are paid on day 1. Assume the hours fit the service windows, materials can be obtained in time and customers accept each conforming unit delivered by the cutoff.

| Workload scenario | Required staff-hours | Relevant supply condition |
| --- | ---: | --- |
| 80 units | 10 + 80 × 0.25 = **30** | Fits the supplied 38 hours. |
| 100 units | 10 + 100 × 0.25 = **35** | Fits the supplied 38 hours. |
| 120 units | 10 + 120 × 0.25 = **40** | The base hours can cover at most 112 units. Obtaining the five-hour block allows all 120 to be served on the stated terms. |

Materials cost 3 for each unit produced. The service recognizes sales of 10 per unit on customer acceptance. Suppose it buys on day 1 just the materials for the quantity it will deliver and the customers pay on day 30. With requests for 100 units and all 100 accepted, sales and receipts are 1,000. Material and resource payments on day 1 are 300 and 120. If collection moves to next month, the same 1,000 of sales becomes a closing receivable. MA.4 carries it forward to collection. A funding decision uses the payer’s whole dated cash position.

At 120 requests, the base arrangement can deliver **112 units**, since (38 − 10) / 0.25 = 112. If the service uses all those hours and the 112 units are accepted, the stated purchasing and settlement terms give 336 for materials, 120 for base provision and 1,120 in sales and receipts. With the additional block obtained and all 120 units accepted, materials cost 360, resource payments total 200 and accepted sales bring 1,200 on day 30. Buying materials for all 120 while delivering 112 would still cost 360 for materials.

If twenty of the 100 units instead require 0.50 hour while eighty still require 0.25, demand becomes 10 + 20 × 0.50 + 80 × 0.25 = **40 hours**. Unchanged total volume therefore crosses the same supply threshold. This establishes the capacity threshold. To forecast the block payment, also establish who decides and when. If a block must be reserved in advance to guarantee service, it costs 80 even when demand is low. When the still-available block is bought after the signal, expected payment is 80 times the probability of purchase. If the rule requires buying one block whenever the qualifying demand crosses the threshold and in no other case, use the probability of that threshold event. These unweighted scenarios leave that probability open.

If demand in the central scenario changes to 96 units and all 96 are made and accepted under the same terms, resource demand becomes **34 hours**, materials **288** and sales **960**. The existing supply payment remains 120. Updating every amount by four percent would wrongly reduce that unchanged payment.

If the team instead obtains extra capacity in response to the high scenario, the revised forecast includes that decision under the terms on which the capacity was obtained. Later outcomes are compared with the conditions of each forecast.

### MA.5:6 - Bias-Annotation

People may conceal an adverse outlook when reporting it threatens a target or future resources. Separate the meanings through MA.6 and inspect the incentives through MA.9 when needed.

A modeler can also mistake abundant historical data for stable future behavior. Changed product mix or supply terms can invalidate a precise extrapolation.

### MA.5:7 - Conformance Checklist

Does the forecast answer for the requested quantity, cutoff and horizon? If it informs a decision, will it reach the recipient in time? Check that the demand inputs refer to the right population without duplication, that the relevant resource or cash consequences follow under the assumed decisions, and that any uncertainty which could change the conclusion is visible. Identify what new evidence would warrant an update.

A constructed scenario demonstrates a conditional consequence. Forecast calibration, actual performance and the success of a response require their corresponding evidence.

### MA.5:8 - Common Anti-Patterns and How to Avoid Them

**Adding orders to a total-demand forecast.** Establish which population the forecast already includes before adding a residual.

**Scaling every cost with volume.** Preserve the supply thresholds and unchanged payments.

**Treating an adverse forecast as a failed promise.** Recover the outlook that was requested, its assumptions and any action taken in response.

**Improving the forecast by rewriting its history.** Retain the earlier premises needed for a valid comparison.

### MA.5:9 - Consequences

The user can prepare for a consequential range and revise the account when evidence changes. The forecast can expose a capacity or funding question early enough for action.

More uncertainty may remain visible than in a negotiated single number. The work also needs maintained assumptions; their detail should be justified by the receiving use.

### MA.5:10 - Architectural Rationale

The receiving question sets the forecast’s horizon. When the recipient must act on it, lead time also matters. Resource and monetary dependencies preserve consequences that total extrapolation can hide.

A stable simple forecast can be adequate for a stable use. Scenarios are useful when different plausible conditions require different responses. A more detailed predictive model is justified by the additional decision-relevant distinction and evidence it can supply.

### MA.5:11 - SoTA-Echoing

The selected line uses Bogsnes's *Implementing Beyond Budgeting*, second edition (2016), printed pp.159–166: forecasts describe expected consequences, should be timely and actionable, and can use scenarios where a point number conceals uncertainty. The current [Beyond Budgeting principles][BB] retain a lean forecasting process distinct from targets and resource allocation.

This changes §§4.1–4.6 by tying horizon and detail to use and preserving responses when learning from outcomes. The pattern qualifies the source's strong external-versus-internal accuracy distinction: intervention changes what comparison is warranted; it does not prohibit evaluating a specified conditional forecast.

Hyndman and Athanasopoulos, *Forecasting: Principles and Practice*, third edition, develops the complementary construction: [chapter 6](https://otexts.com/fpp3/judgmental.html) relates judgment to available data and information, [§6.5](https://otexts.com/fpp3/scenarios.html) builds scenarios from drivers and their interactions, and [§5.8](https://otexts.com/fpp3/accuracy.html) separates fitting from accuracy on held-out observations. §§4.2–4.4 apply these distinctions to the accounting population and its resource consequences. The purpose separation in Beyond Budgeting does not itself supply a demand predictor.

The simple residual benchmark makes the input obtainable, while three resource scenarios reveal a supply threshold. Reopen the affected construction when the response horizon, demand basis, dependencies or relevant uncertainty changes. A stipulated scenario can support its conditional calculation without a fitted predictive model.

### MA.5:12 - Relations

MA.1–MA.4 supply resource and account construction. MA.6 separates forecast, target and resource decisions; MA.7 explains differences; MA.8 supplies cohort or product assumptions. Those responsible for operating and financial decisions can use the forecast in their respective work.

### MA.5:End
