## FIN.2 - Assess Liquidity and Funding Needs by Date

**Type:** Method

**Status:** Stable

### FIN.2:0 - Use this when

A payment is approaching and a bank balance, profit figure or unused credit limit does not yet tell you whether the corporation can pay. Start with the money and commitments at the relevant dates; obtain a dated funding requirement before selecting a response. A sufficient existing cash forecast can be used directly.

### FIN.2:1 - Problem frame

The treasurer or analyst is preparing a liquidity account for a named paying entity, currency and horizon. This method recovers usable balances and timed flows. It does not itself choose a capital structure, obtain a lender's consent or execute a payment.

### FIN.2:2 - Problem

A corporation can have valuable assets and positive projected earnings while missing tomorrow's payment. Totals hide timing; consolidation can hide restrictions between entities; a facility's headline limit can hide a condition that prevents drawing it.

### FIN.2:3 - Forces

Protect payment continuity without keeping unnecessary idle cash. Retain decision-changing detail without forecasting every immaterial transaction. Separate a contractual amount, an expected receipt and an available balance, while using a common timeline to see their combined effect.

### FIN.2:4 - Solution

1. Choose the paying entity, currencies, payment dates and minimum usable cash required at each date. Include the whole baseline of other receipts and payments. Use daily or intraday intervals around tight dates, even when the remaining horizon is monthly.
2. Reconcile opening bank and cash balances to the usable amount: remove restricted, pledged, trapped or unsettled amounts as the actual arrangements require. Identify an intercompany transfer by its source, permitted route, cost and earliest usable time; common ownership alone supplies none of these.
3. Place material operating payments, collections, taxes, debt service, investments and distributions on the timeline. Distinguish agreed dates from expectations. Keep alternative collection or draw assumptions as scenarios; do not add a hoped-for receipt to a committed one.
4. For each facility, establish the remaining commitment, borrower, currency, expiry, draw conditions, notice period, cutoff, collateral and fees. Count a draw as available only on the scenario whose conditions support it. A revocable indicative line contributes a possible funding alternative, not current cash.
5. Calculate each closing balance as opening usable cash plus usable inflows minus payments. For a required reserve, funding need at a date is the positive amount by which the pre-funding balance falls below that reserve. Solve for the gross draw when fees are withheld; include later interest and repayment.
6. Recalculate the whole timeline with the proposed response. A draw that cures today's gap can create a larger maturity gap. Return the amounts, dates, conditions and affected commitments. Use FIN.3 for working-capital alternatives, FIN.10 for financing terms, or FIN.15 for a selected permitted treasury action.

Stop when the receiving decision can distinguish a funded path from its unresolved conditions. If the right to money or the contract's event behavior is unclear, obtain that specific account through [FDM.1 through FDM.3][FDM]. If profit and cash disagree materially, use FIN.4 and the applicable [MA.4][MA] reconciliation.

If you can perform a calculation but cannot explain how it answers this liquidity question, use [FPF B.1.5.EW][EW] to recover the connection. Identify the financial operation being performed through it, the conditions that make it fit the payment plan, and any constituent know-how or contribution still needed. The example below shows that relation.



#### FIN.2:4.1 - Build the account around the payer and the payment


A liquidity forecast answers whether a particular payer can make particular payments when they become due. Start with the bank and settlement accounts that payer can use. An amount in the accounting cash balance can be pending clearance, pledged, reserved by contract or held by a different company. Record the condition and earliest usable date before treating it as a source. Conversely, an undrawn facility is a possible financing action, not opening cash. Adding its limit to the bank balance and then also adding a draw counts the same support twice.

Use the currency in which the obligation must be settled. If another currency supplies the money, include the conversion transaction, obtainable rate or rate scenario, settlement date and any margin or transfer requirement. A common reporting currency helps compare positions but does not perform that conversion. For a group, first establish the separate payers' accounts and the actual transfers that connect them. A consolidated surplus can coexist with a subsidiary's inability to pay. FDM.1–FDM.2 supply the positions, entity boundary and available support; FIN.2 turns those results into dated funding consequences.

The starting cash is an observed or reconciled usable balance at a stated instant. Construct receipts from invoices, customer terms, expected performance and asset realizations; construct payments from the operating plan, supplier terms, payroll, tax, investment and existing finance. FIN.4 and MA.4 supply the connection to the forecast and accounting views. A sale is not yet a receipt, a purchase is not necessarily paid on delivery, and depreciation is not a payment. When a forecast already starts from operating cash after tax or interest, do not subtract those same payments again.

