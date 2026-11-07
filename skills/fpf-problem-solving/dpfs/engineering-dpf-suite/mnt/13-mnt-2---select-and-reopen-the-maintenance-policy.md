## MNT.2 - Select and Reopen the Maintenance Policy

> **Type:** Method
> **Status:** Stable

### MNT.2:1 - Problem frame

Use this pattern when a recurring maintenance task, inspection interval or proposed technology needs a reason to be retained or changed. A calendar says “replace every year,” but the planner cannot explain which failure this prevents or why a different task would be worse.

Choose a reusable maintenance policy for the identified functioning and failure situation. Here a policy states which task applies and under what condition it is performed. The first result can be a justified decision to retain the current policy. A one-off response to today's condition belongs in [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md); a fleet-wide support and work decision belongs in MNT.13.

### MNT.2:2 - Problem

Task frequency and technical sophistication are poor substitutes for policy reasoning. An age-based replacement may remove a wear-related failure, do little for a largely age-independent fault or introduce a new installation fault. A sensor may observe degradation without leaving enough time to obtain a part and act.

A policy therefore needs a credible connection between failure behaviour, what the task can change, the consequence of waiting and the practical burden of intervention.

### MNT.2:3 - Forces

Prevention can avoid an expensive failure but consume useful component life and introduce disturbance. Frequent inspection can shorten detection delay while consuming access and interpretation effort. Keeping stock shortens response time but ties up resources and can leave obsolete parts. Hidden protective functions create a different trade-off from failures that operation immediately notices. Compare these consequences within the maintained use; do not reduce every value to downtime alone.

### MNT.2:4 - Solution

Start from the required function and a failure account sufficient to distinguish policy alternatives. Identify the loss of function, credible mechanisms and consequences. When one policy covers several mechanisms, check each mechanism that could justify a different task. Retain uncertainty where it matters rather than inventing a lifetime distribution from sparse events.

Construct the plausible task alternatives. The following distinctions help select a task; they are not a ladder of maturity.

| Task family | What can make it useful | What can defeat it |
| --- | --- | --- |
| Corrective or deliberate run-to-failure | Failure is detectable and its consequence, recovery demand and collateral effects are acceptable for the use. | A hidden protection loss, unacceptable exposure or unavailable recovery capability makes waiting untenable. |
| Age- or usage-based action | Failure behaviour and restoration effectiveness support acting before a relevant age or usage condition. | Calendar age is a weak predictor, or replacement repeatedly introduces faults. |
| Condition-based action | An observable condition changes early enough to support a useful response. | The relevant failure is not detected, the alarm is unreliable, or response lead time exceeds the usable warning. |
| Failure-finding | A task reveals loss of a function that normal operation does not expose, such as a standby protective function. | The test misses the relevant failure or creates unacceptable exposure without adequate controls. |
| Opportunity-based combination | Shared access or downtime makes coordinated tasks worthwhile. | Bundling consumes useful life, creates interference or overcommits the outage. |

For each credible alternative, explain what performing the task changes. Include imperfect repair, task-induced defects and residual failure modes when material. If no acceptable maintenance action addresses a serious failure, return the specific redesign, redundancy or changed-use question to engineering or operation. Adding inspections that cannot reveal or alter the failure is not a substitute.

For condition-based work, reason across the complete response. The usable interval between detectable degradation and unacceptable functioning must accommodate detection delay, interpretation, obtaining support, access and the selected intervention, with uncertainty appropriate to the consequence. This is an applicability question, not a universal formula for a safe interval. A local detection threshold or interval needs the equipment and operating evidence that supports it.

Compare alternatives using the receiving use's relevant values: loss of service, exposure, labour, material, disturbance, environmental effects and uncertainty. Use comparable operating horizons and state deliberately accepted trade-offs. Existing adequate evidence may already settle the choice. Select further investigation only when an attainable answer could change it enough to justify acquisition, interpretation, delay and displaced work.

