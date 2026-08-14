## C.2.P - Epistemic Precision Restoration

> **Type:** C.2 precision-restoration pattern for episteme, publication, source wording, and source-relation wording
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.2.P:0 - Use this when
**First useful move.** Decide whether the wording is source-expression clarification or FPF-governed use. Then write the smallest sufficient output: repaired sentence, candidate-set note, compact epistemic precision-restoration row, full epistemic precision-restoration check, or explicit non-use disposition.

**Source-expression clarification.** Use this mode when ordinary non-FPF prose needs precise interpretation. The aim is source-local clarification: recover what the sentence may mean, identify candidate kinds and relations, preserve important wording when needed, and produce one clarified phrase, candidate-set note, epistemic precision-restoration note, or use disposition. This mode may use `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another relevant FPF pattern as a repair lens, but it does not require the source expression itself to use FPF vocabulary.

**FPF-governed use.** Use this mode when wording has FPF-governed use and hides one of this pattern's recovery fields. The field may be an episteme or episteme-side view field; a publication, publication form, generic publication face, MVPK face under E.17 constraints, or bounded publication unit field; a carrier or rendering relation; a relation or declared-use-boundary field; or a pattern-application wording field. The wording states the recovered FPF kind named by value, relation record, relation phrase, tuple-like record, project-side FPF kind and reference named by value, or explicit non-use disposition.

Use `C.2.P` as epistemic precision restoration for wording whose hidden field belongs to one of these field families, not to one new umbrella kind:
- source-expression fields: source wording and source-local meaning;
- episteme fields: claim-bearing episteme, episteme-side view, EntityOfConcern, and grounding relation;
- publication fields: publication, face, publication unit, publication-form relation, carrier relation, and rendering relation;
- project-side-use fields: pattern-application wording, project-side reliance wording, and the disposition by which source expression has or lacks FPF-governed use.

Use `E.10` for lexical and wording-use precision and `C.2.P` for epistemic precision restoration across episteme, publication, carrier-relation, and view distinctions. The C.2.P recovery fields are source expression, source-local meaning, recovered FPF kind and relation set, publication construction, carrier relation construction, view construction, EntityOfConcern or grounding relation, reader use, and use or non-use disposition. These are fields of one recovery pass, not sibling kinds.

The practical partition is episteme identity or direct-relation use versus publication-construction use, but it is not limited to named C.2.1 relations. It also handles source expressions selected for FPF-governed use and pattern-application wording when those phrases carry a claim or use boundary. Apply this pattern from E.10 only when the applicable pattern cannot yet be selected because one recovery field is unresolved: source wording, claim-bearing episteme, publication construction, carrier-relation construction, project-side reliance, pattern-application wording, or use or non-use disposition. The local decision selects source-expression clarification or FPF-governed use, recovers the episteme-publication relation set, chooses a recovery disposition, and preserves remaining reader use before a neighboring pattern supplies its own definition, constraint, or test.

For source-wording restoration, `C.2.P` stops at recovery. It names the recovered FPF kind, relation, `projectSideFPFRef`, `declaredUseBoundary`, `relationClaimSlice`, remaining reader use, or explicit non-use disposition. When another FPF pattern defines, constrains, or tests a recovered field, name that pattern and leave the field in its ontology. Do not turn source wording into a standalone kind or keep authority, evidence, gate, work, assurance, or readiness inside source wording.

**Source-use wording guard.** Do not read `source-use` as ordinary work with primary sources or citations. In this pattern, the compact phrase only flags that source wording, a source-bearing relation, a source-ref marker with its referenced object kind or relation slot named, or a source-finding cue is being asked to support FPF-governed use. The actual recovered field must be named through this pattern's fields: source expression, publication relation, carrier relation, relation slice, declared-use boundary, project-side FPF reference, or explicit non-use disposition. If that field is not recoverable, write the more specific phrase - source wording, source-bearing relation, unresolved source-finding cue, quote-only wording, or no FPF-governed use - instead of closing on `source-use`.

**Source-to-use continuity rule.** A source-wording repair is not closed merely because the broad word `source` was replaced by a more precise object name. Preserve the relation that made the wording useful. Name the source expression or source-bearing position that matters: selected source `U.Episteme`; an `EpistemePublicationRelation` occurrence or reference when availability matters; publication form or face; carrier, source-currentness, or source-bearing relation; source-ref marker with its referenced kind or relation slot; relation-claim slice; project-side FPF kind and reference; declared-use boundary; or explicit non-use disposition. Then state which input is used, what transformation, rendering, or use path carries it forward, what use is admissible, and what reopen condition or next pattern applies if the use escalates. Do not close on `value` unless the applicable pattern has a value slot. If these answers cannot be stated, lower the wording to source-finding only, reduced-use cue, blocked use, or incomplete rewrite.

**Epistemic source-material and work-boundary sequence.** When `source data` or epistemic `source material` is current, first recover the source expression, selected source `U.Episteme`, any publication occurrence needed to establish availability, and the source-to-use relation. Then treat any separate relation to a method, plan, work occurrence, transformation, evaluation, delivery, transfer, or receiving use—and the posture claimed for that relation—with the applicable pattern. Stop if that work-side relation and posture are already readable; apply `A.6.P.WMR` only while either remains hidden. Keep physical raw material in its constituent, affected-referent, resource-use, supply, transfer, or transformation relation; the adjective `source` does not move it into `C.2.P`. The source-side settlement and the work-side relation claim are distinct and must not be merged.

**Source-return boundary.** Do not use `source-return` as the generic name for source-wording repair. In the current FPF corpus, `source-return condition` is admissible only for the reverse or escalation edge in a derivative, coarsened, extracted, compressed, rendered, or reused carrier. The reader has already moved away from a named source expression, selected source `U.Episteme`, publication occurrence when availability matters, source-bearing relation, transform record, or evidence relation; a stronger use, dispute, freshness change, hidden loss, or missing distinction now requires return to that source or relation. Name a rule-bearing `ClaimGraph` only when later comparison or reuse depends on rule identity. For ordinary movement from source into current use, say source-to-use path, source relation, source-bearing relation, source expression, or name the applicable relation.

**Work-reliance boundary.** `C.2.P` does not decide whether work may proceed. Use `A.15.4` only after the wording repair shows that an appearance is being used as a reason for intended work or reliance and the relevant slot, relation, or project-side reference is still unnamed. If the applicable pattern is already known, use it without an `A.15.4` intermediate step.

**Precision-restoration pattern note.** A precision-restoration pattern is an architectural pattern for a recurring complex precision problem whose wording routinely hides several current distinctions. `A.6.P` is relation precision restoration; `C.2.P` is epistemic precision restoration. `C.30.P` is the selected architecture and structure precision-restoration pattern when architecture or structure wording hides the architecture claim being made, structure kind, structure relation, view, publication relation, or source relation selected for the current architecture claim. `C.16.P` is the selected characteristic and scale precision-restoration pattern when characteristic, scale, metric, score, indicator, coordinate, threshold, or comparison construction is hidden. `C.16.Q` is the selected quality-term precision-restoration pattern when quality-term or evaluative characterization is current and the found problem is not relation construction. `E.10` detects the wording problem and selects the applicable recovery pattern; `E.10.ARCH` carries the shared recovery algorithm and applicability-row architecture; neither replaces this pattern's episteme, publication, and source-relation ontology.

| Problem in the wording | Use this pattern for | Applicable neighboring FPF pattern |
| --- | --- | --- |
| Ordinary source text needs more precise language | Source-expression clarification: clarify the source-local meaning and, when needed, produce a candidate-set note, epistemic precision-restoration note, or use disposition. These are output forms for one clarification pass, not object kinds. | `E.10`, `A.6.P`, `A.6.6`, `F.18`, `A.7`, `E.17`, or another relevant pattern as a lens for the claim or declared-use-boundary question. |
| Wording has FPF-governed use | FPF-governed use: fill the smallest needed recovery field: recovered FPF kind named by value, relation record, relation phrase, tuple-like record, project-side FPF kind and reference named by value, or explicit non-use disposition. | `E.10` plus the pattern that defines, constrains, or tests each recovered claim or declared-use boundary. |
| An episteme or publication field is current | Recover the field family before accepting the sentence: claim-bearing episteme and its EntityOfConcern or grounding relation; publication, view, face, or bounded publication unit; carrier relation; or source relation named by value. | `C.2.1`, `A.7`, `E.17.0`, `E.17`, MVPK, and local episteme and publication patterns. |
| A relation or use-boundary field is current | Recover the relation, claim being made, declared-use boundary, or project-side reliance field before treating the wording as FPF-governed. | `A.6.P`, retained A.6.P specializations, `A.6.B`, and the applicable evidence, work, decision, assurance, causal-use, mathematical-lens, or quality pattern. |
| A reusable term or stable local head is being chosen | Prevent a broad replacement from becoming a new FPF term by taste. | `F.18`, with `E.10:0.2` replacement-candidate anti-umbrella rule. |
| The repair would leave correct typing but no useful reader action | Treat the rewrite as incomplete. | `E.2`, `E.8`, `E.10:6.2`, `E.12`, and the FPF pattern named by value that carries the claim being made. |

**Ordinary-language survival.** Ordinary words can stay ordinary until the sentence gives them FPF-kind, relation, authority, evidence, use-boundary, work, gate, decision, bridge, or reliance claim. `Source` may stay ordinary when it only means where a quote came from; `view` may stay ordinary when it means what the reader sees and not `U.View`; `route` may stay ordinary navigation prose; `support` may stay ordinary help. Repair by FPF-governed sentence function, not by trigger word alone.

**Not this pattern when.** `C.2.P` is not the pattern for every recovered construct. Use `E.10` for general lexical conformance, `F.18` for stable reusable naming, `A.6.P` for relation precision, `A.6.B` for law-, use-boundary-, deontic-, and effect-claim splitting, `A.7` for EntityOfConcern, Description episteme, and carrier separation, and `E.17` or `E.17.0` for view and publication discipline. Use `C.30`, `C.30.ASV`, `A.22`, `C.31`, or the relevant architecture or structure pattern for those claims; use the relevant FPF pattern for project work, evidence, gate, decision, method, action-invitation, assurance, or engineering-justification claims. When one of these claims is current, `C.2.P` supplies source-expression unpacking and rewrite disposition; the named pattern supplies its invariant.

**Do not punish clarity.** Prefer the clearest ordinary head that preserves kind, relation, and declared use boundary. Do not replace a clear plain phrase with a technical phrase unless the technical phrase blocks a currently plausible false interpretation or is needed for accepted stable FPF naming. In an ordinary case, `reader help`, `source-pointer-only`, or `comparison only` may be better than a more technical phrase.

### C.2.P:0.1 - What goes wrong if missed

Episteme-publication-heavy text starts to build a parallel ontology. A generic publication face becomes a `U.View`, a file becomes an episteme, a dashboard tile becomes evidence, a pattern name becomes a procedure, or a slash list becomes a group kind. A broad word such as `source` is especially dangerous because it can hide several different recovery fields: an FPF pattern or `DRR`; a publication field; a document named for source, evidence, architecture, or review use; a reviewed publication, review packet, review record, or review state; a project-side FPF kind and reference named by value; or a relation.

The immediate cost is not only ugly terminology. Engineers and FPF authors start making action, evidence, gate, decision, or engineering-justification claims from the wrong entity, publication, record, relation, or carrier.

### C.2.P:0.2 - What this buys

`C.2.P` gives one small epistemic precision-restoration move: recover the FPF kind and relation set first, then write wording that preserves the needed distinction without adding another claim. It prevents string-replacement cleanup, keeps FPF-side and project-side episteme and publication work separate, and blocks unclear wording from having FPF-governed use by guesswork.

**Successful repair condition.** Type-correct wording is not enough. A repair must satisfy the `E.2` Pillars, especially `P-2 Didactic Primacy`, together with `E.12` and the register rule in `E.10:6.2`. It closes only when the text preserves or restores a usable action, a recognition reason that tells the working reader why the distinction matters, or a named FPF pattern application that carries the claim. When Tech and Plain registers are both current, the Tech interpretation remains recoverable and the Plain or didactic line maps back to it. An ordinary or metaphorical Plain line may stay light when it carries no FPF-governed use; if it carries an ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim, that claim must be recoverable through the Tech fields, named FPF kind, recovered relation, project-side reference, or disposition. A repair to a Problem frame, recognition text, example, or worked slice is incomplete if it improves typing but hides the working situation, why it matters, or the first useful action; name the applicable FPF pattern when that pattern carries the claim. Overread removal is only half of the repair; the other half is remaining action guidance under the Pillars.

**Recovery focus in plain terms.** The use being made is one episteme-publication-heavy wording use inside conformant text: the word or phrase, the sentence function it carries, the FPF kind or relation it must recover, and the remaining declared use boundary after recovery.

**Primary working user.** The first user is a practitioner maintaining conformant FPF-style or project text: an author, reviewer, or engineer-manager who must repair wording without losing ontology. The downstream user is the practitioner who will rely on the repaired pattern or project text in a working situation.

**Anti-overread payoff question.** A repair is useful only if the text can say in ordinary prose what false downstream interpretation is blocked, what useful action remains, and when the reader must apply another named FPF pattern because evidence, gate, decision, work, assurance, bridge, release, or reliance is current. If the repair blocks an overclaim but leaves no useful action, it is probably becoming ceremony rather than guidance.

### C.2.P:1 - Problem frame

FPF already has episteme, publication, view, carrier, presentation, relation, naming, and pattern-application concepts. FPF-governed project, review, draft, pattern, and architecture prose, plus source prose being unpacked for possible FPF use, can still introduce convenient intermediate words that survive into final guidance without their kind and relation set recovered.

The recurring situation is simple: a sentence is understandable enough to feel worth keeping, but its head kind is not recovered. If it is repaired by replacing one broad word with another broad word, the ontology gets worse while the text looks cleaner.

#### C.2.P:1.1 - Purpose and Scope

This pattern gives the current glossary and rewrite rules for terms around epistemes, publications, views, publication forms, generic publication faces, MVPK faces under E.17 constraints, carriers, records, and bounded publication units.

It exists because episteme-publication-heavy texts can use locally convenient heads that collapse EntityOfConcern, publication unit, publication face, carrier, record, source relation, and project-side FPF kind and reference. Those words may be useful recognition handles, but they are not safe FPF heads when they carry ontology, authority, or authority-changing meaning.

The rewrite discipline here is ontological and use-facing, not lexical; in this pattern the repair is bounded to episteme, publication, source wording, and source-relation precision:
- do not replace one broad token with one new broad token by string substitution;
- first recover the FPF kind and relation set, whether the wording carries a claim, the publication, view, carrier, or relation construction, and any work, action, or authority crossing;
- then choose the smallest wording that preserves the FPF-governed distinction without creating a second ontology.

This pattern uses the `E.10` trigger result as its entry condition, then works in the `C.2.1` and `E.17` epistemic-publication ontology rather than in a lexical registry.

### C.2.P:2 - Problem

Without an epistemic precision-restoration discipline for episteme-publication-heavy wording:

1. broad publication words hide which field family is current: episteme or view, publication form or face, bounded publication unit, carrier relation, named document use, review-state use, or project-side FPF reference;
2. FPF pattern-application claims and project-side fields for work occurrence, work plan, decision, action invitation, method, record, carrier relation, or front-end relation get mixed in one sentence;
3. slash lists and heterogeneous rows become false group kinds;
4. unclear source meaning is guessed into FPF-governed wording rather than blocked or assigned to an accepted FPF extension;
5. authors copy the same loose wording into `DRR`s, patterns, source-relation notes, source-ref target notes, or project texts.

### C.2.P:3 - Forces

| Force | Tension |
| --- | --- |
| Precision vs readability | FPF-governed wording needs kinds named by value, but a sentence overloaded with every possible kind becomes unreadable. |
| Preservation vs cleanup | Accepted source text or accepted governing text must not be paraphrased away, but source-companion statement cannot be mistaken for pattern authority. |
| Local repair vs new ontology | Many phrases only need local A.6.P and F.18 recovery; a few reveal a real missing FPF kind or relation. |
| FPF-side vs project-side work | The same word can describe FPF pattern authorship or a user's project publication, record, work, or action. |
| Guidance vs audit | The pattern must tell authors what to do, while check rows only verify that the rewrite was carried out. |

### C.2.P:4 - Solution

Repair episteme-publication-heavy wording by epistemic precision restoration, not by dictionary replacement.

A successful rewrite satisfies these field-validity constraints:

1. the head kind and sentence function are recoverable under `E.10`;
2. a stable reusable name has an `F.18` naming result;
3. a relation, comparison, dependency, support, sameness, grounding, mapping, or endpoint claim has `A.6.P` relation precision, with use-boundary and project-side reliance questions split into their own fields;
4. a claim-bearing episteme, episteme species named by value, episteme-lane view, or project-side FPF kind and reference named by value has the needed `C.2.1` typing or named FPF claim or declared-use boundary named by value;
5. publication, view, face, and carrier distinctions satisfy `E.17.0`, `E.17`, and MVPK;
6. the repaired text satisfies `E.2` Pillars, especially `P-2 Didactic Primacy`, by preserving or restoring one remaining reader use: a usable action, a recognition reason that tells the working reader why the distinction matters, or a named FPF pattern application that carries the claim being made; when both Tech and Plain registers are current, the Plain or didactic line maps back to the recovered Tech kind, relation, or FPF pattern application under `E.10:6.2`; ordinary Plain wording and intentional didactic metaphor stay light when they carry no FPF-governed use, but ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim in a more expressive Plain line must be recoverable through the repaired Tech fields; FPF-governed Problem frames, Problem sections, recognition texts, examples, and worked slices must still show the broad working situation and first useful move, or the rewrite is incomplete;
7. the final phrase preserves the distinction without adding another claim;
8. unrecoverable meaning, kind, register mapping, or remaining reader use fails closed.

The detailed solution below carries the glossary and rewrite rules as ordinary pattern subsections. It is not an external container: these subsections are the pattern's detailed epistemic precision-restoration guidance.

#### C.2.P:4.0a - EpistemicPrecisionRestorationRecord

For FPF-governed cases, the recovery product is a compact pattern-local `EpistemicPrecisionRestorationRecord` or an equivalent local rewrite note. Ordinary local phrase repair may end as the repaired sentence itself when kind, relation, and declared use boundary are clear and no downstream reliance, cross-context reuse, grouped-kind risk, hidden authority claim, project-side overclaim, conflict among publication, EntityOfConcern, and project-side action claims, or contested source meaning remains. Prefer the plain names `epistemic precision-restoration note`, `compact epistemic precision-restoration row`, or `local rewrite note` when durable inspection does not require the code-like field name. The recovery note is a lightweight pattern-local authoring or review product, not a new ontology, dispatch table, durable FPF record kind, or mandatory heavyweight project record. It becomes durable only if another accepted pattern or `DRR` explicitly admits it. It records only the trigger, recovered FPF kind and relation set, requirement from the applicable FPF pattern, and final rewrite disposition that must remain inspectable.

Minimum fields when FPF-governed:

Recover by sentence function and claim, not word form. For words such as `source`, `support`, `status`, `valid`, `ready`, `approved`, and `used`, first ask what consequence the sentence would allow: source-finding only, source availability, a source relation required by an applicable pattern, evidence relation, gate passage, decision status, readiness threshold, work permission, assurance, engineering justification, or ordinary orientation. Fill only the field whose FPF kind, relation, or project-side reference is current. This list names possible consequences, not kinds in one ontology.

| Field | Meaning | Relevant FPF source when the corresponding claim is made |
| --- | --- | --- |
| `triggerSpan` | The word, phrase, field, row, or sentence fragment carrying episteme-publication claim-bearing use. | `E.10` and this pattern. |
| `sentenceFunction` | Whether the span is definition, claim, instruction, comparison, publication description, evidence statement, gate statement, work statement, reliance statement, example, quote, or another named function. | `E.8`, `E.10`, and the local pattern being authored. |
| `recoveredHeadKind` | The FPF kind named by value or explicit non-use disposition recovered from the phrase. | `F.18`, `A.6.P`, `A.7`, and the pattern that defines, constrains, or tests that kind. |
| `laneAndKindSet` | The current side plus field family. Use this field to say whether the repair is on FPF-side pattern text, project-side episteme, project-side publication, project-side work, A.7 EntityOfConcern-description-carrier separation, publication relation, carrier relation, front-end relation, or a project-side FPF reference such as work, evidence, gate, decision, or action invitation. | `A.7`, `E.17`, current episteme and publication patterns, and project-side FPF patterns. |
| `publicationRelationSet` | Selected `U.Episteme` when content identity matters; an `EpistemePublicationRelation` occurrence or reference when availability is current; `PublicationFormExpressionRelation`, publication form, generic publication face, MVPK face under E.17 constraints, bounded `PublicationUnit`, `PublicationFormBearingRelation`, `U.PresentationCarrier` under E.17 and E.24.PUB when that carrier is current, rendering relation, and front-end relation when that relation is claimed. | `C.2.1`, `E.24.PUB`, `E.17.0`, `E.17`, MVPK, and `A.7`. |
| `claimBearingEpistemeOrRecord` | Current claim-bearing `U.Episteme`, episteme-lane `U.View` with an explicit episteme tether when `E.17` or the applicable view pattern makes that typing current, project record kind and reference named by value, or no claim-bearing episteme or record disposition. Publication form, generic publication face, carrier, `PublicationUnit`, and source-finding cue stay in `publicationRelationSet` or `projectSideFPFRef` unless the claim is about that object. An MVPK face uses episteme-lane `U.View` typing only when the MVPK profile makes it current. | `C.2.1`, `E.17`, and the applicable record pattern when current. |
| `relationClaimSlice` | Empty, or a local note that `A.6.P` relation precision is current for this sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when current. | `A.6.P`. |
| `declaredUseBoundary` | The declared use boundary, blocked use outside that boundary, and L-, A-, D-, and E-claim split when the sentence makes a boundary-use claim. | `A.6.B`, `A.6`, and the applicable pattern for that use. |
| `projectSideFPFRef` | The project-side FPF kind and reference named by value when the sentence would be used for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. | `A.15`, `A.15.4`, `A.10`, `A.20`, `A.21`, `B.3`, `C.11`, `A.2.8`, `A.2.9`, `A.6.A`, or another applicable FPF pattern. |
| `recoveredGoverningPattern` | Empty, or the pattern that defines, constrains, or tests the recovered field after source wording, current FPF wording, publication, and carrier recovery. Fill this only when the record has recovered enough to leave `C.2.P` and use that pattern. The field name is retained for schema compatibility; it does not make a pattern an actor or owner. | `E.10`, `E.10.ARCH`, and the applicable pattern for the recovered field. |
| `selectedRewrite` | The final wording named by value or record-shaped value. | This pattern plus any other pattern needed for the recovered claim. |
| `remainingReaderUse` | One short line, Plain-facing when the text serves a working reader, naming what the reader may now do, why the distinction matters, or how another named FPF pattern contributes to the claim. This is the local `E.2` `P-2` preservation check, not optional commentary. When Tech and Plain registers are both current, the line maps back to the recovered Tech kind, relation, or pattern application. It may be memorable or metaphorical, but any ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim must remain recoverable through the repaired Tech interpretation. If no such line can be stated, the rewrite is incomplete or must fall to a non-use disposition. | This pattern, `E.2`, `E.8`, `E.10:6.2`, `E.12`, and any other pattern that contributes to the claim. |
| `disposition` | Local recovery outcome: recovered by value, reduced-use cue, understandable FPF extension candidate, blocked use, rewrite incomplete, or not triggered. This slot is not a recovered FPF kind. | This pattern. |

`projectSideFPFRef` distinguishes a user-project object, relation, record, or work-use reference from FPF-side pattern or publication text. It replaces no other use qualifier: an exact source or practice boundary, a selected `BoundedModelUseStructure` for a DDD use, claim scope, window, and viewpoint remain separate when current.

Use the short form when only one field is current. Use the full record when several fields are current or when the phrase might otherwise create a grouped kind, hidden authority claim, project-side overclaim, conflict among publication, EntityOfConcern, and project-side action claims, contested source-relation meaning, or procedure-like ordering of pattern applications.

**Carrier-specific recovery.** Words such as `carrier`, `publication carrier`, `access carrier`, `framework carrier`, `front door`, `front-end`, `rendering`, `file`, `dashboard`, `screen`, `skill pack`, or `MCP route` are only recognition cues. First recover the current field: `U.PresentationCarrier` or another carrier relation; publication or access exposure; source-finding cue; evidence or provenance carrier; generated or produced carrier; framework publication or access carrier; or project-side work or reliance. Then use the relevant pattern: `C.2.1` for episteme identity and its direct constitution, empirical-grounding, and edition relations; `E.17`, `E.17.AUD`, and `E.24.PUB` for publication face, unit, carrier, and access or publication relations; `A.10` and `G.11` for evidence, currentness, and provenance; `C.35` for generated or discovered carriers; `E.4.FPF`, `E.4.DPF`, `E.4.PFR`, or `E.4.DPF.DA` for framework package carriers; `A.15` or `A.15.4` for work or reliance; and `C.30.P`, `C.33`, or `C.34` for architecture or structure use. Do not close with `carrier` alone: name the recovered field and the pattern contribution that matters.

#### C.2.P:4.1 - General Recovery Check
Use this recovery check whenever text proposes a new term, repairs an episteme-publication-heavy term, asks for language precision, or relies on wording around `PublicationUnit`, `EntityOfConcern`, publication, view, face, carrier, source relation named by value, source-bearing relation, publication face, EntityOfConcern, or bounded publication-unit claim.

0. **Mode selection.**
   Decide whether the current use is source-expression clarification over non-FPF prose or FPF-governed use. In source-expression clarification, preserve source-local nuance and do not force the whole source into FPF vocabulary. In FPF-governed use, the wording must satisfy `E.10` and any applicable patterns named by the recovery.

1. **E.10 trigger scan and head-kind recovery.**
   Use `E.10:0.2` as the shared trigger scan. Decide what the head noun names before accepting the phrase: EntityOfConcern, Description episteme, or Description episteme selected for specification use, `U.Episteme`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, `U.PresentationCarrier` or another carrier or rendering relation, project-side FPF kind and reference named by value, `A.15.1` dated `U.Work` occurrence, `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, `U.Method`, `U.MethodDescription`, document named for source, evidence, architecture, or review use, reviewed publication, review packet, review record, or review state, or source-local ordinary sense. Apply EntityOfConcern and Description-episteme boundaries, specification use, source-local meaning and scope, Tech, Plain, and carrier-humility rules before treating a word as meaning-bearing.

