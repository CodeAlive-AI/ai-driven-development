## F.7 - Concept-Set Table

**“Put exact local meanings and already established relations side by side; let the table display the argument, never create it.”**

**Status.** Architectural pattern.
**Depends on.** E.10.D1 **Recovering What “Context” Means in Use**; F.0.1 **Source-Local Meaning Recovery**; F.1 **Question-Relative Source Selection**; F.2 **Term Harvesting**; F.3 **Source-Local Sense Clustering**; F.17 for optional exact cells; F.5 **Naming Discipline**; F.9 for actual semantic relations and their separate bounded-use claims.
**Coordinates with.** F.4 **SystemRoleKindDescription**; F.6 **SystemRoleAssignment and Performed-Work Attribution Check**; direct Part C patterns for the compared values; C.16 for characteristics; A.6.9 when umbrella sameness wording must be repaired before a relation is asserted.
**Aliases (informative).** *Concept-Set table*; *comparison grid*; *Giants’ table*.

### F.7:1 - Intent & applicability

**Intent.** Give a reader one compact surface for comparing exact source-local claims, optional F.17 cells, and any relations that already obtain between them. The table also shows the stated comparison or receiving use, direction, losses, evidence, and counterexamples. It makes a distributed argument readable without turning row membership into sameness or permission.

**Use this when.** Two or more selected sources must be compared for one named question, teaching contrast, designation choice, or receiving use, and prose alone scatters the relevant distinctions.

**Do not use this when.** One local claim is enough, or no receiving comparison is named. A table is optional. It creates no value, kind, relation, classification, assignment, evidence use, reliance, verdict, or authorisation.

### F.7:2 - Problem frame

Cross-source comparison commonly fails through:

1. **Silent equivalence:** similar labels are treated as one meaning.
2. **Loss denial:** an actual relation is shown without direction or limitation.
3. **Name inflation:** a new umbrella label is coined merely because several entries share a row.
4. **Cognitive scatter:** source meanings, relations, evidence, and the receiving question are separated across documents.

### F.7:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| **Locality vs comparison** | Each meaning remains source-local, yet the reader must compare them. |
| **Didactics vs fidelity** | A compact row must not hide direction, loss, evidence, or a missing relation. |
| **Simplicity vs completeness** | The page should be memorable without pretending that the table contains the full proof. |
| **Similarity vs relation** | Entries may look alike while no identity, hierarchy, or substitution relation obtains. |

### F.7:4 - Core idea (didactic)

A **Concept-Set row** is a didactic grouping for one stated comparison or use. It contains:

* the exact sources and editions;
* each source-local claim, or its F.17 SchemeSenseCell when durable addressability is useful;
* every **already obtaining** relation that matters here, with direction and declared loss;
* the separate conclusion about the named receiving comparison or use;
* the evidence or direct pattern that supports each substantive claim;
* a counterexample or boundary showing where the comparison stops.

The word *set* names the entries collected for display. It does not assert that they are one value. A row may show an identity, overlap, ordering, incompatibility, disjointness, or no relation at all, but only because that claim is established outside the layout. F.9 is used only when the actual relation is between distinct local meanings. For every other relation, cite the pattern that defines, constrains, or tests it.

### F.7:5 - Minimal vocabulary

* **Local entry** — an exact LocalSenseClaim or optional F.17 SchemeSenseCell, with its source and edition and effective scheme.
* **Obtaining relation** — a relation already supported under its direct pattern; it is not inferred from co-placement.
* **Direction** — which participant is source and which is target when the relation is asymmetric.
* **Loss or limit** — what the relation or receiving use does not preserve.
* **Receiving-use conclusion** — the separate claim that judges whether and how the entries and relations may be used for one named purpose.
* **Contrast row** — a row that teaches a difference or an unresolved comparison and expressly asserts no sameness.
* **Characteristic** — a comparandum defined by its direct characteristic pattern; a table may display measured or target values but does not define the characteristic.

