## E.24.UK - U-kind Governance and Ontic Settlement Coupling

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.UK:0 - Use This When

Use this pattern when an FPF text, heading, title, filename, ToC row, table, or source passage uses a `U.*`, type, kind, or subkind spelling and the author must decide whether it names a durable U-kind, a dependent durable value under an existing ontic settlement, a C.3 `U.Kind`, a Concept-Set or naming object, a slot position, a relation structure, a record, a publication form, a lens, a local frame, or wording that must stay outside current FPF vocabulary.

Typical moments:

- a proposed `U.*` name appears in a pattern title, host filename, monolith heading, or ToC row;
- a current pattern uses type, kind, or subkind wording and the governed value is unclear;
- a structural name looks useful for search, but may advertise a false root kind;
- a slot name, relation position, record field, diagram node, table column, graph expression, or publication form has acquired a `U.*` spelling;
- a single E.24 ontic settlement appears to govern one root value plus several dependent durable values.

**Primary EntityOfConcern.** The EntityOfConcern is the U-kind admission relation for one candidate `U.*`, type, kind, or subkind name. The pattern governs whether the candidate is retained as a durable U-kind, retained as a dependent durable value under a root settlement, governed by C.3 typed-reasoning law, or treated as a non-U object governed elsewhere.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether a public FPF name should remain `U.*`. The downstream reader is the practitioner who uses public pattern titles, headings, ToC rows, and names as orientation cues and needs those cues to point to the real governed object.

**First useful move.** Recover the current governed object and the current use before judging the spelling. Then ask which existing FPF law governs the value: E.24 ontic settlement, C.3 typed reasoning, A.8 universal-core admission, A.11 parsimony, F.8 mint-or-reuse, F.5 naming, a direct subject pattern, or E.10 precision restoration.

**What goes wrong if missed.** FPF grows a shadow ontology by punctuation. A slot label becomes a kind, a publication form becomes an ontic, type and kind wording becomes active beside ontic law, and a useful title survives because it is searchable rather than because it names the governed object.

**What this buys.** Public `U.*` names become trustworthy. Root U-kinds, dependent durable values, C.3 `U.Kind` values, Concept-Set rows, slot names, relation structures, records, publication forms, lenses, local frames, and source wording outside current FPF use are separated before naming.

**Not this pattern when.**

- If the question is whether FPF needs a durable ontic at all, use `E.24`.
- If the question is only detecting an ontic candidate before the durable decision, use `E.24.CD`.
- If the question is the difference among an ontic, its description episteme, publication, and publication form, use `E.24.PUB`.
- If the question is one phrase-level precision issue with no durable name pressure, use `E.10`, `E.10.ARCH`, or the direct precision-restoration pattern.
- If the current value is already recovered and only its public label must be chosen, use `F.8`, `F.5`, `F.18`, or `F.17` according to the naming use.

### E.24.UK:1 - Problem Frame

FPF uses `U.*` names for durable universal values and nearby governed values. Recent ontic work made that spelling more visible in titles, filenames, ToC rows, slot relations, source rows, and headings. The spelling is useful, but it is not ontology.

The same token shape can name different kinds of things:

- a root durable value such as `U.Episteme`, `U.Method`, `U.Work`, or `U.Transformation`;
- a dependent durable value such as `U.MethodDescription`, `U.WorkPlan`, `U.RoleAssignment`, `U.View`, or `U.EpistemePublication`;
- C.3 `U.Kind` or `U.SubkindOf` typed-reasoning values;
- type, kind, or subkind wording whose governed value must be recovered before current FPF use;
- a slot position, relation structure, selected structure, record form, publication form, math lens, representation lens, local frame, or source expression.

E.24.UK governs that separation. It is an E.24 subpattern because U-kind admission depends on ontic settlement, but it is not the head E.24 pattern. E.24 remains the head pattern for `U.Ontic` and ontic introduction. E.24.UK owns the detailed U-kind law.

### E.24.UK:2 - Problem

Without this pattern:

1. **`U.*` spelling substitutes for admission.** A public name is retained because it looks like a kind.
2. **Unsettled type and kind wording competes with U-kind admission law.** Type, kind, subkind, Concept-Set rows, U-kind names, and E.24 ontics become overlapping ontologies.
3. **Dependent values become root values.** A value whose identity is held by a root settlement gets treated as a new root kind.
4. **Structural names over-admit.** Titles, filenames, headings, and ToC rows advertise kindhood more strongly than the pattern body establishes.
5. **Slot names and lenses become objects.** Relation positions, graph expressions, tuple views, table columns, and publication forms receive `U.*` names.
6. **Naming patterns are asked to do ontology.** F.5, F.8, F.18, or F.17 is used before the governed value has been recovered.

