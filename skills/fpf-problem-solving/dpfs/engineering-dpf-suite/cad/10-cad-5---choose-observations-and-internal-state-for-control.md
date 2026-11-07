## CAD.5 - Choose Observations and Internal State for Control

> **Type:** Method pattern
> **Status:** Stable

### CAD.5:1 - Problem frame

**Use this when** an engineered controller has to act before a complete, accurate observation is available. A rapid channel may reveal only part of the situation; a more complete channel may describe an earlier state. You need to choose the channels and their timing, determine what the controller must remember or predict, and establish what control those arrangements can support.

For example, an inspection result can arrive after two control updates while a simpler sensor reports one critical quantity immediately. Adding both sensors is not yet a solution: the controller must relate their observations to the same evolving system, account for actions already performed, and retain uncertainty about unobserved disturbances.

This is a specialized method for **sampled linear control with bounded uncertainty**. It constructs a sufficient information arrangement for a specified control task and a given state-feedback law or a finite set of such laws. It also supplies a stronger negative result when indistinguishable situations require incompatible actions. It does not synthesize arbitrary nonlinear controllers, identify an unknown plant, or infer biological mechanisms from a control analogy.

The intended practitioner can use state-space models, bounded sets and feedback laws. Start with the required controlled quantities, admissible state and input sets, operating horizon, a usable plant model, and realizable sensor and execution alternatives. The first useful result is a comparison that connects **available information → one executable action → the required continuation**, with the internal state and update needed to maintain that connection.

Retain a simpler qualified arrangement when it already works. A current complete observation can remove the need to reconstruct a delayed state. An unobserved but sufficiently bounded component can remove the need for a sensor. If the only question is whether a diagram represents an already constructed control structure adequately, use C.30.LCA.

### CAD.5:2 - Problem

An accurate observation of the past is not an accurate observation of the present. Between sampling and acting, the plant has evolved under known commands and unknown disturbances. Combining the latest values from several channels can therefore create a state that never existed. A point estimate can also hide alternatives that demand different actions.

Choosing the smallest estimation error does not by itself solve the control problem. Error in a harmless direction may cost more to remove than error in a direction that exhausts an actuator margin. Conversely, a low average error can coexist with an unacceptable possible trajectory.

The design problem is to obtain enough timely information for the required action and continuation, at an acceptable sensing, communication, memory and computation cost. Neither maximum observation nor minimum memory is the goal by itself.

### CAD.5:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Freshness and completeness | A rapid partial observation may constrain the next action more usefully than a delayed complete one; neither dominates without a plant and a task. |
| Prediction and unobserved disturbance | Known actions allow a past observation to be propagated, but prediction cannot reconstruct disturbances that no available channel distinguishes. |
| Compact internal state and retained dependence | A small representation is cheaper; discarding correlation, sample time or applied-input history can invalidate its next update. |
| Estimation and control | A sensor can improve estimation while leaving the limiting action unchanged. A smaller error bound can enlarge the set of feasible commands. |
| Rigorous bounds and execution cost | Exact feasible sets can be expensive. An outer approximation is usable if its additional uncertainty still permits control before the deadline. |
| A chosen realization and architectural necessity | Removing one internal path tests that realization. It does not establish that every controller without that path fails. |

### CAD.5:4 - Solution

Construct the possible current states from the information actually available at the action time. Determine whether **one action**, chosen with that information, works for all those states and admits the required continuation. Use failures of that construction to change the observation, its timing, the internal representation or the control demand. Compare complete alternatives under the same demand.

#### CAD.5:4.1 - Fix the action time and the control-relevant distinctions

Use the sampled plant model

$$
x_{k+1}=A x_k+B u^a_k+w_k,\qquad w_k\in W,\qquad x_0\in X_0.
$$

Here \(u^a_k\) is the input actually applied during the update, not merely the requested command. Specify state or output constraints, input limits and the duration for which they must hold. The discrete guarantee covers sample instants; physical constraints between samples require a qualified intersample model and bound. A tracking problem can use deviation coordinates about a known reference; changes of that reference must remain in the model.

For the direct construction below, \(A,B,W,X_0\) are known, \(W\) and \(X_0\) are bounded, and the executed input is available to the estimator. Known actuator queues can first be included in the plant state. Unknown actuation error must be bounded and included in the model; an unbounded discrepancy between requested and applied input defeats the stated guarantee.

State what is available **before** selecting \(u_k\). A packet that arrives after that selection cannot support that action. Include sampling phase, transmission, computation and actuation timing in this account. Specify a maximum age of usable observations and a maximum gap between required samples: a delivery-delay bound alone does not guarantee that a sensor samples often enough.

