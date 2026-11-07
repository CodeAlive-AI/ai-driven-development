## CAD.Reference:4 - The layered planning-and-feedback branch

This branch applies when separate planning and feedback decisions are worth considering. Its exact-state construction remains useful when the state is actually available. The estimate-based connection is in CAD.5:4.7 and CAD.Reference:3; use it wherever the implemented law acts on an estimate. The following sections develop the reasons, quantities, alternatives and returns within the layered branch.

### CAD.Reference:4.1 - The recurring whole problem

A layered control architecture divides decisions while controlling one connected behavior. The division is useful when it lets different calculations use appropriate information, horizons and execution resources. It becomes harmful when each calculation relies on a behavior that the others do not supply.

The difficult question is therefore not just which operation follows another. It is whether the chosen decomposition, models, command meanings, error bounds, feasible commands and execution arrangement can all be true of the same closed loop. A later result can change an earlier design premise. The four Methods are separately usable because these questions arise independently; their results must still agree wherever one receives another.

**Extended reminder.** A useful control split preserves the whole task by making its lost interactions explicit. The exchanged command and its timing determine the error that the lower behavior must contain; the containment consumes state clearance and actuator authority, so it limits what the upper decision may request. Those limits reshape the useful model, horizon and decomposition, while the resources needed to compute and execute them change timing again. Compare and realize this connected choice under one demand, and return a changed condition to the premise it invalidates.

### CAD.Reference:4.2 - Why these four contributions belong together

CAD.1 answers a functional design question: which decisions should become distinct and why? Its result determines which interactions are no longer solved together. A long-horizon optimizer and a fast feedback law are useful only if their separation addresses a real difficulty, such as calculation time or unequal access to information.

CAD.2 answers a modeling and realization question: what behavior does that separation actually produce? It turns a selected command into an exchange with units, time, interpolation, feedback and reset semantics, then derives the joint evolution. This can reveal that a presumed “same reference” is a different signal after implementation. The result constrains the decomposition: an upper model that cannot be related to the lower dynamics under useful conditions is a reason to retain more state, change the command or abandon that split.

CAD.3 answers a feasibility question: which behaviors can be requested without contradicting the conditions of their realization? Error is not merely a quality score. It consumes physical clearance and correction authority. A command envelope that makes the bound large can leave no useful actuation range; a smaller envelope can restore feasibility but prevent the required task. This result therefore constrains both the interface and the original functional choice. It also distinguishes a possible next action from a domain in which operation can continue.

CAD.4 answers a whole engineering choice: which mutually consistent configuration is worth realizing under the actual demand and resources? It compares the outputs of the other Methods, but it also changes their inputs. A different processor, horizon, model order or scheduling arrangement changes what can be computed on time and therefore which error dynamics and command domain are relevant.

The relation is not that every engineer must perform these Methods in this textual order. The relation is that a claim used by another part must be available with the conditions that make it useful. An inherited result can supply it. A changed condition can withdraw it. A missing result can block one architecture while leaving another usable.

### CAD.Reference:4.3 - Connect dynamics, decisions and computation by their actual quantities

The common quantities make the reasoning inspectable. The task sets a demanded progression, cost or reachability condition. A candidate command class S says what the planner may send. The interface yields an error evolution, such as $e^+=Fe+Hz+Gv+w$. S and the mismatch domain bound its forcing. An invariant E bounds the difference between nominal and realized behavior. The inclusions $Pz+E\subseteq X$ and $Qz+Rv+KE\subseteq U$ then restrict S. These are the exact-state formulas. When feedback uses an estimate, CAD.5:4.7 adds estimation error to both the forcing and the input allowance.

These are mutually constraining statements, not independent labels. Enlarging S can enlarge E, which can make the proposed S inadmissible. Reducing E by changing a gain can increase the size of KE and consume more actuator authority. Reducing the planning model can shorten computation while increasing H or the mismatch set. A longer update interval can fit the computation and enlarge the change the tracker must absorb. A bigger model can remove an important residual but leave no time to use the result.

