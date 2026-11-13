## A.22 - Structure and Structural Views

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.22:1 - Problem frame

Use this pattern when a practitioner needs to select `U.Structure` as the `EntityOfConcern`: an organization among constituents and obtaining relations, selected to expose a relation class, applied constraint, invariant, variation class, preserved arrangement, or lost arrangement that changes the next engineering or reasoning action.

Recover the organization selected for the named use:

1. identify every constituent independently through the content that defines its kind and identity;
2. recover the relation occurrences among those constituents that obtain under their predicates;
3. state the constraints applied to those constituents and relations, plus the named selection-use frame that says what question or action this organization serves;
4. name the resulting selected organization and the admissible action or stop that follows.

When the account asserts dated selection Work, establish its independent grounds under §4.1. Those facts explain the performed selection and remain outside `U.Structure` identity. If the judgment must persist, identify a separate C.2.1 result episteme whose claim content designates the selected structure.

The four values above can be stated in ordinary prose or recovered from an existing description. The following optional aid also keeps use limits and any separately needed claims visible:

```text
StructureQuestionCard@Project:
  named selection use:
  independently identified constituents:
  obtaining relation occurrences selected:
  constraints applied:
  selected structure:
  preserved structure:
  lost, hidden, or excluded structure:
  admissible action:
  stop or non-admissible overread: stop or return condition
  grounded non-admissible overread, optional:
  selecting system, method, and dated work, only when dated Work is asserted:
  selection-result episteme, when a durable result is needed:
  claim scope or effective reference scheme of that claim, if current:
  reliance relation, if a neighboring reliance claim is being made:
```

`StructureQuestionCard@Project` is a project-side triage aid for this selected-structure use. It is not a new structure kind. Fill the reliance row only when extraction, coarsening, source-description, base-dependence, grounding, evidence, lens, simulation, representation, or action reliance is being claimed; otherwise leave it unused and keep the move on selected structure.

The `@Project` suffix is a local retrieval cue. If the account separately asserts a composite project `U.Work`, identify that Work and how the current selection, decision or description concerns it. The suffix supplies neither identity nor that relation; the same applies to `ArchitectureStructureKindTriage@Project`.

Stop when the selected organization and next use are clear. Develop a neighboring description, view, publication, extraction, comparison or other claim only when the receiving task needs it.

What goes wrong if A.22 is missed: the practitioner reasons from the visible diagram, source publication, source-use record, lens output, generated representation, project record, or architecture description instead of asking which organization is selected and what loss or reliance boundary matters for action.

What A.22 buys in practice: a practitioner can name selected structure, state preserved and lost structure, name source-basis or lens reliance only when it is being claimed, add a `StructureUseReturnCondition` when loss matters, and apply the FPF definition or test for any non-structure claim being made.

Not this pattern when the question under repair is grounded architecture adequacy, architecture structural-view adequacy, or mathematical-lens use. Use `C.30`, `C.30.ASV`, or `C.29` respectively. For any other claim, use the pattern that defines or tests that claim and keep A.22 only to the selected-structure portion.

For unresolved wording: when the wording still may name a structure, a structure description, an architecture description, a view, a publication form, or another claim, use `C.30.P` or `C.30.STRAT` first as triggered. Apply A.22 only after the selected-structure claim or structure-view portion is recoverable.

### A.22:2 - Problem

FPF needs a selected-structure EntityOfConcern that is usable across domain ontologies, mathematical formalisms, architecture notations, and publication forms. Working projects often notice that "the structure" is doing work:

- dependencies repeat across cases;
- a method or work description hides an invariant relation;
- a model compresses a trace by preserving one relation class and losing others;
- a diagram shows an arrangement but is mistaken for the arrangement itself;
- a mathematical lens exposes preserved structure but is then overread as ontology;
- an architecture discussion needs selected structure over a holon before it can describe architecture.

How can FPF let a practitioner name structure as an EntityOfConcern while preserving the distinction between:

- selected structure and the source-description relation, source-use relation, evidence relation, lens output, simulation, generated representation, or declared substrate from which it was inferred or declared;
- structure and a Description episteme or view of that structure;
- structure and a publication face, diagram, table, graph, or publication form;
- structure and mathematical-lens application;
- structure and another FPF claim kind whose definition or test remains in the cited pattern;
- structure in general and architecture-specific structure selected by `C.30`.

### A.22:3 - Forces

| Force | Tension |
| --- | --- |
| First-principles structure EntityOfConcern vs ontology inflation | FPF needs a reusable selected-structure EntityOfConcern for organizations that expose relations, applied constraints, invariants, variation classes, preserved arrangement, and lost arrangement, but adding one such EntityOfConcern can accidentally invite many false root kinds. |
| Useful compression vs structure-use return | Structure makes work easier by compressing cases, but a `StructureUseReturnCondition` is needed when compression, extraction, coarsening, source-description reuse, base-dependence reuse, grounding reuse, evidence reuse, lens reuse, simulation reuse, or representation reuse hides a distinction needed for action. |
| Description and view usability vs structure confusion | Descriptions and views make structure inspectable, but a useful view can be mistaken for the structure itself. |
| Mathematical-lens application vs mathematical overread | C.29 lens output is usable within its declared mapping, preserved structure, lost structure, and stop condition; any evidence, causal, assurance, or decision claim uses its predicate and result. |
| Architecture dependency vs architecture takeover | Architecture uses selected structure through `C.30`; A.22 does not import architecture as its parent or make every structure an architecture. |
| Plain engineering speech vs Tech recovery | Words such as structure, graph, architecture, module, function, interface, pattern, block, layer, level, tier, stack, expert, cache, router, and gate can remain in Plain prose, but a claim that depends on their precise meaning needs recoverable Tech fields and pattern applications. Use `C.30.STRAT` when a source label leaves the selected-structure claim ambiguous. |

### A.22:4 - Solution

Select `U.Structure` as the A.22 ontic head: a dependent, non-agentive organization selected from independently identified constituents and obtaining relation occurrences under applied constraints for one named use frame.

The constituents keep their identities and kinds. Every selected relation occurrence must already satisfy its defining predicate and retain identity under that predicate's occurrence rule. A system or practitioner selects their organization; A.22 supplies the identity and boundary rule for that selected organization.

The applied constraints are the constraint claims used in the selection judgment, not the identity of the document, table, rule card, or constraint episteme that carries them. A usable frame states the question, admissible action, and stop or return condition. A generic phrase such as “current use” or “appropriate structure” is not a use frame. Any optional explanatory overread follows F.19:4's plausible-reader test and remains outside structure identity.

Ordinary structure selection needs the four discriminators below. An account of dated selection Work additionally uses its admission grounds; a durable result episteme, operation binding, direct participation relation or decision also retains its identity outside the structure.