Ask which possible situations the controller must distinguish. If two situations consistent with all available information require disjoint admissible action sets, no deterministic causal controller using only that information can meet the requirement for both. Conversely, do not demand that every state coordinate be accurately observed if their remaining differences do not prevent an acceptable action and continuation.

Begin with the least elaborate plausible arrangement. Include a qualified current sensor, a fixed observer already meeting the task, or no observation of a harmless stable component. These are substantive alternatives, not merely baselines to be defeated.

#### CAD.5:4.2 - Form realizable observation and timing alternatives

For each offered channel \(j\), specify its observed quantity \(C_jx\), error model, sampling rule, delivery rule and resource demand. For a nonsaturating bounded-error channel, a packet contains

$$
(j,\tau,y),\qquad y=C_jx_\tau+v,\qquad v\in V_j,
$$

where \(\tau\) is the sample time and \(k-\tau\) is its age when used. The channel's constraint on the sampled state is the set

$$
M(j,\tau,y)=\{x_\tau:y-C_jx_\tau\in V_j\}.
$$

A quantized symbol instead denotes its whole quantizer cell, including the noise bound. A saturated extreme cell may be unbounded; do not replace it with a small symmetric error interval. For adaptive thresholds, retain or communicate the thresholds used for that particular sample.

Construct a finite set of feasible channel-and-schedule alternatives. Include the resource coupling that can change their timing: two sensors sharing a bus, for example, need not retain their isolated delivery bounds. State which loss and delay combinations are allowed. A fixed periodic schedule or an explicitly bounded family of allowed modes supplies timing conditions for the error calculation. The number of cases and the cost of set propagation still have to fit the design and execution effort. Arbitrary online sensing policies require a separate policy construction.

A rapid narrow channel, a slow complete channel and their combination are useful candidates when the problem suggests them. They are not compulsory categories. Future-disturbance preview is different from a delayed observation of the current plant; give it its own prediction model rather than treating its timestamp as negative measurement delay.

Do not assume a universal law exchanging accuracy for speed. Obtain that relation from the proposed device, encoding, bandwidth, energy or other physical constraint. If a fast complete channel fits the same total budget, it may remove the reason for a heterogeneous arrangement.

#### CAD.5:4.3 - Construct an internal state that can be updated

Let \(D\) be the largest allowed measurement age. A general sufficient representation retains the compatible joint set of recent states

$$
\xi_k=(x_k,x_{k-1},\ldots,x_{k-D}),\qquad \xi_k\in\Xi_k,
$$

together with the applied-input history, sample identities and the schedule or arrival mode needed for subsequent updates. At startup retain only states at nonnegative times and use \(X_0\); do not invent a prehistory. The set \(\Xi_k\) represents states compatible with the initial condition, model, applied inputs and all observations already incorporated.

Predict the joint set by the map

$$
T(\xi_k,u^a_k,w_k)
 =(A x_k+B u^a_k+w_k,\;x_k,\ldots,x_{k-D+1}).
$$

For a packet arriving at the next action time, intersect this predicted set with the measurement constraint on its **historical component** \(x_\tau\). With several packets, intersect all their valid constraints. The projection onto the first component gives the possible current states \(X_k=\pi_0\Xi_k\).

This is a constructive sufficient internal state, not a claim of minimum order. It preserves the correlation between a past observation and the present through intervening dynamics and actions. Separate marginal intervals need not preserve that correlation; using them as a Cartesian outer approximation is safe only when the ensuing larger uncertainty is carried into control.

A practical realization can use a replay buffer, an observer with equivalent sufficient memory, or a recursive outer set such as an interval, polytope or zonotope. In each case, the represented set must contain every state compatible with the stated model and data. Approximation may enlarge that set; it may not discard a possible state merely to obtain a feasible control.

#### CAD.5:4.4 - Preserve the information needed by the next update

At each action time, use the following causal order:

1. Propagate the previous representation using the input actually executed and the allowed disturbance.
2. Incorporate each newly available packet at its sample time, then obtain the current-state projection.
3. Choose the estimate or set-based action from that projection, apply it by the qualified deadline, and retain the input information needed by the next update.

A state older than \(D\) can be projected out once no allowed future packet refers to it. This is different from throwing away the dependence between retained states. Duplicate packets do not supply additional independent information. In a bounded-set construction, independent noise need not be assumed: common error sources must be represented jointly or enclosed conservatively. With an uncertain timestamp, use the union of the admissible timestamp hypotheses, not their intersection.

If the compatible set becomes empty, the current model, bounds, packet, timestamp or executed-input record is inconsistent. Do not silently reset to a convenient point. Use a separately qualified fallback, obtain a new trusted initialization, or declare the demanded continuation unsupported. Packet loss or delay outside the allowed family likewise invalidates the relevant bound until a qualified recovery applies.

