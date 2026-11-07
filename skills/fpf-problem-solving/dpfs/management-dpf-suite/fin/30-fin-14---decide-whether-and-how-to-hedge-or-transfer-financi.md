## FIN.14 - Decide Whether and How to Hedge or Transfer Financial Risk

**Type:** Method

**Status:** Stable

### FIN.14:0 - Use this when

A financial exposure matters enough to consider changing, offsetting or transferring it. Compare the protection obtained with cost, residual risk and cash demands.

Use the existing arrangement directly while its exposure and conditions remain adequate. A question about whether a payment actually settled belongs first in FIN.15. The fuller Solution explains how to construct a protection comparison when the amount, instrument behavior or choice is still unresolved.

### FIN.14:1 - Problem frame

The object is a protection arrangement for a specified exposure. It can change the underlying activity, use a natural offset, or introduce a derivative, insurance or other applicable transfer. Designing it does not establish that a contract is executed or that the underlying customer will pay.

### FIN.14:2 - Problem

A hedge can reduce price uncertainty while adding volume, basis, margin, credit or funding risk. Matching only the headline notional can leave the corporation with an obligation it cannot settle.

### FIN.14:3 - Forces

Reduce consequential downside while retaining useful flexibility and affordable cash requirements. Compare risk reduction with its price and the conditions under which protection actually works.

### FIN.14:4 - Solution

1. Start from the outcome and exposure in FIN.13. State which change the protection should limit, over what period and for which entity; distinguish cash protection from accounting presentation.
2. Form feasible alternatives: change currency or pricing terms, alter timing or activity, use a reliable natural offset, purchase optional protection, or enter a forward, swap or other appropriate arrangement. Include acceptance of the exposure where allowed.
3. Match amount, underlying reference, currency, reset and settlement dates, exercise conditions and remaining flexibility. Use FIN.8 for a needed option value and [FDM][FDM] for disputed contractual behavior.
4. Project the combined underlying and protection cash in the material scenarios. Include partial or late underlying performance, basis changes, margin or collateral, counterparty failure and termination where these affect the choice. A price hedge is not a guarantee of underlying volume or credit.
5. Compare costs, residual exposures and peak funding needs. Obtain actual legal enforceability and accounting treatment when the proposed use relies on them; a cash-protection comparison can be complete without claiming a reporting qualification.
6. Return the selected design or conditional recommendation, expected protection, exposure left open and what would require resizing, closing or replacing it. FIN.15 executes within authority and verifies settlement.



#### FIN.14:4.1 - Decide what protection is for


Start with the consequence supplied by FIN.13. A corporation may want to preserve a minimum cash contribution, prevent a funding failure, reduce uncertainty in a committed purchase price or limit a loss in the value of an interest. State the protected entity, quantity or activity, horizon and tolerated shortfall. A target for reported earnings needs the corresponding accounting interpretation; a target for payment capacity needs the dated cash account.

Explain why changing that exposure is worth its cost. Protecting the capacity to fund valuable operations, avoiding a costly distress response or maintaining a required margin can justify a hedge. Reducing a measured variance alone does not establish additional corporate value. If the corporation can bear the downside on the selected objective, acceptance may be a feasible alternative. If losses would prevent payment, a favorable expected value does not remove that constraint. FIN.1 supplies the objective and actual alternatives; FIN.2 tests payment capacity.

Keep the underlying commercial decision visible. Changing the invoice currency can move exchange risk to a customer but also change the price or demand. Matching a foreign loan to receipts can leave a useful currency offset and an unsuitable repayment horizon. Changing suppliers or physical stocks changes operations as well as financial exposure. Obtain those consequences from the actual commercial or operating plan; do not assume a natural hedge is free merely because it is not a derivative.

A sufficient supplied exposure and an existing authorized protection arrangement can support direct execution or continued use. Reopen the design when the protected outcome, amount, timing, terms or feasible alternatives change. A missed settlement under an otherwise appropriate contract first needs FIN.15's account of the actual problem; buying another hedge does not by itself resolve that obligation.



#### FIN.14:4.2 - Construct alternatives from what each arrangement makes happen


For each feasible form, recover the conditional cash and obligations it introduces.

