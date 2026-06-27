## E.9.DA - DRR Decision-Adequacy Evaluation CharacteristicSpace

Status: Core.

### E.9.DA:1 - Problem frame

Use `E.9.DA` when one `DRR` must be reliable enough for a declared FPF authoring use: pattern drafting, host amendment, selected-locus distribution, accepted-decision carry-through, source-use carry-through, scope-boundary decision, split decision, or architecture-hold decision.

Not this pattern when the evaluated object is one authored pattern version, one admission or refresh review, one local wording repair, or a measurement-law problem. Use `E.21`, `E.19`, `E.10` and its precision-restoration neighbours, or `C.16`, `A.17`, `A.18`, and `A.19` for those objects.

First useful move: name `DRRVersionRef` by value, declared authoring use, selected-locus disposition map, and qualification window; then evaluate every decision-adequacy coordinate in this pattern. Missing decisions lower coordinates and produce repair, split, or hold status inside the same evaluation.

What goes wrong if missed: a formally valid `DRR` may still be too weak for drafting. It may summarize sources instead of deciding, mention neighbours without obligations, hide rejected alternatives, leave trigger words unresolved, or omit the first drafting action.

Primary EntityOfConcern in plain terms: the decision-adequacy claim of one `DRR` version for a declared FPF authoring use.

### E.9.DA:2 - Problem

`E.9` defines the `DRR` kind and minimum decision-rationale form. It does not by itself say whether one concrete `DRR` is decision-bearing enough for downstream FPF authoring. Without `E.9.DA`, reviewers tend to approve headings, source volume, or clean prose while the pattern author still has to invent missing decisions.

Recurring failures:

1. The decision question is broad or implicit.
2. The selected answer is a summary rather than a decision.
3. Alternatives, rejected options, and outside-decision items are not closed.
4. Receiving loci are named but not assigned content obligations or non-obligations.
5. The selected FPF content architecture is explicit but wrong.
6. Source use is copied without saying what changed in the accepted decision.
7. Architecture descriptions, views, graphs, packets, or notes are treated as the FPF decision.
8. Administrative state becomes adequacy evidence.
9. Ordinal adequacy values become repair targets, so the `DRR` gains source rows, locus tables, boundary catalogues, or review proof while the selected answer and first drafting action do not become more decisive.

### E.9.DA:3 - Forces

| Force | Tension |
|---|---|
| Decision completeness vs concise rationale | A `DRR` must decide enough, but must not become final pattern prose. |
| Exactness vs drafting freedom | The `DRR` fixes selected answers and boundaries; authors still write usable pattern text. |
| Source preservation vs synthesis | Source distinctions matter, but the `DRR` must state FPF decisions. |
| Multi-locus coordination vs EoC boundary | One decision can affect many patterns while one `DRR` adequacy claim stays scoped. |
| Architecture selection vs address completion | Every locus can be assigned and still be the wrong split or merge. |
| Affordability vs completeness | Small editorial decisions stay under `E.9`; opened `E.9.DA` evaluates every coordinate compactly. |

### E.9.DA:4 - Solution

`E.9.DA` is the `DRR` decision-adequacy specialization of `A.19.ECS`. It evaluates whether one `DRR` version carries enough decision content for the declared authoring use.

There is no partial `E.9.DA` result. Once invoked, the evaluator assigns a value, short rationale, and evidence locus to every coordinate in `E.9.DA:4.4`, and states the evidence basis used for the result. If the `DRR` lacks a field, source row, selected-locus map, architecture decision, comparator, or currentness basis needed by a coordinate, the relevant coordinate receives a low value and the status states the repair, split, or hold.

#### E.9.DA:4.1 - Local names and kind settlement

