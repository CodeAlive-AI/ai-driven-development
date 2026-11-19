## B.5.MR - Compare Models by Refinement and Abstraction

> **Type:** Method pattern
> **Status:** Stable

### B.5.MR:1 - Problem frame

**Use this when** you need a model to determine something left open by another model, or need an abstraction that leaves some determinations open while retaining a useful conclusion. The practical question is which answers remain admissible and which conclusions can still be used. Two specifications of a design, two accounts of a method or two editions of the rules for constructing a model can each raise that question.

A useful first result identifies the inquiry, the assertions preserved and the answers admitted by each model. A strict refinement excludes an earlier admissible answer. A strict abstraction admits an answer excluded before, so a conclusion that depended on that exclusion needs reconsideration. When deciding between theories that answer different questions, B.5.TC helps identify a comparable use. When the change is in the actual system, examine the changed system directly.

### B.5.MR:2 - Problem

More detail can narrow a choice, leave the answer unchanged, or contradict an earlier commitment. Omitting detail can leave the same assertions recoverable or lose a premise the reader needs. A change of wording, a new unit or a newly chosen discipline may also change what the reader takes the question to mean. How can the reader construct and compare models while establishing what each change permits them to infer?

### B.5.MR:3 - Forces

A practitioner needs a comparison in ordinary terms. A consequential claim of preservation must cover all remaining possibilities. Model editions can use different representations. An apparent exclusion can arise from dropping a difficult case, changing the meaning of a quantity or switching from a design condition to a report of actual performance. An abstraction can serve a wider inquiry while losing a conclusion needed for a particular decision.

### B.5.MR:4 - Solution

Begin with one question that both models answer. Which designs, executions or other alternatives does each model admit? To refine a model, choose something it leaves open. Show that at least one alternative remains and that every remaining alternative satisfies the earlier assertions under the chosen interpretation. To abstract a model, decide what to leave open and apply the same test with the starting model on the concrete side. The answers tell you whether the difference is strict and which conclusions still hold.

#### B.5.MR:4.1 - Recover the assertions and the answers left open

Identify the modeled entity or the range of candidate applications left open, the inquiry, and the conditions under which each answer will be read. Keep the force of the claims explicit when it matters. Permitted values, predicted values and observed values answer different questions. For a claim-bearing model recover its content, EntityOfConcern and effective interpretation under C.2.1. For a physical model establish which observations on it warrant which inference about the target. PHY.1 in Physical Thinking gives the similarity conditions for transferring a selected observable across changes of scale or operating conditions.

Recover what the model asserts about the participants: which quantities may vary, which relationships must hold, which designs qualify or which performances a Method permits. The relevant subject Method supplies their types and grounds. A stated condition may be an assertion of the model or an assumption under which it applies; distinguish these when they change the answer. If the expression leaves its assertion unrecoverable, use F.19 before treating it as a model at a higher abstraction level.

A **completion** is one way of settling what the model leaves open for this inquiry while satisfying its assertions. A candidate design, a possible behavior or a structure satisfying stated axioms can serve as a completion. The inquiry determines what answer can be read from it. Several different designs can give the same answer. A completion need not have been observed, built or authorized for use. Include probability claims when the inquiry concerns likelihood. Two models can allow the same outcomes and assign them different probabilities.

#### B.5.MR:4.2 - Test preservation and strictness

Identify the completions each model admits. Call the proposed refined model C and the model whose assertions it must preserve A. When their languages or detail differ, explain how every completion of C is read in the terms used for A's answer, and why that reading serves the inquiry. Test that a completion of C exists and that each completion of C, so read, satisfies A's assertions. When these tests hold, **C refines A**, and **A is an abstraction of C**, for this inquiry and interpretation. The two names give converse directions of the same comparison.

This relation includes equivalent answers. To establish **strict refinement**, also identify an answer admitted by A that no completion of C can produce. Only with this strict difference call C **more concrete** than A and A **more abstract** than C. Show a surviving completion of C so that exclusion cannot be attributed to inconsistent assertions.