State the chosen policy in actionable terms. Name the applicable population or configuration, task, trigger or interval basis, relevant support assumptions, response to an out-of-scope condition and the evidence or changed use that would reopen it. Where an operative requirement fixes a task, preserve its current force. A separate merits appraisal may support a request to the authorized rule holder; it does not authorize unilateral relaxation.

#### MNT.2:4.1 - Turn a task family into a usable policy

Use an adequate existing task and trigger directly. When they are unsettled, construct candidate rules at the resolution needed for the decision. Specify what observation, age, usage or opportunity starts the response, when that information becomes available, what action follows and what functioning is expected afterwards. A condition-based candidate includes its observation schedule and response; a scheduled replacement includes what happens if failure occurs first.

Apply each candidate to the same supported failure and operating account. Follow the relevant histories from functioning through degradation, discovery and response to the resulting state. Include a failure before the planned task and the condition after imperfect repair where those branches matter. Use [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md)'s failure account and [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md)'s condition account; obtain an applicable equipment-specific model when projection needs further transition or task-effect evidence. If a consequence needed for the comparison cannot be supported, return that missing contribution rather than assign the desired effect to the task.

Derive the consequences of those histories over a common horizon. Count functioning obtained, losses before detection or restoration, repeated task demand and support constraints. Weight possible histories only where the probability basis supports it; otherwise compare the supported bounds or scenarios. Keep binding requirements and unacceptable consequences visible when comparing burden. Use [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) with the resulting alternatives and comparison basis to select a policy, retain several alternatives or return the unsettled choice.

For a condition-based candidate, place detection and response on one time basis. Let `W` be a supported lower bound on the warning from the proposed detectable condition to unacceptable functioning under the intended duty. Let `I` bound the wait to the next observation and `L` bound the elapsed time for subsequent interpretation, support, access and intervention, including the selected uncertainty allowance. Where that bounded timing model applies, test `I + L <= W`. Derive elapsed `L` from actual sequencing and available overlap through [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and MNT.7. Shorter sampling, an earlier detectable trigger or prepared support are different candidate changes; each needs its own measurement or feasibility basis. A timing fit still needs adequate detection and an effective response.

For a hidden protective function, relate the test interval to the period during which the failed function could remain undiscovered and the consequences of a demand during that period. The test's coverage, any exposure it creates and the relevant failure-and-demand account determine whether the interval is acceptable. Continuing normal production supplies no observation of that protective function.

##### MNT.2:4.1.1 - Build and improve a predictive maintenance option

Use this branch to develop a maintenance policy whose response depends on a forecast or other conditional estimate. An adequate existing estimate and decision rule can be used directly. A competent practitioner's condition assessment can supply the estimate; fitting a statistical model is one possible means.

Start with the decisions the estimate should improve. Determine the available interventions and windows, what continued operation may lose, and what an earlier intervention consumes or disrupts. Connect observations available at the decision time to an estimate of the relevant failure or functioning, then to an intervention rule. This makes the forecast useful through the action it permits and the functioning that action can obtain.

Apply each candidate rule to the supported histories described above. Compare the resulting functioning and burden, including consequential early interventions, missed failures and delays. Examine which differences between estimates change the chosen response. A smaller prediction error that leaves every consequential action unchanged may add little maintenance value; an error near an action boundary can reverse the choice. Keep the required service and other binding conditions in that comparison.

Construct a better response where an obtainable support change makes it possible. Use [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) to establish how the needed part, provider and preparation can be obtained, and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) to construct a feasible window and service arrangement. Bring the required lead times, commitments and burdens back into the candidate. Advance preparation can shorten the delay between warning and intervention; another window can make a previously unusable warning actionable. Compare this complete arrangement with the current one, including preparation and recurring support. Recalculate the response rule when those returned conditions change.

