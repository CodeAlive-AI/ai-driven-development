## OPS.18 - Control Operating Quality and Reliability

> **Status:** Stable


### OPS.18:1 - Problem frame

**Use this when** an operating result may no longer meet its requirement, observed service failures exceed the agreed allowance, a recurring process changes, a lot needs acceptance or an incident raises a containment, recovery or recurrence-prevention question.

Begin with the result at risk, the affected population or configuration, and the action someone is authorized to take. Select the evidence method for that question. The first useful result is a decision about the affected work, service or output, together with the next action and the evidence and conditions needed to support it.

This pattern governs operating decisions about quality and reliability. A monitoring account is one input. A qualified product requirement, clinical decision, statistical method or engineering acceptance result may be another. If the question is only how to define and reconcile observations, use OPS.15. If a current response policy and adequate evidence already settle the action, apply them directly.

For example, twelve nonconforming items in a sample can trigger investigation under a process-monitoring rule. A lot-disposition decision still needs its own acceptance basis. Likewise, exhausting a software service's error budget can pause discretionary changes while urgent restoration continues under the responsible authority.

### OPS.18:2 - Problem

Different quality questions are often compressed into one status: the process looks stable, the customer objective was met, the lot passed or the service is restored. Each statement needs different evidence and supports a different action.

A dashboard can therefore look satisfactory while the actual service remains impaired. The opposite failure reacts to every fluctuation as a process change, consuming effort and destabilizing work without a suitable monitoring basis.

### OPS.18:3 - Forces

| Force | Practical tension |
| --- | --- |
| prompt response and false signals | Earlier detection can help containment while unsuitable thresholds create unnecessary interventions. |
| stability and acceptability | A stable process can repeatedly produce results that fail the requirement. |
| aggregate service and local consequence | A good average can hide an affected customer group or a short severe incident. |
| restoration and causal understanding | Service may be recoverable before the cause is fully established, while recurrence prevention still needs investigation. |
| continuity and protected conditions | Urgent recovery work requires the capability, authority and protections of its actual operation. |

### OPS.18:4 - Solution

#### OPS.18:4.1 - Recover the result, requirement and available action

State the operating result at risk: conforming output, correct responses, timely service, availability or restored operation. Recover the relevant population, configuration, period, requirement and consequence of failure. Name the authority for continuation, containment, acceptance and restart where those decisions differ.

Use the actual requirement. A product specification, an agreed service objective and a statistical control limit answer different questions. A control limit describes variation under its model. A requirement states what the result must satisfy. Recover each from its appropriate basis.

If a known violation already calls for a protective action, take that action under the current authority while obtaining the missing diagnosis or recovery result. A broad data analysis is unnecessary before a response already required by the observed condition.

#### OPS.18:4.2 - Select the evidence branch

| Current question | Evidence method | First operating use |
| --- | --- | --- |
| Has a recurring process changed from its established behavior? | A suitable statistical monitor with a qualified baseline, sampling rule and response policy. | Continue observation or investigate and contain the affected process/result. |
| Is event-based service meeting its objective? | Good/eligible event definitions, observation coverage, window, permitted loss and a response policy. | Adjust continuation or change activity under the service decision. |
| Should a particular lot or result be accepted? | Its qualified acceptance plan, defect definitions, sampling basis and relevant risks. | Accept, reject, segregate, rework or obtain the missing acceptance result. |
| Can an impaired service be restored or restarted? | Evidence of the failure, containment or repair, and the required restart conditions. | Restore service under the appropriate authority and continue any unresolved investigation. |
| What prevention does an incident or near miss need? | Reconstructed events, material explanations and sufficient support for feasible protective measures. | Select and verify prevention under :4.4, retaining the limits on the causal conclusion. |

Branches can be complementary. Select each because its answer changes the current action. A favorable result from one branch cannot supply the evidence required by another.

For recurring variation, recover whether observations are comparable, whether the baseline is appropriate and whether the selected model fits the data. Independence, changing sample size, seasonality, clustering or rare events can change the required monitor. A simple chart should yield to a qualified statistical method when its assumptions or detection performance are inadequate. Make that request usable: supply the defect/result definition, sampling and grouping, time order, baseline provenance, plausible dependence or drift, losses from false and missed signals, and the latest useful response. Ask for the population and model to which the return applies, detection and false-signal performance at specified changes, observation burden, and a rule the operator can execute. “Use EWMA” or a new control limit without those conditions is not the needed return.

