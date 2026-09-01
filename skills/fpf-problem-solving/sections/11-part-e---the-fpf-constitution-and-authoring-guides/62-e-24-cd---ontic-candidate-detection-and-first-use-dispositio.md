## E.24.CD - Ontic Candidate Detection and First-Use Disposition

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.CD:0 - Use This When

Use this pattern when a recurring word, card, table, schema, diagram, record, draft pattern row, or field bundle looks like a new FPF subject and the author must decide what to do next.

Typical moments:

- one word such as "process", "source", "quality", "architecture", "problem", "view", the unqualified word "role", "function", "mechanism", or "method" points to several FPF objects or claims at once;
- several patterns repeat a similar declaration, participant list, or relation rule;
- a project data structure looks concept-shaped, although it may be only a claim-bearing episteme, publication form, representation, or local record;
- a draft ToC row names a family that no current pattern yet governs;
- a proposed `U.*` kind feels useful, but it may duplicate a current kind or direct relation.

**Primary EntityOfConcern.** When the author records this choice in a C.2.1 episteme, its EntityOfConcern is the subject already identified under a direct pattern. If that subject cannot yet be identified, use the source episteme or expression entity whose inquiry remains open. The visible form and the note recording the disposition are not substitutes.

**First useful move.** Write one plain sentence: “For this work or decision, we need to know or do `<action>` about `<subject>`.” Then ignore the wrapper long enough to recover the subject, the needed claim, and the current pattern that defines or constrains it. Apply the first truthful disposition in section 4.

**What goes wrong if missed.** FPF grows shadow ontology. A table becomes a kind; a field label is mistaken for a relation-participant meaning; a filled field is treated as an actual relation participant merely because it occupies a column; a card becomes the subject; or a convenient word creates a second ontology over values and relations that already have subject patterns.

**What this buys.** The author identifies one usable subject pattern without filling a candidate record or maintaining a registry. A genuine durable ontic must still pass E.24's full identity and relation test; simpler cases stop with their subject pattern, local classification, description or publication handling, wording repair, or a precise unresolved question.

**Not this pattern when.**

- If one existing subject pattern already states the needed claim, use it directly.
- If a local kind, criterion, candidate judgment, or extension is already the question, use `C.3`, `C.3.1`, and `C.3.2`.
- If the current question is a description episteme, use `C.2.1` for its identity and the subject-specific description pattern when one applies. For view membership, publication form or occurrence, representation, or carrier, use `E.17.0`, `E.24.PUB`, or `C.29`.
- If the subject and governing claim are clear and only the wording hides them, use `E.10`, `E.10.ARCH`, or the applicable precision-restoration pattern.
- If a durable ontic has already been selected, use `E.24`; if a durable public `U.*` kind is separately at issue, use `E.24.UK`.
- If the work is comparing architecture alternatives, construct the evaluation through `A.19.ECS`.

### E.24.CD:1 - Problem Frame

An apparent ontology candidate usually arrives inside something visible: a label, form, record, diagram, source passage, or repeated field list. That visible thing may point to a real durable subject, but it may instead carry claims about several already governed objects, publish or represent them, classify them for one context, or merely use an imprecise word.

E.24.CD governs this first-use choice before E.24 opens. It neither admits a durable ontic nor creates a candidate object of its own.

### E.24.CD:2 - Problem

Without an explicit first-use disposition:

1. **Publication forms become false subjects.** A card, table, or schema receives ontology authority because it is visible.
2. **Local classification hardens into public ontology.** A criterion useful in one context is treated as a durable FPF kind.
3. **Subject patterns are bypassed.** Existing methods, work, relations, epistemes, structures, sources, and results are duplicated under a new head.
4. **Wording repair becomes ontology creation.** A broad word is replaced with a new broad word while the actual subject and predicate remain hidden.
5. **Candidate work becomes a registry ritual.** Authors fill fields or scores for possible ontics instead of deciding the current case.

### E.24.CD:3 - Forces

| Force | Tension |
| --- | --- |
| Early recognition vs premature ontology | A recurring concern should be noticed, but recurrence alone must not mint a durable subject or `U.*` kind. |
| Visible form vs governed subject | A form can reveal the problem while remaining an episteme, publication form, representation, carrier, or local record. |
| Direct reuse vs shared coordination | Existing patterns should carry their own claims; E.24 opens only when dependent patterns need one stable subject identity and minimal relation set. |
| First-use affordability vs adequate discrimination | The author needs a quick choice, but the choice must still separate direct use, local classification, publication, wording, and durable admission. |
| Traceability vs registry growth | A disputed choice may need one explanatory sentence; it does not need a standing candidate catalogue. |