| Local name | Kind and role |
|---|---|
| `DRRDecisionAdequacyEvaluation` | Authored adequacy-evaluation record for one scoped `DRR` decision-adequacy claim. |
| `DRRVersionRef` | `DRR` version named by value for the evaluation. |
| `DRRDeclaredAuthoringUse` | Downstream FPF authoring use the `DRR` is expected to carry. |
| `DRRSelectedLocusDispositionMap` | Map from selected loci named by value to selected content responsibilities, explicit non-responsibilities, sibling decisions, or outside-decision dispositions. |
| `DRRDecisionAdequacyQualificationWindow` | Edition, source set, accepted-decision record, neighbour condition, and currentness window for which the evaluation holds. |
| `DRRDecisionAdequacyCoordinateSet` | The required coordinates in this pattern. |
| `DRRDecisionAdequacyEvidenceBasis` | `DRR`, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci named by value for coordinate values. |
| `DRRCoordinateValueRationales` | Required result rows: coordinate, value, short rationale, and evidence locus named by value. |
| `DRRCoordinateLocusRefs` | `DRR` loci used as value evidence. |
| `DRRSourceUseDischargeMap` | Source-use role, source-currentness, selected payload, rejected payload, and selected locus when source material governs a decision. |
| `DRRPrecisionRestorationProfile` | Compact scalar profile for DRR wording-use precision: word-use precision, phrase apparatus, repetition-and-distribution, ontic-slot clarity, description-publication-source boundary separation, and pattern-application ontology. It records overall effect, affected coordinates, selected governing pattern, and no-repair disposition with loci when clean. |
| `DRRKindRestorationCheck` | Required pre-repair and post-repair object-kind, relation-or-claim-kind, slot or use-position, admissible-use, and scope check, or `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` disposition with loci, for any DRR wording, naming, or precision-restoration repair proposal. |
| `DRROnticCandidateDisposition` | If the `DRR` selects, rejects, splits, or declines a candidate ontic, this names the candidate `EntityOfConcern`, sufficiency rationale, rejected alternatives, broad candidate-universe sanity sweep when the claim is broad, slot-relation boundary, description-publication boundary, and selected pattern placement by value. |
| `DRRDecisionAdequacyStatus` | Admissible-use status for the scoped `DRR` decision-adequacy claim. |

These names are local evaluation fields. They are not release state, review status, project evidence, gate result, assurance, or pattern-quality values.

#### E.9.DA:4.2 - Evaluation record

```text
DRRDecisionAdequacyEvaluation:
  DRRVersionRef: <DRR version named by value>

  DRRDeclaredAuthoringUse: <drafting | amendment | distribution | source-use carry-through | accepted-decision carry-through | split or hold decision>
  DRRSelectedLocusDispositionMap: <locus -> selected responsibility, explicit non-responsibility, sibling decision, or outside-decision disposition>
  DRRDecisionAdequacyQualificationWindow: <source, edition, neighbour, currentness window>
  DRRDecisionAdequacyEvidenceBasis: <checked DRR, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci; missing or unchecked loci named when they affect values>
  DRRDecisionAdequacyCoordinateTable: <all coordinates, values, short rationales, evidence loci>
  DRRPrecisionRestorationProfile: <word-use precision, phrase apparatus, repetition-and-distribution, ontic-slot clarity, description-publication-source boundary, and pattern-application profile; overall effect, affected coordinates, selected governing pattern, and no-repair or repair disposition with loci>
  DRRKindRestorationCheck: <required for each wording, naming, or precision-restoration repair proposal; pre kind, relation, claim, slot or use-position, admissible use, and scope -> post kind, relation, claim, slot or use-position, admissible use, and scope; not triggered | ordinary prose | already satisfied | preserved | split | intentionally changed | blocker, with loci>
  DRROnticCandidateDisposition: <if ontic or pattern-set architecture is at issue: selected, rejected, split, or declined candidate, sufficiency rationale, rejected alternatives, candidate-universe sanity sweep if broad, slot-relation boundary, description-publication boundary, and selected pattern placement>
  DRRDecisionAdequacyStatus: <status>
  StopOrRepairCondition: <local stop, first repair, split, or architecture hold>
```

`E.22` may frame whether the evaluation is floor-only, exceptional-improvement, trade-off, open-question, absorption, or proposal-producing. `E.23` governs repeated improvement of the `DRR` after evaluation findings exist.

