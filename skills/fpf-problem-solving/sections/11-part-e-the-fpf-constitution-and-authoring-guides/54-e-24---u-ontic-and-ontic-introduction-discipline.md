## E.24 - U.Ontic and Ontic Introduction Discipline

> **Type:** Part E FPF authoring discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### E.24:0 - Use This When

Use this pattern when FPF work appears to need a durable ontic: a connected ontology-architecture unit whose meaning is spread across several typed values, slots, relation positions, pattern nests, and nearby governing patterns.

Typical moments:

- a repeated local use frame starts behaving like a hidden object;
- a source label or project-side expression keeps pointing to several FPF values at once;
- a draft ToC locus names a calculus or object family, but no current pattern carries its governing meaning;
- a subject pattern begins to carry local slot-relation doctrine that other patterns also need;
- a proposed term would sit across one `semanticArea`, one `ontologicalNeighborhood`, and several dependent patterns.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Ontic` as a durable action-facing ontology unit, together with the current ontic-introduction decision about whether a candidate becomes a durable ontic, remains a local use frame, is handled by direct governing patterns, or stays quote-only or reduced-use source wording.

**Primary working reader.** The first reader is an FPF pattern author or reviewer deciding whether several nearby patterns are describing one ontic, several existing governed values, or only a compressed source label. The downstream reader is the practitioner who needs the resulting subject pattern to say what can be done, claimed, relied on, repaired, compared, or stopped.

**First useful move.** Decide whether the construct is a durable ontic, a direct use of existing governing patterns, a local use frame for one bounded application family, or a source label that must remain quote-only or reduced-use.

**What goes wrong if missed.** FPF grows shadow ontology. The same project concern becomes a method in one place, a mechanism in another, a record in a third, and a local checklist in a fourth. Later uses then repair visible symptoms instead of settling the underlying kind, slot, and governing-pattern question.

**What this buys.** A durable ontic gets an explicit slot relation like `U.EpistemeSlotRelation`, or the construct is explicitly kept as a local use frame with pointers to the typed values and governing patterns that already carry the work.

Main gains:

- it prevents duplicate ontology: one project concern is recovered into typed FPF values and slots instead of becoming a different local object in each nearby pattern;
- it replaces long negative catalogues with positive slot discipline: name the ontic, its slots, and the governing patterns for fillers instead of repeating generic semio warnings across dependent patterns;
- it gives dependent patterns a stable head to rely on without copying the whole slot relation;
- it separates durable ontic introduction from thin relation updates, local use frames, direct governing-pattern use, and quote-only source labels;
- it makes wording follow ontology: after the slot relation and fillers are recovered, local words such as method, mechanism, process, morphism, construction, transformation, work, or change can name the slot or filler they actually refer to.

**Not this pattern when.**

- If one existing governing pattern already carries the claim, use that pattern directly.
- If the issue is only one wording-use repair row, use `E.10` and `E.10.ARCH`.
- If the issue is only a new or revised mechanism meaning, use `E.20`.
- If the issue is only durable naming, use `F.18`.
- If the issue is only a pattern publication-form or section-order matter, use `E.8`.

### E.24:1 - Problem Frame

Some FPF governed objects are small enough to define with one relation or one record. Others require a durable ontic. `U.Episteme` is the central example: it needs identity criteria, typed slots, slot-filling discipline, filled assignments, card and publication species, description boundary, publication-form boundary, relation to `U.Signature`, and dependent episteme-morphism and publication patterns. `C.2.1` works because it makes the small ontic slot relation explicit.

The same failure recurs elsewhere. A project label such as "algorithm", "process", "model", "architecture", "service", "quality", "time", "rhythm", "change", or "source" can point to several typed FPF values. If FPF answers only by choosing a better word, the original compression returns. If FPF creates a new `U.*` kind too early, the new kind becomes a duplicate ontology over values that already have governing patterns.

E.24 governs that ontic-introduction decision.

### E.24:2 - Problem

Without this discipline:

1. **Local use frames become pseudo-kinds.** A repeated local table or record starts to look like a new FPF object even though its rows are only links to existing values.
2. **Draft-only loci become false authorities.** A planned ToC row is cited as if it already supplied current governing text.
3. **Pattern nests are mistaken for semantic units.** The placement label becomes the ontic, while `semanticArea` and `ontologicalNeighborhood` stay unstated.
4. **Slot relations are copied without identity.** Several patterns list similar slots but no pattern says what identifies the ontic, which slots are required, and which dependent patterns may rely on them.
5. **Existing typed values are duplicated.** A new head repeats `U.Method`, `U.Mechanism`, `U.WorkPlan`, `U.Work`, evidence, gate, source, or result relations under a new name.

### E.24:3 - Forces

| Force | Tension |
| --- | --- |
| Ontic stability vs local use | A durable FPF ontic needs identity and slots; a local use frame only needs enough structure for one bounded application family. |
| Reuse vs overgrowth | Dependent patterns need a stable slot relation when they rely on one; premature `U.*` growth creates another ontology. |
| Semantic area vs pattern placement | `semanticArea` names the semantic unit; `ontologicalNeighborhood` names the applicability neighborhood; `pattern nest` is only placement. |
| Draft citeability vs current governance | Draft ToC rows can guide investigation, but current pattern text or an accepted DRR must carry governing meaning. |
| Naming vs ontology | F.18 can make a name better, but naming cannot decide the kind, slot relation, species, and dependent-pattern duties by itself. |

### E.24:4 - Solution

This pattern selects `U.Ontic` as the FPF kind for an ontic. `U.Ontic` is the `EntityOfConcern` of E.24: a connected ontology fragment whose stable identity, slots, admissible slot values, neighboring ontology units, dependent pattern obligations, and non-use boundary must be held together before FPF can use that fragment safely in action-facing patterns.

Keep three objects distinct:

- the `U.Ontic` being introduced or rejected;
- the `OnticIntroductionCandidate`, which is a pattern-set architecture problem: duplicated slots, hidden slot boundaries, hidden relation boundaries, weak identity, scattered invariants, high coupling, low cohesion, or dependent patterns copying the same local ontology;
- the publication that describes the selected ontic, usually one head pattern plus dependent patterns.

The introduction decision is not the publication form. A pattern section, table, source row, or relation list may describe the ontic after the decision, but it is not evidence by itself that the pattern set needs a durable ontic.

Start from the ontic, not from its description or publication. An ontic may then have:

- a description episteme that describes the ontic and its slot relation;
- a publication of that description episteme, often as a head pattern plus dependent patterns;
- publication forms, views, examples, and source rows that help users apply it.

Those are downstream of the EoC distinction. A pattern file, section, table, card, packet, review note, or publication form is not the ontic. It may describe or publish the ontic after the ontic has been selected as the object under concern.

A `U.Ontic` names the connected set of:

- the `semanticArea` being settled: the meaning area that lets users recognize the family of claims or uses under concern;
- the `onticSlotRelation`: the small typed slot relation that gives the ontic its identity, required and optional slots, value kinds, reference kinds, relation set, species or record forms, non-slot components, description boundary, and publication boundary;
- the `ontologicalNeighborhood`: the current FPF patterns that carry claims about the ontic, its slots, its values, its neighboring `EntityOfConcern` uses, and its admissible neighboring uses and boundaries;
- the governing head pattern or accepted local frame that describes the ontic when current FPF use needs a citeable description;
- the dependent-pattern obligations that rely on that settlement without copying the whole slot relation.

FPF ontology is therefore not treated here as one flat class list. It is a connected set of ontics. That prevents ontology explosion: FPF can keep a small number of durable ontology units while allowing many project `EntityOfConcern` values, source labels, project-side identifiers, role assignments, records, methods, mechanisms, work plans, descriptions, publications, and other values to appear as slot fillers inside several ontics. A value filling a slot in one ontic does not thereby become a different entity, a different `U.*` kind, or a second ontology.

The `U.Ontic` decision is selected because the repeated semantic-area, ontic-slot-relation, ontological-neighborhood, and dependent-pattern set is now itself a governed object in FPF. Without a named kind, the same architecture unit would be re-described as a semantic area, pattern nest, ontology family, local frame, slot relation, or description and publication arrangement in different places, recreating the duplicate-ontology problem E.24 is meant to prevent. With `U.Ontic`, DRRs and patterns can cite one kind for the ontology-architecture unit while still keeping each filled value under its own governing pattern.

The cost is kernel growth and metamodel risk. E.24 contains that cost by making `U.Ontic` narrow. A local use frame, source label, project-side expression, recurring table, pattern nest, or draft ToC row is not a `U.Ontic` merely because it looks ontology-shaped. It becomes a `U.Ontic` only when the E.24 decision names stable identity, an ontic slot relation, selected semantic area, selected ontological neighborhood, dependent pattern obligations, existing-pattern reuse, and non-use boundary by value.

U-kind admission is a neighboring E.24-family question, not the main body of E.24. E.24 keeps the minimal invariant:

- a durable ontic is a connected action-facing ontology unit;
- durable `U.*` kindhood requires an E.24-compatible settlement;
- ontic settlement and U-kind count are not one-to-one;
- ontic, ontic-description episteme, publication, and publication form stay distinct.

Use `E.24.UK` when a `U.*` spelling, type or kind wording, title, filename, heading, ToC row, or structural name must be retained, governed by `C.3` typed reasoning, kept as a dependent durable value, or renamed to the actual governed object. `E.24.UK` owns the detailed U-kind admission law, root and dependent U-kind governance, relation to `C.3` typed reasoning, and structural `U.*` handling. E.24 only records the result when the ontic-introduction decision needs to say whether a candidate name is retained as a root U-kind, retained as a dependent durable value, governed by `C.3` typed reasoning, or treated as a non-U object governed elsewhere.

#### E.24:4.0 - Constructive Foundation And Math-Lens Boundary

If a reader asks where FPF ontics get constructive grounding, start here and then follow the chain named by the current claim. E.24 supplies the ontic and slot-relation decision: the ontic is the `EntityOfConcern`, its `onticSlotRelation` is the ontology unit being settled, and the description and publication stay downstream.

For structural identity claims, the constructive chain is `E.14 -> B.3.5 -> C.13`: Working-Model relation first, declared `validationMode`, `tv:groundedBy`, and a reconstructible `Γ_m.sum`, `Γ_m.set`, or `Γ_m.slice` trace. That trace is a mathematical or constructive lens for grounding the claim; it does not become the public relation vocabulary and it is not required for non-structural ontics.

For non-structural ontics, use the governing identity, grounding, or recognition rule named by the direct pattern: for example episteme slot relation, work occurrence identity, `C.3` typed reasoning, `A.6` declaration shape, Concept-Set witnesses, formal-substrate or principle-frame declaration, or another accepted identity test. Use `C.29` when the mathematical lens itself is current; use `E.24.UK` when a `U.*` name is being admitted; use `E.24.PUB` when the question is description or publication.

`A.14`, `B.2`, and `A.15.1` carry BORO- and CCO-compatible identity and occurrence discipline. They support the constructive foundation; they do not create a separate durable-kind ontology.

Keep ontic levels separate before dependent patterns rely on the ontic.

An ontic is selected when FPF needs one governed `SlotRelation`: a typed n-ary relation with `SlotSpec` discipline that keeps several different typed objects together without fusing them into one umbrella kind. The ontic is the relation architecture: it says which SlotKinds exist, what ValueKinds and RefKinds can fill them, which governing pattern owns each filler, and what claims become admissible or blocked when a filler changes. A filled use is a value assignment over that relation. Under `C.29`, that filled assignment may be viewed as a tuple for tuple reasoning, or drawn as a graph or hypergraph for dependency reasoning, but tuple, graph, and hypergraph are mathematical-lens views, not alternate ontology heads.

Use the lens that preserves the current question. A tuple view is useful when the question is "which slots and values are present in this assignment?" A graph or hypergraph view is useful when the question is "which values depend on, constrain, or reopen which other values?" Neither view establishes that the filled values form one new kind; both must return to the same `SlotRelation`, SlotSpecs, and governing patterns for fillers.

When several partial ontologies already exist for the same project concern, E.24 does not pick one and delete the others. It selects the head ontic or local frame that can relate them without fusing their kinds: the existing objects become slot fillers, relation positions, graph-valued expressions, descriptions, publications, or neighboring governed values. This prevents duplicate ontology: a `U.Method`, `U.Work`, `U.Mechanism`, a source-local graph-position claim or current `TransformationFlowStructure` expression, role assignment, and publication can participate in one typed relation without becoming the same kind.

1. **Ontic root and identity.** Name the durable ontic or accepted local frame under concern and its stable identity criterion.
2. **Type-level `onticSlotRelation`.** State the SlotKinds, ValueKinds, RefKinds, relation set, required slots, optional-in-use slots, participation slots and check slots, species or record forms when needed, non-slot components, description boundary, and publication boundary. This is the reusable schema, not one filled use.
3. **Filled value assignment or ordinary-use core.** Give a compact filled instance or first-use frame only when users need one concrete application shape. It fills the type-level slots; it is not a second ontology and not a competing slot relation. Under `C.29`, that filled assignment may be viewed as a tuple when tuple reasoning is current.
4. **Description episteme and publication.** Claims about the ontic, its slots, its slot fillers, or relations among those values use `C.2.1`; a pattern section, table, diagram, publication, card, or view may describe the ontic, but it is not the ontic.
5. **Participation slots, check slots, and relation references.** Method, mechanism, work, evidence, source, gate, result, temporal adequacy, math lens, publication, and other typed values may be fixed slot positions in an ontic when claims about the ontic change admissible use, evidence relation, identity, responsibility, enactment, observation, modeling, permission, acceptance, refresh, or dependent-pattern obligations when those fillers change. They are not identity slots unless the ontic identity criterion explicitly depends on them.

Use these criteria when deciding whether a possible slot belongs to the ontic slot relation:

1. **Claim-impact.** A claim about the ontic becomes stronger, weaker, blocked, differently evidenced, or differently usable when the slot filler changes.
2. **Stable participation relation.** The filler specifies, constrains, enables, enacts, observes, models, times, evidences, publishes, authorizes, accepts, refreshes, or otherwise participates in the ontic through a stable relation.
3. **Duplicate-ontology resistance.** Leaving the slot outside would make dependent patterns copy negative catalogues, local tables, or shadow kinds.
4. **Kind preservation.** Including the slot lets the filler keep its governing pattern instead of fusing several kinds into one umbrella value.
5. **First-use cost.** Including the slot gives a bounded disposition check; it does not force a full neighboring-pattern application unless the current claim depends on that value.

The `?` marker or optional-in-use status does not mean "weakly belongs to the ontic." It means that every use considers the slot and records a disposition, while only some uses recover or assert a filler. Under open-world discipline, an unfilled slot means unknown, not recovered, not asserted, or not current for this claim; it does not assert that no such value exists.

Not every ontic needs every named layer. Add a named signature or kind level only when dependent patterns must rely on slot constraints across species or morphisms. Add a named filled-value assignment only when patterns need a publication-form-agnostic filled value; use C.29 tuple-view language only when tuple reasoning is current. Add named card, view, or publication species only when holonic working forms, views, or publication forms are themselves governed by the ontic. Name attached or non-slot components only when common adjacent structures must stay recoverable while remaining outside the ontic identity.

Keep annotation proportional. E.24 requires source-ontology recovery only for wording that can change the ontic, slot, filled value, governing pattern, admissible use, or dependent-pattern obligation. If a domain sentence already preserves those values, do not replace it with a typed paraphrase merely to show that an ontic exists.

This differs from pure ontology engineering because FPF patterns are action-facing: they help an engineer-manager decide what can be done, claimed, relied on, repaired, compared, or stopped in a problem situation. Ontic settlement supplies the object discipline that makes those actions intelligible. It says which objects and relations the pattern acts with, while the subject pattern still carries the practical move, boundary, evidence, and consequence.

Precision restoration uses the same discipline without turning it into lexical style. First recover the ad hoc ontic implied by the source situation: which meaning area, candidate object of concern, slots, neighboring patterns, and typed values are being compressed by the wording or source-side situation. Then repair toward the normative FPF ontic and linked typed values when such an ontic exists. If no normative ontic exists, use the direct governing patterns, keep the frame local, or open an E.24 ontic-introduction decision.

E.24 is the governing description pattern for `U.Ontic`. In that sense it is the ontic-of-ontics pattern: it describes the `U.Ontic` EoC, its slot relation, and its decision discipline. That self-application is allowed only under the same checks it imposes on other ontics; it is not a license for every local ontology-shaped bundle to become a `U.*` kind.

E.24 is compatible with modular ontology and ontology-design-pattern practice: modular ontology libraries and ontology design patterns show why reusable small ontology structures matter, and recent process-modeling work shows that implicit process patterns must be made explicit for reuse. E.24 is narrower and more FPF-specific: it selects when FPF should introduce a durable action-facing ontic, rather than importing an external microtheory or treating every reusable repair table as ontology.

If the choice between "write an ontic" and "keep the existing pattern constellation" needs reusable scoring, build a separate evaluation `CharacteristicSpace` through `A.19.ECS`. The evaluated object is then the FPF pattern-set architecture alternative, not the ontic itself: current constellation, local frame, or durable ontic. Candidate architecture characteristics include cross-pattern coupling, subject cohesion, explicit `onticSlotRelation` and `SlotSpec` discipline, invariant recoverability, duplicate-ontology resistance, dependent-pattern thinness, change-impact locality, first-use cost, and FPF ecology fit. E.24 uses these as diagnostic pressure for the introduction decision; it does not itself become the full architecture-characteristic evaluation pattern.

Within this split, E.24 contains the object split and the ontic-introduction decision needed before dependent patterns rely on a durable ontic. Publication-section rules, adequacy scales, wording-use restoration rules, and general pattern-set architecture evaluation are handled by the neighboring patterns named above.

Use the current split this way:

- use `E.24` for `U.Ontic` identity, type-level `onticSlotRelation`, semantic area, ontological neighborhood, dependent-pattern obligations, and non-use boundary;
- use `E.24.CD` when the current problem is detection of an ontic candidate, hidden-form classification, or sufficiency rationale for deciding whether a recurring construct is a durable ontic, a local use frame, direct governing-pattern use, or source wording only;
- use `E.24.PUB` when the current problem is the distinction among the ontic, the ontic-description episteme, the publication of that description, and publication forms such as cards, records, tables, schemas, diagrams, views, or source packets;
- use `A.19.ECS` only when the contested question is how to construct an evaluation `CharacteristicSpace` for comparing pattern-set architecture alternatives, such as current constellation, local frame, or durable ontic.

This split keeps E.24 ontic-first. Candidate detection, publication discipline, and contested evaluation remain neighboring governed objects rather than sections that make E.24 a general discovery, documentation, or scoring pattern.


Introduce or rely on a durable FPF ontic only after the ontic-introduction decision satisfies four checks.

#### E.24:4.1 - Check 1: Existing Governing Pattern Check

Name the current claim under decision and ask whether an existing pattern already carries it.

Use direct governing patterns first. If the case is method semantics, use `A.3.1`; if it is method description, use `A.3.2`; if it is mechanism meaning, use `A.6.1` and `E.20`; if it is work planning or dated work, use `A.15.2` or `A.15.1`; if it is evidence, gate, source, assurance, decision, release, or publication use, use that governing pattern.

Do not introduce a durable ontic only because several patterns are near each other or because one source word appears often.

#### E.24:4.2 - Check 2: Stable Identity Test

A durable ontic must have stable identity beyond one local wording issue, source expression, or first-use frame.

Ask:

1. What is the primary `EntityOfConcern`?
2. What changes the identity of this ontic?
3. What does not change identity, even if the publication form, notation, view, or local record changes?
4. Which bounded context is required for identity?
5. Which dependent patterns may rely on that identity?

If those questions cannot be answered, keep the construct as a local use frame or direct governing-pattern use.

#### E.24:4.3 - Check 3: Typed Slot Relation Test

A durable ontic must publish a small typed slot relation.

The ontic-introduction decision states:

One-screen first-use card:

```text
OnticIntroductionDecisionCard:
  concern: a recurring FPF subject looks spread across several typed values or patterns.
  decision: durable ontic | local use frame | direct governing-pattern use | source label only.
  onticRootIfSelected: the EntityOfConcern and stable identity criterion.
  typeLevelSlotRelation: required slots, optional-in-use slots, ValueKinds, RefKinds, and governing patterns for fillers.
  filledAssignmentExample: one concrete assignment over the slot relation, not a second ontology.
  publicationBoundary: pattern text, table, card, or diagram may describe the ontic; it is not the ontic.
  blockedLocalOverread: one tempting shadow kind, duplicate ontology, or publication-as-object error.
