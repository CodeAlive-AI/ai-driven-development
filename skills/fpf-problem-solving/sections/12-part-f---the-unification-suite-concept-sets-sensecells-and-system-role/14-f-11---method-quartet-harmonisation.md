## F.11 - Method Quartet Harmonisation

**“Ask separately about the way, its description, the Work that occurred, and any control output produced during that Work.”**

**Status.** Architectural pattern.
**Builds on:** E.10.D1 **Recovering What “Context” Means in Use**; A.3, A.3.1, and A.3.2 for `U.Method` and `U.MethodDescription`; A.15 and A.15.1 for dated `U.Work`; C.2.1 for the identity of each claim-bearing episteme or report.
**Coordinates with.** F.0.1 and F.17 for exact source-local meaning and an optional durable cell; F.4 for local system-role-kind descriptions; F.5 for naming; F.6 for system-role assignment and performed-Work attribution; F.9 only for an actual relation between distinct local meanings; F.10 for status and windows; B.1.5 for Method composition and Work enactment.
**Aliases (informative).** *Method, description, Work, and control-output split*; *design and run distinction*.

### F.11:1 - Intent & applicability

**Intent.** Give a cold reader four practical questions that prevent common category errors:

1. What **`U.Method`**, the way of doing, is meant?
2. What **`U.MethodDescription`**, the episteme whose one exact `EntityOfConcern` is that Method, is being used?
3. What dated **`U.Work`** actually occurred?
4. Did that Work produce a control signal, command, setpoint, transformation output, or other domain-specific output that matters to this claim?

These questions are a reading aid, not a universal four-kind ontology. The fourth answer is whatever value and relation its direct control or transformation pattern defines; F.11 does not mint a universal `U.Actuation` kind.

**Use this when.** A sentence risks mixing a way of doing with its specification, a design with an occurrence, an approved description with evidence of results, or a Work occurrence with one of its outputs.

**Do not use this when.** The statement already names one exact value and direct relation unambiguously. F.11 does not prescribe files, tools, workflows, or a generic fact-transfer relation.

### F.11:2 - Problem frame

1. **Design-time and run-time blur.** A BPMN process description is cited as though it happened.
2. **Description mistaken for result.** Approval of an SOP is treated as proof that later Work met a target.
3. **Work mistaken for output.** A log of setpoints is treated as the whole Work occurrence.
4. **Word drift.** *Activity*, *task*, *execution*, *process*, and *command* change meaning across sources.
5. **Agency blur.** A Method or description is said to act, or a vague “System-in-Role” replaces the actual System, local system-role kind, assignment, Work, and performed-Work attribution.

### F.11:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| **Fidelity and didactics** | Keep the four questions memorable without inventing four universal kinds. |
| **Reuse and locality** | The distinctions recur across disciplines, while each source-local expression retains its own meaning. |
| **Evidence and approval** | A description may be approved, but evidence about Work outcomes remains separate. |
| **Occurrence and output** | Work and a control output may co-occur without being the same object. |

### F.11:4 - Core idea (didactic)

Use four questions, then state only the relations that actually obtain:

* **Method — the way.** An algorithm, test method, clinical pathway, or welding technique is a way of doing under A.3 and A.3.1.
* **MethodDescription — the description episteme.** An SOP, program text, BPMN or SPEM model, or other episteme is a `U.MethodDescription` only when A.3.2 finds one admitted Method as its exact `EntityOfConcern` and at least one substantive claim about that Method as a way of doing.
* **Work — the occurrence.** A dated performance, run, batch, or service episode is `U.Work` under A.15 and A.15.1. Work is the occurrence itself, not a record of the occurrence; a record or report is a separate episteme or carrier.
* **Control or transformation output — if present.** A setpoint, command, duty-cycle value, signal, or changed output is identified under its direct pattern and related to the Work only when that relation obtains.

F.11 allows the plain sentence “this MethodDescription describes the Method” as shorthand for that A.3.2 constitution and membership judgement. It does not add a binary description relation. Several epistemes may each have the same Method as their exact `EntityOfConcern`; one episteme may concern one admitted composite Method; and one document or publication may present several separately identified epistemes. One MethodDescription episteme cannot have several Methods as its `EntityOfConcern`.

Work may enact a Method when the exact enactment relation and evidence are stated. A System may perform Work under an obtaining system-role assignment when A.15.1 and F.6 support that attribution. A claim that a System or Work used, followed, deviated from, conformed to, or relied on a particular MethodDescription edition is separate. Cite the pattern that defines or tests that claim; use A.10 or B.3 for evidence reliance, and return A.6.RCD `missing-governor` when no current pattern supplies the needed relation after its participants and sentence are explicit.

### F.11:5 - Minimal vocabulary

