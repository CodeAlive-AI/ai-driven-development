## MDPE.30 - Construct a Rhythmic Part from a Seed, Phase and Action Rule

**Type:** Method
**Status:** Stable
**Normativity:** Normative

### MDPE.30:1 - Problem frame

**Use this when** a performer or arranger has promising cyclic rhythmic material but still needs a part that places sounds and actions in the right relation to an accompaniment. The intended result includes the phase, audible pattern, action allocation and instruments, with a reason to use that combination under the receiving conditions.

The construction uses a fixed unit-pulse grid and explores two alternating-hand rules. Begin with an already usable seed or construct one through a method appropriate to the musical task; section 5.1 fully derives the three-onset, eight-pulse seed used here. Other counts can use Toussaint's chapter-21 algorithm or another qualified input. Generating every possible seed is outside this method. If an existing part already serves the musical task, use it.

### MDPE.30:2 - Problem

A cyclic onset pattern leaves several musical decisions open. Its shape does not determine where it begins against another part, which hand produces each sound, whether the action pattern repeats at the same boundary or whether the performer can realize it. A changed accompaniment can invalidate one of these relations while leaving the geometric pattern unchanged.

The problem is to construct their joint realization and revise the affected part when the receiving work changes. Rehearsing an incompatible action rule more carefully cannot produce a sound relation that the rule itself excludes.

### MDPE.30:3 - Forces

| Concern | Consequence for construction |
| --- | --- |
| Cyclic shape and fixed musical origin | Rotations can preserve spacing while changing entries, collisions and silences against the accompaniment. |
| Audible attacks and intervening actions | Alternating attacks and alternating motions on every pulse can produce the same onset pattern with different sounds and bodily demands. |
| Local phrase and continuing performance | The rule must be continued across the boundary to determine the period of the whole part. |
| Preserved relation and changed span | Stretching, adding rests and splicing preserve different properties; the wanted musical relation selects the operation. |

### MDPE.30:4 - Solution

Construct the part as a relation between rhythmic material, the receiving musical frame and a way of producing the sounds. Choose only the operations the present difficulty needs. A given seed need not be regenerated, and a sufficient phase or action allocation can remain while another relation changes.

#### MDPE.30:4.1 - Recover the seed and place it in the receiving music

Represent the cycle with its number of unit pulses and the positions of its onsets. Include the gap from the last onset back to the next cycle's first one. Establish the seed's musical purpose: it might preserve a known figure, explore a spacing property or provide material for a changed arrangement.

Fix the origin from the receiving work, such as an accompaniment entry or shared phrase boundary. State the sound or silence that matters there and at other consequential landmarks. To try a phase shift of s pulses in an n-pulse cycle, replace each onset position p with (p + s) modulo n. Compare the resulting positions with those landmarks. Moving every onset while leaving the accompaniment fixed changes the musical relation; merely renaming the coordinates does not.

If no phase supplies the needed relation, return to the seed, the receiving constraint or the arrangement. Do not discard useful rhythmic material solely because one placement fails. Conversely, keep a sufficient placement without enumerating all rotations when the choice is already settled.

#### MDPE.30:4.2 - Construct the action and sound allocation across the boundary

Choose which events advance the alternating-hand rule. When hands alternate on audible attacks only, successive onsets take successive hands; silent pulses do not advance it. Continue through the cycle boundary. With an odd number of attacks, the next cycle starts on the other hand, so the hand-labelled assignment returns after two cycles. With an even number, it returns after one cycle. The audible timbral period also depends on whether the instruments and strokes distinguish those hands.

When hands alternate on every pulse, each successive pulse advances the motion, and the onset pattern determines which motions sound. The other motions remain part of the performed method. With an even number of pulses, the hand allocation returns at the cycle boundary; with an odd number, it changes hands there. This rule changes the amount and organization of movement even when the onset positions are unchanged.

Map the actions to available instruments and the wanted audible differences. Examine at least the span needed for the combined sound and action arrangement to recur, including its relation to the accompaniment. Compare a simpler allocation when it serves the same musical result. If the wanted hand or sound at an entry contradicts the chosen rule, change the rule, phase, instrument assignment or receiving condition. If the rule permits it but the performer cannot yet realize it, the next question concerns capability or another playable allocation.

#### MDPE.30:4.3 - Change the span by the relation that must survive

