## C.20 - Composition of `U.Discipline` (Discipline-CAL)
> **Status:** Stable
> **Type:** Pattern

### E.24.UK settlement

`U.Discipline` is the admitted durable holon kind for one exact field-level practice-and-knowledge whole. C.20 supplies the kind-specific construction criterion; A.1 recognizes one exact candidate under that admitted kind only after the candidate, constituents, obtaining constructive relations, assembly, identity or reidentification rule, composition-grounded whole characteristic, and larger-assembly compatibility are recoverable.

The kind is not established by a field name, subject domain, curriculum, department, professional body, journal, bibliography, standards folder, method family, bridge set, comparison policy, publication set, selected relation structure, or count of local viewpoints. A discipline is not a `U.System` or `U.Episteme` by default. A system, episteme, method, work occurrence, publication occurrence, bridge, comparison, and selected `U.Structure` retain their own identities even when they are used in work concerning a discipline.

C.20 directly governs the narrow `DisciplinePartOfRelation` and the complete discipline-construction test. It does not introduce separate public U-kinds for applied discipline, transdiscipline, tradition, or lineage. Applied, multidisciplinary, transdisciplinary, tradition, lineage, school, and edition wording remains useful only as a separately governed classification, historical claim, or description whose exact criterion is stated.

### C.20:0 - Use This When

Use this pattern when a team needs to decide whether an apparent field is one durable practice-and-knowledge whole rather than a convenient label or collection. Typical moments include:

- comparing rival traditions within or across apparent disciplines without letting a shared label, Bridge, or comparison table merge them;
- moving one practice across semantic localities while preserving the exact local meanings, direction, tolerated loss, and discipline boundaries;
- judging whether an exact Method or method family actually belongs to a field assembly rather than being merely registered, used, cited, published, compared, or taught there;
- keeping discipline continuity inspectable while its canon, standards, or accepted practices change, and identifying another whole when the reidentification rule fails;
- deciding whether a research or engineering field has exact parts and a continuing identity;
- deciding whether a theory, school, standard, or subdiscipline is actually a part;
- using an applied, multidisciplinary, or transdisciplinary label without letting breadth wording create a kind or whole.

**Primary EntityOfConcern.** One exact `U.Entity` candidate being tested for recognition as `U.Discipline`. The candidate is recoverable before the classification result; calling it a candidate discipline does not make the result true.

**First useful move.** Name the exact candidate and two independently identified candidate parts: at least one making a knowledge-bearing contribution and at least one making a reusable-practice contribution. Then state why each direct part relation obtains and one whole-forming fact that couples the two contributions. Do this before letting the discipline name support a comparison, selector or dispatcher, health or maturity claim, transport, or edition decision. If those facts are unavailable, stop at the separately governed objects or collection.

**What goes wrong if missed.** A field name starts doing the work of a canon, method repertoire, institution, bridge, comparison policy, and maturity score at once. A card or graph can then manufacture parts, and changes to a journal, standard, method list, or dashboard can silently manufacture a new discipline. Cross-locality reuse can also look valid after local meanings, evidence lanes, or comparison rules have drifted.

**What this buys.** A practitioner can say what the discipline is made of, how the exact parts form one practice-and-knowledge whole, what remains the same through change, and which surrounding objects are merely used by discipline work. That makes comparison, transport, stewardship, and edition work inspectable without reducing the field to a document list or domain label.

**Not this pattern when.** Use domain or catalogue work for a subject-area label; use the effective `ReferenceScheme`, `ClaimScope`, and F.17 local-sense row for one local meaning; use F.9 only when a semantic relation is claimed between two exact F.17 `SchemeSenseCell` values from different semantic contexts and its predicate obtains; C.2.1 and its publication or source-use patterns for one theory, standard, canon item, or their exact episteme edition; C.3, C.2.1, and direct historical or provenance relations for a school, variant, lineage, or classification; A.3.1 and B.1.5 for a Method or composite Method; A.15.1 for dated Work; A.22 for a selected relation organization; A.19.CPM for an actual comparison; C.21 for field-health characteristics; and E.24.PUB for publication. Use C.20 when determining, explaining, or relying on whether one exact field-level candidate has the required construction and continuity. The result may be `true`, `false`, or `unknown`; when the constructive facts are unavailable, stop at a collection.

### C.20:1 - Problem Frame

Disciplines can persist while theories, standards, methods, organizations, publications, and vocabulary change. In practice that persistence is carried and refreshed through knowledge canons, codified practices and standards, and institutional carriers such as journals, professional bodies, curricula, committees, and laboratories, while none of those carrier families is identical to the discipline. FPF therefore still needs a typed, provenance-preserving field-level composition account. That persistence cannot be explained by a stable name or by one fixed five-position card. It needs exact constituents, direct constructive part relations, whole-forming facts, a field assembly, a reidentification rule, and a whole characteristic that the composition produces or sustains.

The practice side and knowledge side must both be real. A bibliography without reusable ways of investigating or intervening is a knowledge collection. A method catalogue without field-level claim organization is a repertoire. An institution may sustain both through work, but the institution is still a separately identified system. C.20 asks when exact parts and their couplings warrant one further whole.

### C.20:2 - Problem

Without a direct construction test:

- labels, organizations, document sets, curricula, or registries are mistaken for disciplines;
- a canon item or method is called a part merely because a community cites or uses it;
- rival traditions are either flattened into false consensus or treated as separate disciplines without an identity test;
- a changed standard, publication, or health score is mistaken for a new discipline edition;
- bridge loss, comparison admissibility, evidence strength, and selector policy leak into discipline identity;
- an optional selected structure is treated as a context holon, subdiscipline, or breadth count.

### C.20:3 - Forces

| Force | Tension |
| --- | --- |
| **Pluralism vs cohesion** | Rival claims and practices can remain visible while the exact assembly must still sustain one field-level whole. |
| **Continuity vs genuine reidentification** | Parts and relations can change while the same discipline continues, but a name must not hide a changed assembly or boundary. |
| **Readable minimum vs constructive assurance** | Ordinary work needs a short part-and-assembly account; reliance-bearing work may need a C.13 trace, evidence, currentness, and assurance. |
| **Local meaning vs cross-field reuse** | A practice or term can be reused through an exact bridge without the bridge becoming a discipline part or merging its endpoints. |
| **Rigor vs agility** | Exact parts and identity are required, while comparison, publication, health, and registry apparatus are added only for a named receiving use. |
| **Didactic presentation vs ontology** | A discipline card can aid reading but none of its rows, columns, or empty positions makes a world-side relation obtain. |

