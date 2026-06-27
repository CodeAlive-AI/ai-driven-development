## C.2.P.DR - Declarative Representation Precision Restoration

> **Type:** C.2.P precision-restoration child pattern for declarative-representation overread
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.2.P.DR:0 - Use this when

Use this pattern when a declarative representation is about to guide action, reliance, gate, release, evidence, method, mechanism, work, or pattern-application claims by its shape alone.

**First useful move.** Fill one compact `DeclarativeRepresentationRepair` note: encountered representation; representation kind; represented EntityOfConcern or claim; current source or publication relation; tempting imperative overread; recovered governing pattern; retained use; blocked overread; and stop or reopen condition.

**Quick example.** A heat-flow graph in a reactor-cooling review can show preserved and lost flow relations. It does not authorize a valve change by graph shape. The repair keeps the graph path as graph structure, returns release or gate reliance to the gate, source, and evidence patterns, and blocks the hidden work-permission claim.

Use this pattern especially when:

- a graph path, `PathSlice`, flow valuation, transformation-flow structure line, or graph expression over such a structure is overread as a prescribed work route or workflow;
- an `A.10` evidence path is overread as approval, permission, release, gate passage, or assurance;
- a query, access path, query plan, table, dashboard, schema, checklist predicate, or API description is overread as method, work plan, performed work, gate, permission, or proof;
- a publication face, source-chain relation, carrier file path, mathematical representation, method-description representation, or FPF pattern relation is overread as call, dispatch, invocation, send, receive, route, or pattern application;
- method-like wording hides whether the current claim concerns `U.Method`, `U.MethodDescription`, formal substrate, mathematical-lens use, `U.Mechanism`, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, or quote-only source wording.

**What goes wrong if missed.** The representation appears to do work it cannot do. A path "routes" a decision, a query "calls" a pattern, a dashboard "authorizes" release, a checklist predicate "runs" a process, an evidence path "permits" action, or a program-looking text becomes "the method" without recovering method semantics, method description, formal substrate, mechanism, work plan, work, evidence, or source-use relation.

**What this buys.** The working reader keeps the representation useful without making it magical. Graph paths remain graph paths, evidence paths remain evidence paths or provenance paths, queries remain representations, pattern relations remain declarative relations, and method-like wording is assigned to the current ontic slot, relation position, use relation, claim kind, or governing pattern named by value before it guides work, evidence, gate, release, assurance, or method claims.

**Not this pattern when.**

- If the graph path, `PathSlice`, or flow valuation is already current as graph structure, use `E.18` directly.
- If the evidence relation or provenance relation for a claim is already current, use `A.10` directly.
- If the publication face or source-use relation is already current, use `E.17`, `E.17.EFP`, `C.2.P`, or the direct publication pattern.
- If the current claim concerns a semantic way of doing, use `A.3.1`; if it concerns the description of that way, use `A.3.2`.
- If the current claim concerns operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment, use `A.6.1` or `E.20`.
- If the current claim concerns planned work or dated work, use `A.15.2` or `A.15.1`.
- If the word is only quoted source wording or ordinary navigation prose with no FPF-governed claim, keep it quote-only or ordinary.

### C.2.P.DR:1 - Problem frame

FPF uses many declarative representations: graphs, paths, characteristic spaces, predicates, tables, dashboards, publication faces, evidence paths, formal substrates, method descriptions, source-chain relations, and pattern relations. They are valuable because they expose structure without requiring the reader to imagine an action sequence.

The recurring failure is a category shift. Because some representations look like paths, pipelines, calls, dispatches, states, gates, or control programs, the prose starts granting them operational effects. A representation then seems to authorize work, pass a gate, enact a method, prove a result, release a system, or select a pattern by its shape alone.

This pattern repairs that shift. It does not build a general theory of representation. It only restores the FPF kind and governing pattern for declarative representations that are overread as imperative or operational claims.

### C.2.P.DR:2 - Problem

Without this repair:

1. **Graph path becomes work route.** A path or path slice in `E.18` is treated as an ordered work narrative, even when no work occurrence, work plan, or method description is current.
2. **Evidence path becomes permission.** An evidence relation or provenance relation is treated as approval, gate passage, release, safety, or authority rather than as evidence for a named claim or effect.
3. **Query becomes method.** A query, access path, query plan, or dashboard is treated as the semantic way of doing, rather than as a representation, method description, evidence relation, source relation, or ordinary source wording.
4. **Pattern relation overread as dispatch.** Pattern application prose starts saying that one pattern exits to, routes to, calls, invokes, receives, owns, or dispatches another, hiding declarative pattern relations and direct governing-pattern selection.
5. **Programming-paradigm label becomes ontology.** Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, or workflow wording is treated as the FPF kind rather than as one representation style or source label.
6. **Mechanism, method, and work collapse.** A method-like expression is repaired to `method` or `mechanism` by vocabulary rather than by the current claim: way of doing, description, formal substrate, law-governed mechanism, plan, occurrence, evidence, or quote-only wording.

### C.2.P.DR:3 - Forces

| Force | Tension |
| --- | --- |
| Representation usefulness and action overread | Graphs, queries, predicates, and dashboards are useful precisely because they expose structure; their shape does not supply hidden work, permission, or release. |
| Legitimate path words and metaphor repair | `A.10 evidence path`, `E.18` graph path, and carrier file paths may be legitimate; `path` becomes a defect only when it carries a stronger action or authority claim by metaphor. |
| Method generality and slot discipline | Algorithms, programs, solver models, proofs, SOPs, and process models can all be useful, but the current ontic slot, relation position, use relation, or claim kind is recovered before `method`, `method description`, `mechanism`, or `work` is selected. |
| Declarative and imperative labels are too crude | Current programming and process practice includes effects, handlers, constraint models, object-centric events, e-graphs, and process theories; the repair recovers FPF kind, current ontic slot, relation position, use relation, or claim kind rather than choosing one programming-paradigm slogan. |
| Direct governing pattern and local repair | When `E.18`, `A.10`, `A.3.1`, `A.3.2`, `A.6.1`, `A.15.2`, `A.15.1`, `E.17`, or another pattern already governs the current claim, this pattern names only the overread and leaves the next claim to that pattern rather than duplicating it. |

### C.2.P.DR:4 - Solution

Repair declarative-representation overread by recovering representation use, then naming the direct governing pattern for the current claim.

The repair order is:

1. **Name the encountered representation.** Quote or identify the graph, path, query, predicate, dashboard, table, publication face, evidence path, source-chain relation, carrier path, mathematical representation, method-description representation, or pattern relation.
2. **Name the representation kind.** State whether it is graph structure, flow valuation, evidence relation, provenance relation, state predicate, query, table, publication face, formal substrate, method description, source relation, carrier syntax, or another representation kind named by value.
3. **Name the represented EntityOfConcern or claim.** State what the representation is about: claim, effect, method, work occurrence, work plan, graph object, state, EntityOfConcern, publication, evidence relation, gate, source relation, or pattern relation.
4. **Recover source or publication relation when current.** If the representation is a face, source chain, generated explanation, copied text, dashboard, file path, or publication unit, use the publication pattern or source-use pattern governing that relation.
5. **Name the tempting imperative overread.** Say what the representation is being asked to do by resemblance: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work.
6. **Select the governing pattern.** Use the direct pattern when the kind is already recovered; otherwise use this pattern only long enough to recover the representation use and blocked overread.
7. **State retained use.** Keep the weaker useful use: graph structure, evidence relation, source-finding, state predicate, publication face, method-description representation, formal-substrate input, method slot candidate, or pattern relation.
8. **State blocked overread.** Block only the stronger claim that is not recoverable.
9. **Stop or reopen.** Stop when the governing pattern can carry the next claim. Before stopping, ask what claim, evidence relation, gate relation, safety relation, method relation, work relation, or source relation would become less reviewable if the visible representation were accepted as the stronger claim. Reopen if a later source changes representation kind, represented EntityOfConcern, source currentness, governing pattern, or the intended use.

#### C.2.P.DR:4.1 - DeclarativeRepresentationRepair note

Use this compact note when the wording has FPF-governed use:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation:
  RepresentationKind:
  RepresentedEntityOfConcernOrClaim:
  SourceOrPublicationRelation:
  TemptingImperativeOverread:
  RecoveredGoverningPattern:
  RetainedUse:
  BlockedOverread:
  StopOrReopenCondition:
```

The note records the local repair long enough to make the next governing pattern selectable. If the direct governing pattern already supplies a better record, use that record and keep only the repaired wording, retained use, blocked overread, and stop or reopen condition here.

#### C.2.P.DR:4.2 - Direct governing-pattern selection

| If recovery shows... | Use this governing pattern | Keep this boundary |
| --- | --- | --- |
| graph object, graph path, `PathSlice`, crossing, flow valuation, transformation-flow structure relation, or graph expression over that structure | `E.18`, `E.18.2`, or `E.18.1` when P2W carry-through is current | Graph structure or path structure is not work route, method narrative, evidence result, or pattern dispatch by layout. |
| evidence relation or provenance relation for a claim, effect, or reliance use | `A.10` | Evidence path is not approval, permission, gate passage, release, safety, work occurrence, or assurance by itself. |
| state, status value, readiness, validity, or predicate-like value whose bearer and value frame is hidden | `A.19.SPR` or the direct status-value or state-value pattern | A predicate or state-like value is not a workflow, gate, or proof unless the governing pattern says so. |
| publication face, source expression, generated explanation, dashboard face, publication unit, or source-chain relation | `E.17`, `E.17.EFP`, `C.2.P`, `A.15.4`, or source-use pattern named by value | Publication and source visibility do not create work, evidence, authority, release, or gate passage. |
| mathematical representation, formal object, formal substrate, invariant, or mathematical-lens output | `A.6.0`, `C.29`, or direct mathematical pattern | Mathematical representation is not method, mechanism, proof of project result, or work execution until that claim is separately recovered. |
| context-local semantic way of doing | `A.3.1 U.Method` | A method claim is not closed by code, diagram, proof script, plan, run, or mechanism declaration; use `E.10.ARCH:3.1` only to recover the project concern and then recover each linked typed value under its own governing pattern. |
| episteme describing a method: code, SOP, proof script, solver model, process model, protocol, recipe, or diagram | `A.3.2 U.MethodDescription` | Description is not the method itself and not dated work. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment | `A.6.1` and `E.20` | Mechanism meaning is not selected by saying "algorithm" or "method"; it needs mechanism fields. |
| planned work, intended window, role requirements, resource budget, or acceptance criterion | `A.15.2 U.WorkPlan` | Plan is not method, method description, evidence, gate passage, or performed work. |
| dated work occurrence, run trace, concrete parameter binding, result, resource use, or performed-work record | `A.15.1 U.Work` | Work occurrence is not a diagram, plan, method description, source cue, or evidence path by appearance. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications, not exits, receivers, routes, calls, owners, homes, or dispatches. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`path` is not banned.

`A.10 evidence path for <claim, effect, or use>` is legitimate when the evidence relation or provenance relation for the named claim, effect, or reliance use is current. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation, source-use function, or use relation is current.

The defect is not the word. The defect is hidden ontology: the sentence treats a representation as if something literally ran, flowed, executed, authorized, released, proved, selected, or prescribed action without the governing kind named by value.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, and work-slot settlement

Do not repair `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, or `control strategy` by choosing one fashionable replacement.

Recover the current ontic slot, relation position, use relation, or claim kind:

| Current claim | Governing pattern |
| --- | --- |
| context-local semantic way of doing, transformation kind, or enactment kind | `A.3.1 U.Method` |
| episteme describing that way | `A.3.2 U.MethodDescription` |
| formal substrate, signature, postulates, laws, or mathematical declaration | `A.6.0`; use `C.29` when mathematical-lens use is current |
| operation algebra, admissibility predicates, transport, audit, realization, or mechanism-governing-definition assignment | `A.6.1` and `E.20` |
| planned work | `A.15.2 U.WorkPlan` |
| dated performed work | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim | `A.10` |
| wording quoted from source with no FPF-governed use | quote-only source wording |

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal assignments, use `E.10.ARCH:3.1` to recover the project concern and the current relation position. For this host, recover only the representation overread and the direct governing pattern for the current claim; linked typed values remain under their own governing patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, Declare-style, SQL-like, e-graph, hypergraph, or process-mining wording is a cue to recover representation kind and FPF slot. It is not a decision procedure by itself.

Current practice makes the old contrast between imperative and declarative labels too weak as a final ontology:

- constructor and process-theory lines keep computation, information, dynamics, and procedure close to possible or impossible transformations and compositional realization;
- scoped effects and handlers separate operation syntax, semantic handling, scopes, resources, equations, type information, and effect information;
- Declare-style process models and object-centric event logs distinguish constraints, events, objects, relations, ingestion, transformation, storage, and analysis;
- e-graph and monoidal-rewriting work shows that computation or process representation may be equivalence or composition structure rather than instruction order.

