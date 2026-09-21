## B.5.MPC - Connect Physical, Mathematical and Computational Reasoning

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative unless marked informative

### B.5.MPC:1 - Problem frame

**Use this when** a physical question needs contributions from mathematics and computation, and their results do not yet form an interpretable answer together. You may be choosing a robot command, determining whether a gear arrangement can turn, or organizing entry to a room with a finite stock of cards. The difficulty is to connect what the physical arrangement does, what the mathematical result establishes, and what the procedure and its execution actually produce.

Begin with the difference the answer should help you understand or make possible. Take one available contribution and explain what it would have to mean, and what else would have to hold, for that contribution to answer the question. Work the first missing connection far enough to obtain a consequence or locate the next missing contribution. For a motion command, this might already reveal that the supplied count concerns motor revolutions while the distance model concerns wheel revolutions.

The result is a connected solution, a useful conditional consequence or bound, or a particular missing connection that directs the next inquiry. This pattern specializes B.5's choice and connection of inquiry contributions for this joint physical, mathematical and computational difficulty. It governs the reasoning that connects those contributions. Physical laws, mathematical constructions, algorithm design and the engineering of an executing arrangement supply their respective subject content.

This is an epistemological and methodological synthesis. The epistemological question is what the connected contributions allow us to know: what follows from the constructions and premises, and how those consequences bear on the physical situation. The methodological question is how agents obtain and apply that knowledge, divide the work and change their methods. A result can support a physical change, expose a limitation or make a further question worth pursuing.

A practitioner needs enough preparation to recover the question, follow the meanings of the important quantities and operations, and recognize where specialist help is needed. The worked cases explain their elementary algebra, graph and counting constructions. A more demanding application can require additional physical theory, mathematics, computation or measurement expertise; obtain that contribution with its explanation when it is missing.

Use an already adequate calculation, implementation or operating procedure directly when its connection to the intended physical use is settled. A proof or bound can answer a physical design question before implementation is worthwhile. For an actual performance claim, add the observations, measurement relation and evidence needed for that claim; a conditional construction alone answers only what follows under its assumptions.

### B.5.MPC:2 - Problem

Individually correct contributions can fail to support a joint result. A physical model may concern accumulated wheel rotation, a mathematical variable may represent orientation modulo one turn, and a program may accept an absolute target. Each account can be consistent while their composition loses the displacement that the user requested.

The same difficulty occurs without numerical approximation. A graph can correctly encode a chosen contact list, and a program can correctly colour that graph, while the contact list omits an actual mesh. A count invariant can be proved while the proposed admission procedure creates two independent stocks of cards. Improving the proof or the program leaves the missing physical correspondence untouched.

A simple division into “physics first, mathematics second, implementation last” also fails when a later contribution exposes an earlier omission. The interface may require initial state that the first model discarded. A measurement may distinguish fewer cases than the calculation assumes. A mathematical obstruction may make further computation unnecessary. The practitioner needs a way to construct the dependencies, use an available contribution at its point of need, and return a failure to the contribution that can change it.

### B.5.MPC:3 - Forces

| Force | Working tension |
| --- | --- |
| Shared answer and distinct expertise | Specialists can work independently on contributions, while their results must concern compatible participants, assumptions and operations. |
| Useful simplification and physical interpretation | Omitting detail can make a problem tractable; an omitted distinction can determine the requested action. |
| Constructive freedom and justified consequence | New models, expressions and procedures can open a useful route; their decisive properties require the relevant physical or mathematical grounds. |
| Abstract result and executing means | A computation can be correct for its stated inputs while the proposed apparatus cannot prepare, represent or execute those inputs. |
| Reuse and change | Existing results save work, but their use depends on the premises and interpretations that the new question consumes. |
| Explanation and available effort | A person or team needs enough understanding to use and question contributions without reconstructing every discipline before an ordinary decision. |

### B.5.MPC:4 - Solution

Construct the answer by connecting the contributions it actually needs. For each connection, identify the supplied result, the receiving operation and the condition that makes the result usable there. Follow those meanings through a small instance. If the connection is missing, construct it, obtain it from a suitable contributor, or return the particular missing result that prevents the next move.

The long mantra keeps the whole question available while attention moves between contributions:

**Orient by the physical question → propose the relevant physical account → construct a mathematical question and its interpretation → obtain a result and, where needed, a computation → connect its execution and observations to the intended quantities → return the consequence to the physical question → choose the useful action or the next missing contribution.**

The arrows recall result dependencies. They do not prescribe the order in which people must discover, receive or develop every contribution. A ready theorem, algorithm, measurement or physical mechanism can be the first available input.

#### B.5.MPC:4.1 - Recover the physical difference the answer should resolve

Identify the thing or situation being understood or changed. Say which difference would make an answer useful: a displacement within a stated tolerance, the possibility of coupled rotation, a capacity bound during entry, or another consequence the work needs. Include the relevant boundary and operating conditions when changing them could change the answer.

Then recover what is already available. An engineer may have a trusted motion model but an unfamiliar command interface. A mathematician may have an odd-cycle theorem and ask which physical arrangements its obstruction describes. A room attendant may have a reliable card procedure and want to extend it to a second entrance. Enter through that available contribution and recover only the other results needed to answer the question.

Use B.5:4.1 when the question itself needs formation or revision. B.5.4 helps recognize the participants and relations of an explained concept in a concrete situation. If the receiving use is still unclear, work one small consequence of the available result and ask what it would let someone decide or do. Retain a theoretical question when its answer could enable a worthwhile construction, explanation or later inquiry.

#### B.5.MPC:4.2 - Propose the physical account and the observations it needs

Identify the participants, interactions and configurations that could determine the requested difference. Give separately used quantities their participants and reference conditions: the robot's distance to a wall before motion, its distance afterwards and its displacement are three quantities, even though each is called a distance. Start from the arrangement and relevant subject knowledge. For a rolling robot, distinguish wheel, motor, transmission and ground contact. For gears, distinguish an actual contact from proximity in a drawing. For admission cards, distinguish a material card, its holder, the room boundary and the permitted transfers.

