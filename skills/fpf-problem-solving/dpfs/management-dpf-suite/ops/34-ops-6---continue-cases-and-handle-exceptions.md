## OPS.6 - Continue Cases and Handle Exceptions

> **Status:** Stable


### OPS.6:0 - Use This When

Use this pattern during one admitted continuing case when current facts, an exception, or a changed condition makes the standard next action uncertain. Typical cues are “the normal route no longer fits”, “the ticket moved but nothing changed”, “the model recommends a fix”, “we are waiting for one more result”, or “who may act now?” while the case subject, permission, performer, evidence, and next permissible Work are unclear.

The first useful result has one of two forms:

> **Progression:** for case subject `S` in qualified state `Q` at configuration and horizon `H`, matching permission `P` and domain Method `M` support next Work `W` by responsible performer `R`, with stop or fallback `F` and expected evidence `E`; after independently supported performance, report the progressed state `Q'` and its evidence to the participant responsible for the next operating decision under return conditions `N`.
>
> **Blocker:** condition `K` is missing, stale, contradicted, unauthorized, unsafe, unsupported, or unavailable; owner or source `O` must supply the bounded result; safe fallback or stop is `F`; retry when `T` obtains.

Recognition concerns a next action left uncertain by current case facts. Before action, assurance establishes the needed permission and performance conditions. After action, any progression claim needs performance evidence and support for the reported state.

Do not use OPS.6 to design one universal workflow or case lifecycle, reconstruct a reusable Method from event data, infer progress from a ticket, plan, model, trace, or record update, or revise priority merely because the case is old. Use `A.15.7` for the general situation-responsive next-action Method, `A.3.1.MR` when reusable Method recovery from several performances is the actual question, and `OPS.7` when temporal or consequence evidence can change priority or an existing commitment.

#### OPS.6:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| case | One bounded continuing Work situation organized around an exact subject, state, commitments, evidence, authority, and permissible next Work. It is not its file, ticket, queue position, or every Work item within it. |
| case subject | The patient, incident, user issue, release candidate, service relation, request, physical item, or other exact subject around which continuation is being coordinated. |
| case-state claim | A qualified claim about the case subject and relevant relations at a stated time or horizon. It changes only from adequate evidence. |
| exception | A fact or condition for which the standard continuation branch is absent, contradicted, no longer adequate, or requires bounded choice or return. It is not automatically an error or rare event. |
| matching admission and permission | The applicable case admission and independently supported current permission for the same matter, effective conditions, configuration, and horizon. A valid `OPS.5` result may carry both; admission alone is not permission. |
| deciding System | The System authorized to select or confirm the next permissible Work. It may differ from the responsible performer. |
| responsible performer | The System assigned and capable for the selected Work under its conditions. Assignment, capability, permission, authority, and performance remain distinct. |
| next permissible Work | The exact Work that may occur next under the applicable domain Method, permission, obligations, evidence, and stop conditions. A task description or tool call alone does not show that this Work was performed. |
| action choice | A selected next Work, probe, fallback, stop, or return. Choice does not perform the Work or progress the case. |
| Work occurrence | Dated performance admitted from direct evidence under the relevant configuration. Intention, assignment, invocation, trace presence, or artifact creation does not establish it alone. |
| evidence expected from performance | The observations, produced results, or records needed to judge what occurred. State the claim each supports, including any claim of a changed subject state or a failure. |
| record update | A change to a ticket, case file, plan, model, trace, database, or dashboard. It may carry evidence but is not the case-state change by itself. |
| unmet condition | The exact missing, stale, contradicted, unauthorized, unsafe, unsupported, or unavailable condition that prevents a truthful next action or progressed state, together with its return or stop. |
| progression result | Either an evidenced progressed case state with its next return, or an unmet-condition return with owner, fallback or stop, and retry condition. |

### OPS.6:1 - Problem Frame

Continuing cases do not simply advance because a standard sequence exists. New observations, dependency failures, changed permissions, resource relations, specialist decisions, or unexpected outcomes can make yesterday's next action unsafe, impossible, or irrelevant. The operation still needs a bounded way to continue without replacing the applicable clinical, engineering, legal, safety, security, or other domain Method.

The practical problem is to select the next permissible Work from the current situation and then admit progression only after performance and evidence, while returning exact blockers rather than fabricating a state transition.

### OPS.6:2 - Problem

A selected workflow transition can be mistaken for performed Work or an evidenced change in the case. A case-file state, agent loop, plan update, model recommendation, or “done” ticket appears to settle the case even when no authorized performer acted or the resulting subject state is unknown.

