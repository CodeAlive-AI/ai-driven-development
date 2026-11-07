## OPS.7 - Manage Aging, Urgency, and Service Commitments

> **Status:** Stable


### OPS.7:0 - Use This When

Use this pattern when age, time remaining, a promised horizon, dependency change, new risk or consequence evidence, a progressed case state, or an unmet condition can change current priority or an existing bounded operating commitment. Typical cues are “this is old, so put it first”, “the deadline means we must release”, “the queue score escalated it”, “the patient has waited longest”, or “the issue is urgent” without a named consequence, authority, commitment, or decision horizon.

The first useful result is one bounded priority-and-commitment disposition:

> For exact subject or case `S` in qualified state `Q`, temporal claim `T`, existing commitment `C` with parties, conditions, horizon, and commitment authority `A_C`, and decision-bearing dependency, risk, consequence, recovery, and evidence `E`, current priority is `P` for coordination use `U` under priority authority `A_P`; commitment disposition is `K` when it changes; immediate coordination action or truthful blocker is `N`; affected parties, effective horizon, evidence limits, and next review are explicit.

Name the Systems holding `A_P` and `A_C`; the same System may hold both. Record any missing required authority in blocker `N`.

Recognition asks whether delay can change this decision. Assurance needs the temporal evidence, consequence and the distinct authority for priority, promise revision and any specialist action.

Do not use OPS.7 to sort every queue by age, create a universal urgency scale, identify the current constraint, size capacity, design service levels, perform clinical triage, authorize release, or establish a credible whole-service commitment account. Return those results to `OPS.8`–`OPS.13`, `OPS.18`, or their specialist owners. Use `C.27` only when the claim concerns intervention-sensitive rate, rhythm, recovery, or regime change; ordinary state, age, rate, or trend readings do not require it.

#### OPS.7:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| exact subject or case | The incident, patient case, user issue, release candidate, service relation, request, or other subject whose temporal and consequence claims matter. It is not automatically the queue item or record. |
| state claim | A qualified claim about the subject and relevant relations at a stated time or horizon. |
| age | Elapsed time since a defined event for an exact subject under a stated clock and conditions. Age is not urgency, priority, or rank. |
| time remaining | The interval between the current reference time and one relevant horizon under stated assumptions. A deadline alone creates no permission. |
| rate or trend | A relation concerning change per interval or a supported direction across observations. It is not an intervention effect by default. |
| intervention-sensitive temporal claim | A claim that an intervention changes a rate, rhythm, recovery, inertia, or regime. It requires the stronger discipline of `C.27`. |
| urgency | A decision-relative judgement that delay can change a named consequence, commitment, risk, recoverability, or supported use. It is not a durable kind or scalar by default. |
| priority | A current relation used for one coordination decision. It may inform but does not automatically equal queue position, admission order, clinical triage, economic value, authority, or service promise. |
| queue rank | A position under one queue policy and unit definition. It is not the universal expression of priority and can remain outside this pattern. |
| bounded commitment | An existing promise or obligation with parties, result or service, conditions, horizon, authority, and current status. |
| commitment disposition | Preserve, clarify, renegotiate, or withdraw an existing bounded commitment under the applicable authority and conditions. |
| whole-service commitment account | A wider account relating demand, resources, capability, uncertainty, service outcomes, and credible promises. It remains with `OPS.13`, not OPS.7. |
| priority-and-commitment result | The current priority disposition and reason, changed commitment disposition where authorized, immediate coordination action or blocker, parties, horizon, evidence, and next review. |

### OPS.7:1 - Problem Frame

Time matters in operations because delay can alter consequences, commitments, dependencies, recoverability, and the usefulness of later action. Yet the same elapsed time can mean different things for an incident, patient, release candidate, provider change, user issue, maintenance condition, or administrative request.

The practical problem is to make the temporal claim decision-bearing without converting it into automatic urgency, rank, or authority. The operation needs a current disposition that can preserve or revise priority and, where authority exists, maintain or change one bounded existing commitment.

### OPS.7:2 - Problem

Age dashboards and escalation scores compress distinct claims. The oldest item appears most urgent; urgency appears to dictate queue position; a missed horizon appears to authorize release, treatment, staffing, or spending; and one local reprioritization appears to settle a system-wide service promise.

The opposite failure treats time as display-only. Practitioners notice age or deterioration but do not connect it to consequence, recovery burden, dependency, affected parties, existing commitment, authority, or next review. Avoidable delay then becomes visible only after a promise or protected condition has failed.

### OPS.7:3 - Forces

