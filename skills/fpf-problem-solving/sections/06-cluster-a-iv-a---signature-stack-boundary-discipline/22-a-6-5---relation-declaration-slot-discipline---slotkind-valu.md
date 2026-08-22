## A.6.5 - Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative


### A.6.5:1 - Problem frame

**Plain name.** Relation-declaration slot discipline.

**Use this when.** Use this pattern after the direct relation kind has been recovered and a reusable typed declaration of its participants is current for another assertion, comparison, substitution, or reference use. Typical triggers are one relation declaration reused across patterns, another relation referring to an explicitly individuated occurrence, or an engineer checking a proposed replacement participant against the declared ValueKind.

**Primary working reader and concern.** The intended reader is an engineer making one relation declaration reusable while keeping actual relation participants, the `RelationSignature` episteme, relation-participant designations in assertions or descriptions, relation obtaining, and relation occurrence identity distinct.

**Primary EntityOfConcern.** One `SlotSpec` declaration in one exact `RelationSignature`.

**First useful move.** Write the readable relation sentence, identify the relation kind and relation-participant meanings, and name where its predicate, applicability, and identity rule are defined. For every relation-participant meaning whose reusable typed declaration is current, add one SlotSpec to the `RelationSignature`, using the compact declaration notation `SlotSpec = <SlotKind, ValueKind, refMode>`. The angle brackets and ordered entries belong to that notation; they are not parts or participants of the world-side relation. `refMode` states how an assertion or relation-occurrence description episteme carrying a relation-participant designation denotes the actual participant; it does not turn the reference or SlotSpec into that participant. If the direct relation or its relation obtaining predicate is still unclear, stop and use `A.6.P` or `A.6.RSIR`; declaration notation cannot recover a missing ontology.

**First-minute result.** For `Robot_7 is assigned to InspectorSystemRole for this inspection shift`, declare a species under `U.SystemRoleAssignment`, such as `InspectionShiftAssignment`, and state one occurrence for the shift. When reusable participant typing is needed, give `HolderSystemSlot` the value kind `U.System` and entity-reference mode; give `AssignedSystemRoleKindSlot` the value domain `InspectorSystemRoleKindDomain` and by-value reference mode. Add another participant only when it changes the predicate or occurrence identity. An assertion designates the occurrence's participants and states its `assignmentInterval` separately. Stop there unless later work must substitute a participant, distinguish this assignment episode from another, or test an A.2.5 state condition.

**What goes wrong if missed.** In the readable sentence `Robot_7 is assigned to InspectorSystemRole`, the holder system, the exact system-role kind, each declaration-local SlotKind, and each participant designation carried by an assertion episteme can collapse into one word such as *role* or *holder*. A later claim then cannot tell what may be substituted, what retains identity, or whether it refers to a system, a system-role kind, an assignment occurrence, an assignment-state relation, or an assertion about either occurrence.

**What this buys.** Engineers retain a readable relation sentence while its load-bearing uses gain exact participant typing, unambiguous reference use, and a clear route to the definitions or constraints for predicate truth and occurrence identity.

**Not this pattern when.** Use `A.6.P` or `A.6.RSIR` first while the relation kind or its participants remain unresolved. Use `A.6.REL` for relation-occurrence identity, `A.6.0` for the containing `U.Signature`, `C.2.1` for an assertion or description, and `C.3` for a local kind needed by typed quantification. In every other case, find the direct relation's accepted definition before applying this slot discipline.

Select A.6.5 by the engineering use, not by a domain catalogue: one already recovered direct relation needs reusable participant typing in assertions or occurrence descriptions. Its `RelationSignature` contains one SlotSpec for each participant meaning actually reused, with a declaration-local SlotKind, the participant's exact ValueKind, and one designation mode. The worked cases below are contrasts only; none supplies another relation's predicate or definition.

The following objects meet at this boundary and remain distinct:

1. an obtaining relation occurrence in the world;
2. the direct relation kind and its predicate;
3. a `RelationSignature` episteme whose content includes SlotSpecs corresponding to the direct relation's relation-participant meanings and restates its predicate, applicability, and identity rule for reuse;
4. a `SlotSpec` containing the declaration-local SlotKind name for one relation-participant meaning, its actual-participant ValueKind, and its designation mode;
5. an assertion or other episteme claiming that the relation obtains.

Use the `A.6.REL` relation-object architecture. A **relation-participant meaning** is the relation-local semantic content specifying one domain contribution to the obtaining predicate. An **actual relation participant** is the concrete entity participating in an obtaining occurrence under that meaning while retaining its intrinsic kind. A `SlotSpec` is declaration content corresponding to the relation-participant meaning. A **relation-participant designation** is the value or reference of a declared RefKind carried by an assertion or relation-occurrence description episteme to denote the actual participant. Source-specific vocabulary keeps its meaning inside the source representation or ontology until an explicit correspondence relates it to the named FPF object.

The RelationSignature and SlotSpecs are declaration content about reusable relation semantics. The world-side relation obtains under its direct predicate and identity rule independently of those epistemes.
In Tech register, `SlotKind` is the declaration-local kind by which one `RelationSignature` distinguishes a relation-participant meaning. World-side relation prose names the meaning and actual participant directly; the relation occurrence contains no SlotKind. In an assertion or relation-occurrence description episteme, the corresponding SlotSpec distinguishes a relation-participant designation carried by value or by a reference of the declared RefKind. External representation elements retain their source-specific names. A declared correspondence must relate such an element to a named SlotSpec before an FPF relation claim can reuse it.

### A.6.5:2 - Problem

The engineering problem appears when the same relation declaration is used in another claim, substitution, or comparison. A ValueKind that covers participants for which the predicate has different meanings makes typed reuse unsound. A reference value leaves its referent kind unstated. A designator for an actual participant is promoted into a U-kind. A role value is confused with the system that holds it. A verb-shaped predicate is read as proof that the relation is work, a method, a transformation, or an acting holon.

