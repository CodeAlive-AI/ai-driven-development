## ADM.10 - Reconcile Administrative Obligations, Performance and Records

**Type:** Architectural

**Status:** Stable

### ADM.10:0 - Use this when

Use this pattern when participants need to determine whether an administrative obligation was fulfilled, yet the obligation, actual performance and records do not line up clearly. A payment record may be closed while part of the credit remains unconfirmed; an access obligation may be recorded as fulfilled while the recipient could not use the permitted resource.

Start with the particular obligation and its applicable fulfillment rule, then compare the performance evidence and records for that same subject and time. The first useful result is a supported reconciliation, or the remaining discrepancy and competent next action.

Use a sufficient existing reconciliation directly. An isolated spelling correction with no effect on meaning does not require this inquiry. The pattern does not supply statutory accounting, tax, valuation, treasury or legal discharge rules; use the rule actually governing the obligation and obtain a qualified interpretation when that rule is unresolved.

### ADM.10:1 - Problem frame

The handler is comparing what one participant owed another, what actually happened and what the participants recorded. Those may be three different claims about related subjects. A record may describe an instruction, debit, credit, allocation or case closure; each can have a different effective or recording time.

The obligation's fulfillment condition must be known. Issuing an instruction, crediting a recipient, accepting a deliverable and making a resource usable can be different conditions. The handler cannot infer which condition discharges an obligation from the most convenient system status.

Participant-relative descriptions remain legitimate. A payer's outgoing payment and a recipient's incoming receipt can concern the same transfer. ADM.4 supplies their correspondence when needed; this pattern then determines what that event establishes about the particular obligation.

### ADM.10:2 - Problem

A handler compares two totals or status fields without establishing their meaning, scope or time. Apparent equality is then reported as settlement, or a harmless difference in recording time is treated as failed performance.

A handler may treat missing evidence as a reason to repeat a payment. The record says 400 remains, so someone instructs 400 again, although the earlier instruction may already have credited the recipient. Correcting the account requires recovering the event before changing the world.

### ADM.10:3 - Forces

| Force | Tension |
| --- | --- |
| Comparable claims | Common amounts and labels can conceal different events, quantities, purposes or periods. |
| Institutional effect | Actual performance matters under a supplied fulfillment rule; the handler cannot invent that rule. |
| Uncertain effect | Unconfirmed effect differs from known nonperformance and may prevent a safe repeat action. |
| Participant accounts | Several correct records can coexist while their correspondence needs to remain recoverable. |
| Corrective authority | A record correction, additional provision and change to an obligation can require different authority. |

### ADM.10:4 - Solution

#### ADM.10:4.1 - Fix the obligation and the question being answered

Identify who owes what to whom, for which subject, quantity or usable condition, purpose and relevant time. Recover the operative agreement, decision or rule and its actual fulfillment condition. Include a change, suspension, allocation or permitted offset only when it matters to this obligation.

State the receiving question: whether the obligation was fulfilled by a particular date, what is still established as outstanding, why two accounts differ, or which corrective action is now needed. A historical statement and a present payment decision may require different evidence.

If the fulfillment rule is unavailable or disputed, obtain its competent interpretation. A ledger label cannot supply the missing rule. Use ADM.3 for a material effective-time question.

#### ADM.10:4.2 - Align the claims before comparing them

Recover what each record asserts and what evidence supports actual performance. Establish event identity and participant correspondence through ADM.4 when needed. Use [SIE.4 through SIE.6][SIE] for an unresolved source-meaning or identity question.

Match quantities, units, direction, gross or net basis, allocation, observation time and coverage where those distinctions can change the conclusion. A debit from the payer and a credit to the recipient may be different observations of a transfer. Two identical amounts may instead belong to two different transfers.

[OPS.15][OPS] supplies comparison of observations for matching subjects and bases when that operational comparison is needed. It does not determine the obligation's fulfillment rule. Once the claims are adequately aligned, compare them directly without constructing an unnecessary shared database.

#### ADM.10:4.3 - Apply the fulfillment rule to established performance

Determine which evidenced effects satisfy which part of the obligation under the supplied rule. Keep the actual event, evidence of it and institutional consequence distinct. A later report can improve knowledge of an earlier credit without making the credit occur on the report date.

Distinguish at least the differences that change the next action:

