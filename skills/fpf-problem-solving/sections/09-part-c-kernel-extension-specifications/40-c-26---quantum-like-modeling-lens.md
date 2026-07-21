## C.26 - Quantum-Like Modeling Lens

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.26:1 - Problem frame

FPF already has local patterns for decisions, boundaries, bridges, work, measurement, search, and quality bundles. Some real architecture cases still break when those patterns are applied as if every read, question, dashboard, workshop, bridge, or simplified representation were a passive view of a stable state.

Use this pattern when the ordinary FPF pattern remains active but misses one extra representational issue: the act of probing, framing, exporting, comparing, or coarsening changes what can admissibly be inferred from the represented state. The useful move is small. Add a quantum-like mathematical lens only where it tells the user how to avoid a concrete representational mistake.

**What goes wrong if missed.** A dashboard, workshop, metric, bridge, export, or coarsened model is treated as a passive faithful readout even when the probe, frame, publication, or representation shortcut changes what can be inferred.

**What this buys.** The user keeps the ordinary FPF pattern in charge and adds only the minimum quantum-like lens needed to prevent that concrete representational mistake.

This pattern is not a physics claim. In FPF, `quantum-like` names a detached mathematical and representational lens, comparable in role to probability, calculus, optimization, or state-space modeling. It is cheap as a QL-lite note and expensive only when the claim becomes reusable law, assurance evidence, empirical superiority, formal reconstruction, or ontology.

Unifying principle: use QL to cheapen the first correct move, not to make the first mention more expensive.

| Working view | Value |
| --- | --- |
| Primary reader | Architect, method author, steward, or manager deciding whether QL wording improves a concrete FPF representation. |
| Primary EntityOfConcern | A local use of quantum-like mathematical language in pattern prose or work guidance. |
| Admissible move | Admit, select another applicable pattern body, narrow, or escalate the QL wording by ordinary FPF pattern, QL cue, payoff, minimal admissible output, and local stop. |
| Outside work | Physical quantum claims, general ontology, ordinary uncertainty/complexity, ordinary DDD locality, ordinary compression, and search/regime generation. |
| What changes in practice | The writer stops asking "does quantum-like help here?" and asks "what representational mistake does this lens prevent here?" |

What this lens buys in practice:

| QL support | Practical gain |
| --- | --- |
| Probe-aware design | Design a workshop, dashboard, API read, survey, readiness check, or metric publication as a state-shaping interaction when it is not only a readout. |
| Comparison-frame discipline | Notice earlier that two options, scores, or judgments cannot be compared in one frame without a bridge, coupling, or declared joint-comparison route. |
| Export humility | Stop false cross-context substitution quickly: a carried value, report, or label may not export the same state for the intended use. |
| Low-recoverability distributed-state reading | Talk about team, organization, market, or service-mesh behavior without inventing a group mind and without reducing the state to one report. |
| Envelope-first viability | Move from "which single metric wins?" to a viability envelope with variables, sensors, actuators, costs, and failure modes. |
| Admissible coarsening use | Use a cheaper state representation when it helps, while keeping source, loss, admissible use, non-admissible use, and reopen condition visible. |

Plain glosses:
- `quantum-like`: a detached mathematical or representational lens, not a claim about what the target is made of.
- `probe`: an operation that both produces an output and may change the represented state or admissible use of the output.
- `frame`: a probe frame, measurement frame, comparison frame, or model frame. If the text means FPF semantic context, say `U.BoundedContext` or bounded context explicitly.
- `state`: the represented condition relevant to the current decision, not a generic new `U.State` kind.
- `state update`: a typed update claim. When load-bearing, say whether the update is a system change, work change, epistemic reading update, carrier update, emitted-output update, formal model update, or update-law change; do not let one phrase carry all of them.
- `context`: not a shorthand for frame. Use it only in explicit FPF terms such as `U.BoundedContext`, bounded context, or cross-context bridge.
- `export`: a carried representation whose use may lose timing, coordination, role, use conditions, confidence, or relation structure.
- `coarsening`: an intentionally cheaper state representation with declared loss and reopen conditions.

Phrase hygiene:

| Risky phrase | Better FPF phrase |
| --- | --- |
| Dashboard changed the state. | Dashboard publication or use changed work behavior or evidence conditions. |
| Metric acted as observer. | Measurement/publication regime functioned as a probe interaction. |
| Organization knows. | Coordinated work traces support a low-recoverability state reading over a declared collective bearer. |
| Market is entangled with product team. | Ordinary market, feedback, negotiation, and organizational-coupling routes fail; local reads or exports are not admissibly comparable or reusable without declaring the probe, frame, update, or export relation. |
| Boundary collapsed after workshop. | Workshop work selected or created a local boundary reading for this decision window. |
| State cannot be copied. | No faithful-enough export supports the intended cross-context use. |
| Same metric in two contexts. | Same-named result under different measurement or comparison frames. |
| Quantum-like service health. | Viability-envelope reading affected by probe, export, or coarsening cue. |

Example style:

| Style | Example |
| --- | --- |
| Bad | The team's quantum-like distributed state collapsed after the readiness dashboard observation. |
| Better | The readiness dashboard was not a passive read: its publication changed team behavior, so the dashboard result cannot be used alone as pre-publication readiness evidence. |
| Best | Apply `C.16` to ordinary metric issues and `B.3` to release assurance. Retain `C.26.1` only for the residual false passive-read issue: dashboard publication changed readiness behavior in window W. Decision diff: do not use the dashboard as sole release evidence; add independent work traces and record non-admissible use. |

Informative bilingual translation note:

| English | Prefer in Russian or bilingual use | Risk |
| --- | --- | --- |
| `probe` | probe / пробное воздействие / считывающее взаимодействие | "измерение" is too narrow; "зонд" sounds too physical. |
| `state reading` | чтение состояния / state-reading claim | "состояние" without reading sounds ontological. |
| `frame` | рамка сравнения, probe frame, or model frame | "контекст" can collide with bounded context. |
| `instrument` | instrument-like operation / операция-инструмент | "прибор" sounds too physical. |
| `distributed state` | distributed-state reading | "распределённое состояние" sounds like a new object. |
| `faithful-enough export` | достаточно верный перенос для заявленного use | "копия" suggests an impossible-copy ideal. |

### C.26:2 - Problem

Without this pattern, teams make five recurring mistakes.

They treat a probe as a neutral read when the probe changes later answers or behavior. They combine two posterior-looking outputs as if both came from one shared sample space. They export a team state, dashboard value, or context-map result as if it were a faithful-enough export for the intended use. They compress a large state representation for speed and then reuse the shortcut outside its admissible-use scope. They let words such as `quantum`, `entanglement`, `collapse`, or `field` import ontology that the model never earned.

The result is not merely loose wording. The team may approve a release from a dashboard whose publication and operational use changed the work it was supposed to report, average incompatible risk estimates, copy a local decision into another bounded context after the bridge lost the live coordination, or claim a speed gain because the representation was low-bit, linear, symbolic, or compressed without naming the loss.

### C.26:3 - Forces

| Force | Tension |
| --- | --- |
| Ordinary FPF patterns first | `C.11`, `A.6`, `F.9`, `A.15`, `C.25`, `C.16`, `A.10`, `B.3`, `C.18`, `C.19`, and `A.19` already do real work. QL wording must add only the remaining state, probe, or export cue. |
| Lightweight use vs claims requiring additional evidence | A local diagnostic note should be cheap; reusable guidance, assurance, physical claims, or superiority claims need heavier evidence and explicit neighboring-pattern selection. |
| Useful math vs misleading vocabulary | Quantum-like formalisms help with order, contextual probability, incompatible probes, instruments, and open information systems; popular quantum words easily overclaim. |
| Representation cost vs representation loss | A cheaper state representation may be the right engineering move, but only if the source, shortcut, loss, admissible use, and reopen condition stay visible. |
| Recognition vs assurance | Working readers need fast entry; the assurance section needs enough typed fields to prevent pattern-role theft, impossible-copy overread, and hidden ontology. |

