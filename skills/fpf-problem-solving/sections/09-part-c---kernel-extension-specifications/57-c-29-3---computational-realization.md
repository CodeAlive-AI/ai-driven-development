## C.29.3 - Computational Realization

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative unless marked informative

### C.29.3:1 - Problem frame

**Use this when** a computation is available, but the proposed executing arrangement has not yet been connected to its inputs, operations and interpretable results. A motor interface may accept a different number from the one calculated. A circuit may produce a voltage whose scale differs from the input scale. A material admission procedure may preserve a count only while several people share the same stock of cards.

Start with one input the work needs. Explain how it is prepared in the proposed system, which actions perform the computation and how the result is read. Compare the interpreted result with what the abstract computation requires. A failed input preparation, such as a command outside the interface's range, can already determine a useful repair.

The first result is a realization design under stated conditions, an interpreted result from an execution, or a particular failed connection with a proposed correction. The method helps construct and use that connection. The engineering of a circuit, controller, physical apparatus or administrative arrangement supplies the mechanisms that perform the computation.

The reader should understand the intended computation and be able to obtain explanations of the system's relevant operations. The examples supply their arithmetic, elementary electrical account and card rules. More demanding uses need the corresponding knowledge of hardware, numerical methods, physical models or concurrent operation.

Use an adequate existing implementation directly when its inputs, behavior and result interpretation already meet the receiving need. Use C.29.2 when the computational procedure itself must be constructed. Use B.5.MPC when the open question also concerns which physical account and mathematical question can answer the original problem.

### C.29.3:2 - Problem

An abstract operation can be well defined while its proposed execution changes the question. The integer 63,662 can be the right calculated command and be delivered as -1,874 by an overflowing signed field. A circuit can correctly average two voltages while its user reads that average as their sum. Two attendants can each follow the same capacity rule while admitting twice the intended number of visitors through duplicated stocks.

The failure can occur before execution, during intermediate actions or when the result is interpreted. More arithmetic at the middle of the calculation leaves those failures in place. A successful trace of one input can also leave another required input outside the representable range, or omit an interleaving that breaks a shared-state assumption.

A practitioner needs to construct the correspondences, establish the property needed by the receiving use and locate which part to change when the interpreted execution fails to supply that property. The useful comparison can concern a value, a bound, a probability distribution or a property maintained throughout an interaction.

### C.29.3:3 - Forces

| Force | Working tension |
| --- | --- |
| Abstract freedom and available means | A mathematical input or operation may have no preparation or execution in the proposed arrangement. |
| Useful abstraction and intermediate behavior | One logical step can be convenient for reasoning while its physical implementation has consequential intermediate states. |
| Input meaning and output meaning | The same carrier can represent different quantities at different points; preparation and readout need their own interpretations. |
| A demonstrated case and a stated range | A small case exposes mistakes, while a claim covering many inputs needs an argument or evidence that covers them. |
| Precision and useful consequence | Exact equality may be unnecessary; an unexplained error can still defeat a threshold decision. |
| Fixed computation and adaptable arrangement | Changing an interface can preserve a computation; changing its formulation can sometimes use the available arrangement more effectively. |

### C.29.3:4 - Solution

Build and compare two routes from an input to the result required by the use:

~~~text
input → abstract computation → required result

input → prepared system
      → system actions
      → interpreted result
~~~

The second route must supply the result relation needed by the receiving work. This can be equality, a bound, agreement of output distributions or a property of continuing behavior. Input preparation and output interpretation can differ.

**Recover the needed result → prepare a representable input → construct the executing actions → interpret the output or behavior → compare the routes → repair the failed connection → use the sufficient result.**

Enter at an already available contribution. A known device behavior can guide a revised formulation; a settled implementation can supply an operation within a larger computation.

#### C.29.3:4.1 - Determine what the receiving work needs

State the inputs and the consequence to be supplied. For a terminating computation, identify the output and its meaning. For continued interaction, identify the property that must hold across the relevant histories: for example, whether another admission is permitted without exceeding capacity.