Reduce the internal representation when its update and control use remain sufficient. One exact reduction is available when \(s=T_rx\) has closed dynamics \(T_rA=A_rT_r\), the needed observations factor as \(C_j=C_{rj}T_r\), and the control law and constrained quantities depend only on \(s\). Then use \(s^+=A_rs+T_rB u^a+T_rw\) and the corresponding observation sets. If an omitted component influences a required future quantity, its influence must instead be retained or bounded.

Thus two histories may be merged only when the merged representation still supports every required future update and action under the allowed future observations and disturbances. Equal current estimates are not enough. A.3.3.PI develops this general sufficiency test; here the joint-state construction provides a direct control-specific realization.

#### CAD.5:4.5 - Obtain a usable error bound

Choose a representative \(\hat x_k\) and compute an enclosure \(V_{\eta,k}\) such that

$$
x_k=\hat x_k+\eta_k,\qquad \eta_k\in V_{\eta,k}.
$$

The enclosure can be obtained directly from \(X_k-\hat x_k\). To qualify a continuing controller, obtain a bound valid over the whole allowed run, including startup, admissible delays, sample gaps and loss modes. A bound from one favorable packet sequence is insufficient.

For scalar propagation from a measurement of age \(d\), with coefficient \(a\), measurement-error radius \(\epsilon\), disturbance radius \(q\) and known intervening inputs, a sufficient radius is

$$
r(d)=|a|^d\epsilon+q\sum_{i=0}^{d-1}|a|^i.
$$

The propagated center includes every executed input. The second term is uncertainty about unobserved disturbances; a more accurate old sample does not remove it.

For a multidimensional plant, a finite-window construction gives a sufficient bound without requiring every sensor to observe every coordinate. Take available samples with times \(\tau_i\in[k-L,k]\), subtract their known input responses, and stack them:

$$
r_i=y_i-C_i\sum_{s=k-L}^{\tau_i-1}A^{\tau_i-1-s}B u^a_s,\qquad
r=O x_{k-L}+n,\qquad O_i=C_i A^{\tau_i-(k-L)}.
$$

The stacked noise has components

$$
n_i=C_i\sum_{s=k-L}^{\tau_i-1}A^{\tau_i-1-s}w_s+v_i.
$$

Obtain \(N\) by applying these linear maps to the allowed joint disturbance and measurement-error set; separate component bounds give a conservative enclosure if the joint set is unavailable. Retain shared disturbances when practical. If \(O\) has full column rank, choose a left inverse \(J\), \(JO=I\), and form

$$
\hat x_k=A^LJr+\sum_{s=k-L}^{k-1}A^{k-1-s}B u^a_s.
$$

A sufficient error enclosure is

$$
V_\eta=\left(\bigoplus_{s=k-L}^{k-1}A^{k-1-s}W\right)
       \oplus(-A^LJ)N.
$$

The Minkowski sum \(\oplus\) adds all allowed elements of its operands. This enclosure may be conservative because the same disturbances occur in both terms; it does not assume their independence. Enumerate the admissible window and schedule modes, include the initial transient from \(X_0\), and enclose their errors. Poor conditioning of \(O\) can make a full-rank window useless for the required control margin.

Full-state observability is sufficient for this particular construction, not necessary for the task. A stable hidden component may have a small enough reachable set; a reduced state from :4.4 may suffice. If the window has no left inverse, return to the compatible-set construction and the required actions rather than declaring every such design impossible.

#### CAD.5:4.6 - Establish control under that information

First test whether the information permits a common action. In the following calculation, the selected \(u\) is executed as represented by the plant model; any bounded execution discrepancy must already be included in its disturbance or augmented state. For a required next-state set \(R_{\mathrm{next}}\), the robust admissible inputs are

$$
\mathcal U(X_k)=
\{u\in U:A X_k\oplus\{Bu\}\oplus W\subseteq R_{\mathrm{next}}\}.
$$

The quantifiers are “choose one \(u\), then allow every \(x\in X_k\) and \(w\in W\),” not “for every possible state, choose a different action.” For a halfspace \(h^\top x\le b\) of \(R_{\mathrm{next}}\), the test is

$$
\sup_{x\in X_k}h^\top Ax+h^\top Bu+\sup_{w\in W}h^\top w\le b.
$$

This provides a direct calculation for polytopes and support-function representations. When the test fails on an outer approximation, refine the approximation or change the design before claiming impossibility. A negative result for one chosen controller is weaker still.

One feasible step does not establish a continuing guarantee. A sufficient construction for a specified feedback \(u=K\hat x+g\), with constant \(g\) in the selected operating mode, uses \(F=A+BK\):

$$
x_{k+1}=F x_k+B g+w_k-BK\eta_k.
$$

