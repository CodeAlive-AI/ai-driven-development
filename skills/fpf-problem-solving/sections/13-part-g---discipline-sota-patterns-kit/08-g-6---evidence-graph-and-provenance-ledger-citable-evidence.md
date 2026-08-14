## G.6 - Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths

> **Type:** Evidence and provenance pattern
> **Status:** Stable
> **Normativity:** Normative where conformance rows say so; examples and SoTA rows are informative guidance.

### G.6:1 - Problem Frame

Use this pattern when a later user must cite, replay, audit, or refresh a path through several already established objects and relations rather than repeat their complete source account.

Use it when the working question is:

* which admitted dated Work occurrences and actual performer Systems must remain addressable, together with their already-established F.6 attribution and any local system-role kind or assignment identifier that the path separately uses;
* which direct participation or binding facts, produced entities, domain results, result epistemes, outcomes, source publications, carriers, and provenance relations must remain addressable;
* which exact direct relations connect those objects, which pattern defines or constrains each relation, and whether each relation is already established as obtaining;
* which bounded context, reference plane, time window, bridge, edition, policy, source-currentness result, or reliance boundary limits the cited path;
* which downstream work and exact use relation may cite the path; and
* what stronger conclusion, assurance, permission, acceptance, gate passage, or decision the path does not carry.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is an addressable provenance representation: one `EvidenceGraph`, its `PathId` or `PathSliceId`, and any ledger entry that makes the path replayable. G.6 governs path identity, slicing, citation, and local refresh. It does not create the represented work, participation, production, result, episteme, outcome, source, currentness, reliance, or representation correspondence.

**First useful move.** Name the relied-on claim or bounded use, then list the exact object refs and direct relation refs needed to replay it. For every relation record its direct governor and obtaining claim. Only then draw the path. Keep an unresolved relation as a gap; do not turn it into a graph edge asserted as obtaining.

**What goes wrong if missed.** A tidy graph makes an unperformed method look like Work, a co-listed System or entity look like a participant or Work performer, a carrier look like a produced result, a measurement or verdict look like generic evidence, or a provenance edge look like the world-side relation itself.

**What this buys.** Downstream work can cite one stable path while a reviewer can still recover the exact work, participants, products, subject results, result epistemes, sources, direct relations, currentness, and bounded use that the path represents.

**Not this pattern when.** Use `A.2.4` for the first evidence-use or status-use classification, `A.10` for source recovery and bounded reliance, `A.15.1`, `A.2.1`, and `F.6` for performed Work and its attribution, `A.6.1` for actual operation bindings, `A.15.PROD` when production or inception is current, the exact domain pattern for its local result, `C.2.1` for the result episteme, `G.11` for currentness, `C.29` for representation correspondence, and `B.3` for assurance. If only one local source-to-use statement is needed, stay in A.10.

Here `path` means a path in a descriptive provenance graph. It is not an action route, method, workflow, transformation flow, universal evidence relation, or generic work-result relation.

### G.6:2 - Problem

Large projects often need to cite a chain that crosses measurement, evaluation, aggregation, production, publication, and later use. The chain becomes unsafe when the graph is allowed to supply facts missing from the governed objects.

The common failures are:

1. **Edge-to-fact inversion.** A drawn edge is treated as proof that work, participation, production, measurement, evaluation, or use occurred.
2. **Generic relation fallback.** Labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` replace the exact direct relation and its governor.
3. **Result collapse.** Subject result, result episteme, carrier, outcome, assurance, and later decision become one generic result node.
4. **Declaration-to-runtime collapse.** A `MethodDescription`, operation signature, policy, clause, or plan is read as an actual run and its bindings.
5. **Hidden crossing.** A path silently crosses context, reference plane, edition, source order, or currentness window.
6. **Refresh fanout.** One changed source or relation forces a global rerun because the smallest affected path slice cannot be found.

### G.6:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Compact citation versus subject patternship | One path is easy to cite, but each represented fact and relation must remain with its exact governor. |
| Graph readability versus ontic force | Nodes and edges make a chain legible; their presence cannot make any represented relation obtain. |
| Result continuity versus result collapse | A path may connect measurement, evaluation, aggregation, and decision while preserving every local result and result episteme. |
| Reusable declaration versus performed occurrence | Methods, descriptions, policies, and clauses may be cited, but dated work and actual bindings remain separate. |
| Cross-context reuse versus hidden loss | Bridges, editions, time windows, source order, and currentness remain visible at the path slice that depends on them. |
| Refresh locality versus stale reliance | Stable addresses let one changed object or direct relation reopen only the affected path or slice. |

### G.6:4 - Solution — cite independently governed objects and relations

Create an `EvidenceGraph` only after the relied-on claim or bounded use and its supporting objects have been recovered. The graph is a declarative, addressable representation. Each node record cites one independently governed object; each asserted edge record cites one independently established direct relation. `PathId`, `PathSliceId`, and the provenance ledger add citation and refresh locality, not world-side facts.

#### G.6:4.1 - Subject-pattern map

| Represented claim or object | Subject pattern before G.6 represents it |
| --- | --- |
| Reusable method, generic participants, parameters, effects, and conditions | exact `U.Method`; `A.3.2` for its `U.MethodDescription` |
| Admitted dated Work, its actual performer Systems and F.6 attribution, any assignment identifier consumed by the path, enactment, resources, and direct participation or binding facts | `A.15.1`, `A.2.1`, and `F.6` under the Work-recovery rule below; the exact direct participation or resource relation; and `A.6.1` for operation-application bindings |
| Production or inception of an entity or episteme | the exact production relation and `A.15.PROD` when its entry condition is met |
| Measurement result and its measurement-specific basis | `C.16` |
| Acceptance-clause application or other runtime evaluation result | `G.4` or the exact formal, conformance, diagnostic, causal, comparison, selection, gate, or decision governor |
| Work-resource aggregation result | `B.1.6` |
| Durable episteme that states a local result | `C.2.1`; it remains distinct from the domain result |
| Outcome, later action, acceptance, gate passage, permission, or decision | its exact work and domain governor, including `C.11` or `A.21` when applicable |
| Source publication, carrier, copy, extraction, or publication occurrence | `E.17` family plus the exact source relation and the declaration or pattern that defines it |
| Representation correspondence | `C.29` |
| Bridge, congruence, loss, or cross-context transfer | `F.9` |
| Transformation-flow structure distinct from performed work | `E.18` and `E.18.2` |
| First evidence/status use, provenance and bounded reliance, currentness, or assurance | `A.2.4`, `A.10`, `G.11`, or `B.3` respectively |

G.6 does not substitute for any row. If the subject pattern or relation cannot be recovered, the path records an unresolved gap and cannot present that edge as obtaining.

Do not add a local `U.EvidenceRole` or turn proof, measurement, benchmark, source, or status labels into system-role kinds. For any claim that a producer, verifier, laboratory, issuer, or maintainer participates, recover the exact direct relation, the participants it declares, and the place each actual participant fills. Other nearby facts—for example, a local system-role kind, assignment, Work occurrence, responsibility, authority, or permission—are separate and may be cited only when they independently obtain; none establishes participation. Do not infer that a passive laboratory or produced entity performs Work merely because the path cites it.

**Work recovery and compact citation.** Before G.6 represents an occurrence admitted under `U.Work`, its subject account must already establish the actual performer System or Systems, enacted Method, temporal extent, and containing System. For each performer, name the assignment occurrence that covers the Work and its declared `U.SystemRoleAssignment` species. Name every participant that determines the assignment's identity, show that its predicate holds throughout the Work interval, identify its holder as that performer, and establish the F.6 `performedUnderAssignment` relation for the Work–assignment pair. A compact G.6 path may omit an assignment identifier when no receiving use consumes it; the omission changes only the citation, not the assignment or attribution facts. Merely listing an assignment beside Work establishes no relation between them.

#### G.6:4.2 - EvidenceGraph as a representation

An `EvidenceGraph` is a typed directed graph used for provenance citation and replay. It may project a dependency-closed slice of independently governed objects and relations. It is not a holarchy, work plan, method, transformation flow, result algebra, or proof that its contents obtain.

Minimal graph fields:

```text
EvidenceGraph:
  EvidenceGraphId
  ReliedOnClaimOrBoundedUseRef
  BoundedContext
  ReferencePlane
  RepresentedNodeRecords
  RepresentedRelationEdgeRecords
  TimeWindowOrPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  GraphPathAddressingRule
  C29RepresentationRefs
