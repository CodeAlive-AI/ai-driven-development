## A.3.4 - U.Transformation: Bounded Change Under Conditions

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative except where a section is explicitly informative

### A.3.4:0 - Use This When

Use this pattern when a project needs to identify an **actual bounded change** itself: which exact governed referent changed, over which extent or ordered boundary, under which boundary conditions, and which actual subject facts make the before-to-after difference one occurrence of change.

Use it when the working question is:

- what exact entity, structure, episteme, characteristic-bearing referent, or formal object changed;
- which actual characteristic-state and direct-relation facts differ across the boundary;
- what temporal extent, formal ordering, or continuity rule identifies this occurrence;
- whether method, planned work, performed work, mechanism, flow structure, representation, evidence, publication, or a later receiving use is also current and therefore needs its own direct relation.

**Primary EntityOfConcern.** One exact `U.Transformation`: an independently identified actual bounded change. A task, method, plan, desired state, work occurrence, operation family, morphism, predicate, delta formula, trace, assertion, obtaining relation occurrence, before-and-after picture, or result record establishes neither that change nor its identity. Such objects can describe, plan, enact, constrain, represent, support, or use a transformation only through their own governed relations.

**Primary working reader.** A practitioner or modeler who must identify one actual change for a current engineering, scientific, formal, documentary, or architectural use before relating it to method, work, flow, evidence, or production. The heavier composition and admission branch additionally addresses an FPF author or reviewer only when that practitioner use needs positive transformation-part or holon claims.

**First useful move.** Name the exact changed referent and the actual boundary across which it changed. Recover the actual pre-boundary, during-boundary, and post-boundary subject facts under their direct patterns. State the temporal extent or formal ordering and the boundary conditions that delimit the occurrence. If the available material is only a desired state, method, plan, model, trace, or assertion, stop: the actual `U.Transformation` has not yet been grounded.

**Open-world guard.** Failure to recover a method, work occurrence, evidence item, publication, delivery, acceptance, or receiving-use relation proves none of those absent. It only blocks or lowers the claim that depends on that exact relation. Conversely, their presence does not establish that an actual transformation occurred.

**What goes wrong if missed.** Method names become change proof, work traces become laws, process diagrams become execution, dynamics models become permission, temporal trends become intervention claims, mathematical constructions become project-world work, and publications or result records are treated as the change itself.

**What this buys.** A practitioner can identify one actual bounded change at the resolution needed by the current use without settling whether finer parts obtain; that identification establishes neither parthood nor partlessness. Exact transformation composition is grounded only when needed, and only a grounded composite is tested against A.1. Method, work, flow, representation, evidence, publication, production, and receiving-use claims remain with their direct governors.
**Not this pattern when.**

- If the issue is only a semantic way of doing, use `A.3.1`.
- If the issue is a description of that way, use `A.3.2`.
- If the issue is a state-space and transition-law episteme, use `A.3.3`.
- If the issue is a law-governed operation algebra with admissibility predicates, use `A.6.1` and `E.20`.
- If the issue is planned or dated work, use `A.15.2` or `A.15.1`.
- If the issue is the selected compound transformation-flow structure, its locus, path, path slice, crossing, or flow valuation, use `E.18`.
- If the issue is a graph, algebra, category, tuple, morphism, quotient, fold, refinement, factorization, or wiring expression used to describe that structure mathematically, use `E.18.2` and `C.29`.
- If the issue is a positive temporal aspect of an object or claim, use `C.27.TA`.
- If the issue is adequacy or admissible use of a temporal claim, use `C.27`.
- If the issue is holon recognition without a current actual-change identity or constructive transformation-parthood claim, use `A.1`.

### A.3.4:1 - Problem Frame

FPF often needs to talk about change in physical systems, engineered artifacts, organizations, epistemes, documents, architectures, programs, regulatory situations, and research objects. The same source phrase may say "algorithm", "process", "workflow", "procedure", "mechanism", "run", "trajectory", "transition", "stabilization", "editing", "migration", "optimization", "morphism", "construction", or another field-specific name for a change, transformer, or change structure.

Those phrases are not enough to recover the object under concern. A CRISPR editing protocol, a nuclear-plant operating change, a platform refactoring, a model update, a document repair, an architecture move, a proof construction, and a method-result carry-through can all involve transformation, but the FPF values under use differ.

FPF already has strong neighboring patterns:

- `A.3` for transformer constitution: acting system bearing `TransformerRole`, method description, method, and actual work;
- `A.3.1` for `U.Method`;

- `A.3.2` for `U.MethodDescription`;
- `A.3.3` for `U.Dynamics`;
- `A.6.0` and `A.6.5` for signatures and slot discipline;
- `A.6.1` and `E.20` for mechanisms;
- `A.15.2` and `A.15.1` for work plans and dated work;
- `E.18` for transformation-flow structures;
- `E.18.2` for mathematical descriptions of transformation-flow structures;
- `E.18.1` for problem-to-work carry-through;
- `C.27.TA` for positive temporal aspects;
- `C.27` for temporal-claim adequacy;
- `C.29` for mathematical-lens use;
- evidence, gate, assurance, source, result, decision, and publication patterns for their own claims.

What is missing is a positive way to identify the actual bounded change first and then recover each neighboring object through its own direct relation, without turning a checklist or description into the transformation ontology.

### A.3.4:2 - Problem

Without `U.Transformation`, projects repeatedly make category errors:

1. **Method as transformation.** A way of doing is treated as if the change already happened or must happen.
2. **Mechanism as transformation.** A law-governed operation algebra is treated as the actual or intended change, rather than as one governing value for a transformation.
3. **Work as transformation law.** A dated work occurrence or trace is treated as if it defined the reusable transformation.
4. **Dynamics as permission.** A state-space or transition-law episteme is used as if it authorized action, gate passage, or result acceptance.
5. **Temporal claim as transformation.** A claim about rate, rhythm, recovery, delay, effort, inertia, freshness, or validity window is used as if it specified the whole change and its conditions.
6. **Formal construction as project-world work.** A morphism, proof construction, or formal transformation inside a mathematical substrate is treated as a physical or organizational change without a realization or work relation.
7. **Publication as transformation.** A report, dashboard, diagram, source span, or published specification is treated as if it were the changed object or the change event.

