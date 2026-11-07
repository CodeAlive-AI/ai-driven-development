## B.5.2 - Generate and Compare Candidate Explanations (Abductive Loop)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Generate and compare candidate explanations (Abductive Loop).

**Builds on.**
`B.5 Choose the Next Reasoning Contribution (Canonical Reasoning Cycle)`, `B.5.1 Exploration`, `B.5.2.0 U.AbductivePrompt`, `A.10`, `B.3.3`.

**Coordinates with.**
`B.4.1` for needed route publication, `A.16` for admissible language-state moves, `A.6.P` for unresolved relation wording, `C.16.Q` for unresolved evaluative meaning, and `A.6.A` for unresolved action-first wording. Use these wording-restoration contributions when the unclear meaning affects the explanatory question or its scope.

### B.5.2:1 - Problem frame

**Use this when.** An anomaly, opportunity or probe question needs candidate explanations that can be compared on their present plausibility. State the explanatory question, develop candidates and look for serious alternative explanations. The first useful result is a qualified conjecture with its supports, fragilities and allowed use, or a justified abort, defer or split outcome.

An adequate present answer or action need not enter abduction merely to generate another research task. Use C.11 for a live choice among feasible actions and C.28 when a causal-support claim is needed. Abduction contributes candidate explanatory content; it is not the complete evidence synthesis or action decision.

### B.5.2:2 - Problem

Abductive work can fail in several ways:

1. **Inquiry stalls at surprise.**
   A team encounters an anomaly, opportunity, or probe question but does not know how to form and compare candidate explanations.
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

`B.5.2` begins from an account that meets `B.5.2.0`'s `U.AbductivePrompt` entry conditions, develops candidate explanations and compares them under explicit plausibility criteria. Return a qualified conjecture when the grounds support it, or an abort, defer or split outcome under §14.2. Preserve the prompt, candidates considered, supports, limitations and allowed downstream use. Abduction alone assigns no `AssuranceLevel`.

#### B.5.2:4.1 - Nature of abduction in FPF

Abduction develops candidate explanations, models or conjectures for a declared explanatory prompt and compares their plausibility. Prefer a candidate only to the extent that the comparison warrants that preference. A conjecture's plausibility may justify keeping or using it for a bounded purpose; it does not establish its causal mechanism or a stronger empirical claim. Deduction, evidence synthesis and action choice keep their own questions.

#### B.5.2:4.2 - Four-step micro-cycle

| Step | Core activity | Required publication outcome |
|---|---|---|
| **1. Frame the prompt** | State the initiating explanatory question precisely enough that the unexplained contrast, opportunity, or probe pressure is explicit. | A prompt account with its open question, species, scope and motivating grounds under `B.5.2.0`; reuse an adequate existing account. |
| **2. Generate candidate hypotheses** | Develop candidates that could explain the prompt and look for serious rivals. | The candidates actually considered, including any limit from not identifying a serious rival. |
| **3. Apply plausibility filters** | Compare candidates against explicit plausibility criteria. | A short rationale stating why each considered candidate remains live, is deferred or is rejected, and what comparison those grounds support. |
| **4. Return the supported result** | Select a conjecture when the comparison warrants it; otherwise return the applicable outcome in §14.2. | A hypothesis-bearing `U.Episteme` with its prompt, selection rationale, any live rivals, supports, fragilities and allowed use when a conjecture is selected; otherwise the justified abort, defer or split outcome. |

The loop is intentionally iterable. A selected prime hypothesis may later be replaced, narrowed, or reopened if deduction, probe work, or evidence reveals a better rival.

#### B.5.2:4.3 - Entry discipline via `U.AbductivePrompt`

