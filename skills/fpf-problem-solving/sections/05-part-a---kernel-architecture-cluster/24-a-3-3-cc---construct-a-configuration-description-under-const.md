## A.3.3.CC - Construct a Configuration Description under Constraints

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### A.3.3.CC:1 - Problem frame

Use this pattern when you need to describe how participants can be arranged, but choosing values for them separately admits combinations that the modeled situation excludes. A linkage joins its endpoints at a fixed distance; buffers share a fixed stock; a body must fit inside a container. The next calculation needs a description that preserves those connections.

**First useful move.** Name the participants, the question and one condition joining their values. For two buffers containing three jobs altogether, begin with “q1 and q2 are nonnegative integer job counts, and q1 + q2 = 3.” You can now recover the second count from the first and reject a proposed pair whose sum differs from three. Add buffer capacities when the question concerns which distributions fit.

The Method constructs an interpretable description of configurations: the retained arrangement or combination of participant values, expressed through variables and constraints. It can return an equation, a parametrization, a finite set or another usable representation. The arrangement being modeled and its description remain distinct. The examples assume elementary algebra and, for the linkage, the ordinary meaning of sine and cosine; the Solution explains the representation choices.

The practical gain is a basis for finding, comparing or rejecting configurations and for constructing a later model of change. If an available description already supplies the combinations and distinctions the question needs, use it directly. A prediction additionally needs the state information and law addressed by A.3.3.

### A.3.3.CC:2 - Problem

Separate value ranges leave relations unstated. Each endpoint of a rigid link can have a position in a plane, yet most pairs of positions violate the link length. A software representation that permits every pair will include arrangements the intended physical model excludes.

A reduced description can fail in the opposite direction. One buffer count determines the other while total stock is fixed. After external arrivals become possible, keeping that same formula excludes distributions the new situation permits. Counts can also lose job order when the question changes from occupancy to which job is served next.

The construction must therefore retain the differences relevant to the question, express the constraints between them and provide a way to interpret the represented combinations. The choice of variables and the choice of constraints have to be made together.

### A.3.3.CC:3 - Forces

| Force | Tension |
| --- | --- |
| Few coordinates and visible relations | Eliminating a dependent coordinate can simplify calculation; retaining it can make a physical connection or consistency condition easier to understand. |
| Convenient notation and coverage | One parametrization may work locally while missing configurations or becoming singular elsewhere. |
| Compactness and retained distinctions | Counts or aggregate quantities are economical when they answer the question; identity, order or orientation can become consequential in another use. |
| Constraint fidelity and computational cost | Explicitly listing admissible combinations works for a small finite set; larger sets often need equations, predicates or a solver. |
| Present arrangement and possible change | A configuration can satisfy every positional constraint while a proposed motion violates the system's operation or velocity rules. |
| Model usefulness and subject knowledge | A coherent constraint account can support a conditional calculation; deciding whether it describes the actual system may require additional subject knowledge or measurement. |

### A.3.3.CC:4 - Solution

Construct the description from the working question, then choose a representation in which the needed combinations can be expressed and used. If the calculation becomes inconvenient, reconsider the representation. If a premise changes, revisit the variables and constraints it affects.

#### A.3.3.CC:4.1 - Select the participants and retained differences

State what the reader must find: a fitting arrangement, a compatible assignment, a range of positions or the configurations to which a law will later apply. Identify the participants and the differences that can change this answer.

Give each variable a meaning and a value range. For a physical position, include the reference frame and unit needed to interpret it. For a relation, identify its participants: a distance needs the two endpoints; a job count needs the particular buffer. A.17 and A.18 supply the Characteristic and Scale vocabulary when the variables are declared as FPF characteristics.

Separate quantities held fixed in the present model from variables to be found. A link length may be a parameter in a rigid-body model and a changing quantity in an elastic model. The distinction follows the modeled use, so a later revision can change it.

Ask whether two arrangements described by the same values can require different answers to the current question. If they can, retain the missing distinction. For example, a pair of queue lengths suffices for occupancy but loses the order of differently treated jobs. State the needed order before attempting the receiving calculation.

