## E.12 - Didactic Primacy & Cognitive Ergonomics

> **Status:** Stable

### E.12:1 - **Problem Frame**

Use this pattern in either of two working situations:

- **An assurance claim has no clear practical benefit.** An author or reviewer can see the proof or assurance level but cannot say what it helps the intended user understand or decide. Apply the Rationale Mandate in §4.2: explain that benefit in ordinary language, or leave the claimed benefit unexplained pending a substantive answer. The assurance-level judgement retains its own B.3.3 profile.
- **A reader gets stuck, completes a different task fluently, or encounters a costly demand.** Compare the work the intended recipient brought with the task and help available in the passage. Use §4.3 to locate the lost choice, missing support or unnecessary demand and test a repair against the original use.

The first route asks why formal assurance helps. The second investigates the work a passage actually elicits, including a different choice made smoothly. A missing subject prerequisite or unsuitable assignment may call for a different intervention from a repair to the explanation.

### E.12:2 - **Problem**

Giving theoretical purity or formal completeness priority over cognitive ergonomics exposes the framework to two serious failures:

1.  **Goodhart's Law:** When a measure, such as an `AssuranceLevel` within a declared `B.3.3` profile, becomes the primary target, it can cease to indicate the understanding sought. Teams may optimize for the metric and produce assurance-bearing epistemes or publications that satisfy the visible criteria but remain conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users burn out or switch to simpler, less rigorous methods. Certification procedures can consume effort without helping users understand or decide the matter at hand.

### E.12:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How can a system remain formally sound and cognitively accessible? |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How can producing high-quality epistemes or publications always serve the goal of enhancing an agent's cognitive capabilities? |

### E.12:4 - **Solution**

FPF makes **Didactic Primacy (Pillar P-2)** an architectural principle. The Rationale Mandate connects formal assurance to its cognitive benefit; the Human-Factor Loop investigates a concrete obstruction or doubtful demand.

#### E.12:4.1 - The Principle of Didactic Primacy

The primary purpose of the FPF is to enhance the cognitive capabilities (qualified holder ability under A.2.2) of a reasoning system, team, organization, or other acting holon in service of its objectives.

Any architectural decision that increases formal rigour at the cost of clarity or usability must explicitly justify the gain in reasoning that warrants this cost. A checked bound can let an experienced engineer rule out an infeasible operating mode today. That decision with the proof available can be the entire benefit of the work. To claim that the engineer has acquired a lasting ability, compare relevant performances over time with the aids available on the intended job.

#### E.12:4.2 - Mechanism 1: The Rationale Mandate

Every key assurance episteme or publication, such as an assurance case or proof publication, **MUST** contain a human-readable **`rationale`** component. Use B.3:4.2 to develop and inspect the assurance case's argument for the stated use; the rationale explains its practical and cognitive benefit.

*   **Nature:** The `rationale` is a narrative explanation of the cognitive benefit.
*   **Content:** It **MUST** answer: *"How does this level of formal assurance help the agent understand the problem better or make a more reliable decision?"*
*   **Purpose:** The author explains what the formal assurance helps the user understand or decide. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

Name the decision the assurance makes possible. To claim that the work now takes less effort, compare the work required at comparable correctness, including preparation or help that the job calls for.

> **The "So What?" Test for Managers**
>
> When your team presents a complex, formally checked episteme or publication, ask them to explain its benefit in the `rationale`. For example, how does the formal work help you ship a better product, make a better investment, or avoid a critical risk? If the answer is not clear in the `rationale`, the formal work's claimed practical benefit remains unexplained.
>
> Use this question to keep the team's formal work focused on the value it is meant to create. Any assurance-level claim needs its own applicable `B.3.3` profile and result.

#### E.12:4.3 - Mechanism 2: The Human-Factor Loop (HF-Loop)

Use this inquiry when the working result gives reason to examine what a passage or workflow asks of its intended reader. Difficulty can be visible as delay, an unsuccessful attempt, excessive work or a fluent answer to a different question. A workload report or a smooth performance can justify looking closer. Establish what the reader was actually doing before attributing a cause.

1. **Recover the working question.** Read the recipient's commission beside the task they actually received. Identify who had to decide or explain what, which objects and conditions mattered, and which choices the instructions or ordinary help already supplied. Follow the difference to its consequence for the intended work.

   Preserve the relevant assurance and control conditions. If the suspected demand cannot change a worthwhile result, C.11.DUA can justify stopping the inquiry at that limit.
