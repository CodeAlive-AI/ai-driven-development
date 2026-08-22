## A.15.PROD - Production Work, Entity-Identity Inception, and Production Completion Recovery

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Separate production work, when this exact entity first exists, and when production was completed.

**At a glance.** Production wording often compresses three questions: is this dated Work the whole production Work or only a declared part; when did changes attributed to that Work first make the applicable identity rule true so this entity began to exist; and, for completion, which subject state satisfied the criterion and which separate governor made that satisfaction close the exact production Work? This pattern answers each question with separate local claims. It introduces no universal production relation or production-work kind. Call one specification or criterion an edition of another only when their exact C.2.1 `EpistemeEditionRelation` obtains.

**Plain claim-record gloss.** A local compound relation-bearing claim is one checkable statement for one selected question, built from already governed facts. It is neither an omnibus production record nor a new relation kind. Whole production work, first existence, and completion therefore remain three separate claims even when they cite overlapping facts.

### A.15.PROD:1 - Problem Frame

**Use this when.** Practitioners **SHOULD** use this pattern when work is said to have *made*, *produced*, *built*, *assembled*, *grown*, *generated*, *finished*, or *completed* something and the receiving decision needs to know which exact production question is true. They **SHOULD** prefer it when one work occurrence is nested in larger work, several work parts act concurrently, an entity becomes identifiable before all work ends, or completion is being confused with delivery, acceptance, release, publication, or availability.

**Primary EntityOfConcern by selected branch.** Production wording is the umbrella. A production-work-participation claim concerns exact `currentWork`; an entity-inception claim concerns exact `producedEntity` after inception. Completion needs two claims when Work closure is asserted: the state-satisfaction claim concerns exact `completionSubject`, while the production-work-completion claim concerns exact `productionWork` and cites the separate closure governor. Keep each in its own C.2.1 episteme when persisted; never manufacture a union concern.

**Primary working reader.** A practitioner or modeler responsible for settling one of these production, identity, or completion questions for a current engineering, manufacturing, construction, lifecycle, audit, or scientific use before relying on delivery, acceptance, release, publication, or availability.

**Primary viewpoint.** The practitioner **SHOULD** recover the smallest receiver-relevant claim: select one branch, identify its exact `EntityOfConcern`, and stop when that branch is decided or its exact blocker is known. This pattern is not a form to fill in.

**First useful move.** The practitioner **SHOULD** first ask which answer the receiving action or decision needs now:

1. Is this dated Work the whole production Work for this use, or a declared proper part of it?
2. Which identity rule applies to the candidate, and at what boundary did changes attributed to this Work first make that rule true so this entity began to exist?
3. Which subject state satisfies the applicable completion criterion, and which declared predicate or local claim makes that satisfaction close the exact production Work at this boundary?

The practitioner **MUST NOT** answer one question with evidence for another.

**What goes wrong if missed.** Any work-caused change is called production; an entity is treated as existing before its identity rule first holds; a finishing operation is mistaken for entity creation; a plan, log, post-state picture, or first observation is treated as the change-producing link; and later delivery or acceptance silently rewrites historical completion.

**What this buys.** Teams can attribute production work at the right work boundary, state when one entity first exists, and preserve historical completion without inventing a universal relation kind. Narrow and larger production readings can coexist through exact work-part relations. Identity, completion, rework, delivery, acceptance, release, publication, and availability remain independently inspectable.

**Cross-domain recognition test.** These three non-exhaustive recognition situations show that the same three production questions remain separate across heterogeneous practice:

| Recognition situation | First current question | Blocked overread |
| --- | --- | --- |
| A fastening step is said to have "produced Car 42". | Is the step whole production work or a proper part, did Car 42 already exist, and which completion criterion is current? | The last visible step establishes neither first existence nor completion by narrative order. |
| A culture run or spontaneous biological process is said to have "produced Batch B17". | Is there an exact performing System, an obtaining occurrence of a directly declared assignment species, F.6 attribution, and Method enactment in dated Work; only then, which identity or completion branch is current? | Growth or reaction alone may ground actual transformation but establishes no Work occurrence admitted under `U.Work` and no production-through-work claim; a batch label, sample, or first observation closes none of those questions. |
| A build pipeline is said to have "produced ReleaseBinary 12". | Which dated build work and governed effects first established the exact artifact identity, or satisfied the build-completion criterion? | Build success, publication, release, deployment, and availability remain different claims. |

**First worked replay — Car 42.**

- **Work and actor.** `FasteningCell-7 : U.System` performs `NutFasteningWork-42` as the holder of obtaining assignment `Car42FasteningAssignment-42`. The assignment is an occurrence of directly declared `Car42FasteningAssignmentSpecies`, covers the Work, and supplies its F.6 attribution. The Work enacts the applicable fastening Method.
- **Actual change.** The named Work-to-change predicate connects that Work to `Car42FastenerAttachmentTransformation`.
- **State and closure.** At the fastening boundary, Car 42 satisfies the finishing-state criterion. `Car42FasteningClosureRule-v1` separately makes that satisfaction sufficient to close the fastening Work for this narrow use.
- **Answer.** **The Work completed the required fastening; it did not bring Car 42 into existence.**

The nearest blockers leave the established facts intact:

- If the Work-to-change predicate is missing, keep the Work and transformation separate and return `missing-governor[CAR42-FASTENING-WORK-TO-CHANGE]`.
- If Car 42 satisfies the state criterion but no rule connects that satisfaction to closure of the Work, preserve the state-satisfaction claim and return `missing-governor[CAR42-FASTENING-WORK-COMPLETION]`.

Neither failure requires the practitioner to fill a universal production record.
**So-what adoption test.** Would replacing the separate branch answers by one broad production sentence change what the receiver may rely on, schedule, audit, accept, release, or reopen? If yes, the practitioner **SHOULD** apply this recovery. If only one already-governed neighboring claim is current, the practitioner **SHOULD** use its direct pattern instead.

**Not this pattern when.** Practitioners **SHOULD** use `A.15.1` directly when the only question is what work occurred; `A.3.4` when the only question is what actually changed; `A.3.1` when the only question is the reusable way of doing; the direct identity pattern when only entity identity is current; or the direct evaluation, delivery, acceptance, release, publication, availability, evidence, or assurance pattern when only that neighboring claim is current. This pattern coordinates those objects only for a selected production-recovery question.

**No-mint disposition.** Authors and modelers **MUST NOT** introduce `U.ProductionWork` as a U-kind. They **MUST NOT** introduce `WorkProducesEntityRelation`, `EntityIdentityInceptionByWorkRelation`, `ProductionWorkRelation`, or `ProductionCompletionRelation` as universal relation kinds. The default result is one local C.2.1 claim episteme per selected question under A.6.RCD disposition 2. Repeated use of the same predicate with the same participant meanings in one subject practice may justify one reusable predicate-definition episteme in the pattern that defines it for that practice. Consider a derived relation-kind candidate only when a named later action must refer again to the same obtaining relation occurrence rather than merely reuse the predicate; A.6.RCD and later admission govern that continuation.

### A.15.PROD:2 - Problem

Production speech crosses several ontological boundaries. Dated Work is an occurrence. A transformation is the bounded change of a referent. An identity-specification episteme states when a candidate counts as the entity in question; a named applicability predicate or filled local claim applies it to the candidate basis and boundary. Entity-identity inception is the first boundary at which that applicable rule becomes true. For completion, a criterion first tests the state of `completionSubject`; a separate closure predicate or local claim says whether that satisfaction closes `productionWork`. A measurement or evaluation result is a separately defined value or episteme about its own concern; it is neither the produced entity nor Work completion itself.

These boundaries often differ. A ship can first exist while outfitting continues. A car can already exist before a required nut is fastened. A finished product can later be damaged, delivered, rejected, repaired, republished, or made unavailable. One broad production predicate hides those differences and also hides the exact missing governor when attribution cannot be established.

### A.15.PROD:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar production language vs exact claim identity | One sentence often carries work participation, entity inception, completion, and later acceptance at once. |
| Narrow work vs containing work | A finishing occurrence may itself be production work for one bounded use and a proper part of a larger production occurrence for another. |
| Product-class identity before the entity exists | Entity-inception recovery remains blocked unless the exact identity-specification episteme and either a named applicability predicate or a filled local claim apply it to the candidate basis, subject context, and inception boundary before inception; no surrogate future entity is introduced. |
| Actual work effects vs observation | Logs, deltas, pictures, and first observation can support a claim but do not create work-to-change or change-to-identity links. |
| Work composition vs transformation composition | A.15.1 may ground composite work while no accepted transformation-composition governor exists. |
| First existence vs completion | Identity and completion may coincide, but neither criterion entails the other. |
| Historical truth vs later state | Later damage, loss, rework, delivery, or acceptance neither erases nor silently rewrites an earlier completion claim. |
| Reusable language vs ontology economy | Repeated domain use may justify predicate semantics, but a convenient production label does not justify a universal relation kind. |

### A.15.PROD:4 - Solution

The practitioner **MUST** choose one of the three production questions, name the Work and the affected referent, candidate basis, or produced entity involved, and gather only the facts that decide that question. The practitioner **MUST** state each answer as a separate local compound relation-bearing claim and **MUST** stop or return an exact blocker when a required predicate, criterion, applicability rule, boundary fact, work granularity, or transformation-composition rule is missing. If another person, tool, or later decision must reuse the answer, publish that one claim as a C.2.1 episteme.

