## OPS.15 - Build a Decision-Specific Operating Account

> **Status:** Stable


### OPS.15:1 - Problem frame

**Use this when** you need an account that answers an operating question. Figures may disagree, a denominator may exclude unfinished work, or a dashboard may combine events from different services. Establish what the observations support for the requested claim or decision.

Name the decision or operating claim the account must support. Identify its subject, population and time basis. Give the selected observations, their meaning and limits, and the conclusion they support. A short table, an existing record or a view in the current tool can suffice.

This pattern governs the construction and maintenance of that account within continuing operations. The responsible practitioner uses the account to make any operating decision required. Use an adequate existing account directly when its meaning and evidence fit. Statistical estimation, causal investigation or a professional acceptance judgment needs its own method when the receiving claim requires it.

Suppose forty service requests have all reached their due dates. Twenty-seven finished on time, three finished late and ten remain open. Reporting 27 out of 30 completed requests as “90% on time” leaves the overdue open work out of the service judgment. The due-request account shows 27 out of 40, or 67.5%. Recovering the question changes which of these true calculations is useful.

### OPS.15:2 - Problem

Available records often reflect the tool that generated them. A board counts matters, a rig log counts attempts, an invoice records an amount due and a payment account records a receipt. Combining them without their subject and event meanings can produce an apparently precise but unusable conclusion.

More collection can increase reporting effort without settling the question. Identify the evidence the requested conclusion or choice needs, together with any separate assurance or recovery use.

### OPS.15:3 - Forces

| Force | Practical tension |
| --- | --- |
| useful summary and retained meaning | A compact number can hide the population, exceptions or source loss that determines its use. |
| common subjects and unlike views | Several readers can need different accounts of the same operation. |
| current information and collection cost | Frequent refresh is useful when changes can affect the receiving result soon enough to matter. |
| comparable values and changed conditions | A new definition, work mix or measurement method can make old and new values incomparable. |
| sufficient decision evidence and unresolved detail | A bound can settle the choice even while some observations remain unknown. |

### OPS.15:4 - Solution

#### OPS.15:4.1 - Identify the receiving question

Name who will use the account, the decision or claim at issue, and when the answer is needed. State the fact or comparison that could settle it. “Should we retain this service promise?”, “Did the due-date cohort meet its objective?” and “Which rig should receive the next ready package?” need different evidence.

Identify the operating subject and the result of concern. For each needed claim, recover its population: requests, test attempts, accepted packages, shifts, incidents or another explicitly defined set. Preserve the service boundary relevant to the recipient, including work that waits before entering the visible internal workflow.

Inspect existing accounts and observations before adding collection. Reuse one whose subject, conditions, time and definition fit. If a current qualified result already supports the requested claim or action, return it with its limit.

#### OPS.15:4.2 - Define the claims and measures

For each quantity needed for the account, make its meaning recoverable. A ratio needs its numerator, denominator and eligibility rule. A duration needs its start, end, unit and treatment of unfinished cases. A count needs its event or result identity, observation window and duplication rule.

Choose the interpretation with the receiving use. Completed-only cycle time may describe completed work; it cannot by itself describe how all admitted work is progressing. A due-date cohort contains work whose required completion date falls within the selected period. Open work whose deadline has passed differs from open work whose deadline lies in the future.

Use the following questions only where their answers affect the claim:

| Question | Consequence for the account |
| --- | --- |
| What belongs to the population? | Inclusion, exclusion, cancellations, diverted work and service classes change the denominator or reach. |
| When is the event observed? | Clock origin, cutoff, timezone where material, and reporting delay change the time claim. |
| What constitutes completion or acceptance? | Attempts, completed work, accepted service and a later release can be counted differently. |
| How is the value obtained? | Source, measurement rule, sampling and missing data determine what the number supports. |
| Can the values be compared? | Changed definitions, methods, mix or conditions may require recalculation on a common basis. |

Keep uncertainty explicit when it affects the claim or decision. Use an interval, separate unknown category or qualified estimate appropriate to the claim. A precise display does not remove missing observations.

#### OPS.15:4.3 - Reconcile source events and subjects

Trace the quantities to the events or observations that establish them. Recover which request, case, configuration, test, resource and result an event concerns. One event can concern several subjects, and one subject can have many events. Use their actual relationships when joining accounts. If the claim or decision depends on which configuration or provider relation held at a particular time, obtain evidence for that interval; a relation record alone may not supply it.

