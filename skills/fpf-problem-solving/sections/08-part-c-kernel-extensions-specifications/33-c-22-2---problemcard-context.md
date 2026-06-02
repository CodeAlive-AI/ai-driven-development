## C.22.2 - ProblemCard@Context

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Context-bound problem card.

**Intent.** Give a practitioner one compact problem-side record that can turn a messy problem signal into a reviewable problem-side record before downstream Principles-to-Work (P2W), without moving archive, portfolio, selected-set, evidence, autonomy, gate, method, or work authority into the card.

**Use this when.** Use this pattern when a signal, anomaly, drift, risk, hypothesis, stakeholder pressure, set-derived candidate, underused capability, new constraint, new environment, opportunity-like cue, or solution-shaped request must become reviewable before task typing, method-family selection, work planning, evidence use, gate passage, autonomy control, or P2W. Also use it when P2W would otherwise receive a slogan, wish, ticket-shaped task, preselected work item, or solution-shaped task.

**Do not use this when.** Do not use this pattern as a work plan, method selection, evidence pack, gate decision, autonomy permission, archive, portfolio, selected set, parity report, mathematical adequacy record, or general discussion note. Use the neighboring pattern that carries the live relation.

**Builds on.** `E.2`, `E.9`, `E.10`, `C.2.P`, `A.6.P`, `C.16.Q`, `C.16`, `A.19`, `C.22`, `C.25`, `C.29`, `G.5`, `G.9`, `A.6.3.RT`, and `A.6.4`.

**Coordinates with.** `C.11`, `C.18`, `C.19`, `C.22.1`, `C.24`, `C.27`, `C.28`, `A.15`, `A.21`, `E.16`, `G.6`, `G.11`, `A.10`, `B.3`, `E.17`, `E.17.ID.CR`, `A.6.3`, `F.9`, and `E.18`.

**Boundary summary.** `C.22.2` use starts from messy problem-side signals and yields one reviewable `ProblemCard@Context`, a `P2W-ready` problem-side input for downstream `C.22`, or a named neighboring exit. `C.22` keeps the selector-facing `TaskSignature`; neighboring patterns keep authority for characterization, comparison, acceptance, archive and set relations, evidence, gate, autonomy, work, representation, temporal, causal, and mathematical relations. `C.22.2` does not govern those receiving relations.

### C.22.2:1 - Problem Frame

A working team can reach the beginning of development with symptoms, anomalies, stakeholder signals, constraints, risks, old solution evidence, comparison ideas, solution temptations, underused capabilities, new environments, and opportunity-like cues. Opportunity-like signals still need context, scope cut, not-wish reason, improvement or acceptance probe, and honest next move; they do not turn this pattern into ideation authority. If FPF only says "type the task" or "choose a method", P2W can receive a slogan, a ticket-shaped wish, or a solution-shaped task before the problem itself is reviewable.

Problematization becomes useful for FPF use when it makes the problem side explicit. A problem needs symptom detection, improvement check, acceptance probe or candidate acceptance basis, mandatory constraints, risk posture, support posture, validation boundary, freshness or expiry, and a relation to candidate solution search. Many problems also arrive from a retained set: candidates, anomalies, hypotheses, non-dominated fronts, shortlists, selected sets, live pools, and retained stepping stones.

Current FPF already has patterns for archive, pool, front, selected set, parity, refresh, method selection, evidence, autonomy, gate, representation transition, bridge, and mathematical adequacy. The missing piece is a compact problem-side output that lets a practitioner see what is present before P2W receives the problem and which current FPF pattern carries each heavier question.

The first-minute working question is:

> Can I write or review a problem-side record that is specific enough to guide P2W, selection, acceptance, evidence, and first-principles support, while keeping archives, fronts, pools, selected sets, parity, evidence, autonomy, and work planning in their existing FPF patterns?

### C.22.2:2 - Thin First Use and Output Kind

#### C.22.2:2.1 - Thin First-Use Form

The first substantive use of this pattern is the Thin form. It is a practitioner-facing prompt for writing the smallest reviewable problem card, not a demand to complete a field list.

A `ProblemCard@Context` is complete for its current use when it states:

1. why this signal matters now;
2. what problem representation is being carried under which context and scope;
3. why this is not merely a wish, ticket, slogan, or preselected work item;
4. what would count as improvement or an acceptance probe;
5. what the honest next move is.

The Thin form asks for:

- the problem signal or selected-problem cue: what made the practitioner stop before downstream task typing or work selection;
- context grounding and scope cut, including what is outside the current problem;
- the reason this is not merely a wish, slogan, ticket, or preselected work item;
- a provisional improvement check or acceptance probe;
- one honest next move: `P2W-ready`, characterize, compare, search, refresh, retire, archive, `abstain/no-change`, or a named neighboring-pattern exit.

If the Thin form lacks an improvement check or acceptance probe, it may preserve the signal or exit to characterization, comparison, search, refresh, retirement, archive, `abstain/no-change`, or a neighboring pattern, but it must not declare `P2W-ready`.

Only after the Thin pass is legible, recover the output-kind boundary:

`C.22.2 - ProblemCard@Context` is the compact problem-side output under current `C.22`.

`C.22.2 - ProblemCard@Context` is the pattern heading. `ProblemCard@Context` is the `C.22.2`-governed problem-side record shape; an instance is a reviewable problem-side record before P2W. `ProblemCard@ContextRef` may be used as a reference form when downstream text cites such an instance, but it is not a separate durable kind unless a separate naming or kind decision approves one under `F.18` and `A.6.P`. The Tech heading remains `C.22.2 - ProblemCard@Context`. Plain-register glosses or section-local practitioner labels may appear in this pattern, but those labels do not replace the Tech heading.

Local labels in this pattern are local to the `C.22.2` record shape unless a separate accepted FPF naming or kind decision assigns them a broader FPF kind or authority. This includes `support posture`, `validation boundary`, `risk posture`, `solvability band`, `P2W-ready`, `reviewable`, `sentToNeighbor`, `stale`, `refreshed`, `retired`, `archived`, `abstain/no-change`, and `firstPrinciplesCue`; they do not create FPF kinds, gate statuses, state-machine kinds, or local mathematical-lens objects. When a mathematical or first-principles cue is live, cite `C.29`; local `support posture` names only why the problem formulation or structure cue is worth reviewing or moving onward from `C.22.2`; `C.29` carries mathematical-lens adequacy and the support posture for that lens.

Reference labels ending in `Ref` are reference roles, not object names. This includes `ProblemCard@ContextRef`, `setContextRef`, `rivalProblemFormulationRef`, and `semioRelationRef`; do not shorten or promote them into local object kinds such as `ProblemCardRef`, `SetContext`, `RivalFrame`, or `SemioRelation`.

`@Context` means that the card is bound to declared context grounding: a named `U.BoundedContext`, a project-side context reference, or an explicitly bounded practice situation with recoverable local meaning. Domain or practice wording may identify the informative locus of the problem, but it does not replace context grounding. A broad label such as healthcare, education, engineering, research, or operations is not context grounding by itself. When domain or practice wording carries semantic load, recover the named bounded context, project-side context reference, or explicit bounded practice situation and state what local meaning or rule is being used. The card does not assert global problem identity outside that declared context grounding.

Plain gloss for `P2W-ready`: problem-side input ready. It means ready as input to downstream P2W or selector reasoning, not ready to execute work, pass a gate, or select a method.

#### C.22.2:2.2 - Required Solution Moves

The `C.22.2` Solution is organized around practitioner moves from signal to reviewable problem to one admissible next move, not around schema completion.

1. Capture the symptom, anomaly, risk, stakeholder cue, drift, hypothesis, or other source signal before naming the problem.
2. Stabilize the cheap problem-side record: context grounding, scope cut, described entity when load-bearing, primary viewpoint or role concern, and provisional problem framing.
3. Make action possible by separating the symptom detector, improvement check, candidate acceptance basis, optimization target when live, monitored risk signal when live, and proxy-distortion risk when an indicator can be gamed or substitute for value; then state mandatory constraints, risk posture when live, and intended next move before downstream selection.
4. Pay only for live complexity: add conditional fields only when their relation is live, and otherwise name the neighboring-pattern exit or stop at the lighter card.
5. Run the representation-continuity check: if the problem formulation changes the described entity, representation scheme, diagram, functional description, or TGA path reading, name the SEMIO exit before using inherited support.
6. Close by the honest next move rather than by a completed form. A filled card without a truthful next move is not a successful `C.22.2` result.

Cheap-stop rule: the smallest card that gives a truthful next move is sufficient. A conforming `C.22.2` use must not require heavier fields merely because the full field list exists.

First practitioner pass before neighboring exits:

1. Capture the problem signal or selected-problem cue, context grounding, and scope cut.
2. State why it is not merely a wish, slogan, ticket, or preselected work item.
3. State the provisional improvement check or acceptance probe.
4. Choose the honest next move.
Use the neighboring-exit aid only when a conditional relation is live.

This is the Thin-form writing order, not a completion sequence for the whole pattern. It adds no fields; it keeps the practitioner on the smallest truthful card before Standard or High-load relations are paid for.

#### C.22.2:2.3 - Neighboring-Exit Aid

Use this exit aid when a live relation appears while writing or reviewing a `ProblemCard@Context`.

Neighboring exits are authority boundaries, not orchestration steps. The aid names the receiving pattern where authority already lives; it does not give `C.22.2` authority over that pattern or make the neighboring relation local to the card.

Cue and abductive-entry boundary: use `C.22.2` only when the cue can be scoped as a problem-side representation with an improvement check, acceptance probe, or honest next move. If the material is still only a partly stated cue, several candidate meanings, or an explanation-ready prompt without problem-side scope, preserve it under `A.16.1`, `B.4.1`, or `B.5.2.0` before forcing `ProblemCard@Context`.

When `A.16.1`, `B.4.1`, or `B.5.2.0` has preserved or typed the cue, `C.22.2` may receive that cue only to stabilize one problem-side record with context, scope, improvement check or acceptance probe, and honest next move. It does not replace cue preservation, entry-load typing, or abductive prompt handling.
Failure mode: receiving-table over-capture. The practitioner spends the pattern use classifying neighboring patterns, or trying to fill every receiving-pattern column, while the problem signal, context grounding, scope cut, not-wish reason, improvement or acceptance probe, and honest next move remain unstable.

Repair: return to the Thin problem-side action. State the signal, context and scope, why this is not merely a wish, ticket, slogan, or preselected work item, the improvement check or acceptance probe, and the honest next move. Use the exit aid only after that Thin record exposes a live relation that needs a receiving pattern.

