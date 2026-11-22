## RMP.Application:5 - APP-RMP-05 — Should a second approver reduce customer waiting?

Use this application when a workflow change raises a question about customer outcomes. Distinguish the outcome customers need from the indicator the organization records. The example shows how a manager can use process knowledge and arithmetic to frame the question and inspect a comparison. Use a qualified statistical design or analysis where that contribution is needed.

The branches, professional findings and numbers below are assumptions of a constructed case. They show what a manager can obtain and check in a specialist’s result. For another workplace, establish the design, sample and capability appropriate to that task. If your assignment is to design a study of a workplace problem, first use a request whose design has been left to you. State what would change for the recipient, what comparison you would make and which observations or prior findings could support it. In the case below, the measurement window, branch weights, professional analysis and funding thresholds are supplied. Checking their fit or arithmetic exercises a different part of the work.



### RMP.Application:5.1 - Find the question that matters

A quotations manager sees overdue offers and proposes a second approver. The manager distinguishes meeting the promised date from reducing the customer’s actual wait. Extending the promise can improve the first indicator with no change in the second. The manager wants to reduce the time customers actually wait for a usable quotation, with an acceptable limit on any increase in quotation errors. The office records request intake and sending on its working calendar. For the customer’s wait, establish when waiting starts and when a usable quotation first becomes available, including correction and redelivery when the first version cannot be used. Measure that interval on the relevant calendar.

The commissioned study below asks **whether the additional-approver arrangement shortens office working time from receipt of a request to sending the quotation.** That result can inform the wider customer question. A shorter office interval can coexist with later receipt by the customer. Missing input and difficult calculations are other possible sources of delay. Existing evidence can identify an adequate repair, such as restoring a failed forwarding rule. [RMP.1](31-rmp-1-decide-whether-a-question-needs-research-and-when-to-s.md) can return that answer for a repair question. Here the causal effect of additional approval capacity remains open and matters to recurring staffing.

Keep three questions separate:

- **Where did these quotations wait?** Use event records or another adequate source for the actual intervals.
- **Which mechanisms explain the waits?** Consider approval delay, missing input, or both, with initial complexity and workload affecting them.
- **What would the additional-approver arrangement change?** This needs a justified comparison of intervention versions and outcomes.

[Constructing and challenging a causal model (FPF C.28.CM)](../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md) helps specify the proposed mechanisms and their observable implications. Use the evidence to judge the connections drawn in a diagram.



### RMP.Application:5.2 - Obtain records that preserve the needed distinction

The CRM date labelled “status updated” may refer to an administrative edit after the quotation was sent. Establish what the field recorded. A suitable prior validation can answer, or compare retained messages and approval records with their CRM entries. The comparison can establish which office event the field tracks. For a question about receipt, establish how the recorded event relates to delivery. To date the end of the wait for a usable quotation, also establish that the version received was usable then or when a suitable correction reached the customer. Estimating the effect of a second approver requires an intervention comparison.

For one constructed request, the retained records show:

| Event | Recorded time | Working time since the preceding event |
| --- | --- | ---: |
| Customer request received | Monday 09:00 | — |
| Sufficient customer input received | Tuesday 10:00 | 9 hours |
| Calculation completed and submitted for approval | Tuesday 14:00 | 4 hours |
| Approval completed | Wednesday 16:00 | 10 hours |
| Quotation actually sent | Thursday 10:00 | 2 hours |

The office counts weekdays from 09:00 to 17:00. The four intervals add up to 25 working hours, or 3.125 eight-hour days. Of that time, nine hours elapsed before sufficient input, four before submission, ten between submission and approval, and two between approval and sending. The sum reconstructs the interval because these times belong to this request on one calendar and divide its whole path without gaps or double counting. A different distribution of those same 25 hours could change which delay a process repair should address. A CRM edit on Thursday at 11:00 would be another event.

