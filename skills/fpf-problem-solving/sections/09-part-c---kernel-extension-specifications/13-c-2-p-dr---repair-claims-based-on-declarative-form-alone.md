## C.2.P.DR - Repair Claims Based on Declarative Form Alone (Declarative Representation Precision Restoration)

> **Type:** C.2.P precision-restoration child pattern for declarative-representation overread
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.2.P.DR:0 - Use this when

Use this pattern when the appearance of a representation is being used to establish an operational or classification claim without its required grounds—for example, treating a green dashboard tile as release permission or a graph path as prescribed work.

**First useful move.** Identify the expression and the claim being inferred from it. Recover what the expression states or represents, then apply the rule for the disputed claim. Return wording that preserves the supported use and identifies what remains unestablished. A sentence can suffice. Use a `DeclarativeRepresentationRepair` note only when the receiving use needs a separately inspectable repair.

**Quick example.** A heat-flow graph in a reactor-cooling review can show preserved and lost flow relations. It does not authorize a valve change by graph shape. The repair keeps the graph path as graph structure, returns release or gate reliance to the gate, source, and evidence patterns, and blocks the hidden work-permission claim.

Use this pattern especially when:

- a graph path or selected flow structure is treated as a prescribed work sequence;
- an `A.10` evidence path is treated as permission, release or assurance;
- a query plan or program-like expression is treated as a method or as performed work;
- a publication or pattern reference is treated as an actual call, send or application;
- method-like wording leaves the way of doing, its description and an actual episode indistinguishable.

**What goes wrong if missed.** A reader relies on an effect that the expression does not establish. The green tile may report a status while the required release decision is absent; program-like text may be mistaken for a method without identifying a way of doing.

**What this buys.** The reader can retain a useful graph, query or publication while resolving the disputed operational claim under its own rule. An object under direct inspection stays distinct from a representation of that object.

**Not this pattern when.**

- If the graph path, `PathSlice`, or flow valuation is already current as graph structure, use `E.18` directly.
- If the evidence-use or status-use classification of an episteme is already the question, use `A.2.4`. Use `A.10` when source recovery, provenance, currentness or bounded reliance must remain replayable.
- If the publication face or source-use relation is already current, use `E.17`, `E.17.EFP`, `C.2.P`, or the direct publication pattern.
- If the current claim concerns a semantic way of doing, use `A.3.1`; if it concerns the description of that way, use `A.3.2`.
- If the question concerns a reusable operation declaration or its applicability, use `A.6.1`. Use `E.20` when an FPF introduction or revision triggers its mechanism-introduction protocol.
- If the current claim concerns planned work or dated work, use `A.15.2` or `A.15.1`.
- If the word is only quoted source wording or ordinary navigation prose with no FPF-governed claim, keep it quote-only or ordinary.

### C.2.P.DR:1 - Problem frame

A graph can itself be the object under inspection, or a drawing can represent a graph. A table can express claims about a system, or its layout can be the publication form being examined. Recover that distinction before deciding which rule governs the disputed use.

The recurring failure is an unsupported shift from appearance to operational effect. For example, an arrow in a graph can represent a relation without prescribing an action or proving that it occurred.

This pattern repairs that shift. It does not build a general theory of representation. It only restores the exact FPF-governed object, relation, or claim and its subject pattern when declarative-looking wording is overread as imperative or operational.

### C.2.P.DR:2 - Problem

Without this repair:

1. **Graph path becomes work route.** A path or path slice in `E.18` is treated as an ordered work narrative, even when no work occurrence, work plan, or method description is current.
2. **Evidence path becomes permission.** An evidence relation or provenance relation is treated as approval, gate passage, release, safety, or authority rather than as evidence for a named claim or effect.
3. **Query becomes method.** A query, access path, query plan, or dashboard is treated as the semantic way of doing, rather than as a representation, method description, evidence relation, source relation, or ordinary source wording.
4. **Pattern relation overread as dispatch.** A reference to another pattern is treated as an actual call or work occurrence. Ordinary navigation remains adequate when it expresses the intended relation clearly.
5. **Programming-paradigm label becomes ontology.** A label such as functional, declarative or workflow is treated as sufficient to determine an FPF kind.
6. **Mechanism, method, and work collapse.** A method-like expression is repaired to `method` or `mechanism` by vocabulary rather than by the current claim: way of doing, description, formal substrate, law-governed mechanism, plan, occurrence, evidence, or quote-only wording.

