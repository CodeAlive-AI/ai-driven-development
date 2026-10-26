## D.1 - Clarify an Ethical Claim's Value Basis (Value Plurality)

> **Type:** D-family ethical boundary pattern
> **Status:** Stable

**Use this when.** Use this pattern when the value basis of an ethical claim or proposed action is unclear.

If that ethical claim is current but a possibly consequence-bearing System has not yet been identified, or the current affected-System set is not adequate, use `A.1.CSD` first. Return to D.1 with the bounded discovery account or the reason identification remains unresolved. Use that account to clarify the value concern.


**Not this pattern when.** If the current question is already a conflict across declared levels or scopes, use `D.3`. If the current question is how to mediate that conflict or use it in a decision, use `D.4`. If the current question is bias, fairness, human or group impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** FPF looks ethically neutral because it names evidence, method, architecture, or work but leaves the value frame and affected EntityOfConcern implicit.

**What this buys.** The reader can see whose concern is at issue, what is valued, and which ethical question to address next. For a judgement, the reader can recover how the value premises and relevant facts support the conclusion, what changes when a premise changes, and which use the reasoning warrants.

### D.1:1 - Problem Frame

FPF cannot prescribe one final ethics doctrine and still remain usable across engineering, research, organizational, public, and AI-enabled work. But FPF also cannot treat ethical neutrality as permission to omit ethics. Many working claims already carry values: who may be harmed, who benefits, which consequences count, which responsibilities are accepted, what evidence is enough, and which sacrifice is treated as admissible.

When a value concern matters, state what is valued, for whom and under which conditions. Explain the value premise and identify any factual evidence on which the judgement relies.

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

#### D.1:2.1 - Make the value premise do explanatory work

A value label identifies a concern; a reason explains why that concern supports the proposed judgement. State the value premise, the relevant facts and the step joining them. For example, a prediction of greater aggregate benefit can support a recommendation only under a premise giving that benefit the relevant priority. A right can constrain the recommendation under a different premise even when the prediction is correct. Use `B.5.RA` when the argument must be recovered from a source, including a rhetorical question or an analogy.

Keep the grounds of acceptance distinct. Evidence can support a claim about consequences or the conditions in which a person agreed. A normative premise states what ought to count, what may be required or which treatment is permissible. Explaining a tradition's history can help interpret its premise; neither that history nor a model of a system establishes the premise's moral authority. When the premise is contested, preserve the conditional conclusion and identify what accepting another premise would change.

The following argument develops one such conditional basis for decisions about people's participation. It supplies reasons that can be examined and applied; FPF does not select this basis as its final ethical doctrine.

#### D.1:2.2 - Personal authority, voluntary participation and reciprocal limits

Use this reasoning when a proposal treats a person's body, work or participation as available because a planner can describe a useful larger system. The question is who may decide that person's contribution, on what grounds and within what limits.

##### D.1:2.2.1 - State the normative starting point

One possible starting point gives each person presumptive moral authority over the use of their own body and participation. On this view, another person's valuable plan creates a reason to request cooperation, but the value of that plan alone does not authorize the required personal contribution. This is a claim about how people should be treated, not a claim that they always control their circumstances.

Some accounts develop this position through **self-ownership**. The working claim here is the stated personal authority; a stronger ownership theory needs its further premises. Whether rights can be transferred, which rights cannot be waived, and which obligations qualify them are substantive ethical questions. A person's moral standing is also distinct from their present ability to decide or act. Children and people temporarily unable to decide do not become resources available to a planner; a protective or representative arrangement needs its own basis and limits.

For this argument, accept a second premise: comparable persons have the same presumptive standing, and a difference in treatment needs a relevant reason. Equal standing does not mean equal knowledge, skill, resources or preferences. Those differences can change who can perform work or give useful advice without establishing a right to command another person.

##### D.1:2.2.2 - Use reciprocity to expose a missing justification

Suppose a designer claims that knowing how to improve a project permits imposing its work on another person, while denying that the other person may impose work on the designer under comparable conditions. With the equal-standing premise, the designer's identity cannot justify this asymmetry. A relevant difference must do the work: for example, an applicable commitment or a justified authority limited to that decision. If no such difference is established, either the special permission must be withdrawn or the equal-standing premise must be rejected and the alternative defended.

