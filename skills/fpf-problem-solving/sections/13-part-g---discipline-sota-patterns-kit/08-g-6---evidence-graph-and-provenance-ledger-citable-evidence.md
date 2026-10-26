## G.6 - Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths

> **Type:** Evidence and provenance pattern
> **Status:** Stable
> **Normativity:** Normative where conformance rows say so; examples and SoTA rows are informative guidance.

### G.6:1 - Problem Frame

Use this pattern when a later user must cite, replay, audit or refresh a chain of established facts, such as a measurement, an acceptance judgement and a decision. Give that chain a stable address while preserving the evidence and rules for its members.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is an addressable provenance representation: one `EvidenceGraph`, its `PathId` or `PathSliceId`, and any ledger entry that makes the path replayable. G.6 governs path identity, slicing, citation and refresh of the representation. The represented facts remain governed by their subject patterns.

**First useful move.** Name the relied-on claim or bounded use, then list the exact object refs and direct relation refs needed to replay it. For every relation record its direct governor and obtaining claim. Only then draw the path. Keep an unresolved relation as a gap; do not turn it into a graph edge asserted as obtaining.

**What goes wrong if missed.** A tidy graph makes an unperformed method look like Work, a co-listed System or entity look like a participant or Work performer, a carrier look like a produced result, a measurement or verdict look like generic evidence, or a provenance edge look like the world-side relation itself.

**What this buys.** A downstream user can cite one path and recover its supporting facts, their qualifications and the direct relations that connect them. A changed premise can be traced to every dependent path within the established coverage.

**Not this pattern when.** If the required fact or relation has not been established, use its subject pattern in §4.1 first. If only one local source-to-use statement is needed, stay in A.10.

Here `path` means a path in a descriptive provenance graph, not an action route.

### G.6:2 - Problem

Large projects often need to cite a chain that crosses measurement, evaluation, aggregation, production, publication, and later use. The chain becomes unsafe when the graph is allowed to supply facts missing from the governed objects.

The common failures are:

1. **Edge-to-fact inversion.** A drawn edge is treated as proof that work, participation, production, measurement, evaluation, or use occurred.
2. **Generic relation fallback.** Labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` replace the exact direct relation and its governor.
3. **Result collapse.** Subject result, result episteme, carrier, outcome, assurance, and later decision become one generic result node.
4. **Declaration-to-runtime collapse.** A `MethodDescription`, operation signature, policy, clause, or plan is read as an actual run and its bindings.
5. **Hidden crossing.** A path silently crosses context, reference plane, edition, source order, or currentness window.
6. **Incomplete refresh reach.** A changed premise prompts a global rerun or a repair of only the first located slice because its actual dependent paths have not been identified.

### G.6:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Compact citation versus the represented facts' governing rules | One path is easy to cite, but each represented fact and relation must remain with its exact governor. |
| Graph readability versus ontic force | Nodes and edges make a chain legible; their presence cannot make any represented relation obtain. |
| Result continuity versus result collapse | A path may connect measurement, evaluation, aggregation, and decision while preserving every local result and result episteme. |
| Reusable declaration versus performed occurrence | Methods, descriptions, policies, and clauses may be cited, but dated work and actual bindings remain separate. |
| Cross-context reuse versus hidden loss | Bridges, editions, time windows, source order, and currentness remain visible at the path slice that depends on them. |
| Refresh locality versus stale reliance | One changed premise may affect several paths; complete dependency coverage excludes unrelated paths without losing a dependent use. |

### G.6:4 - Solution — cite independently governed objects and relations

Create an `EvidenceGraph` only after the relied-on claim or bounded use and its supporting objects have been recovered. The graph is a declarative, addressable representation. Each node record cites one independently governed object; each asserted edge record cites one independently established direct relation. `PathId`, `PathSliceId`, and the provenance ledger add citation and refresh locality, not world-side facts.

#### G.6:4.1 - Subject-pattern map

| Represented claim or object | Subject pattern before G.6 represents it |
| --- | --- |
| Reusable method, generic participants, parameters, effects, and conditions | `A.3.1` for the exact `U.Method`; `A.3.2` for its `U.MethodDescription` |
| Independently admitted dated Work and its exact actual performer refs; optional obtaining F.6 relation and assignment occurrence refs when the path expressly consumes attribution; enactment, resources, and direct participation or binding facts | `A.13` for each exact actual performer and `A.15.1` for independent Work admission; `F.6` and `A.2.1` only when the path represents precise assignment-bound attribution; the exact direct participation or resource relation; and `A.6.1` for operation-application bindings |
| Production or inception of an entity or episteme | one exact local A.15.PROD claim when its entry condition is met, or a direct subject predicate under its own pattern |
| Measurement result and its measurement-specific basis | `C.16` |
| Acceptance-clause application or other runtime evaluation result | `G.4` or the exact formal, conformance, diagnostic, causal, comparison, selection, gate, or decision governor |
| Work-resource aggregation result | `B.1.6` |
| Durable episteme that states a local result | `C.2.1`; it remains distinct from the domain result |
| Outcome, later action, acceptance, gate passage, permission, or decision | its exact work and domain governor, including `C.11` or `A.21` when applicable |
| Source publication, carrier, copy, extraction, or publication occurrence | `E.17` for a source-backed face and source return; `E.24.PUB` for an obtaining publication occurrence; the direct rule for each copy, extraction or source relation |
| Representation correspondence | `C.29` |
| Bridge, congruence, loss, or cross-context transfer | `F.9` |
| Transformation-flow structure distinct from performed work | `E.18` and `E.18.2` |
| First evidence/status use, provenance and bounded reliance, currentness, or assurance | `A.2.4`, `A.10`, `G.11`, or `B.3` respectively |

If the subject pattern or relation cannot be recovered, the path records an unresolved gap and cannot present that edge as obtaining.

Do not add a local `U.EvidenceRole` or turn proof, measurement, benchmark, source, or status labels into system-role kinds. For any claim that a producer, verifier, laboratory, issuer, or maintainer participates, recover the exact direct relation, the participants it declares, and the place each actual participant fills. Other nearby facts—for example, a local system-role kind, assignment, Work occurrence, responsibility, authority, or permission—are separate and may be cited only when they independently obtain; none establishes participation. Do not infer that a passive laboratory or produced entity performs Work merely because the path cites it.

**Work recovery and compact citation.** Before G.6 represents dated `U.Work`, its subject account must already recover each exact actual performer through A.13 and admit that Work independently under `A.15.1`. Include an assignment occurrence and obtaining F.6 relation only when the graph path or receiving use expressly consumes precise assignment-bound attribution; any present attribution must use the same obtaining A.13 assignment. If a required Work or performer ref is absent, record a Work gap. If an expressly consumed F.6 ref is absent or unresolved, retain the Work node and record an attribution gap rather than suppressing the Work. G.6 neither re-admits the Work nor retests assignment species, occurrence identity, holder, classification, predicate duration, or interval coverage. Merely listing an assignment beside Work establishes no relation between them.

#### G.6:4.2 - EvidenceGraph as a representation

An `EvidenceGraph` is a typed directed graph used for provenance citation and replay. It may project a dependency-closed slice of independently governed objects and relations.

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

A node record is a projection:

```text
RepresentedNodeRecord:
  GraphNodeId
  RepresentedObjectRef
  ObjectKindAsGoverned
  SubjectPatternLocator
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Node records use the object kinds and subject patterns in §4.1. Every cited Work occurrence uses the independently established performer and A.15.1 Work refs specified there; add F.6 refs only when precise attribution is consumed. Co-listing creates no relation among the cited objects.

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

G.6 defines no fallback core edge vocabulary. Legacy or display labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, `derivedFrom`, `usesMethodDescription`, `citesSource` or `evidences` are navigation prompts. Recover the exact direct relation and its governor before asserting an edge as obtaining.

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

`NotCarried` names the stronger claim or use at issue that the path does not establish. Recover the exact premise, reference, operation-argument, decision-use, or other direct relation for actual downstream use. If the use asserts dated `U.Work`, cite its independently admitted A.15.1 Work ref and A.13-qualified performer refs. Add attribution refs only when the use expressly consumes precise assignment-bound attribution. Path availability or citation alone does not establish that use.

#### G.6:4.4 - Provenance ledger

A `ProvenanceLedger` indexes `PathCitationRecord` entries for citation and replay. Its object and relation indexes let a user find paths that cite the same basis.

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

Use a ledger when several downstream consumers need the same path family; a single local source-to-use account can remain in A.10.

#### G.6:4.5 - Refresh and source return

