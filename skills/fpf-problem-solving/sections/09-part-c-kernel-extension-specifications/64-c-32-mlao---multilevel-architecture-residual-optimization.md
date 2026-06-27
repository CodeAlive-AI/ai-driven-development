## C.32.MLAO - Multilevel Architecture Residual Optimization

> **Type:** Architectural subpattern under C.32
> **Status:** Draft
> **Normativity:** Normative unless explicitly marked informative

### C.32.MLAO:1 - Problem frame

Use this pattern when a practitioner has a recoverable cross-scope or interlevel architecture residual and needs candidate architecture changes that reduce that residual under a declared evolution window.

Primary working reader: an architect or architecture-responsible practitioner who has already recovered a residual and must prepare candidate changes without calling a local improvement a whole-holon optimum.

Typical entry phrases:

```text
"The local architecture improvement made another scope worse."
"The platform helps product teams but grows evidence exceptions."
"Local agent autonomy conflicts with the control or policy scope."
"The method template speeds authoring and slows review."
"A graph, residual vector, or Pareto front can inform comparison only after selected structures, residuals, losses, and the receiving pattern are declared; it is not the architecture."
```

**First-minute use slice.** A regulated product-family team has used `C.30.ILC` to name a residual: local product variants are quicker to ship, but certification evidence grows at the family scope. Using C.32.MLAO, the practitioner frames three residual-reducing candidate changes: add evidence scope, narrow interface grammar, or accept a bounded exception with a reopen trigger. Each candidate states the residual it reduces and the new burden it creates. The team now has explicit inputs for `A.19.CPM`, `C.11`, `A.19.SelectorMechanism`, or `G.5` when comparison, local choice, selection, or publication of a selected set is current.

The primary `EntityOfConcern` is a residual-reducing candidate frame for one grounded architecture question. In plain working terms, the frame asks where a local architecture improvement moved the cost and which candidate can reduce that moved cost without hiding its new burden. The described holon can be a system, organization, method family, discipline, cultural practice, evidence-bearing practice, AI-agent setup, built asset, or another admitted holon kind. A publication family may appear only when it is the described holon or selected structure under its own governing pattern; publication-face use stays with `E.17` or `E.24.PUB`. C.32.MLAO is not a universal optimizer, adequacy claim, selector, decision, assurance argument, publication pattern, or software-system-only pattern.

What goes wrong if C.32.MLAO is missed: local success is called whole-holon architecture success, or an optimization phrase hides the residual that shifted to another declared holon-level ref or declared scope ref.

What C.32.MLAO buys in practice: the practitioner can prepare residual-reducing architecture candidates for later comparison by naming residual reduced, new burden created, affected scope, preserved structure, lost structure, and source-return condition.

Ordinary working move: name where the local improvement moved the cost, name the selected structure and scope that now carry the residual, then prepare candidate changes that reduce that residual while making the new burden explicit.

Adoption test: after using C.32.MLAO, a reader can see the residual reduced, the new burden, the affected scope, the preserved structure, the lost structure, and the evolution-window stop condition for each candidate.

Use C.32.MLAO only after residual triage. Do not use it to recover the residual itself, justify a mathematical lens, compare or select candidates, choose locally, publish a selected set, or decide the project architecture.

Common exits by claim kind:

- `C.30.ILC` when the residual is not recoverable yet.
- `C.32.ACS` when architecture-characteristic criteria rows are missing.
- `C.32.ACE` when eval programs or eval results are the current claim.
- `C.29` when mathematical-lens use is being claimed.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for publication of a selected set.
- `C.18` and `C.19` for archive, front, pool treatment, or stepping-stone retention.
- `C.30.AD`, `E.17`, and `E.24.PUB` for architecture-description or publication-face work.
- `C.32.PAD` for project decision.

The first useful output is `MultilevelArchitectureResidualOptimizationFrame@Project`. The frame is the project working record for residual-reducing candidate framing. It records residual movement and candidate burdens; it is not a universal optimizer, scalar optimum, C.29 lens result, or architecture decision:

For a first pass, fill only the described holon, bounded context, residual-triage ref, affected level or scope refs, selected structures, residual-bearing loci, criteria rows, evolution window, residual-reducing candidates with residual reduced and new burden, receiving pattern, and stop condition. Add front, archive, NQD, OEE, C.29 lens, ideality, scale-amenability, function-bearer, and transformer-transformed refs only when that support is current for the candidate being framed.

