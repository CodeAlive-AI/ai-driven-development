## E.17.AUD.OOTD - PublicationUnit Stability Discipline and PublicationUnit Primary-Subject Discipline - publication-unit stability over one primary subject

**Placement.** Narrow publication-unit stability pattern inside the broader `PublicationUnit Stability Discipline`.

**Builds on.** `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.2.8.PER`, `A.2.9`, `A.15`, `A.15.4`, `B.3`, `C.11`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit explicit about its primary subject.

**One-line summary.** `PublicationUnit Primary-Subject Discipline` applies to one bounded publication unit at a time and keeps that unit explicit about what it is mainly about, what claim or communicative move it carries, and what wider work, downstream use, decision, or reliance claim remains outside.

**Primary subject.** In this pattern, `publicationUnitPrimarySubject` means what this bounded publication unit is mainly about for the current reading. It may be a named entity, boundary, episode, question, proposal, pattern section, or another plainly named subject. This is a publication aid, not a new `U.` kind or a `C.2.1` participant by default.

**Exact C.2.1 projection.** Only when the unit carries one identified claim-bearing episteme `E`, and its primary subject is the exact entity that the claims of `E` concern, may the author state `publicationUnitPrimarySubject = EntityOfConcern(E)`. Otherwise do not infer an `EntityOfConcernRef`, do not treat a topic or interpretation as an entity, and do not use a primary-subject transition as evidence that the exact `C.2.1` participant changed.

**Publication unit.** Here this means one bounded note, memo, sheet, review aid, screen, table, or short section that people are expected to read as one unit.

**Use this when.** Use this pattern when one note, memo, sheet, screen, table, comparison aid, or other publication unit sounds continuous while it quietly shifts what it is mainly about, which question it foregrounds, what it claims or asks the reader to do, or which wider process it appears to license. Use it when local word repair is no longer enough and the unit needs one stable answer to: what is this unit about, what move is it making, how may it be used, and what still remains outside?

**What goes wrong if you miss this.** One publication unit starts with one subject and quietly ends with another concern, claim, communicative move, or downstream use. Review then gets trapped in sentence-level wording arguments while the real defect is publication-unit interpretation instability, and readers over-attribute decision weight or scope to a unit that never declared it.

**What this buys you in practice.** It lets a team stop publication-unit interpretation instability before one memo, note, or review unit quietly starts carrying rollout, approval, wider architecture strategy, or another wider concern by habit. In practice that means reviewers can name the real stabilization job earlier, keep downstream work outside, and decide faster whether the current unit is stable enough to keep using at all.

**Not this pattern when.** This is not the right pattern when:
- the problem is still local lexical-head kind or qualifier repair and `E.17.AUD.LHR` (`Local Head Restoration`) is enough;
- the same publication unit is already stable enough, and the question under repair is one bounded comparative review move over already available source epistemes or publications under `E.17.ID.CR`;
- the question under repair is still same-entity rewrite, representation shift, explanation-face work, bridge-explication, or another neighboring pattern whose move is already primary;
- the question under repair is view, face, carrier, or publication architecture rather than publication-unit interpretation instability;
- the unit is already being used to approve, assign, adjudicate, or direct work and should use the more honest downstream decision, work, or reliance publication.

**Quick recovery.** If this situation fits, write the ordinary natural-language declaration in `E.17.AUD.OOTD:4.3` and compare it with the nearest worked slice in `E.17.AUD.OOTD:5.1` through `E.17.AUD.OOTD:5.6`. Use the six diagnostic prompts only if the declaration is hard to make honest. If one clear sentence or two short sentences settle the case, stop there rather than creating a card or climbing into heavier assurance by habit.

**Quick boundary bank.** If this situation no longer fits, stop at the right boundary instead of opening the heavier stack by habit. One overloaded local lexical head or qualifier only -> `E.17.AUD.LHR` (`Local Head Restoration`). Same stable publication unit, but the question under repair is one bounded comparison over already pinned source epistemes or publications -> `E.17.ID.CR`. View, face, carrier, same-entity rewrite, or downstream approval, work, or reliance question -> the neighboring pattern or the more honest downstream decision publication.