When a cited object, direct relation, governor, source, bridge, representation correspondence, edition, policy, time window, currentness result or reliance boundary changes, start at its node or relation-edge projection. Identify the exact changed claim or condition and the receiving use it may alter. Use the represented-object and direct-relation indexes to locate other `PathId` or `PathSliceId` values that consume the same basis. The first located slice is an entry to this inquiry, not its completion boundary.

For each candidate path, recover the actual premise, evidence-use, operation-argument or other direct use under its governor. Follow that dependence while a receiving claim, action or required check can change. A shared calibration, causal assumption or source conclusion can affect several otherwise separate paths; include each affected use. Common storage, a citation or graph reachability alone establishes no such dependence. When a changed source requires discovery beyond an adequate existing index, use A.10.1 for its bounded search, direct-use test and coverage limits. An unsearched or unresolved branch is a limit on the conclusion, not an unaffected branch.

Retain independent results and their qualified paths. For an affected branch, return to the subject pattern to determine whether the available basis supports the same result, a narrower use, a changed result or a scoped gap. If a represented relation no longer obtains or its required support is unavailable, remove it from the relied-on path or mark that gap; retain the earlier account for its historical use where warranted. G.11 uses the resulting dependency scope to decide which refresh actions, if any, are needed. Updating a projection does not establish a replacement relation or perform that Work.

#### G.6:4.6 - Declarative representation discipline

`EvidenceGraph`, `PathId`, `PathSliceId` and `ProvenanceLedger` identify the governed accounts a reader can inspect. When a needed account is missing, return to its subject pattern.

| Current phrase or artifact | Required recovery before G.6 representation |
| --- | --- |
| method, protocol, algorithm, clause, or policy | exact reusable declaration; when the path cites dated Work, recover it separately under §4.1; when it cites actual operation bindings, recover them under A.6.1 |
| work trace, run, test, audit, measurement, or evaluation | independently admitted dated Work ref and A.13-qualified actual performer refs under §4.1; enacted Method, resources, exact direct participation facts, and A.6.1 binding facts remain separate; expose an assignment occurrence and obtaining F.6 relation only when the path expressly consumes precise assignment-bound attribution |
| produced carrier, model, report, or episteme | exact produced entity and either its subject-specific direct production relation, when the subject pattern declares one, or the one local A.15.PROD production-work or inception claim that the current use needs |
| reading, score, verdict, estimate, aggregate, diagnosis, or outcome | exact domain result and direct governor; distinct C.2.1 episteme when durably stated |
| publication, view, export, or graph rendering | exact source relation, E.17 source-backed face, E.24.PUB publication occurrence, and C.29 representation correspondence when each is current |
| evidence, provenance, currentness, reliance, or assurance | A.2.4/A.10, G.11, and B.3 under their separate entry conditions |
| later acceptance, gate, release, or decision | its local result and exact later-use relation under their direct rules; dated Work admitted under §4.1 when that occurrence is asserted |

#### G.6:4.7 - Extension wiring without core drift

Selector, benchmark, assurance, refresh or telemetry patterns may require additional pins in `PathCitationRecord` and cite `PathId` or `PathSliceId`. Each added record still names its represented object or direct relation and governor.

`G.5` may cite a path for selector explanation, `G.9` for benchmark replication, `G.11` for local refresh, and B.3 for an assurance input. Their selection, benchmark, currentness, and assurance results remain their own.

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Measurement, acceptance, and decision

In this constructed case, a measurement team performs dated C.16 measurement Work with bindings for the pressure measurand, detector, calibration, model, input quantities and uncertainty propagation. Its pressure measurement result is stated in a distinct C.2.1 episteme. An evaluation team later performs G.4 `EvaluationWork`, applying one declared acceptance clause through exact A.6.1 bindings and obtaining `unknown`; another C.2.1 episteme states that verdict. A decision maker then performs C.11 decision Work, uses the verdict episteme through an exact premise relation and defers. The performer and Work references are independently established under §4.1.

G.6 may give this chain one `PathId` only after the measurement, work, binding, result, episteme, clause-application, premise, and decision relations are independently established. Its nodes keep raw detector output, indication, actual pressure, measurement result, verdict, and decision distinct. Its edges cite the exact relations; none produces the work, verdict, or decision.

#### G.6:5.2 - Resource aggregation

An engine programme has several C.16 resource measurements, dated test-run Work occurrences, exact phase and overlap relations, and a shared warm-up allocation rule. An aggregation team performs dated B.1.6 aggregation Work, applies `ProgrammeResourcePolicy-v3` and obtains a typed resource vector with propagated uncertainty; a distinct C.2.1 episteme states it. The path uses the independently established performer and Work refs.