### F.7:6 - The table

Use the smallest columns that make the current argument recoverable:

| Comparison or use | Exact source-local entries | Obtaining relations and direction | Loss and boundary | Basis and evidence | Receiving-use conclusion |
| --- | --- | --- | --- | --- | --- |

For a teaching contrast, the relation column may say **none asserted** and the conclusion may say **keep distinct**. For an F.9 relation, show its declared relation kind, direction, CL if that relation actually defines one, and loss. Do not compute a row-wide CL or replace the separate bounded-use claim with a table label.

**Reading rules:**

1. **Entries stay local.** A cell cites the source’s expression and claim; it is not a translation supplied by the table.
2. **Relations stay direct.** For each relation, cite the pattern that defines, constrains, or tests it and the evidence supporting the claim.
3. **Use stays separate.** “These may be compared for this report” is a claim with its own basis, not a property of the row.
4. **Unknown stays unknown.** A blank or unresolved relation is not an invitation to infer similarity.
5. **Loss stays visible.** If the limit needs more than one line, link to the underlying relation or evidence rather than compressing it away.

The nickname **Giants’ table** recalls that comparison relies on prior source work. It signals humility toward those sources, not authority supplied by the table.

### F.7:7 - Conceptual construction

* **Start from a question.** State the comparison or receiving use before selecting entries.
* **Bring exact local meanings.** Use F.0.1, F.2, F.3, and F.17 only as needed.
* **Bring relations, do not manufacture them.** Cite the direct pattern and evidence for each relation that matters.
* **State the receiving-use conclusion separately.** Say what the current comparison permits, with its basis and limits.
* **Keep the row small.** Usually two to four entries are enough; add another only when it changes the answer.
* **Use contrast honestly.** When no adequate relation is established, show the difference rather than forcing a unification.

### F.7:8 - Invariants

1. **Exact entries.** Every filled source-local cell identifies the exact source and edition and claim, or an exact F.17 cell.
2. **No row-created relation.** Co-placement, matching labels, or a shared FPF designation establishes nothing about the entries.
3. **Direct relation basis.** Every stated relation cites its direct pattern and available evidence; F.9 is conditional, not universal.
4. **Separate receiving use.** Any conclusion about comparison, substitution, reporting, or reuse is stated and supported separately.
5. **Direction, time stance, and loss.** Asymmetric relations show direction; any design-time, run-time, or other temporal difference that changes the comparison is explicit; every material limitation remains visible.
6. **No automatic closure.** Relations are not completed pairwise or transitively merely to fill a row.
7. **No universal row type.** A `senseFamily` label is not required and cannot substitute for an intensional account of what is being compared.
8. **Parsimony.** Keep only entries and columns that change the current answer.
9. **Didactic bound.** Split a row that a careful reader cannot understand in about thirty seconds.

### F.7:9 - Micro-illustrations

> The examples show table shapes. Every positive relation still requires its own evidence in an actual use.

#### (a) Class-order comparison

| Comparison or use | Exact source-local entries | Obtaining relations | Loss and boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Explain two class-order notations | OWL 2 `SubClassOf`; FPF `U.SubtypeRelation` claim | An explicit representation or semantic relation, if established for the selected expressions | OWL profile semantics and FPF kind criteria may differ | C.3, C.29, A.6.3.RT, and cited sources | Use one didactic gloss only within the stated notation comparison; do not include FCA order by resemblance. |

#### (b) Measurement comparison

| Comparison or use | Exact source-local entries | Obtaining relations | Loss and boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Compare values against a service target | SOSA result claim; ISO 80000 quantity value; ITIL metric value | Exact measurement, scale and unit, and any source-local semantic relations that actually obtain | Composite ITIL indices may lack unit fidelity | C.16, F.9 when needed, cited observations | Comparable only for the named characteristic, scale conversion, population, and window. |

#### (c) Contrast: *process*

