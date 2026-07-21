## C.32.ADA - Architecture Decision Adequacy Scales

> **Type:** Architecture evaluation pattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.ADA:1 - Problem frame

Use this pattern when a project architecture decision, its method docking, or its ADR-like publication projection must be evaluated for adequacy before use, review, handoff, governance, or improvement.

Primary working reader: an architect, reviewer, or architecture-responsible practitioner checking whether a project architecture decision is good enough for a declared use and which repair should happen next.

Typical entry phrases:

```text
"The decision is written, but can developers actually use it?"
"The ADR looks complete; is the architecture decision itself adequate?"
"Which part is weak: candidate basis, trade-off, method instruction, work split, or publication projection?"
"We need a scale like E.21, but for architecture decisions rather than pattern quality."
"Do not average the decision; tell us what must be repaired."
```

**First-minute use slice.** A reviewer receives a PAD decision relation and ADR projection for a modularization decision. Using C.32.ADA, the reviewer declares the use: "ready for developer work and ADR publication." The reviewer scores each coordinate with a short rationale. Candidate traceability is `4 wellExpressedForDeclaredUse`, architecture-characteristic trade-off is `3 sufficientlyExpressedForDeclaredUse`, method docking is `2 partiallyExpressedForDeclaredUse`, and publication projection is `4 wellExpressedForDeclaredUse`. The result does not approve the decision. It directs repair to the method-use instruction, responsible roles, readiness exit, and expected structure effect before the decision can guide developer work.

The primary `EntityOfConcern` is `ArchitectureDecisionAdequacyEvaluation@Project`: an evaluation record over one `ArchitectureDecisionRelation@Project`, optional `ArchitectureDecisionRecordProjection@Project`, and declared use.

`ArchitectureDecisionAdequacyEvaluation@Project` is not a new `U.*` kind, not a gate, not evidence, not assurance, not pattern-quality evaluation, and not a replacement for `C.32.PAD`. It is a typed adequacy evaluation that sends weak coordinates back to their governing repair patterns.

What goes wrong if C.32.ADA is missed: a decision can appear complete because it has a record, rationale, or diagram, while it is unusable for the declared work. Weak candidate basis, hidden trade-offs, missing method instructions, absent source-return, and vague supersession conditions remain invisible until implementation or review fails.

What C.32.ADA buys in practice: the project can evaluate architecture decisions by complete coordinate set, keep kinds distinct, and repair the weakest live coordinates without turning adequacy into a single score.

Ordinary working move: declare the evaluation use, evaluate every coordinate with an ordinal value and rationale, then return each weak coordinate to the smallest governing pattern that can repair it.

Adoption test: after using C.32.ADA, another practitioner can see the declared use, complete coordinate values, rationales, repair targets, and stop condition for the architecture decision.

Not this pattern when the current object is FPF pattern quality, measurement validity, evidence support, assurance, gate passage, candidate synthesis, comparison, selection, local choice, or ADR publication projection itself. Use the receiving pattern named in `Relations`.

The first useful output is `ArchitectureDecisionAdequacyEvaluation@Project`:

```text
ArchitectureDecisionAdequacyEvaluation@Project:
  evaluationId:
  declaredUse:
  architectureDecisionRelationRef:
  architectureDecisionRecordProjectionRef?
  evaluatorRoleRef:
  coordinateValues:
    - coordinateRef:
      value: 0|1|2|3|4|5
      valueLabel: absent|namedOnly|partiallyExpressedForDeclaredUse|sufficientlyExpressedForDeclaredUse|wellExpressedForDeclaredUse|exceptionallyExpressedForDeclaredUse
      adjacentValueRationale:
      evidenceOrSourceRefs?
      repairPatternRef?
      repairInstruction:
  strongestBlockingCoordinates:
  noAveragePolicy: true
  stopCondition:
  reevaluationTrigger:
```

### C.32.ADA:2 - Problem

Architecture decisions are multi-kind objects in practice. A decision relation can be strong while its ADR projection is weak. A record can be readable while the decision lacks candidate traceability. A candidate basis can be strong while method docking is absent. A method instruction can be clear while the architecture-characteristic trade-off is hidden.

Because of that, a single pass, single grade, or average score is misleading. Adequacy must be evaluated by coordinates tied to the declared use. "Ready for internal architecture review", "ready for developer work", "ready for ADR publication", and "ready for governance enforcement" can require different stop conditions, but each use still needs complete coordinate inspection.