```

A node record is a projection, not a new universal object kind:

```text
RepresentedNodeRecord:
  GraphNodeId
  RepresentedObjectRef
  ObjectKindAsGoverned
  SubjectPatternLocator
  ContextEditionOrTimeQualification?
  RepresentationRef
```

The node set may cite exact Work occurrences and their actual performer Systems. It may also cite, for example, local system-role kinds, assignment occurrences whose identities the path uses, direct participation and binding facts, produced entities, subject results, C.2.1 result epistemes, outcomes, source publications, carriers, currentness results, reliance dispositions, and later Work. Every cited Work occurrence still depends on the complete A.15.1 and F.6 account stated in §4.1. Co-listing creates no relation among Work, assignments, passive participants, bindings, results, epistemes, sources, or graph projections.

An asserted edge is also a projection:

```text
RepresentedRelationEdgeRecord:
  GraphEdgeId
  DirectRelationRef
  DirectRelationKindRef
  ActualParticipantRefs
  SubjectPatternLocator
  ObtainingClaimRef
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Before the edge enters a relied-on path, the exact direct relation must already be established under its governor. The participant refs in the edge must match that relation; adjacency, direction, shared identifiers, timestamps, source order, or visual layout cannot supply them. `RepresentationRef` points outward to the applicable C.29 correspondence when that correspondence is current.

G.6 defines no fallback core edge vocabulary. Legacy or display labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, `derivedFrom`, `usesMethodDescription`, `citesSource`, or `evidences` are navigation prompts only. Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, premise, reference, argument, or other direct relation before asserting the edge as obtaining.

#### G.6:4.3 - PathId and PathSliceId

A `PathId` identifies one claim-local path inside an `EvidenceGraph`. A `PathSliceId` identifies the same path under a declared time window, reference plane, bounded context, edition, bridge, policy, or selected object/relation subset.

Use this compact record:

```text
PathCitationRecord:
  ReliedOnClaimOrBoundedUseRef
  EvidenceGraphRef
  PathId
  PathSliceId
  BoundedContext
  ReferencePlane
  RepresentedObjectRefs
  RepresentedDirectRelationRefs
  SubjectPatternLocators
  SourcePublicationAndCarrierRefs
  C29RepresentationRefs
  TimeWindowOrFreshnessPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  DownstreamWorkRef?
  ExactDownstreamUseRelationRef?
  A10RelianceDispositionRef?
  NotCarried
  UnresolvedRelationGaps
  ReopenTrigger
```

`NotCarried` names every stronger use that the path does not establish: Work occurrence, participation, production, claim truth, assurance, approval, permission, gate passage, release, causal identification, benchmark superiority, acceptance, or decision. Actual downstream use requires an admitted dated Work account under §4.1's Work-recovery rule and one exact premise, reference, operation-argument, decision-use, or other direct relation; path availability or citation is not actual use.

#### G.6:4.4 - Provenance ledger

A `ProvenanceLedger` is a citable replay index over `PathCitationRecord` entries. It is not a work-progress log, result registry, review-comment log, process-status log, or ontic source.

```text
ProvenanceLedger:
  LedgerId
  EvidenceGraphRef
  PathCitationRecords
  RepresentedObjectIndex
  RepresentedDirectRelationIndex
  SourceOrderPolicy
  CurrentnessPolicy
  PrivacyOrDisclosureBoundary
  RefreshScopeRule
```

The ledger may cite work, participants, produced entities, domain results, result epistemes, outcomes, sources, transformations, representation correspondences, provenance, and later uses. A row establishes none of them. Use a ledger when several downstream consumers need the same path family; do not create one merely because a local A.10 account is easy to write.

