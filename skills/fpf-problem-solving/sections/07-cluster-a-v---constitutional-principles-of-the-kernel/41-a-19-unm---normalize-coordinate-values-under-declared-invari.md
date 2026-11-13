## A.19.UNM - Normalize Coordinate Values under Declared Invariants

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (unless marked informative)
> **Boundary:** A.19.CN defines the CN-Spec fields that select normalization and comparability. This pattern defines the normalization operation and how it uses those fields.

**Use this when** a coordinate value must be re-expressed for a declared comparison or characterization use. First recover the input, selected transformation and the distinctions the receiver needs. If direct comparison already has an adequate common basis, use it without introducing normalization.

**For a claimed normalization, recover:**
1) Which **`UNM_id`** (if applicable) and which **`NormalizationMethodInstanceId`** (and its validity window) was used?
2) Which **`NormalizationInvariant[*]`** were declared (i.e., *what is preserved*)?
3) Which **bearer, reference or comparison basis, evidence and intended use** qualify the value, including any scope or data window? Does the receiving use rely on an obtaining F.9 Bridge, kind relation or plane relation?

**Mental model.** UNM applies a declared directed transformation from an input coordinate value (`CV`) to an output (`NCV`). State its domain, target and preserved or lost distinctions. An inverse, an equality-of-output class or an operation on those classes is a narrower result requiring its own conditions.

### A.19.UNM:0 - At a glance — informative

**Intent.** Declare how coordinate values in a `DeclaredCharacteristicSpace` are normalized for a chosen comparison or characterization, including the transformation, admissibility conditions and preserved or lost distinctions.

**Where it sits.**
- **CN-Spec:** `normalization` and `comparability.mode` select the normalization and whether comparison is `coordinatewise` or `normalization-based`.
- **CHR suite role:** stage `normalize` (first-stage, when enabled by the suite protocol / comparability routing).

**Key outputs.**
- `NCV` (NormalizedCharacteristicValue) values for coordinates.
- When requested for a function `n:D→N`, the equality-of-output relation `x ≡_UNM y` iff `n(x)=n(y)` on its domain D. Its classes form a set quotient; preserving further operations or answers needs the additional tests below.
- An inverse only on the stated image of an invertible transformation; an operational quotient only for compatible operations and recoverable queries; a `NormalizationFixSpec` only when a representative of an established class is needed.

**Declaration and configured-method identifiers.**
- `UNM_id?` identifies the selected UNM declaration episteme and its edition under A.6.1; it is distinct from the configured method and from an operation application.
- `NormalizationMethodInstanceId` selects the **normalization method instance** applied to coordinate(s), with its validity window and evidence pins.

**Minimum declaration set.**
- In `CN_Spec.comparability`: set `mode`, and (when UNM participates in acceptance/comparison) set `minimal_evidence`.
- In `CN_Spec.normalization`: declare `UNM_id?`, `methods`, `instances`, `method_descriptions`, `invariants`, and (if representatives are required) `fix`.
- For the normalization or eligibility evaluation, recover the available inputs, selected method and specification editions, preservation conditions and result or reason for abstaining under Audit below. Retain a separate record when the receiving use requires one.

**Non-goals.**
- Not indicator selection (that is **UINDM**).
- Not scoring, aggregation, comparison, selection (USCM / ULSAM / CPM / SelectorMechanism).


### A.19.UNM:1 - Problem frame

To compare coordinate values, engineers need to establish:
- **What it means** to compare values across charts, slices, bearers, or reference bases, and
- **Which transformations preserve the required distinctions**, with their conditions and losses.

Teams routinely face a mismatch between:
- values that look comparable (“they’re numbers”), and
- values whose comparison basis differs, such as units, observation populations or validity windows. A supported normalization may make the needed values comparable; some differences instead require new measurements or evaluation grounds, a different comparison, or an unresolved result.

CHR distinguishes normalization, indicatorization, scoring, aggregation, comparison and selection. The chosen protocol determines which stages are needed; UNM supplies normalization when that comparison or characterization requires it.

### A.19.UNM:2 - Problem

Hidden or inadequately specified normalization causes four recurring difficulties:

1) **Normalization drifts into hidden places.** It gets embedded inside scoring, comparison, or selection, making admissibility and governance non-local.

2) **Comparability becomes rhetorical.** People say “we normalize” but cannot answer:
   *Which method and invariants? Which bearer, comparison basis and scope or window? Which evidence? Does the receiving comparison rely on an obtaining Bridge, kind relation or plane relation?*

3) **Basis and relation changes become invisible.** Teams reuse normalizations for another bearer, comparison basis, source-local meaning, or reference plane without naming what changed or the relation on which the new use depends.

4) **Engineers cannot reconstruct the operation.** Scattered definitions can hide its inputs, result, preservation conditions or limits, preventing a justified reuse.

### A.19.UNM:3 - Forces

| Force | Tension |
|---|---|
| **Evolvability vs Usability** | A stable operation contract supports evolving method families; readers still need to find the selected method and its conditions. |
| **Semantic precision vs Cognitive load** | Formal invariants/quotients ↔ a mechanism description that engineers can act on. |
| **Shared definitions vs Connected use** | UNM uses CN-Spec, CG-Spec and any required relation claims; each retains its own governing definition. |
| **Trustworthiness vs Overreach** | Evidence must support the normalization used; measurement meaning and calibration retain their own grounds. |
| **Locality vs Reuse** | A normalized value retains its declared bearer, basis, scope/window and use; a later use may require another relation or normalization. |
| **Fail-closed safety vs Convenience** | Unknown/insufficient evidence must not coerce ↔ teams want “a number anyway”. |

### A.19.UNM:4 - Solution

