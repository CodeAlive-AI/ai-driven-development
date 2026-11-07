## SYSE.47 - Construct and Revise an Agent's Execution Procedure

> **Type:** Method pattern
> **Status:** Stable

### SYSE.47:1 - Problem frame

**Use this when** a person or technical agent needs a practicable procedure connecting available operations, or an existing procedure repeatedly fails to use their results. A person can lose a carry between steps; an agent can retrieve the right rule again instead of acting on it. Start with the required result and the trace of the failed connection.

The subject is the operative sequence and its conditions for progress, recovery and stop. It may be a written procedure enacted by a person, a supervised sequence or a software controller that prepares requests and consumes returns. Its first result is a performable candidate with a bounded comparison, retained conditions and a usable failure return.

Keep an adequate simple procedure. A person supervising a short model/tool loop may already supply the needed control. Do not construct a larger workflow merely because several steps can be named. A missing domain operation, unknown success predicate or unsupported permission cannot be repaired by adding controller branches.

### SYSE.47:2 - Problem

Available knowledge, tools and performer ability do not themselves connect the steps. The next action needs the right contribution in usable form, and the procedure must distinguish a supplied premise from an unresolved one. Instructions to “check and continue” are ineffective when the executor permits repetition, loses uncertain effects or accepts the model's claim of completion without the required observation.

### SYSE.47:3 - Forces

Explicit control makes consequential conditions observable but adds complexity. Flexible generation can find useful continuations while producing unsupported proposals. More context can expose needed evidence or obscure it. A narrow state machine can be dependable for its task yet fail on a changed task. Cheap repetition may still exhaust the time needed for the actual action.

### SYSE.47:4 - Solution

#### SYSE.47:4.1 - Recover the task and the permitted construction

Recover the required result, supplied domain operations, actual interface conditions and observable evidence of completion. For a repair, inspect a representative trajectory: what contribution was needed, what arrived, how it entered the next action, and where progress stopped. Distinguish a bad continuation from a missing or false return.

Choose the actual performer and implementation: written instructions with usable observations, a supervised sequence, or executable transitions. Establish who can inspect each condition and perform each operation. The procedure connects supplied operations; it cannot create missing arithmetic, domain judgement or bodily ability by naming another step. SYSE.52 constructs the actual next input and tool view; consume its selected evidence, provenance and reconstruction triggers rather than treating context assembly as an unexplained transition. Persisted memory construction belongs to SYSE.43; model parameter or adapter training to SYSE.45; a reusable operator to SYSE.48. One intervention can consume their results without claiming to perform them.

Compare the proposed procedure with the incumbent and other feasible arrangements that could meet the task, including a simpler one when available. State which task, performer conditions, contracts and supports the comparison preserves; include model/settings when an LLM is used. If the missing result meaning is outside the engineer's knowledge, obtain it through SYSE.9 before implementing a predicate that depends on it.

#### SYSE.47:4.2 - Build the steps and their usable inputs

For each necessary step, specify its required evidence, generated proposal if any, allowed external action, and the return that enables further work. Use the supplied human or deterministic operation directly where it suffices. Give a model call the current task, relevant qualified contributions and a tool view containing supported operations with their actual argument and effect semantics.

Select evidence for its next use. Retain source, subject, time or edition and applicability where those distinctions affect the decision. Keep governing instructions separate from retrieved content; a document or tool response supplies data, not permission to rewrite the task. A compact summary must preserve the qualification on which the next action relies. Use SYSE.52 when that selection, compression or tool view needs construction. Pass it the receiving step and actual per-attempt state, consume the resulting input, and preserve its raw-evidence return and recovery operations.

Use per-attempt state only where a transition needs it: outstanding premises, supplied contributions, current target observations, unresolved execution attempts and remaining budget. Such state is not automatically cross-task memory. Invoke SYSE.43 or SYSE.44 only when retained context or divided contributions are actually needed.

#### SYSE.47:4.3 - Implement observable continuations

Connect the steps using predicates grounded in the task and interface. When assistance selection is unsettled, obtain SYSE.50's performer- and access-relative rule: the signal it consumes, the response it selects, its applicability and fallback. Implement that rule without treating confidence as a current fact, permission or resolved effect. A required fresh observation can use a direct rule without a calibrated estimator.

The following distinctions commonly matter; select those that can change this procedure.