These errors are expensive because the wrong neighboring pattern then receives the claim. The project may seek evidence for a method when it needs a work trace, compare dynamics models when it needs a transformation boundary, or invoke temporal-claim adequacy when the real problem is the missing transformation relation.

### A.3.4:3 - Forces

| Force | Tension |
| --- | --- |
| Generality and specificity | One subject-side identification method spans physical, biological, software, organizational, documentary, architectural, formal, and epistemic changes while preserving their direct domain governors and without reducing them to software algorithms. |
| Possible, planned, actual, modeled, and claimed transformation | Source language can present change as possible, planned, enacted, observed, modeled, claimed, or published. Only an independently grounded actual subject-side occurrence qualifies as `U.Transformation`; possibility, plan, work, observation or evidence, model, assertion, and publication claims remain separately governed. |
| Neighboring value competition | Methods, mechanisms, dynamics, work, temporal aspects, evidence, and results all look like "the thing that changes things". Their objects retain the kinds and relations assigned by their direct governing patterns. |
| Time and order | Many transformations need a time window, cadence, duration, ordering relation, or refresh condition, but time wording alone does not define the transformation. |
| Mathematical strength and practical use | Formal task, morphism, state-space, constructor-theory, or dynamics language can make transformations precise, while practical permission, evidence, work, and responsibility stay with their governing patterns. |

### A.3.4:4 - Solution

#### A.3.4:4.1 - Identify the actual bounded change

`U.Transformation` is the FPF ontic for one actual bounded change. Identify one occurrence from the smallest subject-side basis that distinguishes it:

1. **Changed referent.** Identify the exact entity, structure, episteme, characteristic-bearing referent, or formal object under its direct pattern.
2. **Extent and boundary.** State the exact temporal extent of the change, including only gaps admitted by its continuity rule, or the exact ordering boundary in a declared formal substrate.
3. **Boundary conditions.** State the conditions that delimit this change from adjacent persistence, work, or change occurrences.
4. **Actual change facts.** Recover exact characteristic-state facts and obtaining direct relations before, during, and after the boundary. These facts, not a verbal change label, establish what changed.
5. **Continuity or reidentification.** When internal variation, interruption, or composition can occur, state the governed rule under which this remains one transformation.

Here, **one** means one occurrence at the resolution, referent, extent, and boundary required by the current use. It does not mean elementary, atomic, indivisible, or partless. Later refinement or a future governed constructive-part claim can coexist with the present identification. Sampling or temporal subdivision alone establishes neither constructive transformation parthood nor absence of transformation parts.

Generic, possible, desired, intended, planned, predicted, modeled, asserted, and published change claims remain claim content of epistemes, methods, work plans, dynamics models, publications, or other use-side objects under their direct patterns. They identify no actual `U.Transformation` until the subject-side occurrence basis obtains. A formal transformation can be actual relative to an admitted formal substrate; its formula or proof term remains a C.29 representation of the independently recovered formal change.

**Mint vs reuse.** A.3.4 reuses the already admitted root U-kind and public name `U.Transformation` from E.24.UK. It introduces no additional U-kind: `componentTransformation` and `compositeTransformation` are local participant meanings for already individuated occurrences. `TransformationPartOfRelation` remains a provisional designator for a blocked derived relation-kind candidate; it has no admitted occurrence or `RelationSignature`, and durable name selection through F.18 opens only after E.24/E.24.UK admission. A.3.4 mints only the local well-formedness-constraint identifier `WF-A34-TPD-1`; that identifier is not an ontic, relation kind, declaration member, or occurrence.

#### A.3.4:4.2 - First-use transformation basis

Use these questions as a recognition aid, not as fields of a transformation record:

| Question | Exact object to recover | Stop condition |
| --- | --- | --- |
| What changed? | one exact governed referent | stop if only a label, file, diagram, or desired object is available |
| Across which boundary? | temporal extent or formal ordering boundary | stop if before and after are merely two unrelated observations |
| What actual facts differ? | direct relation occurrences and characteristic-state facts | stop if the only basis is a method, plan, trace, formula, or assertion |
| What delimits one occurrence? | boundary conditions and continuity or reidentification rule | split or leave identity unresolved when the rule does not cover the gap |
| Which later claim relies on this change? | exact receiving work or decision and its direct relation | add no neighboring object that the receiving use does not depend on |

**Worked first use.** For a reactor cooling loop, identify the exact loop state as the changed referent, the thermal-power step and stabilization interval as the temporal boundary, the measured temperature-profile facts before and after the boundary, and the operating conditions that delimit the episode. The revised operating method, control-law episteme, dated adjustment work, measurements, safety assessment, and release decision remain separate objects. None alone is the transformation.

##### A.3.4:4.2.1 - Ground proposed components and the whole-configuration change independently

Use `componentTransformation` and `compositeTransformation` only as participant meanings for exact already individuated `U.Transformation` occurrences. They are not additional U-kinds or fields of a composite record.

Identify every proposed component transformation and the proposed whole-configuration transformation independently through A.3.4:4.1. A sampled point, arbitrary subinterval, method step, work part, flow node, graph edge, trace segment, formula term, before-and-after image, shared changed referent, or temporal inclusion establishes neither transformation parthood nor that the selected transformation has no parts.

The neighboring general patterns do not silently supply the missing bridge. `A.22` can identify a selected structure whose relation organization changes; `C.27.TA` can identify temporal aspects; `A.14` and `C.13` govern structural mereology and a `Γ_m` construction trace. None of those results by itself states that one actual change contributes to another actual change, that several changed referents constitute the changed referent of another transformation, or that several transformations compose one transformation. A `Γ_m.sum` of entity parts establishes structural extensional identity under C.13; it does not make the resulting whole an actual bounded change or make changes of its inputs parts of that change.

Accordingly, one independently grounded change of an exact selected configuration may be retained as a configuration transformation under A.3.4:4.1. It is not thereby a composite transformation, and separately grounded mounting, wiring, or connection transformations are not thereby its components. Ground a composite transformation only after exact direct contribution and transformed-referent relations, their temporal and boundary compatibility governors, and one applicable subject composition and reidentification rule are all recoverable. If any of that basis is missing, retain the independently identified transformations and stop before composition or parthood.

