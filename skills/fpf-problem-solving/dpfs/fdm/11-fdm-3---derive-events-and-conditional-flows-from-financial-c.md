## FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms

**Type:** Architectural

**Status:** Stable


### FDM.3:0 - Use this when

Use this pattern when a financial instrument's amount or due-date field cannot answer what happens under its terms. The question may concern payment timing, a conditional draw, repayment, a guarantee or another event that changes the required flows.

The pattern governs an event and flow model of the relevant arrangement. It returns contractual events under stated terms, any scenarios needed for the question and their relation to observed performance.

The construction assumes ordinary financial arithmetic and access to the agreement or a competent interpretation of it. It explains how to obtain and adapt the event model from that basis. An unresolved legal term returns to the precise interpretation request in FDM.1:4.2.

Use an adequate existing schedule directly when its conditions match the question. A new diagram is unnecessary if the contractual behavior is already clear.

### FDM.3:1 - Problem frame

“Loan amount 100” does not say whether 100 is the advance, current principal or payment due. A repayment amount may depend on elapsed time, a reference value, an option or prior events. Its date may depend on a calendar rule rather than a number typed into a report.

Contractual behavior and actual performance also differ. An amount due can remain unpaid. A forecast of receipts requires assumptions about performance even when the contractual schedule is certain.

### FDM.3:2 - Problem

A flat list of amounts and dates can conceal the conditions that produce them. Treating the resulting schedule as an unconditional cash forecast then imports an unsupported performance assumption.

A model of every possible contingency would be costly and often impossible. The working problem is to recover the contractual logic and the conditional outcomes that can change the present use.

### FDM.3:3 - Forces

Contract terms can be precise while required inputs remain uncertain. An amount linked to a future reference value may be contractually well defined without being numerically known today.

Simplification is useful when it preserves the receiving answer. It becomes misleading when it erases an exercise condition, timing rule or priority of events that changes the amount or obligation.

### FDM.3:4 - Solution

#### FDM.3:4.1 - Recover the arrangement and intended question

Identify the relevant parties, instrument or arrangement, version of the terms and time from which the model starts. Use FDM.1 or FDM.2 for missing positions or boundaries.

State the needed answer: the contractual schedule, an adverse funding scenario, the consequence of an option or another specific question. To determine what a borrower must pay next, obtain its obligation and conditional payment account. Determining what it has already discharged needs established performance; assessing whether it can fund the next payment also needs an account of usable money. Reuse existing terms and schedules to the extent that their scope and assumptions match.

#### FDM.3:4.2 - Construct the event rules from the operative terms

Use the operative terms and supported interpretations obtained through FDM.1. For each event that can change the answer, establish who acts or pays, to whom, what amount or quantity is determined, in which currency and at what time.

Read a consequential clause as a connection between a condition and a consequence. An installment clause determines an amount that becomes due on the specified date; the obligation to make that payment may already exist. An election clause creates an available action and specifies when a valid exercise changes the arrangement. A floating-rate clause specifies which observation sets the rate and when it applies. A payment-allocation clause determines how an actual or assumed receipt changes interest and principal.

For each such connection, explain how to decide that its condition holds, calculate its consequence and carry forward what has changed. For example, “payments first satisfy accrued interest” requires calculating the interest up to the payment's effective boundary before applying the remaining receipt to principal. The closing principal then supplies the next accrual interval. Simply extracting “payment = 1,000” omits that operation.

##### FDM.3:4.2.1 - Match or adapt an available model

Try an available model against these rules before constructing a new one. Select a contract family by behavior: scheduled principal repayment only at maturity, specified principal installments and equal total installments imply different future calculations. The marketing label “loan” does not decide among them. An optional prepayment is also different from a mandatory amortization installment.

Inspect the chosen model's definitions, assumptions and event behavior. Check that it can express the actual allocation, calendar and exercise rules. Use it directly when it fits, extend a separable missing behavior when the other meanings remain valid, or retain the unsupported part explicitly. A software default can be used as an explicit assumption; it does not determine the agreement's meaning. [SIE.3][SIE] supplies this reuse decision; SIE.4 supplies a qualified correspondence when two representations use different meanings.

For an [ACTUS][ACTUS] implementation, the useful return is to the chosen contract type's schedule, state initialization, payoff calculations and state transitions, together with the selected dictionary and implementation edition. Supply the operative terms, a supported starting state and any external observations or scenarios that the model needs. Compare its produced events with the agreement-based construction. A successful sample request establishes execution of that sample; it does not establish the mapping for another contract.