**What this pattern does.** `PublicationUnit Stability Discipline` names the broader family. `PublicationUnit Primary-Subject Discipline` is the local writing-and-review pattern for making one unit's primary subject, carried move, downstream-use boundary, and outside-work boundary clear together. The moving lineage remains successive `U.Episteme` publications over `U.CharacteristicSpace`; this pattern only keeps one publication unit clear about that lineage or one move over it.

**Reader.** This pattern is written first for an engineer-manager, architect, reviewer, or programme lead who needs to stop one publication unit from quietly changing what it is about. Others may polish or review the text itself, but the opening should still read as ordinary review and writing guidance.

### E.17.AUD.OOTD:1 - Problem frame

**Use the examples as alternatives.** The quick checks, ordinary declaration, optional diagnostic, heavier extension, and worked slices are alternative aids for one publication unit, not a required sequence. One case may stop after the declaration; another may reopen when outside observations change the honest concern, claim, or downstream use; another may use the neighboring pattern whose instructions fit once approval, work, reliance, or another question becomes primary.

Teams repeatedly write one publication unit that begins with one primary subject and ends with another subject, concern, carried move, or downstream use while still sounding like one unchanged text.

Typical moments include:
- an architecture note that starts about a system boundary and ends by directing rollout work;
- an operations review note that starts about an incident episode and ends as an action approval;
- a requirements or policy note that starts about an exact entity and ends about its carrier or document status;
- an episteme-publication-heavy note that starts about one pattern section or publication form and ends about wider architecture strategy;
- a comparison sheet that starts about one subject and quietly shifts into engineering-process, approval, work, or reliance pressure.

That interpretation instability is usually not caused by one bad sentence alone.
It is caused by one whole publication unit no longer holding a stable answer to what it is about, which concern it foregrounds, what move it carries, how readers may use it, and what wider work still stays outside.

### E.17.AUD.OOTD:2 - Problem

Without a named publication-unit discipline:
1. authors repair one vague phrase at a time but still leave the unit unstable as a whole;
2. reviewers argue about wording while missing that the unit has already shifted subject, concern, claim, communicative move, or downstream use;
3. teams quietly read one note as if it licensed a downstream use the unit never declared;
4. local lexical discipline (`A.6.P`, `E.10`, `F.18`) gets blamed for publication-unit interpretation instability it was never meant to solve alone;
5. unit-form confusion is mistaken for view, face, carrier, or publication architecture even when the immediate problem is simpler and closer.

### E.17.AUD.OOTD:3 - Forces

| Force | Tension |
| --- | --- |
| **Local repair vs publication-unit stability** | The pattern must not replace local precision repair, but it must become available when local repair no longer stabilizes the unit. |
| **Primary-subject clarity vs surrounding-work convenience** | The unit must keep one primary subject without forcing the whole surrounding work process into the same text. |
| **Interpretation clarity vs overgrowth** | The section must distinguish primary subject, exact `EntityOfConcern` when applicable, concern, carried move, downstream use, publication form, carrier, and process without turning into a giant ontology lecture. |
| **Plain entry vs later assurance** | The opening must stay light enough for ordinary use while preserving the distinctions needed if a concrete neighboring claim or assurance question later arises. |
| **Publication-unit stability vs architecture replacement** | The pattern must not replace view, face, carrier, publication, or moving-lineage architecture. |

### E.17.AUD.OOTD:4 - Solution - stabilize one publication unit, one primary subject, one move, and one outside-work boundary

#### E.17.AUD.OOTD:4.1 - Manager-first entry

> `PublicationUnit Primary-Subject Discipline` keeps one publication unit explicit about what it is mainly about, what claim or communicative move it carries, and what wider work remains outside.
>
> It becomes necessary when local repair is no longer enough and the publication unit still shifts among subject, concern, description, carrier, process, or downstream use while sounding unchanged.

In plain working terms, this section is for moments like:
- `this memo is about the architecture boundary, not yet about the rollout plan`;
- `this review note is about the incident episode and the observed contrast, not yet a production-action recommendation`;
- `this comparison sheet is about the options under review, not yet about approval or the downstream decision`;
- `this semio note is about one pattern section or publication form, not the wider architecture policy around it`.

