## A.19.SPR - State-Family Precision Restoration

> **Type:** State-family precision-restoration pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** State-wording repair.

**Intent.**
Recover `state`, `status`, `posture`, `readiness`, and close state-family wording whose bearer, state frame, value set, admissible use, or receiving FPF pattern is hidden.

This pattern does not define a general `Posture` kind. It repairs wording that acts like a state-like claim before a reader treats the word as evidence, assurance, gate passage, release permission, source authority, maturity, or work completion.

**Builds on.** `E.10`, `E.10.ARCH`, `A.19`, `A.3.3`, `C.2.2a`, `A.16.*`, `A.10`, `B.3`, `A.20`, `A.21`, `C.27`, `C.29`, `E.17`, `E.9.DA`, `E.21`, `F.18`, and project-side administrative, review, dispatch, release or admission, or source-control records when the state-like claim is administrative rather than FPF-content-bearing.

**Coordinates with.** `A.17`, `A.18`, `C.16`, `C.16.P`, `C.16.Q`, `A.6.P`, `C.2.P`, `C.30.P`, `E.8`, `E.19`, and `E.11`.

**E.10.ARCH governing-pattern relation.** When `E.10` encounters state-family wording such as `state`, `status`, `posture`, `readiness`, `stance`, `currentness`, `validity`, `stable`, `ready`, `accepted`, `blocked`, `candidate`, or close compounds whose bearer, state frame, value set, admissible use, validity window, reopen condition, or governing pattern is hidden, `E.10.ARCH` assigns the repair to `A.19.SPR` only until those values are recovered or the claim being made belongs to `C.2.P`, `A.10`, `B.3`, `A.20`, `A.21`, `C.27`, `C.29`, `E.9.DA`, `E.21`, `A.6.P`, `A.15`, or the project-side administrative, review, dispatch, release or admission, or source-control record.

### A.19.SPR:0 - Use this when

Use `A.19.SPR` when state-family wording has FPF-governed use but does not yet say what is in which state, according to which state frame or governing pattern, with which value or classification, for which admissible use.

Typical triggers:

- `state`, `status`, `posture`, `readiness`, `stance`, `currentness`, `validity`, `degraded`, `accepted`, `admissible`, `blocked`, `candidate`, `stable`, `ready`, or close compounds;
- local fields such as `source posture`, `evidence posture`, `assurance posture`, `publication posture`, `release posture`, `validation posture`, `readiness posture`, or `support posture`;
- precision-looking local fields such as `LensUseAdmissibilityValue`, `dynClaimPosture`, or a specification-use label when their bearer, value set, governing pattern, use boundary, or reopen condition is not recoverable.

**What goes wrong if missed.** A broad state word becomes a miniature hidden ontology. A source gets called "current", "supporting", or "accepted" without a source-use role. Evidence becomes assurance. A publication face becomes gate passage. A lens-use label becomes empirical truth. An external administrative status leaks into pattern prose. A readiness word implies work may proceed without the threshold, evidence path, gate, or decision record that would carry that claim.

**What this buys.** The reader can recover the state-like claim named by value, the governing pattern, the allowed use, and the blocked adjacent overread before acting on the word.

**First useful move.** Ask: what bearer has which state-like value under which state frame or governing pattern? If that cannot be answered, demote the wording to ordinary prose, quote-only source wording, a reduced-use cue, or a blocker.

**Not this pattern when.**

- If the pattern governing the recovered claim and state-like field are already recoverable by value, use that pattern directly.
- If the wording is ordinary prose and carries no FPF-governed use, keep it ordinary.
- If the state-like claim concerns one `Characteristic`, `Scale`, coordinate, score, or metric, use `C.16.P` before state-family repair.
- If the state-like claim concerns source-expression, publication, carrier, or source-use wording, use `C.2.P` first; return to `A.19.SPR` only if a state-like claim remains.
- If the claim being made is relation construction, architecture or structure wording, quality-term or evaluative characterization, function-like wording, or naming, use `A.6.P`, `C.30.P`, `C.16.Q`, `A.6.F`, or `F.18` as selected by `E.10`.

### A.19.SPR:1 - Problem frame

FPF needs state-like wording. Engineers say that a system is ready, a source is current, an evidence path is incomplete, an assurance claim has decayed, a lens use is admissible, or a pattern is stable. Those compact words are useful when the state frame is declared.

The defect appears when the word substitutes for the frame. `Posture` is the current visible symptom, but the same failure appears with `state`, `status`, `readiness`, `stance`, `currentness`, and similar words. The repair question is:

> What state-like predicate is being asserted over which bearer, under which FPF pattern, for which use, and with which blocked overread?