### C.20:4 - Solution - recover the whole from direct construction

#### C.20:4.1 - Run the complete recognition test

Recover six constructive components for the same exact candidate:

1. **Exact candidate.** Identify one exact `U.Entity` and its proposed field boundary. A public name or description is only a designator or episteme about that candidate.
2. **Exact constituents.** Identify every claimed part under its direct kind and identity pattern. The construction must contain at least one exact knowledge-bearing contribution and at least one exact reusable-practice contribution; these are assembly contributions, not fixed part kinds or heterogeneous card positions.
3. **Constructive part relations and assembly.** Recover each obtaining `disciplinePartOf(part, candidate)` occurrence and every other exact whole-forming claim needed by the assembly. A list, co-use, adjacency, or common publisher supplies none of them.
4. **Identity and reidentification rule.** State which constituent, relation, boundary, or coupling changes preserve this candidate and which identify another whole or end the current one.
5. **Composition-grounded whole characteristic.** State at least one exact A.17-governed Characteristic whose value or state is produced or sustained by the practice-and-knowledge composition and is not attributable to one constituent alone. Use A.18 for Scale legality and C.16 only when an actual value is measured.
6. **Larger-assembly compatibility.** State the candidate boundary, exposed practice-and-knowledge interfaces, relevant whole characteristics, and identity-preservation conditions that make it admissible as a possible constituent under at least one governed larger field assembly. This establishes possibility, not an actual larger-discipline part relation.

The candidate is recognized as `U.Discipline` only when all six components and the C.20-specific practice-and-knowledge condition hold. A materialized classification assertion is a separate C.2.1 episteme about the candidate. Evidence can support that assertion and receiving work can rely on it, but neither creates the discipline.

#### C.20:4.2 - Direct `DisciplinePartOfRelation`

C.20 directly governs `DisciplinePartOfRelation`, expressed in Plain register as `disciplinePartOf(partEntity, candidateDiscipline)`. The first participant is one exact `U.Entity` already identified under its subject pattern. The second is the exact candidate `U.Entity` under the C.20 test; this participant meaning does not presuppose that the candidate has already passed the test.

The predicate obtains throughout an interval exactly when all of the following are true:

- the candidate's actual field assembly includes the exact part as a required contributor or a currently realized admitted alternative for one required knowledge-bearing or reusable-practice contribution;
- at least one exact whole-forming claim is true: that contribution connects to the candidate's field boundary, to another required contribution, and to the declared composition-grounded whole characteristic;
- the candidate's direct reidentification rule treats the current part, its contribution, and any allowed replacement as belonging to this continuing assembly.

Mere eligibility for future use is insufficient. A source citation, canon list, standards list, registry row, curriculum position, organizational affiliation, publication, common label, diagram containment, shared audience, bridge endpoint, comparison row, selected structure, work participation, evidence relation, or health reading does not make `disciplinePartOf` obtain.

One occurrence is identified by `<exact part entity, exact candidate, maximal continuous obtaining interval>`. If the same part leaves the assembly and later returns, the two episodes are distinct occurrences. A changed observation or evidence window does not split an ongoing occurrence; actual cessation and resumption under the direct predicate do. Reidentifying either participant also identifies another occurrence.

Multiple contribution claims for the same part do not create several part occurrences during the same continuous interval. If typed declaration reuse is needed, the direct relation has only the two participant meanings above. Canon, practice, organization, bridge, comparison, policy, evidence, publication, and structure fields are not additional `SlotSpec`s. Qualifiers and whole-forming claims keep their subject patterns.

#### C.20:4.3 - State whole-forming claims before choosing notation

Part relations alone do not make one discipline. State the field assembly in ordinary domain language:

- which exact claim-bearing contributions supply the field's knowledge commitments, distinctions, explanatory resources, or admissible questions;
- which exact methods or other independently governed parts supply reusable ways of investigating, designing, intervening, evaluating, or learning;
- which claims state how knowledge contributions constrain, explain, or qualify practice contributions;
- which claims state why separately governed results of actual practice are relevant to evaluation, revision, or replacement of knowledge contributions;
- how incompatible or rival contributions coexist without being silently equated;
- which boundary, stop conditions, exposed interfaces, and substitution conditions keep the assembly one field-level whole.

Each whole-forming statement stays at the lightest truthful disposition supplied by its direct relation pattern or A.6.RCD: an existing direct predicate, a local compound claim, or a reusable predicate-definition episteme. A readable arrow such as `uses`, `supports`, `tests`, `belongs to`, `standardizes`, or `aligns` does not admit a relation kind and does not make a part relation obtain.

The assembly rule names the exact current part relations, contribution meanings, whole-forming claims, permitted alternatives, incompatibilities, boundary conditions, failure conditions, and substitution conditions. A C.13 `Gamma_m.sum` construction trace may report those facts when a named use needs an inspectable account. The trace is a C.2.1 episteme and creates none of the parts, relations, assembly, identity, or characteristic.

The historical signature was `Γ_disc : ⟨EpistemeCanon, StandardsSet, OrgCarriers, {Bridges}, Policy⟩ → U.Discipline`. Read it only as a map into the direct construction account. Its useful intent was to assemble a reviewable field-level whole account, preserve provenance, support separately governed publication of that account, and enable admissible comparison; none of those receiving functions creates the whole.

Every former argument remains available but loses automatic constructor and identity force: `EpistemeCanon` routes to exact canon epistemes and their claims; `StandardsSet` to exact standard epistemes, Methods, and practice claims; `OrgCarriers` to independently identified systems, system-role kinds and assignments, and Work; `{Bridges}` to exact F.9 occurrences and bounded-use propositions; and `Policy` to exact comparison, evidence, assurance, and acceptance declarations under their subject patterns. Section 4.6 gives the complete intake prompts for those families. Historical `Gamma_disc` expressions are therefore only incomplete shorthand for a C.13 construction account. A five-field argument list, Discipline Card, or filled schema does not complete the account and does not have constructor force.

#### C.20:4.4 - Identity, continuity, and change

The discipline's identity is not the extensional part list. It is the exact candidate with its field boundary, practice-and-knowledge assembly principle, obtaining constructive relations, whole-forming architecture, and declared whole characteristic under one direct reidentification rule.