When the forecasting or response rule itself needs development, use FPF C.40:4.7. Supply the permitted variations, the observations each variant may use, its feasible interventions and the maintenance consequences by which its use will be judged. Use the consequences to identify estimate errors that change a useful action, then vary the relevant assessment, trigger or response rule. Compare those revisions through the maintenance consequences of their selected actions. Return the forecasting or assessment rule together with its response rule and support conditions. A small comparison of expert assessments or rules can suffice.

If model fitting is useful, one implementation tunes the prognostic model using a loss derived from the interventions selected by a chosen policy. Keep that policy's windows and consequences with the fitted model. Such tuning can improve maintenance decisions while worsening a prediction score; any required probability calibration claim still needs its own support. Use [MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) for a supported failure and task-effect account, including lifetimes censored by replacement. Keep consequences estimated through that account distinct from outcomes observed in maintenance.

Select a feasible change when the current observations, applicable model or reasoned expert estimate make its expected benefit worth its complete burden under the relevant uncertainty. Use ranges, scenarios or a qualitative comparison when they are sufficient. Return the policy and the next executable preparation or intervention decision, with the assumptions whose change could reverse the choice. New data or a trial are needed only when their attainable contribution warrants the burden; absence of an already observed improvement does not by itself prevent acting on a reasonable estimate.

#### MNT.2:4.2 - Compare recurring age-replacement costs when that model fits

Suppose replacement restores the component to an as-new state, successive lifetimes `X` are independent with the same distribution, intervention duration is negligible, expected cycle duration is positive and finite, and costs cover the relevant consequences. For replacement at age `a` or earlier failure, derive the two possible endings from the lifetime model, counting a failure at age `a` as corrective:

- the cycle's operating duration is `min(X,a)`;
- corrective cost `Cc` applies when `X <= a`, and planned cost `Cp` otherwise.

The long-run cost per operating-time unit is

`g(a) = [Cc * P(X <= a) + Cp * P(X > a)] / E[min(X,a)]`.

Compare feasible ages, including continued operation to failure where admissible. This calculation includes how often replacement recurs. Use another model when downtime, imperfect restoration, changing duty or coupled components invalidate these assumptions; a finite service horizon also needs its own end condition. See [Arts and colleagues, §2.2.1](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf) for the renewal-reward basis and its limits.

### MNT.2:5 - Archetypal Grounding

For PS17, the constructed condition history supports a bearing-related deterioration concern. The team retains a condition-informed policy for this failure family because the interpreted signal can support a planned response in the stated use. The present recommendation still depends on actual support and access; an alarm alone does not establish that replacement can fit the next outage.

Consider instead a cheap, accessible indicator lamp whose failure is obvious and has no protection role. If its loss and replacement demand are acceptable, deliberate run-to-failure can be a sound policy. Scheduling repeated intrusive replacement needs an additional gain to justify its burden.

The same choice is unsuitable for an otherwise unobserved protective trip function. Normal production can continue while that function has failed. A suitable failure-finding task addresses that detection problem; an operator's observation that “the line still runs” does not. The applicable specialist basis determines the test and interval.

In the 48-pump fleet example, the operating exposures differ, and policy selection is not randomized. Four failures versus six do not by themselves justify replacing the policy. Retain the current policy when its existing failure-and-response basis remains adequate; address the known spare-support deficiency on its own existing evidence. Failure to prove a better rival does not establish that the current policy is adequate.

#### MNT.2:5.1 - Construct an age rule from a failure model

In a separate constructed comparison, a replaceable component lasts 6 or 10 operating-time units, each with probability one half. Replacements meet the assumptions in MNT.2:4.2. The three available candidates are replacement at age 4, at age 8, or at failure. All are admissible for this use. Planned replacement costs 2 units and corrective replacement costs 10, including the case's failure consequences.

At age 4 every cycle ends with planned replacement: cost per operating-time unit is `2/4 = 0.5`. At age 8, half the cycles fail at 6 and half reach planned replacement at 8: expected cost is `0.5*10 + 0.5*2 = 6`, expected duration is `0.5*6 + 0.5*8 = 7`, and the rate is `6/7`, approximately 0.857. At failure the rate is `10/[0.5*6 + 0.5*10] = 1.25`. Age 4 is preferred among these three candidates on the declared cost criterion; this comparison has not searched all possible ages.