| Form | Financial construction | Condition that can change the choice |
| --- | --- | --- |
| Change the activity or commercial terms | Recalculate receipts, costs and dates for the attainable operating alternative, including the party that takes the displaced risk. | Lost contribution, implementation cost, customer response or inability to change an existing commitment can outweigh the risk reduction. |
| Use an existing natural offset | Combine genuinely offsetting receipts and payments on compatible factors and dates; retain their separate performance and access conditions. | Equal currency totals can leave a gap if one payment arrives later or belongs to another entity. |
| Fix an exchange or rate through a forward or swap | Derive both parties' payments from the actual reference, notional schedule, dates, fixed terms and settlement rule. | A delivery duty, changing exposure amount, basis difference, collateral or termination payment can make a price fix costly to maintain. |
| Create a money-market hedge | Borrow or invest in the relevant currencies now so that a known future receipt repays a debt or a future payment is covered by a maturing investment. | Borrowing and investing rates, credit capacity, taxes, access and the actual collection date determine the result; the construction introduces real financing and counterparty claims. |
| Use futures or another margined offset | Match the financial sensitivity and contract amount, then carry each margin movement and the eventual closing or delivery into the cash plan. | Standard quantities and dates can leave a residual; changes in the relation between the exposure price and contract price leave basis risk. |
| Buy an option | Obtain a defined right or contingent cash payoff, pay its premium when due and preserve the exercise, expiry and settlement conditions. | Protection can expire before the exposure resolves; premiums, imperfect matching or a physically delivered exercise can still require money or assets. |
| Insure or obtain a guarantee for a specified loss | Derive the covered event, eligible amount, deductible, limit and claim-payment conditions from the actual agreement. | Exclusions, waiting periods, disputes and provider default can leave a loss or a cash shortage even when the event is covered. |

For a known foreign receipt Q at time T, a simple money-market construction borrows Q / (1 + rF × a) foreign units now, converts that amount at an obtainable spot selling price and invests the home proceeds until T. Here rF is the actual foreign borrowing rate and a is the matching accrual fraction under the stipulated simple-interest terms. The receipt repays Q at T. For a known foreign payment, invest its discounted foreign amount now and fund that purchase from available home cash or actual home borrowing. Use the real compounding and payment rules when they differ. This explains the direction of borrowing and investment; a forward quotation is a different attainable alternative, not proof that either construction is accessible.

For an option, FIN.8 supplies valuation when the premium or conditional strategy must be assessed. An actual sufficient price and payoff can be used directly. Do not price protection by discounting a speculative expected payoff at an arbitrary corporate WACC. Similarly, a market forward rate is an executable term only if an actual provider offers it under usable conditions; it is not automatically a forecast of the future spot price.

Obtain the important terms before treating a form as feasible. A contract called a collar can contain a purchased option and a written option that creates a duty in another state. A zero initial premium can be financed by giving up favorable outcomes or accepting that duty. The combined terms, including barriers, limits or cancellation rights where present, determine protection. [FDM.3][FDM] supplies the derivation of duties and state changes from those terms; FIN.14 compares their financial consequences.



#### FIN.14:4.3 - Choose quantity and dates from the residual exposure


Use gross exposure, reliable offsets and the intended protected portion to establish the proposed amount. The denominator of a hedge ratio must be clear: forecast sales, contracted invoices, expected collections and a price sensitivity are different quantities. A “100% hedge” of a forecast is not necessarily a full match to what will actually be delivered.

For a foreign receipt Q and a forward sale of h foreign units at home-per-foreign rate F, the combined terminal home cash, before charges and financing, is Q × S + h × (F − S), provided all stated transactions can actually settle. With fixed Q and h = Q, the expression becomes Q × F. With h different from actual Q, the remaining market sensitivity is Q − h. In a physical settlement, insufficient foreign receipts still have to be purchased; the algebraic net amount does not fund that purchase beforehand.

If the amount or date is uncertain, compare several protection quantities or a rule for changing them as the exposure becomes firmer. A firm delivery duty for the reasonably supported minimum and optional protection for additional volume can have different consequences from fixing the full forecast. Test the lower-volume and delayed cases explicitly. Treat a rolling hedge as a sequence of future transactions with future prices, access and costs; successive short contracts do not establish today's long-term fixed price.