A composition-grounded whole-level characteristic is not constitutive of composite-transformation identity. It becomes an additional A.1 recognition component only after the same exact composite is independently grounded under the preceding rule. Without that characteristic or the modal larger-assembly component, retain the grounded composite and stop only before A.1 classification; without the composition basis itself, stop earlier and assert no composite.

##### A.3.4:4.2.2 - Keep `TransformationPartOfRelation` at candidate status

`TransformationPartOfRelation(componentTransformation, compositeTransformation)` is a designator for a proposed derived relation-kind candidate, not an admitted FPF relation kind. A.3.4 supplies the subject-side question and a proposed settlement, but neither this pattern nor a predicate-shaped phrase admits the kind. Until one exact E.24/E.24.UK admission result is available, do not assert `TransformationPartOfRelation` occurrences and do not publish an A.6.0 `RelationSignature` for this candidate.

The present one-off transformation-parthood use does not pass A.6.RCD disposition 2. No exact direct pattern supplies actual-change contribution to another actual change or constitution of the whole changed referent by component changed referents; no exact temporal or boundary compatibility predicate and no subject composition rule or substrate are selected. A C.2.1 episteme may identify that blocked claim and its missing basis, but it may not assert a positive local compound transformation-parthood claim.

The proposed derived-kind settlement is therefore conditional and blocked:

| Settlement component | Candidate rule or current stop |
| --- | --- |
| component participant | one exact independently individuated `componentTransformation : U.Transformation` |
| composite participant | one exact independently individuated `compositeTransformation : U.Transformation`, available only after the composition basis in 4.2.1 is governed |
| proposed obtaining | if admitted later, the component's governed actual change contributes to the composite's actual change under exact named base facts; exact temporal, boundary, and transformed-referent compatibility predicates hold; and one selected composition and reidentification rule admits that contribution |
| proposed occurrence identity | one exact reusable definition states the proposed identity and recurrence semantics, including whether the same participant pair under another composition rule, substrate, or base-definition edition is the same occurrence; `A.6.REL` governs that occurrence-identity question, while `E.24` / `E.24.UK` decides only whether to admit the candidate kind against the settled definition |
| current disposition | missing-governor and missing-substrate blocker; no positive local compound transformation-parthood claim, classified occurrence, reusable definition, or admitted kind |
| admission stop | no reusable predicate-definition episteme has one truthful exact C.2.1 `EntityOfConcern`; no exact base-relation kinds and direct patterns govern actual-change contribution or changed-referent constitution; temporal and boundary compatibility governors, selected derivation substrate, base-definition dependencies, one occurrence-consuming receiver, occurrence identity, and an E.24/E.24.UK admission result are absent |
| failure boundary | temporal inclusion, co-occurrence, a shared referent, adjacency in a flow, a list of effects, an unresolved claim, or the candidate designator establishes neither composition, admission, nor an occurrence |

**Well-formedness constraint `WF-A34-TPD-1` — usable future transformation-parthood definition.** A future reusable predicate-definition episteme is usable here only when it names one truthful exact C.2.1 `EntityOfConcern`, the exact base-relation claims and direct governing patterns, derivation under a selected substrate, polarity, scope, time, applicability, dependencies and editions, positive and discriminating cases, the admissible receiving use, and a proposed occurrence-identity law governed by `A.6.REL`. When stable occurrence semantics are required, A.6.RCD routes the proposed settlement to E.24/E.24.UK and A.11; E.24/E.24.UK decides admission, while A.6.REL retains occurrence-identity authority. The definition remains distinct from the candidate kind and every occurrence. Until that basis exists, ordinary work retains the independently identified transformations and the exact blocker.

##### A.3.4:4.2.3 - Apply A.1 only to a governed composite transformation

Membership in `U.Transformation` supplies no holonhood. A.1 remains the authority for the constructive criterion; the table below maps its components to a transformation case without redefining them. Only an exact governed composite transformation may also be classified as `U.Holon`, and only when that same entity satisfies A.1. This is dual classification of one entity, not a relation occurrence and not admission of `U.Transformation` as a holon kind.

The unresolved transformation-parthood blocker supplies neither composite identity nor the exact admitted part-relation occurrences required by A.1. Positive A.1 classification therefore waits for a governed composite transformation, an admitted direct transformation-parthood kind, exact obtaining occurrences under it, and every other A.1 component. An independently identified configuration transformation may remain a valid `U.Transformation` while this positive classification is blocked.

| A.1 constructive component | Transformation-specific realization | Stop or failure boundary |
| --- | --- | --- |
| exact candidate | one already individuated `compositeTransformation` with exact changed referent, extent, boundary conditions, actual change facts, governed composition basis, and continuity or reidentification rule | a separately identified configuration transformation is not yet a composite by that fact; a task, method, plan, delta formula, trace, relation expression, or picture is not the candidate |
| exact constituents | two or more independently individuated `componentTransformation` occurrences whose exact contribution to this composite is governed | arbitrary time slices, concurrent changes, method steps, work parts, and representation nodes are not constituents |
| constructive part relations and assembly | exact obtaining transformation-parthood occurrences under an admitted direct kind, together with the governed contribution, compatibility, and composition facts | the candidate `TransformationPartOfRelation` name, a missing-governor note, temporal inclusion, common referent, or co-occurrence supplies no admitted occurrence |
| reidentification rule | one exact C.2.1 predicate-definition episteme whose `EntityOfConcern` is the composite transformation and whose claim admits declared constituent and boundary-condition variation while preserving that composite | a tuple, path label, trace, or diagram does not reidentify the actual change |
| composition-grounded whole-level characteristic | at least one exact characteristic of the composite whose value or state is produced or sustained by the declared composition and is not attributable to one component alone | this is an additional A.1 component, not a condition for identifying every transformation; an effect label or list of component effects does not supply it |
| possible participation in a larger constructive assembly | the composite's actual boundary, interfaces, relevant characteristics, and identity-preservation conditions satisfy the applicability and compatibility conditions of at least one governed larger-assembly construction method or rule under which it could participate as a constituent while preserving identity | the method-or-rule episteme describes the construction and conditions; it does not create compatibility or possibility |