Find a set \(R\), containing the allowed initial states and contained in the required state set, for which

$$
F R\oplus\{Bg\}\oplus W\oplus(-BK)V_\eta\subseteq R,
\qquad
K(R\oplus(-V_\eta))\oplus\{g\}\subseteq U.
$$

Together with a valid uniform error bound, these conditions prove state and input admissibility by induction. For a stable \(F\), one constructive candidate is the reachable sum of the forcing set \(D_f=\{Bg\}\oplus W\oplus(-BK)V_\eta\):

$$
R_\infty=\bigoplus_{i=0}^{\infty}F^i D_f.
$$

Use a finite outer approximation with a bounded tail, and enlarge it for the specified initial set if necessary; verify the inclusions after enlargement. For example, if an induced norm satisfies \(\|F\|\le q_F<1\) and \(D_f\) lies in a ball of radius \(d_f\), the ball of radius \(d_f/(1-q_F)\), enlarged to contain the initial ball, is invariant. A Euclidean norm larger than one does not prove that no other norm or set works.

These are sufficient conditions, not a universal synthesis algorithm. A stable hidden mode may be handled without measurement; an unstable or tightly constrained uncertain direction may exhaust the input or state margin. Failure can mean excessive approximation, a poor given feedback, an infeasible information arrangement, or an infeasible demand. Distinguish them.

A decisive impossibility witness consists of two admissible histories producing the same available packets and internal information but requiring disjoint actions, or an unavoidable uncertainty width larger than the permitted state interval. Such a witness rules out all causal controllers under those observation conditions, not merely the proposed feedback. Section :5 supplies both a positive construction and such a negative result.

#### CAD.5:4.7 - Connect the information result to a layered control construction

The method can be used without a layered architecture. When CAD.2 supplies a nominal state \(z\), command \(v\), projection \(P\) and control interface, replace its exact-state feedback by the implemented estimate:

$$
u=K(\hat x-Pz)+Qz+Rv,\qquad e=x-Pz,\qquad \eta=x-\hat x.
$$

For \(x^+=Ax+Bu+w\) and \(z^+=A_pz+B_pv\), the derived error dynamics are

$$
e^+=F e+H z+G v+w-BK\eta,
$$

where \(F=A+BK\), \(H=AP+BQ-PA_p\), and \(G=BR-PB_p\). The additional forcing \(-BK\eta\) is the effect of acting on the estimate.

Use the effective disturbance set \(W\oplus(-BK)V_\eta\) in CAD.3's invariant-error construction. For every allowed nominal state and command, state admissibility requires \(\{Pz\}\oplus E\subseteq X\), while the implemented input requires

$$
\{Qz+Rv\}\oplus K E\oplus(-K)V_\eta\subseteq U.
$$

These sums are conservative enclosures, not assertions that tracking and estimation errors are independent. A joint set can retain their correlation when the separate bounds are too costly.

CAD.4 then compares whole arrangements using the estimator's memory, communication, worst-case completion time, admissible packet timing and resulting error set. A new sensor changes \(V_\eta\), which can change the tracking-error set \(E\), the allowed nominal motion and the value of the whole architecture. A larger planner can also increase sensing or estimation latency through a shared resource, requiring the same calculation in reverse.

The added result is the construction of observation availability, internal information state and estimation uncertainty. CAD.1–4 continue to own decomposition, operational interfaces, tracking bounds and whole architectural comparison; this method does not replace them.

#### CAD.5:4.8 - Compare whole alternatives and return to the failed dependence

For each serious channel-and-schedule alternative, obtain the information update, its cost and delay, the error bound and the control conclusion. Keep the demanded behavior, initialization and resource accounting the same. Compare the alternatives that meet the demand; distinguish a proof of impossibility from failure of a sufficient bound.

Choose a sufficient arrangement with an explained cost and margin. A comparison can establish the best member of a stated finite family only when the objective is comparable and every potentially better member is evaluated decisively. Otherwise return the best qualified member found and the unresolved alternatives. A stochastic design can instead minimize an explicitly selected expected cost, but its covariance or a finite successful simulation is not a deterministic bound for this method's hard constraints.

Return according to what failed:

| Observed failure | Useful design return |
| --- | --- |
| Two compatible histories need different actions before any distinguishing packet arrives | Change what is observed, the sampling or delivery time, the actuator or the required behavior. Extra computation on the same information cannot distinguish them. |
| A feasible set is too large only after coarse approximation | Retain a useful correlation or use a tighter representation; include its execution cost. |
| Estimation uncertainty fits, but the given feedback violates an input limit | Change or requalify the feedback and its continuation, or change the physical limit or demand. Do not label this a sensor impossibility. |
| A longer observation gap or shared-resource delay breaks the bound | Restore a qualified timing arrangement or recalculate the information and control sets for the changed timing. |
| A stable unobserved component fits the task without intervention | Remove an unnecessary channel and its associated internal history. |
| A mode switch changes the permitted error or invariant set | Prove that the actual state and information representation enter the new qualified set, or retain a common valid bound. Nominal mode labels do not establish this. |

