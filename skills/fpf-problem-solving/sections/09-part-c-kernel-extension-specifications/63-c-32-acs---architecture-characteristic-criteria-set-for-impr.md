## C.32.ACS - Architecture Characteristic Criteria Set for Improvement Cycles

> **Type:** Architecture characterization pattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.ACS:1 - Problem frame

Use this pattern when a project must turn architecture-characteristic pressure into a small project criteria set for architecture improvement, candidate synthesis, residual optimization, and later eval work.

Primary working reader: an architect or architecture-responsible practitioner turning broad quality names into project criteria rows for the next improvement cycle.

Typical entry phrases:

```text
"Maintainability matters, but which bearer and scale make it an architecture criterion here?"
"We can optimize only a few rows; which characteristics drive optimization and which guard against loss?"
"A method, role, AI workflow, or built asset has trustworthiness or teachability pressure; which Q-Bundle slot or ACS row is current?"
```

**First-minute use slice.** A product-family architect has HCS starter heads and source catalogue names for maintainability, substitutability, evidence reuse, safety, availability, latency, and scale amenability. Using C.32.ACS, the practitioner builds project rows, marks maintainability, substitutability, and evidence reuse as optimization indicators, keeps safety and availability as monitored guardrails, and records bearers, scale form, proxy risk, protected losses, and source-return condition. C.32 can now synthesize candidates against declared criteria instead of against a loose list of quality words.

The primary `EntityOfConcern` is one project architecture-characteristic criteria set for improvement cycles. It prepares rows for C.32 synthesis, C.32.MLAO residual work, C.32.ACE eval programs, and later receiving patterns. Starter packs, Q-Bundles, measurement methods, eval programs, candidate palettes, comparison rules, selection results, G.5 publications, local choices, and architecture decisions remain separate objects.

Ordinary working move: make one row per project architecture characteristic, bind its bearer and scale, mark whether it drives optimization, guards against loss, or only gives context, and record what eval reading can reopen synthesis.

The first useful output is `ArchitectureCharacteristicCriteriaSet@Project`:

For a first pass, fill only the described holon, bounded context, architecture use, three to five draft row names, bearer or selected structure, use class, protected losses, receiving use, and reopen condition. Add readings, target bands, and eval-program references only when the current receiving use needs them.

```text
ArchitectureCharacteristicCriteriaSet@Project:
  describedHolonRef:
  boundedContextRef:
  architectureUseRef:
  holonFamilyStarterPackRef?:
  sourceCatalogueRefs?:
  draftProjectCriteriaRows:
    - architectureCharacteristicRef:
      sourceHeadOrStarterPackRef?:
      bearerOrSelectedStructureRefs:
      endpointShape: singleCharacteristic | qBundle | qBundleSlot | sourceVocabularyOnly
      qBundleRef?:
      architectureQuestion:
      scaleFormRef:
      polarity:
      useClass: optimizationIndicator | monitoredGuardrail | contextOnly
      currentReadingRef?:
      targetBandOrStopCondition?:
      readingMethodRefOrNoReadingReason:
      evalProgramRefs?:
      proxyRisk:
      protectedCounterCharacteristicRefs:
      receivingUseRef:
      sourceReturnCondition:
  optimizationIndicatorRowRefs:
  monitoredGuardrailRowRefs:
  contextOnlyRowRefs?:
  improvementCycleRef?:
  reopenCondition:
```

`draftProjectCriteriaRows` are draft project criteria rows. They are not candidate architectures, selected architectures, or a selected set returned by `A.19.SelectorMechanism`.

What goes wrong if C.32.ACS is missed: the team says that the architecture should be more maintainable, scalable, modular, safe, or evolvable, but no one can say which selected structures carry the characteristic, which few rows are criteria for the next optimization, which rows only guard against loss, which C.25 Q-Bundle is involved, or which eval result can reopen synthesis.

What C.32.ACS buys in practice: the practitioner can reduce broad catalogue and starter-pack material to draft project criteria rows, then to three to five optimization indicators, while keeping other important characteristics as monitored guardrails against Goodhart-style proxy loss.

