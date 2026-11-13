## C.26.2 - Enacted Distributed State Evidence

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless marked informative

### C.26.2:1 - Problem frame

Use this pattern when coordinated work, behavior, or trace patterns give evidence that a team, organization, service mesh, market, or other collective system is acting from a state that no single participant report, survey, policy sentence, dashboard, or API export faithfully carries.

The pattern supports a bounded claim about the collective's current organization or behavior from the evidence available across its parts. Distinguish what those observations establish about the state from what explains its occurrence, and preserve uncertainty in either question.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, incident lead, organizational analyst, or manager judging whether coordinated work, behavior, or trace patterns evidence a minimal collective-state reading. |
| Evidence-bound state reading | An evidence-bound state reading over a declared collective `U.System`. |
| Minimal state-reading move | Recover the collective pattern from its parts' observed actions and relations; retain the evidence, time and live interpretation limits needed by the receiving use. |
| Outside work | Unsupported group-mind or timeless-culture claims, a report mistaken for its subject, and questions already answered adequately by a routine, measurement or other subject account. |
| What changes in practice | The team can use coordinated work, behavior, or trace patterns as evidence without assuming one report faithfully exports the whole state. |

Plain glosses:
- `collective bearer`: the declared team, organization, service mesh, market slice, or other `U.System` whose coordinated work, behavior, or trace pattern is being read.
- `coordinated work or behavior`: role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action.
- `distributed-state reading`: a minimal evidence-bound interpretation of coordinated work or behavior.
- `carrier`: a log, trace record, dashboard, report, API response or other artifact that makes relevant work inspectable. A commitment, routine or change in work is distinguished from the record or observation used as evidence of it.
- `faithful-enough export`: a representation good enough for the current decision; when it is not faithful enough, state what was lost and why.

### C.26.2:2 - Problem

Teams often need to talk about latent alignment, readiness, market posture, service-mesh behavior, or an enacted "we already decided" before one explicit representation exists. Without a pattern, they oscillate between two bad options.

One option is unsupported collective-state language: "the organization knows", "the culture decided", "the market wants", or "the service mesh understands", used as if the wording established the state. The other option is false reduction: a survey answer, policy sentence, dashboard, or report is treated as the whole state.

Both fail. Coordinated behavior may evidence a working state, but it does not automatically identify a durable mind, internal representation, causal mechanism, or faithful-enough export for the intended use.

### C.26.2:3 - Forces

| Force | Tension |
| --- | --- |
| Work evidence vs explicit report | Coordinated work may provide more direct evidence than any one report, but the report is often the only portable carrier. |
| Minimal evidence-bound claim vs useful claim | The pattern must say something useful without claiming group mind or durable hidden ontology. |
| Evidence vs measurement | Some cases have formal measures; many have traces, commitments, routines, and artifacts instead. |
| Export need vs export loss | The state often must be summarized for a decision, but the summary may lose the coordination that matters. |
| Primary source family vs QL lens | Distributed cognition, team cognition, routines and socio-technical evidence are primary. QL additionally requires C.26's named residual contextual-model obstruction. |

### C.26.2:4 - Solution

Model the claim as evidence-bound `U.Episteme` over a declared collective `U.System`. Distinguish the collective's distributed state from the surveys, dashboards, reports, and API responses used to examine it.

If the proposed bearer is a market slice or service mesh, declare whether it is a collective `U.System`, delivery system, trace population, or evidence set. Continue with EDSE only when a collective `U.System` bearer is established; otherwise retain any supported trace-population or evidence-set claim. Do not infer systemhood from coordinated-looking traces alone.

Ground the reading in observed coordinated work or behavior and its evidence. Distributed cognition, routine dynamics and team cognition supply the primary interpretive accounts. These can support an EDSE result without QL; add that lens only when the C.26 activation test establishes a residual contextual-model obstruction.

Recover the enacted pattern before asking how it arose:

1. Locate the participants, actions and relevant times in the available observations or records. Distinguish an observed action from a report, plan or copied statement about it.
2. Connect the actions through the relations that support the proposed collective reading: for example, work handed between teams, jointly held releases, coordinated routing or use of a shared artifact. Preserve gaps in that connection; simultaneous traces alone may support only parallel activity.
3. State the narrow state claim those observations support for the declared bearer and window. A routine, command or shared stimulus may explain that same state rather than refute it. A claim about unspoken agreement, a new mechanism or durable culture needs the additional grounds that distinguish it from those explanations.
4. Examine serious alternatives only where they change the current reading or its use. Return the supported claim, or name the missing observation or relation that prevents it. If an existing routine or subject account already answers the receiving question, use it directly.

This separates two questions: what the collective was doing, and why it did so. The account need not posit an unexplained coordination residue.

Start with these recognition questions. Ordinary prose is sufficient when it retains their answers.

| Mini-entry | Question |
| --- | --- |
| Collective bearer | Whose coordinated work or behavior is being read: which team, organization, service mesh, market slice, or other declared collective system? |
| Carriers / window | Which observations or records of the coordinated work support the reading, and during which window? Distinguish the observed work or commitment from its evidence carrier. |
| Minimal state reading | What is the minimal state reading supported by the coordinated work or behavior, or by the trace pattern? |
| Live alternative, if any | Which plausible reading would change the state claim or its use, and what available observation distinguishes it? |
| Practical change | What can be done now without exceeding the evidence: adjust communication, triage, routing, planning, probe design, or return to a fuller evidence record? |

Use the fuller EDSE record below when the receiving claim or action needs distinctions that the recognition note does not retain. Reuse adequate existing content; publication, reuse, or leaving the immediate discussion alone does not require a fuller record.

Full EDSE record:

| Field | Question |
| --- | --- |
| Collective bearer | Which declared collective `U.System` is being described? |
| Observed coordinated work, behavior, and trace pattern | Which role-work, service behavior, market participant traces, routine, commitment, artifact use, or coordinated action is observed? |
| State reading | Which minimal state reading is consistent with the work? |
| QL cue or formal cue if retained after ordinary work, evidence, or routine explanation | Which named contextual-model obstruction survives ordinary work/evidence explanations and meets C.26's activation test? Omit this field for an ordinary EDSE use. |
| Evidence carriers | Which logs, trace records, commitment records, artifacts, dashboards, API responses or documents support the reading? |
| Probe or measurement approximation | Which survey, dashboard, API read, interview, trace query, metric, or publication approximates the state, and how may that probe change, thin, or frame the state reading? |
| Attempted export and faithful-enough criterion | What export was attempted, and what would count as faithful enough for the current decision? |
| Loss cause and higher-fidelity export | Why is the current export not faithful enough, and could a more discriminating probe, bridge, representation, or time window produce a higher-fidelity export? |
| Time window | During which window does the claim hold? |
| Persistence posture | Is the reading momentary, recurring, stabilized for the incident/release/window, or expected to persist under stated conditions? |
| Decay and refresh condition | What would make the reading expire, refresh, lose support, or need a new probe? |
| Rival interpretation, when material | Which plausible interpretation remains possible and changes the claim or receiving action? |
| Rival explanation not ruled out | Which ordinary explanation remains possible? |
| Minimal supported claim | What may be said without exceeding the evidence, carrier set, time window, or export limit? |
| Supported action or use | Which planning action, communication action, incident action, routing action, bridge use, evidence use, or decision use may now be taken without exceeding the claim? |

#### C.26.2:4.1 - Minimal claim principle

Preferred wording stays close to observed work:

- "During window W, the incident-response organization acted consistently with a rollback-readiness posture, evidenced by release timing, escalation criteria, and shared trace use."
- "The service mesh exhibited a coordinated throttling regime under policy P, evidenced by route changes and saturation traces."
- "Market traces support an expectation-shift claim under probe Q, with media amplification still a rival explanation."

Avoid wording that asserts a heavier claim, such as "the organization decided", "the market knows", or "the team has a distributed mind", unless another FPF pattern and evidence requirement independently support it.