If that is the clarification you need, start here.
If the real problem is still only one vague local lexical head word, start with `E.17.AUD.LHR` (`Local Head Restoration`).

#### E.17.AUD.OOTD:4.1.a - Plain working terms

- **Publication unit** = one written or displayed bounded unit others are meant to read as one unit, such as a note, memo, sheet, table, or guided screen.
- **Primary subject** = what that bounded unit is mainly about for the current reading. It is an ordinary local publication term, not a new ontological kind.
- **Concern** = the question, aspect, or issue foregrounded about that subject. The concern can change while the subject remains the same.
- **Exact `EntityOfConcern`** = the one exact `U.Entity` participating in the `C.2.1` constitution of one identified claim-bearing episteme. It is not a synonym for topic, kind, interpretation, question, or subject.
- **Carried move** = what the unit asserts, compares, explains, recommends, or otherwise communicates about its subject; it may also say that it only stabilizes the reading without adding a new claim.
- **Downstream use** = what a reader is invited or permitted to do with the unit, such as understand, compare, approve, rely, assign, or act.
- **Outside-work boundary** = what wider review, execution work, non-admissible downstream decision, or reliance claim stays outside the current unit.
- **Explicit transition** = the unit openly names which of subject, concern, carried move, or downstream use has changed instead of pretending the unit is unchanged.

#### E.17.AUD.OOTD:4.1.b - What can change

Treat the publication unit under review here as one bounded readable unit with one primary subject for the current reading. That local subject declaration does not make the unit itself the source episteme, `C.2.1` `EntityOfConcern`, publication form, carrier, or E.24.PUB publication occurrence.

Keep five change types distinct:
1. a **subject change** changes what the unit is mainly about;
2. a **concern change** foregrounds another question or aspect while the subject may remain fixed;
3. a **claim or carried-move change** changes what the unit asserts, compares, explains, or recommends;
4. a **downstream-use change** changes what the reader is invited or allowed to do; and
5. an **`EntityOfConcern` change** occurs only when the exact claim-bearing episteme being carried has changed in the entity participant that its claims concern under `C.2.1`.

Use the optional prompts in 4.3 only when these distinctions are hard to recover from the unit itself.

Only after one exact carried episteme `E` is identified may the author add the conditional projection `publicationUnitPrimarySubject = EntityOfConcern(E)`, and only when both sides name the same exact entity. If the lens cannot stay stable after local repair, do not patch over the shift with a heavier declaration; reopen the unit or use the neighboring pattern that addresses the actual remaining question.

#### E.17.AUD.OOTD:4.2 - Scope and exclusions

**In scope**
- one publication unit with an unstable primary subject;
- one unit mixing concern, carried move, downstream use, and outside work;
- one unit quietly shifting between subject, description, carrier, publication unit, process, or downstream decision use;
- episteme-publication-heavy texts where repair disposition, the applicable boundary rule, primary subject, carried move, and outside work must stay explicit across one publication unit;
- a conditional `C.2.1` projection when one exact carried episteme and its exact entity participant are already identified.

**Out of scope**
- local lexical-head repair only;
- pure view, face, or carrier architecture work;
- entityOfConcernRef-preserving transform, explanation, bridge, ontology, or comparative-review questions for which a neighboring pattern already supplies the needed method or test;
- downstream gate, approval, execution, or decision pressure;
- invention of a publication-wide `EntityOfConcern` when no exact claim-bearing episteme supplies one.

**Ordinary stop rule.** If one natural-language declaration plus the nearest worked slice settle the case, stop there. A transition is required only when one occurred, and a neighboring-pattern reference only when a concrete unresolved question remains. Do not climb into heavier assurance just to prove that one unit now keeps one primary subject, one carried move, and one outside-work boundary honestly in place. Ordinary use requires no diagnostic card, `ClaimGraph`, evidence dossier, assurance result, work record, or `C.2.1` projection unless a separate receiving use independently needs one.

#### E.17.AUD.OOTD:4.2.a - Choose the least-cost honest unit architecture

“One primary subject” is a local default for a short unit meant to carry one readily recognizable move. It is not an ontological law and does not forbid a deliberately structured document that readers need as one unit.

Compare four repairs before splitting by reflex:

| Repair | Retain it when | Reject it when |
| --- | --- | --- |
| **Retain one unit with one declared primary subject** | one reader goal, one bounded downstream use, and one honest umbrella subject organize all included material; subordinate paragraphs do not introduce an independent move | the umbrella is merely a vague label hiding unrelated subjects or uses |
| **Declare an explicit transition inside one short unit** | the same reader and bounded use need a small ordered shift, and naming the from/to subject, concern, or move costs less than a split | later readers are likely to extract either part independently, or the second part licenses a different use |
| **Retain one explicitly sectioned multi-subject unit** | the sections have clear local headings and moves, their dependency or shared decision question makes joint reading useful, and one scope/non-scope declaration prevents overread | section boundaries still leave audience, claim, or permitted-use changes hidden |
| **Split into separate units** | subjects serve different readers or actions, need independent reuse or approval, or one part falls outside the declared scope of the other | the split creates navigation, duplication, synchronization, or decision-assembly cost without reducing ambiguity |

Choose the least-cost option that preserves comprehension, exact claim meaning, intended use, and protection against overread. Do not optimize the count of subjects, sections, or documents. If a multi-subject container has no truthful umbrella subject and no joint reader use, treat it as a collection of units or split it; do not invent a broad subject merely to satisfy this pattern.

#### E.17.AUD.OOTD:4.3 - Ordinary declaration and optional diagnostic

The complete ordinary result is one natural-language declaration from which a reader can recover:
- the bounded publication unit;
- its primary subject;
- the claim or communicative move it carries; and
- the wider work or use that remains outside.

One sentence or two short sentences are enough. For example:

> This review note compares the interface-boundary options under the current incident evidence. Rollout responsibility and approval remain outside this note.

Do not require a separate card, record, identifier, table, or field set when that declaration is already clear. Add an explicit transition only when the unit actually changes subject, concern, carried move, or downstream use. Name a neighboring pattern only when one concrete unresolved question remains and that pattern supplies the needed instruction; an empty transition row or speculative neighbor lookup adds no value.

When the sentence is hard to write or a reviewer suspects a hidden shift, use these six prompts privately as an optional diagnostic:

| Prompt | Diagnostic question |
| --- | --- |
| 1 | What single publication unit am I asking people to read as one bounded unit? |
| 2 | What is its primary subject: what is it mainly about? |
| 3 | Which concern is foregrounded, and what claim or communicative move does the unit carry? |
| 4 | What downstream use is permitted or blocked, and what wider work is outside this unit? |
| 5 | Has subject, concern, carried move, downstream use, or the exact `C.2.1` entity participant changed, and is that exact change named? |
| 6 | If this remains unstable after local repair, what exact question remains, and which neighboring pattern supplies the needed repair or boundary? |

These prompts guide attention; they are not six publication rows. Discard the diagnostic once it has yielded the clear ordinary declaration.

If local repair is still enough, go back to `E.17.AUD.LHR` (`Local Head Restoration`) instead of adding more structure here.
If the unit remains one publication unit but neighboring-boundary claim-kind, misuse risk, or cross-interpretation ambiguity becomes claim-bearing, use the heavier extension as the assurance section.
If the same unit is already stable as one primary subject, one carried move, and one outside-work boundary, and the remaining question is one bounded comparative review move over already available source epistemes or publications, apply `E.17.ID.CR` rather than thickening the declaration.
If the unit cannot stay stable even after local repair, reopen the unit or apply the neighboring pattern that answers the exact remaining question; do not stack more fields onto the declaration.

#### E.17.AUD.OOTD:4.4 - Claim-bearing extension and quick boundary summary

Use the heavier extension only after the ordinary declaration is stable and a concrete neighboring claim or downstream use needs more detail.
It is for heavier declaration, not for rescuing a unit that still cannot keep one primary subject, one carried move, and one outside-work boundary in place.

Then add only the fields needed by the current claim or downstream use:
- `publicationUnitFormCue`;
- `primaryInterpretation`;
- `transitionPolicy`;
- `modelingLensPolicy`;
- `downstreamDecisionPolicy`;
- `entityOfConcernProjection`, only for the exact `C.2.1` case stated in 4.1.b.

