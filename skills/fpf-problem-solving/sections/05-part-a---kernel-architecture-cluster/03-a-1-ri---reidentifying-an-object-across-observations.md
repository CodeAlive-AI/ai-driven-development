## A.1.RI - Reidentifying an Object across Observations

> **Type:** Method pattern
> **Status:** Draft
> **Normativity:** Normative

### A.1.RI:1 - Problem frame

Use this pattern when the next calculation or action depends on whether observations concern the same continuing object, and the available identification does not yet settle that question. A moving object appears again after an observation gap. Two tracks compete for one detection. A process number appears in reports made before and after a restart.

The subject practice supplies what counts as continuation of that object: permitted motion, a process lifetime, a material continuity rule or another applicable criterion. The Method constructs and compares the connections that the observations and those rules allow.

**First useful move.** Name the object whose continuation matters and the use that depends on it. Then examine one available observation for a feature that distinguishes continuation from a live competing account. For a process run, a changed start time can settle a question that an unchanged process number leaves open.

The result is an identification or exclusion supported by the available premises, or the remaining alternatives relevant to the next use. It can be conditional on a stated motion or observation account. An adequate existing identification can be used directly.

This Method assumes that the object-continuation criterion and the relevant subject rules can be recovered. Constructing a new criterion, motion theory, sensor model or tracking algorithm is further work when one of those contributions is missing. A question about an aggregate quantity may be answerable without deciding which observation belongs to which object.

### A.1.RI:2 - Problem

Observations describe what was found at particular occasions and under particular conditions. They can differ while concerning one object, or resemble one another while concerning different objects. A repeated name, location or appearance therefore has the identifying force supplied by the subject rules and observation conditions.

Pairwise plausible connections can also conflict. Under a model in which each object is detected once, assigning the same later detection to two earlier objects fails the joint account. Conversely, several complete associations may all satisfy the available constraints.

The practitioner needs to determine what the observations actually resolve and carry that result into the next calculation or action.

### A.1.RI:3 - Forces

| Force | Tension |
| --- | --- |
| Continuation and change | An object can change while continuing; the relevant criterion determines which changes matter. |
| Local resemblance and joint compatibility | A good pairwise match can prevent a coherent association of the other observations. |
| Observation gaps and available rules | Rules can connect separated observations while leaving more than one connection possible. |
| Ranked choice and resolved identification | A preferred hypothesis may support an action even when the observations have not excluded its rivals. |
| Information and cost | Another observation can distinguish alternatives, but the receiving use may already be possible. |
| General Method and subject construction | The association procedure is reusable; its motion, lifetime and observation rules are subject-specific. |

### A.1.RI:4 - Solution

Recover the continuation question, construct the relevant associations under the subject rules, test their joint compatibility and use the distinctions they actually support.

**Name the continuing object → recover observations and rules → construct competing connections → test them together → resolve what the use needs → continue or reopen.**

#### A.1.RI:4.1 - Recover the continuation question

State which object the observations may concern and what would count as its continuation through the interval or change. A continuing software service, one process run and one execution of a requested job have different boundaries. Choose the object required by the question.

Recover the relevant temporal and contextual scope. Coordinates need a frame; a local process number needs the system and naming scope in which it was issued. If the observations use different references, establish their correspondence before comparing values.

State the receiving use. Estimating one object's displacement needs its association across observations. Estimating the mean position of a fixed observed population can leave those associations unresolved.

#### A.1.RI:4.2 - Separate observations, rules and assumptions

Recover the observations already available, their occasions and the limitations that matter to this question. Distinguish the observed indication from a position, identity or event inferred through it. C.16.MR and C.16.IR help when the measurement interpretation itself remains unresolved.

Recover the subject rules used to connect those observations: allowed changes, motion bounds, lifecycle events or other continuity conditions. Include the observation conditions needed by the connection. “Each object was observed once” and “the set of objects stayed fixed” are substantive premises when they make the association one-to-one.

Keep an assumed rule available as an assumption. A conclusion derived under it can be useful while a later question requires a different or better-supported account. Use the assurance and information work appropriate to that receiving question.

