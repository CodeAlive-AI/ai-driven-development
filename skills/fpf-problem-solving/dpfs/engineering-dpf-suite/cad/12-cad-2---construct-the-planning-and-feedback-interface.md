## CAD.2 - Construct the Planning and Feedback Interface

> **Type:** Method pattern
> **Status:** Stable

### CAD.2:1 - Problem frame

**Use this when** a planner and a lower controller have been chosen, but their combined behavior is not determined by their separate models. A reference jump, stale state estimate, model reset or held input may be the event that makes the connection fail.

Start with one command actually received by the lower computation: what quantity it represents, when it applies and how it becomes an actuator action. The first useful result is the connected evolution of plant, planning state and interface error, including the events between updates.

If a qualified interface already supplies this evolution under the current timing and command conditions, reuse it. A diagram or a matching data type is not that result.

### CAD.2:2 - Problem

Models can agree at one exchange instant while diverging between exchanges. A planning state can be initialized from the plant without representing every relevant plant state. A controller can track a smooth signal yet fail when the implemented interface replaces it by steps.

The interface must therefore be designed as behavior over time, not just as a list of variables.

### CAD.2:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Simpler planning state and hidden behavior | Projection removes quantities that can still affect control. |
| Sparse exchange and timely correction | Holding information saves work while increasing mismatch. |
| Reinitialization and continuity | A fresh estimate can improve planning while creating a command jump. |
| Convenient implementation and faithful semantics | Units, frames, clocks and interpolation can change the implemented law. |

### CAD.2:4 - Solution

#### CAD.2:4.1 - Define the exchanged behavior

Use MMP.18 to establish meanings, units, coordinate frames, observation times, validity intervals and the operation performed between messages. A target, an input, an output trajectory and a constraint are different commands. State which one the lower computation receives.

Choose how the upper model represents the lower behavior. For a planning state z and plant state x, a reconstruction $Pz$ can define an error $e=x-Pz$. A measured projection $z=\Pi x$ is a different map. Even if $\Pi P=I$, initializing $z=\Pi x$ leaves $e=(I-P\Pi)x$, which need not vanish.

If the controlled quantity is $y=Cx$ and the planner predicts $y_p=C_pz$, then

$$
y-y_p=Ce+(CP-C_p)z.
$$

Output agreement requires the second term to vanish or be included in the bound. State reconstruction, output matching and physical identity are separate questions.

#### CAD.2:4.2 - Derive the error instead of assuming tracking

For a useful linear branch, express both models at the fast sampling instants:

$$
x^+=Ax+Bu+w,\qquad z^+=A_pz+B_pv.
$$

Here w is an admitted bounded mismatch or disturbance, not a name for all unknown behavior. Select an interface law

$$
u=K(x-Pz)+Qz+Rv.
$$

Substitute $x=Pz+e$ before simplifying. The actual error equation is

$$
e^+=Fe+Hz+Gv+w,
\quad
F=A+BK,\quad H=AP+BQ-PA_p,\quad G=BR-PB_p.
$$

This calculation makes three design choices visible. K changes error correction; P and Q determine whether the nominal state evolution can match; R determines input matching. Solving $H=0$ is useful when possible but is not automatically possible or necessary. If it fails, retain $Hz$ and bound or redesign it. A stable F does not remove forced error from H, G or w.

Use MMP.9 to construct and qualify a reduced model before relying on it here. A fitted upper model with unexamined hidden-state memory is not made adequate by a convenient matrix dimension.

#### CAD.2:4.3 - Add the clock, held values and reset events

Specify the fast interval, slow update interval, which variables evolve between slow updates, and the event order at a shared instant: observation, computation, command acceptance and actuation. Derive the state just before and just after each event.

For example, if z and v are held for N fast steps, first derive the held-z mode by setting $A_p=I, B_p=0$ in the residual equation. With F, H and G for that mode, repeated substitution gives

$$
e_N=F^Ne_0+\sum_{i=0}^{N-1}F^i(Hz+Gv+w_{N-1-i}).
$$

When the next planning state is $z_{\mathrm{new}}$, the same physical x gives

$$
e_{\mathrm{new}}=e_N+P(z-z_{\mathrm{new}}).
$$

A reset is thus an error input, even when the tracker is stable. If the planner instead propagates z every fast step, use that evolution in :4.2; do not also treat z as held.

Model a known delay through the state and commands actually available to the controller. Replacing $x_k$ by $x_{k-d}$ changes the law; augmenting the state with the necessary history is one way to derive its dynamics. If an estimator supplies x, include estimation error and its qualification. A full-state result cannot simply be relabeled output feedback.

A variable delay or missed update needs an explicit admissible timing set and an error model covering it. A bound for one fixed period does not establish a bound for arbitrary switching among periods.

#### CAD.2:4.4 - Return an interface that can be tested and changed

Give CAD.3 the combined evolution, initial-error condition, admissible command class, mismatch class and exact moments at which each required constraint must hold. Retain the meaning and time convention of every exchanged quantity.

A failed error bound has several possible repairs: change the reconstruction, retain an omitted mode, alter feedforward, reduce command jumps, supply an interpolated segment, shorten latency or choose another split. The error equation identifies which change addresses the failure. Do not reflexively raise every update rate.

Test the actual exchange implementation with boundary events: simultaneous update, maximum permitted delay, reset, command reversal and missing command. These tests can falsify the model of the interface; they do not prove its physical assumptions.