##### FDM.3:4.2.2 - Construct enough state and preserve the different dates

Work backward from the next calculation to determine what must be carried forward. Simple interest on unpaid principal needs that principal, the rate and the beginning of the unaccrued interval. Interest already accrued but not paid needs its own amount. An exercised option may change which later events are possible. A more complex instrument can require other state; an unused field need not be invented.

Initialize those values for the requested starting time from supported history or a qualified existing account. Starting halfway through a loan with its original principal can produce a wrong forecast after a repayment. Estimating prior interest from today's principal or rate can also be wrong after a change. Recover the intervening event or the adequate opening value. If it is unavailable, identify which later quantities remain conditional.

Generate recurring dates from the specified anchor, interval and end condition. Preserve a short final period or end-of-month rule where the agreement requires it. Then determine which dates the business-day convention changes. The date used to calculate interest, the date on which payment is due and the date on which a transfer actually settles can differ. Notice and observation dates can add further relevant boundaries.

At a rate or principal change, split the accrual interval at the effective boundary and apply each value only to its interval. When events coincide, obtain the order from the terms or their qualified interpretation. Calculate on the state that the event's rule actually consumes. A convenient spreadsheet row order supplies no financial reason for that choice.

#### FDM.3:4.3 - Derive and inspect contractual behavior

Work through the relevant events in their applicable order. Keep the operative terms, supplied input values and derived amounts distinguishable enough to inspect.

For a simple-interest interval with constant principal **P** and annual rate **r**, the constructed case below uses **P × r × d / 365**, where **d** is its specified actual-day count. Other conventions require their own supplied calculation. Keep the rule that selects the dates beside the arithmetic.

At an event, first bring any needed accrual to its applicable boundary. Determine the amount payable or the noncash consequence. Then apply the event's rule to obtain the next state. For a receipt **C** allocated to interest first, calculate the payable interest **I**, apply the smaller of **C** and **I** to interest, and apply any permitted remainder to principal. Carry unpaid interest forward when **C < I**. Rounding, excess receipts and other allocations follow the arrangement's rules. Capitalization instead adds the eligible interest to principal with no cash payment.

At a due date, the terms determine the amount now payable. A payment event under an assumed performance path can settle it in a forecast. For an account of actual performance, FDM.4 supplies whether the required effect occurred. Keep principal and unpaid interest until their discharge or other change is established. If a forecasting engine clears balances at a scheduled maturity event, that transition cannot by itself establish that the real borrower paid.

The resulting account should let the next user recover the starting position, operative rule, event condition, calculation dates, conditional amount and subsequent state. A short table may be enough. Use an executable model when repetition or interacting conditions make that necessary, while keeping an inspectable example of how its events answer the financial question.

Check the flows and state changes against the terms under representative conditions. Inspect a boundary where a date, event order, exercise or allocation can change the result. A calculation can be mechanically correct while using the wrong meaning for “amount”, the wrong party or an inappropriate initial state. A simple fixed-payment loan can still be modeled in two rows; add branches or execution only where the needed behavior justifies them.

#### FDM.3:4.4 - Add scenarios and performance without replacing the contract

For a scenario, state the additional assumptions: market values, exercise, default, recovery or another condition relevant to the use. Derive the resulting conditional flows. If a probability or expectation is needed, obtain an adequate basis for it and retain its conditions.

Keep the contractual schedule available alongside expected or scenario flows. An expectation is an account across possible outcomes under a model; it is not another amount that every counterparty must pay. Likewise, an observed payment belongs to the actual-performance account. FDM.4 establishes its effect on remaining positions.

A financial choice or valuation may need discounting, risk treatment or comparison with alternatives. [FIN.10][FIN10] consumes the contractual behavior when comparing financing terms; [FIN.2][FIN2] uses the amounts and dates with usable funds. Supply the qualified flows to the method answering the financial question. The event model alone does not select its decision rules.

#### FDM.3:4.5 - Return and adapt the model for its receiving use

Return the contractual or conditional flows, relevant parties, time rules and assumptions at the detail the receiving use needs. Name a missing term or uncertain input where it changes the answer. A missing future market value can leave a usable formula; a missing interpretation can leave different formulas or dates. Return a range, conditional branches or an unresolved amount when the available basis does not determine one value.

Separate a new observation, an exercised existing right, a change to the agreement and correction of an earlier record. A new market fixing supplies a value to an existing rule; an effective amendment can change the rule. A late bank confirmation can establish an earlier receipt. Each calls for a different update.