Identify what must remain: exact onset times, relative spacing, hand blocks, transition gaps, entry sound or another musical relation. Scaling all intervals, appending silence and inserting a segment give different answers. Derive their consequences before choosing the operation.

For the smooth-toggle family shown in section 5.4, the wanted relation is a right-hand onset block followed by a left-hand onset block, with a three-pulse gap at each transition. The seed is eight pulses long, with onsets at 0, 2 and 5 under pulse-wise alternation. At each extension, split the current cycle into equal halves. Copy the two pulses immediately before the split and the two immediately after it, and insert that four-pulse segment between the unchanged halves. The even insertion preserves the parity of the shifted motions; it adds one sounded stroke to each block while retaining the two transition gaps. Repeating that construction gives longer members of this family. It is a specific generator for that retained relation, not a rule for lengthening any rhythm.

After changing the span, return to the accompaniment, entry and performing demand. A twelve-pulse part can be arithmetically correct yet unsuitable for an arrangement that still requires the original eight-pulse return. The useful result is the part that serves the joint music, or a concrete reason to revise that music or retain another part.

#### MDPE.30:4.4 - Try the receiving part and retain the usable result

Compare the selected arrangement with the tempo, reference cues, instruments and partners required by the next use. Reuse adequate observations where those conditions still apply. When an unresolved performing consequence matters, try the part under those conditions: listen for the wanted entries and silences and observe the actions needed to sustain them. A wrong sound caused by unintended contact may call for a different realization or practice; a wrong first hand dictated by odd attack count calls for a changed rule. The diagnosis follows the relation that failed.

