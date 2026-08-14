## F.3 - Source-Local Sense Clustering

**“Under one explicit interpretation basis, merge aliases that make the same local claim and split uses that do not.”**
**Status.** Architectural pattern.
**Depends on.** F.1 **Question-Relative Source Selection**; F.2 **Term Harvesting & Normalisation**; F.17 for the optional three-part local-sense cell; E.10.D1 **Recovering What “Context” Means in Use**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.4 **SystemRoleKindDescription**; F.7 **Concept-Set Table**; F.8 **Mint or Reuse Decision**; F.9 only when two exact local meanings need a tested relation.
**Aliases (informative).** *source-local clustering*; *sense consolidation*.

### F.3:1 - Intent & applicability

**Intent.** Consolidate the expressions recovered by F.2 into a small set of source-local meaning claims under an explicit source and edition and an effective reference scheme. Merge aliases that the source uses interchangeably; split uses whose argument patterns, entailments, or practical consequences differ. The result stays local to its stated interpretation basis.

**Use this when.** Several expressions or uses from a selected source may carry one meaning, or one expression may carry several meanings that matter to the receiving question. Repeat when a changed passage, edition, or interpretation basis changes that partition.

**Do not use this when.** The local meaning is already clear enough, or the question is whether two meanings from distinct interpretation bases are related. That is an F.9 question. F.3 creates no kind, assignment, cross-source sameness, or permission.

### F.3:2 - Problem Frame

Source-local lexical notes often over- or under-differentiate meaning:

1. **Over-split:** an abbreviation and its full form are treated as different meanings despite interchangeable source use.
2. **Under-split:** one gloss covers incompatible argument patterns or conclusions.
3. **Source drift:** different chapters, editions, or translations are blended without checking whether the interpretation basis changed.
4. **Didactic drift:** the Tech and Plain labels begin to teach different things.

F.3 repairs this by testing usage under the exact source basis rather than by counting strings.

### F.3:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| **Parsimony vs fidelity** | Few claims are easier to teach; too few erase distinctions the source relies on. |
| **Usage vs definition** | Recover how the source uses an expression, not an imported dictionary meaning. |
| **Labels vs idiom** | Tech stays source-faithful while Plain helps a newcomer without widening the claim. |
| **Stability vs revision** | Local meanings should remain citable yet change when the source evidence really changes. |

### F.3:4 - Core idea (didactic)

**Cluster by source use, not by spelling.** Under one explicit interpretation basis:

* **Same local meaning:** expressions are interchangeable in the relevant source passages and no source-grounded test makes them support different conclusions.
* **Different local meanings:** their argument patterns, entailments, temporal stance, or practical consequences differ.

The cluster’s outcome is a **LocalSenseClaim**, with a Tech and Plain label pair, supporting expressions, and an optional counterexample. If durable reuse needs an address, use F.17’s `SchemeSenseCell = <ReferenceScheme, LocalExpression, LocalSenseClaim>`. The cell has three parts; it is not a two-part pair and does not make the claim global.

### F.3:5 - Minimal vocabulary (this pattern only)

* **Interpretation basis** — the exact source and edition and the effective `U.ReferenceScheme` used to understand the selected passages.
* **Unit** — a source-local lexical note from F.2.
* **LocalSenseClaim** — the one-sentence claim that a cluster of source uses supports under that basis.
* **Supporting expressions** — the F.2 expressions consolidated by the claim.
* **Counterexample** — a short source-grounded use that must not be covered by this claim.
* **SchemeSenseCell** — F.17’s optional stable address; it carries the scheme, an expression, and the local-sense claim.
* **Usage cue** — collocation, paraphrase, argument pattern, or entailment that suggests a merge or split; a cue is evidence to inspect, not a decision by itself.

### F.3:6 - Solution — how to think about clustering

#### F.3:6.1 - Consolidate source-blessed aliases