### E.24.UK:3 - Forces

| Force | Tension |
| --- | --- |
| Public mnemonic value vs ontology truth | A `U.*` name can improve discovery; it can also advertise a false governed object. |
| Root stability vs dependent reuse | Some durable values deserve names but share identity with a root settlement. |
| C.3 typed reasoning vs U-kind governance | `U.Kind` and `U.SubkindOf` are real C.3 values, but not synonyms for every durable `U.*`. |
| Kernel parsimony vs expressive pattern language | FPF needs useful names, but new U-kinds are expensive and must not replace slots and relations. |
| Host and ToC structure vs prose nuance | A false `U.*` in a title, filename, heading, or ToC row is stronger than a false prose occurrence. |

### E.24.UK:4 - Solution

Treat U-kind governance as a coupled but non-counting relation between durable `U.*` names and E.24-compatible ontic settlement.

Every durable `U.*` name needs one primary E.24-compatible settlement. That settlement may be:

- a root ontic settlement for the governed subject value;
- a dependent durable value under a root settlement;
- explicit reuse of an existing root subject U-kind;
- a C.3 typed-reasoning value when the current question is kind quantification, membership, subkind order, or kind bridge.

Every durable reusable ontic needs a named root subject U-kind or explicit reuse of one. This does not mean one full ontic pattern per U-kind, and it does not mean one U-kind per ontic. `U.Ontic` names the ontology-unit kind; it does not replace the subject kind governed by that ontology unit.

Use this compact decision relation:

```text
UKindAdmissionDecision:
  CandidateSpelling:
  SourceLocationKind: prose | table | heading | title | filename | ToC row | source quote
  RecoveredGovernedObject:
  CurrentUse:
  IdentityGroundingOrRecognitionRule:
  C3KindUse:
  E24Settlement:
  RootSubjectUKind:
  DependentValueIfAny:
  NonUDispositionIfRejected:
  NamingPatternIfRetained:
  StructuralDispositionIfRejected:
  ReopenCondition:
```

#### E.24.UK:4.1 - Positive Test For A Durable U-kind

Retain or introduce a candidate `U.*` name as a durable U-kind only if all of these are true:

1. It names a governed EntityOfConcern, not merely a source expression, local field, table column, reference suffix, publication form, or math-lens expression.
2. The value has stable identity across at least two uses or one load-bearing governing pattern.
3. The admission cites an identity, grounding, or recognition rule: direct governing pattern, C.3 membership and extent rule, Concept-Set witness set, A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, CT2R/Compose-CAL constructive grounding for structural claims, formal-substrate or principle-frame declaration when current, or another accepted operational identity test.
4. FPF users need to make action-facing claims about that value, not only about a wording choice.
5. Existing root U-kinds plus slot and relation combinatorics cannot express the claim without losing reviewable distinctions.
6. The candidate has a primary governing pattern or a selected governing pattern in the same landing set.
7. The candidate has an E.24-compatible settlement: root subject, SlotRelation when needed, semanticArea, ontologicalNeighborhood, admissible use, non-use boundary, and dependent-value policy.
8. Dependent patterns rely on this value by value or are expected to rely on it after the selected amendments.
9. F.18 and F.17 can name and publish the term without turning a local slot label into a kernel kind.
10. Source wording outside current FPF use is repaired by E.10, E.10.ARCH, or the governing pattern named by value.

If any row fails, the candidate is not admitted as a durable U-kind in the current form.

#### E.24.UK:4.2 - Root And Dependent U-kinds

A root U-kind is the subject value whose identity is held by the primary settlement.

A dependent durable U-kind is a reusable governed value whose identity is kept by the same primary settlement as a root U-kind, while the head pattern states the exact dependence relation and the governing pattern for the dependent value. It is not automatically:

- a C.3 subkind;
- a slot name;
- a record form;
- a publication form;
- a synonym for the root;
- a title convenience.

Examples:

| Candidate | Disposition |
| --- | --- |
| `U.Episteme` | root U-kind governed by the episteme ontic settlement. |
| `U.EpistemePublication` | dependent durable value only when the episteme/publication settlement states the dependence relation. |
| `U.View` and `U.Viewpoint` | dependent or directly governed values under episteme and multi-view settlement, not automatic roots. |
| `U.Method` | root U-kind for semantic way-of-doing when governed by the method pattern. |
| `U.MethodDescription` | dependent value: description episteme for a method, not a C.3 subkind by default. |
| `U.Work` | root U-kind for dated performed occurrence. |
| `U.WorkPlan` | dependent value under method, work, role, and time settlement; it does not show that work occurred. |
| `U.Role` | root work-facing role value under role patterns. |
| `U.RoleAssignment` | dependent typed assignment relation value under role, holder, bounded-context, and work settlement. |
| `RoleRelationStructure` | non-U selected relation structure unless E.24.UK evidence admits durable U-kindhood. |
| `MethodRelationStructure` | non-U selected relation structure unless direct method-composition law admits durable U-kindhood. |

#### E.24.UK:4.3 - Combined Admission Order

Use existing law in this order:

1. Recover the source use and governed EntityOfConcern.
2. If the current question is typed claim quantification, apply C.3 and C.3.1 first. `U.Kind` is the context-local intensional value; `U.SubkindOf` is a partial-order relation over those values.
3. Recover the identity, grounding, or recognition rule for the candidate: direct governing pattern, C.3 membership and extent rule, Concept-Set witnesses, A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, CT2R/Compose-CAL constructive grounding when the claim is structural, formal-substrate/principle-frame declaration, or another accepted operational identity test.
4. If durable FPF kindhood is claimed, apply E.24-compatible settlement, A.11 parsimony, and A.8 universal-core testing when kernel-level status is claimed.
5. If the object is a slot, relation position, record, form, lens, local frame, expression, or source wording, do not admit a U-kind; apply the direct governing pattern for that object or claim.
6. Only after the recovered value and admission decision are stable, use F.8 for mint-or-reuse and F.5, F.18, or F.17 for naming and publication.