#### E.9.DA:4.3 - Ordinal coordinate scale

| Value | Label | Meaning for a `DRR` decision-adequacy coordinate |
|---:|---|---|
| 0 | `absent` | The coordinate is not expressed for the declared authoring use. |
| 1 | `namedOnly` | The coordinate is named or implied, but cannot carry decision reliance. |
| 2 | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, or too narrow. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The coordinate can carry the declared authoring use, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | The coordinate is clearly expressed with direct evidence and boundary protection. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The coordinate is exceptionally expressed across reinforcing loci and cases without hiding cost or neighbour loss. |

The value is a content evaluation of the `DRR` text and accepted source-use payload, not a reward for review, landing, popularity, citation volume, or absence of visible defects.

#### E.9.DA:4.4 - Required decision-adequacy coordinates

| Coordinate | Evaluation question |
|---|---|
| `BoundedDecisionQuestionRecoverability` | Can the reader recover the FPF content decision question named by value and adjacent questions outside it? |
| `SelectedAnswerDecisiveness` | Does the `DRR` decide the selected answer now rather than leave it for drafting? |
| `SourceUseAndDecisionInheritanceCarryThrough` | Does needed source use or accepted decision inheritance change selected answers, boundaries, obligations, cases, architecture choices, stops, or reopen conditions by value? |
| `AlternativeDispositionCompleteness` | Are selected, rejected, inherited, lineage-only, rationale-only, and outside-decision options closed for the declared use? |
| `SelectedLocusObligationClosure` | Are selected content responsibilities and explicit non-responsibilities assigned to selected loci named by value without unclassified selected loci, hidden ontic-candidate decisions, or precision-restoration profile defects that would become pasteable pattern prose? |
| `FPFContentArchitectureSelectionAdequacy` | Is the selected FPF content architecture substantively adequate: existing pattern, new pattern, candidate ontic, direct-pattern repair, publication-boundary repair, split, merge, selected content object, branch, and governing pattern for each outside claim, relation, or boundary? |
| `ArchitectureSourceAndViewLossClosure` | Are affected structures, structure kinds, structural views, view losses, source-return conditions, and splits among architecture decision, architecture description, publication, and ontic description decided when the decision uses them? |
| `DraftingActionability` | Can a pattern author recover the first substantive drafting content as this pattern's positive subject-kind and action spine, without mining copied boundary doctrine, reference boilerplate, phrase apparatus, or architecture-placement rationale for pattern prose? |
| `LexicalAndNamingClosure` | Are durable names, trigger words, and relation-like heads repaired through `E.10`, `F.18`, `A.6.P`, `C.2.P`, or the pattern that governs the relevant kind, claim, relation, or name? |
| `SoTAAndEvidenceUseInDecision` | Does each decision-governing source change a decision payload, and are non-SoTA source uses bounded? |
| `ScopeBoundaryAndNonOverread` | Are outside-decision items, inadmissible overreads, source-return conditions, and lost distinctions explicit without letting precision-restoration defects or architecture-memo leakage displace the selected answer? |
| `ConsequencesAndRegressionCoverage` | Are consequences, costs, validation obligations, source-loss regressions, regression cases, and near-misses enough to protect drafting? |
| `SiblingDecisionCoordination` | Is coordination with other `DRR`s, accepted decisions, or evaluation patterns explicit without duplication or weakening? |
| `AdministrativeStateAndAuthoringHistorySeparation` | Are review logistics, packet state, landing, monolith placement, chat history, and authoring history kept out of decision evidence? |
| `CorpusEcologyAndShadowSpecResistance` | Does the `DRR` assign repeated doctrine to governing patterns and avoid duplicate local variants or shadow specs? |

Coordinate separation is by repair question. One `DRR` section may support several coordinates, but the rationale must state the distinct property supported for each. When two heads always fail and repair together, the `DRR` or the evaluation pattern needs characteristic-space repair through `A.19.ECS`.

#### E.9.DA:4.4a - Result-row discipline and calibration