**Core and branch cut.** The common recovery core is receiver-first question selection, exact-object recovery, closure through declared predicates or one local claim selected under A.6.RCD disposition 2, and a deliberate stop. The production-work, entity-identity-inception, and production-completion branches add only their own `EntityOfConcern`, criterion or boundary, and branch-specific base. One branch neither inherits facts from another nor turns the common method into an omnibus production object. Work identity, transformation identity, subject identity, evidence, assurance, delivery, acceptance, release, publication, and availability remain with their subject patterns.

#### A.15.PROD:4.1 - Split the three questions before recovering evidence

| Question | Claim content | Ordinary stopping result | What it does not establish |
| --- | --- | --- | --- |
| Production-work participation | exact `currentWork` is itself `productionWork`, or exact `currentWork` is a declared proper work part of exact `productionWork` | one local positive or negative compound claim, or an exact work-grounding blocker | entity inception, completion, delivery, acceptance, or a universal production-work kind |
| Entity-identity inception | governed actual effects of exact `identityClosingWork` made exact `producedEntity` satisfy the rule in exact applicable `productIdentitySpecification` for the first time at exact `inceptionBoundary` | one local inception claim after the entity exists, plurality of incomparable minimal claims, or an exact blocker | production completion, later persistence, acceptance, or a reusable binary relation kind |
| Production completion | exact `completionSubject` satisfies exact applicable `productionCompletionCriterion` at `completionBoundary`, and a separate declared closure predicate or local claim connects that satisfaction to exact `productionWork` | one state-satisfaction claim plus, when asserted, one historically indexed Work-completion claim; otherwise the exact closure blocker | entity inception, delivery, acceptance, release, publication, or availability |

The three claims may cite overlapping facts. They remain different claims because they answer different receiving questions and can have different boundaries, criteria, and truthful C.2.1 `EntityOfConcern` values.

#### A.15.PROD:4.2 - Recover the smallest exact base

The practitioner **MUST** use only objects needed by the selected branch:

| Working name | Exact object and governor | Required contribution |
| --- | --- | --- |
| `productIdentitySpecification` | one exact C.2.1 predicate-definition episteme whose subject pattern states the identity rule; any continuing-edition relation to another specification episteme is stated separately | states the identity rule before inception without pretending that a future entity exists |
| identity-specification applicability basis | one named applicability predicate with its actual participants and boundary facts, or one filled local compound claim selected under A.6.RCD disposition 2 | applies the exact specification episteme to the candidate basis, subject context, and candidate `inceptionBoundary`; it introduces no universal applicability relation |
| `producedEntity` | one exact `U.Entity`, designated only after inception | is the entity whose identity rule first became true |
| `productionMethod` | one exact `U.Method` under A.3.1 | states the governed way of doing, intended production effect, applicability, and relevant identity or completion criterion meaning |
| `currentWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates the world-side dated occurrence; name each actual performer `U.System`, the obtaining occurrence of an exact directly declared `U.SystemRoleAssignment` species under which it performs, F.6 attribution, at least one obtaining `enactsMethod` relation, extent, and at least one obtaining locally declared containing-system relation. Name an additional enactment, binding, resource-use, or affected-referent relation only when the production claim uses that independently obtaining fact; none is a field stored in the occurrence. |
| `productionWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates either the same occurrence as `currentWork` or the exact larger Work occurrence of which `currentWork` is a declared proper part |
| `actualTransformation` | one or more independently identified `U.Transformation` occurrences under A.3.4 | names what changed without becoming the work or the produced entity |
| work-to-change basis | one named domain predicate with exact Work and transformation participants and obtaining case facts, or one filled local compound claim selected under A.6.RCD disposition 2 | establishes that selected actual changes are effects of exact work; coincidence is insufficient |
| `completionSubject` | the exact state-bearing entity or continuing referent judged by the completion criterion | keeps the criterion's subject explicit instead of applying a product-state test to Work |
| `productionCompletionCriterion` | one exact C.2.1 predicate-definition episteme whose subject pattern states the state-satisfaction rule; any continuing-edition relation to another criterion episteme is stated separately | states what state of `completionSubject` counts as satisfying the production requirement at the candidate boundary |
| production-work closure governor | one declared subject predicate or one filled local A.6.RCD claim that connects exact criterion satisfaction for `completionSubject` to closure of exact `productionWork` at the boundary | states why the Work is complete; criterion satisfaction alone does not supply this link |
| local assertion | one C.2.1 episteme | carries only the state-satisfaction claim or the production-work-completion claim needed by the selected question |

A method description, work plan, objective, commitment, product specification, evaluation result, or publication enters only when a named predicate or filled local claim connects it to the selected Work, entity, or claim and omitting that connection would change the named action or decision. Otherwise keep it separate. None is constitutive of every production occurrence.

#### A.15.PROD:4.3 - Select one production-work branch

**Whole-work branch.** `currentWork = productionWork` is admissible only when that exact dated Work enacts `productionMethod`; the method states its intended production effect; a named applicability claim applies the method to this case's inputs and conditions; the named work-to-change predicates obtain for the exact Work and transformations; and the identity or completion criterion that decides the selected question is named and applicable. A familiar broader production label establishes no parent work.

**Proper-part branch.** Exact `currentWork` is admissible as a proper part of exact `productionWork` only when `OperationalPartOf_work` or another exact A.15.1 work-part relation with fitting occurrence semantics obtains. Interval overlap or concurrency is asserted separately and establishes neither parthood nor coordination. The containing Work must likewise enact the production method; the method must state its intended production effect; a named applicability claim must apply it to the containing case; the named work-to-change predicates must obtain; and the identity or completion criterion that decides the selected question must be named and applicable. A shared label, project membership, common referent, temporal containment, overlap, or adjacency in a plan establishes no work parthood.

The two branches can support different bounded uses. A nut-fastening occurrence can be the whole production work for a narrowly bounded finishing operation and also a proper part of a larger car-production occurrence, provided each local claim names its exact extent, criterion, and work relation. `productionWork` is a relation-defined reading of one Work occurrence admitted under `U.Work`, not an intrinsic kind.

#### A.15.PROD:4.4 - Ground actual effects without inventing transformation composition

The practitioner **MUST** first recover every actual transformation independently through A.3.4: changed referent, exact extent or formal boundary, boundary conditions, actual before/during/after facts, and continuity or reidentification rule. The practitioner **MUST** then name the declared domain predicate for each exact Work-to-transformation pair, state its participant order, and show the case facts that make it obtain. If no one direct predicate suffices, use a local compound claim selected under A.6.RCD disposition 2 only when its constructor, governed base predicates, actual participants, and case facts are recoverable. If neither route is present, keep the Work and transformation separately and return `missing-governor[work-to-change]`. Temporal overlap, a common changed referent, a delta expression, a log record, or a post-state picture does not establish the link.

One transformation identified at the resolution needed by the production claim establishes neither presence nor absence of finer transformation parts. Work parts, method parts, samples, temporal subdivisions, concurrent changes, and flow representations do not establish transformation parts or a composite transformation.

If the selected production claim uses only independently identified transformations, continue without a composition claim. If it asserts positive composite-transformation identity, transformation parthood, or transformation holonhood and no accepted governor supplies that basis, return the exact missing-governor blocker. Composite `identityClosingWork` under A.15.1 does not cure that blocker and does not imply an isomorphic composite transformation.

#### A.15.PROD:4.5 - Recover entity-identity inception

**Definition: A15PROD-D1 (Entity-identity inception).** Entity-identity inception is the boundary at which exact `producedEntity` first satisfies the identity rule stated by exact `productIdentitySpecification` and a named applicability predicate or filled local claim applies that specification to the candidate basis, subject context, and boundary. Plain: **when this exact entity first exists**. `inceptionBoundary` is a case-local boundary designator, not a second technical term, claim kind, or relation kind.

For this branch, the practitioner **MUST** complete all five steps:

1. recover exact `productIdentitySpecification` as one C.2.1 predicate-definition episteme in the subject pattern that states the identity rule. Before inception, the governed question remains about exact work, method, actual effects, that specification episteme, and its candidate basis; no future `producedEntity` participant exists;
2. recover the named applicability predicate or filled local claim that applies that specification episteme to the exact candidate basis, subject context, and candidate `inceptionBoundary`, together with the exact actual effects of exact work and the declared links by which those effects bear on that rule;
3. find the earliest exact `inceptionBoundary` at which the rule in that applicable specification episteme becomes true and designate the resulting exact `producedEntity` only on the after-side of that boundary; the pre-inception candidate basis remains distinct from that entity;
4. identify exact `identityClosingWork`, using the one closing work occurrence when it exists or, for jointly necessary concurrent or nested work parts, their exact composite work under A.15.1 and its declared work-part relations; and
5. publish a positive local inception claim only after exact `producedEntity` exists and the claim names exact `productIdentitySpecification`, its named applicability predicate or filled local claim, exact `identityClosingWork`, exact `inceptionBoundary`, and all declared work-to-change and change-to-identity predicates or compound bases.

