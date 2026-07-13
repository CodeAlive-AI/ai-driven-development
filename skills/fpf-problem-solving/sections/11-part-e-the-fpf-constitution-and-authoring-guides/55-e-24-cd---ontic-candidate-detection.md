## E.24.CD - Ontic Candidate Detection

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24.CD:0 - Use This When

Use this pattern when a recurring FPF construct is an ontic candidate, but the current source material is still a tangle of names, fields, cards, records, tables, schemas, diagrams, views, examples, or nearby pattern fragments.

Typical moments:

- one word such as "process", "source", "quality", "architecture", "problem", "view", "role", "function", "mechanism", or "method" keeps pointing to several FPF values at once;
- several patterns repeat a similar slot list, field list, boundary formula, or generic semio warning;
- a project data structure looks concept-shaped, but it may only be a publication form or local record;
- a draft ToC row or older source label names a family that no current pattern yet governs;
- a proposed new `U.*` kind feels useful, but it might duplicate existing governing patterns.

**First useful move.** Recover the recognizable project concern first, then list the typed FPF values and relation positions that the source material compresses. Only then classify the case as durable ontic candidate, local use frame, direct governing-pattern use, publication-form-only case, or source wording to keep quote-only or reduced-use.

**What goes wrong if missed.** FPF grows a hidden ontology. A table becomes a kind, a card becomes a subject, a draft label becomes authority, and a convenient word creates a second ontology over values that already have governing patterns.

**What this buys.** The author gets a compact candidate cluster and a sufficiency rationale before opening `E.24`. This keeps E.24 small and keeps candidate discovery from becoming a registry, score form, or warning catalogue.

**Not this pattern when.**

- If the durable ontic is already selected and its identity and slot relation must be governed, use `E.24`.
- If the current question is whether a `U.*` spelling in a heading, title, filename, ToC row, table, or source passage should be retained, demoted, or repaired, recover the concern and use `E.24.UK`.
- If the current problem is only confusion between an ontic, its description, and publication forms, use `E.24.PUB`.
- If an existing subject pattern already governs the claim, use that pattern directly.
- If the issue is one wording-use repair, use `E.10`, `E.10.ARCH`, or the relevant precision-restoration pattern.
- If the contested question is how to compare pattern-set architecture alternatives, construct the evaluation `CharacteristicSpace` through `A.19.ECS`.

### E.24.CD:1 - Problem Frame

`E.24` introduces or rejects a durable `U.Ontic`. Before that decision, FPF often needs a smaller move: detect whether an apparent subject is actually a candidate ontic or merely a record, local frame, source label, draft locus, or direct use of existing patterns.

Ontic candidates are easy to overread because they appear through publications. A form, card, schema, table, field list, diagram, source row, review packet, or data model can carry a real subject matter, but it is not automatically the subject matter. Detection must therefore start from the `EntityOfConcern` and the typed values involved, not from the publication form that made the subject visible.

E.24.CD governs that detection move. It prepares an E.24 decision; it does not make the durable ontic decision by itself.

### E.24.CD:2 - Problem

Without ontic-candidate detection:

1. **Publication forms become false objects.** A card, table, or schema receives ontology authority because it is the visible publication form.
2. **Local use frames harden silently.** A useful table for one bounded use starts being cited as if it were a reusable FPF kind.
3. **Direct governing patterns are bypassed.** Existing `U.Method`, `U.Work`, `U.Mechanism`, `U.Episteme`, `U.Structure`, `U.CharacteristicSpace`, source, gate, evidence, or publication patterns are duplicated under a new head.
4. **Candidate selection becomes vocabulary repair.** The author replaces a broad word with a new broad word while the slot relation remains hidden.
5. **Candidate selection becomes scoring ritual.** The author builds a score table before the candidate's identity, slots, and neighboring governing patterns are clear.

### E.24.CD:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition vs premature kind creation | A recurring concern must be noticed early, but early recognition must not mint a `U.*` kind by momentum. |
| Publication visibility vs subject ontology | The visible publication form may reveal the concern, but the ontic candidate is the governed object, not that form. |
| Direct reuse vs hidden duplication | Existing governing patterns should carry their values; a new ontic is justified only when their relation must itself be governed. |
| First-use affordability vs full architecture analysis | The author needs a quick first move; contested alternatives can use `A.19.ECS` in a separate evaluation frame without making every candidate pass a scoring ritual. |
| Semantic cohesion vs registry growth | Several examples can reveal one semantic area; a list of examples is not a registry of ontics. |

### E.24.CD:4 - Solution