These errors do more than blur terminology. They change which substitutions are valid, which object a later claim may reference, what makes the relation obtain, and which definition or constraint the repair must preserve.

### A.6.5:3 - Forces

| Force | Tension |
|---|---|
| Readability and reuse | The first relation sentence stays simple, while later claims may need exact typed SlotSpecs. |
| Local SlotKind and durable participant | A SlotKind is local to one declaration, while the relation participant keeps the identity and kind defined elsewhere. |
| Exact range and open-ended ontology | A ValueKind needs enough precision for the predicate without forcing every participant into a newly minted U-kind. |
| Embedded value and stable reference | Some assertion or relation-occurrence description epistemes designate an actual participant by value; others designate it through a reference to an independently identified entity. The world-side relation occurrence has the participant directly in either case. |
| Logical form and constructive grounding | Predicate and slot discipline help review a relation, while FPF still needs grounded participants, a relation obtaining predicate, and a relation occurrence-identity rule. |
| Grammatical verb and ontological kind | A verb can express a relation predicate without turning the relation into work, method, transformation, agency, or a holon. |

### A.6.5:4 - Solution

Apply relation-declaration slot discipline only after the direct relation and its relation-participant meanings have been recovered. Give every relation-participant meaning needed by the current typed use one complete `SlotSpec` in the `RelationSignature`. Let the direct-relation definition supply the obtaining predicate and occurrence-identity rule. Follow the `A.6.REL` minimum-current-object rule: a later use adds only its current object and the direct relation to an already recoverable object rather than restating the complete relation-object architecture.

#### A.6.5:4.0 - Ontological status of the discipline

Relation-declaration slot discipline is a rule set, not a durable U-kind. This pattern reuses `RelationSignature`, `SlotSpec`, `SlotKind`, `ValueKind`, and `RefKind` from the existing signature and relation vocabulary; it introduces no U-kind. The notation `U.RelationSlotDiscipline` is not admitted: it has no separate instances, identity rule, grounding rule, constructive assembly, or ontic settlement. A.6.5 constrains one `SlotSpec` declaration belonging to one exact `RelationSignature`. Operation argument and result declarations remain under `A.6.1`; mathematical operands and their order remain representation elements under `C.29`.

A.15.3 may cite one exact SlotSpec as the target of a planned participant designation inside a `U.WorkPlan`. That citation does not fill the SlotSpec, extend SlotSpec to another description family, make the planned designation an actual participant, or make the direct relation obtain. Planned operation arguments and results instead cite their exact A.6.1 declarations. No method-description, plan, work, evaluation, card, schema, or record field becomes a SlotSpec. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant.

#### A.6.5:4.1 - Keep pattern scope exact

| Object or claim | Defining or constraining content | What A.6.5 contributes |
|---|---|---|
| Direct relation kind, relation-participant meanings, and relation obtaining predicate | the direct-relation definition | no replacement; A.6.5 supplies the SlotSpec discipline for a compatible `RelationSignature` |
| Relation occurrence and identity | the direct-relation definition and `A.6.REL` | exact participant ValueKinds; refMode applies only to relation-participant designations in an assertion or relation-occurrence description episteme |
| `RelationSignature` declaration | `A.6.0` defines the containing signature | complete `SlotSpec` declarations inside its vocabulary item |
| Assertion that a predicate obtains | `C.2.1` defines assertion content; the direct claim pattern defines that claim family | no new assertion kind; the assertion can name exact relation participants |
| Local derived kind of participants | `C.3` and `C.3.1` define the local kind and its extent rule | a SlotKind that remains local to the relation declaration |
| Planned participant designation | `A.15.2` and `A.15.3` define the planned claim | one exact SlotSpec may be cited as the target of a planned filling; A.6.5 contributes only the declaration-local SlotKind, ValueKind, and refMode discipline and establishes neither the plan claim nor actual participation |

None of these objects gets its identity or truth condition from A.6.5. A.6.5 supplies the participant-declaration and designation-typing discipline at their shared boundary.

#### A.6.5:4.2 - Declare one complete SlotSpec for each relation-participant meaning needed by typed reuse

The following code block is a compact representation of a declaration under `C.29`. Its assignment mark, angle brackets, order, and alternatives are notation elements; the prose below states their FPF meaning.

```text
SlotSpec := <SlotKind, ValueKind, refMode>
refMode := ByValue | RefKind
```

**SlotKind** is the declaration-local kind by which one exact `RelationSignature` distinguishes one relation-participant meaning. `HolderSystemSlot` and `AssignedSystemRoleKindSlot` are different SlotKinds inside the `InspectionShiftAssignment` declaration even when a receiving assertion designates the holder by reference and the assigned system-role kind by value. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant. A mathematical operand or numbered argument belongs to its mathematical representation, not to the relation declaration.

**ValueKind** is the exact world-side kind admitted for the actual participant corresponding to the declared participant meaning. Recover it from the accepted declaration that defines that kind. The declaration may settle a durable U-kind, a current C.3 kind, a Concept-Set entry, or an imported sort whose bridge states the corresponding FPF kind. If one proposed ValueKind hides several kinds for which the predicate has different meaning, recover their real common kind or split the relation kind. A prose list of alternatives does neither.

**RefKind** is the kind of reference used when a named-use assertion or relation-occurrence description episteme carries a relation-participant designation by reference. A system applying the declared resolution Method obtains a participant of the declared ValueKind as referent. `U.EntityRef`, `U.HolonRef`, `U.EpistemeRef`, and `U.StructureRef` are examples only where their exact RefKind declarations and admission predicates apply. The shorthand `byRef` is usable in a compact local sketch only when the exact RefKind is declared next to that sketch; it is not a complete `refMode` by itself.

**ByValue** means that an assertion or relation-occurrence description episteme carries a value as its relation-participant designation. **By reference** means that it carries a reference value of the declared RefKind as that designation. In both cases, the designation denotes the world-side actual participant. The reference value retains its RefKind, its referent retains the declared ValueKind, the SlotSpec remains declaration content, and the relation occurrence retains its direct identity.

