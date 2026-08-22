## A.6.H - Wholeness Language Unpacking — RPR-WHOLE

> **Type:** Relational-precision specialization
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**At a glance.** Use A.6.H when words such as *whole*, *part*, *integrity*, *complete*, *turnkey*, or *end-to-end* hide the exact object or relation on which a decision depends.

**Use this when.** Enter after A.6.P:4.11 has recovered the concrete candidate objects and the sentence needed by the receiving use, and that sentence genuinely asks about a whole, part, structure, integrity, coverage, or completion. A.6.H helps the practitioner expose the candidate whole or other bearer, its boundary when relevant, the independently identified parts or constituents, and the exact direct claim together with the rule that defines, constrains, or tests it.

**Not this pattern when.** Do not enter merely because a source contains a trigger word. Apply `C.16.P`/`C.16` when the current question is characteristic or measurement, `A.10`/`B.3` for evidence use or assurance, `C.2.1` for episteme identity or edition, `E.17`/`E.24.PUB` for publication, and the applicable A.3/A.15 rule for Method, WorkPlan, or Work. Keep using A.6.P when the candidate objects or the receiving sentence are still unknown.

**What goes wrong if missed.** A situation record, diagram, bundle, adjective, phase label, or coverage slogan becomes the supposed whole or relation. Parts, members, portions, phases, method factors, Work parts, evidence, and measured characteristics are then silently treated as one generic “part of” claim.

**What this buys.** A short identity-first repair from overloaded prose to one or more direct claims with exact participants and, when needed, PatternID locators for their definitions or tests—or to an explicit blocker when a needed predicate is absent.

**What changes in practice.** The practitioner stops annotating a wholeness bundle and instead writes the few direct sentences the next decision consumes: which entity, which relation and participants, which rule defines or tests that claim, and which stronger inference remains blocked.

### A.6.H:1 - Problem frame

Natural language compresses several different engineering questions into the same small vocabulary:

- What individual is being treated as one whole?
- Where is its boundary, and what lies outside it?
- Which independently identified objects are parts, constituents, members, portions, or proper temporal restrictions?
- Which relations among those objects actually obtain?
- Does a named use need a construction trace or a selected structure?
- Is the same whole being recognized again, or must it be reidentified?
- Is “complete” about performed Work, capability, specification, evidence, or another exact coverage claim?
- Is “integrity” a measured characteristic, an assurance claim, or a claim that an assembled entity remains one whole?

Those questions have different participants, predicates, and subject patterns. A.6.H does not answer them by creating a common wholeness object. It keeps the source wording readable while making the load-bearing claims exact.

A word is load-bearing here when a requirement, invariant, interface statement, architecture choice, model relation, decision, test oracle, assurance use, or downstream action depends on its interpretation. `E.10` is the pattern for shared wording-use discovery. A.6.H begins only after the current wholeness-family claim has been selected by value.

### A.6.H:2 - Problem

Without an exact-object discipline, the following failures recur:

1. **Candidate-whole ambiguity.** “The whole system” is asserted before one candidate entity, boundary, or identity rule is recoverable.
2. **Reference-level drift.** One noun phrase alternates among a referent, a claim-bearing episteme, a publication form or carrier, intended Work, performed Work, and evidence.
3. **Parthood overload.** Physical components, conceptual constituents, collection members, measured portions, and temporal restrictions are written as one generic inclusion.
4. **Order-as-structure.** A method factor, step description, plan item, or performed occurrence is treated as a component because a diagram places it inside a box.
5. **History-as-parthood.** A `v2`, revision, edition, shift, retry, or monitoring window is routed through `PhaseOf` before episteme identity or Work-temporal law is applied.
6. **Construction-by-list.** A list of objects, repeated trace, or selected diagram is treated as proof that one whole or direct relation obtains.
7. **Coverage-as-wholeness.** “Complete”, “turnkey”, or “end-to-end” is treated as a whole-level property without a scope, covered items, direct coverage or completion predicate, or current Work state.
8. **Integrity collapse.** A measured characteristic, security or data-integrity term, evidence report, assurance claim, and structural-whole claim are all forced through mereology.
9. **Change-by-vocabulary.** Generic verbs such as *recompose*, *rephase*, or *recomplete* replace the exact changed object and direct changed relation.

The practical failure is non-decidability: another reader cannot tell which object is at issue, what relation is claimed, what evidence would bear on it, or which stronger use is blocked.

