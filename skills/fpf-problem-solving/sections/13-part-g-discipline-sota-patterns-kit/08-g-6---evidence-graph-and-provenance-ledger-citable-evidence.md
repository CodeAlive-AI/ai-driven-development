## G.6 - Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths

> **Type:** Evidence and provenance pattern
> **Status:** Stable
> **Normativity:** Normative where conformance rows say so; examples and SoTA rows are informative guidance.

### G.6:1 - Problem Frame

Use this pattern when a claim, admission result, assurance result, selector result, maturity transition, benchmark result, or refresh decision needs a citable evidence-provenance path rather than a local evidence-use statement.

Use it when the working question is:

* which evidence-use relations, source records, work occurrences, method descriptions, proof checks, measurements, status-use relations, or causal-use references make the claim traceable;
* that the evidence relation is a graph path in a declared provenance graph, while actual work and transformation-flow claims remain governed by `A.15.1` and `E.18`;
* which time window, bounded context, reference plane, bridge, edition, policy, or source-currentness relation changes the admissible use;
* which downstream selector record, assurance record, release package, benchmark record, audit record, or refresh record may cite the evidence-provenance path without copying the whole evidence table;
* what stronger downstream use is not carried by the evidence-provenance path and which direct pattern governs that use.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is addressable evidence provenance: an `EvidenceGraph`, its graph-path addresses `PathId` and `PathSliceId`, and the provenance ledger entries that make those paths replayable. The pattern governs addressable provenance. It does not create `U.EvidenceRole`, does not make an episteme hold a work-facing role, and does not replace `A.10`, `A.2.4`, `B.3`, `C.28`, or `F.10`.

**First useful move.** Write the smallest `PathCitationRecord`: claim or use, `EvidenceGraphRef`, graph path, bounded context, downstream citation use or evidence-use relation, time window, source or provenance constraints, bridge or edition refs when current, and `NotCarried`.

**What goes wrong if missed.** Evidence is summarized as a story, badge, confidence phrase, benchmark score, proof label, or dashboard tile; downstream users cannot find which sources and checks carried the claim; context crossings are hidden; refresh becomes a global rerun instead of a local path update.

**What this buys.** A selector, auditor, assurance user, benchmark consumer, or refresh record can cite one stable path and later replay exactly the sources, relations, windows, and constraints that made the claim admissible.