**Naming and source-token repair.** Use `...Slot` only for one declaration-local SlotKind inside one exact `RelationSignature`. Use `...Ref` only for an admitted RefKind or for a reference value or designator of that kind; never use it for the actual participant or the SlotKind. Keep the participant's ValueKind name free of both suffixes. Thus `HolderSystemSlot` is the SlotKind, `U.System` is the participant ValueKind, and `Robot_7_Ref : U.EntityRef` is a reference designation whose referent is `Robot_7 : U.System`. If a source token such as `holder` conflates those objects, split them rather than cosmetically renaming the token. A concrete source field keeps its source name and is related to `HolderSystemSlot` only through an explicit declaration or C.29 correspondence.

#### A.6.5:4.3 - Apply the well-formedness constraints

The following labelled block represents seven rules for reviewing a declaration episteme. The labels and indentation are presentation elements, not SlotSpecs, relation participants, or work occurrences.

```text
A6.5-S1 CompleteSlotSpec:
  every relation-participant meaning needed by reusable typed use has one SlotSpec
  with exactly one SlotKind, one ValueKind, and one refMode.

A6.5-S2 LocalSlotKind:
  SlotKind is interpreted only inside the exact RelationSignature that
  contains the corresponding SlotSpec.

A6.5-S3 ExactParticipantKind:
  each actual participant corresponding to the declared relation-participant meaning
  has the declared ValueKind; each receiving-episteme designation denotes such a participant.
  A C.3 kind ordered by an explicit U.SubkindOf relation may narrow
  that range only when typed membership or substitution is current.

A6.5-S4 HonestReference:
  when refMode is a RefKind, the receiving assertion or description carries
  a reference of that RefKind whose resolution denotes a participant
  of the declared ValueKind. The relation itself does not store it.

A6.5-S5 DirectPredicateDefinition:
  the identified direct-relation definition states the predicate,
  applicability, and any relation occurrence-identity rule.

A6.5-S6 NoHiddenUnion:
  one ValueKind does not hide participant kinds for which the direct
  predicate has different semantics. Recover one real common ValueKind or split the relation kind.

A6.5-S7 RepresentationBoundary:
  a representation or publication form does not become the
  world-side participant or relation occurrence by form.
```

A system performing typed substitution keeps the SlotSpec fixed and checks a proposed relation-participant designation against the exact ValueKind. A system performing retargeting changes a reference value in an assertion or description while preserving SlotKind, ValueKind, and RefKind. Neither operation changes a world-side participant or makes the direct predicate true. The identified direct-relation definition supplies that predicate and identity rule; the current case must supply the relevant facts or constituting history. A system applies the direct obtaining test to those facts or constituting history, and a claim-bearing episteme records affirmative or negative polarity. Only when an explicit reliance judgment is current does `A.10` or the receiving evaluation separately record supported, refuted, or unresolved reliance. Type compatibility, assertion polarity, evidence, and reliance establish neither obtaining nor occurrence identity.

#### A.6.5:4.4 - Distinguish predicate grammar from holonhood and agency

A relation predicate is often written as a verb phrase: a system **is assigned to** a system-role kind, a part **belongs to** a whole, one claim **supports** another, or one occurrence **results from** Work. The grammatical verb only helps express the predicate. It does not settle the ontological kind of what the expression denotes.

Use the following definitions for that distinction:

- `A.15.1` and `A.3.1` supply the constructive assembly, composition, identity, and meta-holon-transition conditions that admit `U.Work` and `U.Method` as holon kinds. `U.Transformation` is instead a root U-kind under `A.3.4` for one independently grounded actual bounded change. Verb-shaped wording proves neither classification.
- One context-local system-role kind is admitted under `C.3` and described through `A.2`; it is neither a holon nor an assignment. An admitted `U.System` participates as holder in an assignment occurrence whose species is declared under `U.SystemRoleAssignment`.
- `U.Relation` is an individuable obtaining relation occurrence under `A.6.REL`. A SlotSpec does not give it constructive parthood or meta-holon transition and does not admit it as a holon.
- Only an admitted `U.System` acts. A system may be classified by an exact local system-role kind and may participate as holder in an obtaining `U.SystemRoleAssignment`; neither the kind nor the assignment acts. Work is performed, a Method is applied in Work, and a transformation occurs or is carried out. The relation, Method, Work, transformation, kind, signature, and structure do not become actors because prose gives them an active verb.

When one word could denote a relation predicate or a holon occurrence, first ground the participants and ask what obtaining or occurrence identity rule the receiving claim needs. Then find its definition. Do not decide by part of speech.

Predicate grammar also decides neither claim polarity nor reliance. An ordinary relational assertion states affirmative or negative polarity for the exact direct predicate; a forecast, scenario, counterfactual, permission, or other claim family retains the rules that define that claim family. Only when an explicit reliance judgment is current for the declared use does `A.10` or the receiving evaluation separately state supported, refuted, or unresolved reliance. None of those claim-side distinctions makes the world-side relation obtain.

#### A.6.5:4.4a - Keep ordinary predicate parameters outside SlotSpec

A reusable predicate definition may be an ordinary A.6.0 `U.Signature` without being a `RelationSignature`. Its semantic parameters are not SlotSpecs unless an independently admitted direct relation kind has world-side participant meanings that a typed receiver must reuse. In particular, the `dependentContent` and `baseContent` parameters of `RuleContentBasisFindingDefinition@R7` are `U.ClaimGraph` values in a predicate declaration. They do not name relation participants, `SlotKind`s, occurrence positions, or a new relation kind.

