## A.6.1 - U.Mechanism - Law-governed application to a SubjectKind over a RangedValueKind

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.6.1:1 - Problem frame

Use this pattern when a reusable declaration must do more than name a signature. Use it when the project needs to declare a **law-governed operation algebra**, admissibility predicates, context-local applicability, cross-context transport, and realization discipline for a `U.Mechanism`.

Use it when the working question is:

* which `SubjectKind` and `RangedValueKind` the mechanism ranges over;
* which operations are available and which SlotSpecs those operations publish;
* which laws and invariants govern the operations;
* which admissibility predicates fail closed before an operation can be used;
* which bridge, reference-plane, and reliability-penalty relation governs cross-context or cross-plane use;
* whether a realization tightens the mechanism without relaxing its laws.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Mechanism`: a specialization of `U.Signature` whose vocabulary is an `OperationAlgebra`, whose laws are a `LawSet`, and whose additional fields declare admissibility, applicability, transport, time policy, plane policy, audit surface, and monotone realization relation.

**First useful move.** Write the mechanism as an A.6.0 Signature Block, then add only the mechanism-specific fields: `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, `Transport`, `GammaTimePolicy`, `PlaneRegime`, and `Audit`. If cross-context use is current, name the Bridge and the Reliability penalty relation before any reuse claim is made.

**What goes wrong if missed.** An implementation recipe, method name, policy rule, telemetry package, or cross-context reuse habit can masquerade as mechanism law. Downstream work then cannot tell which operations are admitted, which predicates fail closed, which realization is monotone, and which losses affect Reliability rather than Formality or Guarantee.

**What this buys in practice.** Scope mechanisms, normalization mechanisms, selector mechanisms, scoring mechanisms, publication mechanisms, and comparison mechanisms can be compared, refined, extended, transported, and realized without hiding law, guard, time, plane, or Reliability assumptions.

**Not this pattern when.** If the claim is only a reusable declaration with no operation algebra and no admissibility predicates, use `A.6.0`. If the claim is a semantic way of doing, use `A.3.1`. If the claim is an episteme describing that way, use `A.3.2`. If the claim is planned or dated work, use `A.15.2` or `A.15.1`. If the claim is evidence, assurance, gate authority, publication use, or result acceptance, use the governing pattern for that claim.

### A.6.1:2 - Problem

Without a kernel mechanism pattern, scope, normalization, selection, comparison, and publication constructs proliferate with incompatible algebras, hidden guard predicates, and ungoverned reuse. Cross-context use loses its Bridge and Reliability penalty relation. Numeric comparison drifts into scale-incompatible scalarization. Realizations begin to relax laws rather than safely implement them.

FPF already has the A.6.0 Signature discipline, bridge and reference-plane patterns, characteristic-space and measurement rules, and work or evidence patterns. What is missing without `U.Mechanism` is one kernel kind for reusable law-governed operation algebras with admissibility, transport, audit, and monotone realization.

### A.6.1:3 - Forces

| Force | Tension |
| --- | --- |
| Locality and transport | Semantics are context-local, but mechanisms often need explicit cross-context or cross-plane use. Transport must be Bridge-only, and penalties belong in Reliability. |
| Expressivity and compliance | Rich operation algebras must stay within characteristic-space, measurement, comparison, and unit-compliance rules. |
| Time determinacy | Admissibility predicates often depend on time, but implicit "latest" assumptions make reuse unreplayable. |
| Slot clarity and specialization depth | Multi-level specialization needs stable SlotKinds and monotone ValueKind narrowing; positional parameters are not enough. |
| Signature hygiene | Imported signatures must remain opaque; mechanisms use `imports`, `provides`, and ClaimIds rather than redeclaring foreign laws. |
| Method and mechanism proximity | The same project phrase can point to a method, method description, mechanism, work plan, dated work, or evidence value; vocabulary alone cannot decide the kind. |

### A.6.1:4 - Solution

#### A.6.1:4.1 - Definition

`U.Mechanism` is a specialization of `U.Signature`. A mechanism publication includes the universal four-row Signature Block:

| Signature row | Mechanism realization |
| --- | --- |
| `SubjectBlock` | `SubjectKind`, `RangedValueKind`, `SliceSet`, `ExtentRule`, and optional `ResultKind` |
| `Vocabulary` | `OperationAlgebra` with SlotSpecs for operation arguments |
| `Laws` | `LawSet` of equations and invariants |
| `Applicability` | bounded context, plane, time, and compliance notes |

