## FIN.6 - Value Capital Projects

**Type:** Method

**Status:** Stable

### FIN.6:0 - Use this when

The corporation can invest in a project and needs to know what it adds relative to the relevant alternative. Construct incremental project cash and value it on matching grounds. If sufficient cash flows and discount factors are already supplied, start with the NPV calculation. Competition for scarce capital among several projects uses the result in FIN.9.

### FIN.6:1 - Problem frame

The analyst values a specified project alternative against a feasible baseline. Familiarity with financial statements, compounding and present value is assumed; the construction below supplies the project-specific cash-flow choices. FIN.4 provides missing projections and reconciliations.

The result is a financial assessment of incremental consequences. Operating feasibility, available funding and authorization require their own grounds.

### FIN.6:2 - Problem

Accounting return, payback and gross revenue can favor a project whose incremental value is negative. A project account can omit value lost elsewhere in the corporation, treat a past expense as a future payment, or assume that working capital and assets turn back into cash merely because the forecast ends.

### FIN.6:3 - Forces

Capture consequential cash effects without building an unnecessarily detailed model. Compare value over time while exposing uncertainty, strategic dependencies and limited funding.

### FIN.6:4 - Solution

1. **Choose the comparison.** Specify the project and a feasible baseline: continue, replace, defer, stop or another actual alternative. Compare both over dates that include their material consequences. Obtain adequate operating quantities, capacity and service consequences; a technically impossible plan has no actionable investment value.
2. **Construct the difference in cash.** For each alternative, project the receipts, operating payments, taxes, investment and ending consequences at their expected dates. Use the construction below when an account supplies earnings rather than cash. Subtract baseline cash from project-alternative cash at each date. Include effects elsewhere in the corporation, including displaced business and the best feasible use of a resource committed to this project.
3. **Match the claim and financing basis.** For an operating valuation, use after-tax cash before financing flows with FIN.5's matched valuation basis. Do not subtract new borrowing's interest and principal from cash discounted at WACC. A finite debt schedule may instead require FIN.5's separately valued financing effects. For an equity valuation, include new borrowing and subtract debt service and other prior-claim payments, with the actual financing-related tax change, then use the corresponding equity return.
4. **Value the dated difference.** NPV is the sum of incremental cash multiplied by factors bringing it to the valuation date. With a constant annual rate r, a flow CF at year t has present value CF/(1+r)^t; include the initial outlay at t = 0. Use date-specific factors when irregular timing matters. When components need different risk bases, value them on their matched grounds before combining value differences. Separate disposal and runoff from continued operation; obtain a supported continuing value from FIN.7 when activity remains beyond the forecast.
5. **Find what can change the answer.** Solve for a decision-changing input or examine an adverse case. A sensitivity changes one assumption; a scenario combines mutually consistent changes. Rebuild affected taxes, working capital, ending effects and, when risk or financing changes, the discount basis. Use probabilities only when they support the intended expected-value claim. A supported range that crosses the decision threshold leaves the recommendation conditional.
6. **Use supplementary measures for their own questions.** IRR solves for a rate that makes NPV zero; payback locates recovery of the initial outlay. IRR can misrank mutually exclusive projects of different scale or timing and can be multiple or absent for unusual cash-flow signs. Ordinary payback omits time value and flows after recovery; discounted payback still omits later value. Accounting measures answer an earnings question.
7. **Return the value and its conditions.** Include the baseline, cash and return basis, and the threshold or uncertainty that changes the recommendation. Obtain valuable exercisable flexibility through FIN.8 and interactions or capital rationing through FIN.9 when material. FIN.2 separately tests whether the payments can be funded.



#### FIN.6:4.1 - Construct the project cash account


Start with the decision the corporation can still change. A past irrecoverable study cost cancels from the comparison. Its future tax effect also cancels if both alternatives obtain it; retain a refund, deduction or other future consequence that differs. An allocated overhead cancels only when taking the project leaves the actual resource commitment unchanged. For cannibalized business, subtract the contribution lost after avoided costs, not automatically its gross revenue. For a resource with another feasible use, include the cash forgone under that use. A with/without projection already containing that loss needs no second opportunity-cost charge.

A compact bridge is available when the account's only noncash charge is depreciation and the relevant taxable income is taxed at a fully usable rate τ in the same period:

FCF_t = (R_t − C_t − Dep_t) × (1−τ) + Dep_t − Capex_t − (NWC_t − NWC_(t−1)).

Apply it to each alternative and subtract their resulting flows. R and C are period revenue and operating cost before depreciation, Dep is the tax depreciation used in this simplified account, and Capex is the dated capital payment. NWC is the operating receivables and inventory less operating payables used in the projection; cash, debt and tax balances are outside this bridge. Its change is over time within one alternative, distinct from the comparison between alternatives. If other operating balances matter, include their cash effects explicitly.

