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

Identify the claimed change, party, arrangement and relevant time. A current position can be established directly at the relevant time. To explain a change, establish its basis and the earlier position to the extent the explanation depends on it. To confirm one particular transaction or how it was carried out, establish the occurrence or actions the request identifies. Use FDM.1 for a missing position and FDM.2 for a party boundary that still matters.

Distinguish a change in permission, duty, usable resources, recorded information or business outcome. A dispatch record can establish that a particular sender sent the message “approved” to a named recipient by noon. If the claim concerns a decision or financial effect, establish which decision the message evidences and the authority or effect that claim requires. An authenticated record of the board’s decision may settle whether approval was granted. If the operative rule or the question concerns a particular signer, establish that party’s contribution.

#### FDM.4:4.2 - Recover the rule that gives the event its effect

Use the applicable terms or institutional rule to identify the recognized act or event, any required actor or authority, the conditions and the effective time. Some changes require communication. Others depend on performance or another occurrence.

Use [FPF A.2.8][DUTY] for duties, [FPF A.2.8.PER][PER] for permissions and [FPF A.2.9][ACT] for communicative work. For a disputed local term, use a qualified interpretation or obtain the specialist judgement the case still needs. A recording act can create an effect where the applicable rule gives it that force.

#### FDM.4:4.3 - Establish what actually occurred

Inspect the evidence relevant to that rule and effect. For a claim about a particular occurrence, match the evidence to the relevant parties, arrangement, amount and time. If the question concerns only the resulting position, use an adequate statement of that position or the effect common to all admissible histories under §4.4. Distinguish an instruction from its execution and a provider's local result from the recipient's result where those differences matter.

Use the dates that matter to the question. The occurrence, effective date, posting and actual availability can differ. Evidence that the provider received an instruction can answer that question while leaving the recipient’s access to funds unresolved. A confirmation received later can establish that the position changed on an earlier day. To explain an action taken on that day, determine what its decision maker could know and what grounds they used then.

For a payment run, recover what was commissioned. Acknowledgement of submission in the agreed form can finish an order to submit a batch. For a promise to settle each invoice, use the terms that determine what discharges it. A payment instruction in the payer's records and the matching credit in the recipient's records can describe stages of one transfer. Two references to an amount do not establish two settlements. Conversely, one transfer to an authorized collection agent can discharge two invoices if its amount, allocation and the agent’s receipt meet the terms of both. A reliable confirmation covering both named invoices, their amounts and discharge by the cutoff can answer the balance question directly. To explain how the payment run accomplished this, connect the relevant instructions and receipts to the rule for each discharge.

If sources disagree, compare their subjects, dates and meanings. Investigate a remaining factual discrepancy when the requested conclusion needs it and the inquiry can resolve it at justifiable cost. Otherwise report the supported result and limit. Use a source for the claim it can establish.

When relying on a missing entry, identify the routes to the effect in question and what each would have left in the examined records by the cutoff. Silence can settle the question when every route would have left a detectable entry. It can also settle an effect for which registration itself is indispensable, when that registration is established as absent. A bank’s instruction log may exclude an instruction there and still leave a waiver or set-off open. Other grounds can settle absence directly. If an agreement first takes effect on Monday and has no retroactive effect, it could give no discharge on the preceding Friday.

#### FDM.4:4.4 - Derive the effect and remaining position

Apply the rule to the established occurrence and identify any change and its effective time. For a partial payment, use the applicable allocation rule to calculate which amounts were discharged and what remains. Include other interest, fees or conditions only where the arrangement makes them relevant.

A forecast can clear its modeled balance at maturity. To establish actual discharge, use evidence of the receipt or other event recognized by the terms, or grounds that establish the same discharge under every remaining history. The evidence and terms must admit at least one history. If they conflict, resolve the conflict or qualify the calculation. FDM.3:5.2 shows how a confirmed receipt updates principal and interest.

