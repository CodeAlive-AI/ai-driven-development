## C.33 - Structural Information Adequacy for Architecture Capture and Source Return

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### C.33:1 - Problem frame

Use this pattern when an architect has a structure-bearing description, view, decision record, ADR-like projection, eval report, method handoff, generated relation graph, source model, or realized holon observation and needs to know which selected architecture-relevant structure is actually recoverable for the next architecture use.

Primary working reader: an architect, architecture reviewer, method owner, or AI-assisted architecture worker who must use one carrier or observation without letting it stand for the whole architecture, the project decision, evidence sufficiency, or realized structure.

Typical entry phrases:

```text
"This view is useful, but what structure does it actually capture?"
"The ADR says what was decided; which selected structures and hidden losses does it leave behind?"
"The code-agent map found dependencies and invariants; can we rely on them for architecture work?"
"The neural-network architecture review names attention, cache, router, and pruning; what FPF structures are recoverable?"
"The operation observation shows the real system diverged; what actual structure is visible enough to return to synthesis?"
```

The first useful output is `StructuralInformationAdequacyNote@Context`. It is a project-side adequacy note for one declared architecture use. It is not a C.16 characteristic, not a measurement, not an evidence record, not an assurance result, not a project decision, and not an architecture description by itself.

For the first pass, fill only the fields that prevent the next wrong use:

```text
StructuralInformationAdequacyNote@Context:
  architectureClaimRef?:
  describedHolonRef:
  boundedContextRef:
  selectedStructureRefs:
  sourceStructureRefs?:
  sourceDescriptionOrViewRefs?:
  decisionOrRecordCarrierRefs?:
  realizedStructureObservationRefs?:
  capturedSelectedStructure:
  expectedButUncapturedStructureHypothesis?:
  lostOrHiddenStructure:
  compressionOrAbstractionMode?:
  observerOrBudgetBoundary?:
  sourceObservationClass?:
  typedRelationSemantics?:
  unexploredRegionRefs?:
  sourceLabelRecoveryRef?:
  mathematicalLensUseOutputRef?:
  measurementOrEvalRefs?:
  admissibleUse:
  nonAdmissibleUse:
  sourceReturnCondition:
  receivingOwnerOrPatternRef:
  receivingClaimKind:
```

Adoption test: after using C.33, another practitioner can tell what selected structure is captured, what structure is expected but not captured, what is lost or hidden, what use is admissible, which non-admissible uses are blocked, and which owner receives the next claim.

What C.33 buys in practice: the practitioner can use a partial carrier without pretending it is complete. The pattern turns "this diagram, ADR, graph, report, or observation is useful" into a reviewable statement about captured structure, missing structure, source return, and next owner.

Ordinary working move: underline the carrier sentence, diagram, graph edge set, or observation being relied on; write what selected structure it captures; write what it leaves out; then name the use that remains admissible.

Not this pattern when the current question asks whether the architecture, record, lens, reading, decision, authorization, or publication is admissible. Use the owner of that question first. Return to C.33 only when that owner relies on a carrier whose captured structural content and missing structural content must be made explicit.

### C.33:2 - Problem

Architecture work depends on partial carriers. Diagrams, views, relation graphs, ADRs, model queries, code-agent probes, neural-network architecture reviews, eval reports, method descriptions, and operation observations can carry enough structure for one action while losing structure needed for another action.

The practical problem is not "is the carrier good?" The problem is: what selected structure can be recovered from it for this declared architecture use, and what source return is needed before relying on it further?

Without C.33:

- a diagram, model, generated graph, ADR, or benchmark trace starts acting as architecture by presentation;
- structural information is confused with a score, entropy value, epiplexity estimate, dashboard reading, or eval result;
- hidden structure becomes invisible exactly when a later candidate, decision, or work method depends on it;
- source labels such as layer, router, expert, cache, memory, block, gate, SSM, pruning, distillation, or architecture search are copied as FPF ontology instead of being recovered through current FPF owners;
- partial-observation outputs from code agents or AI tools are treated as internal belief proof, safe-change authority, evidence sufficiency, or release confidence.

### C.33:3 - Forces

