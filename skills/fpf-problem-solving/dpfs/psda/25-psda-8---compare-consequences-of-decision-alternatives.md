## PSDA.8 - Compare Consequences of Decision Alternatives

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** an **inspectable consequence comparison** for exact alternatives, affected subjects, conditions, horizon, value accounts, and evidence, including the relations that hold and those that remain unresolved.

### PSDA.8:1 - Problem frame

**Use this when** alternatives have been named or ranked but nobody can reconstruct what each would change, for whom, over what time, and under which assumptions. Also use it when a development direction looks attractive from one component's score while its service, transition, interaction, or protected-condition consequences remain absent.

Begin with one alternative and one consequence that matters. Trace the proposed change through its supported mechanism and conditions to the affected subject, then compare that same consequence for the other alternatives. The gain is a comparison that explains its result and its limits.

The governed object is the consequence comparison, not the future outcome or the authorized choice. A consequence claim may be a forecast, conditional model result, observation, or unsupported hypothesis.

**Do not use this pattern** when a current qualified comparison already covers the exact alternatives and receiving use. Use the direct domain Method for a single missing calculation or effect estimate. If the only remaining question is the authorized choice among adequate options, use `C.11` or the direct decision guidance.

### PSDA.8:2 - Problem

A rank can hide an incomplete causal story. A larger pump does not by itself establish delivered flood service. A better-trained worker does not by itself remove a queue constrained by interfaces. A stronger model benchmark does not establish reliability of the deployed service arrangement.

Even accurate separate estimates can form a false comparison. Alternatives may use different baselines, populations, operating assumptions, or horizons. Shared benefits can be counted twice, losses shifted to excluded people, and an average used to hide a tail or distributional difference. The missing work is a consequence account on a compatible basis, not merely a more sophisticated ranking algorithm.

### PSDA.8:3 - Forces

| Force | Tension |
| --- | --- |
| Common basis and real difference | Alternatives need comparable questions, while their mechanisms and affected subjects can genuinely differ. |
| Detail and affordability | Transition, distribution, and dependencies may reverse a conclusion, while exhaustive modeling can miss the decision window. |
| Multiple values and synthesis | A recipient needs a usable comparison without losing protected conditions or incompatible value accounts. |
| Prediction and evidence | A conditional model can inform a future choice without becoming an observed or causal result. |
| Precision and partiality | Numerical relations can clarify a comparison, while absent or incompatible evidence may leave no defensible total order. |

### PSDA.8:4 - Solution

Build consequence claims for the same receiving question, align only the meanings that can be aligned, apply the declared comparison rule, and return the supported relation together with uncertainty, dissent, and exact gaps.

#### PSDA.8:4.1 - Fix the comparison, not just its column names

Name the recipient question, subject or holder, current configuration, horizon, relevant affected subjects, and exact alternatives. Use `PSDA.5`'s set only as the candidate family; generation supplies no ranking. A proposal missing a decisive premise remains conditional rather than silently joining the eligible set.

Use `PSDA.6`'s value account only for this comparison. Keep its attributed values, protected conditions, scales, and unagreed trade-offs. Use `PSDA.7`'s bounded claims and discriminating questions only where their evidence concerns the same configuration and horizon.

These inputs can come from current qualified direct sources. If one is absent, stale, or incompatible, return the exact missing premise or narrow the comparison.

#### PSDA.8:4.2 - Establish consequence paths at the needed grain

For each material alternative, connect the proposed change to intermediate conditions and the consequences that the value account actually uses. Identify who or what bears each consequence, when it appears, whether it persists, and which enabling conditions it needs.

Include transition burdens, delayed effects, and shifted losses when they can alter the comparison. Distinguish the present arrangement from an empty or ideal baseline. Use `C.11.CRC` when the missing input is specifically a finite change's contribution relative to the current configuration; reuse an already adequate contribution claim rather than reconstructing it.

Direct domain models and evidence supply effect estimates and mechanisms. A causal arrow or before–after difference is not sufficient causal support; use the direct causal or field guidance for a causal claim. A qualitative pathway can still identify a missing relationship without estimating its magnitude.

Do not extend a consequence beyond its qualified horizon without a stated model and source. If a short operating horizon excludes a material long-term lock-in or displaced loss, expose the exclusion and reopen the boundary where necessary.

##### PSDA.8:4.2.1 - Construct and question a qualitative consequence network

