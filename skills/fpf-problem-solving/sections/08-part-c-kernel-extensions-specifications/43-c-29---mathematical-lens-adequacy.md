## C.29 - Mathematical Lens Adequacy (MLA)

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Mathematical lens adequacy.

**Governed object.** C.29 governs only mathematical-lens adequacy claims carried by FPF prose, pattern examples, method notes, review records, `PublicationUnit`s, decision-facing text, comparison-facing text, bridge-facing text, or assurance-input text that use a mathematical object, formalism, learned representation, simulation substrate, or mathematical family as a lens for a stated use. It does not govern those objects themselves: `PublicationUnit`s, decision records, comparative review units, bridges, work records, evidence paths, and assurance inputs remain with their own FPF loci; C.29 contributes only the bounded adequacy of the mathematical lens used inside them.

**Output posture.** C.29 outputs are claim-supporting notes, not actors, approvals, gates, work records, or release decisions. They state what the mathematical lens can support for one declared use and which neighboring FPF locus carries any live claim outside lens adequacy.

**No new `U.*` from MLA.** `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, `MLA.Card@Context`, `MLAOutputRef`, and `CC-MLA-*` are C.29-local instruments. They do not mint `U.MathematicalLens`, `U.MLARecord`, `LensKind`, `MLACompliance`, or a durable record family. Durable names, kinds, or records require explicit FPF support through `F.18`, `C.3`, `F.8`, and `E.9`.


### C.29:0 - First-use card

Use this card before the full card. It is enough for the first reading unless publication, bridge, assurance input, benchmark, model selection, prediction, formal pattern claim, or repeated cross-case use is live.

| First question | Required answer before the lens carries claim force |
|---|---|
| Is the mathematical phrase changing the next admissible move, or only helping recognition? | If no move changes, keep ordinary prose or write `NoMLANeededNote`. |
| What phenomenon is being seen through the lens? | Name `TargetPhenomenon` in problem-owning language. |
| What concrete mathematical object, formal role, learned representation, simulation substrate, or local formalism is being used? | Name `CandidateMathObject`; broad family names are prompts only. |
| What structure is preserved? | Name `PreservedStructure`. |
| What structure is lost or deliberately ignored? | Name `LostStructure`; empty loss needs equivalence or isomorphism support. |
| What tempting inference does this lens not license? | Name `StopCondition`; no stop condition means no admissible C.29 result. |

Non-use comes first. Do not open C.29 merely because mathematics appears. Open it only when the mathematical structure changes explanation, decision, prediction, comparison, publication, bridge, assurance input, reusable transfer, or the next admissible repair. If state, transition, measurement, causal use, bridge semantics, temporal adequacy, assurance, selector, benchmark, or release is the live claim, name the neighboring FPF locus and keep C.29 to the mathematical-lens adequacy part.


### C.29:1 - Problem frame

FPF already uses mathematical structures in several local patterns. `A.6.P` asks for stable mathematical substrate during relation precision restoration; `A.3.3` governs dynamics; `A.19` governs characteristic spaces and structural overlays; `C.18.1` and `C.19.1` govern scale-law and Bitter-Lesson claims; `C.26` contains the separation of a quantum-like lens from physical quantum ontology; `F.9` governs cross-context bridges and loss.

The positive need is as important as the guard. In working projects, first-principles mathematical thinking starts from the smallest declared structure that can make a next move derivable, inspectable, or honestly blocked. A queue can expose waiting and bottlenecks, a state space can expose variables and transitions, a graph can expose dependencies, a metric-space distance or topology can expose comparability limits, a symmetry can expose invariants, a variational principle or constrained optimization functional can expose an extremal condition, admissible variation space, boundary condition, conservation link, or trade-off, an information or probability measure can expose uncertainty, a resource bound can expose realizability limits, and an obstruction can expose where a transfer or simplification stops.


The missing FPF rule is general but narrow: when FPF prose, a pattern example, method note, review record, `PublicationUnit`, or neighboring-pattern note uses or plausibly needs a mathematical object, formalism, or family as the basis for explanation, decision, prediction, comparison, publication, bridge, assurance input, or reusable transfer, the `C.29` application records the useful first-principles modeling basis and its boundary. It names the candidate mathematical object or family, what structure is preserved, what structure is lost, what invariant, supported distinction, obstruction, diagnostic boundary, or constructive limit becomes visible, which `LensSupportPosture` value is declared for that use, and where the transfer stops.


`C.29` is not opened because mathematics appears. It is opened when either a mathematical object is used for explanation, decision, prediction, comparison, publication, bridge, assurance input, or reusable transfer, or a stable working problem is under-lensed and a cheap candidate lens could expose useful structure for the next move.

The first move is not a full-card demand. It is a first-principles entry decision: choose the smallest mathematical structure that changes the next admissible move, keep ordinary prose when no mathematical basis changes the move, or send the live claim to the neighboring FPF pattern. The result records what the lens preserves, what it loses, what it makes visible, what remains blocked, and where the use stops.


Selected compact formulation:


> **A useful mathematical lens is compression with invariants and declared losses.**

This compact line is retained as a Plain-register orientation, not as a substitute for the card. It keeps the useful metaphor of a **lens**: a mathematical object can make a hidden structure visible, but only by carrying some structure and dropping other structure. The first reader questions are: **what survives the transfer, what is lost, what can now be done, and where does the lens stop?**

#### C.29:1.1 - First-minute working situation

An FPF author, reviewer, or practitioner faces a working situation where ordinary prose can hide useful structure, or where a mathematical phrase is already doing work:

- waiting, backlog, bottleneck, or throughput can call for a queue or flow lens;
- state change, stabilization, control pressure, or forecast can call for state-space or dynamics vocabulary;
- dependency, interface, composition, or transfer failure can call for graph, hypergraph, category, operad, or compositional vocabulary;
- similarity, distribution shift, population movement, or shape change can call for metric-space distance, topology, embedding, or optimal-transport vocabulary;
- scale transition, coarse behavior, universality, knee, or scaling pressure can call for coarse-graining, RG, or scaling-law vocabulary;
- probe effects, order effects, context effects, or incompatible frames can call for quantum-like or contextual-probability vocabulary.

The useful first-minute intuition is not “hunt for overclaim.” It is “find the structure that would improve the next move, then name the limits.” A vivid phrase can remain when the `C.29` output records what the lens lets the reader see, what it does not license, and which neighboring pattern carries any causal, evidence, bridge, dynamics, scale, measurement, assurance, or release claim.

Without a general adequacy discipline, the reader cannot tell whether the phrase is a bounded structure-preserving representation, an analogy-only prompt, an unsupported ontology import, a local domain model, or prestige language.


#### C.29:1.2 - Minimum scenario / anti-case basis

**Positive scenario.** A production line is represented as a queueing network. The lens preserves flow, bottlenecks, service rates, and waiting times; it loses human meaning, contractual obligations, rare failure modes, and causal interventions not represented by the network; the stop condition says that the queueing lens supports throughput and latency reasoning, not a full organizational ontology.

**Anti-case.** “The organization is a quantum system” is written without a candidate mathematical object, probe/readout distinction, preserved structure, lost structure, `LensSupportPosture`, or stop condition. The `C.29` result is either a downgrade to local metaphor or a repaired use through `C.29` and, where relevant, `C.26`.

**Under-lensed anti-case.** “The work stream has dynamics” or “this portfolio is a network” is used for a diagnosis that affects prediction, comparison, repair, or stop conditions, but no mathematical object changes what can be predicted, compared, diagnosed, repaired, or stopped. The repair is to choose a cheap candidate lens that exposes useful structure, or keep the sentence as ordinary prose.

**False-positive scenario.** A Markov kernel appears inside accepted local reliability modeling. If no contested lens-transfer, publication, assurance, bridge, or reusable explanation claim is live, the claim stays under `A.3.3` and does not open `C.29`.

#### C.29:1.3 - Intended FPF use-value

`C.29` gives a cheap use path before any full card or boundary table. Its first job is to help the working reader introduce, choose, repair, bound, or decline a mathematical lens: choose no MLA, a candidate note, a one-line repair, a mini-card, a full card only when publication, bridge, assurance-input, benchmark, model-selection, prediction, or reusable-explanation use requires it, or a named neighboring locus when the live claim belongs to evidence, causal, bridge, assurance, work, decision, publication, or admission governance rather than lens adequacy. Use it only when the mathematical lens affects a claim or next move; ordinary local math and decorative prose stay outside C.29. A successful `C.29` result makes useful mathematical compression available to FPF as a disciplined modeling move while reducing ontology smuggling, prestige vocabulary, loss-free transfer, causal laundering, bridge duplication, evidence laundering, and assurance laundering.


### C.29:2 - Problem

Current FPF math-lens adequacy criteria are distributed and local:

- `A.6.P` governs relation precision restoration, but not every mathematical-object transfer.
- `A.3.3` governs state, transition, observation, validity, constraints, and calibration for dynamics, but not all mathematical representation choices.
- `A.19` governs characteristic spaces, structural overlays, comparability, normalization, and bridge-aware state comparison, but not the adequacy of all mathematical lenses.
- `C.18.1` and `C.19.1` govern scale-law and BLP claims, but not non-scale mathematical lenses.
- `C.26` is the local precedent for mathematical-lens detachment, but only for quantum-like modeling.
- `F.9` governs cross-context semantic bridges, but does not decide whether a mathematical substrate is adequate inside one context or as a domain-transferring lens.

There are two symmetric failure modes.

The first failure mode is mathematical under-lensing: a working situation needs a mathematical lens that changes prediction, comparison, diagnosis, repair, or stop conditions, but the record carries only ordinary prose, familiar school math, or a broad family name such as graph, field, space, score, trend, dynamics, or quantum-like without a useful invariant, obstruction, state variable, mapping, scale behavior, rival lens, or action-changing payoff.

The second failure mode is mathematical overread:

> a mathematical phrase begins as a helpful representation and then silently becomes ontology, evidence, causality, comparability, assurance, or admissibility.


### C.29:3 - Forces

| Force | Tension |
|---|---|
| **Compression vs truthfulness** | A useful mathematical lens compresses many cases by pairing compression with declared losses. |
| **Plural mathematical foundations vs FPF simplicity** | The intended gain is access to modern plural foundations and applied mathematics, with each selected lens tied to a stated use, declared loss, and neighboring-pattern exit. |
| **SoTA openness vs metaphysical safety** | Vanchurin-like and Sandberg-like material enters as current lens prompts, not final ontology. |
| **General pattern vs local precision** | `C.29` stays non-duplicative with `A.6.P`, `F.9`, `C.26`, `C.28`, `A.3.3`, and `A.19`; its contribution is coordination around lens adequacy. |
| **Didactic usability vs formal rigor** | The first user needs one small card; expert use needs lens mapping mode, invariant claims, loss, `LensSupportPosture`, rival lenses, and stop conditions. |
| **Evocative metaphor vs ontology guard** | “Lens,” “structure survives transfer,” and “where the lens stops” help readers think, while exact fields carry FPF claim force or admissibility. |
| **Transfer reach vs domain validity** | Category, RG, variational, quantum-like, and learning lenses are useful because they travel; that same transfer reach makes misuse easy. |

### C.29:4 - Solution and selected answer

#### C.29:4.1 - Selected answer in one paragraph

`C.29 — Mathematical Lens Adequacy (MLA)` is the general FPF discipline for mathematical lenses used in explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer. It handles two first-use cases, with the positive case first: an under-lensed situation where the next admissible move can benefit from a cheap first candidate lens; and an existing candidate lens ready for application, repair, bounding, replacement, or rejection. Its job is to help the reader introduce, choose, apply, limit, replace, or remove a mathematical lens so that a useful admissible next move survives. A mathematical lens is admissible for a declared use when it compresses a phenomenon by preserving declared structure, exposing useful invariants, and producing lens-supported predictions, distinctions, obstructions, or diagnostic boundaries inside a bounded context. It is inadmissible for an undeclared or unsupported use when it imports source-domain ontology, hides loss under metaphor, treats source prestige as evidence, or licenses claims outside its declared scale, context, validation, bridge, causal, or assurance boundary.


`C.29` does not mint `MathematicalLens`, `U.MathematicalLens`, `LensKind`, or any universal FPF lens object. In this pattern, “mathematical lens” names a declared use of a mathematical object, formalism, learned representation, simulation substrate, or mathematical family under declared mapping, preserved/lost structure, `LensSupportPosture`, admissible use, and stop condition; the target phenomenon and any claim outside lens adequacy keep their own FPF kinds.

Admission guard: C.29 governs mathematical-lens adequacy claims. It does not mint mathematical-lens kinds, and it does not govern or create the described entity, Bridge, evidence path, causal support, assurance score, measurement construction, dynamics semantics, decision record, work record, explanation rendering, comparative review unit, representation transition, coarsened rendering, selector, benchmark, or scale audit. Its outputs are local adequacy outputs unless a separate FPF naming and admission decision makes one durable.


#### C.29:4.2 - Mathematical Lens Adequacy Principle

> **Mathematical Lens Adequacy Principle.**
> A mathematical lens is admissible for a declared use when it compresses a phenomenon by preserving declared structure, exposing useful invariants, and producing lens-supported predictions, distinctions, obstructions, or diagnostic boundaries inside a bounded context. It is inadmissible for an undeclared or unsupported use when it imports source-domain ontology, hides loss under metaphor, treats source prestige as evidence, or licenses claims outside its declared scale, context, validation, bridge, causal, or assurance boundary.

Compact plain form:

> **A useful mathematical lens is compression with invariants and declared losses.**

Register policy: **Tech exactness below, Plain metaphor above.** Plain phrases such as “structures that survive transfer,” “what the lens makes visible,” and “where the lens stops” are admissible as recognition aids. When a sentence carries FPF-kind, relation, evidence, admissibility, causal, assurance, bridge, gate, work, decision, or pattern-application claim force, the corresponding `C.29` output recovers the exact fields and receiving patterns.

Zero/first-principles compatibility note: `E.1` and `E.2` govern the mission and pillar authority. `C.29` supports them by making mathematical first-principles support inspectable for one declared use: candidate mathematical object, preserved structure, lost structure, visible payoff, admissible move, neighboring-pattern boundary, and stop condition. It does not replace pillar authority, neighboring governing loci, ordinary FPF reasoning, or `E.9` design-rationale support for normative changes.

Mathematics is not a prerequisite for FPF use. Ordinary prose is valid when no mathematical structure changes the next admissible move. C.29 earns its place only when a mathematical object, formalism, learned representation, simulation substrate, or mathematical family changes explanation, decision, prediction, comparison, publication, bridge, assurance input, reusable transfer, or the next admissible repair.

Plain/Tech bridge:

| Plain reader question | Tech recovery |
|---|---|
| What structure helps? | `CandidateMathObject` or `CandidateLensFamily` in a `LensCandidateNote`. |
| How does it represent the phenomenon? | `LensMappingMode`. |
| What survives? | `PreservedStructure`. |
| What disappears or is deliberately ignored? | `LostStructure`. |
| Why trust this use? | `LensSupportPosture`, validation overlay when live, and neighboring evidence/assurance loci when their claims are live. |
| What can the reader now do? | `AdmissibleNextMove` or `admissibleUse`. |
| What remains blocked? | `StopCondition` and `nonAdmissibleUse`. |

State, scale, and dynamics trigger: if the lens carries state, transition, forecast, rate, temporal window, scale window, observation, measurement, comparison, score, strong/weak wording, or causal implication, the cheapest honest output either names the minimal relevant field or names the receiving FPF locus. If characteristic, scale, coordinate, score, metric, indicator, or comparison wording is itself hidden, use `C.16.P` before relying on C.29; if a valid measurement relation is already recoverable, measurement construction and direct comparability stay with `C.16`. State and transition semantics stay with `A.3.3`; characteristic spaces and overlays stay with `A.19`; temporal-use adequacy stays with `C.27`; scale-law and scale-preference claims stay with `C.18.1` and `C.19.1`; causal-use support stays with `C.28`.


#### C.29:4.2a - Mathematicalization Utility Principle

A mathematical lens is worth introducing only when it changes the working reader's next admissible move by making at least one first-principles modeling basis visible:

- a declared signature, structure, state variable, transition, or observation map;
- a symmetry, invariant, conservation-like constraint, equivalence, or composition rule;
- a local-global relation, boundary relation, scale variable, coarse-graining rule, scale window, or correspondence condition;
- a variational principle, action, energy, free-energy, loss, or value functional, Euler-Lagrange or stationarity condition, constrained optimization target, dual view, objective vector, or resource trade-off;
- an uncertainty, probability, information, typicality, approximation, sensitivity, or validation boundary;
- an algorithmic, constructive, resource, realizability, implementation, or adversarial limit;
- a bottleneck, obstruction, impossibility, consistency boundary, or failed transfer in the candidate-model space;
- a rival-lens distinction that changes model choice;
- a causal, intervention, or counterfactual preservation question governed by `C.28`;
- a bridge or export loss governed by `F.9`;
- a measurement or comparability condition governed by `C.16`.

If no next admissible move changes, keep the text as ordinary prose, downgrade it to a didactic metaphor, or return `NoMLANeededNote`. A lens that merely makes prose more impressive is not a successful `C.29` result.


#### C.29:4.2b - First-principles lens-family support

`C.29` supports first-principles use only when the principle family changes what the working reader can derive, inspect, compare, observe, or honestly block. The family name is never enough. Each row below is a discovery and recovery discipline: it tells the reader what must be named before the mathematical lens can carry claim force.

| First-principles family | Use when the working problem asks | Required `C.29` recovery | Stop or neighboring exit |
|---|---|---|---|
| Boundary, exterior derivative, Stokes-like local-to-global relation | How local increments, flows, sources, interfaces, or balances compose into a global claim. | Name the domain, boundary, field/form/flow, derivative/divergence/curl-like operator, boundary condition, and what is conserved, sourced, or lost at the boundary. | Does not make all boundary language one mechanism; measurement, evidence, and bridge claims move to `C.16`, `A.10`, or `F.9`. |
| Cohomology, closed/exact split, topological obstruction | Why a local rule cannot be made global, or why a transfer/composition is blocked. | Name the cycle/cocycle-like object, equivalence class or obstruction, local closure condition, failed exactness/global witness, and the blocked claim. | Useful obstruction is a `LostStructure` or `StopCondition`; it is not a causal explanation without `C.28` and evidence. |
| Symmetry, invariance, equivariance, Noether-like conservation | Which transformations leave the relevant claim unchanged, or which conservation-like quantity follows from an invariance. | Name the transformation family, action on the described variables, invariant or conserved quantity, assumptions, and distinctions intentionally lost. | Does not transfer physical conservation, coordinate-free truth, or causal mechanism without domain evidence and dynamics support. |
| Variational principle, action, energy/free-energy/loss/value functional, Legendre or convex duality | Whether a behavior, representation, design, or trade-off follows from stationarity, extremum, dual variables, or potential transformation. | Name the functional, admissible variation space, constraints, boundary conditions, stationarity or extremum condition, dual transform, and what the dual view makes visible. | Does not imply the target literally optimizes that functional unless `A.3.3`, `A.10`, or `C.28` support the dynamics, evidence, or causal use. |
| RG, coarse-graining, fixed point, basin, universality | Why different microdescriptions can share one macropattern, or when a scale claim stops. | Name the scale variable, scale window, coarse-graining rule, fixed point or attractor, basin/regularity condition, invariant or exponent, and lost microstructure. | Scale-law adequacy and scale advantage move to `C.18.1` and `C.19.1`; no micro-mechanism identity is licensed. |
| Diagonal, self-reference, fixed-point theorem, no-go family | Whether a universal evaluator, complete language, self-model, closure rule, or governance rule is blocked by self-application. | Name the encoding, evaluator or self-map, diagonal/fixed-point construction, universal claim being tested, and exact impossibility or closure boundary. | Does not prove every recursive-looking case is a no-go theorem; assurance or governance claims move to `B.3`, `E.19`, or the local domain pattern. |
| Composition, category, operad, optic, semiring or limit transform | Whether composition, interface, view, transformation, or algebraic law is the useful preserved structure. | Name objects, morphisms/relations, composition law, identity or interface condition, preserved algebraic law, failed transfer, and any limit transform such as classical/tropical or Fourier-Laplace/Legendre. | Bridge semantics and substitution safety move to `F.9`; C.29 only records lens adequacy and loss. |
| Probability, information, observation, acquisition | Which uncertainty, information, typicality, readout, or next observation changes the next admissible move. | Name the random variables or distributions, utility or information criterion, observation/probe design variable, model assumptions, estimation method, validation boundary, and robustness posture. | Measurement, evidence, experiment planning, causal support, and assurance stay with `C.16`, `A.10`, `C.28`, `A.15`, and `B.3`. |

This table is normative as a recovery guide, not as a mandatory taxonomy. A local project may name a closer family, but it must recover the same kind of load-bearing structure: mathematical substrate, preserved structure, lost structure, visible payoff, support posture, and stop condition.

#### C.29:4.3 - Use boundary

This boundary prevents `C.29` from being over-applied.

**Use `C.29` when** a mathematical object, formalism, learned representation, simulation substrate, or mathematical family is used as a lens for explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer over a physical, organizational, epistemic, social, computational, scientific, or methodological phenomenon, or when a phenomenon, decision, explanation, comparison, model-selection, diagnosis, or method-choice problem is stable enough that the first useful move is to choose a cheap candidate lens that makes relevant structure visible.

**Do not use `C.29` as the governing pattern when:**

- the mathematics is ordinary local domain theory already governed by a domain pattern;
- the phrase is a purely didactic analogy that is not reused for decisions, evidence, assurance, publication, bridge, comparison, or transfer;
- the live question is causal-use support, which is governed by `C.28`;
- the live question is measurement construction, scale legality, direct comparability, or evidence-stub adequacy, which is governed by `C.16`;
- the live question is cross-context meaning or substitution safety, which is governed by `F.9`;
- the live question is dynamics semantics without a separate lens-transfer claim, which is governed by `A.3.3`;
- the live question is a `CharacteristicSpace` overlay with no domain-transfer, prediction, assurance, publication, or reusable explanation claim, which stays under `A.19`.
- the live object is a `ChoiceResult`, local choice record, selected-set publication, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant source restoration; those claims stay with `C.11`, `G.5`/`G.9`, `A.15`, `A.15.1`, or `A.15.4` as appropriate.
- the live object is an explanation-facing rendering, bounded comparative review unit, same-described-entity representation-scheme transition, or controlled semantic coarsening; those claims stay with `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, or `A.6.3.CSC`, with MLA fields carrying only mathematical-lens adequacy when the mathematical lens affects the stated admissible use.
- the live claim is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for use; temporal-claim adequacy stays with `C.27`.

