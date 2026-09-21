## B.5 - Canonical Reasoning Cycle

> **Type:** Method-description pattern
> **Status:** Candidate
> **Normativity:** Normative unless marked informative

### B.5:1 - Problem frame

Use this pattern when an engineer or researcher has a question, surprising result or promising construction, but the next useful contribution is unclear. They may need to formulate a better question, construct something, prove a claim, explain an observation, or test a consequence. Reasoning is the broader activity; this pattern governs the choice and connection of those contributions in an inquiry.

**First useful move.** State what you want to understand or make possible. Ask whether an available result already answers that question. If it does not, name the missing result and try one operation that could obtain it. Return what that operation established and the next question, if one remains.

For example: “We need the highest component temperature, but our model reports a mean. Two states with the same mean can have different maxima. Next, determine which temperature differences this arrangement admits.” This already redirects the inquiry before another model fit.

The practical gain is a useful answer or a better-founded next question. A correct answer to an inadequate formulation can otherwise consume the inquiry's effort.

Use a known calculation, proof, observation or qualified Method directly when it already answers the question. A separate cycle description adds nothing in that case. Detailed mathematical techniques, physical modeling and domain validation remain with their disciplines.

### B.5:2 - Problem

A hypothesis-led inquiry has a productive structure: propose an explanation, derive consequences and compare them with observations. Trouble begins when this structure is made the only permissible form of reasoning. Constructing a mathematical object, finding a counterexample, exploring a phenomenon or discovering that the intended quantity is not recoverable can change the question before an explanatory hypothesis is appropriate.

A second difficulty survives even when result production becomes cheap. More proofs, simulations or candidate designs do not by themselves say which questions matter, what an argument explains, or which construction should be developed. The inquiry needs ways to inspect and change its own formulation and repertoire while retaining adequate results.

### B.5:3 - Forces

| Force | Tension |
| --- | --- |
| Purpose and discovery | A question directs effort, while a useful result may reveal a better question. |
| Construction and justification | A new object or conjecture opens possibilities; its properties and applicability still need the appropriate argument. |
| Abstraction and use | A simpler representation saves effort, while its lost distinctions can decide the intended use. |
| Rigor and affordability | Formalization, computation and observation can expose errors, but their whole burden must serve the question. |
| Current result and future possibilities | A sufficient answer deserves a stop; a retained construction may enable a different worthwhile inquiry. |

### B.5:4 - Solution

Choose reasoning by the result the current question needs. The abductive–deductive–inductive loop remains the canonical route for **hypothesis-led empirical inquiry**. Its short mantra is **Propose → Analyze → Test**: propose a conjecture, derive consequences that make a test interpretable, and compare them with relevant observations. Construction, exploratory observation and question formation can precede, interrupt or follow that route. A mathematical inquiry may finish with a construction, counterexample or proof.

#### B.5:4.1 - Form or recover the question

Say what an answer would help someone understand, construct, explain, decide or investigate. An epistemic aim, such as exposing an obstruction or finding a more informative theory, can justify inquiry without an immediate product application. Recover an adequate existing answer before commissioning new work.

Separate the subject from its description, the intended result from a convenient proxy, and established premises from assumptions. Use ordinary language, a sketch or a small mathematical example at the precision needed to expose the difficulty.

When the current formulation is inadequate, vary a consequential element. Useful operations include:

- change the quantity or distinction that the answer must preserve;
- restrict or widen a domain, scale, boundary or assumption;
- construct a small case that defeats the current claim;
- introduce a new object, relation, operation or representation and ask what it makes expressible;
- ask what observation or argument would distinguish the remaining possibilities.

Keep a changed formulation when it changes the construction, evidence, explanation, comparison or next action.

C.22.2 helps make a problem-side claim and its next use inspectable. C.29 helps when choosing a mathematical lens or its mapping is the live question. Use their supplied actions at those boundaries; an ordinary mathematical problem need not acquire a separate card.

When you can follow a concept's explanation but cannot yet interpret the situation through it, use [B.5.4][fpf-b5-4-ref] to construct and test the correspondence. Return with the interpreted participants and relations, then choose the reasoning contribution the question needs.

##### B.5:4.1.1 - Propose a first model


When the situation has no usable model yet, begin with the contrast the answer must resolve. Inspect one case or the actual arrangement. Describe what happens and which proposed change or comparison matters. Separate observations from the explanation you are about to try.

