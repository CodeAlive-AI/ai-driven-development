## PHY.6 - Construct Physical Evolution from Balances and Response Laws

> **Type:** Method
> **Status:** Stable
> **Normativity:** Normative

### PHY.6:1 - Problem frame

Use this pattern when you can identify physical participants and their interactions, but cannot yet say how their coupled situation will evolve. You may know what is conserved while lacking the law that determines an exchange rate. You may have equations for each part while their connection or initial preparation remains inconsistent.

Start with the consequence you need: an initial response, a trajectory, a transported amount, a settled state or a distribution of outcomes. Choose the participants, exchanges and response laws needed for that consequence. A usable first result is a coupled physical description from which the consequence follows, or an identified missing response or incompatible condition that tells you what to resolve next.

Here a *response law* relates a physical interaction or change to the conditions on which it depends. A constitutive law is one such relation for a material or component. The method constructs an account from physical balances, response laws and preparation; it works across physical branches.

You need to identify the physical quantities and interpret the proposed relations and their conditions. The worked cases add their own preparation: elementary motion and energy calculations, a spatial continuity equation, and charge storage. These are different demonstrations of the same construction.

If a known physical account already supplies the required result, use it. If a balance alone settles the question, stop there. C.29.BB supplies that general balance method. Use PHY.5 when choosing which physical detail to retain; use this pattern when assembling the retained physical relations. Once that account is settled, MMP.10 and C.29.2 help formulate and obtain its mathematical consequences.

### PHY.6:2 - Problem

A balance says how accumulation relates to transfer and production. It can leave the transfer itself unknown. Adding a convenient rate formula may complete an equation system while describing the wrong physical interaction.

Combining individually useful descriptions adds another difficulty. A contact may store a quantity, a connection may impose a constraint, and two parts may use different signs or reference frames. Initial values acceptable to each isolated part can be impossible after they are connected. A solver can then fail for a physical reason, or return a result for a preparation different from the intended one.

The task is to construct mutually compatible physical relations and preparation, then derive the consequence that the work needs.

### PHY.6:3 - Forces

| Force | Tension |
| --- | --- |
| General balance and particular response | Conservation restricts change; material and interaction laws determine much of the remaining behavior. |
| Reusable parts and coupled behavior | A part's relation can remain useful while its boundary conditions change when connected. |
| Ideal connection and physical preparation | An ideal constraint can simplify later evolution while excluding the supplied initial state. |
| Physical detail and sufficient answer | A total or a bound may answer the question even when a detailed trajectory remains undetermined. |
| Available grounds and conditional use | An established response supports a stronger physical claim than an untested working hypothesis, while both can support useful conditional reasoning. |

### PHY.6:4 - Solution

**Choose the consequence → identify participants and exchanges → supply response laws → connect the relations → make the preparation consistent → derive and use the needed consequence.**

#### PHY.6:4.1 - Choose the consequence and physical participants

State what the answer will let someone interpret, choose or do. Identify the quantity, interval and preparation that matter. A peak response, a total transferred amount and a settled value can require different accounts of the same arrangement.

Choose the physical participants and their boundaries at a useful resolution. Locate the interactions that can affect the answer, including supports, surrounding media and measurement when relevant. Distinguish a quantity stored in a participant from a quantity passing through its boundary. Include storage in a contact or field when omitting it would change the consequence.

Use PHY.5 to resolve a consequential choice of scale or omitted interaction. A spatial field, a few aggregate variables and individual particles are possible descriptions; their physical adequacy depends on the question and regime.

#### PHY.6:4.2 - Construct the balances with physical meanings

Use C.29.BB to choose the additive quantity, common interval, signs, transfers and internal production. Write each term with its physical meaning and compatible units. For vector quantities, use a common frame or an explicit transformation between frames.

For a fixed spatial region, a useful form is

`rate of stored quantity = inward transfer - outward transfer + internal production.`

A local continuity equation expresses the same relation for a density and its flux. The choice of quantity determines the production term: a chemical species can be consumed while the atoms it contains remain in reaction products. A closed boundary alone does not make every selected quantity constant.

Identify which terms remain undetermined. A momentum balance may still need forces; a species balance may need transport and reaction rates. If the requested total already follows without those details, retain that consequence and avoid completing an unnecessary model.

#### PHY.6:4.3 - Supply the response and configuration relations

For each unresolved interaction that affects the answer, state how its response depends on the physical conditions. Use an applicable theory, an established material response, an available measurement or a stated working hypothesis. PHY.4 helps constrain a law whose form is unknown; MMP.11 helps represent its remaining freedom.

