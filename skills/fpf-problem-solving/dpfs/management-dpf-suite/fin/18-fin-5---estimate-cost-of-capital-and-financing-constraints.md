## FIN.5 - Estimate Cost of Capital and Financing Constraints

**Type:** Method

**Status:** Stable

### FIN.5:0 - Use this when

A valuation needs a discount rate, or an attractive financing rate is being used as if it were the required return on the whole investment. Match the return estimate to the cash flows and claims being valued. A sufficient externally supplied rate with the right grounds can be used directly. Use the construction below when those grounds are missing or the project's risk or financing differs.

### FIN.5:1 - Problem frame

The analyst estimates the return capital providers require for the claim being valued and identifies relevant financing constraints. Management separately chooses the minimum return it will accept for a project. An obtainable borrowing offer states financing terms; an authorized financing decision permits a specified action.

The calculation needs an understanding of investment returns and present value, and evidence about the market and business being valued. Beta, market premium and financing weights are explained below. Market observations can come from an exchange, a central bank, a data provider or a qualified valuation supplier. Recover their date and definitions, and explain their relevance to the valued claim.

### FIN.5:2 - Problem

Using a cheap loan rate for risky operating cash flows overvalues the project. Using a corporate average for a materially different project hides risk. Nominal, real, pre-tax and after-tax quantities can be combined into a number with no coherent meaning. Even correct arithmetic gives a fragile answer when the inputs' construction is unknown.

### FIN.5:3 - Forces

Use a tractable estimate while respecting uncertainty in market evidence, risk and future financing. Maintain comparability without asserting that all projects or claims have the same cost of capital. More peers or a longer history can add observations while making the business comparison less relevant.

### FIN.5:4 - Solution

1. **Match the claim and the cash flows.** Identify operating cash available to all capital providers, cash available to common equity, or another specified claim. Fix currency, valuation date, timing, inflation and tax basis. FIN.4 supplies the projection; FIN.6 excludes financing payments from the operating cash flows discounted at WACC. Recover the debt policy from the financing terms and supported plan: which amounts are fixed or repaid, and when borrowing is reset to market value. Establish how the resulting interest deductions are used and priced before selecting a beta-transfer model below.

