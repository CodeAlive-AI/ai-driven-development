## E.17.AUD - PublicationUnit Stability Discipline - keep one publication unit stable enough to read honestly

**Plain name.** Keep one publication unit stable enough to read honestly.

### E.17.AUD:1 - Problem frame

Use this pattern when people still read one note, memo, sheet, table, screen, or short section as one stable unit even though it has quietly changed what it is mainly about, the publication move it makes, or the boundary between that move and a decision, gate, work, or reliance claim.

A typical case starts with one bounded architecture or status question and ends by sounding like rollout, approval, assignment, or assurance. One reviewer wants to repair a vague word, another wants to rewrite the whole unit, and a third sees a comparison or explanation problem. Before they patch different defects, identify the bounded publication unit and its current interpretation.

Name the unit's primary subject. When it carries or exposes a claim-bearing `U.Episteme` or episteme-side `U.View`, use that item's `EntityOfConcern` value only when it is also the unit's primary subject. Otherwise name the ordinary topic or subject and do not invent an `EntityOfConcernRef`. Keep the publication unit distinct from the episteme, publication occurrence, form, face, carrier, and any downstream project claim.

The primary reader is an author or reviewer who needs one usable repair choice. Architects, managers, and program leads are secondary readers when the same unit is being over-read as architecture, approval, or work guidance.

If this check is missed, teams repair one word when the whole interpretation has shifted, rebuild a whole unit when one local head was enough, or polish a comparison, explanation, or status note until it looks like evidence or approval. The check buys one early choice: keep the unit as it is, repair one local head, stabilize the whole unit, treat it as a bounded comparison, or leave this pattern for the applicable neighboring pattern and project record.

Do not use this pattern when one overloaded local head is the only defect; when the stable unit already presents a bounded comparison; when the live issue is explanation use; or when the text is already being used to approve, direct, assign, adjudicate, or support reliance. Apply `E.17.AUD.LHR`, `E.17.ID.CR`, `E.17.EFP`, or the applicable decision, gate, work, evidence, or reliance pattern instead.

The first useful result is one of those five repair choices. If the unit, its primary subject, its publication move, and its outside boundary are already clear enough for the current reader, return `stable for current use` and stop. The checks and examples below are aids, not a mandatory engineering sequence.

### E.17.AUD:2 - Problem

Without a named publication-unit stability discipline:
1. teams repair local wording when the real defect is whole-unit interpretation instability;
2. teams open whole-unit stabilization when the real defect is still one overloaded local lexical head;
3. teams keep thickening a publication-unit repair when the active problem situation is already bounded comparison;
4. teams mistake note, sheet, table, or screen labels for different kinds of publication unit when they name different presentation forms of one unit;
5. teams infer an engineering-process, approval, or rollout claim or effect that the text does not support.

### E.17.AUD:3 - Forces

| Force | Tension |
| --- | --- |
| **Recognisability vs precision** | Cold readers need an early recognizable situation, but the unit still needs explicit primary-subject, carried-publication-move, and outside-work discipline. |
| **Local repair vs whole-unit stabilization** | It is cheaper to fix one overloaded local lexical head, but sometimes the whole publication unit already carries a quiet shift in primary subject, carried publication move, or outside boundary to work, work planning, decision, gate, or reliance claim. |
| **Stability vs an honest next-pattern boundary** | Teams want to keep one unit usable, but they also need to admit when the live question is now comparison, explanation, or a downstream claim or effect. |
| **Form variety vs publication-unit fidelity** | Note, memo, sheet, table, and screen are convenient ordinary labels, but they must not silently replace the publication unit under review. |
| **Readability vs downstream claim or effect laundering** | Clearer or more polished prose helps readers, but it does not by itself mint approval, policy, gate, work, or reliance claim or effect. |

### E.17.AUD:4 - Solution

> Stabilize the interpretation of one publication unit before editing it at the wrong level.
>
> Name what the unit is mainly about, the publication move it carries, the claim that remains outside, and one repair choice. Apply another pattern only when that choice requires it.

#### E.17.AUD:4.0 - Plain working terms