| Force | Tension |
| --- | --- |
| simple age signal versus decision relevance | Age is cheap to compute, while consequence and commitment meaning depends on subject, conditions, and horizon. |
| fast escalation versus authority | Delay can demand attention, but priority and commitment changes require their respective authorized Systems. |
| local coordination versus system policy | One priority disposition can change immediate Work without designing queue order, capacity, constraint, or whole-service promises. |
| current evidence versus forecast | Deterioration, delay cost, and recovery burden may be uncertain; unsupported projections should not become urgency facts. |
| fairness versus unlike consequences | A common waiting rule can be legible, while clinical, safety, service, economic, and recovery consequences remain unlike and separately governed. |
| preserving promises versus truthful renegotiation | Keeping a commitment can matter, but hiding infeasibility harms affected parties and later recovery. |
| measurement versus intervention claim | State, age, rate, and trend can be observed directly; claimed intervention effects require stronger temporal and causal discipline. |

### OPS.7:4 - Solution

#### OPS.7:4.1 - Recover the exact subject, state, and existing commitment

Name the exact subject or case, its current qualified state, configuration and horizon, and the existing bounded commitment. Record the commitment's parties, promised result or service, conditions, horizon, authority, current status, and evidence limits. If no such commitment exists, do not create one by calling a target, service label, or desired date a promise.

Treat a matching `OPS.6` progressed state or unmet condition as evidence input only where it remains current for this decision. It neither authorizes nor entails priority or commitment revision.

#### OPS.7:4.2 - Qualify the temporal claim before interpreting it

State the defining event, clock, observation time, horizon, and conditions. Decide whether the claim is current state, age, time remaining, rate, trend, or an intervention-sensitive temporal claim. Keep ordinary readings ordinary. Use `C.27` only when an intervention is claimed to change rate, rhythm, recovery, inertia, or regime; keep the `C.27.TA` time-window, cadence, and currentness discipline for all temporal uses.

#### OPS.7:4.3 - Relate time to the decision-bearing consequences

Recover only what can change this decision: promised service, dependency state, risk, consequence of further delay, reversibility, recovery burden, affected parties, evidence and uncertainty, current comparison basis, and any feasible probe that could still reverse the result. Name clinical, safety, legal, security, financial, or other specialist claims without replacing their owners.

Relate the remaining useful interval to the whole response: detecting the change, reaching a decision, obtaining any required agreement, and performing or communicating the remedy. Use the supported response account in `OPS.13:4.4`–`OPS.13:4.5`; do not infer a feasible response from an alert alone.

Age alone does not prove urgency. Express urgency as “delay can change `X` for decision `Y` under evidence `Z`”, or leave it unsupported.

#### OPS.7:4.4 - Separate priority authority from commitment authority

Name the System authorized to maintain or change priority for the selected coordination use. Separately name the System authorized to preserve, renegotiate, withdraw, or otherwise alter the existing commitment. A coordinator may have one authority but not the other. Rank, expertise, responsibility, impact, and visibility grant neither by themselves.

#### OPS.7:4.5 - Decide the bounded dispositions

For priority, preserve, raise, or lower it only when current evidence is sufficient and the decision is authorized; state the reason and intended coordination use. If the decision cannot be made, name the unresolved priority question, its intended recipient, and the condition for resuming the decision.

For the commitment, preserve it when support and conditions remain adequate; otherwise trigger authorized clarification, renegotiation, or withdrawal. When escalation or specialist return is needed, send the unresolved priority or commitment question to the participant with the relevant authority and state the decision expected from that participant. Include each unresolved question in the immediate coordination action or truthful blocker recorded in `OPS.7:4.6`.

A proposal to revise a promise is not the revised promise. Keep the old obligation and its current risk visible while the required parties decide; record the effective agreement, refusal or unresolved response. If continued fulfilment is no longer possible, report that fact through the authorized relation without silently substituting a new date. Apply any existing withdrawal or emergency rule on its own authority.

Use `C.11` only where several real admissible dispositions need comparison. A bounded probe is suitable only when it can change the disposition before the relevant horizon.

#### OPS.7:4.6 - State immediate action, parties, horizon, and review

Record the current priority disposition, commitment disposition when one changes, immediate coordination action or truthful blocker, affected parties, effective horizon, supporting evidence and uncertainty, and next review or reopen trigger. Notify or coordinate with affected parties through the established relation; this pattern does not invent notification authority or prove receipt.

Choose the review time early enough that a discovered adverse condition can still receive a useful response. When supported durations are additive, subtract their total from the latest useful action time, then allow for uncertainty; when they overlap or vary, use the applicable response model instead. If no useful interval remains, act or return the blocker now rather than schedule a review after the consequence.

#### OPS.7:4.7 - Return wider policy and specialist questions

Return a shared queue, constraint, capacity or service-design question to `OPS.8`–`OPS.13`, and a quality/reliability response to `OPS.18`. Obtain clinical, legal, safety or release decisions from their competent owners; a local priority disposition supplies none of their authority.