1. **Choose what must remain distinguishable.** Identify participants, states or quantities whose differences could change the answer. Use observed differences and possible interventions to propose a boundary: what can vary separately, what connects those parts, and what surrounding conditions affect them? Keep a distinction when you can explain its consequence for the question.
2. **Propose how they are connected.** Draw or state a dependency and explain how it could produce the observed behavior. Use the relevant subject account to identify the interaction and what it preserves or changes. If that account is unfamiliar, use §4.3 to recover its concept of use. Mark the assumptions that let you omit other interactions or treat a quantity as fixed. For a physical model, use physical knowledge to choose the law that the mathematical account will express.
3. **Obtain a cheap consequence.** Follow the proposed relation far enough to answer a useful part of the question. A direction of change, limiting case or rough bound may suffice before parameter fitting or detailed computation. Show which premise makes that consequence follow.
4. **Challenge a consequential choice.** Ask what observation, omitted interaction or changed condition could defeat the answer. Compare a plausible alternative when the observations leave materially different explanations. Revise the model or obtain the missing observation when that difference matters.

Return the provisional model and what follows under its assumptions. If a missing domain account or formal construction prevents the next contribution, use A.15.9 to request that specific help from the working description. Section 5.6 shows this entry before a heat-transfer calculation has been formulated. **B.5.FM** shows how to choose the model's participants and relations and use them to derive a consequence, in physical and formal problems.

#### B.5:4.2 - Perform the contribution that is missing

The following are common alternatives, not an exhaustive classification or a sequence to complete.

| Missing result | Useful operation | What the result can establish |
| --- | --- | --- |
| An object, procedure or structure with desired properties | Construct it from stated elements and permitted operations; test examples and counterexamples; prove the relevant properties or expose the obstruction. | A construction, existence or impossibility result under its mathematical premises. |
| A consequence or a mathematical justification | Make premises explicit and derive the consequence. Identify the step that carries the argument and the conditions on which it depends. | The implication or theorem within the stated domain and inference rules. |
| An explanation of an anomaly, opportunity or probe result | Use B.5.2 to generate serious rival conjectures and compare their explanatory fit, constraints and prospects for criticism. | A qualified explanatory conjecture, with its grounds and unresolved rivals. |
| A better description of an insufficiently understood phenomenon | Make a purposeful observation or exploratory measurement; vary a condition and inspect what becomes distinguishable. | Observations and possible regularities that can generate or change questions. |
| An empirical consequence of a conjecture | Derive the expected contrast, obtain relevant observations and compare the actual result with it. | Bounded corroboration, a discrepancy or a qualified basis for rejecting or revising the claim. |

**Recover a construction before trying to execute it.** Use this continuation when the source names a desired object or property but you cannot yet obtain the result needed by the question. B.5.RC expands the method below with worked cases and explanations of shared prerequisites, alternative constructions and missing operations.

1. Identify the starting objects or data that are available. State what must be produced and which property the receiving use needs.
2. Find the source's operations for producing or combining those objects. For each needed operation, recover its inputs, application conditions and output. Keep a statement that an object exists with certain properties as an existence claim; seek a way to obtain an instance when the next use requires one.
3. Work backward from the desired result to the required intermediate results and starting inputs. Preserve joint dependencies and alternative ways where the source supplies them. A missing operation is a question for the source or the relevant specialist; a rule you propose is an addition to be tried and justified.
4. Work a small instance from the available inputs, applying each recovered operation when its conditions hold. If the notation prevents the operation, use A.6.3.RT to prepare and compare a more usable expression. For a mathematical account, use its formation and equality rules; identify where a proposed identification changes the operations or property being used.
5. Establish the needed property by the appropriate argument or test. Return the construction and what follows under its premises, or the input, rule or unsupported transition that still prevents the result. Stop when this supplies the receiving use.

For example, a stand specification calls for a portable display. Its assembly rules allow a compatible upright to be joined to a base and a compatible panel to be attached to that upright. Those rules yield the assembly order and the connections to check. Portability remains a requirement to check on the resulting design. If the supplied panel does not fit, the next contribution is a compatible panel, an adapter with its connection rules, or another assembly design. The construction result here is the assembly design; whether the erected stand is stable needs its physical-design argument.

Construction and deduction can work together: an auxiliary object can make a proof possible, and a theorem can suggest a new construction. Novelty does not belong exclusively to one inference type.

