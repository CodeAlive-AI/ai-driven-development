## C.32.LCA - Construct and Compare a Control Architecture

> **Type:** Method pattern in the C.32 architecture-synthesis family
> **Status:** Stable
> **Normativity:** Guidance within the stated applicability

### C.32.LCA:1 - Problem frame

Use this pattern when a result depends on decisions and actions that use different information, take different amounts of time, or belong to participants with different authority, and you need to construct or change how those contributions work together.

A robot can follow a target accurately and still receive a target that exceeds its actuator limit. A production team can respond quickly and still wait for a decision that nobody present may make. In both situations, improving one participant is insufficient: the arrangement must connect what can be observed, decided and done in time.

**First useful move.** Choose one consequential demand or disturbance. Follow it from the information available at the time, through the decision and permitted action, to the receiving result. Check whether the arrangement supplies the conditions along that path. A missing condition directs construction of an alternative; an adequate path can be retained while examining another consequential case or a justified improvement. Follow each proposed change through the same whole.

**What this buys.** The reader obtains comparable control arrangements, the mechanism by which each could obtain the intended result, their conditions and costs, and a reason to retain, select or revise an arrangement. A useful result can be a simpler incumbent, a bounded proposal, a qualified technical construction, or a precise finding that the requested outcome is unavailable under the supplied conditions.

The broad subject is functional organization: how contributions combine to obtain a whole result. This pattern develops its **control-architecture branch**. It constructs the organization of observation, decision and intervention, including coordination needed between controllers or participants. It does not presume a hierarchy, three layers, different update rates, or a correspondence between one function and one physical part. Layered and multirate control are important alternatives within this question.

The primary working reader is an architect, engineer or operations practitioner who can explain the relevant work and obtain the subject knowledge needed for its consequential claims. The common method requires reasoning about dependencies, time and conditions. A numerical stability or safety claim additionally requires the appropriate control-engineering competence and model.

**Ordinary boundaries.**

- If an available controller or working arrangement already answers the question, use it. A new architecture exercise needs a consequential reason.
- If the question is what control structure a description actually represents, use **C.30.LCA**. Its result can supply the present arrangement here.
- If the difficulty is functional construction without a control dependence, use **C.32** for the candidate-configuration question or **C.39** for a missing way to obtain the required contribution. Return here when the observation, decision and intervention dependence is the unresolved part.
- If the task is to establish the purpose or legitimate priority itself, obtain that decision from its governing practice and participants. Here the question is how that decision affects feasible control and when feedback requires its reconsideration.
- If a project needs a particular controller, estimator or safety proof, construct or obtain that technical result. The common architecture method below identifies and uses its necessary contribution; it does not replace the subject mathematics.

A proposed arrangement and an operating arrangement have different evidence. The explanation can justify a candidate before implementation. Claims about its actual effectiveness require observations of its use under the conditions that matter.

### C.32.LCA:2 - Problem

Separately reasonable choices can be incompatible when connected. A planner assumes immediate execution; an executor receives a stale state; two units allocate the same scarce resource; a requested exception requires authority outside the decision window. Each local description can be correct while the intended result remains unobtainable.

A familiar layered drawing does not resolve these dependencies. Nor does naming “strategy, planning and execution”: the designer still needs to determine which choices belong together, what information crosses a boundary, how long each contribution may take, and what remains possible when a premise fails.

The practical problem is to construct and compare those relations without losing the purpose, physical or organizational constraints, or the costs introduced by separation. The result must explain both how the arrangement can continue and which feedback calls for a different action, goal or architecture.

### C.32.LCA:3 - Forces

| Force | Consequence for the construction |
| --- | --- |
| Rapid correction and costly deliberation | Keep a useful immediate response available while slower reasoning proceeds; account for the delay and information it consumes. |
| Local authority and coupled consequences | Permit decisions where they can be made in time, while preserving shared limits and commitments that local success can violate. |
| Detailed state and obtainable information | Retain distinctions that change the decision, including relevant history or uncertainty, without demanding an exhaustive model. |
| Predictive preparation and changed intentions | Early information can remove waiting but can also reserve capacity, cause rework or mislead another decision. |
| Separate competence and joint performance | Qualified components still need compatible inputs, timing, resources and continuation conditions. |
| Adaptation and preserved reliance | Changing a goal, policy, model or learned component can invalidate a result used elsewhere even when its interface spelling stays the same. |
| Strong assurance and affordable use | A conditional calculation may settle one choice; a stronger claim incurs the evidence and modeling burden appropriate to that claim. |

### C.32.LCA:4 - Solution

Construct the arrangement from the result and its causal dependencies, then compare the complete alternatives. The following sections explain connected operations, not a mandatory sequence of meetings or a prescribed stack of controllers. Begin at the first missing contribution; retain an adequate model, decision or component result.

The architectural result changes the organization through which control occurs. **C.43** supplies the broader connection between the current situation, possible continuation, choice, realized influence and revision; use it directly when those answers can be joined within an adequate existing arrangement. The present Method constructs an arrangement when that joining requires different information, timing, allocation, means or interaction. Its result then returns to the ongoing control question.

#### C.32.LCA:4.1 - Recover the controlled situation and the consequence that matters

