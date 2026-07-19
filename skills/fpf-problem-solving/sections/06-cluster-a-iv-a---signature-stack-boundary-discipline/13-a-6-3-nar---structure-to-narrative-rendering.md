## A.6.3.NAR - Structure-to-Narrative Rendering

> **Type:** Specialization pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

### A.6.3.NAR:1 - Problem frame

Use this pattern when selected source structure must become a sequential narrative rendering for a declared reader or listener use. Typical cases include a scientific mechanism turned into a paper section, an architecture trade-off turned into a team explanation, a conceptual graph turned into a lesson sequence, or an event graph turned into a generated story draft.

Primary `EntityOfConcern`: one `A.6.3` epistemic-viewing relation in which an admitted source basis, such as an episteme, publication, model, graph, architecture view, evidence set, situation record, event stream, proof field, or `G.2` source pack, is rendered as a narrative path while the same EntityOfConcern is preserved or a declared correspondence is used.

Plain starting vocabulary:

| Term | Plain meaning |
| --- | --- |
| `source basis` | The admitted source object or record used for rendering: episteme, publication, graph, model, architecture view, evidence set, situation record, event stream, proof field, or `G.2` source pack. |
| `selected source structures` | The relations, constraints, events, mechanisms, dependencies, conflicts, alternatives, or changes that must remain recoverable. |
| `source-structure selection rationale` | The reason these structures, rather than other possible structures, are needed for the declared reader or listener use. |
| `source temporal posture` | Whether the selected source structure or admitted source basis concerns retrospective or reverse-engineered actual structure or event record, live unfolding, prospective planned structure, prospective fictional structure or canon, or a mixed case. |
| `rendering mediation mode` | Whether the narrative rendering is direct source-structure narrativization or architecture-mediated narrativization through architecture understanding, description, view, viewpoint, decision, or telemetry. |
| `narrating or rendering worker` | The person, team, or tool-mediated role arranging the selected source structures into the narrative path. This role does not own authority over the source basis by default. |
| `reader or listener role` | The role and use whose interests constrain source-basis selection, ordering, viewpoint, recoverability, engagement, and source-basis return. This is narrower than a generic audience. |
| `reader-interest or use hypothesis` | The explicit guess about what the reader or listener needs to do with the narrative and what problem the selected structures help solve. |
| `narrative rendering` | The receiving sequential account that makes the source usable by a reader or listener. |
| `ordering rationale` | The reason this sequence is used: event order, causal order, discovery order, didactic order, tension order, traversal rule, or another declared rule. |
| `source-basis return condition` | The condition that names the exact source basis or receiving governing pattern to return to when the narrative no longer carries the needed selected structure for the declared use. |
| `epiplexity question` | The question "how much selected source structure did this rendering pull into an inspectable description for this observer and use?" NAR supplies the relation fields; structural-information and evaluation patterns answer the value claim. |

First useful move: write one compact `StructureToNarrativeRenderingCase@Context` for the case. Name the source basis, selected source structures, source-structure selection rationale, source temporal posture, rendering mediation mode, narrating or rendering worker, reader-interest or use hypothesis, receiving narrative rendering, intended reader or listener role and use, ordering rationale, preserved structure, foregrounded structure, coarsened or lost structure, recoverability, admissible use, non-admissible use, and source-basis or governing-pattern return condition.

What goes wrong if missed: a useful story becomes a substitute for the selected source structure. Readers remember a sequence, example, protagonist, conflict, or conclusion, but cannot reconstruct the relations inside the selected source structure that made the narrative worth using.

What this buys: the narrative can help human use without pretending to be neutral compression, proof, authority, ethics, evidence, architecture, or the selected source structure, source basis, or source episteme itself.

Ordinary use: for low-reliance teaching, orientation, or internal explanation, one compact case note near the narrative is enough. It must still state what the narrative preserves, what it leaves behind, and when to return to the source.

Reliance-facing use: use the full field spine when the narrative will guide architecture work, design decisions, policy communication, safety work, generated-output admission, external teaching, or cross-context reuse.

Not this pattern when the current change is only same-regime wording (`A.6.3.CR`), only representation-scheme transition (`A.6.3.RT`), only coarsened narrower-use rendering (`A.6.3.CSC`), explanation-use adequacy on an existing MVPK face (`E.17.EFP`), changed EntityOfConcern (`A.6.4`), carrier export or serialization, generated-output admission (`C.35`), evidence, assurance, ethics, publication, or work authorization. Use the direct governing pattern first and return here only when the structure-to-sequence narrative relation is live.

