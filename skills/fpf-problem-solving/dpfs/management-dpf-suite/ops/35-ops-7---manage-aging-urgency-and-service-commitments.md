## OPS.7 - Manage Aging, Urgency, and Service Commitments

> **Status:** Stable


### OPS.7:0 - Use This When

**Use this when** further delay could affect an operating result, or a recipient needs to establish the priority or service terms already in force. For the current terms, identify the decision or rule that made them effective for this case. To decide how to respond to a possible delay, identify what further waiting would change, how much time is available and who may take the required action.

State the result for the particular subject and coordination decision.

> Identify the subject and the decision needed. When the choice depends on the consequences of delay, establish those consequences. For a priority choice, give the order that is justified and who may set it. For a question about the terms already in force, return those terms with the action or rule that made them effective. Include any further coordination, notification or review required for the commissioned use.

One System may hold both authorities. If a required authority is missing, identify which decision must wait.

An approaching deadline or a disputed priority can make this method relevant. To rely on a claim about a deadline already in force, establish the applicable terms and when they took effect. To change a priority or revise a promise, establish the consequences of the proposed change and who may authorize it. Obtain any specialist decision the action requires.

Use `OPS.8`–`OPS.13` for wider queue, constraint, capacity and service-commitment questions, and `OPS.18` for operating quality and reliability. Clinical triage and release require their own authoritative decisions. Use `C.27` for an intervention-sensitive claim about a change in rate, rhythm, recovery or regime.

#### OPS.7:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| exact subject or case | The incident, patient case, user issue, release candidate, service relation, request, or other subject whose temporal and consequence claims matter. A queue item or record may refer to this subject. |
| state claim | A qualified claim about the subject and relevant relations at a stated time or horizon. |
| age | Elapsed time since a defined event for an exact subject under a stated clock and conditions. Age is not urgency, priority, or rank. |
| time remaining | The interval between the current reference time and one relevant horizon under stated assumptions. A deadline alone creates no permission. |
| rate or trend | A relation concerning change per interval or a supported direction across observations. Attributing the change to an intervention requires evidence for the connection. |
| intervention-sensitive temporal claim | A claim that an intervention changes a rate, rhythm, recovery, inertia, or regime. It requires the stronger discipline of `C.27`. |
| urgency | A decision-relative judgement that delay can change a named consequence, commitment, risk, recoverability, or supported use. |
| priority | A current relation used for one coordination decision. It may inform but does not automatically equal queue position, admission order, clinical triage, economic value, authority, or service promise. |
| queue rank | A position under one queue policy and unit definition. Use rank here when the decision depends on the queue policy. |
| bounded commitment | An existing promise or obligation with parties, result or service, conditions, horizon, authority, and current status. |
| commitment disposition | Preserve, clarify, renegotiate, or withdraw an existing bounded commitment under the applicable authority and conditions. |
| whole-service commitment account | A wider account relating demand, resources, capability, uncertainty, service outcomes, and credible promises. Use `OPS.13` to develop that account. |
| priority-and-commitment result | The current priority disposition and reason, the status of any affected commitment and any authorized change, immediate coordination action or blocker, parties, horizon, evidence, and next review. |

### OPS.7:1 - Problem Frame

Time matters in operations because delay can alter consequences, commitments, dependencies, recoverability, and the usefulness of later action. Yet the same elapsed time can mean different things for an incident, patient, release candidate, provider change, user issue, maintenance condition, or administrative request.

Decide what the temporal evidence supports for the operating question. It may justify retaining or changing the current priority. If a promise is affected, identify what remains supportable and who may change it.

### OPS.7:2 - Problem

Age dashboards and escalation scores compress distinct claims. The oldest item appears most urgent; urgency appears to dictate queue position; a missed horizon appears to authorize release, treatment, staffing, or spending; and one local reprioritization appears to settle a system-wide service promise.

The opposite failure treats time as display-only. Practitioners notice age or deterioration but do not connect it to consequence, recovery burden, dependency, affected parties, existing commitment, authority, or next review. Avoidable delay then becomes visible only after a promise or protected condition has failed.

### OPS.7:3 - Forces