Choose the comparison accordingly. An integer command can require equality of counts. A physical readout can support an interval containing the computed value. A concurrent procedure can need a bound that holds during every permitted intermediate state.

For a sampling computation, identify the requested distribution or statistic and the discrepancy that the receiving use can tolerate. Individual draws from two adequate samplers can differ. If the computation supplies an estimate to a larger learning or control method, determine what accuracy that method needs from the estimate.

Keep the computational result and its later physical use distinguishable. A controller can calculate a command, and an actuator can then change a physical system. The calculation and the resulting movement consume different premises. In the robot example below, the interface must realize the intended count; interpreting that count as travel additionally uses the motion model.

Use the available premises for a conditional design. An assertion about a performed execution uses the observations and operating circumstances needed to establish that assertion. Additional testing is selected for what it could change in the receiving decision, through C.11.DUA.

#### C.29.3:4.2 - Construct input preparation

Explain how a required input is set in the system. Identify the physical or operational state that represents it: a stored value, an applied signal, an arranged material stock or another prepared condition.

Determine the admitted range and the relevant distinctions. A signed field has a finite range. A voltage input has units and a reference. A stock of three exclusive cards differs from two independent stocks of three. Recover initial state when the input is interpreted relative to it.

Apply the preparation to the required input. If it cannot be represented, choose among changing the encoding, changing the arrangement, restricting the input set or revising the computation. A large integer can sometimes be represented by several smaller values, but their execution must preserve the intended composition.

State rounding or other preparation loss in the same quantity that the receiving comparison uses. Retain a sufficient bound when it answers the question. Locate a lost distinction before deciding that a more precise number will restore it.

#### C.29.3:4.3 - Construct the actions that execute the operations

For each operation whose realization is unresolved, identify what the system does and how its state changes. Connect sequences through the state they leave for the next operation.

When one logical operation spans several physical actions, examine the intervening states. Reserving a card, crossing a room boundary and returning the card are separate events. A visitor can be outside while the card is unavailable. Either show that the intervening behavior preserves the needed result, or change the model or the arrangement.

For shared operation, determine how the same resource or state is accessed. Exclusive possession means that each card can be held by only one participant at a time. Independent copies of an available-card count require a different coordination mechanism. The applicable engineering or administrative method supplies that mechanism.

For repeated or timed operation, include completion, reset and ordering where they affect the result. Two relative increments add only when both are executed under the intended rule. Repeating an absolute target ordinarily asks for the same target again. An ongoing physical process can require a temporal model rather than a sequence of instantaneous assignments.

A physical evolution can itself perform the computation. Determine which initial preparation, controls and interval make its readout useful. A sampler may use a stationary law; a finite-time estimator may use a transient. Choose the evolution and reading rule for the requested result.

A.3.3 supplies the construction of state and permitted continuations. A.6.1:4.6 supplies the realization relation when a reusable operation declaration needs it. Their contributions leave the particular circuit, physical interaction or operating procedure to its subject method.

#### C.29.3:4.4 - Construct result interpretation

Identify the state or indication that the receiver can actually obtain, and explain how it yields the computational result. Give its scale, reference, timing and aggregation rule wherever those change the answer. When several observations yield an estimate, include their dependence in the sampling argument; the number of readings alone does not determine the estimate's uncertainty.

Derive this interpretation from the executing relation. An input scale need not be the output scale. In the analog example below, each input uses one volt for ten units, while the output uses one volt for twenty units.

Check whether different possible outcomes have become indistinguishable to the readout. Counting unavailable cards can bound occupancy without determining it. A command acknowledgment can establish receipt without establishing completed motion. In each case, return the consequence the indication supports.

Use C.16 when reading the result requires a measurement model. Instrument loading, calibration, finite resolution or disturbances enter that model when they change the inference. A bound or another suitable indication can answer the question without reconstructing an inaccessible exact value.

#### C.29.3:4.5 - Compare the routes over the claimed scope

