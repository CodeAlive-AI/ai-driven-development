## FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms

**Type:** Architectural

**Status:** Stable


### FDM.3:0 - Use this when

Use this pattern when an amount or due-date field leaves unclear what an instrument requires under its terms. A payment date, draw condition, prepayment or guarantee can change the flows that the parties must arrange.

Establish the contractual events and flows relevant to the question. For a scenario, add the applicable assumptions. For a question about performance, relate the contractual or conditional account to evidence of what occurred.

Use ordinary financial arithmetic with the operative agreement or a competent interpretation of it. For an unclear term, use FDM.1:4.2 to identify which rule, date or calculation is unresolved. Obtain a supported interpretation if the result needs it, or give the conditional outcomes the available terms allow.

Use an existing schedule directly when its terms, state and assumptions match the question.

### FDM.3:1 - Problem frame

“Loan amount 100” does not say whether 100 is the advance, current principal or payment due. A repayment amount may depend on elapsed time, a reference value, an option or prior events. Its date may depend on a calendar rule rather than a number typed into a report.

What is due and what has been paid are different results. To forecast receipts from a schedule, give the assumptions about payment. To report actual receipts, use evidence of performance.

### FDM.3:2 - Problem

A flat list of amounts and dates can conceal the conditions that produce them. Treating the resulting schedule as an unconditional cash forecast then imports an unsupported performance assumption.

Recover the contractual rules and conditional outcomes that matter to the present use. A model of every contingency can cost more than the information it would supply for that question.

### FDM.3:3 - Forces

Contract terms can be precise while required inputs remain uncertain. An amount linked to a future reference value may be contractually well defined without being numerically known today.

Simplification is useful when it preserves the receiving answer. It becomes misleading when it erases an exercise condition, timing rule or priority of events that changes the amount or obligation.

### FDM.3:4 - Solution

#### FDM.3:4.1 - Recover the arrangement and intended question

Identify the relevant parties, instrument or arrangement, version of the terms and time from which the model starts. Use FDM.1 or FDM.2 for missing positions or boundaries.

Specify the requested result, such as the contractual schedule, an adverse funding scenario or the consequence of an option. To find the borrower’s next required payment, establish its obligation and the applicable event conditions. To find what it has already discharged, use evidence of performance. For its ability to pay, establish usable funds by the due date. Reuse adequate terms and schedules under their stated assumptions.

#### FDM.3:4.2 - Construct the event rules from the operative terms

Use the operative terms and supported interpretations. FDM.1 can supply them when needed. For an event relevant to the question, identify the actor or payer, any recipient, the quantity and currency where applicable, and the relevant time.

Read each material clause as a condition with a consequence. An installment can fall due on a date even though the obligation already exists. An election clause specifies an available action and the effect of a valid exercise. A floating-rate clause specifies the observation setting the rate and when it applies. An allocation clause determines how an actual or assumed receipt changes principal and interest.

Establish how to recognize the condition, calculate the consequence and carry the resulting state forward. If payments first satisfy accrued interest, calculate interest to the receipt’s effective boundary, allocate the receipt and carry the remaining principal into the next accrual interval. A field showing “payment = 1,000” leaves that allocation open.

##### FDM.3:4.2.1 - Match or adapt an available model

Assess a suitable available model against the operative rules. Check whether the candidate model represents the repayment rules and events in this agreement. When several model types could fit and their differences could affect this use, compare their behavior under the terms of the agreement. Principal payable only at maturity, fixed principal installments and equal total installments require different calculations. An optional prepayment is another distinct event. Use the actual terms to determine which the loan requires or permits.

Check whether the model’s definitions and event rules express the required allocation, calendar and exercise conditions. Use a fit directly, extend a separable missing behavior when the rest remains valid, or report what the model cannot support. A software default can support a conditional scenario if stated. Use the agreement to establish its actual terms. [SIE.3][SIE] helps decide whether the model suffices and SIE.4 helps connect different representations.