A published local inception claim **MUST** be indexed by the exact specification episteme and applicability basis used at `inceptionBoundary`. A later specification episteme does not silently rewrite that earlier claim. If an exact C.2.1 `EpistemeEditionRelation` connects the two specifications, the lineage can trigger refresh of a current dependent use, but the later specification still needs its own applicability basis at the boundary being judged. Without that relation, treat the later object as a non-continuing replacement and evaluate it independently. Changed applicability yields either a separately qualified claim under its new exact basis or an exact blocker; it does not move the earlier indexed boundary.

A delta expression, method description, work plan, log, post-state image, identity-rule episteme, or first observation establishes none of those links by itself. Absence of recoverable work granularity for `identityClosingWork` yields a **work-granularity blocker**. Several incomparable minimal work composites yield several local inception claims; narrative simplicity supplies no rule for selecting only one.

**Regulated-identification boundary.** A persistent identifier is not an inception criterion. A current subject practice that allocates an identifier at build or registration while keeping allocation separate from entity status supplies designation and continuity only. First existence requires a separately applicable subject-identity rule; its absence yields the exact identity-governor blocker. An assigned number does not make the candidate basis the after-side entity.

#### A.15.PROD:4.6 - Recover state satisfaction and historically indexed production completion

Completion wording often hides two claims. First ask whether the exact state-bearing subject satisfied the applicable criterion. Then ask whether the subject practice makes that satisfaction sufficient to close the exact production Work.

The **state-satisfaction claim** names:

- exact `completionSubject` whose state is judged;
- exact `completionBoundary`;
- exact `productionCompletionCriterion` episteme applicable to that subject and boundary;
- the named applicability predicate or filled local claim; and
- the actual boundary-state facts and the criterion predicate they satisfy.

When persisted, this C.2.1 episteme has `completionSubject` as its exact EntityOfConcern. It says nothing yet about whether Work is complete.

The separate **production-work-completion claim** names exact `productionWork`, the exact state-satisfaction claim, the same boundary, and the declared closure predicate or filled local A.6.RCD claim that makes this criterion satisfaction sufficient to close that Work. Its exact EntityOfConcern is `productionWork`. If no closure governor is available, keep the positive state-satisfaction claim and return `missing-governor[production-work-completion]`; do not apply a subject-state predicate to Work by metonymy.

Completion is historical. Later damage, loss, destruction, delivery, rejection, acceptance, release, publication, or unavailability does not erase an earlier true state-satisfaction or Work-completion claim. A later or replacement criterion episteme does not rewrite the earlier claim. Rework or later production Work that closes under an applicable criterion at a later boundary receives another local Work-completion claim.

Entity-identity inception, criterion satisfaction, and production-Work completion remain separate even when they share a boundary. A later evaluation-result episteme may support one of these claims under a direct evidence-use relation, but it creates neither the boundary, the subject state, nor Work closure.

Past Work and the two completion claims remain addressable after later destruction or evidence decay. A later assertion carries its own evidence currentness and reliance status. The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain objects and claims defined and tested separately.

**Practice-specific criteria stay local.** NASA systems-engineering guidance, Scrum's Definition of Done, and similar authoritative practice sources can supply a criterion for the exact subject and practice use they address. They do not by themselves identify the A.15.1 Work or state that criterion satisfaction closes it. A subject-practice closure predicate or local claim must provide that second step; transition, delivery, review, or release remains separate.

#### A.15.PROD:4.7 - Publish local claims, not an omnibus relation

The default A.6.RCD disposition is **local compound relation-bearing claim**. For an ordinary positive answer, the practitioner **MUST**:

1. name the receiving action or decision, state what it must decide, and select one production question;
2. recover the exact participants, direct predicates, applicability facts, and boundary facts needed by that question;
3. state the smallest readable conjunction of those governed facts and the one answer it supports, or return the exact missing-information, missing-governor, criterion, applicability, work-granularity, or boundary-state blocker; and
4. keep any durable answer in one truthful C.2.1 episteme with exact claim content, one exact `EntityOfConcern`, and an effective `U.ReferenceScheme`, then stop without introducing a relation kind, relation signature, or relation occurrence.

This ordinary positive branch does not require the practitioner to name a substrate document, constructor, hidden-witness policy, polarity algebra, or ordered-boundary operator. It requires the governed facts and a readable answer. Open author-side semantic replay only when A.6.RCD:4.2 requires a substrate pin—nontrivial, interoperability-facing, proof-bearing, high-consequence, or reusable use—or when the current negative claim or first-satisfying-boundary claim actually depends on negation, witness, ordering, or earliest-boundary semantics.

**Branch constructor semantics for the triggered replay.** These are branch-local claim constructors, not a universal production algebra:

| Branch | Least constructor over governed base claims | Hidden-participant, polarity, and time policy |
| --- | --- | --- |
| production-work participation | one typed conjunction over exact A.15.1 work identity, actual method enactment, method applicability and intended production effect, affected referent, direct work-to-change facts, the receiver's current criterion, and either exact work identity or one exact A.15.1 proper-part relation | every participant and conjunct remains named; no projection hides work, transformation, or criterion witnesses; a negative result requires the selected substrate's explicit negation law rather than absence of a base assertion |
| entity-identity inception | one time-indexed conjunction over identity-specification applicability, exact work and governed effects, direct work-to-change and change-to-identity links, and satisfaction of the applicable identity predicate, followed by the substrate's earliest-satisfying-boundary selection over its declared ordered candidate-boundary domain | the candidate basis remains distinct from the after-side entity; work parts and actual transformations remain named or follow the substrate's explicit witness policy; incomparable minimal work composites remain plural, and A.15.PROD supplies no arbitrary minimization rule |
| production completion | one boundary-indexed conjunction first states criterion satisfaction for exact `completionSubject`; a second conjunction states exact `productionWork`, that satisfaction claim, and the declared closure predicate or local closure rule | the claims keep their different entities of concern; no earliest-boundary operator is implied unless separately required, and missing closure semantics preserves satisfaction while blocking only Work completion |

For DPF or FPF authoring and every other pin-triggering use, the responsible author or modeler **MUST** name the exact selected substrate and edition and replay its constructor inputs, output claim, applicability, hidden witnesses, polarity law, and temporal policy. A negative or earliest-boundary claim **MUST** recover the specific negation, witness, ordering, or selection semantics it consumes even when no broader replay is needed. If no current substrate supplies semantics that the claim actually requires, return the exact **missing-substrate blocker**. A.15.PROD supplies no fallback operator.

For an ordinary positive result, the truthful `EntityOfConcern` is exact `currentWork` for production-work participation and exact `producedEntity` for entity-identity inception. Completion uses exact `completionSubject` for the state-satisfaction episteme and exact `productionWork` for a separate Work-completion episteme. A modeler **MUST** split claim content that cannot truthfully concern one exact entity and **MUST NOT** manufacture a union concern from work, method, transformations, criteria, evidence, and receivers.

Repeated use within one subject practice may justify one predicate-definition episteme, with the subject pattern locating the ClaimGraph that defines those participant meanings. Consider a subject-specific derived relation kind only when a named later action must also refer again to the same obtaining relation occurrence. The subject definition must then state obtaining, applicability, base dependencies, recurrence, and occurrence identity. A.6.RCD defines that candidate-construction branch; A.15.PROD defines no such kind admission by itself.

#### A.15.PROD:4.8 - Separate recognition from assurance

**Recognition branch for ordinary work.** The practitioner **SHOULD** ask only three questions:

1. Which is current: **did this Work count as production work, when did this exact entity first exist, or when was production completed?**
2. What happened, to which existing referent or pre-inception candidate basis, and at what boundary? If first existence is current, which entity exists only after that boundary? Name only the Work or work part, method, transformations, identity rule or completion criterion, declared predicates, applicability, and boundary facts needed to decide that question.
3. What one readable answer do those facts support, and what should the receiver do next? If one deciding fact or governor is absent, return its exact blocker instead of opening the other production questions.

A positive local answer can stop at that readable conjunction. It does not require substrate vocabulary. Open only the specific semantic replay needed when the answer is negative, when first existence requires an ordered earliest-boundary judgment, or when A.6.RCD:4.2 triggers a substrate pin. The practitioner **MUST** stop when the local answer is readable and grounded and **MUST NOT** fill the rest of this pattern as a record.

**Assurance branch for authors and high-consequence use.** Replay the exact basis in six visible groups:

- **Work and Method.** Check exact work identity and every relied-on work-part relation, the actual `enactsMethod` relation, method applicability, and the intended production effect.
- **Actual change and entity inception.** Check every work-to-change and change-to-identity predicate and retain the explicit non-inference from work or method composition to transformation composition.
- **State satisfaction and Work closure.** Check every criterion-applicability fact and boundary-state satisfaction fact. Keep the state-satisfaction claim separate from the closure predicate or local claim that closes the Work.
- **Claim epistemes and their current basis.** Check the exact identity-specification and completion-criterion epistemes, the named applicability predicate or filled local claim for each episteme at its claimed boundary, any separately current C.2.1 `EpistemeEditionRelation`, C.2.1 identity, and the evidence-use relations actually relied on.
- **Positive and discriminating cases.** Replay both, so removal of one deciding fact blocks only the claim that consumes it.
- **Pinned author substrate.** When A.6.RCD:4.2 requires a pin, DPF and FPF authors **MUST** record the selected substrate and edition and expose direct base predicates, applicability, hidden participants, polarity law, boundary domain and ordering, witness policy, and every earliest-boundary rule used by the claim.

Assurance may warrant reliance on the claim; it does not constitute work, change, entity inception, or completion.

