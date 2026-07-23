## A.15.PROD - Production Work, Entity-Identity Inception, and Production Completion Recovery

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Separate production work, when this exact entity first exists, and when production was completed.

**At a glance.** Production wording often compresses three different questions. This pattern recovers them as separate local compound relation-bearing claims: whether exact current work is the whole production work or a proper work part of it; whether, under an exact applicable identity-specification edition, governed effects of exact work made one exact entity satisfy its identity rule for the first time; and whether the subject state satisfied the applicable production-completion criterion at an exact boundary. It introduces no universal production relation or production-work kind.

**Plain claim-record gloss.** A local compound relation-bearing claim is one checkable statement for one selected question, built from already governed facts. It is neither an omnibus production record nor a new relation kind. Whole production work, first existence, and completion therefore remain three separate claims even when they cite overlapping facts.

### A.15.PROD:1 - Problem Frame

**Use this when.** Practitioners **SHOULD** use this pattern when work is said to have *made*, *produced*, *built*, *assembled*, *grown*, *generated*, *finished*, or *completed* something and the receiving decision needs to know which exact production question is true. They **SHOULD** prefer it when one work occurrence is nested in larger work, several work parts act concurrently, an entity becomes identifiable before all work ends, or completion is being confused with delivery, acceptance, release, publication, or availability.

**Primary EntityOfConcern by selected branch.** Production wording is the umbrella. Each application narrows to one exact local claim whose C.2.1 `EntityOfConcern` is exact `currentWork` for production-work participation, exact `producedEntity` after inception for entity-identity inception, or exact `productionWork` for production completion. When more than one branch is current, each branch retains its own claim episteme and `EntityOfConcern`; one manufactured union concern is inadmissible.

**Primary working reader.** A practitioner or modeler responsible for settling one of these production, identity, or completion questions for a current engineering, manufacturing, construction, lifecycle, audit, or scientific use before relying on delivery, acceptance, release, publication, or availability.

**Primary viewpoint.** The practitioner **SHOULD** recover the smallest receiver-relevant claim: select one branch, identify its exact `EntityOfConcern`, and stop when that branch is decided or its exact blocker is known. This pattern is not a form to fill in.

**First useful move.** The practitioner **SHOULD** first ask which answer the receiving work needs now:

1. Is this exact work the whole production occurrence or a declared proper part of it?
2. Under which exact applicable identity-specification edition did exact work make this exact entity satisfy its identity rule for the first time?
3. At which boundary did the subject state satisfy the production-completion criterion edition applicable to this occurrence?

The practitioner **MUST NOT** answer one question with evidence for another.

**What goes wrong if missed.** Any work-caused change is called production; an entity is treated as existing before its identity rule first holds; a finishing operation is mistaken for entity creation; a plan, log, post-state picture, or first observation is treated as the change-producing link; and later delivery or acceptance silently rewrites historical completion.

**What this buys.** Teams can attribute production work at the right work boundary, state when one entity first exists, and preserve historical completion without inventing a universal relation kind. Narrow and larger production readings can coexist through exact work-part relations. Identity, completion, rework, delivery, acceptance, release, publication, and availability remain independently inspectable.

**Cross-domain recognition test.** These three non-exhaustive recognition situations show that the same three production questions remain separate across heterogeneous practice:

| Recognition situation | First current question | Blocked overread |
| --- | --- | --- |
| A fastening step is said to have "produced Car 42". | Is the step whole production work or a proper part, did Car 42 already exist, and which completion criterion is current? | The last visible step establishes neither first existence nor completion by narrative order. |
| A culture run or spontaneous biological process is said to have "produced Batch B17". | Did one exact system under an obtaining role assignment enact a method in dated work, and only then which identity or completion branch is current? | Growth or reaction alone may ground actual transformation but establishes no Work occurrence admitted under `U.Work` and no production-through-work claim; a batch label, sample, or first observation closes none of those questions. |
| A build pipeline is said to have "produced ReleaseBinary 12". | Which dated build work and governed effects first established the exact artifact identity, or satisfied the build-completion criterion? | Build success, publication, release, deployment, and availability remain different claims. |

**So-what adoption test.** Would replacing the separate branch answers by one broad production sentence change what the receiver may rely on, schedule, audit, accept, release, or reopen? If yes, the practitioner **SHOULD** apply this recovery. If only one already-governed neighboring claim is current, the practitioner **SHOULD** use its direct pattern instead.

**Not this pattern when.** Practitioners **SHOULD** use `A.15.1` directly when the only question is what work occurred; `A.3.4` when the only question is what actually changed; `A.3.1` when the only question is the reusable way of doing; the direct identity pattern when only entity identity is current; or the direct evaluation, delivery, acceptance, release, publication, availability, evidence, or assurance pattern when only that neighboring claim is current. This pattern coordinates those objects only for a selected production-recovery question.

**No-mint disposition.** Authors and modelers **MUST NOT** introduce `U.ProductionWork` as a U-kind. They **MUST NOT** introduce `WorkProducesEntityRelation`, `EntityIdentityInceptionByWorkRelation`, `ProductionWorkRelation`, or `ProductionCompletionRelation` as universal relation kinds. The default result is one local C.2.1 claim episteme per selected question under A.6.RCD disposition 2. Repeated subject use may justify one subject-owned reusable predicate-definition episteme. Only the additional need of a named receiver for stable relation-occurrence identity opens a derived relation-kind candidate through A.6.RCD and later admission.

### A.15.PROD:2 - Problem

Production speech crosses several ontological boundaries. Exact dated work is an occurrence. An actual transformation is the bounded change of a referent. An identity-specification edition is an episteme that states when a candidate counts as the entity in question under its direct subject-governed applicability basis. Entity-identity inception is the first boundary at which that applicable edition's rule becomes true. Production completion is satisfaction of an applicable completion criterion by a subject state at a boundary of exact production work. A measurement or evaluation result is a separately governed value or episteme about its exact concern; it is neither the produced entity nor production completion itself.

These boundaries often differ. A ship can first exist while outfitting continues. A car can already exist before a required nut is fastened. A finished product can later be damaged, delivered, rejected, repaired, republished, or made unavailable. One broad production predicate hides those differences and also hides the exact missing governor when attribution cannot be established.

### A.15.PROD:3 - Forces

| Force | Tension |
| --- | --- |
| Familiar production language vs exact claim identity | One sentence often carries work participation, entity inception, completion, and later acceptance at once. |
| Narrow work vs containing work | A finishing occurrence may itself be production work for one bounded use and a proper part of a larger production occurrence for another. |
| Product-class identity before the entity exists | Entity-inception recovery remains blocked unless the exact identity-specification edition and its direct subject-governed applicability to the candidate basis, subject context, and inception boundary are available before inception; no surrogate future entity is introduced. |
| Actual work effects vs observation | Logs, deltas, pictures, and first observation can support a claim but do not create work-to-change or change-to-identity links. |
| Work composition vs transformation composition | A.15.1 may ground composite work while no accepted transformation-composition governor exists. |
| First existence vs completion | Identity and completion may coincide, but neither criterion entails the other. |
| Historical truth vs later state | Later damage, loss, rework, delivery, or acceptance neither erases nor silently rewrites an earlier completion claim. |
| Reusable language vs ontology economy | Repeated domain use may justify predicate semantics, but a convenient production label does not justify a universal relation kind. |

