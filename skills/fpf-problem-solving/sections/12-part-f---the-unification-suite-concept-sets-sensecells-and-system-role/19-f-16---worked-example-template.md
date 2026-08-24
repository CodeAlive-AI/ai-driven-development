## F.16 - Worked-Example Template (Cross-Domain)

**“Show one claim, the actual values and relations that make it true or false, and enough evidence for a reader to replay the example.”**
**Status.** Architectural pattern.
**Builds on:** E.10.D1 **Recovering What “Context” Means in Use**; F.1 for the source cut; F.0.1, F.2, F.3, and F.17 for exact source-local meaning when needed; F.7 for an optional comparison surface; F.9 only for actual semantic relations and bounded-use claims; F.10 for windows; F.15 for checks.
**Coordinates with.** F.12 when a case evaluates promise acceptance; A.10 for evidence use; B.3 only for assurance or material reliance; C.16.P and A.6.RCD when indicator or proxy wording hides a missing relation; E.13 only for optimized or decision-driving proxies; the direct Part C pattern for every illustrated subject; and the A.3, A.15, A.6.1, and B.1.5 method-and-work stack.

### F.16:1 - Intent & applicability

**Intent.** Provide a one-page worked-example shape that starts with a recognizable question and practical gain, names the actual values and obtaining relations, exposes exact sources and evidence, and leaves a clear boundary. Optional lexical cells and comparison tables help navigation only when they reduce reader effort.

**Use this when.** A pattern needs a compact example that crosses disciplines, source schemes, design-time and run-time boundaries, or several relation families and prose alone would hide the hand-offs.

**Do not use this when.** A shorter direct example already shows the claim. F.16 does not require a cross-source relation, table row, lexical cell, system-role claim, window, or SoD unless the case actually contains one.

**Non-goals.** No registry, workflow, editor, storage format, or proof by page layout. The template shapes what the reader sees, not how a team produces it.

### F.16:2 - Problem frame

Cross-domain examples fail when:

1. **The claim is missing.** Sources and facts are listed, but the reader cannot tell what is being demonstrated.
2. **Words replace subjects.** *Process*, *role*, *service*, or *execution* is used without recovering the actual value or relation.
3. **Relations hide in prose.** “Basically the same”, “implements”, “uses”, or “governs” conceals several different relation families.
4. **A table is asked to prove.** Co-placement or row membership becomes sameness, permission, or evidence.
5. **Evidence and limits disappear.** The page reaches a result or status without showing the evaluation, observation, source, loss, or boundary that supports it.

### F.16:3 - Core idea (didactic)

A useful worked example is a compact case with nine visible parts:

* **Question and gain** — the recognizable practical problem and what changes when it is solved.
* **Claim** — one sentence that can be accepted, rejected, or qualified.
* **Actual subjects** — the Systems, epistemes, Methods, Work occurrences, kinds, assignments, claims, observations, values, operation applications, results, status uses, or other entities involved.
* **Direct patterns** — the patterns that define, constrain, or test each substantive value or relation.
* **Source basis** — exact sources and editions and the passages or interpretation schemes that matter.
* **Obtaining relations** — each named directly, with participants, direction, and limits.
* **Evidence, result, and reliance** — what supports the claim, what evaluation actually returned when one occurred, and what remains uncertain.
* **Optional aids** — F.17 cells for recurring local meanings and an F.7 table for comparison; neither creates a fact.
* **Boundary and checks** — where the example stops and the few checks a reader can replay.

The old theatre metaphor can still help memory: the question is the scene, actual values are the participants, obtaining relations are what happens between them, sources and evidence are what let the audience check the scene, and the boundary says what the scene does not show. No fictional “actor” or “cue” replaces an ontological subject.

### F.16:4 - Minimal vocabulary

* **Worked claim** — the exact proposition demonstrated by the page.
* **Actual subject** — the value or entity to which a substantive claim applies.
* **Obtaining relation** — a relation supported for these exact participants; its appearance on the page does not create it.
* **Source basis** — exact source and edition, passage, and effective reference scheme needed by the claim.
* **Evidence basis** — observations, source claims, A.10 evidence-use relations, and any separately warranted B.3 reliance limits that support the conclusion.
* **Evaluation result** — when the case evaluates a promise or criterion, the result bound by an exact A.6.1 application during evaluation Work, on the result scale declared by the applicable rule.
* **Receiving use** — the concrete decision, explanation, comparison, or action for which the result is used.
* **SchemeSenseCell** — an optional F.17 address for a recurring local meaning.
* **Comparison table** — an optional F.7 display of exact entries and already obtaining relations.
* **Window and separation of duties** — F.10 or F.14 constraints included only when time, population, phase, or separation of duties changes the case.