### A.6.H:3 - Forces

| Force | Tension |
| --- | --- |
| Conversational economy vs. recoverability | Ordinary prose needs compact words, while a load-bearing use needs exact objects and relations. |
| Whole recognition vs. relation truth | Recognizing one candidate whole does not establish its parts, structure, integrity, or completion. |
| Stable identity vs. change | A useful history needs continuity, while changed epistemes, Work occurrences, and replaced carriers must not be collapsed. |
| Structural description vs. performed reality | Method descriptions, plans, diagrams, and evidence can guide work without becoming the performed occurrence or its parts. |
| Minimal apparatus vs. downstream assurance | Most cases need one readable direct claim; some need a construction trace, selected structure, measurement chain, or assurance relation. |
| Cross-domain wording vs. subject patternship | *Module*, *pipeline*, *team*, *integrity*, and *complete* travel across domains, but their governed objects do not merge. |

### A.6.H:4 - Solution

#### A.6.H:4.1 - Entry and result contract

Enter with:

- one exact sentence or decision that depends on wholeness-family wording;
- the concrete candidate objects recovered under A.6.P:4.11;
- the receiving use that would change if the wording were read differently; and
- any already known definition, constraint, or test and its PatternID locator when that reference must travel.

Return one of:

1. one or more readable direct claims, each naming the predicate or claim family, ordered participants, material qualification, and the PatternID locator when its defining or testing content must be cited;
2. one concrete next action for a still-current measurement, evidence-use, episteme, publication, Method, plan, Work, production, or completion question: apply the named rule when its entry holds, or stop when no such question remains; or
3. an A.6.RCD `missing-governor[...]` result naming the exact participants, proposed predicate, affected use, and absent definition, applicability, or occurrence-identity rule. Name a future pattern or declaration need only when one is actually identifiable.

When evidence cannot yet select among several readings, keep the candidate objects, discriminating questions, and blocked receiving use explicit in ordinary prose. Do not turn that temporary uncertainty into a `wholenessSituation`, card, bundle, lifecycle record, or new U-kind.

#### A.6.H:4.2 - Apply the exact-object sequence

Use the following sequence only as far as the current sentence requires:

1. **Recover the working question.** State what a reader must decide, do, accept, measure, rely on, start, continue, or stop. The cue word selects no branch.
2. **Name the subject and reference level.** Distinguish the referent entity, claim-bearing episteme, publication occurrence, publication form, presentation carrier, Method, MethodDescription, WorkPlan, performed Work, and evidence carrier. Keep only the subjects current in this case.
3. **Recover a candidate whole only for an actual whole claim.** Identify the candidate individual, its direct identity pattern, relevant boundary or delimitation, environment, and at least one interaction, dependency, or constraint across that boundary when the use needs it.
4. **Identify the alleged parts independently.** A label, location, list, graph node, file section, timestamp, or common name does not identify a part. Recover each component, constituent, member, portion, temporal restriction, Method factor, Work part, or other object using the rule that defines or tests that claim.
5. **State every direct relation occurrence separately.** Name exact participants and test the direct predicate. A relation obtains neither because the whole was recognized nor because a trace, view, or record lists it.
6. **Add construction or selected structure only when the receiving use consumes it.** `C.13` may report already recovered parts, relations, constraints, and a construction rule. `A.22` may identify one selected structure when its selection basis and identity discriminators are current. Neither creates the direct facts.
7. **Recognize or reidentify the whole only when that question is current.** Use `A.1` for holon recognition and `B.2` for a remaining whole-reidentification question after direct existing-whole explanations have been tested. A changed adjective or part list alone decides neither.
8. **Separate coverage, completion, and performed Work.** Name what is covered, under which scope and criterion, by which exact relation, and whether the claim concerns a MethodDescription, capability, plan, Work occurrence, production result, evidence set, or another subject. Apply A.15.1/A.15.PROD or the rule for that exact subject; do not treat a plan as performed Work.
9. **Stop after unpacking.** State each recovered whole, relation, characteristic, Work, evidence use, or verdict directly. Apply another named rule only when one exact question remains and its entry holds; otherwise stop with the completed claims or exact blocker.

#### A.6.H:4.3 - Classify `integrity` by the claim it carries

The word `integrity` never chooses mereology by itself.