- `publication unit under review` = one note, memo, sheet, table, screen, or short section that readers inspect as one unit;
- `primary subject` = what the unit is mainly about; `publicationUnitPrimaryEntityOfConcern` names the primary `EntityOfConcern` of the claim-bearing episteme or episteme-side view carried by the unit; when none is live, use the non-claim-bearing kind named by value or an ordinary topic or subject without inventing an `EntityOfConcernRef`. An ordinary topic or subject value is not a claim about a C.2.1 entity participant;
- `carried publication move` = the claim, interpretation, comparison, or explanation move the unit makes about that primary subject;
- `outside boundary` = the decision, gate, `U.Work`, work planning, reliance claim, or continuing engineering work that the unit does not itself carry;
- `local lexical head` = one word or phrase such as `review`, `interpretation`, `note`, or `text` whose meaning is unstable inside an otherwise stable unit;
- `repair choice` = stable for current use, local-head repair, whole-unit stabilization, bounded comparison, or leave publication-unit stability for explanation classification, bridge or hypothesis work, representation change, controlled coarsening, a changed primary EntityOfConcern, or a downstream action, authority, adjudication, decision, gate, work, or reliance claim;
- `applicable pattern and project reference` = the FPF pattern to apply plus, when the live claim needs it, the exact evidence, gate, decision, work-plan, work-occurrence, method, action-invitation, or relation record, selected `U.Episteme`, or exact `EpistemePublicationRelation` occurrence when availability matters;
- `publication-unit stability family` = `E.17.AUD`, `E.17.AUD.LHR`, and `E.17.AUD.OOTD` together with their comparison and explanation neighbors, grouped here for selecting the applicable repair;
- `presentation-form label` = `note`, `memo`, `sheet`, `table`, `screen`, or a similar clue about form, not a self-authenticating unit kind.

Use the terms above only when their distinctions change the repair choice.

#### E.17.AUD:4.1 - Minimum admissible interpretation

A locally admissible interpretation keeps four entries visible enough to inspect by value:
- one publication unit under review;
- one primary subject;
- one carried publication move over that primary subject;
- one outside boundary to work, work planning, decision, gate, or reliance claim, with one light boundary type when that distinction matters: neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation.

If the publication unit changes any of those four without saying so, its interpretation has already shifted even when the sentences still look polished.

#### E.17.AUD:4.2 - Publication-unit stability vs whole-unit requirement
**Light ordinary output.** The ordinary output is one repair choice, not a dossier:
- `stable for current use`: the four-part interpretation is explicit enough and none of the neighboring questions named above is live;
- `local lexical-head repair`: apply `E.17.AUD.LHR` to the overloaded head;
- `whole-unit stabilization`: apply `E.17.AUD.OOTD` to the unit;
- `bounded comparison`: if the unit is stable, apply `E.17.ID.CR`;
- `leave publication-unit stability`: the live question concerns work, work planning, decision, gate, evidence, explanation, reliance, carrier or front-end work, or another claim that this pattern does not test; apply the relevant pattern and name the exact project object or record.

After choosing the repair, apply `E.17.AUD.LHR` for one local head, `E.17.AUD.OOTD` for whole-unit stabilization, `E.17.ID.CR` for bounded comparison, or the specific neighboring pattern and project record needed by a claim outside publication-unit stability.

Do not repeat or replace the narrower whole-unit check in `PublicationUnit Primary-Subject Discipline`: can this one unit still keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim?

#### E.17.AUD:4.3 - Inherited dynamic frame

Use the lineage and move frame already defined by `C.2.2a` or `A.16.0`. Here, inspect how one publication unit speaks about that lineage or publication move. This is not a standalone theory of documents, carriers, or publication forms.

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

**Publication-unit boundary choice.** A `PublicationUnit` boundary is valid when a careful reader would naturally inspect that bounded item as carrying one primary publication move over one primary subject, with one visible outside boundary to work, work planning, decision, gate, reliance claim, or neighboring pattern application. Choose the bounded item that carries the claim being made or effect being repaired. Do not choose a smaller boundary merely to hide a downstream overclaim, and do not choose a larger boundary merely to absorb several primary subjects into one unit. A table row may be the unit when that row carries the claim; the whole table may be the unit when the table-level caption or comparison frame carries the claim. A dashboard tile, note, card, sheet, or screen block may be the unit only when that bounded item, not the whole carrier or interface, carries the live publication move.

