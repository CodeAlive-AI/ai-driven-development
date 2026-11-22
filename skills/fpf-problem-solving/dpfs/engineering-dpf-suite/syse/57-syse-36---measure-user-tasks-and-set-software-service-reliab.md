## SYSE.36 - Measure User Tasks and Set Software-Service Reliability Objectives

> **Status:** Stable

> **Normativity:** Guidance within the stated software-service measurement use; examples are illustrative.

### SYSE.36:1 - Problem frame

Use this pattern when a software service looks healthy in its infrastructure dashboard while users cannot complete their tasks, or when a reliability target exists without an agreed meaning or response. Start with one named service, its users, configuration and task class, then define what a good result means to those users.

Define each service at its own users’ task boundary. If the promise concerns a complete task that uses several services, establish which attempts and outcomes have to be connected to assess that task. The result may be a measurement definition, qualified instrumentation or a specific gap. An operative service-level objective also needs an agreed target, time or event basis and applicable response policy.

If adequate measurement and an agreed objective already exist, use them for the relevant decision. A one-off correctness check need not become a permanent SLO. This pattern does not define the application's business meaning, certify every use of the service or turn reliability into a complete measure of user value.

### SYSE.36:2 - Problem

A backend counts only the requests it receives. Failures at the user entry can disappear from its denominator. An HTTP success response can accompany the wrong application result. Metrics collected without version or task attribution can mix unlike uses and conceal the changed behavior.

A displayed target has a different defect when nobody agrees what it protects or what to do when it is missed. The measurement then becomes a reporting number, while engineering priorities remain disconnected from user experience.

### SYSE.36:3 - Forces

| Force | Practical tension |
| --- | --- |
| User meaning and affordable observation | The important result may be harder to observe than an existing server counter. |
| Comparability and diversity | An aggregate aids decisions while task classes, users and configurations can have different needs. |
| Reliability and other value | A more reliable service can still be hard to use, slow to improve or not worth providing. |
| Detail and responsible data use | Diagnosis benefits from context while privacy, access, retention and instrumentation cost constrain collection. |

### SYSE.36:4 - Solution

#### SYSE.36:4.1 - Define the subject and the good task result

Name the service, user population, supported task class and relevant configuration. Recover the task's acceptance meaning from the responsible product or practice owner. A platform team can implement observation without acquiring authority to redefine application behavior.

Define an eligible attempt, its beginning and end, and the condition for a good result. Include timing, correctness, freshness or other properties only as the task needs them. Separate unsupported or invalid requests under a stated rule; do not recategorize a valid but failed attempt merely to improve the denominator.

Distinguish a user attempt from internal retries or backend jobs. Several internal operations can serve one attempt, and a failed attempt may produce no backend job. Decide how cancellation, abandonment and incomplete observation affect the stated question rather than excluding them silently.

#### SYSE.36:4.2 - Separate measurement meaning from implementation

Write the service-level indicator, SLI, specification in terms of the user outcome before choosing a counter or query. Then identify how the available instrumentation could observe that specification and where it would miss or distort it.

For an event-ratio indicator, define both good events and eligible events over the same population and interval. For a time-based indicator, define the evaluated periods and their conditions. Do not combine request counts, user minutes and task outcomes in one ratio without a justified measurement Method.

When the required outcome is only partly observed, ask what the remaining records can establish about it. An independent source or a bound may settle the acceptance threshold. Otherwise report the unresolved claim. A dependency check or an HTTP success status can supply a narrower fact with its own meaning.

#### SYSE.36:4.3 - Construct and exercise the observation path