#### CAD.5:4.9 - Make the result executable and reusable

Return the selected and rejected complete arrangements with the controlled task, plant and uncertainty conditions, channel meanings and timing, initialization, internal state and update, control law, and the admissibility calculation. Make the unresolved distinction explicit if no candidate has a sufficient guarantee.

For implementation, connect sample timestamps and identities, actually executed inputs and the estimator's update to real producers and consumers. Qualify computation and transport deadlines under the proposed shared load. Select an already qualified behavior for missing data, inconsistent data and late completion; “hold the last command” is not automatically safe.

What changes in practice is the choice of the information the controller obtains and retains. The engineer can explain why a channel matters to an action, what must be remembered while waiting for another channel, and which changed condition invalidates the resulting control.

### CAD.5:5 - Archetypal Grounding

#### CAD.5:5.1 - A rapid partial observation and a delayed complete observation

Consider two normalized deviation coordinates:

$$
x_{k+1}=
\begin{bmatrix}1.2&0\\0&0.8\end{bmatrix}x_k+u_k+w_k,\qquad
|w_{1,k}|\le0.04,\quad |w_{2,k}|\le0.02.
$$

The initial state is known to be zero. At every sample the requirement is \(|x_1|\le0.08\), \(|x_2|\le0.06\), with \(|u_1|\le0.12\), \(|u_2|\le0.08\). Inputs are executed without delay and their executed values are available. All specified packets and computations finish before the relevant input selection. These are assumptions of a mathematical design case, not measurements of a physical installation.

The offered sensor packages are:

| Package | Observation available before \(u_k\) | Error bound | Sensor-resource cost |
| --- | --- | --- | --- |
| F | Current \(x_{1,k}\) only | \(0.01\) | 1 |
| S | Both coordinates at \(k-2\), at every tick after startup | \(0.005\) per coordinate | 1 |
| H | Both current coordinates | \(0.005\) per coordinate | 3 |

The sensor budget is 2. Estimator execution and transport capacity are assumed separately qualified for F+S; the sensor cost is not a claim about total implementation cost. Compare F, S and F+S under this budget, and retain H as the simpler alternative if the budget changes.

With F+S, use F for the first coordinate. Propagate S's second coordinate using the executed inputs:

$$
\hat x_{2,k}=0.8^2y_{2,k-2}+0.8u_{2,k-2}+u_{2,k-1}.
$$

The required internal state includes the two applicable input values and the delayed packet's sample time. The uncertainty bound is

$$
r_1=0.01,\qquad
r_2=0.8^2(0.005)+(1+0.8)(0.02)=0.0392.
$$

Before the first delayed packet arrives, propagate the known initial state and inputs; the second-coordinate uncertainty is at most \(0.02\) after one update and \(0.036\) after two. The same bound \(0.0392\) therefore covers startup. Incorporating S's first-coordinate information as an additional intersection is permissible but unnecessary for the following guarantee.

Choose \(u_i=-a_i\hat x_i\), with \(a_1=1.2,a_2=0.8\). Then \(x_i^+=a_i\eta_i+w_i\), so

$$
|x_1^+|\le1.2(0.01)+0.04=0.052<0.08,
\qquad
|x_2^+|\le0.8(0.0392)+0.02=0.05136<0.06.
$$

Whenever the required state bounds hold,

$$
|u_1|\le1.2(0.08+0.01)=0.108<0.12,
\qquad
|u_2|\le0.8(0.06+0.0392)=0.07936<0.08.
$$

The initial state is admissible, and these inequalities establish the state and input requirements for every subsequent tick and every disturbance and measurement error within the stated bounds. This is a continuing conditional guarantee, not an inference from a plotted trajectory.

One particular run makes the internal information visible. Let measurement errors be zero and take \(w_1=0.04,w_2=0.02\) at every update. At \(k=1\), \(x_2=0.02\), but no S packet has arrived and its prediction is zero. At \(k=2\), \(x_2=0.036\), while S reports \(x_{2,0}=0\). At \(k=3\), S reports \(x_{2,1}=0.02\); the propagated center is \(0.0128\), not the current \(x_{2,3}=0.0488\). The difference \(0.036\) is due to the two unobserved disturbances. The controller applies \(u_{2,3}=-0.01024\). On the next tick its prediction includes this executed input. Reusing the old observation without that input would no longer implement the qualified update.