| Live relation | Receiving pattern | Permitted local cue or reference | Forbidden local decision |
|---|---|---|---|
| Characterization or measurement basis | `C.16` | Characterization basis, measurement cue, or current reason characterization is not live. | Measurement admission, full characterization protocol, or comparison authority. |
| Characteristics, indicators, scale, unit, or polarity | `A.19` | Characteristic or indicator cue, indicator role, and needed scale or polarity reference. | Indicator admission, scale repair, unit discipline, or characteristic ontology. |
| Q-bundle or multi-characteristic acceptance basis | `C.25` | Q-bundle cue, acceptance-basis cue, or need for multi-characteristic treatment. | Local Q-bundle definition, acceptance settlement, or quality scalarization. |
| Parity, comparability, comparator, budget, or window | `G.9` | Parity basis reference, comparator or window cue, or explicit reason parity is not live. | Fair-comparison claim or parity result. |
| Selected set, shortlist, archive, pool, front, or set-return | `G.5`, `C.18`, `C.19`, `G.11`, `A.6.P:7a`, `C.16.Q` | `setContextRef`, source set kind, selection or retention basis, and non-scalar next move. | Portfolio or archive governance, selected-set authority, single winner, or one readiness score. |
| Local choice among explicit options | `C.11` | Local choice cue and option-set reference when the live issue is choice rather than problem-card completion. | Choice record, chooser authority, or option evaluation. |
| Method-family selection or method cue | `G.5`, `E.18`, `A.15` | Method-family cue and reason method selection is not yet local work. | Method selection, method description, or selected method authority. |
| Work planning, performed work, or result record | `A.15`, `A.10`, `G.6`, `B.3` | Work need, performed-work cue, result-record cue, or work-authority exit. | Work plan, work authorization, performed-work record, or result certification. |
| Evidence need or evidence-looking source | `A.10` | Evidence cue, support posture, source reference, or evidence exit. | Evidence proof, evidence sufficiency, or self-evidence. |
| Provenance or source lineage | `G.6` | Provenance cue, source reference, or relation to a provenance record. | Provenance claim or lineage certification. |
| Assurance, safety reliance, or confidence | `B.3`, with `A.10` or `G.6` when support is live | Validation boundary, support posture, and assurance exit. | Assurance claim, safety-case acceptance, confidence marker, or proof. |
| Gate passage or gate decision | `A.21` | Gate cue, gate need, or relation to a gate record. | Gate passage, gate decision, release permission, or work authorization. |
| Autonomy permission or autonomy budget | `E.16` | Autonomy cue, autonomy risk, or need for autonomy governance. | Autonomy permission, autonomy budget, or delegated authority. |
| Refresh, expiry, stale signal, or unknown handling | `G.11` plus the affected receiving pattern | Freshness or expiry disposition, unknown handling, refresh, retire, bounded-use, or `abstain/no-change` cue. | Silent current validity after expiry or unknown-blocked P2W readiness. |
| Temporal claim: speed, cadence, recovery, adoption, lead time, rhythm, or learning rate | `C.27` | Temporal cue and reason it changes the next move. | Intervention model, trend-as-proof, or effort or rhythm doctrine. |
| Cause-theory, intervention, counterfactual, responsibility, or expected effect | `C.28` plus support or evidence patterns when live | Cause-theory cue that focuses formulation. | Causal-use claim, causal evidence, or transfer license. |
| Agentic call planning or safe probe | `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, `B.3` as applicable | Probe need, call-planning cue, risk posture, and authority exit. | Tool-call permission, delegation authority, world-affecting action, or safety reliance. |
| Representation transition or changed described entity | `A.6.3.RT`, `A.6.4`, `E.17`, `E.18` | `semioRelationRef`, representation-change cue, and support-inheritance boundary. | Same-entity proof or inherited support by wording continuity. |
| Retargeting | `A.6.4`, `E.18` | Retargeting cue and current described-entity boundary. | Claim that the old and new target are interchangeable. |
| Bridge, cross-context reuse, same, equivalent, or aligned wording | `F.9`, `E.17`, `E.18` | Bridge cue, context grounding, loss or congruence need. | Equivalence, alignment, or reuse authority by label alone. |
| Structural reinterpretation | `E.18`, with `C.29` when mathematical structure is live | Structural-reinterpretation cue and receiving-pattern exit. | Local proof that the reinterpretation preserves the problem. |
| Structure cue that improves formulation, including first-principles or mathematical structure when live | `C.29` | `firstPrinciplesCue`, candidate structure, practical formulation payoff, preserved and lost structure when live, support posture, and stop condition. | Mathematical adequacy proof, formalism choice, method selection, or decorative mathematics. |

#### C.22.2:2.4 - Use Boundaries and Profiles

Use this pattern when a signal, anomaly, drift, risk, hypothesis, or stakeholder pressure has appeared and the team must decide whether a problem-side record is needed before downstream task typing. Also use it when P2W would otherwise receive a slogan, wish, ticket-shaped task, preselected work item, or solution-shaped task; when the method is unknown, contested, or not specific enough for task typing, method-family selection, or work planning; or when the problem must become reviewable before method selection or P2W can honestly receive it.

Do not use this pattern as a work-planning record. If the method is already accepted and only work planning is live, use `A.15`. If evidence, proof, provenance, or assurance is central, use `A.10`, `G.6`, or `B.3`; `C.22.2` may name only a support cue or support posture. If gate passage or a gate decision is central, use `A.21`; `C.22.2` may name only a gate cue or neighboring exit. If the live issue is a local choice among explicit options, use `C.11` rather than treating the choice as problem-card completion. If archive, front, pool, selected-set, or portfolio governance is central, use `C.18`, `C.19`, or `G.5`; `C.22.2` may only preserve the `setContextRef` or set-source cue needed for the singleton problem-side record. If the conversation is only ordinary discussion with no downstream project-side move, do not use `C.22.2`.

Use profiles:

- Thin profile: signal, context grounding and scope cut, not-wish, not-slogan, not-ticket, or not-preselected-work reason, provisional improvement check or acceptance probe, and one honest next move.
- Standard profile: the Thin profile plus live fields needed when P2W or selector-facing use is likely: comparison-and-acceptance cue or acceptance-basis reference, mandatory constraints, risk posture, support posture, validation boundary, freshness or expiry, unknown handling, and named neighboring exits.
- High-load profile: conditional for public, disputed, high-risk, set-derived, cross-context, source-transfer-transformed, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, or Part-G-facing cases. It adds references and exits such as `setContextRef`, characterization, parity, support, evidence, gate, autonomy, work, temporal, causal, agentic call-planning, episteme/publication/source-transfer relation, and refresh references; it does not locally certify those relations.

Thin is not an immature profile. When it gives the honest next move, Thin is a final conforming result for the current use. High-load is not a higher maturity claim; it is a conditional profile required when public, disputed, high-risk, set-derived, cross-context, source-transfer-transformed, evidence-adjacent, autonomy-adjacent, gate-adjacent, agentic, or Part-G-facing relations are live in the case.

The profile order is a reading aid, not a required transition sequence. Thin is the default entry; Standard and High-load add only liveness-triggered fields; neighboring exits are consulted after the Thin next move exposes a live relation.

Stop at Thin when the honest next move is local stabilization, local characterization, source reread, or another early problem-side clarification before P2W readiness is claimed. Stop at Standard when it is sufficient to emit or bind a minimal `TaskSignature`, `TaskKind`, or `ProblemProfile` for downstream selector-facing use without carrying high-load relations locally. Exit immediately instead of continuing the card when the live issue is work, evidence, provenance, assurance, gate, autonomy, bridge, representation transition, retargeting, structural reinterpretation, causal-use claim, temporal claim, agentic call planning, or refresh.

#### C.22.2:2.5 - Field Labels and Liveness

The governed move is to make one problem usable before P2W by stating these field labels when they are live for the case:

- problem signal;
- source signal basis: prior solution-use evidence, environmental drift observation, new constraint, new environment, underused capability, opportunity-like cue, risk signal, anomaly, hypothesis, stakeholder signal, accepted local theory, or safe-probe or environment cue;
- domain or practice locus when helpful, plus the context grounding that carries local meaning;
- described entity or exact project-side FPF kind or reference when load-bearing;
- context grounding;
- primary viewpoint or role concern;
- scope cut;
- symptom detection;
- problem hypothesis or cause-theory cue;
- rival-frame reference when multiple plausible problem frames remain live;
- improvement check;
- comparison-and-acceptance cue or acceptance-basis reference;
- characterization basis;
- characteristic or Q-bundle basis;
- indicator selection;
- comparability or parity basis, or explicit current reason it is not needed;
- mandatory constraints;
- risk posture;
- support posture;
- validation boundary;
- freshness or expiry condition;
- unknown handling;
- `setContextRef` when a set, pool, front, archive, shortlist, selected set, or portfolio context is live;
- `firstPrinciplesCue` for a first-principles or mathematical structure cue that changes problem formulation;
- neighboring-pattern exit.

Field liveness for `C.22.2` is determined as follows:

| Field liveness class | Required treatment |
|---|---|
| Always-core problem-card identity fields | State the problem signal or selected problem cue, context grounding, described entity when load-bearing, scope cut, and the current reason this is not just a wish, slogan, ticket, or preselected task. |
| Conditional-live fields | State source signal basis, domain or practice locus when helpful plus the context grounding that carries local meaning, viewpoint or role concern, symptom detection, problem hypothesis or cause cue, rival-frame reference when multiple plausible frames remain live, improvement check, comparison-and-acceptance cue or acceptance-basis reference, characterization or comparability basis, characteristic or Q-bundle basis, indicator selection and indicator role, mandatory constraints, risk posture, support posture, validation boundary, freshness or expiry, unknown handling, `setContextRef` or set-source cue, first-principles cue, and accepted `SEMIO-03` relation exit when that relation affects reviewability. |
| Exit-only fields | Evidence proof, gate passage, autonomy control, method selection, work planning, performed work, result record, and result measurement are not problem-card fields. `C.22.2` may carry only the cue or exit that sends the practitioner to the receiving pattern. |

Field absence rule: if a conditional relation is not live, the field is absent, not `unknown`. Use `unknown` only for a live relation whose value is currently unknown. If a live value is unavailable, state whether the next move is blocked, degraded, sandboxed, or sent to the receiving pattern. If a value is stale, use the freshness or expiry disposition in `C.22.2:12` and `G.11`. If a field is intentionally omitted, state the record-budget reason and do not imply that the omitted relation has been checked. Exit-only material is never completed locally; it is named as cue, reference, or exit. This split is part of the local answer. A minimal `ProblemCard@Context` contains the always-core fields; conditional fields are added when live; exit-only material is named as a neighboring-pattern exit instead of being absorbed into the card.

When the card compares options, selected-set members, retained candidates, or rival problem formulations, it must state the live comparison or parity basis, or state why comparison is not live for the current move. Absence of a parity basis is not automatically a defect; it is a disposition. The admissible result is either parity not live for the current card, or exit to `G.9` before `P2W-ready` is claimed. A local fair-comparison result or selected-set result is not admissible inside `C.22.2`.

A conforming `C.22.2` use includes minimal source and context witness material when source, set, selection, characterization, parity, freshness, or semio relation is live. Otherwise a Thin card may cite the observed signal in plain form. The field-group label `problemCardSource` may be used inside the pattern, but it is not a new FPF object and not an evidence graph. It is a recoverability field group for the source and neighboring references that make the problem-side record reviewable:

```text
problemCardSource:
  sourceSignalRef?
  setContextRef?
  selectionOrRetentionBasis?
  characterizationBasisRef?
  parityBasisRef?
  freshnessRef?
  semioRelationRef?