### C.2.P.DR:3 - Forces

| Force | Tension |
| --- | --- |
| Representation usefulness and action overread | Graphs, queries, predicates, and dashboards are useful because they expose structure; their shape does not supply hidden work, permission, or release. |
| Legitimate path words and metaphor repair | `A.10 evidence path`, `E.18` graph path, and carrier file paths may be legitimate; `path` becomes a defect only when it carries a stronger action or authority claim by metaphor. |
| Method generality and subject discipline | Algorithms, programs, solver models, proofs, SOPs, and process models can all be useful, but first identify the direct object or relation, the current claim, and any exact representation use. Select `U.MethodDescription` only after the claim-bearing episteme passes the A.3.2 membership test; representation form alone selects nothing. |
| Paradigm label and semantics | A programming or process label can locate a source treatment, but the object and claim determine the receiving FPF rule. |
| Subject pattern and local repair | When `E.18`, `A.10`, `A.3.1`, `A.3.2`, `A.6.1`, `A.15.2`, `A.15.1`, `E.17`, or another pattern already governs the current claim, this pattern names only the overread and leaves the next claim to that pattern rather than duplicating it. |

### C.2.P.DR:4 - Solution

Repair declarative-representation overread by separating the visible expression, the direct object or relation, and any representation use before naming the subject pattern for the current claim.

The repair order is:

1. **Identify the expression.** Quote or point to the part that prompted the unsupported inference.
2. **Recover the object or relation at issue.** For example, distinguish a graph path, an evidence relation and a reported state value. Use its subject pattern when that rule is already clear; the selection table below helps when it is not.
3. **Distinguish the direct object from any representation or correspondence use.** When the visible expression represents a separately identified object or claim, name the exact relation and target. When the direct object or relation itself is current and no separate representation claim is needed, keep that direct use; do not relabel the direct object as a representation kind. Record `none` only when the receiving use needs an inspectable account of that distinction.
4. **Recover a source or publication relation when it matters to this claim.** Use the pattern governing that relation and its actual participants.
5. **State the disputed operational claim.** Name the action, result or authority being inferred from the expression.
6. **Apply the claim's subject pattern.** Establish its required grounds or identify what is missing. An actual permission or gate condition comes from that rule.
7. **Preserve the supported use.** The graph may still support a comparison, for example, while leaving action permission unresolved.
8. **Delimit the unsupported claim.** Do not assert the stronger result from appearance alone. Distinguish that missing basis from a use blocked by an applicable rule; a separately established result remains usable under its own conditions.
9. **Stop or reopen.** Stop when the repaired statement supports the intended use or the subject pattern supplies the remaining question. Reopen when a changed source, correspondence or intended use can invalidate that result.

#### C.2.P.DR:4.1 - DeclarativeRepresentationRepair note

Use this compact note only when the receiving use needs an inspectable repair of FPF-governed wording:

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

The ordinary result is the repaired statement and any unresolved condition that changes its use. In the optional note, `BlockedStrongerActionClaim` identifies the assertion that appearance does not establish; it does not by itself declare the underlying action prohibited. Name a blocked use and its governing condition separately when applicable. Reuse a suitable subject-pattern record without copying it into another repair note.

Use four plain questions before the claim-and-pattern table: What visible thing am I looking at? What direct object or relation is current? What, if anything, does it represent? Which stronger claim still needs grounds?

| Visible expression or artifact | Direct object or relation at issue | Representation or correspondence use | Stronger action claim blocked |
| --- | --- | --- | --- |
| highlighted graph path | exact E.18 graph path or `PathSlice`, with any flow valuation kept separate | the graphic rendering corresponds to that path when the relation is current; otherwise `none` when the `PathSlice` itself is under inspection | no prescribed route, valve work, or release by the highlight |
| dashboard tile | exact status or state value with its bearer and value frame, plus any current source or publication relation | the tile represents that value only through an exact current relation; otherwise `none` when the publication face itself is the direct object | no gate passage or release permission from green appearance |
| evidence-path expression | descriptive A.10 evidence-provenance path for the named claim or bounded use, citing independently established direct relations | a diagram may represent that descriptive path through an exact current correspondence; otherwise `none` when the path itself is under inspection | no approval, permission, assurance, or release from path shape |
| solver file | exact publication form or carrier-side object, and whichever formal substrate, claim-bearing episteme, method, mechanism declaration, plan, run, or evidence relation is independently current | the solver expression corresponds to separately identified claims or a formal object when that relation is stated; otherwise `none` | no method, mechanism, performed work, result, or evidence by file form or executability |
| publication table | exact publication face or form and source relation, with table values or claims kept under their subject patterns | the table corresponds to a separately identified object or claim only when the exact relation is current; otherwise `none` | no evidence, approval, gate passage, or action authority from table layout |