Thus “more accurate”, “faster” and “more robust” are incomplete comparisons until their quantities and costs are named. A more accurate nominal prediction does not imply a smaller implemented error if it arrives late. A smaller tracking error does not imply a better task result if the permitted command range becomes too small. A feasible computation does not imply safe execution if its output is applied at the wrong instant.

The mathematical construction does not eliminate the engineering choice. It makes the choice explicit: accept a smaller envelope, change an interface, spend more computation, use another sensor or actuator, or revise an impossible requirement. SYSE.6 remains the place for that larger system decision.

### CAD.Reference:4.4 - Reuse the external foundations without losing the subject transition

C.39 supplies the reasoning from a needed result back to necessary operations and forward through their joins. Here that reasoning asks whether the result called “a feasible controller” includes a realizable command, its timing and a continued path, rather than stopping at the existence of a feedback gain.

MMP.9 supplies the account of what model reduction removes. CAD.1 and CAD.2 consume that account at a specific control decision: does the missing state create memory or forcing that the planner must retain or the tracker must absorb? Calling the lower loop “fast” does not establish that its omitted dynamics are negligible.

MMP.18 supplies the general construction of compatible exchanges and scales. CAD.2 fills its control-specific content: which signal is held, which state is propagated, what resets, and how a reference change enters the error. A well-typed exchange still needs this behavior.

MMP.22 supplies the transformation from mathematical operations to workable performance. CAD.4 consumes it when choosing what to precompute, what data are available at the deadline, what resource is shared and which result can actually arrive. The computation is part of realizing the selected control behavior; successful algebra alone does not enact it.

C.30.LCA then helps describe the resulting control structure adequately. It can expose an unrepresented latency or lower guarantee. It does not establish the guarantee's truth. Conversely, a valid error calculation does not ensure that a view shows the assumptions needed by the next engineer.

These foundations remain useful outside control engineering. The subject contribution here is their specific connection to control decisions, error dynamics, admissible commands and execution.

### CAD.Reference:4.5 - Several legitimate entries and their returns

An engineer replacing a communication interface can start at CAD.2. Preserve the task, qualified model and existing controller law if they remain unchanged. Derive what the new delay or interpolation does to their connection, then return only the affected error and command assumptions to CAD.3. If the new interface cannot support any useful domain, the change reaches CAD.1 or the system architecture decision.

An engineer asked to increase speed can start at CAD.3. Hold the implementation and model fixed while testing the enlarged command class. If correction authority is exhausted, CAD.2 can investigate a continuous segment instead of a larger jump. CAD.4 compares that repair with a changed gain, faster planner or different plant arrangement. The order follows the uncertainty that matters, not a mandatory restart.

An engineer moving the same software onto shared computing hardware starts at CAD.4. A model of independent task execution is no longer the implementation premise. Establish the shared scheduling and communication behavior; if it changes the admitted timing, return that timing to CAD.2. A new hardware name alone does not require every control theorem to be reproved, but an unbounded delay removes the old timing-dependent conclusion.

An engineer with a simple controller already meeting the requirement can stop before any of these expansions. A framework that always recommends more layers has lost its baseline. Conversely, a proven lower law does not justify stopping when the upper layer can issue commands outside its qualified envelope.

#### CAD.Reference:4.5.1 - Keep a qualified loop and govern its commands