The same discipline may continue through a permitted canon revision, method replacement, institutional change, publication change, or temporary part-relation change when the rule admits that variation and the field boundary, required contribution meanings, essential couplings, and whole characteristic remain within their declared continuity conditions. The rule must say which substitutions are permitted and how the replacement contribution reconnects to the assembly.

A change outside those conditions identifies another candidate or leaves the stronger claim unresolved. When a receiving use asks whether the old whole can still explain the case, run B.2's existing-whole explanation check after the direct C.20 facts are recovered. Loss of evidence, another description edition, a renamed field, or a stale registry entry does not itself end or create a discipline.

"Discipline edition" is therefore not one automatic object. Recover the changed subject:

- revised canon, standard, method description, classification assertion, or discipline description is another C.2.1 episteme when its identity discriminator changes, with historical continuation tested separately;
- a newly available edition has its own E.24.PUB publication occurrence, form, carrier, audience, use, and availability interval;
- an unchanged discipline during a proper interval may be described through the direct temporal and A.14 phase route;
- a changed field assembly outside the reidentification rule requires another discipline candidate, not a renamed description.

Keep the change rationale as claim content of one exact C.2.1-identified revision or decision episteme. When historical continuation is asserted, the assertion about the exact `EpistemeEditionRelation` cites the exact source use, applicable continuity policy or rule, and the preserved and deliberately changed claim, EntityOfConcern, and scheme features that the rule consumes. Revision Work, Method, provenance, change facts, and evidence are case facts; no label establishes continuity. When availability changes, trace the publication transition through the ending and beginning E.24.PUB occurrences with their selected edition, audience, bounded use, form, carrier, and availability intervals. The rationale, edition-relation assertion, publication occurrences, and discipline reidentification result remain distinct; none decides another merely by being recorded.

#### C.20:4.5 - Require a composition-grounded whole characteristic

Name at least one exact Characteristic under A.17, its Scale under A.18, and its direct measurement or evaluation route only when a current use needs a value. A useful local choice is the degree to which the assembly sustains a replayable practice-knowledge coupling: independently identified knowledge contributions constrain field practice, and separately governed practice results can be used to test, revise, or replace those knowledge contributions under declared rules. This is a local characteristic choice, not a new universal kind or scalar score; C.16 governs a measurement chain only when dated measurement Work actually attributes a value.

The value must depend on the composition. Citation count from one episteme, frequency of one method, size of one organization, bridge count, publication count, or a single maturity label is not a composition-grounded whole characteristic. Rival traditions can coexist when their boundaries, incompatibilities, permitted uses, and contribution relations are explicit; cohesion does not require false consensus.

C.21 is the pattern for discipline-health characteristics such as reproducibility, standardization, diversity, and disruption balance. A health reading can reveal pressure to inspect construction or reidentification, but it is not a part, assembly fact, identity rule, or classification result.

#### C.20:4.6 - Keep neighboring objects with their subject patterns

Keep the three boundaries explicit. A **domain** is a subject-area or catalogue designation. A **semantic locality** is the bounded use of exact local meanings under its effective ReferenceScheme, ClaimScope, and direct F.17 pattern; it is not another holon or a discipline constituent by locality alone. A **discipline** is the exact field-level practice-and-knowledge whole recognized by the C.20 construction test. The same or similar word across domains or semantic localities establishes none of shared meaning, one discipline, parthood, or identity. When a use relies on a semantic crossing, state the two exact local senses and cite an F.9 Bridge only if its predicate obtains; field or locality difference alone creates no Bridge. Then test each discipline candidate independently; even an obtaining high-congruence Bridge does not merge its endpoints.

The historical five-position card remains a useful intake palette only if every member keeps its subject pattern and receives no automatic part or identity status. Its complete prompts were:

- **canon candidates:** theories, models, reference works, definitions, proof traditions, benchmark descriptions, and other epistemes treated as canonical;
- **practice and standard candidates:** accepted Methods, norms, standard procedures, measurement conventions, and admissible comparison rules;
- **institutional and organizational candidates:** journals, committees, curricula, professional bodies, laboratories, and other institutional arrangements that may carry or refresh field work;
- **cross-locality candidates:** exact F.9 Bridges, F.17 term or local-sense rows, Bridge descriptions, and loss observations used across semantic localities or source traditions;
- **comparison candidates:** exact Characteristics, Scales, Units, comparators, evidence policies, and CG-Spec declarations used to make a named comparison admissible.

The palette prevents those reader questions from disappearing; it is neither a required five-part decomposition nor a constructor. No category must be filled by ritual. Every exact item remains under the subject pattern below and becomes a C.20 part only when `disciplinePartOf` independently obtains.

| Apparent discipline content | Subject pattern and C.20 boundary |
| --- | --- |
| field or domain name | catalogue, designation, or wording pattern; the name is not the candidate or its construction |
| theory, model, canon item, definition, standard, or practice description | C.2.1 identifies the exact episteme; it becomes a discipline part only if a separate `disciplinePartOf` occurrence obtains |
| reusable method or method family | A.3.1 identifies each Method and B.1.5 any composite Method; use, registry membership, or family similarity is not discipline parthood |
| organization, laboratory, committee, journal operator, or professional body | A.1 identifies any system; its system-role assignments and Work stay direct; carrying or stewarding a discipline is not parthood |
| dated research, engineering, teaching, revision, evaluation, or governance work | A.15.1 identifies each Work occurrence; performing work about or within a discipline does not make the work or performer a part |
| selected organization of relations for one model use | A.22 identifies the dependent `U.Structure`; selection gives it no holonhood or discipline parthood |
| semantic Bridge | F.9 identifies an occurrence only after two exact F.17 `SchemeSenseCell` values resolve and its predicate obtains; a field or locality difference alone creates none, and the Bridge never joins its endpoint disciplines into one whole |
| structural correspondence | Use its direct governor; C.34 applies only to a declared architecture-preservation claim. A structural mapping establishes neither an F.9 Bridge nor one discipline. |
| comparison predicate, characteristic space, comparator, or aggregation | use C.16 for the measured values and A.19.CPM for the exact comparison; comparability is not a discipline constituent or identity condition unless a separate C.20 whole-forming claim makes an exact contribution current |
| publication, form, carrier, card, dashboard, registry, or bibliography | C.2.1, E.17, and E.24.PUB keep content, form, carrier, and availability separate; publication does not construct the field |
| evidence, provenance, currentness, assurance, gate, or authorization | use A.10 for evidence and provenance, G.11 for currentness, B.3 only for an actual named assurance claim, A.21 for gates, and the applicable decision pattern for authorization or choice claims; epistemic support changes no world-side part or identity fact |

