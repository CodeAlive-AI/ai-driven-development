## E.17.AUD.OOTD - Clarify the Primary Subject of a Publication Unit (PublicationUnit Primary-Subject Discipline)

> **Status:** Stable

**Placement.** A pattern in the `PublicationUnit Stability Discipline` for stabilizing one publication unit.

**Builds on.** `A.6.P`, `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `C.2.2a`, `A.16.0`.

**Coordinates with.** `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, `A.6.3`, `A.6.3.CR`, `A.6.3.RT`, `A.10`, `A.2.8.PER`, `A.2.9`, `A.15`, `A.15.4`, `B.3`, `C.11`, `A.20`, `A.21`.

**Plain-name.** Keep one publication unit explicit about its primary subject.

**One-line summary.** For one bounded publication unit at a time, `PublicationUnit Primary-Subject Discipline` makes clear what the unit is mainly about, what claim or communicative move it carries, and which wider work, downstream use, decision, or reliance claim remains outside.

**Primary subject.** In this pattern, `publicationUnitPrimarySubject` means what this bounded publication unit is mainly about for the current reading. It may be a named entity, boundary, episode, question, proposal, pattern section, or another plainly named subject. This is a publication aid, not a new `U.` kind or a `C.2.1` participant by default.

**Exact C.2.1 projection.** Only when the unit carries one identified claim-bearing episteme `E`, and its primary subject is the entity that the claims of `E` concern, may the author state `publicationUnitPrimarySubject = EntityOfConcern(E)`. Otherwise do not infer an `EntityOfConcernRef` from a topic label or interpretation alone, or use a primary-subject transition as evidence that the `C.2.1` participant changed.

**Publication unit.** A bounded note, memo, sheet, review aid, screen, table or short section intended for a person or an agent to interpret as one unit. A machine-only operating note qualifies when its recipient needs to interpret the whole note.

**Use this when.** A note, memo, sheet, screen, table, comparison aid, or other publication unit can sound continuous even as it shifts what it is mainly about, which question it foregrounds, what it claims or asks the reader to do, or which wider process it appears to license. Use this pattern when local word repair is no longer enough and the unit needs stable answers about its subject, the move it makes, its permitted use, and the work that remains outside.

**What goes wrong.** A publication unit changes its subject, concern, claim, communicative move, or downstream use without marking the change. Reviewers argue over sentences while the reading of the unit as a whole shifts. Readers then give it decision weight or scope it never claimed.

**Practical gain.** A team can prevent an unmarked change of reading before a memo, note, or review unit comes to stand for rollout, approval, wider architecture strategy, or another concern beyond the unit without saying so. Reviewers can identify what needs to be stabilized sooner, keep downstream work outside the unit, and decide more quickly whether its interpretation is stable enough for continued use.

**When to use another approach.** Use another approach when:
- the problem is still local lexical-head kind or qualifier repair and `E.17.AUD.LHR` (`Local Head Restoration`) is enough;
- the same publication unit is already stable enough, and the question under repair is one bounded comparative review move over already available source epistemes or publications under `E.17.ID.CR`;
- the question under repair is still same-entity rewrite, representation shift, explanation-face work, bridge-explication, or another neighboring pattern whose move is already primary;
- the question under repair is view, face, carrier, or publication architecture rather than publication-unit interpretation instability;
- the unit is already being used to approve, assign, adjudicate, or direct work and should use the downstream decision, work, or reliance publication appropriate to that use.

**Quick recovery.** If this situation fits, write the ordinary natural-language declaration in `E.17.AUD.OOTD:4.3` and compare it with the nearest worked slice in `E.17.AUD.OOTD:5.1` through `E.17.AUD.OOTD:5.6`. Use the six diagnostic prompts only if it is hard to state the declaration accurately. For a request to clarify scope, one or two sentences can finish the work. If the unit owes its reader an assessment, include the criterion, relevant facts and resulting judgment.

**What this pattern does.** `PublicationUnit Stability Discipline` names the broader family. `PublicationUnit Primary-Subject Discipline` is the local writing-and-review pattern for making one unit's primary subject, carried move, downstream-use boundary, and outside-work boundary clear together.