C.32.ADA supplies an E.21-shaped ordinal evaluation pattern for architecture decisions. It uses the E.21 value domain and labels directly, then defines architecture-decision coordinates over PAD relation, method docking, publication projection, structural description, characteristic trade-off, and evolution. Weak coordinates point back to `C.32.PAD`, `C.32.ADR`, `C.30.AD`, `A.15`, `C.32.ACS`, `C.32.ACE`, `C.16`, `C.25`, or another governing pattern.

### C.32.ADA:3 - Forces

| Force | Tension |
|---|---|
| Decision complexity | One architecture decision carries candidate, structure, characteristic, method, work, publication, and evolution content. |
| Declared use | A decision can be adequate for discussion and inadequate for developer work or governance. |
| Repair focus | Review must point to the smallest repair locus, not produce a general complaint. |
| No average | A strong rationale cannot compensate for absent work split or missing source-return. |
| Kind precision | Eval results, evidence, assurance, gates, and publication records must stay distinct from adequacy evaluation. |
| Evolution | The evaluation must expose reopen and supersession weakness before the decision becomes stale. |

### C.32.ADA:4 - Solution

Create `ArchitectureDecisionAdequacyEvaluation@Project` for one declared use. Evaluate the complete coordinate set. Do not average coordinate values. Use the weakest live coordinate to choose the next repair.

#### C.32.ADA:4.1 - Shared value meanings

Use the same ordinal value domain and labels as `E.21`. ADA specializes what counts as expression for architecture-decision adequacy; it does not create a second scale.

| Value | Label | Architecture-decision adequacy meaning |
|---:|---|---|
| `0` | `absent` | The coordinate is not expressed for the declared architecture-decision use. |
| `1` | `namedOnly` | The coordinate is named or implied, but cannot support reliance, action, evaluation, or repair. |
| `2` | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, misplaced, or too narrow for the declared use. |
| `3` | `sufficientlyExpressedForDeclaredUse` | The coordinate can support the declared use in the current project, with limits visible. |
| `4` | `wellExpressedForDeclaredUse` | The coordinate has clear refs, boundaries, source-return, and repair path for likely project changes. |
| `5` | `exceptionallyExpressedForDeclaredUse` | The coordinate is well expressed and transferable across another team, later slice, or adjacent holon kind with minimal recovery work and no hidden neighbor loss. |

Values are ordinal content evaluations. They are not measures, averages, votes, maturity ladder names, evidence weights, assurance levels, gate statuses, or implementation approval.

The result-bearing coordinate row uses the E.21 label domain with an architecture-decision coordinate:

| Coordinate | Value | Label | ShortRationale |
|---|---:|---|---|
| `<ADA coordinate>` | `<0..5>` | `<E.21 label>` | `<why the lower adjacent value would understate the expressed content; why the higher adjacent value would overstate it, or for 5 what makes 4 too weak and what would lower or reopen>` |

`5` is not required for every use. Stop conditions are declared before evaluation. A lower diagnostic floor may be used for exploration or internal discussion, but it does not make the decision ready for developer work, implementation commitment, or governance enforcement.

#### C.32.ADA:4.2 - Complete coordinate set

Evaluate every coordinate. If a coordinate is not live, mark it `notTriggered` only with a short reason grounded in the declared use.