An `E.9.DA` result uses this table shape:

| Coordinate | Value | ShortRationale | EvidenceLocus |
|---|---:|---|---|
| `<E.9.DA coordinate>` | `<0..5>` | `<assigned-value basis; why the lower adjacent value would understate the DRR evidence; why the higher adjacent value would overstate it, or for 5 what would lower or reopen>` | `<DRR section, row, alternative, source-use row, selected-locus row, accepted-decision row, architecture decision, or missing locus named by value>` |

A prose summary, heading checklist, two-column coordinate-and-value table, or table without an `EvidenceLocus` named by value is not an `E.9.DA` result. It is draft evaluation material. Missing or unchecked evidence lowers the coordinate that needs it; it does not make the coordinate inactive.

Common calibration points:

| Coordinate family | `3` | `4` | `5` |
|---|---|---|---|
| Decision question and selected answer | The decision can guide limited drafting, but unsettled or ambiguous material remains visible. | The selected answer and outside questions are directly recoverable for declared authoring use. | The decision is reinforced across question, alternatives, consequences, selected loci, and first drafting action without hidden unsettled branches. |
| Source-use and inheritance | Sources or inherited decisions are relevant, but payload mutation or rejection is compact or incomplete. | Source-use role, adopted payload, rejected payload, currentness, and selected-locus obligation are explicit. | Source distinctions are replayable across selected answer, cases, boundaries, and first drafting action. |
| Selected-locus and architecture closure | Loci are named, but some obligation, non-obligation, split, architecture choice, ordinary reference relation, or phrase apparatus remains generic. | Loci named by value and content obligations are closed for declared use without precision-restoration defects or architecture-memo prose in the future pattern body. | The split, merge, governing pattern for outside claim, relation, or boundary, and lost or source-return distinctions are replayable across cases and consequences while product prose remains positive-subject first. |
| Drafting actionability | A skilled author can proceed, but must infer some first move, subject spine, boundary disposition, selected-locus relation, or reference or architecture disposition from scattered material. | The first substantive drafting content is the positive subject-kind and action spine; copied distinctions owned by other patterns are classified as pointers named by value or non-carried fanout; ordinary references stay as references; architecture rationale and phrase apparatus stay out of pattern prose; and pattern application remains explicit. | Drafting can proceed across heterogeneous selected loci without inventing decisions, final prose, local negative catalogs, reference boilerplate, phrase apparatus, or architecture-memo leakage. |

#### E.9.DA:4.5 - Status and stop condition

| Status | Meaning |
|---|---|
| `admissibleForDeclaredAuthoringUse` | The `DRR` can be used for the declared drafting, amendment, distribution, source-use, or accepted-decision carry-through. |
| `newFrameRequired` | The DRR appears useful only for a different decision, authoring use, selected-locus set, source-use claim, or qualification window than the declared one. This is not an admissible result for the current request; open a new `E.22` frame or repair the DRR. |
| `repairBeforeDrafting` | One or more coordinate floors fail for the declared authoring use. |
| `splitDecisionRequired` | Several coupled questions need separate decision records or explicit convergence. |
| `holdForArchitectureDecision` | Content object, branch, neighbour boundary, selected locus, structural view relation, source-return condition, or publication split must be decided before adequacy can close. |

`admissibleForDeclaredAuthoringUse` states the first drafting action and the most expansive non-admissible overread. `newFrameRequired` is not a pass for the current declared use. Non-ready statuses state the first repair, split boundary, or architecture question.

#### E.9.DA:4.6 - Compact result form

```text
E.9.DA result:
  DRR version: <DRRVersionRef>
  Declared authoring use: <DRRDeclaredAuthoringUse>
  Qualification window: <window>
  Evidence basis checked: <DRRDecisionAdequacyEvidenceBasis>
  Precision-restoration profile: <DRRPrecisionRestorationProfile>
  Status: <DRRDecisionAdequacyStatus>
  Coordinate table: <Coordinate | Value | ShortRationale | EvidenceLocus for every required coordinate>
  First drafting action or first repair: <...>
  Most expansive non-admissible overread: <...>
  Reopen if: <smallest changed locus or condition>
```