### C.26:4 - Solution

Start with the ordinary FPF pattern. Add this lens only when ordinary wording would falsely treat a probe, question, metric, dashboard, API read, workshop, bridge, comparison frame, or coarsened representation as passive, stable, jointly comparable, or faithfully exportable. The main entry question for the whole cluster is: "What should the user do with this lens so that the representational mistake does not arise here?"

Application sequence:

1. Name the ordinary FPF pattern that already carries the baseline question.
2. Name the concrete representational mistake: passive read, shared comparison frame, false faithful-enough export claim for the intended use, exact-state shortcut, or unsupported coarsened representation.
3. Test the positive QL cue and the negative activation list.
4. Fill the QL-lite card if the cue survives.
5. Emit one practical result: use ordinary pattern only, add QL-lite note, select one C.26 child pattern as the applicable pattern body, add evidence and assurance, or drop the QL wording.
6. Escalate only when the claim becomes reusable, assurance-bearing, formal, empirical-superiority-bearing, or ontology-bearing.

C.26 ordinary output: produce one of these, then stop or select the neighboring applicable pattern body:

- no C.26 pattern selection because the ordinary FPF pattern carries the case;
- QL-lite note with the minimum sufficient field set;
- use the ordinary pattern that carries the question under repair;
- escalation to evidence, assurance, or formal-model work when the claim’s evidence or authority demand requires it.

Keep the entry cost proportional to the use. A QL situation does not begin with a full record.

| Working view | Use it when | Ordinary output |
| --- | --- | --- |
| Recognition note | The reader only needs to see that an ordinary FPF pattern plus a QL cue may prevent a representational mistake. | Five-field QL-lite note, local stop, and next action. |
| Decision-bearing record | The QL reading changes a boundary, bridge, work, measurement, viability, or representation decision. | Typed fields for carrier, window, rival, loss, minimal admissible output, admissible use, non-admissible use, and neighboring-pattern handoff. |
| Assurance record | The claim becomes reusable law, audit and evidence support, release-facing support, empirical-superiority claim, formal reconstruction, or ontology-bearing claim. | Evidence graph, measurement relation or assurance relation, source-support role, rival-model comparison, and explicit escalation outside QL-lite. |

Do not make the decision-bearing or assurance record the ordinary entry cost. The everyday pattern move is a small recognition note plus a bounded action.

Affordability by working-reader situation:

| Working-reader situation | Use |
| --- | --- |
| Practitioner or architect | Three-to-five-field recognition note plus decision diff. |
| FPF pattern author | Full card, examples, neighboring-pattern selection, and local anti-cases. |
| Checking reader | Pattern-application check plus false-positive and false-negative tests. |
| Assurance or audit reader | Full evidence record with `B.3`, `A.10`, and `C.16` integration. |
| Research or formalization reader | M3 or M4 formal model, rival models, and empirical or theoretical support. |

Do not require a practitioner or architect to produce a researcher-level record when the claim is only recognition or local-working support condition.

Checking discipline:

| Checking failure | Repair |
| --- | --- |
| "QL word appeared, escalate to assurance." | Ask what claim and evidence demand are actually being made. |
| "This sounds metaphorical, remove it." | Ask what representational mistake the wording prevents. |
| "Use ordinary FPF only." | Name the ordinary FPF pattern that carries the residual claim. |
| "No quantum-like unless mathematically formalized." | Allow QL-lite when it prevents local false reading and no formal claim is made. |
| "Everything with feedback is QL." | Apply `C.16`, `C.25`, or `A.15` first to ordinary feedback, control, and metric-gaming cases. |

Cluster maxim: quantum-like wording does not raise assurance load by default. Assurance load rises only when the claim itself is reused, contested, evidence-bearing, release-facing, high-impact, comparative, formal, or ontology-bearing.

Pattern-local-note dependency rule: when an existing FPF pattern cites `C.26` or a `C.26.*` child, the pattern's ordinary action guidance and conformance text remain primary. The citation means only: if a residual QL cue remains after the ordinary FPF pattern has carried its part, use this lens for that residue. It does not make every citing-pattern case depend on the full C.26 record or on every child-pattern semantic.

QL boundary selection:

| Gate question | Applicable FPF pattern |
| --- | --- |
| Is this ordinary boundary, interface, API, or protocol ambiguity? | `A.6` and the direct boundary or interface pattern. |
| Is this ordinary bridge, export, substitution, or loss across contexts? | `F.9` / `F.9.1`. |
| Is this ordinary measurement, metric gaming, scale, coordinate, or noise? | `C.16`. |
| Is this ordinary evidence, provenance, method, or carrier issue? | `A.10` and, when assurance-bearing, `B.3`. |
| Is this ordinary work, routine, incentive, alignment, or authority issue? | `A.15` and neighboring work/authority patterns. |
| Is this ordinary quality-bundle, viability, feedback, or dynamics tuning? | `C.25`, `U.Dynamics`, and measurement or work patterns. |
| Is this ordinary representation-scheme transition or controlled coarsening? | `A.6.3.RT`, `A.6.3.CSC`, and ordinary representation patterns. |
| Does residual false passive read, false shared frame, false faithful export, unsupported state reading, or QL-specific coarsening remain? | Use `C.26` or the relevant `C.26.*` child with the minimum sufficient field set. |

The default output is a QL-lite card:

| Field | Question |
| --- | --- |
| Ordinary FPF pattern | Which FPF pattern already carries the baseline question? |
| QL cue or formal cue | Which order effect, frame effect, incompatible probe structure, response-replicability tension, measurement-changing-state, no faithful-enough export under the declared probe, frame, or use, bridge loss or export loss, mutual interaction whose local reads and exports are no longer admissibly comparable or reusable without declaring the probe, frame, or update relation, open-information-system update whose update rule, probe frame, or export admissibility is part of the modeling condition, or state-representation coarsening effect changes the admissible reading? |
| Representational payoff | What mistake does the lens prevent, or what cheaper representation does it support? |
| Minimal admissible output | What may be concluded or done now? |
| Decision diff | What would be done incorrectly under the ordinary false reading, and what changes after QL repair? |
| Local stop or neighboring-pattern handoff | Which use is non-admissible under this card, and which neighboring FPF pattern governs that use? |

Decision diff examples:

| False reading | QL repair | Decision diff |
| --- | --- | --- |
| Dashboard passively shows release readiness. | Dashboard publication changes readiness behavior. | Do not use dashboard alone as release evidence; add independent work traces or redesign metric publication. |
| Workshop discovered the boundary. | Workshop also created the boundary meaning. | Do not export workshop result as timeless domain fact; record window, participants, carriers, and unresolved rivals. |
| Service is healthy because latency is green. | Viability envelope is degraded by support load and promise failure. | Add envelope variables and actuators; do not greenlight based on latency alone. |
| Summary preserves architecture state. | Summary is a coarsened shortcut with declared loss. | Use for orientation only; return to source for release or design lock. |

Minimum viable QL-lite note:

```text
Ordinary patterns: C.16 + A.15.
Mistake prevented: dashboard result would be read as passive release-readiness evidence.
Probe effect: publication changed team behavior during W.
Decision diff: do not use dashboard alone for release; add independent work traces.
Stop: not a reusable QL model, not assurance evidence, not physical quantum claim.
```

This is enough for `QLP-0` / `QLP-1` ordinary working use unless the claim is reused, externalized, contested, assurance-facing, comparative, formal, or ontology-bearing.

Use the `C.11` mini-output discipline across the cluster: finish with one choice result or governed follow-up, not with an interesting label.

| Mini-output | Cluster meaning |
| --- | --- |
| Use or choose now | The low-recoverability reading is enough for the declared local action or decision. |
| Probe again | One named probe, order/frame test, measurement, source check, or bridge check could still change the result. |
| Reroute | The question under repair belongs to another FPF pattern rather than QL-lite. |
| No QL wording | Ordinary uncertainty, measurement, work, bridge, quality, or search patterns carry the case. |

Retire QL when the residual cue disappears. If `A.6`, `F.9`, `C.16`, `A.10`, `B.3`, `A.15`, `C.25`, `A.6.3.CSC`, `A.6.3.RT`, or another ordinary FPF pattern now carries the claim without a false passive read, false shared frame, false faithful export, unsupported distributed-state reading, or QL-specific coarsening residue, remove QL wording from the active working note or pattern prose.

Use the lens only after the activation test survives both sides. QL remains active only when the ordinary FPF pattern cannot admissibly treat the output as a passive read, a shared-frame comparison, a faithful-enough export, or a use-scope-preserving state representation. Bridge loss, feedback, coupling, openness, compression, and coarsening are not QL cues unless they change the admissible state, probe, frame, or export reading for the current use. C.26 carries the full negative activation catalog; child and citing patterns should repeat only the local non-trigger that is frequent enough to matter for that pattern.

Canonical cue grammar:

| Cue family | QL only if |
| --- | --- |
| Probe, order, or frame | The operation changes the admissible reading of the output, comparison, or represented state. |
| Export or bridge | The export is not faithful enough for the intended use, and ordinary bridge and loss discipline does not fully carry the remaining export/use issue. |
| Distributed-state reading | Coordinated behavior, trace pattern, or work result supports a low-recoverability state reading no single carrier faithfully exports, after ordinary rivals are checked. |
| Viability envelope | Probe, sensor, actuator, export, boundary condition, or coarsening changes the admissible viability reading. |
| Coarsening | The reduced-detail state representation depends on a QL cue plus declared loss, admissible use, non-admissible downstream use, and reopen trigger; ordinary compression or abstraction alone is not enough. |
| Positive activation pressure | Negative activation test |
| --- | --- |
| Load-bearing order effect, frame effect, incompatible probe structure, response-replicability tension, measurement-changing-state, no faithful-enough export under the declared probe, frame, or use, bridge export of the state that is not faithful enough for the current use, mutual interaction where neither side's output can be used as a faithful-enough local export of the joint state under the intended decision frame after ordinary feedback relations are tried, or state-representation coarsening whose admissible use changes because of a declared QL cue. | No QL activation from discreteness, tokenization, low-bit quantization, stochasticity, ordinary uncertainty, nonlinearity, complexity, ordinary coupling, ordinary feedback, emergence, tacit knowledge, ordinary openness, ordinary compression, ordinary coarsening, ordinary DDD locality, ordinary API boundary, ordinary bridge loss, ordinary feedback control, or impressive quantum-like vocabulary alone. |

Practical payoff in ordinary prose:

- "the metric reported readiness" becomes "the metric publication or measurement regime functioned as a probe interaction that changed readiness behavior";
- "two risk scores disagree" becomes "the two scores may come from non-shared comparison frames with no declared admissible joint comparison route";
- "the workshop discovered the split" becomes "the workshop was a probe whose order and framing changed alignment and local meaning";
- "the team knows" becomes "coordinated work evidences a low-recoverability distributed-state reading with carriers, window, and export loss";
- "this smaller model is enough" becomes "this coarsened state representation carries only its declared admissible-use scope and reopen condition".

#### C.26:4.1 - Inherited QL boundary

Invariant `QL-NQ`: within FPF, `quantum-like` is a detached mathematical and representational modeling lens. It may use quantum-theory-derived structures such as contextual probability, Hilbert-like state spaces, non-Boolean logic, instruments, operator-like update, order effects, open-system descriptions, or incompatible probes.

`Quantum-like` does not assert physical quantum substrate, microscopic quantum process, qubits, quantum computation, physical entanglement, nonlocal causality, literal collapse, mystical observer effects, social substance, or collective mind. A physical-quantum claim is a different claim and needs separate physical or empirical support outside this pattern cluster.

Child patterns inherit `QL-NQ`. They should not restate the global boundary as local guidance unless they are repairing a specific confused phrase.

#### C.26:4.2 - Pattern selector
##### C.26:4.2.1 - Causal-use exit before QL retention

Before retaining `QL-lite`, `QL-NQ`, or a quantum-like framing for a claim being made, check whether the actual question is intervention, counterfactual comparison, causal effect, causal fairness, causal policy, off-policy causal evaluation, or realizability of counterfactual-rung data. If so, redirect the claim or question to `C.28` before any quantum-like retention.

```text
CC-C26-CAUSAL-EXIT:
If the question under repair is intervention, counterfactual comparison,
causal effect, causal fairness, causal policy, or realizability of counterfactual-rung data,
redirect the claim or question to C.28 before retaining QL-lite or QL-NQ.
```

What changes in practice: "the model is quantum-like" cannot be used to skip causality-ladder rung declaration, causal identification, causal evidence support basis, or counterfactual sampling realizability.

What this does not authorize: `C.26` does not become a causal-use pattern and does not treat counterfactual material as a quantum-like subcase; it keeps quantum-like modeling discipline, while causal-use support remains governed by `C.28`.

Use this as a diagnostic sequence before retaining QL wording. DDD, microservice domain analysis, and ordinary boundary/bridge patterns stay first for bounded contexts, service cuts, integration points, and exported meaning; QL is retained only when a workshop, probe, export, or frame changes what can admissibly be inferred.

1. Measurement, metric, scale, method, evidence, or assurance load goes first to measurement and evidence patterns: `C.16`, `A.10`, or `B.3`.
2. Bridge, translation, publication, rendering, or exported-loss question goes first to bridge and publication patterns: `F.9`, `E.17`, or `E.17.EFP`.
3. Causal intervention, command, work enactment, role alignment, or routine question goes first to work and authority patterns: `A.15` and the relevant neighboring pattern.
4. Boundary or interface wording, service-interface typing, bridge endpoint, relation precision, or lexeme-collision question goes first to the direct owner: `A.1` for holon delimitation or boundary crossing, `A.6.P`, `A.6.0`, or `A.6.5` for relation, signature, or slot claims, `A.6.M` for module-interface claims, `A.6.F` for functional ports or elements, `A.6.C` or `A.6.8` for service, protocol, or agreement-like claims, `A.6.B` only for L, A, D, or E statement classification inside a boundary package, and `A.7`, `E.10`, or `F.18` for wording-use repair.
5. Quality, viability, feedback, or control-tuning question goes first to quality, dynamics, and measurement patterns: `C.25`, `U.Dynamics`, and `C.16`.
6. Suspect option menu, unknown alternative, local plateau, basin movement, or candidate-generation question goes first to search and regime patterns: `B.5.2`, `C.18`, `C.19`, or `A.19`.
7. Retain QL only for the remaining declared state, probe, export, frame, open-information-system, or coarsening cue.

