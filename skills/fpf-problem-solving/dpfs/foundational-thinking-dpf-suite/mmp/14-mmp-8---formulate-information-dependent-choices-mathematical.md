## MMP.8 - Formulate Information-Dependent Choices Mathematically

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use

### MMP.8:1 - Problem frame

Use this pattern when a mathematical problem mixes quantities you may choose with quantities you do not control, or when a proposed solution depends on information that arrives too late. A solver can find a configuration for each possible circumstance while leaving you unable to select one in advance. A simulation can show a successful continuation because it chose an environmental value that the acting system cannot choose.

Begin with one proposed action. Ask what will be known when it must be chosen, which quantities remain outside that choice, and what result the action must achieve. Construct two possible circumstances that look the same at that moment. If the proposal assigns different actions to them, it needs another observation, a different decision time or a different policy.

The result is a mathematical formulation of the available choices and the requirement they must satisfy, including their dependence on information. It can establish a feasible fixed choice, a policy, a counterexample to the proposal or the missing contribution. This is a general modeling method for design, prediction and control questions. It develops the formulation before a solver or a control algorithm is selected.

The finite examples need elementary sets, inequalities and the meanings of 'there exists' and 'for every'. More demanding cases can require optimization, stochastic processes or control theory. If the answer condition and available information are already correctly formulated, use C.29.2 or the applicable computational method to obtain the result.

### MMP.8:2 - Problem

A mathematical unknown can represent a decision, an unobserved state, an external input or a quantity constrained by other relations. Treating every unknown as a free decision lets the solution change the problem's circumstances to make the requested result possible.

Timing introduces another error. A family of solutions indexed by the true circumstance can be mathematically valid while requiring an observation that the acting system never receives. Separately optimizing every future case then grants foresight that the described method lacks.

The difficulty is to translate the work's choices, information and requirements into a mathematical question with the corresponding dependencies and quantifiers.

### MMP.8:3 - Forces

| Choice | Consequence |
| --- | --- |
| One decision or an adaptive rule | An adaptive rule can use later observations but needs a realizable way to receive and act on them. |
| Possible success or required success | A successful case can support possibility while leaving a guarantee unresolved. |
| Unknown state and random state | An uncertainty set permits several values; probabilities require an additional model. |
| Strong requirement and useful feasibility | A guarantee across an oversized circumstance set can reject useful choices; changing the set changes the claim. |
| Mathematical existence and an obtainable rule | A policy's existence can matter before an affordable construction is known. |

### MMP.8:4 - Solution

Separate choices from circumstances, express the relations that must hold, and state which information each choice may use. Formulate the requested result over those objects, then test the formulation against a small contrasting pair of circumstances. Preserve any useful conditional answer when a stronger requirement is unavailable.

#### MMP.8:4.1 - Name choices, circumstances and consequences

Start from the question in the work. Identify what a participant can change and what is supplied by the subject or environment. Let a denote the choice and w the circumstance. Give both their domains and meanings. A choice can be an arrangement, an input, a rule for later actions or another object the work can construct.

Use the subject relations to connect them to a result. For a deterministic model, a consequence may be written y=f(a,w). An implicit relation R(a,w,y) can retain several possible consequences. Additional unknowns can describe forces, flows, internal states or other quantities jointly constrained by the model. Acausal equations can constrain these quantities without making them free controls.

State what the question requires of the result. If it asks whether every permitted behavior meets a condition, a solver's ability to find one favorable y does not settle it. If the work can select among the permitted consequences, represent the mechanism that gives it that choice. A.3.3.TR supplies the relevant state-change or interaction rule.

#### MMP.8:4.2 - Recover the order and availability of information

Describe what is observed before each decision and what arrives afterward. Express the available observation as h(w) when it is a deterministic description of the circumstance. It may reveal only part of w. For a random or noisy observation, specify its probability law for each admitted w. An unknown fixed w can index a family P_w of observation laws without having a probability distribution itself. A joint law is needed when the question also treats w as random and averages over it. MMP.7 constructs the recording law.

A policy pi selects an action from the information available: `a=pi(h(w))`. Two circumstances with the same h(w) must therefore receive the same action. This uses MATH.2's condition that an answer remains constant on cases identified by a description. Here the observation determines those groups. The information restriction is often called nonanticipativity: the policy does not use distinctions the decision-maker has yet to observe.

For repeated interaction, use the observation history available at each decision. A policy may remember earlier observations or actions. Omitting that memory is a substantive model choice. Global termination is unnecessary when the question concerns a continuing response; specify the response or progress condition that matters under the admitted inputs.