**Assurance scope by use.** Match the replay to the actual use:

- A modeler whose declaration or model carries one local claim **MUST** check exact claim content, one truthful `EntityOfConcern`, reference scheme, participants, declared predicates, polarity, and boundary indexing.
- A practitioner or conformance reviewer **MUST** verify that the three-question first move reaches either one grounded local answer or one exact blocker and then stops.
- A pattern author or reviewer **MUST** also replay the worked and discriminating cases, neighbor-authority boundaries, checklist, and no-mint disposition.

None of these assurance uses widens the recognition claim or adds a world-side production fact.

#### A.15.PROD:4.9 - Run the recovery sequence and stop deliberately

**Ordinary sequence.** The practitioner **MUST** stop at the first grounded answer or exact blocker:

1. name the receiving action or decision and select one production question; if several are current, handle them one at a time as separate claims;
2. recover only the exact Work, work-part, method, affected-referent, transformation, identity-specification or completion-criterion, applicability, and boundary facts needed by the selected question;
3. select the whole-work or proper-part branch when production-work participation is current;
4. state one readable conjunction and its positive answer, or return the exact blocker naming the missing fact, governor, applicability basis, criterion, work granularity, or boundary state; and
5. if another person, tool, or later decision must reuse the answer, publish it as one local C.2.1 claim episteme; otherwise keep the readable answer local, then stop. Open delivery, acceptance, release, publication, availability, result, evidence, assurance, or relation-kind questions only when the named action or decision asks one of them; none follows from the production answer.

**Triggered author replay.** Continue beyond the ordinary sequence only for an A.6.RCD:4.2 pin-triggering use or when a negative or earliest-boundary answer consumes additional semantics:

6. name the branch-local constructor and, when a pin is required, the exact substrate and edition; expose only the constructor inputs, applicability, hidden-participant or witness policy, polarity law, boundary domain and ordering, and temporal rule that can change this answer;
7. for entity inception, verify the ordered candidate-boundary domain and earliest-satisfying rule; for a negative claim, verify the applicable negation law; for completion, keep the claim indexed by its criterion, applicability basis, and boundary;
8. if one required operator or substrate is unavailable, return the exact missing-substrate blocker rather than lowering the absence to a negative production answer; and
9. stop after the author replay returns the same ordinary answer or blocker.

#### A.15.PROD:4.10 - Pattern NameCard

This NameCard names the recovery pattern, not a relation kind. It uses F.18's expanded identity-bearing form with a direct local-sense claim because no separately recoverable F.17 SenseCell is current for this local naming settlement:

```text
NameCard:
  NameCardId: NC-A15-PROD-PATTERN
  GovernedValueRef: the A.15.PROD pattern that separates and recovers production-work participation, entity-identity inception, and production-completion claims
  SubjectPatternLocator: A.15.PROD
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-A15-PROD-PATTERN.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseRef: local expression `Production Work, Entity-Identity Inception, and Production Completion Recovery`; sense claim: the A.15.PROD recovery pattern asks which of the three production questions is current while keeping actual work, first existence, completion, delivery, acceptance, release, publication, and availability distinct under FPFCoreReferenceScheme
  TechLabel: Production Work, Entity-Identity Inception, and Production Completion Recovery
  PlainLabel: separate production work, when this exact entity first exists, and when production was completed
  CandidateSet: Production Work, Entity-Identity Inception, and Production Completion Recovery; Entity Production by Work; Entity-Identity Inception Through Work; Production Boundary Recovery
  CandidateCoverage: recovery-pattern, entity-production, entity-inception, and boundary-recovery head families; no plausible current family remains untested
  RejectedCandidates:
    Entity Production by Work: hides whether the claim concerns work participation, first existence of the entity, or completed production
    Entity-Identity Inception Through Work: omits production work before and after first existence and omits production completion
    Production Boundary Recovery: uses a generic boundary head and does not expose the three governed questions
  SelectionRationale: the selected title names the three distinctions that the pattern must recover and makes the completion kind explicit; it cannot be parsed as one binary or ternary production relation
  LineageEntries: initial durable settlement; the selected Tech and Plain labels are current; this card asserts no alias, rename, split, merge, or retirement
  RefreshCondition: reopen naming if repeated subject use justifies an admitted derived relation kind or one question needs a separate primary EntityOfConcern and recovery algorithm
```

### A.15.PROD:5 - Archetypal Grounding

#### A.15.PROD:5.1 - Car 42 and the required nut

**Identity boundary.** Car 42 already satisfies its identity rule before `NutFasteningWork-42`.

**Assignment declaration.** `Car42FasteningAssignmentSpecies` is a directly declared `U.SystemRoleAssignment` species. Its ordered participant positions are holder and assigned system-role kind; their domains are `U.System` and `Car42FasteningPerformerSystemRoleKindDomain`.

**Assignment occurrence rule.** The species applies to Car-42 fastening Work and says that its holder supplies the fastening contribution as `Car42FasteningPerformerSystemRole` throughout the declared interval. Holder, assigned-kind value, and that uninterrupted interval identify one occurrence.

**Work and Method basis.** Obtaining occurrence `Car42FasteningAssignment-42` fixes `FasteningCell-7 : U.System` and `Car42FasteningPerformerSystemRole` and covers the whole Work interval. F.6 says that `NutFasteningWork-42` was performed under that occurrence, and the Work enacts the exact fastening Method.

**Actual-change basis.** A.3.4 separately identifies `Car42FastenerAttachmentTransformation`. It concerns the same continuing car and does not bring Car 42 into existence.

**Whole-work branch for the narrow use.** `NutFasteningWork-42` can be the whole `productionWork` when its fastening method is applicable and `FasteningWorkChangedAttachment@Car42(work, transformation)` obtains for that Work and `Car42FastenerAttachmentTransformation`.

**State satisfaction.** At the fastening boundary, `Car42FinishingStateSatisfactionClaim` has exact EntityOfConcern `Car42` and states that the car satisfies `Car42FinishingCriterion-v1`.

**Work closure.** Separately, subject-bounded `Car42FasteningClosureRule-v1` supports `Car42FasteningWorkCompletionClaim`, whose EntityOfConcern is `NutFasteningWork-42`, because the required attachment state is satisfied and no required fastening activity remains for this narrow use.

**Wider-work contrast.** For the broader factory use, the same occurrence can be a proper operational part of `CarProductionWork-42` under an exact A.15.1 part relation. The verb *fasten* and narrative order decide none of these claims.

**Cold-practitioner replay.** Ask only whether `NutFasteningWork-42` completed the narrowly bounded fastening:

- the exact assignment and F.6 relation ground the performer side;
- the Work-to-change predicate connects the Work to the attachment change;
- the car satisfies the finishing criterion; and
- the separate closure rule makes that satisfaction sufficient to close the Work.

The readable answer is: **this Work completed the required fastening for this use; it did not bring Car 42 into existence**.

The nearest blockers remain separate:

- Missing Work-to-change semantics returns `missing-governor[CAR42-FASTENING-WORK-TO-CHANGE]`.
- Missing closure semantics preserves the state-satisfaction claim and returns `missing-governor[CAR42-FASTENING-WORK-COMPLETION]`.

**Author-side replay of the same result.** `Car42FasteningPredicates-v1` declares the Work-to-change predicate, and the fixture supplies its obtaining facts. `Car42-Claims-v2` separately constructs the state-satisfaction claim and the Work-completion claim under `Car42FasteningClosureRule-v1`; it does not apply the car-state predicate to Work.

- Removing the Work-to-change fact blocks the first chain.
- Removing only the closure rule leaves the car-state claim true and blocks only Work completion.

These case-local semantics introduce no universal production or completion relation kind.

#### A.15.PROD:5.2 - Incomplete but identifiable Ship 27

**Identity rule and applicability.** Exact ship-identity specification episteme `SHIP-ID-2` states the hull-closure rule. Local applicability claim `ShipIdentitySpecApplies-2` applies it to exact candidate hull basis `Ship27-HullBasis`, exact yard context `Yard-27`, and the ordered candidate boundaries ending at `inceptionBoundary`.

**Entity inception before later Work ends.** Exact hull-assembly work can close that specification's rule at `inceptionBoundary` while outfitting, software installation, trials, and commissioning continue. The resulting inception claim concerns when Ship 27 first exists and remains indexed by `SHIP-ID-2` and `ShipIdentitySpecApplies-2`.

**Continuing edition — assignment declaration.** `ShipIdentityRuleRevisionAssignmentSpecies` is a directly declared `U.SystemRoleAssignment` species. Its ordered positions are holder and assigned system-role kind, with holder domain `U.System` and assigned-kind domain `ShipIdentityRuleReviserSystemRoleKindDomain`.

**Continuing edition — assignment predicate.** The predicate applies to ship-identity revision Work in `Yard-27` under `ShipIdentityRuleRevisionMethod`. It obtains when the holder supplies that revision contribution throughout the declared interval. Holder, assigned-kind value, `Yard-27`, and that uninterrupted interval identify one occurrence.

**Continuing edition — Work and Method.** Obtaining occurrence `ShipIdentityRuleReviserAssignment-2R` fixes holder `YardIdentityGovernanceSystem` and assigned-kind value `ShipIdentityRuleReviserSystemRole` from that domain. It covers the full extent of `ShipIdentityRuleRevisionWork-2R`; F.6 says that the Work was performed under it, and the Work enacts that Method.