| Force | Tension |
| --- | --- |
| simple age signal versus decision relevance | Age is inexpensive to compute. What further delay means for the case and its commitments depends on the subject, conditions and horizon. |
| fast escalation versus authority | Delay can demand attention, but priority and commitment changes require their respective authorized Systems. |
| local coordination versus system policy | One priority disposition can change immediate Work without designing queue order, capacity, constraint, or whole-service promises. |
| current evidence versus forecast | Deterioration, delay cost, and recovery burden may be uncertain; unsupported projections should not become urgency facts. |
| fairness versus unlike consequences | A common waiting rule can be legible, while clinical, safety, service, economic, and recovery consequences remain unlike and separately governed. |
| preserving promises versus truthful renegotiation | Keeping a commitment can matter, but hiding infeasibility harms affected parties and later recovery. |
| measurement versus intervention claim | State, age, rate, and trend can be observed directly; claimed intervention effects require stronger temporal and causal discipline. |

### OPS.7:4 - Solution

#### OPS.7:4.1 - Recover the exact subject, state, and existing commitment

Name the exact subject or case, its current qualified state, configuration and horizon, and any relevant existing commitment. For that commitment, record the parties, promised result or service, conditions, horizon, authority, current status, and evidence limits. If no such commitment exists, do not create one by calling a target, service label, or desired date a promise.

Use a progressed state or unmet condition from `OPS.6` while it applies to this decision. An authorized participant decides whether those facts warrant retaining or revising priority or a commitment.

#### OPS.7:4.2 - Qualify the temporal claim before interpreting it

State the defining event, clock, observation time, horizon, and conditions. Decide whether the claim is current state, age, time remaining, rate, trend, or an intervention-sensitive temporal claim. Use `C.27` only when an intervention is claimed to change rate, rhythm, recovery, inertia, or regime; keep the `C.27.TA` time-window, cadence, and currentness discipline for all temporal uses.

#### OPS.7:4.3 - Relate time to the decision-bearing consequences

Identify what bears on this decision or its grounds. Consider the promised service, dependencies, risk, consequences of delay, reversibility, recovery work, affected parties, evidence limits and the basis of comparison. If a proposed inquiry could improve the answer in time to matter, compare that benefit with its cost. Use qualified clinical, safety, legal, security, financial or other specialist results where needed.

Relate the remaining useful interval to the whole response: detecting the change, reaching a decision, obtaining any required agreement, and performing or communicating the remedy. Use the supported response account in `OPS.13:4.4`–`OPS.13:4.5`. An alert may arrive after the change was detected. Allow for that delay and the work still needed to respond.

Age alone does not prove urgency. Express urgency as “delay can change `X` for decision `Y` under evidence `Z`”, or leave it unsupported.

#### OPS.7:4.4 - Separate priority authority from commitment authority

When the work includes setting priority, establish who may set it. For a proposed change in commitment, identify who can make that change effective. For an inquiry about the date already in force, the agreement and its application to that order can give the answer. A coordinator may have one authority but not the other. Rank, expertise, responsibility, impact, and visibility grant neither by themselves.

#### OPS.7:4.5 - Decide the bounded dispositions

For priority, preserve, raise, or lower it only when current evidence is sufficient and the decision is authorized; state the reason and intended coordination use. If the decision cannot be made, name the unresolved priority question, its intended recipient, and the condition for resuming the decision.

For an existing commitment, preserve it when support and conditions remain adequate; otherwise trigger authorized clarification, renegotiation, or withdrawal. When escalation or specialist return is needed, send the unresolved priority or commitment question to the participant with the relevant authority and state the decision expected from that participant. Include each unresolved question in the immediate coordination action or truthful blocker recorded in `OPS.7:4.6`.

A proposal to revise a promise is not the revised promise. Keep the old obligation and its current risk visible while the required parties decide; record the effective agreement, refusal or unresolved response. If continued fulfilment is no longer possible, report that fact through the authorized relation without silently substituting a new date. Apply any existing withdrawal or emergency rule on its own authority.

Use `C.11` only where several real admissible dispositions need comparison. Use a bounded probe when its attainable result could improve the disposition or its grounds enough to justify the work before the relevant horizon.