Work a small input through both routes with its meanings intact. Then establish why the required relation holds over the input range or histories for which the result will be used.

For a finite case, a complete case analysis can suffice. For an invariant, show it in the initial state and show how every permitted operation preserves it. For an approximate result, propagate the relevant losses to the quantity used by the receiver. For a sampler or statistical estimator, compare the relevant distributions or estimation properties. Use the mathematical, numerical or empirical method appropriate to that claim.

For example, a required binary sampler gives output 1 with probability 0.5. Suppose the device model gives probability p between 0.49 and 0.51 under the intended preparation. The absolute discrepancy in that probability is at most 0.01, so it meets a tolerance of 0.02. Comparing two individual draws cannot establish or refute that distributional result. Estimating p from a finite run requires the sampling assumptions and uncertainty calculation appropriate to those observations.

When the requested result contains several random components, compare their joint behavior. Suppose the target is a pair of independent fair bits. Preparing one fair bit B and returning (B,B) gives the right distribution at each output separately. But the target assigns probability 1/2 to unequal outputs; this system assigns probability 0. Using two independent draws gives each of the four pairs probability 1/4 and restores the requested result. The realization must provide that joint sampling behavior. When its observations are dependent, use the actual joint law or change how the second component is obtained.

Choose changed cases from consequential features of the arrangement: an endpoint of the command range, a different initial state, an overlapping action or a possible indication error. These cases help locate failures. A sampled success supports the tested case; the broader argument supplies the broader conclusion.

Separate three possible outcomes:

- The interpreted execution supplies the required result under the stated conditions.
- It supplies a weaker result, such as an interval or occupancy bound, that may still answer the receiving question.
- A connection fails or remains unknown, and its location determines the next construction, observation or restriction.

#### C.29.3:4.6 - Repair the connection and its dependents

Return to the part that changes the answer. Repair input preparation when a value cannot be represented. Repair the execution when permitted actions violate the intended operation. Repair readout when the available indication has been given the wrong meaning. Revise the physical or computational model when its retained state cannot express the relevant behavior.

Compare repairs by the result the work needs. Restricting a command range may be sufficient for one device. Splitting commands may preserve a larger range at the cost of extra execution time. Include the preparation, conversion, repeated execution and readout consumed by the proposed repair when comparing its cost with the available alternatives. A stronger sensor may be unnecessary when a conservative bound already settles the action.

Revisit contributions that consume the changed value, meaning or condition. Retain independent results whose assumptions still hold. B.5.MPC connects this local repair to the wider physical, mathematical and computational question.

When adapting the formulation and the apparatus together could improve the result, compare both directions. Ask which physical operations are available, how they can be interpreted computationally, and which change to the arrangement would make the useful operation easier or more reliable. C.29.2 develops the resulting formulation. Designing a new computational model or notation can require a substantial further method; name that task when the present construction reaches it.

#### C.29.3:4.7 - Return the result at the strength obtained

Give the usable realization, input conditions, interpreted consequence and the change that would require reconsideration. Preserve the derivation or operating explanation at the depth needed by its receiver; a short calculation may be enough.

A conditional design can finish before a device is built. An observed execution can establish a result for its actual conditions. An identified incompatibility can stop an unsuitable implementation and open another. Further information or assurance is obtained when the receiving use requires its contribution.

### C.29.3:5 - Archetypal Grounding

These constructed cases expose different realization failures. They establish consequences of the stated models; using an actual apparatus also requires the relevant physical and operating knowledge.

#### C.29.3:5.1 - Carry a calculated count through a finite command interface

A robot's supplied motion model uses rolling without slip, effective wheel radius 0.05 m, ten motor revolutions per wheel revolution and one thousand commanded increments per motor revolution. Positive motor increments produce forward travel. Successful execution completes the requested relative increment.

For a requested distance d, calculate and round:

~~~text
N = nearest integer to ((d / (2π × 0.05 m)) × 10 × 1000)
modeled displacement = N / 10000 × 2π × 0.05 m
~~~

