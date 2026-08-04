## E.9.DA - DRR Decision-Adequacy Evaluation CharacteristicSpace

Status: Core.

### E.9.DA:1 - Problem frame

Use `E.9.DA` when one exact C.2.1 `DRR` episteme must be assessed for decision adequacy under a declared FPF authoring use: pattern drafting, host amendment, selected-locus distribution, accepted-decision carry-through, source-use carry-through, scope-boundary decision, split decision, or architecture-hold decision. E.9.DA supplies the object-specific evaluation characteristic space and result rules; it does not itself perform that assessment.

Not this pattern when the evaluated object is one authored pattern version, one admission or refresh review, one local wording repair, or a measurement-law problem. Use `E.21`, `E.19`, `E.10` and its precision-restoration neighbours, or `C.16`, `A.17`, `A.18`, and `A.19` for those objects.

First useful move: identify the exact checked `DRR` episteme, declared authoring use, `U.ClaimScope`, selected-locus disposition map, qualification window, and E.9.DA evaluation configuration. When an actual result is required, identify the evaluator system, role assignment, semantic evaluation method, dated assessment work, and A.6.1 application/bindings before constituting coordinate-result claims.

What goes wrong if missed: a formally valid `DRR` may still be too weak for drafting. It may summarize sources instead of deciding, mention neighbours without obligations, hide rejected alternatives, leave trigger words unresolved, or omit the first drafting action.

Primary EntityOfConcern in plain terms: one exact C.2.1 `DRR` episteme version assessed for one declared FPF authoring use and qualification window. The assessment work, result episteme, witness/evidence set, optional record, status use, assurance, acceptance, and later repair are separate objects.

### E.9.DA:2 - Problem

`E.9` defines `DRRMethod`, the decision-work/selected-answer boundary, and the minimum C.2.1 DRR episteme form. It does not by itself establish whether one exact DRR episteme is decision-bearing enough for a declared downstream use. Without `E.9.DA`, assessors tend to approve headings, source volume, or clean prose while the pattern author still has to invent missing decisions.

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

`E.9.DA` declares the reusable DRR decision-adequacy evaluation `CharacteristicSpace`, its object-specific evaluation specification, ordinal scale, result-shape rules, and local admissible-use result values. It is a specialization of `A.19.ECS`; it does not itself inspect a DRR, perform assessment work, assign a value, create evidence use, issue assurance, authorize drafting, or repair the DRR.

For an actual evaluation, keep these objects independently recoverable:

1. one exact C.2.1 `DRR` episteme version as the checked object;
2. the declared downstream authoring use, `U.ClaimScope`, qualification window, selected-locus disposition map, and checked evidence basis;
3. the selected `U.CharacteristicSpace`, this E.9.DA evaluation-specification episteme, every coordinate/scale binding, and the local result-form and status-value rules;
4. one separately identified semantic evaluation `U.Method` used for the assessment;
5. dated assessment `U.Work`, its evaluator `U.System`, exact obtaining `U.RoleAssignment`, enacted method, and A.6.1 application/bindings;
6. the per-coordinate result claims and one C.2.1 aggregate decision-adequacy-result episteme when a durable result is needed;
7. witnesses, source or comparator refs, exact A.10 evidence-use/provenance relations, and any B.3 assurance result;
8. an optional evaluation-record episteme that packages those refs without performing the assessment or creating its results;
9. any F.10 status value, status-use/interpretation relation, acceptance, gate, authority, reliance, publication, or currentness claim; and
10. later E.23 improvement or other DRR repair work and its changed DRR episteme.

There is no partial conforming `E.9.DA` result. Once assessment work applies this evaluation for the declared use, the aggregate result episteme states a value, adjacent-value rationale, and evidence locus for every coordinate in `E.9.DA:4.4`, the checked evidence basis, and the local result status. Missing fields, sources, selected-locus decisions, architecture decisions, comparators, or currentness bases lower the coordinate that needs them and can yield repair, split, or hold; an unfinished table or prose impression remains assessment material rather than a result.

Each coordinate-result claim is a quality ascription about the exact checked DRR episteme. It names that bearer, effective ReferenceScheme, characteristic and scale value, evaluation rule or probe, comparison/calibration frame when used, `U.ClaimScope`, declared use and qualification window, assessment application, and evidence locus. Evaluator system and any viewpoint episteme remain distinct; the result does not acquire a viewpoint or grounding merely from the evaluator, record, or source labels.

#### E.9.DA:4.1 - Local names and kind settlement

