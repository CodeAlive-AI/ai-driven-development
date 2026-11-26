## C.11 - Decision Theory (Decsn-CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** `C.11` is the choice-calculus pattern for the moment when options exist and the working question is which option to choose, including whether another probe is worth its cost before commitment.

The alternatives may include a policy or a trajectory. Use C.43 when the practitioner must also construct alternatives, connect a choice to later observations and actions, or revise the course during execution.

### C.11:1 - Problem frame

**When ongoing Work still needs a next action.** If admissible actions still have to be recovered from ongoing Work, its domain Method, and current facts, use `A.15.7` first. Return here only when a current chooser and `OptionSet` exist and comparison can change the result; a mandatory response or one familiar cue need not be expanded into an option set.


**Use this when.** Use this pattern when one `DecisionSubject` already has an `OptionSet` in hand and the question is how to choose among those already-available options under uncertainty, preference, causal or subjunctive dependence, and bounded probing or computation.

**First useful result.** Identify who makes this choice, the alternatives, what each could lead to, and the rule used to compare them. State which option or options the rule supports, why all fail, what further inquiry is worth doing, or where the remaining question belongs. When another party decides, that comparison can serve as advice. To report an actual decision, establish who made it or which authorized procedure put its result into effect.

When a choice is still open, give the recipient the comparison available now, the missing grounds and who can settle it. A supported recommendation or an unfinished comparison can be delivered before the holder decides.

**First-minute questions.**

- Who makes each choice the outcome depends on? If the outcome requires several decisions, how do they take effect together?
- What options are already on the table now?
- What current basis is being used to compare them?
- What could a further observation or calculation change about the choice or what the recipient can rely on?
- Is this still local choice, or has the question moved to a neighboring problem—for example, search, pool policy, selector-result declaration, publication availability, or enactment?

**When advice still hides the decision.** Use `C.11.DUA` when a recommendation or evidence demand still needs its receiving question, demanded work or requirement merits recovered. Return here when a current chooser and options support a local choice. An already adequate choice uses this pattern directly.

**Typical reroutes.** For candidate construction or development, use `C.38`–`C.40` as specified in §4.4; that section also distinguishes pool policy, selected-set publication and enactment. Use `A.13` when agency itself is at issue, or `A.18`/`A.19` when Scale bindings or a declared CharacteristicSpace or reusable predicate are the unresolved question.

**What the chooser gets.** The same options can yield different recommendations if they indicate an outcome, bring it about, or depend on what another chooser will do. Identify the dependence that matters, then check which alternatives the current facts support and what further inquiry could change.

**Not this pattern when.** Do not start here when the current question is still generating candidate options, setting exploration or exploitation policy over a candidate pool, declaring selector-facing set-result content, making that result available to an audience, or sequencing execution under an operational plan.

### C.11:2 - Problem

Many systems have options on the table but still lack one explicit doctrine for what makes one option rational to choose. They mix together at least four different questions.

One question is still generating candidate options, variants, or open-ended search directions. Another question is governing how broadly a candidate pool should be explored or exploited before narrowing. A third question is planning, sequencing, replanning, or enacting the chosen option once a choice has already been made. The fourth question, and the one governed here, is choosing among already-available options under uncertainty, dependence, and bounded deliberation.

A second distortion appears when decision theory is reduced to a slogan about expected utility. Real choosers face evidential and causal distinctions, subjunctive or success-first cases, probe costs, information value, computation value, and situations where the chooser is not just one isolated individual.

Without an explicit place for choice calculus, search, candidate-pool policy, and planning get treated as the same question, while the doctrine of choosing among live options disappears behind generic talk about rationality.

### C.11:3 - Forces

| Force | Tension |
| --- | --- |
| Choice doctrine versus candidate formation and generation | `C.11` must govern choice among already-available options without taking over their formation or development. |
| Evidential, causal, and subjunctive dependence | The pattern must stay usable with classical decision language while making room for causal and success-first repairs where correlation is not enough. |
| Decide now versus probe more | The chooser may need to stop and choose now, or spend more effort on information and computation first. The theory must make that trade legible. |
| Individual and collective choice | A person, a technical system or an authorized body may decide. An outcome may also depend on separate decisions by independent parties. Establish whose choices the governing arrangement requires. |
| Minimal mathematical floor versus premature heavy formalism | The pattern needs a stable object stack for disciplined reasoning and inspection, but it should not treat a full quantum-like or geometry-heavy package as already settled. |

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

Apply the `ChoiceRule` to the available `OptionSet`. A completed comparison yields one explicit `ChoiceResult` under that rule. If the basis still leaves the requested single choice open, §4.2.4 explains what to return to the holder now.

1. **Identify the chooser.**
   Name the `DecisionSubject`. Use `DecisionSubjectGranularity` to identify the unit to which the choice is attributed in this arrangement, for example a controller, a committee or an organization acting through a delegate. If attribution to a component or its containing system changes the result, establish their actual relation and which decision each makes. If a concert requires two independently managed orchestras to agree, identify each orchestra’s decision and the condition that requires both. An agreement can be established without treating the orchestras as one chooser. A witnessed vote can establish a board’s decision when its rule gives that vote effect. A rule requiring a signed record adds that condition.
   Distinguish the chooser from participants who provide evidence, advice or execution. Use `A.13` for a disputed claim about agency and the applicable assignment or mandate for a claim about who can decide.

2. **Freeze the current option set.**
   Establish which alternatives the commission allows and which it asks you to compare. Use the available alternatives in the current comparison as one `OptionSet`. A choice among the offers received can close on those offers. For a claim about the whole permitted domain, establish what an omitted option could change. One offer shown to meet the requirements can settle a request for a workable option. To claim a greatest option under the governing preference, establish that it is at least as preferred as every eligible alternative. Under a partial order an eligible option is nondominated when no eligible alternative strictly dominates it. To name all options attaining a best value, account for other alternatives that could tie.
   If the rows are only labels or fragments and the question is several complete ways to obtain the same result, stop here and apply `C.38`. Use `C.39` when a way to obtain the result still needs explanation, or `C.40` when usable material needs feasible variation and examination. Use `C.18` when generation-account or archive/front claims are needed.

3. **Make the comparison basis explicit.**
   State the preference or measure, current facts and uncertainty, and the `OutcomeModel` used to estimate each option’s consequences. Identify the use for which the options must qualify and any condition that excludes an option regardless of its score. Apply the same interpretation, horizon and material assumptions across options.
   The comparison is not usable if some options are being judged under one belief state and other options under one later, unmarked update.
   If rival outcome models give different rankings, compare all relevant options under each credible model. Show which conclusions hold across them and which depend on an unresolved assumption. A new measurement may update a parameter or the model. A disputed preference or mandate requires its own decision.

4. **Choose the dependence layer that governs the case.**
   Start from the evidential baseline when the choice is being compared through likely outcomes under the current `BeliefState`.
   Add one `InterventionModel` when taking one option changes the world through intervention rather than mere observation.
   Add one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when the case depends on one predictor, one structurally linked chooser, or one decision-procedure coupling that intervention talk alone does not capture.
   Use the least-committing dependence layer that still covers the live case, and do not switch layers across options without saying so explicitly.