If an earlier action changes what can be observed, make h depend on that action and describe the cost and timing of observation. If action also changes the circumstance distribution or evolution, include that relation. C.28 supplies the causal-use question and the policy's permitted pre-action information; C.28.MR constructs the mechanism replacement. A changed distribution cannot be inferred from a favorable selection of historical cases alone.

#### MMP.8:4.3 - State the required quantifiers and performance criterion

For a deterministic success condition G(a,w), these are different questions:

| Working question | Mathematical statement |
| --- | --- |
| Is there some successful combination? | There exist a and w with G(a,w). |
| Does every circumstance have a successful action, if it were known? | For every w, there exists a with G(a,w). |
| Can one action be selected now that succeeds throughout the admitted circumstances? | There exists a such that, for every w, G(a,w). |
| Can an observation-dependent rule succeed throughout those circumstances? | There exists an allowed policy pi such that, for every w, G(pi(h(w)),w). |

Choose the statement from the work's requirement. The first two can expose possibilities or limits even when the latter two fail. A stronger claim can require a different action or information source.

When the receiving use permits failures with a stated probability, name the event and the randomness over which that probability is calculated. For unknown fixed w and random observation O, the question may require `P_w(failure of pi(O)) <= epsilon` for every admitted w. If w itself is modeled as random and the question concerns performance averaged over circumstances, use the joint law of w and O. An expected cost needs the same choice of what is averaged. Neither a probability nor an objective follows just from listing possible circumstances. Feasibility, expected performance, tail risk and worst-case performance are alternative questions with different consequences. Use the common choice and characterization methods to decide which matters to the work.

Preserve dependence within the circumstance set. Independently combining several ranges can create impossible circumstances and overstate a requirement. Conversely, excluding an inconvenient circumstance changes the range of the conclusion and needs a subject reason or an agreed narrower use.

#### MMP.8:4.4 - Construct or refute a usable choice

For each circumstance w, let A(w) be the actions satisfying the requirement under the modeled relations. For a fixed robust choice, seek an action in the intersection of A(w) over the admitted circumstances. An empty intersection refutes that fixed-choice requirement.

For an observation-dependent choice, group circumstances by the observation they produce. For each obtainable observation o, intersect A(w) over the circumstances with h(w)=o. An action in this intersection works throughout that observationally indistinguishable group. In a finite problem, choosing one such action for each observation constructs a policy. One empty intersection proves that this observation cannot support the required policy.

For a noisy observation and an all-cases guarantee, construct the allowed pairs (w,o) from the observation mechanism's admitted realizations. This relation, rather than a positive probability for each individual report, determines compatibility. For example, if O=w+E with E uniform on [-1,1] and all errors in that closed interval are admitted, the boundary error E=1 remains in an all-cases guarantee despite having probability zero. An almost-sure or specified-probability requirement is a different claim; state that choice.

For a received report o, first check that at least one circumstance is compatible with it. If none is compatible, return the conflict between the report and the observation model under C.16.IR:4.4. A universal statement over an empty set supplies no guarantee for the situation that produced the report. With a nonempty compatible set, intersect A(w) over its members. For a probability-of-success requirement, instead calculate the event under the conditional family or joint law chosen in :4.3; the set of allowed pairs alone supplies no probability weights.

For infinite spaces or long-running interaction, these relations still specify the question, but a usable policy requires the corresponding mathematical and computational construction. A pointwise existence argument does not automatically provide an effective rule. C.29.2 addresses that obtaining work; the present method retains the information restrictions in what it asks the computation to produce.

When several outcomes remain possible for one action and circumstance, apply the required quantifier to those outcomes as well. Derive or inspect a violating outcome when refuting a guarantee. If the missing factor is an unmodeled selection mechanism, obtain it or retain the conditional answer rather than allowing the solver to invent a favorable mechanism.

#### MMP.8:4.5 - Interpret the result and change the working method

Follow the resulting action or policy through one modeled case and a consequential change. Return the consequence to the original requirement. If a planned response depends on a distinction absent from the available observation, revise the observation, defer the decision, choose a more tolerant action or change the stated goal with the responsible party.

Compare these options by what they change and cost. A more informative observation can enlarge the feasible policy set, but it may arrive too late or cost more than a sufficient fixed choice. C.11.DUA supplies that comparison. An infeasible guarantee can still leave a useful bounded, conditional or risk-qualified proposal.

For a working-method change, explain who or what supplies the observation, what result it provides, when it becomes available and what the receiving action does with it. B.1.5.CM constructs the proposed Method whole; C.32.MWA.PP connects its execution with the available performers and provision. The mathematical policy then describes an obtainable contribution, rather than relying on an unstated observer or decision-maker.

### MMP.8:5 - Archetypal Grounding