For an event-based service, define the good and eligible events from the recipient's experience. Check omitted events, important subgroups and observation delay. A fast failure can require a timely alert before an end-of-window aggregate is available.

For acceptance, recover the lot or item, what counts as a defect, the sampling/inspection method, and the consequences of accepting unacceptable output or rejecting acceptable output. Obtain the qualified plan where it is missing. An operating practitioner can use a supplied plan without deriving its statistical design anew.

#### OPS.18:4.3 - Interpret the observation within its evidence limits

Calculate the selected quantity from its declared population. Use OPS.15 when event identity, coverage, time or missing observations need repair. Preserve any consequential uncertainty in the control decision.

A process-monitoring signal supports the action specified by its policy; it does not identify the cause by itself. An observation within the limits can still violate a product requirement. A capability claim needs the relevant stable-process and specification basis.

An error budget expresses permitted service loss for a stated objective and population. Compare observed loss with that allowance, then apply the authorized policy. Protected safety, human or clinical conditions remain applicable regardless of budget remaining.

A sample acceptance result supports the named lot decision under its plan and risks. It does not establish that every item conforms, that the process is stable or that a known failure mechanism has been corrected.

#### OPS.18:4.4 - Carry out containment or recovery and preserve continuing service

Select an action within the available authority: continue with observation, segregate affected output, pause a risky change, adjust admission, restore a known workable configuration, rework a lot or request the needed professional decision. State the affected scope and any service that must continue.

Obtain the capability, access and protected human conditions required for the action. Use OPS.12 and OPS.13 if recovery competes with existing service or relies on extra cover. An urgent label can identify priority; the actual assignment and authority determine who may act.

Where containment restores service before the cause is known, state what remains unresolved. Enter the following inquiry when prevention still needs an explanation. Extending a correction to new operating conditions requires support for its protective effect there; a stronger causal claim needs evidence for that claim. Reuse sufficient existing results, and apply a qualified correction directly when they settle the action.

1. **Reconstruct the incident.** Recover the failed result and requirement, affected occurrences and configurations, sequence, effects and containment already performed. Obtain the relevant participants' knowledge and permitted records. Distinguish observations from inferred links and identify missing facts that could matter to prevention.
2. **Develop the material explanations.** Follow contributing conditions beyond the immediate symptom, allowing several interacting conditions or rival accounts. Use B.5.2 when plausible explanations still need to be developed. For a disputed link, identify the existing observation, established mechanism or attainable test that could support or challenge it. C.28 helps qualify the causal conclusion; domain knowledge and evidence must supply the links in this incident.
3. **Choose supported prevention.** Compare retaining adequate protection, a narrow configuration or access correction, a change to the reusable way of working and a larger redesign where these are credible alternatives. Assess future exposure and avoidable consequences together with the full effort, delay, displaced service and other burden of each change. C.11 governs the choice; use C.11.CRC when the contribution of a finite change to the present arrangement needs that comparison. Zero loss in a near miss does not remove the exposed future consequence.
4. **Assign and verify the chosen change.** Name who will deliver it, the required result and its completion conditions. A recurring operating Method change belongs to OPS.16; choosing among ways to retain in an operating repertoire belongs to OPS.17. A local configuration, access or maintenance correction can finish as that correction. Verify completion separately from the restart conditions and later recurrence observations in :4.5.

Require sufficient support for the proposed protection under the relevant explanations that remain plausible. If they all support the same available correction, choosing a final causal account is unnecessary for that prevention decision. Retain the unresolved explanation wherever it limits a claim or later use. Obtain another observation when it can change the prevention, its permissibility or burden, or what the evidence warrants saying. If the worth or feasibility of that inquiry is itself unsettled, use C.11.DUA. Applicable protection and evidence requirements continue to govern the action.

#### OPS.18:4.5 - Verify restart and choose the next observation

Recover the condition under which service, normal production or discretionary change may resume. Obtain the observation that actually establishes it: applicable test evidence, a confirmed working configuration, restored service behavior, qualified acceptance or another required result.

