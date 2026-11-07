## PHY.7 - Obtain Motion from a Physical Variational Principle

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.7:1 - Problem frame

Use this pattern when you need to derive physical evolution from a principle that compares possible histories. The difficulty may be choosing the physical action, incorporating a constraint, or deciding which changes of a history the principle permits. A correct variation of the wrong physical formulation can give a precise but unusable equation.

The first result is an equation of motion, a boundary condition or a conserved consequence with the physical assumptions needed to use it. Sometimes the result is a particular unresolved interaction or constraint rule that must be supplied before the derivation can answer the question.

An *action* assigns a scalar to a history in the chosen physical description. *Stationarity* means that its first variation vanishes for the specified allowed changes. The physical theory supplies the reason to impose that condition. MATH.10 supplies the mathematical reasoning about variations; this method constructs and interprets its physical premises.

You need to identify the physical quantities and understand the proposed principle's range. You also need enough mathematical preparation to interpret a variation, or another contributor who can perform it and explain its result. The examples use elementary constrained mechanics, a charged particle and a continuous field. Their branch-specific laws are stated in the cases.

Use an existing equation or PHY.6's balances and response laws when they already answer the question economically. A variational formulation is useful when it simplifies constrained motion, carries interactions across coordinate changes, exposes a symmetry, or produces both interior and boundary equations. It need not be constructed for every physical problem.

### PHY.7:2 - Problem

Writing `L=T-V` and applying the Euler-Lagrange formula leaves important physical work hidden. Which interactions are represented by the potential? Does a moving support contribute to the velocity? Which endpoint quantities are fixed? Can the constraint really be imposed on every varied history?

These choices can change the resulting motion. A missing velocity-dependent interaction can leave the energy apparently reasonable while removing a force. Discarding a boundary term can replace a loaded boundary by a free one. Extending a rule for position constraints to a different kind of constraint can select a different evolution.

### PHY.7:3 - Forces

| Force | Tension |
| --- | --- |
| Compact principle and physical content | One scalar can generate several equations, but every consequential interaction still needs a physical basis. |
| Convenient coordinates and retained motion | Eliminating a constraint can simplify the calculation while concealing a moving support or an omitted degree of freedom. |
| Interior equations and boundaries | Integration by parts exposes both; the physical preparation decides which boundary variations remain free. |
| Mathematical comparison and physical evolution | Nearby histories define a variation; the predicted motion is selected and used with its own preparation. |
| Reusable formalism and cost | A common derivation helps repeated changes, while a direct balance may obtain one consequence with less work. |

### PHY.7:4 - Solution

**Choose the physical principle → represent the histories and interactions → state the allowed variations → derive the interior and boundary conditions → interpret the consequence → revise the implicated premise.**

#### PHY.7:4.1 - Choose a principle for the physical question

State the consequence needed and the physical situation it concerns. Choose the retained participants, interactions and regime. PHY.5 helps decide which physical detail matters.

Recover an applicable variational principle from the physical theory, or propose one with a stated physical basis and conditional use. Identify what it assigns to a history and what property the realized history is required to have. A stationary action, minimum energy at equilibrium and a dissipative variational rule impose different conditions. Select the one appropriate to the question.

For a smooth classical configuration history `q(t)`, a common form is

`S[q] = integral from t0 to t1 of L(q,qdot,t) dt`,

where `L` is the Lagrangian. A field description can instead integrate a density over space and time. The following steps show how to use such a principle; another physical principle can require a different functional or variation rule.

If the action or its physical grounds are missing, identify the interaction or assumption needed to construct them. A balance with a response law may settle the immediate question while the variational formulation remains open. The availability of a differentiation tool does not resolve that physical choice.

#### PHY.7:4.2 - Construct the histories and their action

Choose coordinates or fields that represent the retained physical configuration. State how they recover the physical quantities needed by the question. Include the time dependence of that recovery: for a position `r=F(q,t)`, velocity is `r_dot=F_q*qdot+F_t`. The second term describes motion of the chosen mapping, such as a moving support.

For a classical mechanical description with the appropriate conservative interactions, construct kinetic energy from those velocities and potential energy from the interactions, then use `L=T-V`. Check the interaction rather than infer this form from the word *energy*. A velocity-dependent coupling, a dissipative interaction or an eliminated environment can require another term or another principle.

Keep relevant boundary contributions. Stored energy at an endpoint, an imposed load and a fixed endpoint are physically different. A field's action can contain an interior density and separate surface or endpoint terms.