The G.6 path cites every measurement result and episteme, the work-set and overlap relations, the edition-pinned policy, aggregation work, aggregation result, sources, and representation refs. Epoch labels alone do not establish work-part relations. Warm-up energy allocation and uncertainty propagation are performed in the aggregation work; an emissions verdict remains a separate result.

#### G.6:5.3 - Produced model and benchmark use

A training team performs dated training Work with exact actual bindings and, when an inception or completion claim is current, one local A.15.PROD claim. An evaluation team separately performs benchmark-evaluation Work, applies its declared method and dataset edition and obtains a result under the benchmark's direct governor; a C.2.1 episteme states that result. Both Work occurrences use their independently established performer refs. E.17 governs the model card's source-backed face and return to the selected claims, E.24.PUB their actual audience availability, and C.29 any consumed representation correspondence. G.11 supplies currentness when later use depends on edition or freshness.

A G.6 `PathSliceId` may cite that dependency chain for replication. The graph does not infer training from the model's presence, participation from a roster, evaluation from the protocol, superiority from the score, or deployment permission from the model card.

#### G.6:5.4 - Dashboard status cue

A dashboard cell shows `Ready`. F.10 governs the status-use classification; A.10 recovers the source and provenance for bounded reliance, with query Work, currentness, and a live rival explanation when those facts affect the claim. G.6 is entered only when a downstream audit or release package needs a stable path through those already established relations. The visible cue, graph path, and ledger row establish neither gate passage nor release.

#### G.6:5.5 - One calibration basis, several receiving paths

In a constructed inspection account, `Path-P1` connects measurement result M1 to acceptance result V1, and `Path-P2` connects M2 to V2. Both measurements use the same calibration qualification K through independently established relations. A later selection S uses both acceptance results. `Path-P3`, stored in the same publication, uses a different calibration and supports an unrelated result.

A correction to K first appears in P1's projection. The ledger's indexes also locate P2, and the receiving-use relations lead from V1 and V2 to S. Reconsider both branches and S under their subject patterns. P3 stays outside this reach because it does not consume the changed qualification. Two paths citing K still cite one common basis; their count supplies no independent corroboration. If the index cannot cover another receiving store, state that discovery limit and use A.10.1 when the receiving question needs that search.

The resulting G.6 account identifies the affected paths and their exact dependencies. G.11:5 continues this case through different branch outcomes and selection of the needed work.

### G.6:6 - Bias-Annotation