#### C.26.2:4.2 - Finish conditions

Finish with one of these results:

| Result | Meaning |
| --- | --- |
| Minimal evidence-bound state assertion | State the collective bearer, the supported pattern of work or behavior, its observations or records and time window; add uncertainty, live alternatives and export limits when they affect the claim or use. |
| Export-loss repair | Keep the state reading minimal and add a bridge or publication note about what the attempted report, survey, API response, dashboard, or policy sentence lost. |
| Probe-coupled neighboring-pattern handoff | Apply `C.26.1` when the survey work, dashboard publication or use, interview, API operation, or publication act changed the state being evidenced while its output is being used as a passive read. |
| Measurement or evidence neighboring-pattern handoff | Route the main support requirement to `C.16` for a measurement's scale and method, `A.10` for evidence provenance and bounded reliance, or `B.3` for a named assurance claim; keep audit requirements under their direct domain pattern. |
| Work or authority question | Use the relevant work or authority pattern when the unresolved question concerns a command, routine, incentive or playbook. An adequate such account may already explain the enacted state. |
| State claim not established | Retain the supported observations and identify the missing bearer, relation, timing or evidence basis. Do not assert the distributed state that those inputs fail to establish. |

#### C.26.2:4.3 - Rival explanation rule

Consider these alternatives when they change the proposed claim. Explaining observed coordination does not erase the coordinated state.

| Possible explanation or alternative | Consequence for the reading |
| --- | --- |
| Policy, command, coercion or management pressure | A command may explain an enacted freeze; it does not establish voluntary agreement. Keep the supported freeze claim and use work or authority patterns for the distinct command claim. |
| Shared incentive or common external stimulus | The evidence may establish only parallel responses. Retain a collective coordination claim only when the needed relations among responses are supported. |
| Routine, habit, script or playbook | An observed routine can establish the current operating pattern. Its presence alone does not establish a new shared intention or durable culture. |
| Dashboard-following, metric gaming or social desirability | Determine whether the output evidences the claimed state or behavior induced by the reporting arrangement. Use `C.26.1` for the unresolved probe question. |
| Copied artifact, template, policy sentence or API response | Copying the statement does not establish its enactment. Locate the observed actions and any export loss. Use `F.9` only for a cross-context sense correspondence, and the publication pattern only for a publication question. |
| Diffusion, contagion, media amplification or signaling | Keep the observed pattern and qualify the proposed mechanism or expectation claim according to its grounds. |

#### C.26.2:4.4 - Export-loss discipline

The phrase "not faithfully exportable under current probe and bridge conditions" is supported only when the text says:

- what export was attempted;
- what would have counted as faithful enough for the current decision;
- what state, coordination, evidence path, timing, role alignment, option structure, survivor relation, or use limit was lost;
- whether the loss comes from bridge, measurement, representation, audience, timing, state change, or another cause;
- whether a more discriminating probe, bridge, representation, or time window could produce a higher-fidelity export.

#### C.26.2:4.5 - Compound-state decomposition card

When the reading depends on relations among parts, recover that organization explicitly. The table helps distinguish local observations, their supported connection and any explanation or uncertainty that matters.

| Field | Question |
| --- | --- |
| Whole system | Which collective `U.System` is being read, and under what boundary? |
| Subsystems | Which locally readable Systems participate as subsystems? Use teams, roles, services, markets, routines, artifacts, or work lanes to locate them while retaining each clue's own kind. |
| Local state readings | What state reading does the evidence support for each part? |
| Correlation or coordination evidence | Which traces, timing, work transfers, commitments, artifact uses, or role-work alignments show coordination? |
| Explanatory basis | Which routine, policy, stimulus, incentive or other mechanism is supported, and what part of the current claim does it explain? |
| Collective pattern | Which relations among the observed activities support the proposed state reading? What remains unresolved? |
| Minimal supported claim | What evidence-bound claim survives for the declared time window and carrier set? |
| Supported action or use | Which planning action, communication action, incident action, routing action, bridge use, evidence use, or decision use may now be taken without exceeding that minimal claim? |