When reducing coordinates, retain how the discarded quantities or reactions can be recovered if needed. If the reduction loses a physical effect important to the question, return to PHY.5; MMP.9 handles the mathematical reduction once its physical premises are chosen.

#### PHY.7:4.3 - State what may vary and what must remain fixed

Specify the interval, endpoint conditions, constraints and regularity used in the comparison. For the ordinary fixed-endpoint principle, take `q_epsilon=q+epsilon*eta`, with `eta(t0)=eta(t1)=0`. A position constraint requires a family that preserves that constraint, or a justified multiplier formulation. MATH.10 distinguishes a finite admissible family from a tangent calculation valid only to first order.

The endpoint values used to derive an equation need not be known future observations. Fixing them in the variation removes its endpoint contribution. After deriving the local evolution equation, an initial-value use supplies compatible initial position and velocity; it does not add a guessed final position as another condition.

Distinguish position constraints from restrictions on velocity that cannot be integrated into position constraints. For such a restriction, varying entire constrained histories and requiring zero work of ideal reactions on selected instantaneous virtual displacements can give different equations. A *virtual displacement* here is a comparison of configurations at one fixed time used to state that reaction condition. Obtain the reaction or allowed-variation rule from the physical constraint model before using either construction.

For example, an ideal reaction model for `A(q,t)*qdot+b(q,t)=0` may prescribe zero reaction work on displacements satisfying `A*delta_q=0`. Generalized forces Q are defined by their virtual work, `delta W=Q dot delta_q`. The Lagrange-d'Alembert equations then have the form `d/dt(L_qdot)-L_q=Q+A^T*lambda`, together with the velocity constraint; here Q contains the other forces and `lambda` determines the reactions. This result uses the ideal-reaction premise. Simply putting the velocity constraint into an action with a multiplier is a different construction and need not reproduce it. Use PHY.6 when the balance and reaction description is the sufficient route.

#### PHY.7:4.4 - Derive the interior and boundary conditions together

Apply MATH.10 to the allowed family. Vary the complete action, including dependent quantities and boundary terms. For the smooth finite-dimensional form above, integration by parts gives

`delta S = [L_qdot dot eta] at t0,t1 + integral (L_q-d/dt(L_qdot)) dot eta dt`.

With fixed endpoints and otherwise arbitrary interior variations, stationarity gives `d/dt(L_qdot)-L_q=0`. With restricted variations, derive the condition supported by that restricted family. Retain force terms when the selected principle includes their virtual work.

For a field, perform the corresponding integration in space as well as time. First identify the boundary terms, then decide which vanish because the boundary value is prescribed and which produce a condition because its variation is free. An endpoint force or boundary energy can change the latter condition without changing the interior equation.

Differentiate symbolically or computationally when helpful, but retain the variables held fixed and the substitution rules. A result from varying only part of the action answers that smaller calculation. It does not justify omitting a physical term.

Stationarity alone does not establish a minimum. Use the stronger comparison only when required and supported. MATH.10 gives both a minimizing free-particle case and a stationary oscillator history with changes of either sign in the action.

#### PHY.7:4.5 - Recover the physical consequence and preparation

Interpret the equations in the original physical quantities. Supply the independent initial, boundary and driving conditions needed for the intended use. Check their compatibility with constraints. An equation of motion can be the sufficient first result; obtaining a trajectory or a peak can require the subsequent computation in C.29.2.

Derive a conservation claim from the applicable symmetry and its conditions. For the ordinary unconstrained Lagrangian with no additional generalized force, absence of a coordinate from L gives a constant corresponding `L_qdot`. Absence of explicit time dependence gives a constant `qdot dot L_qdot-L`. Interpret these expressions physically; a velocity-dependent interaction can make a canonical momentum differ from mass times velocity. MATH.13 supplies the broader symmetry-to-consequence reasoning and PHY.4 supplies the physical grounds for the symmetry.

Use a discriminating comparison when it can change the result's use. A force balance can reveal a missing coupling; boundary work can reveal an omitted load; a change of coordinates can expose a missing velocity term. Agreement establishes that comparison under its premises. It does not independently validate the physical principle.

#### PHY.7:4.6 - Return through the premise that changed

When an interaction changes, revise its action term or force contribution. When a support or boundary changes, revise the histories, velocity mapping and allowed variations before reusing the equations. When a coordinate description changes, transform the whole expression while keeping the physical history recoverable.