If a model admits no completion, examine which assertions make it infeasible. If both models admit none, neither supplies a feasible answer. When each admits at least one completion, equal sets of observable answers establish agreement for this inquiry. If each admits an answer the other excludes, the models are incomparable by refinement. They may still share answers. If they share none, their assertions conflict under the common reading. When feasibility or the correspondence is unknown, identify what would settle it.

Within a chain of models that pass the feasibility and preservation tests under a common interpretation, models that admit the same answers share a level for this inquiry. On different branches, models can give the same answer and impose incompatible constraints. Test preservation separately for the pair in question. A different inquiry can distinguish models the first one treated alike. Before composing comparisons across languages, establish how their interpretations compose.

A claim of greater accuracy needs a reference and an error criterion. A bound can establish accuracy against a mathematical reference. For a claim about accuracy on an actual system, use observations under the relevant conditions. Refinement alone supplies neither empirical accuracy nor evidence of actual performance.

##### B.5.MR:4.2.1 - Refine a model for a further decision

Identify what the next decision needs determined: a value, a construction choice, a permitted performance or another answer left open. Obtain the subject grounds for that determination. Add or bind the corresponding assertion and compare the resulting model with the starting model by section 4.2. Explain the preserved assertions, show a surviving completion and identify any excluded answer.

An added assertion can repeat what already follows. For that inquiry the two models then admit the same answers. If the new model admits a previously excluded answer or contradicts an earlier assertion, identify what changed and reconsider the claim of refinement.

##### B.5.MR:4.2.2 - Construct or select an abstraction

Identify the conclusion the receiving work still needs and the determinations on which it depends. Decide which other determinations may be left open. Construct a model that leaves them open, or select an existing model that does so.

Compare the starting model as C with the proposed abstraction as A under section 4.2: C must have a completion, and every completion of C must satisfy A under the established interpretation. Then check the needed conclusion over the answers A admits. Identify any prior conclusion that no longer follows and the determination on which it depended; report when no conclusion is lost for the inquiry. If the needed conclusion is lost, retain that determination or choose a different abstraction.

Several abstractions can serve different inquiries about the same starting model; several concrete models can refine one abstraction. The comparison supplies no unique inverse construction. Leaving a variable open also does not prove that a result observed at one value holds at every newly admitted value. Wider empirical or methodological claims need their subject grounds. Retaining the same assertions in clearer wording is clarification of their expression; it does not change this model order.

#### B.5.MR:4.3 - Read the levels of model abstraction and refinement

Read **L0 → L4 as levels of model abstraction** and **L4 → L0 as levels of model refinement**. Both names describe one order. A more concrete model preserves the earlier assertions and rules out an answer the more abstract model allowed. Abstracting a model or refining a model is the work of constructing or selecting the model on the chosen side of that comparison. In a chain of applications the five names below identify what each model specifies.

| Level, from more abstract towards more concrete models | What the model specifies |
| --- | --- |
| L4, foundational | A formal or computational construction and the choices its own conditions permit. |
| L3, transdisciplinary | A principle interpreted across eligible disciplines. Bind it to the construction wherever that interpretation is warranted. |
| L2, disciplinary | A subject discipline and the professional method, constraints or interpretation used there. |
| L1, local | Conditions shared by a particular setting or recurrent local population. |
| L0, individual | The identity of the particular entity or occurrence being modeled. Its unobserved characteristics can remain open. |

**Use the levels when deciding what a result establishes.** State the decision and what the model for that decision must specify. Identify the model actually available. An L0 model that identifies a delivery can contain its planned arrival. To decide whether that delivery met its deadline, compare the verified actual arrival with the deadline in force. To decide whether a scheduling rule at L2 guarantees all its deadlines, examine why the rule covers every permitted schedule. One admissible schedule that misses a deadline defeats the claim that every permitted schedule meets its deadline. For a target of 95 percent of actual deliveries on time, assess the eligible deliveries in the specified population and period. Count a late arrival when it occurred there. A calculation using the rule can check its consequences while leaving open who designed it. Carry the result to the decision through the grounds for that particular inference in C.39.QR:4.2–4.3. Accept the conclusion those grounds support and identify what would settle the outstanding claim.