UNM declares directed normalization operations. For an admitted input in the selected transformation's domain, return its NCV and the preserved/lost distinctions needed by the receiving use. An undefined input has no normalization result. Use the additional branches below only when the receiver needs an inverse, classes, a class-level operation or a representative.

Select the configured method and apply the declaration below:
- **Routing** lives in `CN_Spec.normalization` and `CN_Spec.comparability.mode`.
- **Evidence/calibration legitimacy** lives in `C.16 (MM‑CHR)`.
- **Method definitions** come from the selected normalization methods and their descriptions. G.2 can supply method families; extensions identify the methods and references used.

#### A.19.UNM:4.0 - Vocabulary (normative)

**NormalizationMethodId.** A stable token naming a normalization method *kind*, used in `CN_Spec.normalization.methods`.

**NormalizationMethod.** The method *kind* (class) that defines:
1) its input/output domains, the directed transformation and the **invariants** it preserves (`NormalizationInvariant[*]`), with any distinctions it loses,
2) its **closure rules** (composition, and inverses where defined), and
3) its **validity rules** (admitted bearer, reference or comparison basis, intended use, and any scope or qualification window that constrains them).

**NormalizationMethodDescription.** An editioned epistemic description of a normalization method (bounds, validity region/window, scope constraints, and evidence links governed by `C.16`). For an A.3.2 `U.MethodDescription` claim, its EntityOfConcern must be an independently admitted A.3.1 Method and its content must make a substantive claim about that Method as a way of doing.

**NormalizationMethodDescriptionRef.** A ref to an editioned `NormalizationMethodDescription`, used in `CN_Spec.normalization.method_descriptions`.

**NormalizationMethodInstanceId.** A stable token naming a normalization method configured for coordinates in a base `DeclaredCharacteristicSpace`, with a named validity window and (when required) evidence pins. One such configuration can be used by several `apply` occurrences; this identifier does not identify a calculation invocation. Used in `CN_Spec.normalization.instances`.

**NormalizationMethodInstance.** That configured method, referenced by `NormalizationMethodInstanceId`. Its coordinate qualification and validity window are separate from the extent of a calculation that uses it.

**CV (CoordinateValue).** A raw coordinate value for a **named measurable slot** in a chart: conceptually `⟨slot_id, raw_value⟩` (plus any chart/slice scoping needed by the chart). UNM re‑parameterizes `CV → NCV` under declared invariants and validity constraints.

**NCV (NormalizedCharacteristicValue).** A normalized **value** for a coordinate (UNM does **not** “normalize characteristics”; it normalizes coordinate values under declared invariants).

**Directed transformation.** The selected method states its input domain D, target N and transformation rule. For a partial normalizer, D is the subset where a result is defined. An edge from x to its output does not supply a reverse edge. A relation-valued or uncertain output needs its declared result semantics; the function theorem below cannot be applied without a function and equality on its output values.

**`≡_UNM` (equality of normalization outputs).** For one fixed function `n:D→N`, define `x ≡_UNM y` iff `n(x)=n(y)`. Equality in N gives reflexivity, symmetry and transitivity on D. Thus the fibers form the set quotient `D/≡_UNM`. Inputs outside D have neither an n-value nor membership in this partition. This relation is distinct from the directed transformation graph.

**Operational quotient.** To inherit a total operation on classes, equivalent argument tuples must produce equivalent outputs. For a partial operation, its availability must also agree across equivalent tuples. Use the relevant equivalence on each input and output sort. A receiving query q is recoverable only when `x ≡_UNM y` implies `q(x)=q(y)`. Only after these tests may the equivalence be called a congruence for the named operations. A set quotient alone supplies no such result.

**Reversible chart change.** A declared inverse recovers the input on the transformation's stated image. A strictly monotone encoding on a totally ordered domain is injective and invertible on that image, even if the declared target contains other values. A merely monotone LUT may merge inputs. Repeated normalization or idempotence requires its own composable domain and law; it does not follow from the fibers.

**NormalizationInvariant.** A named invariant (e.g., unit alignment, polarity, reference plane) declared in `CN_Spec.normalization.invariants` and/or the selected `NormalizationMethodDescription`. Preserving the declared `NormalizationInvariant[*]` is the core admissibility claim for a normalization method instance.

**NormalizationFixSpec.** A declared policy selecting a representative of an already established `≡_UNM` class when the receiving use needs one. It does not recover which member was the input or restore a lost query answer. Bound via `CN_Spec.normalization.fix`; omit it when no class representative is needed.

**UNM_id.** An optional identifier in `CN_Spec.normalization.UNM_id?` selecting the UNM declaration episteme used by this CN-frame. Resolve its edition; it is distinct from `NormalizationMethodInstanceId` (configured normalization method).

**ValidityWindow.** A named validity window attached to a `NormalizationMethodInstanceId`, bounding where/when the instance is admissible (no implicit “latest”).

**Relation and reuse boundary.** A normalized value remains tied to the selected normalization-method instance and edition, characteristic space, its separately referenced description episteme, CN-Spec edition, bearer, reference or comparison basis, evidence and intended use. Retain any scope, slices or data window that qualify that use, as well as the configured method's declared validity window. Reuse does not establish a transfer relation. Cite an obtaining F.9 Bridge or plane relation when needed, and assess the receiving use separately.

**Lexical discipline.** Name a UNM operation as normalization, re-parameterization or a coordinate mapping under its declared invariants. Use a specialized FPF `Map` designation only when its defining conditions apply; an ordinary mathematical mapping does not thereby assert that specialized kind or an F.9 Bridge.
Legacy κ‑notation for normalization is retired; do not re‑introduce it.

#### A.19.UNM:4.1 - UNM operation declaration (normative)