A diagram, graph, table, model, description, view, or publication may designate, represent, or describe the selected organization and its already identified constituents. Use C.2.1 for the describing episteme, E.17.0 for claimed view membership, and the publication or source-use patterns for those claims. Use C.29 when a mathematical representation-choice, transfer, or reliance question remains unresolved; the participant and relation predicates remain the obtaining basis.

#### A.22:4.1 - Base `U.Structure` Identity and Selection

For a selected structure `S`, recover four identity discriminators:

```text
StructureIdentity(S) = <
  independently identified constituents,
  selected obtaining relation occurrences,
  constraints as applied,
  one named selection-use frame
>
```

Base `U.Structure` identity has no ambient context field. A bounded-context label, `U.ContextSlice`, `U.ClaimScope`, project record, description, view, graph, table, or publication is not automatically an additional discriminator. If a scope is referenced by an applied constraint, that constraint contributes through the third discriminator. If a model-use structure is independently selected as a constituent of another structure, it contributes through the first discriminator.

The first discriminator is a plurality, not a graph node set created by notation. A separately useful C.13 collection may designate the same constituents, but collection membership neither proves parthood nor replaces their identities. The second discriminator contains the relation occurrences chosen for this organization; a relation name, edge label, tuple position, or adjacency row is insufficient. The third contains the semantic constraints applied; changing only the rationale, formatting, or publication of an unchanged constraint claim does not change this discriminator. The fourth names the use question, admissible action, and stop or return condition.

Two references resolve to the same `U.Structure` when all four discriminators resolve to the same values. A changed designator, selecting system, method, work occurrence, result episteme, description, graph, representation scheme, view, or publication leaves the structure unchanged when the four discriminators remain unchanged. Replacing a constituent, a selected relation occurrence, an applied constraint, or the named use frame can identify another structure.

If a relation occurrence may have been reidentified, apply its relation pattern before reapplying A.22. A change to an explanatory guard alone does not change identity. If its content changes an applied constraint or a frame value, compare that existing discriminator.

If no current predicate definition, applicability condition, or occurrence rule can identify the required constituent or test the obtaining-relation claim for this use, stop at the description or representation and return `missing-governor`. If the governor exists and the available case basis is sufficient to apply its positive test but that test fails, return `factually unsupported`; if a fact needed to decide the test is unavailable, return `missing-information`.

State a negative only when an applicable non-obtaining criterion or complete closure basis and satisfying facts establish it. If the constraints or named use frame are absent, name that gap: the material may show an arrangement, but it does not yet support the claimed selected `U.Structure`.

For asserted dated selection Work, first establish the A.13 core: the performing System, local agential-role kind and membership criterion, and an obtaining assignment of its declared direct species for the relevant scope and time. A.15.1 independently admits the performance with its enacted Method and extent; F.6 applies afterward only for assignment-bound attribution. Establish any direct participation or A.6.1 operation binding needed by the receiving claim separately.

The following two records are recovery aids, not new ontic kinds. In `SelectedStructureBasis`, the selected structure, constituents, selected obtaining relations, applied constraints, and use frame state identity; the preserved/lost and action/stop rows state the use-return boundary rather than adding identity fields.

```text
SelectedStructureBasis:
  selectedStructureRef:
  constituentRefs:
  selectedObtainingRelationOccurrenceRefs:
  appliedConstraintClaimRefs:
  namedSelectionUseFrame:
  preservedStructure:
  lostHiddenOrExcludedStructure:
  admissibleAction:
  stopOrNonAdmissibleUse: stop or return condition
  groundedNonAdmissibleUse?:

StructureSelectionUse:
  selectingSystemRef:
  selectionMethodRef:
  selectionWorkRef:
  directParticipationOrOperationBindingRefs?, when the receiving claim needs them:
  selectedStructureRef:
  selectionResultEpistemeRef?, when the judgment must persist:
  selectionDecisionRef?, when an accountable choice is current:
```

`StructureSelectionUse` is used when that dated performance is asserted; it records how the system performed the selection and reached the judgment. `SelectedStructureBasis` records the four identity discriminators plus the use-return boundary. Do not copy the system, work, method, result episteme, or decision into the structure basis.

A `U.ClaimScope`, effective reference scheme, or model-use structure that merely qualifies a claim about either record does not enter base identity. A scope referenced by an applied constraint or a model-use structure selected as a constituent enters only through that already declared discriminator. `stopOrReturnCondition` is another name for `stopOrNonAdmissibleUse`, not an independently filled value.

A.22 structure-aspect names such as functional, mereological, modular, transformation-flow, control, semantic, causal, dynamical, algebraic, topological, geometric, or coarse-grained remain cues for which relations and constraints to recover. They do not identify a structure without the four discriminators. C.30.ASV `ArchitectureStructureKindRef` values remain architecture-local classifiers; a matching label does not imply identity.

#### A.22:4.1a - Auxiliary boundary

Use description, publication, source-use, evidence, work, gate, decision, release, architecture-description, and mathematical-lens patterns when those claims are being made. The A.22 application contains the selected-structure portion and any structure-use return condition required by §4.5; use each neighboring pattern only for the definition or test it contributes. A publication, diagram, graph, table, dashboard, file, model card, generated representation, or lens output may make a structural description or view available; it does not become the selected structure or supply neighboring claim authority by appearance.

#### A.22:4.1b - Constraint-governed unfolding structure

Use `A.22.CGUS` to clarify available continuations and their conditions. Use its formal branch when the named use depends on the identity or CGUS membership of the selected organization. Then identify one A.22 structure with several locally declared loci whose bindings identify the independently selected constituents for the unfolding question; its selected obtaining relation occurrences and applied constraint claims must define at least two potential continuations across allowed cases. The loci are not free-standing A.6.5 slots. A separate case- and time-indexed result may enable zero, one, or several candidates. This specialization remains `U.Structure`; a Method, plan, Work or present-case continuation result is a separate object.

A route card, table, graph, README entry, narrative, slide, or happy-path example may describe or demonstrate the unfolding structure, but it is not the structure itself.

#### A.22:4.1c - Bounded And Cross-Context Model-Use Structure Specializations

`BoundedModelUseStructure` is a `U.Structure` selected over one model episteme, admitted model-use holons, the obtaining model-applicability, actual model-use, and model-expression-coherence occurrences defined and tested by A.1.1, applied constraint claims used by the selection judgment, and one named bounded-model-use frame. Its A.22 identity uses exactly those constituents, selected occurrences, constraint claims, and frame.

A claim scope, membership outcome, boundary display, or carrier is not an applied constraint by itself; a constraint claim may instead state a proposition about that scope or its A.2.6 membership predicate. No boundary crossing participates in that identity.

