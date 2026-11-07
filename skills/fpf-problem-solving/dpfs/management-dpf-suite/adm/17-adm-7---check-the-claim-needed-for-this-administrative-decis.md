## ADM.7 - Check the Claim Needed for This Administrative Decision

**Type:** Architectural

**Status:** Stable

### ADM.7:0 - Use this when

Use this pattern when an administrative action depends on a particular claim and the handler needs to establish whether available evidence adequately supports that claim for this use. Examples include an effective assignment, an expense's eligibility, the identity of the person requesting access or the effect of an earlier payment.

Start by writing the claim and the action that depends on it. The first useful result is a supported answer, a supported negative answer, or the missing evidence or competent check. Reuse a sufficient existing result within its conditions.

Do not run an additional check merely because a form has a field for it. A settled decision whose applicable rule requires no further check can use its established basis. This pattern applies an existing qualified check to a case; redesigning a control or inventing a specialist test is a separate task.

### ADM.7:1 - Problem frame

A handler, deciding person or provider is about to rely on a claim. The claim concerns an identified participant, event, relation, amount or condition at a relevant time. The governing service rule supplies the criterion where one is needed.

A check can establish different things: that a document came from its stated issuer, that a receipt concerns this expense, that a condition holds under a policy, or that a provider effect occurred. A successful check of one thing cannot silently answer another. An authentic assignment record can describe a future appointment; a successful credential operation can leave the person's eligibility unestablished.

The handler specifies and uses the needed result. The person or mechanism competent to perform the check supplies its evidence or judgment. Administrative responsibility for the case does not confer every specialist competence.

### ADM.7:2 - Problem

Administrative checks often follow available documents instead of the decision. Staff confirm that a file exists, a signature is valid or an automated service returned green, then treat that observation as proof of entitlement or completion.

Repeating all checks can also be harmful. It imposes burden without improving the answer, particularly when an adequate result already exists or when the checked fact cannot change the decision. Meanwhile, a consequential missing claim can remain hidden behind several successful but irrelevant checks.

### ADM.7:3 - Forces

| Force | Tension |
| --- | --- |
| Claim precision | A broad label such as “verified” is convenient but conceals what was actually established. |
| Proportionate effort | A wrong answer can matter greatly, while unnecessary checking delays legitimate work and collects avoidable information. |
| Reuse | A prior result may remain adequate, or may concern a different subject, rule, condition or time. |
| Competence | A general evidence account can expose a gap without supplying the qualified domain test. |
| Distinct outcomes | False, unsupported, inapplicable and unavailable can require different next actions. |

### ADM.7:4 - Solution

#### ADM.7:4.1 - State the claim and receiving action

Specify what needs to be true, for whom or what, under which relevant rule and time, and which action depends on the answer. Split a compound claim only when its components need different sources or can lead to different actions.

Ask what a wrong positive or negative answer would change. That consequence helps identify the applicable evidence requirement and any needed specialist contribution; it does not authorize the handler to invent a numerical confidence threshold.

For example, proving that a claimant has an effective assignment does not prove that a particular expense falls under it. Checking the expense's category does not establish that it has not already been reimbursed. Select only the claims actually required for the receiving action.

#### ADM.7:4.2 - Match available evidence to the claim

Recover an existing result before commissioning another check. Identify the actual subject, source, criterion, relevant time and stated limitations. Establish enough correspondence to know that the result concerns this person, expense, grant or provider attempt.

Distinguish the source's identity from the truth of its content. A signed record can support an origin claim while leaving scope, effective date or substantive correctness disputed. [FPF A.10][A10] supplies source recovery and bounded reliance when that account needs to remain inspectable; it does not perform the domain check.

Use ADM.3 for a live effective-time question and ADM.4 when participant accounts or cross-source identity prevent the match. Do not build a larger evidence record when the ordinary source and its conditions already answer the question.

#### ADM.7:4.3 - Reuse the result or perform the needed competent check