#### A.1.RI:4.3 - Construct the materially different connections

Construct the associations still possible under the available account. A connection states which observations concern the continuing object and how the subject rules permit the intervening change. In a small finite case, listing the alternatives can be enough. Larger cases can use the domain's assignment, constraint or probabilistic Methods.

Include a missed observation, new object, ended object or reused identifier when the observed situation and subject rules make that alternative live. For example, a process can terminate between reports and its number can later be reused. A fixed two-object motion exercise can instead supply persistence and complete detection as premises.

When several objects share observations, construct complete associations for the relevant group. Retain the conditions linking their choices. For independent point motions a pair of admissible paths may suffice; interacting bodies can require a joint evolution satisfying their interactions.

#### A.1.RI:4.4 - Test compatibility and the strength of the conclusion

Apply the subject constraints to each materially different connection. Construct a permitted realization where feasibility matters, or identify a violated condition that excludes it. A numerical solver can help perform this step; its returned result still needs the intended observation and subject interpretation.

Compare the surviving alternatives at the distinction required by the receiving use:

- When the supported premises and considered alternatives determine the association, use that conditional identification.
- When they exclude a proposed association, remove it from the current account.
- When materially different associations remain, retain the unresolved distinction.
- When none fits, inspect the failed observation, rule or assumption before extending the same account.

A best score answers the ranking question defined by that score. If the work uses the top-ranked association provisionally, carry its selection rule and relevant uncertainty into that use. Claiming that the observations uniquely determine it requires the corresponding exclusion of alternatives.

The strength of the identifying judgment changes with its basis.

#### A.1.RI:4.5 - Resolve only the distinction the next use needs

Try the receiving calculation or decision on the surviving alternatives. If each gives the needed result, continue with that result and leave the unused identity question open. Section :5.1 obtains the same mean position under both surviving associations.

If the difference changes the next action, determine which available fact, observation or subject constraint would distinguish the alternatives. Prefer an already available discriminator. Obtain more information when its likely contribution warrants its cost and delay; C.11.DUA supplies that choice.

Some work permits a provisional action with the unresolved risk. State what that action assumes and what observation would call for correction. Work that requires the identity to be settled must return to the missing identifying contribution. An unresolved identification need not stop other work whose result is unaffected.

#### A.1.RI:4.6 - Carry the result into use and revise it locally

Use the association to join the relevant observations, calculate the change or address the continuing object. Keep the premises and unresolved alternatives that can change that use.

Reopen the affected connection when a new observation, changed rule or detected observation error invalidates it. Preserve associations and calculations whose basis still holds. B.5.RR helps carry a changed premise through dependent reasoning.

The observations retain their own occasions and claims after their subject is identified. C.2.1 governs observation epistemes and their identities. For a use that needs a separately designated relation occurrence, apply A.6.REL using the direct relation pattern's predicate and occurrence-identity rule.

### A.1.RI:5 - Archetypal Grounding

#### A.1.RI:5.1 - Associate two moving objects and retain an unresolved alternative

Consider two persistent point objects with independent motion on one axis; their paths may cross. Each object is observed once at each end of a one-second interval. Positions are assumed known in one common frame. Initially A is at 0 cm and B at 10 cm. Later R is at 1 cm and S at 9 cm.

The motion account limits speed to 2 cm/s. Construct the complete associations:

| Association | Required displacement magnitudes | Result under the speed bound |
| --- | --- | --- |
| A to R; B to S | 1 cm each | Admissible; the two straight paths give a joint realization. |
| A to S; B to R | 9 cm each | Excluded; each exceeds the permitted displacement. |

Under these premises, R observes the continuing A and S the continuing B. A's displacement is +1 cm and B's is -1 cm.

Now allow speed up to 10 cm/s. Both associations have admissible straight paths. The observations leave A's displacement as either +1 or +9 cm; choosing the shorter path adds a preference absent from the speed-bound premise.