Place observation where material entry, execution and result failures can be detected. Connect the relevant metrics, logs or traces to the right subject and configuration using sufficient correlation. The [OpenTelemetry signals model](https://opentelemetry.io/docs/concepts/signals/) supplies interoperable signal categories for observing the task. Determine success from the user’s required outcome.

For a working measurement, establish how the available observations distinguish the outcomes the claim depends on, including loss of observation. Where relevant, examine failures before a request reaches the backend, and the effects of delays, duplicates, sampling and aggregation. Exercise a case when its outcome is needed or a demonstration is due. For a measurement definition, specify how those outcomes would be observed. Estimating a complete event count from sampled traces requires grounds for that inference.

Keep missing data visible. If eligible attempts are known but their results are not, retain that distinction. If the entry population is unobserved, even the denominator may be unknown. Apply an agreed conservative policy where needed, but distinguish that policy disposition from an observed service failure.

Use the authorized data-handling arrangement. Collect only what the question requires, and avoid exposing secrets or unrestricted personal task content. A correctness check may run within an authorized application boundary and emit a bounded result; it need not export the input values.

#### SYSE.36:4.4 - Agree an objective and its use

When a new or revised objective is needed, use observed task difficulty, user needs, failure consequences and feasible provision to propose a target and interval. Current performance can inform a starting proposal but does not determine what users should accept. Avoid importing another service's percentage or assuming that a more demanding number is always a better choice.

Agree a new or revised target with those who depend on or provide the service, including whoever can make the relevant trade-offs. Define the error budget in the same event/time basis and the actions that follow material consumption or exhaustion. Those actions need authority and capacity; a dashboard configuration does not create either.

A policy can prioritize repair, restrict a class of changes or require a decision before further risk. Choose its scope for the task and consequences. The budget is not permission to cause any kind of harm up to a numerical allowance, and it does not cancel independent constraints.

If agreement, meaningful timing or adequate observation is missing, return a proposal and its unresolved condition rather than claiming an operative SLO.

#### SYSE.36:4.5 - Interpret and improve without changing the subject

Report the observed value or supported bounds with the subject, population, interval and coverage limits. When the required outcome cannot be observed, report the measurement gap. Distinguish measured reliability, proposed or agreed target, delivery speed, user satisfaction and improvement value.

Give platform-task evidence to those making the corresponding provider or practitioner decision. They can use SYSE.25 when choosing a platform improvement. Send application evidence to its application and exposure owners. For exposure evaluation or an alert, use observations for the service and population in question. Use its objective when the decision depends on one.

Compare reported reliability with the difficulties users encounter. Revise the definition or implementation when it misses consequential failures; retain enough continuity to explain why old and new values differ. Do not improve the apparent history by quietly changing who or what is counted.

#### SYSE.36:4.6 - Build a reliability model and an executable policy

Begin with the tasks whose failure changes the user's ability to obtain the service's result. Follow each task from its entry point through dependencies to the result the user receives. Choose an initial set of indicators that distinguishes those failures. Availability and latency may be enough for a simple lookup; a data pipeline can additionally need freshness and correctness. More indicators are useful only when they reveal a different consequential failure or support a different decision. A convenient infrastructure metric can remain a diagnostic signal without becoming another user objective.

Choose aggregation from the tolerated loss. If a global ratio can conceal repeated failure for a supported group that requires its own response, calculate the result for that group or give a distribution that exposes it. Locate the task outcome first, then use component signals to investigate a change. When several properties jointly define a good attempt, count each eligible attempt once under the joint condition.

Suppose ten identified requests must each receive the correct response by its deadline. Nine were correct and nine were timely. If both failures concern one request, nine met both requirements. If they concern different requests, eight did. These totals alone establish a minimum of eight. To decide whether at least nine succeeded, determine whether the failures concerned the same request.

Where outcomes are partly unknown but entry is complete, report the possible range before adopting a policy disposition. Let N > 0 be the number of eligible attempts, with G known good, B known bad and U unknown results. If those outcome categories are disjoint and G + B + U = N, the actual good fraction lies between G/N and (G + U)/N. With no eligible attempts, an event ratio for the interval is undefined. The range is an observation bound, not a probability estimate. For 1,000 entries with 985 good, 5 bad and 10 unknown, the range is 98.5% to 99.5%. A 99% objective is not decided by those observations. A conservative operational policy can act on the lower bound; it must not describe all ten unknown outcomes as observed failures. If entry itself is missing, this calculation no longer bounds the whole population.

Develop the objective and policy together. Estimate what loss users can tolerate over a meaningful interval, what the provider can supply, and what changes are available when the budget is at risk. Compare a feasible initial objective with a more demanding one by the additional engineering, delay and cost it requires. An aspirational target can guide improvement, but it is not an agreed current service promise merely because it appears on a dashboard. For a new service, use a provisional definition and observed trials to negotiate that promise; retain separately any minimum obligation that already applies.

Make the policy executable through recognizable states. Under ordinary conditions, continue permitted delivery while observing the agreed result. Under material rapid loss, use the available mitigation and response arrangement. Under exhausted budget or repeated misses, direct the relevant capacity to reliability work or restrict the changes that add the implicated risk. State how an exception is decided and what evidence permits ordinary operation to resume. Do not automatically ban a repair because it is a change, or freeze an unaffected platform because another application's budget is exhausted. The policy's holder needs authority over the resources and decisions it names.

Exercise that policy on a kind of decision the service faces before treating it as operational. If the last incident had exhausted the proposed budget, which work would have changed, who could have changed it, and would that action have protected the task? If no action follows, either the objective is informational or its decision arrangement is incomplete. If every harmless variation triggers expensive intervention, reconsider the definition, target or response with the affected users; do not quietly hide the observations. Then revise from actual incidents, complaints and changes in supported use.

An unlike pipeline example makes the adaptation clear. A nightly accounting export can be available all day while producing yesterday's incomplete result. Define the eligible run, source cutoff, completeness and due time, and observe the delivered output against them. The provider's HTTP availability remains useful for diagnosis, but adding more successful HTTP calls does not improve the export's reliability. If the task changes to an interactive query, build a new timing and event definition instead of carrying over a daily-run percentage.

### SYSE.36:5 - Archetypal Grounding

#### SYSE.36:5.1 - Measure two different software services

In a constructed ParcelWorks example, the platform offers a supported deployment path to developers. It also deploys an address application used by parcel operators. The two services can fail independently.

For the platform, eligible means one authorized request for an already verified artifact/configuration in a supported class. Good means that the requested runtime identity and bounded deployment-test result reach the requester within the response limit agreed for that class. A failure before any backend job exists is still a failed eligible attempt. An unsupported language request remains a separately classified boundary, not a successful deployment.

For the application h2/c2, eligible means an authorized attempt to view, edit and save an address through the changed form. The application owner requires correct first-line/tail display and preservation of the submitted text under the correspondence in SYSE.34, within the application's own agreed response bound. An empty tail is different from an absent tail.

| Measurement question | Needed observation | Gap that must remain visible |
| --- | --- | --- |
| Did the platform deliver the requested runtime? | User-entry attempt, actual artifact/configuration, bounded test and elapsed response. | No entry observation, unknown target state or missing test result prevents the good claim. |
| Did the new form display the intended address? | Matching form/configuration and its relevant displayed components. | Backend storage success does not show what the user saw. |
| Did the acknowledged save preserve the submitted text? | The value/identity correspondence for that save under a qualified version, snapshot or controlled test. | A later legitimate edit must not be mistaken for corruption; an HTTP 200 is insufficient. |
| May either result be used for a timeliness objective? | The subject's own agreed response bound and a qualified elapsed-time observation. | No agreed bound means timeliness is not yet qualified. |

The team constructs instrumentation for these definitions and exercises good, failed and missing-observation cases. If it cannot yet observe the form correspondence, it can report backend availability separately, but the application-success measurement remains incomplete.

In one constructed controlled test, entry A17 binds the attempt to h2/c2 and starts its response clock. Inside the authorized application/test boundary, the check verifies the displayed L = `12 Oak St`, T = empty text and the acknowledged saved version's exact correspondence to the submitted text ending in LF; later row changes are not substituted for that version. It returns A17, h2/c2, the bounded correctness result and elapsed time, without exporting address text. A qualified internal read retry against that version retains A17: two read calls and duplicate delivery of the same result do not become additional user attempts. If correctness and the agreed response bound both hold, A17 is one good eligible attempt. An entry A18 with no correlated completion is still one eligible attempt, but its outcome remains unknown, not success or an observed failure; any conservative policy disposition is labelled separately.

Suppose ten observed platform deployment attempts complete correctly within their own agreed response bound. Meanwhile, nine general application requests reach h2/c2 but none uses the changed form. The platform observation is favorable for those ten attempts. The application-form observation remains absent, so it does not supply a favorable exposure result.

In another constructed attempt, h2/c2 is installed correctly but its form hides a non-empty tail. The application condition fails while platform delivery remains correct. Conversely, unavailable CI workers can prevent new developer tasks while the old deployed application continues serving parcel operators successfully. Direct each failure to those responsible for its service. Account for it against that service’s budget when the eligible task and agreed objective apply.

These are invented observations for explaining the Method, not measured service results or proof of production instrumentation.

#### SYSE.36:5.2 - Turn a definition into a decision, not just a percentage

For a separate arithmetic illustration, suppose the responsible users/providers agree that at least 99% of a named service's eligible tasks must satisfy its complete good-result definition over a specified 30-day window. They also agree how budget exhaustion changes the priority of reliability work. The target and policy are assumptions of this example.

With 1,000 fully observed eligible tasks, 995 good and 5 bad, the observed ratio is 99.5%. For that observed population, the 1% allowance is 10 bad tasks, so the five consume half of the nominal event budget. Further arrivals change the denominator and the allowance. Unused allowance does not permit violation of an independent data-integrity requirement.

Now suppose ten results are missing rather than fully observed. The exact fraction may be open while the threshold decision is settled. With 1,000 known eligible tasks, 990 known good and ten unknown, at least 99% were good. Fifteen known bad already preclude 99%. When both threshold outcomes remain possible, obtain the missing observations or apply the agreed missing-data policy. If the service sees only ten events in an hour, high-volume alert thresholds require a separate fit decision; the number 99% does not supply it.

For each service, distinguish a response to observed failure, a response to lost observation and a decision about an acceptable level of loss.

### SYSE.36:6 - Bias-Annotation

Providers may count only the work their backend accepted, and application teams may choose the easiest available metric. Aggregate success can hide a small population with consistently poor outcomes. Check user-entry failures, task classes and missing semantic observations before accepting an apparently excellent ratio.

### SYSE.36:7 - Conformance Checklist

- The subject, users, configuration and task class are named.
- The responsible owner supplies the good-result meaning.
- Eligibility and good outcome are defined independently of the convenient telemetry.
- For a working measurement, establish how its observations distinguish good, failed and unobserved outcomes relevant to the claim. Exercise a case where this correspondence needs testing. If some outcomes remain unknown, state which conclusions the available records still support.
- Material pre-backend failures, retries and incomplete outcomes are accounted for.
- When an objective and response policy are required, they are agreed on a consistent event/time basis.
- Each service measure retains its subject and denominator. An end-to-end claim uses evidence about complete tasks or an explicit relation between the contributing outcomes at that same scope.
- A reliability measure is not presented as complete user value or release authority.

### SYSE.36:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| Use backend jobs as all user attempts. | Observe or bound failures at the user entry and explain remaining coverage. |
| Treat HTTP 200 as application correctness. | Observe the task result against its acceptance condition or state the missing semantic check. |
| Set a percentage with no agreed consequence. | Agree the objective and response policy with the service's users and providers, including those authorized to make the relevant trade-offs. |
| Merge platform and application budgets. | Bind each measurement and policy to its own service and users. |

### SYSE.36:9 - Consequences

Task-grounded measurement can expose failures that infrastructure monitoring misses and make reliability decisions more intelligible. It can require additional instrumentation, data-handling design and agreement. It may initially reduce apparent success because previously invisible failures or gaps become visible.

### SYSE.36:10 - Rationale

A reliability objective is useful only when its measurement represents the service result people depend on and its policy changes an available decision. Defining meaning before instrumentation protects that connection. Separating subjects prevents success in an enabling service from being mistaken for success in the work it enables.

### SYSE.36:11 - SoTA-Echoing

For user-relevant reliability, **adopt and adapt** the 2018 [SRE Implementing SLOs](https://sre.google/workbook/implementing-slos/) treatment. User journeys, SLI specification versus implementation, feasible objectives and an agreed error-budget policy are part of that approach. Sections 4.1–4.6 develop their use across platform and application tasks, with explicit unknown-outcome bounds and policies tied to the authority and capacity needed to respond.

**Adopt** [OpenTelemetry signal categories](https://opentelemetry.io/docs/concepts/signals/) as observation means where useful, without treating a telemetry model as application acceptance meaning. Compare a few outcome indicators with a larger indicator set by consequential coverage and maintenance cost. A simpler initial implementation can be useful with its limits visible; an unobservable semantic requirement cannot be replaced silently by a convenient proxy.

Reopen the definition or policy when supported tasks, populations, instrumentation coverage, consequences or feasible provision change. A more demanding percentage is not automatically the better user/provider agreement.

### SYSE.36:12 - Relations

SYSE.25 uses platform-task evidence for improvement choices. SYSE.31 and SYSE.41 provide feedback/deployment observations with their own limits. Use matching task evidence for exposure evaluation under SYSE.35 and for alerts under SYSE.37. A budget-risk alert also needs its service objective. SYSE.38 uses correlated evidence for diagnosis; SYSE.40 makes delayed and rejected work visible. SYSE.4 governs the resulting reliance.

### SYSE.36:End