2. **F.18 naming pass when a stable term is being chosen.**
   If the phrase is becoming a reusable head, fill at least the lightweight Name Card facts: governed value and kind; the pattern and contribution that define or constrain it; effective scheme; any source or practice boundary that changes local identity; local-sense claim; intended use; candidate head families; NQD-front reasoning; sense-seed read-through; and the lexical Q tuple `{SemanticFidelity, CognitiveErgonomics, MorphologicalActionFit, AliasRisk}`. Do not pick a label only because it is intuitive. Do not accept a replacement label until it passes the `E.10:0.2` replacement-candidate anti-umbrella rule.

3. **A.6.P relation-precision pass when a phrase carries relation, comparison, or action-invitation claim.**
   Restore generic head kind first, then endpoint facets and kinds, then relation kind, slots, qualifiers, scope, time, viewpoint, and hooks for use-boundary, evidence, and work. For `support` wording, do not stop at a substitute label: select the current support-like claim or relation under `A.6.P` first, including source-description relation, EntityOfConcern or grounding-holon grounding, base relation through `A.6.6`, evidence, assurance, causal-use, mathematical-lens, characteristic or measurement, declared-use-boundary, work or enablement, or publication-companion use. If ambiguity remains, write a local Candidate-Set Note rather than debating synonyms.