State the applicable physical or operating rules. Explain why a rule supplies the needed relation and where it is an assumption. Wheel rotation yields a distance relation only under the chosen rolling and geometry conditions. Exclusive possession of a card supports an admission limit only when the entrance procedure connects possession to entry and return. A.3.3 helps construct configurations, retained state and allowed continuations; the subject practice supplies the laws and mechanisms those continuations use.

Choose a sufficient account for the present question. A direction or impossibility result may need less physical detail than a trajectory, speed or load calculation. Make an omitted interaction explicit when it could defeat the inference: slip changes wheel travel, a moving gear carrier changes relative rotation, and uncontrolled entry breaks the visitor-to-card association.

When observations supply an input or test a consequence, construct the relation between the sought quantity and the indication. Use C.16:5.3 and C.16:5.4 for the measurement method and model. Motor counts can indicate motor rotation under an encoder account; using them to establish travel additionally consumes the transmission and ground-contact account. If the available indication cannot distinguish the cases needed by the question, obtain a different observation, use an adequate bound, or change the question.

Return a proposed physical account and its consequences under stated conditions. An unknown interaction or calibration is a useful missing contribution when it determines which mathematical question can be constructed.

#### B.5.MPC:4.3 - Construct an interpretable mathematical question and expression

Choose mathematical objects and operations that retain the distinctions needed by the physical question. State what their important elements mean. For instance, let a vertex denote one particular gear, an edge denote a specified mesh, and a colour denote the sign of rotation when viewed from one common side. A colour number has meaning through that interpretation.

Construct the relation that connects the physical rules to the mathematical constraints. Derive a distance per motor increment from wheel circumference and transmission ratio; derive an opposite-colour constraint from the external-contact rule; derive a count invariant from a fixed stock and its permitted transfers. C.29:4.1 supplies the general correspondence-and-return method. When an operation or a compressed representation must preserve a result, use C.29.1 to compare performing the source operation and then transferring its result with transferring the inputs and then performing the receiving operation.

Work the distinction that could defeat the representation. A wheel orientation repeats after one turn; accumulated travel can continue to increase. A graph of opposite-direction contacts answers a different question from a graph in which an edge merely means “these parts are connected.” If two physical cases receive one mathematical representation but require different answers, retain their distinguishing information, restrict the cases or seek a weaker consequence.

Keep the relation available when the question changes. Identify which quantities are now given and which must be obtained, then derive the computational direction that serves that question. Under a model `d = v*T` and `v = k*u`, where u is a motor command setting, positive k, u and T permit `T = d/(k*u)` for a duration question or `u = d/(k*T)` for a command question. Obtain k and the range in which the speed model applies from the physical account. The device's word “power” needs its interface meaning; u is not assumed to be physical power in watts. A resulting command outside the supported range returns a realizability question.

For a conditional example, let u be dimensionless and let `k = 0.2 m/s`. A distance `d = 1 m` at `u = 0.5` takes `T = 10 s`. Changing the requested duration to `T = 5 s` requires `u = 1`. If the available range is `0 < u <= 0.8`, the shortest duration under this model is `1 / (0.2 * 0.8) = 6.25 s`. Returning that bound lets the requester change the deadline or seek a different realization.

An equality constrains the quantities in this model. A program assignment changes a stored value according to its execution rules. Construct the needed assignments or solver from the relation after selecting the givens and unknowns; C.29.2 supplies that formulation Method.

Make an expression that supports the next operation. Use A.6.3.RT:4.1 to express the givens and constraints under an available scheme and compare the result with its source. Put units and participant names where their absence permits the wrong operation. Keep a shared quantity recognizable across expressions, such as the same wheel revolution in the transmission ratio and circumference relation.

Notation can contribute to obtaining the result. A table can expose mutually exclusive card states; a graph can make a closed contact path traceable; a labelled equation can reveal the missing subtraction of an initial position. The subject Method supplies the construction or inference performed with those expressions. If the available scheme cannot express the needed distinction, change the scheme or obtain notation-design work before treating its expressions as adequate.

#### B.5.MPC:4.4 - Obtain a sufficient consequence or construct its computation

Choose the result the use needs: a value, distribution, statistic, bound or property of ongoing behavior. A witness can establish one feasible arrangement; a counterexample can refute a general claim; a proof can establish an obstruction; a bound can settle a threshold decision. Compute an exact numerical answer only when that answer contributes to the use.

When a procedure is needed, construct its inputs, retained state, elementary operations and output interpretation. Explain how it obtains the mathematical result and why it terminates, or which property it preserves during continued interaction. C.29.2 supplies this formulation work; the relevant algorithmic or mathematical Method supplies the actual construction and its argument. B.5:4.2 and B.5:4.3 help recover a construction or a decisive proof step that the available explanation leaves inaccessible.

Trace one instance with its meanings intact. In a two-colouring procedure, a waiting list records vertices still to be processed, while parent links can reconstruct a failed closed path. In a motion calculation, the integer is a count of a particular kind of increment. In an admission procedure, taking a free card changes a finite state and determines whether an entry may proceed.

For a numerical approximation, carry the error that can affect the physical use. Separate rounding of a computed command from uncertainty in radius, calibration or physical response. For a resource claim, include the cost of obtaining the input, representing it and interpreting the output when those costs matter. Counting one graph-edge inspection as one operation is useful under an adjacency-list cost model; it does not estimate the effort of discovering the actual contacts.

Use a supplied proof or computation when its premises, meaning and relevant resource conditions fit. If a necessary construction remains unknown, state the missing operation and what it must connect. C.39 supplies the search for or development of a missing way. A conditional answer or a less demanding bound can finish the current question while that larger construction remains open.

#### B.5.MPC:4.5 - Connect the computation to preparation, execution and observation

Begin with the abstract input and explain how the proposed arrangement represents it. Then identify the system actions that perform the operations and the observation or final state from which the result is read. Use C.29.3 for this realization comparison.

Compare two routes for the same input:

~~~text
abstract input → stated computation → abstract result
abstract input → prepared system → system operation → interpreted result
~~~

The comparison asks whether the second route returns the equality, bound, statistical agreement or behavioral property that the receiving use needs. Input preparation and output interpretation can use different relations. Preparing a motor command and reading robot displacement are different operations; counting free cards and authorizing one transfer use different aspects of the same arrangement.

