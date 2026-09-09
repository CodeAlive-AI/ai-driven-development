## C.11 - Decision Theory (Decsn-CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** `C.11` is the choice-calculus pattern for the moment when options already exist and the working question is which option to choose, including whether another probe is worth its cost before commitment.

### C.11:1 - Problem frame

**When ongoing Work still needs a next action.** If admissible actions still have to be recovered from ongoing Work, its domain Method, and current facts, use `A.15.7` first. Return here only when a current chooser and `OptionSet` exist and comparison can change the result; a mandatory response or one familiar cue need not be inflated into an option set.


**Use this when.** Use this pattern when one `DecisionSubject` already has an `OptionSet` in hand and the real question is how to choose among those already-available options under uncertainty, preference, causal or subjunctive dependence, and bounded probing or computation.

**Start here when.** Start here when a person, team, organization, or other decision-capable system must decide whether to choose now or spend more effort on probing, information gathering, or computation before choosing.

**First output.** The first useful output is one explicit `DecisionSubject`, one explicit `OptionSet`, one explicit comparison basis, one explicit `ChoiceRule`, and one explicit `ChoiceResult` saying whether the lawful choice result is choose now, reject the current set, probe more, or move to a neighboring question.

If that first output still cannot be stated, the local comparison is unfinished or the question belongs to a neighboring pattern.

**Immediate failure indicators.**

- The chooser is still moving between person, team, organization, or another collectivity-bearing level.
- The current comparison is still inventing, expanding, or reframing options while also claiming to compare them.
- The current comparison says more information would help but cannot name one next probe that could still change the result.
- The current result is really surfacing one selected set or one enactment plan rather than one local choice.

**First-minute questions.**

- Who or what is actually choosing here, and at what chooser-bearing level?
- What options are already on the table now?
- What current basis is being used to compare them?
- What next probe could still change the choice, if any?
- Is this still local choice, or has the question moved to a neighboring problem—for example, search, pool policy, selector-result declaration, publication availability, or enactment?

**When advice still hides the decision.** Use `C.11.DUA` when a recommendation or evidence demand still needs its receiving question, demanded work or requirement merits recovered. Return here when a current chooser and options support a local choice. An already adequate choice uses this pattern directly.

**Typical reroutes.** `C.38` when labels or fragments still need to become complete ways of obtaining the same result; `C.18` when the real question is open-ended invention or reframing; `C.19` when the working question is how broadly to explore or exploit the candidate pool; `C.24` when one option is already chosen and the work has become sequencing or enactment; `A.13` when the hard question is agenthood rather than choice; `A.18` for Scale and Coordinate bindings or `A.19` for a declared CharacteristicSpace or reusable predicate when that support question itself becomes primary.

**Common neighboring-pattern mistakes.** Do not use `C.11` to hide search work inside "decision", to hide candidate-pool policy inside one local choice, or to hide execution planning inside one generic rationality account. Do not treat declaring selector-facing set-result content, or later making that result available, as if either were the same question as deciding.

**What goes wrong if this pattern is missed.** Search, selection policy, planning, and choice doctrine collapse into one blurred notion of rationality. Teams either choose too early because pool policy was never stated, keep probing without one reason the next probe is still worth its cost, or leave only one vague claim that "a decision was made" without one explicit decision record naming the current result.

**What this pattern buys.** This pattern gives one stable place to compare classical, causal, success-first or subjunctive, bounded-resource, active-inference-adjacent, and quantum-like decision lines without silently reassigning search, selection, or planning doctrine to the wrong question. In practice it buys one explicit answer to four questions: choose now, reject the current set, probe again, or reroute.

**Not this pattern when.** Do not start here when the current question is still generating candidate options, setting exploration or exploitation policy over a candidate pool, declaring selector-facing set-result content, making that result available to an audience, or sequencing execution under an operational plan.

Decision work often fails not because no options exist, but because the choice among existing options is never typed as its own question. `C.11` starts from one narrower and more useful center: one decision subject choosing among already-available options, including whether more probing is worth the cost before the choice is fixed.

### C.11:2 - Problem

Many systems have options on the table but still lack one explicit doctrine for what makes one option rational to choose. They mix together at least four different questions.

One question is still generating candidate options, variants, or open-ended search directions. Another question is governing how broadly a candidate pool should be explored or exploited before narrowing. A third question is planning, sequencing, replanning, or enacting the chosen option once a choice has already been made. The fourth question, and the one governed here, is choosing among already-available options under uncertainty, dependence, and bounded deliberation.

A second distortion appears when decision theory is reduced to one thin slogan about expected utility. Real choosers face evidential and causal distinctions, subjunctive or success-first cases, probe costs, information value, computation value, and situations where the chooser is not just one isolated individual.

Without one explicit place for choice calculus, search, candidate-pool policy, and planning rush into the same question, while the actual doctrine of choosing among live options disappears behind generic talk about rationality.

### C.11:3 - Forces

| Force | Tension |
| --- | --- |
| Choice doctrine versus candidate formation and generation | `C.11` must govern choice among already-available options without swallowing `C.38` formation of complete ways or `C.18` open-ended search and generation. |
| Evidential, causal, and subjunctive dependence | The pattern must stay usable with classical decision language while making room for causal and success-first repairs where correlation is not enough. |
| Decide now versus probe more | The chooser may need to stop and choose now, or spend more effort on information and computation first. The theory must make that trade legible. |
| Decision subject versus narrower agent language | The chooser may be one person, one team, one organization, or another collectivity-bearing system. The pattern must not silently force all cases into one narrow `Agent` reading. |
| Minimal mathematical floor versus premature heavy formalism | The pattern needs a stable object stack for disciplined reasoning and inspection, but it should not pretend that one full quantum-like or geometry-heavy package is already settled. |

### C.11:4 - Solution
#### C.11:4.1a - Causal-use hook for choice records

When a choice depends on an effect, intervention, counterfactual, causal-policy, or off-policy claim, the `ChoiceResult` keeps the decision question local and cites the C.28 support result as one basis.

```text
ChoiceResult.causalUseSpec?:
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalSupportComponentRefs?: CausalSupportComponentRefs
  causalUseEvidenceDesignRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  supportedUse
  unsupportedUse
```

Omit the tail when causal support changes neither the comparison nor the chosen result. If causal wording changes the result, include the tail or downgrade the wording. A C.28 result does not choose, permit, or deploy an option; C.11 uses it with the other decision premises and may still select, defer, or abstain.

#### C.11:4.1 - Primary EntityOfConcern and admissible choice result

`C.11` governs theory-side choice among already-available options. Its selected decision result states what should be chosen from the current `OptionSet`, including whether further probing, information gathering, or computation is rational before the choice is fixed.

The OptionSet choice question begins only after an option set already exists. It does not form complete ways of obtaining one result, govern open-ended generation of options, or govern the execution order of a plan after a choice has already been made.

#### C.11:4.2 - Decision discipline over a live option set

A conforming `C.11` pass does not stop at naming schools of decision theory. It carries one usable choice discipline over a live `OptionSet`, and it ends with one explicit `ChoiceResult` under one explicit `ChoiceRule`.

1. **Fix the chooser and the choice-bearing level.**
   State one `DecisionSubject` and one `DecisionSubjectGranularity`.
   If the real dispute is still about who or what counts as the chooser, coordinate with `A.13` instead of hiding that dispute inside one local choice.

2. **Freeze the current option set.**
   State the already-available options being compared now as one `OptionSet`.
   If the rows are only labels or fragments and the question is several complete ways to obtain the same result, stop here and apply `C.38`. If the hard work is open-ended invention, expansion, or reframing, apply `C.18`.

3. **Make the comparison basis explicit.**
   State one `PreferenceOrder` or one `EvaluativeMeasure`, plus one `BeliefState` and one `OutcomeModel`.
   The comparison is not usable if some options are being judged under one belief state and other options under one later, unmarked update.
   If two options are only comparable after one further probe or one model revision that changes the belief state or outcome model before comparison, say that the current comparison is unfinished and apply step 5 rather than pretending that one silent basis shift already solved it.

4. **Choose the dependence layer that actually governs the case.**
   Start from the evidential baseline when the choice is being compared through likely outcomes under the current `BeliefState`.
   Add one `InterventionModel` when taking one option changes the world through intervention rather than mere observation.
   Add one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when the case depends on one predictor, one structurally linked chooser, or one decision-procedure coupling that intervention talk alone does not capture.
   Use the least-committing dependence layer that still covers the live case, and do not switch layers across options without saying so explicitly.

