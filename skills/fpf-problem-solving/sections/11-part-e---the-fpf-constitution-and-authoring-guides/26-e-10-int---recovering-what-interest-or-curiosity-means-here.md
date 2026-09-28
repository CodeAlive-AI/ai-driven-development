## E.10.INT - Recovering What Interest or Curiosity Means Here

> **Type:** lexical and ontological precision restoration (E)
>
> **Status:** Draft

### E.10.INT:1 - Problem frame

**Use this when** a claim that something is *interesting*, *in someone's interest* or *driven by curiosity* is being used to choose work, but leaves you unsure what to do. You may need to select an experiment, retain a promising construction, design an agent's exploration policy or understand why participants want different outcomes.

Begin by saying whose interest is involved and what the sentence proposes. “This experiment is interesting” might mean that its result would distinguish two models, that a participant wants to try it, or that the resulting technique could support further experiments. Each meaning can guide useful work.

The first result is a clearer sentence and a next action that follows from its meaning. Keep ordinary wording when its meaning is already sufficient. A musician expressing delight and a contract stating an interest rate can continue their respective work without this recovery.

### E.10.INT:2 - Problem

The same word connects several different questions. An informative observation changes beliefs; a learning-progress signal compares what a learner can do; a promising stepping stone offers further possibilities; an affected participant has something to gain or lose. In a joint project these relations often coexist.

Their differences matter when a phrase becomes an instruction. Asking an agent to maximize “surprise” may reward unpredictable observations instead of observations that help it distinguish its hypotheses. Requiring a promising idea to demonstrate progress toward a distant goal may discard the very construction from which another goal could emerge. Selecting an “interesting rhythm” leaves the choice unresolved until the listener, performer or musical use is known.

### E.10.INT:3 - Forces

| Force | Working tension |
|---|---|
| Shared vocabulary | A short familiar word helps discussion, but can hide which participant or consequence guides a choice. |
| Several useful explanations | Motivation, information gain and future possibilities may contribute together, while their measures answer different questions. |
| Open exploration | A present clue can justify trying a continuation before its eventual uses can be predicted. |
| Proportionate precision | A consequential choice needs its meaning restored; an ordinary expression often needs no further work. |

### E.10.INT:4 - Solution

Recover the relied-on meaning, then continue the work that gives it value.

1. **Locate the claim that matters.** Take the sentence together with the decision or activity it is meant to guide. Ask what would change if the object were judged interesting. If nothing depends on that judgement, keep the expression as it stands.
2. **Name the participant and relation.** Identify who is engaged, affected, learning or choosing. Identify what draws attention, what might change, or what the participant stands to gain or lose. Use the distinctions in §4.1 only where they resolve the sentence.
3. **Preserve combined meanings.** If a participant enjoys an experiment and the experiment could distinguish two models, say both. Let the corresponding motivation and inquiry methods supply their different contributions.
4. **Restore a needed comparison.** When a score or optimization rule is proposed, name what it compares and under which model, experience or resources. Use §4.2 to resolve ambiguous appeals to surprise, progress or a Goldilocks region.
5. **Return to the action.** Rewrite the claim so its recipient can choose, inquire, practise, retain a result or explain a concern. Continue once that meaning is sufficient. A shared decision can keep the clarification in its existing account; an ordinary sentence needs no additional form.

#### E.10.INT:4.1 - Recover the contribution being claimed

These are recurring uses of the wording. Select the ones needed for the sentence; several can apply together.

| What the wording is doing | What to recover | Example of the resulting claim |
|---|---|---|
| Expressing a participant's stake | The participant, affected outcome and consequence | “The maintenance team wants the inspection window because it can then replace the worn coupling.” |
| Expressing attraction or engagement | The person or group, activity and response | “These listeners want to keep moving to this rhythm.” |
| Selecting information-seeking action | The agent's uncertainty, available observation and use of the resulting information | “The controller samples input 1 to distinguish the two candidate relations before choosing its command.” |
| Describing learning progress | The learner or model, what changes and the comparison | “After training, the compressor describes the same material in fewer bits.” |
| Explaining active-inference policy selection | The generative model, candidate actions, information expected from them and preferences over outcomes | “The agent first observes the cue to learn which action is likely to produce its preferred outcome.” |
| Recognizing a promising continuation | The present clue, available variation or combination, and what is worth trying or retaining | “This construction permits a new family of transformations; keep it available for exploration.” |