This boundary keeps mathematical-lens adequacy from becoming a shadow record for neighboring work.

Lexical rule: use **structure-preserving representation** rather than **structure-preserving identification** in discoverability-bearing prose, unless equivalence or identity is explicitly the declared `LensMappingMode`.

#### C.29:4.4 - Action path before the full card

Begin with action guidance, not with the full card.

First action choices: keep ordinary prose, introduce a cheap candidate lens, name a substrate that fits the stated use more directly, add visible payoff, add loss, choose the principal rival lens, add validation posture, narrow an existing claim, downgrade an overclaim, or move any evidence, causal, bridge, assurance, work, decision, publication, or admission claim to the exact neighboring FPF locus.

Memory hook: a successful C.29 application can raise or lower the mathematical claim force. It can introduce a first candidate lens, keep ordinary domain prose, remove a mathematical lens, repair relation wording through `A.6.P`, declare a `CharacteristicSpace` through `A.19`, use `C.16` for measurement and comparability, open `F.9` for bridge semantics, ask the `C.28` causal-use question, restore work or source responsibility through `A.15`, or send temporal-use adequacy to `C.27`.

No-lens cheap path: name the `ProblemStructureCue`, choose the cheapest candidate lens family that makes it visible, test whether that lens changes the next admissible move, and if no move changes, keep ordinary prose or collect more observations before using mathematical-lens wording.

First neighboring-locus map:

| Claim-bearing question | Govern there first | C.29 remainder |
|---|---|---|
| relation substrate, relation kind, or structure-preserving relation wording | `A.6.P` and local relation patterns | mathematical-lens adequacy only if a mathematical object changes the stated use |
| state variables, transition law, observation map, constraints, or calibration | `A.3.3` and `A.19` | preserved/lost structure and lens stop condition |
| measurement construction, scale, unit, polarity, or comparability | `C.16` | lens support posture for measurement-dependent use |
| scale law, universality, knee, exponent, or scale preference | `C.18.1` / `C.19.1` | scale-bounded mathematical-lens adequacy |
| cross-context meaning, substitution, or Bridge-supported use | `F.9` | mathematical structure used inside the bridge claim |
| causal, intervention, policy, or counterfactual use | `C.28` | whether the lens preserves, approximates, or blocks causal-use structure |
| evidence, provenance, source currentness, assurance, release, selector, or benchmark use | `A.10`, `B.3`, or relevant `G.*` pattern | adequacy of the mathematical lens as one input only |

Math-apparatus boundary: `C.29` coordinates the lens-adequacy part across relation substrate, state/characteristic spaces, measurement, dynamics, scale, bridge, causal, evidence, assurance, selector, and benchmark patterns. It does not replace any one of them.


1. **Find the claim-bearing phrase.** Mark the exact mathematical phrase that affects explanation, decision, prediction, comparison, publication, bridge, assurance-input, or reusable transfer.
2. **Choose the smallest output class that preserves honesty.** The output-class decision happens before any full-card fields.
3. **Name the concrete mathematical object or structure.** Family labels such as `category theory`, `field`, `graph`, `quantum`, `RG`, or `geometry` are entry prompts, not adequate substrates for the stated use by themselves.
4. **State the lens mapping mode.** Use the least committing honest `C.29`-local lens mapping mode: analogy-only prompt, representation, empirical fit, simulation, quotient, abstraction, coarse-graining, embedding, homomorphism, isomorphism, functor-like transfer, cross-context lens-transfer candidate, or accepted local theory. If cross-context meaning, substitution, CL, sense cells, or Bridge-supported use is live, `F.9` governs that claim; the MLA fields record only mathematical-lens adequacy for the declared transfer.
5. **State preserved structure and lost structure.** This is the central repair move.
6. **State what becomes visible.** Name the invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, lens-supported distinction, model-selection consequence, or other payoff.
7. **State the supported use and blocked use.** Say what is now admissible, what remains blocked, and which named neighboring FPF locus governs any live claim outside lens adequacy.
8. **If the claim does not pass, repair rather than merely fail.** Downgrade, narrow, switch to a principal rival lens, add `LensSupportPosture` or validation posture, split out bridge, dynamics, measurement, causal, temporal, decision, work, explanation, comparison, representation, scale, or assurance claims to the neighboring governing locus, or remove the mathematical phrase from claim-bearing use.

Application output classes:

| Output class | Output | Use condition | Required content |
|---|---|---|---|
| `NoMLANeeded` | `NoMLANeededNote` or ordinary Plain orientation | Mathematical language is local, didactic, or accepted local theory and is not used for transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable explanation. | State why `C.29` is not opened; no card. |
| `LensCandidateNote` | `MLA.LensCandidateNote` | A problem whose next move can depend on a mathematical lens is stable enough for a first candidate lens, but no adequate mathematical object has been named yet. | `TargetPhenomenon`, `ProblemStructureCue`, `CandidateLensFamily`, optional `CandidateMathObject?`, `WhyThisLensCouldHelp`, `ExpectedVisiblePayoff`, `ObservableOrControllableCue?`, `AdmissibleNextMove`, `OrdinaryRivalOrFallback`, `StopCondition`, `NextMLAOutput`. |
| `OneLine` | `MLA.OneLine` | An under-specified phrase affects explanation, decision, prediction, comparison, publication, bridge, assurance input, or reusable transfer and needs repair before reuse. | `TargetPhenomenon`, `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `VisiblePayoff`, `AdmissibleNextMove`, optional `ObservationOrReadoutNeeded?`, `OrdinaryRivalOrFallback`, `StopCondition`. |
| `MiniCard` | `MLA.MiniCard` | The lens supports a reusable explanation, local decision, comparison, or method-selection claim. | `OneLine` content plus `InvariantsExposed`, `LensSupportPosture`, `admissibleUse`, `nonAdmissibleUse`, principal rival, and `RivalLensRelation?` when another mathematical lens changes the admissible move. |
| `FullCard` | `MLA.FullCard` | Publication, bridge, assurance input, benchmark, model selection, prediction, formal pattern claim, or repeated cross-case use is live. | Full `MLA.Card@Context` plus any conditional overlays. |
| `NeighborGoverningLocusNote` | `NeighborGoverningLocusNote` | The live claim is causal use, bridge or substitution, measurement construction, scale legality, direct comparability, evidence-stub adequacy, dynamics semantics, temporal adequacy, decision result, selected method, work plan, performed work, evidence trust, assurance, explanation rendering, comparative review, representation transition, coarsening, scale law, release, selector, or benchmark. | Name the governing FPF locus and apply `C.28`, `F.9`, `C.16`, `A.3.3`, `C.27`, `C.11`, `A.15`, `A.15.1`, `A.15.4`, `A.10`, `B.3`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, `C.18.1`, `C.19.1`, or a relevant G pattern. The C.29 application keeps only lens-adequacy support. |

Micro-template examples:

```text
MLA.LensCandidateNote example := {
  TargetPhenomenon: slow Product-X team flow,
  ProblemStructureCue: waiting and work-in-progress look more important than individual task difficulty,
  CandidateLensFamily: queue or flow lens,
  CandidateMathObject?: single-server or multi-server queue candidate,
  WhyThisLensCouldHelp: arrivals, service time, WIP, and waiting time could expose the bottleneck,
  ExpectedVisiblePayoff: decide whether delay is arrival-rate, service-rate, batching, or WIP-boundary pressure,
  ObservableOrControllableCue?: arrivals, service time, wait time, WIP limit,
  AdmissibleNextMove: observe the variables before claiming queue adequacy,
  OrdinaryRivalOrFallback: ordinary process narrative without queue assumptions,
  StopCondition: no claim about motivation, obligation, blame, or full team ontology,
  NextMLAOutput: NoMLANeededNote or MLA.OneLine after observation
}
```

```text
MLA.OneLine example := {
  TargetPhenomenon: Product-X backlog delay,
  CandidateMathObject: queue model over arrivals, service time, waiting time, and work in progress,
  LensMappingMode: representation,
  PreservedStructure: flow, bottleneck candidates, wait, WIP, service-rate pressure,
  LostStructure: motivation, priority politics, contractual duties, skill learning, quality of work,
  VisiblePayoff: identify whether delay is arrival-rate, service-rate, batching, or WIP-boundary problem,
  AdmissibleNextMove: observe arrivals, service, wait, and WIP; test one local WIP-limit or batching hypothesis,
  ObservationOrReadoutNeeded?: service-time and wait-time readings,
  OrdinaryRivalOrFallback: process narrative without queue assumptions,
  StopCondition: do not infer team obligation, motivation, blame, or organizational ontology
}
```

```text
MLA.MiniCard example := {
  TargetPhenomenon: production-line throughput and latency,
  CandidateMathObject: queueing network with stated stations and service-rate assumptions,
  LensMappingMode: representation,
  PreservedStructure: flow, bottlenecks, service rates, waiting times,
  LostStructure: human meaning, contractual obligations, rare failure modes, causal interventions not represented by the network,
  InvariantsExposed: bottleneck station and queue-length sensitivity under stated assumptions,
  LensSupportPosture: accepted local theory plus local observations,
  admissibleUse: throughput and latency reasoning inside the declared line model,
  nonAdmissibleUse: motivation, duty, causal intervention, full organization ontology, or release assurance,
  PrincipalRivalLens?: direct empirical dashboard reading,
  RivalLensRelation?: complementary,
  StopCondition: no inference about motivation, obligation, rare-event causality, or full organizational ontology
}
```

```text
MLA.OneLine := {
  TargetPhenomenon,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  VisiblePayoff,
  AdmissibleNextMove,
  ObservationOrReadoutNeeded?,
  OrdinaryRivalOrFallback,
  StopCondition
}
```

For `MLA.OneLine`, `VisiblePayoff` says what the lens makes visible, such as a bottleneck, invariant, obstruction, incompatibility, loss boundary, or diagnostic split. `AdmissibleNextMove` says the now-admissible user move, such as compute a local quantity, compare only inside a declared structure, run a validation slice, apply a neighboring pattern, keep the phrase as local metaphor, or remove the phrase from claim-affecting use. `ObservationOrReadoutNeeded?` names the missing observable, readout, assignment, outcome, validation slice, or scale point needed before the repaired line can support the stated move. `OrdinaryRivalOrFallback` says what the reader would use without this mathematical lens: ordinary prose, accepted local domain theory, direct measurement, a causal model, a queueing model instead of a quantum-like metaphor, an `A.19` space declaration instead of `C.29`, or an `F.9` bridge instead of category-like wording. If two mathematical lenses already change the next move at this cheap-output class, add one ordinary-language note about the disagreement and move to `MLA.MiniCard` or `MLA.FullCard` before claiming a reusable rival-lens relation.

```text
MLA.LensCandidateNote := {
  TargetPhenomenon,
  ProblemStructureCue,
  CandidateLensFamily,
  CandidateMathObject?,
  WhyThisLensCouldHelp,
  ExpectedVisiblePayoff,
  ObservableOrControllableCue?,
  AdmissibleNextMove,
  OrdinaryRivalOrFallback,
  StopCondition,
  NextMLAOutput
}
```

`MLA.LensCandidateNote` is not evidence, assurance, a bridge, a decision record, a selector result, a literature survey, or a full adequacy card. It is a cheap first-candidate lens selection note. Its successful next outputs are `NoMLANeededNote`, `MLA.OneLine`, or a named neighboring governing-locus note.

Name guard for this note: `ProblemStructureCue` is a recognition cue, not a FPF signature; `CandidateLensFamily` is a family prompt, not a kind; `AdmissibleNextMove` is action guidance, not a work record; `NextMLAOutput` is the next C.29 output class, not a new record family.

Do not use `MLA.OneLine` with an empty `CandidateMathObject`. If the candidate object has not yet been named, use `MLA.LensCandidateNote` first or exit to ordinary prose or a neighboring governing locus.

Cheap stop: if the mathematical phrase does not affect any claim beyond orientation, do not open the full card. If the first honest output is `NoMLANeededNote`, that is a successful `C.29` result, not an underfilled card.

#### C.29:4.4.1 - Output set and use-rights

After applying `C.29`, the output is one of these:

| Output | Meaning |
|---|---|
| `NoMLANeededNote` | Ordinary local math or didactic metaphor; no transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable-explanation use. |
| `MLA.LensCandidateNote` | Cheap first-candidate note for an under-lensed problem whose next move can depend on a mathematical lens; not evidence and not a full adequacy card. |
| `MLA.OneLine` | Target, mathematical object, lens mapping mode, preserved structure, lost structure, visible payoff, admissible next move, optional observation or readout needed, ordinary rival or fallback, and stop condition. |
| `MLA.MiniCard` | One-line plus invariant or payoff, `LensSupportPosture`, admissible use, non-admissible use, and rival-lens relation when disagreement changes the next move. |
| `MLA.FullCard` | Full card for publication, bridge, assurance input, model selection, benchmark, prediction, or reusable explanation. |
| `NeighborGoverningLocusNote` | A named neighboring FPF locus governs the live causal, bridge, evidence, scale, dynamics, temporal, decision, work, explanation, comparison, representation, measurement, or assurance claim; the C.29 application records only the lens-adequacy part. |

Positive warning: a successful `C.29` output makes the mathematical lens honest for its declared use. It does not make the claim true, safe, released, benchmark-superior, decision-ready, or causally supported. Truth, safety, release, benchmark, decision, and causal-use claims need their governing neighboring FPF patterns.

`LensMappingMode`, `LensSupportPosture`, and use posture are separate readings.

| Reading | Question it answers | Where it is recorded |
|---|---|---|
| Mapping construction | How does the mathematical object represent, abstract, embed, quotient, simulate, learn, or transfer the phenomenon? | `LensMappingMode`, `PreservedStructure`, `LostStructure`, and any `ScaleWindow?` or `CoarseGrainingRule?`. |
| Support basis | What supports this declared lens use? | `LensSupportPosture`, validation overlay when live, and neighboring evidence or assurance patterns when their claims are live. |
| Use posture | What can the working reader now do, and what remains blocked? | `admissibleUse`, `nonAdmissibleUse`, `AdmissibleNextMove`, `StopCondition`, and named neighboring FPF loci. |

`LensMappingMode` names construction, not permission. Typical local values include `representation`, `abstraction`, `quotient`, `coarse-graining`, `embedding`, `homomorphism`, `isomorphism`, `functor-like transfer`, `simulation substrate`, and `learned or fitted representation`. A broad family name such as graph, field, category, geometry, quantum-like, variational, or Bayesian is only a prompt until the concrete construction and preserved/lost structure are named.

`LensSupportPosture` grants only limited use-rights:

| `LensSupportPosture` value | Allowed use | Blocked use |
|---|---|---|
| analogy-only prompt | orientation, hypothesis generation, recognition cue | decision, assurance, causal claim, or publication as established model |
| diagnosticOnly | finding a candidate obstruction, bottleneck, mismatch, missing state variable, or rival-lens split | prediction, decision, causal use, bridge substitution, assurance, or ontology without neighboring support |
| formal derivation inside accepted theory | local explanation or theorem-supported transfer when assumptions hold | empirical claim without observation or evidence |
| simulation | candidate model and scenario exploration | real-world causal or predictive reliance without validation |
| empirical fit | local prediction inside validation regime | out-of-regime generalization and causal use |
| accepted domain theory | local domain model use | cross-context ontology import |
| SoTA-echo candidate | structured exploration and lens-adequacy testing | accepted FPF law, assurance, release, or foundation claim |
| mechanized proof | formal property under assumptions | real-world adequacy unless assumptions, bridge, and evidence hold |

Use posture is not inferred from elegance, familiarity, source prestige, or mapping type. It is stated in `admissibleUse`, `nonAdmissibleUse`, and `StopCondition`. Mathematical adequacy is not empirical truth, causal support, bridge substitution, assurance, release confidence, decision sufficiency, or benchmark superiority; those claims need their governing neighboring FPF patterns.

#### C.29:4.4.2 - From lens to local action


Local action change from a mathematical lens is limited to these cases unless a neighboring pattern supports the needed non-C.29 use:

1. observe or measure a newly named variable or relation;
2. compare only under a declared structure and loss boundary;
3. diagnose a bottleneck, obstruction, mismatch, invariant, or failed transfer;
4. choose or reject a principal rival lens for the current local use;
5. narrow, downgrade, or block a tempting overread;
6. open the exact neighboring FPF locus when the live claim is causal, bridge, evidence, assurance, measurement, temporal, decision, work, scale, selector, or benchmark.

Each item closes either as a local C.29 output or as a named neighboring-pattern opening. If the needed result is a work plan, choice result, selector output, benchmark, or evidence record, publish that neighboring result in its governing pattern rather than from this list.

#### C.29:4.4.3 - No-lens entry: choosing a first candidate lens

Use this when the next admissible move can benefit from a mathematical lens but no adequate mathematical object has been named. The output is `MLA.LensCandidateNote`, not `MLA.OneLine` and not a full card. State the `ProblemStructureCue`, choose one cheap `CandidateLensFamily`, say what it could make visible, name the `ObservableOrControllableCue?` when available, state the `AdmissibleNextMove`, compare it with the `OrdinaryRivalOrFallback`, and stop if no action changes. If the cue is still pre-articulation and no stable `ProblemStructureCue` can be named, do not mathematize it; preserve cue plurality through `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state locus before returning to `C.29`.