#### MMP.8:5.1 - Choose a preload before or after learning an external load

An ideal static arrangement has a downward load w, an adjustable upward preload a and a residual y=w-a. A later use requires `abs(y)<=1/4`. The load is either 1 or 2, and a can be any value from 0 to 2. The relation is a supplied illustrative mechanical model; the pattern's work is to formulate the choice and its information.

If w=1, acceptable choices form `[3/4,5/4]`; if w=2, they form `[7/4,2]` after the actuator limit is applied. Both sets are nonempty, so each known load has a feasible choice. Their intersection is empty. No one preload chosen before distinguishing the loads can meet the requirement for both.

Suppose a reading available before adjustment reports which of the two loads is present. The policy `a=w` then meets the requirement. A reading received only after the preload is locked cannot support that policy at the relevant decision.

Now the tolerance is relaxed to 3/5. The acceptable intervals overlap from 7/5 to 8/5, so `a=3/2` works before any reading. Additional measurement is unnecessary for this revised requirement. The change is in the required result, not the sophistication of the computation.

#### MMP.8:5.2 - Decide which participant gets a scarce resource

Two work requests, L and R, may need the only available resource. Exactly one needs it. Allocation succeeds when the resource goes to that request. The instruction must choose L or R deterministically from one report received before allocation.

With no distinguishing report, there are two constant instructions: always allocate to L or always allocate to R. Each fails in one circumstance. A truthful timely report permits an instruction that follows it and succeeds in both. A report arriving after allocation cannot supply that choice.

Now the timely report is noisy. The observing procedure independently chooses one of two channels with equal probability, then sends its L/R report without naming the channel. The model supplies these conditional reporting probabilities; the remaining probability in each row produces the opposite report:

| Channel | Actual request needing the resource | Probability of a correct report |
| --- | --- | ---: |
| 1 | L | 0.9 |
| 1 | R | 0.5 |
| 2 | L | 0.7 |
| 2 | R | 0.9 |

Use MMP.7 to remove the unrecorded channel by summing over it. For fixed circumstance L, `P(report L)=0.5*0.9+0.5*0.7=0.8`. For fixed R, `P(report R)=0.5*0.5+0.5*0.9=0.7`. No probability for which request actually needs the resource was needed for this construction.

There are four deterministic instructions from one two-valued report:

| Instruction | Success probability in fixed L | Success probability in fixed R |
| --- | ---: | ---: |
| Always allocate to L | 1 | 0 |
| Always allocate to R | 0 | 1 |
| Follow the report | 0.8 | 0.7 |
| Choose opposite to the report | 0.2 | 0.3 |

If the requirement is success probability at least 0.65 in each admitted circumstance, following the report satisfies it. None of these instructions gives a zero-failure guarantee. The conditional laws are sufficient to make both statements while the circumstance remains unknown and fixed.

Change the question to average success in a stream of requests modeled as L with probability 0.95 and R with probability 0.05, retaining the channel procedure. Following the report gives `0.95*0.8+0.05*0.7=0.795`. Always allocating to L gives 0.95; always allocating to R gives 0.05, and choosing opposite to the report gives 0.205. The instruction with greatest average success among the four is now always L. It still fails in fixed R.

Choose the performance requirement from the work's purpose before adopting an instruction. The observing model supplies conditional probabilities; the decision about the work determines whether performance in each circumstance or an average matters.

To retain the zero-failure requirement, the work could obtain a truthful report in time or provide enough resource to serve both requests. Compare the cost of those changes with the consequences of accepting a mistaken allocation, using C.11.DUA. A changed channel, recorded channel identity or permission to randomize the instruction changes the information or choice set; formulate the revised question accordingly.

#### MMP.8:5.3 - Find a strategy, rather than an answer chosen with future knowledge

A program repeatedly receives a bit b and emits a bit a. A requirement asks it to emit the same bit. If receipt precedes emission, the rule `a=b` works on every round. If emission must precede receipt, each possible future bit has a matching answer, but no deterministic rule using only the earlier history can guarantee a match against every admitted next bit.

To see the failure, hold the earlier history fixed. The rule chooses either 0 or 1. Both next input bits are still admitted, including the opposite one. That continuation refutes the guarantee for this history. Inspecting more successful traces cannot remove it.

A changed requirement may ask for success probability under independent fair input bits. Any earlier choice then matches with probability 1/2 in one round, including a randomized earlier choice independent of the next bit. Success in every one of N such rounds has probability 2^(-N). These probabilistic claims use the new input assumption. They do not establish success against every input stream.

This is a continuing computational interaction. The construction determines how each response may depend on incoming information. The same observation-order construction identifies what a distributed team or controller would need to know before acting.

### MMP.8:6 - Bias-Annotation