`UNM.IntensionRef` is the citation name for the A.6.1 declaration episteme presented here. It does not identify a generic family in place of that declaration. The CHR baseline selects its edition before use; the `normalize` stage resolves to the declaration-local `apply` operation below. Its four named input meanings, NCV result and eligibility guard come from that selected declaration.

A different realizer of the same declaration changes no suite member. A corrected layout or citation can preserve its C.2.1 identity. A changed argument, law or guard changes the declaration contract and must be selected in the suite and protocol. For example, replacing `pass|degrade` admission with `pass` only would change whether `apply` may produce an NCV for degraded evidence; that hypothetical revision cannot enter through the unqualified name UNM. Whether two declarations concern the same operation family is a separate claim requiring that subject's kind and identity rule; the UNM label supplies neither.

**Scope note.** A.6.1 governs this operation declaration. The selected use baseline supplies the project editions and policy references; A.15.2 governs a P2W baseline, and A.15.3 typed filling applies only to independently declared positions. UNM returns the declared operation results and tri-state `GuardDecision`; gate decisions remain with their governing pattern. Audit below states the information needed to recover an application.

**IntensionHeader**
- `IntensionId`: `UNM`
- `IntensionRef`: `UNM.IntensionRef`
- `Name`: Unified Normalization Mechanism
- `Status`: Stable
- `Version`: `v1.0`
- `SuiteRole`: CHR.normalize (when enabled by CN/CHR routing)

**Imports (cite, don’t duplicate)**
- `A.6.1` (shape: `U.Mechanism`, specialization discipline)
- `A.19.CHR:4.2` (CHR suite boundary / membership)
- `A.19.CHR:4.2.1` (CHR SlotKind Lexicon)
- `A.19.CHR:4.5` (suite protocols: ordering/optionality; suite closure)
- `A.19.CN` (CN-frame routing: `normalization`, `comparability.mode`)
- `G.0` (CG-frame admissibility gates where required downstream)
- `C.16` (evidence carriers; calibration/validity for normalization legitimacy)
- `A.17/A.18` (measurement meaning & scale lawfulness; not redefined here)

**SubjectBlock**
- `SubjectKind`: declared normalization methods, with their domains, output kinds and preserved/lost distinctions; functional methods may additionally supply `≡_UNM` over their admitted inputs
- `RangedValueKind`: coordinate values (`CV`) for named measurable slots in the resolved `DeclaredCharacteristicSpace`, with `characteristicSpaceDescriptionRef` and the CN-Spec edition pinned; UNM normalizes **values**, not characteristics
- `BearerAndUseBoundary`: the bearer, reference or comparison basis, evidence and intended use, with any scope, slices or data window that qualify those values
- Input qualification: coordinate values admitted by the selected CN-Spec for this bearer and use, within the configured method's declared validity window. This is not an operation-application extent or an A.6.1 slice-membership `ExtentRule`.
- `ResultKinds`:
  - `NormalizedCharacteristicValue (NCV)`
  - optional function-kernel equivalence (`≡_UNM`) and its set of classes; a congruence claim only for separately checked operations
  - optional quotient objects and/or `Normalization-fixed` representatives (via `NormalizationFixSpec`)

**Space range and resolution.** Use the `DeclaredCharacteristicSpace` criterion and paired reference resolution in A.19:5.1.1.1. `CharacteristicSpaceRef` selects the space; `CN_Spec.characteristicSpaceDescriptionRef: U.EpistemeRef` pins the description supplying its basis. Both must resolve and agree on that space before normalization; otherwise the dependent use remains unresolved and eligibility abstains. Membership establishes the input's space structure; the selected operation must still resolve its positions, Scales and use conditions.

A changed basis requires a new space reference and position resolution, even if its label or document path is unchanged. Preserve the preceding space, description and results; reuse requires the correspondence and operation conditions of the receiving use.

**Operation-local argument and result declarations**

The names below are declaration-local designators. `ByValue` carries the stated value; each named Ref resolves to one value under this declaration's effective reference scheme. An episteme reference selects its edition; the space reference and its separate description-episteme reference follow the rule above. Cardinality is per application. The first four arguments are shared declarations instantiated separately for `apply` and `UNM_Eligibility`.

| Operation and direction | Local designator | Meaning and ValueKind | Designation; cardinality |
| --- | --- | --- | --- |
| apply / UNM_Eligibility argument | NormalizationMethodInstanceSlot | Configured normalization method selected for the value; NormalizationMethodInstanceId | ByValue; 1 for apply, 0..1 for eligibility |
| apply / UNM_Eligibility argument | CoordinateValueSlot | Coordinate value to transform or assess; CV in the named chart | ByValue; 1 for apply, 0..1 for eligibility |
| apply / UNM_Eligibility / compose argument | CharacteristicSpaceSlot | Space that supplies the coordinate meanings and Scales; DeclaredCharacteristicSpace | CharacteristicSpaceRef; 1, or 0..1 for eligibility |
| apply / UNM_Eligibility / compose argument | CNSpecSlot | CN-Spec used for the bearer, basis, evidence requirements and intended comparison, including any scope, slices or qualification window | CNSpecRef; 1, or 0..1 for eligibility |
| apply result | NCVSlot | Transformed value returned under the selected method's domain and preservation/loss basis; NCV | ByValue; 1 on successful return, 0 without a defined/admitted result |
| UNM_Eligibility result | GuardDecision | Eligibility judgment under the predicates below; pass, degrade or abstain | ByValue; 1 on completed evaluation |
| compose argument | NormalizationMethodInstancePairSlot | Ordered pair of configured methods, first inner and second outer; NormalizationMethodInstanceId[2] | ByValue; 1 pair |
| compose result | NormalizationMethodInstanceSlot | Configured composed method, with its declared validity window and evidence basis; NormalizationMethodInstanceId | ByValue; 1 on successful construction |
| quotient argument | domain | Admitted domain D of the selected normalization function, with coordinate meanings recoverable; set of CV values | ByValue or one chart-domain reference; 1 |
| quotient argument | NormalizationMethodInstanceSlot | Configured functional method used to form equality-of-output classes; NormalizationMethodInstanceId | ByValue; 1 |
| quotient result | UNMEquivalenceSlot | Relation on D defined by equality of that function's outputs | ByValue; 1 on successful construction |
| quotient result | classes | Set D/≡_UNM of all classes of that relation | ByValue; 1 on successful construction |

