## NSTD.5 - Choose Narrative Engagement Devices for the Intended Experience or Use

> **Status:** Stable

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** choosing, assessing or revising narrative devices that direct attention, sustain interest or make a relation memorable for an intended use.

### NSTD.5:1 - Problem frame

Use this method when attention, curiosity, identification, suspense or another reader experience matters to the work. It can also help identify why an account encourages misplaced confidence or directs attention away from a required distinction.

Identify the intended effect, then examine a device in an existing passage or try it in the passage being composed. Compare what it adds, changes or removes. An available simpler treatment can help make the difference clear. For a choice or revision, weigh the contribution against its cost and preserve the relations the reader needs.

A reader may leave before the useful part, remember the wrong feature or take a vivid example for stronger evidence than it is. Each observation points to a different question about the passage.

The result can be a device chosen for its expressive purpose, an account of what the text makes salient, or a finding about the response of readers under known conditions.

### NSTD.5:2 - Problem

A story can organize attention and memory around a relation the reader needs. The same device can hide a qualification, reduce a genuine conflict to one viewpoint or lend a conjecture the apparent force of an observation. Decide which effect matters and what would establish it for this use.

### NSTD.5:3 - Forces

| Force | Tension |
| --- | --- |
| Attention vs source fidelity | Engagement can help readers reach source structure or distract from it. |
| Motivation and informed choice | A device can help a reader pursue an aim or conceal information needed to choose it. |
| Memory and confidence | A reader can remember a story and still misjudge how well its claim is supported. |
| Different readers | The same device can direct attention in different ways depending on what readers already know and what they are trying to do. |

### NSTD.5:4 - Solution

Start with the intended use and the passage. An existing reader response can establish a past result. A close comparison can show how a proposed device changes what the passage supplies. Keep a note like this when someone will use the comparison across revisions or audiences.

```text
NarrativeEngagementBoundary@Context:
  narrativeRenderingRef:
  intendedEngagementEffect:
  protectedSourceStructureRefs:
  languageStateFacetProfileRef?:
  coarseningOrPrecisionQuestion?:
  affectedReaderOrGroupRefs?:
  persuasionBoundary:
  nonAdmissibleUse:
  affectedPartyQuestion?:
  additionalClaimGrounds?:
  proposedChangeIfNeeded:
```

Choose the device for the intended use. Preserve source relations promised by an explanation and premises that govern a fictional or hypothetical account. If a literary or simplified expression makes a consequential inference ambiguous, clarify the relation. Use `C.2.LS`, `A.6.3.CSC`, `E.17.EFP` or `E.10` for the corresponding language, coarsening, explanation or precision question. Pursue evidence, assurance or ethics work when the claim or planned influence requires it.

For a design or an assessment, use the parts of this comparison that answer the question.

1. Identify the intended effect, such as attention, curiosity, emotional salience, identification, suspense, memory or willingness to continue.
2. Identify the relations, qualifications or choices the reader still needs to recover.
3. Identify the device at work or try one suited to the task. An analogy can introduce an abstract relation, an open question can invite attention, and repetition can keep a distinction available.
4. For a comparison of devices, identify what each treatment adds, changes or removes in order, salience, wording or repetition. Use an available relevant alternative where it helps. For an actual response, establish what the reader reported or did. Examine prior knowledge and other conditions when they bear on a claim about change, independent understanding or the device’s contribution.
5. Read the scenes together. After hearing one former library user describe the loss of a meeting place, an exhibition visitor can understand that person’s stakes. Placing the same testimony under “What every resident lost” extends the claim to other people. Examine what the sources establish about them. If the question concerns one person’s experience, the testimony may already suffice. Also examine consequential uncertainty, the limit of an analogy and any alternative the presentation conceals.
6. Report the finding. If an editorial choice is needed, keep, change or remove the device according to its contribution and cost. A sufficient simpler passage can be retained. Use `NSTD.6` for a qualified quality evaluation and `NSTD.8` for a learning question.

Where voice matters, use NSTD.4’s speaking relationship and its selected examples or new treatment. A joke, intimate address or repeated question can change who seems to speak and how that speaker treats the reader. Compare the passage with its surroundings and the required voice. A device developed for an essay may need changing for an instruction or a decision notice.