An information-seeking policy can be attributed to a human, an AI agent or a collective whose members obtain and use the information. For a claim about a person's experience, preserve that experiencer. A policy description alone leaves the question of subjective experience open.

A prospective continuation can be supported by a hunch, a newly available operation or a promising variation. State that basis at its actual strength. Where its future destination is unknown, the next action can be to explore or retain the construction. C.18 supplies retention in an exploration archive; C.19 helps choose which directions in an active search pool to continue, retain or stop; C.40 helps develop problems and ways together.

#### E.10.INT:4.2 - Recover the model behind the comparison

For **surprise**, first recover the quantity being used. The surprisal of an observation, `-log p(observation)`, concerns its probability under a selected model. Bayesian surprise concerns the change from prior to posterior beliefs about chosen variables. Expected information gain evaluates a possible observation before it is obtained. A learning-progress signal compares successive predictive or constructive performance under a learning procedure. Those comparisons can disagree, as §5.1 shows.

In **active inference**, distinguish updating beliefs from selecting actions. Predictive coding uses prediction errors to update beliefs about hidden states and, in learning formulations, model parameters. Policy selection also depends on the information and outcomes expected from action. Recover the prior preferences when a source explains avoiding an outcome through its expected surprise. The source's account may couple epistemic and pragmatic value. Preserve that coupling together with the quantities and assumptions that give it meaning.

For a **Goldilocks region**, recover what varies, for which agent and use, and over which range. It might concern an attainable learning challenge, a listener's response to syncopation or a combination of rhythmic properties. Use the applicable account of the relation between those characteristics and the desired result. The useful region can move as the agent learns or as the task changes. In a search algorithm, a difficulty screen can select candidates for learning while novelty and transfer still govern which possibilities are retained.

When a quantitative answer is needed, C.16 supplies measurement and C.17 separates novelty, usefulness and sample surprise. Keep an adequate qualitative comparison when it already settles the action.

#### E.10.INT:4.3 - Combine contributions in a development project

A project can use information-seeking to distinguish alternatives, learning progress to choose a promising practice opportunity, and novelty or diversity to retain further possibilities. State the contribution of each rule to that project.

For example, a group can test the controller in §5.1 during a maintenance window. The researcher calls input 1 interesting because its response distinguishes two candidate relations. A colleague sees the query construction as material for other unknown interfaces. The maintenance team needs the controller returned to service before the window ends. Recover their claims as three instructions: “Query input 1 to choose the command”; “Keep this construction available for exploration of other interfaces”; and “Schedule controller work within the available window.” If the relation is supplied, the query becomes unnecessary. The potential use of the construction remains, and the window still constrains any remaining controller work.

C.11 compares formed options when a choice is needed. C.19 helps decide which directions in an active search pool to continue, retain or stop. A single agent's information-seeking policy uses the applicable subject method; choosing among formed queries can use C.11. C.40 supports the development of problems and ways. The field's methods supply the experiment, training activity or construction itself.

### E.10.INT:5 - Archetypal Grounding

#### E.10.INT:5.1 - An informative controller query

A controller must choose an input that gives output 5. It has two equally plausible candidate relations, `y=x` and `y=-x`, and can first query input 0 or input 1. “Choose the more surprising query” leaves the criterion unclear.

At input 0 both candidates return 0. At input 1 they return 1 and -1 respectively. The second query distinguishes the candidates: after observing 1, command 5; after observing -1, command -5. The recovered instruction is “query input 1 to distinguish the relations, then choose the command.”

A separate fair coin produces an outcome with one bit of surprisal, but its outcome is independent of which relation holds. Querying input 1 yields one bit of information about that relation under the stated equal prior. Tossing the coin yields none. If the controller is already given the relation, it can select the command immediately.