| Local name | Kind and function |
|---|---|
| `DRRDecisionAdequacyEvaluation` | Compatibility compound label for the full evaluation package. Any use resolves to the exact configuration, assessment application/work, result episteme, witnesses/evidence-use relations, and optional record rather than treating this label as one kind or actor. |
| `DRRDecisionAdequacyCharacteristicSpaceRef` | Reference to the exact A.19 `U.CharacteristicSpace` whose slots are the required E.9.DA coordinates and whose scale bindings use `E.9.DA:4.3`; not an assessment, result, or record. |
| `DRRDecisionAdequacyEvaluationSpecRef` | Reference to this object-specific A.19.ECS evaluation-specification episteme: applicability, coordinates, scale meanings, evidence/missingness rules, result shape, calibration, status meanings, and reopen conditions. |
| `DRRVersionRef` | Exact C.2.1 `DRR` episteme version named by value as the checked object. |
| `DRRDeclaredAuthoringUse` | Downstream FPF authoring use for which that exact DRR episteme is assessed. |
| `DRRSelectedLocusDispositionMap` | Map from selected loci named by value to selected content responsibilities, explicit non-responsibilities, sibling decisions, or outside-decision dispositions. |
| `DRRDecisionAdequacyQualificationWindow` | Edition, source set, accepted-decision record, neighbour condition, and currentness window for which the result claim holds. |
| `DRRDecisionAdequacyCoordinateSet` | The required coordinates in this pattern, each bound to the ordinal scale and its local evidence rule. |
| `DRRDecisionAdequacyEvaluationConfiguration` | Local input tuple binding the exact checked DRR, declared use and scope, characteristic space/specification, semantic evaluation method, selected-locus map, evidence basis, and qualification window. It is neither a new U-kind nor performed work. |
| `DRRDecisionAdequacyAssessmentWorkRef` | Exact dated A.15.1 `U.Work` that performs the assessment under a role assignment and enacted semantic evaluation method. |
| `DRRDecisionAdequacyApplicationRef` | Exact A.6.1 application and actual bindings connecting the assessment work, checked DRR, evaluation configuration, and returned coordinate values/result refs. |
| `DRRDecisionAdequacyEvidenceBasis` | Checked DRR, source, accepted-decision, selected-locus, architecture, currentness, and neighbour loci named by value; not evidence use merely by inclusion. |
| `DRRCoordinateValueRationales` | Required result claims: coordinate, value, adjacent-value rationale, and evidence locus named by value. |
| `DRRCoordinateLocusRefs` | Exact DRR loci cited by result claims; citation does not itself establish a value. |
| `DRRSourceUseDischargeMap` | Source-use relation, source-currentness, selected payload, rejected payload, and selected locus when a source publication, source pack, or source-use record governs a decision. |
| `DRRPrecisionRestorationProfile` | Compact scalar profile for DRR wording-use precision: word-use precision, phrase apparatus, repetition-and-distribution, ontic-slot clarity, description-publication-source boundary separation, and pattern-application ontology. It records overall effect, affected coordinates, selected governing pattern, and no-repair disposition with loci when clean. |
| `DRRKindRestorationCheck` | Required pre-repair and post-repair object-kind, relation-or-claim-kind, current ontic slot, relation position, use relation, or claim kind, admissible-use, and scope check, or `not triggered`, `ordinary prose`, `already satisfied`, or `blocker` disposition with loci, for any DRR wording, naming, or precision-restoration repair proposal. |
| `DRROnticCandidateDisposition` | If the DRR selects, rejects, splits, or declines a candidate ontic, this names the candidate `EntityOfConcern`, sufficiency rationale, rejected alternatives, broad candidate-universe sanity sweep when the claim is broad, slot-relation boundary, description-publication boundary, and selected pattern placement by value. |
| `CampaignProblemSolutionUnfoldingCheck` | Triggered carry-through check for DRRs that create or modify README entries, path-shaped patterns, pattern families, DPF entries, first-practical routes, or constraint-governed unfolding structures. It names admitted problem-side record refs or cues, accepted starting records, current starting structures, entry cues, selected solution architecture, affected unfolding families, loci and governing-pattern map added or changed, blocked overreads, and residue that must move from DRR or README into patterns or unfolding structures. |
| `DRRDecisionAdequacyResultRef` | One C.2.1 result episteme whose EntityOfConcern is the exact checked DRR episteme and whose ClaimGraph states the declared use/window, all coordinate-result claims, local status value, stop/repair condition, and bounded overread. It is not the work, witness set, record, or authority. |
| `DRRDecisionAdequacyWitnessRefs` | Exact comparison, source, trace, case, or locus witnesses cited by result claims; witness presence is neither a value nor an evidence-use relation. |
| `DRRDecisionAdequacyEvidenceUseRefs` | Exact A.10 evidence-use/provenance relations supporting reliance on result claims; they do not create those claims or the checked DRR. |
| `DRRDecisionAdequacyRecordRef` | Optional C.2.1 record episteme that packages configuration, work/application, result, witness/evidence, non-use, and reopen refs; it performs no assessment and grants no status or authority. |
| `DRRDecisionAdequacyStatus` | Local admissible-use value asserted by the aggregate result episteme. Any F.10 status use or interpretation by a receiver is a separate relation. |