5. **Compare a live inquiry alternative before commitment.**
   An inquiry alternative is live when a current proposal, consequential uncertainty, anomaly or applicable requirement supplies a plausible way for further information or computation to change this choice or its warranted use.
   Apply the probe-worthiness test to that alternative, stating the feasible probe, budget, cost and relevant information or computation value at the precision the choice needs. Otherwise this step adds no investigation or recording requirement. An empty form field does not activate inquiry, and no new search is required to certify that no other inquiry exists.
   This rule is intentionally local or myopic: it judges the best next feasible probe over the current `OptionSet` and current comparison basis, not one full sequential or non-myopic experimental program. Richer `OED` lines may strengthen this doctrine, but the local `C.11` closure rule already has to decide whether the next feasible probe can still change the current choice.
   If no feasible further probe fits the remaining `ProbeBudget`, or if the best available probe no longer justifies its `CostToProbe`, close under the current comparison basis.
   If a feasible probe is still worth its cost, and that probe could still change which option survives or whether the current `OptionSet` should be rejected, run it, update the `BeliefState` and `OutcomeModel`, and return to step 3.
   If one choice result is already fixed and the remaining probe would change only execution-path description, call-plan ordering, enactment budget, or checkpointing of that chosen option, stop treating the probe as local choice doctrine and apply `C.24`.

6. **Apply one `ChoiceRule` and emit one `ChoiceResult` plus the next question.**
   End with one explicit result: `choose now`, `reject current set`, `probe again`, or `reroute because this is no longer local choice`.
   If the result is `choose now`, name the selected option or retained tie-set and the comparison basis supporting it; add the outcome of a live inquiry comparison or a limitation needed by the decision or its recipient.
   If the result is `reject current set`, name the reason no current option survives under the present basis and, when more work follows, the neighboring question that now takes over.
   If the result is `probe again`, name the next probe and the exact comparison defect it is supposed to repair.
   A `C.11` pass is done only when it names the lawful choice result and the reason that result is lawful.

#### C.11:4.2a - Receive heterogeneous premises without relabeling them as signals

An interesting observation, information-gain estimate, capability result, objective or reward, articulated former cue, or `C.17` characterization enters this pattern only under its exact source/result identity. Use `E.10.LRN` first when *learning* wording still hides that identity. Use `A.10` when an evidence-bearing or source-bearing claim is actually relied on: its existing `RelianceDisposition` qualifies only that bounded premise use. An objective, reward, preference, or loss enters as the `EvaluativeMeasure`, `PreferenceOrder`, or `ChoiceRule` input it actually supplies and is not evidence by numerical form. When an `A.16.1` cue pack remains current as a source or provenance episteme, preserve that source identity and route the separately articulated endpoint result through its direct claim owner. A `C.17` novelty, surprise, use, or creativity characterization remains a characterization and does not license a move by itself.

No separate premise-qualification result sits between those owners and `C.11`. Use the qualified inputs in the live option/probe comparison and return only the existing `ChoiceResult`. When the missing comparison basis is specifically what a finite candidate contributes relative to the current configuration, use `C.11.CRC` to construct that ordinary comparison claim and return here. If every premise and the finite comparison are already explicit, proceed directly.

#### C.11:4.2.1 - Well-formed comparison state


Well-formedness constraint: a live `C.11` comparison state is usable only when the decision record states the following, subject to the stated condition on inquiry:

- one `DecisionSubject` at one `DecisionSubjectGranularity`;
- one current `OptionSet`;
- one current comparison basis through `PreferenceOrder` or `EvaluativeMeasure`, plus one `BeliefState` and one `OutcomeModel`;
- one active dependence layer for the current comparison, unless the record explicitly says that comparison is still being reopened;
- when an inquiry alternative is live, an account of its feasibility, cost and possible contribution to the choice; when a decision or later use needs a retained inquiry limitation or reason, that minimum content in the same decision result.

An inactive inquiry item requires no empty value, no no-probe statement and no waiver. The chooser, option set, shared comparison basis and applicable dependence layer remain necessary.

The comparison is still unfinished, not yet wrong but not yet closeable, when any of the following remains true:

- the chooser is still shifting between person, team, organization, or another collectivity-bearing level;
- the option set is still changing while the record also claims to rank the options;
- one option is being judged under one belief state and another under one later update that is not itself declared as the next probe result;
- one heavier dependence layer is invoked for rhetorical force, but the record never states what defect of the lighter comparison it repairs;
- the record says more information would help, but never says which probe could still change the choice and why.

#### C.11:4.2.1a - Minimal admissible decision semantics

This minimal choice doctrine does not settle every decision-theory dispute, but it already supports some semantic distinctions by value and rules out others.

The following are lawful in this `C.11` body when they are stated explicitly:

- one incomplete or only partially ordered `PreferenceOrder`, so long as the unresolved comparison stays visible through one retained tie-set, one further probe, or one honest `reject current set` result rather than one fake winner;
- one `EvaluativeMeasure` for magnitude, threshold, or trade-off-sensitive cases, so long as the measure being used now is explicit enough to explain why the current result follows under it;
- one temporary unresolved criterion conflict, so long as the record says whether the present comparison is using one priority order, one threshold, one explicit trade-off measure, or one unfinished state that still blocks closure;
- one explicit `BeliefState` revision, so long as it enters the comparison as one named probe result or one named model repair rather than as one silent basis shift;
- one widened `DecisionSubject` at person, team, organization, or other collectivity-bearing level, so long as the current subject-bearing level is explicit and the record does not hide unresolved cross-scale or cross-collective conflict behind one generic chooser label.

The following are not admissible in this `C.11` body:

- silently totalizing one genuinely partial preference relation just to force `choose now`;
- silently switching from one criterion mix or one belief state to another across options;
- pretending that unresolved cross-scale or cross-collectivity conflict is already one settled local ranking when the aggregation question has not actually been discharged;
- using one polished record shape as a substitute for one stated comparison doctrine.

This is why `C.11` is more than one note-taking protocol. The body already supports local incompleteness, partial order, explicit trade-off measures, and wider chooser-bearing cases, but it requires those semantic facts to change the lawful result rather than remain hidden beneath one elegant summary line.

#### C.11:4.2.2 - Probe-worthiness rule

Another probe is worth doing only when all three conditions hold together:

- the probe fits inside the remaining `ProbeBudget`;
- the expected gain from the probe, through `ValueOfInformation` or `ValueOfComputation`, is large enough to justify its `CostToProbe`;
- the probe can actually change the local choice result by changing the ranking, breaking or creating a tie, showing that no current option survives, repairing one missing comparison, or showing that the question should reroute.

This is the current local or myopic probe-worthiness rule for `C.11`: judge the best next feasible probe over the current `OptionSet`, not one whole non-myopic experiment design over longer horizons. Later sequential or non-myopic `OED` may strengthen this doctrine, but they do not relocate the local-choice question outside `C.11`.

Do not keep probing merely because uncertainty remains. Uncertainty is ordinary. What matters is whether one feasible next probe can still change what should be chosen, or whether the current `OptionSet` should be rejected, from the current local choice question.

If the best available next probe cannot change the local choice result, or its expected gain cannot justify its cost, state one explicit `ChoiceResult` under the current basis and current `ChoiceRule`.

If the next probe would no longer change which option survives but would only change how one already-chosen option gets enacted, budgeted, or checkpointed, the question has already crossed to `C.24`.

#### C.11:4.2.3 - `ChoiceRule` versus `ChoiceResult`

`ChoiceRule` and `ChoiceResult` are not the same kind of thing.

- `ChoiceRule` is the doctrine or operator that says how the current comparison basis, dependence layer, and any applicable probe-worthiness value support one `ChoiceResult`.
- `ChoiceResult` is the emitted record stating which choice result is lawful now under that rule.

The operational answer of this pattern is therefore one emitted `ChoiceResult` under one explicit `ChoiceRule`. The result is complete only when it states the choice result and the condition that makes that result lawful.

Only four result forms are lawful here:

- `choose now`
- `reject current set`
- `probe again`
- `reroute`

A fifth soft result such as "keep thinking", "stay with the current view", or "the case is still complex" is not a conforming output. It is one unfinished state that still needs to be typed.

For `choose now`, the emitted `ChoiceResult` should show:

- the selected option or retained tie-set and the comparison basis supporting it;
- the outcome of a live inquiry comparison or a limitation needed by the decision or its recipient, when applicable.

For `reject current set`, the emitted `ChoiceResult` should show:

- that no member of the current `OptionSet` survives under the present comparison basis;
- the exact shared defect, threshold failure, or dominated-outcome reason that defeats the current set;
- the next neighboring question only when more work now follows, such as new option generation or one explicit escalation path.

For `probe again`, the emitted `ChoiceResult` should show:

- the exact next probe;
- the comparison defect that probe is expected to repair;
- the reason the probe is still worth its cost.

For `reroute`, the emitted `ChoiceResult` should show:

- the neighboring question and the pattern used to answer it;
- the reason this is no longer local choice among already-available options.

#### C.11:4.2.4 - Closure rule over the current `OptionSet`

The comparison may close as `choose now` only when all of the following are true together:

- the current `OptionSet` is stable enough that no further options are being invented for this comparison;
- the current comparison basis is explicit enough to state why one option survives or why one tie-set remains;
- no still-feasible next probe is expected to change the survivor relation with enough expected value to justify its cost;
- the record still concerns local choice rather than pool policy, selector-result declaration, publication availability, or enactment.

The comparison may close as `reject current set` only when all of the following are true together:

- the current `OptionSet` is explicit and stable enough to reject as the present choice set;
- the current comparison basis is explicit enough to show why no member survives under the present basis;
- no still-feasible next probe is expected to rescue one member with enough expected value to justify its cost;
- the result is still one local choice conclusion rather than one disguised pool-policy, selector-result declaration, publication-availability, or enactment result.

Assess the probe conditions above from the current basis and any live inquiry alternative. They are conditions of a warranted choice, not a requirement to produce a separate account of omitted checking.

The comparison should close as `probe again` only when all of the following are true together:

- one next probe is named by value;
- that probe fits the remaining `ProbeBudget`;
- that probe is expected to repair one named comparison defect;
- that repaired defect could still change which option survives, whether the current set should be rejected, or whether the question should reroute.

The comparison should close as `reroute` when the record shows that the decision question has changed:

- to `C.38` when labels or fragments must first become complete-enough ways of obtaining the same result;
- to `C.18` when the option set itself is under open-ended invention or reframing;
- to `C.19` when the question is now how broadly to keep exploring or exploiting one candidate pool;
- to `C.24` when one choice result already exists and the next task is now sequencing, enactment, or execution-path probe work;
- to `G.5` when the next task is declaring or naming selector-facing selected-set content; when that result already exists, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and audience availability.

If none of those closure conditions can yet be satisfied, the record is still unfinished. It is not rescued by richer terminology alone.

#### C.11:4.2.5 - Minimal decision-record form

A minimal `C.11` decision record has the shape below. Include `ProbeDecisionValue` only for a live inquiry alternative or an inquiry judgement whose content the decision or recipient needs. Include only the relevant information or computation value. A retained prose reason or limitation alone does not activate that block: put only the needed statement in `ChoiceResult`.

```text
DecisionSubject(...)
DecisionSubjectGranularity(...)
OptionSet(...)
ComparisonBasis(
  preferenceOrder or evaluativeMeasure,
  beliefState,
  outcomeModel,
  optional intervention/counterfactual/subjunctive layer
)
ChoiceRule(
  closure rule over the current basis and any applicable probe decision value
)
ProbeDecisionValue(  # conditional as described above
  probeActionSet,
  probeBudget,
  costToProbe,
  relevant valueOfInformation or valueOfComputation or both
)
ChoiceResult(
  choiceDisposition = choose_now | reject_current_set | probe_again | reroute,
  selectedOption or retainedTieSet or rejectedCurrentSet or rerouteOwner,
  reason this result is lawful now
)
```

Exact syntax is unnecessary. The chooser, options, shared comparison basis, `ChoiceRule` and `ChoiceResult` are required. Inquiry content is required only under the stated condition; an absent block requires no placeholder or omission explanation.

Use branch language only when it changes the actual comparison being performed.

#### C.11:4.2.6 - Resource-aware choice is one lens over declared source families

- Start from one declared source family or one declared source-family composition such as `Front`, `Archive`, or `Front+Archive`.
- Apply one declared decision lens over that source family rather than inventing one hidden universal winner rule.
- `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` belong to that lens-side choice doctrine.
- They may justify another probe, one changed local comparison outcome, or one stop decision, but they do not rename the current `DominanceSet` and do not declare one shortlist-family result.
- If one candidate remains worth probing because its expected information value still exceeds its expected cost, say that explicitly as one lens-side choice judgement.
- If one archive point remains worth probing because it may change the frontier later, keep that as one resource-aware choice claim, not as evidence that the point is already on the current front.
- The kernel floor here is:
  - `A.19.SelectorMechanism` remains the cited set-return floor
  - `SelectionSlot` remains the selector output floor
  - if later selector-facing set-result declaration is required, that set-returning floor may support one `Shortlist` or one `RankedShortlist` in `G.5` rather than one forced single winner

##### C.11:4.3.1 - Classical evidential baseline

Stay with the classical evidential baseline when the question is to compare already-available options through preferences, utilities or desirabilities, beliefs, and likely outcomes under uncertainty.

In this baseline, the options are being compared as evidence about what consequences are likely if they are chosen. This is the ordinary default when intervention structure, predictor-coupling, or context-sensitive non-commutativity are not yet doing real work in the case.

Typical practical cash-outs are:

- `choose now` because the current shared `BeliefState` and `OutcomeModel` already make one option or tie-set survive, and no still-feasible probe is worth its cost;
- `probe again` because one further observation, measurement, or comparison pass could still change the ranking without requiring a heavier causal, subjunctive, or context-order repair;
- `reroute` because the current decision question is no longer really comparing one fixed `OptionSet`, but has become search, pool policy, selector-result declaration, publication-availability, or enactment work.

The baseline is still unfinished when the current comparison invokes it but cannot keep one shared `BeliefState` and `OutcomeModel` across the compared options, or when one heavier defect is already live and the current comparison still pretends one plain evidential comparison is enough.

##### C.11:4.3.2 - Causal repair

Switch on one `InterventionModel` when taking one option changes the world through intervention rather than merely signaling which outcome was already likely.

What changes here is not the prestige label of the theory line, but the comparative question itself: the working question is no longer only what this option indicates about the outcome, but what this option causes in the outcome structure.

Typical practical cash-outs are:

- `choose now` because, under the declared intervention structure, one option now causally dominates or remains the survivor and no remaining feasible probe can reverse that causal ranking;
- `probe again` because one intervention-relevant uncertainty still blocks a lawful causal comparison and one named next probe could still change which option causally survives;
- `reroute` because the intervention-use question has already moved from local choice into enactment planning, protocol design, or one neighboring question.

The causal repair is incomplete if the comparison still treats options only as evidence after invoking causal language, or if an `InterventionModel` is named without stating what defect of the lighter evidential comparison it repairs.

##### C.11:4.3.3 - Success-first or subjunctive repair

Switch on one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when Newcomb-like, blackmail-like, or other predictor-coupled cases remain under-described by the older evidential-versus-causal split.

What changes here is that the comparison must stay answerable to linked decision procedures, predictors, or structurally similar choosers rather than only to direct intervention on one local event.

Typical practical cash-outs are:

- `choose now` because, under the declared counterfactual or subjunctive structure, one option survives once the predictor-coupled comparison is made explicit;
- `probe again` because one further model clarification, predictor assumption check, or decision-procedure comparison could still reverse the current survivor relation;
- `reroute` because the governing decision question is no longer settling local choice doctrine but has become one wider characterization, negotiation, or enactment question that only borrowed predictor-coupling language.

If that coupled structure is not live, do not activate this branch. If a predictor-coupled or success-first repair is named but the linked structure that changes the comparison is still unspecified, the branch is not yet load-bearing in the current decision.

##### C.11:4.3.4 - Active-inference neighboring repair

Bring the active-inference line into view when the chooser is embodied, online, and socially coupled, and when the decision cannot be understood as one disembodied choose-then-act moment.

What changes here is practical choice logic, not one neighboring-school label. The comparison is no longer over one frozen snapshot alone. The comparison must now ask whether one more observation, one more coupled update, or one more socially mediated or role-expectation clarification actually changes what should be done now.