Whether those world-side facts satisfy or fail A.1 is independent of evidence availability. When a reusable recognition evaluation is current, A.6.1 governs the typed operation and actual bindings; its result is `true`, `false`, or `unknown`. `unknown` reports inability to determine satisfaction because evidence or a dependency is unavailable; it is not a state of the transformation.

An optional C.2.1 classification assertion may record the judgment about the exact composite and the already admitted `U.Holon` kind. The assertion creates none of the composite, components, part relations, reidentification rule, whole-level characteristic, compatibility facts, construction method or rule, larger-assembly possibility, or holonhood. Exact evidence and assurance relations support or warrant its claim content; G.11 governs assertion-edition currentness; receiving work decides whether to rely, decline, defer, or reopen. A.1 satisfaction, failure, or recognition-evaluation uncertainty supplies neither warrant for a B.2 whole-reidentification claim nor grounds for selecting B.2.

Stress the boundary before classifying:

- a pressure increase may be identified as one `U.Transformation` at the resolution needed by the current use; sampling or subdivision establishes neither constructive transformation parts nor absence of such parts;
- a switch transition may be treated as effectively instantaneous at the selected temporal resolution and identified as one `U.Transformation`; that resolution claim establishes neither indivisibility nor constructive parts;
- subintervals of continuous biological growth become component transformations only when each is independently identified; they compose one transformation only under exact direct contribution and compatibility governors plus an applicable composition and reidentification rule;
- a formal transformation can be actual under a selected formal substrate, while its formula, morphism, or proof term remains a C.29 representation and supplies no holonhood;
- mounting, wiring, connection, and whole-configuration changes may each be identified independently; without the exact transformation-composition basis they remain separate, and positive A.1 classification does not begin.

##### A.3.4:4.2.4 - Keep work and production claims outside transformation identity

Exact work may cause, realize, or participate in a transformation only through separately governed work-to-change facts; temporal overlap is insufficient. A post-state, work reference, verbal predicate, changed continuing entity, or classification of a composite transformation as `U.Holon` establishes none of production-work participation, entity-identity inception, or production completion. Recover each such claim from its exact work, work-part, subject-identity, completion-criterion, and direct effect facts under `A.15.PROD` and the direct subject patterns it invokes. A.3.4 contributes the independently identified actual transformations and no universal production relation.

#### A.3.4:4.3 - Keep six layers separate

For one exact transformation, keep these objects distinct:

| Layer | Exact object | Governing responsibility |
| --- | --- | --- |
| actual bounded change | one `U.Transformation` | A.3.4 identifies changed referent, extent, boundary conditions, actual change facts, and continuity |
| exact subject facts | obtaining relation occurrences and characteristic-state facts | each direct subject pattern governs participants, obtaining, and identity |
| reusable change semantics | one predicate-definition episteme when repeated use needs the same rule | A.3.4 or the direct subject pattern states how governed facts satisfy the predicate |
| transformation assertion | one C.2.1 episteme asserting that the transformation or base facts obtain | C.2.1 identifies claim content, exact EntityOfConcern, and effective reference scheme; scope and viewpoint remain neighboring relations |
| representation | formula, morphism, path, graph, diagram, trace, tuple, or state-plane expression | C.29 governs correspondence to independently recovered objects |
| evidence or evaluation result | an episteme used to support or evaluate the assertion | the measurement, evaluation, evidence, provenance, or assurance pattern governs that use |

A verbal predicate does not turn every obtaining relation occurrence into a transformation. Assignment, availability, installation, and temporal order can obtain without change. Conversely, one actual transformation may require several relation facts without being identical to any one of them.

Do not restore the old `transformationRelation` field. First use an already governed direct relation when it expresses the needed fact. Otherwise apply A.6.RCD: only a substrate-admitted compound over exact governed base facts can yield a local relation-bearing claim; if that basis is absent, return the exact missing-governor or missing-substrate blocker. Introduce a reusable predicate-definition episteme only for repeated semantics. A new durable relation kind needs its own obtaining and occurrence-identity law; do not insert a task, morphism, operation family, or predicate into one union-valued field.

#### A.3.4:4.4 - Recover neighboring objects only for the current claim

A neighboring object is not a slot of `U.Transformation`. State its exact relation to the transformation, changed referent, work, or receiving use only when that relation is current.

| Current neighboring claim | Exact owner and boundary |
| --- | --- |
| reusable semantic way of doing | `A.3.1` governs `U.Method`; method existence establishes no actual change |
| claim-bearing account of that way | `A.3.2` and C.2.1 govern `U.MethodDescription`; description establishes neither work nor change |
| typed operation arguments or results | A.6.1 governs the exact operation declaration and application binding; these are not generic transformation inputs or outputs |
| intended work | `A.15.2` governs `U.WorkPlan`; intention establishes no dated work or actual transformation |
| performed work | `A.15.1` governs dated Work occurrences admitted under `U.Work`; exact work-to-change facts are recovered under their direct governor, because temporal coincidence is insufficient |
| transformation-flow location or composition | `E.18` governs selected `TransformationFlowStructure`; a flow locus neither performs work nor makes a change actual |
| mathematical expression | `E.18.2` and `C.29` govern representation; a graph edge, morphism, or delta expression is not the world-side occurrence |
| dynamics model | `A.3.3` governs the episteme; prediction is not actuality or permission |
| evidence, measurement, evaluation, or assurance | the direct measurement, evaluation, evidence, provenance, or assurance pattern governs the exact support or judgment relation |
| description, view, publication, form, or carrier | C.2.1 and E.17/E.24.PUB keep the episteme, view membership, publication occurrence, publication form, and carrier distinct |
| `input`, `output`, `result`, `outcome`, `deliverable`, or `handoff` | recover the exact participant and direct relation to a method declaration, planned work, actual work, transformation, evaluation, commitment, delivery, acceptance, transfer, or receiving work; the word is not a kind or universal slot |

A declared post-state is part of transformation description. An actual post-boundary state or changed entity is a subject-side fact. Treating that entity or relation as a result requires an additional exact receiving-use relation; acceptance, delivery, publication, and downstream effect remain separate. A transformation therefore has no generic `ResultRef` or `OutputConditionOrPortRefs` slot.