#### OPS.7:4.6 - State immediate action, parties, horizon, and review

Return the decision the recipient needs, the period it covers and the grounds on which it can be used. Where coordination work follows, identify the relevant action, parties and conditions for review. Provide required notifications under the applicable arrangement. To report that a notice was received, establish the receipt the terms call for.

Choose the review time early enough that a discovered adverse condition can still receive a useful response. When supported durations are additive, subtract their total from the latest useful action time, then allow for uncertainty; when they overlap or vary, use the applicable response model instead. If no useful interval remains, act or return the blocker now rather than schedule a review after the consequence.

#### OPS.7:4.7 - Return wider policy and specialist questions

Return a shared queue, constraint, capacity or service-design question to `OPS.8`–`OPS.13`, and a quality/reliability response to `OPS.18`. Use applicable clinical, legal, safety or release decisions within their terms. Refer any outstanding decision to the party with the relevant authority.

### OPS.7:5 - Archetypal Grounding — Three Aging and Commitment Replays

#### OPS.7:5.1 - PumpWorks incident and release horizon

Continue the constructed matter in OPS.5:5.1 and OPS.6:5.1. At 09:30, I73 is one hour old from its 08:30 opening, while R42 has awaited its final evidence for 36 hours. I73's age is lower, but the field representative is available from 10:00 to 11:00 and has confirmed the required permission for observational live verification; losing that contact would prevent the planned verification today. R42's current promise is an authorized evidenced-release package to the service recipient by 17:00, conditional on the stated safety and field checks. Lab validation alone cannot fulfil it.

The representative needs the decided response before contact closes at 11:00. For this incident, the supplied response estimate is 20 minutes for live verification, 10 for the authorized decision and 10 for communicating its result: 40 minutes in sequence. The latest review that leaves that response possible is 10:20. The incident lead chooses 10:00 to retain 20 minutes of margin for the stated uncertainty. The priority authority gives the incident contact action precedence over the older provider-preparation package; the resource owner retains the active-work limit. This priority leaves R42-T9's independently permitted 09:40 laboratory start unchanged.

At 09:50 the field representative reports loss of access, with the earliest supported replacement contact at 09:00 next day. The lead acts immediately instead of waiting for 10:00: live verification is blocked, the customer liaison sends a truthful partial-result notice by 10:00, and the service owner checks the consequence for R42. The 10:10 laboratory result still counts for its test, and the captured incident discrepancy remains established.

The incident lead can change diagnostic priority but cannot change the customer's promise. At 10:05 the service owner, who has that authority, proposes delivery by 10:00 next day, on the supplied replacement-contact reservation, remaining safety decision and one-hour completion-and-return allowance confirmed by their owners. The recipient has not yet agreed: the old 17:00 obligation remains visible as at risk, and the proposed date is labelled a proposal. At 10:20 the authorized recipient explicitly accepts the changed conditional result and date; the service owner records the agreement and sends it to the affected performers. Only then is the commitment revised. A refusal would have left the old obligation and an unresolved authorized service decision, not licensed a local date edit.

The return contains the priority actually applied, partial result and live-access blocker, effective revised promise, conditions still open and next review at 08:30 next day. The owners supply a ten-minute allowance to obtain current contact/permission confirmation and any already-produced safety result, ten minutes to decide and communicate which 09:00 work may start and whether the conditional 10:00 promise remains supportable, and ten minutes of contingency. Thus 08:30 + 10 + 10 + 10 minutes reaches 09:00. This is time to recover and use a qualified result, not an allowance for inventing a safety verdict. If the result or contact remains unavailable at 08:40, return that exact blocker while a service decision is still possible. A missing safety result blocks reliance on the release promise; observational work can continue when its own permission and inputs hold. Lost contact blocks live verification without erasing the completed laboratory result. A newly lost condition reopens the response immediately. P8-P retains its 13:00 reconsideration, and neither agreement nor priority grants field-release or safety authority.

#### OPS.7:5.2 - Public-hospital waiting and deterioration

One clinical case has a defined waiting age, current observations, possible deterioration evidence, dependencies on clinicians, beds and other resources, a service horizon, affected patient and care participants, and explicit clinical and operating authorities. OPS.7 makes those relations available to the authorized priority and commitment decision.

