## FIN.13 - Identify and Measure Financial Exposures

**Type:** Method

**Status:** Stable

### FIN.13:0 - Use this when

A change in rates, exchange prices, commodity prices, payment behavior or funding access could affect the corporation. Trace the exposure to actual claims and operations, then measure the consequence relevant to the decision. A reported notional amount alone does not identify the risk.

Use a sufficient existing exposure account when its outcome, entity, dates and conditions fit the decision. Rebuild the affected part when those grounds change. The explanations in Solution support constructing and adapting the account; the short steps suffice for a familiar application with adequate inputs.

### FIN.13:1 - Problem frame

The object is the sensitivity of specified corporate value, cash or claims to financial changes over a chosen horizon. Transaction, operating, valuation, counterparty and liquidity effects may coexist, but their measurements answer different questions.

### FIN.13:2 - Problem

Netting different entities or payment dates can hide a funding requirement. A large notional can have a small sensitivity, while an option or collateral requirement can create a large nonlinear or liquidity consequence.

### FIN.13:3 - Forces

Make material risks visible without measuring everything in one generic score. Use simple sensitivities where adequate and more detailed scenarios where timing, correlation or nonlinearity can change the answer.

### FIN.13:4 - Solution

1. Name the exposed corporation, position or activity, decision horizon and outcome of concern: cash needed, earnings variation, value loss or inability to perform. Use [FDM][FDM] for unresolved positions and FIN.4 for the required projection.
2. Trace rate resets, currency receipts and payments, commodity-linked operating cash, customer and counterparty payments, collateral and funding commitments. Distinguish a contractual amount from expected collection and from settled cash.
3. Group or offset exposures only where the decision permits it. Economic offset does not establish legal netting or intraday payment capacity; retain entity, currency and date differences that affect use.
4. Apply suitable measures. For a fixed foreign-currency net receipt, multiply the amount by exchange-rate changes. For rate-sensitive cash, use the actual reset, notional and accrual conventions. For nonlinear instruments, revalue material scenarios rather than extrapolate one small-change sensitivity.
5. Examine concentrations and combined adverse conditions. A customer delay can coincide with an exchange move, collateral call or loss of funding. If a statistical loss measure is used, state its outcome, horizon, probability model and limitations; it does not give a maximum possible loss.
6. Return the exposures and scenarios that can change action, existing protection and residual uncertainty. Use FIN.14 to compare protection, FIN.2 to assess resulting cash needs, or FIN.15 for an execution exception.



#### FIN.13:4.1 - Start with the consequence that can change a decision


An exposure is a relation between a financial change and a consequence for the corporation. Begin with a question such as “How much more cash will this borrower need before the next reset and payment?”, “How far can this export margin fall?” or “What value would these claims lose under the proposed market change?” These questions can use the same contracts but need different calculations.

Set the paying or owning entity, the horizon and the outcome before aggregating. For a cash question, retain currency, account access and actual payment order. For an earnings question, obtain the applicable recognition and translation treatment; a movement in reported earnings need not be a payment. For a value question, FIN.5 and FIN.7 supply compatible pricing and claim boundaries. A fall in the market value of fixed-rate debt can reduce the issuer's measured liability value while leaving the next coupon and principal payment unchanged. It therefore does not supply money with which the issuer can settle those payments.

Specify the comparison as well. A loss can mean a decline from today's value, a shortfall from a budget, or a difference from a feasible alternative. State which one is being measured. An export receipt of 85 against a budget of 90 gives a budget shortfall of 5; it does not show that choosing export instead of another business destroyed value 5. FIN.1 recovers that separate decision comparison.

Use an adequate supplied exposure account directly when its position, outcome, horizon and assumptions fit. Reconstruct it when a changed term, operating premise or receiving question defeats that fit. The method does not require a statistical model for every known payment or a complete risk inventory before answering one material funding question.



#### FIN.13:4.2 - Build the exposure from positions and operating causes


Begin with the positions and operating plan that generate the outcome. [FDM.1 through FDM.3][FDM] recover who holds each claim or obligation, which entity can use a resource, and how actual terms turn events into changed amounts or duties. FIN.4 supplies the projected flows and balances. Retain the part of those accounts needed to explain the present consequence.

For a foreign receipt, recover the currency of the amount actually owed, its amount or amount-setting rule, due date, plausible collection dates and evidence for expected collection. A sale described as “overseas” may be invoiced in home currency, yet still have operating exposure because customers, competitors or imported inputs respond to exchange rates. Conversely, a foreign-currency invoice gives a transaction exposure even if the seller has no foreign subsidiary. A consolidated translation amount is another possible reporting exposure; it is not automatically a remittable balance.