If spelling variants, abbreviations, or explicit synonyms are interchangeable in the relevant passages and do not change a conclusion, let one LocalSenseClaim cover them.

*Example:* ITIL’s *service-level objective* and *SLO* may support one local claim when the cited edition uses them interchangeably.

#### F.3:6.2 - Split incompatible argument patterns

Split when the same head takes materially different participants or occupies a different place in the source’s propositions.

*Example:* a BPMN *event* as a diagram node is not an outage occurrence merely because a tutorial uses the same word narratively.

#### F.3:6.3 - Split divergent entailments

If one use entails occurrence in time and another entails a design structure or capability, the uses support different claims.

*Example:* a PROV *activity* is a time-bounded occurrence; that claim does not describe a static algorithmic capability.

#### F.3:6.4 - Prefer the coarsest adequate partition

Merge candidates when no source-grounded test relevant to the receiving question distinguishes them. Split when a concrete counterexample would otherwise be admitted. Do not split merely to fill a taxonomy.

#### F.3:6.5 - Keep labels honest

Keep the Tech label in the source’s idiom. Make the Plain label explain the same claim to a careful newcomer. Neither label is the value being described, and neither may widen the claim.

#### F.3:6.6 - Address only recurring uses

Ordinary prose may cite the source, expression, and claim directly. Mint an F.17 cell only when the local meaning must be reused, compared, or traced repeatedly.

### F.3:7 - Outputs

For each interpretation basis used by the receiving question, F.3 yields a small set of local-sense claims. Each has:

* a Tech and Plain label pair;
* a one-sentence LocalSenseClaim;
* the supporting expressions and passages;
* an optional counterexample that sharpens the boundary;
* an optional F.17 SchemeSenseCell when durable addressability is worth its cost.

These are reference points for reasoning. They are not mandatory records, and their proximity creates no relation.

### F.3:8 - Invariants

1. **Basis explicit.** Every LocalSenseClaim names the source and edition and the effective reference scheme needed to interpret it.
2. **Parsimony.** Prefer the coarsest partition that preserves source-grounded differences relevant to use.
3. **Idiomatic Tech.** The Tech label remains source-faithful.
4. **Didactic Plain.** The Plain label aids comprehension without adding scope.
5. **Usage first.** Claims follow source passages, not imported taxonomies.
6. **Counterexample rule.** A source-grounded counterexample that matters to the receiving question forces a split or tighter claim.
7. **Category boundary.** A local-sense claim does not establish behaviour, obligation, measurement, kindhood, assignment, or Work.
8. **No relation by clustering.** F.3 establishes no cross-source identity, hierarchy, Bridge, substitution, or permission.

### F.3:9 - Self-checks

* **Same-conclusion test.** Would the candidate uses ever change a source-grounded conclusion relevant here? If not, merge.
* **Argument probe.** Substitute the participants from one use into the other. If the source proposition fails, split.
* **Entailment probe.** Does one use imply an occurrence while the other implies a description, kind, or status? Split.
* **Label inversion.** Read the Plain label alone. If it invites a broader claim, tighten it.
* **Counterexample ping.** State a short use that must be excluded. If it falls inside the claim, refine the boundary.
* **Memory rule.** If a careful reader cannot recall the few relevant claims, the partition is probably too fine.

### F.3:10 - Anti-patterns & remedies