Equivalent expressions can describe the same motion. In the ordinary fixed-endpoint principle, adding `dF(q,t)/dt` changes the action only by endpoint values, so it preserves the interior equations. A use with different endpoint freedoms must also carry the changed boundary term. Distinguish this redescription from introducing another physical interaction.

If a computed consequence fails, locate whether the fault is the physical principle, admissible comparison, mathematical derivation or obtaining procedure. B.5.MPC.R provides the combined return. Seek additional physical evidence only where its possible result could alter the decision or action; a useful conditional derivation can already be used with its stated limits.

### PHY.7:5 - Archetypal Grounding

#### PHY.7:5.1 - Represent a constraint, then move its support

A point mass m moves in a vertical plane on an ideal rigid, massless rod of length l. Its frictionless pivot is initially fixed. Gravity is uniform with acceleration g. Let theta be the angle from the downward vertical; relative to the pivot,

`x=l*sin(theta);  y=-l*cos(theta)`.

The rod constraint is built into this configuration. For its ideal reaction, virtual motion along the circle has no radial displacement and the reaction does no virtual work. Kinetic energy is `T=m*l^2*theta_dot^2/2`, and potential energy is `V=-m*g*l*cos(theta)`. Thus

`L=m*l^2*theta_dot^2/2+m*g*l*cos(theta)`.

Varying theta with fixed temporal endpoints gives

`m*l^2*theta_ddot+m*g*l*sin(theta)=0`.

For `l=1 m`, `g=10 m/s^2` and initial `theta=pi/6`, the angular acceleration is `-5 rad/s^2`. The radial reaction need not be solved to obtain that consequence. It can be recovered from the physical acceleration if a later question concerns the rod load.

**Changed support.** Prescribe a horizontal pivot position X(t). The physical position becomes `x=X(t)+l*sin(theta)` while y is unchanged. Differentiating the complete position gives

`T=m*(X_dot^2+2*X_dot*l*cos(theta)*theta_dot+l^2*theta_dot^2)/2`.

Keeping the same gravitational potential and varying theta gives

`m*l^2*theta_ddot+m*l*X_ddot*cos(theta)+m*g*l*sin(theta)=0`.

With pivot acceleration `X_ddot=2 m/s^2` at the same angle, the angular acceleration is about `-6.732 rad/s^2`. Omitting the pivot term from the velocity would preserve the old answer while losing a real forcing. The pivot's prescribed motion may do work, so the fixed-pivot mechanical-energy conservation claim does not automatically transfer.

**Changed interaction.** For the fixed pivot, add an established damping torque `Q=-b*theta_dot`, with `b>=0`. The virtual-work equation gives `m*l^2*theta_ddot+b*theta_dot+m*g*l*sin(theta)=0`. The mechanical energy has derivative `-b*theta_dot^2`. Appending this dissipative torque to a conservative scalar potential would require a different physical account. PHY.6 supplies the corresponding balance and receiving energy form; a more elaborate dissipative action is useful only when the intended work needs it.

The general move is to construct the allowed configuration and its velocities, derive the consequence, and rebuild only the affected contribution when the support or interaction changes.

#### PHY.7:5.2 - Recover an interaction that energy alone would miss

A nonrelativistic particle with mass m and charge e moves in the xy plane in a prescribed uniform magnetic field B perpendicular to it. Electric fields, radiation reaction and the particle's alteration of the source field are neglected. The electromagnetic coupling is the physical premise; the field does no mechanical work but changes the direction of motion.

Choose a vector potential `A=(-B*y/2,B*x/2,0)`, whose curl is the specified magnetic field. With zero electric scalar potential, the physical Lagrangian is

`L=m*(x_dot^2+y_dot^2)/2 + e*B*(x*y_dot-y*x_dot)/2`.

Its derivatives give

`d/dt(L_xdot)=m*x_ddot-e*B*y_dot/2;  L_x=e*B*y_dot/2`,

and the corresponding y expressions. The Euler-Lagrange equations are therefore

`m*x_ddot=e*B*y_dot;  m*y_ddot=-e*B*x_dot`.

For `e*B/m=2 per second`, initial `x_dot=3 m/s` and `y_dot=0`, the initial acceleration is `(0,-6) m/s^2`. Substitution into the kinetic-energy derivative gives zero. Conservation of kinetic energy alone would also allow straight uniform motion; it does not determine the magnetic turning. Using only T with zero scalar potential would miss the interaction.