These names are local evaluation positions and refs. They are not release state, review status, project evidence, gate result, assurance, work, publication, or pattern-quality values.

#### E.9.DA:4.2 - Evaluation application, result, and optional record

```text
DRRDecisionAdequacyEvaluationConfiguration:
  DRRVersionRef: <exact C.2.1 DRR episteme>
  DRRDeclaredAuthoringUse: <drafting | amendment | distribution | source-use carry-through | accepted-decision carry-through | split or hold decision>
  ClaimScopeRef: <exact U.ClaimScope>
  DRRSelectedLocusDispositionMap: <locus -> selected responsibility, explicit non-responsibility, sibling decision, or outside-decision disposition>
  DRRDecisionAdequacyQualificationWindow: <source, edition, neighbour, currentness window>
  DRRDecisionAdequacyCharacteristicSpaceRef: <exact A.19 space>
  DRRDecisionAdequacyEvaluationSpecRef: <this E.9.DA specification edition>
  SemanticEvaluationMethodRef: <exact U.Method used by assessment work>
  DRRDecisionAdequacyEvidenceBasis: <checked loci and explicitly missing or unchecked loci>

DRRDecisionAdequacyAssessmentApplication:
  AssessmentWorkRef: <dated U.Work>
  EvaluatorSystemRef:
  EvaluatorRoleAssignmentRef:
  EnactedMethodRef: <same SemanticEvaluationMethodRef>
  A6_1ApplicationAndBindingRefs:
  EvaluationConfigurationRef:
  ReturnedCoordinateResultRefs:
  AggregateResultRef:

DRRDecisionAdequacyResultEpisteme:
  EntityOfConcern: <same exact DRRVersionRef>
  EffectiveReferenceScheme:
  ClaimGraph:
    DeclaredAuthoringUse:
    QualificationWindow:
    CoordinateTable: <all coordinates, values, adjacent-value rationales, evidence loci>
    PrecisionRestorationProfile:
    KindRestorationChecks:
    OnticCandidateDisposition: <when triggered>
    CampaignProblemSolutionUnfoldingCheck: <when triggered>
    DRRDecisionAdequacyStatus:
    FirstDraftingActionOrFirstRepair:
    MostExpansiveNonAdmissibleOverread:
    StopOrRepairCondition:
    ReopenIf:
  WitnessRefs:
  EvidenceUseRelationRefs:
```

An optional `DRRDecisionAdequacyRecordRef` may package refs to this configuration, assessment application/work, result episteme, witnesses, evidence-use relations, publication, and currentness. Filling or publishing that record does not perform the work, assign the coordinate values, make evidence relevant, confer assurance, create an F.10 status use, accept the DRR, or authorize downstream drafting.

`E.22` may frame whether the evaluation is floor-only, exceptional-improvement, trade-off, open-question, absorption, or proposal-producing. It neither performs the assessment nor assigns the result. `E.23` governs later repeated improvement work on the checked DRR after result claims or findings exist; it does not retroactively become the E.9.DA assessment.

#### E.9.DA:4.3 - Ordinal coordinate scale

| Value | Label | Meaning for a `DRR` decision-adequacy coordinate |
|---:|---|---|
| 0 | `absent` | The coordinate is not expressed for the declared authoring use. |
| 1 | `namedOnly` | The coordinate is named or implied, but cannot carry decision reliance. |
| 2 | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, or too narrow. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The coordinate can carry the declared authoring use, with limits visible. |
| 4 | `wellExpressedForDeclaredUse` | The coordinate is clearly expressed with direct evidence and boundary protection. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The coordinate is exceptionally expressed across reinforcing loci and cases without hiding cost or neighbour loss. |

Each ordinal value is a content-evaluation result claim about the exact checked DRR episteme under the declared evaluation configuration. It is not a `U.Measure`, assessment work, witness, record field, F.10 status use, assurance, acceptance, or reward for review, landing, popularity, citation volume, or absence of visible defects.

