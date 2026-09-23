## D.4 - Ethical Mediation and Decision Use

> **Type:** D-family ethical mediation and decision-use pattern
> **Status:** Stable
> **Pattern role:** Develop and compare ways to act when an ethical conflict has already been described; return a recommendation, conditional continuation, refusal or impasse.

**Use this when.** Use this pattern when an `InterlevelEthicalConflictDescription` from `D.3` must support mediation, refusal, a decision, an evidence demand, or a return to causal, assurance, or architecture work.

**Not this pattern when.** If the conflict has not yet been described, use `D.3`. If the issue is only value plurality, use `D.1`. If the issue is only entry recognition, use `D.2`. If the current work is bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance, use `D.5`.

**What goes wrong if missed.** Naming the conflict or filling in a decision record replaces the work of developing options and judging what each would require or change.

**What this buys.** The practitioner can compare available ways to act, recognize a useful change to the proposed means, and explain a recommendation or why the choice remains unresolved. Evidence, causal, assurance, architecture and bias-audit claims keep their own subject methods.

### D.4:1 - Problem Frame

Once an interlevel ethical conflict is visible, the next risk is premature closure. A team may declare a compromise before evidence is sufficient, turn an assurance input into ethical permission, use one level's value as a trump card, or hide a refusal behind technical language.

`D.4` guides one use of the conflict described by D.3. It does not make FPF a final moral authority. It asks what move is admissible from the current description and what must return to evidence, causality, assurance, architecture, decision, or value framing before action is justified.

### D.4:1.0 - Problem

A described ethical conflict can still be used badly. The failure is to treat its description, an assurance input, a formula, or an architecture return as if it already selected a compromise, refusal, evidence demand, accepted residual, or bounded decision use.

### D.4:1.1 - Forces

| Force | Tension |
| --- | --- |
| Described conflict vs. premature closure | A conflict description makes action discussable, but does not by itself decide compromise, refusal, or permission. |
| Evidence demand vs. decision pressure | Work may need a decision, while the ethical claim still needs stronger evidence, causal analysis, assurance, or architecture return. |
| Mediation vs. universal authority | D.4 can guide one bounded use of a described conflict, but cannot become a general decision theory. |
| Residual acceptance vs. hidden harm | Proceeding under residual harm can be admissible only when residuals, the admitted Systems involved, prospective plans or assignment requirements, direct responsibility relations or exact missing governors, and return conditions are explicit. When the account asserts performed work, identify that occurrence and its performer; add assignment attribution when that claim is made. |
| Mathematical allocation vs. ethical decision | A formula or optimization can inform a decision, but it is not the ethical decision by itself. |

### D.4:2 - Solution

Recover the conflict, develop feasible alternatives, compare their consequences and constraints under the stated value premises, and give a warranted recommendation or decision. Keep the concerns that remain unresolved visible in that result. A short answer can complete this work.

#### D.4:2.1 - Develop and compare a continuation

1. **Recover the decision and the affected concerns.** Use the D.3 account to identify who or what may gain or lose, over which horizon, and why those consequences matter. Check whether the proposed chooser can make the decision in question. Paying for a project, being represented in a survey, being affected by its result and having authority to decide are different relations. Return a consequential missing party to A.1.CSD; return an unresolved value premise to D.1.
2. **Separate the end from the proposed means.** A valued result can be pursued through means that create another objection. Ask which feature, condition or operation produces that objection and what could supply the valued result without it. B.5.QD.CF develops that question when an assumed necessary means creates the conflict; C.39 supplies construction of another way. Consider continuing the present work, narrowing the change, changing its conditions or refusing it when those are feasible alternatives. A proposed alternative remains a proposal until its required contributions are available.
3. **Compare the same alternatives under the live value premises.** Preserve each side's affected participants, consequences, constraints and uncertainty. An encompassing system's gain does not by itself establish priority over a constituent's loss. Where different value frames give different orderings, keep those orderings distinct. An alternative that is no worse under every retained ordering and better under at least one can remove a need to trade those values for this choice. This conclusion is limited to the alternatives, premises and affected concerns actually compared. If a trade-off remains, state the priority, compromise or other reason proposed for making it. Authority to choose does not make that reason correct or establish others' agreement.
4. **Resolve only the uncertainty that changes this use.** Separate disagreement about consequences from disagreement about which consequences or duties should govern. A causal inquiry can improve the former; it does not by itself settle the latter. Use available support and qualified uncertainty. Where an intended use requires a stronger claim, C.28 or the corresponding subject method supplies its basis; C.11.DUA compares an attainable inquiry with a narrower recommendation, a different option or a stop. Include delay, burden shifted to other parties and displaced work. Preserve a binding requirement's current force while examining its merits or a feasible revision.
5. **Return the supported recommendation or decision.** If the comparison basis and available options are settled, C.11 supplies the local choice. If the value conflict remains unresolved, give the conditional alternatives, the missing agreement or authority, or an explicit refusal or impasse. Do not manufacture a common scalar to force a winner. State a residual consequence and a reconsideration condition when they matter to this use. A recommendation does not establish consent, permission or performed work.

