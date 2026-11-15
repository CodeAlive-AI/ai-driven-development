## FDM.4 - Establish What a Financial Action Changed

**Type:** Architectural

**Status:** Stable


### FDM.4:0 - Use this when

Use this pattern when a financial action is reported as complete and you need to establish what, if anything, changed. Approval, sending an instruction, posting an entry and settlement can each support a different claim.

Establish the effect of the action or event on the relevant financial position. Give the supported change, the supported absence of that change or the particular effect still unresolved. Include the remaining position when the question needs it.

Use an established account of the effect when it supplies the evidence the present question needs.

### FDM.4:1 - Problem frame

A lending decision can authorize a next step without funding a borrower. An agreement can create a duty before funding. A payment instruction can be accepted for processing while the recipient still lacks usable funds. A payment can discharge only part of an obligation.

To establish an actual financial effect, identify the applicable rule and the event it recognizes. Check whether the evidence establishes the rule’s conditions.

### FDM.4:2 - Problem

A local completion label can be used to infer a wider result. That inference can leave a debt overstated, a payment falsely treated as available or a proposed agreement treated as effective.

Waiver, valid modification or another recognized act can change a position before any cash moves. Determine the mechanism from the applicable arrangement and the event that occurred.

### FDM.4:3 - Forces

Operational systems need timely completion signals. Their signals have scopes and can arrive before or after the effect relevant to another participant. Several dates may therefore be useful.

Records can disagree about time, party, meaning or whether an action succeeded. Examine the differences that matter to the requested effect. A routine account can be used directly when it already resolves them.

### FDM.4:4 - Solution

#### FDM.4:4.1 - Name the claimed change and prior position

Identify the claimed change, party, arrangement and relevant time. Establish the previous position as far as needed to explain the effect. Use FDM.1 for a missing position and FDM.2 for a party boundary that still matters.

Distinguish a change in permission, duty, usable resources, recorded information or business outcome. For a message marked “approved,” establish what decision the message reports and who issued that approval before relying on it for another claimed result.

#### FDM.4:4.2 - Recover the rule that gives the event its effect

Use the applicable terms or institutional rule to identify the recognized act or event, any required actor or authority, the conditions and the effective time. Some changes require communication. Others depend on performance or another occurrence.

Use [FPF A.2.8][DUTY] for duties, [FPF A.2.8.PER][PER] for permissions and [FPF A.2.9][ACT] for communicative work. For a disputed local term, use a qualified interpretation or obtain the specialist judgement the case still needs. A recording act can create an effect where the applicable rule gives it that force.

#### FDM.4:4.3 - Establish what actually occurred

Inspect the evidence relevant to that rule and effect. Match the parties, arrangement, amount and occurrence. Distinguish an instruction from its execution and a provider's local result from the recipient's result where those differences matter.

Use the dates that matter to the question. The occurrence, effective date, posting and actual availability can differ. Evidence that the provider received an instruction can answer that question while leaving the recipient’s access to funds unresolved.

If sources disagree, compare their subjects, dates and meanings. Investigate a remaining factual discrepancy when the requested conclusion needs it and the inquiry can resolve it at justifiable cost. Otherwise report the supported result and limit. Use a source for the claim it can establish.

#### FDM.4:4.4 - Derive the effect and remaining position

Apply the rule to the established occurrence and identify any change and its effective time. For a partial payment, use the applicable allocation rule to calculate which amounts were discharged and what remains. Include other interest, fees or conditions only where the arrangement makes them relevant.

A forecast can clear its modeled balance at maturity. To establish actual discharge, use evidence of the receipt or other event recognized by the terms. FDM.3:5.2 shows how a confirmed receipt updates principal and interest, and why an instruction of unknown effect leaves several states possible.

Relate the calculation to its financial meaning. When the arithmetic is possible but the position it would establish is unclear, use [FPF B.1.5.EW][EW] to locate the missing operation. A contractual interpretation may be supplied by a qualified colleague or another adequate source. An incorrect computation calls for a computational correction.

If evidence establishes that the recognized event did not occur, report that the claimed change did not arise through that event. A different waiver, payment or recognized act can still matter. If either the rule or occurrence remains unresolved, identify the missing premise and the effect that remains open.

Relate the records to the supported position. If an account must be corrected, use its responsible process and preserve the relevant history. For a comparison of participants’ accounts, use [ADM.4][ADM].

#### FDM.4:4.5 - Return the result needed by the next user

Return the supported effect, time, remaining position and material limits the user needs. If a missing rule, occurrence or necessary account correction blocks further use, identify the question and who can resolve it when that is known.

FDM.3 uses the resulting state for later events. FDM.5 uses the effect when examining a participant's service result. A demonstrated financial change can be useful even when its longer-term benefit is not yet known.

### FDM.4:5 - Archetypal Grounding