For an [ACTUS][ACTUS] implementation, inspect the selected contract type’s schedule, state initialization, payoff and transition rules, together with the dictionary and implementation edition. Supply the operative terms, supported starting state and any external inputs the model needs. Compare its events with the agreement-based derivation in this case. A successful sample run establishes what that sample executed. Applying the model to another contract needs a correspondence for that contract.

##### FDM.3:4.2.2 - Construct enough state and preserve the different dates

Work back from the next calculation to identify the required state. Simple interest on unpaid principal needs that principal, the rate and the start of the interval still to accrue. Carry any accrued unpaid interest separately. An exercised option may change which events remain possible. Other instruments can require other state.

Initialize the state at the requested starting time from supported history or an adequate opening account. After a repayment, the original principal may give a wrong forecast. After a rate change, today’s rate may give a wrong amount for an earlier interval. Use the intervening event or an adequate opening value. If neither is available, identify the later quantities that remain conditional.

Generate recurring dates from the specified anchor, interval and end condition. Preserve a short final period or end-of-month rule where the agreement requires it. Then determine which dates the business-day convention changes. The date used to calculate interest, the date on which payment is due and the date on which a transfer actually settles can differ. Notice and observation dates can add further relevant boundaries.

When a rate or principal changes, split the accrual interval at the effective boundary and apply each value during its interval. If events coincide, use the order supported by the terms or a qualified interpretation. Calculate each event from the state its rule requires. A spreadsheet row order needs a financial basis before it can determine the result.

#### FDM.3:4.3 - Derive and inspect contractual behavior

Work through the relevant events in their applicable order. Keep the operative terms, supplied input values and derived amounts distinguishable enough to inspect.

For a simple-interest interval with constant principal **P** and annual rate **r**, the constructed case below uses **P × r × d / 365**, where **d** is its specified actual-day count. Other conventions require their own supplied calculation. Keep the rule that selects the dates beside the arithmetic.

At an event, bring any required accrual to the applicable boundary. Determine the amount payable or noncash consequence, then apply the rule for the next state. For a receipt **C** allocated to interest first, compute payable interest **I**, apply the smaller of **C** and **I** to it and apply any permitted remainder to principal. If **C < I**, carry unpaid interest forward as the terms require. Use the arrangement’s rules for rounding, excess receipts and other allocations. Where capitalization is specified, add the eligible interest to principal without a cash payment.

At the due date, derive what is payable. A forecast may assume that the borrower pays it. To report an actual discharge, use FDM.4 with evidence of the event the terms recognize. Keep outstanding principal and interest until discharge or another effective change is established. A forecasting engine that clears its balance at scheduled maturity establishes only the state of that forecast.

Give the receiving user the starting position, operative rule, event condition, dates, amount and next state needed to reconstruct the result. A short table can suffice. An executable model can help with repeated or interacting calculations. Where users must inspect its result, show how a representative event answers their financial question.

Check derived flows and state changes against the terms under conditions representative of the claimed use. Examine a relevant boundary when the date, event order, exercise or allocation can change the result. Correct arithmetic still depends on the party, meaning of the amount and starting state. Use a simple two-row account for a fixed-payment loan when it suffices. Add branches or an executable model for behavior the question needs.

#### FDM.3:4.4 - Add scenarios and performance without replacing the contract

For a scenario, state the assumptions that affect the result, such as market values, option exercise, default or recovery. Derive the conditional flows. A probability or expectation needs a basis appropriate to the claim, including explicitly supplied weights for a conditional calculation.

Preserve contractual flows alongside scenarios or expectations when the receiving use needs those different amounts. Expected receipts combine possible outcomes under a model. Actual receipts require evidence of performance. Use FDM.4 to establish their effect on the remaining position.

For a financing choice, valuation or funding question, supply the qualified flows to the method that needs them. Use [FIN.10][FIN10] to compare financing terms and [FIN.2][FIN2] to relate dated amounts to usable funds. Discounting, risk treatment and rules for choosing an alternative require their respective grounds.

#### FDM.3:4.5 - Return and adapt the model for its receiving use

Return the contractual or conditional flows with the parties, timing rules and assumptions the question needs. An unknown future market value can leave a usable formula. Competing readings of a term may give different formulas or dates. When no single value is established, give the supported range, conditional branches or precise unresolved amount.