#### C.26.2:4.6 - Evidence-bound state reading and claim floor

The evidence-bound state reading is a `U.Episteme` reading over coordinated work, behavior, or trace patterns by a declared collective `U.System`. The pattern does not govern an inner group entity, a culture substance, a market mind, a hidden service intelligence, or a reusable kernel state kind.

The useful state claim retains the collective bearer and boundary, the observed pattern, the evidence supporting it and its time window. Include persistence, probe or export conditions, serious alternatives and further subject work only when the receiving claim depends on them.

This pattern is useful because many work states are enacted before they are articulable. For example:

- A team may behave as if a release freeze exists before any single person states it cleanly.
- A service mesh may exhibit one routing posture before any one dashboard carries the whole situation.
- A market may shift expectations before any one survey faithfully exports the shift.

These enacted patterns can support bounded state claims. The carrier remains distinct from the state.

#### C.26.2:4.7 - Operational evidence sequence

1. Name the collective bearer as a declared `U.System` and state its boundary; a bare social label does not establish that System.
2. Name the coordinated work, behavior, or trace pattern being read: actions, routines, commitments, role-work, service behavior, market participant traces, artifacts, or timing. For a particular dated Work claim, use the `A.15` alignment route through `A.13` and independent `A.15.1` admission; add `F.6` only when the receiving use needs precise assignment-bound attribution through the same obtaining assignment.
3. Identify the observations or records and what each supports. Use `A.10` when a replayable source-to-use account is needed; the empirical claim always retains its required support.
4. State the time window and any serious alternative that changes the reading. Add persistence support, decay/refresh conditions and reprobe cost only when they affect the claim or receiving action, following :4.11. When considering another observation, weigh what it could add against its effects on participants and on the evidence. For example, a quick follow-up in a small team could reveal who gave a response or change what participants report next.
5. Connect the observed actions under the declared bearer and formulate the smallest supported collective-state claim. Keep its causal explanation distinct; a supported routine or command may explain that state.
6. When an attempted export carries the claim, state its fidelity criterion and loss. Otherwise retain the supported local reading.
7. State the supported use and any material limitation. Name another subject question only when it remains needed.
8. Add `B.3` assurance only when a named assurance claim is current; `QLP-3` requires that claim and a `B.3` assurance result for the target claim and receiving use. Consequence level, audit, release, or accountability use may also impose a direct domain requirement for that claim.

Return the supported distributed-state reading and its necessary qualifications, or the gap that prevents it. A useful result may preserve only observations or a narrower trace-population claim when collective-system identity or coordinated organization remains unestablished.

For an adequately supported positive case:

> During incident window W, the incident-response organization acted consistently with rollback-readiness posture P, evidenced by deployment queue changes, escalation messages, rollback artifacts, and support-routing changes; this reading is not faithfully exported by survey S because S loses timing, role-work, and trace linkage.

That sentence is narrower than "the organization decided". It supports adjusting incident communication and release-triage posture during window W; it does not support a durable culture claim or release-readiness assurance claim.

#### C.26.2:4.8 - Well-formed EDSE record

When a record is useful, the following shape can carry the account. Optional fields are included only for a claim or action that consumes them.

```text
EnactedDistributedStateEvidence(
  collectiveBearer = ...,
  boundary = ...,
  observedCoordinatedWork = ...,
  evidenceCarriers = ...,
  probeOrExport? = ...,
  timeWindow = ...,
  persistenceSupport? = ...,
  ordinaryRivals? = ...,
  explanationBasis? = ...,
  unresolvedInterpretation? = ...,
  exportLoss? = ...,
  minimalSupportedClaim = ...,
  boundedActionSupported = ...,
  unsupportedUse? = ...
)
```

The syntax is illustrative. A decision-use record retains the distinctions on which its supported claim or action depends. For an explicitly momentary, local use, follow :4.11 and omit persistence, decay, or reprobe-cost detail when those values cannot change the claim or action.

Well-formedness constraints:

- `collectiveBearer` is a declared collective system, not a metaphorical subject.
- `evidenceCarriers` make the relevant work inspectable through observations, traces, logs, commitment records or other work-result records; the claimed occurrence is not identified with its record.
- `timeWindow` bounds the claim; persistence beyond that window needs its own support.
- `ordinaryRivals`, when needed, contain serious alternatives that change the current reading.
- `minimalSupportedClaim` states the collective pattern established by the observations and relations. A causal explanation is an additional claim with its own grounds.
- `unsupportedUse`, when needed, identifies a live use that exceeds those grounds.

#### C.26.2:4.9 - Carrier, probe, report, and state split

The pattern keeps four objects separate:

| Object | Role in the claim |
| --- | --- |
| Enacted work | What people, service-providing systems, or market participants did in coordination, including routine enactment and artifact use. |
| Evidence carrier | The log, trace, ticket, meeting note, deployment record, dashboard export, report, API response, or policy text that makes some part of the work inspectable. |
| Probe / approximation | The survey, dashboard query, interview, trace query, report request, metric, or publication act that frames the state reading. |
| Distributed-state reading | The minimal `U.Episteme` claim inferred from coordinated work or behavior under carriers, window, rivals, and export limits. |

A survey operation probes; its response records carry outputs. A policy claim can explain an observed routine, while a publication of that policy carries its text. A dashboard can display evidence and act as an instrument in a behavior-changing probe. In each case, recover the operation, content and carrier used; none is automatically a faithful representation of the collective state.

#### C.26.2:4.10 - Case bank and near misses

| Case | Supported C.26.2 reading | Near miss or neighboring-pattern handoff |
| --- | --- | --- |
| Incident release freeze | Teams stop releases, prepare rollback evidence, redirect support work and change escalation. | A clear command can explain the freeze. It changes what may be inferred about spontaneous agreement, not whether the observed freeze occurred. |
| Service-mesh throttling regime | Route changes, saturation traces, retry patterns and on-call routines show a coordinated throttling state under policy P. | A controller rule may adequately explain the same state; reuse that account when it answers the receiving question. |
| Market expectation shift | Pricing, support inquiries, partner messages and risk notes move together after a public signal. | A shared stimulus can account for parallel movement without establishing changed expectations or coordination among participants. Preserve only the supported claim and the bearer's established kind. |
| Team "already decided" posture | Backlog changes, review comments, and role assignments show that the team is acting under an unstated decision. | If the claim is only a vibe or a few statements, do not use EDSE; gather carriers or keep it as informal observation. |
| Survey of culture | Survey answers conflict, but work traces show a stable escalation habit. | Treat the survey as a probe and state any export loss in its answers; do not make those answers the state itself. |
| Dashboard-following organization | Teams coordinate around the public metric after it becomes visible. | The induced pattern can still be an enacted-state claim. Use `C.26.1` when the metric's output is being taken to describe an unaffected state. |

#### C.26.2:4.11 - Evidence posture and confidence

EDSE claims become useful when the text says how much consequence the evidence can carry.

| Evidence posture | Admissible use | Additional support requirement |
| --- | --- | --- |
| `QLP-0` recognition | Flag a possible enacted state for discussion or triage. | Name bearer, work, carriers, and time window. |
| `QLP-1` local working use | Adjust local planning, incident response, or communication. | Retain live alternatives, export loss, persistence and reprobe conditions only where they change that use. |
| `QLP-2` decision-bearing use | Use the distributed-state reading for a named decision whose answer needs more than the current local account. | Retain the needed case comparison, live rivals, near misses, and evidence-carrier distinctions; reuse adequate existing contributions. |
| `QLP-3` assurance use | Answer a named assurance question about the distributed-state reading, its empirical adequacy, or comparative advantage. | Apply A.10 for evidence provenance and bounded reliance and B.3 for that assurance claim and receiving use. Apply C.16 only if measurement is claimed, and keep authority or work requirements with their direct patterns. Reuse adequate existing support and its limits. |

