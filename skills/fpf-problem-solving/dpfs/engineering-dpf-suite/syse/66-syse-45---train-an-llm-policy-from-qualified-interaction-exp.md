## SYSE.45 - Train an LLM Policy from Qualified Interaction Experience

> **Type:** Method pattern
> **Status:** Stable

### SYSE.45:1 - Problem frame

**Use this when** a recurring task warrants changing model parameters or adapters, and qualified interaction experience can teach the targeted behavior. Repeatedly supplying stable guidance may be costly; an existing policy may also keep making a consequential mistake.

The subject is the trained policy candidate and the experience, learning mechanism and retained support that make its changed behavior interpretable. The first useful result is a changed candidate with a bounded comparison, or the precise data, training or evaluation gap.

Compare training with retaining help, improving retrieval, constructing a tool or repairing the external controller. Selecting or transforming the next input belongs to SYSE.52, routing and return consumption to SYSE.47, and external recording to SYSE.43. If training is unavailable, those feasible alternatives remain available. Human practice and learning use E.23.CDI/HCD with their own mechanisms. This pattern supplies a bounded machine-policy intervention; foundation-model pretraining and the receiving domain's correctness criterion remain external.

### SYSE.45:2 - Problem

A successful trajectory can contain incidental values, unnecessary steps or a hidden external contribution. Training on it can reproduce the answer while losing the conditions for success. Removing guidance may then look like internalization even though the agent has simply stopped obtaining necessary evidence.

### SYSE.45:3 - Forces

Stable knowledge may be cheaper to use through a trained policy, but changing interfaces make that knowledge costly to maintain. Successful demonstrations give a target, while informative failures reveal its limits. Feedback can reward an observable proxy rather than the required result. Training and validation share a budget, yet repeated validation can make the final comparison optimistic.

### SYSE.45:4 - Solution

#### SYSE.45:4.1 - Fix the target and retained configuration

Name the behavior to change and its receiving result: for example, forming valid arguments, selecting a useful observation or applying stable procedural guidance. Name the base model and parameter or adapter set to update. Separate that change from context, memory, tool, controller and environment changes. When the target is assistance selection, consume SYSE.50's decision unit, available signals, qualified need evidence and fallback; selecting training does not itself establish which help is needed. For learned effort control, consume SYSE.51's feasible moves, intermediate decision basis, cost accounting and completion obligations; retain externally enforced hard limits.