4. **C.2.1 episteme-identity and direct-relation pass when the recovered value is claim-bearing.**
   Name exact claim content, EntityOfConcern, and effective ReferenceScheme. If empirical grounding is current, name the exact covered claims, grounding holon, and obtaining `EpistemeEmpiricalGroundingRelation`. Name a viewpoint only through the describing use that selects it; keep E.17.0 conformance and same-individual `U.View` membership, C.29 representation relations, publication, and carrier relations separate. Do not use `PublicationUnit` or a carrier word as a substitute episteme.

5. **E.17.0, E.17, MVPK publication pass when the recovered value is published or reader-facing.**
   Separate the underlying selected `U.Episteme` or episteme-lane `U.View`, an `EpistemePublicationRelation` occurrence when availability is current, publication form, generic publication face, MVPK face under E.17 constraints, `PublicationUnit`, carrier or rendering, and the project-side FPF kind and reference when a project-side claim is current. A face, card, screen, or explanation can guide interpretation or source-finding without becoming evidence, work, gate passage, authority, or release permission. If those claims are current, fill `declaredUseBoundary` and `projectSideFPFRef` instead of treating the face as the source value.

5a. **Neighboring-pattern selection after source wording and current FPF wording recovery.**
   If source wording and current FPF wording, publication, carrier, face, or `PublicationUnit` recovery exposes a neighboring pattern's field, put that pattern in `recoveredGoverningPattern`. Do not keep the neighboring field inside `C.2.P` after source wording, current FPF wording, and the publication relation set have been recovered.

6. **Remaining reader use.**
   After the kind, relation, publication, and project-side splits are recovered, state remaining reader use in one short line: what the reader can now do, why the distinction matters, or how another named FPF pattern contributes. When Tech and Plain registers are both current, keep the Tech interpretation recoverable and map the Plain or didactic line back to it under `E.10:6.2`. Do not make this a heavy form for ordinary prose. If the repaired wording only proves that an overclaim was removed but leaves no usable action, recognition reason, or pattern application, do not classify it as recovered by value.

7. **Authority-changing rewrite boundary.**
   If the result would rename an accepted FPF pattern, change an accepted FPF term, or mint a reusable FPF kind, this pattern only classifies the phrase as recovered by value or as an understandable FPF extension candidate. It does not make the authority change by itself. Use the accepted source that already carries the decision by value; do not add a second decision source merely to restate the same content.

Fail closed:
- if the kind and relation set cannot be recovered, keep the term as plain or informative prose;
- if the relation kind cannot be recovered, keep the statement as a cue or split alternatives;
- if the publication construction cannot be recovered, do not use that publication, generic publication face, MVPK face under E.17 constraints, form, carrier, or rendered unit for work, evidence, gate, or authority claims;
- fill `relationClaimSlice` only when a relation claim is current, and fill `declaredUseBoundary` plus `projectSideFPFRef` when an use-boundary or project-side reliance claim is current;
- if the recovered wording is type-correct but leaves no remaining reader use, recognition reason, Tech-to-Plain mapping when both registers are current, or FPF pattern application, or if a Plain or didactic line supplies practical guidance through unrecovered ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim, mark the rewrite incomplete or demote the phrase to reduced-use cue or blocked use before using it as claim-bearing FPF or project text.

##### C.2.P:4.1.1 - Slash Discipline

In conventional abbreviations, source titles, mathematical notations, standards, URLs, file paths, and ordinary notations, a slash can be part of an accepted designation rather than a hidden FPF kind. In FPF-facing episteme and publication ontology, a slash is still a recovery trigger before it is a synonym marker unless the mark is part of such accepted notation, carrier syntax, or conventional designation.

