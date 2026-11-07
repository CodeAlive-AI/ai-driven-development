## CAD.3 - Construct a Jointly Admissible Command Domain

> **Type:** Method pattern
> **Status:** Stable

### CAD.3:1 - Problem frame

**Use this when** a connected controller must respect state, output or actuator limits while following commands from another computation. The upper plan may be feasible in its own model while leaving too little authority for correction below.

Start with the actual connected dynamics from CAD.2 and one limiting constraint. Derive the deviation that consumes its margin. The first useful result is a command domain with an invariant error bound and an admissible continuation, or a specific failure that returns the design for revision.

A simulation that stayed within bounds is useful evidence about that run. It is not the invariant command domain constructed here.

### CAD.3:2 - Problem

The layers can make mutually inconsistent promises. The tracker guarantees a small error only for modest commands, while the planner assumes that error before restricting its commands. Tightening an upper constraint by an arbitrary tolerance conceals that circular dependence. A feasible first command can also lead to a state from which no later command is feasible.

The construction must close both the simultaneous compatibility question and the continuation question.

### CAD.3:3 - Forces

| Force | Consequential tension |
| --- | --- |
| Planning freedom and correction authority | Aggressive nominal commands consume input needed for error rejection. |
| Tight bounds and defensible bounds | A smaller assumed error enlarges the command domain but can invalidate its own premise. |
| One feasible step and continued operation | Current feasibility does not ensure a viable successor. |
| Sampled evidence and continuous constraints | A bound at update instants can miss a violation between them. |

### CAD.3:4 - Solution

#### CAD.3:4.1 - Construct an invariant error set

For the linear interface of CAD.2, write

$$
e^+=Fe+Hz+Gv+w.
$$

Choose a proposed command set S of pairs $(z,v)$, a bounded mismatch set W, and an error set E containing the admitted initial error. A sufficient one-step condition is

$$
FE\ \oplus\ \{Hz+Gv:(z,v)\in S\}\ \oplus\ W\ \subseteq E.
$$

Here $\oplus$ is addition of sets. This is a property to establish, not a consequence of naming E an error tube. Substitution and induction then keep the error in E for every permitted command sequence. Preserve correlations between z and v when they materially reduce conservatism; replacing S by a Cartesian product can enlarge the forcing unnecessarily.

One usable construction takes a positive-definite M and the norm $\|e\|_M=\sqrt{e^\mathsf{T}Me}$. Verify

$$
q=\|M^{1/2}FM^{-1/2}\|_2<1,\qquad
d\geq\sup_{(z,v)\in S,\ w\in W}\|Hz+Gv+w\|_M.
$$

The triangle inequality gives $\|e^+\|_M\leq q\|e\|_M+d$. Therefore

$$
E=\{e:\|e\|_M\leq\varepsilon\},\qquad
\varepsilon\geq\max\{\|e_0\|_M,d/(1-q)\}
$$

is invariant. For a stable fixed F, a positive-definite solution of a discrete Lyapunov equation is a candidate M; verify the displayed norm inequality for the actual values used. Failure of this sufficient construction does not prove that no controller or invariant set exists.

For multiple timing modes, one sufficient condition for arbitrary admissible switching is a common set E containing the initial error and preserved by every admitted mode and reset map. This includes resets caused by a changed reference or error coordinate. Each step then starts in the same E, so induction covers any admitted sequence.

Separate invariant sets for the frozen modes are not sufficient by themselves. With mode-dependent or within-period phase sets $E_i$, prove that every allowed transition from mode or phase i to j, including its reset, sends the admitted part of $E_i$ into $E_j$ for all admitted commands and disturbances. Include initialization and the evolution within each phase. A boundary-map proof can use this construction, but a bound only at period boundaries leaves the intermediate phases uncovered.

#### CAD.3:4.2 - Translate error into planner and actuator constraints

With $x=Pz+e$ and $u=Qz+Rv+Ke$, require

$$
Pz+E\subseteq X,\qquad Qz+Rv+KE\subseteq U.
$$