| # | Anti-pattern | Symptom | Why harmful | Remedy |
| --- | --- | --- | --- | --- |
| **A1** | String = sense | Surface identity decides the cluster. | Different propositions collapse. | Compare argument patterns and entailments. |
| **A2** | Cross-source creep | A BPMN use is folded with a PROV use inside F.3. | The interpretation basis changes unnoticed. | Finish each local claim first; test any relation in F.9. |
| **A3** | Over-granulation | *SLO* and its full form become separate claims without a difference in use. | Friction rises without gain. | Consolidate source-blessed aliases. |
| **A4** | Under-granulation | Diagram node and real occurrence share one claim. | Later inferences contradict each other. | Split on argument or entailment conflict and add a counterexample. |
| **A5** | Imported definition | A dictionary replaces the selected source passages. | The result is no longer source-local. | Ground the claim in the actual passages. |
| **A6** | Label drift | Plain adds scope not present in Tech or the claim. | The cold reader learns the wrong concept. | Keep both labels within the same claim. |
| **A7** | Substantive leakage | A sense line contains policies, equations, or kind criteria. | The lexical note is asked to establish a substantive fact about another value. | Route the claim to its direct pattern. |
| **A8** | Edition blend | Two editions with changed usage share one unqualified claim. | Replay and comparison become unreliable. | State each basis; merge only if evidence supports the same claim. |
| **A9** | Cue worship | Similar collocations are treated as proof. | Correlation replaces source meaning. | Use cues to locate passages, then test propositions. |
| **A10** | Time blur | A design-time use and a run-time occurrence are clustered together. | MethodDescription and Work collapse. | Split and use F.11, A.3, and A.15 for the substantive distinction. |

### F.3:11 - Local-Sense Cards

An optional one-glance card may show:

* **source and edition**;
* **effective reference scheme**;
* **Tech and Plain labels**;
* **LocalSenseClaim**;
* **supporting expressions and passages**;
* **counterexample**;
* **F.17 cell**, only when one is actually used.

The card is a display. Its fields do not create a new object or relation.

### F.3:12 - Worked examples

#### F.3:12.1 - BPMN 2.0

**Process (workflow graph).** Claim: a graph of flow nodes and sequence flows that specifies orchestration among participants. Supporting expressions may include *process*, *process model*, and *business process* where the cited passages use them for the diagram. Counterexample: “this process took five minutes” describes an occurrence, not this design claim.

**Event (node).** Claim: a typed diagram node marking starts, ends, or intermediates. Counterexample: “the outage event happened at 13:05” describes an occurrence.

#### F.3:12.2 - PROV-O

**Activity.** Claim: a time-bounded occurrence that uses or generates entities and may be associated with agents. Counterexample: a sorting algorithm as a reusable way of doing is not an occurrence.

**Agent.** Claim: an entity that bears responsibility for an activity’s effects under the PROV scheme. Counterexample: an RBAC permission role is not thereby a PROV agent.

#### F.3:12.3 - ITIL 4

**Service-level objective and SLO.** One claim may consolidate the full form and abbreviation when the cited edition uses them interchangeably: a target value or range for a service characteristic. Counterexample: an observed availability value is evidence, not the target.

**Incident.** Claim: an unplanned interruption or reduction in service quality. Counterexample: a plant sensor fault is not an ITIL incident unless another relation is separately established.

#### F.3:12.4 - SOSA/SSN

**Observation.** Claim: an act applying a procedure to a feature of interest to obtain a result. Counterexample: “20 °C” is a result value, not the observation act.

#### F.3:12.5 - OWL 2

**SubClassOf.** Claim: every instance of one class is an instance of another. Counterexample: `rdf:type` relates an individual to a class.

**EquivalentClasses.** Claim: two class expressions have the same instances under the OWL semantics. Counterexample: `owl:sameAs` is individual identity.

#### F.3:12.6 - IEC 61131-3

**Task.** Claim: a cyclic or event-driven runtime unit that invokes programs. Counterexample: a control algorithm or program description is not the task occurrence.

### F.3:13 - Safe reasoning moves