Before leaving a slash expression in current prose, classify the expression as one of these cases:
- accepted notation or conventional designation: a standard name, source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, file path, URL, or quoted source wording where the slash is part of the accepted designation or carrier syntax; keep `ISO/IEC`, `ISO/IEC/IEEE`, `1/2`, URLs, conventional abbreviations, and similar forms when the sentence uses them as notation;
- a plain-language synonym pair with no ontology, authority, evidence, or use-boundary claim;
- a lazy `and/or`-style join that must be split or recovered before FPF-governed use;
- a composite-kind candidate that needs `F.18` and `A.6.P` recovery;
- a relation claim that needs a `RelationKind`, a `QualifiedRelationRecord`, or a multi-term relation phrase with typed endpoints, slots, qualifiers, scope, time, and viewpoint;
- a tuple-like record that needs a named record kind and named slot semantics;
- a failed ontology signal where the sentence lists unlike values because the FPF kind under repair, relation record, relation phrase, tuple-like record, alternative-case disposition, or not-triggered disposition has not yet been recovered.

If the expression is not one of the safe notation, conventional-designation, carrier-syntax, quoted-source, or plain-language cases, do not keep the slash as final wording. Do not repair it by replacing the slash with one equally vague grouped word.
Write the recovered FPF kind, relation record, relation phrase, tuple-like record, alternative-case disposition, or not-triggered disposition by value.

##### C.2.P:4.1.2 - Unclear Source Meaning and FPF Extension Candidates

Sometimes the problem is not a bad word but one of two different cases:
- the intended claim cannot be determined from the surrounding source, current `FPF` kinds, or current FPF episteme and publication ontology;
- the claim is understandable, but current `FPF` does not yet contain the kind, pattern, relation record, or method guidance needed to carry it.

Do not merge those cases.
An unclear claim is not current architecture truth merely because deleting it feels risky, and it must not be rewritten by guessing a likely author intention.
An understandable uncovered claim may be retained as a candidate `FPF` extension only when the problem situation, tempting overread, rejected current uses, current `FPF` gap, and the first user action that would improve are stated by value.