For example, a second test attempt may add rig-hours while leaving the number of accepted test packages unchanged. Issuing an invoice for a package and receiving its payment are different events. A release can depend on several test results and a safety decision. Counting these records as interchangeable “completed items” loses the question the account must answer.

Inspect material gaps at the boundary of the measuring system. Server logs can omit failures that occurred before a request reached the server. A queue view can omit rejected, diverted or blocked requests. Obtain another source or narrow the claim where that loss matters.

Use OPS.15.1 when the account needs intervals or aggregates derived from those events. Its construction retains shared batch occupancy, repeated visits, cancellations and the portions of unfinished visits inside an observation window. Reuse a quantity already derived on the required population and boundary.

Reconcile disagreement before aggregating it away. Recover whether two totals use different cutoffs, populations or definitions. If the underlying observations permit it, recalculate on a common basis. Otherwise preserve the disagreement and state the narrower supported comparison or missing result.

#### OPS.15:4.4 - Present the account for its actual readers

Lead with the conclusion supported for the receiving use, then show the observations and qualifications needed to assess it. Retain the source and time basis in the existing account at the detail the use requires. Distinguish observed state, an interpretation, a forecast and the decision made from them.

Several views can be useful. A coordinator needs current readiness and service risk; a finance practitioner needs accepted service, payable amounts and receipts; a release practitioner needs evidence applicable to a particular configuration. Keep the correspondence between their subjects explicit where the decision crosses views.

A shared table is appropriate when it preserves these meanings. Separate views are appropriate when they answer different questions.

#### OPS.15:4.5 - Stop when the evidence suffices and refresh when its grounds change

Ask whether unresolved detail can still affect the requested claim or decision. If even the favorable bound misses the criterion, the uncertainty need not be resolved for that conclusion. Other work may still need the detail for recovery, fairness, required assurance or a different decision; keep those uses separate.

Choose refresh timing from the decision window, rate of relevant change, observation delay and cost of stale information. A live incident can require rapid updates. A stable resource decision may need an update only when demand, configuration, access or another relied-on condition changes.

When the assignment includes reviewing recurring collection, use A.11.OP to check whether a decision, reporting, assurance, recovery or another required use still depends on it. Return the finding to the commissioned recipient. End collection or notify another party when your assignment or a standing duty calls for that action and you have the authority it requires. Reuse a current observation only for the conditions and claims it still supports.

Return the account with the supported claim and any uncertainty material to its use. Obtain another observation only when a receiving use still needs it. If a decision on admission, commitments, finance or control follows, use the account with the corresponding operating method.

### OPS.15:5 - Archetypal Grounding

#### OPS.15:5.1 - Forty requests produce two different service measures

In this constructed case, all forty uncancelled requests in the selected cohort have reached their due dates. At the observation cutoff, twenty-seven finished on time, three finished late and ten remain open. The local service objective concerns timely completion of this due-date cohort and is 90%.

| Observation or calculation | Value | Supported meaning |
| --- | --- | --- |
| Requests completed by the cutoff | 27 + 3 = 30 | Thirty members of the cohort have a completion event. |
| On-time proportion among completed requests | 27 / 30 = 90% | 90% of requests completed by the cutoff finished on time. |
| On-time proportion among all requests due | 27 / 40 = 67.5% | The cohort received timely service on twenty-seven of its forty requests. |
| Still-open requests whose deadlines passed | 10 | These members have already missed the timely-service condition. |

The corrected account says that the due-date cohort missed its 90% objective. It retains the completed-only measure where someone actually needs that narrower description. The ten open requests remain visible for recovery and the recipients' current service decisions.

A later completion of an overdue request changes its open/closed state but cannot make its original completion timely. If the parties revise a future commitment, preserve the original deadline where the historical comparison needs it. New requests with future deadlines belong to a separately defined current-work view, so they do not silently dilute this cohort's result.

Use the existing service method to handle the overdue work and affected commitments. The account supports the missed-objective claim. It does not identify why the service failed or prove that a proposed staffing change will fix it.

#### OPS.15:5.2 - A favorable bound can settle the reporting decision

Consider a separate forty-request cohort with the same 90% objective. Thirty-one are known timely, seven are known late, and two have unresolved completion timestamps. The most favorable result is 33 / 40 = 82.5%, if both unknown requests were timely.