When an episteme about the transformation is current, identify it normally through C.2.1: exact claim content, the transformation or another exact subject as EntityOfConcern, and the effective reference scheme. Add claim scope, viewpoint, empirical grounding, edition, publication, or representation only through the direct neighboring relation required by the use.

#### A.3.4:4.5 - Neighboring Distinction Table

| Current claim | Governing pattern |
| --- | --- |
| actual bounded transformation | `A.3.4 U.Transformation` |
| selected transformation-flow structure, locus, path, crossing, or flow valuation | `E.18`; A.3.4 still governs each exact transformation occurrence |
| graph, algebra, morphism, path, tuple, or wiring expression | `E.18.2` and `C.29` as representation, not actuality |
| semantic way of doing | `A.3.1 U.Method` |
| description of a way of doing | `A.3.2 U.MethodDescription` |
| state-space and transition-law episteme | `A.3.3 U.Dynamics` |
| reusable operation declaration or application binding | `A.6.1` |
| planned or dated work | `A.15.2 U.WorkPlan` or an `A.15.1` Work occurrence admitted under `U.Work` |
| positive temporal aspect or temporal-claim adequacy | `C.27.TA` or `C.27` |
| problem-to-work carry-through | `E.18.1`; it carries exact objects and does not retype them |
| evidence, evaluation, assurance, gate, decision, source use, publication, delivery, acceptance, or transfer | the direct pattern governing that exact claim |

#### A.3.4:4.6 - Description And Publication Boundary

A method description, dynamics model, transformation diagram, transformation-flow structure description, dashboard, result record, source span, publication, or proof may describe a transformation or provide evidence for a use. It is not the transformation.

If the description itself is under concern, use `C.2.1`, `A.3.2`, `A.3.3`, `E.17`, `E.18`, or the direct publication or source pattern. If the transformation is under concern, keep the description as a neighboring episteme or publication value.

#### A.3.4:4.7 - Formal Transformation And Project-World Realization

A morphism, constructive proof, or formal state transition can correspond to an actual transformation of a governed formal object under the selected formal substrate. The formula, morphism, or proof term is still its C.29 representation.

For a physical, clinical, organizational, architectural, documentary, or epistemic change, a formal expression may specify, predict, constrain, or compare the transformation. Project-world actuality additionally needs the exact changed referent, boundary, subject facts, and, when work is claimed, dated work plus governed work-to-change facts. Do not infer realization, evidence, permission, acceptance, or a result relation from the formal construction.

#### A.3.4:4.8 - Multi-reading source phrase

Use this slice when one phrase seems to name method, mechanism, formal construction, work, evidence, and transformation at once:

> "The workflow algorithm transforms the emergency-stop specification, and the proof shows the new plant boundary is safe."

Recover separate objects:

- the workflow or algorithm may designate a `U.Method` or `U.MethodDescription`;
- the proof is a claim-bearing episteme using a declared formal substrate;
- when claim content changes, the earlier specification episteme and the later specification episteme are distinct C.2.1 identities; `EpistemeEditionRelation` relates them only when its historical-continuation predicate obtains;
- dated editing or review is a Work individual admitted under `U.Work`;
- edition succession alone establishes no actual transformation of one continuing episteme. An A.3.4 specification-side transformation requires one exact already-existing continuing referent governed under its direct pattern—such as a selected `U.PresentationCarrier` under E.24.PUB or a separately governed claim-bearing constituent organization—plus the exact boundary, actual before/during/after facts, and continuity or reidentification rule; if that basis is absent, stop without the transformation claim;
- when revision work first constitutes the later episteme, treat that first existence as a separate A.15.PROD entity-identity-inception question. Require the exact `productIdentitySpecificationEdition`, its direct subject-governed applicability basis, exact `identityClosingWork`, governed work-to-change and change-to-identity links, and the earliest satisfying boundary; otherwise return the exact missing-governor or missing-basis blocker;
- a plant change, safety evaluation, assurance claim, gate decision, and publication are separate objects and relations.

If only the proposed wording and proof are available, do not assert a project-world plant transformation. When the specification claims differ, identify the earlier and later epistemes separately and test the exact `EpistemeEditionRelation`; distinct episteme succession is not an actual transformation of one episteme. Assert an A.3.4 specification-side transformation only for a separately governed continuing referent with the required boundary, facts, and continuity basis. If the receiving use instead asks when revision work first constituted the later episteme, route that claim separately through A.15.PROD and stop when its direct basis is absent. The proof can support an exact assertion only through its direct evidence or derivation use; it does not prove its own project use.

### A.3.4:5 - Archetypal Grounding

#### A.3.4:5.1 - Physical system change

A nuclear-plant team claims a revised operating method stabilizes a temperature profile after a thermal-power change. Identify the actual cooling-loop change through the exact loop state, stabilization interval, operating boundary conditions, and characteristic-state facts. The method is `U.Method`; the control-law model is an episteme; dated adjustment work is a Work individual admitted under `U.Work`; measurements and the safety decision have separate governors. None substitutes for the actual transformation.

#### A.3.4:5.2 - Biological editing

A CRISPR project claims an editing protocol changed a DNA target while keeping off-target risk under a bound. The actual transformation concerns the exact biological referent, edit interval, boundary conditions, and sequence facts. The protocol description, biochemical mechanism, lab work, sequence-measurement result, risk evaluation, acceptance verdict, and publication remain separate. `edited sequence`, `lab output`, and `accepted result` do not name one relation.

Separately, `Seedling-B17` undergoes a spontaneous first-leaf unfolding episode. The changed referent is the already-existing seedling under its direct biological identity rule. The exact boundary runs from unfolding onset `t0` to the first stable full-expansion state `t1` under declared growth conditions; exact leaf-configuration and exposed-surface facts before, during, and after distinguish the episode, while measurements only support an assertion about those facts. The same-seedling continuity rule covers ordinary cellular turnover and growth and excludes division, grafting, death, or replacement. At this selected resolution these facts ground one actual `U.Transformation` and assert neither finer transformation parts nor partlessness. No `U.System`, `U.RoleAssignment`, enacted method, dated Work occurrence admitted under `U.Work`, transformer, or production-through-work claim is introduced unless separately grounded. A seedling label, observation series, or growth record supplies none of those claims. A.15.PROD therefore opens no production-through-work claim; retain the actual transformation and return any incompatible actor-side requirement to its direct governor without inventing a performer.