#### A.3.3.CC:4.2 - Express compatible combinations

Start with the product of the separate value sets. Write the conditions selecting the combinations admitted by the model. In a finite problem this may be a table of allowed tuples. In an algebraic description it may use equalities, inequalities or other predicates.

In A.19 terms, `CS = product_i ValueSet(Scale_i)` is the CharacteristicSpace. A constraint predicate `P` selects a subset `Q = {q in CS : P(q)}` used as the represented configuration set. A point in CS supplies a value for every selected slot; membership in Q additionally satisfies the constraints. The same method can be used in ordinary mathematical notation without creating a separate FPF record.

Explain what each condition represents. Fixed distance, conserved stock, nonpenetration and an imposed operating limit can all constrain the calculation, but changing each condition changes a different premise. Keep a condition imposed by the intended use recognizable so that revising a preference does not appear to alter a physical law.

When time or an external parameter changes which combinations are admitted, make that dependence recoverable, for example `Q(t; p)`. A moving wall changes a position constraint even before its interaction law is known.

Place restrictions on rates, operations or transitions with those relations. The car constraint in :5.4 limits instantaneous velocity; it leaves the corresponding configuration variables available. A.3.3 uses both kinds of restriction when constructing allowed continuations.

#### A.3.3.CC:4.3 - Choose a representation that supports the operation

Compare the following forms using the operation the reader actually needs.

| Form | How to construct and use it | When it becomes inconvenient |
| --- | --- | --- |
| Variables with implicit constraints | Keep the participant values and equations or predicates between them. Test a proposed tuple by substitution. | Finding a satisfying tuple can require solving coupled conditions. |
| Parametrization | Choose parameters u and a reconstruction q = f(u) that satisfies the constraints. Perform the calculation in u and reconstruct the required participant values. | The chosen parameters may cover only part of the admitted set, repeat a configuration or become singular. |
| Explicit finite set | Generate candidate tuples, retain those satisfying the conditions and inspect or compare the resulting set. | The product of value sets can become too large to enumerate. |

For a parametrization, establish the coverage its use needs. If the task claims to represent every admitted configuration, explain how each can be obtained, possibly using several charts or cases. State when two parameter values represent the same configuration. A full turn of an angle repeats an orientation; treating its endpoints as unrelated can break a continuity calculation.

Keep redundant coordinates when they preserve useful structure or avoid a difficult elimination. If the task instead uses a local count of freely variable coordinates, establish independence and regularity of the active equality constraints before subtracting their number. A count alone supplies neither a parametrization nor its global coverage.

When replacing one representation with another, reconstruct the participant values and compare the receiving result. C.29.1 supplies a fuller transfer comparison when the replacement can change an operation or lose information. Group configurations as equivalent only when every member gives the same required answer and the required operations preserve that grouping. This mathematical construction is called a quotient. For an operation on the groups, check that choosing another member of the same group gives an equivalent result. Keep differently labeled endpoints distinct when exchanging them changes the answer.

#### A.3.3.CC:4.4 - Obtain the configuration result the question needs

Apply the description to the receiving question. If one fitting arrangement is enough, finding a satisfying tuple can finish the search. If the question asks for all arrangements, a range or impossibility, supply the corresponding enumeration, argument or solver result.

For a small finite product, generate a tuple, evaluate the conditions and retain it when they hold. A partial assignment can already be rejected when it violates a constraint whose participating values are known. Otherwise it may still have no satisfying completion: local checks leave the remaining constraints to be solved. For a large search, use a suitable constraint-solving Method; the explicit variables, domains and conditions provide its input.

For equations or inequalities, solve them to the extent needed and substitute the result into the retained relations. If numerical computation is used, interpret its tolerance against the modeled condition. A small residual has a different use from a proof of equality or an established margin from a collision boundary.

A configuration rejected by one condition identifies a concrete premise to inspect. An empty admissible set under the chosen premises is also useful: it can return the task to a size, capacity, connection or requirement decision. Failure of an incomplete search to find a tuple leaves the existence question open.

