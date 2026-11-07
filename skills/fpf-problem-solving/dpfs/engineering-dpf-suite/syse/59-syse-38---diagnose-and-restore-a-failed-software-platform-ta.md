## SYSE.38 - Diagnose and Restore a Failed Software-Platform Task

> **Status:** Stable

> **Normativity:** Guidance within the stated software-platform recovery use; examples are illustrative.

### SYSE.38:1 - Problem frame

Use this pattern when a practitioner cannot obtain a supported result from a software platform, or receives an uncertain result after a failed attempt. Start with that attempt, its intended outcome, the affected path stage and the current observable effects.

The first result is a restored user task or a usable limited result after mitigation, with remaining limits stated, or a narrowed unresolved cause question with a request for the specific result needed from a specialist. The priority is a useful, qualified response to the impact, not a complete causal explanation before any mitigation.

If a known narrow failure already has a qualified repair procedure, use it and verify the result; a new investigation framework is unnecessary. For a coordinated major incident, use the response Method in section 4.5 with the actual local assignments. A single ordinary failure does not automatically require its entire command structure.

### SYSE.38:2 - Problem

“The platform is down” can conceal several different failures: a request never entered, work is waiting, a provider failed, a runtime changed only partly, or the result was produced but not returned. Blind retry can duplicate resources or repeat irreversible effects.

Diagnosis can also become an uncontrolled sequence of restarts and configuration changes. When the service later recovers, nobody knows which explanation survived, whether the original task completed or whether data was restored.

### SYSE.38:3 - Forces

| Force | Practical tension |
| --- | --- |
| Restoration and explanation | Reducing current harm can be urgent while complete causal understanding takes longer. |
| Evidence and intervention | A useful repair changes the state being investigated; enough prior evidence should survive without prolonging avoidable harm. |
| Local action and shared effects | One task can fail because of a common dependency, and its retry can make other tasks worse. |
| Fast assistance and real authority | An available expert may understand the fix without permission to alter the affected service or information. |

### SYSE.38:4 - Solution

#### SYSE.38:4.1 - Establish the failed task and actual impact

Recover the expected supported result, actual observation, attempt identity, relevant configuration and time. Distinguish the user's report from a controller's interpretation and from an observed target state.

Locate the failure sufficiently to choose a next action: entry, admission, waiting, execution, dependency, result validation or result delivery. Determine who and what are affected, what still works, and whether a useful old path or limited fallback remains.

Use the shared operating account when several people need the same current situation. OPS.3 distinguishes operating subjects, cases, queues and resources; OPS.4 supports shared attention to their actual state. A platform log can contribute without becoming the whole operating account.

#### SYSE.38:4.2 - Reduce impact within a known boundary

Select a useful mitigation within the applicable risk limits, actual permission and current state. It may restrict new work, preserve an old serving path, isolate a failed component or use an already qualified alternative. State what remains unavailable or degraded.

Before reattempting a state-changing operation, determine whether it took effect. Query the original attempt or target where possible. If observation is unavailable and repetition could duplicate or corrupt effects, stop that repetition and return the uncertainty for the appropriate assistance.

Use SYSE.34 for uncertain data effects and SYSE.41 for partial deployment state. A restarted process does not prove restored information. A proposed fallback whose capacity, compatibility or authority is unknown is not yet a recovery path.

#### SYSE.38:4.3 - Discriminate plausible explanations

Form competing explanations that account for the observed failure. Name what would distinguish them. Prefer available read-only evidence or a bounded, qualified experiment that can actually change the next decision.

Compare observations at the relevant path boundaries. Long queue waiting and short execution suggest a different problem from immediate admission followed by a dependency timeout. A correlation with a recent change is a lead, not proof that the change caused the failure.

Make one interpretable intervention at a time where practical. When urgent response requires several actions, retain their timing and effects and avoid claiming that the final action alone established causation. Preserve the useful configuration, attempt and failure evidence within its data-handling limits.

If the remaining question needs a specialist, return the observed failure, surviving alternatives, constraints and result needed. Do not transfer an unbounded “please fix the platform” problem when a narrower question is already known.

#### SYSE.38:4.4 - Verify the user result and residual effects

After mitigation or repair, exercise the affected supported task or recover the original result. Observe identity, correctness and timing to the degree the task requires. A healthy process, an empty queue or an acknowledged alert is not by itself task recovery.

Check partial resources, in-flight work, retained state and consequences for other users. Preserve a bounded degraded result when full restoration is not yet established. Report what is restored, what remains limited and what action still has a holder.

Do not confuse a successful later attempt with completion of an earlier one. Resolve the earlier attempt's effects or keep its uncertainty visible.

#### SYSE.38:4.5 - Use the major-incident response Method when coordination is needed