**Publication-unit snapshot identity.** A `PublicationUnit` may remain the same bounded unit while its carrier rendering, export format, screenshot, or layout changes. It does not remain the same stabilized interpretation by visual or file continuity alone. If a revision, refresh, translation, regeneration, or dashboard update changes the primary subject, carried publication move, outside boundary, source pins, or admissible use, rerun the four-part interpretation for the new snapshot before the unit is used for comparison, explanation, evidence, gate, decision, work, or reliance claims.

#### E.17.AUD:4.5 - Ordinary working card

Use this seven-row card before you widen the repair:

| Row | Ordinary prompt |
| --- | --- |
| 1 | What is the publication unit under review being kept honest here? |
| 2 | What is that unit mainly about right now? |
| 3 | What carried publication move is it making over that primary subject right now? |
| 4 | What downstream `U.Work`, work planning, decision, gate, or reliance claim still remains outside this unit, and is that boundary mainly a neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation? |
| 5 | Is the active problem situation still one overloaded local lexical head, whole-unit primary-subject stabilization, bounded comparison, or another neighboring pattern altogether? |
| 6 | Is the current form label (`note`, `sheet`, `table`, `screen`, and similar ordinary labels) naming only the presentation form, or is it quietly being used as if it changed the publication unit under review or the kind of downstream claim or effect readers are now inferring? |
| 7 | Does the current interpretation depend on a modeling substrate or rationale to identify the primary subject or carried publication move, and if so has that substrate or rationale been published honestly enough for this unit? |

#### E.17.AUD:4.6 - Choose the next pattern

- If row 5 still points to one overloaded local lexical head, apply `Local Head Restoration`.
- If row 5 shows that the whole publication unit still cannot keep one stable primary subject, one carried publication move, and one outside boundary to work, work planning, decision, gate, or reliance claim visible, apply `PublicationUnit Primary-Subject Discipline`.
- If the publication unit is already stable enough and the real move is bounded comparison over already available source publications, apply `E.17.ID.CR ComparativeReviewUnit`.
- If the main problem situation is explanation classification over an existing face, apply the neighboring explanation pattern rather than keeping the case inside publication-unit stability by inertia.
- If claim content, representation, coarsening, or the primary EntityOfConcern changes, apply the relevant `A.6.3` or `A.6.4` pattern before checking a later publication form here.
- If the active problem situation is publication form, bridge or hypothesis work, or a downstream claim or effect, leave the publication-unit stability family, apply the relevant pattern, and name the exact project object or record when one is needed.

#### E.17.AUD:4.7 - Local naming rule

Treat ordinary labels such as `note`, `memo`, `sheet`, `table`, `screen`, `review`, and `status` as presentation-form clues, not as self-authenticating unit kinds.

Working rule:
- if one overloaded local lexical head is doing most of the semantic work, repair that local lexical head first through `Local Head Restoration`;
- if the local lexical head is not the real issue, keep the publication unit stable in the whole-unit stabilization pattern instead of hiding the interpretation shift under one more qualifier;
- do not let cleaner or more formal wording stand in for non-admissible downstream claim or effect or non-admissible comparison source relation.

#### E.17.AUD:4.8 - Keep a needed model or rationale visible

If the primary subject or the carried publication move depends on a modeling substrate or rationale, publish that substrate or rationale briefly in the unit or move the case to a heavier publication form or neighboring pattern that can carry it honestly. Do not let a formally loaded case pretend it is only prose hygiene.

#### E.17.AUD:4.9 - Keep stronger claims separate

When explanation, comparison, or a downstream claim is load-bearing, keep five facts visible enough to preserve the repair choice:
- evidence status and source-pin status when the unit leans on already available source publications;
- current admissible reliance or work interpretation and forbidden non-admissible decision, work, or gate claim;
- whether this unit is the primary publication unit or a derivative helper publication;
- any claim-bearing modeling substrate or rationale;
- and that the assurance section only tightens the opening recognition claim rather than silently broadening it into downstream claim or effect.