C.26 does not choose among options, generate missing alternatives, or settle `C.11` decision quality. It can mark that the available readings sit in non-shared comparison frames or lack a declared admissible joint comparison relation; the choice or search output still belongs to `C.11`, `B.5.2`, `C.18`, `C.19`, or `A.19`.

| If the question under repair is mainly... | First FPF pattern | Add QL only when... |
| --- | --- | --- |
| Choice, comparison, or question order | `C.11` | incompatible probes, order effects, non-shared comparison frames, or no declared admissible joint comparison route change the choice-state reading. |
| Boundary interaction or interface reading | `A.1`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `A.6.C`, `A.6.8`, or `A.6.B` only for L/A/D/E boundary-package classification | the probe or interaction changes the represented state, export validity, or viability decision. |
| Cross-context bridge or publication export | `F.9`, `E.17`, `E.17.EFP` | the exported state is not faithful under the current probe and bridge conditions. |
| Work enactment or coordinated behavior | `A.15`, with `A.10` / `B.3` for evidence | coordinated work evidences a low-recoverability distributed-state reading not faithfully exportable as one representation. |
| Measurement, metric, score, or dashboard | `C.16`, `A.10`, `B.3` | the measurement regime, publication act, or operational use functions as a probe interaction that updates the represented state. |
| Viability or quality bundle | `C.25`, `U.Dynamics`, `A.6`, `A.15` | envelope regulation depends on probe, boundary condition, actuator, export, or coarsened state representation. |
| Candidate generation or option-menu suspicion | `B.5.2`, `C.18`, `C.19`, `A.19` | QL wording only marks that the current frame may be suspect; search patterns generate alternatives. |
| Representation shortcut | CSC, RT, ordinary abstraction, representation learning, POMDP, search-space pruning | the shortcut depends on contextual probability, incompatible probes, instrument-like update, open-information-system update rule, probe-frame, or export-admissibility cue, or lossy state export. |

#### C.26:4.3 - Escalation by evidence or authority demand

| Claim-use class | Use | Required basis |
| --- | --- | --- |
| Ordinary FPF pattern | QL is not needed. | Use the ordinary FPF pattern plainly. |
| QL-lite note | Local diagnosis, model note, or worked recognition. | Fill the five-field card. |
| Reusable pattern prose | A pattern, example, or neighboring note will repeat the move. | Add typed state, probe, or export fields, source support, and local anti-cases. |
| Decision or assurance use | The claim affects boundary, release, audit, evidence, or work decision. | Add rival explanations, evidence-use class, loss notes, and explicit neighboring-pattern selection. |
| Ontology or physical claim | A physical substrate, new ontology, or empirical superiority is asserted. | This pattern does not support the claim; use a separate physical or empirical support outside this pattern cluster. |
For QL claims that carry decision, assurance, ontology, physical-substrate, or empirical-superiority use, compare rival model families before retaining QL as load-bearing. Failure of a simple Bayesian or passive-read model is not yet evidence for QL necessity; it is evidence for trying richer classical, causal, performative, instrument, active-sensing, or representation-abstraction rivals before QL carries the claim:

| Rival family | Use first | Keep QL active only when |
| --- | --- | --- |
| Classical Bayesian, nonparametric Bayesian, or ordinary probabilistic update | `C.11`, measurement and evidence patterns, and model-expansion patterns | incompatible sample spaces, contextual probability, order-sensitive query structure, or failure of ordinary total-probability composition remains active. |
| Causal intervention or ordinary world-state change model | `A.15`, boundary patterns, and evidence patterns | the intervention is also being used as a read, export, comparison, or optimization of the state it changes. |
| Performative prediction, strategic response, or dashboard-induced behavior | `C.16`, `A.10`, `B.3`, `C.26.1`, and viability/work patterns | instrument-like state update, incompatible probes, or non-faithful state export remains after the ordinary behavior account is written. |
| POMDP, active sensing, active inference, or experimental design | `A.3`, `C.16`, `U.Dynamics`, and action-cost patterns | the formal claim also involves incompatible probe frames, contextual probability, or state-representation loss. |
| State abstraction, representation learning, surrogate modeling, sketching, or ordinary compression | `A.6.3.CSC`, `A.6.3.RT`, `A.19`, `F.9`, and ordinary representation patterns | the shortcut depends on contextual, instrument-like, open-information-system update/probe/export-admissibility, or incompatible-probe structure rather than ordinary abstraction engineering. |
| Causal abstraction or approximate causal abstraction | Use first when the shortcut claims to preserve intervention, explanation, manipulation, or cross-scale structure. | contextual probability, incompatible probes, instrument-like update, open-information-system update rule/probe-frame/export-admissibility, or lossy state export remains after the causal-abstraction mapping between source-scale and target-scale states and interventions is stated. |

Math reveal sequence:

| Mathematical-formality class | Use | Form |
| --- | --- | --- |
| M0 - no math | Everyday FPF use. | Plain-language QL-lite note: false passive read, output, admissible use, and stop. |
| M1 - structural sketch | A reader needs to see why ordinary comparison or export fails. | Diagram or table: probes, frames, carriers, export loss, unsupported comparison. |
| M2 - toy formalization | Pattern example, education, or contested architecture claim. | Small finite-state, matrix, or instrument-like toy model, explicitly non-authoritative. |
| M3 - decision-bearing formal model | Reusable guidance or high-impact decision. | Declared assumptions, rival models, validation/evidence, and failure conditions. |
| M4 - formal assurance / research claim | `QLP-3` assurance or reusable-law claim. | Full formal reconstruction, baseline, proof/data, source constraints, and limitations. |

Most C.26 use should stay at M0 or M1.

Evidence-use class is escalation by consequence, not an admission gate. `QLP-0` or `QLP-1` is the ordinary entry class for quick QL-lite use; `QLP-2` / `QLP-3` appears only when the claim is reused, contested, decision-bearing, assurance-facing, high-impact, or made part of reusable pattern action guidance or conformance text.

Evidence-use class scales by use:

| Level | Use | Required content |
| --- | --- | --- |
| `QLP-0` recognition | Example, teaching case, or local recognition prompt. | Claim, example, ordinary FPF pattern, QL cue, and local stop. |
| `QLP-1` local working use | Local architecture discussion, triage, or provisional design reasoning. | `QLP-0` content plus evidence carrier, time window, uncertainty/confidence statement, and stop/reroute condition. |
| `QLP-2` decision-bearing use | Boundary decision, bridge/export use, viability move, work claim, or representation shortcut changes what the team should do. | `QLP-1` content plus rival explanations, export/loss note when live, minimal admissible output, selected applicable pattern body, admissible use, and non-admissible use. |
| `QLP-3` assurance or reusable guidance use | The claim is used for assurance, audit, durable pattern action guidance or conformance text, reusable relation, name, or measure, or high-stakes decision support. | `QLP-2` content plus `A.10` and `B.3` assurance result, `C.16` template if measured, documented bridge and loss relation, source-support role, and explicit local stop or inherited-boundary note. |

#### C.26:4.4 - Recognition case matrix