| Observed condition | Continuation to implement |
| --- | --- |
| A qualified contribution supplies the needed premise | Record it as supplied and pass its usable result to the dependent action. |
| A premise is missing, contradicted or no longer applicable | Open the specific lookup or bounded request that can supply it; retain the reason for reopening. |
| The same query would repeat with the same relevant evidence and no justified refresh | Return the unresolved premise or select a different supported move; do not spend the entire budget rediscovering the same result. |
| A proposal has malformed or unsupported arguments | Return the binding defect through SYSE.42 before execution. |
| An invocation may have effects but its response is missing | Preserve the attempt identity and enter SYSE.26 recovery through SYSE.42 before any replay. |
| The actual completion predicate is satisfied | Return the observed result in a form the receiver can use. |
| Budget is exhausted or no permitted useful continuation remains | Return the unfinished condition and recoverable state; do not label the task complete. |

When further reasoning or tool work needs adaptive allocation, consume SYSE.51's rule before another calculation, source inspection, sample, branch or model call. Pass it the actual intermediate result and remaining resources; enforce its completion reserve and sufficient-result stop. A cap alone does not choose a useful move before exhaustion.

Put consequential limits in the actual controlling means. For software, enforce the permitted tool set, attempt budget and uncertain-effect branch outside model-generated narrative. A human procedure requires usable cues and feasible checking; a written instruction alone does not guarantee that the person performs it. Use SYSE.26–SYSE.28 for applicable platform interaction, interface and control questions, and SYSE.40 for software capacity and retry limits.

Implement the chosen transitions in their supported form: a usable written sequence, supervised enactment, code or workflow definition. Connect actual inputs and returns, including failure paths, then exercise that implementation.

#### SYSE.47:4.4 - Bind predictions without substituting them for observations

When the next action needs a prediction, obtain its model and qualified response through MMP.8.SD, MMP.17 and SYSE.10. Bind the response to the current action, horizon, source conditions and error limit. A.15.7/C.11 use the prediction for choice; SYSE.42 obtains any required actual effect and subsequent observation.

If the current state, model premise or error bound is defeated, return to the named model or observation supplier. Do not invent dynamics in the controller or promote a predicted state into an observed result.

#### SYSE.47:4.5 - Exercise the candidate and retain only useful control

Use SYSE.46 to compare the candidate with its baseline on representative tasks. Include an adequate contribution, a missing premise, changed relevant information and an uncertain effect when those branches are relied on. Use SYSE.49 when informative conditions must be constructed.

Inspect receiving-result correctness, needed access/use, restraint, unresolved effects and total effort. Keep final comparison cases outside procedure tuning. Compare delayed use when persistence is claimed and changed-condition use when transfer is claimed, retaining configuration and support identity.

Retain a procedure that meets the required result at a justified total burden. Return a false sufficiency test to its predicate owner, failed execution to SYSE.42, and misleading feedback to SYSE.49. A more elaborate procedure with no useful advantage should be simplified or rejected. Stop at the bounded executable result or its unresolved construction condition.

### SYSE.47:5 - Archetypal Grounding


#### SYSE.47:5.1 - Connect supplied arithmetic, recording and checking


A person repeatedly loses carries when resuming short multiplications for a stock report. The target includes the exact product and a recoverable intermediate record. Arithmetic operations and an adequate column worksheet are already supplied; the missing construction is a sequence that preserves and uses their returns. Ordinary uninterrupted mental work remains the simpler way when those conditions do not call for the new procedure.

Construct the sequence: bind the expression to the stock task; place the digits in the supplied columns; after each digit operation write its result digit and carry into their next-use positions; resume from the recorded position; check and report the product. For 347 × 6, the person writes units 2 and carry 4 after 7 × 6 = 42, then tens 8 and carry 2 after 4 × 6 + 4 = 28, and obtains 20 from 3 × 6 + 2. The record and report give 2082.

Add the actual recovery: if a carry's position is lost, retrieve the intact record under SYSE.43 or recompute that bounded preceding operation before continuing. SYSE.52 prepares a readable view of the layout and available writing means. If a calculator is the selected aid, SYSE.42 checks its entered expression and uses the display; an incorrect 374 × 6 entry returns to binding, not the next arithmetic step. Stop when the required record and reported product are usable.

Exercise the written procedure through an interruption and a deliberately misplaced carry. Compare recovery and total burden with the incumbent. A recurring assistance-choice defect can consume a rule from SYSE.50; a choice about further checking can consume SYSE.51 while preserving time to report. Those constructors are unnecessary when the short supplied rules already suffice. The result is a usable sequence with bounded performance evidence, not an assertion of acquired unaided skill.