### E.17.AUD:5 - Worked slices

#### E.17.AUD:5.1 - Local-head case

A semio note keeps saying `this review` and `this interpretation`, but nobody can tell which FPF kind or locally declared head those lexical heads name here. The rest of the publication unit under review is still locally stable once the local lexical head is repaired. The honest move is not broad publication-unit stabilization. It is `Local Head Restoration`.

#### E.17.AUD:5.2 - Whole-unit interpretation-shift case

A memo starts about one bounded architecture question over an inherited lineage or move, then shifts into wider rollout or approval language without declaring the transition. Repairing one sentence does not stabilize the publication unit under review because its concern and carried publication move have widened; that does not by itself establish a changed EntityOfConcern. The honest move is `PublicationUnit Primary-Subject Discipline`.

#### E.17.AUD:5.3 - Stable-unit comparison case

A comparison sheet already keeps one stable primary subject and one clear outside boundary to work, work planning, decision, gate, or reliance claim, but the team is using publication-unit instability language because the comparison is contentious. The honest move is not more publication-unit stabilization. It is `E.17.ID.CR ComparativeReviewUnit`.

#### E.17.AUD:5.4 - Explanation-laundering case

An onboarding explainer starts from one stable source-pinned note, but then the simplified prose begins to sound like canonical assurance or policy. The publication unit may still be readable, yet the main problem situation is no longer publication-unit stability. Leave publication-unit stability and use `E.17.EFP`'s simpler source-linked boundary sentence first; instantiate `ExplanationFaithfulnessProfile` only when explanation-class ambiguity still changes the next action.

#### E.17.AUD:5.5 - Downstream decision and reliance case

A status card starts as one bounded summary of progress, then quietly becomes the place where people infer approval, assignment, or go or no-go claim or effect. The problem is no longer only publication-unit stability. The honest move is to stop treating the card as if it were still only one neutral note and use the downstream decision, gate, work, or reliance publication.

#### E.17.AUD:5.6 - Quick contrasting cases

Use this quick contrast set when the first interpretation is still foggy:

| Near-miss case | What to look for | Honest next pattern or project reference |
| --- | --- | --- |
| `LHR-only` | one overloaded local lexical head is doing most of the semantic work while the publication unit under review otherwise stays stable | apply `Local Head Restoration` |
| `whole-unit interpretation shift` | the publication unit under review quietly changes primary subject or carried publication move | apply `PublicationUnit Primary-Subject Discipline` |
| `stable comparison -> CR` | the unit is already stable and the live problem situation is bounded comparison over pinned source publications | apply `E.17.ID.CR ComparativeReviewUnit` |
| `downstream claim or effect overread` | readers are inferring approval, assignment, or go or no-go claim or effect from the publication unit | leave the publication-unit stability family for the more honest downstream decision, gate, work, or reliance publication |
| `modeling-lens hidden` | the unit only makes sense because of one unpublished model, formal substrate, or rationale | publish that substrate or rationale briefly or use a heavier publication form or neighboring pattern |

### E.17.AUD:6 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | How to avoid it |
| --- | --- | --- |
| Fixing one sentence while the whole unit already carries a quiet interpretation shift | local repair is asked to carry whole-unit stabilization | check primary subject, carried publication move, and outside boundary to work, work planning, decision, gate, or reliance claim before repairing the sentence |
| Treating form labels as if they changed the publication unit under review | `table`, `sheet`, or `screen` is used as if it already named a different ontology or downstream claim or effect | treat those as presentation forms first; only leave this pattern when the problem situation itself changes |
| Laundering comparison through stability language | teams keep saying the unit is unstable when the active problem situation is already bounded comparison | apply `E.17.ID.CR ComparativeReviewUnit` and name the exact source publications |
| Laundering downstream decision or reliance through clearer prose | a better-written note is over-read as if it had become an approval, gate, work, or reliance text | keep the outside boundary to work, work planning, decision, gate, or reliance claim explicit and leave this pattern when downstream claim or effect appears |
| Letting three repair choices act at once | lexical-head repair, whole-unit stabilization, and a neighboring-pattern application are patched in parallel with no shared primary-subject interpretation | use the working card first and name one current repair choice before patching the unit |

