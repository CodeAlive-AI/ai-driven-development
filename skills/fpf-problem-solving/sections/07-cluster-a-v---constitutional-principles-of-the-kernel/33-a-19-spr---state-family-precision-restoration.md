## A.19.SPR - State-Family Precision Restoration

> **Type:** State-family precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** State-wording repair.

### A.19.SPR:0 - Use this when

Use this pattern when a phrase such as “the system is ready”, “the source is current”, or “the evidence status is incomplete” matters to an FPF claim but does not yet say which item the sentence is about, what is true of it, or which rule makes that statement meaningful.

**What goes wrong if missed.** A short status word starts carrying several claims at once. A source label becomes evidence, a readiness label becomes gate passage, or a project-side status leaks into pattern guidance.

**First question.** Ask:

> What exact item is this sentence about, what does it say about that item, and which rule or criterion gives the statement its meaning?

**Cheap direct repair.** Write the answer as one ordinary technical sentence. Name the item, the actual value, relation, result, or claim, and the rule or criterion only when the reader needs it to understand or act. If that sentence is clear and safe for the intended use, stop. Do not create a repair note or list every claim the sentence does not make.

**What this buys.** A reader can understand the statement and its next practical use without learning a hidden status vocabulary.

Typical triggers include `state`, `status`, `posture`, `stance`, `currentness`, `validity`, `stable`, `accepted`, `blocked`, `candidate`, `degraded`, `readiness`, `ready`, and similar compounds. A precise-looking field such as `LensUseAdmissibilityValue` or `dynClaimPosture` is also a trigger when its object, possible values, or rule cannot be recovered.

**Not this pattern when.**

- If the exact item, claim or value, and applicable rule are already clear, use that rule directly.
- If `readiness` or `ready` still hides whether the sentence concerns a subject state, assignment condition, work entry, gate decision, publication use, permission, or performed Work, use `E.10.MOVE` first.
- If the wording is ordinary prose and carries no FPF-governed claim, keep it ordinary.
- If one `Characteristic`, Scale, Coordinate, score, or measurement construction is hidden, use `C.16.P` first.
- If a source expression, publication, carrier, or source-use relation is hidden, use `C.2.P` first and return here only if a state-wording problem remains.
- For relation, architecture, quality, function, or naming problems, use `A.6.P`, `C.30.P`, `C.16.Q`, `A.6.F`, or `F.18` as selected by `E.10`.

### A.19.SPR:1 - Problem frame

FPF needs compact state words. Engineers reasonably say that a pump is stable, a source is current, an evidence path is incomplete, an assurance claim has expired, or an intended performance is ready for work entry.

The words work when the reader can recover the item, the actual claim or value, and the rule behind it. Trouble begins when the word replaces those facts. “Ready” may mean a patient condition, an assignment satisfying a condition, an A.15.5 work-entry result, an A.21 gate decision, or merely a green display. Those are different claims.

A repaired sentence may therefore name an ordinary domain condition, an obtaining relation, an assertion episteme, an evaluation result, a decision result, or a project-side record field. It introduces a predicate only when the rule for that claim defines or needs one.

### A.19.SPR:2 - Problem

How can FPF keep useful words such as `state`, `status`, and `ready` without:

- creating one general `Posture` or readiness kind;
- replacing one broad status word with another;
- treating every state statement as a `CharacteristicSpace` position or predicate;
- merging source use, evidence, assurance, publication, assignment state, work entry, gate decisions, performed Work, and project records;
- copying the same wording-repair procedure into every pattern; or
- deleting a useful local finite field whose object, values, rule, and practical use are already clear?

### A.19.SPR:3 - Forces

| Need | Tension |
| --- | --- |
| Short working language | Practitioners need compact sentences, but a consequential claim must still identify what is being judged. |
| Local fields | A finite field can be useful; a vague status field can hide several unrelated claims. |
| Direct patterns | A.19 covers characteristic spaces, while evidence, assurance, publication, assignment state, readiness, gates, and project records keep their own rules. |
| Small repair | Most cases need one rewritten sentence, while replayed or high-consequence cases may need a few additional fields. |