Candidate guidance rows are examples for first recognition. Use the row that fits the working cue, or state a closer local cue using the same fields.

| `ProblemStructureCue` | Cheap `CandidateLensFamily` | First admissible move and stop |
|---|---|---|
| waiting, backlog, bottleneck, or throughput | queue or flow network | Observe arrivals, work in progress, service time, wait time, and bottleneck candidate; do not infer obligation, motivation, or managerial authority from the queueing lens alone. |
| state change, trajectory, stabilization, or control pressure | state-space, dynamics, Markov, ODE, or control lens | Name state, transition law, observation map, and validity window; return dynamics semantics to `A.3.3` and temporal-use claims to `C.27` when live. |
| dependency, interface, composition, or transfer failure | graph, hypergraph, category, operad, or compositional lens | Expose edges, edge meaning, slots, interfaces, composition law, and failed transfer; use `F.9` when cross-context meaning or substitution is live. |
| local-to-global boundary relation, conservation across a boundary, or source/sink balance | Stokes-like, exterior-derivative, divergence, flux, or boundary-operator lens | Name the domain, boundary, local rule, boundary condition, and conserved or sourced quantity; do not infer mechanism, evidence, or bridge safety without the neighboring pattern. |
| local rule that cannot become a global solution, or a transfer blocked by topology | cohomology, closed/exact, obstruction, or failed-extension lens | Name the local closure condition, global witness that fails, obstruction class or equivalent diagnostic boundary, and the blocked claim. |
| comparison, similarity, distribution shift, population movement, or shape change | metric-space distance, topology, embedding, or optimal-transport lens | Declare what distance, neighborhood, order, embedding, coupling, or transport cost preserves and what it loses; use `C.16` for comparability and measurement construction when live. |
| scale transition, coarse behavior, universality, knee, fixed point, or basin-of-attraction cue | coarse-graining, RG, fixed-point, or scaling-law lens | Name scale variable, scale window, coarse-graining rule, fixed point or attractor, basin/regularity condition, and invariants; use `C.18.1` for scale-law adequacy and `C.19.1` when scale advantage or BLP preference is live. |
| invariance under transformations, coordinate changes, or conservation-like claim | symmetry, group action, Noether-like, invariant, or equivariant representation | Identify the transformations, invariant or conserved quantity, assumptions, distinctions preserved, and coordinate details lost; do not import physical conservation without evidence. |
| extremal behavior, trade-off, dual view, potential, or cost/resource relation | variational, Lagrangian/Hamiltonian, action/energy/free-energy, Legendre, convex-duality, or constrained-optimization lens | Name the functional, variation space, constraints, boundary conditions, stationarity/extremum condition, dual transform, and what the dual view makes visible. |
| self-reference, universal evaluator, complete-language claim, closure paradox, or impossible total method | diagonal, fixed-point theorem, no-go, or self-application lens | Name the encoding, evaluator/self-map, diagonal move, universal claim tested, and exact closure or impossibility boundary; do not turn every loop into a no-go theorem. |
| uncertainty, information value, missing observation, active probe, or next sample choice | probabilistic, information-theoretic, BED/OED, active-learning, or Bayesian-optimization lens | Name the variables/distribution, utility or information criterion, design variable, acquisition candidate, model assumptions, estimation method, validation boundary, and robustness posture. |
| intervention, policy effect, or counterfactual question | SCM, causal graph, or causal abstraction lens | Name the causal object, intervention or assignment, outcome readout, and whether counterfactual structure is preserved, approximated, or not claimed; keep causal-use support with `C.28`. |
| learned scientific representation, latent state, surrogate solver, or operator view | neural operator, latent representation, surrogate solver, or world-model lens | Add the observation map, data or training regime, validation slice, generalization claim, uncertainty or approximation note, and stop condition. |
| probe effects, order effects, context effects, incompatible frames, or measurement-as-intervention | quantum-like or contextual-probability lens | Use `C.26` for quantum-like adequacy when order/probe/context effects are actually live; block physical quantum ontology unless separate physics evidence is supplied. |

`MLA.LensCandidateNote` is local first-candidate guidance. It does not replace `G.2` SoTA synthesis, tradition mapping, or broad lens-family review. Use `G.2` when the live work is tradition-scale source synthesis; use `C.29` when the local need is to choose one cheap candidate lens that changes the next admissible move. The cheap observation and control check does not open `C.16` or `A.10` by default; it only asks what the user can observe, read out, assign, vary, or validate now. Measurement construction, evidence strength, intervention support, or validation still moves to the neighboring pattern when live.

#### C.29:4.4.4 - First honest C.29 entry cases

For E.11-style first-entry recognition, distinguish the working entry case before choosing an output:

| First honest entry case | What the working reader met | First `C.29` answer |
|---|---|---|
| Pre-articulation cue | Something feels structurally wrong, but it is not yet a claim and no stable `ProblemStructureCue` can be named. | Do not force a mathematical lens. Use `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state locus first; return to C.29 only when the problem structure is stable enough. |
| No lens or under-lensed problem | A problem situation is stable enough for mathematical help, but no mathematical substrate has been named. | Use `MLA.LensCandidateNote`: `ProblemStructureCue` -> `CandidateLensFamily` -> `AdmissibleNextMove`. |
| Under-specified lens | A phrase such as field-like, graph-like, or quantum-like appears, but no object, mapping, preservation, or loss is stated. | Write `MLA.OneLine` or downgrade to ordinary prose. |
| Useful lens with overread | The lens is useful, but the text turns it into ontology, evidence, causality, assurance, bridge, or release support. | Use `MLA.MiniCard` or `MLA.FullCard` and name blocked use plus neighboring governing locus. |
| Ordinary local math | A Markov kernel, ODE, graph data structure, or accepted domain theory appears inside its local domain use. | Return `NoMLANeededNote` and stay with the local pattern. |
| Wrong first pattern | The reader reaches for `C.26`, `F.9`, `C.28`, `C.16`, or `A.3.3` before knowing whether mathematical-lens adequacy is live, or reaches for `C.29` when a neighbor already governs. | Name the first governing locus and state what `C.29` contributes, if anything. |

#### C.29:4.4.5 - False-positive bank and entry stops

Do not open `C.29` for these non-use cases unless a separate lens-transfer, publication, assurance, bridge, comparison, or reusable-explanation claim becomes live:

- ordinary ODE inside accepted physics or local engineering model;
- Markov kernel inside accepted stochastic dynamics;
- graph used as a local data structure;
- metric-space distance, topology, order, product, subspace, or embedding declared inside `A.19` `CharacteristicSpace` with no domain-transfer claim;
- category-theoretic proof internal to a domain where that formalism is the local theory;
- one-off pedagogical metaphor not reused for decision, evidence, assurance, publication, bridge, comparison, or transfer.

False-negative bank: open `C.29` even when no polished mathematical buzzword appears if the working problem has a structure that changes an admissible next move and ordinary prose is currently hiding it.

| False-negative situation | Why `C.29` is live | Cheap move |
|---|---|---|
| “Something is off, but we cannot yet say whether it is flow, priority, meaning, or evidence.” | The cue is not stable enough for `ProblemStructureCue`. | Stay in language-state work first; do not make C.29 create a mathematical lens from an unstable cue. |
| “We have many tasks waiting, but cannot see where flow slows.” | Queue or flow structure can expose bottleneck and WIP boundary. | Use `MLA.LensCandidateNote` for queue/flow; estimate arrivals, service, waiting, and bottleneck. |
| “This comparison feels important, but distance is unclear.” | Metric-space distance, topology, embedding, or transport adequacy is live. | Name what comparison preserves and loses before using the comparison. |
| “We transfer a structure between contexts because it looks the same.” | Mathematical-lens adequacy and bridge loss are live. | Name preserved/lost structure and use `F.9` when cross-context meaning or substitution is live. |
| “A latent space is used as a scientific explanation.” | Learned-lens overread is live. | Name observation map, validation slice, generalization boundary, and stop causal or ontology overread. |
| “The method scales because the mathematics is elegant.” | Scale-law adequacy or BLP preference claim is live. | Name scale variable/window and use `C.18.1` or `C.19.1` when scale advantage is claimed. |

Entry guidance states when `C.29` is the first governing locus and when another pattern is first:

| Entry situation | First governing locus | Tempting wrong first locus |
|---|---|---|
| mathematical-lens adequacy inside a phrase such as "market is a field" | `C.29` | `C.26`, `F.9`, or `A.3.3` before lens adequacy is checked |
| explanation-facing rendering that uses a mathematical lens | `E.17.EFP`; `C.29` only for the mathematical-lens adequacy part when that lens affects explanation use | `C.29` as the first pattern for every explanation |
| bounded comparative review unit with a mathematical comparison basis | `E.17.ID.CR`; `C.29` only for lens adequacy or rival-lens support | `C.29` as the comparison or adjudication record |
| same-described-entity representation-scheme transition | `A.6.3.RT`; `C.29` only if the transition imports a contested or use-affecting mathematical lens | `C.29` for every table, diagram, geometry, or notation shift |
| coarsened rendering useful only under narrower admissible use and source-bearing reopen | `A.6.3.CSC`; `C.29` only if the coarsening depends on mathematical abstraction or coarse-graining | `C.29` as source-bearing return or bridge support |
| within-context representation adequacy | `C.29` | `F.9` when no cross-context meaning claim is live |
| quantum-like dashboard or probe-order claim | `C.26` plus `C.29` compatibility | physical quantum ontology |
| graph state space | `A.19` or `A.3.3` unless lens transfer is explicit | `C.29` for every graph word |
| category bridge across contexts | `F.9` plus `C.29` adequacy relation | duplicate bridge semantics inside `C.29` |
| prediction, rate, trajectory, recovery, convergence, or rhythm claim | `C.27` when temporal adequacy is live; `C.29` only for lens adequacy | treating a mathematical prediction cue as enough for temporal-use support |
| decorative scale language | no `C.18.1` or `C.19.1` unless scale behavior is live | scale-law review for every scale word |

Admissible entry stops are: no MLA needed, MLA one-line opened, or neighboring governing pattern selected.

#### C.29:4.4.6 - Governing-locus boundary table

A receiving `C.29` application uses this governing-locus discipline so mathematical-lens adequacy stays in the C.29 discipline rather than becoming a second authority over neighboring claims.

Positive governed claim:

> A C.29 application gives a pattern-local adequacy discipline for claims that use a mathematical object, formalism, learned representation, simulation substrate, or mathematical family as a mathematical lens for a stated use. The application asks for candidate mathematical object, lens mapping mode, preserved and lost structure, visible invariant or distinction, `LensSupportPosture` or validation posture, admissible use, non-admissible use, and stop condition.

Boundary transfer rule: when the live claim is a choice result, work plan, evidence path, assurance tuple, explanation rendering, comparative review unit, representation shift, temporal claim, bridge, causal-use claim, measurement claim, scale-law claim, selector, or benchmark, the `NeighborGoverningLocusNote` names the exact receiving FPF locus and exact project-side record. A C.29 application can contribute a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note that the receiving record can cite; it does not create that neighboring record.

| Live object or claim | Governing FPF locus | MLA adequacy contribution |
|---|---|---|
| mathematical-lens adequacy | `C.29` | Names the MLA discipline: candidate mathematical object, lens mapping mode, preserved/lost structure, invariant or distinction, `LensSupportPosture`, admissible use, non-admissible use, and stop condition. |
| durable reusable names beyond pattern-local fields | `F.18` | Cite when `MLA` names become durable beyond C.29-local use. |
| broad wording and epistemic precision restoration | `E.10`, `C.2.P` | Obey head-kind, register, and epistemic precision-restoration discipline. |
| relation precision, arity, polarity, and slot structure | `A.6.P`, `A.6.5` | Apply only if relation substrate becomes representation affecting the stated use. |
| object, description, and carrier distinction | `A.7` | Do not identify the phenomenon directly with the mathematical object. |
| dynamics state space and transition law | `A.3.3` | Assess imported or contested lens adequacy; do not govern dynamics semantics. |
| `CharacteristicSpace`, slots, topology, order, and metric-space distance overlays | `A.19` | Apply only when an overlay becomes a domain-transferring or publication-bearing lens. |
| `ChoiceResult`, local choice record, selected-set publication, option-selection claim, or selector/benchmark result | `C.11`; `G.5`/`G.9` when selected-set or benchmark publication is live | Can contribute a lens-supported prediction, distinction, obstruction, diagnostic boundary, or rival-lens note for the decision or selector record. |
| selected method, method-family selection, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant source restoration | `A.15`, `A.15.1`, `A.15.4` | Can contribute method-relevant lens adequacy; method, plan, performed-work, and source-restoration records stay with the A.15 family. |
| evidence path, source currentness, provenance, evidence carrier, or model card/datasheet used as evidence | `A.10` | States `LensSupportPosture` only; evidence paths and provenance remain A.10 matters. |
| assurance, readiness, reliability, release confidence, safety, trust, or engineering justification | `B.3` plus relevant G patterns when live | Treats lens adequacy as possible input only; mathematical elegance does not raise assurance. |
| measurement construction, scale/unit/comparability, or evidence-stub adequacy | `C.16` | States measurement-dependent `LensSupportPosture` only; measurement construction, scale/unit/polarity, direct comparability, and evidence-stub adequacy stay with `C.16`. |
| explanation-facing rendering or generated explanation use | `E.17.EFP` | States mathematical-lens adequacy for the mathematical explanation used inside the rendering; explanation-use discipline stays with `E.17.EFP`. |
| bounded comparative review unit | `E.17.ID.CR` | States lens adequacy for a mathematical comparison basis or rival lens when that basis affects the comparative review use. |
| same-described-entity representation-scheme transition | `A.6.3.RT` | Applies only if the representation shift imports a contested or use-affecting mathematical lens. |
| coarsened rendering with narrower admissible use and source-bearing reopen | `A.6.3.CSC` | Applies only if the coarsening depends on mathematical abstraction, quotienting, or coarse-graining. |
| cross-context meaning, bridge kind, direction, CL, loss, and substitution | `F.9` | Reference Bridge; do not duplicate Bridge Card semantics. |
| causal-use support | `C.28` | Block causal overread or cite a `C.28` application or support record. |
| forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, temporal window, or rate-change used as sufficient for a use | `C.27` | Can state that a mathematical lens supports a prediction or distinction; temporal-claim adequacy stays with `C.27`. |
| scale-law and Bitter-Lesson preference claims | `C.18.1`, `C.19.1` | Cite scale-window or BLP evidence when scale behavior or scale advantage is live. |
| quantum-like modeling | `C.26` | Treat `C.26` as MLA-compatible specialization, not as full-card inheritance for every QL-lite note. |
| selectors, benchmarks, parity, SoTA packs, and model-selection publications | `G.5`, `G.9`, `G.2`, `G.10` | Selector or benchmark records govern publication and evaluation; an MLA card can contribute lens adequacy for a selector or benchmark input only. |


#### C.29:4.5 - `MLA.Card@Context` shape

`MLA.Card@Context` is a pattern-local card in `C.29`. It is not `U.MLACard`, `U.LensAdequacyRecord`, or any universal `U.*` kind.


Namespace note: `MLA.Card@Context`, `MLAOutputRef`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, and `CC-MLA-*` are `C.29`-local instruments unless they cite existing FPF kinds or refs. `MLAOutputRef` references the applicable `C.29` output for the stated use; it is not a demand for `MLA.FullCard`. Do not mint generic suffixes such as `SystemMLA`, `MLAQuality`, or `MLACompliance`. Durable cross-pattern MLA names, records, or refs require explicit mint/reuse and naming/admission support through `F.8`, `F.18`, `C.3`, and `E.9`; otherwise they remain pattern-local labels.

Read the MLA card through three aspects:

| Aspect | Fields or refs | Boundary |
|---|---|---|
| Mathematical substrate | `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `InvariantsExposed` | Names the representation; does not identify the phenomenon with the mathematical object. |
| Support and validation | `LensSupportPosture`, `ValidationUseOverlayRef?`, `LearnedLensOverlayRef?`, failure case, uncertainty or approximation note | States support for this use; does not create an evidence path, benchmark result, assurance, or release confidence. |
| FPF use and boundaries | `admissibleUse`, `nonAdmissibleUse`, `StopCondition`, `BridgeRefSet?`, `CausalUseDisposition?`, `AssuranceUseDisposition?`, `ExportPolicyRef?` | States what the reader may do and where neighboring FPF loci carry live claims. |