#### E.9.DA:4.4 - Required decision-adequacy coordinates

| Coordinate | Evaluation question |
|---|---|
| `BoundedDecisionQuestionRecoverability` | Can the reader recover the FPF content decision question named by value and adjacent questions outside it? |
| `SelectedAnswerDecisiveness` | Does the `DRR` decide the selected answer now rather than leave it for drafting? |
| `SourceUseAndDecisionInheritanceCarryThrough` | Does needed source use or accepted decision inheritance change selected answers, boundaries, obligations, cases, architecture choices, stops, or reopen conditions by value? |
| `AlternativeDispositionCompleteness` | Are selected, rejected, inherited, lineage-only, rationale-only, and outside-decision options closed for the declared use? |
| `SelectedLocusObligationClosure` | Are selected content responsibilities and explicit non-responsibilities assigned to selected loci named by value without unclassified selected loci, hidden ontic-candidate decisions, or precision-restoration profile defects that would become pasteable pattern prose? |
| `FPFContentArchitectureSelectionAdequacy` | Is the selected FPF content architecture substantively adequate: existing pattern, new pattern, candidate ontic, direct-pattern repair, publication-boundary repair, split, merge, selected content object, branch, and governing pattern for each outside claim, relation, or boundary? |
| `ArchitectureSourceAndViewLossClosure` | Are affected structures, structure kinds, structural views, view losses, missing-structure return conditions, source-use relations, and splits among architecture decision, architecture description, publication, and ontic description decided when the decision uses them? |
| `DraftingActionability` | Does the DRR expose the governed `EntityOfConcern`, first substantive drafting move, exact selected-locus claim/relation/boundary or decision, user-facing action, and only the necessary boundary/reference pointers as positive subject kind and action guidance, without making an evaluation row, copied boundary doctrine, reference boilerplate, phrase apparatus, or architecture-placement rationale stand for future pattern method or work? |
| `LexicalAndNamingClosure` | Are durable names, trigger words, and relation-like heads repaired through `E.10`, `F.18`, `A.6.P`, `C.2.P`, or the pattern that governs the relevant kind, claim, relation, or name? |
| `SoTAAndEvidenceUseInDecision` | Does each decision-governing source change a decision payload, and are non-SoTA source uses bounded? |
| `ScopeBoundaryAndNonOverread` | Are outside-decision items, inadmissible overreads, source-use or missing-structure return conditions, and lost distinctions explicit without letting precision-restoration defects or architecture-memo leakage displace the selected answer? |
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
| Source-use and inheritance | Sources or inherited decisions are relevant, but payload mutation or rejection is compact or incomplete. | Source-use relation, adopted payload, rejected payload, currentness, and selected-locus obligation are explicit. | Source distinctions are replayable across selected answer, cases, boundaries, and first drafting action. |
| Selected-locus and architecture closure | Loci are named, but some obligation, non-obligation, split, architecture choice, ordinary reference relation, or phrase apparatus remains generic. | Loci named by value and content obligations are closed for declared use without precision-restoration defects or architecture-memo prose in the future pattern body. | The split, merge, governing pattern for outside claim, relation, or boundary, and lost-structure or source-use distinctions are replayable across cases and consequences while product prose remains positive-subject first. |
| Drafting actionability | A skilled author can proceed, but must infer some governed `EntityOfConcern`, first move, selected-locus relation/decision, user-facing action, boundary disposition, or reference/architecture disposition from scattered material. | The DRR directly exposes the governed `EntityOfConcern`, first substantive drafting move, exact selected-locus relation or decision, user-facing action, and only necessary boundary/reference pointers as positive subject kind and action guidance; ordinary references remain references, apparatus stays out of pattern prose, and an evaluation row is neither future method nor work. | Drafting can proceed across heterogeneous selected loci without inventing decisions, final prose, local negative catalogues, reference boilerplate, phrase apparatus, architecture-memo leakage, method, or work. |

#### E.9.DA:4.5 - Local result status and stop condition

The following are closed values asserted in the aggregate decision-adequacy-result episteme for its exact checked DRR/use/window. They are not F.10 status uses, review decisions, gates, permissions, assurance levels, or work states. A receiver that relies on or maps one value must state its own exact status-use/interpretation or evidence-use relation.