State what is meant to change, for whom, by when, and within which protected conditions. “Make the system faster” leaves the decision unresolved. “Reach the receiving position within two updates without exceeding the actuator limit” identifies a result and a constraint. “Have the approved panel installed by 16:00 without spending an unauthorized budget” identifies a different result and different conditions.

Identify the acting participants, the subject affected, the available interventions, and the observations that can inform their selection. Recover what an existing arrangement does from an actual consequential episode or an adequate model. For a proposed arrangement, explain the intended dependence without describing it as already operating.

A feedback claim needs an observation, an influence returned to the subject, and a rule and case facts coupling that influence to the observation. **B.2.5** supplies this recovery. Use the result here to find which dependence must be constructed or changed. A dashboard that nobody uses to change action supplies information but not that control dependence.

Keep the selected structure and its representation distinct. **C.30.LCA** helps recover the observation, command, reference, feedback and timing relations represented in a view. Use those relations as inputs, then examine their consequences below. An organizational chart may omit an external supplier who controls a needed release; including that relationship does not make the supplier part of the enterprise.

#### C.32.LCA:4.2 - Separate the goal, its realization and the right to revise it

Distinguish the intended outcome, the constraints that remain binding, and the choices available within them. A destination, an allowed operating region, a customer commitment and a preferred cost are different inputs to a decision. Some are negotiable by the present participant; others must be retained or returned to someone with the relevant authority.

Three changes often require different treatment:

- **Change the immediate action while preserving the goal.** Correct a disturbance, choose another route, reschedule an available resource or use an already qualified fallback.
- **Change an operational goal within the current mandate.** Select the next job, change a waypoint or choose among already authorized service priorities. Recompute the consequences for the work that depends on the earlier choice.
- **Change the mandate, promised result or architecture.** Renegotiate the deadline, remove a required output, obtain a new allocation right or change the available means. Include the time and conditions needed to make that change effective.

These are choices, not necessarily three organizational levels or three people. One actor can perform several of them; different actors can participate in one choice.

Construct the return from infeasibility to goal revision. Identify the observation or forecast that makes the present goal doubtful, the alternative outcomes still available, and who can select among them. Include the receiving work affected by that revision. A planner's failure to find a plan is evidence about that search under its conditions; it is not, by itself, proof that no feasible plan exists. A physical bound or an exhaustive argument can establish a stronger impossibility result.

While the revised decision is unavailable, specify the continuation that remains permitted. Continuing, holding a command, reducing demand, switching to another qualified method or stopping can each be right under different subject conditions. Stopping is not automatically safe: an aircraft, a chemical process and an unfinished organizational obligation have different consequences.

#### C.32.LCA:4.3 - Construct the information that makes the decision possible

Begin with the future distinction the decision needs. To decide whether work can finish today, a count of unfinished jobs may be insufficient if their remaining effort differs. To constrain a moving system, the last reported position may be insufficient if motion since that observation is unknown.

Specify the state, transition account and future input assumptions used by the prediction. Retain pending actions, occupied resources or accepted commitments when their differences change the continuation. Separate the subject's state from the information available about it.

Use **A.3.3.PI** when the retained information needs construction or repair. Compare two admissible situations that the proposed description merges, under the same future inputs and change rule. If their decision-relevant continuations differ, preserve the missing distinction, use sufficient history, or propagate a set or distribution of possibilities. A bound can settle the decision without identifying the exact state.

Date an observation by when it describes the subject, not only when its message arrived. Bring it to the decision time using the known intervening actions and dynamics, or retain the uncertainty those missing facts create. If a model requires information that cannot arrive in time, compare a different observation arrangement, a more conservative action, another model or a different decision allocation.

Construct the forecast for the actual use. A one-step predictor repeatedly applied, a direct longer-horizon predictor and an upper bound can support different conclusions. The model used for planning may differ from the model needed to qualify rapid correction, but the correspondence between their inputs, outputs and retained distinctions must be explained.

Internal simulation and actual intervention supply different returns. A simulated failure can change the proposed action before execution. An observed result after execution updates the state estimate and may challenge the model. Do not count repeated replanning as progress in the controlled subject.

#### C.32.LCA:4.4 - Derive a division of decisions from the whole dependence

Start with a feasible incumbent or a whole-problem account, not a fixed number of layers. Ask which decisions need which observations, available actions, resources and time. Group decisions when their strong interaction makes separate choice costly or unreliable. Separate them when different information or response demands make one undivided computation or authorization path impractical.

For every proposed separation, recover the dependence it removes from local consideration. Suppose two devices share a power supply limited to 10 kW. Each local plan can meet its device's 8 kW demand while their simultaneous demands total 16 kW. Giving both plans a copy of the resource limit does not preserve the joint constraint. Where the work permits different allocations or times, possible constructions include a shared allocation decision, fixed compatible reservations, a request-and-grant interaction, or staggered work. They have different waiting, utilization and change costs. If both devices must draw 8 kW simultaneously, no allocation fits the 10 kW supply; change the available supply, the demand or the simultaneity requirement.

The same question applies to planning and tracking. A planner that ignores actuator effort or response delay can select references that its tracker cannot realize. The joining contribution must restrict the references, supply a feasible trajectory, change the tracking arrangement, or revise the demand. Merely adding a feedback arrow leaves that work undone.