These constraints reserve physical room and actuator authority for correction. For an output constraint use the actual output map, including the mismatch term in CAD.2:4.1.

For example, if $X=\{x:Lx\leq b\}$ and E is the ellipsoid above, each row must satisfy

$$
L_iPz+\varepsilon\sqrt{L_iM^{-1}L_i^\mathsf{T}}\leq b_i.
$$

If $U=\{u:Du\leq f\}$, the input row becomes

$$
D_i(Qz+Rv)+
\varepsilon\sqrt{D_iKM^{-1}K^\mathsf{T}D_i^\mathsf{T}}\leq f_i.
$$

Thus the amount of tightening comes from the connected dynamics and geometry. It is not a universal safety percentage.

Enforce these conditions at every instant covered by the claim. If z evolves between slow updates, an upper constraint checked only at those updates does not bound $Qz$ at every fast instant. Propagate the nominal trajectory or bound its intermediate states. Continuous-time constraints require a continuous evolution argument, not denser-looking sampled plots.

#### CAD.3:4.3 - Close the dependence between commands and error

The proposed command domain determines d, while the resulting E restricts the command domain. Solve this compatibility deliberately. Start with a desired command envelope, construct a valid E, then test the actual state and input inclusions. If they fail, choose a smaller envelope or change the interface, gains, model or timing, and repeat the affected derivation.

A more direct formulation searches for S and E satisfying the error inclusion and the physical constraints together. For finite-dimensional parameterizations this can be an optimization or feasibility problem. No generic solver or convergence guarantee follows from writing that problem.

Do not treat repeated tightening as automatic convergence. A mapping that sends candidate planning sets to newly permitted sets can reverse inclusion: larger commands produce larger errors and smaller permitted commands. Alternating bounds may remain separated. Establish a nonempty self-consistent pair and its inclusions; do not use a numerically stationary iteration as the proof.

When a bound is conservative, try retaining command correlation, phase-dependent sets or a better model before weakening a hard constraint. For a fixed qualified loop, compare a joint state-command admissible set with the separate command and error envelopes used here; [CAD.Reference:4.5.1](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands) gives the governor entry, and :11 identifies a construction using time-dependent estimation bounds. Establish its successor conditions for the actual command rule before replacing this sufficient construction. If the required command is physically impossible, return that incompatibility to the system requirement or architecture decision.

#### CAD.3:4.4 - Construct a continuation, not only one permitted command

A permissible pair $(z,v)$ must also lead somewhere from which work can continue. For the nominal update $z^+=A_pz+B_pv$, seek a set Z such that every admitted z has at least one permitted v with $z^+\in Z$.

One direct construction repeatedly removes states without such a successor:

$$
Z_{n+1}=
\{z\in Z_n:\exists v,\ (z,v)\in S,\ A_pz+B_pv\in Z_n\}.
$$

An exact fixed point is controlled invariant under the stated model. A finite iteration gives an outer candidate, not automatically an invariant set; test the successor condition before relying on it. Gridding a continuous set needs an approximation-error argument.

An alternative is to exhibit a smaller terminal set T and an explicit admissible terminal law. A finite plan ending in T then has a feasible continuation by appending that law. For receding-horizon use, the standard shift argument also needs the actual next nominal state, retained feasible tail, modeled uncertainty and implementation to match the argument. A measurement-based reset must preserve the initialization and feasibility conditions or use an independently qualified recovery.

If a new optimization fails or misses its deadline, continuing a previously feasible tail can be legitimate only while its assumptions still hold. “Use the previous plan” is not a universal fallback.

#### CAD.3:4.5 - Use a continuous-time branch only with its stronger premises

Let D be the domain of the connected continuous state on which the model and the bounds below apply, including the reference and any controller state on which the argument depends. Start the trajectory in D and suppose a differentiable function V satisfies, throughout D under the admitted input law,

$$
V\geq c_e\|x-Pz\|^2,\qquad
\dot V\leq-\alpha V+\beta\|w\|^2,
$$