Mechanism-only additions are `AdmissibilityConditions`, `Transport`, `GammaTimePolicy`, `PlaneRegime`, and `Audit`. They extend the Signature without creating a fifth Signature row.

#### A.6.1:4.2 - Mechanism declaration

```text
MechanismDeclaration:
  DeclarationHeader:
  Imports:
  SubjectBlock:
    SubjectKind:
    RangedValueKind:
    SliceSet:
    ExtentRule:
    ResultKind:
  SlotIndex:
  OperationAlgebra:
  LawSet:
  AdmissibilityConditions:
  Applicability:
  Transport:
  GammaTimePolicy:
  PlaneRegime:
  Audit:
```

`DeclarationHeader` states `id`, `version`, and publication state. If the mechanism is intended to be imported or reused, it includes a `SignatureManifest`; `DeclarationHeader.id`, `DeclarationHeader.version`, publication state, imports, and public symbols must match the manifest.

`Imports` names signatures that supply non-kernel symbols used by the Signature Block or operation algebra. Imports are acyclic. Imported signatures are opaque: reference only their provided symbols and ClaimIds.

`SubjectKind` names the EntityOfConcern kind acted upon. `RangedValueKind` references an existing C.3 `U.Kind`, admitted durable U-kind, Concept-Set row, or imported signature symbol. A mechanism publication does not define a new core kind inside the mechanism definition.

`SlotIndex` is a derived index over SlotSpecs used by `OperationAlgebra` and guard-only SlotSpecs used by `AdmissibilityConditions`. It does not replace per-operator SlotSpecs and does not relax A.6.0 argument discipline.

`OperationAlgebra` names operations whose signatures use SlotKinds from the SlotIndex. Each operation publishes SlotSpec triples for argument positions; numeric indices are presentation only.

`LawSet` states equations and invariants. Admission and eligibility tests belong under `AdmissibilityConditions`, not under `LawSet`.

`AdmissibilityConditions` are deterministic, context-local guard predicates that fail closed. Unknowns become `degrade` or `abstain`; they are not coerced to zero or false.

`Applicability` binds the mechanism to a `U.BoundedContext` with plane, time, and comparison-compliance notes.

`Transport` is a declarative policy surface for cross-context or cross-plane use. It names the Bridge, channel, and `ReferencePlane` relation; when planes differ it names the plane-loss policy. It does not introduce a `U.Transfer` edge and does not restate CL, Phi, Psi, or plane-policy tables. Penalties are recorded in Reliability or effective Reliability only; Formality and Guarantee stay invariant.

`GammaTimePolicy` states point, window, or policy. There is no implicit latest.

`PlaneRegime` declares reference-plane treatment when values, operations, or comparisons cross planes.

`Audit` is a conceptual audit surface. It cites policy ids, crossing records, and edition pins by reference rather than embedding telemetry details or tool-specific execution details in the kernel pattern.

#### A.6.1:4.3 - U-kind and local declaration settlement

This pattern retains `U.Mechanism` as the durable U-kind governed by this host. The other names in the mechanism declaration are local relation, record, or description values, not additional root U-kinds admitted by this sentence.

| Name | Disposition |
| --- | --- |
| `U.Mechanism` | Durable U-kind: law-governed specialization of `U.Signature` over `SubjectKind` and `RangedValueKind`, with operation algebra, laws, admissibility, transport, audit, and monotone realization. |
| `MechanismMorphismRelation` | Mechanism-local relation constructor for refinement, extension, equivalence, quotient, product, and transport relations among mechanisms. It is governed here and by A.6.5 SlotSpec discipline; it is not a root U-kind. |
| `MechanismDeclarationTemplate` | Local record form for publishing a mechanism declaration. It is a description/publication aid, not a durable U-kind. |
| `MechanismDescription` | Description episteme for a mechanism declaration, governed by the episteme and publication patterns when description or publication claims are current. |
| `MechanismFamilyDescription` | Description form grouping one mechanism declaration with several monotone realizations; it does not admit a separate family U-kind here. |
| `MechanismInstanceDescription` | Context-local description of one mechanism declaration with windows, regimes, and BridgeIds; it is not an operational telemetry record and not a root U-kind. |