Continuity across model editions additionally requires the C.2.1 episteme-edition relation and declared A.1.1 continuity rule. `BoundedModelUseStructure` is not a holon, description, view, or endpoint manufactured by a later crossing.

`CrossContextRelationStructure` is a conditional specialization of a different already identified `U.Structure`. Membership requires obtaining crossing occurrences that satisfy independently defined predicates, selected among several bounded model-use structures, applied constraints, and one named crossing-analysis use, with all four A.22 base discriminators established.

Until a compatible crossing predicate and current facts establish those occurrences, a Context Map can describe only a proposed crossing organization and no positive `CrossContextRelationStructure` member is asserted. The selecting system and its work remain separate. Sharing a participant does not merge structures, and overlap does not prove parthood.

`CrossContextRelationStructure` is a provisional A.22-local designator for the conditional rule above. Until its crossing predicates and four identity discriminators are established, describe the proposed organization without claiming an admitted member. The label alone supplies no structure or crossing relation.

DDD `Context Mapping` names a repeatable way of constructing a Context Map; a `U.Method` claim uses A.3.1. When a mapping plan is needed, use A.15.2. An asserted dated mapping Work uses the complete admission grounds in §4.1; assignment-bound attribution additionally uses F.6.

C.2.1 identifies the resulting Context Map episteme independently. While crossing occurrences or the four structure discriminators are missing, its EntityOfConcern is the proposed or described organization. Once both are established, an episteme may designate the selected structure. It is additionally a `U.View` only when E.17.0 establishes `EpistemeViewpointConformanceRelation(E, P)`. Use C.29 for an unresolved mathematical correspondence or transfer question, and E.17/E.24.PUB for rendering or publication. These conditions preserve the source terms without merging the mapping, its product and the described organization.

#### A.22:4.1d - Transformation-flow structure network profile

Use `E.18.NET` when one engineering use selects two or more independently identified transformation-flow structures, or nested networks of them, together with obtaining relations across their boundaries. Apply the four A.22 discriminators: the TFS or nested-network members are the constituents; the cross-member relation occurrences satisfy their defining predicates and identity rules; the applied endpoint, boundary-exposure, and acyclic direct-member constraints are selected under E.18.NET; and the named network-use frame states the practical question, admissible action, and stop or return condition.

Any optional explanatory overread follows F.19:4 and remains outside structure identity. The return condition reopens selection when a member, relation, constraint, or use-frame value changes and is not a fifth identity discriminator. The result is one dependent, non-agentive `U.Structure` specialization. E.18.NET defines the network's detailed identity, reference, recursion, local-state, and conformance rules; A.22 does not copy those fields.

Use the first discriminator to record structure constituents. Introduce a separately re-identifiable world-side membership relation only when a receiving use needs it and can supply its participants, obtaining predicate, and identity rule.

#### A.22:4.9 - Resolve a reference to one selected structure

Use `SelectedStructureReference` when a description, view, transformation account, or architecture claim must refer to the same selected structure. It is a bounded C.3 kind of reference values and an A.6.5 `RefKind` for this use, not another durable public U-kind. Its target range is the `U.Structure` individuals identified in :4.1.

A candidate reference value is interpreted as `<R, d>`: one effective reference scheme and one designation value identified under that scheme. R supplies designation equality and the resolution Method. Designation d includes every registry snapshot/version, temporal qualifier or other input that selects its target under R. A time of inspection or freshness observation that does not select the target remains an evaluation condition. Successful resolutions of one fixed <R,d> must identify the same S; using a lookup basis that selects another target requires an explicit change to d or R.

The reference value remains the same when both components remain the same under those rules. Different reference values can resolve to the same structure; identical printed tokens under different schemes need not. A carrier, description episteme, diagram, or the structure itself is outside this reference-value domain.

The membership criterion requires R to resolve d to exactly one independently identified structure S with all four :4.1 discriminators. The receiving use fixes the declaration edition and C.3.2 judgment slice with explicit versions and a temporal selector. It evaluates resolution using the target-selecting pins already fixed in d under R; a time-independent resolution states that condition. A new assessment can leave the same reference unresolved when its fixed resolution grounds are unavailable, without selecting another target.

For an admissible reference candidate, established unique resolution to S satisfies the criterion; a completed resolution to no target, several targets, or an object outside the target range fails it. An unavailable resolution dependency or unsettled target identity leaves the judgment unknown. An uninterpretable candidate or an inapplicable slice is not-applicable under C.3.2.

In every case without established unique resolution, the structure-dependent use remains unresolved; no negative claim about a purported structure follows. The kind continues while this candidate interpretation and membership distinction remain unchanged.

A returned document can help recover S, but the reader must recover the structure it describes rather than use the document as S. Resolve the four discriminators before testing any additional receiving condition, such as model-use or transformation-flow specialization. Reference membership establishes neither that specialization nor a description, viewpoint, architecture, or reliance relation. A proposal lacking established structure identity remains proposal content under C.2.1.

Retargeting explicitly selects a new <R,d> by changing R or a target-selecting component of d, then repeats resolution and the affected receiving tests. A path whose current content describes a different organization cannot replace S. Preserve the earlier target and dependent conclusions; reopen only uses whose target or required basis changed. A changed carrier or notation can preserve both reference and target when R retains their meanings.

For example, two drawings can designate one pump-flow structure with the same constituents, obtaining connections, applied constraints and use frame. They may use different reference values while resolving to that same S. A new drawing that proposes a replacement connection is proposal content until its required structure basis is established; retaining the old file path does not retarget the earlier reference or make the proposed connection obtain. For a registry reference with d=(CoolingFlow, registry@v1, t1), choosing the same printed path under registry@v2 and t2 changes d and requires explicit selection of that new reference. If the v1 snapshot becomes unavailable, the earlier reference remains the same and its resolution judgment becomes unknown; v2 does not supply a replacement target for it.

#### A.22:4.2 - Structure claim reliance relation selection


When a structure claim relies on something beyond the selected structure, identify the reliance relation and apply the definition or test that supplies its participants and conditions. Use that definition for the relation's required fields and use limits.