| Case | First applicable pattern body | QL cue to test | Local stop |
| --- | --- | --- | --- |
| Domain workshop changes the split | `A.1.1`, `F.9`, `C.26.1` | The workshop is both evidence and intervention; question order or facilitation frame changes split recommendation, team alignment, and local meaning. | Do not replace DDD with QL; keep bounded-context law and bridge fields active. |
| Same label across bounded contexts | `F.9`, `A.6.P` | API extraction or team alignment changes operational state, or export loses the relation that matters. | Same label is not same entity; ordinary bridge may be enough. |
| Organization acts from a latent decision | `A.15`, `A.10`, `B.3`, `C.26.2` | Coordinated role-work, records, commitments, traces, and routines evidence a low-recoverability state no participant faithfully reports. | Do not infer a group mind or timeless culture. |
| Survey, dashboard, policy, or API read of culture | `C.16`, `A.10`, `F.9`, `C.26.1`, `C.26.2` | The probe may change the state it evidences, and the export may lose load-bearing structure. | Treat the output as carrier/probe, not as the state itself. |
| Service boundary under load | `C.25`, `A.6`, `A.15`, `C.26.3` | Viability depends on changing caching, throttling, routing, staffing, protocol, bridge, or context split. | Do not reduce viability to one green metric. |
| Moving body or sensor to see the missing face | active or embodied inference accounts, `C.26:4.5` state-representation coarsening card | The system spends energy, time, risk, attention, or coordination to obtain a discriminating observation. | Do not call ordinary sensing or active inference quantum-like without a QL cue. |
| Glass memory / hysteresis | `C.26.1`, `C.26.3`, `U.Dynamics` | Prior state constrains current response; state history or retained trace changes admissible reading. | Do not force dynamics variables unless load-bearing. |
| Cell-like service situation | service, boundary, work, viability patterns first | Cell-like criteria may clarify boundary, controlled exchange, protected invariants, repair, state-continuity, and resource analogue. | Retain analogy only when it changes a decision beyond ordinary service-facet language. |
| Suspect option menu | `B.5.2`, `C.18`, `C.19`, `A.19` | Current options may be products of the current measurement frame. | QL only marks suspicion; search patterns generate alternatives. |

#### C.26:4.5 - State-representation coarsening card

This card discipline is active when a fuller state representation is too detailed, unstable, unavailable, or expensive for the current bounded decision and a reduced-detail state representation is useful only under a declared QL cue. It is not a standalone speed pattern, not a standalone coarsening pattern, and not a new state-representation kind.

C.26 does not carry ordinary coarsening. `A.6.3.CSC` carries controlled coarsened rendering; `A.6.3.RT` carries same-selected-entity representation-scheme transition; `A.19`, `U.Dynamics`, modeling patterns, and ordinary abstraction patterns carry ordinary state abstraction. C.26 carries only the residual QL cue plus the loss/use boundary for this shortcut.

Question-to-pattern map:

| Main question | First FPF pattern or relation |
| --- | --- |
| Coarsened rendering of source episteme or source publication for narrower use | `A.6.3.CSC` |
| Same-selected-entity representation-scheme or reasoning-medium transition | `A.6.3.RT` |
| Cross-context equivalence, substitution, projection, export, or loss | `F.9` / `F.9.1` |
| Measurement coordinate, scale, score, result, or dashboard reading | `C.16` |
| Evidence carrier, provenance, method, support, or time window | `A.10` |
| Assurance claim, release support, audit, readiness, or compliance use | `B.3` |
| Search-space pruning, option generation, or missing alternatives | `C.18`, `C.19`, `A.19` |
| Residual QL state, probe, frame, export, or coarsening cue after those patterns act | `C.26` |

Start with this coarsening mini-card:

| Mini-entry | Question |
| --- | --- |
| Source | Which fuller state representation, trace set, model, measurement scheme, or dynamics account loses distinctions in the shortcut? |
| Shortcut | Which smaller representation is being used instead, and for which bounded decision or action class? |
| Loss | Which precision, distinction, uncertainty, comparability, traceability, or relation structure is lost? |
| Admissible use | Which bounded decision, probe, comparison, time-window reading, or action class remains admissible for this reduced-detail state representation? |
| Reopen trigger | Which dispute, drift, failure, threshold crossing, bridge demand, or decision change requires return to the source-bearing episteme or source publication? |

For the representation shortcut itself, fill this coarsening card:

| Field | Question |
| --- | --- |
| Source representation | Which fuller model, state space, trace set, measurement scheme, probability model, dynamics model, or representation loses distinctions in the shortcut? |
| Coarsened representation | Which typed, symbolic, finite, operator-like, Hilbert-like, rough-set, low-bit, or source-loss-affected representation is used instead? |
| Shortcut mechanism | Which projection, typed-state reduction, finite-dimensional representation, operator-like update, rough-set approximation, state aggregation, compression, or linearization is doing the representational work? |
| Shortcut purpose | Which bounded decision, probe, comparison, time-window reading, or action class needs the reduced-detail state representation? |
| What is lost | Which precision, distinction, uncertainty, compatibility, traceability, causal detail, or cross-context relation is lost? |
| Loss budget | How much loss is accepted for this decision, probe, comparison, route, or time window? |
| Admissible use | For which decisions, probes, comparisons, candidate-route selections, or time windows does the shortcut preserve the required distinctions? |
| Non-admissible use | For which claims, audits, bridges, comparisons, future actions, or high-stakes decisions does the shortcut lack the required distinctions, source support, or recoverability? |
| Ordinary explanations still active | Which ordinary abstraction, causal abstraction, approximate causal abstraction, state aggregation, representation learning, POMDP simplification, heuristic compression, CSC, RT, or low-bit implementation account remains sufficient if the QL cue is absent? |
| Evidence or formal source | Which model, trace, experiment, source, or formal argument supports the shortcut rather than merely naming it quantum-like? |
| Reopen trigger | Which dispute, drift, threshold crossing, failure, audit, bridge demand, or decision change requires returning to the source representation or ordinary FPF pattern? |

If the text claims that the shortcut is faster, cheaper, more compressed, more linear, more stable, or more tractable, add this claim declaration. The claim is separate from the coarsening card: the card controls the reduced-detail state representation; the declaration controls the performance or tractability assertion.

| Declaration field | Question |
| --- | --- |
| Baseline representation and cost | What ordinary model or route is too expensive, and by which resource: time, memory, measurement, coordination, latency, energy, risk, attention, cognitive load, privacy, or social cost? |
| New representation | Which changed representation creates the claimed gain? |
| Mechanism | Which compression, linearization, operator-state update, reduced information-state encoding, shortcut, or approximation mechanism creates the gain? |
| Claimed gain | What exactly becomes faster, cheaper, more stable, smaller, or more tractable? |
| Loss or error budget | Which precision, expressivity, compatibility, comparability, evidence-support class, traceability, or future-use loss is accepted for the intended use? |
| Admissible use | For which decisions, probes, comparisons, candidate-route selections, time windows, or action classes does the declared gain meet the required threshold? |
| Non-admissible use | For which claims, audits, bridges, comparisons, future actions, or high-stakes decisions does the declared gain fail the required threshold? |
| Ordinary alternatives | Which ordinary compression, approximation, abstraction, feature-engineering, active-inference, search, POMDP, or low-bit route was tried or remains sufficient? |
| Evidence or formal source | Which source, model, trace, worked case, benchmark, or formal analogy supports the claimed mechanism? |
| Reopen trigger | Which dispute, drift, threshold crossing, failure, audit, bridge demand, or decision change requires returning to the source representation or ordinary FPF pattern? |

No speed, compression, linearity, or tractability claim follows merely from the words `linear`, `operator`, `quantum-like`, `quantized`, `tokenized`, `low-bit`, `finite-dimensional`, `compressed`, or `symbolic`.

If the shortcut carries a transition-speed, stabilization, or control claim, add the optional dynamics card:

| Dynamics field | Question |
| --- | --- |
| Rate or acceleration | Which transition, inference, recovery, sensing, routing, or stabilization rate matters? |
| Inertia | What makes the represented state, work routine, boundary condition, or model slow to change? |
| Damping or resistance | What absorbs, slows, filters, or resists the transition? |
| Effort or actuator capacity | Which action, probe, resource, or authority relation can change the transition fast enough? |
| Evidence | Which trace, model, experiment, or operational observation supports the dynamic reading? |

### C.26:5 - Archetypal Grounding

Tell: A reliability dashboard says "Ready" after a new readiness metric is published. Before publication, teams treated incidents as local triage. After publication, they change priorities to satisfy the metric, while unmeasured recovery work gets delayed.

Show, System side: the delivery system, teams, dashboard, incident-handling cycle, and release decision form one operational situation. The dashboard is not only a window; it is part of the work ecology because it changes attention, escalation, and behavior.

Show, Episteme side: the QL-lite card says the ordinary FPF patterns are `C.16`, `A.10`, `B.3`, and `C.25`. The QL cue is an instrument-like metric publication that changes readiness behavior. The minimal admissible output is "treat the dashboard as probe-coupled evidence, not release proof." The local stop is release approval without fuller evidence.

Second grounding: a large state-space model is too expensive for triage, so the team uses four typed operational states. That shortcut is admissible only if the source model, state reduction, loss, admissible use, and reopen trigger remain explicit. The shortcut helps choose a work response; it does not prove the four states are the full system.

### C.26:6 - Bias-Annotation

This pattern intentionally biases authors toward ordinary FPF patterns before QL vocabulary. That bias prevents prestige use of the word `quantum-like` and keeps the mathematical lens useful rather than theatrical.

It also biases authors toward minimal admissible outputs. In ordinary use, the right result is often "apply the neighboring FPF pattern", "do not merge these comparison frames", "mark this dashboard as an instrument", or "return to the source representation if the shortcut fails", not a new doctrine about the target system.

The pattern may under-admit some mathematically valid QL models when the author cannot explain the practical payoff. That is acceptable for FPF pattern prose: a model that cannot say what it buys the working reader is not ready for Core-facing law.

### C.26:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| CC-C26.1 | The text names the ordinary FPF pattern before admitting QL wording. |
| CC-C26.2 | The text states the QL cue as a probe, order, frame, export, comparison, open-information-system update/probe/export-admissibility, or coarsening effect, not as vague complexity. |
| CC-C26.3 | The text states a practical representational payoff. |
| CC-C26.4 | The text states the minimal admissible output. |
| CC-C26.5 | The text states a local stop or neighboring-pattern handoff. |
| CC-C26.6 | The text inherits `QL-NQ` and does not repeat global physical-quantum exclusions as local guidance. |
| CC-C26.7 | If a representation shortcut is used, the coarsening card names source, shortcut, loss, admissible use, non-admissible use, and reopen trigger. |
| CC-C26.8 | A speed, compression, linearity, or tractability claim declaration names baseline representation and cost, changed representation, mechanism, claimed gain, loss budget or error budget, ordinary alternatives, evidence source or formal source, and reopen trigger. |
| CC-C26.9 | If the claim becomes reusable, assurance-bearing, measurement-like, relation-minting, high-stakes, or superiority-claiming, the text escalates beyond QL-lite. |
| CC-C26.10 | The text does not mint `U.Probe`, generic `U.State`, `U.DistributedState`, `U.Lens`, a new boundary kind, or a social-substance kind. |
| CC-C26.11 | A cold reader can tell what changes in practice in the first minute. |
| CC-C26-CAUSAL-EXIT | If the question under repair is intervention, counterfactual comparison, causal effect, causal fairness, causal policy, off-policy causal evaluation, or realizability of counterfactual-rung data, the text redirects the claim or question to `C.28` before retaining QL-lite or QL-NQ. |

### C.26:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Quantum-like as prestige word | The case is only complex, uncertain, nonlinear, discrete, or hard to measure. | Use ordinary FPF patterns. Admit QL only with a declared cue and payoff. |
| Precautionary suppression | QL wording is rejected because it is unusual, while no ordinary FPF pattern has carried the residual false passive read, false export, false comparison frame, unsupported distributed-state reading, or single-metric viability mistake. | Name the ordinary FPF pattern that carries the residual claim. If no such pattern can be named, allow QL-lite at recognition or local-working support condition. |
| Physical overread | The text sounds as if organizations, services, or teams are physically quantum systems. | Cite inherited `QL-NQ`; rewrite the claim as mathematical or representational. |
| Passive dashboard | A metric or score is used as a neutral fact after its publication or operational use changed behavior. | Use measurement and evidence patterns and, if needed, `C.26.1`. |
| Faithful-copy export | A survey, report, API response, or context map is treated as the live state itself. | Use bridge/export loss, `C.26.2`, or ordinary publication patterns. |
| Speed or compression slogan | A shortcut is called fast, cheaper, linear, low-bit, symbolic, or compressed without a declared claim. | Write the speed, compression, or linearity claim declaration: baseline representation and cost, changed representation, mechanism, claimed gain, loss budget or error budget, ordinary alternatives, evidence source or formal source, and reopen trigger. Keep the coarsening card only for the representation shortcut itself. |
| Hidden search problem | The option menu is frame-bound, but the text tries to solve it by naming QL. | Use QL only as a suspicion cue; apply search patterns to generation and regime movement. |
| Cell-like service jump | A service is called cell-like because it has a boundary or internal state. | Unpack service facets first: boundary, controlled exchange, internal state, health maintenance, adaptive behavior, coupling protocol, resource-metabolism analogue, protected invariants, repair, and state-continuity. Retain the analogy only when it changes a boundary, viability, repair and state-continuity, or resource-exchange decision. |

Near-miss taxonomy:

| Near miss | Why not QL by itself |
| --- | --- |
| Feedback loop | Ordinary dynamics/control unless admissible reading, export, or comparison is affected. |
| Metric gaming | Ordinary metric/incentive problem unless measurement publication changes the state reading. |
| Uncertainty | Ordinary epistemic uncertainty unless context, probe, or frame changes variable identity or comparison law. |
| Complexity | Ordinary complexity unless shortcut, export, or probe issue remains. |
| Compression | `A.6.3.CSC`, `A.6.3.RT`, modeling, or implementation pattern first; QL only for state-representation residue. |
| DDD bounded context | `A.6` / `F.9` first; QL only if workshop, probe, or export changes state reading. |
| Low-bit or quantized implementation | Engineering representation first; not QL because it is "quantized". |
| Collective behavior | `A.15`, distributed cognition, routines, and evidence patterns first; QL only for low-recoverability state-reading residue. |

#### C.26:8.1 - Cluster conformance scenarios

Use these as quick applicability tests. A good C.26 use leaves one practical output, not just a clever label.