For a hypothesis-led test, derive the consequences needed to interpret the test. Check whether those consequences conflict with retained premises, and follow their implications through the part of the model relevant to the question. Return inconsistent premises for revision before relying on their joint prediction. Keep the prediction, observations, measurement conditions and inference recoverable before treating the outcome as corroboration. A simulation establishes a result of the simulated model; applying it to the physical target needs a supported model–world correspondence.

An exploratory finding can supply a hypothesis. Its subsequent empirical assessment must account for how that hypothesis was obtained and for the dependence or selection involved. Use the domain's appropriate design and inference; merely relabeling the same data as a later test does not create independent evidence.

A bounded result may be sufficient at any of these contributions. Assurance belongs to the particular claim and receiving use under B.3 and B.3.3, including the applicable domain proof or validation obligations.

#### B.5:4.3 - Make the result understandable for its use

Explain what was obtained, why the decisive step works, and where the result can be used. The needed depth depends on whether the receiver will apply, criticize, extend or teach the argument.

**Recover the argument needed for that use.** Begin with the conclusion or proposed change the receiver needs to understand. B.5.RA develops both the main reason for the result and the local transitions needed to use it.

1. Read the claim with its domain and conditions. For a mathematical statement, recover the meanings of its objects and quantifiers.
2. Work backward from that conclusion through the intermediate claims or constructions it uses. At each needed transition, identify the premises, the operation or inference, and what it establishes. Follow a shared premise wherever the conclusion depends on it; keep jointly needed premises together.
3. Reconstruct a transition the receiver cannot follow from the source's definitions, rules or worked cases. Obtain the missing explanation or specialist contribution when those do not suffice. A conditional argument can be useful while one premise remains to be established; state that premise and the consequence its failure would have for this use.
4. If a premise or requested result changes, use B.5.RR to follow the affected reasoning and derive what still follows. Preserve joint prerequisites and sufficient alternatives. Stop at a sufficient argument for the receiving use or a named unsupported transition. An unchanged, adequately supported part can be reused; a full reproof is needed only when the question calls for it.

For instance, a team expects to recover a drawing because a backup exists. Recovering that conclusion requires the needed data in a readable format and an available way to decode it. If the backup is encrypted and its key is unavailable, the next question concerns access to that key or another copy of the drawing. Repeating the fact that a backup exists leaves that prerequisite unresolved.

When beginning with an unfamiliar theory, reconstruct its concept of use for one working question. State what the practitioner wants to explain, predict, construct or decide; which objects and relations the theory lets them describe; what information and operations the application needs; and how its result answers that question. Use a source application when it answers the question. Otherwise propose a small application from the theory's stated objects and operations, work it through and test the correspondence. Keep that constructed trial distinguishable from an application already supported by the source. The first result is a usable explanation of that application, or the particular missing premise or operation that prevents it. Use the intended application to choose what to learn next. Study the construction deeply enough to perform or change the contribution the work requires. **B.5.TU** develops this application-construction method, including recovery of the needed operations and use of a correct result that answers only part of the receiving question.

To compare theories or ways of using them, ask the same question of each account. Preserve each source's meanings while comparing what is given, what operations are allowed and what answer follows. If the results differ, identify whether the difference comes from the question, assumptions, mathematical structure, inference or proposed physical mechanism. If one account answers a different question, state that complementary use. Choose or change an account for the distinction the receiving work needs. Use C.29 for a proposed mathematical-lens transfer or local candidate choice; domain prediction and intervention claims still need their applicable Methods and evidence. **B.5.TC** develops the comparison: reconstruct both applications, work a common case, distinguish theoretical differences from approximation or execution, and return the use or inquiry that follows.

When the correspondence between a formal account and its intended use is the difficulty, reconstruct one small instance. Name the variables and their domains, the given inputs, the assumptions and permitted operations, and the statement the calculation or proof establishes. Relate the decisive quantities and conditions to the intended use. A source's worked case can supply this reconstruction; recover the omitted step if the receiver cannot yet carry it out.

Challenge the correspondence with a case that could change the answer. Look for a formally admissible answer that the intended use excludes, or two situations identified by the representation that require different answers. If this exposes a mismatch, repair the domain, constraint, quantity or correspondence, or use the existing result for a weaker question that it does answer. A relaxation can remain useful as a bound even when its optimizer cannot be enacted. The worked case below makes both uses explicit.