| Force | Tension |
| --- | --- |
| Useful carriers vs overread | A small carrier can guide architecture work, but it cannot carry every selected structure, decision, evidence, or work claim. |
| Capture vs loss | Architecture use often depends as much on what was lost or hidden as on what was captured. |
| Cheap first note vs full record | Many cases need one note before a full architecture description, view correspondence record, measurement, or eval result. |
| Observer boundary | Code agents, learned representations, probes, and epiplexity-like lenses expose structure under observation and budget limits. |
| Source label pressure | Domain labels are useful recognition material but must be recovered into selected structure, relation, bearer, characteristic, and receiving owner. |
| Evolution | The captured structure can decay when source edition, realized structure, environment, bearer, or holon level changes. |

### C.33:4 - Solution

Create one `StructuralInformationAdequacyNote@Context` for the declared architecture use.

Read the note as a small source-return tool, not as a new documentation format. Its didactic question is simple: "What can I safely take from this carrier, what must I not take, and where do I go if the missing structure matters?"

Work in this order:

1. Name the architecture claim or pre-claim described holon and bounded context.
2. Name the selected structure refs or structure kinds being relied on. If they are not recoverable, stop and return to `C.30`, `C.30.ASV`, `A.22`, or `C.32.P2S`.
3. Name the carrier, source structure, description, view, decision record, eval report, method handoff, generated relation graph, or realized observation being used.
4. State the captured selected structure in relation terms: relations, constraints, invariants, allocations, compositions, variation classes, operations, dynamics refs, or preserved organization.
5. State the expected but uncaptured structure when the next use needs it: hidden placement, data custody, runtime dependency, transformation-flow relation, source label semantics, confidence class, unexplored region, or missing bearer.
6. State lost or hidden structure. If no loss is claimed, justify why the carrier is adequate for the declared use rather than for all uses.
7. Add observer or budget boundary when the carrier comes from a bounded observer, learned representation, probe, relation graph, or epiplexity-style lens.
8. Add source label recovery when source terms come from a domain practice such as neural-network architectures, software modules, built assets, organizational roles, methods, or work.
9. Route mathematical-lens, measurement, eval, decision, evidence, assurance, gate, release, method, work, and publication claims to their direct owners.
10. Stop when admissible use, non-admissible use, source-return condition, receiving owner, and receiving claim kind are clear.

### C.33:5 - Archetypal Grounding

Tell: C.33 is the pattern for using a partial structure-bearing carrier without letting that carrier stand for the whole architecture. The carrier may be a diagram, decision record, query result, eval report, code-agent map, neural-network architecture review, method handoff, or observation of the realized holon. The grounding question is not whether the carrier is impressive. The grounding question is what selected structure it captures, what it leaves out, and which owner receives the next claim.

Show - system case. An ADR-like record says "use event-carried integration with bounded exception." C.33 records that the carrier captures the selected integration style, exception boundary, and method expectation. It does not capture lower-level placement constraints, schema evolution burden, runtime data custody, or deployment topology. The admissible use is decision memory and method handoff; the non-admissible use is proof that the realized modules have the intended architecture. Source return goes to `C.32.PAD`, `C.32.ADR`, `C.30.AD`, and later `C.32` synthesis if actual structure diverges.

Show - episteme case. A code-agent relation graph finds imports, call edges, inferred module roles, and candidate invariants. C.33 records source observation class `observed | inferred | unknownRegionPresent`, typed relation semantics, confidence class, active-passive gap when present, unexplored regions, and lost runtime or deployment structure. The graph can seed `C.34` preservation checks or `C.35` discovery, but it is not internal belief proof, release evidence, or full architecture adequacy.

Show - neural architecture case. A neural-network architecture review says a model changed attention, SSM block, router, cache placement, pruning mask, and distillation path. C.33 recovers which selected structures are being described: dataflow relation, path-selection relation, memory placement, cache placement, block substitution, and affected characteristics such as latency, compute, memory, and robustness. Source labels remain source labels until recovered through `C.30.STRAT`, `C.30.TFS-REL`, `C.31`, `C.32`, `C.16`, or `C.32.ACE` as applicable.

The small working form is enough when it blocks a wrong next use. It is not enough when the next claim needs an architecture description, structural view, decision repair, eval program, evidence record, assurance case, gate, release, or work authorization. In those cases C.33 produces the source-return condition and then exits.

### C.33:6 - Bias-Annotation