| Source | Contribution |
| --- | --- |
| C.3 | Typed claim quantification, intent, extent, membership, kind bridge, and typed guards. |
| C.3.1 | `U.SubkindOf` partial order over `U.Kind`, not dependent-U-kind relation. |
| E.14, B.3.5, and C.13 | Working-Model first, CT2R alias-plus-grounding, and Compose-CAL `Γ_m` traces for structural identity claims. |
| A.6.0 and A.6.1 | Construction-facing declaration shape: `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, vocabulary, laws, applicability, realization, and argument-slot discipline. |
| A.8 | Universal-core test for kernel-level U-kind claims. |
| A.11 | Composition and parsimony before adding a new core concept. |
| E.24 | Ontic settlement and distinction among ontic, description episteme, publication, and form. |
| F.8 | Mint-or-reuse decision after recovered kind and use. |
| F.5 | Naming after recovered meaning; naming does not do ontology. |

#### E.24.UK:4.4 - Source Ontology Conversion Guide

Use this short conversion guide when a source ontology, schema, standard, class hierarchy, or top-level ontology uses words such as type, class, category, object type, entity type, kind, or subtype. BFO-style, ISO-style, OWL/RDF, database-schema, programming-language, and discipline-local type systems are source ontologies or representation regimes; they do not become FPF `U.*` names by translation.

First recover the source construct by value:

- source name and source ontology or schema;
- source identity rule, membership rule, extent rule, or recognition rule;
- source relations such as is-a, part-of, realizes, participates-in, depends-on, or equivalent local relations;
- intended source use: classification, query, modeling, exchange, validation, reasoning, implementation, or documentation.

Then select the FPF object:

| Source construct use | FPF recovery |
| --- | --- |
| claim quantification, membership, extent, subkind, or kind bridge | C.3 `U.Kind`, C.3.1 `U.SubkindOf`, and typed-reasoning law |
| public durable FPF kind needed across patterns | E.24.UK durable U-kind admission, then E.24-compatible settlement |
| a reusable cluster of slots, fillers, and governing relations | E.24 ontic settlement with one root subject U-kind or explicit reuse of an existing root |
| imported formal symbol or declared range in a signature or mechanism | A.6 `SubjectBlock` with `RangedValueKind`, imported signature symbol, Concept-Set row, or admitted durable U-kind |
| source-name alignment across contexts | F.9 bridge, F.17 term row, F.18 naming, and explicit loss notes |
| implementation or serialization category | representation, publication form, record field, schema field, or direct implementation artifact governed by the relevant pattern |

A source "type" may become an FPF kind and may require an ontic, but only after these tests. If the source construct only supplies local classification or exchange syntax, keep it as C.3 typed reasoning, bridge material, representation material, or source wording. Do not create a rival FPF type layer beside durable U-kind governance and E.24 ontic settlement.

#### E.24.UK:4.5 - Structural Location Rule

A `U.*` spelling in a pattern title, host filename, monolith heading, or ToC row is stronger than a prose occurrence. Structural locations orient readers to the governed object.

Use this rule:

- **Prose occurrence:** recover the local claim and direct governing pattern.
- **Table row or record field:** ask whether the field is a slot, record field, publication-form element, or governed value.
- **Heading:** retain `U.*` only when the section really governs that value or directly references an already governed value.
- **Pattern title or host filename:** retain `U.*` only when the pattern's primary EntityOfConcern is that root or dependent U-kind.
- **ToC row:** retain `U.*` only when the row points to a pattern that carries the settlement; otherwise name the direct governed object or repair the wording with E.10.

Do not keep a false `U.*` structural name for memory or search convenience. Use a Plain label, local heading, Name Card, Concept-Set row, relation name, record field, or quoted source wording when that is the actual object.

#### E.24.UK:4.6 - Non-U Dispositions

If the positive test fails, select the actual governed object:

| Candidate pressure | Disposition |
| --- | --- |
| slot or relation position | SlotKind, ValueKind, RefKind, direct relation, or local field under A.6.5 and direct pattern. |
| selected relation structure | non-U selected structure or direct relation structure. |
| record or card shape | record form or publication form under the direct publication pattern. |
| graph, tuple, algebra, metric, view, or formal expression | math lens, representation lens, or direct modeled object. |
| source label or source tradition word | source wording, local sense, or reduced-use quote under E.10 and E.10.ARCH. |
| public naming pressure | F.8 decision, then F.5, F.18, or F.17 only after recovered value is stable. |

### E.24.UK:5 - Archetypal Grounding

#### E.24.UK:5.1 - False Structural U-kind Title

A structural title that names an action-invitation precision-restoration move as `U.ActionInvitationPrecisionRestoration` looks like it names a durable U-kind. E.24.UK asks for the governed object. If the pattern governs a precision-restoration move for action-invitation wording, the `U.*` spelling misnames the public object. Rename the title to the actual pattern object unless the pattern writes E.24.UK evidence that a durable U-kind exists.

#### E.24.UK:5.2 - Retained Root U-kind

`U.Work` can remain a root U-kind because the direct work pattern governs a dated performed occurrence with identity, use boundary, relations to role assignment and method, and action-facing claims. A heading or title may reference `U.Work` only when that governed value is current.

#### E.24.UK:5.3 - Dependent Durable Value

`U.WorkPlan` is not performed work. It may remain a dependent durable value when the work-plan pattern states dependence on method, role, time, and intended work relations. The dependence relation is not `U.SubkindOf` unless C.3 typed-reasoning law explicitly says so.

#### E.24.UK:5.4 - Type And Kind Governance Passage

A passage that says a proposed type must pass A.8 or A.11 is a kernel-level U-kind admission question. A passage that says `U.Kind` and `U.SubkindOf` are used for typed reasoning remains C.3 law. A naming passage in F.5 or F.8 waits until the recovered value and admission decision are stable.

#### E.24.UK:5.5 - Lower-level Heading

A C.2.1 heading such as `U.ClaimGraph` or `U.Viewpoint` does not admit kindhood by heading shape. The heading must be read through the episteme slot relation: retain as dependent value or slot component only if C.2.1 states the settlement; otherwise rename the heading to the actual slot, relation, or publication object.

### E.24.UK:5.6 - Bias-Annotation

This pattern blocks punctuation-bias and taxonomy-bias. A `U.*` spelling, title, filename, table row, or imported type word is not enough to create a durable FPF kind. First recover the governed object, its current use, the owning ontic or typed-reasoning law, and the slot or relation position. Only then decide whether the public name should be a root U-kind, dependent durable value, C.3 `U.Kind`, Concept-Set row, slot name, relation structure, record, publication form, lens, or local frame.

### E.24.UK:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24UK-1` | The candidate's governed object is recovered before the `U.*` spelling is judged. |
| `CC-E24UK-2` | C.3 `U.Kind` and `U.SubkindOf` are not used as synonyms for all U-kind governance. |
| `CC-E24UK-3` | A root U-kind has a primary E.24-compatible settlement and an identity, grounding, or recognition rule rather than a taxonomic label alone. |
| `CC-E24UK-4` | A dependent durable U-kind states the root settlement and dependence relation. |
| `CC-E24UK-5` | Structural locations retain `U.*` only with settlement evidence or direct reference to an already governed value. |
| `CC-E24UK-6` | Non-U objects are classified as slot, relation, record, form, lens, local frame, expression, or source wording outside current FPF use, with the direct governing pattern named where the claim remains current. |
| `CC-E24UK-7` | F.8, F.5, F.18, and F.17 are used only after the recovered value and admission decision are stable. |
| `CC-E24UK-8` | E.24 remains the head ontic pattern; this pattern owns detailed U-kind law and does not duplicate it back into E.24. |