#### C.2.P.DR:4.2 - Subject pattern selection

| If recovery shows... | Use this subject pattern | Keep this boundary |
| --- | --- | --- |
| graph object, graph path, `PathSlice`, crossing, flow valuation, transformation-flow structure relation, or graph expression over that structure | `E.18`, `E.18.2`, or `E.18.1` when P2W carry-through is current | Graph structure or path structure is not work route, method narrative, evidence result, or pattern dispatch by layout. |
| evidence use or provenance for a claim, effect, or reliance use | `A.2.4` for an episteme's evidence use; the direct pattern for the claim or relation; `A.10` when the source-to-use account must remain replayable | Evidence path is not approval, permission, gate passage, release, safety, work occurrence, or assurance by itself. |
| state, status value, readiness, validity, or predicate-like value whose bearer and value frame is hidden | `A.19.SPR` or the direct status-value or state-value pattern | A predicate or state-like value is not a workflow, gate, or proof unless the subject pattern says so. |
| publication face, source expression, generated explanation, dashboard face, publication unit, or source-chain relation | `E.17`, `E.17.EFP`, `C.2.P`, `A.15.4`, or source-use pattern named by value | Publication and source visibility do not create work, evidence, authority, release, or gate passage. |
| mathematical representation, formal object, formal substrate, invariant, or mathematical-lens output | `A.6.0` or the direct mathematical pattern; `C.29` when a separate representation choice, transfer or reliance question remains | Mathematical representation is not method, mechanism, proof of project result, or work execution until that claim is separately recovered. |
| context-local semantic way of doing | `A.3.1 U.Method` | Recover the way of doing and its identity and applicability under A.3.1 from the substantive claims, which may be conveyed in code or another expression. Form alone does not settle Method identity. Use `E.10.ARCH:3.1` only while a linked object or claim remains unclear; otherwise use its subject pattern directly. |
| a question about whether one independently identified `U.Episteme` is a `U.MethodDescription`, or about using its method claims | `A.3.2 U.MethodDescription` | Test the exact `EntityOfConcern` and substantive way-of-doing content. Positive membership requires the admitted Method and content specified by A.3.2; retain negative or unresolved outcomes when those conditions fail or remain unknown. Representation form alone does not settle membership. |
| reusable operation declaration, or a neighboring realization, transport, audit or evaluation claim | `A.6.1` for declaration content; the direct pattern for a neighboring relation; `E.20` when an FPF introduction or revision triggers its protocol | Recover and test the declaration and its required content; an algorithm or method label supplies neither that qualification nor a neighboring relation. |
| planned work, intended window, resource budget, acceptance criterion, or source “role requirement” | `A.15.2 U.WorkPlan` for the plan. Resolve a “role requirement” separately to its exact local system-role kind, separate System-classification judgment, future assignment condition, capability, participant relation, or other direct condition; if unresolved, use `E.10.ROLE`. | The same episteme may also qualify as `U.MethodDescription` under A.3.2, and its use as evidence depends on the claim and applicable grounds. Planning content alone establishes no gate passage, performed Work or obtaining assignment; recover any claimed Method identity under A.3.1. A required kind or condition does not create the future assignment. |
| exact dated Work occurrence | Apply A.13, then `A.15.1 U.Work`; the explanation below gives the representation and F.6 attribution conditions. | The Work occurrence is not its trace, record, binding, resource use, result, diagram, plan, MethodDescription, source cue, or evidence path. |
| run trace or performed-work record | `C.2.1` for the exact trace or record episteme, plus its direct description, publication, source-use, or evidence-use pattern only when that claim is current | The episteme may designate exact `W`, `RA`, holder `S`, and `performedUnderAssignment(W, RA)` when it makes that attribution; it neither is the Work occurrence nor makes the relation obtain. |
| concrete parameter or participant binding | the direct subject-relation pattern, or `A.6.1` for one independently identified operation application and its actual argument or result binding | A declaration, call position, trace field, or type-compatible token establishes no actual binding. |
| performed resource use | the exact direct resource-use relation involving the already identified Work occurrence; use `B.1.6` only when aggregation is current | Resource use is a separately obtaining relation, not a Work field, record field, or result. |
| result or output | identify the exact result entity or episteme first; use `A.15.PROD` when production, entity inception, or production completion is current, and `A.6.RCD` only when the needed direct result relation has no current governor | A binding, record field, Work occurrence, or nearby output label does not identify the result or establish production. |
| FPF pattern application, pattern relation, neighboring-pattern relation, or placement cue | `E.8`, `F.19`, `E.10.ARCH`, or the direct pattern relation named by value | Pattern relations are declarative references or applications. Exit, receiver, route, call, owner, home, or dispatch wording must express a clear ordinary or technical relation; wording alone supplies no action or control semantics. |
| quoted source wording or ordinary navigation | quote-only or ordinary prose | Do not repair ordinary words into FPF terms when no FPF-governed claim is being made. |