| Bias | How C.33 counters it |
| --- | --- |
| Carrier completeness bias | Require captured selected structure, expected but uncaptured structure, lost or hidden structure, admissible use, and non-admissible use before relying on the carrier. |
| Metric bias | Treat entropy, epiplexity estimate, benchmark score, dashboard value, dependency F1, and invariant F1 as readings only when `C.16` or `C.32.ACE` has opened that claim. |
| Source-label ontology bias | Keep source labels such as layer, router, cache, expert, pruning, distillation, block, DSM cluster, and architecture-search result as labels until `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.32`, or another owner recovers the selected structure and relation. |
| Observer-belief bias | Record observation class, confidence, active-passive gap, budget boundary, and unexplored regions for agent-produced or probe-produced carriers. Do not infer internal belief, safe change, or assurance from a map. |
| Decision-memory bias | Treat ADR-like records as decision descriptions and method expectations. Use `C.32.PAD` or `C.32.ADR` for decision and projection claims, and use C.33 only for what structural content the record carries or loses. |

### C.33:7 - Conformance checklist

| Check | Pass condition |
| --- | --- |
| `CC-C33-1` | The note names described holon, bounded context, selected structure refs or structure kinds, and the carrier or observation being used. |
| `CC-C33-2` | Captured selected structure is stated as relations, constraints, invariants, allocations, compositions, variation classes, operations, dynamics refs, or preserved organization. |
| `CC-C33-3` | Expected but uncaptured structure and lost or hidden structure are stated when the next use depends on them. |
| `CC-C33-4` | Observer or budget boundary is present for agent-produced, learned, probed, source-derived, or epiplexity-style carriers. |
| `CC-C33-5` | Mathematical-lens, measurement, eval, decision, evidence, assurance, gate, release, method, work, and publication claims are routed to their owners. |
| `CC-C33-6` | Admissible use, non-admissible use, source-return condition, receiving owner, and receiving claim kind are named. |

### C.33:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair move |
| --- | --- | --- |
| Diagram as complete architecture | The diagram may show modules or links while hiding placement, runtime dependency, control authority, evidence structure, bearer constraints, or data custody. | Write the C.33 note from the diagram: captured structure, missing structure, lost relation semantics, admissible use, and source-return owner. |
| ADR as realized structure proof | A decision record can carry decision memory and method expectation without showing what was built or how it behaves. | Use `C.32.PAD` or `C.32.ADR` for the decision claim; use C.33 only for the structural content and loss carried by the record; send realization claims to the architecture or evidence owner. |
| Code-agent graph as safe-change authority | A graph can expose observed and inferred relations while leaving unknown regions and hidden invariants. | Add observation class, confidence, unexplored regions, and non-admissible use. Route safe-change, assurance, gate, and release claims to their owners. |
| Metric as structural adequacy | A score, entropy value, epiplexity estimate, benchmark trace, or dependency F1 is a reading only under the right measurement or eval owner. | Keep it as lens or reading context until `C.16`, `C.25`, or `C.32.ACE` defines what is measured and how it may be used. |
| Neural label import | Terms such as attention, SSM, router, expert, cache, pruning, distillation, and NAS can hide several structure kinds and characteristics. | Recover the selected structure kind, relation, bearer, affected characteristic, preserved structure, lost structure, and receiving owner before using the label in architecture work. |

### C.33:9 - Consequences

Positive consequences:

- A partial carrier becomes usable without becoming authoritative. The architect can take exactly the structure that is recoverable and stop before overreading the carrier.
- Source return becomes local and reviewable: the note says which missing structure must return to C.30, C.30.ASV, C.32.P2S, C.32, PAD, ADR, C.29, C.16, ACE, evidence, assurance, or work owners.
- AI-produced and source-derived maps become safer architecture inputs because observation class, confidence, unexplored regions, and budget boundary are visible.
- Neural-network and code-architecture source language becomes usable without importing source labels as FPF ontology.

Costs and trade-offs:

- C.33 adds one small note before some architecture work. The cost is justified only when a next use might overread a carrier.
- The note can be too weak for decision, evidence, assurance, eval, release, or realized-structure claims. In those cases C.33 should stop early and route to the direct owner.
- A team may discover that a familiar diagram or ADR is insufficient for the intended use. That is not a failure of C.33; it is the source-return condition doing its job.