```

Before opening the heavier record, run two cheap guards. First, a slot-position label is not a filler kind: name the SlotKind, ValueKind, RefKind, and direct governing pattern separately under A.6.5. Second, role participation is not automatic `U.Role` admission: use A.2, A.2.1, and A.15 only when a work-facing role value or role-assignment claim is current; otherwise keep the value as a slot filler or neighboring relation governed by its own pattern.

Filled replay slice:

```text
OnticIntroductionDecisionCard:
  concern: bounded change talk compresses method, work, mechanism, timing, evidence, result, and flow-structure claims.
  decision: durable ontic selected.
  onticRootIfSelected: `U.Transformation`, identified by transformed entity or structure, bounded context, pre-state and post-state or delta, transformation relation, and boundary condition.
  typeLevelSlotRelation: `TransformationCore` plus linked participation slots for method, method description, mechanism, work plan, work occurrence, evidence relation, result relation, temporal aspect, and flow-structure relation; fillers keep their own governing patterns.
  filledAssignmentExample: pump-station backup architecture change, with `A.3.4` transformation core, `A.15` method and work chain, `C.27.TA` two-release-cycle recovery timing, and evidence references plus result references only where those claims are being made.
  publicationBoundary: `A.3.4` describes the ontic and its slot relation; a table, card, diagram, or transformation-flow view may publish that description but is not the transformation.
  blockedLocalOverread: one "transformation" label does not make method, mechanism, work plan, performed work, evidence, and result the same typed value.
