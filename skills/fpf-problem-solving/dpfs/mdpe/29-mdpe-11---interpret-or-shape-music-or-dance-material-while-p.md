## MDPE.11 - Interpret or Shape Music-or-Dance Material While Performing

> **Status:** Stable

> **Pattern type:** Music-and-Dance performance-enactment pattern

> **Public result:** the interpretation realized, or material generated or changed, during performance Work

### MDPE.11:0 - Use This When

Use this pattern when prepared material, a score, choreography, generative rule, prompt, task, rehearsal result,
or configured performer is being treated as though it were the performed result.

The pattern covers cases in which a musician interprets a score, a social dancer combines learned coordinations with partner response, an improviser generates material inside a form, a live coder changes running code, or a robot uses generated material in performance. The direct Methods differ; the shared difficulty is knowing what existed before Work, what the performer could change during Work, and what interpretation was realized or material generated during that Work.
The first useful result names the prepared material and constraints, the performer and domain Method, the
interpretation or material generated or changed during Work, and the traces needed by the next decision.
It keeps the material, its descriptions, the Work, direct artifacts, and the performance occurrence distinct.

Use the direct interpretation, improvisation, live-coding, partnering, conducting, instrumental, vocal, robotic-
control, or co-performance Method first. Do not use this pattern when that Method already returns the same
material–Work result and useful traces; when alternatives still need comparison (`MDPE.9`); when capability or
configuration is missing (`MDPE.10`, `MDPE.3`); or when the current need is to produce and present the occurrence
(`MDPE.5`) or observe it (`MDPE.12`).

### MDPE.11:1 - The Recurring Difficulty

Prepared and responsive performance coexist across Music and Dance. A classical musician realizes notated
material differently on each occasion. A social dancer draws on learned coordinations while responding to music,
partner, floor, and surrounding dancers. Jazz, improvised Dance, and live coding can generate material while the
performance is already under way.

Project language often collapses several objects:

- a score, choreography, prompt, code listing, cue, or rule describes material, a Method, constraints, or some
  combination;
- musical or movement material is what a performer uses or generates; its bearer is not necessarily the material;
- world-side contact, timing, safety, instrument, latency, or participation constraints obtain or fail during
  Work; a rule card only states proposed constraints;
- the performer performs dated Work, and that Work enacts a domain Method;
- the interpretation or generated material is a result within that Work;
- a recording, code state, changed score, sensor trace, or note preserves selected traces;
- the bounded performance occurrence and its presentation to listeners, viewers, partners, or participants remain
  a separate result.

When these collapse, rehearsal success becomes a performance occurrence, an improvised change is backdated into
the score, a recording becomes “the performance”, or the performer's contribution disappears. The opposite error
is recording every micro-action, disrupting the Work and producing a trace no later decision can use.

### MDPE.11:2 - Solution

For one bounded Work, describe what was prepared, what the performer did and what resulted. Generation and performance can overlap; live
branches can repeat or return.

#### MDPE.11:2.1 - State the receiving question and performer

Name the decision that needs the result: next rehearsal, creation revision, capability demand, production choice,
comparison, teaching return, or local practice-development move. Name the performer or performing whole, the
bounded Work, and the direct Method.

The Agent who
chooses later practice development may be different. Shimon can perform marimba Work while the human team chooses
later engineering and development Work.

#### MDPE.11:2.2 - Recover what exists before Work

Open only positions that can change the performance or receiving decision:

| Before-Work position | Question |
| --- | --- |
| Material | Which rhythm, melody, texture, phrase, figure, coordination, code-produced structure, or other content is available, and which version matters? |
| Bearer or memory | How can the performer recover it: embodied memory, instrument configuration, score, choreography, recording, code, demonstration, or cue? |
| Description | Which indications guide action, and do they describe material, a Method, constraints, or several of these? |
| Proposed constraints | Which relations are intended to hold among which participants and under which conditions? |
| Obtaining conditions | Which body, instrument, partner, timing, space, latency, safety, access, or participation conditions actually bear on Work now? |

A candidate from `MDPE.9` remains material, a description, or a constraint specification under its actual kind.


#### MDPE.11:2.3 - Distinguish preservation, variation, and generation

Before Work, state only the distinctions needed by the current use:

- **preserve:** a rhythmic relation, melodic contour, partner cue, interaction rule, lyrical meaning,
  recognizability condition, or another relation must survive;