### A.15.PROD:4 - Solution

The practitioner **MUST** recover only the selected production question, its exact work and subject objects, and the smallest governed base that answers it. The practitioner **MUST** publish each answer as a separate local compound relation-bearing claim and **MUST** stop or return an exact blocker wherever a required direct relation, criterion, applicability rule, boundary fact, work granularity, or transformation-composition governor is missing.

**Core and branch cut.** The common recovery core is receiver-first question selection, exact-object recovery, closure through direct governors or one local claim selected under A.6.RCD disposition 2, and a deliberate stop. The production-work, entity-identity-inception, and production-completion branches add only their own `EntityOfConcern`, criterion or boundary, and branch-specific base. One branch neither inherits facts from another nor turns the common method into an omnibus production object. Work identity, transformation identity, subject identity, evidence, assurance, delivery, acceptance, release, publication, and availability remain with their direct governing patterns.

#### A.15.PROD:4.1 - Split the three questions before recovering evidence

| Question | Claim content | Ordinary stopping result | What it does not establish |
| --- | --- | --- | --- |
| Production-work participation | exact `currentWork` is itself `productionWork`, or exact `currentWork` is a declared proper work part of exact `productionWork` | one local positive or negative compound claim, or an exact work-grounding blocker | entity inception, completion, delivery, acceptance, or a universal production-work kind |
| Entity-identity inception | governed actual effects of exact `identityClosingWork` made exact `producedEntity` satisfy the rule in exact applicable `productIdentitySpecificationEdition` for the first time at exact `inceptionBoundary` | one local inception claim after the entity exists, plurality of incomparable minimal claims, or an exact blocker | production completion, later persistence, acceptance, or a reusable binary relation kind |
| Production completion | exact subject-state facts satisfied exact `productionCompletionCriterionEdition`, applicable to exact `productionWork`, at exact `completionBoundary` | one historically indexed local completion claim or an exact blocker | entity inception, delivery, acceptance, release, publication, or availability |

The three claims may cite overlapping facts. They remain different claims because they answer different receiving questions and can have different boundaries, criteria, and truthful C.2.1 `EntityOfConcern` values.

#### A.15.PROD:4.2 - Recover the smallest exact base

The practitioner **MUST** use only objects needed by the selected branch:

| Working name | Exact object and governor | Required contribution |
| --- | --- | --- |
| `productIdentitySpecificationEdition` | one exact edition of a C.2.1 predicate-definition episteme owned by the direct subject pattern | states the identity rule before inception without pretending that a future entity exists |
| identity-specification applicability basis | exact direct subject-governed applicability relation or local compound claim selected under A.6.RCD disposition 2 | establishes that the exact edition applies to the candidate basis, subject context, and candidate `inceptionBoundary`; it introduces no universal applicability relation |
| `producedEntity` | one exact `U.Entity`, designated only after inception | is the entity whose identity rule first became true |
| `productionMethod` | one exact `U.Method` under A.3.1 | states the governed way of doing, intended production effect, applicability, and relevant identity or completion criterion meaning |
| `currentWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates the world-side dated occurrence; its performer through an obtaining `U.RoleAssignment`, actual `enactsMethod`, extent, bindings, resources, affected referent, and containing system obtain independently rather than being fields stored in the occurrence |
| `productionWork` | one exact Work individual admitted under `U.Work` by A.15.1 | designates either the same occurrence as `currentWork` or the exact larger Work occurrence of which `currentWork` is a declared proper part |
| `actualTransformation` | one or more independently identified `U.Transformation` occurrences under A.3.4 | names what changed without becoming the work or the produced entity |
| work-to-change basis | exact subject-governed direct relations or local compound claims selected under A.6.RCD disposition 2 | establishes that selected actual changes are effects of exact work; coincidence is insufficient |
| `productionCompletionCriterionEdition` | one subject-governed predicate-definition episteme | states the criterion edition applicable to exact production work at the candidate completion boundary |
| local assertion | one C.2.1 episteme | carries only the compound claim needed for one selected question |

A method description, work plan, objective, commitment, product specification, evaluation result, or publication enters only through its own direct relation when the receiving use depends on it. None is constitutive of every production occurrence.

#### A.15.PROD:4.3 - Select one production-work branch

**Whole-work branch.** `currentWork = productionWork` is admissible only when that exact dated work has the actual `enactsMethod` relation to `productionMethod`, the method's governed intended production effect and applicability are current, exact work-to-change facts obtain, and the identity or completion criterion required by the receiving claim is recoverable. A familiar broader production label establishes no parent work.

**Proper-part branch.** Exact `currentWork` is admissible as a proper part of exact `productionWork` only when `OperationalPartOf_work` or another exact A.15.1 work-part relation with fitting occurrence semantics obtains. Interval overlap or concurrency is asserted separately and establishes neither parthood nor coordination. The containing work needs the same grounding as the whole-work branch: dated work identity, enacted production method, intended effect and applicability, affected referent, exact work-to-change facts, and the current identity or completion criterion. A shared label, project membership, common referent, temporal containment, overlap, or adjacency in a plan establishes no work parthood.

The two branches can support different bounded uses. A nut-fastening occurrence can be the whole production work for a narrowly bounded finishing operation and also a proper part of a larger car-production occurrence, provided each local claim names its exact extent, criterion, and work relation. `productionWork` is a relation-defined reading of one Work occurrence admitted under `U.Work`, not an intrinsic kind.

#### A.15.PROD:4.4 - Ground actual effects without inventing transformation composition

The practitioner **MUST** recover every actual transformation independently through A.3.4: changed referent, exact extent or formal boundary, boundary conditions, actual before/during/after facts, and continuity or reidentification rule. The practitioner **MUST** then recover each work-to-change link under its direct subject governor or as a local compound claim selected under A.6.RCD disposition 2. Temporal overlap, a common changed referent, a delta expression, a log record, or a post-state picture does not establish the link.

One transformation identified at the resolution needed by the production claim establishes neither presence nor absence of finer transformation parts. Work parts, method parts, samples, temporal subdivisions, concurrent changes, and flow representations do not establish transformation parts or a composite transformation.

The recovery continues when the selected production claim needs only independently identified transformations. When it needs a positive composite-transformation identity, transformation parthood, or transformation holonhood and no accepted governor supplies that basis, the result is the exact missing-governor blocker. Composite `identityClosingWork` under A.15.1 does not cure that blocker and does not imply an isomorphic composite transformation.

#### A.15.PROD:4.5 - Recover entity-identity inception

**Definition: A15PROD-D1 (Entity-identity inception).** Entity-identity inception is the boundary at which exact `producedEntity` first satisfies the identity rule stated by exact `productIdentitySpecificationEdition` that the direct subject pattern makes applicable to the candidate basis, subject context, and boundary. Plain: **when this exact entity first exists**. `inceptionBoundary` is a case-local boundary designator, not a second technical term, claim kind, or relation kind.

For this branch, the practitioner **MUST** complete all five steps:

1. recover exact `productIdentitySpecificationEdition` as one C.2.1 predicate-definition episteme in the direct subject pattern before applying it. Before inception, the governed question remains about exact work, method, actual effects, that edition, and its candidate basis; no future `producedEntity` participant exists;
2. recover the direct subject-governed applicability basis by which that edition applies to the exact candidate basis, subject context, and candidate `inceptionBoundary`, together with the exact actual effects of exact work and the direct links by which those effects bear on that applicable rule;
3. find the earliest exact `inceptionBoundary` at which the rule in that applicable edition becomes true and designate the resulting exact `producedEntity` only on the after-side of that boundary; the pre-inception candidate basis remains distinct from that entity;
4. identify exact `identityClosingWork`, using the one closing work occurrence when it exists or, for jointly necessary concurrent or nested work parts, their exact composite work under A.15.1 and its declared work-part relations; and
5. publish a positive local inception claim only after exact `producedEntity` exists and the claim names exact `productIdentitySpecificationEdition`, its direct subject-governed applicability basis, exact `identityClosingWork`, exact `inceptionBoundary`, and all governed work-to-change and change-to-identity links.

A published local inception claim **MUST** be indexed by the exact specification edition and applicability basis used at `inceptionBoundary`. A later identity-specification edition does not silently rewrite that earlier claim. Changed applicability yields either a separately qualified claim under its new exact basis or an exact blocker; it does not move the earlier indexed boundary.

A delta expression, method description, work plan, log, post-state image, identity-rule episteme, or first observation establishes none of those links by itself. Absence of recoverable work granularity for `identityClosingWork` yields a **work-granularity blocker**. Several incomparable minimal work composites yield several local inception claims; narrative simplicity supplies no rule for selecting only one.

**Regulated-identification boundary.** A persistent identifier is not an inception criterion. A current subject practice that allocates an identifier at build or registration while keeping allocation separate from entity status supplies designation and continuity only. First existence requires a separately applicable subject-identity rule; its absence yields the exact identity-governor blocker. An assigned number does not make the candidate basis the after-side entity.

#### A.15.PROD:4.6 - Recover historically indexed production completion

A production-completion claim designates:

- exact `productionWork`;
- exact `completionBoundary` inside or at the end of that occurrence;
- exact `productionCompletionCriterionEdition` applicable to that occurrence at that boundary;
- the exact applicability relation; and
- governed subject-state facts that satisfied that edition at the boundary.

Completion is historical. Later damage, loss, destruction, delivery, rejection, acceptance, release, publication, or unavailability does not erase an earlier true completion claim. A later criterion edition does not rewrite the earlier claim. Rework or later production work that satisfies a criterion at a later boundary receives a separate local completion claim.

Entity-identity inception and production completion remain separate claims even when they share a boundary. The applicable identity-specification edition says when this exact entity first exists under its direct subject-governed applicability basis; the completion criterion says when the applicable production requirement was satisfied. A later evaluation-result episteme may support either assertion under a direct evidence-use relation, but it creates neither the boundary nor the subject state.

Past work, entity-identity inception, and production completion remain addressable after later destruction or evidence decay. A later assertion carries its own evidence currentness and reliance status. The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain separately governed objects and claims.

**Practice-specific completion criteria stay local.** In current NASA systems-engineering practice, product implementation or integration, verification, validation, and product transition are distinct processes; a local completion claim therefore names the exact tailored product-layer criterion and does not substitute transition or delivery for verification or validation. In current Scrum practice, the applicable Definition of Done is a product-specific quality-state criterion and an Increment is born when a Product Backlog item first meets it; Sprint Review and release remain separate. These practice answers can supply an exact criterion or boundary only in their own applicability context. They supply neither the exact A.15.1 work occurrence nor a cross-domain universal completion rule.

#### A.15.PROD:4.7 - Publish local claims, not an omnibus relation

The default A.6.RCD disposition is **local compound relation-bearing claim**. For each selected question, the practitioner **MUST** complete all six actions:

1. name the exact receiving work or decision and the answer that closes it;
2. recover exact participants and direct relations under their own meanings;
3. state the least constructor admitted by the current substrate, its semantics, the governed base claim content it consumes, and any hidden-participant, polarity, applicability, or time policy that changes the result;
4. identify one truthful C.2.1 episteme with exact claim content, one exact `EntityOfConcern`, and an effective `U.ReferenceScheme`;
5. state positive or negative polarity only under the selected substrate's law; keep unresolved reliance or information sufficiency with its evaluation or evidence pattern; and
6. stop without introducing a relation kind, relation signature, or relation occurrence.

**Branch constructor semantics.** These are branch-local claim constructors, not a universal production algebra:

| Branch | Least constructor over governed base claims | Hidden-participant, polarity, and time policy |
| --- | --- | --- |
| production-work participation | one typed conjunction over exact A.15.1 work identity, actual method enactment, method applicability and intended production effect, affected referent, direct work-to-change facts, the receiver's current criterion, and either exact work identity or one exact A.15.1 proper-part relation | every participant and conjunct remains named; no projection hides work, transformation, or criterion witnesses; a negative result requires the selected substrate's explicit negation law rather than absence of a base assertion |
| entity-identity inception | one time-indexed conjunction over identity-specification applicability, exact work and governed effects, direct work-to-change and change-to-identity links, and satisfaction of the applicable identity predicate, followed by the substrate's earliest-satisfying-boundary selection over its declared ordered candidate-boundary domain | the candidate basis remains distinct from the after-side entity; work parts and actual transformations remain named or follow the substrate's explicit witness policy; incomparable minimal work composites remain plural, and A.15.PROD supplies no arbitrary minimization rule |
| production completion | one boundary-indexed conjunction over exact production work, exact criterion edition and applicability, and governed subject-state satisfaction at exact `completionBoundary` | the claim stays indexed by that boundary and edition; no earliest-boundary operator is implied unless the receiving use separately requires and the selected substrate defines it; negative polarity again requires an explicit substrate law |

A readable ordinary-use conjunction does not require a separately materialized substrate document when A.6.RCD:4.2 does not require one. For DPF or FPF authoring of a nontrivial, interoperability-facing, proof-bearing, high-consequence, or reusable claim, the responsible author or modeler **MUST** name the exact selected substrate and edition and **MUST** replay its constructor inputs, output claim, applicability, hidden witnesses, polarity law, and temporal policy. If no current substrate supplies the needed conjunction, boundary indexing, earliest-boundary selection, witness policy, or negation law, the result is the exact **missing-substrate blocker**. A.15.PROD supplies no fallback operator.
For an ordinary positive result, the truthful `EntityOfConcern` is usually exact `currentWork` for production-work participation, exact `producedEntity` for entity-identity inception, and exact `productionWork` for production completion. A modeler **MUST** split claim content that cannot truthfully concern one exact entity and **MUST NOT** manufacture a union concern from work, method, transformations, criteria, evidence, and receivers.

Repeated subject use may justify one predicate-definition episteme in the direct subject pattern. A subject-specific derived relation-kind candidate opens only when a named receiver also consumes stable relation-occurrence identity and the direct subject settlement can state obtaining, applicability, base dependencies, recurrence, and occurrence identity. A.6.RCD governs that continuation; A.15.PROD admits no such kind by itself.

#### A.15.PROD:4.8 - Separate recognition from assurance

**Recognition branch for ordinary work.** The practitioner **SHOULD** ask:

1. Which of the three production questions is current?
2. What exact `currentWork`, `productionWork`, method, affected referent, identity-specification or completion-criterion edition, and direct applicability basis are needed?
3. Which whole-work or proper-part branch obtains?
4. What independently identified actual transformations and direct work-to-change facts are required?
5. Does the exact identity-specification or completion-criterion edition apply at the stated boundary, and do the governed facts satisfy that edition?
6. Does the current substrate supply the branch's conjunction, boundary indexing, witness, polarity, and any earliest-boundary semantics?
7. Can one local compound claim close the receiving use now, or is the result the exact missing-substrate blocker?

The practitioner **MUST** stop when the local answer is readable and grounded and **MUST NOT** fill the rest of this pattern as a record.

**Assurance branch for authors and high-consequence use.** Authors and high-consequence users **MUST** additionally replay the exact work identity and part relations; the actual `enactsMethod` relation; method applicability and intended production effect; every work-to-change and change-to-criterion link; exact identity-specification and completion-criterion editions; the direct subject-governed applicability basis of each edition at its claimed boundary; boundary-state facts; positive and discriminating cases; C.2.1 identity; evidence-use relations; and the explicit transformation-composition non-inference. DPF and FPF authors **MUST** record the selected substrate and edition when A.6.RCD:4.2 requires a pin, and **MUST** expose direct base predicates, applicability, hidden participants, polarity law, boundary domain and ordering, witness policy, and any earliest-boundary rule used by the claim. Assurance may warrant reliance on the claim; it does not constitute work, change, entity inception, or completion.

**Assurance scope by use.** A modeler whose declaration or model carries one local claim **MUST** check exact claim content, one truthful `EntityOfConcern`, reference scheme, participants, direct governors, polarity, and boundary indexing. A practitioner or conformance reviewer **MUST** verify that the three-question first move reaches either one grounded local answer or one exact blocker and then stops. A pattern author or reviewer **MUST** also replay the worked and discriminating cases, neighbor-authority boundaries, checklist, and no-mint disposition. None of these assurance uses widens the recognition claim or adds a world-side production fact.

#### A.15.PROD:4.9 - Run the recovery sequence and stop deliberately

The practitioner **MUST** run the following sequence and **MUST** stop at the first grounded answer or exact blocker:

1. name the receiver and select one or more of the three questions;
2. recover exact work, method, affected referent, identity-specification or completion-criterion edition, its direct subject-governed applicability basis, and independently identified transformations only as needed;
3. select the whole-work or proper-part branch for production-work participation;
4. recover `identityClosingWork`, exact `productIdentitySpecificationEdition`, its applicability to the candidate basis and subject context at exact `inceptionBoundary`, and the earliest satisfying boundary only when first existence is current;
5. recover `completionBoundary`, applicable criterion edition, applicability relation, and boundary state only when completion is current;
6. select the branch-local constructor, state its semantics and governed base claims, and expose any hidden-participant, polarity, applicability, or time policy. For DPF/FPF authoring and other A.6.RCD:4.2 pin-triggering uses, the responsible author or modeler **MUST** name the exact substrate and edition;
7. publish one local C.2.1 claim episteme per answer;
8. return the exact blocker for any missing work granularity, direct governor, identity-specification or completion-criterion edition, direct applicability basis, boundary fact, required transformation-composition basis, constructor semantics, or current substrate; and
9. stop; delivery, acceptance, release, publication, availability, result, evidence, assurance, or relation-kind claims open only when the receiver independently needs them.

#### A.15.PROD:4.10 - Pattern NameCard

This NameCard names the recovery pattern, not a relation kind:

```text
NameCard:
  NameCardId: NC-A15-PROD-PATTERN
  GovernedValueRef: the A.15.PROD pattern that separates and recovers production-work participation, entity-identity inception, and production-completion claims
  GoverningPatternRef: A.15.PROD
  ReferenceScheme: FPFCoreReferenceScheme
  BoundedContextRef: FPF work, transformation, construction, production, and entity-identity use
  LocalSenseRef: recover which production question is current without collapsing actual work, the first existence of one entity, production completion, delivery, acceptance, release, publication, or availability
  TechLabel: Production Work, Entity-Identity Inception, and Production Completion Recovery
  PlainLabel: separate production work, when this exact entity first exists, and when production was completed
  CandidateSet: Production Work, Entity-Identity Inception, and Production Completion Recovery; Entity Production by Work; Entity-Identity Inception Through Work; Production Boundary Recovery
  RejectedCandidates:
    Entity Production by Work: hides whether the claim concerns work participation, first existence of the entity, or completed production
    Entity-Identity Inception Through Work: omits production work before and after first existence and omits production completion
    Production Boundary Recovery: uses a generic boundary head and does not expose the three governed questions
  SelectionRationale: the selected title names the three distinctions recovered by the pattern and makes the completion kind explicit; it cannot be parsed as one binary or ternary production relation
  RefreshCondition: reopen naming if repeated subject use justifies an admitted derived relation kind or one question needs a separate primary EntityOfConcern and recovery algorithm