The coordinate table may be short. It is still complete. Status is not assigned from a prose summary, two-column table, applied-finding count, review acceptance, or result missing evidence loci needed by its values.

#### E.9.DA:4.7 - Finding row

```text
E.9.DA finding:
  DRR version: <DRRVersionRef>
  Declared authoring use: <DRRDeclaredAuthoringUse>
  Coordinate or status affected: <coordinate | status | stop condition>
  DRR locus: <section, row, alternative, source-use row, accepted-decision row>
  Value or status effect: <value, status, floor, or stop impact>
  Correction direction: <selected answer | selected locus | source-use payload | architecture choice | example | boundary | stop or reopen>
  Closure test: <what changed DRR text would show>
```

Vague labels such as `weak DRR`, `needs more evidence`, or `architecture unclear` are not findings until rewritten into this row.

When `E.22`, `E.23`, absorption, or exceptional-improvement framing asks for improvement, below-floor coordinates return findings or repair. Above-floor coordinates receive proposal rows only for substantive non-dominated decision-content opportunities inside the declared authoring use: a more decisive selected answer, source payload mutation, selected-locus obligation, architecture split or merge decision, rejected-alternative closure, first drafting action, regression case, or deletion or relocation of apparatus that would otherwise become pattern prose. Do not treat every value below `5` as a defect. A `4` may be the correct stop value only with loci showing why further decision-content movement is dominated, unavailable, or outside scope.

### E.9.DA:5 - Worked slices

**Weak precision-restoration DRR.** A `DRR` says `E.10`, `A.6.P`, and `C.2.P` are relevant, but does not decide whether a new branch exists, what name it has, which repeated prose moves, or which regression cases test the split. `SelectedAnswerDecisiveness`, `SelectedLocusObligationClosure`, `FPFContentArchitectureSelectionAdequacy`, and `DraftingActionability` fall.

**Adequate multi-locus DRR.** The `DRR` selects a new precision-restoration pattern, assigns selected content responsibilities to selected loci, states rejected alternatives, gives first drafting actions, and carries source-use payload into examples and conformance. It can be admissible for host drafting without containing final pattern prose.

**Architecture-impact DRR.** A `DRR` uses diagrams, graphs, dashboards, or architecture notes. The evaluation asks whether the `DRR` decided the architecture or structure claim, structural view relation, preserved and lost structure, source-return condition, selected loci, and publication boundary. The description locates material; it is not the FPF decision.

### E.9.DA:6 - Bias annotation

This pattern biases FPF toward decisions before drafting. The bias is useful because missing decisions become expensive once they fan out into pattern hosts.

The bias is bounded. Small editorial decisions can use `E.9` directly. Pattern quality remains under `E.21`; repeated improvement remains under `E.23`; wording repair remains under `E.10` and precision-restoration neighboring patterns named by value.