Classify the case explicitly:
- **recovered by value:** the text now names the current `U.Episteme`, selected `EntityOfConcern`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, `PublicationUnit`, carrier relation, relation record, relation phrase, tuple-like record, FPF pattern, document named for source, evidence, architecture, or review use, reviewed publication, review packet, review record, or review state, project-side FPF kind and reference named by value when `projectSideFPFRef` is current. The selected value is one current value, not the list: `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; `A.15.1` dated `U.Work` occurrence; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence path; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or not-triggered alternative;
- **understandable FPF extension candidate:** the thought is clear enough to state as a candidate new or amended FPF kind, pattern, relation record, method guidance, accepted `DRR` content decision, or campaign-scoped content question, but it does not carry current authority, evidence, or use-boundary claim until an accepted architecture decision, accepted `DRR`, or accepted FPF pattern supplies that authority;
- **source wording without FPF-governed use:** the phrase has no current authority, evidence, or use-boundary claim;
- **reduced-use cue:** the phrase is kept only as a recognition cue or anti-case, not as a claim-bearing architecture decision;
- **blocked use:** the phrase is blocked for claim-bearing architecture, pattern, or project text while the needed meaning, kind, or relation is missing.
- **rewrite incomplete:** the repaired wording may be kind-correct, but it does not yet state a remaining reader use, recognition reason, Tech-to-Plain mapping when both registers are current, or FPF pattern application, or a Plain or didactic line carries ontological, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary claim that cannot be recovered from the Tech interpretation; continue repair or demote to a non-use disposition before the text has FPF-governed use.

These dispositions are recovery results, not a meta-governance authority over all of `FPF`.
When recovery names another FPF kind, use the pattern that defines or constrains that kind, its declared use boundary, and its conformance checks.
`C.2.P` may identify that `A.10`, `A.15`, `A.15.4`, `A.20`, `A.21`, `B.3`, `C.11`, `F.9`, `E.17.EFP`, `E.17.ID.CR`, or another FPF pattern applies.
After that identification, `C.2.P` no longer defines or constrains the recovered kind.
`C.2.P` only makes the kind under repair, relation, and use boundary explicit enough to apply the appropriate pattern.

No other disposition is closed.
In particular, "seems to mean", "probably about", a cleaner paraphrase, or a broad umbrella replacement is not a successful recovery.

#### C.2.P:4.2 - Core Glossary

##### C.2.P:4.2.0 - Cross-Side Fields That Must Stay Split

These fields are current episteme-publication precision vocabulary for `DRR`, architecture, and pattern-drafting work.
They exist to prevent one sentence from mixing FPF-side use-boundary, project-side records, actual work or action, method selection, carrier access, and authority records.
They are local recovery aids, not FPF kinds, not record kinds, and not a universal record ontology.
Each field closes only by naming the FPF kind named by value, relation record, relation phrase, project-side FPF kind and reference named by value, or explicit non-use disposition that is current in the sentence.
The same local-aid rule applies to neighboring field names such as `sourceRelationClass`, `explanationSourceRelationClass`, `comparativeRelationClass`, `representationValidityUseBoundaryValue`, `allowedUse`, `misuseRisk`, and `worldContactPolicy`: they help record a local recovery or reader-use boundary, but they do not become kinds. These local fields do not instantiate evidence, gate, assurance, work, commitment, speech act, decision, release, authority, representation kind, world-contact kind, or policy kind. Read `allowedUse` as a local reader-fit field under `declaredUseBoundary`, not as permission, evidence relation, or authority.

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `FPF` as episteme | The whole `FPF` is a claim-bearing episteme with publications, parts, patterns, pattern sections, `DRR`s, and companion publications and documents named for source, evidence, architecture, or review use. | A file, repository, taxonomy, pattern-language metaphor, or packet-local summary by default. |
| FPF pattern | A named FPF pattern: a reusable episteme species that gives action guidance for a problem situation. It is applied in a current problem situation. | Any recurring arrangement, procedure, method call, route, cluster label, checklist, or document named only as a citation or source-finding pointer. |
| pattern section | Either a part of the pattern episteme or a bounded `PublicationUnit` of that pattern publication, depending on sentence function. State which one matters when the distinction carries a claim. | Independent pattern, file location, generic locus, or record with named authority-reference relation. |
| accepted campaign `DRR` | A campaign decision source that states accepted content decisions for one campaign. | A pattern, current-authority summary, open-ended plan, review log, or replacement for pattern text. |
| `relationClaimSlice` | Empty, or a local note that `A.6.P` relation precision is current for one sentence. It must name the relation problem being handled: relation, comparison, dependency, support, sameness, grounding, mapping, endpoint claim, or cross-context bridge claim. The recovery then names `RelationKind`, `QualifiedRelationRecord`, relation phrase, candidate-set note, or bridge card when current, with typed endpoints, slots, qualifiers, and scope. | Dictionary replacement, one new umbrella kind, a bare `RelationKind` standing in for a relation record, a generic relation slot, support relation by default, or a list left as the final answer. |
| `declaredUseBoundary` | The declared use boundary and blocked use outside that boundary when the sentence says what declared use boundary applies to a use, act, claim, or reliance. Use A.6.B when the boundary claim needs L-, A-, D-, and E-claim separation. | Generic supported use, permission-by-appearance, or visual cue or readability cue treated as use-boundary. |
| `projectSideFPFRef` | The project-side FPF kind and reference named by value when a publication, display, cue, or explanation is treated as a project-side source for work, evidence, gate, constraint, adjudication, decision, commitment, method, action invitation, assurance, or engineering justification. The field points to that kind and reference; use the relevant FPF pattern for the relation and its checks. | One slot accepting records, actions, methods, carriers, evidence, gates, decisions, assurance, and engineering justification interchangeably. |
| `rejectedOverread` | A local field naming the tempting interpretation, evidence, gate, work, permission, approval, commitment, release, safety-proof, engineering-justification, or pattern-entry interpretation that must not be granted by resemblance alone. It is valid only with the recovered relation or subject-specific source, scheme, scope, practice, or use that blocks it. It is not `U.Kind`, not a record kind, not a review-finding kind, and not a moralized defect class. | A general risk slogan, review finding, moralized "bad use", vague misuse label, or reusable FPF kind. |
| `useBoundaryTargetKind`, `useBoundaryTargetRef` | Source-local helper fields. Prefer `declaredUseBoundary`; if these fields appear in material being repaired, they name the kind and reference inside `declaredUseBoundary`, not an `A.6.P` relation slot. | A generic `supported use`, document capability, "claim outside the declared boundary", review permission, or untyped pattern assignment. |

##### C.2.P:4.2.1 - Episteme, Publication, and Carrier Distinctions

| Term | Current interpretation | Must not mean |
| --- | --- | --- |
| `U.Episteme` | Claim-bearing episteme or episteme species. Use when the value is a claim-bearing episteme that can be described, viewed, grounded, revised, published, or relied on under FPF. | File, paragraph, screen, carrier, status note, process state, or generic "content". |
| C.2.1 episteme constitution and neighboring relations | An exact episteme is identified through claim content, one exact EntityOfConcern, and one effective ReferenceScheme under `EpistemeConstitutionRelation`. Empirical grounding is a separate `EpistemeEmpiricalGroundingRelation`; describing-use viewpoint selection, E.17.0 conformance and same-individual `U.View` membership, C.29 representation, and publication or carrier relations are also separate. SlotKinds occur only inside the exact reusable `RelationSignature` that declares their participant meanings. | One universal episteme-slot tuple, card, field family, or context container. |
| `EntityOfConcern`, `EntityOfConcernRef` | The EntityOfConcern reference under `C.2.1` named by a claim-bearing episteme or episteme-lane `U.View`: entity, relation, FPF pattern, FPF publication, project episteme, project publication, project-side FPF kind and reference named by value, work or action when that work or action is itself the entity of concern, or another explicitly typed EntityOfConcern referent. Use this when the text is really about what the episteme is about. In publication-unit work, `EntityOfConcernRef` is used only through a claim-bearing episteme or episteme-lane `U.View`; it does not float as a free field on the unit. | Generic topic, local table subject, file title, reviewed publication, review packet, or review record, required project-side work, decision, action invitation, authoring work, or anything someone happens to talk about. |
| wording such as `describedEntity`, `DescribedEntityRef`, `primary described entity` | Use the exact EntityOfConcern participant and its applicable reference under C.2.1 when a claim-bearing episteme is current. Use `publicationUnitPrimaryEntityOfConcern` when one bounded `PublicationUnit` carries or exposes a claim-bearing episteme or same-individual `U.View` and the primary entity of concern must be named. | A second C.2.1 slot family, a free publication-unit field, a generic topic, a second current name, or a new ontology beside `EntityOfConcern`. |
| `publicationUnitPrimaryEntityOfConcern` | The primary entity of concern, non-claim-bearing kind named by value, topic, or subject that one bounded `PublicationUnit` is mainly about for the current use. When a claim-bearing episteme or episteme-lane `U.View` is current, this must be recoverable from the selected `EntityOfConcernRef`; otherwise name the non-claim-bearing kind named by value or keep topic and subject as plain explanatory prose. | `EntityOfConcernRef` created without a claim-bearing episteme or episteme-lane view, publication-unit title by default, authoring process, carrier identity, or reader interest. |
| `GroundingHolon`, empirical-grounding relation | The exact grounding holon and obtaining C.2.1 `EpistemeEmpiricalGroundingRelation` that maps named empirical claims of one exact episteme to the required direct observation, intervention, measurement, or test relations. | A constituent of episteme identity, a convenient source citation, an untyped entity mention, or the declaration-local `GroundingHolonSlot` used as the world-side value. |
| `U.View`, `U.EpistemeView` | Same-individual dependent membership of one already identified episteme when an exact E.17.0 `EpistemeViewpointConformanceRelation` to at least one exact viewpoint episteme obtains. A.6.3 source-to-receiving construction, describing-use viewpoint selection, publication, form, and carrier remain separate. An MVPK face can use this typing only under its exact E.17 constraints. | A UI view, reader viewpoint, screen, generic publication face, projection by default, or new claim-bearing episteme by membership alone. |
| `Viewpoint` | One exact `U.Viewpoint` episteme used as the viewpoint participant of an E.17.0 conformance relation or selected for one named describing use. Selection does not prove conformance or `U.View` membership. If source wording says “system in role,” use E.10.ROLE and recover the exact concern, object, local system-role kind, classification judgment, participant relation, or assigned System by value. | A reader opinion, episteme-identity slot, pattern-application order, publication label, carrier label, or assignment manufactured by the viewpoint phrase. |
| publication | A publishable episteme, view, record relation, act or occurrence of publishing, or publication form, depending on sentence function. Always split by kind before use. | Generic document, any public-looking file, or proof that a claim is authorized. |
| `U.EpistemePublication` (rejected spelling) | No durable kind. Recover the claim as the selected `U.Episteme`, an `EpistemePublicationRelation` occurrence or reference when availability matters, publication form, or `U.PresentationCarrier`, according to sentence function. The spelling may remain only in this rejection explanation or a negative test. | A positive object, kind, reference, field, publication identity, or carrier identity. |
| publication form | The typed form in which an episteme, view, or record is published. | The claim-bearing episteme itself, the face rendered for a reader, or the carrier holding bytes. |
| generic publication face | Reader-facing publication projection or face. It is not `U.View` by default; it becomes a view only when `E.17` or the applicable view pattern supplies that typing. | `U.View` by default, carrier, UI face, front-end display, MVPK face under E.17 constraints, or claim-bearing episteme. |
| MVPK face under E.17 constraints | `E.17` face published under MVPK constraints from a source episteme or episteme-lane view, publication viewpoint, scope, pins, and face kind. It may be a `U.EpistemeView` when the MVPK profile makes that typing current. | Generic publication face, carrier, UI face, front-end display, or proof of evidence, work, gate, or authority by presentation. |
| carrier, front-end, rendering | Publication-side or access-side bearer or display relation. Use `U.PresentationCarrier` under E.17 and E.24.PUB when that exact carrier is current; otherwise name the file carrier, transport carrier, rendering, front-end relation, access-carrier relation, or another carrier relation by sentence function. | Episteme identity, publication form, `U.View`, proof of evidence, or authority-reference relation. |
| `PublicationUnit` | `E.17.AUD`-cluster head for one bounded unit inside a publication that a person inspects as one unit: a pattern body, section, table, note, card, sheet, screen block, or another bounded publication unit whose boundary is named. A card, sheet, or screen block counts only when its boundary is inside a named publication or generic publication face and the sentence needs that bounded unit as the inspected publication unit. It is part of or bounded by the publication face that renders or locates it, whether that face is generic or published under E.17 and MVPK constraints. It may carry or expose a claim-bearing episteme, view, record, cue, or local rendered content when that carried value and relation are named, but it is not identical with the carried value. | Authoring process, review work, file, carrier, front-end, UI behavior, dashboard behavior or export behavior, whole publication architecture, `U.Episteme`, `U.View`, publication form, generic publication face, MVPK face under E.17 constraints, or "anything written". |
| project-side FPF kind and reference named by value | Evidence record, gate record, Work record, status record, commitment record, system-role-assignment record, decision record, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence reference when availability matters, status-register entry, or another project record whose FPF kind is named. | Semantic content in general, current process state, or a free-form note. |
| source document | A document named for source-use, evidence use, architecture use, or review use. Name that document use directly. | A governing source by folder proximity, the EntityOfConcern carried or exposed by that source document, or the authority-reference relation unless that relation is explicit. |
| reviewed publication, review packet, or review record | The reviewed publication named by value, review packet, review record, or bounded publication unit sent or inspected in review. | The EntityOfConcern carried or exposed by that reviewed publication, review packet, or review record, the source relation behind it, or a packet-local summary. |

##### C.2.P:4.2.2 - Trigger Boundary

Use `E.10:0.2`, `E.10:0.2a`, `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d` for lexical trigger scanning and selection of an already known applicable pattern.

This pattern is applicable after that scan only when the applicable pattern cannot yet be selected because one recovery field is still confused: source wording, claim-bearing episteme, publication construction, carrier-relation construction, project-side reliance, pattern-application wording, or use or non-use disposition.

When this pattern is applicable, do not restart from word taste. Keep the `E.10` trigger result as input and recover source-expression clarification, FPF-governed use, current episteme-publication relation set, use disposition, and remaining reader use.

#### C.2.P:4.3 - Current Preferred Vocabulary
Use `PublicationUnit` when the intended entity is a bounded, human-inspected unit inside a publication.
Do not use it for UI behavior, carrier behavior, front-end behavior, file identity, dashboard behavior, or export behavior; use `A.7`, specific carrier or front-end wording, or the applicable named FPF pattern instead.

Use the current cluster names directly: `PublicationUnit Stability Discipline`, `Local Head Restoration`, and `PublicationUnit Primary EntityOfConcern Discipline`.
When the current entity is a bounded unit inside a publication, use `PublicationUnit`; when the current entity is authoring or editing work, name that work directly.

Use EntityOfConcern, EntityOfConcernRef, and publicationUnitPrimaryEntityOfConcern when local wording means the EntityOfConcern named by a claim-bearing episteme or episteme-lane view, or the primary entity of concern stabilized by one bounded publication unit over that carried value.

For `describedEntity`, `DescribedEntityRef`, `primary described entity`, `EntityOfInterest`, or `EoIClass`, use the exact EntityOfConcern participant, its applicable `entityOfConcernRef` or `EntityOfConcernRef`, `EntityOfConcernChangeMode`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the local FPF kind named by value. Use `EntityOfConcernSlot` only while inspecting the exact reusable C.2.1 constitution `RelationSignature`; it is not an episteme field. If no claim-bearing episteme or same-individual `U.View` is current, use a non-claim-bearing kind named by value or plain `topic` or `subject` instead of inventing an `EntityOfConcernRef`.

Use ordinary `topic`, `subject`, or `local referent` only in non-normative explanatory prose where no episteme constitution or neighboring direct relation, publication construction, or authority relation is being asserted.

Do not mint any other reusable FPF name from this pattern alone. The `E.17.AUD` cluster **PublicationUnit Stability Discipline** defines and constrains `PublicationUnit`; this pattern only recovers bounded-publication-unit wording into that head and points to the cluster for its tests. FPF-governed uses keep the nearby definition or explicit publication relation set.

##### C.2.P:4.3.1 - F.18 And A.6.P Naming And Relation Interpretation For `PublicationUnit`

This is the F.18 and A.6.P name interpretation that this pattern reflects from the selected `E.17.AUD` cluster correction.
It records why `PublicationUnit` is the selected bounded publication-unit head for the `E.17.AUD` cluster, while `C.2.P` remains the epistemic precision-restoration pattern.

```text
F.18 and A.6.P naming and relation interpretation:
  Governed value and use boundary: one bounded `PublicationUnit` in a conformant FPF publication, used in authoring or review without confusing it with an episteme, view, publication form, generic publication face, MVPK face under E.17 constraints, carrier, authoring Work, or review process.
  Kind: primary-entity or local-head field for a bounded unit inside one publication.
  Purpose and use-domain: keep one human-inspected publication unit distinct from episteme, view, publication form, generic publication face, MVPK face under E.17 constraints, carrier, authoring work, and review process.
  Selected Tech label: PublicationUnit.
  Plain interpretation: bounded unit inside a publication that a person inspects as one unit.
  Candidate head families considered:
    - authoring-centered unit labels
    - reader-action-centered unit labels
    - mixed authoring-and-reader-action unit labels
    - PublicationReadingUnit
    - PublicationAuthoringUnit
    - PublicationUnit
    - ContentSpan
    - DocumentUnit
  F.18 result:
    - `PublicationUnit` has better SemanticFidelity than authoring-centered unit labels because the unit belongs to the publication lane, not to the authoring process.
    - `PublicationUnit` has better MorphologicalActionFit than mixed authoring-and-reader-action unit labels because it does not mix author action, reader action, and the unit-boundary meaning in one head.
    - `PublicationUnit` has lower AliasRisk than `content span` and `document unit` because `content` and `document` blur episteme, publication form, and carrier.
    - `PublicationUnit` still has nonzero AliasRisk because `publication` itself splits into act or occurrence of publishing, episteme publication, form, generic face, MVPK face under E.17 constraints, unit, and carrier; therefore FPF-governed uses keep the nearby definition or explicit publication relation set.
  Current result: accepted reusable FPF head for conformant episteme-publication-heavy FPF text within the declared bounded-publication-unit repair scope; use a more specific accepted head when it better names the text under repair.
