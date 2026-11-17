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

A model states something about a system, method or another modeled entity, and can leave several answers open. First say which inquiry is being answered and recover the assertions that govern those answers. Refining a model determines something it leaves open while preserving what it already establishes. Abstracting a model leaves determinations open while retaining what the receiving inquiry needs. Compare the admitted answers to establish either relation.

#### B.5.MR:4.1 - Recover the assertions and the answers left open

Identify the modeled entity or the range of candidate applications left open, the inquiry, and the conditions under which each answer will be read. Keep the force of the claims explicit when it matters. Permitted values, predicted values and observed values answer different questions. For a claim-bearing model recover its content, EntityOfConcern and effective interpretation under C.2.1. For a physical model establish which observations on it warrant which inference about the target. PHY.1 in Physical Thinking gives the similarity conditions for transferring a selected observable across changes of scale or operating conditions.

Recover what the model asserts about the participants: which quantities may vary, which relationships must hold, which designs qualify or which performances a Method permits. The relevant subject Method supplies their types and grounds. A stated condition may be an assertion of the model or an assumption under which it applies; distinguish these when they change the answer. If the expression leaves its assertion unrecoverable, use F.19 before treating it as a model at a higher abstraction level.

A **completion** settles what the model leaves open for this inquiry while satisfying its assertions. It can be a candidate design satisfying specified relationships, a behavior compatible with observations, or a structure satisfying stated axioms. An admitted completion need not have been observed, built or authorized for use. A list of observed instances therefore need not exhaust the completions. Choose what the inquiry can distinguish. When likelihoods matter, include the probability claims being compared. Two models can allow the same outcomes and assign them different probabilities.

#### B.5.MR:4.2 - Test preservation and strictness

Identify the completions each model admits. Call the proposed refined model C and the model whose assertions it must preserve A. When their languages or detail differ, explain how every completion of C is read in the terms used for A's answer, and why that reading serves the inquiry. Test that a completion of C exists and that each completion of C, so read, satisfies A's assertions. When these tests hold, **C refines A**, and **A is an abstraction of C**, for this inquiry and interpretation. The two names give converse directions of the same comparison.

This relation includes equivalent answers. To establish **strict refinement**, also identify an answer admitted by A that no completion of C can produce. Only with this strict difference call C **more concrete** than A and A **more abstract** than C. Show a surviving completion of C so that exclusion cannot be attributed to inconsistent assertions.

If a model admits no completion, examine which assertions make it infeasible. If both models admit none, neither supplies a feasible answer. When each admits at least one completion, equal sets of observable answers establish agreement for this inquiry. If each admits an answer the other excludes, the models are incomparable by refinement. They may still share answers. If they share none, their assertions conflict under the common reading. When feasibility or the correspondence is unknown, identify what would settle it.

Under a fixed common reading, the admitted answers order comparable models, with equivalent answers sharing a position. An inquiry that distinguishes additional features can give a different comparison. Before composing comparisons across languages, establish how their interpretations compose. The names do not impose a single ranking on all models.

A claim of greater accuracy needs a reference and an error criterion. A bound can establish accuracy against a mathematical reference. For a claim about accuracy on an actual system, use observations under the relevant conditions. Refinement alone supplies neither empirical accuracy nor evidence of actual performance.

##### B.5.MR:4.2.1 - Refine a model for a further decision

Identify what the next decision needs determined: a value, a construction choice, a permitted performance or another answer left open. Obtain the subject grounds for that determination. Add or bind the corresponding assertion and compare the resulting model with the starting model by section 4.2. Explain the preserved assertions, show a surviving completion and identify any excluded answer.

An added assertion can merely repeat what already follows; then it does not establish a more concrete position for the inquiry. If the resulting model admits a formerly excluded answer or the added assertion contradicts the starting model, report the changed assertion or conflict and reconsider the model. Greater length or a local label does not settle this comparison.

##### B.5.MR:4.2.2 - Construct or select an abstraction

Identify the conclusion the receiving work still needs and the determinations on which it depends. Decide which other determinations may be left open. Construct a model that leaves them open, or select an existing model that does so.

Compare the starting model as C with the proposed abstraction as A under section 4.2: C must have a completion, and every completion of C must satisfy A under the established interpretation. Then check the needed conclusion over the answers A admits. Identify any prior conclusion that no longer follows and the determination on which it depended; report when no conclusion is lost for the inquiry. If the needed conclusion is lost, retain that determination or choose a different abstraction.

Several abstractions can serve different inquiries about the same starting model; several concrete models can refine one abstraction. The comparison supplies no unique inverse construction. Leaving a variable open also does not prove that a result observed at one value holds at every newly admitted value. Wider empirical or methodological claims need their subject grounds. Retaining the same assertions in clearer wording is clarification of their expression; it does not change this model order.

#### B.5.MR:4.3 - Locate levels of model abstraction in an application chain

A **level of model abstraction** is a relative position under the comparison in section 4.2. When the inquiry concerns which applications are eligible, a chain may leave open or determine the interpretation of a formal construction, the discipline, the local conditions and the individual. Five useful names locate these possible restrictions.

| Position | What can be fixed while preserving earlier assertions |
| --- | --- |
| L4, foundational | A formal or computational construction and the choices its own conditions permit. |
| L3, transdisciplinary | A principle interpreted across eligible disciplines. Bind it to the construction wherever that interpretation is warranted. |
| L2, disciplinary | A subject discipline and the professional method, constraints or interpretation used there. |
| L1, local | Conditions shared by a particular setting or recurrent local population. |
| L0, individual | The identity of the particular entity or occurrence being modeled. Its unobserved characteristics can remain open. |

Read L0 toward L4 as abstraction, and L4 toward L0 as refinement, where the comparisons establish those relations. At each step identify the assertions retained and the warranted interpretation. For a strict step, show which answer the more abstract model admits and the more concrete model excludes, together with a surviving completion. The position's name alone establishes neither preservation nor strictness.

Two successive application positions can admit exactly the same answers, as when a local setting adopts a professional rule unchanged for the inquiry at hand. They then occupy the same abstraction position for that inquiry. Specializing an application keeps the general rule as a premise. Merely discarding inconvenient cases from a purported universal result weakens its support. Use the steps the inquiry needs. Several consequential determinations may fall within one named application position; if the individual was fixed at the outset, binding its identity again removes no possibility.

When the entity is a method, a professional rule can be applied locally and a performed work occurrence can be compared with it. Establishing that the work occurred and followed the rule needs its own evidence. When the entity is a system, a more restrictive model can concern the very same system at the same scale. Moving to a constituent invokes the relevant constructive relation under B.1; its effect on the inquiry needs to be established separately.

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
- A strict comparative name has an answer admitted by A and excluded by every completion of C. Equivalent answers and incomparable answers are reported accordingly.
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

Use B.5.TC for comparisons of theoretical accounts, C.2.1 for the identity and grounding of epistemes, C.29 for a mathematical representation and its correspondence, B.1 for reasoning across holonic scales, and C.37.MM for coordinating and handing on models. E.10.D2 governs the use of a description as a specification. F.19 helps recover the model's assertions from its expression; F.17 and F.18 record the names of this comparison and its relative positions.

### B.5.MR:End
