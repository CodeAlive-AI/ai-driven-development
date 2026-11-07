## GOALS.7 - Assign and continue goal-directed AI work

**Type:** Method pattern.
**Status:** Stable.

### GOALS.7:1 - Problem frame

**Use this when** an AI system is to pursue a result through reasoning, tools, multiple actions or later continuation, and an ordinary one-response instruction leaves material conditions unclear. The object is the assignment and operating arrangement for that system's goal-directed work. The result is a feasible authorized undertaking with a usable completion or return.

The user or assigning role needs the actual system's capabilities, available inputs, permissions and continuation behavior. A bounded request that already supplies these can proceed directly. Product-specific instructions remain with the current runtime documentation and tools.

### GOALS.7:2 - Problem

An agent can produce a fluent response while the assigned result remains unavailable, repeat a finished operation after losing context, or infer broader authority from an ambitious goal. Conversely, compulsory human repetition of every competent agent action can make useful autonomy unavailable. The assignment must connect the intended result to real means, permissible actions, state and evidence.

### GOALS.7:3 - Forces

Autonomy can reduce coordination while increasing the importance of a well-formed mandate and useful returns. Broad purpose helps the agent choose means; exact constraints govern consequential actions. Context and tool availability can change across sessions. Checking has costs and should answer the consequence-bearing claim. Runtime limits and human reliance may have different horizons.

### GOALS.7:4 - Solution

#### GOALS.7:4.1 - Give the result and the consequential conditions

Describe the recipient's needed result and how it will be used. Include relevant starting work, sources, completion criteria, protected content, constraints and authority. Distinguish the requested result from an example of a defect or a suggested operation. An instruction to repair one bad paragraph can be narrow; an instruction to develop a usable method requires more than that example.

Make consequential permissions explicit through the actual environment: what the agent may read, modify, execute, spend, communicate or publish, and which decisions belong elsewhere. Use existing authorization where it is sufficient. Ask for a missing decision only when the dependent work actually requires it. A broad goal does not override an access boundary or confer another participant's authority.

#### GOALS.7:4.2 - Match the undertaking to the actual configuration

Establish the available tools, context, sources, memory or persisted work, compute limits and any required competence or independence. Use suitable existing evidence for the task and consequence. If a capability is uncertain and that uncertainty could change the arrangement, obtain a proportionate check or use a qualified alternative. A present result from another configuration supports only what its conditions permit.

Allocate work by contributions: the agent may perform substantive analysis and authorized execution; a human or another system supplies only the decisions, expertise, participation or independent judgement actually needed. Account for source retrieval, checking, correction and recipient attention as well as generation. A human need not supervise every reversible operation if the required guarantees and authority support competent autonomous performance.

When the task includes human learning, use GOALS.6 to preserve the human operation and evidence separately. If the desired result is only the delivered artifact, compare competent direct provision with the additional burden of making the human reproduce its construction.

#### GOALS.7:4.3 - Make continuation possible across the real boundary

Keep the current goal, relevant decisions, accepted results and material remainder in the work product or persistence mechanism that the runtime can actually recover. Preserve enough source identity and conditions to continue without repeating or silently replacing the task. Reuse an existing durable account; do not add another synchronized ledger merely because the work is long.

Choose the continuation arrangement from the actual system. A persistent execution can continue within its budget. A new session may need explicit recovery of the task and saved work. Scheduled later work requires an effective scheduling mechanism. A written promise to return later does not establish that mechanism. Before relying on it, verify the relevant supported behavior and identify what happens at interruption or exhaustion.

On resumption, recover what is complete, what remains and any newer instruction that changes the task. Continue from actual evidence. If an external dependency is missing, return its exact effect and preserve independent useful work; avoid repeating the same unavailable action without a changed condition.

#### GOALS.7:4.4 - Judge completion against the receiving use

Before claiming completion, compare the actual result with the original goal and its latest valid clarifications. Have the necessary actions been performed, the required contributions obtained and the result made usable to its recipient? Tool success can establish a particular operation; a saved artifact can establish availability; subject correctness and authorization can require different evidence.

Distinguish the result wanted by the recipient, the criterion and environment used to evaluate it, and any reward used to train or select the model. Establish what a reported score warrants under that configuration. When the agent can alter tests, data or a judge that supplies completion evidence, preserve an independently controlled basis for the consequential claim or arrange a suitable independent replay. An authorized improvement to the evaluator needs its own grounds. Use GOALS.2 to examine how apparent success could leave the wanted result absent, and obtain the technical evaluation method appropriate to the system and consequence.