```

Generated problem variants, evaluator feedback, and open-ended problem mutation may be recorded only as `sourceSignalRef`, `selectionOrRetentionBasis`, or `setContextRef` when they make the problem-side record reviewable. They do not provide problem authority, evidence sufficiency, or permission to probe or act.

#### C.22.2:2.6 - Anti-Pattern Checks and Worked Slices

Anti-pattern checks begin with card-as-work-item: treating the card as work to execute while the method remains unselected is non-conformant. Filling every field merely to satisfy the form is also non-conformant; fields are required only by liveness, profile, and next-move need. Declaring `P2W-ready` from signal and scope alone is non-conformant when no improvement check or acceptance probe is present.

A preselected solution or work item such as "implement X" is non-conformant as a problem card unless a problem-side signal, context, scope, and candidate acceptance basis are recovered. Evidence, provenance, assurance, gate, and autonomy references inside the card are non-conformant if they are read as proof, gate passage, safety acceptance, or permission instead of a cue, reference, or exit to the receiving pattern.

Treating a problem portfolio, archive, pool, front, shortlist, or selected set as a task queue inside `C.22.2` is non-conformant; the card may only preserve `setContextRef` or a set-source cue and exit. Replacing Goldilocks, NQD, OEE, set-return, partial-order, or stepping-stone reasoning with one readiness score is non-conformant. A first-principles or mathematical cue without practical payoff, preserved and lost structure when live, support posture, and stop condition is non-conformant.

A conforming `C.22.2` use is testable against at least one Thin worked slice, such as repeated task rework or another compact source signal, showing signal, context, not-preselected-work reason, improvement check, and next move. It is also testable against at least one High-load worked slice from a set, archive, pool, front, shortlist, selected set, or portfolio context, showing `setContextRef`, candidate acceptance basis, risk posture, and neighboring exits without creating a local portfolio or archive kind.

#### C.22.2:2.7 - Conformance Checklist Requirements

Checklist role boundary: this checklist protects against overread after the practitioner has written or reviewed the card. It is not the writing order, not a mandatory field-completion sequence, and not a gate. The writing order remains Thin form, honest next move, and live exits only when their relation is live.

| Check | Required test |
|---|---|
| Name and kind identity | A conforming `C.22.2` use keeps the pattern heading as `C.22.2 - ProblemCard@Context` and treats the governed output as a problem-side record shape, not `U.Problem`, `TaskSignature`, `U.WorkPlan`, an evidence object, a gate object, or an autonomy object. |
| Pattern scope boundary | A conforming `C.22.2` use does not present a complete problematization methodology, process model, method model, or work model. It governs the problem-side record before P2W; method, work, evidence, gate, autonomy, organization-capability, and other heavier concerns exit to the receiving patterns named for this pattern. |
| No new `U.` kind | A conforming `C.22.2` use does not introduce `U.ProblemCard@Context`, `U.ProblemCard`, or another `U.`-prefixed problem-card kind. `ProblemCard@Context` remains the `C.22.2`-governed problem-side record shape used by this pattern. |
| Core card identity | A conforming `ProblemCard@Context` states the problem signal or selected-problem cue, context grounding, scope cut including outside scope, described entity when that entity is load-bearing, and the current reason the record is not merely a wish, slogan, ticket, or preselected work item. |
| Cue, reference, and exit discipline | A conforming `C.22.2` use marks heavy neighboring relations as cue, reference, or exit rather than local governing content. Support posture, validation boundary, gate need, evidence need, `setContextRef` or set-source cue, work need, autonomy cue, refresh need, and semio relation may be named only in the role that sends the practitioner to the receiving pattern or preserves the needed reference. |
| No pre-binding by card | A conforming `ProblemCard@Context` does not by itself select a method, plan work, record performed work, pass a gate, prove evidence, grant autonomy, or select a solution. It may mention a work need, but it does not create a WorkPlan-shaped `PlanItem`. It may name only the problem-side cue, reference, or neighboring-pattern exit needed before those relations are handled elsewhere. |
| `P2W-ready` basis | A conforming `ProblemCard@Context` marked `P2W-ready` states an improvement check or acceptance probe and the intended downstream move. `P2W-ready` means sufficient problem-side record for downstream P2W or selector-facing use; it is not work-authorized, not gate-passed, and not method-selected. If that basis is absent, the card may remain reviewable or exit elsewhere, but it must not claim `P2W-ready`. |
| Readiness disposition | A conforming `ProblemCard@Context` states whether it is reviewable-only, `P2W-ready`, or sent to a neighboring pattern. A reviewable-only card must not bind `TaskSignature`. |
| Minimal downstream anchor | When `ProblemCard@Context` emits or binds `ProblemProfile`, `TaskKind`, or `TaskSignature`, a conforming result keeps the downstream `C.22` object minimal and selector-facing. It must not copy the full card fields into `TaskSignature` or make the downstream anchor a work plan. |
| Source-local term recovery | A conforming `C.22.2` use treats source-local terms such as problem factory, solution factory, passport, rule-of-choice card, evidence pack, autonomy budget, logs, gates, and portfolio wording as ordinary source wording or maps them to named receiving patterns. It must not mint them as `C.22.2` subkinds. |
| Acceptance and comparability exits | A conforming `ProblemCard@Context` may state an acceptance probe, candidate acceptance basis, comparison-and-acceptance cue, or acceptance-basis reference, but it does not create local acceptance authority. It sends comparison-frame or CG-Spec governance to `G.0`, acceptance clauses and threshold predicates to `G.4`, parity or comparability questions to `G.9`, and characterization, characteristic, indicator-admissibility, or Q-bundle basis to `C.16`, `A.19`, or `C.25` when those relations are live, instead of settling that basis locally. |
| Detector, check, criterion, and optimization-target distinction | A conforming `ProblemCard@Context` distinguishes symptom detector, improvement check, candidate acceptance basis, optimization target, monitored risk signal, and proxy-distortion risk when those relations are live. A measured value or observed improvement is not by itself an acceptance result for P2W. |
| Set-source reference preservation | When a `ProblemCard@Context` comes from an archive, pool, front, shortlist, selected set, or portfolio, a conforming card cites the existing receiving pattern such as `C.18`, `C.19`, or `G.5` when the set relation is live, preserves `setContextRef` and the selection or retention basis, and does not turn that reference into a new `C.22.2` portfolio or archive kind or task queue. |
| Causal cue boundary | A conforming `ProblemCard@Context` treats local cause-theory wording as a formulation cue unless a causal-use claim is explicitly made. Any causal-use claim exits to `C.28` and the needed support or evidence pattern when live; a local cause-theory cue is not evidence of cause and does not license causal transfer by itself. |
| Temporal claim exit | If speed, cadence, throughput, recovery, adoption, learning rate, review rhythm, lead time, freshness window, or expiry wording changes the next move, a conforming `ProblemCard@Context` names the temporal claim and exits to `C.27`. The card may preserve the cue; it does not turn a trend, cadence note, or freshness field into an intervention model. |
| Representation-relation exit | When representation transition, retargeting, bridge, structural reinterpretation, or changed described entity is live, a conforming `ProblemCard@Context` names the receiving relation in `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` as appropriate. Wording continuity is not same-entity proof, and the card must not inherit support across the changed representation by wording continuity alone. |
| Posture and authority boundary | A conforming `ProblemCard@Context` keeps support posture, validation boundary, risk posture, and next move as problem-side fields or neighboring exits. Support posture means the current reason the problem formulation is worth reviewing or moving onward. It is not a confidence marker, evidence sufficiency, evidence proof, provenance, assurance claim, engineering justification, gate passage, safety-case acceptance, release permission, autonomy permission, or work authority. Validation boundary is not an assurance claim or safety-case acceptance; risk posture is not autonomy permission; next move is not work authority. |
| Support-posture citation boundary | A `ProblemCard@Context` citation is non-conformant if it is used as evidence, gate passage, safety acceptance, assurance, release permission, autonomy permission, or work authorization without naming the receiving pattern record that carries that relation. |
| Freshness and unknown disposition | A conforming `ProblemCard@Context` states whether freshness and unknown handling permit the intended use, require bounded or degraded use, require `abstain/no-change`, require sandbox treatment, require refresh, or block P2W. Expiry or unknowns may not remain as passive notes. |
| Record-budget invariant | A conforming `ProblemCard@Context` is as small as the next move permits. A Thin card is valid when it prevents wish, ticket, or solution-shaped-task collapse and names the next move honestly. The full field set is used only when the corresponding relation is live. |
| No scalar readiness shortcut | A conforming `ProblemCard@Context` does not turn Goldilocks, NQD, OEE, set-return, partial-order, or stepping-stone wording into one local readiness score or a local QD or OEE vocabulary. Those terms may appear only as cue or exit to the current receiving patterns when their relation is live. |
| First-principles and mathematical cue payoff | A conforming first-principles or mathematical cue states the practical payoff for problem formulation, the preserved and lost structure when live, the support posture, and the stop condition or `C.29` exit. A cue without those recoverable elements is not load-bearing action guidance. |

Do not treat a compact card template or worked example as a separate FPF object or pattern.

### C.22.2:3 - Problem Reading and Kind Recovery

For this decision, `problem` remains an ordinary word in non-load-bearing prose. Recovery is required only when the wording changes an admissible move, FPF relation, downstream anchor, support, evidence, causal, bridge, assurance, decision, admissibility load, or neighboring-pattern exit. The preferred center is the framed problem representation: a problem-side representation of a described entity under context, scope, viewpoint or role concern, constraints, and improvement or acceptance probe. When `problem` carries FPF work, selection, evidence, causal, bridge, assurance, decision, or admissibility load, it must be recoverable through this table:

| Load-bearing reading | Current FPF reading | `C.22.2` disposition |
|---|---|---|
| Symptom, anomaly, deviation, risk signal, or stakeholder signal | Problem signal or source signal basis | May trigger a `ProblemCard@Context`, but is not yet a problem-side representation by itself. |
| Problematic situation | Context-bound situation under a viewpoint, domain, constraints, risks, and candidate described entity | Captured only through fields that make the situation reviewable. |
| Framed problem representation | Problem-side representation of a described entity under context and acceptance constraints | Center of `ProblemCard@Context`; representation-change claims exit to `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` when live. |
| Candidate problem in archive or live pool | Member of a retained candidate set, pool, archive, or front | Must preserve source set or reference, declared set relation when that exact FPF relation is live, retention basis, budget or window, and review cadence when live. |
| Selected problem from a set-return treatment | Selected set member or emitted problem-side record under selection basis | `ProblemCard@Context` may carry the selected problem, but selected-set semantics remain with `G.5`, `C.18`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. |
| Problem ready for selector-facing use | Problem-side record sufficient to emit or bind `TaskSignature` or `TaskKind` | `C.22` use reads the typed anchor; `C.22.2` does not expand `TaskSignature` into a problem-card dump. |
| Downstream task or execution target | Method known enough for task typing, method-family selection, planning, or performed work | Exits to `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, gates, or evidence patterns as applicable. |
| E.8 pattern `Problem frame` | Practitioner-recognition section inside a pattern | Not the C.22 problem-side representation. |
| E.9 DRR `Problem frame` | Decision-support section in a design-rationale record | Not the C.22 problem-side representation. |

Blocked readings: `ProblemCard@Context` is not `U.Problem`, not `ProblemProfile`, not `TaskSignature`, not `TaskKind`, not `U.WorkPlan`, not `U.Work`, not the problem-side representation itself, not a general ticket format, not an archive, not a portfolio, not an evidence object or proof, not a gate decision or gate passage, and not an autonomy object or work-plan item.

### C.22.2:4 - Problem, Task, Method, Work, and Result Split

`ProblemCard@Context` is admissible while the method is unknown, contested, not yet selected, or not yet specific enough for downstream work. A known method does not by itself make the problem ready: if the proposed method is known but the problem signal, scope, acceptance probe, or described entity remains unstable, `C.22.2` remains live. If both the problem representation and the method are already accepted and the remaining question is planned execution, exit to `A.15`. The card may carry method-search exits and method-family cues, but it must not present downstream work as already known task execution.

Use this split:

| Term or object | Current FPF reading | Local disposition |
|---|---|---|
| `Problem` | Problem-side representation of the described entity of concern under context | Center of `C.22.2` only after problem-kind recovery. |
| ProblemCard@Context | Compact problem-side record before P2W | `C.22.2`-governed record shape under `C.22`; stabilizes a problem-side representation under declared context. |
| ProblemProfile | C.22-facing profile prepared or bound from a problem-side representation when sufficient | Downstream profile anchor; not the card itself and not a work item. |
| `TaskKind` | Selector-facing task kind in `C.22` | Downstream typed anchor; not a plan item. |
| `TaskFamilyRef` | Reference to a family of task kinds or method-consumption classes | Used only when current `C.22` selector logic requires it. |
| `TaskSignature` | Minimal selector-facing signature read for eligibility, acceptance, and selection | May be emitted or bound from `ProblemCard@Context`; must stay minimal. |
| Method-family selection object | Comparison or selection among method families | Receiving pattern `G.5`; not a problem-card field. |
| `U.Method`, `U.MethodDescription` | Method and method description | Receiving pattern family `A.15` and related method-description anchors. |
| `U.WorkPlan`, `SlotFillingsPlanItem` | Planned work and plan item | Receiving pattern family `A.15`; not a C.22 task signature. |
| `U.Work` | Performed work | Receiving pattern family `A.15`, with evidence, provenance, and assurance exits when live. |
| Result record and result measurement | Evidence, provenance, measurement characterization, assurance, or refresh material depending on use | Receiving patterns `A.10`, `G.6`, `B.3`, `C.16`, `G.11`, and neighbors. |

Transition condition: `ProblemCard@Context` may prepare a candidate `ProblemProfile`, bind an existing `ProblemProfile`, emit a candidate `TaskSignature`, or bind a `TaskSignature` only when P2W or selector readiness is declared. If several downstream signatures remain plausible, keep them as candidate signatures instead of binding one chosen `TaskSignature`. When method-family selection, selected method, planned work, performed work, result record, or result measurement becomes live, use the receiving pattern; `C.22.2` does not absorb that pattern's authority.

### C.22.2:5 - Relation to C.22

`C.22` remains the foundation for `ProblemProfile`, `TaskKind`, `TaskFamilyRef`, and `TaskSignature`. `ProblemCard@Context` is earlier and more explicit: it explains why this problem, under this context, is admissible for P2W, search, comparison, characterization, refresh, retirement, or a neighboring exit.

A `ProblemCard@Context` may prepare a candidate `ProblemProfile`, bind an existing `ProblemProfile`, emit a candidate `TaskSignature`, or bind a `TaskSignature` only when P2W or selector readiness is declared. If several downstream signatures remain plausible, keep them as candidate signatures instead of binding one chosen `TaskSignature`.

This relation does not move problem-card field detail into `TaskSignature`. `TaskSignature` stays minimal for eligibility, acceptance, and selection. Method-family selection, selected method, planned work, performed work, result record, result measurement, evidence, gate, autonomy, archive, portfolio, and selected-set authority remain with their receiving patterns.

### C.22.2:6 - Characterization, Indicators, and Comparability

`ProblemCard@Context` must state either a recoverable `characterization basis` and `comparability or parity basis`, or an explicit current reason why the problem can proceed without one.

The heavy content stays with existing FPF patterns:

- `C.16` carries measurement characterization, backing, and comparability discipline;
- `A.19` carries characteristic, scale, unit, polarity, and indicator admissibility discipline;
- `C.25` carries Q-bundles and quality-like multi-characteristic bundles;
- `G.9` carries parity, comparison-window, comparator, budget, unit, repeatability, and reproducibility pins;
- `G.0` carries comparison-frame and CG-Spec governance;
- `G.4` carries acceptance clauses and threshold predicates;
- `G.5` governs selected-set publication when the problem enters a selected set.

Missing characterization or parity basis is a current disposition. The record exits to characterization, parity, or search or pool work under the receiving pattern instead of pretending the problem is ready for P2W.

