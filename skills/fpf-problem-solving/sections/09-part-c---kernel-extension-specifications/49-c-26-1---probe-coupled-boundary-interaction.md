## C.26.1 - Probe-Coupled Boundary Interaction

> Type: Architectural pattern
> Status: Stable
> Normativity: Normative unless marked informative

### C.26.1:1 - Problem frame

Use this pattern when a boundary read, meeting, metric, API read, dashboard, workshop, survey or message is used as evidence of state, and a possible effect of that interaction on the reported state could change the decision. Recover which state the output supports before deciding whether the read is passive, probe-coupled, or unresolved.

The useful move is to recover what the interaction read, what it changed and which state its output can support. That ordinary result can finish the use. Add QL only under the separate C.26 activation test.

| Working surface | Value |
| --- | --- |
| Primary reader | Architect, platform lead, domain modeler, or manager judging a boundary read, workshop, dashboard, metric, API read, or bridge result. |
| Boundary interaction under concern | A boundary interaction being used as evidence, export, comparison, or decision input. |
| Boundary-interaction decision use | Establish which state and time the output supports, correct a false passive-read or lossless-transfer inference, and redesign or use a neighboring method when needed. |
| Outside work | Ordinary message passing, causal intervention, API semantics or Bridge loss whose output interpretation is already adequate for the receiving use. |
| What changes in practice | The team traces how and when the output was produced and retains only the state claim that the procedure and evidence support. |

Plain glosses:
- `passive read`: treating a workshop, metric, dashboard, API read, survey, or message as if it only reports state.
- `probe-coupled`: the read/export/intervention participates in the represented state enough to change the lawful decision.
- `coupling channel`: the concrete workshop, metric, message, API, dashboard, meeting, bridge, or event stream through which the effect travels.
- `export loss`: what the carried output cannot faithfully carry into another context or decision.

### C.26.1:2 - Problem

Architecture work often treats boundary interactions as passive. A dashboard "shows readiness". A workshop "discovers the context map". An API read "returns state". A meeting "collects alignment". A message "transfers a decision".

Sometimes that is good enough. Sometimes it is false for the current decision. Publishing the dashboard changes readiness behavior. Running the workshop changes alignment and local meaning. Reading the API changes timing assumptions. Sending the message changes trust, escalation, or error handling. Splitting the service changes the viability envelope that the split was meant to optimize.

When the false passive reading survives, the team may keep the wrong boundary, trust the wrong export, combine incomparable outputs, or redesign the system around an artifact that partly created what it reports.

### C.26.1:3 - Forces

| Force | Tension |
| --- | --- |
| Boundary discipline vs probe sensitivity | `A.6` and `F.9` already govern boundaries and bridges; this pattern adds only a probe-coupled reading of the state-changing or export-changing interaction. |
| Intervention vs readout | An action can intentionally change the world. This pattern examines what its output establishes about the state before, during or after that action; QL needs the additional C.26 activation condition. |
| Lean use vs evidence-support class | A short explanation can support local recognition. A release, audit or measurement claim needs the evidence and subject account on which that use relies. |
| Coupling words vs relation tokens | Words such as coupling, interaction, and export can remain local explanatory wording. A reusable name under `F.18` designates an already settled relation; use `A.6.P` when the relation or participants remain unclear. |

### C.26.1:4 - Solution

Examine how the interaction produced the output and whether its effects matter to the state claim being used. A supported passive reading can finish the inquiry. A supported probe effect calls for a qualified reading; insufficient information leaves that interpretation unresolved.

A probe-coupled interaction may be useful and intentionally state-shaping. Its output may still report a pre-probe quantity accurately. The relevant question is which quantity was read, at what point in the interaction, and how the result is used.

Start with these recognition questions; ordinary prose is sufficient when it preserves their answers.

| Mini-entry | Question |
| --- | --- |
| Ordinary governing pattern | Which ordinary FPF pattern already carries the baseline boundary, bridge, measurement, work, or viability question? |
| Reading to examine | What state, time and conditions is the output being taken to report? |
| Possible probe effect | Which operation could change that state or the meaning of the output before, during or after the read? |
| Practical change | Does the recovered procedure support the intended reading, require qualification or redesign, or leave an action-changing question unresolved? |
| Remaining question, if any | What needed claim remains unsupported, and which subject method can supply its missing grounds? |

