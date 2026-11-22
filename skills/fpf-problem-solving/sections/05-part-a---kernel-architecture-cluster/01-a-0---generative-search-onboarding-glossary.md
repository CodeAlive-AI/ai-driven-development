## A.0 - Generative Search Onboarding Glossary (NQD & E/E‑LOG)

> **Status:** Stable
**Use this when** deciding what a generative search should return, or interpreting a search someone has already run. Start from the decision the recipient has to make. Section 4.3 shows when one usable candidate is enough, when to preserve alternatives or construct a combination, and how to distinguish an exploration report from an exhaustive comparison.

**Builds on.** E.2 (**P‑10 Open‑Ended Evolution; P‑2 Didactic Primacy**), A.5, C.17–C.19 - **Coordinates with.** E.7, E.8, E.10; F.17 (UTS); G.5, G.9–G.12 - **Constrains.** Any pattern/UTS row that **describes a generator, selector, typed portfolio publication, or set-return publication surface**.

**Keywords & queries.** *novelty, quality‑diversity (NQD), explore/exploit (E/E‑LOG), **declared set result**, **typed portfolio publication**, illumination map *(report‑only telemetry)*, parity run, comparability, ReferencePlane, CL^plane, **ParetoOnly** default*

### A.0:1 - Problem Frame

Engineer-managers choosing a search or selection need to distinguish candidate quality, search coverage, explore/exploit policy and the result being returned. Plain definitions provide an entry to these distinctions; the corresponding operation in C.17–C.19 or Part G supplies the method and its conditions.

### A.0:2 - Problem

The following mistakes obscure how a search result was obtained and what it can be used for:

* **Single‑winner bias.** Publishing a winner can take away a choice the recipient intended to make, conceal an efficient alternative or hide the coverage of a search. One eligible candidate with established fitness can finish an order for one workable option.
* **Metric confusion.** “Novelty” and “quality” are used informally; units and scales are omitted; ordinal values are averaged, breaking comparability.
* **Hidden policies.** Explore/exploit budgets and governor rules are implicit; results are irreproducible and **refresh‑unsafe** (no edition/policy pins).
* **Tool lock‑in.** Implementation terms (pipelines, file formats) leak into the Core, violating Guard‑Rails.

This glossary names the generative terms in **Plain** register and ties them to their **formal anchors**, so a publication can distinguish candidate scores, retained sets and selected results.

### A.0:3 - Forces

| Force                         | Tension                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------- |
| **Readability vs Rigor**      | One‑liners for managers ↔ lawful definitions with editions and scale types.     |
| **Creativity vs Assurance**   | Open‑ended search (OEE/QD) ↔ conformance, parity, and publication discipline.   |
| **Comparability vs Locality** | Shared N‑U‑C‑D terms ↔ context‑local CG‑frames and bridges with CL.             |
| **Tool‑agnostic Core**        | Conceptual publication in UTS ↔ engineering teams’ urge to cite specific tools. |

### A.0:4 - Solution - Normative onboarding glossary and publication hooks



#### A.0:4.1 - Plain one‑liners (normative on‑ramp; formal anchors in C.17–C.19)