For interest, follow outstanding principal, reset dates, reference definitions, spread changes, floors, caps and accrual conventions. A shock after a coupon has already been fixed can affect later coupons without changing that first payment. For commodity-linked activity, follow physical quantities, the price reference, local basis or quality adjustment, contractual pass-through and the date on which the price becomes fixed. Include the operating response where price changes alter demand, sourcing or output. A price sensitivity holding quantity constant answers a narrower question than a forecast allowing those responses.

Trace the routes through which non-market events change the same account. A customer delay changes cash timing even when the claim remains valid. A default may change both expected recovery and the time to obtain it. A counterparty can owe a favorable derivative payment just when it becomes least able to pay. A financing line can become less drawable when collateral loses value. These effects belong in the scenario that produces them; listing credit and liquidity risks separately is insufficient if the proposed offset relies on both counterparties performing together.

A compact working account can therefore identify, for each material contribution, its party and position, amount-setting factors, performance conditions, relevant dates, outcome affected and existing protection. That is enough when it permits reconstruction of the calculation. When an input is disputed, return to the actual source account or specialist contribution rather than hide the uncertainty in a general risk allowance.



#### FIN.13:4.3 - Measure a change on stated grounds


For a fixed net foreign receipt Q and exchange rate S measured as home units per foreign unit, its home amount is Q × S. Holding Q fixed, the change is Q × (S1 − S0). Reverse the direction for a net payment. Write the quotation convention next to the calculation: using foreign units per home unit would require division and changes the numerical sensitivity. Distinguish a valuation translation rate from the executable buying or selling price, spread and charges needed for an actual conversion.

When volume also changes, calculate the whole amount in each case: Q1 × S1 − Q0 × S0. One exact explanation of that difference is Q0 × (S1 − S0) + S0 × (Q1 − Q0) + (Q1 − Q0) × (S1 − S0). The last term is the interaction. Omitting it can matter for a large combined move. This decomposition explains the result; it does not establish which scenario or probability is credible. The operating forecast must supply the quantity response.

For a simple floating payment with principal N, annual rate r and applicable year fraction a, interest is N × r × a. Apply a rate change only to the principal and periods it can actually reset. If the reference is averaged or compounded, if principal amortizes, or if a floor binds, use that payment rule rather than multiply all debt by one annual shock. Net interest sensitivity can be calculated with similarly exposed deposits, but the cash uses and access constraints of those deposits still matter.

For market value, a sensitivity such as duration or an option's delta describes a local response under its stated model and units. Use the applicable valuation guidance in FIN.5, FIN.7 and FIN.8 when a new value is needed. A first-order estimate is useful for screening small changes; it can fail near an exercise threshold, over a large move or when several factors change together. Revalue the actual position in those cases. The market value of a guarantee is also different from the amount the guarantor may have to pay in a specified event.

Make the direction and units legible before presenting a total. A one-percentage-point rate rise is 0.01 in the interest formula. A sensitivity quoted per basis point uses 0.0001. A home-currency value change and an amount of foreign currency to deliver cannot be added until the receiving measure and conversion basis make that addition meaningful.



#### FIN.13:4.4 - Choose the source of an uncertain response


A payment rule can determine how a known amount changes with a rate. An operating account can calculate the cash consequence of specified prices, quantities and collection dates. When the missing input is how customers, competitors or suppliers will respond, first decide what could support that estimate. FIN.4 and MA.5 propagate an operating response through the account; their arithmetic does not establish the response itself.

A company estimate uses observations from its own business. Choose data for the required outcome and horizon: next-quarter home-currency operating cash, for example, rather than annual share-price returns. Define the factor change, quotation and units, observation frequency and any delay between the factor and the cash response. Recover the business mix, prices, volumes and protection in force during those observations. A model fitted to net cash after an existing hedge cannot be treated as an unhedged response and then have that same hedge deducted again.

For an estimated relation such as change in cash = a + b × exchange-rate change + other modeled contributions, b describes the response on that model's grounds. A fitted association alone does not establish the effect of deliberately changing prices, suppliers or protection. Identify other changes that could account for the association and the operating mechanism that makes its use plausible. A business with little variation in the relevant factor may provide little information about b even with a long record. Select the simplest estimation that can answer the receiving question, obtaining the needed statistical contribution when its support is beyond the available preparation.

Assess errors as well as the fitted coefficient. Examine the differences between observed and predicted outcomes across time, factor values and relevant business changes; a high fit statistic alone can hide a systematic miss. Serial dependence, a changed regime or a few influential observations can make ordinary uncertainty estimates misleading. Compare later observations not used for fitting where the available history permits it, with information restricted to what would have been available at the prediction date. Retain both uncertainty about the response and unexplained outcome variation when the decision needs a range of future cash. An imprecise estimated effect is not evidence of zero exposure.

