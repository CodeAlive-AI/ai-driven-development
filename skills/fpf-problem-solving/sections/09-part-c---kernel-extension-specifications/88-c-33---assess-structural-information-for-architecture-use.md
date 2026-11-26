## C.33 - Assess Structural Information for Architecture Use

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### C.33:1 - Problem frame

Use this pattern when an architect has a description, view, decision record, ADR-like projection, eval report, method handoff, generated relation graph, source model, or realized holon observation that carries or describes selected architecture-relevant structure and needs to know which selected structure is recoverable for the next architecture use.

Use the same pattern when the carrier is a narrative rendering or principle-framework publication for architecture work: the carrier may preserve a problem-to-structure ordering, problem-situation architecture, solution-move architecture, candidate trade-off, decision rationale, or missing-structure cue, but it may also hide selected structures that the next architecture use still needs.

In architecture-mediated rendering, inspect the chain from carrier to architecture description or view, then to the described holon and its architecture-relevant selected structures in context, then to wider selected source structures, because each relation may have captured and lost different structure.

Primary working reader: an architect, architecture reviewer, method steward, or AI-assisted architecture worker who must use one carrier or observation without letting it stand for the whole architecture, the project decision, evidence sufficiency, or realized structure.

Typical entry phrases:

```text
"This view is useful, but what structure does it capture?"
"The ADR says what was decided; which selected structures and hidden losses does it leave behind?"
"The code-agent map found dependencies and invariants; can we rely on them for architecture work?"
"The neural-network architecture review names attention, cache, router, and pruning; what FPF structures are recoverable?"
"The operation observation shows the system diverged; what structure is visible enough to return to synthesis?"
```

The first useful result states which captured structure supports the intended architecture use and which missing structure would limit it. An ordinary explanation can suffice; `StructuralInformationAdequacyNote@Context` is an optional working form. A measurement, assurance conclusion, project decision or architecture description has its own requirements. If an existing account already answers the question for this use, use it directly.

When the structured form helps, include the values needed for the intended use:

```text
StructuralInformationAdequacyNote@Context:
  architectureClaimRef?:
  describedHolonRef:
  architectureConcern:
  intendedArchitectureUse:
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?:
  selectedStructureRefs:
  selectedSourceStructureRefs?:
  sourceDescriptionOrViewRefs?:
  narrativeRenderingRefs?:
  constraintGovernedUnfoldingStructureRef?:
  decisionOrRecordCarrierRefs?:
  realizedStructureObservationRefs?:
  capturedSelectedStructure:
  expectedButUncapturedStructureHypothesis?:
  lostOrHiddenStructure?:
  compressionOrAbstractionMode?:
  observerOrBudgetBoundary?:
  relationObservationClass?:
  typedRelationSemantics?:
  unexploredRegionRefs?:
  sourceLabelRecoveryRef?:
  mathematicalLensUseOutputRef?:
  measurementOrEvalRefs?:
  adequacyEvidenceRefs?:
  admissibleUse:
  nonAdmissibleUse?:
  missingStructureReturnCondition?:
  nextClaimOrRuleRef?:
  receivingClaimKind?:
```

After using C.33, another practitioner can recover the captured structure and the use it supports. State missing structure, excluded uses and the question or test needed to recover it when they affect that use or a plausible continuation. Record a stable reference only when that next use must travel independently.

What C.33 buys in practice: the practitioner can use a partial carrier within its limits. The pattern turns "this diagram, ADR, graph, report, or observation is useful" into a reviewable statement about captured structure, missing structure, missing-structure return, and the next claim or test that needs that structure.

Read the statement, diagram or observation for the decision at hand. Identify the relation it shows and how the source established it. If the decision turns on an omission, find out which relations the source would have shown.

For a reader-relative comparison of structural amount in an expressed account, use `C.2.8` with the reader's preparation, access and budget. State a qualitative comparison directly in the note, or cite an existing measurement or evaluation through `measurementOrEvalRefs?` when that separate result is needed. Then judge whether the captured structure is sufficient for the declared architecture use. The note retains its capture-and-return purpose when it uses a characteristic result.

When the current question concerns architecture, record, lens, reading, decision, authorization, or publication admissibility beyond structure-capture adequacy, use the pattern that defines or tests that object and question. Use C.33 for the captured and missing structural content on which that use depends.

### C.33:2 - Problem

Architecture work depends on partial carriers. Diagrams, views, relation graphs, ADRs, model queries, code-agent probes, neural-network architecture reviews, eval reports, method descriptions, and operation observations can carry enough structure for one action while losing structure needed for another action.