Adoption test: after using C.32.ACS, the project can name the few rows that drive optimization, the guardrail rows that protect against loss, and the bearer, scale, proxy risk, receiving use, and reopen condition for each live row.

Not this pattern when the current work is choosing the holon-family starter pack, modeling a Q-Bundle, validating a measurement method, designing an eval program, synthesizing candidates, comparing or selecting candidates, choosing locally, publishing a selected set, or deciding the project architecture.

Common exits by claim kind:

- `C.32.HCS` for holon-family starter packs.
- `C.25` for Q-Bundles and composite quality families.
- `C.16` for measurement templates, readings, units, thresholds, or comparability claims.
- `C.32.ACE` for eval programs and eval results over declared rows.
- `E.13` when an indicator, score, or dashboard starts replacing the declared architecture concern.
- `E.22` and `E.23` for improvement-question framing and repeated improvement method.
- `C.32` for candidate synthesis and `C.32.MLAO` for residual-reducing candidates.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for publication of a selected set.
- `A.10` and `B.3` when evidence or assurance claims are being made.
- `C.32.PAD` for project decision.

### C.32.ACS:2 - Problem

Architecture synthesis needs criteria. A multi-criteria or multilevel optimization phrase is empty until the criteria are named. In C.32-family work, those criteria are admitted architecture-characteristic rows or declared C.25 Q-Bundle slots of the described holon under the current bounded context.

Architecture characteristics are not the same as user functions. Functional demand says what the holon must do. An architecture characteristic says whether the selected structures make that demand maintainable, controllable, replaceable, observable, evolvable, scalable, affordable, safe enough, or otherwise acceptable.

Source catalogues and textbooks can offer hundreds of possible quality or architecture terms. A project may inspect dozens. The actual optimization loop should normally use only a few indicatorized rows, often three to five. Other important rows remain monitored guardrails or context-only rows so that optimizing one visible measure does not damage functional adequacy, safety, evidence, maintainability, or another protected architecture concern.

C.32.ACS supplies the project criteria set and scale rows. It does not create the holon-family starter pack, define a Q-Bundle, validate a measurement method, run an eval, compare candidates, choose an architecture, or decide the project architecture.

### C.32.ACS:3 - Forces

| Force | Tension |
|---|---|
| Catalogue breadth vs project attention | Many quality names are available, but a project needs a small criteria set for the next improvement cycle. |
| Holon recurrence vs bearer rebinding | Characteristic heads can recur across holon families or declared holon levels, but each project row must bind the project bearer and scale. |
| Optimization indicator vs guardrail | A row can drive optimization, protect against loss, or only provide context. These uses must not collapse. |
| Architecture characteristic vs function | Functional adequacy constrains synthesis, but functional characteristics are not architecture criteria by name. |
| Q-Bundle richness vs row use | Composite quality families belong to C.25, while ACS admits rows or slots for architecture work. |
| Eval program vs criterion | An eval program can read or compare rows, but it is not the row and not the project criterion. |

### C.32.ACS:4 - Solution

Build an `ArchitectureCharacteristicCriteriaSet@Project` from starter heads, source catalogues, architecture constraints, and the project improvement question.

#### C.32.ACS:4.1 - Kind settlement

`ArchitectureCharacteristicCriteriaSet@Project` is a project working record: it holds criteria rows for improvement work. It does not create a new `U.*` kind and does not replace a Q-Bundle, measurement result, eval program, comparison rule, or decision record.

An architecture characteristic is the property or quality-like head under discussion. A C.25 Q-Bundle is the structured form for a composite quality family. A scale row binds one characteristic or Q-Bundle slot to a bearer, scale form, use class, and receiving use. An architecture-characteristic eval program belongs to `C.32.ACE`; it evaluates one declared row, coupled rows, Q-Bundle slots, or C.32 candidate palettes.

#### C.32.ACS:4.2 - Criteria-set construction

Work in this order:

1. Name the described holon, bounded context, architecture use, and improvement cycle or one-pass eval use.
2. Start from a `C.32.HCS` starter pack when the project has no draft criteria rows yet. Use source catalogues only as input, not as the criteria set.
3. Build draft project criteria rows. There may be dozens of draft rows when broad scanning is needed, but each row must have a possible bearer, use reason, and receiving pattern.
4. For each source or starter head, decide whether it is one architecture characteristic, one C.25 Q-Bundle, one Q-Bundle slot, or only source vocabulary.
5. Narrow the optimization-indicator core. The ordinary target is three to five rows. More rows require an explicit reason, such as a regulated trade-off study or a multi-team decision use.
6. Classify remaining admitted rows as `monitoredGuardrail` or `contextOnly`. A guardrail protects against a loss caused by optimizing another row; a context-only row helps interpretation but does not drive optimization now.
7. Bind each admitted row to bearer or selected structure, scale form, polarity, current reading or no-reading reason, proxy risk, protected counter-characteristics, receiving use, and source-return condition.
8. Reference `C.32.ACE` only after the row exists and an eval program is needed for current characterization, candidate comparison, monitoring, or preparing inputs for `A.19.SelectorMechanism`.
9. Reopen the criteria set when the holon family changes, a B.2 whole reidentification changes the bearer, a guardrail degrades, an eval program no longer fits its declared parity frame, or the source-currentness relation changes the acceptable trade-off.

#### C.32.ACS:4.3 - Row use classes

Use `optimizationIndicator` only when the row can responsibly guide architecture changes now. A project normally carries only three to five such rows.

Use `monitoredGuardrail` when the row protects against a loss caused by optimizing another row. Guardrails can have readings and eval results, but they do not define the cycle's optimization direction.

Use `contextOnly` when the row helps interpretation but should not drive improvement, comparison, or selection in the current cycle.

**Stop condition.** Stop C.32.ACS when the criteria set names draft rows, use class, bearer or selected structure, scale form, proxy risk, protected counter-characteristics, receiving use, source-return condition, and any C.32.ACE or Q-Bundle reference that the current use actually needs.

**Lowering condition.** Lower an `optimizationIndicator` to `monitoredGuardrail` or `contextOnly` when it no longer guides the next architecture change or its proxy risk is not controlled. Lower a draft row to source vocabulary when bearer, scale form, use reason, receiving use, or protected counter-characteristics are missing. Return to `C.32.HCS` when the holon-family starting point is wrong, to `C.25` when the row is really composite, and to the named receiving pattern when measurement, eval, comparison, publication, local choice, evidence, assurance, or decision work is current.

#### C.32.ACS:4.4 - Improvement-cycle use

When a row is used inside an improvement cycle, add:

```text
ArchitectureCharacteristicImprovementRow@Project:
  criteriaRowRef:
  useClass:
  currentArchitectureReadingRefOrQualitativeState:
  evalResultRefs?:
  intendedArchitectureChangeDirection:
  candidateSelectedStructureChangeRefs?:
  expectedGain:
  protectedLosses:
  observedReadingAfterChange?:
  nextSynthesisTrigger?:
  stopContinueOrSourceReturnCondition:
```

The row prepares improvement work. It does not carry a claim outside its declared scale and use. An eval result is a reading over a declared row; another pattern may use it as source material for an A.10 evidence relation, improvement feedback, comparison input, selection input, or decision input only when that receiving pattern is named by value. It does not become the characteristic, the declared architecture concern, the architecture choice, or the optimization direction.

### C.32.ACS:5 - Worked slices

**Manufacturing cell.** HCS suggests maintainability, locality, function-bearer fit, change reach, and scale amenability. ACS keeps nine draft criteria rows, then marks setup-change reach, function-bearer fit, and exception growth as optimization indicators. ACS records safety and evidence reuse as monitored guardrails. C.32 later synthesizes universal-fixture candidates under those criteria.

**Method-family architecture.** HCS suggests repeatability, teachability, transferability, evidence reuse, exception growth, and change reach. ACS marks evidence reuse, exception growth, and transferability as optimization indicators. Teachability goes to C.25 because it depends on learner scope, measures, mechanisms, and evidence.

**AI-agent architecture.** HCS suggests evidence refresh, policy controllability, latency, observability, and rollback. ACS marks policy controllability, evidence refresh, and latency as optimization indicators. Benchmark performance is not an architecture characteristic by name; it can supply an eval reading only after the bearer, scale, parity frame, and receiving use are declared.