These fields do not create a rival rule track. `publicationUnitFormCue` names words such as note, sheet, screen, and table as form clues only; it does not make those clues subjects, entity kinds, or claim kinds. `entityOfConcernProjection` records an already justified equality with the exact entity participant of one identified episteme; it neither creates that participant nor turns a topic into an entity. The remaining fields clarify the relevant boundary only when the ordinary declaration is not enough for a named later use.

**Quick boundary to neighboring patterns and project records**
- use `E.17.AUD.LHR` (`Local Head Restoration`) when the instability is still local to one lexical head, qualifier, or interpretation word;
- use `E.17.ID.CR` when the same publication unit already holds one stable primary subject, one carried move, and one outside-work boundary, and the question under repair is one bounded comparative review move over already available source epistemes or publications;
- use this pattern when one publication unit still has unstable subject, concern, carried-move, downstream-use, or outside-work interpretation after honest local repair;
- use the neighboring pattern that addresses the view, face, carrier, entityOfConcernRef-preserving transform, explanation, bridge, ontology, gate, approval, or execution question; keep any required project record with that question.

#### E.17.AUD.OOTD:4.5 - Boundary-rule summary

Use this summary to decide whether to stay with this pattern or move to a neighboring one.

The practical summary is:
1. keep one declared primary subject unless a transition is explicit;
2. do not collapse primary subject, concern, exact `EntityOfConcern`, description, carrier, publication unit, carried move, process, and downstream use into one unchanged interpretation;
3. keep the carried move and permitted downstream use distinct from the wider work around them;
4. use local `E.17.AUD.LHR` (`Local Head Restoration`) first, and open this pattern when publication-unit interpretation instability remains after that;
5. apply `E.17.ID.CR` when publication-unit stability already holds and the remaining question is one bounded comparative review move over already available source epistemes or publications;
6. move out when the unit starts carrying downstream decision pressure or another neighboring-pattern question.

### E.17.AUD.OOTD:5 - Archetypal grounding

**Worked-slice status.** Read the architecture, operations, episteme-publication-heavy, comparison-return-to, and changed-concern cases as a heterogeneous example bank, not as one recommended progression.

#### E.17.AUD.OOTD:5.1 - Architecture note shifting into rollout work

A short architecture memo begins with:
`This note is about the proposed service boundary between catalog and checkout.`

Three paragraphs later it says:
`We should therefore assign rollout responsibility to platform and stage migration in two sprints.`

The fix is not only lexical.
The memo's primary subject began as the service boundary, but its carried move changed from describing or assessing that boundary to assigning responsibility and directing rollout; its apparent downstream use changed from understanding to planning and decision. None of those changes by itself proves that the `C.2.1` `EntityOfConcern` of an exact carried episteme changed.
Repair the memo in one of two ways:
- keep the note about the boundary and push rollout outside;
- or make the changed move and downstream use explicit and use a downstream decision or rollout publication.

**Repaired two-sentence memo.** `This memo assesses the proposed service boundary between catalog and checkout. Rollout sequencing, responsibility assignment, and approval remain outside this memo.`

**Action saved.** The author publishes those two sentences and stops: no six-row artifact, empty transition declaration, neighboring-pattern reference, assurance record, or evidence package is produced. A rollout record opens only if rollout later becomes current work.

#### E.17.AUD.OOTD:5.2 - Operations note shifting into approval

An incident note begins as a comparative review of timing variance and operator context.
It ends as if it already recommends a production action.

The incident episode may remain the primary subject while the foregrounded concern changes and the carried move shifts from comparison to recommendation. Keep the review unit about the episode and the contrast it is surfacing; put action approval in an explicit outside-work or downstream decision text.

Use `C.11` if the new text chooses among already available actions. If an actual approving communication and an instituted permission matter, keep the `A.2.9` communicative Work and the `A.2.8.PER` grant relation separate. Use `A.21` only when a current `OperationalGate(profile)` actually publishes a gate decision.

#### E.17.AUD.OOTD:5.3 - Semio-heavy text mixing one local section and wider architecture strategy

A semio note starts about one selected pattern section and ends as if it had decided the packaging strategy for the whole overlay.

