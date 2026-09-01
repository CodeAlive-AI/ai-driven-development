## A.15.7 - Situation-Responsive Work Steering and Next-Action Selection

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Choose the next action while Work is under way and current facts matter.

**Primary reader.** A person, team, robot, AI system, organization, or other deciding System that must choose what should happen next during ongoing Work, or someone supporting that choice.

### A.15.7:1 - Problem frame

**Use this when.** Use this pattern when you are in the middle of Work, current facts can change what should happen next, and a domain Method still sets what is allowed.

**First useful result.** Give a short answer with three visible parts:

1. **Decision now:** take this next action because this current fact and the Method's limits make it the best supported choice.
2. **Performer:** name the System that will perform it. If another System made the choice, name the chooser separately.
3. **Stop and feedback:** say when to stop, fall back, or look again, and which resulting observation can inform the next choice.

For a reversible local choice, ordinary project language is enough. Create a durable claim-bearing episteme only when another use needs to cite, compare, audit, or rely on the answer. The answer does not itself perform or predict the action, and this pattern adds no universal action, situation, or next-step kind.

**Three recognition cases.**

- A DJ is already performing. The current track is ending, the room response has changed, a promised genre constraint still applies, and several known tracks remain possible. The question is what to play next, who will make the transition, and what cue would make the DJ abandon it.
- A case worker is handling an open case. New evidence may make the displayed case state stale, while policy and authority still bound the allowed response. The question is whether to refresh, take the safe fallback, compare several live actions, or stop.
- A robotic maintenance system receives a recommendation during inspection. A sensor state has changed since the recommendation was produced. The question is whether the recommendation remains usable, needs refresh, or must give way to a safe response.

**What goes wrong if missed.** A plan, policy, score, case file, recommender, dashboard, trace, or pattern body is treated as the chooser. Every cue is forced into a heavy decision record, or every adjustment is called improvisation. The team may also invent an option set after the real issue has become stale information, missing authority, missing capability, or no current Work at all.

**What this buys.** The user gets one practical next action without losing the domain Method, current Work, deciding System, performer, authority, and stop or feedback condition. Familiar recognition, quick adaptation, explicit comparison, candidate generation, and tool-call planning remain different branches rather than one universal procedure.

**Not this pattern when.** Use the nearest applicable pattern instead:

- Before Work exists, use `A.15.2` for intended-work content and `A.15.5` for work-entry readiness.
- When ongoing Work is blocked because an exact performer, support, or continuation-state relation is missing or unsupported—not because known candidates need choosing—use the actual-Work branch of `A.15.8` to repair that configuration or stop, then return here.
- For a settled short procedure with no material branch, use the applicable domain Method; consult its `A.3.2` MethodDescription when a description is needed.
- For a choice outside current Work when the chooser and `OptionSet` are already known, use `C.11`.
- For missing action candidates, use a subject-specific generation Method; use `C.18` only for an actual open-ended candidate archive and front.
- After the action is fixed, use `C.24` only if calls to tools or services must be planned.
- For a plan revision before Work, use `A.15.2`.
- For retrospective Method recovery, use `A.3.1.MR`.

**When a DPF reuses this pattern.** A DPF uses it only for a live next-action question that passes this entry. Reuse supplies the general steering Method; the DPF still names any domain-specific problem, facts, authority, vocabulary, result, and return that change what its practitioner does. If no such use-changing contribution remains, cite this pattern rather than copying it.

### A.15.7:2 - Problem

Situation-responsive Work needs more than permission to vary. A practitioner must notice which facts can change the continuation, remain within the applicable domain Method, distinguish choosing from performing, and know when to stop or reconsider. Existing choice doctrine begins too late when the available actions are still being recovered from current Work. Planning begins too early when the Work is already happening. Tool-call planning begins after the underlying action has been fixed.

Without a direct Method, teams oscillate between two errors. They follow an obsolete plan as though nothing changed, or they call unconstrained variation improvisation and lose reviewability. In both cases the current fact, relevant Method limits, chooser, performer, and return condition disappear.

### A.15.7:3 - Forces