Separate obligations, expected performance and selectable actions. A receivable due on Tuesday establishes a claim; its collection forecast requires evidence about payment. A proposed loan becomes cash only after its conditions, notice and settlement are satisfied. FDM.3 develops this event logic when the arrangement is unclear. A supplied schedule with these distinctions already resolved can be used directly.



#### FIN.2:4.2 - Choose dates that reveal the decision


Near a threatened payment, use event dates or intervals short enough to expose the lowest balance. A weekly total can hide Monday payroll followed by Friday collections. Include intraday order when a bank cutoff, security settlement or same-day receipt changes whether the payment can occur. A longer operating forecast may use monthly periods, but its aggregated cash cannot settle that shorter question.

Carry the horizon through the proposed remedy's repayments and the operating cycle it finances. A draw can remove this week's shortfall while creating a larger maturity next month. If the decision concerns continuing availability, also inspect the next seasonal low, renewal date and material collateral reset. Stop once the relevant obligation and its material financing consequences are covered, and identify any later dependence.

For each scenario and date, begin with the previous closing balance, add usable receipts and actual financing proceeds, and subtract all payments, financing charges and repayments. Compare the resulting balance with the applicable minimum reserve. The reserve is a requirement or a chosen protection level; keeping it separate from the balance lets a reader distinguish inability to pay from an intended safety margin being consumed. If a model allows a negative balance, that row describes an unmet need unless an actual overdraft arrangement supplies it.



#### FIN.2:4.3 - Derive availability and the gross funding need together


A credit limit is only one constraint on drawing. The available amount may also depend on eligible receivables or inventory, collateral valuations, prior drawings, other uses of the facility and conditions in FIN.12. For a simple asset-backed line, a stipulated rule might permit total drawings up to the smaller of the commitment and a percentage of eligible receivables. Incremental room is that amount less existing drawings and other reserved utilization. Read the actual agreement before using such a formula.

A decline in receivable quality can simultaneously delay collections and reduce the line that was expected to bridge them. Therefore project availability in the same adverse state as the cash shortfall. Holding yesterday's line headroom fixed while stressing receipts breaks the proposed protection. A breach may also affect renewal or draw permission before it changes a contractual maturity.

Size a financing action from its net usable proceeds. If a fixed fee is withheld, add that fee to the cash need before solving for the principal. If a percentage is withheld, divide the required net amount by one minus that percentage. A restricted deposit or compensating balance can absorb further proceeds; its later release belongs at its own date. FIN.10 compares the obtainable instruments and their full costs. Return its selected terms here, then recompute the account including interest and repayment. Continue until the chosen borrowing and the cash account agree; an algebraic solution alone does not establish a lender willing to supply it.



#### FIN.2:4.4 - Set protection from a plausible failure and a timely response


A reserve should answer a concrete exposure: uncertain collections, urgent repairs, margin calls or the time needed to obtain replacement funds. For each relevant adverse state, ask how far the balance can fall before a feasible response takes effect. The required initial protection is the largest shortfall relative to the chosen minimum over those dates, after allowing only responses available in that state. This is a scenario requirement, not a statistical confidence level unless the scenario model supports that interpretation.

Avoid treating all uncertainties as independent when they arise from the same cause. A customer's failure can remove a receipt, reduce collateral eligibility and make a financier less willing to extend credit. Equally, adding every imaginable worst outcome can immobilize money without improving the present decision. Select material states from the operating and financing exposures, explain the protection sought, and show the remaining exposure when a full guarantee is unattainable. A sufficiently supported probability model can estimate shortfall likelihood and magnitude; an average balance still does not prove payment capacity.

Compare the cost of holding or arranging protection with the consequences it prevents. Cash holdings may earn a return but have opportunity cost; committed facilities can charge for unused capacity and still contain conditions. Selling assets quickly may realize less than their ordinary value. These costs belong to the choice of protection, while the dated account establishes whether it works. FIN.5–FIN.6 supply the value comparison when material.



#### FIN.2:4.5 - Change the attainable plan and keep the return visible


If the account fails, construct a remedy that changes a dated receipt, payment or available financing action. Accelerating a customer payment has a price and requires acceptance. Extending a supplier term changes an obligation only when the arrangement permits it. Reducing inventory may undermine delivery and hence later receipts. FIN.3 compares these operating terms; FIN.10 constructs or compares finance; FIN.12 identifies restrictions and remedies. When another entity's cash could help but no adequate transfer or support exists, FIN.23 constructs that financial relation and tests both entities' needs. Return their actual consequences to the same account before relying on the repair.