Check the observation's scope and time. A restarted process, a new reporting period or an empty incident queue is not itself evidence that the defect was corrected. Preserve residual uncertainty and a response if the condition fails again.

Choose follow-up from the consequence and detection need. Large isolated departures, small persistent drift and rapid incidents may need different observation rules. Retain enough evidence for the continuing decision, and end collection that no longer contributes to a decision, required assurance or recovery.

Return the action, its evidence, affected population/configuration, authority and restart or next-observation conditions in the existing operating account. The selected control decision is the result; the chart or dashboard makes its basis inspectable.

### OPS.18:5 - Archetypal Grounding

#### OPS.18:5.1 - A process signal calls for containment and investigation

In this constructed recurring inspection operation, the supplied stable reference proportion of nonconforming items is p₀ = 0.02. Samples contain n = 200 independent, comparable items under the stated binomial basis. The local monitoring policy uses a three-standard-deviation p-chart rule and calls for segregation of the affected output and investigation when the upper limit is exceeded.

The upper limit is p₀ + 3√(p₀(1 − p₀)/n) = 0.02 + 3√(0.02 × 0.98 / 200), approximately **0.0497**, or 4.97%. The corresponding lower value is negative and is truncated to zero.

The next sample contains twelve nonconforming items: 12 / 200 = **0.06**, or 6%. This exceeds the specified upper limit. The practitioner applies the policy's containment and investigation response and identifies the sampled output, source process and current configuration.

The arithmetic establishes the signal under that rule. It does not identify why the items failed, determine another lot's disposition or show that the process is capable of meeting a product specification. The three-standard-deviation calculation defines the limit for this rule; it does not supply an exact confidence or false-alarm probability. With this low reference rate, a claim about false-alarm or missed-detection probability needs an appropriately qualified binomial or other statistical design.

Suppose the investigation finds a changed setup condition. Returning to the earlier setup and obtaining the required process and output evidence can support restart under the responsible authority. A single subsequent point below the limit is insufficient to establish every one of those claims. A persistent smaller shift may call for a monitor such as an exponentially weighted moving average (EWMA), which retains information from successive observations, if its detection properties fit the need.

Change the sampling premise. The 200 inspected items now come as fifty groups of four, sharing one setup within each group. In this constructed return, the qualified statistical supplier establishes a bounded model for the defect being monitored: all four items in a group share its conforming/nonconforming state; different sampled groups are independent; the stable reference probability is 0.02 per group. The sample's twelve defects occupy three groups. The count is therefore 3 of 50 independent group outcomes, not 12 of 200 independent item outcomes. The original 4.97% limit is inapplicable. With this model, its apparent trigger would correspond to at least three defective groups, with a baseline false-signal probability of about 7.84% per sample. More rows did not provide more independent information.

The operating owner needs to protect this finite campaign and decide whether a recurring-shift monitor adds a useful further result. The current product rule already holds any known defective group's output. The supplier is asked to compare early detection with the available inspection and response time, including a persistent rise from 2% to 6% defective groups. It returns these two explicit candidate rules under the stated independent-group model and fixed baseline:

| Candidate monitoring rule | Baseline false-signal probability | Detection probability if the group rate is 6% throughout the tested observations | Delay and use |
| --- | --- | --- | --- |
| Investigate at five or more defective groups in one fixed sample of 50. | approximately 0.321% per sample | approximately 17.94% per sample | Available after that sample; often misses this small persistent shift. |
| Investigate at ten or more in one prespecified, nonoverlapping block of four such samples, 200 different groups in total. | approximately 0.748% per block | approximately 76.57% per block | Uses four rounds of evidence; it does not provide an earlier warning. |

These exact-binomial tail calculations are a constructed statistical return, conditional on the supplied model; they are not lifetime false-alarm guarantees. Repeated blocks create repeated opportunities to signal. They do not authorize changing the baseline after seeing unfavorable observations or treating overlapping blocks as independent.

Suppose the next four rounds contain three defective groups each. No individual sample triggers the first rule; twelve of 200 groups triggers the second at the fourth round. The authorized response is a wider process investigation and containment at the supported scope. Each known defective group was held when found under the independent product rule; waiting for the fourth-round monitoring result cannot authorize its release. Unaffected output still uses its own acceptance basis.