For a valid prospective amendment, preserve the history already established and apply the changed rule from its effective boundary. Recompute dependent later events. If the amendment's effectivity or treatment of earlier accrual is unclear, obtain that interpretation before rewriting the prior account. [ADM.3 and ADM.10][ADM] supply the temporal and performance inquiries.

Reopen only the dependent parts when the relevant state, a relied-on scenario premise or the receiving use changes. FDM.4 supplies established effects for updating actual state; FDM.5 examines how using the model contributes to the participant's result. Preserve the source of an opening value or changed rule when later users need it to understand that update.

### FDM.3:5 - Archetypal Grounding

#### FDM.3:5.1 - A fixed payment, expected receipt and actual payment

In the constructed loan, a lender advances 100 and the borrower owes one payment of 105 on day 30. Valid formation, currency and the fixed payment terms are supplied. The model can begin with:

| Event | Lender's cash flow under the stated schedule | Borrower's cash flow under the same schedule |
| --- | ---: | ---: |
| Successful advance | −100 | +100 |
| Contractual payment on day 30 | +105 | −105 |

The signs describe each party's perspective. The second row is contractual; actual receipt still requires performance.

For illustration, suppose a separate performance model assumes an 80% probability of payment of 105 and a 20% probability of payment of only 60, both on day 30. Its expected receipt is **0.8 × 105 + 0.2 × 60 = 96**. These probabilities are supplied assumptions, not an interpretation of an unexplained score. The expected amount is neither the contractual amount nor a discounted value.

If the actual payment is 60, retain that observation separately. Under the example's supplied application rule and absence of additional fees or interest, FDM.4 can establish 45 remaining due. The contractual schedule does not become “60 due” merely because only 60 was paid.

Now consider a conditional support arrangement for X. The terms require a payment of 80 only after a specified failure and valid demand. Its event model must preserve those conditions and the actual payment timing rule. It cannot supply 80 of unconditional day-7 funding merely because that amount appears in the document. If the rule does not establish when funds can arrive, the timing result remains unresolved.

#### FDM.3:5.2 - Constructing a partial payment and a shifted due date

The question is what B must arrange to pay at the next due date after a 1,000-unit early receipt by lender L. Both parties use USD. The case supplies an effective agreement, valid party identities and the following complete terms for the events considered; their legal effect is a premise of the example.

| Supplied term | Modeling consequence to derive |
| --- | --- |
| L advances 3,650 to B on 2 April 2026. | The advance creates principal of 3,650 when it occurs; it is a cash inflow for B and outflow for L. |
| Ordinary interest is simple, 10% annually on unpaid principal, actual days divided by 365. An interval includes its first date and excludes its last. Interest itself bears no interest. | Split an interval when principal changes. Carry accrued interest separately until paid; no capitalization. |
| Remaining principal and ordinary interest are payable on 2 May. A nonbusiness payment date moves to the following business day without extending ordinary interest accrual. For this example only, every Monday–Friday is a business day and there are no holidays. | The accrual endpoint is 2 May; the payment due date is 4 May. This is a stipulated calendar, not a jurisdiction's calendar. |
| B may make an early payment on a business day after valid notice received at least one business day earlier. An effective receipt first pays all interest accrued to that date, rounded to cents, then principal. There is no early-payment fee. | A notice enables the action but changes no amount by itself. Accrue first, allocate the receipt, then use the reduced principal. |
| Payment takes effect only upon irrevocable credit to L's designated account. All effective dates here are treated as the beginning of that date. | A submitted instruction alone cannot establish the receipt or the principal reduction. |
| No other payment, fee, rate change or capitalization affects this calculation. Round interest to the nearest cent, halves upward, when it is paid; final interest is rounded once at maturity payment. | The example's arithmetic needs no guessed charges or daily rounding. Questions about later default charges require their separate terms. |

The history establishes the 2 April advance, valid notice on 16 April and irrevocable credit of 1,000 on 17 April. For these confirmed transfers, both parties' corresponding cash movements occurred on the stated dates. The account is prepared just after the 17 April receipt. The future path assumes full payment on 4 May, with B's debit and L's irrevocable credit both on that date.

The decisive interpretation occurs before subtraction. The 1,000 is a total receipt, not a principal-only reduction. Fifteen days of interest on 3,650 at 10%/365 equal 15.00. The receipt therefore pays 15.00 of interest and 985.00 of principal. Principal becomes 2,665.00; accrued unpaid interest becomes zero.