Here the primary subject broadens from the selected section to the whole overlay, and the carried move broadens from local interpretation to strategy. The unit should state:
- what the note is about now;
- what concern and move it carries over that subject;
- and what wider architecture strategy remains outside the current unit.

#### E.17.AUD.OOTD:5.4 - Unit stabilizes and bounded comparison becomes primary

A review note first shifts between the selected interface boundary, the move it is making over the current evidence, and the rollout implications around that boundary.
After one honest publication-unit repair it now says:
`This review unit is about the interface-boundary options and the contrast they make visible under the current incident evidence; rollout responsibility and approval remain outside this note.`

At that point the same unit already holds one stable primary subject, one carried comparison move, and one outside-work boundary.
`PublicationUnit Primary-Subject Discipline` has done its job.
If the remaining question is now one bounded comparison between the already pinned options over the same evidence, the honest next pattern application is `E.17.ID.CR` rather than keep thickening publication-unit discipline.

#### E.17.AUD.OOTD:5.5 - Outside observation changes the live concern or carried claim

A release-readiness note is already explicit that it is about one candidate publication or view and the risk state visible from the current evidence.
Mid-review, an external vendor bulletin and a new field observation change the live failure boundary for that same candidate.

The candidate may remain the primary subject. What changed first is the evidence-facing concern and the claim the note can honestly carry; a later approval or execution question may also change the downstream use. Do not report an `EntityOfConcern` change unless one identified claim-bearing episteme actually has a different exact entity participant under `C.2.1`.
Repair the note in one of three ways:
- stop the current unit at the originally declared evidence boundary and open a new downstream record for the changed question;
- explicitly reopen the same unit with the revised concern, claim or carried move, permitted use, and outside-work boundary;
- or use the downstream decision or work pattern whose instructions now fit once approval, execution, or another downstream decision publication becomes the more honest primary question.

The bulletin and field observation remain sources until a support, evidence, or currentness claim makes `A.10` relevant. Use `C.11` for a later choice, `A.2.9` and `A.2.8.PER` for an approving act and its permission effect, `A.15` for a work claim, and `A.21` only for an actual gate decision.

#### E.17.AUD.OOTD:5.6 - Deliberately sectioned multi-subject review packet

A release-readiness group needs one packet for one meeting. The packet contains three clearly headed sections:

1. **Interface-boundary options** — compares two architecture alternatives.
2. **Incident evidence** — summarizes the observations that discriminate between those alternatives.
3. **Rollout constraints** — states constraints the later approval decision must respect, without assigning work or granting approval.

The local one-subject heuristic does not force three documents. The packet has one honest umbrella subject—`the evidence and constraints needed to review the interface-boundary choice`—and one bounded use: inform the review, not approve rollout. Keeping the three section-level subjects together avoids navigation and synchronization cost, while the headings prevent their different moves from masquerading as one claim.

An unsectioned version is rejected because readers cannot see the subject and move changes. A short narrative with only one small shift may instead declare that transition. Separate documents become the least-cost choice when the rollout section starts assigning responsibility, serves another audience, needs independent reuse, or becomes an approval input with its own reliance boundary.

### E.17.AUD.OOTD:6 - Bias-Annotation
Lenses tested: **Arch**, **Onto and Epist**, **Prag**, **Did**.
This section intentionally biases toward explicit publication-unit stability and against quietly letting one unit absorb wider work or decision pressure by habit.
The main mitigation is explicit primary-subject, concern, carried-move, downstream-use, and outside-work surfacing; conditional use of exact `EntityOfConcern` only when `C.2.1` warrants it; early return to `E.17.ID.CR` when publication-unit stability is already solved; and an explicit boundary choice once a downstream claim becomes primary.

### E.17.AUD.OOTD:7 - Conformance Checklist

**Checklist scope.** Use this checklist when checking a claimed application of this pattern, not as nine required authoring steps. The one- or two-sentence ordinary declaration remains a complete result; inspect only the rows implicated by the actual unit, transition, `EntityOfConcern` projection, neighboring claim, or unit-architecture choice, and do not publish a nine-row record by default.

1. **CC-OOTD-1 - One publication unit is explicit.**
   The publication unit under review is explicitly identifiable as one note, memo, sheet, screen, table, or section meant to be read as one unit.