Validity boundary: mathematical validity of the object under its assumptions is not the same as representational adequacy to the phenomenon; representational adequacy is not empirical validation for a use; empirical validation is not causal-use support; causal-use support is not assurance, release confidence, decision sufficiency, or benchmark superiority.


```text
MLA.FullCard base fields:
MLA.Card@Context := {
  TargetPhenomenon,
  describedEntityRef?,
  BoundedContext,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  InvariantsExposed,
  LensSupportedPredictionOrDistinction?,
  LensSupportPosture,
  admissibleUse,
  nonAdmissibleUse,
  StopCondition
}
```

Conditional fields apply only when the corresponding neighboring claim, claim-bearing use, or publication use is live:

```text
MLA.FullCard conditional fields := {
  DynamicsRef?,
  TransitionLawRef?,
  ObservationMapRef?,
  ScaleWindow?,
  CoarseGrainingRule?,
  SourceReturnCondition?,
  PublicationUsePosture?,
  PrincipalRivalLens?,
  RivalLensSet?,
  RivalLensRelation?,
  ValidationUseOverlayRef?,
  LearnedLensOverlayRef?,
  BridgeRefSet?,
  CausalUseDisposition?,
  AssuranceUseDisposition?,
  ExportPolicyRef?
}
```

**Plain reading of the card.** A useful mathematical lens says: what phenomenon is being seen, through which mathematical object, by what mapping, what survives, what is lost, what becomes visible, what support posture and validation boundary support this use, the now-admissible user move, the blocked user inference, and where the lens stops.


#### C.29:4.5a - Conditional overlays

The base card stays light. These overlays are used only when their use is live. Ordinary C.29 use does not fill this block; it escalates here only when the claim is already publication-facing, assurance-input, benchmark, bridge, model-selection, prediction, scientific/model, learned-lens, or causal-use facing.


```text
MLA.ValidationUseOverlay@Context :=
⟨
  ClaimUse,
  ValidationRegime,
  EvaluationSlice,
  ApproximationOrUncertaintyNote,
  KnownFailureCaseOrCounterexample,
  SensitivityOrRobustnessNote?,
  DomainOfApplicability,
  OutputChangeCondition?
⟩
```

Use the validation overlay when the lens supports prediction, publication, assurance input, benchmark use, model selection, or scientific/model claim. `LensSupportPosture` alone is then insufficient. Keep the neighboring notions separate: verification is proof or formal checking under stated assumptions; validation is fit for a declared use and regime; calibration aligns model parameters or readouts with observations; explanation states why the lens makes a distinction intelligible. The C.29 output does not let any one of these four labels silently stand in for the others.

```text
MLA.LearnedLensOverlay@Context :=
⟨
  DataOrTrainingRegime,
  ObservationMapRef,
  GeneralizationClaim,
  DiscretizationOrResolutionPolicy?,
  ValidationRegime,
  ApproximationOrUncertaintyNote,
  StopCondition
⟩
```

Use the learned-lens overlay when the mathematical object is fitted, learned, latent, simulation-trained, data-derived, a neural operator, a surrogate solver, an embedding, or a world-model representation.

Learned-lens stop variants are named explicitly when they are tempting:

| Tempting overread | Stop condition form |
|---|---|
| out-of-distribution generalization | no generalization outside the declared validation regime |
| causal mechanism | no causal mechanism claim without `C.28` and evidence support |
| latent dimension ontology | latent coordinate or factor is not an entity kind without separate ontology and evidence |
| unobserved-variable recovery | no recovery of hidden variables beyond the declared observation map and validation slice |
| benchmark superiority | no benchmark or selector superiority outside the declared evaluation slice and relevant `G.*` record |
| assurance or release use | no assurance, release, or reliability use without `A.10`, `B.3`, and relevant G-pattern support |


```text
MLA.CausalAbstractionCheck@Context :=
⟨
  LensMappingMode,
  InterventionStructureStatus ∈ {preserved, approximated, notClaimed},
  CounterfactualUseStatus ∈ {preserved, approximated, notClaimed},
  C28ApplicationRef?
⟩
```

This is not a first-class causal abstraction card. It is a lightweight check: when `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation, and `admissibleUse` would include intervention, policy, counterfactual, or causal explanation, apply `C.28` for causal-use support.

#### C.29:4.5b - Repair decision table

| Failed or missing item | Required repair |
|---|---|
| no `CandidateMathObject` | If the problem still needs a mathematical lens for the next move, first name the `ProblemStructureCue` and write an `MLA.LensCandidateNote` with the cheapest candidate lens family and admissible next move; downgrade to ordinary prose or remove the mathematical claim only when no candidate lens changes action. |
| no `LensMappingMode` | Choose a lens mapping mode or downgrade to analogy-only prompt. |
| no `PreservedStructure` | Remove the claim-bearing mathematical phrase. |
| no `LostStructure` | Add a loss note, downgrade, or support an equivalence or isomorphism claim. |
| no invariant, obstruction, distinction, or payoff | Keep the phrase as didactic recognition cue or orientation-only. |
| no `LensSupportedPredictionOrDistinction` where decision, prediction, or model selection is live | Block decision or assurance use; downgrade to analogy-only if no supported consequence exists. |
| evidence is analogy-only | Block decision, publication-as-established-model, assurance, release, and causal use unless evidence, validation, causal-use support, or assurance support is supplied by its governing pattern. |
| no `LensSupportPosture` | Block decision, publication, assurance, benchmark, and release use. |
| causal, intervention, policy, or counterfactual overread | Apply `C.28` or block causal use. |
| cross-context meaning, export, or substitution overread | Apply `F.9` or block export and substitution. |
| scale, universality, knee, exponent, or scale-advantage claim | Apply `C.18.1` or `C.19.1`, or keep the lens local and bounded by stop condition. |
| assurance or release use | Apply `A.10`, `B.3`, or relevant G patterns, or block assurance use. |
| `StopCondition` is generic | Name the most tempting nearby overread the lens does not license. |

#### C.29:4.6 - Field meanings

| Field | Meaning selected for `C.29` | Boundary guard |
|---|---|---|
| `TargetPhenomenon` | Plain entry prompt naming the phenomenon or situation to be understood. | Not a `U.Kind`, not a described-entity slot, and not a publication object. |
| `describedEntityRef?` | Exact reference used when the lens appears inside a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. | Required only when the lens appears in claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. |
| `BoundedContext` | Context in which the lens is claimed to work. | Cross-context use cites `F.9`. |
| `CandidateMathObject` | Concrete mathematical object, structure, formal role, learned representation, or local formalism. | Broad family labels are prompts until narrowed. |
| `LensMappingMode` | `C.29`-local lens mapping mode. | Does not replace `F.9` BridgeKind, `A.6.P` `RelationKind`, `C.3` kind, or domain relation kinds; cross-context transfer uses `F.9` when bridge semantics are live. |
| `PreservedStructure` | Structure the lens carries into the declared use. | No preserved structure means the mathematical phrase cannot carry the stated use. |
| `LostStructure` | Structure the lens drops, abstracts away, or cannot support. | Empty loss requires explicit equivalence or isomorphism support. |
| `InvariantsExposed` | Invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, or other payoff. | If no payoff is visible, downgrade to recognition cue. |
| `ObservableOrControllableCue?` | Cheap cue naming what can be observed, read out, assigned, varied, or validated before a candidate lens can change action. Examples include arrivals, work in progress, service time, wait time, edge meaning, intervention assignment, outcome readout, observation map, validation slice, scale variable, or scale point. | Not a measurement construction, evidence record, causal-support result, or validation verdict. Open `C.16`, `A.10`, `C.28`, or `A.3.3` when those claim types are live. |
| `ObservationOrReadoutNeeded?` | Optional one-line note naming the observable, readout, assignment, outcome, validation slice, or scale point still needed before the lens supports the stated admissible move. | If this missing item carries measurement, evidence, causal, dynamics, or validation force, the neighboring pattern governs that neighboring work. |
| `LensSupportedPredictionOrDistinction?` | Required when prediction, decision, method selection, model selection, or publication-as-model is live. | Not required for orientation-only use. |
| `DynamicsRef?`, `TransitionLawRef?` | References to `A.3.3`-owned dynamics when dynamics semantics are live. | `C.29` does not own dynamics. |
| `ObservationMapRef?` | Probe, readout, or observation map when observation makes the lens admissible for the declared use. | Required for learned or measurement-dependent lenses when live. |
| `ScaleWindow?`, `CoarseGrainingRule?` | Scale range and coarse-graining or compression rule when scale behavior, macro/effective description, universality, coarse behavior, latent compression, or renormalized description is live. | `C.18.1` and `C.19.1` carry scale-law and BLP evidence; the C.29 output states only how the lens remains adequate inside the declared window. |
| `SourceReturnCondition?` | Condition under which the reader must return from the compressed or coarse description to the source-side variables, observations, cases, or mechanisms. | Required only when abstraction, coarse-graining, compression, latent representation, or macro-modeling drops source-side distinctions that could matter to the stated use. |
| `PublicationUsePosture?` | Optional note for publication-facing use: `orientationOnly`, `explanationFacing`, `comparisonInput`, `decisionInputCandidate`, `benchmarkInput`, `assuranceInputCandidate`, or `reusableModelPublication`. | Does not publish, release, benchmark, assure, or decide anything by itself; the neighboring publication, benchmark, evidence, decision, and assurance loci still govern those claims. |
| `OutputChangeCondition?` | Condition under which the current C.29 output must be narrowed, demoted, replaced, retired from claim-bearing use, or supported by a neighboring FPF locus. | Not a process log or standing status record; it states a result boundary for the current lens use. |


| OrdinaryRivalOrFallback | Ordinary prose, accepted local theory, direct measurement, or simpler neighboring-pattern exit the reader would use without this lens. | Required for cheap outputs; prevents prestige bias before broad rival review. |
| `PrincipalRivalLens?` | Default ordinary or most relevant rival lens. | Preferred over a broad literature survey. |
| `RivalLensSet?` | Broader comparison set only when publication, selection, or claim-bearing comparison is live. | Not a `G.5` selector, benchmark harness, or parity result. |
| `RivalLensRelation?` | Declared relation between the current lens and the principal rival or live rival set. Allowed local relation values include `ordinaryFallback`, `complementary`, `sameUseLowerCost`, `morePreservedStructureHigherCost`, `lowerErrorOnDeclaredEvaluationCriterion`, `clearerExplanationForDeclaredReader`, `bridgeNeedsF9`, `causalUseNeedsC28`, `differentScaleWindow`, `differentLossProfile`, `incomparableForCurrentUse`, `blockedByStopCondition`, and `unresolved`. Examples: a queueing lens and a causal lens can be complementary for different moves; a latent manifold and a causal graph can conflict when latent axes are read causally; an RG-like lens and a micro-dynamics lens can have different scale windows. | Names disagreement only; a C.29 output is not a winning-lens choice, literature review, selector result, benchmark result, or parity result. Any superiority claim names the evaluation criterion, reader, cost, scale window, or receiving pattern that makes the comparison admissible. |

| `LensSupportPosture` | Local support-posture label. | Not evidence, an EvidenceGraph, a PathId, or an assurance score. |
| `BridgeRefSet?` | Reference to `F.9` Bridge material when context crossing is live. | Bridge semantics stay with `F.9`. |
| `CausalUseDisposition?` | One of `noCausalUseClaim`, `causalUseBlocked`, `C28ApplicationRef`, or `C28SupportRecordRef`. | No causal-reference shortcut; no causal verdict from `C.29`. |
| `AssuranceUseDisposition?` | One of `noAssuranceUseClaim`, `assuranceUseBlocked`, `evidenceInputOnly`, `A10Ref`, or `B3ApplicationRef`. | No assurance verdict from mathematical elegance. |
| `admissibleUse` | Admissible current use of the lens. | Matches evidence and validation posture. |
| `nonAdmissibleUse` | Tempting neighboring use that is blocked or handed to another governing locus. | Names the neighboring pattern when live. |
| `StopCondition` | Most tempting nearby claim the lens does not license. | Main anti-overread output; not boilerplate. |
| `ExportPolicyRef?` | Governed reuse or export policy when publication or downstream reuse is live. | Not required for local orientation or mini-card use. |

### C.29:5 - Neighboring-pattern boundaries

Neighboring patterns remain necessary and are not displaced. A retained neighboring-pattern relation note answers the working question for the neighboring pattern being used: what does the reader do with the mathematical lens now? State the neighboring-pattern trigger and the first admissible move for that neighboring pattern. If a note only repeats that C.29 does not replace a neighbor, keep that boundary in the C.29 governing-locus table instead of copying generic boundary prose into the neighboring pattern:

- `A.6.P` handles relation precision restoration.
- `A.3.3` handles dynamics semantics.
- `A.19` handles characteristic spaces, overlays, normalization, and comparability.
- `F.9` handles cross-context semantics and Bridge loss.
- `C.18.1` and `C.19.1` handle scale-law and BLP claims.
- `C.26` handles one specific quantum-like lens family.
- `C.28` handles causal-use admissibility.
- `A.10` and `B.3` handle evidence and assurance.
- `C.11`, `A.15`, `A.15.1`, and `A.15.4` handle choice results, method/work separation, work plans, performed work, and work-relevant source restoration.
- `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, and `A.6.3.CSC` handle explanation-facing renderings, bounded comparative review units, same-described-entity representation-scheme transitions, and controlled semantic coarsening.
- `C.27` handles temporal-claim adequacy.

Use the C.29 discipline when the live question is: **Is this mathematical lens adequate for this declared use, and where does it stop?**

### C.29:6 - Naming, ontology, and epistemic precision-restoration account

#### C.29:6.1 - Name

Name: `C.29 — Mathematical Lens Adequacy (MLA)`.

Abbreviation: `MLA` = **Mathematical Lens Adequacy**. No prior temporary code is reused; the pattern code, card prefix, reference prefix, and checklist IDs use only `MLA`.

The stable name is `Mathematical Lens Adequacy` because `C.29` governs adequacy for a declared use, not strength on an unnamed scale. Plain prose can still say that a useful mathematical lens compresses many cases while preserving declared distinctions; load-bearing use is recovered through `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensSupportPosture`, and `StopCondition`.

#### C.29:6.1a - C.29-local naming guard

`MLA.*` instruments are `C.29`-local unless separately admitted. They are not `U.*` kinds, not durable FPF record families, and not substitutes for `U.Kind`, `KindSignature`, `KindBridge`, `BridgeCard`, `EvidenceGraph`, `ChoiceResult`, `U.WorkPlan`, `U.Work`, or assurance records.

Do not mint `LensKind`, `MathematicalLensKind`, `MLAQuality`, `MLACompliance`, or `MLARecord` from `C.29` use.

When one `C.29` application needs a mathematical-lens name to become reusable outside that application, use `F.18` local-first naming; when it quantifies over a class of described entities, use `C.3` Kind-CAL; when it creates or reuses a durable concept or record family, use `F.8` mint/reuse and `E.9` design-rationale support.

#### C.29:6.2 - Tempting wrong names rejected

| Tempting name | Reason rejected |
|---|---|
| `Mathematical Ontology Principle` | Smuggles the metaphysical claim `C.29` rejects. |
| `Single-Foundation Math Posture` | Would collapse plural lens families into one foundation claim; C.29 instead tests each selected family by declared mapping, local use, and recoverable loss. |
| `Math Metaphor Adequacy` | Too narrow and too vague; the selected answer is structure-preserving representation, not mere metaphor. |
| `Quantum-Like Generalization` | Misplaces the general pattern under one special lens. |
| `Category-Theoretic Bridge Pattern` | Over-privileges category theory; MLA is broader. |

#### C.29:6.3 - Ontology guard selected for FPF

> A physical, organizational, or epistemic phenomenon is not directly identified with a mathematical object; it is represented through a mathematical object by an explicitly declared mapping that preserves some structures and loses others.

#### C.29:6.4 - C.2.P recoveries applied