| Scenario | Expected route | Avoid | Expected output |
| --- | --- | --- | --- |
| Dashboard readiness improves because teams optimize the displayed metric. | `C.16` / `A.15` first; `C.26.1` only if the output is reused as a passive readiness read after state-shaping publication. | Treating the dashboard value as release evidence by itself. | Redesign metric publication or add independent work traces before release use. |
| Workshop "discovers" a boundary but also creates alignment and local meaning. | `A.6` / `A.15` first; `C.26.1` for false pre-probe discovery reading. | Exporting the workshop result as a timeless domain fact. | Record window, participants, carriers, unresolved rivals, and bridge/export limits. |
| API read warms cache and changes downstream timing. | Interface semantics, `A.6`, and `C.16` first; `C.26.1` if the read result is reused as passive state export. | Saying the API read simply copied state. | Mark the read as non-neutral for that timing window or redesign the read path. |
| Two service health reports use different measurement frames. | `C.16` / `F.9` first; `C.26` only if no admissible shared comparison frame remains. | Averaging the scores as one posterior-looking value. | Name the frame difference and either build an admissible comparison route or stop comparison. |
| Team survey says "aligned", but incident behavior contradicts it. | `A.10` / `A.15` / `B.3` first; `C.26.2` if coordinated work traces support a low-recoverability distributed-state reading. | Treating survey output as the team state. | State a low-recoverability carrier/window-bound reading and the rival explanations. |
| Market "expects" a feature because many actors change behavior. | Declare bearer/traces; ordinary market, incentive, and evidence explanation first; `C.26.2` only for residual low-recoverability state reading. | Inventing a market mind. | Name actor traces, window, rivals, and the least-supported behavior-based reading. |
| Latency is green while support load and customer promise degrade. | `C.25` / `C.16` first; `C.26.3` if viability reading is probe/export/frame/coarsening-distorted. | Calling one green metric viability. | Add envelope variables, actuators, costs, and failure mode. |
| Summary compresses an architecture decision for executives. | `A.6.3.CSC` first; no QL unless a state-representation shortcut has QL residue. | Treating the summary as full architecture state. | Use for orientation only; return to source for release or design lock. |
| Diagram translates the same system into graph form. | `A.6.3.RT` first; no QL unless incompatible representation, probe, or export cue remains. | Calling any diagram a QL state model. | Declare representation-scheme change, reasoning-medium change, and source tether. |
| Low-bit model approximates expensive simulation. | Modeling, approximation, compression, or implementation pattern first; QL only if the shortcut claim depends on QL state, probe, or frame admissibility. | Treating low-bit or linear form as QL activation. | Name baseline, shortcut, loss budget or error budget, ordinary alternatives, and reopen trigger. |
| Assurance load is raised only because the word "quantum-like" appears. | Keep QL-lite unless decision, release, audit, reusable-law, comparative, formal, or ontology-bearing claim exists. | Escalating because of vocabulary alone. | Keep recognition or local-working support condition, or retire QL if ordinary patterns now carry the residue. |
| Author claims QL is faster or better than a classical method. | Require baseline, metric, mechanism, evidence or formal argument, loss/use declaration, ordinary alternatives, and reopen trigger. | Accepting superiority rhetoric. | Either write the claim declaration or remove the speed/superiority claim. |

QL can also generate better design options:

| Problem | QL-inspired design option |
| --- | --- |
| Dashboard changes behavior destructively. | Delay publication, split private and public metrics, add independent sampling, or publish confidence and loss boundaries. |
| Workshop creates alignment but masquerades as discovery. | Record pre-workshop hypotheses, post-workshop commitments, and created boundary meaning separately. |
| API read disturbs state. | Add non-mutating read, shadow read, sampling window, idempotence declaration, or separate observation channel. |
| Metrics in two contexts are not comparable. | Build a bridge or coupling record or stop comparison. |
| Summary is overused as source. | Add admissible-use label and return-to-source trigger. |
| Viability scalar hides damage. | Build envelope variables and actuators; add a failure-mode sensor. |

#### C.26:8.2 - AI and LLM work-cycle route examples

LLM-mediated work cycles often create the same representational mistakes C.26 repairs: false passive read, false faithful summary, false shared comparison frame, and shortcut without loss/use declaration. This does not make LLMs quantum-like.

| AI case | Route |
| --- | --- |
| LLM summary of an architecture record | `A.6.3.CSC`, `A.6.3.RT`, and `A.10` first; C.26 coarsening only if a state-representation shortcut is being overused. |
| Prompted model evaluation changes model or prompt behavior | `C.16` / `B.3` first; `C.26.1` only if the eval output is treated as a passive model-state read. |
| Agent work cycle "discovers" requirements | `A.15` / `A.10` / `A.6` first; `C.26.1` only if the interaction created the requirement framing. |
| Synthetic personas "represent market state" | `A.10` / `B.3` first; `C.26.2` only if a low-recoverability state-reading claim is carefully bounded with non-admissible use visible. |

### C.26:9 - Consequences

This pattern gives FPF a single place to define QL-lite and the inherited non-quantum boundary. That reduces repeated disclaimers in child patterns and makes ordinary use lighter.

Cluster success criteria:

| Criterion | Good indicator |
| --- | --- |
| Fewer false passive reads | Dashboards, workshops, API reads, and reports are less often treated as neutral state copies. |
| Fewer invalid comparisons | Same-named metrics from different contexts are not silently compared. |
| Better bridge records | `F.9` records more often include admissible export use and non-admissible export use. |
| Better release and evidence discipline | `B.3` and `A.10` are invoked only when the claim’s evidence or authority demand requires them. |
| Less metaphorical leakage | Fewer `field`, `collapse`, `entanglement`, and `group mind` phrases appear in normative text. |
| Faster local notes | Practitioners can write QL-lite notes without full audit cards. |
| More retirements | QL wording is removed when ordinary FPF patterns carry the claim. |

The best outcome may be fewer but better QL mentions.

Do not retrofit QL into existing FPF examples merely because they involve measurement, context, service boundaries, feedback, coarsening, or distributed work. Patch only examples where a named false passive read, false shared frame, false faithful export, low-recoverability distributed-state reading, or QL-specific coarsening residue changes the decision.

The cost is authoring discipline. A writer must name the ordinary FPF pattern, the actual QL cue, and the local stop. That is more work than saying "context matters", but it prevents the most expensive mistake: treating a changed, thinned, or frame-bound representation as if it were a full state.

The state-representation coarsening card makes speed and tractability claims more honest. It lets teams use cheaper state descriptions while keeping loss and reopen conditions visible.

### C.26:10 - Rationale

The cluster stays small on purpose. A single giant "Quantum-Like Architecture" pattern would hide distinct modeling concerns. Scattering the lens across local pattern bodies would repeat the same definition and boundary notes. This modeling-lens pattern lets the common lens live once while child patterns carry their own primary EntityOfConcern and admissible move.

The key rule is simple: quantum-like is not quantum. Once that is typed, FPF can use the math lens normally. The lens earns its keep when it prevents a passive-read, one-space comparison, faithful-copy, or exact-state shortcut.

Evidence is not prestige. Literature supports the modeling move; local evidence supports the local state, export, or probe claim. A source anchor can justify why order effects, contextual probability, instrument-like readings, or open-system modeling are legitimate modeling patterns. It does not prove that this dashboard changed this team's state, that this workshop changed a boundary, or that this export lost the live coordination. That proof or evidence still belongs under `A.10`, `C.16`, `A.15`, `B.3`, and the ordinary pattern for the local claim.

### C.26:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication |
| --- | --- | --- |
| Mathematical objects can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | Wigner on mathematical usefulness, Jaynes on probability as logic of science, and Khrennikov on quantum formalism outside physics. | Treat QL as a math-lens transfer card: explain the useful structure first, then state the inherited boundary. |
| Quantum-like is a mathematical or representational modeling lens, not a physical claim about the modeled system. | Basieva, Khrennikov, and Ozawa on quantum-like modeling in biology with open-system and instrument language. | Keep `QL-NQ` as non-entailment, not as the main claim; use detached mathematical modeling where state, probe, or export cue is real. |
| Linear quantum-like representation can make selected information-state processing more tractable if the representation and loss profile are declared. | Basieva-Khrennikov-Ozawa linearity / speed-up / stability arguments and finite-dimensional matrix-calculus discussions. | Support the state-representation coarsening card discipline; block blanket "quantum-like is faster" claims unless baseline cost, shortcut, loss, and reopen trigger are named. |
| Quantum probability is useful where inference is contextual, previous judgments change state, or possibilities interfere, but QL is not automatically the only formal route. | Quantum cognition work, quantum-instrument work, and process-theory cautions about classical instrument alternatives. | Use QL-lite as useful abstract modeling, not as proof of non-classical necessity. |
| DDD, microservice, active-inference, and measurement practice already supply ordinary FPF patterns. | DDD and microservice domain analysis, active-inference measurement-as-action work, performative prediction, metric-induced behavior. | Keep ordinary FPF patterns first; add QL only for the remaining state, probe, export, frame, or coarsening cue. |