**Reader.** The primary reader is an engineer-manager, architect, reviewer, or programme lead who needs to stop one publication unit from changing its subject without saying so.

### E.17.AUD.OOTD:1 - Problem frame

**Use the examples as alternatives.** The quick checks, ordinary declaration, optional diagnostic, heavier extension, and worked slices are alternative aids for one publication unit, not a required sequence. One case may stop after the declaration; another may reopen when outside observations change the concern, claim, or downstream use the unit can support; another may use the applicable neighboring pattern once approval, work, reliance, or another question becomes primary.

Teams repeatedly write one publication unit that begins with one primary subject and ends with another subject, concern, carried move, or downstream use while still sounding like one unchanged text.

Typical moments include:
- an architecture note that starts about a system boundary and ends by directing rollout work;
- an operations review note that starts about an incident episode and ends as an action approval;
- a requirements or policy note that starts about an identified entity and ends about its carrier or document status;
- an episteme-publication-heavy note that starts about one pattern section or publication form and ends about wider architecture strategy;
- a comparison sheet that starts about one subject and shifts without warning into engineering-process, approval, work, or reliance pressure.

That interpretation instability is usually not caused by one bad sentence alone.
It arises because the unit as a whole no longer gives a stable answer to what it is about, which concern it foregrounds, what move it carries, how readers may use it, and what wider work remains outside.

### E.17.AUD.OOTD:2 - Problem

Without a named publication-unit discipline:
1. authors repair one vague phrase at a time but still leave the unit unstable as a whole;
2. reviewers argue about wording while missing that the unit has already shifted subject, concern, claim, communicative move, or downstream use;
3. teams quietly read one note as if it licensed a downstream use the unit never declared;
4. local lexical discipline (`A.6.P`, `E.10`, `F.18`) gets blamed for publication-unit interpretation instability it was never meant to solve alone;
5. unit-form confusion is mistaken for view, face, carrier, or publication architecture even when the immediate problem is how to read the unit.

### E.17.AUD.OOTD:3 - Forces

| Force | Tension |
| --- | --- |
| **Local repair vs publication-unit stability** | The pattern must not replace local precision repair, but it must become available when local repair no longer stabilizes the unit. |
| **Primary-subject clarity vs surrounding-work convenience** | One subject and one move can suffice for a short unit. When a joint decision needs connected subjects or moves, make their roles visible together and mark the boundary with surrounding work. |
| **Interpretation clarity vs overgrowth** | The section must distinguish primary subject, `EntityOfConcern` when applicable, concern, carried move, downstream use, publication form, carrier, and process without requiring a long explanation of the ontology. |
| **Plain entry vs later assurance** | The opening must stay light enough for ordinary use while preserving the distinctions needed if a concrete neighboring claim or assurance question later arises. |
| **Publication-unit stability vs architecture replacement** | The pattern must not replace view, face, carrier, publication, or moving-lineage architecture. |

### E.17.AUD.OOTD:4 - Solution - make the subject, move and scope of a publication unit clear

#### E.17.AUD.OOTD:4.1 - Manager-first entry

> `PublicationUnit Primary-Subject Discipline` keeps one publication unit explicit about what it is mainly about, what claim or communicative move it carries, and what wider work remains outside.
>
> It becomes necessary when local repair is no longer enough and the publication unit still shifts among subject, concern, description, carrier, process, or downstream use while sounding unchanged.

First recover what the reader needed to understand, choose or do before this text was written. Ask where the property or relation in that question could arise. The reader may need an account of how a practice repeatedly produces a result, while the draft explains one participant’s choice. Trace what that choice establishes about the practice. Keep the incident as the subject when the request concerns that incident. When the wider question remains, recover the organization or rule that connects the pertinent cases and show the reader how to use it (C.39.QR:4.1, C.39.SA:4).

Examples of statements that clarify a unit’s scope include:
- `this memo is about the architecture boundary, not yet about the rollout plan`;
- `this review note is about the incident episode and the observed contrast, not yet a production-action recommendation`;
- `this comparison sheet is about the options under review, not yet about approval or the downstream decision`;
- `this semio note is about one pattern section or publication form, not the wider architecture policy around it`.

