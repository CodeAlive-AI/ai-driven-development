## A.3.3.TR - Construct a Rule for State Change

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### A.3.3.TR:1 - Problem frame

Use this pattern when you can describe a situation's state but still need to work out how it can change. A connection limits two bodies' positions but leaves their acceleration to be determined. Each participant in a computation has a valid procedure, yet their interleaving can produce an unexpected result. A transformation preserves a mathematical property but can repeat forever.

**First useful move.** Choose one possible change and write which values it reads, which values it changes, what must hold for it to occur and which other values stay fixed during that step. For a participant that has saved a counter value r, its later write sets x' = r + 1. It need not produce x' = x + 1: another participant may have changed x since the read. This small rule exposes the lost-increment case in :5.1.

The Method constructs a rule relating states or describing their continuous evolution under stated inputs. “Allowed” means permitted by that model. The resulting rule can support a conditional calculation, reveal competing continuations or identify a missing interaction, operation or input. A.3.3 supplies the criteria for a U.Dynamics episteme and connects its state space, transition law and observation account.

The finite cases require ordinary arithmetic and conditions. The continuous case additionally uses derivatives and Newton's equation for a stated ideal mechanical model. Subject laws and operation semantics supply the content that the common construction combines.

If a suitable state-change rule already answers the question, apply it directly. When only compatible arrangements are needed, A.3.3.CC can supply that result before a rule of change is available. Use the present Method to construct or revise the rule, not as an extra reporting stage for every calculation.

### A.3.3.TR:2 - Problem

A state constraint and a transition rule answer different questions. Two connected carts may have to maintain a fixed separation; that condition permits many common accelerations. Forces and masses are needed to select one. Similarly, saying that a participant reads before it writes constrains local order but leaves several global execution orders possible.

A rule assembled from separately plausible statements can also be inconsistent or too permissive. An omitted unchanged value may become free to vary. Combining alternatives as if they had to occur together can eliminate legitimate behavior. Treating a desired invariant as an automatic filter can hide the very failure the model was meant to investigate.

The practical problem is to construct a connected account from which the needed changes follow, while keeping visible the choices and missing information that still affect the answer.

### A.3.3.TR:3 - Forces

| Force | Tension |
| --- | --- |
| Observable change and hidden steps | A large modeled step is convenient; intermediate reads, interactions or events may change the result. |
| Local rules and joint behavior | Each participant can obey its own rule while their combination violates the intended whole result. |
| Simultaneous relations and execution order | Coupled equations constrain values together; a computation must choose how to obtain a solution. |
| Constraints and interaction laws | A constraint excludes combinations, but additional laws may be needed to determine rates or successors. |
| Possibility, progress and probability | A rule can allow a result without guaranteeing eventual arrival or assigning its likelihood. |
| Detail and useful return | A complete model may be costly; one counterexample, conditional continuation or identified missing rule can already change the decision. |

### A.3.3.TR:4 - Solution

Construct the rule around the change that matters to the question. Recover the relevant subject operations or interactions, connect their effects and test the resulting continuation. Revise the state or step when that test reveals an omitted difference.

#### A.3.3.TR:4.1 - Choose the state, step and inputs

Name what changes and the observation or decision that depends on it. Recover the admitted states, using A.3.3.CC when their compatibility is still unresolved. Separate changing values, parameters held fixed and inputs supplied from outside the model.

Choose what counts as one step. A step can be one instruction, one transaction, an event, an observation interval or an interval of physical evolution. Say which intermediate effects the model retains. Declaring a read-and-write pair atomic is a substantive assumption about interference, as :5.1 shows.

Retain the values needed to apply the rule. A saved read and an instruction position can matter even when neither is visible in the final output. A mechanical law can require velocities as well as positions. If two cases described by the same retained values require different continuations under the same inputs, return to the state choice or retain the unresolved alternatives. A.3.3 supplies the prediction-sufficiency comparison.