### OPS.7:5 - Archetypal Grounding — Three Aging and Commitment Replays

#### OPS.7:5.1 - PumpWorks incident and release horizon

Continue the constructed matter in OPS.5:5.1 and OPS.6:5.1. At 09:30, I73 is one hour old from its 08:30 opening, while R42 has awaited its final evidence for 36 hours. I73's age is lower, but the field representative is available from 10:00 to 11:00 and has confirmed the required permission for observational live verification; losing that contact would prevent the planned verification today. R42's current promise is an authorized evidenced-release package to the service recipient by 17:00, conditional on the stated safety and field checks. Lab validation alone cannot fulfil it.

The representative needs the decided response before contact closes at 11:00. For this incident, the supplied response estimate is 20 minutes for live verification, 10 for the authorized decision and 10 for communicating its result: 40 minutes in sequence. The latest review that leaves that response possible is 10:20. The incident lead chooses 10:00 to retain 20 minutes of margin for the stated uncertainty. This is a case-specific planning bound, not a probabilistic service guarantee. The priority authority gives the incident contact action precedence over the older provider-preparation package; the resource owner retains the active-work limit. This priority leaves R42-T9's independently permitted 09:40 laboratory start unchanged.

At 09:50 the field representative reports loss of access, with the earliest supported replacement contact at 09:00 next day. The lead acts immediately instead of waiting for 10:00: live verification is blocked, the customer liaison sends a truthful partial-result notice by 10:00, and the service owner checks the consequence for R42. No unsupported field correction or fulfilment is reported. The 10:10 laboratory result still counts for its test, and the captured incident discrepancy remains established.

The incident lead can change diagnostic priority but cannot change the customer's promise. At 10:05 the service owner, who has that authority, proposes delivery by 10:00 next day, on the supplied replacement-contact reservation, remaining safety decision and one-hour completion-and-return allowance confirmed by their owners. The recipient has not yet agreed: the old 17:00 obligation remains visible as at risk, and the proposed date is labelled a proposal. At 10:20 the authorized recipient explicitly accepts the changed conditional result and date; the service owner records the agreement and sends it to the affected performers. Only then is the commitment revised. A refusal would have left the old obligation and an unresolved authorized service decision, not licensed a local date edit.

The return contains the priority actually applied, partial result and live-access blocker, effective revised promise, conditions still open and next review at 08:30 next day. The owners supply a ten-minute allowance to obtain current contact/permission confirmation and any already-produced safety result, ten minutes to decide and communicate which 09:00 work may start and whether the conditional 10:00 promise remains supportable, and ten minutes of contingency. Thus 08:30 + 10 + 10 + 10 minutes reaches 09:00. This is time to recover and use a qualified result, not an allowance for inventing a safety verdict. If the result or contact remains unavailable at 08:40, return that exact blocker while a service decision is still possible. A missing safety result blocks reliance on the release promise; observational work can continue when its own permission and inputs hold. Lost contact blocks live verification without erasing the completed laboratory result. A newly lost condition reopens the response immediately. P8-P retains its 13:00 reconsideration, and neither agreement nor priority grants field-release or safety authority.

#### OPS.7:5.2 - Public-hospital waiting and deterioration

One clinical case has a defined waiting age, current observations, possible deterioration evidence, dependencies on clinicians, beds and other resources, a service horizon, affected patient and care participants, and explicit clinical and operating authorities. OPS.7 makes those relations available to the authorized priority and commitment decision.

It does not equate waiting age with clinical urgency or triage. A qualified clinical System retains medical judgement and treatment authority. The Operations result may preserve or change the current coordination priority and prompt an authorized service-commitment return, but queue redesign, staffing and capacity, consent, privacy, medical safety, statutory permission, treatment efficacy, and patient outcome remain with their direct owners.

#### OPS.7:5.3 - AI-assisted software issue and service promise

One user issue has an exact age and state, user and service consequence, dependency on tool or model access, current trace and test evidence, integration load, recovery burden, bounded concurrency, and a promised horizon. OPS.7 relates those facts without treating model score, episode count, or dashboard severity as automatic urgency.