| Reliance relation kind | What is named | Definition or test to apply |
| --- | --- | --- |
| Source-description relation | source episteme, source view, publication form or rendering where relevant, described structure or structure claim, source-basis pins or structure-use return condition, admissible use, and any grounded non-admissible use | `A.7` when nearby objects need distinguishing; `C.2.1` and `E.10.D2` for the episteme and describing use; `E.17.0` for claimed view membership; `A.6.3` for a source-to-receiving construction; `E.17` for a source-backed reader face; `E.24.PUB` and local rules for publication |
| Base-dependence or basedness | dependent and base, named direct predicate, and an optional C.2.1 assertion episteme; scope, time and evidence only when the relation or receiving use needs them; admissible use and any needed return condition | `A.6.6` for direct-relation recovery and optional assertion content; the subject-specific relation pattern supplies participant meanings, applicability, obtaining predicate and any needed occurrence identity |
| EntityOfConcern or empirical grounding | claim-bearing episteme, its EntityOfConcern, and effective ReferenceScheme; when empirical grounding is claimed, the grounding holon, covered claim subgraph, and obtaining C.2.1 `EpistemeEmpiricalGroundingRelation`; claim scope, optional model-use structure, describing-use viewpoint, reference plane, and observation or witness condition only when current | `C.2.1`, `A.2.6`, `A.1.1`, `E.17.0`, `A.6.4`, `A.6.3.RT`, and `A.6.6` only for a separate base-dependence claim |
| Evidence or witness reliance | the evidence-use relation and target claim; provenance, witness publication or observation record, time and currentness when the receiving use needs them; if an evidence graph is current, its graph path remains a mathematical or provenance expression rather than an action route | `A.2.4` for evidence-use classification; `A.10` when provenance or bounded reliance must remain recoverable; `G.6` when a citable evidence-provenance path is needed |
| Mathematical-lens reliance | the mathematical object and its correspondence to the named subject, the structure preserved or lost, and the use and stop conditions needed by the receiving claim; when C.29 is applied, retain its result and any output reference required by the receiving use | `C.29` when mathematical representation choice, transfer, or reliance remains unresolved; `C.26` only when a residual contextual-model obstruction calls for its quantum-like lens; `F.9` only for separately needed cross-context semantic correspondence; the named mathematical-lens pattern for its claims |
| Simulation, generated representation, model, or extracted trace | source episteme and publication when source availability matters, representation or extraction method, validation boundary, preserved structure, lost structure, and any structure-use return condition required by §4.5 | `C.29` when a mathematical representation-choice, transfer, or reliance question remains unresolved; `E.10.D2` and `E.17.0` for description and view claims; `E.17` and `E.24.PUB` for publication; `C.2.1` only for episteme identity or a claimed empirical-grounding relation; `A.10` for evidence; or the pattern that defines or tests the simulation, extraction, or validation claim |

If the required reliance relation remains unestablished, retain the usable source description or recognition cue with that limit. Do not create a generic reliance record to make the claim look resolved.

`U.Structure` does not carry description, representation, extraction, mathematical-lens, simulation, or generic reliance state as an internal structure field. Those are source-description, source-use, base-dependence, evidence, lens, extraction, simulation, or publication relations about a structure. `PublicationRef` is not an admissible substitute for the source episteme, source view, evidence relation, direct-relation assertion, or lens output.

#### A.22:4.3 - Structural descriptions and views

Structural descriptions use C.2.1 episteme identity; claimed view membership uses E.17.0. Every record whose name ends in `Description@Context` here designates an existing `U.Episteme`: C.2.1 supplies its identity and E.10.D2 constrains its describing use. Every record whose name ends in `View@Context` remains that same episteme and has `U.View` membership only when the E.17.0 conformance test to a viewpoint episteme passes. A.6.3 supplies only an optional source-to-receiving construction. The `@Context` suffix is a local retrieval convention; it does not add a context object or identity field.

In the description and view forms below, `admissibleUse` states the use and its limits. `nonAdmissibleUse?`, also named `groundedNonAdmissibleUse?`, carries one optional explanatory guard under F.19:4's plausible-reader test; the two names do not introduce separate fields.

```text
StructuralDescription@Context ::= {
  descriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  structureRefs: FinSet(SelectedStructureReference),
  structureClaimRelianceRefs?: FinSet(EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  describingEpistemeRef,
  admissibleUse,
  nonAdmissibleUse?
}

StructuralView@Context ::= {
  viewId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  structureRefs: FinSet(SelectedStructureReference),
  structuralAspectDescriptionRefs?,
  selectedRelationsOrOperations,
  hiddenOrLostStructure,
  admissibleUse,
  nonAdmissibleUse?
}
```

The EntityOfConcern and effective scheme identify the episteme with its claim content under C.2.1. `selectedViewpointRef`, when present, records that this named describing use selects viewpoint P; it does not establish conformance or `U.View` membership.

`selectedModelUseStructureRef`, when present, resolves one independently selected `BoundedModelUseStructure` used by the receiving assertion or calculation; it is neither episteme identity nor another viewpoint field.

When reliance is on a named claim, `U.EpistemeRef` resolves the C.2.1 claim-bearing episteme; a PatternID normally locates the definition, constraint, or test it uses, and a ClaimGraph is added only when that identity changes the use.

#### A.22:4.3a - Orientation belongs to a representation of a named structure

Use *vertical*, *horizontal*, *above*, *below*, or *at the same level* as structural shorthand only when the reader can recover **which object's structure is represented, which relation is shown, and how the drawing or ordering convention represents it**. These words can make an explanation easier to follow. Their useful content comes from the named structure and convention.

For example, a diagram of a Method's composition may place encompassing Methods above their constituents and draw each established `methodPartOf` connection upward. A diagram of result use may place a supplying Method to the left of a receiving Method. The second diagram needs to state what result is used and under what conditions; its horizontal arrow supplies no parthood claim. Rotating either diagram changes its orientation, not those relations. Conversely, two boxes at the same height need not denote peers, independent participants, objects of one kind, or simultaneous work.

Recover the relation before choosing an axis:

| Represented subject and question | What gives the orientation meaning |
| --- | --- |
| A System or Method and its constituents | The whole–part relation and its independently established participants; nesting or height alone supplies neither. |
| Kinds, concepts, or Methods ordered by generality | The declared classification, inclusion, subsumption, or refinement relation and its direction. This is a different structure from composition. |
| Actions, result uses, or possible continuations | The named order, dependency, guard, overlap, or return relation. Several relation kinds may require different arrow labels in one picture. |
| Systems, resources, or performed work in space | Their placement, adjacency, or spatial relation in the stated reference frame. Literal vertical and horizontal directions remain spatial claims about these participants. |

A holon can participate in several structures, each with its relevant relations and constraints. A family of holons drawn as a hierarchy need not be one tree. Calling a representation a *lattice* requires the mathematical claim used: a specified order, the requisite meets and joins, and a justified correspondence to the represented subject. Use C.29 when a mathematical representation-choice, transfer, or reliance question remains unresolved. A branching picture or the presence of several encompassing wholes establishes none of these properties.

For a first explanation, a sentence such as “in this diagram of Method composition, upward arrows connect a constituent to its encompassing Method” is sufficient when the relations are already clear. Add a separate structure, view, or mathematical account only when the intended use needs it. C.30.ASV:4.5a develops the selection of structures for Methods; C.30.STRAT recovers an unresolved architecture label.