Any entity in this table can become an actual part only when it is independently identified and the C.20 predicate separately obtains. Its ordinary association with the field is never enough.

#### C.20:4.7 - Optional bounded-model-use structure

Discipline work can use an independently selected `BoundedModelUseStructure` when the selected organization of exact relations changes how a named model is interpreted or used in that work. State the exact model, direct relation occurrences, selection basis, receiving work or claim, and the organization that matters. A.22 is the pattern for the structure and A.15.1 is the pattern for the dated work.

The structure is optional. It is not the discipline, a constituent by selection, a subdiscipline, a context count, a description, a viewpoint, a whole characteristic, a breadth classification, or a second identity carrier. Several selected structures used in work about one discipline do not create several disciplines; one structure used across several disciplines does not merge them.

#### C.20:4.8 - Breadth, tradition, lineage, and school claims

Applied, multidisciplinary, transdisciplinary, tradition, lineage, and school labels do not carry a universal C.20 classification rule.

- For a project-local kind, use C.3 to state exact intent, membership predicate, scope, and the candidate disciplines that satisfy it.
- A multidisciplinary claim normally needs several independently identified disciplines and exact contribution or use claims; co-listing fields or counting viewpoints is insufficient.
- A transdisciplinary claim must declare the integrative criterion that distinguishes it from side-by-side use. If the claim is that one new discipline exists, run the complete C.20 construction test for that new candidate.
- A tradition, lineage, school, variant, edition, or provenance claim identifies its exact subject and the exact historical-continuation, source-use, method, similarity, edition, derivation, or provenance relation under that relation's subject pattern. Tradition or lineage can organize variants or editions within or across disciplines as an ordinary auxiliary value or a C.3 project-local kind; none is a discipline part, subkind, or public U-kind by label. A public kind requires its own direct governor, identity and use rule, and E.24.UK admission.
- An applied classification states what application-facing criterion is satisfied. Method use, one project, one organization, or one selected structure does not establish it by itself.

The classification can remain a C.2.1 claim without admitting another public U-kind. A changed label or classification result does not reidentify the discipline unless the direct C.20 rule independently says the field assembly changed.

#### C.20:4.9 - Crossing, comparison, evidence, health, and publication are conditional branches

Open these branches only when the named discipline use actually needs them.

**Cross-field or cross-sense use.** A cross-field use may use independently governed claims without a semantic crossing. When an exact cross-context semantic relation is claimed, first resolve two exact F.17 `SchemeSenseCell` values; F.9 identifies an obtaining Bridge only when their semantic-context projections differ and the direct predicate and dependencies are satisfied. A field, scheme, cell, or plane difference alone creates no Bridge. For an obtaining Bridge, keep a separate current C.2.1 bounded-use proposition whose EntityOfConcern is that Bridge and whose ClaimGraph names the proposed action `u`, exact direction `d`, use-specific correspondence rule `r`, tolerated semantic loss `t`, and affirmative or negative polarity. Observed loss and counterexamples remain evidence; the permitted-loss tolerance remains claim content. Neither one reidentifies the Bridge.

For ordinary evidence reliance, use the exact A.10 evidence-provenance relation for the same bounded use. Only `RelianceDisposition=pass` supports that affirmative use; `degrade` supports only the named narrower use, while `abstain`, `reopen`, `evidence-needed`, `assurance-needed`, or `blocked-current-use` does not pass the attempt. Use B.3 only when an actual named assurance claim is current, and require its result for that same bounded assurance use. Authorization and any actual comparison, substitution, translation, publication, or Work occurrence remain with their subject patterns.

**Crossing visibility and presentation checks.** Keep an exact Bridge and separate bounded-use proposition discoverable in an account that relies on that obtaining semantic relation. For a ReferencePlane-only crossing, keep the applicable plane relation and policy discoverable instead; if both facts are current, keep both under their own predicates. Materialize an E.18 `CrossingBundle` only when an independently current E.18 structural `GateCrossing` exists and a named downstream use relies on durable evidence for that structural crossing; if it also relies on cross-semantic correspondence, add E.18's separate F.9 block. E.17 governs publication packaging and A.21 governs any actual GateCheck or GateDecision. For lane purity, inspect the current B.3 result by value: every characteristic keeps its bearer and scale, and any aggregation cites its domain model and assumptions; there is no universal F-G-R-CL fold. Apply E.10 lexical checks to the published labels, keep normative prose notation-neutral, and treat every discipline column as didactic only.

**Comparison or aggregation.** A.17 identifies every exact Characteristic; A.18 supplies its Scale, Unit and legal operations; C.16 supplies a measurement result only when an actual measurement chain exists. A mean over an ordinal Scale and an aggregation that mixes unconverted or incommensurable Units are inadmissible: stop that operation, establish a lawful transformation or comparison scheme, or retain the separate values rather than manufacturing an aggregate. One actual A.19.CPM comparison application binds the profile pair, comparator, claim scope and selected slices, optional predicate, reference scheme and plane, evaluation point or interval, dated comparison Work, operation application, set-valued result, and evidence policy; CPM does not fold or aggregate. Any numeric or profile aggregation is a separate explicit A.19.ULSAM or applicable B.1 `Γ-fold` operation with its own dated Work and result binding. Before either operation, the applicable G.0 CG-Spec route names the exact Characteristic ids, `ScaleComplianceProfile` with Scale, Unit, polarity and legal-operation conditions, `MinimalEvidence`, and either the admitted `ComparatorSet` member for comparison or the declared `Γ-fold` and contributors for aggregation. This pre-operation admissibility check fails closed on missing or unknown declarations or evidence and creates neither equality, an aggregate, nor a winner. An operation that relies on an obtaining F.9 Bridge between two exact F.17 `SchemeSenseCell` values uses the separate Bridge, bounded-use-claim, and reliance branch above; a crossing of exact ReferencePlanes instead cites the applicable plane relation and policy. If both facts are current, state both under their own predicates. A scheme, cell, or plane difference alone creates neither relation. Neither branch supplies the comparison or aggregation scope, predicate, comparator, plane, time, result, or selection.

