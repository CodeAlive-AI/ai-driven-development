## RMP.Application:5 - APP-RMP-05 — Should a second approver reduce customer waiting?

Use this application when a manager can describe a workflow but needs help turning a proposed change into an answerable research question, obtaining a suitable comparison and using its result. Start by separating the outcome customers need from the indicator the organization happens to record. The reader needs ordinary process knowledge and arithmetic; a qualified analyst supplies the statistical design and analysis where those are needed.

The example is constructed. Its branch arrangement, professional results and numbers are stipulated for explanation, not observations of an organization or a recommended sample size. It shows how to obtain and inspect a contribution from a specialist. Reading it does not establish that someone can independently design a causal experiment.



### RMP.Application:5.1 - Find the question that matters

A quotations manager sees many overdue offers and proposes a second approver. Two different aims are possible: meet the promised date, or shorten customers' actual wait. Moving the promised date can improve the first indicator while leaving the second unchanged. The manager selects the second aim and keeps quotation errors as an outcome that must not worsen beyond an agreed limit.

The initial working question is: **Would making an additional approver available, under a specified arrangement, shorten the time from a customer's request to the quotation actually sent?** Approval may be only one delay. Missing customer input and difficult calculations are also plausible. Existing evidence may already support a sufficient repair, such as restoring a known failed forwarding rule. [RMP.1](31-rmp-1-decide-whether-a-question-needs-research-and-when-to-s.md) can return that answer without making a new study compulsory. Here, suppose the effect of additional approval capacity remains unresolved and matters to a recurring staffing decision.

Keep three questions separate:

- **Where did these quotations wait?** This needs suitable event records.
- **Which mechanisms explain the waits?** Consider approval delay, missing input, or both, with initial complexity and workload affecting them.
- **What would the additional-approver arrangement change?** This needs a justified comparison of intervention versions and outcomes.

[Constructing and challenging a causal model (FPF C.28.CM)](../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md) helps articulate these mechanisms. A diagram makes their implications inspectable; it does not establish which arrows are warranted.



### RMP.Application:5.2 - Obtain records that preserve the needed distinction

The CRM contains one date labelled "status updated". It may be the time an administrator changed a field after the quotation was sent. Before analyzing it as customer waiting, compare a small set of retained messages and approval records with their CRM entries. This checks what the recording operation means; it does not estimate the effect of another approver.

For one constructed request, the retained records show:

| Event | Recorded time | Working time since the preceding event |
| --- | --- | ---: |
| Customer request received | Monday 09:00 | — |
| Sufficient customer input received | Tuesday 10:00 | 9 hours |
| Calculation completed and submitted for approval | Tuesday 14:00 | 4 hours |
| Approval completed | Wednesday 16:00 | 10 hours |
| Quotation actually sent | Thursday 10:00 | 2 hours |

This office counts working time from 09:00 to 17:00 on weekdays. The total is 25 working hours, or 3.125 eight-hour working days. Approval accounts for ten hours in this case; input waiting accounts for nine. The delay between approval and sending also remains visible. An updated CRM status at Thursday 11:00 would measure a different event.

The registration trial should expose missing events, inconsistent clocks, retrospective guesses, duplicate requests and the effort required to keep the record. If the old messages do not survive, mark the missing history. Begin suitable prospective recording when worthwhile; do not invent past timestamps. If two durations of seven and eight hours are both stored as "one day", repeating that rounded record need not recover their difference.

[RMP.3](33-rmp-3---operationalize-the-research-design-without-replacing.md) connects these choices to the question; [RMP.4](34-rmp-4---preserve-a-criticism-ready-research-trace.md) preserves what actually happened and what can still be examined. Retain both the intended record and consequential departures from it. Stage durations are useful for understanding mechanisms, while the intervention's total effect still concerns the whole time to sending.



### RMP.Application:5.3 - Separate a delay forecast from an intervention effect

Suppose a separate set of 30 old quotations contains 20 late and 10 on-time quotations. The head approver was absent for 13 of the late quotations and three of the on-time quotations. The odds of lateness are initially 20/10 = 2. On learning that the approver was absent, the likelihood ratio is (13/20)/(3/10) = 13/6. Updated odds are 13/3, corresponding to probability 13/16.