One metre gives 31,831 increments and a modeled displacement of approximately 1.0000003576 m. Rounding contributes at most half an increment, approximately 0.0000157080 m. This bound concerns command discretization under the supplied motion relation.

The interface accepts signed 16-bit values from -32,768 to 32,767. The one-metre input is representable. Two metres require 63,662 increments, which cannot be prepared as one positive value in that field.

Suppose the interface wraps modulo 65,536 and interprets the result as signed. Then:

~~~text
63,662 − 65,536 = -1,874
modeled displacement ≈ -0.0588734463 m
~~~

The calculation of the desired count remains correct; input preparation changes the delivered count. An interface that rejects the value would produce a different failure, so the actual interface behavior matters.

One repair uses two completed commands of 31,831. Under the relative-addition rule, their total is 63,662 and their modeled displacement is approximately 2.0000007151 m. The preparation now supplies two representable values, and the execution argument uses addition across their completed displacements.

If a command means "reach this absolute count," repeating 31,831 leaves the same target. For an absolute interface, reconstruct the target from the initial count and check that the resulting target is representable. B.5.MPC supplies the wider comparison when the motion model or the count's physical meaning also changes.

A range restriction is another useful repair. The largest positive relative command corresponds to approximately 1.0294056648 m under this model. Whether that restriction is adequate depends on the requested motion. A deadline can make two commands unsuitable even when their displacements add.

The result is a command procedure with a stated input range and composition rule. For actual travel, determine whether the commands were completed and use a measurement or physical relation that accounts for consequential slip and effective radius.

#### C.29.3:5.2 - Read an analog sum with the output scale it needs

An existing analog channel is intended to supply the sum of two numbers x and y in the range 0 to 10. Its input preparation sets voltages:

~~~text
Vx = x / 10 volts
Vy = y / 10 volts
~~~

Each source is connected through an equal resistor R to one common node. The supplied electrical model has ideal voltage sources, equal resistances, settled behavior and a readout drawing negligible current. The resistor-current relation and current balance at the node give:

~~~text
(Vx − Vout) / R + (Vy − Vout) / R = 0
Vout = (Vx + Vy) / 2
~~~

The arrangement physically produces an average voltage. To obtain the intended sum, derive its readout:

~~~text
decoded result = 20 × [Vout expressed in volts]
               = x + y
~~~

For x = 8 and y = 6, preparation gives 0.8 V and 0.6 V. The node gives 0.7 V. Decoding returns 14. Reusing the input scale, ten units per volt, would return 7.

The abstract and physical routes now agree. Input preparation and output interpretation use different factors because the intervening operation halves the voltage sum.

Now allow each prepared input voltage an error of at most 0.001 V. Suppose the readout indication has an additional error of at most 0.002 V under the same circuit model. The worst-case error in the indicated output is:

~~~text
0.5 × 0.001 V + 0.5 × 0.001 V + 0.002 V = 0.003 V
decoded-result error ≤ 20 × 0.003 = 0.06
~~~

An absolute tolerance of 0.1 is therefore met under these bounds. A tolerance of 0.01 is not established by them. Better input setting or readout, a different realization, or a weaker receiving requirement would need comparison. The bound is deterministic; no cancellation or probability distribution has been assumed.

If the instrument loads the node or the resistor values differ, the stated averaging relation needs revision. Those changes belong in the circuit and measurement account, through C.16 where appropriate. The common realization method supplies the preparation/execution/readout comparison and the receiving error calculation. Electrical design supplies the physical law and actual component behavior.

#### C.29.3:5.3 - Preserve a bound during material admission operations

A demonstration room has a capacity of three visitors. It starts empty with three distinct cards in a free stock. One card is issued to a visitor before entry; the visitor retains it inside and returns it after exit. Every entry follows this rule, each visitor inside holds one card, each card is exclusively assigned, and cards are not lost or duplicated.

The computation is the continuing admission decision and preservation of the capacity bound. People and material transfers execute its finite-state procedure.

