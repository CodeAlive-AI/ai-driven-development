## F.0.1 - Source-Local Meaning Recovery

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### F.0.1:1 - Problem frame

> **One-sentence summary.** Recover what one expression means in one exact source passage before comparing, translating, or reusing it elsewhere.

Use `F.0.1` when a word in an already selected source may be read in more than one way and the reading can change the present answer or action. Name the exact source and edition, state the source-local meaning in ordinary language, and point to the passage that supports that reading.

The first useful result is one source-backed meaning statement. For example: “In OMG BPMN 2.0.2 (January 2014), *Process* here means the designed sequence or flow of Activities in an organization; this reading comes from §10.1.” If that answers the question, use it and stop.

**What changes in practice.** A reader can inspect the source of the meaning without first creating a semantic container, record, relation, or assurance package. A stronger formal result is added only for a named later use.

**Not this pattern when.** Use an already clear source claim directly when no lexical distinction changes the work. Use `F.1` when the open question is which sources can change the answer, `F.0.2` when several source ontologies must be compared for one receiving claim, and `F.18` when the problem is selecting an FPF term after the subject is settled. When the problem is not lexical, use the rule that defines or tests the exact entity, relation, claim, measurement, permission, or Work question. Use `F.9` only when an actual relation between already recovered source-local meanings is current.

### F.0.1:2 - Problem

A string does not identify one meaning across sources. The same spelling can denote a designed structure, a performed occurrence, a status, a permission, a measurement, or another subject. If the source, edition, and passage disappear, a later claim can silently change its entity, relation, time stance, or intended use.

The opposite response is also harmful. A full source survey, durable cell, provenance record, reliance disposition, or assurance claim for every word makes ordinary reading needlessly expensive. The problem is to recover one local meaning cheaply while keeping the point of escalation visible.

### F.0.1:3 - Forces

| Force | Tension |
| --- | --- |
| Local fidelity vs later reuse | The answer must stay true to its source while remaining available to later work. |
| Inspectability vs readable prose | Source and edition must remain recoverable without mechanically qualifying every repetition. |
| Cheap answer vs durable address | One sentence may close the question; repeated or cross-source use may need an exact reusable cell. |
| Useful relation vs false sameness | Two meanings may stand in a useful relation, but shared wording, similarity, or a family label does not establish it. |
| Continuity vs revision | Historical meanings remain citable while a changed relied premise reopens only the affected use. |

### F.0.1:4 - Solution — recover locally, strengthen only for use

#### F.0.1:4.1 - Recover one source-local meaning

1. **Name the question.** State what answer or action can change if the expression is read differently.
2. **Identify the source.** Give the exact source and edition. A discipline or shelf label is not enough.
3. **Locate the passage.** Point to the claim, definition, example, rule, or other passage used.
4. **State the meaning plainly.** Say what the expression denotes or claims in that passage. Keep designed descriptions and performed occurrences distinct when the source does.
5. **Use the answer and stop.** Do not create a durable cell or relation unless a later receiver needs it.

The source, edition, expression, passage, and plain meaning are the ordinary minimum. A brief scoped heading may keep an already established source in view; repeated source tags are unnecessary when the reading remains unambiguous.

#### F.0.1:4.2 - Add a durable address only when it earns its cost

Create one F.17 `SchemeSenseCell <ReferenceScheme, LocalExpression, LocalSenseClaim>` only when stable reuse, a later claim, a named receiver, or an actual relation to another local sense needs an exact address. The effective ReferenceScheme keeps the source and edition recoverable; the LocalSenseClaim states the meaning rather than hiding it in a label.

State an obtaining `LocalSenseBasisRelation` only when the support relation from an exact basis episteme to that cell is itself current and supported. Identifying a source, stating that support relation, relying on it in a later use, and assuring that reliance are four different claims. Use A.10 and B.3 only for the latter questions.

When a source fixes a designed-versus-performed distinction or another time stance, put it in the local sense claim or its exact basis. Do not make an edition label or separate container stand in for the distinction.

#### F.0.1:4.3 - Relate different local meanings only when the relation is current