### E.24.CD:4 - Solution

Start from the work that is blocked, not from the shape of the source material.

Ask these four questions in order:

1. **What must the next person do or decide?** Name the comparison, classification, publication, repair, decision, or other practical use.
2. **What is that use about?** Name the subject, claim, or source expression without treating its card, row, filename, diagram, or field bundle as the answer.
3. **Which current pattern already governs the needed claim?** Name the predicate or judgment that would let the work proceed.
4. **If that pattern does not close the case, what is actually missing?** State one applicable pattern or one precise unresolved stop below.

#### E.24.CD:4.1 - Apply the first truthful disposition

Plain `situation`, `incident`, `current configuration`, `operating <system>`, and `emergency` are recognition cues, not kind names. Recover only the subjects, claims, and relations that the receiving work actually needs.

| Current need | Next use | Stop that follows |
| --- | --- | --- |
| One current subject pattern already states the needed claim or action. | Apply that subject pattern. If the missing piece is a relation-bearing claim that no current direct predicate closes, apply `A.6.RCD` before proposing a relation kind. | Do not create an ontic, kind, candidate note, or disposition record. A local compound claim or predicate-definition episteme is neither a relation kind nor an occurrence; only a separately justified kind candidate proceeds through `E.24` and `E.24.UK`. |
| One exact ClaimGraph forms one claim-bearing whole about one truthful exact EntityOfConcern under one effective ReferenceScheme. | Use `C.2.1` to identify that episteme. Other independently governed objects may be designated inside its claims without becoming extra EntityOfConcern fields or ontic slots. | If one truthful EntityOfConcern or one identity-bearing ClaimGraph cannot be recovered, keep the epistemes separate. State a collection, publication, representation, or other use relation only when its own predicate obtains; common use or co-publication does not identify one episteme. |
| Wording such as `situation`, `incident`, `current configuration`, `operating <system>`, or `emergency` groups several cues. | Recover the exact systems or holons, characteristic or state claims, actual part relations, and only the temporal or causal relations needed by the current use. Add actual `U.Transformation` or `U.Work` only when independently grounded under `A.3.4` or `A.15.1`. Use a possible-state episteme when possibility is the subject, and a separate C.2.1 description episteme only when claim-bearing orientation is current. | Their conjunction is neither `U.Situation` nor `U.IncidentSituation`. An episteme's EntityOfConcern and any grounding holon in a separately current `EpistemeEmpiricalGroundingRelation` neither identify the world-side subject nor become mandatory fields. Stop decomposition once the action-facing distinction needed by the receiving use is recovered. |
| A proposed subject exists only as an arbitrary fusion, co-presence, connected set, or chosen boundary. | Reject the bundle without forcing it through a construction record. If a constructed object survives as the current subject, apply `B.1`, `A.14`, and `C.13`, and apply `B.2` only when whole reidentification is current; recover its exact construction inputs, whole-forming relations, and identity rule. | Fusion, co-presence, connectedness, and a selected boundary alone form no durable whole. The no-mint result does not block a genuinely irreducible subject later shown to have its own identity and obtaining laws. |
| Repeated typed reasoning needs a local criterion, candidate judgment, or true-candidate set for one context slice. | Use `C.3`, `C.3.1`, and `C.3.2`. | The local kind, `KindSignature`, judgment, and optional extension stay distinct; neither a public `U.*` kind nor a classification-relation occurrence follows. |
| A card, record, table, diagram, file, or schema carries claims, is used as a description, conforms to a viewpoint, expresses an edition, represents something, or bears a form. | Use `C.2.1` to identify an episteme only when its constitution test passes. If it describes a method, structure, relation occurrence, or another subject, apply that subject's description pattern. Use `E.17.0` for actual view membership, `E.24.PUB` for publication, and `C.29` for representation and correspondence. Several patterns can apply because they govern different objects or relations. | Visible shape does not identify the described subject or make any neighboring relation obtain. |
| A path, table, dashboard, schema, or other declarative form seems to authorize, dispatch, prove, prescribe, or perform something by its shape. | Use `C.2.P.DR` to name the visible expression, recover the direct object or relation, state its representation or correspondence use—or `none`—and block the unsupported action claim. | A declarative form does not itself authorize or dispatch work, perform an action, or grant authority. |
| Words such as `relation`, `slot`, `field`, `interface`, bare *role*, `function`, or `endpoint` still leave the object or claim unclear. | Use E.10.ROLE first for bare *role*; continue to A.6.RSIR when it denotes relation participation, a declaration place, an interface place, or a representation position. Use A.6.F for function wording and A.6.P or the pattern for the recovered relation. Then stop at that pattern. | An engineering word creates no subject kind, relation kind, participant, declaration, system-role kind, or assignment. |
| The subject and governing claim are already clear, but a word or phrase compresses them. | Repair the bounded wording through `E.10`, `E.10.ARCH`, or the applicable precision-restoration pattern. | A clearer name does not create a new subject, relation, or kind. |
| An already governed value needs a stable reusable name rather than a repaired sentence. | Use `F.18` after recovering the value, its kind and subject pattern, its effective reference scheme, and the local sense to be named. For relation-facing wording, settle any missing direct relation through `A.6.RCD` first. | A label or `NameCard` neither admits the value or a public kind nor makes a relation obtain. |
| One blocked use concerns an independently recoverable candidate, proposal, or source construct; named consumers show concrete cross-pattern duplication or disagreement pressure; and one obvious direct route does not close it. | Open `E.24` and transfer only those detection facts. Let E.24 test identity, the minimal relation set, dependent reliance, non-duplication, and non-use. | E.24.CD neither requires those settlement results nor admits or rejects the ontic. A still-missing identity or relation rule can reach E.24's unresolved branch. |
| The subject, needed claim, or subject pattern cannot yet be recovered. | Keep the inquiry attached to the source expression or blocked work and name what is missing. | Do not hide non-settlement inside a candidate record, score, provisional `U.*` name, or “future ontology” list. |