Distinguish an observation, exercise of an existing right, an amendment and correction of a record. A new market fixing gives an input to an existing rule. An effective amendment may change the rule. A late bank confirmation can establish a receipt that occurred earlier. Update the state, rule or evidence that actually changed.

For a valid prospective amendment, preserve established history and apply the revised rule from its effective boundary. Recompute dependent later events. If effectivity or treatment of prior accrual is unresolved, qualify the affected amount and obtain an interpretation when it is needed. Use [ADM.3 and ADM.10][ADM] for the temporal or performance question.

Revisit the affected calculation when the relevant state, scenario premise or intended use changes. Use FDM.4 for the established effects needed to update actual state. Use FDM.5 for a question about how the model contributed to a service result. Preserve the basis of an opening value or changed rule when a later user needs it.

### FDM.3:5 - Archetypal Grounding

#### FDM.3:5.1 - A fixed payment, expected receipt and actual payment

Suppose a lender advances 100 and the borrower owes one payment of 105 on day 30. The case stipulates valid formation, currency and fixed payment terms. The two parties’ cash flows under the schedule are shown below.

| Event | Lender's cash flow under the stated schedule | Borrower's cash flow under the same schedule |
| --- | ---: | ---: |
| Successful advance | −100 | +100 |
| Contractual payment on day 30 | +105 | −105 |

The signs follow each party’s viewpoint. The second row states what is due under the contract. An actual receipt requires a payment under the applicable conditions.

Suppose a performance model assigns an 80% probability to receipt of 105 and a 20% probability to receipt of 60 on day 30. Its conditional expected receipt is **0.8 × 105 + 0.2 × 60 = 96**. The probabilities are stipulated. Interpreting an unexplained score as a probability would require a separate basis. The contractual amount is 105, and no discounting enters this calculation.

If the actual payment is 60, report that receipt separately. Under the example’s allocation rule, all 60 applies to the obligation. With no additional fees or interest, 45 remains due. The original contractual payment remains 105. Use FDM.4 to establish the actual effect.

Suppose an arrangement specifies support of 80 for X’s debt after a stated failure and valid demand. Identify the beneficiary and payment date from the provisions governing them. If the creditor receives the payment after default, it supplies no cash to X for the original day-7 payment. If the terms leave the recipient or timing open, report the resulting limit.

#### FDM.3:5.2 - Constructing a partial payment and a shifted due date

What must B arrange to pay on the next due date after lender L receives an early payment of 1,000? Both parties use USD. The example stipulates an effective agreement, identified parties and the following terms governing these events.

| Supplied term | Modeling consequence to derive |
| --- | --- |
| L advances 3,650 to B on 2 April 2026. | The advance creates principal of 3,650 when it occurs; it is a cash inflow for B and outflow for L. |
| Ordinary interest is simple, 10% annually on unpaid principal, actual days divided by 365. An interval includes its first date and excludes its last. Interest itself bears no interest. | Split an interval when principal changes. Carry accrued interest separately until paid; no capitalization. |
| Remaining principal and ordinary interest are payable on 2 May. A nonbusiness payment date moves to the following business day without extending ordinary interest accrual. In this example Monday–Friday are business days and there are no holidays. | Accrual ends on 2 May. Payment is due on 4 May under the stipulated calendar. |
| B may make an early payment on a business day after valid notice received at least one business day earlier. An effective receipt first pays all interest accrued to that date, rounded to cents, then principal. There is no early-payment fee. | A notice enables the action but changes no amount by itself. Accrue first, allocate the receipt, then use the reduced principal. |
| Payment takes effect on irrevocable credit to L’s designated account. All effective dates here are treated as the beginning of that date. | A submitted instruction establishes submission. Principal changes on the recognized effective receipt under the allocation terms. |
| No other payment, fee, rate change or capitalization affects this calculation. Round interest to the nearest cent, halves upward, when it is paid; final interest is rounded once at maturity payment. | The example's arithmetic needs no guessed charges or daily rounding. Questions about later default charges require their separate terms. |