Reuse a result while its subject, criterion and action-changing conditions match the current use. Name the specific change that would defeat reuse: a different person, a revised policy, a revoked grant, an altered subject or a later time outside the result's scope.

When evidence is insufficient, select the qualified procedure or competent person that can answer the remaining question. A records custodian may recover a decision; the authorized specialist may interpret a rule; the payment provider may establish an attempt's effect. A new generic document request cannot replace any of these.

If a domain method is missing, return that method gap through ADM.6. If a separately required assurance claim is current, [FPF B.3][B3] supplies the argument about that exact claim and use. Consequence alone does not require constructing such an assurance claim.

#### ADM.7:4.4 - Preserve each action-changing outcome

Return the substantive result in ordinary language and retain distinctions the next action needs.

| Outcome | Meaning and continuation |
| --- | --- |
| The claim is supported for the stated use | The deciding person or handler may use that result under the applicable rule; the check itself does not grant permission or perform provision. |
| Evidence supports the negative condition | Apply the service rule's response to that established negative result. |
| The evidence is insufficient or conflicting | Preserve the unresolved claim and request the particular additional evidence or judgment needed. |
| The chosen check is inapplicable | Choose the check that actually answers the claim, or return the missing method; an irrelevant test supplies no positive or negative answer. |
| The check cannot currently be performed | Use an adequate existing result or separately permitted alternative if available; otherwise report the unavailable check and dependent action. |

An unavailable mechanism is a fact about checking, not a negative answer about the claimant. A policy may prescribe refusal or deferral when evidence is missing, but that disposition still differs from proof that the claim is false.

#### ADM.7:4.5 - Bind the result to the actual use

Return the claim, its answer, the material basis and any limitation that changes action. Add enough identity and timing to prevent substitution between check and use. If a payment instruction can change after approval, verify that the provider receives the approved amount and destination under the applicable procedure.

An observation that a condition held at one time does not by itself establish that it still holds when the result is used. [SYSE.28][SYSE] supplies the engineering question of where a check or enforcement mechanism must act when later changes can defeat it. Use an adequate existing control directly in a case; do not redesign its placement merely because a request arrived.

The consuming person then applies the governing rule or makes the required decision. Keep that decision and subsequent performance separate from the check. Reopen only a result affected by a material changed condition.

### ADM.7:5 - Archetypal Grounding

#### ADM.7:5.1 - An eligible expense, with one missing answer

Use the reimbursement policy P from ADM.5. Elena claims 200 units for travel on 10 September. P requires an effective relevant assignment, a receipt corresponding to an eligible business-travel expense, and no earlier reimbursement of the same expense. In this constructed case, P accepts the assigned manager's confirmation of business purpose.

The existing appointment decision covers Elena and the trip date. The handler reuses that temporal result. The receipt identifies Elena's actual journey and amount; the accepted manager confirmation supplies its business purpose. Those results support the corresponding eligibility claims without another appointment inquiry or purpose interview.

The payment log contains an earlier instruction for the same expense, but its effect is unknown. The missing claim is now precise: was that expense already reimbursed by this attempt? A bank or payment-provider effect inquiry can answer it. Another receipt upload cannot.

The provider confirms that the earlier instruction failed before any credit. That result supports the negative answer to “already reimbursed by this attempt”; the handler still checks the actual policy's required coverage of any other possible reimbursement. Suppose the adequate case records establish none. The finance approver can now make the required decision. The provider then performs any authorized payment. The check neither approved the claim nor paid it.

If the earlier effect remains unknown, the handler preserves that uncertainty. A potentially duplicate payment waits for recovery under ADM.9–ADM.10.

#### ADM.7:5.2 - The wrong test and an unavailable test

An archive requires an accepted person-identity result and a valid read grant. A device credential succeeds. That observation supports the device operation it actually checked; the handler cannot use it as the required person result or read grant.