The state-like bearer under repair may be a holon in a `CharacteristicSpace`, a role-state assertion, a language-state position, a source-use relation, an evidence path, an assurance claim, a publication use, a gate or constraint record, a temporal claim, a mathematical-lens use, a `DRR` decision-adequacy result, a pattern-quality result, or a project-side administrative, review, dispatch, release or admission, or source-control record. Those are not one kind. They only share the need for a state-like predicate named by value.

### A.19.SPR:2 - Problem

How can FPF repair state-family wording without:

- defining a general `Posture` kind;
- replacing one broad word with another broad word such as `basis`, `support`, `state`, or `status`;
- treating every state-like word as a `CharacteristicSpace` position;
- treating publication, source, evidence, assurance, gate, decision, work, release or admission, and administrative states as one source, publication, or language-state case;
- duplicating the state-family recovery algorithm inside every governing pattern;
- demoting finite local fields such as `LensUseAdmissibilityValue` or `dynClaimPosture` when they are already well-formed, or erasing a real specification use or refinement gate that names its neighboring pattern governing the claim and value set.

### A.19.SPR:3 - Forces

| Force | Tension |
| --- | --- |
| Compact state words vs bearer named by value | Working prose needs short state words, but FPF claims need the bearer named. |
| Local finite fields vs hidden ontology | Some pattern-local state fields are useful; others hide source, evidence, assurance, gate, release or admission, or administrative claims. |
| A.19 state-space core vs many governing patterns | `A.19` gives `CharacteristicSpace`, but many state-like claims belong to evidence, assurance, publication, temporal, lens-use, or project-side administrative records. |
| Semio precision vs semio-bias | Source or publication state wording may need semio repair, but not every state-like claim is a source, publication, or language-state case. |
| Cheap repair vs reusable discipline | Many cases need one local rewrite; recurring state-family failures need one reusable realization pattern. |

### A.19.SPR:4 - Solution

Repair state-family wording by producing a `StateFamilyPrecisionRepair` or an equivalent local rewrite.

Minimum shape:

```text
StateFamilyPrecisionRepair:
  triggerSpan:
  boundedTextSpan:
  bearerRef:
  stateFrameOrGoverningPatternRef:
  stateValueOrClassification:
  criteriaOrEvidenceRef?:
  admissibleUse:
  nonAdmissibleOverread:
  validityWindowOrReopenCondition?:
  finalWordingOrBlocker:
  remainingReaderUse:
```

Use the full shape only when the repair must remain inspectable. A direct rewrite is enough when one sentence names the bearer, state frame, value, use boundary, and governing pattern.

#### A.19.SPR:4.1 - Recovery sequence

1. **Capture trigger and bounded text.** Copy the encountered state-family word and the sentence, row, card, or field that uses it.
2. **Recover the bearer.** Name the item whose state-like value is being claimed: holon, role, source, evidence path, assurance claim, publication face, `PublicationUnit`, gate record, temporal claim, lens-use card, `DRR`, pattern version, project-side administrative record, review record, dispatch record, release or admission record, source-control record, or another FPF kind named by value.
3. **Recover the state frame or governing pattern.** Decide whether the frame is `A.19` `CharacteristicSpace`, `A.3.3` dynamics, role-state assertion, `C.2.2a` language-state chart, `A.10` evidence path, `B.3` assurance, `A.20` constraint or adjudication state, `A.21` gate decision, `E.17` publication use, `C.27` temporal-claim state, `C.29` lens-use admissibility, `E.9.DA` DRR-decision adequacy, `E.21` pattern quality, or a project-side administrative, review, dispatch, release or admission, or source-control record.
4. **Recover the value set or classification.** If a local field remains, list its possible values or the neighboring pattern governing that claim that defines them. If no value set is recoverable, do not keep the state-family head as a field.
5. **Recover criteria or evidence only when that claim is being made.** Name threshold rule, observation, source currentness, evidence path, assurance tuple, validation regime, gate record, or witness only when the governing pattern for that claim is selected.
6. **State admissible and non-admissible use.** Say what the reader may do with this value and what adjacent claim remains blocked.
7. **State validity window or reopen condition.** If currentness, readiness, release or admission, validation, assurance, or administrative state can decay, name what changes the value.
8. **Rewrite or demote.** Replace broad wording with the state-like field or governing-pattern phrase named by value; otherwise mark quote-only, reduced-use cue, blocked transfer, or incomplete rewrite.
9. **Return to the subject pattern.** Do not let the repair become the subject Solution unless the pattern is itself about state-family precision restoration.

#### A.19.SPR:4.2 - Direct governing-pattern assignments