Relate the calculation to its financial meaning. When the arithmetic is possible but the position it would establish is unclear, use [FPF B.1.5.EW][EW] to locate the missing operation. A contractual interpretation may be supplied by a qualified colleague or another adequate source. An incorrect computation calls for a computational correction.

If evidence establishes that the recognized event did not occur, report that the claimed change did not arise through that event. A different waiver, payment or recognized act can still matter. If the route remains uncertain, return any position or bound common to the permitted histories. Identify the missing premise for a conclusion that still depends on the route.

Suppose the opening debt was 105 and reliable evidence establishes that, by Friday, either a payment was received in settlement of 60 or an authorized set-off for 60 took effect. These are the only possibilities and there were no other changes. The debt is 45 either way. Whether money reached the creditor is still open. If the second possibility were a refundable deposit that did not discharge debt, the possible balances would be 45 and 105. At least 45 would still be outstanding. For an attainable minimum or maximum, justify the bound throughout and show that a permitted history reaches it. A tight bound need not be attained. For example, if all permissible rates are below 5% and some are arbitrarily close to 5%, 5% is their least upper bound even though no contract pays that rate. A threshold decision may need only a valid outer bound.

Relate the records to the supported position. If an account must be corrected, use its responsible process and preserve the relevant history. For a comparison of participants’ accounts, use [ADM.4][ADM].

#### FDM.4:4.5 - Return the result needed by the next user

Return the supported effect, time, remaining position and material limits the user needs. If a missing rule, occurrence or necessary account correction blocks further use, identify the question and who can resolve it when that is known. If different histories give the same answer to that user, return it and identify any distinct question about the event or the cash that remains open.

FDM.3 uses the resulting state for later events. FDM.5 uses the effect when examining a participant's service result. A demonstrated financial change can be useful even when its longer-term benefit is not yet known.

### FDM.4:5 - Archetypal Grounding

#### FDM.4:5.1 - A payment, an instruction and a modification

Suppose 105 is due on day 30 and the borrower pays 60 to the lender. Evidence establishes the payment. Under the supplied rule all 60 applies to this obligation and no additional fees or interest arise. The remaining amount is **45**.

A servicing report showing all 105 unpaid disagrees with the established position. Report the remaining 45 and the discrepancy. Retain the original contractual payment of 105 and the actual payment of 60 in their respective accounts.

Suppose the evidence instead shows only that the borrower sent an instruction for 60. That establishes submission. It leaves the payment event and reduction to 45 unresolved. If receipt is the only way the debt could have changed here, evidence of receipt or its absence can settle the residual. An adequate statement of the residual may already answer a balance inquiry while leaving the route open.

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

1. The affected party, the requested occurrence, effect or residual position and its relevant time are clear. The account establishes the prior position where the conclusion needs it.
2. The applicable rule and its action, authority or occurrence conditions are established where required.
3. Evidence and operative terms support the reported position, the event claimed or an effect established across the admissible histories. An inference from a missing entry accounts for the recognized routes and cutoff.
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

In §§4.2–4.4, use the rule and evidence to establish the requested occurrence or the financial effect. When alternative histories all produce the same residual, give that residual and preserve any uncertainty about the actual route. This distinguishes “60 instructed” from “60 paid” even when a local display says “complete.” Investigate further if a remaining premise matters to the requested finding or downstream use and the inquiry is worthwhile.

Actual local rules and event evidence govern an actual result. Reopen the account when either changes or when a later use requires a broader effect claim.

### FDM.4:12 - Relations

Use FDM.1–2 for missing positions or identities. Use FDM.3 to derive contractual event conditions and update its actual state with the effect established here. Use FDM.5 when that effect contributes to a claim about service use.

ADM.3, ADM.7–10 and the relevant financial practice supply effectivity, evidence, permission, usable provision and fulfillment questions at their own scope. A.2.8, A.2.8.PER and A.2.9 govern the underlying institutional distinctions.

### FDM.4:End