It reuses `U.Signature`, C.3 kind values, admitted durable U-kinds, `U.BoundedContext`, Bridge, ReferencePlane, characteristic-space, measurement, and reliability-channel terms without changing their governing patterns.

#### A.6.1:4.4 - Method and mechanism positions

Do not decide the method and mechanism question by vocabulary. When a source expression or project concern appears to name changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern`, use `E.10.ARCH:3.1` to recover the project concern first and then assign separately governed typed FPF values.

For this host, keep the local question thin: is the current claim a law-governed mechanism declaration or realization over a `SubjectKind` and `RangedValueKind`? If the source label also raises method, method-description, formal-substrate, work-plan, dated-work, evidence, source, gate, result, publication, or temporal claims, keep those values linked only by explicit relation positions and apply their own governing patterns.

`U.Method` governs the context-local way of doing a transformation or enactment. `U.Mechanism` governs a law-governed declaration over a `SubjectKind` and `RangedValueKind`: operation algebra, laws, admissibility predicates, applicability, transport, audit surface, and monotone realization relation.

A solver-selection scheme can be a `U.Method` in one bounded context; a selector mechanism can declare operations over candidate methods; a selected method can fill a mechanism slot; and a mechanism realization can be implemented through a method description and enacted in dated work. Those links do not make `A.3.1` sufficient for a mechanism claim or `A.6.1` sufficient for a method claim.

Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Slot-position labels do not create alternate ontology.

#### A.6.1:4.5 - Morphisms and constructors

`MechanismMorphismRelation` provides structure-preserving relations and constructors between mechanisms:

| Relation or constructor | Meaning |
| --- | --- |
| Refinement `M' <= M` | narrows SubjectBlock or SlotSpecs and strengthens LawSet or AdmissibilityConditions; it must be safe for substitution |
| Extension `M <=+ M''` | adds operations or new SlotKinds for new operations without weakening existing laws or guards |
| Equivalence `M == M'` | maps subjects and operations bijectively while preserving and reflecting LawSet up to isomorphism |
| Quotient | factors a mechanism by a congruence such as a normalization equivalence |
| Product | combines independent RangedValueKinds componentwise and forbids hidden cross-operations |
| Transport | lifts a mechanism across contexts or planes using Bridge-only policy and Reliability penalties |

For specialization chains:

* name the parent and the morphism kind;
* keep inherited SlotKinds invariant;
* allow ValueKind narrowing and guard strengthening in Refinement;
* introduce extra required inputs only through new operations or adapter mechanisms;
* keep root mechanisms general and domain-specific policies in specialized mechanisms.

#### A.6.1:4.6 - Description records

`MechanismDescription` is the ordinary description episteme for a mechanism declaration. It can show:

```text
Mechanism:
  Imports:
  SubjectBlock:
  SlotSpecs:
  OperationAlgebra:
  LawSet:
  AdmissibilityConditions:
  Transport:
  GammaTimePolicy:
  PlaneRegime:
  Audit:
```

`MechFamilyDescription` groups one MechanismDeclaration with multiple realizations. Each realization may tighten laws or guards and must not relax them.

`MechInstanceDescription` records a mechanism declaration in one context with windows, named regimes, and BridgeIds. It is a conceptual instance description, not an operational telemetry record.

#### A.6.1:4.7 - Defaults

* Local-first semantics: judgments are context-local; crossings are explicit and costed in Reliability.
* Comparison compliance: numeric comparison or aggregation uses comparison, measurement, and characteristic-space rules; partial orders return sets.
* Tri-state guard discipline: unknown guard results become `degrade` or `abstain`.
* Reliability-only penalties: Bridge, kind, scope, and plane losses affect Reliability or effective Reliability, not Formality or Guarantee.
* Opaque imports: imported signatures are referenced by provided symbols and ClaimIds.

#### A.6.1:4.8 - USM and UNM as mechanism instances

USM can be represented as a `U.Mechanism` over `ContextSliceSet` with operations such as membership, subset, intersection, span union, translate, widen, narrow, and refit. Its laws include serial intersection, span union only under a named independence assumption, and mandatory time policy.

UNM can be represented as a `U.Mechanism` for normalization classes and normalization equivalence. It uses normalize-then-compare discipline, scale-appropriate transforms, and comparison-compliance rules.

These examples are informative. They show that scope, normalization, comparison, scoring, and publication mechanisms can share one kernel mechanism shape without changing their own governing patterns.

