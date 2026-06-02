## E.21 - FPF Pattern-Quality Evaluation CharacteristicSpace

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### E.21:1 - Problem frame

Use `E.21` when you are evaluating one FPF pattern version and need to know whether improvement can stop without relying on taste, a single quality score, or template compliance alone. The governed object is the scoped pattern-quality claim; the pattern version under quality read is one authored FPF pattern body in one declared use and reader scope.

Use it especially when a pattern already has the `E.8` skeleton and may even pass an `E.19` review, but authors still disagree about whether the pattern is recognisable, action-guiding, ontologically precise, SoTA-bearing, proportionate in apparatus, and safe to compose with neighbours.

**Not this pattern when.** Use `E.8` to write the pattern body. Use `E.19` to run admission or refresh review profiles. Use `E.9.DA` when the evaluated object is one `DRR` decision-adequacy claim rather than one authored FPF pattern version. Use `C.16`, `A.17`, `A.18`, and `A.19` when the live problem is measurement legality, Characteristic and Scale discipline, or declaring a general `CharacteristicSpace`. Use `C.25` when the live problem is an arbitrary engineering quality family rather than FPF pattern quality. Use `F.18` when the live problem is durable naming. Not this pattern when the live question is whether a user correctly applied an FPF pattern in a project case. `E.21` reads the quality of the pattern text for a declared reader, use, and scope. Pattern-application quality belongs to the receiving project-side or publication-side pattern that governs the actual case: evidence, assurance, gate, work, decision, publication, action invitation, method, or bridge use as applicable.

**First useful move.** The architectural first move of `E.21` is not "run quality control". It is to recover the pattern version's first admissible action-guiding move for the declared reader, use, and window. Start with the ordinary first-pass slice of `PatternQualityQBundle`: name `PatternVersionRef`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`, then inspect the pattern version's `Problem frame` and `Solution` for one first admissible action-guiding move for that working reader.

If that first move is absent, unrecoverable, or only present in the Conformance Checklist, close the first-pass read as `repairBeforeUse` for the declared use, or as `admissibleWithNarrowerUse` when the pattern can still serve an expert-only or support-only scope. Do not require a full coordinate comparison before this result.

Create the fuller `PatternQualityQBundle` only when the first-pass slice survives, when several candidate edits are being compared, or when admission, refresh, high-assurance reuse, or contested neighbour authority is live.

**What goes wrong if missed.** Pattern improvement collapses into a single "quality score", a reviewer preference, or a heading checklist. That hides hard blockers such as undefined vocabulary, shadow authority, decorative SoTA, ordinal arithmetic, missing first move, or neighbour breakage.

**What this buys.** `E.21` gives authors one typed quality space for FPF patterns: hard eligibility filters first, multi-characteristic coordinates second, Pareto-front reasoning for candidate improvements, and an explicit stop condition that does not scalarize.

`E.21` is the pattern-quality evaluation pattern for claims of the form "this pattern version is sufficiently good for this use, readership, and scope." It normalizes such claims into a scoped bundle; it does not run the review process or take over authoring, measurement, naming, project evidence, assurance, gate, release, or work authority from neighbouring FPF patterns.

**Governed object in plain terms.** The governed object is the pattern-quality claim for one FPF pattern version under one declared use and reader scope.

**Primary working reader.** The first reader is an FPF author, reviewer, or steward deciding whether to keep improving a pattern version. The downstream reader is the practitioner or manager who must use the pattern as action guidance.

### E.21:2 - Problem

FPF needs a way to evaluate pattern quality without creating a fake scalar. A single score is attractive because it is easy to compare, but it is false for this object. A pattern can be excellent in SoTA support and still unreadable; precise in ontology and still too heavy for ordinary use; concise and still wrong about neighbours.

The recurring failures are:

1. **Hidden scalarization.** Different coordinates such as recognition, ontology, SoTA, evidence, and reader cost are averaged or ranked as if they had one common unit.
2. **Template-only maturity.** Canonical headings are present, but the first working situation, first admissible move, boundary, and practical payoff remain missing.
3. **Checklist substitution.** The conformance checklist replaces the `Solution` instead of testing it.
4. **Ontology-light review.** Wording is polished while kind, relation, support, evidence, measurement, assurance, and neighbouring-pattern authority remain unstable.
5. **Decorative SoTA.** Sources are cited, but they do not change the `Solution`, conformance checks, boundaries, examples, or relations.
6. **Apparatus bloat.** A draft accumulates fields, manifests, gates, and companion files that increase author and reader cost without improving admissible use.
7. **Coordinate Goodharting.** A draft is optimized for the declared coordinates until it becomes harder to use, costlier to maintain, or less faithful to the practical value the coordinates were meant to protect.
8. **Endless improvement.** Authors keep polishing because there is no declared stop condition and no visible distinction between material improvement and cosmetic movement.

### E.21:3 - Forces

| Force | Tension |
|---|---|
| **Comparability vs hidden scalarization** | Authors need to compare pattern versions, but ordinal qualities do not admit a single arithmetic score. |
| **Hard blockers vs optimization** | Undefined vocabulary or false neighbour authority must be repaired before any front comparison matters. |
| **Optimization pressure vs unmeasured value loss** | Once coordinates become the proxy for value, authors may improve measured properties while degrading affordability, repair-impact predictability, entry and projection integrity, corpus ecology, or direct pattern-use value. |
| **Didactic usability vs ontological precision** | A pattern must be readable by a cold working reader and still preserve exact FPF kinds, relations, and admissible uses. |
| **Open-ended evolution vs stop discipline** | FPF assumes indefinite improvement, but one pattern version still needs an admissible stopping point for the declared use. |
| **SoTA breadth vs local payoff** | Current practice must discipline the pattern, but citations should not become a decorative literature shelf. |
| **Parsimony vs assurance** | Quality evaluation should catch real defects without turning every pattern into a heavy review harness. |
| **Pattern autonomy vs neighbour fit** | A pattern needs a stable local governed object while evidence, assurance, measurement, naming, causality, publication, work, and release claims remain assigned to their governing neighbours. |

### E.21:4 - Solution - Pattern quality as a scoped Q-Bundle over declared characteristics

State the scoped FPF pattern-quality read as a `PatternQualityQBundle`, not as one score.

#### E.21:4.0 - Architectural position

`E.21` is a local receiving pattern for scoped FPF pattern-quality claims. It specialises existing FPF architecture; it does not create a new quality-governance subsystem.

It defines how to read whether one authored FPF pattern version is good enough for one declared reader, use, and scope, why improvement may stop, and which weaknesses remain bounded.

`E.21` governs only these questions:

1. Which exact FPF pattern version is being read?
2. For which reader, use, scope, and currentness window?
3. Which hard blockers make comparison meaningless?
4. Which ordinal pattern-quality coordinates are active?
5. Which content evidence supports the coordinate readings?
6. Which `PatternQualityStatus` follows?
7. Why may improvement stop, or why must the claim narrow, repair, hold for architecture, or refresh?

`E.21` does not govern:

* authoring the pattern body (`E.8`);
* running admission or refresh review profiles (`E.19`);
* general measurement legality (`C.16`, `A.17`, `A.18`, `A.19`);
* arbitrary engineering quality-family bundling (`C.25`);
* durable naming and local-first unification (`F.18`, `E.10`, `A.6.P`);
* project evidence, assurance, gate, work, release, safety, security, or compliance claims (`A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or the exact receiving pattern).

A conforming `E.21` read may cite neighbouring patterns, but it may not absorb their governed objects.

`E.21` protects these pattern-quality boundary loci as part of the pattern-quality read: self-application, first-entry discoverability, publication and projection, bounded non-use, no forced winner, falsifiability and lowering evidence, reviewer-power misuse, AI, RAG, thin-echo summaries, and corpus ecology. A read that crosses one of these loci must keep the pattern-quality claim scoped, replayable, falsifiable, and kept under the exact neighbouring pattern application instead of becoming control apparatus.

#### E.21:4.0a - Mint/reuse and kind settlement

`E.21` mints no new Kernel kind, no project-side evidence kind, no assurance kind, no work kind, no gate kind, no release kind, and no general maturity kind.

Its durable heads are local specialisations, fields, value sets, or scoped support constructs over existing FPF kinds:

| E.21 head | Kind settlement | Existing governing pattern kept intact |
|---|---|---|
| `PatternQualityQBundle` | Local `C.25` Q-Bundle specialisation for one scoped FPF pattern-quality claim. | `C.25` remains the general Q-Bundle normal form. |
| `PatternQualityEvaluationCharacteristicSpace` | Local `A.19` CharacteristicSpace specialisation for ordinal pattern-quality content readings. | `A.17`, `A.18`, `A.19`, and `C.16` keep general Characteristic, Scale, Coordinate, and measurement legality. |
| `PatternQualityStatus` | Local value set inside a `PatternQualityQBundle`; an admissible-use posture for the pattern-quality claim. | Not a role state, release state, gate decision, assurance level, or project status. |
| `EligibilitySet` | Set-valued hard-filter field inside `PatternQualityQBundle`. | Not an `A.21` gate, not an `E.19` review profile, and not a soft score region. |
| `DominanceSet` | Set-valued coordinate-selection field for Pareto comparison after eligibility passes. | Not a hidden scoring method, not `G.5` selection policy, not `C.11` choice result. |
| `TieBreakerSet` | Set-valued secondary preference field among non-dominated candidates. | Not a secret dominance coordinate or hard blocker override. |
| `TelemetrySet` | Set-valued reopen/calibration signal field for the pattern-quality claim. | Not project telemetry, not certification evidence, not replacement for content evidence. |
| `CoordinateEvidenceRef` | Local evidence-reference record for one coordinate reading. | It may cite `A.10` or `B.3` only when evidence or assurance claims are actually live. |
| `CoordinateEvidenceRefs` | Set-valued field of `CoordinateEvidenceRef` records. | Not an evidence archive, review verdict, or proof of project-world truth. |
| `PatternQualityFront` | Scoped non-dominated set over candidate pattern versions or candidate edits under the active `E.21` relation. | Not a `C.18` NQD archive, not a `G.5` shortlist, not a project backlog. |
| `PatternImprovementArchive` | Bounded trade-off evidence archive for candidate pattern edits or variants. | Not process history, chat memory, permanent backlog, or mandatory appendix. |

Coordinate heads in `E.21:4.3` are local pattern-quality characteristic heads inside `PatternQualityEvaluationCharacteristicSpace`. They do not become general FPF characteristics, numeric measures, maturity dimensions, or measurement templates unless a neighbouring `C.16`, `A.17`, `A.18`, or `A.19` declaration makes that live.

A conforming `E.21` read treats these heads as exact local constructs. When a head is reused outside `E.21`, the receiving text must either cite `E.21` by value or rerun the exact governing pattern for the new use.

#### E.21:4.0b - Layered use architecture

`E.21` has four activation layers.

Layer 0 and Layer 1 are ordinary; Layer 2 and Layer 3 are live-claim only.

**Layer 0 - first-pass slice.**
Used for one first read of one pattern version. It names `PatternVersionRef`, `WorkingReaderScope`, `IntendedUse`, `QualificationWindow`, first admissible move evidence, activated blockers, minimal active coordinates, status, and next admissible repair or bounded non-use.

**Layer 1 - content-evidence coordinate read.**
Used when the first-pass slice survives or when a substantive quality claim is being made. It checks activated `EligibilitySet` rows, active ordinal coordinates, and local `CoordinateEvidenceRefs`.

**Layer 2 - comparison and stop.**
Used when several candidate edits or variants are live, or when a stop decision is being claimed. It activates `DominanceSet`, floors, `TieBreakerSet`, `PatternQualityStatus`, and `StopCondition`.

**Layer 3 - optional refresh and trade-off support.**
Used only when live reuse, repeated findings, retrieval failure, high-use patterns, high-assurance reuse, contested neighbour authority, or variant-history retention makes support necessary. It may activate `TelemetrySet`, `PatternQualityFront`, `PatternImprovementArchive`, and full support cards.

A higher layer SHALL NOT be required merely because a lower-layer read exists.

Every activated layer must state what admissible use it buys.

If a field, card, telemetry signal, archive entry, or evidence record does not change first-pass usability, coordinate evidence, variant comparison, stop or reopen condition, or bounded non-use, it is apparatus bloat for the current claim.

#### E.21:4.0c - Self-application and recursion boundary

`E.21` may be applied to itself only through the same lowest sufficient activation layer used for any other FPF pattern.

The ordinary self-application read closes when the current `E.21` text exposes:

1. one first admissible action-guiding move for an author or reviewer;
2. the governed object of the quality read;
3. the no-single-score and no-administrative-proxy boundary;
4. the neighbour-authority boundary to `E.8`, `E.19`, `C.25`, `C.16`, `A.17`, `A.18`, `A.19`, `F.18`, `E.10`, `A.6.P`, `E.17`, `A.10`, `B.3`, `A.20`, `A.21`, and `A.15`;
5. one explicit stop or repair condition for the declared self-read scope.

Self-application SHALL NOT require an additional `PatternQualityQBundle` evaluating the previous `PatternQualityQBundle`. If the first self-read exposes a content defect, repair that defect in the pattern text or narrow the declared use. If the defect is architectural, use `holdForArchitectureDecision`.

#### E.21:4.0d - Pattern-quality question framing

A pattern-quality read does not begin from an implicit request such as "review this", "evaluate this", or "improve this". For a nontrivial read, use `E.22` to declare the quality-read purpose before `E.21` assigns pattern-quality coordinates or stop result.

The question frame states the `QualityReadPurposeSelection`, declared floor, desired improvement aim, protected trade-offs, and open-question classification rule. If no purpose is declared, the default is `floorRead` under the declared or receiving-pattern floor, not `exceptionalImprovementRead`.

`exceptionalImprovementRead` asks for non-dominated edits that could move active coordinates toward `5` where feasible. `paretoTradeoffRead` asks whether that movement damages usability, affordability, repair locality, corpus ecology, neighbour fit, entry and projection integrity, or another protected quality. `openQuestionDiscoveryRead` classifies important unasked questions as an existing `E.21` coordinate issue, candidate coordinate or overlay, or outside `E.21` under another exact FPF pattern. `absorptionRead` maps returned findings to coordinate movement, floor-only closure, unchanged already-satisfied content, trade-offs, quality loss, or outside-pattern disposition.

The question frame is not pattern-quality evidence by itself. It only states which `E.21` question is being asked, so the resulting `PatternQualityQBundle` can answer the intended question rather than a reviewer-selected default.

When the same pattern version is being improved through repeated passes, use `E.23` for the repeated quality-improvement method. `E.21` supplies the pattern-quality coordinates, values, protected trade-offs, status, and stop meanings; it does not govern row-atomic absorption across passes, method-family selection, or stop, narrow, continue, switch method, or hold decisions.


#### E.21:4.1 - PatternQualityQBundle

`PatternQualityQBundle := <PatternVersionRef, ClaimScope, WorkingReaderScope, IntendedUse, QualificationWindow, QualityReadQuestionFrameRef?, EligibilitySet, DominanceSet, CoordinateEvidenceRefs?, TieBreakerSet?, TelemetrySet?, EvidenceRefs, PatternQualityStatus, StopCondition>`
`PatternQualityQBundle` is the publication unit for a scoped pattern-quality claim.

`PatternQualityQBundle` is replayable when another reader can recover the same pattern version, declared scope, active eligibility rows, active coordinates, coordinate evidence refs, status payload, and stop/non-stop reason without chat memory, steward memory, or administrative placement state.

`QualityReadQuestionFrameRef?` is optional. When present, it cites an `E.22` question frame that states whether this is a floor, exceptional-improvement, Pareto trade-off, open-question discovery, absorption, or combined read. The frame does not supply coordinate evidence; it constrains which `E.21` result shape is expected.

Its first-pass slice may contain only the fields needed to decide whether one working reader can recover the governed object and first admissible move.

The full bundle is used when coordinate evidence, variant comparison, admission/refresh closure, high-assurance reuse, or contested neighbour authority is live.

The fields below are slots in that publication unit; they are not independent governed objects. The governed object remains the scoped pattern-quality claim for one pattern version.

| Field | Role |
|---|---|
| `PatternVersionRef` | The exact pattern version being assessed. A title alone is not enough when several extracted hosts or monolith editions exist. |
| `ClaimScope` | The declared pattern-quality claim boundary: ordinary authoring support quality read, admission-support quality read, refresh-support quality read, landing-support quality read, release-support quality read, canonization-support quality read, external-review-support quality read, high-assurance-reuse support quality read, or another named support scope. The administrative action is not the quality scope; it is the neighbouring action that this quality read may support. Do not name the administrative action itself as a coordinate-bearing quality scope. |
| `WorkingReaderScope` | The primary reader role and first-use situation the pattern must serve. |
| `IntendedUse` | What the quality result is allowed to support: continue drafting, admit for declared use, narrow use, repair before use, or refresh. |
| `QualificationWindow` | The time, edition, SoTA, neighbouring-pattern, or release window in which the quality read is current. |
| `EligibilitySet` | Hard filters that must pass before coordinate comparison is meaningful. |
| `DominanceSet` | The selected quality coordinates used for Pareto comparison of candidate versions or candidate edits. |
| `CoordinateEvidenceRefs?` | Text sections, worked cases, SoTA rows, relation checks, or findings that support coordinate values. Review, landing, release, or monolith state alone is not coordinate evidence. |
| `TieBreakerSet?` | Secondary preferences used only among non-dominated candidates. |
| `TelemetrySet?` | Observed return, retrieval, review, and drift signals used to reopen or calibrate the quality read. |
| `EvidenceRefs` | Evidence, worked cases, review findings, SoTA rows, or source references that support the read. |
| `PatternQualityStatus` | The resulting admissible-use posture. |
| `StopCondition` | The explicit condition under which improvement can stop for this scope. |

`PatternQualityStatus` has this value set:

| Value | Meaning |
|---|---|
| `admissibleForDeclaredUse` | Eligibility passes and the selected coordinates meet the declared floors for the current `ClaimScope`. |
| `admissibleWithNarrowerUse` | The pattern can be used only after the `ClaimScope`, `WorkingReaderScope`, or supported use is narrowed by value. |
| `repairBeforeUse` | One or more hard eligibility filters or live quality floors fail, and the pattern should not be relied on for the intended use. |
| `holdForArchitectureDecision` | The defect is not local prose; the governed object, neighbour authority, pattern split, or placement must be decided before quality evaluation can close. |
| `refreshNeeded` | The pattern was previously admissible, but a SoTA, neighbour, terminology, retrieval, telemetry, or use-scope change invalidates the old read. |

A `PatternQualityStatus` is an admissible-use posture for the pattern-quality claim. It is not a gate decision, release state, assurance level, compliance verdict, safety certificate, work authority, publication truth, or project-side refusal/approval.

A status without payload is not checkable. Every `PatternQualityStatus` SHALL carry the minimal status payload:

* `admissibleForDeclaredUse`: declared use, active floors, and remaining bounded non-use, if any.
* `admissibleWithNarrowerUse`: the exact narrowed `ClaimScope`, `WorkingReaderScope`, or `IntendedUse`.
* `repairBeforeUse`: the activated blocker and the first admissible repair move.
* `holdForArchitectureDecision`: the exact unresolved governed-object, neighbour-authority, split, or placement question.
* `refreshNeeded`: the exact SoTA, neighbour, terminology, retrieval, telemetry, or use-scope change that invalidated the previous read.

A bounded non-use result is a valid pattern-quality outcome.

When a pattern is not admissible for the declared ordinary use but remains useful as expert-only support, source-basis support, high-assurance support, historical rationale, narrow worked-case support, or neighbouring-pattern support, the `PatternQualityStatus` SHALL be `admissibleWithNarrowerUse`, not `repairBeforeUse`.

The narrowed use must name:

* the exact narrowed reader/use/scope;
* the prohibited broader use;
* the first admissible next pattern or repair if broader use is still desired.

#### E.21:4.1a - Coordinate readings are content readings, not administrative-state readings

`PatternQualityEvaluationCharacteristicSpace` coordinates measure the current pattern version and the content evidence available for that version: its recognition text, governed object, ontology, names, Solution, checklist, worked cases, SoTA rows, relations, and support boundaries. They do not measure whether the pattern has already been externally reviewed, merged into a monolith, included in a release branch, or accepted by one steward process.

Administrative state can change a `PatternQualityQBundle` only in these ways:

| Administrative-state effect | Admissible role |
|---|---|
| Review, landing, release, or monolith state | May constrain `ClaimScope`, `IntendedUse`, `QualificationWindow`, or confidence in `EvidenceRefs`. It does not raise or lower a coordinate by itself. |
| External review finding | May change a coordinate only when the finding identifies a content defect or content strength in the pattern version. The coordinate changes because of the defect or strength, not because a review event occurred. |
| Landing or publication move | May change which pattern version is referenced by `PatternVersionRef`, and may change discoverability or authority claims handled by other patterns. It does not make the same text more or less mathematically adequate, ontologically precise, or action-guiding by placement alone. |
| Missing administrative action | May block a release, review, or canonization claim. It is not evidence that `FormalClaimLegalityAndLensFit`, `CaseCountercaseAndTransferCoverage`, `ActionPathGuidance`, or another active coordinate is low. |

If a quality read says "low because this has not been externally reviewed" or "high because this is already in the monolith", it is using administrative state as a proxy. The repair is to state the substantive coordinate evidence directly and keep administrative state in `ClaimScope`, `QualificationWindow`, or receiving release/review patterns.

#### E.21:4.1b - Pattern property evidence vs reputation signals

Coordinate values read properties of the pattern version for the declared reader, use, scope, and qualification window. Popularity, adoption, award, steward praise, reviewer praise, external-review completion, number of reviews, monolith placement, release inclusion, or prior use is not a coordinate value and does not raise or lower a coordinate by itself.

Such signals may only serve as pointers to inspect content evidence. A replayable observation such as "three first-time readers could not recover the first admissible move from this Problem frame" may lower `ActionPathGuidance` because it names the pattern text, reader scope, use situation, observed failure, and coordinate affected. A signal such as "widely used", "not yet used", "reviewer-clean", "not externally reviewed", "popular", or "already accepted" remains outside the coordinate value unless it is rewritten into exact pattern-content evidence.

Absence of prior use, external review, landing, release, or steward acceptance is not evidence against `4` or `5`. Only missing or weak pattern-content evidence for the declared use can lower the coordinate. The same pattern text under the same `PatternVersionRef`, `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow` should receive the same coordinate value whether it is still in a host file, already in the monolith, praised by reviewers, ignored by readers, or newly written.


#### E.21:4.2 - EligibilitySet: hard conditions before quality comparison

The `EligibilitySet` is not a low-scoring region. It is the precondition for meaningful comparison.

Eligibility rows have activation. A first-pass pattern-quality read always checks only the rows needed to decide whether one working reader can recognise the situation, recover the governed object, find the first admissible move, and avoid immediate neighbour-authority or apparatus overread.

Rows whose condition depends on a live source, live formal lens, live measurement claim, live accepted basis, live release/review state, live mission/pillar conflict, or live durable-name change activate only when that claim force is present in the pattern version or in the declared `ClaimScope`.

Failure of an activated eligibility row is a content blocker. A non-activated row is not a pass, not a waiver, and not a hidden todo; it is outside the current pattern-quality claim.

| Eligibility condition | Pass condition |
|---|---|
| `canonicalFrameConformance` | The pattern has the `E.8` canonical frame, header block, required sections, and footer marker, or the missing piece is explicitly treated as a mechanical repair before use. |
| `governedObjectClarity` | The early text says which object, relation, move, boundary, or support claim the pattern governs. |
| `firstMoveRecoverability` | The pattern version's `Problem frame` and `Solution` expose one first admissible action-guiding move for the declared `WorkingReaderScope`, or a named neighbouring-pattern application now carries the live claim. |
| `missionOrPillarConflict` | Activated when the pattern claims FPF-wide mission support, changes a pillar interpretation, imports external domain scope, or creates a possible pillar conflict. Absence of pillar recitation is not a defect. Pass condition: no live mission/pillar conflict is hidden, and any live constitutional payoff is carried by the exact coordinate or neighbouring pattern that governs it. |
| `noProcessLeakage` | Live pattern prose contains no campaign, review, history, planning, landing, or "what changed" residue. |
| `normativityAdmissibilitySplit` | RFC keywords state agent obligations only; definitions, invariants, typing rules, and admissibility predicates are not written as duties. |
| `terminologyAdmissibility` | Minted and FPF-force-bearing names pass the `F.18 -> A.6.P -> E.10` chain: kind, relation, qualification, governed object, governed move, and non-admissible neighbouring use are recoverable. |
| `solutionChecklistCoherence` | `Problem`, `Forces`, `Solution`, `Conformance Checklist`, anti-patterns, and relations test the same action guidance. |
| `neighborRelationClosure` | The pattern does not create shadow authority; relations and downstream hooks cite the exact neighbouring FPF patterns by value. |
| `SoTABindingMinimum` | SoTA rows are non-decorative: at least one `Solution`, checklist, boundary, worked case, or relation changes because of the adopted/adapted/rejected source stance. |
| `measurementAndScaleLegality` | Any value, score, coordinate, scale, threshold, comparison, or quality coordinate is typed through `C.16`, `A.17`, `A.18`, and applicable `A.19`/`C.25` discipline. |
| `coordinateAdministrativeIndependence` | Coordinate values are assigned from pattern content and content evidence, not from review completion, landing state, monolith placement, release state, or steward acceptance. |
| `noProxyForValueSubstitution` | The quality read asks what became worse when coordinates improved: first-use cost, author cost, maintenance cost, neighbour ripple, entry/projection cost, corpus cost, practical payoff, and bounded non-use are not hidden outside the active comparison. |
| `formalClaimLegalityAndLensFit` | If a measurement, score, comparison, threshold, aggregation, mathematical lens, causal lens, QL lens, simulation, representation, or learned-lens claim carries FPF force, the scale/comparability basis, preserved structure, lost structure, visible payoff, admissible use, non-admissible use, and stop condition are named. |
| `acceptedBasisCarryThrough` | Accepted intake, DRR, returned findings, or architecture-basis obligations that govern the pattern are expressed, intentionally absent, or assigned to a named receiving FPF pattern or support document. |

If an eligibility condition fails, the status is `repairBeforeUse` or `holdForArchitectureDecision`. Do not average the failure into better coordinates. A missing first move is not a weak coordinate. For an ordinary-use pattern-quality read, failed activated `firstMoveRecoverability` is a blocker unless the claim is explicitly narrowed to expert-only use, reference-only use, or architecture-decision use.

#### E.21:4.3 - PatternQualityEvaluationCharacteristicSpace

`PatternQualityEvaluationCharacteristicSpace` is the declared characteristic space for FPF pattern-quality reads. It uses ordinal coordinates. The default scale is a zero-based six-level scale:

A `PatternQualityEvaluationCharacteristicSpace` is not a general FPF quality ontology. Its coordinate heads remain local pattern-quality characteristic heads unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration makes a broader characteristic or measurement claim live.

A coordinate value in `PatternQualityEvaluationCharacteristicSpace` is an ordinal pattern-quality reading, not a `U.Measure` by default. It becomes a measurement claim only when the pattern explicitly declares a `C.16` measurement template, scale, unit, or admissible coordinate construction. Otherwise the value is an evidence-backed ordinal judgement over pattern content for the declared scope.

| Value | Label | Meaning |
|---:|---|---|
| 0 | `absent` | The characteristic is not expressed in the pattern text for the declared scope. |
| 1 | `namedOnly` | The characteristic is named or implied, but the reader cannot use it as pattern-quality evidence. |
| 2 | `partiallyExpressedForDeclaredUse` | The characteristic is expressed in one or more local loci, but the expression is incomplete, fragile, or too narrow for the declared use. |
| 3 | `sufficientlyExpressedForDeclaredUse` | The characteristic is expressed enough to support the declared use, with known limits kept visible. |
| 4 | `wellExpressedForDeclaredUse` | The characteristic is clearly and repeatedly expressed across the pattern body, with direct evidence and boundary protection. |
| 5 | `exceptionallyExpressedForDeclaredUse` | The characteristic is expressed at an exceptional level for the declared use, across multiple reinforcing loci and cases, without hiding cost or neighbouring-pattern loss. |

The scale is zero-based because true absence is not a weak positive value. It uses six levels rather than ten because the read is ordinal: six levels distinguish absence, mere naming, partial expression, sufficiency, strong expression, and exceptional expression without pretending to have decimal-grade precision. The labels are intentionally domain-neutral. They describe degree of expression of whichever characteristic is being read; they do not import a substantive property such as robustness, stability, safety, maturity, completeness, usability, affordability, or evidence strength into every coordinate.

Authors may use a coordinate-specific named scale when needed, but they must keep the scale ordinal unless a `C.16` measurement basis with the needed measurement semantics is declared. No arithmetic mean, percentage score, or hidden normalization is admissible.

The ordinal value of a coordinate is a content reading. `FormalClaimLegalityAndLensFit = 3` means the formal or lens claim is sufficiently expressed for the declared use; it does not mean "not yet reviewed". `FormalClaimLegalityAndLensFit = 5` means the same coordinate is exceptionally expressed in the current pattern text; it does not mean "already landed". The same pattern text in an extracted host and in a monolith should receive the same coordinate value unless the move changes the text, exposes a new content defect, changes the version under `PatternVersionRef`, or changes the declared use being evaluated.

Coordinate names in this section are local characteristic heads inside `PatternQualityEvaluationCharacteristicSpace`. They are not `U.Measure`s and not general-purpose CHR patterns by name alone.

A coordinate value is an ordinal content reading over the pattern version text for the declared `ClaimScope`. It becomes a measurement claim only when a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration explicitly supplies the measurement basis, scale, unit, comparability mode, and evidence support.

Coordinate values in `PatternQualityEvaluationCharacteristicSpace` are ordinal content readings unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration makes a measurement claim live. `DominanceSet` compares these readings without scalarizing them.

#### E.21:4.3a - Coordinate value evidence test

A coordinate value is justified by content evidence, not by the label alone. The ordinary `4 wellExpressedForDeclaredUse` test is:

1. the coordinate names the exact property being read;
2. the pattern text contains direct evidence for that property;
3. at least one positive case and one boundary or anti-case exercise the property;
4. neighbouring-pattern relations or non-use boundaries protect the property from overread;
5. SoTA or internal FPF architecture changes at least one `Solution`, checklist, relation, or worked-case line when the coordinate depends on a source or modeling lens;
6. the coordinate evidence does not depend on review completion, landing state, monolith placement, release state, or steward acceptance.

A `5 exceptionallyExpressedForDeclaredUse` value requires the `4` test plus additional content evidence: multiple reinforcing loci, heterogeneous cases or anti-cases where the characteristic changes the result, explicit non-use boundary, and no hidden affordability, maintenance, neighbour-ripple, corpus, entry/projection, or proxy-for-value loss.

`3 sufficientlyExpressedForDeclaredUse` means the coordinate is usable for the declared scope but lacks one or more evidence references, cases, anti-cases, or boundary statements required for `4` or `5`. Coordinate value and `CoordinateEvidenceRefs` remain distinct: a value says the declared expression degree for the characteristic; `CoordinateEvidenceRefs` say why that reading is justified.

The coordinates below are not one flat always-on audit grid. `PatternQualityEvaluationCharacteristicSpace` is an activation-normalized characteristic menu for scoped FPF pattern-quality reads.

A coordinate is admissible only when it reads a content property of the pattern version under quality read under the declared `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`.

Hard blockers stay in `EligibilitySet`. Evidence kinds justify coordinate readings but are not coordinates by themselves. Telemetry reopens or calibrates a read but does not replace content evidence. Fronts and archives preserve candidate trade-offs but do not add ordinary drafting obligations. `PatternQualityStatus` and `StopCondition` are results of the read, not coordinates. Project-side evidence, assurance, gate, release, work, safety, security, or compliance claims stay under exact neighbouring patterns.

Each coordinate has an activation class:

- `first-pass core`: ordinarily active for the first ordinary read of one pattern version;
- `ordinary stop core`: active when the read claims admission, stop, repair-before-use, or narrowed-use closure;
- `claim-support`: active when evidence, currentness, SoTA, case breadth, measurement, formal lens, replay, or high-value claim support is live;
- `corpus/publication`: active when the edit changes entry cues, ToC/J.4/Preface, summaries, cards, dashboards, retrieval, durable names, relations, projections, or neighbouring authority;
- `front/refresh`: active when variants, non-dominated fronts, archives, refresh, repeated findings, or no-forced-winner cases are live.

Inactive coordinates are not passes, waivers, or hidden failures. They are outside the current pattern-quality claim.

| Characteristic | Activation class | What it reads | Good state |
|---|---|---|---|
| `WorkingSituationAndUseBoundaryRecognizability` | first-pass core | Whether the working reader recognises the situation, ordinary use, non-use, harm if missed, and first boundary early. | The reader can say "this is / is not my situation" without reading support apparatus. |
| `ActionPathGuidance` | first-pass core | Whether, after the first admissible move is recoverable, the reader can continue the admissible action path. | The `Solution` carries the action path; the checklist tests it rather than replacing it. |
| `ClosureAndBoundedNonUseRecoverability` | ordinary stop core | Whether stop, repair, narrower use, and neighbouring-pattern application are recoverable. | The reader can tell when the governed move is enough, when to narrow, and where remaining live claims go. |
| `GovernedObjectAndClaimScopeStability` | first-pass core | Whether the governed object and quality-claim scope stay stable across title, problem frame, solution, checklist, cases, relations, and status. | The pattern does not drift between pattern, record, bundle, suite, profile, review-profile result, method, work, support document, or broader/narrower use claim. |
| `SemanticKindAndNameRecoverability` | ordinary stop core; first-pass when names carry FPF force | Whether heads, kinds, relations, qualifiers, support roles, evidence roles, and Tech/Plain names recover the same FPF reading. | Names are usable because they preserve kind, relation, and admissible claim force, not because prose is polished. |
| `NeighborAuthorityAndBoundedUseFit` | first-pass core | Whether neighbouring claims stay with exact receiving patterns and residual weakness is bounded. | Evidence, assurance, measurement, naming, work, gate, decision, publication, causal, release, bridge, and refresh claims do not become `E.21` authority. |
| `PracticalUseDeltaAndHarmPrevention` | first-pass core | Whether the pattern changes a real reader move, prevents a named misuse, reduces named cost or ambiguity, or preserves a named boundary. | The reader can state what action, decision, repair, non-use, or neighbouring-pattern use becomes better because the pattern exists. |
| `UseAffordabilityAndApparatusProportionality` | first-pass core | Whether first use is affordable and the apparatus is proportionate to the live claim. Subreadings: first-use cost and apparatus proportionality. | Ordinary use stays light; heavier fields, cards, telemetry, front/archive, support, or evidence apparatus appear only when their live claim buys admissible use. A weak live subreading limits the coordinate value; do not average the subreadings. |
| `RepairLocalityAndChangeImpactPredictability` | ordinary stop core | Whether repairs stay local and downstream impact is predictable. | The repair has the smallest live locus, known impact radius, and no unnecessary changes to names, relations, support records, evidence refs, or entry/projection loci. |
| `ProxyForValueSubstitutionResistance` | ordinary stop core | Whether the quality read prevents Goodhart substitution of rubric satisfaction for pattern-use value. | The read asks what got worse and treats usability, affordability, maintainability, neighbour costs, and bounded non-use as quality evidence rather than afterthoughts. |
| `ClaimSupportTraceabilityCurrentnessAndReplayability` | claim-support | Whether another reader can replay the claim from pinned text, scope, evidence refs, currentness basis, limitations, status, and stop reason. | The claim is traceable and replayable without chat memory, steward memory, or administrative placement state; project assurance stays outside `E.21` and under exact receiving patterns. |
| `CaseCountercaseAndTransferCoverage` | claim-support | Whether positive cases, near-misses, anti-cases, and transfer cases match claimed breadth. | Cases test the main misuse paths and boundary transfers; broad claims have heterogeneous support or explicit narrowing. |
| `SoTABindingAndCurrentness` | claim-support | Whether SoTA, lineage, rejected practice, and refresh triggers are separated and tied to a live pattern-quality claim. | Adopt/adapt/reject stances mutate `Solution`, checklist, boundary, relation, worked case, stop, or reopen condition. |
| `FormalClaimLegalityAndLensFit` | claim-support | Whether measurement, score, comparison, scale, threshold, formal model, or lens claim is legal and bounded. | Scale/comparability basis and preserved/lost structure are visible; non-admissible formal use is named. |
| `FalsifiabilityAndLoweringCondition` | claim-support | Whether high values, status claims, and stop claims say what would lower or reopen the read. | Values `4`/`5`, `admissibleForDeclaredUse`, and stop decisions carry concrete lowering conditions unless the declared use is only first-pass repair triage. |
| `ExternalEntryAndProjectionIntegrity` | corpus/publication | Whether ToC/J.4/Preface cues, cards, summaries, dashboards, generated explanations, retrieval snippets, or thin echoes preserve the governed read. | External projections guide entry by value and scope; they do not become approval badges, authority faces, project evidence, or second semantic tracks. |
| `PatternLanguageEcologyFit` | corpus/publication | Whether the pattern preserves FPF corpus health: relation fanout, name collision risk, entry-map clarity, support-role parity, stale echoes, and neighbouring-authority distribution. | Local improvement does not create corpus-level confusion, relation explosion, entry pollution, stale echoes, or shadow authority. |
| `EvolutionFrontAndRefreshDiscipline` | front/refresh | Whether variants, fronts, archives, refresh windows, no-forced-winner cases, and smallest-live-reopen rules preserve open-ended evolution without endless polishing. | Non-dominated candidates can remain visible until a declared receiving action requires one selected candidate; refresh reopens the smallest live locus. |

**Activated overlays.** These overlays are not ordinary coordinates. They become active only when the pattern version or declared `ClaimScope` makes the issue live.

| Overlay | Activation | Good state |
|---|---|---|
| `ConstraintAndHarmBoundaryFit` | Active when the pattern version contains safety, security, ethics, compliance, deontic, harm-prevention, prohibited-use, non-negotiable constraint, or project-risk claims. | Constraint and harm boundaries are visible, exact receiving patterns are named, and no pattern-quality result is overread as safety, security, compliance, ethics, or project approval. |
| `SelfApplicationAndRecursionBoundary` | Active for meta-patterns that govern pattern authoring, review, quality, naming, publication, SoTA, epistemic precision repair, or characteristic spaces. | The pattern can be applied to itself at the lowest sufficient layer without recursive bundles, infinite review, or self-certifying authority. |

#### E.21:4.4 - DominanceSet, TieBreakerSet, TelemetrySet

`DominanceSet` names the subset of activated characteristics selected for the current `ClaimScope`. The coordinate menu in `E.21:4.3` is not one always-on grid.

For one first ordinary read of one pattern version under quality read, the minimal active coordinates are:

- `WorkingSituationAndUseBoundaryRecognizability`;
- `ActionPathGuidance`;
- `GovernedObjectAndClaimScopeStability`;
- `NeighborAuthorityAndBoundedUseFit`;
- `PracticalUseDeltaAndHarmPrevention`;
- `UseAffordabilityAndApparatusProportionality`.

For admission, stop, repair-before-use, or narrowed-use closure, add the ordinary stop core coordinates:

- `ClosureAndBoundedNonUseRecoverability`;
- `SemanticKindAndNameRecoverability` when names/kinds carry FPF force beyond eligibility minimum;
- `RepairLocalityAndChangeImpactPredictability` when an edit or repair is being judged;
- `ProxyForValueSubstitutionResistance` before any stop or comparison claim.

Activate claim-support, corpus/publication, front/refresh coordinates, and activated overlays only when the pattern version, candidate edit, or declared `ClaimScope` makes their claim force live.

Inactive coordinates are outside the current pattern-quality claim. They are not passes, waivers, or hidden failures.

A candidate pattern version `A` dominates candidate `B` only when:

1. both pass the active `EligibilitySet`;
2. `A` is no worse than `B` on every active dominance coordinate;
3. `A` is better on at least one active dominance coordinate; and
4. `A` does not create a new hard blocker, an unacceptable drop in `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, or `ProxyForValueSubstitutionResistance`, or an unacceptable unscored increase in reader, author, maintainer, migration, evidence, entry/projection, corpus, or neighbour-integration cost.

`TieBreakerSet` is used only among non-dominated candidates. Default tie-breakers are:

| Tie-breaker | Preference |
|---|---|
| `ExistingPatternReuse` | Reuse existing FPF patterns and fields when precision is equal. |
| `MintedNameParsimony` | Mint fewer durable names when semantic fidelity is equal. |
| `ReaderCost` | Lower first-use cost when action guidance and ontology precision are equal. |
| `AuthorCost` | Fewer required declarations when safety and reviewability are equal. |
| `MaintainerCost` | Lower refresh and relation-maintenance cost when quality is equal. |
| `EntryDiscoverability` | Better practical first-entry cues when local precision is equal. |

Cost tie-breakers are not a hiding place for live quality loss. If reader, author, reviewer, maintainer, migration, evidence, entry/projection, corpus, or neighbour-integration cost can change admissible use, represent it through `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, `ProxyForValueSubstitutionResistance`, or another active coordinate before using tie-breakers.

**Support material retention test.** A support card, telemetry fixture, archive row, worked slice, proof sketch, or companion note remains attached to the pattern-quality read only when the read states what real quality breakage would return if it were absent.

If no breakage is named, fold the useful content into the pattern body, keep it as accepted basis only, or remove it from the active quality read.

**High-assurance separation rule.** When high-assurance reuse needs additional evidence, proof sketches, telemetry, or support cards, preserve the ordinary pattern body's first admissible move unless the ordinary use itself changes.

High-assurance material should normally live in a named support card, worked slice, or neighbouring evidence/assurance pattern. It should not be inserted into the ordinary `Solution` if doing so makes first use harder for the declared ordinary reader.

`TelemetrySet` is optional for early drafts and useful for mature or high-use patterns. Telemetry is an activation signal for reopening or calibration, not a standing requirement for every pattern-quality read. Typical telemetry includes:

| Telemetry | Reopen signal |
|---|---|
| `reviewReturnDensity` | P1/P2/P3 findings per pattern or per 1k lines are not falling. |
| `repeatFindingRate` | The same defect class returns after repair. |
| `coldReaderMisentryRate` | Readers choose the wrong first pattern or wrong neighbouring exit. |
| `retrievalHitQuality` | Search or RAG finds the wrong pattern, wrong section, or unsupported summary. |
| `neighborBreakageCount` | A pattern change repeatedly forces downstream repairs. |
| `patternUseAvoidanceSignal` | Readers avoid the pattern, copy only fragments, or return to informal shortcuts because the quality apparatus is too costly. |
| `maintenanceRippleSignal` | Small pattern repairs repeatedly force unrelated name, relation, evidence, or support edits. |
| `proxyOptimizationSignal` | Edits improve checklist or coordinate wording while first-use failures, return findings, or practical-payoff complaints persist. |
| `workedCaseCoverageDelta` | Edits polish wording without adding or preserving live case coverage. |
| `terminologyCollisionCount` | New names collide with existing FPF heads or kinds. |
| `SoTAStalenessSignals` | Current-practice claims now depend on stale or superseded anchors. |

Refresh opens the smallest live locus: the affected source stance, neighbour relation, coordinate reading, worked case, name, eligibility row, or status payload. It reopens the whole pattern-quality read only when that local change can change `PatternQualityStatus` or `StopCondition`.

#### E.21:4.5 - StopCondition

Improvement can stop for the declared scope only when the `PatternQualityQBundle` satisfies:

```text
StopCondition :=
  EligibilitySet passes
  AND the pattern text is an action-guiding FPF pattern under E.8 for the declared use
  AND the first move is recoverable from Problem frame and Solution, or the claim is narrowed to support-only use
  AND no open P1/P2 pattern-quality findings for the declared ClaimScope
  AND all active DominanceSet coordinates meet the declared floor
  AND no active coordinate is 0 or 1 for a use the pattern claims to support
  AND the current candidate is non-dominated on the active DominanceSet
  AND the next proposed edits are TieBreaker-only or cosmetic for this scope
  AND no active improvement creates unmeasured usability, affordability, repair-impact, entry/projection, corpus-ecology, or neighbour-ripple loss outside the DominanceSet
  AND remaining weaknesses are expressed as bounded non-use or a named receiving pattern
  AND TelemetrySet, when active, shows no recurring blocker class
```

No stop condition may close while a visible coordinate improvement creates unmeasured loss in first-use cost, reader comprehension, maintainer locality, neighbour stability, bounded non-use clarity, or practical payoff.

The ordinary floor for an admission-ready pattern is `3 sufficientlyExpressedForDeclaredUse` on every active coordinate. A lower coordinate may remain only by narrowing `ClaimScope`, `WorkingReaderScope`, or `IntendedUse`; it is not hidden in an average.

#### E.21:4.6 - PatternQualityFront and PatternImprovementArchive

A `PatternQualityFront` is live only when at least two candidate versions or candidate edits are being compared.

A `PatternImprovementArchive` is live only when preserving rejected or near-miss variants changes future repair, refresh, or selection.

Do not create either construct for a single ordinary repair unless a candidate comparison or contested stop decision is already live.

When these constructs are live, keep:

| Construct | Meaning |
|---|---|
| `PatternQualityFront` | The current non-dominated set of pattern candidates under the active `EligibilitySet`, `DominanceSet`, and cost coordinates. |
| `PatternImprovementArchive` | A bounded archive of candidate edits, rejected variants, near-miss versions, and trade-off notes that explain why one candidate was not selected. |

This is the pattern-quality analogue of NQD/front discipline. It prevents "one winner" thinking while still allowing one candidate to be selected for the current `ClaimScope`.

The archive is not required for every small edit. It becomes useful when several plausible versions trade off `SemanticKindAndNameRecoverability`, reader cost, `SoTABindingAndCurrentness`, `CaseCountercaseAndTransferCoverage`, `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, or `ProxyForValueSubstitutionResistance`.

`PatternImprovementArchive` records candidate-edit trade-off evidence only. It is not chat memory, process chronology, review history, backlog, or permanent appendix.

#### E.21:4.6a - No forced winner

When several candidates are non-dominated under the active `EligibilitySet`, `DominanceSet`, and cost coordinates, `E.21` SHALL NOT force one winner unless the declared `IntendedUse` requires one selected candidate.

If ordinary drafting, exploration, or architecture discussion remains live, the admissible output may be a scoped `PatternQualityFront` with each candidate's bounded use and known trade-off. A single selected version is required only when admission, landing-support, release-support, high-assurance reuse, or another receiving action requires one candidate by value.

Choosing one candidate from a non-dominated front requires either:

* a declared `TieBreakerSet` that does not override hard blockers or live quality loss;
* a narrowed `ClaimScope` or `WorkingReaderScope`;
* a named neighbouring decision pattern when the choice is no longer a pattern-quality read.

#### E.21:4.7 - Relationship to E.19

`E.21` supplies the characteristic space and stop condition for pattern-quality claims. `E.19` supplies the review profile, findings-first run record, and admission/refresh outcome.

Use them together this way:

1. Use `E.8` to author the pattern.
2. Use `E.21` to state the quality bundle and non-scalar stop condition.
3. Use `E.19` to run the selected review profiles and record findings.
4. If an `E.19` finding changes the quality read, update the `PatternQualityQBundle`; do not turn the `E.19` verdict into a scalar score.
5. If the pattern version is being improved through repeated passes, use `E.23` for the repeated method while `E.21` continues to supply the pattern-quality values and stop meanings.


An `E.19` pass, return, or absence is not itself a coordinate value. It may supply evidence about the pattern text, expose a content defect, justify a confidence judgement, or constrain the admissible `ClaimScope`; it does not change the same `FormalClaimLegalityAndLensFit`, `SemanticKindAndNameRecoverability`, `ActionPathGuidance`, or `ClosureAndBoundedNonUseRecoverability` coordinate reading by administrative state alone.

Do not call an `E.21` `EligibilitySet`, `PatternQualityStatus`, `StopCondition`, or coordinate floor a gate. `E.21` states a scoped pattern-quality read. `E.19` runs pattern-quality review profiles. `A.21` governs operational gate decisions. These three uses do not collapse by metaphor.


An `E.21` result is still a pattern-quality result. It is not project evidence, safety certification, gate passage, assurance acceptance, work authority, release approval, or publication truth unless the exact receiving pattern opens that project-side relation.

#### E.21:4.8 - Minimal PatternQualityQBundle card
**Ordinary first-pass slice.** This is not a new kind. It is the smallest admissible slice of `PatternQualityQBundle` for one first read of one pattern version under quality read.

```text
PatternQualityQBundle / first-pass slice:
  PatternVersionRef:
  WorkingReaderScope:
  IntendedUse:
  QualificationWindow:
  FirstMoveEvidenceRef: <Problem frame / Solution / named neighbouring-pattern application>
  EntryBlockers: <none | first move absent | governed object drift | checklist-as-solution | apparatus overreach | neighbour overread | other activated blocker>
  MinimalDominanceSet: <default six coordinates, plus activated coordinates if live>
  PatternQualityStatus:
  Next admissible repair or bounded non-use:
```

The full one-screen card is used when the first-pass slice survives or when the declared use requires coordinate evidence, variant comparison, admission, refresh, high-assurance reuse, or contested stop.

The fuller card remains one screen when Layer 1, comparison, admission, refresh, high-assurance reuse, or contested stop makes it live:

```text
PatternQualityQBundle:
  PatternVersionRef: <pattern id + edition or host path>
  ClaimScope: <ordinary authoring support quality read | admission-support quality read | refresh-support quality read | landing-support quality read | external-review-support quality read | high-assurance-reuse support quality read | ...>
  WorkingReaderScope: <primary reader + first-use situation>
  IntendedUse: <what this quality read may support>
  QualificationWindow: <edition / SoTA / neighbour / release window>
  EligibilitySet: <pass/fail rows with blockers>
  DominanceSet: <selected coordinates + floor>
  CoordinateEvidenceRefs: <text sections, worked cases, SoTA rows, relation checks, or findings that support coordinate values; not placement/review state alone>
  PatternQualityStatus: <value set from E.21:4.1>
  StopCondition: <satisfied | not satisfied, with exact reason>
  EvidenceRefs: <worked cases, SoTA rows, review refs, source refs>
```

#### E.21:4.8a - Publication and projection boundary for quality cards

A rendered `PatternQualityQBundle`, first-pass slice, quality table, status badge, or dashboard tile is a publication or projection of the pattern-quality read. It is not the pattern version, not the authority source, not project evidence, not release approval, not gate passage, and not assurance acceptance.

When the rendered card is used as a bounded publication unit, the card SHALL keep visible:

1. the exact `PatternVersionRef`;
2. the carried move: scoped pattern-quality read, first-pass slice, variant comparison, stop/non-stop reason, or bounded non-use;
3. the outside boundary to project evidence, assurance, gate, release, work, and publication truth;
4. the exact receiving pattern when a downstream claim is live.

A ToC row, `J.4` row, README note, dashboard tile, or generated summary may echo an `E.21` result only as a thin orientation cue unless it cites the full governed quality read by value.

Generated summaries, retrieval snippets, README lines, ToC reminders, and `J.4` entries may expose an `E.21` result only as `thin echo` or controlled coarsening.

A thin echo may say:

* `<PatternVersionRef> has PatternQualityStatus = repairBeforeUse for ordinary use because first move is absent. See <quality read ref>.`

A thin echo SHALL NOT say:

* `approved pattern`;
* `safe pattern`;
* `compliant pattern`;
* `quality passed`;
* `do not use this pattern` without scope;
* `E.21 certified this pattern`.

If a generated or coarsened rendering is used for reliance beyond orientation, apply the exact receiving pattern live: `A.6.3.CSC`, `E.17.EFP`, `E.17.AUD`, `A.10`, or `B.3`, as applicable.

#### E.21:4.9 - Reader move loop

The fast entry loop for one pattern version under quality read is:

1. write the pattern-version line: `<PatternVersionRef> for <WorkingReaderScope> under <IntendedUse> within <QualificationWindow>`;
2. read only the pattern version's `Problem frame` and `Solution` until one first admissible action-guiding move is recoverable;
3. if no first move is recoverable, or if the move lives only in the Conformance Checklist, assign `PatternQualityStatus = repairBeforeUse` for the declared use unless a narrower support-only use is explicitly named;
4. if the first move is recoverable, check the default six first-pass coordinates and any activated coordinates;
5. expand to the full comparison and stop loop only when a stop decision, variant comparison, admission, refresh, high-assurance reuse, or contested neighbour claim is live.

The full comparison and stop loop is:

1. name the exact `PatternVersionRef`;
2. declare `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`;
3. check activated `EligibilitySet` rows before comparing coordinates;
4. read each active coordinate from `CoordinateEvidenceRefs`, not from administrative state;
5. ask what became worse when the visible coordinates improved: first-use affordability, author/reviewer effort, repair-impact predictability, entry/projection integrity, corpus ecology, neighbour ripple, and proxy-for-value substitution;
6. compare candidates through `DominanceSet` only after eligibility passes and Goodhart-risk questions are visible;
7. use `TieBreakerSet` only among non-dominated candidates;
8. assign one `PatternQualityStatus`;
9. state whether `StopCondition` is satisfied or which bounded non-use, receiving pattern, or content repair remains.

If the reader cannot recover the fast-entry result for one pattern version, activated `firstMoveRecoverability` fails for ordinary use even when the prose is polished. If the first move is recoverable but the reader cannot continue the admissible action path, `ActionPathGuidance` is below `4 wellExpressedForDeclaredUse` for ordinary use. If the reader cannot perform the closure and bounded non-use loop when that loop is live, `ClosureAndBoundedNonUseRecoverability` cannot support stop closure for that declared scope.

#### E.21:4.10 - CoordinateEvidenceRefs support card

`CoordinateEvidenceRefs` may be inline section references, short claims, review findings, worked slices, or full support cards. Full support cards are required only when the coordinate value is contested, reused for high-assurance closure, used across several candidate variants, or cited outside the local pattern-quality read.

`CoordinateEvidenceRefs` is the local evidence list for coordinate values. It is support for coordinate readings, not a coordinate family by itself.

`CoordinateEvidenceRef := <Coordinate, EvidenceKind, HostSectionRef, Claim, Limitation, LoweringCondition?>`

`LoweringCondition?` is required only when a coordinate value is `4` or `5`, or when the coordinate supports `admissibleForDeclaredUse` or `StopCondition`.

It states one concrete content discovery, reader failure, neighbour conflict, SoTA change, worked-case counterexample, cost increase, entry/projection overread, corpus-ecology conflict, or affordability loss that would lower the coordinate or reopen the read.

A lowering condition is not a test suite and not a review plan. It is a falsifiability hook for the current pattern-quality claim.

Default evidence kinds:

| EvidenceKind | Use |
|---|---|
| `recognitionTextEvidence` | Shows why a working reader can recognise the situation, boundary, and first move. |
| `namePrecisionCardEvidence` | Shows why a minted or FPF-force-bearing token has a recoverable kind, relation claim force, admissible use, and non-admissible use. |
| `relationClosureEvidence` | Shows that neighbouring-pattern claims stay with their governing patterns. |
| `workedCaseEvidence` | Shows the coordinate in a positive case, near-miss, anti-case, countercase, transfer case, or heterogeneous application case. |
| `sotaImplicationEvidence` | Shows how a source changes `Solution`, checklist, relation, boundary, worked case, stop condition, or reopen condition. |
| `measurementScaleEvidence` | Shows Characteristic/Scale/Coordinate discipline and blocks illegal arithmetic. |
| `costAndUseEvidence` | Shows first-use, author, reviewer, maintainer, migration, entry/projection, corpus, or ordinary-use cost under the declared scope. |
| `maintenanceRippleEvidence` | Shows whether one pattern repair creates unnecessary cross-FPF relation, naming, support, evidence, entry, or projection churn. |
| `proxySubstitutionEvidence` | Shows whether a coordinate increase preserves the practical value the coordinate was meant to protect. |
| `supportBoundaryEvidence` | Shows the difference between pattern-quality evidence and project-side evidence, assurance, work, gate, release, or publication truth. |
| `entryProjectionEvidence` | Shows how ToC/J.4/Preface/search/RAG/summary/card/dashboard cues preserve the governed pattern-quality read without replacing it. |
| `corpusEcologyEvidence` | Shows whether the edit changes relation fanout, name collisions, support-role parity, entry-map clarity, stale echoes, or neighbouring authority. |
| `loweringConditionEvidence` | Shows what discovery, failure, countercase, conflict, stale source, or cost increase would lower a high coordinate or reopen the status/stop claim. |

`entryProjectionEvidence` and `corpusEcologyEvidence` are active only when the candidate edit changes durable names, relations, ToC/J.4/Preface entry support, retrieval-facing cues, support projections, summaries, cards, dashboards, or neighbouring-pattern authority. They are not required for local wording repair.

Example support card:

```text
CoordinateEvidenceRef:
  Coordinate: FormalClaimLegalityAndLensFit
  EvidenceKind: measurementScaleEvidence + workedCaseEvidence + sotaImplicationEvidence
  HostSectionRef: E.21:4.3, E.21:4.12, E.21:11
  Claim: Q-Bundle + ordinal characteristic space + Pareto/front lens preserve the comparisons needed for pattern improvement while rejecting scalar averages.
  Limitation: Not a statistical estimator, project assurance result, or tool mandate.
  LoweringCondition: If an E.21 edit permits arithmetic averaging of ordinal coordinate values, lower this coordinate to <=2 for ordinary use.
```

#### E.21:4.10a - Pattern-quality finding sentence grammar

A pattern-quality finding is admissible only when it has this shape:

```text
Pattern-quality finding:
  PatternVersionRef: <PatternVersionRef>
  ClaimScope / reader / use / window:
  Finding kind: <eligibility blocker | coordinate reading | status payload | stop-condition failure | bounded non-use | neighbouring-pattern application>
  Exact E.21 locus: <EligibilitySet row | coordinate | status | stop clause>
  Content evidence: <HostSectionRef / worked case / SoTA row / relation check / review finding>
  Result: <PatternQualityStatus effect or coordinate value effect>
  First admissible repair or bounded non-use:
```

Forbidden finding shapes:

* `weak pattern`;
* `not FPF enough`;
* `quality low`;
* `review failed`;
* `needs more evidence`;
* `not safe/compliant`;
* `too complex`;
* `not ready`.

These are admissible only after rewriting into the exact `E.21` locus, content evidence, status effect, and first admissible repair or bounded non-use.

#### E.21:4.11 - Local name-precision cards for E.21 heads

These cards are local name-precision evidence for `E.21`; they are not a separate glossary. Coordinate names are defined in `E.21:4.3` and are not repeated here unless the token also names a local construct.

The `E.21:4.11` local name-precision cards are the local `F.18`-compatible settlement for `E.21` heads. They do not require separate full `Name Card` artifacts for ordinary use.

A full `F.18` Name Card is required only when an `E.21` head is reused outside `E.21`, collides with an existing FPF head, enters a UTS/Concept-Set row, or becomes a durable cross-pattern naming decision rather than a local field/value-set name.

| Token | Kind named | Relation claim force | Admissible use | Non-admissible use |
|---|---|---|---|---|
| `PatternQualityQBundle` | Q-Bundle specialization for one pattern-quality claim. | Binds pattern version, scope, coordinates, evidence, status, and stop condition. | State a scoped non-scalar quality read. | Universal maturity score, review verdict, release approval, or project certification. |
| `PatternQualityEvaluationCharacteristicSpace` | CharacteristicSpace specialization for FPF pattern-quality coordinates. | Holds ordinal pattern-quality coordinates and their scale discipline. | Compare content properties of pattern versions. | Geometric space, administrative state map, or popularity ranking. |
| `EligibilitySet` | Set-valued hard-filter field inside `PatternQualityQBundle`. | Filters candidate versions before coordinate comparison. | Block hard defects before front reasoning. | Low-score region, soft preference list, review profile, or gate profile. |
| `DominanceSet` | Set-valued coordinate-selection field inside `PatternQualityQBundle`. | Defines the active Pareto comparison relation after eligibility passes. | Compare candidates without scalarization. | Total order, average, hidden priority stack, or selector policy. |
| `CoordinateEvidenceRef` | Local evidence-reference record for one coordinate value. | Connects one coordinate value to text, cases, SoTA, relation checks, or findings. | Justify one coordinate reading by content. | Administrative placement, review state, or project evidence by itself. |
| `CoordinateEvidenceRefs` | Set-valued field of `CoordinateEvidenceRef` records. | Holds the evidence refs for active coordinate readings. | Keep coordinate values inspectable. | Support archive, review verdict, or proof package. |
| `TieBreakerSet` | Set-valued secondary-preference field inside `PatternQualityQBundle`. | Breaks ties only after dominance cannot choose. | Prefer lower reader/author/maintainer cost when quality is equal. | Secret dominance coordinate or override for hard blockers. |
| `TelemetrySet` | Set-valued reopen/calibration signal field inside `PatternQualityQBundle`. | Connects return, retrieval, drift, and repeat-finding signals to refresh. | Reopen or calibrate the pattern-quality read. | Project certificate, popularity count, or replacement for content evidence. |
| `PatternQualityStatus` | Local admissible-use value set inside `PatternQualityQBundle`. | Names admissible use, narrowed use, repair, architecture decision, or refresh for the scoped pattern-quality claim. | Express the outcome of the bundle. | Gate passage, release state, role state, assurance acceptance, or project approval. |
| `PatternQualityFront` | Non-dominated candidate set under the active quality relation. | Preserves multiple viable candidates without one scalar winner. | Select among pattern versions or candidate edits. | Permanent backlog, generic archive, or mandatory tool artifact. |
| `PatternImprovementArchive` | Bounded archive of candidate edits and rejected variants. | Keeps trade-off evidence for selected/non-selected candidates. | Explain why one candidate was selected for a scope. | Process log, chat transcript, or mandatory historical appendix. |

**Plain twins for ordinary reading.** These Plain twins are reader aids only; the Tech head remains authoritative.

| Tech head | Plain twin | Guard |
|---|---|---|
| `PatternQualityQBundle` | pattern-quality read bundle | Not a review packet, score sheet, or gate file. |
| `PatternQualityEvaluationCharacteristicSpace` | pattern-quality coordinate space | Not a metric dashboard or maturity model. |
| `PatternQualityStatus` | pattern-quality use posture | Not release status, gate decision, or assurance level. |
| `EligibilitySet` | hard blockers | Not low-score items. |
| `DominanceSet` | active quality coordinates | Not weighted criteria. |
| `CoordinateEvidenceRef` | coordinate support reference | Not project evidence by itself. |
| `PatternQualityFront` | non-dominated pattern-edit set | Not backlog or shortlist by itself. |
| `PatternImprovementArchive` | bounded pattern-edit trade-off archive | Not process log or permanent appendix. |

#### E.21:4.12 - Mathematical lens adequacy proof sketch

The mathematical lens in `E.21` is a finite ordinal characteristic-space lens plus a Pareto/front comparison over candidate pattern versions.

| Lens component | Preserved structure | Lost or rejected structure | Practical payoff |
|---|---|---|---|
| Q-Bundle tuple | Keeps pattern version, scope, evidence, coordinates, status, and stop condition together. | Rejects unscoped quality adjectives. | A quality claim can be inspected without reading chat memory. |
| Ordinal characteristic coordinate | Keeps coordinate identity and ordered levels. | Rejects cardinal distance, averages, percentages, and hidden normalization. | `3` and `4` mean content states, not arithmetic quantities. |
| Eligibility predicate | Keeps hard preconditions outside optimization. | Rejects averaging hard blockers into good coordinates. | Undefined vocabulary, shadow authority, or scale illegality blocks comparison. |
| Pareto dominance relation | Keeps non-dominated alternatives visible. | Rejects one universal total order. | Shorter, more exact, and more SoTA-rich variants can coexist until a scope chooses. |
| Tie-breaker preference | Keeps secondary preferences after non-domination. | Rejects secret reweighting of the main coordinates. | Reader cost or continuity can choose only when quality comparison does not. |
| Goodhart-risk check | Keeps the relation between coordinate improvement and intended pattern-use value explicit. | Rejects "all visible coordinates improved" as sufficient when use, affordability, repair locality, entry/projection integrity, corpus ecology, or neighbour fit got worse. | A quality read must ask what became worse before it can stop. |
| Front/archive pair | Keeps selected and non-selected candidate evidence bounded. | Rejects endless polishing and permanent process history. | Improvement can stop without losing important trade-off evidence. |

The lens is admissible because pattern quality is multi-characteristic, ordinal, and scope-dependent. It is not admissible for estimating user adoption, certifying project safety, proving product compliance, or assigning a universal quality number. The stop condition closes the lens: once eligibility passes, floors are met, the candidate is non-dominated, remaining weaknesses are bounded, no active coordinate improvement hides affordability, repair-impact, entry/projection, corpus-ecology, or neighbour loss, and live telemetry shows no recurring blocker class, additional edits must show a real front movement rather than a cosmetic preference.

### E.21:5 - Archetypal Grounding

**Tell.** A good FPF pattern is not merely complete, attractive, or formally strict. It is an action-guiding method description whose quality is a scoped bundle: it helps the right reader recognise the right situation, make the next admissible move, avoid the wrong neighbour, and trust the result for the declared use.

**Recognition matrix.**

| Working situation | First honest `E.21` move | Likely wrong substitute | Coordinate tested |
|---|---|---|---|
| A system-architecture pattern has precise vocabulary and current, exact sources, but the opening never says what an engineer-manager does first. | Check activated `firstMoveRecoverability`; if it passes, read `WorkingSituationAndUseBoundaryRecognizability` and `ActionPathGuidance` from the opening and `Solution`. | Treat source currentness and fit as enough for admission. | `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, `ActionPathGuidance`, `SoTABindingAndCurrentness`. |
| A publication or evidence pattern reads beautifully, but `PatternQualityStatus = admissibleForDeclaredUse` is being cited as product assurance. | Keep the quality result as pattern-quality evidence and cite `A.10`/`B.3` only when the project-side claim is live. If a card, summary, or status line is visible, check whether the projection stays a scoped echo. | Treat review approval as project certification. | `NeighborAuthorityAndBoundedUseFit`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, `ExternalEntryAndProjectionIntegrity`. |
| A mathematical-lens pattern has the right formula vocabulary, but no preserved/lost structure or non-use boundary. | Require the formal/lens proof sketch: preserved structure, rejected structure, payoff, admissible use, non-admissible use, and stop condition. | Count formal notation as sufficient lens fit. | `FormalClaimLegalityAndLensFit`. |
| A naming-heavy pattern has better prose after editing, but the kind and relation claim force are still ambiguous. | Fill local name-precision cards or use the full `F.18 -> A.6.P -> E.10` chain. | Treat lexical polish as ontology repair. | `SemanticKindAndNameRecoverability`. |
| Two variants both pass eligibility: one is shorter; the other has more informative examples and relation closure. | Compare through `DominanceSet`, then use `TieBreakerSet` only if neither dominates. | Average scores or choose the version that feels cleaner. | `UseAffordabilityAndApparatusProportionality`, `CaseCountercaseAndTransferCoverage`, `EvolutionFrontAndRefreshDiscipline`. |
| A pattern-quality read raises every visible coordinate to `4` or `5`, but the pattern becomes longer, harder to enter, and more expensive to maintain. | Activate `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance`; ask what became worse before accepting the stop condition. | Treat "all coordinates are high" as enough by itself. | `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ProxyForValueSubstitutionResistance`. |

**Show - System pattern.** A system-architecture pattern has precise structure vocabulary and a current, exact SoTA row, but its opening never says what an engineer-manager should do first. Activated `firstMoveRecoverability` fails for ordinary use. The admissible result is not "quality 78/100"; it is `repairBeforeUse` for admission, or `admissibleWithNarrowerUse` if it is kept as expert-only support.

**Show - First-pass pattern-version read.** An author opens a candidate FPF pattern and writes: `PatternVersionRef = C.xx@draft-3; WorkingReaderScope = engineer-manager using the pattern for first ordinary application; IntendedUse = continue drafting or repair before use; QualificationWindow = current FPF edition`.

The author reads only `Problem frame` and `Solution`. If the pattern says which object it governs but gives no first admissible action-guiding move, the first-pass read closes: activated `firstMoveRecoverability` fails and `PatternQualityStatus = repairBeforeUse` for ordinary use. No `PatternQualityFront`, `TelemetrySet`, or full coordinate table is needed.

If the first move exists but the continuation path or apparatus required to apply it is heavier than the ordinary case can justify, activate `ActionPathGuidance` and `UseAffordabilityAndApparatusProportionality`. The repair is to keep the ordinary first move light and move heavier support to a named neighbouring pattern or high-assurance support card.

**Show - Episteme pattern.** A publication or evidence pattern reads beautifully and has many examples, but it treats an `E.19` pattern-quality result as project assurance. `NeighborAuthorityAndBoundedUseFit` and `ClaimSupportTraceabilityCurrentnessAndReplayability` fail because assurance belongs in `B.3` and evidence/currentness belongs in `A.10`. If a dashboard tile or generated summary repeats the result without scope and status payload, `ExternalEntryAndProjectionIntegrity` also fails. The repair is to keep the pattern-quality result as pattern-quality evidence and open the exact project-side receiving relation only when needed.

**Show - Mathematical lens pattern.** A pattern says that it uses a characteristic space, but then compares variants by "overall quality". `FormalClaimLegalityAndLensFit` fails because the ordinal coordinates are being collapsed and the preserved and rejected structures are not named. The repair is to state the finite ordinal coordinate set, eligibility predicate, dominance relation, tie-breaker boundary, and non-admissible scalar uses.

**Show - New pattern candidate.** Two drafts of the same pattern both pass eligibility. Draft A is shorter and easier to read; Draft B has better SoTA, case/countercase breadth, and neighbour closure but adds a heavier bundle card. Neither dominates if Draft B's extra apparatus is live only for high-assurance reuse. The correct output may be one ordinary draft plus a support card for high-assurance use, not one averaged winner.

**Show - Goodhart trade-off.** An author raises visible E.21 coordinates to high values by adding proof sketches, support cards, and SoTA rows. The pattern now reads better on the visible table, but a cold author needs more time to find the first move and a maintainer must update more named sections or evidence records after each small repair. The quality read cannot stop until `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance` are read by content evidence. If those coordinates fall, the candidate is not an improvement for the declared ordinary-use scope; it may become a high-assurance variant instead.

**Show - Self-application support card.**

```text
CoordinateEvidenceRef:
  Coordinate: ActionPathGuidance
  EvidenceKind: recognitionTextEvidence + workedCaseEvidence
  HostSectionRef: E.21:1, E.21:4.9, E.21:5
  Claim: The reader has a first move, a continuation loop, and heterogeneous examples that show when the loop changes the quality result.
  Limitation: This is pattern-quality guidance, not project-side work authorization.
```

### E.21:6 - Bias-Annotation

`E.21` intentionally biases evaluation away from single scores, reviewer taste, and flat audit grids and toward activation-normalized characteristic spaces. This supports `P-1 Cognitive Elegance`, `P-2 Didactic Primacy`, `P-7 Pragmatic Utility`, `P-10 Open-Ended Evolution`, and `P-11 SoTA Alignment`.

Lens cautions:

| Lens | Bias to watch | Counter-move |
|---|---|---|
| Governance | A quality result may be overread as approval, release, or certification. | Keep `PatternQualityStatus` scoped to FPF pattern quality and name receiving project-side patterns separately. |
| Architecture | The pattern may centralize all quality concerns and steal authority from `E.8`, `E.19`, `C.16`, `C.25`, or `F.18`. | State exact relations and keep each neighbour's governing object intact. |
| Activation | The declared coordinate menu may become a hidden checklist. | Use activation classes and inactive-coordinate non-reading: inactive coordinates are outside the claim, not passes, waivers, or hidden failures. |
| Formal and corpus/publication | Formal and corpus/publication coordinates may become bureaucracy. | Activate them only when the pattern version or candidate edit changes those claims, entry/projection loci, names, relations, retrieval behavior, or corpus ecology. |
| Merged coordinates | A merged coordinate may hide a weak subreading. | A weak live subreading limits the coordinate value; do not average subreadings. |
| Onto/Epist | Quality terms may become generic umbrellas. | Use declared Characteristics, scales, kind-specific coordinates, and exact status values. |
| Pragmatic | The bundle may become too heavy for ordinary pattern drafts. | Keep the one-screen card as default and add telemetry/front/archive only when live. |
| Goodhart | The declared coordinates may become proxy objectives and displace the pattern-use value they were meant to protect. | Activate affordability/apparatus, change-impact, corpus/projection, and proxy-substitution coordinates when their cost changes admissible use; ask what got worse before stopping. |
| Didactic | Pareto/front language may obscure the reader's first move. | Pair every technical construct with the practical question it answers. |

#### E.21:6a - Architectural characteristics preserved by this pattern

| Architectural characteristic | How `E.21` preserves it | Failure to prevent |
|---|---|---|
| Auditability & traceability | `PatternQualityQBundle` pins version, scope, evidence, status, and stop condition; `ClaimSupportTraceabilityCurrentnessAndReplayability` keeps support replayable when claim support is live. | Quality claims depending on chat memory, reviewer taste, or placement state. |
| Evolvability | `QualificationWindow`, `refreshNeeded`, bounded non-use, optional telemetry, and `EvolutionFrontAndRefreshDiscipline` reopen only the live locus. | Whole-pattern churn after small source, neighbour, or wording changes. |
| Modularity | `E.21` keeps authoring, review, measurement, naming, evidence, assurance, gate, work, and release claims under exact neighbouring patterns. | Central quality subsystem or shadow authority. |
| Composability | `NeighborAuthorityAndBoundedUseFit` and relation closure keep pattern-quality claims safe to compose with neighbouring patterns. | One pattern-quality read stealing another pattern's governed object. |
| Usability | First-pass slice checks `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, and `ActionPathGuidance` before heavy apparatus. | Type-correct but inert pattern-quality control. |
| Affordability | `UseAffordabilityAndApparatusProportionality` and activation layers keep ordinary reads light. | Review bureaucracy masquerading as quality. |
| Measurement integrity | Ordinal coordinate readings reject averages, percentages, and hidden normalization; `FormalClaimLegalityAndLensFit` activates only when formal claim force is live. | Illegal scalarization of pattern quality. |
| Goodhart resistance | Proxy-substitution checks ask what got worse when visible coordinates improved. | Rubric satisfaction replacing practical pattern-use value. |
| Corpus ecology | `ExternalEntryAndProjectionIntegrity` and `PatternLanguageEcologyFit` activate only when entry/projection/retrieval/name/relation/corpus loci are changed or overread. | Local quality win that creates entry noise, stale echoes, name collisions, relation fanout, or shadow authority. |
| Scope safety | `PatternQualityStatus` remains a pattern-quality posture only. | Overread as project assurance, safety/compliance certification, gate, release, or work authority. |
| Checkability | Status payload, `FalsifiabilityAndLoweringCondition`, and `StopCondition` make closure falsifiable for the declared use. | "Looks good enough" without inspectable stop reason. |

This table states which architectural characteristics `E.21` protects; it does not create a separate review process.

### E.21:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| **CC-E21-1 (No single score).** | A pattern-quality read **SHALL NOT** collapse the active characteristics into one arithmetic score, percentage, average, or hidden total order. | Preserves multi-characteristic truth and scale legality. |
| **CC-E21-2 (Bundle scope declared).** | A `PatternQualityQBundle` **SHALL** declare `PatternVersionRef`, `ClaimScope`, `WorkingReaderScope`, `IntendedUse`, and `QualificationWindow`. | Prevents unscoped quality claims. |
| **CC-E21-2a (Question purpose explicit or floor-defaulted).** | A nontrivial `E.21` read **SHALL** state the requested quality-read purpose or cite an `E.22` `QualityReadQuestionFrame`. If omitted, the read is `floorRead` under the declared or receiving-pattern floor, not `exceptionalImprovementRead`. | Prevents blocker audits from masquerading as exceptional-improvement reads and prevents maximal rewrite pressure when only readiness was requested. |
| **CC-E21-3 (Eligibility before dominance).** | The active `EligibilitySet` **SHALL** be checked before dominance, tie-breaker, or front comparison. | Prevents hard blockers from being averaged away. |
| **CC-E21-4 (Status value set).** | The result **SHALL** use one `PatternQualityStatus` value from `E.21:4.1` or explicitly define a local extension with a narrower meaning. | Keeps outcomes portable and non-vague. |
| **CC-E21-5 (Declared coordinates).** | The active `DominanceSet` **SHALL** name the selected characteristics and their ordinal floors. | Makes the quality space inspectable. |
| **CC-E21-6 (Measurement legality).** | Any comparison, coordinate, threshold, or telemetry reading **SHALL** follow `C.16`, `A.17`, `A.18`, and applicable `A.19`/`C.25` discipline. | Blocks illegal scalarization and ordinal arithmetic. |
| **CC-E21-6a (Coordinate/state separation).** | A pattern-quality read **SHALL NOT** assign coordinate values from review completion, landing state, monolith placement, release state, steward acceptance, or other administrative state. | Prevents administrative proxies from replacing content measurement. |
| **CC-E21-6b (No reputation or adoption medals).** | A pattern-quality read **SHALL NOT** raise or lower coordinate values from popularity, adoption, awards, steward praise, reviewer praise, prior use, absence of use, completed external review, number of reviews, landing, monolith placement, release inclusion, or absence of those signals. A signal may affect a coordinate only after it is rewritten into replayable pattern-content evidence for the exact pattern version, reader/use/scope/window, and coordinate. | Prevents reputation and usage proxies from replacing pattern-property readings. |
| **CC-E21-7 (Neighbour authority).** | A pattern-quality read **SHALL** cite exact neighbouring FPF patterns for evidence, assurance, measurement, naming, work, gate, decision, publication, causal, bridge, release, and refresh claims when those claims are live. | Prevents shadow authority. |
| **CC-E21-8 (SoTA content-bearingness).** | SoTA grounding **SHALL** follow the E.8 definition of SoTA as current best-known problem-solving practice for the governed problem, state what the pattern adopts, adapts, or rejects, and state which `Solution`, checklist, relation, boundary, or worked case changes because of that stance. Official status, source recency, broad popularity, citation volume, institutional adoption, or familiar terminology do not raise `SoTABindingAndCurrentness` by themselves. | Blocks decorative citation and prestige-source substitution. |
| **CC-E21-9 (Action guidance survives).** | If semantic or lexical repair improves type precision, the read **SHALL** check that a remaining admissible reader move still exists or that a named neighbouring pattern now carries the live claim. | Prevents type-correct but inert patterns. |
| **CC-E21-10 (Bounded non-use).** | Remaining weaknesses **SHALL** narrow use or name a receiving pattern; they **MUST NOT** be hidden behind "later", "deferred", or vague future research language inside the pattern-quality claim. | Makes stopping honest. |
| **CC-E21-11 (Front discipline).** | When several variants are live, the selected version **SHOULD** be on the `PatternQualityFront`; choosing a dominated variant requires an explicit reason such as legacy, regulation, or reader-continuity cost. | Preserves open-ended search without endless perfectionism. |
| **CC-E21-12 (Apparatus fit).** | A pattern-quality read **SHALL** add front/archive/telemetry/support fields only when the live claim requires them. | Prevents bureaucracy from masquerading as quality. |
| **CC-E21-13 (Telemetry boundaries).** | Telemetry signals **SHALL** reopen or calibrate the quality read only for the claim they can support; retrieval or review telemetry is not project certification. | Keeps evidence use scoped. |
| **CC-E21-14 (Accepted-basis carry-through).** | Accepted basis obligations governing the pattern **SHALL** be expressed, intentionally absent, inherited, or assigned by value to a named receiving pattern or support document before claiming `admissibleForDeclaredUse`. | Prevents source loss across drafting. |
| **CC-E21-15 (Stop condition explicit).** | A stop decision **SHALL** cite the active `StopCondition` and state whether it is satisfied for the declared scope. | Replaces "looks good enough" with an inspectable end condition. |
| **CC-E21-16 (Cost coordinates not hidden).** | Reader, author, reviewer, maintainer, migration, evidence, neighbour-integration, entry/projection, retrieval, durable-name, relation, and corpus-ecology cost **SHALL** be active coordinates when they can change admissible use; they **SHALL NOT** be hidden as tie-breakers while live. | Prevents affordability, maintainability, entry, and corpus-ecology loss from being optimized away. |
| **CC-E21-17 (Proxy-for-value check).** | Before a stop decision, the read **SHALL** ask what became worse after coordinate improvement; if rubric satisfaction displaces practical pattern-use value, the `DominanceSet`, status, or scope **MUST** be revised. | Blocks Goodhart substitution. |
| **CC-E21-18 (First-pass affordability).** | A first-pass pattern-quality read **SHALL NOT** require `PatternQualityFront`, `PatternImprovementArchive`, `TelemetrySet`, full `CoordinateEvidenceRef` cards, or a complete coordinate-menu read unless the declared `ClaimScope` makes them live. | Keeps ordinary pattern evaluation usable and prevents review apparatus from becoming the first action. |
| **CC-E21-18a (Repeated improvement locus).** | When a pattern-quality read becomes part of repeated improvement, the repeated method **SHALL** be governed by `E.23`; `E.21` continues to supply coordinates, values, protected trade-offs, status, and stop meanings. | Prevents `E.21` from becoming the full improvement-loop method while keeping exceptional pattern improvement available. |

| **CC-E21-19 (First action before control).** | A pattern-quality read **SHALL** recover the pattern version's first admissible action-guiding move from `Problem frame` and `Solution` before adding checklist, telemetry, archive, or high-assurance support. If the first move is absent or only appears in the checklist, the read may close as `repairBeforeUse` or `admissibleWithNarrowerUse`. | Prevents conformance checks and control apparatus from replacing pattern guidance. |
| **CC-E21-20 (SoTA mutation test).** | Every live SoTA row **SHALL** state which `E.21` field, eligibility condition, coordinate, worked slice, relation, conformance item, non-use boundary, or stop/reopen condition changes because of the adopted/adapted/rejected stance. A source that changes no content-bearing text is rationale support, not SoTA binding. | Prevents decorative SoTA and keeps `SoTABindingAndCurrentness` content-bearing. |
| **CC-E21-21 (SoTA currentness and lineage split).** | A foundational, official, popular, or lineage source **MAY** remain in `E.21:11`, but a current-practice claim **SHALL** either cite a current SoTA anchor under E.8 or explicitly mark the older or official source as lineage-only, current-standard reference, rationale-only, or rejected-popular-practice material. | Prevents old standards, fresh standards, classic papers, and popular practice from masquerading as present SoTA. |
| **CC-E21-22 (Evaluation non-certification).** | A pattern-quality evaluation **SHALL NOT** be used as safety, security, compliance, release, project assurance, or gate certification. When such a claim is live, the read **SHALL** open the exact receiving FPF pattern and state the supported and unsupported use. | Blocks audit-theatre and compliance-by-checklist overread. |
| **CC-E21-23 (Activated retrieval evidence only).** | Retrieval, RAG, search, or misentry telemetry **SHALL** be used only when retrieval-facing pattern entry or observed misretrieval is live; it **SHALL NOT** become a universal benchmark requirement for ordinary pattern drafts. | Keeps modern retrieval evaluation useful without adding review bureaucracy. |
| **CC-E21-24 (First-pass content slice).** | A conforming first-pass pattern-quality read **SHALL** be able to close on the smallest slice that identifies pattern version, reader/use/window, first admissible move evidence, activated blockers, minimal dominance coordinates, status, and next admissible repair or bounded non-use. | Keeps `E.21` usable as content guidance rather than review bureaucracy. |
| **CC-E21-25 (Status payload).** | Every `PatternQualityStatus` **SHALL** state the exact use, scope, reader boundary, blocker, reopen trigger, or architecture-decision question that makes the status true. | Prevents status labels from becoming vague maturity tags. |
| **CC-E21-26 (Ordinal-reading boundary).** | A coordinate value **SHALL** be treated as an ordinal content reading unless a `C.16` measurement basis is explicitly declared. | Prevents accidental pseudo-measurement. |
| **CC-E21-27 (Claim-triggered activation).** | Coordinates and eligibility rows **SHALL** be activated by the live claim force of the pattern version or quality claim; inactive rows **SHALL NOT** be treated as hidden failures or waived passes. | Keeps the complete characteristic space from becoming a universal audit grid. |
| **CC-E21-28 (Kind settlement).** | Every durable or FPF-force-bearing `E.21` head **SHALL** be classified as an existing FPF kind specialisation, local field, value set, local evidence-reference record, or scoped support construct. A head with no recovered kind **SHALL NOT** be used in a stop decision. | Prevents `E.21` from minting a parallel quality ontology. |
| **CC-E21-29 (No gate/status overread).** | `PatternQualityStatus`, `EligibilitySet`, coordinate floors, and `StopCondition` **SHALL NOT** be described as gate passage, release status, role state, assurance level, work authority, or project approval. | Keeps `E.21`, `E.19`, `A.21`, `B.3`, and release/work patterns distinct. |
| **CC-E21-30 (Local name-card sufficiency).** | `E.21:4.11` local name-precision cards are sufficient for ordinary `E.21` use. A full `F.18` Name Card is required only when a head is reused outside `E.21`, collides with an existing head, enters durable cross-pattern vocabulary, or changes naming authority. | Preserves naming discipline without turning ordinary pattern-quality reading into naming bureaucracy. |
| **CC-E21-31 (Coordinate-head scope).** | Coordinate heads in `PatternQualityEvaluationCharacteristicSpace` **SHALL** remain local ordinal characteristic heads for pattern-quality reads unless a neighbouring `C.16`/`A.17`/`A.18`/`A.19` declaration promotes a specific coordinate into a measurement or broader characteristic claim. | Prevents accidental metrics, maturity dimensions, and pseudo-measurement. |
| **CC-E21-32 (Neighbour-governed claim boundary).** | A conforming `E.21` read **SHALL** state or preserve the governing-pattern boundary between `E.21` and live neighbouring patterns when authoring, review, measurement, naming, evidence, assurance, gate, release, work, or project-side claims are involved. | Prevents `E.21` from becoming a central quality-governance subsystem. |
| **CC-E21-33 (Layer activation).** | A conforming `E.21` read **SHALL** use the lowest activation layer sufficient for the declared claim. Front, archive, telemetry, and full support-card apparatus **SHALL NOT** be required for a first-pass read unless the claim makes them live. | Preserves affordability and prevents bureaucracy. |
| **CC-E21-34 (Replayable quality read).** | A `PatternQualityQBundle` **SHALL** be replayable from its pinned pattern version, reader/use/scope/window, active eligibility rows, active coordinates, evidence refs, status payload, and stop/non-stop reason, without relying on chat memory or administrative placement state. | Preserves auditability without requiring a process log. |
| **CC-E21-35 (No neighbour substitution).** | `E.21` **SHALL NOT** absorb the governed object of `E.8`, `E.19`, `C.25`, `C.16`/`A.17`/`A.18`/`A.19`, `F.18`/`E.10`/`A.6.P`, or project-side evidence, assurance, gate, work, and release patterns. When such a claim is live, `E.21` **SHALL** name the exact receiving pattern application by value. | Preserves modularity and composability. |
| **CC-E21-36 (Smallest live reopen).** | A refresh or telemetry signal **SHALL** reopen the smallest affected locus: source stance, neighbour relation, coordinate reading, worked case, name, eligibility row, status payload, or stop condition. The whole quality read reopens only when that local change can change status or stop. | Preserves evolvability without whole-pattern churn. |
| **CC-E21-37 (Status is not authority).** | `PatternQualityStatus` **SHALL** remain an admissible-use posture for the pattern-quality claim and **SHALL NOT** be used as project approval/refusal, gate decision, release state, assurance level, compliance verdict, safety certificate, or work authority. | Preserves scope safety and trust calibration. |
| **CC-E21-38 (No quality veto without content locus).** | A blocking pattern-quality finding **SHALL** name the exact activated eligibility row, coordinate, status payload, or stop-condition clause, plus content evidence and the first admissible repair or bounded non-use. | Prevents pattern-quality review from becoming reviewer authority theatre. |
| **CC-E21-39 (Self-application closure).** | `E.21` self-application **SHALL** use the lowest sufficient activation layer and **SHALL NOT** require recursive quality bundles evaluating quality bundles. | Prevents infinite regress and keeps `E.21` usable. |
| **CC-E21-40 (Thin echo boundary).** | ToC rows, `J.4` rows, README notes, dashboards, generated summaries, and retrieval snippets **SHALL NOT** replace the governed `PatternQualityQBundle`; they may only echo it by value and scope. | Prevents projection authority and RAG/snippet overread. |
| **CC-E21-41 (No forced winner).** | When multiple candidates are non-dominated and no receiving action requires one selected candidate, a conforming read **SHALL NOT** force a single winner. | Preserves NQD/front discipline and blocks hidden scalarization. |
| **CC-E21-42 (Bounded non-use as valid outcome).** | `admissibleWithNarrowerUse` **SHALL** be used when a pattern is not ordinary-use admissible but remains useful for a named narrower reader/use/scope. | Prevents unnecessary rewrite churn and preserves useful legacy/support material. |
| **CC-E21-43 (High-value falsifiability hook).** | Coordinate values `4` or `5`, and any coordinate supporting `admissibleForDeclaredUse` or `StopCondition`, **SHALL** state a lowering condition or content discovery that would reopen or lower the read. | Makes high quality claims falsifiable without adding a full harness. |
| **CC-E21-44 (Support retention test).** | Support material **SHALL** remain active only when the read states what quality breakage would return if that material were absent. | Prevents support material from becoming folklore, hidden authority, or permanent reader cost. |
| **CC-E21-45 (Pattern text vs pattern application).** | `E.21` **SHALL NOT** be used to certify that a project correctly applied a pattern. It reads the quality of the pattern version; project/application claims remain under exact receiving patterns. | Preserves FPF-side and project-side boundaries. |
| **CC-E21-46 (High-assurance separation).** | High-assurance support **SHALL NOT** make the ordinary pattern body harder to use unless the ordinary use itself changes. | Keeps ordinary action guidance alive while allowing additional support material where live. |
| **CC-E21-47 (Activation-normalized coordinates).** | `PatternQualityEvaluationCharacteristicSpace` **SHALL NOT** be used as one flat always-on audit grid. Each coordinate **SHALL** state its activation class, and inactive coordinates **SHALL NOT** count as pass, waiver, or hidden failure. | Prevents characteristic bloat and hidden checklist control. |
| **CC-E21-48 (Hard blockers stay out of dominance).** | `firstMoveRecoverability`, hard measurement illegality, shadow neighbour authority, administrative proxy use, and live mission/pillar conflict **SHALL** be treated as eligibility blockers when activated, not weak coordinate values. | Prevents hard failures from being averaged or front-compared away. |
| **CC-E21-49 (No evidence-as-coordinate substitution).** | `CoordinateEvidenceRefs`, evidence kinds, support cards, review findings, and telemetry signals **SHALL** justify, reopen, or calibrate coordinate readings; they **SHALL NOT** become coordinates by themselves. | Keeps the quality space about pattern properties, not support artefact volume. |
| **CC-E21-50 (No hidden double weighting).** | When two quality concerns are directly coupled, the pattern **SHALL** either merge them into one coordinate with explicit subreadings or explain why the two coordinates can fail independently and require different repairs. | Prevents the number of coordinate rows from acting like a hidden weighting scheme. |
| **CC-E21-51 (Formal-claim activation).** | Measurement, score, comparison, threshold, aggregation, mathematical-lens, causal-lens, QL-lens, simulation, representation, or learned-lens checks **SHALL** activate `FormalClaimLegalityAndLensFit`; absence of such a claim **SHALL NOT** create an ordinary coordinate obligation. | Prevents ordinary pattern reads from becoming formal-method bureaucracy. |
| **CC-E21-52 (Projection and corpus activation).** | External entry, publication projection, retrieval, RAG, dashboard, durable-name, relation, or corpus-ecology coordinates **SHALL** activate only when the pattern version or candidate edit changes those surfaces or is known to be misentered or overread through them. | Keeps corpus safety without universal projection bureaucracy. |
| **CC-E21-53 (High-value lowering condition).** | Coordinate values `4` or `5`, `admissibleForDeclaredUse`, and stop claims **SHALL** state a concrete lowering or reopen condition unless the declared use is only first-pass repair triage. | Makes high-value pattern-quality claims falsifiable without requiring a test harness. |

### E.21:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
|---|---|---|---|
| **Quality score illusion** | `Pattern quality = 87/100`. | Hides ordinal scale differences, hard blockers, and trade-offs. | Publish a `PatternQualityQBundle` with eligibility, coordinates, status, and stop condition. |
| **Administrative proxy quality** | `FormalClaimLegalityAndLensFit = 3 because not yet externally reviewed` or `CaseCountercaseAndTransferCoverage = 4 because already landed`. | Measures process state instead of the pattern property being claimed. | Score the coordinate from the pattern text and content evidence; put review, landing, release, or monolith state in `ClaimScope`, `QualificationWindow`, or the receiving review/release pattern. |
| **Reputation medal quality** | `ActionPathGuidance = 5 because many people use it`, `SoTABindingAndCurrentness = 4 because reviewers liked it`, or `UseAffordabilityAndApparatusProportionality = 3 because nobody has tried it yet`. | Measures social uptake or absence of uptake instead of the pattern property being evaluated. | Convert any observation into exact pattern-content evidence or ignore it for the coordinate value: name the pattern version, reader/use/scope/window, observed property, coordinate affected, and lowering or raising condition. |
| **Template-complete but inert** | All sections exist, but the reader cannot tell what to do first. | E.8 form is being mistaken for action guidance. | Repair `firstMoveRecoverability`, `WorkingSituationAndUseBoundaryRecognizability`, and `ActionPathGuidance`; repair Problem frame and Solution. |
| **Checklist-as-solution** | The conformance checklist carries the main method. | The checklist tests guidance; it does not replace guidance. | Move action guidance into `Solution`; make CC items test it. |
| **Decorative SoTA shelf** | Sources are listed but the pattern would read the same without them. | SoTA has no content-bearing effect. | State adopt/adapt/reject and change a live boundary, example, relation, or checklist. |
| **Lexical polishing without kind recovery** | Terms sound cleaner but kind, relation, or support claim force remains ambiguous. | The repair is lexical, not ontological. | Repair `SemanticKindAndNameRecoverability`; run `F.18 -> A.6.P -> E.10` when durable or cross-pattern names are live. |
| **Apparatus maximalism** | Every draft gets telemetry, archive, review cards, and extra companion files. | Reader and maintainer cost rises without added admissible use. | Use the one-screen card unless consequence or reuse makes heavier evidence or companion apparatus live. |
| **All-high-values Goodharting** | Every visible coordinate is marked `4` or `5`, but the pattern is harder to read, costlier to maintain, or less useful in the declared ordinary case. | The coordinate set became a proxy for value and stopped measuring full pattern-use value. | Activate `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `ProxyForValueSubstitutionResistance`; narrow to high-assurance use if the extra apparatus is only justified there. |
| **Cost-hidden tie-breaker** | Reader, author, maintainer, entry/projection, retrieval, relation, or corpus-ecology cost is treated only as a tie-breaker while it changes admissible use. | A live quality loss is being kept outside the dominance relation. | Promote the cost question into `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, `ProxyForValueSubstitutionResistance`, or another active coordinate. |
| **One-domain breadth claim** | The pattern claims transdisciplinary reach with only IT or ML examples. | Example breadth does not support claim breadth. | Repair `CaseCountercaseAndTransferCoverage` or narrow the claim. |
| **Endless perfection loop** | Authors keep improving because a better wording is always imaginable. | Open-ended evolution lacks a local stop condition. | Stop when eligibility passes, the candidate is non-dominated for scope, floors are met, and remaining issues are bounded non-use or a named receiving pattern; use `EvolutionFrontAndRefreshDiscipline` plus `ClosureAndBoundedNonUseRecoverability` to keep the stop local. |
| **Quality veto theatre** | A reviewer blocks use with phrases such as "not ready", "low quality", "not FPF enough", or "needs more review", but does not name an activated eligibility row, coordinate, content evidence, status payload, and first admissible repair or bounded non-use. | The quality read is being used as authority pressure rather than content guidance. | Rewrite the veto as a pattern-quality finding using `E.21:4.10a`, or remove it from the quality read. |
| **Reviewer preference laundering** | A stylistic, political, role-control, or process preference is encoded as low `ActionPathGuidance`, `SoTABindingAndCurrentness`, `SemanticKindAndNameRecoverability`, or another coordinate without content evidence. | A preference is being laundered into a pattern-quality defect. | Move the preference to the correct neighbouring decision/process locus, or state the actual content defect. |
| **Projection-quality shadow track** | A ToC row, J.4 cue, dashboard tile, status badge, generated summary, or retrieval snippet restates the quality result without scope, status payload, non-use boundary, or source read ref. | A projection is becoming a second semantic track or authority face. | Activate `ExternalEntryAndProjectionIntegrity`; make the projection a thin echo by value and scope, or name the exact publication/projection pattern application. |
| **Corpus-local win, pattern-language loss** | A local pattern edit improves wording or evidence but increases relation fanout, name collision, entry noise, stale echoes, or neighbouring authority confusion. | Local quality improved while FPF corpus ecology degraded. | Activate `PatternLanguageEcologyFit`; narrow the edit, name the exact receiving pattern for the claim, or repair the entry/name/relation locus. |
| **Quality result as project certificate** | A clean pattern-quality read is cited as product safety, compliance, release, or assurance evidence. | Pattern quality is not project-world truth. | Open `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, or another exact receiving pattern for the project-side claim. |
| **Evidence theatre** | The pattern adds evidence refs, review findings, telemetry, or support cards, but none of them changes a coordinate value, boundary, worked case, or stop condition. | Support material is being used as authority decoration. | Remove it or state the exact coordinate/status/stop effect it supports. |
| **Legacy flattening** | An older pattern that remains useful as source-basis, historical rationale, or expert-only support is forced into ordinary-use repair instead of narrowing its use honestly. | The quality read treats "not ordinary-use admissible" as "worthless". | Use `admissibleWithNarrowerUse`, state the support-only or historical use, and assign broader use to repair or replacement under the exact receiving pattern. |
| **Narrow-use hiding** | A pattern cannot serve ordinary use, but the quality read still claims broad `admissibleForDeclaredUse`. | A real scope narrowing is hidden to preserve an unwarranted status label. | Change status to `admissibleWithNarrowerUse` and state the narrowed reader, use, or scope. |

### E.21:9 - Consequences

| Benefits | Trade-offs / mitigations |
|---|---|
| Pattern quality becomes inspectable without fake precision. | Authors must name scope and active coordinates; the one-screen card keeps ordinary cost low. |
| Review findings can distinguish hard blockers from optimization trade-offs. | Some drafts will receive `holdForArchitectureDecision`; this is useful when prose repair would hide architecture debt. |
| Stop decisions become less taste-based and less perfectionist. | Pareto/front reasoning is heavier than a score; use it only when several candidates or trade-offs are live. |
| SoTA, examples, and neighbour relations become quality-bearing loci. | Reviewers must read beyond headings; `E.19` already selects depth where risk is live. |
| Pattern improvement aligns with NQD/OEE without forcing one winner prematurely. | The selected front/archive should remain small and scoped to the pattern-quality question. |
| Activation-normalized coordinates make it harder to raise visible values by adding bureaucracy. | Authors must keep blockers, overlays, evidence/support mechanisms, and coordinates separate; the benefit is that a higher coordinate value cannot silently mean a harder first-use path, stale projection, or corpus-local win with pattern-language loss. |
| Merged coordinates reduce hidden double weighting. | A weak live subreading limits the coordinate value; do not average subreadings to hide a missing first-use, support, affordability, formal-legality, or corpus-ecology concern. |

### E.21:10 - Rationale

FPF patterns are not essays, APIs, step lists, or generic best-practice notes. They are action-guiding method descriptions for recurring working situations. Their quality therefore cannot be read from style, section count, one score, or one flat audit grid.

`C.25` already shows why composite quality claims need bundles. `C.16`, `A.17`, and `A.18` show why measured values require declared characteristics and scales. `A.19` shows why multi-coordinate reasoning needs a declared characteristic space. `F.18` and NQD/front discipline show why several viable candidates can remain non-dominated. `E.12` and `E.13` show why usability, cognitive ergonomics, practical utility, and proxy-for-value substitution must remain quality-bearing rather than administrative afterthoughts. `E.19` shows why review should use triggered profiles rather than one giant checklist.

The characteristic space is activation-normalized because FPF pattern quality is read from the live claim made by the pattern version. A first-pass ordinary-use read needs entry, first move, action path, bounded non-use, and a small evidence slice for the active quality claim; a formal-claim read also needs legality of measurement, comparison, mathematical lens, causal lens, quantum-like lens, simulation, representation, or learned model; a publication or retrieval-facing read also needs entry/projection integrity and corpus-ecology fit. Treating every coordinate as always active would turn `E.21` into hidden checklist control.

The coordinate set also avoids hidden double weighting. Concerns that usually fail and repair together are merged with explicit subreadings; a weak live subreading limits the coordinate value instead of being averaged away. Concerns that fail independently remain separate because their repair moves differ: action path is not closure, semantic/name recovery is not neighbour authority, claim support is not project assurance, and local pattern quality is not corpus ecology.

`E.21` applies existing FPF architecture to pattern quality. It gives authors a way to say: this version is admissible for this use, under these active coordinates, with these hard blockers cleared, and these remaining weaknesses bounded. That is more reviewable than "good enough" and lighter than pretending every pattern needs a universal maturity score.

### E.21:11 - SoTA-Echoing

`E.21:11` is a SoTA-binding table, not a bibliography. A row is live only when it changes at least one `E.21` field, eligibility condition, coordinate, worked slice, relation, conformance item, non-use boundary, or stop/reopen condition, and it uses `SoTA` in the E.8 sense: current best-known problem-solving practice for the governed problem.

If a `SoTA Synthesis Pack@CG-Frame` exists for pattern-quality evaluation, this section cites its claim IDs and does not fork an untracked SoTA narrative. If no pack exists, this section is a provisional seed and must still state `adopt | adapt | reject`, the concrete `E.21` effect, and the boundary of non-overread.

A source that only supplies lineage, popularity, or familiar terminology is not a SoTA row. It may remain as rationale material, but it does not satisfy `SoTABindingMinimum`.

| Claim | Source stance | Adopted/adapted content | Concrete E.21 effect | Boundary of non-overread |
|---|---|---|---|---|
| Pattern-quality evidence must show applicability and generality without making ordinary reading heavy. | Current pattern-validation anchors for this narrow problem: Riehle et al. (2021) for explicit pattern validation methods and Zarras (2023) for applicability/generality evidence; Iba (2021) is lineage/writing-style support only. | Pattern claims need explicit discovery or validation support rather than informal consensus, and examples must show how use is done in practice without turning every description into a tiring dossier. | `CaseCountercaseAndTransferCoverage`, `CoordinateEvidenceRefs`, and the first-pass slice require at least one usable application slice and, where broad scope is claimed, heterogeneous or known-use support. | This does not require controlled studies, long empirical packages, or known-use sections for every small FPF edit; ordinary first-pass remains lightweight. |
| Living pattern-quality reads need currentness windows and section-level reopen triggers, not whole-pattern churn. | Living-guideline currentness is adopted by analogy from Akl et al. (2017); PRISMA 2020, Page et al. (2021), is current-standard/reference-only for transparent reporting of review/update basis, not pattern-quality SoTA by itself. | The currentness unit is the live claim, coordinate, source stance, relation, or worked case, not automatically the whole pattern. | `QualificationWindow`, `refreshNeeded`, `SoTAStalenessSignals`, `CoordinateEvidenceRefs`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, and `EvolutionFrontAndRefreshDiscipline` state what makes the read current and what can reopen it. | This does not import systematic-review or clinical-guideline workflow as mandatory apparatus for ordinary FPF pattern drafts. |
| Multi-characteristic improvement should preserve non-dominated alternatives and useful diversity instead of forcing one winner. | Current QD overview: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 100:102240 (2026), for QD currentness; retained lineage: MAP-Elites and the 2016 QD survey; CMA-ME/CMA-MAE, differentiable QD, and QDax-class accelerated QD practice are adopted only for the set-valued/front/archive idea. | Quality-diversity practice keeps diverse high-performing alternatives rather than collapsing to one scalar winner. | `PatternQualityFront`, `PatternImprovementArchive`, and `TieBreakerSet` keep viable candidate edits visible under a declared scope, while ordinary use remains first-pass and non-algorithmic. | No QD algorithm, grid, emitter policy, hardware stack, or library workflow becomes mandatory for pattern review. |
| Coordinate improvement can destroy the value the coordinates were meant to protect. | Current proxy-risk anchors include `Goodhart's Law in Reinforcement Learning` (ICLR 2024) and current catastrophic-Goodhart reward-misspecification work (NeurIPS 2024); retained lineage: Manheim and Garrabrant (2018) for the Goodhart taxonomy. | Overoptimization by a metric or proxy can become ineffective or harmful, and mixed Goodhart mechanisms need exact naming rather than broad "metric failure" prose. | `ProxyForValueSubstitutionResistance` becomes an active coordinate when proxy-risk claim force is live; before stop, the read asks what got worse in first-use cost, repair-impact predictability, neighbour ripple, bounded non-use, practical payoff, entry/projection integrity, or corpus ecology. | This does not make `E.21` an adoption forecast, economics model, or project-value estimator. |
| Pattern-quality evaluation must not become safety, security, compliance, or release certification. | Current-standard/reference-only governance-boundary material: UK AI Safety Institute, `AI Safety Institute approach to evaluations` (GOV.UK, current institutional guidance page), and `What AI evaluations for preventing catastrophic risks can and cannot do` (`arXiv:2412.08653`). These are adopted only for the non-overread boundary, not as FPF pattern-quality value sources. | Evaluations are useful, but evaluation alone is not sufficient for effective governance, real-world safety, or absence-of-risk claims. | `NeighborAuthorityAndBoundedUseFit`, `ClaimSupportTraceabilityCurrentnessAndReplayability`, `supportBoundaryEvidence`, and `PatternQualityStatus` keep project-side evidence, assurance, gate, release, work, safety, security, and compliance claims under exact receiving patterns. | This rejects compliance-by-checklist, audit theatre, and "review passed therefore safe/compliant" readings. It does not import AI-safety governance machinery into ordinary pattern-quality reading. |
| Pattern-quality stop decisions must keep perspective, resource cost, feasibility, acceptability, and equity or differential impact visible when they change admissible use. | Current-standard/reference-only decision-support material: GRADE Evidence-to-Decision practice is adapted for explicit decision perspective and resource/feasibility/acceptability/equity-impact criteria. | Resource use, cost, feasibility, acceptability, equity, and differential impact can legitimately change a recommendation or admissible use. | `WorkingReaderScope`, `UseAffordabilityAndApparatusProportionality`, `RepairLocalityAndChangeImpactPredictability`, and `StopCondition` treat cost and differential reader/practice impact as quality evidence when they change ordinary use. | This does not import clinical guideline panels, medical evidence grading, population-health policy machinery, or project-side impact assessment into FPF pattern review. |
| Retrieval-facing pattern quality needs component-level evidence, not one search-success score. | Retrieval-evaluation reference anchors for the narrow retrieval-facing entry problem: RAGAS, `Automated Evaluation of Retrieval Augmented Generation` (EACL 2024), and ARES, `An Automated Evaluation Framework for Retrieval-Augmented Generation Systems` (NAACL 2024), adopted only for the multi-dimensional retrieval-facing evaluation stance: context relevance, faithfulness to cited context, answer relevance, and component evidence. | Retrieval/RAG evidence distinguishes whether the right context is found, whether the answer is faithful to cited context, and whether the answer is relevant. | `retrievalHitQuality`, `coldReaderMisentryRate`, `ExternalEntryAndProjectionIntegrity`, `PatternLanguageEcologyFit`, and `CoordinateEvidenceRefs` may use tiny retrieval fixtures only when retrieval-facing entry, projection, or observed misretrieval is live. | This does not require universal RAG benchmarks or LLM evaluation harnesses for ordinary pattern drafts. |
| Measurement and bundle discipline should be internal to FPF rather than imported as a rival framework. | Inherited-current FPF neighbours: current FPF `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `E.8`, `E.19`, and `F.18`. | Existing FPF already has Characteristic/Scale, Q-Bundle, review, and naming machinery. | `E.21` composes those patterns and adds the missing pattern-quality receiving locus. | `E.21` does not replace the neighbouring patterns it cites. |
### E.21:12 - Relations

| Neighbour | Neighbour governs | `E.21` may use | `E.21` shall not do |
|---|---|---|---|
| `E.8` | Pattern authoring body and action-guiding structure. | Read whether the body supports declared pattern-quality use. | Add mandatory authoring sections or move Solution guidance into the quality bundle. |
| `E.19` | Review profiles, findings, admission/refresh outcome. | Use findings as content evidence when they identify pattern-content defects or strengths. | Treat review pass, return, or absence as a coordinate value or project certificate. |
| `E.22` | Quality-read question framing before a quality read, review, improvement request, open-question discovery, or absorption pass. | Use `QualityReadQuestionFrame` to distinguish `floorRead`, `exceptionalImprovementRead`, `paretoTradeoffRead`, `openQuestionDiscoveryRead`, and `absorptionRead` before an `E.21` result shape is chosen. | Treat the question frame as coordinate evidence, pattern-quality status, review result, or project-side approval. |
| `E.23` | Repeated quality-improvement method. | Improve one pattern version through repeated `E.22`-framed reads and `E.21` re-reads when exceptional improvement, absorption impact, or trade-off inspection remains live. | Define pattern-quality coordinates, replace `PatternQualityQBundle`, or treat loop continuation, discharge, landing, or praise as a coordinate value. |

| `E.9.DA` | DRR decision-adequacy reads before downstream authoring use. | Open only when a pattern-quality defect traces to an upstream `DRR` whose selected answer, receiving-locus disposition, source-use carry-through, accepted-decision carry-through, or architecture selection is missing, vague, unassigned, source-theatre-like, or architecture-by-addressing. | Treat upstream `DRR` adequacy as a pattern-quality coordinate, require `E.9.DA` before ordinary `E.21` first-pass reads, or reuse pattern-quality coordinates to judge the `DRR` as if it were an authored pattern body. |
| `C.25` | General Q-Bundle normal form. | Specialise Q-Bundle for FPF pattern quality. | Replace arbitrary engineering quality-family bundling. |
| `A.17`, `A.18`, `A.19`, `C.16` | Characteristic, scale, coordinate, measurement legality. | Use ordinal content readings and cite measurement law when live. | Convert ordinal readings into numeric measures, scores, percentages, or averages. |
| `F.18`, `E.10`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q` | Naming, wording-use, relation, epistemic, characteristic/scale, and quality-term precision restoration. | Require recoverable kind, relation, characteristic/scale construction, quality-term endpoint, and admissible use for FPF-force-bearing heads. | Mint durable cross-pattern names by convenience, or let pattern-quality wording carry hidden score, scale, quality, evidence, gate, or release force. |
| `A.10`, `B.3`, `A.20`, `A.21`, `A.15` | Project evidence, assurance, local CV status, gates, work. | Keep project-side reuse under exact receiving patterns. | Certify project safety, compliance, gate passage, release, work authority, or publication truth. |

**Coordinates with `E.11` and `J.4`.**
`E.21` is the governing pattern when the live question is: "Is this FPF pattern version good enough for this declared reader/use/scope, and may improvement stop?"

`E.21` is not the first entry when the live question is only:

* how to write the pattern body (`E.8`);
* which admission/refresh review profile to run (`E.19`);
* how to frame the quality-read purpose before the pattern-quality read (`E.22`);
* how to repair entry discoverability or wrong-pattern selection (`E.11`);
* how to recover overloaded quality or characteristic/scale wording before a pattern-quality claim (`C.16.Q`, `C.16.P`, or `C.25`).

If `E.21` changes `Preface`, `J.4`, ToC query rows, local Problem-frame recognition cues, or retrieval-facing entry support, the entry-facing effect remains governed by `E.11`; `E.21` only supplies the pattern-quality claim.

**Builds on:**

* `E.1` and `E.2` for mission and pillar fit.
* `E.8` for pattern authoring structure, recognition text, action guidance, and SoTA-Echoing obligations.
* `E.19` for review and refresh profiles.
* `C.25` for Q-Bundle normal form.
* `C.16`, `A.17`, `A.18`, and `A.19` for characteristic, scale, coordinate, measurement, and characteristic-space discipline.
* `F.18`, `E.10`, `A.6.P`, `C.2.P`, `C.16.P`, and `C.16.Q` for naming, wording-use, relation, epistemic, characteristic/scale, and quality-term precision.

**Coordinates with:**

* `C.2.P` when epistemic precision repair touches FPF-force-bearing Problem frames, recognition text, examples, or worked slices; an `E.21` quality read treats epistemic precision repair as incomplete when no remaining admissible reader move or exact neighbouring-pattern application survives.
* `E.12`, `E.13`, and `E.14` for cognitive ergonomics, pragmatic utility, Goodhart/proxy checks, and human-centric working-model checks.
* `C.18`, `C.19`, and related NQD/OEE patterns when candidate fronts or search/archive constructs are live.
* `G.11` when telemetry-driven refresh or decay is live.
* `A.10`, `B.3`, `A.20`, `A.21`, and `A.15` when a pattern-quality result is reused as evidence, assurance, local CV status, gate-decision material, or work authority.

**Constrains:**

* Any FPF pattern-quality read that would otherwise use a single score, unscoped maturity label, or reviewer-taste verdict.
* Any pattern drafting or review stop decision that claims the current version is good enough for a declared use.

### E.21:End

