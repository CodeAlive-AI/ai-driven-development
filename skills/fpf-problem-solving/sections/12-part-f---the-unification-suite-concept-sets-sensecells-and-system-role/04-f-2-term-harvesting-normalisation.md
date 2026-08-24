## F.2 — Term Harvesting & Normalisation

**“Harvest the source’s own words, recover what they mean there, and stop before comparison.”**
**Status.** Architectural pattern.
**Depends on.** F.1 **Question-Relative Source Selection**; F.0.1 **Source-Local Meaning Recovery**; E.10.D1 **Recovering What “Context” Means in Use**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.3 **Source-Local Sense Clustering**; F.17 for an optional durable cell and basis relation; F.4 **SystemRoleKindDescription** when the recovered subject is a local system-role kind; F.9 only for an actual relation between distinct local meanings.
**Aliases (informative).** *source-local harvesting*; *local normalisation*.

### F.2:1 - Intent & applicability

**Intent.** Turn usage in an exact source and edition into a small, auditable set of source-local expressions and one-sentence meaning claims. Keep the source’s idiom, help a cold reader, and withhold every cross-source conclusion.

**Use this when.** F.1 has selected a source because it can change the receiving answer, and the reader needs the actual words that carry its contribution. Re-enter when the selected edition, passage, language, or interpretation basis changes enough to change meaning.

**Do not use this when.** The words are already recovered precisely enough for the receiving question, or the current task is to relate two local meanings; use F.9 for that relation. F.2 creates no global term, kind, assignment, behaviour, obligation, or storage scheme.

### F.2:2 - Problem Frame

Three mistakes recur even after the right sources are selected:

1. **Word-centrism.** A string such as *process*, *role*, or *service* is treated as though it carried one meaning everywhere.
2. **Over-normalisation.** Spelling or morphology is forced into a house style and source-specific cues disappear.
3. **Premature structure.** A short lexical note quietly acquires behavioural, deontic, measurement, or kind claims that the source passage does not establish.

F.2 prevents these mistakes by tying each expression and local-sense claim to the exact source basis that supports it.

### F.2:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| **Uniformity vs locality** | Readers benefit from stable labels, but the source’s own idiom must remain visible. |
| **Parsimony vs recall** | Keep the harvest small while retaining rare terms that materially affect later reasoning. |
| **Didactics vs fidelity** | A Plain label should help a newcomer without widening the source-local claim. |
| **Speed vs safety** | Move quickly enough to support F.3 and F.4 without smuggling in a cross-source relation. |

### F.2:4 - Core idea (didactic)

For each needed use, name the **exact source and edition**, the relevant passage, and the **effective `U.ReferenceScheme`** under which the passage is being read. Harvest an attested **LocalExpression**, choose a minimally edited **Local Normal Form (LNF)**, add Tech and Plain labels, and state the **LocalSenseClaim** in one sentence.

That is the ordinary F.2 result. If later work needs a durable address, F.17 may represent it as `SchemeSenseCell = <ReferenceScheme, LocalExpression, LocalSenseClaim>` and record the basis relation. The cell is optional and does not replace the source, passage, or claim. F.2 establishes no relation to another source-local meaning.

### F.2:5 - Minimal vocabulary (this pattern only)

* **Exact source basis** — the selected source, edition or version, relevant passage, and effective `U.ReferenceScheme` needed to recover this use.
* **Attested phrase** — a short verbatim cue showing how the expression is used in that source.
* **LocalExpression** — the exact expression whose source-local meaning is being recovered.
* **Local Normal Form (LNF)** — the minimally edited surface used to cite that expression while preserving the source’s spelling, hyphenation, and casing.
* **Tech and Plain labels** — an engineer-facing label faithful to the source and a newcomer-facing label that does not add scope.
* **LocalSenseClaim** — one sentence saying what the expression means in this source use, at the least generality needed by the receiving question.
* **Source-local lexical note** — the exact source basis, expression and LNF, labels, claim, and one or two attested cues. This is F.2’s ordinary outcome.
* **Homonymy signal** — notice that the same string supports different local claims; this notice is not a relation between those claims.
* **SchemeSenseCell** — F.17’s optional three-part address, used only when durable reuse needs it.