| Comparison or use | Exact source-local entries | Obtaining relations | Loss and boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Prevent homonym collapse | BPMN workflow graph; PROV time-bounded activity; thermodynamic trajectory | **None asserted by this row** | Design structure, occurrence, and trajectory are different subjects | F.0.1, F.3, and direct source passages | Keep distinct unless a later question establishes a specific relation. |

### F.7:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **AP-1** | Row-created sameness | Entries are called “the same” because they share a row. | Layout is mistaken for evidence. | State the actual relation or mark a contrast. |
| **AP-2** | Scope label as licence | “Naming-only” or another row label is treated as permission. | The receiving-use claim and its evidence disappear. | Write the use conclusion separately. |
| **AP-3** | `senseFamily` typing | One broad label is used instead of explaining the comparison. | Hidden kinds and relations remain unnamed. | State the intensional comparison and direct relation. |
| **AP-4** | Temporal blur | Design descriptions and Work occurrences are treated as interchangeable. | MethodDescription and Work collapse. | Show the distinction and any actual relation through F.11, A.3, and A.15. |
| **AP-5** | Loss denial | A relation is shown without its material limitation. | Readers over-transfer. | Add the loss and a concrete counterexample. |
| **AP-6** | Row CL | A minimum or average CL is computed across heterogeneous relations. | One number collapses unrelated claims. | Keep CL only on the F.9 relation that declares it; assess the receiving use separately. |
| **AP-7** | Overwide row | Many sources are added “for completeness”. | Differences hide and the entry cost rises. | Keep two to four answer-changing entries. |
| **AP-8** | Minted paraphrase | A cell replaces the source expression with a new umbrella term. | Provenance and locality vanish. | Cite the exact local claim; put any selected designation in its own column. |
| **AP-9** | Duplicate rows by wording | The same argument is repeated under different labels. | Readers infer distinct concepts where none were established. | Keep one comparison and let F.5 manage aliases. |
| **AP-10** | Automatic transitivity | A–B and B–C are used to assert A–C. | Relation composition may not hold or may add loss. | State only relations whose composition is justified by their direct patterns. |

### F.7:11 - Worked examples

#### F.7:11.1 - Actor wording across BPMN and PROV

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Choose a plain-language heading for a teaching paragraph | BPMN **Participant** claim; PROV **Agent** claim | No identity asserted; any F.9 relation must be established for the exact claims | PROV agents include software and organisations; BPMN participants have model-specific structure | Source passages and F.0.1 | The word **party** may be used as an explanatory umbrella only in this paragraph if the sentences retain each source’s distinct claim. |

#### F.7:11.2 - Runtime occurrence comparison

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Report selected PLC task runs as provenance activities | IEC task-execution claim; PROV Activity claim | A stated source-local semantic or representation relation, direction IEC → PROV, when actually established | PROV omits scan-cycle and scheduling semantics | F.9 or the direct representation pattern plus evidence | Report only the covered occurrence facts; do not infer that every PROV Activity is an IEC task run. |

Performed-Work attribution remains an A.15.1 and F.6 claim about actual Work and system-role assignment. The table supplies neither.

#### F.7:11.3 - Measured value and target

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Judge an observed service characteristic against a target | SOSA observation and its result; ISO quantity value if used; ITIL service target | Measurement, scale, and unit relations; F.9 only for a genuine local-meaning relation | Composite KPI, sampling, and unit limits | C.16, A.10, B.3, and F.12 | Compare only the named characteristic, population, and window with adequate evidence. |

#### F.7:11.4 - Class inclusion and FCA order

A contrast row may show OWL class inclusion, FPF subtype, and FCA concept order together while stating that FCA order is not class inclusion. A positive relation between the first two is still a separate claim with its own semantics and evidence.

#### F.7:11.5 - *Role* trigger word

Show NIST RBAC **role** as a permission grouping and a local system-role-kind claim as a kind whose instances are Systems. Mark them **distinct subjects**. Use E.10.ROLE to recover other uses such as relation participation or signature position; do not assign them one `senseFamily` merely because the spelling matches.