A sector or comparable-business estimate can supply information that the corporation's own history lacks. Establish the match before transfer: outcome, horizon, factor definition, products, geography, pricing behavior, funding and existing protection. Build current business contributions in compatible units; value weights do not automatically aggregate cash sensitivities. A larger sector sample can still give a poor estimate for a particular corporation. Reconcile competing company and sector estimates through the differences that could change action rather than average them solely because both are available.

When neither estimate supports the intended reliance, retain conditional operating scenarios with explicit response assumptions. Vary the uncertain input far enough to locate the decision-changing threshold, without labeling the range a confidence interval or attaching unsupported probabilities. Return the precise missing contribution—for example, next-quarter collection and volume response to a stated currency move under the current sales terms—and why it matters. If all supported alternatives lead to the same permitted action, further estimation may add little; if they lead to different actions, FIN.14 compares the attainable responses on those unresolved grounds. Known contractual contributions remain usable while that narrower uncertainty is investigated.



#### FIN.13:4.5 - Distinguish an economic offset from a usable payment


Combine contributions on the same outcome and scenario before deciding how much remains exposed. An exporter receiving a foreign currency and an importer paying it can offset part of their market sensitivity. That useful observation does not establish that the importing entity can obtain the exporter's money in time. Preserve any transfer, tax, restriction or timing condition that can defeat the proposed use; FDM.2 and FIN.2 supply the corresponding entity and dated-cash work.

Keep gross legs when a supplier, bank or settlement system still requires them. Contractual net settlement can change the required payment, but only for the covered parties, currencies, dates and obligations under an effective arrangement. A favorable derivative value can offset a business loss economically while its payment arrives after the business needs money.

Examine protection already in place before recommending more. Map each hedge to the exposure it is intended to change, including quantity and date. A single receipt cannot be assigned in full to both a supplier-payment offset and delivery under a forward. If two analyses use the same cash, reconcile the combined account. The unprotected position is obtained after applying actual available offsets, not by subtracting every contract labeled “hedge”.

Keep counterparty exposure separate from the market sensitivity being hedged. The cost of replacing a favorable unsettled trade, the principal at risk after an irrevocable payment, and the cash needed when a promised receipt is late answer different questions. Their durations and possible losses need not equal the derivative's notional or current value. FIN.15 examines the actual settlement route; its conditions can therefore change this exposure account.



#### FIN.13:4.6 - Build combined scenarios and use probabilities only for the claim they support


Select scenarios from the ways the corporation's outcome can change. Begin with individual drivers where they clarify the mechanism, then combine changes that can interact: rates and debt resets, exchange rates and collection, commodity prices and quantities, collateral values and drawable finance. Recalculate the account under each combination. Do not sum separately calculated “worst losses” as if their assumptions necessarily coexist, or rely on historical diversification after the scenario removes its operating cause.

A scenario is a conditional account, not a forecast merely because it has precise numbers. Separate an illustrative stress, a plausible planning case and a probability-weighted estimate. For a historical replay, apply the selected past changes to today's positions and terms; yesterday's portfolio loss is not today's exposure. For a hypothetical stress, explain the changed drivers and why the combination is useful for this decision. To find a failure threshold, work backward from the unacceptable cash, value or permission result and solve for changes that would reach it; then examine their plausibility and available responses.

If the use requires a loss distribution, name its baseline, horizon, units and model. Generate losses by applying each modeled factor state to the same positions, including the nonlinear and performance conditions that matter, and attach supported probabilities. A historical sample uses an explicit observation window; a parameter model or simulation needs its distribution, dependence and calibration grounds. More simulated observations reduce sampling noise within the model; they do not validate its missing events or its dependence assumptions.

An expected loss averages those losses. A chosen percentile locates a tail boundary. A tail average describes losses within a specified tail. None is the maximum possible loss, the cash needed at every earlier date or a decision rule without an associated tolerance. Where probabilities are poorly supported, retain conditional scenarios and thresholds instead of assigning invented confidence. A richer statistical model is useful only when its additional grounds improve the receiving decision.

Check whether the measure could miss a consequential failure outside its selected dimensions. Low market volatility can coexist with a single-customer default, inaccessible group cash or an untested settlement route. A market-value model generally needs a separate dated-cash return before it can support a funding conclusion. FIN.2 supplies that return without requiring the exposure model to become the corporation's entire cash forecast.



#### FIN.13:4.7 - Return an exposure that someone can act on