The practical problem is not "is the carrier good?" The problem is: what selected structure can be recovered from it for this declared architecture use, and what missing-structure return is needed before relying on it further?

Common failures:

- a diagram, model, generated graph, ADR, or benchmark trace starts acting as architecture by presentation;
- structural information is confused with a score, entropy value, epiplexity estimate, dashboard reading, or eval result;
- hidden structure becomes invisible when a later candidate, decision, or work method depends on it;
- source labels such as layer, router, expert, cache, memory, block, gate, SSM, pruning, distillation, or architecture search are copied as FPF ontology instead of being recovered through current FPF rules that define the relevant structures and relations;
- partial-observation outputs from code agents or AI tools are treated as internal belief proof, safe-change authority, evidence sufficiency, or release confidence.

### C.33:3 - Forces

| Force | Tension |
| --- | --- |
| Useful carriers vs overread | A small carrier can guide architecture work, but it cannot carry every selected structure, decision, evidence, or work claim. |
| Capture vs loss | Architecture use often depends as much on what was lost or hidden as on what was captured. |
| Cheap first note vs full record | Many cases need one note before a full architecture description, view correspondence record, measurement, or eval result. |
| Observer boundary | Code agents, learned representations, probes, and epiplexity-like lenses expose structure under observation and budget limits. |
| Source label pressure | Domain labels are useful recognition cues. Resolve an ambiguous label only when its meaning changes the selected structure, relation, bearer, characteristic, or next claim; use the rule or test for that claim. |
| Evolution | Captured structural information may no longer be adequate for the declared use when source publication edition, realized structure, environment, bearer, or holon level changes. |

### C.33:4 - Solution

Start with the question the reader must answer or the decision this work must support. Which relation would settle it, and what does this view record about that relation? A confirmed entry can establish that one connection exists within the stated scope. To infer from an empty result that there is no such connection, establish that the source covered the relevant entities, relation and period and that its selection and display would have exposed a match. A filtered view can be complete for that particular inquiry.

Compare the result the recipient needs across the arrangements still consistent with the record. If one action is justified in every case, a request to choose that action can finish. To describe the actual arrangement, list all permitted alternatives or explain why an outcome occurs, preserve the distinctions that change that answer or its grounds. Look for the assignment, rule or observation that can resolve a consequential difference. It may already be in the record.

Work in this order:

1. Name the architecture claim or pre-claim, described holon, architecture concern, intended use, and any ClaimScope or qualification window that changes the adequacy judgment.
2. Identify the selected structures being relied on. If a needed structure is not recoverable, leave the dependent adequacy conclusion open and recover it through `C.30`, `C.30.ASV`, `A.22` or `C.32.P2S` as appropriate. Retain independently supported uses.
3. Name the carrier, selected source structure, description, view, narrative rendering, decision record, eval report, method handoff, generated relation graph, or realized observation being used.
4. State the captured selected structure in relation terms: relations, constraints, invariants, allocations, compositions, variation classes, operations, dynamics refs, or preserved organization.
5. State the expected but uncaptured structure when the next use needs it: hidden placement, data custody, runtime dependency, transformation-flow relation, unexplored region, or missing bearer. State any unresolved source-label semantics or missing confidence class separately when it changes that use.
6. State lost or hidden structure when it limits the intended use or could mislead its reader. Explain the basis of the adequacy conclusion; no invented loss is required when the captured structure suffices.
7. Add the observer and budget conditions needed to interpret a `C.2.8` comparison or a source obtained from a bounded observer, learned representation, probe, relation graph, or epiplexity-style lens. Keep preparation, source access and actual help visible when they can change the recovery claim.
8. Add source label recovery when unresolved terms from a domain practice such as neural-network architectures, software modules, built assets, organizational roles, methods, or work change an architecture claim or its next use.
9. Use the pattern that defines or tests each mathematical-lens, measurement, eval, decision, evidence, assurance, gate, release, method, work, or publication claim when one of those claims is current.
10. Stop when the supported use is clear, with any material limitation and the missing structure needed to resolve it. Apply a further rule or test only when the receiving claim needs it.

CGUS-aware neighbor use: when a carrier, route card, narrative rendering, architecture description, framework publication, or generated relation graph is relied on because it preserves a constraint-governed unfolding structure, C.33 records only what that carrier captures and loses. The selected structure remains `ConstraintGovernedUnfoldingStructure@Context` or a local `U.Structure` block governed by `A.22.CGUS`, `E.18.3`, `C.32.P2S`, `E.23`, or another structure pattern.