For each argument row, its **bindingPredicate** obtains exactly when that application uses the resolved value for the row's stated purpose: as the transformation operand, selected method, governing space/CN-Spec, ordered composition pair or quotient domain. A supplied but unused value is not bound.

`UNM_Eligibility` may assess an incomplete proposal; an absent argument has no binding and the corresponding missing-input condition gives `abstain`. This does not relax `apply`'s inputs.

For each result row, its **bindingPredicate** obtains exactly when that application returns the resolved value as the row's declared result, subject to the result laws below. A returned NCV binds the transformation value; `compose` binds the identifier of the method it constructed; `quotient` binds the relation and class set it constructed; the guard binds the judgment it evaluated.

Each binding has the A.6.1 identity and maximal continuous extent within its application; a result binds at return, not before. Equal values returned by different applications have distinct bindings because their applications differ.

**SlotIndex (derived projection).** Project the designators, ValueKinds, designation rules and cardinalities from these operation-local declarations; the index adds no meanings. The historical `Slot` suffix permits CHR lookup. A.6.5 relation SlotSpecs are not the source of these operation meanings. Method descriptions, invariants and any `NormalizationFixSpec` are resolved from the selected configured method and CN-Spec. They qualify the method or a separately chosen representative use; they are not additional arguments of every operation.

**Relation note (not a SlotKind).** A Bridge, kind relation, or plane relation is cited only when the use relies on that obtaining relation. Its declaration and receiving use remain separate from the UNM SlotIndex.

**OperationAlgebra**
1) `apply`
   - Preconditions: `UNM_Eligibility(…) ∈ {pass, degrade}` (fail‑closed; `abstain` ⇒ no NCV output).
   - Inputs: `NormalizationMethodInstanceSlot`, `CoordinateValueSlot`, `CharacteristicSpaceSlot`, `CNSpecSlot`; the selected CN-Spec supplies the bearer, basis, evidence requirements, intended comparison and scope or data window.
   - Outputs: `NCVSlot` for an input in the selected transformation's domain, with the declared preservation/loss basis. Undefined inputs produce no NCV; an eligibility result cannot create a transformation value. The optional class/operation results follow their separate conditions below.

2) `compose`
   - Purpose: build a composed method when the inner outputs lie in the outer operation's domain and the claimed preservation laws compose. Losses and receiving-use restrictions remain explicit.
   - Inputs: `NormalizationMethodInstancePairSlot` (roles = {inner, outer}), `CharacteristicSpaceSlot`, `CNSpecSlot`; both instances must be admitted for the same declared bearer, basis, intended use and any scope/window.
   - Output: `NormalizationMethodInstanceSlot` (new composed `NormalizationMethodInstanceId`), with a validity window and evidence pins.

3) `quotient(≡_UNM)` (optional)
   - Preconditions: one fixed functional normalization on its domain, with an explicit output equality. Recover that domain and the method/use basis.
   - Inputs: `domain`, resolved from the characteristic-space declaration or a declared chart domain, and `NormalizationMethodInstanceSlot`.
   - Outputs: `UNMEquivalenceSlot` and its `classes` set. Inherited operations additionally require equivalent-output and representative-independent-availability proofs; a class query additionally requires constancy on each class.
   - Use the declared `NormalizationFixSpec` only when a representative is needed. It selects a member of a class rather than proving that member was the original input.

**Applications of these operations**

The **ApplicationPredicate** differs by operation:

- `apply`: a calculation applies the selected configured method to the bound CV under the bound space and CN-Spec. Its defined, admitted return is the NCV required above. An `abstain` decision prevents this application from starting; passing eligibility alone does not start it.
- `compose`: a construction resolves the bound inner/outer methods, checks the domain and preservation conditions and constructs their composite for the bound space and CN-Spec. A failed condition yields no composed-method result.
- `quotient`: a mathematical construction uses the bound functional method and domain to determine equality of outputs and form its classes. A symbolic construction is sufficient; enumeration of an infinite domain is not required. Stronger inherited-operation and query claims retain their separate proofs.
- `UNM_Eligibility`: an evaluation assesses the bound proposal under the eligibility predicates below and returns the corresponding GuardDecision. Its result is separate from any subsequent normalization.

For each operation, the **ApplicationIdentityRule** identifies one invocation at its calculation or construction locus, from taking up those operands for that operation until return or termination. References to the same uninterrupted invocation reidentify one application. A second invocation, including a nested or later one with the same operands, method, qualification window and result, is another application. Changing an operand after beginning a fresh calculation starts another invocation; a continuation of an interrupted calculation counts as the same application only when continuity of that same invocation is established.

The **ApplicationExtentRule** takes that invocation's interval: first use of its arguments through its return or termination. For the guard it is the eligibility evaluation; for compose it is the composite construction; for quotient it is the class construction; for apply it is the value calculation. An unfinished invocation has an open extent and no unreturned result binding. The data's qualification window and the method's validity window do not date these invocations. A trace may designate an invocation; a copied record, matching value or valid method identifier does not establish it. Ordinary function and projection guidance remains usable without an assertion of dated U.Work.