```

The full replay form is heavier:

For ordinary first use, stop at the one-screen card unless dependent patterns will rely on the proposed ontic, the current claim changes admissible use, or a reviewer needs replayable evidence for why a local frame was not enough.

```text
OnticIntroductionDecision:
  ProposedOnticName:
  ProposedConceptHead:
  OnticAsEntityOfConcern:
  BoundedContext:
  StableIdentityCriterion:
  UKindDecision:
    verdict: selected U-kind, no U-kind, or blocked
    selectedUKindName:
    gain:
    cost:
    duplicateOntologyRisk:
    settlementObligation:
  SemanticAreaBaseConcept:
  SemanticArea:
  SemanticAreaSenseFamily:
  OnticSlotRelation:
    RequiredSlotKinds:
    OptionalSlotKinds:
    ValueKinds:
    RefKinds:
    RelationSet:
    SpeciesOrRecordForms:
    NonSlotComponents:
    DescriptionEpistemeBoundary:
    PublicationBoundary:
  OntologicalNeighborhood:
    HeadPattern:
    DependentPatterns:
    NeighboringGoverningPatterns:
    DirectUsePatternsBeforeNewConcept:
  ExistingGoverningPatternsReused:
  DependentPatternObligations:
  SlotPositionLabelsThatAreNotNewKinds:
  NonUseBoundary:
```

For E.24 itself, this record is already decided: `ProposedOnticName = Ontic`, `OnticAsEntityOfConcern = connected ontology fragment under FPF settlement`, and `UKindDecision.verdict = selected U-kind` with `selectedUKindName = U.Ontic`. Other proposed ontics must still fill the record by value; they do not inherit the `U.*` decision from E.24.

The slot relation must use `A.6.5` slot discipline and must not define a second slot discipline. A role-like, method-like, mechanism-like, source-like, publication-like, temporal, or architecture-like slot-position label is not a kind decision. It becomes a kind decision only when the governing pattern names that filled value by value and admits that kind.

#### E.24:4.4 - Check 4: Placement and Dependent-Pattern Obligation

Declare:

- `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`;
- selected `ontologicalNeighborhood`;
- pattern nest and why that placement follows the primary `EntityOfConcern`, relation, or claim;
- first subject pattern to write;
- dependent patterns that may rely on the slot relation;
- draft-only or missing loci that cannot yet govern current claims;
- names that pass `F.18`;
- evaluation pattern for the resulting pattern or DRR, usually `E.21` for a pattern and `E.9.DA` for the DRR.

If the decision selects a durable ontic, write the governing head pattern before dependent patterns rely on it. If only a bounded local frame exists, name it as non-governing and state the claims it carries and does not carry by value. If no governing head pattern is written, do not cite the proposed ontic as governing current FPF use.

#### E.24:4.5 - Local Use Frame Decision

Use a local use frame when a recurring construct is useful for one bounded application family and its filled positions are already governed elsewhere.

A local use frame:

- names the concern, use, or relation being handled in that bounded application family;
- links separately governed typed values without turning the link into a new `U.*` kind;
- points each value to its governing pattern;
- blocks one overread or shadow-kind temptation;
- does not mint a `U.*` kind;
- does not become a project record, evidence record, gate record, method, mechanism, work plan, or work occurrence.

Precision restoration may use a local use frame in one of its slots, but the frame is not defined by repair. P2W, work planning, evidence use, gate use, architecture use, or publication use may use the same subject ontology in different slots for different practical purposes.

### E.24:5 - Archetypal Grounding

Use these slices as archetypes for the ontic-introduction decision. They are not a recommended progression. Each slice shows which object is being governed, which ontic or local use shape is selected, and which tempting overread is blocked.

#### E.24:5.1 - Episteme as Durable Ontic

`U.Episteme` passes E.24. It has stable identity, a normative `U.EpistemeSlotRelation`, required slots, optional slots, filled assignments, card and publication species, a description boundary, a publication-form boundary, and dependent patterns in C.2, A.6.2-A.6.4, and E.17. `C.2.1` is therefore the right form: a subject pattern with a small typed ontic slot relation and dependent-pattern obligations.

#### E.24:5.2 - Multi-Pattern Subject Matter as an Ontic-Candidate Archetype

A project phrase such as "algorithm", "process", "solver", "workflow", "system", "quality", "time", "source", or "architecture" can point to one recognizable subject that is spread across several FPF values and patterns. The point of this archetype is not that all such subjects are one kind. The point is that E.24 must decide the status of the cross-pattern subject before patterns rely on it.

In this archetype, "process" and "workflow" are source-side labels until recovered. They may point to method, method description, work plan, dated work, transformation-flow structure, evidence relation, source relation, gate relation, result relation, publication relation, or another governed value. They become durable FPF ontology only through the same E.24 decision as any other proposed ontic; otherwise keep them quote-only, reduced-use, or resolved under the governing patterns that already carry the claim.

The E.24 move is:

1. name the candidate subject under concern;
2. list the typed values, relation positions, and governing patterns that currently carry pieces of it;
3. decide whether those pieces already close under direct governing patterns, whether a bounded local use frame is enough, whether a durable ontic with a head pattern and slot relation is required, or whether the apparent subject is only a source label or wording compression;
4. if a durable ontic is selected, write or cite the governing head pattern before dependent patterns rely on it.

Method, work, and change are one current stress case for this archetype. A project concern about changing, producing, selecting, deriving, controlling, maintaining, planning, performing, measuring, or carrying a result may involve `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, dated `U.Work`, source-local process labels or workflow labels, transformation-flow representation, evidence relation, source relation, gate relation, result relation, publication relation, and temporal relation. That spread is an E.24 applicability signal. It does not by itself settle either "make one new ontic" or "existing constellation is enough".