#### A.3.3.CC:4.5 - Carry the result into use and revise it when needed

Return the participant meanings, chosen variables, constraints and interpretation needed to use the result. Keep the representation as small as the receiving operation allows. The equations beside a design or the meanings attached to solver input may already carry everything needed; no additional report is required.

For a later prediction, recover the extra state information and transition rules under A.3.3. A linkage configuration may need velocities; an occupied-buffer configuration may need service or arrival information. An arrangement that fits now gives a starting point for planning, while reaching it from another arrangement needs an allowed-transition account.

When the question or premises change, revisit the affected part. A variable length replaces the fixed-length constraint; arrivals change a stock constraint; a job-order question needs more than counts. B.5.MPC.R coordinates a revision when that change also affects the physical interpretation, calculation or actual execution.

Recognition of the Method's result concerns whether the description expresses the selected configurations and supports the receiving operation. Reliance on its physical accuracy uses the subject premises and whatever calibration or uncertainty account that decision needs. C.11.DUA helps decide whether obtaining further information can change the action enough to justify its cost.

### A.3.3.CC:5 - Archetypal Grounding

#### A.3.3.CC:5.1 - A rigid link, then a variable length

Consider a freely placed link in a plane, with distinguishable endpoints A and B and fixed length 2 metres. Use one Cartesian reference frame. The implicit description is

`q = (xA, yA, xB, yB)`, with `(xB - xA)^2 + (yB - yA)^2 = 4`.

The tuple (0, 0, 2, 0), in metres, satisfies the relation. The tuple (0, 0, 1, 0) fails it. Each endpoint separately has a valid position in the plane, but the second pair violates the modeled link.

For locating the endpoints, use parameters X, Y and orientation phi:

`A = (X, Y)`; `B = (X + 2 cos(phi), Y + 2 sin(phi))`.

Every pair of endpoints at distance 2 has such a representation. Orientations differing by a full turn describe the same configuration. Reversing the direction while keeping A fixed changes B, so identifying opposite orientations would lose a distinction of this labeled-endpoint model.

Now allow the link to extend or contract with length `0 < r <= 3`. Replace 2 by the variable r. The formerly rejected pair (0, 0, 1, 0) is admitted at r = 1. A later motion calculation needs a law for the changing length and whatever initial data that law requires. If the question concerns force carried by a rigid constraint, retaining its equation can help express the force calculation through a multiplier; eliminating the constraint from position coordinates has not answered that force question.

#### A.3.3.CC:5.2 - Buffer counts, external arrivals and job order

Two buffers each hold at most two jobs. Exactly three jobs are distributed between them. The product of count ranges is `{0,1,2} x {0,1,2}`; the stock condition is `q1 + q2 = 3`.

Testing the nine pairs leaves `Q = {(1,2), (2,1)}`. Equivalently, choose q1 from {1,2} and reconstruct `q2 = 3 - q1`. The description now supplies both possible occupancy arrangements.

An external arrival can raise the total to four. Keeping `q2 = 3 - q1` would omit the possible arrangement (2,2). Retain both counts and use the total applicable to the new question, or include total N as a variable with `q1 + q2 = N`. Which arrival can occur, and when, comes from an arrival and transition account.

Suppose the next question asks which job a first-in-first-out buffer serves. The sequences [A,B] and [B,A] have the same count, yet they give different next jobs under that rule. Represent the ordered job identities in the relevant buffer. Counts remain recoverable as sequence lengths; the receiving operation gains the distinction it lacked.

#### A.3.3.CC:5.3 - A body must fit, not just its reference point

A rigid body occupies the one-dimensional interval `[x-r, x+r]`; x is its centre and r its half-length. It must lie wholly inside `[0,L]`. Contact with the endpoints is permitted in this model.

Containment gives `x-r >= 0` and `x+r <= L`, hence `r <= x <= L-r`. For L = 3 and r = 1, the admissible centres are [1,2]. Centre x = 0.5 lies inside the container but places part of the body outside it, so a point-only test gives the wrong fitting answer.