When the carrier is a narrative, `A.6.3.NAR` governs only its selected-source carry-through, ordering and connective account, loss, reader use, and source return; it neither selects nor admits the structure.

A `DemonstrativeUnfoldingSlice@Context` may be the `U.Episteme` slice or presentation whose captured structure and lost structure C.33 records; it is not the selected `U.Structure` by itself. C.33 does not admit the CGUS; it tells the practitioner handling the next question what the carrier preserved and where missing selected structure must be inspected or repaired.

### C.33:5 - Archetypal Grounding

C.33 assesses what selected structure a partial carrier captures, what it leaves out, and which practical use it supports. The carrier may be a diagram, decision record, query result, eval report, code-agent map, neural-network architecture review, method handoff, or observation of the realized holon. Apply the rule or test needed by a further claim. Add C.2.1 identity only if that claim must travel independently.

**An integration decision.** An approved decision record says “use event-carried integration with bounded exceptions.” A team can cite the adopted integration style. To decide whether a particular interface qualifies for an exception, the team needs the condition defining the exceptions. If the record gives that condition, the team can apply it to the interface. If the record only says “bounded,” check whether an applicable contract or policy already decides the case. If the applicable rule gives the team discretion, the team can exercise it. If its authority or the applicable rule is still unknown and the answer depends on it, recover that basis or obtain a determination from the decision holder.

To answer which interfaces actually use event-carried integration, inspect evidence about the installed interfaces. A verified as-built inventory attached to the same record can already supply it. Use C.30.AD for the architecture description or C.32.ADR for the decision record. Reopen the decision under C.32.PAD if the rule itself needs to change.

Episteme case. A relation graph records observed dependencies and inferred module roles. Identify the basis for each relation used in the answer and which regions the inquiry covered. The same graph can contain confirmed relations and leave other modules unexamined. Record the consequential gap, including runtime or deployment relations the graph cannot reveal.

The graph can inform `C.34` preservation checks or be assessed under `C.35` for its next architecture use; it does not by itself prove an internal-belief claim, qualify as release evidence, or establish full architecture adequacy.

Neural architecture case. A neural-network architecture review says a model changed attention, SSM block, router, cache placement, pruning mask, and distillation path. C.33 recovers the selected structures and changes being described: dataflow relation, path-selection relation, memory placement, cache placement, and block substitution.

C.33 separately names affected characteristics such as latency, compute, memory, and robustness. Retain clear source-local meanings. Use `C.30.STRAT`, `C.30.TFS-REL`, `C.31`, `C.32`, `C.16` or `C.32.ACE` when a structure, relation or characteristic needed for the current claim remains unresolved.

Architecture narrative case. A team narrative says "we moved from candidate A to candidate B because data custody forced placement P and made latency trade-off T acceptable." C.33 records the structural content and decision context the narrative captures: the move from candidate A to candidate B, data-custody constraint, placement constraint, and trade-off.

The narrative gives the stated reason for the change. To identify who chose B, establish who selected it and, for a choice attributed to the team, why that act counts as the team's decision. To report the grounds they relied on, establish how the explanation relates to that decision. An authoritative account can supply both answers. To use B under a tighter latency limit, establish that its latency meets the new limit under the intended load. An existing validated bound can settle that question. If both A and B remain eligible and the commission calls for choosing between them, compare them under the criteria that decide this choice. To establish which placement was installed, check applicable as-built evidence. Use the evidence already in the account when it settles the question.

The account is sufficient when it establishes what the carrier supports for the intended use. A further claim may need an architecture description, view, evaluation, evidence, decision or authorization under its own rule; C.33 identifies the missing structural contribution and returns that question to the applicable pattern.

### C.33:6 - Bias-Annotation

| Bias | How C.33 counters it |
| --- | --- |
| Carrier completeness bias | Explain captured structure and the use it supports. State lost, hidden or uncaptured structure and excluded uses where they affect reliance. |
| Metric bias | Treat entropy, epiplexity estimate, benchmark score, dashboard value, dependency F1, and invariant F1 as readings only when `C.16` or `C.32.ACE` has opened that claim. |
| Source-label ontology bias | Keep source labels such as layer, router, cache, expert, pruning, distillation, block, DSM cluster, and architecture-search result as source wording. When a label carries an unresolved FPF structure or relation claim, use `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.32`, or another subject pattern to recover the object and predicate for that claim. |
| Observer-belief bias | State observation class, confidence, active-passive gap, budget boundary and unexplored regions where they qualify the use of an agent-produced or probe-produced carrier. A map alone does not establish internal belief, safe change or assurance. |
| Decision-memory bias | Treat ADR-like records as decision descriptions and method expectations. Use `C.32.PAD` or `C.32.ADR` for decision and projection claims, and use C.33 only for what structural content the record carries or loses. |