**Not this pattern when.** If only one episteme is being used as evidence or status before a full path is needed, use `A.2.4`. If the current question is ordinary evidence relation and source-currentness without Part-G path addressing, use `A.10`. If the claim is assurance, use `B.3`. If the claim is causal use, use `C.28`. If the question is status-family mapping, use `F.10`. If the question is publication, view, source-use, explanation-use, or specification-use, use `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, or `E.10.D2`. If the question is performed work, use `A.15.1`.

### G.6:2 - Problem

Large projects need to rely on evidence that is distributed across proofs, measurements, work traces, source publications, credentials, model cards, benchmarks, bridge records, and status sources. A compact evidence-use statement is often enough for a local claim, but it is not enough when downstream work must cite, replay, compare, refresh, or audit the whole provenance line.

The common failures are:

1. **Narrative provenance.** A report says "because the evidence carries the claim" but does not expose the graph path from claim to evidence relations, sources, checks, and work occurrences.
2. **Hidden crossing.** Evidence accepted in one bounded context, reference plane, edition, or status window is reused in another as if no bridge or currentness relation were needed.
3. **Role drift.** A proof, dataset, status cell, report, or benchmark result is treated as if it held an evidence role, instead of being a value in an evidence-use, status-use, source-use, or provenance relation.
4. **Path metaphor drift.** A graph path is read as an action route or workflow. The pattern then starts teaching work planning or performed work, rather than how a provenance graph is addressed.
5. **Ledger process drift.** A provenance ledger is confused with work-progress, review-comment, or process evidence. The pattern then records development status instead of citable evidence-provenance facts.
6. **Refresh fanout.** A source edit, edition change, decay event, bridge change, or policy change forces a broad "rerun everything" because the affected evidence-provenance paths were never addressable.

### G.6:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Citable provenance versus local evidence use | `A.10` and `A.2.4` can state evidence use; G.6 adds stable path identity only when downstream citation or refresh needs it. |
| Graph path and work claims stay distinct | A graph path is a declarative relation in an evidence-provenance DAG; actual work and transformation-flow claims stay with `A.15.1` and `E.18`. |
| Detail versus affordability | A path needs enough nodes, edges, windows, and constraints to replay reliance, but not every neighboring pattern boundary repeated in prose. |
| Typed downstream use versus one citation | The downstream citation may be one `PathId`, while verification, validation, lineage, assurance, status, causal-use, and source-currentness relations remain typed. |
| Bridge visibility versus reuse convenience | Cross-context or cross-plane reuse needs explicit bridge/currentness refs; label equality is not enough. |
| Refresh locality versus stale evidence | Path-level addresses let one changed source, bridge, edition, or policy reopen only the affected evidence-provenance paths. |

### G.6:4 - Solution

Create a citable `EvidenceGraph` and `PathCitationRecord` set when a local evidence-use statement is too small for the reliance being claimed. Keep the graph declarative and typed: nodes and edges carry provenance relations; `PathId` and `PathSliceId` cite graph paths; a provenance ledger records replayable path entries.

#### G.6:4.1 - Boundary to Neighboring Patterns

`G.6` is a path-addressing pattern over evidence provenance. It consumes or cites the following values without redefining them:

| Current value or relation | Governing pattern |
| --- | --- |
| compact episteme evidence-use or status-use relation | `A.2.4` |
| evidence carrier, source-currentness, evidence-producing work relation, evidence relation, and evidence-provenance addressing basics | `A.10` |
| assurance, trust, safety, compliance, readiness, or release-confidence claim | `B.3` |
| causal-use support basis, identification profile, causal-use verdict, or realizability profile | `C.28` |
| status family, status cell, status-use statement, or cross-context status mapping | `F.10` |
| bridge, congruence level, loss, or context-transfer relation | `F.9` |
| transformation-flow structure, gate crossing, or work occurrence used as evidence source | `E.18`, `A.21`, or `A.15.1` as applicable |
| publication, view, explanation, source-use, or specification-use relation | `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, or `E.10.D2` |

Do not add a local `EvidenceRole` value set. Source labels such as "proof role", "measurement role", "benchmark role", or "status role" are repair prompts. Recover the direct evidence-use, status-use, source-use, causal-use, assurance, work, or publication-use relation first.

#### G.6:4.2 - EvidenceGraph

An `EvidenceGraph` is a typed directed acyclic graph used for evidence-provenance citation. It is a graph because path identity, path slicing, and path-local refresh depend on graph structure. The graph is not a holarchy, not a transformation-flow structure, not a work plan, and not a method.

Minimal graph fields:

```text
EvidenceGraph:
  EvidenceGraphId:
  BoundedContext:
  ClaimFamilyOrUse:
  ReferencePlane:
  GraphNodeSet:
  GraphEdgeSet:
  TimePolicyOrWindow:
  SourceCurrentnessPolicy:
  BridgeOrTransferRefs:
  EditionOrPolicyRefs:
  GraphPathAddressingRule:
```

Minimal node kinds:

| Node kind | Value governed by | Use in G.6 |
| --- | --- | --- |
| `EvidenceUseRelationNode` | `A.2.4` or `A.10` | Names one episteme, carrier, source, proof, observation, or record being used as evidence for a claim or use. |
| `EvidenceCarrierNode` | `A.10` | References the concrete carrier or carrier class when material recoverability matters. |
| `SourcePublicationNode` | `E.17` and `A.10` | References a publication, source record, view, explanation, standard, model card, data card, or generated source relation. |
| `EvidenceProducingWorkNode` | `A.15.1` and `A.10` | References work occurrences, measurements, checks, tests, runs, audits, or observations that produced evidence. |
| `MethodDescriptionNode` | `A.3.2` and `A.10` | References the method description or formal substrate used to produce or interpret evidence. |
| `ExternalProducerRoleAssignmentNode` | `A.2.1` and `A.10` | References the work-facing role assignment of the producer, verifier, lab, issuer, or source-maintenance actor when externality decides the evidence relation. |
| `StatusUseRelationNode` | `A.2.4` and `F.10` | References a status-use statement when the path relies on validity, currentness, approval-looking status, or requirement status. |
| `CausalUseReferenceNode` | `C.28` | References causal-use support basis, identification, realizability, or verdict when the path is used for causal claims. |

Minimal edge kinds:

| Edge kind | Meaning |
| --- | --- |
| `verifiedBy` | Formal or proof-like evidence relation. |
| `validatedBy` | Empirical, observational, experimental, or run-time evidence relation. |
| `producedByWork` | Evidence was produced by a named work occurrence, measurement, check, run, or audit. |
| `usesMethodDescription` | Evidence production or interpretation used a named method description, formal substrate, or model description. |
| `derivedFrom` | One evidence node or source record is derived from another through a declared transformation, extraction, copy, representation shift, summary, or publication-use relation. |
| `happenedBefore` | A temporal ordering relation needed for the evidence claim. |
| `citesSource` | The path depends on a source publication, source record, status source, or source-currentness relation. |
| `crossesViaBridge` | The path crosses bounded context, reference plane, edition, or other bridge-relevant boundary through an explicit bridge or loss relation. |
| `hasStatusUse` | The path depends on a status-use statement rather than a display label. |
| `hasCausalUseRef` | The path depends on causal-use content governed by `C.28`. |

Extra graph annotations may exist for diagrams or tools, but conformance depends only on typed nodes, typed edges, path addresses, windows, constraints, and governing-pattern refs.

#### G.6:4.3 - PathId and PathSliceId

A `PathId` is a stable identifier for one claim-local graph path inside an `EvidenceGraph`. A `PathSliceId` is a stable identifier for the same path under a declared slice: time window, reference plane, bounded context, edition, bridge, policy, or selected evidence subset.

Here `path` means a path in the evidence-provenance graph. It is not an imperative route, work sequence, workflow, or transformation-flow path.

Use this compact record:

```text
PathCitationRecord:
  ClaimOrUseRef:
  EvidenceGraphRef:
  PathId:
  PathSliceId:
  BoundedContext:
  ReferencePlane:
  EvidenceUseRefs:
  PathNodeRefs:
  PathEdgeRefs:
  TimeWindowOrFreshnessPolicy:
  SourceCurrentnessRefs:
  BridgeOrLossRefs:
  EditionOrPolicyRefs:
  DownstreamCitationUse:
  NotCarried:
  ReopenTrigger:
```

`NotCarried` names the stronger claim not carried by this graph path: approval, permission, gate passage, release, performed work, assurance, causal identification, status assertion, compliance, benchmark superiority, or truth outside the declared claim and scope.

#### G.6:4.4 - Provenance Ledger

A `ProvenanceLedger` is a citable record over `PathCitationRecord` entries. It is not a work-progress log, review-comment log, or process-status log.

Minimal fields:

```text
ProvenanceLedger:
  LedgerId:
  EvidenceGraphRef:
  PathCitationRecords:
  SourceOrderPolicy:
  CurrentnessPolicy:
  PrivacyOrDisclosureBoundary:
  RefreshScopeRule:
```

Use a provenance ledger when several downstream records need the same path family: selector records, benchmark harnesses, assurance cases, release packages, maturity transitions, refresh records, or safety reviews. Do not create a ledger merely because one local evidence-use statement is easy to write in prose.