- **vary:** the performer may change timing nuance, ornamentation, path, dynamics, phrase order, code parameters,
  articulation, or partner response;
- **generate or revise during Work:** new movement, melodic continuation, running-code transformation, spatial
  response, or a new constraint may arise only as the situation develops.

These positions are decision-relative. A detail preserved for one competition, ensemble, or partner can be open
to variation in another use.

#### MDPE.11:2.4 - Perform Work under the direct Method and steer only live branches

Perform using the applicable domain Method. Several Methods may function simultaneously at different scales: a
dancer can use balance and timing, partner interaction, and an Urban Kiz performance Method in the same Work.

When current sound, movement, partner response, audience response, code behavior, equipment state, or safety can
change the next action, use current FPF situation-responsive steering. The performer selects from
available actions using current facts, the intended performance result, authority, and stop conditions. The performer uses a score,
recommendation, signal, or audience response to inform the choice.



#### MDPE.11:2.5 - Identify what interpretation or material was realized or changed

At a useful boundary, answer:

1. Which prepared material was used or interpreted?
2. Which material or operative constraints were generated, selected, transformed, or revised during Work?
3. Which preserved distinctions survived, changed, or remain unknown?
4. Which observation or direct artifact can support the next decision, and what can it not show?

Plain language is often enough: “The pair retained pulse and partner-readable weight transfer, changed the travel
path after congestion, and added one turn response; the video shows the path but not partner pressure.”

#### MDPE.11:2.6 - Preserve only traces with a use

| Receiving use | Possible direct trace | Important limit |
| --- | --- | --- |
| rehearsal or performer reflection | short audio/video segment, code state, cue note, performer annotation | recording or self-report can omit partner, body, or audience relations |
| creation revision | changed score, choreography note, diff, stem, take, marked phrase | the revision does not establish later enactment |
| technical diagnosis | sensor trace, latency log, actuation record, synchronized capture | measured features may not represent artistic or partner meaning |
| teaching or transmission | annotated example and conditions under which the distinction was recoverable | one example does not establish transfer or retention |
| later observation | occurrence locator, provenance, observer conditions, source return | observation and comparison belong to `MDPE.12` |

A direct artifact is not automatically published, accessible, current, or sufficient evidence. Use publication,
memory, and lineage patterns when those later relations matter.

### MDPE.11:3 - First Useful Result

Keep the result concise:

> - **Receiving question:** [the next rehearsal, creation, production, teaching, observation, or development decision].
> - **Performer and Work:** [dancer, musician, pair, ensemble, robot, hybrid; bounded Work and Method].
> - **Before Work:** [material, bearer or memory, descriptions, proposed constraints, obtaining conditions].
> - **Preserve / vary / generate:** [the distinctions used by this occurrence].
> - **During Work:** [current fact, choice, material or constraint generated or changed, and stop if relevant].
> - **Performed result:** [the interpretation realized or material generated or revised during the Work].
> - **Direct traces:** [artifacts or observations and the claim each can support].
> - **Unknown or unsupported:** [what the traces cannot establish].
> - **Next use or reopen:** [decision served and condition that returns the question].

Use the stated traces to support the next decision within their limits.

### MDPE.11:4 - Worked Cases

#### MDPE.11:4.1 - NDT premiere preparation and performance

The documented NDT production developed choreography, costumes, props, light, sound, stage choices, touring
constraints, and film or archive arrangements before the premiere. Those are prepared material, descriptions,
configurations, and constraints.

For the performance question, identify the dancers and other performers, direct Dance Methods, prepared movement and production material, relations that obtained, and what interpretation and material the premiere Work realized. `MDPE.5` identifies the occurrence and presentation; `MDPE.12` handles later observation and judgement.

#### MDPE.11:4.2 - Live coding

In live coding, visible code, an activated change and produced sound can be three different states. Recover which
one changed before deciding whether to revise the material, interpretation or technical timing.

In a **constructed case**, live coder Ivo and vocalist Nara perform a repeating eight-pulse passage. The low
percussion layer attacks at pulses 0, 2, 4 and 6; pulse 0 marks the start of each cycle. Their score permits Ivo
to remove or restore an interior percussion attack while retaining the cycle duration, pulse spacing and first
attack. The chosen system activates a queued code change at the next cycle boundary. That activation rule is a
condition of this example.