The opposite failure treats every exception as improvisation. Practitioners bypass mandatory domain branches, create an ungoverned OptionSet, or keep analyzing without a responsible performer, stop, evidence expectation, or return. Cases then drift between records while obligations and commitments remain unresolved.

### OPS.6:3 - Forces

| Force | Tension |
| --- | --- |
| responsiveness versus currentness | Cases need timely continuation, but stale facts or permission can make the selected action inapplicable or harmful. |
| domain Method versus local exception | The applicable Method constrains permissible Work, yet current facts may require recognition, adaptation, comparison, probe, or return. |
| chooser versus performer | The System that decides may not perform; collapsing them hides assignment, capability, permission, and responsibility. |
| action versus evidence | Selecting a good action is useful, but it does not show that Work occurred or the case changed. |
| recordability versus subject truth | Files and transitions support coordination, but they represent rather than constitute the case subject and state. |
| automation speed versus authority | Automated episodes can run quickly, but tool access and output do not establish permission, software assurance, release, or accountable continuation. |
| progress pressure versus honest blocker | A visible “next state” is attractive, while naming an unmet condition may be the only truthful result. |

### OPS.6:4 - Solution

#### OPS.6:4.1 - Confirm the case and matching permission

Name the exact case subject, current configuration and horizon, and the demand or commitment being served. Recover the applicable admission and the required current permission for the same matter and conditions. A valid `OPS.5` result may carry both; admission by itself does not establish permission. If the required permission is absent, expired, or contradicted, return that blocker to the authority or source that can resolve it; do not select Work or claim progression under a merely similar item, earlier approval, queue rank, or general mandate.

#### OPS.6:4.2 - Refresh the action-changing situation

Recover the current qualified case state, applicable domain Method, obligations and operating commitments, action-changing evidence and its currentness, relevant permissions and authority, and the condition that made continuation uncertain. Follow only the reach that can change the next action; unaffected case claims remain reusable under their conditions.

#### OPS.6:4.3 - Separate decision, performance, records, and state

Name the deciding System, responsible performer, required permission or authority, available actions, actual Work to be performed, records used or changed, and the state claims the result may support. Do not infer one relation from another. If performer capability, assignment, access, permission, or authority is missing, return that exact condition.

#### OPS.6:4.4 - Use the least elaborate adequate steering branch

Apply the direct mandatory branch when a current rule and facts determine the next permissible Work. Use recognition when one current situation clearly matches a governed action. Adapt within the applicable domain Method when a bounded variation is authorized. Use `C.11` only when several admissible live actions genuinely require comparison. Select a bounded probe only when its expected information can change the decision. If no permissible action exists, generate candidates through the owning practice or return the missing result instead of improvising an ungoverned action.

#### OPS.6:4.5 - Specify the executable continuation contract

State the selected next Work, responsible performer, permission and effective conditions, stop or fallback, expected evidence, and the return to continuing operation. Name the observable change that would invalidate the action and require refresh. An existing plan, instruction, prompt, ticket-transition record, or model recommendation can carry this contract if it states these terms and identifies the required authorization.

#### OPS.6:4.6 - Admit performance and update state separately

After the Work, recover direct performance evidence, the changed subject or result, failures and limits, and the claim each observation supports. Update the case-state claim only when the relevant Work and resulting evidence are independently adequate. If Work did not occur or evidence is insufficient, retain only earlier claims whose support still holds and return the unmet condition. A contradicted or expired claim becomes unsupported or unknown; it is not restored merely because a new result is missing. Never use a record update, successful invocation, generated artifact, or selected action as automatic progression evidence.

#### OPS.6:4.7 - Return one usable result

Return either:

- an evidenced progressed case state, its evidence and limits, fulfilled or still-open obligations, and next return; or
- the unmet condition, direct owner or source of the needed result, safe fallback or stop, and exact retry condition.

Return a required priority, commitment or policy decision to its Operations owner, and a specialist decision to the practice that can supply it. The continuation result does not inherit their authority.

### OPS.6:5 - Archetypal Grounding — Three Continuing-Case Replays

#### OPS.6:5.1 - PumpWorks field incident

Continue the constructed matter in OPS.5:5.1. At 09:05, incident I73 remains unresolved on installation P4. A field report describes intermittent pressure readings; neither their cause nor correction is known. The incident lead has authorized engineer E18 to inspect the identified captured logs until 11:00. The permission allows reading and diagnosis, not altering the deployed controller, declaring safety or releasing R42.

The applicable diagnostic procedure says: compare the captured sensor and controller timestamps; if the discrepancy persists in the captured interval, retain the discrepancy claim and request live verification; if identity fails or the data are corrupt, stop and return to the log owner. This direct rule is sufficient—no alternative-ranking exercise is needed. The incident lead chooses the bounded continuation; E18 performs it. The expected evidence is the identified input, execution trace, comparison result and its time interval.

