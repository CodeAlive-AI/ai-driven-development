## E.2.DA - FPF Pillar-Adequacy Evaluation CharacteristicSpace

Status: Core.

### E.2.DA:1 - Problem frame

Use `E.2.DA` when the object under improvement is an FPF-level object and the question is whether it realizes the `E.2` Pillars adequately for a declared use. The object can be a monolith edition, selected pattern host set, pattern family, projection set, README/Preface/ToC publication change, access-carrier exposure such as a skill or MCP-backed route, release candidate, or whole-FPF edition.

Use it after a broad cleanup, new pattern family, projection repair, source-use repair, FPF-form change under `E.4.FPF`, or corpus-level improvement when local pattern quality is not enough. A set of good local patterns can still harm FPF entry, naming, layering, source use, projection integrity, or open-ended evolution.

Not this pattern when the evaluated object is one authored pattern version, one `DRR`, one local wording repair, or one pattern-use entry problem. Use `E.21`, `E.9.DA`, `E.10` and its precision-restoration neighbours, or `E.11` for those objects.

First useful move: name the FPF object under improvement by value, declared use, reader family, and qualification window; then evaluate all eleven Pillar coordinates. If a Pillar seems unaffected, give it a value and a short rationale saying what is preserved.

What goes wrong if missed: FPF can become locally polished but globally worse. Readers may find fewer useful entry points, precision repairs may erase the working move, source rows can turn decorative, or several patterns can grow local variants of the same doctrine.

Primary EntityOfConcern in plain terms: the scoped FPF object under improvement as an `E.2` Pillar-realizing language object.

### E.2.DA:2 - Problem

`E.2` gives the Pillars and their constitutional meaning. It does not by itself evaluate whether a concrete FPF object realizes those Pillars well enough for a concrete use. Without `E.2.DA`, corpus-level reviews tend to collapse into local pattern scores, process state, review praise, or broad claims that "FPF improved."

The specific failures are:

1. Local pattern quality is averaged into FPF adequacy.
2. Entry projections and companion files start carrying semantics beside governing patterns.
3. Precision repair improves terminology but damages first-use comprehension or changes the FPF kind carried by the repaired text.
4. Source and SoTA rows are counted rather than checked for changes in FPF moves.
5. Front-like words such as `all 5s`, `exceptional`, `Pareto`, `SoTA`, `NQD`, or `shortlist` become loose synonyms.
6. Corpus-level stop claims hide what became worse.
7. Pillar values become repair targets, so the corpus gains projection proof, entry apparatus, source rows, or review evidence while the FPF object becomes less usable, less layered, or less decisive.

### E.2.DA:3 - Forces

| Force | Tension |
|---|---|
| Constitutional meaning vs evaluation | Pillar meanings stay in `E.2`; values over realized adequacy are evaluated here. |
| Whole-FPF quality vs local quality | One strong pattern can still sit in a weak corpus ecology. |
| Discoverability vs precision | Real readers search ordinary words, while FPF claims need governing patterns and kinds. |
| Didactic force vs semantic admissibility | The text must teach the move without smuggling new ontology into examples or projections. |
| Breadth vs affordability | Eleven Pillars are complete enough for FPF; affordability comes from compact evidence, not omitted coordinates. |
| Open-ended evolution vs release stop | FPF can improve forever, but one scoped object needs a local stop condition. |

### E.2.DA:4 - Solution

`E.2.DA` is the Pillar-adequacy specialization of `A.19.ECS`. It evaluates one FPF object under improvement against all eleven `E.2` Pillars for a declared use.

There is no smaller `E.2.DA` evaluation. If the caller only needs local pattern quality, `DRR` adequacy, or wording repair, that is a different object-under-improvement evaluation. Once `E.2.DA` is invoked, every Pillar coordinate receives a value, short rationale, evidence locus, and shared evidence basis for the FPF object being evaluated.

#### E.2.DA:4.1 - Local names and kind settlement