| Recovered state-like claim | First governing pattern or locus |
| --- | --- |
| position in a declared `CharacteristicSpace` | `A.19`, with `A.17`, `A.18`, `C.16`, and `C.16.P` when construction is hidden |
| reusable transition law, trajectory, or dynamics model | `A.3.3` |
| role-state assertion, role assignment, or enactable state | role-state pattern named by value and `A.15` or work pattern governing the claim when work is being claimed |
| language-state position for episteme or publication wording | `C.2.2a` and `A.16.*` after `C.2.P` when source-publication recovery is needed |
| source use, source currentness, source publication, or source-use disposition | `C.2.P`, `E.17`, `E.9.DA`, or source-use field named by value |
| evidence path state, evidence relation, or reliance disposition | `A.10` |
| assurance result, assurance claim, assurance input, or engineering-justification use | `B.3` |
| constraint, local CV, gate, or release readiness | `A.20`, `A.21`, or release or gate pattern governing the claim |
| publication use, publication face, form, or unit value, source-finding use | `E.17`, `E.17.0`, `E.17.AUD`, or publication pattern governing the claim |
| Description episteme admitted for specification use or specification refinement | `A.7`, plus the specification-granting neighbouring pattern named by value: `A.6.2`, `C.2.3`, `A.21`, `C.16`, `E.17`, `E.10`, or another named pattern |
| temporal claim status or temporal-use classification | `C.27`, retaining `dynClaimPosture` only as a declared C.27 field |
| mathematical-lens use admissibility | `C.29`, retaining `LensUseAdmissibilityValue` only as a declared C.29 field |
| `DRR` decision-adequacy result or source-use classification | `E.9.DA` |
| pattern-quality result or pattern-quality review status | `E.21`, with `E.19` only as review or admission profile |
| administrative, review, dispatch, release or admission, or source-control state | the project-side administrative, review, dispatch, release or admission, or source-control record; not pattern prose unless the pattern's own `EntityOfConcern` is that record |

#### A.19.SPR:4.3 - Retained local field rule

A local `...Posture`, `...Status`, `...Readiness`, or `...State` field is admissible only when the text declares:

- field name;
- bearer kind;
- governing pattern;
- value set or declared classification source;
- admissible use;
- non-admissible overread;
- validity window, decay rule, or reopen condition when applicable.

If any of those are missing, either complete them now or rename the field to the phrase or record required by the governing pattern. A narrowing adjective does not count as kind recovery.

### A.19.SPR:5 - Worked slices

**Show, source currentness.** "The source posture is good" is not admissible. Repair to: "The source has `SourceUseRole = acceptedDecisionSource` and `SourceCurrentnessStatus = localAcceptedDecision` for this `DRR` use; it does not become evidence, assurance, gate passage, or FPF doctrine by citation."

**Show, evidence path.** "Evidence posture is incomplete" repairs to an `A.10` result: evidence kind, claim and effect, carrier or source path, currentness window, `RelianceDisposition`, admissible reliance, blocked reliance, and reopen trigger.

**Show, publication use.** "Publication posture allows decision input" repairs to an `E.17` publication use note plus the decision or evidence pattern governing the claim being made. The publication face may orient, expose a source, compare, or carry a candidate input; it does not decide or assure by itself.

**Show, mathematical lens.** `LensUseAdmissibilityValue` may stay in `C.29` because it names a local finite field for a mathematical-lens use. The field still cannot mean evidence, assurance, release, benchmark superiority, or source authority.

**Show, temporal claim.** `dynClaimPosture` may stay in `C.27` when its value set and non-overread boundary are present. The value says what kind of temporal claim use is being made; it does not upgrade evidence, authority, assurance, or promise claim.

**Show, administrative state.** "The release or admission record is ready for release action" belongs in the project-side release or admission, review, dispatch, administrative, or source-control record that carries that state. A pattern body may mention it only as an informative boundary; it must not use that external administrative state as pattern-subject guidance.