This calculation describes the association in that table, under its use as the relevant probability model. It does not give the effect of appointing another approver. Absence may coincide with high workload or difficult cases; the proposed substitute may work differently. Even the forecast for future quotations needs the table to remain an appropriate basis.

To compare "approval delay", "missing input" and "both", an analyst needs the likelihood of the proposed records under those accounts, or a weaker contrast the available records can actually support. Accounts can allow the same observation with different probabilities. Conversely, available observations may fail to distinguish them. Do not fill "the hypothesis is false" with an arbitrary mixture of alternatives or force coexisting mechanisms into an exclusive pair.

Use [statistical inference under an observation model (MMP.13)](../foundational-thinking-dpf-suite/mmp/18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md), for the probability model and update; [observations that distinguish model alternatives (MMP.16)](../foundational-thinking-dpf-suite/mmp/22-mmp-16---design-observations-to-separate-mathematical-model.md), for what an obtainable observation could discriminate; and [intervention-effect identification (MMP.15)](../foundational-thinking-dpf-suite/mmp/20-mmp-15---identify-an-intervention-effect-from-available-data.md), for whether the available comparison identifies the causal quantity. These are different supplied results. A plausible mechanism or larger probability is not yet a staffing decision.



### RMP.Application:5.4 - Ask for a comparison the organization can obtain and run

The manager gives a qualified analyst a concrete request:

> We need to decide whether to fund one additional hour of approval capacity per working day in each participating branch. The new arrangement adds a trained approver during the stated hour, using the same approval rules; the current arrangement has no additional approver. Our outcome is working time from receipt of an eligible customer request to actual sending, including waits for missing input. We also need the change in the proportion of quotations requiring a customer-facing correction. Please specify which cases and branches the answer concerns, how to assign the arrangements, how to handle unfinished or missing cases, and which comparison and uncertainty calculation can support the decision.

The request supplies current workload and complexity records, staffing arrangements, queues, expected arrival volumes, the reporting deadline and the people who can operate the record. The manager also provides a prospective criterion: the lower limit of the specified two-sided 95% interval for the mean reduction must exceed **one working day**, and the upper limit of the corresponding interval for the increase in correction rate must be below **0.5 percentage points**. These are this case's operating criteria, chosen with the responsible decision owner before examining intervention results. They are not universal scientific thresholds.

The analyst must explain how the assignment, outcome, dependence, expected precision, observation period, analysis and stopping rule answer this question. "Run an A/B test" leaves those operations unspecified. [RMP.2](32-rmp-2-choose-a-criticism-bearing-research-design-or-stop.md) uses the supplied professional construction to choose an obtainable design or a useful stop; [RMP.3](33-rmp-3---operationalize-the-research-design-without-replacing.md) makes its consequential operations executable. Ask the analyst to work through one branch and one request so that the responsible staff can check what they would actually do. A citation or an assisting agent's fluent explanation does not supply an unavailable design qualification.

For the positive branch, suppose the analyst supplies and justifies the following arrangement for this workplace:

- Sixteen branches have separate customer populations, queues and approvers. They do not share reserve staff or transfer requests. Eight pairs are formed using pre-intervention workload, complexity and waiting records. Within each pair, random assignment gives one branch the new arrangement and one the current arrangement. Both run over the same calendar period. Requests enter during four weeks; assigned staffing continues for six weeks to cover the planned follow-up. The protocol specifies the limitation to return if sending and correction follow-up remain incomplete, rather than silently dropping those cases.
- The target is the average effect across these branches at the specified workload, giving each branch equal weight. The analyst first calculates each branch's mean for all eligible requests arriving during four fixed weeks, then the eight paired branch contrasts. The number of requests improves information about a branch; it does not turn each request into a separately randomized branch.
- Eligibility is settled at arrival. The total waiting clock includes time obtaining missing input; the analysis does not adjust away approval time, an intended mechanism of the intervention. Follow-up covers sending and the agreed five-working-day correction window. Unsent, withdrawn or untraceable requests have a specified handling rule and remain visible; dropping them because they are inconvenient is not that rule.
- Both arrangements use the same recording and staff-notification practice. Time comes from the relevant events. An assessor who can examine the quotation without its assignment label applies the specified customer-correction rule. The analysis retains the actually used staffing, other changes and departures from the intended arrangement.
- Historical variation and the expected volume support the proposed precision under the analyst's stated assumptions. For this constructed case, the analyst qualifies a paired-contrast model and its interval calculation. Four weeks and eight pairs come from that supplied justification; neither number can be copied into a different workplace without it.
- The plan fixes the primary outcome, weighting, interval calculation and analysis before results are examined. A serious customer harm stops the operational trial and returns the affected decision; missing records or staffing departures are reported for interpretation. An attractive interim result does not authorize early success stopping or a newly selected primary outcome.