| Term                      | Plain definition (on‑ramp)                                                                                                                                   | See        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Novelty (N)**           | How unlike the known set a candidate is in your declared **CharacteristicSpace**. Use the declared `DescriptorMapRef` and `DistanceDefRef`, with no ad-hoc normalisation. | C.17, C.18 |
| **Use‑Value (U / ValueGain)** | What the candidate helps you achieve now under your **CG‑Frame**; tie to acceptance/tests; **publish units, scale kind, polarity, ReferencePlane**.                   | C.17, C.18 |
| **Constraint‑Fit (C)**    | *Satisfies must‑constraints (Resource/Risk/Ethics)*; legality via **CG‑Spec**; **unknowns propagate** (never coerce to zero).                                | C.18, G.4  |
| **Diversity_P (declared retained set)** | Coverage or dispersion of the declared retained set under a named measurement policy; declare **ReferencePlane**. Its change on adding one candidate is **DeltaDiversity_P**. | C.17, C.18 |
| **E/E‑LOG**               | *Named, versioned **explore↔exploit** policy*; governs when to widen space vs refine candidates; **policy‑id is published**.                                   | C.19       |
| **ReferencePlane**        | *Where a value lives:* **world** (system), **concept** (definition), **episteme** (about a claim). For a plane relation, retain its source/target planes and basis. Cite **CL^plane** for a used or required calibration and the **Φ_plane** policy and loss model for a used or required loss calculation; any numerical assurance penalty requires an applicable B.3 model. | F.9, G.Core:4.2.3 |
| **Scale Variables (S)** | Ordered settings such as iteration budget, data exposure or resolution. For a scale claim, identify which settings vary, the tasks, the response of interest and the range examined. | C.18.1 |
| **Scale Elasticity (χ)** | A supported response class (*rising*, *knee*, *flat* or *declining*) over the tested settings, or a wider range when a model or bound justifies the extension. Leave the class open when evidence is insufficient. | C.18.1 |
| **BLP (Bitter‑Lesson Preference)** | A preference supported by a comparable, uncertainty-qualified scale comparison; begin with a **cheap scale-claim probe**. **No scale claim yet** or **no scale-based preference** are valid results. A local generality policy is a separate declared basis. | C.19.1, C.24 |
| **Iso‑Scale Parity** | A comparison of candidates at matched resource settings under a justified common basis. To assess change with scale, compare responses at distinct settings. A knee needs at least three ordered settings along one coordinate or specified path, with evidence for the change in slope. | G.9, C.18.1 |

*(Use **LEX‑BUNDLE** for the applicable measurement and scope terminology.)*



#### A.0:4.2 - Publication & telemetry duties (where these terms **show up**)


1. **UTS surface (Part F).** When a **UTS row describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface each glossary value or policy used by the declared operation or independently required by the receiving use. Type each reported value's applicable **units, scale, polarity and ReferencePlane** under **MM‑CHR** and **CG‑Spec**, and cite its defining basis, including `DescriptorMapRef` and `DistanceDefRef` when used or required. *(Row schema: F.17; shipping via G.10.)*
2. **Parity & edition pins (Part G).** When QD/OEE is in scope, **pin the editions and policies used by the operation or required by its receiving use**, including `DescriptorMapRef.edition`, `DistanceDefRef.edition`, the `CharacteristicSpaceRef` with its separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1 and `TransferRulesRef.edition` where applicable; record `PathSliceId` when required by that use. **G.9** supplies the pin requirements for a parity use. Treat **illumination/coverage as report‑only telemetry**; publish an **Illumination Map** where G‑kit mandates parity records. For an empirical claim about how performance changes with scale, declare **S** and use comparison evidence at distinct settings. Reuse an applicable **scale‑probe**. A theoretical prediction states the assumptions and range that support it. **Dominance policy defaults to `ParetoOnly`;** including illumination in dominance **MUST** cite a CAL policy‑id.
3. **Ground generative claims (E.7/E.8).** An architectural pattern claiming generative behaviour **MUST** show which action or conclusion requires the generative claim, who generated or selected the alternatives where this matters, and which conditions and glossary distinctions warrant the conclusion. Use a system or episteme illustration when it reveals a condition of that claim.



#### A.0:4.3 - Putting the glossary to use