A card can be Free, Reserved outside, Inside with its visitor, or Awaiting return after exit. Let F, R, I and E count those states. The fixed stock gives:

~~~text
F + R + I + E = 3
occupancy = I
occupancy = 3 − F − R − E ≤ 3 − F ≤ 3
~~~

Issuing a card changes Free to Reserved. Entry changes Reserved to Inside. Exit changes Inside to Awaiting return. Return changes Awaiting return to Free. Cancellation can return a Reserved card to Free while its visitor remains outside.

Every operation moves one existing card between states. Entry requires its exclusive reservation. Return requires that its visitor is outside. These conditions preserve both the stock and the association between visitors inside and Inside cards. They establish the capacity bound throughout permitted histories, including overlapping admissions.

After two cards have been issued, one visitor may be inside and the other waiting outside. Then F = 1, R = 1, I = 1 and E = 0. The count of unavailable cards is 2, while occupancy is 1. Reading occupancy as 3 − F would be wrong. That count is an upper bound until R = E = 0.

A second entrance can share the same stock or receive a partition of it, such as two cards at one entrance and one at the other. Both preserve the total of three. Giving the second entrance three copied cards instead permits six simultaneous admissions, despite each attendant following their local procedure.

Partitioning can cause waiting at one entrance while a card is free at the other. Moving an existing free card preserves the total; creating another accepted card changes it. This separates the capacity property from the additional question of useful service across entrances.

The result is a conditional admission arrangement, its preserved bound and a qualified reading of the free stock. The administrative method supplies controlled entry, exclusive possession and return. The mathematical construction makes explicit which physical and procedural properties the computation consumes.

### C.29.3:6 - Bias-Annotation

| Bias | Action-changing consequence | Correction |
| --- | --- | --- |
| A correct program is taken to settle its execution | A valid count is changed by preparation or readout. | Follow a required input through the actual encoding and interpretation. |
| Input and output are assumed to use one scale | The analog sum is read as half its value. | Derive the output interpretation from the executing relation. |
| Logical atomicity is projected onto physical actions | Reservations and unfinished returns are counted as occupants. | Represent the intermediate states or establish why they leave the required property intact. |
| Local success hides a shared resource | Two locally correct stocks exceed one room's capacity. | Recover the common stock or state and how each participant changes it. |
| Numerical precision dominates the account | Command-rounding error hides a larger physical uncertainty. | Express the consequential losses in the receiving quantity before selecting a refinement. |

### C.29.3:7 - Conformance Checklist

Apply the checks to the particular realization and use. Their answers can remain in the working calculation, diagram or operating explanation.

| Check | What must be recoverable |
| --- | --- |
| CC-C29.3.1 - Required result | The computation, admitted inputs and receiving equality, bound or continuing property. |
| CC-C29.3.2 - Input preparation | A way to prepare each claimed input, with its range, initial state and consequential loss. |
| CC-C29.3.3 - Executing actions | System actions and state changes that perform the operations, including relevant intermediate states and shared access. |
| CC-C29.3.4 - Interpretation | The obtainable state or indication and the relation that turns it into the result used. |
| CC-C29.3.5 - Scope of comparison | A constructed case and the argument or evidence supporting the claimed input or behavior scope. |
| CC-C29.3.6 - Changed conditions | Which preparation, execution or interpretation must be reconsidered when range, timing, ordering or uncertainty changes. |
| CC-C29.3.7 - Usable outcome | A sufficient realization or interpreted consequence, or a named incompatibility with the next repair. The strength of the claim matches its grounds. |

### C.29.3:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails here | Repair |
| --- | --- | --- |
| Send an unrepresentable answer | A signed field wraps or rejects a value that is valid in the calculation. | Change the encoding or realization, or restrict the admitted input. |
| Split a command without recovering composition | Two absolute targets do not add like relative increments. | Explain the state and rule connecting the completed commands. |
| Read the carrier by its familiar scale | The circuit's physical average uses a different decoding from its inputs. | Derive and use the receiving scale. |
| Infer exact occupancy from unavailable cards | Some assigned cards are outside during reservation or return. | Use the four-state account or retain the upper bound. |
| Treat one successful run as every required run | An untested endpoint or interleaving can change the result. | Supply the argument or evidence that covers the declared use. |
| Require a new trial for an adequate conditional design | The trial may leave the design decision unchanged. | Finish with the sufficient conditional consequence; obtain further information when its use warrants it. |