Use an `OnticCandidateCluster` as a local detection aid. It is not a `U.*` kind, not a permanent registry entry, and not the ontic. It is a compact description of why the author is considering an E.24 decision.

```text
OnticCandidateCluster:
  RecognizableConcern:
  VisibleSourceForms:
  CompressedTypedValues:
  CandidateSemanticArea:
  CandidateOntologicalNeighborhood:
  PossibleSlotRelation:
  ExistingGoverningPatterns:
  HiddenFormClassification:
  UKindPressure:
  FirstUseGain:
  NonUseDisposition:
  NextPattern:
```

Read the rows this way:

- `RecognizableConcern` names what users or authors are trying to think or act with, before choosing a new kind.
- `VisibleSourceForms` names the forms that revealed the concern: cards, records, tables, schemas, diagrams, views, source rows, examples, or project data structures.
- `CompressedTypedValues` lists the separate FPF values being compressed, such as method, method description, mechanism, work plan, work occurrence, evidence, gate, source, publication, characteristic, structure, role assignment, bounded context, or transformation value.
- `CandidateSemanticArea` names the meaning area where the concern is recognizable.
- `CandidateOntologicalNeighborhood` names the current FPF patterns that already govern nearby values.
- `PossibleSlotRelation` sketches the candidate relation only enough to decide whether E.24 should open.
- `ExistingGoverningPatterns` lists direct patterns that may already close the case.
- `HiddenFormClassification` selects one of the dispositions below.
- `UKindPressure` names any `U.*`, type, kind, subkind, title, filename, heading, ToC row, or structural name whose public shape could over-admit durable FPF kindhood.
- `FirstUseGain` says what becomes easier, safer, or more action-facing if the candidate becomes an ontic.
- `NonUseDisposition` blocks the main overread if no durable ontic is selected.
- `NextPattern` names the next governing pattern: usually `E.24`, `E.24.UK`, `E.24.PUB`, `A.19.ECS`, a direct subject pattern, or `E.10.ARCH`.

#### E.24.CD:4.1 - Detection Signals

Open E.24.CD when several signals cohere around one recognizable concern and a possible slot relation that current patterns do not already make easy to use. The judgement is expert sufficiency, not a score gate: a repeated word alone is a wording-use trigger, and a useful form alone is a publication form or local use frame. Two or more signals can serve as a quick suspicion threshold only when they support the same concern, preserve the typed values involved, and make the possible slot relation worth inspecting.

Useful signals include:

1. **Stable concern across forms.** Several source forms point to the same recognizable concern even when the publication form changes.
2. **Typed-value spread.** The concern repeatedly involves several governed values whose relation matters for use.
3. **Copied slot doctrine.** Several patterns repeat the same field list, slot list, boundary warning, or local relation shape.
4. **Claim-impact from relation changes.** Changing one filler changes what can be claimed, compared, relied on, repaired, or stopped.
5. **Weak identity in current text.** The concern is used as if it has identity, but the identity criterion is missing or inconsistent.
6. **Direct-pattern strain.** Existing governing patterns carry the values, but users still need a stable relation among them.
7. **Publication-form temptation.** A card, record, table, schema, diagram, view, source row, or data structure is treated as the object because it is visible.
8. **U-kind pressure.** A `U.*` spelling, earlier type/kind wording, heading, title, filename, or ToC row appears to claim kindhood before the governed object is recovered.
9. **Dependent-pattern burden.** Nearby patterns need a shared settlement and would otherwise copy the same local ontology.

If the signals do not cohere around one concern, do not open E.24.CD only to collect them. Use the direct governing pattern, `E.10.ARCH`, `E.24.PUB`, or a local-use disposition.

#### E.24.CD:4.2 - Hidden Form Classifications

Classify the detected construct before opening E.24:

| Classification | Meaning | Next use |
| --- | --- | --- |
| Durable ontic candidate | The concern appears to need stable identity, a type-level slot relation, semantic area, ontological neighborhood, and dependent-pattern reliance. | Open `E.24`. |
| U-kind admission pressure | The remaining question is whether a visible `U.*` spelling or earlier type/kind wording should survive in a structural location or public name. | Recover the concern and typed values, then use `E.24.UK`; candidate detection does not admit the U-kind. |
| Local use frame | The relation is useful in one bounded use family, but all filled values are already governed elsewhere and no dependent pattern needs a reusable ontic. | Keep local; cite governing patterns for fillers. |
| Direct governing-pattern use | One existing pattern already carries the claim. | Use that pattern directly. |
| Publication-form-only case | The visible object is a card, record, table, schema, diagram, view, packet, or source form that publishes or organizes another EoC. | Use `E.24.PUB` or the relevant publication pattern. |
| Source wording only | The source label compresses several values but should not enter current FPF vocabulary. | Keep quote-only or reduced-use; use `E.10.ARCH` if repair is needed. |
| Evaluation-construction case | The current problem is comparing pattern-set architecture alternatives. | Build the evaluation `CharacteristicSpace` through `A.19.ECS`. |