### C.33:10 - Rationale

Architecture work often starts from carriers that are neither useless nor complete. A mature pattern must preserve both facts. If C.33 only says "do not confuse the carrier with architecture," it becomes a negative catalogue. If it treats every carrier as an architecture description or measurement, it duplicates C.30, C.16, and C.32.ACE. The chosen solution is a small adequacy note whose center is captured selected structure, lost structure, admissible use, and source return.

This split keeps P2S as the whole architecturing spine and C.32 as candidate synthesis owner. C.33 does not synthesize architecture and does not decide the project architecture. It gives the next owner a typed account of what a carrier contributes and what must still be recovered.

The source choices explain the fields. Epiplexity motivates observer-bounded structural information but not a universal architecture metric. Multi-relational structural entropy motivates relation-kind awareness but not adequacy by number. Sapunov and ToCS motivate partial observability, active-passive gap, invariant fields, confidence, and unexplored regions. GonzoML motivates richer neural architecture operation language without making those labels FPF ontology.

### C.33:11 - SoTA-Echoing

| Source or practice line | Adopt, adapt, or reject | Concrete C.33 locus changed | Boundary and currentness |
| --- | --- | --- | --- |
| Finzi et al., `From Entropy to Epiplexity`, arXiv:2601.03220 | Adapt observer-bounded structural information. | Adds `observerOrBudgetBoundary?`, strengthens hidden-structure and compression guidance, and supports the warning that recoverable structure is observer-bound. | Epiplexity is not an architecture characteristic, proof, selector, evidence, assurance, decision, or realized-structure observation by itself. Reopen the note when observer budget, source edition, or downstream use changes. |
| Cao et al., `Multi-Relational Structural Entropy`, arXiv:2405.07096 | Adapt relation heterogeneity and graph structural-information pressure. | Strengthens `typedRelationSemantics?`, relation-kind recovery, and metric-owner routing. | A graph entropy value routes to `C.16` and `C.32.ACE` when measured or evaluated; it does not establish architecture adequacy. |
| Sapunov, `Theory of Code Space`, and ToCS code-agent architecture-map practice | Adopt the partial-observability and belief-probing lessons; adapt them beyond software code agents. | Adds `sourceObservationClass?`, confidence class, active-passive gap, unexplored regions, invariant source return, and non-overread of JSON probes and benchmark scores. | A probe, JSON output, dependency F1, invariant F1, active-passive gap, or benchmark score is not architecture adequacy, evidence sufficiency, safe-change authority, assurance, gate passage, or release authority. Reopen when the probed codebase, source map, or observation budget changes. |
| GonzoML neural-network architecture intake | Adapt practitioner operation labels into FPF recovery steps. | Adds neural source-label recovery for block substitution, dataflow change, routing, gating, cache, memory, pruning, distillation, NAS, ablation, and affected characteristics. | Source labels and results do not become FPF ontology or adequacy. Recover selected structure, relation, bearer, affected characteristic, loss, and receiving owner before architecture use. |

C.33 deliberately rejects a popular shortcut: "the richest available diagram, map, score, or model summary is the architecture content." The better practice is to ask what the carrier captures for one declared use and what it cannot support. That is why SoTA rows must change fields, stop conditions, or owner routing rather than only supplying lineage.

### C.33:12 - Relations

- **Builds on:** `A.22`, `C.30`, `C.30.AD`, `C.30.ASV`, `C.32.P2S`, and `C.32`.
- **Uses:** `C.29` when a mathematical lens exposes or compresses structure; `C.16`, `C.25`, and `C.32.ACE` when a claim about captured or lost structure is recorded as a measurement, Q-bundle slot, criterion, or eval reading.
- **Coordinates with:** `C.30.STRAT`, `C.30.TFS-REL`, `A.6.M`, `C.31`, `C.31.ASAP`, `C.32.PAD`, `C.32.ADR`, `G.5`, `C.18`, `C.19`, `E.18`, `F.9`, and `F.15`.
- **Boundary:** C.33 governs structure-capture adequacy and source return for a declared architecture use. It does not ground architecture, select candidates, decide projects, publish records, measure values, supply evidence or assurance, authorize work, or claim realization.

### C.33:End