For example, with fixed method `n(x)=x/10`, domain [0,100] and the same CN-Spec, two separate calculations of `n(20)` both return 2. The first operand-to-return episode and the second are two `apply` occurrences; each binds 20 and its own return of 2. A third record containing 2, with no corresponding calculation, supplies no third result binding. Two constructions of `g∘n`, or of the same quotient, are likewise distinct when performed in separate construction episodes; their equal constructed mathematical values do not merge those episodes. Conversely, a second description of the first episode adds no application.

**LawSet (UNM laws; identifiers are stable)**
- **UNM‑L0 (Values, not characteristics).** UNM produces `NCV` as a **value** under declared invariants; it does not redefine the underlying characteristic meaning (measurement meaning remains governed by A.17/A.18 and evidence by C.16).
- **UNM‑L1 (Declared method class gate).** A normalization method instance is admissible only if its method is declared in the allowed method class set: `{ratio:scale, interval:affine, ordinal:monotone, nominal:categorical, tabular:LUT(+uncertainty)}`.
- **UNM‑L1a (Method semantics are governed by the method).** `NormalizationMethod` defines invariants, closure (composition / inverses where defined), and validity rules. UNM consumes these declarations; it does not invent extra admissibility.
- **UNM-L2 (Directed result before narrower claims).** Return the defined transformed value with its domain and preserved/lost distinctions. Functional equality of outputs forms equivalence classes on that domain. A receiving operation descends only after compatibility and, for a partial operation, representative-independent availability hold. A query descends only when constant on the classes; otherwise retain/refine the input or return the missing distinction.
- **UNM-L2a (Declared-basis locality).** Every transformed value, function-kernel equivalence and stronger operation/query claim retains the selected method, domain, characteristic space, its separately referenced description episteme, CN-Spec edition, bearer and comparison basis. Keep the scope and data window and the method's declared validity window. Reusing an unchanged equivalence for a new query does not make that query recoverable; assess its own constancy/compatibility and the receiving-use conditions.
- **UNM‑L3 (Fail‑closed).** If admissibility/evidence is insufficient (or required inputs are missing/stale), UNM does not coerce; it yields `abstain` or `degrade` (tri‑state guard discipline) and may surface a freshness/work request (see A.19.UNM:4.5).
  *Didactic reading:* `abstain` ⇒ no admitted NCV from this proposed application, so a comparison depending on that output cannot proceed on this basis; `degrade` ⇒ NCV may be produced but must be treated as policy‑gated and auditable (never “quietly good enough”).
- **UNM‑L4 (No implicit indicatorization).** `NCV` does not imply “indicator”; indicator status is a separate policy step (UINDM).
- **UNM-L5 (Relation before reuse).** When a receiving comparison depends on an F.9 Bridge, kind relation or plane relation, establish that relation under its own rule and separately assess the receiving use. For an F.9 use, retain its direction, correspondence rule, loss tolerance and required reliance disposition. A change of bearer, scope, corpus, scale, method or window does not itself establish a relation. Assess losses under the receiving rule; a numerical assurance penalty requires an applicable domain model under B.3.
- **UNM‑L6 (Time explicitness).** Validity windows are named; no implicit “latest”.
- **UNM-L7 (Auditability).** The application's selected specifications, supplied inputs, method, conditions, evidence, returned result and any relied-on relation must be recoverable under Audit below. Missing inputs or unresolved references remain explicit when eligibility abstains.
- **UNM-L8 (Source references).** Downstream uses cite the method, CN-Spec, basis and evidence editions on which they rely; a registry helps locate those sources but does not supply their content.
- **UNM-L9 (Publication boundary).** Publication and telemetry remain outside these operation declarations; any published normalization result retains the meaning defined here. The Audit information is separately recoverable.

**AdmissibilityConditions**
Definition (UNM‑Eligibility):
`UNM_Eligibility(NormalizationMethodInstanceSlot, CoordinateValueSlot, CharacteristicSpaceSlot, CNSpecSlot) → GuardDecision`
where `GuardDecision ∈ {pass | degrade | abstain}` and follows this predicate semantics:
- **pass** iff all of the following hold:
  - (**CN-Spec binding**) the selected `NormalizationMethodInstanceId` is declared in `CN_Spec.normalization.instances` (or an equivalent declaration), its method kind is included in `CN_Spec.normalization.methods`, and (if present) it satisfies `normalization.admissible_reparameterizations`; the characteristic space, its separately referenced description episteme, CN-Spec edition, bearer, reference or comparison basis and intended comparison are recoverable, together with any scope, selected slices or qualification window required by those declarations or that use;
  - (**Target coordinate binding**) the input `CV`’s `slot_id` belongs to the method instance’s declared bound coordinate set and its value lies in the selected transformation's input domain;
  - (**Scale‑regime compatibility**) the method kind is compatible with the coordinate’s regime (`ratio:scale | interval:affine | ordinal:monotone | nominal:categorical | tabular:LUT(+uncertainty)`) and preserves the declared `NormalizationInvariant[*]` (from `CN_Spec.normalization.invariants` and/or the method description);
  - (**Validity window**) the method instance’s validity window covers the active slice/time policy (no implicit “latest”);
  - (**Evidence sufficiency when routed into governance**) when `comparability.mode = normalization-based` (or downstream uses `NCV` in gated decisions), the method instance’s evidence pins satisfy `CN_Spec.comparability.minimal_evidence` (structure typically gated by `G.0`; evidence semantics governed by `C.16`).
- **degrade** iff all non‑evidence conditions above hold, but the evidence check does not pass and the declared failure behavior permits producing a policy‑gated degraded `NCV` rather than abstaining.
- **abstain** otherwise (including missing binding, coordinate mismatch, undefined input, out-of-window validity, or evidence failure when the declared failure behavior is abstain).