| Current sentence | First exact objects | Governing exit | Blocked overread |
| --- | --- | --- | --- |
| “Structural integrity is measured at X.” | bearer, integrity Characteristic, Scale or coordinate, Unit when needed, measurement method, result, evidence pointer, and time stance | `C.16.P`, then `C.16` and the exact measurement pattern | Do not invent a candidate whole, boundary, parts, or `PhaseOf` merely because the Characteristic is named *integrity*. |
| “This report supports the integrity claim.” | exact claim, evidence-bearing episteme or carrier, evidence-use relation, relying use, limitations, and currentness when required | `A.10`; `B.3` only when an assurance claim is current | A report title, provenance link, or measured value is neither assurance nor a whole. |
| “The assembled pump remains an integral whole.” | exact pump, direct identity rule, boundary, independently identified parts, direct assembly or parthood relations, any current selected structure, and the whole-recognition or reidentification question | `A.14`, `C.13`, `A.22`, `A.1`, or `B.2` as selected by the actual claim | The adjective *integral*, a BoM, or an assembly record does not establish the whole or relations. |
| “Data integrity” or another defined term of art | exact bearer, defined Characteristic or constraint, threat/assumption or qualification basis, and receiving use | the characteristic, constraint, security, measurement, or evaluation pattern | Do not reinterpret the term as structural wholeness unless the sentence separately makes that claim. |

If the source leaves these readings genuinely open, preserve the alternatives and block the named use until evidence discriminates them.

#### A.6.H:4.4 - Select the direct relation, not a generic part edge

| Intended claim | Required test and subject pattern | Typical non-inference |
| --- | --- | --- |
| Physical or structural component | Identify both entities, the direct `ComponentOf` predicate, boundary relevance, and obtaining facts under `A.14`/the structural pattern. | Diagram containment or removal from a list does not establish component parthood. |
| Conceptual or content constituent | Identify the exact episteme or publication-unit whole and the exact constituent under `A.14`. Keep the described referent separate. | A section in a file is not therefore a component of the described system. |
| Measured portion | Name the whole, portion, extensive measure μ, compatible unit, additivity/non-overlap rule, and boundary under `A.14`. | A percentage, share, or smaller numeral does not make a structural component. |
| Collection membership | Name the collection, its identity rule, member, and direct `MemberOf` occurrence. | Membership is not transitive parthood and does not make an acting collective system. |
| Proper temporal restriction of an enduring individual | Apply the subject's direct identity rule, then use `PhaseOf(x,y)` only when `x` is the same exact `y` restricted to a proper interval and coverage/overlap conditions hold. | A timestamp, state label, or changed property alone does not create a phase object. |
| Distinct episteme history | Compare C.2.1 claim content, EntityOfConcern, and effective ReferenceScheme. When a discriminator changes, identify another episteme; assert `EpistemeEditionRelation` only when its independent historical-continuation predicate obtains. | `v2`, filename, shared title, provenance, publication order, revision Work, or source use establishes neither identity nor continuity. |
| Performed Work interval, episode, part, retry, resumption, or later occurrence | Use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, another admitted Work-part relation, or a separately identified Work occurrence according to its exact predicate. | A shift, phase, step, log row, or MethodDescription section never routes Work through generic `PhaseOf`. |
| Method factor, order, branch, or join | Identify exact Methods and method-composition claims under `A.3.1`/`B.1.5`; use B.1.4 only for a bounded aggregation of already recovered order relations. | A box, sequence position, description constituent, plan item, or Work part is not a Method part by appearance. |

#### A.6.H:4.5 - Unpack `complete`, `turnkey`, and `end-to-end`

Ask what the next reader may do because the claim is supposedly complete.

| Candidate reading | What must be named | Direct return |
| --- | --- | --- |
| Complete whole or assembly | candidate whole, identity, boundary, required parts, direct relations, construction rule when current, and completion predicate | `A.1`, `A.14`, `C.13`, `A.22`, or the exact construction/completion pattern |
| Specification coverage | exact claim-bearing episteme, described EntityOfConcern, effective ReferenceScheme, required content or criterion set, coverage predicate, scope, and gaps | `C.2.1`, `A.3.2`, and the exact coverage/evaluation pattern |
| Capability coverage | exact holder, capabilities, required actions or conditions, scope, and direct coverage criterion | `A.2.2` and the exact capability/coverage pattern |
| Work coverage or completion | exact Work occurrence(s), temporal extent, performed parts or episodes when needed, completion or production predicate, acceptance boundary, and evidence | `A.15.1`, `A.15.PROD`, or the exact completion/acceptance pattern |
| Evidence coverage | exact claim set, evidence-bearing objects, evidence-use relations, scope, limitations, and relying use | `A.10`; `B.3` only for an assurance claim |
| End-to-end method or workflow | exact Methods, method parts and joins, exposed interactions, failure and stop conditions; performed runs remain separate | `A.3.1` and `B.1.5`, with A.15.1 for actual Work |