This is the useful force of the reciprocal question: what would justify the same rule when the positions are exchanged? Preserve the facts that matter to the rule, including a real mandate, vulnerability and effects on others. Asking only whether the proposer personally likes the treatment is weaker: people have different preferences, and someone willing to endure a burden may still lack permission to impose it on others. Reciprocity examines the consistency and grounds of the proposed rule; it does not independently prove the starting premises or settle every conflict.

Combined with the personal-authority premise, the result is a reason to seek an authorized contribution rather than count the person as already available. When no applicable prior commitment or other justified authority covers the move, a plan requires the person's valid agreement or a different way of obtaining the result. Reusing an adequate existing commitment within its limits does not require asking for permission again.

##### D.1:2.2.3 - Explain what consent can authorize

Consent matters under this value basis because it lets the person exercise the authority the premise assigns to them. It must concern the proposed act or a sufficiently clear class of acts. A signature, silence or presence in a group cannot establish its scope and validity without the circumstances that give that response its meaning.

Examine the information and understanding needed for this choice, the person's decision capacity, the pressure involved and the practical ability to refuse. Where a person's agreement is obtained through a threat of a penalty that the adopted ethical basis does not justify, that compliance does not supply voluntary consent. Dependence or limited alternatives can make voluntariness doubtful; their presence calls for a judgement under the applicable ethical and domain standards, rather than an automatic inference either of valid consent or of its absence.

An agreement to contribute gives the recipient only the authorization it actually supplies. Agreeing to a defined task need not authorize a new purpose, wider disclosure or another person's participation. The applicable basis must also establish the conditions for changing or ending a commitment; permission to begin does not by itself answer every question about withdrawal. Some protections may remain non-waivable under that basis. Consent between two parties cannot by itself dispose of a third party's rights or settle harm imposed on that party.

When consent is absent or insufficient, retain the unmet condition. A narrower task, different terms, supported voluntary participation or another provider can sometimes meet the project's purpose. Where the question is which alternative to choose or how to resolve a conflict with another duty, use `D.3` and `D.4`.

##### D.1:2.2.4 - Keep system structure and rights separate

A person can participate in an organization or be a physical component of a working arrangement while retaining moral claims against what that arrangement demands. Describing the organization's useful function does not establish a duty to serve it. Conversely, a person's refusal does not establish that every obligation they previously undertook has disappeared. Identify the proposed act and the relation that could authorize it.

Ownership of a tool, authority over work, membership in a group and physical part-whole relations answer different questions. Treating possessions as an extension of a person may express a moral argument for protecting them, but extending the personal-authority premise to property requires an account of legitimate possession and its limits. It does not make every owned object a physical part of its owner. Likewise, a sponsor's control of funds or equipment does not confer control over every person the project affects.

Dissolving an organization and killing its members have different consequences. A model that calls both entities living systems cannot supply the missing ethical comparison. Investigate the actual consequences for people, including dependence on the organization and the costs of transition, instead of deriving either unconditional preservation or harmless dissolution from the metaphor.

##### D.1:2.2.5 - Identify the premise that changes the conclusion

A consent-based account can recognize duties to others and limited powers that do not depend on consent to each individual act. Their justification must be supplied rather than hidden in the word "system". A valid employment commitment may authorize a bounded assignment. A protective duty or public authority may be offered as another basis; its source, scope, safeguards and application need the relevant ethical and domain reasoning. Calling compliance consent would conceal the difference.

Other value frames can give different reasons for the same decision. A consequence-based account asks whether the proposed intervention produces better supported outcomes than feasible alternatives, with its chosen treatment of distribution and rights. A public-justification account asks whether the governing rule and its unequal powers can be justified to those subject to it, including a basis for binding dissenters. A care-based account may give special weight to dependence and responsibilities arising from a relationship. These lines can support or oppose a particular use of authority; none follows merely from system scale or the number of supporters.