This minimal choice doctrine makes that social-expectation pressure explicit, but it does not yet operationalize one full `ROE` or `SocialExpectationRegime` object model inside `C.11`. If that heavier machinery is itself what the case hinges on, the decision record should say so honestly rather than pretending the local `C.11` floor has already settled it.

Typical practical cash-outs are:

- `probe again` because one further embodied observation, coupled update, or explicit role-expectation clarification can still change the state estimate enough to reverse the current survivor relation;
- `choose now` because delay itself now worsens the state being managed, closes the window in which the preferred option remains feasible, or leaves no lawful time for one more socially mediated check;
- `reroute` because the question has already become enactment sequencing or agent-characterization work rather than local choice.

`C.11` keeps the choice question visible there, but `A.13` still governs the narrower question of what kind of agent or agential system is in play. For measured characteristic and evidence claims, use `A.17` for Characteristic identity and arity, `A.18` for Scale and Coordinate bindings, `A.19` for the declared space and reusable predicate, `C.16` for the measurement account, and `A.10` for bounded reliance on the evidence. `C.24` still governs sequencing and enactment once a choice result has already been fixed.

Do not invoke this line only because one agent is acting in the world. Invoke it when embodied coupling, online updating, or explicit social-expectation pressure actually changes what the chooser should do now from the current `OptionSet`.

##### C.11:4.3.5 - Quantum-like neighboring repair

Bring the quantum-like line into view when context effects, order effects, response-replicability tension, or incompatible-question structure change the comparative state enough that one simple commutative probability reading no longer fits.

What changes here is the practical structure of comparison. One order of questioning or one framing path may produce one different survivor relation from another. The comparison must therefore either stabilize the comparison under one declared order or show why one more clarifying pass is still needed.

This minimal choice doctrine keeps the branch at that measurement-sensitive recognition point. It does not yet claim one full quantum-like state-space package inside `C.11`; it claims only that the live comparison may need one explicit measurement-class or order-sensitive repair rather than one plain commutative reading.

Typical practical cash-outs are:

- `choose now` under one declared order or framing because rival orders no longer change which option survives;
- `probe again` because one framing-sensitive comparison pass, one further question order, one response-replicability check, or one explicit measurement-class clarification could still reverse the survivor relation;
- `reroute` when the current decision question is no longer deciding among live options but has become one selector-result declaration, publication-availability, or enactment problem that only borrowed order-effect language rhetorically.

Do not promote this line to the unmarked default unless those repaired limitations are live in the case.

Do not invoke this line merely because a case feels psychologically subtle. Invoke it when one changed order, framing, response pattern, or incompatible-question structure actually changes the comparison state or the survivor relation in the live choice.

If no causal, subjunctive, active-inference, or quantum-like refinement is needed for a live limitation, stay with the classical evidential baseline.

The family map is therefore one disciplined set of refinements over the same choice question, not one excuse to rename every neighboring question as decision theory.
#### C.11:4.4 - Reroute as soon as the question stops being local choice

Use `C.11` while the question remains: from this current `OptionSet`, what should the `DecisionSubject` choose, and is another probe worth its cost before commitment?

Reroute immediately when the question changes:

- If the current rows are labels or fragments and the hard question is how several complete ways could obtain the same result, leave this pattern and work in `C.38` first.
- If the hard question is still what options should exist at all, or whether the current option set needs open-ended expansion or reframing, leave this pattern and work in `C.18` first.
- If the options already exist but the question is how broadly to keep exploring or exploiting the candidate pool, leave this pattern and work in `C.19`, where the next useful output is one explicit pool-policy result rather than one local `ChoiceResult`.
- If one option is already chosen and the question is how to sequence, budget, or enact that choice, leave this pattern and work in `C.24`, where the next useful output is one enactment-facing call plan or `CheckpointReturn`.
- If the question has shifted from deciding to declaring or naming selector-facing selected-set content, leave this pattern and work in `G.5`. Its next useful output may be a `Shortlist` or `RankedShortlist` when alternatives remain for later choice, a `JointUseSet` when every named member is included for one bounded use, a narrowed handoff, abstain, or escalation. None is one more local `ChoiceResult`. If that result already exists and the current question is presentation or availability to an audience, use `E.17` for the source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

`ProbeBudget` stays here while it means the epistemic or deliberative budget for one more probe before choice and while that probe can still change which option survives or whether the current set should be rejected. When the same word now means execution budget, call budget, enactment budget, or execution-path scouting after one choice result already exists, the question has moved to `C.24`.

`ValueOfInformation` and `ValueOfComputation` also stay theory-side here as comparative criteria while the question is still local choice among the current options. If one more probe could still change which option survives or whether the current set should be rejected, stay in `C.11`. If the choice result is already fixed and those criteria now govern only execution-path sequencing, call-plan ordering, or enactment of the chosen option, the question has crossed to `C.24`. `C.19` and `C.24` may consume the criteria, but they do not become the doctrine authorities for them.

Outside this pattern remain candidate generation, pool-wide exploration policy, selector-facing set-result declaration, publication availability, and execution planning.

#### C.11:4.5 - Minimal inventory and mathematical floor

The minimum usable inventory for this pattern is:

- subject and option objects: `DecisionSubject`, `DecisionSubjectGranularity`, `OptionSet`;
- evaluative and epistemic objects: `PreferenceOrder`, `EvaluativeMeasure`, `BeliefState`, `OutcomeModel`;
- dependence and comparison objects: `InterventionModel`, `CounterfactualModel`, `SubjunctiveDependenceRelation`, `ChoiceRule`, `ChoiceResult`;
- probe and bounded-resource objects: `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`.

The applicable objects from this inventory are required because the decision record must carry one explicit path from a live `OptionSet` through one live `ChoiceRule` to one emitted `ChoiceResult`.

#### C.11:4.5.1 - Always explicit versus conditionally activated objects

The following objects should be explicit in every usable `C.11` decision record:

- `DecisionSubject` and `DecisionSubjectGranularity`;
- `OptionSet`;
- one evaluative basis through `PreferenceOrder` or `EvaluativeMeasure`;
- `BeliefState`;
- `OutcomeModel`;
- `ChoiceRule`;
- `ChoiceResult`.

The following objects activate when the case needs them:

- `InterventionModel` for causal repair;
- `CounterfactualModel` plus `SubjunctiveDependenceRelation` for success-first or predictor-coupled repair;
- `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` when one more probe or one more computation pass is still live.

What matters is not that every decision record mechanically mentions every token. What matters is that the current comparison does not smuggle one active question without naming the object that carries it.

Immediate lexical commitments:

- the default chooser term is `DecisionSubject`, not `Agent`;
- `DecisionSubjectGranularity` names the chooser-bearing level when the question is about whether the chooser is one person, team, organization, or another collectivity-bearing system rather than one generic scalar or coordinate;
- relation-heavy wording remains answerable to `A.6.P` together with `A.6.5`.

Local plain glosses for the load-bearing inventory:

- `DecisionSubject`: who or what is actually carrying this choice now, whether that is one person, one team, one committee, one organization, or another collectivity-bearing system;
- `DecisionSubjectGranularity`: the level at which the choice is being attributed, such as person-level, team-level, or organization-level rather than one vague "agent" label;
- `OptionSet`: the concrete options already on the table now;
- `PreferenceOrder`: the current better-than / worse-than ordering over those options for this decision subject;
- `EvaluativeMeasure`: the explicit utility-style or desirability-style scoring measure used when the case needs magnitudes, thresholds, or trade-offs rather than only one ordering;
- `BeliefState`: the current uncertainty-bearing state about the world, the case, and the likely consequences of the options;
- `OutcomeModel`: the model that maps options plus the current uncertainty picture to the consequences that matter for this choice;
- `InterventionModel`: the part of the model that says how the world changes because one option is actually taken;
- `CounterfactualModel`: the model used to compare relevant non-actual alternatives or alternate decision procedures;
- `SubjunctiveDependenceRelation`: the dependence between this choice and one predictor, one linked chooser, or one structurally similar decision procedure when intervention talk alone is not enough;
- `ChoiceRule`: the current choice doctrine or operator that says what conditions make `choose now`, `reject current set`, `probe again`, or `reroute` lawful in this case;
- `ChoiceResult`: the emitted result record saying which of those lawful choice results actually follows now under the current `ChoiceRule`;
- `ProbeActionSet`: the further checks, measurements, simulations, or questions that can still be run before commitment;
- `ProbeBudget`: the remaining time, money, attention, or tolerated delay available for those pre-choice probes;
- `CostToProbe`: the real cost of another measurement, question, simulation, trial, or delay before commitment;
- `ValueOfInformation`: the expected gain from learning more before choosing;
- `ValueOfComputation`: the expected gain from spending more reasoning or compute before choosing.