For a physical application, connect the mathematical objects and quantities to the phenomenon, measurement and operating conditions. Ask which approximation, omitted interaction, scale or uncertainty could change the conclusion. A rigorous derivation from a model and evidence that the model applies answer different questions.

Use the explanation to test the formulation: does the result answer the intended question, or only the conveniently formalized one? If a distinction was lost, determine whether the use can tolerate that loss, whether a bound suffices, or whether another representation is needed.

#### B.5:4.4 - Settle the question or change the next inquiry

Return the result at its supported scope. Stop when it answers the current use. Continue only for a remaining question whose possible answers could change understanding or action and whose investigation is worthwhile under the available conditions. Account for the effort of learning, obtaining, explaining, checking and maintaining the result as well as calculation cost.

When the result exposes a limitation, identify what must change:

- **The answer or construction for the same question:** repair it or investigate a serious alternative.
- **The formulation:** revise the target, assumptions or boundary and state which earlier results still apply.
- **The available Methods or ways of constructing candidates:** compare retaining, modifying or extending that repertoire. E.23 supplies improvement under an appropriate evaluation; C.18 applies when generation rules, retained alternatives or the effective space of possibilities are the question.
- **A participant's ability to contribute:** distinguish the capability question from missing access or support; use E.23.CAE and E.23.CDI where their conditions hold.

Use **B.5.QD** when the next question is still unclear. Recover a failed dependency or a newly available construction, specify the answer it makes worth seeking, and work a revealing case. This can develop the inquiry after a success as well as a counterexample.

Use E.10.DEV if “development” hides the intended subject and C.36 for an actual cultural-generation, transmission or selection question.

Retain a construction or unresolved alternative when a named future inquiry makes keeping it worthwhile. C.17 can characterize novelty, value and diversity on a declared basis; C.18 distinguishes the archive from a comparison front and a new point from a change in admissible possibilities.

#### B.5:4.5 - Organize human and AI contributions around the work

Calculation, conjecture, proof, explanation, criticism and question formation may be performed with different combinations of people, AI and other tools. Choose that allocation from their actual capabilities, available support, constraints and the evidence needed for the receiving use. Revisit it when those conditions change.

When the question depends on a result from another practice, use [A.15.9][fpf-a15-9-ref] to use the available answer or select a worthwhile missing contribution. State the working question, available inputs, result needed and intended use in terms the receiver can check. If the formal formulation is itself missing, ask the mathematician, physicist or supported AI for that formulation and its correspondence to the working question.

For an engineer, derive the needed capability from representative later work: what must this person be able to understand, ask, construct, criticize or arrange with the assistance that will actually be available? The answer can include interpreting a proof's central idea or recognizing that a measured proxy omits the intended quantity, even when a tool performs most calculations. It can also justify deeper mathematical study when constructing or modifying the theory is the required contribution.

When assessing that capability, use representative work under the declared support and inspect the person's relevant contribution. A completed AI-assisted report alone leaves that contribution underdetermined.

### B.5:5 - Archetypal Grounding

#### B.5:5.1 - A counterexample becomes a constructive mathematical question


An engineer models pairwise incompatibilities with a finite simple undirected graph and asks, “Does connectedness let us divide the vertices into two groups with every edge crossing between groups?”

A triangle is a counterexample: putting the first two adjacent vertices in different groups forces the third to conflict with one of them. This refutes the universal statement but leaves a useful question: **which obstruction prevents such a partition, and can we construct either the partition or a witness of failure?**

Build the tree by keeping an ordered waiting list. The neighbours of a vertex are the vertices joined to it by an edge.

1. Choose any unseen vertex as a root, mark it seen, give it depth 0 and put it on the waiting list.
2. Remove the first waiting vertex. For each of its unseen neighbours, mark that neighbour seen, record the removed vertex as its parent, give it the parent's depth plus 1, and append it to the waiting list. A vertex already seen keeps its first parent and depth.
3. Repeat step 2 until the list is empty. If an unseen vertex remains, start a new root and repeat; this covers disconnected components and isolated vertices.

This is breadth-first search: a discovered vertex waits behind the vertices already waiting. The recorded parent edges form a tree in each component. Assign even-depth vertices to one group and odd-depth vertices to the other. If every graph edge joins opposite parities, these groups give the partition. If an edge joins equal parities, write each endpoint's chain of parents back to the root. Keep the two paths up to their common vertex of greatest depth, discarding the shared part beyond it. The retained paths have an even total length; the extra edge closes a simple odd cycle. An odd cycle cannot alternate between two groups all the way around. Thus the procedure returns either a two-colouring or an odd-cycle witness.