Recover range, units, initial state, ordering and completion conditions at the point where they affect that comparison. A signed command field cannot carry every positive integer. A command meaning “add this displacement” differs from one meaning “reach this position.” A material card available for transfer cannot simultaneously be assigned to another visitor.

Include the timing and retained physical state that the comparison consumes. When a controller is paused for debugging, determine which physical processes continue and which command remains active. Observe or replay the operation with the timing it needs, or interpret the changed run under its changed conditions. Establish the event that completes the requested physical action; program termination, a command acknowledgement and motor stopping can occur at different times. For an observation, include a settling interval or other preparation when the measurement relation requires it.

For a design question, use the stated model of the executing arrangement and return a conditional realization. For a claim about what happened, obtain the corresponding observations and their interpretation. A command receipt can establish that a command was accepted while leaving its successful physical completion open.

Use an existing adequate implementation directly when this comparison is already settled for the receiving use. A manual procedure, analog apparatus or controlled material transfer can supply an execution. Its adequacy follows from its permitted operations and interpretation, not from whether it contains digital software.

#### B.5.MPC:4.6 - Keep joint requirements and alternative routes distinguishable

Recover dependencies by asking, for each needed result, “What results and conditions make this operation possible, and what other operation could supply the same receiving need?” Keep the answer with the actual derivation, diagram or working explanation. A short case may need only a sentence; a shared design may need an explicit dependency diagram.

An **AND dependency** means that contributions are needed together for the stated inference. The robot's distance per motor increment uses the effective wheel radius, transmission ratio and increments per motor revolution together. Replacing any one can change the command.

An **OR alternative** is a different sufficient way to obtain the result needed by the receiving use. A proved upper bound and an exact computation can be alternatives for deciding whether a limit can be exceeded. Each route retains its own assumptions. Two different approximations do not become sufficient alternatives merely because both return a number.

For a conditional physical consequence, one useful small rendering is:

~~~text
applicable physical account
AND mathematical interpretation
AND (sufficient direct consequence OR sufficient interpreted computation)
→ consequence for the physical question
~~~

The computational branch additionally depends on a procedure and an adequate realization for any claimed execution. A claim about observed physical behavior adds the observations and measurement relation it consumes. These are different claims and can end the work at different places.

Keep a shared premise attached to every contribution that consumes it. Both an analytical calculation and a numerical simulation can depend on the same no-slip assumption. Switching between them does not remove that dependency. Conversely, when an upper bound already answers the decision, the exact optimizer need not be obtained.

Enter a ready result at the place where it is used. Recover its inputs and conditions backward, then continue forward with its consequence. When a missing input blocks one route, compare another sufficient route using the available inputs. Do not combine an output from one route with the assumptions of another without establishing their compatibility.

A failed connection can send the inquiry back to its physical account, mathematical construction, notation, procedure, realization or question. Use B.5.MPC.R to locate the incompatibility, construct a sufficient repair and carry it through the affected contributions. If several causes remain compatible with the observations, obtain a discriminating contribution or use a sufficient conditional result. B.5.RA supplies argument recovery and B.5.RR supplies general reasoning revision; C.29.1, C.29.2 and C.29.3 supply the transfer, formulation and realization methods respectively. Retain unaffected contributions whose conditions and meanings still hold.

#### B.5.MPC:4.7 - Return the consequence and choose what to do with it

Explain the result in the original physical terms. A count becomes a modeled displacement; an odd cycle becomes a set of contacts that prevents the stipulated nonzero rotation; a card invariant becomes a bound on occupancy under the entry rules. State what the result enables and the condition that changes that use.

When the consequence is insufficient, make the next contribution specific. “Determine whether these two wheels slip differently under this load” can direct physical work. “Find a representation that retains accumulated turns” can direct mathematical formulation. “Establish whether this interface interprets the number as an increment or an absolute target” can direct realization work. The uncertainty itself can be the result if locating it prevents further work on the wrong question.

Distinguish the consequence of an obstruction. A mathematical contradiction blocks a construction under its stated premises. A physical restriction blocks an intervention under the applicable laws. An expensive computation can remain mathematically possible while unavailable within the resources of this use. Their repairs can require different questions, arrangements or Methods.

Stop when the supported result answers the intended use. When development is the purpose, work one consequential variation far enough to reveal a new construction, obstruction or missing operation. Explain which additional action or longer inquiry it could enable. B.5:4.4, C.39 and C.40 supply the corresponding question and repertoire development; continued work is justified by that use.

#### B.5.MPC:4.8 - Divide human and AI contributions by the result they must supply

Allocate work around the dependencies above. A contributor can supply a physical account, a mathematical construction, a proof, a computation, a proposed realization or an explanation of the connection. State the working question, available inputs, missing result and intended use when obtaining help through A.15.9. Ask for the formulation itself when the equation has not yet been constructed.

Retain enough understanding at each receiving point to use and question its input. The receiver of a motion count should be able to identify its unit, the rotation it counts, its sign and its dependence on the motion model. The receiver of a two-colouring result should be able to connect the returned labels or odd-cycle witness to the actual contact list. The receiver of an occupancy bound should be able to identify the material and procedural conditions that preserve the stock.

That understanding can be held by one person or distributed across people and AI with an effective way to obtain a missing explanation. Arrange a capable contribution for each consequential connection. A completed report alone does not establish that this capability is available when a premise changes.

Choose depth from the later work. Using a stable formula may require interpretation and checks at the connection. Changing the formula requires understanding its derivation. Designing a new algorithm or physical theory requires the additional specialist capability. When assessing a person's preparation, examine their contribution on representative work with the assistance that will actually be available. Include a change of the requested result or a relevant premise when later work requires that adaptation. Ask the practitioner to recover the retained relation, the new unknown and the dependent physical operation.

### B.5.MPC:5 - Archetypal Grounding

The following are constructed cases under stated assumptions. They show how the coordinating Method obtains a jointly interpretable consequence. Physical motion, an assembled gear mechanism and an operating admission system require their corresponding physical arrangements and evidence.

#### B.5.MPC:5.1 - Construct a robot command from a motion question

