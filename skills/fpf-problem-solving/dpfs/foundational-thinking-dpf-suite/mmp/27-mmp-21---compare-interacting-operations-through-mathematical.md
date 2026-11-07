## MMP.21 - Compare Interacting Operations through Mathematical Models

> **Status:** Stable

> **Type:** Method pattern
>
> **Normativity:** Normative within the stated use

### MMP.21:1 - Problem frame

**Use this when** materially different ways of ordering, combining or allocating method contributions are plausible, and their interaction can change the receiving result. Two checks may compete for the same performer. A parallel summary may discard a distinction needed later. A reordered operation may preserve the final object while changing the answer on which someone acts.

Begin with one consequence that could change the choice, then construct the smallest mathematical account that can distinguish the arrangements. The first useful result is a derived property, feasible construction, bound or counterexample, interpreted back into the method comparison.

This method refines C.32.MWA.PP's comparison of arrangements. Here an arrangement concerns how contributions are connected for the selected work; it need not form one Method whole. The mathematical model represents the relevant operations, observations and shared resources. C.29 supplies the correspondence to the working situation. B.1.5.CM supplies the separate judgment about whether participant Methods and their whole relations actually obtain.

Preparation requires the ability to describe the proposed work and its criteria, elementary algebra, and reasoning about functions, inequalities or finite sequences. A larger concurrent model may require a specialist using CMP.14. The specialist's result must expose the property, assumptions and decisive construction or counterexample needed by the method decision.

Use ordinary C.32.MWA.PP comparison when the consequences are already clear and another model would add nothing. A different diagram of the same arrangement is not a rival. If only the status of a proposed Method whole is at issue, use B.1.5.CM. This method compares arrangements; constructing and introducing a changed way of working requires its own design and realization.

### MMP.21:2 - Problem

Locally adequate contributions can fail together. Their inputs may have incompatible meanings, their conditions may not survive another contribution's operation, or their combined demand may exceed an available resource. Conversely, arrangements that look different can preserve everything the receiver needs.

A mathematical model can resolve these questions only if it retains the distinctions that matter. A proof about a reduced description may otherwise conceal the difference that should have changed the decision.

### MMP.21:3 - Forces

| Force | Tension |
| --- | --- |
| Useful simplification | A small model makes comparison affordable, while omitted observations or shared resources can reverse it. |
| Local and combined adequacy | Each contribution can satisfy its own conditions while their connection fails. |
| Result and history | Equal final values can accompany different intermediate answers, delays or failures. |
| Composition and allocation | Independent operations can overlap in principle while competing for the same equipment or attention. |
| Mathematical and practical grounds | A derivation establishes what follows from the model; reliance on the work requires the correspondence and assumptions to hold. |
| Comparison and development | A result can reject or retain an arrangement without constructing a replacement or requiring a new trial. |

### MMP.21:4 - Solution

MMP.10 supplies the mathematical formulation and its answer correspondence. MMP.18 supplies compatible exchanges when component models must first be coupled. This Method uses those contributions for a different choice: which proposed connection, order or allocation of working operations preserves the receiving consequence under shared conditions? Its construction below retains the observations and capacities needed to distinguish the arrangements and derives the conditional comparison. An adequate existing formulation is an input, not a reason to repeat modeling.

Select the consequence, model the competing arrangements and their interactions, derive the difference, and return what it changes in the Method decision.

#### MMP.21:4.1 - Fix the receiving question and the actual alternatives

Take the receiving result and its criteria from C.39.RQ, or reuse an adequate account already available. Take the serious alternatives from C.32.MWA.PP. State how their proposed ordering, result use, allocation or shared resources differ. Keep a feasible incumbent in the comparison when it remains an option.

Choose the property that matters now. Examples include preserving an answer after regrouping work, completing before a deadline with the available capacity, preventing an obsolete result from being used, or ensuring that a required response eventually occurs. Name the inputs, variations and operating conditions over which it is required.

Distinguish an existence question from a guarantee. Finding one schedule establishes that the model admits that schedule; it does not show that every allowed scheduling policy will meet the deadline. Finding one successful sequence does not establish that all allowed interleavings preserve the result.

Retain each alternative's status. A proposed allocation, available tool, performed operation and obtaining Method relation are different facts. Carry a proposed arrangement's unconfirmed conditions into the result.

#### MMP.21:4.2 - Represent the operations and the distinctions the receiver uses