#### E.24.CD:4.3 - Sufficiency Rationale

If the classification is durable ontic candidate, write a short sufficiency rationale before opening E.24:

```text
OnticCandidateSufficiencyRationale:
  CandidateEoC:
  StableIdentityHint:
  PossibleSlotRelation:
  ExistingValuesPreserved:
  SemanticArea:
  OntologicalNeighborhood:
  DependentPatternNeed:
  DuplicateOntologyRiskIfSkipped:
  FirstUseGain:
  MainNonUseBoundary:
```

The rationale is sufficient only when it shows both gain and restraint. Gain: the candidate would reduce duplicated ontology, make claims easier to inspect, and give dependent patterns a reusable relation. Restraint: existing typed values keep their governing patterns, publication forms stay downstream, and a local frame remains local when no durable ontic is needed.

#### E.24.CD:4.4 - Project Data-Structure Recovery

Project data structures often hide ontic candidates. Treat them as signals, not conclusions.

When a project data structure or publication form has fields such as `status`, `owner`, `type`, `target`, `source`, `evidence`, `decision`, `problem`, `view`, `flow`, `quality`, or `architecture`, do not accept the field heads as ontology. Recover:

1. the project concern that the form is helping the team handle;
2. the FPF typed values that may fill those fields;
3. the relation among those values;
4. the publication or record form that carries the visible form;
5. the governing patterns that already own each value;
6. the one overread blocked by this recovery.

Example: an "ArchitectureDecisionRecord" may carry an architecture move, selected structure, decision, evidence, source freshness, gate condition, responsible role assignment, and publication date. That record is not a root `U.ArchitectureDecisionRecord` ontic by appearance. It may be a publication form over values governed by `C.30`, decision, gate, evidence, source, role-assignment, and `E.24.PUB` patterns. Only if the relation itself needs stable identity and dependent-pattern reliance does E.24 open.

#### E.24.CD:4.5 - Stop Conditions

Stop E.24.CD when one of these dispositions is reached:

- **Open E.24:** durable ontic candidate is selected for a full ontic-introduction decision.
- **Open E.24.UK:** the concern is recovered and the remaining decision is root or dependent U-kind admission, C.3 typed-reasoning governance, non-U disposition, or structural-name repair.
- **Use existing pattern:** a direct governing pattern carries the claim.
- **Keep local:** a bounded local use frame is enough and is explicitly non-`U.*`.
- **Use publication discipline:** the problem is confusion among the ontic, its description, and publication form.
- **Use evaluation construction:** the problem is comparing architecture alternatives.
- **Keep quote-only or reduced-use:** the source wording should not become current FPF vocabulary.

Do not keep E.24.CD open as a standing registry of possibilities. Once the disposition is clear, move to the selected governing pattern.

### E.24.CD:5 - Archetypal Grounding

#### E.24.CD:5.1 - Episteme Candidate That Becomes a Durable Ontic

Before `C.2.1`, "description", "view", "claim set", and "publication" could be confused. E.24.CD would detect stable concern across forms, typed-value spread, slot doctrine, publication-form temptation, and dependent-pattern need. The sufficiency rationale points to a durable ontic: `U.Episteme`, with EntityOfConcernSlot, claim graph, viewpoint, reference scheme, grounding, and publication-form boundaries.

The next governed use is E.24-style introduction, then the governing pattern `C.2.1`. The cards and publications are not the episteme; they describe or publish it.

#### E.24.CD:5.2 - Problem Card as Stress Case

`ProblemCard@Context` is a useful working form, but the card form alone does not create `U.Problem`. It can carry a project problem statement, affected entity, concern, evidence, constraints, candidate solution direction, owner role assignment, source references, and gate conditions.

E.24.CD asks what is under concern:

- If the current claim is about the card's publication form and use, use the card or publication governing pattern.
- If the claim is about problematization and problem statement adequacy, use the problematization pattern.
- If several patterns need a reusable problem ontology with stable identity and slot relation, open E.24.

The stress case prevents a common overread: a record form named "ProblemCard" does not by itself show that FPF needs a root `U.Problem`.