Use the same reasoning when the option is advice, publication, a technical change or a change to a method. Identify how its possible use can affect other participants; describing one's contribution as analysis leaves that question open. The relevant causal and responsibility relations still need their own basis.

#### D.4:2.2 - Retain the decision basis when the work needs it

Use an `EthicalMediationDecisionUse` account when another participant needs to inspect, compare, authorize or later revise the result. The necessary content can remain in the existing answer or decision record. The following form groups that content; use only the optional detail needed for this decision:

```text
EthicalMediationDecisionUse:
  conflictDescriptionRef: exact C.2.1 U.Episteme identified through D.3
  affectedEntityOfConcernRef
  affectedSystemRefs?
  valueFrameEditionRefs
  decisionQuestionRef?
  intendedDecisionUse?
  intendedWorkUse?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  optionRefs
  proposedMediationRefs?
  refusalOrStopCondition?
  evidenceDemandRefs?
  causalReturnRefs?
  assuranceReturnRefs?
  architectureResidualReturnRefs?
  acceptedResidualRefs?
  decisionRecordRefs?
  decisionOrRepairSystemRefs?: independently admitted U.System refs
  localSystemRoleKindRefs?: exact local U.Kind refs
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
  intendedWorkPlanOrCommitmentRefs?: prospective plan or commitment content
  intendedAssignmentRequirementRefs?: prospective requirement content; creates no assignment occurrence
  performedWorkRows?:
    - performerSystemRef: exact U.System
      workOccurrenceRef: exact dated U.Work
      assignmentSpeciesRef?: exact directly declared species under U.SystemRoleAssignment, when assignment-bound attribution is claimed
      assignmentOccurrenceRef?: obtaining occurrence of that species with actual participant values, applicability, and extent covering the Work
      f6AttributionRef?: exact performedUnderAssignment occurrence, for that attribution
      holderEquality?: performerSystemRef = assignmentOccurrenceRef.HolderSystemSlot, for that attribution
      methodRef:
      workExtentRef:
      containingSystemRef:
  responsibilityRelationRefs?: exact direct predicate, participants, applicability, and occurrence identity
  responsibilityMissingGovernorRefs?: exact A.6.RCD results
  authorityRelationRefs?: exact direct relation refs
  authorityMissingGovernorRefs?: exact A.6.RCD results
  permissionRelationRefs?: exact direct relation refs
  permissionMissingGovernorRefs?: exact A.6.RCD results
  commitmentRelationRefs?: exact direct relation refs
  commitmentMissingGovernorRefs?: exact A.6.RCD results
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

The record names the current ethical use of the conflict: mediate, refuse, continue under explicit residual, demand evidence, ask a causal question, ask for assurance, return to architecture, or make a bounded decision.

Name the affected EntityOfConcern and any affected Systems, the value-frame editions, the decision question and options, and the intended decision or Work use. Add ClaimScope and a qualification window when they delimit that use. State the proposed mediation or refusal and any accepted residuals. If evidence, causal adequacy, assurance, architecture residuals, responsibility, permission, or actual Work remains unresolved, return only that question to the pattern that defines it. These values delimit the mediation; a generic context field does not.

### D.4:3 - Mediation Moves

| Current situation | Admissible D.4 move | Neighboring subject pattern |
| --- | --- | --- |
| A compromise is proposed but the D.3 description omits a side, affected entity, scope, value frame, consequence, or horizon. | Return to `D.3` and complete the affected side or tension. | `D.3` |
| A causal claim can change the recommendation or decision. | Use its C.28 support and retain the uncertainty that changes this use. If stronger support is needed, use C.11.DUA to compare a feasible inquiry with a narrower use, another option or stopping. | `C.28`, `C.11.DUA` |
| Evidence is too weak or outdated for the proposed use. | Name the affected claim and use. Use `C.11.DUA` to compare a feasible evidence request with a narrower use, explicit residual acceptance or refusal; obtain stronger or fresher evidence when the selected use needs it. | `C.11.DUA`; `A.10` and `C.27` for the evidence and its currentness |
| Assurance claim is being used as ethical permission. | Keep assurance as an assurance or evidence relation, not moral authorization. | `B.3`, `D.5` |
| Architecture move reduces one residual but creates ethical conflict elsewhere. | Return the architecture residual and keep the ethical conflict distinct. | `C.30.ILC`, `D.3` |
| A decision must proceed with residual harm. | Record the accepted residual, admitted decision or repair Systems, prospective plan, commitment, permission, authority, or assignment requirements, direct responsibility relations or exact missing governors, evidence limits, and return condition. If Work has actually occurred, recover each precise performer's A.13 core and independently admit the Work under A.15.1; add F.6 only when the decision account also needs exact assignment-bound attribution. | `C.11`, `B.3`, `D.5`, A.2.1, A.13, A.15.1, and F.6 as applicable |

When the basis required for a particular claim cannot be obtained, that claim remains unsupported. A narrower recommendation or decision must satisfy its own evidence, ethical and authority conditions. Preserve an accepted residual where it changes the use; an inactive inquiry creates no separate omission account.

### D.4:4 - Archetypal Grounding (Worked Slices)

**Fair-share case.** A service outage plan can protect hospitals, households, or industrial customers, but not all at once. The `D.3` conflict description connects each affected scope and value concern to its consequence and horizon. `D.4` records the mediation use: options, accepted residuals, evidence demand, admitted decision Systems, prospective assignment requirements or commitments, direct decision-responsibility relations or exact missing governors, and return conditions. No assignment or Work is asserted merely because the plan names intended action. If the account reports execution, add the actual Work occurrence and its performer; add assignment-bound attribution when that further claim is made. A mathematical allocation Method may have a separate C.29 representation or lens-use assertion, but the allocation formula is not the ethical decision, assignment, or responsibility relation.

**Override case.** An assurance review says a release has the required technical assurance relation, but the `D.3` description shows unresolved harm for a subgroup. `D.4` does not let assurance override that conflict. It records whether release is refused, conditioned, delayed for evidence, handled under C.28 causal-use analysis, or allowed with an explicit residual and an independently obtaining responsibility relation or exact missing governor.

#### D.4:4.1 - Change the means, then reconsider when another constraint changes

A team wants colleagues to find an available specialist, while staff want private calendar details to remain private. The initially proposed means publishes every calendar detail to the whole organization. Turning the service off protects those details but loses the intended availability information.

The D.3 tension concerns staff information and the team's coordination, not two interchangeable scores. Recover the needed contribution: finding somebody available for a question requires neither an appointment title nor its other participants. Suppose an existing feature lets each member publish an availability window without exposing the underlying events; the team has permission and support to offer this voluntary feature. This supplies a third available option.

For this constructed decision, the participants' stated orderings are:

| Value concern and supplied judgement | First | Second | Third |
| --- | --- | --- | --- |
| Useful access to a willing specialist | Voluntary availability windows | Full calendar publication | Service off |
| Staff control of private event details | Voluntary availability windows | Service off | Full calendar publication |

Both orderings prefer the voluntary option to either original alternative. The team can recommend it on this basis without adding the ordinal ranks or deciding how much privacy one unit of access is worth. The judgement concerns these supplied preferences and feature conditions; it does not establish universal approval or a measured productivity gain. The technical feature, the permitted voluntary arrangement and each participant's choice are separate contributions to its use.

Now suppose the team instead needs guaranteed coverage of a required shift. Voluntary windows do not guarantee that contribution. The previous recommendation remains an answer to finding a willing specialist, but does not answer the changed staffing question. Return to the staffing arrangement and its affected commitments. A new assignment, another resource or a changed service promise may be needed; relabelling participation as voluntary cannot supply guaranteed coverage.

#### D.4:4.2 - Keep a useful decision when a stronger claim is unavailable

A comparison has two feasible options under an agreed value frame: retain the current arrangement or make a reversible change. The available basis bounds the change's net benefit between 2 and 4 units for every scenario retained in the comparison; all relevant constraints and affected concerns are already included in this stipulated example. The present question is which option is preferable under that basis, not what its precise effect will be.

The change is preferred throughout the supplied range. A study costing 5 of the same units solely to select between these options cannot improve their choice: its possible refinements within that range leave the selected option unchanged and impose that cost. C.11.DUA therefore supports the bounded recommendation without the study. The conclusion retains its conditional range and makes no precise-effect claim.

If a newly identified consequence can reverse that preference, or the intended use now needs a supported precise effect, the question changes. Examine that missing contribution and the feasible investigation that could supply it. The earlier decision does not authorize a stronger claim or ignore a newly affected party.

### D.4:5 - Boundaries

`D.4` does not define the conflict description, bias audit, ethical assurance, architecture residual, causal identification, evidence provenance, or decision theory in general. It defines one ethical use of a conflict already described by D.3.

Do not name a mediation move "calculus" unless a mathematical lens is selected and the lens is actually doing work. Do not name a mediation move "operator" unless the current pattern explicitly governs an operation. Most D.4 use concerns a practical recommendation or decision. A mathematical representation can support that comparison; its premises and result still need their ethical interpretation.

### D.4:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Conflict description becomes decision | A D.3 description is treated as if it already selected an action. | Name the D.4 move and its admissible use. |
| Assurance becomes permission | Technical assurance is read as ethical authorization. | Keep assurance as an assurance or evidence relation and record the ethical use separately. |
| Formula becomes ethics | Allocation, optimization, or scoring is treated as the ethical decision. | Use `C.29` for the mathematical lens; use D.4 to record the bounded ethical use without making the pattern an agent or responsible party. |
| Residual harm disappears | Action proceeds while residuals, admitted decision or repair Systems, and direct responsibility relations stay unnamed. | Name accepted residuals, prospective plans, commitments, permissions, authority and assignment requirements, the admitted direct responsibility predicates or exact missing governors, evidence limits, and return condition. Identify actual Work and its performer when performance is claimed; add assignment-bound attribution when that further claim is made. |

### D.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-D4-1 | The conflict and its sides are recoverable through D.3; add a stable conflict-description reference when the receiving use needs to cite or revise it. | Keeps the decision connected to the actual tension without requiring a separate record for a short answer. |
| CC-D4-2 | The recommendation or decision connects the affected concerns, value premises, feasible alternatives and comparison to its intended use. Retain differing orderings and residuals when they change the conclusion; add scope, qualification window and reference detail when that use needs them. | Makes the chosen continuation follow from its basis instead of merely listing decision fields. |
| CC-D4-3 | Evidence, causality, assurance, architecture, and decision claims use their subject patterns. | Prevents D.4 from becoming universal decision authority. |
| CC-D4-4 | When proceeding under residual harm, name accepted residuals and admitted Systems; keep any local kind, C.2.1 System-classification assertion episteme, prospective plan or assignment requirement, and actual relation distinct. Every responsibility, authority, permission, or commitment claim has its independently obtaining direct relation or exact A.6.RCD missing governor. Every actual Work row first recovers each precise performer's A.13 core and independently admits the Work under A.15.1; it adds F.6 only when precise assignment-bound attribution is also current. | Keeps bounded decision use reviewable without deriving responsibility or performance from an assignment or decision. |

### D.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Decision-ready by map | The mapped conflict is treated as solved. | Choose a D.4 move: mediate, refuse, demand evidence, return, decide with residual, or stop. |
| Trump-card level | One level's value automatically overrides all others. | Recover the affected sides through D.3 and compare their consequences and value premises through :2.1; a larger scale alone supplies no priority. |
| Unsupported stronger use | A decision or recommendation relies on a claim whose needed support is missing. | Qualify that claim and obtain the required basis for its use, or select a supported narrower continuation through C.11.DUA. An accepted residual does not make the missing claim true. |
| Permission by assurance | A passed assurance relation is treated as moral authorization. | Keep B.3 assurance and D.4 ethical use distinct. |

### D.4:7 - Consequences

This pattern makes ethical action reviewable without pretending that every conflict has a clean optimum. It preserves refusal, evidence demand, and residual acceptance as first-class outcomes. It also prevents architecture, assurance, or causal evidence from quietly becoming moral permission.

### D.4:9 - Rationale

`D.4` exists because an inspectable ethical conflict still needs a bounded use. Some uses stop work. Some demand evidence. Some return to causal, assurance, or architecture patterns. Some proceed under an accepted residual with named responsibility and return conditions. Without this pattern, teams either freeze because conflict exists or move too fast because the conflict was mapped once.

The pattern keeps refusal, evidence demand, and residual acceptance visible as ordinary outcomes. It also prevents formulas, assurance labels, architecture residual repairs, or causal claims from silently becoming moral authorization.

### D.4:10 - SoTA-Echoing

For **turning a value conflict into a different design**, **adapt** Value Sensitive Design's joint examination of technical and social arrangements. Against choosing only between the initial proposal and abandoning its aim, :2.1 and :4.1 follow the needed contribution to another means. The [VSD Lab's current account](https://vsdesign.org/vsd/) distinguishes designer and stakeholder values, direct and indirect stakeholders, and several levels of analysis. Miller, Friedman, Jancke and Gill's [*Value Tensions in Design*](https://www.cs.washington.edu/research/projects/aiweb/media/papers/tmp3oRDl8.pdf) (2007), §§6.1–6.2, supplies a concrete design comparison: useful usage information need not disclose who searched. Its local survey thresholds are not ethical constants or a voting rule for every project. The retained contribution is changing the means while keeping the affected values visible. Developing another design costs work; select it when it could improve the available choice. Reopen when the new arrangement fails a retained value or excludes an affected party.

For **reasoning with several value frames**, **adopt** the comparison problem made explicit by MacAskill, Bykvist and Ord in [*Moral Uncertainty*](https://academic.oup.com/book/31934/chapter/267645761) (2020), Chapter 3, Introduction and §I: ordinal orderings do not supply comparable numerical differences. Against adding arbitrary ranks, :2.1 preserves separate orderings and uses agreement where it suffices, as in :4.1. **Adapt** this limited contribution without making the book's Borda rule or expected-choiceworthiness proposal a universal FPF rule. C.11 already supports a partial ordering; D.4 keeps unresolved ethical aggregation visible rather than duplicating a decision calculus. Reopen when the present choice needs a trade-off or comparison across frames that the available basis cannot justify.

For **deciding how much investigation this mediation needs**, **adopt** C.11.DUA's comparison of attainable information work with its receiving contribution and full burden. Against either an automatic demand for causal certification or ignoring a missing basis, :2.1, :3 and :4.2 distinguish a supported bounded continuation from a stronger unsupported claim. C.28, A.10 and B.3 retain their own causal, evidence and assurance meanings; they do not supply moral permission. This comparison can end with required inquiry, a narrower result or refusal. Reopen when a changed consequence, intended claim, requirement or available inquiry can change that continuation. C.29 supplies a mathematical representation only when its operations improve the comparison; a calculated ranking remains conditional on its ethical premises.

### D.4:11 - Relations

- Builds on `D.3` for the exact conflict-description episteme used by this mediation or decision.
- Coordinates with `D.1` and `D.2` when value frame or multilevel entry is incomplete.
- Coordinates with `D.5` when bias, fairness, impact audit, causal-fairness audit consumption, or ethical assurance is current.
- Coordinates with `A.10`, `B.3`, `C.11`, `C.11.DUA`, `C.28`, `C.29`, and `C.30.ILC` when evidence, assurance, choice, inquiry value, causal, mathematical-lens, or architecture-residual questions are current.
- Uses `B.5.QD.CF` and `C.39` when a conflict over the proposed means calls for another construction; `A.1.CSD` supplies inquiry into a consequential missing party.

### D.4:End
