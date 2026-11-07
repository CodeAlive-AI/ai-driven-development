## CAD.Reference:3 - Information, tracking and execution must describe the same loop

### CAD.Reference:3.1 - How information changes a command margin

CAD.5 constructs compatible state histories from the measurements actually available before the action. Past inputs must be the inputs actually applied; a planned input or a measured value treated as current can produce a different information set. A run-wide bound \(V_\eta\) must cover startup and every allowed delivery mode, not only a favorable observation window.

When the interface is

$$
u=K(\hat x-Pz)+Qz+Rv,
$$

CAD.5:4.7 derives the estimate-based version of CAD.2's tracking equation:

$$
e^+=Fe+Hz+Gv+w-BK\eta.
$$

CAD.3 therefore receives the effective forcing \(W\oplus(-BK)V_\eta\). For every admitted nominal state and command, its state and input tests become

$$
\{Pz\}\oplus E\subseteq X,\qquad
\{Qz+Rv\}\oplus KE\oplus(-K)V_\eta\subseteq U.
$$

The separate set sums are sufficient enclosures, not assertions that tracking and estimation errors are independent. A tighter joint representation may recover a useful design that these separate margins reject. A failure of a sufficient enclosure is consequently different from CAD.5's indistinguishability proof that no action can meet the demand.

This is a two-way design connection. A tighter required command domain can require fresher observations. A sensor or estimator change can enlarge \(V_\eta\), shrink the usable command domain and invalidate a nominal performance claim. CAD.4 includes the cost of obtaining and updating that information. If a larger planner delays the estimator or communication, the old age bound is no longer a premise of the same realization. Reuse an unaffected result, but return the changed timing to CAD.5 and the resulting error to CAD.3.

### CAD.Reference:3.2 - A complete joint design and a changed delay

Consider the constructed scalar plant

$$
x_{k+1}=x_k+u_k+w_k,\qquad |w_k|\le .005,
$$

with \(|x|\le .65\), \(|u|\le .06\), initial \(x_0=z_0=0\), and a requested nominal motion satisfying \(|z|\le .5\), \(|z_{k+1}-z_k|\le .04\). The required tracking bound is \(|x-z|\le .11\), including intervals in which the nominal command uses the full rate \(.04\). The lower law is \(u=-.5(\hat x-z)\). Assume its update is completed every fast tick. The planner needs two fast ticks to calculate a new segment and supplies one every four ticks. Each calculation starts at least two ticks before its segment takes effect, and each new segment starts at the preceding segment's terminal nominal state. Hold \(z=0\) until the first segment is available. These timing and joining conditions are premises to establish for an actual realization.

A complete scalar sensor has error radius \(.005\) and gives the controller a sample at most two ticks old. CAD.5 propagates that sample through the actual intervening inputs, giving

$$
|\eta|\le r=.005+2(.005)=.015.
$$

Known \(x_0\) gives a startup radius at most \(.01\) before the first two-tick-old sample is usable. Thus the uniform radius \(.015\) covers startup as well. A current complete observation would need less memory and give a smaller radius; the delayed sensor is considered here because it is an available realization, not because delay is desirable.

CAD.2 models the timed segment by \(d_k=z_{k+1}-z_k\), so

$$
e_{k+1}=.5e_k-d_k+w_k+.5\eta_k.
$$

CAD.3 obtains the invariant radius

$$
E=\frac{.04+.005+.5(.015)}{1-.5}=.105.
$$

The initial error is inside it. The input bound is \(.5(E+r)=.06\); the state bound is \(.5+E=.605\le .65\); the required tracking bound is met. At the end of a nominal motion, holding \(z\) sets \(d=0\), which stays inside the same admitted increment set and preserves the continuation. The conclusion is conditional on the stated sample, plant and timing bounds.

This also explains the decomposition and interface choice. Asking the two-tick planner for a fresh result every tick misses its assumed deadline. Sending a held target that jumps by \(4(.04)=.16\) can fail immediately: from exact initial alignment and zero estimation error, that jump requests input \(.08>.06\). Sending a joined segment at the same four-tick planning rate preserves the requested nominal rate and the bound above. CAD.4 compares this whole realization with a faster planner, another controller or a current sensor, including their actual costs; the input margin alone does not rank them.

Now suppose shared computation increases the maximum observation age to four ticks. CAD.5 gives \(r=.025\); the same construction gives \(E=.115\) and input allowance \(.07\). It no longer establishes the required tracking or input limits. Reducing the allowed increment to \(.03\) gives \(E=.095\) and input allowance \(.06\), but does not satisfy the unchanged request for the full \(.04\) rate. Recovering the old age bound, using a more timely observation, changing the interface or controller, or obtaining a less conservative joint bound are different repairs to compare. This failed sufficient calculation is not a proof that every controller with four-tick-old observations is impossible.

The example crosses the information, exchange, feasibility and implementation questions without inventing a new control law synthesis theorem. It is an application of CAD.5:4.5–4.7, CAD.2's substitution and timing construction, CAD.3's invariance test and CAD.4's whole-candidate comparison. The larger task determines whether a smaller command domain remains useful.