Select the further question by the reader’s use.

| Reader effect | Practical comparison | Further work when it matters |
| --- | --- | --- |
| Continue reading | Does the location and pacing of the passage let readers reach the needed part? For actual continuation, examine how far they read. | Change the opening, pacing or viewpoint if a revision is called for and contributes to that aim. |
| Remember a relation | What does a reader reconstruct after the relevant interval, with the stated support? | Use `NSTD.6` for a qualified recovery assessment or `NSTD.8` to design learning. |
| Care about a problem | Does the device clarify the stakes and available choices? | Examine a relevant affected-party or manipulation concern through `D.1`–`D.5`. |
| Believe a claim | Are belief and confidence appropriate to its grounds? | Inspect the source; use `A.10` when the source-to-use account is implicit or must remain replayable, and `B.3` for an actual named assurance claim. |
| Decide or act | Does the account preserve the conditions and alternatives needed for that choice? | Use the method for the actual decision if a decision is required. Its holder needs the relevant authority. |
When readers leave early, their responses or access conditions can help locate the difficulty. A different opening, example, rhythm or viewpoint may help. When they become overconfident, check whether the account omits a condition, presents a hypothesis as settled or overlooks another source of the belief. Change the passage if its contribution to the problem is established.

Artistic language can carry atmosphere, felt experience or expression. A memorial may chiefly need that quality. A technical explanation may depend on a condition its metaphor obscures. Examine language-state facets when they help settle the relevant difficulty.

Suspense may depend on an outcome that remains possible within the story, or on when the reader is given information about an outcome already fixed. Use NSTD.10 to construct a needed fictional or hypothetical alternative and NSTD.9 to assess competing readings. A withheld answer, a genuinely unsettled question and a missing premise offer different grounds for curiosity. A reader who knows the answer in advance may respond differently.

### NSTD.5:5 - Archetypal Grounding



#### NSTD.5:5.1 - Worked example: a failure story that teaches a usable distinction


In a fictional teaching case, a team follows the same checklist after its workload changes. The story can make the missing condition visible. Whether a learner identifies the mismatch and whether FPF improves real projects are different questions.

```text
NarrativeEngagementBoundary@FPFFailureStory:
  narrativeRenderingRef: FPFLearningRoute@v1
  engagementDevice: failed-use contrast with tension and repair
  protectedSourceStructureRefs:
    - pattern conditions
    - forces
    - neighboring exits
    - evaluation and improvement route
  intendedEffect: keep attention and make misuse recognizable
  persuasionOrHarmRisk: reader treats story as proof of FPF superiority or as blame of a real group
  sourceFidelityRisk: checklist failure hides the actual source relation being taught
  precisionBackoff: identify the fictional example and point to the pattern's conditions of use
  evaluationReturn: use a relevant response to assess reconstruction of the changed condition. A report of agreement addresses a different question
```

Before:

> This disaster proves why teams must use FPF.

After:

> In this fictional case, the team reused a checklist that assumed a stable workload after demand had changed. Before repeating the old action, compare its assumptions with the present workload. The case illustrates the mismatch. Whether FPF improves actual projects requires evidence from their use.



#### NSTD.5:5.2 - Worked example: an engaging homotopy image with its limiting condition


A homotopy lesson asks the learner to imagine a loop around a missing point. A loop that winds once around the missing point cannot shrink to a point by a continuous deformation that stays in the punctured plane. If the missing point is restored, the same loop can shrink in the plane. The contrast gives “slipping around a hole” its relevant boundary. Use a response to assess whether a particular learner recovered it.

```text
NarrativeEngagementBoundary@HomotopyLoopImage:
  engagementDevice: vivid analogy
  protectedSourceStructureRefs: deformation under constraints, invariant, formal definition, proof-status boundary
  intendedEffect: sustain attention through abstraction
  persuasionOrHarmRisk: low, unless used to make a false certainty claim
  sourceFidelityRisk: analogy replaces condition-bound definition
  precisionBackoff: state where analogy stops and return to formal statement
  evaluationReturn: check which deformations the learner marked as permitted or blocked if their understanding is the question
```