Depreciation reduces the tax base but is added back because it is not another payment for the asset. If tax depreciation, deductible costs, losses or payment dates differ from the shortcut's assumptions, replace the formula's tax charge with the actual unlevered cash-tax schedule. Obtain the applicable tax treatment and use deductions only when the corporation can realize them. Capital and working-capital payments occur when needed, including before operations begin. A direct receipt/payment forecast that already includes collections and supplier settlements needs no additional working-capital subtraction.

At a finite ending, estimate realizable asset-sale proceeds, their taxes, recoverable working capital, and closure payments. Include only recovery supported by the runoff: an uncollectible receivable is not a terminal receipt. If the activity continues, its continuing value needs the investment and working capital that sustain it. Do not also liquidate those same continuing assets in a separate terminal inflow.



#### FIN.6:4.2 - Make the baseline and project boundary economic


The relevant comparison is what would happen with the action versus the attainable continuation without it. “Without” need not mean unchanged sales forever. Competitor entry, asset wear, contractual commitments and maintenance can change the baseline even if the corporation takes no new initiative. A product launch should bear the loss of existing contribution it actually causes, rather than every decline that would have occurred anyway.

Use operating evidence to establish those effects. A new machine may reduce scrap, require retraining and cause a shutdown before it produces savings. Include each consequence at the time it changes money. A proposed productivity improvement is not a realized saving until the forecast explains which resource commitment, purchasing or opportunity changes. If staff time is freed but payroll and other feasible uses do not change, an allocated labor saving is not yet an incremental receipt. The operating account can still show a useful capacity gain; FIN.9 considers the value of its attainable uses.

For a scarce resource, compare its feasible alternative use. Cash obtainable from selling an asset, rent from an available tenant and contribution from another use are different alternatives, not charges to stack together. Choose the relevant forgone continuation and include it once. If a with/without account already includes the alternative's lost cash, do not subtract another imputed rental or sale amount. A resource with no attainable alternative can have a low immediate opportunity cost even when its historical purchase price was high.

Specify the smallest project boundary that captures consequential dependencies. Infrastructure needed by several products may require a combined investment comparison; charging its whole cost to the first proposal and ignoring the later uses can misstate the choice. Conversely, calling all hoped-for later projects part of the first one can credit benefits without their investment or feasible access. FIN.9 compares the whole combination, and FIN.8 tests the contingent later opportunity and its acquisition route.

Keep the timing of the decision visible. A study already paid for can be irrelevant to the next commitment while remaining relevant to whether the corporation's whole development program is worthwhile. Ignore the sunk payment in the forward choice, but do not erase it from learning about that earlier policy. A cancellation fee, recoverable deposit or future tax consequence can still differ now even though the associated contract or expenditure began earlier.



#### FIN.6:4.3 - Treat working capital, replacement and endings as dated consequences


Working capital often has to be provided before the sales it supports. Establish the required inventory, credit sales and supplier terms, then forecast balances and their cash movements through FIN.4. For each alternative, calculate the change over time; only afterward take the difference between alternatives. A continuing increase in sales can require continuing investment in receivables and inventory, so a cash margin alone does not represent all money distributable.

At startup, distinguish amounts already tied up under the baseline from extra amounts caused by the project. At shutdown, model the actual collection and settlement process. Recovering inventory, receivables and deposits can take several periods and incur losses or tax. Settling payables and closure obligations can require cash after sales stop. A terminal line equal to the opening working-capital investment is justified only when that amount is actually recoverable under the case conditions.

A replacement decision includes the old asset's attainable continuation and the new asset's installation, service and disposal consequences. The old purchase cost is sunk, but sale proceeds, a changed tax payment, avoided maintenance or remaining service can matter now. An accounting write-off alone is not a cash payment; its actual tax or contractual effects may be. FIN.9 compares unequal service lives and available replacements when those choices are live.

When operations continue beyond the explicit forecast, value the continuing activity through FIN.7. That activity must retain the capital and working capital needed for its cash production. A liquidation recovery and a going-concern terminal value are alternative treatments of the same resources unless the valued activity explicitly excludes the assets being sold. Make the boundary clear before adding either amount.



#### FIN.6:4.4 - Interpret NPV and competing measures


NPV expresses the change in value at the comparison date after compensating capital at the matched opportunity cost. A positive NPV supports taking the project over its stated baseline on that financial basis. It does not prove that the project is the best of all mutually exclusive choices, that the cash can be raised, or that unmodeled obligations are satisfied. Those questions can require FIN.9, FIN.2 or the responsible practice.