### F.2:6 - Solution — three mental moves

#### F.2:6.1 - Move A — Recover the basis

Ask: **“Which exact source use am I reading, and under which interpretation rules?”**

Name the source and edition, locate the passage, and recover the effective reference scheme with F.0.1. Take one or two representative phrases. If you cannot identify that basis, do not harvest the word yet.

#### F.2:6.2 - Move B — Name the local meaning faithfully

Ask: **“How does this source itself say it?”**

Choose the LNF with minimal editing. Keep an idiomatic Tech label, add a genuinely explanatory Plain label, and write one LocalSenseClaim. Prefer the source’s head noun and meaningful modifiers. Put behavioural equations, obligations, measurements, and kind criteria under their direct patterns rather than inside the lexical note.

#### F.2:6.3 - Move C — Fence the result

Ask: **“What has this source use not established?”**

Refuse to infer sameness, substitution, hierarchy, or transfer across sources; refuse to merge a materially different edition or language use by spelling alone; and refuse to treat the expression as the value that the substantive claim is about. Record an itch to compare for F.9, but do not settle it in F.2.

### F.2:7 - Guard-rails (normative, lightweight)

1. **Basis visible.** Every harvested expression **MUST** name the exact source and edition and the effective reference scheme needed to recover its meaning.
2. **Idiomatic normalisation.** LNF **MUST** preserve meaningful source spelling, hyphenation, casing, and modifiers with minimal edits.
3. **Two registers.** Each note **SHOULD** carry Tech and Plain labels; the Plain label must explain rather than broaden.
4. **Minimal generality.** The LocalSenseClaim **MUST** say no more than the source use and receiving question require.
5. **Category hygiene.** A lexical note **MUST NOT** stand in for behaviour, obligation, measurement, kind, assignment, Work, or evidence.
6. **No cross-source claim.** F.2 **MUST NOT** assert equivalence, subsumption, similarity, permission, or transfer between local meanings.
7. **Edition and language honesty.** When edition or language changes meaning, recover a distinct source-local claim and interpretation basis; do not manufacture a universal “new Context” rule.
8. **Parsimony.** Keep the head expressions that affect F.3, F.4, F.8, or a real F.9 question; omit an unused tail.

### F.2:8 - Micro-examples

> Each item is one source-local lexical note. Their proximity asserts no relation.

* **BPMN 2.0 (2011), effective BPMN scheme** — expression and LNF `process`; Tech **process**; Plain **workflow graph**; claim: “A graph of flow nodes and sequence flows specifying orchestration among participants.”
* **PROV-O (2013), effective PROV scheme** — expression and LNF `activity`; Tech **activity**; Plain **time-bounded occurrence**; claim: “An occurrence that uses or generates entities and may be associated with agents.”
* **ITIL 4 (2020), selected service-management use** — expression and LNF `service-level objective`; Tech **SLO**; Plain **service target**; claim: “A target value or range for a service characteristic.”
* **NIST RBAC (2004), RBAC scheme** — expression and LNF `role`; Tech **access role**; Plain **permission grouping**; claim: “A named grouping of permissions used in access-control assignment.”
* **SOSA/SSN (2017), SOSA scheme** — expression and LNF `observation`; Tech **observation**; Plain **act of observing**; claim: “An act applying a procedure to a feature of interest to obtain a result.”
* **IEC 61131-3, cited edition and runtime passage** — expression and LNF `task`; Tech **task**; Plain **scheduled program execution**; claim: “A cyclic or event-driven runtime unit that invokes programs.”

### F.2:9 - Didactic heuristics (informative)

* Keep the source in your inner speech: say “process in BPMN 2.0” and “activity in PROV-O”.
* Prefer the source’s head noun and meaningful modifier: do not shorten *service-level objective* to *objective*.
* Preserve spelling or case when it carries source signal.
* Compress from attested use, not from a neighbouring theory.
* When *role*, *function*, *process*, or another trigger word appears, recover the actual subject before choosing a label.