| Local name | Kind and use |
|---|---|
| `FPFPillarAdequacyEvaluation` | Authored evaluation record over one scoped FPF Pillar-adequacy claim. |
| `FPFObjectUnderImprovementRef` | FPF object version named by value being evaluated. |
| `FPFAdequacyUseScope` | Declared FPF-level use the object must serve. |
| `FPFAdequacyReaderScope` | Primary reader family and working situation for the adequacy claim. |
| `FPFAdequacyQualificationWindow` | Edition, source-currentness, neighbour, release, or comparison window for which the values hold. |
| `FPFPillarAdequacyCoordinateSet` | The eleven required Pillar coordinates in this pattern. |
| `FPFPillarAdequacyEvidenceBasis` | Checked loci named by value in the scoped FPF object: pattern bodies, host or monolith sections, projections, README scenarios, ToC rows, `E.11` entry-distribution loci, `I.2` expanded entry-disambiguation cases, source rows, relation rows, companion files, evaluation results, and missing or unchecked loci that affect values. |
| `FPFPillarValueRationales` | Required result rows: Pillar coordinate, value, short rationale, and evidence locus named by value. |
| `PillarAdequacyEvidenceRefs` | Loci named by value in patterns, projections, source rows, entry rows, relation rows, or findings used as value evidence. |
| `FPFKindRestorationEvidence` | Pre-repair and post-repair object-kind, relation-or-claim-kind, current ontic slot, relation position, use relation, or claim kind when that position or use is part of the changed FPF-governed claim, admissible-use, and scope evidence for broad precision or wording cleanup that affects the scoped FPF object. |
| `FPFPillarAdequacyStatus` | Admissible-use result for the scoped FPF Pillar-adequacy claim. |
| `FPFPillarAdequacyFront` | Optional non-dominated set of FPF variants or edit packages under the declared coordinate set. |

These names are local to the evaluation unless `F.18` promotes a durable name. They name FPF content objects and evaluation fields, not release state, review state, or project evidence.

#### E.2.DA:4.2 - Evaluation record

```text
FPFPillarAdequacyEvaluation:
  FPFObjectUnderImprovementRef: <object and version named by value>
  FPFAdequacyUseScope: <entry | authoring | review | project use | source absorption | corpus release | other use named by value>
  FPFAdequacyReaderScope: <primary reader and working situation>
  FPFAdequacyQualificationWindow: <edition, source, neighbour, release, or comparison window>
  FPFPillarAdequacyEvidenceBasis: <checked pattern, host, monolith, projection, README, ToC, E.11, or I.2 entry locus, source, relation, companion, evaluation-result, and missing loci that affect values>
  FPFPillarAdequacyCoordinateTable: <all eleven coordinates, values, short rationales, evidence loci>
  FPFKindRestorationEvidence: <when broad wording or precision repair is part of the evaluated change: pre-repair and post-repair kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind if part of the changed FPF-governed claim, admissible use, scope, governing pattern when another pattern governs the kind under repair, relation, claim, or position, and preserved, split, intentionally changed, or blocker disposition>
  FPFPillarAdequacyStatus: <status>
  StopOrRepairCondition: <local stop, first repair, Pillar decision, or architecture decision>
```

`E.22` may frame the evaluation purpose when the caller needs floor evaluation, exceptional improvement, trade-off inspection, open-question discovery, absorption, or proposal portfolios. `E.23` governs repeated improvement after the evaluation returns findings or candidate proposals.

#### E.2.DA:4.3 - Ordinal coordinate scale

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The Pillar is not realized for the declared FPF object and use. |
| 1 | `namedOnly` | The Pillar is named but cannot guide the FPF-level use. |
| 2 | `partiallyExpressedForDeclaredUse` | The Pillar is present but incomplete, fragile, or too local. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The Pillar is realized enough for the declared use, with known limits visible. |
| 4 | `wellExpressedForDeclaredUse` | The Pillar is clear across relevant loci and protected from common loss. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The Pillar is exceptionally realized with reinforcing loci, heterogeneous cases, and no hidden FPF-level loss. |

The values are ordinal content evaluations. They are not a scalar score, maturity ladder, release gate, or proof that development ends.

#### E.2.DA:4.4 - Required Pillar coordinates