2. **Inspect the initial attempt before explaining.** Retain what the reader understood and did with the published passage, task inputs and ordinary permitted support. Include a successful answer to a different task when it helps locate the change of question.

   Distinguish an implicit condition, a missing stated prerequisite and an unavoidable subject question.

   Choose the inquirer for this question; profession, competence, assignment and amendment authority remain distinct.
3. **Compare an alternative for the original use.** Make a condition explicit, remove an unnecessary demand or restore the decision the reader was commissioned to make. Distinguish a change to the wording or help from a change to the work assigned.

   Keep the commissioned task, ordinary prerequisites and assurance requirements constant when comparing expressions. If the previous assignment asked for a different result, record that difference and judge the repaired assignment against the original commission. Use F.19 on the connected passage.

   Evaluate the attainable inquiry's burden under C.11.DUA.
4. **Qualify the evidence.** An expert walkthrough judges recovery from the public text; it is not an observed reader response.

   Preserve the first attempt and the support available to the reader at the time. Unaided recognition requires an unaided first attempt. In a practice with ordinary help, observe what the reader can do with that help. A repeat after the reviewer's explanation shows performance under the changed conditions.

   Psychometric or causal conclusions require their own selected domain methods and data.
5. **Stop with the supported result.** Return a justified wording/content repair, no change, or the exact evidence limit and any worthwhile next question.

   The inquiry proposes; the applicable content/amendment authority decides. Use E.9 for a substantive FPF decision and its lighter wording route for ordinary editorial repair. Neither a role title nor a DRR implements or authorizes an amendment by itself.

#### E.12:4.4 - A result-reuse passage examined at equal conditions

Here the commission is to answer the same question from the available grounds. E.11.PUR §4.2.1 asks whether the earlier result still answers it, using the direct result pattern to compare its EntityOfConcern/edition, question/use, source/dependency conditions and qualification/currentness boundary.

The reuse instruction reads: “When those values still match, cite and use the earlier result.” Its following instructions retain any needed A.10 reliance and G.11 currentness account, and reopen the smallest affected result question when a value changes.

For the same task and prerequisites, compare that connected passage with this alternative sentence: “Cite and reuse the earlier result only when its subject and edition, question and use, relied sources and dependencies, and qualification/currentness still answer the present concern.” Keep the surrounding reliance and reopen rules in both versions. This makes the antecedent explicit without relaxing any assurance condition.

An expert can recover all four comparison duties from the preceding list. A separately commissioned independent performance would still be due even if the earlier answer sufficed for this question. No reader observation or workload measurement is asserted by this example.

If an actual initial attempt instead misses the reuse condition, retain that response and examine whether the explicit alternative repairs that miss.

If the reader lacks an expressly required subject prerequisite, or the difficult step is deciding whether the source remains applicable, making the sentence shorter does not justify deleting that condition.

A second attempt after explaining the list can support only a qualified assisted-reading result. Stop at the demonstrated repair, no-change result or exact limit of that comparison.

### E.12:5 - **Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every key assurance episteme or publication, including an assurance case or proof publication, **MUST** contain a non-empty, human-readable `rationale` that satisfies the "So What?" test. Any `AssuranceLevel` claim separately cites its applicable `B.3.3` profile and shows that the target meets that profile's criteria.
*   **CC-E12.2 (Bounded inquiry trigger):** Examine a consequential mismatch between the commissioned work and the work the passage elicits, an obstruction or a doubtful work demand. Recover the task, passage, prerequisites and assurance the use requires.
*   **CC-E12.3 (Inquiry and stop):** Apply §4.3 at a burden warranted by C.11.DUA. Preserve what the reader did before the reviewer's explanation and the help ordinarily available. Compare the candidate with the commissioned task and its intended conditions. State the repair, the grounds for retaining the passage or what the evidence leaves open. A reader's success supports conclusions about the work that reader actually did.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

### E.12:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | What a Manager May Observe | How to Respond |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes an elegant account of abstract logic that practicing engineers cannot use. | A practitioner can report a concrete obstacle and request inquiry into its cause. A supported proposal follows the applicable content-decision or editorial rule; reviewer competence and assignment do not themselves grant authority to amend the framework. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without a connection to the problem. | The "So What?" test asks the author to explain the cognitive or practical benefit claimed for the formal work. A perfunctory `rationale` fails this pattern's rationale requirement; assess any assurance-level claim separately against its applicable `B.3.3` profile. |
| **Glorifying Complexity** | Teams prize the most complex, hard-to-understand models regardless of their usefulness. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern give teams a standing reason to favor simplicity and clarity. Inspect the specific obstruction and compare a meaning-preserving alternative; retain necessary subject complexity and independently justified controls. |