#### E.24.CD:5.3 - Project Schema With Ontology-Looking Fields

A project may contain a table:

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

The table may be a planning aid, work record, publication form, or schema for project tooling. Its fields reveal possible FPF values, but they do not decide their kinds. E.24.CD recovers the project concern and typed values first. If the relation among method, mechanism, work, evidence, result, source, and transformed entity is governed by existing transformation, method, work, mechanism, evidence, source, and publication patterns, keep the table as a publication or local use frame. If dependent patterns need a reusable relation that existing patterns do not provide, open E.24.

#### E.24.CD:5.4 - Characteristic Space as Candidate

Evaluation work often starts as a score table. The visible table may hide a `U.CharacteristicSpace`: characterized object kind, characteristics, scale bindings, value meanings, coordinate groups, missingness semantics, normalization boundaries, comparability boundaries, and evidence hooks. If the score table is only a local report, use the relevant evaluation pattern. If several patterns rely on that space as a reusable object, the candidate can be selected as `U.CharacteristicSpace` and governed by `A.19`.

The table is not the characteristic space. It can publish one filled evaluation over the space.

### E.24.CD:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Epist**, **Prag**, **Did**.

This pattern intentionally biases toward early recovery of the real object under concern. It resists:

- **publication-form bias:** treating a card, schema, table, or record as the subject matter;
- **wording bias:** treating a repeated word as a kind decision;
- **registry bias:** collecting every possible ontic candidate instead of disposing the current case;
- **scoring bias:** building an evaluation form before identity and slot relation are clear;
- **semio-bias:** discussing descriptions and publications while the ontic candidate and filled values disappear.

The mitigation is concrete: recover the recognizable concern, typed values, current governing patterns, and possible slot relation before naming a candidate or opening E.24.

### E.24.CD:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24CD-1` | The candidate detection names the recognizable concern before naming a new kind, card, record, schema, or publication form. |
| `CC-E24CD-2` | Visible source forms are listed as source forms, not treated as the candidate ontic. |
| `CC-E24CD-3` | Compressed typed values are separated and each is pointed to its current governing pattern when such a pattern exists. |
| `CC-E24CD-4` | Detection records a sufficiency judgement: several signals cohere around one recognizable concern and possible slot relation; repeated wording or one useful form alone is not enough. |
| `CC-E24CD-5` | The hidden-form classification is explicit: durable ontic candidate, U-kind admission pressure, local use frame, direct governing-pattern use, publication-form-only case, source wording only, or evaluation-construction case. |
| `CC-E24CD-6` | Durable ontic candidates carry a sufficiency rationale with identity hint, possible slot relation, semantic area, ontological neighborhood, dependent-pattern need, duplicate-ontology risk, first-use gain, and non-use boundary. |
| `CC-E24CD-6a` | `U.*`, type, kind, subkind, title, filename, heading, and ToC pressure is handled through `E.24.UK` after concern recovery; detection alone does not admit a durable U-kind. |
| `CC-E24CD-7` | Local use frames are explicitly non-`U.*` and do not become registries, evidence records, gate records, methods, mechanisms, work plans, or work occurrences. |
| `CC-E24CD-8` | When publication-form confusion is current, apply `E.24.PUB` rather than solving the confusion by declaring the form to be the ontic. |
| `CC-E24CD-9` | When contested comparison of architecture alternatives is current, apply `A.19.ECS` rather than building the comparison into E.24.CD. |
| `CC-E24CD-10` | The stop condition names one next governing pattern or reduced-use disposition. |

### E.24.CD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Card-to-kind jump | A useful card is promoted into a `U.*` kind because it has repeated fields. | Recover the EoC and typed values; use `E.24.PUB` for publication form. |
| Structural U-kind jump | A heading, title, filename, or ToC row keeps `U.*` because it is convenient for search. | Recover the governed object and use `E.24.UK`; repair the structural name when the primary EoC is not that U-kind. |
| Table ontology by appearance | A table or schema field list is treated as a slot relation. | Ask whether the fields are publication columns, local record fields, or type-level slots with claim-impact. |
| One-word candidate | A broad word is renamed and treated as settled. | Use `E.10.ARCH` and E.24.CD together: recover typed values and slot relation before naming. |
| Registry trap | The author keeps a growing list of possible ontics without disposition. | Stop at one of the E.24.CD classifications and move to the next governing pattern. |
| Scoring before identity | A score form compares alternatives before the candidate EoC and slot relation are clear. | First write the sufficiency rationale; use `A.19.ECS` only when evaluation construction is actually current. |
| Negative-catalogue repair | The text lists neighboring EoCs only as things the candidate is not instead of naming positive values and boundaries. | Name the positive EoC, typed values, and governing patterns; keep the blocked overread to one row. |