Recover the conditions under which the relation is used. Does it describe the current state, dependence on earlier states, a spatial gradient, an average response or fluctuations? Does it assume a settled contact, a constant material parameter or a particular preparation? Supply the configuration relations needed to connect that response to the retained variables.

Keep physical restrictions that the chosen description relies on. A passive damping law transfers mechanical energy into other forms; it does not destroy total energy. If that heating changes the response during the intended use, include the resulting dependence. A fitted or learned response can also supply a relation, but its physical restrictions and usable range must come from its construction or grounds, not from the fact that it produces numbers.

When several physically plausible laws remain, derive what each changes in the requested consequence. A bound or a conditional answer may be sufficient. Seek another observation or a more detailed account when its possible result can change the work; C.11.DUA helps decide that inquiry.

#### PHY.6:4.4 - Connect the physical relations before choosing a solving order

State what a connection makes common and what it transfers. Match quantities, units, frames and orientations at that connection. Equal values require a physical reason: two locations in contact can still have a finite resistance or an intervening store. If the connection has its own consequential dynamics, describe those dynamics.

Combine the part balances through the common transfer. Transfers internal to the combined boundary cancel when they describe the same exchange over the same interval. Retain conversions between quantities and energy forms. For an energetic connection, derive its power expression from the physical variables; variable names such as *potential* and *flow* alone do not establish their product as power.

Keep the equations as simultaneous relations while constructing the physical account. They can include derivatives, algebraic constraints, spatial dependence or statistical response. In a differential-algebraic description, some relations constrain values while others describe change. Which variable is solved for is a later mathematical or computational choice; changing that order need not change the physical interaction.

Eliminate a variable only while retaining the relation or reconstruction needed by later use. MMP.9 supplies mathematical reduction and MMP.10 supplies a formulation for the chosen analysis. If two parts disagree at their connection, return to their quantity meanings and physical assumptions before changing a solver.

#### PHY.6:4.5 - Make the preparation compatible with the connected account

Supply the independent initial, boundary and driving conditions needed by the requested evolution. Substitute the proposed preparation into the connected relations. Solve for dependent initial values and reactions. Preserve the difference between a physical initial condition and a numerical starting guess.

A motion constraint also constrains admissible initial velocity. An electrical connection can constrain initial potentials. A spatial description needs boundary conditions appropriate to its transport and response. Determine which conditions can be chosen freely and which follow from the others.

An equation count can expose an omitted relation, but equal counts do not establish a consistent or uniquely determined problem. Examine the dependence of the actual relations and the existence conditions needed for the intended result. C.29.2 supplies the subsequent computational formulation; a solver diagnostic can help locate a problem without deciding whether the physical preparation should change.

If the preparation is incompatible, identify the conflict and its physical alternatives. Correct a mistaken initial value, relax an unjustified ideal constraint, or describe the interaction that establishes the new state. Choose among these from the actual preparation. Do not silently substitute an easier initial state.

#### PHY.6:4.6 - Derive the consequence and return through the implicated premise

Obtain the first result at the resolution the question needs. This may be an initial derivative, an integrated balance, a limiting state or a computed evolution. B.5.MPC connects the mathematical result and its conditions to the physical question.

Use checks that can distinguish a wrong construction for this use. Combining part balances can expose a duplicated exchange; an energy calculation can expose a sign error or an omitted conversion; substituting the preparation can expose an impossible constraint. A limiting case or available observation can test a disputed physical premise. Passing one such check establishes only what it examines.

Distinguish a consequence of the stated equations from evidence that those equations describe the intended situation. Numerical accuracy concerns how the chosen consequence was obtained. Physical adequacy concerns the premises, preparation and interactions represented. Keep those qualifications with the result, without requiring new evidence when the conditional result already serves the work.

When the question, preparation or connection changes, revisit the affected relations. Retain contributions whose conditions still hold. An unresolved exchange law directs work to physical theory or response characterization; inconsistent coupled quantities direct work to the connection; an adequate account with an inaccurate computed result directs work to the computation. B.5.MPC.R supplies the broader repair when physical, mathematical and computational contributions need to change together.

### PHY.6:5 - Archetypal Grounding

#### PHY.6:5.1 - Derive coupled motion and identify where mechanical energy goes

Two bodies move along one line. Their masses are `m1` and `m2`. Displacements `x1` and `x2` are measured from a configuration in which their connecting spring is unstretched, so its extension is `x2-x1`. Velocities are `v1` and `v2`. A spring and a viscous damper act between them; the connector's inertia is neglected in the chosen regime.

The momentum balances need the connecting force. Use the ideal response

`f = k*(x2-x1) + c*(v2-v1)`,