If that is the clarification you need, start here.
If the problem is still confined to one vague local lexical head, start with `E.17.AUD.LHR` (`Local Head Restoration`).

#### E.17.AUD.OOTD:4.1.a - Plain working terms

- **Publication unit** = a bounded piece of writing or display that the intended person or agent is meant to interpret as a whole, such as a note, memo, sheet, table or guided screen. A validator asked only to check syntax can finish with that result.
- **Primary subject** = what that bounded unit is mainly about for the current reading. It is an ordinary local publication term, not a new ontological kind.
- **Concern** = the question, aspect, or issue foregrounded about that subject. The concern can change while the subject remains the same.
- **`EntityOfConcern`** = the one `U.Entity` occupying the entity-participant position in the `C.2.1` constitution of one identified claim-bearing episteme. Neither a topic label nor a writing question identifies that participant by itself.
- **Carried move** = what the unit asserts, compares, explains, recommends, or otherwise communicates about its subject; it may also say that it only stabilizes the reading without adding a new claim.
- **Downstream use** = what a reader is invited or permitted to do with the unit, such as understand, compare, approve, rely, assign, or act.
- **Outside-work boundary** = what wider review, execution work, non-admissible downstream decision, or reliance claim stays outside the current unit.
- **Explicit transition** = the unit shows which subject, concern, move or use changes and why the new passage bears on the reader’s question. A move to one part, a model at another level of abstraction or a worked case may contribute a premise. Return from it to the conclusion its grounds support.

#### E.17.AUD.OOTD:4.1.b - What can change

Treat the publication unit as the bounded material the reader is meant to interpret together. One primary subject and move suffice for a simple reading. Where a decision depends on linked sections, identify each section’s subject and move and show how their connection supports the judgment. Identifying the unit this way leaves the source episteme, its `C.2.1` `EntityOfConcern`, the publication form, carrier and E.24.PUB occurrence under their own identity rules.

Keep five change types distinct:
1. a **subject change** changes what the unit is mainly about;
2. a **concern change** foregrounds another question or aspect while the subject may remain fixed;
3. a **claim or carried-move change** changes what the unit asserts, compares, explains, or recommends;
4. a **downstream-use change** changes what the reader is invited or allowed to do; and
5. an **`EntityOfConcern` change** occurs only when the claim-bearing episteme being carried has changed in the entity participant that its claims concern under `C.2.1`.

Use the optional prompts in 4.3 only when these distinctions are hard to recover from the unit itself.

Once the carried episteme `E` is identified, the author may add the conditional projection `publicationUnitPrimarySubject = EntityOfConcern(E)`, and only when both sides name the same entity. If the lens cannot stay stable after local repair, do not patch over the shift with a heavier declaration; reopen the unit or use the neighboring pattern that addresses the remaining question.

#### E.17.AUD.OOTD:4.2 - Scope and exclusions

**In scope**
- one publication unit with an unstable primary subject;
- one unit mixing concern, carried move, downstream use, and outside work;
- one unit quietly shifting between subject, description, carrier, publication unit, process, or downstream decision use;
- episteme-publication-heavy texts where repair disposition, the applicable boundary rule, primary subject, carried move, and outside work must stay explicit across one publication unit;
- a conditional `C.2.1` projection when one carried episteme and its entity participant are already identified.

**Out of scope**
- local lexical-head repair only;
- pure view, face, or carrier architecture work;
- entityOfConcernRef-preserving transform, explanation, bridge, ontology, or comparative-review questions for which a neighboring pattern already supplies the needed method or test;
- downstream gate, approval, execution, or decision pressure;
- invention of a publication-wide `EntityOfConcern` when no identified claim-bearing episteme supplies one.

**Ordinary stop rule.** If the commission is to clarify what a unit covers, a clear declaration can finish it. When the reader needs a judgment about the subject, state the judgment and the grounds it needs. A transition is required only when one occurred, and a neighboring-pattern reference only when a concrete unresolved question remains. A unit that has established one primary subject, one carried move, and one outside-work boundary needs no further assurance solely to establish them again. Ordinary use requires no diagnostic card, `ClaimGraph`, evidence dossier, assurance result, work record, or `C.2.1` projection unless a separate receiving use independently needs one.