* **Method** — a `U.Method`, the way of doing.
* **MethodDescription** — a `U.MethodDescription`, the already identified episteme that A.3.2 recognizes as having one admitted Method as its exact `EntityOfConcern`; *describes* is plain shorthand for that judgement.
* **Work** — a dated `U.Work` occurrence.
* **Control or transformation output** — the exact signal, command, value, output, or changed entity defined by the direct domain pattern when the case contains one.
* **Description use** — the exact claim that a System or Work used, followed, interpreted, or departed from a MethodDescription; do not assume one universal relation.
* **Enactment** — the exact relation between Work and Method under B.1.5 and A.15, when supported.
* **Performed-Work attribution** — the A.15.1 and F.6 relation from actual Work to the System and obtaining system-role assignment involved in its performance.
* **Window** — the time or condition envelope used by an F.10 status or evaluation claim.

### F.11:6 - Solution — four questions

#### F.11:6.1 - Which way of doing?

Name the Method and its relevant boundary. Do not identify it merely by a file name, notation, or local expression. If a stable method kind or composition is claimed, use A.3, B.1.5, and any required kind pattern.

#### F.11:6.2 - Which description?

Name the already identified episteme and the one admitted Method that is its exact `EntityOfConcern`. State edition or version when it matters. Several epistemes may each concern the same Method. One episteme may concern one admitted composite Method, while a document or publication may present several separately identified epistemes; one MethodDescription episteme never has several Methods as its `EntityOfConcern`. Saying that it *describes* the Method is only A.3.2's plain shorthand. Approval remains a separate claim and is not evidence that Work occurred or succeeded.

#### F.11:6.3 - Which Work actually occurred?

Name the dated Work, its relevant interval or situation, and the actual System that performed it. If a system-role claim matters, separately name the local system-role kind, the obtaining assignment, and the performed-Work attribution. Do not replace them with a behavioural “mask” or a `System-in-Role` pseudo-object.

#### F.11:6.4 - Which output matters, if any?

Name the actual signal, command, setpoint, transformation output, or resulting value. State how it relates to the Work under the direct control or transformation pattern. Some Work has no control output; a manual command can be simple; neither case forces a fourth universal kind.

#### F.11:6.5 - Which evidence and status claim?

Keep approval or validity claims about a MethodDescription distinct from observations of Work and verdicts about Work outcomes in a window. Keep actual use, following, deviation, and conformance claims separate and cite the pattern that defines or tests each one; return A.6.RCD `missing-governor` when such a pattern is absent. Use C.16 for observations and measurements, A.10 and B.3 for evidence use and reliance, and F.10 and F.12 for status or promise evaluation.

### F.11:7 - Source-local harmonisation map

The following are prompts for recovering local meanings, not declarations of identity:

* **SPEM and ISO 24744:** inspect whether a selected *task definition*, *activity definition*, or process description denotes a Method, a MethodDescription, or another value in that exact passage.
* **BPMN 2.0:** a process diagram is ordinarily a design description; do not call it the Work that later occurred.
* **PROV-O:** an Activity is a time-bounded occurrence under the PROV scheme. Do not identify it with `U.Work` by label; when a report uses that source-local claim for a Work occurrence, state the exact semantic or representation relation established for the case.
* **IEC 61131-3:** distinguish the runtime task execution, the program or program description, and output commands or setpoints.
* **SOSA/SSN:** an Observation and its Result provide measurement structure; neither is the Work merely because it reports on the Work.

Use F.17 only when these local meanings need stable addresses. Use F.9 only if an actual semantic relation between two exact local meanings must be stated. A relation between a description and Work, or between Work and an output, belongs to its direct pattern rather than to a generic Bridge.

### F.11:8 - Invariants

1. **Method and description distinction.** A MethodDescription is the same episteme recognized by A.3.2, with one admitted Method as its exact `EntityOfConcern`; it is not the Method, and *describes* adds no binary relation.
2. **Occurrence distinction.** Work is an actual dated occurrence, not its plan, report, record, or output.
3. **No universal actuation kind.** A control or transformation output is typed and related under its direct pattern.
4. **Explicit enactment.** Work enacts a Method only when the exact relation and basis are stated.
5. **Explicit description use.** MethodDescription use, following, conformance, deviation, interpretation, and reliance are separate claims under their defining or testing patterns; absent such a rule, return A.6.RCD `missing-governor`.
6. **Exact agency.** Performed Work names the actual System and, when relevant, the obtaining system-role assignment; no vague `System-in-Role` substitute.
7. **Evidence separation.** Approval of a description does not establish Work occurrence or outcome.
8. **Source-local wording.** Ambiguous expressions are recovered with F.0.1; F.9 is conditional on a real relation between local meanings.

### F.11:9 - Micro-examples

