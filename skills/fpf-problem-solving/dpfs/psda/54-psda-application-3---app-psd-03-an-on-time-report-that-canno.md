## PSDA.Application:3 - APP-PSD-03 — An on-time report that cannot yet be used



### PSDA.Application:3.1 - Recover the difficulty before naming a solution

A team sends its weekly report before the agreed deadline. The timeliness indicator is green. The planner nevertheless spends time calling colleagues to recover identifiers before assigning the reported work. In twenty rows selected for diagnosis, four need clarification. These observations locate work that the indicator misses; they do not estimate the frequency of the difficulty across the organization.

[FPF B.5.PI](../../sections/08-part-b---trans-disciplinary-reasoning-cluster/42-b-5-pi---initiate-inquiry-from-work.md) helps notice this mismatch between formal completion and actual use. The question is whether something prevents the receiving work from proceeding under its applicable requirements. A complaint, a blank field and an adverse working condition are different objects. [FPF C.22.2](../../sections/09-part-c---kernel-extension-specifications/44-c-22-2---problemcard.md) can express the problem-side account while its factual and criterion premises remain visible.

For this constructed case, the operations manager may authorize a temporary reporting arrangement for the next planning cycle. The inquiry team may return advice; it cannot change another group's deadline or promise extra work on that group's behalf. [PSDA.11](27-psda-11---bound-the-decision-support-engagement-and-authorit.md) keeps that boundary. [PSDA.12](28-psda-12---recover-participants-concerns-and-affected-systems.md) brings in the planner, report preparers and the people who supply the identifiers. Their accounts can differ: the planner needs usable identifiers by planning time, preparers need an unambiguous rule, and upstream staff may not yet have the requested information.

Through [PSDA.1](18-psda-1---generate-plural-problem-formulations.md), retain three formulations with different consequences:

| Formulation | What would make it the current difficulty? | First discriminating check |
| --- | --- | --- |
| The handoff omits available information. | Identifiers existed before submission but the receiving material lacks them. | Compare the source information with the material actually sent and received. |
| Sender and receiver use incompatible identifiers. | Both sides have values, but the receiver cannot map them to the intended work. | Follow one affected identifier through the agreed correspondence and actual processing. |
| The deadline precedes information availability. | The identifier is not knowable at the required time under the current arrangement. | Compare the time information becomes available with the receiving work's real need. |

A fourth possibility is that only the recording is wrong: the receiver obtained usable information, but the register presents an empty field. Inspecting the actual sent and received material can settle that limited question. Correcting the register may then be enough; it does not establish an effect of a reporting rule on operational delay. “Install a CRM” is a proposed means, so it does not replace these formulations.

[PSDA.2](19-psda-2---set-and-reopen-the-problem-boundary.md) bounds this inquiry to information needed for the next planning cycle and the burdens of obtaining it. If the real difficulty is that the planning deadline itself has no useful justification, return to that requirement and its owner. Improving compliance with an unsuitable deadline can make the working situation worse.



### PSDA.Application:3.2 - Construct alternatives only where their consequences matter

Suppose the recording check leaves a real obstacle to using the information, and the team asks whether restoring the earlier handoff rule would reduce planning delay. [PSDA.3](20-psda-3---construct-complementary-situation-and-option-models.md) retains the concern account and the timeline for their own questions. Use an adequate existing causal model directly. When the causal relations are still missing, [FPF C.28.CM](../../sections/09-part-c---kernel-extension-specifications/55-c-28-cm---construct-and-challenge-a-causal-model.md) constructs the needed contribution.

Fix the outcome and horizon before comparing stories. Let X be the rule actually used for a handoff, M whether the receiving information is usable at planning time, Y the delay in assigning that work, and Z the load during the same period. R records what the register says about completeness; S records whether the row was selected for this investigation. Do not replace M with R merely because R is easier to obtain.

One account proposes X→M→Y: the new rule changed the identifier correspondence, which obstructed use and delayed assignment. Load may also have prompted the rule change and delayed work, giving Z→X and Z→Y. The common cause does not erase the proposed mediated path. Under this model, a correctly applied correspondence repair can remove one source of delay while leaving the load-related delay.