`AnomalyStatement` remains a canonical prompt species, but it is not the only one. `B.5.2` also accepts the broader prompt species governed by `B.5.2.0`, such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`.

#### B.5.2:4.4 - Plausibility filters

The filtering step is local and context-sensitive, but the criteria used **SHALL** be explicit. Typical filters include:

- **Parsimony.** Does the candidate introduce only the additional structure that the prompt requires?
- **Explanatory reach.** How much of the prompt does the candidate actually account for?
- **Consistency with established constraints.** Does the candidate avoid collision with already trusted pillars, mechanisms, or scope declarations?
- **Falsifiability / probeability.** What implication, deduction or possible observation could discriminate the candidate from its rivals? Keep that question separate from whether a check is obtainable and worth performing now.
- **Scope fit.** Is the candidate framed for the declared prompt scope rather than for an inflated or shifted target?

Select the filters needed to judge explanatory adequacy and preference for this prompt and intended use. Make their grounds, any decisive comparison and unresolved trade-offs explicit.

When a causal hypothesis cannot yet yield a discriminating implication because its mechanisms and rival accounts are unspecified, use C.28.CM to construct comparable causal models. Return their conditional consequences and unresolved premises to these plausibility filters. A useful hypothesis whose present question is already answered needs no additional model merely to remain a candidate.

#### B.5.2:4.5 - Abductive Unfolding Structure Block

When the question concerns possible continuations of abductive work and their conditions, use A.22.CGUS's ordinary branch. Open its formal branch only when the receiving use depends on the unfolding organization's CGUS identity or membership; reuse of a hypothesis note alone does not require that branch.

```text
AbductiveUnfoldingStructureBlock:
  unfoldingStructureRef: one independently identified A.22.CGUS structure
  abductivePromptRef:
  cueSetWithDownstreamPatternAlternativesRef:
  rivalHypothesisSetRef:
  hypothesisGenerationLoci[]:
  plausibilityConstraintRefs[]:
  evidenceReturnLoci[]:
  languageStateMoveRefs[]:
  poolPolicyOrSelectionRef?:
```

Use `unfoldingStructureRef` to designate the selected structure. Recover its constituents, obtaining relation occurrences, applied constraints and selection-use frame under A.22; qualify its loci and potential continuations under A.22.CGUS. Keep the describing record separate from that identity. Use `cueSetWithDownstreamPatternAlternativesRef` when the prompt still carries several possible patterns for the next question. Use `rivalHypothesisSetRef` for the candidates actually compared and preserve the comparison limit when no serious rival was identified. Use `evidenceReturnLoci[]` to say where later evidence, deduction, probe design, or assurance work can return; do not use those loci as evidence. Abductive plausibility comparison remains here. Use C.18 for archive or front claims, C.19 for live-pool policy, G.5 for a selector's selected-set declaration, or the direct comparison method when that distinct result is needed.

`AbductiveSearchUnfoldingStructure` is a local designation for an A.22.CGUS structure selected for an abductive-search question; it supplies no additional identity rule.

### B.5.2:5 - Archetypal Grounding

**Tell.** Abduction develops candidate conjectures from an admissible prompt through generation, consideration of serious alternatives and plausibility comparison.

**Show (System).** An operations team sees a recurring latency spike that existing explanations do not cover. They publish an `AnomalyStatement`, compare rival causes against current telemetry and mechanism knowledge, and retain a qualified prime conjecture. They name a possible discriminating probe.

**Show (Episteme).** A research group notices that two accepted results no longer fit together under one framing. It publishes a `ProbeCuePrompt`, enumerates several rival explanatory reframings, rejects the ones that fail scope fit or yield no interpretable implication, deduction or possible discriminating contrast, and advances one candidate explanation as the next working hypothesis.

### B.5.2:6 - Bias-Annotation

This pattern favors looking for serious alternatives, making plausibility grounds explicit and preserving prompt provenance.

### B.5.2:7 - Conformance Checklist

- `CC-B.5.2-1` Every abductive run **SHALL** begin from a question account whose content and grounds meet `B.5.2.0`'s `U.AbductivePrompt` entry conditions.
- `CC-B.5.2-2` A conforming abductive run **SHALL** make the serious candidates actually considered recoverable. When no serious rival has been identified, state that limit and qualify any preference claim by the available comparison.
- `CC-B.5.2-3` Selection of a prime hypothesis **SHALL** state the applicable plausibility criteria and grounds sufficient to justify its preference for the declared prompt and intended use.
- `CC-B.5.2-4` The selected prime hypothesis SHALL be published as a hypothesis-bearing `U.Episteme` with its scope, support and limitations. An assurance level, if a receiving use requires one, SHALL follow B.3.3's applicable justified profile rather than the fact that abduction occurred.
- `CC-B.5.2-5` The prime hypothesis record **SHALL** preserve a link to the initiating prompt and to the filtering rationale that justified selection.
- `CC-B.5.2-6` A conforming conjecture SHALL expose an interpretable implication, deduction or possible discriminating contrast. The availability and value of a check SHALL be considered separately before selecting evidence acquisition. An unavailable probe neither creates an observation nor by itself forbids a separately supported present decision.

### B.5.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Authority candidate** | One favored conjecture is advanced without considering serious alternatives or making its plausibility grounds explicit. | `CC-B.5.2-2` and `CC-B.5.2-3` preserve the candidates actually considered and the grounds for any preference. |
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

Iterative comparison keeps a candidate explanation open to revision as rival explanations and plausibility grounds change. A short publication can preserve the prompt, rival candidates and comparison rationale.

### B.5.2:12 - Relations

- **Supplies explanation-led abduction within:** B.5's hypothesis-led empirical inquiry, before deduction and induction.
- **Typically operates during:** `B.5.1 Exploration`.
- **Consumes:** `U.AbductivePrompt` publications from `B.5.2.0`, often reached through `B.4.1` and `A.16`.
- **Returns:** a hypothesis-bearing `U.Episteme` with explicit conjectural content, supports, fragilities and allowed use when a conjecture is selected; otherwise the justified abort, defer or split outcome.
- **Provides inputs for:** deduction, probe design and evidence synthesis when those questions are live. C.11 governs a separate feasible-action or acquisition choice; C.28 supplies needed causal-use support. Naming a possible experiment does not by itself fund or schedule its performance.
- **Uses:** C.28.CM when causal mechanisms and alternatives must be constructed before their implications can inform the plausibility comparison.
- **Coordinates with:** `A.22.CGUS` when the abductive prompt, `B.4.1` cue publication, rival hypotheses, plausibility constraints, evidence-return loci, and downstream tests must be inspected as an `AbductiveSearchUnfoldingStructure`.

#### B.5.2:12.1 - Prompt-entry broadening via `U.AbductivePrompt`

`B.5.2` accepts `U.AbductivePrompt`. `AnomalyStatement` is one canonical species alongside cue-derived prompt species such as `ProblemCuePrompt`, `OpportunityCuePrompt`, and `ProbeCuePrompt`.

### B.5.2:13 - Prompt, Candidate, and Hypothesis Package Discipline

Keep the **prompt**, the **candidate set**, and the **selected prime hypothesis** distinguishable in the publication. One paragraph can suffice when the question, rivals, selection grounds and outcome remain recoverable. Separate or link their expressions when independent revision or a receiving use needs that separation.

#### B.5.2:13.1 - Prompt package

A conforming prompt package should make explicit:

- the **prompt species** under `B.5.2.0` and its applicable conditions,
- the **open question** that makes abduction necessary,
- the **declared scope** under which the question is being posed,
- the **witnesses or provenance cues** that made the prompt worth preserving,
- and any **limitation of an existing explanation or model** that motivates the question.

Use the applicable wording-restoration pattern when the explanatory question, its scope or its intended meanings remain unclear: `A.6.P` for a relation, `A.6.A` for action-first wording, or `C.16.Q` for an evaluative term. Use an already adequate question account directly under `B.5.2.0`'s entry conditions.

#### B.5.2:13.2 - Candidate-set note

A candidate-set note preserves the candidates actually considered and the comparison they support. Make visible:

- candidate identifiers or short names,
- the differentiating claim each candidate adds,
- the principal plausibility supports and liabilities of each candidate,
- whether the candidate remains live, is deferred, or is rejected,
- and the interpretable implications, deductions or possible discriminating contrasts relevant to the comparison, with an availability limitation when it changes the receiving use.

Keep the serious alternatives actually considered and the limits of the comparison recoverable, including when no preference is warranted.

#### B.5.2:13.3 - Prime-hypothesis record

For a selected prime hypothesis, make these contents recoverable:

- the **selected candidate**,
- the **prompt** it answers,
- the **criteria and grounds** supporting its preference, with the limits of that comparison,
- the **scope** within which it is being advanced,
- the **allowed downstream use or next question**, which may concern deduction, a possible probe, a separately justified action or reconsideration; include availability limits when they change that use,
- and any **known fragilities** already visible at selection time.

These terms let the recipient choose a permitted continuation from the conjecture.

### B.5.2:14 - Admissible Transitions, Abort Paths, and Reopening

The abductive loop keeps its outcomes distinct so the recipient can tell whether it receives a qualified conjecture, deferred rivals, or a prompt that needs reopening. None of these outcomes by itself establishes an assurance level or an evidence-acquisition commitment.

#### B.5.2:14.1 - Relation to `B.4.1` and `A.16`

`B.4.1` and `A.16` can help preserve and clarify an initiating publication until it supplies an abductive prompt. `B.5.2` begins only once the current publication is ready to function as an abductive prompt. This boundary matters because it prevents two opposite errors:

- **premature abduction**, where a cue is used to begin rival comparison before its question account meets B.5.2.0's entry conditions;
- **delayed abduction**, where an admissible prompt still needs candidate comparison for the receiving question but remains in early cue form without that contribution.

#### B.5.2:14.2 - Abort, defer, and split cases

Not every abductive run should end in a prime hypothesis. Three non-selection outcomes are admissible:

1. **Abort.** The prompt dissolves because the initiating anomaly or opportunity was misread, duplicated, or already answered elsewhere.
2. **Defer.** The available candidates or grounds do not yet support a qualified conjecture or a warranted preference. Preserve any supported candidates and the unresolved explanatory or comparison question. A separately warranted present action may still proceed under C.11.
3. **Split.** When distinct questions require separate explanatory comparisons, distinguish those questions and their entry grounds. Continue the needed questions under their own prompt-entry conditions.


#### B.5.2:14.3 - Reopening and rival reinstatement

A prime hypothesis may later lose support under deduction, probe results, or new evidence. When that happens, `B.5.2` prefers explicit reopening to silent replacement.

A conforming reopening note should identify:

- which prior prime hypothesis is being reopened,
- whether a stored rival is being reinstated or a new candidate is entering,
- what change in evidence, scope, or internal contradiction triggered the reopening,
- and whether the explanatory question, its prompt account, or only the candidate ranking has changed. Apply `B.5.2.0:4.2.1–4.2.2`: a revised account may still concern the same question; a changed question needs its own entry grounds.


#### B.5.2:14.4 - Scope discipline during iteration

Abductive drift often comes from silent scope expansion. A conjecture first framed for one target slice quietly becomes a universal explanation. `B.5.2` therefore expects scope discipline to remain explicit during iteration. If a candidate requires a broader or narrower scope than the prompt originally declared, state that change before using the candidate at the new scope.

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

Suppose the mediating construct accounts for both claims within their warranted scopes, while the current scope-restriction and invariance alternatives each explain only one side of the mismatch. On those stated grounds, retain it as the provisional prime hypothesis. Keep the scope-restriction rival available for comparison if later deductions expose a failure in that account; revise the preference when the new grounds warrant it.

### B.5.2:16 - Authoring and Review Guidance

#### B.5.2:16.1 - For abductive-publication authors

For an abductive publication, make the prompt, serious candidates actually considered, plausibility grounds and outcome recoverable. If a prime hypothesis is warranted, explain its preference, allowed use and interpretable implication, deduction or possible discriminating contrast. Otherwise state the abort, defer or split outcome and its grounds under §14.2. Return to prompt-shaping or lexical repair when the question, scope or intended meanings remain unclear.

#### B.5.2:16.2 - For hypothesis reviewers

Hypothesis reviewers should not ask only whether the chosen hypothesis looks plausible. They should also ask:

- whether the prompt was typed in an admissible way,
- whether serious alternative explanations were considered and the actual candidate set and limits of comparison remain recoverable,
- whether the stated criteria and their grounds support the asserted preference, including any unresolved trade-offs,
- whether the selected hypothesis has an interpretable implication, deduction or possible discriminating contrast, with the availability and value of any check judged separately,
- and whether any scope inflation occurred during selection.


#### B.5.2:16.3 - For integrators and assurance leads

Integrators receive a qualified conjecture or the justified abort, defer or split outcome. For a conjecture, preserve its prompt, candidates considered, supports, comparison rationale, fragilities and allowed use. Use B.3.3 only for a receiving assurance question, C.11 for a feasible-action or evidence-acquisition choice, and C.28 for causal support when needed. An unavailable probe can leave the explanation unresolved while an independently warranted bounded service action remains useful; do not turn the conjecture into a mandatory work item.

### B.5.2:17 - Boundaries of abductive use

#### B.5.2:17.3 - Boundary to deduction and evidence

`B.5.2` ends with a qualified prime conjecture or an explicit abort, defer or split outcome. Deduction, evidence acquisition, synthesis, assurance and action choice remain separate questions. Naming their possible contribution states a downstream-use boundary; it does not require a new experiment, guarantee its availability or prevent a present decision already supported on other grounds.
### B.5.2:End