where `k>0` is stiffness and `c>=0` is damping. The force on body 1 is `f`; that on body 2 is `-f`.

**When a response parameter is missing.** Suppose this linear response form is already justified, but its parameters are not yet supplied. A static test with extension `1 m`, zero relative velocity and force `3 N` determines `k=3 N/m`; it leaves c undetermined. At extension `1 m` and relative velocity `-2 m/s`, the choices `c=0` and `c=0.5 N*s/m` predict `3 N` and `2 N`. Both reproduce the static test. A prediction of either body's acceleration therefore remains conditional on c; a supplied value or useful bound can settle a stronger question. A question about total momentum change can already be answered from the external forces, independently of c. The single test does not establish the assumed linear form.

With the response parameters and external forces `u1` and `u2` supplied, the connected evolution is

`x1' = v1;  x2' = v2;  m1*v1' = f+u1;  m2*v2' = -f+u2.`

Adding the momentum balances gives `p' = u1+u2` for `p=m1*v1+m2*v2`. This removes the internal force from the total momentum change while retaining it in the relative motion.

The retained mechanical energy is

`H = (m1*v1^2 + m2*v2^2 + k*(x2-x1)^2)/2.`

Differentiating and substituting the evolution gives

`H' = u1*v1 + u2*v2 - c*(v2-v1)^2.`

For the ideal damper whose lost mechanical energy becomes internal energy `U`, add `U' = c*(v2-v1)^2`. Then `(H+U)'` equals the external mechanical power. Omitting `U` from the motion calculation assumes that its change does not appreciably alter the chosen mechanical response.

Take `m1=1 kg`, `m2=2 kg`, `k=3 N/m`, `c=0.5 N*s/m`, `x1=0 m`, `x2=1 m`, `v1=1 m/s`, `v2=-1 m/s`, and no external force. At that instant, `f=2 N`, the accelerations are `2 m/s^2` and `-1 m/s^2`, total momentum has zero rate of change, and mechanical energy decreases at `2 W`. These are useful initial consequences without computing a full trajectory.

**Changed preparation.** Body 2 is instead held at `x2=1 m` from before the initial instant, so `v2=0`. With the other initial values unchanged, `f=2.5 N`. The support supplies the reaction `u2=f`; body 1 accelerates at `2.5 m/s^2`. The selected pair now exchanges momentum with the support. Keeping the earlier `v2=-1 m/s` together with a fixed-position constraint would describe an inconsistent preparation. Suddenly clamping the moving body would be another physical problem, requiring an account of that transition.

The reusable move is to obtain motion by joining balances to a response and preparation, and to revise the relevant exchange when the connection changes.

#### PHY.6:5.2 - Obtain a total without solving its spatial distribution

Let `c(x,t)` be the concentration of one chemical species in a fixed region. Its prescribed velocity field is `u(x,t)`. Use diffusion coefficient `D>0`, a constant first-order consumption rate `k>=0`, and the flux law

`J = c*u - D*grad(c)`.

The species balance supplies

`partial_t(c) = -div(J) - k*c.`

These equations state the response assumptions: advection, Fickian diffusion and first-order conversion. Their applicability is a physical premise. Impose no flux of this species through the region's boundary, `J dot n = 0`, where `n` is the outward normal.

For the total amount `N(t)=integral_region c(x,t) dx`, integration of the balance gives

`N' = -integral_boundary J dot n dS - k*N = -k*N`,

and therefore `N(t)=N(0)*exp(-k*t)`. The requested total follows from its initial total and the stated boundary and reaction laws. Internal transport need not be solved. Consumption of this species can coexist with conservation of the atoms it transfers into products.

**Changed question.** A local concentration maximum requires the initial spatial distribution and its evolution. The total alone no longer answers. Alternatively, if the reaction rate varies with position, the total rate becomes `-integral_region k(x)*c(x,t) dx`; replacing it by a constant times `N` now needs grounds for that reduction. Return to the spatial distribution or a justified bound when the new use needs it.

This case shows how the intended consequence determines which physical relations must be completed. It also separates a global balance result from a local transport prediction.

#### PHY.6:5.3 - Detect an incompatible ideal connection before attempting a transient calculation

Two ideal linear capacitors have positive capacitances `C1` and `C2`. Their lower terminals share a reference conductor; their upper terminals are connected through a resistance `R>0`. The effective description neglects leakage, inductance and radiation. Let `v1` and `v2` be the upper-terminal potentials relative to the common reference, and let current `I` flow from capacitor 1 to capacitor 2.

Charge balances and the resistive response give

`C1*v1' = -I;  C2*v2' = I;  R*I = v1-v2.`