```text
MultilevelArchitectureResidualOptimizationFrame@Project:
  describedHolonRef:
  boundedContextRef:
  residualTriageRef:
  declaredHolonLevelRefs?:
  declaredScopeRefs:
  selectedStructureRefs:
  residualBearingLoci:
  candidatePaletteRef:
  architectureCharacteristicCriteriaSetRef?:
  architectureCharacteristicCriteriaRowRefs:
  qBundleRefs?:
  evolutionWindowRef:
  dynamicFrontOrArchiveRef?:
  nqdOrOeeSupportRef?:
  steppingStoneRefs?:
  architectureIdealityPressureRef?:
  scaleAmenabilityPolicyRef?:
  functionBearerFeasibilityRef?:
  transformerTransformedCorrespondenceRef?:
  residualReducingCandidates:
    - candidateRef:
      selectedStructureChanged:
      affectedLevelOrScope:
      affectedArchitectureCharacteristicRefs:
      affectedCriteriaRowRefs?:
      architectureCharacteristicEvalResultRefs?:
      residualReduced:
      newBurden:
      preservedStructure:
      lostOrHiddenStructure:
      sourceReturnCondition:
  comparisonInputRefs?:
  receivingOperationPatternRef?:
  c29LensOutputRef?:
  metaHolonTransitionRef?:
  stopCondition:
```

### C.32.MLAO:2 - Problem

Many architecture problems are residual problems. A local module boundary improves one team and creates integration exceptions elsewhere. A control relation improves response and creates audit or timing burden. A platform improves reuse and creates evidence decay. A method family speeds authoring and harms transfer.

The tempting shortcut is to call the local improvement optimized. C.32.MLAO blocks that shortcut by asking: where did the residual shift, which selected structure carries it, and which candidate change reduces it enough to be worth its new burden?

### C.32.MLAO:3 - Forces

| Force | Tension |
|---|---|
| Local fit | A candidate may help one scope while harming another. |
| Optimization language | Objective, residual, front, and matrix language sounds decisive before the claim is typed. |
| Declared-level recognition | Level and scope words are useful only after they are declared as holon-level refs or scope refs, or restored as stratification terms through `C.30.STRAT` before selected-structure use. |
| Candidate action | Residual triage must turn into candidate changes when repair work is being performed. |
| New burden | Every residual-reducing candidate change creates another cost or loss. |

### C.32.MLAO:4 - Solution

Build a residual-reducing frame around one recoverable residual. The frame is not a universal optimization target and not a scalar optimization result.

Work in eight steps:

1. Start from a `C.30.ILC`-compatible residual triage.
2. Name the affected declared holon-level refs or declared scope refs and the selected structures that carry the residual.
3. Name the architecture-characteristic criteria rows and any Q-Bundle slots that make the residual worth reducing.
4. Create or reference a C.32 candidate palette.
5. For each candidate, state the residual it reduces, the selected structure changed, and the criteria rows affected.
6. State the new burden, loss, exception, or source-return load created by that candidate.
7. Record the evolution window and whether any NQD, OEE, archive, front, stepping-stone, ideality, or BLP support is only keeping candidate plurality or directionality alive.
8. Stop at the frame, or name the receiving pattern when a later claim is being made: explicit comparison belongs to `A.19.CPM`, set-returning selection to `A.19.SelectorMechanism`, publication of a selected set to `G.5`, local choice to `C.11`, architecture decision to `C.32.PAD`, architecture-description work to `C.30.AD`, publication-face work to `E.17` or `E.24.PUB`, and mathematical-lens use to `C.29`.

Admit a residual-reducing candidate only when it answers the working questions: which declared holon-level ref or declared scope ref is affected, which selected structure changes, which architecture-characteristic row or Q-Bundle slot is at stake, what residual is reduced, what structure is preserved or lost, and what new burden appears.

