## PSDA.Application:3 - APP-PSD-03 — An on-time report that cannot yet be used



### PSDA.Application:3.1 - Recover the difficulty before naming a solution

A team sends its weekly report before the deadline, yet the planner must call colleagues to recover identifiers. Four of twenty distinct rows selected for diagnosis need clarification. The other sixteen are confirmed usable. Suppose the complete report contains forty distinct rows and there is no information about the remaining twenty. At least four and at most twenty-four rows need clarification. If the manager’s trigger is at least 10% of this report, it has been reached. At least 65% is impossible. Whether at least half need clarification is open. The unexamined rows matter to the last decision. To estimate the frequency in future reports, examine whether the selection, units and reporting conditions support the estimate.

With [FPF B.5.PI](../../sections/08-part-b---trans-disciplinary-reasoning-cluster/43-b-5-pi---initiate-inquiry-from-work.md), ask what prevents the planner from using the report under the agreed conditions. A complaint is evidence of what someone reports. A blank field is a property of a record. To establish an obstruction, connect the receiving work, the applicable requirement and what occurred. Use [FPF C.22.2](../../sections/09-part-c---kernel-extension-specifications/44-c-22-2---problemcard.md) to describe that problem and its outstanding factual or criterion premises.

In this constructed case the operations manager can authorize a temporary arrangement for the next planning cycle. The inquiry team can give advice. Separate authority would be needed to change another group’s deadline or commit its resources. Use [PSDA.11](27-psda-11---bound-the-decision-support-engagement-and-authorit.md) for the remit and [PSDA.12](28-psda-12---recover-participants-concerns-and-affected-systems.md) to include the planner, preparers and identifier suppliers. The planner needs usable identifiers in time, preparers need a clear rule, and upstream staff may not yet have the requested information.

Using [PSDA.1](18-psda-1---generate-plural-problem-formulations.md), the team identifies three formulations that would lead it to inspect different evidence.

| Formulation | What would make it the current difficulty? | First discriminating check |
| --- | --- | --- |
| The handoff omits available information. | Identifiers existed before submission but the receiving material lacks them. | Compare the source information with the material actually sent and received. |
| Sender and receiver use incompatible identifiers. | Both sides have values, but the receiver cannot map them to the intended work. | Follow one affected identifier through the agreed correspondence and actual processing. |
| The deadline precedes information availability. | The identifier is not knowable at the required time under the current arrangement. | Compare the time information becomes available with the receiving work's real need. |

A fourth possibility is a recording defect. The receiver may have had usable information while the register displayed an empty field. Use a qualified comparison of the material sent and received, or inspect the relevant material when that evidence is missing. Its contents may settle the question, and correcting the register may complete a repair. Attributing assignment delay to the reporting rule needs evidence about that effect. A CRM is one possible intervention once the difficulty is clear.

With [PSDA.2](19-psda-2---set-and-reopen-the-problem-boundary.md), the team bounds this inquiry to the next planning cycle and the burden of obtaining the needed information. If the deadline itself obstructs the work, establish its grounds and who can change it. Improving compliance with an unsuitable deadline may worsen the problem.



### PSDA.Application:3.2 - Construct alternatives only where their consequences matter

Suppose the recording check reveals an obstacle to actual use. The team asks whether restoring the earlier handoff rule would reduce delay. It uses [PSDA.3](20-psda-3---construct-complementary-situation-and-option-models.md) to retain the concern account and timeline for the questions they answer. Use an adequate causal model if available. Where the relevant relations remain unspecified, use [FPF C.28.CM](../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md) to construct and assess them.

Specify the outcome and horizon. Let X be the handoff rule used, M whether the planner had usable information in time, Y the delay in assigning the work, and Z the load in the same period. R records the register’s completeness entry. S records selection of a row for diagnosis. Evidence about R can stand for M only on a qualified relation between the register and what reached the planner.

One account proposes X→M→Y: the new rule changed the identifier correspondence, which obstructed use and delayed assignment. Load may also have prompted the rule change and delayed work, giving Z→X and Z→Y. The common cause does not erase the proposed mediated path. Under this model, a correctly applied correspondence repair can remove one source of delay while leaving the load-related delay.

