## D.4 - Ethical Mediation and Decision Use

> **Type:** D-family ethical mediation and decision-use pattern
> **Status:** Stable
> **Pattern role:** This compact pattern owns the ethical use of an already mapped conflict: mediation, refusal, evidence demand, bounded decision use, and residual handling.

**Use this when.** Use this pattern when an interlevel ethical conflict structure from `D.3` must be used for mediation, refusal, decision, evidence demand, causal return, assurance return, or architecture return.

**Not this pattern when.** If the conflict structure is not yet mapped, use `D.3`. If the issue is only value plurality, use `D.1`. If the issue is only entry recognition, use `D.2`. If the current work is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** A mapped ethical conflict is treated as solved, blocked, or decision-ready without naming mediation, refusal, evidence demand, return, accepted residual, or bounded decision use.

**What this buys.** The practitioner can use a `D.3` conflict structure for one admissible mediation action or bounded decision use while keeping evidence, causality, assurance, architecture, and bias-audit claims with their owners.

### D.4:1 - Problem Frame

Once an interlevel ethical conflict is visible, the next risk is premature closure. A team may declare a compromise before evidence is sufficient, turn an assurance input into ethical permission, use one level's value as a trump card, or hide a refusal behind technical language.

`D.4` governs the use of the mapped conflict. It does not make FPF a final moral authority. It asks what move is admissible from the current conflict structure and what must return to evidence, causality, assurance, architecture, decision, or value framing before action is justified.

### D.4:1.0 - Problem

A mapped ethical conflict can still be used badly. The failure is to treat a conflict structure, assurance input, formula, or architecture return as if it already selected a compromise, refusal, evidence demand, accepted residual, or bounded decision use.

### D.4:1.1 - Forces

| Force | Tension |
| --- | --- |
| Mapped conflict vs. premature closure | A conflict structure makes action discussable, but does not by itself decide compromise, refusal, or permission. |
| Evidence demand vs. decision pressure | Work may need a decision, while the ethical claim still needs stronger evidence, causal analysis, assurance, or architecture return. |
| Mediation vs. universal authority | D.4 can govern one bounded use of a mapped conflict, but cannot become a general decision theory. |
| Residual acceptance vs. hidden harm | Proceeding under residual harm can be admissible only when residuals, responsibility-bearing role assignments, and return conditions are explicit. |
| Mathematical allocation vs. ethical decision | A formula or optimization can inform a decision, but it is not the ethical decision by itself. |

### D.4:2 - Solution

Record an `EthicalMediationDecisionUse@Context`:

```text
EthicalMediationDecisionUse@Context:
  conflictStructureRef
  boundedContextRef
  valueFrameRefs
  decisionQuestionRef?
  optionRefs
  proposedMediationRefs?
  refusalOrStopCondition?
  evidenceDemandRefs?
  causalReturnRefs?
  assuranceReturnRefs?
  architectureResidualReturnRefs?
  acceptedResidualRefs?
  decisionRecordRefs?
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

The record names the current ethical use of the conflict: mediate, refuse, continue under explicit residual, demand evidence, ask a causal question, ask for assurance, return to architecture, or make a bounded decision.

### D.4:3 - Mediation Moves

| Current situation | Admissible D.4 move | Neighboring owner |
| --- | --- | --- |
| A compromise is proposed but the conflict structure has missing levels, scopes, or affected holons. | Return to `D.3` and complete the conflict structure. | `D.3` |
| Harm claim depends on causal effect. | Demand the C.28 causal-use evidence value and verdict before ethical decision use. | `C.28` |
| Evidence is too weak or outdated. | Demand stronger or fresher evidence before mediation. | `A.10`, `C.27` |
| Assurance claim is being used as ethical permission. | Keep assurance as an assurance or evidence relation, not moral authorization. | `B.3`, `D.5` |
| Architecture move reduces one residual but creates ethical conflict elsewhere. | Return the architecture residual and keep the ethical conflict distinct. | `C.30.ILC`, `D.3` |
| A decision must proceed with residual harm. | Record the accepted residual, responsible role assignments, evidence limits, and return condition. | `C.11`, `B.3`, `D.5` as needed |

### D.4:4 - Archetypal Grounding (Worked Slices)

**Fair-share case.** A service outage plan can protect hospitals, households, or industrial customers, but not all at once. `D.3` maps affected scopes and value concerns. `D.4` records the mediation use: options, accepted residuals, evidence demand, role assignments for decision responsibility, and return conditions. A mathematical allocation method may be cited through `C.29`, but the allocation formula is not the ethical decision by itself.

**Override case.** An assurance review says a release has the required technical assurance relation, but `D.3` shows unresolved harm for a subgroup. `D.4` does not let assurance override the ethical conflict. It records whether release is refused, conditioned, delayed for evidence, returned to C.28 causal-use analysis, or allowed with explicit residual and responsibility.

### D.4:5 - Boundaries

`D.4` does not own conflict structure, bias audit, ethical assurance, architecture residual, causal identification, evidence provenance, or decision theory in general. It owns the ethical use of a mapped interlevel conflict.

Do not name a mediation move "calculus" unless a mathematical lens is selected and the lens is actually doing work. Do not name a mediation move "operator" unless the current pattern explicitly governs an operation. Most D.4 use is a bounded decision-use record, not a mathematical object.

### D.4:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Conflict map becomes decision | A D.3 structure is treated as if it already selected an action. | Name the D.4 move and its admissible use. |
| Assurance becomes permission | Technical assurance is read as ethical authorization. | Keep assurance as an assurance or evidence relation and record the ethical use separately. |
| Formula becomes ethics | Allocation, optimization, or scoring is treated as the ethical decision. | Use `C.29` for the mathematical lens and keep D.4 responsible for bounded ethical use. |
| Residual harm disappears | Work proceeds while residuals and responsibility-bearing assignments stay unnamed. | Name accepted residuals, role assignments, evidence limits, and return condition. |

### D.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D4-1 | A `conflictStructureRef` from D.3 is present or the use returns to D.3. | Prevents mediation without mapped conflict. |
| CC-D4-2 | The record names the current admissible move: mediate, refuse, demand evidence, return to causal, assurance, or architecture owner, decide with residual, or stop. | Keeps ethical use explicit. |
| CC-D4-3 | Evidence, causality, assurance, architecture, and decision claims use their direct owners. | Prevents D.4 from becoming universal decision authority. |
| CC-D4-4 | Accepted residuals and responsibility-bearing role assignments are named when proceeding under residual harm. | Keeps bounded decision use reviewable. |

### D.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Decision-ready by map | The mapped conflict is treated as solved. | Choose a D.4 move: mediate, refuse, demand evidence, return, decide with residual, or stop. |
| Trump-card level | One level's value automatically overrides all others. | Return to D.3 if the level relation or value frame is incomplete; otherwise record the explicit D.4 use. |
| Evidence postponement | The team proceeds while saying evidence can be checked after the decision. | Demand evidence, causal analysis, assurance, or architecture return before the decision use, unless residual acceptance is explicit. |
| Permission by assurance | A passed assurance relation is treated as moral authorization. | Keep B.3 assurance and D.4 ethical use distinct. |

### D.4:7 - Consequences

This pattern makes ethical action reviewable without pretending that every conflict has a clean optimum. It preserves refusal, evidence demand, and residual acceptance as first-class outcomes. It also prevents architecture, assurance, or causal evidence from quietly becoming moral permission.

### D.4:9 - Rationale

`D.4` exists because an inspectable ethical conflict still needs a bounded use. Some uses stop work. Some demand evidence. Some return to causal, assurance, or architecture owners. Some proceed under an accepted residual with named responsibility and return conditions. Without this pattern, teams either freeze because conflict exists or move too fast because the conflict was mapped once.

The pattern keeps refusal, evidence demand, and residual acceptance visible as ordinary outcomes. It also prevents formulas, assurance labels, architecture residual repairs, or causal claims from silently becoming moral authorization.

### D.4:10 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Decision analysis and applied ethics | Mediation and decision use need options, refusal, condition, evidence-demand choices, accepted residuals, responsibility, and return conditions, not only a value slogan. |
| Safety and assurance practice | Assurance can inform bounded ethical decision use, but does not authorize action under unresolved harm or replace D.3 conflict structure. |
| Causal and evidence governance | Harm, benefit, and fairness claims depending on causal effect or weak evidence must return to `C.28`, `A.10`, or `B.3` before ethical decision use. |
| FPF mathematical-lens discipline | Optimization, allocation, scoring, Pareto, and threshold reasoning are selected lenses or measurement claims; they do not replace the D.4 ethical-use record or create a universal optimizer. |

### D.4:11 - Relations

- Builds on `D.3` for the mapped conflict structure.
- Coordinates with `D.1` and `D.2` when value frame or multilevel entry is incomplete.
- Coordinates with `D.5` when bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance is current.
- Coordinates with `A.10`, `B.3`, `C.11`, `C.28`, `C.29`, and `C.30.ILC` when evidence, assurance, decision, causal, mathematical-lens, or architecture-residual claims are current.

### D.4:End