### E.9.DA:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E9DA-1` | Name `DRRVersionRef`, declared authoring use, selected-locus disposition map, and qualification window. |
| `CC-E9DA-2` | Evaluate every coordinate in `E.9.DA:4.4` with value, short rationale, and evidence locus, using the required result-row shape. |
| `CC-E9DA-3` | Justify values from `DRR` decision content and accepted source-use payload, not administrative state or reputation. |
| `CC-E9DA-4` | State `DRRDecisionAdequacyStatus`, first drafting action or first repair, bounded non-use, and reopen condition. |
| `CC-E9DA-5` | Keep `DRR` adequacy distinct from pattern quality, review pass, release state, evidence, assurance, gate, and project work. |
| `CC-E9DA-6` | Apply `E.10` to decision-governing names, coordinates, status values, examples, stop conditions, and finding wording introduced or repaired by the evaluation. |
| `CC-E9DA-6a` | Record `DRRPrecisionRestorationProfile` before assigning or accepting values: word-use precision goes to `E.10`, `E.10.ARCH`, `F.18`, or a governing pattern; phrase apparatus goes to `F.19`; repetition-and-distribution, ontic-slot clarity, description-publication-source boundary separation, and pattern-application ontology are classified by their governing pattern; boilerplate stays out of future pattern prose. |
| `CC-E9DA-6b` | For any proposed wording, naming, or precision-restoration repair, record `DRRKindRestorationCheck`. The repair is not adequate if it only removes a trigger word or substitutes a cleaner phrase while changing, narrowing, widening, flattening, or losing the governed kind, relation, claim kind, slot or use-position, admissible use, or scope without an accepted semantic decision and governing-pattern reference when another pattern governs the kind under repair, relation, claim, or position. |
| `CC-E9DA-6c` | When a `DRR` selects, rejects, splits, or declines a candidate ontic or an ontic-publication boundary, evaluate `DRROnticCandidateDisposition`: candidate `EntityOfConcern`, sufficiency rationale, rejected alternatives, candidate-universe sanity sweep when the claim is broad, slot-relation boundary, description-publication boundary, and selected pattern placement by value. Missing disposition lowers `SelectedAnswerDecisiveness`, `SelectedLocusObligationClosure`, `FPFContentArchitectureSelectionAdequacy`, and `DraftingActionability`. |
| `CC-E9DA-7` | State source contribution by payload mutation when a source governs a decision. |
| `CC-E9DA-8` | State what became worse if visible decision-adequacy values improved. |
| `CC-E9DA-9` | State the `DRRDecisionAdequacyEvidenceBasis`; if source-currentness, accepted-decision inheritance, selected-locus, architecture, or comparator evidence is missing or unchecked, lower the coordinate that needs it. |
| `CC-E9DA-10` | Use adjacent-value calibration when assigning `3`, `4`, or `5`; a rationale must distinguish the assigned value from its lower and higher neighbours. |
| `CC-E9DA-11` | Keep ordinal values as measurement results, not repair targets. Below-floor values require decision-content findings or repair. Above-floor improvement requires substantive non-dominated proposal rows when requested; it cannot close by adding source volume, selected-locus tables, boundary catalogues, quality proof, or process evidence that does not make the `DRR` decision more decisive for its declared authoring use. A no-proposal or stay-at-current-value disposition must name loci and why no worthwhile decision-content move remains. |

### E.9.DA:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Heading-complete DRR.** Headings exist but authors cannot tell what to write. | Lower selected-answer, selected-locus, and drafting-action coordinates. |
| **Source packet in DRR clothing.** Sources are preserved but FPF decisions are absent. | State selected payload, rejected payload, and selected-locus obligations. |
| **Address completion without architecture.** Every locus is named but the split or merge is wrong. | Repair `FPFContentArchitectureSelectionAdequacy`. |
| **Watch item as decision.** Drafting is expected to choose the answer during pattern authoring. | Select, repair, split, or hold. |
| **Ontic candidate left to drafting.** A `DRR` uses uncertain candidate phrasing for a concept cluster or pattern set but leaves candidate sufficiency, rejected alternatives, publication boundary, and placement for the pattern author. | Close `DRROnticCandidateDisposition` now: select, reject, split, or decline the candidate by value; state the direct governing pattern when no new ontic is warranted. |
| **Review-state proxy.** Review acceptance or landing is treated as adequacy. | Use decision-content evidence only. |
| **Adequacy table without evidence loci.** Values are listed without by-value `DRR` or source loci. | Re-run the evaluation with `Coordinate | Value | ShortRationale | EvidenceLocus`; lower any coordinate whose evidence cannot be named. |
| **Apparatus-overwrapped drafting payload.** The `DRR` offers selected-pattern wording wrapped in role, publication-form, locus, flow, state, status, text, package, or process apparatus without changing a recoverable kind, relation, claim kind, admissible use, evidence value, selected locus, user-facing action, or flow role. | Classify the wording under `F.19`. If it changes a kind or claim, repair through precision restoration; if not, remove it from the future pattern payload or rewrite it as the positive subject-kind and action spine. |
| **Goodharted DRR adequacy.** A `DRR` is made easier to defend as `4` or `5` by adding source rows, selected-locus tables, boundary catalogues, or review proof, while selected answer, selected-locus obligations, source payload mutation, architecture choice, or first drafting action do not improve. | Reject apparatus-only improvement; apply `E.13` when adequacy values or review marks are replacing decision usefulness; repair the decision content, delete or relocate proof material, and record checked no-proposal only when no non-dominated decision-content improvement remains. |

