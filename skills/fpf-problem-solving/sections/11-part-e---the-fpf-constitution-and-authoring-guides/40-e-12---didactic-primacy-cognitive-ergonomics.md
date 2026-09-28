## E.12 - Didactic Primacy & Cognitive Ergonomics

### E.12:1 - **Problem Frame**

Use this pattern in either of two working situations:

- **An assurance claim has no clear practical benefit.** An author or reviewer can see the proof or assurance level but cannot say what it helps the intended user understand or decide. Apply the Rationale Mandate in §4.2: explain that benefit in ordinary language, or leave the claimed benefit unexplained pending a substantive answer. The assurance-level judgement retains its own B.3.3 profile.
- **A reader gets stuck, or a work demand appears excessive.** Identify the actual passage or workflow, reader task, stated prerequisites and missed or costly action. Apply the bounded HF-Loop in §4.3 to compare a justified alternative while preserving the method and controls. Return a supported repair, no change or the exact evidence limit; §4.4 shows a no-change result.

The first route asks why formal assurance helps. The second investigates a concrete obstruction or burden; a general complaint about complexity alone does not diagnose it. A missing subject prerequisite, a necessary control or a genuine decision difficulty may remain after the wording is clear. Keep the inquiry's cost proportionate to the useful result it can change.

### E.12:2 - **Problem**

If the framework's design prioritizes theoretical purity or formal completeness over cognitive ergonomics, it becomes vulnerable to two critical failure modes:

1.  **Goodhart's Law:** When a measure, such as an `AssuranceLevel` within a declared `B.3.3` profile, becomes the primary target, it can cease to indicate the understanding sought. Teams may start "gaming the metrics," producing assurance-bearing epistemes or publications that satisfy the visible criteria but remain conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users—the very agents it is meant to serve—either burn out or abandon it in favor of simpler, albeit less rigorous, methods. The "Operating System for Thought" devolves into a bureaucratic machine for certification.

### E.12:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How to build a system that is both formally sound and cognitively accessible, without sacrificing one for the other. |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How to ensure that the production of high-quality epistemes or publications (the means) always serves the ultimate goal of enhancing an agent's cognitive capabilities (the end). |

### E.12:4 - **Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

#### E.12:4.1 - The Principle of Didactic Primacy (Expanded Definition)

The primary purpose of the FPF is to enhance the cognitive capabilities (qualified holder ability under A.2.2) of a reasoning system, team, organization, or other acting holon in service of its objectives. The creation of assurance-bearing epistemes or publications with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in that holder's ability to reason effectively.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance episteme or publication (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is a narrative explanation of the cognitive benefit.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate requires the author to explain how the formal assurance serves its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally checked episteme or publication, the `rationale` is where they answer your fundamental question: "This is impressive, but so what? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer is not clear in the `rationale`, the formal work's claimed practical benefit remains unexplained. Use this question to keep the team's formal work focused on the value it is meant to create. Any assurance-level claim needs its own applicable `B.3.3` profile and result.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)

Use this bounded inquiry when an intended reader encounters a specific consequential obstruction in a named passage or workflow under its stated prerequisites, or when a concrete work demand may cost more than it contributes to the receiving value. A workload report can identify a concern; it does not diagnose its cause or establish a psychometric threshold.

1. **Recover the working question.** Name the reader's task, passage or workflow, stated preparation/access prerequisites, failed or costly action, and the result it should support. Preserve the relevant assurance and control conditions. If the suspected demand cannot change a worthwhile result, C.11.DUA can justify stopping the inquiry at that limit.
2. **Inspect the initial attempt before explaining.** For an actual reading inquiry, retain what the reader initially understood and tried with the public passage and stated task inputs, including where the action stopped or went wrong. Distinguish an implicit condition, a missing stated prerequisite and an unavoidable subject question. Choose the inquirer for this question; profession, competence, assignment and amendment authority remain distinct.
3. **Compare a meaning-preserving alternative.** Make an implicit condition explicit, reduce an unnecessary demand or change the expression only where the suspected obstruction warrants that comparison. Hold task, prerequisites and assurance constant. Check the full connected passage under F.19; a shorter text that removes a needed condition has not preserved the method. Evaluate the attainable inquiry's burden under C.11.DUA.
4. **Qualify the evidence.** An expert walkthrough judges recovery from the public text; it is not an observed reader response. Preserve an actual reader's unassisted first attempt. A repeat after explanation is assisted and familiar, not another independent first reading or proof of reduced workload. Psychometric or causal conclusions require their own selected domain methods and data.
5. **Stop with the supported result.** Return a justified wording/content repair, no change, or the exact evidence limit and any worthwhile next question. The inquiry proposes; the applicable content/amendment authority decides. Use E.9 for a substantive FPF decision and its lighter wording route for ordinary editorial repair. Neither a role title nor a DRR implements or authorizes an amendment by itself.