What follows from `DecisionSubject` being wider than `Agent`:

- the chooser in `C.11` need not be one person-like agent;
- a team, committee, organization, or coupled human-tool system may be the `DecisionSubject` when that is the real level at which the choice is being made;
- the pattern therefore does not force agency characterization to do the job of naming who or what is currently choosing.

This floor is enough to keep choice doctrine inspectable and stable. It does not yet assume one full branch-specific quantum-like package or one cross-scale geometry-heavy package.

#### C.11:4.5.2 - Boundary on multilevel and social-expectation doctrine

`DecisionSubject` and `DecisionSubjectGranularity` are the local answer to human-only and individual-only narrowing. They keep the chooser explicit at person, team, organization, or other collectivity-bearing level so the doctrine does not silently collapse back into one generic individual agent.

This minimal choice doctrine does not yet settle all of the heavier doctrine that can sit behind that wider chooser-bearing scope. In particular, this body does not yet fully settle:

- collective aggregation doctrine over conflicting preferences or criteria;
- cross-scale or cross-collective conflict between person-, team-, organization-, or broader system-level objectives;
- one full `ROE` or social-expectation structure for socially scaffolded choice;
- one full multilevel or geometry-heavy formal package for those cross-scale or cross-collective questions.

Those absences are not hidden exceptions. They are explicit scope boundaries of this `C.11` body. If one of those heavier questions is already live in the case, the decision record should say that the local `C.11` floor is being used only as the current typed floor and should keep the unresolved aggregation, `ROE`, or multilevel support question visible by value.

#### C.11:4.6 - Minimal decision tuple and finish condition

A `C.11` decision record is complete only when it states:

- who or what is choosing: `DecisionSubject` at one `DecisionSubjectGranularity`;
- what is currently choosable: `OptionSet`;
- how the options are compared: `PreferenceOrder` or `EvaluativeMeasure`, plus `BeliefState` and `OutcomeModel`;
- which heavier dependence layer is active when the case needs it: `InterventionModel` for causal repair, or `CounterfactualModel` plus `SubjunctiveDependenceRelation` for success-first or predictor-coupled repair;
- what comparison doctrine currently governs the case: one explicit `ChoiceRule`;
- when an inquiry alternative is live, an account of its feasibility, cost and possible contribution to the choice; when a decision or later use needs a retained inquiry limitation or reason, that minimum content in the same decision result.
- what the current comparison concludes: one emitted `ChoiceResult` that says choose now, reject the current set, probe again, or reroute.
  That result must name either the selected option, the retained tie-set, the rejected current set, or the next probe or reroute named by value.

Without that explicit tuple, choice doctrine usually collapses into one of three easier but wrong substitutes: generic rationality talk, search folklore, or planning folklore.

The finish condition is more specific than "the record now sounds informed." The record is finished enough for practical use only when the choice result stated in `ChoiceResult` follows from the stated comparison basis, stated `ChoiceRule`, and any applicable probe decision value rather than from unstated background assumptions.

A `C.11` pass is finished enough for practical use when all three conditions hold:

- the current comparison basis is explicit enough to explain the stated `ChoiceResult`: why an option or tie-set survives, no current option survives, or probing or rerouting is needed;
- any live inquiry alternative has been resolved sufficiently to support the choice, and the result retains any inquiry reason or limitation needed by this decision or its recipient;
- the next question is explicit: `choose now`, `reject current set`, `probe again`, or `reroute`.

An inactive inquiry item adds no placeholder or omission account to this tuple or finish condition.

If the case remains tied or underdetermined under the current basis, say that directly and keep the tie-set explicit. A lawful `ChoiceResult` may still be `probe again` or `reroute`, but it must not pretend that one winner already exists when the current basis has not earned that conclusion.

If those conditions are still missing, the pattern has not yet answered the choice question even if the terminology already sounds sophisticated.

### C.11:5 - Archetypal Grounding

#### C.11:5.1 - System grounding

**Tell.** A research team already has three experiment plans on the table. The option set exists. The real question is to decide which plan to run and whether one more measurement is worth the delay.

**Show.** The `DecisionSubject` is the team, the `DecisionSubjectGranularity` is team-level, the `OptionSet` is the three current plans, the team's `PreferenceOrder` puts risk reduction ahead of schedule convenience, and the current `OutcomeModel` still carries calibration uncertainty. The extra calibration run belongs in the `ProbeActionSet`, its one-day delay is part of the `ProbeBudget`, and the practical question is whether its `ValueOfInformation` exceeds its `CostToProbe` by enough to change the emitted `ChoiceResult` under the current `ChoiceRule`.

**Show.** If the extra calibration run could still change which plan survives, the one-day delay fits the remaining `ProbeBudget`, and the expected gain justifies its `CostToProbe`, the right `ChoiceResult` is `probe again` with that exact calibration run named. If the measurement can no longer overturn the ranking, the right `ChoiceResult` is `choose now` with the winning plan and the reason further probing is no longer worth its cost.

**Show.** A finished result here should therefore read like one decision record, not one research-theory aside: "Team-level chooser; three current plans; risk reduction preferred; calibration uncertainty still live; one extra calibration run remains feasible and could still overturn the current ranking; its expected gain justifies `CostToProbe`, including the one-day delay; `ChoiceResult = probe again with calibration run`." Or, after that probe is no longer worth doing: "`ChoiceResult = choose plan B now because the remaining calibration gain no longer justifies one more day of delay`."

**Show.** `C.38` is the place for turning labels or fragments into complete ways of obtaining one result, `C.18` is the place for open-ended invention of new plans, `C.19` is the place for broader exploration policy over the plan pool, and `C.24` is the place for the run sheet and execution order after the choice is made.

#### C.11:5.2 - Episteme grounding

**Tell.** A model-selection comparison takes three already-articulated explanations and asks whether one more observation or one more comparison pass is rational before preferring one explanation over the others.

**Show.** `C.11` governs the decision doctrine over the current explanation set: one `BeliefState`, one `OutcomeModel`, one explicit `PreferenceOrder` or `EvaluativeMeasure`, and, when the case needs it, either one `InterventionModel` or one `CounterfactualModel` plus one `SubjunctiveDependenceRelation`, rather than one thinner evidential comparison. When another model comparison pass is on the table, `ValueOfComputation` belongs here as part of the current choice doctrine rather than as one later planning afterthought.

**Show.** If one more comparison pass cannot realistically change which explanation survives, the decision record should not end with "more analysis may help." It should end with one `ChoiceResult` that prefers the current explanation now. If one more pass could still reverse the ordering and is cheap enough to justify, the decision record should say exactly which pass is worth doing and what ambiguity it is expected to resolve.

**Show.** A lawful closing line here is therefore something like: "`ChoiceResult = choose model 2 now because the surviving uncertainty no longer changes the ordering under the current evidence`" or "`ChoiceResult = run one additional comparison pass on models 1 and 2 because the current outcome model still cannot distinguish their failure costs`." Anything vaguer leaves the decision question unfinished.

**Show.** This pattern does not yet govern open-ended hypothesis generation and does not yet govern operational rollout. Those questions stay outside this pattern even when the decision later feeds them.

#### C.11:5.3 - Collective and contextual grounding

**Tell.** A clinical board must decide whether to escalate a patient now or order one more test. The board is the chooser, not one isolated individual, and the result shifts when the case is discussed in prognosis-first versus risk-first order.

**Show.** `C.11` keeps the case legible by typing the chooser as one `DecisionSubject` at explicit `DecisionSubjectGranularity`, keeping the available actions as one current `OptionSet`, keeping one explicit `BeliefState` and `OutcomeModel` around those actions, and asking whether another test belongs in the `ProbeActionSet` with enough expected value to justify its `CostToProbe`.

**Show.** Active-inference-adjacent pressure is visible because the chooser is embodied, online, and socially coupled; quantum-like pressure is visible because context and question order change the comparison state. `C.11` keeps both repaired limitations visible without pretending that the whole pattern has already become one full active-inference or quantum-like formal package.