#### NSTD.5:5.3 - Engagement device selection matrix


| Device | Possible contribution | Risk | Repair when the risk occurs |
| --- | --- | --- | --- |
| Tension | Can sustain attention while an explanation remains uncertain. | The passage suggests that one disputed explanation is settled. | Show the existing result and the question it leaves open. |
| Failure story | Can make the consequence of a missed condition vivid. | An anecdote becomes the sole ground for blame or a general claim. | Identify a constructed case or establish what actually happened. Restore the condition that makes it relevant. |
| Analogy | Can make a selected abstract relation easier to follow. | It replaces the definition or argument needed by the use. | State the condition at which the analogy stops and make the required formal relation available. |
| Character viewpoint | Can draw attention to a participant or relation. | Prominence invites an unsupported attribution of action or responsibility. | Clarify the consequential attribution, using `NSTD.4` when its viewpoint analysis is needed. |
| Surprise reveal | Can support curiosity or memory by changing when information becomes available. | A late disclosure withholds a condition the reader needs earlier, or the account omits it altogether. | Recover a genuinely missing source relation through `NSTD.1` or reconsider its place through `NSTD.2`. If the needed relation and order are already clear, use the scene directly. |
| Humor or style | Can make a passage easier to approach or remember. | Loses a distinction needed for the later use. | Restore that distinction; use `C.2.LS`, `A.6.3.CSC` or `E.10` only for the unresolved language, coarsening or precision question. |



#### NSTD.5:5.4 - Comparing engagement choices


Compare the intended effect with the information the reader needs. An editorial walkthrough can establish what the versions express under stated assumptions. A response may show how one reader understood or experienced a version. If a selection is required, compare the alternatives on the intended use, their expressive aims and costs. To attribute a difference in reception to this device, consider other differences between versions and readers. Use `NSTD.6` when the judgement needs formal qualification.



#### NSTD.5:5.5 - Keeping the reader's use in view


Identify which reader and activity matter. Interest in an unresolved problem can help a reader explore it while leaving the grounds for belief and choice visible.

A plain version of the workload case is “When demand changes, check whether the workload assumptions still hold before reusing the checklist.” The story adds a team caught in that mismatch. Compare whether each version gives the reader the changed assumption and the next relevant check. An expert can identify those differences in the text. Observed attention, memory or a claim that the story caused an improvement need evidence bearing on that outcome. A small expressive gain may justify the longer version, and a sufficient plain explanation can stand.

A science communicator can use tension around a measured result with several live explanations. Preserve the measurement, its scope and the open alternatives. If readers use the account in a policy argument, establish which inference the scientific evidence supports. An actual policy decision has additional conditions and a decision holder.

A homotopy lesson can invite learners to imagine stretching a loop. For a task that depends on the permitted deformations, include the relevant domain and restrictions. If the passage supplies them and a response still treats every deformation as allowed, establish what contributed to that reading before revising the source content or the illustration.

A franchise continuation can use suspense, raised stakes or identification for their expressive effects. Where the brief requires continuity with established events or character choices, preserve those conditions in the device. A new artistic aim can justify a different comparison.

In live commentary, excitement can keep attention on an unfolding play. Identify the observed event, the score, any tactical inference and what awaits an official ruling. The unresolved outcome can itself supply the suspense.

The following examples show how a device can help or obstruct a particular use.

| Device | Good use | Failure mode | Repair |
| --- | --- | --- | --- |
| Hook | Raises a question the account helps the reader answer or explore. | Promises a particular answer the material never supplies. | Change a hook the author chose. When the commission requires the promised answer, supply its grounds or identify what remains open. |
| Tension | Keeps an unresolved relation worth following. | Presents a disputed explanation as a settled outcome. | Retain the live alternative and its grounds. |
| Identification | Helps readers experience a viewpoint. | Sympathy hides another affected participant or relevant alternative. | Restore the missing viewpoint or alternative where the intended decision needs it. |
| Analogy | Makes abstract structure graspable. | Replaces definition or proof boundary. | State where analogy stops and source returns. |
| Repetition | Keeps an easily lost relation available. | Repeats a slogan that obscures the relation. | Repeat the meaningful distinction; add a reconstruction attempt when learning calls for it. |
| Compression | Can make a passage usable in the available time. | Removes a distinction the reader needs at a later choice. | Retain the distinction or give the reader access to it before that choice. If the material supports only a narrower account, state its reach and return any outstanding part of the commission. Use `A.6.3.CSC` for a question about the allowed coarsening. |
| Literary style | Supports pacing, atmosphere or a felt experience. | Its appeal is used to vouch for a factual claim or for quality under another criterion. | Identify the intended expressive result and the basis for any stronger claim. Use language-state or quality guidance where that question remains open. |