### A.6.1:5 - Archetypal Grounding

#### A.6.1:5.1 - Selector mechanism

A team needs to select one method from candidate methods. The selection method can be `U.Method`; the selector mechanism declares operations over candidate sets, criteria, comparison results, context, and selected value. It states admissibility predicates for candidate completeness, comparison availability, and time window. The selected method remains a method value; the selector mechanism is not the selected method.

#### A.6.1:5.2 - Scope mechanism

A project uses context slices to decide where a claim applies. USM declares the slice set, operations, laws, admissibility predicates, bridge policy, and time policy. A source statement such as "scope covers target slice" is admissible only if the guard predicate can be evaluated in the bounded context.

#### A.6.1:5.3 - Normalization mechanism

A benchmark group normalizes scores before comparing systems. UNM declares admissible normalization methods, equivalence, transforms by scale type, and comparison-compliance conditions. Ordinal averaging is rejected because the mechanism cannot make scale-incompatible arithmetic admissible.

#### A.6.1:5.4 - Publication mechanism

A publication mechanism emits selector-ready packs, refresh cues, and crossing records. The mechanism declares operations and admissibility predicates; actual publication work, telemetry, evidence, and gate decisions stay with their governing patterns.

### A.6.1:6 - Bias-Annotation

Typical biases:

* **implementation-as-law bias**: code, workflow diagrams, or recipes are treated as mechanism law;
* **method-as-mechanism bias**: a way of doing is treated as an operation algebra with laws and admissibility predicates;
* **transport-by-habit bias**: cross-context reuse happens without Bridge, ReferencePlane, and Reliability penalty relation;
* **scalarization bias**: partial orders, ordinal scales, or cross-unit values are forced into one number;
* **slot-position bias**: parameter positions substitute for named SlotKinds and SlotSpecs;
* **tool-binding bias**: evaluator, vendor, CI, or telemetry details are put into kernel mechanism semantics.

### A.6.1:7 - Conformance Checklist

**CC-UM.0 (A.6.0 alignment).** A conforming `U.Mechanism` publication includes the four-row `U.Signature` Block. `OperationAlgebra` is the Vocabulary row, `LawSet` is the Laws row, and `Applicability` is the Applicability row. `SlotIndex` is a derived index, not a fifth Signature row.

**CC-UM.1 (Complete declaration).** A conforming publication includes DeclarationHeader, Imports, SubjectBlock, SlotIndex, OperationAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, GammaTimePolicy, PlaneRegime, and Audit.

**CC-UM.2 (Manifest coupling).** If imported or reused, the mechanism includes a SignatureManifest consistent with DeclarationHeader, imports, and provided symbols.

**CC-UM.3 (Monotone realization).** A realization satisfies the mechanism LawSet and imported laws. It may tighten laws or guards and must not relax them.

**CC-UM.4 (Opaque imports).** Realizations and mechanisms treat imported signatures as opaque. They reference only provided symbols and ClaimIds.

**CC-UM.5 (Bridge-only transport).** Cross-context or cross-plane use names BridgeId, channel, ReferencePlane, and plane policy when needed. Transport does not create a `U.Transfer` edge.

**CC-UM.6 (Reliability-only penalties).** Scope, kind, bridge, or plane penalties are recorded in Reliability or effective Reliability only. Formality and Guarantee stay invariant.

**CC-UM.7 (Comparison compliance).** Numeric comparison or aggregation binds to characteristic-space, measurement, scale, and comparison rules. Partial orders remain set-valued unless a declared scorer governs the reduction.

**CC-UM.8 (Tri-state guards).** Guard predicates are deterministic, context-local, and fail closed. Unknowns become `degrade` or `abstain`, not zero or false.

**CC-UM.9 (SlotIndex as view).** SlotIndex is mechanically derivable from per-operator SlotSpecs plus guard-only SlotSpecs. Didactic ValueKind projections do not replace SlotSpecs.

**CC-UM.10 (Specialization chains).** A mechanism specialization names its parent and morphism kind, preserves inherited SlotKinds, narrows ValueKinds only in Refinement, and avoids new mandatory inputs to inherited operations.

**CC-UM.11 (No in-place kind definition).** `RangedValueKind` references an existing C.3 `U.Kind`, admitted durable U-kind, Concept-Set row, or imported signature symbol. Any new durable U-kind requires a separate accepted E.24.UK, A.11, and naming decision.