### F.16:5 - The one-page Worked-Example Canvas

> Each item is a thought the reader needs, not a mandatory form field.

1. **Title, working situation, and gain.** Name the situation in ordinary language and say what practical error or decision the example resolves.

2. **Worked claim.** State one bounded claim. Example: “June availability is evaluated from observations of the defined service-delivery Work, not from the approved runbook.”

3. **Actual subjects.** List only the Systems, Methods, descriptions, delivery and evaluation Work occurrences, promise-content claims, characteristics, observations, values, operation applications, results, status uses, local system-role kinds, assignments, or other values needed by the claim.

4. **Direct pattern route.** Beside each substantive claim, cite the pattern that defines, constrains, or tests the value or relation used by the claim. This prevents one vague word or generic Bridge from taking over several relation families.

5. **Exact source basis.** Cite the source and edition and, where local wording matters, the expression, claim, and effective scheme. Add an F.17 cell only if repeated use needs a durable address.

6. **Obtaining relations.** For each relation, name its exact participants, direction, basis, and loss. Use F.9 only for a real semantic relation between distinct local meanings. Use the defining or testing pattern for MethodDescription membership, enactment, performed Work, measurement, evidence, fulfilment, kind, assignment, publication, transformation, and any load-bearing indicator relation. If proxy wording names no supported relation, use C.16.P and stop at A.6.RCD `missing-governor`.

7. **Evidence, result, and limits.** Show what observations or sources support the claim and how A.10 uses them. When evaluation is part of the case, show the evaluation Work, enacted Method, exact application and result binding, declared result scale, and any separate F.10 status or optional C.2.1 verdict episteme. Use B.3 only for assurance or material reliance. State what remains outside the conclusion.

8. **Optional comparison surface.** If two or more local meanings or source claims are hard to compare in prose, add one compact F.7 table. State the receiving-use conclusion separately. Omit the table when it adds ceremony but no clarity.

9. **Micro-narrative and checks.** In five to seven lines, walk from the working situation through the actual relations to the result. End with two or three F.15 checks and one explicit non-use boundary.

**Memory rule.** If the case cannot fit on one page or slide, reduce it to one claim or split it into linked examples. Do not delete the evidence or relation that makes the claim intelligible merely to preserve the page count.

### F.16:6 - Invariants

1. **Claim first.** The example states one recognizable claim and practical gain before its architecture.
2. **Actual subjects.** World, claim, evidence, status, and use assertions attach to actual values, not lexical cells or rows.
3. **Direct relations.** Every substantive relation cites the pattern that defines or tests it; F.9 is conditional on a real local-meaning relation, and the word *proxy* never supplies an indicator relation.
4. **Optional aids.** F.17 cells and F.7 tables appear only when they reduce reader effort and remain evidentially inert.
5. **Source precision.** Source and edition and the effective scheme are explicit where wording or interpretation changes the claim.
6. **Temporal honesty.** MethodDescription, Work, observation, and output remain distinct; windows are stated when they change the result.
7. **Agency precision.** When a system-role claim matters, name the local system-role kind, actual System, obtaining assignment, and performed-Work attribution as applicable.
8. **Evidence, evaluation, and boundary.** The page shows why the claim is supported; when evaluation occurs, it keeps evaluation Work, operation result, declared scale, EvidenceStatus, RequirementStatus, and optional verdict episteme distinct; and it states what none of them establishes.
9. **Didactic parsimony.** Every item changes the worked answer; optional machinery is omitted when it does not.

### F.16:7 - Optional comparison panel

When a table helps, use a small F.7 panel:

| Named comparison or use | Exact local claims or cells | Obtaining relations | Loss and boundary | Evidence | Separate conclusion |
| --- | --- | --- | --- | --- | --- |

The panel may also be a two-source contrast with **no relation asserted**. A source name becomes a column only when the comparison benefits from it. A row does not make entries the same, and the page does not compute a row-wide permission or assurance score.

### F.16:8 - Worked micro-example

**Title and situation.** *An alarm log does not by itself prove monthly uptime.* Operations has an approved runbook and a month of IEC task and alarm logs; a service report must judge the exact ITIL promise-content claim.