**Evidence, currentness, and assurance.** Use A.10 for source use and the evidence-provenance path, and G.11 for selected-edition currentness. When an imported source claim supports a construction, classification, comparison, publication, or assurance use, keep the exact source and edition plus only the lane tags, freshness window, or validity conditions that the receiving use consumes. Claims that need no such reliance acquire none of this apparatus merely because they concern a discipline. Open B.3 only for an actual named assurance claim. Its `AssuranceResult` identifies the target claim, assurance use, basis, disposition, limits, and reopen condition. If the argument consumes a characteristic or calculation, name its bearer, property, scale, unit, interpretation, basis, dependency model, assumptions, rule, and rival as applicable. C.20 supplies no default F/G/R/CL lanes, weakest-link fold, `SpanUnion`, congruence penalty, plane penalty, or assurance arithmetic. A Bridge-related penalty is current only when an actual named B.3 assurance claim uses an applicable declared domain model whose current facts and rule yield it; that value belongs only to the calculated `AssuranceResult` for that named use. State `ReferencePlane` only when it changes an exact input or interpretation; when an exact plane crossing is current, cite the applicable plane relation and policy. The selected plane and its relation identify neither a discipline part nor a part relation. Insufficient or unknown support narrows, abstains, requests evidence, reopens, or blocks the attempted assurance use under B.3; it does not make a part relation or whole obtain or cease.

**Health or state view.** C.21 can evaluate typed discipline-health characteristics. Local values such as emerging, consolidating, codified, or fragmenting require their own criteria, Scale, evidence basis, qualification window, and currentness. Any decision threshold belongs to the relevant G.4 AcceptanceClause. A state label, health vector, score, or dashboard transition is descriptive and does not itself reidentify the discipline.

**Description and publication.** The claim-bearing whole expressed by a discipline description, construction trace, comparison report, health series, card, or registry row is identified as an episteme under C.2.1 when that pattern's constitution test holds. E.24.PUB governs any actual publication occurrence and keeps selected episteme edition, audience, bounded-use declaration, form, carrier, and availability interval distinct. Updating or publishing the account changes neither the field assembly nor its past.

### C.20:5 - Archetypal Grounding

#### C.20:5.0 - Keep the System/Episteme contrast without making the table a constructor

The former Tell-Show-Show contrast remains useful because it asks five different reader questions. Read every cell as an independently governed example, not as a slot or a recipe for manufacturing a discipline.

| Reader function | System-side safety scene | Episteme-side discipline scene | C.20 boundary |
| --- | --- | --- | --- |
| **Exact object** | One production line with hazardous operations is an exact `U.System` under A.1; its work and state remain separate. | One exact canon or discipline-description `U.Episteme` states accident-model and tolerable-risk claims about its declared EntityOfConcern under its effective ReferenceScheme. The `SafetyEngineering-SE` field candidate remains another entity. | Neither the system nor one episteme is the discipline; identify the field candidate and test its construction independently. |
| **Concept contribution** | Acceptance clauses and evaluation templates bound to exact rigs and windows are epistemes used by the plant system and its Work, not concepts owned by the system. | Canon content can include causality models, design rules, proofs, benchmarks, formal knowledge bases, proof carriers, and concept schemas under their direct episteme, form, or representation patterns. | Ask which exact claim-bearing contribution is constitutive and which whole-forming claim states how it connects to the assembly; conceptual relevance alone creates no part. |
| **Symbolic representation** | Local SOP and checklist notation can express plant procedures for one bounded use. | CLIF, RDF/TriG, proof scripts, diagrams, and other notation packages can express or represent canon content. | E.17/E.24.PUB and C.29 govern form, carrier, publication, and representation; symbolic appearance identifies none of System, Episteme, or Discipline. |
| **Assembly contrast** | A line-specific standard, plant procedures, and a certifying unit are exact epistemes, Methods, systems, system-role kinds or assignments, or Work inputs around a possible `Safety-Plant-A` field candidate. | Canon papers, formal models, a journal or committee, and system-safety or resilience-engineering tradition claims are likewise separately governed around `SafetyEngineering-SE`. | A list or historical `Gamma_disc` fold constructs neither candidate. For either scene, recover exact parts, obtaining `disciplinePartOf` occurrences, whole-forming couplings, assembly, reidentification, whole characteristic, and larger-assembly compatibility. |
| **Evidence-lane contrast** | LA test campaigns with freshness windows, VA design proofs, and TA tool qualifications can support exact plant-side claims. | VA proofs over kinds, LA replications or meta-analyses, and TA evidence for checkers can support exact canon or construction claims. | A.10 keeps the exact source, currentness, and reliance needed by the use. When an actual named assurance claim is current, B.3 adds only the characteristics and result fields that its argument consumes. Evidence changes no System, Episteme, or Discipline identity and creates no part relation. |

#### C.20:5.1 - Safety engineering as a positive construction

Suppose `SafetyEngineering-SE` is one exact field candidate. C.2.1 independently identifies `HazardCausalityCanon-v5` as a claim-bearing episteme. A.3.1 independently identifies `HazardAnalysisMethod-v4` and `IncidentLearningMethod-v2` as reusable Methods. None is a C.20 part yet.

The field assembly makes these exact contributions current:

- `HazardCausalityCanon-v5` supplies the hazard, causal, and acceptable-argument meanings used by the two Methods;
- `HazardAnalysisMethod-v4` supplies the reusable analysis practice by which those meanings constrain identification and treatment of hazards;
- `IncidentLearningMethod-v2` supplies the reusable practice by which separately governed incident and evaluation results can challenge or refine the canon claims.

The three exact relation occurrences are `disciplinePartOf(HazardCausalityCanon-v5, SafetyEngineering-SE)@I-SE-core-1`, `disciplinePartOf(HazardAnalysisMethod-v4, SafetyEngineering-SE)@I-SE-core-1`, and `disciplinePartOf(IncidentLearningMethod-v2, SafetyEngineering-SE)@I-SE-core-1`. They share the explicitly identified maximal current continuous obtaining interval `I-SE-core-1 = [2024-04-01T09:00Z, open)`: its left boundary is the dated field-assembly activation at which all three contributions first became jointly required. At the continuation check `2026-07-31T23:59Z`, each contribution remains required, the canon meanings remain connected to method preconditions and result meanings as stated by the exact whole-forming claims, the same candidate and reidentification rule continue, and no cessation boundary has occurred; therefore the right boundary remains open. If any contribution ceases and later resumes, that part's interval ends at cessation and a new `disciplinePartOf` occurrence begins at resumption. The actual field assembly requires those contributions, and the reidentification rule admits them as current parts. The local A.17 Characteristic `PracticeKnowledgeCouplingReplayability` has the exact subject `SafetyEngineering-SE` and the ordinal A.18 Scale `broken < partial < replayable`: its criterion asks whether the named canon-to-Method constraints and result-to-canon revision routes remain executable across the declared safety-work classes. No constituent can have that whole value alone. If a current use needs a measured value, C.16 requires the exact measurement subject, method, model, Scale, dated measurement Work, uncertainty, and result episteme; the label alone supplies no reading.