### F.2:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | Global normal form | One canonical label is reused across sources. | It erases source-local meaning. | Keep an LNF per recovered source use; relate meanings only in F.9. |
| **A2** | String = meaning | Identical spelling is treated as one concept. | Homonyms such as *role* and *process* collapse. | State source, scheme, and LocalSenseClaim before comparison. |
| **A3** | Over-normalisation | Case, hyphens, or modifiers are removed for consistency. | Source cues and citations become unreliable. | Make only minimal edits. |
| **A4** | Headless multiword | *Service-level objective* becomes *objective*. | Scope disappears. | Preserve the meaningful compound. |
| **A5** | Premature structure | A gloss contains equations, duties, or kind axioms. | A lexical note is asked to establish a substantive fact about another value. | Route the substantive claim to its direct pattern. |
| **A6** | Cross-source folding | “BPMN process ≈ PROV activity” appears in F.2. | A relation and its losses are hidden. | Leave the comparison to F.9. |
| **A7** | Edition blur | A source name has no edition although usage changed. | The claim cannot be replayed. | Name the exact edition and recover the changed meaning afresh. |
| **A8** | Dialect elevation | A tool keyword list is treated as the whole domain. | One source use displaces other evidence. | Keep it as one exact source basis. |
| **A9** | Tail chasing | Hundreds of unused terms are harvested. | Signal and working memory are diluted. | Keep terms that change the receiving answer. |
| **A10** | Fake Plain label | Tech and Plain repeat the same jargon. | The cold reader gains nothing. | Explain the use without widening it. |
| **A11** | Design-time and run-time blur | A design expression is glossed as an occurrence, or conversely. | MethodDescription and Work collapse. | State the actual source-local claim and route the distinction through F.11, A.3, and A.15. |
| **A12** | Cross-language collapse | Bilingual expressions are merged because a dictionary aligns them. | Normative and idiomatic differences vanish. | Recover each source use; assert a relation only when one obtains. |
| **A13** | Alias inflation | A new technical term is invented “for clarity”. | It competes with the source and hides provenance. | Keep inventions, if needed, only as bounded Plain labels. |
| **A14** | Role–status conflation | RBAC *role* is glossed as an acting system role. | Permission and agency claims mix. | Say **access role (RBAC)** and use E.10.ROLE and F.4 for any system-role claim. |

### F.2:11 - Worked examples

#### F.2:11.1 - Enactment and sensing

The BPMN, PROV-O, SOSA/SSN, and ITIL notes above remain four separate source-local claims. They let a writer say “compare an SOSA observation result with the ITIL service target” while withholding any claim that BPMN *process* and PROV *activity* are the same.

#### F.2:11.2 - Control and services

* **State-space control source, cited passage and scheme** — `actuation`; Plain **control output**; claim: “A signal applied to influence plant state or output.”
* **IEC 61131-3, cited runtime passage and scheme** — `task`; Plain **scheduled program execution**; claim as above.
* **ITIL 4 (2020), incident-management use** — `incident`; Plain **reported service disruption**; claim: “An unplanned interruption or reduction in service quality.”

This prevents a plant fault from becoming an ITIL incident merely because a writer wants one word for both.

#### F.2:11.3 - Kind, method, and knowledge sources

* **OWL 2 profile source** — `subClassOf`; Plain **class inclusion**; claim: “Every instance of the first class is an instance of the second.”
* **FCA source** — `formal concept`; Plain **extent–intent pair**; claim: “A maximal object–attribute pair under the stated Galois connection.”
* **SPEM 2.0 and ISO 24744 sources** — `method`; Plain **way of doing**; claim recovered from the cited method passage.
* **SOSA/SSN (2017)** — `procedure`; Plain **observation recipe**; claim: “A description of how an observation may be carried out.”

The notes do not turn an FCA concept into a root kind or a procedure description into a Method. Those are separate claims under their direct patterns.

### F.2:12 - Safe reasoning moves

