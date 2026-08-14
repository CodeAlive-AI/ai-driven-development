## F.12 — Service Acceptance–Work Evidence Link

**“Judge a promise from what happened, in a stated window, with evidence that actually bears on the promised outcome.”**
**Status.** Architectural pattern.
**Builds on:** F.1 **Question-Relative Source Selection**; F.0.1, F.2, F.3, and F.17 for exact source-local meaning and optional addresses; F.5 for naming; F.9 only for actual relations between local meanings; F.10 for status families and windows; F.11 for the Method, MethodDescription, and Work distinctions; A.2.3 for `U.PromiseContent`; A.15.1 for evaluation Work; and A.6.1 for the applied evaluation operation and its result binding.
**Coordinates with.** C.2 and C.16 for observation, characteristic, scale, unit, and measured-value claims; A.3.2 when a selected evaluation MethodDescription edition changes the result; A.10 for evidence use; B.3 only when assurance is claimed or reliance is material; C.16.P and A.6.RCD when indicator or proxy wording hides an unsupported relation; E.13 only when a proxy is optimized or used as a target, incentive, gate, release argument, reputation signal, repair target, or decision driver; and direct transformation or control patterns when outputs are material.
**Non-goals.** No team workflow, tool, record format, or universal acceptance object. F.12 explains the minimum claims needed for a defensible judgement.

### F.12:1 - Intent & applicability

**Intent.** Relate an exact promise-content claim to the delivery Work and outcome being judged, the observations and measured values used as evidence, an explicit window and population, and the separate evaluation Work that applies the declared acceptance rule and returns a result on its declared scale. Map that result to F.10 status only when a receiving use needs status, and create a verdict episteme only when another use needs a durable assertion. Keep each object and relation distinct so a reader can see what would change the result.

**Use this when.** An SLO, SLA clause, safety margin, response-time target, quality gate, or other promise must be judged from actual occurrences.

**Do not use this when.** The question is only what the promise says, how the Method is described, or how a measurement is made. Use the direct A.2.3, A.3, A.15, or C.16 pattern. F.12 does not turn a lexical cell or comparison row into a verdict subject.

### F.12:2 - Problem frame

1. **Plan ≠ proof.** A diagram or playbook is treated as evidence that its promise was met.
2. **Output ≠ outcome.** Commands or setpoints are mistaken for the consumer-relevant result.
3. **Word ≠ measure.** *Availability*, *latency*, or *incident* is used without recovering its exact local meaning and characteristic.
4. **Proxy by assumption.** Monitor output is called a proxy before asking whether the observation and measurement model already concern the promised characteristic directly; when they do not, the needed indicator relation has no defining or testing rule.
5. **Evaluation disappears.** A verdict appears without evaluation Work, an enacted evaluation Method, exact operation inputs, or a result binding.
6. **Status families collapse.** `Satisfied`, `Violated`, and `Inconclusive` are treated as one universal scale even though the first two are RequirementStatus values and the third is an EvidenceStatus value unless an exact local result scale says otherwise.

### F.12:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| **Promise and occurrence** | Promise content is stated in advance; fulfilment concerns actual Work and delivered outcome. |
| **Local meaning and integration** | Sources use different words, while the judgement must join their claims without a generic Bridge. |
| **Parsimony and realism** | One compact pattern must cover thresholds, percentiles, shares, counts, and bands. |
| **Evidence and feasibility** | Direct observation is best, but sometimes only a limited proxy is available. |

### F.12:4 - Core idea (didactic)

Before reporting the result, name nine things:

1. the exact **`U.PromiseContent` claim** being evaluated;
2. the actual **Work occurrence or defined Work population** whose delivery is in question;
3. the promised outcome or characteristic and its scope;
4. the relevant **observations and measured values**, including scale and unit;
5. the explicit **window** and population boundary;
6. the evaluation **Method** and the System's dated evaluation **Work** that enacts it;
7. the exact A.6.1 operation application, including its selected inputs and result binding;
8. the acceptance rule and declared result scale, such as a Boolean, trichotomous, graded, `N/A`, or `Inconclusive`-including scale when that scale is actually declared; and
9. the PromiseContentUse, delivery, fulfilment, measurement, evidence-use, any separately defined indicator or proxy, reliance, and status relations that actually connect these claims.