**Show.** If the order effect still changes which option survives, the comparison should say that directly and keep the comparison unfinished. The next comparison move is then either one framing-stabilizing probe or declaring the comparison order under which the current result will be judged. It should not hide that instability inside one vague statement that the board has mixed intuitions.

**Show.** An admissible output here therefore looks like one of three concrete records:

- `ChoiceResult = probe again with one rapid diagnostic test because the current prognosis-first versus risk-first framing still changes which option survives`;
- `ChoiceResult = choose now and escalate because, under the fixed risk-first order and current evidence, no remaining feasible test can reverse the survivor relation before delay increases harm`;
- `ChoiceResult = reroute to C.24 because the board has already chosen escalation and the next task is now treatment sequencing rather than local choice`.

**Show.** The output still has to be one actionable record. If the current result cannot say which of those three forms is now lawful, then the contextual pressure has been noticed but not yet carried into one usable decision result.

### C.11:6 - Bias-Annotation

This pattern is intentionally biased toward `Prag` and `Onto/Epist` discipline.

It prefers one clear decision-theory EntityOfConcern, one explicit neighboring-question split, and one minimal mathematical floor over one looser but more rhetorically flexible notion of rationality.

That bias can feel too strict in cases where the chooser, option set, or dependence structure is still genuinely moving. The mitigation is not to weaken the pattern back into one general rationality account. The mitigation is to keep the unfinished state explicit: hold one tie-set, hold one `probe again` result, or state the neighboring subject pattern that now truly governs the question.

The family map also remains plural: causal, success-first, active-inference, and quantum-like repairs stay visible without being overpromoted into one default doctrine.

### C.11:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C11.1` | The pattern **SHALL** state that `C.11` governs choice among already-available options rather than formation of comparable ways or open-ended candidate generation. | Keeps `C.38` and `C.18` outside and prevents candidate-construction or search takeover. |
| `CC-C11.2` | The pattern **SHALL** keep `DecisionSubject` as the default chooser term, and **SHALL NOT** use `Agent` as the generic chooser term unless one explicit agency claim is governed by `A.13`; measured characteristic and evidence claims use `A.17` for Characteristic identity and arity, `A.18` for Scale and Coordinate bindings, `A.19` for the declared space and reusable predicate, `C.16` for the measurement account, and `A.10` for bounded reliance on the evidence. | Prevents unwanted narrowing of the chooser. |
| `CC-C11.3` | The pattern **SHALL** state the boundary among `C.11`, `C.38`, `C.18`, `C.19`, `C.24`, and `G.5` explicitly in the body. | Prevents collapse of choice doctrine, same-result way formation, open-ended generation, candidate-pool policy, planning, and selector-facing result declaration. |
| `CC-C11.4` | `Solution` **SHALL** state one inspectable decision procedure from `DecisionSubject` and `OptionSet` through comparison basis, dependence layer, applicable probe-worthiness test, one explicit `ChoiceRule`, and one emitted `ChoiceResult`. | Keeps `C.11` as one operational answer to the choice question rather than one survey of schools. |
| `CC-C11.5` | The pattern **SHALL** name one minimal decision inventory including `DecisionSubject`, `DecisionSubjectGranularity`, `OptionSet`, `PreferenceOrder`, `EvaluativeMeasure`, `BeliefState`, `OutcomeModel`, `ChoiceRule`, `ChoiceResult`, `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation`. | Keeps the calculus objectual rather than slogan-like. |
| `CC-C11.6` | Load-bearing inventory terms used in the pattern text **SHALL** receive local plain glosses or equivalent operational clarification inside the body. | Prevents the core terminology from remaining implicit or displaced into outside basis carriers. |
| `CC-C11.7` | Relation-heavy terms such as `PreferenceOrder`, `CounterfactualModel`, and `SubjunctiveDependenceRelation` **SHALL** remain answerable to `A.6.P` together with `A.6.5`. | Keeps dependence language inspectable and deconflicted. |
| `CC-C11.8` | Active-inference and quantum-like lines **SHALL** be introduced through the limitations they repair, not as prestige branch names. | Preserves practical meaning and avoids branch-name citation without operational load. |
| `CC-C11.9` | The pattern **SHALL** expose one minimal mathematical floor without overclaiming one full quantum-like or geometry-heavy formal package. | Keeps the pattern usable now while leaving heavier support work typed and explicit. |
| `CC-C11.10` | `ProbeBudget` **SHALL** stay in `C.11` while it means the budget for further probing before choice, and `ValueOfInformation` / `ValueOfComputation` **SHALL** stay theory-side comparative criteria even when `C.19` or `C.24` later consume their outputs. | Preserves the bounded-resource bridge without letting neighboring patterns steal the doctrine. |
| `CC-C11.11` | Shortlist or other selector-facing set-result declaration **SHALL NOT** be treated as part of `C.11`; if the question shifts to declaring or naming that result, the text **SHALL** apply `G.5`. Actual presentation or availability **SHALL** remain separate: use `E.17` for the publication face and return to source and `E.24.PUB` for the publication occurrence and availability. | Preserves the boundary among local choice, selector-result declaration, and publication availability. |
| `CC-C11.12` | When one heavier dependence layer or neighboring family line is activated, the text **SHALL** state what limitation of the simpler comparison it repairs and what changes in the actual comparison once that line is in play. | Prevents branch-name citation from replacing use-time doctrine. |
| `CC-C11.13` | The text **SHALL** make the closure rule explicit enough to justify why the lawful result is `choose now`, `reject current set`, `probe again`, or `reroute` rather than some softer holding-pattern output, and **SHALL** treat vaguer endings as unfinished rather than as lawful results. | Prevents the decision record from ending in one sophisticated but operationally empty result. |
| `CC-C11.14` | The decision record **SHALL** make one minimal decision-record shape explicit: chooser, option set, comparison basis, one explicit `ChoiceRule`, inquiry content under the condition in 4.2.1, and one emitted `ChoiceResult`; `choose now`, `reject current set`, `probe again`, and `reroute` outputs **SHALL** each state their mandatory fields explicitly enough to determine the lawful choice result without reopening surrounding rationale. An inactive inquiry item is not a missing mandatory field and creates no omission record. | Keeps the pattern usable as one working decision record rather than one doctrinal memo. |
| `CC-C11.15` | If a `ChoiceResult` is supported by a causal effect, counterfactual comparison, causal policy, or off-policy causal evaluation claim, it **SHALL** carry `ChoiceResult.causalUseSpec?` with the target rung, claim kind, relevant support-component refs, support-result ref when consumed, supported use, and unsupported use. | Prevents decision-theory vocabulary from certifying causal-use support. |

### C.11:8 - Common Anti-Patterns and How to Avoid Them