Use this branch when the important consequences are understandable in ordinary terms but no qualified model yet connects the alternatives to them. It returns conditional consequence profiles and precise questions for investigation. It does not turn an elicited relationship into an established causal law. Reuse a sufficient domain model instead; use a quantitative or dynamic model when timing, magnitude, feedback or joint risk decides the answer.

1. **Recover the participants' reasons.** For each affected party, name the desired state, the proposed action, any required resource and the quality by which that party would judge the result. Ask both “why is this needed?” and “how could it be obtained?” Attribute each answer; a modeler's hypothesis about another person's intention stays a hypothesis. Separate a required result from a prescribed task: two ways may obtain the same result while distributing work and discretion differently.
2. **Construct explicit relationships.** Write each important arrow as a sentence. For an external provision, identify who needs what, why, who could supply it and through which work. For a necessary combination, state which conditions must hold together; for alternative means, state whether either suffices and whether both may coexist. For a quality contribution, explain how an action or intermediate condition supports or impairs that quality. Keep necessity, sufficiency and a merely favorable contribution distinct. Name the conditions and evidence or attributed judgement supporting each sentence. A plausible relationship without support remains an open relationship.
3. **Check the network before using it.** Trace each material consequence to the alternative and to the affected party's criterion. Ask the provider whether the proposed provision is possible and the affected party whether the criterion and stated effect capture their concern. Inspect missing intermediate steps, double-counted paths and contradictory accounts. Do not repair disagreement by deleting one party. If a cycle matters, bound its time steps or obtain an appropriate model; repeatedly circulating a favorable label supplies no additional evidence.
4. **Evaluate one complete alternative at a time.** Hold its configuration and initial assumptions fixed. Carry established or conditional results through necessary combinations and alternative means using their stated meanings. A necessary unfulfilled condition blocks the claimed conjunction; an unknown necessary condition leaves that conjunction unsupported unless another condition already defeats it. One sufficient supported route can establish the stated disjunction even when another route remains unknown. If no route is supported and at least one remains unknown, retain the unresolved result; if every modeled route fails, that modeled disjunction fails. Apply the same discipline to external provision: the receiver's result cannot be established through a provision whose availability is unknown. For contributions, retain the incoming supporting, opposing and unknown grounds together before judging the destination. Do not add signs, count arrows, or promote several weak claims to a strong claim merely because there are several. Distinguish no investigation, an investigated but unknown effect, and opposed grounds.
5. **Ask a question that can settle the disputed transition.** Present the affected person or qualified source with the actual incoming grounds and criterion: would these conditions suffice, only help, obstruct, or leave this outcome unresolved, and why? Record the answer, its scope and dissent. An acceptable judgement may retain a conflict or say that no conclusion is supported. If an unexpectedly favorable or unfavorable result exposes a missing condition, return to the relationship or source rather than adjust the final label to match expectations.
6. **Compare the resulting profiles.** Apply :4.3–:4.5 to the same consequences for all alternatives. Keep a supported trade-off separate from an unknown effect that could reverse it. Return the explanation paths with the profile; a diagram is optional. Mark any judgement on which the comparison depends so that the recipient can challenge it.
7. **Work backward only when the question requires it.** If the recipient asks how several desired conditions could hold together, trace their necessary conditions and candidate sufficient routes backward. Propose a combination of means, ask what incoming conditions would justify each disputed intermediate judgement, then test the whole combination forward under the same assumptions. Set aside a combination with an incompatible condition. Keep a combination with an unsupported decisive transition conditional, naming the missing relationship instead of treating missing evidence as refutation. A failed current combination is not proof that every possible design fails. Do not weaken the recipient's criterion merely to find a solution.
8. **Revise by dependence.** When a source or judgement changes, identify the changed relationship, rerun its downstream consequences for affected alternatives, and recheck the comparison. Reopen the boundary if an omitted party or consequence appears. Preserve independent claims and the earlier result with its earlier conditions.

Use ordinary prose categories appropriate to the subject. If a named language or solver is used, declare its version, propagation rules, treatment of unknown and conflicting evidence, and structural restrictions. A solver's satisfying assignment is a model result, not a commitment by participants or evidence that the arrangement will work.

For an inquiry that also needs to construct and question the underlying actors-and-goals model, [PSDA.20](36-psda-20---explore-a-situation-through-goals-and-dependencies.md) connects this branch to the inquiry's purpose, model views, explicit initial assumptions and a return from unexpected results to new source questions. Its car-park case follows a staffing conflict through a revised allocation and its limited use. The present branch supplies the consequence analysis within that larger inquiry.