An engineer wants a robot to advance by 1 m along a straight guide. The guide keeps its direction fixed. For this calculation, the effective rolling radius of the driven wheel is 0.05 m; rolling occurs without slip; the transmission makes ten motor revolutions for one wheel revolution; and successful execution advances the motor by one thousand commanded increments per motor revolution. Positive motor motion is defined to produce forward travel. The initial question is a conditional command design under those assumptions.

First construct the relation from the participants. One wheel revolution rolls through its circumference, 2π × 0.05 m. The motor makes ten revolutions during that wheel revolution, so that travel corresponds to 10 × 1,000 = 10,000 motor increments. Let N be the signed number of motor increments completed after the command begins. The modeled displacement s is:

~~~text
wheel revolutions = N / (1,000 × 10)
s = [N / (1,000 × 10)] × 2π × 0.05 m
distance per motor increment = 0.0000314159265359 m
~~~

The factors expose the two distinct revolutions and the command unit. A statement that the wheel turns through 2π radians would give orientation change for one turn; the present N retains accumulated turns because the receiving quantity is accumulated travel.

Invert this relation for the target displacement:

~~~text
N_ideal = 1 m / (2π × 0.05 m) × 10 × 1,000
        = 31,830.9886183791 motor increments
N_command = nearest integer to N_ideal = 31,831
~~~

The computational procedure reads the target distance and the three parameters, computes the ideal count and rounds it to the nearest integer. Use enough numerical precision to determine that integer; if arithmetic uncertainty straddles a rounding boundary, refine the calculation or retain the resulting command uncertainty.

Now supply the realization input. The interface accepts signed relative motor-increment commands in the range −32,768 to 32,767. It performs a command to completion before reporting successful completion. Thus 31,831 is representable and its unit and relative-command meaning agree with the calculation. A different interface would require its own preparation relation.

Read the completed command back through the physical model:

~~~text
s_command = 31,831 / 10,000 × 2π × 0.05 m
          = 1.00000035756417 m

maximum error from rounding to the nearest increment
          = 0.5 / 10,000 × 2π × 0.05 m
          = 0.0000157079632679 m
~~~

The rounding bound concerns discretization of the command. It leaves slip, effective-radius error and unsuccessful motor execution outside that numerical bound. If the engineering question is actual travel within a tolerance, those contributions determine whether this command is adequate. For example, motor counts alone cannot discriminate successful rolling from wheel rotation with slip; a displacement measurement needs its own relation to position.

The joint result is the command 31,831 and its modeled consequence under the physical and interface conditions. Physics supplies the rolling and transmission account. Mathematics supplies the relation, its inversion and the error bound. Computation supplies the integer and range check. The coordination connects their meanings and returns the supported displacement.

The same interface's largest positive relative command represents about 1.0294056648 m under this model. If the requested distance and tolerated error require a larger positive count, use another realization or a procedure using several commands whose combination is justified. If the wheel radius, the count's meaning or the use of initial position changes, reconstruct the affected relation before reusing the command. Those changes can affect the physical parameter, mathematical expression and command preparation together; recover the disagreement and its dependent contributions as in :4.6.

#### B.5.MPC:5.2 - Use two-colouring to answer a gear question

A designer asks whether every gear in a connected arrangement can rotate while all specified meshes remain engaged. The supplied idealized account has parallel, fixed axes, external gear contacts and positive pitch radii. View every rotation from the same side. At each external mesh, the two gears have opposite signs of angular velocity. Contact geometry and tooth compatibility are additional physical conditions; this first question concerns the consistency of rotation directions.

Construct a finite undirected graph. A vertex represents one gear and an edge represents one of the stipulated external meshes. Assign colour 0 to one rotation direction and colour 1 to the other. An edge requires different colours at its endpoints. This expression makes the physical question a mathematical one: can the vertices be assigned two colours while satisfying every edge?

The graph records actual contact, not geometric closeness on the page. A drawing with crossing lines does not add a mesh between the gears at that crossing. If an actual contact is absent from the list, the result answers only the incomplete list.

Obtain either a colouring or a witness of failure by the following procedure.

1. Choose an uncoloured vertex as a root. Give it colour 0, depth 0 and no parent; place it on a waiting list.
2. Remove the first vertex from the list and inspect its neighbours. Give each uncoloured neighbour the opposite colour, record the removed vertex as its parent, give the neighbour depth one greater and append it to the list.
3. For an already coloured neighbour, compare colours. If they agree, use that edge and the two parent paths to construct the odd-cycle witness explained below, and return it.
4. Continue until the list is empty. Start another root if an uncoloured vertex remains. If every edge joins different colours, return the colouring.

A vertex is added to the waiting list only once. Each recorded parent has smaller depth, so parent paths reach their root. A finite graph therefore yields a result after all relevant vertices and edges have been examined, or after a contradiction has been found. With adjacency lists, constant-cost access to a vertex's recorded data, and constant-cost insertion and removal in the FIFO waiting queue, the work is proportional to the number of vertices plus edges.

Work a square contact cycle with gears A, B, C and D and contacts AB, BC, CD and DA. Starting at A gives A colour 0; B and D colour 1; and C colour 0. Every contact joins opposite colours. The groups {A,C} and {B,D} therefore give compatible direction choices. Reversing both groups gives the other choice. Four equal pitch circles can be placed with centres at the corners of a square of side twice the pitch radius to obtain those contact incidences; tooth engagement and motion under load still require the corresponding mechanical design.

Now work three gears with contacts AB, BC and CA. Starting at A gives B and C colour 1. Edge BC then joins equal colours. Its endpoints' parent paths B–A and C–A, together with BC, give the three-edge closed path B–A–C–B. Alternating directions around three external contacts asks B to have both directions at once.

The same reasoning constructs a failure witness in a larger graph. For a same-colour edge, follow its endpoints' parent paths until their nearest common vertex. Discard the shared path beyond that vertex. The retained paths have even total length because the endpoints have the same depth parity. The extra edge closes a simple odd cycle. Alternating two colours cannot satisfy every edge of an odd cycle. Conversely, if the procedure finishes without such an edge, its returned colours satisfy every listed constraint.

The physical interpretation can be made quantitative without hiding the direction question. Let rᵢ be a gear's pitch radius and ωᵢ its signed angular velocity. Ideal external meshing with fixed axes gives:

~~~text
rᵢωᵢ + rⱼωⱼ = 0 at each mesh
qᵢ = rᵢωᵢ, so qⱼ = −qᵢ
~~~

