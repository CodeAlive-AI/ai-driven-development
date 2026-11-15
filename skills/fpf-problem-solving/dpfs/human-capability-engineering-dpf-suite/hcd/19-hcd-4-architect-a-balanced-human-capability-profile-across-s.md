## HCD.4 — Architect a Balanced Human Capability Profile Across Simultaneous Work

> **Type:** Human Capability Development practitioner profile-and-choice pattern
> **Status:** Stable


### HCD.4:0 - Use This When

Use this pattern when one named person's later Work requires several contributions at once and the person, a practitioner or a manager needs a comparison of those contributions or a decision about what to preserve, investigate, defer or develop. Begin with a compatible HCD.1 demand account or equivalent qualified scope and compare the evidence for each required contribution.

With compatible scope and evidence, return a **condition-qualified human capability profile**. Explain which contributions are supported, where they interact, and any priority, gap, trade-off or uncertainty that matters to the receiving question. Give a recommendation when requested. For a bounded choice, apply the `C.11` requirements in §4.4. If a required input is missing, keep the comparison and any recommendation it supports. Return `profile-decision-blocked` for the affected conclusion, specifying the missing input and the condition for reconsideration.

The profile shows which contributions to preserve and where a limitation or uncertainty affects the work. Use `HCD.1` when the demand frame is missing. Use `HCD.3` when the limiting cause or target is unresolved. A separate programme comparison (`HCD.2`) may use the profile; HCD.4 neither requires nor invents a programme.

A mastery claim needs evidence of the person’s performance under the required conditions. A claim that the person learned or changed needs evidence across occasions. Use the appropriate professional work and authority for curriculum, provider, employment, safety, legal, clinical or release decisions and for directing ongoing Work. For a decision that was made, identify who made it and whether they had the authority required for that choice.

When choosing learning opportunities requires more than a current–target comparison, also construct a **local qualitative model of proficiency** using §§4.2.1–4.3.1. It describes possible ways of acting or reasoning, the conditions that distinguish them, and testable hypotheses about how one might develop into another. Its distinctions and proposed transitions can guide teaching tasks and observations in HCD.6. A supported comparison or preserve-or-prioritize decision can finish without constructing this additional model.

#### HCD.4:0.1 - Working Terms

| Name in this pattern | What it denotes |
| --- | --- |
| capability claim | One condition-qualified claim about a human contribution or interface needed in representative later Work. Identify the required contribution and conditions even if the evidence includes a course result or score. |
| current profile | The set of supported current claim dispositions for one human holder, configuration, conditions, evidence window, and date. |
| target profile | The set of intended claim dispositions justified by representative later Work. Whether the person has attained them requires observations. |
| intermediate state | A proposed way of acting or reasoning that may be useful between a current and target contribution. Its place and attainability need grounds; a convenient middle row establishes neither. |
| local qualitative model | A revisable account of distinguishable ways of performing a bounded contribution and their relations. A person's current profile locates supported claims within that account, with uncertainty; the account is not the person's actual condition. |
| learning progression | A model of possible qualitative development under specified instructional and task conditions, with supporting evidence and unresolved relations. A newly proposed progression remains a hypothesis. |
| learning pathway | A selected, revisable plan of learning opportunities, tasks and help for a person. HCD.2 and HCD.6 can use a progression to select relevant opportunities. |
| learning trajectory | The recorded history of attempts, help, feedback, observations and supported changes for a person. It may diverge from the selected pathway and reveal defects in the model. |
| profile difference | The claim-by-claim current-versus-target comparison, including preserved strengths, gaps, uncertainty, support dependence, critical errors, and trade-offs. |
| bounded profile decision | A `C.11` choice over an already-available option set, supported by the profile comparison and kept separate from authorization, commitment, and later Work. |
| profile-decision-blocked | A substantive return naming a missing value required for the affected conclusion—scope, evidence, chooser, option, comparison, applicable inquiry input, participation or authority—and its retry condition. |
| simultaneous Work | Representative Work whose contributions or interfaces coexist, overlap, recur, or constrain one another; printed order does not make them a sequence or hierarchy. |

Current and target profiles describe supported and intended contributions. A profile difference compares those descriptions, and an optional aggregate summarizes selected claims. A curriculum plans instruction. Keep these descriptions, comparisons, and plans separate from the person's realized learning trajectory, the Work performed in learning, and any human transformation. Claims about what happened or changed need evidence of those occurrences.

### HCD.4:1 - Problem Frame

A person can be strong in three contributions and weak in a fourth. One contribution may be safe only with a specialist return; another may be independent of a tool; a third may fail only in unfamiliar variants. A single level or average can hide the difference that affects the requested comparison or choice.

A course order can look like a capability hierarchy, a Method decomposition can look like a development sequence, an organization chart can look like a profile, and a platform prediction can look like mastery. In simultaneous Work these structures need not line up one-for-one.

A profile must therefore preserve claim identity, conditions, evidence, support dependence, uncertainty, critical-error boundaries, and trade-offs. It may inform a choice, but a choice also requires a chooser with the relevant authority, available options and a basis adequate for the choice. Inquiry values are needed when further inquiry is live under `C.11`, not as fields to complete for every choice.

### HCD.4:2 - Problem

The common shortcut is to compress unlike claims into one score and then optimize the score. The resulting decision can trade away an already-reliable safety boundary, conceal unsupported transfer, or treat assisted performance as independent human capability.