Compare the actual passages and the use. A dry treatment may lose attention before a needed relation, and a vivid one may conceal its limiting condition. If either difficulty matters, change the feature that contributes to it.

Working examples for a continuing revision or team comparison follow.

```text
NarrativeEngagementBoundary@FPFLearningRoute:
  intendedEngagementEffect: motivation and memory for pattern-use reconstruction
  protectedSourceStructureRefs: EntityOfConcern; forces; solution; relations; source-return condition
  languageStateFacetProfileRef: plain teaching narrative with repeated anchors
  affectedReaderOrGroupRefs: new FPF authors and reviewers
  persuasionBoundary: may motivate study; may not prove FPF authority or tell readers to bypass checks
  nonAdmissibleUse: evidence of FPF correctness; replacement for pattern bodies
  proposedChangeIfNeeded: add a task or source cue for a missing connection, or revise the motivational claim
```

```text
NarrativeEngagementBoundary@HomotopyAnalogy:
  intendedEngagementEffect: curiosity and retention for abstract structure
  protectedSourceStructureRefs: definitions; examples; proof-status boundary; formal return
  languageStateFacetProfileRef: analogy plus formal boundary markers
  persuasionBoundary: analogy may invite exploration, not replace proof
  nonAdmissibleUse: theorem proof, formal definition, or exam solution without source return
  proposedChangeIfNeeded: restore the relevant formal condition, counterexample or source before adding a further metaphor
```

```text
NarrativeEngagementBoundary@FranchiseContinuationProbe:
  intendedEngagementEffect: suspense, identification, and stakes for private storycraft critique
  protectedSourceStructureRefs: canon constraint; continuity; character agency; causal plot support
  affectedReaderOrGroupRefs: private reviewers; no public audience permission implied
  persuasionBoundary: emotional satisfaction does not override source-pack or rights boundary
  nonAdmissibleUse: publication, canon authority, or rights claim
  proposedChangeIfNeeded: restore any continuity, agency or causal connection required by the private storycraft task
```

```text
NarrativeEngagementBoundary@LiveCommentary:
  intendedEngagementEffect: attention under unfolding uncertainty
  protectedSourceStructureRefs: observed event; provisional inference; score state; official return
  affectedReaderOrGroupRefs: listeners and any named parties if blame or harm framing appears
  persuasionBoundary: suspense and emotion do not settle blame, prediction, or official fact
  nonAdmissibleUse: final evidence, disciplinary judgment, or settled tactical analysis
  proposedChangeIfNeeded: identify the uncertainty or official source, or qualify the attribution of blame
```

### NSTD.5:6 - Bias-Annotation

Interest, confidence and sympathy can matter to a narrative’s purpose. To support a factual claim, explain its subject grounds. For a real decision or permission, identify the relevant authority and conditions. When persuasion conceals a material alternative or consequence for a reader or another affected party, examine that loss in the passage and its use.

### NSTD.5:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD5-1` | The editor identifies which reader experience or expression the device is intended to support. An observed effect is grounded in the corresponding reception. |
| `CC-NSTD5-2` | Relations and conditions needed for that use remain recoverable. |
| `CC-NSTD5-3` | Persuasion, policy, work, evidence, ethics, and assurance use boundaries are explicit when live. |
| `CC-NSTD5-4` | When the account raises a question about harm or manipulation, identify whose interests or choices it concerns at the scope the judgement requires. A claim about everyone affected needs grounds covering that group. |
| `CC-NSTD5-5` | Judge engagement by its role in the stated use. Where the task requires recovery of a source relation, assess whether that relation is available and use an appropriate response for a claim about actual understanding. |
| `CC-NSTD5-6` | For an editorial choice, compare the device’s contribution and cost with the passage without it or an available relevant alternative. For a causal claim, use a comparison that distinguishes its effect. A report of what a reader noticed or experienced can use evidence of that response. Examine an ambiguity further when it matters to the conclusion. |