Check each pair for one inquiry under §4.2. Establish which earlier assertions every remaining design or permitted performance satisfies. Show that at least one remains. If the step is strict, name an answer that can no longer be obtained. The same test applies to two models of one design or method, including when both are disciplinary models.

If a site adopts a disciplinary rule with the same interpretation and adds no constraint on the action in question, write “the site uses the L2 rule unchanged.” The L1 practice model records the site's adoption of the rule for recurring work. If asked at what level the rule specifies the permitted action, keep L2. Claim a further level of refinement for that action only when the local model excludes a previously permitted answer. Several strict refinements can occur within one named level. If a rule permits a check at either site, specifying the first site excludes the second answer to “Where may this check take place?” If both sites have to be checked, dropping one abandons an obligation.

A disciplinary model can prescribe a method, a local model can specify how it may be used at one site, and an individual model can describe a particular performance. Evidence that the work occurred and followed the rule must come from that performance. Two models of a system can also stand in strict refinement at the same physical scale. Moving to a constituent invokes the constructive relation under B.1.

Core, DPFs and LPFs supply models that can participate in such comparisons. A publication or discipline does not itself have one abstraction level. Binding a parameter can refine a model without changing its language; changing professional vocabulary can preserve all its admitted answers. A richer representation language can also express a model applicable to more situations. Compare the interpreted assertions for the inquiry.

#### B.5.MR:4.4 - Compare models of models by the same test

A metamodel states conditions on admissible models, such as which field or relation can occur and how it is interpreted. Conformance asks whether a particular model satisfies those conditions. Refinement **of a metamodel** compares two such sets of conditions for the same inquiry about admissible models. A model can conform to both editions. A model conforming to a metamodel and that metamodel conforming to higher-order construction rules gives two separate conformance judgements. C.37.MM helps keep their participants and governing editions recoverable when the models are passed on.

### B.5.MR:5 - Archetypal Grounding

A project commissions a temperature recorder for one installation. The earlier specification permits records at whole-minute intervals of one or two minutes. The new specification permits only one-minute intervals and preserves the units, clock and operating conditions. A one-minute record is still eligible. A two-minute record is excluded. For the inquiry about permitted sampling intervals, this is strict refinement. If the recipient asks only whether every hour contains a reading, both specifications give the same answer. Whether the installed recorder met its specification last night requires observations of that recorder.

Suppose a receiving comparison needs to know whether each recorder specification ensures at least one reading in every hour, without deciding between one-minute and two-minute intervals. Reuse the earlier specification as an abstraction of the one-minute specification. Every completion of the latter still satisfies the former, and both permit a completion. The abstract specification retains the hourly conclusion over all its permitted intervals. It no longer entails that the interval is one minute. For an inquiry that distinguishes the intervals this is strict abstraction; for the hourly inquiry the answers remain equivalent.

A work method screens requests under a criterion and then refers unresolved ones for a second judgement. A local revision adds a deadline to the referral while preserving the screening rule. A referral after the deadline was admissible under the earlier timing rule and now falls outside the local prescription. A second revision silently accepts some requests previously requiring referral. Compare that changed decision with the original rule before relying on it. An excellent record of one compliant case cannot settle the claim for the newly admitted cases.

To compare the local method with methods at other sites for their screening and referral duties, return to the prescription without the local deadline. It is an abstraction if every performance permitted by the local prescription satisfies it and at least one such performance is possible. The referral duty remains; the local deadline no longer follows. Removing that deadline from the model does not withdraw an actual site's deadline or establish that its workers performed the referral. Those are different assertions needing their own grounds.