The opposite shortcut records many dimensions but never closes a practical question. The practitioner needs a comparison that identifies what to preserve, any consequential gap and the uncertainty that matters to the finding. If further work is requested, determine whether to choose, examine a remaining question, refer it or stop.

### HCD.4:3 - Forces

- A scalar is easy to compare, while claim identity, asymmetry, critical-error status, support dependence, and uncertainty may be decision-bearing.
- A staged course or Method hierarchy is easy to draw, while the way human contributions constrain one another in later Work need not follow that order or hierarchy.
- A target can guide development. Claims about the current state or an achieved change need evidence about the person.
- A platform or AI estimate may predict performance under stated conditions. Mastery of the contribution needs evidence of what the person can do.
- Self-monitoring can improve, while self-report and confidence do not establish later-Work capability.
- A recommendation helps an owner act, while the profile does not create authority, options, budget, or commitment.
- Another probe can reduce uncertainty, while probing consumes time and may itself change the holder or Work.
- Preserving every strength is attractive, while real trade-offs may move time, workload, autonomy, support, or risk.
- Human participation matters, while manager, safety, release, clinical, and employment owners retain different decisions.

### HCD.4:4 - Solution

Compare the evidence for each simultaneous contribution with what later Work requires. Explain how the contributions constrain one another, what each conclusion depends on and any trade-offs. Return the comparison. Make a choice only when the task, evidence and authority support it.

#### HCD.4:4.1 - Bind the Profile Use

Name:

1. the person whose work is in question and the basis for their participation;
2. the HCD.1 demand account or equivalent qualified scope, including later-Work family, configuration, conditions, effective horizon, evidence window, and receiving question or decision;
3. the recipient of the comparison and, where needed, the chooser and the sources of any external results or authorizations the comparison relies on;
4. the representative cases and simultaneous contribution interfaces that can change the comparison; and
5. the protected consequences, critical errors, privacy or worker-governance conditions, and stop boundaries.

If the same-holder scope cannot be recovered, return `profile-decision-blocked` for the missing demand frame. A role profile or population average alone cannot identify this person’s supported contributions.

#### HCD.4:4.2 - Build Claim Rows

For each selected capability claim, record:

| Claim field | Required content |
| --- | --- |
| contribution and interface | What the human contribution supports in representative later Work and which simultaneous contributions, tools, or specialist returns it interfaces with. |
| current disposition | Current evidence, conditions, support dependence, date, uncertainty, and any critical-error observation; `unsupported` is preferable to an invented level. |
| target disposition | The contribution and result boundary demanded by representative later Work, with its source and horizon. |
| intermediate disposition | The intermediate contribution, result boundary, and conditions, only when they help this decision. Keep a proposed next action separate from the state description. A threshold may define an intended result boundary, but a claim that it was reached needs observations. |
| discriminating evidence | The representative task or other adequate source, the observation or work product, how it supports the claim under the stated conditions, and the result or consequence the contribution must protect. |
| trade-off and conflict | What time, workload, autonomy, support, evidence burden, or other claim could be harmed by prioritizing this one. |
| next change point | Where the claim may need reconsideration, the next observation, result, decision or changed condition that could affect it or its grounds. |

Use an aggregate only when it preserves every distinction the receiving question needs, including any critical error, support dependence, uncertainty or difference between contributions. Keep the underlying rows available whenever an aggregate is used.

##### HCD.4:4.2.1 - Construct Distinguishable Ways of Acting

Use this extension when different accounts of how proficiency develops would change a learning, assessment or next-practice decision. Begin with the individual claims and representative later Work. A small model of one consequential contribution is often enough.

**Recover the action and its meaningful differences.** Use the relevant domain Method, performance or learner evidence to establish a proposed distinction. Identify what remains hypothetical if observations are missing. Ask what the person attends to, how they represent the difficulty, which alternatives they consider, what they do, and how they detect or repair a wrong result. Compare the same contribution under compatible conditions. For example, counting every incoming message and identifying distinct requests before estimating work are qualitatively different strategies, even when a particular dataset makes their totals coincide. Two arbitrary score bands need not describe different strategies.

**Write descriptions that another practitioner can discriminate.** For each candidate way, give the task conditions, the person's action or reasoning, the resulting work product, help allowed, a positive example and a nearby response that would not warrant that description. Include plausible partial or mistaken reasoning when it changes instruction. A person who notices duplicate messages only after a question is different, for this use, from one who independently chooses the appropriate unit. The same person may show either response in different settings. “No admissible evidence” describes the assessor's knowledge; it is not an initial state of the person.

**Choose the grain by the decision.** Split a description when its components can lead to different instruction or different evidence. Join descriptions when the distinction changes neither the task, feedback, inference nor receiving decision. A single task may require recognizing a difficulty, selecting a Method and enacting it. Preserve their separate contributions where they warrant different evidence or instruction.

**Separate dimensions before ordering them.** Ask whether one contribution can be available while another is absent or uncertain. Use observations that distinguish those combinations. If more are needed, use a suitable existing task or construct one. For example, compare calculation with the unit supplied, unit selection with calculation supplied and their combination in a whole task. Differences across those conditions warrant separate descriptions for the local decision. They do not establish statistical independence or show that isolated success composes automatically. Preserve interfaces and simultaneous resource demands through §4.3.

**Locate the current and intended profiles with their evidence.** Evidence can support different descriptions of a person’s contribution under different conditions or leave several descriptions plausible. Record that uncertainty instead of forcing one label. Keep the desired later-Work performance as the target even when an intermediate instructional task is easier. If personal observations are unavailable, retain a proposed model and target; do not invent that person's starting position, gap or actual passage through it.