A sentence may require several rows. Write several direct claims; do not bundle them back into one “wholeness” record.

#### A.6.H:4.6 - Use wording as a cue, not as ontology

The following recurring expressions are useful review cues, not a second trigger registry:

- *whole*, *entire*, *integrated*, *coherent*, *holistic* — ask whether there is an actual candidate whole, a measured or assurance claim, or only rhetoric;
- *part*, *piece*, *component*, *module*, *element*, *subsystem*, *includes*, *contains*, *comprises* — recover the object and direct relation rather than accepting the noun;
- *phase*, *version*, *revision*, *edition*, *lifecycle* — apply the direct identity pattern before any history label;
- *complete*, *turnkey*, *end-to-end*, *fully specified* — recover the exact coverage or completion claim;
- *pipeline*, *workflow*, *process*, *step*, *stage* — distinguish Method, MethodDescription, WorkPlan, performed Work, order relation, and publication representation;
- *collection*, *group*, *team*, *set* — distinguish membership, acting system, system-role assignments, and selected collection structure;
- *context*, *environment*, *discipline as a whole* — name the actual bounded context, episteme family, community, organization, or other subject before making a boundary or nesting claim.

When a cue occurs inside a defined term of art, retain the definition and its PatternID locator when needed. Open A.6.H only if the sentence also makes an unresolved whole, part, structure, coverage, or completion claim.

#### A.6.H:4.7 - Describe change through the object that changed

When a wholeness-looking story changes, name the exact object and direct relation:

- for a different boundary or interaction claim, state the changed object and apply the applicable boundary or delimitation rule;
- for an added, removed, or differently related part, test the exact parthood, membership, portion, or selected-structure claim;
- for changed episteme content, EntityOfConcern, or effective ReferenceScheme, compare C.2.1 identity and test edition continuity separately;
- for a different publication form, occurrence, or carrier, state that publication or carrier claim and apply its rule;
- for a changed Method, MethodDescription, WorkPlan, Work history, production result, or completion claim, state that object and apply its rule;
- for a changed coverage scope, criterion, evidence set, or assurance use, repair that direct claim rather than inventing a generic completeness status.

Do not substitute a generic change lexicon for those objects and predicates. A readable verb is welcome when the exact direct claim remains recoverable.

#### A.6.H:4.8 - Guardrails

1. No situation record, card, bundle, adjective, table, graph, or trace is the whole or direct relation by presence.
2. No generic `partOf` closes a load-bearing claim when a direct relation kind or subject pattern is required.
3. No order, plan, or Work history is structural parthood by position.
4. No membership is upgraded to component assembly or acting-system identity.
5. No cross-boundary flow or influence is treated as a part merely because it crosses the boundary.
6. No `integrity` reading is selected before the bearer, claim, and receiving use are known.
7. No plan, description, or publication is treated as performed Work.
8. No version, revision, edition, phase, filename, or provenance label decides identity or continuity.
9. No construction trace or selected structure creates its listed parts or relations.
10. No coverage statement becomes assurance, acceptance, readiness, or completion beyond its exact predicate and evidence.

### A.6.H:5 - Archetypal Grounding

#### A.6.H:5.1 - Assembled pump

Source sentence: “After seal replacement, the assembled pump remains an integral whole.”

1. The subject is `PumpUnit-37`, not the maintenance record, drawing, or seal-replacement Work.
2. The pump's direct identity rule decides whether the same individual continued.
3. The current use names the pump boundary, impeller, casing, replacement seal, and the exact assembly or parthood relations on which operation depends.
4. If the decision consumes one selected organization of those relations, A.22 governs that structure; if it consumes a construction account, C.13 reports already recovered facts.
5. A.1 recognizes the candidate whole; B.2 opens only if the replacement leaves a genuine whole-reidentification question.
6. Calibration, seal replacement, and inspection remain separately governed Work and change facts. The adjective *integral* proves none of them.