The operation's result value comes first. A RequirementStatus assertion of `Satisfied` or `Violated` is available only through the exact acceptance result and its F.10 rule. Insufficient evidence can support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or it can yield a locally declared result such as `Inconclusive` when the acceptance scale says so; it never silently creates a mixed universal scale. A plain summary may say **met**, **not met**, or **cannot judge** while retaining that exact distinction. A SchemeSenseCell may help address a local meaning, but it cannot bear the promise, Work, observation, value, result, evidence, or status. A comparison table may display the argument, but it cannot establish any of it.

### F.12:5 - Minimal vocabulary

* **Promise-content claim** — the exact `U.PromiseContent` under A.2.3, including its subject, scope, target, and conditions.
* **Work** — the actual dated `U.Work` occurrence, or an explicitly defined population of Work occurrences, being judged.
* **Observation** — the actual observation occurrence and its result under C.2 and C.16.
* **Measured value** — a value for a named characteristic on an explicit scale and unit.
* **Window** — the time, batch, episode, phase, or other bounded evaluation interval under F.10.
* **Evaluation Work** — the dated Work in which a System enacts the evaluation Method over the selected facts and states.
* **Evaluation application and result** — the A.6.1 operation application with exact argument bindings and a result value on the acceptance specification's declared scale.
* **Evaluation rule and result scale** — the stated comparison or aggregation and its declared admissible results. Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
* **Status use** — a separate F.10 application of an exact EvidenceStatus or RequirementStatus value to its exact target, scope, window, and use after the direct result is recovered.
* **Verdict episteme** — an optional C.2.1 episteme that states the evaluation result or status when another use needs a durable assertion; it is not the operation result or the fulfilment relation.
* **Indicator or proxy relation** — only a separately defined or tested relation in which one observed characteristic or result stands in for another subject or outcome for this use, with exact participants, coverage, and loss. The word *proxy* does not create it.
* **Evidence use and reliance** — an A.10 evidence-use relation and, only for assurance or material reliance, the B.3 branch. Neither creates an indicator relation or the acceptance result.

### F.12:6 - The binding, as eight practical rules

**R1 — Match the promise to delivery.**
Use A.2.3 to keep the exact promise content, `PromiseContentUse`, delivered outcome, and fulfilment relations distinct for the Work occurrence or population being judged. An abstract service label or lexical cell is not enough, and the later evaluation does not make those delivery-side relations obtain.

**R2 — First test for direct measurement.**
Ask whether the observation and measurement model directly concern the promised characteristic of the relevant Work outcome inside the window. If they do, use C.16 for measurement and A.10 for evidence use; add no proxy relation. Commands, approvals, and MethodDescriptions are not outcome evidence by themselves.

**R3 — Recover any real indicator relation.**
If a distinct observed indicator stands in for the promised characteristic or outcome, name both participants and cite the pattern that defines or tests that exact relation. Use C.16.P to recover the construction and distortion risk. If no current rule supplies the relation, stop with A.6.RCD `missing-governor`; do not treat the word *proxy*, A.10 evidence use, or B.3 reliance as its substitute. Use E.13 only when the indicator is optimized or used as a target, incentive, gate, release argument, reputation signal, repair target, or decision driver.

**R4 — Perform the evaluation.**
Name the System that performs dated evaluation Work and the evaluation Method it enacts. Identify the A.6.1 operation application, its selected facts and state references, the applied acceptance rule, and the result binding. Surface a particular MethodDescription edition only when selecting that edition changes the result or its replay.

**R5 — Use the declared result scale.**
Name the characteristic, scale, unit, aggregation, comparison, and admissible result values through the acceptance specification's `verdictScaleDescriptionRef`. Typical calculation shapes include:

* a value at or above, or at or below, a threshold;
* a stated percentile at or below a target;
* a share such as good time divided by total time;
* an event count within a limit;
* all relevant values remaining inside a band.

The calculation shape does not select a verdict scale. Use the exact scale declared by the acceptance specification.

**R6 — State every needed relation directly.**
Use A.2.3 for promise use, delivery, and fulfilment; C.16 for observation and measurement; the defining or testing pattern for any indicator relation; A.10 for evidence use; B.3 only for assurance or material reliance; and F.9 only when distinct local meanings themselves require a semantic relation. One generic Bridge cannot establish clause–Work fit, measurement, indicator validity, evidence, evaluation, status, or fulfilment.

**R7 — Keep the window and population explicit.**
A monthly verdict, a batch verdict, and an incident verdict are different claims. A new promise, monitor, or window does not rewrite an earlier verdict.

