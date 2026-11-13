## E.17.AUD - Keep a Publication Unit Stable (PublicationUnit Stability Discipline)

> **Status:** Stable

**Plain name.** Keep one publication unit stable enough for readers to identify its subject, publication move and outside boundary.

### E.17.AUD:1 - Problem frame

Use this pattern when people read a note, memo, sheet, table, screen, or short section as one stable unit but it leaves a change in its main subject, its publication move, or its boundary with a decision, gate, work, or reliance claim unmarked.

A typical case starts with one bounded architecture or status question and ends by sounding like rollout, approval, assignment, or assurance. One reviewer wants to repair a vague word, another wants to rewrite the whole unit, and a third sees a comparison or explanation problem. Before they patch different defects, identify the bounded publication unit and its current interpretation.

Name the unit's primary subject. When it carries or exposes a claim-bearing `U.Episteme` or episteme-side `U.View`, use that item's `EntityOfConcern` value only when it is also the unit's primary subject. Otherwise name the ordinary topic or subject and do not invent an `EntityOfConcernRef`. Keep the publication unit distinct from the episteme, publication occurrence, form, face, carrier, and any downstream project claim.

The primary reader is an author or reviewer who needs one usable repair choice. Architects, managers, and program leads are secondary readers when the same unit is being over-read as architecture, approval, or work guidance.

If this check is missed, teams repair one word when the whole interpretation has shifted, rebuild a whole unit when one local head was enough, or polish a comparison, explanation, or status note until it looks like evidence or approval.

The check helps the team choose one response early: keep the unit as it is, repair one local head, stabilize the whole unit, treat it as a bounded comparison, or leave this pattern for the applicable neighboring pattern and project record.

Use `E.17.AUD.LHR` when an overloaded local head is the only defect. A stable unit presenting a bounded comparison calls for `E.17.ID.CR`; an explanation-use problem calls for `E.17.EFP`. If the text is already being used to approve, direct, assign, adjudicate, or support reliance, use the applicable decision, gate, work, evidence, or reliance pattern. In those cases the narrower or neighboring pattern governs the work.

The first useful result is one of those five repair choices. If the unit, its primary subject, its publication move, and its outside boundary are already clear enough for the current reader, return `stable for current use` and stop. Use the checks and examples as needed. Their order is optional.

### E.17.AUD:2 - Problem

Without a named publication-unit stability discipline:
1. teams repair local wording when the interpretation of the whole unit is unstable;
2. teams open whole-unit stabilization when the defect is one overloaded local lexical head;
3. teams extend a publication-unit repair when the task already calls for a bounded comparison;
4. teams mistake note, sheet, table, or screen labels for different kinds of publication unit when they name different presentation forms of one unit;
5. teams infer an engineering-process, approval, or rollout claim or effect that the text does not support.

### E.17.AUD:3 - Forces

| Force | Tension |
| --- | --- |
| **Recognisability vs precision** | Cold readers need a recognizable situation at the start. The unit must also make its primary subject, its publication move and its boundary with outside work explicit. |
| **Local repair vs whole-unit stabilization** | It is cheaper to fix one overloaded local lexical head, but the whole unit may have changed its primary subject, its publication move, or its boundary with work, work planning, decision, gate, or a reliance claim without marking the change. |
| **Stability vs the boundary with the next pattern** | Teams want to keep one unit usable, but they also need to recognize when the question has shifted to comparison, explanation, or a downstream claim or effect. |
| **Form variety vs publication-unit fidelity** | Note, memo, sheet, table, and screen are convenient ordinary labels, but a switch from the unit under review to its presentation form must be marked. |
| **Readability and unsupported downstream claims or effects** | Clearer or more polished prose helps readers, but it does not by itself establish an approval, policy, gate, work, or reliance claim or effect. |

### E.17.AUD:4 - Solution

> Name what the unit is mainly about, the publication move it carries, the claim that remains outside, and one repair choice. Apply another pattern only when that choice requires it.

#### E.17.AUD:4.0 - Plain working terms