1. **Data pipeline deployment.** Method: delta-load transformation. MethodDescription: `etl_delta.py@v3` plus its documented rules. Work: the nightly run on 2025-07-14. No control output is material. Approval of the description and measured rows processed are separate claims.
2. **Valve control.** Method: PID tuning and control method. MethodDescription: tuning sheet and cited IEC program description. Work: PLC task cycles from 18:00 to 18:30. Outputs: the exact setpoints and PWM duty values produced during those cycles. Temperature observations, not the commands alone, support a settling-time verdict.
3. **Clinical assay.** Method: ELISA. MethodDescription: kit IFU v7. Work: batch B217. Robot commands are outputs during the Work; absorbance observations support the batch evaluation. IFU approval does not settle the batch verdict.

### F.11:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | Design as occurrence | “The process achieved X” points to a diagram. | MethodDescription becomes Work. | Name the description and the actual Work separately. |
| **A2** | Approval as evidence | “Approved SOP, therefore target satisfied.” | A status about a description replaces outcome evidence. | Use observations of Work and the relevant evaluation relation. |
| **A3** | Work as record | `U.Work` is described as the record of an event. | Occurrence, episteme, and carrier collapse. | Keep Work actual; model report or record separately. |
| **A4** | Work = control output | A setpoint log is treated as the full execution. | Conditions, delays, and other Work facts disappear. | Name Work and its outputs separately. |
| **A5** | Universal Actuation | Every case receives an `Actuation` box or kind. | Domain-specific outputs are forced into a false umbrella. | Use the direct control or transformation pattern and actual output kind. |
| **A6** | Generic Bridge transfer | A Bridge is said to transfer facts between Method, description, Work, and output. | Different relation families collapse. | State MethodDescription membership, enactment, performed-Work, description-use, output, observation, or evidence claims under their own patterns. |
| **A7** | Source-word collapse | *Task*, *activity*, and *process* are interchanged by label. | Source-local claims vanish. | Recover exact meanings; use F.9 only for an actual semantic relation. |
| **A8** | Recipe as system role | A description is said to assign responsibility. | MethodDescription and system-role assignment collapse. | Use F.4 and F.6 for kind and assignment; A.3.2 only for description. |
| **A9** | `System-in-Role` shorthand | The acting participant is a mask-like pseudo-object. | System, kind, assignment, and Work attribution disappear. | Name those four claims separately where material. |
| **A10** | Retroactive description | A new description version is assumed to change past Work. | Historical occurrence claims become unstable. | Keep past Work and its actual description-use evidence unchanged. |
| **A11** | Signal-only compliance | Commands are treated as proof of outcome. | Intended influence replaces observed result. | Use observations under C.16 and evidence relations under A.10 and B.3. |
| **A12** | MethodDescription as kind | A description vocabulary is treated as a taxonomy of Methods. | Description and kindhood collapse. | Establish any kind claim through C.3 and A.3 and keep the description separate. |

### F.11:11 - Worked examples

#### F.11:11.1 - ML service rollout

* **Method:** canary deployment strategy.
* **MethodDescription:** the versioned canary plan with traffic slices and rollback rules.
* **Work:** two dated canary deployment occurrences.
* **Outputs:** traffic-shifting commands, if material to the claim.
* **Agency:** name the deploying System, its exact local system-role kind and assignment, and performed-Work attribution only if responsibility is part of the example.
* **Evidence:** latency and error-rate observations about the Work; the plan’s approval is separate.

The example does not infer SLO satisfaction from the plan. F.12 evaluates the promise from Work outcomes in the stated window.

#### F.11:11.2 - Industrial furnace control

* **Method:** PID with feed-forward.
* **MethodDescription:** controller tuning sheet and program description.
* **Work:** the actual PLC task cycles in the stated interval.
* **Outputs:** setpoints and valve-duty values produced during those cycles.
* **Evidence:** temperature observations and their scale and unit basis.

If the IEC task expression and a PROV Activity expression are related for reporting, state that exact F.9 relation and loss. It does not create the Work-to-output or evidence relations.

#### F.11:11.3 - Clinical assay

The Method is ELISA; the MethodDescription is kit IFU v7; the Work is batch B217; robot commands are optional output detail; absorbance observations support the quality verdict. Any deviation from the IFU is an explicit description-use or conformance claim, not a property inferred from the four-question layout.

#### F.11:11.4 - Incident response

The Method is triage-first incident handling; the MethodDescription is the playbook and diagram; the Work is the handling of INC-3421 from 09:10 to 10:02. MTTR is computed from observations of that Work. Command invocations are included only if a direct control or transformation claim needs them.

### F.11:12 - Safe reasoning moves