Suppose the next question is instead the mean position of these two objects. It was 5 cm and is still 5 cm under both associations. That calculation can proceed without another observation. If a following action must address A individually, look for a discriminator that matters to that action or use an explicitly permitted provisional association.

If the motion premise changes again to a bound below 1 cm/s, neither complete association fits. Reconsider the bound or the observation account before asserting an identification.

#### A.1.RI:5.2 - Test associations together

Keep the one-second, independent, persistent-point and complete-detection premises. Initially A is at 0 cm and B at 1 cm; later R is at 2 cm and S at 3 cm. Each displacement is at most 2 cm.

The admissible pairs are A-R, B-R and B-S. B's nearest detection is R. Assigning it first leaves A without a permitted observation. The joint association A-R with B-S satisfies every constraint and uses each later observation once. It is the only complete association under these premises.

The common Method contributes the joint comparison. The supplied motion bound and complete-detection rule determine which associations it tests. If missed or repeated detections become possible, revise those premises and reconstruct the affected alternatives.

#### A.1.RI:5.3 - Separate a process run from a reused number

An operator wants to compare resource use in two reports carrying the same process number. The object of interest is one process run. Both reports concern the same machine boot and PID naming scope; their fields are assumed to describe the indicated process consistently.

The first report gives start time 1,000 ticks after boot; the second gives 2,400 ticks. Linux exposes such a start-time field in `/proc/pid/stat`. The changed start time excludes continuation of the earlier run, despite the repeated number. Keep the two runs' resource totals separate; subtracting the earlier total from the later one would not measure one run's interval use.

If the reports contain only the number and executable name, they can fit either continuation or termination followed by reuse. An available lifecycle event may distinguish them. For ongoing supervision, a retained process reference such as a Linux PID file descriptor can make a fresh number-based inference unnecessary.

This case resolves run continuity. A question about a service continuing through replacement processes uses the service's own continuation criterion.

### A.1.RI:6 - Bias-Annotation

Under E.3's five Principle-Taxonomy lenses (Gov, Arch, Epist, Prag and Did), this Method concerns what observation and subject constraints support about an object's continuation. Its finite examples favor explicit alternatives and simple constraints. Many real tracking problems require distributions, approximate inference or decisions under unresolved identity.

The Method can be performed by people, computational agents or coordinated teams. Their observation access and ability to construct alternatives differ.

### A.1.RI:7 - Conformance Checklist

- **CC-RI-1 - Continuing object.** The subject and its applicable continuation criterion are clear enough for the requested identification.
- **CC-RI-2 - Observation basis.** Occasions, references and consequential limitations are distinguished from inferred identities.
- **CC-RI-3 - Subject premises.** Allowed changes and observation conditions support the associations being considered.
- **CC-RI-4 - Joint construction.** Connections that share observations or subject constraints are tested together.
- **CC-RI-5 - Supported result.** The conclusion distinguishes a resolved association, exclusion, retained alternatives and an account that fits none.
- **CC-RI-6 - Affordable continuation.** Additional information is sought when resolving the difference can change the receiving use enough to justify its attainable cost and delay.
- **CC-RI-7 - Local revision.** Changed observations or premises reopen their dependent connections and results.

### A.1.RI:8 - Common Anti-Patterns and How to Avoid Them

| Failure in these situations | Consequence | Repair |
| --- | --- | --- |
| Treat a reused label as uninterrupted object continuity | Resource totals or actions can be assigned to another run or object. | Apply the relevant lifecycle or continuity rule to the available observations. |
| Accept a plausible pair without its shared constraints | Another object loses its only possible observation. | Compare the complete associations that must hold together. |
| Report the best-ranked connection as the only possible one | A scoring preference becomes an unsupported identification. | Keep the ranking assumption and test alternatives when uniqueness matters. |
| Require identity resolution for an invariant aggregate | Additional observation delays a result already determined. | Evaluate the receiving quantity across the surviving associations. |
| Treat a failed model as evidence that one convenient association is true | Contradictory observations or rules remain hidden in later reasoning. | Locate the incompatible premise or observation and repair that contribution. |