When a durable public `U.*` kind is also proposed, `E.24.UK` returns its separate admission result. If the ontic and kind are both new, use the atomic co-decision already defined by E.24 and E.24.UK; neither result proves the other.

#### E.24.CD:4.2 - Recover objects hidden by a visible form

For a project card, row, schema, or diagram, inspect only what the current work consumes:

1. Which filled statements are claims, and what is each claim about?
2. Which entities or non-entity values are independently identified under their direct patterns?
3. Which direct predicates are asserted, what are their actual participants, and which independently established facts satisfy their obtaining conditions?
4. Is the visible arrangement a publication form, a C.29 representation, a carrier, or merely a local layout?
5. Does the work need local classification of a candidate, or only a claim about an already governed feature?
6. What stronger reading must be blocked—for example, record existence creates performed work, a row creates membership, or a field name admits a kind?

A field label is not a `SlotSpec`. `A.6.5` governs the declaration: a reusable `SlotSpec` appears only inside a `RelationSignature` for an already recovered direct relation and only when a named later use needs that declaration. A row value is not an actual relation participant merely because it occupies a column.

#### E.24.CD:4.3 - Open E.24 when cross-pattern pressure is concrete

Open E.24 when these detection facts are recoverable:

- one blocked use or decision;
- one independently recoverable candidate entity, proposal episteme, or source-construct entity that carries the inquiry without presupposing a durable ontic;
- concrete duplication or disagreement pressure in more than one current pattern description;
- the named consumers that make shared coordination plausible; and
- why one obvious direct-pattern route does not already close the blocked use.

Transfer those facts to E.24. E.24—not E.24.CD—tests the complete identity or constitution rule, minimal direct-relation set, dependent reliance, non-duplication, practical gain, and nearest non-use boundary. If one of those facts cannot be established, E.24 may return its unresolved result. Detection therefore does not require the author to settle the candidate before opening the settlement pattern.

A plainly direct case still stops at its subject pattern. Repeated words, several source forms, copied fields, or a useful schema can prompt inspection, but without a blocked use, an independently recoverable inquiry subject, concrete cross-pattern pressure, named consumers, and failure of an obvious direct route, they do not open E.24.

#### E.24.CD:4.4 - State one result and stop

Most cases need only one sentence:

> For `<work or decision>`, apply `<subject pattern>` to `<exact subject or claim>` because `<decisive fact>`; `<blocked stronger reading>` does not follow.

When no pattern can yet apply truthfully, say:

> For `<work or decision>`, leave `<exact subject or claim question>` unresolved because `<missing subject, predicate, or subject pattern>`; `<blocked stronger reading>` does not follow.

Use a longer explanation only when another author must understand a disputed disposition. Do not create an `OnticCandidateCluster`, candidate registry, scorecard, or mandatory disposition form. Once the applicable pattern or unresolved stop is stated, continue there; reopen E.24.CD only if the recovered subject or practical use changes.

### E.24.CD:5 - Archetypal Grounding

#### E.24.CD:5.1 - A candidate that genuinely opens E.24

Before `C.2.1`, “description”, “view”, “claim set”, and “publication” repeatedly pointed to a claim-bearing object used across many patterns. The practical need was stable claim identity across description, evaluation, reference, and publication work. Existing patterns could not supply that shared identity and relation set independently.