#### E.12:4.4 - A result-reuse passage examined at equal conditions

The actual E.11.PUR §4.2.1 asks whether an earlier result answers the present concern, using the direct result pattern to compare its EntityOfConcern/edition, question/use, source/dependency conditions and qualification/currentness boundary. It then says: “When those values still match, cite and use the earlier result.” Its following instructions retain any needed A.10 reliance and G.11 currentness account, and reopen the smallest affected result question when a value changes.

For the same task and prerequisites, compare that connected passage with this alternative sentence: “Cite and reuse the earlier result only when its subject and edition, question and use, relied sources and dependencies, and qualification/currentness still answer the present concern.” Keep the surrounding reliance and reopen rules in both versions. This makes the antecedent explicit without relaxing any assurance condition.

An expert walkthrough can recover all four comparison duties from the actual passage's preceding list; on that basis alone, no change is required. No reader observation or workload measurement is asserted by this example. If an actual initial attempt instead misses the reuse condition, retain that response and examine whether the explicit alternative repairs that miss. If the reader lacks an expressly required subject prerequisite, or the difficult step is deciding whether the source remains applicable, making the sentence shorter does not justify deleting that condition. A second attempt after explaining the list can support only a qualified assisted-reading result. Stop at the demonstrated repair, no-change result or exact limit of that comparison.

### E.12:5 - **Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every key assurance episteme or publication, including a `U.AssuranceCase` or proof publication, **MUST** contain a non-empty, human-readable `rationale` that satisfies the "So What?" test. Any `AssuranceLevel` claim separately cites its applicable `B.3.3` profile and shows that the target meets that profile's criteria.
*   **CC-E12.2 (Bounded inquiry trigger):** A significant workflow **SHOULD** make consequential reader obstructions or doubtful work demands recognizable. An inquiry names the task, passage/action, prerequisites and relevant assurance boundary; a conceptual workload threshold alone is insufficient.
*   **CC-E12.3 (Inquiry and stop):** For a live trigger, apply §4.3 at a burden warranted by C.11.DUA. An actual reading inquiry preserves the initial unassisted attempt before explanation and compares any proposed alternative at unchanged task/prerequisites/assurance. Return a supported repair, no change or the exact evidence limit; qualify assistance and leave amendment authority separate.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

### E.12:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes a beautiful but impenetrable fortress of abstract logic that no practicing engineer can actually use. | A practitioner can report a concrete obstacle and request inquiry into its cause. A supported proposal follows the applicable content-decision or editorial rule; reviewer competence and assignment do not themselves grant authority to amend the framework. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without a connection to the problem. | The "So What?" test asks the author to explain the cognitive or practical benefit claimed for the formal work. A perfunctory `rationale` fails this pattern's rationale requirement; assess any assurance-level claim separately against its applicable `B.3.3` profile. |
| **Glorifying Complexity** | A culture emerges where the most complex and difficult-to-understand models are considered the "best," regardless of their utility. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern create a constant pressure towards simplicity and clarity. Inspect the specific obstruction and compare a meaning-preserving alternative; retain necessary subject complexity and independently justified controls. |