#### A.22:4.4 - Extracted and transformed structural views

Recover the extraction or transformation basis when a view of structure is obtained from a corpus, trace, model, simulation, or generated representation, through a mathematical lens or coarsening pass, or within an observer or budget boundary, and may hide distinctions.

```text
ExtractedStructuralView@Context ::= {
  extractedViewId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  sourceCorpusOrTraceRefs,
  structureRefs: FinSet(SelectedStructureReference),
  extractionDescriptionRef,
  preservedStructure,
  lostStructure,
  validationBoundary,
  structureUseReturnCondition?,
  admissibleUse,
  nonAdmissibleUse?
}

StructureExtractionDescription@Context ::= {
  extractionDescriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  sourceInputKind,
  lensOrMethodRef,
  budgetOrObserverBoundary?,
  preservedStructureKinds,
  lostStructureKinds,
  validationBoundary,
  structureUseReturnCondition?,
  admissibleUse,
  nonAdmissibleUse?
}

StructuralAspectDescription@Context ::= {
  aspectDescriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  aspectKindRef,
  structureRefs: FinSet(SelectedStructureReference),
  structureClaimRelianceRefs?: FinSet(EvidenceRelationRef | EvidenceProvenanceRelationRef | MathLensUseOutputRef | StructureUseReturnConditionRef | U.EpistemeRef),
  admissibleUse,
  nonAdmissibleUse?
}

StructuralCoarseningDescription@Context ::= {
  coarseningDescriptionId,
  entityOfConcernRef,
  effectiveReferenceScheme,
  selectedViewpointRef?,
  selectedModelUseStructureRef?,
  sourceStructureRefs: FinSet(SelectedStructureReference),
  resultStructureRefs: FinSet(SelectedStructureReference),
  preservedUnder,
  brokenBy,
  lostStructure,
  structureUseReturnCondition?,
  admissibleUse,
  nonAdmissibleUse?
}
```

#### A.22:4.5 - Structure-use return

`StructureUseReturnCondition` states when to return to the fuller basis because an extracted, coarsened or reused account hides a distinction needed by the receiving action or judgement. Name the hidden distinction, the use that needs it, and the condition that requires returning before that use proceeds.

Do not make structure-use return mandatory for ordinary local recognition when no hidden distinction is being used for action.

#### A.22:4.6 - Relation to architecture
`StructuralAspectDescription@Context` describes one selected structural aspect under A.22. It is not an `ArchitectureStructureKindRef` by itself. `ArchitectureStructuralView@Context` is a C.30.ASV view over the architecture claim or selected architecture-relevant structures. An asserted architecture relation is an independently obtaining C.30 `ArchitectureRelation` between a holon and a selected structure.

A.22 is upstream of C.30. Architecture uses structure; structure does not import architecture as a parent.

`C.30` uses A.22 to identify one selected architecture-relevant structure, then tests the `ArchitectureRelation` between that structure and one holon. `C.30.ASV` separately defines and tests an architecture structural view. A reference from an architecture description establishes neither the relation nor view conformance.

C.30 and its subpatterns supply the architecture-specific description, view and adequacy rules. Select the one that defines or tests the architecture claim.

#### A.22:4.7 - Boundary and repair table

| Tempting collapse | A.22 repair |
| --- | --- |
| The reliance relation is treated as the structure. | Recover the constituents, selected obtaining relation occurrences, applied constraints, and named use frame. When a neighboring source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance claim is current, name that relation and the content that defines or tests it separately. |
| The diagram, graph, table, dashboard, or publication form is the structure. | Recover the description or view and its publication occurrence, form, or carrier when relevant. If the account claims a source-description, base-dependence, grounding, evidence, lens, simulation, extraction, or representation relation, identify and test that relation separately. |
| A transformation-flow graph expression is the structure in every sense. | Use `E.18` for one selected TFS and its internal paths, crossings, and valuations; use `E.18.NET` for a selected network of independently identified TFS members and cross-member relations; use `E.18.2` for the graph expression and `C.29` only when a mathematical representation-choice, transfer, or reliance question remains unresolved. A.22 supplies only the selected-structure identity, and `C.30.TFS-REL` defines and tests the architecture-to-transformation-flow relation claim. |
| A mathematical lens output is the structure. | Use `C.29` for lens-use result and admissibility, and cite `MathLensUseOutputRef` only through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| A structure is cited as sufficient basis for evidence reliance, assurance, safety, causality, or gate passage. | Use `A.10` for claim-bound evidence reliance, `G.6` when a citable evidence-provenance path is needed, `B.3` for a named assurance claim, the safety pattern for safety, `C.28` for causal use, `A.20` for internal-constraint validity, and `A.21` for a gate decision. |
| A structure is a decision or work record. | Use `C.11` or the project-side decision pattern for the decision, `A.15` for the work-family object, and `C.2.1` for an episteme describing it. `A.20` or `A.21` applies only when an internal-constraint result or gate decision is at issue. |
| Architecture is treated as identical to a selected structure. | Use `C.30` to test the `ArchitectureRelation` between the holon and selected structure. Recover the architecture claim and any description or view separately. |
| Function, module, interface, platform, layer, stack, block, expert, cache, router, or gate becomes a root kind by appearing in structure prose. | Use `C.30.STRAT` for an ambiguous source label, then the definition or test required by the recovered claim: `A.6.F` for function, `A.6.M` for a module-interface relation, `A.6.0` for a signature, `A.6.5` for relation slots, `A.6.B` for boundary norms, `A.6.C` for contract unpacking, `A.6.P:4.11a` for service or access wording, `E.18` for transformation-flow structure, or `C.30.ASV` for an architecture structural view. Apply any other pattern only for the claim it defines or tests. |

#### A.22:4.8 - Worked slices

**Maintenance-isolation structure selection.** In this constructed case, a planner chooses which relations matter for planning pump-skid isolation. Under the project’s independently tested installation predicates, Motor_12 drives Pump_37, Bus_7 supplies Motor_12, and Valve_In_4 and Valve_Out_4 lie on the inlet and outlet material paths of Pump_37. Assume these are the complete live energy and material paths for this illustration.

```text
named selection use: choose isolation points before Pump_37 maintenance
constituents: independently identified Pump_37, Motor_12, Valve_In_4, Valve_Out_4, and Bus_7
selected obtaining relations: the established drive, supply, inlet-path, and outlet-path occurrences with the participants named above
applied constraints: isolate every live energy and material path to Pump_37; retain only relations relevant to this isolation use
selecting system: MaintenancePlanner_A
selection method: IsolationStructureSelectionMethod
selected structure: Pump37_MaintenanceIsolationStructure
admissible action: prepare the isolation sequence from the selected paths
stop: reopen selection when a constituent, selected occurrence, or isolation constraint changes
```