State the material driver, the position it changes, the consequence and the conditions on which the calculation depends. Return gross obligations and credible offsets where their distinction affects action. Show the normal comparison, the action-changing adverse case and the residual uncertainty at the grain the receiving decision needs. An unexplained aggregate risk number leaves the next practitioner unable to tell whether to change a commercial term, obtain credit protection, arrange cash or buy a price hedge.

FIN.14 uses the specified outcome and residual exposure to compare protection. FIN.2 uses the dated flows and support conditions to assess funding. FIN.3 can reconsider payment terms, while FIN.10 can reconsider financing whose reset or maturity creates the exposure. If the present issue is an actual failed or uncertain settlement, FIN.15's supported effect account comes first; rerunning an old market sensitivity will not establish what was paid.

Reopen the affected calculation when amounts, operating behavior, counterparties, contract terms or the decision horizon change. An unchanged calculation remains usable where those grounds still fit. Monitoring under FIN.17 follows the inputs and conditions that could change action, such as a missed collection, a reset or a collateral threshold.

### FIN.13:5 - Archetypal Grounding

A constructed corporation expects 100 foreign units from a customer and owes 60 foreign units to a supplier on the same day. If both pay in full, the net economic receipt is 40. A home-per-foreign exchange rate moving from 0.90 to 0.80 changes its home value from 36 to 32, a loss of 4. If the customer instead pays only 30 before the supplier's cutoff, the corporation must obtain 30 foreign units to pay the supplier then. The original net receipt of 40 did not establish payment capacity. If the remaining customer claim of 70 persists under the agreement, retain it separately from that immediate shortage.



#### FIN.13:5.1 - From a fixed invoice sensitivity to operating exposure


In a separate constructed export plan, all sales and costs settle at the end of the period. The business sells 100 units at 2 foreign units each and incurs 1 home unit of cash cost per unit. There are no other flows or tax effects. At 0.90 home per foreign unit, the net operating cash contribution is 100 × 2 × 0.90 − 100 = 80.

If quantity and the foreign price remain fixed while the exchange rate falls to 0.80, the contribution becomes 60. The transaction-price sensitivity is a loss of 20. That result follows from the foreign receipt of 200; it does not establish that demand and pricing will remain unchanged.

Suppose the actual operating scenario instead supports a foreign price of 1.90, sales of 110 units and the same home cost per unit. At 0.80, receipts are 110 × 1.90 × 0.80 = 167.20, costs are 110 and the contribution is 57.20. The loss relative to the first plan is 22.80. FIN.4 carries the supplied operating changes into the account; FIN.13 identifies why the invoice-only sensitivity missed their combined effect. If collection is delayed, this end-period contribution must also be returned to FIN.2 on the changed dates.



#### FIN.13:5.2 - A changed business can invalidate an apparently useful estimate


In a constructed next-quarter cash decision, a corporation has an established empirical model from its former export business. Its data describe quarterly home-currency operating cash, and the estimate was useful while the same products, collection terms and protection remained in place. It has now acquired an import operation. Applying the old company coefficient to the enlarged business would omit the new purchase exposure. A proposed sector substitute measures annual changes in market value; its outcome and horizon do not supply the needed quarterly cash response.

The current operating account instead identifies foreign receipts of 200 and payments of 50 for the retained business, and foreign purchases of 100 for the acquired operation. These quantities are fixed in the case and all settle next quarter. At a home-per-foreign rate rising from 1.00 to 1.10, the retained business's cash change is +15 and the acquired operation's is −10, giving +5 before any further demand or collection response. The agreed baseline for total quarterly operating cash is 40 and already includes those flows at 1.00; no other fixed flow changes.

The remaining uncertainty is the acquired operation's net cash response when it changes selling prices and customers change their purchases. The fixed foreign purchases above are already included; the additional response must not count their cost again. The available commercial evidence supports examining no further cash reduction and a reduction of 8 after the price, volume and collection effects, but supplies no probability or reliable fitted coefficient for that new market situation. These conditional accounts give 45 and 37. A requirement for at least 39 of operating cash is met in the first and missed by 2 in the second.

Use the current contractual account and carry that unresolved sales response into the comparison of attainable protection or funding. Request evidence about the affected product's next-quarter volumes, margins and collection on the proposed price terms if it could change the selected action. A supported matching estimate can later replace the conditional input; neither the historical company fit nor the mismatched sector estimate presently settles it.



#### FIN.13:5.3 - A rate shock acts at resets, not on every reported balance


