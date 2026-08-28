## C.2.P.DR - Declarative Representation Precision Restoration

> **Type:** C.2.P precision-restoration child pattern for declarative-representation overread
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.2.P.DR:0 - Use this when

Use this pattern when a declarative representation is about to guide action, reliance, gate, release, evidence, method, mechanism, work, or pattern-application claims by its shape alone.

**First useful move.** Fill one compact `DeclarativeRepresentationRepair` note: visible expression or artifact; exact current direct object or relation; exact representation or correspondence use, or `none`; current source or publication relation; tempting stronger action claim; recovered subject pattern; retained use; blocked stronger action claim; and stop or reopen condition.

**Quick example.** A heat-flow graph in a reactor-cooling review can show preserved and lost flow relations. It does not authorize a valve change by graph shape. The repair keeps the graph path as graph structure, returns release or gate reliance to the gate, source, and evidence patterns, and blocks the hidden work-permission claim.

Use this pattern especially when:

- a graph path, `PathSlice`, flow valuation, transformation-flow structure line, or graph expression over such a structure is overread as a prescribed work route or workflow;
- an `A.10` evidence path is overread as approval, permission, release, gate passage, or assurance;
- a query, access path, query plan, table, dashboard, schema, checklist predicate, or API description is overread as method, work plan, performed work, gate, permission, or proof;
- a publication face, source-chain relation, carrier file path, mathematical representation, method-description representation, or FPF pattern relation is overread as call, dispatch, invocation, send, receive, route, or pattern application;
- method-like wording hides whether the current claim concerns `U.Method`, `U.MethodDescription`, formal substrate, mathematical-lens use, `U.Mechanism`, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, or quote-only source wording.

**What goes wrong if missed.** The representation appears to do work it cannot do. A path "routes" a decision, a query "calls" a pattern, a dashboard "authorizes" release, a checklist predicate "runs" a process, an evidence path "permits" action, or a program-looking text becomes "the method" without recovering method semantics, method description, formal substrate, mechanism, work plan, work, evidence, or source-use relation.

**What this buys.** The working reader keeps a visible expression useful without making it magical or hiding its subject pattern. Graph paths and structures, evidence or provenance relations, queries and formal objects, publication faces, and pattern relations keep their own kinds. When a graph, file, tile, table, or face represents one of them, the exact representation or correspondence use is stated separately. For method-like wording, the reader identifies the direct object or relation, any represented object or claim, and the exact relation that gives the expression its current use before selecting method, method description, formal substrate, mechanism, plan, work, evidence, source, gate, or release guidance.

**Not this pattern when.**

- If the graph path, `PathSlice`, or flow valuation is already current as graph structure, use `E.18` directly.
- If the evidence relation or provenance relation for a claim is already current, use `A.10` directly.
- If the publication face or source-use relation is already current, use `E.17`, `E.17.EFP`, `C.2.P`, or the direct publication pattern.
- If the current claim concerns a semantic way of doing, use `A.3.1`; if it concerns the description of that way, use `A.3.2`.
- If the current claim concerns operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment, use `A.6.1` or `E.20`.
- If the current claim concerns planned work or dated work, use `A.15.2` or `A.15.1`.
- If the word is only quoted source wording or ordinary navigation prose with no FPF-governed claim, keep it quote-only or ordinary.

### C.2.P.DR:1 - Problem frame

FPF work meets many declarative-looking expressions and many direct objects or relations: graph and table artifacts; paths and selected structures; state predicates and values; dashboard and publication faces; evidence, provenance, source, and pattern relations; formal substrates; and method descriptions. Some visible expressions represent a separately governed object or claim; other named items are themselves the current direct object or relation. Their common declarative appearance does not make them peers in one kind.

The recurring failure is a category shift. Because some representations look like paths, pipelines, calls, dispatches, states, gates, or control programs, the prose starts granting them operational effects. A representation then seems to authorize work, pass a gate, enact a method, prove a result, release a system, or select a pattern by its shape alone.

This pattern repairs that shift. It does not build a general theory of representation. It only restores the exact FPF-governed object, relation, or claim and its subject pattern when declarative-looking wording is overread as imperative or operational.

### C.2.P.DR:2 - Problem

Without this repair:

1. **Graph path becomes work route.** A path or path slice in `E.18` is treated as an ordered work narrative, even when no work occurrence, work plan, or method description is current.
2. **Evidence path becomes permission.** An evidence relation or provenance relation is treated as approval, gate passage, release, safety, or authority rather than as evidence for a named claim or effect.
3. **Query becomes method.** A query, access path, query plan, or dashboard is treated as the semantic way of doing, rather than as a representation, method description, evidence relation, source relation, or ordinary source wording.
4. **Pattern relation overread as dispatch.** Pattern application prose starts saying that one pattern exits to, routes to, calls, invokes, receives, owns, or dispatches another, hiding declarative pattern relations and subject pattern selection.
5. **Programming-paradigm label becomes ontology.** Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, or workflow wording is treated as the FPF kind rather than as one representation style or source label.
6. **Mechanism, method, and work collapse.** A method-like expression is repaired to `method` or `mechanism` by vocabulary rather than by the current claim: way of doing, description, formal substrate, law-governed mechanism, plan, occurrence, evidence, or quote-only wording.

### C.2.P.DR:3 - Forces

| Force | Tension |
| --- | --- |
| Representation usefulness and action overread | Graphs, queries, predicates, and dashboards are useful precisely because they expose structure; their shape does not supply hidden work, permission, or release. |
| Legitimate path words and metaphor repair | `A.10 evidence path`, `E.18` graph path, and carrier file paths may be legitimate; `path` becomes a defect only when it carries a stronger action or authority claim by metaphor. |
| Method generality and subject discipline | Algorithms, programs, solver models, proofs, SOPs, and process models can all be useful, but first identify the direct object or relation, the current claim, and any exact representation use. Select `U.MethodDescription` only after the claim-bearing episteme passes the A.3.2 membership test; representation form alone selects nothing. |
| Declarative and imperative labels are too crude | Current programming and process practice includes effects, handlers, constraint models, object-centric events, e-graphs, and process theories; the repair names the direct object or relation, current claim, any representation use, and subject pattern rather than choosing one programming-paradigm slogan. |
| Subject pattern and local repair | When `E.18`, `A.10`, `A.3.1`, `A.3.2`, `A.6.1`, `A.15.2`, `A.15.1`, `E.17`, or another pattern already governs the current claim, this pattern names only the overread and leaves the next claim to that pattern rather than duplicating it. |

### C.2.P.DR:4 - Solution

Repair declarative-representation overread by separating the visible expression, the direct object or relation, and any representation use before naming the subject pattern for the current claim.

The repair order is:

1. **Name the visible expression or artifact.** Quote or identify the graph highlight, file, query text, predicate display, dashboard tile, table, publication face, path diagram, carrier path, mathematical expression, method-description expression, or pattern sentence that prompted the overread.
2. **Recover the exact current direct object or relation.** Name the graph structure, `PathSlice`, flow valuation, evidence or provenance relation, state predicate or value, query or formal object, publication face or occurrence, formal substrate, claim-bearing episteme, source relation, carrier-side object, pattern relation, or other direct outcome under its own governor. This is a list of alternative recovery outcomes, not representation kinds in one ontology.
3. **State the representation or correspondence use, or write `none`.** When the visible expression represents a separately identified object or claim, name the exact relation and target. When the direct object or relation itself is current and no separate representation claim is needed, write `none`; do not relabel the direct object as a representation kind.
4. **Recover source or publication relation when current.** If a face, source chain, generated explanation, copied text, dashboard, file path, or publication unit is current, use the publication pattern or source-use pattern governing that relation.
5. **Name the tempting stronger action claim.** Say what the visible expression is being asked to do by resemblance: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work.
6. **Select the subject pattern.** Use the direct pattern when the object or relation is already recovered; otherwise use this pattern only long enough to recover the direct outcome, any representation use, and the blocked stronger claim.
7. **State retained use.** Keep the weaker useful use: graph structure, evidence relation, source-finding, state predicate, publication face, exact representation use, formal-substrate input, candidate method reading, or pattern relation.
8. **State the blocked stronger action claim.** Block only the stronger claim that is not recoverable.
9. **Stop or reopen.** Stop when the subject pattern can carry the next claim. Before stopping, ask what claim, evidence relation, gate relation, safety relation, method relation, work relation, or source relation would become less reviewable if the visible expression were accepted as the stronger claim. Reopen if a later source changes the visible expression, direct object or relation, representation relation or target, source currentness, subject pattern, or intended use.

#### C.2.P.DR:4.1 - DeclarativeRepresentationRepair note

Use this compact note when the wording has FPF-governed use:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact:
  CurrentDirectObjectOrRelation:
  RepresentationOrCorrespondenceUse: <exact relation and represented target> | none
  SourceOrPublicationRelation:
  TemptingStrongerActionClaim:
  RecoveredGoverningPattern:
  RetainedUse:
  BlockedStrongerActionClaim:
  StopOrReopenCondition:
```

The note records the local repair long enough to make the next subject pattern selectable. If the subject pattern already supplies a better record, use that record and keep only the repaired wording, exact direct outcome, any representation use, retained use, blocked stronger claim, and stop or reopen condition here.

Use four plain questions before the claim-and-pattern table: What visible thing am I looking at? What direct object or relation is current? What, if anything, does it represent? What stronger action claim must remain blocked?

| Visible expression or artifact | Exact current direct object or relation | Representation or correspondence use | Stronger action claim blocked |
| --- | --- | --- | --- |
| highlighted graph path | exact E.18 graph path or `PathSlice`, with any flow valuation kept separate | the graphic rendering corresponds to that path when the relation is current; otherwise `none` when the `PathSlice` itself is under inspection | no prescribed route, valve work, or release by the highlight |
| dashboard tile | exact status or state value with its bearer and value frame, plus any current source or publication relation | the tile represents that value only through an exact current relation; otherwise `none` when the publication face itself is the direct object | no gate passage or release permission from green appearance |
| evidence-path expression | exact A.10 evidence or provenance relation for the named claim or effect | a diagram may represent that relation; otherwise `none` when the relation itself is current | no approval, permission, assurance, or release from path shape |
| solver file | exact publication form or carrier-side object, and whichever formal substrate, claim-bearing episteme, method, mechanism declaration, plan, run, or evidence relation is independently current | the solver expression corresponds to separately identified claims or a formal object when that relation is stated; otherwise `none` | no method, mechanism, performed work, result, or evidence by file form or executability |
| publication table | exact publication face or form and source relation, with table values or claims kept under their subject patterns | the table corresponds to a separately identified object or claim only when the exact relation is current; otherwise `none` | no evidence, approval, gate passage, or action authority from table layout |

#### C.2.P.DR:4.2 - Subject pattern selection

| If recovery shows... | Use this subject pattern | Keep this boundary |
| --- | --- | --- |
| graph object, graph path, `PathSlice`, crossing, flow valuation, transformation-flow structure relation, or graph expression over that structure | `E.18`, `E.18.2`, or `E.18.1` when P2W carry-through is current | Graph structure or path structure is not work route, method narrative, evidence result, or pattern dispatch by layout. |
| evidence relation or provenance relation for a claim, effect, or reliance use | `A.10` | Evidence path is not approval, permission, gate passage, release, safety, work occurrence, or assurance by itself. |
| state, status value, readiness, validity, or predicate-like value whose bearer and value frame is hidden | `A.19.SPR` or the direct status-value or state-value pattern | A predicate or state-like value is not a workflow, gate, or proof unless the subject pattern says so. |
| publication face, source expression, generated explanation, dashboard face, publication unit, or source-chain relation | `E.17`, `E.17.EFP`, `C.2.P`, `A.15.4`, or source-use pattern named by value | Publication and source visibility do not create work, evidence, authority, release, or gate passage. |
| mathematical representation, formal object, formal substrate, invariant, or mathematical-lens output | `A.6.0`, `C.29`, or direct mathematical pattern | Mathematical representation is not method, mechanism, proof of project result, or work execution until that claim is separately recovered. |
| context-local semantic way of doing | `A.3.1 U.Method` | A method claim is not closed by code, diagram, proof script, plan, run, or mechanism declaration; use `E.10.ARCH:3.1` only to recover the project concern and then recover each linked typed value under its own subject pattern. |
| already identified `U.Episteme` with one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive claim about that method as a way of doing | `A.3.2 U.MethodDescription` | Code, SOP, proof-script, solver-model, process-model, protocol, recipe, and diagram forms are clues only. A name, citation, approval, runnable form, or representation correspondence does not establish membership. |
| law-governed operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment | `A.6.1` and `E.20` | Mechanism meaning is not selected by saying "algorithm" or "method"; it needs mechanism fields. |
| planned work, intended window, resource budget, acceptance criterion, or source “role requirement” | `A.15.2 U.WorkPlan` for the plan. Resolve a “role requirement” separately to its exact local system-role kind, separate System-classification judgment, future assignment condition, capability, participant relation, or other direct condition; if unresolved, use `E.10.ROLE`. | A plan is not a Method, MethodDescription, evidence, gate passage, performed Work, or assignment occurrence. A required kind or condition does not create the future assignment. |
| exact dated Work occurrence | Recover every exact actual performer through A.13, then let `A.15.1 U.Work` independently identify the dated occurrence, enacted Method, time, and containing System. A representation claiming the exact Work keeps every actual performer named or recoverable. Add an A.2.1 assignment occurrence and F.6 relation only when the representation or receiving use expressly represents precise assignment-bound attribution; then it may omit only an unused assignment identifier after the underlying attribution is established. Missing or failed F.6 leaves the Work intact and blocks only that attribution. | The Work occurrence is not its trace, record, binding, resource use, result, diagram, plan, MethodDescription, source cue, or evidence path. |
| run trace or performed-work record | `C.2.1` for the exact trace or record episteme, plus its direct description, publication, source-use, or evidence-use pattern only when that claim is current | The episteme may designate exact `W`, `RA`, holder `S`, and `performedUnderAssignment(W, RA)` when it makes that attribution; it neither is the Work occurrence nor makes the relation obtain. |
| concrete parameter or participant binding | the exact direct subject-relation pattern, or `A.6.1` for one independently identified operation application and its actual argument or result binding | A declaration, call position, trace field, or type-compatible token establishes no actual binding. |
| performed resource use | the exact direct resource-use relation involving the already identified Work occurrence; use `B.1.6` only when aggregation is current | Resource use is a separately obtaining relation, not a Work field, record field, or result. |
| result or output | identify the exact result entity or episteme first; use `A.15.PROD` when production, entity inception, or production completion is current, and `A.6.RCD` only when the needed direct result relation has no current governor | A binding, record field, Work occurrence, or nearby output label does not identify the result or establish production. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications, not exits, receivers, routes, calls, owners, homes, or dispatches. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`path` is not banned.

`A.10 evidence path for <claim, effect, or use>` is legitimate when the evidence relation or provenance relation for the named claim, effect, or reliance use is current. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation, source-use function, or use relation is current.

The defect is not the word. The defect is hidden ontology: the sentence treats a representation as if something literally ran, flowed, executed, authorized, released, proved, selected, or prescribed action without first naming the exact direct object or relation and its subject pattern.

When the representation is route-shaped, loop-shaped, graph-shaped, diffusion-like, or workflow-like, ask first which object is current:

| Current object | Subject pattern |
| --- | --- |
| constraint-governed `U.Structure` across several constrained loci | `A.22.CGUS` |
| transformation-flow structure, path, path slice, crossing, guard, or valuation | `E.18` and `E.18.3` when unfolding use is current |
| description, diagram, table, graph, route card, slide, README line, or narrative that renders the structure | `ConstraintGovernedUnfoldingStructureDescription@Context`, `DemonstrativeUnfoldingSlice@Context`, `A.6.3.NAR`, `E.17`, or the direct description subject pattern |
| reusable semantic way of doing, or a claim-bearing episteme that passes the A.3.2 MethodDescription membership test | `A.3.1` for the method; `A.3.2` for the qualifying episteme |
| work plan, work readiness, or performed work | A.15 family |
| evidence, assurance, gate, decision, architecture, publication, or currentness-refresh claim | the subject pattern for that claim |

Do not repair route-shaped wording by replacing it with another route-shaped word. Always recover the visible expression, exact direct object or relation, representation or correspondence use or `none`, retained use, blocked stronger action claim, subject pattern, and stop or reopen condition. When the representation use is `none`, that is enough to close the repair; do not require a represented target, preserved and lost structure, or a mathematical-lens admissible-use account. When an exact representation, mathematical-lens, or selected-structure use is current, also name its target, the preserved and lost structure, and the admitted and blocked uses required by C.29 or that structure's subject pattern.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, plan, and work settlement

Do not repair `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, or `control strategy` by choosing one fashionable replacement.