### A.19.SPR:4 - Solution

Start with the direct sentence:

1. name the exact item;
2. say what value, relation, result, or claim is current; and
3. name the rule or criterion when the sentence is not understandable or usable without it.

Stop there when the intended reader can act safely. Add evidence, time, allowed-use, or blocked-inference detail only when that detail changes the receiving action or prevents a likely harmful conclusion.

Use a `StateFamilyPrecisionRepair` note only when another person or tool must replay the repair, or when the claim has enough consequence that its extra basis must remain inspectable:

```text
StateFamilyPrecisionRepair:
  triggerSpan:
  finalSentence:
  recoveredObjectRef?:
  recoveredClaimValueRelationOrResult?:
  definingOrTestingPatternLocator?:
  predicateRef?:
  criteriaOrEvidenceRef?:
  allowedUse?:
  blockedInference?:
  checkAgainWhen?:
```

The optional fields are triggered separately:

| Add this field | Only when... |
| --- | --- |
| `predicateRef` | the direct pattern defines or needs a reusable predicate. |
| `criteriaOrEvidenceRef` | a receiving decision relies on the criterion or evidence identity. |
| `allowedUse` | the same value could drive materially different actions. |
| `blockedInference` | a likely adjacent inference would be harmful, such as treating readiness as gate passage. |
| `checkAgainWhen` | the value can expire or change during the intended use. |
| exact references and machine fields | automation, audit, comparison, or later replay needs those identities. |

A direct relation, classification, assertion episteme, evaluation result, decision result, or record field keeps its own form. The repair note does not turn it into a new state predicate or result kind.

#### A.19.SPR:4.1 - Direct repair

For ordinary prose, inspect only the current sentence:

1. **Find the item.** For system-role wording, distinguish an exact local system-role kind, an obtaining assignment, its state condition, the world-side assignment-state relation, and an assertion about either. Do not stop at bare `role`.
2. **Write the claim.** Say that the item has a value, that a relation obtains, that an assertion or result says something, or that a project record has a field value.
3. **Use the direct rule.** Cite the applicable pattern when its criterion or distinction matters. If the direct rule already settles the sentence, A.19.SPR has finished its job.

Add a time boundary, evidence basis, allowed use, or blocked inference only under the triggers above. If the item or claim still cannot be recovered, keep the wording as a quotation or navigation cue, narrow its use, or state the exact blocker.

##### A.19.SPR:4.1.1 - Assignment-state exits

| Recovered claim | Direct exit |
| --- | --- |
| One exact system-role assignment or its holder, with no state condition claimed | `A.2.1`; the assignment itself is not readiness. |
| A reusable condition for assignments to one exact local system-role kind | A.2.5 `SystemRoleAssignmentStatePredicate`, by value. |
| One exact assignment satisfies that condition during the relevant interval | The world-side A.2.5 `SystemRoleAssignmentStateRelation` occurrence. |
| An affirmative or negative claim about the assignment or an established relation occurrence | A.2.5 `SystemRoleAssignmentStateAssertion : U.Episteme`; the assertion is not its EntityOfConcern. |
| Evidence, currentness, reliance, or an evaluation concerning that assertion episteme | `A.2.4`, `A.10`, or the direct evaluation pattern. Keep the assertion episteme distinct from the assignment and world-side relation. |
| Whether intended Work may enter now | `A.15.5` or the direct receiving pattern. A.2.5 may supply an assignment-state input; it does not publish the admission result, gate decision, or Work occurrence. |

##### A.19.SPR:4.1.2 - Readiness exits

When `readiness` or `ready` still hides which governed value is meant, use `E.10.MOVE` first. Once the claim is recovered, leave the wording repair through exactly one direct exit:

| Recovered readiness-like claim | Direct exit |
| --- | --- |
| A subject such as a patient or system has a value in a still-hidden state frame | `A.19.SPR`, followed by the subject pattern that defines or tests that value. |
| An assignment satisfies an assignment-state condition | `A.2.5`. |
| One intended performance satisfies a work-entry criterion | `A.15.5` work-entry readiness result. |
| A distinct `OperationalGate(profile)` consumes declared checks and publishes a decision | `A.21`; a ready label alone is not gate passage. |
| A publication use, permission claim, or dated performed Work is meant | `E.17`, the direct permission pattern, or `A.15.1`, respectively. Readiness wording establishes none of them. |

#### A.19.SPR:4.2 - Where the repaired claim belongs

| What the sentence means | Use this pattern or record |
| --- | --- |
| position in a declared `CharacteristicSpace` | `A.19`, with `A.17`, `A.18`, `C.16`, and `C.16.P` when construction is hidden |
| reusable transition law, trajectory, or dynamics model | `A.3.3` |
| exact system-role assignment with no state condition claimed | `A.2.1`; do not treat assignment as readiness |
| by-value assignment-state condition, obtaining assignment-state relation, or assertion episteme about either | `A.2.5`, keeping `SystemRoleAssignmentStatePredicate`, `SystemRoleAssignmentStateRelation`, and `SystemRoleAssignmentStateAssertion` distinct |
| evidence, currentness, reliance, or evaluation concerning an assignment-state assertion | `A.2.4`, `A.10`, or the direct evaluation pattern; the assertion episteme does not become its subject |
| work-entry use of an assignment-state claim | `A.15.5` or the direct receiving pattern; A.2.5 supplies only the exact assignment-state input |
| language-state position for episteme or publication wording | `C.2.2a` and `A.16.*` after `C.2.P` when source-publication recovery is needed |
| source use, source currentness, source publication, or source-use disposition | `C.2.P`, `E.17`, `E.9.DA`, or source-use field named by value |
| evidence path state, evidence relation, or reliance disposition | `A.10` |
| assurance result, assurance claim, assurance input, or engineering-justification use | `B.3` |
| constraint or local CV | `A.20` or the direct constraint pattern |
| ambiguous `readiness` or `ready` wording | `E.10.MOVE` until the governed value is recovered |
| work-entry readiness | `A.15.5` |
| distinct gate decision | `A.21` only when an `OperationalGate(profile)` consumes declared checks and publishes that decision |
| release or permission claim | the direct release or permission pattern; a readiness value establishes neither |
| publication use, publication face, form, or unit value, source-finding use | `E.17`, `E.17.0`, `E.17.AUD`, or publication pattern governing the claim |
| Description episteme admitted for specification use or specification refinement | `A.7`, plus the specification-granting neighbouring pattern named by value: `A.6.2`, `C.2.3`, `A.21`, `C.16`, `E.17`, `E.10`, or another named pattern |
| temporal claim status or temporal-use classification | `C.27`, retaining `dynClaimPosture` only as a declared C.27 field |
| mathematical-lens use admissibility | `C.29`, retaining `LensUseAdmissibilityValue` only as a declared C.29 field |
| `DRR` decision-adequacy result or source-use classification | `E.9.DA` |
| pattern-quality result or pattern-quality review status | `E.21`, with `E.19` only as review or admission profile |
| administrative, review, dispatch, release or admission, or source-control state | the project-side administrative, review, dispatch, release or admission, or source-control record; not pattern prose unless the pattern's own `EntityOfConcern` is that record |

#### A.19.SPR:4.3 - Keeping a technical state field

A technical field such as `...Status`, `...Readiness`, or `...State` may stay when the text makes three things clear: what item the field describes, which values it can take, and which rule or criterion gives those values meaning.

Add an allowed-use boundary only when the field changes a receiving action. Add a blocked inference only when a likely misreading would be harmful. Add a validity window or recheck condition only when the value can change during the intended use. Machine-readable identifiers belong only to automation, audit, comparison, or replay that consumes them.