2. **CC-OOTD-2 - Primary subject is explicit.**
   The unit states what it is mainly about in ordinary language rather than asking readers to infer it from tone.
3. **CC-OOTD-3 - Any `EntityOfConcern` projection is exact and conditional.**
   The unit uses `EntityOfConcern` only for the exact entity participant of one identified claim-bearing episteme under `C.2.1`; a topic, kind, question, or interpretation is never substituted for that participant.
4. **CC-OOTD-4 - Concern, carried move, downstream use, and outside work are distinct.**
   The unit states which question it foregrounds, what it asserts or communicates, how readers may use it, and which wider work, approval, execution, decision, or reliance remains outside.
5. **CC-OOTD-5 - Any transition is typed and explicit.**
   If subject, concern, claim or carried move, downstream use, or the exact entity participant changes, the unit names which change occurred rather than quietly absorbing all of them into one interpretation.
6. **CC-OOTD-6 - Local vs publication-unit repair choice is honest.**
   Apply `E.17.AUD.LHR` (`Local Head Restoration`) first when local repair is enough; apply this pattern only when publication-unit interpretation instability remains after local repair.
7. **CC-OOTD-7 - Neighboring-pattern boundary is explicit.**
   If an entityOfConcernRef-preserving transform, explanation, bridge, comparative-review, ontology, gate, approval, or execution claim becomes primary, use the neighboring pattern that defines or constrains that claim rather than pretending this pattern still carries the case.
8. **CC-OOTD-8 - Claim-bearing lens is stated when needed.**
   If a minimal modeling lens, exact `C.2.1` projection, or downstream-decision policy is materially claim-bearing, it is stated rather than silently assumed.
9. **CC-OOTD-9 - Unit architecture is the least-cost honest choice.**
   Retaining one unit, declaring a transition, keeping a sectioned multi-subject unit, or splitting is chosen from the current reader, use, reuse, dependency, and overread costs. The author does not split to satisfy a count and does not retain a vague umbrella to avoid a necessary split.

### E.17.AUD.OOTD:8 - Common Anti-Patterns

- **Local-repair inflation.** Opening publication-unit discipline when one overloaded local lexical head or qualifier is still the real defect.
- **`EntityOfConcern` inflation.** Calling every topic, kind, interpretation, question, or writing transition an `EntityOfConcern` or `EntityOfConcern` change.
- **Work-process smuggling.** Letting a note begin as architecture, incident review, or comparison work and end as rollout, approval, or execution guidance without naming the transition.
- **Admissibility-pattern replacement.** Treating this pattern as if it replaced view, face, or carrier architecture, entityOfConcernRef-preserving transform rules, explanation-face rules, bridge rules, or downstream decision texts.
- **Overgrowth by declaration.** Stacking heavier fields onto a unit that still cannot keep one stable primary subject, one move, and one outside-work boundary in place.

### E.17.AUD.OOTD:9 - Consequences

Used well, this section buys three main gains:
- authors stop smuggling wider work into one unit by accident;
- reviewers can name whether subject, concern, carried move, or downstream use changed instead of only arguing about wording;
- neighboring patterns and downstream decision texts stop getting blamed for confusion created one layer earlier.

The cost is that some notes must become shorter, split earlier, or reopen more honestly when their subject, concern, carried move, or downstream use really changes.
That cost is deliberate.

### E.17.AUD.OOTD:10 - Rationale

The point of this pattern is not to create a second architecture of views, faces, carriers, epistemes, or downstream decision texts.
It is narrower: one publication unit can become misleading even when every single sentence looks locally acceptable.

`A.6.P`, `A.7`, `E.10`, and `F.18` already keep kinds, distinctions, and naming precise. `C.2.1` already identifies the exact entity participant of one claim-bearing episteme. This pattern adds only the missing publication-unit discipline: choose the least-cost honest architecture for a bounded readable unit, make its primary subject or section-level subjects and moves visible, and keep downstream use and outside work explicit. It borrows `EntityOfConcern` only through the exact conditional projection in 4.1.b and does not extend that ontology.