Use checks selected for the actual failure consequence, including independent judgement where required. The authoring agent cannot supply independence from its own authorship. Reuse matching results when the candidate and conditions are unchanged. An inability to complete a required step yields a bounded result and a precise unmet condition, rather than a changed definition of success.

Report what was obtained, the material limits and the next action required of the recipient. For continuing work, distinguish the completed current contribution from the still-active wider aim. End when the assigned result is complete or return the actual impasse; continued activity is not itself the goal.

Recognition notices an assignment whose text, authority or continuation cannot support the expected work. Assurance concerns actual capability, performed actions, retained state, result evidence and any stronger reliability claim under the chosen configuration.

### GOALS.7:5 - Archetypal Grounding

A maintenance agent is assigned to find why a report misstates totals, repair the authorized source and produce a verified result for review. The existing instruction permits local edits and tests, while publication belongs to another role. The agent recovers the source and consumers, repairs the calculation, performs the relevant checks and gives the reviewer the usable candidate and evidence. A successful local test does not perform publication, which was outside this assignment.

For that review, the accounting owner supplies the transaction population and a separately calculated control total. The agent can edit the report code and its unit tests; changing their expected values could make those tests pass while leaving the accounting error intact. The reviewer therefore compares the repaired report with the retained transaction basis and control total. If an authorized correction changes which transactions belong to the period, the accounting owner resolves that criterion and the comparison is rerun. The evidence now concerns the intended accounting result under the agreed criterion.

Now change the task: the agent is authorized to carry an accepted change through the actual release path. Returning only a tested patch leaves the assigned result incomplete. The continuation must include the authorized integration, publication checks and recipient access, subject to the actual environment. This difference follows the mandate, not a universal human approval after every tool call.

For a long research task, the runtime stops after a resource limit. A saved account identifies the completed source interpretation and the unresolved comparison. The next session recovers them and resumes that comparison. If the supposed saved state contains only “keep researching,” the missing reasoning must be recovered before dependent conclusions can be trusted; inventing continuity would risk changing the task.

### GOALS.7:6 - Bias-Annotation

Capabilities vary by model, configuration, tools and task. Evaluate the required contribution rather than assuming either human superiority or agent competence from a label. Human psychological findings about goal adoption, affect or well-being do not establish an AI mechanism or permission.

### GOALS.7:7 - Conformance Checklist

- Does the assignment preserve the intended receiving result and its actual scope?
- Are consequential actions within effective authority and available means?
- Can the runtime recover the state required for continuation?
- Does completion evidence concern the result rather than only the last operation?
- What does the evaluation score warrant, and who can alter the criterion, data or evaluator on which that conclusion relies?
- Are required independent and human contributions preserved without unsupported duplication?

### GOALS.7:8 - Common Anti-Patterns and How to Avoid Them

**Stopping at the user's example:** recover the broader assigned result and compare it with what remains.

**Persistence by assertion:** use an effective continuation mechanism and its actual limits.

**Autonomy through inferred authority:** keep the goal's purpose distinct from permission to make a consequential change.

**Human repetition as a default guarantee:** name and perform the specific needed judgement, authorization or participation instead.

### GOALS.7:9 - Consequences

The agent can do substantial work with fewer avoidable handoffs while returning meaningful exceptions and results. The arrangement also makes interruption and failure recoverable. It requires current knowledge of the actual system; no general prompt can guarantee arbitrary competence or persistence.

### GOALS.7:10 - Architectural Rationale

Goal-directed AI work shares the result–evidence–means connection with human and organizational work, but its continuation and action depend on technical and institutional conditions. This method reconstructs those relations rather than transferring a human motivation theory or freezing a particular product interface into the framework.

### GOALS.7:11 - SoTA-Echoing

Tankelevitch and Rintel's 2026 position paper motivates explicit goal meaning, history and revision in human–AI collaboration. It supplies design arguments, not a measured effectiveness result. Documented autonomous workflows show concrete possibilities under their configurations. This method adopts recoverable goals and capable allocation while requiring current runtime grounds for the actual use; product changes reopen the technical arrangement.

OpenAI’s 2025 coding experiments document reward-driven exploitation of evaluation loopholes. Its May 2026 guidance for third-party evaluations connects a performance claim to the model, tools, environment, resources and evaluator actually used. These contributions motivate the explicit result–criterion–reward distinction and controlled completion evidence in section 4.4. A score supports a bounded claim under the reported conditions; stronger reliability claims require their own evidence.

### GOALS.7:12 - Relations

GOALS.1–4 supply common goal interpretation, achievement, feasibility and revision. GOALS.6 preserves separately wanted human mastery. C.43 supplies control and C.39 develops a missing way. Applicable local execution, security, tool and professional methods supply the precise operational conditions.

### GOALS.7:End