For a worked traversal, take vertices A–F and edges AB, AC, BD, CE, DF and EF. Start at A and inspect neighbours alphabetically. The waiting list changes as follows; the processed vertex is the parent of each newly found vertex in that row.

| Processed vertex | Newly found vertices and depth | Waiting list after processing |
| --- | --- | --- |
| A | B, C at depth 1 | B, C |
| B | D at depth 2 | C, D |
| C | E at depth 2 | D, E |
| D | F at depth 3 | E, F |
| E | None; F was already seen | F |
| F | None | Empty |

A has depth 0, so the groups are {A,D,E} and {B,C,F}; each of the six edges crosses between them. Now add DE. Its endpoints both have depth 2. Their parent paths D–B–A and E–C–A, joined by DE, give the five-edge cycle D–B–A–C–E–D. The added edge therefore prevents the requested two-group partition.

The decisive idea is parity plus a tree-path construction, not the enumeration of many successful examples. The result answers a mathematical question without an empirical test. To use it for allocation, separately establish that vertices represent the relevant items and edges the actual pairwise incompatibilities. If three-way constraints matter, that application question must change.

The concrete practice targets are to explain the obstruction, construct a partition or failure witness for another finite graph, and handle disconnected components. Assess those capabilities on a changed graph with the references and assistance permitted in the intended work.

#### B.5:5.2 - A physical question changes the representation

In a constructed engineering case, a cabinet contains two components. The intended question concerns the hottest component, but a proposed lumped model reports only their arithmetic mean temperature.

Let the modeled component temperatures be T1 and T2, with mean m = (T1 + T2)/2. The states (20,80) and (50,50), in degrees Celsius, both give m = 50. Their maxima are 80 and 50. A stipulated threshold of 60 therefore gives different classifications. On a state set containing both pairs, no function of m alone can recover the maximum or that classification.

A constructive repair retains the signed contrast d = (T1 − T2)/2. Then T1 = m + d, T2 = m − d, and max(T1,T2) = m + |d|. If an independently supported bound |d| ≤ Δ holds for the physical conditions, m + Δ is an upper bound within that model. Otherwise the contrast has to be estimated or measured, or the inference restricted.

The next physical inquiry is concrete: which temperature differences are possible under the actual loading, coupling and time window; how well does one temperature represent each component; and what measurements and error bounds cover the hottest relevant region? Compare a direct measurement, a two-state model and a qualified conservative bound by the evidence each requires and the decision each can support. Use existing adequate physical knowledge before selecting another experiment.

The mathematical argument exposes the lost information. For physical use, justify the two-temperature approximation. A more accurate fit to the same mean cannot settle that lost distinction. The first useful return is the changed quantity and representation question plus the physical premise that would distinguish the continuations.

#### B.5:5.3 - The hypothesis-led route remains short

A service has unexplained latency spikes. B.5.2 supplies a qualified backup-interaction conjecture and serious rivals. Derive an observable contrast between backup and comparison intervals, accounting for traffic and other relevant conditions. If the requisite observations exist, compare them under the domain's inference Method. If they do not, the result can finish as a qualified conjecture and a specified missing test.

A separately qualified operational workaround may already answer the immediate service question. Using it does not require pretending that the causal explanation is established or rerunning a sufficient result through every reasoning contribution.

#### B.5:5.4 - A relaxed problem supports a different use

A planner must choose whole jobs for one worker's four-hour window. At most one A-job is available; it takes three hours and has stipulated value 5. At most two B-jobs are available; each takes two hours and has stipulated value 3. For this constructed problem the values and durations add, and the question is which choice satisfying the stated availability and time limits has greatest value. The reader needs elementary algebra and can enumerate the few integer choices.

Let x and y count A- and B-jobs. The intended constraints are x in {0,1}, y in {0,1,2}, and 3x + 2y <= 4; maximize V = 5x + 3y. An AI-assisted calculation instead allows real x and y with 0 <= x <= 1 and 0 <= y <= 2. It returns x = 1, y = 0.5, V = 6.5.

Recover what that calculation establishes. From the relaxed time constraint, y <= (4 - 3x)/2, so V <= 6 + 0.5x <= 6.5. The returned real-valued pair attains this bound. This is an optimum of the relaxation. The proposed half B-job is excluded by the intended whole-job condition.