The same decision applies to other broad heads. A proposed `system`, `relation`, role-participation, role-assignment, slot-discipline, `characteristic space`, `temporal dynamics`, or `architecture` ontic must pass the same decision. E.24 supplies the decision form; the governing subject pattern supplies the subject ontology and source set by value.

Dependent subject patterns may keep a thin cue: when one recognizable concern spans several typed values, name the current relation being made and use that relation's governing pattern. They must not copy a full negative formula, must not call a local constellation a durable ontic before the E.24 decision, and must not assign one typed value to two kinds unless a governing pattern explicitly admits that dual typing. Slot-position labels do not create alternate ontology.

#### E.24:5.3 - Draft Locus as False Authority

A draft ToC row or older source label may name a calculus, family, or object before current FPF has a governing pattern for it. Such a label can guide investigation, but it cannot govern current use.

Example: older source wording may name a method calculus before current pattern text carries it. If no current pattern text carries it, it is not a governing pattern for current FPF use. Use the current patterns that govern the filled values: `A.3.1` for method semantics, `A.3.2` for method description, `A.15.2` for work planning, `A.15.1` for dated work, and `B.1.5` for method composition when ordering is current. A separate method calculus can govern other patterns only after it has its own E.24-style ontic decision, stable identity, slot relation, and dependent-pattern declaration.

