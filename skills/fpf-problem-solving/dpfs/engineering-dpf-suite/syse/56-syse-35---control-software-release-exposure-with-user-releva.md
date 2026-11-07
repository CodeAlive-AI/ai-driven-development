## SYSE.35 - Control Software Release Exposure with User-Relevant Signals

> **Status:** Stable

> **Normativity:** Guidance within the stated software-release use; examples are illustrative.

### SYSE.35:1 - Problem frame

Use this pattern when a software change can reach a bounded population before wider use, and observations from that population can change the next exposure decision. Start with the actual deployed candidate and its deployment-test result from SYSE.41 or a current equivalent, not merely a package in storage.

The first result is an exposure-and-evaluation arrangement: the affected task, comparison, bounded population, observations, decision conditions and qualified recovery action. Once observations exist, it yields a bounded proceed, stop or inconclusive result. The responsible release holder supplies permission for the exposure and decides the reliance.

Do not require a canary for every change. A useful evaluation may be impossible when the relevant event is indivisible, too rare within the allowed interval, or has an irreversible consequence that cannot be bounded. Use a different qualified risk-reduction Method in those cases. A deployment whose actual state is still unknown returns to SYSE.41.

### SYSE.35:2 - Problem

A small deployment can still produce a large consequence through shared state or dependencies. A quiet dashboard can also reflect the wrong user task, absent instrumentation or too few relevant observations rather than a good change.

A comparison is misleading when candidate and control differ in workload, configuration or observation. Successful platform delivery does not demonstrate successful use of the delivered application. Exposure control must therefore connect actual runtime identity to a user-relevant question and a real action.

### SYSE.35:3 - Forces

| Force | Practical tension |
| --- | --- |
| Limited impact and informative observation | A tiny population reduces exposure but may never exercise the changed behavior. |
| Comparability and ordinary use | Controlled comparisons improve attribution while users, workloads and shared dependencies continue changing. |
| Prompt response and causal certainty | A credible harmful effect may justify reducing exposure before the full cause is known. |
| Technical reversibility and retained effects | Routing can change quickly while data writes, messages or other consequences persist. |

### SYSE.35:4 - Solution

#### SYSE.35:4.1 - Recover the candidate, task and permission

Identify the observed artifact/configuration and the interval for which its deployment result holds. Confirm the dependencies and data state required for the intended exposure. A process that starts is not automatically qualified for a user task that its deployment test did not exercise.

Name the service and users whose experience is at issue. Apply SYSE.36 to that subject and task population. A platform deployment-path objective and an application-use objective are separate even if the same dashboard displays both.

Obtain the relevant behavior meaning, reliability objective where applicable and exposure limit. Identify who can authorize the selected exposure and obtain their permission. If only isolated testing is permitted, construct the wider arrangement without executing wider exposure.

#### SYSE.35:4.2 - Choose the comparison and exposure unit

Choose a population or unit that can receive the candidate without invalidating the comparison: for example, a supported user cohort or a bounded set of work items. Identify the control and explain why its observations answer the same outcome question.

Account for task mix, resource conditions, data, time variation and other changes. Where requests from one task can cross candidate and control, preserve enough attribution to understand the result. A shared database or dependency can transmit the candidate's effects to the control; isolation is a condition to examine, not a label to assume.

Compare bounded exposure with alternatives such as a controlled representative exercise, independent feature activation through a qualified feature-flag or experiment configuration, or a planned cutover. Choose an arrangement that can both limit consequence and supply useful evidence. Increase exposure only when the additional information justifies the consequence within the authorized limit.

#### SYSE.35:4.3 - Define observations and three outcomes

Select observations that can reveal the consequential failures of the changed user task. Include correctness, delay and missing results as the task requires. Infrastructure indicators can help explain effects but do not automatically define user success.

Set the evaluation interval, observation delay and adequate-evidence conditions before judging the candidate. Use an appropriate statistical or domain Method when a quantitative inference requires it. A handful of successful attempts cannot establish a rare-failure probability merely because a tool returns a percentage.

| Outcome | Meaning and dependent action |
| --- | --- |
| Proceed basis | The stated evidence conditions and acceptance comparison are met for this population and interval; the authorized next exposure may be considered. |
| Stop basis | A stated unacceptable effect or violated operating condition has been observed; apply the qualified restriction or recovery. |
| Inconclusive | Required observations, attribution or discrimination are insufficient; do not convert absence of a failure signal into a pass. |

An inconclusive result can lead to a longer permitted observation, a better measurement, a different representative exercise or abandonment of this exposure strategy. Each changes an identified missing condition; repeatedly waiting on irrelevant traffic does not.

#### SYSE.35:4.4 - Qualify the stopping action

Determine what reducing exposure actually does. It may stop new task assignments, drain current tasks, change routing or disable a qualified feature. Observe the resulting state; a sent command is not proof that the candidate is no longer affecting users.

