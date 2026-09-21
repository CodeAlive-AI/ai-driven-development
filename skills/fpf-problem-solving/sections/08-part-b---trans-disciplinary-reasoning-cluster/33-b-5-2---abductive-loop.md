## B.5.2 - Abductive Loop

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Abductive loop.

**Builds on.**
`B.5 Canonical Reasoning Cycle`, `B.5.1 Exploration`, `B.5.2.0 U.AbductivePrompt`, `A.10`, `B.3.3`.

**Coordinates with.**
`B.4.1 Observe-Notice-Stabilize-Route` for pre-abductive routing, `A.16` for admissible language-state moves, `A.6.P` for lexical repair before hypothesis publication, and `C.16.Q` / `A.6.A` when the initiating publication face or cue is evaluative or action-inviting rather than explanatory.

### B.5.2:1 - Problem frame

**Use this when.** An anomaly, opportunity or probe question needs candidate explanations that can be compared on their present plausibility. State the question and generate its serious rivals. The first useful result is a qualified conjecture with its supports, fragilities and allowed use, or an honest abort, defer or split outcome.

An adequate present answer or action need not enter abduction merely to generate another research task. Use C.11 for a live choice among feasible actions and C.28 when a causal-support claim is needed. Abduction contributes candidate explanatory content; it is not the complete evidence synthesis or action decision.

### B.5.2:2 - Problem

Without an explicit abductive pattern:

1. **Inquiry stalls at surprise.**
   A team encounters an anomaly, opportunity, or probe pressure but has no admissible next action for producing a candidate hypothesis.
2. **Origin is lost.**
   Once a conjecture appears, the initiating prompt, rival candidates, and early plausibility grounds disappear from the record.
3. **Candidate space collapses too early.**
   The first plausible-seeming explanation is treated as the explanation, even though alternatives were never exposed.
4. **Selection becomes opaque.**
   A chosen conjecture moves downstream without a visible record of why it outranked alternatives.
5. **Untestable hypotheses survive too long.**
   A candidate with no interpretable implication or possible discriminating contrast is treated as a useful explanation. Distinguish this from a meaningful conjecture whose possible check is presently unavailable.

### B.5.2:3 - Forces

| Force | Tension |
|---|---|
| **Generativity vs discipline** | The loop must admit non-deductive candidate generation without making arbitrary guesses look admissible. |
| **Breadth vs typed entry** | Abduction should begin from more than anomaly alone, but not from any untyped prose fragment. |
| **Rival diversity vs decision pressure** | Several candidates should remain visible long enough to compare them, while still allowing one prime hypothesis to progress. |
| **Speed vs traceability** | The loop must be light enough for repeated use but explicit enough to preserve provenance and later review. |
| **Plausibility vs evidence** | A candidate may be worth pursuing before evidence is strong, but it still needs explicit plausibility grounds. |

### B.5.2:4 - Solution - Structured abductive micro-cycle

`B.5.2` begins from an admissible `U.AbductivePrompt`, expands a candidate set, compares it under explicit plausibility criteria, and publishes the selected conjecture as a hypothesis-bearing `U.Episteme`. Preserve the supports, rivals, limitations and allowed downstream use. Abduction alone assigns no `AssuranceLevel`.

#### B.5.2:4.1 - Nature of abduction in FPF

In FPF, abduction proposes a presently most plausible candidate explanation, model or conjecture under a declared prompt. Its plausibility can justify keeping or using that conjecture for a bounded purpose, but does not establish its causal mechanism or a stronger empirical claim. Deduction, evidence synthesis and action choice keep their own questions.

#### B.5.2:4.2 - Four-step micro-cycle