Include the whole price and reuse observations already obtained. In this finite campaign each round's fifty groups are all its output. A qualified full screen costs forty staff-minutes per round, 160 over four rounds, and fits the service window. That adequate product-protection rule applies with or without a process monitor; the monitoring rule does not replace it. Its observations already supply the group outcomes, so do not charge for a second sample. The monitor adds two minutes per round for group/time reconciliation, 120 once for qualification/setup and twenty for the wider investigation in the supplied signal trace: 148 additional minutes, or 308 including inspection, apart from unchanged protective handling. Retain direct protection alone for this one-off use when no continuing exposure or other decision needs the separate recurring-shift answer. Where that answer is useful, compare its expected contribution with these added costs, actual signal workload and missed-loss consequences. The full screen protects this output without itself establishing the process-change claim. If action is needed before four rounds, request a qualified sequential design; the ordinary normal-data EWMA limits cannot simply be pasted onto these rare grouped counts. Correlation between groups, a changed defect mechanism or an unrepresentative baseline reopens this statistical return without canceling already supported containment.

#### OPS.18:5.2 - Service loss exceeds the agreed budget

In a constructed software service, the objective is **99.9% successful requests** over the defined window. The account includes 1,000,000 eligible requests, with success and eligibility measured at the service boundary relevant to users. The allowance is:

- 1,000,000 × (1 − 0.999) = **1,000 unsuccessful requests**;
- observed unsuccessful requests = **1,500**;
- budget consumed = 1,500 / 1,000 = **150%**.

The observed success proportion is 99.85%. The service has exceeded the stated allowance by 500 unsuccessful requests.

Its previously authorized local policy pauses discretionary feature releases when the budget is exceeded, permits the specified urgent recovery and security work, and requires investigation of the affected service. The practitioner applies that policy, names the eligible population and affected service, and directs the authorized recovery work. This is the policy of the constructed case; another service needs its own objective and permitted response.

A total of 1,500 also needs timely interpretation. If most failures occurred in the last few minutes or affected one important user group, the aggregate alone can understate the current incident. Inspect the relevant time and group breakdown where it changes containment.

Now suppose a calendar boundary starts a new reporting window while the failing request path remains impaired. The operation still lacks restoration evidence. Later, the recovery team restores a known working configuration, verifies the previously failing user path and obtains the live observations required by the agreed restart criteria. The responsible service owner can then decide whether to resume discretionary changes. Keep any unresolved causal or recurrence question visible.

The responsible owner uses budget consumption in the stated service policy. Independent safety and acceptance conditions still apply, and recovery work requires qualified people with the appropriate assignment.

#### OPS.18:5.3 - The lot decision uses its own plan

A separate constructed supplier lot arrives after the process signal above. The supplied product-acceptance plan defines the lot, defects, sampling and disposition authority. For this illustration, it specifies a random sample of fifty items and acceptance only if at most one is nonconforming. Its qualification for the actual product and producer/consumer risks belongs to the supplied plan.

The sample contains two nonconforming items. The acceptance practitioner rejects or segregates the lot as the plan requires and obtains the prescribed rework or supplier response. Even if a process chart for that producer has no current signal, the lot fails this stated acceptance rule.

If the lot had passed, the result would support its disposition under the plan's risks. It would not settle the earlier process investigation. If the plan or its risk qualification is missing for the actual use, obtain that result before relying on this sample rule; these illustrative numbers do not provide a general acceptance plan.

#### OPS.18:5.4 - Human service and AI assistance need their actual result

In a hospital operation, the due-request account can show missed service times while clinical priority changes the permissible response. The operating coordinator uses qualified clinical decisions and the current service authority to choose additional cover, rescheduling or another permitted intervention. A low average waiting time cannot clear an individual case whose required condition is unmet.

After an intervention, the coordinator observes the affected service and support work under the selected continuation conditions. A clinical outcome or health-effect claim requires its own evidence. OPS.12 helps preserve human conditions when recovery work adds demand.

In an assisted production service, a monitor may show fewer detected defects after a model change while the current sample excludes difficult requests. Recover that population before interpreting the improvement. Continue or contain the affected use according to the requirement and policy for accepted outputs.