| Earlier wording risk | Recovered wording in `C.29` |
|---|---|
| `source` / `target` | Use `source-basis document`, `Basis used`, `describedEntityRef`, `receiving FPF pattern`, `BridgeRefSet`, or exact pattern reference as appropriate. |
| raw source intake as evidence | Recovered as source-basis text, not authority. Selected content is integrated through `C.29:13a`, `C.29:13`, and the field/checklist rows that carry its live claim. |
| `structure-preserving identification` | Rewritten to `structure-preserving representation / mapping` unless direct equivalence is explicitly the `LensMappingMode`. |
| Slash compounds such as `Dynamics/TransitionLaw?` | Rewritten as `DynamicsRef?` / `TransitionLawRef?`. |
| Procedure-like pattern-control language | Rewritten as `pattern application`, `Disposition`, `BridgeRefSet`, `C28ApplicationRef`, or `C28SupportRecordRef` only when that exact neighboring-pattern application or support record is live. |
| `ExportPolicy` | Split into `admissibleUse`, `nonAdmissibleUse`, and optional `ExportPolicyRef?`. |
| free strength qualifier | Replace with exact adequacy fields, evidence or scale basis, support posture, and stop-condition wording. |
| `model`, `lens`, `math` as prestige heads | Recovered as `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, and `LensSupportPosture`. |
| Causal or assurance implications | Recovered as `CausalUseDisposition?` and `AssuranceUseDisposition?`, with `C.28`, `A.10`, `B.3`, and G-patterns as neighboring governors. |

### C.29:7 - Rationale

#### C.29:7.1 - Why this improves FPF

The selected first-principles posture in `C.29` is operational, not metaphysical. It treats first-principles mathematical thinking as local construction discipline: declare the smallest structure, rule, invariant, resource condition, observation, or consistency boundary from which the next move follows or is blocked. In that sense, a `C.29` application puts mathematical construction before adequacy control: the reader can introduce a queue, graph, state space, measure, topology, algebraic structure, variational quantity, simulation substrate, or learned representation when that structure improves the work, and then record the mapping, preserved structure, lost structure, support posture, and stop condition.


First-principles support can come from several families without turning any one family into an FPF-wide foundation: signatures, logics, axioms, type or abstraction distinctions, symmetries, invariants, compositional structure, local-global relations, scale relations, boundary conditions, variational principles, action, energy, free-energy, loss, or value functionals, constrained optimization structure, probability, information, typicality, algorithmic construction, resource bounds, implementation constraints, consistency boundaries, causal or intervention-preservation questions, operator or function-space mappings, and admissible observation maps. Each use still needs declared mapping, preserved structure, lost structure, validation or support posture, and stop condition.


This fits FPF because FPF already commits to state explicitness, bounded contexts, evidence and assurance, cross-context bridges, open-ended evolution, SoTA alignment, notational independence, and avoidance of ornamental formalism.

`C.29` makes an existing discipline explicit: when FPF uses a mathematical substrate as a mathematical lens for a stated use, the `C.29` application declares what the substrate preserves, what it loses, what it makes visible, which rival lenses remain live, and where its admissible use stops.


The compact Plain line remains useful because it points to a real heuristic: good mathematical lenses are not decoration; they are compact ways of seeing structures that survive transfer. The Plain line stays readable, while the card and checklist carry the exact FPF commitments.


#### C.29:7.2 - Alternatives rejected

| Alternative | Why rejected |
|---|---|
| Keep only local math-lens hooks | Leaves no general conformance carrier; `C.26`-style guardrails do not transfer to non-QL lenses. |
| Add only a paragraph to `A.6.P` | Overloads relational precision restoration with general modeling adequacy. |
| Add only a paragraph to `F.9` | Bridge discipline is about cross-context semantics; MLA also governs within-context mathematical representation. |
| Treat Vanchurin as a new FPF foundation | Too speculative and ontology-bearing; selected source stance is candidate lens only. |
| Treat Sandberg thread as a foundations list | Useful recognition cue, but not a proof source, closed taxonomy, or FPF law. |
| Require a fixed list of permitted lens families | Would make first repair depend on list membership instead of declared structure, loss, and admissible use. |
| Make mechanized proof mandatory for MLA | Too narrow. Mechanized proof can be one `LensSupportPosture`, but adequacy can also rest on accepted domain theory, formal derivation, simulation, or empirical fit. |

#### C.29:7.3 - Pillar impact analysis

| Pillar | Impact |
|---|---|
| `P‑1 Cognitive Elegance` | Positive: first-principles structure becomes visible without ornamental formalism; one adequacy card replaces many prestige metaphors while example rows stay subordinate to declared fields and admissible use. |
| `P‑2 Didactic Primacy` | Positive: first-minute use starts with the useful question "what structure changes the next move?", then Plain wording remains backed by recoverable Tech fields. |
| `P‑3 Scalable Formality` | Positive: supports maturation from ordinary cue to candidate lens, one-line repair, formal derivation, validation posture, or evidence-backed domain theory. |
| `P‑4 Open‑Ended Kernel` | Positive if placed in Part C, not Kernel; avoids making any mathematical family or foundation a kernel axiom. |
| `P‑5 FPF Layering` | Positive: `C.29` becomes a modular parent/coordinator for specific mathematical lenses while neighboring patterns keep their own authority. |
| `P‑6 Lexical Stratification` | Positive: separates Plain "lens" from technical `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `StopCondition`, and evidence fields. |
| `P‑7 Pragmatic Utility` | Positive if every MLA result changes a supported prediction, distinction, obstruction, model choice, diagnostic boundary, or stop condition. |
| `P‑8 Cross‑Scale Consistency` | Positive: scale windows, coarse-graining, local-global relations, composition, dynamics, symmetry, and boundary conditions become declared rather than assumed. |
| `P‑9 State Explicitness` | Positive: state, observation, dynamics, measurement, support posture, and stop-condition fields cite `A.3.3`, `A.19`, `C.16`, and `A.10` when live. |
| `P‑10 Open‑Ended Evolution` | Positive: new lens families and first-principles modeling bases can be added without destabilizing Core. |
| `P‑11 SoTA Alignment` | Positive: admits current mathematical modeling, applied category theory, scientific machine learning, causal abstraction, learning-dynamics research, and plural foundations without over-adopting them. |


#### C.29:7.4 - Principle-taxonomy balance

| Lens | Reading |
|---|---|
| `Gov` | New mathematical-lens adequacy norms require `E.9` design-rationale discipline and SoTA discipline when they alter FPF norms. |
| `Arch` | Wrong carrier placement is blocked; `C.29` coordinates but does not replace neighboring patterns. |
| `Onto/Epist` | Representation, mapping, preservation, loss, and `LensSupportPosture` are explicit. |
| `Prag` | A useful lens produces a useful prediction, distinction, obstruction, or stop condition; otherwise it remains didactic prose. |
| `Did` | The card gives a small first-use check while experts can inspect exact field meanings. |

### C.29:8 - Consequences and validation harness

| Benefit | Cost or handling |
|---|---|
| FPF gains a general discipline for mathematical lens use while mathematical lenses stay tied to declared structure, declared loss, and admissible use. | Adds one new pattern; neighboring-pattern exits carry evidence, causal, bridge, assurance, work, decision, publication, and admission uses. |
| Existing specialized lenses such as `C.26` become easier to explain as special cases. | `C.26` needs only relation wording, not a rewrite of its core. |
| Authors get a small checklist before using terms such as field, quantum, category, RG, manifold, graph, or information geometry. | Some quick analogies will be downgraded to local prose; this is intended. |
| Vanchurin-like speculative work can enter as candidate-lens stress tests. | Requires strict Adapt-not-Adopt marking. |
| Cross-domain transfer becomes auditable through preserved/lost structure and stop conditions. | More upfront statement effort; reduces downstream epistemic precision repair. |
| `C.29` can stay readable rather than becoming a dry ontology form. | Requires a Plain/Tech discipline: Plain metaphors can guide reading, but Tech fields govern claim-bearing uses. |

#### C.29:8.1 - Validation harness for Stable admission and material refresh

For Stable admission or material refresh of `C.29`, run a small MLA validation harness. The harness is not a benchmark mandate and not a tool requirement. It is a repeatable admission check that the pattern yields correct first outputs, avoids false positives, preserves neighboring-pattern writing boundaries, and keeps the first useful move visible.

This subsection governs steward-side validation, not the ordinary C.29 user path. A working user applies the action path and chooses the cheapest honest output; they do not run the harness merely to decide between ordinary prose, `MLA.OneLine`, `MLA.MiniCard`, or a neighboring governing locus.

C.29 output-change conditions:

| New condition | Required result |
|---|---|
| validation slice fails, degrades, or no longer matches the stated regime | Change `LensSupportPosture` to the supported posture, update the failure case, narrow the admissible use, or block prediction-facing use. |
| a principal rival lens changes the next admissible move | Add `PrincipalRivalLens?` and `RivalLensRelation?`, or replace the current lens for that use. |
| the lens becomes decision-facing, publication-facing, assurance-input, benchmark, model-selection, prediction, or repeated cross-case support | Use `MLA.FullCard` and the applicable overlay or neighboring FPF locus. |
| source basis becomes outdated, contradicted, or demoted to background only | Change the `SourceBasisRole`, update the support posture, or retire the lens from claim-bearing use. |
| bridge, causal, measurement, scale, temporal, evidence, assurance, selector, or benchmark claim becomes live | Name the governing neighboring pattern and keep C.29 to the lens-adequacy part. |
| abstraction, compression, coarse-graining, or latent representation drops a distinction now needed for the declared use | Add `SourceReturnCondition?`, narrow the use, or block the compressed-lens claim. |

AI-assisted thin-echo result rule:

| Thin echo or query shape | Required result |
|---|---|
| `field-like`, `quantum-like`, `category-like`, `manifold`, `entropy`, `RG`, `graph`, `embedding`, or another mathematical prestige head appears alone | Do not answer from the family label. First name the live use or state that no C.29 use is live. |
| live claim is causal, measurement, bridge, evidence, temporal, work, assurance, selector, or benchmark-facing | Name the neighboring FPF locus before any C.29 output. |
| C.29 remains live after neighboring-locus check | Return at least `CandidateMathObject`, `PreservedStructure`, `LostStructure`, `AdmissibleNextMove`, and `StopCondition`, or downgrade to `LensCandidateNote` / `NoMLANeededNote`. |

C.29 edge-case boundary results:

| Edge case | Required result |
|---|---|
| mechanized proof of a model property | State assumptions and proven property; empirical evidence or assurance use stays with `A.10`, `B.3`, or relevant G patterns. |
| simulation-calibrated lens | Scenario exploration is allowed; prediction, decision, or counterfactual reliance needs validation and neighboring support. |
| latent-space visualization | Use learned-lens overlay and stop latent ontology, causal mechanism, or unobserved-variable recovery unless separately supported. |
| exact isomorphism or equivalence claim | Support the exact relation or downgrade `LensMappingMode`. |
| multi-lens composition | Name the principal lens and neighboring notes; avoid one giant full card that mixes queue, graph, causal, temporal, and assurance authority. |
| lens becomes accepted domain theory | Keep local domain theory with the domain pattern; durable FPF naming or kind change needs `F.18`, `C.3`, `F.8`, and `E.9`. |
| mathematical notation shift only | Use `A.6.3.RT` unless mathematical-lens adequacy changes the declared use. |
| coarsened explanation | Use `A.6.3.CSC` for source-bearing return, narrowed use, and coarsened rendering; cite C.29 only for abstraction adequacy. |

Harness shape:


| Field | Meaning |
|---|---|
| `CaseId` | Stable case id. |
| `InputPhrase` | The phrase or claim a cold user might write. |
| `ExpectedFirstPattern` | `C.29`, a neighboring pattern, or no MLA needed. |
| `ExpectedMLAOutputClass` | `NoMLANeeded`, `OneLine`, `MiniCard`, `FullCard`, or `NeighborGoverningLocusNote`. |
| `RequiredFields` | Minimal fields or overlays required. |
| `NeighborPatternRefs` | Exact neighboring governing loci when live. |
| `ExpectedRepair` | Downgrade, narrow, add loss, add validation, choose rival lens, or apply neighbor. |
| `ExpectedStopCondition` | Most tempting nearby overread blocked. |
| `ExpectedNonUseDecision` | Present only for false-positive cases. |

Minimum harness cases:

| Case | Expected result |
|---|---|
| “organization is quantum” | `C.26` plus `C.29` compatibility only if order or probe effects are live; otherwise downgrade to metaphor; physical quantum ontology blocked. |
| Markov kernel in accepted local reliability model | `A.3.3`; no full MLA unless lens-transfer, publication, assurance, bridge, or reusable explanation is live. |
| category-like research field | `C.29` mini-card and possibly `F.9`; semantic truth and evidence strength explicitly lost. |
| RG-like scale law | `C.29` plus `C.18.1`; scale window and coarse-graining rule required. |
| Vanchurin-style universe-as-learning | candidate lens only; not accepted physics; stop condition blocks ontology. |
| queueing production line | positive mini-card; throughput and latency supported; motivation, obligation, and full organization ontology blocked. |
| team backlog behaves like a queue | mini-card supports waiting and bottleneck reasoning; motivation and duty claims blocked. |
| same graph formalism in two contexts | `F.9` governs Bridge semantics; `C.29` governs lens adequacy. |
| latent manifold or neural operator as scientific model | learned-lens overlay requires observation map, training/validation regime, generalization claim, uncertainty posture, and stop condition. |

Reader-fit checks for admission or material refresh:

| Reader | Required result |
|---|---|
| engineer-manager | Can decide local metaphor, one-line, or mini-card without opening the full card by default. |
| researcher | Can state preserved structure, lost structure, and stop condition without turning the pattern into a philosophy-of-mathematics essay. |
| FPF steward | Can identify the neighboring governing locus for causal, evidence, bridge, scale, measurement, dynamics, temporal, decision, work, explanation, comparison, representation, or assurance claim before accepting a C.29 claim. |
| SoTA author | Can mark a source as adopt, adapt, reject, or candidate stress test without laundering speculative work into accepted FPF law. |
| AI-assisted reader | Recovers `C.29` or the neighboring governing pattern from the query, and does not answer from a thin echo such as `field-like`, `quantum-like`, or `category-like` alone. |

### C.29:9 - Archetypal grounding

| Archetype | Candidate lens | Preservation | Loss | Output and stop condition |
|---|---|---|---|---|
| Production line as queueing network | Queueing network | flow, service rates, bottlenecks, waiting time | human motivation, contractual duties, rare events not modeled | `MLA.MiniCard`; supports throughput and latency reasoning, not full organizational ontology. |
| Team backlog as queue | Queueing lens | work arrival, work in progress, service time, waiting time | obligation, motivation, priority legitimacy, skill learning | `MLA.OneLine` or mini-card; supports bottleneck reasoning, not moral or managerial authority. |
| Manager sees slow throughput but has no lens | Queue or flow candidate note | possible arrivals, work in progress, service bottleneck, waiting time | motivation, duty, priority legitimacy, full team ontology | Start with `MLA.LensCandidateNote`; move to `MLA.OneLine` or mini-card only after the candidate queue/flow lens changes the next admissible inspection. |
| Measurement comparison as declared distance or scoring choice | Metric-space distance, embedding, or scoring-function lens | comparability, distance, proximity, clustering, threshold structure | evidence strength, causal mechanism, value judgment | `MLA.OneLine` or mini-card; supports comparison design and sensitivity checks, not truth or priority by itself. |
| Stabilizing system as state-space dynamics | State-space or transition lens | state variables, transition relation, attractor, control handle when supported | unobserved motivation, obligation, causal mechanism beyond the model | `MLA.OneLine` or mini-card; supports state/transition inspection, not full dynamics ontology. |
| Research field as citation graph or category-like network | Graph or categorical structure | adjacency, composition, interface, failed transfer, citation or transformation patterns | semantic truth, evidence strength, social meaning | First inspect adjacency, composition, interface, or failed transfer; `MLA.MiniCard` plus `F.9` when contexts cross; never substitute graph proximity for truth or evidence. |
| Quantum-like dashboard | Quantum-like probe/order lens | order effects, probe effects, incompatible frames when actually supported | physical quantum ontology | `C.26` with MLA-compatible stop condition `QL-NQ`; not a full-card cost for QL-lite notes. |
| RG-like scale-law claim | Coarse-graining or fixed-point lens | scale variable, coarse-graining rule, invariants across scales | micro-mechanism identity and universal validity | `C.29` plus `C.18.1` or `C.19.1`; stops outside scale window. |
| Learned operator as scientific lens | Learned operator, latent space, surrogate solver | trained input-output structure, resolution behavior when validated | causal mechanism, out-of-domain generalization, unobserved variables | Learned-lens overlay; validation posture and stop condition required. |

Worked micro-cases by failure mode:

| Failure mode | Reader sees | C.29 repair |
|---|---|---|
| No-lens repair | "Throughput is slow, but we have no model." | Start with a queue or flow `MLA.LensCandidateNote`; observe arrivals, work in progress, service time, wait time, and bottleneck candidate before moving to `MLA.OneLine` or mini-card. |
| Under-specified-lens repair | "The market is a field." | Write `MLA.OneLine` only if the candidate mathematical object, mapping, preserved structure, lost structure, payoff, and stop condition can be stated; otherwise remove the phrase or keep it as ordinary metaphor. |
| Overread repair | "The latent manifold explains reality." | Use the learned-lens overlay, name observation map and validation slice, and stop causal or ontology overread unless a neighboring pattern supports it. |
| Wrong-neighbor repair | "The same graph appears in two contexts, so the meanings are the same." | Open `F.9` for Bridge semantics; keep `C.29` only for mathematical-lens adequacy. |
| Local-math non-use | Accepted Markov kernel inside local dynamics. | Stay in `A.3.3`; return `NoMLANeededNote` if useful; do not open C.29 merely because local mathematics appears. |
| Speculative SoTA stress | Vanchurin-style universe-as-learning. | Treat as candidate-lens stress, not accepted physics, foundation, assurance, or release support. |

Vanchurin-style universe-as-learning is not an ordinary first grounding archetype. Keep it in the validation harness and SoTA posture as a candidate stress test: it can teach overclaim control and adapt-not-adopt discipline, but it does not ground accepted physics, assurance, quantitative law, or routine lens adequacy.

### C.29:10 - Bias annotation