#### PSDA.8:4.3 - Construct a consequence account before aggregating

Keep each alternative's material consequence profile visible. For every relied-on entry, show the relevant subject, meaning, unit or category, condition or scenario, time, source, uncertainty, and missingness. A short parallel description can suffice; use a table when it makes repeated comparisons clearer.

Separate physical or service consequences from how they are valued. A budget estimate, hours of service loss, a probability distribution, and a consent condition do not become interchangeable because they occupy adjacent columns. A lower cost can be compared directly under its scale while a disputed value trade-off remains unresolved.

Where there is a distribution, preserve its event definition and dependence on the alternative and conditions. Expected values alone are insufficient when a tail, threshold, reversibility, or distribution across affected subjects can change the decision. Where no distribution is justified, retain conditional scenarios or bounds.

A missing value is unknown, not zero or equal to the competing alternative. A qualified narrower slice remains usable only with its excluded consequences explicit.

#### PSDA.8:4.4 - Check dependencies and shared burdens

Ask whether consequences share a cause, depend on the same resource, overlap in their accounting, or change under combination. A human–tool arrangement needs a whole-arrangement result; adding a worker's effect to a tool's effect can omit coordination loss or count the same resolved case twice.

Use the dependence structure required by the selected model. Do not assume independent failures simply because separate estimates exist. Linearity can justify adding expected contributions without independence, but it does not justify duplicated quantities, unsupported causal contributions, or a joint tail probability.

Inspect whether a claimed dominance survives the common conditions. Different favorable assumptions for different alternatives produce no fair comparison. If a required correspondence or joint model is missing, keep the particular relation unresolved.

#### PSDA.8:4.5 - Apply only an admitted comparison rule

State what “better”, “equivalent”, “dominated”, or “incomparable” means for this use. A coordinatewise comparison may establish that one alternative is no worse on every included coordinate and better on at least one. That conclusion remains limited to those coordinates, conditions, and admissible alternatives; it is not an overall recommendation.

Use the current value account for any compensatory score, priority rule, threshold, or outranking Method. Do not convert ordinal judgements to arithmetic, add a hidden tie-breaker, or adopt a group average to force closure. If several value models remain admissible, show which relations hold throughout them and which depend on the model.

Use `A.19.CPM` when its profile, comparator, admissibility, and evidence conditions obtain. Its set-valued comparison outcome remains distinct from the application and evidence account, a result episteme, selection, or permission. Use the appropriate direct comparison Method otherwise.

Distinguish three important outcomes. Two alternatives can be tied under a rule, incomparable because of supported conflicting consequences, or not yet comparable because a necessary input is missing. Preserve the difference. If no candidate meets a protected condition, return that failure rather than ranking the least nonconforming candidate as acceptable.

For finite probabilistic consequences, PSDA.6:4.5.6 constructs the missing utility input from comparisons of lotteries and shows how to compare expected utilities over a compatible family. Supply this pattern's common consequence meanings and probability model to that construction. Use the scenario or noncompensatory comparison directly when it already answers the question; the probabilistic branch is not compulsory.

#### PSDA.8:4.6 - Return the relation and what would change it

State the exact alternatives and question; common basis; consequence profiles and source limits; applied rule; supported relations; material value disagreement; excluded or unresolved comparisons; and the smallest change that could invalidate the result.

`PSDA.9` may use this comparison and its evidence for the same configuration and horizon to test robustness. An authorized chooser or recommendation practitioner may use the comparison to inform their own judgement. Establish the basis for a resulting programme or WorkPlan separately, and use evidence of actual performance to support any claim about subsequent Work or its effects.

Recognition begins when a rank lacks a recoverable consequence path. Assurance requires qualified direct models, evidence, source reliance, calculation or implementation checks, and the relevant domain protections. A replayable comparison can still be empirically wrong; independent support of its premises remains necessary.

### PSDA.8:5 - Archetypal Grounding

#### PSDA.8:5.1 - A flood-service comparison with no scenario-free winner

Continue the illustrative next-season case with N, F, M, and S: continue the present arrangement, change fixed capacity, obtain a mobile reserve arrangement, or use a staged combination.

Suppose a later qualified deployment analysis now provides the previously missing conditional operating results for M. A compatible resource estimate and service model provide the following hypothetical analytical slice. Costs are incremental budget units above the common continuing baseline; service loss is hours when the specified pumping service is unavailable. Lower is preferred on both measures for this slice. No scenario probability is supplied.