Recover functional contributions before assigning their bearers. Estimating state, choosing among goals, constructing a trajectory or work plan, correcting a deviation and handling an exception can each contribute without requiring a separate module, department or person. State the effect each must obtain, the inputs and initial conditions it needs, and the conditions it must preserve. Then associate it with a possible System or participant and the means through which that effect could be obtained. One bearer can carry several contributions; several bearers can cooperate in one contribution. Keep existence, capability, access and proposed allocation as separate claims.

Construct the cooperation in both directions. Work back from the required intervention to the decision, information and means that make it possible. Follow each missing intermediate result to a possible producer. Then follow a consequential demand forward from the available observations and initial conditions: what changes, what becomes usable next, and how those changes obtain the receiving effect. Explain where contributions must coincide, wait or retain a result between updates. A state estimate that expires before authorization, or a command whose execution has no available bearer, defeats that candidate even if every named function is sensible.

**C.32.MWA.PP:4.3–4.7** supplies the general construction across Method, Work, performer, means and allocation structures, including their joint demands. Use that account where the proposed division leaves performance or support unresolved. Here the additional connection is control-specific: explain how the joined contributions turn an observation into a permitted influence on the subject, and how the resulting observation can change the next decision. Change the division or its possible realization when that connection fails; preserve already adequate contributions.

For each candidate, explain how a local result becomes usable by the next participant and how a consequential limitation returns. The result is a candidate arrangement with an operating mechanism, not a collection of independently desirable boxes.

#### C.32.LCA:4.5 - Compare serious architectural alternatives

Retain alternatives that change the mechanism, not just the labels. The following are recurring choices, not an exhaustive classification.

A command or reference governor adjusts the requested input to an already qualified closed loop using its current condition and applicable constraints. It is an alternative to redesigning that loop.

| Alternative | When it can answer the question | Cost or limit to examine |
| --- | --- | --- |
| One controller or one timely decision point | The needed information and action rights are available together, and the computation or decision fits the useful window. | Information collection, scarce attention, computation and response delay can become limiting. |
| An already qualified loop with a command or reference governor | The loop's response is adequate, but requested commands can violate its qualified conditions. | The governor can delay or alter the requested outcome; it needs an applicable model and admissible initial situation. |
| Layered planning and correction | Different decisions need different horizons, representations or response times, and a useful interface can preserve their dependence. | Model mismatch, stale information, repeated computation, interface constraints and delay must be included. |
| Local decisions with coordination of shared conditions | Participants can act independently within allocations or agreements, while specified interactions need reconciliation. | Negotiation, conflicting commands, duplicated reservations and unavailable authority can defeat apparent autonomy. |
| Change the work or the physical arrangement | Removing a dependency, changing a capability or changing the demanded result costs less than coordinating the existing arrangement. | Transition cost, lost flexibility, changed commitments and consequences for other users remain part of the comparison. |

Use **C.32** to develop the candidate palette when several structures change together. For an identified conflict across scopes, **C.32.MLAO** helps generate alternatives that reduce it while exposing the burden moved elsewhere. Bring those candidates back to the information, timing and joint-condition construction here.

A policy in a lower control layer need not be less accurate than a decision in an upper control layer. Rapid tracking accuracy, predictive accuracy, semantic understanding, search quality and adaptability are different characteristics. Compare the required characteristics under the actual resource conditions. A rule such as “strategy is slow” is a possible arrangement, not a substitute for that comparison.

#### C.32.LCA:4.6 - Construct the exchange that makes the parts work together

For each consequential connection, explain what the sender supplies, how the receiver interprets it, which action it can change, and which limitation or result returns. Specify the semantics before choosing a message format or transport.

A target value, a trajectory segment and an instruction to achieve an outcome impose different work on the receiver. A target may be held until replaced; a segment can specify its evolution; an outcome request can leave the means open. Determine which interpretation the receiver can realize and which uncertainty remains with the sender. In a technical realization, hold, reset, interpolation and delay rules can change the closed-loop dynamics.

Keep the following meanings distinct when the receiving action depends on them:

- an observation or estimate of what is the case;
- a prediction of what could or is expected to happen under stated inputs;
- a decision selecting a continuation;
- a command or request addressed to a participant;
- an accepted commitment to supply a result under conditions;
- a report of the action or result that actually occurred.

A decision does not necessarily authorize its recipient, and a request does not establish acceptance. An organization may require an explicit commitment; a technical protocol may instead have a specified execution rule. Construct the connection that actually governs the case.

Early communication is useful when a receiver can do worthwhile preparation before the final result exists. Name that preparatory action, the information it needs and its reversibility. Reserving a test slot can reduce later waiting while displacing other work. Preparing material can save time while creating waste if the intended design changes. Compare those consequences with waiting for confirmation; do not treat earlier messages as a free acceleration.

Include the response to change. If a plan, estimate or commitment is replaced, identify which pending action must be cancelled, revised or allowed to finish. Distinguish a message received from a message interpreted and used. Where conflicting editions would change execution, establish which instruction applies and how the recipient learns of its replacement.

Connect the proposed exchange to effective action. Identify who can request the result, who can commit the affected means, who can perform the work, and who can accept or return its result. For the needed contribution, state the supplied result, usable inputs, scope, time window, acceptance conditions and response to refusal or failure. A participant's right to choose an action and another participant's commitment to carry it out are distinct conditions; either can be missing.