with positive $c_e,\alpha$, nonnegative $\beta$, and $\|w(t)\|\leq\bar w$. Let $\tau_D$ be the first exit time from D, with $\tau_D=\infty$ if there is no exit. For every $0\leq t<\tau_D$ on which the solution exists, integration gives

$$
V(t)\leq e^{-\alpha t}V(0)
+\frac{\beta\bar w^2}{\alpha}(1-e^{-\alpha t}).
$$

Consequently $\|x-Pz\|\leq\varepsilon$ on that interval, where
$\varepsilon^2=\max\{V(0),\beta\bar w^2/\alpha\}/c_e$.
If h is Lipschitz with constant $L_h$ on a state domain containing both x(t) and Pz(t), requiring
$h(Pz(t))\geq L_h\varepsilon$ implies $h(x(t))\geq0$ on the same interval.

To claim the conclusion for all future time, separately establish continued existence and containment of the connected trajectory in D under the allowed reference evolution and disturbances, for example through a forward-invariant subset of D containing the admitted initial states. A tracking-error bound alone does not prevent the reference and plant from leaving the region where the derivative or Lipschitz bound is valid.

This is a sufficient construction for a particular connected dynamics and admissible input law. Obtain V and verify its derivative, domain, actuator feasibility and treatment of the moving reference; their existence is not supplied by the formula. Sampling, estimation, saturation and delay must either occur in that dynamics or be covered by its perturbation bound.

#### CAD.3:4.6 - Separate recognition, mathematical assurance and physical reliance

A shrinking error trace or plausible margin recognizes a promising design. The invariance and continuation arguments establish conditional properties of a mathematical model. Model validation, parameter and disturbance bounds, execution timing and physical tests determine whether those properties support the intended engineering use.

A decrease condition that applies only outside a threshold does not, in discrete time, prevent a jump from inside to outside. Use an actual invariant-set inclusion or a one-step bound valid on the entire proposed set. Likewise, a small average error is not a worst-case constraint bound.

### CAD.3:5 - Archetypal Grounding

For the held-reference case of CAD.2, $a=1/2,N=4,\delta=0.1$ give $E=8/75$. Since $|u|=(1-a)|e|$, a sufficient input bound is $4/75\approx0.05333<0.06$. Requiring $|r|\leq1-E=67/75$ also suffices for $|x|\leq1$. This position tightening is conservative: the scalar convex update can support less restrictive position arguments. It is not claimed to be the maximal command domain.

Now double the requested average progression from 0.025 to 0.05 per fast tick while retaining four-tick held updates. Then $\delta=0.2$, $E=16/75$, and the sufficient input bound is $8/75\approx0.10667$. More decisively, an initial jump from $x=r=0$ to $r=0.2$ commands $u=0.1$, directly violating the limit. Merely saturating u changes the error dynamics and requires a new analysis.

For continuous joined segments with $|d_k|\leq0.05$, $E=0.1$ and $|u|\leq0.05$. Choose $|r_k|\leq0.9$ and initialize $|x_0-r_0|\leq0.1$. Then the stated state and input limits hold at every fast sample. Generate the next reference by clipping $r_k+d_k$ to the interval $[-0.9,0.9]$, with $|d_k|\leq0.05$. The choice $d=0$ is always available, so the reference domain has an explicit continuation. This proves model feasibility even at a boundary; it does not promise arrival at every requested target or continuous physical safety between samples.

### CAD.3:6 - Bias-Annotation

Robust envelopes can be unnecessarily restrictive, especially when correlations are discarded. Conversely, nominal examples can make the operating domain look larger than the evidence warrants. Keep sufficiency, necessity, conservatism and empirical observation distinct.

### CAD.3:7 - Conformance Checklist