For a two-colouring, choose any nonzero value q for one colour and −q for the other, then set ωᵢ = qᵢ/rᵢ. This satisfies those kinematic equations. For an odd cycle, following the equations around the cycle gives q = −q and hence q = 0. In a connected graph all gears then have zero angular velocity. Thus the odd cycle excludes the requested nonzero coupled rotation under the stipulated contact model; a stationary arrangement remains compatible with the equations.

Return the cycle as the particular set of physical contacts responsible for the obstruction. Removing one actual contact from the triangle leaves a chain and permits alternating directions. Deleting only its graph edge leaves the physical obstruction in place. An internal gear contact or a moving carrier changes the contact rule and requires a revised physical account before the colouring test is reused.

A compatible direction assignment answers this bounded question. It does not establish adequate torque, tooth phasing, freedom from interference or motion under the intended load. For those questions, retain the graph result and obtain the missing mechanical contribution. The common Method supplies the contact interpretation, the connection to the computational witness and the return to the design. The gear account and graph argument supply the substantive rules that make that return possible.

#### B.5.MPC:5.3 - Maintain an admission bound through material tokens

A demonstration room should contain at most three visitors. Initially the room is empty and three distinct material cards are available. An attendant gives a free card to one visitor before entry. That visitor keeps it while inside and returns it after leaving. A new visitor waits for a card when none is free.

For this case, every entrance and exit follows the procedure, each card is exclusively assigned to one visitor at a time, and cards are neither lost nor duplicated. The material arrangement makes exclusive acquisition possible: taking the available card removes that same card from the free stock. A photograph or printed copy of the card is not accepted for entry.

First consider a moment when every assigned card is held by a visitor inside and every other card is free. The one-card-per-visitor rule gives:

~~~text
occupancy = 3 − number of free cards
~~~

During admission and return, cards can also be held by visitors outside. A visitor may already hold a card while waiting to enter; a departed visitor may still be walking to its return point. To preserve the physical meaning during those intervals, distinguish four states for each card:

| State | Physical interpretation |
| --- | --- |
| Free | The card is available for a new admission. |
| Reserved | The card is held by a visitor who has not yet entered. |
| Inside | The card is held by its visitor inside the room. |
| Awaiting return | Its visitor has left, but the card is not yet free. |

Let F, R, I and E count cards in those four states. Every card occupies exactly one state, so F + R + I + E = 3. Under the visitor-to-card rule, occupancy = I. Therefore:

~~~text
occupancy = I = 3 − F − R − E
occupancy ≤ 3 − F ≤ 3
~~~

The transition procedure has four ordinary operations: issue one free card to a waiting visitor; admit that card's visitor; let the visitor leave with the card; and return the departed visitor's card to the free stock. Their state changes are Free → Reserved → Inside → Awaiting return → Free. A cancelled admission can return a Reserved card directly to Free while its visitor remains outside.

Each operation moves one existing card between states. Issuing a card requires a free card; entering requires its exclusive reservation; returning it requires that its visitor is already outside. Those conditions preserve the total stock and the association between visitors inside and Inside cards. The argument establishes the capacity bound for every sequence of those permitted operations, including overlapping visits.

Work two entries followed by one exit:

| Operation just completed | F | R | I | E | Occupancy |
| --- | ---: | ---: | ---: | ---: | ---: |
| Initial arrangement | 3 | 0 | 0 | 0 | 0 |
| Issue card A | 2 | 1 | 0 | 0 | 0 |
| Visitor A enters | 2 | 0 | 1 | 0 | 1 |
| Issue card B | 1 | 1 | 1 | 0 | 1 |
| Visitor B enters | 1 | 0 | 2 | 0 | 2 |
| Visitor A leaves | 1 | 0 | 1 | 1 | 1 |
| Return card A | 2 | 0 | 1 | 0 | 1 |

Counting free cards gives an upper bound on occupancy during handover and return. It gives the exact occupancy when R = E = 0. That distinction changes what an observer may infer from the same stock. The admission rule can preserve the bound without an exact instantaneous occupancy readout.

Connect the abstract transition rule to the physical means. Exclusive possession realizes consumption of a free token. Carrying it through entry preserves the visitor association. Returning it only after exit prevents its use for a fourth visitor while the first three remain inside. If a visitor passes their card to someone outside while staying inside, the allowed-transition premise fails: the reused card no longer represents one occupied or reserved place.

A second entrance needs access to the same total stock. A copied stock of three additional accepted cards permits six simultaneous admissions, even if both attendants follow their local rule correctly. A shared pool of the original three cards preserves the common bound. Partitioning those same cards, for example two at one entrance and one at the other, also preserves it. The partition can make a visitor wait at one entrance while a card is free at the other; redistribution then needs a transfer of an existing free card.

The useful result is a conditional admission design and an interpretation of its observable stock. Its computational contribution is a finite-state procedure that answers whether an admission can proceed and maintains the relevant count. People and material transfers can execute it without a digital program. The invariant does not establish fair waiting, fast entry or detection of every procedural violation; those are different questions with their own needed contributions.

The coordinating Method makes the physical card and room-boundary rules, mathematical invariant and executing procedure agree. This is also why changing the stock or the return rule changes the joint result even when the counting arithmetic remains correct.

### B.5.MPC:6 - Bias-Annotation

| Likely bias | Consequence for this work | Corrective action |
| --- | --- | --- |
| Familiar equations dominate the physical account | The practitioner begins with a calculable proxy and loses the requested quantity. | Name two physical cases that require different answers and determine whether the proposed variables distinguish them. |
| Successful computation dominates interpretation | A number or certificate is accepted without its meaning in the physical arrangement. | Interpret the decisive count, edge or token transfer and recover the premise connecting it to the receiving action. |
| Diagram familiarity hides physical assumptions | A graph edge is treated as a real contact, or its meaning changes across an example. | Construct the contact or interaction list from the subject account and label the relation that each edge represents. |
| Digital implementation is treated as the default | Material or manual realizations are overlooked even when they answer the question. | Compare their input preparation, permitted operations and result interpretation with the computational need. |
| A precise answer hides an uncertain premise | Small numerical error is reported while model or measurement uncertainty can dominate the result. | Carry the uncertain physical premise into the returned consequence or obtain the measurement that can settle it. |
| Contributor identity substitutes for usable grounds | An expert or AI report is trusted beyond what its stated assumptions and explanation support. | Recover the connection consumed by this use and obtain the missing explanation or evidence from a capable contributor. |