| Bias risk | MLA correction |
|---|---|
| **Mathematical prestige bias** | Require `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensSupportPosture`, and `StopCondition`. |
| **Physics envy** | Physical source-domain ontology does not transfer without separate proof/evidence and receiving pattern. |
| **Category-theory monoculture** | Use category-theoretic material only when composition, interfaces, views, transformations, or transport structure matters to the stated use; otherwise choose the local lens family that exposes the working cue. |
| **Speculation laundering** | Vanchurin enters as candidate lens / SoTA-echo, not accepted fact. |
| **Over-formalization** | Low-consequence analogy can remain local prose; reusable or decision-bearing lens needs an MLA card. |
| **Dry ontology drift** | Keep Plain explanations where they improve recognition, but recover claim-bearing force through exact fields or a named neighboring pattern. |
| **Scale blindness** | Require `ScaleWindow?`; coordinate scale claims with `C.18.1` / `C.19.1`. |
| **Causal laundering** | If the lens licenses causal claims, apply `C.28`; MLA cannot supply causal use by itself. |
| **Assurance laundering** | Mathematical elegance does not raise `R`; evidence and assurance use apply `A.10`, `B.3`, and relevant G patterns. |
| **Pattern-as-actor wording** | A pattern is described as writing, deciding, raising assurance, authorizing work, or creating project records; repair it through claim-bearing text, project-side records, governing FPF loci, and exact pattern application, because patterns supply discipline, not agency. |

### C.29:11 - Conformance checklist

`C.29` checklist verifies the action path without replacing the `Solution`. Candidate-lens guidance belongs in `C.29:4.4.3` or worked grounding, not in this checklist; the checklist verifies only that the cheapest honest output and next admissible move remain visible.