1. **Classify the subject.** Is the sentence about a Method, MethodDescription, Work, or a particular output?
2. **Keep design and occurrence apart.** A design claim does not establish a Work outcome.
3. **Check membership.** Name the one admitted Method that is the episteme's exact `EntityOfConcern`; *describes* is only the plain shorthand allowed by A.3.2.
4. **State enactment only when supported.** Name the Work, Method, and basis for the enactment claim.
5. **State description use separately.** Say whether and how the Work or performing System used, followed, deviated from, or conformed to the versioned description, and cite the rule that defines or tests that claim; otherwise return the bounded missing-governor result.
6. **Locate outputs.** Relate a signal or changed value to the Work through its direct pattern.
7. **Bind agency exactly.** Use actual System, local system-role kind, obtaining assignment, and performed-Work attribution where material.
8. **Use outcome evidence.** Observations about the Work support evaluation; commands and approvals alone do not.
9. **Preserve history.** A new description does not alter past Work or its evidence.
10. **Recover words locally.** Use F.9 only when a genuine relation between local meanings is part of the question.

### F.11:13 - Relations

**Builds on:**

- Use **A.3** and **A.3.1** for `U.Method`, **A.3.2** for `U.MethodDescription`, and **A.15** and **A.15.1** for dated `U.Work`.
- Use **B.1.5** for Method composition and Work enactment, **C.2.1** for the identity of every claim-bearing episteme and report, and **E.10.D1** when vague *context* wording hides the actual source, scheme, scope, use, situation, or evidence basis.
- Use the direct transformation, observation, or control pattern when an output claim is made; F.11 creates no universal actuation kind.

**Constrains:**

- **F.4 and F.6:** a local system-role kind, its description, an assignment, and performed-Work attribution remain distinct from Method, MethodDescription, Work, and output.
- **F.5:** use distinct Plain and Tech designations when one source expression hides different subjects.
- **F.7 and F.9:** compare exact local claims or F.17 cells and cite F.9 only when a semantic relation actually obtains. A shared heading creates no identity, relation, or use licence.

**Used by.** Part C examples and the A.3, A.15, and B.1.5 method-and-work stack. Every MethodDescription membership judgement, enactment, performed-Work attribution, description use, observation, output, evidence use, or publication claim still uses the pattern that defines or tests it.

### F.11:14 - Migration notes

1. **Split conflated process.** Separate MethodDescription from actual Work; add only the exact relations the case supports.
2. **Repair statuses.** Keep approval and validity claims about descriptions distinct from Work-outcome verdicts and their windows.
3. **Expose actual outputs.** Replace a universal Actuation box with the precise signal, command, value, or transformation output and direct relation.
4. **Repair agency.** Replace `System-in-Role` or behavioural-mask language with the actual System, local kind, assignment, and Work attribution where needed.
5. **Version fences.** Preserve the description version actually used or referenced by past Work.
6. **Repair hidden transfer.** Replace generic Bridge language with MethodDescription membership or the direct enactment, description-use, Work, output, observation, evidence, or source-local semantic relation. Return A.6.RCD `missing-governor` instead of inventing a relation when no defining or testing rule exists.

### F.11:15 - Acceptance tests

#### F.11:15.1 - Static conformance

* **SCR-F11-S01 (four questions).** Every relevant statement identifies the Method, the MethodDescription with that one Method as exact `EntityOfConcern`, the Work, or the exact output it concerns.
* **SCR-F11-S02 (Work actuality).** `U.Work` is an occurrence, not a record, plan, or output.
* **SCR-F11-S03 (no universal actuation).** Outputs are typed and related by their direct patterns.
* **SCR-F11-S04 (agency).** Any performer claim names the actual System and exact assignment and attribution basis.
* **SCR-F11-S05 (separate claims).** MethodDescription membership, enactment, description use, output, observation, and evidence claims use their defining or testing patterns and are not replaced by a generic Bridge or invented description relation.
* **SCR-F11-S06 (evidence).** No approval or command alone is used as proof of Work outcome.

#### F.11:15.2 - Regression

* **RSCR-F11-E01 (description update).** Earlier Work and its actual description-use claims remain unchanged.
* **RSCR-F11-E02 (source drift).** Changed source-local wording reopens only the affected F.9 relation or citation.
* **RSCR-F11-E03 (status drift).** New statuses do not migrate between description and Work outcome without a new direct claim.
* **RSCR-F11-E04 (output growth).** Added output detail does not erase or replace Work.

### F.11:16 - Didactic distillation

> “Ask four questions. What is the **Method**, the way of doing? Which **MethodDescription** has that one Method as its exact `EntityOfConcern`—plainly, describes it? What dated **Work** actually occurred? Which particular control or transformation output matters, if any? These are not four universal boxes. Work is the occurrence, not its record. MethodDescription membership adds no binary relation; Work may enact the Method only when that relation is supported. Name the actual performing System and assignment when agency matters. Use observations for outcome claims, and use F.9 only for a real relation between source-local meanings.”

### F.11:End