| Pillar coordinate | Evaluation question | Good state |
|---|---|---|
| `P1CognitiveEleganceAdequacy` | Does the object expose decisive structure without ornamental formalism? | The reader sees the smallest structure that changes the action. |
| `P2DidacticPrimacyAdequacy` | Does human comprehension stay ahead of formal, tooling, or review purity? | Working situation, recognition reason, first move, and payoff stay visible. |
| `P3ScalableFormalityAdequacy` | Can informality mature toward formal assurance without forks or rewrites? | Plain, Tech, Formal, and mathematical strengthening remain staged. |
| `P4OpenEndedKernelAdequacy` | Do kernel concepts stay meta-level while domain knowledge stays in patterns? | New content extends FPF without smuggling domain doctrine into the kernel. |
| `P5FPFLayeringAdequacy` | Do modular pattern layering and neighbour authority stay intact? | Patterns can be added, replaced, or removed without shadow authority. |
| `P6LexicalStratificationAdequacy` | Are Plain, Tech, Formal, and mathematical registers recoverable for the declared use? | Decision-governing wording maps to fields named by value, kinds, lenses, or neighbours. |
| `P7PragmaticUtilityAdequacy` | Do proofs, measures, models, and reviews change real admissible action? | The object changes prediction, decision, diagnosis, design, repair, stop, or assignment. |
| `P8CrossScaleConsistencyAdequacy` | Do composition, aggregation, boundary, emergence, and method-side relation structures stay consistent across scales? | Cross-scale claims name preserved structure, lost structure, lens or algebraic representation, and boundary. |
| `P9StateExplicitnessAdequacy` | Are states, transitions, currentness, editions, and qualification windows explicit for the declared use? | Readers can tell what version and state are being used and what changes them. |
| `P10OpenEndedEvolutionAdequacy` | Can improvement continue cheaply and safely without pretending development ends forever? | Local stop conditions coexist with reopen conditions for new use, source, comparison, or failure evidence. |
| `P11SoTAAlignmentAdequacy` | Does current knowledge discipline the object without citation theatre? | Current sources change moves, boundaries, examples, checks, or stop rules. |

#### E.2.DA:4.5 - Evidence and coordinate separation

One evidence locus may support several coordinates, but the rationale must say what property it supports in each coordinate. The following distinctions carry most repairs:

| Distinction | Use |
|---|---|
| `P1` vs `P2` | smallest decisive structure vs reader comprehension and first move. |
| `P2` vs `P6` | usable recognition text vs recoverable register mapping. |
| `P5` vs `P7` | right governing pattern vs useful change in action. |
| `P7` vs `P11` | practical payoff vs current source contribution. |
| `P8` vs `P9` | cross-scale invariant vs state, transition, edition, and currentness. |
| `P10` vs `E.23` | evolvability of the FPF object vs repeated improvement method. |

If a distinction cannot be recovered from the FPF object, lower the affected coordinate and state the first repair. Do not add a new local doctrine table to explain around the missing content.

`E.21` and `E.9.DA` results are evidence loci for `E.2.DA`, not inputs to be averaged. A pattern-quality value can support a Pillar only by pointing to the FPF-level effect it creates or damages.

#### E.2.DA:4.5a - Result-row discipline and calibration

An `E.2.DA` result uses this table shape:

| Pillar coordinate | Value | ShortRationale | EvidenceLocus |
|---|---:|---|---|
| `<E.2.DA coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the FPF evidence; why the higher adjacent value would overstate it, or for 5 what would lower or reopen>` | `<pattern section, monolith section, host, README scenario, ToC row, E.11 entry-distribution locus, I.2 expanded case, projection, source row, relation row, companion file, evaluation result, or missing locus named by value>` |

A Pillar essay, local-quality average, two-column table, or result whose value depends on unchecked corpus, projection, or source evidence is not an `E.2.DA` result. It is only draft evaluation material. Missing or unchecked evidence lowers the Pillar coordinate that needs it; it does not make the coordinate optional.

Common calibration points:

| Pillar family | `3` | `4` | `5` |
|---|---|---|---|
| Entry, usability, and projection Pillars | The object can be used with visible limits, but projection or first-use evidence is partial. | Relevant governing loci and projections are coherent enough for declared use. | The use is replayable across governing text, projection, cold-reader or retrieval evidence, and non-use boundary. |
| Layering and semantic authority Pillars | Neighbours are plausible, but some authority or shadow-spec risk remains. | Governing patterns named by value and thin projections are distinguishable. | Authority is robust across pattern bodies, relations, projection rows, and anti-fragmentation cases. |
| Source and evolution Pillars | Source or reopen language exists, but currentness, contribution, or smallest-reopen basis is compact. | Source contribution, currentness window, and reopen condition are explicit for declared use. | Source-front movement and future reopen are replayable without freezing development after a local stop. |

#### E.2.DA:4.6 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredFPFUse` | All eleven coordinates meet the declared floor for the scoped use. |
| `repairBeforeFPFUse` | One or more coordinate floors fail for the declared use. |
| `holdForPillarDecision` | The defect requires an `E.2` Pillar amendment or precedence decision. |
| `holdForArchitectureDecision` | The defect requires pattern split, object-under-improvement, source-use, projection-use, or naming architecture decision. |
| `refreshNeeded` | A source, pattern, entry use, projection, relation, or vocabulary change invalidates a previous evaluation. |