Use C.29 to say what the mathematical objects represent. Define the relevant inputs, state, operations, outputs and conditions. For a sequential contribution, a function or partial function may suffice. For a changing document, state can include its revision and which revision a result concerns. For a shared resource, include its occupancy and availability.

Choose what the receiver can observe. Retain an intermediate answer if another step uses it, even when it disappears from the final store. Retain case identity or version when using the wrong case or version changes the result. If probability, timing or cost matters, represent that quantity and the assumptions supporting it; a plain set of possible outputs does not supply its distribution or duration.

Distinguish what is known from what the model assumes. A measured duration, a proposed upper bound and a convenient constant have different grounds. A human or automated performer can be represented by a transition rule for this calculation, but the rule needs a correspondence to the capability and conditions of that performer.

When alternatives use different representations, interpret both through the selected receiving quantities. MATH.18 supplies preservation and recovery across mathematical accounts. If a summary sends two cases to the same value but their required answers differ, that summary cannot support the comparison without recovering the lost distinction.

#### MMP.21:4.3 - Construct the connection, including shared resources

For sequential functions, form \(g\circ f\), meaning first \(f\), then \(g\). Check that every relevant output of \(f\) is an allowed input of \(g\), including its meaning and conditions. With partial functions, determine the inputs on which the composite is defined. MATH.17 supplies the operation collections and closure argument.

Associativity permits regrouping a fixed sequence. Reordering needs a different property: the two orders must agree in the observations the receiver uses. If the operations return information as well as changing state, retain both in that comparison.

For overlapping work, represent the shared state or resource once. Connecting two models that each contain a private copy of the same bench or performer doubles the modeled capacity. Describe when each operation can begin, what it reads, what it changes or occupies, and when it releases a resource.

For example, let operation \(i\) have start time \(s_i\), fixed duration \(d_i\), and resource demand \(r_{ik}\) on resource \(k\). For nonpreemptive work, a precedence \(i\) before \(j\) requires

\[
s_j\geq s_i+d_i.
\]

If the available capacity is \(c_k(t)\), then at every time \(t\),

\[
\sum_{i:\ s_i\leq t<s_i+d_i}r_{ik}\leq c_k(t).
\]

Add input-availability and deadline conditions where they matter. These inequalities describe one timing model; interruptions, setup, rework or uncertain durations require the corresponding extension when they can change the answer.

Use CMP.14 when communications or interleaved updates need a computational interaction model. It supplies allowed steps, interference, coordination and progress arguments. For ordinary schedules or algebraic combinations, the simpler construction can be sufficient.

#### MMP.21:4.4 - Derive the property or the separating case

Carry out the mathematical operation that can settle the question. Compose the functions, derive the resource bound, build a schedule, or explore the allowed transitions. A model name or a diagram is not yet that result.

For a preservation claim, state the condition initially and show why each allowed step retains it. For modular reasoning, establish what each contribution guarantees under its assumptions, then check that the connected contributions and environment supply those assumptions. Two contributions that each wait for the other's result can both satisfy a conditional promise while neither starts. Progress requires an enabling basis and any needed scheduling or delivery assumptions.

For a failure claim, give the input or sequence that produces the prohibited consequence. One admitted counterexample defeats a universal assertion. Check whether it represents a possible working case; an over-broad abstraction can introduce a sequence the work cannot realize. Conversely, a model that omitted a real interaction can miss a failure. CMP.14 and the applicable mathematical interpretation supply the needed refinement.

For a finite construction, exhaustive exploration can establish the property over the explored state space. A few simulation runs establish their observed outcomes. A bound may settle the question without enumeration; if even an optimistic capacity bound misses the deadline, searching more schedules under the same conditions cannot repair that alternative.

Keep the scope of equivalence explicit. Equality of final outputs can be sufficient for a final-output question. Equality of histories, distributions or burdens requires those distinctions in the comparison. A later receiving operation may distinguish arrangements that were equivalent for the earlier use.

#### MMP.21:4.5 - Compare the consequences without hiding moved burden

Return the result in the quantities and conditions chosen in :4.1. Explain which alternative preserves the required answer, which fails, which remains unresolved, and why. Where alternatives trade off time, effort, retained information or another criterion, keep the distinct consequences available to C.32.MWA.PP and the applicable C.11 choice.

Include burden moved by the arrangement: a faster central step may require more preparation elsewhere; releasing a checked snapshot may require storage while a newer revision awaits review; independent instruments may still require the same operator. A local improvement is useful only to the extent that the receiving comparison can accept those effects.