A C.2.1 assertion of `derivedUsingRuleContent` or `evaluatedAgainstRuleContent` designates those exact values and its exact derivation or criterion-selection claim. A record or formula may represent the parameters under C.29, but table shape does not turn them into SlotSpecs. If later work proposes a relation kind, it must independently pass A.6.RCD and E.24/E.24.UK with participant meanings, obtaining, applicability, and occurrence identity; the predicate declaration supplies none by implication.

#### A.6.5:4.5 - Use progressive elaboration

Start with the lightest object that supports the named engineering use. The branch diagram maps three independent receiving-use thresholds that share one recovered direct relation; none is a prerequisite for either of the others:

```text
readable assertion of the recovered direct relation
  +-- reusable RelationSignature with SlotSpecs, when several uses need the same participant typing
  +-- explicit occurrence individuation, when a named claim or direct relation relies on occurrence identity
      +-- relation-occurrence description episteme, when a receiving episteme describes the occurrence
      +-- stable relation-occurrence reference, when a receiving episteme contains a designation of it
  +-- local C.3 kind with an extent rule, when typed quantification over corresponding participants is current
```

The branch marks are representation edges under `C.29`, not transitions in a drafting process, world-side relations, or work occurrences. They show only which additional object the named use consumes. The diagram does not make a `RelationSignature` prerequisite for explicit occurrence individuation, and it neither makes the direct relation obtain nor supplies occurrence identity. The direct-relation definition supplies the obtaining predicate; current case facts or constituting history must satisfy it. The direct occurrence-identity rule determines which occurrence is being distinguished only after that factual condition is met.

The local-kind branch does not turn every participant qualification into a kind. It is justified only when membership, substitution, quantification, or `U.SubkindOf` reasoning will be performed.

#### A.6.5:4.6 - Dispatch the world-side fact, claim, and local kind

| Current reading | Object or claim | Next pattern |
|---|---|---|
| Relevant current-case facts or constituting history satisfy the direct obtaining predicate for these participants | one world-side relation occurrence whose participants retain their own kinds | direct relation pattern for the test and identity rule; the current case for its factual basis; `A.6.REL` only when occurrence identity is consumed |
| A claim-bearing episteme designates the participants under declared SlotSpecs and records affirmative or negative polarity for the direct predicate; evidence and reliance remain separate when used | an assertion episteme about the direct relation; an affirmative assertion may designate an occurrence only after current-case facts or constituting history satisfy the direct predicate and the identity rule has been applied; the assertion states but does not warrant or constitute that result; forecasts, scenarios, counterfactuals, permissions, and other claim families retain their own defining rules | `C.2.1`, A.6.5, and the direct claim-family definition; add `A.10` or the receiving evaluation only when a reliance judgment is current |
| A typed claim ranges over all actual participants corresponding to one declared participant meaning | local C.3 kind whose extent rule selects those participants | `C.3` and `C.3.1` |

These readings do not leave a fourth object called `RelationDefinedQualification`. Do not introduce that name or `E.24.RC`.

They also do not justify a parallel `S-kind` hierarchy for relation-position readings. Keep the direct relation fact under its relation pattern, the claim under `C.2.1`, and introduce a C.3 local kind only when membership, substitution, quantification, or typed reasoning is current.

Do not replace that split with a generic `KindWitnessedFillerSpec` or filler record. The declaration's exact local `ValueKind` types the participant meaning; when typed quantification is current, a separately defined C.3 local kind and its membership rule supply the reusable classification.

#### A.6.5:4.7 - Read the SlotSpecs of a Direct System-Role-Assignment Species

`A.2.1` defines the `U.SystemRoleAssignment` relation family through directly declared species. The family has no root `RelationSignature` that hides several participant laws. For the simple `InspectionShiftAssignment` species, a compatible `RelationSignature` declares these SlotSpecs under A.6.5:

| SlotKind | ValueKind | refMode | Meaning |
|---|---|---|---|
| `HolderSystemSlot` | `U.System` | `U.EntityRef` | The admitted system that is the holder; a receiving assertion designates it by an entity reference. |
| `AssignedSystemRoleKindSlot` | `InspectorSystemRoleKindDomain` | `ByValue` | The exact local system-role kind assigned under this direct species. |

Every assignment species declares its own participant meanings, predicate, applicability, and occurrence-identity rule. It adds another participant meaning only when its corresponding participant changes the predicate or occurrence identity. A `KindSignature`, system-role-taxonomy episteme, effective reference scheme, bridge, or model-use structure may interpret a receiving assertion or use when needed; it is not another participant merely because it helps interpret the claim.

`assignmentInterval` is not another SlotKind or a ValueKind admitted for a relation participant. It is a local content value in an assignment assertion or relation-occurrence description. The field states the currently known temporal extent of one occurrence, including an explicit open end when the occurrence is current. Under `A.2.1`, an occurrence of one direct species begins when its predicate starts obtaining for all fixed actual participants and continues while it obtains without interruption. Closing an open temporal description refines the same occurrence when continuity holds. A missing-evidence interval remains unknown; only demonstrated non-assignment ends that occurrence. A.2.5 defines assignment-state predicates and direct state relations; the patterns for capability, performed Work, and supporting claims retain their distinct definitions.

#### A.6.5:4.8 - Recover interface and port relations before declaring slots

Keep recognizable source words such as **interface**, **port**, **endpoint**, **API**, and **signature** in the recognition sentence; do not erase them and do not promote them into a generic `U.Interface`. Then use this sequence:

1. Repeat the source sentence so the practitioner can still recognize the situation.
2. Say in ordinary language what connects, crosses, or is transferred between which exact entities.
3. Recover the exact direct relation and its definition. If no current definition supplies the needed participant meanings, predicate, applicability, and identity rule, require `A.6.RSIR` or record one missing-relation result naming the proposed participants, required predicate, and receiving use.
4. Only after that relation closes, let its `RelationSignature` declare the SlotSpecs for participant meanings actually reused by the receiving typed claim.