| Event or boundary | Cash for B | Derived state or required payment |
| --- | --- | --- |
| Confirmed advance, 2 April | +3,650.00 | Principal 3,650.00; interest starts accruing. |
| Accrual to 17 April, before receipt allocation | 0 | Interest 3,650 × 0.10 × 15 / 365 = 15.00. |
| Confirmed receipt, 17 April | −1,000.00 | Pay interest 15.00 and principal 985.00; principal 2,665.00, unpaid interest zero. |
| Ordinary accrual endpoint, 2 May | 0 | Another 15 days produce unrounded interest 10.95205479… . |
| Payment due, 4 May | −2,675.95 if fully performed | Principal 2,665.00 plus rounded interest 10.95. Actual discharge still depends on the receipt condition. |

The due amount is a view of the principal and interest being demanded, not a third balance to add to them. Signs reverse for L's account of the same transfers. Neither those signs nor the matching bank amounts establish the institutional allocation without the terms.

Accrue the first interval on the principal that was outstanding during it. The next interval uses 2,665, and the payment moves to Monday while ordinary accrual still stops on Saturday. A model that subtracts the entire 1,000 from principal has omitted allocation; a model that uses 2,665 for the first interval has rewritten the past.

Now change one term: ordinary interest runs to the adjusted payment date. The first receipt and its allocation remain established. Only the later accrual interval changes from 15 to 17 days. Its interest becomes 12.41232877… and the due amount becomes 2,677.41. B's provision of 2,676 would cover the original obligation and fall short by 1.41 under the changed term. Reuse the first interval instead of rebuilding it. If the operative text does not settle which accrual rule applies, return these conditional results and the precise interpretation question.

Change the evidence instead of the term: the 17 April record proves only an instruction and its effect is unknown. Keep the confirmed advance. Ask the payment provider whether and when the same attempt produced the required credit. The 2,665 principal is then conditional on credit on 17 April; it is not an established actual balance. A proved failure with no other receipt leaves principal 3,650 and ordinary interest 30.00 through 2 May, giving 3,680.00 due on 4 May. A credit on a different date requires splitting at that date and recalculating. Missing evidence does not establish any one of these paths.

If the confirmed 1,000 instead belongs to a refundable collateral arrangement, recover that arrangement's effect under FDM.4. A transfer with the same amount and date can create a collateral position while leaving the loan principal unchanged. FDM.4:5.2 develops this distinction between refundable collateral and repayment.

For the model's use, [FIN.2][FIN2] consumes the qualified amount and due date together with B's usable funds; [FIN.10][FIN10] can compare a different financing arrangement. FDM.5 asks whether the treasury service used the model to arrange a sufficient payment and what effect followed. The next action and any claimed benefit depend on that receiving use.

#### FDM.3:5.3 - Constructing the payment conditions of a guarantee

For the loan in §5.2, suppose G separately guarantees L up to 2,000 of B's unpaid principal. The supplied terms activate payment only after the principal due date has passed, two following business days have elapsed without cure, and G has received a valid demand. Payment is due two following business days after that demand. The same stipulated weekday-only calendar applies. The question is whether this guarantee can supply B with money for the 4 May payment.

Construct the condition as a conjunction. A principal shortfall alone supplies only one part. Keep the outstanding covered principal from the loan, the end of the cure interval and the demand's validity and receipt as distinct inputs. When all activation conditions hold, the amount is the lesser of covered unpaid principal and 2,000; the recipient is L. A scenario assumption about default cannot substitute for an actual valid demand.

On the branch where B makes no maturity payment and no intervening event reduces principal, the two following business days are 5 and 6 May. A valid demand received on 7 May makes payment due on 11 May, after 8 May and 11 May as the two following business days. Covered principal is 2,665, so the guarantee payment is 2,000 on that branch.

This construction supplies no funds to B before 4 May. It can protect L against part of the later loss, and its existence could affect a separately offered financing decision. Those are different uses. To account for a later guarantee payment, FDM.4 also needs its effect on L's claim and any resulting claim by G against B. The guarantee amount alone cannot establish that B's total obligations fell by 2,000.

The transferable move is to derive the trigger, qualifying action, beneficiary and resulting date together. Loan-style arithmetic with a guarantee limit inserted as a payment would miss the work that produces the event. If demand validity is unresolved, return the affected conditional event and obtain the responsible interpretation; unrelated known loan amounts remain usable.

### FDM.3:6 - Bias-Annotation