For the whole-job question, x = 0 permits at most y = 2 and value 6. With x = 1, the remaining hour permits y = 0 and value 5. Two B-jobs therefore attain the integer optimum 6. The human or tool doing this reasoning can check both feasibility and the comparison directly.

The relaxation still answers a useful question: can any permitted whole-job choice reach value 7? Every integer choice is also feasible for the relaxation, whose proved upper bound is 6.5, so the answer is no. Choosing a realizable assignment needs the integer result; ruling out value 7 needs only the upper bound. With five hours instead, the same argument gives V <= 7.5 + 0.5x <= 8. The choice x = 1, y = 1 attains value 8 in both formulations. The planner can use that relaxed optimum as the whole-job answer because this returned choice satisfies the integer conditions.

Here the human–AI division follows the contribution being sought. A planner can use assisted optimization while being able to state what counts as a whole job, recover the constraints actually solved, and distinguish an attainable choice from an upper bound. If the required work is to develop the optimization Method, its construction and proof become additional capability targets. An exercise can change the time window or divisibility condition and ask the learner to choose the formulation and explain which result answers the question.

#### B.5:5.5 - Understand which composition a theory permits

A practitioner wants one input to feed two operations. Let `X`, `Y` and `Z` be distinct atomic types, with available operations `f: X → Y` and `g: X → Z`. A cartesian account supplies copying, `Δ_X(x) = (x,x)`. The composite `(f × g) ∘ Δ_X` returns `(f(x),g(x))` from one input.

Compare an account generated only by `f`, `g`, identities, serial composition, tensoring and exchange of factors. Here `f ⊗ g` runs the two operations on separately supplied inputs, `X ⊗ X`. Every permitted generator preserves the number of atomic factors; composition and tensoring preserve that property. Therefore those operations cannot construct `X → Y ⊗ Z`. The missing contribution is a second input or an additional copying operation.

