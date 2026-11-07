## FDM.4 - Establish What a Financial Action Changed

**Type:** Architectural

**Status:** Stable


### FDM.4:0 - Use this when

Use this pattern when someone says a financial action is complete but the resulting position is uncertain. Approval, a sent instruction, a system posting and settlement can support different claims.

The pattern governs an account of an actual action or event's financial effect. It returns a supported change, supported non-change or a specific unresolved effect, including the remaining position where that matters.

Use an adequate established effect account directly. Reconstructing an uncontested payment from every source adds no value when the receiving use already has sufficient evidence.

### FDM.4:1 - Problem frame

A lending decision can authorize a next step without funding a borrower. An agreement can create a duty before funding. A payment instruction can be accepted for processing while the recipient still lacks usable funds. A payment can discharge only part of an obligation.

The financial question concerns the effect that actually obtains under the applicable arrangement. Its answer needs both the relevant institutional or contractual rule and adequate evidence of the event that satisfies its conditions.

### FDM.4:2 - Problem

A local completion label can be used to infer a wider result. That inference can leave a debt overstated, a payment falsely treated as available or a proposed agreement treated as effective.

The opposite error is to require physical cash movement for every financial change. Waiver, valid modification or another recognized act can change a position under its applicable rule. The method must recover the actual effect mechanism rather than select it from the action's label.

### FDM.4:3 - Forces

Operational systems need timely completion signals. Their signals have scopes and can arrive before or after the effect relevant to another participant. Several dates may therefore be useful.

Evidence can disagree because of timing, identity or meaning as well as an actual failed action. Resolving the discrepancy requires enough context to distinguish those explanations, without turning every routine completion into a full investigation.

### FDM.4:4 - Solution

#### FDM.4:4.1 - Name the claimed change and prior position

State what is supposed to have changed, for which party, under which arrangement and at what relevant time. Recover the prior position to the extent needed to explain the effect. FDM.1 supplies a missing position account; FDM.2 resolves an uncertain party boundary.

Distinguish a changed permission, duty, usable resource, recorded statement and business outcome. If a message says only “approved”, establish what its sender actually approved before treating it as evidence of another result.

#### FDM.4:4.2 - Recover the rule that gives the event its effect

Obtain the applicable terms or institutional rule. Identify the event or action the rule recognizes, the actor and authority where required, the conditions and the effective time. Some effects require a communicative act; others depend on performance or another recognized occurrence.

[FPF A.2.8][DUTY], [FPF A.2.8.PER][PER] and [FPF A.2.9][ACT] supply the respective duty, permission and communicative-work questions. Use the relevant specialist for disputed local terms. A record can be constitutive if the applicable rule gives the recording act that role.

#### FDM.4:4.3 - Establish what actually occurred

Inspect the evidence relevant to that rule and effect. Match the parties, arrangement, amount and occurrence. Distinguish an instruction from its execution and a provider's local result from the recipient's result where those differences matter.

Retain the dates needed to interpret the action: occurrence, effective date, posting or actual availability can differ. Obtain only the dates that can change the present answer. Evidence sufficient for “instruction received” may be insufficient for “recipient can use the funds”.

If sources disagree, first compare their subjects, dates and meanings. Then investigate the remaining factual discrepancy. Do not select a source as decisive merely because its application is the most familiar one.

#### FDM.4:4.4 - Derive the effect and remaining position

Apply the recovered rule to the established occurrence. State what changed and when. For a partial payment, use the applicable allocation rule to determine which amounts are satisfied and what remains. Preserve other interest, fees or conditions only where the actual arrangement requires them.

A scheduled transition that clears a forecast balance does not establish actual discharge. Use the receipt or other event recognized by the terms. FDM.3:5.2 shows how an established receipt updates principal and interest for the next calculation, while an instruction with unknown effect leaves alternative states.

Keep the calculation answerable to that interpretation. If you can perform the arithmetic but cannot explain how it establishes the financial position, use [FPF B.1.5.EW][EW] to locate the missing operation in the encompassing work. An unresolved contractual interpretation may need a qualified colleague's contribution; a computational correction addresses a different failure.

When the evidence establishes that the required event did not occur, return the supported non-change for that effect. When the rule or occurrence is unresolved, return the exact missing premise. An unresolved result is not proof of either performance or failure.

Relate the records to the resulting position. A necessary correction belongs in the appropriate account through its responsible process; do not silently rewrite history to make sources appear consistent. Use [ADM.4][ADM] when the participants' accounts require a broader comparison.

#### FDM.4:4.5 - Return the result needed by the next user

Supply the supported effect, time, remaining position and limits. Name the next responsible question when a rule, occurrence or correction still needs resolution.

FDM.3 uses the resulting state for later events. FDM.5 uses the effect when examining a participant's service result. A demonstrated financial change can be useful even when its longer-term benefit is not yet known.

### FDM.4:5 - Archetypal Grounding

#### FDM.4:5.1 - A payment, an instruction and a modification