Choose the reference and maturity from the actual exposure. For borrowing, match reset and accrual periods as well as nominal maturity. For a commodity, identify location, grade, delivery period and any difference between the purchased commodity and the traded reference. For an option, determine when the relevant uncertainty is resolved and whether exercise remains possible then. An offset that works at expiry may have large intervening value and cash changes.

Where an imperfect proxy is proposed, estimate how its payoff changes with the exposure on the relevant horizon and inspect unlike conditions. A regression or covariance estimate can support a quantity aimed at reducing historical variance under its assumptions. It does not establish the quantity that preserves a future cash floor, or that the relationship will persist during the material stress. Use the objective to choose the comparison and return the resulting residual exposure to FIN.13.



#### FIN.14:4.4 - Compare whole outcomes, including the path to settlement


Construct an unprotected or existing-arrangement account first. Add each proposed protection arrangement to that same account, applying the same underlying scenario. Retain premium, bid–ask spread, fees, taxes when relevant, collateral, financing, settlement and termination effects. A favorable derivative payment is one component of the protected outcome. Evaluating it alone would reward a hedge when the business loses and condemn it when the business gains.

Compare amounts on compatible dates. A premium paid now and a receipt in six months need both their actual cash dates and, for a value comparison, an appropriate common-date basis. FIN.5 supplies that pricing question. A quoted terminal gain is not a net gain if its premium or funding cost is omitted. A collateral transfer can restrict usable cash without being a permanent economic loss; its return or application must also be modeled under the actual terms.

Run the combined cash account through adverse paths, not just final states. A hedge that eventually offsets a price change can require margin before the related business cash arrives. If collateral is returned late or has a haircut, the temporary financing need can exceed the reported hedge loss. Include margin on the terms that actually apply; neither “OTC” nor “exchange traded” alone determines every funding condition.

Distinguish the failures that protection covers from those it leaves open. A currency forward generally does not make a customer pay. A price option does not automatically assure production volume. Credit insurance may reimburse a covered default after a delay rather than provide money on the original invoice date. A provider's inability to perform can remove the expected offset precisely when it is needed. Compare provider concentration with the corporation's deposits, borrowing access and other claims where they share the same failure.

Use actual settlement arrangements when determining gross cash demands. A cash-settled payoff can differ from a physical exchange of principals, even when their final economic values match under ideal conditions. Contractual netting or a supported payment-versus-payment service can change particular risks; neither arises from writing a net amount in the model. FIN.15 establishes the usable route and resulting effect. Return any material route limitation to the protection comparison before commitment.



#### FIN.14:4.5 - Select a design and retain the condition for changing it


Eliminate alternatives that cannot meet the required outcome under the accepted decision conditions or cannot be funded on obtainable terms. Compare the remaining protection, residual exposures, flexibility, implementation demands and price. A single largest expected receipt or lowest premium is insufficient if it trades away the outcome the hedge was meant to preserve. Conversely, maximal protection can cost more than the decision warrants.

State the chosen quantity, reference, dates and instrument behavior in terms that treasury can act on. Include the existing exposure, what remains unprotected, required premium or collateral resources, and the conditions that require reconsideration. An adequate existing dealing mandate can authorize ordinary implementation within those bounds. A proposed departure in amount, risk or rights returns through FIN.16 or the applicable decision authority.

Explain what happens if the exposure changes after commitment. Recover the current contract and its close, resize, novation or exercise possibilities before treating the original amount as adjustable. Terminating a hedge crystallizes its current obligations or value under the terms; entering an opposite trade can leave two contracts and two counterparties rather than extinguish the first. Compare continuing, modifying or closing on the remaining exposure and current costs. FIN.17 supplies changed facts, FIN.13 supplies the resulting exposure and FIN.15 verifies any actual contractual or settlement effect.