Use **C.32.MWA.PP:4.7–4.9** to construct and compare the joint workload, commitments and transition. Reuse existing effective arrangements whose scope and conditions fit. When a new permission, reservation or agreement is needed, identify its owner and the obtainable act that could establish it, including the time and participation required. Keep the candidate conditional until that act and its conditions are established. A design specification explains the intended relation; the actual authorization, acceptance or provision supplies a different fact. Return those effective conditions, or their precise unresolved remainder, to the timing analysis and continuation choice.

#### C.32.LCA:4.7 - Derive useful timing from the action window

Start from the last time at which an action can still obtain the required consequence. Work backward through the necessary detection, communication, decision and execution. Include waiting for an available processor, person, authorization or resource, not only active processing time.

For a serial path with applicable upper duration bounds, a sufficient timing condition is

\[
t_{\mathrm{change}}+
L_{\mathrm{detect}}+
L_{\mathrm{deliver}}+
L_{\mathrm{decide}}+
L_{\mathrm{execute}}
\leq t_{\mathrm{needed}}.
\]

Each bound must cover its whole contribution under the compared conditions. Periodic observation contributes the worst wait until the next observation as well as the observation work. A computation bound must include the resource arrangement under which it can be achieved. A decision bound must include the availability of a participant with the required authority.

This sum applies to the stated serial path. For parallel or returning work, construct the timing from its dependencies and resource occupations. Identify when each required input and permission can be available, which resource each action occupies, and when it releases that resource. Reconcile different names for the same person, device or capacity before assigning intervals. A machine may continue a cycle after its operator is free; an allocation must reflect that actual occupation rather than charging both for the whole elapsed cycle.

Construct a candidate schedule by placing each action after its required inputs and authorizations, in intervals where all the resources it needs are jointly available. Preserve any required uninterrupted duration, overlap, synchronization and recurring demand. At a join requiring all outputs, the receiving action can start only after the latest required output is available; its own duration still contributes to final completion. Use **C.32.MWA.PP:4.7** for the joint workload and commitment construction. A failed placement rejects that schedule; it does not prove that a different order or allocation is impossible. A necessary bound can establish a stronger rejection: required occupation exceeding the available qualified capacity in the same window cannot be repaired by rescheduling within that window.

For example, two otherwise parallel branches each require ten minutes from the same editor before their outputs can be used together. With one continuously available editor and no other required work, serializing the two edits gives a twenty-minute completion. A deadline fifteen minutes after both edits become available is impossible under those conditions, although either branch alone fits. A second qualified and authorized editor, a changed operation or a later deadline changes a different premise of the construction.

Retain a timing summary only when the receiving answer follows from what it keeps. Total free time can conceal incompatible windows; an average rate can conceal a late individual response. Derive the response time or useful bound from the retained dependencies, availability and occupation conditions. If two allowed arrangements share the proposed summary but give different answers, retain the distinguishing condition, derive a bound that covers both, or restrict the claim. Failure to find such a pair does not establish sufficiency. This specializes the information question in :4.3 to the time and capacity needed by the control decision. An average duration does not establish a worst-case deadline.

Choose an observation or decision rhythm from how rapidly a consequential difference can develop and how long a useful response takes. Periodic checking, event-triggered messages and prediction of an approaching limit are alternatives. An event trigger needs an obtainable detector and a response route; otherwise “notify on exception” supplies no timing result.

Separate update period, end-to-end latency and prediction horizon. A planner can update slowly while predicting far ahead; a fast controller can use a delayed estimate. Changing one quantity may change model error, computation, communication load or the available response. Recompute the affected dependence rather than assuming that more frequent updates are better.

Before the next update, specify what the current action may do and why that continuation remains acceptable. If a premise can fail sooner than a response can arrive, obtain a local protective action, shorten the exposure, change the observation or reduce the promised operating region. A monitoring arrangement cannot protect a condition it notices only after the last useful action.

#### C.32.LCA:4.8 - Establish joint conditions and a usable continuation

For each relied-on component or participant result, state its inputs, operating conditions, output and limits. Then check the connection in both directions: does the supplier's result satisfy what the receiver needs, and can the rest of the arrangement keep supplying the conditions on which that result depends?

Begin with a jointly possible situation. Two controllers can each require the other to have already restored the shared condition. Two teams can each promise to start when the other releases the only specialist. Such mutual expectations supply neither an initial action nor a continuation. Construct an initial allocation, a compatible joint condition or another arrangement.

Next follow a consequential action or change through the whole. Establish what remains true, what must be updated and what is available next. A successful isolated execution does not establish repeated continuation.

For a modeled controller interconnection, derive or obtain the joint dynamics rather than combining separate stability labels. Include reference changes, state estimation, hold rules, actuator limits and computational delay. A technical result can establish an admissible region, an error bound, recursive feasibility, stability or goal attainment; retain the property actually established. These results are not interchangeable.

For example, an invariant error bound can justify a margin in a planner constraint while leaving the question of reaching its goal unresolved. A continuous inequality proved only in a region applies until the first exit unless remaining in that region is established separately. Under mode switching, one invariant set respected by every allowed transition is a useful sufficient condition; different invariant sets for individual modes do not establish safe transitions between them.