#### G.6:4.5 - Refresh and source return

Reopen the smallest affected `PathId`, `PathSliceId`, node projection, or relation-edge projection when any cited object, direct relation, governor, source, bridge, representation correspondence, edition, policy, time window, currentness result, or reliance boundary changes.

If the direct relation no longer obtains or its proof becomes unavailable, remove it from the relied-on path or mark the exact unresolved gap. Do not preserve the edge from graph history, infer a replacement relation, rerun unrelated paths, or certify a new downstream result through refresh alone.

#### G.6:4.6 - Declarative representation discipline

`EvidenceGraph`, `PathId`, `PathSliceId`, and `ProvenanceLedger` tell a reader which already governed account is being cited. They do not tell a worker what to do and they do not reconstruct missing world-side facts.

| Current phrase or artifact | Required recovery before G.6 representation |
| --- | --- |
| method, protocol, algorithm, clause, or policy | exact reusable declaration; when the path cites dated Work, recover it separately under §4.1; when it cites actual operation bindings, recover them under A.6.1 |
| work trace, run, test, audit, measurement, or evaluation | admitted dated Work and actual performer Systems under §4.1's Work-recovery rule; enacted Method, resources, exact direct participation facts, and A.6.1 binding facts remain separate; expose an assignment identifier only when the receiving use consumes it |
| produced carrier, model, report, or episteme | exact produced entity and production/inception relation |
| reading, score, verdict, estimate, aggregate, diagnosis, or outcome | exact domain result and direct governor; distinct C.2.1 episteme when durably stated |
| publication, view, export, or graph rendering | exact source/publication relation and C.29 representation correspondence when current |
| evidence, provenance, currentness, reliance, or assurance | A.2.4/A.10, G.11, and B.3 under their separate entry conditions |
| later acceptance, gate, release, or decision | separate dated Work admitted under §4.1, local result, and exact later-use relation |

#### G.6:4.7 - Extension wiring without core drift

Selector, benchmark, assurance, refresh, or telemetry patterns may require additional pins in `PathCitationRecord`. They may cite `PathId` or `PathSliceId`, but they do not mint a universal edge, result, evidence, or criterion-participant relation. Any added graph record still names the exact represented object or direct relation and its governor.

`G.5` may cite a path for selector explanation, `G.9` for benchmark replication, `G.11` for local refresh, and B.3 for an assurance input. Their selection, benchmark, currentness, and assurance results remain their own.

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Measurement, acceptance, and decision

C.16 dated measurement work binds the pressure measurand, detector, calibration, model, input quantities, and uncertainty propagation and obtains a pressure measurement result. A distinct C.2.1 episteme states that result. Later G.4 `EvaluationWork` applies one declared acceptance clause through exact A.6.1 bindings and obtains `unknown`; another C.2.1 episteme states that verdict. Later C.11 decision work uses the verdict episteme through an exact premise relation and defers.

G.6 may give this chain one `PathId` only after the measurement, work, binding, result, episteme, clause-application, premise, and decision relations are independently established. Its nodes keep raw detector output, indication, actual pressure, measurement result, verdict, and decision distinct. Its edges cite the exact relations; none produces the work, verdict, or decision.

#### G.6:5.2 - Resource aggregation

An engine programme has several C.16 resource measurements, dated test-run work occurrences, exact phase and overlap relations, and a shared warm-up allocation rule. B.1.6 dated aggregation work applies `ProgrammeResourcePolicy-v3` and obtains a typed resource vector with propagated uncertainty; a distinct C.2.1 episteme states it.

The G.6 path cites every measurement result and episteme, the work-set and overlap relations, the edition-pinned policy, aggregation work, aggregation result, sources, and representation refs. The ledger does not make epoch labels into work parts, allocate the warm-up energy, perform uncertainty propagation, or turn the aggregate into an emissions verdict.

#### G.6:5.3 - Produced model and benchmark use