1) **Recover the decision before choosing the table.** Who will use the result, by when and with what authority? If they need one workable option, an existing candidate with established fitness may finish the job (C.38). A request for the best option also needs a comparison over the allowed alternatives. If the order calls for new candidates, generate them. For a decision left to the recipient, preserve the alternatives they can identify and use in time. Distinguish who set the goal, proposed the candidates and chose the criteria. When designing the search, make and justify the choices left open. When applying a supplied rule, credit those choices to whoever made them.
2) **Work out which choices have to fit together.** Several recipients may choose independently, need the same option, or need every member of a combination. Compare whole combinations when a shared resource or condition affects their suitability. For one feasible combination, exhibit it or establish its existence as the request requires. To promise support for every allowed joint choice, establish a way for the participants to meet every such request. At each commitment the plan assigns an authorised action to each participant on the information that participant has. It must work in every situation still compatible with that information. The plan can branch on a distinction that reaches the participant in time. A declaration of agreed members needs the agreement. A report of actual use needs evidence of the work.
3) **Choose what to compare or count.** Start with the candidates the commission allows, including ones beyond the current table. When designing a comparison, hold your proposed readings fixed and vary a permitted use or shared condition. If the recipient would have to act differently or give a different justification, retain that distinction or establish how the recipient can learn it in time. Group cases when the same answer and grounds hold (C.39.SA:4). State the eligible population, the question of quality, the admissible units and scales (**CG‑Frame**) and the **ReferencePlane**. Choose the **Q components** or **DescriptorMap** coordinates used by this operation and retain their meanings and applicable editions. Occupied cells describe a retained archive. A claim about which regions were tested needs evidence of the tests, including rejected candidates when they count. To report all nondominated answers, establish completeness for the requested population and distinguish objective values, one realization of each value, and all qualifying candidate identities (C.18:4.4).
4) **Use the method for the requested result.** C.11 governs a local choice. C.18 supplies an archive or front. Use C.19 and record the **E/E‑LOG policy‑id** when the search needs explore/exploit control. Use **G.5** for method-family dispatch or to declare a selected set on an established basis. Keep any consumed `Front` or `Archive` identifiable as the source. Return `Shortlist` or `RankedShortlist` for retained alternatives and `JointUseSet` when all named members are included for one use. A G.5 handoff, abstention or escalation carries its own grounds.
5) **Deliver what the recipient can use.** Keep references to the criteria, evidence and editions used for the result (basis pins). To compare runs on common terms, also record the editions and policies that G.9 requires for that comparison (parity pins). Publish when the receiving use calls for publication, with the applicable **PathIds/PathSliceId**. Add a UTS row for a named governed value when F.17's independent naming and reuse conditions hold. An **Illumination Map** remains **report‑only telemetry** by default.

### A.0:5 - Archetypal Grounding
*Informative; manager‑first (E.7/E.8 Tell‑Show‑Show).*