**Worked claim.** June uptime is judged from admissible observations of the promised service outcome over the stated population and window. Alarm and command records may contribute evidence only through explicit relations and coverage limits.

**Actual subjects and routes.** The ITIL promise content and its promise-use, delivery, and fulfilment relations use A.2.3; the service-delivery Work and separate evaluation Work use A.15.1; the exact observations, availability characteristic, scale, and values use C.16; A.6.1 identifies the evaluation application and result binding; F.12 supplies the evaluation shape; A.10 supplies evidence use; and B.3 applies only if assurance is claimed or reliance is material. The runbook is a MethodDescription under A.3.2 only when its claims concern one admitted Method, and its edition is surfaced here only if it changes the evaluation result or replay.

**Source basis.** Cite the ITIL edition and promise passage, IEC edition and task and alarm passages, observation source and procedure, and any source-local meaning needed to interpret *availability* or *alarm*.

**Relations and limits.** State which observations concern which Work. First ask whether the observation and measurement model directly concerns the promised availability characteristic. If it does, use C.16 and A.10 and add no proxy. If alarm-state intervals instead indicate a distinct unavailable-service characteristic, name both participants and the pattern that defines or tests that relation, with covered modes and blind spots. Use C.16.P to recover the relation and stop at A.6.RCD `missing-governor` when no such rule exists. Use E.13 only when the indicator is optimized or drives a target, incentive, gate, release argument, reputation signal, repair, or decision. F.9 is needed only if the exact local meanings of *alarm state* and *unavailable service* are themselves related.

**Result.** A System performs evaluation Work, enacts the evaluation Method, and applies the declared availability rule to June's in-scope observations. The A.6.1 application binds those inputs and returns a result on the declared acceptance scale. Map it to `RequirementStatus=Satisfied` or `RequirementStatus=Violated` only through the exact F.10 rule. If the evidence is inadequate, use `EvidenceStatus=Inconclusive` and leave `RequirementStatus=Pending`, or return the exact local result declared by the scale. Create a verdict episteme only if another use needs it. Plainly: met, not met, or cannot judge. The approved runbook establishes none of these results or statuses.

**Checks.** Actual subjects; a defining or testing pattern for each relation; direct-measurement-before-proxy; evaluation Work, application and result binding; declared result scale; separate EvidenceStatus and RequirementStatus; matching window and population; visible indicator limit; and no row-created fact.

### F.16:9 - Relations

**Builds on:**

- Use **F.1** for the exact source cut and **F.0.1** and **F.17** for each local claim or durable address actually needed by the case.
- Use **F.7** only for a readable comparison surface and **F.9** only for relations that actually obtain between exact local meanings, together with the separate bounded-use claim.
- Use **E.10.D1** to replace vague *context* wording with the source, scheme, scope, model use, working situation, comparison basis, or other value that changes the case.
- Use **F.10** for windows and **F.15** for the small set of replayable checks.

**Coordinates with:** F.4 and F.6 only when a local system-role kind, assignment, or performed-Work attribution is actually part of the case; A.10 for evidence use; B.3 only when assurance is claimed or reliance is material; and the direct Part C pattern for every illustrated subject and relation.

**Constrains:** A cross-domain example may use this canvas or a faithful reduction. It names claim and gain first, actual values and relations next, and optional aids last. It never treats a lexical cell, table row, page layout, or generic Bridge as proof.

### F.16:10 - Didactic distillation

> “Start with one practical question and one claim. Name the actual values involved and the pattern that defines each relation. Cite the exact source and evidence. Use a local-meaning cell only when you need a stable address; use a comparison table only when it makes the argument easier to read; use F.9 only when a real relation between local meanings is part of the case. State the result, its limits, and a few checks. The page displays the reasoning—it does not create it.”

