## FIN.17 - Refresh Financial Models and Data

**Type:** Method

**Status:** Stable

### FIN.17:0 - Use this when

A new receipt date, price, contract, accounting input or operating fact may change a financial model or conclusion currently being used. Update the affected result and its conditions. If the change cannot affect that use, a supported no-update conclusion is sufficient.

### FIN.17:1 - Problem frame

The object is a financial model, projection or conclusion together with the grounds on which someone relies on it. A source-data change is distinct from a change in the described contract or actual position.

### FIN.17:2 - Problem

Updating an input file can leave the receiving recommendation stale. Rebuilding every model after any change wastes effort, while treating every assumption change as a new method choice creates unnecessary work.

### FIN.17:3 - Forces

Keep live reliance current without redoing unaffected calculations. Preserve enough connection between grounds and conclusions to identify which change matters, without maintaining an exhaustive registry of every model cell.

### FIN.17:4 - Solution

The six steps below provide a short route when the necessary financial grounds are already adequate. Use the connected explanations that follow when constructing the result, resolving a changed condition or adapting the way of working.



#### FIN.17:4.1 - Short working route


1. Identify the changed fact or source and the financial use that may depend on it. Recover the previously supported result and its relevant assumptions.
2. Trace the consequence through affected cash dates, amounts, values, ratios, constraints and advice. Distinguish correction of a description, a new expectation, an amended agreement and an actual event.
3. Revise the affected model or projection with the new grounds and recompute the dependent result. Retain unchanged accounts and current supported comparisons. When the changed assumption requires a different method, return that specific choice to FIN.18.
4. Examine the condition most likely to change the action: funding at a due date, sign of value, covenant access, hedge amount or recommendation. Correct any inconsistency introduced by the update.
5. Return the updated model, projection or financial conclusion with its conditions for use. If the needed fact is missing, state the specific reliance limit and what remains usable.
6. Arrange ongoing observation only for an actual continuing use, with a source and trigger that can change action. A one-time calculation does not by itself require continuous monitoring.



#### FIN.17:4.2 - Identify the change before replacing the number


Recover the source, effective time and meaning of the new information. A corrected invoice amount says the earlier description was wrong. A customer's expected payment date changes a forecast. An agreed extension changes the contractual due date. A settled, usable bank receipt changes cash and may discharge a claim under its actual terms. These changes can refer to the same invoice while requiring different model operations. FDM supplies the position, term and event interpretation when it is unclear.

Compare the new information with the exact ground previously used. Check the entity, claim, currency, units, period and whether the value is gross, net, cumulative or a movement. A cumulative collection of 60 does not add another 60 to a model that already included the first 40. A percentage stated per year cannot replace a monthly input without the appropriate conversion. A revised reporting classification may leave cash unchanged while altering a ratio whose definition uses that classification.

Establish whether the source is adequate for the current use. A sales team's revised expectation can be enough to run a liquidity scenario but cannot establish that a lender has changed its repayment date. A bank feed may establish a posting while leaving value date or availability unresolved. Obtain the specific missing interpretation where it changes action. Preserve usable parts of the account instead of waiting for every description to become equally certain.

Keep an earlier forecast available when it will be used to understand error or assess a method. The current operating view should use the supported new grounds, while the earlier decision remains interpretable on what was known then. This need can be met by an existing dated forecast or retained output; it does not require duplicating every workbook after every edit.



#### FIN.17:4.3 - Trace the change to the receiving financial use


Start with the result currently being relied on: today's payment instruction, next week's cash plan, a purchase recommendation, a headroom assessment or a reported value. Follow the financial relation that carries the change. A collection delay first affects cash timing. If it requires borrowing, financing changes later repayments and perhaps tax or value. If the receipt also supports a borrowing base, its eligibility can change the obtainable draw. The consequences are coupled even if separate worksheets calculate them.

Identify the smallest set of dependent results that contains those consequences. The same claim can appear in a receivable schedule, cash forecast and collateral calculation. Those descriptions must agree about the claim while retaining their different uses. A contract amendment may also change accrued charges or security; a simple move of the cash date can leave these dependent meanings stale. Use FIN.2 and FIN.10–FIN.12 for the affected financing calculations and FDM for the position and terms.