The receiving work determines whether copying its input is admissible. The comparison exposes that requirement before selecting an implementation. [Baez and Stay, §2.3](https://arxiv.org/pdf/0903.0340), supplies the cartesian/monoidal distinction; the generated-operation case above makes its use explicit.

#### B.5:5.6 - Choose a first physical model before commissioning a calculation

An engineer is asked whether a stronger external fan can bring an overheating component below 65 °C. In this constructed case, inspection finds the component attached to a metal case through a pad; the fan blows over the outside of the case.

Begin by tracing where heat is generated and how it could leave. The pad suggests a path from component to case, followed by transfer to the surrounding air. Keep the component, the case at the attachment and the air distinguishable: they can have different temperatures, and the proposed fan change acts at the case–air part of that path. Treating the whole device as one temperature would hide the difference relevant to this decision.

Try a steady heat-transfer account first. Assume constant component heating and approximate all generated heat as passing through the pad to the case, with an unchanged linear conductance along that path. The physical premise is that, for a fixed conductance, carrying the same heat per second requires the same temperature difference. [OpenStax, University Physics volume 2, §1.6, equation 1.9](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer) explains that relation for a uniform conducting layer. Approximating this assembly by such a path is the engineer's model choice; inspect bypass paths and contact behavior when assessing it.

Model the case as losing heat only to that air through temperature-driven transfer. At equal case and air temperatures this outward transfer is zero, so a steady case receiving positive heat must remain warmer than the air. The fan increases exchange with the air; air temperature is the ideal lower limit for the case in this model. The same [OpenStax section, introduction and “Convection”](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer) explains the temperature-difference dependence and fan-driven exchange.

Suppose the steady readings are 80 °C at the component, 25 °C at the case attachment and 20 °C in the surrounding air. Take these values as exact for the first conditional calculation. The component–case difference is 55 °C. Under the proposed model it remains 55 °C when only external cooling changes. Even ideal cooling of the case to the 20 °C air therefore leaves the component at 75 °C. Improving only this part of the heat path cannot meet the 65 °C target under those assumptions.

This result redirects the design question toward the component–case path, a new direct heat path or reduced heating. It also identifies what could invalidate the estimate: direct airflow onto the component changes the assumed path, while temperature-dependent heating or conductance changes the fixed-difference argument. For the real device, check measurement uncertainty and those assumptions before relying on the bound. A useful specialist request is now: 'Given this assembly and load, can the component stay below 65 °C after improving its contact to the case; which additional observations would settle that?' The engineer can request that model and calculation without first specifying its equations.

#### B.5:5.7 - Recover an argument, then change its starting point

A reader can use elementary algebra and wants to understand and adapt the claim that the sum of the first n positive odd integers is n squared, for a nonnegative integer n. Let S(n) denote that sum, with S(0) = 0.

Work backward from the formula. It is enough to establish its initial value and how it changes when one term is added. The next odd integer after the first n terms is 2n + 1, so S(n + 1) = S(n) + 2n + 1. The proposed value has the same change: (n + 1) squared - n squared = 2n + 1. Both start at zero. Repeating that step establishes S(n) = n squared for every finite n.

A square of n by n unit cells makes the same step visible. Add one row of n cells and an adjoining column of n + 1 cells; the resulting square has side n + 1. The added cells give 2n + 1. Counting the cells and the algebraic recurrence explain the same increase in different expressions.

Now the requested sum has n terms beginning at 3: 3 + 5 + ... + (2n + 1). Recover which premise changed. These are the first n + 1 positive odd integers with the initial 1 removed. The retained argument therefore gives S(n + 1) - 1 = (n + 1) squared - 1 = n squared + 2n. For four terms, 3 + 5 + 7 + 9 = 24; the old n-squared formula would give 16.

The reusable contribution is the initial-value and increment argument. It lets the reader obtain the changed sum by identifying the changed range and reusing the already established result. A different progression would require recovering its increment before selecting another formula.

### B.5:6 - Bias-Annotation

The examples favor discrete construction and a simple physical representation. Other fields may need probabilistic, interpretive, historical or other arguments with different criticism demands. Select the contribution by the actual question and discipline.

Easy-to-produce outputs can dominate attention. Recover the intended epistemic or practical purpose when speed, proof count, a convenient measurement or the current favorite tool starts determining which question is asked.

### B.5:7 - Conformance Checklist


- **CC-B5.1 — Question and contribution.** The practitioner SHALL identify the question, intended useful result and selected reasoning contribution. A conjecture SHALL retain its grounds, rivals and limits; a construction and its asserted properties SHALL remain distinguishable.
- **CC-B5.2 — Interpretable hypothesis-led testing.** Before claiming empirical corroboration, the practitioner SHALL derive the consequences needed to interpret the test and account for how the tested hypothesis was obtained.
- **CC-B5.3 — Claim-specific support.** A support claim SHALL identify the actual argument or result, its relevance, scope and limitations. An assurance level, when needed, SHALL follow B.3.3 and the applicable domain criteria.
- **CC-B5.4 — Result and continuation.** For a performed empirical test, the practitioner SHALL keep its actual outcome, including a failed or inconclusive result, recoverable through A.10. A further inquiry SHALL use the actual result with its limitations and name the remaining question; a sufficient answer may finish the use.
- **CC-B5.5 — Development-state use.** When B.5.1 is used, an actual transition SHALL meet its project and domain conditions. A reasoning result alone does not establish a development-state transition.
- **CC-B5.6 — Application and change.** The practitioner SHALL distinguish a mathematical result from its physical application and a change of answer, question, Method or capability when that distinction changes the intended use.
- **CC-B5.7 - Recoverability for the receiving use.** When recovering a construction or argument, the practitioner SHALL identify the required inputs and the operations or inferences needed by that use. A missing rule or unsupported transition SHALL remain explicit. A conclusion reused after a premise changes SHALL state which argument or construction still supports it.

### B.5:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Repeatedly improve the fit of a model that omits the intended quantity. | Test the representation against a small action-changing counterexample; recover the missing distinction or qualify a sufficient bound. |
| Treat exploratory regularities as if they were independently predicted and tested. | Preserve their origin and use a design and inference that account for the selection and dependence. |
| Produce an argument whose receiver cannot identify what the crucial step establishes. | Work backward from the needed conclusion and recover the decisive transition and its premises. If a premise changes, follow its effect through the argument. |
| Generate more answers after the important question has changed. | State the changed formulation and which prior results still answer it before selecting further production. |

### B.5:9 - Consequences

The Method preserves cheap use of adequate results while making constructive and question-changing work available. It connects mathematical reasoning, physical interpretation and epistemic criticism without imposing one proof or empirical regime on them.

The cost is attention to purpose, premises and continuation. Keep that effort proportional: one counterexample or a short explanation can settle the question. A difficult theorem or consequential physical inference can demand specialist work and substantially stronger evidence.

### B.5:10 - Architectural Rationale

Inquiry connects different kinds of useful results. A construction supplies an object or procedure; a deduction establishes an implication; a conjecture offers an explanation; observations supply evidence about a phenomenon. Their value depends on what question they answer and what further use their support permits. Treating every result as an explanatory hypothesis would obscure these differences.

Question formation belongs here because the result of one reasoning contribution can alter the premises or aim of the next. Detailed object identity, mathematical-lens use, evidence, search and capability development retain their own Methods. Their results can enter an inquiry without turning each PatternID into a required stage.

### B.5:11 - SoTA-Echoing

**Which reasoning remains useful as result production becomes cheaper?** Adapt Tao's [*Mathematics in the age of AI* (2026), §§2–8](https://arxiv.org/html/2608.16753v1): select the contribution by mathematical and practical purposes, rather than problem-output count alone. Compared with continuing the same production task faster, §§4.1 and 4.4 make a changed question or repertoire available. This accepts the cost of purpose and interpretation work when it can change the next inquiry. Tao's strong-capability premise is conditional.

**What makes a produced proof useful to its receiver?** Adapt [Klowden and Tao (2026), §§4.2, 4.4, 6.3–6.4](https://arxiv.org/html/2603.26524v1): recover the intended statement and the explanatory structure that enables reuse. Section 4.3 explains how to recover the needed transitions and follow a changed premise through their dependencies. Formal correctness suffices for some formal questions; application or extension can require this further account. Compared with rechecking the whole proof, the selected recovery spends effort on the receiver's unresolved use. The paper provides a conceptual rationale for this recovery; the odd-sum example applies it to a small argument.

**Must reasoning always begin with an explanatory hypothesis?** Retain hypothesis-led inquiry where it fits and adapt [Rodin (2023), §§3–6](https://arxiv.org/html/2301.08131v1) for constructive work: recover object-forming operations as well as propositions about their results. Section 4.2 recovers inputs and rules before performing a construction; the graph case shows construction and justification together. An existence statement may answer the question of existence. When the next use needs an instance or procedure, recovering its construction supplies a further result. This accepts the cost of reconstructing only the needed operations, while leaving the choice of mathematical foundation to the question and subject practice.

**How can an inquiry begin before equations are available?** Adapt the qualitative entry described by Etkina and Brookes in [the ISLE method explanation](https://www.islephysics.net/why-isle.html): observations can lead to proposed mechanisms, consequences and discriminating tests before quantitative formalization. Section 4.1.1 makes a first provisional account available; section 5.6 works an engineering model choice. ISLE supplies an instructional method in a supported learning setting.

Reopen these choices when a better method at comparable effort changes the attainable result, a receiving use needs a different explanation or criticism regime, or changed tools alter the useful division of contributions.

### B.5:12 - Relations

- **B.5.2** supplies the explanation-led abductive Method; **B.5.1** coordinates development states when that separate question is current.
- **C.22.2** supplies an inspectable problem formulation and next use. **C.29** supplies mathematical-lens selection and correspondence, including preserved and lost structure.
- **A.15.9** supplies bounded use or acquisition of another practice's result, including help with a missing formulation.
- **A.6.3.RT** prepares and compares an expression when its representation hinders the needed operation. The construction or argument obtained through that expression remains the result of the applicable subject Method.
- **B.3, B.3.3 and A.10** govern claim-and-use-specific assurance and evidence reliance.
- **C.17, C.18 and C.19** supply novelty/value/diversity characterization, archive/front and possibility-space distinctions, and live-pool treatment when those questions arise.
- **E.23, E.23.CAE and E.23.CDI** distinguish object improvement, capability-expression questions and development of a named capability holder. **E.10.DEV** recovers ambiguous development claims; **C.36** governs the cultural-evolution question.
- **B.4** can use these reasoning results in an actual evolution inquiry. A sufficient reasoning result does not itself require another evolution cycle.

[fpf-b5-4-ref]: B.5.4-Recognize-a-Reusable-Concept-in-a-Concrete-Situation.md#b54---recognize-a-reusable-concept-in-a-concrete-situation

[fpf-a15-9-ref]: A.15.9-Request-and-Use-a-Bounded-Result-from-Another-Practice.md#a159---request-and-use-a-bounded-result-from-another-practice

### B.5:End