Use the fuller account below when the receiving decision or a substantive dispute needs distinctions missing from the recognition note. Reuse an already adequate account; publication or reuse alone does not require a new record.

Distinctions for a fuller decision-bearing account:

| Field | Question |
| --- | --- |
| Boundary | Which boundary or interface is involved, and which direct relation, if any, is crossed or queried? Identify each under its applicable subject pattern. |
| Probe or interaction | Which operation or interaction produces the output, using which instrument or channel? |
| QL cue or formal cue | If QL is retained, which named contextual-model obstruction meets C.26's activation test? An ordinary probe effect can be handled without this field. |
| Reading to examine | What passive-read or lossless-transfer assumption does the receiving use make? |
| Pre-probe state or hypothesis, when needed | What is known or assumed about the state before the interaction? |
| State at and after the read | Which state did the output measure or describe, and what changed during or after its production? Preserve uncertainty where the sequence or effect is unknown. |
| Update class, if load-bearing | Is the update a system change, work change, epistemic reading update, carrier update, emitted-output update, formal model update, or update-law change? |
| State-change evidence | Which traces, changed decisions, changed labels, changed priorities, behavior shifts, timing changes, or export failures support the state-change reading? |
| Uncertainty / confidence posture | What remains inferred, approximate, disputed, probe-dependent, or not yet distinguishable? |
| State history / memory, if load-bearing | State this only when path dependence, order effect, hysteresis, or retained trace changes the current lawful reading. |
| Decision | What changes now: mark probe-coupled, redesign probe, order, or frame, add evidence, rewrite bridge or export, split, merge, orchestrate differently, or apply a neighboring FPF pattern? |
| Decoupling / redesign option | Can the probe, order, frame, bridge, metric, dashboard, API read, or boundary interaction be redesigned so the needed output is less state-changing or more faithfully exportable? |

#### C.26.1:4.1 - Activation boundary

Use this pattern while a possible state-changing interaction leaves an unresolved question about the interpretation of its output. A positive probe-coupled claim needs grounds for the relevant effect; suspicion alone does not establish it.

A meeting that changes attention may still accurately report a fact observed before discussion. A mutating API operation can return the old or the new value according to its interface semantics. Identify that timing and meaning before treating either output as a false passive read.

Performative-prediction analysis can explain behavior changed by a deployed prediction, score or metric. Use that account directly, with `C.16` for measurement, `A.10` for source recovery and bounded reliance, and `B.3` for a named assurance claim. C.26.1 can connect the supported probe effect to the corrected use of its output without QL; use it only while that question remains unresolved.

#### C.26.1:4.2 - Finish conditions

The pattern emits one of these results:

| Result | Meaning |
| --- | --- |
| Supported passive or time-qualified read | The procedure and evidence support the stated quantity at the stated time, including when a later probe effect leaves that reading intact. |
| Unresolved interpretation | Name the missing operation, timing or effect premise and restrict only the conclusion that depends on it. |
| Keep boundary, mark probe-coupled | The boundary remains, but the output is interpreted with its supported probe effect. |
| Redesign probe/order/frame | Change the workshop, dashboard, API read, survey, metric or question order when that would supply the needed reading with less distortion. |
| Redesign bridge/export | Preserve the state, timing and use conditions lost by the attempted export; state confidence or a return-to-source condition when the receiving use needs it. |
| Split/merge/orchestrate differently | Boundary structure changes because the interaction changes the phenomenon. |
| Apply `F.9` | Only bridge and loss remain live. |
| Apply `C.16` | The probe is a standard measurement with declared scale, method, evidence, and result. |
| Apply `A.15` | The question concerns work enactment rather than probe-coupled reading. |
| Apply `C.26.3` | Viability-envelope regulation is primary. |

#### C.26.1:4.3 - Probe-coupled context-cut worked use slice

The following constructed case shows a DDD workshop that changes the meaning and use of its own result.

Ask whether the bounded-context cut was only discovered or whether the interaction changed alignment, ownership, vocabulary, export validity, or viability. Examine the workshop, dashboard use, API extraction, bridge use, split, merge, or orchestration involved.