Apply [PagerDuty, During an Incident](https://response.pagerduty.com/during/during_an_incident/) for coordinated major-incident response, adapted to the organization's actual severity decision, people and communication facilities. Its operative contribution is coordinated command, expert investigation/repair, a shared working account and internal/customer communication through assigned roles.

Supply the actual incident lead and supporting assignments, permitted technical actions, communication authority and available contact paths. Follow the selected source's role-specific instructions through those local bindings. Its sample chat commands, role availability and public-announcement discretion are not automatically local facts.

The first coordinated result is an actively managed response with assigned work and shared current information, followed by a bounded recovery/continuation decision. Report missing assignments or permissions to the people authorized to provide them. Security incidents need their own qualified specialist response; this source is not a complete security-investigation Method.

#### SYSE.38:4.6 - Return the improvement question after restoration

Retain the surviving causal explanation, uncertainty and useful failure history for subsequent learning. Separate the immediate mitigation from the change needed to prevent recurrence.

Use SYSE.25 when the platform's supported path needs a product improvement and SYSE.39 when repeated intervention is the burden to remove. A larger application, provider or operating decision goes to its actual owner. Do not keep an urgent response active merely to finish every later improvement.

#### SYSE.38:4.7 - Develop diagnosis from the task path and build recoverable operations

Use the task's causal path to choose observations. An accepted request may wait before dispatch, execute on a worker, call a dependency, commit an effect and return a result. A missing result can arise at any of those boundaries. Find the last boundary at which the particular attempt is known to have progressed and the next boundary for which evidence is missing or adverse. This narrows the next investigation.

Build competing explanations at that boundary. If a worker has started but no dependency response arrives, consider a call that was never sent, an unavailable route, refused access, slow execution and lost response. Choose an observation that separates consequential alternatives. A local successful ping cannot establish that the application identity can perform the required database operation. A diagnostic call through the application's actual route can be more informative, but its side effects and added load must be acceptable. Keep suggestive evidence distinguishable from an observation that rules out an explanation.

Use reduction when the path is large. Compare a known working and failing population for one consequential difference, or inspect a boundary dividing the path into two regions. A successful response from the middle can eliminate some upstream explanations only for the work it actually proves. A failing response from a substitute environment may expose a defect while leaving the production incident unexplained. Preserve a bounded repeatable case when one exists, so invasive experiments can move to a suitable environment under SYSE.33.

Choose mitigation by what it can restore, not by the elegance of its diagnosis. Restricting a costly optional feature may restore the core task while its cause remains uncertain. Adding workers helps a worker bottleneck only if the dependency can accept the added demand. Restarting can remove transient state and erase the best failure evidence at the same time; obtain the inexpensive decisive observations first when user harm permits that delay. When urgent action must come first, record that limitation and do not manufacture a stronger causal claim afterward.

A repeated failure is also a design input for the operation itself. Give important state-changing operations a stable way to recover their actual result after a lost response. Where the implementation supports it, a retained operation identity can link the request, effects and result, allowing a caller to resume observation instead of creating another attempt. This mechanism needs a defined retention interval and qualified behavior under duplicate requests and concurrent consumers. Merely attaching a request ID to a log does not supply deduplication or recoverability.

Build recovery procedures from observed states and allowed transitions. For each relevant partial state, determine what can be inspected, which continuation is safe, which prior state remains usable and what evidence completes the user's task. Exercise the states that interruption can actually leave, including loss of the controller while the target continues. Keep access, dependency availability and recovery capacity within the supported operating arrangement; a dormant script with expired credentials is not an available return. Use the exercise to improve both the procedure and the visibility it needs.

In ParcelWorks, the missing deployment result has two materially different continuations. Before dispatch, restoring capacity lets the original request proceed. After h2 has started with c1, the continuation first establishes that partial runtime and corrects its effective configuration. A third history can contain a completed deployment whose reply was lost: recover and return the existing result instead of redeploying. These histories require different actions even though the user sees the same timeout. An unrelated payment service applies the same reasoning to a possibly committed payment, but needs its own transaction and reconciliation contract; the deployment correction is not a transferable payment-retry recipe.

### SYSE.38:5 - Archetypal Grounding

In a constructed ParcelWorks example, a developer requests deployment of a verified artifact/configuration through the supported path. The request is accepted but no usable result returns. The old application is still serving parcel operators correctly.

The responder recovers the request and its stage observations. The request has not been dispatched to an execution worker. All eight shared workers are occupied by long test jobs; new test jobs continue arriving. No target resources have been created for this request.

Two explanations initially matter: the deployment is waiting for capacity, or the deployment dependency is failing. The next observations distinguish them.

| Observation or bounded probe | Effect on the explanations |
| --- | --- |
| The attempt remains in the admission queue with no execution start. | The current delay occurs before a dependency call in this attempt. |
| A permitted diagnostic probe outside that busy queue reaches the dependency. | A general dependency outage is less consistent with the observed delay. |
| A deployment executes normally when a worker becomes available. | Worker contention is supported as the immediate constraint for this task. |
| The probe fails despite available execution capacity in an alternate history. | Dependency failure remains live and needs its own investigation. |

For the first history, the authorized operator stops admitting additional heavy test jobs, lets current safe-to-finish work drain, and reserves the next available worker for the supported delivery task under an already qualified capacity policy. SYSE.40 supplies the enduring capacity-protection arrangement. The mitigation does not cancel arbitrary jobs.

The original deployment request is then processed without creating a duplicate attempt. Its runtime artifact/configuration and bounded deployment test are observed, and the developer receives the result. Queue waiting has been reduced for that task; the team does not claim that all backlog or every user class is restored.

A second attempt illustrates a different failure. Its outer job timed out after installation began. Readback finds h2 running with old configuration c1 on one candidate instance. Resubmitting the entire deployment would ignore that partial effect. The responder keeps the candidate out of ordinary routing and uses SYSE.41 to reconcile the target or return it under the qualified compatibility conditions. If readback is unavailable, the state remains unknown.

If that second attempt may also have written persistent data, SYSE.34 determines whether replay or old-version return is valid. Restarting the process cannot settle the data question. The request to the specialist names that unresolved write/state relationship while independent diagnosis of the queue can continue.

If the incident spreads across several services and requires coordinated communication, the actual incident lead invokes the major-incident arrangement in section 4.5. A small queue failure resolved by the authorized on-call practitioner does not need that expansion.

What changes in practice is that restoration follows the failed task and its actual effects, while diagnosis tests alternatives rather than collecting plausible stories.

### SYSE.38:6 - Bias-Annotation

Recent changes and familiar past incidents are tempting explanations. A dramatic infrastructure metric can distract from the user's failed path stage. Check contrary evidence and preserved functionality; do not infer an application outage simply because its build or deployment platform is unavailable.

### SYSE.38:7 - Conformance Checklist

- The failed attempt, supported result and actual impact are recovered.
- Proposed mitigation has a known state, compatibility and permission boundary.
- Competing explanations have discriminating observations or bounded tests.
- Partial effects are resolved before potentially duplicating retries.
- User-task recovery is verified separately from process health and alert acknowledgement.
- Major-incident roles and communications use actual assignments, not imported labels.
- Residual limits and later improvement questions reach their appropriate holders.

### SYSE.38:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Retry after every timeout. | Query actual effects and use the operation's qualified replay behavior. |
| Restart everything and name the last restart as the cause. | Preserve observations and distinguish mitigation from causal evidence. |
| Wait for complete root cause before any useful mitigation. | Apply a qualified impact-reducing action while preserving enough evidence. |
| Declare recovery because the controller is green. | Verify the affected user task and retained-state conditions. |

### SYSE.38:9 - Consequences

Task-centered diagnosis can restore useful work sooner and produce a more discriminating follow-up question. It needs accessible state, knowledgeable responders and qualified recovery paths. Some uncertainty can remain after mitigation; that is preferable to either overstated causation or continued avoidable harm.

### SYSE.38:10 - Rationale

A failure is experienced through an interrupted result, while its causes and effects can lie across several components. Recovering the attempt and partial state connects intervention to that result. Competing explanations and bounded tests reduce the chance that successful mitigation becomes a false causal story.

### SYSE.38:11 - SoTA-Echoing

For technical diagnosis, **adopt and adapt** the developed 2016 [SRE Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) Method: triage, a model of the failing path, competing explanations and discriminating tests. It already supports mitigation before complete causal certainty. Section 4.7 connects that reasoning to state-changing operations whose effects can outlive a failed request.

For a coordinated major incident, **adopt** the [PagerDuty During an Incident Method](https://response.pagerduty.com/during/during_an_incident/) through section 4.5's local assignments, informed by the 2018 [SRE Incident Response](https://sre.google/workbook/incident-response/) treatment. Its coordination is useful when scope and consequences require it; a bounded failure handled by one authorized practitioner need not acquire the same overhead.

Reopen the recovery procedure when task paths, access, dependency behavior, persistent effects or observation change. OPS.3 and OPS.4 supply the shared operating distinctions and account.

### SYSE.38:12 - Relations

SYSE.26 identifies the supported user result. SYSE.36 and SYSE.37 provide matching observations and alerts. SYSE.34 bounds data recovery, SYSE.40 supplies capacity protection and SYSE.41 resolves actual deployment state. OPS.3/OPS.4 supply operating distinctions and shared current attention when needed. SYSE.25 and SYSE.39 receive the later platform-improvement question.

### SYSE.38:End