At that later decision date, compare the cash and rights still available under each attainable action. A current negative contract value is an existing economic burden; determine when and how each alternative pays or carries it. Keep that settlement amount separate from a new amendment charge. Earlier nonrefundable fees common to the alternatives are already incurred, while new dealing, funding and termination costs belong in the comparison. If an exit amount already settles the quoted contract value, adding that same value again would double count it.

Build a dated account for collateral released, applied or retained by the change. A promised release after an amendment payment cannot fund the payment without an available bridge. Record the old duty that is extinguished and the duty that remains, then recalculate residual exposure and cash. This permits a smaller hedge to be the preferred available revision even though a new hedge chosen before the original commitment would have had different terms.

Keep economic protection and reporting qualification distinct. If the decision relies on a particular hedge-accounting treatment, obtain the applicable designation, documentation, measurement and ongoing conditions from the responsible accounting specialist. The combined financial comparison can be useful without asserting that treatment. Actual enforceability, tax and authority similarly remain supplied conditions where they change the use.

### FIN.14:5 - Archetypal Grounding

The corporation expects a customer to pay 100 foreign units on day 30. A physical forward obliges it to deliver 100 foreign units and receive 90 home units that day. Assume the customer pays only 60, the unpaid claim of 40 remains, and the forward still requires delivery of 100. At spot 0.95 home per foreign unit, buying the missing 40 costs 38 home units.

If the corporation obtains that money and buys the currency in time, it delivers 100 and receives 90: current net home cash from the purchase and forward is 90−38 = 52, with the customer claim of 40 foreign units still outstanding. If it cannot fund or purchase the missing currency, there is an execution problem. The forward did not eliminate credit or volume risk.

For a separate rate example, debt pays a floating reference plus 2%, and a swap on the same notional and dates receives exactly that floating reference and pays fixed 4%. The matched net rate is 6% before other costs. A different reference, reset or floor breaks that simple cancellation and must be modeled.



#### FIN.14:5.1 - Compare a fixed amount, a smaller amount and optional protection


Before committing to a hedge, consider a constructed comparison for a customer expected to pay 100 foreign units at T. The action-changing scenarios collect either 100 or 60 at T and have a spot rate of either 0.80 or 1.00 home per foreign unit. In the 60-collection cases, the claim on the remaining 40 persists; its later recovery and value are outside these current-cash figures and must be considered separately in the whole financial choice.

Four available alternatives are left unhedged, a physical forward sale of 100 at 0.90, a physical forward sale of 60 at 0.90, and a cash-settled put on 100 at strike 0.90 costing 2 home units now. The put pays 100 × max(0.90 − S, 0) at T. The illustrative offers have no other fees or collateral, all counterparties perform, necessary physical purchases are obtainable, and time value is stipulated zero for this comparison. Actual funding capacity is tested separately.

| Collection and spot at T | Unhedged cash | Forward 100 | Forward 60 | Put 100, after premium 2 |
| --- | ---: | ---: | ---: | ---: |
| 100 at 0.80 | 80 | 90 | 86 | 88 |
| 100 at 1.00 | 100 | 90 | 94 | 98 |
| 60 at 0.80 | 48 | 58 | 54 | 56 |
| 60 at 1.00 | 60 | 50 | 54 | 58 |

Each forward result follows Q × S + h × (0.90 − S). For example, with collection 60 and spot 1.00, the forward for 100 requires buying 40 for 40, then delivering 100 for 90, leaving net current home cash 50. The smaller forward uses the 60 received and pays 54. The put expires without payoff, so selling the 60 at spot and subtracting its earlier premium gives total cash contribution 58.

Suppose the stated objective is a net cash contribution of at least 55 across these four cases, after the protection premium. Only the put meets that objective among the four alternatives. Its premium of 2 must be payable now, and the forward purchase may require interim funding. If only 1 is available for the premium and no further money is obtainable, the put is not feasible. The comparison then returns the need to change the objective, obtain a different attainable arrangement or change the underlying exposure.

With zero collection and spot 1.00, the put pays nothing and the total contribution is −2. The four-case selection therefore does not protect against complete nonpayment. A guarantee or collection response has a different covered event and must be assessed on its actual terms. A cash-settled option also does not automatically reduce its notional when collection falls: the proposed 100 remains a separate position. If it is no longer appropriate, reconsider it with the outstanding claim and available modification terms.