The reidentification rule permits a compatible canon revision or replacement Method only when the field boundary, causal and argument meanings, practice-knowledge feedback, and whole characteristic remain within declared continuity conditions. Removing the feedback route, changing the governing safety concern and field boundary, or replacing the assembly by unrelated document and method lists falls outside the rule.

`Safety Journal`, a standards committee, a university curriculum, a laboratory, a bridge to resilience-engineering terminology, a comparison CG-Spec, and a published discipline card remain separately governed. They are not parts in this case because no separate C.20 predicate has been established for them. For any precise review or teaching Work, use A.13 to identify the actual performer and A.15.1 to admit the dated occurrence independently; add F.6 only if this case must also state exactly under which assignment that Work was performed. The Work may enact a part Method, but it neither becomes the discipline nor proves the three part relations.

For A.1's larger-assembly test, the separately identified rule episteme `EngineeringFieldAssemblyRule-v3` describes a governed larger-field construction whose applicability requires one constituent field to expose stable hazard-constraint meanings, analysis-result meanings, and identity-preserving interfaces to design and verification practices. `SafetyEngineering-SE` has those actual interfaces and its reidentification rule preserves them, so it is compatible with that possible assembly while remaining the same candidate. The rule episteme does not create the compatibility facts, and this result asserts no actual `disciplinePartOf(SafetyEngineering-SE, Engineering-E)` occurrence.

A C.13 `Gamma_m.sum` trace may report the candidate, three parts, three part-relation occurrences, whole-forming claims, assembly, reidentification rule, and whole characteristic. Writing or publishing that trace does not construct `SafetyEngineering-SE`.

#### C.20:5.2 - A department, corpus, and method registry are not yet a discipline

`Safety Department A` performs research and teaching Work. Its repository contains standards and papers, and its registry lists analysis Methods. Those facts establish a system, Work, epistemes, publications, and registry membership under their subject patterns.

They do not yet establish which exact entities are field constituents, any `disciplinePartOf` occurrence, a practice-knowledge assembly, one whole characteristic, or a reidentification rule. The useful result is the recovered collection and work organization. Stop before `U.Discipline`; do not fill missing canon, carrier, bridge, or comparison positions merely to complete a card.

#### C.20:5.3 - Cross-field reuse does not create a transdiscipline

A safety-engineering team proposes to reuse one resilience-engineering term. F.17 resolves the two exact `SchemeSenseCell` values, and their semantic-context projections differ. The stated directed `BridgePredicateProfile` applies to those endpoint readings at its stated as-of basis; the current endpoint meanings satisfy its relation-kind-specific semantic condition and Boolean truth condition; and all required dependencies are present. F.9 therefore identifies an obtaining directed Bridge. A separate bounded-use proposition states the direction, mapping rule, tolerated loss, and polarity for this hazard-review use. Exact review Work may rely on that proposition through A.10, and a comparison may apply A.19.CPM.

These facts establish no `disciplinePartOf` occurrence and no new discipline. Calling the work transdisciplinary requires a declared classification criterion. Claiming one new integrated discipline requires another exact candidate and all six C.20 construction components; one Bridge, two labels, or two selected structures cannot supply them.

#### C.20:5.4 - Canon revision, same field, and another field

`HazardCausalityCanon-v6` changes claim content and is another C.2.1 episteme. Historical continuation from v5 is tested separately. The same `SafetyEngineering-SE` can continue if its C.20 rule permits that replacement and the required contribution meanings, whole-forming couplings, boundary, and whole characteristic persist. The old part occurrence ends and the new one begins; a description or evidence window does not decide those intervals.

If the replacement rejects the field's former causal object, changes the practice-knowledge feedback rule, and changes the field boundary beyond permitted continuity, the same-discipline claim fails. The project then tests another candidate and uses B.2 only if a receiving use needs a whole-reidentification conclusion. A new canon edition, renamed department, or republished card alone decides neither branch.

### C.20:6 - Bias-Annotation

Apply five complementary lenses; the later risk table does not replace them.

| Lens | Question and counter-bias |
| --- | --- |
| **Governance** | Are field names, classification claims, revision rationales, source “steward” or “owner” wording, any separately obtaining kind or assignment, responsibility, authority, ownership, governance, publication Work, and publication availability kept with their subject patterns, or has a name, card, registry, title, or publisher acquired force it does not have? |
| **Architecture** | Are construction, Characteristic/Scale, comparison or aggregation, evidence/assurance, health, publication, and selection still separate branches, or has a convenient CAL/CHR-style record become an omnibus discipline constructor? |
| **Onto/Epist** | Are the discipline, domain designation, semantic locality, system, episteme, description, representation, and evidence claim distinct, with each claim returning to an exact EntityOfConcern and ReferenceScheme? |
| **Pragmatic** | Can ordinary authoring and edition work stop at exact parts, couplings, assembly, and reidentification, while only the receiving comparison, assurance, publication, or decision opens deeper apparatus? |
| **Didactic** | Do twin labels, the System/Episteme contrast, cards, columns, diagrams, and examples aid recognition without supplying hidden parts, relations, kinds, identity, or truth? |

**Scope guard.** Every use is bounded by exact field candidates, semantic localities, scopes, editions, and receiving work. There is no context-free or global discipline established by name, popularity, institutional reach, or a shared vocabulary.

| Bias risk | Failure | Counter-move |
| --- | --- | --- |
| **Label realism** | A familiar field name is treated as the whole. | Recover candidate, parts, direct occurrences, assembly, identity, and whole characteristic. |
| **Institutionalism** | The largest organization carrying the work is treated as the discipline. | Keep the system, system-role kind and assignment, and Work direct; test parthood separately. |
| **Canon or method monocentrism** | One document set or method family stands for both knowledge and practice. | Require independently identified contributions on both sides and exact coupling claims. |
| **Schema completion** | Five filled positions or heterogeneous fields manufacture construction. | Use the two-participant direct relation and ordinary whole-forming claims; treat cards as descriptions. |
| **Bridge universalism** | Translation or high congruence merges fields. | Keep Bridge, bounded-use proposition, reliance, comparison, and discipline construction separate. |
| **Metric reification** | Health or maturity value is treated as discipline identity. | Keep C.21 readings and G.4 thresholds as evaluations over the exact discipline. |
| **Snapshot extensionalism** | Any changed part creates another discipline, or the same part list guarantees sameness. | Apply the assembly-sensitive reidentification rule. |

