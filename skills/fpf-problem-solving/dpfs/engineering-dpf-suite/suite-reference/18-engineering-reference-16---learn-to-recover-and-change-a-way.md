## Engineering.Reference:16 - Learn to recover and change a way of working

Use this practice when you know your own work and want to learn how to explain, compare and change its method. You will work from short records, propose a way for another team to work, and revise it when a condition changes. You need to be able to read the records and do simple arithmetic; a calculator is welcome. The workshop and editorial records below are constructed practice material. All the facts needed for the exercises are supplied here.

For each attempt, read the situation and task, save your answer, then read the discussion and correct the answer in your own words. The discussion supplies reasons for self-checking. Individual feedback requires a qualified helper and agreed time; the section [Arrange useful feedback](18-engineering-reference-16---learn-to-recover-and-change-a-way.md#engineeringreference166---arrange-useful-feedback) explains what that contribution involves. You can make and compare your first attempt on your own.

If a transition remains difficult, work through its explanation and correction before adding another difficulty. You may stop with a useful partial answer and a specific question. There is no requirement to finish every exercise in one sitting. If you have already seen a solution, use it as a worked example; a claim that you can reconstruct a method independently needs an attempt on other suitable material. Keep any help visible when interpreting the result of an attempt.


### Engineering.Reference:16.1 - Start with what happened

You want another team to work as reliably as an experienced workshop employee who prepares kits. The employee has not yet explained the method. You have two records:

- In the first episode, three identical parts were in a common storage area. The employee moved two to a tray, marked it for order A, then confirmed A's kit. When order B requested two parts, the employee pointed to the one part outside the tray and did not confirm B.
- In the second episode, four parts were available. The employee prepared and confirmed two kits of two parts in succession, marking each tray with its order.

The records show the handling of parts and the confirmations. They omit any other conversations and private notes; other handovers of parts and cancellations were not observed. The workshop's rule forbids promising the same part to two orders.

**Try it before reading the discussion.** Explain a possible way of working to a colleague. Distinguish what the records directly support from your explanation of it. What other account could explain the same actions? Identify an unknown that could change how another team should work. Decide which claim needs a further answer and what useful, limited result you can already provide. Use the supplied records rather than filling their gaps with assumptions about warehouses.

**Discuss your answer.** Moving parts, marking trays, confirming A and declining B are recorded. The records do not show when the employee treats a part as promised. One possible account is that placing a part in a marked tray creates that commitment. Another is that the employee first keeps a private tally of commitments and the tray displays an earlier decision. Both fit the visible actions. Saying that the employee always reserves stock in a computer system would add an unobserved tool, action and repeated practice.

Keep an alternative when it fits the material and changes a later decision. Here the difference matters: the new team can see trays, but cannot see an unknown private commitment. A useful question is, "At what point does a part become unavailable to another order, including before its tray is ready?" The employee's answer would be an account to compare with the observations where the receiving decision needs that distinction.

You can finish this recovery with two candidate accounts, each stating a possible repeatable way of working and the limits of its support. You can design a future rule while the choice between these explanations of the earlier work remains unresolved. Claiming to have established that employee's actual repeatable method may need more evidence. A question that could distinguish the accounts does not by itself justify an investigation: compare the benefit and full cost of obtaining the answer with using the limited result already available.

**Correct your answer.** If you treated one account as established, find the sentence that adds an unobserved fact and restate it as a possible explanation. If you only listed events, add a possible repeatable rule and show which events support it. If you stopped all further work pending an interview, distinguish explaining the old practice from proposing a future one. Explain what your colleague can use now and which claim remains unresolved.


### Engineering.Reference:16.2 - Build a rule for the receiving team

Two new dispatchers now look independently at the common stock. With three parts available, each sees enough for an order of two. The team needs assignments backed by available parts, without promising any part twice. For this exercise, A has priority over B. The process owner permits comparison of possible arrangements; introduction into actual work would need its own decision.

A stock clerk can keep a quantity record. Whether that clerk can cover every channel through which parts are promised and handle the required workload remains to be established. No capability of an automatic stock system is given.

**Try it before reading the discussion.** Propose an executable rule. What must a dispatcher obtain before confirming an order, and who produces that result by which action? Show what happens to B. Compare a meaningful alternative, or explain why another alternative would not change this choice. State the support and authority your proposal depends on. Distinguish what you recovered from the earlier records from what you designed for the new conditions.

**Discuss your answer.** A dispatcher needs a confirmation that the kit is committed to that dispatcher's order. Checking the total again does not create this result: two correct checks that 2 ≤ 3 can still lead to promises of four parts. Something must change before the next competing promise. One possible rule is to check the free quantity and reserve the requested quantity for the order in one operation that another reservation cannot interrupt.

Run that proposal forward. A reserves two of the three free parts, leaving one. The returned confirmation names A. B needs two, so B receives a waiting outcome or an authorized change to its requirement, rather than a second confirmation. Reservation must change a record or physical arrangement that everyone promising those parts actually uses. Without that effective change, the proposal only names a desired result.

One clerk processing requests in succession can supply the required operation if all promises pass through that clerk and the resulting wait is acceptable. An automatic operation with the same property is another possibility, if it can be obtained and supported. Allocating separate stocks to the dispatchers can also prevent competing promises, but two independent allocations cannot each contain two parts when only three exist. Later changes in demand can require an authorized reallocation. Compare these alternatives by the same required result, including their waiting time, workload, access and maintenance.

This is a design for new work. It uses the observations without claiming that the employee previously used this exact rule. Its application still depends on the stated capabilities, authority and coverage.

**Correct your answer.** If you proposed checking more carefully, keep the valid arithmetic and add the action that changes what can be promised next. If you proposed a tool, identify the operation that prevents another promise from intervening, or name that missing capability. A different arrangement can be suitable if it preserves the required result and its support is available. Rewrite your instruction so that a colleague can follow both requests and explain why B waits.


### Engineering.Reference:16.3 - Change a condition that matters

Keep your instruction from the previous attempt. First predict what it does under each changed condition; then read the corresponding discussion.

**Cancellation task.** A is cancelled after two parts have been reserved but before they are issued. The cancellation message arrives twice. In a separate episode, cancellation arrives after the parts have been issued. What changes in your rule? What stays valid, and what must happen beyond changing the order record?

**Discuss cancellation.** Cancelling an active, unissued reservation must release its quantity once and change the order's state. After the first cancellation, three parts are free; after the duplicate, three are still free. Releasing the quantity again would invent stock. If the parts have already been issued, cancelling the order record cannot return them: an actual return and a record of it are needed before those parts become free again.

The count explains the distinction. With no receipts or losses, free parts plus reserved parts plus issued parts equal the original three. Reservation moves a quantity from free to reserved; issue moves it to issued; cancellation before issue moves it back to free. A duplicate cancellation has no active reservation left to release. Help with addition can be useful while leaving you the task of deciding which state permits the action.

**Another channel task.** Another employee starts promising parts directly to customers without using the common record. A different manager assigns that employee's work. Which condition of your proposal has failed? Which earlier results remain usable? Propose a change and state whose decision and contribution it needs.

**Discuss the other channel.** Coverage of all promises has failed. Recalculating the sum or asking the first clerk to work faster cannot restore it. You can propose that the new channel also uses the common reservation operation, or allocate genuinely independent stocks with rules for reallocation. Those who control the affected work must decide and provide for the arrangement. Until then, a promise of coverage for all channels is unsupported. The earlier calculation for a covered channel remains valid under its conditions.

**Correct your revision.** Name the changed condition, the action that relied on it and the result the next person can now obtain. If you rewrote everything, recover an independent result that can be retained. If you changed nothing, show how the proposal prevents the competing promise. If you only wrote "coordinate with the other manager", state the decision needed: compulsory use of the common record, authority to change the work, a separate stock, or a narrower promise of coverage.


### Engineering.Reference:16.4 - Try the reasoning on editorial work

Read this material and make an attempt before opening the discussion below. You can do this yourself; a helper is optional. If you have solved a similar problem before, use the exercise as practice without treating it as an unfamiliar task.

An editorial team publishes short analytical notes. You have three versions of one passage. The money unit is arbitrary.

| Version | Number of kits | Price per kit | Written total | Change |
| --- | --- | --- | --- | --- |
| V1, arithmetic checked | 3 | 10 | 30 | Original version |
| V2 | 3 | 10 | 30 | Only the font changed; all other words in the passage are unchanged |
| V3 before the editor's correction | 3 | 12 | 30 | The price changed; all other words in the passage are unchanged |

In the first recorded episode, the editor compares V2 with V1 and reuses the arithmetic check. In the second, the editor recalculates V3, corrects the total and retains a new check. No other conversations or actions are recorded.

The following editorial rule is given for this exercise: a check concerns specified claims, a question and conditions; a prior result may be reused while those remain applicable. Ordinary comparison and calculation tools are available. A new team must choose how to put that rule into practice.

**Try it before reading the discussion.** Explain a possible earlier method and propose a way for the new team to work. Retain alternatives where the records do not distinguish them. Follow your proposal through V2 and V3, explaining why the returned result is usable and where its grounds are insufficient. Then change the proposal: the team is now asked to establish the truth of the original observations, not just the arithmetic consistency of the passage. The sources of those observations are absent from the material.

**Discuss your answer.** No shortage of check results is given. Reusing one result for two suitable versions does not consume it. Reserving that result for only one version would copy a warehouse operation into a different problem. The reasoning to reuse is about what the next action needs, which conditions support it and what a changed condition invalidates.

The recorded comparison supports an account in which the editor checks whether relevant content remains unchanged. It does not establish that this comparison was the only basis for the decision; an unrecorded authorization or earlier check might also have contributed. For the new team, you can explicitly propose comparing the claims, question and conditions before relying on an earlier result. That is a proposal for obtaining grounds for reuse, with its own support conditions.

For V2, the supplied unchanged claims and arithmetic question permit reuse of the sufficient earlier check. For V3, 3 multiplied by 12 is 36. Correct 30 to 36 and check the uses of the new value. The arithmetic result for V1 and the matching V2 remains valid. The new version does not make the former calculation false.

The question about the truth of the observations needs evidence about those observations. More arithmetic cannot supply it. You can return the established arithmetic result and the exact missing contribution, while limiting what you claim. Both unconditional reuse for the new question and rejection of all prior results would lose this distinction.

**Correct your answer.** If you required a complete recheck, identify the claim or condition that makes each repeated operation necessary. If you allowed reuse just because a change was called cosmetic, show the comparison that establishes what actually changed. Preserve the supported arithmetic and identify the evidence needed for the new question. Explain your correction before trying another available version. The editorial rule was supplied here: using it does not establish that you discovered it independently.


### Engineering.Reference:16.5 - Return to work you know

Choose one difficulty in familiar work and use records you can legitimately access. Use several occurrences if your purpose is to recover a repeatable method; one episode can support a hypothesis. You can make this learning attempt without changing the live work or obtaining confidential material.

State the result the next person needs. Separate recorded facts from possible explanations and your proposal. Compare a serious alternative, then follow your proposal through a concrete piece of the available material. Change one condition that could defeat it. State what result remains valid, what needs revision and which missing fact or contribution limits your answer. If the current way is already sufficient, explain why you would keep it.

Use a connected account, a calculation or a small table to make your reasoning inspectable. Explain an important choice to a colleague: why this action supplies the next result, what would make it fail, and how the proposed revision responds. Finish with a useful proposal or a specific limitation. Where the subject grounds are disputed, obtain the relevant professional judgement; these exercises cannot supply missing knowledge of your field.

After discussing or rereading your answer, make the correction yourself. Preserve the first attempt so that you can distinguish what you did unaided from what the discussion supplied. Choose the next task around the operation that still needs practice, rather than repeating a whole exercise by default.


### Engineering.Reference:16.6 - Arrange useful feedback

For self-checking, compare your reasoning with the explained answers above. For individual feedback, a helper examines your attempt and responds to the transition you made: how you selected facts, explained the practice, compared alternatives or changed a proposal. Memorizing the stock rule or matching the author's phrasing is a different result.

For guided practice, agree what the helper will examine and when the feedback will be available before your next attempt. The helper needs to distinguish a possible account of past work from a new proposal, recognize unsupported subject assumptions and give a correction you can act on. Before relying on the help, ask the proposed helper to respond to contrasting learner attempts. Check whether the feedback preserves valid reasoning, identifies the unsupported step and gives the learner a useful correction to make; obtain qualified judgement if you cannot assess this yourself. [HCD.7](../../human-capability-engineering-dpf-suite/hcd/24-hcd-7---arrange-providers-access-tools-and-ai-support-for-hu.md) guides obtaining the contribution; [HCD.8](../../human-capability-engineering-dpf-suite/hcd/25-hcd-8---obtain-or-build-missing-human-capability-development.md) addresses preparing one when it is missing.

If you provide that help, save the learner's reasoning before correcting it. The following are examples of responses to particular difficulties, not a diagnosis of every learner:

| Difficulty in an attempt | Useful contribution from the helper | The learner's own correction |
| --- | --- | --- |
| Wrong sum with the relevant stock state correctly identified | Locate the arithmetic error or offer a calculator while leaving the state question visible | Recalculate and explain whether the decision changes |
| An unobserved action is treated as established | Ask for its support in the record; explain the difference between a record and a candidate explanation using that claim | Qualify the claim and retain a meaningful alternative |
| A new proposal is attributed to the earlier employee | Ask which parts come from observation and which respond to new conditions | Explain the proposal's origin and limits |
| The answer names an outcome such as agreement without an action that produces it | Ask what the next person must obtain and which action changes the relevant state | Construct that transition and follow it through the data |
| Warehouse reservation is copied into editorial checking | Show which subject conditions differ and ask what the next editorial action needs | Construct a way of qualifying reuse of a check |
| A coherent proposal lacks time, access or authority | Retain the proposal and identify the missing support | Narrow the promise, choose an available alternative or return the precise question to the person who can decide it |

Where several explanations of an error remain plausible, ask the learner to explain the reasoning before attributing a recurring difficulty. After a full demonstration, repeating that answer does not show independent recovery; choose other suitable material for that question. A correct answer reached with help remains a result obtained with that help.

An AI assistant can retrieve a source, show a calculation or suggest feedback from the permitted material. If you are learning to make a methodological choice, make and explain that choice yourself. Arrange competent examination of consequential subject assumptions and the proposed feedback. Preparing a request, checking the answer and correcting an assistant's error all take work.

If the helper becomes unavailable, you can retain self-study and a saved attempt on the supplied material. Individual feedback and assessment still need provision. If your present work only needs an expert's answer and you do not need to develop the ability yourself, obtaining that answer can be sufficient.

[HCD.9](../../human-capability-engineering-dpf-suite/hcd/26-hcd-9---perform-deliberate-practice-with-feedback.md) guides practice with feedback and correction; [HCD.10](../../human-capability-engineering-dpf-suite/hcd/27-hcd-10---choose-whether-and-how-to-vary-space-interleave-or.md) helps choose variations for the missing operation. The duplicate cancellation changes an action condition, the additional channel changes coverage, and the editorial case changes the subject. [HCD.12](../../human-capability-engineering-dpf-suite/hcd/29-hcd-12-test-transfer-to-unfamiliar-work-or-learning-from-a-n.md) distinguishes learning with a new source from applying an already demonstrated ability under changed conditions. Use the actual task and assistance when judging what an attempt shows.


### Engineering.Reference:16.7 - Sources and further practice

Anatoly Levenchuk's *Guide to Methodology for Engineers and Managers* (Russian: «Руководство по методологии для инженеров-менеджеров», R7) explains how to make methods explicit, examine one's own work, and introduce methods through explanation and practice. If you have access to the guide, its explanations and project exercises offer further practice. The tasks above are complete without it. An equivalent exercise and workable help already available to you may be a better use of your time.

FPF A.3.1.MR explains recovery of candidate methods; C.39 supplies construction and change for a receiving use. [FPF A.3.2.DE](../../../sections/05-part-a---kernel-architecture-cluster/30-a-3-2-de---describe-a-method-for-its-intended-use.md) helps make an account usable for its intended action. When a proposal is to enter real work, [FPF A.3.1.MI](../../../sections/05-part-a---kernel-architecture-cluster/28-a-3-1-mi---introduce-a-method-into-practice-and-decide-what.md) addresses introduction and what to keep or change. The exercises supply practice with these contributions; successful use in your work needs its own grounds.