Organizational continuation needs a different construction. An accepted commitment must have a capable participant, available means, compatible other commitments and the right to perform the promised action. Establish how an unavailable input, refusal, changed priority or missed window is handled. A promise can be part of the plan's basis without becoming a mathematical guarantee of performance. If the plan needs a deterministic deadline, justify the duration bounds and availability it relies on; otherwise retain the appropriate scenario, uncertainty or conditional promise.

Choose the fallback for the protected result. Keeping a previous command can work only while its qualifying conditions remain true. Escalation can work only if the recipient can decide in time. A replacement performer can work only with the required competence, access and capacity. Compare these as actual continuations, not names in an exception list.

If the joint conditions cannot be established, return the exact unresolved or conflicting dependence. It may justify a different interface, smaller demand, different allocation, additional observation or a revised goal. Keep independently usable component results.

#### C.32.LCA:4.9 - Qualify learned contributions by their actual function

Learning is one way to obtain a contribution to the arrangement. Identify which contribution it supplies. A learned state estimate, forecast, action policy, representation or optimization surrogate has different inputs, outputs and failure consequences.

For a predictor, qualify the output, horizon, available observations, future-action assumptions and error relevant to the receiving decision. For a policy, qualify the actions it can select, the states and instructions it can receive, and the constraints of the actual subject. Agreement with recorded demonstrations and a useful closed-loop result are different tests.

Keep training, inference and online adaptation separate. A policy trained slowly can execute rapidly. An online update can change the policy while its input and output formats remain unchanged. Determine whether the relied-on error, timing or constraint result continues to apply to the updated component.

Compare the learned contribution with an adequate programmed or conventional controller at the same receiving use. Include data acquisition, training or calibration, inference resources, monitoring and recovery in the whole cost. Prefer the learned option when its supported capability changes the result enough to justify those burdens, not because the architecture contains a neural network.

If a separate filter or supervisor modifies a learned command, qualify the resulting combination. The modified command can preserve one constraint while changing a tracking or progress result. A human fallback also needs detection, sufficient time, usable information and actual authority.

The output of this operation is a qualified component use or a named missing result. It is not a general method for training every controller. When the application needs a bound that the learned supplier has not established, compare a narrower operating region, an applicable protective construction, a different supplier or a weaker warranted claim. Do not silently replace the missing bound with average benchmark performance.

#### C.32.LCA:4.10 - Compare the whole arrangements and the work of changing them

Compare candidates under the same required outcome, disturbances, resources, observation conditions and relevant horizons. A faster local algorithm evaluated on an easier demand is not a faster realization of the original problem. A delegated decision evaluated without its coordination and training cost is not the same organizational proposal.

Separate an unavailable candidate from a costly feasible one, and both from a candidate whose consequential premise remains unknown. Compare the coordinates that can change the decision: useful result, delay, constraint exposure, effort, computation, scarce capacity, participant burden, flexibility and recovery. A mathematical optimum remains relative to its model and objective; a project choice also has to respect its obligations.

Include the transition. A new controller needs initialization and an admissible switch. A new organizational allocation needs effective authority, informed participants and preserved obligations. Existing work and performed history do not disappear when the new arrangement is selected.

**C.11** supplies a reasoned local choice among the explained alternatives; the right to commit resources or direct action remains separately established under the actual permission and agreement relations; use **C.11.DUA** when the value of another observation, calculation or trial is itself unresolved. A constructed case can justify a conditional proposal. An effectiveness claim requires evidence from its intended use. Do not require a new trial when existing adequate evidence settles the decision, and do not count a simulated or taught example as operational evidence.

Return the chosen alternative, accepted trade-off and conditions of use to the receiving engineering or organizational decision. If only a candidate comparison was requested, it can finish here without authorizing implementation.

#### C.32.LCA:4.11 - Make the result usable and revise the affected dependence

Explain the result in the ordinary form needed by its users. It must make recoverable:

- the intended outcome and protected conditions;
- the participants, decisions and available interventions;
- the information, exchange and timing that connect them;
- the jointly feasible conditions, continuation and exception response;
- the serious alternative, accepted cost and basis of the present choice;
- the changed observation or condition that requires a different decision.

These are content requirements, not a mandatory record or a demand to model every relationship in the enterprise.

On new evidence, first identify the failed dependence. A fresh observation may only require a new state estimate. A different response can challenge the dynamics or capability. A blocked authorization can require a different allocation or commitment. A changed use can require a revised goal. Alter the architecture when the needed continuation cannot be obtained adequately within the existing arrangement.

Carry the change through its direct consumers. A new estimate can change the admissible command; that command can change arrival time; the changed arrival can defeat an organizational promise. Preserve unaffected results, and requalify the connections that actually changed.

### C.32.LCA:5 - Archetypal Grounding

#### C.32.LCA:5.1 - Retain a qualified loop and change how it receives targets

Consider a constructed discrete model, in normalized units,

\[
x_{k+1}=x_k+u_k,\qquad
u_k=\tfrac12(r_k-x_k).
\]

The actuator condition is \(|u_k|\leq0.06\), and the state must remain in \([-1,1]\). The state is available without delay or error in this first case. The controller computation fits each update. These are premises of the example, not claims about a physical device.