If the three basic facts are missing, complete them or replace the field with the ordinary sentence the reader actually needs. A narrowing adjective alone does not recover the claim.

### A.19.SPR:5 - Worked examples

Each example starts with the smallest useful final wording. The second paragraph adds detail only for a machine-readable, replayed, or high-consequence use.

#### A.19.SPR:5.1 - Physical-system state

**Before:** “Pump 37 is in a good operating state.”

**After:** “Pump 37 satisfies `InspectionOperatingCondition`: its coolant temperature is 72 °C, within the 60–80 °C band, and its discharge pressure is 315 kPa, above the 300 kPa minimum.”

For a relied-on inspection decision, also name the reading time, measurement basis, condition edition, and the event that requires another check. Do not add those fields to a casual status sentence that no decision consumes.

#### A.19.SPR:5.2 - Work-entry readiness is not gate passage

**Before:** “Release 12 is ready.”

**After:** “At 10:00, the A.15.5 check found that `PlanItem-Deploy-12` satisfied its release-entry criterion and was ready for work entry until 10:30; recheck if a required input changes. No A.21 gate decision has yet been made.”

When another use must replay the check, add the exact WorkPlan, criterion, checking Work, input facts, result episteme, and reliance window. Add an A.21 sentence only if a distinct `OperationalGate(profile)` actually consumes declared checks and publishes its own decision.

#### A.19.SPR:5.3 - Source currentness

**Before:** “The source posture is good.”

**After:** “This review uses edition E7 as the accepted decision source. Recheck that use if the edition or the reviewed question changes.”

For automation or consequential reliance, also name the exact source-use relation, currentness result, use window, and the claim that must be reconsidered. The short sentence does not turn the source into evidence, assurance, gate passage, or FPF doctrine.

#### A.19.SPR:5.4 - Other direct repairs

- **Evidence.** Replace “evidence status incomplete” with “The current evidence path does not yet support reliance on claim C; obtain the missing calibration record and check again.” Add exact evidence and currentness references only when the receiving decision needs them.
- **Publication.** Replace “publication posture allows decision input” with “This publication exposes candidate input X for the decision; the decision rule still evaluates X.” Publication does not decide or assure by itself.
- **Mathematical lens.** Keep `LensUseAdmissibilityValue` in C.29 when its possible values and intended lens use are defined. State the practical result in ordinary words; the field does not establish evidence, assurance, release, or source authority.
- **Temporal claim.** Keep `dynClaimPosture` in C.27 when its values and temporal use are defined. Say which temporal claim is usable and for what purpose; the field does not upgrade its evidence or authority.
- **Project-side state.** Put review, dispatch, release, admission, or source-control status in the project record that carries it. A pattern may mention only the user-facing boundary needed for its own subject.

### A.19.SPR:6 - Conformance checks

| Check | Requirement |
| --- | --- |
| `CC-A19SPR-1` | The final sentence names the exact item and what is claimed or valued, or explicitly keeps the wording ordinary, quoted, navigation-only, narrowed, or blocked. |
| `CC-A19SPR-2` | The direct rule or criterion is recoverable whenever the claim is not understandable or usable without it. |
| `CC-A19SPR-3` | A predicate appears only when the direct pattern defines or needs one; relations, assertions, results, decisions, and record fields keep their own forms. |
| `CC-A19SPR-4` | An allowed-use or blocked-inference clause appears only when it changes the receiving action or prevents a likely harmful conclusion. |
| `CC-A19SPR-5` | A time window, expiry rule, or recheck condition appears when the value can change during the intended use. |
| `CC-A19SPR-6` | Source, evidence, assurance, publication, assignment state, work entry, gates, decisions, release or admission, and project records use the patterns or records that define or test those exact claims. |
| `CC-A19SPR-7` | Source and publication patterns are not used as a general home for evidence, assurance, gate, Work, temporal, mathematical-lens, or project status. |
| `CC-A19SPR-8` | A retained technical field names its item, possible values, and rule; it adds use, time, evidence, and blocked-inference fields only under their triggers. |
| `CC-A19SPR-9` | A cold reader can say what the sentence is about, what it claims, and what to do or check next. Type-correct but opaque wording fails. |
| `CC-A19SPR-10` | Corpus repair classifies each use; it never performs a blind global replacement of `posture`, `state`, `status`, or `readiness`. |