The cohort missed the objective under either interpretation of those two timestamps. Further lookup cannot change that classification. The practitioner reports the supported result and the remaining range, from 31 / 40 = 77.5% to 82.5%.

The missing timestamps may still matter to contacting those recipients, recovering service or correcting a source defect. Pursue that work when its separate use requires it without making it a prerequisite for the already settled cohort judgment.

#### OPS.15:5.3 - PumpWorks keeps four views connected

The operation's board includes release candidate R42, incident I73, safety question S19 and provider change P8. A rig history records attempts and setup. The test service records completed packages and customer acceptance. Finance records invoices, payments and receipts. These accounts concern related work, but their rows do not share one universal item identity.

| Reader and decision | Account needed | Correspondence that must remain clear |
| --- | --- | --- |
| Rig coordinator choosing the next slot | Eligible packages, required rig time, configuration and access | A repeat refers to its package and adds resource demand without adding another completed package. |
| Service coordinator handling a promise | The promised test result, recipient, due time, completion and acceptance | A package can be complete at the rig while the customer's evidence acceptance remains pending. |
| Finance practitioner comparing now with deferral | The same third package, payments, acceptance condition and receipt date | The receipt follows the stated payment terms; completion in month 1 does not put cash in month 1. |
| Release practitioner deciding field use | T9 evidence applicable to R42's configuration, S19's result and release authority | Customer acceptance of a test service does not settle the separate release decision. |

For the immediate financial alternative in OPS.14, the third package is accepted in month 1 and its 900 receipt is due at the end of month 2. The account can show both events without calling them the same completion. The rig view retains the repeat among the two earlier packages, so the third package's financial comparison does not acquire an extra test by a mistaken join.

If P8 changes a provider window, update the affected capacity and service claim. If the release configuration changes, reconsider applicability of T9 evidence. Refresh the accounts that depend on the changed subject or claim.

#### OPS.15:5.4 - Hospital and assisted-service accounts expose omitted work

A hospital coordinator asks whether all routine cases due today received the agreed service. A department's completed-visit report omits patients transferred before the visit and cases still waiting. Recover the service definition and who was due the service. One confirmed eligible case without the agreed result refutes a claim of service to every case. A qualified total of distinct served cases can establish coverage when its population and correspondence match. Seek individual dispositions for a case-level decision or when coarser evidence leaves the coverage question open. A transfer may count as fulfilled, redirected or unresolved depending on the actual agreed service; the report cannot choose that meaning by omission.

The resulting account preserves the eligible cases and reasons for unlike dispositions. It can support service coordination while clinical outcome claims remain with qualified clinical evidence. A different clinical priority can require a different operating action without erasing the earlier service history.

In an assisted production service, the system reports sixty generated drafts and six review decisions. The recipient asks for accepted outputs. For a requested count, use a qualified count of distinct accepted outputs if one is available for the same work. Otherwise relate review decisions, drafts and revisions to the results the acceptance terms recognize. Identify individual outputs when the recipient needs them. Counting generated versions or repeated reviews as new accepted results would overstate service.

A useful account shows current review decisions, accepted outputs, rework and outstanding requests with their own time bases. The capacity conclusion can then use review effort, while the recipient's service claim uses accepted outputs. OPS.13 guides the commitment decision and OPS.18 guides a quality response when the evidence requires one.

### OPS.15:6 - Bias-Annotation

Completed cases and successful transactions are easier to observe than abandoned, diverted or still-open work. Begin with the population the operating question concerns and inspect the places where observation can lose its members.

A measure already reported can also become the default objective. State the intended service value and why the selected observation bears on it. Keep a useful proxy qualified where direct observation is unavailable, and revisit it when its relationship to the value changes.

### OPS.15:7 - Conformance Checklist

| Check | Evidence sufficient for the declared use |
| --- | --- |
| The account serves a stated use. | The recipient, operating claim or decision, required time and relevant observation are clear. |
| Subjects and populations are stable. | The relevant work, events, results, inclusions and exclusions can be recovered. |
| Quantities have a meaning. | Units, numerator/denominator where needed, start/end rules, cutoff and interpretation are explicit. |
| Sources support the claim. | Observation method, missingness, delay and comparability fit the receiving use. |
| Views can be related without conflation. | Shared subjects and unlike event meanings are preserved where a conclusion or decision depends on more than one view. |
| Collection and refresh have a purpose. | Each retained observation serves a stated reporting, decision, assurance or recovery need, with a relevant change or expiry condition. |

