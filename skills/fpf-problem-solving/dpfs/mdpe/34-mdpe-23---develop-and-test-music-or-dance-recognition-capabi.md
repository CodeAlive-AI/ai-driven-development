## MDPE.23 - Develop and Test Music-or-Dance Recognition Capability

> **Status:** Stable

> **Pattern type:** Music-and-Dance recognition-capability pattern
> **Public result:** a supported choice for developing recognition, or demonstrated recognition within the receiving use's conditions and limits; revise the distinction, signal, representation or intended population when the available basis requires it

### MDPE.23:0 - Use This When

Use this pattern when a musical, movement, rhythmic, interaction, or stylistic difference matters to a project,
but the people or agents expected to use that difference cannot reliably notice or distinguish it outside a
familiar cue, teacher example, recording, partner, venue, or label.

Examples include a dancer who can identify a style only from the song title, a partner who cannot feel the intended
weight arrival, a musician who hears a rhythm after it is named but not inside unfamiliar material, a judge whose
decision follows costume or school reputation, or recognition software that succeeds on its training performers
and fails on new ones.

The first useful result states:

- who needs the capability;
- what world-side difference must be recognized;
- what task shows recognition;
- which cues are legitimate and which would leak the answer;
- the direct perceptual, bodily, musical, dance, or machine-learning Method used to develop capability; and
- the relevant conditions of later use and the existing or newly obtained observations needed for the present claim.

Use direct ear-training, rhythm-training, movement-perception, partner-sensing, somatic, style-comparison,
perceptual-learning, judging, curation, or machine-recognition Methods for their own results. Use this pattern for
the Music-and-Dance engineering decision that remains: whether the distinction is learnable and usable by the
intended recognizers under the conditions where later Work needs it.

Do not use this pattern when:

- the project only needs observations from already capable observers (`MDPE.12`);
- performance capability rather than recognition is limiting (`MDPE.10`);
- the task is to choose, authorise, or operate a recognition-and-selection arrangement (`MDPE.13`);
- a direct domain Method already demonstrates the required recognition and transfer; or
- the distinction has no named receiving Work or decision and is merely an interesting classification.

### MDPE.23:1 - The Recurring Difficulty

A physical difference can exist without being available to a particular observer. An observer can discriminate two
examples without naming them, can name them without knowing when the distinction matters, or can recognize them in
one classroom context and fail in performance. Recognition is therefore not one undifferentiated mental event.

For this pattern, recognition capability belongs to a named holder and a named family of recognition tasks. The
holder can be a musician, dancer, partner, teacher, listener, curator, judge, performing Agent, or machine
recognizer. A population result concerns a distribution of performances by sampled members unless the population is
also an organised Agent performing collective Work.

Useful recognition tasks include:

- discriminate whether two occurrences differ in a stated respect;
- identify which distinction or category obtains;
- locate a difference in time, space, body, sound, or interaction;
- predict the next relevant change;
- notice that a learned coordination, concept, or Method applies in the current situation; and
- act on the recognized difference without the training cue giving away the answer.

These tasks can rely on different capabilities. A dancer can hear that two rhythms differ yet be unable to locate
the event that changes partner timing. A teacher can name a style but fail to distinguish its enacted movement from
a costume cue.

Three failures are especially costly:

1. **Cue dependence.** Training and test share a teacher, label, costume, recording, partner, or fixed order, so the
   cue rather than the intended distinction controls the answer.
2. **Context-bound retrieval.** The capability appears lost when music, partner, venue, body state, task, or recent
   transition changes, although the earlier response can return in its old context.
3. **A bad distinction.** Intended recognizers cannot reliably access the signal, the categories overlap for the
   receiving use, or the representation omits the relation that matters. More repetition then trains noise or a
   proxy.

Recognition must also stay separate from selection. A listener may recognize a variant and reject it. A platform
may amplify material that its users do not recognize as intended. A judge can recognize a difference without the
authority to define a culture. Demonstrated recognition supplies evidence to `MDPE.13`; it does not make the later
selection decision.

### MDPE.23:2 - Solution

Connect development, observation and receiving use. Begin from what existing observations establish, and select
the missing development or worthwhile comparison. Perception, bodily regulation, memory access, interaction and
action can function simultaneously during one recognition task.