The example constructs an information-seeking policy. Whether a particular controller can execute it is a further capability question.

#### E.10.INT:5.2 - Progress and a stepping stone

In a constructed example, a compressor learns a dictionary entry for a repeated substring in a fixed data block. Its total lossless description of that block, counting the dictionary and encoded data under the same convention, falls from 100 bits before the update to 80 afterwards. “The second version is more interesting” can now be recovered as “this dictionary update reduced the total description by 20 bits for this block.” If the team is choosing more training, it considers the likely further improvement and the work required.

Another construction may deserve attention even though that measure has not improved. In Stanley and Lehman's Picbreeder example, a participant retained and developed an image resembling an alien face; a car-like image appeared through later changes. The first participant could act on the available image and its variation possibilities before knowing that destination. The practical result of this recovery is to retain the construction and its means of variation for exploration. C.18 governs an archive used for that purpose.

These cases permit different choices: improving a known performance measure and preserving a possible starting point for new work.

#### E.10.INT:5.3 - Choosing an interesting rhythm

A workshop needs music for listeners who are familiar with 4/4 and are beginning to work with 7/8. “Choose moderately complex rhythms; they are the most interesting” hides both the response sought and the listeners' preparation.

Recover the request as “choose material that helps these listeners maintain the beat and want to move while encountering 7/8.” The facilitator can start from simpler 7/8 material and adjust from the listeners' response. If the purpose is instead to exercise a skilled drummer's coordination, that practice question needs its own choice of material.

This distinction is supported by Spiech and colleagues' study: Western listeners' groove ratings peaked at moderate complexity in 4/4, while simpler rhythms received the highest ratings in the less common meters tested. Here *groove* means the pleasurable urge to move. The study supports adapting the comparison to listener and meter; the workshop's teaching method supplies the exercise.

### E.10.INT:6 - Bias-Annotation

The source traditions model different aspects of agency. A person's felt curiosity, an AI policy's objective and a collective's exploration practice call for different accounts of how the effect occurs. Use the shared recovery procedure to keep those subjects visible while comparing their contributions.

Rhythm examples also depend on musical experience. A result for Western listeners and selected meters provides a qualified starting point for that use; another musical practice may support another comparison.

### E.10.INT:7 - Conformance Checklist

- The repaired sentence identifies the participant and the contribution that matters to the work.
- Combined meanings remain recoverable when both affect the action.
- A proposed score retains its model, comparison and receiving use.
- An exploratory continuation can proceed from its present basis while its eventual destination remains unknown.
- The reader can resume the relevant activity, or identify the particular unresolved meaning that prevents it.
- The recovery stops when ordinary wording is sufficient; further measurement or inquiry follows the needs of the activity.

### E.10.INT:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it changes the work | Repair |
|---|---|---|
| Rewarding unpredictable observations as if they resolved uncertainty | A random source can consume the query budget while leaving the relevant hypotheses unchanged. | Identify which observation updates beliefs about the question being investigated. |
| Requiring a stepping stone to justify a distant objective | The eventual use may become visible only after the construction is varied or combined with another. | Judge the available exploration or retention opportunity from its present basis. |
| Applying “moderate complexity” across agents and tasks | The learner's available methods or the listener's familiar structure can change which material is usable. | Recover the varying characteristic and the agent-relative comparison. |
| Treating one participant's interest as the project's entire choice rule | Other participants can bear different consequences. | State the affected stakes before the applicable decision method compares options. |

### E.10.INT:9 - Consequences

A clarified interest claim can guide an experiment, an exploration policy, a practice choice or a discussion of stakes. A project can combine these contributions while preserving what each one explains.

Recovery sometimes reveals that the needed information is absent. Keep that uncertainty attached to the claim. Obtain more information only when its possible contribution warrants the work, using C.11.DUA when the advice or demand itself needs examination.

### E.10.INT:10 - Architectural Rationale