#### E.17.AUD.OOTD:4.2.a - Choose the least-cost suitable unit architecture

“One primary subject” is a local default for a short unit meant to carry one readily recognizable move. It is not an ontological law and does not forbid a deliberately structured document that readers need as one unit.

Compare four repairs before deciding to split:

| Repair | Retain it when | Reject it when |
| --- | --- | --- |
| **Retain one unit with one declared primary subject** | one reader goal, one bounded downstream use, and one umbrella subject organize all included material; subordinate paragraphs do not introduce an independent move | the umbrella is a vague label hiding unrelated subjects or uses |
| **Declare an explicit transition inside one short unit** | the same reader and bounded use need a small ordered shift, and naming the from/to subject, concern, or move costs less than a split | later readers are likely to extract either part independently, or the second part licenses a different use |
| **Retain one multi-subject unit with marked sections** | the sections have clear local headings and moves, their dependency or shared decision question makes joint reading useful, and one scope/non-scope declaration prevents overread | section boundaries still leave audience, claim, or permitted-use changes hidden |
| **Split into separate units** | subjects serve different readers or actions, need independent reuse or approval, or one part falls outside the declared scope of the other | the split creates navigation, duplication, synchronization, or decision-assembly cost without reducing ambiguity |

Choose the least-cost option that preserves the meaning of the claims and the reader’s intended use. When the decision turns on a relation between two subjects, keep the comparison and its grounds available together in one passage or in connected, marked sections. Where there is no truthful umbrella subject or joint use, treat the material as separate units or split it. Give connected subjects their own headings when that helps the reader follow the relation. Expected savings in reading effort can guide a design choice. To report what particular readers actually understood, use evidence from their reading.

#### E.17.AUD.OOTD:4.3 - Ordinary declaration and optional diagnostic

A declaration of scope is complete when it gives the reader the following information.
- the bounded publication unit;
- its primary subject or the subjects whose connection matters to this use;
- the claim or communicative move it carries; and
- the wider work or use that remains outside.

One or two sentences can state that scope.

> This review note compares the interface-boundary options under the current incident evidence. Rollout responsibility and approval remain outside this note.

Do not require a separate card, record, identifier, table, or field set when that declaration is already clear. Add an explicit transition only when the unit changes subject, concern, carried move, or downstream use. Name a neighboring pattern only when one concrete unresolved question remains and that pattern supplies the needed instruction. Leave out an empty transition row or a search for a merely possible neighboring pattern.

When the sentence is hard to write or a reviewer suspects a hidden shift, use these six prompts privately as an optional diagnostic:

| Prompt | Diagnostic question |
| --- | --- |
| 1 | What material is the intended reader to interpret as one bounded unit? |
| 2 | What is it mainly about? If the decision connects subjects, which subjects and relation must readers see together? |
| 3 | Which concern is foregrounded, and what claim or communicative move does the unit carry? |
| 4 | What downstream use is permitted or blocked, and what wider work is outside this unit? |
| 5 | Has subject, concern, carried move, downstream use, or the `C.2.1` entity participant changed, and does the unit say precisely what changed? |
| 6 | If this remains unstable after local repair, which question remains, and which neighboring pattern supplies the needed repair or boundary? |

Use the six prompts to guide diagnosis. Once they yield a clear ordinary declaration, discard the diagnostic. The prompts need no six-row publication.

- If local repair is still enough, use `E.17.AUD.LHR` (`Local Head Restoration`) without adding more structure to the unit.
- If the unit remains one publication unit but a claim or downstream use depends on the neighboring-boundary claim kind, misuse risk, or cross-interpretation ambiguity, use the heavier extension as the assurance section.
- If the same unit is already stable as one primary subject, one carried move, and one outside-work boundary, and the remaining question is one bounded comparative review move over already available source epistemes or publications, apply `E.17.ID.CR` without expanding the declaration.
- If the unit cannot stay stable even after local repair, reopen the unit or apply the neighboring pattern that answers the remaining question. Adding fields to the declaration will not stabilize the unit.

#### E.17.AUD.OOTD:4.4 - Claim-bearing extension and quick boundary summary