Nara lengthens an answer into pulse 6, where the low attack now obscures its ending. Ivo hears that collision
and chooses the permitted removal of attack 6, leaving attacks 0, 2 and 4. During cycle 22, at pulse 5, he edits
the pattern and queues it for the next boundary. The screen already shows the sparser pattern, but the old attack
at pulse 6 of cycle 22 still sounds. At the start of cycle 23 the queued pattern takes effect; its final two
pulses leave space for the vocal ending. Nara can hear that space and continues her held ending while both
performers retain the cycle's first-pulse reference. Her timing and vocal interpretation remain her contribution.

For the next rehearsal decision, the synchronized code/activation trace and short audio excerpt locate the edit,
the boundary and the sound actually produced. They show the old attack in cycle 22 and its absence from cycle 23,
with the first-pulse attack retained. Nara's report says the local monitor sound now leaves room for her ending;
the recording alone cannot supply that performer experience or show what every audience member heard.

The pair keeps the sparser variant for this passage and rehearses queuing it early enough for the intended
boundary. The extra attack immediately after the edit is consistent with the declared activation rule, so that
observation does not yet warrant repairing the sound engine. If sound instead changes after the recorded
activation boundary, reopen the technical timing account. If it changes on time but the vocal relation still
fails, reopen the material or interpretation choice. An ordinary saved pattern, excerpt and performer note that
already supports those decisions is sufficient; no second performance record is required.




#### MDPE.11:4.3 - Social dance

A dancer enters a song with learned coordinations and a domain Method. Partner response, floor density, phrasing,
and balance can change the next contribution. The dancer may preserve pulse and readable connection while changing
path, figure, timing nuance, or articulation.

The result names what was preserved, what changed, the partner relation that informed the change, and which trace
or report can support the next teaching or practice question.

When familiar figures do not supply a wanted movement quality or a usable transition, [MDPE.26](28-mdpe-26---construct-and-change-a-partnered-movement-organiza.md) develops the bodily means and their connection to partner response and musical material. It explains how to prepare the next organization's entry conditions, continue when the partner responds differently, and derive the missing practice from the failed relation.

#### MDPE.11:4.4 - Shimon generation and performance

People supplied a four-measure seed; Shimon generated the remainder and performed it on marimba. Do not assume that
composition continuation happened during marimba performance. If the sources identify separate generation and
performance Work, treat the generated continuation as prepared material for the later occurrence. Use in-Work
shaping only when timing and evidence support that claim.

#### MDPE.11:4.5 - Balboa, brushes, and event timing

Here **brushes** means drum brushes: a brush can continue sweeping on a drumhead while increased pressure articulates an audible accent. In a partnered Balboa phrase, continuous floor contact and body movement can likewise carry a distinct weight transfer. The analogy separates continuing movement from the event made perceptible within it; it does not make a foot tap, weight arrival and the partner's perceived timing identical. The [Dance profile](08-mdpe-reference-7---music-dance-and-overlapping-use-profiles.md#mdpereference72---dance-making-movement-usable-for-its-participants) gives the source and limits.

##### MDPE.11:4.5.1 - Choosing an optional articulation during a phrase

In this **constructed performance case**, a pair has prepared a repeating small-step phrase followed by a change of direction. Its agreed material fixes the transfer timing and direction change but leaves a free-leg tap optional. Both participants can already perform the simpler phrase. During one repetition, the initiating performer adds the tap before that foot accepts weight. The partner starts the direction change at the tap and then hesitates because the transfer is not ready. The performer feels the unexpectedly early response through their connection. That response warrants adjusting the phrase; it does not reveal, by itself, everything the partner perceived.

On the next repetition, while the performance continues, the performer omits the optional tap. The foot continues its sliding preparation, the body completes the transfer at the agreed point, and movement carries on into the direction change. The performer changes articulation within the prepared material; neither the transfer timing nor the next direction is newly composed. In the stipulated result, the partner continues without the earlier hesitation. After the phrase, the partner reports having taken the earlier tap-related contact change as weight arrival, whereas the second repetition made the arrival clear. The source analogy helped identify a variable to change: remove the competing accent while preserving the continuing movement and usable transfer.

The direct result is the phrase this pair actually enacts in the constructed occurrence, including that adjustment and continuation. The performer keeps the simpler version for the next repetition. Recovering an audible ornament becomes a later candidate-comparison question under MDPE.9, not an obligation to solve it during this performance. The partner's report and the observed response support that local choice; they do not demonstrate a general effect for other partners. Audio can locate the tap, video can show floor contact and movement, and a contact or force trace can indicate pressure changes. Those observations cannot replace the partner's report about the perceived event, nor does that report locate a physical force maximum.