**Method-description membership guard.** A code file, SOP, proof script, solver model, process model, protocol, recipe, diagram, or query plan is only a representation clue. First identify the claim-bearing episteme under C.2.1. Apply A.3.2 only when that same episteme has one admitted `U.Method` as its exact `EntityOfConcern` and at least one claim says how that method is done, such as its transformation or enactment concern, applicability, precondition, intended effect or preserved condition, bound, generic participant meaning, or internal method composition. A name, author, citation, approval, file form, runnable configuration, or representation correspondence alone is a near-miss. If the test fails, do not assign `U.MethodDescription`; keep the representation, publication, plan, dated work, result, formal substrate, mechanism declaration, evidence, or source use with its subject pattern. A representation or publication change does not decide membership. If claim content, exact method, or effective reference scheme changes, C.2.1 first identifies the resulting episteme; then apply A.3.2 to that individual.

Recover what the source is actually about and what it asserts:

| Current claim | Subject pattern |
| --- | --- |
| context-local semantic way of doing a transformation or enactment | `A.3.1 U.Method` |
| transformation or enactment kind stated inside a current method claim | keep it as one method-identity field or claim content under A.3.1; it is not a peer `U.Method` |
| independently grounded actual bounded change | `A.3.4 U.Transformation` |
| possible, required, desired, intended, planned, predicted, modeled, or asserted change | keep it as claim content under the exact requirement, architecture, capability-gap, functional-view, method, work-plan, dynamics-model, publication, or other subject pattern; wording alone admits no `U.Transformation` |
| already identified episteme whose exact `EntityOfConcern` is one admitted `U.Method` and whose claims include at least one substantive way-of-doing claim | `A.3.2 U.MethodDescription` |
| formal substrate, signature, postulates, laws, or mathematical declaration | `A.6.0`; use `C.29` when mathematical-lens use is current |
| operation algebra, admissibility predicates, transport, audit, realization, or mechanism-governing-definition assignment | `A.6.1` and `E.20` |
| planned work | `A.15.2 U.WorkPlan` |
| dated performed work | `A.15.1 U.Work` |
| evidence relation or provenance relation for a claim | `A.10` |
| wording quoted from source with no FPF-governed use | quote-only source wording |