If the person checker is unavailable, the outcome is unavailable checking. The existing approved alternative may supply a qualified person check through ADM.6. If the person check instead establishes that the person is different from the grant beneficiary, that is a substantive negative correspondence result, and the applicable service rule supplies the response.

These cases require different next actions despite each sometimes being displayed as “verification failed”.

### ADM.7:6 - Bias-Annotation

Available data and automated scores can dominate the question even when they concern convenient proxies. Start with the actual claim and inspect what the selected check can establish.

The pattern assumes access to applicable criteria and qualified sources. It cannot infer those from institutional prestige, a familiar interface or an applicant's ability to produce more documents. Additional collection should have an action-changing purpose and follow the actual information rules.

### ADM.7:7 - Conformance Checklist

**Recognition.** A reader can recover the claim, dependent action, applicable criterion, subject correspondence and substantive outcome. Existing adequate evidence has an explicit scope of reuse.

**Assurance for reliance.** Examine the actual source and check for this claim. Try a relevant subject substitution, changed effective time or unavailable-check case. Confirm that each produces the correct limitation or next action under the rule. Use the qualified domain procedure for consequential correctness; a well-filled evidence table alone cannot establish it.

### ADM.7:8 - Common Anti-Patterns and How to Avoid Them

**Green means eligible** substitutes a successful technical operation for the required institutional claim. State the property actually checked and recover the missing result.

**Unknown means false** turns unavailable evidence into an accusation or an incorrect case account. Preserve uncertainty while applying the policy's actual response to missing evidence.

**Check everything again** ignores adequate existing results. Recheck only a claim whose receiving use or relevant condition has changed.

### ADM.7:9 - Consequences

The handler can reduce irrelevant requests and direct missing-evidence work to the source that can answer it. Decisions receive more precise inputs, and a refusal can distinguish a failed condition from an unavailable check.

This may expose a previously hidden method or evidence gap. Identifying the gap does not establish the claim; it helps prevent unsupported permission, denial or duplicate action. Actual service observations are needed to establish the effect on errors and participant burden.

### ADM.7:10 - Architectural Rationale

The organizing relation is between one claim, its evidence and its receiving use. That relation allows a source result to be reused where it remains adequate and limited where it does not. Institutional decisions and provider actions retain their own conditions instead of being collapsed into a generic “verified” status.

### ADM.7:11 - SoTA-Echoing

The working question is how to check the administrative claim that matters to a particular decision without replacing it by an available proxy. The May laboratory's control-purpose problem supplies the domain failure. [FPF A.10][A10], especially §§4.1–4.2 and 4.5–4.6, supplies source and bounded-use recovery; [FPF B.3][B3] is retained only for an actual separately named assurance question.

The selected synthesis applies that evidence discipline with the actual reuse, outcome and change-before-use instructions in [SYSE.28][SYSE]. A generic checklist is an alternative: it suffices when its items already match the case claims and preserve consequential outcomes. It fails when one “pass/fail” field hides an inapplicable or unavailable check, which motivates §§4.1 and 4.4.

[NIST SP 800-63-4][NIST]'s separation of digital-identity functions supports the bounded identity example. It does not supply an expense rule or a universal permission test. The cases are constructed applications, not estimates of checking accuracy.

Reopen a result when its relevant subject, rule, evidence or use changes. Reopen the reusable checking design when actual failures show that the test cannot answer the claimed question or cannot protect the interval before reliance.

### ADM.7:12 - Relations

ADM.2–ADM.4 supply participant, relation, time and account correspondence when needed. The handler uses the check result in the actual permission or case decision; ADM.8 governs the permission question, and ADM.9 governs provision. An unavailable competent check returns through ADM.6.

ADM.10 uses effect evidence to reconcile an obligation and performance. [FPF A.10][A10] retains the source-to-use account; [FPF B.3][B3] addresses an actual assurance claim; [SYSE.28][SYSE] designs or repairs a check's placement when that separate question is live.

### ADM.7:End
