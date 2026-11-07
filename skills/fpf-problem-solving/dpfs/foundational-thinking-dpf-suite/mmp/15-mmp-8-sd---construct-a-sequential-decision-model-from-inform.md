## MMP.8.SD - Construct a Sequential Decision Model from Information and Consequences

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative within the stated use.

### MMP.8.SD:1 - Problem frame

**Use this when a choice changes what can be done or learned later, and comparing its immediate result does not settle the useful course of action.** You might reserve a resource for a later request, inspect an unfamiliar document before choosing how to process it, or pursue a target whose attainment depends on several moves.

Start with two possible first actions. For each, write what becomes available before the next choice and what the next choice can change. This small decision tree often reveals the missing resource, remembered event or uncertainty that a proposed “current state” has discarded.

The object being constructed is a **sequential decision model**: a mathematical account connecting available information, allowed actions, subsequent observations and accumulated consequences. Its result lets a reader compare a present action together with an admissible continuation. A continuation is the later policy: a rule for choosing actions from the information available then.

This is the sequential refinement of **MMP.8 - Formulate Information-Dependent Choices Mathematically**. It retains that pattern's separation of chosen quantities, uncontrolled circumstances and information available at each choice. It adds the construction of a state sufficient for the selected decision problem and the relation between current action and remaining consequence. A short history tree is a valid starting model; a compact state becomes useful when the tree repeats questions or grows too large.

A reader can work the finite cases with conditional probability, finite sums and maxima, or with sets of possible outcomes. For continuous, constrained or indefinitely continuing models, the person supplying the mathematical argument needs the relevant preparation in stochastic control, decision theory or the applicable field. This can be the reader or an available specialist. Give a specialist the actual timing, allowable actions and consequence criterion; ask for the resulting model and its limitations.

**Not this pattern when** the useful comparison is already a single choice with no consequential continuation. Use MMP.8 directly. If the decision model is adequate and only its solution is expensive, the next work is computational. If the difficulty is deciding whose interests or which consequences should count, obtain that choice from the responsible people and the applicable decision or strategy practice.

### MMP.8.SD:2 - Problem

A record of the present can omit information that changes a later action's availability or value. A forecast can predict the next reading correctly while omitting an accumulated loss that matters at the end. A plan can also give its future decision maker information that will arrive too late.

These defects can survive accurate computation. Optimizing a model of the latest observation, a guessed hidden state or immediate payoff may return the best answer to a different problem. Conversely, retaining every observation and solving for every possible future can cost more than the decision warrants.

The modeling question is: **what information and consequence account make the present choice and its continuation comparable, under the actual conditions of use?**

### MMP.8.SD:3 - Forces

| Force | Tension |
| --- | --- |
| Useful memory | A compact state saves work, but merging histories can remove an allowed action or change its consequences. |
| Information timing | Later observations support conditional action, while a plan chosen now cannot depend on their unrealized values. |
| Present and later consequences | A locally attractive move may consume a resource, remove an option or change what can be learned. |
| Criterion choice | Expected total gain, probability of meeting a target and worst possible loss can prefer different policies. |
| Affordable adequacy | Exact reconstruction of the hidden state may be unnecessary; an adequate comparison or bound can already settle the use. |
| Model and computation | A correct solver can answer a deficient model, and an adequate model can remain computationally difficult. |

### MMP.8.SD:4 - Solution

Construct the information available at each choice, retain what determines the relevant continuation, and derive the accumulated consequence of a policy. Use that derivation to locate the premise responsible when a changed condition alters the answer.

#### MMP.8.SD:4.1 - Fix the decision times and the consequence being compared

Recover from MMP.8 the choices, uncontrolled circumstances and information available before each choice. Mark the order of observation, action, transition and consequence. Include delays, commitments and stopping opportunities when they change what can be done.

For decisions at times `t=1,…,T`, let `H_t` be the available history immediately before action `A_t`. It contains received observations and known previous actions. Include a realized gain or cost in this history only if the decision maker can know it then. A policy `π_t(H_t)` selects an allowed action from that history; randomization is an additional allowed operation when the problem permits it.