The authorized System may revise the issue's coordination priority or trigger an authorized commitment renegotiation, with an immediate check, integration action, fallback, or stop and next review. The result does not establish software assurance, security, model capability, provider authority, agenthood, causal effectiveness, integration, release permission, or service fulfilment.

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
- [ ] The existing commitment has parties, content, conditions, horizon, authority, status, and evidence limits.
- [ ] Any `OPS.6` result is used as evidence only at the matching configuration and horizon.
- [ ] State, age, time remaining, rate, trend, and intervention-sensitive temporal claims are distinguished.
- [ ] `C.27` is used only for an intervention-sensitive rate, rhythm, recovery, inertia, or regime claim.
- [ ] Urgency names the consequence, commitment, risk, recovery, or supported use that delay can change.
- [ ] Priority, queue rank, clinical triage, economic value, permission, and commitment remain distinct.
- [ ] Priority authority and commitment authority are separately established.
- [ ] The current comparison basis and any useful probe are explicit.
- [ ] Priority and commitment dispositions, immediate action or blocker, parties, horizon, evidence, and next review are recorded.
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
| temporal overanalysis | Ordinary age or rate triggers unnecessary dynamics modelling. | Keep ordinary temporal claims ordinary; use `C.27` only when the intervention-sensitive claim is current. |

### OPS.7:9 - Consequences

The operation gains a disciplined way to act before avoidable delay becomes failure while resisting automatic escalation. Practitioners can explain why priority changed, whether a bounded commitment changed, who held each authority, which parties are affected, and when the result must be reviewed.

The cost is obtaining the consequence and authority information that one convenient age score omits. Some cases must return to another decision owner before their priority or promise can change; actual fulfilment is observed later.

### OPS.7:10 - Rationale

Temporal facts become useful only through a receiving decision. Age is broadly observable, but urgency depends on what delay changes; priority depends on one coordination use; and commitment alteration depends on parties, conditions, and authority. Keeping these relations separate prevents time pressure from becoming unearned permission.

The pattern is intentionally local. It can preserve or revise one current priority and one existing bounded commitment without waiting for a complete queue, capacity, or service-design account. Explicit returns keep queue, buffer, constraint, capacity, service-design, whole-service commitment, and specialist questions with their governing patterns or competent participants.

### OPS.7:11 - SoTA-Echoing

The question is how a temporal change alters present action and an existing promise. Competent flow practice already compares consequences, not just age. The [Open Guide to Kanban, July 2025, prioritization appendix](https://kanbanguides.org/open-guide-to-kanban/2025.7/) discusses service classes, delay-cost rates, cumulative delay cost and opportunity cost, with cautions about uncertain estimates and reprioritizing started work. Reinertsen's historical economic-flow treatment and TameFlow's commitment and signal reasoning supply related mechanisms. OPS adopts that consequential comparison.

For section 5.1, a capable fixed-date or expedite policy can already prefer the younger incident because the field-contact opportunity expires. Both approaches can preserve the ongoing laboratory work rather than interrupt it. The residual OPS contribution is the connection between unlike clocks, the remaining whole response, and the distinct authority to change the promise. A local severity or queue decision cannot make the proposed next-day date effective. Sections 4.3–4.6 keep the 17:00 obligation visible until agreement and select a review early enough for action; the case shows the adverse change before that review and the actual agreement afterward.

If the incumbent service policy already records the response window, the affected recipients and effective agreement, use it unchanged. The additional burden otherwise is estimating the relevant response, obtaining the missing authorized decision and maintaining one current promise—not building a second priority scale. Those calls and confirmations consume time too; include them in feasibility and prefer a direct rule when it settles the matter. No precise score compensates for absent safety, clinical or legal authority.

FPF `C.27.TA` qualifies event, interval and currentness claims; `C.27` applies only to a consequential intervention-sensitive temporal claim. DEMO's commitment distinctions help inspect parties and agreement without assigning their authority. OPS.13 supplies service-level support and response construction. Reopen when consequence, required response, parties or agreement conditions change, or an incumbent achieves the same action and truthful promise account at lower total effort.

### OPS.7:12 - Relations

- `OPS.6` supplies a progressed state or unmet condition only as evidence where it changes this decision at the same configuration and horizon. It does not authorize a priority or commitment revision.
- `C.27.TA` governs temporal aspect, window, cadence, and currentness. `C.27` governs intervention-sensitive rate, rhythm, recovery, inertia, or regime claims; neither supplies Operations priority or authority.
- `C.11` governs comparison only when several admissible live dispositions require choice. `A.10` governs evidence reliance.
- `OPS.5` retains admission and explicit-start conditions. A current priority relation neither admits demand nor establishes start permission or Work.
- `OPS.8`–`OPS.11` retain queue, buffer, constraint, capacity, variability, and interacting-structure decisions. `OPS.13` retains the credible whole-service commitment account. `OPS.18` retains operating quality and reliability questions.
- Clinical triage, consent, medical safety, law, privacy, security, finance, product assurance, release, provider authority, and other specialist results remain with their direct owners.
- Practitioners may enter OPS.7 directly when its current evidence and authority exist, repeat it as conditions change, or return without using OPS.5 or OPS.6 in the same episode.

### OPS.7:End
