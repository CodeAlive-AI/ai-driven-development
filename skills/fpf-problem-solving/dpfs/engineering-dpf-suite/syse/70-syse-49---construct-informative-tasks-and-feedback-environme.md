## SYSE.49 - Construct Informative Tasks and Feedback Environments for Agent Work

> **Type:** Method pattern
> **Status:** Stable

### SYSE.49:1 - Problem frame

**Use this when** you need to establish whether available interaction experience answers an agent-development or comparison question, or to obtain experience that is missing. Relevant failures may be rare, expensive to reproduce or hidden by misleading feedback. A controller or tool constructor can need this experience while model parameters stay fixed.

The subject is the task and interaction arrangement that supplies informative experience to the named construction or comparison. Its realization may be human practice material with an available feedback provider, or a software fixture with executable state and observations. The first result is that usable arrangement with qualified feedback and limits, or the missing condition. For human practice, use an applicable exercise design from HCD.6, or develop the missing design there. Prepare the material, interaction and feedback the learner needs.

Use an adequate existing environment. Use a small fixture when it supplies the evidence needed for the distinction. Learner construction and final assessment are separate consumers; neither is required to justify a useful fixture for a controller repair.

### SYSE.49:2 - Problem

A realistic-looking transcript can omit the state transition that matters. Generated tasks and judges can share a wrong premise and certify each other. Rewarding every action encourages unnecessary calls; rewarding fluent reports can hide missing effects. More varied tasks are not more informative unless their differences bear on the receiving question.

### SYSE.49:3 - Forces

Real interaction offers relevant effects but can be costly or difficult to reset. Synthetic conditions permit controlled variation while risking false transfer. Automatic generation expands coverage but can create impossible tasks and easy shortcuts. Tight feedback can discriminate progress or distort the behavior being developed.

### SYSE.49:4 - Solution

#### SYSE.49:4.1 - Select the failure boundary and result meaning

Name the receiving construction or comparison: for example, distinguish an unapplied operation from an applied operation whose reply was lost. Recover the consequence that makes that distinction matter, any evidence of failure and the experience that could distinguish the candidate responses.

Obtain the task's success, restraint and protected-effect predicates from the relevant domain or interface contract. State which observations can establish them and which remain unavailable. If a necessary acceptance criterion is missing, identify what must be established by a qualified supplier before using the affected judgement.

Distinguish the task, its working environment and the feedback it produces. Qualify the experience for its intended use separately from any resulting change to the agent or its support. For software fixtures, SYSE.33 supplies reproducible conditions and reset. A human branch obtains HCD.6's practice design and HCD.7's actually available support, then prepares the selected material, interaction and feedback conditions. SYSE.47, SYSE.48 or SYSE.45 consumes qualified experience for its own distinct result. For SYSE.50, construct qualified help/no-help decisions with the performer's actual input, feasible assistance and independently grounded outcomes; another performer's tool use alone does not label necessity for this one.

#### SYSE.49:4.2 - Construct feasible tasks and consequential variation

Start with a feasible task that exposes the boundary. Vary inputs or conditions that could change the correct continuation: target, starting state, available evidence, timing, applicable edition or actual effect. Keep the task instruction consistent with the provided material, implemented state and permitted operations. For human practice, use the design from HCD.6 for any demonstration, first attempt, correction or changed-condition task the learning question needs. An answer-bearing cue changes what the attempt can show.

Include progress and restraint cases where they can distinguish responses that matter to the receiving question. An already satisfied target may require no mutation; an impossible transition may require stopping that action; delayed evidence may require waiting or an unresolved return. Give credit for a call when it contributes to the task under these conditions.

Broaden variation where an incidental constant, wording or order could account for a successful response. Choose difficulty from the receiving question. For an empirical estimate of transfer, keep the final evaluation cases and their expected results, including consequential near-duplicates, outside adaptation. A structural argument or exhaustive check can separately establish a property across its qualified range.

#### SYSE.49:4.3 - Implement observable state, actions and reset

Prepare the material, actions and observations needed for the selected distinction. For a human task, make the relevant work and response visible. When assessing a contribution the learner is to supply, withhold that contribution while providing the assistance allowed for the task. For a software fixture, implement the needed state, permitted actions and effects. Make hidden fixture state available to an authorized evaluator when it is needed to judge consequences, without leaking it into the agent's task.