That case opens E.24. E.24 then decides the durable ontic; C.2.1 governs the resulting `U.Episteme`; E.17.0, E.24.PUB, F.18, and C.29 keep viewpoint conformance, publication, naming, and representation separate. Cards and files do not become the episteme.

#### E.24.CD:5.2 - Local cooling-pump classification

A maintenance team repeatedly asks whether Pump #14 counts as a cooling pump in plant slice S-14. Pump #14 and its flow, heat-transfer, and operating-state features already have direct governors. The needed outputs are a reusable local criterion and a candidate judgment, not a durable ontology unit.

Apply C.3.2. A `KindSignature` may declare the criterion for repeated use; the judgment can be `true`, `false`, or `unknown`; a current extension is materialized only for a named set-consuming use. A measurement supports a claim about Pump #14's features but does not create its membership.

#### E.24.CD:5.3 - Problem card

A `ProblemCard@Context` under `C.22.2` is a problem-side episteme. It may carry a signal, hypothesis, forecast, scenario, anticipated-condition claim, affected-entity reference, evidence cue, constraint, proposed direction, assignment cue, source reference, or gate cue without creating an actual Problem.

An actual Problem is one obtaining `ProblematicForRelation` under `C.22.PFR`. A card may assert that exact predicate, but it may designate a current Problem occurrence only after C.22.PFR independently establishes the actual-condition relation, criterion-applicability relation, adverse truth, and occurrence identity. Signals, hypotheses, forecasts, scenarios, anticipated conditions, and reviewable formulations remain under `C.22.2` or their exact forecast, scenario, temporal, or causal governor.

For a repair decision, keep the affected entity, evidence-use relation, any current local system-role kind and classification judgment, any exact obtaining system-role assignment, any separately governed responsibility relation, source-use relation, and gate or decision claim under their subject patterns. Apply `E.18.1`, `E.23`, and the exact Work, search, evaluation, or continuation pattern when repeated problematization or later action is current. Neither the card nor its acceptance or publication creates or ends an actual Problem. Open `E.24` only if a different reusable subject-identity or relation gap remains after these direct claims are recovered; do not rediscover the actual Problem as a new ontic.

#### E.24.CD:5.4 - Record-shaped false candidate

A project schema contains:

```text
ChangeItem:
  status:
  owner:
  method:
  mechanism:
  evidence:
  result:
  target:
  source:
```

Treat the schema as source material, not as an ontology. A proposal episteme, method, mechanism declaration, work plan, intended-work claim, performed-work occurrence, holder system, state claim, evidence item, result, affected referent, and source remain different objects. Recover only those that the meeting actually uses:

| Field cue | Object and relation to recover |
| --- | --- |
| `owner` | Apply E.10's bounded `owner` recovery, then name the exact recovered relation and participants, ordinary or quoted non-use, or blocker. An established architectural owner—for example, the module designated for one functional-architecture object—keeps that direct architecture relation. Organizational, policy, source-maintenance or stewardship, legal ownership, responsibility, authority, and commitment uses keep their own recovered relations. Only a claim actually recovered as work-facing local classification or assignment proceeds through E.10.ROLE to A.2 or A.2.1. The field alone creates no System, kind, assignment, ownership occurrence, responsibility, or authority. |
| `status` | Name the exact bearer and the governed state or status value, claim, gate disposition, decision result, or other current relation. Field presence implies no readiness, validity, gate passage, work authorization, or release. |
| `method` and `mechanism` | Keep an admitted `U.Method` and any qualifying `U.MethodDescription` distinct from the A.6.1 `U.Mechanism` declaration episteme and its declared operation family. If the field concerns one use, identify the exact operation application and only its declaration-local argument or result bindings that obtain. If it concerns realization, identify the realizing entity and the obtaining mechanism-realization relation. Apply `A.6.1` when the row does not yet distinguish these readings. Shared wording identifies none of them. |
| plan, intended work, and actual work | Keep a `U.WorkPlan` or intended-work claim under `A.15.2`. Add a `U.Work` under `A.15.1` only for an independently grounded performed occurrence, whether ongoing with an open end or completed. A proposal, row, trace, or completion label does not make work occur. |
| `evidence` | First identify what the field points to; do not rename it to fit a pattern. Keep its direct kind: an episteme or evidence record, a carrier, the work that produced or interpreted evidence, a currentness relation, or a provenance relation. If it is an episteme and the meeting asks only about its bounded evidence-use or status-use for the claim, use `A.2.4` first. Use `A.10` when the evidence path must be retraceable; include only the record, carrier, work, currentness relation, and provenance relation needed for this claim. Use `B.3` only when a separate assurance claim is current. The field proves neither the claim nor the row's status. |
| `result` | Identify the result entity, value, or result episteme independently, then state the exact production, measurement, evaluation, decision, delivery, acceptance, or other result relation actually claimed. A result label creates no generic result object or relation. |
| `target` | Identify the affected referent and state an exact work-to-referent, change, effect, or other subject relation only when current. The field does not make the referent a work participant or changed entity. |
| `source` | Identify the source episteme or expression and the exact source-use relation. Source presence is not evidence, authority, or currentness by itself. |