```

### A.15.PROD:5 - Archetypal Grounding

#### A.15.PROD:5.1 - Car 42 and the required nut

In this case, Car 42 already satisfies its identity rule before `NutFasteningWork-42`. The dated fastening work enacts an exact fastening method and changes exact fastener, torque, and attachment facts. Those changes concern the same continuing car; they do not bring Car 42 into existence.

For a narrowly bounded finishing use, `NutFasteningWork-42` can be the whole `productionWork` when the method's intended production effect and applicability, exact work-to-change facts, and completion criterion edition are governed. For the broader factory use, the same occurrence can be a proper operational part of `CarProductionWork-42` under an exact A.15.1 part relation. First satisfaction of the applicable completion criterion at the fastening boundary yields a local completion claim; prior completion instead classifies the work as later rework, repair, or maintenance. The verb *fasten* and the presence of a car decide none of these claims.

For the author-side constructor replay, exact local assertion-substrate edition `Car42-Claims-v2` defines typed conjunction over the named work-identity, method-enactment, applicability, affected-referent, work-to-change, criterion, and whole-work or proper-part claims. The narrow positive case closes because every conjunct has common applicability to that receiving use. In the discriminating failure, the same edition receives only a torque result and temporal overlap but no governed work-to-change fact; conjunction semantics cannot manufacture the missing conjunct, so the branch returns the exact missing-governor blocker rather than a negative production claim. `Car42-Claims-v2` is a case-local substrate-edition designator, not a new FPF kind, relation kind, or required universal language.

#### A.15.PROD:5.2 - Incomplete but identifiable Ship 27

In this case, exact ship-identity specification edition `SHIP-ID-2` is directly governed as applicable to the candidate hull basis, yard context, and exact `inceptionBoundary`. Exact hull-assembly work can close that edition's rule at `inceptionBoundary` while outfitting, software installation, trials, and commissioning continue. The resulting inception claim concerns when Ship 27 first exists and remains indexed by `SHIP-ID-2` and that applicability basis. A later `SHIP-ID-3` edition does not move the earlier boundary; applying it there requires its own direct applicability basis and a separately qualified claim, or returns an exact blocker.

Exact author-side substrate edition `YardIdentityHistory-v3` defines time-indexed conjunction over the named work, applicability, actual-effect, work-to-change, change-to-identity, and identity-satisfaction claims plus earliest selection over its declared ordered candidate-boundary domain. The positive replay returns exact boundary `tI` because `SHIP-ID-2` is false at every earlier candidate boundary and true at `tI`; exact work and transformation witnesses remain named. In the discriminating failure, a snapshot substrate can conjoin facts at `tI` but supplies no ordered boundary domain or earliest-selection law. That substrate cannot establish inception even if a later image satisfies the rule, so the branch returns the exact missing-substrate blocker rather than treating first observation as first existence. The example adds no universal earliest operator or arbitrary minimal-work selection.

An IMO ship identification number may designate Ship 27 and remain stable across later flag, name, ownership, or type changes. The current IMO integrated scheme nevertheless states that number allocation does not define ship status. The number therefore supports regulated designation and continuity only; it neither supplies `SHIP-ID-2` nor proves `inceptionBoundary`. If the receiving use cannot recover a separate applicable ship-identity rule, the inception branch returns the exact identity-governor blocker.

A larger exact production-work occurrence contains the identity-closing work and later work through declared A.15.1 part relations. Production completion occurs only when Ship 27's governed state satisfies the applicable completion-criterion edition at `completionBoundary`. Delivery, class acceptance, and operational release remain separate. The sentence `the yard produced Ship 27` is admissible only when the receiving use makes the intended work extent and completion reading recoverable.

#### A.15.PROD:5.3 - Nested and concurrent attribution

Factory work may contain project work, subassembly work, `identityClosingWork`, and completion-closing work. Every selected work-part relation remains explicit. Jointly necessary concurrent work parts use exact composite work under A.15.1. Two incomparable minimal work composites yield two local inception claims, each indexed by its exact identity-specification edition and applicability basis. Nested or concurrent attribution creates no additional inception occurrence, and none of those work compositions establishes transformation composition. The identity-specification and completion-criterion editions remain epistemes cited by the local claims, and the identity-specification applicability basis remains its separately governed relation or claim; none is a work participant.

#### A.15.PROD:5.4 - Pressure adjustment without entity inception

A dated pressure-adjustment Work occurrence may stand in an exact `enactsMethod` relation, and a separately governed work-to-change relation may connect that Work individual to an independently identified pressure transformation. If the affected vessel or process already exists and no production-completion criterion is current, the case closes as work plus actual change, without manufacturing production-work, entity-inception, or completion claims merely because a method intended a changed state.

#### A.15.PROD:5.5 - PumpSkid assembly before PumpSkid identity

Mounting, wiring, fluid-connection, and whole-configuration changes may each be independently identified under A.3.4. Exact work parts may also be grounded under A.15.1. If exact PumpSkid identity-specification edition, its direct applicability basis for the candidate configuration, subject context, and boundary, exact work-to-change facts, and direct change-to-identity basis establish when PumpSkid 7 first exists without relying on a composite transformation, the inception claim may proceed. A selected claim that requires positive composite-transformation identity or transformation parthood without an accepted governor yields the exact missing-governor blocker. Work or method decomposition supplies no proof of transformation decomposition.

#### A.15.PROD:5.6 - Completion persists after later destruction

In this case, exact production work satisfied criterion edition `PC-3` at boundary `tC`, and a later accident destroyed the product. Exact author-side substrate edition `CompletionHistory-v1` defines boundary-indexed conjunction over production-work identity, applicability of `PC-3`, and the governed subject-state facts at `tC`; it does not apply an earliest operator. The positive replay therefore retains the historical completion claim at `tC`, while the destruction is a later transformation. In the discriminating failure, an unindexed current-state predicate or later completion certificate supplies no `satisfiedAt(tC)` constructor semantics. That substrate returns the exact missing-substrate blocker for the historical claim rather than moving completion to the certificate or current state. Current evidence, availability, replacement work, acceptance status, and insurance decisions remain separately governed.

#### A.15.PROD:5.7 - Non-agentive biological synthesis

A spontaneous reaction or biological growth process may be independently grounded as one or more actual transformations under A.3.4. The transformed biological, chemical, or physical referent may itself be a `U.System`; that fact neither identifies it as a performing system nor supplies production work. If no exact performing system is designated through an obtaining `U.RoleAssignment` and grounded as actually enacting an applicable method in one dated Work occurrence admitted under `U.Work`, A.15.PROD opens no production-through-work claim: retain the exact transformed referent and actual transformations, while entity identity remains with the direct biological subject governor. `Batch B17`, a sample label, first observation, or process record supplies none of the performer-side basis, work identity, or production attribution.

If an exact performing system designated through an obtaining role assignment did enact a governed applicable method in dated work, the relevant A.15.PROD branch may open. Entity-identity inception still needs the exact applicable identity-specification edition and governed work effects; production completion still needs its applicable criterion edition, boundary, and boundary-state facts. The same observed growth can therefore support an actual-change claim while the production-work claim remains blocked; the transformed referent remains present in either result and is not erased when the performer-side basis is absent.

#### A.15.PROD:5.8 - Scrum Increment before review or release

In this case, the current Scrum Guide and one exact organizational Definition of Done edition govern a software-product use. When exact Product Backlog item `PBI-84` first satisfies that applicable Definition of Done at boundary `tD`, exact `Increment-I84` is born under that practice; work that does not meet the Definition of Done is not part of the Increment. Multiple Increments may exist before Sprint Review, and the review is not a release gate.

A.15.PROD may therefore use the applicable Definition of Done as the branch-specific identity and completion criterion at `tD`, while keeping Sprint Review, delivery, and release separate. The guide does not identify the exact A.15.1 Work occurrence, performer-side basis, actual effects, or work-to-change links. Missing independently obtaining relations involving the Work occurrence, Definition of Done edition, or applicability to `PBI-84` yields the corresponding work, criterion, applicability, or boundary blocker rather than a production inference from a Sprint, ticket, review, or release label.

### A.15.PROD:6 - Bias-Annotation

**Scope limitation and five-lens coverage.** These annotations cover the three production-recovery branches and their named neighboring claims; they do not classify production language outside a current A.15.PROD use. `Gov` covers criterion, applicability, and historical-authority errors; `Arch` covers branch, neighbor-owner, and omnibus-relation errors; `Onto/Epist` covers work, change, entity, claim, record, and publication distinctions; `Prag` covers receiver-first selection, useful stops, and exact blockers; and `Did` covers the familiar verbs, visible final steps, labels, and records that make the overreads plausible.

| Bias | Countermeasure |
| --- | --- |
| Verb bias | The countermeasure treats *make*, *produce*, *build*, *finish*, and *complete* as retrieval cues and selects one of the three questions by exact facts. |
| Record bias | The countermeasure keeps plans, logs, pictures, tickets, certificates, and publications as epistemic or publication objects until direct relations connect them to work, change, identity, or completion. |
| Final-step bias | The check rejects creation by last-visible-step order and replays the exact applicable identity-specification edition, its direct applicability basis, and the exact work effects. |
| Container bias | A project, factory, batch, case, or common referent supplies no proof of work parthood or production attribution. |
| Composition bias | Work parts, method parts, samples, and flow structure supply no transformation-part inference. |
| Present-state bias | The check evaluates completion at its historical boundary and criterion edition, not only from the entity's current state. |
| Universal-relation bias | The countermeasure prefers the local compound claim that answers the receiver over a broad production relation name. |

### A.15.PROD:7 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-A15.PROD-1` | The receiving use selects production-work participation, entity-identity inception, production completion, or an explicit subset; one question's evidence is not used as another's answer. |
| `CC-A15.PROD-2` | `currentWork` and `productionWork` designate exact A.15.1 Work occurrences admitted under `U.Work`, not plans, labels, projects, methods, logs, publications, or records that describe those occurrences. |
| `CC-A15.PROD-3` | The whole-work branch names actual `enactsMethod`, method applicability and intended production effect, affected referent, exact work-to-change facts, and the criterion current for the receiver. |
| `CC-A15.PROD-4` | The proper-part branch names an exact A.15.1 work-part relation and gives the containing work the same grounding required by the whole-work branch. |
| `CC-A15.PROD-5` | Every actual transformation is independently identified under A.3.4; work, method, samples, temporal subdivision, and flow representations do not imply transformation composition. |
| `CC-A15.PROD-6` | Every work-to-change and change-to-identity or change-to-completion link has a direct governor or is stated in a local compound claim selected under A.6.RCD disposition 2. |
| `CC-A15.PROD-7` | Exact `productIdentitySpecificationEdition` is available before inception without a surrogate future `producedEntity`; its direct subject-governed applicability to the candidate basis, subject context, and exact `inceptionBoundary` is recoverable, and the entity is designated only after that applicable edition's rule first holds. |
| `CC-A15.PROD-8` | A positive inception claim satisfies `A15PROD-D1` and names exact `identityClosingWork`, exact `productIdentitySpecificationEdition`, its direct applicability basis, exact `inceptionBoundary`, exact `producedEntity`, and first satisfaction of that applicable edition's rule. |
| `CC-A15.PROD-9` | Concurrent or nested identity-closing work is composed only through exact A.15.1 work-part relations; incomparable minimal composites remain plural, and each local inception claim retains its exact identity-specification edition and applicability basis. |
| `CC-A15.PROD-10` | A completion claim names exact production work, completion boundary, criterion edition applicable then, applicability relation, and governed boundary-state facts. |
| `CC-A15.PROD-11` | Later criterion editions, damage, loss, delivery, acceptance, release, publication, and availability do not rewrite historical completion. Rework at another boundary receives another claim. |
| `CC-A15.PROD-12` | Each local assertion is one C.2.1 episteme with one truthful exact `EntityOfConcern`, claim content, effective reference scheme, and decided positive or negative polarity; no union concern is manufactured, and unresolved information sufficiency or reliance remains separately evaluated. |
| `CC-A15.PROD-13` | An unresolved basis is returned as the exact missing-governor, work-granularity, criterion, applicability, boundary-state, or transformation-composition blocker, not as a third predicate value. |
| `CC-A15.PROD-14` | The current no-mint result introduces no universal production relation kind, `U.ProductionWork`, relation signature, or relation occurrence and asserts no universal reducibility. A later subject-specific candidate returns to A.6.RCD under its exact derived- or primitive-kind conditions: named occurrence-semantics need or failed lossless derivation with an action-facing loss, plus obtaining, applicability, independent uses when primitive, recurrence, and occurrence identity. |
| `CC-A15.PROD-15` | Recognition and assurance remain separate; evidence and evaluation may support the claim but create none of work, transformation, entity inception, or completion. |
| `CC-A15.PROD-16` | The produced entity, measurement or evaluation result, delivered entity, acceptance verdict, release, publication, availability, and downstream effect remain distinct and use their direct governors. |
| `CC-A15.PROD-17` | A practice-specific source is used only for the branch question it answers: a stable identifier does not establish entity status or inception; a systems-engineering realization criterion does not collapse transition into completion; and a Scrum Definition of Done does not supply work identity, effects, review, or release. |
| `CC-A15.PROD-18` | Each local claim states its branch-local constructor semantics, governed base claims, common applicability, hidden-participant or witness policy, polarity law, and temporal policy. A DPF/FPF-author, nontrivial, interoperable, proof-bearing, high-consequence, or reusable use pins the exact selected substrate and edition; an unavailable operator returns the exact missing-substrate blocker. |