**R8 — Preserve result, status, and assertion boundaries.**
Keep the operation result on its declared acceptance scale. Map it to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the exact F.10 rule. If evidence coverage, indicator adequacy, scale conversion, or relation support is insufficient, use `EvidenceStatus=Inconclusive`, leave `RequirementStatus=Pending`, or return the exact local result declared by the acceptance scale. Create a C.2.1 verdict episteme only when another use needs that durable assertion.

### F.12:7 - Evaluation shapes

#### F.12:7.1 - Availability share

Promise: availability is at least 99.9% for a calendar month. Delivery Work: the defined service-delivery occurrences or population during that month. Evidence: observations and measurement results for the promised availability characteristic. A System performs evaluation Work; its A.6.1 application binds the in-scope values and returns the declared result. If the observation model already concerns the promised characteristic, there is no proxy relation. If synthetic probes instead indicate a different user-experience characteristic, name the exact indicator relation, its defining or testing pattern, uncovered regions or degradations, and the evidence-use boundary; otherwise stop with `missing-governor`.

#### F.12:7.2 - Latency percentile

Promise: p95 response latency is at most 120 ms for a stated request population and window. Evidence: response-time observations for that population. Evaluation Work applies the declared sampling, exclusion, and percentile rule and binds its result on the declared acceptance scale. Sampling bias or missing paths can support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or yield a locally declared result when the scale explicitly says so.

#### F.12:7.3 - Safety or quality band

Promise: temperature remains within `[L,U]` during the batch phase. Evidence: calibrated temperature observations for the relevant EntityOfConcern and interval. Evaluation Work applies the stated sampling, uncertainty, and band rule; the exact application binds the values and returns a result on the declared scale. A RequirementStatus follows only through its own rule.

#### F.12:7.4 - Incident duration

Promise: restoration occurs within 60 minutes for each in-scope incident. Delivery Work: each handling occurrence. Evidence: observations of the defined start and restoration events. Evaluation Work applies the elapsed-time rule to those bindings and returns its declared result. A BPMN design may be a MethodDescription under A.3.2, but it is not either Work occurrence or evidence of the result.

### F.12:8 - Invariants

1. **Exact promise.** The evaluation identifies the `U.PromiseContent` claim, not merely an SLO label or cell.
2. **Delivery-side relations.** The judged delivery Work or population and the applicable A.2.3 promise-use, delivered-outcome, and fulfilment relations remain distinct from evaluation.
3. **Outcome evidence.** Observations and values concern the promised characteristic of that Work; outputs and approvals alone are insufficient.
4. **Direct-before-proxy.** When observation and measurement directly concern the promised characteristic, use C.16 and A.10 and add no proxy. A distinct indicator relation needs exact participants and a defining or testing pattern, or the result is `missing-governor`.
5. **Window and population.** Both are explicit and match the promise.
6. **Evaluation Work and application.** A System performs dated evaluation Work, enacts the evaluation Method, and applies the exact A.6.1 operation with recoverable inputs and result binding.
7. **Declared result scale.** Characteristic, scale, unit, aggregation, threshold, exclusions, and admissible result values are stated as applicable. Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
8. **Status separation.** `Satisfied` and `Violated` are RequirementStatus values reached only through a direct acceptance result. `Inconclusive` is an EvidenceStatus value unless the declared local result scale independently admits that label; insufficient evidence otherwise leaves RequirementStatus pending.
9. **Optional verdict episteme.** A durable C.2.1 assertion is created only for a named later use and never replaces the application result, status-use occurrence, evidence relation, or fulfilment relation.
10. **Bounded reliance.** A.10 governs evidence use; B.3 is used only for assurance or material reliance; E.13 is used only for an optimized or decision-driving proxy.
11. **Non-retroactivity.** Later promise, monitor, MethodDescription edition, or interpretation changes do not silently alter past evaluations or assertions.
12. **Cells are addresses only.** An F.17 cell may identify local meaning but establishes none of the substantive claims above.

### F.12:9 - Micro-examples

#### F.12:9.1 - SaaS uptime