#### FDM.4:5.1 - A payment, an instruction and a modification

Suppose 105 is due on day 30 and the borrower pays 60 to the lender. Evidence establishes the payment. Under the supplied rule all 60 applies to this obligation and no additional fees or interest arise. The remaining amount is **45**.

A servicing report showing all 105 unpaid disagrees with the established position. Report the remaining 45 and the discrepancy. Retain the original contractual payment of 105 and the actual payment of 60 in their respective accounts.

Suppose the evidence instead shows only that the borrower sent an instruction for 60. That establishes submission. It leaves the payment event and reduction to 45 unresolved. To establish the residual position, determine whether the event recognized by the terms occurred.

In a separate case, suppose the competent parties validly modify a lender’s conditional advance obligation before funding. The supplied terms give that modification its effect. Report the changed undertaking from the effective event even though no money has yet moved.

The results depend on the stipulated formation, modification and payment-allocation terms. Use the terms governing the particular instrument to establish its effects.

#### FDM.4:5.2 - Deriving the position through an interpreted calculation

Suppose the lender receives 60 under terms classifying it as refundable cash collateral. The loan obligation of 105 remains outstanding. Subtracting 60 from 105 gives 45 arithmetically. Here the appropriate account retains **105** due on the loan and identifies the separate collateral position.

By interpreting the receipt under the contract, the modeler derives its financial effect and constructs the position account. The repayment terms permit subtraction from the debt. The collateral terms require a separate collateral position. The bank receipt is the financial event interpreted in that work.

If the modeller can calculate but lacks the required interpretation, use an adequate existing interpretation or obtain one from a qualified source. Develop the modeller’s own interpretive capability if the work also requires that ability. With the terms established, use the existing evidence of receipt. If collateral can later be applied to the debt, establish the relevant event and its effect before updating the obligation.

### FDM.4:6 - Bias-Annotation

A service team may judge success from its own processing, while a financial report emphasizes the latest posting. Check what each observation establishes under the rule giving the event its effect.

When the available sources cannot establish whether the event occurred, retain that uncertainty.

### FDM.4:7 - Conformance Checklist

Check these criteria for the particular effect claimed.

1. The affected party, prior position, claimed change and relevant time are clear.
2. The applicable rule and its action, authority or occurrence conditions are established where required.
3. Evidence supports the actual event at the scope claimed.
4. The derived effect and any residual obligation follow the applicable terms.
5. Records, effective relations and resource availability remain distinct where their differences matter.
6. The result distinguishes supported change, supported non-change and unresolved effect.

### FDM.4:8 - Common Anti-Patterns and How to Avoid Them

**Closing the obligation from a sent instruction.** Establish the event the applicable arrangement recognizes as performance.

**Treating all postings as either constitutive or merely descriptive.** Recover the actual rule and the role of the recording act in that arrangement.

**Using one date for every consequence.** Retain distinct occurrence, effect or availability dates when they change the receiving answer.

### FDM.4:9 - Consequences

A practitioner can explain what the financial action changed, what remains and which part the local completion signal establishes.

The account may establish that a required event did not occur, or that the available evidence leaves its occurrence unknown. An unresolved rule or a record requiring correction can also limit further work. Use a qualified source or the responsible participant when that work is needed.

### FDM.4:10 - Architectural Rationale

A financial effect depends on an operative rule and the occurrence satisfying its conditions. A term can establish what would happen. Evidence of an occurrence can establish which branch applies and when.

A transaction log is sufficient when it already supplies adequate evidence for a settled effect rule. A broad business-outcome inquiry is unnecessary for a narrow residual-balance question. The wider inquiry becomes useful when someone claims the financial change itself established the participant's benefit.

### FDM.4:11 - SoTA-Echoing

For an actual financial change, apply FPF’s distinctions among duties, permissions and communicative acts. Use ADM.3 and ADM.9–10 when the case turns on effectivity, usable provision or fulfillment. These distinctions help determine what a decision, message or record can establish.

In §§4.2–4.4, identify the rule, establish the recognized occurrence and derive the position. This distinguishes “60 instructed” from “60 paid” even when a local display says “complete.” Investigate further if a remaining premise matters to the requested finding or downstream use and the inquiry is worthwhile.

Actual local rules and event evidence govern an actual result. Reopen the account when either changes or when a later use requires a broader effect claim.

### FDM.4:12 - Relations

Use FDM.1–2 for missing positions or identities. Use FDM.3 to derive contractual event conditions and update its actual state with the effect established here. Use FDM.5 when that effect contributes to a claim about service use.

ADM.3, ADM.7–10 and the relevant financial practice supply effectivity, evidence, permission, usable provision and fulfillment questions at their own scope. A.2.8, A.2.8.PER and A.2.9 govern the underlying institutional distinctions.

### FDM.4:End