The useful result identifies the onset pattern and fixed origin, hand/action rule, instruments and audible differences, receiving accompaniment, selected alternative and grounds for the claimed use. A completed score can finish the construction; a demonstrated performing use additionally needs the corresponding observations and conditions. Timing geometry, a Method for generating or performing it, understanding the construction and acquiring the performance remain different results. The [style and acquisition account](52-mdpe-application-5---participation-learning-recognition-and.md#mdpeapplication53---connect-style-method-structure-and-acquisition) explains this distinction when teaching the operation.

`MDPE.9` can use the generated alternatives, `MDPE.3` their performed combination and `MDPE.10` a missing capability. For broader rhythmic comparison, transformation or coordination, use Rhythmics RHY.7, RHY.8 and RHY.11 or the applicable specialist method. Stop at the constructed part or supported receiving result when it answers the current question.

### MDPE.30:5 - Archetypal Grounding

The following arrangement, constraints and rehearsal outcomes are constructed examples. Toussaint supplies the rhythmic and action constructions. The examples show how receiving requirements select and change their use; they report no experiment on these performers or universal ranking of musical quality.

#### MDPE.30:5.1 - Generate the small seed and choose its phase

An ensemble wants three audible attacks in a repeating eight-pulse span. Its pulse 0 is fixed by the accompaniment. Another instrument has a cue at pulse 6, where this new part should remain audibly silent. The percussionist has a low-sounding instrument for the right hand and a contrasting high-sounding instrument for the left. The first musical question is whether a two-cycle timbral exchange works with the accompaniment.

Use `x` for an audible onset and `.` for a silent pulse. For this specific seed, begin with three onset columns and five silent pulses. Give each onset one silent pulse, leaving two; append the remaining two to the first two columns. Read each column downwards and concatenate:

```text
initial groups:       [x]   [x]   [x]     remaining: . . . . .
after first sharing:  [x .] [x .] [x .]   remaining: . .
after second sharing: [x . .] [x . .] [x .]
concatenated:         x . . x . . x .
positions:            0 1 2 3 4 5 6 7
```

The onsets are 0, 3 and 6. Their cyclic gaps are 3, 3 and 2, including the return from 6 to the next cycle's 0. There are three onsets, eight positions and gaps differing by at most one pulse. These facts establish the selected construction, not its musical value. For a different number of onsets or pulses, use the chapter-21 repeated-distribution algorithm or an already qualified seed; the particular two-sharing calculation above is not a general formula for every pair of counts.

The seed places an attack on the other instrument's cue at 6. Rotate every onset forward by two positions, wrapping at 8: 0 becomes 2, 3 becomes 5, and 6 becomes 0. The ordered result is 0, 2, 5, with gaps 2, 3, 3. It preserves the cyclic spacing family and attack count, includes the fixed pulse 0 and leaves pulse 6 silent. This rotation changes the relation to the accompaniment even though a comparison of unanchored cyclic shapes treats the two patterns as equivalent. Merely rotating the diagram's labels would not change the performed phase.

#### MDPE.30:5.2 - Turn the onsets into actual hand and sound parts

First alternate hands on **audible attacks only**. Begin with the right hand and continue alternation across the cycle boundary; do not restart the rule at each bar. Three is odd, so the next cycle starts with the other hand.

| Eight-pulse span | Pulse 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| First cycle | R | . | L | . | . | R | . | . |
| Second cycle | L | . | R | . | . | L | . | . |

Here R and L are audible strokes on the respective instruments. The combined onset pattern repeats after eight pulses, but the hand and timbre assignment repeats after sixteen. In one sixteen-pulse span, right-hand attacks are at 0, 5 and 10, and left-hand attacks at 2, 8 and 13. Those two parts were generated by an action rule; they were not inferred from the onset polygon alone.

The ensemble compares this with playing all three attacks on one sound. The single-sound alternative preserves timing and costs less coordination but removes the proposed timbral exchange. In the constructed rehearsal, the percussionist can perform the alternating-attack version at the agreed 72 pulses per minute with the audible reference retained, and the partner musician reports that pulse 6 remains clear. The ensemble keeps it for the next rehearsal because the two-cycle exchange serves that arrangement. This is a stipulated bounded receiving decision, not a measured long-run reliability or a causal claim that the generation algorithm improved music.

#### MDPE.30:5.3 - Change the receiving condition without confusing the two action rules

The accompaniment is revised: the low right-hand sound must now mark pulse 0 **of every eight-pulse cycle**. The alternating-attack version fails this condition by construction, even when played perfectly. More practice of that same rule cannot fix the alternating first sound.

Compare a second action rule from chapter 32. Alternate the hands on **every pulse**, including silent motions, and sound only positions 0, 2 and 5. Capitals below mean audible strokes; lowercase letters mean the indicated hand moves without an audible attack, stopping short or using an appropriately silent motion.

```text
pulse:   0 1 2 3 4 5 6 7
motion:  R l R l r L r l
sound:   x . x . . x . .
```

Eight is even, so this hand allocation repeats at the next cycle. The first two audible attacks are right-hand strokes and the last is left-hand: it is the chapter-32 smooth-toggle seed. The audible spacing and silence at 6 remain; the timbral organization and movement demand change. Instead of three audible strokes with alternation between them, the performer maintains eight alternating pulse motions. That can help one performer and burden another. Silent movement is not a silent instruction to skip the movement.

In the constructed return, the percussionist first sounds an unintended stroke at 4. The ensemble slows the passage, separates audible from silent motions, then returns to the same receiving tempo and accompaniment. Once the required sound pattern and entry are demonstrated under those conditions, it selects this version for that use and retains the two-cycle version for the earlier arrangement. If the performer cannot obtain the required silent motion reliably in the available preparation time, choose a playable allocation or change the instrumentation, entry demand or rehearsal commitment.

#### MDPE.30:5.4 - Extend the phrase while preserving a chosen action relation

Suppose a later arrangement has a twelve-pulse span and still wants a block of right-hand attacks followed by a block of left-hand attacks, with the same three-pulse gaps at the two transitions. Stretching every old interval by 1.5 would move the attacks off the new unit-pulse grid. Adding four rests would keep the old onsets but break the chosen transition spacing. Neither operation supplies the requested relation.

Use chapter 32's splice instead. Cut the eight-pulse motion after position 3. Copy its four-pulse transition segment at original positions 2–5, then insert that copy between the two halves:

```text
first half       inserted transition    second half
R l R l          R l r L                r L r l

new positions:   0 1 2 3 4 5 6 7 8 9 10 11
new motion:      R l R l R l r L r L r  l
```

The result has right-hand attacks at 0, 2 and 4 and left-hand attacks at 7 and 9. Its cyclic gaps are 2, 2, 3, 2, 3. Five attacks replace three, the span becomes twelve, and the selected hand blocks and three-pulse transitions remain. Inserting an even number of pulses preserves the parity of the shifted hand motions.

The new part still needs its relation to the revised accompaniment and the performer's capability. If the accompaniment actually keeps an eight-pulse landmark, the twelve-pulse construction is not an adequate replacement merely because the arithmetic works. Retain the eight-pulse part or reconsider the joint arrangement. If twelve pulses are intended, try the new part with those receiving landmarks and compare the audible transition, effort and entry.

### MDPE.30:6 - Bias-Annotation

The equal-pulse representation makes spacing and alternation calculable. It does not represent every timing nuance or determine a tradition's musical criteria. The two-hand cases are specific action constructions. An electronic instrument can reproduce their sounds through different actions, and a performer with another physical arrangement needs an appropriate realization rather than an automatic transfer of this hand technique.

### MDPE.30:7 - Conformance Checklist

- The seed's onset positions, cycle length and last-to-first gap are recoverable.
- The phase is related to a fixed receiving origin and the entries or silences that matter.
- The action rule states whether attacks or all pulses advance it and continues across the boundary.
- The action allocation and instruments produce the wanted sound relation over the needed repeated span.
- A changed span preserves the selected relation by a stated construction and is compared with the receiving accompaniment.

Inspecting the score can settle those structural questions. A claim that the performer can use the part requires adequate receiving-performance evidence with the assistance and conditions that will actually remain. Reuse matching observations or obtain a receiving trial when needed. Broader reliability or learning claims require their own grounds.

### MDPE.30:8 - Common Anti-Patterns and How to Avoid Them

| Invited mistake | Repair |
| --- | --- |
| Treat cyclic rotations as interchangeable against a fixed accompaniment | Compare actual entries and silences with the unchanged receiving origin. |
| Restart hand alternation at the bar line without changing the stated rule | Continue the rule through the boundary and determine the complete hand-labelled period. |
| Practice an allocation that structurally gives the wrong entry sound | Change the rule or arrangement; reserve practice for an attainable performing result. |
| Extend a part by a convenient arithmetic operation that loses its musical relation | Choose the preserved relation first, derive the changed part and check the join with the accompaniment. |

### MDPE.30:9 - Consequences

The arranger obtains a constructed part whose geometric, timbral and action relations can be explained and changed separately where the music permits. A phase or rule change may solve the problem with the same seed. The cost is considering the combined repeated span and the actual performing demand.

### MDPE.30:10 - Architectural Rationale

Rhythmic material becomes a part through its place in the music and the actions that produce it. Keeping these relations together explains why one unchanged onset polygon can support different performances and why a changed receiving condition returns to a particular construction. The method combines specialized generation and allocation with a musical choice.

### MDPE.30:11 - SoTA-Echoing

| Source and use | Adopted or adapted contribution | Boundary and alternative |
| --- | --- | --- |
| Toussaint, *The Geometry of Musical Rhythm*, second edition, 2020, chapter 21, especially Figure 21.2 | Use the explicit three-onset, eight-pulse construction and the distinction between a spacing family and its performed phase. | Other seeds may be supplied by the chapter's general algorithm or another qualified construction. The shown calculation is not that whole algorithm. |
| Toussaint, chapter 31, “Alternating-Hands Method”, pp. 218–220 | Adapt alternating audible attacks into hand and sound parts, continuing the operation across the boundary. | A known adequate part or simpler allocation can answer the musical task at lower performing cost. |
| Toussaint, chapter 32, pp. 225–230, especially Figures 32.1–32.2 | Adapt pulse-wise alternation and the smooth-toggle splice into an arrangement with explicit receiving conditions. | The family construction preserves specified relations; it establishes neither universal musical quality nor a performer's capability. |
| RHY.7, RHY.8 and RHY.11 | Use their structural comparison, transformation and shared-performance methods when the work needs those broader results. | Their general operations do not by themselves select this specialized seed and action construction. |

The receiving constraints, alternatives and revised arrangements are this framework's synthesis of those constructions. The historical and cultural examples in the source are not used as evidence that this particular arrangement will succeed. Reconsider the choice when an available method, instrument or observation changes the attainable musical result or its cost.

### MDPE.30:12 - Relations

- MDPE.9 uses the generated parts in comparing creative alternatives.
- MDPE.3 obtains the performed combination with the accompaniment and other means.
- MDPE.10 develops a missing capability when the intended rule is structurally adequate.
- MDPE.11 determines prepared and live choices within the performance.
- RHY.7, RHY.8 and RHY.11 provide the broader comparisons, transformations and coordination named above.
- Application 5.3 connects the recoverable structure of a method, its description and acquisition when this construction is taught.

### MDPE.30:End
