## C.29 - Mathematical Lens Use

> **Type:** Architectural pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Mathematical lens use.

**Primary EntityOfConcern.** The use of a mathematical representation to answer a stated working question, with an explicit correspondence to the phenomenon and limits on the resulting inference.

**Use this when.** Use C.29 when choosing or transferring a mathematical representation could expose a needed relation, invariant, obstruction, approximation or resource limit, or when an existing representation is being relied on beyond what its correspondence supports. The related Methods in C.29.1, C.29.2 and C.29.3 respectively construct a result transfer, a computation and its realization. Enter the Method whose contribution is missing; B.5.MPC connects these contributions to a physical question.

**What goes wrong if missed.** The reader either misses a useful mathematical construction or carries a result into a situation where a needed assumption or distinction has been lost.

**What this buys.** A concrete mathematical question, a representation that makes it tractable, and a consequence that changes what to calculate, observe, compare or rule out.

**Not this pattern when.** An adequate local equation, algorithm or domain model already answers the question and no separate representation or transfer issue remains. Complete that work without a C.29 note. A one-off metaphor used only for orientation also needs no card.

### C.29:0 - First mathematical move

Ask what you need to find out. Choose the smallest mathematical object that could answer it; say how its elements and operations correspond to the working situation. Identify the structure needed for the inference, the distinctions omitted, and the assumptions on which the result depends. Derive a consequence, then decide what it changes and what would defeat its use.

For waiting work, a queue candidate turns “slow flow” into questions about arrivals, service and waiting. For a proposed dense state array, counting its entries can already rule out an implementation. For a familiar local calculation such as `V = IR` under its accepted conditions, use the equation directly: the calculation does not require a lens-use record.

If no concrete object can yet be chosen, retain the working cue and the next observation or construction as a candidate. **B.5.FM** helps when the participants or interactions needed to formulate that mathematical question are still unclear. A family label remains a discovery cue until a concrete object and correspondence are supplied. Recording options in :4.4 serve later inspection or reuse of the result; the mathematical operation comes first.

### C.29:1 - Problem frame

A mathematical representation can make a working question answerable by exposing the relations needed for an inference. It may combine source cases into a summary, change coordinates without losing distinctions, or embed the source in a larger mathematical domain. Each construction supports different uses. A queue may expose flow restrictions while omitting rework; an extension of the rational numbers to the reals makes limits available while retaining rational arithmetic.

C.29 addresses this representation choice and its use across a stated correspondence. It begins either with a working problem that needs a useful construction or with a proposed representation whose consequence needs to be derived, limited or rejected. Domain theory supplies the mathematical laws and application conditions.

> **A useful mathematical lens makes a needed inference possible through an explained correspondence.**

Ask what the correspondence preserves, omits or introduces, which operations it supports, and how the resulting conclusion answers the working question.

#### C.29:1.1 - First-minute working situation

A production manager sees waiting work but cannot tell whether an extra station would help. The first task is to distinguish an arrival restriction, a service bottleneck and a batching effect. The candidate queue has to make at least one of those distinctions calculable or observable. The discovery cues in :4.2b help choose an object; they are not a required tour of mathematical families.

#### C.29:1.2 - Minimum scenario and anti-case set

**Positive scenario.** In :4.4's two-station queue, the departure recurrence distinguishes a five-minute latency reduction from a change in sustained output. The next observation focuses on the slower station. Changed service time or finite-buffer blocking withdraws the affected calculation; actual capacity reliance requires checking the model against the line.

**Anti-case.** “The organization is a quantum system” is written without a candidate mathematical object, probe distinction or readout distinction, preserved structure, lost structure, `LensUseBoundaryValue`, or stop condition. The `C.29` result is either a downgrade to local metaphor or a repaired use through `C.29` and, where relevant, `C.26`.

**Under-lensed anti-case.** “The work stream has dynamics” or “this portfolio is a network” is used for a diagnosis that affects prediction, comparison, repair, or stop conditions, but no mathematical object changes what can be predicted, compared, diagnosed, repaired, or stopped. The repair is to choose a cheap candidate lens that exposes useful structure, or keep the sentence as ordinary prose.

**False-positive scenario.** A Markov kernel appears inside accepted local reliability modeling. When no separate representation or transfer question is open, complete the A.3.3 result without a C.29 output. If such a question arises, use the reliance rule in :4.4.

#### C.29:1.3 - Intended FPF use-value

The useful result is an answer, bound, obstruction, diagnostic split or next observation that the working reader could not recover from the prior account. Keep the correspondence and limitations inspectable when someone will reuse that result. A more elaborate record is useful only for the information its receiving use needs.

### C.29:2 - Problem

A broad name such as “graph”, “field”, “dynamics” or “quantum-like” does not yet identify the mathematical object or yield a consequence. Conversely, a valid derivation inside a model may be transferred to a case whose necessary structure the representation does not preserve.

The practitioner therefore needs both construction and criticism: make the relevant structure explicit, perform the mathematical operation, and test whether its result answers the original question under the stated conditions.

### C.29:3 - Forces

| Force | Tension |
|---|---|
| **Useful representation vs justified return** | A summary, coordinate change or larger mathematical domain can simplify an inference. Returning its result requires the correspondence and conditions that support the source question. |
| **Plural mathematical foundations vs FPF simplicity** | Different foundations and constructions open different operations; choose them for the question and explain the needed correspondence. |
| **First-use effort vs later scrutiny** | A first calculation may need only a stated correspondence and assumptions; consequential reuse needs a recoverable argument, losses and validation. |
| **Transfer reach vs domain fit** | Cross-domain transfer can expose useful structure. Establish the correspondence and material losses for the receiving question before relying on the transferred lens. |

### C.29:4 - Solution - selected answer

#### C.29:4.1 - Construct and test the correspondence

1. **State the working question.** Name the quantity, relation, distinction or possibility that would change the next action. Recover the intended use and the precision or range it needs.
2. **Choose a concrete mathematical object.** Specify its elements, variables, relations, operations and constraints. Use the least costly adequate local theory or construction. A family name is a discovery cue; if no object is yet available, keep a candidate and name the next observation or construction.
3. **Establish the correspondence.** Say what each relevant element or operation represents and in what direction the inference is used. Distinguish an analogy, a fitted representation, a simulation and an exact structure-preserving map. State the assumptions, scale and context that the correspondence requires.
4. **Determine what the correspondence preserves, omits or introduces.** Identify the structure on which the intended result relies and any omitted distinction that could change it. Establish the preservation claimed for the needed operations. If the receiving domain adds objects or operations, determine which of their results answer the source question. C.29.1 constructs these comparisons, including cases with no loss of source distinctions and cases where a receiving solution has no source counterpart.
5. **Do the mathematical work.** Calculate, derive, construct or demonstrate the obstruction. For a missing computational formulation or procedure, use C.29.2; for an unsettled connection to an executing system, use C.29.3. Return the result through the correspondence to the working question. A statement that a queue “exposes bottlenecks” is not yet the bottleneck calculation.
6. **Choose the resulting action and its limit.** Use the result within its assumptions, collect a discriminating observation, compare a relevant rival, narrow the question or reject the representation. Test the material loss and changed premises. When another person or later use needs the account, retain the smallest sufficient record under :4.4.

##### C.29:4.1.1 - Transfer the result through the operations

A source operation or result is available, and you need to use it through another representation. Use **C.29.1 - Mathematical Result Transfer** to recover the operation and its permissions, compare performing then mapping with mapping then performing, and test whether choosing another represented source case changes the answer.

Its Solution constructs a transferable consequence, a justified bound or a specific repair of the correspondence. It also separates a receiving operation that gives a useful relaxation from one whose result can be realized as a source action. The reservation and route-cost entries in :7.1–:7.2 lead to its worked constructions.

##### C.29:4.1.2 - Construct a computation for the question

The needed answer is identified, but the available representation and operations do not yet explain how to obtain it. Use **C.29.2 - Computational Formulation** to select the distinctions retained in computational state, construct a procedure or solver formulation, establish the claimed result and estimate the cost that matters to its use.

Its Solution starts from either a question or available computational means. Worked cases develop an interpreter, a bounded root calculation, a memory-limited quantum-state representation, two questions about the same circuit, and a probability estimate. The result is a usable computation under stated conditions or the missing construction that prevents it.

##### C.29:4.1.3 - Realize the computation and read its result

A computation is available, but how a concrete system performs it is unsettled. Use **C.29.3 - Computational Realization** to connect input preparation, system actions and result interpretation, then compare the required result with the interpreted execution. For a design calculation, the comparison uses the supplied system model; a claim about an actual run uses its observations.

The result is a conditional realization, an interpreted result or a located failure in preparation, operation or readout. Digital, analog, stochastic and manual arrangements can enter through the same question. Its robot, analog addition and admission-card cases show repairs of range, scale and shared-state conditions. B.5.MPC coordinates these results with the physical account, mathematical construction and receiving action.

#### C.29:4.2 - Mathematical Lens Use Principle

A mathematical lens is useful for a stated question when its correspondence preserves the structure needed for an actual consequence and makes the material losses explicit. A proof under mathematical assumptions establishes that consequence inside the model. Reliance on the phenomenon additionally requires the correspondence and application conditions to hold; prediction and other model-bearing uses require their validation under :4.5a.

Plain phrases such as “what survives transfer” can guide recognition. For a used result, make the actual correspondence, preserved structure, loss and stopping condition recoverable. Include a blocked overread only when it passes F.19's plausible-reader test.

#### C.29:4.2a - When mathematicalization pays

Introduce a representation when it changes what can be derived, compared, observed, constructed or ruled out for the working question. An adequate ordinary calculation may already supply the answer. If no useful consequence or next inquiry follows, keep ordinary prose or the domain result; no C.29 output is required.

#### C.29:4.2b - Discover a candidate from the working cue

Choose the row that fits the problem, or use a closer domain construction. The menu is informative; when a listed construction is used, its named mathematical elements and conditions must be supplied. The shared test is :4.1, not membership in this list.

| Working cue | Candidate structure and first mathematical work | Conditions that can change the use |
| --- | --- | --- |
| Waiting, backlog, throughput | Queue or flow network: identify stations, routing, arrivals, service and waiting; derive a capacity bound or waiting relation. | Check discipline, batching, rework, finite buffers and station availability before applying the result. |
| State change, trajectory, stabilization or control | State space, Markov model, ODE or control model: name state, transition law and constraints; add an observation map when the receiving use needs it. | A.3.3 supplies dynamics semantics; C.27.TA and C.27 apply to the temporal aspect and temporal-use claim being made. |
| Conditional independence or computational-boundary cue | Probabilistic graph, Markov blanket or active-inference model: state variables, conditional-independence assumptions, observation/action partition and model boundary. | Recover a separately claimed physical interface, component or agency condition through its direct pattern. |
| Dependency, interface, composition or change of algebra | Graph, hypergraph, category, operad, optic or semiring: state edge/slot meanings, objects, morphisms, identities, interface conditions and composition laws; test the required composition or transform. | Classical, tropical, Fourier–Laplace or Legendre transforms can change the retained law. F.9 supplies cross-context semantic correspondence when needed. |
| Local-to-global flow or balance | Boundary operator, exterior derivative, divergence or Stokes-like construction: name domain, boundary, field/form/flow, local operator, boundary conditions and source or conservation balance. | The chosen domain law and regularity assumptions must support the global inference. |
| Local rule with no global extension | Cohomology, closed/exact distinction or another obstruction: identify the cycle/cocycle, equivalence class, local closure and failed global witness. | Use the obstruction to delimit this transfer; the failure does not select the rival model or identify a cause. |
| Sameness under transformations | Group action, symmetry, invariant or equivariant representation: identify transformations, action on variables and preserved quantity; derive a conservation link only under its theorem's assumptions. | State coordinate details and distinctions lost; a physical conservation claim needs its domain basis. |
| Extremum, trade-off, potential or dual view | Variational, Lagrangian/Hamiltonian, action, energy, free-energy, loss, value or entropy functional; constrained optimization or Legendre/convex duality. Name variation space, constraints, boundary conditions and stationarity/extremum or dual transform. | A system's actually following that extremum is a separate dynamics or causal question. |
| Similarity, distribution shift, population or shape movement | Metric, topology, order, embedding, coupling or optimal transport: define neighborhood/distance or transport plan, conserved mass and cost; calculate the comparison. | State what is transported and lost. C.16 supplies a used measurement/comparability construction; a policy effect or fairness claim needs its own argument. |
| Scale transition, coarse behavior, universality or knee | Coarse-graining, RG or fixed-point view: name scale variable/window, coarse-graining rule, fixed point or attractor, basin/regularity assumptions and invariant or exponent. | Return to the microdescription when an omitted distinction matters. C.18.1, C.19.1 and C.31.ASAP supply the separately claimed scale-law, method preference and architecture preference results. |
| Self-reference or a universal evaluator | Diagonal, self-application or fixed-point construction: specify encoding, evaluator/self-map, tested universal claim and exact obstruction. | A recursive-looking loop alone does not establish a no-go result. |
| Uncertainty, missing observation or next sample | Probability/information measure, Bayesian workflow, BED/OED, active learning or Bayesian optimization: state variables, priors/likelihood, utility or information criterion, design/acquisition variable and estimation method. | Check prior-data conflict, predictive mismatch, estimation cost, uncertainty and robustness to model/noise error; use the result within its validation boundary. |
| Recoverable structure under a resource bound | MDL, epiplexity or another code/measure: name source episteme/trace, observer, admissible model/coding scheme and execution bound; distinguish selected structure from residual description. | Apply the correspondence and observation/postulate boundary in :4.2c; return to source when the discarded structure matters. |
| Learning update, curvature or optimization trajectory | Information geometry or a learning-dynamics model: specify update variables, metric/noise relation and the property being calculated. | Establish the mapping to the particular learning process before using the result beyond the formal model. |
| Nonlinear dynamics needing a tractable observable | Koopman/operator, DMD or system-identification construction: select observables, operator and approximation; derive the forecast or diagnostic consequence. | Finite closure and predictive/control validity need checking; A.3.3 and C.27 supply the actual dynamics and temporal-use conditions. |
| Learned scientific representation or surrogate solver | Neural operator, latent representation, embedding or world model: specify function/state/field mapping, observation map, training or simulation regime and resolution policy. | Apply :4.5a's learned-lens and validation conditions, including generalization scope and approximation loss. |
| Intervention, policy effect or counterfactual | SCM, causal graph or micro-to-macro causal abstraction: specify assignment/intervention, outcome and preserved or approximated intervention/counterfactual structure. | C.28 supplies identification and causal-use justification; an associative graph or latent manifold may not answer this question. |
| Probe, order or context effect with incompatible frames | Quantum-like or contextual-probability model: identify the contextual obstruction that still changes inference or action after the ordinary subject patterns. | Apply C.26's adequacy conditions. A physical quantum claim additionally needs the relevant physics and observations. |
| Storage, computational or realizability limit | Count actual represented objects and operations; apply a resource bound or constructive/impossibility argument. | Recompute for the actual alternative representation. A valid rejection of one implementation does not yet supply a feasible replacement. |