Not every row has every listed object, not every filled field is claim-bearing, and co-presence in one row does not constitute a larger subject. The filled row is one C.2.1 episteme only when one exact ClaimGraph forms a claim-bearing whole about one truthful exact EntityOfConcern under one effective ReferenceScheme. Otherwise keep the epistemes separate and state only the exact collection, publication, representation, or meeting-use relation that actually obtains.

The column arrangement is a publication form only when selected to express an identified episteme for the meeting. The form is not a `U.ChangeItem`, and its columns are not ontic slots. If the project later needs a local kind of records for a query, `C.3.2` may classify those records as records. If several FPF patterns later demonstrate a different shared durable subject with its own identity and minimal relation set, that evidence can reopen `E.24`; the schema's shape cannot.

#### E.24.CD:5.5 - Current configuration around a holon

A maintenance review asks about “the current configuration around Pump #14.” Identify Pump #14 under its system governor, then recover only the characteristic or state claims, actual part relations, temporal phase, and other direct relations that the maintenance decision uses. If the work compares a possible configuration, identify the possible-state episteme and its direct state or configuration claims rather than asserting current actuality.

A separate C.2.1 description episteme may provide claim-bearing orientation. Its exact EntityOfConcern and any grounding holon in a separately current `EpistemeEmpiricalGroundingRelation` neither identify Pump #14 nor turn the surrounding claims into one world-side object. The holon and those current relations answer the question; their conjunction is not `U.Situation`.

#### E.24.CD:5.6 - Operating pump with connected parts

Pump #14 is operating while a sensor, valve, and controller are connected. `Operating` first cues a governed state claim; it does not establish `U.Work` or `U.Transformation`. Connectedness does not establish parthood. Identify the pump and connected entities, state the exact connection relations, and use `A.14` only for part relations whose predicates actually obtain.

Add dated maintenance or control `U.Work` only after every precise performer has an A.13 core and A.15.1 independently identifies the Work's performance history, Method, time, containing System, and performers. Add F.6 only when the recovered situation account also needs precise assignment-bound attribution. A local system-role kind and its classification remain separate. A short situation-recovery sentence may omit identifiers its receiving use does not need. If maintenance or control is merely intended, keep it as an A.15.2 WorkPlan or other modal claim; it creates neither Work nor assignment. Add an actual bounded change under `A.3.4` only when its changed referent, boundary, conditions, and change facts obtain. No bundle of system, state, connection, work, and change becomes a situation entity.

#### E.24.CD:5.7 - Multi-party emergency

An emergency report mentions a leaking vessel, an overheated subsystem, a suppression system, and response teams. Recover each participating System and each actual change separately. For every dated response claimed as `U.Work`, recover each precise performer's A.13 core and independently admit the occurrence under A.15.1 as stated in `E.24.CD:5.6`; add F.6 only when the current account also needs exact assignment-bound attribution. Keep any local system-role classification separate. Keep an intended response as a plan or other modal content until it occurs. State temporal relations through their temporal patterns and a causal relation through `C.28` only when that claim is current and supported.

Use a C.2.1 emergency-description episteme only when the receiving work needs claim-bearing orientation across those objects. The emergency word, the record, and the co-presence of several systems and works identify neither `U.IncidentSituation` nor another bundled whole. Stop decomposition once the response decision has the exact subjects and relations it needs.

#### E.24.CD:5.8 - Mathematical inconsistency under a declared formal substrate

Two specification epistemes state constraints that cannot both hold under one declared `FormalSubstrate` and applicability. Identify the exact claims or epistemes, name that formal substrate, and state the exact inconsistency or consequence relation under its direct formal governor. Use `C.29` only when the formalism is also being used as a mathematical lens for another declared use.

The formal relation may guide a later decision or repair-work occurrence, but it establishes no project-world event, work, transformation, causal relation, adverse episode, actual Problem, or situation entity. Formal consequence is not causation. Inconsistent descriptions do not make their world-side subjects inconsistent without a separately governed bridge claim. If the exact relation or substrate cannot be named, leave the formal claim unresolved rather than letting the word `inconsistency` stand for it.