**Cooling contrast.** A reusable cooling procedure can be `U.Method` only after the context-local way of doing, its transformation or enactment kind, transformed referent or structure, preconditions, and intended effects are recovered. “Required cooling effect” alone is claim content, not a method. If a later cooling episode actually changes the governed loop state, that occurrence remains a separate A.3.4 `U.Transformation` and needs its own changed referent, boundary, conditions, actual facts, and continuity or reidentification basis.

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal claims, use `E.10.ARCH:3.1` to state the project concern in ordinary words, then identify each exact object and claim separately. For this host, repair only the representation overread and name the subject pattern for the current claim; linked values remain under their own subject patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

Imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, Declare-style, SQL-like, e-graph, hypergraph, or process-mining wording is a clue to identify the visible expression, direct object or relation, any representation use, and current claim. It is not a decision procedure by itself.

Current practice makes the old contrast between imperative and declarative labels too weak as a final ontology:

- constructor and process-theory lines keep computation, information, dynamics, and procedure close to possible or impossible transformations and compositional realization;
- scoped effects and handlers separate operation syntax, semantic handling, scopes, resources, equations, type information, and effect information;
- Declare-style process models and object-centric event logs distinguish constraints, events, objects, relations, ingestion, transformation, storage, and analysis;
- e-graph and monoidal-rewriting work shows that computation or process representation may be equivalence or composition structure rather than instruction order.

Use those lines as guardrails: recover the exact FPF-governed object, relation, claim, or representation use and its subject pattern instead of replacing one programming-paradigm label with another.

### C.2.P.DR:5 - Worked slices

#### C.2.P.DR:5.1 - Graph path in a transformation-flow structure

Wording: "The P2W path routes the team from principle to work."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: P2W graph expression with a highlighted path or path slice
  CurrentDirectObjectOrRelation: exact E.18 `PathSlice` and E.18.1 carry-through relation among the named records when those objects are current
  RepresentationOrCorrespondenceUse: C.29 correspondence from this P2W graph expression to the exact E.18 `PathSlice`
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ordered work route for the team
  RecoveredGoverningPattern: E.18.1, with A.15.2 or A.15.1 only if planned or dated work is current
  RetainedUse: selected graph path and carry-through relation for inspection
  BlockedStrongerActionClaim: no work route or prescribed workflow by path shape alone
  StopOrReopenCondition: reopen when path, source currentness, graph edition, or intended work relation changes