Compare the chosen model with a cheaper sufficient argument. A two-step trace can expose an ordering failure without a model checker. A workload lower bound can rule out a schedule without detailed simulation. Use a larger construction when it can change an unresolved consequence or support a broader claim that the decision actually needs.

The outcome may support retaining an incumbent, rejecting one proposal, preserving several alternatives, or selecting a bounded trial. It need not rank every arrangement. Existing FPF choice, Pareto and improvement methods govern those results; no new scoring rule is introduced by drawing a mathematical model.

#### MMP.21:4.6 - Interpret the result and reopen the affected premise

State the mathematical conclusion and the working conclusion it supports. For example: under the stated durations and exclusive-resource rule, no schedule of this arrangement completes by the deadline; if those conditions describe the proposed work, this arrangement cannot meet that criterion.

For reliance on actual work, examine the correspondence where a wrong premise could change the decision. Existing observations or a subject argument may suffice. If the decisive uncertainty concerns setup time, operator availability or a possible edit, obtain the relevant clarification only when its contribution warrants the effort. C.11.DUA governs that choice. A mathematical comparison does not create a requirement for an experiment.

A changed premise returns to its affected operation or constraint. Adding a second bench leaves the operator constraint unchanged. Allowing an intervening update can invalidate a formerly adequate sequence. Changing the requested statistic can invalidate an otherwise correct summary. Preserve conclusions whose conditions remain unchanged.

Use B.1.5.CM when the receiving claim concerns an actual Method whole and its participant relations. Mathematical composition alone establishes neither those relations nor a performed trial. If the comparison reveals a needed change of procedure, return the candidate's required behavior for construction; if it only reveals a different description of the same behavior, say so. A comparison can finish with its conditional decision and return condition.

### MMP.21:5 - Archetypal Grounding

The following constructed cases expose different comparison questions.

#### MMP.21:5.1 - Compare centralized calculation with combined local summaries

Two teams must report the mean of all their measurements. The proposed arrangements are to send every measurement to one calculator, or to compute a summary in each team and combine the summaries. All values have the same meaning and units, and every included measurement has equal weight.

Represent a finite list \(x=(x_1,\ldots,x_n)\) by

\[
T(x)=\left(\sum_{i=1}^{n}x_i,\ n\right).
\]

Combine pairs by \((s,n)\oplus(t,m)=(s+t,n+m)\). For concatenation of lists \(x\) and \(y\),

\[
T(x\,y)=T(x)\oplus T(y).
\]

Both components follow from adding the sums and counts. Pair addition is associative, so repeated regrouping preserves the summary. For a nonempty combined list, recover the mean as total sum divided by total count. This supplies the composition and recovery needed by the parallel arrangement.

With lists \((0,4)\) and \((10)\), the summaries are \((4,2)\) and \((10,1)\). Their combination is \((14,3)\), giving \(14/3\), the same mean as central calculation. Averaging the two local means instead gives \((2+10)/2=6\), answering a different weighting question.

The mathematical comparison supports using sum-and-count summaries when this mean is the receiving result. Application requires consistent inclusion and weighting rules, with every included record assigned to one team and counted once. The algebra uses exact addition; a rounded implementation needs the relevant numerical error comparison. Whether the two teams use those rules needs grounds from their work.

Now the recipient asks how many measurements exceed \(3\). Replacing \((0,4)\) by \((2,2)\) leaves the local sum-and-count pair unchanged, and leaves the combined pair \((14,3)\) unchanged, but changes the requested count from two to one. No rule using only that pair can distinguish the cases. The earlier mean-equivalence remains valid; the new question needs another retained quantity or a return to the measurements. The method decision must not treat the old summary as a substitute for all uses of the records.

#### MMP.21:5.2 - Compare parallel checks with their shared capacity exposed

A team considers one automated test bench versus two independent benches. Two preparations can run independently from time zero, each with its own analyst. Preparation A takes three minutes; preparation B takes two. Each subsequent check occupies a bench for four minutes. Both completed check results are required for one minute of final assembly.

For this calculation, durations are fixed, the work is nonpreemptive, and setup and transfer times are zero. Benches and the final assembler are available when needed, with no competing work. Checks initially require no continuously attending operator. The required completion time is at most ten minutes.

With two benches, check A runs from minute 3 to 7 and check B from 2 to 6. Assembly runs from 7 to 8. The model admits completion at minute 8.