The `C.22.2` candidate acceptance basis must distinguish functional check, constraint compliance, risk or safety boundary, parity or comparison basis, and freshness window when those relations are live. Comparison frame, CG-Spec, or comparability governance exits to `G.0`. Acceptance clauses and acceptance threshold predicates exit to `G.4`; `C.22.2` may name only the need, cue, or reference. Passing a test, improving one observed indicator value, or naming an acceptance phrase is not by itself admissible acceptance for P2W.

### C.22.2:7 - Source Record-Form Receiving Map

These are source-form recovery rows, not a taxonomy of FPF forms or `C.22.2` subkinds. This map keeps source wording from becoming local `C.22.2` subobjects. A form may enrich the problem card only when it supplies problem-side source, set, characterization, or comparison material. Authority, evidence, gate, autonomy, work, method, and result forms remain neighboring exits.

Problem-side and set-source forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Problem card | Carried by this pattern. | Use `C.22.2 - ProblemCard@Context`. |
| Problematization passport | Absorbed as the compact support template inside `C.22.2`. | Do not mint a new FPF object. |
| Problem archive | Assigned to archive, pool, and provenance patterns. | Use `C.18`, `C.19`, `A.10`, and `G.6`; do not create a local portfolio or archive kind in `C.22.2`. |
| Problem portfolio | Assigned to selected-set, pool-policy, parity, and refresh patterns. | Use `G.5`, `C.19`, `G.9`, and `G.11` according to the live relation. |
| Selected set, shortlist, front, archive, pool, or Goldilocks source | Preserved only as source or set-source cue. | Use `setContextRef`, source set kind, source-set form, selection or retention basis, non-scalar next move, and the receiving pattern when live. |
| Solution search | Assigned to archive, pool, or selection patterns according to state. | Use `C.18`, `C.19`, `C.11`, or `G.5`; `C.22.2` names only the search exit. |
| Solution portfolio | Assigned to selected-set, archive, front, and method-family selection patterns. | Use `G.5`, `C.18`, `C.19`, and `G.9`; `C.22.2` only carries the candidate acceptance-basis reference and set-return exits that make downstream solution selection reviewable. |

Comparison and characterization forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Characterization passport | Assigned to characterization and comparison patterns. | Use `C.16`, `A.19`, and `C.25` where live; `C.22.2` cites the basis. |
| Characteristic card | Assigned to characteristic and scale discipline. | Use `A.19` and `C.16`; problem-card use appears through `indicator selection` and `characteristic or Q-bundle basis`. |
| Parity plan or report | Assigned to parity harness. | Use `G.9`; `C.22.2` names the need for parity only as a neighboring-pattern exit. |
| Rule-of-choice card | Assigned to local choice or selected-set patterns when a chooser and option set are live. | Use `C.11` for local choice records; use `G.5` for selected-set publication and `C.19` for pool policy. |

Neighboring authority, evidence, work, method, and result forms:

| Source record form | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| ADR-like decision record | Assigned by the decision being recorded. | Use `E.9` for FPF content decisions, `C.11` for local choice records, and `A.21` for gate decision logs. |
| Evidence pack | Assigned to evidence, provenance, and assurance patterns. | Use `A.10`, `G.6`, and `B.3`; `C.22.2` names support posture and validation boundary without certifying evidence. |
| Autonomy budget declaration | Assigned to autonomy governance. | Use `E.16`; `C.22.2` carries only risk or autonomy cues that point to this pattern. |
| Autonomy ledger | Assigned to autonomy, work, and gate patterns. | Use `E.16` with `A.15` and `A.21` when work or gates are live. |
| Gate decision log | Assigned to gate decision recording. | Use `A.21`; if the same record also carries evidence or provenance load, that load exits to `A.10`, `G.6`, or `B.3`. |
| Override protocol | Assigned by the live autonomy, gate, work, evidence, or control relation. | Use `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` as applicable. Use `A.2.8` only when an explicit deontic relation is live. |
| Deontic commitment, permission, or obligation | Assigned only when the commitment, permission, or obligation is explicit. | Use `A.2.8`; do not apply it to logs or override-looking wording by appearance. |
| Method selection | Assigned to method-family selection. | Use `G.5` and `A.15`; `C.22.2` carries only method-family cues. |
| Work planning | Assigned to work-planning patterns. | Use `A.15` and `SlotFillingsPlanItem`; not `TaskSignature`. |
| Performed work | Assigned to work, evidence, and provenance patterns. | Use `A.15`, `A.10`, `G.6`, and `B.3` according to use. |
| Result record and result measurement | Assigned to evidence, provenance, assurance, measurement characterization, and refresh patterns. | Use `A.10`, `G.6`, `B.3`, `C.16`, and `G.11`; `C.22.2` does not certify results. |
| Candidate solution or described system | Assigned to selection, method, work, evidence, and system-description patterns according to live use. | Use `G.5`, `A.15`, `E.17`, `E.18`, `A.10`, `G.6`, and `B.3`; do not treat selected solution publication as the problem card. |
| Runbook and rollback plan | Assigned to work-planning, gate, autonomy, evidence, and control patterns. | Use `A.15`, `A.21`, `E.16`, `A.10`, `G.6`, and `B.3`; `C.22.2` may name reversibility or containment as a risk or validation boundary only. |

Source-local exposition terms:

| Source wording | Current disposition | FPF receiving pattern and content obligation |
|---|---|---|
| Problem factory, solution factory, or factory-of-factories | Source exposition for related work families, not FPF process kinds. | `C.22.2` covers only the problem-side output. Solution and P2W work exits to `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, or `G.11` when those relations are live. |
| Ordinary log | Assigned by the relation the log is used to support. | Use `A.10`, `G.6`, or `B.3` when evidence, provenance, assurance, or support posture is live; use `G.11` when the log supports refresh or update discipline. `C.22.2` may cite the cue, but does not treat a log as problem evidence by appearance. |
| Passport, card, budget, ledger, protocol, plan, and pack wording | Recovered by use, not by label shape. | If the source term carries problem-side material, recover it through the relevant `C.22.2` field. If it carries authority, evidence, gate, autonomy, work, method, result, selection, or assurance load, send that relation to the receiving pattern. |
### C.22.2:8 - Portfolio, Archive, and Set-Return Treatment

Archive, portfolio, pool, front, shortlist, selected-set, and set-return material remain source and set cues for the current problem-side record. `ProblemCard@Context` preserves `setContextRef`, source-set kind, selection or retention basis, and the non-scalar next move when live; portfolio and archive governance stays with the named receiving patterns and does not become a local problem-card kind.

Archive, portfolio, palette, front, shortlist, ranked shortlist, selected set, live pool, and set-return material remain live source distinctions, but their current FPF receiving patterns are already available:

| Source wording | Current FPF receiving pattern | Required problem-card preservation when live |
|---|---|---|
| Problem archive | `C.18`, `C.19`, `A.10`, `G.6` | Preserve source set or reference, retention basis, candidate status, and provenance relation. |
| Problem portfolio | `G.5`, `C.19`, `G.9`, `G.11` | Preserve selection or retention basis, budget or window, review cadence, and selected-set or live-pool relation. |
| Palette | `C.18`, `C.19`, `G.5` | Preserve candidate-family or option-set reading without turning it into evidence or approval. |
| Front | `C.18`, `A.19`, `C.25`, `G.5` | Preserve declared characteristics and non-dominated set reading. |
| Shortlist | `G.5`, with `G.9` when comparison pins matter | Preserve selected-set basis and downstream use. |
| Ranked shortlist | `G.5` only when an admissible order is declared | Preserve ranking basis or narrow to selected set with tie notes. |
| Selected set | `G.5` | Preserve selected-set output, basis pins, and unknown handling. |
| Live pool | `C.19` | Preserve pool policy, current treatment, and change trigger. |
| Set-return | `G.5`, `C.18`, `C.16.Q`, declared comparison records | Preserve set-valued result when total order is not admissible. |

A singleton problem card is the degenerate case. If it came from a portfolio, front, archive, or pool, the selected problem remains traceable through `setContextRef`: the lightweight reference to the source set kind, source reference, selection or retention basis, budget or window, review cadence, and receiving pattern when live. `setContextRef` is a reference field, not a new `SetContext` kind, and is not evidence, gate passage, approval, portfolio object, or work authority.

`setContextRef` must preserve the recoverable source-set form when live: `Palette`, `Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, `SelectedSet`, `LivePool`, or another accepted source-set form. If the source-set form is not recoverable, the card may keep a source cue, but it must not claim selected-set readiness or archive-derived readiness.

When multiple plausible problem formulations remain live, `C.22.2` must not bind one `TaskSignature` prematurely. Each optional `rivalProblemFormulationRef` must state the rival formulation, described entity, context, preserved concern, lost concern, reason not selected yet, and next discrimination move. It is not a `CG-Frame`, not the E.8 `Problem Frame`, and not a representation-frame object.
The next discrimination move may be to characterize, compare, retarget, reopen the source, choose a local problem formulation, or exit to the relation-bearing pattern. Reframing is triggered when context grounding, described entity, viewpoint, scope cut, or cause-theory cue changes the problem representation enough that support or readiness cannot be inherited by wording continuity.

### C.22.2:9 - Goldilocks and Set-Return Docking

Goldilocks problem selection is the problem-side adaptation of the current NQD, OEE, and set-return family. It is not direct QD or OEE vocabulary import, not a new scalar readiness doctrine, not a local QD or OEE vocabulary, and not a single score. `C.22.2` must not mint `GoldilocksProblem`, `GoldilocksScore`, `GoldilocksReadiness`, or any equivalent local kind; Goldilocks remains a readiness and selection reading carried by current receiving patterns.

A Goldilocks, stepping-stone, or archive-derived problem must be represented as source context or set context, selection or retention basis, and current next move, not as problem difficulty, priority, or readiness score.

`ProblemCard@Context` carries only the problem-side readiness fields and exits:

- source set kind when archive, pool, front, shortlist, selected set, or portfolio language is live;
- solvability band;
- characteristic-space, declared problem-side characteristic descriptor, or Q-bundle basis;
- declared difference-reading basis when novelty or diversity is claimed, or an exit to the receiving characterization or comparison pattern;
- non-scalar trade-off, dominance, partial-order, or set-return basis when live;
- measurability or explicit unknown handling;
- reversibility or containment for safe probing when live;
- stepping-stone option value when retention matters;
- expiry or refresh condition;
- selected-set, archive, pool, front, or parity exit when live.

The local `solvability band` label means a context-bound, non-scalar reading of feasible-but-not-trivial fit under current capability, constraints, support, and optional set-return basis. It is not a universal difficulty claim, not a hidden readiness scale, and not a single-score ranking.

If the band is not supported by a characteristic, Q-bundle, comparison, retention, or capability-context cue, treat Goldilocks wording as informal recognition only and send any selection, set-return, or parity claim to the receiving pattern.