#### MDPE.23:2.1 - Name the holder, task, and receiving use

State:

- the capability holder or sampled population;
- the Music or Dance Work in which recognition matters;
- the world-side subjects and difference to be recognized;
- the required response: discriminate, identify, locate, predict, recognize applicability, or act;
- the cost of false positive, false negative, delay, or uncertainty; and
- the later decision that a demonstrated capability can change.

“Recognize Urban Kiz” is incomplete. A usable task might be: distinguish two
movement-and-partner-interaction variants while music, clothing, and teacher cues vary, because a festival teaching
decision depends on whether learners can preserve the intended difference.

#### MDPE.23:2.2 - Ground the distinction and expose cue leakage

Use `MDPE.12` or a direct observation Method to identify the actual characteristic or relation and the indications
that make it accessible. Separate:

- the world-side rhythmic, acoustic, movement, contact, spatial, or interaction difference;
- its representation in notation, syllables, audio features, video, geometry, labels, or examples;
- cues legitimately available in later Work; and
- accidental cues present only in teaching or the dataset.

If competent observers cannot agree under a suitable task, inspect the distinction before training novices. The
right result can be a narrower category, a changed representation, a different signal, two separate distinctions,
or abandonment of the proposed distinction.

#### MDPE.23:2.3 - Establish a baseline with plausible rivals

Use an adequate existing observation when it already identifies the contribution needed for the next teaching or receiving-use decision. When a live uncertainty could change that decision, choose an attainable baseline comparison whose information warrants its burden. Same/different or alternative cases can expose answer-by-label. Observe the task result and only the timing, uncertainty or error distinctions that affect the decision. A known access failure calls for access repair; a missing lesson need not wait for another test.

Consider a rival when it could change the next action. Common possibilities include:

- the holder cannot perceive the signal;
- the signal is available but the category or boundary is unclear;
- the distinction is recognized but the required action cannot be performed;
- cue conflict, attention, fatigue, pair coordination, or current conditions block expression;
- earlier learning is retrieved only in its old context; and
- the proposed distinction does not support the intended use.

Do not call every wrong performance a recognition failure. A capable listener can identify a rhythm that the same
person cannot yet play; a dancer can recognize a partner cue but lack movement capability to answer it.

#### MDPE.23:2.4 - Develop capability through varied but relevant tasks

Choose the direct domain Method from the failure. Examples include:

- contrastive listening with matched distractors;
- singing, clapping, stepping, movement, or partner response tied to the same rhythmic relation;
- changing tempo, instrument, performer, view, orientation, body, partner, or venue while preserving the target
  difference;
- moving between notation, syllables, sound, movement, force, and geometry only when the correspondence is taught;
- fading labels, teacher demonstrations, fixed order, or costume cues;
- interleaving neighbouring styles or variants when discrimination is the goal; and
- training machine recognizers on varied carriers and performers while protecting a held-out transfer set.

Vary contexts expected in later Work or needed to distinguish rival
explanations. Preserve protected conditions such as safety, consent, fatigue bounds, accessibility, and cultural
source integrity.

#### MDPE.23:2.5 - Probe context-dependent access before declaring loss

The COIN model treats sensorimotor adaptation as contextual inference over several memories. Broader work on memory
also reports context dependence, but one common computational account for all kinds of memory remains an open
hypothesis. Use the hypothesis when it changes a cheap discriminating probe.

When a previously demonstrated response becomes unavailable, compare the live explanations with the next action they would justify. Lost support, changed demand, fatigue, inaccessible cues and context-dependent expression can call for different responses. If the available observation already selects an adequate repair, use it. If several explanations still permit the same worthwhile next action, proceed under that stated uncertainty.

Choose a context comparison only when its attainable result could change teaching, support or the warranted receiving use enough to justify the effort and delay. A brief return to earlier successful conditions without reteaching may help; alternatively, hold those conditions fixed while changing one suspected cue. Compare practice order or an unfamiliar setting only when switching or generalization is the unresolved question.