```

#### C.2.P:4.4 - Epistemic Precision Restoration After E.10

Use `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d` for lexical trigger rewrite rules.

Use this pattern after those rules only when one of these remains unresolved:
- source-expression clarification versus FPF-governed use;
- source-local meaning versus current FPF wording;
- claim-bearing episteme versus publication, view, face, carrier, or publication unit;
- EntityOfConcern, grounding relation, or source-finding cue versus project-side evidence, work, gate, decision, assurance, method, action, release, or engineering justification;
- declarative FPF pattern application versus project work or control flow;
- use disposition: recovered by value, reduced-use cue, understandable FPF extension candidate, blocked use, rewrite incomplete, or not triggered;
- remaining reader use or Tech-to-Plain mapping after epistemic precision repair.

When none of these remains unresolved, apply the pattern named in the matching `E.10` row.

#### C.2.P:4.5 - Rewrite Execution Modes
Use the smallest sufficient mode that preserves the distinction. The template is an epistemic precision device, not a form to fill for every ordinary wording cleanup.

##### C.2.P:4.5.1 - Local prose cleanup

Use this mode when the phrase under repair is non-normative local prose and does not carry ontology, authority, review scope, release state, use-boundary, or a reusable name.

Action: rewrite directly or leave it unchanged. No table row is required.

##### C.2.P:4.5.2 - Compact epistemic precision-restoration row

Use a compact row for ordinary architecture, source-ref target, or review-use document cleanup where a sufficient FPF kind, relation record, relation phrase, or tuple-like record can be recovered without minting a new FPF head.

```text
Compact epistemic precision-restoration row:
  file path, if current:
  FPF pattern, if current:
  pattern section, if current:
  sentence reference:
  phrase under repair:
  current sentence function:
  selected FPF kind named by value or project-side FPF kind:
  `relationClaimSlice` triggered? yes or no
  relation problem, if triggered:
  declaredUseBoundary triggered? yes or no
  projectSideFPFRef triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    endpoint, slot, qualifier notes:
    useBoundaryTargetKind:
    useBoundaryTargetRef:
  if a local source, scheme, scope, practice, or use distinction is current:
    FPF-side kind, reference, or relation:
    project-side FPF kind, if current:
    project-side reference named by value, if current:
    notTriggeredReason:
  replacement:
  remaining reader use:
  distinction disposition: preserved, split, intentionally retired, still missing
```

##### C.2.P:4.5.3 - Full epistemic precision-restoration check

Use the full check when the wording may change ontology, introduce or retire a reusable head, change a claim-bearing pattern or document named for source, evidence, architecture, or review use, reviewed publication, review packet, review record, or review state, or resolve a contested source-meaning problem.

```text
Epistemic precision-restoration check:
  file path, if current:
  FPF pattern, if current:
  pattern section, if current:
  sentence reference:
  phrase under repair:
  sentence function:
  distinction carried:
  E.10 head kind and EntityOfConcern and Description-episteme boundary and specification use interpretation:
  F.18 naming result: no stable term, reuse, MintNew sketch, DocumentLegacy
  F.18 candidate head families, if naming is current:
  F.18 lexical Q result, if naming is current:
    SemanticFidelity:
    CognitiveErgonomics:
    MorphologicalActionFit:
    AliasRisk:
  A.6.P trigger? yes or no
  relation kind, slots, and qualifiers recovered with A.6.P, if current:
  claim-bearing episteme current? yes or no
  FPF kind and relation set:
  C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme; separate grounding, describing-use viewpoint selection, view conformance, or representation relation, if current:
  E.17 and MVPK publication form, generic face, MVPK face under E.17 constraints, view, carrier split:
  PublicationUnit typing, if any:
  FPF-side or project-side sentence:
  `relationClaimSlice` triggered? yes or no
  relation problem, if triggered:
  declaredUseBoundary triggered? yes or no
  projectSideFPFRef triggered? yes or no
  relation claim? yes or no
  if relation claim:
    RelationKind:
    QualifiedRelationRecord slots:
    useBoundaryTargetKind:
    useBoundaryTargetRef:
  if a local source, scheme, scope, practice, or use distinction is current:
    FPF-side kind, reference, or relation:
    project-side FPF kind, if current:
    project-side reference named by value, if current:
    notTriggeredReason:
  rejectedOverread, if current:
  project-side record, work, action, method, carrier crossing:
  heterogeneous-list classification: one kind under repair, relation set, tuple-like record, alternative cases, failed ontology, not triggered
  pattern application, project work, decision distinction:
  chosen rewrite:
  remaining reader use:
  distinction disposition: preserved, split, intentionally retired, still missing
  unrecovered wording retained? no, yes, with scope and reason:
  use disposition: recovered by value, extension candidate, reduced-use cue, blocked use, rewrite incomplete, not triggered
```

##### C.2.P:4.5.4 - Epistemic Precision-Restoration Note

Use an epistemic precision-restoration note only when wording carries ontology, authority, evidence, or use-boundary claim. The note records the original phrase, recovered FPF kind or relation, reference named by value when current, project-side FPF kind and reference when current, remaining reader use, and disposition: recovered by value, extension candidate, reduced-use cue, blocked use, rewrite incomplete, or not triggered.

#### C.2.P:4.6 - Ordinary Completion and Reopen Boundary

A `C.2.P` application is complete for ordinary pattern-authoring use when the smallest sufficient product is present:

1. `E.10` trigger result is kept as input and the text does not restart from word taste;
2. the wording is either left ordinary, repaired locally, expressed as a compact epistemic precision-restoration row, or escalated to the full check because the claim being made requires it;
3. the recovered episteme, publication, view, face, carrier, publication unit, EntityOfConcern, grounding relation, project-side reference, or use disposition is named by value;
4. every relation-like slice that remains current is assigned to `A.6.P` or its retained specialization, rather than being hidden inside this pattern;
5. the remaining reader use survives in ordinary prose or the wording is explicitly demoted to reduced-use cue, blocked use, rewrite incomplete, or not triggered.

Use the lowest sufficient product. A clean sentence is enough when one sentence recovers the claim being made. Use a compact row when the reader must inspect one recovered kind, relation, or disposition later. Use the full check only when several fields are current, when source wording's FPF use is contested, when a durable name may be minted, or when a publication, carrier, or project-side overread would otherwise survive.

This pattern can be applied to its own wording at the same lowest sufficient mode. If `C.2.P` text itself blurs a source expression, publication construction, pattern application, relation slice, or project-side reliance claim, repair that local wording here; do not create a recursive pattern-quality apparatus.

Reopen or lower a prior `C.2.P` repair when one of these content discoveries appears:

- the replacement head is another umbrella word such as `support`, `display`, `route`, `kind`, `object`, `record`, `map`, or `mapping` without FPF kind named by value and boundary;
- the repaired wording is type-correct but no longer tells the working reader what action, non-use, or neighboring-pattern application remains;
- a neighboring pattern now applies to the current evidence, assurance, gate, work, decision, publication, architecture, structure, relation, or naming claim;
- an entry cue, ToC row, summary, dashboard, retrieval snippet, or source-relation note preserves the pre-repair broad interpretation after the pattern body was repaired;
- repeated use shows that authors are filling the full check where a local sentence or compact row would suffice.

The ordinary stop condition is local: once the current sentence or bounded publication unit preserves kind, relation, use disposition, and remaining reader use, stop. Do not keep improving wording merely because a more elaborate record could be filled.

### C.2.P:5 - Archetypal Grounding

| Scenario | Show - failure without C.2.P | Show - repair with C.2.P |
| --- | --- | --- |
| FPF pattern prose | A pattern section, row, or source line appears to support an action. The reader cannot tell whether the sentence is about applying a pattern, a section as `PublicationUnit`, a document, a file, or a relation. | Name the object and sentence function that matter. Keep an ordinary pattern-use claim when that is all the sentence says; narrow it to source-finding when the publication only helps navigation; use the named FPF pattern when its definition, constraint, or test carries the action claim. |
| Engineering project publication | A green dashboard tile, certificate badge, or generated explanation is treated as evidence, gate passage, engineering justification, assurance, or permission for work. | The engineer names the generic publication face, MVPK face under E.17 constraints, or carrier, then names the one project-side FPF kind and reference that carries the downstream claim: evidence record, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `B.3` assurance or engineering-justification record, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, or `U.MethodDescription`. The next action is orientation or source-finding only, or finding or creating the named evidence, gate, decision, assurance, plan, work, method, or invitation before work or reliance proceeds. Choose one current value, not the list. |
| Source-wording or source-relation text | A source note says that material supplies a claim without naming the recovered field: pattern application, selected source `U.Episteme`, publication occurrence when availability matters, publication form or carrier, relation record, or project-side FPF kind and reference. | State the recovered field and sentence function. Apply the relevant FPF pattern or cite the selected source episteme, publication occurrence, or relation. If the meaning remains unclear, reduce the phrase to source-finding or block its claim-bearing use. |
| Pattern-control wording | A text says that one pattern routes into another, calls another pattern, exits to a pattern, or chains patterns. The reader may treat pattern application as executable process control. | If the sentence is about applicability, say that a practitioner uses or applies the pattern in the problem situation. If it is about project activity, name the action, work, method, decision, or invitation needed for that claim. Add the acting `U.System`, `U.MethodDescription`, `U.Method`, dated `U.Work`, or separate decision and invitation identities only when their distinction changes the claim or its later use. |
| Architecture or structure wording | A source says an architecture description, structure representation, design rationale, or structural view carries a claim, but the sentence does not show whether the use under repair is a described holon, architecture description, structure, structural view, relation, publication face, or carrier. | `C.2.P` first recovers the source expression, source-relation function, and publication and carrier relation set. If the architecture claim, structure kind, structure relation, view, publication relation, or source relation is still hidden, use `C.30.P`; if it is already recoverable, use `C.30`, `C.30.ASV`, `A.22`, `C.31`, or the applicable architecture or structure pattern. Use `A.6.P` for relation-like wording. |

#### C.2.P:5.1 - Boundary and Anti-Cases

| Boundary case | C.2.P result | Why this protects use |
| --- | --- | --- |
| Ordinary reader help | The sentence says a note helps a reader find another section, with no evidence, authority, use-boundary, work, gate, decision, or project reliance claim. Leave ordinary wording ordinary or make one local wording repair. | Keeps ordinary prose affordable; `support` as ordinary help is not forced into a record. |
| Relation-only support wording | The sentence says one claim, source description, grounding relation, evidence record, assurance record, causal-use relation, mathematical-lens relation, characteristic relation, declared-use boundary, work relation, or publication-companion use warrants another claim, and source-relation use or publication construction is already clear. Apply `A.6.P`; no C.2.P recovery is needed. | Prevents this pattern from absorbing relation precision restoration. |
| Known FPF kind named by value | The sentence already names the project-side FPF kind and reference, such as an evidence path, gate decision, decision record, work occurrence, assurance record, or architecture pattern application. Apply the named pattern without an intermediate C.2.P step. | Avoids a needless logical hop and keeps the relevant neighboring-pattern application intact. |
| Source phrase without recovered FPF-governed use | Source wording is interesting but its FPF kind, relation, or use disposition cannot be recovered. Keep it as reduced-use cue or block its FPF use. | Preserves source meaning without guessing FPF meaning. |
| Replacement head is another umbrella | A proposed repair changes `support` to `basis`, `display` to `face`, or `route` to `path` while the kind and relation are still hidden. Mark repair incomplete. | Blocks lexical churn and forces the kind named by value, relation, and declared use boundary to be recovered. |
| Apparatus too heavy | A one-sentence local repair is replaced by a full record, checklist, and source note with no additional declared use boundary. Use the local sentence or compact row instead. | Keeps first-use cost and maintenance cost inside the quality claim. |

#### C.2.P:5.2 - Transfer Coverage

`C.2.P` is intentionally narrow but must transfer across three recurrent publication situations:

- FPF-side drafting: pattern text, DRR text, source-relation notes, review-use notes, and pattern draft prose;
- project-side publication: dashboards, explanations, cards, documents, front-ends, rendered files, and generated summaries used around evidence, work, gates, decisions, assurance, or methods;
- external source-expression clarification: seminar fragments, papers, reviews, standards, and tool outputs being clarified before possible FPF use.

In all three situations the same invariant holds: before accepting the wording as current FPF text, recover the distinction between source wording and current FPF wording, claim-bearing episteme, publication construction, carrier-relation construction, relation-like slice, the applicable neighboring pattern for any non-C.2.P field, and remaining reader use.

### C.2.P:6 - Bias-Annotation

| Lens | Risk | Mitigation |
| --- | --- | --- |
| Ontology | Precise-looking words become a new parallel ontology. | Require recovery to current FPF kinds and relations before reuse. |
| Usability | The rule becomes too heavy for ordinary edits. | Use the smallest sufficient rewrite mode; reserve the full check for FPF-governed wording. |
| Preservation | Source-relation or source-ref target text is mistaken for direct pattern authority. | Keep source-related statements separate from the ordinary pattern guidance. |
| Checklist ritual | The rule becomes a form to satisfy rather than a wording action to perform. | Put the action in `Solution`; use row evidence only when wording has FPF-governed use. |

### C.2.P:7 - Conformance Checklist

| Item | Check |
| --- | --- |
| CC-C2P-1 | Every FPF-governed broad head names the recovered FPF kind, relation record, relation phrase, tuple-like record, project-side FPF kind and reference named by value when `projectSideFPFRef` is current, or explicit non-use disposition. The selected project-side entry must be one named kind under repair, such as `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, `A.15.1` dated `U.Work` occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence path, typed evidence record, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, carrier relation, front-end relation, or not-triggered alternative. |
| CC-C2P-2 | Slash compounds and heterogeneous lists are not left as final kinds unless they are accepted tokens, carrier syntax, plain synonym pairs with no FPF-governed use, or explicitly recovered tuple-like constructions or relation constructions. |
| CC-C2P-3 | FPF pattern-application claims and project-side publication, record, work, method, carrier, and action claims stay separated when both are current. |
| CC-C2P-4 | Broad use-boundary, source wording, source-relation use, publication-face, carrier, placement, movement, procedure-like, topic-like, pre-FPF sign, or publication wording requires epistemic precision restoration when it carries ontology, authority, evidence, or use-boundary claim. Relation-support wording belongs to `A.6.P` unless the publication or source-relation construction is itself unresolved. |
| CC-C2P-5 | Unclear meaning is not rewritten by guesswork; it is classified as reduced-use cue, blocked use, or understandable FPF extension candidate. |
| CC-C2P-6 | Any newly stable name passes `F.18`; any relation claim passes `A.6.P`; any use-boundary claim fills `declaredUseBoundary` and uses `A.6.B` when L-, A-, D-, and E-claim separation is current; any claim-bearing episteme, episteme species, episteme-lane view, or project-side FPF kind and reference passes `C.2.1` or the applicable named FPF pattern as needed; any publication, view, or carrier claim passes `E.17.0`, `E.17`, and MVPK as needed. |
| CC-C2P-7 | The final text remains action guidance under `E.2` `P-2` and `E.12`: it tells the author what wording action to take, what overread to block, why the distinction still matters to the working reader, and what remaining reader use or FPF pattern application remains. When both Tech and Plain registers are current, the Plain or didactic line maps back to the recovered Tech interpretation under `E.10:6.2`. |
| CC-C2P-8 | This pattern does not rename existing FPF patterns or mint reusable heads without `F.18` and `A.6.P`. |
| CC-C2P-9 | The smallest sufficient product was used: local sentence repair, compact epistemic precision-restoration row, full check, or explicit non-use disposition. A full check is not required when a local sentence or compact row preserves the current distinction. |
| CC-C2P-10 | The repair names a lowering or reopen condition when it is used as reusable guidance, when it changes entry or projection wording, or when the result is claimed as a stable pattern-body repair. |
| CC-C2P-10a | Epistemic `source data` and `source material` close their source expression, episteme or publication occurrence, and source-to-use relation first. Treat a separate work-side relation and its claim posture with the applicable pattern; stop when both are already readable, and apply `A.6.P.WMR` only while either remains hidden. Physical raw material stays in its physical constituent, affected-referent, resource-use, supply, transfer, or transformation relation. |