### F.16:11 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **AP-1** | Architecture before question | The page opens with cells and routes but no recognizable problem. | Reader cannot tell what changes in practice. | Lead with situation, gain, and worked claim. |
| **AP-2** | Mandatory row | Every example must span two sources and contain a Concept-Set row. | Ceremony replaces the simplest adequate explanation. | Make the table optional; use direct prose when enough. |
| **AP-3** | Row-created sameness | Entries are “the same for this claim” because they share a row. | Layout becomes an ontological assertion. | State the actual relation and evidence, or show a contrast. |
| **AP-4** | Cell as subject | A RoleDescription, promise, Work, observation, result, or status is anchored to one cell as though the cell were that value. | Lexical address replaces the subject. | Name the actual value; cite a cell only for local wording. |
| **AP-5** | Generic Bridge | All cross-domain relations are labelled Bridges. | MethodDescription membership, description use, enactment, indicator, evidence, assignment, and fulfilment collapse. | Use each defining or testing pattern; recover unsupported indicator wording through C.16.P and A.6.RCD, and reserve F.9 for local-meaning relations. |
| **AP-6** | Global trigger word | *Role*, *function*, *process*, or *service* appears without recovering its subject. | Polysemy hides objects and relations. | Apply E.10 and F.0.1 and then choose precise plain wording. |
| **AP-7** | Design-time and run-time blur | A design description is narrated as Work. | Plan and occurrence collapse. | Use F.11, A.3, and A.15 and state the actual relation. |
| **AP-8** | Edition haze | Source name lacks the edition that controls meaning. | The example cannot be replayed. | Name the source, edition, and relevant passage. |
| **AP-9** | Evidence silence | The result appears without observations, source claims, or reliance basis. | Confidence cannot be assessed. | Show evidence use, limits, and non-use boundary. |
| **AP-10** | Ontologist’s shorthand | Predicate notation replaces an ordinary explanation. | Precision becomes inaccessible to the cold reader. | Lead with plain language; retain compact notation only when it genuinely shortens a repeated calculation. |

### F.16:12 - Extended worked micro-examples

#### F.16:12.1 - OWL class and FCA formal concept

**Situation and claim.** A product catalogue uses an OWL class named *Pump* and an FCA formal concept with a similar label. The example asks whether their covered products may be compared for one catalogue query.

Recover both exact local claims. State the actual relation, if any, between their extensions for this data set and the difference between OWL subclass semantics and FCA lattice order. A small comparison table may display the evidence and limits. Similar labels and table co-placement do not establish identity or class inclusion.

#### F.16:12.2 - System role and RBAC role

**Situation and claim.** The same System performs Work under a local operator system-role assignment and also has permissions grouped by an RBAC role. The claim is that these are different subjects even when both use the word *role*.

Use F.4 and F.6 for the local system-role kind, System, obtaining assignment, and performed-Work attribution. Use the access-control pattern for the permission grouping. Use E.10.ROLE and F.0.1 for the trigger word. State any separation-of-duties constraint directly. No disjointness or sameness follows from a table row or from spelling.

#### F.16:12.3 - Method description, Work, and service promise

**Situation and claim.** A build MethodDescription contains a target duration; dated build Work occurs; observations report actual duration; a service promise is evaluated for a calendar week.

Use A.3.2 for MethodDescription membership, A.15 and B.1.5 for delivery and evaluation Work and any Method enactment, C.16 for observations and measured values, A.2.3 and F.12 for promise evaluation, A.6.1 for the exact evaluation application and result binding, A.10 for evidence use, and B.3 only for assurance or material reliance. Cite the MethodDescription edition only if it changes the result or replay, and state separately whether the Work used it. A comparison table may show promised and observed values, but it establishes neither Work, result, status, nor a verdict episteme.

### F.16:13 - Safe reasoning moves

1. **Recognize.** State the working situation, failure, and practical gain.
2. **Bound.** Write one claim and one receiving use.
3. **Name actual subjects.** Replace vague words with the Systems, epistemes, Methods, Work, claims, observations, values, kinds, or assignments actually involved.
4. **Route relations.** Name the defining or testing pattern for each relation. For an alleged proxy, first test direct measurement; if a distinct indicator relation is needed and no rule supplies it, return A.6.RCD `missing-governor`.
5. **Recover local wording.** Cite the source, edition, and scheme; add F.17 only when recurring use needs an address.
6. **Show evidence and evaluation.** Explain how A.10 uses the evidence. When evaluation occurs, show the evaluation Work, Method, application, result binding, declared scale, separate F.10 status, and optional verdict episteme as applicable; use B.3 only for assurance or material reliance.
7. **Use aids sparingly.** Add an F.7 table only when it lowers reading cost; never infer from layout.
8. **State limits.** Include direction, loss, window, population, uncertainty, or non-use boundary that changes the conclusion.
9. **Replay.** Run two or three focused checks that target the case's real risks, including result and status separation when evaluation is present.