#### CAD.5:5.2 - Why the individual channels do not suffice

With F alone, the second coordinate is never observed and does not influence the observed first coordinate. Consider two runs with opposite second-coordinate disturbances and otherwise identical information. The controller chooses the same second-coordinate commands in both. After five updates, half their separation is

$$
0.02(1+0.8+0.8^2+0.8^3+0.8^4)=0.067232>0.06.
$$

No common center can place both states inside the required interval. This excludes every causal controller using F alone under the stated assumptions, not just \(u=-A\hat x\).

With S alone, the latest two first-coordinate disturbances are unobserved when the next command is chosen. Even with perfect older observations, the next first-coordinate interval has unavoidable half-width

$$
0.04(1+1.2+1.2^2)=0.1456>0.08.
$$

The same indistinguishability argument rules out the required all-time bound. Improving the old measurement's accuracy cannot recover these disturbances before their consequences matter.

F+S is therefore sufficient where either offered channel alone is insufficient, under the same sensor budget and timing assumptions. This establishes a task-dependent benefit of combining channels. It does not establish that all heterogeneous sensing is superior or that the offered catalog is globally optimal.

#### CAD.5:5.3 - Increase the delay, then change the design or the demand

Suppose bus contention changes S's age from two ticks to four, while F and the requirements remain unchanged. The reconstructed second-coordinate radius becomes

$$
r_2(4)=0.8^4(0.005)+0.02(1+0.8+0.8^2+0.8^3)=0.061088.
$$

The same controller's next-state bound is \(0.8r_2(4)+0.02=0.0688704\), which exceeds \(0.06\). More decisively, four unobserved disturbances plus the next one yield the half-width \(0.067232\) from :5.2 even if S's old measurement is exact. F still reveals nothing about the second coordinate. Thus a different filter or gain using the same available information cannot restore this hard bound.

The engineer must change a consequential condition. Restore the qualified two-tick transport arrangement, obtain a timely observation of the second coordinate, or revise the task or physical dynamics. If the sensor budget becomes 3, H alone supports the same feedback with next-state bounds \(0.046\) and \(0.024\); its input bounds are \(0.102\) and \(0.052\). H needs no delayed-observation reconstruction. It is now a simpler sufficient choice.

A different task can also justify less information. If the allowed second-coordinate deviation becomes \(0.12\), retain F and set \(u_2=0\). The unobserved stable second coordinate has the invariant bound

$$
|x_2|\le\frac{0.02}{1-0.8}=0.1<0.12.
$$

S, its delayed packet processing and its input-history reconstruction are then unnecessary. This is sufficient for the changed task; it is not a cheaper solution to the original \(0.06\) requirement.

#### CAD.5:5.4 - What an internal-path ablation does and does not establish

For the scalar noiseless plant \(x_{k+1}=a x_k+u_k\), with a one-tick delayed observation \(y_k=x_{k-1}\), the predictor

$$
\hat x_k=a y_k+u_{k-1},\qquad u_k=-a\hat x_k
$$

uses the executed-input history. Removing that input term while retaining the remaining gains gives \(u_k=-a^2x_{k-1}\). At \(a=1.2\), the resulting characteristic polynomial is \(\lambda^2-1.2\lambda+1.44\); its roots have modulus \(1.2\), so this ablation is unstable.

It does not prove that every controller lacking that input-history path is unstable. Retuning the memoryless delayed-output law to \(u_k=-0.6x_{k-1}\) gives roots of \(\lambda^2-1.2\lambda+0.6\), both with modulus \(\sqrt{0.6}<1\). The latter establishes stabilization of this noiseless model, not the original predictor's performance or a bounded-disturbance constraint guarantee.

Use the first comparison to explain why a particular realization depends on its internal path. Use an impossibility argument such as :5.2–:5.3 when claiming that the available information cannot meet a requirement under any controller in the stated class.

#### CAD.5:5.5 - Recover two coupled coordinates from observations at different times

The general construction in :4.5 is not a coordinate-by-coordinate delay correction. Consider

$$
A=\begin{bmatrix}6/5&1/5\\1/10&4/5\end{bmatrix},\qquad B=I,
$$

with disturbance radii \((.04,.02)\) and measurement-error radius \(.005\). At time \(k=2\), use a first-coordinate observation sampled at time 0 and a second-coordinate observation sampled at time 1. Both samples and the actually applied \(u_0,u_1\) are available before this estimate is used. After subtracting the known input response,

$$
r=\begin{bmatrix}y_{1,0}\\y_{2,1}-[0\ \ 1]u_0\end{bmatrix},
\quad
O=\begin{bmatrix}1&0\\1/10&4/5\end{bmatrix},
\quad
J=O^{-1}=\begin{bmatrix}1&0\\-1/8&5/4\end{bmatrix}.
$$