1. **Localise.** Hear the expression only in the exact source use now under examination.
2. **Recover.** Identify the edition, passage, effective scheme, and source-local claim.
3. **Normalise minimally.** Choose an LNF that preserves the source’s idiom.
4. **Explain twice.** Keep an idiomatic Tech label and a genuinely helpful Plain label.
5. **Check scope.** Tighten any sentence that says more than the passage supports.
6. **Signal homonymy.** Note repeated spelling without claiming a relation.
7. **Stop.** When the local note is clear enough for the receiving question, do not add a cell or comparison merely for completeness.
8. **Address only when needed.** Use F.17’s three-part cell when later reuse requires stable addressability.

### F.2:13 - Relations

**Builds on:**

- Use **F.1 Question-Relative Source Selection** to recover the exact sources, editions, answer-changing contributions, and receiving question.
- Use **F.0.1 Source-Local Meaning Recovery** to recover the exact source-local claim.
- Use **E.10.D1** when vague *context* wording hides source, scheme, scope, situation, or use.
- Use **F.17** for a durable `SchemeSenseCell` and basis relation only when later reuse needs that address.

**Constrains:**

- **F.3** clusters exact expressions and local claims under one effective scheme; it does not infer sameness across sources.
- **F.4** may cite an exact F.17 cell when a local system-role-kind description needs it; a harvested expression establishes no kind.
- **F.9** receives exact local meanings only when a proposed use needs an actual relation between them. F.2 supplies no Bridge, equivalence, direction, or use licence.

**Used by.** Part C patterns may cite the exact source expression and local-sense claim. The direct subject pattern still defines or constrains the value in the current claim.

### F.2:14 - Migration notes

1. **New edition.** Recover the changed passage and scheme; keep the earlier note if its source use remains relevant.
2. **Idiomatic correction.** Repair the LNF without silently changing the LocalSenseClaim.
3. **Ambiguity in one source.** Recover two claims when selectional frames or entailments differ; F.3 tests the split.
4. **Language change.** Determine whether the language edition changes source wording, reference scheme, or both; do not merge by translation alone.
5. **Tail pruning.** Remove working notes that do not affect an active question; preserve cited source evidence elsewhere as required.
6. **Tool dialect.** Keep it as one exact source basis and do not let it define other sources’ idiom.

### F.2:15 - Acceptance tests

#### F.2:15.1 - Static conformance

* **SCR-F2-S01 (basis).** Every note names the exact source and edition and the effective scheme required to recover the claim.
* **SCR-F2-S02 (idiomatic LNF).** Each LNF preserves meaningful spelling, hyphenation, casing, and modifiers.
* **SCR-F2-S03 (two registers).** Tech is faithful and Plain is explanatory without added scope.
* **SCR-F2-S04 (lexical boundary).** No note substitutes for behaviour, obligation, measurement, kind, assignment, Work, or evidence.
* **SCR-F2-S05 (no cross-source claim).** F.2 asserts no equivalence, hierarchy, transfer, or permission between local meanings.
* **SCR-F2-S06 (minimal generality).** Each LocalSenseClaim is no broader than its source use and receiving question.

#### F.2:15.2 - Regression

* **RSCR-F2-E01 (edition change).** A changed edition produces a newly recovered claim only where meaning changed; earlier source identity remains visible.
* **RSCR-F2-E02 (normaliser stability).** LNF edits do not silently widen or narrow the claim.
* **RSCR-F2-E03 (language honesty).** Translation does not create unproved sameness.
* **RSCR-F2-E04 (no stealth relation).** New notes still contain no cross-source identity or use claim.
* **RSCR-F2-E05 (head-term focus).** The working set remains small and tied to actual downstream questions.

### F.2:16 - Didactic distillation

> “Name the exact source and edition, find the passage, and say under which reference scheme you are reading it. Keep the source’s own expression, add a faithful Tech label and a helpful Plain label, and state its local meaning in one sentence. Stop there. The same spelling elsewhere proves nothing. Use F.17 only if you need a stable address, and use F.9 only if a real relation between two local meanings must be tested.”

### F.2:End