A constructed borrower has debt principal 100 and a deposit of 40 throughout two quarters. Each quarter has an accrual fraction of 0.25. Debt pays the reference plus 2 percentage points; the deposit pays that same reference minus 1 percentage point. Both first-quarter rates are already fixed using a reference of 4%. The second-quarter reference is uncertain. There are no floors, principal changes or other charges in this case.

At a second-quarter reference of 4%, debt interest is 1.50 in each quarter and deposit interest is 0.30 in each quarter, for net six-month interest cost 2.40. At a second-quarter reference of 6%, the first quarter stays unchanged, while second-quarter debt interest is 2 and deposit interest is 0.50. Net cost becomes 2.70, an increase of 0.30.

If the deposit instead keeps its existing rate through the second quarter, the debt's extra 0.50 has no deposit offset then. Net cost becomes 2.90. Treating the deposit and loan notionals as one permanently floating balance would miss the reset difference. If the deposit is restricted, even the original economic offset does not establish that its cash can service the debt.



#### FIN.13:5.4 - A percentile leaves both a tail and a funding question


For a constructed one-period loss distribution, loss is 0 with probability 90%, 10 with probability 8% and 40 with probability 2%. Define the 95th-percentile loss as the smallest amount with cumulative probability at least 95%. It is 10: cumulative probability is 90% at 0 and 98% at 10. Expected loss is 0.90 × 0 + 0.08 × 10 + 0.02 × 40 = 1.60.

The largest loss within these three modeled cases is 40, and the 95th percentile does not remove its 2% probability. Averaging the worst 5% of this distribution gives (0.03 × 10 + 0.02 × 40) / 0.05 = 22. Because the distribution has discrete probabilities, that tail average includes part of the probability mass at 10; averaging only losses strictly greater than 10 would instead give 40 and answer a different question.

These are three summaries of the same stipulated model. Its probabilities require evidence before actual reliance, and unmodeled outcomes can exceed 40. If a case also requires cash collateral before its final gain or loss is realized, neither the expected loss 1.60 nor the percentile 10 supplies the intervening funds. Return the actual payment sequence to FIN.2.

### FIN.13:6 - Bias-Annotation

Historical correlations may fail when liquidity is most scarce. An aggregate group view can omit local access constraints. A favorable expected receipt can conceal a concentrated counterparty obligation.

### FIN.13:7 - Conformance Checklist

Is the measured outcome, entity, horizon and unit clear? Can the sensitivity be traced to actual terms or operations? Are offsets usable for the claimed purpose? Do material timing, credit and nonlinear scenarios survive the aggregation?

### FIN.13:8 - Common Anti-Patterns and How to Avoid Them

Treating a notional as value at risk conflates amount and sensitivity; calculate the consequence. Netting across dates can remove an actual cash gap; retain the payment timeline. Calling a quantile a worst-case bound overstates its claim; keep the modeled tail limitation.

### FIN.13:9 - Consequences

The corporation can decide which exposure needs protection, funding or acceptance. The account may show that a liquidity or credit action matters more than reducing a headline market-risk number.

### FIN.13:10 - Architectural Rationale

Exposure begins with what changes for the corporation. Separating sensitivity, collection and settlement makes measures useful for action.

### FIN.13:11 - SoTA-Echoing

The [AFP treasury specification][AFP] includes market, credit, counterparty and liquidity risk within treasury practice. The [CFA contingent-claims reading][CFA-OPTIONS] explains the limits of local option sensitivities. FIN.13 combines those concerns with actual payment conditions rather than accepting notional or aggregate net exposure as a complete answer.

The public [CFA market-risk reading, 2026][CFA-MARKET-RISK] distinguishes sensitivity, scenario and distribution measures and their limits. FIN.13 adapts that distinction to corporate cash, operating and claim consequences rather than treating a portfolio loss measure as a complete corporate risk account. Its operating and reset cases show why factor, quantity and date rules matter; its discrete-tail case qualifies the reported statistic. The public introduction and summary are the source scope used here, not the restricted full reading.

Damodaran's historical [risk-profiling treatment][DAM-RISK] develops company-history and sector estimates and exposes their sensitivity to changing business composition. FIN.13 uses that choice with an outcome and horizon match; it does not infer an absence of risk from an insignificant estimate or assume that a sector average always transfers. The [NIST model-validation discussion][NIST-MODEL] and its connected error diagnostics support examining residual structure and uncertainty. Those statistical checks do not establish the corporation's future operating response.

### FIN.13:12 - Relations

FIN.2 assesses cash consequences, FIN.14 compares protection and FIN.15 handles actual performance. FIN.4 and [FDM][FDM] supply missing projections and position meanings. FIN.17 updates exposures whose grounds have changed.

### FIN.13:End