These biases can affect one person as well as a team. Apply the correction at the missing subject operation, correspondence or observation.

### B.5.MPC:7 - Conformance Checklist

Use these checks on the claimed joint result and its explanation. They establish conformance to this Method's stated use; physical validity and any stronger assurance claim require their applicable subject evidence.

| Check | Content to inspect |
| --- | --- |
| CC-MPC.1 — Receiving question | The explanation identifies the physical difference to be resolved and what the supported answer enables. |
| CC-MPC.2 — Physical premises | Participants, interactions and operating conditions are sufficient to recover the mathematical question; consequential assumptions remain distinguishable from observations. |
| CC-MPC.3 — Interpretable construction | Important quantities, structures and operations have meanings that survive the construction, and a lost distinction either leaves the use intact or changes the returned result. |
| CC-MPC.4 — Obtained consequence | The proof, construction, bound or computation is actually supplied for the stated case, with the decisive argument and its conditions. A missing operation is named as missing. |
| CC-MPC.5 — Executing arrangement | Any realization claim connects preparation, system operations and result reading. Range, units, initial state and ordering are recovered wherever they change the inference. |
| CC-MPC.6 — Joint and alternative dependencies | Jointly needed contributions remain together; alternative routes each satisfy the receiving need under their own conditions. A shared premise remains shared across alternatives. |
| CC-MPC.7 — Notation in use | The expression supports the needed operation under explained or familiar rules; new subject conclusions are justified by that operation rather than presented as mere re-expression of givens. |
| CC-MPC.8 — Supported return | The consequence is interpreted in the physical question with the bounds and uncertainties its use consumes. Conditional design and observed performance remain distinguishable. |
| CC-MPC.9 — Useful continuation | The explanation ends with an adequate use, a specific missing contribution or a justified next question. A change returns to its affected contribution and dependents. |

A short sufficient calculation can satisfy these questions without separate records for each row. A shared or consequential result retains enough of the derivation, interpretation and evidence for its receiver to inspect the connections.

### B.5.MPC:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Failure visible in the worked cases | Repair |
| --- | --- | --- |
| Substitute the right number into the wrong command | A count of relative motor increments is treated as an absolute wheel-position target. | Recover the interface's counted participant, unit and initial-state use; construct the input it actually accepts. |
| Check only the middle calculation | The robot arithmetic is correct while rolling or successful completion remains unsupported for an actual-travel claim. | Add the physical and observation contributions consumed by that stronger claim, or return the conditional design. |
| Treat a sufficient abstraction as complete physical design | A gear colouring is taken to establish torque or mechanical compatibility. | State the bounded direction consequence and obtain the missing mechanical account when the decision requires it. |
| Repair the drawing while leaving the arrangement unchanged | An odd-cycle edge is deleted from the contact graph but the gears remain meshed. | Change the actual contact or revise the contact rule with its physical basis, then reconstruct the graph consequence. |
| Count reservations as occupants | Three cards outside the free pool are reported as three visitors inside during handover. | Retain Reserved and Awaiting-return states, or report the resulting occupancy bound. |
| Preserve local rules while duplicating a shared resource | Each entrance has its own three-card stock and both are used for one room. | Use one total stock or a partition of it; transfer existing free cards when balancing entrances. |
| Traverse every contribution before using a sufficient result | A proof already excludes a design, yet simulation and implementation continue as compulsory stages. | Return the proved physical obstruction under its assumptions and choose a revised design question. |
| Ask a contributor for an unexplained answer | The receiver gets a count, proof or program whose needed meaning cannot be recovered. | Request the particular interpretation, decisive argument or operating condition required by the next use. |

### B.5.MPC:9 - Consequences

The practitioner can assemble a useful answer from contributions obtained at different times and from different people, AI systems or established sources. The resulting explanation identifies how the answer concerns the physical situation and which premise or operation would change it. That makes a partial result useful: a bound can settle a decision, an odd cycle can locate a design obstruction, and an unresolved command meaning can direct one precise request.

The method also changes what work is commissioned. Instead of asking for another undifferentiated simulation or report, a team can ask for the missing physical relation, retained state, constructive algorithm, measurement or realization. An already adequate contribution remains available when an unrelated part changes.

This connection work has a cost. Recovering an unfamiliar source, learning notation or obtaining a physical premise can take more effort than calculating the displayed answer. Spend that effort where it changes the receiving use. The method provides no automatic completeness claim for physics, mathematics or computing; it makes the needed subject contribution and its remaining boundary visible.

### B.5.MPC:10 - Architectural Rationale

#### B.5.MPC:10.1 - Why the connection is a Method in its own right

The receiving physical question joins several operations whose local success has different meanings. Derivation establishes what follows within a mathematical account. A physical explanation supports the choice of that account for a phenomenon. A procedure obtains a represented result; its realization connects that procedure to available system behavior. Coordinating these operations requires preserving their result dependencies while selecting a useful next contribution.

The epistemological and methodological contributions meet in the use of a result. Axiomatization can make the objects, premises and permitted constructions explicit. A physical postulate contributes to empirical knowledge through an interpreted model whose consequences can be compared with observations. Computational formulation and realization let agents work through consequences using specified operations on represented inputs. The practitioner connects these contributions to obtain and apply knowledge, then uses an encountered limitation or a newly available operation to change the method or pose another question. Their detailed constructions give substance to the pragmatic question: which further work becomes possible?

The robot makes the need concrete. Circumference, transmission ratio, integer rounding and signed-command semantics are separately intelligible. The useful command exists only when they refer to compatible motion and counts. A.3.3 can help recover state, C.29 can construct and transfer the mathematical consequence, and C.16 can interpret an observation. Their contributions enter the joint question through the dependencies explained in :4; none by itself chooses all the other subject content.