The pattern also stays intentionally close to `E.14` and `E.19`.
Recognition comes first through a manager-usable entry block and one ordinary natural-language declaration; the six prompts remain an optional diagnostic.
Heavier declaration comes only after the ordinary declaration already holds and a named receiving use consumes the added fields.

### E.17.AUD.OOTD:11 - SoTA-Echoing

**Source boundary.** These sources support topic focus, scope/non-scope, reader-need organization, and explicit document structure. None establishes a universal ontological rule that every publication unit has one subject, and none supplies a `C.2.1` entity participant. OOTD therefore keeps the one-primary-subject rule as a defeasible local heuristic and compares it with transition, sectioning, and splitting.

| Publication-unit obligation | Exact source and current contribution | Local repair of the source limit | Working implication here |
| --- | --- | --- | --- |
| Keep the current unit focused and expose its scope and non-scope. | [Google Technical Writing One — Documents](https://developers.google.com/tech-writing/one/documents) (updated 2025-07-07) tells authors to state scope and non-scope, then refocus or revise the scope when content veers; [Paragraphs](https://developers.google.com/tech-writing/one/paragraphs) (updated 2025-03-28) treats a paragraph as one independent unit of logic focused on one topic. | Paragraph focus does not imply one subject for every memo, packet, or document. OOTD scales the move by naming the bounded unit and comparing retention, explicit transition, sectioning, and splitting. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:4.3`, `E.17.AUD.OOTD:5.1`, `E.17.AUD.OOTD:5.6` |
| Organize documentation around the user's need and keep different action/cognition modes visible. | [Diátaxis](https://diataxis.fr/) organizes content, architecture, and form around four distinct user needs; its [compass](https://diataxis.fr/compass/) tests whether material informs action or cognition and supports acquisition or application, at sentence or whole-document scale. | The four modes diagnose a use shift but are not an FPF ontology or a formula for document count. OOTD names the actual carried move and downstream use, then keeps one structured unit only when a shared reader goal makes that cheaper and still clear. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.2`, `E.17.AUD.OOTD:5.6` |
| Use a single-subject reusable topic when modular reuse is the main need. | [OASIS DITA 1.3 `<topic>`](https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/langRef/base/topic.html) defines the top-level topic as a single-subject topic or article. This is established structured-authoring lineage (2015), not the current source of OOTD's whole-document rule. | A DITA topic is one valid reusable unit architecture, not evidence that a deliberately sectioned review packet is defective. OOTD selects it when independent reuse or retrieval dominates and otherwise permits the coherent multi-section unit. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.6` |
| Keep object words and local designations precise without importing another concept system. | ISO 704:2022 and ISO 1087:2019 terminology practice distinguishes objects, concepts, definitions, designations, and terms. | Terminology discipline repairs overloaded heads but does not choose the publication architecture. OOTD first uses `E.17.AUD.LHR`, then makes subject, concern, carried move, and use explicit only when unit-level instability remains. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2`, `E.17.AUD.OOTD:5.3` |

### E.17.AUD.OOTD:12 - Relations

**Builds on**
- `A.6.P`
- `A.7`
- `E.10`
- `F.18`
- `E.14`
- `E.19`
- `C.2.2a`
- `A.16.0`

**Nearest neighbors**
- `E.17.AUD.LHR` for local lexical-head kind or qualifier repair;
- `E.17.ID.CR` when the same unit is already stable and the remaining question is one bounded comparative review move;
- `E.17.EFP` when explanation-face use or faithfulness on existing faces is primary;
- `A.6.3`, `A.6.3.CR`, and `A.6.3.RT` when the question under repair is same-entity rewrite or representation change;
- `A.10` when evidence or provenance becomes primary;
- `A.15` and `A.15.4` when work, reliance, or execution claim becomes primary;
- `B.3` when assurance or engineering justification becomes primary;
- `C.11` when choosing among already available options becomes primary;
- `A.2.9` when an actual approval is communicative Work, and `A.2.8.PER` when the question is the permission or grant relation it institutes, its exercise, or its conflict;
- `A.20` only when step-local `FlowConstraintValidity` becomes primary, and `A.21` only when a current `OperationalGate(profile)` publishes the gate decision.

### E.17.AUD.OOTD:End