### A.15.PROD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Every work-caused transformation is production | Modification of a continuing entity is treated as entity creation or completed production. | The repair first recovers work plus actual change and opens only the production question needed by the receiver. |
| The final visible step created the product | Narrative order substitutes for first satisfaction of the exact applicable identity-specification edition. | The repair recovers exact `identityClosingWork`, direct effects, identity-specification edition, its direct applicability basis, and earliest satisfying boundary. |
| Plan or log as production work | Intended or recorded material is treated as the dated occurrence. | The repair recovers exact A.15.1 work and relates plan, log, and evidence separately. |
| Shared label as work parthood | Two occurrences called *assembly* are treated as parent and part. | The repair states the exact A.15.1 work-part relation or keeps the occurrences separate. |
| Work parts imply transformation parts | Composite work is used as proof of a composite transformation. | The repair keeps transformations independently identified and returns the missing transformation-composition governor when needed. |
| Completion equals acceptance | A satisfied production criterion is replaced by a customer's or regulator's later verdict. | The repair publishes completion at its boundary and governs acceptance separately. |
| Current damage erases completion | Present nonconformance is used to deny an earlier satisfied criterion. | The repair indexes completion by occurrence, criterion edition, boundary, and boundary state and records the later transformation separately. |
| One omnibus production episteme | Work, inception, completion, delivery, and evidence are put into one claim with a union concern. | The repair splits one local C.2.1 episteme per selected question and direct neighboring claim. |
| Relation-name escalation | Familiar production wording is promoted to a universal relation kind. | The repair stops at A.6.RCD disposition 2 unless repeated subject semantics and occurrence identity independently justify continuation. |