| Candidate change family | Use when | Repair it provides |
|---|---|---|
| `splitScope` | One scope carries incompatible tempo, functional demand, constraint, or admissibility condition. | Separates the conflict and names coordination cost. |
| `mergeScope` | Mediation creates more burden than separation saves. | Removes unnecessary boundary and names coupling risk. |
| `addMediator` | Direct cross-scope dependency is brittle. | Adds mediation and names mediator failure mode. |
| `addControlStructure` | Rate, feedback, policy, or supervisor conflict persists. | Makes control responsibility explicit and names timing or accountability burden. |
| `addInterfaceGrammar` | Variation grows through unmanaged interface variants. | Names allowed variation, conformance expectation, and exception risk. |
| `repairFunctionBearerGap` | A residual-reducing functional change has no feasible bearer at the affected declared holon-level ref or declared scope ref. | Adds or changes bearer, splits function, changes placement or resource access, changes control responsibility, or rejects the candidate. |
| `addEvidenceScope` | Reusable candidate bearer lacks reusable evidence scope. | Makes evidence maintenance part of the candidate; A.10 evidence-relation validity or sufficiency claims belong to `A.10` when they are current. |
| `addWorkMethodScope` | Repeated work remains bespoke because method structure is missing. | Transfers repeated work into method structure and names review or training burden. |
| `repairTransformerTransformedCorrespondence` | The residual is carried by mismatch between a changing holon's architecture and the architecture of the holon being changed. | Opens `C.32.CONWAY`; prepares candidate alternatives that change the transformer side, change the transformed side, change both, or keep a bounded mismatch. |
| `acceptBoundedException` | Eliminating the residual costs too much now. | Records exception, source-return condition, and reopen trigger. |

**Comparison-input boundary.** C.32.MLAO prepares comparison inputs; it does not run the comparison or choose a candidate. Its output rows are candidate records with residual reduced, new burden, selected structures, preserved structure, lost structure, source-return condition, and optional C.29 lens-output references.

Those references are diagnostic inputs only.

Admitted profiles and a `ComparatorSpec` belong to the receiving explicit-comparison pattern.

If the current claim is explicit comparison, use `A.19.CPM` with admitted profiles and a declared `ComparatorSpec`. If the claim is local choice over an existing option set, use `C.11`. If the claim is set-returning selection, use `A.19.SelectorMechanism`. If the claim is publication of a selected set, use `G.5`.

**Lens-output discipline.** Graphs, fronts, residual vectors, DSMs, RG-like descriptions, and frustration language are C.29 lens outputs, structural descriptions, or diagnostic signals after their architecture use is typed. The real failure is proxy preference: a candidate is preferred because the output looks better while selected structures, lost structure, architecture characteristics, and receiving pattern remain unnamed. The repair is to interpret the output over selected structures and state what residual or loss it exposes; any comparison, selection, or choice claim then belongs to its receiving pattern.

**Method, culture, and episteme discipline.** Method-family, cultural-practice, and episteme-mediated cases are admitted when the described holon and selected structures are recoverable. If a publication family or publication face is in view, recover whether it is a described holon, a selected structure, an architecture description, or an MVPK face before using it. C.32.MLAO governs only the residual-reducing architecture candidate frame; method, work, publication, evidence, ethical, and decision claims use their governing patterns when current.

**Dynamic candidate discipline.** A preferred or retained candidate is bounded by an evolution window, source conditions, and the receiving pattern that admitted the preference or retention. NQD, OEE, C.18, and C.19 can keep a front, archive, pool, or stepping stone visible; they do not select the architecture and they do not turn a front member into a durable optimum.

**Ideality and BLP discipline.** TRIZ ideality can suggest residual-reducing candidate changes: remove a support bearer, transfer a useful function onto an existing resource, or generalize a bearer so fewer selected structures carry more useful functions. BLP can prefer a more general scale-amenable bearer only inside its declared scale window and audit boundary. Both lines guide candidate generation; neither removes the need to state new burden, lost structure, and receiving pattern.

**Functional-bearer feasibility discipline.** A residual-reducing functional change is not admissible until the function has a bearer under the module, placement, resource, control, information, and evidence constraints declared for the case. If no bearer exists, the residual-reducing candidate must add a bearer, split the function, change placement or resource access, change control responsibility, reduce the demand, or return to C.32 as an unfit candidate.

**Transformer and transformed holon discipline.** When the residual is created by a holon that changes another holon, use `C.32.CONWAY`. Keep the transformer architecture and transformed-holon architecture distinct; then prepare residual-reducing candidates that change the transformer side, the transformed side, both sides, or a bounded mismatch as comparison inputs or downstream candidate alternatives. Transformation, flow, work, and module-interface claims belong to `A.3.4`, `E.18`, `A.15`, or `A.6.M` when current. Structural-similarity claims belong to `C.29` only when they are current.