A changed model can also alter the relevant failure modes. Qualification of the current acceptance method, actual accepted results and any affected customer promises may therefore need reconsideration. A passed sample from the earlier version is reusable only for the claims and conditions it still supports.

#### OPS.18:5.5 - An unresolved cause need not delay a supported correction

In this constructed print-shop incident, the customer approved proof P2, but the booklets reproduce P1. Records and participant accounts establish that the operator followed the work card containing P1; P2 was unavailable at the station, and the admission check asked only whether a proof was attached. The quality rule requires the affected order to be held.

Trace how P1 reached the station and why P2 was unavailable. Two explanations remain plausible: the preparer copied the earlier attachment, or the station received it from a stale synchronized folder. The records do not distinguish those paths. Both leave the same exposed condition: production can start without checking the proof against the customer's approved edition.

For this case, a qualified proof-control procedure is available for both paths: retrieve the approved proof through the authorized source, check its edition at the station and require first-article acceptance before releasing the order. The responsible production manager has authority and the necessary staff and access to apply it; its effort fits the continuing service commitments. These are supplied premises of the example, not results inferred merely because both explanations sound plausible.

The manager applies that correction. Staff verify that P2 is available, perform the edition check and obtain the required first-article acceptance for restart. Selecting between the copying and synchronization explanations is not a prerequisite to this adequately supported response. Their difference would become relevant if, for example, a proposed automatic retrieval change protected only one path; that proposal would need the missing discrimination or a protection covering both.

OPS.16 addresses any resulting decision to change the recurring operating Method; OPS.17 is needed only for a repertoire choice among competing ways. Completion of the proof-control change is observed separately from recurrence over the later orders and exposure that the prevention claim covers. A clean first article does not establish a long-term recurrence rate.

If the edition check catches P1 before printing, no booklets are spoiled: the check has protected this order. Whether further change is needed depends on the remaining exposure and available protection.

### OPS.18:6 - Bias-Annotation

Visible control limits can look authoritative even when their model or baseline does not fit the operation. Keep the required product or service result beside the monitoring claim and inspect the assumptions before extending its use.

A recent repair can also encourage early closure. Verify restored service at the affected scope, and distinguish that result from identification of the cause and evidence about recurrence. Acknowledging the remaining question allows useful recovery without overstating it.

### OPS.18:7 - Conformance Checklist

| Check | Evidence sufficient for the declared use |
| --- | --- |
| The result and possible action are clear. | Requirement, affected population/configuration, consequence and response authority are recoverable. |
| The evidence method answers that question. | Monitoring, service-objective, acceptance, recovery and prevention uses retain their distinct bases. |
| The observation is interpretable. | Baseline, sample or event population, coverage, time, model and uncertainty fit the claim. |
| The action follows the applicable rule. | Continuation, containment, acceptance, restoration or Method change uses the actual policy and protected conditions. |
| Restart has real evidence. | The required result is established at the relevant scope and time; a reporting reset does not stand in for it. |
| Remaining work is directed. | Unresolved cause, recurrence risk, missing professional result or changed method assumption has a concrete receiving use. |
| Prevention has sufficient support. | Further discrimination changes prevention, permissibility, burden or a supported claim; a common adequately supported correction can proceed with the remaining explanation explicit. |

### OPS.18:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Working repair |
| --- | --- |
| Treat statistical stability as product conformity. | Compare output with its requirement and obtain the applicable capability or acceptance result. |
| Use a chart signal as proof of a specific cause. | Contain as required and investigate the actual mechanism. |
| Let an error budget authorize every kind of loss. | Preserve independent safety, human, clinical and acceptance conditions. |
| Accept a lot because the process chart looks normal. | Apply the lot's qualified acceptance plan and risks. |
| Resume normal work when the reporting window resets. | Verify the actual restart conditions and obtain the authorized continuation decision. |
| Reuse an old monitor after the population or failure modes change. | Requalify the affected observation and detection method for the new use. |

### OPS.18:9 - Consequences

The practitioner can connect quality and reliability evidence to a concrete operating response. The action remains scoped to the affected output, service or configuration, while necessary service can continue under its own conditions.

Monitoring and acceptance can incur false alarms, missed failures, inspection cost or delayed service. Recovery can restore operation while leaving a cause unresolved. Selecting the method and evidence by consequence makes these trade-offs visible instead of hiding them in a single green status.