##### HCD.4:4.2.2 - Propose and Challenge the Relations

A list of descriptions becomes useful for development when it explains which relationships matter and why. Draw a graph only if it helps retain them; a few sentences or a table can carry the same account.

| Proposed relation | How to construct it | What could change it |
| --- | --- | --- |
| A contribution is required during another performance | Inspect the domain action: identify the input or coordinated contribution that must be present, including what a reference, tool or colleague can supply. | A valid alternative Method or supplied contribution removes the supposed personal requirement. |
| One capability must be available before a particular learning opportunity is usable | Explain what the learner must already notice or do to benefit from that task under its actual help. Distinguish this instructional prerequisite from a requirement of later Work. | A supported route makes the task learnable without that prerequisite, or a learner succeeds through another route. |
| One learning move may produce a qualitative change | Name the starting way, intended way, learning action, support and proposed mechanism; connect them to domain teaching knowledge, relevant research or prior observations. | Adequate enactment produces no predicted difference, a different change appears, or the change disappears outside the cue that supplied it. |
| Two ways may develop separately or through different routes | Specify a plausible combination of performances and a task contrast that could distinguish it from one common ordering. | Comparable observations consistently require the missing contribution or expose an omitted shared requirement. |
| A return or renewed support may be needed | Identify the changed condition, such as a more complex task class, lost access, a misconception, fatigue or a delayed difficulty. Name the result the return is meant to recover. | Restoring the condition removes the difficulty, or evidence supports a different cause. Returning to help alone is not evidence of lost capability. |

For each relation used to select a pathway, state its grounds, which may include domain analysis, research under compatible conditions or local observation. Identify a proposed link that still rests on a hypothesis. These grounds support different strengths of reliance. Co-occurrence or a common teaching order does not establish necessity. Success after instruction does not isolate its causal effect.

Make a proposed transition concrete: **for a learner showing this starting response under these conditions, this activity and help are expected to make this different response attainable, because this learning process addresses the observed difference; this observation would weaken or redirect that expectation.** HCD.5 compares development Methods for that process. HCD.6 constructs the actual learning and observation tasks. If the mechanism or starting evidence is too uncertain for a useful proposal, identify the missing account and which inference the missing evidence prevents.

Keep more than one route when the evidence supports materially different starts, supports or mechanisms. A route can revisit an earlier distinction, maintain an already acquired action while developing another, or use renewed guidance in a harder task class. Retain only relations that matter to the receiving decision.

##### HCD.4:4.2.3 - Preserve Different Proposals for Learning a Method

When the subject is a Method described by a pattern language, two candidate orderings expose different questions. Examine their proposed relations against the decisions and evidence in the particular learning task.

One proposal follows **recognition in a supplied example → explanation of situation, conflicts and mechanism → supported enactment → independent familiar enactment → adaptation in a new context → composition and repair → developing and testing variants, helping others learn and improving the pattern description**. Its useful question is how the person's ways of using a Method differ as demands change. Lack of evidence sits outside this sequence. Composition, repair, variant testing, teaching others and improving the pattern description must each have their own target and observation; they need not form one highest stage.

The other follows **noticing isolated signs → recognizing the conflict among requirements in the situation → selecting an applicable Method → supported enactment → independent action → adaptation and composition in a new context**. Its useful question is how interpretation of the situation makes a Method choice possible. Recognizing a finished example in the first proposal does not establish that a person notices a conflict in an unlabelled situation in the second.

Localize each proposed link. To examine signs-to-conflict, contrast two situations with the same conspicuous sign but different relationships among requirements; ask what action each warrants. To examine conflict-to-selection, retain the difficulty while making a neighboring Method a plausible rival. To examine supported-to-independent enactment, compare performance with and without the help that supplied the targeted contribution, while retaining the ordinary tools and other relevant conditions of later Work. To examine familiar-to-unfamiliar use, identify the consequential novelty and obtain an attempt that does not merely repeat the demonstrated answer.

Compare the proposals against the same work and learner evidence. Keep a useful local order where its grounds survive; split dimensions or allow another route where the evidence distinguishes them. Use the relations that matter to the contribution being learned. A learner can use a Method in familiar work before learning to adapt it or teach it to others. §§5.5 and HCD.6:5.6 show how a proposed relation changes while the required later-Work result stays the same.

#### HCD.4:4.3 - Compare Without Inventing Order

Use `C.32.MWA` to check a proposed correspondence. A course sequence, Method hierarchy, Work order, organization chart, or platform dashboard may be a source structure; none is the profile architecture merely because its rows line up with capability names.

Ask which contributions are simultaneous, which interfaces constrain each other, which supported claims must be preserved, whether any gap limits the work, and where a local gain would move burden or risk. State the current and target profiles and their differences, including any priorities, trade-offs, recommendations or remaining questions the comparison supports. If a choice is needed, use that comparison.

##### HCD.4:4.3.1 - Test and Revise the Model without Rewriting the History

For a relation that matters to the next question, look for observations whose plausible outcomes favour different accounts. Use a suitable existing result. Design a further observation if needed and attainable. Specify the task, means, relevant first action and inference before interpreting its result. An answer that both accounts predict supplies little discrimination. HCD.11 returns the observation and its limits; it does not make the proposed categories true merely by scoring them.