**Source expression and predicate.** C.2.P recovers the source expression *hull assembly closes Ship 27 identity* in `SHIP-ID-2`. Predicate-definition episteme `YardRevisionSourceUsePredicates-v1` declares case-local predicate `usesAsRevisionSource(work, sourceEpisteme)` with participant order `<revision Work, source episteme>`.

**Source-use obtaining test.** The predicate applies only to ship-identity revision Work under `ShipIdentityRuleRevisionMethod`. It is true only when that Method application opens the source episteme and uses the selected source claim as a premise.

**Edition basis.** The exact source-use participants are `ShipIdentityRuleRevisionWork-2R` and `SHIP-ID-2`. The revision Work opens `SHIP-ID-2`, selects its hull-closure claim as an explicit premise, and produces `SHIP-ID-2R`, whose separate C.2.1 ClaimContent says that hull assembly plus installed propulsion closes Ship 27 identity. Those facts make `usesAsRevisionSource(ShipIdentityRuleRevisionWork-2R, SHIP-ID-2)` obtain.

The applicable continuity rule for this specification family requires exact use of `SHIP-ID-2`, preservation of the ship EntityOfConcern and listed identity claims, and explicit identification of the corrected claim content without a reference-scheme retargeting. The current source use and preserved and deliberately changed features satisfy that rule, so `ShipIdentitySpecEdition-2-to-2R : EpistemeEditionRelation` obtains for `SHIP-ID-2` and `SHIP-ID-2R`. The performer, Method, Work, provenance, and replacement facts supply evidence for the test; no label makes continuity true. The lineage carries forward neither old applicability nor a new inception boundary.

**Lineage blockers.** Keep the two failures distinct:

- If the source-use predicate is not defined, return `missing-governor[SHIP-IDENTITY-REVISION-SOURCE-USE]`.
- If its definition is current but the actual premise-selection facts cannot be recovered, return `missing-information[SHIP-IDENTITY-REVISION-SOURCE-USE]`.

Either result keeps `SHIP-ID-2R` usable as a separately identified specification episteme but blocks `ShipIdentitySpecEdition-2-to-2R`. A similar title, later date, common publisher, or bare provenance edge does not restore that lineage.

**Non-continuing replacement.** `SHIP-ID-3` is another exact specification episteme, but this fixture establishes no `EpistemeEditionRelation` from `SHIP-ID-2` or `SHIP-ID-2R` to it. A later date, similar ship terminology, and use by the same yard do not make it an edition. A use selecting `SHIP-ID-3` must establish its applicability independently and publish a separately qualified claim or exact blocker; lineage-based refresh cannot substitute it for either earlier specification.

The continuing edition reopens dependent current uses through the named lineage. The non-continuing replacement opens a new applicability question without altering earlier claims.

**Author-side substrate.** Exact substrate edition `YardIdentityHistory-v3` defines time-indexed conjunction over the named work, applicability, actual-effect, work-to-change, change-to-identity, and identity-satisfaction claims. It also defines earliest selection over its declared ordered candidate-boundary domain.

The positive replay returns exact boundary `tI` because `SHIP-ID-2` is false at every earlier candidate boundary and true at `tI`. Exact work and transformation witnesses remain named.

**Nearest substrate failure.** A snapshot substrate can conjoin facts at `tI` but supplies no ordered boundary domain or earliest-selection law. It cannot establish inception even if a later image satisfies the rule, so the branch returns the exact missing-substrate blocker rather than treating first observation as first existence. The example adds no universal earliest operator or arbitrary minimal-work selection.

**Designation is not identity.** An IMO ship identification number may designate Ship 27 and remain stable across later flag, name, ownership, or type changes. The current IMO integrated scheme nevertheless states that number allocation does not define ship status.

The number therefore supports regulated designation and continuity only; it neither supplies `SHIP-ID-2` nor proves `inceptionBoundary`. If the receiving use cannot recover a separate applicable ship-identity rule, the inception branch returns the exact identity-governor blocker.

**Larger Work.** A larger exact production-work occurrence contains the identity-closing and later Work through declared A.15.1 part relations.

**State satisfaction.** At `completionBoundary`, one claim may state that Ship 27's actual state satisfies the applicable completion criterion.

**Work closure.** A separate yard closure predicate or local claim must connect that satisfaction to completion of the larger production Work. Without it, preserve the state claim and return `missing-governor[SHIP27-PRODUCTION-WORK-COMPLETION]`.

Delivery, class acceptance, and operational release remain separate. The sentence `the yard produced Ship 27` is admissible only after the writer selects Work participation, first existence, state satisfaction, or Work completion.

#### A.15.PROD:5.3 - Nested and concurrent attribution

**Work structure.** Factory work may contain project work, subassembly work, `identityClosingWork`, and completion-closing work. Every selected work-part relation remains explicit. Jointly necessary concurrent work parts use exact composite work under A.15.1.

**Plural minimal composites.** Two incomparable minimal work composites yield two local inception claims, each indexed by its exact identity-specification episteme and applicability basis. Nested or concurrent attribution creates no additional inception occurrence, and none of those work compositions establishes transformation composition.

**Epistemic basis remains separate.** The identity-specification and completion-criterion epistemes remain cited by the local claims. Each applicability basis remains its named predicate or filled local claim, and any C.2.1 edition relation between such epistemes is separate. None is a work participant.

#### A.15.PROD:5.4 - Pressure adjustment without entity inception

**Work, Method, and change.** A dated pressure-adjustment Work occurrence may enact an exact pressure-adjustment method, while A.3.4 independently identifies a pressure transformation.

**Work-to-change claim.** Open a positive claim only when the subject practice supplies a named predicate with Work and transformation participant positions and the case facts make that predicate obtain. Otherwise keep the two occurrences separate and return `missing-governor[pressure-work-to-change]`.

**Stop.** If the affected vessel or process already exists and no production-completion criterion is current, even the positive route closes as work plus actual change, not as production work, entity inception, or completion.

#### A.15.PROD:5.5 - PumpSkid assembly before PumpSkid identity

**Actual Work and change.** Mounting, wiring, fluid-connection, and whole-configuration changes may each be independently identified under A.3.4, and exact work parts may be grounded under A.15.1.

**Inception basis.** A PumpSkid inception claim may proceed only when a named applicability predicate or filled local claim applies the exact PumpSkid identity-specification episteme to the candidate configuration and boundary. Named Work-to-change and change-to-identity predicates must also obtain for the actual participants and case facts. A missing applicability or link returns its exact blocker.

**Transformation-composition boundary.** A claim that additionally requires positive composite-transformation identity or transformation parthood stops at `missing-governor[transformation-composition]`. Work or method decomposition supplies no proof of transformation decomposition.

#### A.15.PROD:5.6 - Completion persists after later destruction

**Historical positive case.** The product's state satisfied criterion episteme `PC-3` at boundary `tC`, and the subject-practice closure rule made that satisfaction sufficient to close the named production Work.

`CompletionHistory-v1` keeps the Work identity, applicability of `PC-3`, subject-state facts at `tC`, state-satisfaction claim, and separate Work-completion claim explicit. The two claims keep their different entities of concern. The history uses the declared boundary and does not apply an earliest operator. A later accident destroyed the product but did not rewrite either historical claim.

**Nearest historical failure.** Keep the later certificate or an unindexed current-state predicate, but remove the semantics that say the subject satisfied `PC-3` at `tC`. That material cannot move satisfaction or Work completion to the certificate or current state; it returns the exact missing-substrate blocker for the historical claim.

If only the closure rule is missing, the state-satisfaction claim remains and only Work completion returns its exact missing governor. Current evidence, availability, replacement Work, acceptance status, and insurance decisions remain separate.

#### A.15.PROD:5.7 - Non-agentive biological synthesis

**Actual transformation.** A spontaneous reaction or biological growth process may be independently grounded as one or more actual transformations under A.3.4. The transformed biological, chemical, or physical referent may itself be a `U.System`; that fact neither makes it the performer nor supplies production work.

**Performer-side requirement.** A.15.PROD opens a production-through-Work claim only when all of the following are grounded:

- an exact performing System holds the performer position in an obtaining occurrence of an exact directly declared `U.SystemRoleAssignment` species;
- the Work has the F.6 attribution; and
- one dated Work occurrence admitted under `U.Work` enacts an applicable Method.

When that basis is absent, retain the transformed referent and transformations. Evaluate entity identity only with the biological practice's named identity predicate; if no such predicate is available, return the exact identity-governor blocker. `Batch B17`, a sample label, first observation, or process record supplies none of the performer-side basis, work identity, or production attribution.

**Fixture result.** This case stipulates no exact biological production assignment species or obtaining occurrence. The production-through-Work branch therefore remains blocked.

The branch may open only when the subject practice supplies all of the following:

- a directly declared species with participant meanings, assigned system-role-kind domain and value, predicate, and applicability;
- an exact obtaining occurrence with the performer System as holder and a covering interval;
- F.6 attribution; and
- actual Method enactment.

Entity inception and completion then still need their own exact identity, state-satisfaction, and Work-closure governors. Do not turn observed growth into the missing performer-side basis.

#### A.15.PROD:5.8 - Scrum Increment before review or release