### A.6.3.NAR:2 - Problem

Projects often need narrative because selected source structures are too tangled for a reader to use directly. A mechanism, architecture, model, evidence set, or event graph may need a beginning, order, tension, action, update point, or learning path before humans can follow it.

Without `A.6.3.NAR`:

1. narrative is treated as style polish after the real work is done;
2. narrative is treated as a lossy summary even when sequence-making is the main representational move;
3. selected source structure, order, event model, and lost relations disappear behind fluent prose;
4. engagement is allowed to raise confidence, authority, ethical permission, or policy force without a direct governing pattern;
5. generated narrative output is trusted because it is coherent or dramatic;
6. teaching material can be smuggled into pattern bodies instead of being kept as a separate test-run publication carrier or ordinary publication carrier.

### A.6.3.NAR:3 - Forces

| Force | Tension |
| --- | --- |
| Selected source structure vs human sequence | A reader often needs an ordered path, while the selected source structure may be a graph, mechanism, option set, architecture, or evidence field rather than a line. |
| Engagement vs truth boundary | Tension, viewpoint, protagonist, and pacing can help attention, but they do not widen truth, evidence, authority, ethical permission, or admissible downstream use. |
| Compression vs recoverability | A narrative foregrounds some structure and leaves other structure behind. The useful loss must be visible. |
| Event comprehension vs non-event structure | Some selected source structures involve events and actions; others involve dependencies, constraints, alternatives, or architectures. The pattern must support both without forcing a fiction model. |
| Domain richness vs Core economy | Narratology, storycraft, cognitive narrative research, science communication, NLG, and teaching practice are rich, but most of their vocabulary belongs in domain narrative source packs or local and domain frameworks rather than FPF Core. |

### A.6.3.NAR:4 - Solution

Create a `StructureToNarrativeRenderingCase@Context` for the narrative relation.

Use this compact form. Fill only fields that change the admissible use or block a likely overread.

```text
StructureToNarrativeRenderingCase@Context:
  sourceBasisRef:
  selectedSourceStructureRefs:
  sourceStructureSelectionRationale:
  sourceTemporalPosture:
  renderingMediationMode: direct-source-structure | architecture-mediated | mixed
  architectureMediationRef?:
  sourceStructureGoverningPatternRef?:
  narratingOrRenderingWorkerRef?:
  readerOrListenerRoleRefs:
  readerInterestOrUseHypothesis:
  preservedEntityOfConcernRef?:
  declaredCorrespondenceRef?:
  receivingNarrativeRenderingRef:
  intendedReaderOrListenerUse:
  orderingRationaleOrTraversalRule:
  preservedStructure:
  foregroundedStructure:
  coarsenedOrLostStructure:
  epiplexityOrStructuralInformationRef?:
  recoverabilityClassOrSourceBasisReturnCondition:
  eventModelSupport?:
  engagementOrMotivationClaim?:
  admissibleUse:
  nonAdmissibleDownstreamUse:
  neighboringPatternExits:
```

Use this unfolding block when the selected source structure must be carried into a reader-facing sequence with explicit loss and return.

```text
NarrativeUnfoldingStructureBlock:
  structureBeingRenderedRef:
  unfoldingStructureBeingRenderedRef?:
  narrativeOrderingStructureRef:
  readerActSequenceHypothesis?:
  narrativeRenderingRef?:
  preservedStructure:
  lostOrCoarsenedStructure:
  narrativeStructureUseReturnCondition:
  blockedOverread: narrative sequence is not the ontology of the input structure being rendered, proof, decision, work sequence, or gate
```

`structureBeingRenderedRef` names the input structure under concern. `narrativeOrderingStructureRef` names the ordering rule or sequence structure used for reader understanding. `narrativeRenderingRef` names the episteme or publication unit that carries the narrative. These are different positions. A good narrative may preserve the right structure for a reader while deliberately coarsening, reordering, or omitting other structure; the block makes that loss inspectable.

`NarrativeUnfoldingStructureBlock` is a local `A.22.CGUS` `U.Structure` specialization block governed here for narrative-rendering use. It is not a root U-kind, not a workflow, not a proof, not an architecture decision, not evidence, and not publication permission. `A.6.3.NAR` governs the source-structure-to-sequence relation; generated-output admission, source-pack claims, architecture-description claims, ethics, evidence, assurance, rights, publication, and work claims leave to their direct governing patterns.

Use `unfoldingStructureBeingRenderedRef` only when the source basis itself is a constraint-governed unfolding structure. Otherwise NAR may still order a selected source structure, architecture description, event stream, proof dependency field, option field, or source pack without claiming CGUS.