**Level, stratification-term, and whole-reidentification discipline.** If the case uses `level`, `system level`, `holon level`, `layer`, `tier`, or another stratification term, first use `E.10.ARCH` and `C.30.STRAT` unless the direct governing pattern and recovered neighborhood are already named by value. If the case uses `BOSC`, `MHT`, `MET`, `MFT`, emergence-family, boundary-crossing, or promotion-like wording, first use `E.10` and `B.2.P` to recover the claim kind. Use `B.2` only when a whole-reidentification question remains after the existing-whole explanation check; otherwise use the direct governing pattern for architecture, boundary, capability, function, measurement, publication, work, or lens claims.

**Stop condition.** Stop after the frame names residual, affected declared holon-level refs or declared scope refs, candidate changes, new burdens, preserved and lost structure, source-return conditions, and receiving patterns.

**Lowering condition.** Keep the frame as C.32.MLAO work only while the residual triage, affected level or scope refs, selected structures, criteria rows, evolution window, residual reduced, new burden, and receiving pattern remain current. Lower a candidate to a diagnostic note when the residual is not recoverable, the selected structure is unknown or stale, the architecture characteristic is missing, the new burden is not named, or the receiving pattern cannot use the row. Retire a candidate when its evolution window closes or a stronger residual triage replaces it. Return to `C.30.ILC` when the residual itself is missing, to `C.32.ACS` when criteria rows are missing, to `C.32.ACE` when eval results are needed but not current, to `C.29` when the current claim is a mathematical-lens claim, and to `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, or `C.32.PAD` when the downstream claim is current.

### C.32.MLAO:5 - Worked Residual Cases

| Grounded working case | Residual-bearing locus | Residual-reducing candidates | Stop condition |
|---|---|---|---|
| Regulated product family where shared platform reduces engineering work but grows certification exceptions | Product-variant scope against family evidence scope; module-interface and evidence-scope structures | Add reusable evidence scope; narrow interface grammar; keep bounded exception for one variant | Stop before assurance, G.5 publication of a selected set, or decision unless those claims are current. |
| Clinical triage practice where local intake speed increases downstream escalation misses | Intake scope against hospital escalation scope; role-enactor and procedural-work structures | Add mediator role; split triage scope by patient class; change escalation responsibility | Stop before ethical mediation or staffing decision unless `D.3`, `D.4`, or the receiving staffing-decision pattern is current. |
| AI-agent review setup where local agent quality improves while policy violations increase | Agent task scope against policy-control scope; control and evidence-refresh structures | Add supervisor relation; narrow model-interface admissibility; change evidence refresh cadence | Stop before safety, gate, release, or causal claims unless their governing patterns are current. |
| ML inference workflow where the searched functional graph improves quality and exceeds edge-device resource limits | Functional graph against deployment and resource scopes; module-interface, placement, and resource structures | Split the function, change deployment placement, add a resource bearer, or reject the candidate for this evolution window | Stop before release, benchmark, or G.5 publication claims unless their governing patterns are current. |
| Method family where template reuse accelerates authoring and creates review residue | Authoring scope against review scope; method-structure and authored-section structures | Split method variants; add review-evidence scope; accept bounded local method residue | Stop before method governance, MVPK publication-face governance, or project decision unless the receiving pattern is current. |
| Built-asset maintenance program where digital-twin abstraction hides lower-scope source loss | Asset-family scope against maintenance-work scope; reference-designation, information, and work-method structures | Add source-return scope; split information view; retarget maintenance responsibility | Stop before built-asset architecture-description, publication-face, or A.10 evidence-relation claims unless their governing patterns are current. |

### C.32.MLAO:6 - Residual And Trade-Off Failure Modes

| Failure mode | C.32.MLAO repair action |
|---|---|
| **Local improvement shifts the residual elsewhere** | Record the scope and selected structure that improved, the scope and selected structure that worsened, and the new burden created. |
| **Universal optimizer is assumed** | Treat optimization as bounded residual reduction over declared holon-level refs or declared scope refs, with comparison inputs, receiving pattern, and stop condition. |
| **Proxy result substitutes for comparison or choice claim** | When a score, vector, graph partition, front, DSM, or C.29 lens output is used to prefer a candidate, name the selected structures, preserved structure, lost structure, architecture characteristic, and receiving pattern. |
| **Level or scale word is not typed** | Recover level, layer, tier, scope, and scale wording through `E.10.ARCH`, `C.30.STRAT`, and `C.16.P` as applicable; recover BOSC, MHT, MET, MFT, and emergence-family wording through `E.10` and `B.2.P` before declaring holon-level refs, scope refs, scale windows, B.2 whole reidentification, or C.32.MLAO residual claims. |
| **Software-source overfit** | Treat software examples as domain lineage; admit other holons only after selected structures and affected scopes are recoverable. |
| **Lossless repair is assumed** | Every residual-reducing candidate names the new burden it creates. |
| **Front member is treated as durable optimum** | A front member is an archive or front relation under an evolution window, not a durable architecture optimum. |
| **Stepping stone is erased too early** | Keep retained stepping stones visible through `C.18` or `C.19` when they preserve future residual-reduction reach. |
| **Transformer-transformed residual is hidden** | A residual between the changing holon and the changed holon must open `C.32.CONWAY`; prepare transformer-side, transformed-side, joint, and bounded-mismatch candidates as comparison inputs or downstream candidate alternatives. |
| **Ideality is used as optimum** | Treat ideality as direction for candidate generation, not as an adequacy claim that a bearer may be removed. |
| **Universal bearer is admitted without scale window** | A general bearer still needs declared criteria rows, scale window, safety and admissibility boundaries, and an eval result when the claim depends on a reading. |
| **Functional graph has no feasible bearer** | A functional architecture that lacks feasible bearers is an unfit candidate, not an optimized architecture. |

### C.32.MLAO:7 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C32.MLAO-1` | The use starts from a recoverable residual triage. | Prevents premature optimization. |
| `CC-C32.MLAO-2` | Affected declared holon-level refs or declared scope refs and selected structures are named. | Keeps multilevel wording reviewable. |
| `CC-C32.MLAO-3` | Each candidate names residual reduced, architecture characteristic affected, and new burden. | Prevents one-sided optimization. |
| `CC-C32.MLAO-4` | Comparison inputs, comparison results, selection results, and choice results name their receiving pattern. | Keeps C.32.MLAO from performing comparison, selection, or choice locally. |
| `CC-C32.MLAO-5` | Lens-backed claims use C.29 when mathematical-lens use is being claimed. | Keeps mathematical adequacy outside this pattern. |
| `CC-C32.MLAO-6` | Source-return condition is present when compression hides distinctions. | Keeps later source-use or decision-use claims tied to recoverable sources. |
| `CC-C32.MLAO-7` | Evolution window, dynamic front or archive relation, and any NQD or OEE support are typed as retention or generation support only. | Blocks static-optimum and selector overread. |
| `CC-C32.MLAO-8` | Transformer and transformed holon architectures stay distinct when the residual crosses a changing relation, and `C.32.CONWAY` is used when correspondence candidates are being prepared. | Preserves kind distinction between architecture, work, transformation, and structural similarity. |