### F.16:14 - Acceptance tests

#### F.16:14.1 - Static conformance

* **SCR-F16-S01 (recognition).** Situation, failure, gain, and worked claim are clear to a cold reader.
* **SCR-F16-S02 (actual subjects).** No cell, row, label, or record substitutes for an actual value.
* **SCR-F16-S03 (direct relations).** Every substantive relation names its exact participants and cites the pattern that defines or tests it; unsupported proxy wording ends at A.6.RCD `missing-governor`.
* **SCR-F16-S04 (conditional F.9).** F.9 appears only for a real relation between distinct local meanings.
* **SCR-F16-S05 (source and evidence).** Exact sources and editions and the A.10 evidence-use basis are visible where they affect the claim; B.3 appears only for assurance or material reliance.
* **SCR-F16-S06 (optional aids).** Cells and tables are omitted when they do not reduce reader effort and are never evidential.
* **SCR-F16-S07 (time and agency).** Windows, Work, System, assignment, and attribution are explicit when material.
* **SCR-F16-S08 (one-page parsimony).** Every included item changes the answer; a larger case is split without losing its basis.
* **SCR-F16-S09 (evaluation architecture).** When evaluation is present, the performing System, evaluation Work, enacted Method, exact application and result binding, declared result scale, separate EvidenceStatus and RequirementStatus, and optional verdict episteme remain recoverable.

#### F.16:14.2 - Regression

* **RSCR-F16-E01 (edition drift).** Changed editions reopen only affected local claims and relations; no silent rewrite.
* **RSCR-F16-E02 (relation change).** A changed relation updates dependent conclusions and limits, not unrelated parts of the page.
* **RSCR-F16-E03 (sense split).** A changed local claim leaves no ambiguous F.17 address or table entry.
* **RSCR-F16-E04 (window change).** Changed cadence or population creates an explicit new evaluation boundary.
* **RSCR-F16-E05 (plain-language guard).** Repairing ontology does not replace readable sentences with avoidable symbolic or bureaucratic language.

### F.16:15 - Migration notes

1. **Refactor source tours.** Recover the practical question and one claim; keep only sources that change that answer.
2. **Replace mandatory rows.** Retain a table only if it improves comparison; move substantive relations and conclusions back to their direct statements.
3. **Replace cell subjects.** Name actual kinds, Systems, Work, claims, observations, values, and evidence; leave cells as optional wording addresses.
4. **Split generic Bridges.** Restore MethodDescription membership, description use, enactment, performed-Work, measurement, evidence, reliance, fulfilment, kind, assignment, publication, or transformation claims as applicable. Add an indicator relation only when a defining or testing pattern supplies it; otherwise retain the blocker.
5. **Repair trigger words.** Recover what *role*, *function*, *process*, *service*, or *context* denotes in each sentence before rewriting it.
6. **Keep the gain.** After every ontological repair, reread the page as a cold practitioner and simplify any wording that became harder without gaining precision.

### F.16:16 - Teaching variants

* **Single-source direct case.** One source, one actual value, one obtaining relation, one boundary; no table or F.9 relation.
* **Two-source comparison.** Two exact local claims, an optional F.7 row, and one separately supported conclusion.
* **Triangulated evidence case.** Promise, Work, and observation sources joined by their direct fulfilment, measurement, and evidence relations.
* **Difference lesson.** Two trigger-word uses kept distinct, with no relation asserted unless one actually obtains.
* **Window primer.** The same promise and Work evaluated under different explicit windows to show why result, status-use, and verdict-episteme identity must be checked separately.

### F.16:17 - Didactic checklist

* Recognizable situation, failure, and gain?
* One bounded worked claim and receiving use?
* Actual values named?
* Defining or testing pattern named for every substantive relation, with direct measurement checked before any proxy?
* Exact sources and editions and evidence where material?
* F.17 cell or F.7 table only if it lowers reading cost?
* F.9 only for an actual local-meaning relation?
* Evaluation Work, application result, declared scale, status family, optional verdict episteme, window, population, agency, loss, and uncertainty visible where they change the answer?
* Plain language retained after ontological repair?

### F.16:18 - Closing distillation

> A useful worked example is one replayable argument: situation and gain → claim → actual subjects → direct relations → exact sources and evidence → result and limits → a few focused checks. Cells and tables are optional reading aids. They never replace the values, relations, evidence, or judgement that make the example true.

### F.16:End