Work in this order:

1. Name the source basis, the selected source structure that must survive, and its temporal posture: retrospective or reverse-engineered actual, live unfolding, prospective planned, prospective fictional, or mixed.
2. State the source-structure selection rationale and the reader-interest or use hypothesis. If these are only implicit in a draft, treat the draft as a candidate carrier until the rationale is reconstructed.
3. Name the rendering mediation mode. Use `direct-source-structure` for a situation, event stream, proof field, canon, or source pack rendered directly; use `architecture-mediated` when architecture understanding, architecture description, architecture view, architecture viewpoint, decision record, candidate structure, or telemetry is the mediating source basis.
4. Name the narrating or rendering worker, the receiving narrative rendering, and the intended reader or listener role and use.
5. State whether the same EntityOfConcern is preserved or whether a `C.34` correspondence is needed.
6. Choose the ordering rationale: event order, causal order, discovery order, didactic order, tension order, graph traversal, architecture-decision sequence, live-commentary sequence, prospective-scenario sequence, source-publication order, or another declared rule.
7. State preserved structure, foregrounded structure, coarsened or lost structure, and recoverability.
8. If the live question is how much structure was pulled into the narrative, create or cite the structural-information or epiplexity note instead of answering with fluency. For architecture-relevant uses this routes to `C.33`; for declared narrative-quality evaluation this routes to the domain narrative evaluation pattern, `A.19.ECS`, and `C.16` as applicable.
9. Add event-model support when the narrative asks the reader to understand events, actions, mechanisms, goals, obstacles, state updates, or change.
10. Add engagement or motivation only as a declared-use claim. If persuasion, harm, affected parties, policy influence, bias, value conflict, or ethical assurance is live, route the claim to `D.1` through `D.5`, `A.10`, or `B.3` as applicable.
11. Close with admissible use, non-admissible downstream use, source-basis or governing-pattern return condition, and neighboring-pattern exits.

#### A.6.3.NAR:4.1 - Ordinary and claim-bearing cases

Ordinary narrative renderings can stay lightweight. An internal explanation, teaching example, or orientation story usually needs only a compact note: source basis, selected structure, sequence rule, visible loss, and source-basis return condition.

Claim-bearing cases need the fuller record. A case is claim-bearing when the narrative will be used for design, architecture, policy, safety, public science communication, generated-output admission, cross-context reuse, assurance-facing training, or a disputed interpretation.

#### A.6.3.NAR:4.2 - Same-entity and correspondence-mediated profiles

Use the same-entity profile when the receiving narrative is still a rendering of the same EntityOfConcern and the source tether remains visible.

Use the correspondence-mediated profile when the narrative is produced from a source model, graph, architecture view, or generated relation set that corresponds to the source but is not the same representation. In that case, create or cite the `C.34` correspondence record before the narrative is treated as same enough for a downstream use.

#### A.6.3.NAR:4.2.1 - Direct and architecture-mediated routes

Use the direct source-structure mediation mode when the narrative worker renders a situation, event stream, domain model, proof dependency field, evidence set, fictional canon, or source pack directly into a narrative path. View and viewpoint discipline may still help, but the central governing relation is the NAR relation plus any domain-specific narrative or evaluation pattern, not the architecture line.

Direct does not mean implicit. If the selected source structures, selection rationale, reader-interest hypothesis, ordering rationale, and loss account are left inside the writer's intuition, an LLM prompt, or a finished story, the output is only a candidate carrier or candidate prose, not an admitted narrative rendering. It can inspire a later NAR case, but reliance-facing use requires reconstructing and checking the missing selection and loss record.

Use the architecture-mediated mode when the selected source structure is actual or possible holon structure that has been understood through architecture work: reverse-engineering an existing holon, comparing candidate future structures, using architecture descriptions and views, applying architecture decisions, or checking telemetry after realization. In this mode the return chain is narrative rendering to architecture description or view, then to architecture as selected structures in context, then to wider holon or source-basis structures when those are current. Each relation can select, coarsen, abstract, omit, or order structure, and each relation needs its own source-basis, description, view, architecture-decision, or governing-pattern return condition when the loss becomes live. `C.33`, `C.34`, `C.32.*`, architecture-description governing patterns, and architecture-decision governing patterns remain live. NAR governs only the narrative rendering of that architecture-relevant structural information.

The temporal posture matters in both mediation modes. A historical reconstruction, a live football broadcast, a prospective project narrative, and a fictional continuation may all be narratives, but they have different source-basis return, evidence, uncertainty, ordering, and non-admissible-use obligations.