### C.29.3:9 - Consequences

The practitioner can locate an implementation failure without replacing every part of the reasoning. The desired count, arithmetic and motion model can remain useful while input encoding changes. A readout can be repaired while the circuit remains intact. A shared-stock rule can preserve capacity while another method improves waiting time.

The comparison also clarifies the division of work. One contributor supplies the computation, another the executing mechanism, and another the needed measurement relation. Their results join through the preparation and interpretation that the receiving use consumes.

Constructing those connections can cost more than the displayed calculation. Reuse settled implementations and sufficient bounds. A new device, computational model or concurrency mechanism can require substantial specialist work beyond the common method.

### C.29.3:10 - Architectural Rationale

#### C.29.3:10.1 - Why realization needs its own method

Mathematical result transfer compares accounts and their operations. Computational formulation constructs a procedure for the requested result. Realization begins with that procedure and asks how an executing arrangement supplies it. Its new work is preparation, physical or operational execution, readout and comparison under the conditions of use.

A.6.1 provides the declaration and realization relation. It leaves the design and interpretation of a particular executing arrangement to the method that uses the relation. C.29.3 supplies that constructive work within the mathematical-use family. The method can be entered directly with an available computation.

Checking a program alone is useful when its execution environment is already established. It is insufficient for the unresolved interface, readout and shared-stock cases here. The present comparison follows only connections on which the receiving result depends.

#### C.29.3:10.2 - Preparation, execution and interpretation