Include the decision's execution lead time. An asset sale closing after payroll is not a payroll remedy. A loan with enough face amount but an unsatisfied condition is not yet one either. When no attainable plan covers the obligation, state the uncovered date and amount and the action-changing missing condition; FIN.22 becomes relevant if ordinary adjustment is insufficient. A request for consent is not itself consent.

Roll the forecast forward using actual receipts and payments. Explain material deviations as timing, amount, scope or failed action, then revise the remaining account and response. Do not erase the original reason for a borrowing need by relabeling an overdue receipt as collected. For a genuine temporary surplus, preserve access before the next required use: compare maturity, settlement, credit risk and redemption conditions of any proposed placement. The gross bank balance is not automatically available for investment or payout.

### FIN.2:5 - Archetypal Grounding

A constructed order brings 1,200 on day 28 and requires payments of 440 on day 0 and 100 on day 7. The otherwise unchanged whole-business baseline has cash of 500 at each relevant date after all other flows. The operating account already establishes a favorable incremental contribution of 660 and feasible capacity.

| Event | Cash without financing |
| --- | ---: |
| Opening, day 0 | 500 |
| After paying 440, day 0 | 60 |
| After paying 100, day 7 | −40 |
| After receiving 1,200, day 28 | 1,160 |

A committed facility can provide up to 80 before the day-7 payment. Its fee of 3 is withheld on drawing, and interest of 2 is paid with principal on day 28. A gross draw of 43 supplies the missing 40; day-7 cash becomes zero. Repayment of 45 leaves day-28 cash at 1,155. With a required reserve of 10, draw 53 instead; a draw of 43 no longer suffices. Assume the same stated fee and interest for these illustrative amounts.

If collection moves to day 40 while repayment stays on day 28, the first financing path leaves a gap of 45 on day 28. An actual extension or replacement is needed. Neither the unused limit nor the order's positive contribution establishes that extension.

#### FIN.2:5.1 - The calculation within the liquidity work

While preparing this case's payment plan, an analyst solves d − 3 = 40, where d is the gross draw and 3 is the withheld fee. Solving that equation determines the gross amount that supplies the missing usable cash. Through this sizing, the analyst performs part of constructing the dated liquidity account. The connection depends on the facility being available to this payer before the day-7 payment, the stated fee treatment, and the plan's reserve and repayment conditions.

Raise the required reserve from zero to 10: the same funding operation now requires d − 3 = 50, giving 53. Correctly repeating the old equation would no longer perform the needed sizing. Conversely, someone who can subtract amounts but cannot translate a withheld fee into net proceeds lacks a constituent operation needed for this plan. They can obtain an explanation and practise that operation, or obtain a qualified calculation whose conditions they can use. More repetitions of an unexplained spreadsheet formula do not supply the missing connection.

These are connected descriptions of the analyst's work. The lender's transfer is a different occurrence whose availability the plan relies on. Sending the completed account to a decision maker is a subsequent use.



#### FIN.2:5.2 - A delayed receipt also reduces available finance


In a separate constructed weekly account, one corporation has usable opening cash 20, a chosen minimum reserve 10, and no existing drawings. All amounts are in one currency, taxes and ordinary costs are already in the stated payments, and interest on a new line draw is paid after week 3. The supplied payment schedule has no earlier low point within each week.

| Week | Customer receipts | Operating payments | Cash without a new draw |
| --- | ---: | ---: | ---: |
| 1 | 30 | 50 | 0 |
| 2 | 80 | 30 | 50 |
| 3 | 20 | 30 | 40 |

A drawable line of 50 is additionally limited to 80% of eligible receivables. For this case, eligibility is tested on drawing; no later borrowing-base test or mandatory paydown occurs before the stated week-3 maturity. Eligible receivables are 40 at the week-1 draw date, so the maximum total draw is 32. There are no fees. Drawing 10 just before week-1 payments preserves the reserve; cash after weeks 1, 2 and 3 is 10, 60 and 50 before any repayment. Repayment with stipulated interest 1 after week 3 leaves cash 39. The remedy covers the full stated horizon.

Now a customer's dispute moves 25 of week-1 receipts to week 3 and makes 15 of the 40 receivables ineligible at the draw date. Unfinanced cash is −25, 25 and 40. The amount needed to preserve the reserve in week 1 is 35, but the line permits only 0.80 × 25 = 20. Drawing 20 leaves cash −5; neither the commitment of 50 nor the eventual receipt removes the week-1 failure.