2. **Choose a return model for that use.** One route for equity is CAPM: required equity return = risk-free return + equity beta × market equity premium. Beta measures how the equity return varies with the chosen market's return; it is not the probability of project failure. This model prices exposure to market risk for a diversified investor. Use the fuller construction below when estimating its inputs. A private company may use comparable listed businesses, but concentrated ownership, market access and the valuation's purpose can require another supported return model or valuation adjustment. Establish that basis before adding a “private-company premium”; [CFA's private-company discussion][CFA-PRIVATE] identifies these differing circumstances. If a needed adjustment is unsupported, return a conditional estimate and name the missing evidence.

3. **Estimate a current debt return for comparable borrowing.** Start from current traded debt or obtainable terms with matching currency, maturity, security and priority. Separate the benchmark rate from the credit spread; explain which issuer and financing conditions make that spread relevant. The coupon on an old loan need not be today's borrowing cost. A yield based on promised payments can approximate the required expected return when expected default losses are immaterial; otherwise estimate expected receipts and losses consistently with the valuation model. FIN.10 supplies net proceeds, fees and actual payment terms for an issue comparison. A one-off issue fee belongs in that financing comparison or its explicit valuation effect, rather than silently becoming a perpetual debt spread.

4. **Combine matching returns and financing weights.** For the matched debt-and-common-equity model, WACC = E/(D+E) × required equity return + D/(D+E) × debt return × (1−usable marginal tax rate). E and D are market values of the claims, or a justified prospective market-value mix supplied by FIN.11. For traded equity, price times the relevant share count supplies a starting value. For untraded claims, use FIN.7's valuation for the identified interest or an adequate supplied value; carry a material valuation range into the weights. Other claims require their own weights and treatment. Book amounts are usable proxies only with a reason they approximate the needed values. The tax adjustment requires applicable deductibility, timely usability and the financing/tax-shield model used in the risk transfer.

5. **Value financing under the selected policy.** Use the peer's and project's own policy assumptions in the construction below. A fixed debt amount, a repayment schedule and a repeatedly restored market-value share can require different valuations. For a schedule outside the supported constant-WACC case, use adjusted present value: discount operating cash flows at the unlevered required return, then add the present value of usable financing benefits and subtract financing costs, including relevant distress effects. Calculate the tax savings on the actual debt and deduction schedule; price their risk explicitly. Do not also include those same benefits in an after-tax WACC. The [APV explanation and worked valuation][DAM-APV] develop the separate-effects approach. If weights depend on the resulting value, reconcile those values and weights. FIN.12 supplies the access constraints.

6. **Return a usable estimate and its sensitivity.** Give the rate or range, the claim and cash-flow basis it supports, the relied-on inputs and dates, and the assumptions whose change would alter the decision. Propagate plausible changes into FIN.6–FIN.8's valuation. If they reverse the choice, report that dependence and obtain the missing estimate or compare a conditional action. Keep the estimated investor return, management's chosen project-acceptance minimum and the quoted borrowing offer distinct.



#### FIN.5:4.1 - Understand what the required return represents


Capital committed here cannot simultaneously be used in an available alternative of comparable risk. The required return represents that opportunity cost in the selected valuation model. It is not an extra payment appearing in the operating cash account, a promise that the project will earn that amount, or management's wish for a larger margin of safety. NPV tests whether the projected cash more than compensates for that opportunity cost.

In CAPM, the additional compensation concerns the claim's co-movement with the market opportunity set for a diversified investor. A firm-specific failure can still reduce expected receipts even where that particular risk earns no separate market premium. Model the failure's consequences in expected cash; do not treat “diversifiable” as “cannot lose money.” Conversely, a large spread of possible outcomes does not by itself identify the beta or required premium.

Identify how risk is represented before changing either cash or the rate. Expected cash already includes unfavorable outcomes with their supported probabilities. A market-risk premium applied to those expected flows is not automatically double counting: the expected loss and the price of bearing its covariance risk are different effects. Double counting occurs when the same compensation for risk has already been deducted in a certainty-equivalent cash amount and is charged again through a risk-adjusted rate. A deliberately conservative management scenario is neither automatically an expectation nor a certainty equivalent.

A low borrowing offer does not make operating risk disappear. Lenders and equity holders have different claims on the same business, and a guarantee can shift who bears a loss without eliminating its cost. A subsidy or concession can have value, but identify the resulting financing benefit and its conditions separately. Do not replace the entire project's required return with the subsidized loan's coupon.

The applicable investor and valuation purpose matter. A traded diversified-investor valuation and a particular undiversified owner's reservation value need not use the same risk preferences or model. Identify that change through FIN.1 and obtain the appropriate supported approach. Adding several unexplained premiums for size, private ownership, country and “project uncertainty” can charge overlapping effects without establishing any of them.



#### FIN.5:4.2 - Build the risk-free return and market premium


Obtain a default-free benchmark in the cash-flow currency at the valuation date. Its maturity or term structure should match the cash-flow horizon: a short bill repeatedly rolled over does not fix a long-term return. Where maturity differences matter, use the relevant zero-coupon curve and dated discount factors. A government yield containing material default risk needs an explicit adjustment or another supported benchmark. Real cash flows need a real return basis. [The risk-free-rate explanation][DAM-RF] develops these matching choices.

Choose an equity premium for the same market and benchmark convention. A historical estimate compares equity total returns with the specified risk-free returns over a stated period; the period and averaging convention affect it. An implied estimate solves for the return consistent with the current market price and forecast distributions, then subtracts the matched risk-free return. It depends on the forecast and pricing model. Compare defensible estimates when the choice matters; a historical average is not an observed future premium. [The estimation discussion][DAM-INPUTS] explains the trade-offs.



#### FIN.5:4.3 - Match business exposure to the project


A corporate average is usable for a project only insofar as the valued activity and financing assumptions are comparable. Investigate the economic sources of exposure: what moves demand and prices, which costs can adjust, which payments are fixed, what customers or suppliers concentrate risk, and how contracts or regulation alter the response. A familiar industry label alone does not establish the same exposure.

For a corporation with several activities, use the relevant business contribution rather than the average exposure of unrelated divisions. The bottom-up construction below allows a project without traded equity to use evidence from comparable activities. A new project serving different customers or operating with a materially different cost structure may need its own comparison. Explain the difference before deciding that finer estimation is worthwhile; numerical precision cannot rescue an economically poor peer.

Distinguish the uncertainty of the estimate from the underlying investment risk. An imprecisely estimated beta is a reason to inspect the sample, compare an alternative estimate or carry a range. Raising the central rate merely because the analyst is unsure does not identify the price of the actual risk. A larger peer set can reduce some estimation noise while introducing less comparable activities, and common source errors do not vanish through averaging.

Account for changes in business mix, contract protection and operating conditions over the valued horizon. A past regression can describe exposure that the proposed operation no longer has. In a cross-border activity, currency matching does not by itself settle the risk of customer demand, enforceability, restrictions or transfer of proceeds. Model the relevant operating and payment consequences and obtain an evidenced risk treatment; place of incorporation alone does not determine a universal surcharge.

Retain the economic reason for the chosen estimate so that a changed project can be reassessed. A rate copied without that reason gives the next analyst no way to tell whether a larger plant, a long-term offtake agreement or a different customer group changes the basis.



#### FIN.5:4.4 - Recover business risk before transferring a beta


For a listed comparable business, obtain aligned stock and market total returns, including distributions, for the same periods. Subtract each period's risk-free return to obtain excess returns. If x is market excess return and y is the claim's excess return, estimate beta as Σ[(x−mean x)×(y−mean y)] / Σ[(x−mean x)²]. This is the regression slope. The same calculation can estimate a traded debt claim's beta when suitable return data exist. Alternatively, obtain an estimate with those definitions. Examine the window, market benchmark, infrequent trading and business changes before using it.

Choose peers for their operating exposure and establish the financing policy underlying each estimate. Use financial statements, repayment terms and supported refinancing assumptions to distinguish a fixed amount from a market-value target and its reset dates. Then select the project's forward policy from FIN.10–FIN.11. A matching current D/E ratio alone does not establish a matching policy.

Let a express the financing model's adjustment in the following relations. Two illustrative choices are:

| Financing and tax-shield model | Factor a |
| --- | --- |
| Permanent fixed debt amount; constant usable tax rate t; tax savings have debt risk. | 1−t |
| Debt reset each year to a constant share of market value; constant usable t and debt return kD; the next year's tax savings have debt risk, while later debt resets follow business value. | 1−t×kD/(1+kD) |

The permanent-debt case values its recurring tax savings at t×D. Annual resetting fixes only the coming year's borrowing; subsequent amounts depend on business value. Both models require usable deductions and treatment of additional financing frictions. The examples below stipulate proportional loss-sharing and tax-exempt debt cancellation, with the deductions priced at the expected debt return. With risky debt, verify those loss and tax conditions; another treatment can change the tax-shield discount rate. [The policy derivation, especially equation 11 and footnote 9][ALS-POLICY], explains those conditions. A finite fixed loan does not satisfy the permanent-debt premise; use its dated financing effects in step 5. If the actual policy or shield risk is unsupported, obtain that basis or keep the valuation conditional.

For each peer, remove its financing effect as βU = [βE + βD×a×D/E] / [1 + a×D/E]. Apply the target's own factor and debt estimate as βE = βU + (βU−βD)×a×D/E. Here βU is unlevered business beta, βE equity beta and βD debt beta. Set βD to zero only when negligible debt market risk is a justified approximation.

Combine relevant business estimates only after removing their financing effects. Material excess cash or a different business mix needs separation; revenue weights need not equal business-value weights. Use a supported debt-beta estimate or a range when debt risk matters. [The fuller bottom-up-beta treatment][DAM-BETA] develops peer selection and combination; the policy choice above qualifies its tax-adjusted transfer. Compare the resulting valuations when more than one financing policy remains plausible. An approximation cannot settle the decision when the supported alternatives change its result.



#### FIN.5:4.5 - Use discount factors and financing effects on compatible grounds


A single annual rate is a useful compression only when the valued cash and financing model support it. For deterministic annual forward discount rates r1 through rt, the discount factor to time t is 1/[(1+r1)×...×(1+rt)]. A time-t spot rate zt instead gives 1/(1+zt)^t. Do not treat a quoted spot rate as a one-year forward rate and compound both adjustments. For risky cash, use the corresponding supported pricing factors or model; the risk-free term structure alone does not supply them.

When risk changes over time, identify which remaining claim is exposed to which conditions before selecting its pricing model. A fixed contractual payment, an uncertain operating receipt and an exercisable option can have different risks even when they occur on the same date. Value materially different components on their matched grounds and combine their present values. FIN.8 supplies the changing contingent payoff of an option.

For a certainty-equivalent approach, obtain the amount certain at each date that has the same value as the risky claim, then discount that amount using the matching risk-free factors. The risk adjustment needs a supported model; a discretionary haircut is not enough. For an expected-cash approach, use the required expected-return model that prices those cash flows. Keep the two representations distinct through the calculation.

Do not apply an increasing “risk rate” indiscriminately to unavoidable future costs. A higher positive discount rate reduces the present magnitude of a negative payment and can make an adverse obligation appear cheaper. Establish the payment's own risk and timing. Similarly, a bond yield computed from promised payments includes a different relationship between price, default losses and receipts from a required return computed on expected payments. When losses matter, obtain the expected payment/recovery account and its matching pricing basis rather than transferring the promised yield unchanged.

APV is especially useful when the financing schedule must remain visible. It separates operating value from the usable deductions, subsidies, issue costs and other financing effects that change value. Value each effect once with its own timing and risk. Adding a distress estimate already included through lost customers or recovery flows would count that consequence twice. Omitting such effects merely because a tax-shield calculation is precise would overstate the benefit of borrowing.

Finally propagate a defensible range into the receiving decision. In the worked case below, a tiny rate difference changes the NPV sign. More displayed decimals cannot settle uncertain debt policy or business comparability. Return the rate's grounds and the condition that would change the choice; FIN.11 decides the financing mix and FIN.12 determines what can actually be obtained.

### FIN.5:5 - Archetypal Grounding

**Combining supplied inputs.** All numbers here are constructed. Suppose the supplying analysis has already qualified equity return 9% (3% + beta 1.2×premium 5%), debt return 6%, market equity 60, debt 40 and a usable 25% debt-tax adjustment for the receiving valuation. Their WACC is 0.6×9% + 0.4×6%×0.75 = 7.2%. Holding the returns and weights fixed, removing only that tax adjustment gives 7.8%. These computations combine supplied inputs; constructing them for another business or financing policy requires the following work.

**Constructing a project rate.** Take a peer with equity beta 1.15, debt beta 0.6 and market D/E of 0.5. Stipulate that it maintains a permanent fixed debt amount and that its constant 25% usable tax savings have debt risk. Its factor is therefore 0.75, giving βU = (1.15 + 0.6×0.75×0.5)/(1 + 0.75×0.5) = 1. Assume comparable operating exposure and no material excess cash.

The project instead resets debt each year to 40% of the remaining project's market value, with final repayment at year 2. Assume no additional financing costs in either project policy. Use the annual model's stated tax and loss-treatment assumptions, a flat 3% risk-free curve, market premium 5%, debt beta 0.6 and matched debt return kD = 3% + 0.6×5% = 6%. The factor becomes 1−0.25×0.06/1.06 = 0.985849. With D/E = 40/60, equity beta is 1 + (1−0.6)×0.985849×40/60 = 1.262893, equity return is 9.314465%, and WACC is 7.388679%.

Apply FIN.6 to an investment of 1,000 and expected after-tax operating cash flows of 556 at each of the next two year-ends, before financing payments. NPV at the constructed annual-policy rate is −1,000 + 556/1.07388679 + 556/1.07388679² = −0.13, rounded. The break-even rate is about 7.379143%. Using the earlier supplied 7.2% would give +2.48, but that earlier input does not establish the annual-policy rate for this business. Using the 6% debt return gives +19.37 and prices the wrong claim. The isolated 7.8% sensitivity gives −5.78.

**Changing the financing policy.** The annual-policy valuation implies initial debt of 0.4×999.868382 = 399.947353. Now hold that same amount until final repayment in year 2, instead of resetting it in year 1. Assume the expected tax savings are 0.25×0.06×399.947353 = 5.999210 each year, priced at the debt return under the stipulated tax/loss treatment. The unlevered required return is 3% + 1×5% = 8%. APV is 556/1.08 + 556/1.08² + 5.999210/1.06 + 5.999210/1.06² = 1,002.49. NPV is +2.49. This is a finite schedule calculation; the permanent-debt factor was used only to recover the stipulated peer's business risk. If the project's debt policy is unresolved, these differing signs require a conditional recommendation or resolution of that policy before choosing on value.

**Changing business risk.** Return to annual debt resetting, but use a supported unlevered beta of 1.4 for a more cyclical business. Hold the illustrative debt risk, financing share and other model assumptions fixed. Equity beta becomes 1.925786, equity return 12.628931%, WACC 9.377358%, and NPV −26.92. This adaptation requires the project's operating-risk estimate. An actual leverage change would also reopen the debt estimate. The valuation does not establish funding access or authorize investment.

### FIN.5:6 - Bias-Annotation

Quoted market data may be stale, incomparable or unavailable for a private corporation. A model can conceal judgment in its beta, premium or target leverage. A narrow peer set can be noisy; a broad set can describe the wrong business. Expose action-changing uncertainty instead of reporting extra decimal places.

### FIN.5:7 - Conformance Checklist

Do the claim, currency, inflation, tax and timing bases match? Can another analyst recover how the risk inputs and financing weights were obtained? Does a peer comparison separate operating from financing risk using its own debt policy? Does the target calculation use the target's policy and tax-shield risk? Is the tax benefit usable under the assumed conditions? Do plausible changes alter the valuation or next action? Can the reader distinguish the estimated investor return, management's chosen acceptance minimum and the terms of a borrowing offer?

### FIN.5:8 - Common Anti-Patterns and How to Avoid Them

Using book weights merely because they are easy to find can misstate the relevant financing mix; recover suitable values or qualify the estimate. Adding a risk premium after already making the same risk adjustment to cash flows double-counts it; identify where each effect enters. Copying a peer's equity beta into a differently financed project transfers the peer's financing risk as well as its business exposure.

### FIN.5:9 - Consequences

The valuation has an interpretable rate and sensitivity range. A rate range can support a robust choice or identify the uncertainty on which the choice turns. The analyst can request the particular missing input instead of substituting an unsupported corporate average; financing access still depends on the actual terms and conditions.

### FIN.5:10 - Architectural Rationale

The required return expresses the opportunity cost of committing capital to the valued risk. Equity holders receive what remains after senior claims, so the same business can have different equity risk under different financing. Separating business exposure from financing explains both the peer adjustment and why a low debt return cannot price the whole operation.

The debt policy also determines future deductions. A fixed borrowing amount and an amount reset with business value expose those tax savings to different risks. That is why policy selection precedes beta transfer. WACC is a convenient operating discount rate when its model fits; APV keeps dated financing effects explicit when the fixed-rate representation does not. The choice depends on the financial arrangement and tax basis, not on which calculation gives the preferred NPV.

### FIN.5:11 - SoTA-Echoing

[OpenStax 2e's WACC treatment][OS-WACC] develops the weighted calculation and estimation uncertainty. CFA Institute's public [2026 cost-of-capital discussion][CFA-COST] emphasizes model, financing and tax choices; its [private-company discussion][CFA-PRIVATE] qualifies transfer to another valuation setting. Those public discussions frame the choice.

Damodaran's historical explanations develop [benchmark matching][DAM-RF], [return inputs][DAM-INPUTS], [business-risk transfer][DAM-BETA] and [separate financing effects][DAM-APV]. Arnold, Lahmann and Schwetzler's [2017/2018 analysis][ALS-POLICY] makes the financing-policy condition operational. FIN.5 uses those model distinctions with current application data and the actual tax basis; historical quotations and numerical proxies do not establish them.

### FIN.5:12 - Relations

FIN.4 supplies cash flows; FIN.6–FIN.8 use matching rates. FIN.10 supplies actual financing terms, FIN.11 compares financing mixes, and FIN.12 tests access constraints. FIN.17 refreshes changed inputs; FIN.18 handles a material change in rate-estimation method.

### FIN.5:End