Use SYSE.33 to initialize and reset isolated software instances, preserving task identity, starting state and trajectory. An old effect or cached answer can invalidate the comparison. For people, prepare fresh material and record prior exposure, help and fatigue; replacing a worksheet does not reset the person's experience.

Distinguish imagined observations, outputs predicted by a model, and state actually obtained by executing the fixture. An observed run establishes what happened in the fixture. A claim about the receiving service needs grounds that connect the fixture to that service. When simulated dynamics supply a relied-on approximation, qualify the model and consequential error through MMP.17/SYSE.10.

#### SYSE.49:4.4 - Construct feedback that can defeat the generator

Derive checks from the supplied result predicates. Prefer direct state or effect checks where they establish the claim. Use a judgment model only for a contribution that needs it, with an explicit basis and disagreement return. A favorable narrative cannot overrule an observed failure of a required condition.

Test whether the feedback rejects misleading acknowledgements, forbidden duplicate effects or needless mutations. On a task that cannot succeed, check whether it recognizes warranted restraint. Choose the challenge from the actual contract.

Challenge shared generator/verifier errors using an independently grounded check or reader. Independently generated prose from the same mistaken premise is insufficient. Executable code that runs without errors establishes runtime consistency, not the validity of its success rule.

#### SYSE.49:4.5 - Qualify use and supply the consuming construction

Compare the constructed interaction with its receiving-use basis. For human material, check that the supplied HCD.6 target action, help and actionable feedback can actually occur. For a fixture, compare its behavior with the real interface or qualified source model. Record which distinctions transfer and which remain synthetic assumptions. A missing real recovery operation can defeat that branch's usefulness without erasing a valid normal-result test.

Provide the consumer with tasks, starting conditions, trajectories, feedback basis and their limits. A fixed-model controller can use these traces to revise its transitions; a tool constructor can use them to construct a wrapper; parameter training is optional. Establish any claimed change through its implementation and relevant observations.

Return misleading feedback to its construction, provision/reset faults to SYSE.33, missing result meaning to the domain owner, and failed transfer to the relevant model or environment assumption. SYSE.46 supplies a separate final comparison before broader configuration reliance. Stop when the selected distinction has informative, qualified experience or an unresolved gap.

### SYSE.49:5 - Archetypal Grounding


#### SYSE.49:5.1 - Make a missed carry observable in human practice


The receiving engineering question is whether a proposed worksheet and sequence make carry recording and use recoverable. HCD.6 supplies a practice design for a person already able to perform the digit products: produce a correct stock total with intermediate working, first with an allowed demonstration, then correct the affected action if the intermediate working or reported result is wrong. The arithmetic criteria are supplied. The engineer prepares the worksheet, task cards, independent answer basis and an available observer who can give the designed feedback.

Use 123 × 3 = 369 as a no-carry contrast and 127 × 3 = 381 as a carry case. The latter requires recording the 2 from 7 × 3 = 21 into the tens column and using it in 2 × 3 + 2 = 8. Capture the written relation and performed operation: an absent carry record, a recorded 2 ignored during calculation, and correct working copied into a wrong report are different observations.

If the person records 2 but writes tens 6, feedback preserves the correct units/hundreds, points to the unused carry and asks for correction of that operation. The corrected result is 381. This can be supported correction on the same case. For a judgement about independent recognition, use suitable work in which the person had to recognize and use the carry before receiving a cue. An earlier independent attempt can supply that evidence. Obtain a new one when the earlier work does not cover the required use. A partially worked demonstration must not be counted as that independent recognition.

Challenge the feedback itself: an answer key that approves 361 despite the visible unused carry fails the supplied arithmetic criterion. A sheet whose carry row is misplaced returns to SYSE.48/SYSE.52; a missed use despite a correct supplied layout returns to the procedure or the human learning diagnosis. The qualified material and observations can inform that repair. For a claim of learning, transfer or retention, use the corresponding observations of the learner’s performance through HCD.11–HCD.13.


#### SYSE.49:5.2 - Distinguish an absent effect from an absent reply


An agent sometimes repeats a configuration change after a lost reply. Reproducing the failure on the real service is costly. The interface owner supplies four predicates: the requested target reaches the requested version; one attempt has at most one state-changing effect; an acknowledgement without the effect is not completion; unresolved effect does not authorize blind replay.