**Product-state and identity basis.** The Scrum Guide and one exact organizational Definition of Done episteme are authoritative practice sources for this bounded software-product use. When `PBI-84` first satisfies that criterion at `tD`, the local product-state and Increment-identity claims may be stated under their exact applicability rules. Work that does not meet that Definition of Done is not part of the Increment.

**Review and release stay separate.** Multiple Increments may exist before Sprint Review, and review is not a release gate.

**Current A.15.PROD use.** The pattern may use the applicable Definition of Done for the state-satisfaction or identity question it actually answers, while keeping Sprint Review, delivery, and release separate.

**Work-completion boundary.** The guide does not identify exact A.15.1 Work, its performer basis, or a local predicate that makes satisfaction close that Work. A Work-completion claim therefore needs an additional subject-practice closure governor. Otherwise keep the product-state claim and return the exact Work-completion blocker.

#### A.15.PROD:5.9 - ReleaseBinary 12: complete build-to-inception replay

BuildOps asks one question: **when did exact `ReleaseBinary_12` first exist?** Verification, transfer, release, deployment, publication, and availability are not part of this answer. The fixture uses one affected referent and one transformation; it does not hide an unnamed effect chain.

| Needed fact | Exact case fact |
| --- | --- |
| Work, performer, and method | A.15.1:6.7.1 supplies the complete A.15.1/F.6 basis for `ReleaseBinary12_BuildWork_2026-07-21T0900_0912 : U.Work`: `BuildRunner_A : U.System`, the exact direct assignment species and its obtaining occurrence `BuildRunnerAssignment_2026-07-21`, F.6 attribution, enacted method `ReproducibleBuild@BuildOps-v12`, interval 09:00–09:12, and the obtaining `BuildWorkOccursWithinServiceBoundary` relation to `BuildService_A`. The enacted method states the intended effect of producing an immutable binary. Method-applicability claim `ReproducibleBuildApplies-12` applies that method to exact build input and configuration `BuildInputSet_12`. |
| Application and candidate basis | After the produced entity exists, A.6.1 application `BuildApplication_12` has result binding `builtBinary -> ReleaseBinary_12`; that binding designates the returned entity but establishes neither its inception nor its boundary. The same identified application is an application of declared operation `storeWrite@BuildOps-v12` and has argument binding `storeTarget -> ArtifactStorePartition_12`; A.15.1:6.7.1 uses this application and binding in the obtaining test for the named Work-to-transformation predicate below. Before inception, `BuildOutputBasis_12` designates the candidate bytes, manifest, digest, and their positions in that partition, not a surrogate future binary. |
| Actual transformation | A.3.4 independently identifies the one transformation consumed here: `ArtifactStorePopulationTransformation_12 : U.Transformation`, the change of `ArtifactStorePartition_12` from no complete candidate tuple at 09:00 to the written bytes, manifest, and digest at 09:11, after which that tuple remains fixed through build completion at 09:12. |
| Work to change | A.15.1:6.7.1's BuildOps relation specification declares `BuildWorkPopulatedStore@BuildOps-v12(work, transformation)` with participant order `<work, transformation>`. Its stated test and the stipulated Work, application, target-binding, and transformation facts make `BuildWorkPopulatedStore@BuildOps-v12(ReleaseBinary12_BuildWork_2026-07-21T0900_0912, ArtifactStorePopulationTransformation_12)` obtain. Shared timing or the result binding alone would not establish this predicate. |
| Identity criterion and applicability | Predicate-definition episteme `ReleaseBinaryIdentitySpec_v12` says that this BuildOps binary exists when one immutable byte sequence, manifest, and digest are fixed together and addressable by that digest in `ArtifactStorePartition_12`. Applicability claim `ReleaseBinaryIdentitySpecApplies-12` applies that episteme to `BuildOutputBasis_12`, the BuildOps-v12 context, and the ordered candidate boundaries from 09:00 through 09:12. This is the criterion episteme for the selected inception question; `BuildCompletionCriterion_v12` belongs to the separate completion question at 09:12. |
| Change to identity | BuildOps predicate-definition episteme `ReleaseBinaryIdentityPredicates-v12` declares case-local predicate `StorePopulationClosedBinaryIdentity@BuildOps-v12(transformation, identitySpecification, candidateBasis, boundary, producedEntity)` with that participant order. Its test requires the governed store change to make the applicable identity rule false at every earlier candidate boundary and true at the named boundary. The stipulated case facts make it obtain for `<ArtifactStorePopulationTransformation_12, ReleaseBinaryIdentitySpec_v12, BuildOutputBasis_12, 09:11, ReleaseBinary_12>`. |
| Local result | C.2.1 episteme `ReleaseBinary12InceptionClaim` has exact `EntityOfConcern = ReleaseBinary_12` and states only that this entity first exists at 09:11 through the governed effects of `ReleaseBinary12_BuildWork_2026-07-21T0900_0912` under `ReleaseBinaryIdentitySpec_v12` and `ReleaseBinaryIdentitySpecApplies-12`. It asserts neither build completion nor verification, transfer, acceptance, release, deployment, publication, or availability. |

**Ordinary replay.** The runner performed the named Work under the applicable build method. The named work-to-change predicate connects that Work to the store-population transformation. The named change-to-identity predicate says that this transformation made the applicable binary-identity rule become true first at 09:11.

The readable answer is: **`ReleaseBinary_12` first exists at 09:11 through this build Work; decide completion and later uses separately.**

**Nearest failing variant.** Keep every fact above, including the result binding, store transformation, work-to-change predicate, identity specification, applicability, ordered boundaries, and the state that satisfies the identity rule at 09:11. Remove only the declaration and obtaining fact for `StorePopulationClosedBinaryIdentity@BuildOps-v12`.

The exact result is `missing-governor[RELEASE-BINARY-CHANGE-TO-IDENTITY]` for `<ArtifactStorePopulationTransformation_12, ReleaseBinaryIdentitySpec_v12, BuildOutputBasis_12, 09:11, ReleaseBinary_12>`. A timestamp, completed write, or `builtBinary` binding cannot replace that missing change-to-identity predicate.

**Author-side replay of the same result.** Case substrate `ReleaseBinaryInceptionClaims-v1` defines a time-indexed conjunction over the named Work, performer basis, method applicability, the performed `storeWrite` application fact (not the later result binding), affected referent, transformation, work-to-change predicate, identity specification, applicability claim, and change-to-identity predicate.

Its declared ordered boundary domain is 09:00-09:12, and its earliest-satisfying rule returns 09:11. The positive replay therefore yields `ReleaseBinary12InceptionClaim`.

In the failing variant, the same constructor lacks exactly the change-to-identity conjunct and returns `missing-governor[RELEASE-BINARY-CHANGE-TO-IDENTITY]`, exactly as the ordinary replay does. These case-local predicates and this substrate introduce no universal production, work-to-change, or change-to-identity relation kind.

### A.15.PROD:6 - Bias-Annotation

**Scope limitation and five-lens coverage.** These annotations cover the three production-recovery branches and their named neighboring claims; they do not classify production language outside a current A.15.PROD use. `Gov` covers criterion, applicability, and historical-authority errors; `Arch` covers branch, neighboring-pattern, and omnibus-relation errors; `Onto/Epist` covers work, change, entity, claim, record, and publication distinctions; `Prag` covers receiver-first selection, useful stops, and exact blockers; and `Did` covers the familiar verbs, visible final steps, labels, and records that make the overreads plausible.

| Bias | Countermeasure |
| --- | --- |
| Verb bias | The countermeasure treats *make*, *produce*, *build*, *finish*, and *complete* as retrieval cues and selects one of the three questions by exact facts. |
| Record bias | The countermeasure keeps plans, logs, pictures, tickets, certificates, and publications as epistemic or publication objects until direct relations connect them to work, change, identity, or completion. |
| Final-step bias | The check rejects creation by last-visible-step order and replays the exact applicable identity-specification episteme, its direct applicability basis, and the exact work effects. |
| Container bias | A project, factory, batch, case, or common referent supplies no proof of work parthood or production attribution. |
| Composition bias | Work parts, method parts, samples, and flow structure supply no transformation-part inference. |
| Present-state bias | The check evaluates completion at its historical boundary under the exact criterion episteme used there, not only from the entity's current state. |
| Universal-relation bias | The countermeasure prefers the local compound claim that answers the receiver over a broad production relation name. |