Use the heavier extension only after the ordinary declaration is stable and a concrete neighboring claim or downstream use needs more detail.
The extension cannot stabilize a unit that still shifts between primary subjects, carried moves, or outside-work boundaries.

Then add only the fields needed by the current claim or downstream use:
- `publicationUnitFormCue`;
- `primaryInterpretation`;
- `transitionPolicy`;
- `modelingLensPolicy`;
- `downstreamDecisionPolicy`;
- `entityOfConcernProjection`, only for the `C.2.1` case stated in 4.1.b.

These fields supplement the ordinary declaration without establishing a separate set of rules. `publicationUnitFormCue` records words such as note, sheet, screen, and table as form clues only; it does not make those clues subjects, entity kinds, or claim kinds. `entityOfConcernProjection` records an already justified equality with the entity participant of one identified episteme; it neither creates that participant nor turns a topic into an entity. The remaining fields clarify the relevant boundary only when the ordinary declaration is not enough for a named later use.

**Quick boundary to neighboring patterns and project records**
- use `E.17.AUD.LHR` (`Local Head Restoration`) when the instability is still local to one lexical head, qualifier, or interpretation word;
- use `E.17.ID.CR` when the same publication unit already holds one stable primary subject, one carried move, and one outside-work boundary, and the question under repair is one bounded comparative review move over already available source epistemes or publications;
- use this pattern when the unit's unstable subject, concern, carried move, downstream use, or outside-work interpretation extends beyond local lexical repair;
- use the neighboring pattern that addresses the view, face, carrier, entityOfConcernRef-preserving transform, explanation, bridge, ontology, gate, approval, or execution question; keep any required project record with that question.

#### E.17.AUD.OOTD:4.5 - Boundary-rule summary

Use this summary to decide whether to stay with this pattern or move to a neighboring one.
1. choose the least-cost suitable unit architecture under 4.2.a: retain one primary subject, declare a transition, keep an explicitly sectioned unit, or split;
2. do not collapse primary subject, concern, `EntityOfConcern`, description, carrier, publication unit, carried move, process, and downstream use into one unchanged interpretation;
3. keep the carried move and permitted downstream use distinct from the wider work around them;
4. use `E.17.AUD.LHR` when one local head or qualifier is the defect; use this pattern when that repair cannot settle the unit's subject, move, use, or outside boundary;
5. apply `E.17.ID.CR` when publication-unit stability already holds and the remaining question is one bounded comparative review move over already available source epistemes or publications;
6. move out when the unit starts carrying downstream decision pressure or another neighboring-pattern question.

### E.17.AUD.OOTD:5 - Archetypal grounding

The cases below show alternative outcomes in architecture, operations, episteme publication, a return to comparison, and a changed concern. They do not prescribe a progression.

#### E.17.AUD.OOTD:5.1 - Architecture note shifting into rollout work

A short architecture memo begins with:
`This note is about the proposed service boundary between catalog and checkout.`

Three paragraphs later it says:
`We should therefore assign rollout responsibility to platform and stage migration in two sprints.`

The memo moved from the interface to a proposal to assign and schedule rollout. Mark the transition if the reader needs both, or put independent rollout work in its own unit. Moving from describing to assessing the same interface need not change the `C.2.1` `EntityOfConcern` of the episteme.

For an introduction, “This note introduces the service boundary between catalog and checkout. Rollout is outside its scope” can finish the job. For an assessment, keep the two sides together and give the finding. Suppose checkout must handle every agreed catalog response. The catalog can return “item unavailable” and checkout accepts only a priced item. The current interface therefore fails that requirement. One such response settles this failure. To establish compatibility for that requirement, show that checkout handles every agreed response under the stated conditions.

Either finding can guide an interface decision. Where a broader assessment also depends on an unknown deployment condition, identify what remains open. A standing rule can assign qualifying rollout work to the duty shift. If a separate allocation is reserved to a particular party, establish that act before reporting who has been assigned.

#### E.17.AUD.OOTD:5.2 - Operations note shifting into approval

An incident note begins as a comparative review of timing variance and operator context.
It ends as if it already recommends a production action.