The supplied observations are: E18 performed the comparison from 09:05 to 09:25; the retained trace identifies the P4 capture and comparison; a timestamp mismatch occurs in that capture; no live verification or controller change was performed. The defensible update is **“discrepancy established in the captured interval; live cause and present field condition unresolved.”** It is progress in diagnosis, not restoration of the installation. E18 returns the trace and this limited claim to the incident lead, closes I73-D at a safe stop and requests observational live verification in the 10:00–11:00 contact window. At 09:30 the field owner confirms access and the required permission for that bounded observation, without authorizing a setting change.

At 09:50 the field contact withdraws availability. The lead cannot start live verification under the earlier access assumption. The result becomes a returned access-and-permission condition, with the field owner as recipient and confirmed contact plus matching permission as the retry condition. Offline analysis of the already authorized capture remains allowed. The separate R42-T9 lab procedure, fixture check and performer are unaffected and remain in use; its result at 10:10 can support only its laboratory criterion. The operation does not erase the captured discrepancy or assert a current safe field state from the lack of a new report.

The next participant receives the bounded diagnostic result, the live-verification blocker, still-permitted work and the next useful contact action. OPS.7 uses those facts for priority and promise decisions without treating the diagnostic return as authority to change either.

#### OPS.6:5.2 - Public-hospital clinical case

One admitted clinical case continues from the exact patient and clinical-case subjects, current observations, applicable clinical and operating Methods, authorized practitioners, bed and resource relations, service obligations, and current consent, privacy, safety, and statutory conditions. A qualified clinical System retains medical decisions.

OPS.6 can state the next authorized clinical or operating Work, responsible performer, stop or fallback, and evidence needed before the case-state claim changes. Missing consent, clinical evidence, bed relation, competence, medical-safety return, or statutory permission remains an unmet condition, not an Operations workaround. A record closure, bed-board move, or elapsed wait does not establish treatment, patient change, or clinical resolution.

#### OPS.6:5.3 - AI-assisted user issue

An admitted user issue encounters a changed trace, tool result, provider condition, model input, candidate change, or harness state. The operation refreshes evidence and applies the software domain Method and current established authority. It distinguishes the human or other deciding System, the responsible performer, agent episode, tool invocation, candidate change, test evidence, issue record, and release decision.

The continuation contract may authorize one bounded diagnostic, test, or repair Work with context and tool limits, stop, fallback, evidence expectation, and human return. Report issue or candidate progression only after performance evidence supports it. A successful episode, green local test, visible trace, automated loop, or generated patch does not by itself establish issue progression, an integrated change, software assurance, a security result, or release permission.

### OPS.6:6 - Bias-Annotation

| Bias or pressure | How it distorts continuation | Countermeasure |
| --- | --- | --- |
| workflow-state bias | A configured transition becomes the case truth. | Recover the exact case subject, performance evidence, and qualified state separately. |
| action bias | Selecting any next step feels better than returning a blocker. | Use direct mandatory and recognition branches first; return when no permissible action exists. |
| automation bias | A successful agent episode or model output is treated as progress. | Separate invocation, Work, artifact, evidence, integration, and case-state claims. |
| plan-completion bias | Updating a plan or checklist appears to satisfy the obligation. | Name the actual Work, responsible performer, result, and evidence expected. |
| stale-permission bias | Earlier permission is reused after conditions changed. | Match matter, conditions, configuration, horizon, and authority before selection. |
| expert-shadowing bias | Operations quietly substitutes for clinical, safety, legal, or engineering judgement. | Return the bounded specialist result and keep the receiving coordination decision local. |
| exception novelty bias | Every surprising event is treated as unprecedented improvisation. | Reuse the applicable domain Method and choose the least elaborate adequate branch. |

### OPS.6:7 - Conformance Checklist

- [ ] The exact case subject, configuration, horizon, and served demand or commitment are named.
- [ ] The required current permission is supported for the same matter and conditions; admission alone is not treated as that permission.
- [ ] Current case state, domain Method, obligations, commitments, evidence, and exception are recovered.
- [ ] The authorized chooser and capable, assigned performer are identified; neither selection nor a record update is reported as performance or case change.
- [ ] Direct mandatory or recognition branches are used when adequate.
- [ ] `C.11` is used only when several admissible live actions genuinely require comparison.
- [ ] The continuation contract names Work, performer, conditions, stop or fallback, expected evidence, refresh, and return.
- [ ] Case progression is reported only after independently supported Work and adequate resulting evidence.
- [ ] The result is either evidenced progression or an exact unmet-condition return with owner, fallback or stop, and retry.
- [ ] Specialist and wider Operations results remain with their owners.