For an interval of evolution, specify the inputs over that interval. One initial input value determines a later result only under an assumption such as a held input or a supplied input law. Distinguish that condition from the initial state.

#### A.3.3.TR:4.2 - Write each contribution as a relation

For a discrete action, write its enabling condition and its relation between the values before and after the action. A prime can mark an after-value: x is the counter before a write, and x' is its value after the write. State what remains unchanged when the action affects only part of the state.

An action may leave several after-values possible. Keep the relation broad enough to represent them. An expression x' = f(x,u) is appropriate when the supplied state and input u determine that after-value; a relation R(x,x',u) can retain several possibilities.

For continuous evolution, recover the subject laws relating quantities, rates and interactions. These may be written as differential equations, algebraic constraints and any event conditions needed by the model. Include the initial and boundary conditions that the selected law requires. With constrained bodies, identify the forces exchanged through their connection and combine the equations, as :5.2 demonstrates.

The form of an equation does not establish its physical applicability. Recover its domain meaning and conditions from the subject account. When that account is missing, name the missing relation and return the conditional result already obtainable.

#### A.3.3.TR:4.3 - Combine jointly active relations and alternative actions

Relations that must hold during the same modeled change are imposed together. For two coupled carts, both force equations and the fixed-separation condition hold together. The variables shared by those equations must keep the same meanings, reference frames and units.

Actions that provide alternative ways to take the next step are joined as alternatives. In the counter case, the next action can be an enabled read or write by either participant. Requiring every one of those actions in the same step would describe a different computation.

Check how participants interact through shared values. A local action's condition and effect refer to the global state at the selected step. If actions occur together, define their joint effect or derive it from the governing relations; textual order alone supplies neither simultaneity nor a conflict-resolution rule.

For equation-based modeling, keep the coupled relations available while choosing a computation. A solver's evaluation order is part of obtaining a solution. If the actual system has a communication delay, sequential update or other timing effect, represent that effect in the modeled rule. Modelica's instantaneous event semantics is one explicit modeling convention; it requires modeled delays when those delays matter.

A.22.CGUS can help expose alternative continuations and their conditions when that is the working question. The present construction supplies the rules used to judge those alternatives. The jointly applicable equations can also determine a single continuation.

##### A.3.3.TR:4.3.1 - Combine continuous evolution with events

When the model mixes continuous evolution and discrete events, state the flow law in each mode, where that flow is permitted, each event's condition and timing, and its reset relation. A reset specifies which values change and which remain continuous.

For a condition that triggers an immediate event, evolve only to its first occurrence. Stop the continuous segment, apply the event relations, and resume from the resulting state under the applicable law. Process an already-enabled immediate event before advancing time. If the reset enables another immediate event, resolve that event according to the model before resuming flow. Incompatible event relations or an unresolved sequence of instantaneous changes are reasons to return a model or computation limitation.

An event that is merely permitted has a different timing rule: retain the allowed waiting and choice. Where simultaneous events can conflict, supply their joint relation or a justified priority. The thermostat in :5.4 uses mandatory immediate switching and a reset that preserves temperature.

#### A.3.3.TR:4.4 - Derive a change and test the required property

Work one case far enough to obtain a successor, a rate, a short behavior or an obstruction. Substitute the resulting values into the jointly required relations. In a finite model, enumerate or explore enabled actions from an admitted start; in a continuous model, derive or compute the behavior needed by the question.

To establish that a property P holds throughout reachable behavior, one sufficient induction argument proves two obligations: P holds at the admitted starts, and every permitted step from any admitted state satisfying P preserves P. For continuous evolution, use the corresponding invariance argument for the selected law and domain.

If preservation fails, seek a reachable path to the failing transition or strengthen the assertion using properties of reachable states. A transition from an unreachable state can defeat this proof without exhibiting a behavior that violates P. A stronger assertion I closes the proof when the admitted starts satisfy I, every permitted step from a state satisfying I preserves I, and I implies P. If neither argument is available, return the unproved obligation. Keep the transition rule being investigated intact while repairing the argument.