The engineer constructs a fixture with target/version, attempt identity and effect count. Its operations can apply an effect, suppress the reply after application, acknowledge without applying, and return delayed state observations. Clean initialization and exercised reset come from SYSE.33.

Paired tasks vary target, initial version and reply/effect condition. Additional cases begin already complete or request an unsupported transition. A contract-derived check reads actual fixture state and effect count; it distinguishes completion, warranted restraint and unresolved effect.

To challenge shared error, deliberately make both a task generator and its generated verifier equate acknowledgement with success. An acknowledgement-only response leaves the target unchanged, so the independent state check defeats that premise. A second challenge repeats the effect: the final version looks right, but effect count exposes the forbidden duplicate.

Qualified traces return to SYSE.47 to construct the missing-effect/unknown-effect branch while the model stays fixed. A recovery wrapper under SYSE.48 or a trained policy under SYSE.45 would be a separate optional result. For evidence of performance beyond those construction cases, use independent final comparison tasks under SYSE.46.

If the real service lacks the fixture's attempt lookup, the useful-recovery claim remains unqualified. Retain valid normal-result exercises and return the mismatch to the interface/environment owner. This constructed example specifies the fixture and observations to obtain.

### SYSE.49:6 - Bias-Annotation

A generator can favor tasks it can solve or verify. A judge can favor familiar language, action frequency or confident completion. Preserve contract-derived restraint cases and a challenge that can falsify the generator's premise.

### SYSE.49:7 - Conformance Checklist

- The task variations distinguish outcomes that matter to the question the experience is meant to answer.
- Result and protected-effect meanings have qualified suppliers.
- The task admits the response to be assessed under the stated information, resources and permissions. Recognizing an infeasible request can itself be the required result.
- State, observations, reset and feedback remain distinguishable.
- Independent challenges can expose shared generator/verifier mistakes.
- Synthetic execution and real-world evidence retain their different provenance.
- The relation to the receiving work supports the claimed transfer. Estimates of performance on new tasks use evidence independent of adaptation and appropriate to that task population.

### SYSE.49:8 - Common Anti-Patterns and How to Avoid Them

**Generate tasks until there are many.** Add a variation only when it can reveal a consequential distinction or shortcut.

**Let the same generated rubric define and certify success.** Challenge it against independently supplied result meaning and actual state.

**Treat a working simulator as a faithful world.** Qualify the transitions and observations that the receiving claim needs.

### SYSE.49:9 - Consequences

Rare or costly failures can become reproducible experience for a bounded construction. Environment and feedback maintenance become new obligations. A useful fixture can support a local repair while leaving deployment reliability unresolved.

### SYSE.49:10 - Architectural Rationale

A qualified task and feedback arrangement can be constructed and used independently of changes to the agent. It may inform a change to a procedure or tool, or a decision about training. Separating task generation, provision, feedback and qualification prevents executable consistency from becoming semantic assurance. A separate final assessment tests whether the result extends beyond the cases used for adaptation.

### SYSE.49:11 - SoTA-Echoing

For the software realization, [Agent World Model v1](https://arxiv.org/html/2602.10090v1) supplies a direct construction option: generated tasks drive database-backed environments, callable operations and state-based verification signals. Correction by execution can find faults that prevent a run. Check the task’s intended meaning independently. Feedback that favors taking action can penalize warranted restraint, so test it on a case where stopping is correct.

Retain that separation and add independently grounded result challenges for the receiving use. A manually constructed fixture can suffice when it answers the question at lower total cost. Reopen qualification when result predicates, real interface behavior, simulated transitions or the consuming claim changes.

### SYSE.49:12 - Relations

Use HCD.6 for human practice design and HCD.7 to arrange the required support; HCD.11–HCD.13 address human performance, transfer and retention conclusions. SYSE.33 provisions and resets software conditions; MMP.17/SYSE.10 qualify selected simulated responses and reliance. SYSE.47, SYSE.48 and SYSE.45 consume experience for controller, operator and policy changes. SYSE.50 consumes qualified assistance-decision examples. SYSE.51 consumes trajectories where a consequential intermediate observation changes the useful allocation, including easy stops and unaffordable or uninformative continuations. SYSE.46 supplies final configuration assessment. CMP.7 retains learner construction; RMP.3 supplies a criticism-bearing research design when a research design is needed for the receiving question.

### SYSE.49:End