- `publication unit under review` = one note, memo, sheet, table, screen, or short section that readers inspect as one unit;
- `primary subject` = what the unit is mainly about. `publicationUnitPrimaryEntityOfConcern` names the primary `EntityOfConcern` of the claim-bearing episteme or episteme-side view carried by the unit. When no such EntityOfConcern applies, use the non-claim-bearing kind named by value or an ordinary topic or subject without inventing an `EntityOfConcernRef`. An ordinary topic or subject value is not a claim about a C.2.1 entity participant;
- `carried publication move` = the claim, interpretation, comparison, or explanation move the unit makes about that primary subject;
- `outside boundary` = a decision, gate, `U.Work`, work planning, reliance claim, or continuing engineering work that remains outside the unit;
- `local lexical head` = one word or phrase such as `review`, `interpretation`, `note`, or `text` whose meaning is unstable inside an otherwise stable unit;
- `repair choice` = stable for current use, local-head repair, whole-unit stabilization, bounded comparison, or leave publication-unit stability for explanation classification, bridge or hypothesis work, representation change, controlled coarsening, a changed primary EntityOfConcern, or a downstream action, authority, adjudication, decision, gate, work, or reliance claim;
- `applicable pattern and project reference` = the FPF pattern to apply plus, when the live claim needs it, the exact evidence, gate, decision, work-plan, work-occurrence, method, action-invitation, or relation record, selected `U.Episteme`, or exact `EpistemePublicationRelation` occurrence when availability matters;
- `publication-unit stability family` = `E.17.AUD`, `E.17.AUD.LHR`, and `E.17.AUD.OOTD` together with their comparison and explanation neighbors, grouped here for selecting the applicable repair;
- `presentation-form label` = `note`, `memo`, `sheet`, `table`, `screen`, or a similar description of form. The label alone does not establish the unit’s kind.

Use the terms above only when their distinctions change the repair choice.

#### E.17.AUD:4.1 - Minimum admissible interpretation

A locally admissible interpretation keeps four entries available for inspection by value:
- one publication unit under review;
- one primary subject;
- one carried publication move over that primary subject;
- one outside boundary to work, work planning, decision, gate, or reliance claim, with one light boundary type when that distinction matters: neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation.

If the publication unit changes any of those four without saying so, its interpretation has shifted, however polished the sentences look.

#### E.17.AUD:4.2 - Publication-unit stability vs whole-unit requirement
**Ordinary result.** Choose one of the following responses.
- `stable for current use`: the four-part interpretation is explicit enough and none of the neighboring questions named above is live;
- `local lexical-head repair`: apply `E.17.AUD.LHR` to the overloaded head;
- `whole-unit stabilization`: apply `E.17.AUD.OOTD` to the unit;
- `bounded comparison`: if the unit is stable, apply `E.17.ID.CR`;
- `leave publication-unit stability`: the live question concerns work, work planning, decision, gate, evidence, explanation, reliance, carrier or front-end work, or another claim that this pattern does not test; apply the relevant pattern and name the exact project object or record.

Leave the narrower whole-unit check to `PublicationUnit Primary-Subject Discipline`. Its question is whether this unit can still keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim.

#### E.17.AUD:4.3 - Inherited dynamic frame

When the unit describes a lineage or move, use `C.2.2a` or `A.16.0` for that subject and inspect how the unit expresses it.

#### E.17.AUD:4.4 - Kind and boundary

Treat one publication unit as a readable unit. Do **not** identify it automatically with:
- the `U.Episteme` or episteme species whose claims the unit carries, quotes, or describes;
- an `EpistemePublicationRelation` occurrence, publication form, or carrier involved in making that selected episteme available;
- the primary subject, including the exact EntityOfConcern when applicable;
- a generic publication face or MVPK face under E.17 constraints;
- a carrier or evidence carrier;
- proof, evidence record, assurance claim, or release admissibility;
- a view or viewpoint;
- an engineering-process stage;
- a downstream decision, gate, work, or reliance publication.

Those objects may matter, but mentioning them in the same note, sheet, or screen does not make them the current publication-unit problem.