#### C.2.P:7.1 - Current Scan Boundary

Use `E.10:0.2`, `E.10:0.2a`, `E.10:0.2b`, `E.10:0.2c`, and `E.10:0.2d` for lexical trigger scanning.

`C.2.P` conformance begins only when the `E.10` result is `epistemic precision restoration required` or `combined precision restoration required`, or when non-FPF source text is being unpacked before possible FPF transfer.

Do not copy the `E.10` trigger list into this pattern as a second registry. Use the `E.10` result as input and recover source-expression unpacking mode, FPF-governed use mode, current episteme-publication relation set, use disposition, and remaining reader use. When the relation-bearing slice is current, `A.6.P` remains a separate required precision-restoration pattern.

### C.2.P:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Avoidance |
| --- | --- | --- |
| Token swap | Replace `display` with `face` or `host` with `file` without recovering kind and sentence function. | Apply head-kind and relation recovery before rewriting. |
| Group-kind list | Leave a list such as `pattern, record, relation, or action` as if the list names one kind. | Decide whether the sentence needs one kind, a relation record, a tuple-like record, alternative cases, or a blocked ontology. |
| Type-correct but inert rewrite | All overread is removed, all heads are typed, and no practical guidance remains: the reader can see that local checks passed but cannot tell why the distinction matters, what to do, or which FPF pattern application or project-side FPF kind carries the claim being made. | Recover the didactic or recognition function in wording whose claim being made is recovered through the named FPF pattern, keep any Plain line mapped to the recovered Tech interpretation when both registers are current, state the remaining reader use, or demote the phrase to reduced-use cue, blocked use, or rewrite incomplete instead of pretending the repair landed. |
| Expressive overread rebound | A repair restores practical guidance with a memorable Plain or didactic line, but that line carries a claim not recoverable from the Tech fields, named FPF kind, recovered relation, project-side reference, disposition, or pattern application. | Map the line to the recovered Tech interpretation under `E.10:6.2`; use the FPF pattern that defines, constrains, or tests the claim; or demote the phrase to reduced-use cue, blocked use, or rewrite incomplete. |
| Pillar-blind precision pass | A broad cleanup proves trigger removal and kind recovery, but never checks whether `E.2` `P-2`, `E.6`, `E.8`, or `E.12` still let the intended reader see the working situation, why it matters, and what first useful move remains. | For FPF-governed Problem frames, Problem sections, recognition texts, examples, and worked slices, state the remaining reader use or FPF pattern application. Preserve intentional didactic metaphors when they are ordinary recognition aids or when their claim being made maps back to Tech. If the didactic function was harmed, repair the Plain wording so it maps back to the recovered Tech interpretation, or mark the rewrite incomplete instead of accepting type-correct but inert wording. |
| Source-companion header leakage | Carry a source-companion header into a pattern and let `Authority: none` or `Current use` define the new pattern. | State the pattern-use claim and authority claim in the pattern header and relations. |
| Pattern as procedure | Say the pattern is called, routed, invoked, or chained as if it were executable code. | Say that a practitioner uses or applies the pattern in a problem situation. If actual project activity is claimed, name the relevant work occurrence, method, decision, or action invitation; add actor or `U.MethodDescription` identity only when it changes the claim or its later use. |
| Strength metaphor | Say a claim is strong or weak without a characteristic, threshold, evidence class, scope, gate, or use-boundary relation. | Name the comparison characteristic, threshold, evidence class, scope, gate, or use-boundary relation, or replace the metaphor with the recovered use-boundary relation. |

### C.2.P:9 - Consequences

| Benefit | Trade-off and mitigation |
| --- | --- |
| Prevents parallel episteme and publication ontology from entering FPF-governed wording. | Adds a small recovery step before apparently simple rewrites; mitigate by using the smallest sufficient mode. |
| Preserves accepted glossary and rules without turning source-related statements into accidental pattern authority. | Requires a clear separation between pattern guidance and source-related statements. |
| Makes unclear meaning fail closed. | Some attractive phrases will not be accepted until their kind or relation is actually recovered. |
| Improves DRR and pattern drafting discipline. | Authors must resist convenient lists and umbrellas when one kind named by value or relation is needed. |

#### C.2.P:9.1 - Operating Consequence
For new episteme-publication precision prose:
- start from FPF kinds and relations, not from familiar publication nouns and document nouns;
- use `PublicationUnit` for bounded publication units;
- use the exact `EntityOfConcern` participant and its applicable reference when a claim-bearing episteme is current, and translate `describedEntity` source wording to the adopted EntityOfConcern family before FPF-governed use closure;
- keep publication form, generic publication face, MVPK face under E.17 constraints, view, carrier, document named for source, evidence, architecture, or review use, reviewed publication, review packet, review record, or review state, and project-side FPF kind and reference named by value separate;
- name `relationClaimSlice`, `declaredUseBoundary`, and `projectSideFPFRef` separately when more than one is current;
- classify heterogeneous kind lists before writing a sentence that depends on them;
- say that FPF patterns are applied in problem situations, not called or routed as procedures;
- leave accepted FPF names untouched unless a separate accepted naming decision authorizes a rename.