### C.32.MLAO:8 - Common repair cues

| Anti-pattern | Symptom | Repair |
|---|---|---|
| `LocalEvalAsWholeArchitecture` | One scope improves or one eval result is better, and the whole architecture is called better. | Return to residual triage; name improved and harmed scopes, selected structures, criteria rows, and residual-bearing locus before framing residual-reducing candidates. |
| `ProxyResultAsPreferenceRule` | A residual vector, score, graph, front, dashboard reading, or lens output is used to prefer a candidate before the selected structures and lost structure are recovered. | Recover the selected structures and lost structure, interpret the result as a diagnostic signal or lens output; comparison belongs to `A.19.CPM`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, and publication of a selected set to `G.5`. |
| `ParetoFrontAsDecision` | A front is treated as selected architecture. | Publication of a selected set belongs to `G.5`, local choice to `C.11`, set-returning selection to `A.19.SelectorMechanism`, and project architecture decision to `C.32.PAD`. |
| `StaticOptimumClaim` | A current residual-reducing candidate is called optimal without an evolution window. | Add evolution window, source-return condition, reopen trigger, and the receiving pattern result that actually produced the preference. |
| `TransformerTransformedCollapse` | The architecture of the changing holon and the changed holon are treated as one structure. | Open `C.32.CONWAY`; recover the changing relation, selected structures on both sides, residual-bearing locus, candidate alternatives, and any C.29 structural-similarity claim before residual framing. |
| `LevelWordsNoLevels` | Text says level or scope without declared refs. | Use `C.30.STRAT` for stratification-term recovery or `B.2.P` for whole-reidentification wording, then return to residual triage before candidate framing. |
| `OptimizationNoLoss` | Candidates show only gains. | Add new burden, known loss, or bounded exception. |
| `IdealityNoBurden` | A candidate removes a bearer or support function but does not name lost function, coupling, evidence, control, or source-return burden. | Return to C.32 and C.31; name function-bearing transfer, characteristic changes, and BLP scale window or waiver if scale advantage is claimed. |
| `FunctionNoBearerAtScope` | A functional change reduces one residual but no bearer can carry it at the affected scope under resource, placement, control, or evidence constraints. | Add or change bearer, split function, change placement or resource access, change control responsibility, reduce the demand, or reject the candidate. |