| Force | Tension |
| --- | --- |
| Responsiveness versus method discipline | Current facts may require a different continuation, but the domain Method still limits admissible action. |
| Speed versus truthfulness | A cheap reversible choice should stay light; stale or consequential input needs refresh, comparison, fallback, or stop. |
| Recognition versus explicit comparison | A familiar cue may support one response without constructing an `OptionSet`; several live alternatives may require `C.11`. |
| Choice versus action | The deciding System and intended performer may be the same or different, and neither a score nor a document occupies either position. |
| Domain Method versus steering Method | The reusable way being performed and the Method for choosing its next action are distinct even when the same Work enacts both. |
| Feedback versus retrospective rewriting | A new observation may inform the next choice or a later Method change; it does not rewrite completed Work or the earlier Method. |
| Plain use versus durable reliance | Most local choices need a readable sentence; another use may need a separately identified claim-bearing episteme and exact supporting relations. |

### A.15.7:4 - Solution

Use the following steering Method. Keep the answer as small as the current decision permits, and stop as soon as a direct result or honest blocker is available.

#### A.15.7:4.1 - Keep the two Method positions distinct

The **domain Method** is the reusable way whose current enactment is being steered. It states the applicable way of doing, participant meanings, intended result or preserved condition, allowed variation, and stops.

The **steering Method** supplied here uses current facts to choose one next action within those limits.

Usually, one current Work occurrence may enact the domain Method and, when this steering Method is actually used, also enact the steering Method. Before either claim, use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If this account must also say under which assignment the Work was performed, check that relation separately through F.6. Ground each `enactsMethod` claim separately; neither follows from the other. If the choice must be treated as a smaller Work occurrence, identify its own performer and Work basis and state its relation to the larger Work only when that relation actually obtains.

A domain Method may instead be an admitted composite containing the steering Method as a submethod. That requires the identity of both Methods and an exact composition relation under `A.3.1` and `B.1.5` or another direct composition rule. Method composition still does not prove that a particular Work occurrence enacted the submethod.

Reading this pattern, consulting a MethodDescription, following a plan, or receiving a recommendation establishes none of those Method, composition, or enactment claims.

#### A.15.7:4.2 - Run the seven-step steering Method

1. **Confirm current Work or close this entry.** Name the ongoing Work occurrence at the grain that changes the decision. When the performed-Work claim matters, first use A.13 to identify the actual performer, then let A.15.1 independently admit the dated occurrence from its performance history, enacted domain Method, time, and required containing-System relation. If this steering account must also identify the assignment under which the Work was performed, check that assignment separately through F.6; F.6 identifies neither performer nor assignment, and a failed check leaves the Work intact. If Work has not begun, stop using this pattern: use `A.15.2` for intended-work content, `A.15.5` for work-entry readiness, or `C.11` only when a known chooser must compare an already formed `OptionSet`. Do not turn intended Work into a current occurrence or every small action into separate Work.
2. **Use only action-guiding information about current facts.** Name the relevant observation, participant response, available material, resource or safety limit, commitment, case fact, or time pressure. If an observation, report, recommendation, displayed case-state claim, or other relied-on information may be out of date, has no checkable source, or has no stated time window for use, re-observe it or refresh it from its source; otherwise use a named safe fallback or stop. A directly checkable live cue needs an ordinary observation sentence, not a universal situation record or evidence dossier.
3. **Recover both Method positions.** State the domain Method and its relevant allowances and stops. State the steering Method only when it is actually used, and choose the separately grounded co-enactment or admitted-submethod account in §4.1. A description, plan, policy, score, case model, recommender, or dashboard may inform the decision; it neither acts nor decides.
4. **Form the smallest honest set of available actions.** Include only actions allowed now by the domain Method and named constraints. If the Method already requires one action and no material branch remains, follow it and stop using this pattern. If no acceptable action is known, use a subject-specific generation Method; use `C.18` only when an open-ended candidate archive and front are actually needed. Do not hide invention inside choice.
5. **Use the lightest truthful choice mode.** State the cue, comparison, quick forecast, value concern, or mandatory criterion that can change the answer. A reliable cue may select a familiar response after an applicability and consequence check. An unfamiliar or consequential case may require diagnosis, adaptation, or a quick mental or physical forecast. When several live alternatives genuinely require comparison, pass the chooser, current `OptionSet`, comparison basis, and probe question to `C.11`.
6. **Keep choosing, authority, and acting separate.** Name the deciding System and the intended performer. If the choice depends on permission, responsibility, commitment, capability, or authority, establish that exact relation instead of inferring it from a system-role label or recommendation score. If the required relation does not obtain or cannot be grounded, return to the System that must supply it or stop.
7. **Return decision, performer, and feedback separately.** State the selected action and the reason that distinguished it, the intended performer, and the nearest stop, fallback, new observation, or return to ongoing Work. If the choice changes intended-work content, update the `U.WorkPlan` separately. If the action is performed, follow step 1 to identify its actual performer and admit the dated Work; add F.6 only if the returned result must also identify the assignment under which the action was performed, and ground any operation application separately. Retain the resulting observation without rewriting the earlier Method or Work.