```

A graph publication or pattern publication remains a separately governed publication object. If one is current, state its exact source or publication relation and participants in the neighbouring claim; neither publication object belongs in `SourceOrPublicationRelation` by mention alone.

#### C.2.P.DR:5.2 - Evidence path near release

Wording: "The evidence path authorizes release."

Repair: `A.10` can state an evidence path for the claim or effect. Release, permission, or gate passage requires the authority, gate, or release pattern that defines or constrains that claim. This pattern is used only if `path` wording itself is causing the representation to be overread as a permission route.

#### C.2.P.DR:5.3 - Query plan and access path

Wording: "The query plan calls the production work sequence."

Repair: recover whether the query plan represents optimizer choices, expresses claims about an exact method, presents a formal substrate, supplies a source cue or evidence relation, states a work plan, or records an actual query run. If it only represents query-evaluation choices, stop at the representation. Use A.3.1 for a reusable semantic way-of-doing claim. Use A.3.2 only when the claim-bearing episteme passes the MethodDescription membership guard in 4.4. Use A.15.1 for a performed query run, together with the exact evidence or source-use relation when that later claim is current.

#### C.2.P.DR:5.4 - Dashboard predicate

Wording: "The dashboard green path lets the release move."

Repair: recover dashboard face, source relation, status or state bearer, value frame, source currentness, and gate or release claim. The dashboard may be a publication face and source cue; it is not release permission unless the gate or authority pattern consumes the source and states that effect.

#### C.2.P.DR:5.5 - Pattern relation

Wording: "This pattern exits to A.10."

Repair: if the current relation is "use `A.10` when an evidence relation or provenance relation is current", write that declarative boundary. Do not use exit, receiver, route, owner, home, dispatch, or call language unless the pattern is actually about an action occurrence, work plan, control mechanism, or communication relation that has those semantics.

#### C.2.P.DR:5.6 - Solver algorithm

Wording: "The solver algorithm is the mechanism."

Repair: first identify what the solver expression represents and which claim is current. A solver configuration may represent claims carried by an episteme that qualifies as `U.MethodDescription` only after the 4.4 membership guard; the configuration is not that episteme by file form or executability. The reusable semantic way of solving may be `U.Method`; the MILP formulation may expose a formal substrate and mathematical-lens use; a reusable operation algebra with laws and admissibility predicates may be `U.Mechanism`; a solver run may be `U.Work`; and a run result may support another claim through its direct evidence relation. Select A.6.1 and E.20 only when their mechanism fields are present in the current claim.

#### C.2.P.DR:5.7 - Reactor-cooling flow graph

Wording: "The preserved heat-flow path authorizes the valve change."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: reactor-cooling heat-flow graph with one highlighted preserved path
  CurrentDirectObjectOrRelation: exact E.18 heat-flow path or `PathSlice`; keep boundary conditions and any flow valuation under their subject patterns
  RepresentationOrCorrespondenceUse: C.29 correspondence from this reactor-cooling graph rendering to the exact selected E.18 heat-flow `PathSlice`
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: graph path authorizes physical valve-change work
  RecoveredGoverningPattern: E.18 and C.29 for graph and lens use; A.21, A.10, A.15.2, and A.15.1 only if gate, evidence, work plan, or dated work is current
  RetainedUse: graph structure for comparison, model review, and source-finding
  BlockedStrongerActionClaim: no release, gate passage, physical intervention, or work occurrence by highlighted path alone
  StopOrReopenCondition: reopen when gate decision, source currentness, measurement boundary, or work plan becomes current
```

An engineering-review publication and a gate record remain separate objects. State any exact source or publication relation with its participants, and keep any gate relation under its subject pattern; neither object belongs in `SourceOrPublicationRelation`.

#### C.2.P.DR:5.8 - CRISPR guide-selection table

Wording: "The guide-selection table approves the edit."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: CRISPR guide-selection table with off-target scores and candidate ranking
  CurrentDirectObjectOrRelation: candidate-guide comparison and exact characteristic values under C.16 or A.19; add an A.10 evidence relation only when it independently obtains
  RepresentationOrCorrespondenceUse: C.29 correspondence from this table's candidate and off-target-score representation elements to the exact candidate-guide comparison and exact characteristic values named above
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ranked row approves biological intervention
  RecoveredGoverningPattern: C.16 or A.19 for characteristics when current; A.10 for evidence; A.15.2 for experimental work plan; A.21 or authority pattern only if approval or gate claim is current
  RetainedUse: source-finding, candidate comparison, and constraint review
  BlockedStrongerActionClaim: no edit approval, work occurrence, safety claim, or gate passage from table rank alone
  StopOrReopenCondition: reopen when protocol, gate decision, evidence path, lab classification or assignment, exact GrantedPermissionRelation@Context or direct authority result, or dated lab Work becomes current; unresolved “role authorization” goes to E.10.ROLE, and an unsupported stronger permission or authority claim returns missing-governor