Suppose the supplier actually agrees to move 15 of week-1 payment to week 2 without charge. With that change and the draw of 20, balances become 10, 45 and 60. After week-3 repayment of 20 and stipulated interest 2, cash is 38. Thus the operating concession and the available finance jointly restore the selected reserve. They are separate attainable actions, and the deferred 15 is paid rather than lost from the model. Without the supplier's agreement this combined route remains conditional. If payments precede the assumed draw within week 1, refine the account before claiming it works.



#### FIN.2:5.3 - A later borrowing-base test changes the repayment date


Vary the delayed-receipt case above by adding a later contractual test. At the test in week 2, eligible receivables are only 10 while the drawn principal is still 20. The permitted amount is 0.80 × 10 = 8, leaving an overadvance of 12. The stipulated agreement requires repayment of that excess, or acceptance of additional eligible security, by a stated deadline. Merely recording zero room for another draw leaves this obligation unpaid.

First suppose the test and cure deadline fall after the week-2 receipt of 80 and before its operating payment of 45. Opening cash for that week is 10. Repaying 12 leaves 10 + 80 − 12 − 45 = 33 after the operating payment, with principal 8 outstanding. Week 3 adds net operating cash of 15, giving 48; repayment of 8 plus the stipulated interest 2 leaves 38. For this variant, the contract keeps the total interest payment at 2 despite the earlier partial repayment. There are no other charges. The final balance matches the preceding case, but the repayment consumes liquidity earlier.

Alternatively, the company can supply previously unpledged eligible receivables of 15 if they are actually available and the agreement admits them. Their completed acceptance raises the base to 25 and permitted debt back to 20. This cures the overadvance without a cash repayment: week-2 cash remains 45, and the original week-3 repayment of 22 leaves 38. These claims are security, not another cash receipt. Check any effect of pledging them on other financing; the illustration assumes no competing pledge or cost.

Now move the test and cash cure deadline before the receipt of 80, with eligible receivables still 10. With only 10 on hand, repayment of 12 is unavailable; keeping the reserve of 10 would require 12 of new usable cash before that deadline. The later receipt cannot satisfy the earlier requirement. The company must obtain timely funding, complete an eligible collateral cure, obtain an effective amendment or return the unresolved failure. A request still awaiting acceptance does not change the account. FIN.12 supplies the actual cure rule and FIN.10 the terms of any replacement funding.

### FIN.2:6 - Bias-Annotation

The forecast follows the selected corporation's ability to pay. A group total can conceal a subsidiary's shortage, and a base-case collection date can understate customer risk. Choose adverse cases because their consequences matter, without representing unspecified probabilities as measured likelihoods.

### FIN.2:7 - Conformance Checklist

Can another treasurer recover the usable opening amount, all material dated flows, reserve, draw conditions and gross-to-net proceeds? Does every proposed cure remain funded through its repayment? Are cash in another entity and unfulfilled conditions excluded from the asserted available amount?

### FIN.2:8 - Common Anti-Patterns and How to Avoid Them

Using profit as payment capacity hides noncash items and timing; recover the cash account. Using the portal limit as draw evidence ignores the contract; inspect the remaining conditions. Adding the same customer receipt to both baseline and incremental forecast double-counts money; reconcile the two before calculating need.

### FIN.2:9 - Consequences

The result identifies the amount and date that a response must cover and the conditions under which it works. Finer timing and conditional flows add forecasting effort, so retain only detail that can change payment, reserve or funding advice.

### FIN.2:10 - Architectural Rationale

A dated cash account makes the decisive constraint visible before financing is ranked. Ratios can summarize liquidity but cannot demonstrate that a particular payment is fundable at its cutoff.

### FIN.2:11 - SoTA-Echoing

The public [CFA working-capital introduction][CFA-WC] frames the cash-conversion and liquidity problem. [OpenStax's cash-management discussion][OS-CASH] distinguishes transactional needs, precaution and accessible placements. FIN.2 develops the dated paying account, conditional availability and response timing rather than inferring payment capacity from a balance-sheet ratio. FDM.1–FDM.3 supply actual positions, support and contractual events. The constructed borrowing-base case shows why a receipt delay and lost credit capacity must be considered together. A changed payment, restriction or financing condition reopens the account.

### FIN.2:12 - Relations

FIN.1 supplies a missing decision boundary; FIN.4 supplies a missing cash projection. FIN.3 and FIN.10 compare responses, FIN.12 examines covenant access, and FIN.15 carries out the permitted action. [FDM][FDM] resolves financial positions when needed; it does not replace the liquidity calculation.

### FIN.2:End