### C.32.MLAO:9 - Consequences

| Positive consequence | Cost or trade-off |
|---|---|
| Residual-reducing architecture candidates are made explicit. | The practitioner must name the affected levels or scopes, selected structures, residuals, preserved structure, lost structure, new burdens, and the receiving pattern for any comparison or choice claim. Use `C.30.STRAT` or `B.2.P` first when level wording or whole-reidentification wording is not yet typed. |
| Optimization language is usable without carrying architecture adequacy. | No scalar selector or architecture decision is available by wording alone. |
| Holonic breadth is preserved. | Non-software cases must still recover their selected structures and receiving patterns. |
| Residual triage and candidate framing stay distinct. | The team may need both `C.30.ILC` and C.32.MLAO. |
| Compressed representations can guide action. | Source-return triggers must be visible. |

### C.32.MLAO:10 - Rationale

`C.30.ILC` names cross-scope residuals and first architecture repair directions. `C.32` creates candidate palettes. C.32.MLAO is needed when the constructive candidate work is specifically about reducing a residual across declared holon-level refs or declared scope refs.

The nontrivial work is to prepare candidate architecture changes for later comparison by naming residual reduced and burden created, not by using an optimizer phrase, scalar output, or locally improved structure as the candidate frame.

This subpattern also keeps multilevel source-side material usable as source cues without ontology transfer: multilevel learning, frustration, RG-like, DSM, and Pareto material may discipline the frame only after the affected declared holon-level refs or declared scope refs, selected structures, preserved structure, lost structure, comparison inputs, receiving pattern, and stop condition are declared.

### C.32.MLAO:11 - SoTA-Echoing

These rows document transfers from source practice into C.32.MLAO. Each row states which part of the residual-reducing frame the draft sets or revises from the source; none imports its source-domain ontology into FPF.