For states {0,1,2}, start 0 and transitions 0->0, 1->2 and 2->2, P defined as x<=1 holds throughout reachable behavior. The transition 1->2 defeats direct preservation of P, but 1 is unreachable. The stronger assertion x=0 is preserved and establishes P. A path from an admitted start to a violation would instead be a counterexample to the claimed property.

A small test can find a violation; a claim covering all allowed behavior needs an argument or method covering that behavior.

Keep the intended property separate from the rule being examined. If the model is intended to reveal whether an implementation can overflow a buffer, silently clipping its successors to capacity removes that failure from the model. Derive a control rule that prevents overflow, model what happens at overflow, or narrow the claimed operating conditions with a stated reason.

When no successor is found, determine what that result establishes. A contradictory set of equations, a terminal state, a disabled action, a deadlock and an unsuccessful incomplete search call for different next moves. Return the first missing condition or demonstrated obstruction that matters to the present use; do not invent a successor to fill the gap.

#### A.3.3.TR:4.5 - Add selection, progress or probability only when needed

State what selects among remaining continuations: an input, a scheduler, a control choice, an unresolved environmental condition or a stochastic mechanism. If the current use needs only possibility or a counterexample, the alternative set may be sufficient.

For a progress question, supply the conditions needed to reach the intended result. An invariant can hold throughout an endless repetition. A decreasing nonnegative integer can establish termination for the Euclidean construction in :5.3; a concurrent protocol may instead require a scheduling or fairness condition. Describe what that condition demands of the participating system.

For a likelihood question, use a probability model over the relevant choices or behaviors. Counting alternatives alone gives a count. Different scheduler rules can assign different weights to the same six counter histories.

For a numerical calculation, name the approximation or update method used to obtain the model's consequence. Check the result at the resolution and accuracy the question needs. A numerical step can introduce behavior absent from the subject law; C.29.2 supplies the broader construction and comparison of computations.

#### A.3.3.TR:4.6 - Return the usable rule or the missing contribution

Return the rule with the state meanings, applicable inputs and conditions needed for its next use. Depending on the question, the first useful result can be a permitted continuation, an impossible transition, a counterexample, a sufficient bound or an identified missing law. Use that result in the calculation, design or explanation for which it was constructed.

If a changed question requires previously hidden steps, forces, state information or observations, reopen those contributions and retain the unaffected ones. B.5.MPC.R coordinates revision across the physical, mathematical and computational accounts. C.11.DUA helps decide whether resolving a remaining uncertainty can improve the choice enough to justify the work.

### A.3.3.TR:5 - Archetypal Grounding

#### A.3.3.TR:5.1 - Two correct local increments can lose a global increment

Participants A and B each read an integer counter and later write the saved value plus one. Individual reads and writes are atomic. Each participant reads before it writes. Initially x = 0.

Use the state x, positions pA and pB in the two local procedures, and saved values rA and rB after their reads. Positions 0, 1 and 2 mean before read, after read and finished. Initially pA = pB = 0 and rA = rB = 0; each participant overwrites its saved value before using it.

The four action rules are:

| Action | Enabled when | Changed values | Other values |
| --- | --- | --- | --- |
| ReadA | pA = 0 | rA' = x; pA' = 1 | x, pB and rB retain their values |
| WriteA | pA = 1 | x' = rA + 1; pA' = 2 | rA, pB and rB retain their values |
| ReadB | pB = 0 | rB' = x; pB' = 1 | x, pA and rA retain their values |
| WriteB | pB = 1 | x' = rB + 1; pB' = 2 | rB, pA and rA retain their values |

The next step is any one enabled action. From pA = pB = 0, six complete histories respect the local orders. ReadA, WriteA, ReadB, WriteB and its A/B reversal finish at x = 2. In the other four, both reads precede either write; both saved values are zero, so the final value is one.