#### A.6.3.NAR:4.3 - Ordering rationale

The ordering rationale is not decoration. It is the structure-to-sequence rule.

Common ordering rationales:

| Ordering rationale | Use when |
| --- | --- |
| Event order | The selected source structure is a sequence of happenings or state changes. |
| Causal order | The reader must understand mechanism, dependency, intervention, or consequence. |
| Discovery order | The narrative teaches how a claim, design, or explanation was found. |
| Didactic order | The source basis is reordered so a learner can build prerequisites and reconstruct the selected source structures later. |
| Tension order | The narrative preserves conflicts, trade-offs, obstacles, failed attempts, or unresolved alternatives. |
| Traversal rule | The source basis is a graph, architecture, relation set, or option field and the narrative follows a declared path through it. |

If the source basis only changes carrier form, file format, export layout, OCR extraction, or byte order, this pattern is not open. Carrier serialization alone is not narrative rendering.

#### A.6.3.NAR:4.4 - Event model, viewpoint, and agency

If the narrative asks readers to understand events, actions, mechanisms, or change, state the event-model support. At minimum, name the event or mechanism type, participating holons or agents when present, causal or dependency links, update points, and what the narrative asks the reader to predict or revise.

If viewpoint, narrator, focalized object, protagonist, or agency choices affect understanding, keep them in domain narrative vocabulary unless a direct FPF governing pattern is live. In FPF Core, the reusable claim is simpler: the viewpoint choice foregrounds some selected source structure and hides or weakens another structure for a declared use.

#### A.6.3.NAR:4.5 - Engagement, ethics, and assurance boundary

Engagement is a real use claim, but it is not truth or permission.

When an engagement or motivation claim matters, state:

- intended effect for the declared use;
- selected source structure that may not be distorted for that effect;
- affected reader, listener, group, or decision context when relevant;
- non-admissible uses that would overread the narrative;
- direct governing pattern for ethical, evidence, assurance, or policy claims.

Use `D.1` for ethical value-frame entry, `D.2` through `D.4` for multilevel conflict and decision use, `D.5` for bias, human impact, or ethical assurance, `A.10` for evidence, and `B.3` for assurance. Narrative engagement never grants moral permission by itself.

#### A.6.3.NAR:4.6 - Reopen, lower, and return rule

A NAR case stays admissible only while its source basis, selected source structures, intended use, ordering rationale, source-basis or governing-pattern return condition, and neighboring governing-pattern exits still match the narrative rendering's use. When one of these changes, repair the smallest affected part of the case before relying on the narrative again. Do not turn NAR into a general monitor for all narrative science; this rule is local to the declared NAR case and its governing-pattern routing obligations.

| Trigger | Required move |
| --- | --- |
| Selected source structures or source basis change | Reopen the NAR case; restate preserved, foregrounded, coarsened, and lost structure; use `C.33` only when the narrative rendering is being used as architecture-relevant structural information, use the domain evaluation pattern for non-architecture epiplexity, use `G.2` for source-pack claims, and lower admissible use until the named source basis or receiving governing-pattern return condition is restored. |
| Intended reader or listener use becomes stronger, broader, or more reliance-facing | Lower the narrative to orientation-only use until the case is repaired; route publication or audience-unit claims to `E.17` or `E.17.AUD`, and route evidence, assurance, ethics, or policy force to `A.10`, `B.3`, or `D.1` through `D.5`. |
| Ordering rationale or traversal rule changes | Reopen the ordering field and visible-loss account; use `A.6.3.RT` if the representation scheme changed, `A.6.3.CSC` if the source basis was deliberately coarsened for narrower use, and NAR only when selected source structure is still being ordered into a narrative path. |
| Source-basis or governing-pattern return condition is missing, stale, or no longer reachable | Lower downstream use, return to the named source basis or receiving governing pattern, and refresh that return condition before treating the narrative as reliance-facing. Use `G.11` when currentness or freshness is the live problem. |
| Generated output, source-basis plan, schema, or admission result changes | Return to `C.35` for generated-carrier admission and `G.2` for source-pack claims; reopen NAR only after the source-basis-to-narrative relation, captured or lost structure, and correspondence obligations are again explicit. |
| Domain narrative vocabulary, source-pack basis, or relevant narrative, NLG, or cognitive SoTA changes the meaning of a relied-on narrative field | Refresh the domain vocabulary or source-pack basis first; lower any NAR claim that depended on the old vocabulary or source-basis anchor until the field meaning is replayable. |
| Downstream use requires stronger evidence, assurance, ethics, publication, or work authority than the NAR case carries | Keep NAR as a representation relation only; route the stronger claim to `A.10`, `B.3`, `D.1` through `D.5`, `E.17`, or the direct work or decision governing pattern, and mark that downstream use non-admissible until that governing pattern admits the stronger claim. |
| Correspondence or preservation claim weakens after repair | Use `C.34` only for the weakened correspondence that remains; use `C.33` for captured and lost architecture-relevant structures, use the domain evaluation pattern for non-architecture epiplexity, and lower any downstream use that required stronger sameness. |