| ID | Requirement | Purpose |
|---|---|---|
| `CC-MLA-0 Use condition` | Use MLA only when a mathematical object, formalism, family, learned representation, or simulation substrate is used for explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer. | Keeps local analogies lightweight. |
| `CC-MLA-1 Output class selected before full card` | Select no-MLA-needed, one-line, mini-card, full-card, or `NeighborGoverningLocusNote` output before presenting full-card fields. | Prevents card-before-problem bureaucracy. |
| `CC-MLA-2 Named substrate` | A mathematical phrase affecting explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer names a concrete `CandidateMathObject`, not a prestige family label. | Blocks prestige vocabulary. |
| `CC-MLA-2a Intervention preservation` | If `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation and causal use is live, state whether intervention and counterfactual structure is preserved, approximated, or not claimed, then apply `C.28` for causal-use support. | Prevents causal abstraction laundering. |
| `CC-MLA-3 Lens mapping mode` | State the `C.29`-local lens mapping mode and do not use it as `F.9` BridgeKind, `A.6.P` `RelationKind`, or domain ontology. If bridge semantics are live, cite or open `F.9`. | Prevents hidden bridge, relation-kind, or ontology conversions. |
| `CC-MLA-4 Preserved structure` | State what structure the lens preserves. | Makes transfer testable. |
| `CC-MLA-5 Lost structure` | State what does not transfer; if nothing is lost, support an equivalence or isomorphism claim. | Prevents map-territory collapse. |
| `CC-MLA-6 Invariants exposed` | Name invariants, obstructions, fixed points, symmetries, conservation laws, dualities, distinctions, or diagnostic boundaries. | Makes the lens usefulness visible. |
| `CC-MLA-6a First-principles family recovery` | When a first-principles lens-family row from `C.29:4.2b` carries claim-bearing use, recover the concrete substrate, preserved structure, lost structure, visible payoff, support posture, and stop condition or neighboring exit for that family. | Prevents family names such as boundary, cohomology, symmetry, variational, RG, diagonal, composition, probability, or information from replacing actual MLA recovery. |
| `CC-MLA-7 Lens-supported prediction or distinction` | When decision, prediction, model selection, or publication-as-model is live, state at least one lens-supported prediction, distinction, obstruction, or diagnostic boundary, or downgrade to analogy-only prompt. | Prevents decorative formalism. |
| `CC-MLA-8 State, observation, and evidence separation` | If state, observation, probe, readout, or evidence is live, apply `A.3.3`, `A.19`, `C.16`, or `A.10` as needed. | Prevents passive-read and dashboard mistakes. |
| `CC-MLA-8a Neighboring claim distribution` | If the live output is a choice result, method or work record, evidence path, assurance claim, explanation rendering, comparative review unit, representation shift, coarsened rendering, temporal claim, selector, benchmark, or publication-facing use, name the governing FPF locus and exact project-side record. | Prevents C.29 from absorbing neighboring claims. |
| `CC-MLA-9 Scale window` | If scale, universality, knees, exponents, or coarse-graining are live, declare the scale range and coordinate with `C.18.1` and `C.19.1`. | Prevents universalization. |
| `CC-MLA-9a Temporal use boundary` | If the live claim is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for a use, cite `C.27` or state that temporal adequacy is not live. | Prevents mathematical prediction cues from replacing temporal-claim adequacy. |
| `CC-MLA-10 Rival lens discipline` | Use a principal rival or default ordinary lens by default; require a broader rival set only for selection, publication, or claim-bearing comparison. When a rival relation is live, name the declared relation value and any evaluation criterion, cost, reader, scale window, or neighboring pattern that makes the comparison admissible. | Prevents unnecessary literature-review work and unnamed lens-superiority claims. |

| `CC-MLA-10a Validation posture` | If the lens supports prediction, publication, assurance input, benchmark, model selection, or scientific/model claim, add validation regime, evaluation slice, uncertainty or approximation note, failure case, domain of applicability, and output-change condition when needed. | Keeps prediction-bearing and model-bearing uses SoTA-aligned. |
| `CC-MLA-10b Source-basis role` | If a source carries C.29 force, name its `SourceBasisRole`; do not let source prestige silently become evidence, causal support, bridge semantics, assurance, release, selector, benchmark, or accepted law. | Separates source use from adoption posture. |

| `CC-MLA-11 LensSupportPosture` | Label `LensSupportPosture` as analogy-only prompt, diagnosticOnly, formal derivation, simulation, empirical fit, accepted domain theory, SoTA-echo candidate, or mechanized proof, with matching use-rights. | Prevents evidence laundering. |
| `CC-MLA-12 No ontology smuggling` | Do not import source-domain ontology without separate proof/evidence and receiving pattern. | Protects FPF from metaphysical collapse. |
| `CC-MLA-13 Stop condition` | State the most tempting nearby claim the lens does not license. | Makes misuse locally visible. |
| `CC-MLA-14 Bridge discipline` | Cross-context mathematical transfer cites `F.9`; Bridge and MLA fields agree without duplicate writing. | Keeps semantics bounded. |
| `CC-MLA-15 Causal-use discipline` | Causal-use claims apply `C.28`; MLA cannot make causal use admissible by itself. | Blocks causal laundering. |
| `CC-MLA-16 Assurance discipline` | Assurance, release, reliability, and engineering-justification claims apply `A.10`, `B.3`, and relevant G patterns. | Prevents elegance from raising assurance directly. |
| `CC-MLA-17 C.2.P recovery` | Broad heads, source/target wording, mapping wording, pattern-application wording, and Plain metaphors are recovered to exact FPF kinds, fields, neighboring patterns, or explicit non-transfer dispositions. | Keeps the pattern from minting parallel ontology. |
| `CC-MLA-18 Plain/Tech balance` | A Plain sentence can remain when it aids recognition; if it carries ontology, evidence, causal, assurance, bridge, gate, work, decision, or admissibility claim force, that claim force is recovered through the Tech fields or neighboring pattern. | Preserves didactic force without shadow semantics. |
| `CC-MLA-19 Non-use and false-positive bank` | The pattern includes non-use examples for ordinary local domain equations, local graph data structures, A.19 overlays, local category proofs, and one-off metaphors. | Prevents MLA-everywhere. |
| `CC-MLA-20 Repair matrix` | Failed checks map to repair outputs: downgrade, narrow, add loss, add evidence, choose rival lens, apply neighbor, or block overread. | Keeps MLA as repair pattern. |
| `CC-MLA-21 Validation harness` | Stable admission requires the small harness cases in §8.1 or an admitted equivalent validation carrier. | Makes repeatable readiness visible. |

### C.29:12 - Common anti-patterns

| Anti-pattern | What it looks like | Repair |
|---|---|---|
| **Map-territory collapse** | “The organization is a quantum system.” | “A quantum-like lens models order, probe, or contextual-probability effects; no physical quantum ontology is licensed.” |
| **Prestige substitution** | “Use category theory” without naming objects, morphisms, functors, preservation, or loss. | Name the categorical structure, preserved composition or interface, and failed transfer. |
| **Family-name substrate** | `field`, `graph`, `category`, `RG`, or `quantum` appears as if the family name were enough. | Name the concrete object, structure, formal role, or downgrade to Plain recognition. |
| **MLA-everywhere** | Every measurement template, score, graph, kernel, ODE, equation, or local formal object opens `C.29`. | Require lens-transfer, publication, assurance, bridge, comparison, or reusable-explanation use. |
| **Card-before-problem** | The author fills fields before stating the working phrase and first repair. | Begin with the phrase, stated use, output class, and first repair output. |
| **Local-theory over-escalation** | Accepted local dynamics or domain equations are treated as needing MLA by default. | Keep them under the local domain pattern or `A.3.3` unless a separate lens-transfer claim, publication use, assurance input, bridge, comparison, or reusable-explanation use is live. |
| **False exactness** | Equivalence, isomorphism, or exact representation is declared when only analogy, fit, or simulation exists. | Downgrade `LensMappingMode` or provide support for the declared exact relation. |
| **RG-as-vibe** | “Everything is coarse-graining” with no scale window, coarse-graining rule, or fixed point. | Declare scale variable, coarse-graining rule, invariants, and rival micro-models. |
| **Elegant-math override** | A specialized or elegant mathematical lens is selected over a more general or scale-amenable alternative because of elegance or prestige while scale advantage is live. | Use BLP scale-audit when the claim is scale advantage; otherwise mark the lens as local and bounded by `C.29` stop condition. |
| **Familiar math misses live structure** | A graph, linear trend, average, two-characteristic chart, or score is used because it is familiar while the live problem needs uncertainty, topology, dynamics, causal structure, scale law, distribution geometry, or operator view. | Name the working problem cue; choose a lens family that exposes the missing structure, or keep the simple math as local orientation only and block transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable-explanation use. |
| **Vanchurin over-adoption** | “FPF now says physics is learning.” | Mark as candidate lens; retain open questions and evidence limits. |
| **Invariant-free metaphor** | “Market is a field” with no invariant, transition law, observation map, or `LensSupportPosture`. | Downgrade to local metaphor or build an MLA one-line or mini-card. |
| **Loss-free bridge** | Mathematical structure is exported across contexts without `F.9`, loss notes, counter-example, or supported use. | Use `F.9` Bridge plus MLA `LostStructure` and `StopCondition`. |
| **Duplicate bridge writing** | MLA repeats sense cells, CL, substitution scope, and Bridge-supported use. | Let `F.9` write Bridge semantics; cite Bridge from MLA. |
| **LensMappingMode as BridgeKind** | A local `LensMappingMode` value is used to skip `F.9`. | Do not define a bridge-valued `LensMappingMode`; use a local transfer class only for lens adequacy and open `F.9` for cross-context meaning, substitution, CL, sense cells, or Bridge-supported use. |
| **Causal laundering** | Lens fit is treated as proof of intervention effect. | Apply `C.28` and evidence design, or block causal use. |
| **Assurance laundering** | Elegant formalism is treated as release confidence. | Use `A.10` and `B.3`; MLA can be evidence input only when `LensSupportPosture` and validation posture are declared. |
| **LensSupportPosture laundering** | `SoTA-echo candidate` sounds like authority. | Restrict to exploration or lens-adequacy tests unless validation and neighboring evidence patterns support prediction, decision, causal use, bridge substitution, assurance, or ontology. |
| **RivalLensSet as literature review** | The C.29 application produces a survey instead of naming the live rival. | Use `PrincipalRivalLens?` by default; add `RivalLensRelation?` when disagreement changes the next move; broaden to `RivalLensSet?` only when publication, selection, or claim-bearing comparison is live. |
| **StopCondition boilerplate** | The card says “does not prove everything.” | State the most tempting nearby overread the lens does not license. |
| **Neighbor absorption** | MLA repeats `F.9`, `C.28`, `A.3.3`, `A.19`, `C.11`, `A.15`, `A.10`, `B.3`, `C.16`, `C.27`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, or assurance semantics. | Apply the governing-locus table and cite the neighboring pattern. |
| **Plain metaphor carrying law** | “What survives transfer” becomes an unstated Tech claim. | Recover the claim force through `C.2.P` fields or keep it as ordinary Plain recognition only. |
| **MLA-kind inflation** | `MLA.Card` is treated as a universal `U.*` object or durable FPF record. | Keep it pattern-local; durable cross-pattern records require explicit mint/reuse, naming, kind, and design-rationale support through `F.8`, `F.18`, `C.3`, and `E.9`. |

### C.29:13 - SoTA-echoing account

SoTA support for `C.29` is accepted only when it changes action guidance. A citation that only decorates the file does not carry `C.29`.

`C.29` separates source-basis roles from adoption posture. `Adopt`, `Adapt`, `Reject`, and candidate-stress-test disposition say what FPF does with the source; `SourceBasisRole` says what work the source may perform inside a C.29 application.

| `SourceBasisRole` | Admissible `C.29` use | Blocked `C.29` use |
|---|---|---|
| `recognitionCue` | Help the reader notice an invariant, obstruction, symmetry, duality, state variable, scale cue, or comparison cue. | Supply evidence, truth, ontology, causal support, assurance, or release confidence. |
| `candidateLensPrompt` | Suggest a first candidate lens family or mathematical object to test against the current problem cue. | Require a lens before the candidate changes the next move. |
| `adequacyControlSource` | Discipline preserved structure, lost structure, stop condition, validation posture, or neighboring-pattern exit. | Replace the C.29 fields or the neighboring governing pattern. |
| `validationSupport` | Support declared validation regime, evaluation slice, uncertainty, failure case, or domain of applicability. | Become an evidence path, assurance claim, benchmark result, or release confidence by source prestige alone. |
| `acceptedDomainTheory` | Support local use inside a domain where the theory is already the governing local substrate. | License cross-context ontology import or broader transfer without `F.9`, evidence, and stop condition. |
| `proofUnderAssumptions` | Support a formal property under stated assumptions. | Prove real-world adequacy unless assumptions, observations, bridge, and evidence are also supported. |
| `negativeExample` | Expose failure, obstruction, non-transfer, counterexample, or stop condition. | Act as a proof that the rival or source family is globally unusable. |
| `rivalLensSource` | Name a principal rival lens or relation that changes the current admissible move. | Become a literature review, selector result, or benchmark result. |
| `sourceIdentityLocator` | Preserve exact source identity when a source is being cited or traced. | Carry substantive adequacy by itself. |
| `historicalBackgroundOnly` | Explain lineage or terminology without carrying current adequacy support. | Support present-day prediction, decision, bridge, causal, assurance, or admission use. |

| SoTA line | Selected action-guidance effect | Disposition |
|---|---|---|
| Applied category theory and compositionality | Use category-theoretic material for composition, interfaces, views, transformations, and transport discipline. Require named structure, preserved composition or interface, lost structure, and failed transfer. | **Adapt.** Useful for composition and interface questions when those structures matter to the stated use. |
| Obstructions to compositionality | Treat failures and obstructions as first-class `LostStructure` and `StopCondition` material. | **Adapt.** A lens can be useful because it names where transfer fails. |
| Plural foundations of mathematics | Allow multiple structural families with local adequacy, declared mapping, and declared loss. | **Adopt.** Supports plural-foundations stance. |
| Geometric deep learning, invariance, and equivariance | Use symmetry, group action, invariance, and equivariant representation as lens-discovery cues when generic feature lists hide the relevant sameness under transformations. Ask which transformations are admissible, which distinctions are preserved, and which coordinate details can be lost. | **Adapt as lens-discovery support.** Not evidence for domain law, causal mechanism, or coordinate-free truth. |
| Optimal transport and distribution geometry | Use transport plans, couplings, Wasserstein-like geometry, and declared movement cost as lens-discovery cues for population, distribution, shape, shift, or allocation questions. Ask what moves, under which cost, and what structure or mass is lost. | **Adapt as lens-discovery support.** Not evidence for causality, fairness, mechanism, or policy effect. |
| Model reporting and responsible modeling practice | Intended use, evaluation conditions, limitations, validation regime, failure cases, uncertainty, and domain of applicability become MLA validation posture for prediction, publication, assurance-input, benchmark, model-selection, and scientific/model uses. | **Adapt.** Turns reporting practice into fields and repair moves. |
| Causal and approximate causal abstraction | When abstraction, quotient, coarse-graining, simulation, or macro-modeling is live, ask whether intervention and counterfactual structure is preserved, approximated, or not claimed; use `C.28` for causal-use support. Approximate abstraction is a source-backed posture, not a softened causal-use grant. | **Adapt.** No C.29 output is causal authority. |
| Causal representation learning | Use causal-representation work as a discovery guard for latent variables, learned factors, interventions, assignments, and invariance across environments. If a latent lens is being read causally, keep causal-use support with `C.28`. | **Adapt as lens-discovery support.** Blocks “latent means causal”; does not make representation learning a causal verdict. |
| Scientific machine learning as hybrid first-principles/data-driven modeling | Treat first-principles support as plural and domain-bound: conservation laws, constitutive relations, boundary conditions, symmetries, known dynamics, numerical stability, uncertainty, and data-driven approximation can each discipline a lens. Require the C.29 user to name the concrete structure and validation boundary rather than saying "science says so." | **Adapt.** Supports the first-principles posture without making any one SciML family the FPF foundation. |
| Variational principles and constrained extrema | Use action, energy, free-energy, loss, value, entropy, or resource functionals as first-principles lenses only when the admissible variation space, constraints, boundary conditions, stationarity or extremum condition, conserved or dual quantities, and neighboring dynamics/evidence exits are named. | **Adapt as first-principles lens-discovery support.** Does not imply the target literally optimizes the declared functional; dynamics, evidence, causal-use, and assurance claims stay with neighboring loci. |
| Physics-informed ML and learned scientific representations | Use physics-informed losses, governing equations, neural operators, surrogate solvers, and learned representations only with observation map, training or simulation regime, resolution or discretization policy, generalization claim, validation slice, uncertainty or approximation note, and stop condition. | **Adapt.** Supports the learned-lens overlay; does not license out-of-regime solver replacement, causal mechanism, or unobserved-state truth. |
| Scientific and physics foundation models | Treat foundation-model claims in scientific domains as learned-lens stress tests: broad pretraining, in-context dynamics inference, zero-shot or transfer claims, and cross-domain simulation all require declared training regime, task family, validation regime, uncertainty, failure cases, and output-change condition. | **Adapt as SoTA pressure.** A foundation-model result can suggest a candidate lens or benchmark question; it is not accepted FPF law and not a universal first-principles source. |
| Koopman, operator-theoretic dynamics, and system identification | Use observables, operator representations, dynamic-mode decomposition, and sparse identification as discovery cues for nonlinear dynamics. Name the state, observable or readout, forecast or control use being tested, and the neighboring dynamics or temporal locus. | **Adapt as lens-discovery support.** Does not prove a real mechanism, dynamics semantics, evidence, or temporal-use adequacy. |
| Probabilistic programming, Bayesian workflow, and model criticism | Use priors, likelihood assumptions, posterior predictive checks, prior-data conflict, model mismatch, and uncertainty as lens-adequacy cues. Ask what the probabilistic lens makes visible, what assumptions it imports, and where prediction or explanation stops. | **Adapt as lens-discovery and criticism support.** Not a truth verdict, evidence verdict, or assurance result by itself. |
| Modern Bayesian/OED, active sensing, and adaptive sampling | Use modern BED/OED, expected-information-gain estimation, acquisition-function, active-learning, Bayesian-optimization, and robustness results to ask which observation, probe, assignment, fidelity, or sample would change the lens's next admissible move. Require declared utility, design variable, model assumptions, computational tractability, model-misspecification or robustness posture, and validation boundary before using the result for prediction, decision, experiment planning, evidence, causal support, or assurance. | **Adapt as current lens-discovery support.** Not a measurement construction, evidence record, causal-support result, experiment plan, or assurance claim by itself. |
| Uncertainty, approximation, sensitivity, and robustness practice | Prediction or scientific/model use requires approximation or uncertainty posture, known failure or counterexample, and domain of applicability. | **Adapt.** Prevents empirical-fit overread. |
| Vanchurin 2026 | Use as structure-dense candidate lens and overclaim stress-test: learning dynamics, coarse-graining, effective geometry, gauge, metric-tensor, or distance language, variational or thermodynamic optimality. | **Adapt, not adopt.** Not central SoTA authority and not accepted physics. |
| Sandberg structural-sameness examples | Use as recognition examples for invariants, obstructions, dualities, fixed points, symmetries, and conservation-like structures. | **Adopt as recognition cue and examples, not proof authority.** |

#### C.29:13.1 - Sandberg thread / structural sameness examples

Adopt the Sandberg thread as a recognition cue, with two distinct source roles retained: the original X post is the **source identity locator**, while the Axis of Ordinary `Math` section is the checked text carrier used here.

The source-basis examples are not a proof source and not an exhaustive taxonomy. They are a checked example carrier for `InvariantsExposed`: generalized Stokes and boundary-exterior derivative duality; de Rham, cohomology, and topological obstruction; CLT as RG or fixed-point viewpoint; Lawvere-style diagonal family; Noether and symmetry-conservation; and Legendre, potential-duality, and tropical-limit family.

Plain reading: the thread illustrates mathematical compression that makes hidden structure visible. Tech reading: every FPF use still needs `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensSupportPosture`, and `StopCondition`.

Do not adopt the thread as a proof source, peer-reviewed taxonomy, or authority for all mathematical details.

#### C.29:13.2 - Vanchurin 2026 as candidate lens

Adopt/adapt the following as a candidate lens family:

> **learning dynamics → coarse-graining → effective geometry → gauge fields, metric-tensor fields, or distance-like structure → variational/thermodynamic optimality**

Use this source as the case for why FPF needs a lens adequacy card: the source carries many mathematical structures, but its claims are broad and speculative. The candidate-lens stress-test value comes through trainable variables, local update rules, Legendre transforms, thermodynamic potentials, gauge-field, metric-tensor-field, and distance-language claims, memory and processing trade-offs, and RG-like re-optimization of compressed representations.

The Plain lesson is “this is a useful candidate lens, not a new FPF cosmology.” Selected posture:

**Adoption stance: Adapt, not Adopt.**

Adapt:

- learning dynamics as a general language of change,
- resource constraints as a possible source of effective laws,
- coarse-graining as a mechanism for simple macrodescriptions,
- thermodynamic or variational potentials as links between cost, memory, processing, and geometry,
- RG-like re-optimization as a scale-transition discipline.

Do not adopt as FPF norm:

- “the universe really is a neural network,”
- “physics has already been proven from learning,”
- “quantum, GR, or gauge theory reduce to a learning rule or learning dynamics” as established fact.

Known limitations from the checked source stance remain material for MLA use: non-Abelian gauge fields are not treated as a landed FPF result; thermodynamic RG flow is not treated as a quantitative FPF law; quantitative predictions require explicit learning-algorithm specification.

#### C.29:13.3 - Plural foundations stance

Adopt the plural-foundations stance: several structural families can be reusable across domains, and their adequacy depends on declared mapping, local use, mutual interpretability, and recoverable loss.

Source-basis use: Rodin supports the positive stance that several structurally useful families recur across domains. C.29 carries this as local adequacy discipline: select the family that fits the declared use, state the mapping, and publish recoverable loss.

#### C.29:13.4 - Applied category theory

Adopt applied category theory as one major organizer for cross-domain transfer, especially composition, interfaces, views, transformations, and bridges. Retain the concrete source-basis examples: databases, electric circuits, and dynamical systems as application families; adjoint functors, enriched categories, and toposes as categorical structures that organize transfer.

In `C.29`, category-theoretic material is used through the same local adequacy fields as any other lens: stated use, named structure, preserved composition or interface, lost structure, failed transfer, and neighboring-pattern exits. It is especially useful when composition, interfaces, views, transformations, or bridges matter to the admissible move.

#### C.29:13.5 - Obstructions to compositionality

Adapt the obstructions and failures-of-compositionality perspective into `LostStructure` and `StopCondition`: a lens can be useful precisely because it exposes where transfer fails, not only where it succeeds. In Plain language, a good lens does not only say “this travels”; it also names the boundary where transfer stops.

### C.29:13a - Source locators and source-basis guard

SoTA materials are not nameless background. Exact substantive basis and governing inheritance remain recoverable by value, and SoTA rows shape action guidance rather than decorate the file. The source locators and the source-basis role of each external source are retained here.

#### Exact source and governing basis posture

| Basis id | Basis item | What it contributes | Use posture in `C.29` |
|---|---|---|---|
| `FPF-CORE-2026` | Current FPF Core Specification, especially `E.9`, `E.10`, `C.2.P`, `A.6.P`, `A.3.3`, `A.19`, `A.10`, `A.15`, `A.15.1`, `A.15.4`, `B.3`, `C.11`, `C.16`, `C.18.1`, `C.19.1`, `C.26`, `C.27`, `C.28`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, `F.9`, `G.5`, `G.9`. | Governs `C.29` adequacy, lexical/epistemic precision repair, pattern placement, bridge discipline, decision/work/evidence/assurance/explanation/comparison/representation boundaries, state/measurement/dynamics/temporal boundaries, causal-use boundary, and evidence/assurance escalation. | **Governing inheritance.** `C.29` applications satisfy E.9 and phrase-local episteme/publication/source-transfer material through C.2.P. |
| `SAND-THREAD-MATH-LINKS-2026-05-12` | Accessible mirror of Sandberg thread, lines headed “Math,” linking to the original X post. | Recognition examples of structural sameness: generalized Stokes, CLT/RG/fixed-point reading, Lawvere-style diagonal family, Noether, Legendre transforms. | **Adopt as recognition cue and examples, not proof authority.** Direct X content was not treated as a formal source. |
| `VAN-SELF-LEARNING-2026` | Vitaly Vanchurin, **The Self-Learning Universe**, ResearchGate preprint page, May 2026, DOI `10.13140/RG.2.2.17023.16808`. | Candidate lens family: resource-constrained distributed learning → coarse-graining → effective geometry, gauge fields, metric-tensor fields, or distance-like structure → thermodynamic/variational optimality. | **Adapt, not adopt.** Use as SoTA-echo / candidate lens; do not accept the physical claims as FPF law. |
| `RODIN-2023` | Andrei Rodin, **One Mathematic(s) or Many? Foundations of Mathematics in Today's Mathematical Practice**, arXiv:2301.08131. | Supports plural-foundations stance and mutual-interpretability caution. | **Adopt** as support for multiple structural families checked through local adequacy, declared mapping, and recoverable loss. |
| `FONG-SPIVAK-2018/2019` | Brendan Fong and David I. Spivak, **Seven Sketches in Compositionality / An Invitation to Applied Category Theory**, arXiv:1803.05316 and book publication context. | Supports applied category theory as one useful family for composition, interfaces, views, transformations, and bridges. | **Adopt/adapt** for examples and transport discipline when those structures matter to the stated use. |
| `GDL-BRONSTEIN-2021` | Bronstein et al., **Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges**, arXiv:2104.13478. | Supports lens discovery through symmetry, invariance, equivariance, group action, geometric structure, and graph structure. | **Adapt as discovery support.** Helps find a candidate lens; does not supply domain evidence, causal mechanism, or validation by itself. |
| `PEYRE-CUTURI-2019` | Gabriel Peyré and Marco Cuturi, **Computational Optimal Transport**, arXiv:1803.00567 and Foundations and Trends in Machine Learning publication context. | Supports distribution-geometry discovery through transport plans, couplings, Wasserstein-like distances, movement cost, and shape or population shift. | **Adapt as discovery support.** Helps formulate comparison and movement questions; does not supply causal, fairness, mechanism, or policy-effect support by itself. |
| `PUCA-ETAL-2023` | Puca, Hadzihasanovic, Genovese, Coecke, **Obstructions to Compositionality**, arXiv:2307.14461. | Supports making failures and obstructions to compositional transfer explicit. | **Adapt** into `LostStructure`, `StopCondition`, and checks that not every transfer preserves the needed structure. |
| `MODEL-REPORTING-2018/2021` | Mitchell et al., **Model Cards for Model Reporting**; Gebru et al., **Datasheets for Datasets**. | Supports intended-use, evaluation-condition, limitation, dataset-context, and out-of-scope-use declarations for model and data-bearing lenses. | **Adapt.** Use for `admissibleUse`, `nonAdmissibleUse`, validation posture, limitation notes, and domain-of-applicability fields; do not treat documentation presence as evidence or assurance by itself. |
| `CAUSAL-ABSTRACTION-2017/2019` | Rubenstein et al., **Causal Consistency of Structural Equation Models**; Beckers and Halpern, **Abstracting Causal Models**. | Supports asking whether abstraction, quotient, macro-model, or coarse-graining preserves intervention and counterfactual structure. | **Adapt.** Feeds `MLA.CausalAbstractionCheck`; causal-use support still belongs to `C.28`. |
| `APPROX-CAUSAL-ABSTRACTION-2019/2020` | Beckers, Eberhardt, and Halpern, **Approximate Causal Abstraction / Approximate Causal Abstractions**, arXiv:1906.11583 and PMLR 2020. | Supports treating approximate micro-to-macro causal abstraction as a separate posture from exact abstraction, including discrepancy between low-level and high-level causal models and uncertainty in probabilistic causal models. | **Adapt.** Justifies the `approximated` status in `MLA.CausalAbstractionCheck`; causal-use support still belongs to `C.28`. |
| `CAUSAL-ABSTRACTION-JMLR-2025` | **Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability**, JMLR 2025. | Supports generalized mechanism transformation, graded faithfulness, and abstraction checks for learned systems, including where representation mappings become too flexible to carry explanation or causal use. | **Adapt.** Strengthens the abstraction-preservation question; causal-use support still belongs to `C.28`. |
| `SCHOLKOPF-ETAL-2021` | Scholkopf et al., **Towards Causal Representation Learning**, Proceedings of the IEEE 2021, arXiv:2102.11107. | Supports separating learned latent representations from causal variables, interventions, assignments, environment invariance, and causal-use claims. | **Adapt as discovery support.** Helps detect when `C.28` is live; does not make a latent representation causal by itself. |
| `SCIML-NEURAL-OPERATORS-2019/2021` | Raissi, Perdikaris, and Karniadakis on PINNs; Karniadakis et al. on physics-informed machine learning; Lu et al. on DeepONet; Li et al. on Fourier neural operators. | Supports learned-lens obligations: observation map, data or training regime, discretization or resolution policy, generalization claim, validation regime, uncertainty, and stop condition. | **Adapt.** Use as source basis for the lightweight learned-lens overlay; do not promote a full SciML specialization or assume out-of-domain generalization. |
| `SCIML-DIETRICH-SCHILDERS-2025` | Dietrich and Schilders, **Scientific machine learning**, Mathematische Semesterberichte 2025, DOI `10.1007/s00591-025-00399-4`. | Supports the hybrid first-principles/data-driven framing: conservation laws, constitutive relations, boundary conditions, physical consistency, operator learning, probabilistic approaches, uncertainty, robustness, and validation limits. | **Adapt.** Reinforces plural first-principles discipline and validation boundaries; does not make SciML a universal FPF foundation. |
| `PIML-SURVEY-2025` | **When physics meets machine learning: a survey of physics-informed machine learning**, Machine Learning for Computational Science and Engineering 2025, DOI `10.1007/s44379-025-00016-0`. | Supports treating physics-informed learning as integration of prior physics knowledge with data-driven models for data efficiency, generalization, and plausibility, including Lagrangian/Hamiltonian mechanics, energy conservation, physics-informed losses, and physics-informed optimization as current first-principles lens families. | **Adapt.** Strengthens the learned-lens and variational-principle posture; does not make physics-informed wording sufficient evidence or assurance. |
| `NEURAL-OPERATORS-NRP-2024` | **Neural operators for accelerating scientific simulations and design**, Nature Reviews Physics 2024, DOI `10.1038/s42254-024-00712-5`. | Supports neural operators as learned mappings between functions over continuous domains, often constrained by physics and domain structure, with generalization and validation boundaries. | **Adapt.** Supports operator/function-space lens discovery and validation posture; does not license out-of-regime solver replacement. |
| `PHYSICS-FOUNDATION-MODEL-2025` | **Towards a Physics Foundation Model**, arXiv:2509.13805. | Supports using scientific or physics foundation-model claims as SoTA pressure around broad pretraining, in-context dynamics inference, cross-domain simulation, zero-shot transfer, and long-horizon prediction. | **Adapt as candidate/stress-test.** Does not make a foundation model accepted physics, causal support, assurance, or a universal first-principles source. |
| `KOOPMAN-SINDY-DMD-2016` | Brunton, Proctor, and Kutz, **Discovering governing equations from data by sparse identification of nonlinear dynamical systems**; Kutz et al., **Dynamic Mode Decomposition: Data-Driven Modeling of Complex Systems**. | Supports operator and system-identification discovery through observables, dynamic-mode decomposition, sparse identification, forecast use, and control-oriented representation. | **Adapt as discovery support.** Does not make the identified operator a real mechanism or validate temporal-use claims by itself. |
| `BAYES-WORKFLOW-PPL-2018/2020` | van de Meent et al., **An Introduction to Probabilistic Programming**; Gelman et al., **Bayesian Workflow**. | Supports probabilistic-model discovery and criticism through priors, likelihood assumptions, posterior predictive checks, prior-data conflict, model mismatch, uncertainty, and iterative model revision. | **Adapt as discovery and criticism support.** Does not make posterior fit truth, evidence, or assurance by itself. |
| `MODERN-BED-2023/2024` | Rainforth, Foster, Ivanova, and Bickford Smith, **Modern Bayesian Experimental Design**, arXiv:2302.14545; accepted/published in Statistical Science context. | Supports modern BED as utility-driven, computationally constrained experiment design, with recent methods for tractable expected information gain, sequential or adaptive design, and practical deployment limits. | **Adapt as current discovery support.** Does not make C.29 a measurement-construction, evidence, causal-support, or experiment-planning pattern. |
| `MODERN-OED-2024/2026` | Huan, Jagalur, and Marzouk, **Optimal experimental design: Formulations and computations**, Acta Numerica 2024; arXiv:2407.16212 v2 2026. | Supports broad current OED framing: design variables, utility criteria, computational methods, sequential design, complex models, and prediction-oriented data acquisition. | **Adapt as current discovery support.** C.29 may ask what data acquisition would make the lens usable, but neighboring patterns govern experiments, evidence, causal support, and work planning. |
| `BO-AL-ADAPTIVE-SAMPLING-2024` | Di Fiore, Nardelli, and Mainini, **Active Learning and Bayesian Optimization: A Unified Perspective to Learn with a Goal**, Archives of Computational Methods in Engineering 2024, DOI `10.1007/s11831-024-10064-z`. | Supports treating active learning, Bayesian optimization, and adaptive sampling as goal-driven acquisition schemes, not as generic "collect more data" advice. | **Adapt as current discovery support.** Use only for the candidate observation/probe/acquisition move; do not import selector, evidence, or assurance force. |
| `EIG-DENSITY-APPROX-2024/2026` | Li, Baptista, and Marzouk, **Expected information gain estimation via density approximations: Sample allocation and dimension reduction**, arXiv:2411.08390 v3 2026. | Supports the current computational caution that EIG estimation itself can require density approximation, sample-allocation, and dimension-reduction choices before it is usable. | **Adapt as computational-tractability support.** A claimed information-gain lens needs an estimation and approximation posture when the computation is live. |
| `ROBUST-GBOED-2025` | Barlas, Sloman, and Kaski, **Robust Experimental Design via Generalised Bayesian Inference**, arXiv:2511.07671. | Supports robustness to model misspecification, outliers, and incorrect noise assumptions through generalized/Gibbs Bayesian OED and Gibbs expected information gain. | **Adapt as robustness support.** If model misspecification is plausible, the C.29 output records the robustness posture; it does not turn robustness into evidence or assurance by itself. |
| `VVUQ-UQ-PREDICTION-2010/2012/2007` | Oberkampf and Roy, **Verification and Validation in Scientific Computing**; National Research Council, **Assessing the Reliability of Complex Models**; Gneiting and Raftery, **Strictly Proper Scoring Rules, Prediction, and Estimation**. | Supports validation, uncertainty, prediction scoring, calibration caution, sensitivity or robustness notes, and domain-of-applicability boundaries. | **Adapt.** Prediction, publication-as-model, benchmark, model-selection, or assurance-input uses need a validation or uncertainty posture; source prestige does not supply that posture. |

| Source-basis id | Locator(s) | Recoverability and use in `C.29` |
|---|---|---|
| `SAND-THREAD-X-2026-05-12` | Original X post locator: `https://x.com/anderssandberg/status/2053757849918939364` | **Source identity locator.** Keep the X link because the source being mirrored matters. Do not rely on direct X content as proof text unless the post content is actually retrievable in the checking environment. |
| `SAND-THREAD-MATH-LINKS-2026-05-12` | Accessible mirror / quotation carrier: `https://axisofordinary.substack.com/p/links-for-2026-05-12`, section headed `Math`, linking to the X post above. | **Checked source-text carrier.** Supplies the recognition examples: generalized Stokes / boundary-exterior derivative duality; de Rham/cohomology/topological obstruction; CLT as RG/fixed-point viewpoint; Lawvere-style diagonal family; Noether/symmetry-conservation; Legendre/duality/tropical-limit family. |
| `VAN-SELF-LEARNING-2026` | `https://www.researchgate.net/publication/404659508_The_Self-Learning_Universe`, DOI `10.13140/RG.2.2.17023.16808` | **Candidate-lens source.** Use as structured SoTA stress test and example of why MLA needs source posture, preserved/lost structure, and stop condition. Do not use as accepted physics. |
| `RODIN-2023` | `https://arxiv.org/abs/2301.08131` | **Plural-foundations source.** Supports multiple interpretable mathematical foundations or families checked through local adequacy, declared mapping, and recoverable loss. |
| `FONG-SPIVAK-2018/2019` | `https://arxiv.org/abs/1803.05316`; Cambridge page: `https://www.cambridge.org/core/books/an-invitation-to-applied-category-theory/D4C5E5C2B019B2F9B8CE9A4E9E84D6BC` | **Applied-category-theory source.** Supports category theory as one useful organizer for composition, interfaces, views, transformations, and bridges when those structures matter to the stated use. |
| `GDL-BRONSTEIN-2021` | `https://arxiv.org/abs/2104.13478` | **Geometric-deep-learning discovery source.** Supports using symmetry, invariance, equivariance, group action, graph structure, and geometric structure to find candidate lenses; not evidence that a domain law, causal mechanism, or validation claim holds. |
| `PEYRE-CUTURI-2019` | `https://arxiv.org/abs/1803.00567` | **Optimal-transport discovery source.** Supports transport plans, couplings, Wasserstein-like geometry, costed movement, and distribution, population, shape, shift, or allocation comparison; not causal, fairness, mechanism, or policy-effect support by itself. |
| `PUCA-ETAL-2023` | `https://arxiv.org/abs/2307.14461` | **Obstruction source.** Supports making failures of transfer explicit; feeds `LostStructure`, `StopCondition`, and the rule that not every functor-like transfer preserves the needed structure. |
| `MODEL-CARDS-2018/2019` | `https://arxiv.org/abs/1810.03993` | **Model-reporting source.** Supplies intended-use, evaluation-slice, limitation, and out-of-scope-use structure for model-bearing lenses; does not make reported model use admissible by itself. |
| `DATASHEETS-2018/2021` | `https://arxiv.org/abs/1803.09010`; CACM page: `https://cacm.acm.org/research/datasheets-for-datasets/` | **Dataset-documentation source.** Supplies provenance, composition, collection, recommended use, and limitation prompts when a lens depends on data or dataset-derived representation. |
| `CAUSAL-CONSISTENCY-2017` | `https://arxiv.org/abs/1707.00819` | **Causal-abstraction source.** Supports checking whether SEM descriptions at different granularities agree about intervention effects; feeds the intervention-preservation question without giving `C.29` causal authority. |
| `CAUSAL-ABSTRACTION-2019` | `https://arxiv.org/abs/1812.03789`; AAAI page: `https://ojs.aaai.org/index.php/AAAI/article/view/4117` | **Causal-abstraction source.** Supports distinguishing transformations, abstractions, and named abstraction classes; used only to require explicit `C.28` application when causal use is live. |
| `APPROX-CAUSAL-ABSTRACTION-2019/2020` | `https://arxiv.org/abs/1906.11583`; PMLR page: `https://proceedings.mlr.press/v115/beckers20a.html` | **Approximate causal-abstraction source.** Supports `approximated` intervention and counterfactual preservation status in the lightweight causal-abstraction check; does not let `C.29` decide causal-use support without `C.28`. |
| `CAUSAL-ABSTRACTION-JMLR-2025` | `https://jmlr.org/beta/papers/v26/23-0058.html` | **Current causal-abstraction source.** Supports generalized mechanism-transformation and graded-faithfulness checks for learned systems; keeps causal-use support with `C.28`. |
| `SCHOLKOPF-ETAL-2021` | `https://arxiv.org/abs/2102.11107`; DOI `10.1109/JPROC.2021.3058954` | **Causal-representation discovery source.** Supports asking whether a learned latent representation has intervention, assignment, outcome, and environment-invariance support before causal use; opens `C.28` when causal-use support is live. |
| `PINN-2019` | DOI `10.1016/j.jcp.2018.10.045` | **Physics-informed ML source.** Supports validation, training-regime, governing-equation, and inverse/forward problem distinctions for learned mathematical lenses. |
| `PIML-2021` | DOI `10.1038/s42254-021-00314-5` | **Physics-informed machine-learning survey source.** Supports treating physics-informed learning as a broad learned-lens family requiring problem, prior-knowledge, validation, and uncertainty boundaries. |
| `DEEPONET-2021` | DOI `10.1038/s42256-021-00302-5` | **Neural-operator source.** Supports operator-learning as a learned mathematical lens over function spaces; requires training domain, observation map, generalization claim, and stop condition. |
| `FNO-2020/2021` | `https://arxiv.org/abs/2010.08895` | **Neural-operator source.** Supports resolution and PDE-family generalization checks; does not license out-of-regime solver replacement without validation. |
| `SCIML-DIETRICH-SCHILDERS-2025` | DOI `10.1007/s00591-025-00399-4`; `https://link.springer.com/article/10.1007/s00591-025-00399-4` | **Current SciML survey source.** Supports hybrid first-principles/data-driven framing, physical consistency, operator learning, probabilistic approaches, uncertainty, robustness, and validation limits. |
| `PIML-SURVEY-2025` | DOI `10.1007/s44379-025-00016-0`; `https://link.springer.com/article/10.1007/s44379-025-00016-0` | **Current physics-informed ML survey source.** Supports prior-physics integration as data-efficiency, generalization, and plausibility support; not evidence or assurance by itself. |
| `NEURAL-OPERATORS-NRP-2024` | DOI `10.1038/s42254-024-00712-5`; `https://www.nature.com/articles/s42254-024-00712-5` | **Neural-operator review source.** Supports function-space/operator lens obligations, physics/domain constraints, and validation boundaries for scientific simulation and design. |
| `PHYSICS-FOUNDATION-MODEL-2025` | `https://arxiv.org/abs/2509.13805` | **Physics-foundation-model candidate source.** Supports candidate/stress-test handling of broad scientific foundation-model claims; does not make those claims accepted FPF law. |
| `KOOPMAN-SINDY-DMD-2016` | SINDy DOI `10.1073/pnas.1517384113`; DMD DOI `10.1137/1.9781611974508` | **Operator-dynamics and system-identification discovery source.** Supports choosing observables, dynamic-mode-decomposition or sparse-identification lenses for nonlinear dynamics; dynamics semantics, evidence, and temporal-use support still require `A.3.3`, `A.10`, or `C.27` when live. |
| `BAYES-WORKFLOW-PPL-2018/2020` | Probabilistic programming arXiv `https://arxiv.org/abs/1809.10756`; Bayesian Workflow arXiv `https://arxiv.org/abs/2011.01808` | **Probabilistic-model discovery and criticism source.** Supports prior, likelihood, posterior predictive, prior-data conflict, model mismatch, uncertainty, and revision cues; does not make probabilistic fit a truth, evidence, or assurance result by itself. |
| `MODERN-BED-2023/2024` | `https://arxiv.org/abs/2302.14545`; DOI `10.48550/arXiv.2302.14545` | **Modern Bayesian experimental design source.** Supports current BED as utility-driven and computationally constrained, with tractable EIG, sequential/adaptive design, and deployment limits; neighboring patterns still govern measurement construction, evidence, causal support, and work planning. |
| `MODERN-OED-2024/2026` | `https://arxiv.org/abs/2407.16212`; Cambridge Core DOI `10.1017/S0962492924000023` | **Modern optimal experimental design source.** Supports broad OED formulations and computations for complex models; C.29 uses it only to ask what acquisition would make a candidate lens usable. |
| `BO-AL-ADAPTIVE-SAMPLING-2024` | DOI `10.1007/s11831-024-10064-z`; `https://link.springer.com/article/10.1007/s11831-024-10064-z` | **Adaptive-sampling source.** Supports goal-driven acquisition and the BO/active-learning relation; does not create selector, evidence, or assurance authority. |
| `EIG-DENSITY-APPROX-2024/2026` | `https://arxiv.org/abs/2411.08390`; DOI `10.48550/arXiv.2411.08390` | **EIG computation source.** Supports density-approximation, sample-allocation, and dimension-reduction caution for expected-information-gain claims. |
| `ROBUST-GBOED-2025` | `https://arxiv.org/abs/2511.07671`; DOI `10.48550/arXiv.2511.07671` | **Robust experimental-design source.** Supports generalized-Bayesian robustness for model misspecification, outliers, and incorrect noise assumptions. |
| `OBERKAMPF-ROY-2010` | Cambridge page: `https://www.cambridge.org/core/books/verification-and-validation-in-scientific-computing/contents/9399D588DE8B3D49E392CF0436D5A67D` | **Verification-and-validation source.** Supports separation of verification, validation, uncertainty, calibration, and prediction-use boundaries. |
| `NRC-VVUQ-2012` | DOI `10.17226/13395`; `https://nap.nationalacademies.org/catalog/13395/assessing-the-reliability-of-complex-models-mathematical-and-statistical-foundations` | **VVUQ source.** Supports uncertainty quantification and reliability limits for complex model use. |
| `GNEITING-RAFTERY-2007` | DOI `10.1198/016214506000001437` | **Prediction-scoring source.** Supports proper scoring and prediction-evaluation posture when a lens claims predictive use. |