The stop condition states the declared floor, values, bounded non-use, smallest reopen locus, and first repair if the declared use is not yet admissible.

#### E.2.DA:4.7 - Compact result form

```text
E.2.DA result:
  FPF object under improvement: <FPFObjectUnderImprovementRef>
  Declared use and reader: <scope>
  Qualification window: <window>
  Evidence basis checked: <FPFPillarAdequacyEvidenceBasis>
  Status: <FPFPillarAdequacyStatus>
  Coordinate table: <Pillar coordinate | Value | ShortRationale | EvidenceLocus for all eleven Pillars>
  First repair or stop: <repair | hold | local stop>
  Reopen if: <smallest changed locus or condition>
```

For a small release decision, the coordinate table may be compact. It is still complete. Status is not assigned from prose, a checklist count, a local-pattern average, a two-column table, or a result missing evidence loci needed by its values.

When `E.22`, `E.23`, absorption, or exceptional-improvement framing asks for improvement, below-floor Pillar coordinates return findings or repair. Above-floor coordinates receive proposal rows only for substantive non-dominated FPF-level content opportunities inside the declared use: better entry recognition, governing-pattern authority, source-currentness carry-through, projection thinning, corpus-ecology repair, kind-preserving precision restoration, open-ended evolution support, or deletion or relocation of apparatus that weakens the FPF object. Do not treat every value below `5` as a defect. A `4` may be the correct stop value only with loci showing why further Pillar-content movement is dominated, unavailable, or outside scope.

### E.2.DA:5 - Worked slices

**Broad precision cleanup.** A wording pass makes many patterns more admissible but several `Problem frame`s now explain less about why the distinction matters, or a cleaned phrase changes the governed kind while the trigger word disappears. `P2`, `P6`, and `P7` receive lower values until the affected patterns restore recognition reason, useful action, and pre-repair and post-repair kind evidence in admissible wording.

**Ontic architecture repair.** A campaign adds `E.24.CD`, `E.24.PUB`, or a new ontic host. Pillar values rise only if the change reduces duplicate ontology, type explosion, or shadow authority and improves FPF entry, authoring, review, or project use. Extra ontic terminology, score proof, or publication-boundary prose without better action lowers `P1`, `P2`, `P5`, `P6`, and `P7`.

**Repeated content, route, reference, neighbour-reference, and negative-fanout cleanup that weakens content.** A corpus pass removes repeated "not proof", "not gate", and "not work" prose, route metaphors, repeated guards, repeated mini-rules, repeated conditional neighbour-reference mappings, reference boilerplate, or architecture-placement prose, but leaves several patterns with less positive ontology, method, norm, or worked action than before. `P2`, `P5`, `P6`, `P7`, and `P10` receive lower values until the affected patterns restore their own subject content and state only current declarative governing relations.

**Projection repair.** README scenarios, ToC rows, `E.11` entry-distribution loci, and `I.2` expanded entry-disambiguation cases improve search but can start carrying pattern semantics. `P5` and `P9` fall because projections become shadow authority. The repair moves durable semantics back to governing patterns and leaves thin echoes in projections.

**Source absorption.** A new source family adds current methods, but pattern bodies only cite it. `P11` stays low until source rows change selected actions, examples, checks, or stop conditions. `P7` changes only when the source changes action.

### E.2.DA:6 - Bias annotation

This pattern biases FPF toward whole-language adequacy. The bias is useful because local repairs often hide corpus-level loss.

The bias is bounded by the object-under-improvement declaration. `E.2.DA` does not replace `E.21`, `E.9.DA`, `E.10`, `E.11`, or `E.23`; it evaluates their FPF-level Pillar effect when the scoped FPF object includes their results.