This comparison occurs before commitment. In the existing partial-receipt case above, the corporation already owes delivery under its forward; it cannot retrospectively choose the better column.



#### FIN.14:5.2 - Reduce an existing forward after the expected receipt changes


In a separate constructed case, a forward already requires delivery of 100 foreign units for 90 home units on day 30. It was based on forecast orders. At the new decision date, day 15, the revised orders support a receipt of only 60 foreign units on day 30; the other 40 were uncontracted forecast sales, so no customer claim for them exists. This differs from partial payment of an existing invoice. Assume the stated 60 is collected in both compared scenarios.

A new forward for the same settlement date is quoted at 1.00 home per foreign unit. With zero discounting for this contract-value comparison, the old sale at 0.90 has value 100 × (0.90 − 1.00) = −10. The bank offers an amendment that, once agreed and paid on day 15, extinguishes 40 of the delivery duty for a payment of 4 plus a new charge of 0.40. The remaining duty is to deliver 60 for 54 on day 30, with current value −6. The payment 4 settles the removed portion's existing value; 0.40 is the additional amendment cost.

The corporation has usable home cash 5 and a separate collateral claim of 10 already posted before day 15. Under the stipulated arrangements, continuing leaves all 10 blocked until completed settlement on day 30. The amendment returns 4 on day 16 and retains 6 until completed settlement on day 30. No further collateral calls occur in these compared paths. An unrelated committed home receipt of 50 arrives on day 20. The cash reserve is 2 throughout. All parties perform the stated payments and collateral releases; there are no taxes or other flows. An initial dealing fee of 0.20 was paid before day 15 and is already reflected in the opening cash.

**Continue the original forward.** Home cash becomes 55 on day 20. On day 30, buy the missing 40 foreign units before delivering 100. At a spot rate of 0.80 this costs 32; at 1.20 it costs 48. Even the larger purchase leaves usable cash 7 before the forward receipt. Receipt of 90 and return of collateral 10 then leave 123 or 107. Continuing requires no new day-15 payment, but retains the price exposure on the excess delivery quantity.

**Accept the amendment.** Paying 4.40 immediately from cash 5 would leave 0.60 and breach the reserve. An obtainable bridge advances 1.40 net on day 15 and requires repayment of 1.50, including its charge, on day 20. The cash path is 5 + 1.40 − 4.40 = 2 on day 15; 6 after the collateral return on day 16; and 6 + 50 − 1.50 = 54.50 on day 20. On day 30, deliver the collected 60 for 54 and receive the remaining collateral 6. Ending home cash is 114.50 in either spot scenario.

| Action from day 15 | Ending cash at spot 0.80 | Ending cash at spot 1.20 |
| --- | ---: | ---: |
| Continue the delivery duty of 100 | 123 | 107 |
| Amend it to 60 with the stated bridge | 114.50 | 114.50 |

If the objective is at least 110 of ending cash in both scenarios while maintaining reserve 2, the funded amendment meets it and continuing does not. If the bridge is unavailable, the amendment on these payment terms is infeasible. If the released collateral 4 is instead actually usable before the amendment payment, the bridge is unnecessary and ending cash is 114.60. That changed timing saves the bridge charge; returning already owned collateral is not a new hedge profit.

The later choice retains the old loss and its remaining contractual effect. It does not recreate an initial choice of a forward for 60 at today's rate without paying for the old position. FIN.13 receives the reduced delivery exposure; FIN.2 receives the amendment payment, collateral dates and bridge repayment; FIN.15 obtains the actual amendment effect and performs the funded actions.



#### FIN.14:5.3 - An eventual offset can require cash first


Consider a separate cash-settled forward sale of 100 foreign units at 0.90, paired with a receipt of 100 at day 30. Assume zero discounting and an enforceable term requiring cash collateral equal to an adverse marked value. On day 15, the remaining forward price is 1.00, so the seller's forward value is −10 and collateral 10 must be posted by day 16. Usable cash then is 6 and the required reserve is 2. Only 4 is free for this purpose, leaving a funding need of 6.