**Compact contrast.** In “the evaporator outlet interfaces with the compressor inlet,” keep **interfaces** for recognition. If the intended claim is that refrigerant crosses from one named outlet to one named inlet, name that medium and those two endpoints and recover the exact transfer-relation definition before declaring any slots. If **interface** instead names a diagram boundary, API description, protocol, or publication form, use the definition for that object and use. A catalogue of possible participants closes neither branch; without a definition of the direct relation, stop before a `RelationSignature`.

#### A.6.5:4.9 - Name the operation by the object that changes

| Operation | Exact change | Relevant defining or constraining content |
|---|---|---|
| supply a designation under one SlotSpec in an assertion or description | carry a value or reference that designates the actual participant admitted by that SlotSpec | A.6.5 supplies designation typing; the direct-relation definition supplies the participant meaning and predicate |
| replace a participant designation in an assertion or description | change the designation associated with one SlotSpec while preserving that SlotSpec | resolve the new designation, then let a system apply the direct obtaining test to the relevant facts or constituting history before recording assertion polarity and any separate reliance posture |
| substitute a participant designation in typed reasoning | replace one designation with another while preserving the SlotSpec and testing ValueKind compatibility; this operation does not replace a world-side participant or establish predicate truth | A.6.5, with C.3 only when the reasoning quantifies over a local participant kind |
| retarget a reference | replace one reference value in an episteme with another of the same RefKind | the receiving episteme's definition states how it carries the designation; the effective reference scheme supplies the resolution rules and the RefKind declaration constrains the referent range; F.18 enters only when a durable name changes; world-side change is a separate claim |
| resolve a reference | obtain the designated referent from a reference under its reference scheme | the effective reference scheme supplies the resolution rules and the direct RefKind pattern constrains the referent range; F.18 enters only when durable naming is current |
| revise or re-edition a referent | change the referred object or episteme under its own continuity rules | direct object and edition patterns |

`F.18` supplies the rules for durable name designation; participant-designation substitution and reference resolution do not. When a system selects a method at run time, use the definition of that method family or selector; A.6.5 supplies no method-selection operation. Do not rename that choice with the generic slot `binding` metaphor. If early or late timing matters, name which operation in this table is early or late.

### A.6.5:5 - Archetypal Grounding

#### A.6.5:5.1 - System-role assignment: first minute, substitution, and repeated occurrence

**First minute.** Assume the case facts explicitly: `Robot_7` is an admitted `U.System`; `InspectorSystemRole` is a local system-role kind; and `InspectionShiftAssignment <: U.SystemRoleAssignment` declares only two participant positions, holder System and assigned system-role kind. `InspectionShiftAssignment-17` is the occurrence with those values that obtains without interruption from 09:00 to 17:00 on 13 July. A.2.1 defines the species predicate and continuity rule; it does not inspect this robot or warrant the assertion. The stated case facts satisfy that predicate, and the `SystemRoleAssignmentAssertion` records affirmative polarity. Any evidence and reliance posture remain separately established. The following field block represents that assertion episteme under `C.29`:

```text
SystemRoleAssignmentAssertion:
  directClaimFamilyRef: A.2.1 InspectionShiftAssignment
  participantDesignations:
    HolderSystemSlot: Robot_7_Ref
    AssignedSystemRoleKindSlot: InspectorSystemRole
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The two labels inside `participantDesignations` are convenient source-side labels in this compact representation. An explicit C.29 correspondence relates each label to the matching SlotKind in the `InspectionShiftAssignmentRelationSignature`; equal spelling does not identify field and SlotKind, and another source field keeps its own name. `assignmentInterval` is a different assertion field and corresponds to no relation-participant SlotSpec. `Robot_7_Ref : U.EntityRef` resolves to `Robot_7 : U.System`; `InspectorSystemRole` is carried by value under the declaration-local `InspectorSystemRoleKindDomain`. The assertion does not create the assignment, and neither the system-role kind, assertion, nor assignment performs inspection Work.

If inspection admission also needs `InspectionReady`, A.2.5 tests `InspectionShiftAssignment-17` against that exact `SystemRoleAssignmentStatePredicate`. The resulting `SystemRoleAssignmentStateRelation` is separate from the assignment and has its own maximal continuous truth interval. The assignment may continue while that state relation ceases to obtain.

**Substitution.** Assume `Robot_8_Ref : U.EntityRef` resolves to another admitted `Robot_8 : U.System`. Replacing only the `HolderSystemSlot` designation with `Robot_8_Ref` passes the declared ValueKind check, but it does not create an assignment for `Robot_8`. Current case facts must separately satisfy the direct `InspectionShiftAssignment` predicate before an affirmative assertion is warranted. The proposed designation can therefore be type-correct while the direct claim remains negative or unresolved.

**Repeated occurrence.** If the same two participants enter another inspection shift after a demonstrated non-assignment period, the A.2.1 continuity rule ends the first occurrence and starts another. A copied field block or reused row key does not merge them. Conversely, closing an open `assignmentInterval` for one uninterrupted assignment refines the same occurrence; an evidence gap alone does not split it. Under that continuing assignment, `true → false → true` for one fixed A.2.5 predicate creates two assignment-state-relation occurrences without creating another assignment.

#### A.6.5:5.2 - Hypothetical physical-assembly boundary

`Bearing_B isPartOf Pump_P` may remain a readable source claim, but current A.14 supplies no generic or installed-part occurrence-identity rule based on removal, reinstallation, installation interval, or installation work. `PartHolonSlot`, `WholeHolonSlot`, and their RefKinds are therefore only a hypothetical declaration candidate until an accepted direct part-relation pattern states the participant meanings, predicate, applicability, and same-versus-new-occurrence rule. Do not claim current conformance or an individuated part-relation occurrence from this sketch.

Conditional on such a future declaration, changing a proposed part designation from `Bearing_B_Ref` to `Bearing_C_Ref` could be ValueKind-compatible while the direct relation remains false because current case facts do not satisfy its predicate. Until that parthood relation is defined, keep the bearings, pump, installation work, proposed part relation, assertion, designations, and representation separate. The counterexample demonstrates that typed substitution cannot create obtaining; it does not supply the missing parthood settlement.

#### A.6.5:5.3 - Episteme fields are not relation participants by table shape

An evaluation episteme has an EntityOfConcernRef, contains a ClaimGraph, and states an effective ReferenceScheme under `C.2.1`. A card or tuple view may contain visible fields such as `entityOfConcernRef`, `claimGraph`, and `referenceScheme`. Their co-occurrence in one record does not by itself establish another world-side relation, make the fields participants, or declare SlotSpecs for them.

When a direct relation among an episteme and other entities is current, its definition states the relation kind, participant meanings, obtaining condition, and occurrence identity, and its compatible `RelationSignature` contains the needed SlotSpecs. A.6.5 supplies the rules for typing participant designations in a receiving assertion. This prevents a convenient episteme form from becoming a pseudo-relation merely because it can be drawn as a tuple or table.

#### A.6.5:5.4 - Relation-dependent result wording

After machining, the machined component can remain the same physical entity in a changed state. It does not acquire a special result kind. Start with one question: **did this same component continue through the change, or did a new entity begin?**

1. **Same component continued.** Name that component, the characteristic that changed, and the actual machining transformation. Use the pattern that defines that characteristic and A.3.4 for the bounded change. The component's identity continues; calling it the work's “result” adds no kind, participant meaning, or relation.
2. **A new entity began.** Use this branch only when a current definition supplies an admitted identity-inception predicate and identity rule and the current Work and change facts satisfy them. If no such definition exists, return one missing identity-inception result naming the candidate entity, relevant work and change facts, required inception predicate, and receiving use. Do not infer a generic work-result relation.
3. **The sentence names another relation.** Rewrite it with its one concrete verb and participants before declaring slots. For example, `Component_C was delivered to AssemblyCell_2` selects one candidate delivery claim about that item and receiver, not a `result` kind. Recover that direct relation's definition and any additional participant meanings it requires; if it does not close, return a missing-relation result. Handle an evaluation or acceptance sentence separately when that is the actual wording rather than listing possible pattern families.

Only the direct relation selected by one of those concrete sentences receives a compatible `RelationSignature`, and only when reusable typed use is current. Its assertion episteme records that relation; A.6.5 neither invents a broad result participant nor turns the domain choice into a catalogue.

#### A.6.5:5.5 - Formal reduced case

The expression `3 < 5` is notation carried by a mathematical assertion episteme. Its numeral occurrences, comparison sign, and left and right operand places are representation elements under `C.29`; they are not thereby FPF relation participants or SlotSpecs. When a reusable direct-relation declaration is current in an FPF use, the relation definition must identify what entities the numerals designate, the lesser-number and greater-number participant meanings, and the obtaining condition. Its `RelationSignature` may then contain local SlotSpecs such as `LesserNumberSlot` and `GreaterNumberSlot`. An explicit correspondence relates the operand places and their designations to those SlotSpecs. Operand order remains local to the mathematical representation, and the notation alone neither establishes the world-side relation nor individuates an occurrence. No receiving use in this case relies on occurrence identity, so the engineer stops at the typed assertion.

### A.6.5:6 - Bias-Annotation

This pattern has a typed-declaration bias because it serves relation uses that depend on reusable participant typing. Progressive elaboration limits that bias: ordinary users stop at a readable relation sentence when no receiving use depends on SlotSpecs.

It also has a logic-facing bias because predicates and typed declarations make substitution and comparison reviewable. Constructive FPF adds what that logical form alone cannot supply: grounded participants, a direct obtaining condition, and an occurrence identity rule when identity is needed.

A declaration episteme describes reusable relation semantics; a separate representation episteme may represent an assertion or relation-occurrence description. Neither episteme is the world-side relation occurrence by form, and publication changes neither identity.

### A.6.5:7 - Conformance Checklist

1. The direct relation kind and the definition of its predicate, applicability, participant meanings, and identity rule are named before SlotSpecs are declared.
2. Every participant meaning needed by reusable typed use has one complete `<SlotKind, ValueKind, refMode>` SlotSpec in the `RelationSignature`.
3. Each SlotKind is local to the one exact `RelationSignature` that contains its SlotSpec.
4. World-side relation prose names participant meanings and actual participants; declaration prose uses `SlotSpec` and `...Slot` only for declaration-local SlotKinds; receiving-episteme prose names participant designations and uses `...Ref` only for admitted RefKinds or reference values of those kinds. Actual participant ValueKind names carry neither suffix. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant. `Position` and `place` are not alternate FPF names for a declaration slot.
5. Each ValueKind is exact enough for the direct predicate and does not combine participant kinds for which the predicate has different semantics.
6. An assertion or description episteme that designates a participant by reference names the exact RefKind and resolves it to the declared ValueKind.
7. The actual relation participant, its reference, reference resolution, SlotSpec declaration, participant designation in the assertion, and relation occurrence remain distinct.
8. A C.3 kind is introduced only for a current typed-quantification, membership, substitution, or subkind use.
9. A verb-shaped predicate is not used as evidence of work, method, transformation, agency, or holonhood.
10. Only an admitted `U.System` is admitted for `HolderSystemSlot`. Each species under `U.SystemRoleAssignment` declares its `AssignedSystemRoleKindSlot` domain and any additional participant meaning whose value changes the predicate or occurrence identity.
11. `U.Work` and `U.Method` rely on their own constructive holon tests, while `U.Transformation` relies on `A.3.4`'s actual-bounded-change identity; A.6.5 admits none of them by grammar.
12. The direct-relation definition supplies the obtaining predicate and occurrence-identity rule; current-case facts or constituting history supply the factual basis; a claim-bearing episteme records polarity; and evidence or reliance remains a separate judgement.
13. A declaration, assertion, description, representation, or publication episteme does not create the world-side relation by form.
14. Ordinary use can stop before signatures, explicit occurrence identity, or C.3 kind derivation when the receiving use depends on none of them; typed reuse, occurrence identity, and local-kind quantification are independent thresholds, and none is a prerequisite for another.
15. Relation-declaration slot discipline remains a rule set; its pattern name is not promoted to `U.RelationSlotDiscipline`.
16. A relation fact, an episteme claim, and a locally derived kind are handled by the patterns that define those respective objects without minting `RelationDefinedQualification` or `E.24.RC`.
17. SlotSpecs occur only inside exact `RelationSignature` declarations for direct-relation participant meanings; method-description, operation, plan, work, evaluation, representation, card, schema, and record fields do not become SlotSpecs by shape or label. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant.
18. An A.15.3 planned-filling row may cite an exact SlotSpec, but the planned designation remains plan content and establishes neither an actual participant nor relation obtaining.
19. Interface, port, endpoint, API, and signature language remains available for recognition. The text states what connects, crosses, or is transferred between which entities and recovers the direct-relation definition before declaring SlotSpecs; an unresolved case requires A.6.RSIR or an exact missing-relation result.
20. When source wording calls an entity a result, first determine whether the same entity continued or a new entity began. A separately worded delivery, acceptance, or evaluation claim is opened one at a time with its concrete participants; no pattern catalogue or generic result kind substitutes for that decision.

### A.6.5:8 - Common Failure Modes and Repairs

| Failure | Why it matters | Repair |
|---|---|---|
| `U.RelationSlotDiscipline` treated as a root kind | A rule set is promoted into an unsupported world-side entity. | Keep A.6.5 as the rule set that constrains `SlotSpec` declarations; apply E.24.UK to any future U-kind candidate. |
| Generic `byRef` without an exact RefKind | A later use cannot tell what referent kind can be resolved. | Declare the exact RefKind, or expand the compact sketch next to its use. |
| Reference treated as the relation participant | A storage or publication choice changes the claimed world-side ontology. | Keep the referent as participant; state refMode only for the receiving assertion or description episteme that carries the designation. |
| One SlotSpec contains a ValueKind written as a list of unrelated alternatives | Different predicate semantics are hidden behind one participant meaning. | Recover the real common ValueKind when one exists; otherwise split the relation kind. |
| One source word names a SlotKind, participant ValueKind, reference, and field | A reader cannot tell which object may be substituted, resolved, or renamed. | Split the meanings: use `...Slot` only for the declaration-local SlotKind, `...Ref` only for an admitted RefKind or reference value of that kind, and neither suffix for the participant ValueKind. Keep the source field name and state its explicit correspondence; for example, distinguish `HolderSystemSlot`, `U.System`, and `Robot_7_Ref : U.EntityRef`. |
| Active grammar used as agency evidence | A relation, method, work, structure, or episteme is said to act. | Recover the acting `U.System`; use the patterns that define the relation, Work, Method, and transformation claims. |
| A universal context, taxonomy, scheme, or model-use SlotSpec added to the `U.SystemRoleAssignment` family or every species | Interpretive or receiving-use material is turned into a world-side participant, and several assignment laws are hidden under one root signature. | Give each assignment species only `HolderSystemSlot`, its declaration-local `AssignedSystemRoleKindSlot`, and any additional participant meaning whose value changes the predicate or occurrence identity. Keep a `KindSignature`, taxonomy episteme, scheme, bridge, or model-use structure with the assertion or receiving use unless another relation independently makes it a participant. |
| Interface language erased or promoted | A recognizable source sentence is replaced by either a generic `U.Interface` or an untyped participant catalogue. | Keep the source word for recognition, state what connects, crosses, or is transferred between which exact entities, recover the definition of the direct relation, and declare only the SlotSpecs that a receiving typed use actually reuses. Stop at A.6.RSIR or a missing-relation result when the relation remains undefined. |
| Result-family catalogue | The word `result` triggers a list of possible relation families, so the reader cannot tell which object continued or what claim to make. | Ask whether the same entity continued or a new entity began. For continuation, name the changed characteristic and actual transformation. For inception, require an admitted identity-inception predicate and its definition. If another concrete verb such as `delivered` is present, recover that one relation and its participants. Return the corresponding missing-relation or missing identity-inception result when the needed definition is absent. |
| A participant designation is promoted into a new qualification ontic | A value or reference in an episteme is mistaken for a further world-side object. | Apply the three-way dispatch in A.6.5:4.6: direct relation fact, assertion episteme, or current local participant kind. |
| A method-description, operation, plan, work, evaluation, card, schema, or record field is called a SlotSpec | A reusable direct-relation participant declaration is invented from representation shape or broad wording. | Require the direct-relation definition and one exact `RelationSignature` and SlotSpec. A receiving semantic field is covered by an explicit declaration against that SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant. Handle operation arguments and results under A.6.1 and use the definitions for the other fields. |
| An A.15.3 planned designation is treated as the actual relation participant | Plan content is mistaken for world-side participation and predicate satisfaction. | Keep the row in the WorkPlan; identify any later participant and obtaining relation independently under that relation's definition. |

### A.6.5:9 - Consequences

**Benefits.** Typed relation reuse becomes reviewable without treating an assertion or storage record as the world-side relation. Substitution checks can name the SlotKind and exact participant ValueKind. Reference changes can be distinguished from referent changes. Exact local system-role kinds remain separate from their holder systems and assignment occurrences, and relation predicates remain separate from Work and agency.

**Costs.** Load-bearing relation patterns need exact participant ValueKinds and designation modes. A proposed ValueKind may require a relation-kind split when the direct predicate has different semantics for different participant kinds. Existing compact `byRef` sketches may need adjacent expansion before another pattern can rely on them.

**Limits.** A.6.5 is limited to precise SlotSpec declarations and participant-designation typing. It neither defines the direct obtaining test nor decides a current case. The direct-relation definition supplies the predicate and identity rule, current facts or constituting history supply the case basis, and a claim-bearing episteme states the result. Separate patterns define evidence, reliance, model-use structure selection, and domain-interface semantics.

### A.6.5:10 - Rationale

SlotKind, ValueKind, and RefKind answer three different engineering questions about one `RelationSignature`: **which participant meaning does this declaration distinguish**, **what exact world-side kind must the corresponding actual participant have**, and **how does a receiving assertion or description episteme designate that participant**. Keeping the answers separate is enough to support typed substitution and honest reference use without adding a universal relation record.

The direct-relation definition remains essential. A pair of typed participants does not say whether the relation obtains or whether repeated occurrences with the same participants are identical. Constructive ontology therefore combines logical slot discipline with grounding and domain identity rather than treating a schema as the world.

The predicate boundary prevents a second collapse. Natural language often verbalizes relations, work, methods, and transformations. FPF admits their kinds through direct ontological tests, not through grammar. This keeps only systems as actors and as actual participants corresponding to `HolderSystemSlot`, while preserving the accepted holonhood of work and methods and the separate actual-bounded-change identity of transformations.

### A.6.5:11 - SoTA-Echoing

| Current line | What it contributes | FPF adoption and practical effect |
|---|---|---|
| [Lean 4 reference: structures and fields](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/) | The current official Lean language reference makes each structure field and its type explicit; a later field type may depend on an earlier field. | **Adapt as a formal stress test.** In a SlotSpec, the declaration-local SlotKind and exact participant ValueKind are explicit. FPF does not infer that a Lean structure is a world-side relation or ontic. This disciplines the formal reduced case in A.6.5:5.5, where operand order remains local to the mathematical representation and an explicit correspondence relates operands to `RelationSignature` SlotSpecs before FPF reuse. |
| [TypeDB `relates` statement](https://typedb.com/docs/typeql-reference/statements/relates/) | In current TypeDB 3.x syntax, each external role type is declared through a named relation type, with explicit scope when equal labels occur under different relation types. | **Adapt the declaration locality.** FPF uses `SlotKind`, not `SystemRole`, for the declaration-local name of a participant meaning inside a `RelationSignature`; the exact system-role kind remains the by-value participant under a direct assignment species' `AssignedSystemRoleKindSlot`, and occurrence identity remains with A.2.1 rather than storage identity. This prevents `HolderSystemSlot`, `AssignedSystemRoleKindSlot`, and `InspectorSystemRole` from collapsing in A.6.5:5.1. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/) | The RDF 1.2 Candidate Recommendation of 7 April 2026 distinguishes triple terms, propositions, asserted triples, and reifiers used in further statements. | **Adopt the separation.** A graph term or reifier may represent an assertion, but it does not replace the world-side relation, direct obtaining condition, or SlotSpec. This is the boundary exercised by the episteme case in A.6.5:5.3. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | The current comparison line exposes relation aspects, reification choices, and higher-order typing pressure. | **Use as a stress comparator.** Keep relation occurrence, signature, assertion, and local typed projection distinct without importing the source taxonomy as FPF ontology. This tests the three-way dispatch in A.6.5:4.6 and the result-qualification case in A.6.5:5.4. |

Reopen only the affected rule or worked case when a current source revises a premise used here: declaration locality or field typing; the separation of an assertion, reifier, or representation from the world-side relation; or the higher-order-typing stress on the three-way dispatch. A newer edition by itself does not reopen the pattern.

### A.6.5:12 - Relations

- `A.6.0` defines `U.Signature` and `RelationSignature`; A.6.5 supplies SlotSpec declaration discipline inside their vocabulary declarations.
- `A.6.REL` defines explicit relation-occurrence individuation and the progressive threshold for stable reference.
- `A.6.P` and `A.6.RSIR` recover the direct relation and its participants before slot typing begins.
- Use `A.2.1` for each direct system-role-assignment species' predicate, identity, and participant meanings, and A.6.5 for the exact SlotSpec reading of that species' declaration.
- `C.2.1` defines episteme identity, assertion and description content, and their semantic fields. A receiving semantic field is covered by an explicit declaration against one exact SlotSpec. An external or independently named representation field keeps its source name and requires an explicit C.29 correspondence. Neither route makes the field a SlotSpec or the designation an actual participant.
- `C.3` and `C.3.1` define local participant kinds only when typed quantification or kind order is current.
- `A.15.3` may cite an exact RelationSignature SlotSpec for a planned participant designation; A.15.2/A.15.3 define the planned claim, the direct-relation definition supplies the participant meaning and later actual-participation predicate, and A.6.5 supplies only SlotSpec declaration discipline. Operation arguments and results remain A.6.1 declarations.
- `A.15.1` and `A.3.1` define the constructive holonhood and identity of Work and Methods; `A.3.4` defines the actual-bounded-change identity of transformations; `E.18` defines selected transformation-flow structures over those independently defined transformations and adjacent loci.
- `A.1`, `A.2`, `A.2.1`, and `A.15` keep acting systems, exact local system-role kinds, system-role assignments, Methods, and performed Work distinct.
- Use `A.2.4` for compact episteme evidence-use and status-use relation SlotSpecs, `A.10` for the full evidence-provenance path, and `F.10` for durable status semantics. A.6.5 does not duplicate those relations or make an episteme the holder system, assigned system-role kind, assignment occurrence, or assignment-state relation.
- When one is current, the exact named C.30 architecture-relation subpattern defines the architecture relation. `A.6.M` defines module-interface relations; after `A.6.RSIR` recovery, a non-module interface use follows its direct-relation definition. A.6.5 does not duplicate either family.
- `C.29` defines how tuple components, graph nodes and edges, database fields and rows, and mathematical operands represent a relation, assertion, signature, or occurrence description.
- `E.10` supplies wording-use recovery, `E.24.UK` supplies the U-kind admission test, and `F.18` supplies designation guidance after the object is known.

### A.6.5:End