Values can be added when the components' cash, interactions, claims and pricing grounds have been made compatible. The same is not true of IRRs: a percentage discards the scale of the value increment. A small high-percentage project can contribute less total value than a larger lower-percentage one, while limited capital can make a combination preferable to either ranking. Use the actual alternative cash and constraints.

For the conventional pattern of one initial outlay followed by nonnegative receipts, an economically relevant IRR can summarize the break-even constant rate. With later cleanup payments, additional investment or financing-like flows, the NPV profile need not decline monotonically with the rate. Several roots, or no useful root, may exist. Compute NPV at the warranted pricing basis and inspect the profile if the rate dependence matters; selecting the root that gives a favorable recommendation has no economic justification.

Ordinary payback accumulates undiscounted receipts until the initial outlay is recovered. Discounted payback uses discounted flows but still stops counting later consequences. These measures can communicate capital exposure or a management recovery requirement. Neither establishes full value, and a project can recover quickly before incurring a major closure cost. If an actual constraint concerns payments by a date, use the dated liquidity and financing account rather than assuming a payback cutoff supplies it.

A modified return measure needs explicit financing and reinvestment assumptions. It may be useful for communication, but it does not create those opportunities or supersede the underlying value comparison. Computing NPV itself does not require the corporation actually to reinvest each intermediate receipt at the discount rate. Reinvestment opportunities become explicit alternatives when they are part of the decision; a chosen terminal-wealth calculation must state its own assumptions.



#### FIN.6:4.5 - Adapt the evaluation when uncertain facts or later choices matter


First identify what could change the cash or chosen alternative: price, volume, capacity, the feasible baseline, construction delay, investment cost, tax use or financing policy. A break-even calculation asks how far a specified input can move before the comparison changes. It does not state the probability of that movement. For an input related to other drivers, recompute their consequences in a coherent scenario rather than holding a physically incompatible combination fixed.

Distinguish a probability-weighted expected value from the NPV of a central planning case. FIN.4 explains why nonlinear capacity costs and timing can make them differ. A scenario can be useful without probability weights, but its existence alone cannot support an expected-return conclusion. More simulated trials reduce numerical sampling error in a stated model; they do not validate its causal relations or input distributions.

Ask which decisions remain available after information arrives. A fixed plan that continues investing after failure is different from a stage-gated plan that can stop. FIN.8 constructs the latter using only information available at each decision. Do not credit its avoided losses to a fixed project forecast and then add the option's full value again. The project result should identify whether it already contains the adaptive policy.

Separate uncertainty that can be reduced in time from uncertainty that must be borne. A test is worth considering when it could change an important commitment and its expected decision gain exceeds its cost and delay on supported grounds; C.11.DUA supplies the inquiry comparison. If information cannot arrive before commitment, report a conditional range or compare a feasible smaller or delayed action instead of assuming future knowledge today.

Return the substantive reason for the comparison, not just its sign: the baseline it beats, the cash effects that drive the gain, the threshold that could reverse it and the actionable limitation. In the worked case, the room's obtainable rent changes the opportunity cost and reverses NPV without changing project sales. That is an economic revision to the choice; changing only the spreadsheet's discount rate would obscure it.

### FIN.6:5 - Archetypal Grounding

**With qualified supplied flows.** A constructed project pays 1,000 now and receives 600 at the end of each of the next two years. These are complete incremental after-tax operating cash flows; no terminal value remains. At a matching annual rate of 10%, NPV = −1,000 + 600/1.10 + 600/1.10² = 41.32. Equal annual receipts of 576.19 would give zero NPV. At a required return of 15%, the same 600 receipts give −24.57. Thus the result supports the project on the stated 10% basis, and the relevant return assumption can reverse it. The 41.32 is a value estimate; it does not supply the initial 1,000.

**Construct the flows from the alternatives.** A separate constructed two-year project requires equipment costing 900 and operating working capital of 100 now. The baseline continues the existing business and rents the available room for 40 per year. The project uses that room, generates annual revenue 1,100 and incurs operating costs 400. It also reduces the existing business's annual contribution after avoided costs by 60. There are no other operating changes. A study costing 30 was paid already and has no differing future tax effect; allocated headquarters expense of 50 per year would be incurred under either alternative.

Assume nominal amounts, a matched supplied annual return of 10%, and no debt. All operating receipts, payments and taxes occur at each year end; the initial working capital stays at 100 until its complete cash recovery at year 2. Under the stipulated tax rules, all the relevant income and deductions use 25% in the same year, tax depreciation is 450 each year, and no other noncash charge exists. At year 2, equipment with zero tax basis sells for 100, taxable in full, and closure costs 20 are deductible and paid.