For a fixed target, the error contracts by one half per update. Nevertheless, if \(x_0=0.5\) and a planner immediately applies \(r_0=0.7\), the commanded input is \(0.1\), outside the actuator limit. The separate tracking result did not qualify that reference change.

One alternative is to redesign the controller and planner together. Another candidate retains the controller and limits the applied target from the desired goal \(g_k\in[-1,1]\):

\[
r_k=x_k+\operatorname{clip}(g_k-x_k,-0.12,0.12).
\]

Here \(\operatorname{clip}(a,l,h)=\min(\max(a,l),h)\). Substitution gives
\[
u_k=\tfrac12\operatorname{clip}(g_k-x_k,-0.12,0.12).
\]
Thus the actuator condition holds. The next state lies between \(x_k\) and \(g_k\), so an initial state in \([-1,1]\) stays there. This establishes the stated discrete constraints for this model. It does not establish intersample physical safety or a prescribed arrival time.

For the constant goal \(0.7\), the first three applied targets are \(0.62,0.68,0.7\); the corresponding inputs are \(0.06,0.06,0.04\), and the resulting states are \(0.56,0.62,0.66\). The limiter uses the loop's remaining action capability and returns a different progress forecast to the planner. It is a simple state-dependent governor construction, not a reason to add a new tracking layer.

Now request \(x_2\geq0.68\) from \(x_0=0.5\). Under the actuator bound, even an arbitrary control law can increase the state by at most \(2(0.06)=0.12\), giving \(x_2\leq0.62\). That requirement is impossible under the stated model and limit. The next choice concerns the deadline, attained position or available actuation; faster planning alone cannot obtain it. The participant authorized to change the demanded result must receive this bound.

Change the governor's observation condition instead. Suppose the governor receives only \(\hat x_k\), with a qualified current bound \(|x_k-\hat x_k|\leq0.02\), while the local tracker retains the original state-based feedback law. Limiting \(|r_k-\hat x_k|\) to \(0.12\) would allow \(|r_k-x_k|=0.14\) and input \(0.07\). A sufficient repair is to limit \(|r_k-\hat x_k|\leq0.10\) and require \(r_k\in[-1,1]\). Then \(|r_k-x_k|\leq0.12\), while the original convex update preserves the state interval. The set of targets satisfying both conditions must be nonempty; it is nonempty here when the state lies in the interval and the stated estimate bound holds.

The error bound must describe the current state. A bound for a stale measurement cannot be reused without accounting for intervening motion. If the tracker also loses its state measurement, its response equation and the convexity argument need reconsideration. Replacing it with a learned policy likewise reopens the calculation: the old response equation no longer supplies its proof.

This case shows the common method's contribution: recover the violated join, compare a governor with joint redesign, construct the admissible interface, calculate its consequence for the goal, and reopen the affected condition when observation or policy changes.

#### C.32.LCA:5.2 - Obtain a timely organizational decision

An exhibition panel must be installed by 16:00. Under a constructed operating arrangement, the following bounds are available:

| Contribution | Upper duration and its conditions |
| --- | --- |
| Detect a material content change | 20 minutes, including the wait for the scheduled check and the checking work |
| Deliver the complete change to the editor | 5 minutes through an available channel |
| Decide and send the approved file | 10 minutes, including waiting; the editor is available and the change is within the editor's authority |
| Print and install | 25 minutes; material, access and the allocated performer are available |

These contributions are serial for this arrangement. A change occurring by 15:00 can therefore be handled by 16:00. The latest sending time is 15:20; delivery is by 15:25, approval reaches the performer by 15:35, and installation finishes by 16:00. A later change can still succeed in a favorable case, but the hour-long bound no longer establishes the promise.

The useful state includes the current content, its approval status, the required materials and the availability of the people and means. “The file was sent” does not distinguish an approved file from an unapproved proposal, or a delivered message from one awaiting a decision.

Compare three changes to the arrangement.

1. **Shorten detection to five minutes.** If every other premise remains true, the bound becomes 45 minutes. This helps changes that occur by 15:15. It adds observation effort and does not repair a missing decision right.
2. **Authorize a defined local exception in advance.** If the current change needs an extra expenditure outside the editor's authority, the ten-minute decision premise fails. An effective limited authorization, available reserve and competent decision maker can restore a bounded path. A proposal to delegate does not do so until those conditions hold.
3. **Retain central authority and change the commitment or work.** Obtain an available central decision window, agree to freeze content earlier, use an already accepted substitute panel, or omit the affected panel where the receiving commitment permits it. Compare the changed result, delay and cost; these are not equivalent ways to meet the unchanged promise.

A forecast of a likely change can allow reversible preparation before approval. Establish which materials or capacity may be reserved, what another job loses, and how the reservation is released if the forecast changes. Printing an unapproved final panel is a different action with different consequences.

The control mechanism is now explicit: a dated observation changes a decision made within actual authority, that decision supplies a usable input to an available performer, and the resulting installation or failure returns to the responsible participants. One person may perform several contributions, provided their demands still fit. No three-level management hierarchy follows from the four duration bounds.

The timing implication is mathematical under its premises. The premises about people, authority, resources and duration need organizational support and observation; they are not supplied by the equation. In actual use, distinguish a committed service bound, an empirical estimate and a planning assumption.