### E.17.AUD:7 - Consequences

- You slow down long enough to name the active publication-unit problem situation before patching the draft.
- You reduce pointless escalation from one overloaded local lexical head into a whole-unit rewrite.
- You reduce the opposite failure too: trying to solve whole-unit interpretation instability with one more qualifier on the same local lexical head.
- You keep neighboring publication-unit repair patterns and neighboring non-publication-unit patterns explicit instead of letting one broad stability name quietly absorb them.
- You make it harder for clearer prose, official-looking formatting, or wider circulation to masquerade as downstream claim or effect.

### E.17.AUD:8 - Rationale

`PublicationUnit Stability Discipline` is worth stating explicitly because local lexical-head repair and whole-unit primary-subject stabilization are both already real problem situations, but authors and reviewers still need one stabilization check that says when the case is local, when it is whole-unit, when it is already bounded comparison, and when it has left the publication-unit stability family entirely.

The pattern stays intentionally narrow. It does not turn every publication-unit problem into publication design or downstream decision, gate, work, or reliance work. Its job is to keep one publication unit honest enough that readers can still tell what it is mainly about, which carried publication move it makes, and which downstream `U.Work`, work planning, decision, gate, or reliance claim remains outside.

### E.17.AUD:9 - SoTA-Echoing

**Claim 1.** FPF's current EntityOfConcern and description apparatus keeps the entity of concern distinct from the claim-bearing episteme or publication that describes it. This supplies the exact-entity case of the publication-unit subject distinction.

**Practice, source, alignment, and adoption.** `C.2.1`, `A.7`, `E.17`, and the description patterns keep an EntityOfConcern, a description episteme, its publication occurrence, form, and carrier distinct. ISO/IEC/IEEE 42010:2022 is standards lineage for the narrower architecture/architecture-description distinction, not the source of this general publication-unit ontology. `PublicationUnit Stability Discipline` adapts the current FPF distinction to one readable unit and requires a primary-subject shift to be explicit; an EntityOfConcern change requires the exact C.2.1 case. For a reviewer or architect, this is the practical guard behind worked slices 5.2 and 5.3.

**Claim 2.** Best-known current information-for-use practice treats user-facing units as purpose-bound, structured information rather than as loose bundles that can mix explanation, instruction, warning, and decision or reliance effect by convenience.

**Practice, source, alignment, and adoption.** Joint IEC and IEEE 82079-1:2019 requires information for use to be purpose-directed, structured, and evaluated for usability. `PublicationUnit Stability Discipline` adopts purpose-bound publication units and explicit outside boundaries to work, work planning, decision, gate, or reliance claim, adapts that discipline from information-for-use to notes, memos, sheets, tables, and screens, and rejects the shortcut where a clearer or official-looking unit is treated as if it had already become approval, policy, gate, work, or reliance text. For a manager or operator, this is the practical guard behind worked slices 5.4 and 5.5: better explanatory form does not itself mint downstream claim or effect.

**Claim 3.** Best-known current pattern-writing and pattern-validation practice keeps patterns tied to recognisable situations, explicit problem, solution, and consequence structure, and reviewable rationale rather than elegant internal naming alone.