1. **Alias consolidation.** Merge expressions only when the source uses them interchangeably for the current question.
2. **Argument split.** Split uses whose required participants differ materially.
3. **Entailment split.** Split when the uses support different conclusions.
4. **Parsimony merge.** Merge when no relevant source-grounded test distinguishes the candidates.
5. **Counterexample trigger.** Tighten or split a claim that admits a concrete excluded use.
6. **Label check.** Tech stays idiomatic; Plain explains without widening.
7. **Address check.** Create an F.17 cell only when recurring use needs a stable address.
8. **Edition check.** Re-evaluate the interpretation basis before carrying a claim across an edition change.
9. **Coverage ping.** If a frequent source expression that matters to the receiving question has no local-sense claim, check whether one useful cluster is missing.
10. **Stop rule.** Do not infer a relation to another local meaning from clustering alone.

### F.3:14 - Relations

**Builds on:**

- Use **F.1** for the finite source cut and receiving question.
- Use **F.2** for exact expressions and source-local lexical notes.
- Use **F.17** for `<ReferenceScheme, LocalExpression, LocalSenseClaim>` only when a stable address is needed.
- Use **E.10.D1** to keep source, scheme, claim scope, model use, and working situation distinct when *context* wording is encountered.

**Constrains:**

- **F.4** may cite an exact cell but never infers a local system-role kind from it.
- **F.7** displays exact local claims or cells and already obtaining relations for one stated comparison or use; F.3 clustering creates neither a row relation nor permission.
- **F.8** compares proposed wording with exact existing designations and claims without treating either as the value being named.
- **F.9** tests a relation only between exact local meanings whose interpretation bases differ. F.3 establishes no Bridge, cross-source sameness, substitution, or use licence.

**Used by.** Part C patterns may cite a local-sense claim under its exact source and scheme; the direct pattern still defines or constrains the substantive value or relation in the example.

### F.3:15 - Migration notes

1. **Usage clarifies.** Merge only when the source-grounded distinction test fails.
2. **Usage diverges.** Split and add a counterexample when argument patterns or entailments pull apart.
3. **Edition changes.** Recover the changed basis and claim; do not automatically invent a new universal container.
4. **Labels drift.** Repair Tech or Plain without silently changing the claim.
5. **Dormant claim.** Omit it from the active comparison when it no longer changes the receiving answer; do not fold it into another claim without evidence.
6. **Bridge temptation.** Record the question for F.9; do not answer it in F.3.

### F.3:16 - Acceptance tests

#### F.3:16.1 - Static conformance

* **SCR-F3-S01 (basis).** Every LocalSenseClaim names its source and edition and the effective reference scheme.
* **SCR-F3-S02 (labels).** Tech and Plain denote the same bounded claim.
* **SCR-F3-S03 (fidelity and time stance).** Each claim is grounded in cited source use, preserves any source-grounded design-time, run-time, or other temporal distinction, and contains no imported substantive calculus.
* **SCR-F3-S04 (parsimony).** The claim set is small enough for the receiving question.
* **SCR-F3-S05 (counterexample).** Ambiguous heads have a concrete boundary test.
* **SCR-F3-S06 (no inferred relation).** Clustering asserts no cross-source identity, hierarchy, transfer, or permission.

#### F.3:16.2 - Regression

* **RSCR-F3-E01 (merge soundness).** Every merge has a failed relevant distinction test.
* **RSCR-F3-E02 (split necessity).** Every split cites an argument, entailment, temporal, or counterexample difference.
* **RSCR-F3-E03 (edition honesty).** Changed editions are not silently absorbed into an old claim.
* **RSCR-F3-E04 (label stability).** Label changes do not change the claim unnoticed.
* **RSCR-F3-E05 (downstream continuity).** After a split or merge, direct citations and any F.17 cells remain unambiguous; no silent aliasing occurs.

### F.3:17 - Didactic close

> “Start with one explicit source and interpretation basis. Merge aliases only when the source uses them interchangeably and no relevant conclusion changes. Split uses when their participants, entailments, or time stance differ. Give each result one faithful Tech label, one helpful Plain label, and a short counterexample. Use an F.17 cell only when recurring work needs the address. Nothing in this clustering makes two sources the same; test that separately in F.9.”

### F.3:End