| Step | Core activity | Required publication outcome |
|---|---|---|
| **1. Frame the prompt** | State the initiating `U.AbductivePrompt` precisely enough that the unexplained contrast, opportunity, or probe pressure is explicit. | A prompt record with open question, scope notes, and provenance. |
| **2. Generate candidate hypotheses** | Produce multiple candidate conjectures that could resolve the prompt. | A visible candidate set, even if lightweight. |
| **3. Apply plausibility filters** | Compare candidates against explicit plausibility criteria. | A short rationale that records why some candidates remain live and others are rejected. |
| **4. Select and publish the prime hypothesis** | Choose the presently preferred conjecture where the comparison warrants one. | A hypothesis-bearing `U.Episteme` with its prompt, selection rationale, live rivals, supports, fragilities and allowed use. No universal level or mandatory next experiment follows. |

The loop is intentionally iterable. A selected prime hypothesis may later be replaced, narrowed, or reopened if deduction, probe work, or evidence reveals a better rival.

#### B.5.2:4.3 - Entry discipline via `U.AbductivePrompt`

`AnomalyStatement` remains a canonical prompt species, but it is not the only one. `B.5.2` also accepts the broader prompt species governed by `B.5.2.0`, such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`. This broadens entry without dissolving type discipline.

#### B.5.2:4.4 - Plausibility filters

The filtering step is local and context-sensitive, but the criteria used **SHALL** be explicit. Typical filters include:

- **Parsimony.** Does the candidate introduce only the additional structure that the prompt requires?
- **Explanatory reach.** How much of the prompt does the candidate actually account for?
- **Consistency with established constraints.** Does the candidate avoid collision with already trusted pillars, mechanisms, or scope declarations?
- **Falsifiability / probeability.** What implication, deduction or possible observation could discriminate the candidate from its rivals? Keep that question separate from whether a check is obtainable and worth performing now.
- **Scope fit.** Is the candidate framed for the declared prompt scope rather than for an inflated or shifted target?

No one filter is universally decisive. The pattern only requires that at least two filters be declared when a prime hypothesis is selected.

#### B.5.2:4.5 - Abductive Unfolding Structure Block

When the abductive run must be reused as more than a one-off hypothesis note, add an unfolding block. It shows how the prompt becomes rival hypotheses and downstream tests without treating the creative passage as evidence.

```text
AbductiveUnfoldingStructureBlock:
  unfoldingStructureRef: current AbductiveSearchUnfoldingStructure record
  abductivePromptRef:
  cueSetWithDownstreamPatternAlternativesRef:
  rivalHypothesisSetRef:
  hypothesisGenerationLoci[]:
  plausibilityConstraintRefs[]:
  evidenceReturnLoci[]:
  languageStateMoveRefs[]:
  poolPolicyOrSelectionRef?:
  blockedOverread: not inspiration event, not linear ideation workflow, not evidence by itself
```

Use `unfoldingStructureRef` for the current local structure record; use A.22.CGUS `specializedStructureRef?` only when the generic CGUS record must point to this narrower specialization. Use `cueSetWithDownstreamPatternAlternativesRef` when the prompt still carries several possible patterns for the next question. Use `rivalHypothesisSetRef` before selecting a prime hypothesis. Use `evidenceReturnLoci[]` to say where later evidence, deduction, probe design, or assurance work can return; do not use those loci as evidence. If the live claim becomes candidate retention, pool policy, selected-set result declaration, or comparison, apply `C.18`, `C.19`, `G.5`, or the pattern that defines the required comparison instead of making abduction a selector.

`AbductiveSearchUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization used for abductive search. It is not a root U-kind, ideation workflow, evidence, or selection decision. Use `B.5.2` to state the abductive prompt, cue set with alternative next patterns, rival hypotheses, plausibility constraints, and evidence-return loci. Use the patterns that define or test evidence, deduction, probe design, assurance, selected-set result declaration, pool policy, and comparison when those claims become current.

### B.5.2:5 - Archetypal Grounding

**Tell.** Abduction is not "a flash of insight." It is the governed passage from a typed prompt to a candidate conjecture through explicit rival generation and plausibility comparison.