5. **Compare a live inquiry alternative before commitment.**
   Consider another observation or computation when a plausible outcome could change the choice, the claim supporting it or the use for which it is admissible. Identify whose time or other resources the inquiry consumes. A mandatory check has the force and scope of its governing rule.
   Apply the probe-worthiness test to that alternative, stating the feasible probe, budget, cost and relevant information or computation value at the precision the choice needs. Otherwise this step adds no investigation or recording requirement. An empty form field does not activate inquiry, and no new search is required to certify that no other inquiry exists.
   Compare the best attainable next probe for this choice. A longer sequential experiment design can be a separate question. If an inquiry is binding, apply its governing terms to eligibility or use.
   When no worthwhile feasible probe remains, apply the choice rule to the evidence available. The cost of more inquiry can justify stopping. Selecting an option still needs grounds for its eligibility and preference. If a binding prerequisite remains unmet, keep the affected choice or use open, narrow it where the rule permits, or select an eligible alternative.
   If the expected gain warrants a feasible probe, return `probe again` and name it. After someone performs the probe, use its actual result to update the comparison. An inconclusive observation can leave the ranking unchanged.
   If one choice result is already fixed and the remaining probe would change only execution-path description, call-plan ordering, enactment budget, or checkpointing of that chosen option, stop treating the probe as local choice doctrine and apply `C.24`.

6. **Apply the `ChoiceRule` and report what it supports.**
   A completed comparison has one result form: `choose now`, `reject current set`, `probe again`, or `reroute because this is no longer local choice`. An open comparison can still inform the holder under §4.2.4.
   For `choose now`, give the option or retained set and its grounds. State whether the alternatives in a retained set are equally preferred or incomparable, and which further decision, if any, remains.
   If the result is `reject current set`, name the reason no current option survives under the present basis and, when more work follows, the neighboring question that now takes over.
   If the result is `probe again`, name the next probe and the exact comparison defect it is supposed to repair.
   State the conditions under which the result follows from the rule. If another person or system must adopt the recommendation, the result can go to them now.

##### C.11:4.2a - Receive heterogeneous premises without relabeling them as signals

An interesting observation, information-gain estimate, capability result, objective or reward, articulated former cue, or `C.17` characterization enters this pattern only under its exact source/result identity. Use `E.10.LRN` first when *learning* wording still hides that identity. Preserve the source and support needed for the bounded premise use. Reuse an adequate existing account; use `A.10` when the source-to-use account remains implicit or must be replayable. An applicable `RelianceDisposition` qualifies only that premise use.

An objective, reward, preference, or loss enters as the `EvaluativeMeasure`, `PreferenceOrder`, or `ChoiceRule` input it actually supplies and is not evidence by numerical form. When an `A.16.1` cue pack remains current as a source or provenance episteme, preserve that source identity and route the separately articulated endpoint result through its direct claim owner. A `C.17` novelty, surprise, use, or creativity characterization remains a characterization and does not license a move by itself.

No separate premise-qualification result sits between those owners and `C.11`. Use the qualified inputs in the live option/probe comparison and return only the existing `ChoiceResult`. When the missing comparison basis is specifically what a finite candidate contributes relative to the current configuration, use `C.11.CRC` to construct that ordinary comparison claim and return here. If every premise and the finite comparison are already explicit, proceed directly.

When a later outcome must first be compared with an earlier decision's actual relied-on basis, use `C.11.DBR` to localize the material difference and preserve unaffected uses. Return here when the current chooser, finite `OptionSet` and comparison basis are available. This prepares a particular reconsideration; it adds no qualification layer for otherwise ready premises.

##### C.11:4.2.1 - Well-formed comparison state


Well-formedness constraint: a live `C.11` comparison state is usable only when the decision record states the following, subject to the stated condition on inquiry:

- one `DecisionSubject` at one `DecisionSubjectGranularity` for the choice being represented. When the receiving outcome requires several independent choices, use the respective subjects and establish how their decisions combine.
- one current `OptionSet`;
- one current comparison basis through `PreferenceOrder` or `EvaluativeMeasure`, plus one `BeliefState` and one `OutcomeModel`;
- one active dependence layer for the current comparison, unless the record explicitly says that comparison is still being reopened;
- when an inquiry alternative is live, an account of its feasibility, cost and possible contribution to the choice; when a decision or later use needs a retained inquiry limitation or reason, that minimum content in the same decision result.

An inactive inquiry item requires no empty value, no no-probe statement and no waiver. The chooser, option set, shared comparison basis and applicable dependence layer remain necessary.

The comparison is still unfinished, not yet wrong but not yet closeable, when any of the following remains true:

- the comparison moves between a participant’s preference and the collective decision without establishing whose rule applies;
- the option set is still changing while the record also claims to rank the options;
- one option is being judged under one belief state and another under one later update that is not itself declared as the next probe result;
- one heavier dependence layer is invoked for rhetorical force, but the record never states what defect of the lighter comparison it repairs;
- the record asks for more information without identifying a feasible inquiry and a plausible result that would change which option qualifies, the preference between options, or the claim on which the recipient could rely.

##### C.11:4.2.1a - Minimal admissible decision semantics

This minimal choice doctrine does not settle every decision-theory dispute, but it already supports some semantic distinctions by value and rules out others.

The comparison can use the following when their basis is explicit:

- an incomplete or partially ordered `PreferenceOrder`, with unresolved alternatives retained explicitly, a worthwhile further probe, or an unfinished comparison; incomparability alone does not justify `reject current set`, which requires the current rule to exclude every option;
- one `EvaluativeMeasure` for magnitude, threshold, or trade-off-sensitive cases, so long as the measure being used now is explicit enough to explain why the current result follows under it;
- one temporary unresolved criterion conflict, so long as the record says whether the present comparison is using one priority order, one threshold, one explicit trade-off measure, or one unfinished state that still blocks closure;
- one explicit `BeliefState` revision, so long as it enters the comparison as one named probe result or one named model repair rather than as one silent basis shift;
- a collective `DecisionSubject` when the decision is attributed to that body under its actual decision arrangement. If members disagree, establish the aggregation or delegation rule needed for the collective result.

The following are not admissible in this `C.11` body:

- silently totalizing one partial preference relation just to force `choose now`;
- silently switching from one criterion mix or one belief state to another across options;
- treating unresolved cross-scale or cross-collectivity conflict as a settled local ranking before the aggregation question has been resolved;
- using a record's form as a substitute for a stated comparison doctrine.

A partial order can leave alternatives incomparable. Equal preference means that the rule treats two alternatives as tied. If the receiving task accepts a set, the `retainedTieSet` field can list the retained alternatives and state which of these conditions holds. If the task needs one course, identify the applicable tie-break or the decision still needed.

##### C.11:4.2.2 - Probe-worthiness rule

Use the following three conditions to appraise an optional next probe for this choice. An independently binding condition continues to govern the affected option or use.

- the probe fits inside the remaining `ProbeBudget`;
- the expected improvement in the decision or its warranted use from the information or computation justifies the full `CostToProbe`, including delay and work displaced;
- a plausible result could change which option qualifies or is preferred, resolve a tie, reveal that the current set fails, change what use is warranted, or move the question elsewhere.

This is the local or myopic probe-worthiness rule for `C.11`: judge the best next feasible probe over the current `OptionSet`, not one whole non-myopic experiment design over longer horizons. Later sequential or non-myopic `OED` may strengthen this doctrine, but they do not relocate the local-choice question outside `C.11`.

Remaining uncertainty alone gives no reason to probe. State what plausible outcomes would change for the chooser. If every attainable result leaves the decision and its warranted use unchanged, this decision supplies no gain from that optional inquiry. An independently required check still follows its own rule.

If no worthwhile probe is available, state what the current basis and `ChoiceRule` support. If they leave the choice unresolved, name the missing premise or authority.

If the next probe would no longer change which option survives but would only change how one already-chosen option gets enacted, budgeted, or checkpointed, the question has already crossed to `C.24`.

##### C.11:4.2.3 - `ChoiceRule` versus `ChoiceResult`

`ChoiceRule` and `ChoiceResult` are not the same kind of thing.