#### G.6:4.5 - Refresh and Source Return

Reopen the smallest affected path when one of these changes:

* evidence carrier identity, integrity, access, or hash;
* source publication, source order, supersession, or currentness window;
* work occurrence, measurement run, method description, proof check, or observation record;
* bridge, congruence level, loss statement, reference plane, or bounded context;
* causal-use profile, status-use statement, assurance-use requirement, or gate relation consumed downstream;
* edition, policy, threshold, verifier rule, relying-party context, or minimum disclosure boundary.

The reopen result is local to `PathId`, `PathSliceId`, or the smallest graph subpath that carries the changed relation. It does not rewrite the whole project and does not certify a new downstream decision by itself.

#### G.6:4.6 - Declarative Representation Discipline

`EvidenceGraph`, `PathId`, and `PathSliceId` are declarative representation values. They tell a reader what provenance relation is being cited. They do not tell a worker what to do next.

When a source phrase says "evidence path", "provenance route", "audit trail", "lineage flow", "data pipeline", or "workflow", recover the kind before copying the word:

| Source phrase is about | Governed by |
| --- | --- |
| graph path from claim to evidence and source refs | `G.6` and `A.10` |
| actual work that produced evidence | `A.15.1` |
| method or procedure for producing evidence | `A.3.1` and `A.3.2` |
| transformation-flow structure or graph | `E.18` and `E.18.2` |
| publication view, source form, explanation, or exported report | `E.17`, `E.17.0`, `E.17.2`, or `E.17.EFP` |
| assurance, gate, release, or permission use | `B.3`, `A.21`, or the direct governing boundary pattern |

#### G.6:4.7 - Extension Wiring Without Core Drift

Method-family, benchmark, selector, parity, or telemetry patterns may add required pins to a `PathCitationRecord`. They do not add new core node kinds unless the governing pattern explicitly changes G.6.

Examples:

* `G.5` may cite a `PathId` for selector explainability or admissibility.
* `G.9` may cite a `PathSliceId` for benchmark parity or replication lineage.
* `G.11` may consume reopen triggers and affected path slices for refresh.
* A causal-use pattern may add `C.28` refs to a path, but the causal-use relation remains governed by `C.28`.
* An assurance pattern may consume a path, but the assurance tuple remains governed by `B.3`.

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Brake Envelope Claim

A braking-system claim says the vehicle stops within a declared distance under declared conditions. `A.10` identifies telemetry files, calibration certificates, test runs, and external lab work. `G.6` mints a `PathId` that cites the graph path from the claim to proof checks, instrumented tests, calibration records, work occurrences, and time windows. `NotCarried` names stronger downstream uses; `B.3` and gate patterns govern assurance and release uses.

#### G.6:5.2 - Benchmark Parity Claim

A model-family report says a method reaches parity on a benchmark. `G.6` cites the path through dataset version, evaluation protocol, result record, source publication, method description, and replication work. If the dataset edition, metric policy, or source-currentness relation changes, the affected `PathSliceId` reopens without rerunning unrelated evidence-provenance paths.

#### G.6:5.3 - Dashboard Status Cue

A dashboard cell shows `Ready`. `F.10` governs status-family mapping and status-use. `A.10` governs the evidence relation to the governing register or source. `G.6` is used only when a downstream release package, selector, assurance record, or audit needs a stable evidence-provenance path from the visible cue to source, status-use relation, query time, window, issuer, and currentness policy.

#### G.6:5.4 - Causal Policy Result

A policy report says an intervention caused improvement. `C.28` governs causal-use support basis, identification, and realizability. `A.10` records evidence relation. `G.6` only gives a citable evidence-provenance path from the policy claim to the causal-use refs, data sources, assumptions, work occurrences, time window, and bridge refs needed for later audit.

### G.6:6 - Bias-Annotation

Biases guarded here:

| Bias | Guard |
| --- | --- |
| Role ontology drift | No `U.EvidenceRole`; evidence/status/source use is relation-slot work. |
| Semio-bias | The path addresses evidence provenance for a claim; publication faces and displays are only source nodes or cues unless direct patterns admit stronger use. |
| Imperative metaphor drift | `PathId` cites declared provenance graph structure; actual work and transformation-flow claims are governed by `A.15.1` and `E.18`. |
| Ledger process drift | Provenance ledger is content evidence, not work-progress state. |
| Proxy-for-value substitution | Badges, dashboards, scores, confidence phrases, and provenance labels do not become assurance, release, or truth. |
| Fanout by repetition | Neighbor boundaries are named once in the path record and direct-pattern table, not repeated as boilerplate in every example. |

### G.6:7 - Conformance Checklist

| ID | Check | Repair if missing |
| --- | --- | --- |
| `CC-G6-01` Primary EoC | Is the current evidence-provenance concern an `EvidenceGraph`, `PathId`, `PathSliceId`, or provenance ledger entry, with any role, work, or assurance claim kept under its own governing pattern? | Return to `A.2.4`, `A.10`, `B.3`, `C.28`, `F.10`, `A.15.1`, or `E.17` as appropriate. |
| `CC-G6-02` Graph path identity | Does each `PathId` resolve to a graph path in a named `EvidenceGraph`? | Mint or repair `EvidenceGraphRef`, node refs, edge refs, and path addressing rule. |
| `CC-G6-03` Node typing | Are node kinds explicit and governed by neighboring patterns? | Replace role-shaped or label-shaped nodes with evidence-use, status-use, source, work, method-description, carrier, or causal-use refs. |
| `CC-G6-04` Edge typing | Are provenance edges typed and minimal? | Replace narrative "because" text with verified, validated, produced-by-work, uses-method-description, source, bridge, time, status, or causal-use edges. |
| `CC-G6-05` Context and time | Are bounded context, reference plane, time window, freshness, currentness, edition, or policy refs stated when they decide use? | Add the missing refs or lower the path to source-finding or local evidence orientation. |
| `CC-G6-06` Bridge visibility | Are cross-context, cross-plane, cross-edition, or source-order crossings explicit? | Add bridge, loss, currentness, or source-order refs; otherwise block downstream reuse. |
| `CC-G6-07` Not carried | Does the path say what stronger downstream use it does not carry? | Add `NotCarried` for the stronger use and cite the governing pattern. |
| `CC-G6-08` Downstream use | Is the downstream citation use named? | Name selector, assurance, benchmark, release, maturity, refresh, audit, or local claim use, or stay in `A.10`. |
| `CC-G6-09` Refresh locality | Does a changed source, bridge, policy, edition, status, causal-use, or time relation reopen the smallest path slice? | Add `PathSliceId` and reopen trigger; avoid broad rerun language. |
| `CC-G6-10` No process leakage | Is the provenance ledger free of work-progress notes, review comments, release proof, or quality proof? | Move process evidence to the current process carrier; keep G.6 to evidence-provenance facts. |

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Narrative-only provenance | The reader cannot replay which evidence carried the claim. | Write `PathCitationRecord` with nodes, edges, windows, and `NotCarried`. |
| Evidence role node | Recreates old `U.EvidenceRole` ontology. | Use evidence-use relation nodes and work-facing role assignment refs only when producer externality matters. |
| Workflow overread | Treats declarative graph structure as work instruction. | `PathId` cites declared provenance graph structure; if actual work is current, use `A.15.1`; if transformation-flow structure is current, use `E.18`. |
| Dashboard-to-decision shortcut | A visible cell is treated as a downstream decision basis by itself. | Use `F.10` for status-use, `A.10` for source evidence, and the direct governing pattern for the stronger downstream use. |
| Provenance means truth | Origin, history, or attestation is treated as truth, safety, or adequacy. | Keep provenance as evidence for a named claim and use; apply direct patterns for truth-claim adequacy or assurance. |
| Global refresh | One source change triggers an undifferentiated rewrite of every record. | Reopen only affected `PathId`, `PathSliceId`, or graph subpath. |

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition, and time changes reopen the smallest path slice;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their governing patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