**Show (System).** An operations team sees a recurring latency spike that existing explanations do not cover. They publish an `AnomalyStatement`, compare rival causes against current telemetry and mechanism knowledge, and retain a qualified prime conjecture. They name a possible discriminating probe without assigning a maturity level or committing the service team to an experiment.

**Show (Episteme).** A research group notices that two accepted results no longer fit together under one framing. It publishes a `ProbeCuePrompt`, enumerates several rival explanatory reframings, rejects the ones that fail scope fit or would not generate decisive probes, and advances one candidate explanation as the next working hypothesis.

### B.5.2:6 - Bias-Annotation

This pattern biases authors toward visible candidate plurality, explicit plausibility criteria, and persistent prompt provenance. That bias is intentional. `B.5.2` would rather keep early conjectures slightly over-exposed than let their origin and selection grounds disappear.

### B.5.2:7 - Conformance Checklist

- `CC-B.5.2-1` Every abductive run **SHALL** begin from a declared `U.AbductivePrompt`; arbitrary prose fragments are not sufficient prompt-entry forms.
- `CC-B.5.2-2` A conforming abductive run **SHALL** record at least one rival candidate alongside any selected prime hypothesis, unless the author explicitly justifies why no rival candidate was available.
- `CC-B.5.2-3` Selection of a prime hypothesis **SHALL** cite at least two explicit plausibility filters.
- `CC-B.5.2-4` The selected prime hypothesis SHALL be published as a hypothesis-bearing `U.Episteme` with its scope, support and limitations. An assurance level, if a receiving use requires one, SHALL follow B.3.3's applicable justified profile rather than the fact that abduction occurred.
- `CC-B.5.2-5` The prime hypothesis record **SHALL** preserve a link to the initiating prompt and to the filtering rationale that justified selection.
- `CC-B.5.2-6` A conforming conjecture SHALL expose an interpretable implication, deduction or possible discriminating contrast. The availability and value of a check SHALL be considered separately before selecting evidence acquisition. An unavailable probe neither creates an observation nor by itself forbids a separately supported present decision.

### B.5.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Authority candidate** | One favored conjecture is advanced immediately, with no rival set and no explicit filtering. | `CC-B.5.2-2` and `CC-B.5.2-3` require candidate plurality and visible plausibility grounds. |
| **Untestable grand conjecture** | The candidate sounds explanatory but has no interpretable implication or discriminating contrast. | Use CC-B.5.2-6 to make its implications clear or refuse that abductive result. Do not confuse absence of a useful implication with temporary unavailability of a meaningful check. |
| **Prompt amnesia** | A later reader can see the conjecture but not the initiating anomaly, opportunity, or probe pressure. | `CC-B.5.2-1` and `CC-B.5.2-5` keep prompt provenance attached. |
| **Symptom patching** | The selected candidate only redescribes a visible symptom and leaves the actual prompt unresolved. | The explicit plausibility filter for explanatory reach forces the candidate to be compared against the whole prompt. |

### B.5.2:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Disciplined generativity.** Abduction stays inventive without collapsing into formless conjecturing. | Requires explicit prompt and filter publication; mitigation: the required record can remain lightweight. |
| **Traceable hypothesis origin.** Later review can reconstruct why a conjecture entered the reasoning cycle. | Adds a small provenance-support load; mitigation: reuse prompt and candidate-set notes from adjacent patterns. |
| **Cleaner downstream use.** A hypothesis-bearing episteme gives the receiving question its scope, rivals, support and limitations. | A candidate can remain useful without being confirmed or receiving a universal level; a stronger claim still needs its own evidence. |
| **Admissible reopening.** Rival candidates can be revisited when later work undermines the selected prime hypothesis. | Demands editorial discipline so that abandoned rivals remain legible rather than silently vanishing. |

### B.5.2:10 - Rationale

For the hypothesis-led empirical inquiry described in B.5, B.5.2 supplies explanation-led abduction before deduction and induction. It keeps hypothesis generation explicit, connects it to typed prompt publications, and prepares the output for later assurance work without pretending that early plausibility is already evidence.