### C.29:13b - Source correction notes retained as selected basis

1. `VAN-SELF-LEARNING-2026` is treated as a ResearchGate preprint / early-stage source. Peer-review status is not established from the checked page. `C.29` therefore does not state that its physics is accepted or that its derivations are FPF law.
2. `SAND-THREAD-MATH-LINKS-2026-05-12` is a recognition cue, not a mathematical proof source or FPF law.
3. CLT-as-RG/fixed-point wording is retained only as a structural modeling viewpoint. A safe formulation is: under the usual normalization, the Gaussian is an attractive fixed point for finite-variance distributions; other stable laws are other fixed points under suitable normalization.
4. Claims that the Vanchurin preprint derives Schrödinger, Klein–Gordon, Dirac, Einstein, or Maxwell equations are represented as **claims made by that preprint**, not as accepted FPF facts.
5. The intake correction from direct identification to structure-preserving representation is selected and becomes a central ontology guard.

### C.29:14 - Informative taxonomy seed

Use this recognition menu only to identify a possible lens family and likely neighboring-pattern exits. After selecting a row, state the local C.29 fields that make the lens adequate or stop the use.

| Lens family | What it catches | FPF use | Common stop condition | Likely neighboring patterns |
|---|---|---|---|---|
| **Boundary / Stokes / cohomology** | Boundary operators, exterior-derivative or divergence-like local-to-global relations, flows, closed/exact splits, and topological obstructions. | Use when local rules, interfaces, flows, or balances must be related to a global claim or blocked global extension. | Does not license all boundary phenomena as the same physical mechanism; evidence, measurement, and bridges remain neighboring work. | `F.9`, `A.19`, `C.16`, `A.10` |
| **Obstruction-first / failed-transfer lens** | Impossibility, incompatibility, failed composition, blocked transfer, missing invariant, or diagnostic boundary. | Use when the useful mathematical result marks where a transfer, comparison, model, or simplification stops. | Does not make the rival claim true or the failure cause known without neighboring support. | `F.9`, `A.6.P`, `A.10`, `E.19` |
| **Symmetry / invariance / equivariance / Noether** | Group actions, invariants, equivariant representations, conservation-like constraints, and geometric-deep-learning regularities. | If the problem depends on sameness under transformations or a conservation-like claim, ask which transformations are admissible, what remains invariant, and which distinctions are lost. | Does not transfer physical conservation law, causal mechanism, or coordinate-free truth without domain evidence. | `A.10`, `C.16`, `A.19`, domain pattern |
| **Variational / action / optimization / Legendre** | Action, energy, free-energy, loss, value, entropy, or resource functionals; stationarity, extrema, dual variables, potentials, and Legendre or convex duality. | Use when the useful lens is an extremal condition, admissible variation space, boundary condition, dual view, or trade-off. | Does not imply the target literally optimizes unless dynamics and evidence support it. | `A.3.3`, `C.28`, `A.10` |
| **Diagonal / self-reference / no-go** | Self-application, universal evaluators, closure limits, diagonal constructions, and impossibility boundaries. | Use when the payoff is to block a tempting universal claim or expose a closure boundary. | Does not prove every recursive-looking case is a diagonal or no-go case. | `B.3`, `E.19`, local domain pattern |
| **RG / coarse-graining / fixed point / universality** | Why different micromodels yield one macropattern; fixed points, basins, scale windows, universality classes, or stable-law-like alternatives. | Use for scale transitions, abstraction, domain compression, and macropattern claims that require a declared scale variable and coarse-graining rule. | Does not assert micro-mechanism identity or universal validity outside `ScaleWindow`. | `C.18.1`, `C.19.1`, `A.3.3` |
| **Category / compositionality / optics / semiring-limit** | Composition, interfaces, views, transformations, algebraic laws, limit transforms, and cases where changing algebra changes what is preserved. | Multi-view architecture, bridges, system composition, and classical/tropical or Fourier-Laplace/Legendre-style transform cues. | Does not imply all target objects are categories or that every functor-like transfer preserves the needed structure. | `F.9`, `A.6.P`, `A.19` |
| **Information geometry / learning dynamics** | Update, curvature, optimization trajectory. | Adaptive systems, learning agents, epistemic dynamics. | Does not license “everything is learning” ontology. | `A.3.3`, `A.10`, `C.28` |
| **Optimal transport / distribution geometry** | Transport plans, Wasserstein-like geometry, couplings, costed movement between distributions, populations, shapes, or allocations. | Use when the question is how one distribution, population, shape, or allocation can move toward another under declared costs and losses. | Does not license causality, fairness, mechanism, or policy effect by itself. | `C.16`, `A.10`, `C.28`, `D.5` |
| **Operator learning / SciML / latent representations** | Learned function-to-function operators, neural operators, surrogate solvers, embeddings, and world-model representations. | Use when the first useful lens is an operator over functions, states, or fields; name the observation map, training or simulation regime, validation slice, and generalization boundary. | Does not license out-of-domain solver replacement, causal mechanism, or unobserved state truth without validation and neighboring support. | `A.10`, `C.16`, `A.3.3`, `C.28` |
| **Koopman / operator-theoretic dynamics** | Observables or coordinates where nonlinear dynamics can be represented by an operator, often approximately linear. | Use when nonlinear dynamics need a tractable forecast, control, or diagnostic representation; name the observable/readout and the forecast or control use being tested. | Does not prove a real linear mechanism or temporal-use adequacy; dynamics semantics, evidence, and temporal claims stay with `A.3.3`, `A.10`, and `C.27`. | `A.3.3`, `A.10`, `C.27` |
| **Causal representation / causal abstraction** | Causal graphs, SCMs, causal representation learning, micro/macro mappings, quotient models, and intervention-preservation questions. | If the user asks what to change to get an effect, test causal graph, SCM, or causal abstraction as the candidate lens, not correlation graph or latent manifold by default. | `C.29` can state lens adequacy only; causal-use support, intervention claims, and counterfactual reliance stay with `C.28`. | `C.28`, `A.10`, `A.3.3` |
| **Quantum-like / contextual probability** | Probe effects, incompatible frames, order effects. | Dashboards, workshops, surveys, measurement-as-intervention. | Quantum-like is not physical quantum unless separate physics evidence is supplied. | `C.26`, `C.16`, `F.9` |

### C.29:15 - Relations

- **Builds on:** `A.1.1`, `A.6.P`, `A.3.3`, `A.19`, `A.10`, `A.15`, `B.3`, `C.16.P`, `C.16`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, `F.9`.
- **Constrained by:** `E.8`, `E.10`, `C.2.P`, `E.19`.
- **Decision basis:** `E.9` design-rationale discipline and the source-basis rows in `C.29:13a`.
- **Supports:** `E.2` pillar-impact analysis when a pillar argument relies on mathematical first-principles structure; only lens adequacy is in scope, with no amendment to pillar content, priority, or constitutional authority.

- **Coordinates with:** `C.11`, `A.15.1`, `A.15.4`, `C.18.1`, `C.19.1`, `C.26`, `C.27`, `C.28`, `G.5`, `G.9`, `G.2`, `G.10`.
- **Specialization relation:** `C.26` is selected as an MLA-compatible specialization for quantum-like modeling, with affordability qualifications.
- **Does not replace:** `F.9` bridges, `C.28` causal-use discipline, `A.3.3` dynamics semantics, `A.19` characteristic-space governance, `C.16` measurement construction, scale legality, direct comparability, and evidence-stub adequacy, `A.10` and `B.3` evidence and assurance, `C.11` decision records, `A.15`/`A.15.1`/`A.15.4` method and work records, `E.17.EFP` explanation-use discipline, `E.17.ID.CR` comparative review units, `A.6.3.RT` representation transitions, `A.6.3.CSC` coarsening, `C.27` temporal-claim adequacy, `C.18.1` and `C.19.1` scale-law and BLP support, or G-pattern selector and benchmark work.


### C.29:End