### F.7:12 - Safe reasoning moves

1. **Name the comparison.** What question or receiving use makes the row worth having?
2. **Recover each entry.** Cite its exact source, scheme, expression, and local claim.
3. **List only obtaining relations.** For each, state direction when relevant, the pattern that defines, constrains, or tests it, the supporting evidence, the loss, and any temporal difference that changes the comparison.
4. **Judge the use separately.** Explain what the named use may conclude and why.
5. **Expose absence.** When no relation is established, say so and use a contrast row.
6. **Resist closure.** Do not invent missing pairwise or transitive relations.
7. **Extend cautiously.** Add a source only when its claim or relation changes the answer; re-evaluate the use conclusion.
8. **Keep evidence visible.** A table cell never replaces the evidence-use or reliance relation.

### F.7:13 - Relations

**Builds on:**

- Use **F.1** for the exact source cut and receiving question, and use **F.2** and **F.3** for exact expressions and source-local claims.
- Use **F.17** only when durable local-meaning addresses are needed.
- Use **F.5** for selected designations without making them the values being named.
- Use **F.9** to define and test a relation between exact local meanings and to state the separate bounded-use claim when that is the actual relation family. A table creates none of these facts.

**Constrains:**

- **F.4** may cite a table for reader navigation, but the direct kind description and C.3 membership criterion remain the basis for a local system-role-kind claim.
- **F.6** may reuse a designation from the table; the row supplies neither classification, assignment, Work, nor performed-work attribution.

**Used by.** Part C patterns may use the table as a didactic comparison surface. B.3 may rely only on exact evidence and obtaining relations, never on row position or a computed row score.

### F.7:14 - Migration notes

1. **Relation changes.** Update the exact relation cell and re-evaluate only the receiving-use conclusions that depended on it.
2. **New source.** Do not auto-expand rows; add it only if it changes the stated comparison.
3. **Local claim splits.** Replace the old entry with the relevant child claim or split the comparison.
4. **Use widens.** Re-evaluate the new use directly; a former row label grants no promotion.
5. **Designation changes.** Update F.5 wording without changing source-local entries or relations.
6. **Edition changes.** Recover the successor claim and recheck affected relations; preserve the earlier source identity where historical claims remain relevant.

### F.7:15 - Acceptance tests

#### F.7:15.1 - Static conformance

* **SCR-F7-S01 (exact entries).** Every local entry identifies an exact claim or F.17 cell and its source and edition.
* **SCR-F7-S02 (no row-created fact).** No relation or permission is inferred from co-placement, label similarity, or layout.
* **SCR-F7-S03 (relation basis).** Every positive relation cites the pattern that defines, constrains, or tests it, states direction where relevant, and cites its evidence.
* **SCR-F7-S04 (receiving use).** Every practical use conclusion is separate from the row and has its own basis.
* **SCR-F7-S05 (loss disclosure).** Material limitations and counterexamples remain visible.
* **SCR-F7-S06 (parsimony).** Every extra entry changes the current comparison or use.

#### F.7:15.2 - Regression

* **RSCR-F7-E01 (relation drift).** A changed relation triggers re-evaluation of dependent use conclusions, not a global row score.
* **RSCR-F7-E02 (sense split).** A split local claim leaves no ambiguous cell reference.
* **RSCR-F7-E03 (use integrity).** No consumer treats a row label as licence outside the stated conclusion.
* **RSCR-F7-E04 (no stealth growth).** New entries create no silent relation, closure, or widened use.

### F.7:16 - Didactic distillation

> “A Concept-Set table is a comparison surface. Put the exact source-local claims in it, then list only relations that have already been established, with direction and loss. State separately what one named comparison or use may conclude and why. A shared row, a shared label, or a minimum score proves nothing. If no relation is known, show a contrast. The table makes the reasoning easier to read; it never supplies the reasoning.”

### F.7:End