### A.1.RI:9 - Consequences

The practitioner can join observations through an explicit subject construction, distinguish what has been resolved from what remains assumed, and continue calculations that are unaffected by remaining alternatives. A changed premise has a recoverable effect on the identifying result.

The Method depends on the coverage and quality of the available subject account. Constructing and comparing many alternatives can become expensive; domain algorithms and the receiving decision determine how much of that work is worthwhile.

### A.1.RI:10 - Architectural Rationale

Object continuity and observation identity answer different questions. Relating two observations to one object can be a substantive result of reasoning: a motion account connects positions, or lifecycle information distinguishes runs. The observations can retain different claims after that result is obtained.

The common construction couples three contributions: a criterion of continuation, constraints connecting observations, and a comparison of the connections relevant to use. Spatial motion supplies one realization. Lifecycle and other subject rules supply different realizations of the same Method.

A.1 supplies the general individuation question. This member develops observation-based reidentification without requiring the object to be recognized as a holon or system. C.2.1 retains the episteme questions, and C.16 supplies measurement interpretation. Their distinct results can participate in one investigation.

### A.1.RI:11 - SoTA-Echoing

**Practice question and choice.** What may observations support about the continuation of an object? Use the domain criterion and observation account to construct and compare relevant associations; retain the distinctions that change the receiving use.

**A comparison at the same finite task.** In :5.1 with the 10 cm/s bound, selecting the association with the smaller total displacement gives A-R/B-S. Comparing all admissible associations retains that candidate and A-S/B-R. Both methods can use the same four distances and supplied constraints. The selected construction additionally keeps the second complete association and its consequences. This small cost answers whether the speed-bound observations resolve the identity. The minimum-displacement choice supplies a provisional association when the practice accepts that preference; it adds an assumption that the stated motion bound did not provide. The mean-position use needs neither choice nor more observations.

**Adapt** Andrei Rodin's [*Venus Homotopically*](https://philsci-archive.pitt.edu/12116/1/vh.pdf), §§2-8: observation and a theory-supported connecting construction contribute to identification. The distinction between possible and actual trajectories motivates :4.3-4.4. Its homotopy-type interpretation is one mathematical reconstruction, while the ordinary Method uses whichever subject construction supplies the connection.

**Adapt** the explicit association operation in Bewley et al., [*Simple Online and Realtime Tracking*](https://arxiv.org/abs/1602.00763), §3.3, as a historical computational comparator. It combines predicted states, an association cost and a globally solved assignment for online tracking. The present synthesis keeps subject constraints, ranked selection and the strength of an identifying conclusion separate. SORT's benchmark results do not establish the performance of this general Method, and the finite displacement comparison above is an authored case rather than its image-overlap algorithm.

**Adopt** the relevant lifecycle meanings from the current Linux manuals for [process start time](https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html) and [PID file descriptors](https://man7.org/linux/man-pages/man2/pidfd_open.2.html) in :5.3. They supply a nonspatial continuation case and a direct-use alternative to reconstructing identity from repeated numbers.

Reopen the chosen construction when a changed subject or observation model admits a consequential omitted association, an available reference makes reconstruction unnecessary, or a cheaper procedure supplies the distinction needed for use. A new tracking algorithm's practical gains belong to its stated object, data and decision conditions.

### A.1.RI:12 - Relations

- **A.1** supplies general individuation; **A.1.SCR** can consume an identity result when system recognition is the next question.
- **C.2.1** distinguishes observation-episteme identities and the object they concern.
- **C.16.MR and C.16.IR** construct and interpret the measurement relation when indication meanings affect association.
- **A.3.3.TR and A.3.3.PI** construct permitted continuations and retain the information needed to predict them.
- **B.5.TU and B.5.TC** construct a working theory use and compare accounts when the identifying premises need that work.
- **B.5.RR** revises reasoning affected by a changed observation or premise.
- **C.11.DUA** selects worthwhile information work for the receiving decision.
- **A.6.REL** supplies occurrence individuation when a later use specifically needs a designated identifying relation.

### A.1.RI:End