**Role-team architecture.** A hospital escalation team starts from coordination load, accountability clarity, decision latency, evidence custody, and role substitutability. ACS marks decision latency, accountability clarity, and evidence custody as optimization indicators for the next architecture cycle, keeps patient-safety loss and role-continuity loss as guardrails, and leaves staffing choice to the receiving decision pattern.

### C.32.ACS:6 - Kind and Receiving-Claim Boundary

C.32.ACS governs project criteria-set construction for architecture improvement. It does not govern:

- holon-family starter packs, governed by `C.32.HCS`;
- architecture-characteristic eval programs, governed by `C.32.ACE`;
- C.25 Q-Bundle normal form, governed by `C.25`;
- C.16 measurement templates or readings, governed by `C.16`;
- C.31 modularity and reusable-structure characteristic repair, governed by `C.31`;
- C.31.ASAP scale-preference claims, governed by `C.31.ASAP`;
- E.22 question framing and E.23 repeated improvement method, governed by `E.22` and `E.23`;
- C.32 candidate synthesis, governed by `C.32`;
- A.19.CPM comparison, A.19.SelectorMechanism selection, C.11 local choice, G.5 publication of a selected set, or architecture-decision work for `C.32.PAD`.

### C.32.ACS:7 - Conformance requirements

| Requirement | Required result |
|---|---|
| `CC-ACS-1` | The criteria set names the described holon, bounded context, architecture use, and receiving use. |
| `CC-ACS-2` | Source catalogue, HCS starter pack, draft project criteria rows, optimization indicators, monitored guardrails, and context-only rows remain distinct. |
| `CC-ACS-3` | The ordinary optimization core is three to five rows, or the text states why more are needed. |
| `CC-ACS-4` | Each row names a bearer or selected structure. A characteristic without a bearer is not admitted as an architecture criteria row. |
| `CC-ACS-5` | User function, architecture characteristic, Q-Bundle, scale row, reading, eval program, and eval result remain separate. |
| `CC-ACS-6` | Any composite quality family belongs to `C.25`; ACS may reference the Q-Bundle or one declared slot. |
| `CC-ACS-7` | Each optimization row names proxy risk and protected counter-characteristics before it is used in C.32, C.32.MLAO, C.32.ACE, or E.23. |
| `CC-ACS-8` | Eval-program construction belongs to `C.32.ACE` and is not used as criteria rows. |
| `CC-ACS-9` | The criteria set does not compare, select, publish, decide, certify, or carry an architecture-adequacy claim by itself. |

### C.32.ACS:8 - Common failures and repairs

| Failure | Working symptom | Repair |
|---|---|---|
| `CatalogueCopyAsCriteriaSet` | A project imports a long list of ilities and treats the list as architecture guidance. | Use HCS for starter heads, then build ACS rows, mark optimization indicators, and keep guardrails and context-only rows separate. |
| `TooManyOptimizationIndicators` | Dozens of rows drive optimization at once. | Keep the few rows that change the next synthesis step; demote the rest to monitored guardrails or context-only rows. |
| `FunctionGoalAsArchitectureCriterion` | A user-visible function is used as the architecture optimization criterion. | Recover the function through `A.6.F`; then name the architecture characteristic that makes the function sustainable. |
| `QBundleDuplicatedAsScaleSet` | Maintainability, availability, security, teachability, or trustworthiness is treated as one ACS row when the truth depends on several typed slots. | Open `C.25`, construct or reference the Q-Bundle, then select only the relevant slot for ACS use. Keep any report-only proxy outside the criteria row unless its bearer, scale, proxy risk, and receiving use are declared. |
| `EvalProgramAsCriterion` | A test, monitor, source-side fitness function, benchmark, dashboard, or eval result is named as the criterion. | Name the characteristic row first; eval-program construction belongs to `C.32.ACE` and measurement claims belong to `C.16`. |
| `HolonLevelCarryoverWithoutRebinding` | An engineered-system row is copied to a method, role, or culture without changing bearer, scale, or admissible use. | Return to HCS and ACS; rebind the row to the new holon family and selected structures. |
| `LocalGainHidesCounterLoss` | A candidate improves one row while worsening evidence burden, control burden, source-return cost, or functional adequacy. | Add monitored guardrail rows and open `E.13` when proxy-to-value drift appears before comparison or next synthesis. |
| `ReadingAsDecision` | A better reading is treated as the selected architecture. | Keep the reading as feedback; explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, local choice to `C.11`, publication of a selected set to `G.5`, and project architecture decision to `C.32.PAD`. |