| Difference | What must be resolved |
| --- | --- |
| Meaning or identity | Whether the records concern comparable claims about the same subject or event. |
| Time or coverage | Whether one account is earlier, later or covers a different interval or subset. |
| Quantity or condition | Whether established performance meets the amount or usable condition actually owed. |
| Authority or allocation | Whether the governing decision permits the claimed change, correction, offset or application. |
| Unknown effect | Whether an earlier action actually supplied any of the condition; missing evidence is not proof of nonperformance. |

A known fulfilled part and an uncertain remainder can coexist. Report each with its basis. Do not infer that a whole obligation is settled merely because the case record is closed, or that an uncertain remainder is definitely unpaid.

#### ADM.10:4.4 - Select the correction that matches the discrepancy

For a recording defect with adequate performance evidence, obtain the authorized correction and retain the needed connection to the original event and prior account. Correcting a description does not undo or repeat the historical action. If the governing rule gives a recording act a constitutive effect, apply that rule explicitly.

For established missing performance, identify the provider action and permission actually required to complete it. ADM.8 supplies a live permission inquiry; ADM.9 supplies provision. A handler authorized to edit a case record is not thereby authorized to issue payment or amend the obligation.

For an unknown earlier effect, first recover the same attempt through its competent provider. If the effect occurred, reconcile and correct the account. If it did not occur, use the applicable authorized continuation. If it remains unknown, preserve that uncertainty and the next recovery action before any repetition that could duplicate performance.

A dispute about the obligation or its interpretation returns through ADM.6 to its competent decision maker. The reconciliation cannot settle that dispute by choosing one participant's preferred record.

#### ADM.10:4.5 - Return the reconciled account and remaining action

Give the participants the bounded conclusion, material basis and any unresolved difference. Retain each participant's correct account and explain its correspondence where a common event is used.

A small case may finish with a short note: the named obligation was fulfilled by the confirmed effect at the relevant time, and the record has been corrected by the authorized handler. An unresolved case needs the precise missing claim, its competent recipient and the action that depends on it.

Reopen only the affected conclusion when new evidence, a corrected meaning, a valid changed obligation or a relevant effective-time fact arrives. Do not reopen unrelated reconciled cases merely because the same provider supplied the new information.

### ADM.10:5 - Archetypal Grounding

#### ADM.10:5.1 - One thousand owed, six hundred confirmed, four hundred unknown

Organization P owes supplier Q 1,000 units for invoice I. The supplied terms say that amounts credited to Q's designated account discharge the corresponding portion of this obligation. For this example there are no fees, offsets, other credits or changes to I.

Evidence confirms a 600-unit credit to that account. A second instruction for 400 units was issued, but its effect is unknown. The case record says “paid 1,000” because both instructions were sent.

The handler establishes that the confirmed 600 discharges that portion under the supplied terms. The second instruction establishes an attempted payment, not its credit. The remaining 400 has an unresolved effect; the available evidence does not establish whether the actual outstanding amount is now 400 or zero. The record's closed status cannot settle the question.

The handler uses the original second-attempt reference to ask the payment provider whether and when Q's account was credited. The possible returns have different consequences:

| Provider result | Reconciliation and next action |
| --- | --- |
| The 400 was credited to Q's designated account | The supplied terms establish full fulfillment. The authorized handler corrects the account or evidence linkage as needed; there is no remaining payment to issue. |
| The attempt failed without a credit | The available evidence establishes 400 still outstanding under the stated assumptions. The competent participants arrange the properly authorized remaining provision. |
| The effect still cannot be established | Retain the confirmed 600 and the 400-unit uncertainty. Continue the assigned effect inquiry before any potentially duplicate payment. |

Suppose the confirmed second credit occurred on 10 September but the provider's report arrived on 12 September. The event time remains 10 September. A report made on 11 September with only the earlier evidence should have stated uncertainty. The later evidence supports a better historical account, not a new credit on 12 September.

#### ADM.10:5.2 - Compare debit, credit and fee before deciding fulfillment

In a different case, P's account shows a 1,000-unit debit, while Q's account shows a 990-unit credit and a separate fee claim. Before inferring an unpaid balance, the handler establishes the event correspondence, quantity bases and actual fee allocation.