#### A.3.4:5.3 - Specification repair

A safety specification is revised so that an emergency-stop boundary no longer permits two incompatible readings. `EmergencyStopSpec-E1` and `EmergencyStopSpec-E2` differ in claim content and are therefore distinct C.2.1 epistemes. `EpistemeEditionRelation(EmergencyStopSpec-E1, EmergencyStopSpec-E2)` may obtain only when its historical-continuation predicate is grounded; neither participant is the same changed episteme. Suppose exact source carrier `EmergencyStopSpec-Carrier-17 : U.PresentationCarrier` is selected under E.24.PUB and independently governed as the same carrier across the editing interval. A.3.4 may then identify a transformation of that continuing carrier only from its exact editing boundary, before/during/after borne-expression facts, and carrier-continuity rule; if direct carrier identity, those facts, or that rule are absent, no A.3.4 transformation claim follows from the two episteme identities. If the editing work is additionally claimed to have first constituted `EmergencyStopSpec-E2`, the separate A.15.PROD inception branch requires the exact applicable identity-specification edition, exact identity-closing work, governed effects and links, and earliest satisfying boundary; otherwise return its exact blocker and do not assert that inception or an edition relation that depends on it. The editing work, repair method, ambiguity-removal assertion, review result, and publication of the later episteme remain distinct.

#### A.3.4:5.4 - Formal construction

A proof constructs a formal object and shows that a morphism preserves an invariant. Under the declared formal substrate, the exact formal object and ordered boundary can ground a formal transformation. The proof term and morphism expression are representations; a publication of the proof is another relation. No physical or organizational work follows without an independently governed realization claim.

#### A.3.4:5.5 - Architecture change

An architecture team changes a selected structure so that an interlevel conflict is reduced while a key architecture characteristic stays within bounds. The selected structure and its before-and-after relation organization remain governed by the architecture patterns. The architecture work, change assertion, characteristic evaluation, decision, and publication remain separate from the actual transformation of the selected structure.

#### A.3.4:5.6 - Functional transformer in a flow

When a sentence says that a system "transforms input to output" or "implements an algorithm", recover at least four different claims: the exact system and its role assignment when current; the actual transformation and changed referent; the direct participant, port, or operation bindings at the boundary; and the selected E.18 flow location. Recover the method or method description only when that claim is current.

Examples:

- A pump can be the acting system while the actual transformation is the bounded pressure change of an exact fluid volume. Inlet and outlet pressure facts are characteristic-state and port facts; the pump curve is a model episteme.
- A warehouse can perform receiving work while pallet location and inventory-state changes are transformations. Orders and pallets participate under their exact work, transfer, resource, or affected-referent relations; they are not one input-output kind.
- A neural-network block can participate in an activation transformation. Tensor-shape declarations, attention method, dated inference work, benchmark evaluation, and architecture allocation retain separate governors.

A flow position, algorithm label, module name, or output record establishes neither actual transformation nor work.

#### A.3.4:5.7 - Assembly changes before PumpSkid identity

Before any claim that PumpSkid 7 exists as one entity, the exact referents are the already existing base frame `BF-7`, pump unit `PU-7`, motor `MU-7`, junction enclosure `JE-7`, pipe spool `PS-7`, cable set `CS-7`, and their open mechanical, electrical, and fluid-interface facts. `AssemblyConfiguration-7` is the exact A.22 selected structure of those referents and their actual attachment, terminal, and flange-connection relation organization during assembly. It is not a surrogate name for a future PumpSkid 7 entity.

The mounting transformation changes the exact frame-to-pump and frame-to-motor attachment facts. The wiring transformation changes exact cable-to-terminal connection facts. The fluid-connection transformation changes exact spool-to-flange and seal facts. Each is identified independently under A.3.4:4.1 by its changed referent, extent, boundary conditions, actual before/during/after facts, and continuity rule. Provided the attachment, terminal, flange, and seal facts themselves have direct application-side governors, the change of `AssemblyConfiguration-7` can likewise be identified independently from that selected structure's before/during/after relation organization, exact extent and boundary conditions, and its own continuity rule. Call that occurrence the configuration transformation; the three other changes are not its components merely because they occur in the same assembly episode.

No named FPF basis in this use supplies the missing transformation-to-transformation bridge. A.22 supplies the selected structure, C.27.TA supplies temporal aspects, and A.14/C.13 supply structural mereology and `Γ_m` traces; none supplies actual-change contribution, changed-referent constitution, transformation-specific temporal or boundary compatibility, or the subject composition rule required by A.6.RCD. The case therefore stops before any component-to-configuration parthood or composite-transformation claim. It retains the independently identified mounting, wiring, fluid-connection, and configuration transformations plus the exact missing-governor and missing-substrate blocker.

The candidate `TransformationPartOfRelation` name creates no occurrence, and no positive local compound parthood claim is asserted. Positive A.1 classification is also blocked: it would additionally require an admitted direct transformation-parthood kind with exact obtaining occurrences, a composite reidentification rule, a composition-grounded whole-level characteristic, and the modal larger-assembly component. The point at which a separate PumpSkid 7 identity rule first becomes true remains an entity-identity inception question; production completion, commissioning work, evidence, acceptance, and any B.2 whole-reidentification claim also remain separate.

### A.3.4:6 - Bias-Annotation

Lenses tested: **Onto**, **Arch**, **Prag**, **Epist**, **Gov**.

This pattern keeps actual change, transformation composition, conditional holon classification, direct subject facts, method, work, flow structure, representation, assertion, evidence, evaluation, publication, production, and receiving use distinct. It resists software narrowing, method-as-effect, model-as-authority, trace-as-law, formal-as-project-work, relation-verb-as-change, sampled-slice composition, blanket transformation holonhood, work-caused-change-as-production, and result-word-as-kind errors.

### A.3.4:7 - Conformance Checklist