| Coordinate | What is evaluated | Repair when weak |
|---|---|---|
| `BoundedDecisionQuestionRecoverability` | Decision subject, described holon, bounded context, status, and decision question can be recovered. | Return to `C.32.PAD` decision subject fields. |
| `CandidateBasisAndSelectionTraceability` | Candidate palette, residual frame, comparison, selection, selected set, or reason no candidate-set question is live is recoverable. | Return to `C.32`, `C.32.MLAO`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, or `C.11`. |
| `AffectedStructureAndDescriptionAdequacy` | Affected selected structures, views, architecture descriptions, correspondence, structural-information lens uses, and source-return are recoverable. | Return to `C.30`, `C.30.ASV`, `C.30.AD`, `A.6.F`, `A.6.M`, or `C.29`. |
| `ArchitectureCharacteristicTradeoffAdequacy` | Architecture characteristics, criteria rows, Q-Bundles, eval readings, accepted losses, and guardrails are explicit. | Return to `C.32.ACS`, `C.32.HCS`, `C.25`, `C.32.ACE`, `C.16`, `C.31`, or `C.31.ASAP`. |
| `MethodAndWorkDockingAdequacy` | Method-use instructions, responsible roles, work boundaries, readiness, and expected structure effects are usable. | Return to `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, or `C.24`. |
| `ArchitectDeveloperSplitAdequacy` | Architect-owned structures, developer-owned refinement, holon-transition or BOSC-triggered boundary refs, and source-return condition are explicit. | Return to `C.32.PAD`, `A.15`, `B.2.P` for claim-kind recovery, and `B.2` when whole reidentification is triggered. |
| `PublicationProjectionAdequacy` | ADR-like or other publication projection carries the needed section functions for the declared readers. | Return to `C.32.ADR`, `E.17`, or `E.24.PUB`. |
| `EvidenceEvalAndGateExitAdequacy` | Eval, evidence, assurance, gate, or governance exits are named only when live and routed to governing patterns. | Return to `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or local governance pattern. |
| `EvolutionAndReopenConditionAdequacy` | Reopen, supersession, stronger-source return, and changed-context triggers are clear. | Return to `C.32.PAD`, `C.32.FAIL`, `C.18`, `C.19`, `E.23`, or source-currentness pattern. |
| `TransformerTransformedCorrespondenceAdequacy` | Required correspondence between transformer-side and transformed-side structures is present when the decision depends on it. | Return to `C.32.CONWAY`, `A.15`, `A.3.4`, `A.3.4.P`, or `E.18`. |
| `NonOverreadAndReceivingPatternAdequacy` | The decision, description, publication, method, eval, evidence, assurance, and gate claims are kept with their governing patterns. | Return to `A.7`, `A.6.P`, `E.10`, `F.18`, or the exact receiving pattern. |
| `ConsequenceAndRepairGuidanceAdequacy` | Consequences, accepted losses, weak coordinates, and next repair instructions are actionable for the declared use. | Return to PAD consequence rows, ADR section functions, or the coordinate-specific repair pattern. |

#### C.32.ADA:4.3 - Use-specific stop conditions

Declare the use before scoring. Common uses:

| Declared use | Ordinary stop condition |
|---|---|
| Internal architecture discussion | Every triggered coordinate is evaluated; `0 absent` coordinates block reliance, and values below `3 sufficientlyExpressedForDeclaredUse` carry repair owners. |
| Ready for architecture review | No triggered coordinate below `3 sufficientlyExpressedForDeclaredUse`; candidate basis, trade-off, affected structures, work split, and reopen condition are strong enough for reviewers to inspect by value. |
| Ready for developer work or implementation commitment | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse` unless a governing project decision explicitly declares a lower diagnostic floor and says the result is not an implementation commitment. |
| Ready for ADR-like publication | Publication projection, section functions, status, source-return, and supersession are at least `4 wellExpressedForDeclaredUse`; if the record will guide developer work, use the developer-work floor too. |
| Ready for governance enforcement | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse`; the gate, evidence, assurance, or governance pattern still owns enforcement status. |

Use these as ordinary defaults. A project can declare stricter stop conditions. It must not weaken a triggered coordinate by hiding it under an average, and it must not call a diagnostic result ready for developer work or governance enforcement.

#### C.32.ADA:4.4 - Small complete evaluation slice

```text
ArchitectureDecisionAdequacyEvaluation@OrderFlow:
  declaredUse: readyForDeveloperWork
  architectureDecisionRelationRef: PAD:order-flow-event-integration
  architectureDecisionRecordProjectionRef: ADR:order-flow-event-integration
  noAveragePolicy: true
  stopCondition: every triggered coordinate >= 4 wellExpressedForDeclaredUse
  strongestBlockingCoordinates:
    - MethodAndWorkDockingAdequacy
    - ArchitectureCharacteristicTradeoffAdequacy
  result: repairBeforeUse
```