Publication or reuse under unchanged assumptions does not by itself raise the evidence posture. Select additional support from the receiving conclusion under C.26:12b.

For a momentary claim, name the bearer, observations or carriers, window and minimal supported reading. Add the temporal, alternative or export detail that changes the receiving action; local use, reuse or a fuller form alone does not create that need.

The ordinary EDSE claim is minimal but actionable. It says: "this coordinated work or behavior supports this bounded reading for this use."

### C.26.2:5 - Archetypal Grounding

Tell: In a constructed incident case, the independently identified incident-response System includes Release, Support and Operations teams. Between 14:00 and 14:30, their deployment logs show non-critical releases held, support-routing records show incident traffic redirected, and rollback artifacts are prepared. No written freeze decision is found for that interval. Later survey answers about whether "we had decided to freeze release" conflict.

Show, System side: the bearer is that incident-response System during the stated half-hour. Preparing rollback and changing support routing are observed work; logs, messages and artifact records make those actions inspectable. The observations are not replaced by the later survey.

Show, Episteme side: the System acted consistently with a release-freeze readiness posture during 14:00–14:30. Report those coordinated actions in incident communication instead of reporting a unanimous freeze decision.

An unwritten directive, playbook, shared alarm or dashboard effect remains a rival explanation; the case does not establish a separate causal mechanism. If a playbook fully explains the actions needed by the receiving use, retain that ordinary account.

If a next-day plan relies on the posture persisting, obtain the additional support for that later window. The half-hour reading supplies neither persistence nor release-readiness assurance.

### C.26.2:6 - Bias-Annotation

This pattern biases authors toward minimal evidence-bound claims and explicit evidence. This makes distributed-state language usable.

It also biases authors to keep primary grounding in distributed cognition, team cognition, organizational routines, socio-technical work, and evidence practice. The QL lens is secondary and additionally requires C.26's contextual-model obstruction test; ordinary export loss or changed probing alone is insufficient.

### C.26.2:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.2.1 | The collective bearer is a declared `U.System` or collective system, not a bare group label. |
| CC-C26.2.2 | Observed coordinated work, behavior, and trace pattern is named. |
| CC-C26.2.3 | Evidence carriers and time window are named. |
| CC-C26.2.4 | The QL cue / formal cue is named if QL wording is retained. |
| CC-C26.2.5 | Persistence, decay/refresh conditions and reprobe cost are retained when the claim or receiving action depends on them. |
| CC-C26.2.6 | The minimal supported claim is stated. |
| CC-C26.2.7 | Serious alternative readings are considered when they change the claim or its use; no rival is invented merely to fill a field. |
| CC-C26.2.8 | A load-bearing collective reading states the local observations and relations supporting the pattern. Its causal explanation is separately qualified and need not leave an unexplained residue. |
| CC-C26.2.9 | Any survey, dashboard, report, API response, or policy sentence is typed as representation, carrier, or export, not as the distributed state itself. |
| CC-C26.2.10 | Probe / measurement approximation, attempted export, faithful-enough criterion, loss cause, and higher-fidelity export possibility are stated when export or measurement carries the claim. |
| CC-C26.2.11 | Export loss is stated when the claim depends on export that is not faithful enough for the declared use. |
| CC-C26.2.12 | The evidence and uncertainty qualifications needed by the receiving claim remain recoverable. |
| CC-C26.2.13 | Formal measurement uses `C.16`; a needed replayable source-to-use account uses `A.10`; a named assurance claim uses `B.3`. `QLP-3` retains the B.3 result for that target claim and use. A cross-context sense Bridge uses `F.9`. |
| CC-C26.2.14 | QL use inherits the separate C.26 activation condition and `QL-NQ`. |