The result identifies how interference defeats the intended total. Serializing the two read-and-write pairs or supplying an indivisible increment changes the transition rule and removes these lost-increment histories. If serialization introduces waiting, a claim of eventual completion still needs its scheduling conditions.

The ordering rules already suffice to exhibit failure. If a scheduler chooses uniformly among enabled actions at each step, the two serialized histories each have probability 1/4 and the other four each have probability 1/8; the lost-increment probability is 1/2. Uniform choice among the six complete histories instead gives 2/3. Choose and justify a scheduler model when a likelihood estimate is needed.

#### A.3.3.TR:5.2 - A fixed connection and two force equations determine acceleration

Two carts move on an ideal frictionless straight track. A massless rigid connector keeps their positions q1 and q2 at q2 - q1 = L. Their positive masses are m1 and m2. Signed external forces along the track are F1 and F2. The connector exerts equal and opposite signed forces, written -lambda on cart 1 and +lambda on cart 2.

The positional constraint alone permits many common motions. Differentiating the constant-separation condition gives v2 = v1 and a2 = a1 = a for compatible motion. Newton's equations for this ideal model give

    m1*a = F1 - lambda
    m2*a = F2 + lambda

Adding them obtains `a = (F1 + F2)/(m1 + m2)`. Substituting back gives `lambda = (m2*F1 - m1*F2)/(m1 + m2)`. The connection constraint and both interaction equations were needed to determine the common acceleration and exchanged force.

For m1 = 1 kg, m2 = 3 kg, F1 = 4 N and F2 = 0, the result is a = 1 m/s² and lambda = 3 N. Start with q1 = 0, q2 = L and both velocities zero. While the forces remain constant, q1(t) = t²/2 and q2(t) = L + t²/2 in metres when t is in seconds; both velocities are t metres/second.

These formulas provide a state-transition calculation for any chosen interval within those assumptions. If the forces vary, supply their time or state dependence before computing the motion. If the connector is elastic or has consequential mass, its constitutive and interaction account changes the rule. Choosing smaller numerical time steps cannot supply that missing physical relation.

The calculation combines the physical interaction account, mathematical constraints and an executable rule. It also shows why reducing to one position can simplify motion prediction while retaining the connector force lets a designer determine the load on the connection.

#### A.3.3.TR:5.3 - Preserving a value and making progress require different arguments

For nonnegative integers a and b with `a >= b > 0`, use integer division `a = k*b + r`, where k and r are integers and `0 <= r < b`. Take the transition `(a,b) -> (b,r)`. Every common divisor of a and b divides `r = a - k*b`; every common divisor of b and r divides `a = k*b + r`. The integer quotient makes both implications valid. The transition therefore preserves the common divisors and hence the greatest common divisor. At `b = 0`, stop and return a.

From (30,18), the successive states are (18,12), (12,6), (6,0). The terminal result is 6. The second component is a nonnegative integer and decreases at every nonterminal step, establishing termination.

By comparison, repeatedly swapping the two arguments also preserves their greatest common divisor but can alternate forever. Preservation alone did not establish progress. The Euclidean rule adds the remainder operation and a decreasing quantity.

This is a transition account for a mathematical construction. An implementation must supply integer operations with the assumed meanings; using a bounded machine representation introduces its own arithmetic conditions.

#### A.3.3.TR:5.4 - A switch changes the law within the prediction interval

Consider a stated temperature model with T in degrees Celsius and heater mode OFF or ON. While OFF, temperature falls at 1 degree/minute; while ON, it rises at 2 degrees/minute. OFF at T<=18 switches immediately to ON. ON at T>=20 switches immediately to OFF. A switch changes the mode and preserves T.

Start at T=19, OFF. The requested result is temperature and mode at 1.5 minutes. In OFF mode, flow is permitted while T>18. The trajectory T(t)=19-t reaches 18 at minute 1; the event then switches the mode to ON. The new law gives T(t)=18+2*(t-1) until T reaches 20. At 1.5 minutes the result is **19 degrees, ON**.