The total upper-plate charge `Q=C1*v1+C2*v2` is constant. The difference `delta=v1-v2` obeys

`delta' = -(1/C1+1/C2)*delta/R`.

Thus the difference decays with time constant `tau=R*C1*C2/(C1+C2)`, and both potentials approach

`v_final = (C1*v1(0)+C2*v2(0))/(C1+C2)`.

For `C1=1 F`, `C2=3 F`, `R=2 ohm`, `v1(0)=8 V` and `v2(0)=0 V`, the settled potential is `2 V`, `tau=1.5 s`, and `I(t)=4*exp(-t/1.5) A`, with time measured in seconds.

Stored electrical energy is `H=(C1*v1^2+C2*v2^2)/2`. Substitution gives `H'=-R*I^2`. Its initial and final values are `32 J` and `8 J`, so `24 J` is converted into other energy, here heat in the ideal resistance. More generally, the energy difference is

`C1*C2*(v1(0)-v2(0))^2/(2*(C1+C2))`.

**Changed connection.** Set `R=0` as an ideal connection from the initial instant. Its constraint `v1=v2` conflicts with the supplied unequal initial potentials. The smooth evolution above cannot simply start from them under that constraint. Recover the interaction that establishes the common potential when its current, duration or energy conversion matters. Resistance, inductance or electromagnetic emission may matter depending on the actual arrangement and interval; the ideal connection alone does not specify them.

If only the settled potential is needed, conserved charge together with the premise that the connected system settles can already supply it. A transient description is needed for a different question, such as peak current. Taking the positive-resistance time constant to zero does not remove the finite energy conversion. This is why changing an idealization can require revisiting both the preparation and the requested consequence.

### PHY.6:6 - Bias-Annotation

The examples use classical descriptions with explicit response laws. Their calculations are convenient for exposing balance, coupling and preparation. A stochastic, quantum or history-dependent response requires its own physical grounds and mathematical representation; the example equations do not supply those grounds.

Component descriptions can also make localized parts seem necessary. An account can instead describe a continuous medium through fields or many interacting constituents through collective variables. Choose the physical participants and the resolution of their description from the question.

### PHY.6:7 - Conformance Checklist

- The intended physical consequence and relevant preparation determine the scope of the construction.
- Each balance names the selected quantity, physical transfers and any production or conversion.
- Response and configuration relations supply the dependencies needed for the answer, with their physical grounds and conditions.
- Connected descriptions agree on exchanged quantities, signs, units and frames; consequential connection storage or dynamics remain represented.
- Independent initial and boundary conditions are compatible with the coupled relations, and dependent conditions are derived.
- The first consequence is obtained or a particular missing response or incompatible preparation directs the next work.
- Checks and further inquiry concern what can change the intended use; mathematical consequence, computational accuracy and physical adequacy remain distinguishable.

### PHY.6:8 - Common Anti-Patterns and How to Avoid Them

| Misstep exposed by the construction | Consequence | Repair |
| --- | --- | --- |
| Expect conservation to determine every rate | The momentum balance still lacks the connecting force. | Supply and qualify the interaction's response law. |
| Remove internal force from each body because it cancels in the total | The relative motion disappears from the description. | Combine balances for the total while retaining the force in the part equations. |
| Treat mechanical damping as destruction of total energy | The energy account misses heating and possible feedback on the response. | Identify the receiving energy form and retain its dynamics when it affects the answer. |
| Read a total as a spatial prediction | An integrated species amount is used to infer a local concentration peak. | Restore the distribution and the conditions its evolution needs. |
| Impose an ideal connection on incompatible initial values | The capacitor transient is undefined within the chosen smooth account. | Resolve the preparation or represent the establishing interaction. |
| Build a detailed transient before using a sufficient balance | Work grows although the settled value or total is already determined. | Derive the required consequence first and expand only where needed. |

### PHY.6:9 - Consequences

The construction makes a physical account easier to use and divide among contributors. A specialist can supply a response law or preparation condition while another derives or computes its consequence. The connection states what each contribution must mean for the combined result.

Balances expose some construction errors cheaply. They leave many response questions open, so a balanced model can still be physically inadequate. Complex constraints, unresolved responses or changing regimes can require more physical work before the desired prediction becomes available. A conditional result or a narrower consequence can remain useful during that work.

### PHY.6:10 - Architectural Rationale

Separating balances, response laws and preparation makes their different contributions recoverable. Balances restrict change; response laws add behavior; preparation selects admissible evolution. Combining these relations before imposing a solving order lets the same physical account support different mathematical questions.