The common operation is to recover the relation hidden by a familiar expression. A single engagement score would lose the distinction between a participant's response, a model's progress and a construction's further uses. Conversely, treating these meanings in isolation would miss how one project coordinates them.

The procedure therefore identifies the participant and contribution first, and adds models or measurements only for the question that needs them. This also lets a promising new method be pursued from available clues while later uses are still being discovered.

### E.10.INT:11 - SoTA-Echoing

**Learning progress.** Schmidhuber's historical [formal theory of creativity and intrinsic motivation](https://people.idsia.ch/~juergen/ieeecreative.pdf) distinguishes improvement of a predictor or compressor from the unpredictability of its input. Adopt that comparison for progress claims in §4.2. The competing shortcut, fixed-model surprise, can reward an unlearnable signal; §5.1 makes the related information-seeking error actionable.

**Information-seeking policies.** [Paprika](https://arxiv.org/html/2502.17543v3) describes strategic information gathering for task completion without an intrinsic-motivation reward. Its training curriculum uses a coefficient-of-variation heuristic for sampling tasks. Adapt the policy distinction in §4.1; keep that sampling heuristic separate from a measurement of acquired capability.

**Active inference.** [Friston et al. (2017), §2](https://activeinference.github.io/papers/process_theory.pdf), supplies the historical coupling of epistemic and pragmatic value. Their [2025 technical note](https://arxiv.org/abs/2512.21129) extends information-seeking to distinctions among model structures. Adapt those contributions in §4.2: recover the model, expected information and preferences behind the action. This supplies a richer continuation than explaining all exploration as aversion to an unexpected observation; the selected formal account still determines its assumptions.

**Open-ended search.** Stanley and Lehman's [Why Greatness Cannot Be Planned](https://doi.org/10.1007/978-3-319-15524-1), Chapters 5 and 9, gives the historical argument for judging available stepping stones without requiring their final destination. [Enhanced POET](https://proceedings.mlr.press/v119/wang20l.html), §§2-3, combines a population-relative difficulty screen with novelty and transfer. Adopt the distinction between an attainable learning opportunity and retained possibilities in §§4.1-4.3. A progress-only selector can lose the latter; the particular search method must supply its generation, retention and resource rules.

**Agent-relative challenge.** [Oudeyer's 2026 preprint review](https://pyoudeyer.com/Curiosity-Review-OudeyerMarch26.pdf) compares curiosity processes across timescales and examines conditions for an intermediate-knowledge preference. Adapt this conditional treatment of the Goldilocks region. It improves on an agent-independent midpoint rule by retaining the learner, environment and changing knowledge.

**Rhythmic interest.** Toussaint's *The Geometry of Musical Rhythm*, second edition, Chapter 41 and Epilogue, develops an account using several rhythmic properties and their combinations. [Spiech et al. (2025)](https://www.nature.com/articles/s44271-025-00360-0) compare groove ratings across complexity and meter in three behavioral experiments. Adapt their listener-and-meter distinction in §5.3. It provides a more useful selection basis than a universal complexity optimum, while leaving rhythm construction and teaching to their field methods.

Reconsider these comparisons when a source provides a better account of the particular contribution, changes the conditions under which a signal works, or enables the same action with less inference or measurement.

### E.10.INT:12 - Relations

- **E.10 and E.10.ARCH** locate this recovery when interest-family wording hides the relation needed for work. F.19 handles the surrounding prose.
- **E.10.LRN** recovers a remaining ambiguity about what learned or changed. E.10.DEV handles a remaining development or evolution claim.
- **C.16 and C.17** supply measurement and the distinctions among novelty, usefulness and sample surprise.
- **C.11** compares formed options; **C.19** governs directions in an active search pool; **C.18** supplies retention in an exploration archive. **C.40** develops problems and ways together.
- **D.1 and D.3** supply ethical-value and conflict analysis when affected interests raise those questions.
- **E.23.CDI** offers candidate capability-development guidance that separates a described acquisition method, its execution and an asserted capability change. It can govern an FPF claim only after its own admission; the applicable admitted field pattern supplies the acquisition or intervention method.

### E.10.INT:End