Interpret the actual response with the changed conditions and support preserved. Reappearance shows availability in that condition; it does not establish the COIN mechanism or exclude other explanations. Failure to reappear may leave several explanations unresolved. Retain only distinctions needed for the decision, such as recovery, interference or a still-unobserved transfer. Return the supported teaching or use choice, with the uncertainty that changes it, and stop when that question is answered. MDPE.17:3.4 develops the same proportionate context comparison for transmission.

#### MDPE.23:2.6 - Test transfer without the teaching answer

When the receiving decision needs a transfer claim, use matching existing evidence or held-out examples and changed conditions representative of later Work. Preserve the target relation while changing irrelevant cues. Include a delayed observation when retention matters to that use. A current teaching choice can instead close with the supported next action and its limits; it need not commission every stronger capability test.

For a human recognizer, choose a response that demonstrates the target recognition without requiring an additional performance capability. For machine recognition, hold out performers, recordings, devices, venues, or
styles according to the intended use and inspect error distributions rather than one average score.

Return one of these useful results:

- a supported next development choice, with uncertainty that affects its use;
- demonstrated recognition within named transfer limits;
- recognition that remains dependent on a named cue or context;
- evidence that access or representation, rather than learning, is limiting;
- recognition without the performance capability needed for later action;
- a revised distinction, task, signal, representation, or intended population; or
- an unsupported claim naming the missing Method, access, examples, capability, or evidence.

### MDPE.23:3 - First Useful Result

> **Recognition-capability result**
>
> - **Holder and receiving Work:** [musician, dancer, partner, teacher, listener, judge, performing Agent, machine
>   recognizer, or sampled population; later use].
> - **Recognition task:** [discriminate, identify, locate, predict, recognize applicability, or act].
> - **Grounded distinction:** [world-side difference; legitimate indications; representation and omissions].
> - **Available recognition basis:** [existing observations or selected comparison; relevant cues, help, errors and limits].
> - **Development Method:** [direct perceptual, musical, dance, bodily, partner, or machine-learning Method].
> - **Context probe, if a previously demonstrated response fails and a comparison that could change the next action is worth its burden:** [earlier successful conditions, controlled return or change, observed recovery or interference, remaining rival explanation].
> - **Transfer or retention basis, when needed for the claim:** [matching existing evidence or selected new observation and its conditions].
> - **Result:** [supported development choice, demonstrated capability within its limits, changed distinction, or unresolved basis; distinguish these claims].
> - **Next use:** [performance development, observation, changed-condition use, transmission, or selection design].

### MDPE.23:4 - Worked Cases

#### MDPE.23:4.1 - Balboa weight arrival and brush articulation

A teacher wants dancers to distinguish audible brush onset, weight arrival, perceived beat centre, and
partner-readable pressure. These events can be related but are not identical. The capability holder can be a
dancer performing a solo discrimination task or a partner sensing the relation through contact.

Use sound, video, contact or force indications, partner reports, and direct Balboa teaching. Fade verbal labels,
vary music and partner, and test unfamiliar articulations. Success means the dancer or partner can make the stated
discrimination under the intended conditions; it does not prove whole-style recognition or performance mastery.

#### MDPE.23:4.2 - A multidance recognition-transfer trial

This constructed project example tests recognition rather than performance quality. A learner must notice which
of two taught partner-coordination variants is current before responding. In variant A, the signalling partner
begins the torso/contact cue for redirection while completing the preparatory weight transfer. In B, that cue
follows the completed transfer and a one-pulse pause. The contact change's timing relative to the transfer and
pause is the legitimate indication. These are the two specified task variants, not definitions of whole genres. The pair's enacted timing and contact
supply the distinction. A music label, track title, teacher voice, costume or fixed presentation order can leak
the answer; the partner's changing timing and contact remain legitimate cues in the receiving task.

The receiving use is a supported partner-response exercise in which either participant can pause before the
next direction change. The learner says A or B within one agreed pulse after the cue, before trying that
direction change. The teacher checks the partners' enacted cue against the demonstrated references; an incorrectly
presented cue is not scored as the learner's recognition error. Late answers and abstentions are unsuccessful
recognition responses, although stopping remains available.