Assess missing events, clock consistency, retrospective estimates, duplicate requests and the effort of recording. Use an existing validation or try the recording method where needed. If the history is missing, state the limit. Prospective recording can serve later cases when worthwhile. When both seven and eight hours have been stored as “one day”, more copies of the rounded values cannot recover the missing distinction.

[RMP.3](33-rmp-3---operationalize-the-research-design-without-replacing.md) connects the specification to the question, and [RMP.4](34-rmp-4---preserve-a-criticism-ready-research-trace.md) preserves what happened and what the evidence permits a recipient to examine. Compare intended recording with consequential departures. Stage durations can locate waits. The study’s intervention question concerns office working time until sending. To use that result for customer waiting, establish how the two calendars relate and how long customers wait for delivery and any necessary correction. These links must apply in the branches and periods covered by the decision.



### RMP.Application:5.3 - Separate a delay forecast from an intervention effect

Suppose a separate set of 30 old quotations contains 20 late and 10 on-time quotations. The head approver was absent for 13 of the late quotations and three of the on-time quotations. The odds of lateness are initially 20/10 = 2. On learning that the approver was absent, the likelihood ratio is (13/20)/(3/10) = 13/6. Updated odds are 13/3, corresponding to probability 13/16.

Under the stated table model, absence raises the predicted probability of lateness in those records. High workload or complex cases could coincide with absence, and a substitute could behave differently. Estimating an effect of the proposed staffing arrangement requires a suitable intervention comparison. For a forecast about later quotations, establish that the earlier table is an appropriate basis.

To compare approval delay, missing input and their combined contribution, identify which observations differ in expectedness under the accounts. Use likelihoods when the model supports them or a weaker contrast the available records permit. Two accounts can allow the same finding with different probabilities. When their expected findings coincide, report the unresolved distinction. Include plausible coexisting mechanisms and give any mixture of alternatives a justified composition.

Use [statistical inference under an observation model (MMP.13)](../foundational-thinking-dpf-suite/mmp/18-mmp-13---infer-unknowns-statistically-under-a-stated-observa.md) for the probability model and update, [observations that distinguish model alternatives (MMP.16)](../foundational-thinking-dpf-suite/mmp/22-mmp-16---design-observations-to-separate-mathematical-model.md) for the alternatives an obtainable observation can distinguish, and [intervention-effect identification (MMP.15)](../foundational-thinking-dpf-suite/mmp/20-mmp-15---identify-an-intervention-effect-from-available-data.md) for identification of the stated intervention effect. The manager can use the result relevant to the staffing question. The decision owner with authority to commit the resources decides under the applicable criteria.



### RMP.Application:5.4 - Ask for a comparison the organization can obtain and run

Before commissioning the analysis, the decision owner settles whose waiting time the proposed staffing should improve. Give every eligible request equal weight for a claim about the average request. For a claim about a branch selected with equal probability, give each branch’s mean equal weight. For a promised improvement in every branch, check what can be concluded for each. Agreement on the target determines what to ask the analyst to estimate.

To see why, suppose the same eligible cohorts and comparison give a reduction of three days for each of 10 requests in one branch and zero for each of 100 in another. The equal-branch mean reduction is 1.5 days. The equal-request mean is 30/110 of a day. The second branch has no reduction. Only the first mean exceeds one day. These stipulated reductions demonstrate what the quantities measure. To conclude that the actual study clears both funding criteria, use its two specified interval limits. Failure on either required criterion can rule out approval under that rule. An independent limit on staffing or expenditure may already settle the funding decision.

The owner of this trial wants a result for a branch at the stated workload and gives each participating branch equal influence on both outcomes. The manager asks the analyst to design a comparison for that target.

> We need to decide whether to fund an additional hour of approval capacity per working day in each participating branch. The new arrangement adds a trained approver during that hour using the existing rules. The current arrangement has no additional approver. We need working time from an eligible request to sending the quotation, including waits for missing input, and the change in the proportion of quotations requiring a customer-facing correction. Use the agreed equal branch weights. Specify the eligible cases and branches, assignment, treatment of unfinished or missing cases, comparison and uncertainty calculation.