| Slice field | Example content |
| --- | --- |
| Case | A product organization considers splitting payment handling out of a checkout bounded context after repeated payment-failure incidents. |
| Ordinary DDD finding | Checkout and Payment use different local meanings for `Order.status`, `PaymentFailure`, and `Retryable`; an ordinary `F.9` bridge is needed. |
| Probe / intervention | The event-storming workshop starts from payment-failure dashboards and asks teams to place incidents by owner, customer impact, and recovery path. |
| Post-probe reading | Product, Support, and Payment start treating payment failure as a customer-risk gate, not only a technical retry condition. |
| Evidence | Incident labels are reclassified, escalation changes, backlog priority changes, and the dashboard query is rewritten. |
| Export loss | Copying `PaymentFailure = customer risk` into both contexts loses the difference between retryable technical failure, promise breach, and support escalation trigger. |
| Decision output | Treat the workshop result as evidence of the post-workshop reading; recover the separate local senses and their `F.9` correspondence/loss before export. Assess the proposed split and escalation promise under their ordinary design and authority grounds; the probe effect alone does not select or authorize them. |

#### C.26.1:4.4 - Boundary interaction under concern and operational sequence

The boundary interaction under concern is used as evidence, export, comparison input or architecture decision input. Identify the concrete operation, any instrument or channel it uses, and the output being interpreted.

The useful result is a supported reading of that output, a corrected use, or the unresolved premise. A redesign is a further result only when it is needed and justified.

Operational sequence:

1. State the quantity or condition the receiving decision needs, its bearer and relevant time. Locate the output in the procedure, interface description, question sequence or available trace.
2. Reconstruct the order of operations that can affect that quantity: preparation, sampling or questioning, state changes, output construction and later use. Read interface contracts, query definitions, timestamps, question wording or observed actions for those steps. Keep an unavailable step explicit rather than filling it with an assumed passive read.
3. Trace a plausible effect from the operation to the reported quantity. For example, a query may populate a cache, publishing a score may change what people report, or discussion may change the agreement later summarized. Use existing mechanism or causal grounds; `C.28.CM` can develop an unresolved causal account. Temporal succession alone does not establish the effect.
4. Determine whether the output concerns the state before, during or after that effect. Compare the intended interpretation with the procedure and observations. An operation that changes later state does not automatically invalidate an earlier reading. Distinguish an actual change in the subject from a changed label, carrier or interpretation.
5. Retain only effects, export losses, order, memory or frame conditions that change the current use. If material alternatives remain, seek the existing trace or procedural fact that distinguishes them. A new comparison or probe is warranted only when its attainable result could change the receiving action enough to justify its cost. If the needed distinction cannot be made, state the unresolved interpretation and its consequence.
6. Return the supported reading and choose any needed continuation: qualify the output, redesign the probe or export, change the boundary arrangement, or use the subject method for the remaining question. A sufficient reading finishes here.

For example, suppose an API request measures a cold-cache response and then fills the cache. The first response time can still support a cold-cache claim; a later response time cannot be used as that same cold-cache observation without further grounds.

Recover the cache initialization, write point and measured interval from the procedure or trace. When those are unavailable, the unresolved point is which cache regime the timing represents.

#### C.26.1:4.5 - Well-formed probe-coupled boundary state

A positive probe-coupled claim identifies the interaction, the relevant state or output meaning it changes, the grounds for that effect, and the consequence for the intended reading. Include the boundary, instrument, carrier, state history and confidence qualification when they carry that claim. A before/after reconstruction may be partial; do not turn missing information into an asserted change.

A useful result remains incomplete when the receiving use still depends on an unexplained output-producing step, an unsupported effect or a lost condition. State that specific gap. Evidence, command, measurement and semantic correspondence retain their distinct relations when more than one is used.

A minimal supported result may be:

- "this dashboard value evidences readiness behavior while the displayed score is used to allocate staffing";
- "the workshop changed agreement, so its closing note is evidence of the resulting alignment";
- "this API response contains the value sampled before the write."

Add a limit or further route only for a live unsupported use.

#### C.26.1:4.6 - Probe, observable, output, and carrier split

Distinguish what is being read from the method used to read it, the resulting output, and the output carrier.

| Role | Boundary-facing question |
| --- | --- |
| Observable or output dimension | What readiness, status, alignment, failure, response, risk, split, promise, or boundary condition is being read? |
| Probe method | How is the dashboard, API read, workshop order, survey, canary, incident review, event stream, or meeting format used to probe the situation? |
| Measurement / interaction scheme | What timing, threshold, sampling rule, question order, aggregation, publication path, or access path shapes the output? |
| Output or result record | What score, label, context map, API response, survey answer, incident class, readiness status, or bridge field was emitted? |
| State update | What behavior, alignment, meaning, trust, priority, escalation, or timing changed because of the probe? |
| Evidence carrier | Which log, dashboard export, meeting note, trace, decision record, ticket history, context map, or API result carries the output? |