| Bias | Guard |
| --- | --- |
| Graph-authority bias | A node or edge represents an object or direct relation only after that object or obtaining relation has been independently established under its governing rule. |
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
| `CC-G6-05` Work boundary | Does each represented Work cite one independently admitted A.15.1 Work ref and its A.13-qualified actual performer refs? Are assignment occurrence and F.6 refs included only when the path expressly consumes precise assignment-bound attribution, with a missing attribution recorded as a gap rather than loss of the Work node? Are Method, MethodDescription, resources, direct participation, and A.6.1 bindings still separate? | Use A.13 and A.15.1 for the already-established performer and Work. Cite A.2.1/F.6 only for an expressly consumed attribution, A.6.1 for actual operation bindings, and the exact direct relation for every other participant claim. |
| `CC-G6-06` Result boundary | Are produced entity, subject result, result episteme, carrier, outcome, assurance, and later action distinct and independently identified under exact predicates? | Handle each through the exact predicates and assertions located in A.15.PROD, the domain result pattern, C.2.1, E.17/E.24.PUB/C.29, B.3, or the later-action source. |
| `CC-G6-07` Source and representation | Are source publication, carrier, copy/transform chain, and C.29 correspondence explicit when current? | Recover those relations before treating the graph rendering as source truth. |
| `CC-G6-08` Time and crossing | Are bounded context, plane, window, bridge/loss, edition, policy, source order, and G.11 currentness visible where they limit use? | Add the exact refs or narrow/block the path slice. |
| `CC-G6-09` Provenance and use | Are A.2.4/A.10 evidence/status use, A.10 provenance/reliance, downstream work, and exact use relation separate? | Recover the direct use; path citation or membership is not actual reliance. |
| `CC-G6-10` Ledger boundary | Does the ledger merely index already established objects and relations, with `NotCarried`, gaps, and local reopen triggers? | Remove process status, generic result fields, and fact-creating language. |
| `CC-G6-11` Affected reach | Does the refresh scope include every established dependent use that can change within the declared coverage, including uses of a shared premise on other paths? | Follow §4.5; retain independent paths, expose unresolved coverage and return each affected judgement to its subject pattern. |

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Edge as fact | Drawing or storing an edge is mistaken for an obtaining relation. | Establish the exact direct relation under its governor, then cite it through a representation record. |
| Universal evidence edge | `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` absorbs several relation families. | Replace the label with the exact formal, measurement, work, production, source, use, or other direct relation. |
| MethodDescription as run trace | Generic declarations acquire actual participants, time, or results by graph membership. | Cite one independently admitted dated Work ref and its A.13-qualified actual performer refs through §4.1. Keep Method enactment, resources, direct participation, and A.6.1 bindings separate; expose an assignment occurrence and F.6 relation only when the path expressly consumes precise assignment-bound attribution. |
| Generic result node | Measurement, evaluation, aggregation, episteme, outcome, and decision collapse. | Keep each local result under its domain governor and each durable assertion under C.2.1. |
| Provenance as result or assurance | A path or ledger row is read as truth, currentness, safety, permission, or acceptance. | Use A.10, G.11, and B.3 under their entry conditions, and state the exact local result under its applicable predicate and pattern. |
| Citation as actual use | A downstream record cites a path and is assumed to have used it. | Establish the exact premise, reference, argument, or decision-use relation; recover dated Work separately under §4.1 when the claim asserts that occurrence. |
| Workflow overread | A declarative path becomes a method or action route. | Handle Work under A.15.1 and transformation-flow structure under E.18; limit G.6 to representation and citation. |
| Global refresh or first-slice stop | A changed premise either reopens every graph or leaves another dependent path unchanged. | Recover all actual dependent uses within the covered scope under §4.5; retain independent paths and expose gaps. |

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition and time changes reopen their full affected dependency scope while preserving independent results;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their subject patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

### G.6:10 - Rationale

A.10 recovers one relied-on claim, its source/provenance account and bounded reliance. G.6 adds stable path identity, slicing and shared citation. Its indexes help locate uses of a changed common basis; A.10.1 supplies further source-change discovery when needed, and G.11 selects refresh from the resulting scope.

That representational gain does not justify a second ontology of evidence edges. Work, participants, products, subject results, result epistemes, outcomes, sources, provenance, currentness, and later uses already have direct governors. G.6 therefore projects their exact refs and direct relations, and C.29 governs the representation correspondence when current. This makes a complex chain readable without allowing graph topology to create facts.

The ledger is likewise an index over established provenance, not a result store or process log. Missing relation evidence remains a visible gap; it is never repaired by drawing a more persuasive path.

### G.6:11 - SoTA-Echoing

The source-use decisions below are based on the publishers' source versions current on 2026-07-30. These decisions remain qualified through 2027-07-30 unless a new Recommendation, specification edition, maintenance status, or replacement changes the adopted contract earlier.