#### A.6.H:5.2 - Laboratory pipeline

Source sentence: “The whole chromatography pipeline is turnkey, and the chemist owns the whole thing.”

The repair produces several claims:

- the reusable procedure is one exact Method or composite Method under A.3.1/B.1.5, with exact joins and exposed interactions;
- its procedure document is a separate `U.MethodDescription` episteme under C.2.1/A.3.2;
- “turnkey” becomes the exact specification, capability, Work, or evidence coverage claim needed by the receiving use;
- treat *owns* as a local wording cue. First state the decision that depends on it and the exact proposed sentence. Candidate readings include, for example, property or title, possession or custody, operational control, decision authority, stewardship or responsibility, assignment, commitment, and permission; they have different participants and predicates. Apply the direct rule when one exists, or return A.6.RCD `missing-governor[...]` naming the participants, proposed predicate, affected use, and absent definition; and
- an actual laboratory run is dated Work under A.15.1.

Thus “the laboratory owns the instrument,” “the chemist has custody during the run,” “the chemist may authorize disposal,” and “the chemist is responsible for calibration” are four different claims. None follows from team membership, classification, assignment, commitment, or permission merely by form.

No one claim is a component relation merely because the source uses *pipeline* or *whole*.

#### A.6.H:5.3 - Paper, proof, and revision

Source sentence: “Section 3 is part of the proof, and v2 is part of v1.”

- Recover whether Section 3 is a constituent of the paper episteme, a publication-unit constituent, or a described proof step. Keep those subjects separate.
- Recover argument order under its subject pattern rather than as physical containment.
- Compare the exact C.2.1 triples for the two labelled epistemes. Changed claim content identifies two epistemes. Assert `EpistemeEditionRelation(E_v1,E_v2)` only when its historical-continuation predicate obtains.
- If one unchanged episteme is needed only during a proper interval, `PhaseOf(E@τ,E)` may state that restriction. It does not connect v1 to v2.
- Drafting, review, and publication are Work and publication relations, not participants of the edition relation.

#### A.6.H:5.4 - Integrity measurement and assurance

Source sentence: “The structural integrity score is 0.82, so the system is assured.”

First recover the bearer, integrity Characteristic, Scale, measurement method, result episteme, evidence, and time stance under C.16.P/C.16. Then ask whether a named B.3 assurance claim is actually being made and recover its claim, evidence-use relation, scope, limitations, and relying context. The number does not create a candidate whole, a part relation, or an assurance result.

### A.6.H:6 - Recognition and assurance stay separate

**Recognition questions** decide which objects and direct relations are current:

- Is there one candidate whole under A.1?
- Which independently identified parts, constituents, members, portions, or temporal restrictions participate?
- Which direct relations obtain?
- Does a selected structure or construction account matter to this use?
- Does the same whole persist, or is reidentification current?

**Assurance questions** decide what may be relied on:

- Which claim is being supported?
- Which evidence bears on it through which relation?
- What scope, limitation, time stance, and relying use apply?
- Does the evidence support recognition, relation truth, measurement, completion, or another claim?

Evidence can make an assertion inspectable without becoming constitutive of the whole or relation. Unknown support does not create a third identity or obtaining state.

### A.6.H:6.1 - Bias-Annotation

- **Governance bias.** The pattern favors reviewable direct claims over rhetorically satisfying wholeness language. Ordinary prose and explicit unresolved alternatives mitigate this when a decision is not yet due.
- **Architecture bias.** Use the applicable patterns and small typed vocabularies instead of one reusable wholeness schema. The minimum-current-object rule mitigates unnecessary apparatus.
- **Ontological/epistemic bias.** It insists on separating referent, episteme, publication, Method, plan, Work, and evidence. This cost is paid only when the distinction changes the receiving use.
- **Pragmatic bias.** It favors early disambiguation to avoid downstream refactoring. A local direct sentence is sufficient; reusable declarations or structures are added only for a named later use.
- **Didactic bias.** It uses recurring cue words and worked cases to teach the route, while `E.10` remains the shared wording-use pattern and the cue list creates no second registry.

### A.6.H:7 - Conformance Checklist