This split prevents a common mistake: "the dashboard says ready" hides at least four objects. The dashboard definition, the displayed result, the behavior it changes, and the readiness decision are distinct.

#### C.26.1:4.7 - Reroute and disambiguation guide

Use this guide when a draft says that a boundary, system, team, or service is "coupled", "aligned", "interacting", "measured", "exported", "synchronized", or "read".

| Trigger surface | Question that changes use | Supported effect | No relevant effect established |
| --- | --- | --- | --- |
| "The dashboard shows readiness." | Did publishing or using the score change the behavior that this output is taken to report? | Qualify the readiness claim using the supported effect and timing. | Use an adequate reporting or measurement account; if the effect remains material and unknown, retain that uncertainty. |
| "The workshop discovered the boundary." | Did discussion change the local meaning, ownership or agreement described by the final map? | Distinguish the resulting arrangement from the pre-workshop arrangement; add `F.9` only for an actual cross-context sense correspondence. | Use the supported domain account, or state which step or effect remains unknown. |
| "The API read returns state." | What value is sampled relative to cache updates, mutations and response construction? | Interpret the output at that point in the sequence; redesign if the needed state is not recoverable. | Use adequate interface semantics, measurement or freshness grounds; do not infer a pre-state or post-state value from the verb "read" alone. |
| "The message transferred the decision." | Did transmission or reception change the authority, trust, timing or meaning needed by this use? | Qualify the carried claim and use the applicable work or authority method. | Keep the supported transfer; identify any unresolved relation needed by the receiving use. |
| "The split improved viability." | Does the evaluation depend on a change caused by the split or by the observation procedure? | Use `C.26.3` for the envelope and the probe account for the affected observation. | Use an adequate boundary or quality account, retaining a material unknown where necessary. |

Use the direct relation pattern when the relation and participants are known, `A.6.P` when their meaning remains unclear, and `F.18` when the settled relation needs a reusable name.

#### C.26.1:4.8 - Positive examples and near misses

| Case | Supported C.26.1 use | Near miss and neighboring-pattern handoff |
| --- | --- | --- |
| Readiness dashboard | The readiness score changes team behavior: teams stop surfacing borderline failures because the dashboard is watched by release management. The score is probe-coupled evidence, not a passive readiness copy. | If the dashboard only reports a well-defined measure with no behavior-changing or frame-changing effect, use `C.16` and the direct pattern for any evidence claim that is current. |
| API consistency check | A request warms the cache and changes later latency. Recover whether each timing was measured before or after warming; a later warm-cache result cannot by itself establish cold-cache performance. | If the interface and measured interval already settle that question, use the adequate API and measurement account directly. |
| Survey order | Asking "who owns incidents?" before "which context owns payment failure?" changes the resulting context map and escalation plan. | If different answers merely reveal unresolved meanings, use `F.9` / `A.6.P` first. |
| Event-storming workshop | The workshop produces a map and also changes team alignment, local vocabulary, and backlog priority. | If it only documents known differences, use ordinary DDD and bridge fields. |
| Service split | Splitting Checkout and Payment changes recovery paths and support load, so the split is part of the phenomenon being evaluated. | If the split only reduces deployment coupling with no probe/export effect, use ordinary boundary and quality patterns. |
| Incident metric | Publishing "cache failover is the primary risk" shifts attention, staffing, and reproduction work. | If the metric is only a report of already-carried evidence, use `A.10` for any source-recovery or bounded-reliance question, and `B.3` only for a named assurance claim. |

The positive examples establish probe-coupled interaction readings. Use those results without QL wording when the ordinary subject patterns carry the case. Retain QL only when the additional C.26 activation test establishes one named contextual-model obstruction that survives those patterns and changes the admissible inference or action.

#### C.26.1:4.9 - Evidence posture for probe-coupled claims

Use the least-committing evidence posture that still supports the intended use.