For this exercise the teacher sets a local entry criterion of at least ten correct, timely responses in twelve
held-out trials under the intended conditions. That criterion permits trying the subsequent supported response
task; it does not establish movement fluency, a population accuracy rate or readiness for unrestricted social
performance. The counts below use this response rule.

Before additional teaching, the learner identifies the current coordination in eleven of twelve trials with the
familiar teacher-partner but only six of twelve with an unfamiliar partner and matched music. Errors follow the
expected style of the track even when the partner enacts the other coordination. Returning to the familiar room
and teacher-partner without reteaching restores eleven of twelve correct responses.

This result makes context dependence a useful current explanation, but the probe changes room and partner
together. It does not distinguish retrieval of a context-linked memory from teacher-partner cue leakage, access
to the enacted timing-and-contact signal, the COIN mechanism, or another explanation. If the mechanism changes
the next teaching decision, vary familiar and changed rooms separately from familiar and unfamiliar partners.

The selected direct teaching Method uses contrastive partner-sensing tasks, matched musical distractors, rotating
partners, randomized order, and gradual removal of labels. The recognition response is only a spoken A/B
indication after a short partner cue and before the learner performs the target coordination. Inability to perform
the subsequent movement therefore cannot be counted as a recognition error.

A held-out test uses two unfamiliar partners and previously unheard excerpts, without supplied answers or style
labels in the prompts. The learner identifies ten of twelve trials. In a second matched block, the signalling
partner first presents A and then B in
rapid succession while retaining the current recording and partner. The next recognition cue is independently
selected as A or B, so the preceding movement sequence does not disclose the answer. The learner identifies
seven of twelve cues. The changed condition is the recent movement-task transition. If a later trial also changes
the recording, report the combined condition separately.

The result is demonstrated recognition transfer within the tested music and partner conditions, with a remaining
transition-sensitive limit. It is not performance fluency, authority to classify entire styles for others or
evidence that the practitioner population selects either variant.

The ordinary held-out block meets the exercise's entry criterion; the rapid-transition block does not. Retain
the first result for its tested conditions and work on the transition limit before including rapid switches in
the receiving exercise. The teacher stops adding blocked repetition and selects interleaved transition practice
and a later check for that remaining question. If distinguishing retrieval from cue access would change the
intervention, use the room-by-partner comparison above. If performance fails after a correct recognition response,
move to `MDPE.10`. If competent recognizers cannot maintain the distinction across the intended contexts, revise
the distinction or receiving use instead of drilling a leaking cue.

#### MDPE.23:4.3 - One rhythm through several representations