`Pump37_MaintenanceIsolationStructure` is identified by the constituents, selected obtaining occurrences, applied isolation constraints, and maintenance-isolation use frame. The selection method and any C.2.1 episteme describing the judgment remain separate.

The selected organization directs planning to Bus_7 and both material-path valves; it establishes no completed isolation. If the completeness assumption fails, return to path identification before planning from this selection.

A C.29 graph may represent the same organization, while the predicates of the selected relation occurrences remain its obtaining basis. A visually identical graph with an unestablished connection remains a representation candidate.

**Architecture kernel slice.** A team says, "the architecture is the graph." Recover the selected structure and the graph's reliance relation:

```text
declaredStructureSubstrateRef: TransformationFlowStructureRef under E.18, with mathematical graph description under E.18.2 when that expression is the current claim
candidate structure: selected transformation-flow structure
structure-claim reliance relation: selected relation record named by value(
  sourceDescriptionOrPatternApplicationRef = SourceViewRef, structure or crossing record selected under E.18, or E.18.2 mathematical graph description,
  relationContribution = E.18 selected-structure or crossing definition | A.6.6 base-dependence test | independently established support relation recovered through A.10 provenance and bounded-use account | C.29 mathematical-lens result, chosen for the claim being made,
  relationKind = source-description | base-dependence | evidence | lens, selected for this reliance,
  validationBoundary = graph-path currentness boundary, slice currentness boundary, or crossing currentness boundary
)
next FPF pattern application: C.30.TFS-REL when this selected structure is used in an architecture-to-transformation-flow relation
stop or return condition: stop at the selected reliance relation's result; for a Work, evidence, gate, or decision claim, apply its test in A.22:4.7
non-admissible use: the graph as the whole architecture
```

The practitioner can now use the graph through the selected source-description, base-dependence, evidence, or lens relation and route the architecture claim to C.30.TFS-REL.

**Extracted code structure slice.** A code-agent relation graph or probe JSON reports imports, calls, registry wiring and data-flow links. Recover the source codebase or publication, extraction method, preserved and lost structure, validation boundary and structure-use return condition. That establishes the declared extraction result only. For an A.6.3 epistemic-viewing claim, identify source episteme `X` and receiving episteme `Y`, their same EntityOfConcern, and the projected or re-expressed ClaimGraph and ReferenceScheme. Qualify `Y` as a `U.View` only when the applicable E.17.0 viewpoint conformance independently obtains. A claim about the codebase architecture, internal agent belief, assurance or release readiness still needs its evidence and governing predicate.

```text
ExtractedStructuralView@Context:
  sourceCorpusOrTraceRefs: repo snapshot, probe outputs, traces
  preservedStructure: selected typed relation families
  lostStructure: unexplored regions, dynamic calls, hidden generated code, ambiguous relation kinds
  validationBoundary: probe coverage and source codebase or publication edition
  structureUseReturnCondition: when an architecture decision, assurance use, or repair depends on a relation not observed by the extraction
```

### A.22:5 - Archetypal Grounding

| Tell-Show-Show row | Grounding |
| --- | --- |
| Tell | A practitioner sees an arrangement that matters but does not yet know whether it is a diagram, a model, a graph, an architecture claim, a source description, base-dependence relation, evidence relation, lens relation, or decision. A.22 asks first: which constituents and obtaining relations are selected, under which applied constraints and named use frame, and what loss changes the next action? |
| Show: `U.System` | In a plant, vehicle, software system, or neural-network model, the selected structure may be transformation-flow, control, module-interface structure, placement, information, scale, or declared logical structure. The structure record does not become the system and does not prove that the system is safe, maintainable, or ready. |
| Show: `U.Episteme` | A paper, model, generated relation graph, dashboard, architecture note, or mathematical-lens output may describe or present a description of selected structure. A selected-structure claim may rely on that description through a source-description relation or an A.6.6 base-dependence relation. The episteme, view, and publication remain separate from the structure and from each relied-on relation; name that relation and any validation boundary required by its definition or intended use; add a structure-use return condition when §4.5 requires it. |

### A.22:6 - Bias-Annotation

| Bias risk | Mitigation |
| --- | --- |
| Architecture bias | Do not make architecture the parent of all structure. A.22 stays upstream; C.30 carries grounded architecture and selected-structure adequacy. |
| Mathematical-formalism bias | A mathematical lens can expose preserved structure and lost structure, but C.29 still defines the lens-use result, admissibility, and stop condition. |
| Diagram bias | A useful diagram or generated relation graph is attractive enough to be mistaken for the structure. Description, specification-use, and publication boundaries stay explicit. |
| Review-only bias | A check returns the supported recognition, conclusion or action needed for the receiving use. Repair a defect when the check exposes one. |

Use the checklist to inspect the selected structure claim and only the neighboring claims made.