**CC-UM.12 (Method-position separation).** A mechanism publication does not close a method, method-description, work-plan, dated-work, evidence, gate, publication-use, or result claim. Linked values are named by their governing patterns.

**CC-UM.13 (No tool binding).** Kernel mechanism narrative does not depend on vendor names, CI hooks, telemetry fields, or tool-specific evaluator semantics. Such details are outside the mechanism unless another governing pattern admits them.

### A.6.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| SlotIndex treated as a fifth Signature row | Keep SlotSpecs inside operator declarations; use SlotIndex only as a derived view. |
| Admission tests put in LawSet | Move operational guards to AdmissibilityConditions. |
| Implicit context crossing | Name BridgeId, channel, ReferencePlane, and Reliability penalty relation. |
| Penalties leak into Formality or Guarantee | Record losses in Reliability or effective Reliability only. |
| Scale-incompatible scalarization | Use characteristic-space, measurement, scale, and comparison rules; keep partial orders set-valued. |
| Specialization breaks SlotKind identity | Preserve inherited SlotKinds; narrow ValueKinds only where Refinement permits it. |
| Unknown coerced to zero or false | Use `degrade` or `abstain`. |
| Method label treated as mechanism law | Recover the current governed claim and relation position first; use A.6.1 only when operation algebra, laws, admissibility predicates, transport, audit, or realization relation are current. |
| Tool configuration treated as mechanism declaration | Keep tool settings in the direct tooling, publication, work, or evidence pattern; put only mechanism semantics in A.6.1. |

### A.6.1:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Mechanism families share one kernel declaration shape. | Teams must name slots, laws, guards, and transport policy explicitly. |
| Reuse becomes auditable across contexts and planes. | Bridge and Reliability penalty relations cannot be skipped for convenience. |
| Realizations can vary without relaxing laws. | Implementations must be checked against signature and imported-law opacity. |
| Method, mechanism, work, evidence, and gate claims stay separated. | Source labels often need `E.10.ARCH` recovery before typed assignment. |
| Comparison and normalization mechanisms stop hiding scale-incompatible arithmetic. | Some familiar single-score practices become inadmissible until a scorer is declared. |

#### A.6.1:9.1 - Quick use cards

* **Mechanism = operation algebra plus laws.** Add guards, transport, time, plane, audit, and realization discipline.
* **Method is not mechanism.** A method can use or fill a mechanism slot; it does not become the mechanism by name.
* **Guards fail closed.** Unknown guard results become `degrade` or `abstain`.
* **Transport is Bridge-only.** Crossings need Bridge, ReferencePlane, and Reliability penalty relation.
* **SlotKinds travel.** Positional parameters do not replace SlotSpecs.
* **Realizations tighten.** A realization may specialize but not relax mechanism laws.

### A.6.1:10 - Rationale

Mechanisms need a kernel shape because many FPF practices declare reusable operation families: scope operations, normalization operations, selector operations, comparison operations, publication operations, and scoring operations. Without one shape, each practice invents local vocabulary for operations, laws, guards, reuse, and realization.

Binding mechanisms to A.6.0 Signature discipline keeps declaration and realization separate. The Signature carries boundary semantics; realization varies under monotonicity. Bridge-only transport and Reliability-only penalties keep cross-context losses visible without mutating Formality or Guarantee.