Distinguish three updates. New evidence may locate this person differently within an unchanged model; it may require a different description, condition or relation in the model; or it may only require changing a task or available help. If a supposedly higher performance appears while its asserted prerequisite fails under comparable conditions, examine the prerequisite claim, the observations and the model's grain. If the apparent contradiction comes from an inaccessible task or changed help, repair that comparison before changing the proficiency account.

Look for a way of acting that the proposed categories miss, using learner explanations or work products suited to that question. Where the categories collapse different mechanisms, split them; where two categories never change a relevant inference, consider merging them. Reconsider task validity, scoring and alternative explanations along with the model. Small local evidence can justify a reversible pathway change while leaving a population-wide progression unvalidated.

Keep the earlier observation, its conditions and the model interpretation used at the time. Record the revised interpretation with its reason. Revising a model is a change in an account; claiming that the person learned, forgot or transferred requires evidence about the person. HCD.14 uses this distinction when the model revision also changes the remaining learning arrangement.

#### HCD.4:4.4 - Make a Bounded Choice Under C.11

When a bounded choice is requested, establish or use the inputs and conditions required by `C.11`:

| `C.11` input or condition | HCD.4 use |
| --- | --- |
| `DecisionSubject` and `DecisionSubjectGranularity` | The person, team or other system making this choice and the level at which it makes it. Use `A.13` when it is unclear which person, team or other agent made or can make the choice. |
| `OptionSet` | Concrete options already on the table. HCD.4 does not generate a missing programme alternative. |
| `PreferenceOrder` or `EvaluativeMeasure` | The explicit comparison basis, including protected claims and unacceptable critical errors. |
| `BeliefState` | Current uncertainty, evidence limits, and live rivals shared across the options. |
| `OutcomeModel` | How the options and uncertainty map to the consequences that matter for this choice. |
| dependence layer | Evidential by default; causal, counterfactual, subjunctive, or other heavier dependence requires its own current support. |
| `ChoiceRule` | The condition under which `choose now`, `reject current set`, `probe again`, or `reroute` is lawful. |
| probe-worthiness | When inquiry is live under `C.11`—through a current proposal, consequential uncertainty or an applicable requirement that could change the choice or warranted use—obtain the relevant `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, and value of information or computation. Otherwise these fields do not apply to finishing the supported choice. |
| governance | Holder participation and the chooser's applicable authority; authorization, commitment, and later execution remain separate. |

If a required input, condition, or necessary current/target evidence is absent, keep the profile comparison and recommendation if they are supported, then return `profile-decision-blocked` with the missing value, blocked choice, safe boundary, and retry condition.

With the required inputs and conditions established, the chooser applies the explicit `ChoiceRule` to the current comparison basis, dependence layer and any applicable inquiry values. Return a `ChoiceResult` with the supported disposition, its grounds and any next question required by `C.11`. Record the rule applied, its inputs and the result.

Finish when the available grounds support the choice. Keep the profile, actual choice grounds and any short reason or limitation needed by this decision or a later recipient in that same result. A live feasible probe can still be selected when its attainable contribution justifies its whole burden. An evidence limit remains a limit when acquisition is not selected.

#### HCD.4:4.5 - Recognition and Assurance

**Recognition.** Use HCD.4 when a conversation contains “well-rounded,” “level up,” “mastery score,” “skills matrix,” “promotion profile,” or a course pathway, and the question turns on several different contributions to later Work.

**Assurance.** Stronger reliance requires holder- and condition-compatible task evidence for each claim used in the conclusion; explicit current, target, and uncertainty positions; preservation of critical-error and support-dependence boundaries; an inspectable trade-off account; and, for a choice, all required current `C.11` inputs and conditions, application of the rule, and an inspectable result. High-stakes employment, clinical, safety, legal, or release uses need their direct owner and assurance in addition to this profile.

#### HCD.4:4.6 - What Changes in Practice

Ask which contributions are supported under the stated conditions, which must be preserved, and which gaps, interactions or uncertainties matter across simultaneous Work. This can complete a descriptive comparison. For a requested choice, identify what could change the priority or its grounds.

### HCD.4:5 - Archetypal Grounding

#### HCD.4:5.1 - Constructed Positive Case: ImpactReview-17

`ImpactReview-17` is a constructed case. `ImpactReview-17-Domain-Oracle-v1` supplies engineering correctness and criticality criteria for `PumpWorks-Config-Baseline-42` and `AI-Assist-M4`. The observations and decision conditions below are stipulated case data.

The human holder is Engineer-P14. The later-Work demand is independent review of AI-proposed change-impact claims under a forty-five-minute case limit, current source/configuration access, auditable evidence, and bounded safety and maintenance specialist returns. The work permits a routine reminder to construct and test an alternative hypothesis, while the engineer must supply the case-specific rival and its test. The explicit probe prompt in HCD.3:5.1 names that operation without supplying its answer. Self-initiated recall remains a separate question. HCD.4 keeps four claim rows:

| Claim in the constructed profile | Current evidence | Target and trade-off disposition |
| --- | --- | --- |
| source/configuration trace | 8/8 under the stipulated configuration | Preserve; do not trade traceability for speed. |
| independent AI-output challenge | 2/4 planted-error cases; both misses are unfamiliar variants | Priority gap; target 4/4 and zero accepted seeded safety-critical omissions, within the forty-five-minute limit for each review. Record any additional time the challenge takes. |
| bounded specialist return | 2/2 relevant cases | Preserve the authority boundary; do not internalize specialist judgement. |
| auditable evidence return | 8/8 | Preserve; no aggregate may hide a missing critical-error record. |

For Engineer-P14, preserve the three supported contributions. In unfamiliar cases, investigate whether the engineer generates and tests an alternative before accepting the AI’s claim. Prompt design remains a plausible alternative explanation for the missed errors. The comparison leaves the programme choice open.

Engineer-P14 faces one person-level self-development-focus choice within a separately pre-authorized twelve-hour allocation. The constructed decision record captures the chooser's inputs and application of `C.11`:

| Decision value | Constructed case value |
| --- | --- |
| `DecisionSubject` | Engineer-P14. |
| `DecisionSubjectGranularity` | Person-level; Engineer-P14 participates directly in the comparison. |
| `OptionSet` | `O1` preserve the profile without selecting a change; `O2` make independent AI-output challenge the priority for later programme comparison while preserving the three supported claims; `O3` defer a human profile-change priority and return the live prompt-design question to the Method/tool owner. |
| `EvaluativeMeasure` | Prefer fewer accepted seeded safety-critical omissions while preserving source/configuration trace, specialist authority, auditable evidence, the forty-five-minute case limit, and reversibility. |
| `BeliefState` | Two unfamiliar misses, a small sample, and a live prompt-design rival remain. |
| `OutcomeModel` | A two-case prompt comparison can still change which of `O2` or `O3` survives, while differences between the cases remain unresolved. This supplies evidential input rather than an isolated causal prompt effect. `O1` leaves the observed critical-error gap unchanged. |
| dependence layer | Evidential baseline only; no causal intervention or capability-change claim is used. |
| `ChoiceRule` | Choose a profile-change priority now only if it survives the live nonhuman rivals and no feasible decision-changing probe is worth its cost; otherwise emit `probe again` for the smallest feasible probe that can reverse `O2` versus `O3` within the allocation and protected conditions. |
| `ProbeActionSet` | Two further unfamiliar seeded-error cases, with one first attempt per case: one uses a neutral prompt, the other an explicit counter-hypothesis prompt. Observe whether Engineer-P14 generates and tests a counter-hypothesis, and whether they reject the wrong AI claim. Keep the same sources, tools, specialist routes, and forty-five-minute limit per case. |
| `ProbeBudget` | Two hours remaining for this pre-choice probe inside the twelve-hour allocation. |
| `CostToProbe` | Up to ninety minutes for the two attempts, plus thirty minutes reserved for preparation and comparison: two hours in total. |
| value of information | A tested counter-hypothesis and rejection of the wrong claim only with the permitted reminder would strengthen `O3`: the observed human contribution works under that assistance condition. It would not establish self-initiated recall. Misses under both prompts would strengthen `O2`. Interpret either result with the small sample and unresolved case differences. The seeded critical-error boundary makes this possible change in choice worth the bounded cost. |
| probe-worthiness | Feasible and worth its cost. |
| `ChoiceResult` | **`probe again`** with this two-case comparison, one attempt per prompt condition. No profile option is selected yet. |
| next question and authority | Return the new observations to HCD.3 and the updated comparison to HCD.4. The accountable manager owns time allocation, Work assignment, and employment consequences; safety and release owners retain their authority. |

Engineer-P14 applies the stated rule and selects the two-case comparison under the existing time allocation. Each case receives one prompt condition, so the result must be interpreted with the unresolved differences between cases. The manager’s allocation and the separate safety, release and employment authorities remain in force.

#### HCD.4:5.2 - Missing Case: ReleaseWork-R9

For Engineer-E27, HCD.1 can return a prospective `ReleaseWork-R9` demand hypothesis, but no compatible current profile comparison is supportable. The actual Work occurrence, occurrence-produced result claim, occurrence-bound result record, representative observations, and actual `SYSE.21` supplier result required by `XRI-21` remain distinct missing values.

HCD.4 may retain prospective target claims for AI-output challenge, configuration-impact reasoning, evidence return, specialist coordination, critical-error detection, and unfamiliar-variant adaptation. Without compatible observations it cannot infer Engineer-E27’s current contributions, their difference from the target or a priority based on that difference.

Return `profile-decision-blocked`. The blocked choice is any preserve, investigate, defer, narrow, specialist-evidence, or profile-change decision that depends on current holder evidence. The incomplete HCD profile does not justify claims of mastery, a current-versus-target gap, or transformation, or decisions about a programme, allocation, or employment. This boundary applies to uses of that unsupported profile; separate decisions need their own sufficient evidence and appropriate authority. Retry with a compatible same-holder demand frame, claim-by-claim current and target evidence under the intended configuration and evidence window, direct target-domain and specialist boundaries, holder participation, and—if a choice is requested—the current `DecisionSubject`, pre-existing `OptionSet`, comparison basis, applicable inquiry values, authority, and `ChoiceRule`.

#### HCD.4:5.3 - Unlike Case: Clinical and Participation Profiles

For an adult seeking treatment for social anxiety, use qualified clinical care for diagnosis, treatment targets, provider competence, safety, and outcome interpretation. Symptom scales, exposure ladders, treatment plans, and provider pathways inform that clinical work; they do not by themselves establish a profile of the person's contributions in later Work.

HCD.4 may compare condition-qualified contributions for a separately legitimate non-clinical participation or later-Work question only when the person and clinical owner supply a safe boundary and compatible evidence. A symptom change alone does not demonstrate the later-Work contribution. HCD.4 does not select treatment, and clinical safety must not be traded against productivity. Managerial authority over allocation confers neither clinical competence nor clinical decision authority and does not replace the person's consent. If the required boundary or evidence is missing, return `profile-decision-blocked`; route a clinical question to its clinical owner.

#### HCD.4:5.4 - Constructed Ordinary Case: Preserve a Supported Profile

Engineer-K6 asks which of two already proposed profile priorities to retain for next month's review of the same kind of configuration note, using the same sources, AI support and specialist return. A qualified HCD.1 demand account supplies a forty-five-minute case limit, source traceability, independent challenge of AI claims and auditable return. This constructed case stipulates current same-holder observations and the target-domain correctness criteria.

At the current forty-minute working pace, source traces and evidence returns are complete in eight of eight representative cases, and four of four seeded incorrect AI claims are rejected. In four additional, compatible cases at a twenty-minute pace, traces and returns remain complete, but only two of four seeded incorrect claims are rejected. The sample supports these condition-qualified rows; it does not establish mastery, an isolated causal effect of pace or transfer to other tools.

K6 is the person-level chooser and participates directly. The current options are `O1`, preserve independent challenge together with trace and evidence return at the present pace, and `O2`, prioritize twenty-minute completion. The comparison first preserves rejection of the seeded critical errors and then prefers less review time within the forty-five-minute limit. The outcome account uses the observed contribution and trade-off under each pace. The uncertainty about other tools lies outside this receiving use.

The explicit `ChoiceRule` selects the option supported for all required contributions before preferring speed. Applied to these rows, it returns **`choose now: O1`**: preserve the present profile; the faster option loses a required contribution. The result keeps the claim rows, options, rule, reason and same-configuration limit. A programme, release, allocation or employment decision would need its own basis and authority.

#### HCD.4:5.5 - A Local Model for Selecting the Unit of Work

Coordinator-N24 is fictional. The following tasks, observations and resources are stipulated for this example. N24 must estimate active processing work from request records. In this case each distinct request needs 18 minutes, and each duplicate message adds no further processing. These simplifying assumptions are supplied domain facts; real coordination, queueing and variable request effort require their own model.

The target is to choose the unit appropriate to the requested result, calculate the active effort and state its boundary. In two initial tasks, N24 calculates correctly when given the number of distinct requests. With 80 message records including 20 duplicates, N24 initially uses 80 and returns 24 hours. After a teacher asks which records concern the same request, N24 groups them into 60 requests, returns 18 hours and explains the difference. The first response and the helped correction are separate evidence.

The practitioner constructs this small model:

| Contribution | Candidate qualitative descriptions | Current position and intended change |
| --- | --- | --- |
| selecting the unit | follows the salient record label; uses the work request when grouping is prompted; independently chooses and checks the unit against the receiving question | The first two are observed. Independent selection is the target, with uncertainty about cues and context. |
| carrying out the calculation | needs the unit and operation supplied; applies 18 minutes per distinct request with ordinary calculator access | The second is supported when the unit is given. Preserve it while changing selection. |
| coordinating the result | reports a number without its scope; relates the estimate to active effort while keeping response time and queue clearance separate | Include that scope distinction in whole-task practice; do not infer it from arithmetic alone. |

Model M0 tentatively orders independent selection by context familiarity: success in new service contexts is expected to come with reliable selection in familiar ticket formats. This cumulative proficiency hypothesis would favor familiar-format practice before moving to new contexts. Its basis is a plausible teaching assumption, not an established prerequisite. M0 also predicts that an explanation of the duplicate/request relation will help selection; the earlier helped explanation has not yet tested independent use. HCD.6:5.6 constructs two routes that could address that difference.

The two candidate orderings lead to different observations: noticing duplicate signs is not yet recognizing the unit conflict; recognizing that conflict is not choosing the relevant operation; supported grouping is not independent selection. Explanation, calculation, selection and qualification of the whole result remain distinguishable. Whether learning them also supports later adaptation or repair needs separate observations. Teaching another person would be a different target. The observation and revision of M0 are developed in HCD.6:5.6.

### HCD.4:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| scalar bias | One score hides claim identity, critical errors, support dependence, and uncertainty. | Keep claim rows; aggregate only when the receiving decision loses nothing material. |
| ladder bias | Current, intermediate, and target states become a universal maturity path. | Use intermediate descriptions when they clarify the comparison under the stated conditions; distinguish intended targets from observed states. |
| curriculum bias | Course order becomes capability architecture. | Recover simultaneous later-Work contributions and keep the instructional plan distinct from the capability profile. |
| source-layout bias | A Method hierarchy, Work order, organization chart, or dashboard becomes the profile. | Recover contributions and their mutual constraints from simultaneous Work. Use a corresponding source structure only when that correspondence is justified for the profile question. |
| tool-score bias | A model prediction or assisted result becomes human mastery. | Bind the prediction to its task, data, support posture, uncertainty, and direct evidence. |
| deficit-only bias | Strong claims disappear while one gap is amplified. | State what must be preserved and the trade-off created by prioritizing the gap. |
| chooser bias | A manager, platform, or assisting System is treated as the chooser without a current choice relation. | Name `DecisionSubject` and granularity; route unresolved agency to `A.13`. |
| probe-for-free bias | More information is always requested. | If additional observation is under consideration, check that it fits the available budget, compare its attainable value with its full cost and identify when to stop. |
| authority collapse | A profile recommendation becomes authorization, employment action, safety choice, or commitment. | Keep comparison, `ChoiceResult`, authorization, commitment, and later Work separate. |

### HCD.4:7 - Conformance Checklist

- [ ] The person whose contributions are being compared and a compatible HCD.1 demand account or equivalent qualified scope are recoverable.
- [ ] Later-Work family, configuration, conditions, horizon, evidence window, receiving question or decision, and representative simultaneous interfaces are explicit.
- [ ] Each claim row states contribution, current evidence, target, optional intermediate only when useful, conditions, support posture, observation date, uncertainty, discriminating task/evidence, critical-error boundary, any relevant trade-off and what could justify reconsideration.
- [ ] Profile descriptions and their comparison or aggregate are distinguished from instructional plans, realized learning trajectory, performed learning Work, and human transformation; occurrence and change claims have corresponding evidence.
- [ ] When a local progression model is used, qualitative descriptions have discriminating examples; dimensions, task conditions, prerequisites and transition hypotheses retain their different grounds.
- [ ] When a model is used, identify an observation that could challenge each consequential relation. Distinguish a new judgement about the person’s position from a change to the model, task or help. A supported comparison or choice can finish without an additional model.
- [ ] Any source structure used for the profile is justified by the contributions and mutual constraints in representative Work.
- [ ] Supported claims to preserve are visible alongside gaps and trade-offs.
- [ ] An aggregate is used only when it removes no decision-bearing identity, asymmetry, critical-error, support, or uncertainty value.
- [ ] The profile gives its recipient the supported comparison and any relevant priorities, trade-offs, gaps or remaining questions. A requested recommendation identifies the appropriate decision holder where known.
- [ ] For any bounded choice, the chooser has applied the `ChoiceRule` to the required current `C.11` inputs; the record includes chooser granularity, pre-existing options, comparison basis, belief, outcome model, rule, applicable inquiry values, result, participation and authority. Keep a reason or limit needed for this or a later use in the substantive result.
- [ ] A missing decision or evidence value required for the affected conclusion produces `profile-decision-blocked` with the affected finding or choice, safe boundary and condition for reconsideration.
- [ ] The result fabricates no HCD.2 programme and authorizes no curriculum, provider, employment, safety, legal, clinical, or release action.
- [ ] The recipient can identify supported contributions, any consequential gap and whether further work is warranted. If a choice is requested, the comparison identifies what may affect it and who can decide, or what authority is still unknown.

### HCD.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| “Overall mastery: 72%” | The aggregate can hide a critical error and unsupported claim. | Restore claim rows and use an aggregate only where its losses do not affect the receiving question. |
| “Complete level 2 before level 3” | A convenient ladder becomes an unsupported Work or learning sequence. | Show simultaneous contributions. Use a local intermediate target only when the current decision needs it, and judge its achievement from observations rather than course position. |
| “The platform predicts mastery” | A model output depends on its data, item representation, task, and support assumptions. | Keep it as one evidence source and require direct claim-task-observation-inference trace. |
| “The target profile is the current profile” | Intention is mistaken for current evidence or transformation. | Record current, target, difference, and evidence dates separately. |
| “Improve the weak dimension” | The decision can damage a strong claim, authority boundary, or protected consequence. | State preserved claims and moved trade-offs before recommending priority. |
| “The profile chose the programme” | A comparison neither generates alternatives nor supplies an HCD.2 Method. | Return the supported profile, recommendation, blocker or `C.11` choice over already-available non-programme options. |
| “More data” | The next observation has no decision-changing purpose or bounded cost. | Name the exact probe, budget, cost, value, and reversal condition—or close now. |
| “The manager is the subject” | Manager authority over allocation does not erase the human holder's participation or transfer clinical, safety, or release authority. | Keep `DecisionSubject`, participation, and direct-owner authorities explicit. |

### HCD.4:9 - Consequences

Practitioners can preserve reliable contributions, expose one limiting gap, show the cost of prioritization, and distinguish a recommendation from a lawful choice. Missing required evidence or choice values become exact blockers instead of silently completed forms; an inapplicable inquiry field blocks nothing.

A claim-by-claim comparison can require more evidence and interpretation than a single score. Claim rows can disagree, uncertainty can remain, and the lawful result may be `probe again` or reroute rather than a selected priority. A later programme, intervention, or employment decision still needs its own Method and authority.

### HCD.4:10 - Rationale

A capability profile relates contributions that the person may have to make together under stated conditions. Keeping each contribution identifiable reveals different supports, critical-error limits, uncertainties and trade-offs that an overall score can conceal.

The profile supplies the comparison; a choice also requires an identified chooser, available options and the relevant authority. Under `C.11`, applying the `ChoiceRule` can return `probe again` when a feasible observation is worth its cost and could materially affect the choice or its grounds. Record the inputs, rule and result. An already supported choice can finish without a new observation. `profile-decision-blocked` identifies absent prerequisites for the actual conclusion.

### HCD.4:11 - SoTA-Echoing

**How should a practitioner compare several human capability claims for simultaneous later Work without turning a score, source layout, or target into mastery or a programme?**

The selected current line combines claim-level assessment traceability and bounded mastery evidence. Winget and Persky’s [A practical review of mastery learning](https://doi.org/10.5688/ajpe8906) (2022; `COG-06`) describes arrangements with local thresholds, formative evidence, correction, and retest; it establishes neither one universal level nor later professional performance. Gutierrez de Blume’s [Calibrating calibration](https://doi.org/10.1037/edu0000674) (2022; `COG-07`) informs the use of self-monitoring accuracy as one evidence source, while confidence is not a demonstration of capability. Arieli-Attali and colleagues’ [Expanded evidence-centered design](https://doi.org/10.3389/fpsyg.2019.00853) (2019; `COG-08`) supports making the claim, task, observable evidence, inference, and proposed transition recoverable; this design framework supplies no causal treatment comparison, and an evidence model does not make its claim true. Abdelrahman and colleagues’ [Knowledge tracing: a survey](https://doi.org/10.1145/3569576) (2023; `COG-09`) describes latent-state and next-response predictions under model and data assumptions; such predictions do not demonstrate transfer, retention, capability, or causal learning. `C.32.MWA` adds the architecture guard: relationships among simultaneous contributions need not match course order, Method partition, Work structure, or organization structure. Recover those relationships from the Work; a matching layout alone does not justify the correspondence.

A serious alternative is the single competency score, role-level matrix, or mastery ladder. It can communicate a coarse result compactly. For the receiving question, check which differences between contributions, critical errors, support conditions, uncertainties, simultaneous demands or shifts in burden the summary conceals. Use it only if those losses leave the answer intact. Keep the individual claims available.

Choice requirements come from `C.11`; a decision record documents their application to the case. Direct target-domain sources supply correctness and criticality criteria. Reopen when the holder, later Work, configuration, Method or source edition, support posture, claim set, evidence date, critical-error predicate, trade-off, profile owner, options, chooser, authority, or decision rule changes.

For the additional question, **how can a practitioner construct and revise a local model of qualitative development rather than merely list current and target claims?**, the selected line separates descriptions of proficiency from hypotheses about changing it. [Expanded evidence-centered design](https://doi.org/10.3389/fpsyg.2019.00853) makes that missing connection explicit through a proficiency-change account, task support and change evidence. HCD.4 adapts this construction in §§4.2.1–4.3.1 without requiring a psychometric model for every local decision; the effect of a proposed teaching move requires its own evidence.

[Kaldaras, Haudek and Krajcik (2024)](https://doi.org/10.1186/s40594-024-00516-0), in their account of learning-progression-aligned STEM assessment, distinguish hypothetical progressions from validity evidence accumulated through tasks and responses. Their discussion also treats progression as dependent on instructional conditions. HCD.4 adopts that bounded practice of revising descriptions and relations against observations; their proposed AI assessment architecture does not validate N24's model or an automated mastery judgement.

A serious alternative is a fixed rubric of increasing independence, or an unconnected list of skills. Either can suffice for reporting a bounded performance when its distinctions fit that use. Neither explains why the next activity should produce a particular change. The local construction adds that explanation, alternative routes and a discriminating observation, at the cost of domain analysis and case preparation. The added model is justified only when those distinctions change learning or assessment. Reopen it when a new response crosses the proposed ordering, a supposedly independent dimension depends on another, or a different task or support changes what a description predicts.

### HCD.4:12 - Relations

- **`HCD.1`:** supplies the same-holder scope and result frame. An equivalent qualified demand account may substitute; an incompatible population profile may not.
- **`HCD.3`:** may supply a qualified target and any still-plausible rival as evidence.
- **`C.32.MWA`:** helps establish which relations in a course sequence, Method hierarchy, organization chart or other representation correspond to the relations in simultaneous Work.
- **[Winget and Persky’s review (2022)](https://doi.org/10.5688/ajpe8906) (`COG-06`):** supplies the local-threshold, correction, and retest contribution, not a universal mastery ladder.
- **[Gutierrez de Blume’s meta-analysis (2022)](https://doi.org/10.1037/edu0000674) (`COG-07`):** supplies self-monitoring accuracy as one bounded evidence source.
- **[Arieli-Attali and colleagues’ design framework (2019)](https://doi.org/10.3389/fpsyg.2019.00853) (`COG-08`):** supplies claim/task/evidence/inference traceability, not a causal intervention result.
- **[Abdelrahman and colleagues’ survey (2023)](https://doi.org/10.1145/3569576) (`COG-09`):** supplies model-prediction limits; a predicted state does not establish this person's mastery.
- **`C.11`:** governs local choice over a current option set. Applying the explicit rule can return `choose now`, `reject current set`, `probe again`, or `reroute`.
- **`A.13`:** receives an unresolved agency claim when an assisting System, coupled arrangement, team, or organization is proposed as chooser.
- **`E.23.CAE` and `E.23.CDI`:** may supply differential or later development/transfer evidence under their own entry conditions; neither is implied by a profile.
- **Target-domain and specialist sources:** provide criteria and evidence for correctness, quality, criticality, safety, legal, clinical, and specialist-return questions in the claim rows. Qualified specialists supply professional judgements, and authorized actors make the corresponding decisions.
- **Programme comparison (`HCD.2`):** may receive priority characteristics, trade-offs and relevant local progression hypotheses as criteria for the programme comparison when they apply to this person and later Work.
- **`HCD.5`, `HCD.6`, `HCD.10`, `HCD.11` and `HCD.14`:** respectively compare learning mechanisms, turn local transition hypotheses into tasks and pathways, select the next practice change, test the claims and relations, and revise the affected model or arrangement. A model does not supply a selected plan or an observed trajectory.

- **Managers and direct decision owners:** retain allocation, assignment, employment, safety, legal, clinical, and release authority; the human holder's participation remains explicit.

### HCD.4:End