**Show‑A - SRE capacity plan (selector returns a set).**
*Frame.* The service team will choose how to raise Q4 headroom while meeting its latency commitment. This search is commissioned to keep alternatives available for that later choice.
*Alternatives retained for the team.* `{cache‑expansion, read‑replicas, query‑shaping, circuit‑breaker tuning, schema‑denorm}`. A recommendation to deploy a combination would also have to account for its joint cost and behavior.
*Glossary in action.* `U = latency@p95 & error‑rate`, `C = budget ≤ $X, risk ≤ R`, `N = dissimilarity to current playbook`, `Diversity_P = coverage of the declared retained set under the niche policy`, `DeltaDiversity_P = additional coverage from adding a candidate (e.g., “shifts load to edge” fills an empty niche)`. E/E‑LOG starts **Explore‑heavy**, flips **Exploit‑heavy** once ≥ K distinct niches are lit. *(Publish a UTS row only when **F.17**'s naming and reuse conditions hold; retain parity pins for a parity use; illumination stays report‑only telemetry.)*

**Show‑B - Policy search with QD archive (MAP‑Elites‑class).**
*Frame.* Robotics team explores gaits that trade stability vs energy use.
*Glossary in action.* `CharacteristicSpace = {step‑frequency, lateral‑stability}`, `ArchiveConfig = CVT grid`, `N` from descriptor distance, `U` = task reward, `Diversity_P` = coverage of the retained gait set under the declared grid policy; **PortfolioMode=Archive**. Families include **MAP‑Elites (2015)**, **CMA‑ME/MAE (2020–)**, **Differentiable QD/MEGA (2022–)**, **QDax (2024)**; publish editions and policy‑ids; treat illumination as **report‑only telemetry**.

*(Optional)* **Show‑C - OEE parity (POET/Enhanced‑POET).**
Co‑evolve declared `{environment, method}` sets; publish **coverage/regret** as telemetry metrics; pin `TransferRulesRef.edition`; return *sets*, not a single winner.

**Show‑Epi - Evidence synthesis (U.Episteme).**
*Frame.* A living review compares rival **causal identification** methods (e.g., IV vs. DiD vs. RCT‑adjacent surrogates) across policy domains.
*Glossary in action.* `U = external‑validity gain @ F/G‑declared lanes`, `C = ethics & data‑licence constraints`, `N = dissimilarity in **ClaimGraph** transformations`, `D_P = coverage of identification niches in the archive`. `ReferencePlane = episteme`. Illumination/coverage stays **report‑only telemetry**; selection retains alternative methods as an unranked `Shortlist`, with the relevant identification niches stated for each method. When the receiving use calls for publication, publish a typed portfolio view of that result. *(Publish UTS rows only when **F.17**'s naming and reuse conditions hold; cite obtaining Bridges for cross‑domain semantic correspondence, with calibration and loss‑model pins when used or required under **G.Core:4.2.3**; edition‑pin the Descriptor/Distance defs used or required by the QD use.)*

### A.0:6 - Bias-Annotation

**Scope.** Trans‑disciplinary; glossary applies to work concerning both **Systems** and **Epistemes**.
**Known risks & mitigations.**
*Over‑aggregation:* forbid mixed‑scale sums; use **CG‑frame** and **MM‑CHR**.
*Terminology drift:* enforce **LEX‑BUNDLE** registers; ban tool jargon in Core.
*Optimization monoculture:* require declared set-result or typed portfolio publication where G‑kit mandates parity; illumination stays **report‑only telemetry** unless a CAL policy promotes it (policy‑id cited).

### A.0:7 - Conformance Checklist (SCR/RSCR stubs)

| ID          | Requirement                                                                                                                                                                               | Purpose                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **CC‑A0‑1** | If a pattern/UTS row **describes a generator, selector, typed portfolio publication, or set-return publication surface**, it **MUST** surface the glossary values and policies used by its operation or independently required by the receiving use, with their applicable **units, scale, polarity, ReferencePlane and policy‑ids**. | Makes generative claims comparable and auditable (UTS as publication surface). |
| **CC‑A0‑2** | For QD/OEE, **pin** the editions and policy‑ids used by the operation or required by the receiving use, including `DescriptorMapRef.edition`, `DistanceDefRef.edition`, the `CharacteristicSpaceRef` with its separate `characteristicSpaceDescriptionRef: U.EpistemeRef` under A.19:5.1.1.1 and `TransferRulesRef.edition` where applicable. Log `PathSliceId` when required; follow **G.9**'s pin requirements for a parity use. | Enables admissible parity and refresh; edition-aware telemetry. |
| **CC‑A0‑3** | **No mixed‑scale roll‑ups**; ordinal data **SHALL NOT** be averaged; any roll‑up **MUST** live under a declared **CG‑frame**.                                                             | Prevents illegal scoring; keeps comparisons lawful.                             |
| **CC‑A0‑4** | Where the G‑kit requires parity, **publish an Illumination Map** (coverage per niche); **single‑number leaderboards are non‑conformant** on the Core surface when a ParityReport is required. | Declared-set-first / typed portfolio-publication posture; avoids single‑winner bias.                         |
| **CC‑A0‑5** | Keep **illumination/coverage** as **report‑only telemetry**; **dominance policy defaults to `ParetoOnly`**; any change is CAL‑authorised and cited by policy‑id.                                          | Separates fit from exploration; preserves auditability.                         |
| **CC‑A0‑6** | Apply **E.7/E.8**: include a **U.System** and a **U.Episteme** illustration when claiming generative behaviour; obey **E.10** register hygiene; use the subsection title **“Archetypal Grounding.”** | Locks didactic primacy; prevents jargon drift.                                  |
| **CC-A0-7** | **ReferencePlane declared** for every reported N/U/C/Diversity_P head. For a plane relation, retain its source/target planes and basis under **G.Core:4.2.3**; cite **CL^plane** for a used or required calibration and the **Φ_plane** policy and loss model for a used or required loss calculation. Numerical assurance penalties follow an applicable B.3 model. | Prevents plane/stance category errors while preserving applicable crossing and receiving-use grounds. |
| **CC‑A0‑8** | **Diversity_P ≠ Illumination.** Diversity_P measures the retained set; DeltaDiversity_P measures a candidate's marginal contribution to it. Either requires a declared `PromotionPolicy` before entering dominance. **Illumination** remains **report‑only telemetry** unless explicitly promoted by a CAL-authorized policy-id.                                         | Matches QD triad semantics and parity defaults.                                 |
| **CC‑A0‑9** | For a generator or selector scale-behaviour claim, declare the scale variables **S** and the settings or range the claim covers. Cite the **E/E-LOG scale policy-id** when the claim or its use depends on a policy, for example a knee threshold or selection by class. A prediction from a model states the assumptions of the derivation. Mark **S = N/A** when no scale-behaviour claim is made. | Identifies what varies and the grounds for the asserted response. |
| **CC‑A0‑10** | For an empirical scale-behaviour claim, identify the compared settings, response, conditions and uncertainty. Use an applicable probe or obtain the missing evidence when the claim is needed. Report the class supported under **C.18.1**. With only one setting, report the result there and leave the trend open. Use a UTS row when **F.17** calls for one. | Makes the grounds for the scale claim recoverable, including when classification remains open. |
| **CC‑A0‑11** | Apply **Iso‑Scale Parity** in parity runs when S is declared; where infeasible, state the **loss notes** and treat results as **non‑parity**. For a penalty calculated or required by the receiving use, cite its model and policy; numerical assurance penalties require an applicable B.3 model. | Keeps comparisons fair and auditable under scale constraints. |
| **CC‑A0‑12** | Record a **BLP-waiver** only when overriding a declared generality preference that would otherwise decide the use. Apply **C.19.1**'s governed grounds: admissibility override, parity-supported scale-probe overturn, or non-blocking complementary bias. Bounded specialization alone requires no waiver. | Makes a policy override transparent without imposing one on ordinary bounded tactics. |

### A.0:8 - Consequences

**Benefits.**
- Plain definitions tied to the formal anchors needed for use and checking.
- Distinct names for retained sets and selector outcomes, with their metric and policy meanings.
- Explicit edition and policy basis for checking comparability and refreshing affected results.

**Trade‑offs & mitigations.**
- Slightly longer UTS rows → mitigated by consistent schema and copy‑paste snippets.
- Requires discipline on units and scales → mitigated by CG‑frame templates.

### A.0:9 - Rationale

Quality-diversity and open-ended search require both candidate comparison and retention of useful search coverage. This glossary makes those purposes distinguishable in an operation and its published results, supporting **P‑10 Open‑Ended Evolution**. Plain definitions follow **Didactic Primacy (P‑2)** and **LEX‑BUNDLE (E.10)**; references to C.17–C.19 retain the metric and policy definitions under **Patterns Layering (P‑5)**. The examples in section 5 show how these distinctions apply to search without prescribing a particular tool.

### A.0:10 - Relations

**Builds on.** **E.2 Pillars** (P-10, P-2, P-6), **A.5** (Open-Ended Kernel), **B.5/B.5.2.1** (Abductive loops + NQD integration), **C.17–C.19** (Creativity-CHR, open-ended search archive/front stewardship, E/E-LOG).

**Coordinates with.** **E.7/E.8** (Archetypal Grounding; Authoring template), **E.10** (LEX‑BUNDLE), **F.17** (UTS), **G.5/G.9–G.12** (set‑returning selectors, **iso‑scale** parity, shipping & refresh).
**Constrains.** Any generator/selector/typed portfolio publication on the Core surface: the **glossary values, policies and basis pins used by its operation or required by its receiving use; lawful scales; S/Scale‑probe for scale claims; parity pins for parity use; declared-set publication where mandated**. (Ties into UTS rows and parity records.)
For agentic orchestration of scalable tool‑calls under **BLP**/**SLL**, see **C.24 (Agent‑Tools‑CAL)**.

### A.0:QF.0a - Scope of this glossary

Use C.17–C.19 for the corresponding metrics and search policies. This glossary connects their terminology to the selected operation and its publication or telemetry requirements.

### A.0:QF.1 - Early set-result and metric-kind vocabulary

- Use `Palette` for a plurality-preserving set with no dominance semantics yet.
- Use `TraditionPalette` only when the members are traditions gathered before later comparison or choice semantics are declared.
- For methods, hypotheses, environment-method pairs, candidate explanations, or other member kinds, use `Palette` plus explicit `SubjectKind` instead of borrowing the `TraditionPalette` head.
- Use `Front` for nondominated candidates over an identified population under the declared `DominanceSet`. A report of the objective values they realize or one representative per value can merge distinct candidates (C.18:4.4).
- Use `Q-Front` when the declared `DominanceSet` is the declared `Q` components.
- Use `Archive` for a retained set whose purpose is coverage, stepping-stone retention, or frontier expansion rather than current non-domination.
- Use `ExplorationArchive` for the broad retained exploration surface; it is the exploration-specific specialization of `Archive`.
- Use `SteppingStoneSet` only for one narrower retained subset whose stated purpose is future frontier reach rather than the whole archive. It is not part of the ordinary first-pass public-head family for retained exploration.
- Use `Shortlist` for the set chosen from one declared source set by one named lens.
- Use `RankedShortlist` only when that shortlist is explicitly rank-ordered.
- Use `JointUseSet` when every named member is designated for one use. Give that use, keyed members, inclusion conditions and basis pins under G.5. Ground a claim of joint feasibility or actual use in the conditions or Work that establish it.
- Use `ShortlistId` for the stable public token of one emitted shortlist; it is not the shortlist itself.
- Use `ChoiceSet` only when the mathematical set object underlying one shortlist must be named explicitly; do not let it replace the public shortlist head.
- Use `Q-set` for the declared current objective tuple that may ground the current `DominanceSet`.
- For a result or claim used by a pool policy, retain its direct pattern's reference name and kind; for example, `A.2.2` supplies `capabilityHolderRef` and `capabilityStatementRef`. Use `C.19` for the resulting pool treatment. Citing an input does not add it to `Q` or dominance.
- Use `competenceModelRef` under `C.19` only for one model episteme used by the policy; identify the capability and supporting results separately.
- When the pool treatment relies on an evidence-bearing or source-bearing claim, use `a10RelianceRef` for the claim and bounded pool-treatment reliance under `A.10`.
- Use `goalSpaceExpansionPolicyRef` under `C.19` when an independently declared archive or curriculum expansion policy governs goal- or task-space growth; that policy does not place a candidate on a front or add a dominance coordinate.
- When future reach depends on a transition or transfer relation, cite its direct rule and supporting result references together with any model episteme used. Keep their use in archive/pool policy separate from any explicitly authorized promotion into dominance.
- If one front is meant to be current-`Q` by default, say so as `Q-Front` or as `Front over the declared Q components` rather than leaving the relation between `Q-set` and `DominanceSet` implicit.
- `Use-Value` may be one member of the `Q-set` only when the current Context declares it there; it is not the whole `Q-set` or the default `Q-set` by itself.
- Metric-kind doctrine: the `Q-set` is the candidate/front-facing objective tuple; `Novelty@context` is one context-relative candidate signal; `DeltaDiversity_P` is one set-relative marginal diversity contribution; `IlluminationSummary` is one report-only archive telemetry summary unless one explicit policy promotes it.
- Minimal mathematical lens: the current front lives in one declared comparison or outcome space, while the exploration archive may depend on one declared search, niche, or reachability space. Keep both spaces explicit when they differ.
- Keep `Novelty@context`, `DeltaDiversity_P`, `Surprise`, and `IlluminationSummary` outside the default `Q-set` unless one declared `PromotionPolicy` says otherwise.
- A reader should be able to tell whether one sentence is talking about a `Palette`, a `Front`, an `Archive`, a `SteppingStoneSet`, a `Shortlist`, a `RankedShortlist`, or a `JointUseSet`, and whether one selected set came from one declared source set, before later policy or geometry detail arrives.
- Use `portfolio` only when the portfolio or set-result field is a declared retained set plus a selection/retention rule or a portfolio-publication posture. Do not use bare `portfolio` when `Palette`, `Front`, `Archive`, `SteppingStoneSet`, `Shortlist`, or `RankedShortlist` is already recoverable.

### A.0:QF.1a - Helper declarations for set-result language

- Ordinary public set-result family heads are `Palette`, `TraditionPalette`, `Front`, `Q-Front`, `Archive`, `ExplorationArchive`, `Shortlist`, `RankedShortlist`, and `JointUseSet`; the applicable pattern fixes which families its operation may return.
- `SteppingStoneSet` is one narrow retained-subset head only when that subset itself is the visible published surface; do not treat it as the ordinary public head for retained exploration.
- `SetResultFamily` is a declaration field naming which public set-result family is being emitted; it is not another public head.
- `SourceSetFamily` is a declaration field naming the immediate source-set family acted on by a lens, such as `Q-Front`, `ExplorationArchive`, `Front`, `Archive`, or `TraditionPalette`; it does not specify derivation, composition, or object identifiers, and it does not rename the emitted result.
- `SourceSetComposition` is an optional declaration field for a composition of several declared source sets, including different sets of the same family. Identify each contributing set and its family, and state how its members contribute, such as `Front+Archive` through a union when that is the construction. It is not itself a kind.
- `SubjectKind` is a declaration field naming what the members are, such as traditions, methods, hypotheses, environment-method pairs, candidate explanations, or other subject-kinded alternatives.
- `EligibilitySet`, `DominanceSet`, `TieBreakerSet`, and `TelemetrySet` are the comparison-bundle sets behind the published set result, not rival publication heads: `EligibilitySet` says what may enter, `DominanceSet` says what counts for current non-domination, `TieBreakerSet` says what may order or choose among survivors, and `TelemetrySet` says what may be reported without changing dominance.
- `PromotionPolicy` is the policy pin that authorizes one tie-breaker or telemetry signal to move into dominance. Without that pin, novelty, diversity, surprise, illumination, or similar signals remain outside the current `DominanceSet`.
- `DerivedViewKind` is an optional declaration field for a derived view, such as one tradition view used for interpretation or publication. It must leave the base `SourceSetFamily`, `SetResultFamily`, and emitted shortlist family recoverable.
- `BasePaletteRef` is an optional cited id/ref for the base palette when one derived tradition view or shortlist depends on that palette; it is a ref, not a kind.
- Stable values for `SetResultFamily`, `SourceSetFamily`, `SourceSetComposition`, `SubjectKind`, and `DerivedViewKind` should come from controlled tokens, cited ids, or already-declared head labels; do not let one ad hoc local prose label become a de facto field value.
- When the upstream object is `SoTAPaletteDescription` and its members are traditions, `TraditionPalette` may be used as the reader-facing tradition-only alias for that same palette declaration. When the members are not traditions, keep `SoTAPaletteDescription` or `Palette + SubjectKind` explicit instead of widening `TraditionPalette`.
- `RetentionIntent=steppingStone` is a field value on retained archive membership intended for future frontier reach. A `SteppingStoneSet` names a narrower retained subset only when that subset itself is the published set result being discussed; the ordinary archive head names the whole archive.

### A.0:QF.2 - First public wording for shortlisted results

- When a reader needs the visible selected set, say `Shortlist from <SourceSetFamily> under <LensId>`.
- When the selected set must be cited as one stable emitted object, say `ShortlistId` and keep one nearby line that names the shortlist and its source set.
- When the shortlist is ordered, say `RankedShortlist` and keep the underlying shortlisted set result recoverable rather than jumping straight from `Front` to ranking.
- Use `choice set underlying that shortlist` only when the mathematical set object itself is the point of the sentence.
- A reader should be able to recover on first pass what source set was acted on, what shortlist came out, and whether the text is naming the published set result, the token, or the mathematical set object.

### A.0:QF.2a - Set/space reading glosses

The set/space terms have the following meanings:

- `SearchSpaceRef`
  - a declared reference to the `CharacteristicSpace` currently used to search, compare, or navigate candidate possibilities
  - a role-named ref field using the existing `CharacteristicSpaceRef` / `SpaceRef` idiom; it introduces no new space kind
- `OutcomeSpaceRef`
  - a declared reference to the `CharacteristicSpace` currently used to judge outcomes, effects, or realized value
  - a role-named ref field using that same idiom; it is not a synonym for `SearchSpaceRef`
- `DeclaredSubstrateInterpretiveView`
  - the common head of an optional interpretive-view family over an already-declared substrate-bearing line, a source set, or a set result whose substrate remains recoverable
  - it helps the reader see the current inspection question; it does not replace the base source set or introduce a new substrate
- `DeclaredSubstrateAtlasView`
  - an optional interpretive view that shows how several declared views, spaces, mappings or qualifications relate within the same substrate
  - use it only when the current reading needs that composite interpretation, and say why a simpler interpretation is not enough; it is not the default meaning of palette, front, archive, shortlist, or candidate set
- `TypedSetViews`
  - a list of the declared set-view heads that the current atlas/support reading holds together
  - use it when several declared views must stay visible together; it does not create a new set result and should not hide the active source set or active set result
- `OutcomeMapRef`
  - a map reference showing how a declared source or set result bears on a declared outcome-side or effect-side space when that map materially affects the interpretation
  - it qualifies the reading; the source set and the outcome-side declared space or reference remain distinct
- `SpaceMetricRef`
  - a metric-ref qualifier for the metric, neighborhood, distance, density, or reachability discipline used inside a declared space
  - it qualifies how positions in that space are compared; it is not the space itself or a substitute for `SearchSpaceRef` or `OutcomeSpaceRef`
- `TransitionRelationRef`
  - a transition-ref qualifier for the transition, cross-scale state-change, dynamic-coupling, or phase-change basis on which the reading depends
  - it explains why motion or cross-scale state change is read a certain way; it does not by itself decide policy, planning, or publication
- `BridgeDistortionNote`
  - a note describing fidelity limits in a useful bridge, projection, aggregation, or derived reading
  - it identifies where comparison is distorted or information is lost, so claims of bridging, substitution, or reliance stay within the stated limits

### A.0:QF.2b - Practitioner-facing reading cue

- If the question is “Which space are we searching or navigating?”, look for `SearchSpaceRef`.
- If the question is “Which space are we judging outcomes in?”, look for `OutcomeSpaceRef`.
- If the question is “What optional overlay helps me read several declared views or set results together?”, look for `DeclaredSubstrateInterpretiveView`.
- Use `DeclaredSubstrateAtlasView` when answering the named inspection question requires showing how several declared views, spaces, mappings or qualifications relate within the same substrate.
- If the atlas/support reading must keep several declared set views visible at once, look for `TypedSetViews`.
- If the overlay depends on one explicit source-to-outcome mapping, look for `OutcomeMapRef`.
- If the overlay depends on one metric, neighborhood, or reachability discipline inside one declared space, look for `SpaceMetricRef`.
- If the overlay depends on one transition, cross-scale state-change, or dynamic-coupling basis, look for `TransitionRelationRef`.
- If the overlay depends on one bridge or projection that may lose fidelity, look for `BridgeDistortionNote`.

### A.0:QF.2c - First-use classification check

- Start with `DeclaredSubstrateInterpretiveView` when the NQD/OEE task is simply to keep one declared palette, front, shortlist, or archive readable while comparing candidate material.
- Start with it only when any cited `SearchSpaceRef`, `OutcomeSpaceRef`, mappings, or qualifiers are already declared elsewhere and remain recoverable through the base substrate, source set, or set result.
- Escalate to `DeclaredSubstrateAtlasView` only when one named `InspectionQuestion` about the same declared substrate requires reading several declared views, spaces, mappings, or qualifiers together. State what their joint reading contributes to that question and why a simpler interpretation is insufficient; use `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` for the declaration.
- If the reading keeps several declared set views together, name `TypedSetViews` explicitly.
- If the reading depends on one source-to-outcome map, name `OutcomeMapRef` explicitly.
- If the reading depends on one metric or neighborhood discipline, name `SpaceMetricRef` explicitly.
- If the reading depends on one transition, cross-scale state-change, or dynamic-coupling basis, name `TransitionRelationRef` explicitly.
- Creating a search doctrine, an outcome metric family, or a publication surface lies outside this interpretive-view guidance; use the object's governing patterns for those decisions.

### A.0:End

---