The current receiving family is `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. The relation to `C.22:14` is a role and timing relation inside the same family: `C.22.2` uses the family before P2W, while `C.22:14` uses it downstream when candidate solutions for a `TaskKind` make `TaskSignature` informative.

### C.22.2:10 - Structure Cue That Improves Formulation

`C.29` carries the neighboring adequacy check for first-principles or mathematical structure cues used by `ProblemCard@Context`.

`firstPrinciplesCue` is a local cue label for a formulation-changing structure and an exit to `C.29`; it is not a local mathematical-lens kind or a substitute for `C.29` lens adequacy.

The problem card may ask whether a first-principles or mathematical structure helps find or improve the problem formulation, not only whether an already-mentioned mathematical object is admissible. Useful cues include state space, graph, boundary, topology, symmetry, invariant, variational or constrained-optimization structure, probability or information structure, resource bound, obstruction, scale window, composition, or coarse-graining choice.

The admissible practitioner move is:

> State the structure that improves the problem formulation, the preserved structure, the lost structure, the practical payoff, the support posture, and the stop condition.

Distribution by principles:

| Source pressure | Current receiving pattern | `C.22.2` use |
|---|---|---|
| Zero-principles and first-principles invariants, constraints, symmetry, composition, multi-scale description, variational structure, probability or information, and resource limits | `C.29`, with `A.19`, `C.16`, `C.25`, and `G.9` when characteristics, measurement characterization, quality bundles, or parity are live | Carry a first-principles or mathematical structure cue and exit to the receiving pattern. |
| Second-principles method-family implications | `G.5`, `A.15`, `E.18`, `A.19` as applicable | Name the method-family cue; do not perform method selection in the problem card. |
| Third-principles reproducibility, checks, templates, records, logs, rollback, evidence | `A.10`, `G.6`, `B.3`, `A.21`, `G.11`, `E.16` as applicable | Name the reproducibility or evidence obligation as a neighboring-pattern exit. |

When no useful mathematical structure survives, record that absence and proceed without forcing mathematical prose into the problem card.

### C.22.2:11 - Support, Validation, AI-Agent Pressure, and Safe Probing

`ProblemCard@Context` exposes support posture and validation boundary; it does not certify evidence, assurance, gate passage, safety, or autonomy control.

Plain definition: support posture names the current reason this problem formulation is worth keeping, reviewing, discriminating, or moving onward now. Typical bases include an observed signal, stakeholder cost or risk, repeated rework, violated constraint, stale or changed environment, selected-set retention basis, cheap probe value, first-principles structure that changes formulation, or stale but still useful archive or refresh cue. It is not evidence sufficiency, proof, confidence, provenance, assurance, gate passage, safety-case acceptance, release permission, autonomy permission, or work authority.

Plain definition: validation boundary states what has and has not been checked for the current next move, what the current problem formulation may be used for now, what it cannot yet support, and where any validation, evidence, assurance, gate, autonomy, or work claim beyond this local boundary is assigned. It is not an assurance claim, safety-case acceptance, release permission, or work authorization.

Plain definition: risk posture names the monitored risk, risk condition, cost-of-error concern, or containment concern that may change the safe next move. It is not the validation boundary, not the support reason, not evidence of danger by itself, and not permission to probe, delegate, or act.

Local-label boundary: `support posture`, `validation boundary`, and `risk posture` are local problem-card field labels unless a separate accepted FPF decision assigns a different governing kind. When mathematical-lens support is live, cite `C.29` and do not read local support posture as `LensSupportPosture`. When assurance, evidence, or provenance support is live, exit to `B.3`, `A.10`, or `G.6` as applicable.

Detector, check, and optimization-target discriminator:

- symptom detector: what revealed the possible problem; not an acceptance criterion.
- improvement check: what would show that the problem formulation became better.
- acceptance probe: what downstream acceptance may need to inspect; not local acceptance authority.
- optimization target: what a later selector may improve under comparison-governance or selection-governance patterns; not a local method choice.
- monitored risk signal: what may worsen, distort value, or change the safe next move; not proof by itself.
- acceptance authority: carried by `G.4` or another receiving acceptance pattern, not by `C.22.2`.

Reliance-disposition rule for P2W receiving use:

Use this rule when support posture or validation boundary may enter P2W as evidence-like, confidence-like, conformance-like, proxy-like, safety-looking, redress-bearing, or currentness-bearing support. The first C.22.2 move is to keep the result problem-side: name the P2W receiving use, unsupported use, and any live receiving-pattern exit. This rule does not add a default field family to `ProblemCard@Context`. If the Thin card already gives an honest next move and live exits, no additional reliance record is required.

Support role: the disposition table below is a local P2W-reliance recognition and minimum local record aid, and the worked P2W reliance slices are regression/review slices. They are not card field lists, project checklists, or hidden SEMIO state machines. Use them only to state the supported P2W receiving use, unsupported use, and receiving-pattern exit when support posture or validation boundary is actually being relied on. This local section returns the attempted P2W use to the C.22.2 problem-side relation and named receiving-pattern exits; it does not create an extra SEMIO authority or cross-pattern relation vocabulary.

Affordability card: orientation, discussion, or source-finding can remain an ordinary problem-side cue; bounded P2W reliance states the supported receiving use, unsupported use, window, and exit; threshold reliance names the receiving evidence, assurance, gate, autonomy, control, work, temporal, or representation relation instead of making the card larger. Plain wording remains ordinary unless it changes admissible use, support, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

Common wrong first reading: `P2W-ready` means proof, safety acceptance, gate passage, method selection, work authorization, or release permission. First honest entry: keep the result problem-side; name the P2W receiving use and any exact evidence, assurance, gate, autonomy, control, work, temporal, or representation exit when live.

| Attempted P2W use | Local card move | Receiving-pattern exit when live | Forbidden overread |
| --- | --- | --- | --- |
| Support posture is enough for the next P2W receiving use | State `RelianceDisposition=pass` only for the named P2W receiving use, unsupported attempted P2W use, support posture, validation boundary, context, and window. | Open `A.10`, `B.3`, `A.21`, `C.16`, `C.27`, `G.11`, `A.6.3.RT`, or `A.6.4` only when that relation carries part of the support. | Treating `P2W-ready` as proof, safety acceptance, gate passage, method selection, work authorization, portfolio authority, or release permission. |
| Support is useful but narrower than the attempted P2W use | State `RelianceDisposition=degrade`, the narrowed P2W use, the unsupported attempted use, and the stop condition. | Open measurement, evidence, temporal, refresh, representation, or assurance loci only for the live dependency. | Quietly broadening a weak support posture into full P2W readiness. |
| Source, confidence, or validation is stale, conflicted, uncalibrated, or not tied to the live relation | State `RelianceDisposition=abstain` or `RelianceDisposition=evidence-needed`, plus the missing evidence kind or receiving relation and the decision point. | `A.10` for evidence/currentness, `C.16` for measurement or marker support, `C.27`/`G.11` for time, expiry, refresh, or monitoring. | Letting uncertainty become indefinite delay or silent permission to continue. |
| Contest, redress request, changed representation, retargeting, or changed described entity defeats support inheritance | State `RelianceDisposition=reopen`, the relation being reopened, and the card use that is no longer supported. | `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, `E.18`, `A.10`, `B.3`, or another exact relation when the represented problem, evidence path, or support source changed. | Treating an older card as still current merely because its text was preserved. |
| Safety-looking, release-looking, compliance-looking, public-behavior, resource, people/status, autonomy, gate, or control-bearing use is attempted from the card | State `RelianceDisposition=safety-case-required`, `RelianceDisposition=no-supported-current-use`, or a named exit; do not authorize the use locally. | `B.3` for assurance and the minimum reliance safety support record, `A.21` for gate decision, `E.16` for autonomy, `A.15` for work, `B.2.5` only when a controlled object is regulated through a feedback channel, evidence channel, cadence, window, or supervisory/control relation, `A.10`/`G.6` for evidence/provenance. | Reading a problem-side card as safety acceptance, tool-call permission, delegated-agent authority, release permission, work plan, performed work, or control authority. |

Minimum P2W support statement when this rule is live: support posture, validation boundary, `RelianceDisposition`, supported P2W receiving use, unsupported use, currentness or window when relevant, contest or redress path when relevant, and live receiving-pattern exits. Do not copy evidence, gate, assurance, work, autonomy, or control fields into the card unless the card is explicitly naming a live exit to the receiving pattern.

Misuse guard: `RelianceDisposition=abstain` and `RelianceDisposition=degrade` must state the condition for reopening, narrowing, or closing the P2W use; do not use uncertainty to block valid P2W receiving use indefinitely or to hide a full pass behind a narrower label.

False-negative reliance guard: a blocked, abstained, or evidence-needed P2W use is not final if admissible challenge evidence, missing affected-party evidence, changed source, changed representation, or redress can materially change the disposition.

Support-inheritance guard: support does not inherit across representation scheme, episteme-lane view, publication face, described entity, retargeting relation, or source-basis change merely because the same card text, dashboard label, source phrase, support cue, generated explanation, coarsened or redacted rendering, screenshot, or copied approval survived. Use A.6.3.RT, A.6.3.CSC, A.6.4, E.17, F.9, or E.18 only when that relation is live; otherwise keep the local card use bounded.

Positive repaired path: a messy support cue becomes useful when the card states what P2W may receive now, what P2W must not infer, and which exact neighboring pattern carries any evidence, assurance, gate, temporal, representation, autonomy, control, or work relation. A successful result can be `P2W-ready`, degraded P2W use, evidence-needed, refresh, reopen, `abstain/no-change`, or a named neighboring exit; it need not become a bigger card.

Worked P2W reliance slices:

| Slice | Local card move | Boundary |
| --- | --- | --- |
| An archive or portfolio retention cue supports looking at a problem again. | State the support posture, validation boundary, source-set or retention basis, currentness/window, and `RelianceDisposition=degrade`, `RelianceDisposition=evidence-needed`, or `refresh` when the cue is stale or incomplete. | Retention is not proof, safety acceptance, method selection, or work authorization. |
| Confidence-looking support is enough for one reversible exploration step. | State `RelianceDisposition=pass` only for that P2W receiving use, unsupported attempted use, context, window, and stop condition. | The same card does not become full readiness, release permission, or assurance. |
| A problem card is cited as safety acceptance or tool-call permission. | State `RelianceDisposition=safety-case-required`, `RelianceDisposition=no-supported-current-use`, or a named exit to `B.3`, `E.16`, `A.21`, `A.15`, or `A.10`. | `ProblemCard@Context` does not authorize action, autonomy, gate passage, work, or release. |
| A contest, redress request, or changed described entity defeats inherited support. | State `RelianceDisposition=reopen`, the relation being reopened, and which previous P2W use is no longer supported. | Preserved card text does not preserve currentness when representation or evidence changed. |
| A selected-set or portfolio basis is used before P2W. | Keep the set-source, selection, retention, and not-selected disposition as source cues and name the receiving set patterns when live. | The card is not portfolio authority, selected-set proof, or scalar readiness. |

A cause-theory cue may focus problem formulation inside `ProblemCard@Context`. If that cue is used to claim association, intervention, counterfactual, responsibility, expected effect, or causal evidence, the relation exits to `C.28` plus `A.10`, `G.6`, or `B.3` when support, provenance, or assurance is live.

The AI-agent and autonomy material from the source material is received as neighboring pressure:

- autonomy budget and delegated-agent control exit to `E.16`;
- gate decisions and gate logs exit to `A.21`;
- method selection and work execution exit to `G.5` and `A.15`;
- evidence, provenance, and assurance exit to `A.10`, `G.6`, and `B.3`;
- freshness, monitoring, decay, and update triggers exit to `G.11`.

Environment design and safe probing may appear as source signal basis, validation boundary, risk posture, or neighboring-pattern exit. When the next move requires probe planning, autonomy control, gate authority, evidence, assurance, or work authority, an honest card may record `safe-probe-needed` and name `C.24`, `E.16`, `A.21`, or another live receiving pattern; this records a probe need and receiving-pattern relation, not local probe authorization. `C.22.2` does not create a separate problem-environment pattern. If the next move may affect the world, spend resources, call tools, delegate to agents, change an operational state, or require agentic tool-call scouting, tool-call plan selection, checkpoint return, or bounded call plan, `ProblemCard@Context` may only name the probe need. The authority to probe or act exits to `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` when those relations are live.

### C.22.2:12 - Freshness, Expiry, and Unknown Handling

`C.22.2` includes a section-local state and disposition vocabulary for `ProblemCard@Context`; this vocabulary is not a new FPF kind. These labels describe the card's current admissible use; they are not required states in a transition sequence, event kinds, or gate records. The local labels are:

| State or disposition label | Required reading |
|---|---|
| `draftSignal` | A source signal has been captured, but the card is not yet reviewable. |
| `reviewable` | The problem-side record can be inspected, challenged, sent onward, or refined, but it is not necessarily P2W-ready. |
| `P2W-ready` | Local disposition label with plain gloss: problem-side input ready. The problem-side record is sufficient for downstream P2W or selector-facing use; it is not `ReadyForWork`, `GateReady`, `MethodReady`, `AutonomyReady`, or work authorization. |
| `sentToNeighbor` | A live relation has exited to the named receiving pattern. |
| `stale` | Freshness or expiry blocks the intended downstream use until refreshed, retired, or otherwise disposed. |
| `refreshed` | The relevant source, context, characterization, parity, support, or semio relation has been updated enough for the named use. |
| `retired` | The problem-side record should no longer be used as a live problem for downstream work. |
| `archived` | The record is retained under the relevant archive, pool, front, or selected-set pattern without being live for P2W. |
| `abstain/no-change` | No downstream project-side move is selected because the signal is stale, duplicate, already solved, already absorbed, unnecessary, or not worth current downstream work. |

Freshness must name the affected locus: problem signal, context, characterization or parity basis, support or source, set-source reference, or semio relation. For the problem-signal locus, ask whether the original signal is still present, recurring, solved, absorbed, duplicate, unnecessary, or no longer worth downstream work. For context, ask whether the local context or scope cut has changed enough to alter the formulation. For characterization or parity, ask whether measurement, comparison, and parity bases are current enough for the intended next move. For support or source, ask whether cited sources, provenance, and support references are fresh enough for the stated support posture. For set-source reference, ask whether archive, front, pool, shortlist, or selected-set membership and the selection or retention basis are still current. For semio relation, ask whether wording, diagram, functional description, TGA path, bridge, retargeting, or representation change alters the described entity, support inheritance, context grounding, viewpoint or role concern, scope cut, comparison basis, admissible next move, or relation needed for inheritance.