### E.12:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Supports FPF's Core Mission:** The Rationale Mandate and HF-Loop give authors and reviewers ways to challenge formalism that does not help users reason. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* choose a method appropriate to the actual inquiry and report only what its observations/comparison support; the HF-Loop label supplies no psychometric or causal result. |
| **Makes inquiry responsibility explicit:** Name the actual reader question, competent reviewer and applicable amendment authority separately; example profession names create no constitutional power. | - |
| **Supports Early Correction:** An HF-Loop review can identify excessive complexity and propose corrections before users become frustrated and abandon the framework. | - |
| **Supports bounded correction:** Inquiry can yield a repair, no change or a precise evidence limit. | A reading comparison costs reader time; select it only where its attainable result can improve the receiving use. |

### E.12:8 - **Rationale**

This pattern operationalizes **Didactic Primacy (P-2)**, transforming it from a philosophical statement into an enforceable architectural Standard. The `Rationale Mandate` requires a clear explanation of the cognitive purpose of each key assurance episteme or publication. The bounded Human-Factor inquiry examines an actual reader obstruction or work demand while retaining the method's prerequisites and assurance. It does not require a speculative threshold or a refinement proposal when none is supported.

A purely conceptual workload warning would leave the reader without a next action; a stronger psychometric or causal method would require separately justified observations and design. The bounded inquiry supplies an attainable examination and honest stop. It complements formal rigor with the unchanged Rationale Mandate and preserves independently justified controls. Together they support FPF's aim of serving meaningful, human-relevant goals as an "Operating System for Thought."

#### E.12:8.1 - SoTA-Echoing — investigate the obstruction before prescribing simplification

**Practice question.** Does a reader's missed condition justify rewriting the passage, supplying a stated prerequisite, or retaining a necessary difficulty? The selected line examines one task and the initial attempt, compares a meaning-preserving alternative at the same prerequisites and control conditions, and stops with the supported result. A serious cheaper alternative is an expert heuristic review: it can identify likely wording or presentation problems without recruiting a reader, but cannot establish what a reader actually recovered.

The [GOV.UK Service Manual's moderated usability-testing guidance](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) supplies the task-observation line: use believable tasks and neutral instructions that do not reveal the route to completion. **Adapt** that discipline to §4.3 steps 1–2 and 4: preserve the public passage, task inputs and initial attempt before explaining. Its domain is service/interface research; it supplies neither a psychometric workload scale nor evidence that HF-Loop improves reasoning in every framework domain.

[Moran and Gordon's heuristic-evaluation method, 2023](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) supplies the expert-review alternative and its stated limit. It scopes review to tasks and acknowledges that a heuristic violation need not be a defect in context. **Adopt** that economical inquiry where expert recovery settles the wording question, including a justified no-change result. **Reject** promoting that judgment to observed reader success. Use actual reading when the F.19 conditions require it, particularly when competing reconstructions or an observed miss can change the repair.

In §4.4 the expert can recover the four reuse duties from the preceding list, so the shorter explicit sentence is not automatically a better instruction. If the intended reader's first attempt misses one duty, the task-bound comparison can distinguish a hidden antecedent from missing subject preparation. At the same passage and task scope, expert review saves participant time; actual reading costs more but adds evidence the expert cannot supply. Holding assurance fixed prevents an apparent improvement obtained merely by deleting the reuse condition. After an explanation, a successful second attempt remains assisted and familiar.

This comparison governs §4.3's initial-attempt, equal-condition, evidence-qualification and stopping steps, and §4.4's no-change/observed-miss branches. It selects evidence appropriate to the claim instead of a universal reader-test requirement. Reopen when a new unassisted attempt contradicts the expert account, the task or prerequisites change, or a proposed method can answer the same consequential recovery question with lower justified burden. Broader causal, psychometric or population-wide effectiveness claims require separately selected methods and data.

### E.12:9 - **Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Uses:** F.19 for connected meaning-preserving reading and evidence qualification; C.11.DUA for the value and full burden of demanded work or further inquiry.
*   **Complements:** `E.13 Pragmatic Utility and Proxy-to-Value Alignment` keeps visible measures, scores, review results, and release cues tied to intended value; this pattern focuses on the cognitive and working-reader usability of the framework.
*   **Coordinates with:** `E.9` for the bounded content decisions that proposed HF-Loop improvements require. The DRR records the selected answer and rationale; the resulting pattern change carries the implementation. Ordinary editorial repair follows the lighter method identified by `E.9`.

### E.12:End