#### C.26:11.1 - Selected operational source anchors

This section is intentionally short. It carries operational anchors for using the pattern, not an expanded bibliography.

| Claim | Source family | Practical implication |
| --- | --- | --- |
| Mathematical formalisms can be transferred as modeling lenses without claiming the target domain is made of the source-domain stuff. | [Wigner on mathematical usefulness](https://www.organism.earth/library/document/unreasonable-effectiveness-of-mathematics), [Jaynes on probability as logic](https://openlibrary.org/books/OL22584017M/PROBABILITY_THEORY_THE_LOGIC_OF_SCIENCE), and Khrennikov's quantum-like modeling line. | Treat QL as a math-lens transfer: name the useful structure, the ordinary FPF pattern, and the local stop before any claim requiring additional evidence or authority. |
| Quantum-like open-system and instrument formalisms can model state and probe interaction without physical quantum ontology. | [Basieva, Khrennikov, and Ozawa](https://www.sciencedirect.com/science/article/pii/S0303264720301994) and [arXiv](https://arxiv.org/abs/2010.15573), plus [Khrennikov on open systems](https://www.mdpi.com/1099-4300/25/6/886). | Keep `QL-NQ` central and use QL only where probe, instrument, open-information-system update rule, probe frame, export admissibility, or state export cue changes the admissible reading. |
| Question order, contextual judgment, and instrument-like operations are practical cues, but not automatic proof that QL is necessary. | [Quantum instruments for question-order effects](https://www.sciencedirect.com/science/article/pii/S0022249620301152), [Quantum Cognition](https://www.annualreviews.org/content/journals/10.1146/annurev-psych-033020-123501), and [process-theory non-exclusivity](https://arxiv.org/abs/2604.08604). | Use QL-lite when order/frame/probe effects change the result; keep classical instrument, Bayesian, causal, and ordinary measurement rivals live. |
| Same-content-looking measurements under different probe or measurement frames should not be silently treated as the same random variable or as jointly distributed. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207). | Use QL when the frame changes variable identity, joint availability, or admissible comparison; otherwise keep the ordinary measurement, bridge, or bounded-context pattern. |
| Viability and active sensing often mix reading and acting, but ordinary control and measurement patterns remain primary. | [Free-energy and quantum-cognition link](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full), [physiological regulation and FEP](https://www.sciencedirect.com/science/article/pii/S0149763423004281), [active inference behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612), and [smart-building active inference](https://arxiv.org/abs/2503.18161). | For viability cases, name sensors, probes, actuators, and envelope variables first; retain QL only for remaining probe, frame, export, or coarsening cue. |
| Boundaries and contexts are already disciplined by ordinary architecture and DDD practice. | [Computational boundary of a self](https://philpapers.org/rec/LEVTCB-3), [Markov blankets of life](https://philarchive.org/rec/KIRTMB), [Azure domain analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis), and [DDD 2025 SLR](https://www.sciencedirect.com/science/article/pii/S0164121225002055). | Apply ordinary FPF patterns first to boundary, interface, bounded-context, bridge, and microservice questions. If Markov-blanket wording is present, restore whether it names local Markov dynamics, mathematical lens, statistical or probabilistic boundary-lens cue, physical-boundary claim, module-interface claim, component claim, description claim, publication claim, or agency-threshold claim; retain C.26 only where probe, order, frame, export, or state-reading effects remain load-bearing. |
| Low-bit, tokenized, compressed, geometric, or neural representations may be useful shortcuts without being QL activation. | [1-bit LLMs](https://arxiv.org/abs/2402.17764), [implicit continuity in language models](https://arxiv.org/abs/2504.03933), [emergent quantumness in neural networks](https://arxiv.org/abs/2012.05082), and [covariant gradient descent](https://arxiv.org/abs/2504.05279). | Keep implementation substrate, geometry, compression, and representation shortcuts in ordinary FPF patterns unless a declared QL cue changes the admissible use. |
| Unknown alternatives and regime movement are search/generation problems, not QL claim authority. | [Open-endedness](https://arxiv.org/abs/2406.04268) and [quality-diversity through AI feedback](https://openreview.net/forum?id=owokKCrGYr). | Use QL only to mark a suspect frame; apply search or regime patterns to generation of alternatives. |

### C.26:12 - Relations

**C.28 causal-use relation.**

- C.28 governs causal-use question, causality-ladder rung, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, causal-use verdict, causal fairness, causal policy, and causal method parity.
- This pattern keeps residual quantum-like probe, frame, order, export, or coarsening discipline after ordinary causal-use explanation has been tried.
- Non-admissible use: intervention, causal effect, causal fairness, causal policy, counterfactual comparison, causal method parity, or counterfactual-rung-data realizability do not activate quantum-like modeling by themselves.
- Exit: when the question under repair is causal, cite `C.28` before retaining QL-lite or QL-NQ.

**C.27 temporal-claim relation.**

- C.27 may flag: ordinary state/rate/rate-change, effort-window, rhythm, braking, coasting, or intervention-timing claims before any quantum-like cue is considered.
- This pattern keeps: residual quantum-like probe, frame, order, export, or coarsening discipline.
- Non-admissible use: discreteness, finite differences, typed states, state-space reduction, tokenization, dashboards, probes, measurement plans, speed words, rhythm words, or Dyn2 words do not activate quantum-like modeling by themselves.
- Boundary: use C.27 and ordinary FPF patterns first; use C.26 only where residual probe, frame, order, export, or coarsening cue remains after those relations are named.

- Builds on: `E.8`, `E.9`, `C.11`, `C.16`, `C.25`, `A.6`, `A.6.P`, `F.9`, `A.15`, `A.10`, `B.3`, `A.3`, `C.18`, `C.19`, `A.19`.
- Constrains: QL wording in `C.26.1`, `C.26.2`, and `C.26.3`.
- Carries: state-representation coarsening as a card inside `C.26:4.5`, not as a separate pattern.
- Does not cover: physical quantum claims, a generic probe ontology, a generic state ontology, a service/cell pattern, or a field-like synchronization pattern.
- Name boundary: `Quantum-Like Modeling Lens` is a pattern label for a modeling lens and modeling discipline, not `U.Lens`, not `QuantumLikeArchitecture`, not `Quantum Substrate`, not `Quantum Ontology`, and not a universal architecture doctrine.

### C.26:12b - C.29 mathematical-lens use relation

> `C.26` is a C.29-compatible specialization for quantum-like modeling. It carries a pre-filled adequacy profile for QL work: preserved structure includes order, probe, and contextual-probability effects when supported; lost structure includes physical quantum ontology; the canonical stop condition remains `QL-NQ`. A QL-lite note does not inherit a blank full `MathLensUse.FullCard`. A full C.29-compatible profile is needed only when the QL claim is decision-bearing, reusable, publication-bearing, assurance-bearing, bridge-bearing, or formal-model-bearing.

### C.26:End