### A.19.SPR:6 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-A19SPR-1` | Every FPF-governed state-family word SHALL name a bearer or be demoted to ordinary prose, quote-only wording, reduced-use cue, or blocker. |
| `CC-A19SPR-2` | Every retained state-family field SHALL name the state frame or governing pattern that defines its value. |
| `CC-A19SPR-3` | Every retained state-family field SHALL have a value set, classification source, or neighboring-pattern result named by value. |
| `CC-A19SPR-4` | The repair SHALL state admissible use and non-admissible overread. |
| `CC-A19SPR-5` | Currentness, readiness, validation, assurance, release or admission, or administrative state claims SHALL state a validity window, decay rule, or reopen condition when the value can change. |
| `CC-A19SPR-6` | Source, evidence, assurance, publication, gate, work, decision, release or admission, and administrative uses SHALL be assigned to patterns governing the recovered claims or project-side records rather than hidden under state-family wording. |
| `CC-A19SPR-7` | Semio patterns govern only language-state and source or publication cases. They SHALL NOT become the general home for evidence, assurance, gate, work, temporal, mathematical-lens, or administrative states. |
| `CC-A19SPR-8` | Local fields named by value, such as `LensUseAdmissibilityValue` and `dynClaimPosture`, may stay only with declared governing pattern, value set, boundary, and reopen condition; specification wording SHALL recover a Description episteme admitted for specification use or refinement plus the specification-granting neighbouring pattern named by value. |
| `CC-A19SPR-9` | The repair SHALL preserve one remaining reader use. Type-correct but inert wording is incomplete. |
| `CC-A19SPR-10` | Whole-corpus cleanup SHALL be classified. Blind global replacement of `posture`, `state`, `status`, or `readiness` is nonconforming. |

### A.19.SPR:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Posture as cover.** | A sentence uses `posture` to avoid saying source relation, evidence path, assurance result, gate decision, or release state. | Recover the bearer and governing pattern; rewrite to the FPF field or block named by value. |
| **Support-to-state laundering.** | Old `support` wording becomes `support posture`, `basis posture`, or `source posture`. | Apply `A.6.P`, `A.6.6`, `C.2.P`, `A.10`, `B.3`, `C.16.P`, `C.29`, or the pattern governing the recovered claim. |
| **Finite field without value set.** | A `...Status` or `...Posture` field appears with no values or non-overread boundary. | Complete the field or replace it with the phrase or record required by the governing pattern. |
| **External administrative state in pattern prose.** | A project-side administrative, review, dispatch, release or admission, or source-control state appears as if it were user-facing pattern guidance. | Move the state claim to the project-side record; keep only an informative boundary if useful. |
| **Semio sink.** | Every state-like word is sent to source-publication or language-state repair. | Use semio only for source, publication, or language-state cases; assign evidence, assurance, gate, work, temporal, lens-use, and administrative cases to governing patterns or project-side records. |

### A.19.SPR:8 - Relations

| Pattern | Relation |
| --- | --- |
| `E.10` | Catches state-family trigger wording and selects local repair, `A.19.SPR`, direct governing-pattern assignment, controlled precision reduction, `F.18`, or fail-closed non-use. |
| `E.10.ARCH` | Provides the shared wording-use restoration architecture. `A.19.SPR` is the realization pattern for recurring state-family hidden-field cases. |
| `A.19` | Governs `CharacteristicSpace` and state-space typing. `A.19.SPR` uses A.19 only when the state-like claim is a characteristic-space position or comparable state. |
| `A.3.3` | Governs dynamics and state-transition laws when reusable change semantics are being claimed. |
| `C.2.P`, `C.2.2a`, `A.16.*`, `E.17` | Govern source-use and publication-use assignments, language-state positions, and admissible moves. |
| `A.10` | Governs evidence path state and reliance disposition. |
| `B.3` | Governs assurance result, assurance claim, and assurance-input use. |
| `A.20`, `A.21` | Govern constraint or adjudication state and gate decisions. |
| `C.27` | Governs temporal-claim state and retains `dynClaimPosture` when declared. |
| `C.29` | Governs mathematical-lens use and retains `LensUseAdmissibilityValue` when declared. |
| `E.9.DA`, `E.21`, `E.19` | Govern DRR adequacy status, pattern-quality status, and pattern review or admission profiles. |
| `F.18` | Governs durable naming when a state-family field becomes reusable vocabulary. |
| `E.11` | Places practical entry questions for hidden state-family wording in README scenarios, ToC query cues, local Problem frames, or expanded `I.2` entry-disambiguation cases instead of a duplicate index row. |

### A.19.SPR:9 - Rationale

The repeated problem is not a bad word. The repeated problem is an untyped state-like claim. FPF needs finite state-like fields, but each field must be over a bearer and a state frame. Placing this pattern under the `A.19` neighborhood keeps the general repair near state-space and state-comparability discipline without making semio the home for every status word and without turning `E.10` into an omnibus ontology.

The pattern also protects local fields named by value. `LensUseAdmissibilityValue` and `dynClaimPosture` are acceptable when their governing patterns declare value sets and boundaries. Specification wording is acceptable only as a Description episteme admitted for specification use or refinement under a specification-granting neighbouring pattern named by value; it is not a reusable posture field. Broad `source posture`, `evidence posture`, `assurance posture`, `publication posture`, `release posture`, and administrative forms are not acceptable unless they are repaired into FPF kinds named by value or moved to the project-side administrative, review, dispatch, release or admission, or source-control record that actually governs them.

### A.19.SPR:End