#### A.15.7:4.3 - Select the current branch

| Current situation | What to use now | Result and stop |
| --- | --- | --- |
| The domain Method already requires one action | Follow the Method or its selected description directly. | The required action and its existing stop; no steering or decision wrapper. |
| One familiar live cue points to one response and a quick consequence check passes | Use the recognition branch in this pattern. | One decision, intended performer, live cue, and nearest return to ongoing Work. |
| Several admissible actions remain and comparison can change the choice | Use `C.11`; add `A.19` kernels only when their comparison or selection result matters. | A `ChoiceResult` that fits the applicable constraints, then return here for performer and feedback. |
| The available actions are absent or inadequate | Use a subject-specific generation Method; use `C.18` only for an actual open-ended archive/front question. | New candidates or an honest failure to generate; no premature choice. |
| The action is fixed but calls to tools or services must be planned | Use `C.24`. | A call plan and checkpoint return; the call plan is not the underlying choice. |
| An observation, report, recommendation, case-state claim, or other action-guiding information is outdated or lacks usable time or source support | Re-observe it or obtain up-to-date information from a named source; otherwise use the named safe fallback or stop. | No action justified by an old recommendation, case-state claim, resource report, or participant-response report. |
| Safety, authority, capability, applicability, or current Work is unresolved | Use the pattern that defines or tests the missing claim—for example, `A.2.2` for capability, `A.15.1` for performed Work, and `A.15.5` only for work-entry readiness; keep safety, authority, and applicability with the pattern that defines them. | No fabricated action, permission, capability, Work, or Method change. |

#### A.15.7:4.4 - Keep the first result light

For a reversible local use, speak plainly: “Choose track B because the room response changed and it still satisfies the promised genre constraint; the DJ performs the transition; abandon it if the next cue shows the transition is failing.”

Only a named later use justifies a durable claim-bearing episteme. Identify it under `C.2.1`, state what exact decision or observation it concerns, and include only the source, currentness, authority, comparison, or assurance distinctions on which that use relies. Do not mint a general `SituationRecord`, `NextActionRecord`, or `FeedbackRecord` merely to preserve the template.

### A.15.7:5 - Archetypal Grounding

#### A.15.7:5.1 - DJ performance

A DJ is already performing under an event performance Method. The current track is ending, the DJ directly hears that room response has fallen, one promised genre constraint still applies, and three known tracks fit the remaining time. The DJ rules out one track because its transition violates the domain Method, recognizes a familiar cue favoring a second, briefly checks how the transition is likely to land, and chooses it.

The answer names the chosen track and reason, the DJ as chooser and intended performer, and the condition for abandoning the transition. The current Work separately enacts the performance Method and, because this steering Method was actually used, the steering Method. The playlist shows available material; it is not the performer, the whole Method, or proof that either enactment obtains.

#### A.15.7:5.2 - Social dance or jazz

During one performance, a participant recognizes a familiar phrase ending and chooses a contribution that fits the domain Method and the other participants' current response. A quick forecast is enough because the contribution is reversible and the next cue arrives immediately. If several materially different contributions need comparison, the chooser forms a current option set and opens `C.11`; otherwise no formal comparison record is needed.