| Check | Conformance statement |
| --- | --- |
| `CC-A34-1` | One exact changed referent, temporal extent or formal ordering boundary, boundary conditions, actual change facts, and continuity or reidentification rule identify the transformation. |
| `CC-A34-2` | A task, desired state, method, plan, work trace, operation family, model, delta expression, morphism, predicate, relation occurrence, assertion, picture, or publication does not establish actuality or transformation identity. |
| `CC-A34-3` | Every subject fact uses its direct relation or characteristic governor; no union-valued `transformationRelation` field is used. |
| `CC-A34-4` | Method, method description, operation declaration or binding, plan, work, flow structure, representation, evidence, evaluation, and publication retain separate identities and relations. |
| `CC-A34-5` | A transformation assertion is a C.2.1 episteme about the actual transformation or exact base facts; it is not the occurrence. |
| `CC-A34-6` | Time, rate, rhythm, duration, and ordering claims use `C.27.TA` and `C.27` without replacing transformation identity. |
| `CC-A34-7` | E.18 flow structure and C.29 representation neither perform work nor make the transformation actual. |
| `CC-A34-8` | Evidence, assurance, gate, acceptance, and decision authority are not inferred from the transformation or its description. |
| `CC-A34-9` | `input`, `output`, `result`, `outcome`, `deliverable`, and `handoff` remain Plain relation-position cues until the exact participant and direct relation are recovered. |
| `CC-A34-10` | When performed work is claimed to cause or realize the transformation, exact work-to-change facts are governed independently; co-occurrence is insufficient. |
| `CC-A34-11` | Every proposed component and whole-configuration transformation is identified independently. Composition is asserted only under exact direct contribution and transformed-referent relations, temporal and boundary compatibility governors, and one applicable composition and reidentification rule; otherwise the transformations remain separate. |
| `CC-A34-12` | `WF-A34-TPD-1` remains unsatisfied while any exact base relation, direct pattern, temporal or boundary compatibility governor, derivation substrate, composition or reidentification rule, dependency edition, occurrence-consuming receiver, or `A.6.REL` identity basis is absent. `TransformationPartOfRelation` remains a proposed derived-kind designator, and the exact result is a blocker: no positive local compound transformation-parthood claim and no candidate-kind occurrence are asserted. |
| `CC-A34-13` | Only an exact grounded composite with exact admitted part-relation occurrences and every additional A.1 fact may also be classified as `U.Holon`; world-side satisfaction, three-valued evaluation, optional assertion, evidence or warrant, edition currentness, receiving disposition, and B.2 remain separate. |
| `CC-A34-14` | No post-state, work reference, work-caused change, changed continuing entity, or transformation holon classification proves production-work participation, entity-identity inception, or production completion. |

### A.3.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Method name as change | "This method transforms X" is treated as an actual occurrence. | Recover the exact changed referent, boundary, and actual subject facts; keep the method under A.3.1. |
| Process diagram as work | A workflow diagram is treated as enacted work. | Use `E.18` or `A.3.2` for the diagram; use `A.15.1` for dated work. |
| Dynamics model as permission | A transition law is used to approve action. | Keep `A.3.3` for the model; use evidence, gate, decision, and assurance patterns for use authority. |
| Temporal trend as intervention | A rate or rhythm trend is treated as proof of changed behavior under an intervention. | Use `C.27.TA` and `C.27`, then recover the actual changed referent and exact subject facts separately. |
| Formal construction as work | A morphism or proof construction is treated as work performed in a project-world object. | Use `C.29` or the direct formal pattern for the mathematical relation; name realization and work separately. |
| Publication as transformation | A dashboard or report is treated as the changed state. | Use publication or source patterns for the publication; keep the transformation as the governed object. |
| Sliced trajectory as composition | Samples, subintervals, method steps, work parts, concurrent changes, or flow nodes are declared component transformations by containment or proximity. | Independently identify every actual transformation. Assert composition only when exact direct contribution and compatibility governors plus an applicable composition and reidentification rule are available; otherwise retain separate transformations and the exact blocker. Sampling or subdivision likewise supplies no evidence of indivisibility. |
| Current-resolution identification as partlessness | A change identified as one occurrence at the resolution of the current use is treated as necessarily atomic, indivisible, or partless, or as automatically composite and holonic. | Keep the independently identified `U.Transformation`; infer neither presence nor absence of finer parts. Open composition only under its exact governors and apply A.1 only to a grounded composite transformation. |
| Work-caused change as production | Any change following work is called a produced entity or completed production. | Recover exact work-to-change facts, then separately test subject identity inception and the applicable production-completion criterion. |

### A.3.4:9 - Consequences

- FPF gains one place to identify actual bounded transformations without turning method, work, relation expressions, descriptions, evidence, or publications into the change.
- Current-resolution identification remains cheap: one bounded change can be identified without settling its finer composition. This says neither that finer parts exist nor that they do not.
- An independently grounded change of a selected configuration remains distinct from concurrent component changes until exact contribution, compatibility, composition, and reidentification governors establish one composite transformation.
- When the exact base relations or derivation substrate are absent, A.6.RCD returns a missing-governor or missing-substrate blocker; neither a positive local compound parthood claim nor a typed transformation-parthood occurrence is available.
- Only after exact admitted parthood occurrences and the additional A.1 whole-level and modal components are present may the same composite be considered for `U.Holon` classification.
- Direct subject patterns keep ownership of the facts by which change, contribution, compatibility, work participation, and any later production claim are grounded.
- E.18 can arrange or locate transformation occurrences in a selected flow structure without becoming their occurrence ontology.
- Ordinary result wording remains usable after the exact receiving relation is recovered; no universal transformation-result or production relation is introduced.
- Users pay the cost of occurrence identity, composition, and classification only when the receiving use depends on those distinctions.

### A.3.4:10 - Rationale

`U.Transformation` gives FPF one governed object for actual bounded change. Its identity basis is subject-side: exact changed referent, extent or ordering boundary, boundary conditions, actual change facts, and continuity or reidentification. Task, method, plan, work, operation family, relation occurrence, predicate, representation, assertion, evidence, evaluation, publication, and receiving-use relations remain inspectable because none is hidden as a field of the transformation.