Now change only corrective cost to 3. The rates become `0.5`, `2.5/7`, approximately 0.357, and `3/8 = 0.375`. Age 8 becomes preferred. The failure model and task family remain unchanged; the consequence change reopens the interval choice.

#### MNT.2:5.2 - Construct a condition-response timing candidate

In another constructed case, the supported warning bound `W` is 8 hours and the subsequent response demand `L`, including its uncertainty allowance, is 5 hours. Observation every 4 hours gives a bound of `4 + 5 = 9` hours and cannot meet that warning. Every 2 hours gives `2 + 5 = 7`, so it passes this timing comparison. The remaining choice includes the burden of more frequent observation and the alternative of reducing response demand.

If support delay raises `L` to 6.5 hours, the two-hour candidate no longer fits: `2 + 6.5 = 8.5`. Reconsider sampling, support or another admissible policy. The failure threshold has not moved, and the old timing result supplies no permission to extend use. These quantities illustrate construction from a supplied equipment model; they are not operating limits.

#### MNT.2:5.3 - Obtain a useful response from a conditional estimate

Consider a constructed ten-day service horizon. The current arrangement replaces a component on day 5; obtaining a compatible spare and an agreed access window permits replacement on day 1. Suppose untreated failure is on day 2 with conditional probability `p`, and otherwise after day 10. For this comparison, replacement prevents that failure for the remaining horizon. Both options meet the other binding requirements. All distinguishing costs are included: day-5 replacement costs 20 if the component survives, while failure before it costs 100 in total. Day-1 replacement costs 20 plus 10 for advance support and early intervention.

The expected cost of the current arrangement is `100p + 20(1-p) = 20 + 80p`; the prepared early response costs 30. A condition estimate `p = 0.20` therefore favours the new arrangement: 36 versus 30. Even a supported range `0.15 <= p <= 0.25` leaves the current arrangement at 32–40. MNT.5 establishes the spare's readiness and MNT.7 obtains the window; their result makes the day-1 response available. The selected move is to arrange that support and replace on day 1, without requiring another experiment merely because the benefit is still an estimate. An adequate expert condition estimate can supply this input.

To examine improvement of the estimating rule, take two equally common condition groups with probabilities 0.10 and 0.20 in the comparison model. Both forecasting variants use information available before the choice; their development and use costs are equal here. Each selects the lower expected-cost action using its own probability estimate and the same available responses.

| Forecasting variant | Estimates for the two groups | Mean absolute probability error | Selected responses | Mean cost under the comparison model |
| --- | --- | --- | --- | --- |
| A | 0.11; 0.12 | 0.045 | Day 5; day 5 | `(28 + 36) / 2 = 32` |
| B | 0.02; 0.18 | 0.050 | Day 5; day 1 | `(28 + 30) / 2 = 29` |

B has the larger prediction error but selects the more useful response in the second group. Comparing the consequences therefore favours B for this use; it does not establish B as the better probability model for other uses. The probabilities supplying this examination are stipulated model inputs, not information assumed available during a real intervention.

If the added cost of the early arrangement rises from 10 to 25, its total becomes 45. At `p = 0.20`, the day-5 arrangement's 36 now wins. Reopen the response and forecast comparison with that changed support cost, or construct another obtainable arrangement. Under the changed costs, both forecasting variants choose day 5 for both groups and have mean model cost 32, so their earlier cost ranking disappears. These calculations illustrate the construction and return; they are not measured field savings.

### MNT.2:6 - Bias-Annotation

Breakdowns are conspicuous; unnecessary preventive work and failures introduced by maintenance can disappear into ordinary cost codes. Include those consequences in a comparison. A vendor's technology categories can also favour its own sensor or software offering over a simpler adequate task.