Retain distinctions across horizons. A monthly collection total can remain unchanged when a receipt moves from the first to the last week of the month, yet an intervening payroll becomes unfunded. A long-term value can change little while the next-day settlement path fails. Conversely, a change to a distant terminal margin may alter a purchase price limit without changing the cash available for this week's payments. Materiality follows the receiving action and tolerance, not one universal percentage of revenue.

Stop tracing when a supported boundary shows that the changed ground cannot affect a further result at the required precision or use. An unchanged supplier account can be reused directly. Explain a no-update conclusion through that boundary: the renamed debtor is the same party with the same claim and timing, or the corrected historical display figure is outside the model's inputs and relied-on result. The mere absence of a visible formula link does not establish independence when someone manually copied the earlier result into advice.



#### FIN.17:4.4 - Roll actual events into the remaining forecast


Choose the observation cutoff and reconcile opening position plus actual movements to the position at that cutoff. Then forecast what remains. For cash, a receipt already in the opening bank balance must not also remain as a future inflow. For a receivable, actual settlement reduces the remaining claim only to the extent established by the terms and event. A partial payment leaves the unpaid balance and its expected dates visible. FIN.4 supplies account roll-forward; FDM.4 resolves an uncertain financial effect.

Keep the contractual date, expected date and actual date where their difference changes the result. A late forecast collection does not remove overdue status or alter a creditor's right. A payment instruction sent before cutoff can remain unsettled. Show the supported status and the usable cash consequence rather than forcing every item into either “paid” or “unpaid” when the evidence cannot support that simplification.

Replace forecasts with actuals on an explicit common basis. A monthly forecast may combine several invoices, whereas the actual source lists transactions. Reconcile the included population and any fees, withholding, returns or currency conversion before treating their difference as error. Correct a mapping defect in the description without rewriting the underlying event. Extend the remaining forecast far enough to contain the obligations created by a proposed remedy; a bridge loan is not resolved merely because its draw removes a gap inside the original horizon.

If evidence of an important event is late, use the best-supported present position with a named reliance limit. An unknown payment status may require FIN.15's recovery before another instruction is sent. A scenario can show the consequences of receipt and nonreceipt, but it does not establish which occurred. The current recommendation must retain that distinction.



#### FIN.17:4.5 - Recompute a coherent account and explain the difference


Apply the changed inputs through the owning calculation. Recalculate the dependent account, then reconcile the outputs to its financial identities: opening cash plus dated inflows less dated outflows; opening debt plus draw, accrual or amendment less repayment; or the applicable asset, claim and ownership bridge. Distinguish an inconsistent model from a model that correctly reports a shortage, negative value or breached constraint. Changing an input to make a warning disappear can destroy the information the update was meant to reveal.

Explain the movement from the earlier answer in terms the receiver can use. Separate the effect of new actual events, a revised forecast and a changed valuation or policy premise when those differences matter. A rate-only recomputation can isolate one change under otherwise fixed assumptions. It cannot establish that the rate change caused an observed market outcome. When several nonlinear inputs change together, a sequential bridge depends on the order of the changes; state that basis or show the joint result directly.

Reconnect shared assumptions. A new sales expectation can change variable expense, inventory provision, customer collections and tax, while a fixed capacity payment may remain unchanged. Scaling every line by revenue imports a method change without examining its grounds. If the current construction cannot express the new business relation, return the particular choice to FIN.18 or the supplying operating method. A different coefficient within a still adequate relationship can remain a routine refresh.

Compare the updated result with the same decision criterion used before, unless the authorized decision itself changed. New forecast cash does not silently revise the reserve. A reduced value does not automatically change an agreed transaction price. The refresh exposes the discrepancy and sends it to the work that can act on it.



#### FIN.17:4.6 - Test the changed path at the point where it could fail


Choose checks from the financial consequence of the update. If collection moves after repayment, inspect the cash available just before repayment and the actual replacement finance. If the value crosses the purchase threshold, check the changed cash, risk basis and relevant alternative. If an agreement changes a draw limit, recompute that limit from its actual definitions before using the facility. A balanced spreadsheet alone establishes none of those external conditions.

For an implemented model, check that the changed source reaches the intended outputs. A stale imported value, a formula overwritten by a constant or a calculation mode that leaves results unchanged can defeat an otherwise correct financial method. Compare the result with an independent small calculation or an expected limiting case where that can expose the defect. A suitable reviewer may be needed for a consequential complex model; the scale of checking should follow the reliance and uncertainty.