### A.6.3.NAR:5 - Archetypal Grounding

Tell: `A.6.3.NAR` is the pattern for making an ordered narrative path from selected source structure while keeping the source-basis relation inspectable. It is not a pattern for writing a better story in general.

#### A.6.3.NAR:5.1 - Scientific mechanism narrative

A chemistry paper has calculations, candidate mechanisms, failed synthesis attempts, and an unresolved tension between theory and experiment. The narrative uses discovery order: failed attempts, structural clue, revised mechanism, new experiment, remaining uncertainty.

The NAR case records selected source structures `calculation set`, `mechanism candidates`, `experiment attempts`, and `unresolved tension`. It records preserved structure `candidate mechanism and failed-attempt relation`, foregrounded structure `discovery sequence`, lost structure `full calculation detail`, and source-basis return condition `return to the named calculation source basis before using the narrative for mechanism proof`.

This is not only conservative retextualization because ordering and tension carry the use. It is not proof because the narrative does not replace evidence.

#### A.6.3.NAR:5.2 - Architecture trade-off narrative

An architecture team explains why one candidate structure was selected. The source includes module structure, data custody, placement constraints, architecture characteristics, and rejected candidates.

The rendering mediation mode is architecture-mediated and prospective when the team is still choosing a future structure; it is retrospective when the team is reverse-engineering why an existing holon has the structure it has. The narrative follows tension order: current pain, candidate split, characteristic trade-off, rejected alternatives, selected structure, remaining residual. The NAR case records what structure the story preserves and which hidden structures remain non-admissible for implementation decisions until the architecture description, decision record, or synthesis governing pattern is reopened.

#### A.6.3.NAR:5.2.1 - Architecture narrative repair after source change

Later, one rejected candidate gains a new measurement basis and a placement constraint changes. The old narrative still tells a coherent tension story, but it no longer preserves the live candidate set. The repair is local: lower the old narrative to historical orientation, reopen the NAR case, replace the selected-source-structure refs and ordering rationale, and add a new source-basis or governing-pattern return condition pointing to the updated architecture description, decision record, or synthesis governing pattern.

The captured and lost structures move to `C.33`: old rejected-candidate relation preserved as history, new candidate-set relation captured, and obsolete measurement basis marked lost for current decision use. `C.34` may carry only the weakened correspondence that remains between the old narrative and the updated source. Implementation or decision use stays non-admissible until the architecture description, decision record, or synthesis governing pattern is repaired.

#### A.6.3.NAR:5.2.2 - Live unfolding event narrative

A commentator narrates a football match while the source event is still unfolding. The rendering mediation mode is direct source-structure and live. The selected source structures include score state, possession changes, tactical shape, player roles, momentum, and uncertainty about what the next play means.

The NAR case records that the narrative can orient the listener during the event, but later analysis, statistics, rule disputes, injury reports, or official results require return to the event record, official result publication, or governing evidence pattern. Live commentary may use tension and prediction, but it cannot treat provisional interpretation as settled event evidence.

#### A.6.3.NAR:5.3 - FPF seminar-route boundary

A team tests whether a future seminar series can explain FPF. The narrative rendering may use `A.6.3.NAR` to declare how FPF selected source structures are ordered for learners: EntityOfConcern discipline, problem frames, pattern use, relation records, source-basis return, framework authoring, and improvement loops.

The probe evaluates whether NAR supports an external seminar-route publication carrier for declared teaching use. It is not a narrative-rendering quality result, not evidence that FPF is correct, and not permission to place seminar outlines, slides, scripts, or exercises inside Core pattern bodies.

The actual seminar outline, slides, exercises, and script are not part of this pattern. They belong in a separate test-run publication carrier or teaching publication carrier. This pattern governs only the structure-to-sequence relation used by that carrier.

#### A.6.3.NAR:5.4 - Franchise-continuation storycraft probe boundary