### A.15.PROD:9 - Consequences

| Benefits | Trade-offs and mitigations |
| --- | --- |
| Production attribution becomes replayable at exact work boundaries. | More than one local claim may replace one familiar sentence; the three-question first move keeps ordinary use short. |
| Entity first-existence and production completion no longer overwrite each other. | The added cost is an exact edition and applicability basis for each current identity or completion criterion; reusing direct subject specifications avoids copying them. |
| Narrow and containing production work can coexist without a new kind. | Absence of exact work mereology yields an unresolved work-granularity blocker. |
| Historical completion survives later change while current evidence remains refreshable. | Boundary truth and present reliance stay separate; direct evidence and refresh patterns govern current reliance. |
| Missing transformation composition no longer blocks independent production claims. | A composition-dependent claim stops at an explicit blocker; independently identified transformations and exact blockers remain useful results. |

### A.15.PROD:10 - Rationale

In the selected cases and declared receiving uses, no need for a universal production relation kind has been demonstrated. Each current question closes through exact governed direct facts and one branch-local claim or exact blocker. This is a bounded current parsimony result, not proof that every production relation is reducible or that no irreducible production-relation fact can occur in another subject practice. The bases vary across manufacturing, construction, biology, software, formal work, and epistemic production; local compound claims preserve those subject differences and make a missing governor visible instead of hiding it behind a broad relation name.