With one bench, the two checks cannot overlap. A feasible schedule is B from 2 to 6, A from 6 to 10, and assembly from 10 to 11. No schedule finishes earlier: the bench cannot start a check before minute 2 and must perform eight minutes of check work before the final assembly minute. Thus eleven minutes is both a lower bound and an achieved value.

The one-bench arrangement fails the ten-minute criterion under these premises. The two-bench arrangement passes that criterion in the constructed schedule. Whether acquiring or allocating another bench is worthwhile remains a choice involving its availability and other burdens. The calculation does not supply those missing facts.

**Changed premise.** Both checks now require one qualified operator throughout, and only one such operator is available from minute 2 onward. Add a capacity-one operator constraint to the model. Two benches no longer permit overlap: there are still eight exclusive operator minutes, no check can begin before minute 2, and assembly follows both checks. The eleven-minute lower bound applies again and the same serial schedule attains it.

A hardware-only proposal therefore does not repair the deadline under the changed condition. The useful next comparison concerns an available arrangement that changes the limiting condition, or a justified change of requirement. Merely redrawing two parallel lanes leaves the conflict in place.

#### MMP.21:5.3 - Compare orders by the result a later action consumes

A publication team proposes two arrangements for an edit and a review: edit then review, or review then edit. The required result is that the released artifact is the revision to which the review result applies. Review quality is a separate criterion; this comparison concerns revision correspondence.

Use state \((v,c,p)\): \(v\) is the working revision, \(c\) the reviewed revision, and \(p\) the released revision. Initially the state is \((0,\bot,\bot)\), where \(\bot\) means none. Model an edit \(E\) as incrementing \(v\), a completed review \(K\) as setting \(c=v\), and release \(P\) as setting \(p=v\). No other operation occurs in the initial model.

| Proposed order | States after its steps | Required result |
| --- | --- | --- |
| \(E;K;P\) | \((1,\bot,\bot)\), \((1,1,\bot)\), \((1,1,1)\) | \(p=c\) holds. |
| \(K;E;P\) | \((0,0,\bot)\), \((1,0,\bot)\), \((1,0,1)\) | \(p=c\) fails. |

Both orders finish with working revision 1. A model retaining only \(v\) would make them look equivalent and lose the distinction needed by release. The separating trace rejects the second ordering for the stated criterion.

Now the environment permits an additional edit after review but before release. Even the first ordering admits

\[
(1,1,\bot)\ \longrightarrow\ (2,1,\bot)\ \longrightarrow\ (2,1,2).
\]

Its earlier result depended on excluding this intervention. The team also offers an arrangement that retains an immutable copy of the reviewed revision and releases that copy. In the same situation it releases revision 1, giving \(p=c=1\), while the workspace contains revision 2. This arrangement satisfies the revision-correspondence criterion if the copy and its review association are actually preserved. It leaves a different question: is releasing revision 1 still useful and permitted, or does the receiving work require revision 2? C.39.RQ and C.32.MWA.PP retain that criterion and trade-off rather than silently replacing it.

The comparison supplies a condition for the release arrangement, not evidence that anyone performed the review or retained the copy. If source-copy retention or release selection needs implementation, that construction remains to be done.

#### MMP.21:5.4 - Use a mathematical construction to change how work is divided

- **Situation:** A repeated calculation gathers all measurements in one place, while the measurements are already available to several teams.
- **Question:** Can the teams return smaller contributions that preserve the required answer, and what must change when the recipient asks a different question?
- **First useful result or blocker:** A proposed distributed procedure with a derivation of its preserved answer and its resource consequences, or the information the proposed summaries lose.
- **Start with:** C.39.RQ for the receiving requirement, [MMP.21](27-mmp-21---compare-interacting-operations-through-mathematical.md) for the comparison, and [MMP.22](28-mmp-22---construct-a-way-of-working-through-mathematical-tra.md) to turn the mathematical construction into a changed procedure.
- **Stop or return:** Retain the current procedure when the new one has no worthwhile benefit. A changed required answer returns to the summary and recovery construction; if a team's capability or support changes, reconsider the affected allocation or support before relying on the procedure.

**1. Choose the answer to preserve.** The recipient needs the mean of all included measurements, each with equal weight. The records have the same units and meaning. C.39.RQ retains those conditions when a team proposes sending local means instead of individual measurements.

**2. Compare the mathematical constructions.** MMP.21 exposes the weighting difference. For local lists (0,4,0,4) and (10,10), the local means are 2 and 10. Averaging those means gives 6; the mean of all six measurements is 28/6, or 14/3.