A shared label, close paraphrase, common superclass, table row, embedding score, or family membership does not establish identity or another relation. First recover each source-local meaning separately. Then use F.9 when a receiving use needs an actual relation between the two F.17 cells.

The F.9 result states which two cells are related, what kind of relation obtains, how its endpoints are oriented, and what relation profile makes it true. When a receiving use is current, state a separate C.2.1 claim: what action is proposed, in which direction, under which correspondence rule, how much loss it tolerates, and whether the Bridge is suitable for that use. Changing this use claim does not change the Bridge. Neither the relation nor the claim by itself permits translation, substitution, or row membership, establishes reliance or authorization, or shows that the action occurred. A chain of relations does not silently create a direct endpoint relation.

#### F.0.1:4.4 - Recover old Context-shaped artifacts only for a current reliance

An old Context Card or two-part SenseCell remains an historical episteme or representation under its original edition. Do not relabel it as a current F.17 cell.

When a current claim or action actually relies on it, recover only the values that use needs: for example, the exact source and edition, expression, source-local claim, passage, effective scheme, claim scope, or obtaining relation. If a needed value cannot be recovered, return the exact unresolved value and reopen only the dependent claim or action. Mere archival presence does not start a migration.

#### F.0.1:4.5 - Minimal conceptual objects

| Object | What it is | What it is not |
| --- | --- | --- |
| Source-backed meaning statement | A plain answer tied to one exact source passage. | A new kind, container, relation, or assurance result. |
| `SchemeSenseCell` | F.17's durable address for one expression and local sense claim under one effective ReferenceScheme. | The ordinary first result or a container of source doctrine. |
| `LocalSenseBasisRelation` | A current direct support relation from an exact basis episteme to the cell. | Automatic provenance, reliance, or assurance. |
| F.9 Bridge | An actual semantic relation between distinct recovered cells under its applicable relation profile. | A proposed use, a bounded-use claim, permission, reliance, authorization, or evidence that an action occurred. |
| Short source note | An optional readable representation of already recovered source information. | A form whose presence establishes meaning or admission. |

#### F.0.1:4.6 - Invariants

1. Every load-bearing local meaning has a recoverable source, edition, and passage.
2. A plain source-backed statement may be the complete result.
3. A `SchemeSenseCell` is created only for a named durable use and keeps scheme, expression, and claim distinct.
4. A basis relation is stated only when it obtains; reliance and assurance remain separate.
5. Different local meanings remain distinct unless an exact relation between them is established.
6. Designed and performed readings do not become identical through shared wording.
7. A changed edition, passage, or relation reopens only claims and uses that relied on the changed premise.
8. Historical artifacts remain historical; current recovery does not require corpus-wide relabelling.

#### F.0.1:4.7 - Readable reasoning moves

- **Local reading.** “This source passage uses *t* to mean *m*.”
- **Durable address.** “This receiver will reuse that reading, so record it as an F.17 cell under the effective source scheme.”
- **Basis.** “This exact source episteme supports the cell through a current `LocalSenseBasisRelation`.”
- **Cross-source relation.** “The two recovered cells stand in this stated F.9 relation under this relation profile.” When a receiving use is current: “A separate C.2.1 claim says whether that Bridge is suitable for this action, direction, correspondence rule, and tolerated loss.”
- **No transitive shortcut.** Two established relations through an intermediate meaning do not establish a direct third relation.
- **Affected-only reopening.** A changed source premise reopens the claims that used it, not every claim that cites the edition.

These are allowable conceptual moves, not storage fields, APIs, or mandatory workflow records.

### F.0.1:5 - Archetypal Grounding

#### F.0.1:5.1 - Entry, stop, and continuation

Start with one troublesome use in one already selected source. Return one ordinary sentence plus a source pointer. Stop when it answers the question.

Continue only for the next result actually needed:

- `F.1` for a question-relative source cut;
- `F.17` for a durable local-sense address and, when current, its basis relation;
- `F.9` for an actual relation between distinct recovered cells;
- `F.0.2` for a bounded comparison or synthesis among source ontologies;
- `F.18` for naming after the subject distinction is settled; or
- the rule that defines or tests the exact entity, relation, claim, measurement, permission, or Work question itself, with its pattern ID as locator.