| Status | Meaning |
|---|---|
| `admissibleForDeclaredAuthoringUse` | The result claims that the checked DRR can support the declared drafting, amendment, distribution, source-use, or accepted-decision carry-through within the stated window. The value alone neither accepts the DRR nor authorizes that downstream work. |
| `newFrameRequired` | The DRR appears useful only for a different decision, authoring use, selected-locus set, source-use claim, or qualification window than the declared one. This is not an admissible result for the current request; open a new `E.22` frame or repair the DRR. |
| `repairBeforeDrafting` | One or more coordinate floors fail for the declared authoring use. |
| `splitDecisionRequired` | Several coupled questions need separate decision records or explicit convergence. |
| `holdForArchitectureDecision` | Content object, branch, neighbour boundary, selected locus, structural view relation, missing-structure return condition, source-use relation, or publication split must be decided before adequacy can close. |

A result carrying `admissibleForDeclaredAuthoringUse` states the first drafting action and most expansive non-admissible overread. `newFrameRequired` is not a pass for the current declared use. Non-ready result values state the first repair, split boundary, or architecture question; the result episteme neither performs that repair nor imposes a gate without a separately governed receiving relation.

#### E.9.DA:4.6 - Compact result form

```text
E.9.DA result episteme:
  ResultRef: <DRRDecisionAdequacyResultRef>
  EntityOfConcern: <exact DRRVersionRef>
  EffectiveReferenceScheme:
  Declared authoring use: <DRRDeclaredAuthoringUse>
  ClaimScopeRef:
  Qualification window: <window>
  Evaluation configuration: <CharacteristicSpaceRef, EvaluationSpecRef, SemanticEvaluationMethodRef>
  Assessment work and A.6.1 application refs:
  Evidence basis checked: <DRRDecisionAdequacyEvidenceBasis>
  Precision-restoration profile: <DRRPrecisionRestorationProfile>
  Status: <local DRRDecisionAdequacyStatus value>
  Coordinate table: <Coordinate | Value | ShortRationale | EvidenceLocus for every required coordinate>
  Witness refs and exact evidence-use relation refs:
  First drafting action or first repair: <...>
  Most expansive non-admissible overread: <...>
  Reopen if: <smallest changed locus or condition>
```
The coordinate table may be short, but the result episteme is complete only when every coordinate and required identity/configuration field is recoverable. No result is constituted from a prose summary, two-column table, applied-finding count, review acceptance, absent failure rows, or missing evidence loci. A downstream F.10 status use, B.3 assurance, E.19 admission decision, authority, or drafting permission is a separate governed claim.

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

Vague labels such as `weak DRR`, `needs more evidence`, or `architecture unclear` are not findings until rewritten into this row. A finding row is one actionable evaluation-result claim or a row cited by the aggregate result episteme; writing it neither performs assessment work nor repairs the checked DRR.

When `E.22`, `E.23`, absorption, or exceptional-improvement framing requests improvement, below-floor coordinate-result claims support finding rows and subsequent repair work; they do not themselves repair the DRR. Above-floor coordinates receive proposal rows only for substantive non-dominated decision-content opportunities inside the declared authoring use: a more decisive selected answer, source payload mutation, selected-locus obligation, architecture split or merge decision, rejected-alternative closure, first drafting action, regression case, or deletion or relocation of apparatus that would otherwise become pattern prose. Do not treat every value below `5` as a defect. A `4` may be the correct stop value only with loci showing why further decision-content movement is dominated, unavailable, or outside scope.

### E.9.DA:5 - Worked slices

**Weak precision-restoration DRR.** A checked DRR episteme says `E.10`, `A.6.P`, and `C.2.P` are relevant, but does not decide whether a new branch exists, what name it has, which repeated prose moves, or which regression cases test the split. Its aggregate assessment result assigns lower values to `SelectedAnswerDecisiveness`, `SelectedLocusObligationClosure`, `FPFContentArchitectureSelectionAdequacy`, and `DraftingActionability`.

**Adequate multi-locus DRR.** The checked DRR episteme records a selected precision-restoration pattern, responsibilities for selected loci, rejected alternatives, first drafting actions, and source-use payload carried into examples and conformance. Dated assessment work enacts the selected semantic evaluation method; the A.6.1 application returns value bindings, and the separate aggregate result episteme can state `admissibleForDeclaredAuthoringUse` without the DRR containing final pattern prose. A separately governed receiving decision determines whether drafting proceeds.

**Architecture-impact DRR.** A checked DRR episteme cites diagrams, graphs, dashboards, or architecture notes. Assessment work applies the E.9.DA configuration to determine whether its decision claims settle the architecture or structure claim, structural-view relation, preserved and lost structure, missing-structure return condition or source-use relation, selected loci, and publication boundary. A description locates material; it is neither the decision nor the assessment result.

### E.9.DA:6 - Bias annotation

This pattern biases FPF toward decisions before drafting. The bias is useful because missing decisions become expensive once they fan out into pattern hosts.