**Applicability**
UNM is applicable when:
- `CN_Spec.comparability.mode = normalization-based`, or
- a declared downstream step requires “compare-on-invariants” and thus requires normalization.

UNM is typically skipped when `comparability.mode = coordinatewise` (unless an explicit downstream step requires a declared quotient/fix anyway).

**Relation and reuse boundary**
- A normalized value retains the method instance and edition, its declared validity window, characteristic space, separately referenced description episteme, CN-Spec edition, bearer, reference or comparison basis, evidence and intended comparison, with any scope or data window.
- If a receiving use depends on a relation between distinct source-local meanings, cite the F.9 Bridge, its direction, what it preserves or loses, and that receiving use. If reference planes differ and the comparison depends on their relation, cite the plane relation as a separate claim.
- A changed bearer, scope, corpus, scale, method or window does not by itself establish either relation. A correspondence between bearer kinds has its own grounds. Retain the receiving-use rule and its loss limits; quantify an assurance effect only under an applicable B.3 domain model.

**Γ_timePolicy**
- Default: `point` (no implicit “latest”).
- If normalization relies on time windows, the validity window is part of the method instance and must be declared.

**PlaneRegime**
- A normalized value keeps the reference plane declared for its input and intended comparison; normalization creates no implicit plane crossing.
- When a comparison relies on a relation between different planes, cite that relation, its direction and loss, and keep its use separate from the normalization result.

**Audit**
Make the following information recoverable from the specifications, inputs, evidence and results used. Retain a separate record when the receiving use requires one. For an incomplete eligibility proposal, identify missing inputs or unresolved references and the resulting `abstain`; do not invent an `apply` occurrence or an NCV.
- for a supplied and resolved CN-Spec, `CNSpecRef.edition` + `comparability.mode`, the `CharacteristicSpaceRef`, the separate `characteristicSpaceDescriptionRef: U.EpistemeRef` pinned there, and the evaluated bearer
- (when present) `CN_Spec.normalization.UNM_id` (the selected UNM declaration identity for this CN-Spec)
- the selected `NormalizationMethodInstanceId`, when resolved, its validity window and any `NormalizationMethodDescriptionRef.edition`
- declared `NormalizationInvariant[*]` and `NormalizationFixSpec` (if used)
- any declared admissible re-parameterizations (if present in `CN_Spec.normalization`)
- reference or comparison basis, intended comparison, all evidence pins used, and any claim scope, selected slices or data window that qualify this use
- an F.9 Bridge, kind relation, or plane relation only when the recorded result or receiving use relies on it, including direction, preserved or lost meaning, and the receiving use
- the operation evaluated or applied, its returned value or absence of a result, and any emitted `FreshnessRequest` / work request identifiers (see §4.5)

#### A.19.UNM:4.2 - CN-frame wiring: `normalization` and comparability routing (normative-by-reference)

CN-Spec selects normalization and the basis of comparison:
- `comparability.mode ∈ {coordinatewise, normalization-based}` governs whether comparisons are done directly or “normalize-then-compare”.
- `normalization.UNM_id?` selects the UNM declaration episteme and its edition for this CN-frame.
- `normalization.methods / instances / method_descriptions / invariants / fix` provide the declared surface that UNM consumes.

(If present) `normalization.admissible_reparameterizations` constrain which re‑parameterizations count as “admissible” under the declared invariants.
A.19.CN defines these CN-Spec fields; this section states how UNM uses them.

#### A.19.UNM:4.3 - Evidence and calibration are governed by MM‑CHR (normative-by-reference)

Ground the normalization's applicability and preservation claims in the relevant evidence, calibration and validity account under C.16, referenced from the configured method. A reference identifies that basis; assess its content for the receiving use.

#### A.19.UNM:4.4 - Select the result needed by the receiver

For a value comparison, first use the transformed values and their declared preservation/loss basis. Ask whether that basis retains every distinction the comparison requires. Keep original values, refine the normalization, or return the missing distinction when it does not.

Form classes only when their set-level result is useful. For an operation on classes, check output compatibility and partial-operation availability. For a query, check class constancy. Name a `NormalizationFix` only when an already justified class use needs a representative. A representative-selection policy and additional evidence cannot repair a false compatibility theorem.

#### A.19.UNM:4.5 - P2W and transformation-flow integration note (normative-by-reference)

When UNM is used inside transformation-flow structures/graphs (e.g., `E.18`):
- UNM occurs **before** selection/decision steps.
- If required measurements are **missing or stale**, apply the declared `abstain` or `degrade` rule and state the gap. The receiving practitioner first checks whether an adequate current basis is already available and whether obtaining new evidence is worth doing. Any chosen acquisition is separately planned and performed under its applicable method; UNM itself neither obtains measurements nor mandates new Work.
- A receiving step cites the normalized values, method and CN-Spec editions, bearer, comparison basis, evidence, intended use and scope/window. Establish any relation and its receiving-use conditions under UNM-L5; an assurance penalty follows the applicable B.3 domain model.
- Downstream consumers cite editioned method, basis and evidence anchors as refs and do not re-author them.

### A.19.UNM:5 - Archetypal Grounding

Use the normalization declaration to re-express coordinate values with their preserved and lost distinctions:
1) Choose an admissible configured method with its evidence and validity window.
2) Apply it to produce NCVs.
3) Return an inverse, equivalence, class-level operation or query result only when its additional conditions hold for the receiving use.

**Normalization before comparison.** A team compares alternatives using `normalization-based` comparability:
- CN-Spec declares:
  - `comparability.mode = normalization-based`
  - `normalization.invariants = {unit-alignment, polarity}`
  - a method instance `M_unitScale` with validity window `VW_2026Q1` and evidence pins.