For a constrained extremum or stationary construction, construct or reuse a family of allowed candidates and calculate the resulting change in the target quantity. Distinguish an improving candidate, a necessary stationary condition and a justified optimum; carry the resulting conclusion and its assumptions into the working question.

For a symmetry argument, follow the transformation through the problem's data, conditions and required answer. Derive the transferred solution, restriction or obstruction to selection, and say which problem that consequence answers.

When a balance must be constructed or its boundary changes, C.29.BB identifies the additive quantity, included stores and crossing transfers. It combines compatible accounts and returns the total, a bound or the missing contribution.

For a first candidate, compare with ordinary prose, direct observation or the accepted domain model before a broader survey. When the question is a tradition-scale source synthesis, use G.2; C.29 needs only the candidate or rival relevant to this working question.

When expected information gain determines which observation to obtain, choose a feasible way to estimate it. If density approximations are used, allocate samples between fitting them and computing the expected gain. In high dimensions, consider reducing the parameter or observation space and account for the information lost by that reduction. Compare estimation cost and error with the distinction needed for the choice. [Li, Baptista and Marzouk (2026)](https://arxiv.org/abs/2411.08390v3) develop these sample-allocation and dimension-reduction choices.

#### C.29:4.2c - Bounded-observer structural-information lens

Use this subcase when a mathematical lens estimates, compresses, codes, compares, or otherwise exposes how much selected structure a bounded observer can recover from a description, relation trace, generated graph, model, or reusable-structure accounting result. Typical examples include MDL-like two-part codes, epiplexity-style extracted-structure estimates, compression-complexity comparisons, and information-functionals over relation graphs.

`C.2.8` defines extractable structural information for the episteme, expressing form and observer under stated conditions. When this lens output is used to estimate that characteristic, state how its mathematical objects, admissible models, selected structure and resource bound correspond to those conditions. A comparison that uses an adequate domain method directly needs no mathematical lens.

For an epiplexity estimate, distinguish the selected model's description length from the residual data description, the model-execution bound from estimation effort, and conditional model information from all familiar structure a reader can recover. Use the existing source, mapping, preserved/lost-structure and stop fields to state the correspondence. The formal model and its application conditions are explained in `C.2.8:4.6`; a numerical measurement claim also uses `C.16`.

Minimum record:

```text
MathLensUse.StructuralInformationLensUse@Context:
  TargetPhenomenon:
  SourceEpistemeOrTraceRef:
  BoundedObserverRef or observerBoundary:
  CandidateMathObject:
  LensMappingMode:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  ObservationBoundary?:
  PostulateBoundary?:
  SourceReturnCondition?:
  LensUseBoundaryValue:
  declaredLensUse:
  StopCondition:
  blockedLensOverread?:
```

When the target is a physical, organizational, or project-world situation, the record must say whether the structural-information claim is observational, postulated, simulated, or only a description-local compression. When the lens is used in architecturing, `C.30` governs architecture as EntityOfConcern, `C.30.ASV` governs structural-view adequacy, `C.30.AD` governs architecture descriptions, and `C.31` or `C.31.RSA` governs modularity or reusable-structure accounting. `C.29` records only the declared lens use: what recoverable structure the mathematical lens makes visible, what it loses, and where that use stops.

#### C.29:4.2d - Architecture-local lens descriptions

Architecture work may use C.29-local descriptions for graph, flow, control, structural-information, RG or coarse-graining, and multilevel-learning or frustration lenses.

| Local C.29 description | Candidate mathematical object | Visible payoff | Stop condition |
| --- | --- | --- | --- |
| `MLU.Description@ArchitectureGraphDSM` | typed graph, hypergraph, DSM, DMM, or MDM matrix | dependencies, clusters, change propagation, and bottlenecks | for semantic interface correctness, compositional quality, or an architecture decision, apply the pattern for that separate claim |
| `MLU.Description@TransformationFlowStructure` | graph, morphism-family, wiring, matrix, or network expression over a selected `TransformationFlowStructure` | flow topology, crossings, carried relations, and path slices without hidden scalarization | for a Work occurrence, gate decision, or evidence claim, apply its subject pattern |
| `MLU.Description@ArchitectureLCA` | layered control structure or multi-rate control model | planner, regulator, plant, observer, feedback timing, and externality separation | stability or causal-use questions require their dynamics, evidence, and `C.28` basis |
| `MLU.Description@EpiplexityStructuralInformation` | bounded-observer structural information or two-part code | learnable reusable structure versus residual or unmodeled structure | establish any utility, assurance, out-of-distribution guarantee, or causal-proof claim through its subject pattern |
| `MLU.Description@RGArchitecture` | scale map over architecture descriptions, fixed-point or basin metaphor, or declared coarse-graining map | scale-stability of an architecture vector and exploding exceptions | a literal physical-RG claim requires its domain theory |
| `MLU.Description@MultilevelLearningFrustration` | multilevel learning over structurally renormalizable descriptions, frustrated optimization landscape, or variational residual model | residual-reducing architecture moves across declared scopes or holon levels | a project-wide optimization claim requires a separately justified global function |

`MLU.Description@RGArchitecture` applies only when the use names a declared aggregation scope, scale variable or scale window, coarse-graining rule, preserved structure, lost structure, source-return condition, declared use, and stop condition. Include a blocked overread only when it passes F.19's plausible-reader test. If the claim becomes a scale-preference claim, `C.31.ASAP` governs the architecture preference side; C.29 keeps the declared mathematical-lens use.

Minimum RG architecture description:

```text
MLU.Description@RGArchitecture:
  TargetPhenomenon:
  CandidateMathObject:
  LensMappingMode:
  ScaleWindow?:
  CoarseGrainingRule?:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  SourceReturnCondition?:
  declaredLensUse:
  NextLensUseAction:
  StopCondition:
  blockedLensOverread?:
```

For architecture work, a common RG-shaped candidate object is:

```text
A_l = (Holons_l, FunctionalRelations_l, FlowRelations_l, ControlRelations_l,
       ModuleRelations_l, InterfaceSpecificationRefs_l, DependencyEdges_l,
       WorkMethodRefs_l, EvidencePackageRefs_l, QualifierRefs_l)

R_l : A_l -> A_{l+1}
```

`InterfaceSpecificationRefs_l` contains only governed `U.EpistemeRef` values that resolve independently identified `InterfaceSpecification` epistemes under the identifying rule located at A.6.M. The references, their resolution, and the specification content remain separate; changing a lens token or retargeting a reference does not edit the specification.

The index `_l` is a declared aggregation-scope index inside this C.29 lens, not a generic level, tier, layer, or ladder. Each use names the aggregation scope, the coarse-graining rule, the lost structure, and the source-return condition.

`MLU.Description@MultilevelLearningFrustration` applies only when the use names declared holon levels or declared scopes, a mapping between them, conflicting constraints or residuals, preserved structure, lost structure, and the nearest neighboring FPF pattern for any measurement, causal, evidence, assurance, work, selected-set, or decision claim.

Minimum multilevel-learning and frustration description:

```text
MLU.Description@MultilevelLearningFrustration:
  TargetPhenomenon:
  CandidateMathObject:
  LensMappingMode:
  PreservedStructure:
  LostStructure:
  VisiblePayoff:
  declaredLensUse:
  NextLensUseAction:
  SourceReturnCondition?:
  StopCondition:
  blockedLensOverread?:
```

Declared lens use: triage, explanation, candidate generation, rival-lens comparison, scale-window reasoning, source-return triggers, and architecture-decision rationale only when the neighboring pattern defines or constrains any non-C.29 claim. Stop or return when the mapping, scale window, preserved structure, or source basis no longer supports the use. A causal-proof, assurance-score, or necessary-complexity-growth claim needs its own argument and source basis. Apply `C.11`, `C.28`, `B.3`, `C.16`, `G.5`, or the applicable stakeholder or ethics pattern when its respective non-C.29 claim is current. Include a project-wide-optimizer or other blocked overread only when it passes F.19's plausible-reader test.

#### C.29:4.3 - Use boundary

Use C.29 for a consequential choice or transfer of mathematical representation. Ordinary equations, data structures and accepted domain models remain usable directly when no such issue is open. A separate causal, measurement, dynamics, semantic-bridge or other claim uses its subject pattern under :4.4.6.

Use **structure-preserving representation** in discoverability-bearing prose unless equivalence or identity is explicitly the justified mapping mode.

#### C.29:4.4 - Record the result for its receiving use

First complete or delimit the mathematical move in :4.1. Record its question, concrete object, correspondence, retained and lost structure, consequence and next action when another reader or later reliance needs them. Choose the smallest sufficient form below; a form does not replace a missing construction, derivation or observation.

**One reliance rule.** A conditional derivation, diagnostic comparison or reusable explanation may remain a MiniCard when it retains the same object, assumptions, correspondence, loss and narrow use, and its consequence is used to understand the model or choose the next inquiry. A FullCard is required when the result is relied on as an adequate model of the phenomenon for prediction, an operational or consequential decision, model adoption, benchmark or assurance input, Bridge-dependent reliance, or transfer as a reusable model to further cases. It then needs the applicability, rival and validation information relevant to that reliance. Publication or repetition of the same conditional explanation alone does not change its class.

Keep adequate existing domain/model documentation and refer to it; FullCard means a recoverable full account, not recopying that information into a blank form. Reassess the same rule whenever the intended use or reliance changes.

Application output classes:

| Output class | Output | Use condition | Required content |
|---|---|---|---|
| `NoMathLensUseNeeded` | No C.29 output; keep the ordinary local result or Plain orientation | Accepted local mathematics or didactic language makes no separate lens-use claim requiring resolution. | Finish with the local result. A short `NoMathLensUseNeededNote` is useful only when a proposed or disputed lens use needs an explanation; it is not a certificate required for ordinary local mathematics. |
| `LensCandidateNote` | `MathLensUse.LensCandidateNote` | A problem whose next lens-use action can depend on a mathematical lens is stable enough for a first candidate lens, but no adequate mathematical object has been named yet. | `TargetPhenomenon`, `ProblemStructureCue`, `CandidateLensFamily`, optional `CandidateMathObject?`, `WhyThisLensCouldHelp`, `ExpectedVisiblePayoff`, `ObservableOrControllableCue?`, `NextLensUseAction`, `OrdinaryRivalOrFallback`, `StopCondition`, `NextMathLensUseOutput`. |
| `OneLine` | `MathLensUse.OneLine` | A concrete object and correspondence can support a bounded first inspection or repaired phrase; adequacy for further reliance remains open. | `TargetPhenomenon`, `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `VisiblePayoff`, `NextLensUseAction`, optional `ObservationOrReadoutNeeded?`, `OrdinaryRivalOrFallback`, `StopCondition`. |
| `MiniCard` | `MathLensUse.MiniCard` | Conditional derivation, diagnostic comparison, choice of a next inquiry, or reusable explanation within the same declared assumptions and losses. | `OneLine` content plus `InvariantsExposed`, `LensUseBoundaryValue`, `declaredLensUse`, optional `blockedLensOverread?`, principal rival, and `RivalLensRelation?` when another mathematical lens changes the bounded action. |
| `FullCard` | `MathLensUse.FullCard` | Reliance on the result as an adequate phenomenon model under the rule above. | Full `MathLensUse.Card@Context`, using existing references where adequate, plus the applicable overlays and receiving subject-pattern result. |
| `NeighborGoverningPatternNote` | `NeighborGoverningPatternNote` | The next action concerns a separately governed question. | Name that question and follow its receiving action in :4.4.6. |

Micro-template examples:

Architecture and P2W first-use slice:

```text
MathLensUse.LensCandidateNote@ArchitectureP2W := {
  TargetPhenomenon: cooling-fixture deformation problem accepted as a problem-side distinction,
  ProblemStructureCue: heat-flow balance, boundary condition, interface reference plane, and deformation residual change the next architecture or method-choice question,
  CandidateLensFamily: boundary and variational heat-flow lens,
  CandidateMathObject?: temperature field with boundary-condition relation and optional energy functional,
  WhyThisLensCouldHelp: the lens can expose whether the useful distinction is a preserved heat-flow invariant, a boundary-condition mismatch, or a deformation factor outside the model,
  ExpectedVisiblePayoff: a net heat-flow imbalance would require stored-energy change; a balanced total alone would still leave the spatial gradient needed for the deformation question unresolved,
  ObservableOrControllableCue?: boundary temperatures, heat-flow observations, reference-plane assignment, deformation readout,
  NextLensUseAction: define the fixture control volume and heat paths; compare measured inflow and outflow, then obtain spatial temperatures and mechanical constraints before deriving deformation,
  OrdinaryRivalOrFallback: ordinary deformation narrative plus local measurement note,
  StopCondition: keep this as a candidate until the heat balance and temperature-to-deformation correspondence are specified; return to the deformation question when omitted gradients or constraints can change its answer,
  NextMathLensUseOutput: MathLensUse.OneLine or NeighborGoverningPatternNote
}
```

The heat balance is the proposed first mathematical operation. A formal vocabulary/law declaration uses A.6.0 only when that separate declaration is needed; carrying accepted problem-side distinctions into later work uses E.18.1. The receiving conditions are stated in :4.4.6.


```text
MathLensUse.LensCandidateNote example := {
  TargetPhenomenon: slow Product-X team flow,
  ProblemStructureCue: waiting and work-in-progress look more important than individual task difficulty,
  CandidateLensFamily: queue or flow lens,
  CandidateMathObject?: single-server or multi-server queue candidate,
  WhyThisLensCouldHelp: arrivals, service time, WIP, and waiting time could expose the bottleneck,
  ExpectedVisiblePayoff: decide whether delay is arrival-rate, service-rate, batching, or WIP-boundary pressure,
  ObservableOrControllableCue?: arrivals, service time, wait time, WIP limit,
  NextLensUseAction: observe the variables before claiming queue adequacy,
  OrdinaryRivalOrFallback: ordinary process narrative without queue assumptions,
  StopCondition: stay with the candidate note until observations support queue adequacy; use the ordinary process narrative if the queue candidate does not change the next action,
  NextMathLensUseOutput: NoMathLensUseNeededNote or MathLensUse.OneLine after observation
}
```

```text
MathLensUse.OneLine example := {
  TargetPhenomenon: Product-X backlog delay,
  CandidateMathObject: queue model over arrivals, service time, waiting time, and work in progress,
  LensMappingMode: representation,
  PreservedStructure: flow, bottleneck candidates, wait, WIP, service-rate pressure,
  LostStructure: motivation, priority politics, contractual duties, skill learning, quality of work,
  VisiblePayoff: identify whether delay is arrival-rate, service-rate, batching, or WIP-boundary problem,
  NextLensUseAction: observe arrivals, service, wait, and WIP; test one local WIP-limit or batching hypothesis,
  ObservationOrReadoutNeeded?: service-time and wait-time observations,
  OrdinaryRivalOrFallback: process narrative without queue assumptions,
  StopCondition: return to the process narrative or choose another lens when observations do not support the queue representation or its declared losses prevent the next action
}
```

**Worked conditional queue comparison.** A production manager asks whether speeding station A would raise the line's output, or whether the next investigation should focus on B. Use an authored, stipulated case: identical jobs arrive at `a_n = 10n` minutes, starting with `n = 0`, and pass through A then B. Both stations have one server, first-come-first-served non-preemptive service, no failures or rework, and an unbounded intermediate queue in the model. For a finite run the same calculation applies while its actual buffer does not fill. Transfer time is zero. A takes 10 minutes per job; B takes 15. The line starts empty.

The mathematical object is a deterministic two-station tandem queue. A job represents one part; an arrival is its release to A; service is uninterrupted processing at the named station; a departure from A is the arrival at B. This preserves order, routing, occupied service time and interstation waiting. Variable product mix, stoppages, rework and finite-buffer blocking are omitted. The network correspondence and the importance of blocking are introduced in [Wu's queueing-network lecture, slides 9 and 23–24](https://web.mit.edu/1.041/spring2023/lectures/L10-queuing-network-models-2023sp.pdf); the following deterministic numbers and derivation are constructed here.

A job can start only after it has arrived and the previous job has left that station. With previous departures initialized to zero, its departure times therefore obey:

```text
d_A(n) = max(a_n, d_A(n−1)) + 10
d_B(n) = max(d_A(n), d_B(n−1)) + 15
d_A(−1) = d_B(−1) = 0
```

| Job n | Arrival a_n, min | Departure A, min | Departure B, min | Total latency, min |
| --- | --- | --- | --- | --- |
| 0 | 0 | 10 | 25 | 25 |
| 1 | 10 | 20 | 40 | 30 |
| 2 | 20 | 30 | 55 | 35 |
| 3 | 30 | 40 | 70 | 40 |

The recurrence gives `d_A(n) = 10n + 10` and `d_B(n) = 15n + 25`: after its first arrival B remains occupied. The output spacing is 15 minutes, hence the long-run rate is 4 jobs/hour. The station-capacity bound is `min(6, 4) = 4` jobs/hour, attained in this stipulated run. Latency is `d_B(n) − a_n = 25 + 5n` minutes. It keeps growing; the calculation supplies no finite steady-state mean delay.

Now halve A's service time to 5 minutes while leaving the arrivals and B unchanged. The same recurrence gives `d_A(n) = 10n + 5` and `d_B(n) = 15n + 20`. The rate is still 4 jobs/hour; each job's latency falls by 5 minutes but still grows with n. The useful distinction is between a shorter initial traversal and a higher sustained output rate. The next inquiry is therefore to observe B's service, interruptions and queue growth, and test whether its assumed restriction describes this line. An observed-output dashboard is the ordinary fallback and a complementary check; output counts alone do not derive the two station-change scenarios.

**Use and return.** This is a MiniCard-level conditional derivation and comparison, reusable with the same premises. It directs observation, not a capacity commitment about an unvalidated line. Actual prediction, equipment selection or operational reliance uses :4.4's full applicable account and :4.5a's validation. Keeping A's original 10-minute service, if an omitted inspection adds 5 minutes to every B service, B's service becomes 20 minutes: `d_B(n) = 20n + 30`, the rate is 3 jobs/hour and latency is `30 + 10n`. Withdraw the 4-job/hour and `25 + 5n` results. If finite storage instead blocks A, reconstruct the blocked-service recurrence before reusing the schedule.

```text
MathLensUse.OneLine := {
  TargetPhenomenon,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  VisiblePayoff,
  NextLensUseAction,
  ObservationOrReadoutNeeded?,
  OrdinaryRivalOrFallback,
  StopCondition
}
```

For `MathLensUse.OneLine`, `VisiblePayoff` says what the lens makes visible, such as a bottleneck, invariant, obstruction, incompatibility, loss boundary, or diagnostic split. `NextLensUseAction` says the now-bounded user-facing action, such as compute a local quantity, compare only inside a declared structure, run a validation slice, apply a neighboring pattern, keep the phrase as local metaphor, or remove the phrase from claim-affecting use. `ObservationOrReadoutNeeded?` names the missing observable, readout, assignment, outcome, validation slice, or scale point needed before the repaired line makes the stated action usable. `OrdinaryRivalOrFallback` says what the reader would use without this mathematical lens: ordinary prose, accepted local domain theory, direct measurement, a causal model, a queueing model instead of a quantum-like metaphor, an `A.19` space declaration instead of `C.29`, or an `F.9` bridge instead of category-like wording. If two mathematical lenses already change the next action at this cheap-output class, add one ordinary-language note about the disagreement and use `MathLensUse.MiniCard` or `MathLensUse.FullCard` before claiming a reusable rival-lens relation.

```text
MathLensUse.LensCandidateNote := {
  TargetPhenomenon,
  ProblemStructureCue,
  CandidateLensFamily,
  CandidateMathObject?,
  WhyThisLensCouldHelp,
  ExpectedVisiblePayoff,
  ObservableOrControllableCue?,
  NextLensUseAction,
  OrdinaryRivalOrFallback,
  StopCondition,
  NextMathLensUseOutput
}
```

`MathLensUse.LensCandidateNote` is a cheap first-candidate lens selection note. Its successful next outputs are `NoMathLensUseNeededNote`, `MathLensUse.OneLine`, or a named neighboring subject-pattern note.

Do not use `MathLensUse.OneLine` with an empty `CandidateMathObject`. If the candidate object has not yet been named, use `MathLensUse.LensCandidateNote` first, keep ordinary prose, or write a `NeighborGoverningPatternNote` when a non-lens claim is being made.

Cheap stop: if the mathematical phrase does not affect any claim beyond orientation, do not use the full card. If the first honest output is `NoMathLensUseNeededNote`, that is a successful `C.29` result, not an underfilled card.

#### C.29:4.4.1 - Output set and declared-use boundary

Use the single output/reliance rule in :4.4. The form states the mathematical account; a used empirical, causal, semantic-bridge, assurance or decision result additionally needs its subject-pattern basis in :4.4.6.


`LensMappingMode`, `LensUseBoundaryValue`, and declared lens use are separate fields.

| Lens-use aspect | Question it answers | Where it is recorded |
|---|---|---|
| Mapping construction | How does the mathematical object represent, abstract, embed, quotient, simulate, learn, or transfer the phenomenon? | `LensMappingMode`, `PreservedStructure`, `LostStructure`, and any `ScaleWindow?` or `CoarseGrainingRule?`. |
| Lens-use boundary value | What limited lens-use value is declared for this use? | `LensUseBoundaryValue`, validation overlay when validation use is being claimed, and neighboring evidence or assurance patterns when their claims are being made. |
| Declared lens use | What can the working reader now do, and when must the use stop or return? | `declaredLensUse`, `NextLensUseAction`, `StopCondition`, optional `blockedLensOverread?`, and named governing FPF patterns. |

`LensMappingMode` names construction, not permission. Typical local values include `representation`, `abstraction`, `quotient`, `coarse-graining`, `embedding`, `homomorphism`, `isomorphism`, `functor-like transfer`, `simulation`, and `learned or fitted representation`. A broad family name such as graph, field, category, geometry, quantum-like, variational, or Bayesian is only a prompt until the concrete construction and preserved structure and lost structure are named.

`LensUseBoundaryValue` declares only a limited lens-use boundary:

| `LensUseBoundaryValue` value | Declared use | Stop or neighboring-pattern condition |
|---|---|---|
| analogy-only prompt | orientation, hypothesis generation, recognition cue | decision, assurance, causal claim, or publication as established model |
| diagnosticOnly | finding a candidate obstruction, bottleneck, mismatch, missing state variable, or rival-lens split | prediction, decision, causal use, bridge substitution, assurance, or ontology without the neighboring-pattern result named by value |
| formal derivation inside accepted theory | local explanation or theorem-backed transfer when assumptions hold | empirical claim without observation or evidence |
| simulation | candidate model and scenario exploration | real-world causal or predictive reliance without validation |
| empirical fit | local prediction inside validation regime | out-of-regime generalization and causal use |
| accepted domain theory | local domain model use | cross-context ontology import |
| SoTA-echo candidate | structured exploration and lens-use testing | accepted FPF law, assurance, release, or foundation claim |
| mechanized proof | formal property under assumptions | real-world adequacy unless assumptions and evidence hold and any needed semantic Bridge is established |

State the declared lens use in `declaredLensUse` and its stopping or return boundary in `StopCondition`. Elegance, familiarity, source prestige, and mapping type supply no substitute for that declaration. Include `blockedLensOverread?` only when it passes F.19's plausible-reader test.

#### C.29:4.4.2 - From lens to local action

A consequence can direct a new observation, make a bounded comparison possible, expose a bottleneck or obstruction, or reject a candidate representation. State which of these happens and why. If the requested result is a plan, decision or other neighboring result, supply the mathematical consequence to that result under :4.4.6.

**Worked local bottleneck: dense-state storage.** A proposed dense pure-state representation for 50 qubits contains `2^50` complex amplitudes. At a stipulated 16 bytes per amplitude, its array alone requires `16 × 2^50 = 2^54` bytes, or `16,777,216 GiB`. A 64 GiB implementation cannot hold it. Counting the representation's elements and multiplying by storage per element identifies this bottleneck before implementation.

Recover the requested observable or property, then reconsider which structure must be represented. A restricted case, another representation or a justified approximation may change the resource demand; estimating each actual candidate's storage and work can change the choice. When a particular representation change has been chosen, [A.6.3.RT:4.1][fpf-a6-3-rt-4-1-ref] supplies the conversion and preserved/lost-content check. Until a suitable domain algorithm is supplied, the present result is rejection of the dense implementation and a specific representation question. Ordinary storage arithmetic alone needs no lens card.

#### C.29:4.4.3 - No-lens entry: choosing a first candidate lens

Use this when the next lens-use action can benefit from a mathematical lens but no adequate mathematical object has been named. The output is `MathLensUse.LensCandidateNote`, not `MathLensUse.OneLine` and not a full card. State the `ProblemStructureCue`, choose one cheap `CandidateLensFamily`, say what it could make visible, name the `ObservableOrControllableCue?` when available, state the `NextLensUseAction`, compare it with the `OrdinaryRivalOrFallback`, and stop if no action changes. If the cue is still pre-articulation and no stable `ProblemStructureCue` can be named, do not mathematize it; preserve cue plurality through `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state pattern before applying `C.29`.

Use the single discovery menu in :4.2b. Compare one candidate with the ordinary fallback; broaden the search only when this comparison leaves a material question unresolved. Asking what can be observed or varied does not by itself require a measurement or experiment record; apply its subject pattern when constructing that result.

#### C.29:4.4.4 - First honest C.29 entry cases

For E.11-style first-entry recognition, distinguish the working entry case before choosing an output:

| First honest entry case | What the working reader met | First `C.29` answer |
|---|---|---|
| Pre-articulation cue | Something feels structurally wrong, but it is not yet a claim and no stable `ProblemStructureCue` can be named. | Do not impose a mathematical lens. Use `C.2.LS`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, or the relevant language-state pattern first; apply C.29 only when the problem structure is stable enough. |
| No lens or under-lensed problem | A problem situation is stable enough for mathematical help, but no `CandidateMathObject` has been named. | Use `MathLensUse.LensCandidateNote`: `ProblemStructureCue` -> `CandidateLensFamily` -> `NextLensUseAction`. |
| Under-specified lens | A phrase such as field-like, graph-like, or quantum-like appears, but no object, mapping, preservation, or loss is stated. | Keep a `LensCandidateNote` while the object is missing. Use `OneLine` only after the object and correspondence can be supplied; otherwise keep ordinary prose. |
| Useful lens with overread | A useful conditional result is presented for a use its assumptions or correspondence do not support. | Narrow the claim and use the corresponding class in :4.4, or establish the fuller reliance through its required basis and receiving subject pattern. |
| Ordinary local math | A Markov kernel, ODE, graph data structure, or accepted domain theory appears inside its local domain use. | Stay with the local pattern and finish its result without a C.29 note or card. A separate proposed or disputed transfer retains the explanation, lost-condition examination, and validation required by that use. |
| Wrong first pattern | The reader reaches for `C.26`, `F.9`, `C.28`, `C.16`, or `A.3.3` before knowing whether mathematical-lens use is being made, or reaches for `C.29` when a neighbor already governs. | Name the first subject pattern and state what `C.29` contributes, if anything. |

#### C.29:4.4.5 - False-positive bank and entry stops

An ordinary ODE in physics, a Markov kernel in local stochastic dynamics, a graph data structure, an A.19 distance/topology/order/embedding, a category-theoretic proof internal to its domain, or a one-off teaching metaphor needs no C.29 output merely because mathematics appears. The same applies to Markov-blanket wording used only to recognize a physical interface or boundary already recovered through its subject pattern.

Enter C.29 when a separate representation or transfer issue affects the result: unexplained waiting may need a queue construction; an important comparison may need a distance with explicit losses; transferring the same graph between contexts may need both mathematical correspondence and F.9 semantics. A learned representation used for scientific explanation needs :4.5a's observation and validation conditions. A scale claim needs the applicable scale-law or preference argument in :4.4.6.

If the cue is still “something is off” and no stable structural question can be named, keep the language-state work open under :4.4.3. An inconclusive candidate, a rejected lens, an ordinary local answer and a receiving subject-pattern result are all useful stopping points.

#### C.29:4.4.6 - Subject-pattern boundary table

Use this table when the mathematical result contributes to a separately governed question. Name that question and the first receiving action; cite the existing result when it already supplies the needed basis.

`CandidateMathObject` names the mathematical object used in the representation. State its correspondence and preserved and lost structure in the accompanying account.

For a relation claim with clear participants and meaning, apply the current direct relation pattern's rule and use its result. If the rule needs an unavailable case fact, identify that fact and leave the claim unresolved pending it. Use `A.6.P` when the relation or participant meaning remains unclear; use `A.6.RCD` only after recovery when no current direct predicate can state the needed claim. Explicitly identify an obtaining relation occurrence under its direct identity rule only when a receiving claim or operation must distinguish that occurrence.

Use `A.6.0`'s FormalSubstrate profile when a separate declaration of vocabulary, laws, imports and applicability is needed. Apply `A.6.1` for mechanism import or realization of that declaration, and `E.18.1` when accepted problem-side material needs the declaration carried into later work. The same mathematical object may be designated in several epistemes or uses; select the subject pattern for the actual object and claim.

| Object or claim being made | Governing FPF pattern | C.29 contribution |
|---|---|---|
| mathematical-lens use | `C.29` | Names the C.29 discipline: candidate mathematical object, lens mapping mode, preserved structure and lost structure, invariant or distinction, `LensUseBoundaryValue`, declared lens use, any justified blocked overread, and stop or return condition. |
| durable reusable names beyond pattern-local fields | `F.18` | Cite when `MathLensUse` names become durable beyond C.29-local use. |
| broad wording and epistemic precision restoration | `F.19`, `E.10`, `C.2.P` | Use F.19 for ordinary precise-plain-language repair, E.10 for cues and unresolved wording, and C.2.P for unresolved epistemic meaning. |
| relation precision, arity, polarity, needed-claim derivation, and slot structure | The direct relation pattern; `A.6.P` for unresolved relation or participant meaning; `A.6.RCD` for a needed claim with no suitable current predicate; `A.6.5` for reusable typed participant declarations | C.29 applies only if a mathematical object represents the settled claim or derivation and changes the stated lens use. |
| object, description, and carrier distinction | `A.7` | Do not identify the phenomenon directly with the mathematical object. |
| dynamics state space and transition law; temporal aspect | `A.3.3`; `C.27.TA` for the temporal aspect | Supply the imported or contested representation and its losses to the stated dynamics/temporal question. |
| `CharacteristicSpace`, slots, topology, order, and metric-space distance overlays | `A.19` | C.29 applies only when an overlay becomes a domain-transferring or publication-bearing lens. |
| local choice among available options | `C.11` | Supply the bounded mathematical result or rival-lens note to the option comparison; use `C.11` for the `ChoiceResult` or local choice record. |
| selected method, method-family selection, `U.WorkPlan`, performed `U.Work`, work-result record, or work-relevant appearance-based reliance repair | `A.15`, `A.15.1`, `A.15.2`, `A.15.4` | Can contribute method-relevant lens use; method, plan, performed Work, and any result record stay with their direct patterns, while A.15.4 only repairs reliance on a misleading appearance. |
| evidence relation, source currentness, provenance, evidence carrier, or model card or datasheet used as evidence | `A.10` | States `LensUseBoundaryValue` only; evidence relations and provenance remain A.10 matters. |
| assurance, readiness, reliability, release confidence, safety, trust, or engineering justification | `A.15.5` for work-entry readiness; `A.10` for evidence reliance; `B.3` only for an actual named assurance claim; the direct domain pattern for other readiness, reliability, release, safety, trust, or engineering-justification claims, plus relevant G patterns when their claims are made | Treats declared lens use as possible input only; mathematical elegance does not raise assurance. |
| measurement construction, scale, unit, or comparability, or evidence-stub adequacy | `C.16` | States measurement-dependent `LensUseBoundaryValue` only; measurement construction, scale, unit, or polarity, direct comparability, and evidence-stub adequacy stay with `C.16`. |
| explanation-facing rendering or generated explanation use | `E.17.EFP` | States mathematical-lens use for the mathematical explanation used inside the rendering; explanation-use discipline stays with `E.17.EFP`. |
| bounded comparative review unit | `E.17.ID.CR` | States declared lens use for a mathematical comparison construction or rival lens when that construction affects the comparative review use. |
| same-EntityOfConcern representation-scheme transition | `A.6.3.RT` | C.29 applies only if the representation shift imports a contested or use-affecting mathematical lens. |
| coarsened rendering with narrower declared lens use and source-bearing reopen | `A.6.3.CSC` | C.29 applies only if the coarsening depends on mathematical abstraction, quotienting, or coarse-graining. |
| cross-context meaning, bridge kind, direction, CL, loss, and substitution | `F.9` | Reference the Bridge and its separate bounded-use claim; keep Bridge semantics in `F.9`. |
| causal-use question or verdict | `C.28` | Block causal overread or cite a `C.28` application or `CausalUseSupportResultRef`. |
| forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, temporal window, or rate-change used as sufficient for a use | `C.27` | Can state a prediction-relevant or distinction-relevant mathematical-lens use; temporal-claim adequacy stays with `C.27`. |
| scale-law and Bitter-Lesson preference claims | `C.18.1`, `C.19.1`, `C.31.ASAP` | Cite scale-window, scale-law, BLP, or architecture scale-preference evidence when scale behavior, general method scale preference, or architecture scale preference is being claimed. |
| quantum-like modeling | `C.26` | Treat `C.26` as C.29-compatible specialization, not as full-card inheritance for every QL-lite note. |
| selected-set result declaration, parity or benchmark result use, source harvesting and synthesis, Part-G shipping, or publication | `G.5`, `G.9`, `G.2`, `G.10`, `E.17`, and `E.24.PUB` | Use `G.5` for selected-set result declaration, `G.9` for parity or benchmark result use, `G.2` for source harvesting and synthesis, `G.10` for shipping Part-G outputs, `E.17` for a source-backed publication face and return to source, and `E.24.PUB` for an actual publication occurrence and availability. Supply the bounded mathematical result or rival-lens note with its declared use as input. |

#### C.29:4.5 - `MathLensUse.Card@Context` shape

The full card collects the account needed for a declared reliance under :4.4. `MathLensUseOutputRef` may reference any applicable C.29 output; its use does not require a FullCard. Local naming conditions are in :6.1a.

Read `MathLensUse.Card@Context` through three aspects:

| Aspect | Fields or refs | Boundary |
|---|---|---|
| Selected mathematical representation and lens mapping | `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `InvariantsExposed` | Names the selected mathematical object and the representation or correspondence used for the C.29 account. |
| Use boundary and validation | `LensUseBoundaryValue`, `ValidationUseOverlayRef?`, `LearnedLensOverlayRef?`, failure case, uncertainty or approximation note | States the lens-use boundary value for this lens use. |
| FPF use and boundaries | `declaredLensUse`, `StopCondition`, `blockedLensOverread?`, `BridgeRefSet?`, `CausalUseDisposition?`, `AssuranceUseDisposition?`, `ExportPolicyRef?` | States what the reader may do, when to stop or return, and which governing FPF patterns define or constrain neighboring claims. |

```text
MathLensUse.FullCard base fields:
MathLensUse.Card@Context := {
  TargetPhenomenon,
  entityOfConcernRef?,
  BoundedContext,
  CandidateMathObject,
  LensMappingMode,
  PreservedStructure,
  LostStructure,
  InvariantsExposed,
  LensBoundedPredictionOrDistinction?,
  LensUseBoundaryValue,
  declaredLensUse,
  StopCondition,
  blockedLensOverread?
}
```

Conditional fields apply only when the corresponding neighboring claim, claim-bearing use, or publication use is being made:

```text
MathLensUse.FullCard conditional fields := {
  DynamicsRef?,
  TransitionLawRef?,
  ObservationMapRef?,
  ScaleWindow?,
  CoarseGrainingRule?,
  SourceReturnCondition?,
  PublicationUseClassification?,
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

**Plain card gloss.** A useful mathematical lens says: what phenomenon is being seen, through which mathematical object, by what mapping, what survives, what is lost, what becomes visible, what lens-use boundary value and validation boundary make this use bounded, the now-bounded user-facing action, any justified blocked user inference, and where the lens stops.

#### C.29:4.5a - Conditional overlays

Apply overlays for the actual reliance selected in :4.4. A conditional calculation within a stipulated model still states and checks its mathematical assumptions; a claim that the model is adequate for the phenomenon additionally requires the validation account below. A learned representation needs the learned-lens information even when the exploration remains small.

```text
MathLensUse.ValidationUseOverlay@Context :=
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

Use the validation overlay for the FullCard reliance in :4.4: prediction about the phenomenon, an operational or consequential decision, adoption of a model, benchmark/assurance input, Bridge-dependent model reliance, or transfer as a reusable phenomenon model. This includes a scientific claim of model adequacy. A published explanation of a conditional derivation needs its derivation and assumptions, not an empirical-adequacy claim invented for it. `LensUseBoundaryValue` alone is insufficient for the stronger reliance. Keep the neighboring notions separate: verification is proof or formal checking under stated assumptions; validation is fit for a declared use and regime; calibration aligns model parameters or readouts with observations; explanation states why the lens makes a distinction intelligible. The C.29 output does not let any one of these four labels silently stand in for the others.

To evaluate a probabilistic prediction, choose a scoring rule appropriate to its forecast form. Use a proper rule when the score should favor reporting the assessed distribution without distortion in expectation. The Brier loss for binary events and logarithmic scores for predictive densities are examples. State which direction is better and compare forecasts against the same observations. [Gneiting and Raftery (2007)](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf) explain these scoring choices.

```text
MathLensUse.LearnedLensOverlay@Context :=
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

For `DataOrTrainingRegime`, identify the data's origin, what the collection includes and omits, how observations were collected and transformed, and the recommended uses and limitations. Use those facts to judge the proposed generalization or narrow it. [Datasheets for Datasets](https://arxiv.org/abs/1803.09010v8) supplies questions for recovering these conditions; select those relevant to the present use.

Use the following learned-lens stop variants when the declared use reaches the corresponding boundary. Include a separate guard only when it passes F.19's plausible-reader test:

| Tempting overread | Stop condition form |
|---|---|
| out-of-distribution generalization | no generalization outside the declared validation regime |
| causal mechanism | no causal mechanism claim without `C.28` and evidence relation |
| latent dimension ontology | latent coordinate or factor is not an entity kind without separate ontology and evidence |
| unobserved-variable recovery | no recovery of hidden variables beyond the declared observation map and validation slice |
| benchmark superiority | no benchmark or selector superiority outside the declared evaluation slice and relevant `G.*` record |
| assurance or release use | require the corresponding assurance, release, or reliability result under its direct subject pattern; use `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, and relevant G patterns for their claims |

```text
MathLensUse.CausalAbstractionCheck@Context :=
⟨
  LensMappingMode,
  InterventionStructureStatus ∈ {preserved, approximated, notClaimed},
  CounterfactualUseStatus ∈ {preserved, approximated, notClaimed},
  C28ApplicationRef?
⟩
```

This is not a first-class causal abstraction card. It is a lightweight check: when `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation, and `declaredLensUse` would include intervention, policy, counterfactual, or causal explanation, apply `C.28` for causal-use question and verdict.

For causal explanation through a learned representation, state which variables and interventions correspond between the models, then compare their results under those interventions. For approximate agreement, specify the similarity measure, the distribution of evaluated interventions and the way similarities are aggregated. Decoding a variable from an activation shows that the decoder can recover it; a claim that the variable affects the model's behavior needs the intervention comparison. [Geiger et al. (2025), §§2.4, 3.2 and 3.6.3](https://jmlr.org/papers/v26/23-0058.html) develop these distinctions.

#### C.29:4.5b - Repair decision table

| Failed or missing item | Required repair |
|---|---|
| no `CandidateMathObject` | If the problem still needs a mathematical lens for the next lens-use action, first name the `ProblemStructureCue` and write a `MathLensUse.LensCandidateNote` with the cheapest candidate lens family and next lens-use action; downgrade to ordinary prose or remove the mathematical claim only when no candidate lens changes action. |
| no `LensMappingMode` | Choose a lens mapping mode or downgrade to analogy-only prompt. |
| no `PreservedStructure` | Remove the claim-bearing mathematical phrase. |
| no `LostStructure` account | Describe the omitted source distinctions. If none are lost for this use, explain why the relevant distinctions and operations are preserved. C.29.1 supplies the comparison. |
| no invariant, obstruction, distinction, or payoff | Keep the phrase as didactic recognition cue or orientation-only. |
| no `LensBoundedPredictionOrDistinction` where decision, prediction, or model selection is being claimed | Block decision or assurance use; downgrade to analogy-only if no declared lens-use consequence is named. |
| evidence is analogy-only | Block decision, publication-as-established-model, assurance, release, and causal use unless evidence relation, validation regime, causal-use relation, or assurance result is supplied by its subject pattern. |
| no `LensUseBoundaryValue` | Block decision, publication, assurance, benchmark, and release use. |
| causal, intervention, policy, or counterfactual overread | Apply `C.28` or block causal use. |
| cross-context meaning, export, or substitution overread | Apply `F.9` when the export or substitution needs semantic correspondence between local senses; otherwise use the direct subject pattern. Block unsupported export or substitution. |
| scale, universality, knee, exponent, or scale-advantage claim | Apply `C.18.1` for scale-law adequacy, `C.19.1` for general method scale preference, or `C.31.ASAP` for architecture scale preference when that claim is made; otherwise keep the lens local and bounded by stop condition. |
| assurance or release use | Apply the direct release pattern, `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, or relevant G patterns for their claims; block unsupported assurance or release use. |
| `StopCondition` is generic | Name the condition for narrowing or stopping, a no-lens exit, or source-return trigger. Include a blocked overread only when it passes F.19's plausible-reader test. |

#### C.29:4.5c - Reopen a used result

C.29 output-change conditions:

| New condition | Required result |
|---|---|
| validation slice fails, degrades, or no longer matches the stated regime | Change `LensUseBoundaryValue` to the updated boundary value, update the failure case, narrow the declared lens use, or block prediction-facing use. |
| a principal rival lens changes the next lens-use action | Add `PrincipalRivalLens?` and `RivalLensRelation?`, or replace the lens for that use. |
| the intended use or reliance changes | Reapply :4.4's single rule. Keep a conditional explanation small when its conditions and use are unchanged; use FullCard plus the relevant validation/receiving result for phenomenon-model or consequential reliance. |
| source-use relation becomes outdated, contradicted, or demoted to background only | Change the `SourceUseRelation`, update the lens-use boundary value, or retire the lens from claim-bearing use. |
| bridge, causal, measurement, scale, temporal, evidence, assurance, selector, or benchmark claim is being made | Name the governing neighboring pattern and keep C.29 to the declared lens-use part. |
| abstraction, compression, coarse-graining, or latent representation drops a distinction now needed for the declared use | Add `SourceReturnCondition?`, narrow the use, or block the compressed-lens claim. |

Smallest source-return and output-change conditions:

| Condition | Required result |
|---|---|
| source material or a source family changes the lens family, validation boundary, limitation, or stated use used by this C.29 output | Update `SourceUseRelation`, `LensUseBoundaryValue`, and `OutputChangeCondition?`; narrow, replace, or retire claim-bearing use when the new source-use row no longer fits the declared use. |
| a later source supersedes or contradicts the source-use decision that bounded the lens use | Mark the source-use decision as superseded or contradicted for that use, then select a new source-use relation, lower the output class, or block claim-bearing use. |
| a neighboring subject pattern changes the declared lens-use boundary for measurement, evidence, causal use, assurance, Bridge semantics, scale law, selector, benchmark, decision, or work | Keep C.29 only for the declared lens-use part and apply the changed subject pattern to the neighboring claim before the C.29 output is reused. |
| the same lens family starts carrying validation, causal-use, evidence, assurance, selector, benchmark, release, or work claim | Add the subject-pattern application, or narrow the C.29 result to lens-bounded prediction, distinction, obstruction, diagnostic boundary, or stop condition only. |
| preserved structure or lost structure can no longer be replayed from the source-domain variables, observations, cases, mechanism, or episteme | Add `SourceReturnCondition?`, restate `PreservedStructure` and `LostStructure`, lower the output class, or block the compressed-lens claim. |


AI-assisted thin-echo result rule:

| Thin echo or query shape | Required result |
|---|---|
| `field-like`, `quantum-like`, `category-like`, `manifold`, `entropy`, `RG`, `graph`, `embedding`, or another mathematical prestige head appears alone | Do not answer from the family label. First name the use under repair or state that no C.29 use is being made. |
| claim being made is causal, measurement, bridge, evidence, temporal, work, assurance, selector, or benchmark-facing | Name the governing FPF pattern before any C.29 output. |
| C.29 still applies after the subject-pattern check | Return at least `CandidateMathObject`, `PreservedStructure`, `LostStructure`, `NextLensUseAction`, and `StopCondition`, or downgrade to `LensCandidateNote` or `NoMathLensUseNeededNote`. |

C.29 edge-case boundary results:

| Edge case | Required result |
|---|---|
| mechanized proof of a model property | State assumptions and proven property; empirical evidence or assurance use stays with `A.10`, `B.3`, or relevant G patterns. |
| simulation-calibrated lens | Scenario exploration is allowed; prediction, decision, or counterfactual reliance needs validation and the neighboring-pattern result named by value. |
| latent-space visualization | Use learned-lens overlay and stop latent ontology, causal mechanism, or unobserved-variable recovery unless separately governed by the neighboring pattern governing that claim. |
| isomorphism or equivalence claim named by value | Justify the relation named by value or downgrade `LensMappingMode`. |
| multi-lens composition | Name the principal lens and neighboring notes; avoid one giant full card that mixes queue, graph, causal, temporal, and assurance authority. |
| lens becomes accepted domain theory | Keep local domain theory with the domain pattern; durable FPF naming or kind change needs `F.18`, `C.3`, `F.8`, and `E.9`. |
| mathematical notation shift only | Use `A.6.3.RT` unless mathematical-lens use changes the declared use. |
| coarsened explanation | Use `A.6.3.CSC` for source-bearing return, narrowed use, and coarsened rendering; cite C.29 only for abstraction adequacy. |


#### C.29:4.5d - When a source changes the used result

`C.29` separates source-use relations from source-use disposition. `Adopt`, `Adapt`, `Reject`, and candidate-stress-test disposition say what FPF does with the source; `SourceUseRelation` says what work the source may perform inside a C.29 application.

Local `SourceUseRelation` slot discipline:

- source material reference or locator;
- declared C.29 output, lens-use boundary, or `LensUseBoundaryValue` affected by that source;
- source-use disposition for the substantive use: adopt, adapt, reject, candidate stress test or recognition cue;
- currentness, supersession, contradiction, narrowing, or demotion condition;
- output-change condition for the C.29 result;
- stop or return condition, and any blocked overread that passes F.19's plausible-reader test.

| `SourceUseRelation` | Declared `C.29` use | Use boundary or return |
|---|---|---|
| `recognitionCue` | Help the reader notice an invariant, obstruction, symmetry, duality, state variable, scale cue, or comparison cue. | For evidence, truth, ontology, a causal-use verdict, assurance, or release confidence, establish that separate claim and its basis through its subject pattern. |
| `candidateLensPrompt` | Suggest a first candidate lens family or mathematical object to test against the problem cue being repaired. | Test a candidate cheaply when it could change the next lens-use action; require use of that lens only after its contribution is established. |
| `adequacyControlSource` | Discipline preserved structure, lost structure, stop condition, validation regime, or neighboring-pattern application. | Satisfy C.29's field requirements and the applicable subject pattern for the resulting claim. |
| `validationBoundarySource` | Constrain the declared validation regime, evaluation slice, uncertainty, failure case, or domain of applicability. | An evidence relation, assurance claim, benchmark result, or release confidence requires its own basis and subject-pattern result. |
| `acceptedDomainTheory` | Permit local use inside a domain where the theory is already the governing local formalism. | For cross-context ontology import or broader transfer, establish the needed evidence relation and a stop condition; apply `F.9` when semantic correspondence between local senses is needed. |
| `proofUnderAssumptions` | Justify a formal property under stated assumptions. | A formal proof can support a real-world-adequacy claim only when its assumptions, observations, and evidence relation are also established, together with any needed semantic Bridge. |
| `negativeExample` | Expose failure, obstruction, non-transfer, counterexample, or stop condition. | Scope the result to the demonstrated failure and its return condition. |
| `rivalLensSource` | Name a principal rival lens or relation that changes the bounded lens-use action being made. | Keep the principal-rival choice bounded to the current lens-use action. Undertake a literature review, or establish a selector or benchmark result, only for that separately current question. |


#### C.29:4.6 - Field meanings

| Field | Meaning selected for `C.29` | Boundary guard |
|---|---|---|
| `TargetPhenomenon` | Plain entry prompt naming the phenomenon or situation to be understood. | |
| `entityOfConcernRef?` | EntityOfConcern reference named by value when the lens appears inside a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. | Required only when the lens appears in a claim-bearing episteme, `PublicationUnit`, benchmark, bridge, or assurance-bearing statement. |
| `BoundedContext` | Context in which the lens is claimed to work. | Cite `F.9` when the use needs semantic correspondence between local senses. |
| `CandidateMathObject` | Concrete mathematical object, structure, formal position, learned representation, or local formalism. | Broad family labels are prompts until narrowed. |
| `LensMappingMode` | `C.29`-local lens mapping mode. | Cross-context transfer uses `F.9` when bridge semantics are being claimed. |
| `PreservedStructure` | Structure preserved by the lens in the declared use. | No preserved structure means the mathematical phrase cannot justify the stated use. |
| `LostStructure` | Source structure the representation omits or does not preserve. | When none is lost for the stated use, name the preserved distinctions and operations and the reason preservation holds. A receiving domain may still contain additional objects; use C.29.1 to establish what can be returned. |
| `InvariantsExposed` | Invariant, obstruction, fixed point, symmetry, conservation law, diagnostic boundary, or other payoff. | If no payoff is visible, downgrade to recognition cue. |
| `ObservableOrControllableCue?` | Cheap cue naming what can be observed, read out, assigned, varied, or validated before a candidate lens can change action. Examples include arrivals, work in progress, service time, wait time, edge meaning, intervention assignment, outcome readout, observation map, validation slice, scale variable, or scale point. | When making a measurement, evidence, causal or dynamics claim, apply its corresponding pattern in :4.4.6. |
| `ObservationOrReadoutNeeded?` | Optional one-line note naming the observable, readout, assignment, outcome, validation slice, or scale point still needed before the stated bounded lens-use action is justified. | If the account of this missing item makes a measurement, evidence, causal, dynamics, or validation claim, apply the neighboring pattern that governs that claim. |
| `LensBoundedPredictionOrDistinction?` | The derived consequence used for a conditional comparison, prediction, choice or model claim. | State whether the consequence holds inside stipulated premises or is relied on for the phenomenon; apply :4.4 and :4.5a accordingly. |
| `DynamicsRef?`, `TransitionLawRef?` | References to dynamics defined by `A.3.3` when dynamics semantics are being claimed. | `C.29` does not define dynamics. |
| `ObservationMapRef?` | Probe, readout, or observation map when observation makes the declared lens use bounded enough for the stated claim. | Required when learned or measurement-dependent lens use is being made. |
| `ScaleWindow?`, `CoarseGrainingRule?` | Scale range and coarse-graining or compression rule when scale behavior, macro description or effective description, universality, coarse behavior, latent compression, or renormalized description is being claimed. | `C.18.1` and `C.19.1` govern scale-law and BLP evidence; the C.29 output states only how the lens remains adequate inside the declared window. |
| `SourceReturnCondition?` | Condition under which the reader must return from the compressed or coarse description to the source-domain variables, observations, cases, or mechanisms. | Required only when abstraction, coarse-graining, compression, latent representation, or macro-modeling drops source-domain distinctions that could matter to the stated use. |
| `PublicationUseClassification?` | Optional note for publication-facing use: `orientationOnly`, `explanationFacing`, `comparisonInput`, `decisionInputCandidate`, `benchmarkInput`, `assuranceInputCandidate`, or `reusableModelPublication`. | Apply :4.4 and :4.4.6 for the stated use. |
| `OutputChangeCondition?` | Condition under which this C.29 output must be narrowed, demoted, replaced, retired from claim-bearing use, or handed to a neighboring FPF pattern. |  |
| OrdinaryRivalOrFallback | Ordinary prose, accepted local theory, direct measurement, or simpler neighboring-pattern application the reader would use without this lens. | Required for cheap outputs; prevents prestige bias before broad rival review. |
| `PrincipalRivalLens?` | Default ordinary or most relevant rival lens. | Preferred over a broad literature survey. |
| `RivalLensSet?` | Broader comparison set when a selection or superiority question requires more than the principal rival. | Publication alone does not create a selector or benchmark question; use its receiving pattern when that result is needed. |
| `RivalLensRelation?` | Declared relation between the lens in this use and the principal rival or rival set being compared. Allowed local relation values include `ordinaryFallback`, `complementary`, `sameUseLowerCost`, `morePreservedStructureHigherCost`, `lowerErrorOnDeclaredEvaluationCriterion`, `clearerExplanationForDeclaredReader`, `bridgeNeedsF9`, `causalUseNeedsC28`, `differentScaleWindow`, `differentLossProfile`, `incomparableForCurrentUse`, `blockedByStopCondition`, and `unresolved`. Examples: a queueing lens and a causal lens can be complementary for different lens-use actions; a latent manifold and a causal graph can conflict when latent axes are read causally; an RG-like lens and a micro-dynamics lens can have different scale windows. | Any superiority claim names the evaluation criterion, reader, cost, scale window, or subject pattern that makes the comparison bounded for use. |
| `LensUseBoundaryValue` | Local finite lens-use boundary field. |  |
| `BridgeRefSet?` | Reference to `F.9` Bridge material when semantic correspondence between local senses is needed. | Bridge semantics stay with `F.9`. |
| `CausalUseDisposition?` | One of `noCausalUseClaim`, `causalUseBlocked`, `C28ApplicationRef`, or `CausalUseSupportResultRef`. | No causal-reference shortcut; no causal verdict from `C.29`. |
| `AssuranceUseDisposition?` | One of `noAssuranceUseClaim`, `assuranceUseBlocked`, `evidenceInputOnly`, `A10Ref`, or `B3ApplicationRef`. | No assurance verdict from mathematical elegance. |
| `declaredLensUse` | Declared lens use in this C.29 application. | Matches evidence and validation regime. |
| `blockedLensOverread?` | Optional tempting neighboring use that is blocked or governed by another subject pattern; include it only when it passes F.19's plausible-reader test. | Names the neighboring pattern when that neighboring claim is being made. `groundedLensOverread?` is an alias for this same optional value. |
| `StopCondition` | Condition for narrowing, stopping, returning to source material, or applying the direct pattern for a neighboring claim. | States the concrete boundary of the declared lens use. |
| `ExportPolicyRef?` | Governed reuse or export policy when publication or downstream reuse is being claimed. | Not required for local orientation or mini-card use. |

### C.29:6 - Naming, ontology, and epistemic precision-restoration account

#### C.29:6.1 - Name

Name: `C.29 — Mathematical Lens Use`.

Local namespace: `MathLensUse` = **Mathematical Lens Use**. The pattern-local card and reference namespace uses `MathLensUse`; checklist IDs use `CC-C29-*`.

The stable name is `Mathematical Lens Use` because `C.29` governs a declared use and its use boundary. A mathematical lens may summarize, re-express or extend an account. For a recorded use, `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensUseBoundaryValue`, and `StopCondition` describe the correspondence and its limits.

#### C.29:6.1a - C.29-local naming guard

`MathLensUse.*` instruments are `C.29`-local unless separately admitted.


When one `C.29` application needs a mathematical-lens name to become reusable outside that application, use `F.18` local-first naming; when it quantifies over a class of described entities, use `C.3` Kind-CAL; when it creates or reuses a durable concept or record family, use `F.8` minting or reuse and `E.9` design-rationale discipline.

#### C.29:6.3 - Ontology guard selected for FPF

> A physical, organizational, or epistemic phenomenon is not directly identified with a mathematical object; it is represented through a mathematical object by an explicitly declared mapping that preserves some structures and loses others.

### C.29:7 - Archetypal Grounding

| Archetype | Candidate lens | Preservation | Loss | Output and stop condition |
|---|---|---|---|---|
| Production line as queueing network | Queueing network | flow, service and waiting under stated premises | station failures, rework and blocking if omitted | MiniCard for the conditional comparison in :4.4; FullCard with validation when the same result is used for actual capacity or latency reliance. Withdraw the affected result when its premises fail. |
| Team backlog as queue | Queueing lens | work arrival, work in progress, service time, waiting time | obligation, motivation, priority legitimacy, skill learning | `MathLensUse.OneLine` or mini-card; admits bottleneck reasoning; moral or managerial authority, when claimed, needs its own basis. |
| Manager sees slow throughput but has no lens | Queue or flow candidate note | possible arrivals, work in progress, service bottleneck, waiting time | motivation, duty, priority legitimacy, full team ontology | Start with `MathLensUse.LensCandidateNote`; use `MathLensUse.OneLine` or mini-card only after the candidate queue or flow lens changes the next lens-use inspection. |
| Measurement comparison as declared distance or scoring choice | Metric-space distance, embedding, or scoring-function lens | comparability, distance, proximity, clustering, threshold structure | evidence relation, causal mechanism, value judgment | `MathLensUse.OneLine` or mini-card; admits comparison design and sensitivity checks, not truth or priority by itself. |
| Stabilizing system as state-space dynamics | State-space or transition lens | state variables, transition relation, attractor, control handle when the neighboring relation is named by value | unobserved motivation, obligation, causal mechanism beyond the model | `MathLensUse.OneLine` or mini-card; admits state inspection or transition inspection, not full dynamics ontology. |
| Research field as citation graph or category-like network | Graph or categorical structure | adjacency, composition, interface, failed transfer, citation or transformation patterns | semantic truth, evidence relation, social meaning | First inspect adjacency, composition, interface, or failed transfer; `MathLensUse.MiniCard` plus `F.9` when the use needs semantic correspondence between local senses; never substitute graph proximity for truth or evidence. |
| Quantum-like dashboard | Quantum-like probe and order lens | order effects, probe effects, incompatible frames when actually present | physical quantum ontology | Apply C.26's ordinary-pattern comparison and residual-obstruction test before claiming QL use. An admitted C.26 use retains the C.29-compatible stop condition `QL-NQ`; QL-lite alone does not require a FullCard. |
| RG-like scale-law claim | Coarse-graining or fixed-point lens | scale variable, coarse-graining rule, invariants across scales | micro-mechanism identity and universal applicability | `C.29` plus `C.18.1` or `C.19.1`; stops outside scale window. |
| Learned operator as scientific lens | Learned operator, latent space, surrogate solver | trained input-output structure, resolution behavior when validated | causal mechanism, out-of-domain generalization, unobserved variables | Learned-lens overlay; validation regime and stop condition required. |

Worked micro-cases by failure mode:

| Failure mode | Reader sees | C.29 repair |
|---|---|---|
| No-lens repair | "Throughput is slow, but we have no model." | Start with a queue or flow `MathLensUse.LensCandidateNote`; observe arrivals, work in progress, service time, wait time, and bottleneck candidate before using `MathLensUse.OneLine` or mini-card. |
| Under-specified-lens repair | "The market is a field." | Write `MathLensUse.OneLine` only if the candidate mathematical object, mapping, preserved structure, lost structure, payoff, and stop condition can be stated; otherwise remove the phrase or keep it as ordinary metaphor. |
| Overread repair | "The latent manifold explains reality." | Use the learned-lens overlay, name observation map and validation slice, and stop causal or ontology overread unless an exact causal or ontological predicate is defined and current facts satisfy it. |
| Wrong-neighbor repair | "The same graph appears in two contexts, so the meanings are the same." | Apply `F.9` for Bridge semantics; keep `C.29` only for mathematical-lens use. |
| Local-math non-use | Accepted Markov kernel inside local dynamics. | Stay in `A.3.3`; return `NoMathLensUseNeededNote` if useful; do not use C.29 merely because local mathematics appears. |
| Speculative SoTA stress | A proposed metric/noise coupling is carried from a learning model to a physical or biological system. | Use :13.2's candidate conditions; identify variables and assumptions and test the correspondence before using the transferred result. |

A speculative learning-dynamics model can be tried as a candidate with a concrete mathematical object and a testable correspondence. The bounded source use is in :13.2.

#### C.29:7.1 - Preserve a reservation operation

A display that retains on-hand quantity n but omits reserved quantity r merges (n,r)=(1,0) and (1,1), although only the first permits another reservation. **C.29.1:5.1** constructs the available quantity `F(n,r)=n-r`, compares reservation before and after mapping, and establishes the shared permission condition. It returns a quantity that supports the reservation question while retaining separate totals when another question needs them.

#### C.29:7.2 - A route summary changes the cost question

Routes costing 1 and 4 can have the same endpoints without having the same cost. **C.29.1:5.2** shows why the cost of a chosen route cannot be assigned to their common endpoint summary, then constructs a different answer: the minimum over admissible routes. A shared continuation preserves that minimum; a continuation available only after the more expensive prefix defeats minimizing the first stage alone. The repair retains the continuation condition or compares compatible complete routes.

#### C.29:7.3 - Make calculation rules available as data

The same executor can perform different integer calculations when their instructions are supplied as data. **C.29.2:5.1** constructs its state and instruction rules, obtains 8 and 7 from two orders applied to input 3, and gives separate arguments for the result, termination and cost. Adding jumps, interaction or larger stored integers returns to the corresponding behavior or resource question.

#### C.29:7.4 - A correct distance calculation meets a finite command range

A calculated count of 63,662 motor increments cannot be sent as a positive signed 16-bit command. **C.29.3:5.1** derives the count from a stated motion model, shows the wrapped command's contrary motion, and tests splitting the count under relative and absolute command meanings. It returns a command procedure with its supported range and motion conditions; B.5.MPC:5.1 shows the joint physical, mathematical and computational reasoning.

#### C.29:7.5 - Realize a capacity bound with a shared stock of cards

Three unique admission cards can support a three-visitor bound when their possession and transfer rules control entry. **C.29.3:5.3** follows free, reserved, inside and awaiting-return states. The free-card count gives a sufficient occupancy bound during handover; an occupancy equality additionally needs the intermediate states. A second entrance must share or partition the same stock. The worked construction shows how copying the stock defeats the bound and how controlled transfers restore it.

### C.29:8 - Bias-Annotation

| Bias risk | C.29 correction |
|---|---|
| **Mathematical prestige bias** | Require `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensUseBoundaryValue`, and `StopCondition`. |
| **Physics envy** | Physical source-domain ontology does not transfer without separate proof or evidence and subject pattern. |
| **Category-theory monoculture** | Use category-theoretic material only when composition, interfaces, views, transformations, or transport structure matters to the stated use; otherwise choose the local lens family that exposes the working cue. |
| **Speculation laundering** | Keep the metric/noise-coupling use in :13.2 conditional on its actual model assumptions and correspondence. |
| **Over-formalization** | Apply :4.4's consequence/reliance rule; reusing or publishing a conditional explanation alone does not require a full empirical-model account. |
| **Scale blindness** | Require `ScaleWindow?`; coordinate scale claims with `C.18.1` or `C.19.1`. |
| **Causal laundering** | If the lens licenses causal claims, apply `C.28`; MathLensUse cannot supply causal use by itself. |
| **Assurance laundering** | Mathematical elegance does not raise `R`; evidence and assurance use apply `A.10`, `B.3`, and relevant G patterns. |

### C.29:9 - Conformance Checklist

Use this checklist after constructing or delimiting the result in :4.1. Its conditions concern the actual correspondence, consequence and receiving use; a completed form alone does not satisfy them.

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C29-0 Use condition` | Use C.29 only when a mathematical object, formalism, family, learned representation, or simulation object is used for explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer, or when a stable problem needs a first candidate lens that could change the next lens-use action. | Keeps local analogies lightweight. |
| `CC-C29-1 Mathematical move before record` | State the question, choose a concrete object, establish its correspondence and losses, and derive or delimit the consequence before selecting the sufficient record under :4.4. | Keeps recording subordinate to the mathematical work. |
| `CC-C29-1a Computational construction` | When the mathematical result needs a computational construction, use C.29.2 to obtain the procedure, its interpretation, the argument supporting its claimed result and the relevant cost estimate. | Lets the reader construct or locate the missing computation. |
| `CC-C29-1b Realization correspondence` | When the result depends on an unsettled execution correspondence, use C.29.3 to connect preparation, system operations and readout and establish the required result relation. | Lets the reader use or repair the proposed execution. |
| `CC-C29-2 Named mathematical object` | A mathematical phrase affecting explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer names a concrete `CandidateMathObject`, not a prestige family label. | Blocks prestige vocabulary. |
| `CC-C29-2a Intervention preservation` | If `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation and causal use is being claimed, state whether intervention and counterfactual structure is preserved, approximated, or not claimed, then apply `C.28` for causal-use question and verdict. | Prevents causal abstraction laundering. |
| `CC-C29-3 Lens mapping mode` | State the `C.29`-local lens mapping mode and the concrete correspondence. If bridge semantics are claimed, apply `F.9`. | Makes the correspondence and any needed semantic Bridge explicit. |
| `CC-C29-4 Preserved structure` | State what structure the lens preserves. When the result uses a transferred operation, establish the needed preservation through C.29.1. When it uses a representative, establish that the choice leaves the required answer unchanged. | Makes the claimed preservation usable in the inference. |
| `CC-C29-5 Lost structure` | State which source distinctions or operations do not transfer. If none needed for this use are lost, explain their preservation through C.29.1 and distinguish any additional receiving objects from represented source objects. | Supports lossless embeddings as well as lossy representations. |
| `CC-C29-6 Invariants exposed` | Name invariants, obstructions, fixed points, symmetries, conservation laws, dualities, distinctions, or diagnostic boundaries. | Makes the lens usefulness visible. |
| `CC-C29-6a First-principles family recovery` | When a first-principles lens-family row from `C.29:4.2b` is used for claim-bearing lens use, recover the concrete `CandidateMathObject` for the candidate family, preserved structure, lost structure, visible payoff, lens-use boundary value, and stop condition or neighboring-pattern application for that family. | Prevents family names such as boundary, cohomology, symmetry, variational, RG, diagonal, composition, probability, information, or structural-information compression from replacing actual MathLensUse recovery. |
| `CC-C29-6b Bounded-observer structural-information lens` | When MDL, epiplexity, compression, graph information, or description-recoverability changes the next lens-use action, recover `TargetPhenomenon`, source episteme or trace, bounded observer, candidate measure or code, mapping mode, preserved and lost selected structure, visible payoff, observation or postulate boundary, source-return condition, lens-use boundary value, and stop condition. | Makes the selected structure, observer and use limit recoverable. |
| `CC-C29-6c Architecture-local lens descriptions` | When `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration`, or another architecture-local lens description is used for claim-bearing lens use, recover declared scope or scale window, candidate mathematical object, mapping mode, preserved structure, lost structure, source-return condition, next lens-use action, and stop condition; apply the neighboring patterns that define or constrain architecture, scale-preference, measurement, evidence, assurance, selected-set, and decision claims. | Makes scope, lost structure and source return explicit. |
| `CC-C29-7 Lens-bounded prediction or distinction` | State the actual consequence or obstruction, its premises and the use selected under :4.4. For phenomenon prediction or consequential reliance, supply the required applicability and validation account. | Makes the result and its reliance boundary inspectable. |
| `CC-C29-8 State, observation, and evidence separation` | If state, observation, probe, readout, or evidence is being claimed, apply `A.3.3`, `A.19`, `C.16`, or `A.10` as needed. | Prevents passive-read and dashboard mistakes. |
| `CC-C29-8a Receiving use` | When the lens result contributes to a separately governed question, identify that question and follow :4.4.6's receiving action. | Connects the lens result to its receiving use. |
| `CC-C29-9 Scale window` | If scale, universality, knees, exponents, or coarse-graining are being claimed, declare the scale range and use `C.18.1` for scale-law adequacy, `C.19.1` for general method scale preference, and `C.31.ASAP` for architecture scale preference when the respective claim is made. | Prevents universalization. |
| `CC-C29-9a Temporal use boundary` | If the claim being made is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for a use, cite `C.27` or state that temporal adequacy is not being claimed. | Prevents mathematical prediction cues from replacing temporal-claim adequacy. |
| `CC-C29-10 Rival lens discipline` | Start with the principal rival or ordinary fallback; broaden only when the actual selection or superiority question requires it. Name the comparison criterion, cost, reader, scale window or receiving pattern that makes the claim testable. | Keeps the comparison proportionate to the intended use. |
| `CC-C29-10a Validation regime` | Apply :4.4's reliance rule and :4.5a. Phenomenon-model reliance requires validation regime, evaluation slice, uncertainty/approximation, failure case, applicability and any output-change condition. A conditional derivation states its assumptions and loss without claiming empirical adequacy. | Matches validation cost to the actual reliance. |
| `CC-C29-10b Source-use relation` | If a source changes C.29 declared lens use, name its `SourceUseRelation` with source material reference, declared C.29 output or lens-use boundary, source-use disposition, source-currentness or supersession condition, and output-change condition. Include a blocked source-prestige overread only when it passes F.19's plausible-reader test. | Separates the source-use relation from source-use disposition and makes its governing slots recoverable. |
| `CC-C29-10c Source-currentness and return condition` | If source material, source-use family, source-use decision, or a neighboring subject pattern changes the declared lens-use boundary for this output, state `SourceReturnCondition?` or `OutputChangeCondition?` and narrow, demote, replace, retire, or block the claim-bearing use. | Keeps SoTA currentness and neighboring-pattern currentness tied to the declared C.29 output rather than to source prestige or process evidence. |
| `CC-C29-11 LensUseBoundaryValue` | Label `LensUseBoundaryValue` as analogy-only prompt, diagnosticOnly, formal derivation, simulation, empirical fit, accepted domain theory, SoTA-echo candidate, or mechanized proof, with a matching declared-use boundary. | Prevents evidence laundering. |
| `CC-C29-12 No ontology smuggling` | Do not import source-domain ontology without separate proof or evidence and subject pattern. | |
| `CC-C29-13 Stop condition` | State the condition for narrowing, stopping, returning to source material, or applying a neighboring pattern. | Makes closure locally visible. |
| `CC-C29-14 Bridge discipline` | Cross-context mathematical transfer cites `F.9` when semantic correspondence between local senses is needed; Bridge and C.29 fields agree without duplicate writing. | Keeps semantics bounded. |
| `CC-C29-15 Causal-use discipline` | Causal-use claims apply `C.28`; C.29 cannot carry a causal-use verdict by itself. | Blocks causal laundering. |
| `CC-C29-16 Assurance discipline` | Assurance, release, reliability, and engineering-justification claims apply their direct subject patterns: `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, the direct domain pattern for the release, reliability, or engineering-justification result, and relevant G patterns for their claims. | Prevents elegance from raising assurance directly. |
| `CC-C29-17 Meaning recovery` | If wording obscures the object, claim or participants needed for the current lens use, rewrite it so the reader can identify them and take the next lens-use action. Use `C.2.P` only when an unresolved epistemic distinction still prevents selecting or using the relevant pattern. If the meaning cannot be recovered, state the unresolved point and stop the dependent use. Keep ordinary wording when it already supplies the needed meaning. | Makes the statement and its next use recoverable. |
| `CC-C29-18 Plain and Tech balance` | A Plain sentence can remain when it aids recognition; if it makes ontology, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary commitment, that commitment is recovered through the Tech fields or neighboring pattern. | Preserves didactic usefulness without shadow semantics. |
| `CC-C29-20 Repair failed conditions` | For each failed required condition, apply :4.5b and state the resulting repair, narrowed use, return or stop. | Makes the next corrective action or stop explicit. |

### C.29:10 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | Repair |
|---|---|---|
| **Map-territory collapse** | “The organization is a quantum system.” | “A quantum-like lens models order, probe, or contextual-probability effects; no physical quantum ontology is licensed.” |
| **Prestige substitution** | “Use category theory” without naming objects, morphisms, functors, preservation, or loss. | Name the categorical structure, preserved composition or interface, and failed transfer. |
| **Family-name as object** | `field`, `graph`, `category`, `RG`, or `quantum` appears as if the family name were enough. | Name the concrete object, structure, formal position, or downgrade to Plain recognition. |
| **C.29-everywhere** | Every measurement template, score, graph, kernel, ODE, equation, or local formal object is treated as requiring `C.29`. | Require lens-transfer, publication, assurance, bridge, comparison, or reusable-explanation use. |
| **Card-before-problem** | Fields are filled before the question or mathematical operation is known. | State the question, construct the correspondence and derive or delimit its consequence before choosing a record. |
| **Local-theory over-escalation** | Accepted local dynamics or domain equations are treated as needing C.29 by default. | Keep them under the local domain pattern or `A.3.3` unless a separate lens-transfer claim, publication use, assurance input, bridge, comparison, or reusable-explanation use is being made. |
| **False exactness** | Equivalence, isomorphism, or representation is declared by value when only analogy, fit, or simulation exists. | Downgrade `LensMappingMode` or justify the declared relation named by value through the subject pattern. |
| **RG-as-vibe** | “Everything is coarse-graining” with no scale window, coarse-graining rule, or fixed point. | Declare scale variable, coarse-graining rule, invariants, and rival micro-models. |
| **Elegant-math override** | A specialized or elegant mathematical lens is selected over a more general or scale-amenable alternative because of elegance or prestige while a general method scale-preference claim or architecture scale-preference claim is being made. | Use BLP scale-audit when a general method scale-preference claim is being made; use C.31.ASAP when an architecture scale-preference claim is being made; otherwise mark the lens as local and bounded by `C.29` stop condition. |
| **Familiar math misses needed structure** | A graph, linear trend, average, two-characteristic chart, or score is used because it is familiar while the working problem needs uncertainty, topology, dynamics, causal structure, scale law, distribution geometry, or operator view. | Name the working problem cue; choose a lens family that exposes the missing structure, or keep the simple math as local orientation only and block transfer, decision, evidence, assurance, publication, bridge, comparison, or reusable-explanation use. |
| **Vanchurin over-adoption** | “FPF now says physics is learning.” | Mark as candidate lens; retain open questions and evidence limits. |
| **Invariant-free metaphor** | “Market is a field” with no invariant, transition law, observation map, or `LensUseBoundaryValue`. | Downgrade to local metaphor or build a `MathLensUse.OneLine` or mini-card. |
| **Loss-free bridge** | Mathematical structure is exported across semantic contexts as a Bridge without `F.9`, loss notes, counter-example, or declared lens use. | Use `F.9` Bridge plus MathLensUse `LostStructure` and `StopCondition`. |
| **Duplicate bridge writing** | C.29 repeats sense cells, CL, substitution scope, and Bridge-declared lens use. | Use `F.9` to establish Bridge semantics; cite Bridge from the C.29 output. |
| **LensMappingMode as BridgeKind** | A local `LensMappingMode` value is used to skip `F.9`. | Do not define a bridge-valued `LensMappingMode`; use a local transfer class only for declared lens use and apply `F.9` to cross-context meaning, Bridge-dependent substitution, CL, sense cells, or Bridge-declared lens use. |
| **Causal laundering** | Lens fit is treated as proof of intervention effect. | Apply `C.28` and evidence design, or block causal use. |
| **Assurance laundering** | Elegant formalism is treated as release confidence. | Use the direct release pattern, `A.10` for evidence reliance, and `B.3` only for an actual named assurance claim; C.29 can be evidence input only when `LensUseBoundaryValue` and validation regime are declared. |
| **LensUseBoundaryValue laundering** | `SoTA-echo candidate` sounds like authority. | Restrict to exploration or lens-use tests unless validation and neighboring evidence patterns define or constrain prediction, decision, causal use, bridge substitution, assurance, or ontology. |
| **RivalLensSet as literature review** | A broad survey is produced before a material rival question has been named. | Start with the principal rival and its action-changing difference; broaden only when the actual selection or superiority question requires it. |
| **StopCondition boilerplate** | The card says only “does not prove everything.” | State the concrete stop, no-lens exit, or source-return condition; include a blocked overread only when it passes F.19's plausible-reader test. |
| **Plain metaphor carrying law** | “What survives transfer” becomes an unstated Tech claim. | Recover the commitment through `C.2.P` fields or keep it as ordinary Plain recognition only. |
| **C.29 local-kind inflation** | `MathLensUse.Card` is treated as a universal `U.*` object or durable FPF record. | Keep it pattern-local; durable cross-pattern records require explicit minting or reuse, naming, kind, and design-rationale decision through `F.8`, `F.18`, `C.3`, and `E.9`. |

### C.29:11 - Consequences

| Benefit | Cost or handling |
|---|---|
| Authors get a small checklist before using terms such as field, quantum, category, RG, manifold, graph, or information geometry. | Some quick analogies will be downgraded to local prose; this is intended. |
| A proposed metric/noise relation can suggest a candidate learning model. | Its correspondence and application conditions still need testing before reliance. |
| Cross-domain transfer becomes auditable through preserved structure and lost structure and stop conditions. | More upfront statement effort; reduces downstream epistemic precision repair. |

### C.29:12 - Rationale

The useful representation is question-relative. The two-station recurrence distinguishes output rate from latency while omitting details of the work. An embedding can instead retain the source distinctions and introduce mathematical objects useful for an inference. C.29.1:5.4 uses a real-number construction to obtain a rational approximation, then examines a request that requires a rational solution. These uses depend on different return conditions. A reader with an adequate construction, correspondence and limitations can use them directly; C.29 helps recover whichever contribution is missing.

The cost is explicit construction and a check of material losses. A queue calculation, geometric transformation or learned model still needs its own mathematical Method. C.29's discovery cues help locate a candidate; its reliance rule determines which missing application information must be supplied for the result's use.

### C.29:13 - SoTA-Echoing

**Question and selected line.** How should a practitioner choose and bound a mathematical representation before relying on its result? Adopt problem-first domain modeling as the first-use Method: recover the question and required precision, choose an adequate construction from known structure and available data, compute its consequence, and check the application conditions. Adapt C.29 as assistance with missing correspondence, loss and transfer conditions, not a preliminary hierarchy of forms.

**Same-case comparison.** Use :4.4's queue question: does halving A's service time increase sustained output? Give both approaches the same arrivals, station times, routing and service assumptions, and a reader who can use maxima, a short recurrence and minutes-per-hour arithmetic. Give both the same bounded work allowance: a four-job prefix, the two specified service-time variations and their use limits. Neither approach receives a trained surrogate, extra observations or a larger literature review.

| Usable approach | First action and result | Effort and selection |
| --- | --- | --- |
| Direct queue Method with problem-specific assumptions and explanation | Construct departure times from arrival and server availability; compare the original and faster-A schedules. It gives the 4-job/hour rate and the five-minute latency difference, with the explicit no-blocking and constant-service conditions. | The recurrence, two variations and application limits use the stated calculation allowance. Select this direct construction; when its account is adequate, no extra C.29 output is needed. |
| Generic representation-selection account with C.29 recording | If it starts by choosing and filling a form, it still has to obtain the same recurrence before answering the question. The field hierarchy supplies no different capacity result. | Reject recording as the first move. In :4.1, start with the working question and actual construction; :4.4 permits the same short conditional account and references existing documentation. |
| Reuse of only “the line produces 4 jobs/hour” for another line or a capacity commitment | The missing step is to recover what a job, station and service interval represent, and whether constant service and no blocking still hold. In the original example, adding the omitted inspection at B changes the result to 3 jobs/hour. | Retain C.29's explicit correspondence/loss return when that information is absent. It costs a return to the source model and application conditions; if the domain account already does this, use it rather than repeat it. |

The first action-changing difference from an output-first procedure is the departure construction, not a more complete form. The retained transfer check can change a reused conclusion or leave reliance unresolved, but it is also part of competent domain modeling. C.29 supplies a reusable entry for that missing work; it is not selected over an already adequate domain Method.

**Source comparison and limits.** [Meng et al., §2.1.2](https://link.springer.com/article/10.1007/s44379-025-00016-0) compares conventional PDE solvers with physics-informed learning through confidence in equations, precision, cost and incomplete knowledge. Adapt that choice discipline, not a claim that the PDE Methods solve this queue. Known equations and a small exact computation favor the direct construction here; missing dynamics or a costly many-query problem can instead make a learned or hybrid candidate worth testing.

[Dietrich and Schilders, §§2 and 5](https://link.springer.com/article/10.1007/s00591-025-00399-4) explain problem-specific combinations of structure and data and the limits of generalization, robustness and physical consistency. This supports :4.1's application conditions, :4.2b's plural discovery and :4.5a's learned-model checks; it does not establish a universal best representation.

[Mitchell et al., §4](https://arxiv.org/html/1810.03993v2) supplies tailored reporting for trained models, their context and stakeholders. Adapt intended use, evaluation conditions and limitations for actual model reliance. Reject a universal FullCard requirement inferred from model reporting: :4.4 allows the conditional explanation to remain small and strengthens the account when reliance changes.

**Trade-off and reopening.** The selected line spends effort on the mathematical operation and only the application information needed by the receiving use. It gives up the uniform appearance of a full form for every example. Reopen the choice when an actual competing construction gives the needed result with lower effort or loss, when observations defeat a relied-on premise, or when the intended reliance changes. A measured learning-speed or error-rate advantage for C.29's complete recording hierarchy over good domain practice has not been established.

#### C.29:13.1 - Structural-sameness recognition examples

Sandberg's examples, available in the [Math section of *Links for 2026-05-12*](https://axisofordinary.substack.com/p/links-for-2026-05-12), suggest several discovery cues used in :4.2b: Stokes and boundary/exterior-derivative relations; de Rham and cohomological obstruction; a CLT fixed-point view; Lawvere-style diagonal constructions; Noether's symmetry/conservation relation; and Legendre, potential-duality and tropical-limit viewpoints. Use the example to find a candidate, then return to the chosen mathematical result and its assumptions before relying on it.

In the CLT-as-RG or fixed-point viewpoint, the Gaussian is an attractive fixed point for finite-variance distributions under the usual normalization; other stable laws are other fixed points under suitable normalization.


#### C.29:13.2 - Metric/noise coupling as a candidate lens

[Vanchurin, *Geometric Learning Dynamics*, v3, §§2–6](https://arxiv.org/html/2504.14728v3) studies learning dynamics with a trainable-space metric and noise covariance. Its `g ∝ κ^α` regimes and proposed interpolation provide a candidate for a question about how that coupling changes an update process. The stationary-entropy-production construction has its stated loss constraint; the Schrödinger-like case additionally depends on a discrete shift symmetry.

For that question, specify the trainable variables, update/loss model, covariance and metric, then test the chosen relation and time-scale assumptions. Compare with the ordinary update model under the same data and intended use. Retain only a conditional candidate until the correspondence and validation support further reliance. The paper's proposed physical and biological interpretations do not by themselves establish that correspondence for a particular system. Its §6 explicitly leaves rigorous phase-transition analysis open.

#### C.29:13.3 - Plural mathematical structures

[Rodin's plural-foundations discussion](https://arxiv.org/abs/2301.08131) supports considering several interpretable structural families rather than selecting by a foundational label. Its role here is a discovery prompt. The actual construction still has to preserve the law needed by the working question under :4.1.

When a mathematical equivalence, interpretation or homomorphism supports later formal work, name the exact objects, correspondence and preserved law. Use A.6.0 when a separate formal vocabulary/law declaration is needed, and E.18.1 when accepted problem-side material must be carried into later work. The object and receiving conditions are stated in :4.4.6.

#### C.29:13.4 - Applied category theory

Adopt the operation-preservation discipline explained by [Fong and Spivak, §3.3.2](https://arxiv.org/pdf/1803.05316): a functor maps objects and arrows while preserving identities and composition. C.29.1 makes the corresponding comparison available before a result is reused, including operation permissions, representative independence and weaker bounds. The authors' §2.5.3 also shows how composition and choice compute route costs; C.29.1:5.2 uses an authored case to expose when an omitted continuation condition defeats that reduction.

Applied category theory remains one organizer for composition, interfaces and transfer. The book's databases, electric circuits and dynamical systems provide source applications; adjoint functors, enriched categories and toposes provide further constructions to study when the question needs them. The trade-off is the work of defining the objects and operations and establishing their laws. When an ordinary domain calculation already provides the correspondence and consequence, use it directly. A failed comparison can instead identify the next required distinction or construction.

#### C.29:13.5 - Obstructions to compositionality

Adapt the obstructions and failures-of-compositionality perspective into `LostStructure` and `StopCondition`: a lens can be useful precisely because it exposes where transfer fails, not only where it succeeds. In plain language, a good lens does not only say "this transfer holds"; it also names the boundary where transfer stops.

#### C.29:13.6 - Computation and its physical realization

[Turing 1936, §6](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf) constructs a machine that interprets encoded machine descriptions. C.29.2 adopts the rules-as-data construction. Its finite interpreter obtains results from the listed instructions; Turing's broader universality result uses his machine-simulation construction.

[Horsman, Stepney, Wagner and Kendon 2014, §§VI–VIII](https://arxiv.org/abs/1309.7979) connect abstract computation with physical preparation, evolution and interpretation. C.29.3 adopts this comparison and explains its current extensions to digital, analog and stochastic realizations. Its source discussion distinguishes the resulting computational claim, the system model and performed execution.

These Methods and their worked constructions are conceptual synthesis. Algorithm design, numerical analysis, learning, coding and distributed computation supply further construction techniques, guarantees and cost analysis when the working question needs them.

### C.29:13a - References

The comparison above selects the first-use Method. The references below provide further source returns for the particular discovery cues and model conditions in :4.2b/:4.5a; they do not rank those families for a working problem.

| Source | Locator |
| --- | --- |
| `SAND-THREAD-MATH-LINKS-2026-05-12` | [Links for 2026-05-12, Math section](https://axisofordinary.substack.com/p/links-for-2026-05-12) |
| `VAN-GEOM-LEARNING-2025/2026` | [Geometric Learning Dynamics, v3, 14 March 2026](https://arxiv.org/html/2504.14728v3) |
| `RODIN-2023` | `https://arxiv.org/abs/2301.08131` |
| `FONG-SPIVAK-2018/2019` | `https://arxiv.org/abs/1803.05316`; Cambridge page: `https://www.cambridge.org/core/books/an-invitation-to-applied-category-theory/D4C5E5C2B019B2F9B8CE9A4E9E84D6BC` |
| `GDL-BRONSTEIN-2021` | `https://arxiv.org/abs/2104.13478` |
| `PEYRE-CUTURI-2019` | `https://arxiv.org/abs/1803.00567` |
| `PUCA-ETAL-2023` | `https://arxiv.org/abs/2307.14461` |
| `MODEL-CARDS-2018/2019` | `https://arxiv.org/abs/1810.03993` |
| `DATASHEETS-2018/2021` | `https://arxiv.org/abs/1803.09010`; CACM page: `https://cacm.acm.org/research/datasheets-for-datasets/` |
| `CAUSAL-CONSISTENCY-2017` | `https://arxiv.org/abs/1707.00819` |
| `CAUSAL-ABSTRACTION-2019` | `https://arxiv.org/abs/1812.03789`; AAAI page: `https://ojs.aaai.org/index.php/AAAI/article/view/4117` |
| `APPROX-CAUSAL-ABSTRACTION-2019/2020` | `https://arxiv.org/abs/1906.11583`; PMLR page: `https://proceedings.mlr.press/v115/beckers20a.html` |
| `CAUSAL-ABSTRACTION-JMLR-2025` | `https://jmlr.org/beta/papers/v26/23-0058.html` |
| `SCHOLKOPF-ETAL-2021` | `https://arxiv.org/abs/2102.11107`; DOI `10.1109/JPROC.2021.3058954` |
| `PINN-2019` | DOI `10.1016/j.jcp.2018.10.045` |
| `PIML-2021` | DOI `10.1038/s42254-021-00314-5` |
| `DEEPONET-2021` | DOI `10.1038/s42256-021-00302-5` |
| `FNO-2020/2021` | `https://arxiv.org/abs/2010.08895` |
| `SCIML-DIETRICH-SCHILDERS-2025` | DOI `10.1007/s00591-025-00399-4`; `https://link.springer.com/article/10.1007/s00591-025-00399-4` |
| `PIML-SURVEY-2025` | DOI `10.1007/s44379-025-00016-0`; `https://link.springer.com/article/10.1007/s44379-025-00016-0` |
| `NEURAL-OPERATORS-NRP-2024` | DOI `10.1038/s42254-024-00712-5`; `https://www.nature.com/articles/s42254-024-00712-5` |
| `PHYSICS-FOUNDATION-MODEL-2025` | `https://arxiv.org/abs/2509.13805` |
| `KOOPMAN-SINDY-DMD-2016` | SINDy DOI `10.1073/pnas.1517384113`; DMD DOI `10.1137/1.9781611974508` |
| `BAYES-WORKFLOW-PPL-2018/2020` | Probabilistic programming arXiv `https://arxiv.org/abs/1809.10756`; Bayesian Workflow arXiv `https://arxiv.org/abs/2011.01808` |
| `MODERN-BED-2023/2024` | `https://arxiv.org/abs/2302.14545`; DOI `10.48550/arXiv.2302.14545` |
| `MODERN-OED-2024/2026` | `https://arxiv.org/abs/2407.16212`; Cambridge Core DOI `10.1017/S0962492924000023` |
| `BO-AL-ADAPTIVE-SAMPLING-2024` | DOI `10.1007/s11831-024-10064-z`; `https://link.springer.com/article/10.1007/s11831-024-10064-z` |
| `EIG-DENSITY-APPROX-2024/2026` | `https://arxiv.org/abs/2411.08390`; DOI `10.48550/arXiv.2411.08390` |
| `ROBUST-GBOED-2025` | `https://arxiv.org/abs/2511.07671`; DOI `10.48550/arXiv.2511.07671` |
| `OBERKAMPF-ROY-2010` | Cambridge page: `https://www.cambridge.org/core/books/verification-and-validation-in-scientific-computing/contents/9399D588DE8B3D49E392CF0436D5A67D` |
| `NRC-VVUQ-2012` | DOI `10.17226/13395`; `https://nap.nationalacademies.org/catalog/13395/assessing-the-reliability-of-complex-models-mathematical-and-statistical-foundations` |
| `GNEITING-RAFTERY-2007` | DOI `10.1198/016214506000001437` |


### C.29:15 - Relations
- **Construction and argument recovery:** B.5 recovers the inputs, operations and dependencies needed to obtain or understand a result. C.29 tests which consequence can be carried through the proposed mathematical correspondence.

- **Related Methods:** C.29.1 constructs mathematical result transfer; C.29.2 constructs a computation; C.29.3 connects computation to concrete execution. Each has its own working entry. They can be composed when one result supplies another's input; a computational question can also begin with an already adequate mathematical representation.

- **Boundary balance:** C.29.BB constructs and revises an additive change account, preserving shared transfers and the information needed for the requested total.
- **Joint reasoning:** B.5.MPC connects the physical account, mathematical question, computation and realization, starting from whichever contribution is available and returning to the contribution whose conditions fail. A.3.3 supplies state and continuation semantics; A.6.1 supplies the realization relation; C.39 helps find or develop a missing operation.

- **Extractable structural information:** `C.2.8` defines the characteristic and observer conditions consumed by a structural-information estimate. C.29 supplies the particular mathematical-lens correspondence and its limits.
- **Architecture lens boundary:** `C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite C.29 lens outputs for preserved structure, lost structure, structural information, epiplexity, scale mapping, residual mapping, or source-return.
- **Structural-information adequacy boundary:** `C.33`, `C.34`, and `C.35` may cite C.29 outputs when mathematical-lens results expose captured structure, preserved structure, lost structure, or discovery adequacy.

- **Builds on:** `A.1.1`, `A.6.P`, `A.6.RCD`, `A.3.3`, `A.19`, `A.10`, `A.15`, `B.3`, `C.16.P`, `C.16`, `E.17.EFP`, `E.17.ID.CR`, `A.6.3.RT`, `A.6.3.CSC`, `F.9`.
- **Constrained by:** `E.8`, `E.10`, `F.19`, `C.2.P`, `E.19`.



- **Coordinates with:** `A.6.0`, `A.6.1`, `E.18.1`, `C.11`, `A.15.1`, `A.15.2`, `A.15.4`, `C.18.1`, `C.19.1`, `C.26`, `C.27.TA`, `C.27`, `C.28`, `C.31.ASAP`, `G.5`, `G.9`, `G.2`, `G.10`.
- **Specialization relation:** `C.26` is selected as a C.29-compatible specialization for quantum-like modeling, with affordability qualifications.
The conditional receiving questions and first contributions are collected in :4.4.6.

[fpf-a6-3-rt-4-1-ref]: A.6.3.RT-Representation-Scheme-Transition.md#a63rt41---ordinary-representation-move

### C.29:End