### B.5.2:11 - SoTA-Echoing

Contemporary inquiry practice in science, engineering, design, and diagnosis treats candidate generation as iterative and contrast-driven rather than singular and opaque. The pattern aligns with that practice, but keeps the representation lightweight: explicit prompts, visible rival candidates, and local plausibility grounds instead of heavyweight ideation machinery.

### B.5.2:12 - Relations

- **Supplies explanation-led abduction within:** B.5's hypothesis-led empirical inquiry, before deduction and induction.
- **Typically operates during:** `B.5.1 Exploration`.
- **Consumes:** `U.AbductivePrompt` publications from `B.5.2.0`, often reached through `B.4.1` and `A.16`.
- **Produces:** hypothesis-bearing `U.Episteme` publications with explicit conjectural content, supports, fragilities and allowed use; no automatic `AssuranceLevel:L0`.
- **Provides inputs for:** deduction, probe design and evidence synthesis when those questions are live. C.11 governs a separate feasible-action or acquisition choice; C.28 supplies needed causal-use support. A possible experiment is not funded or scheduled Work.
- **Coordinates with:** `A.22.CGUS` when the abductive prompt, `B.4.1` cue publication, rival hypotheses, plausibility constraints, evidence-return loci, and downstream tests must be inspected as an `AbductiveSearchUnfoldingStructure`.

#### B.5.2:12.1 - Prompt-entry broadening via `U.AbductivePrompt`