#### F.0.1:5.2 - Compact worked results and recognition cues

A **worked result** below names the exact source, edition, passage, and meaning used. A **recognition cue** only marks a likely false friend; it establishes no local meaning until the practitioner supplies those four values. This distinction keeps a broad set of examples useful without dressing an unresolved pointer as source-backed knowledge.

##### F.0.1:5.2.1 - *process* and *activity*

- **Worked result — OMG BPMN 2.0.2 (January 2014), §10.1, Processes.** *Process* denotes the designed sequence or flow of Activities in an organization.
- **Worked result — W3C PROV-O Recommendation (30 April 2013), §3.1, Starting Point Terms.** *Activity* denotes something that occurs over a period of time and acts upon or with entities, including using or generating them.

The first question may need only one of these readings. If a later use relates the designed structure to performed occurrences, recover two F.17 cells and state the exact F.9 relation, including concurrency or trace information that does not carry across. Do not call the two meanings identical.

##### F.0.1:5.2.2 - *actuation* and *control output*

- **Recognition cue — control theory.** If *actuation* may mean a signal applied to plant actuators, select one exact control-theory publication, edition, and passage before using that reading.
- **Recognition cue — IEC 61131-3.** If *control output* may mean a program-produced value sent to field I/O, identify the exact edition and clause before using that reading.

These cues establish no relation. After both readings become worked results, F.9 may test whether the PLC output can be read as the controller's actuation signal for one stated operating regime while keeping hardware and scan-cycle limits visible.

##### F.0.1:5.2.3 - *observation* and *service metric*

- **Worked result — W3C SOSA/SSN Recommendation (19 October 2017), §4.3.2.2, `sosa:Observation`.** *Observation* denotes the act of carrying out a procedure to estimate or calculate a value of a property of a feature of interest.
- **Recognition cue — ITIL 4.** If *service-level metric* is used for a quantity that evaluates a service-level objective, identify the exact ITIL 4 publication, edition, and passage before using that reading.

The verified SOSA reading alone establishes no service-metric relation. Once the second reading is source-backed, a named use may ask whether the observation supplies evidence for that metric; that is a subject relation, not lexical identity or same-row membership.

##### F.0.1:5.2.4 - *subclass-of* and *is-a*

- **Worked result — W3C OWL 2 Structural Specification and Functional-Style Syntax, Second Edition (11 December 2012), §9.1.1, Subclass Axioms.** `SubClassOf(CE1 CE2)` states that the first class expression is a subclass of the second.
- **Recognition cue — engineering glossary.** If *is-a* is being used as a less formal kind-of relation, identify the exact glossary, edition, and entry before relying on that reading.

Keep the verified formal reading and the unresolved cue separate. Relate them only when the receiving artifact needs the formal relation and an exact second passage supports the correspondence.

##### F.0.1:5.2.5 - *permission* and RBAC *role*

- **Worked result — W3C ODRL Information Model 2.2 Recommendation (15 February 2018), §2.6.1, Permission Class.** A Permission allows an action on an Asset when its refinements and constraints are satisfied and its duties are fulfilled.
- **Recognition cue — NIST RBAC.** If *role* is being used for an access-control grouping through which permissions are assigned, identify the exact NIST publication, edition, and passage before using that reading.

The verified permission reading is not the unresolved role reading. A later access-control use may relate two source-backed meanings, but familiar wording alone establishes neither the relation nor interchangeability.

#### F.0.1:5.3 - Quick checks for later use

- **String check.** If the only evidence is the same spelling, no cross-source relation has been established.
- **Stance check.** If one source describes a design and another a performed occurrence, state that difference before any relation or row use.
- **Direction check.** Preserve the direction and limits of the actual relation; a reverse or broader reading needs its own support.
- **Chain check.** Keep intermediate meanings and accumulated loss visible; test a direct endpoint relation separately when needed.
- **Contradiction check.** Incompatible relation claims about the same cells remain explicit rather than being averaged into a vague alignment.
- **Row check.** A Concept-Set row needs the relation and bounded receiving-use judgment required by F.7 and F.9; a label or confidence level cannot admit a member.