### E.12:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Supports FPF's Core Mission:** The Rationale Mandate and HF-Loop give authors and reviewers ways to challenge formalism that does not help users reason. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* choose a method appropriate to the actual inquiry and report only what its observations/comparison support; the HF-Loop label supplies no psychometric or causal result. |
| **Makes inquiry responsibility explicit:** Name the reader's question, a competent reviewer and the applicable amendment authority separately. Naming a profession as an example grants no formal decision-making authority. | - |
| **Supports Early Correction:** An HF-Loop review can identify excessive complexity and propose corrections before users become frustrated and abandon the framework. | - |
| **Supports bounded correction:** Inquiry can yield a repair, no change or a precise evidence limit. | A reading comparison costs reader time; select it only where its attainable result can improve the receiving use. |

### E.12:8 - **Rationale**

The `Rationale Mandate` connects formal assurance to its cognitive purpose. The Human-Factor inquiry examines a consequential difference in the reader's work, including apparent success on an easier assignment. Its result may justify a repair, retention or further inquiry.

A purely conceptual workload warning would leave the reader without a next action; a stronger psychometric or causal method would require separately justified observations and design.

The bounded inquiry supplies an attainable examination and honest stop. It complements formal rigor with the Rationale Mandate and preserves independently justified controls. Together they connect formal assurance with what practitioners need to understand or decide for their work.

#### E.12:8.1 - SoTA-Echoing — investigate the obstruction before prescribing simplification

**Practice question.** Does a reader's missed condition justify rewriting the passage, supplying a stated prerequisite, or retaining a necessary difficulty? The selected line examines one task and the initial attempt, compares a meaning-preserving alternative at the same prerequisites and control conditions, and stops with the supported result.

An expert heuristic review offers a less costly alternative. It can identify likely wording or presentation problems without recruiting a reader, but cannot establish what a reader actually recovered.

The [GOV.UK Service Manual's moderated usability-testing guidance](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing) supplies the task-observation line: use believable tasks and neutral instructions that do not reveal the route to completion. **Adapt** that discipline to §4.3 steps 1–2 and 4: preserve the public passage, task inputs and initial attempt before explaining.

Its domain is service/interface research; it supplies neither a psychometric workload scale nor evidence that HF-Loop improves reasoning in every framework domain.

[Moran and Gordon's heuristic-evaluation method, 2023](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/) supplies the expert-review alternative and its stated limit. It scopes review to tasks and acknowledges that a heuristic violation need not be a defect in context.

**Adopt** that economical inquiry where expert recovery settles the wording question, including a justified no-change result. **Reject** promoting that judgment to observed reader success.

Use actual reading when the F.19 conditions require it, particularly when competing reconstructions or an observed miss can change the repair.

In §4.4 the expert can recover the four conditions for using the earlier answer from the preceding list, so the shorter explicit sentence is not automatically a better instruction.

If the intended reader's first attempt misses one duty, the task-bound comparison can distinguish a hidden antecedent from missing subject preparation.

At the same passage and task scope, expert review saves participant time; actual reading costs more but adds evidence the expert cannot supply.

Holding assurance fixed prevents an apparent improvement obtained merely by deleting the reuse condition. After an explanation, a successful second attempt remains assisted and familiar.

This comparison governs §4.3's initial-attempt, equal-condition, evidence-qualification and stopping steps, and §4.4's no-change/observed-miss branches. It selects evidence appropriate to the claim instead of a universal reader-test requirement.

Reopen when a new unassisted attempt contradicts the expert account, the task or prerequisites change, or a proposed method can answer the same consequential recovery question with lower justified burden.

Broader causal, psychometric or population-wide effectiveness claims require separately selected methods and data.

### E.12:9 - **Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Uses:** F.19 for connected meaning-preserving reading and evidence qualification; C.11.DUA for the value and full burden of demanded work or further inquiry.
*   **Complements:** `E.13 Pragmatic Utility and Proxy-to-Value Alignment` keeps visible measures, scores, review results, and release cues tied to intended value; this pattern focuses on the cognitive and working-reader usability of the framework.
*   **Coordinates with:** `E.9` for the bounded content decisions that proposed HF-Loop improvements require. The DRR records the selected answer and rationale; the resulting pattern change carries the implementation. Ordinary editorial repair follows the lighter method identified by `E.9`.

### E.12:End