### C.33:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C33-1` | The account identifies the described holon, architecture concern and intended use, selected structures, carrier or observation, grounds of the adequacy or insufficiency conclusion, and any material ClaimScope or qualification window. |
| `CC-C33-2` | Captured selected structure is stated as relations, constraints, invariants, allocations, compositions, variation classes, operations, dynamics refs, or preserved organization. |
| `CC-C33-3` | The account identifies what an omission leaves open for the intended use. A conclusion drawn from the absence of an entry identifies why a matching entry would have been recorded and visible. |
| `CC-C33-4` | Observer, access or budget conditions are stated when they limit recovery or the use of an agent-produced, learned, probed or source-derived carrier; a formal epiplexity-style estimate retains its model conditions. |
| `CC-C33-5` | Each current mathematical-lens, measurement, eval, decision, evidence, assurance, gate, release, method, work, or publication claim uses the pattern that defines or tests it. |
| `CC-C33-6` | The supported use and any material limits are clear. A required source return names the missing structure and the question, rule or test needed to obtain it. |

### C.33:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Diagram as complete architecture | The diagram may show modules or links while hiding placement, runtime dependency, control authority, evidence structure, bearer constraints, or data custody. | Write the C.33 note from the diagram: captured structure, missing structure, lost relation semantics, admissible use, and the condition that reopens the next dependent claim or question. Add its predicate and assertion identity only when that identity must travel independently. |
| ADR as realized structure proof | A decision record can carry decision memory and method expectation without showing what was built or how it behaves. | Use `C.32.PAD` for the project decision claim and `C.32.ADR` for its record projection; use C.33 only for the structural content and loss carried by the record; state realization claims using the architecture or evidence predicate and cite the pattern that defines or tests it when that reference is needed. |
| Narrative as complete architecture | A narrative can preserve a route through selected structures while hiding placement, alternatives, measurements, interfaces, or realized structure. | Use `A.6.3.NAR` for the structure-to-narrative rendering relation and C.33 for captured and lost selected structure before architecture reuse. |
| Code-agent graph as safe-change authority | A graph can expose observed and inferred relations while leaving unknown regions and hidden invariants. | Add observation class, confidence, unexplored regions, and non-admissible use. Use the patterns that define the safe-change, assurance, gate, and release checks when those claims are current. |
| Metric as structural adequacy | A score, entropy value, epiplexity estimate, benchmark trace, or dependency F1 supports only the conclusion established by its calculation, measurement or evaluation conditions. | Retain the mathematical model and correspondence needed by a computed value; use `C.16` when measurement is claimed, `C.25` for a current Q-bundle claim, and `C.32.ACE` for architecture evaluation. Use `C.29` for an unresolved mathematical-representation choice, transfer, or reliance question. |
| Neural label import | Terms such as attention, SSM, router, expert, cache, pruning, distillation, and NAS can hide several structure kinds and characteristics. | Recover the selected structure kind, relation, bearer, affected characteristic, preserved structure, and lost structure needed by the architecture claim, and identify the next claim plus the rule or test it needs before relying on the label for that use. |

### C.33:9 - Consequences

Positive consequences:

- A partial carrier becomes usable without becoming authoritative. The architect can take the structure that is recoverable and stop before overreading the carrier.
- Missing-structure return becomes local and reviewable: the note says which missing structure requires C.30, C.30.ASV, C.32.P2S, C.32, PAD, ADR, C.29, C.16, ACE, evidence, assurance, or work checks before the next use.
- AI-produced maps and maps derived from named source publications, source models, or source codebases become safer architecture inputs because observation class, confidence, unexplored regions, and budget boundary are visible.
- Neural-network and code-architecture source labels become usable without importing those labels as FPF ontology.

Costs and trade-offs:

- The assessment takes attention and may need a retained note. Its cost is justified when a structural uncertainty could change the next use; an already adequate account can be reused.
- The note can be too weak for decision, evidence, assurance, eval, release, or realized-structure claims. In those cases C.33 should stop early and use the pattern that defines or tests the current claim.
- A familiar diagram or ADR may leave structure needed for the intended use unestablished. Recover that structure before relying on the dependent conclusion.