**Publication-unit boundary choice.** A `PublicationUnit` boundary is valid when a careful reader would naturally inspect that bounded item as carrying one primary publication move over one primary subject, with one visible outside boundary to work, work planning, decision, gate, reliance claim, or neighboring pattern application.

Choose the bounded item that carries the claim being made or effect being repaired. Do not choose a smaller boundary merely to hide a downstream overclaim, or a larger one merely to absorb several primary subjects into one unit.

A table row may be the unit when that row carries the claim; the whole table may be the unit when the table-level caption or comparison frame carries the claim. A dashboard tile, note, card, sheet, or screen block may be the unit only when that bounded item, not the whole carrier or interface, carries the live publication move.

**Publication-unit snapshot identity.** A `PublicationUnit` may remain the same bounded unit while its carrier rendering, export format, screenshot, or layout changes. It does not remain the same stabilized interpretation by visual or file continuity alone.

If a revision, refresh, translation, regeneration, or dashboard update changes the primary subject, carried publication move, outside boundary, source pins, or admissible use, rerun the four-part interpretation for the new snapshot before the unit is used for comparison, explanation, evidence, gate, decision, work, or reliance claims.

#### E.17.AUD:4.5 - Ordinary working card

When a wider repair needs these distinctions, use the seven questions to recover them:

| Row | Ordinary prompt |
| --- | --- |
| 1 | Which publication unit is under review? |
| 2 | What is that unit mainly about in this interpretation? |
| 3 | What publication move does the unit make about that subject in this interpretation? |
| 4 | What downstream `U.Work`, work planning, decision, gate, or reliance claim remains outside this unit, and is that boundary mainly a neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation? |
| 5 | Does the present problem call for repair of an overloaded local head, stabilization of the whole unit’s primary subject, bounded comparison, or another neighboring pattern? |
| 6 | Is the current form label (`note`, `sheet`, `table`, `screen`, and similar ordinary labels) naming only the presentation form, or are readers taking it to change the publication unit under review or the kind of downstream claim or effect they infer? |
| 7 | Does the current interpretation depend on a modeling substrate or rationale to identify the primary subject or carried publication move, and if so is the necessary substrate or rationale published where the reader can recover that subject or move for this unit? |

#### E.17.AUD:4.6 - Choose the next pattern

- If row 5 points to one overloaded local lexical head, apply `Local Head Restoration`.
- If row 5 shows that the whole publication unit still cannot keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim visible, apply `PublicationUnit Primary-Subject Discipline`.
- If the publication unit is stable enough and its move is bounded comparison over available source publications, apply `E.17.ID.CR ComparativeReviewUnit`.
- If the main problem is explanation classification over an existing face, apply the neighboring explanation pattern.
- If claim content, representation, coarsening, or the primary EntityOfConcern changes, apply the relevant `A.6.3` or `A.6.4` pattern before checking a later publication form here.
- If the active problem situation is publication form, bridge or hypothesis work, or a downstream claim or effect, leave the publication-unit stability family, apply the relevant pattern, and name the exact project object or record when one is needed.

#### E.17.AUD:4.7 - Local naming rule

Treat ordinary labels such as `note`, `memo`, `sheet`, `table`, `screen`, `review`, and `status` as clues to presentation form. A label alone does not establish the kind of publication unit.

Working rule:
- if one overloaded local lexical head is doing most of the semantic work, repair that local lexical head first through `Local Head Restoration`;
- if the local lexical head does not explain the instability, keep the publication unit stable in the whole-unit stabilization pattern. Adding another qualifier could hide the shift in interpretation;
- cleaner or more formal wording cannot make an inadmissible downstream claim, effect, or comparison source relation admissible.

#### E.17.AUD:4.8 - Keep a needed model or rationale visible

If the primary subject or the carried publication move depends on a modeling substrate or rationale, publish that substrate or rationale briefly in the unit or move the case to a fuller publication form or neighboring pattern that can carry it. When the interpretation depends on a formal model or rationale, wording repair alone is insufficient.

#### E.17.AUD:4.9 - Keep stronger claims separate