### C.26.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Group mind claim | The text says the team, market, service, or organization knows or wants something without evidence for that claim. | Rewrite as an evidence-bound state reading over a collective bearer during a window. |
| Survey-as-state | A survey answer is treated as the distributed state. | Treat the answer as a probe result or other emitted output that can serve as an evidence carrier, and ask what the probe changed or the output lost. |
| Tacit skill overreach | A tacit skill or team vibe is called distributed state. | Recover the coordinated work, its evidence and window, and any serious alternative that changes the proposed claim. |
| Routine overread | Enactment of a playbook is used to infer unspoken agreement or durable culture. | Keep the supported current-state and routine claims; the stronger interpretation needs its own grounds. |
| Timeless culture | A momentary observation becomes a durable culture claim. | State window, persistence support, decay, and reprobe condition. |

### C.26.2:9 - Consequences

This pattern lets FPF discuss enacted collective states. It gives authors a way to use traces, routines, coordinated work, and export loss in one minimal claim.

The cost is that many claims become narrower. Minimal evidence-bound claims are often more useful than confidently asserted claims that lack support.

### C.26.2:10 - Rationale

Existing FPF patterns can carry parts of the support requirement, but no single ordinary pattern makes the combined minimal distributed-state claim easy to write. `A.15` carries Work alignment, `A.10` carries source-to-use evidence accounts, `B.3` carries named assurance claims, `F.9` carries cross-context semantic Bridge loss, and `C.16` carries formal measurement. C.26.2 coordinates those neighboring-pattern applications for the specific case where coordinated work evidences a non-articulated state.

### C.26.2:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Coordinated work can evidence state-like organization without reducing that state to one participant report. | [Representing distributed cognition in socio-technical systems](https://www.sciencedirect.com/science/article/abs/pii/S2405896316321164), team cognition, shared mental models, transactive memory, [organizational routine dynamics resources](https://routines.broad.msu.edu/resources), work traces, and socio-technical systems. | Make these the primary grounding; infer only minimal evidence-bound state readings from carriers, traces, and work. | Adapt as primary non-QL grounding. |
| Probe/export conditions can change or thin the state reading. | [Quantum-like modeling in biology with open quantum systems and instruments](https://www.sciencedirect.com/science/article/pii/S0303264720301994) / [arXiv](https://arxiv.org/abs/2010.15573) and [Open Systems, Quantum Probability, and Logic for Quantum-like Modeling in Biology, Cognition, and Decision-Making](https://www.mdpi.com/1099-4300/25/6/886). | Examine the probe/export effect under its ordinary subject account; retain QL only when C.26's separate obstruction test is met. | Adapt as secondary modeling support. |
| Contextual judgment and previous judgments can alter the state being reported. | [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501). | Treat surveys, interviews, reports, and dashboards as possible probes of enacted state, not faithful copies by default. | Use as probe/export caution with ordinary evidence routes. |
| Some sequential data can be carried by classical instrument models. | [Quantum-like Cognition in Process Theories: An Analysis](https://arxiv.org/abs/2604.08604). | EDSE is a useful FPF evidence pattern; it does not establish that only QL formalism works. | Use as rival-model discipline. |
| Carrier plurality is normal in operational evidence. | Observability, incident-management, audit, work-trace, and assurance practice. | Use logs, trace records, dashboard outputs, meeting notes, commitment records and other artifacts as evidence of work and operational changes; recover what their content supports about the collective state. | Adopt through `A.10` evidence-provenance accounts and `B.3` when a named assurance claim is current. |

Apply these source contributions:

- ground the claim in coordinated work before QL vocabulary appears;
- state the evidence carriers and time window before stating the state reading;
- examine alternatives where they change the state claim or receiving use;
- treat survey/report/dashboard outputs as carriers or as instruments of a stated probe, not as the state;
- escalate to measurement, evidence, assurance, or authority patterns when the use requires measurement, evidence, assurance, or authority support.

### C.26.2:12 - Relations

- Builds on: `C.26`, `A.15`, `A.10`, `B.3`, `F.9`, `C.16`, `E.17.EFP`, `C.11`.
- Coordinates with: `C.26.1` when the probe changes the state being evidenced and its output is being used as a passive read; `C.26.3` when the coordinated state is part of viability-envelope regulation.
- The distributed-state reading concerns the declared collective bearer and remains bounded by its supporting observations and time window.

### C.26.2:End