* **Promise content:** availability ≥ 99.9% for the named service scope in June.
* **Delivery Work population:** the in-scope service-delivery occurrences during June, connected to the promise through the applicable A.2.3 relations.
* **Evidence:** synthetic-probe observations, with regions and outage-detection coverage stated. If their measurement model directly concerns the promised availability characteristic, no proxy is added; otherwise the distinct probe-to-user indicator relation needs a defining or testing pattern.
* **Evaluation:** a System performs evaluation Work; the exact application binds observed good time and total in-scope time and returns a value on the declared result scale.
* **Status or summary:** map the result to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only when that F.10 rule applies. If the evidence basis is inadequate, use `EvidenceStatus=Inconclusive` and `RequirementStatus=Pending`, or the exact locally declared result. Plainly: met, not met, or cannot judge.

#### F.12:9.2 - Furnace temperature band

The promise content states `[720,740] °C` during the soak phase. The delivery Work is the actual batch soak occurrence. Calibrated thermocouple observations either measure the product characteristic directly or use a separately defined sensor-location indicator relation. Evaluation Work applies the band rule and binds its result. An out-of-band result can support `RequirementStatus=Violated`; insufficient spatial evidence supports `EvidenceStatus=Inconclusive` and leaves the requirement pending unless the declared acceptance scale specifies another local result.

#### F.12:9.3 - Incident MTTR

The promise content states restoration within 60 minutes per in-scope incident. Each incident-handling Work has observed start and restoration events. A separate evaluation Work occurrence applies the declared event and subtraction rule; its application binds those timestamps and returns the result. A playbook may be the selected evaluation MethodDescription when its edition changes that rule, but it is not the Work or proof of the duration.

### F.12:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | Plan as proof | A diagram or runbook is cited as acceptance evidence. | Description replaces occurrence and outcome. | Name Work and observations of its outcome. |
| **A2** | Output as outcome | Setpoint writes or commands prove service delivery. | Intended influence replaces observed result. | Use observations and measurement that directly concern the promised characteristic; if a distinct indicator relation is needed, define or test it and state its loss. |
| **A3** | Cell as subject | ClauseCell, WorkCell, or MeasureCell bears the result or status. | Lexical address replaces promise, Work, evaluation, and evidence. | Cite the actual values; retain a cell only as an address. |
| **A4** | Generic Bridge | One Bridge is claimed to connect promise, Work, measure, indicator, result, and status. | Several distinct relations disappear. | Use A.2.3 for promise-side relations, C.16 for measurement, the defining or testing pattern for an indicator relation, A.10 for evidence use, A.15.1 and A.6.1 for evaluation, F.10 for status, and F.9 only for local-meaning relations. |
| **A5** | Windowless result | “We met the SLA” has no period, population, evaluation Work, or applied rule. | The claim cannot be replayed. | State window, population, evaluation Work, application, result binding, and declared scale. |
| **A6** | Percentile mirage | Annual pooled p95 is used for a monthly promise. | Aggregation and promise scope differ. | Evaluate within the promise’s exact window and population. |
| **A7** | Proxy by label | Synthetic probes equal user experience because they are called a proxy. | The text skips the direct-measurement question and any actual indicator relation. | First test whether C.16 already measures the promised characteristic. If not, name both indicator participants and its defining or testing pattern; use C.16.P and return `missing-governor` when absent. |
| **A8** | Work mismatch | Evidence concerns another product, region, or occurrence. | The result is about the wrong subject. | Match every observation to the judged Work or population. |
| **A9** | Silent units | “Latency ≤ 120” omits scale or unit. | The threshold is ambiguous. | State characteristic, scale, unit, and conversion basis. |
| **A10** | Hidden aggregation | A global result rests on a subset with no rule. | Evidence scope is overstated. | State the aggregation or confine the result. |
| **A11** | Status on umbrella | “The service is Satisfied.” | Promise content, delivery Work, evaluation result, target clause, window, and F.10 status use disappear. | Recover the direct result first, then state the exact RequirementStatus use only if its rule applies. |
| **A12** | Retroactive renorming | A new monitor silently rewrites old results and status assertions. | Historical claims lose identity. | Preserve old basis; issue a new evaluation when authorised. |
| **A13** | Universal trichotomy | Every evaluation returns Satisfied, Violated, or Inconclusive. | RequirementStatus, EvidenceStatus, and the acceptance specification's own result scale collapse. | Use the declared result scale; map to F.10 status separately, and use a plain “met, not met, or cannot judge” summary only as a rendering. |

### F.12:11 - Extended worked examples

#### F.12:11.1 - CDN latency by region