In the constructed loan, 105 is due on day 30. Adequate evidence establishes a payment of 60 by the borrower to the lender. The supplied application rule applies all 60 to that due amount; there are no additional fees or interest. The resulting unpaid amount is **45**.

A servicing report still showing 105 unpaid disagrees with that established effect. The model returns the 45 position and the report discrepancy. It retains the original 105 contractual schedule and the actual 60 payment as distinct statements, rather than editing either into the other.

Now suppose the available evidence instead establishes only that the borrower sent a payment instruction for 60. The evidence does not yet establish the event that the supplied terms recognize as payment. The claimed reduction to 45 remains unresolved. The next question is whether that event occurred, not whether subtraction was performed correctly.

A separate pre-funding example has different effect conditions. A valid modification, made by the competent parties under supplied terms, changes a lender's conditional advance obligation before any money moves. The model follows that rule and its actual occurrence. It does not wait for disbursement to recognize every change.

These examples demonstrate reasoning under their supplied premises. Another instrument's payment-allocation, formation or modification rule can produce a different result.

#### FDM.4:5.2 - Deriving the position through an interpreted calculation

Consider a variant in which receipt of 60 is established, but the supplied terms classify it as refundable cash collateral. The terms leave the borrower's loan obligation of 105 unchanged. Subtracting 60 from 105 still produces 45 arithmetically, but does not describe the remaining loan obligation under these terms. The account instead retains the obligation of **105** and the separate collateral position.

While applying the contractual classification, the modeler is deriving the financial effect and constructing the position account. What the larger account must explain determines what the local calculation may claim. The earlier repayment example permits the subtraction; this collateral example does not. The banking receipt supplies an occurrence to interpret, rather than becoming part of the modeler's act of interpretation.

Someone who can calculate but cannot interpret the collateral terms needs to learn to interpret them or obtain an adequate interpretation from an appropriate specialist. Once the interpretation is adequate, the account can proceed without a fresh investigation of the already established receipt. If the terms later provide that collateral is applied to the debt, establish the event and effect under that changed condition before updating the obligation.

### FDM.4:6 - Bias-Annotation

A service team may equate its own successful step with the recipient's result. A financial reporter may give the latest posting more authority than its evidential meaning supports. Recover the effect and its rule before judging either account.

When the available sources cannot establish whether the event occurred, retain that uncertainty.

### FDM.4:7 - Conformance Checklist

For the effect being asserted, examine whether:

1. The affected party, prior position, claimed change and relevant time are clear.
2. The applicable rule and its action, authority or occurrence conditions are established where required.
3. Evidence supports the actual event at the scope claimed.
4. The derived effect and any residual obligation follow the applicable terms.
5. Records, effective relations and resource availability remain distinct where their differences matter.
6. The result distinguishes supported change, supported non-change and unresolved effect.

A calculation can verify the consequence of supplied premises. It cannot establish the missing event or institutional rule.

### FDM.4:8 - Common Anti-Patterns and How to Avoid Them

**Closing the obligation from a sent instruction.** Establish the event the applicable arrangement recognizes as performance.

**Treating all postings as either constitutive or merely descriptive.** Recover the actual rule and the role of the recording act in that arrangement.

**Using one date for every consequence.** Retain distinct occurrence, effect or availability dates when they change the receiving answer.

### FDM.4:9 - Consequences

The practitioner can explain what a financial action actually changed and what remains. Local system success no longer automatically becomes a broader completion claim.

The work can expose a missing rule, uncertain event or account correction. Resolving it may require another participant or specialist.

### FDM.4:10 - Architectural Rationale

The method joins a governing rule with an actual occurrence because neither alone establishes the particular effect. A generic term describes what would happen; an event description becomes financially meaningful through the applicable conditions.

A transaction log is sufficient when it already supplies adequate evidence for a settled effect rule. A broad business-outcome inquiry is unnecessary for a narrow residual-balance question. The wider inquiry becomes useful when someone claims the financial change itself established the participant's benefit.

### FDM.4:11 - SoTA-Echoing

The practice question is how to distinguish an actual financial effect from a decision, message or record. The method applies FPF's duty, permission and communicative-work distinctions to financial actions, with ADM.3 and ADM.9–10 supplying effectivity, usable provision and fulfillment questions.

This changes §§4.2–4.4: recover the effect rule, establish the occurrence and derive the remaining position. At the effort of examining one completion claim, it can distinguish “60 instructed” from “60 paid”, which a status-only reading conflates. More extensive investigation is justified when the unresolved premise changes the receiving use.

Actual local rules and event evidence govern an actual result. Reopen the account when either changes or when a later use requires a broader effect claim.

### FDM.4:12 - Relations

FDM.1–2 supply positions and parties. FDM.3 supplies contractual event logic and consumes the resulting actual state. FDM.5 uses the supported effect in a service-contribution account.

ADM.3, ADM.7–10 and the relevant financial practice supply effectivity, evidence, permission, usable provision and fulfillment questions at their own scope. A.2.8, A.2.8.PER and A.2.9 govern the underlying institutional distinctions.

### FDM.4:End