```

A lab notebook, protocol publication, source episteme, and review record remain separate objects. State an exact source or publication relation and its participants only when it obtains; none of these objects belongs in `SourceOrPublicationRelation` by mention alone.

### C.2.P.DR:6 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C2PDR-1` | A repair separately names the visible expression or artifact, the exact current direct object or relation, and the exact representation or correspondence use or `none`; no field types structures, relations, formal objects, publication objects, or carrier-side objects as one family of representation kinds. |
| `CC-C2PDR-2` | When a representation use is current, the repair names its exact represented EntityOfConcern or claim and, for a mathematical-lens or selected-structure use, the preserved and lost structure and admitted and blocked uses required by its subject pattern; any current source or publication relation is named independently. When `RepresentationOrCorrespondenceUse` is `none`, no represented-target, preserved/lost-structure, or lens-use account is required. |
| `CC-C2PDR-3` | The tempting stronger action claim is explicit: route, call, dispatch, invoke, run, flow, send, receive, authorize, release, prove, prescribe, execute, select, pass a gate, or record work. |
| `CC-C2PDR-4` | The recovered subject pattern is named by value, or the case is demoted to quote-only, ordinary prose, reduced-use cue, blocked use, or incomplete rewrite. |
| `CC-C2PDR-5` | Legitimate `A.10 evidence path`, `E.18` graph path, `PathSlice`, carrier file path, URL, or mathematical path use is preserved when its exact evidence, provenance, graph, carrier/source, or mathematical object or relation is current. |
| `CC-C2PDR-6` | Method-like and algorithm-like wording identifies the visible expression, direct object or relation, current claim, and any exact representation use before selecting a subject pattern. If A.3.2 is selected, one already identified C.2.1 episteme has one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive way-of-doing claim; code, SOP, proof, solver, workflow, process, procedure, recipe, protocol, model, or diagram form alone does not pass. |
| `CC-C2PDR-7` | An `E.10.ARCH:3.1` project-concern recovery may connect method, mechanism, formal-substrate, work values, evidence relations, source relations, gate relations, or result relations, but each connected value keeps its own subject pattern and typed claim. |
| `CC-C2PDR-8` | The repair leaves one retained use and one blocked overread; type-correct but inert wording is incomplete. |
| `CC-C2PDR-9` | The pattern does not become a general representation theory, API pattern, schema pattern, legal framework, workflow framework, or generic admissibility pattern. |
| `CC-C2PDR-10` | Subject patterns keep their invariants. This pattern only restores representation use and blocked overread before those patterns carry their own claims. |

### C.2.P.DR:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Path word deletion | Every `path` is replaced or avoided. | Preserve legitimate `A.10`, `E.18`, carrier, mathematical, URL, and quoted-source path uses; repair only hidden stronger claims. |
| Imperative metaphor as ontology | Representations "route", "call", "dispatch", "receive", "invoke", or "flow" by prose habit. | Separate the visible expression, direct object or relation, exact representation use or `none`, and blocked stronger action claim; then write the direct relation declaratively. |
| Algorithm as method or description by form | Code, solver model, proof script, workflow, SOP, recipe, protocol, or diagram form is treated as proof of `U.Method` or `U.MethodDescription`. | Use A.3.1 only for the recovered reusable way of doing. Use A.3.2 only for an already identified claim-bearing episteme with one admitted `U.Method` as exact `EntityOfConcern` and a substantive way-of-doing claim; otherwise keep the representation or other claim with its subject pattern. |
| Mechanism by prestige | `mechanism` is used because the word sounds more rigorous than method or algorithm. | Require operation algebra, laws, admissibility predicates, transport, audit, realization, or governing-definition assignment. |
| Dashboard as gate | Green status, dashboard tile, score, or status label becomes permission or release. | Recover source relation or publication relation, state-family value, evidence relation, and gate or release pattern when current. |
| Pattern dispatcher | Pattern relations are written as routes, exits, receivers, calls, owners, or homes. | Write declarative neighboring-pattern boundary or application relation; use `E.8` and `F.19` together when both publication-form and phrase-apparatus claims are live, or use the one subject pattern when only one claim is live. |
| Generic representation theory | The repair tries to classify every representation in FPF or becomes an API pattern, schema pattern, legal framework, workflow framework, or generic admissibility pattern. | Stop at the representation-use field set and use the subject pattern for the current claim. |

### C.2.P.DR:8 - Relations

- **Builds on:** `E.10`, `E.10.ARCH`, `C.2.P`, `A.7`, `E.17`, `E.8`, and `F.19`.
- **Coordinates with:** `E.18`, `E.18.1`, `A.10`, `A.19.SPR`, `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.15.4`, `A.20`, `A.21`, `B.3`, and direct publication, gate, authority, release, evidence, method, work, and assurance patterns when those claims are being made.
- **Specializes:** `C.2.P` for one recurring case: declarative representation and imperative-metaphor overread.
- **Used by:** `E.10.ARCH` applicability-row distribution and full-pattern text precision restoration when route, path, workflow, call, or dispatch wording hides representation use.