If clearance is required, include the clearance in the inequalities. If L = 1.5 while r remains 1, the interval for x is empty. That conditional impossibility directs the next decision to the body size, container size or permitted deformation. It was obtained by connecting a physical extent, a mathematical inequality and a calculation; no motion simulation was needed.

#### A.3.3.CC:5.4 - A velocity restriction leaves a configuration question open

For an ideal car rolling in a plane without lateral wheel slip, let (x,y) be the point halfway between the rear wheels and theta the chassis orientation. Let v be this point's velocity component along the chassis's forward direction. Then

`xdot = v cos(theta)`, `ydot = v sin(theta)`,

so `sin(theta) xdot - cos(theta) ydot = 0`. At theta = 0 the rear reference point has ydot = 0.

This equation constrains a velocity at a configuration. It does not impose a fixed y coordinate: a stationary car at another y satisfies the same velocity condition with v = 0. Whether a car can reach a selected parking position from its current one also depends on steering, obstacles and an allowed sequence of motions. Preserve those as a planning question instead of deleting the position from the configuration description.

### A.3.3.CC:6 - Bias-Annotation

A familiar coordinate system can make its convenient operations look like properties of the subject. The centre-only containment test in :5.3 demonstrates the loss: the representation retained a point while the fitting question concerned an extended body. Recover the modeled participants and required distinctions before transferring the result.

Minimal-coordinate preference can also hide a useful relation. In the linkage, fewer coordinates simplify position reconstruction, while the retained constraint equation is useful for a constraint-force question. Choose with that operation in view.

Both biases can occur in a person's reasoning, an AI-generated model or a shared engineering calculation. Make the interpretation recoverable to the next participant, including when a computation is delegated.

### A.3.3.CC:7 - Conformance Checklist

- Does the description name the arrangement question, participants and differences that can change its answer?
- Can the reader interpret each variable, its value range and any quantity held fixed?
- Do the constraints state which combinations are admitted and why those conditions apply to this model or use?
- If a parametrization or reduced description is used, does it cover the required cases and preserve the distinctions used in the answer?
- Can the receiving operation obtain its required tuple, set, range or conditional impossibility from the description? Is an unfinished search reported as unfinished?
- Are restrictions on configurations distinguished from any rate or transition conditions actually used?
- When the question changes, are newly relevant quantities, identities or order retained?
- Is support for physical reliance supplied to the extent that the particular decision needs, with further inquiry chosen by its possible effect on that decision?

### A.3.3.CC:8 - Common Anti-Patterns and How to Avoid Them

| Observed or example-demonstrated failure | Repair |
| --- | --- |
| Choosing valid values for each endpoint but violating the link between them | Test the joint tuple against the distance constraint, or reconstruct both endpoints from parameters satisfying it. |
| Carrying a fixed-total reduction into a model with arrivals | Make the changed total explicit or retain the counts needed to express it. |
| Answering a job-order question from queue lengths alone | Retain the ordered identities used by the service rule. |
| Treating a small coordinate count as a global representation | Supply coverage and equivalence information; use multiple charts or implicit constraints where needed. |
| Rejecting a parking position because immediate sideways motion is forbidden | Keep the position and test a sequence of allowed motions under the relevant steering and obstacle conditions. |
| Treating a failed search as impossibility | Return the search limit, or obtain a complete argument or computation for the impossibility claim. |

### A.3.3.CC:9 - Consequences

The description makes compatibility usable: a solver can seek a fitting arrangement, a practitioner can locate the condition excluding one, and another participant can reconstruct the represented values. A later law of change starts from interpretable configurations.

Construction takes effort, particularly when constraints interact or a compact representation loses necessary detail. An implicit description may save modeling effort while making each computation harder; a parametrization reverses that trade-off. Reuse an adequate description until a changed operation, premise or required distinction defeats it.

### A.3.3.CC:10 - Architectural Rationale

Constraint-based construction connects the subject's arrangement to the mathematical and computational operations used on it. Separating value ranges from compatibility explains why independently valid coordinates can form an inadmissible combination. It also lets the same construction work with continuous positions, finite stocks and ordered data.