Specify the external contributions that remain: execution, current observations, access permissions, retrieval when facts change and independent checking where the claim needs it. Compare complete later configurations through C.38/C.11.CRC and C.11. Include stability of the proposed mapping, expected recurrence, target preparation, training, independent qualification, maintenance and the fallback after a failed trial. A cheaper response that loses a necessary contribution is a different result. The [Reference comparison (Engineering.Reference:19.7)](../suite-reference/21-engineering-reference-19---make-an-available-contribution-wo.md#engineeringreference197---develop-the-arrangement-across-attempts) selects an explicit rule for its supplied 100-update conditions and manual work for five.

Keep an unchanged baseline and the means to restore it. Establish the task-family boundary and what finding would make training no longer worthwhile.

#### SYSE.45:4.2 - Obtain experience with interpretable feedback

Collect observation/action trajectories whose inputs, source/configuration and outcomes can be recovered. Include successful alternatives, informative failures, required restraint and changed-condition cases. Use SYSE.49 when the needed experience must be constructed; qualify its feedback before using it as a training signal.

Separate the agent's actions from tool observations and the judge's conclusions. For each selected target, identify what counts as correct and why. A failed trace can teach a corrected action or a failure condition; blindly imitating its actions teaches the failure.

Partition construction, adaptive validation and final evaluation by the dependencies that could leak the answer, such as shared scenarios, source instances or near-duplicate trajectories. Keep the final cases outside training and repeated candidate selection. Generated labels remain provisional until their result meaning is qualified.

#### SYSE.45:4.3 - Select and execute the learning mechanism

First choose the experience transformation that can supply the intended policy target. The learning algorithm then consumes that target.

| Available experience and intended change | Construct the signal | Further-use question and return |
| --- | --- | --- |
| A qualified action sequence demonstrates the needed behavior | Pair each retained decision history with the agent action it warrants. Keep tool observations as inputs, and fit only the intended agent outputs. Vary target identifiers and values across applicable examples while preserving their correct binding in each target action. | Does the policy choose the action on a new applicable input and abstain on an unsupported one? An unqualified successful transcript returns to result/trajectory assessment. |
| A recorded decision is wrong or unnecessarily costly | An experience-informed teacher proposes a corrected next action at that history. Qualify it against the task, interface and facts the student will actually have. Train the student on that history/action pair without the teacher's extra experience. | Does the correction remain warranted without hidden teacher facts? Obtain a needed fact or retain support if it does not. The old next observation follows the old action, not the proposed correction. |
| A search or deliberation procedure finds useful candidates | Preserve selected candidate comparisons, evaluation grounds and backtracking decisions as targets where their signals are available to the student. Distillation can transfer how candidates are generated or compared. | Test unseen alternatives and defeated evaluator premises. Imitating a planner's trace does not transfer its proof or guarantee. |
| Actual attempts supply outcome or process feedback | Bind feedback to the required result and protected conditions. When a final reward leaves the responsible decision unclear, use a qualified intermediate state or a discriminating action contrast to localize the target. Keep an uncertain credit assignment at that evidential strength. | Test the actual result and the relevant intermediate behavior separately. Reward growth with duplicated effects or lost required access fails. |
| Qualified comparative judgements express a preference | Name whose preference, the task/context, the compared action or answer pair and the grounds for its ordering. Give those pairs to a supported preference-training Method and implementation; return a missing judgement or implementation. | Preferred behavior still needs independent factual, permission and protected-result grounds. A rater's preference supplies no missing world effect. |

**Match the update to that signal.** Supervised learning fits qualified actions or corrected continuations; reinforcement learning uses attempted actions and qualified reward; distillation transfers the selected teacher or search behavior. CMP.7 supplies learner construction and the distinction between obtaining data, fit and further use. The selected implementation supplies the exact update algorithm, tokenizer and trainable parameters. Bind them to these data transformations and the later input format. Keep the configuration that actually produced each comparison.

For decisions separated by tool observations, [Engineering.Reference:26.4.1](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2641---learn-from-interleaved-actions-and-observations) constructs the learning histories, selects generated positions, calculates an outcome update and uses the changed policy with its retained tool. It explains how annotated calls, prepared demonstrations, justified preferences or changing stage objectives change the required input and what the update can teach. A useful call followed by a failed answer makes the limits of terminal credit visible.

When additional training attempts compete for a limited budget, [Engineering.Reference:26.4.2](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2642---allocate-training-attempts-and-select-the-update) obtains a probability measure, allocates and executes continuations, and consumes their qualified feedback in an update. It separates the allocation rule, entropy modulation and a selected backward operation, with explicit returns for missing probability access and changed resource or clipping conditions.

For an explicit strategy followed by conditional execution, [Engineering.Reference:26.4.3](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2643---learn-a-strategy-together-with-its-execution) constructs separate comparison groups, updates both choices and tests whether favorable outcomes are controllable by learning. When an action changes memory retained across sessions, [26.4.4 (Engineering.Reference:26.4.4)](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2644---learn-actions-whose-value-persists-across-sessions) obtains continuation credit, updates the present choice and consumes the retained information later. It compares value estimates, a recurrence heuristic and controlled memory-editing trials, with returns for changed recurrence or unreliable help.

When an external procedure supplies useful demonstrations, [Engineering.Reference:26.4.5](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2645---transfer-a-procedure-through-teacher-guided-learning) explains how to select hard targets, teacher distributions or outcome feedback, compute a first update and execute the changed policy after a fresh observation. It also compares three responses to inadequate guidance: change its weight, obtain better evidence for the teacher, or adapt the teacher itself.

To choose which recurring guidance to learn or retain, [Engineering.Reference:26.4.6](../suite-reference/28-engineering-reference-26---construct-a-guard-a-learning-upda.md#engineeringreference2646---select-what-to-learn-and-reassess-the-support-that-remains) constructs the intervention, qualified target, first updates and subsequent joint support arrangement. It shows why removing either guide alone can preserve the result while removing both loses it, how a new fact changes the next assistance decision, and when keeping an aid or obtaining a converter is preferable.

**Construct tool knowledge and use separately when that is the gap.** Tool-Internalized Reasoning separates learning a tool's documented semantics, supervised preparation on tool-use trajectories, and optimization of subsequent tool reasoning. For an interval setter, the semantic target includes what operation and unit its arguments denote; a trajectory target then puts the call at the right decision with the right observations. A later reward can distinguish the selected tool and argument choice only at its qualified meaning. At inference, that source first selects tool tokens, retrieves the selected tools' current descriptions and parameters, then generates arguments; retain the documentation lookup with the executor. Its special tool vocabulary, document/token mapping and reward are implementation choices, not prerequisites for every adapter. A tool/argument proxy does not establish the resulting service effect. A plain converter or retained description may supply the needed operation more cheaply.

When reducing repeated procedural guidance, vary only the contribution intended to become unnecessary. Keep execution and current observations available. Test separately a stable mapping presented with all its needed inputs and a decision whose new interface fact was withheld. Their different repairs are worked below. Restore needed support rather than rewarding unsupported fluency.

**Bound repeated and episode-local updates.** Identify the state or parameters being changed, the qualified signal that permits an update, the experience retained, and the lifetime/reset rule. An episode-local adapter may be discarded at the end; durable shared parameters need a recoverable baseline and regression tests across later tasks. A runtime hidden state or learned memory token is not automatically either shared-parameter learning or an external text record. SYSE.52 prepares the exposed working representation, SYSE.43 maintains separately persisted episodes, and this Method governs selected parameter learning. Specialized backbone or latent-memory-module construction remains with its direct implementation.

Choose update extent and stop from applicable held-out behavior and the available means. Test older useful restraint and correct actions alongside the new target. Repeated self-generated failures are observations of failure; frequency does not turn them into positive labels. Reset, revert or return the unqualified signal when the update destroys earlier required behavior.

#### SYSE.45:4.4 - Compare the intended later use

Through SYSE.46, compare the trained candidate with the baseline under matched task and retained-support conditions. Read actual result, necessary access/use, restraint, protected effects and total effort separately. Adaptive validation selects candidates; an untouched final comparison supports the bounded reliance claim.

Test delayed or shifted use when the claimed benefit includes persistence or adaptation. Identify intervening model, memory, controller or source changes before attributing a difference to training. A policy that uses fewer tools while missing a newly changed fact fails that receiving use.

Retain, revise or reject the candidate according to the comparison. Return bad feedback to its supplier, unsupported transfer to the training question and runtime routing defects to SYSE.47. A learned predictor or auxiliary target retains its MMP/CMP meaning; correct predictions alone do not establish a useful acting policy.

### SYSE.45:5 - Archetypal Grounding


#### SYSE.45:5.1 - A converter, a learned interpretation and two failed withdrawals


A service accepts an interval in seconds. Target identity, revision and actual effect must be obtained through the current interface. For already structured input `duration_ms=12000`, a deterministic conversion returns `seconds=12`. Under the supplied conditions that small controller is adequate and cheaper to construct and qualify than an adapter. Stable recurrence alone supplies no reason to replace it.

Now change the target to interpreting recurring, varied requests such as “take three readings each minute” and “take one reading every twenty seconds.” Both call for `seconds=20` under the supplied meanings. The fixed converter still works after a supported structured duration exists, but it does not obtain that interpretation. Compare a phrase-rule parser, retained specialist/guidance support, and an adapter with the same converter, current interface and executor. In this constructed case, representative source examples establish that a small phrase rule leaves many intended forms unsupported; expanding and maintaining it has greater estimated whole-horizon burden than the offered bounded adapter trial, including target qualification, tests and failed-trial fallback. C.11 therefore selects that trial. If those grounds or training access are absent, use the supported parser/guidance way or obtain a worthwhile comparison premise.

Training histories include the request, applicable tool definition, current target/revision and the observations needed for a call. Targets vary phrases, rates, durations and identifiers. Missing-unit or ambiguous requests target clarification. The learner fits the intended interpretation/call, while the executor retains permission, actual-state binding and result checks. Optional semantic preparation and trajectory warm-up address different failures; any later reward must use qualified tool/argument meaning and protected results.

Two held-out failures discriminate what was lost when guidance was reduced. Inspect the candidate's proposed call before execution; the retained binding checks reject an unsupported call:

| Input and condition | Candidate output and observed defect | Supported repair |
| --- | --- | --- |
| `duration_ms=12000`; the applicable definition still says the argument is seconds, and current target/revision are present | `seconds=12000` instead of 12. The stable conversion is wrong despite sufficient inputs. | Retain the small converter or restore guidance; if learning that mapping remains worthwhile, repair its targets and test new values. Another current-state lookup cannot supply the missing transformation. |
| The provider changed to a millisecond argument, but the new definition was omitted from the input; the old call uses `seconds=12` | The call no longer matches the current interface. Restoring the fresh definition, with the same weights, yields the supported `duration_ms=12000` call. | Retain the required interface observation and repair its retrieval/input path. Training on old documentation cannot supply an unobserved future contract. |

Guidance reduction therefore tests a particular stable contribution, not all support. Untouched cases also include ambiguity, unsupported units and restraint after a lost reply. A delayed comparison must record intervening adapter, provider, controller and memory changes before attributing retained benefit.


#### SYSE.45:5.2 - Construct a corrected continuation from a recorded history


A recorded history H contains the permitted outcome-lookup operation, the original attempt A17, an acknowledgement followed by a lost reply, and the at-most-one-effect requirement. The recorded next action was an unsafe repeat of the mutation. An experience-informed teacher, using that failure and other qualified episodes, proposes `lookup_outcome(attempt=A17)`.

The engineer checks that H itself supplies the attempt identity, supported lookup and unresolved effect that warrant this correction. The student receives H without the teacher's extra experience; its action target is the lookup, not the old repeated mutation or the following observation. The old next observation remains evidence about the old action. To establish what the correction does, exercise that lookup in a new qualified test occurrence or use applicable environment evidence; relabelling the old observation would fabricate its consequence.

The training example fits only the corrected agent action. If H had lost A17 or the lookup contract, restore that input or target obtaining the missing contribution instead. A final success reward alone would not identify whether safe recovery or a lucky duplicate caused the result; the supplied intermediate attempt/effect state localizes the unsafe replay decision. A contrasting acknowledgement-without-effect case tests the feedback rule.

For a preference branch, the service owner may compare two factually supported reports and prefer one that exposes unresolved status before optional explanation. Record that owner, task and report pair with the judgement. Both reports must still meet the effect and factual requirements before the pair can support that preference target.

Untouched trials compare the trained policy with the baseline on new attempt identities, known and unknown outcomes, a missing lookup operation and earlier useful no-replay behavior. An episode-local update declares when the adapter resets; a durable update tests that older behavior after the new target is learned. The result is a candidate and bounded evidence, not an inferred successful deployment.

### SYSE.45:6 - Bias-Annotation

Training sources often favor tasks with cheap, automatically scored outcomes. A high reward can conceal poor currentness, unsupported actions or a narrow domain. Keep specialist criteria and the external contributions of the intended work visible throughout selection and qualification.

### SYSE.45:7 - Conformance Checklist

- The updated parameters/adapters, target behavior and baseline are identified.
- Retained support is part of the intended later configuration.
- Experience and feedback have qualified result meaning, including useful failures and restraint.
- The experience transformation and learning mechanism match the target and available feedback; corrected targets are warranted by the student's available history.
- Update lifetime, retained/reset state and regression checks are explicit where repeated learning is used.
- Construction, adaptive validation and final comparison remain distinguishable.
- Further-use evidence supports the stated change, or the candidate returns its qualification gap.

### SYSE.45:8 - Common Anti-Patterns and How to Avoid Them

**Train on every successful transcript.** Recover which actions and external contributions explain the success; exclude incidental answers and unsupported labels.

**Reward fewer calls.** Preserve actual task success and required fresh access. A necessary observation is not waste.

**Distil away the checker.** Transfer a demonstrated computation only at its warranted reach; separately needed evidence and authority remain external obligations.

### SYSE.45:9 - Consequences

The policy can make a stable contribution with less repeated guidance or deliberation. Training introduces data, computation, maintenance and regression costs. A retained tool, source lookup or human contribution may remain the better complete arrangement.

### SYSE.45:10 - Architectural Rationale

Changing parameters is a distinct development intervention. Separating it from memory and controller construction permits a fair comparison of means and a useful return when training is unavailable. The policy's later behavior is evaluated together with its retained execution arrangement because the task depends on both.

### SYSE.45:11 - SoTA-Echoing

The practice question is which stable contribution can be learned without losing necessary external support. [Tool-Internalized Reasoning, ACL 2026](https://aclanthology.org/2026.acl-long.2077.pdf), §§3.3–3.5, separates tool-semantics acquisition, trajectory warm-up and tool-reasoning optimization. This Method uses that distinction to diagnose what the learner must acquire; its specialized tokens and reward design remain optional direct implementations, and real-tool coverage and functionally equivalent tool labels limit the reported reach. [Skill0 v2](https://arxiv.org/html/2604.02268v2) supplies a guidance curriculum whose budget ultimately reaches zero, with execution retained. [SLIM v2](https://arxiv.org/pdf/2605.10923v2) offers contribution-based retention and retirement. The connected Reference application selects the actual intervention and rechecks the joint support after learning or removal.

[Sample-Efficient Learning from Agent Experience v1](https://arxiv.org/html/2607.21051v1), §3, supplies the teacher-at-recorded-history construction above. Its useful target can avoid new interaction during target production, while the recorded successor still belongs to the original action. Generated corrections require qualification; task-specific consolidation and cross-task transfer remain different evidence claims.

Adapt their selective target, rather than treating all tool dependence as a defect. Compare a fixed-model controller or retained guidance on the same whole-task cost basis. The exact learning algorithm and its evidence stay within the selected source edition; a changed interface or a failed untouched use reopens that reliance.

### SYSE.45:12 - Relations

E.23.CDI frames development for later work and E.10.LRN identifies the changed subject. CMP.7 supplies learner construction. SYSE.49 supplies missing qualified interaction experience; SYSE.46 supplies configuration and longitudinal comparisons. SYSE.42 preserves actual execution, SYSE.43 supplies retained context, and SYSE.47 supplies the separate controller intervention. MMP.8.SD/MMP.17 govern decision-model or surrogate targets when those are selected.

### SYSE.45:End