Use those lines as guardrails: recover the FPF kind and slot instead of replacing one programming-paradigm label with another.

### C.2.P.DR:5 - Worked slices

#### C.2.P.DR:5.1 - Graph path in a transformation-flow structure

Wording: "The P2W path routes the team from principle to work."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: P2W path or path slice in a selected TransformationFlowStructure
  RepresentationKind: graph path or PathSlice candidate under E.18 and E.18.1
  RepresentedEntityOfConcernOrClaim: carry-through relation from accepted problem-side material to next FPF kind named by value
  SourceOrPublicationRelation: current graph or pattern publication when relevant
  TemptingImperativeOverread: ordered work route for the team
  RecoveredGoverningPattern: E.18.1, with A.15.2 or A.15.1 only if planned or dated work is current
  RetainedUse: graph representation or path representation and carry-through record
  BlockedOverread: no work route or prescribed workflow by path shape alone
  StopOrReopenCondition: reopen when path, source currentness, graph edition, or intended work relation changes
```

#### C.2.P.DR:5.2 - Evidence path near release

Wording: "The evidence path authorizes release."

Repair: `A.10` can state an evidence path for the claim or effect. Release, permission, or gate passage requires the authority, gate, or release pattern that governs that claim. This pattern is used only if `path` wording itself is causing the representation to be overread as a permission route.

#### C.2.P.DR:5.3 - Query plan and access path

Wording: "The query plan calls the production work sequence."

Repair: recover whether the query plan is an optimizer representation, method description, formal substrate, source cue, evidence relation, work plan, or actual work trace. If it only represents query evaluation choices, do not treat it as `U.WorkPlan` or `U.Work`. If the current claim concerns method semantics, use `A.3.1`; if it concerns a method description, use `A.3.2`; if it concerns a performed query run, use `A.15.1` and the evidence pattern or source-use pattern.

#### C.2.P.DR:5.4 - Dashboard predicate

Wording: "The dashboard green path lets the release move."

Repair: recover dashboard face, source relation, status or state bearer, value frame, source currentness, and gate or release claim. The dashboard may be a publication face and source cue; it is not release permission unless the gate or authority pattern consumes the source and states that effect.

#### C.2.P.DR:5.5 - Pattern relation

Wording: "This pattern exits to A.10."

Repair: if the current relation is "use `A.10` when an evidence relation or provenance relation is current", write that declarative boundary. Do not use exit, receiver, route, owner, home, dispatch, or call language unless the pattern is actually about an action occurrence, work plan, control mechanism, or communication relation that has those semantics.

#### C.2.P.DR:5.6 - Solver algorithm

Wording: "The solver algorithm is the mechanism."

Repair: recover the current ontic slot, relation position, use relation, or claim kind. The solver configuration may be `U.MethodDescription`; the accepted semantic way of solving may be `U.Method`; the MILP formulation may expose formal substrate and mathematical-lens use; a reusable operation algebra with laws and admissibility predicates may be `U.Mechanism`; a solver run may be `U.Work`; a run result may be evidence for another claim. Select `A.6.1` and `E.20` only when mechanism fields are present in the current claim.

#### C.2.P.DR:5.7 - Reactor-cooling flow graph

Wording: "The preserved heat-flow path authorizes the valve change."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: reactor-cooling heat-flow graph with one highlighted preserved path
  RepresentationKind: graph path or flow relation representation under E.18 and C.29 when mathematical-lens use is current
  RepresentedEntityOfConcernOrClaim: preserved heat-flow structure and boundary conditions for the cooling subsystem
  SourceOrPublicationRelation: current engineering review publication, source relation, or gate record when one is cited
  TemptingImperativeOverread: graph path authorizes physical valve-change work
  RecoveredGoverningPattern: E.18 and C.29 for graph and lens use; A.21, A.10, A.15.2, and A.15.1 only if gate, evidence, work plan, or dated work is current
  RetainedUse: graph structure for comparison, model review, and source-finding
  BlockedOverread: no release, gate passage, physical intervention, or work occurrence by highlighted path alone
  StopOrReopenCondition: reopen when gate decision, source currentness, measurement boundary, or work plan becomes current
```

#### C.2.P.DR:5.8 - CRISPR guide-selection table