| Coordinate | Value | Label | Short rationale and repair |
|---|---:|---|---|
| `BoundedDecisionQuestionRecoverability` | `4` | `wellExpressedForDeclaredUse` | Subject, holon, context, status, and question are clear; `5` would need transfer evidence across another product-family slice. |
| `CandidateBasisAndSelectionTraceability` | `4` | `wellExpressedForDeclaredUse` | Candidate palette and selected option are cited; `5` would need another team to replay the selection without local recovery. |
| `AffectedStructureAndDescriptionAdequacy` | `4` | `wellExpressedForDeclaredUse` | Module and information structures plus C.30.ASV refs are usable; `5` would need a worked cross-team source-return case. |
| `ArchitectureCharacteristicTradeoffAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Substitutability gain and latency loss are named, but guardrail eval rows are incomplete; repair through `C.32.ACS`, `C.32.ACE`, `C.25`, and `C.16`. |
| `MethodAndWorkDockingAdequacy` | `2` | `partiallyExpressedForDeclaredUse` | The ADR says "use events" but lacks method description, responsible role, readiness exit, and expected structure effect; repair through PAD and `A.15`. |
| `ArchitectDeveloperSplitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Architect-owned event boundary is clear, but developer-owned schema refinement lacks source-return threshold; repair through PAD and, if level pressure is real, `B.2.P` or `B.2`. |
| `PublicationProjectionAdequacy` | `4` | `wellExpressedForDeclaredUse` | ADR section functions are mapped; `5` would need a replayed package-update or supersession case. |
| `EvidenceEvalAndGateExitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Eval and gate exits are named but not replayable enough for developer commitment; repair through `C.32.ACE`, `C.16`, `A.10`, `B.3`, or `A.21` as triggered. |
| `EvolutionAndReopenConditionAdequacy` | `4` | `wellExpressedForDeclaredUse` | Reopen triggers cover latency and schema-version pressure; `5` would need an executed supersession slice. |
| `TransformerTransformedCorrespondenceAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Toolchain and product-structure correspondence is locally stated; repair through `C.32.CONWAY` if it becomes load-bearing for work organization. |
| `NonOverreadAndReceivingPatternAdequacy` | `4` | `wellExpressedForDeclaredUse` | Decision, ADR, method, eval, and gate claims are routed to owners; `5` would need a near-miss showing avoided overread. |
| `ConsequenceAndRepairGuidanceAdequacy` | `4` | `wellExpressedForDeclaredUse` | Consequences and repair loci are actionable; `5` would need transfer evidence across another holon kind. |

**PAD adequate, ADR weak.** A fixture architecture decision relation can reach `4 wellExpressedForDeclaredUse` on every triggered PAD, method, work-split, trade-off, and reopen coordinate while the trade-study memo omits status and supersession. ADA returns only the publication projection to `C.32.ADR`; it does not rewrite the PAD relation.

**ADR readable, PAD weak.** A Markdown ADR can have clear headings, status, context, decision, and consequences while the project relation lacks candidate basis, affected selected structures, and method docking. ADA returns the decision relation to `C.32.PAD`, `C.32`, and `A.15`; template completeness does not make the architecture decision adequate.

### C.32.ADA:5 - Archetypal Grounding

**Developer-work readiness.** A service architecture decision has strong candidate traceability and trade-off rationale, but the ADR only says "teams should use events." ADA gives `MethodAndWorkDockingAdequacy = 2 partiallyExpressedForDeclaredUse` because responsible roles, method description, expected structure effect, and readiness exit are not recoverable. The repair returns to PAD and A.15 before developers are instructed.

**ADR-publication readiness.** A manufacturing architecture decision is clear, but the trade-study memo omits status and supersession. ADA gives `PublicationProjectionAdequacy = 2 partiallyExpressedForDeclaredUse` and `EvolutionAndReopenConditionAdequacy = 3 sufficientlyExpressedForDeclaredUse`. The repair returns to C.32.ADR for record status and supersession rows.

**Architecture review.** A method-family architecture decision has candidate options and method instructions, but no declared architecture characteristics. ADA gives `ArchitectureCharacteristicTradeoffAdequacy = 0 absent`. The repair returns to C.32.ACS and C.25 before review can judge the decision.

**Governance enforcement.** A toolchain-product correspondence decision depends on team and tool structures. ADA evaluates `TransformerTransformedCorrespondenceAdequacy`; if the correspondence refs are absent, the repair returns to C.32.CONWAY before governance can enforce the method.

### C.32.ADA:6 - Bias-Annotation