A later subject practice reopens A.6.RCD continuation when repeated uses need reusable predicate semantics or stable occurrence semantics. A derived-kind candidate needs a named receiver for occurrence identity and a direct settlement of obtaining, applicability, base dependencies, recurrence, and stable relation-occurrence identity. A primitive candidate additionally needs failed lossless derivation, one exact action-facing distinction that every accepted derivation loses, and independent receiving uses. Repeated predicate use without a need for occurrence semantics stops at reusable predicate semantics. A.15.PROD therefore records the present no-mint disposition but neither forbids nor pre-admits a later subject-specific derived or primitive relation kind.

The three-question split also preserves time correctly. Work may begin before an entity exists and continue after it first exists. Completion may occur at inception or later. Delivery, acceptance, release, publication, and availability may occur later still. Keeping each boundary and criterion separate gives practitioners useful historical claims without treating every neighboring event as part of production identity.

### A.15.PROD:11 - SoTA-Echoing

Current Scrum, maritime-identification, and NASA systems-engineering practice supplies three narrower operational answers for identity or completion boundaries. Manufacturing-information, product-information lifecycle, event-log, constructional-ontology, and provenance sources remain useful comparators with different and explicitly limited roles. None of these traditions supplies one universal production ontology or a cross-domain answer to every A.15.PROD branch.

**FPF synthesis scope.** The three-claim decomposition is an FPF-scoped architectural hypothesis for receiver-specific production recovery, not a claim that the cited traditions share one production ontology. The SoTA-bearing rows below govern only their named practice branches. No current primary source in the reviewed set answers the cross-domain A.15.PROD:4.3 question of when exact work is the whole production work or its proper part; that branch remains a bounded FPF hypothesis built from A.15.1 work identity and exact subject governors. A subject domain that demonstrates a different best-known answer, failed lossless derivation with an exact action-facing loss, direct obtaining and applicability laws, independent receiving uses, recurrence, and stable relation-occurrence identity reopens the affected branch and A.6.RCD continuation.