Wording: "The guide-selection table approves the edit."

Repair:

```text
DeclarativeRepresentationRepair:
  EncounteredRepresentation: CRISPR guide-selection table with off-target scores and candidate ranking
  RepresentationKind: table representation, characteristic-space representation, or evidence-facing representation, depending on the claim being made
  RepresentedEntityOfConcernOrClaim: candidate guide comparison, off-target risk claim, or experimental-design option
  SourceOrPublicationRelation: lab notebook, protocol publication, source episteme, or review record when current
  TemptingImperativeOverread: ranked row approves biological intervention
  RecoveredGoverningPattern: C.16 or A.19 for characteristics when current; A.10 for evidence; A.15.2 for experimental work plan; A.21 or authority pattern only if approval or gate claim is current
  RetainedUse: source-finding, candidate comparison, and constraint review
  BlockedOverread: no edit approval, work occurrence, safety claim, or gate passage from table rank alone
  StopOrReopenCondition: reopen when protocol, gate decision, evidence path, role authorization, or dated lab work becomes current
```

### C.2.P.DR:6 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C2PDR-1` | A repair names the encountered representation and representation kind before changing wording. |
| `CC-C2PDR-2` | A repair names the represented EntityOfConcern or claim and any current source or publication relation. |
| `CC-C2PDR-3` | The tempting imperative overread is explicit: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work. |
| `CC-C2PDR-4` | The recovered governing pattern is named by value, or the case is demoted to quote-only, ordinary prose, reduced-use cue, blocked use, or incomplete rewrite. |
| `CC-C2PDR-5` | Legitimate `A.10 evidence path`, `E.18` graph path, `PathSlice`, carrier file path, URL, or mathematical path use is preserved when that kind is current. |
| `CC-C2PDR-6` | Method-like and algorithm-like wording recovers the current ontic slot, relation position, use relation, or claim kind before replacement: `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.10`, direct governing pattern, or quote-only source wording. |
| `CC-C2PDR-7` | An `E.10.ARCH:3.1` project-concern recovery may connect method, mechanism, formal-substrate, work values, evidence relations, source relations, gate relations, or result relations, but each connected value keeps its own governing pattern and typed claim. |
| `CC-C2PDR-8` | The repair leaves one retained use and one blocked overread; type-correct but inert wording is incomplete. |
| `CC-C2PDR-9` | The pattern does not become a general representation theory, API pattern, schema pattern, legal framework, workflow framework, or generic admissibility pattern. |
| `CC-C2PDR-10` | Direct governing patterns keep their invariants. This pattern only restores representation use and blocked overread before those patterns carry their own claims. |