The qualified clinical service uses its clinical evidence and authority to determine triage and treatment. Use the waiting and deterioration evidence for the operating priority decision and any needed return to the holder of a service commitment. Use a qualified result for a dependent question of queue design, staffing, capacity, consent, privacy, medical safety, statutory permission, treatment efficacy or patient outcome. Refer any consequential gap to the competent source.

#### OPS.7:5.3 - AI-assisted software issue and service promise

One user issue has an exact age and state, user and service consequence, dependency on tool or model access, current trace and test evidence, integration load, recovery burden, bounded concurrency, and a promised horizon. Assess what further delay would change for the user or service, using the evidence behind any severity score.

The authorized System may revise the issue's coordination priority or trigger an authorized commitment renegotiation, with an immediate check, integration action, fallback, or stop and next review. Use the evidence and authority for any dependent technical, release or fulfilment claim.

### OPS.7:6 - Bias-Annotation

| Bias or pressure | How it distorts temporal decisions | Countermeasure |
| --- | --- | --- |
| age-equals-urgency bias | Elapsed time substitutes for consequence and decision context. | Relate delay to one named risk, commitment, dependency, recovery, or supported use. |
| score reification | A severity or priority number appears to be an objective property. | Recover the comparison basis, intended coordination use, evidence, and authority. |
| deadline authority | A date is treated as permission to release, treat, spend, or bypass a condition. | Keep commitment horizon, priority, and specialist permission separate. |
| queue-rank collapse | Current priority becomes one universal queue position. | Bound the disposition and return queue policy to its owner. |
| commitment-preservation bias | An earlier promise is preserved despite unsupported conditions. | Revalidate parties, content, conditions, horizon, authority, and feasibility evidence. |
| local-to-system overreach | One reprioritization is reported as a service-wide promise or capacity result. | State the local result and return to `OPS.13` or the wider owner. |
| intervention-story bias | A change in rate or recovery is attributed to the chosen action without adequate temporal support. | Apply `C.27` only to the intervention-sensitive claim and preserve evidence limits. |

### OPS.7:7 - Conformance Checklist

- [ ] The exact subject or case, qualified state, configuration, and horizon are named.
- [ ] For any relevant existing commitment, the account gives parties, content, conditions, horizon, authority, status, and evidence limits.
- [ ] Any `OPS.6` result is used as evidence only at the matching configuration and horizon.
- [ ] State, age, time remaining, rate, trend, and intervention-sensitive temporal claims are distinguished.
- [ ] `C.27` is used only for an intervention-sensitive rate, rhythm, recovery, inertia, or regime claim.
- [ ] Urgency names the consequence, commitment, risk, recovery, or supported use that delay can change.
- [ ] Priority, queue rank, clinical triage, economic value, permission, and commitment remain distinct.
- [ ] For a decision to set priority or revise a commitment, identify the authority required for that act. Check the applicable terms for an inquiry into an existing commitment.
- [ ] When the decision requires comparing options, the comparison and any further inquiry it warrants are explicit.
- [ ] The result answers the question about priority, delay or commitment that the recipient brought, with enough evidence for its use. Return any other action still required under the terms.
- [ ] Any wider policy, service or specialist question has a usable return to the participant who can answer it.

### OPS.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| oldest first by nature | Age becomes a universal priority rule. | State the subject, consequence, commitment, comparison basis, and policy owner. |
| urgency score as fact | A representation hides assumptions, evidence, and receiving use. | Reconstruct the decision-relative claim and uncertainty. |
| deadline grants permission | Commitment pressure bypasses clinical, safety, legal, security, or release authority. | Keep horizon, priority, and permission as separate results. |
| local escalation becomes queue policy | One disposition silently reorders every item. | Bound the coordination result and return the queue decision. |
| promise by label | A service target or desired date is treated as an obtaining commitment. | Recover parties, content, conditions, authority, and status. |
| record change becomes stakeholder agreement | A revised field is treated as renegotiation or receipt. | Use the established commitment and communication relations and preserve evidence of acceptance. |
| temporal overanalysis | Ordinary age or rate triggers unnecessary dynamics modelling. | State the event, interval and clock. Use `C.27` only when the intervention-sensitive claim is current. |