- UNM applies `M_unitScale` to each coordinate value, producing NCVs.
- CPM compares the NCV-profiles (not raw profiles).
- If required evidence pins are missing for a slice, UNM returns `GuardDecision = abstain`; this comparison cannot rely on a new admitted NCV.

**A many-to-one LUT.** Let D be `{0,1,2}` and `n(0)=0`, `n(1)=n(2)=1`. Applying n to 2 returns the transformed value 1. Equality of outputs partitions D into `{0}` and `{1,2}`: it is reflexive, symmetric and transitive. The directed edge `2→1` supplies no edge `1→2`.

The query `x>0` is constant on each class and can be answered from the class. The query `x>1` is false at 1 and true at 2, so no function of their common class can recover it. Retain x, split that class with the needed distinction, or return the unresolved answer set `{false,true}` when that set answers the receiving question. Selecting 1 as a representative would answer a question about the representative, not the lost original input.

Now let a partial operation f be defined at 0 and 1 but not at 2, with `f(1)=0`. Because `1 ≡_UNM 2` while availability differs, f cannot descend to a representative-independent operation on these classes. Matching only the outputs that happen to exist would miss the failure. Preserve the distinguishing input or refine the class before applying f.

**Reversible conversion and partial normalization.** For exact temperature values in the declared physical domain, Celsius-to-kelvin conversion `n(c)=c+273.15` has inverse `c=k-273.15` on its image. For example, 20 °C maps to 293.15 K and back to 20 °C. Measurement uncertainty remains governed by its measurement result; the exact coordinate law does not remove it. More generally, a strictly monotone encoding has an inverse on its image, not automatically everywhere in the named target.

Restrict the LUT above to D=`{0,1}`. Input 2 is then undefined, has no NCV and belongs to no kernel class of that partial normalizer. A policy's degraded-evidence allowance does not define n(2). Likewise, an idempotence claim needs composability and `n(n(x))=n(x)` on the named domain; a function's fibers do not prove it.

**Missing or stale inputs in a transformation flow.**
- A selector (or comparator) requires comparability under `normalization-based` mode.
- UNM finds that a required coordinate value is missing/stale for the current slice and the instance validity window.
- UNM returns `GuardDecision = abstain` (fail-closed) and identifies the missing current measurement. The receiver may reuse an adequate existing result, choose a justified acquisition, or leave this comparison unresolved; any acquisition has its own planning and enactment basis.

### A.19.UNM:6 - Bias‑Annotation

Common cognitive traps around normalization:
- **Normalization-as-truth bias:** treating an NCV as a justified answer before checking its input basis, transformation and receiving-use conditions.
- **Hidden-steps bias:** assuming normalization “happened somewhere” and skipping routing/pins.
- **Unit-blindness:** treating numeric sameness as semantic sameness.
- **Proxy legitimacy:** assuming a popular method is legitimate without evidence pins or validity region.

Mitigation: enforce `NormalizationMethodInstance` + validity window + evidence pins; and distinguish the directed output, optional classes and any separately justified operation or query on them.

### A.19.UNM:7 - Conformance Checklist

- [ ] **Normalization identity:** cite the selected method and configured instance, its description, invariants and any representative-fixing rule. Resolve legacy identifiers through F.18 when used. An ordinary coordinate mapping does not assert a specialized `Map` kind or a Bridge; apply the lexical distinction in §4.0.
- [ ] **CN routing:** uses `CN_Spec.comparability.mode` and the `CN_Spec.normalization` surface; does not embed “shadow CN-spec”.
- [ ] **Fail-closed:** eligibility is tri-state and never coerces unknown to pass.
- [ ] **Lawfulness classes declared:** method class is one of `{ratio:scale, interval:affine, ordinal:monotone, nominal:categorical, tabular:LUT(+uncertainty)}` and the instance's validity window is named.
- [ ] **No indicator conflation:** does not treat NCV as automatically implying indicator status.
- [ ] **Relation and reuse discipline:** recover each NCV's method and CN-Spec editions, bearer, basis, evidence, intended comparison and qualifications. Any relied-on relation and its receiving use satisfy UNM-L5; an assurance penalty has a justified domain model.
- [ ] **Result branch:** the domain, directed output and preserved/lost distinctions are explicit. An inverse is claimed only on its stated image. A set quotient uses equality of function outputs on that domain; an inherited operation also passes compatibility and partial-availability checks, and a recovered query is constant on each class. A required representative has a declared fix and is not treated as the lost original input.
- [ ] **Auditability:** the inputs, method and specification editions, evidence, conditions, result or reason for abstaining, and any relied-on relation are recoverable under Audit in §4.1. A separate record is retained when required by the receiving use.
- [ ] **Source references:** downstream uses cite the method, basis and evidence editions they need, preserving the source definitions.
- [ ] **Missing or stale inputs:** apply the declared abstain/degrade rule and name the gap. An undefined transformation input has no NCV. Reuse an adequate existing basis or plan a justified acquisition under its own method; normalization alone mandates no new Work.
- [ ] **SlotKind discipline:** SlotKind tokens reuse the CHR SlotKind lexicon where applicable; UNM‑specific SlotKinds are docked into the suite lexicon before use (no ad‑hoc drift).


### A.19.UNM:8 - Common Anti‑Patterns and How to Avoid Them

1) **Hidden normalization inside scoring or selection**
   Avoid this by using `CN_Spec.comparability.mode` and applying UNM.

2) **“NCV ⇒ indicator” shortcut**
   Avoid by treating indicatorization as UINDM policy, not a byproduct of normalization.

3) **“We normalized” without declaring invariants**
   Avoid by naming the domain, transformation, preserved invariants and lost distinctions; supply a class or congruence claim only under its additional conditions.