### C.20:7 - Conformance Checklist

| ID | Passing condition |
| --- | --- |
| `CC-C20-1` | One exact candidate `U.Entity` and proposed field boundary are named before `U.Discipline` recognition. |
| `CC-C20-2` | Every claimed part is independently identified under its subject pattern; at least one exact knowledge-bearing contribution and one exact reusable-practice contribution are current. |
| `CC-C20-3` | Every `disciplinePartOf` occurrence passes the required-or-currently-realized-alternative predicate and is identified by exact participants plus maximal continuous obtaining interval. |
| `CC-C20-4` | Contribution claims and other whole-forming facts are stated in ordinary domain language and retain their direct predicate, local-claim, or reusable-definition disposition. |
| `CC-C20-5` | The assembly names exact parts, relations, required contributions, alternatives, incompatibilities, boundary, stop conditions, and substitution conditions. A card or trace is not its cause. |
| `CC-C20-6` | The direct reidentification rule says which part, relation, coupling, boundary, and characteristic changes preserve or end the whole. |
| `CC-C20-7` | At least one exact A.17 Characteristic is composition-grounded and not reducible to one constituent, count, label, or external health score; A.18 governs its Scale and C.16 opens only for an actual measurement. |
| `CC-C20-8` | Candidate-side interfaces and identity-preservation conditions fit at least one governed possible larger field assembly; an actual larger-discipline part claim still needs its own obtaining occurrence. |
| `CC-C20-9` | Domain names, epistemes, Methods, systems, Work, structures, Bridges, comparisons, publications, evidence, and decisions remain with subject patterns unless the separate C.20 part predicate actually obtains. |
| `CC-C20-10` | Any selected bounded-model-use structure is optional, independently identified, tied to one named receiving use, and creates no part, holon, subkind, viewpoint count, breadth, or identity. |
| `CC-C20-11` | Applied, multidisciplinary, transdisciplinary, tradition, lineage, and school claims state their own criteria; no public U-kind or discipline part follows from wording or counts. |
| `CC-C20-12` | A field, scheme, cell, or plane difference alone creates no F.9 Bridge. A use that relies on an obtaining Bridge separates it from its bounded-use proposition, direction, rule, tolerance, polarity, A.10 reliance or actual named B.3 assurance branch, observed loss when relevant, and actual comparison; a ReferencePlane-only crossing instead cites the applicable plane relation and policy. |
| `CC-C20-13` | Comparison declares characteristic, scale, unit, polarity, comparator, scope, window, and admissible operation under C.16/A.19.CPM; C.20 performs no comparison and defines no reliability fold. |
| `CC-C20-14` | A health value, state label, evidence profile, registry row, description edition, publication occurrence, form, or carrier changes no discipline construction fact by itself. |
| `CC-C20-15` | Any C.13 trace names the already grounded candidate, exact parts, direct occurrences, assembly, identity rule, and whole characteristic; `Gamma_m.sum` or historical `Gamma_disc` syntax creates none of them. |
| `CC-C20-16` | Core prose and labels follow E.10 and remain notation- and tool-neutral; a didactic discipline column carries no hidden semantics. |

### C.20:7.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "TDD discipline" or another Method/tradition label already names a discipline. | Treat "Test-Driven" as a tradition, method-family, or other local classification only under its exact criterion and subject. Identify each Method under A.3.1; identify a discipline only by the complete C.20 construction test. |
| “Safety Discipline Owner” or another owner or steward title proves ownership, parthood, responsibility, or decision authority. | Treat the title as an `E.10.ROLE` trigger. Admit the System that actually performs any Work; recover any local system-role kind, classification, or assignment independently; and cite the exact ownership, responsibility, authority, governance, or other direct relation that obtains. If no pattern establishes the stronger relation, return `missing-governor`. |
| "ClinicalSafetyDomain Governance" or another compound domain-governance label supplies a discipline and its comparison policy. | Separate the subject-area or catalogue label, exact governance system-role kind and assignment, direct governance rule, Work, any independently constructed C.20 discipline, and the A.19.CPM/G.0 comparison declaration. The compound label creates none of those objects or facts. |
| "The five card positions are filled, so the discipline exists." | Recover the exact candidate, direct part occurrences, whole-forming claims, assembly, reidentification, characteristic, and larger-assembly compatibility. |
| "The department is the discipline." | Keep the organization as an exact system; apply A.15.1 to any claimed Work and establish any discipline part relation independently. |
| "Every canonical paper and standard is a discipline part." | Identify each episteme and apply the C.20 predicate; citation, canonical status, or publication is insufficient. |
| "Every method used in the field is a part." | Identify the Method under A.3.1 and test whether the current assembly makes its contribution constitutive; registry membership and use alone are insufficient. |
| "The Bridge set assembles a transdiscipline." | Keep each Bridge and bounded-use proposition direct; apply a declared breadth criterion or rerun the full construction test for a new candidate. |
| "The selected model-use structure is the discipline context." | Keep the optional A.22 Structure attached only to the named use; it is neither whole nor part by selection. |
| "Three viewpoints make the field multidisciplinary." | State a project-local breadth predicate over exact disciplines and contributions; viewpoint or structure count proves nothing. |
| "The journal, card, or dashboard carries the discipline." | Separate discipline, description episteme, publication occurrence, form, carrier, and health reading. |
| "A maturity drop created a new discipline edition." | Keep the C.21 result separate and apply the C.20 reidentification rule to actual construction changes. |
| "A later canon edition is the later discipline." | Apply C.2.1 to the canon and C.20 to the field; historical continuation and discipline continuity are separate claims. |

### C.20:8 - Consequences

**Benefits.** Discipline claims become auditable without freezing one universal canon, institution, bridge set, or method repertoire. Rival traditions can remain explicit and federate only through admissible directed uses rather than false consensus; constituent replacement and genuine reidentification can be distinguished. Field comparison and dispatch can consume the exact construction without becoming its cause. A selector can additionally consume exact discipline-relevant Characteristic and evidence or assurance claims, while an admitted publisher System can perform publication Work that yields a readable didactic presentation without making its title, card, column, or registry ontological. Any stewardship, responsibility, authority, ownership, or assignment is stated separately when it independently obtains.