### C.33:10 - Rationale

A partial carrier can preserve the relations needed for one architecture use while omitting those needed for another. Assessing its captured structure against the intended use makes that boundary explicit and identifies any missing structural contribution. A description, measurement or evaluation remains available under its own requirements.

This split keeps P2S as the whole architecturing spine and C.32 as the pattern that describes candidate synthesis. C.33 does not synthesize architecture and does not decide the project architecture. It explains what the carrier contributes and what the next use still needs.

The source choices explain the fields. Epiplexity supplies a computational model for observer-bounded structural information; `C.2.8` defines the general characteristic consumed here when the source is an expressed episteme. Captured amount informs the architecture-use adequacy judgment without replacing it. Multi-relational structural entropy motivates relation-kind awareness but not adequacy by number. Sapunov and ToCS motivate partial observability, active-passive gap, invariant fields, confidence, and unexplored regions. GonzoML motivates richer neural architecture operation language without making those labels FPF ontology.

### C.33:11 - SoTA-Echoing

| Source or practice line | Use of the contribution | Contribution to the assessment | Boundary of use |
| --- | --- | --- | --- |
| [OMG SysML 2.0, Language, Views and Viewpoints](https://www.omg.org/spec/SysML/2.0/Language/PDF) | Use the view’s selection of exposed elements and the conditions that filter them. | Tells a reader where to check whether the required model element would appear. | A complete view of selected model elements supports a claim about an installation when the interpretation and as-built evidence also support that claim. |
| Finzi et al., `From Entropy to Epiplexity`, arXiv:2601.03220 | Adapt bounded-observer structural information through the characteristic in `C.2.8`. | Connects observer and budget conditions and captured/lost-structure comparison to the reader's preparation and access. A formal estimate retains its specified source/model correspondence and model conditions; use `C.29` for a separate unresolved choice, transfer, or reliance question. | The amount characterizes extraction from the expressed source under observer conditions. The described architecture and its adequacy for the next use retain their own questions and evidence. Reopen the note when observer conditions, source publication edition, or downstream use changes. |
| Cao et al., `Multi-Relational Structural Entropy`, arXiv:2405.07096 | Adapt relation heterogeneity and graph structural-information pressure. | Distinguishes relation kinds when interpreting a graph and its measurements or evaluation. | For a graph entropy value, use `C.16` when measurement is claimed and `C.32.ACE` when architecture evaluation is current; it does not establish architecture adequacy. |
| Sapunov, `Theory of Code Space`, and ToCS code-agent architecture-map practice | Adopt the partial-observability and belief-probing lessons; adapt them beyond software code agents. | Distinguishes observation class, confidence, active-passive gap and unexplored regions; an invariant claim returns to the relevant architecture source map or defining rule. | A probe, JSON output, dependency F1, invariant F1, active-passive gap, or benchmark score is not architecture adequacy, evidence sufficiency, safe-change authority, assurance, gate passage, or release authority. Reopen when the probed codebase, architecture source map, or observation budget changes. |
| GonzoML neural-network architecture intake | Adapt practitioner operation labels into FPF recovery steps. | Supports interpretation of neural source labels for block substitution, dataflow change, routing, gating, cache, memory, pruning, distillation, NAS, ablation, and affected characteristics. | Use clear source-local meanings directly. Resolve a structure, relation, bearer, characteristic or loss when it remains unclear and changes the architecture claim; apply any rule required by that claim. |

### C.33:12 - Relations

- **Builds on:** `A.22`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.32.P2S`, and `C.32`.
- **Uses:** `C.2.8` for extractable structural amount in an expressed episteme; `C.29` when choosing, transferring, or relying on a mathematical representation remains unresolved; `C.16`, `C.25`, and `C.32.ACE` when a claim about captured or lost structure is recorded as a measurement, Q-bundle slot, criterion, or eval reading.
- **Coordinates with:** `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `A.6.3.NAR`, `C.31`, `C.31.ASAP`, `C.32.PAD`, `C.32.ADR`, `G.5`, `C.18`, `C.19`, `E.18`, `F.9`, and `F.15`.
- **Boundary:** C.33 governs structure-capture adequacy and missing-structure return for a declared architecture use. It does not ground architecture, select candidates, decide projects, publish records, measure values, supply evidence or assurance, authorize work, or claim realization.

### C.33:End