The performers, deciding System, musical or movement material, interaction, Methods, and Work occurrence remain distinct. “Improvisation” is a retrieval word here, not a universal Method or permission for random variation.

#### A.15.7:5.3 - Case handling and stale information

A worker is performing one case-handling Work occurrence under a domain Method. A displayed case state predates newly filed evidence. Because that age can change the action, the worker refreshes the case state before relying on it. If refresh is unavailable, the worker uses the declared safe fallback or stops. The case file records claims; it neither chooses, supplies authority, nor performs Work.

If the organization's admitted case-handling Method already includes this steering Method, state that composition separately. Do not infer it from the case model or a repeated workflow label.

#### A.15.7:5.4 - AI recommendation

An AI model proposes the next inspection action, but a sensor condition changed after the model's input window closed. The model and recommendation remain separate from the deciding and performing Systems. The responsible deciding System refreshes the input, tests the recommendation under the current Method and safety constraints, uses a safe fallback, or stops. A confident score establishes neither currentness, authority, capability, nor the action.

### A.15.7:6 - Bias-Annotation

- **Optimization bias:** do not force every responsive choice into a fully enumerated optimization problem.
- **Human-only bias:** deciding and performing Systems may be people, teams, robots, AI systems, organizations, or other equipped or combined arrangements.
- **Automation bias:** a recommender, score, dashboard, or case file informs a decision only through current and applicable claims; it does not become the chooser.
- **Improvisation romanticism:** responsiveness remains bounded by the domain Method, actual constraints, and stop conditions.
- **Record inflation:** durable records are optional and use-driven; a direct observation sentence can be enough.

### A.15.7:7 - Conformance Checklist

- **CC-A15.7-1 — Current Work.** Is ongoing Work identified, or did the user correctly stop and name `A.15.2`, `A.15.5`, or `C.11` for the question that remains?
- **CC-A15.7-2 — Method limits.** Is the applicable domain Method and the relevant allowance or stop explicit?
- **CC-A15.7-3 — Action-guiding information.** Does every stated fact matter to the action, and is the observation, report, recommendation, or other information current enough when that matters?
- **CC-A15.7-4 — Method relation.** Are domain and steering Methods distinct, with co-enactment or composition asserted only from its own basis?
- **CC-A15.7-5 — Available actions.** Are mandatory action, recognition, comparison, generation, and tool-planning branches kept separate?
- **CC-A15.7-6 — Chooser and performer.** Are the deciding System, intended performer, and any authority or capability claim stated separately?
- **CC-A15.7-7 — First result.** Does the answer visibly state the decision, performer, and stop or feedback condition?
- **CC-A15.7-8 — No backdating.** Are later observations, plan changes, performed actions, and Method changes identified separately rather than written back into earlier Work?
- **CC-A15.7-9 — Plain use.** Can a cold practitioner understand what to do before meeting the formal distinctions?

### A.15.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The dashboard chose the next action.” | Name the deciding System; state which current dashboard claim it used and why that claim remained applicable. |
| “We improvised.” | State the relevant domain-Method limits, current fact, chosen action, performer, and stop. |
| “Every cue needs a decision dossier.” | Keep a reversible live cue in ordinary language unless another use relies on a durable claim. |
| “The steering Method is obviously part of the domain Method.” | Either state two separately grounded enactments or admit the exact submethod relation; infer neither from consultation. |
| “The recommendation was recent enough.” | State the action-changing qualification window or refresh, safe fallback, or stop. |
| “The plan already contains the action, so Work occurred.” | Keep plan revision, next-action answer, and performed Work separate. |
| “Several options might exist, so use C.11 first.” | Recover the current Work, relevant Method limits, facts, and available actions first; use `C.11` only when several live options remain. |