The bias is bounded. Small editorial decisions can use `E.9` directly. Once an E.9.DA assessment application is current, dated assessment work enacts the selected method, A.6.1 bindings return coordinate values, and a separate result episteme states the claims compactly; the pattern and optional record perform none of those acts. Pattern quality remains under `E.21`; repeated improvement remains under `E.23`; wording repair remains under `E.10` and precision-restoration neighboring patterns named by value.

### E.9.DA:7 - Conformance checklist

| Check | Requirement |
|---|---|
| `CC-E9DA-0` | Keep the exact checked DRR episteme, evaluation characteristic space/specification, semantic evaluation method, dated assessment work and A.6.1 application, coordinate/result episteme, witnesses/evidence use, optional record, local status value, downstream status use/assurance/authority, and later repair independently recoverable. |
| `CC-E9DA-0a` | Constitute any durable aggregate result under C.2.1 with the exact checked DRR episteme as EntityOfConcern, an effective ReferenceScheme, and a ClaimGraph carrying the declared use/window, complete coordinate claims, local status, stop/repair, bounded overread, and reopen condition. |
| `CC-E9DA-1` | Name the exact `DRRVersionRef`, declared authoring use, `U.ClaimScope`, selected-locus disposition map, qualification window, characteristic-space/spec refs, and semantic evaluation method in the evaluation configuration. |
| `CC-E9DA-2` | Identify the dated assessment work, evaluator system and obtaining role assignment, enacted method, and A.6.1 application/bindings; constitute a separate result claim for every coordinate with value, adjacent-value rationale, and evidence locus. |
| `CC-E9DA-3` | Justify values from `DRR` decision content and accepted source-use payload, not administrative state or reputation. |
| `CC-E9DA-4` | In the aggregate result episteme state the local `DRRDecisionAdequacyStatus` value, first drafting action or first repair, bounded non-use, and reopen condition. Keep any receiving status use, assurance, acceptance, gate, authority, or permission separate. |
| `CC-E9DA-5` | Keep DRR adequacy result claims distinct from the checked DRR, assessment work/application, witnesses and evidence-use relations, optional record/publication, pattern quality, E.19 admission, review or release state, assurance, gate, project work, and later repair. |
| `CC-E9DA-6` | Apply `E.10` to decision-governing names, coordinates, status values, examples, stop conditions, and finding wording introduced or repaired by the evaluation. |
| `CC-E9DA-6a` | Record `DRRPrecisionRestorationProfile` before assigning or accepting values: word-use precision goes to `E.10`, `E.10.ARCH`, `F.18`, or a governing pattern; phrase apparatus goes to `F.19`; repetition-and-distribution, ontic-slot clarity, description-publication-source boundary separation, and pattern-application ontology are classified by their governing pattern; boilerplate stays out of future pattern prose. |
| `CC-E9DA-6b` | For any proposed wording, naming, or precision-restoration repair, record `DRRKindRestorationCheck`. The repair is not adequate if it only removes a trigger word or substitutes a cleaner phrase while changing, narrowing, widening, flattening, or losing the governed kind, relation, claim kind, current ontic slot, relation position, use relation, or claim kind, admissible use, or scope without an accepted semantic decision and governing-pattern reference when another pattern governs the kind under repair, relation, claim, or position. |
| `CC-E9DA-6c` | When a `DRR` selects, rejects, splits, or declines a candidate ontic or an ontic-publication boundary, evaluate `DRROnticCandidateDisposition`: candidate `EntityOfConcern`, sufficiency rationale, rejected alternatives, candidate-universe sanity sweep when the claim is broad, slot-relation boundary, description-publication boundary, and selected pattern placement by value. Missing disposition lowers `SelectedAnswerDecisiveness`, `SelectedLocusObligationClosure`, `FPFContentArchitectureSelectionAdequacy`, and `DraftingActionability`. |
| `CC-E9DA-6d` | When first-entry, route-shaped, path-shaped, DPF, pattern-family, or unfolding-structure material is selected by the DRR, evaluate `CampaignProblemSolutionUnfoldingCheck`. If the selected solution architecture remains only in the DRR or public README after drafting, lower `SourceUseAndDecisionInheritanceCarryThrough`, `SelectedLocusObligationClosure`, `DraftingActionability`, and `CorpusEcologyAndShadowSpecResistance` as applicable. |
| `CC-E9DA-7` | State source contribution by payload mutation when a source governs a decision. |
| `CC-E9DA-8` | State what became worse if visible decision-adequacy values improved. |
| `CC-E9DA-9` | State the `DRRDecisionAdequacyEvidenceBasis`; if source-currentness, accepted-decision inheritance, selected-locus, architecture, or comparator evidence is missing or unchecked, lower the coordinate that needs it. |
| `CC-E9DA-10` | Use adjacent-value calibration when assigning `3`, `4`, or `5`; a rationale must distinguish the assigned value from its lower and higher neighbours. |
| `CC-E9DA-11` | Keep ordinal values as ordinal content-evaluation result claims, not repair targets. Below-floor values require decision-content findings or repair. Above-floor improvement requires substantive non-dominated proposal rows when requested; it cannot close by adding source volume, selected-locus tables, boundary catalogues, quality proof, or process evidence that does not make the `DRR` decision more decisive for its declared authoring use. A no-proposal or stay-at-current-value disposition must name loci and why no worthwhile decision-content move remains. |