**Dated Work: admission, representation and attribution.**

Recover every actual performer and its obtaining A.2.1 system-role assignment through A.13, then let `A.15.1 U.Work` independently identify the dated occurrence, enacted Method, time, and containing System.

A representation claiming the exact Work keeps every actual performer named or recoverable. Keep the underlying assignment facts recoverable; include an assignment identifier in the representation only when the receiving use needs it.

Add an F.6 relation through that same obtaining assignment only when the representation or receiving use expressly represents precise assignment-bound attribution. Missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds still hold and blocks only that attribution.

#### C.2.P.DR:4.3 - Legitimate path and route settlement

`A.10 evidence path for <claim, effect, or use>` is legitimate when a descriptive source-to-use account is current under A.10. `E.18` graph path and `PathSlice` are legitimate when the graph object, path, slice, crossing, or flow valuation is current. Carrier file paths, URLs, mathematical paths, and quoted source paths are legitimate when their notation, source-use function, or use relation is current.

Repair path wording when it carries an unsupported claim about what happens or what may be done. A clear ordinary reference or navigation instruction can remain unchanged.

For a route or unfolding expression, identify the object before selecting its rule:

| Current object | Subject pattern |
| --- | --- |
| constraint-governed `U.Structure` across several constrained loci | `A.22.CGUS` |
| transformation-flow structure, path, path slice, crossing, guard, or valuation | `E.18` and `E.18.3` when unfolding use is current |
| description, diagram, table, graph, route card, slide, README line, or narrative that renders the structure | `A.22.CGUS:4.4` for descriptions of a qualified CGUS and post-qualification demonstrative slices, including the wording `ConstraintGovernedUnfoldingStructureDescription@Context` or `DemonstrativeUnfoldingSlice@Context`; `A.6.3.NAR` for narrative rendering; `E.17` for publication; or the direct description subject pattern |
| reusable semantic way of doing, or a MethodDescription membership or use question about one identified episteme | `A.3.1` for the way of doing; `A.3.2` for the MethodDescription question |
| work plan, work readiness, or performed work | A.15 family |
| evidence, assurance, gate, decision, architecture, publication, or currentness-refresh claim | the subject pattern for that claim |

Recover the relation the route expression conveys. Direct inspection of a graph object needs no separate represented target or lens account. If a representation or selected structure supports an inference, establish its target and the preservation or loss relevant to that inference under its subject pattern. Use C.29 for a separate mathematical representation or transfer issue; adequate local mathematics or an unambiguous rendering can suffice without a C.29 record.

#### C.2.P.DR:4.4 - Method, algorithm, mechanism, plan, and work settlement

For method-like wording, recover the claimed way of doing and distinguish it from its expression and any actual performance.

**Method-description membership.** First identify the claim-bearing episteme under C.2.1. Use A.3.2 to determine whether that same individual is a `U.MethodDescription`. Positive membership requires one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive claim about that Method as a way of doing. Such a claim can state its transformation or enactment concern, applicability, precondition, intended effect or preserved condition, bound, generic participant meaning, or internal composition.

When either condition is false, membership fails; when the available basis does not settle them, leave membership unresolved. Representation form, execution or approval alone does not supply these conditions. Keep any independently established representation, publication, plan, Work, result, formal declaration or evidence use under its own pattern.

A representation or publication change does not decide membership. If claim content, exact subject or effective reference scheme changes, identify the resulting episteme under C.2.1 and apply the test to that individual.

Recover what the source is about and what it asserts:

| Current claim | Subject pattern |
| --- | --- |
| context-local semantic way of doing a transformation or enactment | `A.3.1 U.Method` |
| transformation or enactment kind stated inside a current method claim | keep it as one method-identity field or claim content under A.3.1; it is not a peer `U.Method` |
| independently grounded actual bounded change | `A.3.4 U.Transformation` |
| possible, required, desired, intended, planned, predicted, modeled, or asserted change | keep it as claim content under the exact requirement, architecture, capability-gap, functional-view, method, work-plan, dynamics-model, publication, or other subject pattern; wording alone admits no `U.Transformation` |
| a question about whether one identified episteme substantively describes an admitted Method, or about using those method claims | `A.3.2 U.MethodDescription` |
| formal substrate, signature, postulates, laws, or mathematical declaration | `A.6.0`; use `C.29` when a separate mathematical-representation choice, transfer or reliance question remains |
| reusable operation declaration, or a neighboring realization, transport, audit or governing-definition-assignment question | `A.6.1` for declaration content; the direct pattern for the neighboring relation; `E.20` when an FPF introduction or revision triggers its protocol |
| planned work | `A.15.2 U.WorkPlan` |
| dated performed work | `A.15.1 U.Work` |
| evidence-use or provenance question for a claim | `A.2.4` for an episteme's evidence use; the direct pattern for a provenance relation; `A.10` when source-to-use recovery or reliance must remain replayable |
| wording quoted from source with no FPF-governed use | quote-only source wording |

**Cooling contrast.** A reusable cooling procedure can be `U.Method` only after the context-local way of doing, its transformation or enactment kind, transformed referent or structure, preconditions, and intended effects are recovered. “Required cooling effect” alone is claim content, not a method. If a later cooling episode changes the governed loop state, that occurrence remains a separate A.3.4 `U.Transformation` and needs its own changed referent, boundary, conditions, facts, and continuity or reidentification basis.

When the source label hides method, mechanism, formal-substrate, work, evidence, gate, result, or temporal claims, use `E.10.ARCH:3.1` to state the project concern in ordinary words, then identify each exact object and claim separately. Use this pattern to repair only the representation overread and name the subject pattern for the current claim; linked values remain under their own subject patterns rather than becoming one representation-repair claim.

#### C.2.P.DR:4.5 - Programming-paradigm and process-model settlement

A paradigm label helps locate the relevant source semantics. Those semantics, together with the claim, determine which FPF question to ask.

The source distinctions below help identify what an expression is being used to claim:

- constructor and process theories distinguish an abstract task from the physical processes proposed to implement it; recover whether the account specifies a transformation or asserts its performance;
- scoped-effect calculi distinguish an operation, its handler and the rules governing scope and effects; recover which object and semantic relation the current claim concerns;
- Declare constraints restrict admissible traces, while object-centric logs record events and object relations; data-ingestion and transformation pipelines are another subject, so identify which of these the account describes;
- e-graphs and monoidal rewriting represent equivalence and composition; inspect that relation before treating an edge or rewrite as execution order.

Use the distinction relevant to the case to recover the object or claim, then apply its subject pattern.

### C.2.P.DR:5 - Worked slices

#### C.2.P.DR:5.1 - Graph path in a transformation-flow structure

Wording: "The P2W path routes the team from principle to work."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: P2W graph expression with a highlighted path or path slice
  CurrentDirectObjectOrRelation: exact E.18 `PathSlice` and E.18.1 carry-through relation among the named records when those objects are current
  RepresentationOrCorrespondenceUse: highlighted nodes and edges render the selected E.18 `PathSlice`; the highlight adds no work ordering
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ordered work route for the team
  RecoveredGoverningPattern: E.18.1, with A.15.2 or A.15.1 only if planned or dated work is current
  RetainedUse: selected graph path and carry-through relation for inspection
  BlockedStrongerActionClaim: no work route or prescribed workflow by path shape alone
  StopOrReopenCondition: stop at inspection of the selected path and carry-through relation; use A.15.2 for a prescribed work sequence. If a separate mathematical transfer is proposed, establish its C.29 correspondence and limits before relying on that transfer. Reopen when the selected graph, source or intended work relation changes