A stale support reference does not always retire the problem; it may send the card to refresh while the problem remains reviewable. A stale problem signal may support refresh, retire, archive, abstain or no-change, or another named neighboring disposition.

Freshness or expiry failure is a current disposition. A stale or unknown-bearing problem card may remain reviewable as a problem-side record, but it does not become P2W-ready unless freshness and unknown handling permit the intended downstream move. A stale problem card does not silently remain admissible for P2W.

When freshness, expiry, or unknown handling fails, the record exits to one of these current dispositions:

- refresh the problem card or its characterization or comparison basis under `G.11`, `C.16`, `A.19`, `C.25`, or `G.9`;
- retire or deprecate the problem-side record under the relevant archive, pool, selected-set, or refresh pattern;
- continue only as explicitly governed bounded-risk use under the relevant authority, evidence, gate, autonomy, or work pattern.

Unknown-handling fields must state whether they permit use, require degraded use, abstention, or sandbox treatment, or make the current problem formulation inadmissible. No P2W, no change, or abstain-for-now may be a successful next move when the signal is stale, duplicate, already solved, already absorbed, unnecessary, or not currently worth downstream work. Before `ProblemCard@Context` emits or binds `TaskSignature`, it must check whether the problem signal is still present and whether prior work has already solved or removed the problem.

### C.22.2:13 - SEMIO Relation and Representation Continuity

The accepted `SEMIO-03` result is part of the current FPF basis. `C.22.2` uses `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, and `E.18` as exits when changed problem formulations, diagrams, functional descriptions, TGA paths, or `PathSlice` examples carry relation load.

Framing is not wording repair. A framing change is live when described entity, context grounding, scope cut, viewpoint, comparison basis, support inheritance, or honest next move changes. SEMIO material is triggered only when wording, diagram, functional description, TGA path, bridge, retargeting, or representation change alters the carried problem-side representation, described entity, support inheritance, context grounding, viewpoint or role concern, scope cut, comparison basis, admissible next move, or live receiving pattern. Ordinary wording cleanup does not trigger a SEMIO exit and does not block a Thin `ProblemCard@Context`.

| Pattern or pattern family | Problem-card relation | SEMIO-03 effect | Current disposition |
|---|---|---|---|
| `C.22` | Relate problem-side record, `ProblemProfile`, and `TaskSignature`. | Changed problem formulations can either preserve the described entity, retarget it, or require a representation-transition witness. | `C.22` carries only the relation and the explicit exit to `A.6.3.RT`, `A.6.4`, `E.17`, `F.9`, or `E.18` when relation load appears. |
| `C.22.2` | Carry the problem-side output. | A problem card may cite transformed representations only with recoverable support posture and the correct relation exit. | `C.22.2` may use SEMIO-03 terms as exits, not as local proof. |
| `C.16` | Characterization and comparability support. | Measurement representation changes can need representation-transition or retargeting checks. | Inherited unchanged; cite as receiving pattern. |
| `A.19` | Characteristics, indicators, scales, units, polarity. | Changing a characteristic representation can change the described entity or comparison basis. | Inherited unchanged; cite as receiving pattern. |
| `C.25` | Q-bundle or multi-characteristic acceptance basis. | Bundle representations must not hide a retargeting or loss. | Inherited unchanged; cite as receiving pattern. |
| `C.29` | First-principles and mathematical structure cue. | Mathematical representations can preserve, coarsen, or retarget the described entity or the problem-side representation. | Inherited unchanged; `C.22.2` uses `C.29` output and semio exits when structure changes entity reading. |
| `C.18` | Archive, front, diversity, stepping-stone retention. | Retained representations must not be treated as the same problem without continuity support. | Inherited unchanged; cite as receiving pattern. |
| `C.19` | Live pool and exploration and exploitation policy. | Pool members may be related variants, retargeted problems, or transformed representations. | Inherited unchanged; cite as receiving pattern. |
| `G.5` | Selected set, shortlist, method-family or selected-set output. | Selection over transformed representations must preserve the declared object of selection. | Inherited unchanged; cite as receiving pattern. |
| `G.9` | Parity and comparability. | Comparators and windows must not silently compare different described entities. | Inherited unchanged; cite as receiving pattern. |
| `G.11` | Freshness, decay, refresh, retirement. | Refresh may preserve, update, or retarget the represented problem under context. | Inherited unchanged; cite as receiving pattern. |
| `A.6.P` and `C.16.Q` | Restore broad source wording and quality wording. | Semio-heavy source terms require kind and relation recovery before use. | Inherited unchanged; cite as receiving pattern. |
| `E.17`, `F.9`, `E.18` | Multi-view, bridge, and structural reinterpretation exits. | They carry the relation work when same-entity continuity, bridge, or reinterpretation is live. | Inherited unchanged; cite as receiving pattern. |
| `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, `A.15` | Evidence, provenance, assurance, gate, autonomy, method, and work exits. | Transformed evidence or work records need the correct relation witness before support is inherited. | Inherited unchanged; cite as receiving patterns. |

`C.22.2` may not treat changed-problem examples as support unless the appropriate accepted FPF relation is named.

### C.22.2:14 - Source and P2W Carry-Forward

The source presentation is not compressed into a generic problem-card summary. The following source details become carry-forward constraints for `C.22.2` use and for the P2W-facing exit from `C.22.2`.

| Source detail | Current FPF reading | `C.22.2` carry-forward or exit |
|---|---|---|
| Source examples: person, team, organization, system, community, episteme, and work project | Source-local recognition examples for the domain or practice locus when that locus helps identify use, and for the described entity or exact project-side FPF kind or reference when load-bearing; not a new FPF kind taxonomy | `ProblemCard@Context` may state the domain or practice locus when it affects time horizon, indicators, cost of error, role concern, or admissible comparison, but it must also state the context grounding that carries local meaning. The listed examples are not minted here as a new taxonomy of FPF kinds. |
| Engineering language for reproducibility and management language for coordination, rights, resources, and responsibility | Verification and reproducibility, and coordination and authority, are different FPF relations | `C.22.2` may name reproducibility, role, budget, right, or responsibility pressure only as a field or exit; gate, autonomy, work, evidence, and authority relations stay with their receiving patterns. |
| Problem factory, solution factory, and factory-of-factories | Source exposition for three related work families, not FPF process kinds | `C.22.2` covers only the problem-side output. Solution and P2W work exits to `G.5`, `A.15`, `E.18`, `A.10`, `G.6`, `B.3`, `A.21`, `E.16`, and `G.11`; organizational-development or platform-capability questions are outside this pattern. |
| Characterization protocol: context or slice, compared set, role or viewpoint characteristics, scale, polarity, measurement method, freshness, repeatability, budget, missing data, and comparison rules | `C.16`, `A.19`, `C.25`, and `G.9` receiving patterns | `ProblemCard@Context` must cite characterization and comparability basis when live; it must not treat available measurement as admitted indicator. |
| Indicator roles: admission constraints, optimization objectives for the current cycle, and risk signals | Characteristic and Q-bundle use under selected comparison or acceptance | `C.22.2` must preserve whether an indicator is a mandatory constraint, an optimization objective, or a monitored risk signal when that distinction affects acceptance. |
| Problem portfolio as period-bounded selected set with budget, role assignment, review cadence, and not-selected disposition | `G.5`, `C.19`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q` | `ProblemCard@Context` must preserve source set or reference, selection or retention basis, budget or window, review cadence, and not-selected or stepping-stone disposition when the set-source relation is live. |
| Goldilocks as zone-of-growth selection calibrated to current capability and context | Problem-side entry to current NQD, OEE, and set-return family | `C.22.2` must not turn Goldilocks into one global difficulty scale or scalar readiness score. |
| Stepping stones as option value: new actions, tools, data, interfaces, environments, or experiment modes that may expand downstream search | Retained archive, front, or pool member, or selected-set reason | `C.22.2` may record stepping-stone value only with a receiving set-return, archive, or pool pattern and a retention or tie-break basis. |
| P2W chain: signatures and principles help select formalism, ontology, characterization, and method-family material | `A.6.0`, `A.6.1`, `C.16`, `A.19`, `C.29`, `G.5`, and `E.18` | `C.22.2` supplies problem-side cues and exits; it does not select the formalism, ontology, mechanism, or method family by itself. |
| P2W chain: condition measurement and comparison help select a concrete method | `C.16`, `A.19`, `C.25`, `G.9`, `G.5`, and `A.15` | State the comparison-and-acceptance cue or acceptance-basis reference and parity and characterization exits needed by downstream method selection. |
| P2W chain: work planning makes planned work inspectable | `A.15`, `A.15.3`, and `SlotFillingsPlanItem` | `C.22.2` may emit or bind `TaskSignature`, but planned work stays in work-planning patterns. |
| P2W chain: performed work produces work-result records | `A.15`, `A.10`, `G.6`, and `B.3` | `C.22.2` must not read performed work or result records as problem-card fields beyond support cues or named exits. |
| P2W chain: result measurement can trigger refresh or return to earlier source material | `C.16`, `G.11`, `A.10`, `G.6`, `B.3`, `C.18`, and `C.19` | `C.22.2` must state freshness or expiry and unknown-handling exits that let downstream result measurement refresh, retire, or re-open the problem-side record. |
| Runbook, rollback plan, canary, SafeStop, error budget, and override protocol | Work, gate, autonomy, evidence, and control records | These source forms are not `C.22.2` subobjects; they are exits to `A.15`, `A.21`, `E.16`, `A.10`, `G.6`, and `B.3` when live. |
| Trust debt after validity expiry | Freshness and decay indicator and bounded-risk continuation question | Treat trust debt as an indicator or support posture cue, not as punishment, proof failure, or gate passage by itself. |

This carry-forward preserves detail, not broader scope. `C.22.2` remains the problem-side output; P2W receives it with enough fields and exits to select method families, plans, performed work, and result measurement without making the problem card a P2W pattern.

### C.22.2:15 - SoTA Decision Support

The following external anchors are adopted or adapted only where they change this pattern's local answer by value.

| Current support line | Anchor | Pattern use | Disposition |
|---|---|---|---|
| Problem framing turns an ill-structured situation into a solvable design problem and requires care because "framing" is ambiguous. | 2025 CEEA paper "Towards a Theoretical Framework of Framing in Engineering Design", `https://doi.org/10.24908/pceea.2025.19713` | Supports deconfliction of symptom, situation, framed problem representation, and task. | Adopted as field and kind-recovery pressure; wording is expressed in current FPF terms. |
| Strategic problem framing distinguishes symptoms and attention allocation from causal problem formulation. | 2025 Organization Science article "Looking at the Trees to See the Forest: Construal Level Shift in Strategic Problem Framing and Formulation", DOI suffix `2024.19134`, `https://doi.org/10.1287/orsc.2024.19134` | Supports the fields for problem signal, problem hypothesis/cause-theory cue, and improvement check. | Adapted; causal claims still exit to `C.28` plus evidence and support patterns when live. |
| QD and OEE work supports collections, fronts, archive retention, set-return, and non-single-winner treatment. | 2026 survey "A survey on Quality-Diversity optimization: Approaches, applications, and challenges", `https://www.sciencedirect.com/science/article/pii/S2210650225003979`; QD-as-MOO anchor `https://arxiv.org/abs/2602.00478` checked 2026-05-20 | Supports set-source-reference and Goldilocks docking into current `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, and `C.16.Q`. | Adopted as field and exit pressure; no local QD or OEE vocabulary or scalar readiness score is introduced. |
| Open-ended coding agents use archives, self-improvement, problem variants, evaluator feedback, and stepping-stone retention. | Darwin Godel Machine `https://arxiv.org/abs/2505.22954`, FrontierSmith `https://arxiv.org/abs/2605.14445`, and AlphaEvolve `https://arxiv.org/abs/2506.13131`, all checked 2026-05-20 | Supports record-form, set-source reference, Goldilocks, safe-probe, and freshness fields and exits for archive, problem generation, safe probes, evaluator feedback, no-change and abstain dispositions, and autonomy and evidence boundaries. | Adapted as recent stress/trend pressure; `C.22.2` is not turned into AI-agent doctrine or an AI-agent management pattern. |
| External AI-agent and autonomy practice increases pressure for evidence, logs, gates, autonomy budgets, and update discipline. | Source presentation plus current FPF autonomy, evidence, and gate patterns | Supports receiving-pattern assignment for support, validation, AI-agent pressure, and safe probing. | Non-load-bearing for the center of `C.22.2`; load-bearing content remains with `E.16`, `A.21`, `A.10`, `G.6`, `B.3`, `A.15`, and `G.11`. |