4) **Reusing a normalized value after its basis changed**
   Recover the bearer, method and CN-Spec editions, comparison basis, evidence, intended use and scope/window. Recheck the conditions that changed, including any relation required by the new use.

5) **Choosing a representative implicitly**
   Avoid by either keeping quotient objects abstract or declaring `NormalizationFix`.

6) **Treating a generic mapping word as a specialized relation claim**
   State the normalization's operands, rule, invariants and loss. Test any specialized `Map` or F.9 Bridge claim separately under its defining pattern.

7) **Treating UNM outputs as comparable beyond their declared bearer, basis, scope/window, or reference plane**
   Avoid by keeping comparison local to the recorded premises. Where a conclusion depends on another source-local meaning, bearer kind, or plane, cite the obtaining relation and its loss; otherwise constitute a new normalization result or fail closed.

8) **Re-authoring method, basis, or evidence anchors downstream**
   Avoid by citing the editioned method, basis, and evidence anchors as refs; a downstream pattern neither rewrites them nor replaces them with a generic registry.

### A.19.UNM:9 - Consequences

**Benefits**
- Makes the selected normalization and comparison basis inspectable.
- Separates the common operation contract from each method's definition and applicability.
- Allows a method family to change without changing the common operation contract when its meanings and conditions remain compatible.
- Makes known admission failures explicit through the declared guard result; correctness still depends on the grounds used by the evaluation.

**Costs**
- Requires declarations (method instance, invariants, validity window, evidence pins).
- Class-level use requires compatibility/query arguments; ordinary transformed-value use need not construct a quotient or fix.

### A.19.UNM:10 - Rationale

UNM separates three contributions needed to justify a normalized value:
- The selected transformation defines its domain, output and preservation/loss conditions.
- CN-Spec states when normalization is needed and which configured method applies to the comparison.
- C.16 supplies measurement and calibration grounds for that use.

The receiving use determines which distinctions must survive and whether a relation to another meaning, kind or plane is required. Those relations and any assurance calculation retain their own conditions; a common numeric range supplies none of these grounds.



### A.19.UNM:11 - SoTA-Echoing — preserve the answer needed after normalization

**Practice question.** May a receiver answer its original query from normalized values after the transformation merges inputs? The selected mathematical condition checks whether that query is constant on each fiber of the declared function. An alternative keeps only bounded normalized values and uses a representative or inverse-transform interface for later queries. The latter is convenient when the receiver deliberately accepts the lost distinctions; it is insufficient for recovering an exact original-input answer that differs within a fiber.

The [Lean reference on quotients](https://lean-lang.org/doc/reference/latest/The-Type-System/Quotients/) supplies the mathematical line: lifting a function requires equal results for equivalent representatives. It also describes canonical-representative implementations as a useful alternative representation. **Adopt** the query-constancy criterion in §4.0, UNM-L2 and §4.4. **Reject** the inference that choosing a representative recovers an original-input query: the representative defines a choice, and recovery still needs constancy. These are mathematical conditions; using Lean or constructing a proof-assistant artifact is not required by UNM.

The [scikit-learn 1.9 MinMaxScaler documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html) supplies a preprocessing alternative and its declared trade-off. Optional clipping keeps held-out values in the chosen range, while its documentation warns that inverse transformation may not restore the original data and that clipping can distort the test distribution. **Adapt** this loss disclosure as a receiving-use check, rather than banning bounded preprocessing or treating the software interface as evidence of invertibility.

For example, a declared clipped transform n(x)=min(1,max(0,x/100)) sends 120 and 150 to 1. The query “was x above 130?” gives different answers, so it cannot be recovered from that NCV or its class representative. Keep the original value, refine the output with the needed distinction, or return the unresolved answer allowed by the receiving rule. This is the same test used by the finite-domain example in §5 and the Result branch checklist; separately inherited partial operations also retain their availability check.

At comparable effort, both choices use the same declared transform and query. One counterexample within a fiber can settle failure cheaply; a positive exact-recovery claim needs a constancy argument over the admitted domain, not just sampled successes. Keeping additional input information has a storage/handling cost, while clipping can be appropriate for a model that only needs its bounded input. The chosen rule makes that trade-off explicit and leaves ordinary transformed-value use cheap. Reopen when the receiver changes its query, the transformation or domain changes, or a proposed smaller representation retains the required answer with a sound argument. Neither software documentation nor the quotient theorem supplies measurement legitimacy, evidence sufficiency or assurance for an application.

### A.19.UNM:12 - Relations

**Builds on / cites**
- `E.8` (pattern template)
- `E.20` for introduction or revision of a mechanism definition and its governing-pattern assignment
- `A.15.2` for the edition/reference baseline on a P2W path; `A.15.3` only for typed planned filling of an independently declared position
- `F.18` (alias docking / token continuity, when renaming or retiring legacy UNM tokens)
- `A.6.1` (U.Mechanism shape; specialization discipline)
- `A.19.CHR` (CHR suite boundary; slot lexicon; suite protocols)
- `A.19.CN` (CN_Spec normalization + comparability routing)
- `C.16` (MM‑CHR evidence/calibration carriers)
- `G.0` (CG-frame admissibility gates used downstream)
- `G.2` (SoTA synthesis packs as the method‑family ingress; wiring‑only integration)
- `E.18` (when UNM is used in transformation-flow structures/graphs; P2W freshness/work routing)
- `C.29` when the chosen function, equivalence or quotient leaves an unresolved representation or transfer question; use an adequate local calculation. `B.3` applies to a named assurance claim.

**Used by**
- CHR suite protocols (normalize stage), when `comparability.mode` requires normalization-based comparability.

### A.19.UNM:End