Dated training work has exact actual bindings and, when the production claim is current, an A.15.PROD-governed relation to one produced model edition. Separate benchmark-evaluation work applies its declared method and dataset edition and obtains a result under the benchmark's direct governor; a C.2.1 episteme states that result. A source publication and model card expose selected claims under E.17/C.29 relations. G.11 supplies currentness when later use depends on edition or freshness.

A G.6 `PathSliceId` may cite that dependency chain for replication. The graph does not infer training from the model's presence, participation from a roster, evaluation from the protocol, superiority from the score, or deployment permission from the model card.

#### G.6:5.4 - Dashboard status cue

A dashboard cell shows `Ready`. F.10 governs the status-use classification; A.10 recovers the source, query work, provenance, currentness, bounded reliance, and rival explanation. G.6 is entered only when a downstream audit or release package needs a stable path through those already established relations. The visible cue, graph path, and ledger row establish neither gate passage nor release.

### G.6:6 - Bias-Annotation

| Bias | Guard |
| --- | --- |
| Graph-authority bias | A node or edge represents an object or direct relation only after its governor establishes it. |
| Generic-edge bias | Reject fallback `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, and `evidences` relations; recover the exact direct relation. |
| Result-node bias | Keep subject result, result episteme, carrier, outcome, assurance, and later action distinct. |
| Declaration-runtime bias | A method, description, policy, clause, signature, or plan establishes no occurrence or actual binding. |
| Provenance-as-truth bias | Origin and history support only their named bounded claim; provenance is not truth, safety, approval, or assurance. |
| Path-as-workflow bias | Graph path identity supports citation and refresh; actual work and transformation flow retain their subject patterns. |
| Ledger-process bias | The ledger contains replayable provenance records, not campaign status, review proof, or work-progress notes. |

### G.6:7 - Conformance Checklist

| ID | Check | Repair if missing |
| --- | --- | --- |
| `CC-G6-01` Exact use | Is one relied-on claim or bounded downstream use named? | Name it, or stay in local A.10 source recovery. |
| `CC-G6-02` Object projection | Does every node cite an exact independently governed object, kind, governor, qualification, and representation ref? | Recover the object or record an unresolved gap; do not mint a graph-only world object. |
| `CC-G6-03` Relation prerequisite | Does every asserted edge cite one exact direct relation, its actual participants, governor, obtaining claim, and context? | Establish the direct relation first or remove the edge from the relied-on path. |
| `CC-G6-04` No fallback edge | Are legacy or display labels prevented from acting as universal relations? | Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, or later-use relation. |
| `CC-G6-05` Work boundary | Are reusable Method and MethodDescription, dated Work, each actual performer and its F.6 attribution, any cited assignment identifier, resources, direct participation, and A.6.1 bindings distinct? | Use A.15.1, A.2.1, and F.6 to establish the complete Work account for each performer; a compact path may omit an unused assignment identifier. Use A.6.1 for actual operation bindings and the exact direct relation for every other participant claim. |
| `CC-G6-06` Result boundary | Are produced entity, subject result, result episteme, carrier, outcome, assurance, and later action distinct and independently identified under exact predicates? | Handle each through the exact predicates and assertions located in A.15.PROD, the domain result pattern, C.2.1, E.17/C.29, B.3, or the later-action source. |
| `CC-G6-07` Source and representation | Are source publication, carrier, copy/transform chain, and C.29 correspondence explicit when current? | Recover those relations before treating the graph rendering as source truth. |
| `CC-G6-08` Time and crossing | Are bounded context, plane, window, bridge/loss, edition, policy, source order, and G.11 currentness visible where they limit use? | Add the exact refs or narrow/block the path slice. |
| `CC-G6-09` Provenance and use | Are A.2.4/A.10 evidence/status use, A.10 provenance/reliance, downstream work, and exact use relation separate? | Recover the direct use; path citation or membership is not actual reliance. |
| `CC-G6-10` Ledger boundary | Does the ledger merely index already established objects and relations, with `NotCarried`, gaps, and local reopen triggers? | Remove process status, generic result fields, and fact-creating language. |

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Edge as fact | Drawing or storing an edge is mistaken for an obtaining relation. | Establish the exact direct relation under its governor, then cite it through a representation record. |
| Universal evidence edge | `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` absorbs several relation families. | Replace the label with the exact formal, measurement, work, production, source, use, or other direct relation. |
| MethodDescription as run trace | Generic declarations acquire actual participants, time, or results by graph membership. | Ground dated Work and each actual performer through §4.1's Work-recovery rule; keep Method enactment, resources, direct participation, and A.6.1 bindings separate. Expose an assignment identifier only when the receiving use consumes it. |
| Generic result node | Measurement, evaluation, aggregation, episteme, outcome, and decision collapse. | Keep each local result under its domain governor and each durable assertion under C.2.1. |
| Provenance as result or assurance | A path or ledger row is read as truth, currentness, safety, permission, or acceptance. | Use A.10, G.11, and B.3 under their entry conditions, and state the exact local result under its applicable predicate and pattern. |
| Citation as actual use | A downstream record cites a path and is assumed to have used it. | Ground dated downstream work and one exact premise, reference, argument, or decision-use relation. |
| Workflow overread | A declarative path becomes a method or action route. | Handle Work under A.15.1 and transformation-flow structure under E.18; limit G.6 to representation and citation. |
| Global refresh | One changed source or relation reopens every graph. | Reopen only the affected path, slice, node projection, or relation-edge projection. |

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition, and time changes reopen the smallest path slice;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their subject patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

### G.6:10 - Rationale

A.10 recovers one relied-on claim, its source/provenance account, and bounded reliance. G.6 adds stable graph-path identity, slicing, shared citation, and path-local refresh when several downstream consumers need the same dependency-closed representation.

That representational gain does not justify a second ontology of evidence edges. Work, participants, products, subject results, result epistemes, outcomes, sources, provenance, currentness, and later uses already have direct governors. G.6 therefore projects their exact refs and direct relations, and C.29 governs the representation correspondence when current. This makes a complex chain readable without allowing graph topology to create facts.

The ledger is likewise an index over established provenance, not a result store or process log. Missing relation evidence remains a visible gap; it is never repaired by drawing a more persuasive path.

### G.6:11 - SoTA-Echoing

Source qualification was checked against the publishers' current surfaces on 2026-07-30. These decisions remain qualified through 2027-07-30 unless a new Recommendation, specification edition, maintenance status, or replacement changes the adopted contract earlier. Internal FPF neighbour authority stays in Relations; it is not presented as an external source decision.

| Exact source and source-use decision | Visible G.6 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable entity/activity/agent references only as a representation discipline for exact FPF objects and direct relations. | `RepresentedNodeRecord`, `RepresentedRelationEdgeRecord`, the measurement-to-decision case, and `CC-G6-02/03` require every node and edge to cite an independently governed object or obtaining relation with its governor and qualification. | A PROV-shaped class, activity, agent, qualified association, or derivation does not establish FPF work, participation, production, result, truth, currentness, or later use. | Reopen only §4.2's node/edge rules, the measurement-to-decision path, and `CC-G6-02/03` if PROV-O's qualified-relation contract changes. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content provenance. | `PathCitationRecord` carries source publication/carrier, C.29 representation, edition/policy, currentness, and `NotCarried`; the produced-model case and `CC-G6-07/08` retain the exact content carrier, transform chain, trust regime, and version. | A valid manifest, visible Content Credential, ingredient chain, or authenticity mark does not establish truth of the represented world state, authorship beyond its exact assertion, work, safety, permission, or adequacy. | Reopen only those `PathCitationRecord` source/version fields, the produced-model carrier slice, and `CC-G6-07/08` when C2PA changes manifest/assertion identity, validation, trust, or version semantics. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) with [in-toto Attestation Framework v1.2 and `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The produced-model/benchmark path names training work, produced model edition, dataset/method edition, benchmark work/result, source inputs, publication/carrier, verifier context, and currentness; `CC-G6-07/08` keep those refs replayable without one generic attestation edge. | A signed statement, provenance predicate, SLSA level, or verification summary does not prove an uncited build/work/result relation, benchmark superiority, runtime safety, release approval, gate passage, or assurance. | Reopen only the attestation-bearing fields of that path slice, the produced-model/benchmark case, and `CC-G6-07/08` when the adopted SLSA provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** credential subject, issuer, holder, verifier, status, context, and validity separation for a path that cites an independently governed credential/status use. | `PathCitationRecord` separates source/carrier/currentness refs, downstream work, exact use relation, A.10 reliance disposition, and `NotCarried`; the dashboard-status case and `CC-G6-09` require the status cue, query/use work, verifier or relying context, and actual reliance to remain distinct. | A valid credential, successful proof check, holder presentation, status value, or graph membership does not become claim truth, authorization, permission, gate passage, release, actual reliance, or assurance. | Reopen only those credential/status/use fields, the dashboard-status path, and `CC-G6-09` if VC 2.0 or its adopted status/validity contract changes. |
| Pineau et al., [*Improving Reproducibility in Machine Learning Research*, JMLR 22(164), 2021](https://jmlr.org/papers/v22/20-303.html), and Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596) — **adapt** exact method, dataset, metric, evaluation condition, version, limitation, and run-evidence disclosure as inputs to a replayable benchmark path. | The produced-model/benchmark case, dependency-closed `PathSliceId`, and `CC-G6-02/07/08` keep model edition, training/evaluation work, dataset and method editions, local result, result episteme, source carrier, limitations, and currentness separately addressable. | A reproducibility checklist, model card, disclosed score, or limitation does not establish that training or evaluation occurred, that the reported result is current, that one model is superior, or that deployment is permitted. | Reopen only the model/benchmark slice fields, that worked case, and `CC-G6-02/07/08` if the adopted reproducibility or reporting contract changes. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) — **adapt** the separation between cited evidence and the structure, maintenance, and evaluation of an assurance case. | `NotCarried` names assurance explicitly, the subject-pattern map and §4.7 handle assurance under B.3, and `CC-G6-10` permits the ledger to index evidence paths without becoming an assurance result. | A complete-looking evidence path, ledger entry, confidence label, or signed carrier is not an assurance claim, safety result, readiness result, compliance result, or release confidence. | Reopen only `NotCarried`, the B.3 extension boundary, one assurance-input path, and `CC-G6-10` if the adopted assurance-case evidence or maintenance boundary changes. |

Source refresh is local: replay the changed row's named record fields, rule or case, and checklist rows first. Widen only when that replay contradicts another current G.6 locus; a changed source cannot by itself create a represented object, obtaining relation, work occurrence, result, currentness, reliance, assurance, permission, or decision.

### G.6:12 - Relations

* **Builds on:** `A.10` for source recovery, provenance, bounded reliance, and graph-edge discipline; `A.2.4` for first-use evidence/status classification; `C.2.1` for claim and result epistemes; `C.29` for representation correspondence.
* **Coordinates with:** `A.15.1`, `A.2.1`, and `F.6` for admitted dated Work, the exact covering assignment and attribution for each actual performer, and proportional citation of assignment identifiers; `A.6.1` for actual operation bindings; the exact pattern for each participation relation; `A.15.PROD` for production or inception when current; `C.16` for measurement results; `G.4` for runtime evaluation results; `B.1.6` for work-resource aggregation results; `C.28` for causal use; `F.10` for status use; `F.9` for bridge and loss; `E.18` and `E.18.2` for transformation-flow structure; `G.11` for currentness; `B.3` for assurance; `E.17` for publication; and the pattern that defines each exact formal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, or decision claim cited by a path.
* **Used by:** selector, benchmark, replication, audit, refresh, assurance, maturity, and release patterns that need stable provenance-path citation, including `G.5`, `G.9`, and `G.11`.
* **Does not govern:** any represented work occurrence, participation, production, local result, result episteme, outcome, source publication, representation correspondence, currentness result, assurance, later use, or stronger conclusion named in `NotCarried`.

### G.6:End