Locate the disagreement: the standing assigned to persons, the priority of a duty, the validity of an authorization, a predicted consequence or the interpretation of a rule. That tells the practitioner what could change the judgement. A conditional argument for voluntary cooperation establishes neither that all public projects fail nor that every collective decision needs unanimous consent. Whether an artificial system has moral standing is also a separate question from whether it can pursue goals or perform a task.

The practical result is an explained boundary on a proposed action: which contribution may be requested or required under which premises, which agreement or authority supports it, and what remains unresolved. `D.3` describes a resulting value conflict; `D.4` develops and compares ways to continue.

### D.1:3 - Boundaries

`D.1` keeps value plurality and FPF boundary discipline. It does not replace:

| Question | Subject pattern |
| --- | --- |
| Which levels, scopes, holons, interests, responsibilities, methods, work, and consequences are in ethical tension? | `D.3` |
| How should a mapped ethical conflict be mediated, refused, escalated, or used in a decision? | `D.4` |
| Is a model, metric, policy, publication, or release-bearing claim biased, unfair, or ethically unsafe? | `D.5` |
| Does the causal fairness claim have the required C.28 evidence value and verdict? | `C.28`, with `D.5` for ethical-audit use |
| Is the ethical claim supported, and can that support be relied on for this use? | The applicable subject and evidence patterns for support; `A.10` for bounded reliance on the result |
| Is an assurance claim being made? | `B.3` |
| Is an architecture residual current? | `C.30.ILC` |

### D.1:4 - Archetypal Grounding (Worked Slice)

A team says that a triage model is "ethical because it maximizes total benefit." Asked which ethical question this leaves open, the practitioner can answer: the claim values aggregate benefit, while equal access and avoidable subgroup harm may lead to a different judgement. The next question is how those concerns apply to the affected patients. That answer completes the initial recognition task.

If the team instead proposes this claim as a reason to adopt the model, identify the affected patients and institutions, the meaning of "total benefit", the consequence theory, the excluded concerns, the evidence relied on, and the use that evidence warrants. `D.3` describes any live conflict over access or harm; `D.4` governs its mediation or decision use.

#### D.1:4.2 - A project needs a person's contribution

A community workshop has adopted a personal-authority premise for voluntary participation. Its coordinator wants members to carry location trackers during a festival so that help can be dispatched quickly. The equipment sponsor approves the plan. Members had agreed to specified volunteer shifts, with no agreement to continuous tracking.

The benefit of faster dispatch gives a reason to propose tracking, while the sponsor's approval covers the supplied equipment. Neither supplies the members' missing agreement. Under the adopted premise, the coordinator must obtain valid agreement to the proposed information use or construct another arrangement. The reciprocal question exposes the missing ground: the coordinator would also need a reason for letting another organizer collect the coordinator's movements merely because it helped that organizer's project.

Suppose members understand the purpose and retention period, can decline without losing access to ordinary workshop services, and can instead report availability at agreed intervals. A member's agreement can authorize the limited tracking described. It does not authorize publishing a route that reveals a nonparticipant's location; that changed effect needs its own consideration. The alternative reporting arrangement also shows why a useful dispatch purpose need not require the initially chosen means.

Now change the question to an ordinary task within a member's already accepted shift. If the established agreement authorizes the coordinator to allocate that task, the personal-authority premise does not require a new consent ceremony. Recover the actual scope and any remaining constraints. If the proposed tracking is instead claimed to be mandatory under an applicable safety rule, establish that rule and its ethical basis; voluntary consent is no longer the explanation for the mandate. These different conclusions arise from changed grounds of authority, not from a change in the person's status.

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
| CC-D1-3 | Ethical theory, tradition, or project-specific value frame is named when it changes the claim. A conditional judgement preserves its value premises, relevant facts and inference; a contested premise remains identifiable. | Keeps plural value frames inspectable and reasoning recoverable. |
| CC-D1-4 | Multilevel conflict, mediation, bias or fairness audit, causal use, evidence, assurance, and architecture residuals use their subject patterns. | Keeps D.1 as boundary pattern rather than universal ethics owner. |