The manager supplies workload and complexity records, staffing, queues, expected volumes, the reporting deadline and who can keep the records. Before seeing intervention results, the manager and decision owner set two criteria. The lower limit of the specified two-sided 95% interval for mean time reduction must exceed **one working day**. The upper limit of the corresponding interval for increased correction rate must be below **0.5 percentage points**. These criteria govern the case’s operating decision.

The analyst explains how assignment, outcomes, dependence, expected precision, observation period, analysis and stopping rule answer the question. [RMP.2](32-rmp-2-choose-a-criticism-bearing-research-design-or-stop.md) uses that construction to choose an obtainable design or finish with no new study. [RMP.3](33-rmp-3---operationalize-the-research-design-without-replacing.md) specifies or assesses the consequential operations. A worked branch and request can show the staff what the plan asks them to do. Use the qualified design and its grounds, including a sufficient existing explanation when available.

For the study branch, assume the analyst justifies the following arrangement for this workplace.

- Sixteen branches have separate customer populations, queues and approvers, with no shared reserve staff or transferred requests. Form eight pairs from prior workload, complexity and waiting records. Randomly assign one branch in each pair to each arrangement for the same calendar period. Admit requests for four weeks and continue the assigned staffing for six to cover follow-up. Specify how an unobserved sending or correction outcome would limit the conclusion.
- Estimate the average across these branches at the specified workload, weighting each branch equally. Calculate each branch’s mean for eligible requests arriving during the four weeks, then the eight paired branch contrasts. More requests can improve information on a branch. The eight assignments are drawn independently across pairs. Within a pair, assigning one branch to the new arrangement determines the other branch’s assignment.
- Determine eligibility at arrival. Include time spent obtaining missing input in total wait and keep approval time in the total effect. Follow each eligible request through sending and the agreed five-working-day correction window. Apply a specified rule to unsent, withdrawn or untraceable requests and disclose their numbers and treatment.
- Use the same recording and notification practice under both arrangements. Take times from their respective events. An assessor who can inspect quotations with assignment labels hidden applies the correction rule. Retain evidence of actual staffing, other changes and departures from the plan.
- The analyst uses historical variation and expected volume to qualify the proposed precision under stated assumptions. For this case the analyst supplies a paired-contrast model and interval calculation for eight pairs and four weeks of incoming requests. Assess design and precision afresh where the conditions differ.
- Set the primary outcome, weighting, interval calculation and analysis before inspecting outcomes. This workplace’s rule stops the trial for serious customer harm and returns the issue to the responsible decision-maker. Report missing records and staffing departures. Continue to the planned end under this stopping rule even if an interim result looks favourable. Retain the specified primary outcome and identify any additional exploratory analysis as such.

Pairing uses known background characteristics to improve comparability. Random assignment determines which branch within a pair receives the additional approver. Inspect the achieved balance and any shared queue. The [NIST account of randomized blocks](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) explains the distinction between the factor under study and background variation controlled by blocking. Qualify the specific workplace design from its own conditions.

Before relying on the workplace analysis, use the complete protocol and its grounds for unfinished cases, precision and analysis. The summary identifies what the manager needs to inspect and operate. If a required part is missing, obtain it from the analyst or another qualified source.



### RMP.Application:5.5 - Decide whether the study is worth obtaining

Suppose the comparison fits eight calendar weeks, with four for incoming requests, two more under assigned staffing to complete follow-up, and time for analysis and return. The eight assigned branches need 240 additional approval hours across six five-day weeks. Recording setup and checks take 24 staff-hours, analysis 32 and management 16. The total is **312 staff-hours**, within the allowance of 340. For the stated eight-week arrangement, suppose appropriately qualified staff can cover the assigned hours in each branch as well as recording, analysis and management when needed. The total alone settles the staff-hour budget question. The decision owner also considers which work the approval hours displace, customer disruption and the cost of delaying a staffing decision.