| Alternative | Incremental budget units | Service-loss hours with normal access | Service-loss hours with road loss |
| --- | --- | --- | --- |
| N — continuing baseline | 0 | 7 | 11 |
| F — fixed-capacity change | 8 | 2 | 3 |
| M — mobile-reserve arrangement | 5 | 1 | 9 |
| S — staged combination | Not yet qualified | Not yet qualified | Not yet qualified |

These figures are invented to demonstrate the comparison; they are not engineering, financial, safety, or investment advice. The current sources do not establish reachable assistance or all property-loss consequences. Those value and protected-condition questions remain outside this numerical slice and can block an overall recommendation.

Under normal access, M costs less and has fewer service-loss hours than F. Under road loss, F loses fewer service hours but costs more. Thus the slice establishes no condition-independent dominance between F and M. N uses fewer incremental resources but loses more service hours; zero incremental cost does not mean that the baseline has no continuing obligations or consequences.

S is not assigned zero or dropped as an inferior candidate. Its missing whole-arrangement result is returned as a gap. The inspector can reproduce the narrower relations while seeing why neither those relations nor the table supports a complete four-candidate recommendation.

#### PSDA.8:5.2 - Compare whole development arrangements, not component scores

In the ninety-day organization case, a course assessment and an AI benchmark cannot be placed directly into one service-reliability ranking. Suppose the adviser obtains a qualified allocation and operations comparison for two whole arrangements: I, internal development with covered service duties, and H, a mixed human–tool arrangement with oversight and fallback.

The hypothetical supplier result gives ninety-day unplanned service-loss bounds of 12–18 hours for I and 8–20 hours for H, on the same service definition and operating conditions. Both retain their separately qualified resource and security conditions. No joint relation between the uncertain losses is supplied.

Those marginal bounds do not establish that H is always better, nor do they establish equality. H permits both a lower and a higher loss than I within the supplied bounds. The comparison returns an unresolved robust service ordering and asks which coordination or operating condition accounts for that difference. A joint model could provide a stronger relation, but it must be supplied rather than inferred from overlapping intervals.

The human capability result, organization-allocation result, and exact-version AI evaluation remain separate premises of that whole-arrangement comparison. No human learning effect is transferred to a model, and no model score stands for the organization's outcome.

#### PSDA.8:5.3 - Cheap non-use

A current qualified comparison already covers two replacement arrangements, their transition costs, service consequences, and the recipient's value rule. Reuse it for the authorized choice. A second consequence table with the same content adds no new result.

#### PSDA.8:5.4 - Two feasible library services with opposed and unknown effects

A library must compare two ways of giving complex reference help during the next four weeks: A, booked consultations with preparation time; B, a walk-in desk with triage. Both have qualified staffing, access and budget arrangements. Neither is excluded for infeasibility. The following observations and judgements are invented to show the method, not findings about libraries.

The reader wants a usable answer; a shift worker also needs a way to seek help without knowing next week's schedule. The librarian wants uninterrupted preparation for difficult questions. The manager needs a service whose answer quality and accessibility can both be defended. These are distinct concerns, not interchangeable satisfaction scores.

The practitioner interviews the roles separately and constructs these relationships:

| Relationship in this case | Ground and limit |
| --- | --- |
| A usable specialist answer needs the reader's question, an accessible relevant collection, and competent librarian work together. | The service definition and a sample of completed requests support this necessary combination. Availability of the collection alone does not produce an answer. |
| The librarian depends on the reader providing enough detail before preparation can start. | The reader supplies the question; the librarian explains which missing details prevent preparation. The booking confirmation itself is not that provision. |
| Booking online or through the staffed telephone can obtain a slot. | Either route suffices for reserving an available slot; they are not mutually exclusive. Neither establishes that the reader can attend. |
| Advance detail and protected preparation help answer quality under A. Walk-in interruptions under B impair preparation for difficult questions. | Librarians can identify the interrupted work in the sample. This supports the direction, not a population-wide effect size. |
| B permits a visit without a prior appointment; A requires attendance at a booked time. | The actual service rules establish this difference. Shift workers explain why the appointment condition can obstruct their access. |
| Reminders under A might improve attendance. | No evidence yet says whether these readers receive a reminder in time or can act on it. The effect is investigated but unknown. |

