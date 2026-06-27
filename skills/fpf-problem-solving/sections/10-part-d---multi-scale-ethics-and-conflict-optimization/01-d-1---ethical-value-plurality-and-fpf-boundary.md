## D.1 - Ethical Value Plurality and FPF Boundary

> **Type:** D-family ethical boundary pattern
> **Status:** Stable
> **Pattern role:** This compact pattern gives the stable entry boundary and conformance checks for value-plurality use; fuller ethical theory remains outside FPF unless a direct pattern names it.

**Use this when.** Use this pattern when an FPF claim, method, work plan, architecture move, policy, recommendation, model, or system change has ethical force, but the value theory or ethical concern behind the claim is not yet explicit.

**Not this pattern when.** If the current question is already a conflict across declared levels or scopes, use `D.3`. If the current question is how to mediate that conflict or use it in a decision, use `D.4`. If the current question is bias, fairness, human or group impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** FPF looks ethically neutral because it names evidence, method, architecture, or work but leaves the value frame and affected EntityOfConcern implicit.

**What this buys.** The ethical concern becomes a bounded FPF claim with value frame, affected EntityOfConcern, evidence, admissible use, and direct next owner.

### D.1:1 - Problem Frame

FPF cannot prescribe one final ethics doctrine and still remain usable across engineering, research, organizational, public, and AI-enabled work. But FPF also cannot treat ethical neutrality as permission to omit ethics. Many working claims already carry values: who may be harmed, who benefits, which consequences count, which responsibilities are accepted, what evidence is enough, and which sacrifice is treated as admissible.

`D.1` supplies the boundary rule. When the ethical claim matters, make the value concern explicit enough that neighboring FPF patterns can inspect it. Do not hide it inside words such as "responsible", "safe", "fair", "humane", "acceptable", or "aligned" without saying what is being valued, for whom, in which context, and with what evidence.

### D.1:1.0 - Problem

Ethically loaded FPF claims often arrive as ordinary technical, architectural, method, evidence, or publication claims. The failure is not that the text lacks moral vocabulary; the failure is that the affected EntityOfConcern, value concern, evidence, admissible use, and stronger-source return condition are not explicit enough to inspect.

### D.1:1.1 - Forces

| Force | Tension |
| --- | --- |
| Value plurality vs. shared use | FPF must work across ethical traditions, but the current claim still needs an inspectable value frame. |
| Technical adequacy vs. ethical force | Evidence, assurance, method, architecture, or work quality may be strong while the value concern remains implicit. |
| Local usefulness vs. overreach | A bounded ethical claim can guide work, but it must not become universal moral permission. |
| Plain language vs. hidden doctrine | Words such as responsible, safe, fair, aligned, or humane are useful only after the valued object and affected parties are named. |
| Boundary entry vs. conflict handling | D.1 should surface the value frame, while D.3, D.4, and D.5 own conflict structure, mediation, bias audit, and assurance use. |

### D.1:2 - Solution

Recover an `EthicalValueFrame@Context` before treating the claim as ethically admissible:

```text
EthicalValueFrame@Context:
  ethicalClaimRef
  affectedEntityOfConcernRef
  boundedContextRef
  valueConcernRefs
  ethicalTheoryOrTraditionRefs?
  affectedHolonRefs?
  affectedEpistemeRefs?
  roleAssignmentRefs?
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs
  uncertaintyOrCurrentnessCondition
  admissibleUse
  inadmissibleOverread
  strongerSourceReturnCondition
```

This frame does not settle the ethical question. It makes the value frame inspectable. A utilitarian consequence claim, a deontic constraint, a virtue or character claim, a care-ethics concern, a rights claim, a professional-duty claim, and a project-specific value trade-off may all be admissible starting points, but they must not be presented as the same claim merely because the same word "ethical" appears.

### D.1:3 - Boundaries

`D.1` keeps value plurality and FPF boundary discipline. It does not replace:

| Question | Direct owner |
| --- | --- |
| Which levels, scopes, holons, interests, responsibilities, methods, work, and consequences are in ethical tension? | `D.3` |
| How should a mapped ethical conflict be mediated, refused, escalated, or used in a decision? | `D.4` |
| Is a model, metric, policy, publication, or release-bearing claim biased, unfair, or ethically unsafe? | `D.5` |
| Does the causal fairness claim have the required C.28 evidence value and verdict? | `C.28`, with `D.5` for ethical-audit use |
| Is there evidence for the claim? | `A.10` |
| Is an assurance claim being made? | `B.3` |
| Is an architecture residual current? | `C.30.ILC` |

### D.1:4 - Archetypal Grounding (Worked Slice)