One quick usability test helps here: if the closing line does not state one lawful choice result for the working chooser or team, the current result is still unfinished even if the doctrine survey looks polished.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| --- | --- | --- | --- |
| Candidate-formation or search takeover | The text starts constructing complete ways or generating options as if that work were already part of decision doctrine. | `C.11` loses its decision-theory EntityOfConcern and silently absorbs `C.38` or `C.18`. | State the option set as already existing; use `C.38` for same-result way formation and `C.18` for open-ended generation. |
| Policy collapse | Exploration or exploitation governance over a candidate pool is written as if it were identical with choosing among current options. | Choice doctrine and candidate-pool policy become indistinguishable. | `C.19` remains explicit as the neighboring pattern for selection policy and exploration governance. |
| Planning collapse | Sequencing, replanning, and enactment budgeting are written as if they were already part of the choice calculus. | Planning-side question moves out of `C.24` by accident. | Execution order and operational budgeting remain in `C.24`, even when `C.11` says more probing is rational. |
| Inventory without decision rule | The current comparison names many objects and schools but never shows how to move from a live option set through one `ChoiceRule` to one `ChoiceResult`. | The pattern becomes one cleaned-up survey rather than one decision discipline. | State one explicit decision-record shape: chooser, option set, comparison basis, dependence layer, applicable probe-worthiness test, one explicit doctrine, and one emitted result. |
| Hidden basis shift | Different options are compared under different belief states, outcome models, or dependence layers without one explicit statement that the basis changed. | The comparison only looks precise; in fact the choice rule cannot be audited. | Keep one shared comparison basis until one named probe or model change updates it, and state explicitly when the dependence layer changes. |
| No closure rule | The text sounds careful but never says what makes `choose now`, `reject current set`, `probe again`, or `reroute` lawful. | The record never closes into one explicit decision result. | State the closure conditions explicitly and show why the current case satisfies exactly one of them. |
| Undefined load-bearing terms | Terms such as `PreferenceOrder`, `BeliefState`, or `OutcomeModel` appear without local operational clarification. | Core comparison objects stay implicit and the decision question depends on outside theory or undocumented assumptions. | Give one local plain gloss or equivalent operational clarification for each load-bearing term used in the pattern text. |
| Bounded-resource bridge loss | `ProbeBudget`, `ValueOfInformation`, or `ValueOfComputation` are mentioned, but the text silently lets `C.19` or `C.24` own them. | The theory-side doctrine disappears into neighboring policy or planning prose. | Keep those objects theory-side in `C.11`; let neighboring patterns consume their outputs without minting the concepts. |
| Result-boundary collapse | The text treats declaring selector-facing set content, or later making it available, as if either were identical with deciding. | Choice doctrine silently absorbs the `G.5` result question or the publication question. | Keep both outside `C.11`: use `G.5` to declare the selector-facing result, `E.17` for its publication face and return to source, and `E.24.PUB` for the publication occurrence and availability. |
| Agent-default narrowing | Every chooser is described as one `Agent` even when the subject is really one team, organization, or other collectivity-bearing system. | The governed chooser is narrowed before the doctrine even starts. | `DecisionSubject` remains the default, and `DecisionSubjectGranularity` types the chooser-bearing level. |
| Prestige-branch citation | Active inference or quantum-like work is cited only as one fashionable name. | The text sounds current without stating what limitation is being repaired. | The repaired limitation is stated directly: embodied online updating for active inference, and context or order effects for quantum-like lines. |
| Cost-free deliberation | The text speaks as if probing and computation are free. | Bounded-resource doctrine disappears behind one idealized choice moment. | `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` stay visible in the calculus. |

### C.11:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| --- | --- |
| Keeps decision doctrine distinct from search, candidate-pool policy, and planning. | The same working episode now needs an explicit question split across choice, pool policy, and planning rather than one blurred rationality account. |
| Makes evidential, causal, and subjunctive branches comparable in one place. | The pattern becomes more explicit about dependence language and therefore needs tighter lexical discipline. |
| Keeps bounded-resource probing inside the doctrine rather than as one afterthought. | Fast-path use now carries a slightly richer inventory before the doctrine feels natural under pressure. |
| Keeps active-inference and quantum-like repairs visible without letting them silently replace the whole core. | Those lines stay load-bearing only when they change the actual `ChoiceResult`, unfinished state, or reroute logic; heavier formal packages still remain outside this body. |
| Makes the choice result explicit through one `ChoiceResult` record instead of one general statement that the case is complex. | Each decision record has to show why `choose now`, `reject current set`, `probe again`, or `reroute` is lawful, which removes rhetorical room to sound informed without committing to one result. |
| Makes downstream work cleaner because search, pool policy, publication, and enactment can receive one explicit output instead of one blurred upstream "decision happened" claim. | Reroutes now require one named next subject pattern and one reusable part of the record instead of one vague upstream claim that deliberation happened somewhere. |
| Lets one comparison stay open honestly through one explicit tie-set or `probe again` result instead of forcing a fake winner. | Some outcomes will look less rhetorically decisive because the pattern refuses to hide unfinished comparison under elegant prose. |

### C.11:10 - Rationale

A live option set and a live choice among that set are not the same question as generating options, governing a candidate pool, or sequencing execution. Keeping that distinction explicit is what makes the doctrine usable rather than ceremonial.

`DecisionSubject` is the better default chooser term because decision theory often applies to persons, teams, organizations, and other system-bearing collectivities. `Agent` remains useful, but only when an explicit agency claim is actually being made.

A minimal mathematical floor is necessary because choice doctrine without one stable object stack quickly turns into verbal drift. But a pattern also fails if it keeps only the object names and never shows how those objects discipline an actual choice. That is why `Solution` here is procedural: it must carry the path from `OptionSet` through one `ChoiceRule` to one `ChoiceResult`, including the stop-or-probe decision, rather than only one survey of neighboring theories.

The practical gain of that procedure is not elegance for its own sake. It is that later search, policy, publication, and planning work receive one explicit result instead of one hand-waving claim that deliberation happened somewhere upstream.

At the same time, this pattern should not pretend that one full quantum-like or geometry-heavy package is already settled just because those neighboring lines are real.

### C.11:11 - SoTA-Echoing