Now evaluate A. The necessary resources and work arrangement are supported; answer quality has favorable grounds. Telephone booking provides another way to reserve a slot. Shift workers explain that this helps booking but does not establish their ability to attend at the fixed time. The reminder effect remains unknown, so overall accessibility is unresolved.

Evaluate B on the same four-week basis. Unscheduled access is supported, while preparation for complex questions has adverse grounds. Triage may help preparation, but the librarian says it cannot remove interruptions under this staffing arrangement. The comparison consequently contains a supported trade-off plus one unresolved effect:

| Consequence | A — booked consultations | B — walk-in triage |
| --- | --- | --- |
| Preparation for difficult questions | Favorable grounds from advance detail and protected time | Adverse grounds from interruptions, not removed by triage |
| Access without a predictable schedule | Obstructed by fixed attendance; overall access unresolved | Supported by the walk-in rule within desk hours |
| Actual attendance and completed help | Reminder effect unknown | Not inferred merely from an open desk |

There is no supported overall winner. The manager cannot substitute one aggregate satisfaction label for these differences. The return identifies a discriminating question: can the shift-worker group obtain help through A when its schedule changes, and under what continuation?

Work backward from the manager's proposed joint requirement: preserve preparation and provide a route usable after a schedule change. A's telephone booking cannot by itself meet the second condition. B meets that access condition but does not preserve uninterrupted preparation. A possible combination is a booked service with a staffed same-day rescheduling route and protected preparation time. That is a new candidate, not a conclusion that A already meets both conditions. Its staffing interaction and ability to retain preparation must be checked before comparison.

Suppose a bounded trial shows that changed shifts overlap the booked appointments, preventing those readers from attending; reminders arrive after the changes, and appointments cannot be moved during the four-week service. This new ground settles one relationship: reminders do not restore access for the observed shift-worker situations. Rerun A's access branch and the joint-requirement test. Retain A's independently supported preparation advantage and B's existing profile. If access after a schedule change was declared a protected condition, A now fails that condition for this scope; if it was a negotiable value, the result is a clearer trade-off, not automatic exclusion. The trial supports neither a claim about all readers nor the untested combined candidate.

The useful result is the explained comparison, the precise failed route and the next candidate's missing premise. It is more informative than either “both are feasible” or “A scored higher”, and it does not authorize a service change.

### PSDA.8:6 - Bias-Annotation

**Scope:** consequence comparisons for bounded decision-support use. **Lenses:** **Onto/Epist** separates alternative, forecast, observation, and result; **Arch** exposes interaction and distribution; **Prag** fixes the receiving question; **Gov** preserves conditions and authority; **Did** makes the comparison replayable.

Ranking bias prefers closure over partiality. Baseline bias compares change with an empty world. Aggregation bias hides losers and shared burdens. Model precision can conceal missing applicability. Counter these by exposing consequence paths, testing the common basis, and stating the exact relation actually supported.

### PSDA.8:7 - Conformance Checklist

- [ ] Alternatives, subject, configuration, affected subjects, horizon, and receiving use are fixed for the comparison.
- [ ] Candidate, value, and uncertainty inputs are current and compatible or their gaps are returned.
- [ ] Each material consequence has a supported path, subject, timing, and uncertainty account.
- [ ] Where a qualitative network is constructed, relationships have distinct meanings and grounds; opposing and unknown evidence reaches the judgement without arithmetic cancellation.
- [ ] A backward proposal is tested forward as a whole; an unsupported transition or failed combination is not generalized to every possible design.
- [ ] Transition, interaction, shared burdens, and displaced losses are included where they can change the result.
- [ ] Measures, value transformations, protected conditions, and evidence retain their different meanings.
- [ ] Missing entries are not zero, equal, or silently favorable.
- [ ] The comparison rule and admissible operations are explicit.
- [ ] Ties, supported incomparability, and inability to compare are distinguished.
- [ ] The result states supported relations, limits, dissent, and exact reopen conditions.
- [ ] Comparison does not establish robustness, recommendation, authorization, Work, or effect.

### PSDA.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Compare a component's score with a whole arrangement's outcome. | Obtain consequence claims for the same receiving subject and use. |
| Use favorable conditions for each alternative. | Hold the comparison basis fixed or show explicit conditional branches. |
| Sum separately advertised benefits. | Recover overlap, interaction, and the qualified whole-arrangement result. |
| Treat overlapping uncertainty intervals as equality. | State what relation the bounds actually support and what joint information is missing. |
| Rank a failed protected condition by compensatory score. | Keep eligibility separate and return the failure. |
| Call an archive front a consequence comparison. | Recover the actual comparator, consequence profiles, conditions, and evidence. |