The incident may stay the primary subject while the move changes from comparison to recommendation. Mark the change if the reader needs both. To communicate an existing approval, cite its authoritative outcome and scope. For a status inquiry, identify the pending approval and who holds the authority. Take the proposal and its grounds to that authority when the commission or a duty requires it.

Use `C.11` if the new text chooses among already available actions. If an actual approving communication and an instituted permission matter, keep the `A.2.9` communicative Work and the `A.2.8.PER` grant relation separate. Use `A.21` only when a current `OperationalGate(profile)` publishes a gate decision.

#### E.17.AUD.OOTD:5.3 - Semio-heavy text mixing one local section and wider architecture strategy

A semio note starts about one selected pattern section and ends as if it had decided the packaging strategy for the whole overlay.

Here the primary subject broadens from the selected section to the whole overlay, and the carried move broadens from local interpretation to strategy. The unit should state:
- what the note is about now;
- what concern and move it carries over that subject;
- and what wider architecture strategy remains outside the current unit.

If the commissioned question is the packaging strategy itself, inspect what the section establishes for it. For example, a distribution option that requires every section to stand alone can be ruled out by one section whose essential definition is available only in another. That finding can settle a request to assess this option. To design a workable distribution, establish which definitions readers need together and how each reader will obtain them when needed. The list of required terms from this one section can contribute to that design.

#### E.17.AUD.OOTD:5.4 - Unit stabilizes and bounded comparison becomes primary

A review note first shifts between the selected interface boundary, the move it is making over the current evidence, and the rollout implications around that boundary.
After one publication-unit repair it now says:
`This review unit is about the interface-boundary options and the contrast they make visible under the current incident evidence; rollout responsibility and approval remain outside this note.`

At that point the same unit already holds one stable primary subject, one carried comparison move, and one outside-work boundary.
`PublicationUnit Primary-Subject Discipline` has done its job.
If the remaining question is now one bounded comparison between the already pinned options over the same evidence, use `E.17.ID.CR` for that contrast. The unit needs no further stabilization for this purpose.

#### E.17.AUD.OOTD:5.5 - Outside observation changes the live concern or carried claim

A release-readiness note is already explicit that it is about one candidate publication or view and the risk state visible from the current evidence.
Mid-review, an external vendor bulletin and a new field observation change the reported failure boundary for that same candidate.

The candidate and the question about its current risk can both remain the same while new evidence changes the answer. For a request about an earlier date, preserve the finding within its stated evidence window. Reconsider a pending decision if its grounds have changed. An `EntityOfConcern` change arises only when a claim-bearing episteme has a different entity participant under `C.2.1`.
For the unit and the further work it supports, choose the applicable continuation:
- stop the current unit at the originally declared evidence boundary and open a new downstream record for the changed question;
- revise the affected claim in the same unit, retaining the original question and bounds wherever they still apply;
- or use the downstream decision or work pattern whose instructions now fit once approval, execution, or another downstream decision publication becomes the primary question.

The bulletin and field observation remain sources until a support, evidence, or currentness claim makes `A.10` relevant. Use `C.11` for a later choice, `A.2.9` and `A.2.8.PER` for an approving act and its permission effect, `A.15` for a work claim, and `A.21` only for an actual gate decision.

#### E.17.AUD.OOTD:5.6 - Deliberately sectioned multi-subject review packet

A release-readiness group needs one packet for one meeting. The packet contains three sections with distinct headings:

1. **Interface-boundary options** — compares two architecture alternatives.
2. **Incident evidence** — summarizes the observations that discriminate between those alternatives.
3. **Rollout constraints** — states constraints the later approval decision must respect, without assigning work or granting approval.

The local one-subject heuristic does not force three documents. The packet has one umbrella subject that fits all three sections—`the evidence and constraints needed to review the interface-boundary choice`—and one bounded use: inform the review, not approve rollout. Keeping the three section-level subjects together avoids navigation and synchronization cost, and the headings distinguish each section’s move from the others.

An unsectioned version is rejected because readers cannot see the subject and move changes. A short narrative with only one small shift may instead declare that transition. Separate documents become the least-cost choice when the rollout section starts assigning responsibility, serves another audience, needs independent reuse, or becomes an approval input with its own reliance boundary.