### OPS.18:10 - Rationale

Monitoring, acceptance, restoration and prevention regulate different moves. Selecting the evidence from the current decision preserves the meaning of a statistical limit, a product requirement, a service objective and a supported protective change.

The separation between containment, restored service and causal knowledge also supports proportionate action. A practitioner can act on sufficient operating evidence while obtaining the stronger result needed for prevention, wider use or a more consequential commitment.

### OPS.18:11 - SoTA-Echoing

The practice question is how to control operating quality and reliability from evidence suited to the required action. The selected best-known line uses qualified statistical monitoring, user-relevant service indicators and explicit acceptance or recovery criteria. Compared with one aggregate quality status, it exposes the distinct decisions in the worked cases.

| Source and practice question | Selected move and alternative | Operative contribution and limit |
| --- | --- | --- |
| [NIST proportions control charts](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc332.htm) and [process stability](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm) | Use a monitor suited to recurring variation, instead of reacting to every raw fluctuation. | Sections 4.2–4.3 and 5.1 preserve baseline, population and model. The original three-sigma signal and the changed group-count return answer different sampling conditions; exact tail risks are stated only for the latter's supplied model. |
| [NIST EWMA guidance](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc324.htm) | Consider a memory-bearing monitor when persistent small shifts matter more than one large point. | Sections 4.5 and 5.1 retain detection delay and assumptions as reasons to change the method. NIST's ordinary EWMA limits assume independent data and their tabulated design assumes normality; grouped rare-event monitoring needs a qualified design, not merely the chart name. |
| [NIST process capability](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) and [acceptance sampling](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm) | Select specification/capability or lot-disposition evidence for that question, instead of reusing a monitoring verdict. | Sections 4.2–4.3 and 5.3 keep the lot, defect and producer/consumer risk basis separate. |
| [SRE service objectives](https://sre.google/workbook/implementing-slos/), [error-budget policy](https://sre.google/workbook/error-budget-policy/) and [alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) | Relate user-relevant observed loss to an agreed action and timely detection, instead of using infrastructure availability alone. | The service case adopts the loss calculation and policy relation. Local targets, exceptions, authority and restart evidence are supplied for the actual service. |
| Ries, *The Lean Startup* (2011), chapter 11; [Lean Enterprise Institute, Five Whys](https://www.lean.org/lexicon-terms/5-whys/); [Google SRE, Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) (2016) | Recover contributing conditions and assign supported prevention, instead of stopping at the first symptom or treating a question count as causal proof. | Sections 4.4 and 5.5 adapt incident reconstruction, knowledgeable participation, countermeasure selection and follow-up. The historical accounts and practice guidance do not prove a particular causal chain or a recurrence reduction; those claims need their own evidence. |

The NIST handbook provides standing technical models. The SRE Workbook supplies software-service guidance and a dated 2018 policy example. Their contributions are adapted to the stated operating decisions.

For an individual known failure, immediate qualified containment can be the stronger response than developing a new statistical monitor. For recurring uncertain behavior, a designed monitor can reduce reactive disturbance and improve timely detection. Reopen the selected method when the population, baseline, loss consequence, detection need or authorized policy changes.

### OPS.18:12 - Relations

OPS.15 helps construct the observation account when its subjects, coverage or definitions are unresolved. OPS.4 guides shared attention to qualified operating state. OPS.5–OPS.7 guide admission, continuation and attention to aging work when the control decision changes those actions.

Use OPS.12 for human conditions and OPS.13 for service commitments and resource choices affected by containment or recovery. OPS.14 helps compare consequential operating and financial alternatives. OPS.16 evaluates a change to an operating Method; OPS.17 compares and refreshes the repertoire of ways available for operating work.

B.5.2 helps develop rival explanations of the incident; C.28 qualifies their causal support. C.11 and C.11.CRC support the choice and whole-burden comparison of preventive changes. C.11.DUA enters only when the contribution or feasibility of a requested inquiry remains in question.

FPF C.16 governs the measures and statistical assumptions relied on, and A.10 preserves evidence reach. A.11.OP limits additional monitoring or records to their decision, assurance or recovery contribution. Engineering, clinical and other qualified practitioners supply the specific acceptance, protection or restoration results their domains require.

### OPS.18:End