Thus \(\hat x_2=A^2Jr+A u_0+u_1\). The second measurement contains \(w_{02}\), the second coordinate of the first disturbance, so it is related to the uncertainty in the subsequent propagation. Writing \(w_0=(w_{01},w_{02})\), \(w_1=(w_{11},w_{12})\), and the two measurement errors as \(v_1,v_2\), substitution gives

$$
\eta_1=\frac65w_{01}-\frac3{10}w_{02}+w_{11}
       -\frac{141}{100}v_1-\frac12v_2,
$$

$$
\eta_2=\frac1{10}w_{01}-\frac1{40}w_{02}+w_{12}
       -\frac{47}{400}v_1-\frac{33}{40}v_2.
$$

The exact coordinate radii for the stated box of original uncertainties are \((.10355,.0292125)\). Using the separate Minkowski enclosure in :4.5 gives the larger radii \((.11155,.0612125)\): the same \(w_{02}\) was allowed to vary separately in two occurrences. Both enclosures are valid; retaining the shared variable can save a margin that a conservative test would spend.

This calculation supplies a finite-window error set, not a controller or an all-time guarantee for this new plant. The next use is :4.6 with the required actions and continuation, or :4.7 when a planning-and-feedback interface is already selected. Repeated use also needs the other allowed sample windows and startup to be covered.

### CAD.5:6 - Bias-Annotation

The finite model and channel catalog can omit a better physical realization. Sensor-resource prices are contextual, and error or delay bounds need engineering grounds. An exact mathematical result cannot establish those grounds.

The bounded-set construction favors robust guarantees and can be conservative. A stochastic expected-cost problem may favor a different sensor schedule or estimator. Neither answer should be presented as the optimum for the other's criterion.

A compelling biological or organizational analogy can suggest a useful design question without supplying the engineered plant, uncertainty set or execution guarantee. Internal information reuse also admits different mathematical and physical realizations; a chosen block diagram is not evidence of a unique anatomy.

### CAD.5:7 - Conformance Checklist

- The controlled task, action time, initialization and allowed uncertainty are explicit, including the meaning of an actually executed input.
- Each observation constrains the state at its sample time; admissible sample gaps, delivery modes and resource coupling are included.
- The internal representation can be updated without discarding a control-relevant dependence; approximations enclose all compatible states.
- The control conclusion uses one action for the available information, and a continuing guarantee includes a valid error bound and continuation argument.
- Serious simpler alternatives are compared under the same demand; a changed demand is not disguised as a cheaper equivalent solution.
- A changed delay, observation or internal-state reduction returns to the affected calculation.
- An ablation, a failed sufficient bound and an information-based impossibility have different stated scopes.

### CAD.5:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Treating the most recently received values as simultaneous current state | Retain sample times and propagate their constraints through actual intervening inputs and disturbances. |
| Selecting sensors solely by total estimation error | Calculate the actions, constraints and continuation that the remaining uncertainty permits. |
| Assuming a complete delayed observation removes uncertainty | Retain the disturbances accumulated since the sample; test whether any action can tolerate them. |
| Keeping only an estimate and losing the means to update it | Construct sufficient history or an equivalent recursive state; verify the next update after the proposed reduction. |
| Turning a smaller covariance or successful simulation into a hard bound | Use the stated stochastic conclusion or derive a separate bounded-set guarantee. |
| Calling a conservative test failure a physical impossibility | Refine the enclosure or provide indistinguishable histories with incompatible consequences. |
| Removing an internal path, keeping all gains, and concluding the path is universally necessary | Retune the competing architecture under the same requirement, or use an information-based impossibility proof. |
| Adding a second sensor without including shared transport and compute load | Recalculate timing and the resulting error under the joint realization. |

### CAD.5:9 - Consequences

The result connects observation selection to admissible control rather than to an isolated estimator score. It can justify a combination of channels, a retained internal history, a tighter representation, or the removal of unnecessary sensing.

The cost is explicit modeling and calculation. Exact joint sets can grow too expensive, and robust outer sets can reject useful designs conservatively. The result remains conditional on the model, bounds, timing and implementation. It supplies neither a general guarantee for learned perception nor a complete treatment of nonlinear, state-dependent sensing and actuation.

### CAD.5:10 - Rationale

Information matters through distinctions the next action must respect. A measurement can refine an old state while leaving recent disturbances unresolved. Applied-input history makes predictable change available to the controller; it does not create missing information about unpredictable change.

The method therefore joins three constructions: compatible state histories, a sufficient internal update, and a common action with a qualified continuation. The two-channel example works because the rapid channel restricts a direction whose uncertainty grows too quickly, while the delayed complete channel is sufficient for the slower direction. The simpler changed-task case works because an unobserved direction remains bounded without intervention.