Optimization tools encourage viewing every variable they can assign as an available choice. Recover the subject meaning of each unknown before interpreting a solution. A second bias is to make robustness the default goal. State the receiving requirement first; a conditional answer or an explicitly accepted risk may be more useful than an infeasible all-circumstances guarantee.

### MMP.8:7 - Conformance Checklist

- Are choices, circumstances and consequences distinguished by what the acting system can actually change?
- Does each choice depend only on information available at its decision time?
- Do the quantifiers express the intended possibility, guarantee, policy or probabilistic question?
- Are dependent circumstances and remaining possible outcomes preserved in the formulation?
- Does a witness, empty intersection, policy or bound have the claimed meaning?
- Does the interpreted result support an action, a changed method or a specific unresolved contribution?

### MMP.8:8 - Common Anti-Patterns and How to Avoid Them

| Failure in this work | Repair |
| --- | --- |
| A solver changes an external load or unknown state to satisfy the goal. | Treat it as a circumstance and apply the required quantifier. |
| A separately optimal action for every future is presented as one available strategy. | Group cases by the information available at the decision; require a common action within each group. |
| An existentially chosen consequence stands in for all allowed behavior. | Retain the behavior relation and test the quantifier required by the goal. |
| A larger uncertainty set is called safer without examining its subject meaning or cost. | Check the joint possible circumstances and choose the requirement for the actual use. |
| Better observation is required after a sufficient common action is already available. | Compare what the additional information can change before commissioning it. |

### MMP.8:9 - Consequences

The formulation prevents computation from supplying unavailable control or foresight. It can expose a useful change to observation, timing or the requirement before optimization begins. It can also be harder to solve than its scenario-wise surrogate; that extra difficulty reflects the question the work actually asked.

### MMP.8:10 - Architectural Rationale

Quantifier order and permitted dependence express different aspects of the working problem. 'For each circumstance there is an action' concerns a family of possible solutions. An executable policy also needs a way to select its action from obtainable information. Grouping indistinguishable circumstances makes that additional condition visible and gives a constructive test for finite cases.

This mathematical formulation can describe physical adjustment, resource allocation or computational interaction. Its source premises and available actions differ across those practices. The method keeps those differences explicit while reusing the same reasoning about choices and information. It complements FPF's continuation and computation methods by constructing the mathematical answer condition they consume.

### MMP.8:11 - SoTA-Echoing

[Boyd and Vandenberghe, Convex Optimization, section 4.1](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), distinguish the feasible set from the objective and transformations of a problem. Adopt that separation in :4.1 and :4.3. The present finite constructions do not require convexity; the book's convex solution guarantees apply only under their conditions.

[Ben-Tal, Goryashko, Guslitzer and Nemirovski, Adjustable robust solutions of uncertain linear programs (2004)](https://doi.org/10.1007/s10107-003-0454-y), develop adjustable decisions alongside choices fixed before uncertainty is revealed. Adapt this distinction into the information-dependent formulation; do not transfer linear-program tractability to unrestricted policies.

[Duchi, Optimization with uncertain data (2018), sections 1 and 6](https://web.stanford.edu/class/ee364b/lectures/robust_notes.pdf), compares uncertainty-set requirements with probabilistic ones and makes choosing the uncertainty set a modeling question. Adopt that choice explicitly; no worst-case objective is imposed by this pattern.

[Vayanos, Georghiou and Yu, Robust Optimization with Decision-Dependent Information Discovery, version 3 (2022)](https://arxiv.org/abs/2004.08490v3), treats actions that affect when uncertainty can be observed. Carry that extension into :4.2 and the return to method design. Its specialized algorithms are further methods, not assumed capabilities of every reader.

The interval, allocation and bit-response examples are constructed demonstrations of the method under their stated assumptions.

### MMP.8:12 - Relations

B.5.FM and C.29 connect the work's question to its mathematical formulation. A.22.CGUS exposes allowed continuations; A.3.3.TR constructs the behavior relation. MMP.7 supplies a missing observation law for probabilistic uses. MATH.2 explains the identification of cases that preserve a requested answer; here grouping by available information determines which actions a policy can distinguish. C.29.2 obtains a computation for the formulated question and C.29.3 examines realization. C.28 governs causal claims when acting changes the represented world. B.1.5.CM uses the result to construct the composition of observing, deciding and acting Methods; C.32.MWA.PP compares the needed contributions, timing and provision.

MMP.8.SD refines this formulation for continuing decisions. It constructs a decision-sufficient state or belief, transitions and observations, and the relation between a present choice and its later consequences. Use that refinement when the one-step formulation leaves a consequential continuation unresolved.

### MMP.8:End