### C.32.ACS:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Architecture optimization gets declared criteria. | C.32 and C.32.MLAO can use multi-criteria language without unnamed criteria. | The project must admit and type rows before synthesis or optimization claims. |
| The 300-to-3 problem is handled by staged admission. | Broad catalogues inform the project without serving as the project criteria set. | Some familiar qualities must be guardrails or context rows. |
| Anti-Goodhart guardrails are explicit. | Optimization can protect functional adequacy and other architecture concerns. | A single convenient score cannot govern choice by itself. |
| Measurement and eval stay clean. | C.16 and ACE keep readings, eval programs, and eval results separate from criteria. | Some eval programs require additional receiving-pattern work before they can drive action. |
| Q-Bundle structure stays clean. | Composite quality families keep their C.25 structure. | ACS cannot shortcut a composite family into one scalar row. |

### C.32.ACS:10 - Rationale

Architecture optimization is meaningful only after the criteria are named. ACS supplies that middle object: not a generic quality catalogue, not a starter pack, not a Q-Bundle, not an eval program, and not a decision, but a project criteria set that can guide synthesis, residual reduction, and repeated improvement.

The pattern stays holonic by allowing starter heads to recur across holon families while requiring bearer and scale rebinding. It stays action-facing by limiting optimization indicators and keeping non-optimized criteria rows as guardrails.

### C.32.ACS:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.ACS. Keep a source citation only when the draft uses it to set or revise a criteria-row field, use-class rule, or receiving-pattern boundary.

| Source to inspect | Why this source is load-bearing here | Transfer into ACS | Concrete ACS mutation | Blocked overread |
|---|---|---|---|---|
| FPF source presentation `ТриПрототипаТриОшибки` (2022-03-26) | The presentation distinguishes eval from test and requires characteristic cards, scale procedures, fair comparison, explicit indicatorization, hard constraints, optimization goals, and risk signals. | Put characteristic rows and use classes before any ACE eval program or explicit comparison. | ACS row shape carries use class, scale form, current reading or no-reading reason, proxy risk, protected counter-characteristics, receiving use, and source-return condition. | An eval, test, dashboard, score, or hard constraint is not the architecture characteristic or project criterion by itself. |
| ISO/IEC 25010:2023 (`https://www.iso.org/standard/78176.html`) and SQuaRE quality-model practice | Current standard source for product quality vocabulary and measurement context. | Use standards as source catalogue material that must be rebound to the described holon, bearer, scale, and use class. | ACS separates source catalogue, HCS starter pack, draft project criteria rows, optimization indicators, monitored guardrails, and context-only rows. | A standard quality-model characteristic is not automatically an FPF project criterion, scale row, eval program, or holon ontology. |
| Richards and Ford, `Fundamentals of Software Architecture`, 2nd ed. (`https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/`) | Current practitioner line treats architecture characteristics as criteria for success, trade-off analysis, scope, and governance. | Criteria rows must be admitted and typed before synthesis, residual optimization, measurement, or governance claims. | ACS rows supply the criteria consumed by `C.32`, `C.32.MLAO`, and later receiving patterns. | A broad architecture-characteristic list is not a project criteria set. |
| Ford, Richards, Sadalage, and Dehghani, `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Mature practitioner line for least-worst trade-offs among competing architecture characteristics. | Keep explicit protected losses; explicit comparison belongs to `A.19.CPM` when comparison is being made. | ACS requires use class, proxy risk, protected counter-characteristics, and downstream comparison boundary. | No single criterion or local gain may dominate without naming the losses it can hide. |
| Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`), `Software Architecture Metrics` (`https://www.oreilly.com/library/view/software-architecture-metrics/9781098112226/`), and `C.32.ACE` | Current practitioner line for guided change and repeatable eval over architecture characteristics. | Restore source-side fitness-function wording as eval programs over declared ACS rows. | Row shape has `evalProgramRefs?` and names ACE as the eval-program governing pattern after the row exists. | An eval program or metric is not a characteristic kind, project criterion, selected architecture, or decision. |
| Current FPF `C.25` and `E.13` | Local receiving law for composite quality families and proxy-for-value drift. | Keep Q-Bundle structure and proxy repair outside ACS while carrying the needed links. | Row shape includes `endpointShape`, `qBundleRef?`, `proxyRisk`, and `protectedCounterCharacteristicRefs`; proxy drift exits to `E.13`. | A composite quality family is not one scalar row, and a convenient indicator is not the declared architecture concern. |
| ATAM lineage and ATRAF 2025 (`https://arxiv.org/abs/2505.00688`) | Mature and current architecture-evaluation practice binds quality attributes to scenarios, trade-offs, sensitivity points, risks, and repeated refinement. | Admit a quality word as a project row with bearer, scale, polarity, counter-characteristics, and receiving use before it affects synthesis. | Explicit comparison belongs to `A.19.CPM`; composite quality bundles belong to `C.25`; ACS retains row preparation. | Scenario analysis and trade-off vocabulary do not compare or choose candidates until the receiving comparison, selection, choice, or decision pattern is being used. |