### A.19.SPR:7 - Common mistakes

| Mistake | Symptom | Repair |
| --- | --- | --- |
| **Status word as cover** | `posture` or `status` hides a source relation, evidence result, assurance result, gate decision, or release claim. | Say what item has which value or relation under the direct rule. |
| **One broad word replaces another** | `support` becomes `support posture`, `basis posture`, or `source posture`. | Recover the actual source, evidence, assurance, relation, characteristic, or reader-help claim before choosing words. |
| **Technical field without meaning** | A `...Status` or `...Posture` field has no object, possible values, or rule. | Complete those three facts or replace the field with an ordinary sentence. |
| **Project status in pattern prose** | Review, dispatch, landing, release, or source-control state appears as user guidance. | Move it to the project record and keep only the practical boundary the pattern user needs. |
| **Everything becomes a source-language case** | Evidence, assurance, gate, Work, temporal, or lens-use claims are all sent to source or publication repair. | Use the direct pattern for the actual claim. |

### A.19.SPR:8 - Relations

The dependency and distribution detail belongs here, after the working method. A.19.SPR builds on `E.10`, `E.10.ARCH`, `E.10.MOVE`, `A.19`, `A.3.3`, `A.2.5`, `A.15.5`, `C.2.2a`, `A.10`, `B.3`, `A.20`, `A.21`, `C.27`, `C.29`, `E.17`, `E.9.DA`, `E.21`, and `F.18`. It coordinates with `A.17`, `A.18`, `C.16`, `C.16.P`, `C.16.Q`, `A.6.P`, `C.2.P`, `C.30.P`, `E.8`, `E.19`, and `E.11` when those patterns define or test the recovered claim.

| Pattern | Contribution |
| --- | --- |
| `E.10`, `E.10.ARCH` | Recognize the wording problem and keep one shared restoration architecture. |
| `E.10.MOVE` | Resolves ambiguous readiness-like wording before it exits to A.19.SPR or a direct pattern. |
| `A.2.5`, `A.15.5` | Distinguish assignment-state predicate, world-side relation, assertion episteme, and the separate work-entry readiness result. |
| `A.19`, `A.3.3`, `C.16.P` | Define characteristic-space, dynamics, and characteristic or scale claims when those are the actual subject. |
| `C.2.P`, `C.2.2a`, `A.16.*`, `E.17` | Define source, publication, and language-state claims. |
| `A.10`, `B.3` | Define evidence-use and assurance claims. |
| `A.20`, `A.21` | Define constraint or adjudication results and distinct gate decisions. |
| `C.27`, `C.29` | Define temporal-claim and mathematical-lens uses, including their local fields. |
| `E.9.DA`, `E.21`, `E.19` | Define DRR adequacy, pattern-quality results, and review or admission profiles. |
| `F.18`, `F.19` | Settle durable names after the claim is known and rewrite the final practitioner path in plain technical language. |
| `E.11` | Places first-use cues without creating a second routing table. |

### A.19.SPR:9 - Rationale

The problem is not the word `state`. The problem is a sentence that hides what has changed, what is being judged, or which rule makes the judgment meaningful. Recovering those facts first lets FPF keep short engineering language without creating a general status ontology.

Local fields such as `LensUseAdmissibilityValue` and `dynClaimPosture` remain useful when their object, possible values, and rule are clear. Broad phrases such as `source posture`, `evidence posture`, or `release posture` should instead become the direct sentence or project record the reader actually needs.

### A.19.SPR:End