A precise formula can attract more confidence than its inputs deserve. Keep the source and uncertainty of performance assumptions visible, especially when a score has been converted into a probability.

A familiar simple loan can also bias the interpretation of another instrument. Use its actual terms; a repeated software field name does not establish the same event behavior.

### FDM.3:7 - Conformance Checklist

For the intended flow use, examine whether:

1. The arrangement, parties, relevant terms and initial state are identified.
2. Event conditions, amounts, currencies, timing and state updates follow the applicable terms or explicit assumptions.
3. The representation retains the branches and ordering that can change the answer.
4. Contractual, scenario, expected and actual flows remain distinguishable.
5. Missing terms and uncertain inputs are exposed where they affect the result.
6. A valuation or decision claim uses the further method and evidence it requires.

### FDM.3:8 - Common Anti-Patterns and How to Avoid Them

**Using principal as the maturity payment.** Recover the amount's contractual meaning and derive the payment from the terms.

**Treating a schedule as a receipt forecast.** State the performance assumptions and retain the contractual obligation separately.

**Applying an undocumented default.** Establish whether the chosen convention belongs to the actual arrangement. If it is only a scenario assumption, say so where it changes the flow.

### FDM.3:9 - Consequences

The user can explain where an amount or date comes from and can compare contractual requirements with conditional and actual outcomes. The result can feed funding, risk, reporting or service work.

The model may reveal that a previously definite number depends on an unresolved term or uncertain input. That limits reliance while giving the recipient a precise next question. Greater instrument complexity increases construction and maintenance effort.

### FDM.3:10 - Architectural Rationale

Events and their conditions are central because an instrument's financial behavior depends on how the arrangement responds over time. A flat amount-and-date record can be sufficient for a simple fixed obligation; it needs extension when conditions alter that obligation.

Separating contractual behavior from performance keeps both interpretable. A single blended “forecast cash flow” can be useful to its intended decision, but its construction must retain the contractual and scenario meanings needed to explain or revise it.

### FDM.3:11 - SoTA-Echoing

The practice question is how to obtain an event model from terms and use it through changing conditions. ACTUS offers an algorithmic supplier: schedules, initialized state, event payoffs and transitions. Its [technical specification v1.1][ACTUS-SPEC], released in 2020, is a historical reference for those rules. For example, its PAM prepayment rule brings accrual to the event before reducing principal. The [terms dictionary][ACTUS-TERMS], version 1.4 dated 2023-12-08, distinguishes changing a calculation date from shifting the payment date. Those distinctions inform §§4.2–4.3; the agreement determines which behavior is applicable.

The current [ACTUS analytics account][ACTUS-ANALYTICS] connects contract inputs and external risk factors to analytical uses. Its [Quick Start][ACTUS-QUICKSTART] supplies an implementation entry. A spreadsheet is adequate for an inspectable small construction; an event engine becomes useful when repeated or interacting calculations justify the mapping and maintenance effort. Use the selected implementation's specification and dictionary when constructing that mapping. Neither a familiar contract-type name nor successful execution of a sample establishes agreement-specific behavior.

FINOS CDM's [Event Model, version 7.0.0][CDM-EVENT] provides a complementary model of trade state and changes. Terms amendments, observed resets and transfers with different statuses supply different updates. It informs the distinction in §4.5 between changing a rule, obtaining an input and establishing performance. Such a state-and-event representation is useful for lifecycle integration, while contractual payoff logic is useful for deriving amounts. A project can need both; their outputs require a qualified correspondence.

The worked cases use their stated agreement terms. To assess an ACTUS or CDM implementation, compare its result and conventions with that agreement-based model. [SIE.3 through SIE.4][SIE] supply the general reuse and correspondence methods, and FDM.4 supplies actual-effect reasoning. Reopen a relied-on mapping when its terms, state, event behavior or implementation edition changes.

### FDM.3:12 - Relations

FDM.1–2 supply adequate positions and party boundaries. FDM.4 establishes actual events and their effects; FDM.5 uses the flows relevant to a participant's service result.

SIE.3–6 supply general model construction and connection. [Management Accounting (MA.4)][MA4] reconciles operating, reporting and cash accounts; [MA.5][MA5] uses the relevant conditional flows in its forecast. [FIN.10][FIN10] uses contractual event behavior to design and compare financing instruments and terms; [FIN.2][FIN2] compares dated requirements with usable funds. The responsible financial practice supplies any additional valuation or choice method.

### FDM.3:End