### OPS.15:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Working repair |
| --- | --- |
| Use completed-only data to describe every due request. | Recover the due population and retain overdue open work in the service denominator. |
| Join every event to one arbitrary case identifier. | Preserve the actual relationships among requests, attempts, configurations and accepted results. |
| Add a second dashboard to reconcile a definition conflict. | Resolve the differing populations, dates or meanings before choosing a presentation. |
| Treat a current file as current evidence. | Recover the observation time and the conditions under which it remains applicable. |
| Collect every unresolved detail before making any decision. | Test whether its possible values can affect the requested conclusion or choice, while preserving other necessary uses. |
| Infer the cause of a failure from a descriptive difference. | Use the account to frame the causal question and use relevant causal evidence or identify the inquiry needed if a causal conclusion is requested. |

### OPS.15:9 - Consequences

The reader can recover what a reported value establishes for the operating question. Different practitioners can use unlike views of the same work while retaining the connections needed for a service, resource or release choice.

Some apparent disagreements remain after their meanings are clarified because the evidence is incomplete or incomparable. The account exposes that limit. A smaller set of relevant observations can reduce recurring effort, although repairing a lost event population may require work on the source system.

### OPS.15:10 - Rationale

A measure is useful through the claim it supports for the receiving use. Starting with that claim makes eligibility, event identity and time rules practical necessities rather than optional metadata.

Separate views preserve the different consequences of one piece of work. Bounds and directed refresh then reduce collection whose result cannot affect the current claim or choice, while retaining the observations needed for another real use.

### OPS.15:11 - SoTA-Echoing

The practice question is how to obtain a trustworthy operating account without measuring everything. Start with the claim or decision, qualify the observed population and measurement procedure, and preserve event relationships across views. These distinctions explain the forty-request discrepancy and the different service, resource and cash events in PumpWorks.

The [SRE Workbook's guidance on service indicators](https://sre.google/workbook/implementing-slos/) distinguishes what service behavior an indicator should represent from how the measurement is implemented. Sections 4.2–4.3 adopt that distinction: a server log or completed-item table can omit events belonging to the service question. The source is a 2018 software-service treatment; the method here applies its observation-boundary reasoning to the constructed operating cases without deriving clinical or financial conclusions from it.

[Kanban's flow measures](https://kanbanguides.org/the-kanban-guide/2025.5/) make work boundaries and elapsed-time evidence explicit. The account retains their useful defined-population discipline while choosing measures for the receiving question. The due-cohort example uses a service-deadline population that must be defined separately from a completed-item cycle-time population.

The [OCEL 2.0 specification](https://www.ocel-standard.org/2.0/ocel20_specification.pdf), sections 3–4, and [van der Aalst's 2023 account of object-centric process mining](https://www.mdpi.com/2227-7390/11/12/2691) support preserving events' relationships to several objects. Section 4.3 adopts that representation choice where one case identifier would lose the PumpWorks relationships. These sources describe representation and analysis; they do not establish the operating decision or the validity time of every relation. A larger measurement or process-mining system is appropriate when its result could materially improve the claim or decision at a justified cost; the simple account remains preferable where existing observations and a transparent bound suffice.

Use FPF A.11.OP to decide which observations to keep for a reporting, decision, assurance or recovery need. Reconsider the account when its use, population, event meaning, source coverage or observation method changes.

### OPS.15:12 - Relations

OPS.4 guides shared operating attention using qualified state claims; this pattern helps construct the account when those claims are not yet supported. OPS.3 helps identify the operating subjects that source events concern.

OPS.5–OPS.10 provide admission, continuation, aging, queue, constraint and capacity questions that can select the account's observations. OPS.12–OPS.14 provide human-condition, commitment and financial uses. OPS.18 guides the control action based on quality and reliability evidence, while OPS.17 helps reconsider a failed method assumption.

FPF C.16 governs the measurement characteristics, units and comparison basis used here. A.10 keeps evidence reach explicit, and E.13 helps examine a proxy when its relationship to the intended value is in question. A.11.OP limits recurring account work to its actual contribution.

### OPS.15:End