Use SYSE.34 for retained data and interface conditions. Returning traffic to an old executable is allowed only while that executable remains compatible with the actual state. Identify effects that persist after routing changes and who can resolve them.

Make the response available to the actual authorized person or mechanism. If the proposed stop requires unavailable access, an unsupported old runtime or a data restoration that has not been qualified, repair that premise before relying on bounded recovery.

#### SYSE.35:4.5 - Observe, act and retain the limits

During the permitted exposure, check that observations still concern the named candidate, control and task. Respond to credible harm without waiting for a complete causal account when the qualified stop is justified. Continue diagnosis through SYSE.38 as needed.

After reducing exposure, verify the user result and residual effects. After an adequate favorable result, return only the scope the evidence supports. Wider use, a different workload or changed state may need another decision.

Retain the useful observations and unresolved question in the working release account.

#### SYSE.35:4.6 - Construct an exposure sequence that can answer the release question

Start with the consequential difference introduced by the candidate. A changed form needs attempts using that form and its meaningful data variants; a changed scheduler needs enough whole jobs to expose assignment and completion behavior. Choose a unit over which the difference and its effects remain interpretable. For a stateless read it may be a request. For a multistep edit it may be a session or user cohort. For a job that runs for hours it may be a complete job and its output. Randomly distributing individual requests can spoil a comparison when one task then crosses incompatible versions or shares mutable intermediate state.

Choose the comparison for the available system. Concurrent candidate and control populations can reduce time-related differences, but only if task assignment, workload and dependencies make their results comparable. Before/after observation can be useful when concurrent operation is impossible; account for intervening demand and environmental changes and retain its weaker attribution where those cannot be controlled. An isolated replay can exercise a rare harmful case without live exposure, provided recorded inputs and simulated dependencies represent the behavior being judged. None of these arrangements is universally dominant.

Separate absolute protection from relative comparison. If candidate and control both fail because a shared database is saturated, their similar error rates are not a healthy result. Keep an absolute task or service limit that can stop the exposure even when relative comparison is neutral. Conversely, a control's unrelated failure should not automatically condemn the candidate: investigate whether the compared populations and conditions still answer the chosen question. A release observation can justify protecting users before it establishes which component caused the harm.

Choose successive exposure bounds from the information and consequence at each step. A first step can establish installation and basic behavior; another can cover ordinary task variants; another can reveal sustained resource or dependency effects. Reuse applicable observations rather than replaying every earlier exercise, but obtain the evidence introduced by the wider scope. The fraction of traffic alone is insufficient: ten percent of an infrequent task can yield no useful observation, while one percent of a high-impact write stream can already create extensive persistent effects.

Select the duration from task completion, observation delay and the failure mechanism. A latency comparison can stabilize sooner than a memory leak, cache invalidation, scheduled job or end-of-day reconciliation. Exclude or model warm-up behavior deliberately instead of letting it silently decide the result. Make sure the metric window contains candidate observations from the intended interval; a long aggregate dominated by the previous version can hide a new failure. For a rare-failure probability, obtain a suitable statistical design rather than choosing a convenient count of successes. For a known unacceptable semantic defect, one demonstrated occurrence may already be decisive under the acceptance rule.

At each step, decide what a favorable result permits next and which condition requires a pause, stop or return. Make widening an explicit operation with the required authority. A fully automated sequence is useful when these predicates and actions are qualified. A human decision is useful when the next step needs interpretation; supply the actual evidence and alternatives rather than a color asking for reflex approval. If stopping cannot bound the relevant harm, replace the exposure strategy before running it.

For ParcelWorks, a session-bound cohort keeps a complete edit on one form version. The first permitted exercise includes absent, empty and non-empty address tails, because those distinguish the changed behavior; general browsing cannot substitute for them. After those cases pass, a later step can study ordinary edit load and response time. For an asynchronous importer, use whole import batches and compare validated output after completion instead. In that case a five-minute window containing only job starts cannot establish successful import, even if every start request returned promptly. The same construction changes its unit and duration while retaining the result question.

### SYSE.35:5 - Archetypal Grounding

In a constructed ParcelWorks case, SYSE.41 has established a candidate application h2/c2 on two isolated instances, with a successful bounded deployment test. The old h1/c1 pool serves ordinary traffic. The data construction from SYSE.34 retains the old address contract, so a qualified return remains possible. A release holder permits a limited application exposure with a defined stop.

The changed task is viewing, editing and saving an address. The application owner supplies its meaning: the new form must display the first line and remaining text correctly and preserve the submitted value, including an empty versus absent tail. The common outcome comparison is correct address use under each form's supported contract, not identical screen layout.

The arrangement identifies the candidate/control configuration for each relevant attempt. A version/snapshot or controlled observation distinguishes later legitimate edits from corruption. The exposure remains bounded until the agreed behavioral and observation conditions are met; an HTTP response code alone cannot establish the address result.