#### C.32.LCA:5.3 - The smaller sufficient result

A machine already has an applicable controller, command range, state estimate, timing qualification and recovery procedure. The proposed change only redraws their representation for a maintenance team. Use C.30.LCA to make the obtaining relations and limits recoverable. Do not repeat architecture synthesis unless that reading exposes a consequential missing or changed relation.

Similarly, a team can retain an adequate allocation when a new report does not change any action, deadline or protected condition. More communication is not a required improvement.

### C.32.LCA:6 - Bias-Annotation

The method can overfavor engineered, explicitly measurable interactions. Human participants can contest the goal, decline a request or hold interests that the model omitted. Recover their actual commitments and protected conditions before treating a proposed arrangement as available.

A layered picture can overfavor hierarchy. Shared resources, peers, external suppliers and overlapping authority may require coordination without one superior controller. Examine the actual influence and decision rights.

A successful demonstration can overfavor its observed conditions. Keep the operating region, information quality, available support and receiving criterion with the result. Compare the whole arrangement, including work displaced elsewhere.

### C.32.LCA:7 - Conformance Checklist

- [ ] The intended result, protected conditions and authority to revise them are recoverable.
- [ ] The candidate explains observation, decision and intervention dependencies, including the consequential return.
- [ ] The retained information supports the needed prediction or bound at the actual decision time.
- [ ] The proposed separation preserves shared constraints through a constructed interaction or allocation.
- [ ] Serious alternatives include retaining an adequate arrangement or changing the dependency itself.
- [ ] Timing accounts for waiting, resources, authority and the last useful action, not only message or computation speed.
- [ ] Initial conditions and continuation are jointly possible; component claims are not silently promoted to whole guarantees.
- [ ] A learned contribution is qualified for its actual function and its changed use is followed through the arrangement.
- [ ] The comparison preserves the same demand and includes transition and displaced burden.
- [ ] The result distinguishes a proposal, a conditional derivation and evidence of actual operation, and names its relevant return condition.

### C.32.LCA:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails in this use | Repair |
| --- | --- | --- |
| Draw strategy, planning and execution and call the architecture complete | The drawing leaves the connecting information, authority and feasible actions unspecified. | Derive the division from the needed decisions and construct each consequential exchange. |
| Give every local unit the whole resource limit | Simultaneously valid local choices can exceed the shared capacity. | Establish a joint allocation or coordination rule and its timing. |
| Forward every update immediately | Irrelevant changes consume attention; premature preparation can waste or reserve scarce resources. | Identify the receiving action and compare early preparation with waiting. |
| Escalate every exception | A decision can arrive after the last useful action or at a participant without the needed means. | Bound the actual response path or construct a qualified local continuation. |
| Call separate controller stability a whole-system guarantee | Reference changes, delay, estimation and interactions can violate the individual premises. | Derive or obtain the joint behavior under the real interface. |
| Treat a promise or benchmark average as a hard bound | The required availability, tail behavior or operating condition may be unsupported. | Use the warranted bound, uncertainty or conditional claim and change the reliance accordingly. |
| Improve the local rate while weakening the demanded outcome | The comparison changes the task and manufactures a gain. | Hold the receiving demand fixed or make the changed commitment an explicit alternative. |

### C.32.LCA:9 - Consequences

The reader can change the relation that prevents a result: the available information, allocation of a decision, command semantics, timing, shared capacity or the demanded outcome. An adequate incumbent can survive the comparison.

The method makes the price of separation visible. Layers can reduce immediate computation or authorization demand while adding models, interfaces and coordination. Delegation can remove waiting while adding qualification, communication and exposure. A simpler arrangement can be preferable.

Construction itself has a cost. Stop with sufficient grounds for the receiving decision; pursue additional modeling or evidence when a plausible result can change that decision or when a binding obligation requires it.

### C.32.LCA:10 - Architectural Rationale

The arrangement is constructed from joint use because the consequence belongs to the connected system or work. Local correctness is useful only when the receiver can use the result under conditions the rest of the arrangement can supply.

Different time demands justify considering a division, not prescribing one. Separation is advantageous when its saved computation, waiting or coordination exceeds the burden of preserving the lost dependence. The governor case shows that a smaller change can preserve a qualified component. The exhibition case shows that changing a decision right can matter more than increasing message speed.

Goal revision belongs in the architecture because feedback can make the selected outcome unattainable or no longer useful. Its authority remains distinct from the ability to compute another plan. This prevents a fast local optimization from silently changing the promise made to another participant.

Model-based guarantees and organizational commitments remain different contributions. Both can constrain a design, but their grounds and failure responses differ. That distinction makes the common method transferable without importing a control theorem into an enterprise through matching labels.

The current arrangement can itself become the subject of a slower development activity. That does not identify every operational goal revision with architecture development: choosing another authorized destination can preserve the arrangement, whereas moving decision rights or changing the available interventions changes it.

### C.32.LCA:11 - SoTA-Echoing

**Which line answers the working question?** For constructing joint control under different information, timing and authority, this pattern selects a synthesis of whole-arrangement comparison, explicit dynamic and temporal connections, and domain-specific qualification. A fixed three-layer template is cheaper to draw but leaves those connections to the reader. The additional work here is justified when a consequential dependency remains unresolved; :5 shows a changed command interface and an authority-dependent deadline. These are conditional constructions, not measured enterprise benefits. Retain a sufficient incumbent and reopen this choice if its extra analysis cannot change the receiving decision.