Preserve useful earlier checks when their predicates and inputs are unaffected. Test the changed relation and the consumers that depend on it instead of rebuilding an unrelated valuation. For coupled changes, checking each altered cell alone is insufficient: their combination can create a funding gap or violate an assumption even though each isolated change appears acceptable.

If a check fails, distinguish an implementation error, an inadequate method and an adverse financial conclusion. Repair the implementation through the model's normal controls. Return an inadequate method to FIN.18. Carry an adverse but correctly computed result to FIN.16 or the relevant financial decision. These returns prevent “fixing the model” from becoming an instruction to restore the earlier preferred answer.



#### FIN.17:4.7 - Replace stale reliance as well as the model


Give the receiver the changed result, its effective basis and the consequence for the earlier instruction or recommendation. Identify the previous result that is no longer adequate where coexistence could cause action on obsolete grounds. An updated workbook stored elsewhere does not repair a payment request or investment memo still using the old amount. Update the actual receiving account, or explicitly return the required change to its owner.

When a transaction is already committed, the refresh must start from that commitment. It can recommend a modification, finance the remaining duty or change future action; it cannot undo the contract by replacing its forecast. Separate the instruction that can still be withdrawn from the financial effect that has already occurred. FIN.15 supplies execution and recovery; FIN.14 handles a changed protection arrangement.

A useful return can be short: “Collection now falls on day 40; the loan still requires 45 on day 28; the earlier funding recommendation is conditional on obtaining 45 before repayment.” Include the affected calculation when the receiver needs to inspect it. Preserve an unaffected operating contribution or valuation component explicitly when doing so prevents an unnecessary restart.

Finish when the current financial result and its actual receiving use agree, or the exact unresolved dependence is returned. A model refresh can be complete while the resulting financing choice remains open. Those outcomes should remain distinct so that a successful recalculation is not reported as restored payment capacity.



#### FIN.17:4.8 - Choose an observation rhythm that can still change action


For continuing reliance, connect observation to the time needed to respond. A weekly forecast cannot protect a same-day settlement if the decisive information arrives and the payment becomes binding between updates. Identify a practicable source and the latest point at which an adverse change can still lead to funding, resizing or a stop. Use event-triggered reconsideration for a material missed receipt, changed offer or new commitment when waiting for the next calendar cycle would be too late.

The source's delay limits what monitoring can achieve. A daily report built from last month's customer expectations does not create daily knowledge. Improve the needed source, retain a conditional buffer or narrow the reliance when the observation cannot support the required response. The financial value and burden of obtaining more timely information belong in the receiving comparison.

Avoid turning every numerical movement into a full refresh. A materiality rule can retain an adequate current result when a change is within a supported tolerance and does not cross an action boundary. Test the threshold near the boundary and under combined changes; two individually small movements can exhaust a narrow margin together. A new entity, business model or contractual structure can invalidate the rule itself.

End monitoring when the reliance ends, the position is settled or another current process takes over the actual observation. Preserve the historical result needed for explanation or method evaluation. A completed one-time appraisal does not become an ongoing surveillance obligation solely because it used a model.

### FIN.17:5 - Archetypal Grounding

FIN.2's order was expected to collect 1,200 on day 28. Its draw of 43 supplied net cash 40 and was due with interest, totaling 45, on day 28. A new supported expectation moves collection to day 40; it does not amend the loan. The updated cash projection shows a day-28 gap of 45. The operating contribution before financing remains 660 if all other operating grounds are unchanged. The analyst must reconsider the financing recommendation because repayment on day 28 is now unfunded; the previous net gain of 655 cannot be retained without accounting for a feasible repayment arrangement and its cost. FIN.10 supplies that comparison. By contrast, correcting a customer display name while retaining the same debtor, claim, dates and use may support no financial-model update.



#### FIN.17:5.1 - Partial collection changes the remaining account


In a separate constructed case, opening cash is 20, a receipt of 100 is expected on day 8, payroll of 70 is due on day 12 and a committed supplier payment of 20 is due on day 14. Cash must remain at least 10. No other flows occur through day 20. The original projection reaches 120, then 50 and 30, so both payments are funded.

At the end of day 8, actual collection is 60. The remaining claim of 40 is now expected on day 18; the customer obligation itself has not been amended. The updated account starts from actual cash 80. It reaches 10 after payroll and −10 after the supplier payment. It needs an additional 20 before day 14 to preserve the reserve. Keeping the original forecast receipt of 100 as a further future inflow would count cash already collected again.