### A.6.1:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current scoped-effects and handlers work | Bosman, van den Berg, Tang, and Schrijvers, "A Calculus for Scoped Effects & Handlers", LMCS 20(4), 2024, arXiv:2304.09697; Matache, Lindley, Moss, Staton, Wu, and Yang, "Scoped Effects as Parameterized Algebraic Theories", ESOP 2024 extended version, arXiv:2402.03103. | Adopt and adapt: operations, equations, scopes, resources, handlers, and type information are separated rather than hidden in one implementation object. | `OperationAlgebra`, `LawSet`, `AdmissibilityConditions`, and context-local applicability are explicit surfaces. |
| Typed semantic translation and categorical data migration | Spivak and Schultz, *Seven Sketches in Compositionality* and CQL practice lines. | Adapt: typed translation and quotient ideas are useful, but cross-context use in FPF must be Bridge-only with Reliability penalties. | Mechanism morphism, quotient, product, and transport relations are explicit and bounded without admitting an extra root U-kind. |
| Policy-as-code and safety standards practice | Open Policy Agent and Rego practice; UL 4600:2020; ISO 21448 road-vehicle safety practice. | Adapt: guard predicates and safety conditions are reviewable only when context, window, and fail-closed behavior are explicit. | `AdmissibilityConditions` and `GammaTimePolicy` are separate from `LawSet`; evaluator tooling stays outside kernel semantics. |
| Session, typestate, and protocol-safety practice | Contemporary session-type and typestate practice after 2015. | Adapt: operation-sequence constraints matter, but they must be expressed as guards or laws rather than hidden automata in prose. | SlotSpecs, SlotKinds, and specialization-chain rules prevent positional or hidden-state drift. |
| Calibrated uncertainty and conformal prediction | Angelopoulos and Bates, "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification", arXiv:2107.07511; contemporary conformal-prediction and calibrated-uncertainty practice. | Adopt and adapt: uncertainty sets and calibration show why admissible comparison must preserve scale and uncertainty conditions. | Comparison mechanisms bind to measurement, scale, and scorer rules; partial orders stay set-valued unless the scorer is declared. |

Refresh this pattern when current work on effect systems, typed semantic translation, policy-as-code, safety standards, protocol types, calibrated uncertainty, characteristic-space comparison, or FPF's own signature, method, work, evidence, gate, and transport patterns changes the governing distinction.

### A.6.1:12 - Relations

* **Builds on:** `A.6.0 U.Signature`; `A.1.1 U.BoundedContext`; SlotSpec and argument-discipline patterns; Bridge and ReferencePlane patterns.
* **Coordinates with:** `A.3.1 U.Method`; `A.3.2 U.MethodDescription`; `A.15.2 U.WorkPlan`; `A.15.1 U.Work`; `A.19`; `C.16`; `C.29`; `A.10`; `B.3`; `A.20`; `A.21`; `E.18`; `E.20`.
* **Separates from:** direct method choice, implementation recipe, telemetry publication, evidence record, gate decision, result certification, and realization work.
* **Uses for precision restoration:** `E.10`, `E.10.ARCH`, and `F.18`; use `E.10.ARCH:3.1` when source labels such as `algorithm`, `program`, `workflow`, `process`, `procedure`, `recipe`, `solver`, or `control strategy` hide the current relation position.

#### A.6.1:12.1 - P2W mechanism-use relation

When `E.18.1` reaches a mechanism cue, A.6.1 carries the mechanism meaning: operation algebra, LawSet, AdmissibilityConditions, realization relation when declared, transport, and mechanism descriptions. P2W may name the cue and governing pattern, but it does not define these mechanism relations locally.

If the issue under repair is new mechanism introduction, mechanism stabilization, or method-related mechanism use, use `E.20` when mechanism-governing-definition assignment is current. A P2W citation of a mechanism does not select a method, execute work, pass a gate, prove evidence, or certify a result.

#### A.6.1:12.2 - Lowering, repair, and refresh conditions

A `U.Mechanism` remains usable while its MechanismDeclaration, imported signatures, SlotSpecs, LawSet, AdmissibilityConditions, Applicability, Transport, GammaTimePolicy, PlaneRegime, and Audit relations remain recoverable and monotone with respect to A.6.0.

Repair the mechanism, or define a new mechanism when monotone repair is impossible, if any of these conditions holds:

* an inherited SlotKind is renamed, widened, or given a new required argument;
* a realization relaxes a law, bypasses an admissibility predicate, or depends on hidden structure inside an imported signature;
* a cross-context or cross-plane reuse claim lacks BridgeId, ReferencePlane, loss policy, or Reliability penalty relation;
* a numeric comparison or aggregation is no longer compliant with the governing characteristic-space, measurement, scale, or comparison patterns;
* a GammaTimePolicy, applicability window, or implicit latest assumption changes an admissibility result;
* a current SoTA change in effect systems, protocol types, typed semantic translation, policy-as-code, calibrated uncertainty, or context normalization changes the operation algebra, guard discipline, morphism relation, or transport boundary.

Do not repair the mechanism merely because one work occurrence, telemetry publication, evidence record, gate decision, method choice, or realization version changed. Repair the object governed by that neighboring relation unless the change alters the MechanismDeclaration, its imported signature relation, or the monotone relation between a realization and the MechanismDeclaration.

### A.6.1:End