#### SYSE.47:5.2 - Repair a fixed-model controller that ignores a usable return


One engineering agent repeatedly retrieves an applicable maintenance procedure until its budget expires. The trace shows that the controller never records the returned rule as supplying the outstanding premise. The engineer can change the external controller, but cannot train the model.

The repair adds per-attempt state and routing. A procedure return includes its source edition and applicability. When it supplies the outstanding rule, the controller marks that premise supplied and places its result in the existing action step's input. A subsequent identical lookup requires a missing or defeated premise, or a justified refresh. Otherwise the procedure continues to the required current-target observation.

The model endpoint/settings, instruction templates, tool contracts, permissions and persistent memory policy/store stay fixed. Selected prompt inputs change because the controller now passes the usable return forward. This is an execution change, not parameter learning or a new memory policy.

The candidate must still reopen the premise when a new procedure edition changes a precondition. It must also preserve an unresolved effect across a lost reply. Compare ordinary progress, missing information, the changed edition and the interrupted effect under SYSE.46. A successful repair reduces redundant retrieval while preserving necessary fresh access and actual execution. This constructed example specifies observations to obtain; it claims no measured improvement.

### SYSE.47:6 - Bias-Annotation

A controller designer can mistake the successful trace's incidental order for the only valid route. A fixed benchmark can reward a memorized branch. Preserve alternative successful continuations and challenge predicates with a changed premise, not just another wording of the familiar task.

### SYSE.47:7 - Conformance Checklist

- Task meaning, supported operations and observable completion come from qualified suppliers.
- Each step has usable inputs, allowed actions and consumed returns.
- Parameter, persistent-memory and execution changes remain distinguishable.
- Missing evidence, malformed proposals, uncertain effects and completion lead to appropriate continuations.
- Consequential limits and observations are implemented by the actual executor or practicable human control; their performance is tested.
- The candidate is executable and compared with a feasible baseline.
- Failed conditions return to their suppliers without concealing useful partial results.

### SYSE.47:8 - Common Anti-Patterns and How to Avoid Them

**Add “think again” after every failure.** Recover the missing contribution or transition and implement a continuation that can change it.

**Treat every tool return as progress.** Test whether it supplies the premise the next action actually needs.

**Encode an invented success rule.** Obtain domain acceptance meaning; syntactic completion or an agent's declaration cannot replace it.

### SYSE.47:9 - Consequences

An available contribution can enter actual work, and recurring failures become localizable. Explicit transitions and observations add implementation and maintenance cost. The result remains bounded by the supported task, predicates and external operations; it does not supply every skill used within that task.

### SYSE.47:10 - Architectural Rationale

The procedure connects operations into actual progress. A person can have the needed arithmetic and aid yet lose their result between steps; a fixed model can succeed or fail with different surrounding control. Separating proposals, effects and usable returns makes that intervention testable. Preserving the domain and interface suppliers prevents the controller from silently defining its own task and success.

### SYSE.47:11 - SoTA-Echoing

For the technical realization, [AFlow v2](https://arxiv.org/html/2410.10762v2) supplies one optional construction mechanism: search over executable prompt/code workflows with fixed model parameters. Its answer-task evaluations do not qualify state-changing effects. The [simple supervised loop](https://www.anthropic.com/engineering/building-effective-agents) is a feasible comparison option when it supplies the required control.

Select workflow search only when its construction cost is justified. The retained line is task-grounded executable control with an independent comparison; manual construction can supply it. Reopen the procedure when task semantics, tool behavior or the evidence required for a transition changes.

### SYSE.47:12 - Relations

SYSE.25 diagnoses the failed continuation in a platform path. SYSE.9 obtains missing subject results. Use SYSE.26–SYSE.28 for applicable platform interaction, interface and control questions, and SYSE.40 for software capacity and retry limits. SYSE.42 executes calls, SYSE.43 supplies memory, SYSE.44 supplies divided contributions, and SYSE.48 supplies reusable operators. SYSE.49 constructs missing experience and SYSE.46 tests the configuration. MMP.8.SD/MMP.17 supply qualified predictive contributions. Use SYSE.45 when parameter learning is selected. SYSE.50 constructs the assistance rule and SYSE.51 the adaptive effort rule that this procedure implements. SYSE.52 constructs the actual next input and tool view; the procedure keeps these distinct from its own per-attempt state.

### SYSE.47:End