```

#### C.2.P.DR:5.2 - Evidence path near release

Wording: "The evidence path authorizes release."

Repair: name the claim or bounded use and recover its grounds under the direct subject pattern. Add the descriptive A.10 source-to-use account when source recovery, provenance, currentness or bounded reliance must remain replayable. Release, permission, or gate passage requires the authority, gate, or release pattern that defines or constrains that claim. This pattern is used only if `path` wording itself is causing the representation to be overread as a permission route.

#### C.2.P.DR:5.3 - Query plan and access path

Wording: "The query plan calls the production work sequence."

Repair: recover whether the query plan represents optimizer choices, expresses claims about an exact method, presents a formal substrate, supplies a source cue or evidence relation, states a work plan, or records an actual query run. If it only represents query-evaluation choices, stop at the representation.

Use A.3.1 for a reusable semantic way-of-doing claim. Use A.3.2 when MethodDescription membership or a use of the method claims is the question; apply the test in 4.4 and retain its positive, negative or unresolved membership result. Use A.15.1 for a performed query run, together with the exact evidence or source-use relation when that later claim is current.

#### C.2.P.DR:5.4 - Dashboard predicate

Wording: "The dashboard green path lets the release move."

Repair: recover dashboard face, source relation, status or state bearer, value frame, source currentness, and gate or release claim. The dashboard may be a publication face and source cue. Recover release permission through the applicable gate decision (`A.21`) or authority relation, including any source contribution required by its governing rule.

#### C.2.P.DR:5.5 - Pattern relation

Wording: "This pattern exits to A.10."

Repair: if the current relation is "use `A.10` when the source-to-use account must remain replayable", write that declarative boundary. Keep ordinary ownership or navigation wording when its relation and participants are clear. Use exit, receiver, route, owner, home, dispatch, or call language to assert action or control only when the pattern is about an action occurrence, work plan, control mechanism, or communication relation that has those semantics.

#### C.2.P.DR:5.6 - Solver algorithm

Wording: "The solver algorithm is the mechanism."

Repair: first identify the direct object or relation, any representation use, and which claim is current. A solver configuration may represent claims carried by a separately identified episteme; apply A.3.2 when MethodDescription membership is the question. File form or executability alone does not establish that membership.

The reusable semantic way of solving may be `U.Method`; the MILP formulation may expose a formal substrate; a declaration episteme for a reusable operation family, with its required laws and applicability, may qualify as `U.Mechanism` under A.6.1; a solver run may be `U.Work`; and a run result may support another claim through its direct evidence relation.

Use A.6.1 to recover and test the proposed declaration. Use E.20 when an FPF introduction or revision triggers its protocol.

#### C.2.P.DR:5.7 - Reactor-cooling flow graph

Wording: "The preserved heat-flow path authorizes the valve change."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: reactor-cooling heat-flow graph with one highlighted preserved path
  CurrentDirectObjectOrRelation: exact E.18 heat-flow path or `PathSlice`; keep boundary conditions and any flow valuation under their subject patterns
  RepresentationOrCorrespondenceUse: the rendering identifies the selected E.18 path; a proposed inference from its edges to physical heat flow lacks its correspondence and boundary conditions
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: graph path authorizes physical valve-change work
  RecoveredGoverningPattern: E.18 for graph inspection; C.29 for the unresolved mathematical transfer; A.10 when its source-to-use account must remain replayable; A.21, A.15.2 or A.15.1 only for a current gate, work-plan or dated-Work question
  RetainedUse: graph inspection and identification of the missing heat-flow correspondence
  BlockedStrongerActionClaim: no release, gate passage, physical intervention, or work occurrence by highlighted path alone
  StopOrReopenCondition: keep the proposed physical inference unresolved until the correspondence, material losses and boundary conditions support it under C.29; operational reliance also needs the applicable validation and gate or authority result. Reuse adequate existing domain/model documentation. Reopen when that basis or intended intervention changes
```

#### C.2.P.DR:5.8 - CRISPR guide-selection table

Wording: "The guide-selection table approves the edit."

Repair:

```text
DeclarativeRepresentationRepair:
  VisibleExpressionOrArtifact: CRISPR guide-selection table with off-target scores and candidate ranking
  CurrentDirectObjectOrRelation: candidate-guide comparison and exact characteristic values under C.16 or A.19; recover any direct support relation under its subject pattern, with A.2.4 for an episteme's evidence use and A.10 for a needed replayable source-to-use account
  RepresentationOrCorrespondenceUse: rows identify the compared candidate guides and columns reproduce named score values with their scales and source references; the ranking adds no approval relation
  SourceOrPublicationRelation: none
  TemptingStrongerActionClaim: ranked row approves biological intervention
  RecoveredGoverningPattern: C.16 or A.19 for characteristics when current; A.2.4 for an episteme's evidence use; A.10 when the source-to-use account must remain replayable; A.15.2 for experimental work plan; A.21 or authority pattern only if approval or gate claim is current
  RetainedUse: source-finding, candidate comparison, and constraint review
  BlockedStrongerActionClaim: no edit approval, work occurrence, safety claim, or gate passage from table rank alone
  StopOrReopenCondition: stop at the supported comparison under the stated score meanings and source conditions. Use C.29 when a separate mathematical-representation choice, transfer or reliance question remains. Intervention approval needs its applicable authority or gate result; resolve unclear “role authorization” through E.10.ROLE, distinguishing a missing rule from missing facts under a known rule. Reopen when the scores, protocol or intended use changes
```