[Horsman and colleagues (2014)](https://arxiv.org/abs/1309.7979) distinguish abstract computation from its use through physical preparation, evolution and representation. Adopt their comparison as the basis for :4. The practical extension here is to return the equality, bound or behavior needed by the work, and to repair the particular connection that defeats it.

That account is one theory of physical computation. The method uses its constructive comparison without settling every philosophical classification of computing systems. For the declared use, establish whether the interpreted execution supplies the required result under the stated conditions, using :4.5.

The examples explain why both directions matter. Input preparation asks what state can be made; output interpretation asks what result can be obtained from the state or indication. They can have different scales, ranges and physical means.

#### C.29.3:10.3 - Realization and the surrounding physical activity

A computation can contribute to physical control while the controlled system continues to evolve. [Horsman, Stepney, Clarke and Kendon (2026), §§3.3–3.4 and 5.3](https://arxiv.org/html/2604.16162v1) distinguish the compute cycle within control from the broader physical control cycle. Adopt that distinction in :4.1 and the requirement to include consequential timing in :4.3.

The robot calculation supplies a command; the command's execution and its relation to travel supply further claims. In the card arrangement, the abstract admission rule is carried through reservation, crossing and return. The physical conditions that maintain those relations must remain understandable.

#### C.29.3:10.4 - Changing model and means together

A fixed computation can be a useful constraint on the device design. A fixed device can instead suggest more suitable computational operations. [Stepney (2019), §§4–5](https://eprints.whiterose.ac.uk/id/eprint/147381/) proposes combining these directions in model-and-substrate co-design.

[Kalita and colleagues (2026), §§1 and 3–4](https://arxiv.org/html/2603.24531v1) develop the reverse direction through a bosonic-device example: capabilities of the physical system inform a computational model and language. Adapt this source contribution as the formulation return in :4.6. Developing such a language requires its own constructive repertoire; a return from realization identifies that work rather than completing it.

The analog example shows a small instance of the same design freedom. Keeping the averaging circuit and changing its encoding or decoding can supply a useful addition operation. The physical relation constrains which interpretation works.

Thermodynamic sampling and optical ML hardware extend this design choice to computations based on distributions or iterative physical evolution. [Melanson et al. (2025)](https://www.nature.com/articles/s41467-025-59011-x) demonstrate sampling and matrix inversion on a small stochastic circuit. [Kalinin et al. (2025)](https://www.nature.com/articles/s41586-025-09430-z) co-design an optical/electronic fixed-point computation with its learning model. Their different result and execution forms motivate the choices in :4.1–4.5. The detailed sampler, model-training and device-construction Methods supply the corresponding specialist work.

### C.29.3:11 - SoTA-Echoing

The selected answer combines a physical-realization comparison with scope-sensitive result use and a return to formulation when the available means suggest a different construction. The examples are authored conceptual synthesis under their stated models.

| Working question | Source contribution and selected use | Comparison and limit |
| --- | --- | --- |
| How does an abstract result become obtainable through a physical arrangement? | **Adopt** preparation, evolution and interpretation from Horsman et al. (2014), as used in :4.2–4.5. | Compared with abstract refinement alone, the comparison exposes input and readout failures. The theory's general classification claims are outside this method's required conclusion. |
| How does computation participate in physical control? | **Adapt** the compute-cycle/control-cycle distinction from Horsman et al. (2026) in :4.1 and :4.3. | The preprint sharpens the timing and output question. Its broader claim about all control systems is not needed to establish these worked cases. |
| Should the device or the computational model change? | **Adapt** Stepney's 2019 co-design proposal and Kalita et al.'s 2026 substrate-to-model construction as the two-way return in :4.6. | A fixed-model implementation remains preferable when it meets the use at lower cost. The bosonic example demonstrates a particular methodology; it establishes no general performance advantage for every substrate. |
| How is a stochastic program realized? | **Adapt** the distinction between a target stochastic program, its compiled kernels and its interpreted readout from [Amico et al. (2026), III and V](https://arxiv.org/html/2608.01615v1), in :4.1 and :4.5. | Comparing local operations, composed output laws and receiving-task results can reveal different failures. The preprint's compilation demonstrations do not establish a general hardware energy advantage. |
| Must physical evolution reach equilibrium? | **Adapt** the finite-time approximation choice from [Thermodynamic natural gradient descent (2026), Results](https://www.nature.com/articles/s44335-025-00049-x), in :4.3. | A useful inner estimate can support the learning update before equilibrium. The reported thermodynamic timing is estimated; select the interval by the receiving computation's requirements. |
| How much additional checking is useful? | **Use** C.11.DUA to compare what a further observation, proof or trial could change. | A conditional design can be sufficient. An actual-performance or wider-range claim needs the grounds that its receiving use consumes. |

Reconsider the realization when a required input, observation relation, execution condition or receiving tolerance changes. A new substrate or computational model can also change which preparation, operations and interpretation are worth developing.

### C.29.3:12 - Relations

| Relation | Contribution to the work |
| --- | --- |
| C.29 - Mathematical Lens Use | Provides the general correspondence-and-return method and discovery of this realization difficulty. |
| C.29.1 - Mathematical Result Transfer | Compares operations between accounts when the computational representation itself changes. |
| C.29.2 - Computational Formulation | Supplies or revises the interpreted procedure that the arrangement is intended to perform. |
| B.5.MPC - Connect Physical, Mathematical and Computational Reasoning | Connects the local realization to the physical question, mathematical construction and useful consequence. |
| A.3.3 - U.Dynamics | Constructs the state and permitted continuations needed to reason about intermediate or repeated operation. |
| A.6.1 - U.Mechanism | Supplies operation-declaration and realization semantics when those relations are asserted. |
| A.6.3.RT - Representation-Scheme Transition | Helps change the representation of preparation, operations and readout under an available scheme while preserving the content needed for use. |
| C.16 - Measurement and Metrics Characterization | Supplies the measurement relation and the interpretation limits of a physical indication. |
| C.11.DUA - Decision-Useful Advice and Evidence Demands | Selects further assurance or information by the receiving decision and its cost. |

### C.29.3:End