| Exact source and source-use decision | G.6 use | Rejected overread | Direct source-change entry |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable entity/activity/agent references only as a representation discipline for exact FPF objects and direct relations. | `RepresentedNodeRecord`, `RepresentedRelationEdgeRecord`, the measurement-to-decision case, and `CC-G6-02/03` require every node and edge to cite an independently governed object or obtaining relation with its governor and qualification. | A PROV-shaped class, activity, agent, qualified association, or derivation does not establish FPF work, participation, production, result, truth, currentness, or later use. | Start with §4.2's node/edge rules, the measurement-to-decision path, and `CC-G6-02/03` if PROV-O's qualified-relation contract changes. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content provenance. | `PathCitationRecord` carries source publication/carrier, C.29 representation, edition/policy, currentness, and `NotCarried`; the produced-model case and `CC-G6-07/08` retain the exact content carrier, transform chain, trust regime, and version. | A valid manifest, visible Content Credential, ingredient chain, or authenticity mark does not establish truth of the represented world state, authorship beyond its exact assertion, work, safety, permission, or adequacy. | Start with those `PathCitationRecord` source/version fields, the produced-model carrier slice, and `CC-G6-07/08` when C2PA changes manifest/assertion identity, validation, trust, or version semantics. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) with [in-toto Attestation Framework v1.2 and `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The produced-model/benchmark path names training work, produced model edition, dataset/method edition, benchmark work/result, source inputs, publication/carrier, verifier context, and currentness; `CC-G6-07/08` keep those refs replayable without one generic attestation edge. | A signed statement, provenance predicate, SLSA level, or verification summary does not prove an uncited build/work/result relation, benchmark superiority, runtime safety, release approval, gate passage, or assurance. | Start with the attestation-bearing fields of that path slice, the produced-model/benchmark case, and `CC-G6-07/08` when the adopted SLSA provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** credential subject, issuer, holder, verifier, status, context, and validity separation for a path that cites an independently governed credential/status use. | `PathCitationRecord` separates source/carrier/currentness refs, downstream work, exact use relation, A.10 reliance disposition, and `NotCarried`; the dashboard-status case and `CC-G6-09` require the status cue, query/use work, verifier or relying context, and actual reliance to remain distinct. | A valid credential, successful proof check, holder presentation, status value, or graph membership does not become claim truth, authorization, permission, gate passage, release, actual reliance, or assurance. | Start with those credential/status/use fields, the dashboard-status path, and `CC-G6-09` if VC 2.0 or its adopted status/validity contract changes. |
| Pineau et al., [*Improving Reproducibility in Machine Learning Research*, JMLR 22(164), 2021](https://jmlr.org/papers/v22/20-303.html), and Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596) — **adapt** exact method, dataset, metric, evaluation condition, version, limitation, and run-evidence disclosure as inputs to a replayable benchmark path. | The produced-model/benchmark case, dependency-closed `PathSliceId`, and `CC-G6-02/07/08` keep model edition, training/evaluation work, dataset and method editions, local result, result episteme, source carrier, limitations, and currentness separately addressable. | A reproducibility checklist, model card, disclosed score, or limitation does not establish that training or evaluation occurred, that the reported result is current, that one model is superior, or that deployment is permitted. | Start with the model/benchmark slice fields, that worked case, and `CC-G6-02/07/08` if the adopted reproducibility or reporting contract changes. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) — **adapt** the separation between cited evidence and the structure, maintenance, and evaluation of an assurance case. | `NotCarried` names assurance explicitly, the subject-pattern map and §4.7 handle assurance under B.3, and `CC-G6-10` permits the ledger to index evidence paths without becoming an assurance result. | A complete-looking evidence path, ledger entry, confidence label, or signed carrier is not an assurance claim, safety result, readiness result, compliance result, or release confidence. | Start with `NotCarried`, the B.3 extension boundary, one assurance-input path, and `CC-G6-10` if the adopted assurance-case evidence or maintenance boundary changes. |

Start source return at the changed row's named fields, rule, case and checklist rows. Then follow §4.5 through every actual dependent representation and receiving use, including another row when it shares the changed premise. Preserve independently supported accounts. The applicable subject patterns establish any revised relation or result before its graph projection is updated.

### G.6:12 - Relations

* **Builds on:** `A.10` for source recovery, provenance, bounded reliance and graph-edge discipline; `A.10.1` for source-change discovery and affected-use reach; `A.2.4` for first-use evidence/status classification; `C.2.1` for claim and result epistemes; `C.29` for representation correspondence.
* **Coordinates with:** `A.13` and `A.15.1` for already-established exact actual performers and Work; `F.6` and `A.2.1` only when the receiving path expressly consumes precise assignment-bound attribution; `A.6.1` for actual operation bindings; the exact pattern for each participation relation; `A.15.PROD` for production or inception when current; `C.16` for measurement results; `G.4` for runtime evaluation results; `B.1.6` for work-resource aggregation results; `C.28` for causal use; `F.10` for status use; `F.9` for bridge and loss; `E.18` and `E.18.2` for transformation-flow structure; `G.11` for currentness; `B.3` for assurance; `E.17` for source-backed faces and return to source; `E.24.PUB` for obtaining publication occurrences; and the pattern that defines each exact formal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, or decision claim cited by a path.
* **Used by:** selector, benchmark, replication, audit, refresh, assurance, maturity, and release patterns that need stable provenance-path citation, including `G.5`, `G.9`, and `G.11`.
* **Does not govern:** any represented work occurrence, participation, production, local result, result episteme, outcome, source publication, representation correspondence, currentness result, assurance, later use, or stronger conclusion named in `NotCarried`.

### G.6:End