### E.9.DA:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Specification or record as evaluator.** A filled coordinate table, published record, or E.9.DA pattern is said to have assessed the DRR, issued assurance, accepted it, or authorized drafting. | Recover the evaluator assignment, semantic method, dated assessment work, A.6.1 application, result episteme, witnesses/evidence-use relations, and receiving authority separately; let the optional record package refs only. |
| **Heading-complete DRR.** Headings exist but authors cannot tell what to write. | Lower selected-answer, selected-locus, and drafting-action coordinates. |
| **Source packet in DRR clothing.** Sources are preserved but FPF decisions are absent. | State selected payload, rejected payload, and selected-locus obligations. |
| **Address completion without architecture.** Every locus is named but the split or merge is wrong. | Repair `FPFContentArchitectureSelectionAdequacy`. |
| **Watch item as decision.** Drafting is expected to choose the answer during pattern authoring. | Select, repair, split, or hold. |
| **Ontic candidate left to drafting.** A `DRR` uses uncertain candidate phrasing for a concept cluster or pattern set but leaves candidate sufficiency, rejected alternatives, publication boundary, and placement for the pattern author. | Close `DRROnticCandidateDisposition` now: select, reject, split, or decline the candidate by value; state the direct governing pattern when no new ontic is warranted. |
| **Review-state proxy.** Review acceptance or landing is treated as adequacy. | Use decision-content evidence only. |
| **Adequacy table without evidence loci.** Values are listed without by-value `DRR` or source loci. | Re-run the evaluation with `Coordinate | Value | ShortRationale | EvidenceLocus`; lower any coordinate whose evidence cannot be named. |
| **Apparatus-overwrapped drafting payload.** The `DRR` offers selected-pattern wording wrapped in role, publication-form, locus, flow, state, status, text, package, or process apparatus without changing a recoverable kind, relation, claim kind, admissible use, evidence value, selected locus, user-facing action, or flow role. | Classify the wording under `F.19`. If it changes a kind or claim, repair through precision restoration; otherwise expose the governed EntityOfConcern, first substantive drafting move, exact selected-locus relation/decision, user-facing action, and only necessary boundary/reference pointers as positive subject kind and action guidance. An evaluation row is neither future method nor work. |
| **Goodharted DRR adequacy.** A `DRR` is made easier to defend as `4` or `5` by adding source rows, selected-locus tables, boundary catalogues, or review proof, while selected answer, selected-locus obligations, source payload mutation, architecture choice, or first drafting action do not improve. | Reject apparatus-only improvement; apply `E.13` when adequacy values or review marks are replacing decision usefulness; repair the decision content, delete or relocate proof material, and record checked no-proposal only when no non-dominated decision-content improvement remains. |
| **Solution architecture evaporates after DRR.** A `DRR` solves a multi-locus unfolding or first-entry problem, but pattern hosts receive only local fragments and the DRR remains the only place where the full problem-solution structure is understandable. | Run `CampaignProblemSolutionUnfoldingCheck`; move the residue into selected pattern bodies, local unfolding blocks, E.11 entry expansions, or direct governing-pattern relations. |

### E.9.DA:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| DRR adequacy becomes inspectable before drafting. | Pattern authors get decisions, not source summaries. | Every opened `E.9.DA` evaluation touches all coordinates. |
| Architecture selection becomes visible. | By-value but wrong split or merge choices no longer pass as complete distribution. | Some DRRs need architecture repair before drafting. |
| Source mutation is explicit. | SoTA, standards, reviews, audits, and accepted decisions shape decisions rather than decorate them. | Rationale-only sources cannot raise values. |

### E.9.DA:10 - Rationale

