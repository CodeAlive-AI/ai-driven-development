# UX of AI products

Sources verified **2026-10-21**. Apply to generation, recommendation, assistant and agent interfaces. These sources give research-based and practical recommendations, not a mandatory technical standard. Do not treat the verification year as the publication year. Answer in the user's language; translate internal state identifiers into plain interface text.

## Diagnose before designing

**Skill synthesis:** establish the person's task, the useful outcome, the data available to the system, the cost of an error, the reversibility of the action and the acceptable level of automation. Distinguish the quality of an answer from the quality of the completed task. Clarify what is unknown when it changes the decision; mark other assumptions explicitly. For an audit, request or study the available flow and states: a single screenshot cannot confirm model quality, the presence of undo, the correctness of sources or the success of an external action.

## Apply the sources to the task

### AI-01 — Plan the whole interaction cycle

[Microsoft — Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/). Based on a CHI publication from **2019**; no update date given.

Consider first contact, normal use, AI errors and how the product changes over time. Select the applicable guidelines and decide how to verify them for the specific task. Do not treat all 18 guidelines as mandatory for every feature. Use this material as a research foundation; do not present it as new 2026 research.

### AI-02 — Make capabilities and control clear

[Microsoft — HAX Design Library](https://www.microsoft.com/en-us/haxtoolkit/library/). No update date given.

Explain what the system can do and the nature of its limitations; make invoking, dismissing and correcting a result available. When the goal is unclear, ask for clarification or limit the action. Preserve useful context, provide settings for behavior and report significant changes in capabilities. Design personalization with clear boundaries: a recommendation to take behavior into account does not permit hidden data collection and does not prove that the model retrains immediately.

### AI-03 — Help people judge reliability

[Google PAIR — Explainability + Trust](https://pair.withgoogle.com/guidebook-v2/chapter/explainability-trust/). No chapter update date given.

Show the data, limitations and explanations a person needs to decide. The goal is appropriate trust: understanding when to verify a result. Show numeric confidence only when there is a meaningful, validated metric and its usefulness is proven in user testing. Do not invent percentages and do not turn the plausibility of text into a probability of correctness. If a number misleads, use a specific description of the uncertainty and the available next step. Match the amount of explanation to the complexity and consequences of the decision.

### AI-04 — Make feedback honest

[Google PAIR — Feedback + Control](https://pair.withgoogle.com/guidebook-v2/chapter/feedback-controls/). No chapter update date given.

Distinguish deliberate feedback from a behavioral signal: a click does not necessarily mean preference. Say what the feedback will change, for whom and when. Provide ways to change earlier preferences, reset personalization and manage the applicable data settings. Do not promise instant learning if feedback only goes into an analysis queue. Match the granularity of feedback to what the system can actually change; do not collect extra input without a clear purpose.

### AI-05 — Design for recovery

[Google PAIR — Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/). No chapter update date given.

Distinguish a wrong result, a technical failure, a capability limit and a wrong assumption about the person's context. Offer a workable way out: correcting the input, clarifying, retrying, another way to finish, or help. When control is handed over, preserve the necessary information and explain the next step. Do not assume manual mode is universally safe. Collect problem reports next to the ordinary result as well: the system may not recognize its own error.

### RE-01 — Make explanations verifiable

[NN/g — Explainable AI in Chat Interfaces](https://www.nngroup.com/articles/explainable-ai/), **2025-12-12**; the author's analysis of interfaces and observations.

Link each source to the claim it supports, show a clear name and, where possible, open the relevant passage. Check that the link exists and that its content matches the claim. A citation or a confident explanation does not by itself confirm that the answer is correct. Do not present a generated rationale as a faithful trace of the model's internal process. Do not hide significant limitations in a general disclaimer far from the point of decision.

### RE-02 — Verify AI audits

[NN/g — Demand Accuracy in Your AI Tools: Lessons from Baymard Institute](https://www.nngroup.com/articles/baymard-ai-tool-accuracy/), **2026-01-30**; interviews and the author's analysis, not a universal model benchmark.

Separate a detected pattern from the judgment of whether it is appropriate. For each finding state the observation, the task context, the source and the way to verify it; mark properties that cannot be verified from the available materials. Do not transfer the accuracy of the model or product mentioned to the current tool. Accept an AI recommendation to change the interface after checking its applicability, not because the wording is convincing.

## User states and actions

The following table is a **practical skill synthesis** based on control and recovery; it is not a named state model from HAX or PAIR. Choose only the states that exist in the product.

| Internal state | What to show the person | Available control |
|---|---|---|
| `staged` | The prepared result and the consequences of applying it | Edit, apply, dismiss |
| `running` | The real stage of work; waiting without invented progress | Stop, if the operation supports stopping |
| `done` | The confirmed result and where it appears | Review; undo, if recovery is possible |
| `partial` | What was done, what remains, which consequences have already occurred | Finish the remainder or fix a specific part |
| `failed` / `cancelled` | The cause, the preserved context and the actual outcome | Retry safely or choose another path |

**Skill synthesis:** match confirmations to consequences. For significant external actions give a verifiable preview; for reversible actions use control and recovery without needless interruptions. Do not show successful completion before the system confirms it. When retrying after partial completion, prevent duplication of an action already performed.

## Minimum scenario check

**Skill synthesis:** walk through an ordinary task, ambiguous input, a wrong answer, missing data, a technical failure, cancellation and partial completion. Check that user edits are preserved, controls are available, the next step is clear and the status matches the actual result. Evaluate observable behavior; separate the checks performed from proposed research with representatives of the audience.
