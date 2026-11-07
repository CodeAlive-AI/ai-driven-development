## MMP.20 - Obtain a Computable Continuation When Physical Constraints Change

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.20:1 - Problem frame

**Use this when** component equations describe a physical system in several modes, but changing the active constraints leaves the next computation undefined, inconsistent or dependent on an unexplained reset. A diode starts conducting, a loose rope becomes taut, or two rotating shafts engage. The task is to obtain the next admissible state and the equations that can evolve it.

The mathematical object is a physical model whose active differential and algebraic equations change with the mode. A differential-algebraic equation system (DAE) combines evolution laws with constraints that must hold at the same time. Here the working question is how that model can continue through a change of constraints.

The result is a conditional continuation: a processed system for each used mode, a restart relation tied to the preceding state, and the conditions under which integration may resume. A missing impact law or a contradictory switch can instead be the useful result. A model with an already justified reset and suitable numerical realization can be used directly.

The reader needs the component laws, elementary differential equations, differentiation of constraints and linear algebra. The worked cases below need only small systems. Larger models need symbolic structural analysis and suitable numerical solvers. An engineer may obtain those operations from a specialist or tool, while retaining responsibility for the physical assumptions and requested outputs.

### MMP.20:2 - Problem

Joining the component equations can determine motion in each mode while leaving the transition between them undefined. A velocity inherited from free flight can violate the tangency required by a newly taut rope. Finding a point that satisfies the new equations then leaves a further question: is it the state produced by the preceding motion and the specified impact?

A consistent initializer can solve the new constraints while changing quantities that the physical transition must preserve. Conversely, imposing continuity on every stored variable can make an admissible impulse impossible. The missing construction connects the previous trajectory, the active physical laws and the new consistency conditions before numerical evolution resumes.

### MMP.20:3 - Forces

| Force | Consequence for the construction |
| --- | --- |
| Component equations are reusable, but their dependencies change with the mode. | Recover constraints and solvable unknowns for the active equation set. |
| The old trajectory fixes event data; the new mode imposes additional conditions. | Separate inherited values from variables the restart may determine. |
| A short physical interaction can have a finite integrated effect. | Preserve impulse balance while taking the event-duration limit. |
| A numerical state must be both determined and physically admissible. | Check the actual equations and mode inequalities as well as their structural matching. |
| An ideal constraint can admit several impact laws. | State the physical choice or return the missing specification. |

### MMP.20:4 - Solution

Start at one such event. Write the equations active before it, the equations intended to hold afterwards, and the values fixed by the preceding trajectory. Try those values in the new mode's consistency conditions. A failed condition locates the restart problem.

Use an existing justified restart when it supplies the needed continuation. Otherwise perform the following construction on the affected modes. The small cases in :5 show both a continuous restart and an impulse derived from the event equations.

#### MMP.20:4.1 - Compose equations and recover the constraints on a start

Write component laws and connection balances together, retaining their units and sign conventions. Distinguish equations common to the modes from equations activated by a mode. A mode is a selected set of equations and inequalities over an interval. The choice of that set does not choose an order in which to calculate its variables.

For an active DAE, F(z,z_dot,t)=0, identify the highest derivative of each variable appearing in each equation. An equation–variable incidence graph can expose a missing determination or an overconstrained subsystem. When a constraint must hold throughout an interval, differentiate it to obtain the additional relations needed to solve for the leading derivatives and algebraic variables. Keep the undifferentiated and lower derivative constraints as conditions on a consistent start.

For example, a mass m>0 on a taut rope of length L has position q=(x,y) and velocity v. With downward gravitational acceleration g, its equations are

~~~
q_ddot + lambda*q + (0,g) = 0,
q·q = L^2.
~~~

Here lambda is a force coefficient: the tension magnitude is m\*L\*lambda on the circle. Differentiating the circle constraint within the taut mode gives q·v=0, then v·v+q·q_ddot=0. Substitution yields lambda=(v·v-g\*y)/L\^2. The position and tangency conditions constrain initialization; the last equation determines the coefficient used in the acceleration. Require L>0 and lambda≥0 for a rope that can pull but cannot push.