**Source-currentness boundary.** Use each source row only for the ACS field, use-class rule, or receiving-pattern boundary named in that row. Recheck the row when a named standard, book edition, source presentation, FPF receiving pattern, or current architecture-evaluation line changes the transferred move. If the project wants measurement, eval-program design, comparison, selection, publication of a selected set, local choice, evidence, assurance, or decision use, leave ACS and open the receiving pattern.

### C.32.ACS:12 - Relations

- **Builds on:** `C.32.HCS`, `A.17`, `A.18`, `C.16`, `C.16.P`, `C.25`, `C.30`, `C.30.P`, `C.31`, `C.31.ASAP`, `E.13`, `E.22`, and `E.23`.
- **Receiving uses:** `C.32.P2S` problem-to-structure architecturing flow, `C.32` candidate synthesis, `C.32.MLAO` multilevel residual work, `C.32.CONWAY` correspondence frames, `C.32.FAIL` repair cues, `C.32.ACE` eval programs, `A.19.CPM` comparison inputs, `A.19.SelectorMechanism` selection inputs, `C.11` local choice inputs, inputs for publishing a selected set under `G.5`, and architecture-decision inputs for `C.32.PAD`.
- **Starter-pack boundary:** Use `C.32.HCS` when the project needs a holon-family starting set before criteria rows exist.
- **Q-Bundle boundary:** Use `C.25` when the architecture characteristic is really a composite quality family with several measures, scope slots, mechanisms, statuses, qualification windows, or evidence.
- **Eval boundary:** Use `C.32.ACE` when a project wants an eval program over declared rows, Q-Bundle slots, candidates, or selected-structure changes.
- **Measurement boundary:** Use `C.16` when a reading, coordinate, unit, threshold, score, or cross-case comparability claim is made.
- **Structural-information boundary:** Use `C.33` or `C.34` when the issue is captured structure, lost structure, or preservation adequacy before a criterion row exists. Use C.32.ACS only when that structural-information or preservation concern becomes a declared architecture-characteristic criterion row. Use `C.35` only as generated-carrier admission support or discovered-carrier admission support before C.32 or ACS receives a criteria-bearing claim.
- **Proxy boundary:** Use `E.13` when an optimization indicator, score, eval result, or dashboard state begins to replace the declared architecture concern.
- **Synthesis boundary:** Use `C.32` after criteria rows exist and the next useful work is to synthesize candidate selected-structure changes.
- **Decision and publication boundary:** Use `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, and `C.32.PAD` when comparison, selection, choice, publication of a selected set, or architecture decision is being made.

### C.32.ACS:13 - Footer marker

C.32.ACS closes when the project can name the starter-pack row or source-catalogue line, draft project criteria rows, optimization indicators, monitored guardrails, context-only rows, bearers, scale forms, current reading or no-reading reason, protected counter-characteristics, receiving uses, and source-return conditions. The next architecture work then belongs to the receiving pattern.

### C.32.ACS:End