The cheapest place to repair missing FPF decisions is the DRR, before pattern prose spreads uncertainty across several hosts. A compact complete result episteme is better than a heavy preliminary audit: dated assessment work enacts the method, A.6.1 application bindings return coordinate values, and the result episteme states every coordinate claim, first repair, and bounded stop. The evaluation specification, optional record, and favorable local status neither perform nor authorize repair.

### E.9.DA:11 - SoTA-Echoing

| Claim | Practice basis | Local adoption |
|---|---|---|
| DRR adequacy is decision-content adequacy, not template completeness. | Architecture-description and ADR traditions keep concerns, alternatives, decisions, rationale, and consequences inspectable. | The `DRR` must carry selected answers, alternatives, consequences, and selected-locus decisions. |
| Multi-host FPF changes need selected-locus disposition. | Lightweight ADR practice is useful but too central-record-oriented for multi-pattern FPF changes. | `DRRSelectedLocusDispositionMap` states obligations and non-obligations by locus. |
| Feedback needs desired condition, current condition, next action, and tactics. | Sadler and Hattie and Timperley feedback traditions, carried through `E.22` and `E.23`. | `ShortRationale`, evidence locus, finding and proposal rows, and checked no-proposal dispositions stay separate. |
| Source evidence must mutate the decision. | Current FPF `E.8`, `E.19`, `E.21`, and living-source discipline require non-decorative source use. | `SoTAAndEvidenceUseInDecision` checks changed decision payload, not citation presence. |
| Improvement remains multi-coordinate and trade-off sensitive. | MCDA, Pareto, and QD, OEE, and NQD lines inherited through `E.22` and `E.23`. | E.9.DA result rules require the result episteme to state what became worse; repeated improvement work remains outside E.9.DA. |
| Decision-adequacy measures can become targets. | Goodhart and Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines. | `E.9.DA` forbids all-`5` or `5-defensible` repair targeting; values rise only when decision content becomes stronger for declared authoring use, and `E.13` governs any proxy-to-value claim about those values. |

### E.9.DA:12 - Relations

| Pattern | Relation |
|---|---|
| `E.9` | Defines `DRRMethod`, selected-answer decision work/result, and the minimum C.2.1 DRR episteme form. E.9.DA governs assessment of one exact DRR episteme; it is not a second DRR method or form. |
| `A.19`, `A.19.ECS`, `A.17`, `A.18`, `C.16`, `C.16.Q`, `C.25` | Govern the characteristic space, evaluation specification, characteristics, scales, measurement boundary, quality-ascription precision, and any separately selected Q-Bundle consumed here. E.9.DA supplies the DRR-specific coordinates and result rules. |
| `A.15.1`, `A.6.1`, `A.2`, `A.2.1` | Govern dated assessment work, the actual evaluation application/bindings, evaluator role, and obtaining role assignment. The E.9.DA specification and optional record perform none of these. |
| `C.2.1` | Constitutes the checked DRR episteme, per-coordinate result claims, aggregate adequacy-result episteme, and optional evaluation-record episteme independently. |
| `A.10`, `B.3` | Govern exact evidence use/provenance and any assurance or reliance on the result. Witness presence and a favorable value create neither relation. |
| `F.10`, `G.11` | Govern any downstream status use/interpretation and currentness. A local E.9.DA status value does not authorize drafting by itself. |
| `E.24.PUB`, `C.29` | Govern publication occurrence, form, carrier, and representation of a result or record; publication does not perform assessment or strengthen its claim. |
| `E.8` | Governs later authored pattern bodies after a separately authorized decision; E.9.DA neither authors nor admits them. |
| `E.19` | May use current E.9.DA result claims as evidence or return findings exposing upstream DRR defects. Its admission/refresh check and result remain distinct. |
| `E.21` | Declares the pattern-quality characteristic space and result rules used for resulting pattern versions. Dated E.21 assessment work and its result concern one exact pattern version, not DRR adequacy, E.19 admission, or the E.9.DA record. |
| `E.22` | Frames one evaluation question/use without performing assessment or assigning values. |
| `E.23` | Governs repeated improvement and repair work after findings or proposals exist; it does not become the original assessment or result. |
| `E.13` | Governs proxy-to-value alignment when adequacy values, source counts, review marks, or discharge evidence substitute for decision usefulness. |
| `E.10`, `A.6.P`, `C.2.P`, `F.18`, `F.19` | Govern wording/use precision, relation and episteme phrasing, durable naming, and apparatus classification used by the precision profile. |
| Architecture-facing FPF patterns | Receive architecture, structure, view, graph, publication, and source-use distinctions when the DRR decision uses them. |

### E.9.DA:End