- `ChoiceRule` is the doctrine or operator that says how the current comparison basis, dependence layer, and any applicable probe-worthiness value support one `ChoiceResult`.
- `ChoiceResult` records the conclusion reached by applying that rule to the present comparison.

A usable `ChoiceResult` gives the selected disposition and the grounds for it. It can inform a later decision or take effect directly under a delegated decision procedure. To establish which occurred, use the record of that decision or procedure.

The record has four result forms:

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
- the reason each option fails the stated conditions. Some options may fail for different reasons;
- the next neighboring question only when more work now follows, such as new option generation or one explicit escalation path.

For `probe again`, the emitted `ChoiceResult` should show:

- the next probe;
- the comparison defect that probe is expected to repair;
- the reason the probe is still worth its cost.

For `reroute`, the emitted `ChoiceResult` should show:

- the neighboring question and the pattern used to answer it;
- the reason this is no longer local choice among already-available options.

##### C.11:4.2.4 - Closure rule over the current `OptionSet`

The comparison may close as `choose now` only when all of the following are true together:

- the current `OptionSet` is stable enough that no further options are being invented for this comparison;
- the common basis and rule identify an eligible preferred option, or a set that the receiving task accepts. State whether the retained alternatives tie or remain incomparable;
- no feasible optional probe offers enough expected improvement in the selection or its warranted use to justify its full cost, and the selection meets the applicable prerequisites;
- the record still concerns local choice rather than pool policy, selector-result declaration, publication availability, or enactment.

The comparison may close as `reject current set` only when all of the following are true together:

- the current `OptionSet` is explicit and stable enough to reject as the present choice set;
- the current comparison basis is explicit enough to show why no member survives under the present basis;
- no feasible optional probe offers enough expected improvement to justify its cost in reconsidering that rejection or its warranted use;
- the result is still one local choice conclusion rather than a pool-policy, selector-result declaration, publication-availability, or enactment result.

Assess the probe conditions above from the current basis and any live inquiry alternative. They are conditions of a warranted choice, not a requirement to produce a separate account of omitted checking.

The comparison should close as `probe again` only when all of the following are true together:

- one next probe is named by value;
- that probe fits the remaining `ProbeBudget`;
- its expected contribution to the choice justifies its `CostToProbe`;
- at least one attainable result could change which option qualifies or is preferred, which claim or use is warranted, or where the question belongs. State what an inconclusive result would leave open when that matters.

The comparison should close as `reroute` when the record shows that the decision question has changed:

- to `C.38` when labels or fragments must first become complete-enough ways of obtaining the same result;
- to `C.39` when a way to obtain the result still needs explanation;
- to `C.40` when usable material needs feasible variation and examination;
- to `C.18` when the question concerns the generation account or archive/front stewardship;
- to `C.19` when the question is now how broadly to keep exploring or exploiting one candidate pool;
- to `C.24` when one choice result already exists and the next task is now sequencing, enactment, or execution-path probe work;
- to `G.5` when the next task is declaring or naming selector-facing selected-set content; when that result already exists, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and audience availability.

If no closure condition holds, send the comparison the available basis supports. Identify the eligible alternatives, the missing comparison or priority, and who can settle it. For a requested single choice, retaining several candidates can inform the decision holder while their choice remains open. Record a `ChoiceResult` when the rule supports one of the four forms.