A rival account makes load the cause of both information arriving late and assignment delay: Z→M and Z→Y, with Z→X explaining why the rule changed at the same time. It omits X→M. Returning to the earlier rule then leaves those delays unless it changes another mechanism. These accounts may be combined if both mechanisms operate. Their arrows require process knowledge and evidence; the temporal coincidence of a template change and delay selects neither account.

The useful consequence is now explicit: restoring the rule can change M in the first account but does not do so in the second under their stated mechanisms. Trace an affected identifier and the availability times to challenge that difference. If the disagreement is only about how to present known facts, causal construction adds no result. If the necessary process fact is missing, return that fact request instead of completing a graph by intuition.

Selection also matters. If rows enter the investigation because their information is unusable or their assignment is delayed, both M and Y affect S. Restricting attention to S=1 can create dependence between M and Y even without a causal effect between them. Its direction and size do not follow from the three-node shape alone. Use the whole-path rules of C.28.CM for the chosen graph. Address this selection before using those rows to infer a relation across all handoffs.

Separate the start, persistence and amplification of the episode. A correspondence change may start it; a continuing stream of unresolved rows with no correction owner may sustain it; repeated assignment changes may amplify the rework. These are hypotheses about different outcomes and times, not three interchangeable names for one root cause. When delay feeds future load, represent Y(t)→Z(t+1) with the relevant earlier influences. Do not call an unqualified directed cycle a DAG.



### PSDA.Application:3.3 - Match the proposed action and the evidence to the question

Turning a blank field green changes an indication. Correcting and applying the identifier correspondence changes how information is handed over. [FPF C.28.MR](../../sections/09-part-c---kernel-extension-specifications/56-c-28-mr---derive-an-intervention-consequence-by-mechanism-re.md) can derive their different consequences once the mechanisms and intervention are specified. [FPF C.28](../../sections/09-part-c---kernel-extension-specifications/54-c-28---causaluse-cal-causal-use-questions-identification-and.md) separately asks what supports the resulting causal claim. A calculated consequence does not establish that the chosen mechanism describes this workplace.

A qualitative distinction may suffice. If the decision needs a quantitative causal effect, [MMP.15](../foundational-thinking-dpf-suite/mmp/20-mmp-15---identify-an-intervention-effect-from-available-data.md) asks whether the effect is identified under the model and available information. Its adjustment, front-door and transport examples develop different ways to obtain or limit an answer.