MATH.17 supplies an operation on summaries: represent a list by its sum and count, and combine two pairs by adding their respective components. This operation is associative. MATH.18 supplies the interpretation question: does summarizing a concatenated list give the same result as combining its summaries? Here both routes give the total sum and count. Division recovers the required mean when the total count is positive. The construction preserves this answer for any partition under the stated inclusion and weighting rules.

**3. Construct the changed way of working.** MMP.22 now uses that mathematical result to propose local sum-and-count calculation followed by pair addition and division. Every included record must be counted once; each team must have its assigned records and deliver the pair before the result is needed. These are requirements on the changed procedure and its support. The algebra does not establish that the teams already have those capabilities or connections.

For k nonempty teams and N scalar measurements, the proposal transmits 2k scalar values instead of N, apart from any identifiers and communication overhead. It can reduce that transfer when N exceeds 2k, while adding local calculation and coordination. In the small example, four scalar values replace six. C.32.MWA.PP and C.11.MV compare that contribution with the total burden; equality of the mean alone does not establish practical improvement. Rounded computation needs its numerical error allowance.

**4. Describe and introduce only the supported change.** A.3.2.DE makes the selected procedure and its conditions available to its users. B.1.5.CM addresses a claim that the participating Methods constitute a Method whole when that claim matters. A.3.1.MI addresses introduction into practice; A.3.1.WT supplies a trial only when the result it could obtain is worth the work. Existing adequate grounds can suffice for the decision being made.

**5. Reopen the construction when the required result changes.** The recipient now also needs the number of measurements greater than 3. Replacing the first list by (2,2,2,2) preserves its sum and count, hence the overall mean, but changes the total above 3 from four to two. The old pair cannot supply the new answer.

MMP.21 returns this separating case to MMP.22. Add a local count above 3 to the summary and combine those counts by addition, or retain access to the original records. The former mean calculation remains valid. Here three values per team would again transmit six scalars, so the original reduction in their number disappears. A later change of threshold can require a different retained contribution again. C.39.RQ preserves the revised requirement, while A.3.2.DE describes the revised instruction.

### MMP.21:6 - Bias-Annotation

A familiar notation can make its retained quantities seem like the only relevant ones. Start with the receiving consequence before selecting a function, graph, schedule or simulation.

Treating every participant as an independent resource can conceal shared attention, access or preparation. Treating a participant as permanently occupied can make an arrangement look worse than its actual operation. Model the demand and release conditions that the comparison uses.

A favorable trace or convenient parameter choice can conceal an allowed failure. Conversely, an overly permissive environment can manufacture an obstruction. Preserve the assumptions that make the example or counterexample relevant.

### MMP.21:7 - Conformance Checklist

When the comparison is used for a decision, the following content must be recoverable from the calculation and its explanation.

| Check | Required content |
| --- | --- |
| Working question | The receiving consequence, criteria and materially different arrangements. |
| Correspondence | What the model represents, with decision-changing omissions and assumptions. |
| Connection | Applicable inputs and outputs, relevant order or overlap, and shared resources represented once with their stated capacity limits. |
| Mathematical result | A derivation, construction, bound or reproducible counterexample at the stated scope. |
| Result strength | Existence, universal preservation, observed simulation outcome and practical reliance are distinguished where they change the decision. |
| Comparison | Consequences and moved burdens are returned to the receiving criteria without an invented aggregate score. |
| Continuation | The supported decision, unresolved premise or changed-condition return; Method-whole claims remain with B.1.5.CM. |

### MMP.21:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Compare pictures whose underlying arrangements are identical. | Identify the changed relation or finish with a change of description. |
| Infer combined adequacy from isolated component success. | Model the connection and establish the property needed of the combination. |
| Treat associativity as permission to reorder work. | Compare the two orders under their required observations. |
| Duplicate a shared performer or tool inside separate branches. | Use one shared-capacity account and recompute feasible overlap. |
| Treat one successful run as a guarantee over allowed interactions. | Retain its observed scope or derive the broader property. |
| Treat a model's counterexample as an observed work failure. | Check the correspondence and state whether the result is a possibility, an impossibility under assumptions, or an observation. |
| Turn mathematical composition into Method parthood. | Return the mathematical consequence to C.32.MWA.PP; use B.1.5.CM for whole identity and obtaining relations. |

### MMP.21:9 - Consequences

A comparison can expose an impossible deadline, justify regrouping work for a selected result, or locate the interaction that makes one arrangement fail. Some alternatives can be discarded before costly implementation, while others remain useful under different conditions.