Matching branches reduces known background differences; random assignment supplies the allocation mechanism. Neither guarantees that a realized small comparison is perfectly balanced or protects against a shared queue. The [NIST account of randomized blocks](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) explains the distinction between the factor being varied and background variation controlled by blocking. Its design principle is not a qualification of this workplace protocol.

Obtain the complete protocol and its grounds from the analyst before relying on it. The summary above identifies what the manager inspects and operates. It is not a replacement for the setting-specific treatment of unfinished cases, precision and analysis.



### RMP.Application:5.5 - Decide whether the study is worth obtaining

Suppose the promised contribution is feasible within eight calendar weeks: four weeks of incoming requests, two more weeks with the assigned staffing and follow-up, then analysis and return. The estimated burden is 240 hours of additional approval work in the eight assigned branches over six five-day weeks, 24 hours of recording setup and checks, 32 analyst hours and 16 management hours: **312 staff-hours**, against an authorized allowance of 340. Reallocated approval time also displaces other work; the decision owner considers that lost contribution, customer disruption and the value of a delayed decision rather than counting only the analyst's invoice.

In this case the owner judges the prospective answer worth that burden because a supported reduction would change a recurring staffing choice, while an unsupported or harmful result would prevent that commitment. This is a supplied value judgement. A large uncertainty by itself would not make the study worthwhile. The same effort could be unjustified when the staffing choice is already settled, the result will arrive too late, or an adequate existing answer is available.

If no competent provider is available on useful terms, the plan has not been obtained. The manager can finish the current allocation decision with no new study, retain the observed stage delays and leave the additional approver's causal effect unresolved. Alternatively, a worthwhile limited recording improvement can prepare a later decision. Specify what new availability, consequence or evidence would make reconsideration useful. Stopping expenditure neither proves the proposal ineffective nor increases confidence in it.



### RMP.Application:5.6 - Use the returned analysis at the strength it supports

Now suppose the planned work has been completed under the supplied conditions. In this constructed realization, all eligible requests have their sending and correction follow-up; the trace reports no lost cases, cross-branch assistance or changes to the approval rules. The analyst examines actual assignment, workload and conduct before accepting the planned analysis.

The returned time reductions, current arrangement minus new arrangement, are **1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6 and 2.8 working days** for the eight branch pairs. Their mean is 2.10 days. The analyst's qualified paired model uses the standard deviation of those eight contrasts divided by √8, giving standard error 0.173 days. With the stipulated t interval and seven degrees of freedom, the 95% interval is approximately **1.69 to 2.51 days**.

For correction rate, the paired changes, new minus current arrangement, are **−0.4, −0.2, 0, 0.1, 0.1, 0.2, 0.4 and 0.6 percentage points**. The mean change is +0.10 percentage points, with standard error 0.112 and the corresponding interval approximately **−0.16 to +0.36 percentage points**. The analyst has qualified this approximation for the case's branch rates; low event counts or a different dependence structure would require its own analysis. The [paired-mean interval formula](https://www.itl.nist.gov/div898/handbook/prc/section3/prc312.htm) lets a reader check this arithmetic. Arithmetic alone cannot establish assignment validity, model adequacy or recording fidelity.

| Predeclared condition | Returned result | Consequence for this use |
| --- | --- | --- |
| Lower time-reduction limit exceeds one working day. | 1.69 days exceeds 1 day. | The supplied analysis clears the case's meaningful-improvement criterion. |
| Upper increase in correction rate is below 0.5 percentage points. | +0.36 is below +0.5 percentage points. | It clears the case's average quality criterion; it does not establish zero harm or improvement in every branch. |
| Conduct and resources preserve the agreed comparison. | The stipulated trace supports the protocol conditions; the burden remains within the authorized allowance. | Return the bounded result for a staffing decision. A defeated condition would restrict that return even with the same numbers. |