### E.24.UK:6.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| **U-dot by punctuation.** A heading or filename contains `U.` and therefore survives as a kind. | Public spelling outruns admission. | Apply the durable U-kind test; otherwise rename to the governed object. |
| **Slot becomes kind.** `EvidenceRole`, `MethodRole`, or `DescriptionRole` is admitted because a value fills a relation position. | Slot-position label becomes a false ontology branch. | Keep SlotKind, ValueKind, RefKind, and governing pattern separate. |
| **Source type import.** A BFO, ISO, OWL, database, or programming-language type is copied as an FPF U-kind. | Source ontology and FPF ontic law become mixed. | Use the source conversion guide and name the FPF governed object. |
| **Searchable title wins.** A memorable heading remains public even though the body governs a record, publication form, relation structure, or local frame. | Discoverability replaces ontology. | Keep the searchable phrase in entry or retrieval material if useful, and put the governed object in the public pattern name. |
| **Dependent value promoted.** A value that depends on an existing ontic settlement is admitted as an independent root U-kind. | FPF grows duplicate roots for one ontological neighborhood. | Keep the root settlement and state the dependent durable value relation explicitly. |

### E.24.UK:8 - Consequences

Positive consequences:

- public `U.*` names become reliable orientation signals;
- dependent values can be named without pretending to be roots;
- type and kind wording is governed by C.3, E.24.UK, A.8, A.11, F.8, and F.5 rather than preserved as overlapping ontology;
- structural names are settled before they become misleading public names.

Costs:

- pattern authors must read the governed object before keeping a convenient `U.*` spelling;
- some familiar host filenames, headings, and ToC rows must be renamed;
- structural inventory work becomes part of U-kind governance, not an afterthought.

### E.24.UK:5.7 - Rationale

FPF needs U-kind names to stay rare and load-bearing because they orient many patterns at once. Without a separate U-kind governance rule, ordinary type words, source-ontology classes, slot labels, filenames, and memorable headings create a second ontology beside E.24 ontic settlement and C.3 typed reasoning.

The coupling rule keeps the architecture compact: a durable U-kind needs an E.24-compatible settlement or an explicit C.3 typed-reasoning status; dependent durable values remain dependent on their root settlement; non-U objects keep their ordinary governing patterns. This lets FPF reuse source ontologies and discipline vocabularies without importing their taxonomy as FPF U-kinds.

### E.24.UK:5.8 - SoTA-Echoing

| Source line | Use in this pattern | Practical implication |
| --- | --- | --- |
| Foundational and applied ontology distinguish classes, individuals, relations, roles, qualities, functions, and representation forms. | Adapt: FPF does not copy one source taxonomy as U-kind law; it recovers the governed object and its admission basis. | A source `type`, `class`, or `category` becomes an FPF U-kind only after FPF admission, not by translation. |
| Modular ontology and ontology-design-pattern practice use reusable fragments rather than one flat taxonomy. | Adopt for E.24 coupling: public durable names are backed by ontic settlement and neighboring-pattern obligations. | A durable U-kind must be usable across patterns without forcing a new taxonomy branch for every slot position. |
| Naming and controlled-vocabulary practice separate labels from the objects they label. | Adopt through F.5, F.8, F.17, and F.18 after the governed value is recovered. | A good title can remain searchable while the body names the actual governed object and avoids false U-kind admission. |

### E.24.UK:7 - Relations

- **Specializes:** `E.24` for durable U-kind admission and structural-name U-kind settlement.
- **Coordinates with:** `E.24.CD` for candidate detection, `E.24.PUB` for publication and structural-name pressure, `C.3` and `C.3.1` for typed reasoning, `A.8` and `A.11` for kernel admission constraints, `F.8` and `F.5` for naming decisions, `E.10` and `E.10.ARCH` for source wording outside current FPF use.
- **Does not replace:** direct subject patterns for method, work, role, episteme, transformation, relation, characteristic, view, measurement, publication, evidence, gate, source, or decision claims.

### E.24.UK:End