| Evidence posture | Admissible use | Typical support |
| --- | --- | --- |
| `QLP-0` recognition | Flag a likely probe-coupled situation for local discussion. | Meeting note, dashboard screenshot, issue comment, context-map draft. |
| `QLP-1` local working use | Change a local probe/order/frame, bridge note, or boundary decision in a team setting. | Before/after labels, changed tickets, changed dashboard query, changed escalation path, changed architecture note. |
| `QLP-2` decision-bearing use | Use a probe-coupled reading for a named boundary, probe, export, or other decision whose answer needs more than the current local account. | The action-changing rival explanations, declared loss and receiving-use limits, and observations or comparisons that this decision consumes; reuse adequate existing contributions. |
| `QLP-3` assurance use | Answer a named assurance question about the probe-coupled claim, its empirical adequacy, or comparative advantage. | The applicable A.10 and B.3 support for that conclusion, with C.16 measurement or a Bridge/loss account only where the conclusion relies on it; retain adequate existing support and its limits. |

Recognition or local working use may remain at `QLP-0` or `QLP-1` when its account is sufficient. Select additional support from the receiving conclusion under C.26:12b; publication, reuse, or formal wording alone does not require escalation or recollection of adequate evidence.

### C.26.1:5 - Archetypal Grounding

A team runs a service-boundary workshop after a series of incidents. The first map says "Payments is separate from Checkout". A week later, incident triage and backlog priorities have changed because the workshop reframed payment failure as a customer-promise risk.

System side: the teams, services, dashboards, event stream, workshop format, and escalation routine are part of the boundary situation. The workshop changes alignment and future work; its notes and resulting map carry the recorded output.

Episteme side: the minimal evidence-bound claim is "the workshop work functioned as a probe lane that changed the represented boundary state and exposed export loss across Checkout and Payment." Use that account to assess a boundary or probe decision and the needed `F.9` correspondence; it does not by itself establish that the split is desirable or authorized.

### C.26.1:6 - Bias-Annotation

This pattern biases authors toward examining how an interaction affects the interpretation of its output. That bias is useful when dashboards, workshops, surveys, and API reads are treated as if they carry state without changing it.

The pattern also biases authors against overusing QL. When no probe-coupled reading remains, the ordinary questions of intervention, message passing, bridge loss, API semantics, and work enactment stay with their existing FPF patterns.

### C.26.1:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.1.1 | The boundary, role relation, authority relation, bridge, split, or queried system edge is named. |
| CC-C26.1.2 | Identify the probe operation or interaction separately from its Method, instrument/channel and output carrier when those distinctions carry the claim. Quantum-instrument wording remains a modeling analogy unless supported by a formal account. |
| CC-C26.1.3 | Observable, probe method, measurement scheme or interaction scheme, emitted output or result record, update class, and evidence carrier are separated when they carry the claim. |
| CC-C26.1.4 | The QL cue or formal cue is named, or the case is handled without QL wording. |
| CC-C26.1.5 | The state, timing and output interpretation needed by the receiving use are stated. |
| CC-C26.1.6 | The relevant output-producing sequence is recovered; pre-probe, read-time and post-probe states are distinguished where needed, with missing information preserved. |
| CC-C26.1.7 | A claimed probe effect has support, and material uncertainty is retained. |
| CC-C26.1.8 | State history, memory, path dependence or order/frame sensitivity is stated when load-bearing. |
| CC-C26.1.9 | The result distinguishes a supported passive reading, a supported probe effect and an unresolved interpretation; only the positive effect claim asserts a change caused by the interaction. |
| CC-C26.1.10 | The output is one of the pattern finish conditions. |
| CC-C26.1.11 | The decoupling, probe-redesign, order-redesign, frame-redesign, bridge-redesign, or boundary-redesign option is stated when it could reduce the problem. |
| CC-C26.1.12 | The receiving claim retains the evidence and uncertainty qualifications it needs; reuse of an adequate account alone requires no additional posture record. |
| CC-C26.1.13 | Ordinary intervention, bridge, work, measurement, and viability routes are tried before QL wording is retained. |
| CC-C26.1.14 | Coupling or interaction wording becomes a reusable relation name under `F.18` only after the relation and participants are settled under their direct pattern; `A.6.P` is used when their meaning remains unclear. |
| CC-C26.1.15 | The pattern inherits `QL-NQ` from `C.26` instead of restating the inherited boundary as local law. |