| Incremental cash construction | Now | End of year 1 | End of year 2 |
| --- | ---: | ---: | ---: |
| Operating margin before depreciation: 1,100 − 400 − 60 − 40 | 0 | 600 | 600 |
| Cash tax on that margin after depreciation: (600 − 450) × 25% | 0 | −37.50 | −37.50 |
| Equipment payment | −900 | 0 | 0 |
| Working-capital investment and recovery | −100 | 0 | +100 |
| Equipment sale after tax: 100 − 25 | 0 | 0 | +75 |
| Closure payment after tax: −20 + 5 | 0 | 0 | −15 |
| Incremental free cash flow | −1,000 | +562.50 | +722.50 |

The annual operating cash can also be recovered as taxable operating income 150 × 75% + depreciation 450 = 562.50. The 900 equipment payment is counted once; the 30 study and unchanged 50 allocation cancel. At 10%, NPV = −1,000 + 562.50/1.10 + 722.50/1.10² = **108.47**.

**Change the baseline.** A credible alternative tenant offers 150 per year instead of 40. Holding the other case grounds fixed, the extra forgone rent is 110 before tax, or 82.50 after tax each year. The revised flows are −1,000, +480, +640 and NPV is **−34.71**. The rent that makes the project indifferent to this baseline is 40 + 108.471074/[0.75 × (1/1.10 + 1/1.10²)] = **123.33 per year**. If the obtainable rent is unresolved across that threshold, obtain firmer terms or give a conditional comparison. The tax and timing assumptions are part of that threshold.

### FIN.6:6 - Bias-Annotation

Sponsor forecasts may overstate demand or understate implementation loss. An apparently conservative sensitivity can still omit a correlated adverse scenario. Keep operating evidence and the selected baseline visible.

### FIN.6:7 - Conformance Checklist

Can the reader rebuild both alternatives and their dated cash difference? Are opportunity cost, working capital, tax and terminal effects handled once? Do the cash and discount bases match? Is any claimed flexibility feasible, and is funding distinguished from positive NPV?

### FIN.6:8 - Common Anti-Patterns and How to Avoid Them

Charging an unchanged allocated overhead as incremental cost can reject a useful project; recover the resource effect. Ignoring cannibalized contribution can overvalue it; include the lost alternative cash. Choosing by highest IRR alone can discard more valuable feasible capital uses; compare their NPV and constraints.

### FIN.6:9 - Consequences

The result shows whether the project adds financial value on stated grounds and what changes the answer. The analyst can complete this valuation while funding for the initial investment or the project's operating feasibility remains unresolved. Building the two alternatives takes more work than discounting a supplied series; stop rebuilding when the supplied incremental series is sufficient.

### FIN.6:10 - Architectural Rationale

The difference between alternatives identifies what the present choice changes. The earnings-to-cash bridge locates payment and tax effects; discounting then compares their value across dates. Keeping these operations separate makes a wrong baseline or an omitted cash effect visible before a precise NPV disguises it.

A project account is a causal comparison as well as a set of quantities. If the baseline would lose the same customer or incur the same payment, attributing that whole effect to the proposal misstates its contribution. If the proposal changes another product or resource use, restricting the account to the sponsor's cost center loses a real consequence. The economic boundary follows the decision's effects, while FIN.1 preserves the corporation and claimant perspective.

Discounting expresses the value trade-off over time; it does not provide money on the payment date. A precise positive NPV can coexist with an insolvent implementation schedule. Nor does a fixed-project NPV settle whether waiting or making a smaller initial commitment is better. FIN.2, FIN.8 and FIN.9 supply those actual missing comparisons. Additional measures are useful when their own question is explicit, rather than as unexplained votes to be averaged with NPV.

### FIN.6:11 - SoTA-Echoing

The public [CFA 2026 capital-investment overview][CFA-CAPITAL] keeps after-tax cash, effects on the rest of the firm, double counting and real options central to appraisal. [Damodaran's Chapter 5][DAM-PROJECT], particularly its earnings-to-cash explanation and Illustrations 5.4–5.5, is an older developed treatment of input construction and timing. FIN.6 uses that explanatory work alongside the current professional framing; the historical examples do not supply current tax or market facts.

Compared with discounting a sponsor's accounting return or supplied “project cash” without recovering its baseline, this construction exposes displaced cash and ending obligations. The worked baseline change shows when a new opportunity changes the decision. Reopen the value when those grounds, realizable flexibility or the matching return changes.

### FIN.6:12 - Relations

FIN.4 provides missing projections and accounting bridges; FIN.6 constructs the incremental project comparison, and FIN.5 supplies its matched return or financing-effects basis. FIN.7 supplies a needed continuing value. FIN.8 values flexibility; FIN.9 compares interacting uses. [MA][MA] and [OPS][OPS] supply missing resource and feasibility results. FIN.16 returns the financial recommendation.

### FIN.6:End