A team says that a triage model is "ethical because it maximizes total benefit." `D.1` does not accept the phrase as a finished ethical judgment. It records the affected patients and institutions, the value concern called "total benefit", the consequence theory being used, the excluded concerns such as equal access or avoidable harm to a subgroup, the evidence set, and the admissible use of the claim. If equal access or subgroup harm becomes live, `D.3` maps the conflict and `D.4` governs mediation or decision use.

### D.1:4.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Ethical label as permission | A word such as responsible or fair is treated as enough to act. | Name the value concern, affected EntityOfConcern, evidence, and admissible use. |
| One doctrine by default | The local text silently assumes one ethical theory while claiming neutrality. | Name the ethical theory, tradition, or project value frame when it changes the claim. |
| Technical proof substitutes for value frame | Evidence, model quality, or architecture adequacy is read as ethical adequacy. | Keep evidence and assurance owners separate from the ethical value frame. |
| Ethics becomes universal owner | Every difficult concern is assigned to D.1. | Use D.1 only for value-frame boundary; return conflict, mediation, bias, causal, assurance, and architecture claims to their owners. |

### D.1:5 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D1-1 | The value concern, affected EntityOfConcern, bounded context, and evidence refs are named. | Keeps "ethical" from becoming a label without content. |
| CC-D1-2 | The text states admissible use and non-admissible overread for the ethical claim. | Prevents value wording from authorizing action by itself. |
| CC-D1-3 | Ethical theory, tradition, or project-specific value frame is named when it changes the claim. | Keeps plural value frames inspectable. |
| CC-D1-4 | Multilevel conflict, mediation, bias or fairness audit, causal use, evidence, assurance, and architecture residuals use their direct owners. | Keeps D.1 as boundary pattern rather than universal ethics owner. |

### D.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Neutrality theater | The work claims to avoid ethics by naming only technical evidence or method quality. | Recover the value concern or explicitly state that no ethical claim is being made. |
| Slogan ethics | Responsible, safe, humane, aligned, fair, or beneficial is used without affected parties and admissible use. | Fill `EthicalValueFrame@Context`. |
| Doctrine smuggling | A utilitarian, rights, duty, care, virtue, professional, or project-specific value frame is treated as obvious. | Name the value frame and the stronger owner for any conflict. |
| Universal D.1 | D.1 is used to decide mediation, bias, causal fairness, or assurance. | Return to D.3, D.4, D.5, C.28, A.10, B.3, or the direct owner. |

### D.1:6 - Consequences

This pattern makes ethical claims portable across FPF without pretending that FPF has one final ethical theory. It also prevents a common failure: a technical pattern silently inherits one ethical theory because a word such as "safe", "fair", "beneficial", or "responsible" sounded ordinary.

The cost is extra explicitness. The gain is that ethics becomes reviewable in the same FPF body as systems, methods, work, evidence, assurance, architecture, and publication use.

### D.1:8 - Rationale

`D.1` is an entry boundary for ethical value plurality. It is intentionally modest: it does not settle ethical theory and does not decide an interlevel conflict. It makes the live value frame visible enough for neighboring FPF patterns to carry the next claim without hiding ethics inside technical adequacy, evidence, architecture, method, work, or publication wording.

This keeps FPF usable in engineering, research, organizational, public, and AI-enabled contexts where ethical traditions differ but value-bearing claims still need explicit affected entities, evidence, admissible use, and stronger-source return conditions.

### D.1:9 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Value pluralism and applied ethics practice | FPF should not pretend that one ethical doctrine resolves every project claim; it should name the current value frame, affected EntityOfConcern, excluded concerns, evidence, and admissible use before an ethical claim guides work. |
| Engineering ethics and assurance practice | A method, work plan, architecture move, recommendation, system, or holon can be technically adequate while shifting harm, benefit, responsibility, or coercion elsewhere; technical verification does not settle the ethical claim. |
| Human-impact, AI governance, and dual-use practice | Fairness, responsibility, alignment, safety, and misuse words need affected parties, context, consequence horizon, evidence, and admissible use before they guide action. |
| FPF direct-owner discipline | Ethical entry does not absorb evidence, causality, assurance, architecture, or bias-audit owners. |

### D.1:10 - Relations

- Builds on `A.1` and `A.7` for EntityOfConcern and description distinction.
- Coordinates with `A.10` for evidence, source currentness, and source-use relations.
- Coordinates with `B.3` when an assurance claim is current.
- Coordinates with `D.2`, `D.3`, `D.4`, and `D.5` for multilevel entry, conflict structure, mediation, bias audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `C.28` for causal fairness use and with `C.30.ILC` when an architecture residual is current.

### D.1:End