### A.15.PROD:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A15.PROD-1` | The receiving use selects production-work participation, entity-identity inception, production completion, or an explicit subset; one question's evidence is not used as another's answer. |
| `CC-A15.PROD-2` | `currentWork` and `productionWork` designate exact A.15.1 Work occurrences admitted under `U.Work`, not plans, labels, projects, methods, logs, publications, or records that describe those occurrences. |
| `CC-A15.PROD-3` | The whole-work branch names actual `enactsMethod`, method applicability and intended production effect, affected referent, exact work-to-change facts, and the criterion current for the receiver. |
| `CC-A15.PROD-4` | The proper-part branch names an exact A.15.1 work-part relation and gives the containing work the same grounding required by the whole-work branch. |
| `CC-A15.PROD-5` | Every actual transformation is independently identified under A.3.4; work, method, samples, temporal subdivision, and flow representations do not imply transformation composition. |
| `CC-A15.PROD-6` | Every Work-to-change and change-to-identity link names a declared predicate with participant order and obtaining facts or a filled local A.6.RCD claim. Completion separately names the criterion-satisfaction predicate for `completionSubject` and the closure predicate or local claim for `productionWork`; neither substitutes for the other. |
| `CC-A15.PROD-7` | Exact `productIdentitySpecification` is available before inception without a surrogate future `producedEntity`; a named applicability predicate or filled local claim applies it to the candidate basis, subject context, and exact `inceptionBoundary`, and the entity is designated only after that exact applicable specification's rule first holds. Any claim that it is an edition of another specification names an obtaining C.2.1 `EpistemeEditionRelation`. |
| `CC-A15.PROD-8` | A positive inception claim satisfies `A15PROD-D1` and names exact `identityClosingWork`, exact `productIdentitySpecification`, its named applicability predicate or filled local claim, exact `inceptionBoundary`, exact `producedEntity`, and first satisfaction of that exact applicable specification's rule. |
| `CC-A15.PROD-9` | Concurrent or nested identity-closing work is composed only through exact A.15.1 work-part relations; incomparable minimal composites remain plural, and each local inception claim retains its exact identity-specification episteme and applicability basis. |
| `CC-A15.PROD-10` | A completion use first names exact `completionSubject`, criterion episteme, applicability, boundary-state facts, and state-satisfaction predicate. A separate Work-completion claim names exact `productionWork` and the closure predicate or local claim that makes that satisfaction sufficient to close it. Missing closure semantics blocks only Work completion. |
| `CC-A15.PROD-11` | Later criterion epistemes, damage, loss, delivery, acceptance, release, publication, and availability do not rewrite historical state-satisfaction or Work-completion claims. Rework or another closure under another criterion and boundary receives new claims. |
| `CC-A15.PROD-12` | Each local assertion is one C.2.1 episteme with one truthful exact `EntityOfConcern`, claim content, effective reference scheme, and decided positive or negative polarity; no union concern is manufactured, and unresolved information sufficiency or reliance remains separately evaluated. |
| `CC-A15.PROD-13` | An unresolved basis is returned as the exact missing-governor, work-granularity, criterion, applicability, boundary-state, or transformation-composition blocker, not as a third predicate value. |
| `CC-A15.PROD-14` | The current no-mint result introduces no universal production relation kind, `U.ProductionWork`, relation signature, or relation occurrence and asserts no universal reducibility. A later subject-specific candidate requires A.6.RCD only when a named later action must reidentify the same obtaining relation occurrence; its definition states obtaining, applicability, base dependencies, recurrence, and occurrence identity. A primitive candidate additionally demonstrates failed lossless derivation, one action-facing distinction every accepted derivation loses, and independent receiving uses. |
| `CC-A15.PROD-15` | Recognition and assurance remain separate; evidence and evaluation may support the claim but create none of work, transformation, entity inception, or completion. |
| `CC-A15.PROD-16` | The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain distinct; each positive claim names its declared predicate or its own subject pattern, and a missing predicate returns the corresponding blocker. |
| `CC-A15.PROD-17` | A practice-specific source is used only for the branch question it answers: a stable identifier does not establish entity status or inception; a systems-engineering realization criterion does not collapse transition into completion; and a Scrum Definition of Done does not supply work identity, effects, review, or release. |
| `CC-A15.PROD-18` | An ordinary positive local claim names its governed base facts, common applicability, readable conjunction, answer, and stop without requiring a substrate document. A DPF/FPF-author, nontrivial, interoperable, proof-bearing, high-consequence, or reusable use pins the exact selected substrate and edition and replays constructor semantics. A negative or earliest-boundary claim exposes the specific polarity, witness, boundary-domain, ordering, or selection law it consumes. An unavailable required operator returns the exact missing-substrate blocker. |

### A.15.PROD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Every work-caused transformation is production | Modification of a continuing entity is treated as entity creation or completed production. | The repair first recovers work plus actual change and opens only the production question needed by the receiver. |
| The final visible step created the product | Narrative order substitutes for first satisfaction of the exact applicable identity-specification episteme. | The repair recovers exact `identityClosingWork`, actual effects, the specification episteme, its named applicability predicate or filled local claim, and the earliest satisfying boundary. |
| Plan or log as production work | Intended or recorded material is treated as the dated occurrence. | The repair recovers exact A.15.1 work and relates plan, log, and evidence separately. |
| Shared label as work parthood | Two occurrences called *assembly* are treated as parent and part. | The repair states the exact A.15.1 work-part relation or keeps the occurrences separate. |
| Work parts imply transformation parts | Composite work is used as proof of a composite transformation. | The repair keeps transformations independently identified and returns the missing transformation-composition governor when needed. |
| Completion equals acceptance | A satisfied production criterion is replaced by a customer's or regulator's later verdict. | The repair publishes completion at its boundary and governs acceptance separately. |
| Current damage erases completion | Present nonconformance is used to deny an earlier satisfied criterion. | The repair indexes completion by occurrence, exact criterion episteme, applicability basis, boundary, and boundary state and records the later transformation separately. |
| One omnibus production episteme | Work, inception, completion, delivery, and evidence are put into one claim with a union concern. | The repair splits one local C.2.1 episteme per selected question and direct neighboring claim. |
| Relation-name escalation | Familiar production wording is promoted to a universal relation kind. | The repair stops at A.6.RCD disposition 2 unless repeated subject semantics and occurrence identity independently justify continuation. |

### A.15.PROD:9 - Consequences

| Benefits | Trade-offs and mitigations |
| --- | --- |
| Production attribution becomes replayable at exact work boundaries. | More than one local claim may replace one familiar sentence; the three-question first move keeps ordinary use short. |
| Entity first-existence and production completion no longer overwrite each other. | The added cost is one exact identity-specification or completion-criterion episteme and its applicability basis for each current claim; name a separate C.2.1 edition relation only when lineage is current. Reuse the specification episteme already identified by the subject pattern instead of copying it. |
| Narrow and containing production work can coexist without a new kind. | Absence of exact work mereology yields an unresolved work-granularity blocker. |
| Historical completion survives later change while current evidence remains refreshable. | Boundary truth and present reliance stay separate; direct evidence and refresh patterns define or constrain current reliance. |
| Missing transformation composition no longer blocks independent production claims. | A composition-dependent claim stops at an explicit blocker; independently identified transformations and exact blockers remain useful results. |

### A.15.PROD:10 - Rationale

In the selected cases and declared receiving uses, no need for a universal production relation kind has been demonstrated. Each current question closes through declared predicates, the case facts that make them obtain, and one branch-local claim or exact blocker. This is a bounded current parsimony result, not proof that every production relation is reducible or that no irreducible production-relation fact can occur in another subject practice. The bases vary across manufacturing, construction, biology, software, formal work, and epistemic production; local compound claims preserve those subject differences and expose a missing predicate instead of hiding it behind a broad relation name.

A later subject practice reopens A.6.RCD when several named claims reuse the same participant meanings or when a named later action must refer again to the same obtaining relation occurrence. Repeated predicate use alone stops at a reusable predicate-definition episteme. A derived-kind candidate additionally states obtaining, applicability, base dependencies, recurrence, and stable relation-occurrence identity. A primitive candidate additionally requires failed lossless derivation, one action-facing distinction lost by every accepted derivation, and independent receiving uses. A.15.PROD records the present no-mint disposition but neither forbids nor pre-admits a later subject-specific derived or primitive relation kind.

The three-question split also preserves time correctly. Work may begin before an entity exists and continue after it first exists. Completion may occur at inception or later. Delivery, acceptance, release, publication, and availability may occur later still. Keeping each boundary and criterion separate gives practitioners useful historical claims without treating every neighboring event as part of production identity.

### A.15.PROD:11 - SoTA-Echoing

Scrum, NASA systems-engineering guidance, and IMO regulation are authoritative practice or regulatory sources for their named local questions. They are not treated here as SoTA merely because they are official or widely used. Manufacturing-information, product-information lifecycle, event-log, constructional-ontology, and provenance sources remain bounded comparators. None supplies a universal production ontology or a cross-domain answer to every A.15.PROD branch.

**FPF synthesis scope.** The three-question decomposition is an FPF-scoped architectural hypothesis for receiver-specific production recovery. The reviewed source set contains no independent best-known comparison that would justify calling Scrum, NASA, or IMO a SoTA answer to the cross-domain architecture. Their rows constrain only their named practice questions. The whole-to-proper-part and Work-closure architecture remains a bounded FPF hypothesis built from exact Work identity, direct predicates, state-satisfaction claims, and subject-practice closure rules. A later best-known comparison can reopen only the affected branch.

