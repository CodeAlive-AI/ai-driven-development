## DTM.4 - Find Conditions for Variant Invasion, Persistence and Return

**Type:** Method
**Status:** Stable

### DTM.4:1 - Problem frame

**Use this when** early growth, a fitted trend or a single threshold is being used to claim that a practice will establish itself, disappear, or return after an intervention.

A method may decline when few groups use it yet persist once compatible partners or supporting capabilities become common. A brief reduction can be followed by return to the same regime. A favorable gain from switching may still produce no uptake when no capable, authorized recipient receives the proposal.

The first result is a conditional account of possible continuation: whether a rare variant grows in a specified environment, what can maintain it, and what would change the reachable regime. Use the relevant mathematical methods to establish the properties of the chosen model; this pattern selects and connects the questions that a spread claim must answer.

For an immediate one-off choice with no reliance on persistence or later return, a comparison of the available actions may be sufficient.

### DTM.4:2 - Problem

“Increases now,” “can establish,” “persists under present conditions” and “cannot be reversed” are different claims. Local growth does not settle long-term coexistence. A stable regime need not attract every admissible initial condition. A mathematical equilibrium at zero remains possible even when a nonzero introduction would grow.

A threshold without its governing event law, surrounding state and admissible initial conditions can therefore support the wrong intervention.

### DTM.4:3 - Forces

| Force | Tension |
| --- | --- |
| A decision needs a useful prediction | The available model may establish only a conditional possibility. |
| A rare-variant test is inexpensive | Reinforcement or several interacting variants can require a finite introduction. |
| Local stability summarizes nearby behavior | Large changes and delayed feedback can cross its boundary. |
| A response changes current prevalence | It may also change the environment in which another variant can establish. |

### DTM.4:4 - Solution

**Specify the surrounding regime, test growth from rarity, find maintained regimes, then examine reachable change and return.**

#### DTM.4:4.1 - Preserve the law and the surrounding conditions

Recover the transmission and uptake construction from DTM.2 and the relevant feedback from DTM.3. Identify the variables being varied and those held fixed, the feasible state region, units of time and the environmental conditions. Keep the counted event and eligible population unchanged across that handoff. A per-recipient probability or hazard, a repeatable-event count and a population flow are different inputs; convert them using the stated receiving event before analyzing regimes.

State the practical question before solving: establishment from a small introduction, persistence of an existing variant, coexistence, reduction to a desired range, or return after a temporary change. “What happens?” is too broad when those questions depend on different initial conditions.

If a capability, permission or resource required for uptake is absent, preserve that absence in the law. A favorable comparison is not itself an event.

#### DTM.4:4.2 - Test a rare variant in a specified resident regime

Place the proposed variant at a small positive amount in an otherwise specified regime. Determine its initial growth from the modeled receiving events and losses.

For one rare quantity y, a local form y'=r y plus smaller terms gives growth when r>0 and decline when r<0. r concerns this surrounding regime and these assumptions. If r=0 or the neglected terms can dominate at the relevant scale, the first-order test does not decide.

With several linked rare states, use the appropriate coupled linearization or generation-to-generation operator supplied by the mathematical modeling method. Do not assign one scalar “reproduction number” until its construction and threshold apply to that model.

A zero initial amount can remain zero in a deterministic model with no external introduction. The rare-variant test asks about a small positive amount; it does not predict that an introduction will occur.

#### DTM.4:4.3 - Find what can maintain the variant

Find admissible stationary or recurring regimes and determine their relevant stability. Retain coexistence, oscillation or continued replacement if the model supports those forms; persistence need not mean a constant population share.

Where reinforcement or compatibility matters, examine finite initial amounts as well as rarity. A rare variant can decline while a sufficiently established variant persists. In that case, identify what separates the continuations and whether the proposed action can cross that boundary.

Use analytical reasoning, validated numerical calculation or a justified qualitative argument at the formality needed by the decision. A solver's last point alone is not evidence of an attracting regime; check the event law, feasible region and behavior under relevant nearby conditions.

#### DTM.4:4.4 - Distinguish a temporary displacement from a changed law

Model what the contemplated action changes. A one-time alteration of current use changes an initial condition. Continuing support, a compatibility adapter or a revised recognition rule can change a rate or a dependence. A newly available variant changes the candidate set.

Follow the trajectory during the action and after its removal. Ask whether the post-action state remains in the same region of attraction, enters another one, or encounters a different law because capabilities, resources or variants have changed.

For an intended return, identify the route and means needed to realize it. Lowering a parameter is insufficient if a necessary alternative has been lost or an endpoint is invariant under the model. Use C.36.RP and the relevant domain method to obtain an unavailable contribution; do not invent it as a free change in the state variable.

#### DTM.4:4.5 - Express the result as conditional continuations

Give the conditions and their consequences together:

- the surrounding regime in which a rare variant grows or declines;
- the maintained regimes relevant to the question;
- initial conditions or interventions that distinguish reachable continuations;
- the observations or changed assumptions that would defeat the account.

Use the existing comparison and portfolio methods when several actions remain viable. DTM.1 preserves whose consequences are being compared. DTM.6/.9 reopen the law when another variant or protective response changes the surrounding regime.

Stop with the weakest supported claim that answers the practical question. A useful conditional threshold need not become an unconditional prediction, and a qualitative return may be enough to reject an ineffective intervention.

### DTM.4:5 - Archetypal Grounding

#### DTM.4:5.1 - Rare growth and persistence give different answers

Consider a constructed reversible uptake model for the share f using a practice. The modeled adoption flow is s f²(1−f): encounters must provide the reinforcement represented by f². The modeled abandonment flow is s θ f(1−f): access to alternative users contributes to departure. Thus:

~~~text
f' = s f(1−f)(f−θ),    0≤f≤1,    s>0,    0<θ<1.
~~~

The two flows are nonnegative on the stated region. Their forms are hypotheses for this example, not universal properties of social learning. With θ=0.4 and s=1 per chosen time unit, the fixed points are 0, 0.4 and 1.

For 0<f<0.4 the derivative is negative; for 0.4<f<1 it is positive. The endpoint regimes attract interior states on their respective sides, while 0.4 separates them. At f=0.2 the rate is −0.032; at f=0.6 it is +0.048.

The rare-variant test reports decline near zero. It does not establish that an existing majority will disappear. The model instead gives persistence from the higher initial range. The first useful result is this distinction, before any choice of intervention.

#### DTM.4:5.2 - A temporary reduction can be followed by return

In the same model, suppose an admissible action temporarily changes f from 0.8 to 0.5. When the action ends and the old law resumes, f increases again because 0.5 remains above 0.4. A displacement to 0.3 would instead place the trajectory in the lower range.

These statements do not establish an available or legitimate way to change f. They tell the project what a claimed temporary intervention would need to achieve under the model. Changing ongoing support would require a revised law, not a fictitious one-time jump.

The endpoints in this model are invariant: departure is absent at f=1 and uptake absent at f=0. If the actual practice permits independent departure, outside introduction or invention, add those processes before using the endpoint predictions. A change in the underlying event account may remove the threshold or replace the two regimes.

#### DTM.4:5.3 - Compatibility changes a threshold but does not guarantee uptake

Suppose a switching group bears conversion costs while old-standard partners keep their process unchanged. Over one horizon, its gain relative to continuing is g(f)=2−0.5−3(1−f), where f is the adopter share. Assume equally weighted encounters in a homogeneous population, so f also gives the group's relevant partner share on the new standard. The gain is positive only above f=0.5.

An available adapter costing 0.4 and reducing the conversion coefficient to 0.2 gives gₐ(f)=2−0.5−0.4−0.2(1−f). At f=0.2, g=−0.9 while gₐ=0.94.

This is a threshold of the group's comparison, not yet a population stability result. Add the explicit event rule that a fraction e of the remaining groups receive a feasible, authorized offer and adopt when the gain is positive. Then one step gives:

~~~text
f_next = f + (1−f)e × indicator(g>0).
~~~

For f=0.2 and e=0.25, the share remains 0.2 without the adapter and becomes 0.4 with it. For e=0, neither positive gain nor a favorable threshold produces uptake.

This constructed rule omits departure, unequal partners and changing expectations. To conclude persistence or reversibility, supply those mechanisms where they matter and repeat the corresponding question. ECO.8 retains the coordination and allocation of costs; the engineering method establishes compatibility.

### DTM.4:6 - Bias-Annotation

The term “invasion” denotes growth from a small positive presence in a specified model. It assigns neither moral value nor an instruction to spread something.

An attractive tipping-point narrative can encourage modelers to choose reinforcement in advance. Compare a simpler uptake law when the evidence does not establish it, and preserve the resulting difference in continuation.

### DTM.4:7 - Conformance Checklist

- The practical question distinguishes establishment, persistence and return.
- The resident state, feasible region and event law are identifiable.
- A rare-variant result is conditional on a specified surrounding regime and a nonzero introduction.
- Maintained regimes are distinguished from a trajectory's transient values; finite-introduction effects are examined where relevant.
- The proposed action changes an initial condition, law, resource or variant set explicitly.
- The result after action removal and any unavailable return contribution remain visible.
- A comparison threshold is not presented as proof of uptake, stability or authority.

### DTM.4:8 - Common Anti-Patterns and How to Avoid Them

**A positive trend proves inevitability.** Recover the surrounding regime and test the continuation that the claim actually needs.

**Rare decline proves eventual disappearance.** Examine persistence from established states when reinforcement or compatibility supplies a different regime.

**One successful reduction proves durable change.** Follow the post-action law and reachable state.

**A profitable transition occurs automatically.** Include exposure, means and authority in the event rule.

### DTM.4:9 - Consequences

The result can reject an intervention that only displaces the state temporarily, or reveal that a failed small introduction does not rule out persistence under different conditions. Its value depends on the event law and feasible actions; precise calculation cannot repair a missing mechanism.

### DTM.4:10 - Rationale

Establishment, persistence and return are related questions on one dynamic account, but they use different evidence. Keeping them together prevents a local calculation from answering a more expansive question by implication. Mathematical methods supply the analysis; the subject method keeps its conditions connected to the intended change in practice.

### DTM.4:11 - SoTA-Echoing

[Solé et al. (2026 preprint)](https://arxiv.org/abs/2609.03344) provide a current example of reinforcement producing multiple stable coupling regimes. This motivates examining establishment and persistence separately; the one-variable construction above is a different illustrative model, not a reduction or empirical validation of that paper.

The historical [Katz–Shapiro compatibility analysis (1985)](https://idv.sinica.edu.tw/kongpin/teaching/io/KatzShapiro1.pdf) shows why outcomes may depend on other adopters. A gain comparison does not supply an adoption process. The worked adapter construction adds its own explicit event rule and leaves stronger dynamic claims open.

The pattern uses existing mathematical stability and continuation methods. Its contribution is the linked subject inquiry from rare growth through maintained regimes to feasible return.

### DTM.4:12 - Relations

- **DTM.1** preserves the participants and consequence comparison.
- **DTM.2/.3** supply the event law, internal change and feedback.
- **DTM.5/.6** can change the resident composition or selection conditions.
- **DTM.8/.9** supply protective actions and their dynamic effects.
- **MMP**, relevant mathematical and computational methods perform the selected analysis; **C.36.RP** helps recover a contribution needed for an otherwise unavailable return.

### DTM.4:End