### NSTD.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency as truth | A smooth account invites reliance beyond its grounds. | State what the subject evidence supports. Use `NSTD.6` for a needed recovery assessment and `A.10` when the route from source to claim is implicit or must remain reproducible. |
| Identification replacing a condition for action | Sympathy with a protagonist is taken as sufficient grounds for a choice whose relevant condition or alternative is missing. | Restore the needed condition or alternative. Examine a further policy, work or affected-party question only when the actual proposed action raises it. |
| Literary appeal treated as overall adequacy | Memorable wording is preferred even when it loses a distinction needed for the task. | Compare the passage on the intended expressive and subject requirements. Use `NSTD.6` for a needed qualified judgement or `A.6.3.CSC` to assess a deliberate coarsening. |
| Engagement taken as proof of understanding | A reader reports liking the passage. The work also requires comprehension of a relation. | Use a suitable response if understanding needs to be established. If the passage omits required material or misstates the link, repair the affected contribution through `NSTD.1`–`NSTD.3`. |

### NSTD.5:9 - Consequences

Comparing a device with a relevant alternative can identify a contribution worth retaining or a qualification its wording obscures. The cost ranges from rereading one passage to obtaining new evidence about reception where the question warrants it.

### NSTD.5:10 - Rationale

Design engages the reader through particular choices of content and expression. The same image can communicate a criterion in one account and obscure it in another. The intended use determines which comparison matters.

### NSTD.5:11 - SoTA-Echoing

Green and Brock's [transportation study](https://doi.org/10.1037/0022-3514.79.5.701) (2000) connects immersion with story-consistent beliefs. Dahlstrom and Ho's [science-communication analysis](https://journals.sagepub.com/doi/10.1177/1075547012454597) (2012) examines purpose, accuracy and whether narrative is suitable. These are historical anchors. Mengelkamp, Golke and Appel's [reading-goal experiments](https://doi.org/10.1002/acp.70036) (2025) found condition-dependent comprehension benefits, while overestimation remained across conditions. Georgiou et al.'s [narrative-memory study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11852912/) (2025) distinguishes recall, recognition and summary. These findings motivate separate attention, recovery and confidence questions; they do not establish one universally superior engagement device.

Use these source contributions for the questions they address.

- Transportation research raises the question of whether immersion contributes to a reader’s confidence in a claim. Compare the belief with its substantive grounds.
- Science-communication ethics makes the intended influence, required accuracy and choice of narrative explicit where they affect public reasoning.
- Reading-goal research motivates identifying the learning aim and assessing the resulting comprehension. Confidence in one’s own understanding is a further outcome.
- Memory research distinguishes retained gist from recalled detail. Select the aspect needed by the intended learning or later use.
- Use FPF language-state and coarsening methods when a compressed or literary treatment changes which distinctions a reader can recover. Judge quality on the declared use.

A judgement about curiosity, recall or confidence can answer the particular reception question. Use the evidence and criteria needed for any further claim about understanding or informed choice.

### NSTD.5:12 - Relations

Use `A.6.3.NAR`, `NSTD.1` and `NSTD.3` for narrative form, selected material and its connections. `NSTD.6` and `C.16.Q` help qualify the intended quality claim. Use `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10` or `A.6.P` for the particular expression, coarsening, explanation or precision issue. For a consequential value or harm conflict use `D.1`–`D.5`. For an evidence route or assurance claim use `A.10` or `B.3` when needed. `E.17` concerns publication for its audience, and `G.11` a changed source affecting the maintained result. The Semiotic and Language-Precision Bridge addresses sign and expression choices, NSTD.Reference:11 locates definitions, and the Source Use and Refresh Map helps trace a consequential source claim.

### NSTD.5:End