Suppose the spot rate is 0.80 on day 30, the customer pays in full, and the forward counterparty pays the resulting gain of 10 and returns all collateral 10 at that time. The operating receipt converts to 80. The hedge's dated cash is −10 on day 16 and +20 on day 30, for net 10 before funding costs; combined net cash from receipt and hedge is 90. Counting the collateral return as an additional profit would overstate that result by 10.

The eventual protection is therefore effective under these stated performance conditions, but it was not executable without the missing interim 6. FIN.2 assesses an obtainable response and its repayment; FIN.15 performs it within authority. A different margin rule, return date or failed counterparty changes both the funding and protection comparison.



#### FIN.14:5.4 - Basis and contractual floors leave different residuals


A manufacturer plans to buy 100 commodity units. The physical price is a traded reference plus a local basis. Initially those amounts are 50 and 5 per unit, and the initial futures price is also 50. A perfectly performing futures offset gains the increase in that reference on 100 units, with margin funding assumed available. At purchase, the reference is 60 but local basis is 9: physical cost is 6,900 and the hedge gain is 1,000, leaving net cost 5,900. The initial implied cost was 5,500. The residual 400 comes from the local basis, which the selected contract does not fix. Changing physical quantity also requires recomputing the offset amount.

For the rate example above, change the debt to pay max(reference, 0) + 2%, while the swap still receives the unfloored reference and pays fixed 4%. At a reference of 3%, total debt and swap cost is 5% + 1% = 6%. At a reference of −1%, debt costs 2% and the swap costs 5%, giving 7%. The debt floor defeats the claimed constant 6% even though notional and dates still match. A change in the loan's credit spread can leave another residual; matching the base reference does not fix that spread.

### FIN.14:6 - Bias-Annotation

A low premium or zero initial payment can conceal later collateral and termination costs. A reported hedge ratio can hide uncertainty in the exposure volume. The chosen protection may transfer risk to a counterparty with correlated weakness.

### FIN.14:7 - Conformance Checklist

Can the reader replay combined cash under normal and consequential adverse performance? Do notional, reference and dates match the claimed offset? Are margin, funding and counterparty effects included where material? Is any accounting or enforceability conclusion supported by its applicable facts?

### FIN.14:8 - Common Anti-Patterns and How to Avoid Them

Declaring the exposure “fully hedged” from matching notional hides partial collection; model the event. Treating a zero-cost contract as free ignores contingent payments and collateral. Removing an unpaid customer claim after settling the derivative confuses two positions; retain their separate effects.

### FIN.14:9 - Consequences

The result specifies what the corporation is protected against and what it must still fund or bear. The comparison can support choosing more expensive optional protection when volume uncertainty makes a fixed delivery obligation unsuitable.

### FIN.14:10 - Architectural Rationale

Comparing the combined activity and instrument reveals the protection's actual result. Separating design, execution and remaining claims prevents a desired risk reduction from being reported as an accomplished financial effect.

### FIN.14:11 - SoTA-Echoing

[FDM][FDM] supplies the conditional instrument and event distinctions; [CFA's option treatment][CFA-OPTIONS] supplies optional-payoff reasoning. FIN.14 uses both within a combined cash comparison, rather than treating instrument name or notional equality as protection. Changed underlying performance or settlement terms reopen the design.

[ACCA's developed foreign-exchange example][ACCA-FX] connects trade direction, dates, financing, contract quantity and premium to a cash comparison. Its historical examination assumptions do not choose a corporate policy. FIN.14 adds an explicit protection objective, uncertain collection, funding paths and remaining obligations; it does not generalize the source's assumed option exercise or linear basis convergence.

The public [CFA forward-commitment treatment, 2026][CFA-FORWARDS] distinguishes an agreed forward price from the contract's changing value. FIN.14 carries that distinction into the later choice of keeping or amending a hedge, together with actual charges, collateral access and financing. Its public valuation assumptions do not establish an obtainable exit or amendment.

### FIN.14:12 - Relations

FIN.13 supplies exposure, FIN.8 option value, FIN.2 funding consequences and FIN.15 execution. FIN.16 returns a material hedge recommendation. A legal or accounting qualification remains with its applicable specialist method.

### FIN.14:End