An independently identified configuration transformation is not a composite merely because separately identified changes occur within the same episode or concern referents selected into that configuration. Composite identity opens only when exact direct contribution and transformed-referent relations, temporal and boundary compatibility predicates, and one applicable composition and reidentification rule are governed. The proposed `TransformationPartOfRelation` candidate would classify constructive parthood only after its exact reusable definition, base relations, derivation substrate, dependencies, occurrence-consuming use, identity law, and admission are settled. Until then, the truthful result is the exact blocker and the independently identified transformations, not a positive local compound claim or candidate-kind occurrence.

A.1 remains an independent second test. An exact composite can exist without satisfying the whole-level-characteristic or modal larger-assembly components. Conversely, the word composite and the candidate parthood name supply no holonhood; positive classification requires exact admitted part-relation occurrences and all remaining A.1 facts.

This architecture also keeps production and result claims honest. Work can cause or participate in change without every work-caused change being production. A post-boundary entity can be the same continuing entity rather than a newly constituted entity. Production-work participation, entity-identity inception, production completion, delivery, acceptance, and downstream effect each require their own exact governed claim.

### A.3.4:11 - SoTA-Echoing

A.3.4 uses four current source branches for four different questions. None of them makes a task, event description, graph, proof, work trace, or construction label an actual `U.Transformation`, and none admits transformation composition for FPF.

| Current source and practice answer | Exact use in A.3.4 | Adoption status and blocked overread |
| --- | --- | --- |
| Marletto, Deutsch, and Vedral, ["Tests of constructor theory"](https://arxiv.org/abs/2606.07352v1), 2026, arXiv edition `2606.07352v1`, reviews the current experimental-test branch of constructor theory in terms of possible and impossible tasks and constructors rather than ordinary program execution. | A.3.4:4.1 and 4.7 require an independently grounded actual bounded change even when a constructor-theory task or formal transformation is current; case 5.4 keeps the proof term or morphism expression as representation. | **Adapt.** Use the task/constructor distinction to discipline possibility and governing conditions. Reject the overread that a task, its description, a constructor label, or a formal expression establishes the actual occurrence, project-world realization, evidence, or permission; this source branch is not treated as consensus ontology for every change. |
| Deutsch and Marletto, ["Constructor theory of time"](https://arxiv.org/abs/2505.08692v3), 2025, current arXiv edition `2505.08692v3` revised in 2026, shows within that current branch why duration and dynamics need an account distinct from task possibility. | A.3.4:4.1 identifies the occurrence through its extent or formal ordering boundary and actual subject facts; 4.4-4.5 send temporal aspect and dynamics claims to `C.27.TA`, `C.27`, and `A.3.3`; case 5.1 keeps the control-law episteme separate from the cooling-loop change. | **Adapt.** Preserve the separation among task, duration, dynamics, and actual occurrence without importing constructor theory as FPF temporal ontology. Reject duration, a dynamics model, or a task specification as sufficient transformation identity. |
| Guizzardi, Benevides, Fonseca, Porello, Almeida, and Sales, ["UFO: Unified Foundational Ontology"](https://doi.org/10.3233/AO-210256), 2022, gives the current-state UFO account through distinct micro-theories that include events, situations, participation, causation, and change. | A.3.4:4.1 and 4.3-4.5 keep actual-change identity, subject facts, participation or work-to-change facts, causation, assertion, and representation as separately governed questions; case 5.6 exercises that separation for a system in a flow. | **Adopt the separation pressure; reject wholesale import.** FPF does not import UFO categories or infer event mereology from a model. It identifies one `U.Transformation` at the resolution of the receiving use and opens participation, causation, work, or representation only through their direct governors. |
| Borgo and Righetti, ["Towards Applied Constructional Ontology"](https://doi.org/10.3233/FAIA250480), 2025, argues that applied constructional ontology still requires explicit choices about mereology, dependence, identity, and application concerns. | A.3.4:4.2.1-4.2.3 and the PumpSkid case 5.7 require independently identified component and whole-configuration changes, direct contribution and transformed-referent relations, compatibility conditions, a composition and reidentification rule, and later kind admission before any transformation-parthood occurrence or holon classification. | **Adopt.** Adopt the demand for explicit applied mereology and identity choices. Reject the shortcut that temporal inclusion, graph adjacency, a shared referent, a construction label, or a selected structure already supplies transformation composition, part identity, or holonhood. |

For cases 5.1-5.7 the practitioner consequence is stable: recover the changed referent, boundary, actual facts, and continuity rule first; keep task, dynamics, work, participation, representation, assertion, and publication neighboring; and return the exact missing-governor blocker when a composition or production claim lacks its direct basis. Reopen these source-use decisions only if the constructor-theory branch changes the task-versus-actual-occurrence boundary, a stronger foundational event account changes the separation among event identity, participation, causation, and representation, or applied constructional ontology supplies a defensible contribution and reidentification rule that changes 4.2.1. A new notation, process diagram, or modeling tool alone is not enough.

### A.3.4:12 - Relations

- **Builds on:** `A.1` for the independent holon criterion, `A.6.RCD` for the missing-governor or missing-substrate stop and any future derived-kind route, `C.2.1` for blocker, definition, and assertion epistemes, and `A.7` for category separation.
- **Coordinates with:** `A.3` for acting-side transformer constitution only when an acting-system claim is current; `A.6.REL` for occurrence identity; `E.24` / `E.24.UK` for any future exact admission result; `F.18` for durable naming only after that settlement; `A.11` for parsimony when current; `A.14` and `C.13` for structural mereology without transformation-composition overread; `A.22` for a selected changed structure; `A.3.1`, `A.3.2`, `A.3.3`, `A.6.1`, `A.15.1`, `A.15.2`, and `A.15.PROD` for production-work participation, entity-identity inception, and production-completion recovery; `E.18`, `E.18.1`, `C.32.P2S`, `C.27.TA`, `C.27`, `C.29`, `A.10`, `B.3`, `G.11`, `B.2`, and the direct work-to-change, evidence, evaluation, gate, decision, source-use, production, delivery, acceptance, transfer, assurance, and publication patterns.

### A.3.4:End