**Changed representation.** Let `chi=B*x*y/2` and use `A_new=A+grad(chi)=(0,B*x,0)`. The new Lagrangian is `L_new=m*(x_dot^2+y_dot^2)/2+e*B*x*y_dot`. Its difference from L is `e*d(chi)/dt`, so the fixed-endpoint equations are unchanged. The canonical momenta `L_xdot` and `L_ydot` do change; the physical velocity and magnetic field do not. Comparing those canonical expressions as though they were two observed mechanical momenta would invent a physical discrepancy.

The action's stationary paths depend on the physical interaction; equivalent gauge descriptions preserve them under the stated endpoint rule.

#### PHY.7:5.3 - Derive an interior law and change the endpoint condition

A taut string has uniform tension T and mass per unit length mu. Its transverse displacement u(x,t) is small enough that slopes can be treated to leading order; changes of tension and longitudinal motion are neglected. The kinetic energy per length is `mu*u_t^2/2`. Expanding the extra length to second order in slope gives the stored elastic contribution `T*u_x^2/2`. For length l, use

`S[u]=integral over time and 0<=x<=l of (mu*u_t^2-T*u_x^2)/2 dx dt`.

Take variations eta that vanish at the two temporal endpoints. Integration by parts gives the interior coefficient `-mu*u_tt+T*u_xx` and the spatial boundary contribution

`integral over time of [-T*u_x*eta] at x=0,l dt`.

Thus the interior equation is `mu*u_tt=T*u_xx`. At a fixed endpoint, eta is zero. At an unloaded endpoint free to move transversely in this model, eta is arbitrary and the corresponding slope must be zero.

For `mu=0.01 kg/m`, `T=100 N` and `l=1 m`, wave speed is `sqrt(T/mu)=100 m/s`. Two fixed endpoints admit the lowest nonzero spatial mode `sin(pi*x/l)`, giving frequency `50 Hz`. Keep the left endpoint fixed and free the right endpoint transversely while maintaining its axial tension; the lowest mode becomes `sin(pi*x/(2*l))` and its frequency is `25 Hz`. The interior equation did not change. Reusing the fixed-end spectrum would miss the changed boundary.

**Loaded endpoint.** Attach a massless transverse spring of stiffness kappa at x=l. Add `-integral kappa*u(l,t)^2/2 dt` to the action. With the right endpoint variation free, its coefficient gives `T*u_x(l,t)+kappa*u(l,t)=0`. The spring changes the boundary condition through its stored energy. If an endpoint mass is consequential, its kinetic term must be included too; the massless condition would no longer supply that boundary's dynamics.

Retain the boundary contribution until the physical freedom or load determines its use.

### PHY.7:6 - Bias-Annotation

The examples make smooth classical stationarity easy to inspect. Quantum or probabilistic descriptions can connect an action to observations through a different rule; the fixed-history calculation here does not supply that rule. Use the principle and interpretation of the relevant physical theory.

Compact energy expressions can also hide how a constraint is maintained. The ideal rod, imposed pivot motion and massless endpoint spring each exclude physical detail. Restore that detail when reaction, compliance or a transient changes the requested consequence.

### PHY.7:7 - Conformance Checklist

- The selected physical theory or stated hypothesis supplies the principle and its range.
- Coordinates or fields recover the needed physical quantities, including time-dependent mappings.
- The action includes consequential interactions and boundary contributions.
- Allowed variations and constraints follow the selected physical principle; endpoint restrictions are explicit.
- Interior, force and boundary terms produce the conditions actually used.
- The interpreted result retains compatible preparation and the reach of its stationarity or conservation claim.
- A changed interaction, constraint or representation returns through its affected contribution; further inquiry serves a consequential question.

### PHY.7:8 - Common Anti-Patterns and How to Avoid Them

| Misstep | Consequence | Repair |
| --- | --- | --- |
| Use T-V without recovering the interaction | The magnetic force disappears although kinetic energy is constant. | Supply the coupling from the physical theory and vary the complete Lagrangian. |
| Differentiate coordinates while omitting their moving reference | The prescribed pivot acceleration is absent from the motion. | Differentiate the complete position map, including its explicit time dependence. |
| Discard a boundary term before deciding what is fixed | A loaded or free endpoint receives the wrong condition. | Retain the term until the boundary freedom and physical contribution are specified. |
| Use one constraint rule for every velocity restriction | Different variational constructions are treated as the same physical model. | Recover the constraint's reaction or admissible-variation premise. |
| Read stationary as minimum | A saddle history receives an unsupported optimality claim. | Use the first-variation result at its established scope and perform the stronger comparison when needed. |
| Read a changed canonical expression as changed motion | Gauge-related descriptions appear to disagree physically. | Recover the physical quantities and the endpoint term preserved by the transformation. |