The result is narrower than a complete endorsement of a way of working. Unmodeled quality, capability or access can still decide the choice. Additional mathematical detail is worthwhile only when it changes a needed consequence or its support.

### MMP.21:10 - Architectural Rationale

C.32.MWA.PP selects the structures and alternatives that matter to a Method decision. This method adds the construction that makes an interaction calculable: compatible operation domains, retained observations, combined resource demand, and a property or counterexample of the proposed connection.

MATH.17 and MATH.18 supply operations on operations and comparison through interpretations. CMP.14 supplies computational interactions when shared state or communication makes ordinary sequential composition insufficient. C.29 connects those mathematical results to the working situation.

The distinction between model and work is productive: a conditional impossibility can already reject a proposed arrangement under accepted conditions, while an uncertain premise can identify the clarification that matters. Neither result needs a claim that the mathematical components are actual parts of one Method. B.1.5.CM handles that separate question.

### MMP.21:11 - SoTA-Echoing

The practice question is how to compare interacting method contributions without reducing the decision to isolated scores or expanding every case into a large simulation. The selected line uses a property-specific model, explicit composition conditions and the least costly adequate derivation. The three worked cases show why different receiving questions need different retained structure.

**Resource composition versus isolated timing or unrestricted simulation.** [Arronategui, Bañares and Colom, *Large scale system design aided by modelling and DES simulation: A Petri net approach* (2025), §§2.2, 4–5](https://onlinelibrary.wiley.com/doi/full/10.1002/spe.3374) develops interpreted components, shared-resource composition and structure-preserving execution. It also distinguishes properties preserved by construction from failures that composition can introduce. **Adapt** this line in :4.2–:4.4: assign meanings to model elements and derive the selected combined property. Petri nets are an option for larger interacting systems; the inequalities in :5.2 settle the smaller capacity question more cheaply. Simulation becomes a serious alternative when analysis is impractical, with its outcome qualified accordingly. Reopen the representation when omitted resource or timing behavior changes the comparison.

**Compositional contracts versus whole-model verification.** [Dewes and Dimitrova, *Contract-based Design and Verification of Multi-Agent Systems with Quantitative Temporal Requirements* (AAAI 2025), §§4–6](https://arxiv.org/html/2412.13114v1) supplies a contemporary construction for local obligations, shared requirements and modular verification. Its experiments show a trade-off: smaller component checks can avoid the memory burden of a whole-model check, while their overhead can lose on small specifications. **Adapt** :4.4–:4.6 to check assumption compatibility and reopen dependent conclusions after changes. Retain a short whole-model argument when it suffices. The source's temporal logic, quantitative combination rule and computational-agent assumptions are not universal requirements for Method comparison.

For operation regrouping and interpretation, MATH.17 and MATH.18 provide the general mathematical constructions used in :5.1 and :5.3.

These sources supply mathematical and computational modeling methods, not empirical proof that a proposed organizational arrangement improves work. C.39.RQ supplies the situated criteria, and C.29 governs application of the derived consequence. Reopen the comparison when a new source method answers the same practical question with less effort or when a material work distinction defeats the present model.

### MMP.21:12 - Relations

- **MMP.10** supplies the required formulation and answer interpretation; **MMP.18** supplies a joint model when component exchange or shared dependence is still unresolved. Reuse either result at its actual scope.
- **C.39.RQ** supplies situated requirements and their subjects. **C.32.MWA.PP** supplies the broader comparison and receives the derived consequence, moved burden and qualification.
- **B.1.5.CM** resolves a proposed Method whole into supported obtaining relations or a prospective account. Equality or composition of mathematical descriptions does not perform that work.
- **MATH.17** constructs admissible operations and their composition laws. **MATH.18** constructs interpretations and tests what transfers between mathematical accounts.
- **C.29**, with **C.29.1–.3** where needed, supplies subject correspondence, result transfer, computational formulation and realization.
- **CMP.14** constructs and checks computational interaction when shared state, messages or progress matter. Its environment assumptions remain visible in the receiving Method comparison.
- **C.11 and C.11.CRC** supply choice and contribution comparison; **C.18** governs Pareto or retained-alternative treatment; **E.22 and E.23** supply evaluation and improvement. **C.11.DUA** governs whether another observation or trial is worth its burden.
- **MMP.22** addresses construction of a changed Method from a mathematical transformation. The present result is a comparison or a returned construction requirement, not an assertion that the changed Method has been obtained.

### MMP.21:End