| Source, named branch question, and classification | Exact answer carried into A.15.PROD | Adoption status and blocked overread |
| --- | --- | --- |
| Schwaber and Sutherland, [*The Scrum Guide*](https://scrumguides.org/scrum-guide.html), official current edition 2020. **SoTA-bearing practice source for the Scrum-software question: when does one usable Increment exist and count as done relative to review or release?** | The guide makes the applicable Definition of Done the quality-state criterion, states that an Increment is born when a Product Backlog item meets it, excludes work that does not meet it, permits multiple Increments before Sprint Review, and denies that review is a release gate. Sections 4.5-4.6, case 5.8, and `CC-A15.PROD-17` therefore use the exact applicable Definition of Done edition at one boundary while keeping review and release separate. | **Adopt for the named Scrum branch.** The Definition of Done supplies only the branch-specific identity and completion criterion; a Sprint, backlog item, Increment label, review, or release supplies neither exact A.15.1 work, performer, effects, nor a cross-domain production rule. |
| NASA [NPR 7123.1D, *Systems Engineering Processes and Requirements*](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter3), effective 2023-2028, together with the official [NASA Systems Engineering Handbook product-realization guidance](https://www.nasa.gov/reference/5-0-product-realization/). **SoTA-bearing practice source family for the NASA systems-engineering question: which tailored product-layer result counts as realized, and what remains transition?** | NPR 7123.1D requires distinct implementation or integration, verification, validation, and transition processes; the handbook supplies the current associated best-practice guidance and keeps a validated end product and its later transition to the next product layer or user distinct. Section 4.6 and `CC-A15.PROD-17` therefore require the exact tailored product-layer criterion and forbid delivery or transition from substituting for verification or validation. | **Adopt for the named NASA branch.** The applicable product-layer success, verification, or validation criterion supplies the local completion basis. The process sequence establishes no universal production-completion relation, and a validation report, transition record, or delivery is not the world-side boundary. |
| IMO [Resolution A.1215(34), *Integrated IMO Identification Number Scheme*](https://wwwcdn.imo.org/localresources/en/OurWork/IIIS/Documents/A%2034-Res.1215%20-%20INTEGRATED%20IMO%20IDENTIFICATION%20NUMBER%20SCHEME%20%28Secretariat%29.pdf), 2025, and [Circular Letter No.5096](https://wwwcdn.imo.org/localresources/en/OurWork/IIIS/Documents/Circular%20Letter%20No.5096%20-%20Implementation%20of%20Resolution%20A.1215%2834%29%20-%20IMO%20Integrated%20Identification%20Number%20Scheme%20%28Secretariat%29.pdf), 2026. **SoTA-bearing regulatory-practice source family for the maritime question: what does a persistent ship identifier establish, and does its allocation define ship status or inception?** | The current scheme allocates a ship identifier at build or first registration and keeps it unchanged through the ship's life; the implementation circular explicitly says allocation does not define ship status. Section 4.5, case 5.2, and `CC-A15.PROD-17` therefore use the number for regulated designation and continuity only and require a separate applicable ship-identity rule for inception. | **Adopt the stable-designation boundary; reject the inception shortcut.** An IMO number can help reidentify Ship 27 but does not by itself make the hull basis the ship, locate first existence, or establish completion, delivery, or operational status. |
| [IEC 62264-2:2026](https://webstore.iec.ch/en/publication/75127). **Current-standard reference for the manufacturing-information question: which operations objects and relationships can an interface exchange?** | Sections 4.2, 4.6, and 4.8 keep exact work, actual resources, criterion or test content, boundary-state facts, records, and evaluation results separately recoverable; case 5.6 preserves an earlier completion claim after later destruction. | **Adopt and adapt as an information-interface reference, not a SoTA-bearing production-recovery answer.** An exchanged operations object, record, test result, or work definition establishes neither a Work occurrence admitted under `U.Work` nor any work-to-change, inception, or completion fact by form. |
| Failla, Rossoni, Quirini, and Colombo, ["Managing lifecycle of product information with an ontology-based knowledge framework"](https://doi.org/10.1016/j.jii.2025.100820), 2025. **Current research proposal for the product-information traceability question.** | Sections 4.2 and 4.8 and cases 5.2 and 5.5 preserve traceability between product knowledge and a project instance while keeping templates, cloned information individuals, records, and the project-world entity distinct. | **Adapt for product-information lifecycle traceability, not physical or project-world inception.** The paper does not supply A.15.PROD's identity-specification applicability, earliest world-side boundary, work-to-change chain, or completion architecture. |
| [IEEE 1849-2023 XES](https://standards.ieee.org/ieee/1849/10907/). **Current-standard reference for the event-evidence interchange question.** | Sections 4.4 and 4.8 and the plan-or-log anti-pattern let logs and event streams support reconstruction while exact A.15.1 work, A.3.4 transformations, work-to-change facts, identity, and completion remain independently governed. | **Adopt for evidence interchange; reject as ontology.** A logged event, timestamp, trace order, or extension attribute establishes neither a performed occurrence nor a causal, production, identity, or completion link by form. |
| Borgo and Righetti, ["Towards Applied Constructional Ontology"](https://doi.org/10.3233/FAIA250480), 2025. **Ontology-design analogy about givens, constructors, dependence, mereology, and identity choices.** | The Rationale and the construction-label and composition anti-patterns retain only the caution that a chosen ontology construction or label does not settle a product-construction fact. The paper supplies no production-work, project-world inception, or production-completion practice answer. | **Retain as a sharply limited design analogy, not SoTA-bearing product-construction evidence.** Lexical proximity between constructional ontology and constructing products supplies no support for sections 4.3-4.6 or case 5.5. |
| The historical [W3C PROV-DM Recommendation](https://www.w3.org/TR/prov-dm/), 2013. **Historical lineage for provenance generation and availability.** | Sections 4.1, 4.5, and 4.6 deliberately separate production-work participation, entity-identity inception, production completion, and later availability so each can have its own work, rule, boundary, and evidence. | **Reject wholesale; retain as lineage.** PROV remains useful for provenance interchange, but its generation bundle is not imported as FPF's universal production ontology. |

The practical source-use result is visible in the Solution, checklist, and cases: Scrum supplies a Definition-of-Done boundary without review/release collapse; NASA systems engineering supplies a tailored realization criterion without transition/delivery collapse; and IMO supplies stable designation without status/inception collapse. The remaining comparators constrain information and evidence overreads. None supplies the still-hypothetical cross-domain whole/proper-part production-work answer.

### A.15.PROD:12 - Relations

- **Builds on:** `A.15.1` for exact work identity, work parts, concurrency, and continuity; `A.3.1` for production method, intended effect, and applicability; `A.3.4` for independently identified actual transformations and the transformation-composition stop; `C.2.1` for local claim and predicate-definition epistemes; and `A.6.RCD` for disposition, derivation, blocker, and any subject-specific continuation.
- **Coordinates with:** `A.1` and the direct subject identity pattern for entity identity; `A.15.2` for plans that remain distinct from work; `A.15.6` for project and process wording recovery; `G.11` when a pinned base definition, substrate edition, or applicability settlement changes; and direct work-to-change, characteristic-state, evaluation, evidence, assurance, completion-criterion, delivery, acceptance, release, publication, availability, and refresh patterns when those relations are current.
- **Informs:** production attribution, manufacturing and construction histories, biological and informational entity inception, rework analysis, product-lifecycle records, completion audits, and P2W or P2S continuation whenever the receiving use needs one of the three recovered claims.

### A.15.PROD:13 - Lowering, Repair, and Refresh Conditions

A production-work claim lowers when exact work identity, enacted method, method applicability, intended production effect, affected referent, work-part relation, work-to-change basis, common applicability, or conjunction semantics is missing. An inception claim lowers when exact `productIdentitySpecificationEdition`, its direct subject-governed applicability to the candidate basis, subject context, and `inceptionBoundary`, `identityClosingWork`, direct effect basis, ordered candidate-boundary domain, earliest-satisfying rule, witness policy, or exact entity after inception cannot be recovered. A completion claim lowers when the production work, applicable criterion edition, applicability relation, boundary, boundary-indexed constructor, or boundary-state facts are missing. A negative claim also lowers when the selected substrate supplies no applicable negation law. Absence of a current substrate for the required constructor, witness, polarity, or time semantics yields the exact missing-substrate blocker; punctuation, a project, plan, label, result record, log, certificate, or publication supplies no substitute.

A maintainer **MUST** repair only the affected local claim when later information changes work identity or parthood, a direct work-to-change fact, an identity-specification edition or its applicability basis, a completion-criterion edition or applicability relation, a boundary state, a relied-on base-predicate edition, or the selected substrate edition or constructor semantics. An earlier inception claim remains indexed by the exact identity-specification edition and applicability basis used at its boundary; a later edition does not silently rewrite it, and changed applicability yields a separately qualified claim or exact blocker. A later transformation, delivery, acceptance, release, publication, or availability claim does not by itself repair or invalidate an earlier production claim.

A relying practitioner **MUST** refresh an earlier claim after a change to its identity-specification edition or direct applicability basis, completion-criterion edition or applicability relation, relied-on base-predicate edition, selected substrate edition, constructor semantics, witness or hidden-participant policy, polarity law, temporal policy, work-continuity policy, evidence basis, reference scheme, claim scope, or receiving use. The practitioner **MUST** refresh claim currentness and reliance separately from the historically indexed occurrence, edition, applicability, and boundary facts.

A maintainer **MUST** reopen source binding only for the branch whose practice answer changed: a changed Scrum Definition-of-Done rule reopens the software-Increment branch; a changed NASA realization, verification, validation, or transition rule reopens the affected systems-engineering completion use; and a changed IMO identification rule reopens regulated ship designation and continuity, not a generic entity-inception claim. A new source that actually answers cross-domain whole/proper-part production-work attribution reopens section 4.3 and the FPF synthesis hypothesis. A changed comparator reopens only the information, evidence, analogy, or lineage boundary it supports unless a direct subject rule also changes.

### A.15.PROD:End