| Source to inspect | Why this source is load-bearing here | Transfer into C.32.MLAO | Concrete C.32.MLAO mutation | Blocked overread |
|---|---|---|---|---|
| Current FPF architecture residual, criteria, eval, comparison, and level-recovery line: `E.10`, `E.10.ARCH`, `C.30.STRAT`, `B.2.P`, `B.2`, `C.30.ILC`, `C.32.ACS`, `C.32.ACE`, `A.19.CPM`, `A.19.SelectorMechanism`, `C.11`, `G.5`, `C.29`, `C.31`, `C.31.ASAP`, and architecture source section 15.3 | Current local law for interlevel and cross-scope architecture residuals. It is load-bearing because C.32.MLAO starts only after residual triage, because criteria and eval have separate receiving patterns, because stratification terms and whole-reidentification wording already have governing recovery patterns, and because comparison, selection, choice, and publication of selected sets have existing receiving patterns. | Require C.30.STRAT recovery when stratification wording is ambiguous and B.2.P recovery when BOSC, MHT, MET, MFT, or emergence wording is ambiguous; require declared holon-level refs or declared scope refs, selected structures, criteria rows, residual-bearing loci, preserved structure, lost structure, eval result refs when used, comparison inputs, and receiving pattern before residual-reducing candidates enter comparison, selection, choice, or publication of a selected set. | `MultilevelArchitectureResidualOptimizationFrame@Project` now requires residual triage, declared holon-level refs or declared scope refs, selected structures, architecture-characteristic criteria rows, residual-bearing loci, residual-reducing candidates, optional C.29 lens-output ref, comparison input refs, receiving pattern ref, and stop condition. | Same-scope structure conflict, generic complexity wording, untyped criteria, eval-result overread, untyped stratification terms, untyped BOSC or MHT triggers, local comparison work, local selection work, and untyped optimization phrases return to their governing patterns before C.32.MLAO admits the frame. |
| Vanchurin, Wolf, Katsnelson, and Koonin, `Towards a Theory of Evolution as Multilevel Learning` (`https://arxiv.org/abs/2110.14602`); Wolf, Katsnelson, and Koonin, `Physical foundations of biological complexity` (`https://arxiv.org/abs/1803.09975`); Akhtyrchenko, Katsnelson, and Ustyuzhanin, `Directing Open-Ended Evolution ... via Multi-Scale Path Divergence`, submitted 2026-06-12 (`https://arxiv.org/abs/2606.17091`) | Current source line for multilevel residual and scale-dependent frustration as a mathematical lens. The 2026 MSPD paper is current because it makes scale-dependent frustration explicit and computable while still being a lens over a substrate. | Use frustration and multiscale divergence as optional C.29-backed lens outputs for residual-bearing loci across declared holon-level refs or declared scope refs. | C.32.MLAO adds `c29LensOutputRef?`, residual-bearing locus, preserved and lost structure, comparison input refs, and receiving pattern ref so any comparison has its receiving pattern named. | Source-domain ontology stays outside architecture; a scalar output must be interpreted as pressure, loss, or residual over selected structures before a receiving comparison or choice pattern can use it. |
| Evolutionary architecture: Ford, Parsons, Kua, and Sadalage, `Building Evolutionary Architectures`, 2nd ed. (`https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/`) | Current practitioner architecture line for guided incremental change over declared architecture characteristics, affected selected structures, and feedback from source-side fitness functions. | Residual-reducing candidates must name the new burden they introduce and the stop or reopen condition; source-side fitness-function practice is restored as ACE eval programs over ACS criteria rows. | Candidate-family table includes bounded exception, evidence scope, interface grammar, control structure, and work-method scope; consequences require new burden, source-return triggers, and receiving use for eval results. | A local eval improvement needs an architecture interpretation before a comparison, selection, or choice receiving pattern can use it. |
| TRIZ ideality and laws of technical-system evolution, read with `C.19.1` BLP | Older heuristic line: systems tend toward more useful function with less cost, harm, and support apparatus; BLP supplies FPF scale-amenability discipline for general bearers. | Use ideality and scale amenability to generate residual-reducing candidates, not to select them. | Frame adds `architectureIdealityPressureRef?` and `scaleAmenabilityPolicyRef?`; Solution adds ideality and BLP discipline; anti-pattern table adds `IdealityNoBurden`. | Removing a part, consolidating functions, or choosing a universal bearer is not residual reduction unless selected structures, characteristics, new burden, and scale boundary are declared. |
| Multi-objective and hardware-aware NAS: Elsken, Metzen, and Hutter 2019 (`https://www.jmlr.org/papers/v20/18-598.html`); Sukthanker et al., v3 revised 2025-02-04 (`https://arxiv.org/abs/2402.18213`); Sinha et al. 2024 (`https://arxiv.org/abs/2404.12403`) | Current architecture-search line where functional graph candidates are judged against hardware, latency, cost, and transfer constraints; useful as a general co-design lesson beyond ML. | Residual-reducing candidates that change functional structure must also name feasible bearers at affected scopes. | Frame adds `functionBearerFeasibilityRef?`; Solution adds functional-bearer feasibility discipline; candidate-family table adds `repairFunctionBearerGap`. | A functional graph, resource score, or Pareto member is not residual reduction if no admitted bearer can carry the function. |
| Architecture trade-off practice and `Software Architecture: The Hard Parts` (`https://www.oreilly.com/library/view/software-architecture-the/9781492086888/`) | Best current practitioner line for no-best-practice architecture decisions and explicit trade-off analysis in hard architecture problems. | Frame each candidate as residual reduced plus burden created, not as a universal best answer. | Candidate rows require `residualReduced`, `newBurden`, `preservedStructure`, and `lostOrHiddenStructure`; final choice exits to `C.11` or `C.32.PAD`. | A trade-off scenario, ranking, or preferred decomposition is not a decision inside C.32.MLAO. |
| DORA loosely coupled teams, last updated 2025-10-20 (`https://dora.dev/capabilities/loosely-coupled-teams/`), DORA trunk-based development (`https://dora.dev/capabilities/trunk-based-development/`), and Team Topologies key concepts (`https://teamtopologies.com/key-concepts`) | Current socio-technical practice for independent change, testing, deployment, small batches, dependency reduction, and fast flow. It is load-bearing because many residuals are borne by role, work, responsibility, and coordination structures, not only software modules. | Admit organization, work, role-enactor, and method-scope residuals when selected structures and affected scopes are recoverable. | Worked cases include clinical practice, AI-agent review setup, and method family; candidate-family table includes mediator, work-method scope, interface grammar, and control structure. | Organization-design observations enter C.32.MLAO only after they are mapped to role, work, responsibility, coordination, or method structures; they do not supply module, evidence, assurance, or decision claims by themselves. |
| Design-space and architecture-spread research: Shaw and Petre 2024 (`https://arxiv.org/abs/2407.18502`); Cortellessa et al. 2024 (`https://arxiv.org/abs/2402.19171`) | Current research showing that useful alternatives need a design-space or architecture-space view, not only objective-space scores. | Preserve plural residual-reducing candidates when residuals shift differently across structures or scopes. | C.32.MLAO preserves candidate plurality as C.32 input; publication of a selected set belongs to G.5; spread, diversity, or objective-space output is used only after the architecture differences it reveals are named. | Candidate preference still depends on declared architecture characteristics, losses, and a receiving pattern. |
| C.18 archive and front stewardship plus C.19 explore-exploit governance | Current FPF pattern line for open-ended search, NQD, OEE, archive, front, pool treatment, and stepping-stone retention. | Treat NQD and OEE as generation and retention support for residual-reducing candidates, not as architecture selection. | Frame fields add `dynamicFrontOrArchiveRef?`, `nqdOrOeeSupportRef?`, `steppingStoneRefs?`, and `evolutionWindowRef`; Solution adds dynamic optimum discipline. | Archive membership, front membership, retained stepping stone, or pool treatment is not architecture adequacy or decision. |
| Conway's law, mirroring, DORA loosely coupled teams, Team Topologies, and current `C.32.CONWAY` | Current practice line for residuals where the changing holon's work, communication, tool, method, deployment, or evidence structures no longer fit the changed holon's desired architecture. | Treat correspondence mismatch as a residual-reducing architecture synthesis problem, not as organization identity or transformed-holon architecture settlement. | Frame field `transformerTransformedCorrespondenceRef?` now points to `C.32.CONWAY`; candidate-family table adds `repairTransformerTransformedCorrespondence`; Solution prepares transformer-side, transformed-side, joint, and bounded-mismatch candidates as comparison inputs or downstream candidate alternatives. | A correspondence residual is repaired only after the shifted burden, affected structures, characteristic pressure, and exception cost are named. |