Promise content: p95 end-user latency ≤ 200 ms per region per month. Delivery Work population: delivery occurrences per region in that month. Evidence: response-time observations tagged by region and path. If probes measure the promised characteristic directly, use C.16 and A.10 without a proxy. If they indicate a distinct user-experience characteristic, name the exact probe-to-user relation, its defining or testing pattern, and last-mile loss. Evaluation Work returns one result per region on the declared scale. A global all-regions statement is a separate logical aggregation of those results or statuses, not a property of a table row.

#### F.12:11.2 - Stroke care door-to-needle

Promise content: at least 90% of in-scope ischemic-stroke episodes achieve door-to-needle ≤ 30 minutes in the quarter. Delivery Work population: patient-episode care occurrences. Evidence: observations of defined door and needle events. Evaluation Work binds those events, counts qualifying episodes, divides by the eligible population, and returns the declared result. Missing triage tags or event ambiguity may support `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or produce the exact local result declared by the acceptance scale.

#### F.12:11.3 - Cold-chain warehouse

Promise content: product temperature remains in `[2,8] °C` for at least 99.5% of each day. Delivery Work: the daily storage occurrence or defined population. Evidence: calibrated thermistor observations. First ask whether the measurement model directly concerns product exposure. If sensor position indicates another characteristic, name the exact indicator relation and its stratification loss or stop at `missing-governor`. Evaluation Work returns in-band covered time divided by in-scope time on the declared scale. Any result assertion, RequirementStatus, evidence use, and material reliance statement retain the indicator limit separately.

#### F.12:11.4 - SaaS incident MTTR

Promise content: MTTR ≤ 60 minutes for each in-scope incident. Delivery Work: each incident-handling occurrence. Evidence: observed start-fix and restoration events. Evaluation Work applies the declared duration operation and binds one result per incident. Quarterly reporting explicitly aggregates those results or their separately warranted statuses.

### F.12:12 - Safe reasoning moves

1. **Match scope.** Confirm that the promise content covers the exact delivery Work or population and keep A.2.3 promise use, delivery, and fulfilment distinct.
2. **Name the window.** Make time, batch, phase, and exclusions explicit.
3. **Test direct measurement first.** Confirm whether each observation and its measurement model directly concern the promised characteristic; if so, use C.16 and A.10 and add no proxy.
4. **Recover an indicator only when needed.** When another characteristic stands in, name both participants, the defining or testing pattern, coverage, and loss. Use C.16.P for recovery and A.6.RCD `missing-governor` when the relation is absent.
5. **Check values.** Name characteristic, scale, unit, aggregation, and uncertainty.
6. **Perform the evaluation.** Name the performing System, evaluation Work, enacted Method, exact A.6.1 application, input bindings, and result binding. Cite a particular MethodDescription edition only when it changes the result or replay.
7. **Use evidence directly.** Record the A.10 evidence-use claim. Enter B.3 only for assurance or material reliance, and E.13 only when a proxy is optimized or drives a decision, gate, incentive, release argument, reputation signal, or repair.
8. **Keep the result on its declared scale.** Boolean, trichotomous, graded, `N/A`, and `Inconclusive`-including scales are examples, not defaults.
9. **Map status separately.** Use `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the direct acceptance result. Evidence insufficiency can support `EvidenceStatus=Inconclusive` and leave the requirement pending, or produce an exact locally declared result.
10. **Create a verdict episteme only on demand.** Use C.2.1 only when another use needs a durable assertion about the result or status.
11. **Aggregate explicitly.** Population-level results and statuses follow the promise's stated quantifier; they are not inferred from a few green cases.
12. **Preserve history.** New promises, monitors, evaluation methods, or scales create new evaluations rather than changing old ones silently.

### F.12:13 - Relations

**Builds on:**

- Use **F.1** and **F.0.1** to recover exact sources and local claims, and **F.2**, **F.3**, and **F.17** only when expressions or durable addresses are needed.
- Use **F.5** for clear designations, **F.9** only for an actual relation between distinct local meanings, **F.10** for separate EvidenceStatus and RequirementStatus uses and windows, and **F.11** to keep Method, MethodDescription, Work, and output distinct.
- Use **A.2.3** for exact promise content, PromiseContentUse, delivered outcome, and fulfilment; **A.15.1** for delivery and evaluation Work; and **A.6.1** for the exact evaluation-operation application and result binding.