### E.2.DA:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E2DA-1` | Name `FPFObjectUnderImprovementRef`, use scope, reader scope, and qualification window. |
| `CC-E2DA-2` | Preserve `E.2` as the source of Pillar meaning. |
| `CC-E2DA-3` | Evaluate all eleven Pillar coordinates with values, short rationales, and evidence loci, using the required result-row shape. |
| `CC-E2DA-4` | Justify values from FPF content, not review praise, landing, monolith placement, or absence of visible defects. |
| `CC-E2DA-5` | State status, stop or first repair, bounded non-use, and reopen condition. |
| `CC-E2DA-6` | Keep projections, packets, companions, and entry rows below governing pattern authority. |
| `CC-E2DA-7` | Treat `E.21` and `E.9.DA` as evidence loci only where they change Pillar realization. |
| `CC-E2DA-8` | State what became worse when visible coordinates improved. |
| `CC-E2DA-9` | State the `FPFPillarAdequacyEvidenceBasis`; if host or monolith parity, projection, README, ToC, `E.11`, `I.2`, source-currentness, relation, companion, or evaluation-result evidence is missing or unchecked, lower the Pillar coordinate that needs it. |
| `CC-E2DA-10` | Use adjacent-value calibration when assigning `3`, `4`, or `5`; a rationale must distinguish the assigned value from its lower and higher neighbours. |
| `CC-E2DA-11` | When the evaluated FPF object includes broad wording, naming, or precision cleanup, state `FPFKindRestorationEvidence` for changed FPF-governed phrases. If the cleanup changes, narrows, widens, flattens, or loses the governed kind, relation, claim kind, current ontic slot, relation position, use relation, or claim kind when that position or use is part of the changed FPF-governed claim, admissible use, or scope without accepted decision evidence and governing-pattern reference when another pattern governs the kind under repair, relation, claim, or position, lower the affected Pillar coordinates and keep the repair blocking. |
| `CC-E2DA-11a` | When the evaluated FPF object includes ontic architecture, evaluate FPF-level effect, not ontic apparatus volume: reduced duplicate ontology or type explosion, clearer `EntityOfConcern` and SlotRelation boundaries, correct description-publication separation, thinner projections, and improved entry, authoring, review, or project use. Missing effect lowers the affected `P1`, `P2`, `P4`, `P5`, `P6`, `P7`, or `P8` coordinates. |
| `CC-E2DA-12` | Keep Pillar values as measurement results, not repair targets. Below-floor values require FPF-level findings or repair. Above-floor improvement requires substantive non-dominated proposal rows when requested; it cannot close by adding projection proof, entry apparatus, source volume, review praise, monolith parity evidence, or all-`5` result framing that does not improve Pillar realization for the declared FPF use. A no-proposal or stay-at-current-value disposition must name loci and why no worthwhile Pillar-content improvement remains. |

### E.2.DA:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Pillar essay.** A review names Pillars without values or evidence. | Produce the complete `E.2.DA` result form. |
| **Local-quality averaging.** Several `E.21` values are averaged into FPF adequacy. | Re-evaluate Pillar effects over the FPF object. |
| **Sterile or kind-changing precision cleanup.** Language is admissible but no longer usable, or the trigger word is gone while the governed kind, relation, claim kind, current ontic slot, relation position, use relation, or claim kind that is part of the changed FPF-governed claim, admissible use, or scope changed. | Lower `P2`, `P6`, and `P7` and restore recognition reason, useful action, and pre-repair and post-repair kind evidence; if the current ontic slot, relation position, use relation, or claim kind changed without an accepted decision, treat the cleanup as a blocking semantic defect. |
| **Ontic apparatus without FPF gain.** A change adds ontic names, pattern-set maps, publication-boundary prose, or evaluation proof while duplicate ontology, entry confusion, or project-use difficulty remains. | Lower the affected Pillar coordinates; repair the governed object, slot-relation boundary, publication split, and user action, or decline the ontic candidate. |
| **Projection authority.** A ToC, packet, or companion carries semantics. | Move semantics to the governing pattern and leave projection echo. |
| **Citation shelf.** Source rows do not change FPF moves. | Lower `P11` and state the missing source contribution. |
| **Pillar table without evidence loci.** Values are listed but not tied to corpus loci named by value. | Re-run with `Pillar coordinate \| Value \| ShortRationale \| EvidenceLocus`; lower any Pillar whose evidence cannot be named. |
| **Goodharted Pillar adequacy.** FPF-level values rise because more projection, source, review, or parity evidence was added, while entry recognition, layering, semantic authority, pragmatic utility, source use, or open-ended evolution becomes worse. | Reject apparatus-only improvement; apply `E.13` when Pillar values become targets replacing Pillar realization; repair the FPF-level content effect, delete or relocate proof material, and record checked no-proposal only when no non-dominated Pillar-content improvement remains. |

### E.2.DA:9 - Relations