### E.9.DA:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| DRR adequacy becomes inspectable before drafting. | Pattern authors get decisions, not source summaries. | Every opened `E.9.DA` evaluation touches all coordinates. |
| Architecture selection becomes visible. | By-value but wrong split or merge choices no longer pass as complete distribution. | Some DRRs need architecture repair before drafting. |
| Source mutation is explicit. | SoTA, standards, reviews, audits, and accepted decisions shape decisions rather than decorate them. | Rationale-only sources cannot raise values. |

### E.9.DA:10 - Rationale

The cheapest place to repair missing FPF decisions is the `DRR`, before pattern prose spreads uncertainty across several hosts. A compact complete evaluation is better than a heavy preliminary audit: it gives every coordinate a value, identifies the first repair, and stops.

### E.9.DA:11 - SoTA-Echoing

| Claim | Practice basis | Local adoption |
|---|---|---|
| DRR adequacy is decision-content adequacy, not template completeness. | Architecture-description and ADR traditions keep concerns, alternatives, decisions, rationale, and consequences inspectable. | The `DRR` must carry selected answers, alternatives, consequences, and selected-locus decisions. |
| Multi-host FPF changes need selected-locus disposition. | Lightweight ADR practice is useful but too central-record-oriented for multi-pattern FPF changes. | `DRRSelectedLocusDispositionMap` states obligations and non-obligations by locus. |
| Feedback needs desired condition, current condition, next action, and tactics. | Sadler and Hattie and Timperley feedback traditions, carried through `E.22` and `E.23`. | `ShortRationale`, evidence locus, finding and proposal rows, and checked no-proposal dispositions stay separate. |
| Source evidence must mutate the decision. | Current FPF `E.8`, `E.19`, `E.21`, and living-source discipline require non-decorative source use. | `SoTAAndEvidenceUseInDecision` checks changed decision payload, not citation presence. |
| Improvement remains multi-coordinate and trade-off sensitive. | MCDA, Pareto, and QD, OEE, and NQD lines inherited through `E.22` and `E.23`. | The evaluation asks what became worse and keeps repeated improvement outside `E.9.DA`. |
| Decision-adequacy measures can become targets. | Goodhart and Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines. | `E.9.DA` forbids all-`5` or `5-defensible` repair targeting; values rise only when decision content becomes stronger for declared authoring use, and `E.13` governs any proxy-to-value claim about those values. |

### E.9.DA:12 - Relations

| Pattern | Relation |
|---|---|
| `E.9` | Defines the `DRR` kind and minimum form. |
| `E.8` | Receives authored pattern bodies after accepted decisions. |
| `E.21` | Evaluates resulting pattern versions, not `DRR` adequacy. |
| `E.22` | Frames the evaluation purpose when needed. |
| `E.23` | Runs repeated improvement of a `DRR` after findings or proposal rows exist. |
| `E.13` | Governs pragmatic utility and proxy-to-value alignment when `DRR` adequacy values, review marks, source-counts, or discharge evidence become substitutes for decision usefulness. |

| `E.19` | May return findings that expose upstream `DRR` defects. |
| `E.10`, `A.6.P`, `C.2.P`, `C.16.Q`, `F.18` | Govern wording, relation, episteme, quality-term, and naming repair. |
| `C.16`, `A.17`, `A.18`, `A.19`, `C.25` | Govern characteristic, scale, measurement, characteristic-space, and quality-bundle claims. |
| Architecture-facing FPF patterns | Receive architecture, structure, view, graph, publication, and source-use distinctions when the `DRR` decision uses them. |

### E.9.DA:End