##### C.11:4.2.5 - Minimal decision-record form

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
  selectedOption or retainedTieSet or rejectedCurrentSet or nextProbe or rerouteOwner,
  grounds for this disposition under the current rule
)
```

Exact syntax is unnecessary. The chooser, options, shared comparison basis, `ChoiceRule` and `ChoiceResult` are required. Inquiry content is required only under the stated condition; an absent block requires no placeholder or omission explanation.

Use branch language only when it changes the comparison being performed.

##### C.11:4.2.6 - Resource-aware choice over an archive or front

- When the `OptionSet` is drawn from a `Front`, `Archive`, or their composition, identify that source basis.
- Apply one declared decision lens over that source family rather than assuming an unstated universal winner rule.
- `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` belong to that lens-side choice doctrine.
- They may justify another probe, one changed local comparison outcome, or one stop decision, but they do not rename the current `DominanceSet` and do not declare one shortlist-family result.
- If one candidate remains worth probing because its expected information value still exceeds its expected cost, say that explicitly as one lens-side choice judgement.
- If one archive point remains worth probing because it may change the frontier later, keep that as one resource-aware choice claim, not as evidence that the point is already on the current front.
- For an actual `A.19.SelectorMechanism` application, retain its set-returning declaration and bindings:
  - `A.19.SelectorMechanism` remains the cited set-return floor
  - `SelectionSlot` remains the selector output floor
  - if later selector-facing set-result declaration is required, that set-returning floor may support one `Shortlist` or one `RankedShortlist` in `G.5` rather than one forced single winner

#### C.11:4.3 - Dependence layers and neighboring repairs

##### C.11:4.3.1 - Classical evidential baseline

Stay with the classical evidential baseline when the question is to compare already-available options through preferences, utilities or desirabilities, beliefs, and likely outcomes under uncertainty.

In this baseline, the options are being compared as evidence about what consequences are likely if they are chosen. This is the ordinary default when intervention structure, predictor-coupling, or context-sensitive non-commutativity do not affect the comparison.

Typical choice results are:

- `choose now` because the current shared `BeliefState` and `OutcomeModel` already make one option or tie-set survive, and no still-feasible probe is worth its cost;
- `probe again` because one further observation, measurement, or comparison pass could still change the ranking without requiring a heavier causal, subjunctive, or context-order repair;
- `reroute` because the current decision question is no longer comparing one fixed `OptionSet`, but has become search, pool policy, selector-result declaration, publication-availability, or enactment work.

The baseline remains unfinished when the comparison cannot keep a shared `BeliefState` and `OutcomeModel` across the options, or when a limitation already calls for a further dependence layer and the comparison still uses only the evidential baseline.

##### C.11:4.3.2 - Causal repair

Switch on one `InterventionModel` when taking one option changes the world through intervention rather than merely signaling which outcome was already likely.

The comparative question changes: the working question is no longer only what this option indicates about the outcome, but what this option causes in the outcome structure.

Typical choice results are:

- `choose now` because, under the declared intervention structure, one option now causally dominates or remains the survivor and no remaining feasible probe can change that comparison with enough expected gain to justify its cost;
- `probe again` because an uncertainty about the effect of an intervention prevents the current comparison and the proposed probe could change which option is preferred;
- `reroute` because the intervention-use question has already moved from local choice into enactment planning, protocol design, or one neighboring question.

The causal repair is incomplete if the comparison still treats options only as evidence after invoking causal language, or if an `InterventionModel` is named without stating what defect of the lighter evidential comparison it repairs.

##### C.11:4.3.3 - Success-first or subjunctive repair

Switch on one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when Newcomb-like, blackmail-like, or other predictor-coupled cases remain under-described by the older evidential-versus-causal split.

What changes here is that the comparison must stay answerable to linked decision procedures, predictors, or structurally similar choosers rather than only to direct intervention on one local event.

Typical choice results are:

- `choose now` because, under the declared counterfactual or subjunctive structure, one option survives once the predictor-coupled comparison is made explicit;
- `probe again` because one further model clarification, predictor assumption check, or decision-procedure comparison could still reverse the current survivor relation;
- `reroute` because the governing decision question is no longer settling local choice doctrine but has become one wider characterization, negotiation, or enactment question that only borrowed predictor-coupling language.

If that coupled structure is not live, do not activate this branch. If a predictor-coupled or success-first repair is named but the linked structure that changes the comparison is still unspecified, the branch is not yet load-bearing in the current decision.

##### C.11:4.3.4 - Active-inference neighboring repair

Bring the active-inference line into view when the chooser is embodied, online, and socially coupled, and when the decision cannot be understood as one disembodied choose-then-act moment.

The comparison is no longer over one frozen snapshot alone. It must now ask whether an additional observation, coupled update, or socially mediated or role-expectation clarification changes what should be done now.

This minimal choice doctrine makes that social-expectation pressure explicit, but it does not yet operationalize one full `ROE` or `SocialExpectationRegime` object model inside `C.11`. If the case hinges on that machinery, the decision record should state that this local `C.11` floor does not settle it.

Typical choice results are:

- `probe again` because one further embodied observation, coupled update, or explicit role-expectation clarification can still change the state estimate enough to reverse the current survivor relation;
- `choose now` when further delay would close the window for an eligible option and the current comparison supports choosing it;
- `reroute` because the question has already become enactment sequencing or agent-characterization work rather than local choice.

`C.11` keeps the choice question visible there, but `A.13` still governs the narrower question of what kind of agent or agential system is in play. For measured characteristic and evidence claims, use `A.17` for Characteristic identity and arity, `A.18` for Scale and Coordinate bindings, `A.19` for the declared space and reusable predicate, `C.16` for the measurement account, and `A.10` for bounded reliance on the evidence. `C.24` still governs sequencing and enactment once a choice result has already been fixed.

Do not invoke this line only because one agent is acting in the world. Invoke it when embodied coupling, online updating, or explicit social-expectation pressure changes what the chooser should do now from the current `OptionSet`.

##### C.11:4.3.5 - Quantum-like neighboring repair

Bring the quantum-like line into view when context effects, order effects, response-replicability tension, or incompatible-question structure change the comparative state enough that one simple commutative probability reading no longer fits.

What changes here is the practical structure of comparison. One order of questioning or one framing path may produce one different survivor relation from another. The comparison must therefore either stabilize the comparison under one declared order or show why one more clarifying pass is still needed.

This minimal choice doctrine keeps the branch at that measurement-sensitive recognition point. It does not yet claim one full quantum-like state-space package inside `C.11`; it claims only that the live comparison may need one explicit measurement-class or order-sensitive repair rather than one plain commutative reading.

Typical choice results are:

- `choose now` under one declared order or framing because rival orders no longer change which option survives;
- `probe again` because one framing-sensitive comparison pass, one further question order, one response-replicability check, or one explicit measurement-class clarification could still reverse the survivor relation;
- `reroute` when the current decision question is no longer deciding among live options but has become one selector-result declaration, publication-availability, or enactment problem that only borrowed order-effect language rhetorically.

Do not promote this line to the unmarked default unless those repaired limitations are live in the case.

Do not invoke this line merely because a case feels psychologically subtle. Invoke it when one changed order, framing, response pattern, or incompatible-question structure changes the comparison state or the survivor relation in the live choice.

Use the evidential comparison when its dependence assumptions suffice for the decision. If two approaches recommend different options, identify the assumption responsible and what could decide between their uses.

These approaches can model the same choice under different assumptions. A causal or order-sensitive model may reverse a recommendation. To claim that one model strictly refines another, compare their feasible possibilities for the same inquiry and interpretation under B.5.MR. Establish what the second preserves and which previously possible answer it excludes.
#### C.11:4.4 - Reroute as soon as the question stops being local choice

Use `C.11` while the question remains: from this current `OptionSet`, what should the `DecisionSubject` choose, and is another probe worth its cost before commitment?

A completed `ChoiceResult` answers the local comparison. Return it to the continuation that needs it, preserving the evidence, information and action conditions used in the choice. Under **C.43**, a changed goal, available means or later observation can reopen the appropriate contribution without requiring the whole control task to become one fixed option set. The local next-probe rule below is not a general solution for all sequential information acquisition.

Reroute immediately when the question changes:

- If the current rows are labels or fragments and the question is how several complete ways could obtain the same result, leave this pattern and work in `C.38` first.
- If a way to obtain the result still needs explanation, use `C.39`. If usable material needs feasible variation and examination, use `C.40`. Use `C.18` when the question concerns the generation account or archive/front stewardship.
- If the options already exist but the question is how broadly to keep exploring or exploiting the candidate pool, leave this pattern and work in `C.19`, where the next useful output is one explicit pool-policy result rather than one local `ChoiceResult`.
- If one option is already chosen and the question is how to sequence, budget, or enact that choice, leave this pattern and work in `C.24`, where the next useful output is one enactment-facing call plan or `CheckpointReturn`.
- If the question has shifted from deciding to declaring or naming selector-facing selected-set content, leave this pattern and work in `G.5`. Its next useful output may be a `Shortlist` or `RankedShortlist` when alternatives remain for later choice, a `JointUseSet` when every named member is included for one bounded use, a narrowed handoff, abstain, or escalation. None is one more local `ChoiceResult`.

  If that result already exists and the current question is presentation or availability to an audience, use `E.17` for the source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

`ProbeBudget` covers the resources available for further observation or deliberation while the choice or reliance on it can still change. `ValueOfInformation` and `ValueOfComputation` express the expected improvement compared with deciding now. Once the choice and its permitted use are settled, the budget for performing or sequencing the selected work belongs to C.24. C.19 and C.24 may use these measures in their own decisions.

Outside this pattern remain candidate generation, pool-wide exploration policy, selector-facing set-result declaration, publication availability, and execution planning.

#### C.11:4.5 - Minimal inventory and mathematical floor

The minimum usable inventory for this pattern is:

- subject and option objects: `DecisionSubject`, `DecisionSubjectGranularity`, `OptionSet`;
- evaluative and epistemic objects: `PreferenceOrder`, `EvaluativeMeasure`, `BeliefState`, `OutcomeModel`;
- dependence and comparison objects: `InterventionModel`, `CounterfactualModel`, `SubjunctiveDependenceRelation`, `ChoiceRule`, `ChoiceResult`;
- probe and bounded-resource objects: `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`.

The applicable objects from this inventory are required because the decision record must carry one explicit path from the `OptionSet` through the `ChoiceRule` to the emitted `ChoiceResult`.

##### C.11:4.5.1 - Always explicit versus conditionally activated objects

A completed `C.11` decision record makes the following objects explicit. For a comparison sent while the decision is open, identify the usable premises and the missing basis under §4.2.4.

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
- For a live inquiry, identify its `ProbeActionSet`, `ProbeBudget` and `CostToProbe`. Use `ValueOfInformation` for new observations, `ValueOfComputation` for additional reasoning over available evidence, or both when the inquiry needs both.

Use these names or ordinary wording that makes the applicable objects and their roles in the comparison recoverable.

Immediate lexical commitments:

- the default chooser term is `DecisionSubject`, not `Agent`;
- `DecisionSubjectGranularity` identifies the unit to which the decision is attributed. A committee may decide for itself or on behalf of an organization under a mandate. Where scale matters, identify the actual part and whole. B.5.MR compares the levels of abstraction or refinement of two models for a given inquiry; the same chooser can use both models.
- use `A.6.P` if a relation's predicate or participants remain unclear, and `A.6.5` when its argument or slot structure needs clarification.

Local plain glosses for the load-bearing inventory:

- `DecisionSubject`: the system making the decision, which can be a person, an automated controller, a committee or another organized body;
- `DecisionSubjectGranularity`: the unit to which the choice is attributed in this arrangement. A committee member can submit an individual ranking and the committee can decide by vote;
- `OptionSet`: the concrete options already on the table now;
- `PreferenceOrder`: the current better-than / worse-than ordering over those options for this decision subject;
- `EvaluativeMeasure`: the explicit utility-style or desirability-style scoring measure used when the case needs magnitudes, thresholds, or trade-offs rather than only one ordering;
- `BeliefState`: the current uncertainty-bearing state about the world, the case, and the likely consequences of the options;
- `OutcomeModel`: the model that maps options plus the current uncertainty picture to the consequences that matter for this choice;
- `InterventionModel`: the part of the model that says how the world changes because one option is actually taken;
- `CounterfactualModel`: the model used to compare relevant non-actual alternatives or alternate decision procedures;
- `SubjunctiveDependenceRelation`: the dependence between this choice and one predictor, one linked chooser, or one structurally similar decision procedure when intervention talk alone is not enough;
- `ChoiceRule`: the rule for evaluating the current alternatives and any worthwhile probe, and for reaching one of the four result forms;
- `ChoiceResult`: the disposition that follows from applying that rule, with the grounds the receiving use needs;
- `ProbeActionSet`: checks, measurements, simulations or questions available while the choice or its warranted use can still change;
- `ProbeBudget`: the money, time, attention or delay available for those inquiries;
- `CostToProbe`: the resources an inquiry would consume, including the work or benefit displaced by its delay;
- `ValueOfInformation`: the expected improvement in the decision from using the possible observation results, compared with choosing on what is known now;
- `ValueOfComputation`: the expected improvement in the decision from performing the proposed additional computation. Compare either gain with the inquiry’s cost on the same basis and count that cost once.

A person may make a decision, an organization may decide by an agreed procedure, or an automated controller may choose under delegated limits. An analyst, AI assistant or tool can also supply comparisons while another party decides. Identify the actual arrangement before attributing the decision.

This floor is enough to keep choice doctrine inspectable and stable. It does not yet assume one full branch-specific quantum-like package or one cross-scale geometry-heavy package.

##### C.11:4.5.2 - Boundary on multilevel and social-expectation doctrine

`DecisionSubject` and `DecisionSubjectGranularity` identify who makes the choice and whether it is an individual or collective decision. Several participants can contribute evidence or carry out the chosen course. Attribution to a larger system requires grounds for its decision, such as a collective rule or an authorized delegate acting within a mandate. When the parties retain separate authority, report their individual decisions and what those decisions settle together. A recommendation or its circulation leaves open whether the parties accepted it.

This minimal choice doctrine does not fully settle the broader questions that can accompany that chooser-bearing scope, including:

- collective aggregation doctrine over conflicting preferences or criteria;
- conflicts between the objectives of a participant, a group and a containing organization whose decisions are linked in this case;
- one full `ROE` or social-expectation structure for socially scaffolded choice;
- one full multilevel or geometry-heavy formal package for those cross-scale or cross-collective questions.

If one of these questions matters to the choice, retain the unresolved aggregation, social-expectation or multilevel premise and obtain its needed support. The local choice record alone does not settle it.

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

The result is usable when `ChoiceResult` follows from the stated comparison basis, `ChoiceRule` and any applicable probe decision value.

A `C.11` pass is finished enough for practical use when all three conditions hold:

- the current comparison basis is explicit enough to explain the stated `ChoiceResult`: why an option or tie-set survives, no current option survives, or probing or rerouting is needed;
- any live inquiry alternative has been resolved sufficiently to support the choice, and the result retains any inquiry reason or limitation needed by this decision or its recipient;
- the next question is explicit: `choose now`, `reject current set`, `probe again`, or `reroute`.

An inactive inquiry item adds no placeholder or omission account to this tuple or finish condition.

If the current rule leaves alternatives tied or incomparable, report which and what that means for the receiving task. A result that retains several eligible options can supply a request for a set. Choosing one of them requires a rule or a decision by the designated chooser.

If those conditions are missing, retain the unfinished comparison and identify the premise or decision still needed.

### C.11:5 - Archetypal Grounding

#### C.11:5.1 - System grounding

**Tell.** A research team already has three experiment plans on the table. The option set exists. The question is to decide which plan to run and whether one more measurement is worth the delay.

**Comparison.** The team can choose among three feasible plans. It first minimizes the predicted number of missed defects per 100 reference cases. It breaks ties by schedule. Its current estimates use two equally likely calibration states.

| Calibration state | Plan A | Plan B | Plan C |
| --- | ---: | ---: | ---: |
| First | 4 | 2 | 5 |
| Second | 6 | 5 | 3 |

On this basis, A averages 5 misses, B averages 3.5 and C averages 4. If the team must choose now, its rule selects B.

**Probe.** A one-day calibration run can identify the state before the plan is fixed. The team could then choose B in the first state and C in the second, for 2.5 expected misses per 100. The improvement over choosing B now is one expected miss per 100. The day fits the budget, and the team judges that avoiding this loss is worth the delay.

**Result.** The current `ChoiceResult` is `probe again`. Once the run identifies a state, apply the comparison in that row. If the run becomes unavailable while the estimates and rule still hold, B remains the supported choice on the present evidence.

**Show.** Use `C.38` if the team must turn labels or fragments into complete ways of obtaining one result. Use `C.39` if a plan still lacks an explanation of how to obtain that result, or `C.40` if the team can vary a plan and needs to examine the difference. Use `C.18` when the team needs a generation account or archive/front claim; `C.19` for exploration policy over the plan pool; and `C.24` for the run sheet and execution order after choice.

#### C.11:5.2 - Episteme grounding

**Tell.** A planning team has three models for predicting restart delays. It needs one forecast for the staffing decision due tomorrow. For this use the team judges a model by its mean absolute timing error on comparable held-out shifts.

**Comparison.** Under the agreed mix of shifts the three models miss restart time by 6, 3 and 5 minutes on average. All three can supply the forecast in time. The current comparison supports model 2. Choosing it for staffing does not establish which mechanism caused the delays.

**When another comparison matters.** Suppose tomorrow’s roster includes a previously unrepresented shift. Applying all three models to the same set of comparable logged shifts could change their order. Check whether those logs can be obtained before the roster is fixed and whether the resulting change in staffing would justify the effort.

**Result.** For the original mix, choose model 2 on its lower error. For the changed mix, return `probe again` if the log comparison is feasible and worth doing. If the logs are unavailable and the previous order cannot be supported for the new mix, report that limit to the planner.

**Show.** This pattern governs neither open-ended hypothesis generation nor operational rollout. Those questions stay outside this pattern even when the decision later feeds them.

#### C.11:5.3 - Collective and contextual grounding

**Tell.** A clinical board must decide whether to escalate a patient now or order one more test. The board is the chooser, not one isolated individual, and the result shifts when the case is discussed in prognosis-first versus risk-first order.

**Show.** `C.11` keeps the case legible by typing the chooser as one `DecisionSubject` at explicit `DecisionSubjectGranularity`, keeping the available actions as one current `OptionSet`, keeping one explicit `BeliefState` and `OutcomeModel` around those actions, and asking whether another test belongs in the `ProbeActionSet` with enough expected value to justify its `CostToProbe`.

**Show.** The changing patient state and the board's update process matter when they change feasible actions or estimated consequences. The observed order effect requires an explicit comparison-order account. Neither collective choice nor an order effect alone establishes that active-inference or quantum-like formalism is needed; use a branch only for the remaining limitation it addresses.

**Show.** If the order effect still changes which option survives, the comparison should say that directly and keep the comparison unfinished. The next comparison move is then either one framing-stabilizing probe or declaring the comparison order under which the current result will be judged. The record should identify that comparison instability instead of describing it only as mixed intuitions.

**Show.** An admissible output here therefore looks like one of three concrete records:

- `ChoiceResult = probe again with a comparison under both stated question orders because it can distinguish a missing prognosis premise from a framing-dependent ranking; the expected decision gain justifies the feasible delay`;
- `ChoiceResult = choose now and escalate because the receiving decision accepts the declared risk-first comparison, and no further feasible test offers enough expected decision gain to justify the harmful delay`;
- `ChoiceResult = reroute to C.24 because the board has already chosen escalation and the next task is now treatment sequencing rather than local choice`.

**Show.** Record which comparison the board used, its conclusion and whether the board acted on it. When the ranking still depends on an unresolved framing choice, retain that uncertainty.

### C.11:6 - Bias-Annotation

This pattern is intentionally biased toward `Prag` and `Onto/Epist` discipline.

It prefers a clear decision-theory EntityOfConcern, an explicit neighboring-question split, and a minimal mathematical floor over a less constrained notion of rationality that allows more variation in its formulation.

That bias can feel too strict when the chooser, option set, or dependence structure is still changing. Address this by keeping the unfinished state explicit, rather than broadening the pattern into a general rationality account: retain a tie-set, a `probe again` result, or state the neighboring subject pattern that governs the question.

The family map also remains plural: causal, success-first, active-inference, and quantum-like repairs stay visible without being overpromoted into one default doctrine.

### C.11:7 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| `CC-C11.1` | A comparison **SHALL** use already-available options; when complete ways or new candidates still need construction, use their governing pattern first. | Keeps candidate construction and development outside local choice. |
| `CC-C11.2` | Identify who makes the choice and whether it is attributed to an individual or to an organized whole. A precise agency claim **SHALL** be governed by `A.13`. Measured characteristic and evidence claims retain their `A.17`–`A.19`, `C.16` and `A.10` grounds. | Makes the attribution of the choice inspectable. |
| `CC-C11.3` | When the question leaves local choice, the result **SHALL** identify the receiving question under §4.4, including candidate construction/development, pool policy, enactment or selector-facing result declaration when applicable. | Separates choice from candidate construction and development, the generation or archive/front account, pool policy, planning, and selector-facing result declaration. |
| `CC-C11.4` | A completed comparison **SHALL** identify the chooser, options, comparison basis, applicable dependence assumptions, any live probe decision, `ChoiceRule` and the `ChoiceResult` it supports. An open comparison identifies what the holder can use now and what still prevents closure (§4.2.4). | The recipient can use the result at the strength the available grounds support. |
| `CC-C11.5` | The comparison **SHALL** identify the applicable objects in §4.5.1, preserving its always-required versus conditionally activated distinction. | Keeps the objects of the calculus explicit. |
| `CC-C11.6` | Load-bearing terms in a decision record **SHALL** have recoverable meanings, using the local glosses or an explicit equivalent interpretation. | Prevents the core terminology from remaining implicit or displaced into outside basis carriers. |
| `CC-C11.7` | When a relation predicate or participant remains unclear, use `A.6.P`; when argument or slot structure remains unclear, use `A.6.5`. An already clear relation uses its governing rule directly. | Keeps dependence language inspectable and deconflicted. |
| `CC-C11.8` | An active-inference or quantum-like branch **SHALL** address a stated limitation of the current comparison; the branch name alone supplies no support. | Preserves practical meaning and avoids branch-name citation without operational load. |
| `CC-C11.9` | A local choice result **SHALL** remain distinct from any separately needed quantum-like, aggregation or multilevel formal support. | Keeps the pattern usable now while leaving heavier support work typed and explicit. |
| `CC-C11.10` | Use `ProbeBudget` for inquiry while the choice or reliance on it can still change. Apply the relevant information or computation value. Once the choice and its use are settled, resources for performing the chosen work belong to execution planning. | Identifies which decision the inquiry informs. |
| `CC-C11.11` | When the question shifts to declaring selector-facing set content, use `G.5`. For presentation or availability of an existing result, use `E.17` for its publication face and source return, and `E.24.PUB` for the publication occurrence and availability. | Preserves the boundary among local choice, selector-result declaration, and publication availability. |
| `CC-C11.12` | When a further dependence layer or neighboring family is used, the comparison **SHALL** state the limitation it addresses and the resulting change in the comparison. | Prevents branch-name citation from replacing use-time doctrine. |
| `CC-C11.13` | The result **SHALL** justify `choose now`, `reject current set`, `probe again` or `reroute` under the closure conditions; an unresolved comparison **SHALL** remain explicit. | Prevents the decision record from ending without a justified choice result. |
| `CC-C11.14` | The decision record **SHALL** make the chooser, option set, comparison basis, `ChoiceRule`, conditionally required inquiry content and `ChoiceResult` recoverable. Each result branch **SHALL** retain the content specified in §4.2.3. An inactive inquiry item creates no placeholder or omission record. | Keeps the pattern usable as one working decision record rather than one doctrinal memo. |
| `CC-C11.15` | If a `ChoiceResult` is supported by a causal effect, counterfactual comparison, causal policy, or off-policy causal evaluation claim, it **SHALL** carry `ChoiceResult.causalUseSpec?` with the target rung, claim kind, relevant support-component refs, support-result ref when consumed, supported use, and unsupported use. | Prevents decision-theory vocabulary from certifying causal-use support. |

### C.11:8 - Common Anti-Patterns and How to Avoid Them

A result is usable when its recipient can recover the choice and the grounds on which it follows.

| Anti-pattern | Symptom | Why it fails | How to avoid / repair |
| --- | --- | --- | --- |
| Candidate-formation or search takeover | The text starts constructing complete ways or generating options as if that work were already part of decision doctrine. | The choice rule has no stable option set to compare. | State the existing option set. Use `C.38` for same-result way formation, `C.39` for a missing explanation of how to obtain the result, or `C.40` for feasible variation and examination. Add `C.18` when a generation account or archive/front claim is needed. |
| Policy collapse | Exploration or exploitation governance over a candidate pool is written as if it were identical with choosing among current options. | Choice doctrine and candidate-pool policy become indistinguishable. | `C.19` remains explicit as the neighboring pattern for selection policy and exploration governance. |
| Planning collapse | Sequencing, replanning, and enactment budgeting are written as if they were already part of the choice calculus. | Planning-side question moves out of `C.24` by accident. | Execution order and operational budgeting remain in `C.24`, even when `C.11` says more probing is rational. |
| Inventory without decision rule | The current comparison names many objects and schools but never shows how to move from a live option set through one `ChoiceRule` to one `ChoiceResult`. | The pattern becomes a survey rather than one decision discipline. | State one explicit decision-record shape: chooser, option set, comparison basis, dependence layer, applicable probe-worthiness test, one explicit doctrine, and one emitted result. |
| Hidden basis shift | Different options are compared under different belief states, outcome models, or dependence layers without one explicit statement that the basis changed. | The comparison looks precise, but its choice rule cannot be audited. | Keep one shared comparison basis until one named probe or model change updates it, and state explicitly when the dependence layer changes. |
| Missing grounds for closure | The record ends the comparison or selects an option without showing why. | The recipient cannot distinguish a justified choice from the exhaustion of time or budget. | Show which disposition follows from the rule. For a selected option, give the comparison that supports it. |
| Undefined load-bearing terms | Terms such as `PreferenceOrder`, `BeliefState`, or `OutcomeModel` appear without local operational clarification. | Core comparison objects stay implicit and the decision question depends on outside theory or undocumented assumptions. | Give one local plain gloss or equivalent operational clarification for each load-bearing term used in the pattern text. |
| Bounded-resource bridge loss | `ProbeBudget`, `ValueOfInformation`, or `ValueOfComputation` are mentioned, but the text silently lets `C.19` or `C.24` own them. | The theory-side doctrine disappears into neighboring policy or planning prose. | Keep those objects theory-side in `C.11`; let neighboring patterns consume their outputs without minting the concepts. |
| Result-boundary collapse | The text treats declaring selector-facing set content, or later making it available, as if either were identical with deciding. | Choice doctrine silently absorbs the `G.5` result question or the publication question. | Keep both outside `C.11`: use `G.5` to declare the selector-facing result, `E.17` for its publication face and return to source, and `E.24.PUB` for the publication occurrence and availability. |
| Mistaken attribution | An adviser, implementer or tool that supplied a ranking is treated as the chooser. | Participation alone leaves the decision arrangement open. | Identify the actual `DecisionSubject` and use `DecisionSubjectGranularity` for the individual or collective attribution. |
| Prestige-branch citation | Active inference or quantum-like work is cited only as one fashionable name. | The text sounds current without stating what limitation is being repaired. | The repaired limitation is stated directly: embodied online updating for active inference, and context or order effects for quantum-like lines. |
| Cost-free deliberation | The text speaks as if probing and computation are free. | Bounded-resource doctrine disappears behind one idealized choice moment. | `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` stay visible in the calculus. |

### C.11:9 - Consequences

| Benefits | Trade-offs / Mitigations |
| --- | --- |
| Keeps decision doctrine distinct from search, candidate-pool policy, and planning. | The same working episode now needs an explicit question split across choice, pool policy, and planning rather than one blurred rationality account. |
| Makes evidential, causal, and subjunctive branches comparable in one place. | The pattern becomes more explicit about dependence language and therefore needs tighter lexical discipline. |
| Keeps bounded-resource probing inside the doctrine rather than as one afterthought. | Fast-path use now carries a slightly richer inventory before the doctrine feels natural under pressure. |
| Keeps active-inference and quantum-like repairs visible without letting them silently replace the whole core. | Those lines stay load-bearing only when they change the actual `ChoiceResult`, unfinished state, or reroute logic; heavier formal packages still remain outside this body. |
| Gives the recipient the choice and its basis. | A decision record must distinguish the reason to select an option from the reason to stop investigating it. |
| Makes downstream work cleaner because search, pool policy, publication, and enactment can receive one explicit output instead of one blurred upstream "decision happened" claim. | Reroutes now require one named next subject pattern and one reusable part of the record instead of one vague upstream claim that deliberation happened somewhere. |
| Keeps an unfinished comparison explicit through a tie-set or `probe again` result instead of forcing an unsupported winner. | Some outcomes will look less decisive because they state that the comparison is unfinished. |

### C.11:10 - Rationale

A live option set and a live choice among that set are not the same question as generating options, governing a candidate pool, or sequencing execution. Keeping that distinction explicit is what makes the doctrine usable rather than ceremonial.

`DecisionSubject` covers a person, a technical system or an organized body for the particular decision. Use `A.13` when a claim about agency itself needs examination.

A minimal mathematical floor is necessary because choice doctrine without one stable object stack quickly turns into verbal drift. But a pattern also fails if it keeps only the object names and never shows how those objects discipline an actual choice. That is why `Solution` here is procedural: it must carry the path from `OptionSet` through one `ChoiceRule` to one `ChoiceResult`, including the stop-or-probe decision, rather than only one survey of neighboring theories.

The receiving work can use the selected option, retained alternatives or next probe together with the grounds and limits of that choice.

At the same time, this pattern should not treat a full quantum-like or geometry-heavy package as settled merely because those neighboring lines exist.

### C.11:11 - SoTA-Echoing

| Claim | SoTA practice | Primary source | Alignment with `C.11` | Adoption status |
| --- | --- | --- | --- | --- |
| Decision theory still needs an explicit classical baseline over options, preferences, utility, and uncertainty. | Contemporary reference treatments still present decision theory through option sets, preferences, utilities, and uncertainty as the baseline language of rational choice. | [Decision Theory (Stanford Encyclopedia of Philosophy, Fall 2023)](https://plato.stanford.edu/archives/fall2023/entries/decision-theory/) | `C.11` adopts this as the baseline vocabulary for choice among already-available options. | **Adopt.** |
| Evidential dependence is not enough in all cases. | Causal decision theory remains the standard repair when intervention structure matters. | [Causal Decision Theory (Stanford Encyclopedia of Philosophy, Winter 2024)](https://plato.stanford.edu/archives/win2024/entries/decision-causal/) | `C.11` keeps one explicit evidential-versus-causal split rather than one blended correlation claim. | **Adopt.** |
| The field extends beyond the older EDT/CDT split. | Functional or success-first work keeps subjunctive dependence live in Newcomb-like and related cases. | [Functional Decision Theory: A New Theory of Instrumental Rationality](https://arxiv.org/abs/1710.05060) | `C.11` keeps success-first or subjunctive repair visible without treating it as one settled default doctrine. | **Adapt.** |
| The live EDT/CDT/FDT family map now has more technical comparison structures than one older philosophical split alone. | Recent mechanized or causal-graph taxonomies compare live decision-theory families through more explicit technical structures rather than only a dispute over names. | [Mechanized-causal-graphs taxonomy of decision theories (2023)](https://arxiv.org/abs/2307.10987) | `C.11` therefore treats EDT, CDT, and success-first or FDT-like lines as technically live family options. | **Adapt.** |
| Decision under bounds must account for probing and deliberation cost. | Current metareasoning and optimal-experimental-design lines treat information acquisition, probing, and computation allocation as first-class theoretical questions rather than free background steps. | [Metareasoning: Theoretical and Methodological Developments](https://pmc.ncbi.nlm.nih.gov/articles/PMC11765846/) | `C.11` therefore keeps `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` inside the doctrine rather than assigning them only to planning; the current closure rule is local or myopic over the next feasible probe, with richer sequential or non-myopic `OED` left as later strengthening. | **Adapt.** |
| Decision and update can be embodied, online, and socially coupled. | Active-inference work treats decision as tightly coupled to action, inference, and expectation regimes rather than one disembodied one-shot selection. | [Embodied decisions as active inference](https://pmc.ncbi.nlm.nih.gov/articles/PMC12201680/) | `C.11` carries this as one neighboring repair of the chooser picture, makes social-expectation pressure explicit enough for use-time reroute or probe logic, and states that full `ROE` or social-expectation object modeling remains outside this local choice body. | **Adapt.** |
| Some decision cases exhibit context effects, order effects, response-replicability tension, and incompatible-question structure. | Current quantum-like decision and cognition work treats those cases as one measurement-sensitive research program rather than an automatic physics transfer. | [Measurement-theory decision/cognition anchor (2025)](https://arxiv.org/abs/2503.05859) | `C.11` carries this as one named neighboring branch where those limitations occur, while leaving heavier branch-specific formalism outside this body. | **Adapt.** |
| Incompatible question/context structures need a more specific cue than "context matters." | Contextuality-by-Default treats same-content-looking measurements in different contexts as distinct random variables unless an admissible joint treatment is supplied. | [Contextuality-by-Default](https://www.sciencedirect.com/science/article/abs/pii/S0022249616300207) | Use CbD as the formal cue when question/context structure changes variable identity, joint availability, or admissible comparison inside the current option set. | **Adopt/Adapt.** |
| Some quantum-like lines also claim one practical representational gain from linear state dynamics over harder nonlinear underlying processes. | Quantum-like modeling in biology presents linear Hilbert-space dynamics as one simplifying and potentially faster information-processing lens over nonlinear classical biophysical dynamics, while treating this as representational modeling rather than proof that the modeled system is physically quantum. | [Quantum-like modeling in biology with open quantum systems and instruments](https://www.sciencedirect.com/science/article/pii/S0303264720301994) | `C.11` takes this only as one possible practical reason to keep the quantum-like branch available when measurement-sensitive effects occur; it does not treat quantum-like choice as one claim of physical quantumness. | **Adapt cautiously.** |
| Broader contextual and multilevel lines pressure decision texts to keep one typed substrate rather than pure verbal drift. | Current multilevel-learning and evolution-as-inference work argues for one shared formal lens across levels even when the heavier final geometry is still unsettled. | [Multilevel selection as Bayesian inference, major transitions in individuality as structure learning](https://royalsocietypublishing.org/doi/10.1098/rsos.190202) | `C.11` therefore keeps one minimal typed floor and one wider chooser-bearing scope while stating by value that full aggregation doctrine, cross-scale or cross-collective conflict doctrine, and heavier multilevel mathematics remain outside this local choice body. | **Adapt.** |

Practical reading of this alignment:

- In ordinary current-option cases, start with the classical evidential baseline and use it to emit one explicit `choose now`, `reject current set`, `probe again`, or `reroute` result under one shared `BeliefState` and `OutcomeModel`.
- Failure of a simple Bayesian or passive-read-like model is not yet evidence that QL is necessary. Try richer classical, causal, performative, instrument, active-sensing, or representation-abstraction rivals before keeping the QL branch as load-bearing.

- If intervention structure changes the survivor relation, state that explicitly and switch to causal comparison rather than treating it as a correlational comparison.
- If predictor-coupling or structurally linked choice procedures remain load-bearing, keep the subjunctive layer visible and say what linked structure could still reverse the current result.
- If another measurement, comparison pass, or search pass is being considered, treat its value and cost as part of the current decision doctrine rather than assigning them only to later planning.
- If the chooser is embodied, online, and socially coupled, or if context and order effects change the comparison state, keep those repaired limitations visible by naming the observation, social-expectation clarification, order stabilization, response-replicability check, or measurement-class clarification that could still change the current `ChoiceResult`.

  In those cases, state when fuller `ROE`, quantum-like state-space, or multilevel doctrine still sits outside this local choice body.
- If the quantum-like line is activated, treat it as one measurement-sensitive mathematical lens or representational repair, not as one claim that the chooser or world is physically quantum.
- If none of those heavier repaired limitations is live, stay with the lighter branch rather than adding a branch label that does not change the next action.

### C.11:12 - Relations

C.11.MV constructs a Method-option worth comparison, preserving the receiving result, present alternative, learning and transition effort, recurring support and distribution of burden. It uses this choice discipline and C.11.DUA where a demanded inquiry or requirement itself needs appraisal.

- **Builds on:** `A.6.P`, `A.6.5`, `A.10`, `A.13`, `A.18`, `A.19`; **coordinates with:** `E.10.LRN` for learning-word recovery, `C.11.CRC` for a missing finite configuration-relative comparison claim, `C.17` for bounded characterization
- **Read next when candidate work is needed:** `C.38` for forming complete ways of obtaining one result, `C.39` for a missing explanation of how to obtain it, or `C.40` for feasible variation and examination of usable material. Use `C.18` when generation-account or archive/front claims are needed.
- **Other neighboring questions:** `C.19` for one explicit pool-policy result over exploration or exploitation governance; `C.24` for one enactment-facing call plan or `CheckpointReturn`; `G.5` for the selector-facing result kind for the receiving use—retained alternatives, all-member joint use, narrowed handoff, abstain, or escalation; and `C.28` when the choice result depends on causal-use support
- **Keeps outside:** candidate generation, pool-wide exploration or exploitation policy, selector-facing set-result declaration, publication availability, and execution sequencing
- **Aligns with:** classical evidential decision theory, causal decision theory, success-first or subjunctive repair, bounded-resource metareasoning and probe-cost doctrine, `C.28` causal-use question/rung/support vocabulary, active-inference-adjacent decision work, quantum-like contextual repair where context or order effects occur, and multilevel mathematical-lens pressure at the minimal-floor level only

### C.11:12a - Quantum-like choice-boundary note

Use C.11 first when the question is local choice, belief, preference, comparison, question order, option-menu framing, or an incompatible-question effect inside one decision situation. Quantum-like wording is retained only when it adds a concrete residual order-effect, probe, frame, or comparison reading that ordinary decision or probability language would hide.

Decision repair sequence:

1. State the current `DecisionSubject`, `OptionSet`, comparison basis, and `ChoiceRule`.
2. Ask whether the apparent QL issue changes the local choice result: choose now, reject current set, probe again, or reroute.
3. If the issue is question order, incompatible questions, response-replicability tension, non-shared comparison frames, or CbD-style variable identity / joint-availability trouble inside the current option set, keep the QL repair inside C.11.
4. If the current option set itself is suspect, incomplete, generated by the wrong frame, or still needs expansion/reframing/search, leave C.11. Use `C.39` for a missing explanation of how to obtain the result or `C.40` for feasible variation and examination of usable material. Use `C.18` when a generation account or archive/front claim is needed; `C.19` for live-pool policy; `A.19` for the declared CharacteristicSpace or reusable predicate; or `B.5.2` for abductive hypothesis formation, according to the question that needs repair.
5. If the issue changes boundary state, bridge/export faithfulness, coordinated-work evidence, measurement admissibility, or viability envelope, apply the pattern governing that claim.
6. Emit one `ChoiceResult` and one next question; do not leave the QL branch as a theory label.

When the question leaves local choice, apply the subject pattern instead of stretching C.11:

| Question that appears in the decision case | First pattern |
| --- | --- |
| Boundary interaction, API read, workshop, dashboard, or message changes the represented state | `C.26.1` only for the remaining state or probe question, with `A.6`, `A.6.B`, and `A.6.P` still active |
| Cross-context export, translation, or same-label comparison loses state or comparability | Use the direct source/use rule; apply `F.9` when the use requires correspondence between different local senses. |
| Coordinated work evidences a state no report faithfully carries | `A.15` plus evidence patterns, with `C.26.2` only for the remaining low-recoverability distributed-state reading |
| Measurement, metric, survey, or score frame changes the represented state | `C.16` plus evidence patterns |
| Viability envelope, adaptation cost, or boundary-maintenance decision is load-bearing | `C.25` for a quality bundle with several differently typed contributors; `C.26.3` for a multi-characteristic viability envelope under disturbance when a candidate intervention, boundary condition, adaptation cost, or failure mode matters. Add `C.26` for a remaining probe/export/frame/coarsening question only when an exact contextual-model obstruction still changes what may be inferred or done after the ordinary patterns have carried their part. |
| Current option set is suspect, incomplete, frame-generated, or still being expanded/reframed/searched | Use `C.39` for a missing explanation of how to obtain the result or `C.40` for feasible variation and examination of usable material. Use `C.18` when a generation account or archive/front claim is needed; `C.19` for live-pool policy; `A.19` for the declared CharacteristicSpace or reusable predicate; or `B.5.2` for abductive hypothesis formation, according to the question that needs repair. |

Useful outputs:

- `choose now` under a declared order/frame;
- `probe again` because another question order, response-replicability check, or frame test could still change the survivor relation;
- `reroute` because the live problem is no longer local choice;
- no QL wording when ordinary uncertainty, preference conflict, or option-generation work is enough.

C.11 may cite `C.26` as the common quantum-like modeling lens only for the residual question after the local-choice split is applied. It is not the whole-cluster pattern for boundary, bridge/export, distributed-evidence, viability, or state-representation coarsening claims.

### C.11:12b - C.29 mathematical-lens use relation

> `C.29` may supply a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note that a decision record can cite. If the output is a `ChoiceResult` or local choice record, use `C.11` to state and test the decision. Any `G.5` selector-result declaration and `G.9` benchmark result remain separate. When one of those results must be available to an audience, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability. `C.29` does not select the option by mathematical elegance.

### C.11:End