#### E.24.CD:5.9 - Architecture diagram

An architecture diagram may carry claims about selected structures of one holon. If the diagram is selected as one claim-bearing whole, C.2.1 identifies that episteme. The same episteme has `U.View` membership only when E.17.0 conformance obtains; its publication form and carrier use E.24.PUB; selected graphical elements use C.29 only with explicit correspondence to independently recovered objects.

The diagram does not become the architecture, structure, or ontic by being visible. If the current work is simply to correct one architectural claim, apply the architecture and structure patterns directly.

#### E.24.CD:5.10 - Broad source word

A source says that a method “supports” production. If the author can recover a specific required-effect, method-use, work-enactment, capability, evidence-use, or other direct claim, apply its subject pattern. If the source word still compresses several claims, use E.10 and E.10.ARCH to retain it only with its bounded meaning or in quote-only or reduced use.

Do not open E.24 merely because `support` recurs, and do not invent `SupportRelation` as the candidate.

#### E.24.CD:5.11 - Score table and characteristic space

A score table can serve as the publication form of an evaluation-result episteme over a `U.CharacteristicSpace`, or it may be only a local report. Use A.19 when the characteristic space itself must be identified and A.19.ECS when the work is constructing the evaluation characteristics for a contested comparison. Use C.29 when readers calculate, compare, infer, navigate, or inspect through the table's mathematical structure and those available operations matter.

The table does not admit `U.CharacteristicSpace` by appearance and does not require another candidate ontology beside the current A.19 subject pattern.

### E.24.CD:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Epist**, **Prag**, **Did**.

This pattern intentionally biases toward early recovery of the real subject and the blocked work. It resists:

- **publication-form bias:** treating a card, schema, table, or record as the subject matter;
- **wording bias:** treating a repeated word as a kind or relation decision;
- **registry bias:** collecting possible ontics instead of disposing the current case;
- **scoring bias:** rating a candidate before its subject, identity rule, direct relations, and practical use are known;
- **semio-bias:** discussing forms and labels while the governed subject and claim disappear.

The mitigation is concrete: name the work, subject, needed claim, pattern that states it, applicable disposition, and blocked stronger reading. Open E.24 only when several named patterns need the same subject identity or relation rules.

### E.24.CD:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24CD-1` | The first-use disposition starts with a recognizable work or decision and the subject or claim that blocks it. |
| `CC-E24CD-2` | A visible card, row, schema, diagram, filename, or field bundle is not treated as the subject merely by form. |
| `CC-E24CD-3` | Independently governed objects and direct predicates are recovered before a new ontic or kind is proposed. |
| `CC-E24CD-4` | A current subject pattern is applied when it already closes the needed claim. A relation-bearing claim that no current predicate closes goes through A.6.RCD; a local compound claim or predicate-definition episteme is not thereby a relation kind or occurrence. |
| `CC-E24CD-5` | One C.2.1 episteme requires one exact ClaimGraph, one truthful exact EntityOfConcern, and one effective ReferenceScheme. Otherwise epistemes remain separate, and co-use or co-publication supplies no shared identity. |
| `CC-E24CD-6` | Local classification uses C.3.2's kind, signature, judgment, and optional extension distinction and does not imply a public `U.*` kind or direct classification relation. |
| `CC-E24CD-7` | Episteme, view membership, publication form, representation, carrier, and publication occurrence remain separate and use their subject patterns only when current. |
| `CC-E24CD-8` | E.24 opens from a blocked use, an independently recoverable candidate, proposal, or source construct, concrete duplication or disagreement pressure across named patterns, named plausible consumers, and failure of one obvious direct route. E.24.CD does not require the identity rule, minimal relation set, dependent-use proof, non-duplication result, practical gain, or nearest non-use; E.24 owns those judgments and may return unresolved. |
| `CC-E24CD-9` | Any public U-kind question is handled by E.24.UK as a separate admission result; E.24.CD admits neither ontic nor kind. |
| `CC-E24CD-10` | No candidate cluster, registry, scorecard, or mandatory disposition form is created. |
| `CC-E24CD-11` | The result names the exact pattern applied to the exact subject or claim, or a precise unresolved stop, and blocks the strongest tempting overread. |
| `CC-E24CD-12` | A record-shaped false candidate keeps holder, status bearer and value, method, mechanism, plan, work, evidence item and use, result and relation, target and subject relation, and source and source-use relation distinct; absent fields and row shape establish none of them. |
| `CC-E24CD-13` | Bare *role* uses E.10.ROLE and then the recovered branch; ambiguous relation, slot, interface, function, and endpoint wording uses its matching precision-restoration pattern. None becomes ontology by wording alone. |
| `CC-E24CD-14` | Declarative-form agency is blocked through C.2.P.DR, and reusable naming starts in F.18 only after the governed value and any needed relation settlement are available. |
| `CC-E24CD-15` | Wording such as `situation`, `incident`, `current configuration`, `operating <system>`, or `emergency` recovers only the Systems, claims, Work, change, and temporal or causal relations needed by the current use; their conjunction creates neither `U.Situation` nor `U.IncidentSituation`. Every asserted actual Work first recovers each precise performer's A.13 core and is independently admitted under A.15.1 from its performance history, Method, time, and containing System. F.6 is added only when precise assignment-bound attribution is also current; local system-role-kind classification remains separate. Intended action stays plan or other modal content until its predicates obtain. |
| `CC-E24CD-16` | Arbitrary fusion, co-presence, connectedness, or a chosen boundary creates no whole. Only a surviving constructed-object candidate is tested for exact inputs, whole-forming relations, and identity under B.1, A.14, C.13, and B.2 when reidentification is current. |
| `CC-E24CD-17` | Mathematical inconsistency names exact claims or epistemes, the declared formal substrate, and the direct inconsistency or consequence relation; it establishes no world event, causation, Work, Transformation, Problem, or situation. |
| `CC-E24CD-18` | A ProblemCard, signal, forecast, scenario, formulation, actual Problem, and later problematization or work remain under C.22.2, C.22.PFR, and their exact continuation governors rather than one card-derived ontic. |