Older wording that makes `AnomalyStatement` the exclusive entry form is superseded. `B.5.2` accepts `U.AbductivePrompt`, where `AnomalyStatement` remains one canonical species alongside cue-derived prompt species such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`.

### B.5.2:13 - Prompt, Candidate, and Hypothesis Package Discipline

The abductive loop stays auditable only if the three main publication forms remain distinct: the **prompt**, the **candidate set**, and the **selected prime hypothesis**. Collapsing them into one paragraph is one of the main reasons later review cannot reconstruct what actually happened.

#### B.5.2:13.1 - Prompt package

A conforming prompt package should make explicit:

- the **prompt species** (`AnomalyStatement`, `ProblemCuePrompt`, `OpportunityCuePrompt`, or `ProbeCuePrompt`),
- the **open question** that makes abduction necessary,
- the **declared scope** under which the question is being posed,
- the **witnesses or provenance cues** that made the prompt worth preserving,
- and the **reason the current model is insufficient**.

If the initiating publication is still primarily evaluative, action-inviting, or lexically overloaded, it should first be repaired by the relevant A.6 family before it is treated as a stable abductive prompt. `B.5.2` assumes typed entry, not raw lexical ambiguity.

#### B.5.2:13.2 - Candidate-set note

A candidate-set note is the minimal record that preserves rival plurality. It need not be heavy, but it should make visible:

- candidate identifiers or short names,
- the differentiating claim each candidate adds,
- the principal plausibility supports and liabilities of each candidate,
- whether the candidate remains live, is deferred, or is rejected,
- and the implication or possible evidence that would best discriminate among remaining rivals, with an availability limitation when it changes the receiving use.

The important point is not bureaucratic completeness. The important point is to prevent retrospective rewriting in which the surviving candidate is made to look as if it had been the only serious option from the beginning.

#### B.5.2:13.3 - Prime-hypothesis record

A selected prime hypothesis should preserve more than the hypothesis sentence itself. Its record names:

- the **selected candidate**,
- the **prompt** it answers,
- the **filters** under which it outranked rivals,
- the **scope** within which it is being advanced,
- the **allowed downstream use or next question**, which may concern deduction, a possible probe, a separately justified action or reconsideration; include availability limits when they change that use,
- and any **known fragilities** already visible at selection time.

This is how `B.5.2` stays connected to the rest of the reasoning cycle. The abductive loop does not merely emit an idea; it emits a conjecture with explicit downstream-use terms.

### B.5.2:14 - Admissible Transitions, Abort Paths, and Reopening

The abductive loop keeps its outcomes distinct so the recipient can tell whether it receives a qualified conjecture, deferred rivals, or a prompt that needs reopening. None of these outcomes by itself establishes an assurance level or an evidence-acquisition commitment.

#### B.5.2:14.1 - Relation to `B.4.1` and `A.16`

`B.4.1` and `A.16` often supply the pre-abductive seam. They help preserve and stabilize upstream publications, including publication forms that carry route-shaped representations when those forms are explicitly governed, before the publication is fit for explicit conjecture. `B.5.2` begins only once the current publication is ready to function as an abductive prompt. This boundary matters because it prevents two opposite errors:

- **premature abduction**, where a low-articulation cue is treated as if it had already earned hypothesis form;
- **delayed abduction**, where a now-stable prompt is kept indefinitely in early cue form even though rival conjectures should already be compared.

#### B.5.2:14.2 - Abort, defer, and split cases

Not every abductive run should end in a prime hypothesis. Three non-selection outcomes are admissible:

1. **Abort.** The prompt dissolves because the initiating anomaly or opportunity was misread, duplicated, or already answered elsewhere.
2. **Defer.** Several candidates remain live and the available comparison does not justify a winner, for example because a needed discriminator is unavailable. Preserve the unresolved set and its limits without inventing a winning explanation. A separately warranted present action may still proceed under C.11.
3. **Split.** The original prompt turns out to contain several distinct questions. The run should fork into several narrower prompts rather than select one over-broad conjecture.

These outcomes are not failures. They are part of keeping abduction honest.

#### B.5.2:14.3 - Reopening and rival reinstatement

A prime hypothesis may later lose support under deduction, probe results, or new evidence. When that happens, `B.5.2` prefers explicit reopening to silent replacement.

A conforming reopening note should identify:

- which prior prime hypothesis is being reopened,
- whether a stored rival is being reinstated or a new candidate is entering,
- what change in evidence, scope, or internal contradiction triggered the reopening,
- and whether the original prompt itself has changed or only the candidate ranking has changed.

This allows the reasoning cycle to keep continuity without pretending that the earlier abductive choice had never been made.

#### B.5.2:14.4 - Scope discipline during iteration

Abductive drift often comes from silent scope expansion. A conjecture first framed for one target slice quietly becomes a universal explanation. `B.5.2` therefore expects scope discipline to remain explicit during iteration. If a candidate requires a broader or narrower scope than the prompt originally declared, that scope move should be stated rather than smuggled in under the rhetoric of a "better explanation."

### B.5.2:15 - Worked Examples

#### B.5.2:15.1 - Service degradation diagnosis

A service team notices recurring latency spikes during one operating window. The prompt species is `AnomalyStatement`: *why does latency spike in the evening batch window despite unchanged nominal load?*

The candidate set includes:

- queue saturation in one downstream dependency,
- a time-window interaction with backup traffic,
- and a recent mechanism regression in cache invalidation.

The backup-interaction conjecture is preferred because its timing fits the existing observations and it remains consistent with known mechanisms; the other two candidates remain live. Isolating backup traffic and comparing latency against prior windows is a possible discriminator. When that probe is obtainable and its expected contribution justifies its cost and delay, it can be selected as separate work. The conjecture itself records no observation from that unperformed probe.

Now keep the same observations and rival set but make the probe window unavailable. The qualified conjecture and its uncertainty remain; if the available comparison cannot select a winner, defer that selection. No new test, waiver or study proposal is needed just to finish the present abductive result.

In both variants, suppose an existing operational qualification independently supports a bounded diversion to a spare instance for this traffic and interval, with sufficient capacity and actual permission, across all three remaining causes. C.11 can support that service response on the available basis. Diverting traffic does not identify the cause; a causal claim about the mechanism still needs the appropriate C.28 support. If that operational basis is absent, do not infer a justified diversion from conjecture plausibility.

#### B.5.2:15.2 - Opportunity-driven materials inquiry

A research group sees an opportunity rather than a failure: a new fabrication method appears to create a micro-structure with useful thermal behavior. The prompt species is `OpportunityCuePrompt` rather than anomaly.

Candidate hypotheses include:

- the effect is caused by surface geometry,
- it is caused by composition gradients,
- or it is an effect of one measurement regime.

The geometry explanation is the prime conjecture because it fits more of the initial observations and suggests a clearer discriminating experiment. Keep the composition and measurement rivals visible. The possible experiment can inform a separate research choice; its description neither funds it nor makes it mandatory. Long-horizon research can be worthwhile on its own declared contribution, without treating the conjecture as an established thermal-performance result.

#### B.5.2:15.3 - Probe-driven theory repair

A theory-maintenance group identifies a probe-worthy mismatch between two accepted claims. The prompt species is `ProbeCuePrompt`: *what changed assumption would allow these two claims to coexist without contradiction?*

The candidate set includes:

- hidden scope restriction on the first claim,
- mistaken invariance assumption in the second,
- and a more general missing mediating construct.

The selected prime hypothesis is the mediating construct, but the scope-restriction candidate remains stored as a live rival because it could still outperform if later deductions fail. This example illustrates why `B.5.2` tracks the rival set rather than only the currently favored conjecture.

### B.5.2:16 - Authoring and Review Guidance

#### B.5.2:16.1 - For abductive-publication authors

Authors should treat the abductive loop as a **selection discipline**, not as a prose genre. The minimal questions are:

- what is the prompt,
- what rival candidates were seriously considered,
- why is one candidate currently the best live conjecture,
- and what downstream move could expose that selection as right or wrong?

If those answers cannot be given, the publication is probably not yet at `B.5.2` and should return to prompt-shaping or lexical repair.

#### B.5.2:16.2 - For hypothesis reviewers

Hypothesis reviewers should not ask only whether the chosen hypothesis looks plausible. They should also ask:

- whether the prompt was typed in an admissible way,
- whether at least one real rival was preserved,
- whether the filters named at selection time actually discriminate among candidates,
- whether the selected hypothesis has interpretable implications and a meaningful possible discriminator, with actual availability kept separate from that explanatory contribution,
- and whether any scope inflation occurred during selection.

A polished hypothesis with no visible rivals is usually less trustworthy than a rougher hypothesis whose rival space is explicit.

#### B.5.2:16.3 - For integrators and assurance leads

Integrators receive a qualified conjecture, not early assurance conferred by an `L0` label. Preserve its prompt, rivals, supports, filter rationale and fragilities. Use B.3.3 only for a receiving assurance question, C.11 for a feasible-action or evidence-acquisition choice, and C.28 for causal support when needed. An unavailable probe can leave the explanation unresolved while an independently warranted bounded service action remains useful; do not turn the conjecture into a mandatory work item.

### B.5.2:17 - Migration and Boundary Notes

#### B.5.2:17.1 - Migration from anomaly monopoly

Older wording that says abduction begins only from anomaly should be rewritten into the broader but still typed claim: abduction begins from an admissible `U.AbductivePrompt`, of which anomaly is one canonical species.

#### B.5.2:17.2 - Migration from inspiration rhetoric

Legacy prose that describes abduction as a flash, leap, or raw creative moment may remain as didactic metaphor, but it should not be used as the operational description of the pattern. The operational core is typed prompt -> rival set -> plausibility filtering -> prime hypothesis publication.

#### B.5.2:17.3 - Boundary to deduction and evidence

`B.5.2` ends with a qualified prime conjecture or an explicit abort, defer or split outcome. Deduction, evidence acquisition, synthesis, assurance and action choice remain separate questions. Naming their possible contribution states a downstream-use boundary; it does not require a new experiment, guarantee its availability or prevent a present decision already supported on other grounds.
### B.5.2:End