### C.2.P.DR:6 - Conformance checklist

| Check | Requirement |
| --- | --- |
| `CC-C2PDR-1` | A repair separately names the visible expression or artifact, the exact current direct object or relation, and any current representation or correspondence use. Record `none` for the representation branch only when the receiving use needs an inspectable account. No field types structures, relations, formal objects, publication objects, or carrier-side objects as one family of representation kinds. |
| `CC-C2PDR-2` | When a representation use is current, the repair names its exact represented EntityOfConcern or claim and, for a mathematical-lens or selected-structure use, the preserved and lost structure and admitted and blocked uses required by its subject pattern; any current source or publication relation is named independently. When `RepresentationOrCorrespondenceUse` is `none`, no represented-target, preserved/lost-structure, or lens-use account is required. |
| `CC-C2PDR-3` | The disputed operational claim is explicit. Its missing grounds remain distinct from a use blocked by an applicable rule. |
| `CC-C2PDR-4` | Use the recovered subject pattern for the governed claim. Sufficient ordinary wording or a bounded source quotation may finish without further formalization. If recovery is incomplete, retain only the supported use and identify the unresolved claim; apply any stop under its governing rule. |
| `CC-C2PDR-5` | Legitimate `A.10 evidence path`, `E.18` graph path, `PathSlice`, carrier file path, URL, or mathematical path use is preserved when its exact evidence, provenance, graph, carrier/source, or mathematical object or relation is current. |
| `CC-C2PDR-6` | Method-like and algorithm-like wording identifies the visible expression, direct object or relation, current claim, and any exact representation use before selecting a subject pattern. If A.3.2 is selected, test whether the identified C.2.1 episteme has one admitted `U.Method` as its exact `EntityOfConcern` and at least one substantive way-of-doing claim. Positive membership requires both conditions; retain a negative or unresolved result when the test warrants it. Representation form alone does not settle membership. |
| `CC-C2PDR-7` | An `E.10.ARCH:3.1` project-concern recovery may connect method, mechanism, formal-substrate, work values, evidence relations, source relations, gate relations, or result relations, but each connected value keeps its own subject pattern and typed claim. |
| `CC-C2PDR-8` | The repair preserves the supported use and delimits the unsupported inference. It leaves the reader with the needed result or a specific unresolved condition. |
| `CC-C2PDR-9` | The repair stays within declarative-representation overread; separately governed questions use their own patterns. |
| `CC-C2PDR-10` | Subject patterns keep their invariants. This pattern only restores representation use and blocked overread before those patterns carry their own claims. |

### C.2.P.DR:7 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Path word deletion | Every `path` is replaced or avoided. | Preserve legitimate `A.10`, `E.18`, carrier, mathematical, URL, and quoted-source path uses; repair only hidden stronger claims. |
| Imperative metaphor as ontology | Representations "route", "call", "dispatch", "receive", "invoke", or "flow" by prose habit. | Separate the visible expression, direct object or relation, exact representation use or `none`, and blocked stronger action claim; then write the direct relation declaratively. |
| Algorithm as method or description by form | Representation form is treated as proof of `U.Method` or `U.MethodDescription`. | Use A.3.1 for the reusable way of doing and A.3.2 for a MethodDescription membership question about an identified episteme. Apply the conditions in 4.4, retaining positive, negative or unresolved membership and any independently established other use. |
| Mechanism by prestige | `mechanism` is used because the word sounds more rigorous than method or algorithm. | Recover and test the reusable declaration and its required content under A.6.1. Keep realization, transport, audit and other neighboring relations under their direct patterns. |
| Dashboard as gate | Green status, dashboard tile, score, or status label becomes permission or release. | Recover source relation or publication relation, state-family value, evidence relation, and gate or release pattern when current. |
| Pattern dispatcher | Pattern relations are given action or control effects through route, exit, receiver, call, owner, or home wording. | Write declarative neighboring-pattern boundary or application relation; use `E.8` and `F.19` together when both publication-form and phrase-apparatus claims are live, or use the one subject pattern when only one claim is live. |
| General theory substituted for repair | The repair expands into classifying all representations. | Resolve the disputed inference and continue under its subject pattern. |