**Practice, source, alignment, and adoption.** Iba (2021), [How to Write Patterns](https://hillside.net/plop/2021/plopourri/PLoP21_PLOPOURRI_Iba_Methodology4.pdf), and Riehle, Harutyunyan, and Barcomb (2025), [Pattern Discovery and Validation Using Scientific Research Methods](https://doi.org/10.1007/978-3-662-70810-1_6), with the [authors' 2021 preprint](https://arxiv.org/abs/2107.06065), treat pattern writing and validation as requiring recognisable situations, explicit structure, and reviewable reasoning rather than only elegant naming. `PublicationUnit Stability Discipline` adopts worked slices, recognisable entry cues, and an explicit next-pattern and project-reference boundary, adapts those expectations to publication-unit stability work, and rejects a pattern text that is cleanly labeled but domain-thin or reader-thin. For the current working reader, this is the practical guard behind the Problem frame and slices 5.1 through 5.5: the pattern should be usable before one has to reconstruct the surrounding rationale from scratch.

**Local stance.** The current SoTA claim is narrow. This pattern is not claiming one universal theory of documents. It claims a smaller and more practical point: one publication unit stays trustworthy only when its primary subject, carried publication move, and outside boundary to work, work planning, decision, gate, or reliance claim remain explicit enough for cold readers to recover, and when practitioners apply the specific neighboring pattern needed by a different problem.

### E.17.AUD:10 - Conformance Checklist

1. **CC-AUD-1 — One publication unit under review is explicit.**
   The case names one note, memo, sheet, table, screen, or short section as the publication unit under review rather than letting presentation-form labels stand in for the publication unit under review.
2. **CC-AUD-2 - Primary subject and carried publication move are explicit enough to identify the applicable pattern.**
   The case keeps visible which primary subject the unit is about and which carried publication move it performs over that primary subject right now.
3. **CC-AUD-3 — Outside-work boundary is explicit.**
   The case states what downstream `U.Work`, work planning, decision, gate, or reliance claim still remains outside the publication unit under review, including neighboring pattern application, downstream claim or effect, or ongoing engineering-process continuation when that distinction matters.
4. **CC-AUD-4 — The active repair choice is named honestly.**
   The case returns `stable for current use` when the unit, primary subject, carried publication move, and outside boundary already suffice. Otherwise it names local lexical-head repair, whole-unit primary-subject stabilization, bounded comparison, or the applicable neighboring pattern rather than patching several problem situations at once.
5. **CC-AUD-5 - The next pattern and project-reference boundary is explicit.**
   When the problem calls for `Local Head Restoration`, `PublicationUnit Primary-Subject Discipline`, `E.17.ID.CR ComparativeReviewUnit`, an explanation-faithfulness pattern, or a downstream decision, gate, work, or reliance pattern, name the pattern to apply and the exact project object or record when one is needed.
6. **CC-AUD-6 — Presentation-form labels do not launder publication-unit kind or downstream claim or effect.**
   `note`, `memo`, `sheet`, `table`, `screen`, and similar labels remain presentation-form clues and do not silently change the publication unit under review, create proof, create evidence, create release admissibility, or mint downstream claim or effect.
7. **CC-AUD-7 - A claim-bearing modeling substrate or rationale remains visible.**
   If the primary subject or carried publication move depends on a modeling substrate or rationale, publish that substrate or rationale briefly enough for review or handle the case by a heavier publication form or neighboring pattern that can carry it honestly.
8. **CC-AUD-8 — Clearer prose does not silently widen downstream claim or effect.**
   Readability, formatting, and wider circulation may improve the unit, but they do not by themselves turn the unit into approval, policy, assignment, gate, work, or reliance text.

### E.17.AUD:11 - Relations

- **Builds on:** `A.7`, `E.10`, `F.18`, `E.14`, `E.19`, `E.17`, and `C.2.1`.
- **Coordinates with:** `E.17.AUD.LHR Local Head Restoration`, `E.17.AUD.OOTD PublicationUnit Primary-Subject Discipline`, `E.17.ID.CR ComparativeReviewUnit`, `E.17.EFP ExplanationFaithfulnessProfile`, and `E.21` when a pattern-quality card, table, status line, or generated summary is published as a bounded publication unit. Use `E.17.AUD` to test publication-unit honesty and `E.21` to evaluate the underlying pattern-quality claim. Also use project-side patterns such as `C.11`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, and `A.21` when decision, evidence, gate, assurance, engineering-justification, work, or reliance claims become primary.
- **Boundary consequence:** when the publication unit can no longer stay honest inside this pattern, apply the neighboring FPF pattern and name the exact project object or record when one is needed instead of treating publication-unit stability as a general explanation, comparison, decision, gate, work, or reliance discipline.

### E.17.AUD:End