### A.22:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-A22-1 Base identity.** | The selected `U.Structure` is recoverable from independently identified constituents, selected obtaining relation occurrences, constraints as applied, and one named selection-use frame. | Recover the missing discriminator. If a constituent lacks its defining identity content or a relation lacks its predicate or occurrence rule, stop at that blocker rather than naming a structure from a graph or record. |
| **CC-A22-1a Independent grounding.** | Every constituent and selected relation occurrence keeps its identity; a collection, constraint episteme, graph, table, description, view, or publication neither creates them nor makes a relation obtain. | Apply the constituent and relation patterns first; treat the visible artifact as a C.29 representation or C.2.1 episteme only when that is what is present. |
| **CC-A22-1b Selection work and result separation.** | When dated selection Work is asserted, establish the complete A.13 core and A.15.1 admission in §4.1 and the method-enactment relation. Establish any direct participation or A.6.1 binding relation needed by the receiving claim separately. Any durable result is a separate C.2.1 episteme, and any accountable choice uses its decision predicate and test. | Name the acting system, method and work separately from structure identity; identify any binding, result or decision needed by the current claim under its grounds. |
| **CC-A22-1c Reidentification.** | A changed designator, method, work, result episteme, graph, description, or publication leaves the structure unchanged when all four identity discriminators remain unchanged; a changed discriminator reopens identity. | Compare the four discriminators and apply each selected relation occurrence's identity rule before reapplying A.22. |
| **CC-A22-1d Transformation-flow network profile.** | An E.18.NET value applies all four A.22 discriminators to TFS or nested-network constituents, cross-member relation occurrences satisfying their predicates, the E.18.NET constraints as applied, and one named network-use frame. A constituent row supplies no generic membership occurrence, and A.22 carries no duplicate network fields. | Recover any missing member, relation predicate, or identity rule, then apply E.18.NET. If a separate membership relation is needed, state its participants and apply its predicate rather than inferring it from the constituent list or graph. |
| **CC-A22-2 Non-agentive structure.** | Any claimed action has a recoverable capable actor. Use F.19:4 to test literal or metonymic action wording; apply the relevant proof, decision, warrant, or adaptation predicate when that claim is current. | Recover the actor and action; identify System and Work only when the claim needs their identity. For another claim, use the pattern that defines or tests its result. |
| **CC-A22-3 Structure-claim reliance relation boundary.** | When source-description, source-use, base-dependence, grounding, evidence, lens, simulation, extraction, or representation reliance is claimed, name the relation and the definition or test used for it. | Add the relation kind, definition or test, admissible use, and any validation boundary or stop condition required by that relation or receiving use. Add a structure-use return condition when §4.5 requires it. Test any optional non-admissible use through F.19:4. If no admissible reliance is established, mark the reliance phrase as carrying no admissible reliance. |
| **CC-A22-4 Description and view separation.** | A structural description, structural view, extracted view, diagram, table, graph, dashboard, or publication face is not treated as the structure itself. | Recover any description or view and its publication form or occurrence; resolve any source-description relation or A.6.6 base declaration separately. Name the selected structure separately only if selected organization is being claimed. |
| **CC-A22-5 Describing-use separation.** | Description epistemes keep claim content, EntityOfConcern, and effective scheme under C.2.1. A named describing use may separately select one viewpoint, and a receiving calculation or assertion may separately select one independently identified `BoundedModelUseStructure`. E.17.0 alone supplies the `U.View` conformance test; A.6.3 supplies optional viewing construction. | Remove any compound context field; state only the episteme values and the optional use selections that the current action needs. |
| **CC-A22-6 Structure-use return.** | `StructureUseReturnCondition` is present when hidden selected-structure, source-basis, source-description, evidence, lens, simulation, extraction, or representation distinctions are used for action, assurance, causal use, legal or regulatory review, comparison, or decision reopening. | Add one structure-use return condition or narrow the record's admissible use so the hidden distinction is not relied on. |
| **CC-A22-7 Non-structure claim kind.** | Evidence, assurance, gate, release, causal, dynamics, measurement, work, decision, publication, bridge, and mathematical-lens claims use the patterns that define or test those claims. | The check passes when that contribution and the claim kind are named, while the A.22 record remains limited to selected-structure use. |
| **CC-A22-8 Architecture pattern application.** | Architecture claims use `C.30` and `ArchitectureRelation`; A.22 does not treat architecture as a root kind or define C.30-specific records. | Apply C.30 or a C.30 subpattern and keep A.22 only as the selected-structure EntityOfConcern and structure-claim reliance relation. |
| **CC-A22-9 Plain and Tech recovery.** | Plain structure phrases may remain, but if they carry ontological, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim, the relevant Tech fields and FPF pattern applications are recoverable. | Add the missing Tech fields or demote the Plain phrase to ordinary recognition wording. |
| **CC-A22-10 Useful action.** | The repair preserves the supported recognition, understanding, decision or action the practitioner needs. | Restore the information or action required by that use. If the wording cannot support it, use `E.10:17` to name any remaining use as a cue or quotation, identify a blocked transfer, or say that the rewrite is unfinished. |
| **CC-A22-11 CGUS qualification and case use.** | A formal CGUS qualification identifies one A.22 structure by the four discriminators; its local locus bindings, selected relations, and applied constraints define at least two potential continuations. The present-case result, any description, and every stronger neighboring claim are judged separately. | Use `A.22.CGUS`'s ordinary branch to clarify available alternatives and their conditions. Use formal qualification when the named use depends on structure identity or CGUS membership. If the structure qualifies but case facts are missing, return `unknown` for the affected alternatives. If only a display is present, keep it as an explanation; send description adequacy and stronger claims to their patterns. |

### A.22:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-document** | A diagram, table, dashboard, relation graph, or prose section is called the structure. | Recover publication, publication-form, description, or view relation; name the structure separately only when selected organization is being claimed. |
| **Reliance-interpretation-as-structure** | A trace used as source basis, benchmark, lens output, model, or simulation is treated as the structure. | Name the A.6.6, source-description, evidence, or lens relation and its definition or test; state the validation and stop conditions required by that relation or intended use, and add a structure-use return condition when §4.5 requires it. Use F.19:4 for any optional explanatory guard. |
| **Loss-free extraction** | An extracted or coarsened account hides a loss that changes the receiving use. | State what is preserved and lost, the supported use and any required validation boundary. Add a structure-use return condition under §4.5 or narrow the use so the hidden distinction is not relied on. |
| **Architecture root-kind rebound** | Structure work reintroduces `U.Architecture` or treats architecture as parallel to structure. | Use `ArchitectureRelation` and C.30; keep A.22 as the upstream selected-structure EntityOfConcern. |
| **Lens ontology import** | A mathematical lens output becomes the imported ontology. | Use C.29 for the lens, cite it through C.29 lens-use result, preserved structure, lost structure, and stop-condition discipline. |
| **Sterile precision rewrite** | The text removes overread but no longer tells the practitioner what to do. | Restore the information and any action still needed for the practitioner's receiving question. |

### A.22:9 - Consequences

| Benefit | Cost or trade-off |
| --- | --- |
| FPF gains a reusable selected-structure EntityOfConcern without minting architecture, module, interface, platform, or graph as root kinds. | A conforming use recovers the four structure-identity discriminators, including the question, admissible action and stop or return condition in the named use frame. Extraction, coarsening and reliance claims also retain the preservation, loss, validation and structure-use return information required by their receiving use. |
| Structural views become usable without confusing the view, publication form, publication, source-use relation, grounding relation, and selected structure EntityOfConcern. | Existing loose prose that says "the structure is the diagram" needs repair. |
| Structure claims can rely on C.29 mathematical-lens results or E.18 transformation-flow structures through separately established relations, without treating them as the general structure ontology. | FPF pattern applications are named when evidence, assurance, causal-use, gate, work, or decision claims are being made. |
| Architecture work can start from selected structure through C.30 instead of forcing architecture to be either a document or a module diagram. | Architecture-specific conformance stays outside A.22, so practitioners can require one extra C.30 application when the architecture claim or durable architecture-description use is being made. |

### A.22:10 - Rationale

FPF needs one general selected-structure kind because many useful claims depend on organization before they depend on an architecture, mathematical, measurement, or publication pattern. The selected structure is dependent and non-agentive. Claims about it are carried by separate epistemes and views: it can be described, sourced, compared, coarsened, extracted, or used by architecture.