### C.2.P.DR:8 - Relations

- **Builds on:** `E.10`, `E.10.ARCH`, `C.2.P`, `A.7`, `E.17`, `E.8`, and `F.19`.
- **Coordinates with:** `E.18`, `E.18.1`, `A.2.4`, `A.10`, `A.19.SPR`, `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.15.2`, `A.15.1`, `A.15.4`, `A.20`, `A.21`, `B.3`, and direct publication, gate, authority, release, evidence, method, work, and assurance patterns when those claims are made.
- **Specializes:** `C.2.P` for one recurring case: declarative representation and imperative-metaphor overread.
- **Used by:** `E.10.ARCH` applicability-row distribution and full-pattern text precision restoration when route, path, workflow, call, or dispatch wording hides representation use.

### C.2.P.DR:9 - Consequences

- FPF can keep useful graph, path, query, table, dashboard, publication, and pattern-relation vocabulary without banning ordinary words.
- Operational claims receive their grounds and conditions; a supported comparison remains useful while a stronger claim is unresolved.
- Method and mechanism claims become easier to compose because `E.10.ARCH:3.1` keeps separately recovered values connected only by the exact direct relations and participant meanings supplied by their subject patterns, without treating source labels as alternate ontology.
- The cost is this recovery, with a small note only when the receiving use needs an inspectable repair. Ordinary navigation, source quotation, and already-governed graph or evidence paths do not need the note.

### C.2.P.DR:10 - SoTA-Echoing

The sources below support the stated distinctions. The final column gives their use in this FPF repair.

| Exact source or practice anchor | Source-use function or relation | What it changes here |
| --- | --- | --- |
| Gogioso et al., ["Constructor Theory as Process Theory"](https://arxiv.org/abs/2401.05364v1), EPTCS 397, 2023; Deutsch and Marletto, ["Constructor theory of time"](https://arxiv.org/abs/2505.08692v3), revised 2026-06-05. | The first relates abstract tasks to their physical implementations in a compositional process framework. The second formulates laws through possible and impossible transformations and examines duration and dynamics on that basis. | Recover whether the current claim specifies a task, proposes an implementation or asserts performance, then apply the corresponding subject rule from 4.4. |
| Bosman et al., ["A Calculus for Scoped Effects & Handlers"](https://arxiv.org/abs/2304.09697v7), LMCS 20(4), 2024; Matache et al., ["Scoped Effects as Parameterized Algebraic Theories"](https://arxiv.org/abs/2402.03103v2), ESOP 2024 extended version. | The first supplies operational semantics and a type-and-effect system for scoped effects and handlers. The second gives an algebraic treatment of scoped operations and equations for equational reasoning. | Identify the operation, handler, scope or equation under discussion before classifying a Method, declaration or performed Work claim. |
| Chiariello et al., ["Direct Encoding of Declare Constraints in ASP"](https://arxiv.org/abs/2412.10152v1), TPLP 25, 2025; Berti et al., ["OCEL (Object-Centric Event Log) 2.0 Specification"](https://arxiv.org/abs/2403.01975v1), 2024; Bosmans et al., ["Dynamic and Scalable Data Preparation for Object-Centric Process Mining"](https://arxiv.org/abs/2410.00596v1), 2024. | Declare constraints specify admissible traces; the ASP work encodes their semantics directly. OCEL 2.0 defines an event-and-object data model and exchange formats. The data-preparation work separates ingestion, transformation and storage from static log exchange. | Distinguish the constraint, event report or data-preparation activity before accepting a method, work-plan, Work, evidence or gate claim. |
| Tiurin et al., ["Equivalence Hypergraphs: DPO Rewriting for Monoidal E-Graphs"](https://arxiv.org/abs/2406.15882v2), revised 2025-05-20. | Equivalence hypergraphs represent morphisms in a monoidal setting and support categorical rewriting. | Recover the equivalence or composition relation represented by an edge or rewrite. A separate claim about instruction order or performed action keeps its own grounds. |

### C.2.P.DR:End