The construction uses C.29.BB for common balance reasoning and adds the physical choice of interactions, response grounds and compatible preparation. MMP.10 and C.29.2 handle the subsequent formulation and obtaining of mathematical results. This division permits a return to the missing physical premise without treating every solver difficulty as a computational defect.

Energy-based composition is especially useful when storage, conversion and exchange dominate the question. Direct momentum, species or charge balances can be simpler for another consequence. A physical variational principle offers another way to derive motion when its premises apply. The balance-and-response route is selected here for the difficulty it resolves, without requiring one formalism for every physical account.

### PHY.6:11 - SoTA-Echoing

**How much physical description is needed to obtain a selected consequence?** Adopt the quantity-first construction supplied by C.29.BB and developed in :4.1-.3. For the species total in :5.2, integration of the balance gives `N(t)=N(0)*exp(-k*t)`. Constructing and solving the full spatial evolution gives the same total under the same laws and boundary condition, but additionally needs an initial concentration field and a way to obtain its evolution. If only the total is used, the integrated account preserves the answer with fewer needed inputs and operations. It deliberately gives up the spatial profile. A local-concentration question or a position-dependent reaction rate reopens that choice. A readily available spatial solution can also supply the total.

**How should a reusable physical account be composed?** Retaining simultaneous component relations, as in :4.4-.5, preserves their meaning when the analysis or connection changes. For the positive-resistance capacitor case, eliminating the common current into two explicit evolution equations gives the same response as the retained three relations. Keeping the charge balances and the resistive relation separately makes their different contributions available when the connection changes: the balances survive, while setting R to zero changes the latter into a voltage-equality constraint that also restricts the preparation. This accepts the extra task of solving simultaneous relations when reuse or changing connections makes it worthwhile. For an isolated explicit evolution already suited to the question, use that simpler form. Reopen the choice when a new connection introduces a constraint or a consequential store.

[Van der Schaft, Port-Hamiltonian nonlinear systems](https://arxiv.org/html/2412.19673v1) (2024 preprint, sections 1.1-1.2) supplies a contemporary synthesis of storage, dissipation and power-conserving interconnection, including differential-algebraic descriptions. Adapt its separation of these contributions to the physical assembly in :4.3-.4. Remark 1.3 makes an important limit explicit: replacing mechanical dissipation by an untracked internal-energy increase is conditional on the relevant thermodynamic feedback being absent. Adopt that qualification in the damper case. For the two-body case, direct momentum equations and their energy derivative already show motion and the conversion into heat. A port-Hamiltonian representation gives the same consequences under the same response laws and makes energy-preserving composition explicit. Adapt the storage/interconnection distinction without requiring the reader to construct that formal representation for this small problem. Its additional structure becomes useful when a later question needs systematic composition or passivity properties of several interacting parts. Reopen the chosen account when an omitted store or thermal feedback changes those consequences.

The [Modelica 3.7 equation rules](https://specification.modelica.org/maint/3.7/equations.html), especially section 8.6, distinguish simultaneous relations, initialization equations and numerical guesses. Its [connection rules](https://specification.modelica.org/maint/3.7/connectors-and-connections.html), section 9.2, give explicit equality and signed flow-sum constructions. Adopt these as a worked formal tradition for composable physical descriptions and consistent initialization. The physical reason for a connection and the adequacy of a response remain separate from language conformance. Retaining algebraic constraints avoids inventing a physical direction merely to obtain explicit state-derivative equations.

The current [Dyad component-construction tutorial](https://help.juliahub.com/dyad/stable/tutorials/creating-components.html) demonstrates reusable connector and response relations with separate analyses. Adapt that distinction so a reader can reuse the component relations for several analyses.

The three worked calculations are constructed examples under their stated idealizations.

### PHY.6:12 - Relations

- **C.29.BB:** constructs balances across chosen boundaries and distinguishes transfer from production.
- **B.5.TU, PHY.4 and PHY.5:** supply theory use, constraints on an unknown law and the choice of effective physical detail.
- **MMP.10 and C.29.2:** formulate the selected mathematical question and obtain its result; **MMP.9** supplies mathematical reduction when needed.
- **MMP.11:** represents the freedom left in a response law after applicable constraints.
- **A.3.3.TR:** supplies common construction and composition of relations between states; the present method supplies the physical response and preparation.
- **B.5.MPC** connects the consequence to the physical question; **B.5.MPC.R** repairs a failed connection among physical, mathematical and computational contributions.
- **PHY.1 and PHY.2:** use the constructed physical account for similarity and analogue construction.
- **C.11.DUA:** decides whether resolving another physical uncertainty can improve the work enough to justify the inquiry.

### PHY.6:End