A storycraft team tests whether a continuation-style narrative for a well-known space-opera franchise can preserve admitted source structures without becoming a fan-service list or an unauthorized publication plan. The source basis is the admitted canon or local source pack. The selected source structures may include continuity constraints, premise, theme, character-agency treatment, causal plot structure, viewpoint, stakes, and source-basis return refs.

`A.6.3.NAR` governs only the structure-to-sequence relation: which selected source structures are ordered into the proposed narrative path, which are foregrounded, which are lost or deferred, and when the worker must return to the named source pack. Storycraft vocabulary, canon classification, generation method, rights or publication permission, and full narrative-quality evaluation stay outside Core. Use `G.2` for the canon or source-pack claim, domain narrative and evaluation patterns plus direct FPF governing patterns for agency, responsibility, and declared-use rendering-quality claims, `C.35` when generated drafts are used, and publication or rights governing patterns when publication is live.

#### A.6.3.NAR:5.5 - Homotopy-theory explanation probe boundary

A teacher turns a graph-heavy mathematical source publication into a sequential explanation of homotopy theory. The selected source structures may include definitions, dependency order, examples, counterexamples, theorem prerequisites, proof-status boundaries, and return to formal statements. The narrative order may be didactic dependency order rather than historical discovery order or proof order.

`A.6.3.NAR` records the chosen sequence rule and visible loss: which mathematical structures remain reconstructible, which proof details or generalizations are deferred, and when the learner must return to formal mathematical statements. It does not certify the mathematical proof, replace the formal text, or turn analogy recall into understanding. Use mathematical-lens, proof, `G.2` source-use, evidence, publication, and teaching-evaluation governing patterns when those claims are live.

#### A.6.3.NAR:5.6 - Automated event-graph narrative

An LLM or NLG system receives an event graph, agent goals, constraints, and a domain schema, then proposes a story scene.

NAR records the relation only after source-basis admission and generated-output admission have done their work. The case names source plan, selected event relations, ordering rule, preserved event constraints, coarsened or hallucinated structure, and source-basis return condition. Generated fluency does not make the narrative authoritative; generated-output admission remains with `C.35`, source-pack claims with `G.2`, and evidence or assurance with their direct governing patterns.

### A.6.3.NAR:6 - Bias-Annotation

| Bias | How NAR counters it |
| --- | --- |
| Story-substitution bias | Requires selected source structure, preserved structure, lost structure, admissible use, and source-basis return condition before relying on the narrative. |
| Engagement-authority bias | Treats engagement as a declared-use claim and routes ethics, evidence, assurance, and policy force to their governing patterns. |
| Sequence-naturalization bias | Requires the ordering rationale instead of letting a fluent order look inevitable. |
| Carrier-serialization bias | Keeps file export, stream order, OCR, and layout changes outside NAR unless selected source structure is ordered into a narrative path. |
| Generated-fluency bias | Keeps generated narratives as carriers or candidates until source-basis relation, structure preservation, and governing-pattern routing are declared. |
| Narratology-import bias | Keeps narratology and storycraft vocabulary in domain source packs or local and domain frameworks, not as automatic FPF Core ontology. |

### A.6.3.NAR:7 - Conformance Checklist

| Check | Pass condition |
| --- | --- |
| `CC-NAR-1` | Source basis and selected source structures are named. |
| `CC-NAR-2` | Source-structure selection rationale and reader-interest or use hypothesis are explicit enough to explain why these structures matter. |
| `CC-NAR-3` | Source temporal posture, rendering mediation mode, narrating or rendering worker, receiving narrative rendering, and intended reader or listener role and use are named. |
| `CC-NAR-4` | The case states whether the same EntityOfConcern is preserved or a `C.34` correspondence is required. |
| `CC-NAR-5` | Ordering rationale or traversal rule is explicit. |
| `CC-NAR-6` | Preserved, foregrounded, coarsened, and lost structures are stated enough to block overread. |
| `CC-NAR-7` | Event-model support is present when events, mechanisms, goals, obstacles, or change are part of the use. |
| `CC-NAR-8` | Engagement or motivation claims are bounded by declared use and do not widen truth, evidence, assurance, policy force, or ethical permission. |
| `CC-NAR-9` | Admissible use, non-admissible downstream use, source-basis or governing-pattern return condition, and neighboring-pattern exits are named. |
| `CC-NAR-10` | Reused narrative cases are lowered, reopened, or routed through the governing pattern named in `A.6.3.NAR:4.6` when source basis, use, ordering, generated-output, source-pack, SoTA, or downstream-authority conditions change. |