When explanation, comparison, or a downstream claim is load-bearing, keep five facts recoverable to preserve the repair choice:
- evidence status and source-pin status when the unit leans on already available source publications;
- which reliance or interpretation of work is currently admissible on the basis of this unit, and which decision, work or gate claims cannot be made on that basis;
- whether this unit is the primary publication unit or a derivative helper publication;
- any claim-bearing modeling substrate or rationale;
- how any assurance finding corrects or bounds the opening claim according to its result. If the revision also proposes a downstream claim or effect, distinguish that proposal from what the finding establishes.

### E.17.AUD:5 - Worked slices

#### E.17.AUD:5.1 - Local-head case

A semio note keeps saying `this review` and `this interpretation`, but nobody can tell which FPF kind or locally declared head those lexical heads name here. Once those terms are clarified, the rest of the unit is stable. Use `Local Head Restoration`; a whole-unit repair is unnecessary.

#### E.17.AUD:5.2 - Whole-unit interpretation-shift case

A memo starts about one bounded architecture question over an inherited lineage or move, then shifts into wider rollout or approval language without declaring the transition. Repairing one sentence does not stabilize the publication unit under review because its concern and carried publication move have widened; that widening does not by itself establish a changed EntityOfConcern. Use `PublicationUnit Primary-Subject Discipline`.

#### E.17.AUD:5.3 - Stable-unit comparison case

A comparison sheet already keeps one stable primary subject and one clear outside boundary to work, work planning, decision, gate, or reliance claim, but the team is using publication-unit instability language because the comparison is contentious. Use `E.17.ID.CR ComparativeReviewUnit`. The team can address the contested comparison without further stabilization.

#### E.17.AUD:5.4 - Explanation-laundering case

An onboarding explainer starts from one stable source-pinned note, but then the simplified prose begins to sound like canonical assurance or policy. The publication unit may still be readable, yet its main problem has shifted from unit stability to explanation use. Use `E.17.EFP`'s simpler source-linked boundary sentence first; instantiate `ExplanationFaithfulnessProfile` only when explanation-class ambiguity still changes the next action.

#### E.17.AUD:5.5 - Downstream decision and reliance case

A status card starts as one bounded summary of progress, then leads readers to infer approval, assignment, or go or no-go claim or effect. The problem is no longer only publication-unit stability. Treating the card as a neutral note would miss those consequences. Use the downstream decision, gate, work, or reliance publication.

#### E.17.AUD:5.6 - Quick contrasting cases

Use this quick contrast set when the initial interpretation is unclear:

| Near-miss case | What to look for | Next pattern or project reference |
| --- | --- | --- |
| `LHR-only` | one overloaded local lexical head is doing most of the semantic work while the publication unit under review otherwise stays stable | apply `Local Head Restoration` |
| `whole-unit interpretation shift` | the publication unit under review changes its primary subject or carried publication move without marking the change | apply `PublicationUnit Primary-Subject Discipline` |
| `stable comparison -> CR` | the unit is already stable and the live problem situation is bounded comparison over pinned source publications | apply `E.17.ID.CR ComparativeReviewUnit` |
| `downstream claim or effect overread` | readers are inferring approval, assignment, or go or no-go claim or effect from the publication unit | leave the publication-unit stability family for the applicable downstream decision, gate, work, or reliance publication |
| `modeling-lens hidden` | the unit only makes sense because of one unpublished model, formal substrate, or rationale | publish that substrate or rationale briefly or use a heavier publication form or neighboring pattern |