This separates two ideas often discussed together. **Diversity-enabled sweet spots (DeSS)** concern a favorable whole arrangement of components with different limitations under a specified task and resource model. **Internal feedback pathways (IFP)** concern reuse of internal action, prediction or state information in a controller's realization. One does not prove the other; the information and control calculations must establish their particular connection.

### CAD.5:11 - SoTA-Echoing

The precise question here is how to choose realizable observations and sufficient internal memory for bounded-error sampled control. The method joins state estimation and robust control constructions through their information, timing and admissibility conditions.

- [Nakahira, Liu, Sejnowski and Doyle, 2021, “Diversity-enabled sweet spots in layered architectures and speed–accuracy trade-offs in sensorimotor control”](https://doi.org/10.1073/pnas.1916367118) supplies a historical model of complementary pathways. Retain its demand for a whole-task and resource comparison; do not universalize its particular speed–accuracy relation or infer IFP from that DeSS model.
- [“Internal Feedback in Biological Control: Architectures of Diversity and Delays,” 2022 version](https://arxiv.org/pdf/2109.11752v3) supplies a related mathematical contrast between fast partial and delayed observations. Its selected-model and ablation comparisons do not establish necessity across all retuned architectures. Sections :4.6 and :5.4 retain that distinction.
- [Li, Sarma, Sejnowski and Doyle, 2023, “Internal feedback in the cortical perception–action loop enables fast and accurate behavior”](https://doi.org/10.1073/pnas.2300445120), especially its estimation and attention constructions, makes the role of internally available actions and predictions explicit. Adapt that mechanism, with its stated model limits. Do not adopt its asserted scalar no-IFP optimum: in the one-tick-delay, unit-white-noise model of pp.3/11 at \(a=1\), the proposed gain \(k_1=-1/4\) yields stationary state variance \(80/27\), while \(k_1=-1/2\) yields \(12/5\); both closed loops are stable. This comparison uses the article's state-only cost, not a control-effort penalty. The guarantees here use the separately stated bounded-disturbance criterion.
- [Casini, Garulli and Vicino, “Adaptive Threshold Selection for Set Membership State Estimation with Quantized Measurements,” author copy linked to the 2025 publication](https://www3.diism.unisi.it/casini/pdf/TAC_2025.pdf), §§3–6, develops feasible-set updates and adaptive quantization ([IEEE Transactions on Automatic Control](https://doi.org/10.1109/TAC.2025.3545704)). Adopt the set interpretation and explicit outer-approximation cost. Its higher-dimensional threshold choice targets output uncertainty, so control constraints and heterogeneous delivery timing still need the construction here. In particular, output uncertainty and its asymptotic boundedness are not the same requirement as the all-time state and input constraints in :4.6.
- [Dutta, Wilde and Smith, 2023 version, “A Unified Approach to Optimally Solving Sensor Scheduling and Sensor Selection Problems in Kalman Filtering”](https://arxiv.org/pdf/2304.02692v2), §§II–IV, is a serious alternative when the selected criterion is weighted expected estimation or LQG cost under finite-horizon resource constraints. Its mixed-integer construction can compare schedules under that stochastic formulation. Do not relabel its covariance result as a hard feasible-state bound; use it when its criterion is the required one.

Choose between these approaches by the required conclusion, permitted uncertainty model and executable cost. A fixed observer or current complete observation can remain preferable. Reopen the construction when the demanded constraint, admissible timing, sensor model, available computation or a relevant stronger result changes the design conclusion; a later publication date alone does not establish dominance.

### CAD.5:12 - Relations

[SYSE.5](../syse/26-syse-5---develop-an-engineered-system-s-functional-organizat.md) develops the engineered system's functional organization and bearer alternatives. This method supplies a specialized construction for its observation, internal information and control-use contributions. Its qualified alternatives and limitations can enter SYSE.6's broader architecture decision; they do not decide that whole architecture.

C.32.LCA supplies the general construction and comparison of a control architecture. This specialized method develops the mathematical information construction for the bounded class stated in :1; it does not revise the general method's scope. C.30.LCA qualifies the corresponding control-structure view rather than deriving the estimator or controller.

A.3.3.PI supplies the general test for retaining information needed by future prediction and update. Sections :4.3–:4.5 construct sufficient internal state and error bounds for the present control problem.

[CAD.1–4](11-cad-1---derive-a-control-decomposition-from-the-whole-proble.md) supply the connected quantitative construction of decomposition, interfaces, tracking bounds and whole control alternatives. Section :4.7 provides the explicit composition: estimator error enters their forcing and input constraints, while their execution arrangement constrains this method's observation age and computation time.

### CAD.5:End