### B.5.MR:6 - Bias-Annotation

A vivid individual case can conceal what the earlier assertion covered. Start with the intended inquiry and an admissible alternative. Looking only for a stricter result can hide agreement, a real conflict or uncertainty. Looking only for a simpler abstraction can conceal the loss of a conclusion the next decision needs.

### B.5.MR:7 - Conformance Checklist

- The inquiry, participants, force, assertions and common reading are recoverable.
- A refinement claim has at least one admissible completion of C and covers every completion of C for the inquiry. An abstraction claim uses the converse comparison.
- Call a model more concrete or more abstract only if the comparison exhibits a distinguishable answer that is admitted on the abstract side and excluded on the concrete side. Report when the models give the same answers for the inquiry or are incomparable under refinement.
- The receiving conclusion has been checked over the answers the selected model admits. Any reported loss identifies the conclusion and its missing premise; absence of loss remains a possible result.
- Claims of conformance, parthood, occurrence or empirical accuracy use the grounds for their own relations.

### B.5.MR:8 - Common Anti-Patterns and How to Avoid Them

A longer document may repeat the same assertions in a more useful form. Test which answers have changed. A project can also specify an individual that does not exist. If no candidate survives an attempted binding, reopen the identification.

A model abstracted from one successful performance can admit other performances whose success has not been established. Use the subject Method to justify the wider claim before relying on it. A simpler drawing or a shorter paragraph can preserve the same model; compare its assertions before assigning a different abstraction level.

### B.5.MR:9 - Consequences

A receiving practitioner can reuse preserved assertions, determine an open choice, or reopen a choice without losing track of the conclusions that depend on it. The comparison locates the premise to revisit when a model, correspondence or inquiry changes. A teacher can ask a learner to construct each direction and explain the retained and lost conclusions on an unfamiliar application.

### B.5.MR:10 - Architectural Rationale

One comparison serves many kinds of modeled entity because it concerns the assertions a model makes for an inquiry. Its converse supplies abstraction while leaving the construction of a suitable model to the receiving need and subject grounds. Kind-specific composition, physical similarity and performed work retain their own tests. This division lets the same model answer questions at different scales without assigning its file or language a single level.

### B.5.MR:11 - SoTA-Echoing

Specification theory compares models that satisfy stated sentences. It supports comparison across signatures when an interpretation specifies how a later model yields an earlier one. Under ordinary set inclusion, an empty class is included in every class. If the task is to show that a specification is infeasible, emptiness can settle it. A practitioner relying on a refined model to select a feasible design or action also needs a surviving completion. Section 4.2 therefore tests existence and preservation and asks which earlier possibility is lost when strictness matters. If the receiving inquiry changes what counts as the same answer, reconsider the interpretation and the comparison under it. This is a historical formal basis for the comparison. [Sannella and Tarlecki, *Specifications in an Arbitrary Institution*, §§2 and 8](https://homepages.inf.ed.ac.uk/dts/pub/inst-asl.pdf)

Probabilistic program development also uses refinement and abstraction as converse directions while retaining probability-sensitive guarantees. A comparison of outcome sets alone loses that information; section 4.1 therefore keeps the probability claims relevant to the inquiry. The formal construction is a historical anchor, not a claim that every Method is a probabilistic program. [Morgan, *The Generalised Substitution Language extended to probabilistic programs*, §2](https://cgi.cse.unsw.edu.au/~carrollm/probs/Papers/Morgan-98.pdf)

### B.5.MR:12 - Relations

Use B.5.TC for comparisons of theoretical accounts, C.2.1 for the identity and grounding of epistemes, C.29 for a mathematical representation and its correspondence, B.1 for reasoning across holonic scales, and C.37.MM for coordinating and handing on models. E.10.D2 governs the use of a description as a specification. F.19 helps recover assertions from their expression. F.17:12.6 and F.18:4.5 give the names for both directions and their ordered levels.

### B.5.MR:End