An externally assigned offer of help is not the same variable as help actually used. For an instrumental-variable argument, MMP.15:4.3.1 derives the binary local effect and :5.4 works through the difference between offer, local-use and population effects. Hernán and Robins, [*Causal Inference: What If*, Chapter 16, §§16.1–16.6](https://miguelhernan.org/whatifbook), provide a fuller discussion of the assumptions and limits. Return with the target effect, the proposed instrument, the grounds for its assumptions, the identifying expression or remaining bounds, and the uncertainty relevant to this decision. For a binary offer and binary use, the difference in mean outcomes between offer groups divided by the difference in use rates is the Wald ratio. Relevance, exclusion and instrument exchangeability are necessary for that argument; those conditions alone do not identify the population average effect. With monotonicity and the chapter's consistency and interference conditions, the ratio identifies the average effect among people whose use changes because of the offer. These people are not simply everyone who accepted help, and that local effect need not answer what universal use would achieve. An invitation that teaches the work independently of use breaks exclusion; a weak change in use makes the ratio unstable. If this conditional result does not answer the decision, return to the target, information or feasible intervention instead of relabelling it as a population effect.

If an unresolved question still warrants research, [RMP.1](../rmp/31-rmp-1-decide-whether-a-question-needs-research-and-when-to-s.md) frames the exact question and current basis. [RMP.2](../rmp/32-rmp-2-choose-a-criticism-bearing-research-design-or-stop.md) compares a useful, feasible design with using the evidence already available and selecting no new study. For a rule comparison, the design must address the load, information availability, timing and selection differences that could defeat its inference. A plan for such a comparison establishes no result of performing it.



### PSDA.Application:3.4 - Give a usable answer while uncertainty remains

[PSDA.5](22-psda-5---generate-decision-alternatives.md) keeps alternatives connected to the live formulations: repair the correspondence, restore the former rule, offer temporary clarification, change the deadline where authorized, or retain adequate current work. A rule repair addresses a proposed mechanism; temporary clarification may protect the receiving work while its cause remains unresolved. They are different claims of benefit.

[PSDA.6](23-psda-6---represent-values-and-trade-offs.md) keeps the value question visible: timeliness matters because of a receiving use, and the receiving group's convenience does not make unlimited upstream calls acceptable. [PSDA.7](24-psda-7---represent-decision-relevant-uncertainty-and-evidenc.md) and [FPF C.11.DUA](../../sections/09-part-c---kernel-extension-specifications/24-c-11-dua---make-advice-and-evidence-demands-worth-their-burd.md) ask which remaining uncertainty can change the current choice and whether obtaining the missing result warrants its burden. A disruptive permanent rule change may need evidence that a temporary workaround does not.

Suppose competent staff can perform one authorized cycle of manual clarification within a specified time budget, and current operational evidence supports its ability to make the required information usable. The manager may choose that bounded help while both causal accounts remain live. Its justification rests on the action's expected contribution, feasibility, costs and limits. Agreement among the models on this temporary action does not prove either model.

If the same arrangement transfers intolerable work to another group, or if usable information still cannot exist by the required time, the temporary option loses that basis. Reopen the comparison or deadline question. Through [PSDA.8](25-psda-8---compare-consequences-of-decision-alternatives.md) and [PSDA.9](26-psda-9---test-robustness-and-sensitivity-of-decision-alterna.md), distinguish a change that matters only under one causal account from an action that remains adequate across the retained accounts. Return a partial comparison when no current basis selects among the permanent alternatives.

[PSDA.14](30-psda-14---prepare-and-return-a-decision-support-recommendati.md) can now return: use the justified temporary help for this cycle; correct any established recording defect; keep the permanent rule choice open until the stated mechanism question is answered or the decision no longer needs it. This is conditional advice, not authority or evidence that the plan was executed.

[EXD.4](../exd/12-exd-4---co-construct-and-repair-an-explanation-in-dialogue.md) helps explain the decisive distinction and use the recipient's response. A preparer's objection, “that identifier does not exist until Friday,” can change the formulation, deadline premise and recommendation. Repeating the original explanation more clearly would not answer it. Agreement is unnecessary for a useful return that locates the disagreement and its consequence.



### PSDA.Application:3.5 - Reconsider the affected claim after action

For the next cycle, the manager names a person with access to the sent material and processing history to report any recurrence before the following planning decision. Suppose that cycle is again delayed. [PSDA.15](31-psda-15---arrange-decision-follow-up-or-reassess-advice-afte.md) first distinguishes what was recommended, what was chosen, what people actually did and what the observations measured. Do not infer non-execution from a bad outcome or execution from a green completion flag.

When the follow-up asks about a reusable working method, [FPF A.3.1.WT](../../sections/05-part-a---kernel-architecture-cluster/24-a-3-1-wt---design-and-interpret-a-method-work-trial.md) records the intended task and actual Work for the stated trial question. The resulting evidence can serve [FPF A.3.1.FT](../../sections/05-part-a---kernel-architecture-cluster/26-a-3-1-ft---qualify-method-fit-and-transfer.md) on fit or transfer and [FPF C.11.MV](../../sections/09-part-c---kernel-extension-specifications/25-c-11-mv---compare-the-worth-of-a-method-option.md) on practical worth against current alternatives. One successful cycle establishes none of those broader conclusions by itself.

The return depends on the supported distinction:

| What the follow-up establishes | What to reconsider |
| --- | --- |
| The record described a different event or value from the one needed. | Correct or replace the measurement and revise claims that relied on it. |
| Clarification was performed, but the proposed causal difference did not occur under the model's stated conditions. | Challenge that mechanism or its application; inspect live alternatives before strengthening the claim. |
| The action had its predicted effect but cost more or displaced more important work than the comparison allowed. | Reopen the value, burden or option comparison. |
| The chosen action was not performed, or its actual implementation changed the mechanism. | Address the execution or implementation question; the outcome does not test the unperformed action's effect. |
| The action and model conditions held, but an acknowledged uncertain outcome occurred. | Update the evidence and current choice without treating one adverse outcome as proof that every prior decision was wrong. |

Several explanations may hold together, or the evidence may not distinguish them. Return to the particular record, model, comparison, execution arrangement or formulation whose basis changed. “Poor discipline” cannot stand in for that discrimination, and success cannot certify the whole original theory.

Operational work, temporary assistance and research can overlap in time. The causal graph describes proposed influences. The combination of methods describes which contribution another activity needs. The work history describes what actually occurred and when.



### PSDA.Application:3.6 - Make a usable aid for your own inquiry

The report case supplies one connected application. To use the reasoning in recurring work, you may need an aid whose questions colleagues can interpret and answer. Start with a narrow receiving use, such as deciding how to make next week's planning input usable. A ready problem account or a short conversation can be sufficient. Make a reusable form only when repeated omissions or misunderstandings warrant its preparation and upkeep.

The following construction adapts the problem-card and intervention exercises in Anatoly Levenchuk's R4 guide to problem-structuring work. The filled cases are constructed teaching material. They show how to produce and change an aid; they do not establish that completing a form improves workplace decisions or that its reader has learned the method.

**Derive questions from the next use.** Write the action the recipient must be able to take after reading the account. For the planning team, this is to choose a justified next response without assuming that a green timeliness indicator means usable information. Work backwards from mistakes that would change that response. Confusing a register with the received report calls for the actual material and its source. Confusing inconvenience with breach of an agreed requirement calls for the receiving work and applicable criterion. Confusing an explanation with an observation calls for separate support and conjecture. [PSDA.1](18-psda-1---generate-plural-problem-formulations.md) supplies the formulation content and material contrasts; it does not require a separate form for every perspective.

A first problem aid for this use can have four sections:

| Section and instruction | Filled report example |
| --- | --- |
| **What receiving work is obstructed?** Identify the work, affected people, occasion and requirement. State the undesirable condition without naming a preferred remedy. | The planner cannot assign four reported items without clarification before this week's planning meeting. Sending by the deadline is insufficient: the agreed input must identify the work to be assigned. |
| **What supports that account?** Separate what someone said, what was inspected, and the conclusion. Identify the cases and source; keep missing or contrary information visible. | In twenty rows selected for diagnosis, the planner requested clarification for four. The sent and received material can be inspected. The selection gives no organization-wide failure rate. Whether the identifiers existed before submission is unresolved. |
| **What else could explain or change the difficulty?** Retain alternatives only where they change the next inquiry or response. Do not require a proved cause to describe an actual obstruction. | Available information may have been omitted, sender and receiver may use different identifiers, or the information may become available too late. A recording defect is also possible until actual receipt is checked. |
| **What would count as useful improvement, and what is needed next?** State the receiving result and constraints; name the next consequential question, not every unknown. | The planner can identify and assign the required work in time without unbounded clarification work elsewhere. Inspect one affected handoff's actual information and availability time before attributing the delay to the reporting rule. |

Each section has a consumer. Evidence limits what can be asserted; alternative formulations change what to inspect; the improvement condition later tests whether an option helps. A heading such as “Root cause” would force an early hypothesis into a settled answer. “Proposed software” would prematurely restrict the option set. Remove such requirements rather than asking users to fabricate entries.

An agent's dissatisfaction can itself be a real difficulty. It does not by itself establish a particular defect, cause or remedy. The aid can therefore retain “the planner reports repeated frustration” while the delivery claim remains unresolved. Preserve the source and support of each claim.

**Build the intervention account from the problem account.** Copy only the formulation, receiving result and conditions needed to compare responses. Do not copy a suspected cause into a field labelled “established mechanism.” For each candidate, explain what changes, how that change is expected to help, what it depends on and what observation could require revision. Include temporary help, adaptation or continuation when they are serious alternatives. [PSDA.5](22-psda-5---generate-decision-alternatives.md) supplies alternative generation; C.28.CM and C.28.MR supply a causal construction and its consequence when that question is live.

For the report case, the intervention aid can carry these genuinely different candidates:

| Candidate | Proposed change and expected contribution | Conditions and comparison that matter |
| --- | --- | --- |
| Apply a corrected identifier correspondence | Change the correspondence used in preparing and receiving the report. If a wrong correspondence is the operative obstacle, this supplies usable identifiers without repeated manual clarification. | Recover the actual correspondence defect, obtain authority to change both uses and check the material produced. Compare usability and processing delay for relevant cases; a successful example alone does not estimate a general causal effect. |
| Provide one cycle of manual clarification | A competent person obtains and conveys the required information for this cycle. This can protect planning while the explanation of the original failure remains open. | Information must exist in time; the helper needs access and a feasible time budget. Observe whether the planner can use the information and how much work is displaced. Stop or revise if the budget or required availability fails. |
| Change the timing or content of the commitment | Where information cannot exist by the current deadline, obtain an authorized agreement about later completion or a usable preliminary report. This changes the obligation rather than making unavailable information appear. | The receiving work must tolerate the changed commitment. Observe its actual delay and burden, not merely whether the revised due date makes the indicator green. |

Keeping current work remains an option when its present consequences are acceptable under the applicable criteria. It is not equivalent to leaving every question unanswered. A combination also needs its own explanation: temporary clarification may accompany a correspondence repair, but the helper's finite time cannot be promised independently to every measure.

Add a final section, **“What will be compared, by whom, and what follows?”** Bind observations to the intended result and the action actually performed. For example: before the next planning decision, the assigned observer checks the received identifiers, clarification time and assignment delay for the agreed cycle. The observer reports whether the chosen measure was performed and under which conditions. A failed receiving result can reopen measurement, implementation, mechanism or value; use the preceding return table to distinguish those claims. Comparing before and after is descriptive unless a suitable design supports causal attribution.

**Try the aid where a causal story is unnecessary.** A workshop coordinator has promised two sessions on Friday, needing three and two hours of the same room. The room is available for four hours. For this exercise, the sessions cannot overlap or be shortened, no preparation time is needed, and these durations and availability are given facts. The difficulty is not an unexplained fall in productivity: the simultaneous commitments cannot be met under these constraints, because 3 + 2 > 4.

The problem account now names both commitments, the shared room and Friday's window as its basis. “Why are people inefficient?” adds an unsupported cause. The useful next question is whether a commitment or a resource condition may change. One intervention moves the two-hour session to a separately available Saturday slot, subject to participants' and the commitment owner's agreement. Another obtains a second suitable room for those two hours, with the required access and cost acceptable to the responsible parties. Retaining both Friday commitments in the original room is infeasible under the stated premises; a preference score cannot repair that fact.

If either option is selected, the receiving check concerns the actual booking and the preserved session requirements. No new causal graph is needed to establish the arithmetic incompatibility. Whether participants will attend on Saturday is a different empirical premise, which the sum does not settle. If the second room is unavailable, retain the incompatibility result and reconsider the options; do not reinterpret an unconfirmed booking as capacity.

This case changes the aid's explanation section to **“What grounds establish or could change this account?”** It permits a constraint argument as well as causal hypotheses. The intervention section still asks what changes and why that supplies the receiving result. A form that requires a hidden root cause and an experiment for every difficulty would fail this use. For a form intended only for report handoffs, keep the narrower terms and state that boundary instead of expanding it into a universal questionnaire.

**Test the aid and correct the transition that fails.** Fill it with two or three actual or constructed cases within its intended scope, including an unresolved claim. Give a filled account to a colleague without supplying an oral explanation of facts absent from the aid. Ask them to explain the difficulty, the basis for the claims and the next justified move. Their request for an omitted availability time can reveal missing content; inability to interpret “complete” can reveal ambiguous wording; disagreement with an authorized criterion may instead expose a substantive conflict. Do not repair every objection by adding a field or by repeating the explanation.

[FPF C.41.TF](../../sections/09-part-c---kernel-extension-specifications/121-c-41-tf---construct-a-checklist-template-that-preserves-its.md) explains how selected questions, answer meanings and references survive a reusable form and its views. Use it when representation is the difficulty. Return a missing or unsuitable question to its substantive owner. Retain an adequate existing aid when the new version adds burden without changing what the recipient can do.

If learning is the purpose, save the first attempt, explain the correction and try a changed case before claiming independent performance. [HCD.9](../human-capability-engineering-dpf-suite/hcd/26-hcd-9---perform-deliberate-practice-with-feedback.md) supplies practice with feedback; [HCD.10](../human-capability-engineering-dpf-suite/hcd/27-hcd-10---choose-whether-and-how-to-vary-space-interleave-or.md) helps vary the missing operation. A completed template, an intelligible description, a justified intervention and demonstrated capability are different results. This construction can finish with a useful aid and a precise unresolved question without establishing the effectiveness of an intervention or a person's later unaided performance.