### E.24.CD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Card-to-kind jump | A useful card is promoted into a `U.*` kind because it has repeated fields. | Recover its claims, subject, form, and carrier; use C.2.1 or E.24.PUB as triggered. |
| Structural U-kind jump | A heading, title, filename, or ToC row keeps `U.*` because the spelling is convenient. | Recover the subject and use E.24.UK for the admission question; naming follows the result. |
| Column-to-participant jump | A field label is treated as a relation-participant meaning, or a filled field as an actual participant; either is called a `SlotSpec` because of column position. | Recover the direct predicate, its relation-participant meanings, and its actual participants first. Keep the field as a representation element or participant designation; under `A.6.5`, declare a `SlotSpec` only inside a needed `RelationSignature` for that already recovered relation. |
| One-word candidate | A broad word is renamed and treated as settled. | Recover the subject and predicate; use E.10 and E.10.ARCH when only wording remains. |
| Local-kind inflation | A useful project criterion is promoted to durable public ontology. | Use C.3.2 and keep the local kind, declaration, judgment, and extension distinct. |
| Registry trap | The author keeps a list of possible ontics without deciding the blocked case. | State the work, apply one truthful subject pattern or name one precise unresolved stop, and stop. |
| Scoring before identity | A score form is filled before the subject and direct relation gap are known. | Recover the subject, identity rule, dependent uses, and missing coordination; use A.19.ECS only for an actual comparison. |
| Repetition-as-admission | Several forms or patterns share a label, so an ontic is inferred. | Require the E.24 entry facts: one subject identity and minimal relation set reused by named dependent patterns. |
| Negative-catalogue repair | The text lists only what the candidate is not. | State the positive subject, claim, governor, next action, and one blocked stronger reading. |

### E.24.CD:9 - Consequences

Positive consequences:

- authors reach a subject pattern from a recognizable work situation;
- durable ontics are proposed from an identity and reuse gap rather than from form or vocabulary;
- local classification, claim coordination, publication, representation, and wording remain cheaper dispositions;
- cards, records, tables, and schemas remain useful source material and detection cues without becoming ontology by appearance;
- no candidate registry or score ritual is added to routine authoring.

Costs:

- the author must recover the subject and needed claim before choosing a subject pattern or unresolved stop;
- some attractive names are lowered to local kinds, source wording, epistemes, publication forms, or representations;
- a genuine durable candidate still requires the full E.24 decision and, when current, a separate E.24.UK admission result.

### E.24.CD:10 - Rationale

Ontic candidates rarely arrive as pure ontology. They appear through the forms people use: project tables, cards, schemas, diagrams, source packets, draft rows, examples, and repeated words. Those forms reveal working concerns, but they do not decide what exists, what relation obtains, or what FPF kind is needed.