The same test applies to any draft-only locus. If the label has no current governing text, do not cite it as ontology. Either cite current governing patterns, keep the label as investigation context, or open an E.24 ontic-introduction decision.

#### E.24:5.4 - System-Like Head Concepts

`system`, `episteme`, `architecture`, `method`, `mechanism`, `temporal claim`, `dynamics`, and `change` can each appear as a broad head for many dependent FPF patterns. That breadth is not itself enough to create a durable FPF ontic. Apply E.24 before treating a broad head as current governing ontology: name the primary `EntityOfConcern`, stable identity, `onticSlotRelation`, selected `semanticArea`, selected `ontologicalNeighborhood`, dependent patterns, description boundary, and publication boundary. If those rows are missing, use the current governing patterns that already carry the claim and do not cite the broad head as if it supplied current slot discipline.

#### E.24:5.5 - Mature Comparator Discharge

`E.24` is mature only when its selected mature-pattern ingredients are present in the body, not only in a separate planning or evaluation note.

| Comparator | Selected mature ingredient | Current E.24 locus | Lowering condition |
| --- | --- | --- | --- |
| `C.2.1` | stable identity plus small typed slot relation for a durable ontic | `E.24:4.2`, `E.24:4.3`, `E.24:5.1` | Lower if E.24 asks for fields but no longer asks what preserves or changes identity. |
| `E.20` | introduction discipline for one governed subject family | `E.24:4.1`, `E.24:4.4`, `E.24:8` | Lower if mechanism-specific doctrine is copied here instead of left with `E.20`, `A.6.1`, and related patterns. |
| `E.8` | publication-form and section-order boundary | `E.24:0`, `E.24:4.4`, `E.24:6`, `E.24:8` | Lower if E.24 starts regulating pattern format instead of the ontic-introduction decision. |
| `E.10.ARCH` | wording-use restoration architecture that uses existing subject ontology before sending wording symptoms to the governing precision-restoration pattern | `E.24:4.1`, `E.24:4.5`, `E.24:5.2`, `E.24:7` | Lower if a local use frame is treated as a durable ontic or if a wording trigger alone creates a new ontology unit. |
| `F.18` | durable naming after ontology is settled | `E.24:4.4`, `E.24:6`, `E.24:7` | Lower if a new name substitutes for identity, slot, and dependent-pattern settlement. |

### E.24:5.6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.
Scope: the authoring decision for a durable ontic, direct governing-pattern use, or local use frame, not the subject matter governed by the resulting pattern.

This pattern intentionally biases toward explicit identity, typed slots, and governing-pattern reuse. It resists five recurring distortions:

- **shadow-kind bias:** repetition of a local use frame is mistaken for a new object;
- **placement bias:** a pattern nest or draft ToC row is mistaken for semanticArea or governing text;
- **name bias:** a cleaner term hides unresolved kinds, slots, and relations;
- **semio-bias:** discussion of descriptions, publications, or review evidence displaces the ontic or subject matter being introduced;
- **process-bias:** development-state, publication-state, evaluation-state, or process evidence status is copied into ontic or subject-matter content.

The mitigation is the same in each case: recover the primary `EntityOfConcern`, stable identity, typed slot relation, selected `semanticArea`, selected `ontologicalNeighborhood`, and governing-pattern reuse before naming, placement, dependent pattern reliance, or publication form starts governing the decision.