A rival account has Z→M and Z→Y, with Z→X explaining why the rule changed at the same time. It omits X→M. Under those mechanisms, restoring the earlier rule leaves the load-related delay. Both mechanisms could operate together. Test the proposed relations against process knowledge and evidence. The shared timing of a template change and a delay leaves their causal relation open.

Restoring the rule could change M in the first model. In the second there is no such path. An affected identifier and the times at which its information was available can help distinguish them. A disagreement about presentation of known facts may need no causal model. If a necessary process fact is missing, establish it from a suitable source if feasible and warranted, or report how its absence limits the causal answer.

Selection also matters. If rows enter the investigation because their information is unusable or their assignment is delayed, both M and Y affect S. Restricting attention to S=1 can create dependence between M and Y even without a causal effect between them. Its direction and size do not follow from the three-node shape alone. Use the whole-path rules of C.28.CM for the chosen graph. Address this selection before using those rows to infer a relation across all handoffs.

Distinguish what may have started, sustained or amplified the difficulty. A change in correspondence could start it. A continuing stream of unresolved rows with nobody assigned to correct them could sustain it. Repeated assignment changes could amplify the rework. Each hypothesis has its own outcome and period. To represent delay feeding later load, use Y(t)→Z(t+1) and the relevant earlier influences. A directed acyclic graph requires this time structure to be free of directed cycles.



### PSDA.Application:3.3 - Match the proposed action and the evidence to the question

Turning a blank field green changes the recorded indication. Applying a corrected identifier correspondence changes the handoff. Using [FPF C.28.MR](../../sections/09-part-c---kernel-extension-specifications/56-c-28-mr---derive-an-intervention-consequence-by-mechanism-re.md), derive what each intervention implies under the specified mechanisms. Use [FPF C.28](../../sections/09-part-c---kernel-extension-specifications/54-c-28---causaluse-cal-causal-use-questions-identification-and.md) to examine the evidence connecting those mechanisms to this workplace.

A qualitative distinction may answer the question. For a quantitative causal effect, use [MMP.15](../foundational-thinking-dpf-suite/mmp/20-mmp-15---identify-an-intervention-effect-from-available-data.md) to determine what the model and available information identify. Choose adjustment, front-door, transport or another suitable argument according to its actual assumptions.