### OPS.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| workflow transition equals progress | A representation substitutes for changed case state. | Require independently supported Work and resulting evidence. |
| selected action equals Work | A choice or instruction becomes a performance claim. | Name performer and admit the dated Work separately. |
| agent ran, therefore case advanced | Invocation and output hide authority, integration, and subject evidence. | Preserve episode, Work, artifact, test, integration, decision, and state distinctions. |
| generic exception handler | One fallback overrides domain Methods and specialist returns. | Recover the applicable Method and exact unmet condition. |
| chooser-performer collapse | Decision authority, assignment, capability, and performance become one relation. | Name and support each relation independently. |
| stale authorization carryover | Permission survives changed conditions by default. | Revalidate exact matter, configuration, horizon, and effective conditions. |
| endless analysis | No responsible performer, stop, evidence expectation, or return is stated. | Produce the executable continuation contract or a blocker return. |

### OPS.6:9 - Consequences

The operation gains a defensible continuation move for exceptional and changing cases. Practitioners can tell what may happen next, who should perform it, what evidence will count, when to stop, and whether the case truly progressed or remains blocked.

The cost is that visible motion no longer counts as progress by default. In some cases, the account cannot yet report progression while an unmet condition is returned.

### OPS.6:10 - Rationale

Case continuation sits between permission and evidence. If it collapses into admission, selection appears to perform Work. If it collapses into priority or commitment management, elapsed time or consequence pressure can bypass the applicable domain Method. Keeping the continuation contract and the later state update separate makes exceptions usable without inventing a lifecycle.

The two-result form is deliberate. An exact unmet condition with owner, safe fallback, and retry can be the complete useful Operations result. It prevents administrative state changes from hiding missing permission, capability, evidence, or specialist conclusions.

### OPS.6:11 - SoTA-Echoing

The decision is how to continue a case after new facts while reporting a defensible result. A strong incumbent combines authorized case planning with outcome-aware execution. [CMMN 1.1, §4.1 and §5.4.9](https://www.omg.org/spec/CMMN/1.1/PDF) supplies runtime discretion, procedural subwork and planning authorization. Current [DCR robot documentation](https://documentation.dcr.design/documentation/dcr-robots/) distinguishes effect success, failure and timeout and the associated continuation. OPS adopts these mechanisms.

In I73, such an arrangement can authorize log inspection, execute a diagnostic activity and route a failed or unavailable live verification. If its case contract already states the capture identity, evidence interval, external subject claim and receiving authority, it produces the same adequate continuation as OPS.6. A second contract would only add synchronization work. The residual arises when an engine's successful diagnostic activity is used as evidence that the physical installation is now restored. Sections 4.5–4.7 bind the operation's observation to its warranted subject-state claim: the capture shows a discrepancy; present field condition remains unresolved. Loss of contact stops the dependent action without invalidating independent laboratory work.

That addition costs the domain mapping from execution outcome to observation and subject claim, a check of current permission, and a return the next participant can use. It does not require a new case model or a probe whenever a direct procedure is sufficient. More detailed logging can delay a time-sensitive response; collect the evidence needed by the actual receiving decision, not every available event.

FPF `A.15.7` supplies situation-responsive steering and `C.11` the conditional comparison branch. DEMO helps distinguish production and coordination; software-runtime sources inform bounded automation and stopping. Their execution semantics, source-local roles and software evidence do not grant external domain authority. Reopen when the incumbent already preserves the same physical-subject and permission distinctions more cheaply, or changed evidence, permission or execution semantics defeats the current continuation.

### OPS.6:12 - Relations

- `OPS.5` supplies admission and may carry independently grounded start permission for the same matter and effective conditions.
- `A.15.7` governs the general situation-responsive steering Method. `A.3.1.MR` separately governs candidate reusable Method recovery from several performances or other direct evidence.
- `C.11` governs comparison only where several admissible live actions require choice. `A.10` governs evidence reliance; `A.15.8` governs the performance configuration or recovery dependency when that is current.
- `OPS.7` may consume an evidenced progressed state or unmet condition only as evidence where it changes priority or an existing commitment. It does not inherit revision authority.
- `OPS.8`–`OPS.13` retain wider queue, capacity, interacting-structure, and commitment-account questions.
- Clinical, medical-safety, consent, privacy, legal, software assurance, security, release, provider, capability, and other specialist practices retain their decisions and evidence.
- Practitioners may enter OPS.6 directly with matching valid permission for an admitted case, repeat it as facts change, stop at a blocker, or return to another current pattern.

### OPS.6:End