If a `C.22.2` use carries a wider external claim than these dispositions, the claim is outside this pattern and requires a separate content decision or demotion to a non-load-bearing example.

Each load-bearing SoTA use is recovered as a local test: source idea, FPF invariant, practitioner check, and popular shortcut rejected. A source citation without that local test is not enough to carry pattern authority.

Local SoTA-to-action tests:

| Support pressure | Popular shortcut rejected | Required local result | Reopen condition |
|---|---|---|---|
| Problem framing is ambiguous and abstraction shifts matter. | Symptom, root-cause story, request, or ticket is treated as the problem. | Recover source signal, framed problem representation, context and scope, viewpoint or role concern, improvement check, and rival frame when live. | Reopen when context, scope, viewpoint, rival frame, evidence need, or improvement or acceptance probe changes. |
| P2W receives only a reviewable problem-side record. | `P2W-ready` is treated as work authorization, gate passage, method selection, evidence proof, assurance, or selected solution. | State support posture, validation boundary, readiness disposition, supported P2W use, unsupported use, and named neighboring exit when live. | Reopen when the signal, context, scope, acceptance probe, support posture, validation boundary, freshness, or named exit changes. |
| QD, OEE, and set-return work produce archives, fronts, pools, and selected sets. | Priority score, single winner, local problem portfolio, or local selected-set authority. | Preserve `setContextRef`, source set kind, selection or retention basis, and a non-scalar next move; exit to the receiving set, parity, archive, pool, or refresh pattern when live. | Reopen when the source set, retention basis, parity basis, archive, pool, front, selected set, budget, window, or freshness disposition changes. |
| Open-ended agents, problem variants, evaluator feedback, and stepping stones change source pressure. | Agent output, evaluator trace, or generated variant is treated as authority to act. | Record generator, evaluator, variant, or stepping-stone basis only as a source cue; name support, validation, freshness, and authority exits before probe or action. | Reopen when generator, evaluator, variant, stepping-stone basis, safety/probe condition, or authority condition changes. |
| First-principles or mathematical structure can improve formulation. | A named formalism or mathematical or ontological prestige is treated as adequacy or rigor. | Record the candidate structure, mapping or `C.29` exit, preserved and lost structure when live, practical formulation payoff, support posture, and stop condition. | Reopen when candidate structure, preserved or lost structure, support posture, stop condition, or `C.29` result changes. |
| Early class or kind taxonomy looks available. | A class list or ontology-first taxonomy is treated as the problem formulation. | Keep the formulation question live; record candidate structure, preserved and lost structure when live, and representation or retargeting exits before freezing kind structure. | Reopen when formulation question, kind structure, relation, representation support, or retargeting support changes. |
| Object model looks clarifying. | Object-model clarity freezes the wrong described entity or relation. | Keep described entity and relation reviewable; name representation-transition, retargeting, or bridge exits before inheriting support or readiness. | Reopen when described entity, relation, view, bridge support, or representation-transition support changes. |

### C.22.2:16 - Rationale

`ProblemCard@Context` gives the practitioner one compact problem-side record between vague problem talk and downstream P2W. The card is useful because it is light enough for ordinary use and exact enough to show when comparison, characterization, evidence, selection, mathematical support, method, work, gate, autonomy, bridge, representation transition, or refresh must exit to another FPF pattern.

The card gives the practitioner one thing to write, inspect, and challenge. A practitioner can see whether a problem is ready without first assembling the problem-side record from `TaskSignature`, Q-bundle, parity report, evidence note, selected-set output, and refresh record. At the same time, the card stays outside archive, portfolio, decision, autonomy, work, gate, evidence, bridge, and assurance authority.

The archive and portfolio distinctions remain live when they matter because the card preserves `setContextRef` and exits to the current receiving patterns. Changed problem formulations, diagrams, functional descriptions, or TGA path readings require the accepted representation or retargeting exits before support is inherited. Current SoTA and first-principles cues matter only when they change fields, exits, boundaries, or the problem formulation itself.

### C.22.2:17 - Problem-Card Use Invariants

These invariants govern use of one `ProblemCard@Context`; they do not add card fields.

| Invariant | Required reading |
|---|---|
| One card, one current problem-side representation | One `ProblemCard@Context` instance carries one problem-side representation under one declared context. If the represented problem changes, the card states the changed representation or exits to the representation pattern that carries the change. |
| No hidden companion records | A card may mature, but it does not fork into hidden `TaskSignature`, `WorkPlan`, evidence, gate, autonomy, archive, portfolio, selected-set, or mathematical adequacy records. |
| Heavy relations exit | Evidence, provenance, assurance, gate, autonomy, work, archive, selected-set, comparison, acceptance, representation-transition, temporal, causal, and mathematical adequacy authority stays with the receiving pattern that owns the live relation. |
| `P2W-ready` is problem-side readiness | `P2W-ready` means problem-side input ready, not work ready, not gate-passed, not method-selected, and not evidence-proved. |
| Stale or blocked cards need a disposition | A stale, unknown-blocked, changed-representation, or missing-basis card cannot silently remain `P2W-ready`; it states refresh, retirement, bounded use, `abstain/no-change`, or a named neighboring exit. |
| Smallest truthful card wins | The smallest card that gives an honest next move is sufficient. Full field completion is not required when a Thin card already gives the truthful next move. |

### C.22.2:18 - Misuse Modes and Repairs

| Misuse mode | Non-conforming reading | Repair |
|---|---|---|
| Content creep | The card starts carrying evidence, gate, work, autonomy, or portfolio state instead of cue, reference, and exit relations. | Return the live relation to the receiving pattern and leave only the local cue, reference, or exit in the card. |
| Selector leakage | `ProblemCard@Context` becomes a pre-`TaskSignature`, selects a method family, selects a formalism, creates a work plan, or copies card fields into `C.22` `TaskSignature` by default. | Return to the problem-side record. If downstream readiness is declared, name only a candidate `ProblemProfile`, `TaskKind`, or `TaskSignature` basis and the relation to `C.22`; selector-facing anchor authority stays with `C.22`. |
| Hidden scalarization | Goldilocks or readiness becomes one score instead of a declared set-return, partial-order, descriptor, characteristic, or retention basis. | Preserve `setContextRef`, source-set kind, selection or retention basis, and non-scalar next move; exit to the receiving set, parity, archive, pool, or refresh pattern when live. |
| Silent retargeting | A changed problem formulation changes the described entity, representation scheme, diagram, functional description, or TGA path reading without naming the required relation exit. | Name the representation-transition, retargeting, bridge, structural reinterpretation, or SEMIO relation before inheriting support or readiness. |
| Support overread | Support posture is read as evidence proof, provenance, assurance, gate passage, or safety acceptance. | Treat support posture as the local reason to keep, review, discriminate, or move the formulation onward; evidence, provenance, assurance, gate, and safety reliance exit to their receiving patterns. |
| Refresh dead end | Expiry or unknown handling is recorded, but no current disposition is made. | State refresh, retirement, bounded use, `abstain/no-change`, or the named neighboring exit before claiming `P2W-ready`. |
| Cognitive overload | Every field is treated as mandatory and the card becomes form-compliance work. | Return to Thin use: signal, context and scope, reason the record is not a wish, ticket, slogan, or preselected work item, improvement check or acceptance probe, and honest next move. |

### C.22.2:19 - Use-Quality Checks

A practitioner checking one `ProblemCard@Context` use should be able to find these results in the card, its stated next move, and its named exits. These checks protect use quality; they do not add fields to the card.

| Use-quality check | Practitioner-visible result |
|---|---|
| Problem frame | The working situation is recognizable before internal field taxonomy or neighboring-pattern exits take over. |
| Solution moves | The card shows practitioner moves from messy signal to reviewable problem-side record to honest next move, not only a field schema. |
| Use profiles | Thin, Standard, and High-load use stay distinct, so added fields follow live relation need. |
| Conformance review | The card can be checked for output kind, scope, readiness, cue, reference, exit, `setContextRef`, causal cue, representation continuity, freshness, scalarization, first-principles payoff, and record budget. |
| Anti-pattern resistance | The card resists card-as-work-item, fill-every-field, premature P2W readiness, preselected solution or work item, evidence, gate, and autonomy overread, portfolio-as-task-queue, scalar readiness, and sterile first-principles cue. |
| Validation use | At least the provided golden and anti-case slices can be used to test whether the card produces a usable next move without overclaiming. |
| Entry support | A practitioner can find `C.22.2` through first-entry phrases and tempting-wrong-pattern boundaries without reading the whole neighboring pattern network first. |
| P2W export rule | The card states what it exports to downstream P2W or selector-facing use and what it must not decide: method family, work authorization, gate passage, evidence proof, autonomy permission, or selected solution. |
| P2W reliance rule | When support posture or validation boundary is used for P2W receiving use, the card states `RelianceDisposition`, supported use, unsupported use, and live exits without adding default evidence, assurance, gate, autonomy, control, or work fields. |
| Neighboring-exit aid | The card user can look up the live relation, receiving pattern, permitted local cue, and forbidden local decision in one aid near the start without treating the aid as the main action engine. |
| Non-bureaucracy invariant | The card remains as small as the honest next move permits and does not require full-form completion when lighter reviewability is enough. |

### C.22.2:20 - Worked Slices and Anti-Cases

These worked slices and anti-cases support local use-quality validation. They are not a benchmark suite, scorecard, or completeness test; they test entry support, wrong-pattern boundary, and admissible stop for a `C.22.2` result.

#### C.22.2:20.1 - Five-Case Worked Slices

Five messy source signals serve as worked slices for use-quality validation, not as a benchmark suite: AI and human task rework, musical mastery tempo drift, problem set or Goldilocks selection, customer-support escalation after a policy or interface change, and literature-synthesis anomaly before method selection.

Thin card slices:

| Micro-slice | Problem signal | Context and scope cut | Not-wish or not-preselected-work reason | Improvement check or acceptance probe |
|---|---|---|---|---|
| AI and human task transfer rework | Repeated AI-agent task rework after transfer between human and agent. | Development or review setting where transfer produces avoidable rework; outside scope is selecting the agentic call plan, tool policy, or performed work. | The signal is not "ask the agent again" or "implement X"; the problem may be unclear task framing, missing candidate acceptance basis, unsafe delegation, or stale context. | The next task transfer is better only if the problem signal, context, acceptance probe, and safe-call or work-authority exit are recoverable. |
| Musical mastery tempo drift | Practice tempo drifts away from the intended mastery band. | Skill-development setting where tempo, recovery, rhythm, or learning rate changes the next move; outside scope is certifying a training method. | The signal is not "play faster" as a wish; the problem may be an untyped temporal claim, unsuitable acceptance probe, or missing recovery boundary. | The formulation improves only if the temporal claim, practice context, acceptance probe, and `C.27` exit are named when live. |
| Problem set or Goldilocks selection | A candidate problem is selected from an archive, pool, front, shortlist, selected set, or portfolio because it appears to fit a Goldilocks reading. | Problem-selection setting with retained candidates and possible stepping stones; outside scope is redefining QD or OEE semantics or selected-set semantics. | The signal is not a priority score or task queue item; the problem remains tied to `setContextRef`, source-set form, and selection or retention basis. | The card is usable only if `setContextRef`, characteristic or Q-bundle basis, partial-order or set-return cue, and non-scalar next move are recoverable. |
| Customer-support escalation after a policy or interface change | Support escalation volume rises after the change. | Product or operations setting where a changed promise, interface path, policy, or support script may have changed user behavior; outside scope is choosing the fix, staffing plan, or release decision. | The signal is not "reduce escalations" as a wish; the problem may be unclear interface promise, changed user path, stale support documentation, wrong acceptance probe, or a causal-use claim that needs another pattern. | The next revision is better only if the cause cue, acceptance probe, risk boundary, measurement or characterization exit, and evidence or causal-use exit are recoverable when live. |
| Literature-synthesis anomaly before method selection | A repeated anomaly in a literature synthesis does not fit the current category labels. | Named research or review context; outside scope is accepting a new theory, choosing a research method, or settling evidence sufficiency. | The signal is not "explain the anomaly" as a ready task, proof, or theory change; the problem may be an unstable described entity, rival frame, evidence need, or bridge or representation boundary. | The formulation improves only if `rivalProblemFormulationRef`, described entity, evidence need, and bridge, representation, or mathematical-structure exits are recoverable when live. |

Next move and tempting wrong-pattern check:

| Micro-slice | Honest next move | Tempting wrong pattern |
|---|---|---|
| AI and human task transfer rework | Stabilize the problem-side record; if agentic call planning or world-affecting action is live, exit to `C.24`, `E.16`, `A.21`, `A.15`, `A.10`, `G.6`, or `B.3` before action. | Treat repeated rework as a work item, a prompt retry instruction, or permission to delegate again. |
| Musical mastery tempo drift | Name the temporal claim and exit to `C.27` when tempo, rhythm, recovery, lead time, or learning rate changes the next move. | Treat drift or a trend line as an intervention model, method success, or evidence of mastery. |
| Problem set or Goldilocks selection | Preserve `setContextRef`; send set, parity, refresh, or set-return questions to `C.18`, `C.19`, `G.5`, `G.9`, `G.11`, `A.6.P:7a`, or `C.16.Q` when live. | Treat Goldilocks as one readiness score, priority rank, or local selected-set authority. |
| Customer-support escalation after a policy or interface change | Stabilize the problem-side record; characterize the signal through `C.16` and `A.19`, and exit to `C.28` if the card claims causal use. | Treat escalation volume as an automatic fix request, staffing plan, release rollback, or evidence that the policy was wrong. |
| Literature-synthesis anomaly before method selection | Preserve `rivalProblemFormulationRef` when rival frames remain live; exit to `A.10`, `B.3`, `F.9`, `E.18`, or `C.29` when evidence, assurance, bridge, representation, or mathematical structure is live. | Treat the anomaly as proof for a new theory, an accepted research task, or a selected method. |

P2W-ready disposition check:

| Micro-slice | P2W-ready disposition | Why |
|---|---|---|
| AI and human task transfer rework | Not P2W-ready until the acceptance probe and any agentic, work, safety, evidence, provenance, assurance, or gate exit are named. | The signal may still be a prompt retry, work-authority question, or unsafe delegation cue rather than a reviewable problem for downstream task typing. |
| Musical mastery tempo drift | Not P2W-ready while the temporal claim is untyped; exit to `C.27` when the tempo, rhythm, recovery, or learning-rate claim changes action. | A drift observation does not by itself state effort, window, resistance, basis, or reopen discipline. |
| Problem set or Goldilocks selection | Conditionally P2W-ready only when `setContextRef`, selection or retention basis, characteristic or Q-bundle basis, and non-scalar next move are present. | Without those fields, the case collapses into priority ranking, selected-set authority, or local QD or OEE vocabulary. |
| Customer-support escalation after a policy or interface change | Not P2W-ready until scope, affected user path, acceptance probe, risk boundary, and measurement or causal-use exits are explicit. | Escalation volume alone may reflect documentation, interface promise, staffing, policy, causal evidence, or measurement changes rather than one ready downstream task. |
| Literature-synthesis anomaly before method selection | Not P2W-ready until described entity, rival formulations, evidence need, and bridge, representation, or mathematical-structure exits are explicit when live. | An anomaly in synthesis may still be a cue, an abductive prompt, a bridge problem, or a representation problem rather than one ready downstream task. |

Additional validation cases:

| Validation case | What it checks | Expected result |
|---|---|---|
| Wish-to-problem | A wish-like input such as "I want to improve X" is not yet a reviewable problem for P2W. | The card requires a problem signal, improvement check or acceptance probe, and mandatory constraints before P2W readiness can be claimed. |
| Preselected work item | An input such as "implement X" may be a solution-shaped task rather than a problem. | The card blocks P2W readiness until a problem-side signal, context, scope, and candidate acceptance basis are stated. |
| Set-derived problem | A problem comes from an archive, pool, front, shortlist, selected set, or portfolio. | The card preserves `setContextRef` and the selection or retention basis, cites the receiving set pattern when live, and does not create a local portfolio or archive kind. |
| Agentic safe probe | An agentic next move may affect the world, spend resources, call tools, delegate to agents, or change operational state while authority is unclear. | The card names the risk or probe cue and exits to `C.24`, `E.16`, `A.21`, `A.15`, or the needed evidence, provenance, or assurance pattern; it does not authorize the probe locally. |
| Useful first-principles or mathematical cue | A first-principles or mathematical structure cue changes the problem formulation instead of merely decorating the card. | The card records the formulation payoff, preserved and lost structure when live, support posture, stop condition, and `C.29` exit. |
| Citation misuse | A later practitioner cites the card as proof, gate passage, safety acceptance, work authorization, or autonomy permission. | The citation is admissible only as cue, reference, or exit; gate passage needs `A.21`, evidence, provenance, or assurance needs `A.10`, `G.6`, or `B.3`, autonomy needs `E.16`, and work authority needs `A.15`. |
| Backlog-intake overread | Every ticket, idea, support request, or backlog item is forced through a full `ProblemCard@Context` before ordinary local work can continue. | Use `C.22.2` only when the signal must become reviewable before P2W, task typing, method-family selection, evidence use, gate passage, autonomy control, set-return handling, or first-principles support; the Thin form is sufficient when it gives the honest next move. |
| Already-solved or stale | The signal is stale, duplicate, already solved, already absorbed, unnecessary, or not currently worth downstream work. | A successful result may be refresh, retire, archive, `abstain/no-change`, bounded use under authority, or another named neighboring exit; the card must not silently remain `P2W-ready`. |

### C.22.2:21 - Machine-Assisted Drafting Boundary

Machine-assisted `ProblemCard@Context` drafting is admissible only as draft support. The practitioner remains responsible for verifying the governing fields and neighboring exits before the card is used for P2W, selection, evidence, gate, autonomy, or work.

For AI-assisted entry or retrieval, a `C.22.2` hit is only a candidate-pattern hit. The practitioner or assistant must still check the first honest entry load: problem-side record before P2W, work plan, evidence claim, local choice, safe probe, mathematical-lens adequacy, or ordinary discussion.

Required practitioner checks for a machine-assisted draft:

- source signal;
- improvement check or acceptance probe;
- support posture;
- unknown handling;
- freshness or expiry disposition;
- neighboring exits;
- no evidence, gate, work, or autonomy overread.

### C.22.2:22 - First Practical Entry Support
This section is discoverability support only. It helps a practitioner or assistant find a candidate pattern; it does not prescribe a transition sequence and does not require opening `C.22.2` for every problem-sounding text.

These likely practitioner entry phrases point to `C.22.2`:

- "We have a problem, but it is not yet clear what work should be done."
- "This looks like a ticket, but I am not sure the problem is stated."
- "A signal or anomaly keeps recurring before method selection."
- "We selected this candidate from a front, archive, pool, or selected set, but need to state why it is a problem now."
- "P2W would otherwise receive 'implement X'."
- "There is a symptom, but we do not yet know what to solve."
- "We need to know whether this problem is ready for P2W or should exit elsewhere."

Tempting wrong first patterns:

- Do not start at `C.11` if the live issue is not yet a local choice among available options.
- Do not start at `C.16` or `A.19` if the live issue is not only measurement, characterization, or indicator admissibility.
- Do not start at `C.18`, `C.19`, or `G.5` if the live object is one selected singleton problem card rather than the archive, pool, front, or selected-set object.
- Do not start at `A.15` if no method or work plan is ready.
- Do not start at `A.10`, `G.6`, or `B.3` if evidence, provenance, or assurance is not the center.
- Do not start at `A.21` or `E.16` if no gate or autonomy authority is being decided.

Not `C.22.2` anti-cases:

- "The method is accepted; now schedule the work." Use `A.15`.
- "We need proof this result is reliable." Use `A.10`, `G.6`, or `B.3`.
- "Which option should we choose among explicit options?" Use `C.11`, or `G.5` when set publication or selected-set semantics are live.
- "Can the agent call the tool?" Use `C.24`, `E.16`, or `A.21`; `ProblemCard@Context` may only name the problem-side cue or exit and does not grant tool-call, autonomy, or gate authority.
- "This is ordinary discussion with no downstream project-side move." Do not use `C.22.2`.

First-use Thin-card test:

Given a messy signal, a practitioner must be able to produce a Thin `ProblemCard@Context` in under one page and correctly choose one admissible next move: `P2W-ready`, characterize, compare or parity, search or pool, refresh, retire, `abstain/no-change`, or named neighboring-pattern exit.

Entry relation:

The entry relation is local: `C.22.2` is introduced under `C.22`, and `C.22` names the `ProblemCard@Context` relation. The `C.22.2` body carries the Problem frame, first-entry phrases, tempting-wrong-pattern boundaries, and first-use Thin-card test needed for ordinary discovery.

### C.22.2:23 - Downstream Boundary Exports
A downstream citation of `ProblemCard@ContextRef` is admissible only for the local cue or reference named by the downstream relation. For `C.22` use, cite problem-side readiness and candidate `TaskSignature` basis only. For `G.5` use, cite selected-set or search cues only as source cues. For `A.15` use, cite work need only after work planning is live. For `A.10`, `G.6`, and `B.3` use, cite support or evidence cues only as cues, not proof. For `C.29` use, cite `firstPrinciplesCue` only for mathematical-lens adequacy, not method or acceptance authority. No downstream citation inherits full-card authority by reference.

P2W export from `ProblemCard@Context` includes:

- problem-side representation.
- context grounding and scope cut.
- not-wish, not-ticket, not-slogan, or not-preselected-work reason.
- improvement check or acceptance probe.
- readiness disposition: reviewable-only, `P2W-ready`, no-work or abstain, or sent to a named neighbor.
- candidate `TaskSignature` basis only when downstream selector or P2W readiness is declared.
- named neighboring exits and references, without importing neighboring authority into the card.

P2W export from `ProblemCard@Context` does not include:

- method-family selection or selected method.
- `WorkPlan`, work authorization, performed work, result record, or result measurement.
- evidence proof, evidence sufficiency, provenance certification, or assurance claim.
- gate passage, gate decision, release permission, or safety-case acceptance.
- autonomy permission, delegated-agent authority, tool-call permission, or permission to spend resources.
- selected solution, portfolio authority, selected-set authority, or mathematical adequacy proof.

| Downstream relation | Exportable local cue or reference | Forbidden local settlement |
|---|---|---|
| Evidence and safety-reliance follow-on work | Support posture and validation boundary. | Proof, conformance, safety-case reliance, confidence, release permission, gate passage, or work authorization. |
| P2W follow-on work | Problem-side cues sufficient for P2W receiving use or selector-facing use. | Formalism, ontology, method family, `WorkPlan`, performed Work, method selection, or work authorization. |
| Decision, NQD, and OEE follow-on work | `setContextRef`, Goldilocks, and stepping-stone cues relevant to selected-set or set-return follow-on work. | QD or OEE definitions, selected-set docking, Q-front, set-return semantics, decision-quality admissibility, or the selected set itself. |

### C.22.2:24 - Consequences

#### C.22.2:24.1 - Benefits

- FPF gains a clear problem-side output for problematization as the input P2W can use.
- P2W receives a typed problem-side record rather than a slogan, ticket-shaped wish, or preselected method.
- `C.22.2` has practical value for FPF when it reduces at least one expensive failure: a wish enters P2W as `TaskSignature`; a preselected work item is treated as the problem; method selection happens before the problem is reviewable; a problem from a set loses `setContextRef`; an indicator is used without admission; support posture is cited as proof; a stale problem remains active; scalar readiness replaces set-return; or support is inherited across a changed representation without a SEMIO witness.
- Current archive, pool, front, shortlist, set-return, parity, refresh, evidence, and `C.29` patterns are reused instead of duplicated.
- The positive role of mathematical and first-principles thinking is preserved: it can find missing structure, not only check already-written mathematics.
- Characterization and parity are no longer optional background when they are prerequisites for problem reviewability.
- Representation-change support is handled through named relation exits rather than local proof inside the problem card.

#### C.22.2:24.2 - Costs of Use

- A `ProblemCard@Context` adds a small writing step before P2W. The cost is justified only when the signal must become reviewable before task typing, method-family selection, evidence use, gate passage, autonomy control, set-return handling, or first-principles support.
- The practitioner must keep the card small: preserve the split between problem, task, method, work, and result; keep `TaskSignature` minimal; and add conditional fields only when their relation is live.
- For problems emitted from archives, pools, fronts, selected sets, or portfolios, the practitioner must preserve `setContextRef` or the set-source relation without turning the card into a portfolio, archive, selected-set, or work-planning object.
- External or source-local terms may guide recognition only when they change a concrete boundary, field, exit, or validation obligation. Otherwise they remain examples or source cues, not local authority.

### C.22.2:25 - Relations

- Builds on: `E.2`, `E.9`, `E.10`, `C.2.P`, `A.6.P`, `C.16.Q`, `C.16`, `A.19`, `C.22`, `C.25`, `C.29`, `G.5`, `G.9`, `A.6.3.RT`, and `A.6.4`.
- Coordinates with: `C.11`, `C.18`, `C.19`, `C.22.1`, `A.15`, `A.21`, `E.16`, `G.6`, `G.11`, `A.10`, `B.3`, `E.17`, `E.17.ID.CR`, `A.6.3`, `F.9`, and `E.18`.

### C.22.2:End