- The bound covers the actual initial condition, command class, mismatch and timing modes.
- Switching uses a common invariant set or proved transitions between the admitted mode or phase sets.
- A continuous-time claim ends at the first exit from its proof domain unless continued existence and containment in that domain are established.
- Every claimed constraint is tied to the instants or continuous intervals actually covered.
- Nominal commands leave justified correction authority.
- The command/error dependence closes without a circular assumption.
- There is a feasible continuation or an explicit limit on the duration of the claim.
- Physical reliance is no broader than the model and implementation evidence.

### CAD.3:8 - Common Anti-Patterns and How to Avoid Them

A tolerance selected first and justified afterward can consume imaginary authority; derive it with the command domain. A nonempty feasible set can contain dead ends; test successors. A sampled safe plan is not a continuous safety argument. A stable controller plus actuator saturation is a different closed loop from the unsaturated proof.

### CAD.3:9 - Consequences

The designer obtains commands that the whole architecture can support under stated conditions, or a precise reason to revise it. Some planning freedom is exchanged for dependable correction. The result may be conservative and computationally expensive; those costs belong in CAD.4.

### CAD.3:10 - Architectural Rationale

The lower guarantee and upper assumption concern the same connected behavior. Error propagation and constraint propagation therefore form one coupled construction. Adding continuation prevents a one-step solution from being mistaken for an operating strategy.

### CAD.3:11 - SoTA-Echoing

**How can a command domain support continued constrained operation?** The selected line is robust error containment, constraint tightening and a separate continuation argument in :4.1–4.4. It adapts [Stamouli and colleagues' constraint-propagation construction, §§4–5](https://arxiv.org/html/2504.10461). Their reported output-constraint guarantee is at slow samples; the all-fast-sample input extension has an additional condition. Here each claimed time interval is explicit, and direct set inclusion establishes invariance without extending a decrease-only condition into a global bound. The price is a sufficient domain that may exclude useful commands.

A serious alternative for a fixed qualified loop is a governor's joint state-command admissible set ([CAD.Reference:4.5.1](04-cad-reference-4---the-layered-planning-and-feedback-branch.md#cadreference451---keep-a-qualified-loop-and-govern-its-commands)). It can retain relations discarded by one common error envelope. [Castroviejo-Fernandez and colleagues, §§4–6, especially Proposition 2](https://arxiv.org/html/2401.02054v1) further use observer-error bounds and a sequence of admissible sets with a proved successor relation. Adapt that idea when a worst-case constant disturbance envelope is unnecessarily restrictive; the extra assumptions on estimation and disturbance variation, and the set computation, must be worth the enlarged domain. This motivates the return in :4.3 rather than weakening a hard constraint.

A predictive safety filter is another alternative when the requested object is a plant input and a finite backup trajectory can be computed. [Milios, Wabersich, Berkel and Schwenkel, §§II–IV](https://arxiv.org/html/2404.05496v2) distinguish recursive constraint satisfaction from additional stability guarantees and supply separate stabilizing conditions. Adopt that distinction in :4.4 and CAD.4:4.2. Such a filter needs its model, terminal ingredients and online computation; inserting it after the tracker changes the law analyzed in CAD.2.

For continuous dynamics, the [Matni–Ames–Doyle treatment, §4.5](https://arxiv.org/html/2401.15185) supplies a distinct safety-transfer line. Section :4.5 adapts the connection through an explicit error margin, conditional on remaining in the derivative and Lipschitz domains; it does not assume that every nonlinear controller supplies those premises. Reopen the selected containment construction when conservatism prevents the task, the admitted switching or disturbance changes, or the intended claim changes from constraint satisfaction to convergence or completion.

### CAD.3:12 - Relations

CAD.2 supplies the exact connected dynamics. CAD.1 is the return when no useful command domain exists for the selected split. CAD.4 uses the size and cost of the feasible domain in whole-candidate comparison. MMP.18 supplies general compatibility reasoning; this pattern supplies the control-specific invariance, margin and continuation construction.

For feedback on an estimated state, CAD.5:4.7 supplies the extra forcing and input allowance. Use its run-wide error bound, including startup and allowed delivery modes, before qualifying the resulting command domain.

### CAD.3:End