### MNT.2:7 - Conformance Checklist

Does the policy address a stated functioning loss and credible failure behaviour? Can the selected task detect, prevent, mitigate or restore the relevant failure in time? Are consequence, support and task-induced effects considered where they distinguish the alternatives? Is the chosen applicability and trigger usable by the intended practitioner?

A retain decision can close the question. New trials, a complete failure model and numerical optimization are warranted only when their obtainable contribution changes this choice.

### MNT.2:8 - Common Anti-Patterns and How to Avoid Them

“Predictive is better than preventive” ranks technology without the failure and response conditions. Compare what each arrangement can actually change. “We have always replaced annually” conceals the interval's basis; recover that basis and reopen only the unsupported choice.

A protective function that has never been demanded can appear failure-free. Examine how its failed state would be detected before choosing run-to-failure.

### MNT.2:9 - Consequences

The chosen task has an explicit maintenance contribution and a useful reopen condition. Some existing work can be retained; some unnecessary work can stop through the applicable decision. Where no task provides an acceptable answer, the Method makes the engineering or operating problem visible instead of disguising it as a maintenance backlog.

### MNT.2:10 - Architectural Rationale

A reusable policy differs from a current intervention choice: one establishes when a task generally applies, while the other resolves a present case. Keeping them related but separate permits a valid policy to coexist with an exceptional current response.

The task alternatives remain plural because failure visibility, mechanism, consequence and support differ. A single escalating technology sequence would discard legitimate corrective and failure-finding policies.

### MNT.2:11 - SoTA-Echoing

For the question “Which task is worth performing for this failure?”, this pattern adapts the applicable/effective task reasoning of NASA's historical 2008 RCM guide and the mechanism-plus-decision-model line discussed by Arts and colleagues in 2025. It rejects a technology ladder as the policy rule: the comparison table and complete-response reasoning preserve corrective, hidden-function and support-limited cases that the ladder obscures. More demanding models remain useful when their decision gain warrants their effort. Neither source supplies a universal interval or permission rule. Reopen when failure behaviour, warning time, restoration effectiveness or the operating consequence changes. See the [RCM task discussion](https://www.nasa.gov/wp-content/uploads/2023/06/nasa-rcmguide.pdf) and [maintenance optimization account](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf).

For improving forecasts through the decisions they induce, [Xie, Abdin and Fang (2025), §§2–5](https://arxiv.org/html/2506.19698v1) supply one ML realization: fine-tune a prognostic model against maintenance consequences under a selected policy and given windows. Their numerical evidence uses NASA C-MAPSS FD001 simulation, not universal field superiority. The extension to changing obtainable support in MNT.2:4.1.1 combines MNT.5 and MNT.7 with this pattern's policy construction; it is not a result established by that study. FPF C.40:4.7 supplies the general Method of developing a way by what its use produces.

### MNT.2:12 - Relations

[MNT.3](14-mnt-3---establish-degradation-and-failure-evidence-for-maint.md) supplies failure evidence and [MNT.4](15-mnt-4---monitor-and-interpret-system-condition-for-maintenan.md) supplies condition interpretation. [MNT.5](16-mnt-5---prepare-maintenance-service-capability-spares-tools.md) and [MNT.7](18-mnt-7---coordinate-maintenance-intervention-and-continuing-o.md) qualify response feasibility; [MNT.6](17-mnt-6---diagnose-condition-and-choose-a-maintenance-response.md) selects the present intervention. [MNT.13](24-mnt-13---coordinate-the-maintenance-programme-and-fleet-lear.md) uses policy consequences across a fleet and [MNT.14](25-mnt-14---compare-maintenance-methods-for-retention-or-change.md) compares Method changes. [FPF C.11](../../../sections/09-part-c---kernel-extension-specifications/21-c-11---decision-theory.md) supports comparison, and [FPF C.11.DUA](../../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) governs a disputed evidence demand or requirement appraisal.

### MNT.2:End