For an instrumental-variable argument, distinguish the assigned offer of help from the help used. With binary offer and use, the Wald ratio divides the difference in mean outcomes between offer groups by their difference in use rates. Give the grounds for relevance, exclusion and instrument exchangeability. With monotonicity and the applicable consistency and interference conditions, the ratio identifies the average effect among those whose use changes with the offer. That group need not include everyone who accepted, and its effect need not equal the effect of universal use. An invitation that teaches the work independently of use breaks exclusion. A small difference in use rates makes the ratio unstable. MMP.15:4.3.1 derives the local effect, :5.4 distinguishes offer, local-use and population effects, and Hernán and Robins give the assumptions in [*Causal Inference: What If*, Chapter 16, §§16.1–16.6](https://miguelhernan.org/whatifbook). Return the target effect, instrument, supported expression or remaining bounds and relevant uncertainty. If the identified effect differs from the requested one, state the difference and what further information or intervention could resolve it.

For an unresolved question that warrants research, use [RMP.1](../rmp/31-rmp-1-decide-whether-a-question-needs-research-and-when-to-s.md) to define it and the available basis. With [RMP.2](../rmp/32-rmp-2-choose-a-criticism-bearing-research-design-or-stop.md), compare a feasible study with answering on existing evidence or commissioning no study. A rule comparison must address differences in load, information availability, timing and selection that could defeat the inference. A proposal establishes the study design. To report its execution or findings, establish what work was done and what follows from the evidence, including suitable archival observations where applicable.



### PSDA.Application:3.4 - Give a usable answer while uncertainty remains

With [PSDA.5](22-psda-5---generate-decision-alternatives.md), consider options for the live problems, including repairing the correspondence, restoring the former rule, providing temporary clarification, changing the deadline within its authority, or keeping adequate current work. A rule repair may address a proposed cause. Temporary clarification can protect the planner’s work while that cause remains open.

Use [PSDA.6](23-psda-6---represent-values-and-trade-offs.md) to establish what timeliness serves and whose work the upstream calls consume. With [PSDA.7](24-psda-7---represent-decision-relevant-uncertainty-and-evidenc.md) and [FPF C.11.DUA](../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md), identify which uncertainty matters to the requested finding, its grounds or the choice at hand. Weigh the expected contribution of obtainable evidence against the full burden. A permanent rule change may require stronger evidence than a one-cycle workaround.

Suppose qualified staff have access, authority and enough time for one cycle of manual clarification. Operational evidence supports its ability to supply usable information. The manager can choose it for this cycle on its expected contribution, costs and limits while both causal models remain plausible. Agreement about the temporary response still leaves the original causal question open.

If clarification would impose an unacceptable burden on another group, or the identifiers cannot exist by the deadline, reconsider the temporary option or the deadline. With [PSDA.8](25-psda-8---compare-consequences-of-decision-alternatives.md) and [PSDA.9](26-psda-9---test-robustness-and-sensitivity-of-decision-alterna.md), distinguish an option that works across the retained accounts from one that depends on a particular mechanism. Report the supported comparison even when the permanent alternatives cannot yet be ordered.

Using [PSDA.14](30-psda-14---prepare-and-return-a-decision-support-recommendati.md), the team can recommend one justified cycle of temporary help, correction of any established recording defect and deferral of the permanent rule choice while the mechanism remains material and unresolved. The manager holds the applicable decision. To report execution, establish what the participants did.

With [EXD.4](../exd/12-exd-4---co-construct-and-repair-an-explanation-in-dialogue.md), explain why available information and the deadline matter and use the recipient’s response. A preparer’s statement that the identifier does not exist until Friday can change the formulation and recommendation when supported. If views still differ, return the disagreement, its grounds and its consequence.



### PSDA.Application:3.5 - Reconsider the affected claim after action

For the next cycle the manager assigns an observer with access to the sent material and processing history. The observer will report any recurrence before the following decision. Suppose the cycle is delayed again. Through [PSDA.15](31-psda-15---arrange-decision-follow-up-or-reassess-advice-afte.md), distinguish the recommendation, choice, work performed and measurements. Establish execution from suitable evidence of the work. To use a completion flag for that conclusion, check what event the flag records and how it relates to the claimed action.

If the question concerns a trial of a reusable method, use [FPF A.3.1.WT](../../sections/05-part-a---kernel-architecture-cluster/24-a-3-1-wt---design-and-interpret-a-method-work-trial.md) to connect the intended task with the work and conditions of the occurrence. That can answer what was done in this cycle. For a further question of fit or transfer, use [FPF A.3.1.FT](../../sections/05-part-a---kernel-architecture-cluster/26-a-3-1-ft---qualify-method-fit-and-transfer.md). For practical worth against feasible alternatives, use [FPF C.11.MV](../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md). Each stronger use needs the corresponding grounds.

The return depends on the supported distinction:

| What the follow-up establishes | What to reconsider |
| --- | --- |
| The record described a different event or value from the one needed. | Correct or replace the measurement and revise claims that relied on it. |
| Clarification was performed, but the proposed causal difference did not occur under the model's stated conditions. | Challenge that mechanism or its application; inspect live alternatives before strengthening the claim. |
| The action had its predicted effect but cost more or displaced more important work than the comparison allowed. | Reopen the value, burden or option comparison. |
| The chosen action was not performed, or its actual implementation changed the mechanism. | Address the execution or implementation question; the outcome does not test the unperformed action's effect. |
| The action and model conditions held, and one of the possible adverse outcomes occurred. | Update the evidence and any judgement that depends on it. One event under uncertainty need not invalidate the earlier decision. |

Several explanations can hold together. The evidence may also leave them unresolved. Revisit the particular record, model, comparison, work arrangement or formulation whose basis changed and return the supported finding or limit.

Operational work, temporary help and research can overlap. A causal graph represents proposed influences. A method combination identifies contributions that different activities need. A work history identifies the events that occurred and their order.



### PSDA.Application:3.6 - Make a usable aid for your own inquiry

For recurring work, start with what the recipient needs, such as usable input for next week’s planning. A ready account or short conversation can suffice. Consider building or revising an aid if repeated omissions or misunderstandings justify the work of preparing and maintaining it.

This construction adapts the problem-card and intervention exercises in Anatoly Levenchuk’s R4 guide. The filled cases illustrate how to build and revise an aid. Claims that a form improves decisions or that someone learned the method need evidence of the corresponding work and effect.

**Derive the questions from the intended use.** Identify the conclusion or action the recipient needs. Here the planner decides what can be assigned using the information that actually arrived, and what clarification or help to request. A green timeliness indicator can coexist with unusable information. The planner can request clarification or propose help. Under §3.4 the inquiry team recommends an arrangement, and the operations manager decides whether to allocate temporary help. Work backwards from errors that could change that result. Distinguishing the register from the received report takes the material and its source. Distinguishing inconvenience from breach of a requirement takes the receiving work and the applicable criterion. Separate observations from proposed explanations. [PSDA.1](18-psda-1---generate-plural-problem-formulations.md) helps construct the formulations and contrasts that matter.

A first problem aid for this use can have four sections:

| Section and instruction | Filled report example |
| --- | --- |
| **What receiving work is obstructed?** Identify the work, affected people, occasion and requirement. State the undesirable condition without naming a preferred remedy. | The planner cannot assign four reported items without clarification before this week's planning meeting. Sending by the deadline is insufficient: the agreed input must identify the work to be assigned. |
| **What supports that account?** Distinguish testimony, inspected material and conclusions. Identify the cases, their sources and any missing or contrary evidence. | In twenty rows selected for diagnosis, the planner requested clarification for four. The sent and received material is available for inspection. Whether the identifiers existed before submission remains unknown. The selection does not establish an organization-wide failure rate. |
| **What else could explain or change the difficulty?** Keep alternatives that affect the requested explanation, its grounds, the next inquiry or the response. Describe an observed obstruction even when its cause is open. | Available information may have been omitted, the identifiers may differ, or the information may have arrived too late. A recording defect remains possible until the receipt is checked. |
| **What would count as useful improvement, and what is needed next?** State the receiving result and constraints; name the next consequential question, not every unknown. | The planner can identify and assign the required work in time without unbounded clarification work elsewhere. Inspect one affected handoff's actual information and availability time before attributing the delay to the reporting rule. |

The evidence section qualifies what can be asserted. Alternative formulations guide inspection. An improvement criterion can later test whether a response helps. Requiring a “Root cause” before it is known invites a guess. Requiring “Proposed software” excludes viable responses. Keep the entry that serves the recipient and allow an unknown to remain open.

A participant’s reported dissatisfaction can itself be the difficulty under inquiry. Record the planner’s repeated frustration on the basis of that report. Whether delivery failed, why and what would remedy it remain separate questions to investigate if needed.

**When an intervention account is needed, build it from the problem.** Carry forward the formulation, receiving outcome and relevant conditions. Identify hypotheses as such. For each live candidate, describe what it would change, how that could help, what it depends on and what evidence could alter the conclusion. Include temporary help, adaptation or continuation when viable. Use [PSDA.5](22-psda-5---generate-decision-alternatives.md) to construct alternatives and C.28.CM and C.28.MR for a needed causal account and its consequences.

For this report, the intervention aid can distinguish the following responses.

| Candidate | Proposed change and expected contribution | Conditions and comparison that matter |
| --- | --- | --- |
| Apply a corrected identifier correspondence | Change the correspondence used in preparing and receiving the report. If a wrong correspondence is the operative obstacle, this supplies usable identifiers without repeated manual clarification. | Recover the actual correspondence defect, obtain authority to change both uses and check the material produced. Compare usability and processing delay for relevant cases; a successful example alone does not estimate a general causal effect. |
| Provide one cycle of manual clarification | A qualified provider obtains and conveys the required information for this cycle. The planner may use that result while the original cause remains open. | The information must exist in time and the provider needs access and sufficient time. To assess performance, establish what arrived, whether it was usable and what work was displaced. Review or stop under the applicable mandate if the budget or availability fails. |
| Change the timing or content of the commitment | Where information cannot exist by the current deadline, obtain an authorized agreement about later completion or a usable preliminary report. This changes the obligation rather than making unavailable information appear. | The receiving work must tolerate the changed commitment. Observe its actual delay and burden, not merely whether the revised due date makes the indicator green. |

Keeping the current arrangement remains an option when its consequences meet the applicable criteria. A combination needs its own feasibility assessment. Temporary clarification can accompany a correspondence repair if the helper’s available time covers the combined demand and the other relevant conditions hold.

When follow-up is needed, specify **what will be examined, by whom and for which use**. Before the planning decision, for example, the assigned observer can check the received identifiers, clarification time and assignment delay for the agreed cycle. Establish what work occurred under which conditions. A failure may concern measurement, implementation, mechanism or value. Use the preceding table to locate the affected conclusion. Before-and-after observations can describe change. Attribution to the intervention needs suitable causal grounds.

**Apply the aid to a constraint question.** Two promised Friday sessions require three and two hours of the same room. The exercise gives a four-hour window, no preparation time and no option to overlap or shorten the sessions. Since 3 + 2 > 4, the two commitments cannot be met as stated. That calculation answers the feasibility question.

For the feasibility finding, give the two commitments, the room and the available window. If the coordinator must make the sessions possible, examine which conditions can change. Moving the two-hour session to Saturday needs a suitable slot and the relevant agreements. A second room needs suitable access for two hours at an acceptable cost. Under the original Friday constraints, a preference score cannot create the missing room-hour.

For a chosen alternative, establish the booking and the session requirements it must preserve. The arithmetic already establishes the original incompatibility. Saturday attendance requires its own evidence. If the second room is unavailable, retain the Friday finding and reconsider alternatives when the task needs a remedy.

A general aid can ask **“What grounds establish or could change this account?”** It can then accept a constraint argument or causal hypothesis. A section about interventions can still ask what each change would supply. For an aid limited to report handoffs, keep the narrower terms and state that scope.

**Test the aid where its use remains uncertain.** Choose cases that distinguish the uses in scope, including an unresolved claim where that matters. Existing suitable tests can provide evidence. For a new test of independent reading, let an intended user read a filled account without first supplying a missing explanation. If the aid is commissioned for conducting an inquiry, give its intended user the available material and the aid, leaving the inquiry decisions to that person. If the commission is to select the next action, examine the choice and its grounds. For an inquiry carried to a conclusion, also follow how the user interprets the available or newly obtained evidence and gives the recipient a warranted answer, a revised conclusion or the remaining gap. A previous use that already shows the commissioned work under the needed conditions can suffice. Examine the difficulty, basis and warranted next result they recover. A request for the omitted availability time can expose missing content. An ambiguous use of “complete” may require a wording change. Disagreement with a criterion can be substantive. Repair the element that failed when a repair is needed.

Use [FPF C.41.TF](../../sections/09-part-c---kernel-extension-specifications/124-c-41-tf---construct-a-checklist-template-that-preserves-its.md) when the representation must preserve selected questions, answer meanings and references across views. Address a missing substantive question through the relevant practice. Preserve an adequate aid when a proposed revision adds work without improving the recipient’s use.

For a learning task, preserve an interpretable first attempt before giving a decisive cue. Offer feedback or another case when the learner’s work calls for it. To establish independent performance, examine the learner’s action and permitted support under the relevant conditions. [HCD.9](../human-capability-engineering-dpf-suite/hcd/26-hcd-9---perform-deliberate-practice-with-feedback.md) supports practice with feedback and [HCD.10](../human-capability-engineering-dpf-suite/hcd/27-hcd-10---choose-whether-and-how-to-vary-space-interleave-or.md) helps vary the practice. A useful aid, a justified intervention, evidence of learning and evidence of an intervention’s effectiveness can answer different requests.