When an existing loop already tracks and rejects disturbances adequately, but abrupt or excessive commands violate constraints, command admission can be the remaining problem. [Garone, Di Cairano and Kolmanovsky's survey, §2.1 and §6.1](https://merl.com/publications/docs/TR2016-102.pdf) develops reference and command governors as additions before a stabilized loop. They modify commands using the current closed-loop state and predicted constraint admissibility, rather than merely applying a fixed low-pass filter.

For the basic held-command construction, use a model whose state includes the plant and controller. Obtain a set of state-command pairs from which holding the selected command satisfies the constraints at all claimed future instants. A scalar reference governor selects the largest admitted step along the line from the previous command toward the desired one; a command governor can optimize the command vector. The previous command supplies continuation only under the construction's admissibility and initialization conditions. Scalar search is smaller, while the restricted search direction can sacrifice response.

This is a candidate within the control architecture question, not an opposing field. It can preserve a qualified lower controller and avoid introducing a reduced planning model. Compare its reference distortion, progress and computation with the required task. If filtering makes the requested arrival time unattainable, constraint satisfaction alone has not solved that task. If the lower controller, sensor or timing changes, its governor model and admissible sets must change with it.

Later constructions change different premises: observer-dependent domains in CAD.2–CAD.3, online cost adaptation in CAD.1, and inexact computation or controller switching in CAD.4. Use those developments only with their corresponding models and conditions.

### CAD.Reference:4.6 - Worked joint revision

The running example begins with two different concerns: a planner needs two fast ticks of computation, while an inexpensive feedback law runs every tick. CAD.1 makes the reason for separation explicit. The separation does not yet decide the command: a held target and a timed segment remain alternatives.

CAD.2 derives how their meanings change the error. A held target creates a boundary jump; a joined segment supplies bounded increments at every fast tick. CAD.3 turns that difference into actuator reserve. At the doubled demand, the four-tick held target has a direct violating first input; the joined-segment command has a sufficient input bound of 0.05 under the toy model. Its limited reference interval also has an explicit continuation by holding the reference.

CAD.4 returns the result to the practical choice. The segment design fits the declared computation arrangement but requires a clocked generator, continuity at handover and an admitted initial error. The engineer cannot keep only its attractive input number and omit that realization. If physical actuation is later found to be delayed, the error derivation changes and the bound must be reopened. The reason for separating planning from feedback can remain useful even while that specific realization fails.

During the calculation of an error margin, the immediate mathematical work contributes to constructing a command domain, which contributes to choosing a viable control architecture, which contributes to the engineered system's required behavior. A changed whole requirement alters what counts as a useful local margin. This connection explains why a numerically correct sub-result can still fail to resolve the engineering problem.

### CAD.Reference:4.7 - Recognition, assurance and the cost of the arrangement

A layered diagram recognizes a candidate organization. A plausible trace recognizes a candidate behavior. Mathematical invariance establishes a conditional property; a real model, disturbance envelope and execution arrangement must support its premises before physical reliance. These are different results, and the full use needs whichever the intended claim actually consumes.

The primary trade-off is between cheaper or more specialized local decisions and the burden of maintaining their coupling. The arrangement earns its cost when separate decisions remain useful and their conditions can be made compatible. A direct controller or direct existing Method remains preferable when it already serves the task.

A whole-use inspection therefore asks whether the selected split has a useful reason, whether the derived exchange is the one realized, whether its command/error dependence closes, whether continuation and performance are distinguished, and whether implementation conditions fit. These questions use the full constructions of CAD.1–CAD.4.

### CAD.Reference:4.8 - Source boundaries, bias and future change

The constructions compared in the patterns answer different quantitative questions. The reader should not assemble their conclusions into a theorem that none states. The cost-elimination branch, sampled linear margins, continuous error-based safety transfer, reference governing and a specific two-layer co-design each retain their own models and qualifications. The direct derivations and explicit returns here make a first use possible without claiming complete coverage of control engineering.

The running linear case makes computations transparent but can bias intuition toward easy matching, full-state access and deterministic timing. Its general lesson is to derive and reconnect the consequences of a split. Its numerical margins, feasible domain and fallback remain local to the stated model.

When a source revises a relied-on condition, reopen that condition and its consumers. When a physical model or execution fact changes, reopen the claims that use it even if no source publication changed. A new paper can improve a method; a failed application can expose a missing family of problems. Either can justify revising the framework's scope, while an unchanged adequate supplier remains available.