### E.17.AUD:6 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | How to avoid it |
| --- | --- | --- |
| Fixing one sentence while the whole unit has changed interpretation without marking the change | local repair is asked to carry whole-unit stabilization | check primary subject, carried publication move, and outside boundary to work, work planning, decision, gate, or reliance claim before repairing the sentence |
| Treating form labels as if they changed the publication unit under review | `table`, `sheet`, or `screen` is used as if it already named a different ontology or downstream claim or effect | treat those as presentation forms first; only leave this pattern when the problem situation changes |
| Laundering comparison through stability language | teams keep saying the unit is unstable when the active problem situation is already bounded comparison | apply `E.17.ID.CR ComparativeReviewUnit` and name the exact source publications |
| Laundering downstream decision or reliance through clearer prose | a better-written note is mistaken for an approval, gate, work, or reliance text | keep the outside boundary to work, work planning, decision, gate, or reliance claim explicit and leave this pattern when downstream claim or effect appears |
| Letting three repair choices act at once | lexical-head repair, whole-unit stabilization, and a neighboring-pattern application are patched in parallel with no shared primary-subject interpretation | use the working card first and name one repair choice before patching the unit |

### E.17.AUD:7 - Consequences

- You pause to name the problem with the publication unit before patching the draft.
- You reduce unnecessary escalation from one overloaded local lexical head into a whole-unit rewrite.
- You reduce the opposite failure too: trying to solve whole-unit interpretation instability with one more qualifier on the same local lexical head.
- You keep neighboring publication-unit repair patterns and neighboring non-publication-unit patterns explicit so that a broad stability label does not obscure which pattern applies.
- You make it harder for clearer prose, official-looking formatting, or wider circulation to be mistaken for a downstream claim or effect.

### E.17.AUD:8 - Rationale

Local lexical-head repair and whole-unit primary-subject stabilization address different problems. Authors and reviewers need one check that distinguishes those cases, recognizes a bounded comparison, and shows when the work has moved outside the publication-unit stability family.

The pattern has a narrow scope. It does not turn every publication-unit problem into publication design or downstream decision, gate, work, or reliance work. It helps readers identify the publication unit’s primary subject, the move it makes about that subject, and which downstream `U.Work`, work planning, decision, gate, or reliance claim remains outside.

### E.17.AUD:9 - SoTA-Echoing

**Claim 1.** FPF’s current treatment of EntityOfConcern and descriptions keeps the entity of concern distinct from the claim-bearing episteme or publication that describes it. This supplies the exact-entity case of the publication-unit subject distinction.

**Practice, source, alignment, and adoption.** `C.2.1`, `A.7`, `E.17`, and the description patterns keep an EntityOfConcern, a description episteme, its publication occurrence, form, and carrier distinct. ISO/IEC/IEEE 42010:2022 is standards lineage for the narrower architecture/architecture-description distinction, not the source of this general publication-unit ontology.

`PublicationUnit Stability Discipline` adapts that FPF distinction to one readable unit and requires a primary-subject shift to be explicit; an EntityOfConcern change requires the exact C.2.1 case. For a reviewer or architect, this distinction guides worked slices 5.2 and 5.3.

**Claim 2.** Information-for-use practice treats user-facing units as purpose-bound, structured information rather than as loose bundles that can mix explanation, instruction, warning, and decision or reliance effect by convenience.

**Practice, source, alignment, and adoption.** Joint IEC and IEEE 82079-1:2019 requires information for use to be purpose-directed, structured, and evaluated for usability.

`PublicationUnit Stability Discipline` adopts purpose-bound publication units and explicit outside boundaries to work, work planning, decision, gate, or reliance claim, adapts that discipline from information-for-use to notes, memos, sheets, tables, and screens, and rejects the shortcut where a clearer or official-looking unit is treated as approval, policy, gate, work, or reliance text.

For a manager or operator, this matters in worked slices 5.4 and 5.5: better explanatory form does not by itself establish downstream claim or effect.

**Claim 3.** Pattern-writing and pattern-validation practice keeps patterns tied to recognisable situations, explicit problem, solution, and consequence structure, and reviewable rationale rather than elegant internal naming alone.