| Source, named branch question, and classification | Exact answer carried into A.15.PROD | Adoption status and blocked overread |
| --- | --- | --- |
| Schwaber and Sutherland, [*The Scrum Guide*](https://scrumguides.org/scrum-guide.html), official edition 2020. **Authoritative practice source for the bounded Scrum question.** | The guide makes the applicable Definition of Done the quality-state criterion, says that an Increment is born when a Product Backlog item meets it, excludes work that does not meet it, permits multiple Increments before Sprint Review, and says that review is not a release gate. The guide does not identify exact Work or provide the subject-practice rule that closes Work. | **Adopt for this bounded practice question, not as SoTA or a cross-domain production rule.** The Definition of Done supplies only the branch-specific criterion; a Sprint, backlog item, Increment label, review, or release supplies neither the exact A.15.1 Work, its performer and effects, nor a universal production rule. |
| NASA [NPR 7123.1D, *Systems Engineering Processes and Requirements*](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter3) and the official [NASA Systems Engineering Handbook product-realization guidance](https://www.nasa.gov/reference/5-0-product-realization/). **Authoritative agency practice source family for its tailored realization question.** | The sources distinguish implementation or integration, verification, validation, and transition. The handbook also keeps a validated end product separate from its later transition to the next product layer or user. They do not identify the exact local Work or make criterion satisfaction close that Work. | **Adopt for the named NASA practice branch, not as SoTA or a universal completion rule.** The tailored product-layer success, verification, or validation criterion can supply a local state-satisfaction basis; a validation report, transition record, or delivery is not the world-side boundary or the separate Work-closure governor. |
| IMO [Resolution A.1215(34), *Integrated IMO Identification Number Scheme*](https://wwwcdn.imo.org/localresources/en/OurWork/IIIS/Documents/A%2034-Res.1215%20-%20INTEGRATED%20IMO%20IDENTIFICATION%20NUMBER%20SCHEME%20%28Secretariat%29.pdf) and [Circular Letter No.5096](https://wwwcdn.imo.org/localresources/en/OurWork/IIIS/Documents/Circular%20Letter%20No.5096%20-%20Implementation%20of%20Resolution%20A.1215%2834%29%20-%20IMO%20Integrated%20Identification%20Number%20Scheme%20%28Secretariat%29.pdf). **Authoritative regulatory source family for ship designation.** | The current scheme allocates an identifier at build or first registration, keeps it unchanged through the ship's life, and explicitly says that allocation does not define ship status. It supplies neither an applicable identity rule nor inception or Work completion. | **Adopt the stable-designation boundary, not as SoTA or an identity-inception rule.** The number can help reidentify Ship 27 but does not by itself make the hull basis the ship, locate first existence, or establish completion, delivery, or operational status. |
| [IEC 62264-2:2026](https://webstore.iec.ch/en/publication/75127). **Current-standard reference for the manufacturing-information question: which operations objects and relationships can an interface exchange?** | Sections 4.2, 4.6, and 4.8 keep exact work, actual resources, criterion or test content, boundary-state facts, records, and evaluation results separately recoverable; case 5.6 preserves an earlier completion claim after later destruction. | **Adopt and adapt as an information-interface reference, not a SoTA-bearing production-recovery answer.** An exchanged operations object, record, test result, or work definition establishes neither a Work occurrence admitted under `U.Work` nor any work-to-change, inception, or completion fact by form. |
| Failla, Rossoni, Quirini, and Colombo, ["Managing lifecycle of product information with an ontology-based knowledge framework"](https://doi.org/10.1016/j.jii.2025.100820), 2025. **Current research proposal for the product-information traceability question.** | Sections 4.2 and 4.8 and cases 5.2 and 5.5 preserve traceability between product knowledge and a project instance while keeping templates, cloned information individuals, records, and the project-world entity distinct. | **Adapt for product-information lifecycle traceability, not physical or project-world inception.** The paper does not supply A.15.PROD's identity-specification applicability, earliest world-side boundary, work-to-change chain, or completion architecture. |
| [IEEE 1849-2023 XES](https://standards.ieee.org/ieee/1849/10907/). **Current-standard reference for the event-evidence interchange question.** | Sections 4.4 and 4.8 and the plan-or-log anti-pattern let logs and event streams support reconstruction while exact A.15.1 work, A.3.4 transformations, work-to-change facts, identity, and completion remain independently governed. | **Adopt for evidence interchange; reject as ontology.** A logged event, timestamp, trace order, or extension attribute establishes neither a performed occurrence nor a causal, production, identity, or completion link by form. |
| Borgo and Righetti, ["Towards Applied Constructional Ontology"](https://doi.org/10.3233/FAIA250480), 2025. **Ontology-design analogy about givens, constructors, dependence, mereology, and identity choices.** | The Rationale and the construction-label and composition anti-patterns retain only the caution that a chosen ontology construction or label does not settle a product-construction fact. The paper supplies no production-work, project-world inception, or production-completion practice answer. | **Retain as a sharply limited design analogy, not SoTA-bearing product-construction evidence.** Lexical proximity between constructional ontology and constructing products supplies no support for sections 4.3-4.6 or case 5.5. |
| The historical [W3C PROV-DM Recommendation](https://www.w3.org/TR/prov-dm/), 2013. **Historical lineage for provenance generation and availability.** | Sections 4.1, 4.5, and 4.6 deliberately separate production-work participation, entity-identity inception, production completion, and later availability so each can have its own work, rule, boundary, and evidence. | **Reject wholesale; retain as lineage.** PROV remains useful for provenance interchange, but its generation bundle is not imported as FPF's universal production ontology. |

The practical source-use result is visible in the Solution, checklist, and cases: the Scrum source supplies a bounded product-state criterion without collapsing review into release; NASA guidance distinguishes realization activities from transition; and IMO regulation supplies stable designation without status or inception. These are authoritative local constraints, not evidence that any one source is the best-known cross-domain production architecture.

### A.15.PROD:12 - Relations

- **Builds on:** `A.15.1` for exact work identity, work parts, concurrency, and continuity; `A.3.1` for production method, intended effect, and applicability; `A.3.4` for independently identified actual transformations and the transformation-composition stop; `C.2.1` for local claim and predicate-definition epistemes; and `A.6.RCD` for disposition, derivation, blocker, and any subject-specific continuation.
- **Coordinates with:** `A.1` and the subject-specific pattern that states the candidate's identity rule and applicability; `A.15.2` for plans that remain distinct from work; `A.15.6` for project and process wording recovery; `G.11` when a pinned base definition, substrate edition, or applicability settlement changes; and the declared work-to-change, characteristic-state, evaluation, evidence, assurance, completion-criterion, delivery, acceptance, release, publication, availability, and refresh predicates or patterns selected by the current case.
- **Informs:** production attribution, manufacturing and construction histories, biological and informational entity inception, rework analysis, product-lifecycle records, completion audits, and P2W or P2S continuation when the receiving action or decision asks one of the three recovered questions.

### A.15.PROD:13 - Lowering, Repair, and Refresh Conditions

An ordinary production-work claim lowers when its exact Work, Method enactment and applicability, intended production effect, affected referent, Work-part relation, Work-to-change predicate or local claim, shared applicability, or receiver's deciding criterion is missing.

An inception claim lowers when its exact identity specification and applicability, identity-closing Work, actual effects, Work-to-change and change-to-identity bases, or after-side entity cannot be recovered. A claim that this is the first satisfying boundary additionally needs an ordered candidate-boundary domain and an earliest-satisfying rule.

A completion use preserves a valid state-satisfaction claim whenever possible. That claim lowers only when its completion subject, criterion and applicability, boundary, boundary-state facts, or state-satisfaction predicate is missing. The separate Work-completion claim lowers when exact production Work or its closure predicate or local claim is absent; loss of that link does not erase the state-satisfaction claim.

An ordinary positive claim needs no materialized substrate document. A negative claim needs the selected substrate's applicable negation law. A pin-triggering or earliest-boundary use needs only the constructor, witness, polarity, ordering, or time semantics it actually consumes; missing required semantics yields the exact missing-substrate blocker. A project, plan, label, result record, log, certificate, publication, or punctuation supplies no substitute.

A maintainer **MUST** repair only the affected local claim when later information changes work identity or parthood, a direct work-to-change fact, the exact identity-specification episteme or its applicability basis, the exact completion-criterion episteme or applicability relation, a boundary state, a relied-on base-predicate edition, or the selected substrate edition or constructor semantics. An earlier inception or completion claim remains indexed by the exact specification or criterion episteme and applicability basis used at its boundary. An obtaining C.2.1 `EpistemeEditionRelation` can trigger lineage-aware refresh of current dependent uses but does not rewrite that claim; a non-continuing replacement opens a new independent applicability question. A later transformation, delivery, acceptance, release, publication, or availability claim does not by itself repair or invalidate an earlier production claim.

A relying practitioner **MUST** refresh an earlier claim after a change to its exact identity-specification episteme or direct applicability basis, completion-criterion episteme or applicability relation, any relied-on C.2.1 `EpistemeEditionRelation`, relied-on base-predicate edition, selected substrate edition, constructor semantics, witness or hidden-participant policy, polarity law, temporal policy, work-continuity policy, evidence basis, reference scheme, claim scope, or receiving use. Follow an obtaining edition relation only to discover the continuing later episteme, then re-evaluate that episteme's applicability for the current use. Treat a replacement without that relation as a new identity and do not carry forward lineage or applicability. Refresh claim currentness and reliance separately from the historically indexed occurrence, exact specification or criterion episteme, applicability, and boundary facts.

A maintainer **MUST** reopen source binding only for the branch whose practice answer changed: a changed Scrum Definition-of-Done rule reopens the software-Increment branch; a changed NASA realization, verification, validation, or transition rule reopens the affected systems-engineering completion use; and a changed IMO identification rule reopens regulated ship designation and continuity, not a generic entity-inception claim. A new source that actually answers cross-domain whole/proper-part production-work attribution reopens section 4.3 and the FPF synthesis hypothesis. A changed comparator reopens only the information, evidence, analogy, or lineage boundary it supports unless a direct subject rule also changes.

### A.15.PROD:End