An obtainable bridge can supply net 20 before the supplier payment and require 21 on day 20 after collection. With that arrangement, cash is 30 before the supplier payment, 10 afterward, 50 after collection and 29 after repayment. The original operating receipt and payments still give a closing cash amount of 30 before the new financing cost; the bridge reduces it by 1. If an offer of “20” instead deducts an upfront fee of 1 and supplies only 19, it fails the first-date reserve by 1. The actual net advance must govern the update.

Move the expected remaining collection again, to day 25. The same bridge no longer has a funded day-20 repayment: cash would be 10 before repayment and −11 afterward, a gap of 21 including the reserve. FIN.10 must compare an obtainable later maturity or another funded path. The model refresh is a completed identification of that changed need, not evidence that replacement finance exists.



#### FIN.17:5.2 - A changed value premise reaches the purchase advice


Another constructed appraisal compares an immediate outlay of 100 with two annual cash receipts of 60. On a supplied matching annual rate of 10%, value is about 104.13 and NPV is +4.13. The recommendation is therefore sensitive to fairly small changes in the qualified cash and return grounds.

Suppose a newly supported risk basis raises the matching rate to 12%, while an operating change reduces each receipt to 55. Rate-only recomputation on the original flows gives value about 101.40 and NPV +1.40. Applying the changed cash at 12% gives value about 92.95 and NPV −7.05. That sequential bridge explains a rate contribution of about −2.73 followed by a cash contribution of about −8.45. Reversing the sequence changes the attributed intermediate contributions; the combined final result is the same.

FIN.5 supplies the changed return basis and FIN.4 and FIN.6 supply the altered flows. FIN.17 carries them together to the relied-on value, while FIN.16 revises the purchase advice. If the purchase is still optional, the prior positive-NPV recommendation is no longer supported at price 100. If it is already binding, the remaining decision concerns its attainable continuation; the historical outlay is not made avoidable by recalculating NPV.

### FIN.17:6 - Bias-Annotation

A convenient new datum can be adopted before its meaning or reliability is understood. Conversely, a model owner can protect an earlier recommendation by treating a consequential change as cosmetic.

### FIN.17:7 - Conformance Checklist

Is the changed fact distinguished from the financial event or agreement it describes? Are all action-changing dependent results updated, and unaffected results retained? Does the return name the actual updated object or a specific no-update reason? Is any ongoing observation justified by continuing use?

### FIN.17:8 - Common Anti-Patterns and How to Avoid Them

Changing an input without recomputing the dependent financial results and reconsidering the advice that uses them can leave the recommendation based on obsolete assumptions; carry the change through to that receiving use. Rebuilding unrelated models increases work without repairing the current answer. Treating a revised forecast as lender consent changes the wrong object; recover actual agreement.

### FIN.17:9 - Consequences

The practitioner returns a current financial result or an explicit reliance limit. This can reopen a financing decision while preserving the supported operating account.

### FIN.17:10 - Architectural Rationale

Refresh follows the connection between a changed ground and its use. It is smaller than redesigning the method and broader than editing a number in a data source.

### FIN.17:11 - SoTA-Echoing

[MA][MA] supplies purpose-qualified forecasts and account differences; [FDM][FDM] distinguishes descriptions from financial positions and events. FIN.17 adopts these distinctions to update relied-on finance conclusions. Compared with blanket refresh or input-only replacement, it follows the action-changing consequence; a changed method basis invokes FIN.18.

[ICAEW's Financial Modelling Code, 2024][ICAEW-MODEL] develops readable model flows, separation of actual and forecast data, and checks directed at possible errors. FIN.17 uses those contributions for updating a relied-on financial result and its consumers. For models implemented outside spreadsheets, retain the applicable principles and choose checks that fit that implementation. Actual financial terms and effects remain supplied through FDM and the direct FIN Methods; MA.4–MA.6 supply account and forecast meanings. A changed model assumption, contractual condition or receiving use can reopen the refresh.

### FIN.17:12 - Relations

FIN.17 refreshes the models, projections and conclusions used by the other FIN methods. FIN.18 handles a needed method choice, while FIN.16 returns changed advice. The appropriate MA or FDM method supplies a newly unresolved source account.

### FIN.17:End