### E.17.AUD.OOTD:6 - Bias-Annotation
This pattern favors making the unit’s reading stable and visible. It discourages letting the unit take on wider work or decision pressure without marking that change.
To counter that bias, name the primary subject, concern, carried move, downstream use, and outside work. Use `EntityOfConcern` only when `C.2.1` warrants that identification. Return promptly to `E.17.ID.CR` when the unit is stable and a bounded comparison remains, and state which boundary applies once a downstream claim becomes primary.

### E.17.AUD.OOTD:7 - Conformance Checklist

**Checklist scope.** Use this checklist when checking a claimed application of this pattern, not as nine required authoring steps. A short declaration can settle scope. When the unit is commissioned to assess its subject, check that the reader also gets the judgment and its grounds. Inspect only the rows implicated by the unit, transition, `EntityOfConcern` projection, neighboring claim, or unit-architecture choice, and do not publish a nine-row record by default.

1. **CC-OOTD-1 - One publication unit is explicit.**
   The text identifies the publication unit under review as one note, memo, sheet, screen, table, or section meant to be read as one unit.
2. **CC-OOTD-2 - Primary subject is explicit.**
   The unit states what it is mainly about in ordinary language rather than asking readers to infer it from tone.
3. **CC-OOTD-3 - Any `EntityOfConcern` projection is exact and conditional.**
   The unit uses `EntityOfConcern` only for the entity participant of one identified claim-bearing episteme under `C.2.1`. A topic label alone does not identify that participant. An independently identified entity, including an admitted relation kind, may do so when the claims concern it.
4. **CC-OOTD-4 - Concern, carried move, downstream use, and outside work are distinct.**
   The unit states which question it foregrounds, what it asserts or communicates, how readers may use it, and which wider work, approval, execution, decision, or reliance remains outside.
5. **CC-OOTD-5 - Any transition is typed and explicit.**
   For a change of subject, concern, carried move, downstream use or entity participant, the reader can tell why the passage shifts and what conclusion returns to the original question. A wider conclusion needs grounds across its stated range.
6. **CC-OOTD-6 - Choose between local and publication-unit repair.**
   Use `E.17.AUD.LHR` when one local head or qualifier is the defect. Apply this pattern when that repair cannot settle the unit's subject, move, use, or outside boundary.
7. **CC-OOTD-7 - Neighboring-pattern boundary is explicit.**
   If an entityOfConcernRef-preserving transform, explanation, bridge, comparative-review, ontology, gate, approval, or execution claim becomes primary, use the neighboring pattern that defines or constrains that claim.
8. **CC-OOTD-8 - Claim-bearing lens is stated when needed.**
   If a claim or downstream use materially depends on a minimal modeling lens, `C.2.1` projection, or downstream-decision policy, state that lens, projection, or policy.
9. **CC-OOTD-9 - Choose the least-cost suitable unit architecture.**
   Retaining one unit, declaring a transition, keeping a sectioned multi-subject unit, or splitting is chosen from the current reader, use, reuse, dependency, and overread costs. The author does not split to satisfy a count and does not retain a vague umbrella to avoid a necessary split.

### E.17.AUD.OOTD:8 - Common Anti-Patterns

- **Local-repair inflation.** Opening publication-unit discipline when one overloaded local lexical head or qualifier is the defect that remains.
- **`EntityOfConcern` inflation.** Calling every topic, kind, interpretation, question, or writing transition an `EntityOfConcern` or `EntityOfConcern` change.
- **Work-process smuggling.** Letting a note begin as architecture, incident review, or comparison work and end as rollout, approval, or execution guidance without naming the transition.
- **Admissibility-pattern replacement.** Treating this pattern as if it replaced view, face, or carrier architecture, entityOfConcernRef-preserving transform rules, explanation-face rules, bridge rules, or downstream decision texts.
- **Overgrowth by declaration.** Stacking fields onto a unit while readers still cannot tell which subjects and moves it connects or what remains outside.

### E.17.AUD.OOTD:9 - Consequences

Using the pattern well has three main benefits:
- authors stop smuggling wider work into one unit by accident;
- reviewers can name whether subject, concern, carried move, or downstream use changed instead of only arguing about wording;
- neighboring patterns and downstream decision texts stop getting blamed for confusion created one layer earlier.