**Source-currentness boundary.** Use each source row only for the frame field, candidate-family row, discipline paragraph, or boundary named in that row. Recheck the row when a cited paper, book edition, DORA or Team Topologies page, FPF receiving pattern, project residual, selected structure, criteria row, or evolution window changes. If the source no longer supports the concrete mutation, lower it to background lineage and keep the residual frame only when local residual triage, selected structures, criteria rows, new burden, and receiving pattern remain recoverable.

### C.32.MLAO:12 - Relations

- **Builds on:** `C.30.ILC` for residual triage, `C.32` for palettes, `C.32.ACS` for architecture-characteristic criteria rows, `C.32.ACE` for eval programs and eval results, `C.29` for mathematical-lens use when claimed, `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice over an existing option set, `G.5` for publication of a selected set, `C.19.1` for scale-amenability preference claims, and `C.31` or `C.31.ASAP` for characteristic or scale-preference claims.
- **Uses:** `E.10.ARCH` and `C.30.STRAT` when stratification terms hide the recovered neighborhood; `E.10` and `B.2.P` when BOSC, emergence-family, MHT, MET, MFT, boundary-crossing, or promotion-like wording hides the claim kind; `B.2` when the candidate creates, reidentifies, splits, joins, or changes the relevant whole after existing-whole explanations are insufficient; `C.32.CONWAY` when residual reduction requires co-synthesis of transformer and transformed architectures; `A.6.M`, `C.30.LCA`, `C.30.TFS-REL`, and method or work patterns when their structures are the affected selected structures.
- **Receiving patterns:** `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `G.5` for publication of a selected set, `C.11` for fixed local choice, `C.30.AD`, `E.17`, and `E.24.PUB` for architecture-description or publication-face work, and `C.32.PAD` for project architecture decisions.
- **P2S docking:** `C.32.P2S` uses MLAO when cross-scope, interlevel, interlayer, or meta-holon residual pressure must become candidate-synthesis and repair content inside the wider architecturing flow.
- **Boundary:** C.32.MLAO governs residual-reducing architecture candidate frames after residual triage. It does not govern mathematical-lens adequacy, evidence, assurance, gate passage, ethical mediation, causal claim adequacy, work authorization, or final selection.

### C.32.MLAO:13 - Footer marker

`C.32.MLAO` governs bounded residual-reducing architecture candidate frames. Upstream residual triage and downstream decision, gate, release, publication, or authority-relation claims use their own patterns.

### C.32.MLAO:End