##### MDPE.11:4.5.2 - One coordinating Method, two physical realizations

Now consider a passage that requires the accents. Its task is to retain a regular supporting pulse while placing those accents at selected positions, including positions between beats. Both can be accurate separately and interfere in combination: an accent pulls the pulse out of time, or the habitual pulse movement postpones the accent to an easier place. [RHY.11:4.4.1](../rhy/24-rhy-11---coordinate-simultaneous-rhythmic-layers.md#rhy11441---keep-a-common-time-while-allowing-different-actions) develops the common Method: recover the joint timing, prepare the accent within the continuing action, choose compatible means, correct the missed contribution and retain the required range of choices.

For **drum brushes**, use an already learned comfortable sweep as the supporting action. One practical realization keeps one hand on a repeatable circular path while the other places audible strokes or pressure accents. Relate the circle to the beat, then prepare each accent so its audible event reaches the selected subdivision while the sweeping hand continues through it. If lifting the articulating hand also lifts the sustaining hand, keep the latter's contact and shorten the former's stroke. If the stroke waits for the circle's turning point, change when its preparation starts instead of postponing the musical target. Listen for the sustained texture, the regular reference and the accent's placement; a sweep can remain audible while its period changes.

This realization adapts the progression in [*A Fresh Approach to the Drumset*, Lesson 29, printed p. 73](https://ae.vicfirth.com/wp-content/uploads/Fresh-Approach-to-Drumset-SAMPLER.pdf): repeatable legato movement, a beat-related pressure pulse, and varied articulation by the other hand. The new performance question is whether the chosen offbeat can move while the support remains regular. [Ed Soph's two-legato-hand alternative](https://www.moderndrummer.com/article/foundational-brush-technique/) realizes the same contribution distinction differently: pressure can articulate without lifting a hand. Select the means compatible with the required sound and the performer's available technique.

For a **partnered Balboa fragment**, continuous support and weight organization carry time while a free foot can articulate without accepting weight. In a constructed fragment, the pair has a supported hold through beats 1 and 2 and a planned full weight arrival at 3. A small unweighted toe contact is wanted halfway between 1 and 2; another may be wanted halfway between 2 and 3. The standing leg continues its taught pressure–release, and the free foot makes the chosen contact without moving the body's support onto it. The foot then returns along a manageable path in time to prepare the scheduled weight arrival. Early floor contact is possible without early loading.

At the full transfer, the previously free leg becomes the support. The pulse must continue through that exchange; later free-leg articulation belongs to the newly available leg. The action therefore preserves a temporal function through changing body-part roles. It cannot be implemented by freezing one leg as permanent timekeeper. If a large tap pulls the torso into premature loading, shorten or redirect that free-foot action while preserving its required accent. If the smaller action becomes inaudible when sound is required, select another available articulation or return the technique question. The partner's response checks usable weight arrival and continuation; sound locates an audible accent, and observation of loading checks a different event.

The cases share a way of coordinating: prepare and articulate a chosen event while continuing the supporting action, then assess both against the intended time. Their differences explain the required adaptations. Brushes need available contact, stroke and sound control; partnered movement needs viable support, timely role exchange and a partner-readable continuation. The common Method can guide these choices. These are source-informed constructions, not reported outcomes of a joint training trial.

##### MDPE.11:4.5.3 - Keep freedom when the passage changes

Change the accent from the midpoint of an interval to a later subdivision, then use a new short sequence of accent places. Keep the selected pulse and required accent character. A performer who can only repeat the first joint pattern still has a useful pattern, but not the range this new passage needs. If the musical reference changes tempo, relocate both the supporting events and the accents within the new intervals. Retaining old absolute accent times would lose their musical relation.

When these choices cannot yet be performed, [MDPE.10:4.6](26-mdpe-10---develop-and-test-music-or-dance-performing-capabil.md#mdpe1046---learn-to-vary-accents-over-a-continuing-pulse) develops the needed capability from this construction. During an occurrence, use an already available variant within the agreed material. Omitting an optional tap, as in :4.5.1, can solve that occurrence's problem; a phrase that requires the tap still needs a means of performing it.

#### MDPE.11:4.6 - Direct-Method stop

A chamber ensemble uses a maintained interpretation and rehearsal Method that already identifies the score
edition, interpretive choices, performers, Work, recording, limits, and return. No cross-domain integration
question remains. Use that Method directly; return to `MDPE.11` only if in-Work generation or the
material–description–constraint boundary becomes unclear.

### MDPE.11:5 - Checks and Common Repairs

| Check | Failure it prevents | Repair |
| --- | --- | --- |
| Material, description, and occurrence stay distinct | A score revision is substituted for a needed change in its performed interpretation. | Name material, bearer, performer, Work, realized result, and occurrence separately. |
| Proposed and obtaining constraints stay distinct | Proposed contact is treated as observed coordination. | Observe whether the stated relation obtained among named participants. |
| Preservation and variation are explicit | “Improvised freely” hides the Method and boundary. | State preserved distinctions, allowed change, current facts, performer authority, and stop. |
| Direct domain Method remains primary | A generic pattern replaces music, dance, live-coding, partnering, or control practice. | Use `MDPE.11` only for material–Work integration. |
| Simultaneous Methods are not a lifecycle | Multi-scale enactment becomes a fictitious sequence. | Keep simultaneous Methods separate from any teaching or Work unfolding. |
| Performer and practice developer stay distinct | A robot or performer gets authority over later development by grammar. | Name who performed and who chose later Work. |
| Trace matches the claim | Video is used as evidence of pressure, felt control, or audience response. | State what each trace can support and obtain the missing observation. |
| Recording burden is bounded | Every micro-choice becomes paperwork. | Preserve only information that can change the receiving decision. |

### MDPE.11:6 - Sources and Epistemic Boundaries

| Source or maintained result | Contribution used here | Boundary |
| --- | --- | --- |
| FPF `A.15.7` Situation-Responsive Work Steering | A bounded next-action choice from current facts while preserving domain Method, chooser, performer, authority, stop, and feedback. | It supplies no Music or Dance material, performance Method, occurrence, or artifact choice. |
| FPF `A.15.1` Work, `A.2.1` assignment, and `F.6` attribution | `A.15.1` governs dated Work, the performing Agent as a sufficiently agentic System, enacted Method, containing System, and direct result relations; `A.2.1` governs a declared assignment species and obtaining occurrence; `F.6` governs performed-Work attribution through that assignment. | These results do not determine material, interpretation, occurrence, or presentation, and an assignment does not establish Work. |
| [Live Coding: A User’s Manual](https://livecodingbook.toplap.org/book/) and [Algorave guidelines](https://github.com/Algorave/guidelines/blob/master/README_en.md) | Running-code changes and improvisatory composition during performance; visible technical Systems and public conditions. | The sources describe heterogeneous practice, not one universal Method or one local application. |
| [Kloosterman and van Kempen, NDT production case](https://doi.org/10.1016/j.ccs.2026.100710); see also `MDPE.5:4.2`, *Tell Your Mom You Love Your Skin* | Prepared choreography and production material, rehearsal integration, premiere, direct artifacts, review, and archive. | One production does not supply a universal Dance interpretation Method or moment-by-moment account. |
| [Shimon project](https://gtcmt.gatech.edu/shimon) | Robot-performed generation and marimba Work, with separate human-led engineering and practice development. | The sources do not establish in-performance generation for every occurrence or robot-held cultural authority. |
| Drum-brush explanation in the [Dance profile](08-mdpe-reference-7---music-dance-and-overlapping-use-profiles.md#mdpereference72---dance-making-movement-usable-for-its-participants), drawing on Ed Soph; constructed Balboa occurrence in :4.5 | Continuing movement and a perceptible event within it; a permitted articulation change during performance, with a partner-perceived result and next move. | The movement analogy is Method-design input. The pair and observations are constructed; they establish no empirical generalization, universal exercise order or completed capability result. |

Use a direct field Method when it supplies the same result with less burden. Keep the material–Work distinctions that change the current action or evidence.

### MDPE.11:7 - Relations

- `MDPE.9` can supply material, a description, or a constraint specification for the performer's Work.
- `MDPE.10` and `MDPE.3` can supply capability and configuration.
- `MDPE.5` identifies and presents the performance occurrence; `MDPE.12` observes and compares it.
- `MDPE.18` governs usable cultural memory and lineage when direct traces enter later continuation Work.
- Direct Music and Dance Methods govern subject Work. Current FPF governs general steering, Work, Method,
  description, evidence, and publication distinctions.
- This specialization uses applicable Systems Engineering and Method Engineering results when Systems or Methods
  are changed.

### MDPE.11:End