In the first constructed interval, nine general application requests reach h2/c2, but none uses the changed address form. The relevant task has no observations. At the same time, the platform has completed ten supported deployment requests successfully within its own agreed response bound. Those are good platform observations, not evidence about the application form.

| Observation | Exposure conclusion |
| --- | --- |
| Nine candidate requests, none exercising the changed form. | Inconclusive for the form change; relevant evidence is missing. |
| Ten successful platform deployment tasks. | No change to the application conclusion; this is another measured subject. |
| A permitted form attempt hides a non-empty tail, although the backend stores it correctly. | The application acceptance condition fails; stop or reduce exposure within the qualified boundary. |
| Candidate/control identity is absent from the form observation. | Attribution is missing; do not infer a favorable comparison. |
| The required representative cases succeed under the agreed comparison and observation conditions. | A bounded favorable basis exists for the named next decision, not a universal correctness claim. |

In the adverse form attempt, the candidate was deployed exactly as requested. The defect is therefore not evidence that the platform failed to install h2/c2. The authorized response keeps or restores ordinary routing to the qualified old pool, handles in-flight work according to the selected rule and verifies that the old form still reads and preserves the current data. Diagnosis of the hidden tail can then proceed without continuing unnecessary exposure.

If the state had crossed SYSE.34's incompatible boundary, that routing return would no longer be a sufficient recovery. The release holder would need the qualified forward repair or restoration result rather than a misleading “rollback complete” message.

The [Argo Rollouts analysis model](https://argoproj.github.io/argo-rollouts/features/analysis/#inconclusive-runs) provides a concrete implementation comparison: an inconclusive analysis can pause progression for a decision. Its status does not choose the right metric or guarantee that missing observations were configured correctly.

What changes in practice is that insufficient evidence can stop widening exposure without being misreported as either proven success or a diagnosed application defect.

### SYSE.35:6 - Bias-Annotation

Release pressure can turn every neutral signal into permission to proceed. A convenient cohort can also avoid the very behavior being changed. Inspect relevance, missing observations and shared effects, and preserve a legitimate inconclusive outcome even when the planned release interval is ending.

### SYSE.35:7 - Conformance Checklist

- The actual deployed candidate and its bounded deployment result are available.
- Subject, users, task and acceptance meaning are distinct from platform-delivery success.
- Candidate/control observations are relevant, attributable and sufficiently informative for the stated inference.
- Proceed, stop and inconclusive conditions have different consequences.
- The stop/recovery action is authorized and compatible with actual retained state.
- Wider exposure is not inferred from a quiet dashboard or a controller's success label.
- Residual effects and restored user behavior are observed after stopping.

### SYSE.35:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Count all application traffic as evidence for a rare changed task. | Observe the relevant eligible attempts or return insufficient evidence. |
| Treat platform deployment success as application acceptance. | Measure the application task under its own meaning and configuration. |
| Stop routing and assume every effect vanished. | Account for in-flight work, retained data and shared dependencies. |
| Automatically accept missing or empty metric results. | Configure and exercise the intended missing-evidence disposition. |

### SYSE.35:9 - Consequences

Bounded exposure can reveal defects while limiting affected use. It costs comparison design, observation and recovery capability, and it can delay a decision when relevant traffic is sparse. A truthful inconclusive result preserves a choice of better evidence instead of manufacturing confidence.

### SYSE.35:10 - Rationale

Exposure is useful as an engineering move only when it produces relevant discrimination and supports a qualified response. Runtime identity, task meaning and recovery conditions connect the experiment to actual consequences. A comparison alone does not create permission to impose those consequences.

### SYSE.35:11 - SoTA-Echoing

For bounded release evaluation, **adopt and adapt** the developed 2018 [SRE Canarying Releases](https://sre.google/workbook/canarying-releases/) treatment. It already explains candidate/control selection, contamination, timing, absolute protection and long-running work. Section 4.6 applies those considerations to choosing a task unit and a sequence whose observations can decide the next exposure.

**Adopt** an explicit inconclusive outcome, concretely supported by [Argo Rollouts analysis](https://argoproj.github.io/argo-rollouts/features/analysis/#inconclusive-runs). The tool can enact a pause but cannot establish task meaning or adequate evidence. Compare concurrent canarying with replay, before/after observation and planned cutover according to representativeness, shared effects, consequence and available stopping action.

Reopen the arrangement when the changed behavior, workload, telemetry, data compatibility or recovery permission changes. A favorable smaller exposure supports its actual comparison; it is neither universal correctness nor automatic permission for wider use.

### SYSE.35:12 - Relations

SYSE.41 supplies the observed deployment; SYSE.36 supplies matching task measurement and objectives. SYSE.34 bounds stateful return, SYSE.38 supports diagnosis/restoration, and SYSE.40 addresses overload that can contaminate exposure. SYSE.4 governs evidence reliance and SYSE.14 the actual release decision.

### SYSE.35:End