| Risk handled | How C.32.ADA handles it |
|---|---|
| Record completeness as adequacy | ADR projection is one coordinate, not the whole evaluation. |
| Average-score drift | Coordinate values are not averaged; weak coordinates drive repair. |
| Generic review prose | Each weak coordinate names a governing repair pattern. |
| Gate confusion | ADA does not approve, certify, assure, or pass a gate. |
| Hidden method failure | Method and work docking has its own coordinate. |
| Evolution blindness | Reopen, supersession, and source-return have explicit coordinates. |

### C.32.ADA:7 - Conformance Checklist

| Requirement | Required result |
|---|---|
| `CC-ADA-1` | Declared use and stop condition are written before evaluation. |
| `CC-ADA-2` | The evaluated decision relation and optional ADR projection are cited. |
| `CC-ADA-3` | Every coordinate is scored `0 absent` through `5 exceptionallyExpressedForDeclaredUse` or marked `notTriggered` with a grounded reason. |
| `CC-ADA-4` | Every value has adjacent-value rationale, not only a number. |
| `CC-ADA-5` | No coordinate values are averaged or converted into one global score. |
| `CC-ADA-6` | Weak coordinates name repair pattern refs and repair instructions. |
| `CC-ADA-7` | Evidence, assurance, gate, measurement, eval, publication, method, work, and pattern-quality claims exit to their governing patterns. |

### C.32.ADA:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `DecisionAdequacyAverage` | Strong rationale and readable ADR produce a high average despite absent method docking. | Remove the average; use weakest triggered coordinates to choose repair. |
| `ADRCompletenessAsDecisionAdequacy` | The record has all headings, so the decision is treated as adequate. | Evaluate PAD relation, method docking, trade-off, source-return, and reopen conditions separately. |
| `ReviewCommentWithoutRepairPattern` | The reviewer says "unclear" or "not enough detail" without a target repair pattern. | Assign the weak coordinate to `C.32.PAD`, `C.32.ADR`, `A.15`, `C.30.AD`, `C.32.ACS`, or another exact governing pattern. |
| `GateByScale` | A value of `4` or `5` is treated as approval or certification. | Keep ADA as evaluation; use `A.21`, `A.10`, `B.3`, or governance patterns for gate, evidence, assurance, and enforcement claims. |
| `NotTriggeredAsConvenience` | A difficult coordinate is marked not triggered to close the review. | Require a declared-use reason and receiving-pattern boundary; otherwise score it and repair. |
| `MethodDockingSkipped` | The decision is adequate for architecture discussion but then used to direct developer work. | Re-declare use as developer-work readiness and evaluate method docking, work split, and publication handoff. |

### C.32.ADA:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Adequacy is coordinate-based. | Review can point to exact repairs instead of vague approval or rejection. | Evaluation takes longer than reading a record once. |
| Declared use controls stop condition. | A decision can be adequate for one use and inadequate for another without contradiction. | Teams must state intended use before scoring. |
| No average is allowed. | Weak but critical coordinates stay visible. | Some dashboards and summaries need redesign. |
| Repair exits are mandatory. | Review results become actionable. | Reviewers must know or find the receiving pattern. |

### C.32.ADA:10 - Rationale

C.32.ADA exists because architecture-decision adequacy is not one property. It is a family of recoverability and use-readiness coordinates across decision relation, selected structures, architecture characteristics, method docking, work split, publication projection, evidence or eval exits, and evolution.

The pattern follows the same discipline as FPF quality evaluation: declared use first, complete coordinate set, ordinal values with rationale, no average, and targeted repair. It remains architecture-specific because the coordinates are tied to PAD, ADR projection, architecture descriptions, candidate synthesis, method-use instructions, and architecture-characteristic trade-offs.

### C.32.ADA:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ADA. Keep a source citation only when it changes a coordinate, value meaning, stop condition, or repair exit.