### PHY.7:9 - Consequences

A useful physical principle can organize several coupled equations and expose what changes when coordinates, constraints or boundaries change. The calculation can be shared with a mathematical specialist or a symbolic tool while the physical premises remain inspectable.

The compact formulation does not remove the need for physical knowledge. Constructing a justified action can be harder than writing a balance. An equation derived from it may still require substantial work to solve or to connect to observation. Stop at the consequence sufficient for the current work and retain unresolved physical choices in any conditional use.

### PHY.7:10 - Architectural Rationale

The action, allowed comparison and physical interpretation carry different information. Keeping them together prevents the mathematical operation of variation from silently choosing a physical theory. Keeping them distinct allows a return to the part that changed.

MATH.10 supplies the common variational argument. PHY.7 adds the physical choice of principle, interactions, constraint model and preparation. PHY.6 offers the alternative construction from balances and response laws. MMP and the computational patterns receive the resulting equations and conditions when the intended consequence needs further formulation or calculation.

### PHY.7:11 - SoTA-Echoing

**When does an action formulation repay its cost?** For the ideal rod in :5.1, both the angular-action calculation and a tangential projection of Newton's force balance obtain the angular acceleration without solving the radial reaction. Both retain the rod constraint as a physical premise. If the rod load is the requested result, the balance or a reaction reconstruction is needed. For :5.3, both local force balance and field variation give the wave equation; retaining the action's endpoint term also makes the changed spring contribution available. Select that organization when repeated constraint or boundary changes make it useful. Use the simpler sufficient balance for an isolated question. These comparisons are constructed uses.

[Sussman and Wisdom, Structure and Interpretation of Classical Mechanics, second edition, chapter 1](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/9579/sicm_edition_2.zip/chapter001.html), is the established source for treating coordinate choice, physical action and variation as a connected construction. Adopt that connection in :4.1-.4. Sections 1.6 and 1.10 limit the automatic use of T-V and of coordinate-constraint arguments. In particular, section 1.10.3 distinguishes stationarity over constrained histories from the ideal-reaction rule for nonintegrable velocity constraints. The resulting instruction is to recover the physical constraint model before choosing the variation. Reopen that choice when the way a constraint is maintained changes a predicted reaction or motion.

[Gaset, Lainz, Mas and Rivas, The Herglotz variational principle for dissipative field theories](https://arxiv.org/abs/2211.17058) (2022 preprint, published 2024), develops two formulations of dissipative field variation. Its section 5.2 gives a mathematical case where they have different solutions; the conclusions identify a condition under which the approaches agree. Adapt the methodological consequence: naming a variational principle is insufficient without its variation rule and conditions. The example establishes formal non-equivalence; it does not select the physical adequacy of either account for an apparatus. An action-based treatment of a new dissipative interaction reopens that choice.

[Galley, Tsang and Stein, The principle of stationary nonconservative action for classical mechanics and field theories](https://arxiv.org/abs/1412.3082) (2014), supplies a distinct route using doubled variables and an initial-value construction. Its opening eliminated-oscillator example shows why eliminating an environment inside the usual endpoint action can lose the intended causal response. For the supplied damping torque in :5.1, the force or virtual-work equation already gives the desired motion with less apparatus. The extended-action route becomes relevant when the work needs elimination within an action or a variational treatment of nonconservative coupling. Retain that choice rather than silently absorbing every loss into an ordinary potential.

The worked calculations are constructed consequences of their stated classical descriptions.

### PHY.7:12 - Relations

- **MATH.10:** constructs admissible variations and establishes the reach of the resulting condition.
- **PHY.4, PHY.5 and B.5.TU:** supply physical symmetry grounds, retained detail and use of a theory in a case.
- **PHY.6 and C.29.BB:** provide balance and response constructions for an alternative derivation or a discriminating comparison.
- **MATH.13:** derives a mathematical consequence from symmetry; this method supplies the physical action and its admissible symmetry.
- **MMP.9, MMP.10 and C.29.2:** reduce or formulate the resulting mathematical problem and obtain the needed consequence.
- **B.5.MPC:** connects the mathematical result and its conditions to the physical question.
- **B.5.MPC.R:** revises a failed physical, mathematical or computational contribution and its affected uses.
- **C.11.DUA:** selects further inquiry when resolving the uncertainty can improve the work enough to justify its cost.

### PHY.7:End