A learner must recognize a rhythmic phrase when its entry moves within a continuing cycle. Sound, notation and
movement can expose different parts of that relation. First establish what each representation retains:
beat-position syllables identify where an onset falls within a beat; a learned solkattu phrase can keep its syllabic
grouping when its entry moves. [RHY.5:4.2 through RHY.5:4.3](../rhy/18-rhy-5---choose-a-rhythmic-representation-for-the-intended-wo.md#rhy542---match-the-convention-to-the-rhythmic-content)
explains these conventions and the independent reference needed to interpret them.

In this constructed lesson, a four-beat cycle has beats at 0, 1, 2 and 3; the next cycle begins at 4. The learned
phrase is **ta–ki–ta**, with three onsets half a beat apart. Compare its initial entry with an entry half a beat
later, keeping that spacing and the continuing beat cycle. For the position reading, use the duple Takadimi
convention: **ta** names the beat onset and **di** its halfway point.

| Representation | Entry at beat 0 | Entry half a beat later |
| --- | --- | --- |
| Onset times, in beats from the same cycle origin | 0, 0.5, 1 | 0.5, 1, 1.5 |
| Learned phrase syllables, placed at those times | ta–ki–ta | ta–ki–ta |
| Takadimi position syllables, placed at those times | ta–di–ta | di–ta–di |

Construct the second reading from the timed phrase: retain its order and spacing, add the displacement to each
onset, then name the resulting beat positions. Keep the cycle running while demonstrating or listening. Restarting
the cycle with the phrase would erase the displacement; retaining the old position syllables would misstate it.
If an onset crosses a cycle boundary, retain which cycle it belongs to and its place in the phrase.
[RHY.6](../rhy/19-rhy-6---translate-a-rhythm-without-erasing-needed-distinctio.md)
develops this translation and the return to the source rhythm.

For a receiving task that needs recognition across representations, present an unheard entry with an audible or
visible cycle reference and ask the learner to locate the phrase's onsets, then translate them into the other
convention. Withhold the answer labels. An unchanged syllable string alone cannot establish unchanged placement.
Use the response to decide whether the learner needs help recovering the reference or applying the correspondence.

Correct recognition does not establish simultaneous phrase-and-cycle performance. When that performance is the
missing capability, use the worked construction in
[RHY.11:5.2](../rhy/24-rhy-11---coordinate-simultaneous-rhythmic-layers.md#rhy1152---phrase-accents-need-not-follow-every-beat-gesture)
and its practice in
[RHY.12:5.1](../rhy/25-rhy-12---develop-rhythmic-capability-through-representative.md#rhy1251---phrase-and-gesture-keep-different-groupings).

#### MDPE.23:4.4 - Scene-recognition claim with no Method

A proposed Algorave event or Tarraxo teaching variation is said to be recognisable to a relevant scene. Current
guidance can supply material, programme, teaching, and observation choices, but the available sources do not
supply the population, competence criterion, comparison task, transfer test, and result needed to support the claim.

Either recruit suitable recognizers and design a bounded study, lower the claim to an identified practitioner
judgement, or leave the recognition claim open. Attendance, teacher approval, platform counts, and one participant
report do not become scene recognition.

#### MDPE.23:4.5 - Machine recognition

A classifier distinguishes dance or music variants in its training recordings. Hold out performers, recording
conditions, devices, tempi, and neighbouring styles according to the intended use. Inspect which cues drive errors
and whether the model can abstain when the distinction is unavailable.

Classification transfer establishes only the stated machine capability. It does not establish understanding,
authority, cultural membership, or permission to judge people.

#### MDPE.23:4.6 - Direct-Method stop

An ear-training Method already defines the interval distinction, matched examples, cue fading, varied musical
contexts, delayed transfer test, error interpretation, and next lesson. Use it directly. `MDPE.23` is unnecessary
unless the Music-or-Dance project must connect that capability to another recognizing population, representation,
interaction, or cultural decision.

### MDPE.23:5 - Checks and Common Repairs

| Check | Failure | Repair |
| --- | --- | --- |
| Holder and task are named | “The audience should recognize the style.” | Name the sampled people or Agent, recognition task, context, response, and later use. |
| Distinction is grounded | A label or representation becomes the thing recognized. | Name the world-side sound, movement, rhythm, interaction, or relation and how it is accessed. |
| Recognition differs from performance | A wrong movement is treated as proof of failed perception. | Use existing evidence or a small separating response when that distinction changes the next action; address performance through MDPE.10 where needed. |
| Cue leakage is controlled | The teacher, costume, file name, or fixed order gives the answer. | Match irrelevant cues, fade prompts, randomise order, and use held-out examples. |
| Variation serves transfer | More contexts are added without a receiving use. | Vary conditions expected in later Work or needed to distinguish rival explanations. |
| A context probe answers a worthwhile question | Reappearance in the old context is called relearning. | When the distinction can change the next development action enough to warrant a comparison, return to earlier successful conditions or vary one relevant cue. Preserve uncertainty about the mechanism. |
| Human and machine claims retain their kinds | Classifier accuracy becomes cultural understanding. | State the task, holder, data, conditions, error distribution, and non-use boundary. |
| Recognition differs from selection | A capable recognizer is treated as authorised judge or curator. | Pass capability evidence to `MDPE.13`; establish authority and selection separately. |
| The distinction can be changed | Repetition continues despite ambiguous or inaccessible categories. | Revise the signal, representation, boundary, population, or intended use; abandon the distinction when needed. |
| Direct Methods remain primary | A cross-domain pattern replaces ear training, Dance pedagogy, partner sensing, or ML evaluation. | Use each direct Method for its result and retain only the cross-result Music-and-Dance decision here. |

### MDPE.23:6 - Sources and Epistemic Boundaries

Compare development Methods by their expected gain, burden, protected conditions and receiving use. A claimed recognition capability needs compatible evidence about the recognizer's response to the relevant Music or Dance distinction; use an adequate result already available or obtain a worthwhile missing observation. A supported teaching choice need not wait for a stronger capability claim.

| Source or maintained result | Contribution used here | Boundary |
| --- | --- | --- |
| [Heald, Lengyel, and Wolpert, *Contextual inference underlies the learning of sensorimotor repertoires*](https://doi.org/10.1038/s41586-021-04129-3) and [*Contextual inference in learning and memory*](https://doi.org/10.1016/j.tics.2022.10.004) | Context-sensitive creation, expression, and updating of memories; discriminating return and cue-variation probes. | The first model is sensorimotor; one identical computation for every memory and every agent remains an open hypothesis. |
| [Makarome, *South Indian Konnakkol in Western Musicianship Teaching*](https://ir.upsi.edu.my/files/docs/2020/2114_2114.pdf), especially p. 38 | Distinguishes beat-position syllables from retained phrase groupings under displacement; supplies the distinction used in :4.3. | The timed example here is constructed. The article's teaching experience and feedback do not establish this learner's recognition or performance. |
| Context-dependent recall and transfer (unpublished source note) | Multidance switching and blending cases, rival explanations, and human and ML probes. | The note supplies hypotheses and source leads, not a general Method or an established cross-domain result. |
| Balboa, Brushes, Pulse, and P-Center (unpublished source note) | Continuous carrier, articulation, several timing centres, partner feedback, and interleaved recognition tasks. | It does not prove one universal exercise order or transfer to all performers. |
| [Wood et al., *The Global Jukebox*](https://doi.org/10.1371/journal.pone.0275469); comparison methods in `MDPE.12:6` | Recordings, coding guides and coder training make selected musical distinctions available for comparison; reliability differs by characteristic. | Agreement on a coded feature does not establish its recognition or meaning for a different population. |
| [Whitehead et al., *Capturing spontaneous interactivity*](https://doi.org/10.3389/fpsyg.2024.1465595) | Compare kinematic coordination measures with the improvising dancers' reports; their disagreement can change the recognition task or observation method. | These observations do not establish audience recognition of the proposed style distinction. |
| [Dawou Tarraxo, TOCA Method: student book and teacher guide](https://tocamethod.com/) | A teaching approach combining touch, observation, control and awareness, with individual and partnered exercises and progressions. | This is one practice-specific teaching approach; its description alone does not demonstrate recognition or transfer by the current learners. |

Prefer contextual inference over a live rival only when observations support that comparison. Otherwise retain it as a hypothesis where it helps identify a worthwhile comparison; a shared useful next action can proceed while the explanations remain unresolved.


### MDPE.23:7 - Relations

- `MDPE.12` supplies grounded observations and can expose whether recognition, signal access, representation, or
  comparison is limiting.
- `MDPE.10` concerns capability to perform Music or Dance Work; recognition can be present without performance and
  performance can follow contextual cues without explicit recognition.
- `MDPE.13` can use demonstrated recognition capability for the same people or agents, distinction, conditions, and
  transfer limits. Capability neither authorises nor performs selection.
- `MDPE.6` and `MDPE.17` can use recognition evidence when changed-condition use or receiving enactment depends on
  noticing the relevant difference.
- When capability development is selected, [FPF E.23.CDI](../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/64-e-23-cdi---developing-capability-for-a-named-work-family.md)
  guides the baseline, target, limiting contribution, protected conditions and representative transfer check.
  Direct Music and Dance Methods still supply the intervention.
- When a previously demonstrated response fails after conditions change, competing explanations would change
  the next teaching or support decision, and an attainable comparison is worth its burden, use [FPF E.23.CAE](../../sections/11-part-e---the-fpf-constitution-and-authoring-guides/65-e-23-cae---capability-access-and-expression-differential-pro.md).
  Compare a qualified reference condition with a controlled change without further teaching; distinguish whether
  the response is selected as applicable, accessible, expressed and enacted, while retaining surviving explanations.
  The probe supplies observations for the later choice; it neither selects the intervention nor establishes a memory mechanism.

### MDPE.23:End