Operationally, each rewrite should:
- separate FPF-side epistemes and publication or use relations from project-side epistemes and their publication or use relations whenever both are present;
- name `relationClaimSlice`, `declaredUseBoundary`, and `projectSideFPFRef` separately when a publication, display, cue, or explanation is treated as evidence, gate, constraint, adjudication, decision-making reliance, work permission, assurance, or engineering justification;
- classify heterogeneous lists before naming them: one kind under repair, relation set, tuple-like record, alternative cases, not-triggered alternatives, or failed ontology;
- say that FPF patterns are applied in problem situations, while project records, publications, views, carriers, and actions are worked with in project practice;
- avoid strength metaphors unless the characteristic, scale, threshold, evidence class, or use-boundary relation is named.

For cleanup of existing conformant texts:
- do not do a global string replacement;
- classify each unclear term occurrence by the smallest sufficient rewrite mode;
- use the full epistemic precision-restoration check only when ontology, reusable naming, FPF pattern text, or source-bearing project text is current;
- do not rename accepted FPF patterns from this pattern alone.

### C.2.P:10 - Rationale

FPF already contains the relevant ontology. The recurring defect was not lack of concepts but ad hoc wording that bypassed them: `source`, `target`, `display`, `object`, `host`, `route`, `supported use`, and similar trigger terms packed several FPF kinds and relations into one convenient phrase; they are examples of wording to unpack, not current replacement vocabulary.

The correct repair is therefore not a new umbrella. It is a disciplined recovery action: use `E.2`, `E.10`, `F.18`, `A.6.P`, `A.7`, `C.2.1`, `E.17.0`, `E.17`, and MVPK together until the sentence says which EntityOfConcern, relation, publication, view, carrier, record, work, action, or pattern application it means.

Because every normative FPF pattern must satisfy `E.2`, epistemic precision is not a value apart from `P-2 Didactic Primacy`. A stricter repair has not landed if it turns reader-facing problem text into a kind inventory with no working situation or first useful move. The remedy is recognition wording whose claim remains recoverable through the Tech interpretation or a named FPF pattern application, with a declared-use boundary when that boundary matters.

The detailed rules remain in ordinary pattern sections, so the pattern is usable as FPF guidance rather than as an external glossary container.

### C.2.P:11 - SoTA-Echoing

`C.2.P` does not claim to replace semiotics, terminology science, document engineering, or ontology engineering. Its claim being made is narrower: episteme-publication-heavy conformant text must recover accepted FPF kinds and relations before it is rewritten, so that episteme, publication, view, carrier, naming, relation, and project-side records are not replaced by ad hoc words.

A full external SoTA comparison is not needed for this bounded architectural precision-restoration pattern. A reduced external practice set is still required to check terminology drift and epistemic precision restoration. It sharpens only the recovery discipline, creates no new ontology, and does not outrank the FPF patterns named below.

In this section, `SoTA-Echoing` means compatibility with current FPF ontology and selected external practice anchors, not that those anchors are sufficient SoTA for every field. ISO terminology entries are standards anchors for designation practice; SHACL-style validation is only a fail-closed constraint analogy; word-sense and ambiguity-resolution practice is used only for context-sensitive sense recovery. If one of those domains becomes the object of a future claim, use its current SoTA pattern or source review.


| Reduced source idea | Adapted FPF invariant | Rejected shortcut | Recovery section |
| --- | --- | --- | --- |
| ISO 704:2022 and ISO 1087:2019 terminology work distinguishes the entity under discussion, the concept used in a terminology system, the definition, the designation, and term-formation practice. | Recover the FPF kind, relation, and sentence function before accepting a rewritten phrase. Use external terminology work only as external corroboration for careful designation and definition practice. | Do not replace FPF episteme and publication ontology with an ISO concept system, a dictionary substitution, or a global class row. | `C.2.P:4.1`, `C.2.P:4.4`, and `C.2.P:10` |
| SHACL-style constraint validation makes local constraints explicit and fail-closed when a data shape does not satisfy them. | Treat the epistemic precision-restoration record as a local fail-closed recovery check when the FPF kind, relation, or declared use boundary cannot be recovered. | Do not import SHACL ontology, machine-validation authority, or shape vocabulary as FPF pattern ontology. | `C.2.P:4.0a`, `C.2.P:4.2`, and `C.2.P:8` |
| Word-sense disambiguation and ambiguity-resolution practice treats sense recovery as context-sensitive rather than solved by the most common word sense. | When one local head or qualifier carries several plausible senses, recover the local FPF context and the applicable named FPF pattern before choosing wording. | Do not import machine-learning benchmarks or treat common usage as proof that the local FPF sense is recovered. | C.2.P:4.4, C.2.P:4.1.2, E.17.AUD.LHR, and F.18 |

**External-practice boundary.** External traditions enter only through the local FPF invariant named by value they sharpen. Object-oriented modeling and OWL-style ontology modeling do not become the default repair for vague FPF wording. Architecture-description standards help keep views, viewpoints, concerns, and descriptions explicit. Explainability and NLP faithfulness work helps prevent explanation laundering. RAG evaluation helps separate retrieval evidence, source availability, and answer trust. Quality-diversity and multi-objective search help avoid premature scalarization in candidate selection. None of these traditions becomes FPF ontology, FPF authority, or a universal pattern-quality benchmark.

#### C.2.P:11.1 - Relevant FPF Patterns

The current FPF corpus already has patterns that contribute to this discipline:

- `E.10` supplies the head-kind, term, morphology, register, and forbidden-umbrella discipline.
- `E.10.D2` gives the "thing vs words vs rules" discipline and the carrier humility rule.
- `F.18` gives the local-first naming protocol: governed value and kind; the pattern and contribution that define or constrain them; by-value scheme; local-sense claim; intended use; candidate comparison; and any separately obtaining relation.
- `A.6.P` gives the relation-precision restoration method: restore generic head kind, build candidate sets for endpoint kinds and relation kinds, select kind-explicit slots and qualifiers, then allow guardrailed wording.
- `C.2.1` gives episteme identity through exact claim content, EntityOfConcern, and effective ReferenceScheme and keeps empirical grounding and edition continuity as distinct direct relations.
- `A.7` keeps EntityOfConcern, Description episteme, and publication carrier distinct.
- `E.17.0`, `E.17` distinguish views, viewpoints, MVPK faces, publication forms, and publication projections.
- `A.15.4` shows how to keep an encountered publication, display, or low-articulation cue distinct from the project-side FPF kind and reference used for work or reliance.
- `A.16`, `A.16.0`, `A.19`, `B.2.5`, `C.27`, and `A.3.3` provide the movement, control, and temporal machinery used when episteme-publication prose talks about route, trajectory, movement, cadence, or dynamics.
- `E.19` already treats terminology and sentence-level precision restoration as required review checks, not editorial polish.
- `A.6.A` carries action-invitation discipline when a publication, representation, or cue invites an action without itself becoming authority, evidence, gate passage, or work completion.
- `C.11` carries decision-making and decision-record discipline when the question under repair is a decision rather than generic action.
- `A.15` and `A.15.4` split system-role kind and assignment, Method, WorkPlan, and actual-Work alignment from appearance-based reliance repair; do not use `A.15` as a universal repair for episteme-publication wording.
- `E.9` is the campaign `DRR` pattern for campaign-level content decisions; `E.11` is only for entry-discoverability situations and must not organize an episteme and publication repair by default.

These internal FPF patterns remain primary:

| Claim need | Relevant FPF pattern(s) | Alignment with C.2.P | Adoption result |
| --- | --- | --- | --- |
| Head-kind discipline | `E.10` | Use head-kind recovery before accepting a phrase. | Adopt. |
| Stable naming | `F.18` | Run a name card when a reusable head is being minted. | Adopt. |
| Relation precision | `A.6.P` | Recover relation kind, endpoints, slots, qualifiers, and scope when a relation or use-boundary claim is current. | Adopt. |
| Carrier and EntityOfConcern-description humility | `A.7` | Keep EntityOfConcern, Description episteme, and carrier apart before treating a publication as evidence, work, gate, or authority. | Adopt. |
| Episteme and publication ontology | `C.2.1`, `E.17.0`, `E.17`, MVPK | Separate episteme, publication, view, generic publication face, MVPK face under E.17 constraints, publication unit, carrier, and rendering. | Adopt. |
| Project-side downstream use | `A.6.A`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`, `C.11` | When a publication, display, cue, or explanation is treated as evidence, gate, decision, work permission, method, assurance, or engineering justification, name the applicable FPF pattern and the project-side FPF kind and reference. | Adopt. |

This reduced external-practice set changes the Solution in one practical way: epistemic precision restoration cannot close merely because the replacement sounds cleaner. The FPF kind, relation, declared use boundary, and any needed pattern application must be recoverable by value; otherwise the wording is blocked or becomes a candidate for a separate FPF-kind decision.

#### C.2.P:11.2 - E.19 Review Profile Carry-Through

Run `PCP-TERM` when the repair changes episteme-publication-heavy naming, umbrella words, slash compounds, trigger-word replacements, or relation wording.

Run `PCP-BRIDGE` when the repair imports terms, claims, norms, or authority expectations between named sources, practices, disciplines, reference schemes, publication forms, or project record kinds.

Run `PCP-ENTRY` only when the repair changes which FPF pattern a working reader should apply in a problem situation. Do not use `PCP-ENTRY` as a substitute for the epistemic precision restoration itself.

Run `PCP-PRAG` when the repair changes reader action, practical payoff, or what the working reader can safely do next. A type-correct but inert repair fails this line even when every recovered kind is technically right.

When the repair changes evidence, proof, witness, grounding, explanation, gate, release, or engineering-justification claims, apply the relevant FPF pattern (`A.10`, `E.17.EFP`, `A.20`, `A.21`, `B.3`, or another applicable pattern) and select the current `E.19` profile by the changed claim. Do not mint a local evidence-review profile inside `C.2.P`.

### C.2.P:12 - Relations

* **Builds on:** `E.2` Pillars, especially `P-2 Didactic Primacy`; `E.10`, `E.10.ARCH`, `A.7`, `F.18`, `A.6.P`, `C.2.1`, `E.17.0`, `E.17`, MVPK, and `A.6.A`.
* **Coordinates with:** `E.6`, `E.7`, `E.8`, `E.9`, `E.12`, `E.19`, `A.10`, `A.15`, `A.15.4`, `B.3`, `A.20`, `A.21`, `A.6.F`, `A.6.P.WMR`, `A.6.3.CSC`, `A.6.3.CR`, `A.6.3.RT`, `C.30.P`, `C.16.P`, `C.16.Q`, `E.17.EFP`, and `E.17.ID.CR`.
* **Does not replace:** `E.10` general lexical rules, `F.18` naming protocol, `A.6.P` relation precision, or local episteme and publication patterns. It says when those patterns must be applied to episteme-publication-heavy wording.

### C.2.P:End