### G.6:10 - Rationale

`A.10` already gives the evidence-provenance graph relation for claims. `G.6` adds the Part-G need that local A.10 records do not fully satisfy: stable citation and path-local refresh for selectors, benchmarks, maturity transitions, assurance records, and release packages.

The pattern uses a graph mathematical lens because the useful mathematical object is a path through typed nodes and edges. It does not use graph language to claim that work "flows" through the path. When actual transformation structure matters, `E.18` governs it. When actual work matters, `A.15.1` governs it.

The pattern uses ledger language only for a provenance record. It does not invite process logs into pattern prose.

### G.6:11 - SoTA-Echoing

| Source family | G.6 adoption | Practitioner implication |
| --- | --- | --- |
| Verifiable-credential, content-provenance, and supply-chain attestation practice | Keep subject, issuer or producer, verifier or relying context, proof or signature check, status/currentness relation, policy, time, and input evidence or attestation refs separate. A summary attestation may be useful only when the underlying path or input attestations remain recoverable. | A provenance credential, content credential, or verification summary can feed a `PathId`; stronger downstream uses still need their governing patterns. |
| Current provenance, attestation, credential, and content-authenticity practice | Separate subject, issuer or producer, proof check, status check, time window, verifier or relying context, and source-currentness relation. | A provenance mark or credential view may evidence bounded origin or status; stronger downstream uses are not created by display. |
| Reproducible research, data lineage, model-card, datasheet, and benchmark governance practice | Keep dataset, metric, method description, evaluation condition, version, limitation, and run evidence addressable. | A benchmark or model report can be replayed and refreshed by path slice instead of becoming a frozen story. |
| Assurance-case and safety-case practice | Keep evidence-provenance paths citable by assurance claims without letting evidence presence equal assurance. | `B.3` can consume a `PathId`, but still needs its own assurance tuple, limitations, decay, and reopen relation. |
| Temporal and source-currentness practice | Treat windows, expiry, supersession, and source-order changes as path-local reopen events. | Stale or contested evidence lowers or reopens the path; it does not silently continue to carry reliance. |
| Declarative graph and provenance-graph practice | Use graph paths for addressability and replay, while keeping work execution and transformation-flow structures separate. | A path can be checked without telling a worker to follow it as a route. |

Refresh the source use behind this pattern when current provenance, credential, attestation, benchmark, lineage, assurance-case, or source-currentness practice changes the separation between provenance presence, evidence use, assurance, status use, and role assignment.

### G.6:12 - Relations

* **Builds on:** `A.10` for evidence-provenance graph relation, evidence relation, and source-currentness basics; `A.2.4` for compact evidence-use and status-use relation slots; `A.6.5` and `A.6.RSIR` for relation-slot discipline; `C.2.1` for episteme slot relation; `E.24` for ontic and slot-relation concept discipline.
* **Coordinates with:** `B.3` for assurance; `C.28` for causal-use evidence content; `F.10` for status-family mapping; `F.9` for bridge and loss; `E.17`, `E.17.0`, `E.17.2`, `E.17.EFP`, and `E.10.D2` for publication, view, explanation, and specification-use; `A.15.1` for work occurrences; `E.18` and `E.18.2` for transformation-flow structures and their mathematical descriptions; `A.21` for gate decisions when those are the downstream use.
* **Used by:** selector, benchmark, parity, refresh, assurance, maturity, and release patterns that need stable evidence-provenance path citation, including `G.5`, `G.9`, and `G.11`.
* **Does not govern:** stronger downstream uses named in `NotCarried`, work occurrence, source publication identity, or transformation-flow structure; those remain with their direct governing patterns.

### G.6:End