**Adopt joint design rather than independent layer tuning.** Matni, Ames and Doyle's [2024 treatment, §§2–3 and 4.5](https://arxiv.org/html/2401.15185) supports reasoning from a whole control problem to interacting layers. This changes :4.4 and :4.8: a removed consistency condition becomes an obligation to construct the connection. The source develops a research programme, not a universal optimal layer count. The common method adapts that question beyond its technical constructions; a claimed transfer still needs the receiving dynamics, conditions and evidence. Reopen when the proposed separation has no supported interface or a simpler controller answers the same demand.

**Adapt quantitative architectural co-design within its class.** [Verhoek et al., 2026, §§2, 5 and 7](https://arxiv.org/html/2610.20900v1) make model order, sampling ratio and controller parameters joint design variables for a two-layer LTI construction with compute constraints. Compared with fixed rate heuristics, this supports the whole comparison in :4.7–:4.10. The accepted cost is a demanding optimization and qualification problem. This is a bounded preprint result; general composition and several extensions remain open. Use a simpler qualified design when sufficient, and reopen on a changed plant, observation regime or implementation premise.

**Retain a governor as a serious alternative.** The [Garone, Di Cairano and Kolmanovsky survey, §§2 and 6](https://merl.com/publications/docs/TR2016-102.pdf) supplies the established alternative of managing commands over a pre-stabilized system. [Castroviejo-Fernandez and colleagues, 2024](https://arxiv.org/html/2401.02054v1), develop a disturbance-observer-based continuation. Their conditions motivate :4.5 and the observation change in :5.1. Adopt the architecture when its qualified loop and admissible-set construction answer the demand; reject treating it as automatic mission achievement. Its price is altered progress and model-dependent qualification. Reopen if those costs or assumptions defeat the receiving use.

**Adapt organizational design and commitment-based coordination.** [Joseph and Sengul's 2025 review](https://journals.sagepub.com/doi/10.1177/01492063241271242) compares organizational-design approaches rather than making decentralization a universal answer. [Guerreiro and Dietz, 2024](https://arxiv.org/pdf/2410.08215), preserve request, promise, declaration, acceptance and exceptional continuations in business-process descriptions. These lines change :4.2, :4.6 and :4.8: the organization must supply decision rights and workable commitments, not merely fast commands. Their use can add negotiation and coordination cost. Reopen when the decisive dependency is an unavailable capability, resource or conflicting interest rather than the proposed information or authority arrangement.

**Use safety analysis for its distinct result.** The [STPA Handbook, Chapters 2–3](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf), is an established approach to unsafe control actions and inadequate process models. Adapt its attention to timing, missing feedback and conflicting control in :4.3, :4.7 and :4.8. It is a serious alternative to checking only nominal performance when harmful loss is possible; it does not replace performance synthesis or prove absence of loss. Reopen the relevant safety analysis when a control action, model, responsibility or operating condition changes.

**Learned execution does not settle architecture qualification.** Figure's [Helix 02 description](https://www.figure.ai/news/helix-02) gives a concrete comparator: semantic reasoning, 200 Hz joint targets and 1 kHz whole-body execution with a learned lower component. It supports considering different functional and timing demands, not the superiority of that allocation in every system. Adapt the distinction in :4.9; retain a programmed qualified component as a rival. Reopen on a changed policy, observation distribution, latency or relied-on constraint. The vendor demonstration supplies no general enterprise or closed-loop safety theorem.

### C.32.LCA:12 - Relations

- **C.30.LCA** recovers the obtaining or proposed control structure represented in a view and its claim limits. This method consumes that account and returns constructed alternatives whose descriptions can be examined there.
- **B.2.5** establishes the observation, returned influence and coupling needed for a feedback claim. A new architecture proposal still needs evidence of those relations when put into use.
- **A.3.3, A.3.3.TR and A.3.3.PI** supply the dynamics, transition rule and predictive information. Their results enter the decisions and timing here; a changed input policy can reopen them.
- **C.32 and C.32.MLAO** supply candidate generation and changes that address a recovered cross-scope residual. This pattern adds the control-specific construction of information, intervention, timing and continuation.
- **C.32.MWA.PP:4.3–4.9** supplies construction and comparison of joint performance and provision, including shared means, workload, commitments and transition conditions. This pattern connects those conditions to the observation, decision and intervention that must occur in time. A proposed relation remains prospective until its obtaining conditions are met; changed authority or resource demand returns to the affected comparison.
- **C.11 and C.11.DUA** supply the local choice and the worth of further inquiry. The architecture explanation is their input; neither that explanation nor the choice establishes permission to act. **C.43** returns the selected arrangement to the connected continuation it must make possible.
- **C.28** governs reliance on a causal result when an empirical effect is used to justify the change. A conditional calculation retains its model premises.
- **C.39 and B.1.5.RS** support construction of a missing contribution and preservation of receiving uses when one contribution is replaced. A replacement that changes observations, timing or actions returns to the affected joint-condition analysis here.

### C.32.LCA:End