| ID | Requirement |
| --- | --- |
| `CC-A6H-1` | The entry names the working decision, concrete candidate objects, receiving use, and load-bearing sentence. |
| `CC-A6H-2` | The subject level is explicit when referent, episteme, publication, carrier, Method, plan, Work, or evidence would select different relations. |
| `CC-A6H-3` | An actual whole claim identifies the candidate individual, direct identity pattern, boundary or delimitation when relevant, and independently recovered parts or constituents. |
| `CC-A6H-4` | Every direct relation claim names exact participants and passes its own obtaining rule; co-listing, wording, position, or representation establishes none. |
| `CC-A6H-5` | `PortionOf` names an extensive measure μ, compatible unit, and additivity/non-overlap basis. |
| `CC-A6H-6` | `PhaseOf` is used only for a proper temporal restriction of one unchanged directly governed individual; changed epistemes use C.2.1 and Work uses A.15.1. |
| `CC-A6H-7` | Method factors, description constituents, plan items, and performed Work parts remain separate and use their subject patterns. |
| `CC-A6H-8` | `integrity` is classified as a characteristic/measurement, evidence/assurance, actual structural-whole claim, or another defined term before another rule is applied. |
| `CC-A6H-9` | `complete`, `turnkey`, and `end-to-end` name the exact covered objects, scope, criterion, predicate, gaps, and applicable defining or testing rule. |
| `CC-A6H-10` | C.13 construction and A.22 selected structure are added only for a named use and create no direct part or relation occurrence. |
| `CC-A6H-11` | A.1 recognition and B.2 reidentification are opened only for their actual questions; an adjective, list, or changed label decides neither. |
| `CC-A6H-12` | The result is one or more subject-qualified assertions or exact blockers, never a wholeness record, bundle, or new kind. A PatternID appears only as a locator for current defining or testing content, or for an identifiable future definition need. |

### A.6.H:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Holistic-as-evasion | “We took a holistic view” replaces the actual decision, subject, boundary, or relation. | Name the receiving use and exact claim, or remove the load-bearing assertion. |
| Universal part-of | Components, constituents, members, portions, phases, Method factors, and Work parts share one edge. | Recover each object and direct predicate under its subject pattern. |
| Record-as-whole | A `wholenessSituation`, bundle, BoM, graph, or trace is treated as the whole or relation. | Recover the candidate entity, independently grounded facts, exact assertion and predicate, and the subject pattern only as its ClaimGraph locator. |
| Structure-as-sequence | Method order or plan order becomes containment. | Recover exact Methods and order/join claims under B.1.5/B.1.4; keep Work separate. |
| Version-as-phase | Different epistemes are called phases of one document lineage. | Apply the C.2.1 identity triple, then test `EpistemeEditionRelation` independently. |
| Work-phase shortcut | Shift, monitoring window, episode, retry, or resumption uses generic `PhaseOf`. | Apply A.15.1's exact temporal-part, episode, operational-part, retry, resumption, or occurrence rule. |
| Integrity-as-wholeness | A measurement, security property, report, or assurance claim is forced through parts and boundary. | Use the four-way integrity classification in 4.3. |
| Completeness-by-rhetoric | “Turnkey” or “end-to-end” supplies no covered set, scope, criterion, or subject pattern. | State the exact specification, capability, Work, evidence, construction, or completion claim. |
| Description/referent drift | The same noun alternates among a system, model episteme, document, carrier, plan, and Work. | Name each current subject and its direct relation. |
| Generic change narration | A new change verb replaces the changed object and predicate. | State the exact boundary, relation, episteme, publication, Method, Work, or coverage change. |

### A.6.H:9 - Consequences

| Benefits | Costs and mitigations |
| --- | --- |
| Decidable disagreements | The practitioner must name the exact subject and receiving use before arguing about the word. |
| Local repair | One sentence may become several direct claims; stop after the claims the receiving use actually needs. |
| Separate rule sources | Mereology, episteme identity, Work, measurement, evidence, publication, and assurance retain their distinct rules. |
| Honest uncertainty | An unresolved case blocks only the named use instead of creating an omnibus record. |
| Reusable assurance | Recognition facts and evidence-use claims can be checked independently. |
| Less ontology by wording | Familiar trigger words no longer mint kinds, relations, structures, or lifecycle objects. |

The practical test is simple: **if “whole” matters, name the thing, the relation, and what the reader may do with the claim.**

### A.6.H:10 - Rationale