A practitioner can state the four identity values and stop when they answer the receiving question. `StructureQuestionCard@Project` is one optional aid. Heavier describing-use viewpoint selection, independently selected model-use structure, A.6.6 base-dependence, extraction, lens, evidence, and structure-use return records are used only when the next use would otherwise hide loss, source-basis dependence, or a non-structure claim kind.

C.30 defines the `ArchitectureRelation` between one holon and one selected A.22 structure. An architecture claim states whether that relation obtains, or describes candidate or expected structure. Architecture descriptions and views are epistemes; publication makes them available. A.22 supplies the selected structure and its identity basis.

### A.22:11 - SoTA-Echoing

| Practice or source anchor | FPF adoption | Action consequence | Boundary |
| --- | --- | --- | --- |
| FPF `C.2.1` and `E.10.D2` description discipline, `E.17.0` view membership, `A.6.3` construction, and `E.17`/`E.24.PUB` publication discipline | FPF separates EntityOfConcern, effective reference scheme, viewpoint, grounding holon, view, publication, rendering, and carrier. | A.22 structural descriptions and views reuse those relations rather than inventing a local display ontology or mandatory context field. | A description or view does not become the selected structure and supplies no evidence, assurance, gate, or decision authority by form. |
| Evans, [Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/), 2026 | The cited DDD case motivates distinguishing model-use boundaries and their relationships from the Context Map used to inspect them; the FPF identities are an adaptation. | A.22 admits the `BoundedModelUseStructure` membership condition and the conditional `CrossContextRelationStructure` membership condition; the latter has no positive member until independently defined crossing occurrences and all four base discriminators exist. A mapping Method and any dated Work use their admission grounds; the product is a C.2.1 episteme concerning a proposed organization until a structure can be designated; it becomes `U.View` only under E.17.0 conformance. | The DDD terms do not turn a system part, method, proposal, structure, view, and diagram into one object. |
| C.29 mathematical-lens discipline | Adopt preserved structure, lost structure, lens-use admissibility, and stop-condition discipline when a mathematical lens is used for a structure claim. | Cite C.29 output through C.29 lens-use result, preserved structure, lost structure, stop condition, and structure-use return discipline. | The lens output remains separate from the selected structure. Its evidential use, any assurance or causal-use claim, and any decision need their grounds. |
| [arXiv:2603.00601](https://arxiv.org/abs/2603.00601) code-space architecture relation-graph work and related code-probing practice | Adapt partial-observability, typed-relation, uncertainty, and structure-use return pressure for extracted structural views. | State the extraction basis, its validation boundary and, where needed, whether a relation is `observed`, `inferred`, or `unknown`. Add a structure-use return condition when §4.5 requires it. | Do not mint `U.CodeSpace`. Probe and benchmark outputs may contribute evidence under an established evidence-use relation; their presence alone does not establish structure adequacy, assurance or release readiness. |
| Coarsening, compression, and RG-adjacent traditions | Adopt the need to say what structure is preserved and what is lost. | Use `StructuralCoarseningDescription@Context` when the receiving use needs that account; add `StructureUseReturnCondition` when §4.5 requires it. | For RG, epiplexity, structural information, or equivalence reasoning, use C.29, C.16, or the cited pattern that defines or tests the claim. |
| GonzoML neural-network architecture discussions as practitioner-language intake | Adapt block replacement, dataflow change, memory placement, cache placement, path-selection, pruning, distillation, and architecture-search wording as general architecture-operation recognition material. | Keep the source's local terms when their meaning is clear. Use `C.30.STRAT` when a label leaves the claimed object or relation unresolved. Recover the selected or proposed organization, and any further relation, only when the current claim needs it. | Neural-network labels, benchmark results, ablations, or pruning masks do not become structure ontology, architecture decisions, evidence sufficiency, gate passage, assurance, or architecture adequacy by themselves. |

**How can an orientation cue preserve a structural claim across different diagrams?** §4.3a uses the named subject, relation and representation convention. The default is to read height, nesting or direction as one common relation across holons, kinds and activities. That reading fails when the same Method is shown inside one composition and beside a Method using its result. The FPF construction retains each claim when the drawing rotates or changes layout, at the cost of naming the relation once. [OMG Essence 2.0 beta 2, Figure 7.1](https://www.omg.org/spec/Essence/2.0/Beta2/PDF) is a positive comparator: its vertically arranged boxes already have differently labelled relations for composition, description and definition. **Adopt** that relation-sensitive reading; the figure does not establish FPF parthood or a universal holon lattice.

### A.22:12 - Relations

Builds on: `A.1`, `C.13`, `C.2.1`, `A.6.REL`, `A.6.0`, `A.6.5`, `A.3.1`, `A.6.1`, `A.15.1`, `A.6.P`, `A.7`, `A.6.2`, `A.6.3`, `A.14`, `C.16`, `C.29`, `E.10.D2`, `E.10`, `C.2.P`, `E.17.0`, `E.17.1`, `E.24`, `E.24.PUB`, and `F.18`.

Coordinates with: `A.1.1`, `A.2.6`, `A.22.CGUS`, `C.30.P`, `C.30.STRAT`, `C.30`, `C.30.ASV`, `C.30.TFS-REL`, `C.30.LCA`, `C.30.ILC`, `A.6.F`, `E.18`, `E.18.NET`, `E.18.3`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `C.28`, `A.15`, `C.11`, `C.16`, `C.25`, `G.5`, `C.33`, `C.34`, and `C.35` when architecture-specific structure-capture, preservation, or discovery adequacy claim kinds are being made.

Architecture-specific adequacy: `C.33`, `C.34`, and `C.35` define or test architecture-specific capture, preservation, and discovery adequacy over selected structures. A.22 keeps the general selected-structure portion; it does not decide architecture use, candidate admission, measurement, evidence, assurance, or decision authority for those adequacy claims.

Does not replace: `C.30.P` or `C.30.STRAT` wording-use precision restoration, `C.30` for grounded architecture adequacy and conditional architecture-description use, `C.29` for mathematical-lens use, `C.16` for measurement and characterization, `C.28` for causal-use relation, `B.3` for assurance, `A.10` for claim-bound evidence reliance, `G.6` for citable evidence-provenance paths, `A.20` for internal-constraint validity, `A.21` for gate decisions, the subject pattern for release claims, `A.15` for work-family objects, `C.11` for decisions, `E.17` for a source-backed reader face, or `E.24.PUB` for publication occurrence, form, carrier, audience, bounded use, and availability.

Use `F.19` for ordinary precise-plain-language repair and its plausible-reader test for optional guards; unresolved structure or architecture wording follows `C.30.P` or `C.30.STRAT`.


### A.22:End