**Costs and trade-offs.** A positive claim needs exact parts, direct relation intervals, whole-forming claims, an assembly, a reidentification rule, one whole characteristic, and a larger-assembly compatibility account. The cost is proportional: ordinary use can stop at readable sentences. A named comparison adds Scale, comparator, and CG-Spec literacy; a cross-locality use that relies on an obtaining semantic Bridge adds its separate bounded-use claim and reliance work; trace, evidence, publication, health, selector, or assurance apparatus is added only for a named receiver. That extra explicitness pays back in safer reuse and clearer governance.

**Risks avoided.** The pattern blocks label-made fields, institution-made identity, publication-made parts, context-count breadth, bridge-made merger, health-score ontology, and registry-made method or discipline membership.

### C.20:9 - Rationale

A discipline is durable because a governed practice-and-knowledge assembly can continue through permitted replacement, not because all surrounding artifacts remain fixed. Direct part relations establish which exact entities are constitutive during which intervals. Whole-forming claims explain their contributions and coupling. The assembly and reidentification rule then distinguish continuity from a different field, while the composition-grounded characteristic shows why the candidate is a whole rather than a collection.

Keeping organizations, Work, methods, epistemes, structures, Bridges, comparisons, publications, evidence, and health readings separate does not make them unimportant. It lets each object affect the discipline claim through its actual relation without being promoted to an automatic part or identity discriminator.

This separation keeps every discipline-related claim local to an exact EntityOfConcern and effective ReferenceScheme, comparison admissible only under its current Scale and comparator declarations, and ordinary evidence-bearing reliance explicit under A.10 and any actual named assurance claim explicit under B.3. It also lets plural traditions, obtaining directed Bridges with use-specific tolerated loss and any material observed loss kept visible, typed health readings, and TA/VA/LA evidence lanes remain inspectable together. Scale compliance, B.3's requirement for an applicable domain model and stated assumptions, and Bridge hygiene stay with their subject patterns: C.20 adopts their constraints for a named use but defines no universal field score or reliability fold. Charisma, prestige, institutional reach, or an attractive field name cannot create a discipline that fails to return to exact construction, Characteristics, and source evidence.

### C.20:9.1 - SoTA-Echoing

| Current source or practice line | C.20 adoption | Boundary of non-overread |
| --- | --- | --- |
| Constructional-ontology work cited in A.1 and C.13 requires explicit constituents, constructive relations, assembly, dependence, and identity choices rather than an extensional list. | Require exact part occurrences, whole-forming claims, an assembly-sensitive reidentification rule, and one composition-grounded whole characteristic. | A graph, card, constructor expression, shared label, or input set creates neither whole nor relation. |
| Current science-of-science and reproducibility practice cited in C.21 treats field health as several typed, scoped, time-qualified characteristics. | Let C.21 evaluate exact disciplines without importing health coordinates into construction. | Reproducibility, standardization, disruption, diversity, or evidence granularity is not discipline identity or truth by itself. |
| Current model, workflow, and publication practice separates semantic ways of doing, claim-bearing descriptions, actual work, results, and publication availability. | Keep Methods, epistemes, Work, results, and publication occurrences independently governed even when their exact relations support a field assembly claim. | Use, representation, occurrence, evidence, or publication does not make an entity a discipline part. |
| Plural-field and translation practice needs explicit local meanings, direction, substitution conditions, an explicit use-specific loss tolerance, and any material observed loss. | Use an exact F.9 Bridge only after two exact F.17 `SchemeSenseCell` values resolve and its predicate obtains; when a named use relies on it, add the separate bounded-use proposition and direct reliance or comparison branch. A plane-only crossing uses the applicable ReferencePlane relation and policy instead. | A Bridge count or high congruence neither merges disciplines nor creates a transdisciplinary kind. |

**Currentness and reopen.** Reopen only the affected construction, identity, crossing, or health decision when its direct source interface changes. A newer discipline study can change the local breadth criterion or worked case without weakening the exact-part, direct-relation, assembly, and reidentification boundary.

### C.20:10 - Relations

**Builds on.** A.1 for constructive holon recognition; A.6.REL for relation-occurrence discipline; A.14 and direct part patterns for mereological meaning; C.13 for an optional construction trace; A.17 and A.18 for the composition-grounded Characteristic and Scale, with C.16 only for an actual measurement chain; E.24.UK for public-kind admission.

**Coordinates with.** C.2.1 for canon, standard, classification, description, trace, and result epistemes; A.3.1 and B.1.5 for Methods and method composition; A.15.1 for dated discipline work; A.22 for optional selected structures; B.2 for a separately current whole-reidentification question; C.3 for project-local breadth and tradition classifications; C.22 for selector-facing problem typing and TaskSignature assignment; C.23 for MethodFamily evidence and maturity; E.10 for lexical precision; and F.17/F.18 for local-sense term publication and durable naming.

**Conditional branches.** F.9 for exact Bridges; A.10 for ordinary evidence-bearing reliance and B.3 only for an actual named assurance claim; C.21 for discipline health; A.19.CPM for comparison and G.0 for its CG-Spec admissibility declaration; G.4 for acceptance thresholds; E.24.PUB for publication; G.5 for selector use of independently grounded discipline or method claims.

**G.2 source-pack boundary.** When one current G.2 harvest or synthesis informs a discipline account, preserve the anti-monoculture intent by keeping plausible rival lineages and the semantic localities relevant to that named synthesis visible, with an explicit coverage or omission rationale and explicit crossings where needed. C.20 sets no minimum number of Traditions, local frames, cards, contexts, or matrix rows; G.2 alone governs conformance of its pack. A plural or conforming pack, `TraditionPalette`, `BridgeMatrix`, or historical `Gamma_disc` expression still constructs no discipline and supplies no part relation.

**Constrains.** A C.13 discipline trace consumes C.20 facts and creates none. C.21 evaluates an already identified discipline. G.5 may consume an independently identified Method together with exact discipline-relevant construction or classification, Characteristic, and evidence or assurance claims only through its own declared predicate. An ungrounded discipline name supplies none of field belonging, comparison value, evidence strength, selection, or truth. A registry or family row, selector request, policy, result or shortlist, CG-Spec reference, and EvidenceGraph row can make an actual G.5 use auditable; none lets G.5 infer Method membership, discipline parthood, actual selector application or selection, or claim truth. A selected structure, Bridge, comparison, publication, evidence graph, health reading, or label never supplies a missing C.20 part occurrence.

### C.20:End