| Claim | SoTA practice | Primary source | Alignment with `C.11` | Adoption status |
| --- | --- | --- | --- | --- |
| Decision theory still needs an explicit classical baseline over options, preferences, utility, and uncertainty. | Contemporary reference treatments still present decision theory through option sets, preferences, utilities, and uncertainty as the baseline language of rational choice. | [Decision Theory (Stanford Encyclopedia of Philosophy, Fall 2023)](https://plato.stanford.edu/archives/fall2023/entries/decision-theory/) | `C.11` adopts this as the baseline vocabulary for choice among already-available options. | **Adopt.** |
| Evidential dependence is not enough in all cases. | Causal decision theory remains the standard repair when intervention structure matters. | [Causal Decision Theory (Stanford Encyclopedia of Philosophy, Winter 2024)](https://plato.stanford.edu/archives/win2024/entries/decision-causal/) | `C.11` keeps one explicit evidential-versus-causal split rather than one blended correlation claim. | **Adopt.** |
| The field no longer stops honestly at the older EDT/CDT split. | Functional or success-first work keeps subjunctive dependence live in Newcomb-like and related cases. | [Functional Decision Theory: A New Theory of Instrumental Rationality](https://arxiv.org/abs/1710.05060) | `C.11` keeps success-first or subjunctive repair visible without treating it as one settled default doctrine. | **Adapt.** |
| The live EDT/CDT/FDT family map now has more technical comparison structures than one older philosophical split alone. | Recent mechanized or causal-graph taxonomies compare live decision-theory families through more explicit technical structures rather than only one slogan-level naming dispute. | [Mechanized-causal-graphs taxonomy of decision theories (2023)](https://arxiv.org/abs/2307.10987) | `C.11` therefore treats EDT, CDT, and success-first or FDT-like lines as technically live family options rather than one frozen classroom argument. | **Adapt.** |
| Decision under bounds cannot leave probing and deliberation cost as one slogan. | Current metareasoning and optimal-experimental-design lines treat information acquisition, probing, and computation allocation as first-class theoretical questions rather than free background steps. | [Metareasoning: Theoretical and Methodological Developments](https://pmc.ncbi.nlm.nih.gov/articles/PMC11765846/) | `C.11` therefore keeps `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` inside the doctrine rather than hiding them in planning-only prose; the current closure rule is intentionally local or myopic over the next feasible probe, with richer sequential or non-myopic `OED` left as later strengthening. | **Adapt.** |
| Decision and update can be embodied, online, and socially coupled. | Active-inference work treats decision as tightly coupled to action, inference, and expectation regimes rather than one disembodied one-shot selection. | [Embodied decisions as active inference](https://pmc.ncbi.nlm.nih.gov/articles/PMC12201680/) | `C.11` carries this as one neighboring repair of the chooser picture, makes social-expectation pressure explicit enough for use-time reroute or probe logic, and states honestly that full `ROE` or social-expectation object modeling remains outside this local choice body. | **Adapt.** |
| Some decision cases exhibit context effects, order effects, response-replicability tension, and incompatible-question structure. | Current quantum-like decision and cognition work treats those cases as one measurement-sensitive research program rather than one discarded curiosity or one automatic physics transfer. | [Measurement-theory decision/cognition anchor (2025)](https://arxiv.org/abs/2503.05859) | `C.11` carries this as one named neighboring branch where those repaired limitations are real, while leaving heavier branch-specific formalism outside this body. | **Adapt.** |
| Incompatible question/context structures need a cleaner cue than "context matters." | Contextuality-by-Default treats same-content-looking measurements in different contexts as distinct random variables unless an admissible joint treatment is supplied. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207) | Use CbD as the clean formal cue when question/context structure changes variable identity, joint availability, or admissible comparison inside the current option set. | **Adopt/Adapt.** |
| Some quantum-like lines also claim one practical representational gain from linear state dynamics over harder nonlinear underlying processes. | Quantum-like modeling in biology presents linear Hilbert-space dynamics as one simplifying and potentially faster information-processing lens over nonlinear classical biophysical dynamics, while treating this as representational modeling rather than proof that the modeled system is physically quantum. | [Quantum-like modeling in biology with open quantum systems and instruments](https://www.sciencedirect.com/science/article/pii/S0303264720301994) | `C.11` takes this only as one possible practical reason to keep the quantum-like branch available when measurement-sensitive effects are real; it does not treat quantum-like choice as one claim of physical quantumness. | **Adapt cautiously.** |
| Broader contextual and multilevel lines pressure decision texts to keep one typed substrate rather than pure verbal drift. | Current multilevel-learning and evolution-as-inference work argues for one shared formal lens across levels even when the heavier final geometry is still unsettled. | [Multilevel selection as Bayesian inference, major transitions in individuality as structure learning](https://royalsocietypublishing.org/doi/10.1098/rsos.190202) | `C.11` therefore keeps one minimal typed floor and one wider chooser-bearing scope while stating by value that full aggregation doctrine, cross-scale or cross-collective conflict doctrine, and heavier multilevel mathematics remain outside this local choice body. | **Adapt.** |

Practical reading of this alignment:

- In ordinary current-option cases, start with the classical evidential baseline and use it to emit one explicit `choose now`, `reject current set`, `probe again`, or `reroute` result under one shared `BeliefState` and `OutcomeModel`.
- Failure of a simple Bayesian or passive-read-like model is not yet evidence that QL is necessary. Try richer classical, causal, performative, instrument, active-sensing, or representation-abstraction rivals before keeping the QL branch as load-bearing.

- If intervention structure changes the survivor relation, state that explicitly and switch to causal comparison rather than leaving the comparison at the level of correlation talk.
- If predictor-coupling or structurally linked choice procedures remain load-bearing, keep the subjunctive layer visible and say what linked structure could still reverse the current result.
- If another measurement, comparison pass, or search pass is being considered, treat its value and cost as part of the current decision doctrine rather than as one later planning afterthought.
- If the chooser is embodied, online, and socially coupled, or if context and order effects change the comparison state, keep those repaired limitations visible by naming the observation, social-expectation clarification, order stabilization, response-replicability check, or measurement-class clarification that could still change the current `ChoiceResult`, and say directly when fuller `ROE`, quantum-like state-space, or multilevel doctrine still sits outside this local choice body.
- If the quantum-like line is activated, treat it as one measurement-sensitive mathematical lens or representational repair, not as one claim that the chooser or world is physically quantum.
- If none of those heavier repaired limitations is live, stay with the lighter branch rather than activating one prestigious label that does not yet change the next action.

Worked-slice discipline from these rows:

- the system grounding slice is disciplined primarily by the bounded-resource and classical-baseline rows, so the output must end in one explicit probe-or-choose result;
- the episteme grounding slice is disciplined by the bounded-resource row and the dependence layer active in the case; the output must name the comparison pass that could still reverse the result, or a predictor-coupled clarification when that coupling is live;
- the collective and contextual grounding slice is disciplined primarily by the active-inference and quantum-like rows, so the output must name the embodied observation, framing stabilization, or reroute that now becomes lawful.

**Smallest reopen.** A newer publication does not by itself reopen `C.11`. Reopen only when it materially changes the current-option boundary, chooser, comparison basis, probe value or cost, or one branch-activation condition used by the `Solution`. Revise the affected source row and its matching procedure branch, worked slice, checklist item, or public entry cue; leave unrelated decision doctrine unchanged.

### C.11:12 - Relations

- **Builds on:** `A.6.P`, `A.6.5`, `A.10`, `A.13`, `A.18`, `A.19`; **coordinates with:** `E.10.LRN` for learning-word recovery, `C.11.CRC` for a missing finite configuration-relative comparison claim, `C.17` for bounded characterization
- **Read next when this question leaves local choice:** `C.38` for forming complete ways of obtaining one result, `C.18` for open-ended candidate generation and reframing, `C.19` for one explicit pool-policy result over exploration or exploitation governance, `C.24` for one enactment-facing call plan or `CheckpointReturn`, `G.5` for the selector-facing result kind that is actually current—retained alternatives, all-member joint use, narrowed handoff, abstain, or escalation—and `C.28` when the choice result depends on causal-use support
- **Keeps outside:** candidate generation, pool-wide exploration or exploitation policy, selector-facing set-result declaration, publication availability, and execution sequencing
- **Aligns with:** classical evidential decision theory, causal decision theory, success-first or subjunctive repair, bounded-resource metareasoning and probe-cost doctrine, `C.28` causal-use question/rung/support vocabulary, active-inference-adjacent decision work, quantum-like contextual repair where context or order effects are real, and multilevel mathematical-lens pressure at the minimal-floor level only

### C.11:12a - Quantum-like choice-boundary note

Use C.11 first when the question is local choice, belief, preference, comparison, question order, option-menu framing, or an incompatible-question effect inside one decision situation. Quantum-like wording is retained only when it adds a concrete residual order-effect, probe, frame, or comparison reading that ordinary decision or probability language would hide.

Decision repair sequence:

1. State the current `DecisionSubject`, `OptionSet`, comparison basis, and `ChoiceRule`.
2. Ask whether the apparent QL issue changes the local choice result: choose now, reject current set, probe again, or reroute.
3. If the issue is question order, incompatible questions, response-replicability tension, non-shared comparison frames, or CbD-style variable identity / joint-availability trouble inside the current option set, keep the QL repair inside C.11.
4. If the current option set itself is suspect, incomplete, generated by the wrong frame, or still needs expansion/reframing/search, leave C.11. Use `C.18` for option generation, reframing, and archive/front stewardship; `C.19` for live-pool policy; `A.19` for the declared CharacteristicSpace or reusable predicate; or `B.5.2` for abductive hypothesis formation, according to the question that needs repair.
5. If the issue changes boundary state, bridge/export faithfulness, coordinated-work evidence, measurement admissibility, or viability envelope, apply the pattern governing that claim.
6. Emit one `ChoiceResult` and one next question; do not leave the QL branch as a theory label.

When the question leaves local choice, apply the subject pattern instead of stretching C.11:

| Question that appears in the decision case | First pattern |
| --- | --- |
| Boundary interaction, API read, workshop, dashboard, or message changes the represented state | `C.26.1` only for the remaining state or probe question, with `A.6`, `A.6.B`, and `A.6.P` still active |
| Cross-context export, translation, or same-label comparison loses state or comparability | `F.9` |
| Coordinated work evidences a state no report faithfully carries | `A.15` plus evidence patterns, with `C.26.2` only for the remaining low-recoverability distributed-state reading |
| Measurement, metric, survey, or score frame changes the represented state | `C.16` plus evidence patterns |
| Viability envelope, adaptation cost, or boundary-maintenance decision is load-bearing | `C.25` for a quality bundle with several differently typed contributors; `C.26.3` for a multi-characteristic viability envelope under disturbance when a candidate intervention, boundary condition, adaptation cost, or failure mode matters. Add `C.26` for a remaining probe/export/frame/coarsening question only when an exact contextual-model obstruction still changes what may be inferred or done after the ordinary patterns have carried their part. |
| Current option set is suspect, incomplete, frame-generated, or still being expanded/reframed/searched | Before applying C.11, use `C.18` for option generation, reframing, and archive/front stewardship; `C.19` for live-pool policy; `A.19` for the declared CharacteristicSpace or reusable predicate; or `B.5.2` for abductive hypothesis formation, according to the question that needs repair. |

Useful outputs:

- `choose now` under a declared order/frame;
- `probe again` because another question order, response-replicability check, or frame test could still change the survivor relation;
- `reroute` because the live problem is no longer local choice;
- no QL wording when ordinary uncertainty, preference conflict, or option-generation work is enough.

C.11 may cite `C.26` as the common quantum-like modeling lens only for the residual question after the local-choice split is applied. It is not the whole-cluster pattern for boundary, bridge/export, distributed-evidence, viability, or state-representation coarsening claims.

### C.11:12b - C.29 mathematical-lens use relation

> `C.29` may supply a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note that a decision record can cite. If the output is a `ChoiceResult` or local choice record, use `C.11` to state and test the decision. Any `G.5` selector-result declaration and `G.9` benchmark result remain separate. When one of those results must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. `C.29` does not select the option by mathematical elegance.

### C.11:End