#### F.0.1:5.4 - Quick reference

- **Ordinary result:** one source-backed plain meaning statement.
- **Durable local meaning:** an optional F.17 `SchemeSenseCell`.
- **Current support:** an optional obtaining `LocalSenseBasisRelation`.
- **Different local meanings:** separate cells; use F.9 only for an actual relation.
- **Source selection:** F.1; **synthesis:** F.0.2; **naming:** F.18; **subject reasoning:** the defining or testing rule for the recovered claim.

> **Mental checklist:** Name the source and edition → locate the passage → say what the expression means → stop if sufficient → add only the durable address or relation a named receiver needs.

### F.0.1:6 - Bias-Annotation

- **Gov:** Source authorship, popularity, or standard status does not decide the receiving claim.
- **Arch:** The pattern favors recoverable local meanings and explicit relations over one global vocabulary or universal container.
- **Onto/Epist:** A word, a local-sense claim, its subject, its source, a basis relation, and a receiving claim remain different.
- **Prag:** Ordinary use is one sentence and one citation; stronger objects and assurance are conditional.
- **Did:** Plain worked cases come before formal designators. A scoped source heading may reduce repetition without hiding the source.
- **Scope:** The pattern recovers meaning. It does not establish source truth, source adequacy, relation obtaining, permission to substitute, or assurance.

### F.0.1:7 - Conformance Checklist

#### F.0.1:7.1 - Static checks

- **SCR-F01 (Recoverable source).** Every load-bearing local meaning identifies the exact source, edition, and passage directly or through an unambiguous scoped reference.
- **SCR-F02 (Plain first result).** The ordinary branch's result is a readable meaning statement, and the practitioner may stop there.
- **SCR-F03 (Conditional cell).** A `SchemeSenseCell` appears only for a named reuse, claim, receiver, or relation need and keeps ReferenceScheme, LocalExpression, and LocalSenseClaim distinct.
- **SCR-F04 (Separate support).** A `LocalSenseBasisRelation` is asserted only when current; source identification, reliance, and assurance are not inferred from it.
- **SCR-F05 (No string identity).** Shared wording, family, score, or row does not establish a relation between local senses.
- **SCR-F06 (Explicit relation and use).** Every claimed cross-local relation uses exact F.17 endpoints and the applicable F.9 relation profile. When a receiving use is current, a separate C.2.1 claim names the proposed action, use direction, correspondence rule, tolerated loss, and polarity.
- **SCR-F07 (Temporal honesty).** Designed descriptions and performed occurrences remain distinct wherever the source fixes that difference.
- **SCR-F08 (No subject capture).** The local gloss does not redefine the subject's behaviour, deontics, measurement, kind, proof, or work rules.

#### F.0.1:7.2 - Regression and evolution checks

- **RSCR-F01 (Affected edition change).** A changed edition or passage reopens only local claims and later uses that relied on the changed content.
- **RSCR-F02 (Endpoint change).** A changed cell claim or stance triggers recheck of relations and uses that cite that endpoint.
- **RSCR-F03 (Composition guard).** A relation chain never silently becomes a direct relation or unrestricted substitution.
- **RSCR-F04 (Source-cut relevance).** Reopen F.1 only when the receiving question or use, a relied source role, known rival, counterexample, or transfer limit changes.
- **RSCR-F05 (Historical recovery).** An old Context-shaped artifact is recovered only for a current reliance; missing values return as exact unresolved inputs.

### F.0.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Global term | A load-bearing word has no recoverable source reading. | Name the exact source and passage and state the local meaning. |
| String-match identity | The same label in two sources is treated as one meaning. | Recover both meanings and inspect the actual F.9 relation. |
| Edition blur | A source is cited without the edition that fixes the reading. | Identify the edition and reopen only affected uses when it changes. |
| Domain equals source | “Control” or another shelf label is treated as one vocabulary. | Identify the actual source or practice and its claim. |
| Time-stance confusion | A design description and a performed occurrence are treated as the same thing. | State the source-local distinction and any supported relation. |
| Mixed local-sense claim | A lexical gloss absorbs behaviour, permissions, measurement, or proof rules. | Keep the meaning statement local, then use the defining or testing rule for each non-lexical claim. |
| Relation by similarity | A score, paraphrase, or common row is treated as an obtaining relation. | Use it only to guide inspection; state the exact relation if supported. |
| Heavy first answer | A cell, record, reliance account, and assurance package are required before one word can be understood. | Return the plain source-backed statement first and add stronger objects only for named uses. |
| Historical relabelling | An old Context Card is renamed into a current cell without recovering its values. | Keep it historical and recover only the values needed by the current reliance. |