In this case the owner judges the expected answer worth the effort. A supported reduction could inform recurring staffing, and inconclusive or adverse evidence could prevent an unwarranted commitment. If the answer would arrive too late, a sufficient result already exists, or the choice is settled on other grounds, the same study could have less value.

If the comparison cannot be obtained on useful terms and no adequate design or result is already available, the manager can report the observed stage intervals and the unresolved staffing effect. The authorized decision-maker can decline the new expenditure. A limited improvement to recording can prepare later work if its contribution warrants the effort. State what new evidence, availability or consequence would matter to reconsideration.



### RMP.Application:5.6 - Use the returned analysis at the strength it supports

Now suppose the work was completed as specified. Every eligible request has sending and correction follow-up. The case records show no lost cases, cross-branch assistance or changes to approval rules. The analyst checks assignment, workload and conduct against the planned analysis.

The returned time reductions, current arrangement minus new arrangement, are **1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6 and 2.8 working days** for the eight branch pairs. Their mean is 2.10 days. The analyst's qualified paired model uses the standard deviation of those eight contrasts divided by √8, giving standard error 0.173 days. With the stipulated t interval and seven degrees of freedom, the 95% interval is approximately **1.69 to 2.51 days**.

For correction rate, the paired changes, new minus current, are **−0.4, −0.2, 0, 0.1, 0.1, 0.2, 0.4 and 0.6 percentage points**. The mean change is +0.10 percentage points, standard error 0.112, with an interval of approximately **−0.16 to +0.36 percentage points**. The analyst qualifies the approximation for these branch rates. Low event counts or different dependence could require another analysis. The [paired-mean interval formula](https://www.itl.nist.gov/div898/handbook/prc/section3/prc312.htm) supports checking the arithmetic. Examine assignment, model adequacy and recording against their own evidence.

| Predeclared condition | Returned result | Consequence for this use |
| --- | --- | --- |
| Lower time-reduction limit exceeds one working day. | 1.69 days exceeds 1 day. | The supplied analysis clears the case's meaningful-improvement criterion. |
| Upper limit of the mean increase in correction rate is below 0.5 percentage points. | +0.36 is below +0.5 percentage points. | The average meets the quality criterion. The limit for an individual branch or branch pair is a different question. |
| Conduct and resources preserve the agreed comparison. | The stipulated trace supports the protocol conditions; the burden remains within the authorized allowance. | Return the bounded result for a staffing decision. A defeated condition would restrict that return even with the same numbers. |

The intervals express uncertainty about the average under the qualified analysis. One pair’s observed correction-rate increase is 0.6 percentage points. The predeclared criterion concerns the average. These data do not establish that every branch or pair remained below 0.5 percentage points.

[RMP.5](35-rmp-5---analyze-and-criticize-the-research-claim-under-its-m.md) connects the observations, analysis and criticism to the claim. [RMP.8](38-rmp-8---use-research-results-to-retain-or-revise-an-episteme.md) returns the supported change to the knowledge account. **Under these branch, workload and monitoring conditions, the specified additional-approver arrangement reduced the equally weighted mean of the branches’ office working times from request receipt to quotation dispatch, with the stated uncertainty and the upper bound on the increase in the equally weighted mean branch correction rate.** Input and other stages can still contribute to delay. Assess differently specified staffing arrangements under their own conditions.

The decision owner can use this result for a staffing decision based on office dispatch time. For a decision about customer waiting, trace requests to the first usable quotation or establish a sufficient bound on the difference between that interval and the measured office time under both arrangements. Account for the customer’s calendar, correction delays and the weights the decision assigns to waits. When dispatch already makes the quotation usable on the required calendar and the weights fit, the existing result can suffice. The owner compares the warranted benefit with staffing costs and alternative uses of staff. At one hour each working day, eight branches need 160 approval hours per four-week period and sixteen need 320. Suppose 160 hours are available without displacing a more valuable commitment. The authorized owner may continue in branches that can be staffed within those hours and observe the relevant outcomes. The choice of branches and the capacity to serve them require their own grounds.



### RMP.Application:5.7 - Change the shared-queue condition

Suppose hard requests from apparently separate branches actually go to the same reserve approver. Additional capacity in one branch can change waiting in both assigned groups. The earlier contrast for independent queues no longer has its assumed interpretation. Increasing the number of requests within this shared queue preserves that dependence.

Give the analyst the actual queue, staffing and transfer relations for any design still needed through RMP.2 and RMP.3. Alternatives include assigning independent queues, studying a whole-network intervention or making a time comparison that accounts for trends, learning and carryover. A next-day switch in one office can retain learning from the previous condition.

With one shared queue and no worthwhile attainable design for the causal question, report the supported description and the unresolved effect. The original intervals apply to their own arrangement. A proposed study of the network can supply a design before the observations needed for any finding have been made.



### RMP.Application:5.8 - Keep the threats connected to actual decisions

When inspecting a plan or its execution, identify which conditions affect the comparison and what their presence would do to the proposed inference.

| Threat | What it changes in this application |
| --- | --- |
| Initial differences between groups | Pairing and random assignment address the comparison; inspect actual workload and complexity. Selecting only the worst branch for treatment and comparing it with an easier branch needs a different justification. |
| Reaction to being observed | Common recording makes the comparison refer to monitored work. Withdrawing that practice changes the conditions for transferring the answer. |
| Several changes introduced together | Record the treatment bundle. A valid contrast that changes both the priority rule and the number of approvers estimates their joint effect. Distinguishing the individual contributions requires a comparison that can do so. |
| Time, learning or carryover | The concurrent branch comparison and the changed shared-queue case require different dependence models. A later result may depend on earlier training or a seasonal workload change. |
| A convenient indicator replaces the goal | Identify the interval, whose calendar it uses and whose waits the decision weights. For customer waiting, connect dispatch to access to the first usable quotation, including any correction delay. |
| Judgement affected by the observer | Use suitable event records and an applicable correction rule. Where feasible, conceal assignment from the assessor. If the assessor knows it, examine what bias that could introduce and how it affects the claim. |
| Repeated records mistaken for independent units | Analyze the assigned branches and matched pairs. Several records from one request, approver or branch do not supply additional independent assignments. |
| Inadequate recording resolution or precision | Inspect the recording operation and the planned uncertainty. More rounded rows may add no distinction; more genuinely informative units may still be too costly to obtain. |
| Selecting outcomes, analyses or stopping after seeing results | Preserve what was fixed beforehand and why later choices changed. An exploratory favorable subgroup can suggest another question; it does not retrospectively become the planned confirmatory answer. |

Before extending the finding, examine the workload, staffing and interactions in the receiving setting. Re-running the same data can expose a computational error. If the question concerns other workplace cases, existing evidence about those cases may answer it. If new observations have been commissioned, obtain them under the agreed conditions or report an obstacle to the commissioner. When a further check is open for selection, assess it through [RMP.6](36-rmp-6---choose-a-credibility-test-that-bears-on-the-research.md). Finish with the supported answer or its precise limit. Where a decision is part of the task, state what the result can inform. If the commission concerns a request selected from all eligible requests, use request weights to calculate an overall mean when its value depends on them. For a threshold decision, a bound that covers the possible weights may suffice. To answer for customers, also establish how to count a customer with several requests. If it concerns every branch, ask whether the scope and precision of the branch results support that requirement. A changed target calls for reconsidering the part of the comparison it affects. Existing data or a bound that covers the new target may already answer it.