Differentiation applies on the smooth segment. Differentiating a position constraint across an impact while silently assuming continuous velocity would remove the very jump that needs explanation.

For larger DAEs, the Sigma or Pantelides methods organize this index reduction. They use equation–variable incidence and derivative orders to select differentiations and solution blocks. Obtain the transformed equations, consistency conditions and reconstruction of requested outputs from the implementation. An equation count or a perfect matching alone cannot establish solvability at the actual parameter values: the equations a+b=1 and 2a+2b=2 have a perfect structural matching but a singular numerical Jacobian.

A cold initializer chooses values satisfying the initial specification and these constraints. A hot restart additionally has to respect the preceding trajectory and the physical effects concentrated at the event. Replacing a physical initial value is a model change; replacing a numerical starting guess is part of solving the same model.

#### MMP.20:4.2 - Preserve the preceding state while constructing the event

Locate the first enabled event with its specified direction of crossing. At that instant, retain a copy of the preceding values. Recover any equality implied by the event, such as q·q=L^2 when the rope first reaches full extension. A time command to tighten a rope does not imply that equality.

Determine which stored quantities can remain continuous from the governing laws. With finite current a capacitor voltage is continuous; an impulsive current can change it. With finite force a velocity is continuous; a force impulse can change it. Thus continuity is a consequence to justify for the transition, not a universal property of every variable labelled a state.

If the inherited values satisfy the new consistency conditions, solve for the new algebraic variables and derivatives and check the new mode's inequalities. This can produce a continuous restart even when some algebraic readouts jump. If inherited values conflict with a newly imposed constraint, preserve the common physical balances and construct the effect needed at the event. A numerical projection onto the new constraint set is suitable only when that projection follows from the specified physical transition.

#### MMP.20:4.3 - Construct and rescale a mode-change array when an impulse is needed