**Practice, source, alignment, and adoption.** Iba (2021), [How to Write Patterns](https://hillside.net/plop/2021/plopourri/PLoP21_PLOPOURRI_Iba_Methodology4.pdf), and Riehle, Harutyunyan, and Barcomb (2025), [Pattern Discovery and Validation Using Scientific Research Methods](https://doi.org/10.1007/978-3-662-70810-1_6), with the [authors' 2021 preprint](https://arxiv.org/abs/2107.06065), treat pattern writing and validation as requiring recognisable situations, explicit structure, and reviewable reasoning rather than only elegant naming.

`PublicationUnit Stability Discipline` adopts worked slices, recognisable entry cues, and an explicit next-pattern and project-reference boundary, adapts those expectations to publication-unit stability work, and rejects a well-labeled pattern text that offers too little domain content or too little guidance for its reader.

For a reader using the pattern, this matters in the Problem frame and slices 5.1 through 5.5: the pattern should be usable before one has to reconstruct the surrounding rationale from the beginning.

**Local stance.** The unit is sufficiently clear for its declared use when readers can recover its primary subject, carried publication move and outside boundary, and apply the neighboring pattern needed by a different problem. This clarity judgement does not itself establish the truth or warrant of its claims.

### E.17.AUD:10 - Conformance Checklist

1. **CC-AUD-1 — One publication unit under review is explicit.**
   The case names one note, memo, sheet, table, screen, or short section as the unit under review. Its presentation-form label alone does not identify that unit.
2. **CC-AUD-2 - Primary subject and carried publication move are explicit enough to identify the applicable pattern.**
   The case keeps visible the unit’s primary subject and the publication move it makes about that subject.
3. **CC-AUD-3 — Outside-work boundary is explicit.**
   The case states what downstream `U.Work`, work planning, decision, gate, or reliance claim remains outside the publication unit under review, including neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation when that distinction matters.
4. **CC-AUD-4 — The active repair choice is named.**
   The case returns `stable for current use` when the unit, primary subject, carried publication move, and outside boundary already suffice. Otherwise it names local lexical-head repair, whole-unit primary-subject stabilization, bounded comparison, or the applicable neighboring pattern rather than patching several problem situations at once.
5. **CC-AUD-5 - The next pattern and project-reference boundary is explicit.**
   When the problem calls for `Local Head Restoration`, `PublicationUnit Primary-Subject Discipline`, `E.17.ID.CR ComparativeReviewUnit`, an explanation-faithfulness pattern, or a downstream decision, gate, work, or reliance pattern, name the pattern to apply and the exact project object or record when one is needed.
6. **CC-AUD-6 — Presentation-form labels do not launder publication-unit kind or downstream claim or effect.**
   `note`, `memo`, `sheet`, `table`, `screen`, and similar labels are clues to presentation form. They do not silently change the unit under review, create proof or evidence, make a release admissible, or establish a downstream claim or effect.
7. **CC-AUD-7 - A claim-bearing modeling substrate or rationale remains visible.**
   If the primary subject or carried publication move depends on a modeling substrate or rationale, publish that substrate or rationale briefly enough for review or handle the case by a fuller publication form or neighboring pattern that can carry the needed basis.
8. **CC-AUD-8 — Clearer prose does not silently widen downstream claim or effect.**
   Readability, formatting, and wider circulation may improve the unit, but they do not by themselves turn the unit into approval, policy, assignment, gate, work, or reliance text.

### E.17.AUD:11 - Relations

- **Builds on:** `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `E.17`, and `C.2.1`.
- **Coordinates with:** `E.17.AUD.LHR Local Head Restoration`, `E.17.AUD.OOTD PublicationUnit Primary-Subject Discipline`, `E.17.ID.CR ComparativeReviewUnit`, `E.17.EFP ExplanationFaithfulnessProfile`, and `E.21` when a pattern-quality card, table, status line, or generated summary is published as a bounded publication unit. Use `E.17.AUD` to test whether the publication unit keeps its subject, move and outside boundary clear and `E.21` to evaluate the underlying pattern-quality claim.

  Also use project-side patterns such as `C.11`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, and `A.21` when decision, evidence, gate, assurance, engineering-justification, work, or reliance claims become primary.
- **Boundary consequence:** when the publication unit can no longer be interpreted within the scope of this pattern, apply the neighboring FPF pattern and name the exact project object or record when one is needed. Publication-unit stability does not govern explanation, comparison, decision, gate, work, or reliance in general.

### E.17.AUD:End
