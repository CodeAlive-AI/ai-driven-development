## CAD.1 - Derive a Control Decomposition from the Whole Problem

> **Type:** Method pattern
> **Status:** Stable

### CAD.1:1 - Problem frame

**Use this when** a control problem seems to call for different planning and reaction times, but “add a strategic, tactical and operational layer” does not tell you which decisions belong where. You may also have an inherited hierarchy whose purpose is no longer clear.

Start by writing one consequential behavior that the entire closed loop must produce, together with the available observations, actuators and execution limits. Then identify the decision that prevents a direct solution. The first useful result is a candidate split and an account of what its parts must jointly preserve.

If one qualified controller already meets the task and implementation constraints, retain it. Layering needs an identified benefit; it is not a requirement for accuracy or sophistication.

### CAD.1:2 - Problem

A hierarchy can divide a diagram while leaving the original difficulty untouched. A planner assumes commands can be realized, a tracker assumes commands change slowly, and neither assumption follows from the split. Conversely, trying to solve every decision at the fastest rate can make a good control formulation impossible to execute.

The design problem is to change the organization of decisions while retaining enough of their interactions to obtain the required behavior.

### CAD.1:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Long-horizon choice and rapid correction | A larger look-ahead can improve a plan while consuming time needed for reaction. |
| Simplification and lost interaction | An easier subproblem can omit actuator limits, memory or coupling that determines feasibility. |
| Local improvement and whole performance | A better isolated planner can issue commands that make the combined system worse. |
| Functional separation and realization | Different decision rates do not require different processors; shared processors introduce interference. |

### CAD.1:4 - Solution

#### CAD.1:4.1 - Formulate the unsplit question

State the controlled quantities, objective or preference, hard constraints, operating domain, relevant disturbances, measurements and available actions. Distinguish three time quantities: the dynamics and disturbance times, the horizon over which a choice matters, and the time needed to obtain and execute that choice. A fast update is useful only if observations, computation and actuation support it.

Use a centralized mathematical formulation when it helps reveal coupling, even if that formulation is too expensive to run. It can be a finite-horizon objective with dynamics and constraints, a reach-and-avoid problem, or a reference-following requirement. It is the common comparison basis, not a promise that one optimizer must solve everything.

Retain a feasible simple controller as a baseline where available. State what it cannot achieve at acceptable effort: for example obstacle look-ahead, preview-dependent economy or long-horizon allocation. If the baseline's actual limitation is unknown, test that uncertainty before adding layers.

When a qualified existing loop has adequate tracking and disturbance rejection but requested commands violate constraints, compare adding a reference or command governor before redesigning that loop. Use the joint plant-controller model, admissible initial conditions and qualified command-update rule described in [CAD.Reference:4.5.1](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands). Check whether the resulting command delay or distortion still meets the task. If it does, retain that candidate; if it does not, identify the unmet requirement that a different interface, planner or controller must address.

#### CAD.1:4.2 - Separate decisions because their information and effects differ

For each consequential decision, ask what it changes, which information it needs, how long its effect persists, how quickly a wrong choice becomes harmful, and what resources its computation consumes. Cluster decisions only when those answers support one useful calculation or law.

A slow planning decision might choose a route, reference segment or allocation. A faster decision might reject local disturbance or track that reference. This does not imply that the faster model is less detailed: a tracking model may retain actuator dynamics omitted by a planning model.

Generate materially different candidates. Compare a single loop, a planning-and-feedback split, or another separation motivated by the problem. Do not add a third layer merely because the source diagram contains three. A communication boundary can matter more than a time-scale boundary, and a faster processor can make a proposed split unnecessary.

#### CAD.1:4.3 - Expose what the split removes

A useful way to derive a candidate is to introduce separate variables for decisions that were coupled in the whole problem. Initially constrain them to agree. For example, let a planner choose a nominal trajectory z while the plant state is x; keep the relation that says what plant behavior z represents. Only then relax that relation to obtain separately solvable subproblems.

For each relaxation, recover its price. Replacing equality by tracking allows an error; removing full dynamics requires a realizability condition; replacing continuous interaction by periodic exchange introduces stale information and intersample evolution. Removing future disturbance information requires a prediction or uncertainty treatment. These are concrete missing relations, not a generic “integration risk”.

Use MMP.9 when reduction is involved: derive the retained evolution and identify terms depending on omitted state, past inputs or unresolved quantities. A term does not disappear because the upper model has fewer states. Decide whether it is retained through memory, bounded as mismatch, supplied by a lower closed loop, or left as an unresolved limitation.

The first candidate is complete enough to continue when every removed interaction has a proposed receiving treatment in CAD.2 or CAD.3. A treatment may fail; naming it does not establish it.

#### CAD.1:4.4 - Make the slow decision account for fast consequences

Do not optimize the slow part as if the faster part were free. Eliminate or approximate the fast response inside the slow objective when the model permits it.

For example, suppose a particular linear design starts at x = 0 and keeps x at zero by choosing a fast action f after observing w, while a slow action s remains fixed for a block. If the fast input matrix is invertible, the required correction is

$$
f=-B_f^{-1}(B_s s+w).
$$

Substitution gives a slow objective containing both the cost of s and the anticipated cost of these corrections. With a block of k forecast values, a possible norm-cost objective is