The result can be useful before a transition law exists. Keeping that stopping point allows division of work: one participant constructs the configuration description, another supplies interaction or operation rules, and another computes a receiving result. Their contributions remain connected through interpretable participant values and conditions.

Implicit descriptions, parametrizations and finite enumeration expose different operations. Treating one as universally preferable would make the Method fail on either constrained geometry or a small discrete problem. The representation can be refined at the scale its use needs. C.29.1 handles the more general transfer between accounts; here the construction specifically obtains compatible arrangements.

### A.3.3.CC:11 - SoTA-Echoing

**How should constraints determine the representation?** Tong's [Classical Dynamics, section 2.3](https://www.damtp.cam.ac.uk/user/tong/dynamics/dynhtml/S2.html) develops generalized coordinates and the alternative of retaining constraints through multipliers. At comparable effort for the linkage, reduced coordinates make positions easy to reconstruct; the implicit relation keeps the connection available for a force calculation. Sections :4.2-:4.3 adopt this choice by the receiving question. Its mechanics supplies the physical interpretation of those constraints, not a law for every modeled subject.

Lynch and Park's [Modern Robotics, section 2.3.2](https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-3-2-configuration-space-representation/) compares explicit and implicit configuration representations, including singular coordinate descriptions of a sphere. Section :4.3 adopts the coverage and representation question instead of equating fewer coordinates with a better account. Their [section 2.4](https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-4-configuration-and-velocity-constraints/) distinguishes holonomic configuration constraints from nonholonomic velocity restrictions. Section :5.4 carries that distinction into a small motion question. These are durable construction Methods; the particular robot geometry and kinematic assumptions must still be supplied for a new robot.

**How does physical extent enter a computational configuration?** LaValle's [Planning Algorithms, chapter 4, introduction and sections 4.2-4.3](https://lavalle.pl/planning/ch4.pdf), constructs robot configurations, transformations and collision sets. Compared with checking a reference point alone, testing the transformed body's intersection with obstacles preserves the extent that the fitting question needs. Sections :4.1-:4.2 and :5.3 adopt that connection and the need to state contact conditions. The one-dimensional containment calculation is an authored reduced case. Path planning and collision algorithms retain their own assumptions and costs.

**When should a finite constraint set be solved by enumeration?** Poole and Mackworth's [Artificial Intelligence: Foundations of Computational Agents, third edition, section 4.1](https://artint.info/3e/html/ArtInt3e.Ch4.S1.html) makes variables, value domains, assignments and constraints explicit. Their [section 4.2](https://artint.info/3e/html/ArtInt3e.Ch4.S2.html) compares complete-assignment testing with search that rejects a partial assignment once a relevant constraint fails. Sections :4.2-:4.4 adopt those operational forms. For the two-buffer case, nine combinations make full enumeration inexpensive; a large product calls for a solving Method that exploits its constraints. Early rejection saves search without changing the satisfying set; it does not make arbitrary constraint problems cheap.

Together these sources supply complementary current answers to the construction question, with older sources serving as substantive methods rather than as claims of novelty. Reconsider the representation when the needed operation, configuration coverage, contact condition, participant distinctions or computational budget changes. A faster solver cannot recover a physical distinction omitted from its input.

### A.3.3.CC:12 - Relations

- **A.3.3** connects configurations to state, transition rules, observation and the information required for prediction.
- **A.17, A.18 and A.19** supply characteristic meanings, value scales, the product space and predicates selecting admitted combinations.
- **B.5.FM** constructs a first model for a working question; this Method supplies its configuration construction when compatibility is the difficulty.
- **C.29 and C.29.1** connect the subject with a mathematical representation and compare transfer to another account.
- **C.29.2** constructs a computational formulation when obtaining the configuration result requires a nontrivial computation.
- **A.6.3.RT** makes the chosen notation usable under its interpretation scheme.
- **B.5.MPC and B.5.MPC.R** coordinate the joint physical, mathematical and computational answer and its revision.
- **C.16 and C.11.DUA** support a needed measurement relation and the decision whether additional information is worth obtaining.

### A.3.3.CC:End