### C.26.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Every interaction is QL | Any message, meeting, or API call is called probe-coupled or QL. | Examine a material question about what the interaction's output supports; require grounds for a positive probe effect and the separate C.26 activation test for QL. |
| Causal action mistaken for probe | A deployment or command changes the world, and QL is invoked. | Use intervention or work-governing patterns unless the action is being used as a readout of the state it changes. |
| Bridge loss alone | Export loses local meaning, but no state-changing probe is live. | Use `F.9` with loss notes. |
| Context-word drift | *Context* hides source-local meaning, a selected model-use organization, ClaimScope, a probe frame, or a measurement setup. | Name what *context* denotes here. Retain *bounded context* only when using the established DDD term. |
| Relation token leakage | `coupledBy(...)` appears as if already ratified. | Keep it as local drafting form; recover the relation and participants through `A.6.P` when unclear, and use `F.18` only for a reusable name of the settled relation. |

### C.26.1:9 - Consequences

This pattern corrects the interpretation used by a boundary decision. It turns "the workshop showed the split" into "the workshop both showed and changed the split-relevant state." It turns "the dashboard says ready" into "the dashboard is probe-coupled evidence with a limited decision use."

Dashboards, workshops, surveys, API reads and messages remain useful. A supported probe effect changes only the readings it affects; an unresolved effect limits the dependent conclusion.

### C.26.1:10 - Rationale

An output depends on the operation that produced it. When that operation also changes the represented state, the user must recover which state the output supports before using it in a decision. A supported ordinary account can establish that relation without QL.

Use this account while the interaction leaves a material uncertainty or error in the interpretation of its output. An already adequate subject account is sufficient.

### C.26.1:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| A probe or instrument can produce both an output and a state update; the output alone does not specify the operation. | [Quantum-instrument modeling of question order, response replicability, and QQ-equality](https://www.sciencedirect.com/science/article/pii/S0022249620301152). | Ask what operation produced both output and update before treating dashboards, API reads, workshops, surveys, or metrics as passive reads. | Adapt the instrument/update lesson. |
| Contextual judgment and order effects are common enough to be a practical modeling cue. | [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501). | Treat question order, workshop order, and dashboard framing as possible state-shaping operations when they change the decision. | Adopt as a recognition cue. |
| Classical instrument models may explain some sequential-decision data, so QL is useful but not uniquely necessary by default. | [Quantum-like Cognition in Process Theories: An Analysis](https://arxiv.org/abs/2604.08604). | Keep rival routes visible; QL remains a modeling lens, not a necessity claim. | Use as non-exclusivity discipline. |
| A prediction, score, or metric can change the target distribution because people act on it, without requiring a QL probe reading. | [Performative Prediction](https://proceedings.mlr.press/v119/perdomo20a.html). | Use the performative-prediction account to explain dashboard-induced or score-induced behavior. Apply C.26.1 when the output still needs a corrected state/use interpretation; add QL only under C.26's separate activation test. | Adopt as a classical rival path that sharpens when C.26.1 is useful. |
| Boundaries can be modeled by what a system can measure, model, and affect, while mathematical boundary descriptions are not new worldly substances. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Make the boundary/probe relation explicit without reifying the boundary or coupling phrase. | Adapt for boundary-function discipline. |
| Bounded-context and microservice practice already governs ordinary domain cuts and integration points. | [Use domain analysis to model microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) and [DDD in software development: a 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Use C.26.1 only when the cut, workshop, bridge, dashboard, API extraction, split, or merge changes represented boundary state or export validity. | Use DDD as baseline; add C.26.1 only for the probe-coupled support load. |

Apply these source contributions:

- start from the ordinary FPF pattern before QL wording;
- show the concrete operation that produced the output;
- show the supported state update or export loss that changes the decision, or the unresolved premise;
- keep relation wording local; use `A.6.P` for unresolved relation meaning and `F.18` for a reusable name only after the relation is settled under its direct pattern;
- keep source-formalism language as modeling support, not as pattern-body ontology.

### C.26.1:12 - Relations

- Builds on: `C.26`, `A.6`, `A.6.B`, `A.6.P`, `F.9`, `A.15`, `C.16`, `A.10`, `B.3`, `C.25`, `A.1.1`.
- Coordinates with: `C.26.2` when coordinated work evidences a non-exportable distributed state; `C.26.3` when the boundary interaction changes a viability envelope.
- The worked context-cut case in `C.26.1:4.3` connects a workshop's effect to the corrected interpretation of its output.

### C.26.1:End