The method in [Benveniste et al., v1, §§2–7](https://arxiv.org/abs/2512.10580v1) uses a small formal interval epsilon to relate derivatives to successive values, for example v_dot=(v_next-v)/epsilon. Combine finitely many shifted copies of the new mode's equations and their necessary differentiated constraints. Add these Euler identities. This finite system is a mode-change array; it is used to derive an event relation, not to select the eventual integration step size.

Values already determined by the previous mode are data. Event equalities involving only those data can be removed from the unknown solve when their validity follows from the guard and previous smooth trajectory. Record that reason: an inconvenient equation with a small residual is not automatically such a fact.

The array must retain the dynamics common to the two modes and all the new mode's equations at its final instant, including the consistency conditions and the equations for leading derivatives. Some new constraints that conflict with the inherited state may be postponed at earlier instants of the array. This is the constrained construction in the source, not permission to delete whichever equation prevents a solve. Match the dependent variables to equations while retaining all equations required to be active. A structurally underdetermined part identifies values still lacking a determining relation.

Find the orders of the potentially impulsive quantities. If z grows as epsilon\^(-mu), replace it by z_bar=epsilon\^mu\*z and scale its equations accordingly. The source solves conditions that preserve a matched term of maximal order in each equation; for the linear occurrences of impulsive quantities these reduce to difference constraints on the offsets. Its general procedure also chooses bounded array heights and diagnoses underdetermined portions.

A usable result needs finite offsets, finite restart variables, and enough array values to express the scaled quantities without introducing an unavailable later value. A nonlinear function of an impulsive variable can defeat this construction. Failure of that test is a limitation of the proposed restart construction; further physical specification or another mathematical treatment may be needed.

After scaling, set epsilon to zero. Solve the remaining restart equations using the preceding values as inputs. Check existence, local uniqueness and conditioning at the actual data, the new consistency constraints, conserved quantities and the physical inequalities. Reconstruct the new mode's algebraic values and leading derivatives. Resolve further immediate events before advancing time. If a mode requires a negative rope tension or a negative conducting diode current, it is not the admissible continuation.

For automatic processing of a larger array, the cited paper supplies the construction in §5, the rescaling problem and goodness conditions in §6, and the bounded-height and offset results in §7. The derivation below makes the limit construction explicit for one small model. It assumes a genuine outward crossing and a specified following interval. Grazing contact, simultaneous impacts and an accumulating sequence of events require further event semantics and analysis.

#### MMP.20:4.4 - Choose and use a sufficient realization

For the small cases, hand reduction plus event location and the derived restart is sufficient. For a larger composition, obtain a tool that supports the selected mode equations, structural changes, event localization and the chosen restart semantics. Exercise the consequential transition on the actual configuration; a successful single-mode solve does not answer that question.

[Modelica's reinit operator](https://specification.modelica.org/master/equations.html#reinit), as described in its development specification, applies a supplied state reset at an event. [ModelingToolkit's event API](https://docs.sciml.ai/ModelingToolkit/dev/API/model_building/#Event-handling) provides event effects and DAE reinitialization options. These are ways to execute and reconcile a specified update; the cited API descriptions do not establish that they derive the impulse law above from every multimode DAE. When computing a reset in a callback, preserve the pre-event values before updating any component, then solve the new algebraic conditions.

If an instantaneous idealization is unsuitable, model a finite contact duration, compliant rope or nonideal diode. That changes the physical or mathematical model and can introduce stiffness. Compare the answer needed at the receiving time scale as the added parameters vary. Reducing a solver's step alone does not supply the omitted contact law.

Use the checks that bear on the requested continuation: equation and constraint residuals, signs that admit the mode, conserved or dissipated quantities, event location, and numerical sensitivity. Structural regularity and actual numerical solvability answer different questions. A convergence check supports the computed case and horizon; it does not validate the physical idealization.

### MMP.20:5 - Archetypal Grounding

The circuit first shows a change of algebraic readouts with continuous stored energy. The rope then shows why a changed velocity needs a derived impulse and a stated impact law. The executable realization in :5.4 supplies the event and the following short trajectory for both cases.

#### MMP.20:5.1 - A mode change that needs no storage-state jump: RLDC2

Use the RLDC2 balance and component equations below. For each k=1,2, i_k is the diode current, u_k its signed voltage, v_k the capacitor voltage, and j_k the current through the resistor–inductor branch. The diode convention is i_k≥0, u_k≤0, i_k\*u_k=0. Set V=u1+v1=u2+v2, R=(10,15) ohm, L=(1,1.5) H and C=(0.1,0.15) F. The common equations include

~~~
i1+i2+j1+j2 = 0,
Lk*j_k_dot = V-Rk*j_k,
ik = Ck*v_k_dot.
~~~

A conducting diode imposes u_k=0; a blocking diode imposes i_k=0. The modes require different reductions. When both conduct, v1=v2 and differentiation gives v1_dot=v2_dot. When both block, j1+j2=0 and differentiation supplies the relation used to find V. With only one conducting, only its capacitor voltage is tied to V. Preserve the reduced state's reconstruction of the eliminated voltage or current.

Begin with v1=0.5 V, v2=0.7 V, j1=-0.2 A and j2=-0.3 A, with only the first diode conducting. Then V=v1, i1=-(j1+j2)>0 and u2=v1-v2<0. Because R1/L1=R2/L2=10 s^-1, V satisfies

~~~
V_ddot + 10*V_dot + (50/3)*V = 0,
V(0)=0.5, V_dot(0)=5.
~~~

The two characteristic roots r,s solve r\^2+10\*r+50/3=0. Write V=A\*exp(r\*t)+B\*exp(s\*t), with A=(5-0.5\*s)/(r-s) and B=0.5-A. This derivative stays positive through t=0.1 s, so the bracket [0,0.1] contains the first crossing of V=0.7. To recover the individual currents, set J=-C1\*V_dot and D=L1\*j1-L2\*j2. The component equations give D_dot=-10\*D, hence D=0.25\*exp(-10\*t), j1=(D+L2\*J)/(L1+L2), and j2=(L1\*J-D)/(L1+L2).

The second diode reaches u2=0 while u2 is increasing at t≈0.055317579971 s. At the event, V=v1=v2=0.7 V, j1≈-0.088645906588 A and j2≈-0.154950677682 A. The capacitor voltages and inductor currents are a consistent start for the mode with both diodes conducting. Set

~~~
V_dot = -(j1+j2)/(C1+C2),
i1 = C1*V_dot, i2 = C2*V_dot.
~~~

This yields i1≈0.097438633708 A and i2≈0.146157950562 A, both admissible. Just before the event the currents were approximately (0.243596584270,0) A. Their finite jump changes neither capacitor voltage nor inductor current. Both modes satisfy the energy balance

~~~
E = (L1*j1^2+L2*j2^2+C1*v1^2+C2*v2^2)/2,
E_dot = -R1*j1^2-R2*j2^2.
~~~

One millisecond into the new mode gives V≈0.700967203954 V and j1+j2≈-0.240011099724 A; both diodes still conduct. The implementation below uses the closed form on each of these two segments and locates the event by a bracketed root. Its chosen bracket contains the first crossing for these initial data.

When the R/L ratios change, return to the joint equations for V,j1,j2 and choose a numerical solution or a new reduction. The displayed scalar closed form uses the equal ratios. The mode equations and continuity argument remain available. A changed connection that instantaneously ties unequal capacitor voltages can instead require a charge-transfer impulse or a model of the intervening resistance. Use the equations of that new connection to determine it.

#### MMP.20:5.2 - Construct an impact and continue the motion

Take a unit mass, L=1 m, and g=9.81 m/s^2. During free flight the initial values are q0=(0.4,-0.74905) m and v0=(2,-0.019) m/s. The trajectory

~~~
q(t) = (0.4+2*t, -0.74905-0.019*t-g*t^2/2),
v(t) = (2, -0.019-g*t)
~~~

first reaches the circle at t=0.1 s, with q_minus=(0.6,-0.8) and v_minus=(2,-1). The radial component is outward: q_minus·v_minus=2. The new taut mode requires q_plus·v_plus=0, which continuity of the old velocity would violate.

Specify an inelastic capture into a taut interval. Keep q continuous. To display the event limit, use the inherited limiting position and velocity as the earlier array values and set q_epsilon=q_minus+epsilon\*v_minus. Using the source's past-determined Euler values instead changes these data by O(epsilon) and gives the same limit here. The circle residual at q_epsilon is O(epsilon), owing to the boundary event, and tends to zero. Use the common force equations and the velocity Euler identity, imposing tangency at that next position:

~~~
a + lambda*q_minus + (0,g) = 0,
v_epsilon-v_minus = epsilon*a,
q_epsilon·v_epsilon = 0.
~~~

These are five scalar equations for a_x,a_y,lambda,v_epsilon_x,v_epsilon_y. This reduced subsystem follows the construction in the source's Figures 2–3: the earlier tangency condition and its acceleration-level consequence are postponed, while the final-instant constraints remain active. The new mode's equations for leading derivatives at the final instant can be solved once this velocity is known; the calculation below reconstructs them through lambda_plus.

Acceleration and lambda can be O(1/epsilon), while both velocities remain finite. Set a_bar=epsilon\*a and alpha=epsilon\*lambda, multiply the force equations by epsilon, and take the limit q_epsilon→q_minus, v_epsilon→v_plus:

~~~
v_plus-v_minus + alpha*q_minus = 0,
q_minus·v_plus = 0,
q_plus = q_minus.
~~~

The Jacobian of the first three scalar equations with respect to v_plus_x,v_plus_y,alpha has determinant -(x_minus^2+y_minus^2)=-L^2. For L>0 this system has the unique solution

~~~
alpha = (q_minus·v_minus)/L^2,
v_plus = v_minus - alpha*q_minus.
~~~

Here alpha=2 s\^-1 and v_plus=(0.8,0.6) m/s. The impulse is radial; the scalar angular momentum per unit mass x\*v_y-y\*v_x is 1 m\^2/s both before and after. Kinetic energy falls from 2.5 J to 0.5 J. In general, the loss for this inelastic capture is m\*(q_minus·v_minus)\^2/(2\*L\^2). These results follow from the displayed equations.

Now compute the taut-mode coefficient using the new velocity: lambda_plus=8.848 s\^-2. It is positive, so a taut interval is locally admissible. Parameterize q=L\*(sin(theta),-cos(theta)); then theta_dot=omega and omega_dot=-(g/L)\*sin(theta). The restart gives theta=atan2(0.6,0.8), omega=1 s\^-1. Integrating those equations for another 0.1 s gives theta≈0.712977020833 and omega≈0.380685005685 s\^-1. Tension stays positive over that computed segment.

This example has passed through a free trajectory, an event, a derived impulse and a computable new segment. Continue monitoring the tension. A later loss of tension changes the active equations again.

#### MMP.20:5.3 - Change the impact law or event and return to the affected construction

The rope constraint and common force direction do not select an impact law. Add a coefficient of restitution e with 0≤e≤1 and radial relation q_minus·v_plus=-e\*(q_minus·v_minus). The same impulse balance now gives

~~~
v_plus = v_minus - (1+e)*(q_minus·v_minus)*q_minus/L^2.
~~~

For e=0.5 the initial event above yields v_plus=(0.2,1.4), radial component -1, and kinetic energy 1 J. The ball moves inward and the next interval is free flight. Imposing the taut interval's tangency condition together with this restitution relation would contradict the nonzero incoming radial velocity. Preserve the free-flight equations and replace the event law and selected next mode.

Without a restitution or capture law, radial impulse balance leaves alpha free. For this case, inward or tangent departure and no energy gain still allow every alpha in [2,4]. The values alpha=2 and alpha=4 give different valid departures under different impact assumptions. Report the missing law instead of choosing an arbitrary nearby consistent state.

Changing the guard can require a different model as well. If a time command imposes the length L=1 when q_minus=(0.5,0), the event no longer supplies q_minus·q_minus=L^2. Position continuity and the new circle constraint cannot both hold. Obtain a law for reeling, finite compliance or another specified physical action. Reusing the boundary-impact reset would silently change the situation.

#### MMP.20:5.4 - Run the two small models

Save the following code as `mode_changes.py` and run `python mode_changes.py` with Python 3. It uses the standard library. The default circuit event is near 0.055317579971 s; its voltage 1 ms later is near 0.700967203954 V. The rope event is at 0.1 s, with inelastic restart velocity (0.8,0.6) m/s. A further 0.1 s of taut motion gives theta near 0.712977020833 rad and omega near 0.380685005685 s^-1.

The code uses the reductions derived above. Its root brackets and horizons belong to these initial data. To change the event or parameters, establish a bracket for the first enabled crossing and follow the relevant return in :5.1 or :5.3. The final calls demonstrate rejection of a missing impact law and an event away from the rope boundary. Residuals, conserved quantities and the step-halving comparison help distinguish an implementation error from a change in the modeled physics.

~~~python
"""Small-model realization: RLDC2 event and a specified rope impact (SI units)."""
from math import atan2, cos, exp, sin, sqrt


def first_root(f, lo, hi):
    assert f(lo) < 0 < f(hi)
    for _ in range(60):
        mid = (lo + hi) / 2
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def voltage(v0, dv0, capacitance, t):
    # Applies here because R1/L1 = R2/L2 = 10 and L = (1, 1.5).
    d = sqrt(100 - 4 * (1 + 1 / 1.5) / capacitance)
    r, s = (-10 + d) / 2, (-10 - d) / 2
    a = (dv0 - s * v0) / (r - s)
    b = v0 - a
    return a * exp(r * t) + b * exp(s * t), r * a * exp(r * t) + s * b * exp(s * t)


te = first_root(lambda t: voltage(.5, 5, .1, t)[0] - .7, 0, .1)
V, dV = voltage(.5, 5, .1, te)
J = -.1 * dV
D = .25 * exp(-10 * te)
j1, j2 = (D + 1.5 * J) / 2.5, (J - D) / 2.5
assert J < 0 and abs(V - .7) < 1e-14
di = [(V - 10 * j1), (V - 15 * j2) / 1.5]
for cap_rates in ([dV, 0], [-J / .25, -J / .25]):
    i1, i2 = .1 * cap_rates[0], .15 * cap_rates[1]
    assert i1 >= 0 and i2 >= 0 and abs(i1 + i2 + J) < 1e-14
    energy_rate = j1 * di[0] + 1.5 * j2 * di[1] + V * (i1 + i2)
    assert abs(energy_rate + 10 * j1**2 + 15 * j2**2) < 1e-14
print('RLDC2 event:', te, V, j1, j2, 'diode currents after:', -.1 * J / .25, -.15 * J / .25)
Vr, dVr = voltage(V, -J / .25, .25, .001)
assert dVr > 0  # Both diodes continue conducting on this short segment.
print('RLDC2 1 ms later:', Vr, 'J:', -.25 * dVr)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


g, length = 9.81, 1.0


def flight(t):
    return (.4 + 2 * t, -.74905 - .019 * t - g * t * t / 2), (2, -.019 - g * t)


def impact(q, v, restitution):
    if restitution is None:
        raise ValueError('Specify an impact law before computing its reset.')
    if not 0 <= restitution <= 1 or abs(dot(q, q) - length**2) > 1e-12:
        raise ValueError('This reset requires a boundary impact and 0 <= e <= 1.')
    radial = dot(q, v) / length**2
    if radial <= 0:
        raise ValueError('This entry requires outward approach to the boundary.')
    return tuple(v[k] - (1 + restitution) * radial * q[k] for k in range(2))


tb = first_root(lambda t: dot(flight(t)[0], flight(t)[0]) - length**2, 0, .2)
q, vm = flight(tb)
vp = impact(q, vm, 0)
assert abs(dot(q, vp)) < 1e-12
assert abs(q[0] * vm[1] - q[1] * vm[0] - (q[0] * vp[1] - q[1] * vp[0])) < 1e-12
assert abs((dot(vm, vm) - dot(vp, vp)) / 2 - 2) < 1e-12
print('ball event:', tb, q, vm, 'inelastic restart:', vp)


def taut_segment(h):
    theta = atan2(q[0], -q[1])
    omega = (q[0] * vp[1] - q[1] * vp[0]) / length**2
    initial_energy = .5 * length**2 * omega**2 - g * length * cos(theta)
    min_tension = float('inf')
    for _ in range(round(.1 / h)):
        k1 = omega, -g / length * sin(theta)
        k2 = omega + h * k1[1] / 2, -g / length * sin(theta + h * k1[0] / 2)
        k3 = omega + h * k2[1] / 2, -g / length * sin(theta + h * k2[0] / 2)
        k4 = omega + h * k3[1], -g / length * sin(theta + h * k3[0])
        theta += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        omega += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        min_tension = min(min_tension, omega**2 + g / length * cos(theta))
    assert min_tension > 0
    energy_error = abs(.5 * length**2 * omega**2 - g * length * cos(theta) - initial_energy)
    return theta, omega, energy_error


coarse, fine = taut_segment(.001), taut_segment(.0005)
assert max(abs(coarse[k] - fine[k]) for k in (0, 1)) < 1e-10
print('ball after 0.1 s taut:', fine, 'step-halving difference:', max(abs(coarse[k] - fine[k]) for k in (0, 1)))
ve = impact(q, vm, .5)
assert abs(dot(q, ve) + 1) < 1e-12 and abs(dot(ve, ve) / 2 - 1) < 1e-12
print('changed restitution e=0.5:', ve, 'radial velocity:', dot(q, ve), 'new mode: free')
for args in [(q, vm, None), ((.5, 0), vm, 0)]:
    try:
        impact(*args)
    except ValueError as exc:
        print('required model return:', exc)
    else:
        raise AssertionError('An unsupported reset was accepted.')
~~~

### MMP.20:6 - Bias-Annotation

Ideal diodes and an inextensible rope concentrate the question on equation changes. Real switching and contact can involve resistance, compliance and a finite interaction time. Choose that idealization from the physical question and the time scale on which the answer will be used.

A numerically convenient reset can conceal a physical choice. Recover the physical law and admissible signs before accepting it. For a different component, obtain its balances, event and consistency conditions before transferring either derivation.

### MMP.20:7 - Conformance Checklist

Use this checklist when deciding whether the computed continuation can answer the physical question.

| Check | What to establish |
| --- | --- |
| CC-MMP.20.1 | The active equations, mode inequalities, sign conventions and quantities inherited from the preceding trajectory are explicit. |
| CC-MMP.20.2 | The processed mode equations determine the required leading derivatives and algebraic variables. Any differentiated constraints retain their lower conditions at a start; the actual solve is sufficiently determined and conditioned. |
| CC-MMP.20.3 | The event direction and any equality treated as a fact follow from the guard and preceding trajectory. |
| CC-MMP.20.4 | Continuity or a jump of each affected stored quantity follows from its governing balance and the specified transition. |
| CC-MMP.20.5 | An array used to derive an impulse preserves the common dynamics and final constraints, admits finite rescaling, and uses no unavailable later value. |
| CC-MMP.20.6 | The restart satisfies the new consistency conditions, physical inequalities and relevant conserved or dissipated quantities. Any additional impact law is stated. |
| CC-MMP.20.7 | The numerical realization resolves the event and next segment at sufficient accuracy; further immediate events are settled before time advances. |
| CC-MMP.20.8 | A changed law, guard or reduction assumption returns to the affected construction; an absent determining law is reported as a model question. |

### MMP.20:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Effect | Repair |
| --- | --- | --- |
| Keep every stored variable continuous at an impact | Excludes the velocity change required by the new constraint | Derive the jump from the impulse balance and impact law |
| Project to any nearby consistent state | Can change momentum or energy without a physical cause | Derive which projection, if any, the transition permits |
| Drop a conflicting equation solely to obtain a square system | Can remove the common balance or a required final constraint | Preserve those equations and use the constrained array construction |
| Treat a perfect matching as numerical invertibility | Misses parameter-dependent or algebraic singularities | Examine the actual Jacobian and the resulting solve |
| Treat a time command as a boundary crossing | Introduces a geometric fact the event did not supply | Reconstruct the event or obtain the missing physical action |
| Reuse a reduction after its parameter relation changes | Evolves a different model | Return to the joint mode equations and derive a suitable reduction |
| Reduce the integration step to select an impact law | Adds precision without determining the physical continuation | Specify the law or resolve a finite contact model |

### MMP.20:9 - Consequences

The model can supply a next state together with the equations and conditions that make its continuation meaningful. A failure can be localized to the component laws, event, consistency constraints, structural processing or numerical computation.

This changes repair in practice. A different coefficient of restitution reopens the event law and next mode. A changed R/L relation reopens the circuit reduction. A tighter requested numerical tolerance changes the computation while preserving a justified physical restart. An unresolved impact law remains a modeling question even when a solver returns a consistent point.

The construction costs more than executing a supplied reset. Use it where that reset or its admissibility is missing. Large arrays require appropriate symbolic and numerical support, and a singular or unsupported event can require a richer physical model.

### MMP.20:10 - Architectural Rationale

The preceding trajectory and the new mode contribute different information. Treating both as freely adjustable initialization data loses the relation between the event and its physical history. Treating both as simultaneously smooth can suppress a real jump. Keeping inherited values separate from restart unknowns exposes the determining relation.

A mode-change array preserves the time relation long enough to identify the concentrated effect. Scaling before taking the limit retains the finite impulse that would disappear from an unscaled calculation. The final constraints then connect that event result to ordinary evolution in the new mode.

Separate physical specification, mathematical processing and numerical realization so that a change returns to the operation it affects. An improved numerical solver can compute an already determined answer more accurately; choosing a different impact law changes the answer being computed.

### MMP.20:11 - SoTA-Echoing

**Mode-dependent structural processing.** Benveniste, Caillaud and Malandain, *The Mathematical Foundations of Physical Systems Modeling Languages* (2020/2021), §12, uses RLDC2 to show that dependencies and differentiations change with the diode modes. This pattern adopts that structural lesson. The example in :5.1 uses the declared complementarity directly and permits finite jumps of algebraic diode currents. The source's continuous-diode-current assumption would exclude this event. The printed auxiliary convention s=i when conducting, s=−u when blocking, with conduction selected by s≥0, would classify a constant blocking state i=0,u=−1 as conducting. Its fixed initial currents j1=2,j2=1 also require i1+i2=−3 under the displayed balance, contradicting i_k≥0. Use the explicit convention and consistent initial data in :5.1. The source's discussion of particular compiler versions is historical. [Source, §12](https://arxiv.org/abs/2008.05166).

**Derive the restart before integrating it.** Benveniste et al., *Structural Methods for handling mode changes in multimode DAE systems*, v1 (December 2025), §§2–7, develops the array, permitted postponement, rescaling and restart construction used in :4.3 and :5.2. The source supplies general structural procedures and conditions for a well-defined limit. The small derivation here exposes the physical balances and the finite system an engineer can solve directly; automatic treatment of larger arrays needs the source's height, matching and rescaling algorithms. [Source](https://arxiv.org/abs/2512.10580v1).

**An impact choice remains a physical input.** The January 2026 revision adds a restart constraint T and an elastic-impact example in §9. This supports the explicit-law alternative in :5.3: a different restitution can require a different following mode. Adopt that distinction when specifying the transition; a mode declaration alone leaves the impact choice unresolved. [Revision v2, §9](https://arxiv.org/html/2512.10580v2#S9).

**Use the simplest adequate realization.** A supplied, justified reset can be executed with an event update, such as the Modelica or ModelingToolkit facilities cited in :4.4. Deriving a mode-change array is useful when the reset itself is missing. A finite contact or switching model is another choice when its duration or internal behavior matters; it adds parameters and possibly stiffness, while retaining the transient physics the instantaneous idealization removes. Compare those alternatives against the same physical question and required time scale.

### MMP.20:12 - Relations

- **MMP.18** supplies a joint formulation when the component models still need compatible exchanges. This pattern processes an already composed model when its active constraints change.
- **A.3.3.TR** uses the resulting mode equations, event and restart relation to describe and compose the continuation. Its supplied-reset case can be used directly when that relation is already justified.
- **C.29.2** connects mathematical equations with an effective computation; **CMP.8** controls the numerical approximation of the answer determined here.
- **MMP.10** helps revise an inconsistent constraint formulation. The subject practice supplies the component and impact laws whose meaning the formulation must retain.
- **MMP.9** can reduce a determined evolution and **MMP.17** can replace selected responses when their preservation conditions hold. Neither is a required stage for the small continuations above.
- **MMP.14** investigates a failed prediction when the discrepancy, rather than an already identified changed premise, is the unresolved question.

### MMP.20:End