The history establishes the 2 April advance, valid notice on 16 April and irrevocable credit of 1,000 on 17 April. For these confirmed transfers, both parties' corresponding cash movements occurred on the stated dates. The account is prepared just after the 17 April receipt. The future path assumes full payment on 4 May, with B's debit and L's irrevocable credit both on that date.

The 1,000 receipt includes interest and principal. Fifteen days of interest on 3,650 at 10% per year using actual/365 give 15.00. Apply 15.00 to interest and the remaining 985.00 to principal. Principal becomes 2,665.00 and unpaid accrued interest becomes zero.

| Event or boundary | Cash for B | Derived state or required payment |
| --- | --- | --- |
| Confirmed advance, 2 April | +3,650.00 | Principal 3,650.00; interest starts accruing. |
| Accrual to 17 April, before receipt allocation | 0 | Interest 3,650 × 0.10 × 15 / 365 = 15.00. |
| Confirmed receipt, 17 April | −1,000.00 | Pay interest 15.00 and principal 985.00; principal 2,665.00, unpaid interest zero. |
| Ordinary accrual endpoint, 2 May | 0 | Another 15 days produce unrounded interest 10.95205479… . |
| Payment due, 4 May | −2,675.95 if fully performed | Principal 2,665.00 plus rounded interest 10.95. Actual discharge still depends on the receipt condition. |

The amount due comprises the principal and interest being demanded. Adding it to those balances would count them twice. The transfer signs reverse for L. Use the terms to identify how the corresponding bank movements affected the obligation.

The first interval accrues on the 3,650 then outstanding. The next accrues on 2,665. Payment moves to Monday while ordinary accrual stops on Saturday. Subtracting the full 1,000 from principal would omit the interest allocation. Applying 2,665 to the first interval would use a principal that arose later.

Suppose instead that ordinary interest runs to the adjusted payment date. Keep the established first receipt and its allocation. The later interval increases from 15 to 17 days. Its interest is 12.41232877… and 2,677.41 falls due. B’s provision of 2,676 covers the original amount and falls short by 1.41 under the changed term. If the operative text leaves the end date open, report both conditional amounts and the unresolved interpretation.

Return to the original terms, with ordinary accrual ending on 2 May. Now suppose the 17 April record establishes only a submitted instruction and its effect is unknown. Keep the confirmed advance. To determine actual principal, use qualified evidence of whether and when that attempt produced irrevocable credit, or seek the provider’s result if needed. Principal of 2,665 is conditional on credit on 17 April. If the attempt failed and no other receipt occurred, principal is 3,650. Ordinary interest through 2 May is 30.00 and 3,680.00 is due on 4 May. A credit on a different date requires splitting accrual at that date. If its outcome remains unknown, return the affected possibilities.

If the confirmed 1,000 instead belongs to a refundable collateral arrangement, use FDM.4 to establish its effect. The same transfer amount and date can create a collateral position and leave the loan principal unchanged. FDM.4:5.2 develops that distinction.

For a funding question, use [FIN.2][FIN2] with the qualified amount, due date and B’s usable funds. Use [FIN.10][FIN10] to compare financing arrangements when needed. Use FDM.5 to establish whether a treasury service used the model, arranged the required payment and produced a claimed contribution. The calculation itself can answer the question about how much is due.

#### FDM.3:5.3 - Constructing the payment conditions of a guarantee

Suppose G separately guarantees L up to 2,000 of B’s unpaid principal on the loan in §5.2. Payment requires the principal due date to have passed, two following business days to have elapsed without cure, and G to have received a valid demand. It falls due two following business days after that demand. Use the same weekday-only calendar. Can this guarantee give B funds for the payment on 4 May?

Construct the condition as a conjunction. A principal shortfall alone supplies only one part. Keep the outstanding covered principal from the loan, the end of the cure interval and the demand's validity and receipt as distinct inputs. When all activation conditions hold, the amount is the lesser of covered unpaid principal and 2,000; the recipient is L. A scenario assumption about default cannot substitute for an actual valid demand.

