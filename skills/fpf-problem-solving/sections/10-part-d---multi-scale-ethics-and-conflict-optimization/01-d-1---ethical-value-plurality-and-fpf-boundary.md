## D.1 - Ethical Value Plurality and FPF Boundary

> **Type:** D-family ethical boundary pattern
> **Status:** Stable
> **Pattern role:** This compact pattern gives the stable entry boundary and conformance checks for value-plurality use; fuller ethical theory remains outside FPF unless a direct pattern names it.

**Use this when.** Use this pattern when an FPF claim, method, work plan, architecture move, policy, recommendation, model, or system change has ethical force, but the value theory or ethical concern behind the claim is not yet explicit.

If that ethical claim is current but a possibly consequence-bearing System has not yet been identified, or the current affected-System set is not adequate, use `A.1.CSD` first. Return to D.1 with the bounded discovery account or its exact blocker; discovery alone does not make a claim ethical or complete the value frame.


**Not this pattern when.** If the current question is already a conflict across declared levels or scopes, use `D.3`. If the current question is how to mediate that conflict or use it in a decision, use `D.4`. If the current question is bias, fairness, human or group impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** FPF looks ethically neutral because it names evidence, method, architecture, or work but leaves the value frame and affected EntityOfConcern implicit.

**What this buys.** The reader can see whose concern is at issue, what is valued, and which ethical question to address next. A judgement additionally states its basis and the use that basis supports.

### D.1:1 - Problem Frame

FPF cannot prescribe one final ethics doctrine and still remain usable across engineering, research, organizational, public, and AI-enabled work. But FPF also cannot treat ethical neutrality as permission to omit ethics. Many working claims already carry values: who may be harmed, who benefits, which consequences count, which responsibilities are accepted, what evidence is enough, and which sacrifice is treated as admissible.

`D.1` supplies the boundary rule. When the ethical claim matters, make the value concern explicit enough that neighboring FPF patterns can inspect it. Do not hide it inside words such as "responsible", "safe", "fair", "humane", "acceptable", or "aligned" without saying what is being valued, for whom, in which context, and with what evidence.

### D.1:1.0 - Problem

Ethically loaded FPF claims often arrive as ordinary technical, architectural, method, evidence, or publication claims. The failure is that the reader cannot recover who or what is affected, what is valued, or what the ethical claim is meant to support. A conclusion can also overstate the evidence or hide a limitation that changes its use.

### D.1:1.1 - Forces

| Force | Tension |
| --- | --- |
| Value plurality vs. shared use | FPF must work across ethical traditions, but the current claim still needs an inspectable value frame. |
| Technical adequacy vs. ethical force | Evidence, assurance, method, architecture, or work quality may be strong while the value concern remains implicit. |
| Local usefulness vs. overreach | A bounded ethical claim can guide work, but it must not become universal moral permission. |
| Plain language vs. hidden doctrine | Words such as responsible, safe, fair, aligned, or humane are useful only after the valued object and affected parties are named. |
| Boundary entry vs. conflict handling | Use D.1 to surface the value frame, D.3 for conflict structure, D.4 for mediation, and D.5 for bias audit and assurance use. |

### D.1:2 - Solution

Start with the ethical claim or question, the affected EntityOfConcern, the value concern, and the present use of the answer. Name evidence and material uncertainty when the answer relies on them. If the task is to recognize the concern, a short statement of the value concern and next question completes that task; use `D.3` when its sides and tension need description.

To judge a use ethically admissible, explain how the value premises and available evidence support that judgement and where it remains limited. Recognizing a concern supplies neither that judgement nor permission to act.

Use an `EthicalValueFrame@Context` when the present reasoning or a later reader needs to compare value premises, distinguish the uses a judgement supports, or revisit a premise that can change it. This content can remain in the answer or an existing decision record. The following form groups the applicable content:

```text
EthicalValueFrame@Context:
  ethicalClaimRef
  affectedEntityOfConcernRef
  intendedEthicalUse
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  valueConcernRefs
  valueFrameEditionRefs?
  ethicalTheoryOrTraditionRefs?
  affectedHolonRefs?
  affectedSystemRefs?
  affectedEpistemeRefs?
  directResponsibilityRelationRefs?
  systemRoleAssignmentRefs?: FinSet(U.RelationRef constrained to U.SystemRoleAssignment)
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

Include a source-return condition when a particular stronger claim or changed use needs it. Use `C.11.DUA` when the contribution or burden of a proposed frame, report, or evidence request is unresolved. The form creates no obligation to invent a further check or explain an inactive one.

This frame makes the value premises inspectable; the ethical judgement still needs its own reasoning. A utilitarian consequence claim, a deontic constraint, a virtue or character claim, a care-ethics concern, a rights claim, a professional-duty claim, and a project-specific value trade-off may all be admissible starting points, but they must not be presented as the same claim merely because the same word "ethical" appears.

### D.1:3 - Boundaries

`D.1` keeps value plurality and FPF boundary discipline. It does not replace:

| Question | Subject pattern |
| --- | --- |
| Which levels, scopes, holons, interests, responsibilities, methods, work, and consequences are in ethical tension? | `D.3` |
| How should a mapped ethical conflict be mediated, refused, escalated, or used in a decision? | `D.4` |
| Is a model, metric, policy, publication, or release-bearing claim biased, unfair, or ethically unsafe? | `D.5` |
| Does the causal fairness claim have the required C.28 evidence value and verdict? | `C.28`, with `D.5` for ethical-audit use |
| Is there evidence for the claim? | `A.10` |
| Is an assurance claim being made? | `B.3` |
| Is an architecture residual current? | `C.30.ILC` |

### D.1:4 - Archetypal Grounding (Worked Slice)

A team says that a triage model is "ethical because it maximizes total benefit." Asked which ethical question this leaves open, the practitioner can answer: the claim values aggregate benefit, while equal access and avoidable subgroup harm may lead to a different judgement. The next question is how those concerns apply to the affected patients. That answer completes the initial recognition task.

If the team instead proposes this claim as a reason to adopt the model, identify the affected patients and institutions, the meaning of "total benefit", the consequence theory, the excluded concerns, the evidence relied on, and the use that evidence warrants. `D.3` describes any live conflict over access or harm; `D.4` governs its mediation or decision use.

### D.1:4.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Ethical label as permission | A word such as responsible or fair is treated as enough to act. | Name the value concern, affected EntityOfConcern, evidence, and admissible use. |
| One doctrine by default | The local text silently assumes one ethical theory while claiming neutrality. | Name the ethical theory, tradition, or project value frame when it changes the claim. |
| Technical proof substitutes for value frame | Evidence, model quality, or architecture adequacy is read as ethical adequacy. | Keep evidence-use and assurance patterns separate from the ethical value frame. |
| Ethics becomes universal owner | Every difficult concern is assigned to D.1. | Use D.1 only for value-frame boundary; return conflict, mediation, bias, causal, assurance, and architecture claims to their subject patterns. |

### D.1:5 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D1-1 | The ethical claim or question, affected EntityOfConcern, value concern, and intended use are named. Relied-on evidence and material uncertainty qualify the answer. Value-frame editions, ClaimScope, qualification window, affected Systems, and direct responsibility relations are added when they change the claim or its warranted use. | Keeps "ethical" from becoming a label without content or a generic context premise. |
| CC-D1-2 | A judgement of ethical admissibility states its warranted use and any limitation that changes it. A separate frame or stronger-source return serves a particular reasoning or receiving need. | Prevents value wording from authorizing action by itself. |
| CC-D1-3 | Ethical theory, tradition, or project-specific value frame is named when it changes the claim. | Keeps plural value frames inspectable. |
| CC-D1-4 | Multilevel conflict, mediation, bias or fairness audit, causal use, evidence, assurance, and architecture residuals use their subject patterns. | Keeps D.1 as boundary pattern rather than universal ethics owner. |

### D.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Neutrality theater | The work claims to avoid ethics by naming only technical evidence or method quality. | Recover the value concern or explicitly state that no ethical claim is being made. |
| Slogan ethics | Responsible, safe, humane, aligned, fair, or beneficial is used without affected parties and warranted use. | Name the affected parties, value concern, and intended claim; qualify the basis relied on. |
| Doctrine smuggling | A utilitarian, rights, duty, care, virtue, professional, or project-specific value frame is treated as obvious. | Name the value frame and the pattern for the stronger claim for any conflict. |
| Universal D.1 | D.1 is used to decide mediation, bias, causal fairness, or assurance. | Use D.3, D.4, D.5, C.28, A.10, B.3, or the subject pattern. |

### D.1:6 - Consequences

This pattern makes ethical claims portable across FPF without pretending that FPF has one final ethical theory. It also prevents a common failure: a technical pattern silently inherits one ethical theory because a word such as "safe", "fair", "beneficial", or "responsible" sounded ordinary.

Explicitness follows the claim being used: recognition needs a clear concern and next question, while a judgement needs its supporting basis and use limits. A durable frame earns its effort through the comparison or later reliance it supports.

### D.1:8 - Rationale

`D.1` is an entry boundary for ethical value plurality. It is intentionally modest: it does not settle ethical theory and does not decide an interlevel conflict. It makes the live value frame visible enough for neighboring FPF patterns to carry the next claim without hiding ethics inside technical adequacy, evidence, architecture, method, work, or publication wording.

This keeps FPF usable in engineering, research, organizational, public, and AI-enabled contexts where ethical traditions differ but value-bearing claims still need explicit affected entities, value concerns, and warranted use, with the evidence and return conditions that this use needs.

### D.1:9 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Value pluralism and applied ethics practice | FPF should not pretend that one ethical doctrine resolves every project claim; it should expose the current value concern, affected EntityOfConcern, and excluded concerns, and qualify the basis of the judgement being used. |
| Engineering ethics and assurance practice | A method, work plan, architecture move, recommendation, system, or holon can be technically adequate while shifting harm, benefit, responsibility, or coercion elsewhere; technical verification does not settle the ethical claim. |
| Human-impact, AI governance, and dual-use practice | Fairness, responsibility, alignment, safety, and misuse claims need affected parties, context, and warranted use; relied-on evidence and the consequence horizon qualify that use. |
| FPF subject-pattern discipline | Ethical entry does not absorb evidence, causality, assurance, architecture, or bias-audit owners. |

### D.1:10 - Relations

- Builds on `A.1` and `A.7` for EntityOfConcern and description distinction.
- Coordinates with `A.1.CSD` when a current ethical claim still lacks an adequate set of Systems that may bear consequences; D.1 consumes the returned account and does not add value fields to its neutral core.

- Coordinates with `A.10` for evidence, source currentness, and source-use relations.
- Coordinates with `C.11.DUA` when a proposed ethical record or evidence demand needs appraisal of its contribution, feasibility, burden, or requirement merits.
- Coordinates with `B.3` when an assurance claim is current.
- Coordinates with `D.2`, `D.3`, `D.4`, and `D.5` for multilevel entry, conflict structure, mediation, bias audit, causal-fairness audit consumption, and ethical assurance.
- Coordinates with `C.28` for causal fairness use and with `C.30.ILC` when an architecture residual is current.

### D.1:End