### E.24:6 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E24-1` | The authoring decision names the primary `EntityOfConcern`, bounded context, and current claim before proposing a durable ontic. |
| `CC-E24-2` | Existing governing patterns are checked by value before a new ontic is selected. |
| `CC-E24-3` | A durable ontic publishes stable identity criteria and says what does and does not change identity. |
| `CC-E24-4` | A durable `onticSlotRelation` names SlotKinds, ValueKinds, RefKinds, relation set, species or record forms, non-slot components, description boundary, and publication boundary. |
| `CC-E24-4a` | When constructive grounding is claimed, the text names the direct grounding rule. Structural identity claims use the `E.14 -> B.3.5 -> C.13` chain with Working-Model, `tv:groundedBy`, and `Γ_m`; non-structural ontics use the identity, grounding, or recognition rule of their governing pattern. |
| `CC-E24-5` | The decision declares the selected `ontic` components by value: `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `onticSlotRelation`, selected `ontologicalNeighborhood`, pattern nest, and dependent-pattern obligations, without treating any of them as synonyms. |
| `CC-E24-5a` | The pattern keeps ontic root identity, type-level `onticSlotRelation`, filled value assignment or ordinary-use core, description episteme, publication form, and neighboring relation references distinct; a filled core or neighbor list is not treated as a second ontology. |
| `CC-E24-6` | Draft-only loci are marked non-governing until a current governing pattern is written or a bounded local frame states the claims it carries and does not carry by value. |
| `CC-E24-7` | A local use frame is explicitly non-`U.*`, non-ontic, and points typed values to their governing patterns. |
| `CC-E24-8` | The selected name passes `F.18`; the name does not hide a second ontology or one umbrella for several kinds. |
| `CC-E24-8a` | Durable `U.*` names, reusable SlotKind heads, species or record-form names, public ids, Core-facing heads, and cross-context labels use `F.18`; `F.17 UTS` and Name Card material is opened only when that name becomes public, Core-facing, or cross-context, and never replaces `A.6.5` SlotSpec discipline. |
| `CC-E24-8b` | A `U.*` spelling, type or kind wording, structural heading, title, filename, or ToC row that claims U-kind force is governed by `E.24.UK` before naming patterns are asked to choose or keep a public term. |
| `CC-E24-9` | Pattern-quality and DRR-adequacy checks stay in `E.21` and `E.9.DA`; they are not copied as user-facing ontic or subject-matter content. |
| `CC-E24-10` | Dependent patterns state how they rely on the head ontic or local use frame without duplicating the whole slot relation. |
| `CC-E24-11` | Slot-position labels, including role-like labels, method-like labels, mechanism-like labels, temporal labels, source labels, and publication labels, do not create alternate ontology; `U.Role` is not a SlotKind, SlotKind is not a role, and role participation uses a slot-disciplined `U.RoleAssignment` only when `A.2`, `A.2.1`, and `A.15` role-governing patterns govern the case. |
| `CC-E24-12` | Ontic slot talk uses slot-language (`onticSlotRelation`, `SlotSpec`, `SlotKind`, `ValueKind`, `RefKind`, slot discipline, slot boundary, relation boundary); `interface` is used only when a governing boundary, module, signature, mechanism, or architecture pattern makes interface meaning current. |
| `CC-E24-13` | Source-ontology annotation is proportional: decision-changing kind, slot, relation, admissible-use, and governing-pattern differences are recovered, while stable domain prose is not expanded into type labels. |
| `CC-E24-14` | When candidate detection, publication-form discipline, or contested evaluation is current, apply `E.24.CD`, `E.24.PUB`, or `A.19.ECS` respectively; E.24 itself stays centered on `U.Ontic` identity, slot relation, semantic area, ontological neighborhood, and dependent-pattern obligations. |

### E.24:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Shadow-kind by repetition | The same local record appears in several patterns and starts being cited as an object. | Apply E.24; either write a durable ontic pattern or lower the construct to a local use frame. |
| Draft locus as authority | A ToC row is cited as if it supplied current governing text. | Treat it as investigation cue only; use current governing patterns until the pattern exists. |
| Slot list without identity | A pattern lists fields but never says what identifies the ontic. | Add stable identity criteria or lower the construct to a local use frame. |
| Pattern nest as ontology | The numbering area is treated as the semantic unit. | Declare `semanticArea`, `ontologicalNeighborhood`, and primary `EntityOfConcern` separately. |
| New name as solution | The repair invents a smoother term while the typed values remain mixed. | Recover kinds, slots, semantic area, and ontological neighborhood first; name only after the ontology is settled. |
| Slot-position kind inflation | A role-like, method-like, temporal, source, or publication position receives a fresh kind name only because it occupies a slot. | Keep the value's kind under its governing pattern and record the slot position separately. |
| Interface metaphor for slots | A slot relation, SlotSpec, relation position, or filler constraint is called an interface only because that word feels familiar. | Rename to the slot-language term unless a governing boundary/interface pattern makes interface meaning current. |
| Typed paraphrase overload | A readable subject sentence is rewritten as a full chain of kinds, slots, and source-ontology labels without changing the claim. | Keep the subject sentence and annotate only the decision-changing slot or value under decision. |

### E.24:9 - Consequences

- FPF can introduce rich ontology units without letting every local use frame become a new ontology.
- Draft-only loci stop acting like current governing patterns.
- Dependent patterns get a stable slot relation when a durable ontic is selected.
- The cost is a short ontic-introduction decision before writing or relying on a durable ontic.

### E.24:5.7 - Rationale

FPF needs a pattern for ontic introduction because many important FPF ontology units are not one term, one field, one taxonomy branch, or one U-kind. They are small typed slot relations with identity criteria, slots, admissible values, record or publication species, dependent patterns, and action-facing use boundaries.

The compactness gain is the central reason for `U.Ontic`. A taxonomy-heavy design tends to create a new type for each contextual position: reviewer, evidence reviewer, architecture reviewer, work reviewer, mechanism reviewer; method, mechanism, procedure, process, algorithm; record, evidence record, gate record, authority record. An ontic design instead keeps a small number of governed ontology units and lets many objects fill typed relation slots. A relation slot works like a parameter position in a relation-function: the value is typed and constrained by the slot, but it does not become a new kind merely because it fills that position.

`U.Episteme` is the main stress case inside FPF. `C.2.1` does not define epistemes by a long taxonomy of descriptions. It defines stable identity and a small slot relation: EntityOfConcernSlot, claim graph, viewpoint, reference scheme, grounding, publication-form and source boundaries, and dependent episteme patterns plus publication patterns. The same small slot relation can hold many claim kinds, descriptions, views, publications, and project cases without minting a new episteme kind for each one.

Role participation is the second stress case. It is not the claim that roles are slots, slots are roles, or role is a special case of slot. `U.Role` remains useful because holons participate in contexts under context-bound role values, and `U.RoleAssignment` remains useful because the assignment binds holder, role, context, and window before work can be enacted through that assignment. The compactness gain comes from representing `U.RoleAssignment` as a typed relation with slot positions while preserving the governing kinds of the filled holon, role, context, window, method, plan, and work values.

This prevents a separate ontology for every participation name while preserving the real action-facing gain of the role patterns. "Engineer", "reviewer", "evidence reviewer", and "operator" do not become new system kinds merely because they appear in project language. They are recovered, when the case requires it, as role values and assignment relations under A.2, A.2.1, and A.15. Conversely, arbitrary relation participants such as a transformed television, an evidence target, an input, an output, a base, or a dependent are slot fillers or relation participants under their governing patterns, not `U.Role` values merely because ordinary language can say they "play a role."

Without E.24, FPF ontology development oscillates between two bad moves. One move invents a new umbrella name and leaves the mixed ontology intact. The other refuses the new name but still leaves several patterns carrying duplicated local slot doctrine. E.24 gives a bounded authoring decision: use an existing governing pattern, introduce a durable ontic, keep a local use frame local, or keep the source label quote-only or reduced-use.

The pattern is deliberately about the introduction decision. It does not define every ontic and does not become a registry of system, episteme, method, mechanism, architecture, source, quality, temporal, dynamics, or change objects. Each accepted subject matter still needs its own governing pattern or accepted local frame.

### E.24:5.8 - SoTA-Echoing

E.24 does not claim to replace ontology engineering, OWL-style formal ontology, or UFO-style foundational ontology. Its governing reason is the current FPF need for action-facing ontology compactness, plus a narrow SoTA echo:

| Source family | Current lesson for E.24 | FPF decision |
| --- | --- | --- |
| W3C [SKOS Reference](https://www.w3.org/TR/skos-reference/), 2009, and W3C [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), 2012. | Reference-baseline use, not a current-best SoTA claim: SKOS remains useful for controlled vocabularies, labels, broader and narrower relations, and concept schemes; OWL remains useful for classes, properties, individuals, axioms, and declarative semantics. | Adopt as baseline and adapt: do not present FPF ontology as one taxonomy tree. Use taxonomy relations where they fit, but introduce an ontic only when stable identity and typed slot relation are required. Current competitive guidance comes from the 2024-2026 modular ontology, interoperability, process-representation, and foundational-ontology rows below. |
| Modular ontology design patterns, MODL/MOMo, and commonsense ontology micropatterns, including [Shimizu and Hitzler 2024](https://arxiv.org/abs/2411.09601) and [Eells, Dave, Hitzler, and Shimizu 2024](https://arxiv.org/abs/2402.18715). | Current ontology-engineering work emphasizes reusable small ontology structures and pattern libraries, including LLM-assisted ontology engineering where modularity becomes more important, not less. | E.24 adapts the modular-pattern lesson: a durable ontic is a reusable FPF ontology unit with a governing head pattern and dependent-pattern obligations, not a local checklist copied across patterns. |
| [Qiang 2025/2026 ontology-interoperability ecosystem](https://arxiv.org/abs/2507.12311). | Overlapping and conflicting concepts block interoperability; current approaches combine design patterns, matching and versioning, and validation across the ontology lifecycle. | E.24 prevents shadow ontology and type explosion before matching and versioning becomes a rescue operation. It asks whether a proposed head is a durable ontic, existing governing-pattern use, local use frame, or non-use. |
| [Norouzi, Hertling, Waitelonis, and Sack 2025 process-representation ODP work](https://arxiv.org/abs/2509.23776). | Process ontologies and workflow ontologies often contain implicit design patterns; reuse suffers when those patterns are not explicit and accessible to domain experts. | E.24 uses this as a caution for any process-like or temporal subject: do not hide process, method, work, or temporal material in a local use frame. If such material needs a durable ontic, write its own slot relation and governing pattern. |
| [Almeida, Guizzardi, Sales, and Fonseca 2026 gUFO](https://arxiv.org/abs/2603.20948); UFO and OntoUML role, relator, situation, and high-order type practice. | Current foundational-ontology work uses type typology, reification of intrinsic and relational aspects, situations, and high-order types to avoid naive taxonomic flattening. | E.24 keeps role-assignment, relation-slot, signature, interface-as-boundary, episteme and publication distinctions, and mechanism, method, and work distinctions as slot-governed ontology architecture rather than one taxonomic tree. |

This SoTA echo justifies a bounded conclusion: ontic-based FPF ontology architecture gives compactness and structure compared with a taxonomy-only design when the governed subject depends on identity, relation slots, dependent patterns, and action-facing use. It does not make every modular ontology pattern an FPF ontic. External sources govern the decision only when the DRR selects their payload for the specific ontic or subject matter under decision.

Use external sources when one ontic or subject matter itself depends on a source tradition. Put that source decision in the DRR and in the governing pattern for that subject matter. Do not make E.24 carry a borrowed external theory of every durable ontic.

#### E.24:5.9 - Currentness and Lowering Logic

Treat E.24 as current for ontic-introduction decisions only while the current FPF slot, precision-restoration, naming, and pattern-quality apparatus remain the governing source set. Lower E.24's current authority for a case when one of these changes governs that case:

- a new accepted FPF pattern changes slot discipline, `EntityOfConcern` discipline, or durable-name discipline;
- a local use frame begins to be reused as if it were a durable ontic;
- a draft locus becomes a current pattern and changes the ontic-introduction decision;
- dependent patterns start copying a slot relation instead of relying on the governing head pattern;
- external source work governs the introduction method itself rather than one selected ontic or subject matter.

Lower the decision before use when E.24 cannot decide among durable ontic, local use frame, existing governing-pattern use, quote-only source label, or reduced-use source label. A failed decision is not resolved by adding more fields; it is resolved by returning to `E.24:4.1` and settling which object, slot relation, semantic area, ontological neighborhood, and governing patterns actually govern the decision.

### E.24:8 - Relations

- **Builds on:** `E.8`, `E.9`, `E.9.DA`, `E.10`, `E.10.ARCH`, `E.20`, `E.21`, `F.18`, `A.6.5`, `C.2.1`, `E.24.CD`, and `E.24.PUB`.
- **Coordinates with:** `E.24.UK` for durable U-kind admission and structural-name U-kind settlement; `C.29` when the mathematical lens itself is current; `E.14`, `B.3.5`, and `C.13` for structural constructive grounding; governing patterns that describe durable ontics or their filled values, especially `C.2.1` for epistemes; `A.2`, `A.2.1`, `A.2.2`, and `A.15` for role participation, role assignment, capability, and role-method-work alignment; `A.6.1` and `E.20` for mechanisms; `A.3.1` and `A.3.2` for method and method description; `A.3.4`, `E.18`, and `C.27.TA` for transformation, transformation-flow, and temporal-aspect examples; and precision-restoration patterns such as `C.2.P`, `C.2.P.DR`, and `C.30.STRAT`.
- **Used by:** DRRs and pattern authors when repeated slot-relation-shaped material is being considered as either a durable ontic or a local use frame.

### E.24:End