| Source to inspect | Why this source is load-bearing here | Transfer into ADA | Concrete ADA mutation | Blocked overread |
|---|---|---|---|---|
| Current FPF `E.21` scale discipline | Existing FPF pattern for declared-use evaluation, exact `0 absent` through `5 exceptionallyExpressedForDeclaredUse` labels, complete coordinates, adjacent-value rationale, and no averaging. | Reuse the value domain and evaluation discipline for architecture decisions without copying pattern-quality coordinates. | ADA requires declared use, complete coordinate set, E.21 value labels with adjacent rationale, no average, and use-specific stop conditions. | E.21 pattern-quality status and coordinates are not architecture-decision adequacy. |
| `C.32.PAD` and `C.32.ADR` | PAD and ADR define the decision relation and publication projection being evaluated. | Make relation adequacy and projection adequacy separate coordinates. | ADA can say a PAD relation is usable while ADR projection needs repair, or the reverse. | A complete ADR does not make the decision relation adequate. |
| ISO/IEC/IEEE 42010:2022 official standard (`https://www.iso.org/standard/74393.html`; IEEE page `https://standards.ieee.org/ieee/42010/6846/`) with the 42010 companion site as secondary reading (`https://iso-architecture.org/42010/`) | Current official source for architecture descriptions, viewpoints, views, correspondence, and rationale; the companion site is used only as secondary reading. | Add coordinates for affected structure, architecture-description adequacy, and source-return. | ADA routes weak description coordinates to `C.30.AD` and `C.30.ASV`. | Architecture-description adequacy does not decide or approve the architecture. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner source for architecture feedback and incremental change under eval-like mechanisms. | Add evolution, reopen, guardrail, and confirmation coordinates. | ADA checks reopen and eval exits before a decision is used for long-running work. | Source-side fitness-function wording is not imported as ADA object naming. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Current practitioner source for trade-off analysis under competing characteristics. | Add architecture-characteristic trade-off adequacy and accepted-loss repair. | ADA sends weak trade-off coordinates to ACS, ACE, C.16, C.25, C.31, or C.31.ASAP. | Trade-off discussion is not an assurance claim or governance approval. |
| 2026 ADR violation-detection research (`https://arxiv.org/abs/2602.07609`) | Recent research shows explicit, code-inferable decisions are easier to check than implicit deployment or organization decisions. | Add confirmation, source-return, method, deployment, and organization refs to adequacy checks when live. | ADA scores confirmation and method docking separately and blocks hidden organizational knowledge from passing as ready. | Automated violation detection is not proof, evidence, assurance, or gate passage. |

**Source-currentness boundary.** Recheck a source row when FPF evaluation discipline, architecture-decision practice, ADR violation checking, evolutionary-architecture eval practice, or project governance changes a coordinate, value meaning, or repair exit.

### C.32.ADA:12 - Relations

- **Builds on:** `C.32.PAD`, `C.32.ADR`, `C.32.P2S`, `C.32`, `C.32.MLAO`, `C.32.ACS`, `C.32.ACE`, `C.32.CONWAY`, `C.32.FAIL`, `C.30.AD`, `C.30.ASV`, `A.15`, `C.16`, `C.25`, `C.29`, `E.17`, and `E.21`.
- **Evaluation boundary:** ADA evaluates architecture-decision adequacy for declared use. It does not perform candidate synthesis, comparison, selection, selected-set publication, local choice, evidence support, assurance, gate passage, governance enforcement, or pattern-quality evaluation.
- **Decision and projection boundary:** Use `C.32.PAD` to repair the decision relation and `C.32.ADR` to repair ADR-like publication projection.
- **Description and structure boundary:** Use `C.30`, `C.30.AD`, and `C.30.ASV` for architecture claim, description, and view adequacy.
- **P2S docking:** Use `C.32.P2S` when a weak decision-adequacy row must reopen the connected architecturing flow rather than only repair the decision record.
- **Method and work boundary:** Use `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, and `C.24` for method, work, readiness, pattern-use, and agentic tool-use claims.
- **Characteristic and eval boundary:** Use `C.32.ACS`, `C.32.HCS`, `C.25`, `C.32.ACE`, `C.16`, `C.31`, and `C.31.ASAP` for characteristic rows, Q-Bundles, eval programs, measurement, modularity, and scale preference.
- **Evidence, assurance, gate, and governance boundary:** Use `A.10`, `B.3`, `A.21`, and local governance patterns when those claims are live.

### C.32.ADA:13 - Footer marker

C.32.ADA closes when `ArchitectureDecisionAdequacyEvaluation@Project` declares the use and stop condition, cites the evaluated decision relation and optional projection, evaluates every coordinate with an E.21 value label and rationale or grounded not-triggered status, names weakest blocking coordinates, assigns repair patterns and repair instructions, and avoids average-score replacement.

### C.32.ADA:End