| Pattern | Relation |
|---|---|
| `E.2` | Supplies Pillar names and meanings. |
| `A.19.ECS` | Supplies construction discipline for object-under-improvement evaluation characteristic spaces. |
| `E.4.FPF` | Names FPF itself as a first-principles framework edition and routes FPF form, publication/access carriers, and whole-FPF adequacy to this pattern. |
| `E.21` | Evaluates one pattern version; may supply evidence loci. |
| `E.9.DA` | Evaluates one `DRR`; may supply evidence loci. |
| `E.24`, `E.24.CD`, `E.24.PUB` | Govern ontic concept introduction, candidate detection, ontic-description and publication discipline, and publication-boundary repairs whose FPF-level Pillar effect may be evaluated here. |
| `E.22` | Frames the quality-evaluation purpose when needed. |
| `E.23` | Runs repeated improvement after values or proposal rows exist. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when Pillar values, corpus indicators, review result, or projection evidence become substitutes for realized FPF value. |

| `E.10`, `A.6.P`, `C.2.P`, `C.16.Q`, `F.18` | Govern local precision and naming repair. |
| `E.11`, `E.17`, `I.2` | Govern entry, projection, publication, description, and expanded entry-disambiguation uses that may affect Pillar adequacy. |
| `C.18`, `C.19`, `G.5`, `G.9`, `G.11` | Govern OEE, NQD, pool, selected-set, parity, and refresh semantics when those semantics are claimed. |
| `C.29`, `C.16`, `A.17`, `A.18`, `A.19` | Govern mathematical-lens, characteristic, scale, measurement, and characteristic-space admissibility when those claims are being made. |

### E.2.DA:10 - Rationale

FPF needs a corpus-level quality instrument because the language can degrade while individual pattern edits look successful. The complete eleven-coordinate evaluation prevents the common escape hatch: "this is only a local repair" repeated across many files until Pillar realization changes.

The instrument is still affordable because it asks for short rationales and evidence named by value loci. It does not require a new review process, full audit bundle, or exhaustive evidence or source-material dossier.

### E.2.DA:11 - SoTA-Echoing

| Claim | Practice basis | Local adoption |
|---|---|---|
| Pillar meanings stay constitutional, while evaluation checks realized adequacy. | `E.2` constitutional source plus `A.19.ECS` evaluation-characteristic construction. | `E.2.DA` evaluates one scoped FPF object without redefining the Pillars locally. |
| Whole-language adequacy needs aim, evidence, change, and learning. | Model for Improvement, PDSA, and PDCA lineage carried through `E.22` and `E.23`. | The evaluation names declared FPF use, evidence basis, first repair or stop, and reopen condition rather than treating release result as improvement. |
| Feedback needs current state, desired state, next action, and tactics. | Sadler and Hattie and Timperley feedback traditions carried through `E.22` and `E.23`. | Values, short rationales, evidence loci, proposal rows, and checked no-proposal dispositions stay distinct. |
| Local pattern quality is not whole-FPF adequacy. | Pattern-language entry and projection discipline from `README`, ToC, `E.11`, and `I.2`, plus current `E.21` and `E.9.DA` source lines. | `E.21` and `E.9.DA` are evidence loci only when they change Pillar realization; they are not averaged into corpus adequacy. |
| Precision repair can improve wording while damaging use. | `E.10`, `A.6.P`, `C.2.P`, `C.16.Q`, `F.18`, and `F.19` precision-restoration lines. | Broad cleanup must show pre-repair and post-repair kind, relation, admissible use, and FPF-level Pillar effect; lexical disappearance is not closure. |
| Multi-coordinate improvement needs trade-offs and non-dominated alternatives. | MCDA, Pareto, ATAM, and QD, OEE, and NQD lines carried through `E.22` and `E.23`. | `E.2.DA` asks what became worse and treats front-like vocabulary as governed semantics, not praise. |
| Pillar-adequacy measures can become targets. | Goodhart and Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines. | `E.2.DA` forbids all-`5` or `5-defensible` repair targeting; values rise only when the scoped FPF object better realizes Pillars for declared use, and `E.13` governs any proxy-to-value claim about those values. |

### E.2.DA:12 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| FPF-level adequacy becomes measurable by content. | Release and corpus decisions no longer rely on local praise or review state. | Evaluators must name the FPF object and use named by value. |
| Complete Pillar evaluation blocks partial-good stories. | Hidden losses in entry, layering, source use, and evolution become visible. | Even compact evaluations must touch all eleven coordinates. |
| Local evaluation patterns keep their authority. | `E.21`, `E.9.DA`, and `E.10` are evidence or repair neighbours, not substitutes. | Users must choose the right object under improvement before evaluating. |

### E.2.DA:End