The pattern therefore asks for one first-use disposition instead of a candidate record. Keep direct claims in their direct patterns; use C.2.1 only when one exact ClaimGraph, one truthful EntityOfConcern, and one effective ReferenceScheme constitute an episteme; and use C.3.2 for local classification. Keep publication in E.24.PUB and representation in C.29. Use C.2.P.DR to block action inferred from declarative form; resolve ambiguous wording through A.6.RSIR, A.6.F, A.6.P, or E.10; and name only an already governed value through F.18. Open E.24 only when named dependent patterns need one stable subject identity and minimal relation set that those simpler applications cannot preserve.

This order keeps the first move affordable and falsifiable. Another author can see which fact selected the applicable pattern or unresolved stop and which stronger reading was blocked. A list of candidate fields or scores would make the form look authoritative and invite optimization of the record instead of settlement of the subject.

### E.24.CD:11 - SoTA-Echoing

| Source family | Current lesson for E.24.CD | FPF decision |
| --- | --- | --- |
| Shimizu and Hitzler 2024, and Eells, Dave, Hitzler, and Shimizu 2024. | Current modular-ontology and micropattern work favors ontology units that are understandable, extensible, aligned, reusable, and small enough to assemble. | Inspect repeated subject identity and direct-relation rules across named dependent uses; do not treat word frequency, common nouns, or record fields as admission evidence. |
| Norouzi, Hertling, Waitelonis, and Sack 2025. | Current process-ontology ODP extraction work shows that process-like and workflow-like forms can expose implicit design patterns that domain experts need to examine. | Recover the objects and predicates hidden by process, record, card, and field-list forms and check them against their subject patterns; do not reopen transformation-flow decisions or import imperative motion metaphors. |
| Nayyeri et al. 2025, and Oyewale and Soru 2026. | Current data-model-to-ontology and enterprise-KG work shows that schemas, documentation, relations, provenance, and validation can reveal ontology candidates while also encouraging schema-shaped overreads. | Treat project databases, tables, schemas, and enterprise data models as source material and detection cues for selecting the applicable subject pattern, not as ontology decisions; require bounded scope, agreement with each current subject pattern, and expert validation. |
| CYC microtheory line. | Lineage-only caution: context-bounded knowledge modules are a useful analogy for contradiction locality and scope-bounded ontology fragments. | Do not cite CYC as current decisive support for FPF ontic design and do not import CYC architecture as FPF law. |
| OWL, SKOS, RDF, and triple-store practice. | Infrastructure and expression lineage: these lines carry ontology descriptions, vocabulary links, queries, and serialization forms. | Use them as expression and publication caution only; they do not substitute for `U.Ontic`, do not show that labels are ontology, and do not answer FPF ontic modularization by themselves. |

Smallest source-currentness reopen trigger: reopen this SoTA slice when a newer ontology-engineering or data-model-to-ontology source changes the selected criteria for reusable subject identity, minimal relation sets, bounded scope, validation, or source-form overread; do not reopen it merely because a new vocabulary, serialization, or KG tool appears.

### E.24.CD:12 - Relations

- **Builds on:** `E.24` for durable ontic settlement; `E.24.UK` for separate public U-kind admission; `C.2.1` for exact episteme constitution; `C.3`, `C.3.1`, and `C.3.2` for local typed projection; `E.24.PUB` for publication; `C.29` and `C.2.P.DR` for representation and declarative-form overread; `A.6.5` for `SlotSpec` declaration and participant-designation discipline; `A.6.RSIR`, `A.6.F`, `A.6.P`, `E.10`, and `E.10.ARCH` for bounded ambiguity repair; and `F.18` for naming after the governed value is settled.
- **Coordinates with:** `A.6.RCD` when the missing piece is a relation-bearing claim that no current direct predicate closes. A local compound claim or predicate-definition episteme is neither a relation kind nor an occurrence; only a separately justified kind candidate proceeds through `E.24` and `E.24.UK`. It also coordinates with `E.17.0` for actual view membership; `A.1`, `B.1`, `B.2`, `A.14`, and `C.13` for a surviving constructed-whole question; `A.3.4`, `A.15.1`, the temporal patterns, and `C.28` for actual change, work, temporal, and causal claims; `A.6.0` and `C.29` for formal-substrate and mathematical-lens use; `C.22.PFR`, `C.22.2`, `E.18.1`, and `E.23` for actual Problem, problem-side formulation, and later problematization; `A.19` for `U.CharacteristicSpace`; and `A.19.ECS` for evaluation-characteristic construction.
- **Used by:** DRRs and authoring work that must decide whether a recurring construct uses an existing subject pattern, remains one or several bounded epistemes, becomes a local typed projection, applies description or publication handling, receives wording repair, opens E.24, or remains unresolved.

### E.24.CD:End