### F.0.1:9 - Consequences

Local meanings become inspectable and revisable without forcing a global vocabulary. A reader sees when source selection, synthesis, naming, subject reasoning, or a cross-local relation is the real next question. Most uses become cheaper because one sentence and one citation can close them.

The cost is explicit judgment about source, edition, passage, and meaning. A reusable cell or relation requires more work only when a later receiver needs it. This cost is preferable to hiding several different objects behind one generic container.

### F.0.1:10 - Rationale

Meaning is cheapest to recover where a source actually uses an expression. Starting with the source passage prevents a later comparison from rewriting the source before the commonality or difference is known. Keeping durable cell identity in F.17 and cross-local relations in F.9 prevents local recovery from becoming a second ontology or relation catalogue.

The proportional split also protects practical use: one identified source can yield an answer immediately; several possible sources call for F.1; several source ontologies call for F.0.2; an actual relation calls for F.9.

### F.0.1:11 - SoTA-Echoing

| Current practice line and exact sources | Decision and effect in `F.0.1` | Limit kept visible |
| --- | --- | --- |
| ISO 1087:2019 and ISO 704:2022 distinguish objects, concepts, definitions, and designations. | **Adopt, with a boundary.** Recover the source-local designation and concept contribution before comparison. | Standard status establishes neither one universal vocabulary nor the receiving claim. |
| Kapferer and Zimmermann, *Domain-driven Architecture Modeling and Rapid Prototyping with Context Mapper* (2021), keep a software-domain model and language within a named DDD boundary and make inter-boundary relations explicit. | **Adapt as a software-domain example.** Use that boundary only when a DDD bounded context is the actual subject. | It does not warrant a transdisciplinary `U.BoundedContext` or make that object the source of all meaning. |
| Abd Nikooie Pour et al., *Results of the Ontology Alignment Evaluation Initiative 2025* (2025); Giglou et al., *LLMs4OM* (2024); Hu and Ichise, *From Matching to Retrieval: A New Role for LLMs in Ontology Alignment* (2025); and Qiang et al., *OAEI-LLM* (2024). | **Adapt.** Use lexical, structural, retrieved, or model-produced correspondences to find candidates worth inspecting; establish an F.9 relation only from the exact recovered senses and its relation profile. | A benchmark result, similarity score, or model answer establishes neither semantic identity nor the separate C.2.1 claim that a Bridge suits a receiving use. |
| W3C SHACL (2017) and DCAT 3 (2024) separate constraints, validation, catalog metadata, versions, and provenance from described subject claims. | **Adapt.** Keep source and edition metadata recoverable and use a compact source note when useful. | Metadata form, validation, or provenance establishes neither meaning, truth, reliance, nor assurance. |

The non-dominated combination is a plain local answer first, an exact durable address only for reuse, an inspectable relation only when current, and receiving-use judgment separately.

### F.0.1:12 - Relations

- `F.17` defines `SchemeSenseCell` and `LocalSenseBasisRelation`.
- use `F.1` to select exact sources and editions for one receiving question and use.
- `F.0.2` compares or synthesizes several source ontologies after their meanings are recovered.
- `F.2` and `F.3` support term evidence and local-sense clustering when those heavier moves are needed.
- Use `F.7` for Concept-Set rows and `F.9` for actual cross-local relations and their bounded uses.
- Use `E.15` for edition continuity, supersession, and affected-premise reopening.
- Use `A.10` for evidence use and reliance and `B.3` for assurance.
- Use `F.18` for term choice after the subject distinction is settled.

### F.0.1:End