### A.6.3.NAR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair move |
| --- | --- | --- |
| Good story as source replacement | The narrative is memorable, but later users cannot recover the selected source structure. | Fill the NAR case: selected source structures, preserved and lost structure, source-basis return condition, and non-admissible downstream use. |
| Tacit selection as narrative success | The worker or model picked some structures, but no one can explain why those structures serve this reader use. | Reconstruct the source-structure selection rationale and reader-interest hypothesis; keep the output orientation-only until this passes. |
| Sequence by habit | The author uses chronology, textbook order, or dramatic order without saying why that order preserves the source. | State the ordering rationale and what the chosen order hides. |
| Engagement as evidence | Reader attention, transportation, or emotional uptake is treated as stronger truth or permission. | Keep engagement as a declared-use effect; route evidence to `A.10`, assurance to `B.3`, and ethics to `D.1` through `D.5`. |
| Narratology word import | Terms such as plot, focalization, voice, protagonist, suspense, or narrator are used as Core FPF kinds. | Keep those terms in domain source packs or local and domain frameworks unless a later DRR admits a reusable Core distinction. |
| Generated narrative by fluency | LLM output is accepted because it reads coherently. | Use `C.35` for generated carrier admission, then apply NAR only to a declared source-to-narrative relation. |
| Teaching material inside pattern body | A seminar script or exercises are inserted into the pattern rather than testing the pattern. | Keep teaching material in a separate test-run publication carrier or teaching publication carrier; the pattern states the relation, checks, and source-basis return rule. |

### A.6.3.NAR:9 - Consequences

Positive consequences:

- Narrative becomes a reviewable representation relation rather than ungoverned prose.
- Readers can benefit from sequence, tension, viewpoint, and event support without losing source-basis return discipline.
- Generated and human-authored narratives receive the same source-structure checks before downstream use.
- FPF Core stays small while narrative-studies, narratology, NLG, pedagogy, and storycraft details can mature outside Core.

Costs and trade-offs:

- Authors must write a small relation note for reliance-facing narratives.
- Some attractive narratives will be downgraded to orientation-only use because selected source structure is not recoverable.
- Engagement claims can trigger ethics, evidence, or assurance governing patterns, which may slow publication but prevents persuasion from becoming hidden authority.

### A.6.3.NAR:10 - Rationale

Narrative is a powerful way to make structure usable by humans. It can order events, mechanisms, evidence, options, architecture decisions, and learning paths. That strength is also the risk: a well-formed narrative can make a source look simpler, more certain, more complete, or more ethically acceptable than it is.

The chosen Core pattern is therefore narrow. It does not make FPF a narratology, storycraft, teaching, or NLG framework. It adds one reusable relation under `A.6.3`: selected source structure is ordered into a sequential narrative rendering for declared use, while preservation, loss, admissibility, and source-basis return remain visible.

### A.6.3.NAR:11 - SoTA-Echoing