Wholeness language is useful because it compresses boundary, identity, relation, construction, coverage, and assurance into ordinary speech. The same compression becomes dangerous only when downstream work relies on one particular reading.

The minimal repair is therefore not a richer wholeness schema. It is an exact-object sequence that starts with the working decision, recovers only the objects that decision consumes, and applies another rule only for a still-current concrete question. This preserves conversational economy while preventing a representation, record, label, or adjective from replacing an in-world object or relation.

The sequence also preserves two positive uses often lost in blanket cleanup. `PhaseOf` remains valid for a proper restriction of one unchanged enduring individual, including one unchanged episteme when its C.2.1 identity triple is fixed. And ordinary whole recognition remains useful when an exact candidate entity, boundary, parts, relations, and direct identity rule are genuinely current.

### A.6.H:11 - SoTA-Echoing

| Source tradition | Current practice used here | Local adoption | Rejected shortcut |
| --- | --- | --- | --- |
| [ISO/IEC/IEEE 42010:2022](https://www.iso.org/standard/74393.html), architecture-description practice | Distinguish the entity of interest from its description and make concerns, viewpoints, environment, and boundary explicit. | Recover the candidate referent and boundary before treating a description or publication as evidence about it. | A view, diagram, or architecture document is the system whole or establishes its parts. |
| [ISO/IEC 21838-2:2021](https://www.iso.org/standard/74572.html), upper-ontology discipline | Keep continuants, temporal parts, occurrents, and relation types explicit. | Preserve direct identity and relation tests, including proper temporal restriction without using it as episteme-edition or Work shorthand. | One universal part edge or lifecycle object covers components, versions, and Work. |
| [ArchiMate 3.2](https://www.opengroup.org/sites/default/files/docs/downloads/n221p.pdf), enterprise-architecture relation practice | Different structural and behavioral relations answer different questions. | Use the source vocabulary as a comparison aid while retaining FPF subject patterns and occurrence rules. | A modelling-language edge label establishes the in-world FPF relation. |
| [Team Topologies](https://teamtopologies.com/), sociotechnical boundary practice | Team boundaries, interaction modes, and cognitive load affect organization and flow. | Treat team and ownership wording as cues. Recover the exact claim first—for example property or title, custody, control, authority, responsibility, assignment, commitment, permission, interaction, or Work—and use A.6.RCD when its predicate lacks a current definition. | A team boundary or membership list establishes ownership, responsibility, assignment, or Work by itself. |
| ISO/IEC/IEEE 29148:2018, requirements quality | Requirements should identify the item, condition, and verifiable claim without referent/document ambiguity. | Require exact subjects, scopes, predicates, and blocked overreads on load-bearing surfaces. | A specification sentence becomes true or complete because the document is complete-looking. |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), security and privacy controls | Integrity claims depend on exact information, constraints, threats, controls, assessment, and evidence. | Recover the data/security integrity characteristic, measurement, evaluation, or assurance question and apply its rule before any structural-whole reading. | Every occurrence of *integrity* means wholeness or mereological coherence. |

Whenever *fraction*, *percentage*, or *share* is used as a part claim, recover the extensive measure μ and additivity basis before `PortionOf`; otherwise keep the value with its measurement, allocation, membership, or other subject pattern.

### A.6.H:12 - Relations

- **Specialises:** `A.6.P` after its 4.11 whole/part/integrity/coverage branch has recovered exact candidate objects and the receiving sentence.
- **Uses for direct mereology:** `A.14`; construction accounts to `C.13`; selected structures to `A.22`; holon recognition to `A.1`; and remaining whole reidentification to `B.2`.
- **Uses for episteme and publication questions:** `C.2.1`, `A.3.2`, `E.17`, `E.24.PUB`, and `C.29` as selected by the exact subject.
- **Uses for Method, plan, and Work questions:** `A.3.1`, `B.1.5`, `A.15.2`, `A.15.1`, `A.15.PROD`, and `B.1.4` only for bounded aggregation of already recovered temporal or order relations.
- **Uses for integrity, evidence, and assurance questions:** `C.16.P`, `C.16`, the exact measurement pattern, `A.10`, and `B.3`.
- **Uses for absent relation governance:** `A.6.RCD` after participants, required predicate, and blocked receiving use are exact.
- **Does not create:** a wholeness situation, card, bundle, lifecycle kind, automatic edition series, universal part relation, coverage status, assurance verdict, or direct relation occurrence.

### A.6.H:End