$$
k\|s\|_s+\sum_{i=1}^{k}\|B_f^{-1}(B_s s+\widehat w_i)\|_f.
$$

This is a derivation under a particular model, not a general recipe for plants with saturation or delay. When fast actions are limited, retain their feasibility condition as well as their cost. When an exact elimination is unavailable, use a qualified response model, a bound or joint optimization; label the remaining approximation and compare the actual combined result.

#### CAD.1:4.5 - Preserve the whole question through the next design move

Pass each candidate's controlled behavior, separation reason and lost interactions to CAD.2. A command's type alone is insufficient: a target position, a timed trajectory and a velocity segment imply different problems for the tracking layer.

Keep candidates comparable under the same task, disturbance class and resource limits. A slower update with a smaller demanded reference change may look better only because the task was weakened. Retain a whole alternative until its decisive incompatibility or disadvantage is understood.

### CAD.1:5 - Archetypal Grounding

A constructed actuator model is $x_{k+1}=x_k+u_k$, with $|x|\leq1$ and $|u|\leq0.06$. An existing fast law follows a reference. A planning calculation takes two fast sampling periods on a dedicated resource, so it cannot produce a new result every fast tick. Planning remains useful because it chooses future reference segments; the fast law supplies inexpensive execution.

One candidate sends a new held value every four ticks. Another sends a timed segment whose intermediate values the fast task can generate. They differ in the interaction removed by planning: the first assumes a jump can be tracked within the input limit; the second assumes a known continuous segment and a reliable clock. CAD.2 derives those consequences. Neither candidate has yet earned a safety claim.

As a non-use case, suppose the only task is stabilization around one fixed equilibrium and the existing fast law meets every limit. A slow planner adds no demonstrated decision benefit; keep the simpler controller.

### CAD.1:6 - Bias-Annotation

Organizational hierarchies and biological analogies make layered pictures persuasive. They do not determine a control decomposition. The linear example favors a tractable model; nonlinear or partially observed plants can require a different split and different assurance.

### CAD.1:7 - Conformance Checklist

- The unsplit behavior, constraints, information and resource conditions are recoverable.
- Each separation has a decision-specific reason and a serious alternative.
- Removed interactions have explicit receiving treatments or remain visible gaps.
- Slow choices include material fast consequences.
- The compared candidates serve the same demand.

### CAD.1:8 - Common Anti-Patterns and How to Avoid Them

“Slow is accurate; fast is inaccurate” merges optimization quality, model fidelity and tracking error. State the quantity and comparison. “Three layers are necessary” replaces construction with a diagram; derive only the separations the problem needs. A planner that ignores actuator feasibility hands its original problem to the tracker; retain that interaction in the next construction.

### CAD.1:9 - Consequences

The result is a smaller set of explainable architecture candidates. Some apparently attractive splits will be rejected before controller tuning. The cost is retaining the original problem long enough to compare whole behavior instead of judging each box independently.

### CAD.1:10 - Architectural Rationale

The method starts from coupled behavior because a decomposition is a change to that coupling. Introducing agreement before relaxing it makes the lost condition recoverable. This gives later error and feasibility work a specific obligation rather than an open-ended request to integrate components.

### CAD.1:11 - SoTA-Echoing

**When should the decisions be separated?** The selected line derives the split from the whole problem and keeps a qualified existing loop, with a governor if needed, and a single constrained controller as serious alternatives in :4.1–4.3. Separation earns its additional interface and assurance work when differences in information, prediction horizon or execution resources prevent those simpler arrangements from meeting the same demand. If a single MPC formulation can retain the relevant coupling and meet the deadline, decomposition still has to offer a gain that outweighs maintaining its interfaces.

The method adopts the problem-decomposition and coupling-relaxation move in [Matni, Ames and Doyle, §2.2](https://arxiv.org/html/2401.15185), while treating its particular layer arrangement as a choice. It adapts [Goel, Chen and Wierman's construction, §§II–IV](https://arxiv.org/html/1704.07785v2) in :4.4 to include fast consequences in the slow decision. That fixed two-rate, prediction-dependent cost result does not select a layer count or cover actuator limits. The corresponding price is explicit here: a split that saves computation still owes an error and feasibility construction.

A contemporary alternative is to keep the stabilized dynamics fixed and combine online optimization of references with a governor. [Nonhoff, Al Torshan and Müller, 2026 preprint, §§II–IV](https://arxiv.org/html/2601.23160v1) construct this combination for disturbed linear systems under strong convexity of the steady-state costs, compact convex constraints and their bounded-disturbance and initialization assumptions. Their performance statement concerns regret against varying optimal steady states; it is not a solution for arbitrary trajectory or mission objectives. Retain that alternative when changing costs, rather than preview-dependent motion, create the upper decision. The governor comparison in [CAD.Reference:4.5.1](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands) explains when the existing loop can remain.

Reopen the split when measured computation, required preview, available observations or permitted command distortion changes. A newly feasible single-loop or governor solution can remove the reason for a larger architecture; a missed task requirement can justify developing it.

### CAD.1:12 - Relations

C.39 supplies the general construction of a way to obtain a result; CAD.1 supplies the control-specific decomposition. MMP.9 supplies model reduction. CAD.2 consumes the selected candidate and makes its exchanges operational. CAD.4 compares whole candidates, including the unsplit alternative. SYSE.5 consumes the resulting functional organization when developing the engineered system.

### CAD.1:End