The intervals express uncertainty under the supplied analysis, not a guarantee about the effect in every branch. In particular, one pair's observed correction-rate increase is 0.6 percentage points. The stated criterion concerns the average; a requirement that each branch stay below 0.5 would be a different decision and would not be cleared by this table.

[RMP.5](35-rmp-5---analyze-and-criticize-the-research-claim-under-its-m.md) connects the actual material, analysis and criticism to the claim. [RMP.8](38-rmp-8---use-research-results-to-retain-or-revise-an-episteme.md) returns the supported change in the knowledge account: **the specified additional-approver arrangement reduced average customer waiting under these branch, workload and monitoring conditions, with the stated remaining uncertainty and average quality bound**. This result does not establish that approval was the only source of delay or that every form of extra staffing would work.

The decision owner still compares the recurring benefit with the recurring burden and alternative uses of staff. Continuing in eight branches requires 160 approval hours per four-week period; extending to sixteen requires 320 under the same schedule. Suppose only 160 hours are available without sacrificing a more valuable commitment. A reasonable authorized action is bounded continuation where those hours can be provided, with the affected service outcomes observed. The research result informs that choice; it does not create the missing capacity or determine which branches should receive it.



### RMP.Application:5.7 - Change the shared-queue condition

Before copying this plan, suppose the manager discovers that "separate branches" actually send hard requests to one reserve approver. An additional approver can then change waiting in both assigned groups. The original branch contrast no longer has its assumed interpretation. Adding more request rows to the same shared queue cannot restore it.

Return the actual queue, staffing and transfer relation to the analyst through RMP.2 and RMP.3. The alternative might assign whole independent queues, study a whole-network intervention, or use a time comparison that explicitly handles trends, learning and carryover. Each changes what must be justified. Switching the same office between arrangements tomorrow and the next day is not automatically a valid substitute when staff retain what they learned.

If the organization has one shared queue and no obtainable design that can answer the causal question at worthwhile cost, finish with the supported descriptive answer and the unresolved effect. The original plan's numbers and intervals cannot qualify this different arrangement. A proposed new study remains a proposal until its needed construction and conduct exist.



### RMP.Application:5.8 - Keep the threats connected to actual decisions

Use these distinctions while inspecting the supplied plan and its execution. Each threat changes what the comparison or its result can support.

| Threat | What it changes in this application |
| --- | --- |
| Initial differences between groups | Pairing and random assignment address the comparison; inspect actual workload and complexity. Selecting only the worst branch for treatment and comparing it with an easier branch needs a different justification. |
| Reaction to being observed | Common recording makes the comparison refer to monitored work. Withdrawing that practice changes the conditions for transferring the answer. |
| Several changes introduced together | Record the actual treatment bundle. Adding a new priority rule as well as an approver estimates that bundle unless another justified comparison separates them. |
| Time, learning or carryover | The concurrent branch comparison and the changed shared-queue case require different dependence models. A later result may depend on earlier training or a seasonal workload change. |
| A convenient indicator replaces the goal | Keep actual sending time distinct from a changed promise or CRM update. Restore the event-to-measure relation before using the number. |
| Judgement affected by the observer | Use event records and an applicable correction rule, with assignment hidden from the assessor when feasible. Unavoidable awareness limits the resulting claim. |
| Repeated records mistaken for independent units | Analyze the assigned branches and matched pairs. Several records from one request, approver or branch do not supply additional independent assignments. |
| Inadequate recording resolution or precision | Inspect the recording operation and the planned uncertainty. More rounded rows may add no distinction; more genuinely informative units may still be too costly to obtain. |
| Selecting outcomes, analyses or stopping after seeing results | Preserve what was fixed beforehand and why later choices changed. An exploratory favorable subgroup can suggest another question; it does not retrospectively become the planned confirmatory answer. |

Before extending the result, check the receiving workload, staffing and interactions that its use depends on. Re-running the same data can expose a computational error; it supplies no new workplace cases. A relevant new-data check earns its cost through [RMP.6](36-rmp-6---choose-a-credibility-test-that-bears-on-the-research.md). The useful finish is the supported answer and the action it can inform, or a precise limitation with a justified next move.