B.5 provides the general inquiry method: recover the question, perform the missing contribution, make its result understandable, and settle or revise the inquiry. This specialization adds the recurring connections among physical account, mathematical interpretation, computational formulation and executing arrangement. The relation is specialization of inquiry coordination and composition with the constituent Methods. A mathematical Method does not become the parent of a physical modeling Method merely because its result is used there.

An alternative is to use a fixed forward sequence. That is convenient when every input is new and later stages expose no earlier gap. It becomes wasteful when a ready theorem supplies the answer, and inadequate when command semantics require an earlier state distinction. The dependency method retains a forward traversal but also supports backward recovery, direct entry and returns after changed conditions.

Another alternative is to let each specialist check only their own output. That can be sufficient when all receiving correspondences are already established. Where they are unresolved, a correct local output can remain unusable by the next contributor. Give the connection itself an explicit receiving question and a capable contributor.

#### B.5.MPC:10.2 - What the sources contribute to the synthesis

Rodin's *Axiomatic Architecture of Scientific Theories* develops a constructive account of axiomatization in which object-forming activity matters alongside propositions. That supports asking how the needed object is obtained and which operations its theory permits. In :4.3–4.4, this becomes recovery of an actual construction. Physical interpretation still requires its subject account; the mathematical construction does not establish that a proposed physical interaction occurs. See [Rodin, 2020, §§4.2.2–4.2.3](https://philsci-archive.pitt.edu/17600/1/bde.pdf).