**Uses direct subject patterns.** Use C.2 and C.16 for observations, characteristics, scales, units, and measured values. When the measurement does not directly concern the promised characteristic, use C.16.P to recover the distinct indicator relation and cite the pattern that defines or tests it; use A.6.RCD `missing-governor` when no such rule exists. Use A.10 for evidence use, B.3 only for assurance or material reliance, E.13 only for optimized or decision-driving proxies, and the appropriate direct pattern for kind, control, or transformation claims.

**Constrains:** Reporting and assurance keep promise content, delivery Work, observation, measured value, window, evaluation Method and Work, operation application, result binding, declared result scale, optional verdict episteme, EvidenceStatus, RequirementStatus, evidence use, material reliance, any defined indicator relation, and any F.9 relation distinct. A relation-specific CL or loss is reported with that relation, not folded into the result or status.

### F.12:14 - Migration notes

1. **Promise revision.** Keep the old promise-content identity, evaluation results, and status assertions; evaluate the new claim separately.
2. **Monitor change.** State whether the new observation model directly measures the promised characteristic or needs a separately defined indicator relation; preserve past evidence identity.
3. **Scope correction.** Retire a result or status assertion about the wrong Work or population and issue a corrected evaluation rather than redefining the promise.
4. **Scale and unit change.** Apply the direct conversion and measurement relations; use F.9 only when local meanings also differ.
5. **Population refinement.** Treat per-region, per-zone, or per-episode changes as explicit promise or evaluation changes.
6. **Indicator retirement.** Prefer direct measurement when available; keep prior indicator-dependent results, status assertions, and evidence uses with their original limits.

### F.12:15 - Acceptance tests

#### F.12:15.1 - Static conformance

* **SCR-F12-S01 (actual subjects).** Every evaluation names exact promise content, delivery Work or population, observations and measured values, window, and rule; cells are optional addresses only.
* **SCR-F12-S02 (scope match).** Promise, Work, evidence, population, and window align.
* **SCR-F12-S03 (evidence).** Observations concern the promised outcome of the judged Work.
* **SCR-F12-S04 (evaluation explicit).** The performing System, evaluation Work, enacted Method, exact A.6.1 application and argument and result bindings, characteristic, scale, unit, aggregation, threshold, exclusions, and declared result values are stated as needed.
* **SCR-F12-S05 (indicator boundary).** Direct measurement adds no proxy. A distinct indicator relation names exact participants and a defining or testing pattern, or the evaluation stops at A.6.RCD `missing-governor`.
* **SCR-F12-S06 (direct relations).** Promise use, delivery, fulfilment, measurement, indicator, evidence use, assurance or material reliance, evaluation, status, and any verdict assertion use their defining or testing patterns.
* **SCR-F12-S07 (result and status).** The operation result stays on its declared scale; RequirementStatus and EvidenceStatus are mapped separately, and evidence insufficiency is never implicit target falsity.
* **SCR-F12-S08 (optional episteme).** A C.2.1 verdict episteme exists only for a named later use and remains distinct from result and status.
* **SCR-F12-S09 (no generic Bridge).** F.9 is used only for a real local-meaning relation and establishes none of the other relations.
* **SCR-F12-S10 (temporal honesty).** No timeless or retroactively rewritten result or status assertion appears.

#### F.12:15.2 - Regression

* **RSCR-F12-E01 (relation update).** A changed indicator, evidence, or semantic relation affects only evaluations that depended on it.
* **RSCR-F12-E02 (edition change).** Source-local meaning remains tied to the edition used by each evaluation.
* **RSCR-F12-E03 (population drift).** New population definitions create explicit new evaluations.
* **RSCR-F12-E04 (window partition).** Weekly and monthly results and statuses remain distinct; any roll-up states its aggregation.
* **RSCR-F12-E05 (indicator retirement).** Direct measurement changes future evaluations without silently rewriting prior indicator-dependent results or assertions.

#### F.12:15.3 - Didactic distillation

> “Name the exact promise, the delivery Work it covers, the promised characteristic, the observations and measured values, and the window and population. First ask whether the measurement is direct; if another indicator stands in, name its exact relation or stop. Then name the System's evaluation Work, enacted Method, operation inputs and result, and the declared result scale. Map that result to RequirementStatus or EvidenceStatus only through the exact rule, and create a verdict episteme only when another use needs it. Plainly: met, not met, or cannot judge. Judge what happened—not the plan, the command, the word *proxy*, or the table.”

### F.12:End