### D.1:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Neutrality theater | The work claims to avoid ethics by naming only technical evidence or method quality. | Recover the value concern or explicitly state that no ethical claim is being made. |
| Slogan ethics | Responsible, safe, humane, aligned, fair, or beneficial is used without affected parties and warranted use. | Name the affected parties, value concern, and intended claim; qualify the basis relied on. |
| Doctrine smuggling | A utilitarian, rights, duty, care, virtue, professional, or project-specific value frame is treated as obvious. | State the normative premise and how it supports the judgement; use D.3 when the disagreement forms an ethical conflict. |
| Universal D.1 | D.1 is used to decide mediation, bias, causal fairness, or assurance. | Use D.3, D.4, D.5, C.28, A.10, B.3, or the subject pattern. |

### D.1:6 - Consequences

Explicit value premises let readers compare ethical claims and identify where their grounds differ.

Explicitness follows the claim being used: recognition needs a clear concern and next question, while a judgement needs its supporting basis and use limits. A durable frame earns its effort through the comparison or later reliance it supports.

For decisions about people, the conditional argument in :2.2 makes a practical difference: the planner can distinguish a valued result from authority to require a person's contribution, reuse an adequate commitment, and identify when consent, another justification or a different means is still needed. It also shows which disagreement concerns the normative basis rather than a missing technical fact.

### D.1:8 - Rationale

D.1 connects a value concern with the premises and facts needed to assess its use. Revealing that connection lets a reader identify whether a disagreement concerns values, facts or authority and direct the unresolved question to the appropriate method.

This keeps FPF usable in engineering, research, organizational, public, and AI-enabled contexts where ethical traditions differ but value-bearing claims still need explicit affected entities, value concerns, and warranted use, with the evidence and return conditions that this use needs.

### D.1:9 - SoTA-Echoing

| Source line | Practical implication for this pattern |
| --- | --- |
| Value pluralism and applied ethics practice | FPF should not pretend that one ethical doctrine resolves every project claim; it should expose the current value concern, affected EntityOfConcern, and excluded concerns, and qualify the basis of the judgement being used. |
| Engineering ethics and assurance practice | A method, work plan, architecture move, recommendation, system, or holon can be technically adequate while shifting harm, benefit, responsibility, or coercion elsewhere; technical verification does not settle the ethical claim. |
| Human-impact, AI governance, and dual-use practice | Fairness, responsibility, alignment, safety, and misuse claims need affected parties, context, and warranted use; relied-on evidence and the consequence horizon qualify that use. |
| Developed consent reasoning in the [Belmont Report, “Respect for Persons” and “Informed Consent”](https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html) (1979), [UNESCO bioethics declaration, Articles 5–7](https://www.unesco.org/en/legal-affairs/universal-declaration-bioethics-and-human-rights) (2005), and [Declaration of Helsinki, paragraphs 25–30](https://www.wma.net/policies-post/wma-declaration-of-helsinki/) (2024) | Adapt their distinction between a stated personal concern and valid consent, including capacity, dependence and representation. These developed domain treatments keep consent connected to reasons and limits; they do not establish a universal political doctrine. Section :2.2 uses that explanatory discipline while leaving domain requirements with their sources. |
| FPF subject-pattern discipline | Ethical entry does not absorb evidence, causality, assurance, architecture, or bias-audit owners. |

### D.1:10 - Relations

- Builds on `A.1` and `A.7` for EntityOfConcern and description distinction.
- Coordinates with `A.1.CSD` when a current ethical claim still lacks an adequate set of Systems that may bear consequences; D.1 consumes the returned account and does not add value fields to its neutral core.

- Coordinates with `B.5.RA` when the ethical argument must be recovered from a source and with `B.5.RR` when a changed premise requires revising its conclusions.
- Coordinates with `A.10` for descriptive provenance and bounded reliance on the source or evidence used.
- Coordinates with `C.11.DUA` when a proposed ethical record or evidence demand needs appraisal of its contribution, feasibility, burden, or requirement merits.
- Coordinates with `B.3` when an assurance claim is current.
- Use `D.2` to recognize concerns across levels and scopes, `D.3` to describe conflicts, `D.4` to develop and compare continuations, and `D.5` to select and interpret an ethical audit.
- Coordinates with `C.28` for causal fairness use and with `C.30.ILC` when an architecture residual is current.

### D.1:End