### PSDA.8:9 - Consequences

A recipient can inspect why an alternative compares favorably and exactly where that conclusion stops. Partial comparisons remain useful, and missing domain results become precise requests. The cost is explicit consequence and dependence work; focus it on distinctions that could reverse the result rather than building a maximal model.

### PSDA.8:10 - Rationale

A consequence comparison connects proposed actions to values through qualified claims about affected subjects. Keeping that chain visible prevents a ranking from silently deciding the model, value system, or protected conditions. Separate comparison and choice allow a well-supported partial answer to remain a valid result.

### PSDA.8:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should alternatives be connected to consequences? | Use explicit outcome models with the conditions and dependencies needed by the decision. | Rank isolated attributes or tool outputs without a consequence path. | **Adapt:** :4.1–:4.4 reconstruct only decision-changing consequence paths and shared burdens. The added effort is accepted when an omitted interaction could reverse the comparison; a qualified existing account is reused. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current graphical-model and uncertainty line. It does not validate a local mechanism or establish causal effects from arrows. `C.11.CRC` supplies a missing finite configuration-relative contribution, not field calculations. | Reopen when a changed configuration, mechanism, affected subject, or horizon invalidates a consequence path. |
| What comparison is justified by conflicting or incomplete values? | Use a declared preference model and preserve its partial or model-dependent relations. | Impose one total weighted rank. | **Adapt:** :4.5–:4.6 retain ties, incomparability, and missing-input distinctions. The deliberately accepted trade-off is less rhetorical decisiveness for a truthful relation. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) is a comparison candidate for alternative preference and recommendation forms. Its finite-action methods do not supply local values, probabilities, or decision authority. | Reopen if elicitation or evidence changes the admitted model set or resolves a previously missing comparison. |
| How can early qualitative consequences be constructed and questioned before a complete domain model exists? | Make the intermediate relationships and their grounds explicit, carry each alternative through them, and use attributed domain judgement where evidence does not determine the result. | Draw influence arrows, count favorable signs, or declare a complete model necessary before any useful comparison. | **Adapt:** :4.2.1 and :5.4 supply construction, questioned propagation, conditional backward exploration and local revision; no new notation or solver is required. | Horkoff and Yu's [PoEM 2009 procedure](https://www.cs.toronto.edu/~jenhork/Papers/Horkoff_PoEM_2009l.pdf) and [ER 2010 backward analysis](https://www.cs.toronto.edu/~jenhork/Papers/ER_Horkoff.pdf) are historical method anchors, not current empirical validation or iStar 2.0 semantics. Qualitative support does not establish causal magnitude, participant commitment or realized success. | Reopen when a changed relation, stakeholder judgement or domain model changes a material consequence; use a stronger model when quantitative interaction or feedback decides the answer. |
| Does generic candidate stewardship already compare the consequences? | Keep profile comparison, finite contribution, and archive/front stewardship distinct. | Treat C.18 as a general consequence-ranking Method. | **Adopt:** :4.2 and :4.5 use the exact C.11.CRC and A.19.CPM contributions when needed; the PSDA consequence account retains its field question. No archive machinery is required for a small comparison. | Current `C.18` governs generation, archive, and front objects; `A.19.CPM` governs its admitted set-valued comparison; direct domain Methods supply consequence models. Their different result boundaries defeat the broader attribution. | Reopen when the current question actually becomes archive stewardship or a direct comparison contribution changes. |

### PSDA.8:12 - Relations

- `PSDA.5` supplies the alternative family, `PSDA.6` the value and trade-off account, and `PSDA.7` bounded evidence and uncertainty claims. Each is used only under compatible subject, configuration, horizon, and receiving conditions.
- `PSDA.9` may consume the comparison's evidence to test robustness for that same use. The comparison does not entail the robustness result.
- `C.11.CRC` supplies a missing finite configuration-relative contribution claim. `A.19.CPM` supplies an admitted profile comparison only when its own conditions obtain. `C.18` retains its different archive/front and generation function.
- Direct engineering, operations, human-development, AI/model, financial, scientific, and other practices govern their own consequence and evidence results. `A.10` qualifies reliance; `A.15.9` supports a needed bounded outside contribution.
- `C.11` or the direct decision owner supplies the later choice. An unavailable, stale, or incompatible premise is replaced by a qualified direct result or remains a named gap.

### PSDA.8:End