If the supplied terms require a net 1,000 credit to Q, the 990 credit alone does not establish full performance of that condition. If a different applicable term assigns the fee differently, its competent interpretation determines the institutional consequence. The two record totals cannot choose the term.

Likewise, a 1,000-unit receipt allocated to another invoice cannot automatically close I. The handler needs the actual allocation basis and authority before applying the receipt to this obligation.

### ADM.10:6 - Bias-Annotation

The most accessible ledger can appear to be the truth for every question. Inspect whether it records instructions, effects, obligations or a participant's classification before relying on it.

Financial examples make quantities visible, but administrative fulfillment can concern usable access or another condition. Do not force every such condition into a monetary balance. The pattern also does not equate one common event account with one mandatory database.

### ADM.10:7 - Conformance Checklist

**Recognition.** The result distinguishes the obligation, its fulfillment rule, evidenced performance and records. It states what is established, what remains uncertain and which correction or provision is actually needed.

**Assurance for reliance.** Trace the conclusion through actual event correspondence, comparable quantities and times, and the governing rule. Examine a missing-effect, changed-allocation or delayed-evidence case that could alter the next action. Verify that a record correction and any new provision use their own authority, and that uncertainty has not become an invented settlement or duplicate action.

### ADM.10:8 - Common Anti-Patterns and How to Avoid Them

**The ledger is closed, therefore the obligation is discharged** substitutes record status for the applicable fulfillment condition. Apply the rule to evidenced performance.

**The totals match, therefore the accounts agree** ignores gross/net basis, identity, allocation or time. Align the claims before comparing amounts.

**Unconfirmed means unpaid** turns missing evidence into an instruction to repeat. Recover the earlier effect and retain uncertainty until the result supports a continuation.

**Correcting history by changing the event** treats a revised account as another payment or a retroactive obligation change. Distinguish authorized description correction from actual provision and constitutive acts.

### ADM.10:9 - Consequences

Participants can see which portion of a claim is established, why apparently different accounts may both be correct and what work remains. Reconciliation can avoid duplicate provision and direct corrections to the person with the right authority.

The process depends on adequate event evidence and an applicable fulfillment rule. A precise unresolved account may be the only supportable result. Broader accounting correctness and operational effectiveness require their own qualified evidence.

### ADM.10:10 - Architectural Rationale

The obligation, performance and record have different change conditions. Their connection is established through event correspondence and the operative institutional rule. Keeping those conditions separate permits a later correction of knowledge without changing the event, and a legitimate additional action without treating every discrepancy as missing performance.

### ADM.10:11 - SoTA-Echoing

The working question is how to determine fulfillment across participant accounts without confusing instructions, effects and records. The July laboratory supplies the administrative problem. Use an account suited to the decision while preserving accounts needed for other purposes. Partridge and colleagues' [accounting][PARTRIDGE-A] and [agentology][PARTRIDGE-B] arguments support preserving participant-relative meanings around an established common subject.

The selected synthesis combines that representational contribution with the comparable-observation question in [OPS.15][OPS], the meaning and identity work in [SIE.4 through SIE.6][SIE], and the recovery of uncertain provider effects in [SYSE.26][SYSE]. The substantive fulfillment rule remains an explicit local input.

Direct matching of two records suffices when their semantics, coverage and evidence already support the requested conclusion. A universal ledger or wholesale ontology replacement adds no needed result to the worked cases. Sections 4.1–4.4 instead make the institutional rule and unresolved effect visible while retaining adequate existing records.

The 2018 representation arguments are conceptual sources, not current evidence that a particular accounting system is superior. Reopen the affected reconciliation when the obligation, source meaning, allocation, evidence or effective-time basis changes. A broader financial or accounting claim needs its qualified method and evidence.

### ADM.10:12 - Relations

ADM.3 supplies material effectivity distinctions; ADM.4 establishes participant-relative correspondence before this pattern determines what performance fulfills. ADM.7 supplies a missing claim check. ADM.8 establishes any needed permission, and the provider performs remaining provision through ADM.9. ADM.6 returns an unresolved substantive question to its competent source.

[SIE.4 through SIE.6][SIE] and [OPS.15][OPS] supply meaning, identity and observation comparison within their scopes. The handler uses those results under the actual fulfillment rule; none of those methods creates the obligation or authorizes payment merely by describing it.

### ADM.10:End