### OPS.7:9 - Consequences

Practitioners can identify the last useful response time. If that time has passed, they can report which response is no longer possible and consider any alternative. They can explain the grounds for retaining or changing priority, what happened to any affected commitment, who held each authority, which parties are affected and when to review the result.

The cost is obtaining the consequence and authority information that one convenient age score omits. Some cases must return to another decision owner before their priority or promise can change; actual fulfilment is observed later.

### OPS.7:10 - Rationale

Age is broadly observable, but urgency depends on what delay changes; priority depends on one coordination use; and commitment alteration depends on parties, conditions, and authority. Keeping these relations separate prevents time pressure from becoming unearned permission.

Practitioners can preserve or revise priority for the subject of the operating decision and the terms of an affected commitment without waiting for a complete queue, capacity, or service-design account. Explicit returns keep queue, buffer, constraint, capacity, service-design, whole-service commitment, and specialist questions with their governing patterns or competent participants.

### OPS.7:11 - SoTA-Echoing

The question is how a temporal change alters present action and an existing promise. Competent flow practice already compares consequences, not just age. The [Open Guide to Kanban, July 2025, prioritization appendix](https://kanbanguides.org/open-guide-to-kanban/2025.7/) discusses service classes, delay-cost rates, cumulative delay cost and opportunity cost, with cautions about uncertain estimates and reprioritizing started work. Reinertsen's historical economic-flow treatment and TameFlow's commitment and signal reasoning supply related mechanisms. OPS adopts that consequential comparison.

For section 5.1, a capable fixed-date or expedite policy can already prefer the younger incident because the field-contact opportunity expires. Both approaches can preserve the ongoing laboratory work rather than interrupt it. The residual OPS contribution is the connection between unlike clocks, the remaining whole response, and the distinct authority to change the promise. A local severity or queue decision cannot make the proposed next-day date effective. Sections 4.3–4.6 keep the 17:00 obligation visible until agreement and select a review early enough for action; the case shows the adverse change before that review and the actual agreement afterward.

If the incumbent service policy already records the response window, the affected recipients and effective agreement, use it unchanged. The additional burden otherwise is estimating the relevant response, obtaining the missing authorized decision and maintaining the applicable promise. Those calls and confirmations consume time too; include them in feasibility and prefer a direct rule when it settles the matter. No precise score compensates for absent safety, clinical or legal authority.

FPF `C.27.TA` qualifies event, interval and currentness claims; `C.27` applies only to a consequential intervention-sensitive temporal claim. DEMO's commitment distinctions help inspect parties and agreement without assigning their authority. OPS.13 supplies service-level support and response construction. Reopen when consequence, required response, parties or agreement conditions change, or an incumbent achieves the same action and truthful promise account at lower total effort.

### OPS.7:12 - Relations

- Use the progressed state or unmet condition from `OPS.6` when it applies to the configuration and horizon and bears on priority, a commitment or the grounds for retaining either. Establish authority for changing priority or changing a promise separately.
- `C.27.TA` governs temporal aspect, window, cadence, and currentness. `C.27` governs intervention-sensitive rate, rhythm, recovery, inertia, or regime claims; neither supplies Operations priority or authority.
- `C.11` governs comparison only when several admissible live dispositions require choice. `A.10` governs evidence reliance.
- `OPS.5` retains admission and explicit-start conditions. A current priority relation neither admits demand nor establishes start permission or Work.
- `OPS.8`–`OPS.11` retain queue, buffer, constraint, capacity, variability, and interacting-structure decisions. `OPS.13` retains the credible whole-service commitment account. `OPS.18` retains operating quality and reliability questions.
- Clinical triage, consent, medical safety, law, privacy, security, finance, product assurance, release, provider authority, and other specialist results remain with their direct owners.
- Enter `OPS.7` directly when you need a decision about timing and priority or an affected commitment. Use the evidence and authority already available, or identify what is missing. Reapply the method when conditions change. A particular episode may require neither `OPS.5` nor `OPS.6`.

### OPS.7:End