### E.24.CD:9 - Consequences

Positive consequences:

- E.24 stays compact because candidate discovery has its own pattern.
- New ontics are selected from recognizable subject matter, not from publication-form appearance.
- Existing governing patterns are reused before a new `U.*` kind is considered.
- Data structures, cards, records, and schemas become useful detection signals without becoming ontology by appearance.

Costs:

- The author must do a short detection pass before opening E.24 for a new durable ontic.
- Some attractive names are lowered to source wording, local frames, or publication forms.
- A contested architecture comparison may require a separate `A.19.ECS` evaluation construction instead of a quick authorial preference.

### E.24.CD:10 - Rationale

FPF needs E.24.CD because ontic candidates are rarely visible as pure ontology. They show up as forms that people use: project tables, cards, schemas, diagrams, source packets, draft pattern rows, examples, and repeated words. Those forms are important because they reveal project concerns, but they are unreliable as ontology decisions.

The pattern therefore uses a small detection cluster rather than a score sheet. A cluster is enough to recover the concern, values, possible relation, and next disposition. A score sheet would make candidate discovery look like a maturity test and invite Goodhart-style optimization of the candidate record instead of ontology settlement.

This also preserves the distinction among EoC, description, and publication. A card can describe an episteme, a table can publish a filled characteristic-space evaluation, and a schema can carry source-side data. None of those forms is automatically the ontic. Conversely, the fact that a concern appears through several forms may be a strong signal that an ontic is needed.

### E.24.CD:11 - SoTA-Echoing

| Source family | Current lesson for E.24.CD | FPF decision |
| --- | --- | --- |
| Shimizu and Hitzler 2024, and Eells, Dave, Hitzler, and Shimizu 2024. | Current modular-ontology and micropattern support: useful ontology units are understandable, extensible, aligned, reusable, and small enough to be assembled. | Detect coherent ontology modules, repeated relation shape, slot-relation density, and dependent-pattern copying; do not treat word frequency, common nouns, or every record field as an ontic decision. |
| Norouzi, Hertling, Waitelonis, and Sack 2025. | Current process-ontology ODP extraction support: process-like and workflow-like forms can hide implicit design patterns that need explicit publication for domain experts. | Inspect process-like, record-like, card-like, and field-list forms for hidden slot relations; do not reopen the transformation-flow settlement and do not import imperative motion metaphors. |
| Nayyeri et al. 2025, and Oyewale and Soru 2026. | Current data-model-to-ontology and enterprise-KG support: schemas, documentation, relations, domain ontologies, extraction, hierarchy structuring, provenance, and validation can expose ontology candidates while also producing overreads. | Treat project databases, tables, schemas, and enterprise data models as ontology-signal sources requiring bounded scope, semantic alignment, slot-relation discipline, expert validation, and a blocked-overread row. |
| CYC microtheory line. | Lineage-only caution: context-bounded knowledge modules are a useful analogy for contradiction locality and scope-bounded ontology fragments. | Do not cite CYC as current decisive support for FPF ontic design and do not import CYC architecture as FPF law. |
| OWL, SKOS, RDF, and triple-store practice. | Infrastructure and expression lineage: these lines carry ontology descriptions, vocabulary links, queries, and serialization forms. | Use them as expression and publication caution only; they do not substitute for `U.Ontic`, do not show that labels are ontology, and do not answer FPF ontic modularization by themselves. |

Smallest source-currentness reopen trigger: reopen this SoTA slice when a newer ontology-engineering or data-model-to-ontology source changes the selected detection criteria for coherent modules, hidden slot relations, bounded scope, validation, or source-form overread; do not reopen it merely because a new vocabulary, serialization, or KG tooling paper appears.

### E.24.CD:12 - Relations

- **Builds on:** `E.24`, `E.24.UK`, `A.6.5`, `C.2.1`, `E.10`, `E.10.ARCH`, `F.18`, `F.19`, and `A.19.ECS`.
- **Coordinates with:** `E.24.PUB` for ontic-description and publication-form boundary, `A.19` for `U.CharacteristicSpace`, `A.19.ECS` for evaluation-characteristic construction, and the governing subject patterns for values recovered in the candidate cluster.
- **Used by:** DRRs and authoring passes that need to decide whether a recurring construct should become a durable ontic, remain a local use frame, use existing governing patterns, or stay as quote-only or reduced-use source wording.

### E.24.CD:End