### C.2.P.DR:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Path word deletion | Every `path` is replaced or avoided. | Preserve legitimate `A.10`, `E.18`, carrier, mathematical, URL, and quoted-source path uses; repair only hidden stronger claims. |
| Imperative metaphor as ontology | Representations "route", "call", "dispatch", "receive", "invoke", or "flow" by prose habit. | Recover representation kind and governing pattern, then write the relation declaratively. |
| Algorithm as method by default | Code, solver model, proof script, or workflow is called the method without slot recovery. | Use `A.3.1` only for semantic way of doing; use `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, or `A.10` when those claims are current. |
| Mechanism by prestige | `mechanism` is used because the word sounds more rigorous than method or algorithm. | Require operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment. |
| Dashboard as gate | Green status, dashboard tile, score, or status label becomes permission or release. | Recover source relation or publication relation, state-family value, evidence relation, and gate or release pattern when current. |
| Pattern dispatcher | Pattern relations are written as routes, exits, receivers, calls, owners, or homes. | Write declarative neighboring-pattern boundary or application relation; use `E.8` and `F.19` together when both publication-form and phrase-apparatus claims are live, or use the one governing pattern when only one claim is live. |
| Generic representation theory | The repair tries to classify every representation in FPF or becomes an API pattern, schema pattern, legal framework, workflow framework, or generic admissibility pattern. | Stop at the representation-use field set and use the direct governing pattern for the current claim. |

### C.2.P.DR:8 - Relations

- **Builds on:** `E.10`, `E.10.ARCH`, `C.2.P`, `A.7`, `E.17`, `E.8`, and `F.19`.
- **Coordinates with:** `E.18`, `E.18.1`, `A.10`, `A.19.SPR`, `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.15.4`, `A.20`, `A.21`, `B.3`, and direct publication, gate, authority, release, evidence, method, work, and assurance patterns when those claims are being made.
- **Specializes:** `C.2.P` for one recurring case: declarative representation and imperative-metaphor overread.
- **Used by:** `E.10.ARCH` applicability-row distribution and full-pattern text precision restoration when route, path, workflow, call, or dispatch wording hides representation use.

### C.2.P.DR:9 - Consequences

- FPF can keep useful graph, path, query, table, dashboard, publication, and pattern-relation vocabulary without banning ordinary words.
- The repair blocks hidden authority, release, gate, evidence, method, mechanism, work, and pattern-dispatch claims by requiring the governing pattern named by value.
- Method and mechanism claims become easier to compose because `E.10.ARCH:3.1` can link separately recovered typed values through relation-position discipline without treating slot-position labels as alternate ontology.
- The cost is a small recovery note when representation wording is actually carrying FPF-governed use. Ordinary navigation, source quotation, and already-governed graph or evidence paths do not need the note.

### C.2.P.DR:10 - SoTA-Echoing

This pattern uses external sources only for the representation-overread repair question. They do not replace FPF ontology, and older famous sources are lineage or contrast unless a current source below supplies the contemporary payload.

| Source or practice line | Source-use function or relation | What it changes here |
| --- | --- | --- |
| `E.10`, `E.10.ARCH`, and `C.2.P` | Current FPF precision-restoration architecture. | This pattern is a bounded child realization under `C.2.P`, not a new umbrella pattern. |
| `A.10` and `E.18` | Local FPF direct governing patterns for evidence paths, provenance paths, transformation-flow graph paths, and path slices. | Path wording is legitimate when those kinds are current; the defect is stronger overread. |
| `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, and `A.15.1` | Local FPF method-like and algorithm-like wording discipline. | The repair recovers current ontic slot, relation position, use relation, or claim kind before choosing method, method description, formal substrate, mechanism, work plan, or work occurrence. |
| Stefano Gogioso, Vincent Wang-Mascianica, Muhammad Hamza Waseem, Carlo Maria Scandolo, and Bob Coecke, "Constructor Theory as Process Theory", arXiv:2401.05364, EPTCS 397, 2023; David Deutsch and Chiara Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Current SoTA decision payload for transformation-theory and process-theory repair of computation, method, and dynamics wording. | Computation, information, dynamics, and procedure wording is interpreted through possible or impossible transformation and compositional-process claims when that claim is current, not through software notation or ordered instruction prose first. |
| Roger Bosman, Birthe van den Berg, Wenhao Tang, and Tom Schrijvers, "A Calculus for Scoped Effects & Handlers", Logical Methods in Computer Science 20(4), 2024, arXiv:2304.09697; Cristina Matache, Sam Lindley, Sean Moss, Sam Staton, Nicolas Wu, and Zhixuan Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Current SoTA decision payload for effectful computation and programming-model wording. | Operation syntax, semantic handling, scope, resources, equations, and effect information remain separable; pure-function slogans and imperative-declarative slogans are not enough. |
| Francesco Chiariello, Valeria Fionda, Antonio Ielo, and Francesco Ricca, "Direct Encoding of Declare Constraints in ASP", Theory and Practice of Logic Programming 25, 2025, arXiv:2412.10152; Alessandro Berti et al., "OCEL (Object-Centric Event Log) 2.0 Specification", arXiv:2403.01975; Lien Bosmans et al., "Dynamic and Scalable Data Preparation for Object-Centric Process Mining", arXiv:2410.00596. | Current SoTA decision payload for process-model, trace, workflow, and event-record wording. | Constraint, event, object, relation, data model, ingestion, transformation, storage, and analysis claims are recovered separately before a method, work plan, work occurrence, evidence, or gate claim is accepted. |
| Aleksei Tiurin, Chris Barrett, Dan R. Ghica, and Nick Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Current SoTA decision payload for graph, equivalence, and compositional-representation wording. | Graph, equality, equivalence, and rewrite representations do not become instruction order by layout; preserve representation kind and represented object before any method, work, or action claim is made. |
| Robert Kowalski 1979; E. F. Codd 1970; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Historical lineage or contrast only. | These sources explain why the overread is recognizable; they do not carry current SoTA weight for this pattern by age, fame, or popularity. |

### C.2.P.DR:End