Fong and Spivak make preservation under composition explicit: a functor preserves identities and composition between categories. The use here is the comparison of corresponding operations, supplied by C.29.1. It explains why relabelling objects alone cannot establish a transfer. A physical approximation may instead need a bound or another qualified relation; the coordinating Method does not require every connection to be a functor. See [*Seven Sketches in Compositionality*, §3.3.2](https://arxiv.org/pdf/1803.05316).

Horsman, Stepney, Wagner and Kendon distinguish the representation of a physical system from the preparation and interpretation needed to use a physical process for computation. Their account supports :4.5's two routes and the distinction between refining an abstract description and realizing it. It also permits input preparation and result reading to differ. The present Method adapts that comparison to a receiving physical question and to useful bounds, rather than adopting their account as a universal definition of all computation. See [*When Does a Physical System Compute?*, 2014, §§VI–VIII](https://arxiv.org/abs/1309.7979).

Turing's 1936 construction of a universal computing machine provides a historical demonstration that an executor can interpret an encoded description of another machine's procedure. That helps distinguish the rule description, its interpreter and the realized operation. The finite interpreter in C.29.2:5.1 provides a small entry to that distinction. Use C.29.2 for the computation-specific cost account when a resource limit matters; :4.4 carries that cost and the computation's meaning into the joint use. See [Turing, *On Computable Numbers*, §6](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf).

These contributions answer different construction questions. The synthesis is to hold their input and result meanings together for a physical use, inspect their joint and alternative dependencies, and let a failed connection determine the next contribution. It preserves mathematical, empirical and realization grounds at the points where they are needed.

#### B.5.MPC:10.3 - Why notation and understanding remain part of the work

An expression can help a practitioner perform a construction. Macbeth's account of paper-and-pencil reasoning explains how a diagram or inscription can participate in the reasoning, including by allowing the same content to be analysed in more than one way. Dutilh Novaes examines formal languages as cognitive tools whose use depends on learned abilities to read and manipulate signs. These accounts support the operative expression step in :4.3. They do not establish that a notation improves every task or that a human learning effect transfers unchanged to AI. See [Macbeth, 2011](https://doi.org/10.1093/philmat/nkr006) and [Dutilh Novaes, 2012, §§3.2, 5.2 and 6.1](https://doi.org/10.1017/CBO9781139108010).

For this Method, the practical consequence is precise. Naming the same count N in several expressions is useful only while its participant and operation remain recoverable. A gear graph helps reason about closed contact paths because its edge meaning and traversal rules are available. The four card states distinguish occupancy from reservation throughout entry and exit, where an undifferentiated “not free” count gives only a bound. These are changes to what the expression helps someone do, not merely choices of appearance.

A second alternative is to make one formal language carry the whole inquiry. This can help when a mature language expresses the required physical, mathematical and execution distinctions and its users can work with it. If it cannot express a necessary distinction, use another representation or develop the language. Retaining interpretable correspondences allows several forms to contribute without assuming that one form already covers the whole problem.

Levenchuk's [2012 robotics account](https://ailev.livejournal.com/1034484.html) describes difficulty combining familiar speed calculations, several distance quantities, program expressions and physical timing. It motivates changing the question while retaining the interpreted relations in :4.3, and examining the timing of observation and execution in :4.5. The account is a historical report of a particular learning situation. The resulting Method here is a conceptual synthesis.

AI can reduce the cost of obtaining a calculation, candidate proof or explanation while leaving the choice and interpretation of the receiving question open. Klowden and Tao discuss the difference between a formally checked statement, its intended meaning and the understanding that enables further use. Section :4.8 turns that distinction into a contribution question: who can recover the decisive connection and adapt it when the premise changes? This is a capability to arrange, not an assertion that every participant must reproduce every proof. See [*Mathematical Methods and Human Thought in the Age of AI*, 2026, §4](https://arxiv.org/html/2603.26524v1).

#### B.5.MPC:10.4 - Why a sufficient answer can also open a better question

Deutsch's discussion of foundational theories treats their connections as sources of criticism across areas, rather than relying on a theory's foundational status to settle another question. This motivates examining how a claim about computation constrains a physical proposal and how physical knowledge constrains an executing arrangement. The specific correspondences still require their arguments. See [Deutsch's interview on *The Beginning of Infinity*](https://beginningofinfinity.org/interview/).

The same connection work can generate a worthwhile next problem. The robot account raises which observations distinguish rolling from slip. The gear witness raises which physically available contact change removes the obstruction. The card bound raises whether redistribution can reduce waiting while preserving the shared stock. Each continuation identifies an additional possible action and a construction or uncertainty that matters to it.

A sufficient answer remains a legitimate stopping point when the current use is complete. When inquiry development is selected, retain the useful connection and work a consequential change to the question or apparatus. A general invitation to keep exploring supplies less direction than the particular obstruction or newly available operation.

### B.5.MPC:11 - SoTA-Echoing

For the declared coordination question, the selected answer is the explicit combination of physical interpretation, operation-preserving mathematical use, computational formulation and realization comparison. The sources below supply particular advances and alternatives. The combined Method and the three constructed cases are conceptual synthesis; they do not establish a measured advantage for every discipline, reader or team.

| Practice question | Selected line, comparison and change to this Method | Limits and condition for reconsidering the choice |
| --- | --- | --- |
| How should a discrepancy between a physical prediction and an indication be investigated? | Dounas-Frazer and Lewandowski's 2018 account of experimental modeling distinguishes the model of the physical system from the model of the measuring system and distinguishes changing either model from changing either apparatus. **Adopt** these separate contributions in :4.2 and the return in :4.6. Compared with fitting one model directly to raw readings, this exposes whether the observation relation itself needs repair. [Source, §2](https://arxiv.org/pdf/1805.10334). | The source develops a framework for experimental-physics modeling; it supplies neither every physical law nor the whole joint Method. Reconsider the selected return when another diagnosis better distinguishes the live causes or when the current physical question needs no measurement. |
| What makes a mathematical result usable after changing its representation or receiving operation? | Fong and Spivak's preservation-under-composition account supplies a precise comparison where category-theoretic structure is applicable. **Adapt** it through C.29.1 and :4.3 to the equality, bound or behavioral relation actually needed. Compared with transferring a result because formulas look alike, this exposes a failed operation or a lost distinction. [Source, §3.3.2](https://arxiv.org/pdf/1803.05316). | Mathematical preservation does not establish the physical account. Use a less elaborate direct argument when it supplies the same comparison; reconsider the chosen relation when the receiving operation or tolerated loss changes. |
| What connects a valid computation to an available physical execution? | Horsman and colleagues explicitly compare abstract evolution with preparation, physical evolution and interpretation. **Adopt and adapt** this construction in :4.5. Abstract refinement and a successful software trace remain useful alternatives for their own questions, but leave input range, material exclusivity or physical result reading open when those are the unresolved connection. [Source, §§VI–VIII](https://arxiv.org/abs/1309.7979). | This is a specific account of physical computation, not a universal criterion established for every use. Reconsider the selected realization when its actual operations or observation rules change; reuse it directly when the receiving conditions remain supported. |
| When should notation be changed during the reasoning? | The operative-notation accounts discussed in :10.3, together with Zhang and colleagues' *How Notations Evolve* (2026), support relating meaningful distinctions to the expressive and perceptible differences of a notation. **Adapt** that question in :4.3: construct an expression and try the operation it should support. Compared with assessing the appeal of isolated symbols, this can expose an omitted count meaning or an unusable compound expression. [Contemporary study](https://glassmanlab.seas.harvard.edu/papers/notationsCHI26.pdf). | The historical analysis supports notation-design questions; it does not demonstrate that these particular expressions improve human or AI performance. Reconsider the scheme when the intended operation cannot be performed or a meaningful difference cannot be recovered at acceptable effort. |
| What understanding is still needed when proof and calculation can be obtained from AI? | Klowden and Tao's 2026 discussion separates proof production and formal verification from interpretation and the understanding used to extend an argument. **Adapt** that distinction in :4.8: obtain the needed contribution and retain capability to recover its receiving connection. Compared with accepting a polished answer or requiring every receiver to reproduce its full derivation, this targets the understanding the next work actually consumes. [Source, §4](https://arxiv.org/html/2603.26524v1). | The source combines observations, arguments and forecasts; it establishes no universal allocation of human and AI work. Reconsider the allocation when support, capabilities, required adaptation or consequences change. |

The source-supported distinctions remain useful even when their historical origin is older than a current tool. Their selection here depends on the defects and constructive differences in these comparisons. Further disciplinary development can supply better constructions, representations or realization Methods without replacing the need to interpret their joint result.

### B.5.MPC:12 - Relations

| Relation | Concrete contribution |
| --- | --- |
| **Specializes B.5 — Canonical Reasoning Cycle** | Retains question formation, selection of a missing contribution, result understanding and sufficient-result closure; adds the joint physical, mathematical and computational connections and their dependencies. |
| **Uses B.5.4 — Recognize a Reusable Concept in a Concrete Situation** | Supplies recognition of an explained concept's participants and relations when the physical situation has not yet been interpreted through it. |
| **Uses C.29 — Mathematical Lens Use** | Constructs the mathematical account and returns its consequence to the working question. |
| **Uses C.29.1 — Mathematical Result Transfer** | Constructs the correspondence and tests the operations and distinctions needed to carry a result between mathematical accounts. |
| **Uses C.29.2 — Computational Formulation** | Constructs the computational state, operations and obtaining procedure, with the result argument and resource account that its use needs. |
| **Uses C.29.3 — Computational Realization** | Compares input preparation, system operation and readout with the required result, and returns a failed connection to its repair. |
| **Uses A.3.3 — U.Dynamics** | Supports the construction of configurations, retained state and allowed continuations when the receiving prediction or operation requires them. It uses the supplied subject laws and interaction rules. |
| **Uses C.16 — Measurement and Metrics Characterization** | Constructs and interprets the measurement relation connecting the sought quantity, apparatus influences and indication. This contribution is needed when the joint consequence consumes an observation. |
| **Uses A.6.3.RT — Representation-Scheme Transition** | Constructs an operative expression under an available scheme and compares its content and use with the source. The applicable subject Method supplies any new conclusion obtained with that expression. |
| **Uses A.6.1 for realization semantics** | Keeps a declared operation, its realization relation and the performance of a Method distinguishable when those claims matter to the executing arrangement. |
| **Uses A.15.9 for a needed contribution from another practice** | Helps obtain the specific result, explanation or formulation that the next operation needs, with its receiving use made explicit. |
| **Coordinates with C.39 and C.40** | Searches for a missing way and develops the problem or Method repertoire when the existing connections expose a worthwhile construction question. |
| **Uses C.11.DUA for a decision about further effort** | Compares whether additional calculation, observation, explanation or checking can change the receiving action enough to justify its cost. |
| **Uses B.3 and B.3.3 for stronger assurance questions** | Qualifies evidence and assurance for the particular claim and use when a conditional consequence or ordinary construction no longer suffices. |

### B.5.MPC:End