| Exact source or practice anchor | Adopt, adapt, or reject | Concrete NAR locus changed | Boundary and currentness |
| --- | --- | --- | --- |
| Roald Hoffmann, "The Tensions of Scientific Storytelling" (American Scientist, 2014) | Adopt as practice-grounded evidence that scientific narratives often order calculations, attempts, mechanisms, unresolved theory and experiment tensions, and discoveries rather than merely decorate results. | Adds scientific mechanism and discovery-order worked slices; requires ordering rationale, unresolved tension, and source-basis return condition. | Hoffmann is used as science-storytelling practice grounding, not current empirical cognitive SoTA and not authority over FPF ethics. |
| Wolf Schmid, `Narratology: An Introduction` (2010), and Matei Chihaia, `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` (2012) | Adapt Schmid's domain distinction between pre-narrative material, story, narrative, and presentation constitution, plus Chihaia's survey of narratology traditions, as domain vocabulary: source basis, selection, composition, ordering, viewpoint, and presentation matter. | Strengthens `orderingRationaleOrTraversalRule`, viewpoint loss, and the Core or domain boundary in the Solution and anti-patterns. | Fiction-bound narratology terms do not become FPF Core ontology unless a later DRR admits a reusable Core distinction. |
| Tan T. Nguyen, "A Review of Mechanistic Models of Event Comprehension" (2024); Lijuan Chen and Xiaodong Xu, "Neural and Behavioral Evidence for Differential Processing of Narrative Perspective in Novel Reading" (2026); Christoph Mengelkamp, Stefanie Golke, and Markus Appel, "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" (2025); Antonios Georgiou, Tankut Can, Mikhail Katkov, and Misha Tsodyks, "Large-scale study of human memory for meaningful narratives" (2025) | Adopt as current cognitive pressure for event-model support, reconstruction tasks, memory loss, overconfidence, and viewpoint effects. | Adds `eventModelSupport?`, learner reconstruction boundary, and checks for prediction, update, recall, source-detail loss, and viewpoint-sensitive recovery. | These sources support NAR and later domain narrative use claims; they do not supply evidence, assurance, or ethics by themselves. |
| Albert Gatt and Emiel Krahmer, "Survey of the State of the Art in Natural Language Generation" (2018); Amal Alabdulkarim, Siyan Li, and Xiangyu Peng, "Automatic Story Generation: Challenges and Attempts" (2021); Rogelio E. Cardona-Rivera, Joshua A. F. Ware, et al., "The Story So Far on Narrative Planning" (2024); Tuhin Chakrabarty, Vishakh Padmakumar, et al., "SceneCraft: Automating Interactive Narrative Scene Generation in Digital Games with Large Language Models" (2023); Yuan Ma, Richard Susilo, Patrik Haslum, and Hanna Suominen, "Text-to-Text Automatic Story Generation: A Survey" (2026); Aynigar Rahman, Aihe Yu, and Kyungeun Cho, "Game Knowledge Management System: Schema-Governed LLM Pipeline for Executable Narrative Generation in RPGs" (2026); Kien Nguyen-Trung and Ngoc Lan Nguyen, "Narrative-Integrated Thematic Analysis (NITA): How can LLMs support theme generation without coding?" (2026) | Adopt for automated narrativization boundaries: content planning, story planning, grounding, schema constraints, repair, evaluation limits, and human interpretive agency must be explicit. | Adds generated event-graph worked slice, generated-fluency bias, and governing-pattern exits to `C.35`, `G.2`, evidence, and assurance governing patterns. | Current story-generation and tool-assisted narrative SoTA is used for domain automation duties. NAR does not make generated output authoritative. |
| Melanie C. Green and Timothy C. Brock, "The Role of Transportation in the Persuasiveness of Public Narratives" (2000); Michael F. Dahlstrom and Shirley S. Ho, "Ethical Considerations of Using Narrative to Communicate Science" (2012); Hanna Meretoja, "Narrative and Human Existence: Ontology, Epistemology, and Ethics" (2014, abstract-level only here); FPF `D.1` through `D.5` ethics patterns | Adapt engagement as a real effect family with bounded use and ethical routing. | Adds engagement and motivation boundary, D-line governing-pattern routing, and anti-pattern against engagement as evidence or permission. | Engagement, persuasion, and narrative ethics vocabulary cannot widen truth, policy force, moral permission, or assurance without `D.1` through `D.5`, `A.10`, or `B.3`; Meretoja is background only until a source-pack claim sheet admits exact payload. |

### A.6.3.NAR:12 - Relations

- **Specializes:** `A.6.3` as a same-EntityOfConcern or declared-correspondence epistemic-viewing relation.
- **Coordinates with:** `A.6.3.CR` for same-regime textual re-expression, `A.6.3.RT` for representation-scheme transition, `A.6.3.CSC` for controlled semantic coarsening, `A.6.4` for changed EntityOfConcern, and `E.17.EFP` for explanation-use adequacy.
- **Uses:** `C.33` when the narrative rendering is being used as architecture-relevant structural information and its captured and lost structure must be made explicit, the domain evaluation pattern when the same question is non-architecture narrative epiplexity, and `C.34` when selected source structure and narrative structure are treated as same enough for downstream use.
- **Coordinates with:** `A.22.CGUS` when the structure being rendered is itself a constraint-governed unfolding structure or when a `NarrativeUnfoldingStructureBlock` must keep selected source structure, ordering structure, reader-act sequence hypothesis, narrative rendering, preserved structure, and loss inspectable.
- **Coordinates with:** `C.35` for generated or discovered carriers that may contain candidate narrative renderings, `G.2` for source-pack claims, `E.6` and `E.11` for learning-order and first-entry publication questions, and `E.17` or `E.17.AUD` for publication-face and audience-unit questions.
- **Uses:** `G.11` when source-basis return currentness, freshness, telemetry, or source-pack decay is the live reason a NAR case must be refreshed before reuse.
- **Routes to:** `D.1` through `D.5`, `A.10`, and `B.3` when value frame, multilevel harm, conflict, decision use, bias, impact, evidence, or assurance becomes live.
- **Boundary:** NAR governs the structure-to-sequence narrative rendering relation. It does not publish the narrative, authorize reliance, prove the source, admit generated output, decide ethics, create a teaching script, or make a domain narrative vocabulary part of FPF Core.

### A.6.3.NAR:End