The cost is that some notes must become shorter, split earlier, or reopen with the change stated when their subject, concern, carried move, or downstream use changes.


### E.17.AUD.OOTD:10 - Rationale

This pattern leaves the architecture of views, faces, carriers, epistemes, and downstream decision texts to their respective methods.
It addresses a smaller problem. A publication unit can mislead even when each sentence appears acceptable on its own.

`A.6.P`, `A.7`, `E.10`, and `F.18` already keep kinds, distinctions, and naming precise. `C.2.1` already identifies the entity participant of one claim-bearing episteme. This pattern adds a discipline for the bounded publication unit: choose the least-cost suitable architecture for that unit, make its primary subject or section-level subjects and moves visible, and keep downstream use and outside work explicit. It borrows `EntityOfConcern` only through the conditional projection in 4.1.b and does not extend that ontology.

The pattern also draws on `E.14` and `E.19`.
Recognition comes first through a manager-usable entry block and one ordinary natural-language declaration; the six prompts remain an optional diagnostic.
Heavier declaration comes only after the ordinary declaration already holds and a named receiving use consumes the added fields.

### E.17.AUD.OOTD:11 - SoTA-Echoing

**Source boundary.** These sources support topic focus, scope/non-scope, reader-need organization, and explicit document structure. None establishes a universal ontological rule that every publication unit has one subject, and none supplies a `C.2.1` entity participant. OOTD therefore keeps the one-primary-subject rule as a defeasible local heuristic and compares it with transition, sectioning, and splitting.

| Publication-unit obligation | Exact source and current contribution | Local repair of the source limit | Working implication here |
| --- | --- | --- | --- |
| Keep the current unit focused and expose its scope and non-scope. | [Google Technical Writing One — Documents](https://developers.google.com/tech-writing/one/documents) (updated 2025-07-07) tells authors to state scope and non-scope, then refocus or revise the scope when content veers; [Paragraphs](https://developers.google.com/tech-writing/one/paragraphs) (updated 2025-03-28) treats a paragraph as one independent unit of logic focused on one topic. | Paragraph focus does not imply one subject for every memo, packet, or document. OOTD scales the move by naming the bounded unit and comparing retention, explicit transition, sectioning, and splitting. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:4.3`, `E.17.AUD.OOTD:5.1`, `E.17.AUD.OOTD:5.6` |
| Organize documentation around the user's need and keep different action/cognition modes visible. | [Diátaxis](https://diataxis.fr/) organizes content, architecture, and form around four distinct user needs; its [compass](https://diataxis.fr/compass/) tests whether material informs action or cognition and supports acquisition or application, at sentence or whole-document scale. | The four modes diagnose a use shift but are not an FPF ontology or a formula for document count. OOTD names the carried move and downstream use, then keeps one structured unit only when a shared reader goal makes that cheaper and still clear. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.2`, `E.17.AUD.OOTD:5.6` |
| Use a single-subject reusable topic when modular reuse is the main need. | [OASIS DITA 1.3 `<topic>`](https://docs.oasis-open.org/dita/dita/v1.3/os/part1-base/langRef/base/topic.html) defines the top-level topic as a single-subject topic or article. This is established structured-authoring lineage (2015), not the current source of OOTD's whole-document rule. | A DITA topic is one valid reusable unit architecture, not evidence that a deliberately sectioned review packet is defective. OOTD selects it when independent reuse or retrieval dominates and otherwise permits the coherent multi-section unit. | `E.17.AUD.OOTD:4.2.a`, `E.17.AUD.OOTD:5.6` |
| Keep object words and local designations precise without importing another concept system. | ISO 704:2022 and ISO 1087:2019 terminology practice distinguishes objects, concepts, definitions, designations, and terms. | Terminology discipline repairs overloaded heads but does not choose the publication architecture. OOTD uses `E.17.AUD.LHR` for a local-head defect and its own architecture choice when the instability extends beyond that repair. | `E.17.AUD.OOTD:4.1.a`, `E.17.AUD.OOTD:4.2`, `E.17.AUD.OOTD:5.3` |

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