State the consequence criterion supplied by the receiving use. One common finite model maximizes

    J(π) = E^π[R_1 + R_2 + … + R_T + G].

Here `R_t` is the gain at decision step t, `G` is a terminal contribution, and the expectation uses the trajectory law induced by policy π and the model. Gains can be negative costs. Their addition presupposes a common meaning and scale. Specify the initial information or distribution under which policies are compared.

An expected sum is one choice of criterion. For a target such as “finish with at least k points,” the consequence can instead be the terminal indicator, equal to 1 when the target is met and 0 otherwise. Its expectation is the attainment probability. For several criteria, retain their comparison or trade-offs until an applicable choice method supplies a selection rule. A scalar “reward” does not decide that rule.

Use a horizon or stopping condition appropriate to the work. Assign the consequences left at the horizon, such as unused stock or unfinished obligations. A discounted sum gives later gains smaller weights; choose that meaning deliberately. Shortening a computational planning window does not make omitted consequences disappear.

#### MMP.8.SD:4.2 - Construct how an action changes the world and the available information

Write the transition and observation account for each allowed action. For a finite stochastic model, choose an underlying state X that retains the information needed for the transition account. One possible representation is the joint law

    K_t(x', y, r | x, a)
      = modeled probability of next state x',
        next observation y and current gain r
        when action a is applied in state x.

This representation assumes that, given x and the applied action a, the omitted history does not further change the law. Retain a missing historical distinction when that assumption fails. Using a joint law permits dependence between the transition, observation and gain. Factor it into simpler laws only when the model supports the corresponding conditional independence. A deterministic rule or a relation of possible successors can replace probabilities when that is what the available knowledge warrants.

Identify the source of these relations. A subject model supplies the consequences of applying the action; MMP.7 supplies how observations are recorded and become available. An intervention model through C.28.MR can supply the changed mechanism. A conditional association among logged actions and outcomes is not automatically the law under a new policy.

An action can change both the subject and what the next decision maker will know. An inspection might consume time, disturb an object and produce a reading. Include each effect that changes the policy comparison. If two participants receive different observations, preserve their separate information; a policy using all their private information would require a means of sharing it before the choice.

For a small problem, enumerate the allowed actions and possible next observations at each history. Label branches with probabilities or allowed circumstances and gains. This tree supplies a reference calculation before any compression.

#### MMP.8.SD:4.3 - Retain a state sufficient for the selected continuation

Propose `Z_t=s_t(H_t)`, a summary obtainable from the information available at time t. It may be an observed state, a history window, a set of possibilities or a belief: a probability distribution over the hidden state conditional on the available history.

When the retained state is a belief, A.3.3.PI:4.4 supplies its prediction and observation update under a specified model. Use that distribution and update here. Include uncertain fixed parameters or other remembered quantities when they affect future consequences. A point estimate can discard differences that change an action's value. A posterior over physical coordinates alone can also be insufficient when a resource budget or terminal target depends on the past.

For the expected additive criterion in :4.1, a constructive sufficient test compares any two admitted histories at the same decision time having the same proposed Z. For every action covered by the model, determine whether those histories give:

- the same allowed actions;
- the same conditional expected current gain;
- the same conditional law of the next retained state after the action.

At the terminal time, the conditional expected terminal contribution must also depend only on the retained state. Supply an initialization and an update from retained information, the action taken and the next received observation. These conditions let the continuation calculation use Z in place of the full history. They are sufficient conditions for this reduction, not a claim that every useful decision requires this much information.

The comparison covers the actions and histories for which the policy is to be used, including alternatives to the former policy. A match only along recorded behavior can hide distinctions that another action makes consequential. Predicting irrelevant observations is unnecessary when their differences affect neither the criterion nor future choices.

When the test fails, identify the missing distinction and repair the state. An unspent resource, elapsed time, accumulated amount or belief over an unknown mode can be the needed addition. If the repair is expensive, retain the history tree, restrict the claimed use, or use a bound sufficient for the present comparison. Two histories with different forecasts can still support the same action when that action dominates under both.

For an approximate summary, determine how its errors can change the action comparison. Carry errors in current gains and in expected continuation through the selected horizon, using an applicable bound or model criticism. If computed action values each have justified absolute error at most e relative to the intended model and criterion, a largest value more than `2e` above every rival has the same maximizing action. Without such separation, preserve the unresolved comparison or improve only the approximation that can change it. A small prediction error on a training sample alone does not supply this guarantee.

#### MMP.8.SD:4.4 - Derive current gain plus continuation

First evaluate a policy that selects its actions from the retained state. With a sufficient state, let `V_t^π(z)` mean expected gain from time t onward when the policy is followed, conditional on current retained state z. For a deterministic policy, the finite model gives

    V_(T+1)^π(z) = g(z)
    V_t^π(z) = r_t(z, π_t(z))
               + sum_z' P_t(z' | z, π_t(z)) V_(t+1)^π(z').

Here `g(z)` is the conditional expected terminal contribution, `r_t(z,a)` the expected current gain, and `P_t` the next retained state's law derived from :4.2–:4.3. A randomized rule averages the right-hand side over its action probabilities.

The equation follows by splitting the accumulated gain into the current term and the remaining terms, then conditioning on the next information state. Thus each action is compared with what can follow it, including the information then available.

For a finite state and action problem with nonempty allowed action sets, whose only policy restrictions are those local sets, the best attainable value satisfies

    V_(T+1)(z) = g(z)
    Q_t(z,a) = r_t(z,a) + sum_z' P_t(z' | z,a) V_(t+1)(z')
    V_t(z) = max over a in A_t(z) of Q_t(z,a).

An attaining action at each reached state defines an optimal policy for this model and criterion. Finite sets make these maxima attainable. For more general spaces, determine the relevant existence, measurability and integrability conditions. When a maximum is not attained, distinguish the supremum from any obtained approximate policy.

The order of choice and averaging matters. When a later observation is available before the next action, its branch can use its own continuation. A fixed action sequence cannot use that observation. At a common decision node, selecting a different action for each still hidden state would add unavailable information.

Retain restrictions coupling choices across histories or times. A total resource limit can often be represented by remaining resource in Z; a constraint on the whole policy may instead require a constrained formulation. Independently maximizing every node can violate a coupling that the state has omitted.

These equations define the mathematical continuation problem. CMP.3 supplies sharing and scheduling of repeated subcomputations; CMP.9 supplies a sampling procedure and the error of estimated expectations; CMP.5 can supply a relaxation, a usable policy and an improvement bound when its recovery conditions hold. C.29.2 supplies the wider computational formulation, including a continuing response rather than a terminating answer.

For indefinitely continuing use, first select a finite total, discounted sum, average rate or other well-defined criterion. For example, bounded per-step gains and a discount factor γ with `0≤γ<1` make the infinite discounted sum finite. A fixed-point or limiting equation then needs conditions appropriate to that criterion. A solver's convergence and a policy's consequences remain separate questions.

#### MMP.8.SD:4.5 - Match the continuation to the uncertainty and objective

When the available information is a set of possible circumstances, evaluate a policy over the permitted complete trajectories. Compare its worst consequence, an interval or another requested result without inventing a probability distribution.

A stage-by-stage worst-case calculation is justified only if the retained description preserves which continuations remain possible. In particular, one unknown parameter fixed throughout a run cannot silently take a different worst value at each stage. Carry that parameter's compatible set and any information learned about it, or keep the coupled trajectories. :5.4 shows a choice reversed by losing this dependence.

Likewise, a terminal threshold depends on the accumulated amount. Retain that amount if it is observed; otherwise retain the uncertainty about it together with the other relevant state. In :5.3, current expected gain is enough to compare one objective but insufficient for another.

For a compressed or learned state, separate three possible claims: performance of a specified restricted policy; an optimum within that policy class; and an optimum among all policies allowed by the available history. Neither a convenient memory representation nor a converged learning algorithm makes those claims interchangeable. Evaluate the returned policy under the original information and consequence account, with the uncertainty or approximation relevant to its intended use.

#### MMP.8.SD:4.6 - Return the model and propagate a consequential change

Return the state or belief and its update, admissible policy information, action-dependent relations, consequence criterion and continuation relation. Include a computed policy comparison or bound when it is already useful, and state the assumptions that make it applicable. A formula alone can be the right input to a computational specialist; a two-branch calculation can already settle an ordinary choice.

Work through an available case from initial information to the result that the receiving activity uses. If a state reduction was needed, include the histories it would otherwise merge. Compare with a serious simpler option: a fixed plan, immediate-gain choice, full history tree or an existing policy with an adequate bound. Added state and computation earn their cost by changing the answer, making it obtainable or preserving a needed qualification.

When an actual premise changes, follow the affected dependency. A delayed observation changes allowable conditioning; changed resource availability changes actions and transitions; a new target changes the consequence account and may change the state. Recalculate the affected continuations. Use MMP.14 when observations reveal systematic mismatch in the proposed model, and the subject method when its action consequences need repair.

Use C.11.DUA to decide whether additional observation, modeling or computation can improve the receiving use enough to warrant its cost. An existing bound can settle the question. A hypothetical sensitivity exercise is useful when it can expose a consequential assumption; it is not an additional task when it cannot change use.

A human or AI participant can construct or calculate this model. Applying a policy in the subject still requires the observations, permitted actions and performing method that the model assumes. Methodological work uses the model to decide, for example, whether to observe before acting, retain a resource or change a method after an informative result; it also supplies the practical conditions under which that sequence can be performed.

### MMP.8.SD:5 - Archetypal Grounding

The following are constructed finite models. Their numbers show what follows from the stated assumptions.

#### MMP.8.SD:5.1 - Reserve a resource for an observed later request

A portable power unit has enough energy to serve one task in either of two slots, with no recharge. Serving the current task in slot 1 yields 4 units on an already selected gain scale. In slot 2 a different task arrives with probability 0.6 and yields 10 if served. Arrival is observed before the slot-2 decision. Unused energy has terminal value zero; the current task cannot be deferred. Serving consumes the whole unit.

Let b be remaining energy, either 0 or 1, and d indicate the later arrival. At slot 2,

    V_2(b,d) = 10*b*d.

Use the retained state `(time, remaining energy, current request)`. The slot-1 comparison is

    serve now: 4 + 0 = 4
    reserve:   0 + 0.6*10 + 0.4*0 = 6.

The resulting policy reserves energy, then serves if the request arrives. It has larger expected gain than immediate service, although it yields zero when no request arrives. If the requirement is a gain of at least 4 in every admitted case, serving now meets it and reservation does not.

Two histories can show the same later request but differ in whether the energy was already used. Merging them would make the slot-2 service appear available after both histories. Retaining b prevents that error.

Suppose the arrival probability changes to 0.3, with the other premises unchanged. Reservation now gives 3 and immediate service gives 4, so the first action changes. If instead the only available probability statement is `0.55≤p≤0.65`, reservation gives expected gain between 5.5 and 6.5 and exceeds 4 throughout. Refining p is unnecessary for that comparison.

#### MMP.8.SD:5.2 - Pay for information only when a later choice can use it

An unfamiliar encoded document uses format A or B, initially with equal probabilities. Two supplied decoders are available: the matching decoder gives a usable output worth 10, and the other gives 0. The model permits one final decoder application. An optional diagnostic costs 1 on the same gain scale and leaves the format unchanged.

The diagnostic returns + with probability 0.8 in format A and 0.2 in format B; the complementary probabilities give −. Its result arrives before decoder selection. The supplied observation model and A.3.3.PI's conditioning give:

| Information before decoder choice | Probability of format A | Best decoder | Expected final gain |
| --- | --- | --- | --- |
| No diagnostic | 0.5 | A or B | 5 |
| Diagnostic + | 0.8 | A | 8 |
| Diagnostic − | 0.2 | B | 8 |

The decision state can be `(stage, p)`, where p is the current probability of A. At the final stage,

    V_2(p) = max(10*p, 10*(1-p)).

Each diagnostic result has probability 0.5 under the initial model. Thus

    skip diagnostic:  V_2(0.5) = 5
    use diagnostic:  -1 + 0.5*V_2(0.8) + 0.5*V_2(0.2) = 7.

The continuation's choice changes with the observation. Fixing one decoder in advance gives 5 before the diagnostic cost, or 4 after it. This is why the extra information has value here.

Now the diagnostic result is delayed until after the final decoder choice. The decoder choice can no longer depend on that result. Using the diagnostic then has net expected gain 4, so skipping it gives the better value 5. This repair changes the information timing rather than the arithmetic of conditioning.

A different changed condition also reverses the comparison: with a timely but weaker symmetric diagnostic that is correct with probability 0.55, using its result gives `-1+10*0.55=4.5`. Skipping still gives 5 and is preferable.

The decoder and diagnostic behavior are premises of this example. A real use requires the applicable processing and observation methods to supply those consequences.

#### MMP.8.SD:5.3 - Retain accumulated progress when the terminal goal changes

In a two-round game, all awarded points are observed immediately. The first move is either A, giving 2 points with probability 0.5 and 0 otherwise, or B, giving 1 point certainly. In the last round, the player chooses Safe, adding 1 point certainly, or Gamble, adding 3 with probability 0.4 and 0 otherwise. The gamble's outcome is independent of the first round.

The objective is initially to maximize the probability of finishing with at least 3 points. Let c be points already earned. The terminal contribution is `g(c)=1` when `c≥3` and 0 otherwise. With zero intermediate contribution, the continuation compares terminal attainment:

| Points before last round | Safe: attainment probability | Gamble: attainment probability | Best continuation |
| --- | --- | --- | --- |
| 0 | 0 | 0.4 | Gamble |
| 1 | 0 | 0.4 | Gamble |
| 2 | 1 | 0.4 | Safe |

Therefore first move A gives `0.5*1+0.5*0.4=0.7`, while B gives 0.4. Choose A and condition the last move on earned points. Retain the state `(round, c)`. The round number alone is insufficient: histories with c=0 and c=2 require different continuations.

If the objective were expected final points, Gamble's expected increment 1.2 exceeds Safe's 1 at every c. Both first moves have expected increment 1, so both then give 2.2 expected final points. That calculation answers a different question from attainment probability.

Now change the requested terminal target from 3 to 4 points. From c=2, Gamble attains it with probability 0.4 and Safe fails. From c=0, neither last move can attain it. Thus A gives `0.5*0.4+0.5*0=0.2`. B followed by Gamble gives 0.4 and becomes preferable. The transition probabilities remain unchanged; the changed terminal criterion alters both the continuation and the first choice.

#### MMP.8.SD:5.4 - Preserve one unknown condition across stages

A two-stage processing route incurs costs w and `1-w`, where an unknown w is fixed for the whole run and belongs to `{0,1}`. Choosing that route commits to both stages. A supplied alternative has total cost 1.5. The question is to minimize worst total cost, with no probability model.

The two possible cost sequences for the route are `(0,1)` and `(1,0)`; both total 1. The route therefore beats the alternative. Adding the worst first-stage cost 1 to the worst second-stage cost 1 gives 2, but combines different possible runs.

For the first choice, the common total 1 already suffices. If the remaining cost is later needed and the first-stage cost is observed, that observation identifies w and determines the remaining cost.

Now the operating condition is allowed to change between stages: costs are `w_1` and `1-w_2`, with all four pairs `(w_1,w_2)` allowed. The pair `(1,0)` gives total cost 2. The route's worst total is now 2, so the fixed-cost alternative 1.5 is preferable. The old conclusion fails because the admitted dependence changed.

### MMP.8.SD:6 - Bias-Annotation

Finite stochastic examples make expectations and recursion easy to inspect, but may encourage a probability model or scalar gain where neither is supplied. Keep non-probabilistic possibilities and multiple criteria when that is what the work supports.

A model with one decision maker can also conceal separate information held by different people or systems. Represent communication and its timing when the proposed continuation depends on shared knowledge. Learned memory is attractive in large problems; its convenience does not establish sufficiency for a changed action set or criterion.

### MMP.8.SD:7 - Conformance Checklist

- The model states the decision order, information available before each action and allowed policy class.
- Transition and observation relations distinguish applied actions from uncontrolled circumstances and retain consequential dependence.
- The proposed state has an obtainable initialization and update. Its sufficiency or approximation is tied to the selected actions, criterion and horizon.
- The accumulated consequence includes the relevant terminal contribution, resource constraint or remembered progress.
- The continuation relation preserves the order of observation, choice and aggregation over uncertainty.
- A worked comparison returns a useful policy consequence, bound or unresolved distinction; any real changed premise is propagated to its affected use.
- Additional data or computation is selected for its possible effect on the decision. An already sufficient result remains usable.
- The mathematical model, computed policy and subject performance have distinct claims and required contributions.

### MMP.8.SD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Latest reading called the state | Histories with different resources or beliefs become indistinguishable. | Compare the histories' allowed actions and continuation, then retain the missing distinction. |
| Future knowledge used now | A policy selects a branch before its observation arrives. | Place observations and commitments on the same decision timeline. |
| Immediate score treated as total value | Resource use or information acquisition changes the future comparison. | Include the continuation under each current action. |
| Every objective written as a sum of immediate rewards | A terminal target or policy constraint changes meaning. | Preserve the criterion and augment the state or formulation where it needs history. |
| Independent worst values substituted for one fixed unknown | The calculation creates a trajectory excluded by the model. | Preserve coupling across stages or explicitly adopt the enlarged uncertainty set. |
| Convergence treated as decision sufficiency | A solver can converge for a representation that loses relevant history. | Identify the solved problem and evaluate the returned policy under the intended model. |

### MMP.8.SD:9 - Consequences

The reader obtains a model that explains why a present action is useful together with what can follow it. It can reveal that a resource should be retained, that a reading is worth obtaining only before a commitment, or that a changed target requires remembering different information.

The construction also locates missing contributions: an observation law, an action consequence, a criterion, a retained distinction or a computational procedure. A small bound may close the comparison before any large policy computation.

A sufficient state can greatly reduce repeated reasoning, but constructing it and solving the resulting problem can still be costly. More detailed modeling can worsen the work when it cannot change the receiving decision.

### MMP.8.SD:10 - Architectural Rationale

The construction begins with available histories because they expose the actual information constraint. A state is then a justified reduction of the decision problem. Starting from a convenient list of current features reverses that order and can hide lost memory.

Prediction contributes the distribution or set needed to describe a continuation. Decision modeling additionally specifies allowable actions and how consequences are accumulated and compared. In :5.3, identical transition knowledge supports different policies after a change of goal. In :5.2, identical diagnostic accuracy has different value after a change of timing.

A full history tree is a serious alternative to state compression. For a small problem it is often the clearest and cheapest model. A fixed plan is adequate when future information cannot improve the selected comparison; the delayed diagnostic shows such a boundary. For larger problems, a justified compact state makes repeated questions reusable by computational methods.

The continuation relation describes the mathematical problem consumed by those methods. It does not prescribe a solver or the worth criterion. This keeps model construction usable in physical operations, investigation, computational work and method design without replacing their subject methods.

### MMP.8.SD:11 - SoTA-Echoing

The practice question is how to retain enough information for a useful sequential choice without demanding an unnecessarily complete reconstruction.

| Question and comparison | Adopted or adapted contribution and limit |
| --- | --- |
| Can a compact summary replace the full history tree? | **Adopt** the information-state line of Subramanian, Sinha, Seraj and Mahajan, [*Approximate Information State for Approximate Planning and Reinforcement Learning in Partially Observed Systems*](https://jmlr.org/papers/volume23/20-1165/20-1165.pdf), JMLR 23 (2022), §§2.2–2.3 and 3.2, especially Theorems 5 and 9. Preservation of expected gain and the next summary's law supports the reduction in :4.3–:4.4; approximate preservation needs a consequence bound. A full history tree remains preferable when small. This line saves representation and computation only when its conditions are obtainable; prediction fit alone supplies less. Reopen when a newly relevant action, history or criterion changes the equivalence between merged histories. |
| What if compact memory is useful but not sufficient? | **Adapt** Sinha and Mahajan, [*Agent-state based policies in POMDPs: Beyond belief-state MDPs*](https://arxiv.org/html/2409.15703v1), arXiv v1, 24 September 2024, §§II-C–II-D and III. Its comparison of policy classes supports :4.5: evaluate a restricted controller as such, rather than assuming an arbitrary recurrent memory admits the continuation equation in :4.4. Direct policy search is a serious alternative when sufficient-state construction is too costly. Preserve whether its result is locally optimal or best within a restricted policy class. Reopen when memory, available computation or required policy class changes. |
| Does convergence of a modern learning algorithm close the state question? | **Reject that inference**, using Sinha, Geist and Mahajan, [*Convergence of regularized agent-state-based Q-learning in POMDPs*](https://arxiv.org/html/2508.21314v2), arXiv v2, 2 September 2025, §§II-B–IV and Theorem 1. Under its learning-rate and visitation assumptions, the limit is for a regularized model that depends on the behavior policy's limiting distribution. The result sharpens :4.5's separation of numerical convergence from the intended policy comparison. Regularized learning remains a computational option; it brings its objective and representation conditions. Reopen when a proposed solver claims a stronger use than its result supports. |
| What if probabilities are unavailable and the criterion is worst consequence? | **Adapt** Dave, Venkatesh and Malikopoulos, [*Approximate Information States for Worst-Case Control and Learning in Uncertain Systems*](https://arxiv.org/html/2301.05089v2), arXiv v2, 6 April 2024, §§II–III. Conditional ranges and a criterion-specific continuation are a serious alternative to expected gain. The paper derives continuations for maximum instantaneous and terminal cost. For accumulated costs, :4.5 and :5.4 preserve the allowed complete trajectories. The trade-off is a worst-case comparison in place of a probabilistic average; reopen when the uncertainty set or its cross-stage dependence changes. |

### MMP.8.SD:12 - Relations

- **MMP.8 - Formulate Information-Dependent Choices Mathematically** supplies choices, uncertainty, information timing and admissible policies. This nested refinement constructs their sequential state and continuation.
- **A.3.3.PI - Retain the Information Needed for Prediction**, especially :4.4, supplies prediction and hidden-state belief updates. This method consumes them in action and accumulated-consequence comparisons.
- **MMP.7** supplies the recording law and available observations. **MMP.13** can supply inferred model quantities with their uncertainty; neither contribution alone establishes the effect of a new action policy.
- **C.28.MR** supplies intervention through a changed mechanism. A subject method supplies or justifies the resulting action and observation relations used here.
- **MMP.14** supplies criticism and repair when comparable predictions fail. A detected failure here identifies which state, information or consequence premise must return to modeling.
- **C.29.2 - Computational Formulation** specifies the computational answer or continuing response and the procedure needed to obtain it.
- **CMP.3 - Share and Schedule Repeated Subcomputations** organizes repeated evaluations of the continuation. **CMP.9 - Construct a Randomized Estimator or Sampling Procedure** estimates expectations with a computational error account. **CMP.5 - Bound an Optimum or Recover a Feasible Candidate through a Relaxed Problem** supplies relaxation, candidate recovery and improvement bounds for the chosen formulation.
- **C.11.DUA** helps decide whether further information or computation is worth obtaining. FPF choice and portfolio methods and the applicable development, Strategy or Core Method-development contribution supply criteria, compare the returned alternatives and organize their practical use.

### MMP.8.SD:End