### A.15.7:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Responsive Work remains methodical without becoming rigid. | The practitioner must identify the few facts that can actually change the next action. |
| Familiar cue recognition stays lightweight. | High-consequence or stale-input cases still require comparison, refresh, fallback, or stop. |
| Choosing, authority, and acting remain visible. | A recommender cannot absorb accountability merely because it supplies a score. |
| Feedback can improve later choices or Methods. | Completed Work and earlier Method claims cannot be rewritten after the fact. |
| `C.11`, candidate generation, and `C.24` keep clear entry points. | The user must stop this pattern when another question becomes current. |

### A.15.7:10 - Rationale

The missing contribution is not a new action ontology. It is a reusable Method for a common working question: what should this deciding System do next during current Work, given current facts and the Method that still bounds the Work? Keeping that Method separate from the domain Method preserves two independently testable claims while allowing either co-enactment or an admitted composite.

The pattern begins before late-stage option comparison and ends before tool-call planning or performed-action recording. That placement keeps the first result small and makes explicit comparison, generation, planning, evidence, and assurance conditional rather than universal burdens.

### A.15.7:11 - SoTA-Echoing

| Source line and status (qualified 2026-08-26) | Contribution | FPF adoption |
| --- | --- | --- |
| Recent peer-reviewed reviews: [high-risk decision-making](https://pmc.ncbi.nlm.nih.gov/articles/PMC10564111/) (2023) and [recognition-primed decision-making in sport](https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/) (2022) | Distinguish direct recognition, diagnosis or adaptation, quick simulation, rule-based response, analytic comparison, and adaptive response in different situations. | **Adopt the plurality of choice modes.** Do not turn one occupational model into a universal law; use the lightest truthful mode for the current case. |
| Mature representation standard: [OMG CMMN 1.1](https://www.omg.org/spec/CMMN/1.1/About-CMMN) (2016) | Represents discretionary, event-centered case work whose later actions can depend on changing case information. | **Use as a representation contrast, not as current universal practice.** A notation or case file does not identify the deciding System, establish authority, or supply this Method. |
| Current beta input: [OMG Essence 2.0 Beta 2](https://www.omg.org/spec/Essence/2.0/Beta2) (beta, March 2026) | Offers a current proposal for describing and composing engineering-method elements. | **Use only as neighboring beta Method Engineering.** Its beta status and method-description purpose do not make it a stable next-action doctrine. |
| Method Engineering lineage and recent review: the [2010 situational Method Engineering review](https://www.jucs.org/jucs_16_3/situational_method_engineering_state.html) and a [2023 review](https://doi.org/10.1016/j.procir.2024.06.001) | Show established and recent ways to construct or adapt Methods for a situation. | **Keep as neighboring Method Engineering.** Constructing or describing a Method is not the same Work as choosing the next action during its enactment. |
| Current FPF `A.15.1`, `C.11`, `C.24`, and `G.11` | Separates performed Work, fixed-option choice, downstream call planning, and refresh of a changed basis. | **Adopt directly.** Place this pattern between current Work/Method recovery and only the branch that becomes current. |

**Qualification and smallest reopen.** These sources were checked for the uses above on 2026-08-26. Reopen only the row and the recognition, adaptation, currentness, or case-handling passage whose action guidance changes. A newer example, a new decision model, or a status change with no practical effect does not reopen the whole pattern.

### A.15.7:12 - Relations

- **Builds on:** `A.3.1` for domain and steering Method identity; A.13 for each actual performer; `A.15.1` for independently admitted current Work and each separately obtaining enactment; F.6 when the result must also identify the assignment under which that Work was performed; and `A.10` for source/currentness reliance when it changes the action.
- **Coordinates with:** `A.15` for SystemRole–Method–Work alignment before next-action selection; `A.15.6` for recovery of the direct subject from project, process, or case wording before live Work steering; `A.15.2` for intended-work content and a separate WorkPlan change; `A.15.5` for work-entry readiness; `B.1.5` for admitted Method composition; `C.11` for comparison among a current `OptionSet`; `A.19` only for a current comparison or selector result; `C.18` only for an actual open-ended candidate archive/front; `C.24` for tool-call planning after the action is fixed; and `G.11` for scoped refresh.
- **Keeps separate:** chooser, intended performer, authority, capability, MethodDescription, plan, recommendation, performed action, result, and later Method or description change.

### A.15.7:End