### CAD.2:5 - Archetypal Grounding

#### CAD.2:5.1 - A held reference

For the constructed plant $x_{k+1}=x_k+u_k$, choose

$$
u_k=(1-a)(r_k-x_k),\qquad a=\tfrac12.
$$

With a held reference r, $e_{k+1}=ae_k$. Let the reference change by $\Delta r_j$ at the start of each N-step block. The error immediately after that change obeys

$$
e_{j+1,0}=a^Ne_{j,0}-\Delta r_j.
$$

For $|\Delta r_j|\leq\delta$, the interval $|e|\leq E$ is invariant at block starts if

$$
E\geq a^NE+\delta,\quad\text{hence}\quad E=\frac{\delta}{1-a^N}.
$$

It also bounds intermediate fast instants because $|a|\leq1$. The initialization condition is $|e_{0,0}|\leq E$. With $N=4,\delta=0.1$, $E=8/75$. The reference jump, not instability of the fast law, determines this worst-case envelope.

#### CAD.2:5.2 - A continuous reference segment

Now let the fast computation generate r from a timed segment and let $d_k=r_{k+1}-r_k$, with $|d_k|\leq v_{\max}$. The same plant and gain give

$$
e_{k+1}=ae_k-d_k,\qquad
E=\frac{v_{\max}}{1-a}.
$$

The planner can still update every four ticks. What changed is the command trajectory between updates. At $v_{\max}=0.05$, $E=0.1$. Segment endpoints must join continuously; an additional jump would add to d and invalidate the bound.

If a new segment is unavailable, holding the current reference gives $d=0$, which remains within this command class. This is an error-bound argument for that fallback, not evidence that holding position satisfies every mission requirement.

### CAD.2:6 - Bias-Annotation

A common output makes unlike models appear interchangeable. Check the mapping and missing dynamics. The linear branch makes exact substitution easy; nonlinear models need the same semantic work but may require set propagation or different Lyapunov constructions.

### CAD.2:7 - Conformance Checklist

- The command's meaning, applicability time and between-update behavior are explicit.
- Projection, reconstruction and controlled-output comparison are distinguished.
- Combined error dynamics include mismatch and every update or reset mode.
- The stated initial set and timing class match the implementation being considered.
- Estimation or delay is represented wherever the law uses it.

### CAD.2:8 - Common Anti-Patterns and How to Avoid Them

Matching array dimensions does not match quantities; recover their meanings and maps. Resetting the upper model does not reset the plant; derive the new error. Using a continuous reference in analysis and a held target in code changes the architecture; analyze the implemented exchange. Independent stability of two components does not establish stability of their connection.

### CAD.2:9 - Consequences

The interface becomes a design object whose consequences can be calculated and tested. A small change to interpolation or initialization may replace an expensive change to controller bandwidth. The cost is modeling events and time conventions that a block diagram suppresses.

### CAD.2:10 - Architectural Rationale

The reconstructed state provides a mathematical reference for comparing the planning model with plant behavior. Substitution exposes both the desired correspondence and the residual terms. Making update events part of the same evolution allows feasibility to be established for the connected system.

### CAD.2:11 - SoTA-Echoing

**Which relation between planning and realization is sufficient to use?** For the stated linear branch, the selected construction is an explicit state reconstruction and tracking interface, followed by residual and event equations. It adopts the tracking-law form used by [Stamouli, Tsiamis, Morari and Pappas, §3.2, Theorem 1](https://arxiv.org/html/2504.10461): feedback on the reconstructed-state error with nominal and input feedforward terms. The serious matching-model alternative is a discrete-time simulation-function construction; its usable output-distance guarantee still needs a verified invariant sublevel set, not only decrease outside it. Section :4.2 adapts the law by retaining nonzero nominal mismatch H and bounded w; :4.1 also retains the output-matching residual. These substitutions do not inherit the source theorem: CAD.3 derives the bound for the resulting equation.

This choice makes a failed exact match actionable, at the cost of bounding more forcing and possibly shrinking the usable command domain. If the existing closed-loop model already supports a governor, use that whole model as explained in [CAD.Reference:4.5.1](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands); adding a reduced planning model and P is unnecessary unless it supplies a useful decision or computational gain. The held-value and continuous-segment cases in :5 are constructed applications of the residual equation, not interchangeable implementations of one reference.

For partial observations, [Castroviejo-Fernandez and colleagues, §§3–6](https://arxiv.org/html/2401.02054v1) provide a developed alternative: state and disturbance estimation with time-dependent error bounds for reference governing. Adopt their requirement to carry observer error into constraint predictions when choosing that branch; its extra observer and set computations replace the full-state premise, not merely the notation x. Section :4.3 therefore returns an estimator-based implementation to the connected-dynamics derivation. Reopen the interface when its measured quantities, reconstruction, hold, interpolation, reset or delay changes; compare bounds and computation under the same actual exchange before choosing between these constructions.

### CAD.2:12 - Relations

CAD.1 supplies the decomposition and lost interactions. MMP.9 supplies a qualified reduction; MMP.18 supplies exchange and scale compatibility. CAD.3 consumes the derived error and timing modes. CAD.4 returns implementation changes that require this derivation to be reopened. C.30.LCA can then test whether a control-structure view exposes the relations that the construction actually uses.

CAD.5:4.7 supplies the estimate-based version of the interface when exact state is unavailable. It derives the additional forcing from estimation error; the observation model and timing must describe the same implemented loop.

### CAD.2:End