### C.2.P.DR:9 - Consequences

- FPF can keep useful graph, path, query, table, dashboard, publication, and pattern-relation vocabulary without banning ordinary words.
- The repair blocks hidden authority, release, gate, evidence, method, mechanism, work, and pattern-dispatch claims by requiring the subject pattern named by value.
- Method and mechanism claims become easier to compose because `E.10.ARCH:3.1` keeps separately recovered values connected only by the exact direct relations and participant meanings supplied by their subject patterns, without treating source labels as alternate ontology.
- The cost is a small recovery note when representation wording is actually carrying FPF-governed use. Ordinary navigation, source quotation, and already-governed graph or evidence paths do not need the note.

### C.2.P.DR:10 - SoTA-Echoing

This pattern uses external sources only for the representation-overread repair question. They do not replace FPF ontology, and older famous sources are lineage or contrast unless a current source below supplies the contemporary payload.

| Exact source or practice anchor | Source-use function or relation | What it changes here |
| --- | --- | --- |
| `E.10`, `E.10.ARCH`, and `C.2.P` | Current FPF precision-restoration architecture. | This pattern is a bounded child realization under `C.2.P`, not a new umbrella pattern. |
| `A.10` and `E.18` | Local FPF subject patterns for evidence paths, provenance paths, transformation-flow graph paths, and path slices. | Path wording is legitimate when the exact evidence or provenance relation, graph path, or `PathSlice` is current; the defect is stronger overread. |
| `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, and `A.15.1` | Local FPF method-like and algorithm-like wording discipline. | The repair identifies the represented object and current claim before choosing method, qualifying method-description episteme, formal substrate, mechanism, work plan, or work occurrence; representation form alone chooses none of them. |
| Stefano Gogioso, Vincent Wang-Mascianica, Muhammad Hamza Waseem, Carlo Maria Scandolo, and Bob Coecke, "Constructor Theory as Process Theory", arXiv:2401.05364, EPTCS 397, 2023; David Deutsch and Chiara Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Current SoTA decision payload for transformation-theory and process-theory repair of computation, method, and dynamics wording. | Computation, information, dynamics, and procedure wording is interpreted through possible or impossible transformation and compositional-process claims when that claim is current, not through software notation or ordered instruction prose first. |
| Roger Bosman, Birthe van den Berg, Wenhao Tang, and Tom Schrijvers, "A Calculus for Scoped Effects & Handlers", Logical Methods in Computer Science 20(4), 2024, arXiv:2304.09697; Cristina Matache, Sam Lindley, Sean Moss, Sam Staton, Nicolas Wu, and Zhixuan Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Current SoTA decision payload for effectful computation and programming-model wording. | Operation syntax, semantic handling, scope, resources, equations, and effect information remain separable; pure-function slogans and imperative-declarative slogans are not enough. |
| Francesco Chiariello, Valeria Fionda, Antonio Ielo, and Francesco Ricca, "Direct Encoding of Declare Constraints in ASP", Theory and Practice of Logic Programming 25, 2025, arXiv:2412.10152; Alessandro Berti et al., "OCEL (Object-Centric Event Log) 2.0 Specification", arXiv:2403.01975; Lien Bosmans et al., "Dynamic and Scalable Data Preparation for Object-Centric Process Mining", arXiv:2410.00596. | Current SoTA decision payload for process-model, trace, workflow, and event-record wording. | Constraint, event, object, relation, data model, ingestion, transformation, storage, and analysis claims are recovered separately before a method, work plan, work occurrence, evidence, or gate claim is accepted. |
| Aleksei Tiurin, Chris Barrett, Dan R. Ghica, and Nick Hu, "Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs", arXiv:2406.15882, v2 revised 2025-05-20. | Current SoTA decision payload for graph, equivalence, and compositional-representation wording. | Graph, equality, equivalence, and rewrite objects keep their direct kinds; any representation relation to them remains separate from instruction order, method, work, or action claims. |
| Robert Kowalski 1979; E. F. Codd 1970; Selinger et al. 1979; van der Aalst, Pesic, and Schonenberg 2009; Van Roy and Haridi 2004; Deutsch 2013; Deutsch and Marletto 2015. | Historical lineage or contrast only. | These sources explain why the overread is recognizable; they do not carry current SoTA weight for this pattern by age, fame, or popularity. |

### C.2.P.DR:End