At minute 2, the upper-threshold event switches to OFF; the next segment uses T(t)=20-(t-2). This continuation follows from retaining the mode and restarting the evolution after each event.

Keeping the initial OFF law through the whole first interval would give 17.5 degrees. Checking the switch only at the interval's end describes a controller that samples at those times, with different behavior from the supplied immediate-event model. A real controller's sampling or delay therefore belongs in its modeled timing.

### A.3.3.TR:6 - Bias-Annotation

The continuous example uses an ideal Newtonian model with supplied masses, forces and constraints. Its simplicity makes the common construction visible; another phenomenon needs its own interaction account. The concurrent example assumes atomic reads and writes and makes interleaving observable at that scale. Choose the granularity from the interactions and intermediate effects that can change the answer.

Finite examples can make complete exploration look inexpensive. Large state sets and continuous systems may require abstraction, symbolic reasoning, approximation or a less detailed conclusion. The Method permits a useful conditional result before that larger work.

### A.3.3.TR:7 - Conformance Checklist

- **CC-A3.3.TR-1 - Working change.** The subject, needed result and modeled step are recoverable.
- **CC-A3.3.TR-2 - State and inputs.** The rule retains the values it reads, separates held parameters and states input assumptions over the interval being modeled.
- **CC-A3.3.TR-3 - Connected effects.** Jointly required relations share their variable meanings; alternatives remain alternatives; unchanged values are stated where omission would permit unintended changes.
- **CC-A3.3.TR-4 - Subject contribution.** The physical interactions or operation semantics used by the rule are supplied, or their absence is the returned limitation.
- **CC-A3.3.TR-5 - Worked consequence.** An application obtains a continuation, rate, behavior, obstruction or missing contribution relevant to the question.
- **CC-A3.3.TR-6 - Required property.** A claimed invariant or progress property has the corresponding argument over the claimed cases. A failed induction step is distinguished from a reachable violation; testing and incomplete search retain their actual reach.
- **CC-A3.3.TR-7 - Choice and likelihood.** A selection, progress or probability claim has its own needed conditions.
- **CC-A3.3.TR-8 - Changed use.** A change to granularity, constraints, inputs or subject laws reopens the affected rule and its consequences.

### A.3.3.TR:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it changes the result | Repair |
| --- | --- | --- |
| Replace saved-value updates with updates of the current value | Interference between read and write disappears from the model. | Retain the saved value and instruction position, or justify an atomic operation. |
| Conjoin alternative actions | The model demands incompatible changes at once and can lose legitimate executions. | State the alternatives and the condition enabling each one. |
| Leave a local action's other state values free | A model can introduce changes no participant performs. | State the unchanged values or the joint action that changes them. |
| Filter away violations of the property being investigated | The model excludes the failure instead of explaining whether the implementation prevents it. | Model the behavior or derive the prevention rule, then test the property. |
| Infer progress from preservation | An invariant can hold in a cycle with no useful completion. | Supply a decreasing measure, scheduling condition or other relevant progress argument. |
| Repair a missing interaction law by changing a numerical setting | The computation still lacks the relation needed to determine the modeled change. | Repair the subject account and then select a computation for it. |

### A.3.3.TR:9 - Consequences

The reader can obtain a connected rule from local contributions, expose interference or missing interactions, and choose a useful return before constructing a larger model. The same construction makes assumptions about step size, inputs, alternative selection and progress available for revision.

The result's usefulness depends on the supplied subject account and the distinctions retained in the state. Extending the prediction horizon or changing what is observed can require more state information or a different approximation.

### A.3.3.TR:10 - Architectural Rationale

The independently useful result is a rule for modeled change. Configuration construction establishes compatible arrangements; prediction sufficiency asks whether retained information supports the needed future distinction. Neither contribution by itself connects the interactions and operations that produce allowed continuations.