Suppose B makes no maturity payment and no intervening event reduces principal. The two following business days are 5 and 6 May. A valid demand received on 7 May makes payment due on 11 May, with 8 and 11 May the two following business days. Covered principal is 2,665, so 2,000 of the guarantee is due to L on this branch.

The guarantee provides B with no funds for 4 May. It may protect L against part of a later loss or affect a separate offer of financing. For an actual guarantee payment, use FDM.4 to establish its effect on L’s claim and any claim G acquires against B. A payment of 2,000 to L can change the holder of a claim without reducing B’s total obligations by the same amount.

Derive the trigger, qualifying action, beneficiary and due date together. Entering the guarantee limit as a loan payment omits the conditions that produce the event. If demand validity is unresolved, give the conditional event. Use a qualified determination of validity if the question needs a definite outcome. Other established loan amounts remain available.

### FDM.3:6 - Bias-Annotation

A precise formula can attract more confidence than its inputs deserve. Keep the source and uncertainty of performance assumptions visible, especially when a score has been converted into a probability.

A familiar simple loan can also bias the interpretation of another instrument. Use its actual terms; a repeated software field name does not establish the same event behavior.

### FDM.3:7 - Conformance Checklist

Check the following for the intended use of the flows.

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

An amount that previously appeared definite may depend on an unresolved term or unknown input. A conditional amount or formula can still be usable. More complex instruments usually require more work to construct and maintain the model.

### FDM.3:10 - Architectural Rationale

An instrument’s behavior follows from how terms and events change its state over time. An amount-and-date record can suffice for a fixed obligation. Extend it when the question depends on conditions that change the result.

Separating contractual behavior from performance keeps both interpretable. A single blended “forecast cash flow” can be useful to its intended decision, but its construction must retain the contractual and scenario meanings needed to explain or revise it.

### FDM.3:11 - SoTA-Echoing

ACTUS supplies event schedules, state initialization, payoff calculations and state transitions. Its [technical specification v1.1][ACTUS-SPEC] (2020) gives a historical example in the PAM prepayment rule, which brings accrual to the event before reducing principal. The [terms dictionary][ACTUS-TERMS] v1.4 (8 December 2023) distinguishes shifting a calculation date from shifting a payment date under the applicable business-day convention. These distinctions inform §§4.2–4.3. To use an ACTUS implementation for the loan above, check how its date and event rules map to that loan’s agreed treatment, including the maturity date.

The [ACTUS analytics account][ACTUS-ANALYTICS] relates contract inputs and external risk factors to analytical uses. Its [Quick Start][ACTUS-QUICKSTART] gives an implementation entry. A spreadsheet can suffice for an inspectable small calculation. Repeated or interacting events may justify an event engine and its mapping and maintenance costs. Use the selected edition’s specification and dictionary to map the operative terms and check the resulting behavior.

FINOS CDM’s [Event Model, version 7.0.0][CDM-EVENT] describes trade state and changes. An amendment, an observed reset and a transfer have different effects. Use this distinction in §4.5 to separate rule changes, new inputs and evidence of performance. The state-and-event representation serves lifecycle integration. To derive contractual amounts, use the applicable payoff logic and establish the correspondence if both models are needed.

The examples derive events from their stipulated agreements. When assessing an ACTUS or CDM implementation, compare its conventions and outputs with that derivation. Use [SIE.3 through SIE.4][SIE] for reuse and correspondence, and FDM.4 for actual effects. Revisit a mapping if changes in terms, state, event behavior or implementation edition affect its use.

### FDM.3:12 - Relations

FDM.1–2 supply adequate positions and party boundaries. FDM.4 establishes actual events and their effects; FDM.5 uses the flows relevant to a participant's service result.

Use SIE.3–6 to construct and connect models. Use [Management Accounting (MA.4)][MA4] to reconcile operating, reporting and cash accounts and [MA.5][MA5] for a forecast using the applicable conditional flows. Use [FIN.10][FIN10] to design or compare financing terms and [FIN.2][FIN2] to compare dated requirements with usable funds. For a valuation or choice, use the method and evidence appropriate to that financial task.

### FDM.3:End