A relational description keeps joint constraints and unresolved alternatives available before a computation chooses how to solve or explore them. This supports physical, mathematical and computational reasoning together. It also lets a reader alter the inputs or seek a different unknown without discarding the already useful relations.

Atomic actions, continuous equations, event resets and stochastic transitions have different semantics and can use different temporal scales. Their shared construction requires explicit participating quantities and effects; their specialized solution and validation Methods retain the substantive differences.

### A.3.3.TR:11 - SoTA-Echoing

**Working question and selected answer.** How can a reader construct a rule when several local operations or physical interactions jointly determine the change? The selected best-known line keeps their state relations available, combines jointly applicable relations, and retains alternative actions until the question or model selects among them. A serious alternative is a directly executable update procedure with a fixed order. That procedure is cheaper to apply when its order and effects already describe the required behavior; :1 therefore permits direct use of a suitable existing rule.

For the interference question in :5.1, choosing one execution order loses the alternative histories that can defeat the total. Retaining saved values and local instruction positions costs additional description and exploration, but a single lost-increment history already answers whether failure is possible. For the load question in :5.2, retaining the connection force makes that result calculable; eliminating it is useful when only motion is needed. The selected trade-off is to keep the relations and alternatives that can change the requested answer, and to stop at a sufficient result. **Adapt:** :4.1–:4.3 construct those contributions, :4.4 derives the consequence, and :4.5–:4.6 limit stronger claims and additional work.

**Discrete operations and proof.** Lamport's [Specifying Systems](https://lamport.azurewebsites.net/tla/book-02-08-08.pdf), chapters 2–3 and §5.7, supplies before/after actions, unchanged values and the distinction between reachable invariance and an inductive assertion. **Adopt** these constructions in :4.2–:4.4 and :5.1. TLA's stuttering and fairness conventions serve their stated modeling purposes; choose progress assumptions for the use in :4.5.

**Constrained interaction.** Tong's [Classical Dynamics, §2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) compares generalized coordinates and constraint-force treatment. **Adapt** the latter in :4.2 and :5.2 to retain the exchanged force when it is needed. Reduced coordinates offer a serious simpler alternative for motion alone. The cart derivation is an authored Newtonian case with its idealizations stated; another physical theory must supply its own relations.

**Coupled equations and events.** The [Modelica Language Specification 3.7, chapter 8](https://specification.modelica.org/maint/3.7/equations.html) supplies simultaneously satisfied equations, event semantics and consistent initialization. Its [DAE representation](https://specification.modelica.org/maint/3.7/modelica-dae-representation.html) separates continuous evolution and event processing: halt at a detected event, resolve its relations and restart integration. **Adapt:** :4.2–:4.3 keep joint relations distinct from evaluation order; :4.3.1 and :5.4 teach the continuous/event passage. Modelica supplies one explicit instantaneous-event convention; actual delays enter the model when consequential.

The joint Method is a conceptual synthesis whose comparison is supported by these constructions and their stated uses. Reopen the choice if a competing construction retains the same consequential continuations or interaction result at lower effort, or if an observed missing interaction, intermediate effect or event defeats the selected rule. Further Methods develop efficient exploration, proof, differential-equation solution and protocol design when the constructed rule requires that work.

### A.3.3.TR:12 - Relations

- **A.3.3 - U.Dynamics** identifies a supplied state-and-law account and compares retained information with the prediction being attempted.
- **A.3.3.CC** constructs the compatible configuration description from which state-change work can begin.
- **B.5.FM** constructs a first model for the working question; **B.5.MPC** connects the physical, mathematical and computational contributions.
- **B.5.MPC.R** revises the affected contributions when the question or conditions change.
- **A.22.CGUS** exposes alternatives and case conditions when continuation comparison is needed.
- **C.29.1** compares mathematical representations for the operations they preserve; **C.29.2** constructs the computation that obtains the needed result.
- **C.11.DUA** selects worthwhile additional information and support for the decision being made.

### A.3.3.TR:End
